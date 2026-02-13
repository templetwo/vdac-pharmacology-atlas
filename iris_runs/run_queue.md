# IRIS Gate Evo Run Queue — VDAC Pharmacology Atlas

Pre-written questions ready to fire when API credits are available.
Priority order reflects maximum scientific yield per run.

---

## Run 1 (COMPLETED) — Isoform Selectivity & Binding Site Architecture

**Session**: evo_20260213_174104_pharmacology
**Outcome**: S3 FAILED (cosine 0.9124 peak) — rich gold extracted
**Gold**: [vdac_isoform_binding_architecture.md](https://github.com/templetwo/iris-evo-findings/blob/main/gold/vdac_isoform_binding_architecture.md)
**Key findings**: Three non-overlapping VDAC1 binding sites (TYPE 0, 4/5); VDAC2 N-terminal >=10-fold selectivity (TYPE 1, 3/5); two pharmacological classes — gating modulators vs pore blockers (TYPE 1, 3/5)

**Domain**: pharmacology + structural_biology

```
What structural features of VDAC isoforms determine ligand selectivity?
Specifically: (1) Do CBD, erastin, and DIDS share a common binding site on
VDAC1 or engage distinct allosteric mechanisms? (2) What structural differences
between VDAC1 and VDAC2 — particularly the additional N-terminal residues of
VDAC2 and the BAK-binding interface — could enable isoform-selective ligand
design? (3) Does the VDAC1 N-terminal helix (gating domain) vs barrel wall
(conductance domain) distinction predict different pharmacological outcomes
for allosteric modulators vs pore blockers? (4) Is VDAC2-sparing compound
design feasible given >70% transmembrane homology, or must selectivity be
achieved through the cofactor landscape (HK-II occupancy, BAK competition)?
```

**Why first**: This determines whether the entire "selective VDAC modulator"
concept is physically possible. If the answer is "no selectivity possible at
the binding level," the atlas pivots entirely to cofactor/context-dependent
strategies.

---

## Run 2 (COMPLETED) — The Cofactor Decision Landscape

**Session**: evo_20260213_182457_pharmacology
**Outcome**: S3 FAILED (cosine 0.9215 — all-time high) — rich gold extracted
**Gold**: [vdac_cofactor_decision_landscape.md](https://github.com/templetwo/iris-evo-findings/blob/main/gold/vdac_cofactor_decision_landscape.md)
**Key findings**: 5/5 Warburg biphasic response (TYPE 0); 4/5 2-DG+ABT-737 synergy (TYPE 0); 3/5 HK-II displacement is permissive not sufficient (TYPE 1); cofactor equation derived

**Domain**: pharmacology + bioelectric

```
How does the VDAC1 cofactor landscape — specifically hexokinase-II (HK-II)
occupancy, Bcl-xL binding, tubulin blockade, and membrane lipid composition
(cardiolipin, cholesterol) — determine whether a VDAC-binding small molecule
produces cytoprotection vs cytotoxicity? (1) Does HK-II displacement from
VDAC1 by CBD or erastin trigger cytochrome c release, and is this the primary
death signal rather than direct conductance change? (2) Does the Warburg
phenotype (high glycolysis, high HK-II-VDAC1 coupling) paradoxically protect
cancer cells from VDAC-mediated apoptosis at low CBD doses while sensitizing
them at high doses? (3) Can pharmacological manipulation of the cofactor
landscape (e.g., 2-deoxyglucose to displace HK-II, ABT-737 to displace
Bcl-xL) predictably shift the VDAC decision gate from survival to apoptosis?
```

**Why second**: The cofactor equation from the original preprint was onto
something but lacked the VDAC2 term. This run fills in the full equation.

---

## Run 3 (COMPLETED) — Membrane Lipid Modulation of VDAC Pharmacology

**Session**: evo_20260213_183423_pharmacology
**Outcome**: S3 PASSED FIRST CYCLE (cosine 0.9512 — record) -> FULL PIPELINE
**Gold**: [vdac_membrane_lipid_modulation.md](https://github.com/templetwo/iris-evo-findings/blob/main/gold/vdac_membrane_lipid_modulation.md)
**Key findings**: 5/5 olesoxime requires cholesterol (TYPE 0); 5/5 cancer cholesterol lowers CBD Kd to 3-6uM (TYPE 0); 4/5 CL alters VDAC gating (TYPE 0); 3/5 cancer-mimetic liposome delivery (TYPE 1); 4 hypotheses operationalized; 3 NOVEL

**Domain**: pharmacology + biophysics

```
Does the outer mitochondrial membrane lipid composition modulate VDAC-ligand
interactions differently in healthy vs cancer mitochondria? Specifically:
(1) Cardiolipin is enriched in inner mitochondrial membrane but present in
OMM contact sites — does it alter VDAC gating or CBD binding at these sites?
(2) Cancer cell membranes have altered cholesterol/phospholipid ratios — does
this change the effective Kd of lipophilic VDAC modulators like CBD (logP 6.3)?
(3) Olesoxime (TRO19622) binds VDAC via a cholesterol-recognition motif —
does membrane cholesterol content determine whether olesoxime is neuroprotective
or neutral? (4) Could membrane-targeted delivery (liposomes with specific lipid
compositions) enhance or reduce VDAC modulator potency in a cell-type-specific way?
```

**Why third**: The membrane partitioning paradox from the EFSA run (logP 6.3
enables occupancy but destroys selectivity) might be resolvable through
lipid-environment manipulation. This is the "can we engineer selectivity
back in?" question.

---

## Run 4 (COMPLETED) — VDAC as a Biomarker Platform

**Session**: evo_20260213_183936_pharmacology
**Outcome**: S3 PASSED (cycle 2) -> FULL PIPELINE (6th pass)
**Gold**: [vdac_biomarker_platform.md](https://github.com/templetwo/iris-evo-findings/blob/main/gold/vdac_biomarker_platform.md)
**Key findings**: 4/5 GSH/GSSG predicts risk (TYPE 0); 4/5 mito panel is pharmacodynamic not predictive (TYPE 0); CTC VDAC1 unreliable; Gemini dissent on blood-liver GSH compartmentalization

**Domain**: pharmacology + clinical

```
Can VDAC-related biomarkers predict individual vulnerability to mitochondrial
modulators, enabling risk-stratified prescribing? (1) Does baseline GSH/GSSG
ratio in peripheral blood or liver function tests (ALT, GGT) reliably predict
hepatotoxicity risk from VDAC-engaging drugs (CBD, valproate, acetaminophen)?
(2) Is VDAC1 expression level in circulating tumor cells a predictive biomarker
for response to VDAC-targeting cancer therapies (erastin, CBD)? (3) Could a
simple "mitochondrial stress test" panel (GSH, ATP/ADP ratio, MMP by TMRM)
serve as a companion diagnostic for VDAC-modulating drugs? (4) What existing
clinical datasets (Epidiolex trials, erastin Phase I) contain the pharmacokinetic
and hepatic biomarker data needed to retrospectively validate this framework?
```

**Why fourth**: This is the translational output. If a simple blood panel can
predict who's safe and who's not, that's a clinical tool, not just a paper.

---

## Run 5 (COMPLETED) — The VDAC-Metabolite Interaction Network

**Session**: evo_20260213_184357_pharmacology
**Outcome**: S3 PASSED FIRST CYCLE (cosine 0.9547 — new record) -> FULL PIPELINE (7th pass)
**Gold**: [vdac_hidden_drug_interactions.md](https://github.com/templetwo/iris-evo-findings/blob/main/gold/vdac_hidden_drug_interactions.md)
**Key findings**: 5/5 VPA modulates VDAC1 (TYPE 0); 5/5 NAPQI covalently modifies VDAC cysteines (TYPE 0); 5/5 lipophilic statins are VDAC modulators (TYPE 0); metformin disputed; 3 NOVEL

**Domain**: pharmacology

```
Beyond CBD, which commonly prescribed drugs or their metabolites interact with
VDAC at therapeutically relevant concentrations? (1) Valproic acid is a known
hepatotoxin and mitochondrial modulator — does it engage VDAC1? (2) Acetaminophen
toxicity involves mitochondrial dysfunction — is VDAC part of the NAPQI damage
cascade? (3) Metformin accumulates in mitochondria and inhibits Complex I — does
it also modulate VDAC gating? (4) Statins (particularly lipophilic ones like
atorvastatin) partition into membranes — is VDAC occupancy a hidden variable in
statin-associated myopathy? (5) What is the predicted VDAC interaction landscape
for the top 20 most prescribed drugs with known mitochondrial effects?
```

**Why fifth**: This is the "hidden variable" run. If VDAC modulation is an
unrecognized mechanism for commonly prescribed drugs, that's a public health finding.

---

## Estimated Budget

| Run | Estimated API Cost | Expected Value |
|-----|-------------------|----------------|
| Run 1 | DONE (~$0.80) | YES — selective design IS possible (N-terminal selectivity filter) |
| Run 2 | DONE (~$0.80) | Cofactor equation derived: Threshold = K/[(1-f_HKII)(1-f_BclxL)]*(Chol/CL) |
| Run 3 | DONE (~$0.90) | YES — cholesterol lowers Kd 2-3x; olesoxime needs cholesterol; 3 NOVEL |
| Run 4 | DONE (~$0.90) | GSH predicts risk; mito panel monitors not predicts; CTC unreliable |
| Run 5 | DONE (~$0.90) | VPA, NAPQI, statins all hit VDAC; metformin disputed; 3 NOVEL |

Total spent: ~$4.30 for the full atlas (5/5 runs complete).
Cross-run analysis: free (local embedding, no API calls).

## ATLAS COMPLETE

All 5 runs fired and analyzed. Results:
- **3 full pipeline passes** (Runs 3, 4, 5) — 16 operationalized hypotheses
- **2 S3-failed with rich gold** (Runs 1, 2) — binding site map + cofactor equation
- **14 gold-extracted findings** across 5 runs
- **9 NOVEL findings** (no prior literature) identified by Perplexity VERIFY
- **Cosine trajectory**: 0.9124 -> 0.9215 -> 0.9512 -> 0.8807 -> 0.9547
