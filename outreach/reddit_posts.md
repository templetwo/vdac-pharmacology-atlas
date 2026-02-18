# Reddit Launch Posts — VDAC Pharmacology Atlas v2

Three posts, three audiences, three angles. Post and forget.

**Updated 2026-02-18 with Run 32 findings (Gate-Jamming Score, immunotherapy prediction).**

---

## Post 1: r/bioinformatics

**Target**: Computational biologists, method-oriented researchers
**Angle**: The method — multi-LLM convergence as a reproducible scientific tool
**Best time to post**: Tuesday-Thursday, 9-11am EST

### Title

We ran the same pharmacology question through 5 independent AI models with no cross-exposure, graded convergence server-side, and 32 runs later the system is generating clinically testable predictions. Here's how.

### Body

I'm an undergrad (horticulture + IT) who built a multi-LLM convergence protocol called IRIS to study VDAC1 pharmacology. The core idea: five models (Claude, Gemini, Grok, Mistral, DeepSeek) receive the same compiled question, respond independently, and the *system* finds convergence through semantic embedding + complete-linkage clustering. No model ever sees another's output.

**How it works:**
- Claims extracted from each model's response and embedded with all-MiniLM-L6-v2
- Cosine similarity ≥ 0.70 → clustered. TYPE assigned by model count: 5/5 = TYPE 0, 1/5 = TYPE 3 (singular)
- S3 convergence gate: cosine > 0.85 + Jaccard floor + domain-adaptive thresholds
- Claims verified against indexed literature (Perplexity sonar-pro)
- Hypotheses operationalized with Monte Carlo parameter maps
- Cross-run tool: embeds claims across all runs, finds matches the single-run gate misses
- Zero self-reported convergence. All server-side.

**What 32 runs produced:**
- 200+ synthesized claims across pharmacology, neuroscience, and consciousness domains
- 34+ findings verified as NOVEL against indexed literature
- 35+ operationalized hypotheses (mean testability 7.2/10)
- A cofactor equation for apoptotic threshold that 5 models converged on independently
- A **Gate-Jamming Score** — three measurable biopsy variables that predict immunotherapy response (6 novel findings, 0 contradictions in the convergence run)
- 6 molecules (CBD, lithium, THC, psilocybin, metformin, ketamine) independently showing the same dose-dependent bifurcation pattern across 4 target classes
- Cross-run analysis: 10 cross-validated matches from 22 analyzed runs

**Key methodological findings:**

1. *S3-failed runs contain gold.* Two THC runs both failed convergence, but their singulars echoed each other across runs. The cross-run tool catches what the within-run gate misses.

2. *Convergence INCREASED over the project.* Early frontier questions (ultrasound, erastin) produced S3 failures. Later runs built on prior findings (immunotherapy prediction) passed S3 first cycle. The corpus bootstraps itself.

3. *Model disagreement is informative.* When models actively diverge across recirculation cycles (cosine drops), that's genuine scientific disagreement — not noise. The ultrasound-VDAC run showed cosine dropping from 0.95 → 0.48 across 3 cycles. The models were pushed apart, not together.

**Total cost: ~$22 in API calls for 32 runs.** The entire pipeline runs on a laptop.

Everything is open:
- **Paper** (bioRxiv): [BIORXIV/2026/706165](https://doi.org/10.1101/2026.02.16.706165)
- **Full dataset** (HuggingFace): [TheTempleofTwo/vdac-pharmacology-atlas](https://huggingface.co/datasets/TheTempleofTwo/vdac-pharmacology-atlas)
- **Code** (GitHub): [templetwo/iris-gate-evo](https://github.com/templetwo/iris-gate-evo)
- **Data + Index** (GitHub): [templetwo/vdac-pharmacology-atlas](https://github.com/templetwo/vdac-pharmacology-atlas)
- **Archive** (OSF): [10.17605/OSF.IO/C9RQB](https://osf.io/c9rqb/)

I'm not claiming this replaces wet-bench science. Every hypothesis awaits experimental validation. What I am claiming is that multi-model convergence with transparent classification produces clinically testable predictions at a cost and speed that changes who can do hypothesis generation.

---

## Post 2: r/pharmacology

**Target**: Pharmacologists, drug interaction researchers, clinical scientists, oncology-adjacent researchers
**Angle**: The clinical prediction — Gate-Jamming Score, immunotherapy, the cofactor equation
**Best time to post**: Monday-Wednesday, 10am-12pm EST

### Title

A three-variable score from tumor biopsy may predict checkpoint inhibitor response: we mapped VDAC1 pharmacology across 32 AI convergence runs and found that the same mechanism that jams the apoptotic gate also hides tumors from the immune system.

### Body

VDAC1 (voltage-dependent anion channel 1) controls metabolite flux across the outer mitochondrial membrane, gates cytochrome c release, and serves as the docking platform for hexokinase-II and Bcl-2 family proteins. We built the first systematic pharmacology of VDAC1 using a multi-model AI convergence protocol (5 independent models, server-side convergence grading, 32 runs). The manuscript is on bioRxiv ([BIORXIV/2026/706165](https://doi.org/10.1101/2026.02.16.706165)) and all data is open.

**The Cofactor Equation:**

> Apoptotic Threshold = K / [(1 - f_HKII)(1 - f_BclxL)] × [Chol]/[CL]

Every variable has a physical address on the protein. Cancer corrupts all of them simultaneously: HK-II jammed ON (Warburg), Bcl-xL overexpressed, cholesterol loaded into the OMM.

**The new finding — why gate-jamming predicts immunotherapy failure:**

When VDAC1 oligomerizes (the death commitment step), it leaks mtDNA into the cytoplasm, activating cGAS-STING innate immune signaling. Cancer cells that successfully jam the gate prevent VDAC oligomerization — and therefore prevent immune detection. **The Warburg effect serves dual purpose: metabolic survival AND immune evasion through the same mechanism.**

Five models converged on this independently (cosine 0.93, S3 PASSED first cycle). Six findings verified as NOVEL against indexed literature. Zero contradictions.

**The Gate-Jamming Score (GJS):**

> GJS = f_HKII × 0.4 + f_BclxL × 0.3 + [Chol]/[CL] × 0.3

Three terms, all measurable from tumor biopsy. Prediction: GJS correlates with immune-cold tumor status and predicts checkpoint inhibitor non-response.

**Operationalized hypotheses (from the convergence run):**
1. HK-II displacement (methyl jasmonate/clotrimazole) in immune-cold cell lines → measure cGAS-STING activation and mtDNA release (testability 9/10)
2. Gate-restoring drugs + anti-PD-1 → synergistic specifically in immune-cold syngeneic tumors (4T1, B16F10)
3. GJS computed across TCGA pan-cancer data predicts documented immunotherapy response rates (effect size 1.22)

**Cancer-type-specific weak links (from a separate run):**
- GBM (glioblastoma): f_HKII ~0.9 → HK-II displacement is rate-limiting
- AML (leukemia): f_BclxL ~0.8 → Bcl-xL release is rate-limiting (venetoclax)
- Cholesterol-loaded tumors: statin + any second term = supra-additive

**The multiplicative structure matters:** Reducing two terms by 50% each produces a 75% threshold drop. The combination is always worth more than the sum.

**Also in this atlas:**
- 17-compound modulator database (Kd/IC50, mechanism, isoform selectivity)
- VPA + CBD pharmacovigilance alert (mitochondrial hepatotoxicity beyond CYP450)
- Six molecules (CBD, lithium, THC, psilocybin, metformin, ketamine) all showing the same structural isomorphism: molecule as stress test, dose picks pathway, tissue determines outcome
- 35+ operationalized hypotheses with protocols

All data, all claims, all convergence scores: open access, CC BY 4.0.

- **Paper**: [bioRxiv BIORXIV/2026/706165](https://doi.org/10.1101/2026.02.16.706165)
- **Repository**: [templetwo/vdac-pharmacology-atlas](https://github.com/templetwo/vdac-pharmacology-atlas)
- **OSF**: [10.17605/OSF.IO/C9RQB](https://osf.io/c9rqb/)

Every finding is a hypothesis. Every prediction is falsifiable. If you work on VDAC-targeted therapeutics, checkpoint inhibitor biomarkers, or mitochondrial oncology, the data and protocols are waiting.

---

## Post 3: r/MachineLearning

**Target**: ML researchers, AI-for-science community
**Angle**: The dataset, what multi-model disagreement reveals, and the emergent structural pattern
**Best time to post**: Tuesday-Thursday, 10am-1pm EST

### Title

We're releasing a multi-LLM scientific convergence dataset: 5 models × 32 questions × 200+ classified claims. The same dose-response pattern emerged independently across 6 molecules in 6 different runs. Was it prompted? No.

### Body

**Dataset**: [TheTempleofTwo/vdac-pharmacology-atlas](https://huggingface.co/datasets/TheTempleofTwo/vdac-pharmacology-atlas) (HuggingFace, CC BY 4.0)

**Paper**: [bioRxiv BIORXIV/2026/706165](https://doi.org/10.1101/2026.02.16.706165)

This dataset comes from a pharmacology research program (mapping VDAC1, a mitochondrial decision gate), but the methodological contribution is model-independent: what happens when you run the same scientific question through 5 LLMs with zero cross-exposure and grade convergence server-side?

**Setup**: Claude, Gemini, Grok, Mistral, and DeepSeek each receive an identical compiled prompt. No model sees another's output. Responses are parsed into structured claims, embedded with all-MiniLM-L6-v2, and clustered by cosine similarity (complete-linkage, threshold 0.70).

**TYPE taxonomy** (assigned by model count in cluster):
- TYPE 0: 5/5 models agree (established consensus)
- TYPE 1: 3-4/5 models (strong convergence)
- TYPE 2: 2/5 models (speculative)
- TYPE 3: 1/5 models (singular — one model said something no other said)

**What the dataset contains (v2 — expanded)**:
- 32 runs across pharmacology, neuroscience, and consciousness domains
- 200+ synthesized claims with TYPE, confidence, mechanism, and falsifiability fields
- Per-run JSON: raw formulations (s1), synthesis (s2), convergence scoring (s3), hypotheses (s4), Monte Carlo (s5)
- Cross-run analysis: 10 cross-validated matches from 22 analyzed runs
- 23 human-curated "gold" documents integrating machine output into scientific analysis

**Four findings relevant to ML:**

1. **Singulars (TYPE 3) are disproportionately novel.** Of 34+ findings verified as NOVEL against indexed literature, a disproportionate fraction came from singulars — claims only one model made. The gate wants to filter these. Cross-run analysis shows singulars from one run often match convergent claims in another. TYPE 3 is where the frontier lives.

2. **Model agreement ≠ truth, but model *divergence* is informative.** When cosine similarity DROPS across recirculation cycles (we feed converged claims back and re-query), the models are actively pushed apart. The ultrasound-VDAC run showed cosine dropping 0.95 → 0.48 across 3 cycles. This signature — decreasing convergence under pressure — reliably indicates genuine scientific disagreement rather than noise.

3. **Structural isomorphism: same pattern, 6 molecules, never prompted.** CBD, lithium, THC, psilocybin, metformin, and ketamine all produced the same abstract pattern — molecule as stress test, dose picks pathway, tissue determines outcome — across runs separated by days with different seed questions. Four different target classes (channel, kinase, GPCR, enzyme). Whether this reflects genuine biological structure or a shared representation bias in LLM training is an open empirical question. The dataset lets you investigate.

4. **The corpus bootstraps itself.** Early runs on frontier questions (ultrasound, erastin) produced S3 failures. Later runs that built on established findings (immunotherapy prediction built on the cofactor equation) passed S3 first cycle with strong convergence. Prior runs create a knowledge scaffold that makes subsequent convergence easier. This has implications for sequential scientific AI: the order you ask questions matters.

If you work on LLM evaluation, multi-agent systems, scientific AI, or convergence metrics, this is 32 runs of structured claim-level data with human-annotated gold standards, cross-run replication analysis, and an emergent structural regularity to explain or debunk.

- **Dataset**: [HuggingFace](https://huggingface.co/datasets/TheTempleofTwo/vdac-pharmacology-atlas)
- **Pipeline code**: [GitHub](https://github.com/templetwo/iris-gate-evo)
- **Full repo with index**: [GitHub](https://github.com/templetwo/vdac-pharmacology-atlas)

---

## Post 4: r/oncology or r/cancer

**Target**: Oncology researchers, clinical trial designers, immunotherapy community
**Angle**: The Gate-Jamming Score as immunotherapy biomarker
**Best time to post**: Monday-Wednesday, 10am-12pm EST

### Title

A computational model predicts that the same metabolic rewiring that makes tumors glycolytic (Warburg effect) also makes them invisible to the immune system — through one protein and one equation.

### Body

We've been mapping the pharmacology of VDAC1 (voltage-dependent anion channel 1) — the most abundant protein in the outer mitochondrial membrane, the gate that controls whether a cell commits to apoptosis.

From 32 multi-model AI convergence runs (5 independent models, server-side convergence, no cross-contamination), a prediction emerged that we think the oncology community should examine:

**The logic chain:**
1. Cancer cells jam the apoptotic gate by simultaneously overexpressing HK-II (blocks VDAC), overexpressing Bcl-xL (suppresses audit), and loading cholesterol into the OMM (rigidifies membrane)
2. Jamming the gate prevents VDAC1 oligomerization
3. Without VDAC oligomerization, there is no mtDNA release into the cytoplasm
4. Without mtDNA release, the cGAS-STING innate immune pathway doesn't fire
5. Without cGAS-STING, the tumor is invisible to innate immunity
6. Checkpoint inhibitors (PD-1/PD-L1 blockade) require immune visibility to amplify — if the tumor is invisible, there's nothing to amplify

**The prediction:** Gate-jamming → immune evasion. The Warburg effect serves dual purpose — metabolic survival AND immune invisibility — through the same mechanism.

**The proposed biomarker — Gate-Jamming Score (GJS):**

> GJS = f_HKII × 0.4 + f_BclxL × 0.3 + [Chol]/[CL] × 0.3

Three terms, all measurable from tumor biopsy. We predict GJS correlates with immune-cold status and checkpoint inhibitor non-response.

**Three testable hypotheses (from the convergence run):**
1. Displacing HK-II from VDAC1 in immune-cold cell lines should activate cGAS-STING and trigger mtDNA release (testability 9/10)
2. Gate-restoring drugs + anti-PD-1 should show synergy specifically in immune-cold syngeneic tumors
3. GJS computed across TCGA pan-cancer data should predict documented immunotherapy response rates

**Cancer-type specificity:** The equation's multiplicative structure means the "weakest link" differs by cancer type. In glycolytic tumors (GBM), HK-II displacement is rate-limiting. In hematologic malignancies (AML), Bcl-xL inhibition matters more. Cholesterol-loaded tumors respond to statins.

Five models converged on this framework independently (cosine 0.93). Six claims verified as NOVEL against indexed literature. Zero contradictions.

This is a computational prediction, not a clinical finding. Every hypothesis requires experimental validation. But the logic is falsifiable, the biomarker is measurable, and the data is open.

- **Preprint**: [bioRxiv BIORXIV/2026/706165](https://doi.org/10.1101/2026.02.16.706165)
- **Full data**: [templetwo/vdac-pharmacology-atlas](https://github.com/templetwo/vdac-pharmacology-atlas)
- **Run 32 data**: `runs/evo_20260218_002623_pharmacology/` in the repo

If you work on checkpoint inhibitor biomarkers, tumor immunology, or mitochondrial oncology — we'd welcome scrutiny. The claims are structured, typed, and falsifiable. That's the point.

---

## Bonus Communities (shorter posts, link + 2-3 sentences)

### r/GrassrootsResearch
*Already connected community.* Short post linking the manifesto PDF with one line: "An undergrad with no lab, no grant, and $22 in API calls mapped the pharmacology of the protein that decides whether your cells live or die — and the 32nd run produced a biomarker proposal for immunotherapy response. Here's the manifesto on what that means for who gets to do science."

### r/labrats
"If you work on VDAC1, mitochondrial pharmacology, or checkpoint inhibitor biomarkers: we have 35+ operationalized hypotheses with protocols waiting for a bench. The newest one predicts that HK-II displacement from VDAC1 should activate cGAS-STING in immune-cold tumor lines. Open access, CC BY 4.0. Paper on bioRxiv, data on GitHub." Link to repo.

### r/druginteractions or r/pharmacy
Focused post on the VPA + CBD hepatotoxicity alert specifically. "We found evidence of a mitochondrial mechanism for CBD + valproate hepatotoxicity beyond CYP450 competition. Relevant to epilepsy patients on Epidiolex + VPA. GSH/GSSG ratio may be predictive. Details in our preprint." Link to bioRxiv.

### r/immunotherapy or r/immunology
Focused post on Run 32: "A multi-model AI convergence analysis predicts that cancer's metabolic gate-jamming (HK-II + Bcl-xL + cholesterol) simultaneously prevents apoptosis AND immune detection by blocking VDAC1 oligomerization → mtDNA release → cGAS-STING. We propose a three-variable Gate-Jamming Score measurable from biopsy that may predict checkpoint inhibitor response. 5 models, 0 contradictions, all data open." Link to repo + preprint.

---

*Updated 2026-02-18. 32 runs. Post, forget, let the work speak.*
