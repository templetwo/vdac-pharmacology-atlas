# Twitter/X Launch Thread — VDAC1 Pharmacology Atlas

**Audience**: Science Twitter — immuno-oncology, computational biology, pharmacology
**Tone**: Confident, hedged appropriately. Predictions not proofs.
**When to post**: Tuesday-Thursday, 10am-12pm EST

---

## The Thread

**1/**
New preprint: We predict a three-variable score from tumor biopsy that may identify checkpoint inhibitor non-responders before treatment begins.

Gate-Jamming Score = f_HKII x 0.4 + f_BclxL x 0.3 + [Chol]/[CL] x 0.3

All three terms measurable from standard biopsy.

https://doi.org/10.1101/2026.02.16.706165

---

**2/**
The logic: cancer cells that jam VDAC1 shut prevent oligomerization. No oligomerization means no mtDNA release into the cytoplasm. No mtDNA release means no cGAS-STING activation. The tumor becomes invisible to innate immunity -- not by suppressing the immune system, but by never triggering it.

---

**3/**
The Warburg effect may serve dual purpose: metabolic survival AND immune evasion through the same gate-jamming mechanism. HK-II on VDAC blocks apoptosis. It also blocks the oligomerization step that would alert the immune system. One corruption, two payoffs.

---

**4/**
We mapped this from 32 runs of a multi-LLM convergence protocol (5 independent models, zero cross-exposure, server-side grading). On the immunotherapy prediction run, all 5 models converged independently at cosine 0.93. Six novel findings, zero contradictions.

---

**5/**
The Gate-Jamming Score derives from a cofactor equation for the apoptotic threshold:

Threshold = K / [(1 - f_HKII)(1 - f_BclxL)] x [Chol]/[CL]

Cancer corrupts every term simultaneously. The GJS linearizes the three most druggable variables into a predictive biomarker.

---

**6/**
The same structural pattern -- dose picks the pathway, tissue determines the outcome -- appeared independently across 6 molecules (CBD, lithium, THC, psilocybin, metformin, ketamine) in 6 separate runs. Every molecule is a stress test. The protein is the decision gate.

---

**7/**
Also in the atlas: a pharmacovigilance alert for VPA + CBD co-prescription. The standard CYP450 explanation for hepatotoxicity is incomplete. We predict a mitochondrial convergence mechanism affecting an estimated 2,000-3,500 US pediatric epilepsy patients currently on both drugs.

---

**8/**
Total cost: $22 in API calls. 32 runs. Built by an undergrad with no lab, no grant, no institutional backing. Every finding is a hypothesis. Every prediction is falsifiable. The data, code, and all convergence scores are open access (CC BY 4.0).

---

**9/**
Everything is open:

Preprint: https://doi.org/10.1101/2026.02.16.706165
Data + code: https://github.com/templetwo/vdac-pharmacology-atlas
Full dataset: https://huggingface.co/datasets/TheTempleofTwo/vdac-pharmacology-atlas

35+ operationalized hypotheses with protocols and testability scores.

---

**10/**
If you work on VDAC-targeted therapeutics, checkpoint inhibitor biomarkers, or mitochondrial oncology: the GJS is testable today. Compute it across TCGA pan-cancer, correlate with documented immunotherapy response rates, and the prediction either holds or it does not. We welcome the test.
