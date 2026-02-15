# Circadian-VDAC1 Chronopharmacology Model
**Run**: evo_20260211_201329_pharmacology+bioelectric
**Date**: 2026-02-11
**Outcome**: S3 FAILED (3 cycles, 15 calls) — gold extracted via human fact-check

## The Question

"Does circadian cycling of mitochondrial membrane potential alter the dose-response
threshold at which CBD shifts from cytoprotective to cytotoxic effects via VDAC1,
and what time-dependent mechanisms govern this transition?"

## What the Models Got Wrong

3/5 models (gemini, grok, mistral) converged on the claim that VDAC1 opens at
depolarized ΔΨm and closes at hyperpolarized ΔΨm. S2 promoted this to TYPE 1.

**This is factually incorrect.** VDAC1 gating is bell-curved around ~0 mV on the
outer mitochondrial membrane (OMM). The models confused inner membrane ΔΨm
(-160 to -180 mV) with OMM voltage. VDAC1 never sees ΔΨm directly.

This is the first documented case where IRIS Gate Evo TYPE 1 consensus promoted
a factually wrong claim. Convergence ≠ truth when training data biases are shared.

## What Claude Got Right (Singulars)

Claude's TYPE 3 singulars were more accurate than the 3/5 consensus:

1. **Donnan equilibrium**: VDAC1 responds to OMM voltage, not ΔΨm directly.
   ΔΨm influences OMM voltage via Donnan equilibrium across the intermembrane space.
   This is correct per VDAC1 electrophysiology literature.

2. **Hexokinase-II hypothesis**: Circadian cycling of GSK3β/AKT drives rhythmic
   HK-II dissociation from VDAC1, creating a time-dependent vulnerability window.
   This survived full literature verification as GENUINELY NOVEL.

## The Novel Hypothesis

**"Circadian cycling of GSK3β/AKT activity drives rhythmic HK-II dissociation
from VDAC1, creating a time-dependent vulnerability window for CBD's
dose-dependent pathway switching."**

### Verified Components

| Component | Status | Source |
|-----------|--------|--------|
| GSK3β phosphorylates VDAC1 Thr51 → HK-II detachment | Confirmed | Pastorino 2005, PMID:16288047 |
| HK-II dissociation → VDAC1 oligomerization | Confirmed | Science Immunology 2023 |
| VDAC1 oligomerization → cytochrome c release | Confirmed | Shoshan-Barmatz 2010 |
| Circadian oscillation of AKT/GSK3β activity | Established | Multiple sources |
| HKI binds VDAC via membrane-buried glutamate | Confirmed | Nature Comms Bio 2025 |
| **Integration into chronopharmacology model** | **NO PRIOR WORK** | **Novel** |

### The Mechanism Chain

```
Circadian clock
  → BMAL1/CLOCK oscillation
    → AKT activity peaks (active phase)
      → GSK3β suppressed → HK-II bound to VDAC1 (protective)
    → AKT activity troughs (rest phase)
      → GSK3β active → VDAC1 Thr51 phosphorylated → HK-II dissociates
        → VDAC1 oligomerization-competent
          → CBD at VDAC1 → cytochrome c release → apoptosis
```

**Prediction**: CBD cytotoxicity IC50 should shift with circadian phase,
lower when GSK3β is active (HK-II dissociated) and higher when AKT is active
(HK-II bound, VDAC1 protected).

### Falsifiable By

1. CBD dose-response curves in circadian-synchronized cells at CT6 vs CT18
2. CBD-VDAC1 FRET signal ± HK-II overexpression across circadian timepoints
3. GSK3β inhibitor (CHIR-99021) abolishing circadian CBD IC50 shift

## Connection to Structural Isomorphism

This extends the two-pathway pattern:
- **CBD**: dose picks pathway, tissue determines outcome (via VDAC1)
- **Lithium**: dose picks pathway, tissue determines outcome (via GSK-3β)
- **THC**: dose picks pathway, tissue determines outcome (via CB1 occupancy)
- **CBD + circadian**: dose picks pathway, **TIME** determines outcome (via HK-II/VDAC1)

The circadian model adds a temporal dimension to the structural isomorphism.
GSK3β appears in both the lithium model (as the direct target) and the
circadian-CBD model (as the HK-II/VDAC1 regulator). This is convergence
across compounds via a shared kinase.

## Methodological Finding

This run produced the first evidence that IRIS Gate Evo TYPE 1 consensus can
be factually wrong due to shared training data biases across models. When all
models learn the same incorrect association (ΔΨm polarity → VDAC1 gating),
convergence amplifies the error rather than catching it.

**Proposed flag**: COUNTER-CONSENSUS SINGULAR — when a TYPE 3 claim directly
contradicts a TYPE 1 consensus, flag for human review. The singular may be
the correct one.
