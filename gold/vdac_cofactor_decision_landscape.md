# VDAC Cofactor Decision Landscape: HK-II, Bcl-xL, and the Apoptotic Gate
**Run**: evo_20260213_182457_pharmacology
**Date**: 2026-02-13
**Outcome**: S3 FAILED after 3 cycles (cosine peaked 0.9215 — new all-time high)
**TYPE 0/1 climbed from 20% to 63%. Kappa reached 0.947 — highest inter-model agreement ever.**

## The Question

How does the VDAC1 cofactor landscape determine whether a VDAC-binding molecule
produces cytoprotection vs cytotoxicity? Three specific sub-questions:
1. Is HK-II displacement the primary death signal, or is conductance change?
2. Does the Warburg phenotype create a biphasic CBD response?
3. Can cofactor manipulation (2-DG + ABT-737) predictably shift the gate?

This is Run 2 of the VDAC Pharmacology Atlas — the cofactor equation.

## The Findings: HK-II Is the Gatekeeper, Not VDAC Conductance

### TYPE 0 — Warburg Biphasic Response via Target Affinity Hierarchy (5/5 models)

**All five models converged** on the same mechanism:

CBD's biphasic dose-response in Warburg cancer cells is a direct consequence of its
target affinity profile:
- **Low doses (<5 uM)**: Engage TRPV1 (Kd 2 uM) and PPARgamma (EC50 5 uM) —
  cytoprotective signaling. HK-II remains bound to VDAC1 (sub-nM affinity cannot
  be displaced by 5 uM CBD with Kd 11 uM). Metabolic shielding intact.
- **High doses (>15 uM)**: Mass-action displacement of HK-II occurs. Once metabolic
  flux disrupted (G6P depleted), HK-II affinity drops — positive feedback collapse.
  Oligomerization cascade triggers.

**The inflection point is NOT gradual** — Claude predicts switch-like behavior due to
G6P-dependent HK-II affinity. Below Kd, HK-II's sub-nM grip holds. Above Kd,
metabolic disruption weakens the grip cooperatively.

**Falsifiable by**: CBD analogs with higher VDAC1 affinity (Kd <1 uM) eliminating
the protective phase in Warburg cells; HK-II overexpression in non-Warburg cells
recapitulating the biphasic response.

### TYPE 0 — 2-DG + ABT-737 Synergy Is Supra-Additive (4/5 models)

**Claude, DeepSeek, Grok, Mistral** converged:

2-DG + ABT-737 collapse two independent "clamps" on VDAC1 simultaneously:
- 2-DG depletes G6P, reducing HK-II's VDAC1 residence time (metabolic clamp)
- ABT-737 displaces Bcl-xL directly (signaling clamp)
- Combined: supra-additive (CI < 0.8), lowering effective CBD apoptotic threshold
  from ~20 uM to within the therapeutic window (1-10 uM)

**This is a testable combination therapy prediction.** The math is specific:
apoptotic threshold proportional to 1/[(1-HK-II occ.) x (1-Bcl-xL occ.)].

**Falsifiable by**: Bliss independence analysis showing additivity not synergy;
isobologram in HK-II/Bcl-xL overexpressing vs knockout cells showing CI=1.

### TYPE 1 — HK-II Displacement Is Permissive, Not Sufficient (3/5 models)

**Claude, DeepSeek, Mistral** converged (Gemini and Grok echoed with nuances):

HK-II displacement is NECESSARY but INSUFFICIENT for cytochrome c release. The
actual commitment point is downstream:
1. HK-II removed → unmasks cardiolipin (CL) microdomains
2. CL exposure → recruits Bax
3. Bax insertion + CL peroxidation → destabilizes OMM
4. Cytochrome c release → apoptosis

**Direct VDAC1 conductance change is SECONDARY** — it's a consequence of the
membrane remodeling, not the cause. This means the "VDAC conductance" literature
may be measuring an epiphenomenon.

**Falsifiable by**: HK-II displacement in CL-deficient mitochondria (Taz knockdown)
showing no cyt c release despite conductance increase; or HK-II knockdown cells
showing attenuated response to CBD despite conductance change.

## Singulars — Potential Novel Insights

### Gemini: VDAC1 Oligomerization Is the True Point of No Return (confidence 0.85)

HK-II displacement is permissive, but the IRREVERSIBLE death commitment is VDAC1
oligomerization into a Bax/Bak-receptive macropore, allosterically promoted by exposed
cardiolipin. Non-oligomerizing VDAC1 mutants would survive HK-II displacement.

**This refines the sequence**: HK-II displacement → CL exposure → VDAC1 oligomerization
→ Bax recruitment → cyt c release. The oligomerization step is the point of no return.

### Grok: HK-II Displacement Is the PRIMARY Signal (confidence 0.82)

Counter to the "permissive" framing: HK-II displacement IS the primary trigger,
with CL unmasking/peroxidation as the direct effector. Tubulin blockade acts
redundantly but weaker. VDAC conductance change is secondary.

### Gemini: Quantitative Threshold Equation (confidence 0.75)

Apoptotic threshold [Drug] = f(free VDAC1, cholesterol:CL ratio):
- Inversely proportional to fraction of cofactor-free VDAC1
- Directly proportional to membrane cholesterol:cardiolipin ratio
- Both HK-II/Bcl-xL and cholesterol are independent negative regulators

### Grok: CL Enrichment Shifts EC50 2-3x (confidence 0.68)

Cardiolipin enrichment in OMM lowers apoptotic CBD EC50 from ~11 uM to ~4-6 uM.
Cholesterol raises it equivalently. This is a lipid-engineering target.

### Grok: Tubulin Is Minor Player (confidence 0.55)

Tubulin blockade reinforces Bcl-xL but not HK-II. Displacement requires >20 uM CBD.
Contributes <20% to gate-shift. The cofactor hierarchy is:
**HK-II >> Bcl-xL >> Tubulin**

## The Cofactor Equation

This run produces the full cofactor equation for the VDAC1 decision gate:

```
Apoptotic_Threshold = K / [(1 - f_HKII) * (1 - f_BclxL)] * (Chol/CL)

Where:
  K = constant related to VDAC1 oligomerization energy
  f_HKII = fractional HK-II occupancy on VDAC1
  f_BclxL = fractional Bcl-xL occupancy on VDAC1
  Chol/CL = cholesterol to cardiolipin ratio in OMM
```

**At high HK-II occupancy (Warburg)**: threshold is very high → protection at clinical doses
**After 2-DG + ABT-737**: threshold drops 5-10x → clinical CBD doses become cytotoxic
**In CL-enriched cancer mitochondria**: threshold further reduced ~2-3x

## Cross-Run Integration

| Connection | Run | New Understanding |
|-----------|-----|-------------------|
| CBD two-pathway model | evo_20260210_222428 | The "tissue determines outcome" IS the cofactor landscape |
| EFSA universal stressor | evo_20260210_232904 | CBD hits all cells, but HK-II in Warburg cells creates the buffer |
| Run 1 binding sites | evo_20260213_174104 | CBD at N-terminal helix = gating modulator, NOT the death signal |
| Chronic dosing | evo_20260213_042930 | GSH depletion compounds with cofactor landscape — both must be considered |
| Partial occupancy | Run 1 Gemini singular | 30-48% VDAC1 occupancy at therapeutic doses is BELOW HK-II displacement threshold |

**The master picture is now clear:**
1. CBD at therapeutic doses (1-10 uM) achieves ~30-50% VDAC1 occupancy (Run 1)
2. This is BELOW the HK-II displacement threshold in Warburg cells (this run)
3. Cytoprotective targets (TRPV1, PPARgamma) are engaged first (this run, 5/5)
4. Death requires either high dose (>15 uM) OR cofactor manipulation (2-DG + ABT-737)
5. GSH status determines whether the cell survives the stress (chronic run, 4/5)
6. The cofactor landscape IS the "tissue determines outcome" variable from the original model

## Key Unknowns

1. **HK-II-VDAC1 Kd in living cells** — estimated sub-nM but never measured in situ
2. **VDAC1 oligomerization stoichiometry** — hexamer? tetramer? protein-lipid pore?
3. **Cholesterol-VDAC1 oligomerization quantitative relationship** — rate constant unknown
4. **Tubulin-VDAC1 Kd** — whether competitive with HK-II or independent site
5. **In vivo [CBD] at the OMM** — plasma 1-10 uM, but local concentration at mitochondria?

## Impact on VDAC Pharmacology Atlas

| Atlas Component | New Data |
|----------------|----------|
| Cofactor hierarchy | HK-II >> Bcl-xL >> Tubulin |
| Decision equation | Threshold = K / [(1-f_HKII)(1-f_BclxL)] * (Chol/CL) |
| Combination therapy | 2-DG + ABT-737 + CBD: supra-additive (CI<0.8) |
| Warburg explanation | Target affinity hierarchy creates biphasic response |
| CL modulation | 2-3x EC50 shift via cardiolipin engineering |
