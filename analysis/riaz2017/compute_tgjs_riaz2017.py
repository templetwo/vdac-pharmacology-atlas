#!/usr/bin/env python3
"""
tGJS Analysis: Riaz 2017 Nivolumab Cohort (GSE91061) — Supplementary Analysis S4
==================================================================================
Tests whether tGJS predicts nivolumab response in pre-treatment melanoma biopsies.

Data:  Riaz et al., Cell 2017 — GSE91061
       109 samples, pre- and on-treatment biopsies
       Melanoma, anti-PD-1 (nivolumab) monotherapy

Prediction: NULL result (boundary confirmation)
  - Melanoma has high baseline TMB (tobacco/UV mutagenesis)
  - Nuclear DNA noise dominates cGAS-STING, same logic as IMvigor210
  - tGJS expected to show no response signal

Key tests:
  1. tGJS vs binary response (pre-treatment only)
  2. tGJS vs ordinal RECIST (Spearman)
  3. tGJS by response category (Kruskal-Wallis)
  4. Pre vs on-treatment tGJS shift in responders vs non-responders
"""

import os
import sys
import json
import gzip
import urllib.request
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import GEOparse

# ── Paths ─────────────────────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR   = os.path.join(SCRIPT_DIR, 'data')
PLOT_DIR   = os.path.join(SCRIPT_DIR, 'figures')
GEO_CACHE  = '/tmp/riaz2017'
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(PLOT_DIR, exist_ok=True)
os.makedirs(GEO_CACHE, exist_ok=True)

print("=" * 62)
print("tGJS ANALYSIS — Riaz 2017 Nivolumab (Supplementary S4)")
print("=" * 62)

# ── 1. Load GEO metadata ──────────────────────────────────────────────────────
print("\n[1] Loading GSE91061 metadata...")
gse = GEOparse.get_GEO('GSE91061', destdir=GEO_CACHE, silent=True)
print(f"    Series: {gse.metadata['title'][0]}")
print(f"    N samples: {len(gse.gsms)}")

# Build clinical dataframe from sample metadata
records = []
for gsm_id, gsm in gse.gsms.items():
    chars = {}
    for c in gsm.metadata.get('characteristics_ch1', []):
        if ':' in c:
            k, v = c.split(':', 1)
            chars[k.strip()] = v.strip()
    records.append({
        'sample_id': gsm_id,
        'title':     gsm.metadata['title'][0],
        'response':  chars.get('response', 'NA'),
        'visit':     chars.get('visit (pre or on treatment)', 'NA'),
        'tissue':    chars.get('tissue', 'NA'),
    })

clin = pd.DataFrame(records)
print(f"\n    Visit distribution:")
print(clin['visit'].value_counts().to_string())
print(f"\n    Response distribution:")
print(clin['response'].value_counts().to_string())

# ── 2. Download FPKM matrix ───────────────────────────────────────────────────
fpkm_url  = ("ftp://ftp.ncbi.nlm.nih.gov/geo/series/GSE91nnn/GSE91061/"
             "suppl/GSE91061_BMS038109Sample.hg19KnownGene.fpkm.csv.gz")
fpkm_path = os.path.join(GEO_CACHE, 'fpkm.csv.gz')

if not os.path.exists(fpkm_path):
    print("\n[2] Downloading FPKM matrix (~30MB)...")
    urllib.request.urlretrieve(fpkm_url, fpkm_path)
    print("    Downloaded.")
else:
    print("\n[2] FPKM matrix already cached.")

print("    Parsing FPKM matrix...")
with gzip.open(fpkm_path, 'rt') as f:
    fpkm = pd.read_csv(f, index_col=0)

print(f"    FPKM shape: {fpkm.shape[0]:,} genes x {fpkm.shape[1]} samples")
print(f"    Index sample: {fpkm.columns[0]}")

# ── 3. Match FPKM columns to clinical data ────────────────────────────────────
print("\n[3] Matching expression columns to clinical metadata...")

# FPKM columns may be sample titles (e.g. "Pt1_Pre") not GSM accessions
# Build a title -> gsm_id map
title_to_gsm = {row['title']: row['sample_id'] for _, row in clin.iterrows()}

# Try direct match first, then strip common prefixes
matched = {}
for col in fpkm.columns:
    if col in title_to_gsm:
        matched[col] = title_to_gsm[col]

print(f"    Direct title matches: {len(matched)} / {len(fpkm.columns)}")

if len(matched) < len(fpkm.columns) * 0.5:
    # Try partial match on GSM IDs embedded in column names
    gsm_ids = set(clin['sample_id'])
    for col in fpkm.columns:
        for gsm in gsm_ids:
            if gsm in col:
                matched[col] = gsm
                break
    print(f"    After GSM-in-column search: {len(matched)}")

# Build a working expression frame aligned to clinical
# Keep samples that matched
clin = clin.set_index('sample_id')

if len(matched) > 0:
    # Rename FPKM cols to GSM IDs
    fpkm_matched = fpkm[list(matched.keys())].rename(columns=matched)
else:
    # Fallback: assume FPKM column order matches GEO sample order
    print("    WARNING: No title match; assuming column order matches GEO order")
    gsm_order = list(gse.gsms.keys())
    if len(gsm_order) == fpkm.shape[1]:
        fpkm_matched = fpkm.copy()
        fpkm_matched.columns = gsm_order
    else:
        print("    ERROR: Column count mismatch. Cannot align.")
        sys.exit(1)

print(f"    Aligned expression: {fpkm_matched.shape}")

# ── 4. Extract tGJS genes ─────────────────────────────────────────────────────
print("\n[4] Extracting tGJS genes (HK2, BCL2L1, TSPO)...")

GENES = {'HK2': None, 'BCL2L1': None, 'TSPO': None}

for gene in GENES:
    # FPKM index is gene symbols (hg19KnownGene — may be Entrez or symbols)
    matches = [idx for idx in fpkm_matched.index
               if str(idx).upper() == gene.upper()]
    if not matches:
        # Try partial match
        matches = [idx for idx in fpkm_matched.index
                   if gene.upper() in str(idx).upper()]
    if matches:
        GENES[gene] = matches[0]
        print(f"    {gene}: found as '{matches[0]}'")
    else:
        print(f"    {gene}: NOT FOUND in index")

# Check if all found
missing = [g for g, v in GENES.items() if v is None]
if missing:
    print(f"\n    Checking index format (first 10 entries):")
    print(list(fpkm_matched.index[:10]))
    # If Entrez IDs, use known IDs: HK2=3099, BCL2L1=598, TSPO=706
    entrez_map = {'HK2': 3099, 'BCL2L1': 598, 'TSPO': 706}
    for gene in missing:
        eid = entrez_map[gene]
        if eid in fpkm_matched.index:
            GENES[gene] = eid
            print(f"    {gene}: found as Entrez ID {eid}")
        elif str(eid) in fpkm_matched.index:
            GENES[gene] = str(eid)
            print(f"    {gene}: found as string Entrez ID '{eid}'")

still_missing = [g for g, v in GENES.items() if v is None]
if still_missing:
    print(f"\nFATAL: Cannot find genes: {still_missing}")
    print("Index sample:", list(fpkm_matched.index[:20]))
    sys.exit(1)

# Extract FPKM vectors per gene
hk2_fpkm    = fpkm_matched.loc[GENES['HK2']].astype(float)
bcl2l1_fpkm = fpkm_matched.loc[GENES['BCL2L1']].astype(float)
tspo_fpkm   = fpkm_matched.loc[GENES['TSPO']].astype(float)

print(f"\n    HK2    median FPKM: {hk2_fpkm.median():.2f}")
print(f"    BCL2L1 median FPKM: {bcl2l1_fpkm.median():.2f}")
print(f"    TSPO   median FPKM: {tspo_fpkm.median():.2f}")

# ── 5. Compute tGJS ───────────────────────────────────────────────────────────
print("\n[5] Computing tGJS (z-score weighted)...")

def zscore(v):
    v = np.array(v, dtype=float)
    sd = np.std(v, ddof=1)
    if sd == 0:
        return np.zeros_like(v)
    return (v - np.mean(v)) / sd

hk2_z    = zscore(hk2_fpkm.values)
bcl2l1_z = zscore(bcl2l1_fpkm.values)
tspo_z   = zscore(tspo_fpkm.values)

tGJS = 0.40 * hk2_z + 0.30 * bcl2l1_z + 0.30 * tspo_z

tgjs_s = pd.Series(tGJS, index=fpkm_matched.columns, name='tGJS')

print(f"    tGJS: mean={tgjs_s.mean():.4f}  sd={tgjs_s.std():.4f}")
print(f"          range=[{tgjs_s.min():.3f}, {tgjs_s.max():.3f}]")

# ── 6. Assemble analysis frame ────────────────────────────────────────────────
print("\n[6] Assembling analysis frame...")

df = clin.copy()
df['tGJS']      = tgjs_s
df['HK2_fpkm']  = hk2_fpkm
df['BCL2L1_fpkm'] = bcl2l1_fpkm
df['TSPO_fpkm'] = tspo_fpkm

# Binary response — GEO deposit uses 'PRCR' for CR/PR combined
df['resp_bin'] = df['response'].map(
    {'CR': 1, 'PR': 1, 'PRCR': 1, 'SD': 0, 'PD': 0}
)
# Ordinal RECIST — PRCR gets 3.5 (midpoint CR/PR)
df['resp_num'] = df['response'].map(
    {'CR': 4, 'PR': 3, 'PRCR': 3.5, 'SD': 2, 'PD': 1}
)
# tGJS groups
df['tGJS_high'] = (df['tGJS'] > df['tGJS'].median()).map({True: 'High', False: 'Low'})
df['tGJS_tertile'] = pd.qcut(df['tGJS'], q=3, labels=['Low', 'Mid', 'High'])

# Visit labels
df['visit_clean'] = df['visit'].str.strip()

print(f"    Total samples: {len(df)}")
print(f"    Pre-treatment: {(df['visit_clean'] == 'Pre').sum()}")
print(f"    On-treatment:  {(df['visit_clean'] == 'On').sum()}")

# ── 7. Primary analysis — PRE-TREATMENT ONLY ──────────────────────────────────
print("\n[7] Primary analysis (pre-treatment biopsies only)...")

pre = df[df['visit_clean'] == 'Pre'].dropna(subset=['tGJS', 'resp_bin'])
print(f"    N pre-treatment with response data: {len(pre)}")
print(f"    Response: CR={( pre['response']=='CR').sum()} "
      f"PR={(pre['response']=='PR').sum()} "
      f"SD={(pre['response']=='SD').sum()} "
      f"PD={(pre['response']=='PD').sum()}")

# Wilcoxon
cr_pr = pre['tGJS'][pre['resp_bin'] == 1]
sd_pd = pre['tGJS'][pre['resp_bin'] == 0]
wstat, wp = stats.mannwhitneyu(cr_pr, sd_pd, alternative='two-sided')
print(f"\n    CR/PR mean tGJS: {cr_pr.mean():.3f} (n={len(cr_pr)})")
print(f"    SD/PD mean tGJS: {sd_pd.mean():.3f} (n={len(sd_pd)})")
print(f"    Wilcoxon p = {wp:.4f}")

# Logistic regression (manual via scipy)
from scipy.special import expit
pre_clean = pre.dropna(subset=['resp_bin', 'tGJS'])
x = pre_clean['tGJS'].values
y = pre_clean['resp_bin'].values.astype(float)

from scipy.optimize import minimize
def neg_loglik(params):
    b0, b1 = params
    p = expit(b0 + b1 * x)
    p = np.clip(p, 1e-10, 1 - 1e-10)
    return -np.sum(y * np.log(p) + (1 - y) * np.log(1 - p))

res = minimize(neg_loglik, [0, 0], method='Nelder-Mead')
b0, b1 = res.x
or_val = np.exp(b1)
print(f"    Logistic OR = {or_val:.3f}")

# Spearman vs ordinal RECIST
pre_ord = pre.dropna(subset=['tGJS', 'resp_num'])
rho, rho_p = stats.spearmanr(pre_ord['tGJS'], pre_ord['resp_num'])
print(f"    Spearman rho vs RECIST: {rho:.3f}, p = {rho_p:.4f}")

# Kruskal-Wallis by tertile
groups = [grp['tGJS'].values for _, grp in pre.groupby('tGJS_tertile')]
kw_stat, kw_p = stats.kruskal(*groups)
print(f"    Kruskal-Wallis by tertile: p = {kw_p:.4f}")

# Response rate by tertile
print("\n    Response rate by tGJS tertile:")
for t in ['Low', 'Mid', 'High']:
    sub = pre[pre['tGJS_tertile'] == t]
    rr = sub['resp_bin'].mean() * 100 if len(sub) > 0 else float('nan')
    print(f"      {t}: n={len(sub)}, RR={rr:.1f}%")

# ── 8. Pre vs On-treatment comparison ────────────────────────────────────────
print("\n[8] Pre vs on-treatment tGJS in responders vs non-responders...")

# Match patients across visits using title (e.g., Pt1_Pre -> Pt1_On)
df['patient'] = df['title'].str.extract(r'(Pt\d+)', expand=False)
df['visit_short'] = df['visit_clean'].map({'Pre': 'Pre', 'On': 'On'})

paired = df.dropna(subset=['patient', 'tGJS', 'resp_bin'])
patients_both = (paired.groupby('patient')['visit_short']
                 .apply(lambda x: set(x) == {'Pre', 'On'}))
paired_pts = patients_both[patients_both].index

if len(paired_pts) > 0:
    paired_data = paired[paired['patient'].isin(paired_pts)]
    for resp_label, resp_val in [('Responders (CR/PR)', 1), ('Non-responders (SD/PD)', 0)]:
        sub = paired_data[paired_data['resp_bin'] == resp_val]
        pre_v = sub[sub['visit_short'] == 'Pre']['tGJS']
        on_v  = sub[sub['visit_short'] == 'On']['tGJS']
        if len(pre_v) > 0 and len(on_v) > 0:
            print(f"    {resp_label}: Pre tGJS={pre_v.mean():.3f}, "
                  f"On tGJS={on_v.mean():.3f} (n={len(pre_v)} pairs)")
else:
    print("    No matched pre/on pairs found")

# ── 9. Save data matrix ───────────────────────────────────────────────────────
print("\n[9] Saving results...")

out_cols = ['title', 'visit', 'response', 'resp_bin', 'resp_num',
            'tGJS', 'tGJS_high', 'tGJS_tertile', 'HK2_fpkm',
            'BCL2L1_fpkm', 'TSPO_fpkm']
df[out_cols].to_csv(os.path.join(DATA_DIR, 'riaz2017_tgjs_matrix.csv'))

summary = {
    'study':          'Riaz 2017 (GSE91061)',
    'n_samples':      int(len(df)),
    'n_pre_treatment': int((df['visit_clean'] == 'Pre').sum()),
    'n_pre_with_response': int(len(pre)),
    'primary_test': {
        'wilcoxon_p':         float(wp),
        'logistic_OR':        float(or_val),
        'spearman_rho_vs_RECIST': float(rho),
        'spearman_p':         float(rho_p),
        'kw_tertile_p':       float(kw_p),
    }
}
with open(os.path.join(DATA_DIR, 'riaz2017_tgjs_summary.json'), 'w') as f:
    json.dump(summary, f, indent=2)

print(f"    Saved matrix and summary JSON to {DATA_DIR}")

# ── 10. Figures ───────────────────────────────────────────────────────────────
print("\n[10] Generating figures...")

PALETTE = {'CR': '#2166ac', 'PR': '#74add1', 'SD': '#f46d43', 'PD': '#d73027'}
RESP_ORDER = ['CR', 'PR', 'SD', 'PD']

# ── Fig S4a: tGJS by response category (pre-treatment) ──
fig, ax = plt.subplots(figsize=(6, 5))
pre_plot = pre[pre['response'].isin(RESP_ORDER)]
colors = [PALETTE[r] for r in RESP_ORDER if r in pre_plot['response'].unique()]
resp_present = [r for r in RESP_ORDER if r in pre_plot['response'].unique()]
sns.violinplot(data=pre_plot, x='response', y='tGJS', order=resp_present,
               palette=PALETTE, inner='box', ax=ax, linewidth=1.2)
ax.axhline(0, color='grey', lw=0.8, ls='--', alpha=0.5)
ax.set_xlabel('RECIST Response', fontsize=12)
ax.set_ylabel('tGJS (z-score)', fontsize=12)
ax.set_title(f'tGJS by Response — Riaz 2017 Pre-treatment (n={len(pre_plot)})\n'
             f'Wilcoxon CR/PR vs SD/PD: p={wp:.3f}', fontsize=10)
for r in resp_present:
    n = (pre_plot['response'] == r).sum()
    xi = resp_present.index(r)
    ax.text(xi, ax.get_ylim()[0] + 0.05, f'n={n}', ha='center', fontsize=9, color='#444')
plt.tight_layout()
plt.savefig(os.path.join(PLOT_DIR, 'figS4a_tgjs_by_response.png'), dpi=150)
plt.close()
print("    figS4a saved")

# ── Fig S4b: Response rate by tGJS tertile ──
fig, ax = plt.subplots(figsize=(5, 4.5))
tert_rr = (pre.groupby('tGJS_tertile')['resp_bin']
           .agg(['mean', 'count'])
           .reset_index())
tert_rr['rr_pct'] = tert_rr['mean'] * 100
ax.bar(tert_rr['tGJS_tertile'].astype(str), tert_rr['rr_pct'],
       color=['#74add1', '#a8ddb5', '#2166ac'], edgecolor='white', linewidth=1.2)
ax.set_xlabel('tGJS Tertile', fontsize=12)
ax.set_ylabel('Response Rate (CR+PR %)', fontsize=12)
ax.set_title(f'Response Rate by tGJS Tertile\nKruskal-Wallis p={kw_p:.3f}', fontsize=10)
for i, row in tert_rr.iterrows():
    ax.text(i, row['rr_pct'] + 0.5, f"{row['rr_pct']:.1f}%\n(n={int(row['count'])})",
            ha='center', fontsize=9)
ax.set_ylim(0, max(tert_rr['rr_pct']) * 1.3 + 5)
plt.tight_layout()
plt.savefig(os.path.join(PLOT_DIR, 'figS4b_response_rate_by_tertile.png'), dpi=150)
plt.close()
print("    figS4b saved")

# ── Fig S4c: Pre vs on-treatment tGJS shift ──
if len(paired_pts) > 0:
    fig, axes = plt.subplots(1, 2, figsize=(8, 5), sharey=True)
    for ax, (resp_label, resp_val) in zip(axes,
        [('Responders\n(CR/PR)', 1), ('Non-responders\n(SD/PD)', 0)]):
        sub = paired_data[paired_data['resp_bin'] == resp_val]
        sub_pre = sub[sub['visit_short'] == 'Pre'].set_index('patient')
        sub_on  = sub[sub['visit_short'] == 'On'].set_index('patient')
        common  = sub_pre.index.intersection(sub_on.index)
        for pt in common:
            ax.plot([0, 1],
                    [sub_pre.loc[pt, 'tGJS'], sub_on.loc[pt, 'tGJS']],
                    'o-', color='#2166ac' if resp_val == 1 else '#d73027',
                    alpha=0.5, lw=1)
        ax.set_xticks([0, 1])
        ax.set_xticklabels(['Pre', 'On'], fontsize=11)
        ax.set_title(resp_label, fontsize=11)
        ax.axhline(0, color='grey', lw=0.8, ls='--', alpha=0.5)
        ax.set_ylabel('tGJS', fontsize=11)
    fig.suptitle('tGJS Shift: Pre vs On-Treatment by Response', fontsize=11, y=1.01)
    plt.tight_layout()
    plt.savefig(os.path.join(PLOT_DIR, 'figS4c_pre_vs_ontreatment.png'), dpi=150)
    plt.close()
    print("    figS4c saved")
else:
    print("    figS4c skipped (no paired samples)")

# ── Fig S4d: tGJS high vs low — summary scatter ──
fig, ax = plt.subplots(figsize=(5, 4.5))
jitter = np.random.RandomState(42).uniform(-0.15, 0.15, len(pre))
colors_pt = pre['resp_bin'].map({1: '#2166ac', 0: '#d73027'})
ax.scatter(pre['tGJS_high'].map({'High': 1, 'Low': 0}) + jitter,
           pre['tGJS'],
           c=colors_pt, alpha=0.65, s=40, edgecolors='white', lw=0.4)
ax.set_xticks([0, 1])
ax.set_xticklabels(['tGJS Low\n(≤ median)', 'tGJS High\n(> median)'], fontsize=11)
ax.set_ylabel('tGJS (z-score)', fontsize=11)

from matplotlib.patches import Patch
ax.legend(handles=[Patch(color='#2166ac', label='CR/PR'),
                   Patch(color='#d73027', label='SD/PD')],
          fontsize=10, framealpha=0.7)
ax.set_title(f'Individual tGJS Values by Response\n(pre-treatment, n={len(pre)})',
             fontsize=10)
plt.tight_layout()
plt.savefig(os.path.join(PLOT_DIR, 'figS4d_tgjs_scatter_by_response.png'), dpi=150)
plt.close()
print("    figS4d saved")

# ── Final summary ─────────────────────────────────────────────────────────────
print()
print("=" * 62)
print("RESULTS SUMMARY")
print("=" * 62)
print(f"  Study:            Riaz 2017 (GSE91061) — melanoma, nivolumab")
print(f"  N total:          {len(df)}")
print(f"  N pre-treatment:  {(df['visit_clean'] == 'Pre').sum()}")
print(f"  N pre w/ response:{len(pre)}")
print()
print(f"  PRIMARY TESTS (pre-treatment):")
print(f"    Wilcoxon (CR/PR vs SD/PD): p = {wp:.4f}")
print(f"    Logistic OR:               {or_val:.3f}")
print(f"    Spearman rho vs RECIST:    {rho:.3f}, p = {rho_p:.4f}")
print(f"    Kruskal-Wallis by tertile: p = {kw_p:.4f}")
print()

if wp > 0.05 and abs(rho) < 0.15:
    print("  INTERPRETATION: NULL RESULT")
    print("  Consistent with S3 (IMvigor210): high-TMB tumor type,")
    print("  VDAC1 gate-jamming not the rate-limiting innate immune step.")
    print("  Confirms framework boundary: gate-jamming signal absent in")
    print("  genomically unstable tumors regardless of ICI type.")
else:
    print("  UNEXPECTED: Signal detected — review carefully.")

print()
print(f"  Output: {DATA_DIR}")
print(f"  Figures: {PLOT_DIR}")
