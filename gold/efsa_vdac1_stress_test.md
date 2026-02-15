# EFSA Challenge: VDAC1 Dual-Pathway Stress Test
**Run**: evo_20260213_035958_pharmacology
**Date**: 2026-02-13
**Outcome**: S3 PASSED (cycle 2) -> VERIFY -> LAB GATE PASSED -> S4/S5/S6 complete
**This is a full pipeline pass — the third ever.**

## The Question

Four hostile peer-review challenges to the VDAC1 dual-pathway model, aimed at
the EFSA 2mg/day CBD safety limit:
1. Does CYP450 clearance prevent VDAC1 saturation? Does 7-OH-CBD also bind?
2. Does CBD discriminate VDAC1 vs VDAC2? Could dual inhibition harm healthy cells?
3. Is the 2x ROS scavenging ratio realistic? When does glutathione deplete?
4. Does CBD clog the pore (ATP starvation) or lock it open (ROS)? Is the model incomplete?

## The Verdict: 5/5 Models Agreed — The Model Has a Real Problem

### TYPE 0 — VDAC Isoform Non-Selectivity (5/5 models)

**The single most important finding of this run.**

All five models independently concluded: CBD does NOT meaningfully discriminate
between VDAC1 and VDAC2. The isoforms share >70% sequence homology in
transmembrane domains. No published data demonstrates isoform selectivity.

**Why this matters**: VDAC2 is anti-apoptotic — it sequesters BAK and prevents
its oligomerization. If CBD inhibits VDAC2 alongside VDAC1, it releases BAK
in ALL cells, not just compromised ones. This undermines the core selectivity
argument of the dual-pathway model.

**Falsifiable by**: Binding assays showing >10x Kd difference between CBD-VDAC1
and CBD-VDAC2. If selectivity exists, the model is rescued. If it doesn't,
the "healthy cells are safe" claim needs major revision.

**This directly challenges our preprint.** The cofactor equation assumes VDAC1
selectivity. If VDAC2 is equally engaged, the equation needs a VDAC2 term.

### TYPE 0 — GSH Depletion Threshold ~20 uM (4/5 models)

The 2x ROS scavenging ratio is plausible for hepatocytes vs HCC. But glutathione
depletion requires intracellular CBD >20 uM — a concentration unlikely in healthy
liver under oral dosing but possible in metabolically compromised cells.

**This partially supports EFSA's caution**: if a patient has pre-existing liver
compromise (fatty liver, hepatitis, alcohol use), the safety margin shrinks.
The 2mg/day limit may be appropriate for at-risk populations even if it's
overly conservative for healthy individuals.

### TYPE 1 — CYP450 Clearance Limits Free Hepatic CBD (3/5 models)

CBD is unlikely to reach VDAC1-saturating concentrations (>=11 uM) in healthy
hepatocytes under standard oral dosing. High first-pass metabolism (CYP2C19/
CYP3A4) and low bioavailability (6-19%) limit steady-state free liver CBD
to ~1-10 uM.

**But**: 7-OH-CBD (primary metabolite, 20-40% of dose) may contribute to VDAC1
occupancy. Its Kd is unknown. Grok predicted ~10-20 uM based on structural
similarity. This is the critical unknown — if 7-OH-CBD binds VDAC1, the
effective occupancy window is wider than the parent compound alone.

### TYPE 1 — Allosteric Gating, Not Pore Occlusion (3/5 models)

CBD modulates VDAC gating allosterically from within the membrane, not by
physically plugging the pore. This means ATP starvation and ROS generation
are NOT mutually exclusive — they're a continuum of conductance dysregulation.

**The ROS-focused model misses half the picture.** Partial closure reduces ATP
flux AND increases electron leak simultaneously. The death pathway is dual:
energy starvation + oxidative damage in parallel.

## Singular Gold

### Claude — Membrane Partitioning Eliminates Selectivity

CBD's logP of 6.3 creates 100-1000x enrichment in mitochondrial membranes.
This SOLVES the PK problem (bulk free CBD < 11 uM, but local membrane
concentration >> 11 uM) while DESTROYING the selectivity argument (membrane
partitioning is cell-type-indiscriminate).

This is the deepest challenge to the preprint's thesis: the same physics
that lets CBD reach VDAC1 at low doses also means it reaches VDAC1 in
every cell type equally.

### Gemini — Occlusion vs Lock-Open Is False Dichotomy

"The outcome (low-conductance starvation vs. high-conductance uncoupling)
depends on the pre-existing metabolic state of the cell."

The mechanism isn't fixed — it's state-dependent. Same molecule, same target,
different mode of action depending on the cell's current VDAC gating state.
This is the two-pathway model at the channel-biophysics level.

### Grok — 7-OH-CBD Binding Prediction

7-OH-CBD likely binds VDAC1 with Kd ~10-20 uM based on structural preservation
of the core scaffold. Falsifiable by direct ITC/SPR measurement. If confirmed,
the effective VDAC1 occupancy time doubles because 7-OH-CBD accumulates with
slower clearance than parent CBD.

## Operationalized Hypotheses (Full Pipeline)

### H4: GSH Depletion Assay (Testability: 9/10)
Treat primary hepatocytes + HCC lines with CBD dose series (1-100 uM).
Measure GSH/GSSG by Tietze assay, ROS by DCFDA, MitoSOX, viability by
CellTiter-Glo. Pre-treat with NAC or BSO. Timeline: 4-6 weeks.

**Expected**: EC50 ratio (healthy:HCC) <3x; both >20 uM. ROS scavenging <2x.
**Null**: EC50 ratio >5x (selectivity exists) OR depletion at <10 uM in HCC.

### H1: Membrane Enrichment Quantification (Testability: 7/10)
Treat hepatocytes with [3H]-CBD or deuterated CBD (1, 3, 10 uM). Isolate
mitochondria, separate membrane fractions, quantify by LC-MS/MS.

**Expected**: Enrichment >=50x; no significant difference between cell types.
**Null**: Enrichment <50x (occupancy problem stands).

### H3: VDAC1 vs VDAC2 Selectivity (Testability: 7/10)
Measure CBD binding to VDAC1 and VDAC2 by MST/ITC in lipid nanodiscs.
Functional assay: BAK oligomerization +/- VDAC2 knockdown.

**Expected**: Kd ratio <5x; CBD increases BAK in healthy hepatocytes.
**Null**: Kd ratio >10x (selectivity exists — model rescued).

### H2: Electrophysiology — Gating vs Occlusion (Testability: 6/10)
Reconstituted VDAC1 in planar lipid bilayers. Single-channel recordings
+/- CBD (1-100 uM). Analyze conductance histograms, V1/2 shifts.

**Expected**: Subconductance states (30-70% of full open), V1/2 shift >=10 mV.
**Null**: Zero-conductance block events (pure occlusion).

## Monte Carlo Results

All four hypotheses achieved power = 1.0 with effect sizes 0.73-1.01 (Cohen's d).
300 iterations per hypothesis, all converged. The experiments are well-powered.

## Impact on the Preprint

This run stress-tested the preprint and found it **partially vulnerable**:

| Preprint Claim | Status After Stress Test |
|----------------|------------------------|
| VDAC1 is the decision gate | SURVIVES — but must include VDAC2 |
| Cofactor equation predicts selectivity | CHALLENGED — needs VDAC2 term |
| Healthy cells buffer CBD at VDAC1 | COMPLICATED — membrane partitioning solves PK but breaks selectivity |
| ROS is the death pathway | INCOMPLETE — ATP starvation runs in parallel |
| 2x scavenging ratio is valid | PLAUSIBLE — but GSH depletion threshold ~20 uM provides margin |

**The preprint should be updated** to acknowledge:
1. VDAC2 non-selectivity as an open question requiring experimental resolution
2. Dual death pathway (ROS + ATP starvation)
3. 7-OH-CBD as potential occupancy contributor
4. Membrane partitioning as both enabling and selectivity-destroying

This is the gate doing exactly what it should — catching weaknesses before
a reviewer does.

## Cross-Run Pattern

EFSA run joined the `dose_dependent` structural pattern alongside the original
lithium, THC, and VDAC1 cofactor runs. The dose-dependence here is more
nuanced: it's not just "high dose = toxic" but "effective dose at VDAC depends
on membrane partitioning, metabolite contribution, and pre-existing GSH status."
