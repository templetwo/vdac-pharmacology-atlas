# Outreach Email Templates — VDAC1 Pharmacology Atlas

---

## Email 1: Devinsky Group (NYU Langone) — VPA+CBD Pharmacovigilance

**Subject:** Untested mitochondrial mechanism in VPA+CBD hepatotoxicity — open data, testable protocol

Dear Dr. Devinsky,

I am an undergraduate researcher at Delaware Valley University writing to share a pharmacovigilance analysis that may be relevant to your work on cannabidiol in Dravet syndrome.

Up to 30% of patients co-prescribed VPA and CBD develop ALT elevations >3x ULN. The standard CYP450 explanation is problematic: CBD actually *decreases* VPA and 4-ene-VPA plasma levels (Gaston et al. 2017), which should reduce hepatotoxicity, not increase it. No publication we have found connects the two well-documented sides of this problem.

We propose a mitochondrial convergence mechanism. VPA depletes mitochondrial reserves (carnitine, CoA, glutathione) while CBD alters VDAC1 conductance and outer membrane permeability. Neither drug alone crosses the hepatotoxicity threshold in most patients. Together, they may.

An estimated 2,000-3,500 US pediatric patients are currently affected by this interaction. Our analysis suggests three concrete next steps:

1. **Clinical (low-cost):** Measure GDF15 and FGF21 in patients with existing ALT elevations — these mitochondrial stress biomarkers would distinguish metabolic from idiosyncratic injury.
2. **In vitro:** Test whether VPA-pretreated hepatocytes show increased sensitivity to CBD at clinically relevant concentrations.
3. **Mechanistic:** Test whether VDAC1 conductance inhibition (e.g., DIDS) is protective in the dual-exposure model.

The full analysis, including a detailed alert document and supporting data, is openly available:

- Preprint: [doi.org/10.1101/2026.02.16.706165](https://doi.org/10.1101/2026.02.16.706165)
- Alert document: [github.com/templetwo/vdac-pharmacology-atlas/blob/main/paper/vpa_cbd_hepatotoxicity_alert.md](https://github.com/templetwo/vdac-pharmacology-atlas/blob/main/paper/vpa_cbd_hepatotoxicity_alert.md)

I should be transparent: this work is computational and AI-assisted, not experimentally validated. The hypothesis is falsifiable and the protocols are specified. I would welcome any feedback, including reasons this mechanism has already been considered and ruled out.

Respectfully,

Anthony J. Vasquez Sr.
Delaware Valley University
vasquezaj3921@delval.edu

---

## Email 2: VDAC1 Bench Scientists (Template for Multiple Labs)

**Subject:** Operationalized VDAC1 hypotheses with falsifiable predictions — open dataset, looking for experimental collaborators

Dear Dr. [NAME],

I am an undergraduate researcher at Delaware Valley University. I have assembled a pharmacology atlas of VDAC1 gating behavior using structured multi-LLM convergence analysis, and I am writing because your lab's work on [SPECIFIC TOPIC] directly addresses several predictions the model generates.

The central quantitative output is a **Gate-Jamming Score**:

GJS = f(HK-II) x 0.4 + f(Bcl-xL) x 0.3 + [Cholesterol]/[Cardiolipin] x 0.3

GJS predicts immune-cold tumor status by quantifying how thoroughly VDAC1's normal conductance switching is suppressed. Two predictions your lab could test:

1. **HK-II displacement from VDAC1 should activate cGAS-STING** via mtDNA release through restored conductance. This is testable with clotrimazole or methyl jasmonate in high-GJS cell lines, measuring cytosolic mtDNA and IFN-beta within 24 hours. (Testability: 9/10 — reagents are standard, readouts are established.)

2. **Gate restoration + anti-PD-1 should show synergy** specifically in immune-cold (high-GJS) tumors, converting them to inflamed phenotypes. Syngeneic models with pre/post immune profiling would be definitive.

The full dataset includes 32 structured runs and 35+ operationalized hypotheses, each with specified protocols, predicted outcomes, and falsification criteria:

- Preprint: [doi.org/10.1101/2026.02.16.706165](https://doi.org/10.1101/2026.02.16.706165)
- Repository: [github.com/templetwo/vdac-pharmacology-atlas](https://github.com/templetwo/vdac-pharmacology-atlas)

This work is computational and AI-assisted. It awaits experimental validation. I am not asking for authorship — I am looking for researchers interested in testing falsifiable predictions with open data. Any feedback, including skepticism, would be valuable.

Respectfully,

Anthony J. Vasquez Sr.
Delaware Valley University
vasquezaj3921@delval.edu
