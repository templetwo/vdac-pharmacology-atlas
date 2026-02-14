# VDAC Pharmacology Atlas

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Status: Active Research](https://img.shields.io/badge/Status-Active%20Research-green.svg)]()

**An open-access map of the voltage-dependent anion channel as a druggable decision gate.**

Anthony J. Vasquez Sr. — Delaware Valley University

---

## Why This Exists

The voltage-dependent anion channel (VDAC) sits at the most consequential
decision point in cell biology: whether a cell lives or dies. It controls
metabolite flux across the outer mitochondrial membrane, gates cytochrome c
release, and serves as a docking platform for hexokinase-II, Bcl-2 family
proteins, and tubulin.

Multiple drugs interact with VDAC — CBD, erastin, DIDS, olesoxime — but no
systematic pharmacology exists. There is no binding site atlas, no isoform
selectivity map, no unified drugability assessment.

This project builds that map.

## Origin

This atlas grew from the [CBD Two-Pathway Model](https://github.com/templetwo/cbd-two-pathway-model),
where multi-model convergence analysis ([IRIS Gate Evo](https://github.com/templetwo/iris-gate-evo))
revealed that CBD is a universal mitochondrial stressor acting through VDAC1/2,
with outcomes determined by cellular metabolic reserve rather than molecular
selectivity. The finding generalized: if VDAC is the decision gate, then
understanding its pharmacology helps everyone, not just CBD researchers.

## What's Here

```
vdac-pharmacology-atlas/
├── README.md
├── data/
│   ├── vdac_modulators.csv              # Known VDAC-interacting compounds
│   ├── vdac_isoform_comparison.csv      # VDAC1 vs VDAC2 vs VDAC3 features
│   └── resilience_biomarker_framework.md # Generalized vulnerability prediction
├── iris_runs/
│   └── run_queue.md                     # Pre-written IRIS Gate Evo questions
├── figures/                             # Generated from IRIS run data
└── paper/
    └── manuscript.md                    # Six-layer atlas manuscript
```

### The Modulator Database

`data/vdac_modulators.csv` contains 17 compounds/proteins with known VDAC
interactions, including:

| Compound | Target | Mechanism | Context |
|----------|--------|-----------|---------|
| CBD | VDAC1/2 | Allosteric gating | Cancer / neuroprotection |
| Erastin | VDAC2/3 | Opens channel | Ferroptosis / cancer |
| VBIT-4 | VDAC1 | Prevents oligomerization | Neuroprotection |
| Hexokinase-II | VDAC1 | Pore capping | Warburg effect |
| Olesoxime | VDAC1 | Cholesterol-motif binding | ALS (clinical trials) |

Each entry includes Kd/IC50 (where published), mechanism of action, isoform
preference, therapeutic context, and citation status.

### The Resilience Biomarker Framework

A generalized prediction model: vulnerability to ANY VDAC-engaging compound
can be predicted by a common biomarker panel (GSH/GSSG ratio, synthesis rate,
ATP/ADP). Validated by two independent IRIS Gate Evo pipeline passes on the
CBD model. Applicable across the VDAC drug class including erastin, VBIT-4,
valproate, and acetaminophen.

### The Manuscript

`paper/manuscript.md` is a six-layer portrait of VDAC1 synthesized from 20 IRIS runs:

1. **The Protein** — 19-strand barrel, five molecular machines, parallel seam life/death switch
2. **The Gate** — Three nested threshold signals, cofactor equation, VDAC1 as external audit
3. **The Atlas** — 6 dedicated runs, 22 novel findings, 24 operationalized hypotheses
4. **The Disease** — Cancer as lost coherence, Warburg effect as gate-jamming cost
5. **The Method** — IRIS multi-LLM convergence protocol, what it can and cannot establish
6. **The Frame** — Threshold logic from protein to organism, sovereignty through coherence

### IRIS Runs Completed

All five queued runs plus a sixth (membrane architecture) have been completed:

| Run | Question | S3 | Key Finding |
|-----|----------|----|-------------|
| 1 | Isoform selectivity & binding architecture | PASSED | Three non-overlapping binding sites, VDAC2 11-residue extension = selectivity |
| 2 | Cofactor decision landscape | PASSED | Cofactor equation: `Threshold = K / [(1-f_HKII)(1-f_BclxL)] * (Chol/CL)` |
| 3 | Membrane lipid modulation | PASSED | Cancer cholesterol lowers CBD Kd from 11 to 3-6 uM (cosine 0.9512) |
| 4 | Biomarker platform | PASSED | GSH/GSSG ratio predicts hepatotoxicity; mitochondrial panel is pharmacodynamic only |
| 5 | Hidden drug interactions | PASSED | VPA opens VDAC, NAPQI closes it — opposite gating, both hepatotoxic (cosine 0.9547) |
| 6 | Membrane architecture | PASSED | Honeycomb lattice as structural gate; CBD may be membrane chaotrope (cosine 0.9047) |

**Corpus**: 139 claims, 22 novel findings, 24 hypotheses, mean testability 7.2/10. Total cost: ~$15.

## How to Contribute

This is open science. If you have:
- **Published VDAC binding data** we're missing: open an issue or PR to `data/vdac_modulators.csv`
- **Experimental capacity** to test a hypothesis: see `iris_runs/run_queue.md` for open questions
- **Clinical datasets** with both VDAC-modulating drug exposure and hepatic biomarkers: contact us

## Related Projects

| Project | Link | Relationship |
|---------|------|-------------|
| CBD Two-Pathway Model | [github.com/templetwo/cbd-two-pathway-model](https://github.com/templetwo/cbd-two-pathway-model) | Proof of concept — CBD as VDAC stress test |
| IRIS Gate Evo | [github.com/templetwo/iris-gate-evo](https://github.com/templetwo/iris-gate-evo) | Convergence engine — multi-model validation |
| IRIS Evo Findings | [github.com/templetwo/iris-evo-findings](https://github.com/templetwo/iris-evo-findings) | Run data, gold extraction, cross-run analysis |
| OSF Archive | [osf.io/nuxhv](https://osf.io/nuxhv/) | Preprint, datasets, protocol packages |

## License

CC BY 4.0. Use it, build on it, cite it.

## Citation

```bibtex
@misc{vasquez2026vdac,
  title={The VDAC1 Pharmacology Atlas: A Multi-LLM Convergence Portrait of Life's Decision Gate},
  author={Vasquez, Anthony J., Sr.},
  year={2026},
  url={https://github.com/templetwo/vdac-pharmacology-atlas}
}
```
