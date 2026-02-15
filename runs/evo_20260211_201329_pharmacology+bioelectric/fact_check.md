# Fact-Check: Circadian-VDAC1 Run
**Session**: evo_20260211_201329_pharmacology+bioelectric
**Date**: 2026-02-11
**Verified by**: Anthony (human) + Claude.ai + PubMed/web literature search

## Summary

3/5 models converged on wrong VDAC1 gating polarity. S2 promoted it to TYPE 1.
Claude's singulars were more accurate than consensus. One genuinely novel
hypothesis survived full literature verification.

## Claim-by-Claim Verification

### 1. VDAC1 open at depolarized ΔΨm (TYPE 1, gemini/grok/mistral)
**VERDICT: WRONG**

Real VDAC1 electrophysiology: bell-curve gating, open at ~0 mV, closed at
potentials above ±30-40 mV on the OMM. Models confused inner membrane ΔΨm
(-160 to -180 mV) with the outer membrane voltage that actually gates VDAC1.

Sources:
- Frontiers Physiology 2025: https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2025.1666994/full
- Springer: Structure, gating and interactions of VDAC (2021): https://link.springer.com/article/10.1007/s00249-021-01515-7

### 2. Circadian ΔΨm via BMAL1 -> NAMPT -> NAD+ (Claude singular, TYPE 3)
**VERDICT: PARTIALLY REAL**

The pathway BMAL1/CLOCK -> NAMPT -> NAD+ -> SIRT3 -> mitochondrial acetylation
is well-established. ~38% of mitochondrial proteins oscillate with 24h periodicity.
The specific "15-20 mV amplitude" number is NOT in the literature — fabricated quantification.

Sources:
- Peek et al., Science 2013: https://www.science.org/doi/10.1126/science.1243417
- PMC 2024 circadian-mitochondria review: https://pmc.ncbi.nlm.nih.gov/articles/PMC11078072/

### 3. VDAC1 oligomerization -> cytochrome c release (TYPE 2, claude/grok)
**VERDICT: CONFIRMED**

VDAC1 oligomerizes upon apoptosis induction, forming pores large enough for
cytochrome c. Up to 20-fold increase in oligomerization. Contact sites at
beta-strands 1, 2, and 19 confirmed. Strongest claim in the run.

Sources:
- Shoshan-Barmatz et al., BBA 2010: https://www.sciencedirect.com/science/article/pii/S0005272810000939
- PMC: VDAC1 oligomerization and apoptosis: https://pmc.ncbi.nlm.nih.gov/articles/PMC3004265/

### 4. HK-II/VDAC1 dissociation via GSK3beta/AKT (Claude singular, TYPE 3)
**VERDICT: MECHANISM REAL, CIRCADIAN LINK NOVEL**

GSK3beta phosphorylates VDAC1 at Thr51, causing HK-II detachment (Pastorino 2005).
2025 structural paper resolved HKI-VDAC binding via charged membrane-buried glutamate.
HK dissociation promotes VDAC1 oligomerization (Science Immunology 2023).
NO PRIOR LITERATURE linking this to circadian rhythm. Genuinely novel hypothesis.

Sources:
- Pastorino et al. 2005 (PMID:16288047): https://pubmed.ncbi.nlm.nih.gov/16288047/
- Nature Comms Bio 2025 (structural): https://www.nature.com/articles/s42003-025-07551-9
- Science Immunology 2023 (HK dissociation -> oligomerization): https://www.science.org/doi/10.1126/sciimmunol.ade7652

### 5. VDAC1 N-terminal alpha-helix voltage sensor (Mistral singular, TYPE 3)
**VERDICT: STRUCTURE REAL, POLARITY WRONG**

N-terminal alpha-helix confirmed as gating element. But mistral's claim that
"P_open peaks at -170 mV" contradicts established bell-curve gating at ~0 mV.
Same ΔΨm/OMM voltage confusion as Claim 1.

## Novel Hypothesis (Survived Verification)

"Circadian cycling of GSK3beta/AKT activity drives rhythmic HK-II dissociation
from VDAC1, creating a time-dependent vulnerability window for CBD's
dose-dependent pathway switching."

Components verified independently:
- GSK3beta/AKT phosphorylation of VDAC1 -> HK-II dissociation (confirmed)
- HK-II dissociation -> VDAC1 oligomerization (confirmed)
- VDAC1 oligomerization -> cytochrome c release (confirmed)
- Circadian oscillation of AKT/GSK3beta activity (established in literature)
- Integration of all four into a chronopharmacology model: NO PRIOR WORK

## Methodological Implications

1. TYPE 1 consensus can be WRONG when models share training data biases
2. Singulars (TYPE 3) can outperform consensus on accuracy
3. Need: COUNTER-CONSENSUS SINGULAR flag for pipeline
4. Human verification layer is non-negotiable for publishing
