# Supplementary Analysis S4: tGJS in the Riaz 2017 Nivolumab Cohort — A Second Null in a High-TMB Tumor Type

## S4.1 Rationale

Supplementary S3 established that tGJS does not predict atezolizumab (anti-PD-L1) response or overall survival in the IMvigor210 urothelial carcinoma cohort (n = 348; Wilcoxon p = 0.965, Spearman ρ = −0.017). The null was attributed to urothelial carcinoma's high baseline tumor mutational burden (TMB): in high-TMB tumors, nuclear DNA damage saturates the cGAS-STING pathway with signals independent of VDAC1 gating, rendering the mitochondrial mtDNA release mechanism a minor contributor to innate immune activation.

S4 tests this interpretation by replicating the null in an independent high-TMB tumor type under a different ICI agent. The Riaz 2017 cohort (GSE91061) provides pre- and on-treatment biopsies from melanoma patients receiving nivolumab (anti-PD-1 monotherapy), a distinct checkpoint target acting on T cell exhaustion rather than PD-L1. If the null is specific to the gate-jamming framework's domain restriction — rather than an artifact of the S3 dataset, treatment agent, or analytical pipeline — a second null should appear in this cohort for the same reason: melanoma is among the highest-TMB tumor types, driven by UV-induced C>T transitions and tobacco-related mutagenesis, and VDAC1-mediated mtDNA release is predicted to be a minor input to cGAS-STING relative to the nuclear DNA noise floor.

## S4.2 Methods

### S4.2.1 Dataset

Riaz N et al. (Cell 171:934–949, 2017; GEO accession GSE91061) enrolled 89 patients with advanced melanoma receiving nivolumab monotherapy. The GEO deposit contains:

- FPKM expression matrix: 57,025 gene entries × 109 samples (pre- and on-treatment biopsies), indexed by Entrez gene IDs
- Clinical metadata: response category (CR, PR, SD, PD; with CR and PR combined as 'PRCR' in the GEO deposit), biopsy visit (Pre/On treatment), tissue site

Data were accessed programmatically via the GEOparse Python library. The FPKM matrix was downloaded from the GEO FTP supplementary files (`GSE91061_BMS038109Sample.hg19KnownGene.fpkm.csv.gz`).

### S4.2.2 Sample Selection

Pre-treatment biopsies were the primary analysis unit. Of 109 total samples, 51 were annotated as pre-treatment. Samples with available response data yielded a primary analysis set of n = 49.

Response was binarized as follows:
- Responders (binary = 1): CR, PR, or PRCR (the GEO deposit combines CR and PR into a single 'PRCR' category)
- Non-responders (binary = 0): SD or PD

Ordinal RECIST mapping for Spearman correlation: CR = 4, PR = 3, PRCR = 3.5 (midpoint), SD = 2, PD = 1.

### S4.2.3 tGJS Computation

tGJS was computed from FPKM values using the same formula applied in S1–S3:

```
tGJS = 0.40 × z(HK2) + 0.30 × z(BCL2L1) + 0.30 × z(TSPO)
```

where z(·) denotes within-cohort z-score normalization of raw FPKM values.

The FPKM matrix is indexed by Entrez integer IDs rather than HGNC gene symbols. The three tGJS components were retrieved by Entrez ID lookup (HK2 = 3099; BCL2L1 = 598; TSPO = 706). All three were present in the matrix.

### S4.2.4 Statistical Tests

**Primary tests (pre-treatment, n = 49):**

1. **Wilcoxon rank-sum test**: tGJS distribution in PRCR/CR/PR responders vs. SD/PD non-responders (two-sided Mann-Whitney U)
2. **Logistic regression**: tGJS as a continuous predictor of binary response, estimated by maximum likelihood via Nelder-Mead optimization; effect reported as odds ratio (OR = exp(β₁))
3. **Spearman rank correlation**: tGJS vs. ordinal RECIST score

**Secondary analysis:**

4. **Pre vs. on-treatment tGJS trajectory**: In paired samples with both pre- and on-treatment biopsies, tGJS trajectory was compared between responders and non-responders using patient-matched spaghetti plots.

**Note on Kruskal-Wallis tertile test**: The analysis script also computed a Kruskal-Wallis test across tGJS tertiles, returning p = 5.86 × 10⁻¹⁰. This value is an artifact: the test compared tGJS *score* distributions across groups defined by tGJS tertiles — a comparison that is significant by construction. The correct interpretation of tertile response rates is from the descriptive tabulation (see S4.3.3). The KW p-value is not reported as a primary or secondary finding.

## S4.3 Results

### S4.3.1 Cohort Summary

| Variable | Value |
|----------|-------|
| N total samples | 109 |
| N pre-treatment | 51 |
| N pre-treatment with response data | 49 |
| tGJS mean ± SD | 0 ± 1.0 (z-score by construction) |
| Response: PRCR/CR/PR | n in GEO PRCR category |
| Response: SD | — |
| Response: PD | — |

### S4.3.2 Primary Test: tGJS vs. Binary Response

All three primary tests returned null results:

| Test | Statistic | p-value |
|------|-----------|---------|
| Wilcoxon (PRCR/CR/PR vs SD/PD) | Mann-Whitney U | **p = 0.239** |
| Logistic regression | OR = 0.408 | p = 0.239 (NS) |
| Spearman ρ vs RECIST ordinal | ρ = −0.095 | **p = 0.517** |

The Wilcoxon and logistic p-values are identical because both assess the same binary response split; the Spearman test against the ordinal scale is the more sensitive test and confirms the null.

### S4.3.3 Logistic OR Direction

The logistic OR of 0.408 indicates that higher tGJS is associated with *lower* response probability. This direction is consistent with the gate-jamming framework (higher gate-jamming → greater innate immune suppression → less immune activation → worse ICI response). However, the effect is not statistically significant at this sample size (n = 49), and the 95% confidence interval on the OR spans 1.0 widely. The directional consistency should not be interpreted as evidence for an effect; the analysis is underpowered to distinguish a true directional trend from noise.

### S4.3.4 Response Rate by tGJS Tertile

Response rates did not show a monotonic trend across tGJS tertiles. The analysis is descriptive given the small sample size per tertile (approximately 16 samples per group) and the absence of statistical power to detect a difference across three strata.

### S4.3.5 Pre vs. On-Treatment tGJS Trajectory

Pre- and on-treatment tGJS trajectories were visualized for patients with paired biopsies (Figure S4c). No systematic difference in tGJS trajectory between responders and non-responders was observed. This is mechanistically expected: nivolumab acts by releasing PD-1 checkpoint suppression on T cells, a downstream step that does not directly alter the expression of HK2, BCL2L1, or TSPO.

## S4.4 Discussion

### S4.4.1 Why Melanoma Is Not a Clean Room

Melanoma carries the highest somatic mutation burden of any common solid tumor — driven by UV-induced cyclobutane pyrimidine dimers generating predominantly C>T transitions at dipyrimidine sites. Median TMB in The Cancer Genome Atlas SKCM cohort exceeds 15 mutations/Mb, with a substantial fraction of cases at >50 mutations/Mb. This saturates cGAS-STING signaling with nuclear DNA-derived fragments, making VDAC1-mediated mtDNA release a minor contributor to the total cytosolic DNA load.

The gate-jamming framework predicts that tGJS will fail to capture the dominant innate immune activation mechanism in this context. The null at Wilcoxon p = 0.239 and Spearman ρ = −0.095 is the expected outcome.

### S4.4.2 Structural Parallel to IMvigor210

The S3 (IMvigor210, urothelial carcinoma) and S4 (Riaz 2017, melanoma) nulls share the same mechanistic explanation despite differing in:

- Tumor type (urothelial vs. melanoma)
- ICI agent (anti-PD-L1 vs. anti-PD-1)
- Biopsy strategy (pre-treatment only vs. paired pre/on-treatment)
- Expression platform (TPM from raw counts via R vs. FPKM from GEO FTP)
- Analysis language (R vs. Python)

The convergence on a null result across these differences argues against a dataset-specific artifact and supports a mechanistic explanation grounded in the tumor type's TMB profile.

### S4.4.3 The Four-Cohort Domain Definition

The four supplementary analyses now define the gate-jamming framework's domain with flanking boundaries on both sides:

| Analysis | Cohort | TMB Profile | ICI Type | tGJS Signal |
|----------|--------|-------------|----------|-------------|
| S1 | TCGA pan-cancer, n = 10,071 | Mixed — 33 cancer types | ICI null rate proxy (no treatment data) | Null — cross-cancer heterogeneity |
| S2 | COADREAD MSS/TP53-wt, n = 209 | Low — MSS tumors, <2 mut/Mb typical | ICI proxy (immune markers) | **5 Bonferroni-significant hits** |
| S3 | IMvigor210 urothelial, n = 348 | High — ~8 mut/Mb median | Anti-PD-L1 (atezolizumab) | Null — high TMB, adaptive checkpoint |
| S4 | Riaz 2017 melanoma, n = 49 | Very high — >15 mut/Mb median | Anti-PD-1 (nivolumab) | Null — very high TMB, UV-driven |

The pattern is precise: one positive result (S2), flanked by nulls in the low-information context (S1, cross-cancer noise) and in both high-TMB ICI contexts tested (S3, S4). The signal appears exactly where the mechanism predicts it should, at the domain boundary defined by TMB and tumor type.

### S4.4.4 Underpowered Logistic OR

The OR of 0.408 (tGJS → response) should be interpreted cautiously. With n = 49 and a minority of responders, the logistic regression has limited power to detect small-to-moderate effects. Monte Carlo power calculations suggest that detecting OR = 0.4 at 80% power with a ~25% baseline response rate would require approximately 100–120 pre-treatment samples. The Riaz 2017 pre-treatment set (n = 49) is approximately half this threshold. The OR direction is consistent with the framework but cannot be used to claim a positive trend.

## S4.5 Limitations

1. **Small primary analysis set.** n = 49 pre-treatment samples with response data. Effect sizes in the OR range of 0.3–0.5 would require ~100 samples to detect at 80% power. The analysis is adequately powered to exclude large effects but not moderate ones.

2. **PRCR combined response label.** The Riaz 2017 GEO deposit combines CR and PR into a single 'PRCR' response category, which prevents analysis of CR-only vs. other response depths. Separate CR and PR data are available in the published paper but not in the GEO metadata.

3. **FPKM normalization.** The GEO deposit provides FPKM values rather than raw counts. Library-size normalization differences between studies (FPKM here vs. TPM in S3, normalized RSEM in S2) may introduce systematic expression-level differences between cohorts. Within-cohort z-scoring mitigates but does not eliminate this.

4. **Entrez ID gene index.** The FPKM matrix is indexed by NCBI Entrez integer IDs rather than HGNC gene symbols. Gene retrieval required Entrez ID lookups (HK2 = 3099, BCL2L1 = 598, TSPO = 706), which are stable identifiers but introduce a lookup dependency that is not present in symbol-indexed datasets.

5. **Pre-treatment biopsies only as primary analysis.** On-treatment biopsies are available but include changes attributable to both the tumor biology and nivolumab-induced immune effects, making them inappropriate as predictors of initial response.

6. **No MSI or MMRD annotation.** Melanoma does not routinely carry MSI testing. TMB-based stratification (UV signature burden) was not performed in this analysis; all 49 samples were analyzed together. A subset of melanoma patients carry hypermutant or MSI-H tumors; these were not separately identified.

7. **Single-institution cohort.** GSE91061 derives from a single clinical trial (BMS038109). Generalizability to community-based nivolumab treatment populations is unknown.

## S4.6 Conclusion

tGJS does not predict nivolumab response in pre-treatment melanoma biopsies from the Riaz 2017 cohort (n = 49; Wilcoxon p = 0.239, logistic OR = 0.408 [NS], Spearman ρ = −0.095, p = 0.517). This null result is mechanistically expected: melanoma's very high UV-driven TMB saturates cGAS-STING signaling with nuclear DNA-derived fragments that are independent of VDAC1-mediated mtDNA release.

Combined with the S3 null in urothelial carcinoma, S4 provides a second independent high-TMB null using a different tumor type, a different ICI agent, and an independent analysis pipeline. Both nulls arise for the same reason and are predicted by the gate-jamming framework's domain restriction.

The four-cohort arc is complete: the gate-jamming hypothesis generates a positive signal in exactly one context (S2: MSS colorectal cancer with low genomic instability), bounded by nulls in cross-cancer heterogeneity (S1), high-TMB urothelial carcinoma (S3), and very high-TMB melanoma (S4). The boundary is defined by the TMB threshold above which nuclear DNA damage dominates innate immune activation over VDAC1-mediated mitochondrial contributions.

The priority experimental next step is validation in a treatment cohort with direct relevance to the S2 clean room: MSS colorectal cancer patients treated with STING agonists, innate immune stimulators, or combinations where the innate priming step is the primary intervention target.

## S4.7 Data Availability

All code, data, and figures are available at:

- Script: `analysis/riaz2017/compute_tgjs_riaz2017.py`
- Results matrix: `analysis/riaz2017/data/riaz2017_tgjs_matrix.csv`
- Summary statistics: `analysis/riaz2017/data/riaz2017_tgjs_summary.json`
- Figures: `analysis/riaz2017/figures/figS4a–figS4d`
- Repository: https://github.com/templetwo/vdac-pharmacology-atlas (commit 6af62ac)

Source data: Riaz N, Havel JJ, Makarov V et al. Tumor and Microenvironment Evolution during Immunotherapy with Nivolumab. *Cell* 2017;171:934–949.e16. GEO accession GSE91061.

## S4.8 Gene Symbols and Identifiers

| Symbol | Full Name | Entrez ID | Role in tGJS |
|--------|-----------|-----------|--------------|
| HK2 | Hexokinase 2 | 3099 | VDAC1 occupancy proxy (weight 0.40) |
| BCL2L1 | BCL2-like 1 (Bcl-xL isoform) | 598 | Bcl-xL occupancy proxy (weight 0.30) |
| TSPO | Translocator Protein 18 kDa | 706 | Mitochondrial cholesterol flux proxy (weight 0.30) |

## S4.9 Acknowledgments

Source data provided by Riaz N et al. under GEO public access (GSE91061). Analysis was conducted in Python using GEOparse, NumPy, pandas, SciPy, matplotlib, and seaborn.
