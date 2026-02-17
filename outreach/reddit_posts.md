# Reddit Launch Posts — VDAC Pharmacology Atlas

Three posts, three audiences, three angles. Post and forget.

---

## Post 1: r/bioinformatics

**Target**: Computational biologists, method-oriented researchers
**Angle**: The method — multi-LLM convergence as a reproducible scientific tool
**Best time to post**: Tuesday-Thursday, 9-11am EST

### Title

We ran the same pharmacology question through 5 independent AI models with no cross-exposure and graded convergence server-side. Here's what 20 runs and $15 produced.

### Body

I'm an undergrad (horticulture + IT) who built a multi-LLM convergence protocol called IRIS to study VDAC1 pharmacology. The core idea is simple: five models (Claude, Gemini, Grok, Mistral, DeepSeek) receive the same compiled question, respond independently, and the *system* finds convergence through semantic embedding + complete-linkage clustering. No model ever sees another's output.

**How it works:**
- Claims are extracted from each model's response and embedded with all-MiniLM-L6-v2
- Cosine similarity ≥ 0.70 → clustered. TYPE assigned by model count: 5/5 = TYPE 0, 1/5 = TYPE 3 (singular)
- S3 convergence gate: cosine > 0.85 + Jaccard floor + domain-adaptive thresholds
- Claims verified against indexed literature (Perplexity sonar-pro)
- Hypotheses operationalized with Monte Carlo parameter maps
- Zero self-reported convergence. All server-side.

**What 20 runs produced:**
- 139 synthesized claims across pharmacology, neuroscience, and consciousness domains
- 22 findings verified as NOVEL against indexed literature
- 24 operationalized hypotheses (mean testability 7.2/10)
- A cofactor equation for apoptotic threshold that 5 models converged on independently
- 3 pharmacovigilance alerts (including a CBD + valproate interaction in epilepsy patients)
- Cross-run analysis: 11,881 pairwise claim comparisons, 6 cross-validated matches

**The interesting methodological finding:** S3-failed runs contain gold. Two independent runs on THC both failed the convergence gate, but their singulars (TYPE 3 — one model only) echoed each other across runs. The cross-run tool catches what the within-run gate misses. Singulars are signal, not noise.

**Total cost: ~$15 in API calls.** The entire pipeline runs on a laptop.

Everything is open:
- **Paper** (bioRxiv): BIORXIV/2026/706165
- **Full dataset** (HuggingFace): [TheTempleofTwo/vdac-pharmacology-atlas](https://huggingface.co/datasets/TheTempleofTwo/vdac-pharmacology-atlas) — first publicly available multi-LLM scientific convergence dataset
- **Code** (GitHub): [templetwo/iris-gate-evo](https://github.com/templetwo/iris-gate-evo)
- **Data + Index** (GitHub): [templetwo/vdac-pharmacology-atlas](https://github.com/templetwo/vdac-pharmacology-atlas)
- **Archive** (OSF): [10.17605/OSF.IO/C9RQB](https://osf.io/c9rqb/)

I'm not claiming this replaces wet-bench science. Every hypothesis awaits experimental validation. What I am claiming is that multi-model convergence with transparent classification produces something qualitatively different from asking a single model — and that the evidentiary structure is worth examining as methodology.

Happy to answer questions about the pipeline, the embedding approach, or why complete-linkage clustering matters here (union-find caused transitive chaining that inflated TYPE 0 counts).

---

## Post 2: r/pharmacology

**Target**: Pharmacologists, drug interaction researchers, clinical scientists
**Angle**: The science — VDAC1 as druggable target, the cofactor equation, the VPA+CBD alert
**Best time to post**: Monday-Wednesday, 10am-12pm EST

### Title

We mapped the first systematic pharmacology of VDAC1 — the mitochondrial channel that decides if your cells live or die. 17 compounds, 3 isoforms, and a cofactor equation that cancer corrupts on every term.

### Body

VDAC1 (voltage-dependent anion channel 1) controls metabolite flux across the outer mitochondrial membrane, gates cytochrome c release, and serves as the docking platform for hexokinase-II, Bcl-2 family proteins, and tubulin. Multiple drugs interact with it — CBD, erastin, DIDS, olesoxime — but until now, no one had assembled a systematic pharmacology: no binding site atlas, no isoform selectivity map, no unified drugability assessment.

We built that map using a multi-model AI convergence protocol (5 independent models, server-side convergence grading, 20 runs). The manuscript is on bioRxiv (BIORXIV/2026/706165) and all data is open.

**The central finding — the Cofactor Equation:**

> Apoptotic Threshold = K / [(1 - f_HKII)(1 - f_BclxL)] × [Chol]/[CL]

Every variable has a physical address on the protein:
- **f_HKII**: Hexokinase-II occupancy on the cytoplasmic barrel face — the metabolic loyalty signal
- **f_BclxL**: Bcl-xL binding to extruded N-terminal helices — the anti-apoptotic badge
- **Chol/CL**: Cholesterol-to-cardiolipin ratio in the lipid annulus — the membrane stability readout
- **K**: Honeycomb lattice exit energy — the rate-limiting step

The multiplicative structure means simultaneous reduction of f_HKII + f_BclxL produces threshold drop *greater than the sum* of individual reductions. Prediction: 2-DG + ABT-737 combination index CI < 0.8 (supra-additive). This converged across 4 of 5 models independently.

**Why cancer is gate-jamming:**
Cancer rewrites every term simultaneously. HK-II jammed ON (Warburg), Bcl-xL overexpressed, cholesterol loaded into the OMM. The Warburg effect may exist specifically to fund the gate-jamming — it's expensive because it has to be. The cost is detectable precisely because maintaining all three corruptions requires continuous metabolic investment.

**Pharmacovigilance alert — VPA + CBD:**
Valproate opens VDAC (increasing conductance). NAPQI (acetaminophen metabolite) closes it. Both are hepatotoxic — opposite mechanisms, same organ damage. CBD engages VDAC directly (Kd ~11 μM). In epilepsy patients on VPA + CBD (which is a real clinical combination — Epidiolex), there's a mitochondrial mechanism for hepatotoxicity *beyond* the known CYP450 competition. The GSH/GSSG ratio is predictive; standard liver panels miss it until damage is done.

**Modulator database**: 17 compounds with Kd/IC50, mechanism, isoform preference, therapeutic context — available as CSV in the repo.

All data, all claims, all convergence scores, all hypotheses: open access, CC BY 4.0.

- **Paper**: bioRxiv BIORXIV/2026/706165
- **Repository**: [templetwo/vdac-pharmacology-atlas](https://github.com/templetwo/vdac-pharmacology-atlas)
- **OSF**: [10.17605/OSF.IO/C9RQB](https://osf.io/c9rqb/)

Every finding is a hypothesis, not a fact. Every prediction is falsifiable. Six open questions in the manuscript, each a full paper for whoever wants to run it. If you work on VDAC-targeted therapeutics, mitochondrial pharmacology, or drug-induced hepatotoxicity, the protocols are waiting.

---

## Post 3: r/MachineLearning

**Target**: ML researchers, AI-for-science community
**Angle**: The dataset and what multi-model disagreement reveals
**Best time to post**: Tuesday-Thursday, 10am-1pm EST

### Title

We're releasing the first multi-LLM scientific convergence dataset: 5 models × 20 questions × 159 classified claims, with full TYPE taxonomy and cross-run replication analysis

### Body

**Dataset**: [TheTempleofTwo/vdac-pharmacology-atlas](https://huggingface.co/datasets/TheTempleofTwo/vdac-pharmacology-atlas) (HuggingFace, CC BY 4.0)

**Paper**: bioRxiv BIORXIV/2026/706165

This dataset comes from a pharmacology research program (mapping VDAC1, a mitochondrial decision gate), but the methodological contribution is model-independent: what happens when you run the same scientific question through 5 LLMs with zero cross-exposure and grade convergence server-side?

**Setup**: Claude, Gemini, Grok, Mistral, and DeepSeek each receive an identical compiled prompt. No model sees another's output. Responses are parsed into structured claims, embedded with all-MiniLM-L6-v2, and clustered by cosine similarity (complete-linkage, threshold 0.70).

**TYPE taxonomy** (assigned by model count in cluster):
- TYPE 0: 5/5 models agree (established consensus)
- TYPE 1: 3-4/5 models (strong convergence)
- TYPE 2: 2/5 models (speculative)
- TYPE 3: 1/5 models (singular — one model said something no other said)

**What the dataset contains**:
- 22 runs across pharmacology, neuroscience, and consciousness domains
- 159 synthesized claims with TYPE, confidence, mechanism, and falsifiability fields
- Per-run JSON: raw formulations (s1), synthesis (s2), convergence scoring (s3), hypotheses (s4), Monte Carlo (s5)
- Cross-run analysis: 11,881 pairwise cosine comparisons across 18 runs, 6 matches at threshold ≥ 0.75
- 22 human-curated "gold" documents integrating machine output into scientific analysis

**Three findings relevant to ML:**

1. **Singulars (TYPE 3) are the most novel claims.** Of 22 findings verified as NOVEL against indexed literature, a disproportionate fraction came from singulars — claims only one model made. The gate naturally wants to filter these. But cross-run analysis showed that singulars from one run often match convergent claims in another. The signal-to-noise ratio in TYPE 3 is low, but the signal is where the frontier lives.

2. **Model agreement ≠ truth.** All 5 models share training data from the same scientific literature corpus. TYPE 0 (5/5 agree) can mean "this is well-established" or "this is a popular misconception all models learned." The VERIFY stage (checking against indexed sources) caught several TYPE 0 claims that were confidently wrong. Convergence is evidence of training distribution overlap, not ground truth.

3. **Cross-run replication reveals structure invisible within runs.** Two independent runs on THC pharmacology both failed the convergence gate. But their singulars — claims from Gemini in one run, Claude in another — described the same mechanism (CB1 occupancy-dependent pathway switching). The within-run gate can't see this. The cross-run tool (cosine across all claim pairs from different runs) found 6 such matches from 11,881 comparisons.

**Structural isomorphism**: The same abstract pattern (molecule as stress test, dose picks pathway, tissue determines outcome) emerged independently across 5 different molecules in 5 different runs. This was never prompted. It's an emergent structural regularity in how LLMs represent dose-response pharmacology. Whether this reflects genuine biological structure or shared training bias is an open question — and this dataset lets you investigate it.

If you work on LLM evaluation, multi-agent systems, scientific AI, or convergence metrics, this is raw material. 22 runs of structured claim-level data with human-annotated gold standards.

- **Dataset**: [HuggingFace](https://huggingface.co/datasets/TheTempleofTwo/vdac-pharmacology-atlas)
- **Pipeline code**: [GitHub](https://github.com/templetwo/iris-gate-evo)
- **Full repo with index**: [GitHub](https://github.com/templetwo/vdac-pharmacology-atlas)

---

## Bonus Communities (shorter posts, link + 2-3 sentences)

### r/GrassrootsResearch
*Already connected community.* Short post linking the manifesto PDF with one line: "An undergrad with no lab, no grant, and $15 in API calls mapped the pharmacology of the protein that decides whether your cells live or die. Here's the manifesto on what that means for who gets to do science."

### r/labrats
"If you work on VDAC1, mitochondrial pharmacology, or drug-induced hepatotoxicity: we have 24 operationalized hypotheses with protocols waiting for a bench. Open access, CC BY 4.0. Paper on bioRxiv, data on GitHub." Link to repo.

### r/druginteractions or r/pharmacy
Focused post on the VPA + CBD hepatotoxicity alert specifically. "We found evidence of a mitochondrial mechanism for CBD + valproate hepatotoxicity beyond CYP450 competition. Relevant to epilepsy patients on Epidiolex + VPA. GSH/GSSG ratio may be predictive. Details in our preprint." Link to bioRxiv.

---

*Written 2026-02-16. Post, forget, let the work speak.*
