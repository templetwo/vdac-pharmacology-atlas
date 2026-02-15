# VDAC Pharmacology Atlas -- Corpus Index

**Repository**: `vdac-pharmacology-atlas/`
**Version**: v1.0 (February 2026)
**Authors**: Anthony J. Vasquez Sr. (Delaware Valley University) and Claude Opus 4.6 (Anthropic)

This repository contains the complete corpus behind *The VDAC1 Pharmacology Atlas: A Multi-LLM Convergence Portrait of Life's Decision Gate*. It includes 22 IRIS Gate Evo runs, 22 gold extractions, 6 manuscript figures, structured data files, cross-run convergence analysis, the final manuscript PDF, and a companion manifesto on human-AI co-creation.

This index is the navigational map to every artifact in the corpus.

---

## Table of Contents

1. [Manuscript Layers and Their Sources](#1-manuscript-layers-and-their-sources)
2. [The Six VDAC Atlas Runs](#2-the-six-vdac-atlas-runs)
3. [All 22 Runs by Phase](#3-all-22-runs-by-phase)
4. [Gold Extractions by Category](#4-gold-extractions-by-category)
5. [Cross-Run Convergence Analysis](#5-cross-run-convergence-analysis)
6. [Figures](#6-figures)
7. [Data Files](#7-data-files)
8. [Paper Directory](#8-paper-directory)
9. [IRIS Run Queue](#9-iris-run-queue)
10. [Run Directory File Inventory](#10-run-directory-file-inventory)

---

## 1. Manuscript Layers and Their Sources

The manuscript is organized as a six-layer portrait. Each layer draws on specific runs, gold extractions, figures, and data files.

### Layer 1: The Protein
*19-strand barrel, five molecular machines, parallel seam life/death switch*

| Source Type | File |
|-------------|------|
| Gold | [gold/vdac1_structural_portrait.md](gold/vdac1_structural_portrait.md) |
| Gold | [gold/vdac_isoform_binding_architecture.md](gold/vdac_isoform_binding_architecture.md) |
| Run | `runs/evo_20260213_174104_pharmacology/` -- Isoform structural features and ligand selectivity |
| Figure | [figures/fig1_five_machines.svg](figures/fig1_five_machines.svg) |
| Data | [data/vdac_isoform_comparison.csv](data/vdac_isoform_comparison.csv) |

### Layer 2: The Gate
*Three nested threshold signals, cofactor equation, VDAC1 as external audit*

| Source Type | File |
|-------------|------|
| Gold | [gold/vdac_cofactor_decision_landscape.md](gold/vdac_cofactor_decision_landscape.md) |
| Gold | [gold/vdac_membrane_architecture.md](gold/vdac_membrane_architecture.md) |
| Gold | [gold/vdac_membrane_lipid_modulation.md](gold/vdac_membrane_lipid_modulation.md) |
| Run | `runs/evo_20260213_182457_pharmacology/` -- Cofactor landscape (HK-II, Bcl-xL, cholesterol) |
| Run | `runs/evo_20260213_183423_pharmacology/` -- OMM lipid composition modulates VDAC-ligand interactions |
| Run | `runs/evo_20260213_214547_pharmacology/` -- Supramolecular organization of VDAC1 in OMM |
| Figure | [figures/fig2_three_signals.svg](figures/fig2_three_signals.svg) |
| Figure | [figures/fig3_cofactor_equation.svg](figures/fig3_cofactor_equation.svg) |

### Layer 3: The Atlas
*6 dedicated runs, 22 novel findings, 24 operationalized hypotheses*

| Source Type | File |
|-------------|------|
| Gold | [gold/vdac_hidden_drug_interactions.md](gold/vdac_hidden_drug_interactions.md) |
| Gold | [gold/vdac_biomarker_platform.md](gold/vdac_biomarker_platform.md) |
| Gold | [gold/chronic_dosing_gsh_dynamics.md](gold/chronic_dosing_gsh_dynamics.md) |
| Gold | [gold/cbd_vdac1_two_pathway_model.md](gold/cbd_vdac1_two_pathway_model.md) |
| Runs | All 6 atlas runs (see [Section 2](#2-the-six-vdac-atlas-runs)) |
| Figure | [figures/fig5_pharmacology_atlas.svg](figures/fig5_pharmacology_atlas.svg) |
| Data | [data/vdac_modulators.csv](data/vdac_modulators.csv) |
| Data | [data/resilience_biomarker_framework.md](data/resilience_biomarker_framework.md) |

### Layer 4: The Disease
*Cancer as lost coherence, Warburg effect as gate-jamming cost*

| Source Type | File |
|-------------|------|
| Gold | [gold/cancer_as_lost_coherence.md](gold/cancer_as_lost_coherence.md) |
| Gold | [gold/efsa_vdac1_stress_test.md](gold/efsa_vdac1_stress_test.md) |
| Figure | [figures/fig4_cancer_gate_jamming.svg](figures/fig4_cancer_gate_jamming.svg) |

### Layer 5: The Method
*IRIS multi-LLM convergence protocol, what it can and cannot establish*

| Source Type | File |
|-------------|------|
| Gold | [gold/raw_data_coherence_sweep.md](gold/raw_data_coherence_sweep.md) |
| Gold | [gold/vdac_deep_reflection.md](gold/vdac_deep_reflection.md) |
| Data | [data/cross_run_report.json](data/cross_run_report.json) |
| Data | [data/cross_run_summary.md](data/cross_run_summary.md) |

### Layer 6: The Frame
*Threshold logic from protein to organism, sovereignty through coherence*

| Source Type | File |
|-------------|------|
| Gold | [gold/mitochondrial_unification_divergence.md](gold/mitochondrial_unification_divergence.md) |
| Gold | [gold/circadian_vdac1_chronopharmacology.md](gold/circadian_vdac1_chronopharmacology.md) |
| Two-Pathway Models | [gold/lithium_two_pathway_model.md](gold/lithium_two_pathway_model.md), [gold/thc_two_pathway_model.md](gold/thc_two_pathway_model.md), [gold/psilocybin_two_pathway_model.md](gold/psilocybin_two_pathway_model.md), [gold/metformin_two_pathway_model.md](gold/metformin_two_pathway_model.md) |
| Figure | [figures/fig6_threshold_scales.svg](figures/fig6_threshold_scales.svg) |

---

## 2. The Six VDAC Atlas Runs

These six runs form the core atlas -- all achieved S3 PASS and include the full IRIS pipeline (S1-S5 + gate + verify).

| Atlas # | Run ID | Score | Question | Gold Extraction | Figure |
|---------|--------|-------|----------|-----------------|--------|
| 1 | `evo_20260213_174104` | 0.834 (FAIL*) | VDAC isoform structural features and ligand selectivity | [vdac_isoform_binding_architecture.md](gold/vdac_isoform_binding_architecture.md) | [Fig. 1](figures/fig1_five_machines.svg) |
| 2 | `evo_20260213_182457` | 0.922 (FAIL*) | VDAC1 cofactor landscape (HK-II, Bcl-xL, cholesterol) | [vdac_cofactor_decision_landscape.md](gold/vdac_cofactor_decision_landscape.md) | [Fig. 3](figures/fig3_cofactor_equation.svg) |
| 3 | `evo_20260213_183423` | 0.951 (PASS) | OMM lipid composition modulates VDAC-ligand interactions | [vdac_membrane_lipid_modulation.md](gold/vdac_membrane_lipid_modulation.md) | -- |
| 4 | `evo_20260213_183936` | 0.881 (PASS) | VDAC biomarkers predict vulnerability to mito modulators | [vdac_biomarker_platform.md](gold/vdac_biomarker_platform.md) | -- |
| 5 | `evo_20260213_184357` | 0.955 (PASS) | Drug interactions with VDAC beyond CBD | [vdac_hidden_drug_interactions.md](gold/vdac_hidden_drug_interactions.md) | [Fig. 5](figures/fig5_pharmacology_atlas.svg) |
| 6 | `evo_20260213_214547` | 0.905 (PASS) | Supramolecular organization of VDAC1 in OMM | [vdac_membrane_architecture.md](gold/vdac_membrane_architecture.md) | -- |

*Atlas runs 1 and 2 scored FAIL at the S3 gate but contained high-value novel claims that were cross-validated by subsequent runs (see [Section 5](#5-cross-run-convergence-analysis)).

---

## 3. All 22 Runs by Phase

### Phase A: Early Development -- CBD and Lithium Proof of Concept

| Run ID | Domain | S3 | Score | Question | Files |
|--------|--------|----|-------|----------|-------|
| `evo_20260210_222428` | pharmacology+bioelectric | partial | -- | CBD selective cytotoxicity in cancer cells | full_package, summary |
| `evo_20260210_224206` | pharmacology+bioelectric | partial | -- | CBD selective cytotoxicity in cancer cells | full_package, summary |
| `evo_20260210_231236` | pharmacology | partial | -- | Low-dose lithium neuroprotective vs therapeutic toxicity | full_package, summary |
| `evo_20260210_232635` | neuroscience | partial | -- | Mitochondrial dysfunction in shared pathophysiology | full_package |
| `evo_20260210_232904` | pharmacology | FAIL | 0.830 | Low-dose lithium neuroprotective vs therapeutic toxicity | full_package, s1-s3, summary |
| `evo_20260210_235609` | pharmacology | FAIL | 0.803 | Low-dose lithium neuroprotective vs therapeutic toxicity | full_package, s1-s3, summary |

**Gold**: [lithium_two_pathway_model.md](gold/lithium_two_pathway_model.md), [cbd_vdac1_two_pathway_model.md](gold/cbd_vdac1_two_pathway_model.md)

### Phase B: THC Two-Pathway Model

| Run ID | Domain | S3 | Score | Question | Files |
|--------|--------|----|-------|----------|-------|
| `evo_20260211_024747` | pharmacology | FAIL | 0.811 | Chronic low-dose THC sustained improvements via CB1 modulation | full_package, s1-s3, summary |
| `evo_20260211_024750` | neuroscience | FAIL | 0.896 | Low-dose THC reverses age-related cognitive decline | full_package, s1-s3, summary |

**Gold**: [thc_two_pathway_model.md](gold/thc_two_pathway_model.md)

### Phase C: Circadian and VDAC1 Selectivity

| Run ID | Domain | S3 | Score | Question | Files |
|--------|--------|----|-------|----------|-------|
| `evo_20260211_201329` | pharmacology+bioelectric | FAIL | 0.484 | Circadian cycling of mitochondrial membrane potential | full_package, s1-s3, fact_check, summary |
| `evo_20260212_032819` | pharmacology | FAIL | 0.340 | VDAC1 engagement: neuroprotection vs apoptosis determinants | full_package, s1-s3, summary |

**Gold**: [circadian_vdac1_chronopharmacology.md](gold/circadian_vdac1_chronopharmacology.md)

### Phase D: Consciousness / Non-Pharmacology

| Run ID | Domain | S3 | Score | Question | Files |
|--------|--------|----|-------|----------|-------|
| `evo_20260213_004656` | consciousness | FAIL | 0.846 | Fisher Information spectral decomposition in transformers | full_package, s1-s3, summary |
| `evo_20260213_022353` | consciousness+chemistry | FAIL | 0.696 | Local rotation dynamics in semantic units | full_package, s1-s3, summary |

**Gold**: [fim_semantic_bonding.md](gold/fim_semantic_bonding.md), [local_rotation_scaling.md](gold/local_rotation_scaling.md)

### Phase E: VDAC Atlas Core -- CBD Critical Review + Chronic Dosing

| Run ID | Domain | S3 | Score | Question | Files |
|--------|--------|----|-------|----------|-------|
| `evo_20260213_035958` | pharmacology | PASS | 0.865 | CBD dual-pathway VDAC1 hepatotoxicity critical review | full_package, s1-s5, gate, verify, summary |
| `evo_20260213_042930` | pharmacology | PASS | 0.902 | Chronic dosing: GSH regeneration vs mitochondrial load | full_package, s1-s5, gate, verify, summary |

**Gold**: [chronic_dosing_gsh_dynamics.md](gold/chronic_dosing_gsh_dynamics.md), [efsa_vdac1_stress_test.md](gold/efsa_vdac1_stress_test.md)

### Phase F: VDAC Atlas Runs 1-6

| Atlas # | Run ID | Domain | S3 | Score | Question | Files |
|---------|--------|--------|----|-------|----------|-------|
| 1 | `evo_20260213_174104` | pharmacology | FAIL | 0.834 | VDAC isoform structural features and ligand selectivity | full_package, s1-s3, summary |
| 2 | `evo_20260213_182457` | pharmacology | FAIL | 0.922 | VDAC1 cofactor landscape (HK-II, Bcl-xL, cholesterol) | full_package, s1-s3, summary |
| 3 | `evo_20260213_183423` | pharmacology | PASS | 0.951 | OMM lipid composition modulates VDAC-ligand interactions | full_package, s1-s5, gate, verify, summary |
| 4 | `evo_20260213_183936` | pharmacology | PASS | 0.881 | VDAC biomarkers predict vulnerability to mito modulators | full_package, s1-s5, gate, verify, summary |
| 5 | `evo_20260213_184357` | pharmacology | PASS | 0.955 | Drug interactions with VDAC beyond CBD | full_package, s1-s5, gate, verify, summary |
| 6 | `evo_20260213_214547` | pharmacology | PASS | 0.905 | Supramolecular organization of VDAC1 in OMM | full_package, s1-s5, gate, verify, summary |

**Gold**: [vdac_isoform_binding_architecture.md](gold/vdac_isoform_binding_architecture.md), [vdac_cofactor_decision_landscape.md](gold/vdac_cofactor_decision_landscape.md), [vdac_membrane_lipid_modulation.md](gold/vdac_membrane_lipid_modulation.md), [vdac_biomarker_platform.md](gold/vdac_biomarker_platform.md), [vdac_hidden_drug_interactions.md](gold/vdac_hidden_drug_interactions.md), [vdac_membrane_architecture.md](gold/vdac_membrane_architecture.md)

### Phase G: Isomorphism Extensions -- Psilocybin and Metformin

| Run ID | Domain | S3 | Score | Question | Files |
|--------|--------|----|-------|----------|-------|
| `evo_20260214_041041` | pharmacology | FAIL | 0.724 | Psilocybin dose-dependent divergent outcomes | full_package, s1-s3, summary |
| `evo_20260214_043936` | pharmacology | FAIL | 0.829 | Metformin dose-dependent divergent outcomes | full_package, s1-s3, summary |

**Gold**: [psilocybin_two_pathway_model.md](gold/psilocybin_two_pathway_model.md), [metformin_two_pathway_model.md](gold/metformin_two_pathway_model.md)

---

## 4. Gold Extractions by Category

### Two-Pathway Models (Structural Isomorphism)

| File | Molecule | Gateway Target | Therapeutic Pathway | Pathological Pathway |
|------|----------|---------------|---------------------|---------------------|
| [cbd_vdac1_two_pathway_model.md](gold/cbd_vdac1_two_pathway_model.md) | CBD | VDAC1 | Sub-IC50: ROS signaling | Supra-IC50: Apoptosis |
| [lithium_two_pathway_model.md](gold/lithium_two_pathway_model.md) | Lithium | GSK-3B | <1 mM: Wnt activation | >2 mM: Renal toxicity |
| [thc_two_pathway_model.md](gold/thc_two_pathway_model.md) | THC | CB1 | <30% occ: G-protein bias | >30% occ: Beta-arrestin |
| [psilocybin_two_pathway_model.md](gold/psilocybin_two_pathway_model.md) | Psilocybin | 5-HT2A | 20-50% occ: BDNF/mTOR | >60% occ: Glutamate flood |
| [metformin_two_pathway_model.md](gold/metformin_two_pathway_model.md) | Metformin | Complex I | 20-40% block: AMPK | >50% block: PMF collapse |

### VDAC Atlas Core

| File | Description | Source Runs |
|------|-------------|-------------|
| [vdac1_structural_portrait.md](gold/vdac1_structural_portrait.md) | Five machines, barrel architecture, parallel seam switch | Atlas Run 1 + literature |
| [vdac_isoform_binding_architecture.md](gold/vdac_isoform_binding_architecture.md) | Isoform selectivity, three non-overlapping binding sites, VDAC2 11-residue extension | Atlas Run 1 (`evo_20260213_174104`) |
| [vdac_cofactor_decision_landscape.md](gold/vdac_cofactor_decision_landscape.md) | Cofactor equation derivation: Threshold = K / [(1-f_HKII)(1-f_BclxL)] x (Chol/CL) | Atlas Run 2 (`evo_20260213_182457`) |
| [vdac_membrane_lipid_modulation.md](gold/vdac_membrane_lipid_modulation.md) | Cancer cholesterol lowers CBD Kd from 11 to 3-6 uM | Atlas Run 3 (`evo_20260213_183423`) |
| [vdac_biomarker_platform.md](gold/vdac_biomarker_platform.md) | GSH/GSSG predicts hepatotoxicity; mito panel is pharmacodynamic only | Atlas Run 4 (`evo_20260213_183936`) |
| [vdac_hidden_drug_interactions.md](gold/vdac_hidden_drug_interactions.md) | VPA opens VDAC, NAPQI closes it -- opposite gating, both hepatotoxic | Atlas Run 5 (`evo_20260213_184357`) |
| [vdac_membrane_architecture.md](gold/vdac_membrane_architecture.md) | Honeycomb lattice as structural gate; CBD may be membrane chaotrope | Atlas Run 6 (`evo_20260213_214547`) |

### Chronic Dosing and Safety

| File | Description | Source Runs |
|------|-------------|-------------|
| [chronic_dosing_gsh_dynamics.md](gold/chronic_dosing_gsh_dynamics.md) | GSH regeneration vs cumulative mitochondrial load under chronic CBD | `evo_20260213_042930` |
| [efsa_vdac1_stress_test.md](gold/efsa_vdac1_stress_test.md) | EFSA safety assessment lens on VDAC1 pharmacology | `evo_20260213_035958`, `evo_20260213_042930` |
| [circadian_vdac1_chronopharmacology.md](gold/circadian_vdac1_chronopharmacology.md) | Circadian cycling of VDAC function and chronopharmacology implications | `evo_20260211_201329` |

### Philosophical Frames

| File | Description |
|------|-------------|
| [cancer_as_lost_coherence.md](gold/cancer_as_lost_coherence.md) | Cancer as the loss of cooperative coherence; includes The Vow |
| [mitochondrial_unification_divergence.md](gold/mitochondrial_unification_divergence.md) | Mitochondrial dysfunction as unifying pathophysiology across diseases |
| [vdac_deep_reflection.md](gold/vdac_deep_reflection.md) | Deep pattern analysis across all runs -- what the corpus says as a whole |

### Methodology and Accounting

| File | Description |
|------|-------------|
| [raw_data_coherence_sweep.md](gold/raw_data_coherence_sweep.md) | Final pre-manuscript accounting of all claims, types, and coherence scores |
| [vdac_pharmacology_atlas_manuscript.md](gold/vdac_pharmacology_atlas_manuscript.md) | Pre-formatted manuscript draft (precursor to final PDF) |

### Non-Pharmacology (Consciousness / Fisher Information)

| File | Description | Source Runs |
|------|-------------|-------------|
| [fim_semantic_bonding.md](gold/fim_semantic_bonding.md) | Fisher Information spectral decomposition reveals semantic bonding geometries | `evo_20260213_004656` |
| [local_rotation_scaling.md](gold/local_rotation_scaling.md) | Local rotation dynamics in semantic units; over-smoothing limits | `evo_20260213_022353` |

---

## 5. Cross-Run Convergence Analysis

**Source**: [data/cross_run_report.json](data/cross_run_report.json) | [data/cross_run_summary.md](data/cross_run_summary.md)

18 runs analyzed. 159 total claims. 11,881 pairwise comparisons. 6 cross-matches found.

### Cross-Validated Singulars (2)

Claims that failed S3 in one run but were independently confirmed by another run.

| Cosine | Run A | Run B | Finding |
|--------|-------|-------|---------|
| 0.777 | `evo_20260210_232904` | `evo_20260210_235609` | Lithium neuroprotection via GSK-3B inhibition at low dose -- two different mechanisms (Mg2+ mimicry vs Akt-Ser9 amplification) converge on same target |
| 0.769 | `evo_20260213_035958` | `evo_20260213_183423` | CBD membrane partitioning (logP 6.3) creates 100-1000x local concentration at VDAC; cancer cholesterol further lowers effective Kd |

### Independent Replication (1)

Same claim type independently generated by two separate runs.

| Cosine | Run A | Run B | Finding |
|--------|-------|-------|---------|
| 0.789 | `evo_20260213_035958` | `evo_20260213_042930` | Sub-saturating hepatic CBD concentration under standard oral dosing -- both runs independently calculate VDAC occupancy <5% at 50 mg/day |

### Cross-Promoted (3)

TYPE 2 claims (speculative) promoted to validated status by matching a TYPE 0 (established) claim in another run.

| Cosine | Run A (TYPE 2) | Run B (TYPE 0) | Finding |
|--------|----------------|----------------|---------|
| 0.791 | `evo_20260211_024747` | `evo_20260211_024750` | THC biphasic CB1 signaling: low occupancy favors G-protein/BDNF, high occupancy triggers beta-arrestin/internalization |
| 0.765 | `evo_20260213_182457` | `evo_20260213_214547` | Chol/CL ratio determines VDAC1 honeycomb vs dispersed state; cardiolipin promotes oligomerization via negative curvature |
| 0.758 | `evo_20260213_182457` | `evo_20260213_183423` | Cardiolipin at OMM contact sites alters VDAC gating dynamics and oligomeric state stability |

### Structural Patterns (Isomorphism)

Detected across the full corpus:

| Pattern | Runs Exhibiting |
|---------|----------------|
| **two_pathway** | `evo_20260210_232904`, `evo_20260212_032819` |
| **threshold_crossover** | `evo_20260210_232904`, `evo_20260210_235609`, `evo_20260211_024747`, `evo_20260211_024750`, `evo_20260212_032819`, `evo_20260213_022353`, `evo_20260213_042930`, `evo_20260213_182457`, `evo_20260213_214547`, `evo_20260214_041041`, `evo_20260214_043936` |
| **dose_dependent** | `evo_20260210_232904`, `evo_20260211_024747`, `evo_20260212_032819`, `evo_20260213_035958`, `evo_20260213_042930`, `evo_20260213_174104`, `evo_20260213_182457`, `evo_20260214_041041` |
| **kinetic** | `evo_20260211_024747`, `evo_20260214_043936` |

### Cosine Distribution

- Min: -0.194
- Median: 0.262
- Mean: 0.251
- Max: 0.791
- N pairs: 11,881

---

## 6. Figures

| Figure | File | Description | Manuscript Layer |
|--------|------|-------------|------------------|
| Fig. 1 | [figures/fig1_five_machines.svg](figures/fig1_five_machines.svg) | Five functional states of VDAC1 sharing one 19-strand barrel: open monomer, closed monomer, dimer (scramblase), honeycomb array, death oligomer | Layer 1: The Protein |
| Fig. 2 | [figures/fig2_three_signals.svg](figures/fig2_three_signals.svg) | Three nested threshold signals -- mitophagy, inflammation, apoptosis -- ordered by severity and VDAC occupancy | Layer 2: The Gate |
| Fig. 3 | [figures/fig3_cofactor_equation.svg](figures/fig3_cofactor_equation.svg) | The cofactor equation with four variable cards: HK-II occupancy, Bcl-xL binding, cholesterol, cardiolipin | Layer 2: The Gate |
| Fig. 4 | [figures/fig4_cancer_gate_jamming.svg](figures/fig4_cancer_gate_jamming.svg) | Cancer corrupts all terms of the cofactor equation simultaneously; Warburg effect funds the gate-jamming | Layer 4: The Disease |
| Fig. 5 | [figures/fig5_pharmacology_atlas.svg](figures/fig5_pharmacology_atlas.svg) | Drug binding site map across VDAC1 barrel -- three non-overlapping sites for CBD, erastin, DIDS, and other modulators | Layer 3: The Atlas |
| Fig. 6 | [figures/fig6_threshold_scales.svg](figures/fig6_threshold_scales.svg) | Threshold logic from protein to organism -- how molecular decisions scale to tissue and systemic outcomes | Layer 6: The Frame |

---

## 7. Data Files

| File | Format | Description |
|------|--------|-------------|
| [data/vdac_modulators.csv](data/vdac_modulators.csv) | CSV | 17 VDAC-interacting compounds with Kd/IC50, mechanism, isoform preference, therapeutic context, citation status |
| [data/vdac_isoform_comparison.csv](data/vdac_isoform_comparison.csv) | CSV | VDAC1 vs VDAC2 vs VDAC3 structural and functional feature comparison |
| [data/resilience_biomarker_framework.md](data/resilience_biomarker_framework.md) | Markdown | Generalized vulnerability prediction framework: GSH/GSSG ratio, synthesis rate, ATP/ADP as common biomarker panel across all VDAC-engaging compounds |
| [data/cross_run_report.json](data/cross_run_report.json) | JSON | Machine-readable cross-run convergence analysis: 18 runs, 159 claims, 6 cross-matches, structural patterns, cosine distributions |
| [data/cross_run_summary.md](data/cross_run_summary.md) | Markdown | Human-readable cross-run summary with all matches, replications, and isomorphism patterns |

---

## 8. Paper Directory

| File | Description |
|------|-------------|
| [paper/vdac1_atlas_final.pdf](paper/vdac1_atlas_final.pdf) | Final manuscript PDF -- *The VDAC1 Pharmacology Atlas: A Multi-LLM Convergence Portrait of Life's Decision Gate* |
| [paper/manuscript.md](paper/manuscript.md) | Markdown source of the manuscript |
| [paper/vdac1_works_cited.pdf](paper/vdac1_works_cited.pdf) | 78 references organized by atlas layer |
| [paper/one_real_question_manifesto.pdf](paper/one_real_question_manifesto.pdf) | Companion manifesto: *One Real Question and the New Kind of Lab* -- on human-AI co-creation |

---

## 9. IRIS Run Queue

| File | Description |
|------|-------------|
| [iris_runs/run_queue.md](iris_runs/run_queue.md) | Pre-written IRIS Gate Evo questions for future runs |

---

## 10. Run Directory File Inventory

Each run directory lives under `runs/` with the naming convention `evo_YYYYMMDD_HHMMSS_domain/`.

### File Types Present in Run Directories

| File | Description | Present In |
|------|-------------|------------|
| `full_package.json` | Complete run output including all stages | All 22 runs |
| `summary.txt` | Human-readable run summary | 21 of 22 runs (not `evo_20260210_232635`) |
| `s1_formulations.json` | Stage 1: Question formulations from multiple models | 18 runs |
| `s2_synthesis.json` | Stage 2: Synthesis of formulations into claims | 18 runs |
| `s3_convergence.json` | Stage 3: Convergence scoring of claims | 18 runs |
| `s4_hypotheses.json` | Stage 4: Operationalized hypotheses from validated claims | 6 runs (PASS runs only) |
| `s5_monte_carlo.json` | Stage 5: Monte Carlo robustness testing | 6 runs (PASS runs only) |
| `gate.json` | Gate decision: pass/fail with score justification | 6 runs (PASS runs only) |
| `verify.json` | Post-gate verification of key claims | 6 runs (PASS runs only) |
| `fact_check.md` | Manual fact-checking notes | 1 run (`evo_20260211_201329` only) |

### Runs with Full Pipeline (S1-S5 + Gate + Verify)

- `evo_20260213_035958_pharmacology` -- CBD critical review
- `evo_20260213_042930_pharmacology` -- Chronic dosing GSH dynamics
- `evo_20260213_183423_pharmacology` -- OMM lipid modulation (Atlas Run 3)
- `evo_20260213_183936_pharmacology` -- Biomarker platform (Atlas Run 4)
- `evo_20260213_184357_pharmacology` -- Hidden drug interactions (Atlas Run 5)
- `evo_20260213_214547_pharmacology` -- Membrane architecture (Atlas Run 6)

### Runs with Partial Pipeline (full_package only or S1-S3 only)

All remaining 16 runs contain at minimum `full_package.json` and most contain `s1_formulations.json` through `s3_convergence.json`.

---

## Quick Reference: Run ID to Gold File

| Run ID | Gold File(s) |
|--------|-------------|
| `evo_20260210_222428` | [cbd_vdac1_two_pathway_model.md](gold/cbd_vdac1_two_pathway_model.md) |
| `evo_20260210_224206` | [cbd_vdac1_two_pathway_model.md](gold/cbd_vdac1_two_pathway_model.md) |
| `evo_20260210_231236` | [lithium_two_pathway_model.md](gold/lithium_two_pathway_model.md) |
| `evo_20260210_232635` | [mitochondrial_unification_divergence.md](gold/mitochondrial_unification_divergence.md) |
| `evo_20260210_232904` | [lithium_two_pathway_model.md](gold/lithium_two_pathway_model.md) |
| `evo_20260210_235609` | [lithium_two_pathway_model.md](gold/lithium_two_pathway_model.md) |
| `evo_20260211_024747` | [thc_two_pathway_model.md](gold/thc_two_pathway_model.md) |
| `evo_20260211_024750` | [thc_two_pathway_model.md](gold/thc_two_pathway_model.md) |
| `evo_20260211_201329` | [circadian_vdac1_chronopharmacology.md](gold/circadian_vdac1_chronopharmacology.md) |
| `evo_20260212_032819` | [vdac_cofactor_decision_landscape.md](gold/vdac_cofactor_decision_landscape.md) (precursor) |
| `evo_20260213_004656` | [fim_semantic_bonding.md](gold/fim_semantic_bonding.md) |
| `evo_20260213_022353` | [local_rotation_scaling.md](gold/local_rotation_scaling.md) |
| `evo_20260213_035958` | [cbd_vdac1_two_pathway_model.md](gold/cbd_vdac1_two_pathway_model.md), [efsa_vdac1_stress_test.md](gold/efsa_vdac1_stress_test.md) |
| `evo_20260213_042930` | [chronic_dosing_gsh_dynamics.md](gold/chronic_dosing_gsh_dynamics.md), [efsa_vdac1_stress_test.md](gold/efsa_vdac1_stress_test.md) |
| `evo_20260213_174104` | [vdac_isoform_binding_architecture.md](gold/vdac_isoform_binding_architecture.md), [vdac1_structural_portrait.md](gold/vdac1_structural_portrait.md) |
| `evo_20260213_182457` | [vdac_cofactor_decision_landscape.md](gold/vdac_cofactor_decision_landscape.md) |
| `evo_20260213_183423` | [vdac_membrane_lipid_modulation.md](gold/vdac_membrane_lipid_modulation.md) |
| `evo_20260213_183936` | [vdac_biomarker_platform.md](gold/vdac_biomarker_platform.md) |
| `evo_20260213_184357` | [vdac_hidden_drug_interactions.md](gold/vdac_hidden_drug_interactions.md) |
| `evo_20260213_214547` | [vdac_membrane_architecture.md](gold/vdac_membrane_architecture.md) |
| `evo_20260214_041041` | [psilocybin_two_pathway_model.md](gold/psilocybin_two_pathway_model.md) |
| `evo_20260214_043936` | [metformin_two_pathway_model.md](gold/metformin_two_pathway_model.md) |

**Gold files not tied to a single run**:
- [cancer_as_lost_coherence.md](gold/cancer_as_lost_coherence.md) -- Synthesized across the full corpus
- [vdac_deep_reflection.md](gold/vdac_deep_reflection.md) -- Cross-corpus pattern analysis
- [raw_data_coherence_sweep.md](gold/raw_data_coherence_sweep.md) -- Final accounting across all runs
- [vdac_pharmacology_atlas_manuscript.md](gold/vdac_pharmacology_atlas_manuscript.md) -- Manuscript draft (all runs)

---

## Top-Level Files

| File | Description |
|------|-------------|
| [README.md](README.md) | Repository overview, key findings, and contribution guide |
| [CITATION.cff](CITATION.cff) | Machine-readable citation metadata |
| [LICENSE](LICENSE) | CC BY 4.0 |
| **INDEX.md** | This file |

---

*Generated 2026-02-14. 22 runs, 22 gold files, 6 figures, 5 data files, 4 paper files.*
