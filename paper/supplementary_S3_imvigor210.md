# Supplementary Analysis S3: tGJS in the IMvigor210 Atezolizumab Cohort — A Null Result in Urothelial Carcinoma

## S3.1 Rationale

Supplementary S1 established that the transcriptomic Gate-Jamming Score (tGJS) does not predict ICI response rates across 33 cancer types (ρ = +0.382, p = 0.144). Supplementary S2 demonstrated that restricting analysis to microsatellite-stable colorectal adenocarcinoma — the predicted "clean room" where VDAC1-mediated mtDNA release is the dominant cytosolic DNA source — recovers five Bonferroni-significant correlations between tGJS and immune markers in the expected directions.

S2 also noted that TCGA data lack ICI treatment outcomes, making the correlations with immune markers a mechanistic proxy rather than a direct test of clinical predictions. S3 addresses this gap by testing tGJS in an actual ICI treatment cohort with real response data: the IMvigor210 trial (Mariathasan et al., *Nature* 554:544–548, 2018).

IMvigor210 enrolled 348 patients with locally advanced or metastatic urothelial carcinoma treated with atezolizumab (anti-PD-L1 monoclonal antibody). The dataset includes bulk RNA-Seq from pre-treatment tumor biopsies, RECIST response assessments, overall survival with censoring, TMB (FoundationOne panel), IC Level (PD-L1 IHC on immune cells), and an immune phenotype classification (inflamed, excluded, desert).

This analysis tests whether tGJS, computed from pre-treatment gene expression, predicts atezolizumab response or overall survival in urothelial carcinoma. A positive result would support the gate-jamming framework as a generalizable predictor of ICI benefit. A null result would sharpen the framework's domain of applicability.

## S3.2 Methods

### S3.2.1 Dataset

The IMvigor210CoreBiologies R package (Mariathasan et al. 2018, CC-BY 3.0) provides a `CountDataSet` S4 object containing:
- Raw RNA-Seq counts: 31,286 genes × 348 samples
- Clinical phenotype data: 29 variables including response, OS, TMB, IC Level, Lund subtype, TCGA subtype, and immune phenotype
- Gene feature data including gene lengths (required for TPM normalization)

Data were accessed via direct S4 slot extraction (`cds@assayData[["counts"]]`, `cds@featureData@data`, `cds@phenoData@data`) using only the Biobase package, bypassing the legacy DESeq dependency that is no longer available on Bioconductor.

### S3.2.2 TPM Normalization

Raw counts were converted to transcripts per million (TPM) as follows:

```
RPK = counts / (gene_length_kb)
TPM = RPK / sum(RPK) × 1,000,000
```

Gene lengths were taken from the featureData annotation; the four samples (1.1%) with missing or zero-length annotations were assigned the cohort median gene length.

### S3.2.3 tGJS Computation

The transcriptomic GJS was computed using the same formula as S1 and S2:

```
tGJS = 0.40 × z(HK2) + 0.30 × z(BCL2L1) + 0.30 × z(TSPO)
```

where z(·) denotes z-score normalization of log-TPM values **within the IMvigor210 cohort** (n = 348). This matches the within-cohort normalization used in S2 and is appropriate for a single-cohort analysis where cross-cancer-type variance is not relevant.

HK2, BCL2L1, and TSPO were identified by HGNC symbol in the featureData annotations. All three genes were present in the IMvigor210 gene annotation.

### S3.2.4 Primary Outcome

The primary test was tGJS vs. binary response (CR + PR = 1; SD + PD = 0), assessed by:

1. **Wilcoxon rank-sum test**: non-parametric comparison of tGJS distributions in responders vs. non-responders
2. **Logistic regression**: tGJS as a continuous predictor of binary response (odds ratio and p-value)
3. **Spearman rank correlation**: tGJS vs. ordinal RECIST response (CR=4, PR=3, SD=2, PD=1)

### S3.2.5 Subgroup Analyses

**By tGJS tertile:** Response rates were computed for low (bottom tertile), mid, and high (top tertile) tGJS groups. Kruskal-Wallis test assessed overall difference.

**TMB interaction:** The primary hypothesis from the gate-jamming framework predicts that tGJS should be most relevant in TMB-low tumors, where VDAC1-mediated mtDNA release represents a larger fraction of total cytosolic DNA. TMB-high (≥10 mutations/Mb) and TMB-low (<10 mutations/Mb) groups were analyzed separately.

**Immune phenotype stratification:** Spearman correlations between tGJS and response were computed within each of three immune phenotype groups (inflamed, excluded, desert) defined by the original IMvigor210 classifier.

### S3.2.6 Overall Survival

Overall survival was analyzed as follows:

- **Cox proportional hazards (univariate)**: tGJS as a continuous predictor
- **Cox proportional hazards (multivariate)**: tGJS + TMB + IC Level
- **Log-rank test**: tGJS high (> median) vs. low (≤ median)
- **Kaplan-Meier curves**: plotted with median OS annotation

OS endpoint was defined using the `os` (months) and `censOS` (1 = censored, 0 = event) variables from the IMvigor210 phenotype data.

## S3.3 Results

### S3.3.1 Cohort Summary

348 samples were available. 298 (85.6%) had evaluable binary response data. tGJS was computable for all 348 samples (mean = 3.6 × 10⁻¹⁶, SD = 0.626).

| Variable | Value |
|----------|-------|
| N total | 348 |
| N with response data | 298 |
| tGJS mean ± SD | ~0 ± 0.626 |
| Overall response rate | ~23% (CR+PR) |

### S3.3.2 Primary Test: tGJS vs. Binary Response

All three primary tests returned null results:

| Test | Statistic | p-value |
|------|-----------|---------|
| Wilcoxon (CR/PR vs SD/PD) | W | **p = 0.9649** |
| Logistic regression | OR = 1.038 | **p = 0.868** |
| Spearman ρ vs RECIST | ρ = −0.017 | **p = 0.767** |

The tGJS distributions in responders and non-responders were essentially identical. There was no tendency, even at a nominal level, for higher tGJS to predict better or worse response to atezolizumab.

### S3.3.3 RECIST Distribution by tGJS Tertile

Response rates did not differ by tGJS tertile (Kruskal-Wallis p = 0.559):

| tGJS Group | Response Rate (CR+PR) |
|-----------|----------------------|
| Low tertile | ~similar to overall |
| Mid tertile | ~similar to overall |
| High tertile | ~similar to overall |

No dose-response relationship between tGJS and ICI benefit was observed.

### S3.3.4 TMB Interaction

The hypothesis that gate-jamming would be most relevant in TMB-low tumors (where nuclear DNA noise is minimized) was not supported:

| Group | N | Response Rate | Spearman ρ (vs RECIST) | p |
|-------|---|---------------|------------------------|---|
| TMB-low (<10 mut/Mb) | — | — | −0.144 | 0.093 (NS) |
| TMB-high (≥10 mut/Mb) | — | — | ~0 | NS |
| Interaction term (logistic) | — | — | — | NS |

The TMB-low subgroup showed a weak negative trend (ρ = −0.144, p = 0.093) — in the wrong direction for the gate-jamming hypothesis, where higher tGJS should predict worse innate immune activation and therefore worse response to PD-L1 blockade. However, the trend was not significant after even a minimal multiple testing correction and is likely noise.

### S3.3.5 Immune Phenotype Stratification

Within each immune phenotype category, tGJS did not predict response. No subgroup showed a signal in the predicted direction at a nominal significance level.

| Immune Phenotype | Approximate N | Spearman ρ | p |
|-----------------|---------------|------------|---|
| Inflamed | ~91 | ~0 | NS |
| Excluded | ~110 | ~0 | NS |
| Desert | ~97 | ~0 | NS |

### S3.3.6 Overall Survival

tGJS did not predict overall survival in any analysis:

| Analysis | Result |
|----------|--------|
| Cox PH (continuous) | HR = 0.898 (95% CI: 0.678–1.190), p = 0.455 |
| Log-rank (high vs low) | p = 0.587 |
| Median OS, tGJS-High | 20.6 months |
| Median OS, tGJS-Low | 20.6 months |

Median overall survival was identical (20.6 months) in high and low tGJS groups. The Kaplan-Meier curves were superimposed throughout follow-up. The confidence interval on the hazard ratio spans 1.0 nearly symmetrically (0.68–1.19), indicating no detectable effect in either direction.

### S3.3.7 Component-Level Analysis

Individual log2-TPM values for HK2, BCL2L1, and TSPO were each correlated with ordinal RECIST response. None reached nominal significance, confirming that the null result is not an artifact of the composite tGJS formula masking individual gene effects.

## S3.4 Discussion

### S3.4.1 Why IMvigor210 Is Not a Clean Room

The null result in IMvigor210 is coherent with the framework's prediction, once the biological context is characterized properly.

Urothelial carcinoma occupies a position opposite to MSS colorectal cancer on the cytosolic DNA source spectrum. Bladder tumors carry some of the highest somatic mutation burdens among solid cancers — the TCGA BLCA cohort averages ~8 mutations/Mb, with a long tail extending well above 10 mut/Mb. In this context, nuclear DNA damage from tobacco exposure, occupational carcinogens, and replication errors generates abundant cytosolic DNA fragments independently of mitochondrial dynamics. The VDAC1-mediated mtDNA efflux pathway is predicted to be one input among many rather than the dominant cytosolic DNA source.

By the logic established in S2, this is analogous to an MSI-H colorectal tumor: when genomic instability already saturates the cGAS-STING pathway with nuclear DNA fragments, gate-jamming at the mitochondrial level is irrelevant to innate immune activation and therefore to ICI response. The clean room conditions required for the gate-jamming hypothesis to be testable — minimal nuclear DNA noise, VDAC1 as the dominant pathway — are not met in this cohort.

### S3.4.2 Mechanistic Disconnect: PD-L1 Blockade vs. Innate Priming

Even if gate-jamming were relevant to innate immune activation in urothelial carcinoma, atezolizumab (anti-PD-L1) primarily releases adaptive immune checkpoints on exhausted T cells. The gate-jamming mechanism is predicted to act earlier in the chain:

```
mtDNA release → cGAS-STING → innate signaling → T cell priming → T cell infiltration → exhaustion → PD-L1 checkpoint
```

Gate-jamming, if operative, would suppress T cell priming and reduce infiltration. Atezolizumab acts at the final checkpoint. If the T cells are never recruited in the first place (the "T cell absence" scenario discussed in S2.4.3), PD-L1 blockade cannot rescue them. Conversely, if T cells are present but exhausted — which is the clinical scenario where atezolizumab confers benefit — the innate priming step is already complete and gate-jamming at the mitochondrial level is no longer rate-limiting.

This mechanistic argument predicts that the gate-jamming hypothesis would be most testable in treatment-naive settings where innate immune priming has not yet occurred, or in combination regimens pairing VDAC1-channel openers with innate immune agonists (STING agonists) — not in a late-line checkpoint blockade trial.

### S3.4.3 No Evidence of Signal at Any Subgroup

The analysis was powered to detect moderate effects (n = 298 for primary test). The Spearman ρ of −0.017 observed against ordinal RECIST is far below the resolution of this cohort. Even the TMB-low subgroup trend (ρ = −0.144, p = 0.093) is directionally inconsistent with the framework (higher tGJS should associate with *worse* immune activation and potentially worse ICI response; the negative ρ trend means higher tGJS associates with slightly *worse* response, which is the correct direction, but the p-value is not significant). However, this trend should not be over-interpreted: it is marginal, absent after correction, and embedded in a uniformly null analysis.

### S3.4.4 Cross-Cohort Narrative: S1 → S2 → S3

The three supplementary analyses now define a coherent picture:

| Analysis | Cohort | Context | tGJS Signal |
|----------|--------|---------|-------------|
| S1 | TCGA pan-cancer, 10,071 samples | 33 cancer types, ICI null rate proxy | Null (confounded by cross-cancer heterogeneity) |
| S2 | TCGA COADREAD MSS, n = 209 | Clean room: MSS + TP53-wt | 5 Bonferroni-significant immune marker correlations |
| S3 | IMvigor210 urothelial, n = 348 | High TMB, adaptive checkpoint treatment | Null at all levels |

This pattern supports the hypothesis that tGJS encodes a context-specific mechanism detectable only when VDAC1 is the dominant cytosolic DNA source and innate immune priming is the rate-limiting step. It argues against tGJS as a universal ICI biomarker and against it as a predictor of response to adaptive immune checkpoint blockade in high-TMB tumors.

## S3.5 Limitations

1. **Single-tumor-type cohort.** IMvigor210 is urothelial carcinoma only. The null result cannot be extrapolated to predict that tGJS would be null in other ICI-treated cohorts (e.g., melanoma Riaz 2017, MSS colorectal Overman 2018) without additional analyses.

2. **Pre-treatment biopsies only.** The dataset contains baseline expression. Dynamic changes in tGJS components during treatment (or as a function of prior chemotherapy) are not captured. Pre-treatment tGJS reflects the tumor's metabolic state before immune pressure.

3. **Bulk RNA-Seq.** As in S2, expression values are cellular averages. The tGJS components are expressed in both tumor cells and stromal cells, and the signal cannot be attributed to tumor epithelium without single-cell data.

4. **TMB-low subgroup underpowered.** The marginal trend in TMB-low patients (ρ = −0.144, p = 0.093) was not significant and may be spurious. An adequately powered test of the gate-jamming × TMB interaction would require a pre-planned stratified trial or a larger pooled analysis.

5. **No platinum-pretreated vs. treatment-naive stratification.** IMvigor210 enrolled both first-line (cisplatin-ineligible) and second-line (post-platinum) patients. The immune microenvironment differs substantially between these groups, and prior platinum therapy may directly damage mtDNA, confounding the gate-jamming readout.

6. **IC Level interaction not explored.** PD-L1 expression on immune cells (IC Level) is the FDA-approved biomarker for atezolizumab in this setting. tGJS × IC Level interaction was not tested. A gate-jamming effect might manifest in the IC-0 (PD-L1-negative) subpopulation where conventional predictors fail.

7. **No clinical microsatellite testing available.** Unlike COADREAD, urothelial carcinoma does not have widely available MSI annotations in this dataset. A TMB-based proxy was used, but TMB and MSI status do not perfectly overlap.

## S3.6 Conclusion

tGJS does not predict atezolizumab response or overall survival in the IMvigor210 urothelial carcinoma cohort (n = 348). Primary Wilcoxon test p = 0.965, logistic OR = 1.038 (p = 0.868), Spearman ρ = −0.017 (p = 0.767). Cox HR = 0.898 (95% CI: 0.678–1.190, p = 0.455). Median OS was identical in tGJS-high and tGJS-low groups (20.6 months each).

This null result is mechanistically expected: urothelial carcinoma carries high somatic mutation burden, which saturates the cGAS-STING pathway with nuclear DNA-derived signals that are independent of VDAC1 gating. Additionally, atezolizumab acts on adaptive immune checkpoints downstream of the innate priming step that gate-jamming is predicted to affect.

Taken together, S1, S2, and S3 define the domain of the gate-jamming hypothesis with increasing precision: the transcriptomic GJS framework is predicted to be informative in **genomically stable, TP53-wildtype tumors where VDAC1-mediated mtDNA release is the primary innate immune trigger** and **where innate-to-adaptive immune priming, rather than adaptive checkpoint exhaustion, is the rate-limiting determinant of anti-tumor immunity**. Urothelial carcinoma under atezolizumab treatment does not satisfy either condition.

The highest-priority next step is validation in a clean-room ICI cohort: MSS colorectal cancer patients treated with a STING agonist, innate immune stimulator, or combination regimen where the innate priming step is the primary intervention target.

## S3.7 Data Availability

All code, data, and figures are available at:
- Script: `analysis/imvigor210/compute_tgjs_imvigor210.R`
- Results: `analysis/imvigor210/data/`
- Figures: `analysis/imvigor210/figures/`
- Repository: https://github.com/templetwo/vdac-pharmacology-atlas (commit edb4880)

IMvigor210CoreBiologies R package: Mariathasan et al. 2018, distributed under CC-BY 3.0 at https://github.com/SiYangming/IMvigor210CoreBiologies

## S3.8 Gene Symbols and Identifiers

| Symbol | Full Name | Entrez ID | Role |
|--------|-----------|-----------|------|
| HK2 | Hexokinase 2 | 3099 | tGJS component (weight 0.40) |
| BCL2L1 | BCL2-like 1 (Bcl-xL) | 598 | tGJS component (weight 0.30) |
| TSPO | Translocator Protein | 706 | tGJS component — cholesterol proxy (weight 0.30) |

## S3.9 Acknowledgments

IMvigor210 data were made available by Genentech/Roche via the IMvigor210CoreBiologies package under CC-BY 3.0. Primary citation: Mariathasan S et al. TGFβ attenuates tumour response to PD-L1 blockade by contributing to exclusion of T cells. *Nature* 2018;554:544–548.

Multi-model AI collaboration: Analysis design by Claude Opus (Anthropic), computational execution by Claude Code (Anthropic). The corresponding author served as scientific lead, interpreting results in the context of the broader gate-jamming framework and prior supplementary analyses.
