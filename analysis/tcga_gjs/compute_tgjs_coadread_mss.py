#!/usr/bin/env python3
"""
Transcriptomic Gate-Jamming Score (tGJS) — COADREAD MSS-Stratified Deep Dive
Supplementary Analysis S2

This script tests the GJS hypothesis in its strongest domain: MSS/MSI-L colorectal
tumors, where VDAC1-mediated mtDNA release is the dominant source of cytosolic DNA
reaching cGAS (unlike MSI-H tumors where genomic instability creates a parallel flood).

Strata:
  1. MSS/MSI-L + TP53-wildtype  — the "clean room"
  2. MSS/MSI-L + TP53-mutant    — gate-jamming + broken apoptosis
  3. MSI-H + TP53-wildtype      — genomic instability control
  4. MSI-H + TP53-mutant        — maximum chaos

Primary hypothesis: In stratum 1, tGJS negatively correlates with immune infiltration
(sign flip vs pan-cancer positive correlation).

Data sources:
  - Expression: cached parquet (analysis/tcga_gjs/data/tcga_expression_raw.parquet)
  - Extra genes: cBioPortal REST API (coadread_tcga_pan_can_atlas_2018)
  - Clinical: cBioPortal REST API (MSI status, TP53 mutation)
  - ESTIMATE: pre-computed from MD Anderson or ssGSEA fallback

Usage:
    python compute_tgjs_coadread_mss.py           # Full analysis
    python compute_tgjs_coadread_mss.py --cache   # Use all local caches, skip API calls
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
import requests
import seaborn as sns
from scipy import stats

# ─── Configuration ────────────────────────────────────────────────────────────
CBIOPORTAL_API = "https://www.cbioportal.org/api"
STUDY_ID = "coadread_tcga_pan_can_atlas_2018"

GJS_GENES    = ["HK2", "BCL2L1", "TSPO"]
GJS_WEIGHTS  = {"HK2": 0.4, "BCL2L1": 0.3, "TSPO": 0.3}

IMMUNE_GENES = ["CD8A", "IFNG", "CXCL10", "GZMB", "PRF1"]
EXHAUST_GENES = ["HAVCR2", "LAG3", "PDCD1", "TIGIT"]        # need API fetch
EFFECTOR_GENES = ["GZMB", "PRF1", "IFNG"]                   # for E/E ratio

STING_GENES  = ["CGAS", "STING1", "ENPP1", "TREX1", "CD274"]
ACUTE_STING  = ["IFNB1", "CXCL10", "CCL5"]
CHRONIC_STING = ["IDO1", "TGFB1", "IL6", "ARG1", "NOS2"]

# All extra genes not in parquet that need API fetch
EXTRA_GENES  = list(dict.fromkeys(EXHAUST_GENES))

STRATUM_LABELS = {
    "MSS_TP53wt":  "MSS/MSI-L + TP53-wt",
    "MSS_TP53mut": "MSS/MSI-L + TP53-mut",
    "MSIH_TP53wt": "MSI-H + TP53-wt",
    "MSIH_TP53mut":"MSI-H + TP53-mut",
}
STRATUM_COLORS = {
    "MSS_TP53wt":  "#2196F3",
    "MSS_TP53mut": "#FF9800",
    "MSIH_TP53wt": "#4CAF50",
    "MSIH_TP53mut":"#9C27B0",
}

SCRIPT_DIR = Path(__file__).parent
DATA_DIR   = SCRIPT_DIR / "data" / "coadread_mss"
PLOT_DIR   = SCRIPT_DIR / "figures" / "coadread_mss"
CACHE_DIR  = SCRIPT_DIR / "data"

# ─── Utilities ────────────────────────────────────────────────────────────────

def api_get(url, params=None, timeout=30, retries=3):
    """GET with retry and basic rate-limit handling."""
    for attempt in range(retries):
        try:
            r = requests.get(url, params=params, timeout=timeout)
            if r.status_code == 429:
                time.sleep(2 ** attempt)
                continue
            r.raise_for_status()
            return r.json()
        except requests.exceptions.Timeout:
            if attempt == retries - 1:
                raise
            time.sleep(2)
        except requests.exceptions.RequestException as e:
            if attempt == retries - 1:
                raise
            time.sleep(1)
    return None


def bonferroni_correct(p_values, n_tests):
    """Apply Bonferroni correction."""
    return [min(p * n_tests, 1.0) for p in p_values]


# ─── Step 1: Clinical Annotations ─────────────────────────────────────────────

def fetch_clinical_data():
    """Fetch MSI status and TP53 mutation for all COADREAD samples."""
    cache_path = DATA_DIR / "coadread_clinical.csv"
    if cache_path.exists():
        print(f"  Loading clinical data from cache: {cache_path}")
        return pd.read_csv(cache_path)

    print("  Fetching clinical data from cBioPortal...")

    # ── MSI status ──────────────────────────────────────────────────────────
    msi_attrs = ["MSI_STATUS_7_CATEGORY_CONSENSUS_CALLS",
                 "MSI_SCORE_MANTIS", "MSI_SENSOR_SCORE",
                 "MICROSATELLITE_INSTABILITY_ADJ_STRAND_BIAS"]
    msi_records = {}

    for attr in msi_attrs:
        try:
            url = f"{CBIOPORTAL_API}/studies/{STUDY_ID}/clinical-data"
            data = api_get(url, params={"clinicalDataType": "SAMPLE",
                                         "attributeId": attr}, timeout=45)
            if data:
                for rec in data:
                    sid = rec["sampleId"][:15]
                    if sid not in msi_records:
                        msi_records[sid] = {}
                    msi_records[sid][attr] = rec["value"]
                print(f"    {attr}: {len(data)} records")
        except Exception as e:
            print(f"    {attr}: {e}")

    # ── TP53 mutations ───────────────────────────────────────────────────────
    tp53_mutants = set()
    try:
        # Get TP53 Entrez ID
        gene_info = api_get(f"{CBIOPORTAL_API}/genes/TP53")
        entrez_id = gene_info["entrezGeneId"]

        # Get mutation profile — must belong to STUDY_ID
        profiles = api_get(f"{CBIOPORTAL_API}/molecular-profiles",
                           params={"studyId": STUDY_ID})
        mut_profile = next(
            (p["molecularProfileId"] for p in profiles
             if "mutation" in p["molecularProfileId"]
             and STUDY_ID in p["molecularProfileId"]), None
        )
        if mut_profile:
            sample_list = f"{STUDY_ID}_all"
            mutations = api_get(
                f"{CBIOPORTAL_API}/molecular-profiles/{mut_profile}/mutations",
                params={"sampleListId": sample_list,
                        "entrezGeneId": entrez_id},
                timeout=60
            )
            if mutations:
                for m in mutations:
                    mtype = m.get("mutationType", "")
                    # Exclude silent/synonymous
                    if mtype.lower() not in ("silent", "synonymous_variant", "3'utr", "5'utr"):
                        tp53_mutants.add(m["sampleId"][:15])
                print(f"    TP53 non-silent mutations: {len(tp53_mutants)} samples")
    except Exception as e:
        print(f"    TP53 fetch failed: {e}")

    # ── Assemble clinical table ──────────────────────────────────────────────
    # Get all samples in the study
    try:
        samples_data = api_get(f"{CBIOPORTAL_API}/studies/{STUDY_ID}/samples",
                               timeout=45)
        all_sample_ids = [s["sampleId"][:15] for s in samples_data]
    except Exception as e:
        print(f"    Sample list fetch failed: {e}")
        all_sample_ids = list(msi_records.keys())

    records = []
    for sid in all_sample_ids:
        row = {"sample_id": sid}
        mr = msi_records.get(sid, {})

        # Classify MSI status
        msi_status = "UNKNOWN"
        consensus = mr.get("MSI_STATUS_7_CATEGORY_CONSENSUS_CALLS", "")
        if consensus:
            if "MSI-H" in consensus.upper() or consensus.upper() in ("MSI_H", "MSI-H", "HIGH"):
                msi_status = "MSI-H"
            elif consensus.upper() in ("MSS", "MSI-L", "MSI_L", "LOW"):
                msi_status = "MSS"
        else:
            # Fall back to numeric scores
            try:
                mantis = float(mr.get("MSI_SCORE_MANTIS", "nan"))
                if mantis > 0.4:
                    msi_status = "MSI-H"
                elif mantis <= 0.4:
                    msi_status = "MSS"
            except ValueError:
                pass
            if msi_status == "UNKNOWN":
                try:
                    sensor = float(mr.get("MSI_SENSOR_SCORE", "nan"))
                    if sensor > 10:
                        msi_status = "MSI-H"
                    elif sensor <= 10:
                        msi_status = "MSS"
                except ValueError:
                    pass

        row["msi_status"] = msi_status
        row["tp53_status"] = "mutant" if sid in tp53_mutants else "wildtype"
        row["mantis_score"] = mr.get("MSI_SCORE_MANTIS", np.nan)
        row["sensor_score"] = mr.get("MSI_SENSOR_SCORE", np.nan)
        records.append(row)

    clinical = pd.DataFrame(records)
    print(f"\n  MSI status distribution:")
    print(clinical["msi_status"].value_counts().to_string())
    print(f"\n  TP53 status distribution:")
    print(clinical["tp53_status"].value_counts().to_string())

    clinical.to_csv(cache_path, index=False)
    return clinical


# ─── Step 2: Fetch Extra Genes from cBioPortal ────────────────────────────────

def fetch_extra_genes(sample_ids):
    """
    Fetch exhaustion marker expression (HAVCR2, LAG3, PDCD1, TIGIT)
    from cBioPortal for COADREAD.
    """
    cache_path = DATA_DIR / "coadread_extra_genes.csv"
    if cache_path.exists():
        print(f"  Loading extra genes from cache: {cache_path}")
        return pd.read_csv(cache_path)

    print(f"  Fetching exhaustion genes from cBioPortal: {EXTRA_GENES}")

    # Get mRNA profile — must belong to STUDY_ID to avoid cross-study contamination
    profiles = api_get(f"{CBIOPORTAL_API}/molecular-profiles",
                       params={"studyId": STUDY_ID})
    mrna_profile = next(
        (p["molecularProfileId"] for p in profiles
         if "rna_seq_v2_mrna" in p["molecularProfileId"]
         and STUDY_ID in p["molecularProfileId"]), None
    )
    if not mrna_profile:
        mrna_profile = next(
            (p["molecularProfileId"] for p in profiles
             if "mrna" in p["molecularProfileId"].lower()
             and STUDY_ID in p["molecularProfileId"]), None
        )
    if not mrna_profile:
        print("  WARNING: No mRNA profile found. Exhaustion genes will be missing.")
        return pd.DataFrame({"sample_id": sample_ids})

    print(f"  Using profile: {mrna_profile}")
    sample_list_id = f"{STUDY_ID}_all"

    all_rows = []
    for gene in EXTRA_GENES:
        try:
            gene_info = api_get(f"{CBIOPORTAL_API}/genes/{gene}")
            entrez_id = gene_info["entrezGeneId"]

            data = api_get(
                f"{CBIOPORTAL_API}/molecular-profiles/{mrna_profile}/molecular-data",
                params={"sampleListId": sample_list_id, "entrezGeneId": entrez_id},
                timeout=45
            )
            if data:
                for rec in data:
                    all_rows.append({
                        "sample_id": rec["sampleId"][:15],
                        "gene": gene,
                        "value": rec["value"]
                    })
                print(f"    {gene}: {len(data)} samples")
        except Exception as e:
            print(f"    {gene}: failed — {e}")

    if not all_rows:
        return pd.DataFrame({"sample_id": sample_ids})

    long_df = pd.DataFrame(all_rows)
    wide_df = long_df.pivot_table(index="sample_id", columns="gene",
                                   values="value", aggfunc="first").reset_index()
    wide_df.to_csv(cache_path, index=False)
    return wide_df


# ─── Step 3: Load and subset COADREAD expression ──────────────────────────────

def load_coadread_expression():
    """Load COADREAD from parquet and pivot to wide format."""
    parquet_path = CACHE_DIR / "tcga_expression_raw.parquet"
    print(f"  Loading from: {parquet_path}")
    raw = pd.read_parquet(parquet_path)

    coad = raw[raw["cancer_type"] == "COADREAD"].copy()
    coad["sample_id"] = coad["sample_id"].str[:15]

    # Pivot to wide
    wide = coad.pivot_table(
        index=["sample_id", "patient_id", "study_id", "cancer_type"],
        columns="gene",
        values="value",
        aggfunc="first"
    ).reset_index()

    print(f"  COADREAD samples: {len(wide)}")
    print(f"  Available genes: {[c for c in wide.columns if c not in ['sample_id','patient_id','study_id','cancer_type']]}")
    return wide


# ─── Step 4: ESTIMATE Scores ──────────────────────────────────────────────────

def fetch_estimate_scores(sample_ids):
    """
    Try to get pre-computed ESTIMATE scores.
    Falls back to simple ssGSEA-like proxy using available immune genes.
    """
    cache_path = DATA_DIR / "coadread_estimate.csv"
    if cache_path.exists():
        print(f"  Loading ESTIMATE scores from cache: {cache_path}")
        return pd.read_csv(cache_path)

    print("  Attempting to fetch pre-computed ESTIMATE scores...")

    # ESTIMATE scores are not available via a simple API; we build a proxy
    # using ssGSEA with a subset of the ESTIMATE immune gene signature
    # available in the parquet (CD8A, IFNG, CXCL10, GZMB, PRF1).
    #
    # This is NOT the full 141-gene ESTIMATE immune score, but it captures
    # the same core biology (cytotoxic immune infiltration).
    # Label clearly as "Immune Proxy Score" not "ESTIMATE Immune Score".

    print("  Pre-computed ESTIMATE not available via API.")
    print("  Computing immune proxy score from available cytotoxic immune genes.")
    print("  Note: This is NOT the official ESTIMATE score — label as 'Immune Proxy'.")

    # Return empty; will be computed from expression data in main flow
    return pd.DataFrame({"sample_id": sample_ids})


# ─── Step 5: Compute tGJS (rank-normalized within COADREAD) ───────────────────

def compute_tgjs_coadread(expr_df):
    """
    Compute tGJS with rank-based normalization within COADREAD.
    Rank normalization is more robust than min-max for small cohorts.
    """
    df = expr_df.copy()
    n = len(df)

    for gene in GJS_GENES:
        if gene not in df.columns:
            raise ValueError(f"Missing GJS gene: {gene}")
        # Rank normalize: 0 to 1
        df[f"{gene}_norm"] = df[gene].rank(method="average") / n

    df["tGJS"] = (
        df["HK2_norm"]    * GJS_WEIGHTS["HK2"] +
        df["BCL2L1_norm"] * GJS_WEIGHTS["BCL2L1"] +
        df["TSPO_norm"]   * GJS_WEIGHTS["TSPO"]
    )
    return df


# ─── Step 6: Assign Strata ────────────────────────────────────────────────────

def assign_strata(expr_df, clinical_df):
    """Merge clinical annotations and assign stratum labels."""
    merged = expr_df.merge(
        clinical_df[["sample_id", "msi_status", "tp53_status",
                      "mantis_score", "sensor_score"]],
        on="sample_id", how="left"
    )

    def get_stratum(row):
        msi = row["msi_status"]
        tp53 = row["tp53_status"]
        if msi == "UNKNOWN":
            return "UNKNOWN"
        is_msih = (msi == "MSI-H")
        is_mut  = (tp53 == "mutant")
        if not is_msih and not is_mut:
            return "MSS_TP53wt"
        elif not is_msih and is_mut:
            return "MSS_TP53mut"
        elif is_msih and not is_mut:
            return "MSIH_TP53wt"
        else:
            return "MSIH_TP53mut"

    merged["stratum"] = merged.apply(get_stratum, axis=1)

    print("\n  Stratum counts:")
    counts = merged["stratum"].value_counts()
    for s, label in STRATUM_LABELS.items():
        n = counts.get(s, 0)
        flag = " ⚠ < 20" if n < 20 else ""
        print(f"    {label}: N = {n}{flag}")
    n_unknown = counts.get("UNKNOWN", 0)
    if n_unknown:
        print(f"    Unknown MSI: N = {n_unknown} (excluded from stratified analysis)")

    return merged


# ─── Step 7: Compute Immune Proxy and Derived Signatures ─────────────────────

def compute_derived_signatures(df):
    """Compute composite scores from individual genes."""

    # Immune proxy score: mean z-score of cytotoxic immune genes
    immune_avail = [g for g in IMMUNE_GENES if g in df.columns and df[g].notna().sum() > 5]
    if immune_avail:
        for g in immune_avail:
            vals = df[g].dropna()
            df[f"{g}_z"] = (df[g] - vals.mean()) / vals.std()
        df["immune_proxy"] = df[[f"{g}_z" for g in immune_avail]].mean(axis=1)

    # Exhaustion score
    exhaust_avail = [g for g in EXHAUST_GENES if g in df.columns and df[g].notna().sum() > 5]
    if exhaust_avail:
        for g in exhaust_avail:
            vals = df[g].dropna()
            df[f"{g}_z"] = (df[g] - vals.mean()) / vals.std()
        df["exhaustion_score"] = df[[f"{g}_z" for g in exhaust_avail]].mean(axis=1)

    # Effector / Exhaustion ratio
    effector_avail = [g for g in EFFECTOR_GENES if g in df.columns and df[g].notna().sum() > 5]
    if effector_avail and exhaust_avail:
        effector_score = df[[f"{g}_z" for g in effector_avail]].mean(axis=1)
        df["ee_ratio"] = effector_score - df["exhaustion_score"]

    # Acute STING signature
    acute_avail = [g for g in ACUTE_STING if g in df.columns and df[g].notna().sum() > 5]
    if len(acute_avail) >= 2:
        for g in acute_avail:
            vals = df[g].dropna()
            df[f"{g}_z"] = (df[g] - vals.mean()) / vals.std()
        df["acute_sting"] = df[[f"{g}_z" for g in acute_avail]].mean(axis=1)

    # Chronic STING signature
    chronic_avail = [g for g in CHRONIC_STING if g in df.columns and df[g].notna().sum() > 5]
    if len(chronic_avail) >= 2:
        for g in chronic_avail:
            vals = df[g].dropna()
            df[f"{g}_z" if f"{g}_z" not in df.columns else f"{g}_z2"] = \
                (df[g] - df[g].dropna().mean()) / df[g].dropna().std()
        df["chronic_sting"] = df[[f"{g}_z" for g in chronic_avail
                                   if f"{g}_z" in df.columns]].mean(axis=1)

    if "acute_sting" in df.columns and "chronic_sting" in df.columns:
        df["sting_ratio"] = df["acute_sting"] - df["chronic_sting"]

    return df


# ─── Step 8: Stratified Correlations ─────────────────────────────────────────

def run_stratified_correlations(df):
    """
    For each stratum, compute Spearman correlations of tGJS against all markers.
    Returns a long-format dataframe with Bonferroni-corrected p-values.
    """
    markers = (
        ["immune_proxy"] +
        [g for g in IMMUNE_GENES if g in df.columns] +
        ["exhaustion_score", "ee_ratio"] +
        [g for g in EXHAUST_GENES if g in df.columns] +
        ["ENPP1", "TREX1", "CD274", "CGAS", "STING1"] +
        ["acute_sting", "chronic_sting", "sting_ratio"]
    )
    markers = [m for m in markers if m in df.columns]
    markers = list(dict.fromkeys(markers))  # deduplicate

    strata = [s for s in STRATUM_LABELS if s in df["stratum"].unique()]
    results = []

    for stratum in strata:
        sdf = df[df["stratum"] == stratum].copy()
        n = len(sdf)
        n_tests = len(markers)

        p_raw = []
        rhos   = []
        ns     = []

        for marker in markers:
            subset = sdf[["tGJS", marker]].dropna()
            if len(subset) < 10:
                rhos.append(np.nan)
                p_raw.append(1.0)
                ns.append(len(subset))
            else:
                rho, p = stats.spearmanr(subset["tGJS"], subset[marker])
                rhos.append(rho)
                p_raw.append(p)
                ns.append(len(subset))

        p_bonf = bonferroni_correct(p_raw, n_tests)

        for marker, rho, p_r, p_b, n_pairs in zip(markers, rhos, p_raw, p_bonf, ns):
            results.append({
                "stratum": stratum,
                "stratum_label": STRATUM_LABELS[stratum],
                "marker": marker,
                "spearman_rho": round(rho, 4) if not np.isnan(rho) else np.nan,
                "p_raw": p_r,
                "p_bonferroni": p_b,
                "n": n_pairs,
                "significant_bonf": p_b < 0.05,
                "significant_raw": p_r < 0.05,
            })

    return pd.DataFrame(results)


# ─── Step 9: Figures ──────────────────────────────────────────────────────────

def plot_all(df, corr_df):
    """Generate Figures S2a–S2e."""
    PLOT_DIR.mkdir(parents=True, exist_ok=True)
    sns.set_style("whitegrid")
    sns.set_context("paper", font_scale=1.3)

    plot_df = df[df["stratum"].isin(STRATUM_LABELS.keys())].copy()
    strata_order = ["MSS_TP53wt", "MSS_TP53mut", "MSIH_TP53wt", "MSIH_TP53mut"]
    strata_order = [s for s in strata_order if s in plot_df["stratum"].unique()]

    # ── Fig S2a: tGJS distribution by stratum ─────────────────────────────
    fig, ax = plt.subplots(figsize=(9, 6))
    palette = {s: STRATUM_COLORS[s] for s in strata_order}
    sns.violinplot(data=plot_df, x="stratum", y="tGJS", order=strata_order,
                   palette=palette, inner="box", ax=ax, cut=0)
    ax.set_xticklabels([STRATUM_LABELS[s].replace(" + ", "\n") for s in strata_order])
    ax.set_xlabel("")
    ax.set_ylabel("tGJS (rank-normalized within COADREAD)")
    ax.set_title("tGJS Distribution by MSI × TP53 Stratum\n(TCGA COADREAD, n=592)")

    # Annotate sample counts
    for i, s in enumerate(strata_order):
        n = (plot_df["stratum"] == s).sum()
        ax.text(i, plot_df[plot_df["stratum"] == s]["tGJS"].max() * 1.02,
                f"n={n}", ha="center", fontsize=10, color="black")

    plt.tight_layout()
    _save_fig(fig, "figS2a_tgjs_by_stratum")

    # ── Fig S2b: tGJS vs Immune Proxy by stratum ──────────────────────────
    if "immune_proxy" in plot_df.columns:
        _scatter_by_stratum(plot_df, "tGJS", "immune_proxy",
                            strata_order,
                            xlabel="tGJS",
                            ylabel="Immune Proxy Score\n(mean z-score: CD8A, IFNG, CXCL10, GZMB, PRF1)",
                            title="tGJS vs Immune Infiltration by Stratum",
                            fname="figS2b_tgjs_vs_immune_proxy")

    # ── Fig S2c: Correlation heatmap ──────────────────────────────────────
    marker_order = (
        ["immune_proxy", "CD8A", "GZMB", "PRF1", "IFNG", "CXCL10"] +
        ["ee_ratio", "exhaustion_score"] +
        [g for g in EXHAUST_GENES if g in plot_df.columns] +
        ["ENPP1", "TREX1", "CGAS", "STING1", "CD274"] +
        ["acute_sting", "chronic_sting", "sting_ratio"]
    )
    marker_order = [m for m in marker_order if m in corr_df["marker"].unique()]
    marker_order = list(dict.fromkeys(marker_order))

    pivot = corr_df[corr_df["stratum"].isin(strata_order)].pivot_table(
        index="marker", columns="stratum", values="spearman_rho"
    )
    pivot = pivot.reindex(index=[m for m in marker_order if m in pivot.index],
                          columns=strata_order)

    sig_pivot = corr_df[corr_df["stratum"].isin(strata_order)].pivot_table(
        index="marker", columns="stratum", values="significant_bonf"
    )
    sig_pivot = sig_pivot.reindex(index=pivot.index, columns=strata_order)

    fig, ax = plt.subplots(figsize=(10, max(6, len(pivot) * 0.45)))
    im = sns.heatmap(pivot.astype(float), annot=True, fmt=".2f",
                     cmap="RdBu_r", center=0, vmin=-0.6, vmax=0.6,
                     ax=ax, cbar_kws={"label": "Spearman ρ"},
                     linewidths=0.5, linecolor="gray")

    # Star significant cells
    for i, marker in enumerate(pivot.index):
        for j, stratum in enumerate(pivot.columns):
            if sig_pivot.loc[marker, stratum]:
                ax.text(j + 0.85, i + 0.2, "*", color="black",
                        fontsize=14, ha="center", va="center")

    ax.set_xticklabels([STRATUM_LABELS[s].replace(" + ", "\n")
                        for s in pivot.columns], rotation=30, ha="right")
    ax.set_ylabel("")
    ax.set_title("tGJS Correlations by Stratum\n(* = Bonferroni-significant)")
    plt.tight_layout()
    _save_fig(fig, "figS2c_correlation_heatmap")

    # ── Fig S2d: tGJS vs ENPP1 by stratum ────────────────────────────────
    if "ENPP1" in plot_df.columns:
        _scatter_by_stratum(plot_df, "tGJS", "ENPP1",
                            strata_order,
                            xlabel="tGJS",
                            ylabel="ENPP1 expression (RSEM)",
                            title="tGJS vs ENPP1 by Stratum\n(anti-correlation = evasion strategy partitioning)",
                            fname="figS2d_tgjs_vs_enpp1")

    # ── Fig S2e: tGJS vs Effector/Exhaustion Ratio by stratum ────────────
    if "ee_ratio" in plot_df.columns:
        _scatter_by_stratum(plot_df, "tGJS", "ee_ratio",
                            strata_order,
                            xlabel="tGJS",
                            ylabel="Effector/Exhaustion Ratio\n(mean-z: GZMB+PRF1+IFNG − TIM3+LAG3+PD1)",
                            title="tGJS vs Effector/Exhaustion Ratio by Stratum",
                            fname="figS2e_tgjs_vs_ee_ratio")


def _scatter_by_stratum(df, xcol, ycol, strata_order, xlabel, ylabel, title, fname):
    """Shared scatter plot with per-stratum regression lines and ρ annotations."""
    fig, ax = plt.subplots(figsize=(9, 7))
    patches = []

    for stratum in strata_order:
        sdf = df[df["stratum"] == stratum][[xcol, ycol]].dropna()
        if len(sdf) < 5:
            continue
        color = STRATUM_COLORS[stratum]
        label = STRATUM_LABELS[stratum]
        ax.scatter(sdf[xcol], sdf[ycol], color=color, alpha=0.4, s=18, label=label)

        # Regression line
        z = np.polyfit(sdf[xcol], sdf[ycol], 1)
        x_line = np.linspace(sdf[xcol].min(), sdf[xcol].max(), 100)
        ax.plot(x_line, np.poly1d(z)(x_line), color=color, linewidth=2, alpha=0.9)

        rho, p = stats.spearmanr(sdf[xcol], sdf[ycol])
        patches.append(mpatches.Patch(color=color,
                                       label=f"{label}\nρ={rho:.3f}, p={p:.2e}, n={len(sdf)}"))

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend(handles=patches, loc="best", fontsize=8, framealpha=0.7)
    plt.tight_layout()
    _save_fig(fig, fname)


def _save_fig(fig, name):
    for ext in ["png", "svg"]:
        path = PLOT_DIR / f"{name}.{ext}"
        fig.savefig(path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {name}.png/svg")


# ─── Step 10: Save Results ────────────────────────────────────────────────────

def save_results(df, corr_df, clinical_df):
    """Save all outputs."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Expression matrix with labels
    expr_cols = (["sample_id", "stratum", "tGJS"] +
                 GJS_GENES + ["HK2_norm", "BCL2L1_norm", "TSPO_norm"] +
                 [g for g in IMMUNE_GENES if g in df.columns] +
                 [g for g in EXHAUST_GENES if g in df.columns] +
                 [g for g in STING_GENES if g in df.columns] +
                 ["immune_proxy", "exhaustion_score", "ee_ratio",
                  "acute_sting", "chronic_sting", "sting_ratio"])
    expr_cols = [c for c in expr_cols if c in df.columns]
    expr_cols = list(dict.fromkeys(expr_cols))
    df[expr_cols].to_csv(DATA_DIR / "coadread_mss_expression_matrix.csv", index=False)

    # Full correlation table
    corr_df.to_csv(DATA_DIR / "coadread_mss_correlations.csv", index=False)

    # Clinical annotations
    clinical_df.to_csv(DATA_DIR / "coadread_mss_clinical.csv", index=False)

    # Strata summary
    strata_summary = {}
    for stratum, label in STRATUM_LABELS.items():
        sdf = df[df["stratum"] == stratum]
        strata_summary[stratum] = {
            "label": label,
            "n": int(len(sdf)),
            "mean_tGJS": round(float(sdf["tGJS"].mean()), 4) if len(sdf) > 0 else None,
            "std_tGJS": round(float(sdf["tGJS"].std()), 4) if len(sdf) > 0 else None,
        }

    summary = {
        "study": STUDY_ID,
        "total_coadread": len(df),
        "strata": strata_summary,
    }
    with open(DATA_DIR / "coadread_mss_strata_summary.json", "w") as f:
        json.dump(summary, f, indent=2)

    print(f"\n  Results saved to {DATA_DIR}/")


# ─── Step 11: Interpretation Summary ─────────────────────────────────────────

def print_interpretation(df, corr_df):
    """Print the key findings summary."""
    print()
    print("=" * 60)
    print("COADREAD MSS-STRATIFIED tGJS ANALYSIS")
    print("=" * 60)

    # Sample counts
    print("\nSample counts:")
    for s, label in STRATUM_LABELS.items():
        n = (df["stratum"] == s).sum()
        flag = "  ⚠ < 20" if n < 20 else ""
        print(f"  {label}: N = {n}{flag}")

    # Helper to get rho/p for a marker in a stratum
    def get_corr(stratum, marker):
        row = corr_df[(corr_df["stratum"] == stratum) &
                      (corr_df["marker"] == marker)]
        if row.empty:
            return None, None
        return float(row["spearman_rho"].iloc[0]), float(row["p_bonferroni"].iloc[0])

    # Primary test
    primary = "MSS_TP53wt"
    print(f"\nPRIMARY TEST ({STRATUM_LABELS[primary]} — the clean room):")

    key_markers = [
        ("immune_proxy", "Immune Proxy Score"),
        ("CD8A",         "CD8A"),
        ("GZMB",         "GZMB"),
        ("ee_ratio",     "Effector/Exhaustion Ratio"),
    ]

    sign_flips = []
    for marker, label in key_markers:
        rho, p = get_corr(primary, marker)
        if rho is not None:
            direction = "↓ NEGATIVE" if rho < 0 else "↑ POSITIVE"
            print(f"  tGJS vs {label}: ρ = {rho:.3f}, p_bonf = {p:.2e}  {direction}")
            sign_flips.append(rho < 0)
        else:
            print(f"  tGJS vs {label}: N/A (insufficient data)")

    if sign_flips:
        any_flip = any(sign_flips)
        all_flip = all(sign_flips)
        if all_flip:
            flip_verdict = "YES — all key markers negative in clean room (vs positive pan-cancer)"
        elif any_flip:
            flip_verdict = "PARTIAL — some markers negative in clean room"
        else:
            flip_verdict = "NO — positive correlations persist even in clean room"
        print(f"\nSIGN FLIP? {flip_verdict}")
    else:
        print("\nSIGN FLIP? INCONCLUSIVE (insufficient data)")

    # ENPP1 test
    print("\nENPP1 ANTI-CORRELATION TEST:")
    print(f"  Pan-cancer ENPP1:     ρ = -0.181 (p = 4.3×10⁻⁷⁵)")
    for s in ["MSS_TP53wt", "MSS_TP53mut", "MSIH_TP53wt"]:
        rho, p = get_corr(s, "ENPP1")
        if rho is not None:
            stronger = "STRONGER" if rho < -0.181 else ("similar" if abs(rho + 0.181) < 0.05 else "WEAKER")
            print(f"  {STRATUM_LABELS[s]}: ρ = {rho:.3f} ({stronger})")
    rho_mss, _ = get_corr("MSS_TP53wt", "ENPP1")
    if rho_mss is not None:
        verdict = "YES" if rho_mss < -0.181 else "NO"
        print(f"  Anti-correlation strengthened in MSS/TP53-wt? {verdict}")

    # MSI-H control
    print("\nMSI-H CONTROL:")
    msih = "MSIH_TP53mut"
    rho_h, p_h = get_corr(msih, "immune_proxy")
    rho_mss_ip, _ = get_corr(primary, "immune_proxy")
    if rho_h is not None:
        attenuated = (abs(rho_h) < abs(rho_mss_ip)) if rho_mss_ip is not None else None
        verdict = "YES" if attenuated else ("NO" if attenuated is False else "N/A")
        print(f"  tGJS vs Immune Proxy (MSI-H + TP53-mut): ρ = {rho_h:.3f}, p_bonf = {p_h:.2e}")
        print(f"  Signal attenuated in MSI-H vs MSS clean room? {verdict}")

    print()
    print("=" * 60)


# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="COADREAD MSS-stratified tGJS Analysis (S2)")
    parser.add_argument("--cache", action="store_true",
                        help="Use all local caches, skip all API calls")
    args = parser.parse_args()

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    PLOT_DIR.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("COADREAD MSS-STRATIFIED tGJS — SUPPLEMENTARY S2")
    print("=" * 60)

    # 1. Load base expression
    print("\n[1] Loading COADREAD expression from parquet...")
    expr_df = load_coadread_expression()

    # 2. Fetch clinical annotations
    print("\n[2] Fetching clinical annotations (MSI, TP53)...")
    if args.cache:
        cache_path = DATA_DIR / "coadread_clinical.csv"
        if not cache_path.exists():
            print("  --cache set but no cache found. Fetching from API...")
        clinical_df = fetch_clinical_data()
    else:
        clinical_df = fetch_clinical_data()

    # 3. Fetch exhaustion genes
    print("\n[3] Fetching exhaustion marker genes...")
    extra_df = fetch_extra_genes(expr_df["sample_id"].tolist())
    if len(extra_df.columns) > 1:  # has gene columns
        expr_df = expr_df.merge(extra_df, on="sample_id", how="left")

    # 4. Compute tGJS (rank-normalized within COADREAD)
    print("\n[4] Computing tGJS (rank-normalized within COADREAD)...")
    expr_df = compute_tgjs_coadread(expr_df)
    print(f"  Mean tGJS: {expr_df['tGJS'].mean():.4f} ± {expr_df['tGJS'].std():.4f}")

    # 5. Assign strata
    print("\n[5] Assigning MSI × TP53 strata...")
    df = assign_strata(expr_df, clinical_df)

    # 6. Compute derived signatures
    print("\n[6] Computing immune proxy, exhaustion, and STING signatures...")
    df = compute_derived_signatures(df)
    derived_avail = [c for c in ["immune_proxy", "exhaustion_score", "ee_ratio",
                                  "acute_sting", "chronic_sting", "sting_ratio"]
                     if c in df.columns]
    print(f"  Derived signatures available: {derived_avail}")

    # 7. Stratified correlations
    print("\n[7] Running stratified correlations (Bonferroni-corrected)...")
    corr_df = run_stratified_correlations(df)
    print(f"  Computed {len(corr_df)} correlation pairs across {corr_df['stratum'].nunique()} strata")

    # 8. Figures
    print("\n[8] Generating figures...")
    plot_all(df, corr_df)

    # 9. Save
    print("\n[9] Saving results...")
    save_results(df, corr_df, clinical_df)

    # 10. Interpretation
    print_interpretation(df, corr_df)


if __name__ == "__main__":
    main()
