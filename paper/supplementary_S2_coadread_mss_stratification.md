# Supplementary Analysis S2: COADREAD MSS-Stratified tGJS Clean Room Test

## S2.1 Rationale

Supplementary S1 established that a transcriptomic Gate-Jamming Score (tGJS) computed from pan-cancer TCGA data (n = 10,071) did not predict ICI response rates across cancer types (ρ = +0.382, p = 0.144). However, the pan-cancer analysis aggregated immunogenomically distinct tumor types, each with different mutational burdens, stromal compositions, and baseline immune activation states. This heterogeneity introduces confounders that may obscure a real signal.

A cancer immunology expert (Master's graduate, Reddit user SquidwardHurrHurrHur) identified the critical refinement: **microsatellite-stable (MSS) tumors represent the cleanest test case for the GJS framework**. In MSI-high tumors, pervasive genomic instability generates abundant cytosolic DNA fragments from nuclear sources, activating cGAS-STING independently of mitochondrial DNA release. In MSS/MSI-low tumors, VDAC1-mediated mtDNA efflux is predicted to be the dominant — potentially sole — source of cytosolic DNA capable of triggering innate immune signaling. If the gate-jamming mechanism is physically real, its transcriptomic signature should be most detectable where the gate matters most.

The same expert recommended TP53 stratification (to separate apoptosis-competent from apoptosis-resistant tumors) and colorectal adenocarcinoma (COADREAD) as the target cohort, given its clinical relevance, available MSI annotations, and representation in the existing dataset.

This analysis tests whether the null pan-cancer result reflects true absence of signal or masking by immunogenomic noise.

## S2.2 Methods

### S2.2.1 Cohort Selection

592 COADREAD samples were extracted from the TCGA PanCanAtlas expression dataset used in S1.

### S2.2.2 Clinical Annotations

MSI status was determined using two complementary scores retrieved from cBioPortal (study: `coadread_tcga_pan_can_atlas_2018`):

- **MANTIS score** (557 samples): MSI-H defined as MANTIS ≥ 0.4
- **MSISensor score** (584 samples): MSI-H defined as MSISensor > 10

Samples were classified as MSI-H if either score exceeded its threshold, MSS if both scores were below threshold, or UNKNOWN if neither score was available. Two samples with unknown MSI status were excluded from stratified analyses.

TP53 somatic mutation status was retrieved from cBioPortal mutation data. Samples carrying any non-silent TP53 mutation (missense, nonsense, frameshift, splice site) were classified as TP53-mutant; all others as TP53-wildtype.

**Germline syndrome exclusion:** Standard open-access TCGA clinical data does not include germline variant flags for Lynch syndrome, Li-Fraumeni syndrome, or familial adenomatous polyposis (FAP). However, filtering for MSS/MSI-low status effectively excludes the majority of active Lynch syndrome phenotypes, which present as MSI-H. Li-Fraumeni (germline TP53) cases cannot be distinguished from somatic TP53-mutant tumors without controlled-access germline data. This is acknowledged as a limitation.

### S2.2.3 Stratification

Samples were assigned to four strata based on the 2 × 2 matrix of MSI status × TP53 mutation:

| Stratum | MSI Status | TP53 Status | n | Rationale |
|---------|-----------|-------------|---|-----------|
| MSS/TP53-wt | MSS or MSI-L | Wildtype | 209 | "Clean room" — minimal genomic instability, intact apoptosis, VDAC1 gate as dominant variable |
| MSS/TP53-mut | MSS or MSI-L | Mutant | 286 | Gate-jamming + impaired apoptosis |
| MSI-H/TP53-wt | MSI-H | Wildtype | 67 | Genomic instability noise — negative control |
| MSI-H/TP53-mut | MSI-H | Mutant | 28 | Maximum chaos — expect no coherent signal |

### S2.2.4 tGJS Computation

The transcriptomic GJS was computed using the same formula as S1:

```
tGJS = 0.40 × norm(HK2) + 0.30 × norm(BCL2L1) + 0.30 × norm(TSPO)
```

Critically, rank-based normalization was performed **within the COADREAD cohort** (n = 592), not carried over from the pan-cancer dataset. This ensures the score reflects relative gate-jamming intensity among colorectal tumors rather than cross-cancer-type expression differences.

### S2.2.5 Immune and Pathway Markers

The following markers were assessed, consistent with S1 and extended per expert recommendation:

**Immune infiltration:** CD8A, IFNG, CXCL10, GZMB, PRF1, plus a composite immune proxy score (mean of rank-normalized values).

**T cell exhaustion (new in S2):** HAVCR2 (TIM-3), LAG3, PDCD1 (PD-1), TIGIT. Expression data retrieved from cBioPortal RNA-Seq V2 profile.

**Effector/Exhaustion ratio:** mean(GZMB, PRF1, IFNG) / mean(HAVCR2, LAG3, PDCD1). Values > 1 indicate effector-dominant; values < 1 indicate exhaustion-dominant.

**cGAS-STING pathway:** MB21D1 (cGAS), STING1, ENPP1, TREX1, CD274 (PD-L1).

**Acute vs. chronic STING signatures:** Acute: mean(IFNB1, CXCL10, CCL5). Chronic: mean(IDO1, TGFB1, IL6, ARG1, NOS2). Ratio: z-scored acute minus z-scored chronic.

### S2.2.6 Statistical Analysis

Spearman rank correlations were computed for tGJS against each marker within each stratum. P-values were Bonferroni-corrected for 20 comparisons per stratum (4 strata × 20 markers = 80 total tests). Significance threshold: p_bonf < 0.05.

## S2.3 Results

### S2.3.1 Primary Test: MSS/TP53-wt Clean Room (n = 209)

Five markers reached Bonferroni significance, all in directions consistent with the gate-jamming hypothesis:

| Marker | Spearman ρ | p_bonf | Direction | Interpretation |
|--------|-----------|--------|-----------|----------------|
| HAVCR2 (TIM-3) | **-0.349** | **5 × 10⁻⁶** | ↓ | High tGJS associated with lower T cell exhaustion marker expression — fewer T cells infiltrate to become exhausted |
| TREX1 | **+0.315** | **7 × 10⁻⁵** | ↑ | High tGJS co-occurs with elevated cytosolic DNA exonuclease — dual evasion mechanism (see S2.4.2) |
| CXCL10 | **-0.231** | **0.015** | ↓ | Reduced IFN-γ-induced chemokine — consistent with suppressed upstream innate signaling |
| STING ratio | **-0.216** | **0.034** | ↓ | Residual STING signaling shifts toward chronic/immunosuppressive profile |
| cGAS (MB21D1) | **-0.208** | **0.049** | ↓ | Lower cGAS expression in high-tGJS tumors |

Additional markers showed directional consistency without reaching Bonferroni significance:

| Marker | Spearman ρ | p_raw | Direction |
|--------|-----------|-------|-----------|
| Immune proxy | -0.099 | 0.155 | ↓ Negative |
| CD8A | -0.084 | 0.224 | ↓ Negative |
| GZMB | +0.012 | 0.858 | ~ Null |
| Effector/Exhaustion ratio | +0.167 | 0.016 | ↑ Positive |

The partial sign flip — from uniformly positive pan-cancer correlations to predominantly negative correlations in the clean room — demonstrates that the pan-cancer signal reflected the co-occurrence of metabolic aggression and immune provocation across heterogeneous tumor types. When immunogenomic confounders are removed, the predicted gate-jamming pattern emerges.

The effector/exhaustion ratio remaining positive despite individual exhaustion markers dropping is consistent with both effector and exhaustion transcripts being suppressed in high-tGJS tumors, maintaining or slightly elevating the ratio.

### S2.3.2 MSI-H Negative Control

| Marker | MSI-H/TP53-wt ρ | MSI-H/TP53-mut ρ |
|--------|-----------------|------------------|
| Immune proxy | +0.017 | -0.153 |
| CD8A | +0.052 | -0.146 |
| HAVCR2 | -0.164 | -0.375 |
| cGAS | +0.210 | +0.043 |
| STING ratio | -0.146 | +0.092 |

No immune markers reached Bonferroni significance in MSI-H strata (except effector/exhaustion ratio in the small MSI-H/TP53-mut group, n = 28, which is unreliable). Genomic instability dominates the signaling landscape in these tumors, and tGJS does not predict immune status, consistent with the prediction that VDAC1-mediated mtDNA release is not the rate-limiting step when abundant nuclear DNA fragments are already present in the cytosol.

### S2.3.3 ENPP1 Anti-Correlation Resolved

The pan-cancer ENPP1 anti-correlation (ρ = -0.181, p = 4.3 × 10⁻⁷⁵) identified in S1 was interpreted as evidence of orthogonal evasion strategies. In the COADREAD MSS/TP53-wt subset, ENPP1 correlation with tGJS was ρ = -0.027 (not significant). This attenuation indicates the pan-cancer ENPP1 signal was driven by cross-cancer-type expression differences rather than a within-tumor-type biological relationship. The "orthogonal strategies" interpretation from S1 should be revised: ENPP1 and gate-jamming gene expression are not anti-correlated within colorectal cancer.

### S2.3.4 TP53 Stratification Effect

In the MSS/TP53-mutant stratum (n = 286), most correlations attenuated compared to the TP53-wildtype clean room. Only TREX1 maintained Bonferroni significance. This suggests TP53 mutation introduces additional immunogenomic complexity (altered cell death signaling, modified neoantigen landscape) that partially obscures the gate-jamming signal, consistent with the expert recommendation to layer GJS on top of TP53 status rather than treating it independently.

## S2.4 Discussion

### S2.4.1 The Clean Room Validates the Framework's Domain

The transition from S1 to S2 demonstrates a core principle: the GJS framework describes a specific physical mechanism (HK-II/Bcl-xL/cholesterol occupancy of VDAC1 preventing oligomerization-dependent mtDNA release) that operates in a specific immunogenomic context. In tumors where alternative cytosolic DNA sources dominate (MSI-H), the gate is irrelevant. In tumors where VDAC1-mediated mtDNA release is predicted to be the primary innate immune trigger (MSS, TP53-wildtype), five Bonferroni-significant correlations emerge from a 209-sample cohort using a crude three-gene transcriptomic proxy.

This does not validate the GJS as a clinical biomarker. It establishes that the framework's predictions are detectable at the transcriptomic level when the appropriate biological context is selected.

### S2.4.2 TREX1 Co-Occurrence: Layered Evasion

The positive correlation between tGJS and TREX1 (ρ = +0.315, p_bonf = 7 × 10⁻⁵) was not predicted by the metabolic efficiency model proposed in S1, which suggested tumors would employ either upstream gating (VDAC1 blockade) or downstream erasure (enzymatic cGAMP/DNA degradation) but not both simultaneously.

The COADREAD MSS data suggest a different architecture: the most evasion-committed tumors co-deploy mitochondrial gate-jamming (preventing mtDNA release) and cytosolic DNA exonuclease activity (degrading any DNA that escapes). TREX1 degrades cytosolic double-stranded DNA, preventing cGAS activation (Stetson et al. 2008; Gray et al. 2015). Its co-expression with high tGJS in MSS tumors indicates a belt-and-suspenders strategy rather than an either/or trade-off.

This revises the S1 interpretation: ENPP1 (cGAMP degradation) may represent the alternative downstream strategy employed by tumors that do NOT gate-jam, while TREX1 (DNA degradation) is co-opted by tumors that DO gate-jam as a redundant failsafe. The two "erasers" serve different evasion architectures.

### S2.4.3 HAVCR2 as the Strongest Signal

HAVCR2 (encoding TIM-3) showing the strongest anti-correlation with tGJS (ρ = -0.349) has a straightforward interpretation: TIM-3 is primarily expressed on exhausted T cells that have undergone prolonged antigen exposure. If gate-jamming suppresses the innate immune signal that would recruit and activate T cells in the first place, fewer T cells infiltrate, and therefore fewer reach the exhausted state. The HAVCR2 drop reflects absence of immune engagement rather than reversal of exhaustion.

This aligns with the immunologist's concern about the "recognition vs. stamina" bottleneck: in high-tGJS MSS tumors, the problem may not be T cell exhaustion but T cell absence.

### S2.4.4 Acute-to-Chronic STING Shift

The negative STING ratio correlation (ρ = -0.216) indicates that high-tGJS tumors, when they do exhibit residual STING pathway activity, skew toward the chronic immunosuppressive profile (IDO1, TGFB1, IL6) rather than the acute anti-tumor profile (IFNB1, CXCL10, CCL5). This is consistent with the temporal dynamics model: acute VDAC1-dependent mtDNA bursts are suppressed by gate-jamming, while low-level chronic DNA leak persists and activates the immunosuppressive arm of STING signaling (Bakhoum et al. 2018; Lai et al. 2025).

## S2.5 Limitations

1. **Transcriptomic proxy remains crude.** tGJS measures mRNA abundance of HK2, BCL2L1, and TSPO. It cannot distinguish between HK-II in the cytosol versus docked on VDAC1, Bcl-xL bound to VDAC1 versus other mitochondrial targets, or TSPO-mediated cholesterol at the outer mitochondrial membrane versus elsewhere. Protein-level validation (proximity ligation assay, co-immunoprecipitation, mitochondrial lipidomics) remains essential.

2. **Sample size.** The MSS/TP53-wt stratum (n = 209) provides adequate power for moderate effect sizes but cannot detect subtle interactions. The MSI-H/TP53-mut stratum (n = 28) is underpowered and its results should be interpreted cautiously.

3. **Bulk RNA-seq.** Expression values represent averages across tumor cells, stromal cells, and infiltrating immune cells. CIBERSORTx deconvolution or single-cell RNA-seq would be required to attribute expression changes to specific cell populations.

4. **ESTIMATE scores.** Pre-computed ESTIMATE immune and stromal scores were not available for this analysis. The immune proxy score (mean of rank-normalized CD8A, IFNG, CXCL10, GZMB, PRF1) is a simplified substitute. Future analyses should incorporate full ESTIMATE or MCPcounter deconvolution.

5. **Germline confounders.** Li-Fraumeni syndrome cases (germline TP53 mutations) cannot be distinguished from somatic TP53-mutant tumors without controlled-access germline data from dbGaP.

6. **No ICI response data.** TCGA samples were collected before widespread ICI use. The correlation between tGJS and immune markers is a mechanistic proxy, not a direct test of treatment response. Validation in ICI-treated cohorts (IMvigor210, Hugo 2016, Riaz 2017) is the necessary next step.

7. **Correction of S1 interpretation.** The ENPP1 anti-correlation reported in S1 as evidence of orthogonal evasion strategies does not replicate within COADREAD MSS tumors. This finding should be interpreted as a cross-cancer-type artifact until validated in additional single-cancer-type analyses.

## S2.6 Conclusion

The COADREAD MSS/TP53-wildtype stratification recovers a gate-jamming signal that was invisible in the pan-cancer analysis. Five Bonferroni-significant correlations in a 209-sample cohort — HAVCR2 (↓), TREX1 (↑), CXCL10 (↓), STING ratio (↓), cGAS (↓) — are directionally consistent with the hypothesis that VDAC1 gate-jamming suppresses innate immune activation in microsatellite-stable colorectal tumors.

The null MSI-H control and the attenuation of correlations in TP53-mutant strata define the framework's domain of applicability: GJS is predicted to be informative in genomically stable tumors where mitochondrial DNA release is the dominant cytosolic DNA source and apoptotic machinery is intact.

The TREX1 co-occurrence finding revises the evasion architecture model: gate-jamming and cytosolic DNA degradation are co-deployed in the most evasion-committed tumors, while ENPP1-mediated cGAMP degradation represents an alternative strategy.

Validation priorities:
1. Protein-level GJS measurement in COADREAD MSS tissue (PLA for HK-II–VDAC1 and Bcl-xL–VDAC1 complexes)
2. Single-cancer-type ICI response cohort analysis (IMvigor210 bladder cancer as initial target)
3. Single-cell RNA-seq to resolve cell-type-specific expression of tGJS components and immune markers
4. TREX1 co-regulation mechanism — is TREX1 upregulation driven by the same metabolic reprogramming that elevates HK2/BCL2L1?

## S2.7 Data Availability

All code, data, and figures are available at:
- Script: `analysis/tcga_gjs/compute_tgjs_coadread_mss.py`
- Results: `analysis/tcga_gjs/data/coadread_mss/`
- Figures: `analysis/tcga_gjs/figures/coadread_mss/`
- Repository: https://github.com/templetwo/vdac-pharmacology-atlas (commit af63c2b)

## S2.8 Gene Symbols and Identifiers

| Symbol | Full Name | Entrez ID | Role in Analysis |
|--------|-----------|-----------|-----------------|
| HK2 | Hexokinase 2 | 3099 | tGJS component (weight 0.40) |
| BCL2L1 | BCL2-like 1 (Bcl-xL) | 598 | tGJS component (weight 0.30) |
| TSPO | Translocator Protein | 706 | tGJS component — cholesterol proxy (weight 0.30) |
| HAVCR2 | Hepatitis A Virus Cellular Receptor 2 (TIM-3) | 84868 | T cell exhaustion marker |
| LAG3 | Lymphocyte Activating 3 | 3902 | T cell exhaustion marker |
| PDCD1 | Programmed Cell Death 1 (PD-1) | 5133 | T cell exhaustion marker |
| TIGIT | T Cell Immunoreceptor With Ig And ITIM Domains | 201633 | T cell exhaustion marker |
| MB21D1 | Mab-21 Domain Containing 1 (cGAS) | 115004 | Cytosolic DNA sensor |
| STING1 | Stimulator of Interferon Response cGAMP Interactor 1 | 340061 | cGAS-STING pathway |
| ENPP1 | Ectonucleotide Pyrophosphatase/Phosphodiesterase 1 | 5167 | cGAMP degradation ("eraser") |
| TREX1 | Three Prime Repair Exonuclease 1 | 11277 | Cytosolic DNA degradation ("eraser") |
| CD274 | CD274 Molecule (PD-L1) | 29126 | Immune checkpoint |
| CD8A | CD8A Molecule | 925 | Cytotoxic T cell marker |
| IFNG | Interferon Gamma | 3458 | Effector cytokine |
| CXCL10 | C-X-C Motif Chemokine Ligand 10 | 3627 | IFN-γ-induced chemokine |
| GZMB | Granzyme B | 3002 | Cytotoxic effector |
| PRF1 | Perforin 1 | 5551 | Cytotoxic effector |
| IFNB1 | Interferon Beta 1 | 3456 | Acute STING signature |
| CCL5 | C-C Motif Chemokine Ligand 5 | 6352 | Acute STING signature |
| IDO1 | Indoleamine 2,3-Dioxygenase 1 | 3620 | Chronic STING signature |
| TGFB1 | Transforming Growth Factor Beta 1 | 7040 | Chronic STING signature |
| IL6 | Interleukin 6 | 3569 | Chronic STING signature |
| ARG1 | Arginase 1 | 383 | Chronic STING signature |
| NOS2 | Nitric Oxide Synthase 2 | 4843 | Chronic STING signature |

## S2.9 Acknowledgments

This analysis was designed in response to experimental design feedback from Reddit user SquidwardHurrHurrHur (self-identified Master's graduate in Cancer Immunology), who identified MSI-low stratification as the critical refinement and recommended TP53 layering, exhaustion marker profiling, and hereditary syndrome exclusion. Their contribution shaped the analytical approach of this supplementary.

Multi-model AI collaboration: Analysis prompt designed in Claude Opus (Anthropic), gene panel and dataset recommendations from Gemini (Google DeepMind), literature gap analysis from Grok (xAI), computational execution by Claude Code (Anthropic). The corresponding author served as orchestrator, integrating domain-expert feedback with AI-assisted analysis.
