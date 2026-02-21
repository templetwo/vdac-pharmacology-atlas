# Undergraduate Research Proposal
## Does Venetoclax Activate Innate Immunity Before It Kills Cancer Cells?
### A Mechanistic Test in AML Cell Lines

**Proposed by**: Anthony J. Vasquez Sr.
**Date**: February 2026
**Relevant preprint**: bioRxiv submission pending DOI — github.com/templetwo/vdac-pharmacology-atlas

---

## The Question

Venetoclax (ABT-199) is an FDA-approved drug for acute myeloid leukemia (AML).
The standard explanation for how it works: it inhibits BCL-2/Bcl-xL, releasing
the apoptotic brake, and the cancer cell dies.

This proposal tests a different — and potentially additional — mechanism.

**Hypothesis**: Before venetoclax kills AML cells, it displaces Bcl-xL from the
VDAC1 channel on the outer mitochondrial membrane. This displacement triggers
VDAC1 oligomerization, which releases mitochondrial DNA (mtDNA) into the
cytoplasm. The cell's innate immune sensor (cGAS-STING) detects this mtDNA and
fires an alarm signal — before the cell is dead.

If this is true, venetoclax is not just an apoptosis drug. It may also be an
innate immune activator. That would be a new, unreported mechanism for a drug
already in clinical use.

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

At each time point, three measurements in parallel:

| Measurement | What It Tells Us | Method | Equipment |
|---|---|---|---|
| Cytosolic mtDNA | Is mtDNA leaking from mitochondria? | Cell fractionation + qPCR | qPCR machine |
| IFN-β secretion | Is cGAS-STING alarm firing? | ELISA on cell supernatant | Plate reader |
| Caspase-3 activity | Is the cell dying? | Colorimetric assay | Plate reader |

**Positive result**: mtDNA appears in cytosol and IFN-β rises at early time
points (2-4h), while caspase-3 activation occurs later (8-12h).

**Negative result**: caspase-3 fires at the same time or before mtDNA/IFN-β.
This would mean the standard apoptosis explanation is sufficient and complete.

Either result advances knowledge.

---

## Cell Line

**THP-1** (ATCC TIB-202) — human AML monocytic cell line. Suspension culture.
Available from ATCC. Requires BSL-2 cell culture conditions. Well-characterized
and widely used for AML mechanistic studies.

Alternatively: **HL-60** (ATCC CCL-240) — also suspension, also widely available.

---

## Controls

- **Vehicle control**: DMSO at matched concentration (no venetoclax)
- **Positive apoptosis control**: Staurosporine (known apoptosis inducer)
- **VDAC1-KO control** (optional, if CRISPR available): removes the specific
  mechanism and should abolish early mtDNA release if the hypothesis is correct

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
| qPCR primers (mtDNA: Cyt b or D-loop; nuclear: GAPDH) | IDT or Sigma | ~$100 |
| Standard culture media (RPMI + FBS), consumables | Lab stock | ~$100–200 |
| **Total** | | **~$1,200–1,500** |

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
