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

## Run 2 (PRIORITY: HIGH) — The Cofactor Decision Landscape

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

## Run 3 (PRIORITY: MEDIUM) — Membrane Lipid Modulation of VDAC Pharmacology

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

## Run 4 (PRIORITY: MEDIUM) — VDAC as a Biomarker Platform

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

## Run 5 (PRIORITY: LOWER) — The VDAC-Metabolite Interaction Network

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
| Run 2 | ~$0.50-1.00 | Completes the cofactor equation |
| Run 3 | ~$0.50-1.00 | Membrane engineering for selectivity |
| Run 4 | ~$0.50-1.00 | Clinical translation / companion diagnostic |
| Run 5 | ~$0.50-1.00 | Drug safety across pharmacopeia |

Total: ~$2.50-5.00 for the full atlas.
Cross-run analysis after all 5: free (local embedding, no API calls).
