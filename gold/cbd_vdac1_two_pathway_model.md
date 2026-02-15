# CBD/VDAC1 Two-Pathway Model: Gold Extraction

**Source runs**: `evo_20260210_222428_pharmacology+bioelectric` + `evo_20260210_224206_pharmacology+bioelectric`
**Extraction date**: 2026-02-11
**S3 outcome**: Both PASSED (cosine 0.908, TYPE 0/1 82.35%)
**Question**: "What are the mechanisms by which CBD induces selective cytotoxicity in cancer cells while sparing healthy cells, with specific reference to VDAC1-mediated mitochondrial membrane potential disruption?"

## Core Model

CBD selectivity is governed by **mitochondrial membrane potential (psi_m) acting as a voltage-dependent switch on VDAC1 gating state**. Cancer cells (-120 mV) present VDAC1 in an open conformation favorable for CBD binding; healthy cells (-180 mV) gate VDAC1 closed, resisting CBD-induced conformational shift.

This is the founding two-pathway model that established the structural isomorphism pattern.

## Multi-Model Convergent Claims

### TYPE 0 (5/5 models agree)
- VDAC1 voltage-dependent gating is the primary selectivity switch
- CBD binding (Kd=11 uM) favors long-lived open state at cancer psi_m
- Healthy cells' hyperpolarized psi_m stabilizes VDAC1 in low-conductance closed state

### TYPE 1 (3-4/5 models agree)
- **ROS amplification cascade**: CBD triggers ROS beyond lethal threshold (~0.8-0.9 rel) in cancer cells (baseline 0.45 rel), unreachable in healthy cells (baseline 0.08 rel)
- **TRPV1/2 synergy**: Ca2+ influx via TRPV1/2 (Kd=2-3.7 uM, engages first) pre-loads cells; cancer cells with impaired Ca2+ buffering accumulate mitochondrial Ca2+ via VDAC1/MCU
- **Lethal positive feedback loop**: VDAC1 disruption + TRPV1/2 Ca2+ overload + elevated ROS triggers mPTP opening = irreversible psi_m collapse

### Two Pathways

| Property | Cancer Cell (-120 mV) | Healthy Cell (-180 mV) |
|----------|----------------------|----------------------|
| VDAC1 state | Open, CBD-accessible | Closed, CBD-resistant |
| CBD binding effect | Locks pathological open state | Minimal functional impact |
| ADP/ATP exchange | Blocked -> ETC stalls | Maintained |
| ROS trajectory | 0.45 -> >0.8 rel (lethal) | 0.08 -> ~0.2 rel (buffered) |
| Ca2+ handling | Overload -> mPTP opening | Buffered by SERCA/MCU |
| Outcome | Apoptosis | Spared |

## Hypotheses Generated (S4)

**H1**: VDAC1 open-state probability increases >=3-fold at -120 mV + 11 uM CBD but <1.3-fold at -180 mV
- Test: Patch-clamp on reconstituted VDAC1 in planar lipid bilayers at clamped voltages

**H2**: Cancer cells (MDA-MB-231) show MitoSOX >0.8 rel within 4h of 15 uM CBD; NAC (5 mM) rescues viability to >75%
- Test: Flow cytometry MitoSOX + Annexin V/PI at 24h, +/- NAC

**H3**: Pre-depolarizing healthy cells (MCF-10A) from -180 mV to -120 mV sensitizes them to CBD killing
- Test: FCCP pre-treatment + CBD dose-response, comparing to cancer cell sensitivity

## Lab Gate Result
18/18 claims passed (falsifiable + feasible + novel). Zero rejections.

## Key Parameters
- VDAC1 Kd for CBD: 11 uM
- TRPV1 Kd/EC50: 2-3.7 uM
- Cancer psi_m: -120 mV
- Healthy psi_m: -180 mV
- Cancer baseline ROS: 0.45 rel
- Healthy baseline ROS: 0.08 rel
- Lethal ROS threshold: ~0.8-0.9 rel

## Pipeline Stats
- Total LLM calls: 17
- S3 passed cycle 2 (cosine 0.908, TYPE 0/1 82.35%)
- Reproducible: second run (evo_20260210_224206) also S3 PASSED
