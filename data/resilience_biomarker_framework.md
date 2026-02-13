# The Resilience Biomarker Framework

## Core Principle

VDAC modulation is a universal mitochondrial stressor. The outcome — survival vs
death — is not determined by the drug, but by the patient's metabolic reserve.

This means vulnerability to ANY VDAC-engaging compound can be predicted by a
common set of biomarkers. The framework generalizes from CBD-specific findings
to the entire VDAC drug class.

## The Biomarker Panel

### Tier 1: Validated by IRIS Gate Evo (2 independent pipeline passes)

| Biomarker | What It Measures | Threshold | Source |
|-----------|-----------------|-----------|--------|
| GSH/GSSG ratio | Antioxidant reserve capacity | >20 uM intracellular = safe zone | EFSA run TYPE 0 (4/5) |
| GSH synthesis rate | Regeneration capacity | >0.5 umol/g/hr = healthy | Chronic run TYPE 0 (4/5) |
| ALT/GGT | Hepatocyte damage (proxy for reserve) | Elevated = compromised | Standard clinical |

### Tier 2: Predicted, Awaiting Experimental Validation

| Biomarker | What It Measures | Rationale |
|-----------|-----------------|-----------|
| ATP/ADP ratio | Mitochondrial functional reserve | Mistral dissent: ATP deficit may compound independently |
| VDAC1 expression (tumor biopsy) | Target density | Higher VDAC1 = more sensitive to modulators |
| MitoSOX / TMRM | Baseline mitochondrial ROS / membrane potential | Direct measure of mitochondrial health |
| Hepatic CBD/7-OH-CBD ratio | Metabolite accumulation | 7-OH-CBD Kd unknown; high ratio = wider occupancy window |

### Tier 3: Proposed for Future Research

| Biomarker | What It Measures | Rationale |
|-----------|-----------------|-----------|
| HK-II-VDAC1 occupancy | Cofactor landscape state | HK-II displacement may be the actual death signal |
| Cardiolipin content (OMM) | Membrane environment | May modulate effective Kd of lipophilic VDAC modulators |
| Circulating mtDNA | Mitochondrial damage marker | Chronic low-grade damage not captured by ALT |

## Risk Stratification Model

```
IF GSH/GSSG > threshold AND GSH synthesis rate > 0.5 umol/g/hr AND ALT normal:
    -> LOW RISK: Standard dosing appropriate
    -> Safety margin: 5-10x (IRIS TYPE 1, 3/5)

IF GSH/GSSG < threshold OR GSH synthesis reduced >2x OR ALT elevated:
    -> HIGH RISK: Conservative dosing or contraindication
    -> Safety margin: 2-3x (IRIS TYPE 1, 3/5)
    -> Consider NAC co-administration (H3 from EFSA run, testability 7/10)
```

## Applicability Across VDAC Drug Class

This framework applies to any compound that engages VDAC:

| Drug | Current Context | VDAC Relevance | Biomarker Applicability |
|------|----------------|----------------|------------------------|
| CBD | Epilepsy, cancer, wellness | Direct VDAC1/2 modulator | Full panel |
| Erastin | Cancer (ferroptosis) | VDAC2/3 opener | GSH + VDAC1 expression |
| VBIT-4 | Neuroprotection (preclinical) | VDAC1 oligomerization blocker | GSH + ATP/ADP |
| Valproate | Epilepsy, bipolar | Suspected mitochondrial effects | GSH + ALT (already monitored) |
| Acetaminophen | Pain/fever | NAPQI damages mitochondria | GSH (NAC already standard rescue) |

## The NAC Connection

N-acetylcysteine (NAC) is already the standard treatment for acetaminophen
overdose — precisely because it replenishes GSH. The Resilience Framework
predicts that NAC co-administration would rescue vulnerability to ANY
VDAC-engaging compound, not just acetaminophen.

This is testable: H3 from the EFSA run (testability 7/10) proposes exactly
this experiment for CBD. If confirmed, NAC becomes a universal "VDAC safety
net" across the drug class.
