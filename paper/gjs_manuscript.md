# Context-Specific Innate Immune Evasion via VDAC1 Gate-Jamming in Microsatellite-Stable Colorectal Cancer: A Three-Cohort Transcriptomic Analysis

**Anthony J. Vasquez Sr.**

Delaware Valley University, Doylestown, PA, USA

**Corresponding author:** vasquezaj3921@delval.edu

---

## Abstract

Immune checkpoint inhibitors (ICIs) have transformed oncology for microsatellite instability-high (MSI-H) colorectal cancer, yet 85–95% of colorectal cancer patients carry microsatellite-stable (MSS) tumors and derive no benefit from current ICI regimens. We propose that VDAC1-mediated mitochondrial DNA (mtDNA) gate-jamming — suppression of VDAC1 oligomerization by HK-II docking, Bcl-xL binding, and outer mitochondrial membrane cholesterol loading — explains this selectivity by silencing the cGAS-STING innate immune signal required for spontaneous T cell priming. To test this hypothesis at scale, we computed a transcriptomic Gate-Jamming Score (tGJS = 0.4 × HK2 + 0.3 × BCL2L1 + 0.3 × TSPO, rank-normalized) and conducted three sequential analyses: (S1) pan-cancer TCGA (n = 10,071, 33 cancer types) — null result (ρ = +0.38 vs ICI response rate, p = 0.14); (S2) COADREAD MSS/TP53-wildtype clean room (n = 209) — five Bonferroni-significant inverse correlations between tGJS and immune markers including HAVCR2 (ρ = −0.349, p_bonf = 5 × 10⁻⁶), CXCL10 (ρ = −0.231, p_bonf = 0.015), and cGAS (ρ = −0.208, p_bonf = 0.049); (S3) IMvigor210 urothelial carcinoma atezolizumab cohort (n = 348) — null result (Wilcoxon p = 0.965, Cox HR = 0.898, p = 0.455). The flanking nulls (S1, S3) define the framework's domain: the gate-jamming signal is detectable only when VDAC1-mediated mtDNA release is the dominant cytosolic DNA source and innate priming is the rate-limiting step. The S2 clean room results, combined with the three-layer therapeutic hypothesis (VDAC1 gate-opener + cGAMP/DNA eraser inhibitor + checkpoint blockade) independently derived from the same data by three AI analytical systems, motivates protein-level validation in MSS colorectal cancer and combination ICI trials in this specific population.

**Keywords:** VDAC1, gate-jamming, cGAS-STING, microsatellite-stable colorectal cancer, innate immunity, immunotherapy resistance, tGJS

---

## 1. Introduction

Colorectal cancer is the second leading cause of cancer mortality in the United States, with approximately 150,000 new cases annually. Pembrolizumab and nivolumab achieve durable responses in the ~5–15% of patients with MSI-H tumors — where pervasive genomic instability generates abundant mutational neoantigens and activates innate immune sensing. For the remaining 85–95% of patients with MSS tumors, ICI monotherapy has consistently failed in randomized trials, and no predictive biomarker identifies a responsive MSS subpopulation. The central unmet need in colorectal cancer immunotherapy is converting MSS tumors from immune-cold to immune-hot.

VDAC1 (voltage-dependent anion channel 1) is the most abundant protein in the outer mitochondrial membrane, present at densities exceeding 1,000 molecules per μm². Its oligomeric form releases 500–650 bp mitochondrial DNA (mtDNA) fragments into the cytoplasm (Kim et al. 2019, *Science*), activating the cGAS-STING innate immune pathway required for spontaneous CD8+ T cell priming (Woo et al. 2014, *Immunity*). Cancer cells suppress this oligomerization through at least three mechanisms: hexokinase-II (HK-II) docking on VDAC1's outer barrel (Wolf et al. 2023, *Science Immunology*; Bieker et al. 2025, *Communications Biology*), Bcl-xL binding via its BH4 domain (Monaco et al. 2015, *JBC*), and cholesterol loading of the outer mitochondrial membrane (Betaneli et al. 2012, *Biophysical Journal*). Together, these constitute a gate-jamming architecture that silences the mitochondrial innate immune alarm.

Critically, this mechanism is predicted to be relevant precisely in MSS tumors. In MSI-H tumors, nuclear DNA damage generates cytosolic DNA fragments independently of mitochondrial dynamics, saturating cGAS-STING regardless of VDAC1 state. In MSS tumors where nuclear DNA damage is minimal, VDAC1-mediated mtDNA release is the predicted dominant — potentially sole — cytosolic DNA source. Gate-jamming in this context suppresses the entire innate priming axis, explaining ICI failure without invoking T cell exhaustion.

We formalized this hypothesis as a transcriptomic Gate-Jamming Score (tGJS) and conducted three sequential analyses designed to test the framework, define its domain, and identify the biological context where protein-level validation is most warranted.

---

## 2. Methods

### 2.1 Transcriptomic Gate-Jamming Score

The tGJS is a rank-normalized composite of three genes encoding the primary VDAC1 gate-jamming proteins:

```
tGJS = 0.40 × norm(HK2) + 0.30 × norm(BCL2L1) + 0.30 × norm(TSPO)
```

HK2 encodes hexokinase-II (VDAC1 docking, weight 0.40 reflecting its primacy as the dominant gate-jamming mechanism in most solid tumors); BCL2L1 encodes Bcl-xL (VDAC1 binding, weight 0.30); TSPO encodes the Translocator Protein, a cholesterol transport protein at the outer mitochondrial membrane used as a transcriptomic proxy for mitochondrial cholesterol loading (weight 0.30). Weights are derived from convergent assessment across five independent AI models (see Section 2.4) and are empirical predictions subject to refinement.

Normalization is performed within each cohort (rank-based for TCGA analyses; z-score for IMvigor210 TPM data), ensuring the score reflects relative gate-jamming intensity within the study population rather than cross-cohort expression differences.

### 2.2 S1: Pan-Cancer TCGA Analysis

Expression data for 10,071 samples across 33 TCGA cancer types were retrieved from the TCGA PanCanAtlas (cBioPortal, study: `pan_cancer_atlas_2018`). ICI response rates per cancer type were compiled from published meta-analyses of anti-PD-1/PD-L1 trials (Supplementary Analysis S1). tGJS was correlated with per-cancer-type mean ICI response rate using Spearman rank correlation. Pan-cancer boundary analysis assessed whether TCGA COADREAD tGJS distributions fell within the ranges defined by ICI-responsive and ICI-refractory cancer types.

### 2.3 S2: COADREAD MSS-Stratified Clean Room Analysis

592 COADREAD samples from `coadread_tcga_pan_can_atlas_2018` were stratified by MSI status × TP53 mutation into four groups:
- MSS/TP53-wt (n = 209): MSS/MSI-L + no TP53 mutation — "clean room"
- MSS/TP53-mut (n = 286): MSS/MSI-L + any non-silent TP53 mutation
- MSI-H/TP53-wt (n = 67): negative control
- MSI-H/TP53-mut (n = 28): negative control

MSI status was determined from MANTIS (threshold ≥ 0.4) and MSISensor (threshold > 10) scores retrieved from cBioPortal; MSI-H if either score exceeded threshold. TP53 mutation status was retrieved from the COADREAD mutation profile. Spearman correlations were computed between tGJS and 20 immune/pathway markers in each stratum, with Bonferroni correction for 20 comparisons per stratum. Full marker panel and rationale are described in Supplementary Analysis S2.

### 2.4 S3: IMvigor210 Atezolizumab Cohort

The IMvigor210CoreBiologies R package (Mariathasan et al. 2018) provides pre-treatment bulk RNA-Seq from 348 urothelial carcinoma patients treated with atezolizumab, with RECIST response, overall survival, TMB (FoundationOne), IC Level (PD-L1 IHC), and immune phenotype classification. Raw counts were converted to TPM using gene lengths from featureData annotations. tGJS was computed using z-score normalization within the cohort. Primary tests: Wilcoxon rank-sum (binary response), logistic regression (binary response), Spearman ρ vs. ordinal RECIST, Cox proportional hazards (overall survival), log-rank (tGJS high vs. low). TMB-stratified and immune-phenotype-stratified subgroup analyses were prespecified. Full methods in Supplementary Analysis S3.

### 2.5 Multi-Model Convergence Protocol

The gate-jamming therapeutic hypothesis was evaluated using the IRIS (Independent Replicated Inquiry System) protocol, in which five independent large language models (Claude Opus 4.6, Gemini 2.5 Pro, Grok 4.1 Fast, Mistral Large, DeepSeek Chat) received the identical compiled question without cross-exposure. Claims were extracted and embedded using all-MiniLM-L6-v2 (384-dimensional), clustered by cosine similarity ≥ 0.70, and classified by model agreement (TYPE 0 = 4–5 models, TYPE 1 = 3/5, TYPE 2 = 2/5, TYPE 3 = 1/5). Cross-run analysis across 28 independent runs (27,931 pairwise comparisons) assessed inter-run replication. The protocol is described in full in the companion IRIS Gate Evo repository.

---

## 3. Results

### 3.1 S1: Pan-Cancer tGJS Does Not Predict ICI Response (n = 10,071)

Across 33 TCGA cancer types, tGJS was not inversely correlated with published ICI response rates (Spearman ρ = +0.382, p = 0.144). The positive trend reflects that metabolically aggressive tumors — which have higher tGJS — tend to be the same tumors with higher mutational burden and baseline immune activation, creating a confound that overwhelms any gate-jamming signal at the cross-cancer level. ENPP1 expression showed the strongest pan-cancer inverse correlation with tGJS (ρ = −0.181, p = 4.3 × 10⁻⁷⁵), initially interpreted as evidence of orthogonal evasion strategies (upstream gating vs. downstream cGAMP degradation).

TCGA COADREAD tGJS values fell near the midpoint of the pan-cancer distribution, providing no boundary signal in either direction. The pan-cancer null is consistent with the hypothesis that a cancer-type-homogeneous, immunogenomically stratified analysis is required to observe the gate-jamming signal.

Full results and boundary analysis are reported in Supplementary Analysis S1 (commit 88ff1f7).

### 3.2 S2: MSS/TP53-wt Clean Room Recovers Five Bonferroni-Significant Signals (n = 209)

Restricting analysis to the MSS/TP53-wildtype COADREAD stratum — where VDAC1-mediated mtDNA release is predicted to be the dominant cytosolic DNA source — recovered five markers reaching Bonferroni significance (Table 1), all in directions predicted by the gate-jamming hypothesis:

**Table 1. Bonferroni-significant correlations in the MSS/TP53-wt clean room (n = 209).**

| Marker | Spearman ρ | p_bonf | Direction | Interpretation |
|--------|-----------|--------|-----------|----------------|
| HAVCR2 (TIM-3) | **−0.349** | **5 × 10⁻⁶** | ↓ | Fewer T cells infiltrate to become exhausted |
| TREX1 | **+0.315** | **7 × 10⁻⁵** | ↑ | Co-deployment of mtDNA erasure alongside gate-jamming |
| CXCL10 | **−0.231** | **0.015** | ↓ | Reduced IFN-γ-induced chemokine recruitment |
| STING ratio (acute/chronic) | **−0.216** | **0.034** | ↓ | Residual STING signaling shifts toward immunosuppressive profile |
| cGAS (MB21D1) | **−0.208** | **0.049** | ↓ | Lower cGAS in high-tGJS tumors |

No immune markers reached Bonferroni significance in the MSI-H control strata (n = 67 and n = 28), consistent with the prediction that genomic instability saturates cGAS-STING independently of VDAC1 state.

The ENPP1 anti-correlation (ρ = −0.027, not significant in COADREAD MSS/TP53-wt) did not replicate within the clean room, correcting the S1 interpretation: the pan-cancer ENPP1 signal was driven by cross-cancer-type expression differences rather than a within-tumor-type biological relationship.

Two unexpected findings refined the evasion architecture model:

**TREX1 co-occurrence.** The positive correlation between tGJS and TREX1 (cytosolic DNA exonuclease) indicates that the most evasion-committed MSS tumors co-deploy mitochondrial gate-jamming and cytosolic DNA erasure simultaneously — a belt-and-suspenders strategy rather than an either/or trade-off. This revises the S1 model: ENPP1 (cGAMP degradation) may represent an alternative downstream strategy in non-gate-jamming tumors, while TREX1 co-expression is characteristic of tumors that do gate-jam.

**HAVCR2 as the primary signal.** The strongest anti-correlation was not with effector markers (CD8A, GZMB) but with TIM-3, an exhaustion marker expressed on T cells that have undergone prolonged antigen exposure. This suggests high-tGJS MSS tumors suffer from T cell *absence* rather than T cell *exhaustion* — consistent with the mechanism (suppressed innate priming prevents initial T cell recruitment) and with a clinical implication: these tumors are predicted to be poor candidates for checkpoint inhibitors that target exhaustion checkpoints, but good candidates for interventions that restore the innate priming signal.

Full stratified results, all 20 markers across 4 strata, and 5 figures (S2a–S2e) are in Supplementary Analysis S2 (commit af514d1).

### 3.3 S3: tGJS Does Not Predict Atezolizumab Response in Urothelial Carcinoma (n = 348)

In the IMvigor210 cohort, tGJS showed no association with atezolizumab response or overall survival at any level of analysis:

**Table 2. IMvigor210 primary results (n = 348, n_response = 298).**

| Test | Result | p-value |
|------|--------|---------|
| Wilcoxon (CR/PR vs SD/PD) | — | p = 0.965 |
| Logistic regression | OR = 1.038 | p = 0.868 |
| Spearman ρ vs RECIST | ρ = −0.017 | p = 0.767 |
| Kruskal-Wallis by tertile | — | p = 0.559 |
| Cox PH (continuous) | HR = 0.898 (95% CI: 0.678–1.190) | p = 0.455 |
| Log-rank (high vs low) | — | p = 0.587 |
| Median OS, tGJS-High | 20.6 months | — |
| Median OS, tGJS-Low | 20.6 months | — |

The TMB-low subgroup (predicted to be the most informative by the gate-jamming hypothesis) showed a non-significant negative trend (ρ = −0.144, p = 0.093) in the wrong direction for gate-jamming prediction. No subgroup analysis — by TMB, immune phenotype, or response category — yielded a signal above nominal significance.

This null is mechanistically expected: urothelial carcinoma carries high baseline somatic mutation burden from tobacco and occupational carcinogen exposure, generating nuclear DNA-derived cytosolic DNA independently of VDAC1 state. The clean room conditions required for the gate-jamming hypothesis (MSS, VDAC1 as dominant cytosolic DNA source, innate priming as rate-limiting step) are not present in this cohort. Additionally, atezolizumab targets the adaptive immune checkpoint on exhausted T cells downstream of innate priming; even if gate-jamming were relevant, its effect would operate upstream of the treatment's mechanism of action.

Full results, four figures (S3a–S3d), and mechanistic discussion are in Supplementary Analysis S3 (commit 61048d4).

---

## 4. Discussion

### 4.1 Three Analyses Define the Framework's Domain

The S1→S2→S3 arc is the central finding of this work. It answers not only "is there a signal?" but "where does the signal live?":

| Analysis | Cohort | Context | tGJS Signal |
|----------|--------|---------|-------------|
| S1 | TCGA pan-cancer (n = 10,071) | 33 cancer types, ICI response proxy | Null — cross-cancer confounds |
| S2 | TCGA COADREAD MSS/TP53-wt (n = 209) | Clean room: MSS + intact apoptosis | 5 Bonferroni-significant immune correlations |
| S3 | IMvigor210 urothelial (n = 348) | High TMB, PD-L1 blockade | Null — wrong context, wrong treatment mechanism |

The two nulls are not failures — they are the framework's falsification boundaries. A signal that appears everywhere is not a mechanism; it is noise. A signal that appears precisely where the biology predicts it should appear, and not where the biology predicts it shouldn't, is evidence that the model is capturing something real.

The COADREAD MSS/TP53-wildtype stratum represents the tightest available approximation of the predicted clean room using existing public data: minimal nuclear DNA instability, intact TP53 apoptosis signaling, VDAC1 as the predicted dominant cytosolic DNA source. Five Bonferroni-significant findings from 209 samples, using a three-gene transcriptomic proxy of a physical protein-occupancy mechanism, suggest the biological structure is robust enough to survive a crude measurement instrument.

### 4.2 The Therapeutic Hypothesis: Three Independent Systems, One Stack

The analytical arc motivates a specific three-layer therapeutic intervention. This hypothesis was independently derived by three AI analytical systems (Claude Opus, Gemini Pro, Grok) working from the same data without cross-exposure, converging on identical components:

1. **VDAC1 gate-opener** — displace HK-II from VDAC1 (methyl jasmonate, 2-DG, clotrimazole) to restore oligomerization-dependent mtDNA release and cGAS-STING activation
2. **DNA/cGAMP eraser inhibitor** — inhibit TREX1 or ENPP1 to prevent degradation of the released mtDNA or its downstream signaling product cGAMP, amplifying and sustaining innate immune activation
3. **Checkpoint blockade** — administer anti-PD-1/PD-L1 to prevent exhaustion of the T cells now being recruited and primed by the restored innate signal

The order matters. Gate-opener generates the innate signal; eraser inhibitor sustains it; checkpoint blockade amplifies the adaptive response. Checkpoint blockade alone — the current standard of care for MSS CRC where it is used at all — skips steps one and two.

The TREX1 co-occurrence finding from S2 directly informs step two: the positive correlation between tGJS and TREX1 in the clean room MSS tumors indicates that high-gate-jamming tumors simultaneously upregulate cytosolic DNA erasure. This co-deployment implies that gate-opener alone may be insufficient — released mtDNA may be degraded before cGAS activation occurs. TREX1 inhibition as the eraser step addresses this specifically. An alternative is targeting ENPP1 in non-gate-jamming tumors (where TREX1 is not co-elevated) that still fail ICI through downstream cGAMP degradation.

Three independently reasoning systems arriving at the same three-layer stack from the same data does not constitute experimental validation. It constitutes a prior strong enough to justify the next experiment.

### 4.3 Why MSS Colorectal Is the Right Target

The colorectal cancer context is not incidental. It is where the framework makes its strongest prediction:

MSS colorectal adenocarcinoma has: (1) the largest absolute population of ICI-refractory patients among common cancers where ICI is attempted; (2) well-characterized MSI stratification, allowing clean separation of the signal; (3) an available TP53 mutation axis that further refines the predicted clean room; (4) a tumor biology where VDAC1 docking by HK-II is supported by multiple independent lines of evidence (high HK2 expression, high metabolic dependency on aerobic glycolysis, low baseline TIL infiltration in MSS tumors).

The HAVCR2 finding (ρ = −0.349, the strongest signal in S2) points to T cell absence rather than T cell exhaustion as the immune bottleneck in high-tGJS MSS tumors. This is a meaningful clinical distinction: trials of anti-TIM-3 antibodies in MSS CRC are testing the wrong checkpoint. The problem is upstream of T cell activation, not at the exhaustion checkpoint.

### 4.4 The GJS as One Layer of a Multi-Layer Evasion Architecture

The GJS measures one specific bottleneck — VDAC1 oligomerization suppression — within a multi-layer immune evasion system. Several critical caveats govern interpretation:

**The cGAS-STING axis is not uniformly anti-tumor.** Lai et al. (2025, *Immunity*) showed that VDAC-mediated mtDNA from senescent tumor cells can enhance immunosuppression through MDSC recruitment — the acute, oligomerization-dependent burst (immunogenic) is mechanistically distinct from the chronic low-level leak (potentially immunosuppressive). Gate-restoration is predicted to produce immunogenic cell death signals, but cellular context and timing determine the net immune outcome.

**The tumor microenvironment can override gate-restoration.** Even successful VDAC1 oligomerization and cGAS-STING activation may be insufficient if the TME (CAFs, TAMs, acidosis, hypoxia) prevents effector T cell infiltration. Gate-restoration addresses the innate priming step; TME remodeling may be required as a fourth layer in advanced MSS CRC.

**STING pathway competence must be assessed.** STING silencing via promoter methylation occurs in 1–25% of tumors pan-cancer. A high-GJS tumor with silenced STING requires epigenetic reactivation (DNMT inhibitors) before gate-restoration can be effective. The GJS × STING status matrix generates four distinct therapeutic predictions:

| | **STING Intact** | **STING Silenced** |
|---|---|---|
| **High GJS** | Primary target — gate-opener + eraser inhibitor + checkpoint | Requires DNMT inhibitor before gate-restoration |
| **Low GJS** | Gate open, pathway active — checkpoint alone may suffice | Chronic signaling, paradoxical immunosuppression |

### 4.5 What the tGJS Does Not Capture

The transcriptomic proxy is a deliberate simplification. tGJS measures mRNA abundance of three genes; it cannot distinguish HK-II in the cytosol versus docked on VDAC1, Bcl-xL bound to VDAC1 versus other mitochondrial targets, or TSPO-mediated cholesterol at the outer mitochondrial membrane versus elsewhere. The fact that five Bonferroni-significant signals emerge from this crude proxy suggests the biology is robust; it does not mean the transcriptomic score is sufficient for clinical application.

Protein-level measurement — proximity ligation assay for HK-II–VDAC1 and Bcl-xL–VDAC1 complexes, mitochondrial lipidomics for the Chol/CL ratio — is required to compute the true GJS:

> **GJS = f_HKII × 0.40 + f_BclxL × 0.30 + [Chol]/[CL]_norm × 0.30**

where f_HKII is the fraction of VDAC1 occupied by HK-II and f_BclxL is the fraction bound by Bcl-xL (both 0–1), and [Chol]/[CL]_norm is the molar cholesterol-to-cardiolipin ratio normalized to published physiological and cancer ranges. The tGJS is a screening tool to identify where this protein-level assay should be run first.

### 4.6 Limitations

1. **No experimental validation.** All findings are computational. The gate-jamming mechanism is supported by published structural biology (Bieker et al. 2025, Daniilidis et al. 2025, Kim et al. 2019) but the composite GJS has not been validated against protein-level measurement in any tumor type.

2. **Bulk RNA-Seq.** Expression values are cellular averages across tumor, stromal, and immune cells. Single-cell attribution is required to determine which cell type drives the tGJS signal.

3. **TCGA lacks treatment data.** The S2 correlations are with immune markers, not ICI outcomes. The hypothesis that high-tGJS MSS CRC tumors fail ICI is mechanistically motivated but not directly tested.

4. **IMvigor210 is a single cohort.** The S3 null applies to urothelial carcinoma treated with PD-L1 blockade. It does not predict the outcome in MSS CRC treated with combination gate-restoration regimens.

5. **VBIT-4 specificity.** Ravishankar et al. (2025, bioRxiv) showed VBIT-4 disrupts membranes independent of VDAC1 at ≥30 μM. Claims requiring VBIT-4 experiments demand orthogonal genetic validation (VDAC1/3 knockout, K53R mutants).

6. **TREX1 inhibitors are not clinically available.** The belt-and-suspenders evasion finding implicates TREX1 inhibition as a component of the therapeutic stack, but no clinical-stage TREX1 inhibitor exists. This identifies a drug development gap.

### 4.7 Immediate Next Steps

**In vitro (4–8 weeks):** Displace HK-II from VDAC1 (methyl jasmonate 0.5–3 mM, or clotrimazole 10–50 μM) in immune-cold cell lines (Panc-1, HCT116) and measure cytoplasmic mtDNA by qPCR after digitonin fractionation, p-STING (Ser366) by Western blot, and IFN-β by ELISA. Compute GJS across 15+ cell lines and correlate with basal cGAS-STING activity (Spearman ρ ≤ −0.6 predicted). Predicted effect size d = 0.81–1.22 by Monte Carlo simulation (H1, H2 protocols).

**Protein-level validation in COADREAD tissue (8–12 weeks):** Run proximity ligation assay for HK-II–VDAC1 complexes in MSS vs. MSI-H colorectal cancer tissue sections. Correlate PLA signal with immune infiltration (CD8A IHC) and with tGJS to validate the transcriptomic proxy against protein measurement.

**In vivo (10 weeks):** Gate-restoration combination (methyl jasmonate 100 mg/kg IP + ABT-263 50 mg/kg PO) + anti-PD-1 in 4T1 (immune-cold) and MC38 (immune-hot) syngeneic tumor models. Prediction: synergy (CI < 0.7 by Bliss independence) in 4T1, no added benefit in MC38.

**GSE91061 melanoma validation:** The Riaz 2017 nivolumab cohort (n = 109) provides pre- and on-treatment biopsies in a high-TMB tumor type (predicted null per the S3 logic) and is the next planned validation to confirm the boundary conditions.

---

## 5. Data Availability

All code, data, and figures are openly available:

- **Analysis scripts:** `analysis/tcga_gjs/compute_tgjs.py`, `compute_tgjs_coadread_mss.py`; `analysis/imvigor210/compute_tgjs_imvigor210.R`
- **Supplementary analyses:** `paper/supplementary_S1_pan_cancer.md`, `paper/supplementary_S2_coadread_mss_stratification.md`, `paper/supplementary_S3_imvigor210.md`
- **Repository:** https://github.com/templetwo/vdac-pharmacology-atlas
- **Dataset archive:** https://huggingface.co/datasets/TheTempleofTwo/vdac-pharmacology-atlas
- **OSF preregistration:** https://osf.io/c9rqb/
- **IRIS Gate Evo pipeline:** https://github.com/templetwo/iris-gate-evo

---

## 6. Author Contributions

A.J.V. conceived the research questions, designed the analytical framework, executed all computational analyses, interpreted all results, and wrote the manuscript. Computational analyses were executed with Claude Code (Anthropic). Manuscript drafting was assisted by Claude (Anthropic). The IRIS multi-model convergence protocol was developed and run by A.J.V. using five independent AI systems (Claude Opus, Gemini Pro, Grok, Mistral, DeepSeek); convergence metrics are system-computed. All scientific decisions, interpretations, and conclusions are solely the responsibility of A.J.V.

---

## 7. Competing Interests

The author declares no competing interests. This work received no external funding.

---

## 8. License

This manuscript and all associated data are released under CC BY 4.0.

---

## References

Betaneli V, Petrov EP, Schwille P. (2012) The role of lipids in VDAC oligomerization. *Biophys J* 102:523.

Bieker JT, Timme S, et al. (2025) A membrane-buried glutamate mediates VDAC-hexokinase binding. *Commun Biol* 8:212.

Carozza JA, et al. (2023) ENPP1 as an innate immune checkpoint. *PNAS*.

Daniilidis M, Gunsel U, et al. (2025) Structural basis of apoptosis induction by VDAC1. *Nat Commun* 16:9481.

Fadzeyeva E, et al. (2026) CBD-induced VDAC1 oligomerization-dependent effects. *Pharmaceuticals* 19:95.

Gehrcken L, et al. (2025) cGAS-STING in anti-tumor immunity. *Adv Sci* 12:2500296.

Goicoechea L, et al. (2023) Mitochondrial cholesterol: metabolism and impact on redox biology. *Redox Biol* 61:102643.

Ikeda H, et al. (2025) Mitochondrial transfer from cancer cells to TILs. *Nature*.

Jahn H, Bartos L, Dearden GD, et al. (2023) VDAC1 dimers as phospholipid scramblases. *Nat Commun* 14:8115.

Kim J, et al. (2019) VDAC oligomers form mitochondrial pores to release mtDNA. *Science* 366:1531.

Lafargue K, et al. (2025) Lipid regulation of VDAC1 assemblies. *Commun Biol* 8:936.

Lai J, et al. (2025) VDAC-mediated mtDNA release from senescent tumor cells. *Immunity* 58:811.

Mangalhara KC, et al. (2023) Complex II loss activates MHC-I. *Science* 381:1316.

Mariathasan S, et al. (2018) TGFβ attenuates tumour response to PD-L1 blockade by contributing to exclusion of T cells. *Nature* 554:544.

Monaco G, et al. (2015) The BH4 domain of Bcl-xL targets VDAC1 for Ca²⁺ control. *J Biol Chem* 290:9150.

Montero J, et al. (2008) Mitochondrial cholesterol contributes to chemotherapy resistance in HCC. *Cancer Res* 68:5246.

Prashar A, et al. (2024) VDAC1-dependent inner membrane herniation vesicles. *Nature* 632:1110.

Ravishankar H, et al. (2025) VBIT-4 specificity challenge. *bioRxiv*.

Ren H, et al. (2025) VSTM2L enhances HK2-VDAC1 interaction. *Nat Commun* 16:1534.

Rimmerman N, et al. (2013) Direct modulation of the OMM channel VDAC1 by CBD. *Cell Death Dis* 4:e949.

Samson N, Ablasser A. (2022) The cGAS-STING pathway and cancer. *Nat Cancer* 3:1452.

Shoshan-Barmatz V, et al. (2025) p53 directly binds VDAC1. *Biomolecules* 16:141.

Wan X, et al. (2026) VDAC1 oligomerization regulates PANoptosis. *Neural Regen Res* 21(4).

Wolf AJ, et al. (2023) HK2 dissociation from VDAC1 triggers NLRP3. *Sci Immunol* 8:eade7652.

Woo SR, et al. (2014) STING-dependent cytosolic DNA sensing mediates innate immune recognition of tumors. *Immunity* 41:830.

Xian H, et al. (2022) Oxidized mtDNA exit via mPTP and VDAC channels. *Immunity* 55:1370.
