# VDAC Biomarker Platform: Risk-Stratified Prescribing
**Run**: evo_20260213_183936_pharmacology
**Date**: 2026-02-13
**Outcome**: S3 PASSED (cycle 2) -> VERIFY -> LAB GATE PASSED -> S4/S5/S6 complete
**Sixth full pipeline pass. Kappa: 0.993 (cycle 1) — near-perfect inter-model agreement.**

## The Question

Can VDAC-related biomarkers predict individual vulnerability to mitochondrial
modulators? Four sub-questions on GSH/GSSG as predictor, CTC VDAC1 expression,
a mitochondrial stress panel, and retrospective validation in clinical datasets.

This is Run 4 of the VDAC Pharmacology Atlas — the clinical translation question.

## The Findings: GSH Predicts Risk, But With Caveats

### TYPE 0 — GSH/GSSG Ratio Predicts Hepatotoxicity Risk (4/5 models)

**Claude, DeepSeek, Grok, Mistral** converged:

Baseline peripheral blood GSH/GSSG ratio predicts hepatotoxicity risk from
VDAC-engaging drugs (CBD, valproate, acetaminophen). Mechanism: low GSH/GSSG
reflects impaired mitochondrial antioxidant capacity; VDAC modulation exacerbates
ROS, triggering hepatocyte death and ALT/GGT elevation.

**This directly validates the Resilience Biomarker Framework** from the atlas.
The chronic dosing run (4/5 TYPE 0) established GSH synthesis rate as the key
variable. This run adds the clinical readout: peripheral blood GSH/GSSG.

### TYPE 0 — Mito Panel Is Pharmacodynamic, Not Predictive (4/5 models)

**Claude, DeepSeek, Gemini, Mistral** converged:

A "mitochondrial stress test" panel (GSH, ATP/ADP, MMP by TMRM) is a
**pharmacodynamic readout** — it measures on-target effect AFTER drug exposure.
It is NOT a predictive companion diagnostic because baseline values integrate
too many confounding variables (nutrition, comorbidities, genetics).

**This is an important negative finding.** The atlas's Tier 2 biomarkers
(ATP/ADP ratio, MitoSOX/TMRM) are useful for monitoring, not prediction.
Only GSH/GSSG and clinical markers (ALT/GGT) have predictive power.

### TYPE 1 — Epidiolex Trials as Retrospective Validation (3/5 models)

**Claude, Grok, Mistral** converged:

GWPCARE trials (Epidiolex Phase III) measured ALT/GGT and CBD plasma levels.
Retrospective analysis could correlate these with hepatotoxicity — BUT only
if stored samples exist for GSH/GSSG measurement. Sample degradation is a risk.

**This is actionable**: Contact GW Pharma/Jazz Pharmaceuticals about stored
biobank samples from GWPCARE1-4 trials.

### TYPE 1 — CTC VDAC1 Expression Is NOT Reliable (3/5 models)

**Claude, DeepSeek, Mistral** converged:

CTC VDAC1 is a poor biomarker because:
- CTCs are rare (1-100/mL, often <5)
- 50% phenotypic heterogeneity
- No validated quantitative CTC-VDAC1 assay exists
- Erastin acts primarily via system Xc- inhibition (VDAC involvement debated)

## Singulars

### Gemini: Blood GSH Is Low-Fidelity for Liver (confidence 0.75)

**Critical dissent**: Peripheral blood GSH/GSSG does NOT reliably reflect
hepatic-specific redox state because the liver maintains its own compartmentalized
GSH pool not in rapid equilibrium with circulating blood. Correlation likely r < 0.7.

**This matters**: If Gemini is right, the entire GSH-based prediction framework
needs a liver-specific readout. Options: GGT isoforms, urinary NAPQI metabolites,
or breath tests for hepatic glutathione (MEGX-like). The 4/5 convergence on
GSH/GSSG as predictor may be overconfident.

### Grok: CTC VDAC1 Varies 10-fold by EMT Status (confidence 0.78)

VDAC1 expression in CTCs varies 10-fold depending on epithelial-mesenchymal
transition status. Even if you could reliably capture and measure CTCs,
the VDAC1 reading would be meaningless without EMT stratification.

## Lab Gate Results

Lab Gate was appropriately harsh — only **3/19 claims passed**:
- H1: GSH stratification predicts CBD hepatotoxicity (feasible, novel)
- H2: VDAC1 knockdown reduces CBD-induced ROS (feasible, novel)
- H3: Three-component panel as pharmacodynamic marker (feasible, borderline)

Filtered out:
- CTC VDAC1: not feasible (rarity, heterogeneity)
- Epidiolex retrospective: lacks novelty (standard pharmacovigilance)
- Mito stress panel as companion diagnostic: not feasible (confounders)

## Operationalized Hypotheses

### H1: GSH Stratification (Testability 8/10, d=0.86)
Stratify primary hepatocytes by baseline GSH/GSSG into tertiles.
Treat with CBD 10 uM. Low-GSH tertile shows >=3x more cell death.

### H2: VDAC1 Knockdown Reduces CBD ROS (Testability 9/10, d=1.07)
siRNA VDAC1 in HepG2. CBD 10 uM, 48h. ROS decreases >=50%.
**Highest effect size of all 4 hypotheses.**

### H3: Three-Panel Pharmacodynamic Marker (Testability 7/10, d=0.81)
Escalating CBD/erastin doses. Panel (GSH, ATP/ADP, MMP) detects
toxicity >=6h before viability assays.

### H4: VDAC1 Expression Panel (Testability 5/10, d=0.0)
Rank cancer cell lines by VDAC1 expression, correlate with
erastin/CBD sensitivity. **Monte Carlo gave d=0.0 — underpowered.**

## Impact on Resilience Biomarker Framework

| Framework Component | This Run's Contribution |
|--------------------|-----------------------|
| Tier 1 GSH/GSSG | VALIDATED as risk predictor (4/5 TYPE 0) |
| Tier 1 ALT/GGT | Confirmed as damage proxy |
| Tier 2 ATP/ADP | DOWNGRADED: pharmacodynamic, not predictive |
| Tier 2 MitoSOX/TMRM | DOWNGRADED: pharmacodynamic, not predictive |
| Tier 2 VDAC1 expression | NEGATIVE: CTC measurement unreliable |
| Blood vs liver GSH | NEW CAVEAT: Gemini dissent on compartmentalization |
| Clinical validation | ACTIONABLE: GWPCARE stored samples |

## Updated Risk Stratification

```
PREDICTIVE (before drug):
  - GSH/GSSG ratio (blood) — with caveat re: liver compartmentalization
  - ALT/GGT (standard liver function)
  - Clinical history (NAFLD, alcohol, comorbidity)

PHARMACODYNAMIC (during drug):
  - Mito stress panel (GSH, ATP/ADP, MMP) — monitor, not predict
  - Serial ALT/GGT

NOT USEFUL:
  - CTC VDAC1 expression (too heterogeneous, too few CTCs)
  - VDAC1 protein levels in blood (no validated assay)
```
