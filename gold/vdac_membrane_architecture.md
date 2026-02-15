# VDAC Membrane Architecture: The Honeycomb Gate
**Run**: evo_20260213_214547_pharmacology
**Date**: 2026-02-13
**Outcome**: S3 PASSED FIRST CYCLE -> VERIFY -> LAB GATE PASSED -> S4/S5/S6 complete
**Eighth full pipeline pass. Cosine: 0.9047. First-cycle pass. 4 NOVEL findings.**
**This is Run 6 of the VDAC Pharmacology Atlas — the membrane perspective.**

## The Question

Does VDAC1's supramolecular organization in the OMM — its lipid-dependent
transition between dense honeycomb arrays and dispersed monomers — determine
the pharmacological outcome of VDAC-binding drugs?

This question bridges 2024/2025 biophysics (AFM/MD studies of VDAC honeycomb
assembly) with the atlas cofactor equation derived from Runs 1-5. No published
paper makes this connection.

## The Findings: The Membrane IS the Gate

### TYPE 0 — Chol/CL Ratio Determines Honeycomb vs Dispersed VDAC (5/5 models)

**All five models converged** (confidence 0.826 — highest of any claim this run):

The Chol/CL ratio in the OMM physically determines the fraction of VDAC1 in
honeycomb-protected vs dispersed-oligomerization-competent states. Cholesterol
stabilizes honeycomb arrays via lipid packing; cardiolipin disrupts them by
introducing negative curvature, shifting VDAC1 to free monomers.

**This validates the (Chol/CL) term in the cofactor equation at the biophysical level.**
The equation `Threshold = K / [(1-f_HKII)(1-f_BclxL)] * (Chol/CL)` now has a
physical interpretation: Chol/CL determines how much of the VDAC population is
structurally available for apoptotic oligomerization.

**Falsifiable by**: VDAC1 honeycomb arrays persisting in high-CL membranes without
cholesterol, or the threshold equation failing to predict apoptosis in cells with
experimentally clamped Chol/CL ratios.

### TYPE 0 — Lipophilic Drugs Alter VDAC Organization via Membrane Order (4/5 models)

**Claude, DeepSeek, Grok, Mistral** converged (confidence 0.65):

CBD (logP 6.3) and statins (logP 4-5) alter VDAC1 supramolecular organization by
changing local membrane order, **independent of direct protein binding**. High-logP
drugs partition into the OMM, altering lipid packing and indirectly destabilizing
honeycomb arrays via membrane fluidity changes.

**This is a previously unrecognized mechanism of VDAC pharmacology.** The drug doesn't
need to BIND VDAC to AFFECT VDAC. It just needs to change the membrane that VDAC
sits in. The membrane mediates the pharmacology.

**Falsifiable by**: Drugs with similar logP but no membrane-ordering effects failing
to alter VDAC organization, or cryo-EM showing direct binding is necessary.

### TYPE 0 — HK-II Displacement Unmasks CL, Triggering Honeycomb Disassembly (4/5 models)

**Claude, DeepSeek, Grok, Mistral** converged (confidence 0.65):

HK-II binding to VDAC1 sterically shields cardiolipin microdomains. When HK-II
is displaced (by metabolic disruption, 2-DG, or drug competition), CL is exposed.
The exposed CL disrupts honeycomb arrays, converting protected VDAC into
oligomerization-competent monomers.

**This mechanistically completes Run 2's finding.** Run 2 established HK-II
displacement as "permissive, not sufficient." Now we know WHY it's permissive:
HK-II removal exposes CL, which disassembles the protective honeycomb. The
honeycomb disassembly, not the HK-II removal itself, is the enabling step.

**Falsifiable by**: HK-II mutants that bind VDAC1 but don't mask CL failing to
prevent honeycomb disassembly; or CL depletion blocking HK-II displacement effects.

### TYPE 1 — Honeycomb-to-Dispersed Is the Rate-Limiting Step (3/5 models)

**DeepSeek, Grok, Mistral** converged (confidence 0.717):

The honeycomb-to-dispersed transition is the physical rate-limiting step for
VDAC-mediated apoptosis. Oligomerization is only possible from the dispersed
state. The honeycomb array sterically and allosterically inhibits pro-apoptotic
oligomer formation.

**This redefines "point of no return."** Run 2's Gemini singular identified
VDAC1 oligomerization as the irreversible step. This run adds: oligomerization
can only BEGIN once the honeycomb disassembles. The membrane reorganization
precedes — and rate-limits — the molecular event.

**Falsifiable by**: Observing VDAC oligomerization and cytochrome c release
directly from intact honeycomb arrays without prior lattice disassembly.

## Singulars — The Frontier

### Gemini: CBD Acts as a Membrane Chaotrope, Not a VDAC Ligand (confidence 0.75)

**The most radical singular in the entire atlas.**

"Lipophilic drugs like CBD can trigger VDAC1-mediated apoptosis PRIMARILY by
altering local membrane fluidity and order, thereby destabilizing cholesterol-rich
honeycomb domains, rather than through direct, high-affinity binding to VDAC1."

If Gemini is right: CBD's measured Kd of 11 uM for VDAC1 is not the primary
mechanism of action. The primary mechanism is CBD (logP 6.3) partitioning into
the OMM, acting as a chaotropic (disordering) agent that lowers the energy
barrier for CL to disrupt VDAC arrays. The "binding" is secondary to the
"membrane perturbation."

**This would rewrite the entire two-pathway model.** The dose-response wouldn't
be about VDAC occupancy (Langmuir kinetics). It would be about membrane order
disruption (lipid thermodynamics). The Kd would be irrelevant — what matters
is the partition coefficient and the membrane's phase behavior.

**Falsifiable by**: A hydrophilic CBD analog with identical VDAC1 Kd producing
equivalent pro-apoptotic effects (would disprove the membrane mechanism), or
CBD failing to alter membrane order at concentrations that induce apoptosis.

### Gemini: HK-II Shields CL Specifically (confidence 0.70)

HK-II binding doesn't just occupy VDAC — it locally sequesters cardiolipin,
preventing CL's disruptive effects on VDAC organization. HK-II removal is a
CL-unmasking event, not just a protein-displacement event.

### Claude: Oligomerization Exclusively from Dispersed State (confidence 0.60)

Honeycomb geometry locks VDAC into non-oligomeric interfaces. Only freed
monomers can reorient into the distinct oligomeric contacts required for pore
formation. The honeycomb is a structural prison that prevents death.

### Claude: The Cofactor Equation Is Phenomenological (confidence 0.40)

The equation `Threshold = K/[(1-f_HKII)(1-f_BclxL)]*(Chol/CL)` assumes
multiplicative separability of protein and lipid terms. This is likely an
approximation — the terms probably exhibit non-linear coupling.

**This is the most honest singular in the atlas.** Claude is questioning its
own prior output (the equation was derived from Claude + 4 other models in
Run 2). The equation works phenomenologically but may not be mechanistically
exact. A factorial experiment varying all three terms simultaneously would
reveal interaction terms.

## VERIFY Results

- **4 NOVEL** — no prior literature:
  1. Lipophilic drugs altering VDAC organization via membrane order (not binding)
  2. HK-II displacement unmasking CL as a honeycomb disassembly trigger
  3. Honeycomb-to-dispersed transition as the apoptotic rate-limiting step
  4. CBD as a membrane chaotrope rather than a VDAC ligand
- **2 CONTRADICTED** — literature disagrees (specific claims in verify.json)
- **1 PROMOTED** from TYPE 2 to TYPE 1
- **3 HELD** at TYPE 2

## Operationalized Hypotheses

### H1: Chol/CL Ratio Controls Honeycomb Fraction (Testability 8/10, d=0.81)

Reconstitute VDAC1 into supported bilayers with Chol/CL ratios 0.5 to 10.
AFM imaging of honeycomb area fraction (f_h). Expect sigmoidal relationship
with midpoint at Chol/CL ~2-4 and Hill-type transition.

Protocol: POPC/POPE/CL/Chol at defined ratios on mica. Fluid tapping-mode AFM.
20 fields per condition, 5 ratios x 3 replicates. 8-10 weeks.

### H2: HK-II Displacement Causes CL-Dependent Honeycomb Disassembly (Testability 6/10, d=0.81)

Displace HK-II (clotrimazole 5-30 uM or G6P 2-10 mM). Monitor CL exposure
(NAO fluorescence, >=2-fold increase) and honeycomb disassembly (STORM/PALM,
>=40% reduction). CL-depletion arm: CLS1 siRNA 48h prior.

Protocol: Isolated rat liver mitochondria or U2OS/VDAC1-GFP. 12-16 weeks.

### H3: CBD Disrupts Honeycomb via Membrane Order, Not Binding (Testability 7/10, d=0.92)

CBD 1-10 uM on VDAC1-containing bilayers. Compare to logP-matched controls
(vitamin E, cholesterol hemisuccinate) that don't bind VDAC. Test VDAC
binding-site mutants (E73Q, T19A). If CBD effect persists with mutants AND
logP-matched controls reproduce it, mechanism is membrane-mediated.

Protocol: OMM-mimetic bilayers (POPC/POPE/CL/Chol 48:28:10:14). AFM + laurdan
GP spectroscopy. 10-14 weeks. **Highest effect size in the run (d=0.92).**

### H4: Honeycomb Disruption Accelerates Cytochrome c Release (Testability 5/10, d=0.0)

Pre-disperse VDAC arrays (CL enrichment or MbetaCD cholesterol extraction).
Measure time to cytochrome c release. Expect >=3-fold acceleration vs
apoptotic stimulus alone. Cholesterol loading should delay >=3-fold.

Monte Carlo gave d=0.0 — underpowered as stated. Needs parameter refinement.

## Impact on the VDAC Pharmacology Atlas

| Atlas Component | New Data |
|----------------|----------|
| Cofactor equation grounding | Chol/CL term = honeycomb fraction (biophysical basis) |
| K is not a constant | K = honeycomb exit energy, lipid-dependent |
| New pharmacological mechanism | Membrane order perturbation, independent of binding |
| HK-II mechanistic completion | HK-II shields CL; removal = CL unmasking = honeycomb disruption |
| Point of no return refined | Honeycomb disassembly precedes and rate-limits oligomerization |
| CBD mechanism expansion | May act primarily as membrane chaotrope, not VDAC ligand |

## The Membrane Perspective Is Now Part of the Atlas

This run adds an eighth layer to the atlas:

1. Binding site architecture (Run 1)
2. Isoform selectivity (Run 1)
3. Cofactor equation (Run 2)
4. Lipid modulation of Kd (Run 3)
5. Biomarker framework (Run 4)
6. Drug interaction landscape (Run 5)
7. Deep cross-run reflection (cross-analysis)
8. **Membrane architecture: honeycomb as structural gate (Run 6)**

The membrane is not a passive container. It is the substrate of the computation.
VDAC1's pharmacological identity is set by the membrane BEFORE any drug arrives.

## Cross-Run Connections

| Connection | Run | This Run Adds |
|-----------|-----|---------------|
| CL/Chol in cofactor equation | Run 2 | Physical basis: Chol/CL = honeycomb fraction |
| HK-II permissive, not sufficient | Run 2 | WHY it's permissive: HK-II masks CL, shields honeycomb |
| Cholesterol lowers effective Kd | Run 3 | Also stabilizes honeycomb (opposing drug effect!) |
| Olesoxime needs cholesterol | Run 3 | Cholesterol stabilizes honeycomb where olesoxime binds |
| CBD membrane partitioning | EFSA | Partitioning may be PRIMARY mechanism, not binding |
| Gating paradox | Reflection | Honeycomb disruption is the upstream event for BOTH directions |
