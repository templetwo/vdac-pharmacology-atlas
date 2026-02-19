# Supplementary Analysis S1: Transcriptomic Gate-Jamming Score — A Boundary Analysis

**Associated manuscript:** "The Gate-Jamming Score: A VDAC1-Based Composite Biomarker Linking Warburg Metabolism to Immune Evasion in Cancer"

---

## S1.1 Rationale

The Gate-Jamming Score (GJS) predicts immune-cold tumor status based on three protein-level mechanisms that suppress VDAC1 oligomerization: hexokinase-II docking, Bcl-xL binding, and cholesterol loading of the outer mitochondrial membrane. We asked whether a crude transcriptomic proxy — using mRNA expression of the genes encoding these components — could recapitulate the GJS prediction at the pan-cancer level.

This analysis was designed as a boundary test: if a 3-gene mRNA proxy worked, it would suggest the GJS captures a transcriptionally regulated program. If it failed, it would define the measurement modality required for direct validation.

## S1.2 Methods

### Gene selection

We constructed a transcriptomic GJS (tGJS) using three genes mapped to the original GJS components:

| GJS Component | Gene | Weight | Rationale |
|---|---|---|---|
| f(HK-II) | HK2 | 0.40 | Hexokinase-II, the isoform that docks on VDAC1 |
| f(Bcl-xL) | BCL2L1 | 0.30 | Encodes Bcl-xL |
| [Chol]/[CL] ratio | TSPO | 0.30 | Translocator protein; mediates cholesterol import to outer mitochondrial membrane |

TSPO was selected over STAR (steroidogenic acute regulatory protein) after an initial analysis showed STAR expression is dominated by tissue identity in steroidogenic organs (adrenocortical carcinoma ranked first), confounding any cancer-general signal.

### Extended gene panel

Beyond the three GJS proxy genes, we measured:

- **Immune markers** (5 genes): CD8A, IFNG, CXCL10, GZMB, PRF1
- **cGAS-STING pathway** (2 genes): CGAS, STING1
- **Signal erasers** (2 genes): ENPP1 (degrades cGAMP), TREX1 (degrades cytosolic DNA)
- **Immune checkpoint**: CD274 (PD-L1)
- **Acute STING signature** (3 genes): IFNB1, CXCL10, CCL5
- **Chronic STING signature** (5 genes): IDO1, TGFB1, IL6, ARG1, NOS2

### Data source

Expression data (RNA-Seq V2 RSEM) were retrieved from cBioPortal via REST API for all 32 TCGA PanCanAtlas studies (n = 10,071 samples). Each gene was min-max normalized across the full cohort before computing the weighted tGJS.

### Statistical analysis

Spearman rank correlations were computed between tGJS and all extended panel genes. Cancer type-level mean tGJS was correlated with published ICI objective response rates from clinical trials.

## S1.3 Results

### Primary prediction: NOT CONFIRMED

tGJS did not inversely correlate with checkpoint inhibitor response rates across 16 cancer types with available ICI data:

> **Spearman ρ = +0.382, p = 0.144** (n = 16 cancer types)

The correlation was positive (wrong direction) and not significant. High-tGJS cancer types included both ICI-responsive (SKCM, BLCA, LUSC) and ICI-resistant (PAAD, HNSC) tumors.

**Top 5 highest tGJS:** HNSC (0.098), COADREAD (0.089), CHOL (0.089), PAAD (0.088), LUSC (0.085)

**Top 5 lowest tGJS:** GBM (0.041), SARC (0.039), LIHC (0.036), LGG (0.026), PCPG (0.025)

### Immune marker correlations: opposite of prediction

All five immune markers correlated *positively* with tGJS:

| Immune Marker | Spearman ρ | p-value | n |
|---|---|---|---|
| GZMB | +0.308 | 10^-221 | 10,071 |
| IFNG | +0.167 | 10^-64 | 10,071 |
| PRF1 | +0.161 | 10^-59 | 10,071 |
| CXCL10 | +0.141 | 10^-45 | 10,071 |
| CD8A | +0.082 | 10^-16 | 10,071 |

**Interpretation:** HK2 and BCL2L1 are upregulated in metabolically aggressive, genomically unstable tumors that simultaneously provoke immune infiltration. At the transcriptomic level, the Warburg phenotype and immune engagement co-occur — they are not opposing forces. The GJS framework predicts immune evasion through *protein-level gating* (physical occupancy of the VDAC1 channel), not through transcriptional suppression of metabolic genes. Bulk mRNA cannot distinguish between HK2 protein in the cytosol performing glycolysis and HK2 protein physically docked on VDAC1 blocking oligomerization.

### cGAS-STING pathway: intact machinery in high-tGJS tumors

| Pathway Gene | Spearman ρ | p-value | Interpretation |
|---|---|---|---|
| STING1 | +0.222 | 10^-113 | Pathway machinery present |
| CGAS | +0.211 | 10^-101 | Sensor ready to fire |
| CD274 (PD-L1) | +0.150 | 10^-51 | Inflamed/checkpoint-active |

High-tGJS tumors express *more* cGAS and STING1, not less. The innate immune sensing pathway is transcriptionally intact. This is consistent with the GJS framework: gate-jamming suppresses the *signal* (mtDNA release through VDAC1 oligomers) rather than silencing the *machinery* that would detect it. The gun is loaded; the trigger is blocked.

### ENPP1 anti-correlation: orthogonal evasion strategies

| Eraser Gene | Spearman ρ | p-value | Interpretation |
|---|---|---|---|
| **ENPP1** | **-0.181** | **10^-75** | Less cGAMP degradation in high-tGJS tumors |
| TREX1 | +0.087 | 10^-18 | Weakly positive |

ENPP1 encodes ecto-nucleotide pyrophosphatase/phosphodiesterase 1, which degrades the cGAS product cGAMP before it can activate STING. The significant inverse correlation with tGJS (ρ = -0.181, p = 4.3 x 10^-75) suggests that tumors employing the metabolic gate-jamming phenotype (high HK2/BCL2L1/TSPO) do *not* simultaneously upregulate enzymatic cGAMP destruction.

This is consistent with two orthogonal immune evasion strategies:

1. **Gate-jamming (upstream):** Block mtDNA release by suppressing VDAC1 oligomerization — prevents the danger signal from ever reaching the cytosol.
2. **Enzymatic erasure (downstream):** Allow cGAMP production but degrade it before STING activation.

These strategies appear to be anti-correlated at the transcriptomic level. Tumors may preferentially employ one or the other, not both. This partitioning — if validated at the protein level — could have therapeutic implications: gate-jamming tumors might respond to VDAC1-targeted interventions (HK-II displacement), while ENPP1-high tumors might respond to ENPP1 inhibitors currently in clinical development.

### Acute vs. chronic STING ratio

The acute/chronic STING signature analysis was limited by gene availability in the TCGA RNA-Seq V2 dataset. Among available genes:

| Metric | Spearman ρ | p-value |
|---|---|---|
| Acute STING signature | +0.144 | 10^-47 |
| Chronic STING signature | +0.171 | 10^-66 |
| STING ratio (acute - chronic) | -0.021 | 0.036 |

The slight negative correlation of the acute-minus-chronic ratio with tGJS (barely significant at p = 0.036) hints at a shift toward chronic immunosuppressive STING signaling in high-tGJS tumors, but the effect size is negligible and this finding should not be over-interpreted.

## S1.4 Limitations

1. **mRNA ≠ protein occupancy.** The GJS describes physical protein-protein interactions (HK-II docking on VDAC1, Bcl-xL binding, cholesterol integration into lipid bilayers). Transcript abundance of these genes does not measure whether the proteins are performing their gate-jamming function. A cell can express abundant HK2 mRNA with all protein in the cytosol.

2. **Bulk transcriptomics averages over cell types.** Tumor samples contain cancer cells, fibroblasts, endothelial cells, and immune infiltrate. HK2 expression from immune cells (which upregulate glycolysis upon activation) would inflate the tGJS in inflamed tumors, producing the observed positive correlation with immune markers.

3. **Three-gene proxy is inherently crude.** The cholesterol/cardiolipin ratio — a membrane biophysical property — cannot be captured by any single gene. TSPO expression is a better proxy than STAR but still measures transport capacity, not actual membrane composition.

4. **ICI response rates are ecological estimates.** Cancer type-level response rates from published trials are population averages, not sample-level outcomes. The correlation was computed on n = 16 data points.

## S1.5 Conclusion

The transcriptomic Gate-Jamming Score does not predict checkpoint inhibitor resistance at the pan-cancer level. This establishes a critical validation boundary: the GJS hypothesis describes protein-level gating events that cannot be captured by bulk mRNA measurement.

The analysis yielded two secondary findings of interest:

1. **Intact pathway machinery:** High-tGJS tumors retain full cGAS-STING expression, consistent with upstream signal blockade rather than pathway silencing.

2. **Orthogonal evasion strategies:** The ENPP1 anti-correlation (ρ = -0.18) suggests metabolically aggressive tumors employ mitochondrial gating instead of enzymatic cGAMP degradation, partitioning into distinct evasion phenotypes.

These findings define the next experimental step: protein-level assays (proximity ligation for HK-II/VDAC1 interaction, co-immunoprecipitation for Bcl-xL/VDAC1, mitochondrial lipidomics for cholesterol/cardiolipin ratio) are required to test the GJS directly. The IMvigor210 bladder cancer cohort, which provides sample-level ICI response data with matched transcriptomics, could further refine whether tGJS has any predictive value within a single cancer type where tissue-of-origin effects are controlled.

## S1.6 Data Availability

All code, raw data, and figures for this analysis are available at:
- Script: `analysis/tcga_gjs/compute_tgjs.py`
- Data: `analysis/tcga_gjs/data/`
- Figures: `analysis/tcga_gjs/figures/`
- Repository: https://github.com/templetwo/vdac-pharmacology-atlas

## S1.7 Gene Symbols and Identifiers

| Symbol Used | Full Name | Entrez ID | cBioPortal Symbol |
|---|---|---|---|
| HK2 | Hexokinase 2 | 3099 | HK2 |
| BCL2L1 | BCL2-like 1 (Bcl-xL) | 598 | BCL2L1 |
| TSPO | Translocator protein | 706 | TSPO |
| CGAS | Cyclic GMP-AMP synthase | 115004 | CGAS |
| STING1 | Stimulator of interferon response cGAMP interactor 1 | 340061 | STING1 |
| ENPP1 | Ectonucleotide pyrophosphatase/phosphodiesterase 1 | 5167 | ENPP1 |
| TREX1 | Three prime repair exonuclease 1 | 11277 | TREX1 |
| CD274 | Programmed death-ligand 1 (PD-L1) | 29126 | CD274 |
