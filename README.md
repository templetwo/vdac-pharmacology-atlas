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
└── paper/                               # Atlas manuscript (in progress)
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

### The IRIS Run Queue

Five pre-written research questions ready for multi-model convergence analysis:

1. **Isoform selectivity & binding site architecture** — Can we design VDAC2-sparing compounds?
2. **The cofactor decision landscape** — HK-II, Bcl-xL, tubulin: who controls the gate?
3. **Membrane lipid modulation** — Can lipid engineering restore selectivity?
4. **Biomarker platform** — Can a blood panel predict VDAC drug vulnerability?
5. **Hidden VDAC interactions** — Which common drugs hit VDAC without anyone knowing?

Estimated total budget: ~$2.50-5.00 via IRIS Gate Evo.

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
  title={VDAC Pharmacology Atlas: Mapping the Mitochondrial Decision Gate},
  author={Vasquez, Anthony J., Sr.},
  year={2026},
  url={https://github.com/templetwo/vdac-pharmacology-atlas}
}
```
