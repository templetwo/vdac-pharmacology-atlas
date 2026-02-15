# Lithium Two-Pathway Model: Gold Extraction

**Source run**: `evo_20260210_231236_pharmacology`
**Extraction date**: 2026-02-11
**S3 outcome**: PASSED (cosine 0.917, TYPE 0/1 94.74%)
**Question**: "What mechanisms explain why low-dose lithium is neuroprotective while therapeutic-dose lithium causes nephrotoxicity, and what molecular targets determine the dose-dependent switch between cytoprotection and organ toxicity?"

## Core Model

The dose-dependent switch is a **tissue-[Li+] phenomenon**. Renal collecting duct cells concentrate lithium 3-4x above serum via ENaC, reaching locally toxic levels (>2 mM) that fully inhibit IMPase and GSK-3beta. Brain lithium remains sub-toxic (~0.4-0.6 mM) due to BBB efflux, achieving only partial GSK-3beta inhibition (10-25%) which activates neuroprotective pathways.

## Multi-Model Convergent Claims

### TYPE 0 (5/5 models agree)
- **Pharmacokinetic partitioning**: Renal ENaC concentrates Li+ to 2-4 mM; brain stays at 0.4-0.6 mM
- **PINK1/Parkin mitophagy**: Rate-limiting for mitochondrial quality control in both neurons and beta-cells

### TYPE 1 (3-4/5 models agree)
- **GSK-3beta partial inhibition = neuroprotection**: 10-25% inhibition at brain [Li+] ~0.3-0.6 mM activates Nrf2/ARE antioxidant genes + stabilizes beta-catenin for BDNF/Wnt survival signaling
- **IMPase inhibition = nephrotoxicity driver**: >70% inhibition at renal [Li+] >2 mM depletes free inositol, disrupting PI(4,5)P2-dependent AQP2 trafficking -> nephrogenic diabetes insipidus
- **Dual-target engagement at high [Li+]**: IMPase (inositol depletion) + GSK-3beta (>50% inhibition -> aberrant Wnt/beta-catenin -> fibrosis) synergize for renal toxicity

### TYPE 2 (2/5 models)
- **GSK-3beta biphasic effect**: 10-30% inhibition = neuroprotective; >50% = dysregulates glycogen metabolism + beta-catenin proliferation -> fibrosis
- **Complex I binding**: High renal [Li+] inhibits mitochondrial Complex I (ND2/4 subunits), exacerbating toxicity via ROS beyond IMPase/GSK-3beta

### Two Pathways

| Property | Brain (0.3-0.6 mM Li+) | Kidney (2-4 mM Li+) |
|----------|------------------------|---------------------|
| GSK-3beta inhibition | 10-25% (partial) | >50% (near-complete) |
| IMPase inhibition | <15% (negligible) | >70% (saturating) |
| Nrf2/ARE activation | Active -> antioxidant defense | Overwhelmed |
| Wnt/beta-catenin | Stabilized -> BDNF, survival | Dysregulated -> fibrosis |
| Inositol pools | Intact | Depleted -> AQP2 trafficking failure |
| Outcome | Neuroprotection | NDI + interstitial fibrosis |

## Hypotheses with Monte Carlo (S5)

**H1**: ENaC-mediated Li+ accumulation (d=1.17, power=1.0)
- Renal cells show intracellular [Li+] 2.5-4.0x extracellular at steady state
- ENaC-knockout/amiloride-blocked cells show ratios <1.5x
- Parameters: renal Li ratio (2.0-4.5), amiloride IC50 (0.1-1.0 uM)

**H2**: IMPase-driven AQP2 trafficking failure (d=1.06, power=1.0)
- [Li+] >2 mM reduces AQP2 apical membrane insertion >50% within 48h
- Myo-inositol (10 mM) rescues to >75% baseline
- Parameters: IMPase Ki (0.5-1.2 mM), AQP2 reduction (40-80%)

**H3**: GSK-3beta/Nrf2 neuroprotection (d=1.06, power=1.0)
- 0.3 mM Li+ decreases GSK-3beta 15-25%, increases Nrf2 >2-fold, improves glutamate survival >30%
- GSK-3beta-S9A mutant neurons show NO protection; Nrf2-/- neurons >50% attenuation
- Parameters: GSK3B Ki (1.2-2.5 mM), Nrf2 fold induction (1.5-4.0)

**H4**: GSK-3beta/beta-catenin renal fibrosis (d=0.85, power=1.0)
- 3 mM Li+ -> >50% GSK-3beta inhibition -> >5-fold TOPFlash, >3-fold fibrotic markers within 72h
- 0.3 mM Li+ shows <2-fold TOPFlash and no fibrotic induction
- Parameters: GSK3B inhibition at 3mM (50-75%), fibrotic marker fold (2-6x)

## Lab Gate Result
12/19 claims passed. 7 filtered:
- 3 claims about Mg2+ competition: "lacks novelty" (well-established mechanism)
- 2 claims about Ki-based molecular switch: "not feasible" (requires in vivo measurement of multiple simultaneous Ki values)
- 2 additional Mg2+ displacement variants

## Key Parameters
- GSK-3beta Ki: ~1.5-2.0 mM
- IMPase Ki: ~0.8 mM
- Brain [Li+]: 0.4-0.6x serum
- Renal [Li+]: 3-4x serum (via ENaC)
- Therapeutic serum: 0.8-1.2 mM
- Neuroprotective threshold: ~10% GSK-3beta inhibition
- Nephrotoxic threshold: ~2 mM local [Li+]

## Pipeline Stats
- Total LLM calls: 11
- S3 passed cycle 3 (cosine 0.917, TYPE 0/1 94.74%)
- All 4 hypotheses: Cohen's d 0.85-1.17, power 1.0
- 1200 total Monte Carlo iterations
