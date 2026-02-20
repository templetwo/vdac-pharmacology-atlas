# VDAC1 Gate-Jamming and Innate Immune Evasion in MSS Colorectal Cancer

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Status: Submitted to bioRxiv](https://img.shields.io/badge/Status-Submitted%20to%20bioRxiv-b31b1b.svg)]()
[![Archive: OSF](https://img.shields.io/badge/Archive-OSF-orange.svg)](https://osf.io/c9rqb/)
[![Dataset: HuggingFace](https://img.shields.io/badge/Dataset-HuggingFace-yellow.svg)](https://huggingface.co/datasets/TheTempleofTwo/vdac-pharmacology-atlas)

**Anthony J. Vasquez Sr.** — Delaware Valley University, Doylestown, PA, USA

**Corresponding author**: vasquezaj3921@delval.edu

---

## The Paper

**Context-Specific Innate Immune Evasion via VDAC1 Gate-Jamming in Microsatellite-Stable Colorectal Cancer: A Three-Cohort Transcriptomic Analysis**

> *Submitted to bioRxiv — February 2026. DOI pending.*

85-95% of colorectal cancer patients carry microsatellite-stable (MSS) tumors and derive no benefit from immune checkpoint inhibitors. This paper proposes that VDAC1 gate-jamming — suppression of VDAC1 oligomerization by HK-II, Bcl-xL, and mitochondrial cholesterol — silences the cGAS-STING innate immune signal that checkpoint inhibitors require to function, and tests this hypothesis across three cohorts.

**Manuscript:** [`paper/gjs_manuscript.docx`](paper/gjs_manuscript.docx) | [`paper/gjs_manuscript.md`](paper/gjs_manuscript.md)

---

## The Three-Cohort Arc

| Analysis | Cohort | n | Result |
|----------|--------|---|--------|
| **S1** | TCGA pan-cancer | 10,071 | Null — cross-cancer confounds mask signal |
| **S2** | COADREAD MSS/TP53-wt | 209 | **5 Bonferroni-significant immune correlations** |
| **S3** | IMvigor210 atezolizumab | 348 | Null — wrong tumor type, wrong treatment mechanism |

The two nulls define the framework's boundary. The signal appears precisely where the biology predicts it should — and not where it shouldn't.

### S2 Key Findings (MSS/TP53-wildtype clean room)

| Marker | Spearman rho | p_bonf | Direction |
|--------|-------------|--------|-----------|
| HAVCR2 (TIM-3) | -0.349 | 5 x 10^-6 | Down — T cell absence, not exhaustion |
| TREX1 | +0.315 | 7 x 10^-5 | Up — belt-and-suspenders DNA erasure |
| CXCL10 | -0.231 | 0.015 | Down — suppressed IFN-gamma signaling |
| STING ratio | -0.216 | 0.034 | Down — shift to immunosuppressive profile |
| cGAS | -0.208 | 0.049 | Down |

---

## The Hypothesis

```
tGJS = 0.40 x norm(HK2) + 0.30 x norm(BCL2L1) + 0.30 x norm(TSPO)
```

A three-gene transcriptomic proxy for the physical Gate-Jamming Score:

```
GJS = f_HKII x 0.40 + f_BclxL x 0.30 + [Chol]/[CL]_norm x 0.30
```

Where f_HKII and f_BclxL are the fractions of VDAC1 occupied by hexokinase-II and Bcl-xL respectively (measurable by proximity ligation assay), and [Chol]/[CL] is the outer mitochondrial membrane cholesterol-to-cardiolipin ratio (measurable by lipidomics).

### The Therapeutic Stack

Three independent AI analytical systems (Claude Opus, Gemini Pro, Grok) converged on the same three-layer intervention from the same data without cross-exposure:

1. **VDAC1 gate-opener** — displace HK-II (methyl jasmonate, clotrimazole) to restore mtDNA release and cGAS-STING activation
2. **DNA/cGAMP eraser inhibitor** — block TREX1 or ENPP1 to sustain the innate signal
3. **Checkpoint blockade** — amplify the adaptive response now that T cells are being recruited

---

## Repository Structure

```
vdac-pharmacology-atlas/
├── paper/
│   ├── gjs_manuscript.md                        # Manuscript source
│   ├── gjs_manuscript.docx                      # Submission file
│   ├── build_manuscript_docx.py                 # Reproducible build script
│   ├── supplementary_S1_tcga_boundary_analysis.md
│   ├── supplementary_S2_coadread_mss_stratification.md
│   ├── supplementary_S3_imvigor210.md
│   ├── supplementary-S1-tcga-boundary-analysis.docx
│   ├── supplementary-S2-coadread-mss.docx
│   ├── supplementary-S3-imvigor210.docx
│   └── vpa_cbd_hepatotoxicity_alert.md          # Pharmacovigilance alert
├── analysis/
│   ├── tcga_gjs/
│   │   ├── compute_tgjs.py                      # S1: pan-cancer pipeline
│   │   ├── compute_tgjs_coadread_mss.py         # S2: COADREAD MSS stratified
│   │   ├── data/
│   │   │   └── coadread_mss/                    # S2 results + strata summary
│   │   └── figures/
│   │       ├── fig1-4 (S1 pan-cancer figures)
│   │       └── coadread_mss/ (figS2a-e)
│   └── imvigor210/
│       ├── compute_tgjs_imvigor210.R            # S3: IMvigor210 analysis
│       ├── data/                                 # S3 results matrix + summary
│       └── figures/ (figS3a-d)
├── runs/                                         # IRIS Gate Evo convergence runs
├── gold/                                         # Gold extractions from runs
├── data/
│   ├── vdac_modulators.csv                      # 17 VDAC-interacting compounds
│   └── vdac_isoform_comparison.csv
└── figures/                                      # Atlas overview figures
```

---

## Supplementary Analyses

| File | Contents |
|------|----------|
| [S1](paper/supplementary_S1_tcga_boundary_analysis.md) | Pan-cancer tGJS across 10,071 TCGA samples; boundary analysis; ENPP1 anti-correlation |
| [S2](paper/supplementary_S2_coadread_mss_stratification.md) | COADREAD 4-stratum analysis; 20 markers x 4 strata; TREX1 co-occurrence finding; ENPP1 artifact correction |
| [S3](paper/supplementary_S3_imvigor210.md) | IMvigor210 null result; TMB interaction; immune phenotype stratification; OS analysis |

---

## Pharmacovigilance Alert

**[paper/vpa_cbd_hepatotoxicity_alert.md](paper/vpa_cbd_hepatotoxicity_alert.md)**

> Up to 30% of co-prescribed VPA + CBD patients develop ALT elevations >3x ULN. The standard CYP450 explanation is incomplete. VPA depletes mitochondrial reserves; CBD alters VDAC1 conductance. An estimated 2,000-3,500 US pediatric patients currently affected. Three testable steps to close the mechanistic gap.

---

## Key Commits

| Commit | Description |
|--------|-------------|
| `88ff1f7` | S1 pan-cancer tGJS pipeline — 10,071 samples, null result |
| `af63c2b` | S2 COADREAD MSS stratified analysis — 5 Bonferroni hits |
| `af514d1` | S2 writeup with synthesis sentence |
| `edb4880` | S3 IMvigor210 analysis — second null |
| `61048d4` | S3 writeup |
| `779f399` | Manuscript restructured around S1-S2-S3 arc |
| `aeb2e44` | Submission-ready docx with proper table formatting |

---

## Related Projects

| Project | Link | Relationship |
|---------|------|-------------|
| IRIS Gate Evo | [templetwo/iris-gate-evo](https://github.com/templetwo/iris-gate-evo) | Multi-model convergence engine |
| CBD Two-Pathway Model | [templetwo/cbd-two-pathway-model](https://github.com/templetwo/cbd-two-pathway-model) | Origin of the gate-jamming question |
| IRIS Evo Findings | [templetwo/iris-evo-findings](https://github.com/templetwo/iris-evo-findings) | Run corpus and cross-run analysis |
| HuggingFace Dataset | [TheTempleofTwo/vdac-pharmacology-atlas](https://huggingface.co/datasets/TheTempleofTwo/vdac-pharmacology-atlas) | Full convergence corpus |
| OSF Archive | [osf.io/c9rqb](https://osf.io/c9rqb/) | Preregistration and data archive |

---

## Citation

```bibtex
@article{vasquez2026gatejamming,
  title={Context-Specific Innate Immune Evasion via VDAC1 Gate-Jamming
         in Microsatellite-Stable Colorectal Cancer:
         A Three-Cohort Transcriptomic Analysis},
  author={Vasquez, Anthony J., Sr.},
  year={2026},
  journal={bioRxiv},
  note={Submitted February 2026. DOI pending.},
  url={https://github.com/templetwo/vdac-pharmacology-atlas}
}
```

---

## License

CC BY 4.0. Use it, build on it, cite it.
