#!/usr/bin/env python3
"""
Transcriptomic Gate-Jamming Score (tGJS) — TCGA Pan-Cancer Analysis

Computes a transcriptomic proxy for the Gate-Jamming Score across TCGA
tumor samples and correlates with immune classifications.

tGJS = normalize(HK2) × 0.4 + normalize(BCL2L1) × 0.3 + normalize(TSPO) × 0.3

Data source: cBioPortal REST API (TCGA PanCanAtlas)
Immune subtypes: Thorsson et al. 2018, Immunity

Usage:
    python compute_tgjs.py              # Full analysis
    python compute_tgjs.py --download   # Download data only
    python compute_tgjs.py --plot       # Plot from cached data
"""

import argparse
import json
import os
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import seaborn as sns
from scipy import stats

# === Configuration ===
CBIOPORTAL_API = "https://www.cbioportal.org/api"
STUDY_ID = "pancan_pcawg_2023"  # Pan-cancer study
GENES = ["HK2", "BCL2L1", "TSPO"]  # GJS proxy genes (TSPO = cholesterol translocator)
IMMUNE_GENES = ["CD8A", "IFNG", "CXCL10", "GZMB", "PRF1"]  # Immune markers
STING_GENES = ["CGAS", "STING1", "ENPP1", "TREX1", "CD274"]  # cGAS, STING, erasers, PD-L1
ACUTE_STING = ["IFNB1", "CXCL10", "CCL5"]  # Acute anti-tumor STING signature
CHRONIC_STING = ["IDO1", "TGFB1", "IL6", "ARG1", "NOS2"]  # Chronic immunosuppressive STING
GJS_WEIGHTS = {"HK2": 0.4, "BCL2L1": 0.3, "TSPO": 0.3}

OUTPUT_DIR = Path(__file__).parent
DATA_DIR = OUTPUT_DIR / "data"
PLOT_DIR = OUTPUT_DIR / "figures"


def fetch_available_studies():
    """List TCGA pan-cancer studies on cBioPortal."""
    url = f"{CBIOPORTAL_API}/studies"
    params = {"keyword": "pan_cancer", "projection": "SUMMARY"}
    resp = requests.get(url, params=params, timeout=30)
    resp.raise_for_status()
    studies = resp.json()
    tcga = [s for s in studies if "tcga" in s["studyId"].lower() or "pancan" in s["studyId"].lower()]
    return tcga


def find_best_study():
    """Find the best pan-cancer TCGA study available."""
    url = f"{CBIOPORTAL_API}/studies"
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    studies = resp.json()

    # Prefer these studies in order
    preferred = [
        "pancan_pcawg_2023",
        "pan_origimed_2020",
        "laml_tcga_pan_can_atlas_2018",  # fallback
    ]

    # Find any pan-cancer study with mRNA data
    pancan = [s for s in studies if "pancan" in s["studyId"].lower()
              or "pan_can" in s["studyId"].lower()]

    # Also look for the combined TCGA study
    tcga_all = [s for s in studies if s["studyId"] == "acc_tcga_pan_can_atlas_2018"]

    print(f"Found {len(pancan)} pan-cancer studies")
    for s in pancan[:10]:
        print(f"  {s['studyId']}: {s['name']} ({s.get('allSampleCount', '?')} samples)")

    return pancan


def get_molecular_profiles(study_id):
    """Get mRNA expression profile for a study."""
    url = f"{CBIOPORTAL_API}/molecular-profiles"
    params = {"studyId": study_id}
    try:
        resp = requests.get(url, params=params, timeout=30)
        resp.raise_for_status()
        profiles = resp.json()
        mrna = [p for p in profiles if "mrna" in p["molecularProfileId"].lower()
                or "rna_seq" in p["molecularProfileId"].lower()]
        return mrna
    except Exception:
        return []


def fetch_expression_via_pancan():
    """
    Fetch gene expression across all TCGA PanCanAtlas studies.
    Uses individual TCGA study queries and combines them.
    """
    url = f"{CBIOPORTAL_API}/studies"
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    all_studies = resp.json()

    # Find all TCGA Pan-Cancer Atlas studies
    pancan_studies = [s for s in all_studies
                      if "pan_can_atlas_2018" in s["studyId"]
                      and s.get("allSampleCount", 0) > 0]

    print(f"Found {len(pancan_studies)} TCGA PanCanAtlas studies")

    all_genes = GENES + IMMUNE_GENES + STING_GENES + ACUTE_STING + CHRONIC_STING
    # Deduplicate (CXCL10 appears in both IMMUNE and ACUTE)
    all_genes = list(dict.fromkeys(all_genes))
    all_data = []

    for study in pancan_studies:
        sid = study["studyId"]
        cancer_type = sid.replace("_tcga_pan_can_atlas_2018", "").upper()

        # Find mRNA profile
        profiles_url = f"{CBIOPORTAL_API}/molecular-profiles"
        try:
            presp = requests.get(profiles_url, params={"studyId": sid}, timeout=15)
            presp.raise_for_status()
            profiles = presp.json()
        except Exception:
            continue

        mrna_profiles = [p for p in profiles
                         if "rna_seq_v2_mrna" in p["molecularProfileId"]
                         and sid in p["molecularProfileId"]]
        if not mrna_profiles:
            mrna_profiles = [p for p in profiles
                             if "mrna" in p["molecularProfileId"].lower()
                             and sid in p["molecularProfileId"]]
        if not mrna_profiles:
            continue

        profile_id = mrna_profiles[0]["molecularProfileId"]
        sample_list_id = f"{sid}_all"

        # Resolve gene Entrez IDs once
        gene_url = f"{CBIOPORTAL_API}/genes"

        for gene_symbol in all_genes:
            try:
                gresp = requests.get(f"{gene_url}/{gene_symbol}", timeout=10)
                gresp.raise_for_status()
                gene_info = gresp.json()
                entrez_id = gene_info["entrezGeneId"]

                # Fetch all samples for this gene
                sample_url = f"{CBIOPORTAL_API}/molecular-profiles/{profile_id}/molecular-data"
                sresp = requests.get(sample_url,
                                     params={"sampleListId": sample_list_id,
                                             "entrezGeneId": entrez_id},
                                     timeout=30)
                sresp.raise_for_status()
                samples = sresp.json()

                for s in samples:
                    all_data.append({
                        "sample_id": s["sampleId"],
                        "patient_id": s.get("patientId", ""),
                        "study_id": sid,
                        "cancer_type": cancer_type,
                        "gene": gene_symbol,
                        "value": s["value"]
                    })

            except Exception as e:
                print(f"  Warning: {gene_symbol} in {sid}: {e}")
                continue

        n_samples = len([d for d in all_data if d["study_id"] == sid and d["gene"] == "HK2"])
        print(f"  {cancer_type}: {n_samples} samples from {profile_id}")

    df = pd.DataFrame(all_data)
    return df


def download_data():
    """Download TCGA expression data and save locally."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    cache_file = DATA_DIR / "tcga_expression_raw.parquet"
    if cache_file.exists():
        print(f"Using cached data: {cache_file}")
        return pd.read_parquet(cache_file)

    print("Downloading TCGA PanCanAtlas expression data from cBioPortal...")
    print("This may take a few minutes...\n")

    df = fetch_expression_via_pancan()

    if len(df) == 0:
        print("ERROR: No data retrieved. Check network connection.")
        sys.exit(1)

    df.to_parquet(cache_file)
    print(f"\nSaved {len(df)} data points to {cache_file}")

    # Summary
    n_samples = df["sample_id"].nunique()
    n_cancers = df["cancer_type"].nunique()
    print(f"Total: {n_samples} samples across {n_cancers} cancer types")

    return df


def compute_tgjs(df):
    """Compute transcriptomic GJS from expression data."""
    # Pivot to get genes as columns
    expr = df[df["gene"].isin(GENES)].pivot_table(
        index=["sample_id", "cancer_type", "study_id"],
        columns="gene",
        values="value",
        aggfunc="first"
    ).reset_index()

    # Drop samples missing any GJS gene
    expr = expr.dropna(subset=GENES)

    # Min-max normalize each gene within the full cohort
    for gene in GENES:
        vals = expr[gene]
        expr[f"{gene}_norm"] = (vals - vals.min()) / (vals.max() - vals.min())

    # Compute tGJS
    expr["tGJS"] = (
        expr["HK2_norm"] * GJS_WEIGHTS["HK2"] +
        expr["BCL2L1_norm"] * GJS_WEIGHTS["BCL2L1"] +
        expr["TSPO_norm"] * GJS_WEIGHTS["TSPO"]
    )

    return expr


def add_immune_markers(expr_df, raw_df):
    """Add immune marker expression to the tGJS dataframe."""
    immune_data = raw_df[raw_df["gene"].isin(IMMUNE_GENES)].pivot_table(
        index="sample_id",
        columns="gene",
        values="value",
        aggfunc="first"
    ).reset_index()

    merged = expr_df.merge(immune_data, on="sample_id", how="left")
    return merged


def correlate_immune(df):
    """Compute correlations between tGJS and immune markers."""
    results = []
    for gene in IMMUNE_GENES:
        if gene not in df.columns:
            continue
        subset = df[["tGJS", gene]].dropna()
        if len(subset) < 10:
            continue
        rho, pval = stats.spearmanr(subset["tGJS"], subset[gene])
        results.append({
            "immune_marker": gene,
            "spearman_rho": round(rho, 4),
            "p_value": pval,
            "n": len(subset),
            "significant": pval < 0.01
        })

    return pd.DataFrame(results)


def compute_sting_ratio(df):
    """Compute acute/chronic STING ratio and correlate with tGJS."""
    # Check which genes are available
    acute_avail = [g for g in ACUTE_STING if g in df.columns and df[g].notna().sum() > 100]
    chronic_avail = [g for g in CHRONIC_STING if g in df.columns and df[g].notna().sum() > 100]

    if len(acute_avail) < 2 or len(chronic_avail) < 2:
        print(f"  Insufficient STING genes (acute: {acute_avail}, chronic: {chronic_avail})")
        return df, {}

    # Compute mean z-scored signatures
    for gene in acute_avail + chronic_avail:
        vals = df[gene].dropna()
        df[f"{gene}_z"] = (df[gene] - vals.mean()) / vals.std()

    acute_cols = [f"{g}_z" for g in acute_avail]
    chronic_cols = [f"{g}_z" for g in chronic_avail]

    df["acute_sting"] = df[acute_cols].mean(axis=1)
    df["chronic_sting"] = df[chronic_cols].mean(axis=1)

    # Ratio: positive = acute-dominant, negative = chronic-dominant
    df["sting_ratio"] = df["acute_sting"] - df["chronic_sting"]

    # Correlate
    results = {}
    for col, label in [("acute_sting", "Acute STING"), ("chronic_sting", "Chronic STING"),
                        ("sting_ratio", "STING Ratio (acute-chronic)")]:
        subset = df[["tGJS", col]].dropna()
        if len(subset) > 10:
            rho, pval = stats.spearmanr(subset["tGJS"], subset[col])
            results[label] = {"rho": round(rho, 4), "p": pval, "n": len(subset)}
            print(f"  tGJS vs {label}: ρ = {rho:.4f}, p = {pval:.2e}")

    # ENPP1 and TREX1 correlations (cGAMP/DNA erasers)
    for gene in ["ENPP1", "TREX1", "CD274", "CGAS", "STING1"]:
        if gene in df.columns:
            subset = df[["tGJS", gene]].dropna()
            if len(subset) > 10:
                rho, pval = stats.spearmanr(subset["tGJS"], subset[gene])
                label = {"ENPP1": "ENPP1 (cGAMP eraser)", "TREX1": "TREX1 (DNA eraser)",
                         "CD274": "CD274/PD-L1", "CGAS": "cGAS", "STING1": "STING1"}.get(gene, gene)
                results[label] = {"rho": round(rho, 4), "p": pval, "n": len(subset)}
                print(f"  tGJS vs {label}: ρ = {rho:.4f}, p = {pval:.2e}")

    return df, results


def cancer_type_analysis(df):
    """Compute mean tGJS per cancer type and rank."""
    ct = df.groupby("cancer_type").agg(
        mean_tGJS=("tGJS", "mean"),
        median_tGJS=("tGJS", "median"),
        std_tGJS=("tGJS", "std"),
        n_samples=("tGJS", "count"),
        mean_HK2=("HK2", "mean"),
        mean_BCL2L1=("BCL2L1", "mean"),
        mean_TSPO=("TSPO", "mean"),
    ).reset_index()

    ct = ct.sort_values("mean_tGJS", ascending=False)

    # Add known ICI response rates (approximate, from literature)
    ici_response = {
        "SKCM": 0.40,   # melanoma
        "LUAD": 0.20,   # lung adeno
        "LUSC": 0.20,   # lung squamous
        "BLCA": 0.21,   # bladder
        "HNSC": 0.16,   # head & neck
        "KIRC": 0.25,   # kidney clear cell
        "STAD": 0.15,   # gastric
        "LIHC": 0.17,   # liver
        "COAD": 0.05,   # colon (MSS)
        "READ": 0.05,   # rectal (MSS)
        "PAAD": 0.03,   # pancreatic
        "GBM": 0.08,    # glioblastoma
        "LGG": 0.05,    # low-grade glioma
        "BRCA": 0.12,   # breast (overall)
        "OV": 0.08,     # ovarian
        "PRAD": 0.05,   # prostate
        "UCEC": 0.15,   # endometrial (overall)
        "LAML": 0.10,   # AML
    }
    ct["ici_response_rate"] = ct["cancer_type"].map(ici_response)

    return ct


def plot_results(df, ct_df, corr_df):
    """Generate all figures."""
    PLOT_DIR.mkdir(parents=True, exist_ok=True)
    sns.set_style("whitegrid")
    sns.set_context("paper", font_scale=1.2)

    # Figure 1: tGJS distribution by cancer type
    fig, ax = plt.subplots(figsize=(14, 8))
    order = ct_df.sort_values("mean_tGJS", ascending=True)["cancer_type"].tolist()
    # Only plot cancer types with enough samples
    order = [c for c in order if ct_df[ct_df["cancer_type"] == c]["n_samples"].values[0] >= 20]
    plot_df = df[df["cancer_type"].isin(order)]

    sns.boxplot(data=plot_df, x="cancer_type", y="tGJS", order=order,
                color="steelblue", fliersize=1, ax=ax)
    ax.set_xlabel("Cancer Type (TCGA)")
    ax.set_ylabel("Transcriptomic GJS (tGJS)")
    ax.set_title("Gate-Jamming Score Distribution Across TCGA Cancer Types")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    fig.savefig(PLOT_DIR / "fig1_tgjs_by_cancer_type.png", dpi=300)
    fig.savefig(PLOT_DIR / "fig1_tgjs_by_cancer_type.svg")
    plt.close()
    print(f"Saved: fig1_tgjs_by_cancer_type.png/svg")

    # Figure 2: tGJS vs ICI response rate by cancer type
    ct_ici = ct_df.dropna(subset=["ici_response_rate"])
    if len(ct_ici) >= 5:
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.scatter(ct_ici["mean_tGJS"], ct_ici["ici_response_rate"],
                   s=ct_ici["n_samples"] / 5, alpha=0.7, c="steelblue", edgecolors="black")

        for _, row in ct_ici.iterrows():
            ax.annotate(row["cancer_type"],
                        (row["mean_tGJS"], row["ici_response_rate"]),
                        fontsize=8, ha="center", va="bottom")

        rho, pval = stats.spearmanr(ct_ici["mean_tGJS"], ct_ici["ici_response_rate"])
        ax.set_xlabel("Mean tGJS")
        ax.set_ylabel("Approximate ICI Response Rate")
        ax.set_title(f"tGJS vs Checkpoint Inhibitor Response\n(Spearman ρ = {rho:.3f}, p = {pval:.4f})")
        plt.tight_layout()
        fig.savefig(PLOT_DIR / "fig2_tgjs_vs_ici_response.png", dpi=300)
        fig.savefig(PLOT_DIR / "fig2_tgjs_vs_ici_response.svg")
        plt.close()
        print(f"Saved: fig2_tgjs_vs_ici_response.png/svg")

    # Figure 3: tGJS vs immune markers (scatter + correlation)
    available_immune = [g for g in IMMUNE_GENES if g in df.columns and df[g].notna().sum() > 100]
    if available_immune:
        n_markers = len(available_immune)
        fig, axes = plt.subplots(1, n_markers, figsize=(5 * n_markers, 5))
        if n_markers == 1:
            axes = [axes]

        for ax, gene in zip(axes, available_immune):
            subset = df[["tGJS", gene]].dropna()
            # Downsample for plotting if too many points
            if len(subset) > 2000:
                subset = subset.sample(2000, random_state=42)

            ax.scatter(subset["tGJS"], subset[gene], alpha=0.1, s=3, c="steelblue")
            rho, pval = stats.spearmanr(subset["tGJS"], subset[gene])
            ax.set_xlabel("tGJS")
            ax.set_ylabel(f"{gene} expression")
            ax.set_title(f"ρ = {rho:.3f}, p = {pval:.2e}")

            # Add regression line
            z = np.polyfit(subset["tGJS"], subset[gene], 1)
            p = np.poly1d(z)
            x_line = np.linspace(subset["tGJS"].min(), subset["tGJS"].max(), 100)
            ax.plot(x_line, p(x_line), "r-", linewidth=2, alpha=0.8)

        plt.suptitle("tGJS vs Immune Markers (TCGA Pan-Cancer)", fontsize=14, y=1.02)
        plt.tight_layout()
        fig.savefig(PLOT_DIR / "fig3_tgjs_vs_immune_markers.png", dpi=300, bbox_inches="tight")
        fig.savefig(PLOT_DIR / "fig3_tgjs_vs_immune_markers.svg", bbox_inches="tight")
        plt.close()
        print(f"Saved: fig3_tgjs_vs_immune_markers.png/svg")

    # Figure 4: Component heatmap by cancer type
    components = ct_df[ct_df["n_samples"] >= 20][["cancer_type", "mean_HK2", "mean_BCL2L1", "mean_TSPO", "mean_tGJS"]].copy()
    components = components.sort_values("mean_tGJS", ascending=False)
    if len(components) >= 5:
        fig, ax = plt.subplots(figsize=(8, max(6, len(components) * 0.4)))

        # Normalize for heatmap display
        for col in ["mean_HK2", "mean_BCL2L1", "mean_TSPO"]:
            vals = components[col]
            components[col + "_norm"] = (vals - vals.min()) / (vals.max() - vals.min())

        heatmap_data = components.set_index("cancer_type")[
            ["mean_HK2_norm", "mean_BCL2L1_norm", "mean_TSPO_norm"]
        ]
        heatmap_data.columns = ["HK2 (×0.4)", "BCL2L1 (×0.3)", "TSPO (×0.3)"]

        sns.heatmap(heatmap_data, annot=True, fmt=".2f", cmap="YlOrRd",
                    ax=ax, cbar_kws={"label": "Normalized Expression"})
        ax.set_title("GJS Component Expression by Cancer Type")
        ax.set_ylabel("")
        plt.tight_layout()
        fig.savefig(PLOT_DIR / "fig4_gjs_components_heatmap.png", dpi=300)
        fig.savefig(PLOT_DIR / "fig4_gjs_components_heatmap.svg")
        plt.close()
        print(f"Saved: fig4_gjs_components_heatmap.png/svg")


def save_results(df, ct_df, corr_df, sting_results=None):
    """Save analysis results."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Save tGJS per sample
    df.to_csv(DATA_DIR / "tgjs_per_sample.csv", index=False)

    # Save cancer type summary
    ct_df.to_csv(DATA_DIR / "tgjs_by_cancer_type.csv", index=False)

    # Save correlations
    if len(corr_df) > 0:
        corr_df.to_csv(DATA_DIR / "tgjs_immune_correlations.csv", index=False)

    # Save summary stats
    summary = {
        "total_samples": len(df),
        "cancer_types": int(df["cancer_type"].nunique()),
        "mean_tGJS": round(float(df["tGJS"].mean()), 4),
        "std_tGJS": round(float(df["tGJS"].std()), 4),
        "correlations": corr_df.to_dict("records") if len(corr_df) > 0 else [],
        "top5_high_gjs": ct_df.head(5)[["cancer_type", "mean_tGJS", "n_samples"]].to_dict("records"),
        "top5_low_gjs": ct_df.tail(5)[["cancer_type", "mean_tGJS", "n_samples"]].to_dict("records"),
    }

    # Add STING analysis if available
    if sting_results:
        summary["sting_analysis"] = sting_results

    # Add ICI correlation if available
    ct_ici = ct_df.dropna(subset=["ici_response_rate"])
    if len(ct_ici) >= 5:
        rho, pval = stats.spearmanr(ct_ici["mean_tGJS"], ct_ici["ici_response_rate"])
        summary["ici_correlation"] = {
            "spearman_rho": round(float(rho), 4),
            "p_value": float(pval),
            "n_cancer_types": len(ct_ici),
            "prediction": "CONFIRMED" if rho < -0.3 and pval < 0.05 else "NOT CONFIRMED"
        }

    with open(DATA_DIR / "tgjs_analysis_summary.json", "w") as f:
        json.dump(summary, f, indent=2)

    print(f"\nResults saved to {DATA_DIR}/")


def main():
    parser = argparse.ArgumentParser(description="TCGA tGJS Analysis")
    parser.add_argument("--download", action="store_true", help="Download data only")
    parser.add_argument("--plot", action="store_true", help="Plot from cached data")
    args = parser.parse_args()

    print("=" * 60)
    print("TRANSCRIPTOMIC GATE-JAMMING SCORE — TCGA PAN-CANCER")
    print("=" * 60)
    print()

    # Step 1: Download/load data
    raw_df = download_data()
    if args.download:
        return

    # Step 2: Compute tGJS
    print("\nComputing tGJS...")
    expr_df = compute_tgjs(raw_df)
    print(f"  tGJS computed for {len(expr_df)} samples")
    print(f"  Mean tGJS: {expr_df['tGJS'].mean():.4f} ± {expr_df['tGJS'].std():.4f}")

    # Step 3: Add immune markers
    print("\nAdding immune markers...")
    full_df = add_immune_markers(expr_df, raw_df)

    # Step 4: Correlate with immune markers
    print("\nCorrelating tGJS with immune markers...")
    corr_df = correlate_immune(full_df)
    if len(corr_df) > 0:
        print(corr_df.to_string(index=False))

    # Step 4a.5: Add STING panel + acute/chronic genes
    print("\nAdding STING panel and acute/chronic signature genes...")
    sting_all = STING_GENES + ACUTE_STING + CHRONIC_STING
    sting_all = list(dict.fromkeys(sting_all))  # deduplicate
    sting_data = raw_df[raw_df["gene"].isin(sting_all)].pivot_table(
        index="sample_id", columns="gene", values="value", aggfunc="first"
    ).reset_index()
    # Only merge columns not already present
    new_cols = [c for c in sting_data.columns if c not in full_df.columns or c == "sample_id"]
    full_df = full_df.merge(sting_data[new_cols], on="sample_id", how="left")

    # Step 4b: STING ratio and eraser gene analysis
    print("\nComputing acute/chronic STING ratio and eraser correlations...")
    full_df, sting_results = compute_sting_ratio(full_df)

    # Step 5: Cancer type analysis
    print("\nCancer type analysis...")
    ct_df = cancer_type_analysis(full_df)
    print("\nTop 10 highest tGJS cancer types:")
    print(ct_df.head(10)[["cancer_type", "mean_tGJS", "n_samples", "ici_response_rate"]].to_string(index=False))
    print("\nTop 10 lowest tGJS cancer types:")
    print(ct_df.tail(10)[["cancer_type", "mean_tGJS", "n_samples", "ici_response_rate"]].to_string(index=False))

    # ICI correlation
    ct_ici = ct_df.dropna(subset=["ici_response_rate"])
    if len(ct_ici) >= 5:
        rho, pval = stats.spearmanr(ct_ici["mean_tGJS"], ct_ici["ici_response_rate"])
        print(f"\n*** tGJS vs ICI response rate: Spearman ρ = {rho:.4f}, p = {pval:.4f} ***")
        if rho < -0.3 and pval < 0.05:
            print(">>> PREDICTION CONFIRMED: tGJS inversely correlates with ICI response <<<")
        elif rho < 0:
            print(">>> TREND in predicted direction but not significant <<<")
        else:
            print(">>> PREDICTION NOT CONFIRMED: no inverse correlation <<<")

    # Step 6: Save and plot
    save_results(full_df, ct_df, corr_df, sting_results=sting_results)
    plot_results(full_df, ct_df, corr_df)

    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
