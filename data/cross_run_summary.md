# Cross-Run Convergence Report

**Generated**: 2026-02-17 23:41 UTC
**Runs analyzed**: 22
**Total claims**: 192
**Cross-matches found**: 10

## Runs

| Session | Domain | S3 | Claims |
|---------|--------|----|--------|
| evo_20260210_232904_pharmacology | pharmacology | FAIL | 13 |
| evo_20260210_235609_pharmacology | pharmacology | FAIL | 9 |
| evo_20260211_024747_pharmacology | pharmacology | FAIL | 9 |
| evo_20260211_024750_neuroscience | neuroscience | FAIL | 7 |
| evo_20260211_201329_pharmacology+bioelectric | pharmacology+bioelectric | FAIL | 10 |
| evo_20260212_032819_pharmacology | pharmacology | FAIL | 7 |
| evo_20260213_004656_consciousness | consciousness | FAIL | 10 |
| evo_20260213_022353_consciousness+chemistry | consciousness+chemistry | FAIL | 15 |
| evo_20260213_035958_pharmacology | pharmacology | PASS | 9 |
| evo_20260213_042930_pharmacology | pharmacology | PASS | 9 |
| evo_20260213_174104_pharmacology | pharmacology | FAIL | 6 |
| evo_20260213_182457_pharmacology | pharmacology | FAIL | 9 |
| evo_20260213_183423_pharmacology | pharmacology | PASS | 4 |
| evo_20260213_183936_pharmacology | pharmacology | PASS | 7 |
| evo_20260213_184357_pharmacology | pharmacology | PASS | 7 |
| evo_20260213_214547_pharmacology | pharmacology | PASS | 8 |
| evo_20260214_041041_pharmacology | pharmacology | FAIL | 8 |
| evo_20260214_043936_pharmacology | pharmacology | FAIL | 12 |
| evo_20260217_035010_pharmacology | pharmacology | PASS | 6 |
| evo_20260217_035450_pharmacology | pharmacology | FAIL | 9 |
| evo_20260217_233407_pharmacology | pharmacology | FAIL | 10 |
| evo_20260217_233429_pharmacology | pharmacology | PASS | 8 |

## Cross-Validated Singulars

### CROSS-VALIDATED SINGULAR (cosine=0.7896)
- **Run A** (evo_20260217_035010_pharmacology, TYPE 0): Cancer OMMs (↑cholesterol ~2x, ↓CL ~50%) have lower threshold (~0.5x I) for US-induced VDAC1 transition vs. healthy cells.
- **Run B** (evo_20260217_035450_pharmacology, TYPE 3): The elevated OMM cholesterol in cancer cells acts as a "mechanoresistor," increasing the acoustic energy density required to trigger VDAC1-mediated ap

### CROSS-VALIDATED SINGULAR (cosine=0.7765)
- **Run A** (evo_20260210_232904_pharmacology, TYPE 3): Lithium neuroprotection at low dose (<0.5 mM) primarily via partial GSK3β inhibition (IC50 1-2 mM), stabilizing β-catenin, upregulating BDNF and autop
- **Run B** (evo_20260210_235609_pharmacology, TYPE 0): 2:** Neuroprotection at low dose is mediated primarily by indirect GSK-3β inhibition via Akt-Ser9 phosphorylation amplification, with effective EC50 ~

### CROSS-VALIDATED SINGULAR (cosine=0.7685)
- **Run A** (evo_20260213_035958_pharmacology, TYPE 3): Membrane partitioning of CBD (logP 6.3) creates local mitochondrial membrane concentrations 100-1000× above free aqueous levels, potentially achieving
- **Run B** (evo_20260213_183423_pharmacology, TYPE 0): Increased OMM cholesterol in some cancers significantly raises the effective local concentration of CBD at VDAC, lowering its apparent functional Kd b

## Independent Replications

- **cosine=0.8045** | evo_20260213_214547_pharmacology ↔ evo_20260217_035010_pharmacology
  A: The Chol/CL ratio in the OMM physically determines the fraction of VDAC1 in honeycomb vs. dispersed states, and this rat
  B: Reorganization of OMM cholesterol-rich lipid domains can shift VDAC1 from a honeycomb to a dispersed state.

- **cosine=0.789** | evo_20260213_035958_pharmacology ↔ evo_20260213_042930_pharmacology
  A: 1:** *CBD is unlikely to reach VDAC1-saturating concentrations (≥11 µM) in healthy hepatocytes under standard oral dosin
  B: At 50mg/day oral CBD, steady-state hepatic [CBD] ~0.1-0.5μM (plasma 0.05-0.2μM × liver enrichment), VDAC occ <5%, ROS lo

- **cosine=0.7818** | evo_20260217_035010_pharmacology ↔ evo_20260217_035450_pharmacology
  A: Ultrasound at clinically relevant frequencies and intensities can deliver sufficient mechanical energy to the OMM to tra
  B: Therapeutic ultrasound (20-100 kHz) coupled with microbubbles generates localized inertial cavitation events capable of 

## Cross-Promoted (TYPE 2 → validated)

- **cosine=0.8** | evo_20260217_035010_pharmacology (T0) ↔ evo_20260217_035450_pharmacology (T2)
  A: Cancer OMMs (↑cholesterol ~2x, ↓CL ~50%) have lower threshold (~0.5x I) for US-induced VDAC1 transition vs. healthy cell
  B: 4**: *Cancer cells with cholesterol-loaded OMMs exhibit higher apoptotic thresholds under US due to stabilized VDAC1 mon

- **cosine=0.7914** | evo_20260211_024747_pharmacology (T2) ↔ evo_20260211_024750_neuroscience (T0)
  A: 1:** Chronic low-dose THC (≤2.5 mg/day) improves wellbeing via *biphasic CB1 signaling*: G-protein activation (EC50 ~10 
  B: 1:** The biphasic (inverted-U) dose-response of THC occurs because low CB1 occupancy (<20%) preferentially engages Gi/o-

- **cosine=0.7648** | evo_20260213_182457_pharmacology (T2) ↔ evo_20260213_214547_pharmacology (T0)
  A: 4:** Cardiolipin enrichment at the OMM lowers the apoptotic threshold by ~2-fold by stabilizing VDAC1 oligomers and faci
  B: The Chol/CL ratio in the OMM physically determines the fraction of VDAC1 in honeycomb vs. dispersed states, and this rat

- **cosine=0.7575** | evo_20260213_182457_pharmacology (T2) ↔ evo_20260213_183423_pharmacology (T0)
  A: 4:** Cardiolipin enrichment at the OMM lowers the apoptotic threshold by ~2-fold by stabilizing VDAC1 oligomers and faci
  B: Cardiolipin at OMM contact sites alters VDAC gating dynamics, likely promoting a conformation with higher affinity for c

## Structural Patterns (Isomorphism)

- **two_pathway**: evo_20260210_232904_pharmacology, evo_20260212_032819_pharmacology
- **threshold_crossover**: evo_20260210_232904_pharmacology, evo_20260210_235609_pharmacology, evo_20260211_024747_pharmacology, evo_20260211_024750_neuroscience, evo_20260212_032819_pharmacology, evo_20260213_022353_consciousness+chemistry, evo_20260213_042930_pharmacology, evo_20260213_182457_pharmacology, evo_20260213_214547_pharmacology, evo_20260214_041041_pharmacology, evo_20260214_043936_pharmacology, evo_20260217_035450_pharmacology, evo_20260217_233407_pharmacology
- **dose_dependent**: evo_20260210_232904_pharmacology, evo_20260211_024747_pharmacology, evo_20260212_032819_pharmacology, evo_20260213_035958_pharmacology, evo_20260213_042930_pharmacology, evo_20260213_174104_pharmacology, evo_20260213_182457_pharmacology, evo_20260214_041041_pharmacology, evo_20260217_233429_pharmacology
- **kinetic**: evo_20260211_024747_pharmacology, evo_20260214_043936_pharmacology

## Cosine Distribution (cross-run pairs)

- Min: -0.1937
- Median: 0.2632
- Mean: 0.2542
- Max: 0.8045
- N pairs: 17532
