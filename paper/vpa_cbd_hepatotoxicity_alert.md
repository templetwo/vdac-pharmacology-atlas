# Pharmacovigilance Alert: VPA + CBD Hepatotoxicity

## Mechanisms, Monitoring, and the Untested Mitochondrial Convergence Hypothesis

> **Up to 30% of co-prescribed patients develop ALT elevations >3× ULN**  
> **The standard CYP450 explanation is demonstrably wrong**  
> **An estimated 2,000–3,500 US pediatric patients are currently affected**

**Anthony J. Vasquez Sr.**  
Independent Pharmacovigilance Research — The Temple of Two  
Delaware Valley University — Cannabis Pharmacology / Horticulture  
February 2026

*FOR CLINICAL AND RESEARCH USE — NOT A PRESCRIBING DIRECTIVE*

---

## 1. Executive Summary

The mechanism driving the synergistic hepatotoxicity of valproate (VPA) and cannabidiol (CBD) remains unknown — and the standard CYP450 explanation is wrong. Multiple well-designed pharmacokinetic studies have definitively shown that CBD does not increase circulating VPA or its hepatotoxic metabolite 4-ene-VPA, yet up to 30% of patients on both drugs develop ALT elevations above 3× ULN. This pharmacodynamic interaction — real, dose-dependent, and clinically significant — affects an estimated 2,000–3,500 pediatric epilepsy patients in the United States currently co-prescribed this combination for Dravet syndrome.

The June 2025 FDA label update added postmarketing reports of cholestatic and mixed liver injury patterns not seen in clinical trials, signaling an evolving safety profile. No fatal hepatotoxicity cases from this combination have been published, but a convergent mitochondrial mechanism — VPA depleting cellular reserves while CBD modulates VDAC1 conductance — has never been tested and represents a critical gap in pharmacovigilance.

---

## 2. The Standard CYP450 Explanation Does Not Hold Up

The textbook account of this interaction is straightforward: CBD inhibits CYP2C9, which metabolizes VPA, leading to elevated VPA levels and accumulation of its hepatotoxic metabolite 4-ene-VPA. This explanation is widely cited in clinical references and drug interaction databases. **It is also contradicted by every rigorous pharmacokinetic study conducted to date.**

Morrison et al. (2019) administered CBD 750 mg BID with VPA 500 mg BID to healthy volunteers and found no clinically relevant effect on VPA exposure — no increase in VPA Cmax, AUC, or 4-ene-VPA levels. Ben-Menachem et al. (2020) replicated this in epilepsy patients: VPA Cmax decreased 13%, AUCτ decreased 17%, and critically, 4-ene-VPA decreased by 23–30% — the **opposite direction** from what CYP2C9 inhibition would predict. The 2025 Epidiolex prescribing label confirms these findings: VPA exposure decreased approximately 17–21%, and 4-ene-VPA exposure decreased 28–33% with CBD co-administration.

Yet the hepatotoxicity signal is unambiguous. In controlled trials for Lennox-Gastaut syndrome and Dravet syndrome, ALT elevations above 3× ULN occurred in 21% of patients on VPA + CBD (without clobazam) and 30% of patients on VPA + CBD + clobazam, compared to just 3% on CBD alone and 1% on placebo. In the Dravet GWPCARE1 trial, all 12 patients with elevated transaminases in the CBD group were taking concomitant VPA. The odds ratio for liver enzyme elevation with VPA co-administration is **6.92 (95% CI 4.74–10.09, p<0.001)**. This interaction is pharmacodynamic, not pharmacokinetic — the drugs are not changing each other's blood levels in a way that explains the liver damage.

### Computational Modeling Failure

The most sophisticated attempt to model this interaction computationally — Lakhani et al.'s 2023 DILIsym quantitative systems toxicology study — tested three major mechanisms of direct hepatotoxicity: bile acid transporter inhibition, mitochondrial dysfunction, and reactive oxygen species production. **None could reproduce the clinical synergy.** The authors concluded that the "marked increased incidence of CBD-associated ALT elevations in patients already receiving VPA is unlikely to involve the three major mechanisms of direct hepatotoxicity."

Beers et al. (2025) achieved the first in vitro recapitulation of the interaction using 3D human hepatocyte spheroids but stated explicitly that "the mechanism for the synergistic toxicity with CBD and VPA concomitant use remains unknown."

---

## 3. What the FDA Label Actually Says — and Where It Falls Short

The Epidiolex prescribing label (NDA 210365/S-023, revised June 2025) places hepatotoxicity in Section 5.1 (Warnings and Precautions) — notably **not** a boxed warning, and no REMS is required. The label stratifies risk clearly by concomitant medication status:

| Patient Scenario | ALT >3× ULN Incidence |
|---|---|
| CBD alone (no VPA, no clobazam) | 3% |
| CBD + clobazam only | 4% |
| CBD + VPA only | 21% |
| CBD + VPA + clobazam | 30% |
| CBD + elevated baseline ALT | 30% |
| Placebo | 1% |

Approximately 5% of all patients on VPA had ALT >5× ULN, and less than 1% exceeded 20× ULN. Two cases in clinical trials met modified Hy's Law criteria (ALT ≥3× ULN combined with bilirubin ≥1.5× ULN), both resolving without intervention.

The 2025 label update added two significant postmarketing findings: cholestatic or mixed patterns of liver injury (distinct from the hepatocellular pattern seen in trials) and elevated ammonia levels in patients with transaminase elevations, primarily those on concomitant VPA or clobazam.

### Monitoring Schedule Comparison

The FDA monitoring schedule requires baseline transaminases and total bilirubin before initiation, then at 1, 3, and 6 months, and periodically thereafter. For patients on VPA, the label recommends "more frequent monitoring" without specifying an exact schedule. The EMA's Epidyolex SmPC is more prescriptive, mandating checks at **2 weeks, 1 month, 2 months, 3 months, and 6 months** for patients on VPA or with elevated baseline LFTs. Discontinuation criteria are ALT >3× ULN with bilirubin >2× ULN, or sustained transaminase elevations >5× ULN.

A notable finding from a 2025 FDA-funded randomized controlled trial (Florian et al., JAMA Internal Medicine): 5.6% of healthy adults receiving CBD at consumer-relevant doses (~397 mg/day) developed ALT >3× ULN after just 28 days — with no concomitant medications. This establishes an intrinsic hepatotoxicity signal for CBD independent of drug interactions.

---

## 4. A Mitochondrial Convergence Hypothesis That No One Has Tested

Two bodies of evidence exist in parallel, each well-established, **never connected in any peer-reviewed publication**.

### Evidence Stream 1: VPA Mitochondrial Toxicity

Spanning decades and hundreds of publications, VPA's mitochondrial toxicity is documented in granular mechanistic detail. VPA enters mitochondria as valproyl-CoA, competing with endogenous fatty acid β-oxidation, sequestering CoA, and generating the reactive metabolite 2,4-diene-VPA-CoA that irreversibly inhibits β-oxidation enzymes and depletes mitochondrial glutathione.

VPA depletes carnitine through three independent mechanisms:
1. Valproylcarnitine formation and renal excretion
2. Inhibition of endogenous carnitine biosynthesis
3. Impaired renal reabsorption

VPA directly inhibits cytochrome c oxidase (Complex IV) and α-lipoamide dehydrogenase at concentrations within the therapeutic range. The clinical consequence is hepatocytes operating with **diminished metabolic reserves** — reduced GSH, carnitine, CoA, and impaired oxidative phosphorylation — in a compensated but vulnerable state. The catastrophic sensitivity of POLG-mutation carriers (52% fatality rate with VPA exposure) provides genetic proof that pre-existing mitochondrial compromise converts VPA from manageable stress to lethal insult.

### Evidence Stream 2: CBD's Direct VDAC1 Interaction

Rimmerman et al. (2013, *Cell Death & Disease*) demonstrated that CBD binds VDAC1 (voltage-dependent anion channel 1) on the outer mitochondrial membrane, markedly decreasing channel conductance in single-channel recordings. VDAC1 is the primary gateway for ATP/ADP exchange, metabolite flux, and calcium transit between the cytosol and mitochondrial intermembrane space.

CBD reduces mitochondrial membrane potential (IC50 ~10 μM), induces ROS production (EC50 ~4.9 μM), and triggers calcium dysregulation that can activate the mitochondrial permeability transition pore. Subsequent studies have confirmed VDAC1 as a validated CBD binding target, with pharmacologic VDAC1 inhibition (DIDS) providing substantial protection against CBD-mediated cell death.

### The Convergence: Never Proposed in Literature

**No peer-reviewed publication has connected these two well-documented mitochondrial effects as a convergent mechanism for VPA + CBD hepatotoxicity.**

This represents an explicit, clearly identified gap in the literature.

The theoretical framework is biologically coherent: VPA chronically depletes the metabolic reserves (carnitine, CoA, GSH) and impairs the respiratory chain capacity of hepatocytes, then CBD is added and alters VDAC1 conductance — disrupting metabolite flux, calcium homeostasis, and potentially facilitating mPTP opening in cells that have lost the antioxidant and metabolic buffer capacity to withstand the additional stress.

Critically, the Lakhani et al. DILIsym study that failed to reproduce the synergy tested "generic" mitochondrial dysfunction via electron transport chain inhibition assays — it did not model VDAC1-specific effects, cumulative reserve depletion, or threshold dynamics. The negative finding may reflect model limitations rather than a genuine absence of mitochondrial convergence.

---

## 5. Managing the Combination in Dravet Syndrome Patients

Dravet syndrome affects approximately 20,000 people in the United States (incidence ~1 per 15,700 live births). Real-world prescription data from the TriNetX network (Xu et al., *Epilepsia Open* 2025) show that approximately 34% of Dravet patients receive VPA and 29% receive CBD/Epidiolex, suggesting a co-prescribed population of roughly **2,000–3,500 US patients**. Both VPA and clobazam remain first-line maintenance therapies per international consensus (Wirrell et al., 2022 Delphi process), while CBD is positioned as a first- to third-line option depending on guideline source.

### Actionable Risk Mitigation

| Intervention | Recommendation | Evidence |
|---|---|---|
| **Dose** | Use 10 mg/kg/day CBD rather than 20 mg/kg/day when possible | ALT >3× ULN drops from ~21% to ~1% at lower dose |
| **Monitoring** | Follow EMA schedule: 2 weeks, 1, 2, 3, and 6 months | More sensitive than FDA schedule for high-risk patients |
| **Ammonia** | Monitor alongside transaminases | 2025 label update — VPA co-administration elevates risk |
| **L-Carnitine** | 100 mg/kg/day (max 2 g/day) for young children on VPA polytherapy | Pediatric Neurology Advisory Committee recommendation |
| **POLG Screening** | Consider in developmental regression or family history of mito disease | 52% fatality rate with VPA in confirmed POLG carriers |
| **Discontinuation** | ALT >3× ULN with bilirubin >2× ULN, or sustained >5× ULN | EMA/FDA threshold |

No fatal hepatotoxicity cases attributable to VPA + CBD have been published. No liver transplants from this combination have been reported. Approximately two-thirds of transaminase elevations resolved with dose reduction of CBD and/or VPA, and one-third resolved spontaneously during continued treatment. However, the postmarketing emergence of cholestatic and mixed liver injury patterns warrants continued vigilance.

---

## 6. The Biomarker Gap and What Could Fill It

Standard monitoring relies on ALT, AST, and total bilirubin — blunt instruments that cannot distinguish benign adaptive elevation from progressive injury, hepatocellular from cholestatic damage, or CYP450-mediated effects from mitochondrial toxicity. Several emerging biomarkers could transform monitoring of VPA + CBD patients but remain **untested in this specific context**.

| Biomarker | What It Detects | Evidence Base |
|---|---|---|
| GDF15 + FGF21 | Mitochondrial hepatopathies | 88% sensitivity, 96% specificity when both >98th percentile (Van Hove 2024) |
| miR-122 | Hepatocyte damage (pre-clinical) | Rises before transaminases; ROC-AUC 0.98 for DILI |
| GLDH | Mitochondrial damage specifically | Mitochondrial matrix enzyme; specific for mito injury |
| Acylcarnitine profile | Impaired β-oxidation | Validated for VPA; could reveal if CBD worsens signature |

### Pharmacogenomic Testing: An Unexploited Avenue

CYP2C9 wild-type carriers produce more 4-ene-VPA and show higher hepatotoxicity risk (OR 7.50 in Chinese epilepsy cohorts). POLG heterozygous variants carry dramatically elevated VPA hepatotoxicity risk (OR 23.6 in DILIN data). **No pharmacogenomic study has been conducted specifically in VPA + CBD patients** — a striking omission given the severity and frequency of the interaction.

---

## 7. Conclusion and Testable Predictions

The VPA + CBD hepatotoxicity interaction presents a paradox: it is one of the most clinically significant drug interactions in pediatric epilepsy, affecting up to 30% of co-prescribed patients, yet its mechanism remains genuinely unknown. The standard CYP450 narrative is demonstrably incorrect. The DILIsym computational model has ruled out the three canonical mechanisms of direct hepatotoxicity. What remains is a pharmacodynamic interaction occurring at the intracellular or tissue level, invisible to plasma pharmacokinetics and uncharacterized by any existing model.

### Three Concrete Steps to Test the Hypothesis

1. **Measure GDF15/FGF21** in VPA + CBD patients who develop transaminase elevations to confirm or exclude mitochondrial involvement.
2. **Assess VPA-pretreated hepatocytes** for enhanced sensitivity to CBD-induced mitochondrial depolarization in vitro.
3. **Test VDAC1 inhibition or N-acetylcysteine supplementation** as protective interventions against the synergistic toxicity.

---

For clinicians managing these patients today: **Use 10 mg/kg/day CBD when possible** (reducing ALT >3× ULN risk from ~21% to ~1%), follow the EMA's intensive monitoring schedule, supplement L-carnitine in all young children on VPA polytherapy, monitor ammonia alongside transaminases, and consider POLG screening.

The gap between the severity of this interaction and the depth of our mechanistic understanding demands urgent, targeted research — **the children receiving this combination cannot wait for a mechanism to be discovered by accident.**

---

*Part of the [VDAC1 Pharmacology Atlas](https://github.com/templetwo/vdac-pharmacology-atlas) — Temple of Two, February 2026*  
*License: CC BY 4.0*
