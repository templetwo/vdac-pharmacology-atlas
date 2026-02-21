# Undergraduate Research Proposal
## Venetoclax as a Dual-Action Agent: Apoptosis and Innate Immune Activation via VDAC1 Gate-Opening
### Temporal Decoupling of mtDNA Release and Cell Death in AML Cell Lines

**Proposed by**: Anthony J. Vasquez Sr.
**Date**: February 2026
**Relevant preprint**: bioRxiv submission pending DOI — github.com/templetwo/vdac-pharmacology-atlas

---

## The Question

Venetoclax (ABT-199) is an FDA-approved drug for acute myeloid leukemia (AML).
The standard explanation for how it works: it inhibits BCL-2/Bcl-xL, releasing
the apoptotic brake, and the cancer cell dies.

This proposal tests a different — and potentially additional — mechanism.

**Hypothesis**: Venetoclax acts through two temporally distinct mechanisms.
First, it displaces Bcl-xL from the VDAC1 channel on the outer mitochondrial
membrane, triggering VDAC1 oligomerization and mtDNA release into the cytoplasm.
The innate immune sensor cGAS-STING detects this mtDNA and fires an alarm signal.
Second — and only afterward — canonical apoptosis (caspase activation, cell death)
follows.

If this temporal decoupling is real, venetoclax is not just an apoptosis drug.
It is a dual-action agent: an innate immune activator first, a cancer cell killer
second. That sequence is unreported and would reframe how the drug is understood
— and how it might be combined with checkpoint inhibitors.

---

## Why It Matters

The cGAS-STING pathway is the same pathway that checkpoint inhibitors (anti-PD-1,
anti-PD-L1) need to function. If venetoclax activates cGAS-STING before killing
cancer cells, then venetoclax + checkpoint inhibitor combinations might have
synergistic potential in AML — the innate alarm recruits T cells; the checkpoint
inhibitor amplifies them.

This connects to published work showing that mtDNA release activates cGAS-STING
(Rongvaux et al., Cell 2014; McArthur et al., Science 2018) and to the
VDAC1-Bcl-xL structural interaction (Shimizu et al., Nature Cell Biology 1999;
Arbel et al., EMBO Journal 2012).

---

## What We Would Measure

The experiment has one central design: treat AML cells with venetoclax and
measure the SEQUENCE of events — does innate signaling fire BEFORE or AFTER
cell death?

**Timeline**: venetoclax treatment at t=0, collect cells at t=2h, 4h, 8h, 12h, 24h.

Two parallel treatment arms run simultaneously:

**Arm A — Venetoclax alone** (standard condition)
**Arm B — Venetoclax + z-VAD-FMK** (pan-caspase inhibitor, 50 µM)

z-VAD-FMK blocks caspase-3 and caspase-7, which — once activated — physically
cleave cGAS and IRF3, destroying the innate immune sensor (Rongvaux et al. 2014).
Without this inhibitor, even if the gate opens and the alarm fires, dying caspases
may degrade the signal before we can measure it. Adding Arm B gives a clean window:
the gate can open, mtDNA can flood the cytosol, and the immune signal has nothing
suppressing it. If the hypothesis is correct, Arm B should show a dramatically
amplified and earlier IFN-β signal than Arm A.

At each time point, three measurements in both arms:

| Measurement | What It Tells Us | Method | Equipment |
|---|---|---|---|
| Cytosolic mtDNA | Is mtDNA leaking from mitochondria? | Cell fractionation + qPCR | qPCR machine |
| IFN-β secretion | Is cGAS-STING alarm firing? | ELISA on cell supernatant | Plate reader |
| Caspase-3 activity | Is the cell dying? | Colorimetric assay | Plate reader |

**Positive result**: In Arm A, mtDNA and IFN-β rise at 2-4h, caspase-3 follows
at 8-12h. In Arm B, IFN-β signal is larger and earlier with caspase-3 suppressed.

**Negative result**: caspase-3 fires simultaneously with or before mtDNA/IFN-β
in both arms. Standard apoptosis explanation is complete.

Either result advances knowledge.

---

## Cell Line

**THP-1** (ATCC TIB-202) — human AML monocytic cell line. Suspension culture.
Well-characterized for cGAS-STING signaling studies. Intact STING pathway.
Primary cell line for this experiment.

**Backup: U937** (ATCC CRL-1593.2) — human myeloid leukemia cell line,
suspension culture, intact STING pathway. If THP-1 is unavailable, U937
is the appropriate backup.

**Important**: HL-60 (sometimes listed as an AML alternative) is STING-deficient
and must not be used as a backup for this experiment. If HL-60 were substituted
and IFN-β was undetectable, the result would be uninterpretable — the sensor
would be absent, not the signal.

---

## Controls

- **Vehicle control**: DMSO at matched concentration (no venetoclax)
- **Positive apoptosis control**: Staurosporine (known apoptosis inducer)
- **z-VAD-FMK alone**: Confirms the inhibitor has no baseline effect on IFN-β
- **VDAC1-KO control** (optional, if CRISPR available): should abolish early
  mtDNA release if the gate-opening mechanism is specific

---

## Equipment Required

| Item | Available at DVU? |
|---|---|
| BSL-2 cell culture hood + incubator | **Confirm with lab** |
| qPCR machine | **Confirm with lab** |
| Plate reader (absorbance + fluorescence) | **Confirm with lab** |
| Centrifuge (for cell fractionation) | Likely yes |
| Standard micropipettes, tubes, consumables | Yes |

---

## Reagents and Estimated Cost

| Reagent | Source | Estimated Cost |
|---|---|---|
| Venetoclax (ABT-199), research grade | Selleck Chemicals (S8048) | ~$150 |
| THP-1 cell line | ATCC or lab gift | ~$300 or free from collaborator |
| Cytoplasmic/mitochondrial fractionation kit | Abcam ab65320 or Thermo 89874 | ~$200 |
| Human IFN-β ELISA kit | Invivogen or R&D Systems | ~$350 |
| Caspase-3 colorimetric assay kit | Abcam ab39401 | ~$150 |
| z-VAD-FMK (pan-caspase inhibitor) | Selleck Chemicals (S7023) | ~$100 |
| qPCR primers (mtDNA: Cyt b or D-loop; nuclear: GAPDH) | IDT or Sigma | ~$100 |
| Standard culture media (RPMI + FBS), consumables | Lab stock | ~$100–200 |
| **Total** | | **~$1,400–1,700** |

---

## Timeline

| Week | Activity |
|---|---|
| 1–2 | Acquire cells, expand culture, confirm viability |
| 3 | Dose-response curve: find venetoclax IC50 in THP-1 |
| 4–5 | Time-course experiment: 5 time points × 3 measurements |
| 6 | Repeat experiment (biological replicate) |
| 7–8 | Data analysis, figures, interpretation |

**Total: ~8 weeks from cell arrival to data.**

---

## What Success Looks Like

A positive result — mtDNA in cytosol and IFN-β secretion preceding caspase
activation — would be a novel mechanistic finding for venetoclax. It would:

1. Support submission of a short communication to a peer-reviewed journal
   (e.g., *Cancer Letters*, *Biochemical and Biophysical Research Communications*)
2. Provide direct experimental evidence for the gate-jamming framework
   developed in the accompanying preprint
3. Support a grant application (undergraduate research grant, NIH AREA,
   or institutional funds) for a larger follow-up study
4. Be a concrete finding to bring to a collaborating AML lab or clinical center

A negative result is equally publishable as a mechanistic constraint.

---

## Anticipated Confound: TREX1

THP-1 cells express TREX1 — a cytosolic DNA exonuclease that degrades
single-stranded DNA fragments, including mtDNA. This is directly relevant:
our transcriptomic analysis (S2, COADREAD MSS cohort) showed that TREX1
expression rises in lockstep with high gate-jamming scores (rho = +0.315,
p_bonf = 7×10⁻⁵), suggesting that tumors deploy TREX1 as a secondary guard
to degrade any mtDNA that leaks past VDAC1 gate-jamming.

In this experiment, TREX1 could produce the following pattern: cytosolic
mtDNA appears briefly at 2h (gate opens, mtDNA leaks), then disappears by
4h (TREX1 degrades it), and IFN-β rises only weakly or later than predicted.

If this pattern appears, it is not a failed experiment. It is the S2
discovery manifesting in vitro — the same belt-and-suspenders evasion
identified computationally now visible at the cellular level. The discussion
section should address this pattern explicitly if observed, and flag TREX1
inhibition as the logical next condition to test.

---

## Literature Basis

- Rongvaux A et al. Apoptotic caspases prevent the induction of type I interferons
  by mitochondrial DNA. *Cell* 2014;159:1563-1577.
- McArthur K et al. BAK/BAX macropores facilitate mitochondrial herniation and
  mtDNA efflux during apoptosis. *Science* 2018;359:eaao6047.
- Shimizu S et al. Bcl-2 family proteins regulate the release of apoptogenic
  cytochrome c by the mitochondrial channel VDAC. *Nature* 1999;399:483-487.
- Arbel N et al. VDAC1 as a mediator of the anti-apoptotic activity of Bcl-xL.
  *EMBO J* 2012;31:1980-1992.
- DiNardo CD et al. Venetoclax combined with decitabine or azacitidine in
  treatment-naive AML. *NEJM* 2020;383:617-629.
