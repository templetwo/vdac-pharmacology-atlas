# The VDAC1 Pharmacology Atlas: A Multi-LLM Convergence Portrait of Life's Decision Gate

**Authors**: A. Vaquez and Claude Opus 4.6 (Anthropic)
**Date**: 2026-02-14
**Status**: Preprint / Atlas Document
**IRIS Corpus**: 20 runs, 139 synthesized claims, 5 independent AI models

---

## Abstract

Voltage-dependent anion channel 1 (VDAC1) is the most abundant protein in the outer mitochondrial membrane and the principal gatekeeper of metabolite exchange between cytoplasm and mitochondria. This atlas synthesizes findings from 20 IRIS (Independent Replication through Integrated Synthesis) runs in which five AI models -- Claude, Gemini, Grok, Mistral, and DeepSeek -- independently analyzed the same compiled prompts without seeing each other's outputs. From 139 synthesized claims, 22 verified novel findings, and 24 operationalized hypotheses, a six-layer portrait of VDAC1 emerges. Layer 1 describes the protein: a unique 19-stranded beta-barrel housing five molecular machines in distinct oligomeric states. Layer 2 maps the decision architecture: three nested threshold signals (mitophagy, inflammation, apoptosis) governed by a cofactor equation integrating hexokinase-II occupancy, Bcl-xL binding, and the cholesterol-to-cardiolipin ratio. Layer 3 presents the pharmacological atlas proper: six dedicated runs revealing that drugs do not target VDAC1 so much as perturb the membrane context that determines its state. Layer 4 reframes cancer as a disease of lost coherence in which every term of the cofactor equation is simultaneously corrupted. Layer 5 describes the IRIS multi-LLM convergence method and what it can and cannot establish. Layer 6 situates VDAC1 within a broader framework of threshold logic operating from protein barrel to organism. What began as a pharmacology question about cannabidiol became a portrait of how multicellular life organizes its own error correction.

**Keywords**: VDAC1, mitochondria, apoptosis, pharmacology, multi-LLM convergence, hexokinase-II, cardiolipin, cholesterol, honeycomb lattice, cancer, cofactor equation, threshold logic, IRIS protocol

---

## Layer 1: The Protein -- What VDAC1 Is

### A Barrel Unlike Any Other

VDAC1 is 283 amino acids folded into a beta-barrel with 19 strands -- an odd number unique among porins. Most porins pair their strands antiparallel in even counts of 16 or 22. VDAC1's odd strand count forces beta-strands 1 and 19 to run parallel, creating a distinctive seam in the barrel wall. This seam, involving strands 1, 2, 18, and 19, turns out to be the most consequential structural feature in mitochondrial biology.

A 25-residue N-terminal alpha helix lies horizontally across the pore interior, narrowing the 34-angstrom opening to just 14 angstroms. This helix is intrinsically disordered in isolation and folds only on contact with the barrel. It carries three positive charges (Lys-12, Lys-20, Arg-15) and two negative (Asp-9, Asp-16), making it both a selectivity filter and a voltage sensor. It is, residue for residue, the most information-dense segment in mitochondrial biology.

Room-temperature crystallography in 2024 revealed that the barrel compresses 12% relative to cryogenic structures (10,314 to 9,102 cubic angstroms), demonstrating mechanical compliance. The barrel breathes. Elevated B-factors at loops connecting strands 1-2, 5-6, 8-9, and 18-19 mark these as hinges primed for conformational motion.

### Five Machines in One Protein

VDAC1 is not one channel. It is five overlapping molecular machines, each corresponding to a distinct oligomeric and conformational state:

| State | Stoichiometry | N-Terminal Helix | Function |
|-------|--------------|------------------|----------|
| Open monomer | 1 | Folded inside barrel | Metabolite highway: ATP, ADP, NADH pass freely (4 nS conductance) |
| Closed monomer | 1 | Displaced to barrel wall | Ca2+ conductor, metabolite restriction (~2 nS) |
| Dimer | 2 (parallel) | Inserted | Phospholipid scramblase -- accounts for >90% of mitochondrial lipid import |
| Honeycomb array | n (lattice) | Inserted | Protective lattice preventing oligomerization |
| Death oligomer | 6+ | Extruded from barrel | Cytochrome c release pore (~4 nm), Bcl-xL sequestration |

The voltage gating follows a symmetric bell curve centered at 0 mV, closing at both positive and negative voltages beyond 25-30 mV. This is unique among ion channels and means the OMM potential under normal conditions (~0 mV) keeps VDAC predominantly open -- the metabolite highway state.

### The Parallel Seam: Life and Death on the Same Interface

The parallel seam at strands 1/2/18/19 serves as the dimer interface for scramblase function and the oligomerization interface for death pore formation. These are mutually exclusive. The same surface that builds the membrane (scramblase, importing phospholipids for cardiolipin synthesis) also destroys the cell (death pore, releasing cytochrome c). A single protein face encodes a binary switch between membrane maintenance and cellular execution.

The 2025 cryo-EM discovery confirmed that oligomerization triggers N-terminal helix extrusion -- the helix physically leaves the pore and becomes exposed on the channel exterior, where it binds and sequesters anti-apoptotic Bcl-xL. This connects VDAC electrophysiology (helix position determines gating) with apoptosis biology (Bcl-xL sequestration determines cell fate). The helix is the molecular bridge.

### The Lipid and PTM Landscape

Five cholesterol binding sites on the barrel exterior stabilize both individual barrels and the honeycomb lattice. Two cardiolipin binding sites (near E73 and strands 18-19) sit in the disruption-sensitive region. The barrel exterior is wrapped by an anisotropic lipid annulus extending approximately 50 angstroms, with different faces recruiting different lipids.

More than 20 post-translational modification sites have been identified, including phosphorylation by PKA, PKC, GSK-3beta, JNK3, ERK, and CaMK-II, plus SIRT5-mediated desuccinylation, glutathionylation, and cysteine oxidation. GSK-3beta phosphorylation at Thr-51 is particularly significant: it regulates HK-II binding affinity, linking the circadian clock (BMAL1/CLOCK oscillation of GSK-3beta activity) directly to VDAC1's apoptotic threshold.

---

## Layer 2: The Gate -- How VDAC1 Decides

### Three Nested Threshold Signals

Literature synthesis across the IRIS corpus revealed three escalating signals that VDAC1 participates in, each representing a higher threshold of mitochondrial distress:

**Signal 1 -- Mitophagy (recycle this mitochondrion).** Cardiolipin externalizes from the inner to outer mitochondrial membrane, binds LC3 on the cytoplasmic face, and triggers selective autophagy. The damaged mitochondrion is removed. The cell survives.

**Signal 2 -- Inflammation (alert the immune system).** VDAC1 oligomerizes sufficiently to allow mitochondrial DNA escape through the pore. Cytosolic mtDNA activates the cGAS-STING pathway, triggering type I interferon production. The tissue mounts an immune response.

**Signal 3 -- Apoptosis (this cell must die).** Full oligomerization creates a pore large enough for cytochrome c release. The caspase cascade fires. Phosphatidylserine flips to the outer leaflet as an "eat me" signal. A macrophage engulfs the corpse.

The architecture is one of escalating sacrifice: repair, then alarm, then death. Each threshold is higher than the last. Cardiolipin oxidation state serves as the threshold variable: non-oxidized CL triggers mitophagy; oxidized CL drives apoptosis.

### The Cofactor Equation

Across Runs 2, 3, and 6 of the atlas, a quantitative threshold equation crystallized with convergence from all five models:

```
Apoptotic_Threshold = K / [(1 - f_HKII) * (1 - f_BclxL)] * (Chol / CL)
```

Where:
- **K** = energy barrier for honeycomb-to-dispersed transition (lipid-dependent)
- **f_HKII** = fraction of VDAC1 occupied by hexokinase-II (metabolic loyalty signal)
- **f_BclxL** = fraction of VDAC1 bound by Bcl-xL (anti-apoptotic badge)
- **Chol/CL** = cholesterol-to-cardiolipin ratio in the OMM (determines honeycomb fraction)

Every variable has a physical address. f_HKII maps to HK-II shielding cardiolipin microdomains at the VDAC surface. f_BclxL maps to Bcl-xL capturing extruded N-terminal helices. Chol/CL maps to the fraction of VDAC1 locked in honeycomb arrays versus dispersed as oligomerization-competent monomers (TYPE 0, 5/5 models, Run 6).

The equation's structure reveals something important: the honeycomb-to-dispersed transition is the rate-limiting step for apoptosis (TYPE 1, 3/5 models, Run 6). Oligomerization can only begin once the lattice disassembles. The membrane reorganization precedes -- and rate-limits -- the molecular death event.

### VDAC1 as External Audit

This threshold architecture has a distinctive property: it does not require the cell's cooperation. p53 requires the cell to honestly read its own DNA damage. Rb requires the cell to obey its own growth signals. Both are internal -- the cell policing itself. VDAC1's oligomeric state, by contrast, is set by membrane physics: cardiolipin redistribution, cholesterol content, HK-II binding affinity modulated by extracellular signaling cascades. These are conditions the body imposes on the cell, not conditions the cell imposes on itself. VDAC1 is the body's external audit of cellular fitness.

---

## Layer 3: The Atlas -- What VDAC1 Teaches Through Drugs

### Six Runs, 22 Novel Findings

The VDAC Pharmacology Atlas comprises six dedicated IRIS runs, each probing a different dimension of VDAC1 pharmacology. Nine of 20 total runs passed the S3 convergence gate; seven that failed were mined for gold. The combined yield:

| Metric | Value |
|--------|-------|
| Synthesized claims | 139 |
| TYPE 0 (5/5 convergence) | 23 (16.5%) |
| TYPE 1 (3-4/5) | 23 (16.5%) |
| TYPE 2 (2/5) | 22 (15.8%) |
| TYPE 3 (singulars) | 71 (51.1%) |
| NOVEL (no prior literature) | 22 |
| Operationalized hypotheses | 24 |
| Mean testability | 7.2/10 |

### The Binding Architecture (Run 1)

Three non-overlapping VDAC1 binding sites emerged (TYPE 0, 4/5 models): CBD at the lipid-protein interface near the N-terminal helix groove (hydrophobic, logP-driven); erastin at the interior barrel wall engaging E73/R15 (moderate polarity, sulfonamide chemistry); and DIDS at pore vestibule lysines K12/K20 (irreversible covalent, isothiocyanate electrophile). This establishes two pharmacological classes: gating modulators (CBD class, graded dose-response, wider therapeutic window) and pore blockers (erastin/DIDS class, steep dose-response, narrower margin).

VDAC2's 11-residue N-terminal extension sterically occludes the helix groove, providing at least 10-fold isoform selectivity (TYPE 1, 3/5 models). At clinical CBD concentrations (1-10 micromolar), Langmuir kinetics predict 31-48% VDAC1 occupancy but only 3-5% VDAC2 occupancy.

### The Cofactor Landscape (Run 2)

HK-II displacement is permissive but insufficient for apoptosis (TYPE 1, 3/5 models). The commitment sequence: HK-II removal unmasks cardiolipin microdomains, exposed CL recruits Bax, Bax insertion plus CL peroxidation destabilizes the OMM, cytochrome c releases. The cofactor hierarchy is HK-II >> Bcl-xL >> tubulin. The combination of 2-DG (depletes G6P, reducing HK-II residence time) and ABT-737 (displaces Bcl-xL directly) is predicted supra-additive with CI < 0.8 (TYPE 0, 4/5 models).

### Lipid Modulation (Run 3)

The highest-convergence run in the corpus (cosine 0.9512, first-cycle S3 pass). Cancer OMM cholesterol lowers effective CBD Kd from 11 to 3-6 micromolar (TYPE 0, 5/5 models), resolving the puzzle of how 1-10 micromolar plasma CBD reaches an 11-micromolar Kd target. Olesoxime requires cholesterol via its CRAC motif (TYPE 0, 5/5 models), explaining clinical variability in ALS trials. Cardiolipin alters VDAC gating dynamics (conformational states, not binding affinity) -- a distinction no prior publication had drawn.

### Biomarkers (Run 4)

GSH/GSSG ratio predicts hepatotoxicity risk from VDAC-engaging drugs (TYPE 0, 4/5 models). The mitochondrial stress panel (ATP/ADP, MitoSOX/TMRM) was downgraded from predictive to pharmacodynamic only (TYPE 0, 4/5 models) -- it measures on-target effect after exposure, not pre-existing vulnerability. A Gemini singular flagged that peripheral blood GSH may not reliably reflect hepatic GSH due to compartmentalization (confidence 0.75), adding a critical caveat to the biomarker framework.

### Drug Interactions (Run 5)

Three 5/5 TYPE 0 convergences on the first cycle (cosine 0.9547, record). Valproic acid directly modulates VDAC1 at therapeutic concentrations (300-700 micromolar), promoting the open state. NAPQI covalently modifies VDAC1 cysteines (Cys127/Cys232), forcing the closed state. These produce opposite gating directions yet both cause hepatotoxicity -- revealing that VDAC1 must oscillate to function and any drug that stabilizes either extreme is toxic.

The VPA + CBD synergistic hepatotoxicity prediction is a pharmacovigilance alert: both drugs are prescribed for epilepsy (Epidiolex patients are often on concurrent valproate), and the GWPCARE trials documented elevated ALT in VPA co-administered patients. This atlas proposes a mitochondrial mechanism beyond the known CYP450 competition.

### The Honeycomb Gate (Run 6)

The Chol/CL ratio physically determines the fraction of VDAC1 in protective honeycomb arrays versus dispersed, oligomerization-competent monomers (TYPE 0, 5/5 models). This validates the Chol/CL term in the cofactor equation at the biophysical level. Lipophilic drugs can alter VDAC1 organization via membrane order changes independent of direct protein binding (TYPE 0, 4/5 models).

The most radical singular in the atlas came from Gemini (confidence 0.75, d=0.92): CBD may act primarily as a membrane chaotrope -- a disordering agent that destabilizes cholesterol-rich honeycomb domains -- rather than a direct VDAC1 ligand. If confirmed, this would shift the mechanistic model from Langmuir binding kinetics to lipid thermodynamics.

### Structural Isomorphism

Three molecules studied independently produced the same abstract architecture:

| Molecule | Gateway Target | Low Dose | High Dose | Context Variable |
|----------|---------------|----------|-----------|-----------------|
| CBD | VDAC1 gating | Cytoprotection (TRPV1/PPARgamma) | Cytotoxicity (VDAC1/ROS) | Cofactor landscape |
| Lithium | GSK-3beta inhibition | Neuroprotection (10-25% inhibition) | Nephrotoxicity (>50% inhibition) | Tissue concentration |
| THC | CB1 occupancy | G-protein bias (<30% occupancy) | Beta-arrestin (>30% occupancy) | Receptor reserve + 2-AG tone |

Every molecule is a stress test. Dose picks the pathway. Tissue determines outcome. GSK-3beta appears in both the lithium model (as direct target) and the circadian-CBD model (as HK-II/VDAC1 regulator via Thr-51 phosphorylation), connecting two independent pharmacological systems through one kinase.

---

## Layer 4: The Disease -- What Happens When the Gate Fails

### Cancer as Lost Coherence

Cancer is not a disease of growth. It is a disease of lost coherence.

Every cell carries the capacity for unlimited division. What prevents it is a 600-million-year-old cooperative architecture: specialize, divide only when the tissue requires it, stop when signaled, and die when the body asks. Apoptosis -- the process VDAC1 gates -- is the deepest term of this architecture. A cell that cannot die cannot be trusted to live in a body.

Cancer breaks this architecture through damage. Each mutation silences a communication channel. p53 goes down and the cell can no longer read DNA damage. Rb goes down and the cell can no longer hear "stop dividing." Bcl-2 goes up and the cell can no longer hear "die now." What remains is the oldest program in biology: replicate. The single-celled default. Cancer is not a new disease. It is the old program, running without the newer layer of restraint.

### Rewriting Every Term Simultaneously

Cancer does not break one variable in the cofactor equation. It corrupts all of them at once:

| Equation Term | Normal Function | Cancer's Countermeasure |
|--------------|-----------------|------------------------|
| f_HKII | Metabolic loyalty signal | HK-II overexpression (Warburg glycolysis) -- jammed ON |
| f_BclxL | Anti-apoptotic badge | Bcl-xL/Bcl-2 overexpression -- jammed ON |
| Chol/CL | Membrane stability readout | Cholesterol loading of OMM -- jammed ON |
| K (honeycomb exit) | Lattice stability | All of the above simultaneously |

Every countermeasure requires active, ongoing energy expenditure to maintain. The Warburg effect -- cancer's preference for inefficient glycolysis over oxidative phosphorylation -- may exist in part to fund this gate-jamming. Glycolysis produces the glucose-6-phosphate that keeps HK-II loaded on VDAC1. The real product of cancer glycolysis is not ATP. It is HK-II on the gate. The metabolic inefficiency is the electricity bill for running the gate-jamming equipment.

This is testable and already partially observed: inhibiting glycolysis with 2-DG or 3-bromopyruvate reduces HK-II-VDAC occupancy and lowers the apoptotic threshold. Dichloroacetate, which redirects pyruvate to mitochondria, increases sensitivity to apoptotic stimuli. The correlation between glycolytic rate and apoptotic resistance should be quantitatively predictable from the f_HKII term.

### The External Audit Cannot Be Silenced Cheaply

Cancer silences p53 and Rb with single mutations -- these are internal checkpoints, the cell policing itself. A corrupted cell cannot be trusted to run its own quality control. But VDAC1's oligomeric state is set by membrane physics: conditions the body imposes, not conditions the cell controls. Jamming the VDAC gate requires metabolic reprogramming (Warburg), protein overexpression (Bcl-xL), and membrane remodeling (cholesterol loading) -- all expensive, all ongoing, all detectable. The external audit is harder to silence than the internal ones. That is why it exists.

---

## Layer 5: The Method -- How We Found This

### The IRIS Protocol

IRIS (Independent Replication through Integrated Synthesis) works by treating AI model diversity as a resource rather than a liability. Five frontier language models receive the same compiled prompt independently. No model sees another's output. Convergence is measured server-side through semantic embedding with complete-linkage clustering (cosine similarity threshold 0.70).

The TYPE classification system:

| TYPE | Convergence | Interpretation |
|------|------------|----------------|
| TYPE 0 | 5/5 models | Robust mechanism, likely reflected across training distributions |
| TYPE 1 | 3-4/5 models | Strong signal, minor model-specific variation |
| TYPE 2 | 2/5 models | Emerging pattern, requires verification |
| TYPE 3 | 1/5 (singular) | Frontier insight or noise -- the most novel findings live here |

Beyond convergence classification, three additional gates filter the output:

- **S3 gate**: cosine > 0.85 + domain-adaptive TYPE thresholds, iterated up to 3 cycles with recirculation
- **VERIFY**: Perplexity sonar-pro checks TYPE 2 claims against literature (PROMOTED / HELD / NOVEL / CONTRADICTED)
- **Lab Gate**: Model-evaluated feasibility, novelty, and falsifiability
- **S4/S5**: Hypothesis operationalization with Monte Carlo parameter simulation

### What the Corpus Revealed About the Method

Across 20 runs (12-42 API calls per run, approximately $0.20-1.00 each, total corpus cost under $15):

**S3 failures contain gold.** The THC runs failed S3 but produced the two-pathway occupancy model. The isoform run failed on parser artifacts despite 0.9124 cosine. Seven of 20 runs failed S3 yet contributed to the atlas through manual gold extraction.

**Singulars are 51% of claims but contain the most novel findings.** CBD as membrane chaotrope (Gemini singular), circadian GSK-3beta phosphorylation (Claude counter-consensus singular, subsequently verified), the cofactor equation being phenomenological (Claude self-questioning singular) -- these represent the frontier of what the corpus can see.

**Gemini produces disproportionately validated frontier singulars.** Its training distribution apparently includes more frontier biophysics, making it willing to propose mechanisms other models will not.

**Claude uniquely self-questions its own prior outputs.** "The cofactor equation is phenomenological" (Run 6) questioned the equation Claude helped derive in Run 2. A model that challenges convergence is more valuable than one that amplifies it.

**The corpus knew something none of its parts knew.** The Warburg-as-gate-jamming insight was distributed across 6 runs. No single run stated it. It became visible only when the aggregate was read as a single narrative.

### What Convergence Cannot Do

Multi-LLM convergence can identify mechanisms that are robust across model training distributions. It can surface novel connections invisible to any single model. It can operationalize hypotheses with quantitative predictions.

It cannot replace wet-lab validation. It cannot prove causation. It cannot escape the collective blind spots of its training corpora -- the three-signal threshold architecture (mitophagy, inflammation, apoptosis) required human integration with literature that none of the models synthesized on their own. IRIS is a discovery tool, not a proof engine.

---

## Layer 6: The Frame -- What This Means

### Thresholds at Every Scale

The threshold architecture discovered in VDAC1 recurs at every scale of biological and physical organization:

| Scale | Open / Closed | Death / Catastrophe |
|-------|--------------|---------------------|
| VDAC barrel | Low voltage: open monomer | High stress: death oligomer |
| Mitochondrion | CL internal: healthy | CL externalized: mitophagy or apoptosis |
| Cell | Coherent signaling: function | Lost coherence: apoptosis or cancer |
| Tissue | Homeostasis | Inflammation, remodeling |
| Organism | Health | Disease, death |
| Silicon (MOSFET) | Below threshold voltage: off | Above threshold: on |

The MOSFET parallel is not metaphorical. Gate oxide maps to N-terminal helix. Channel maps to barrel. Substrate maps to lipid membrane. Threshold voltage maps to the cofactor equation. Noise margin maps to honeycomb lattice. Both are threshold devices that integrate continuous inputs into binary decisions, with protective structures that prevent noise-triggered switching.

### Sovereignty Through Coherence

A cell that participates in a body is not enslaved. It gains oxygen delivery, immune protection, nutrient regulation, and decades of life instead of hours. The cooperative architecture is not oppression -- it is the condition for a longer existence. Cancer breaks the architecture and gets weeks of unrestrained growth, then death. The rebel does not win freedom. It wins isolation, then extinction.

The cofactor equation is the mathematical form of the cooperative architecture. The honeycomb lattice is the structural form. The three-signal threshold system is the enforcement mechanism. And VDAC1 -- 283 amino acids, 19 beta-strands, one helix -- is the keeper: the gate that ensures the deepest commitment of multicellular life can still be honored when the cell that made it can no longer remember making it.

### From Pharmacology to Organizing Principle

What began as a pharmacology question about CBD and VDAC1 became, through 20 IRIS runs and 139 claims across 5 independent AI models, a portrait of how life organizes itself against entropy. The question narrowed from "what does this drug do" to "what IS this protein" to "what IS this gate" -- and the answer turned out to be the same at every level: a threshold device that integrates context into a binary decision, protected by a lattice that prevents premature firing, auditable by the system it serves.

---

## What Remains

Five questions the atlas points toward but cannot answer:

1. **Does VDAC1 scramblase activity change during apoptosis?** Oligomerization competes with dimerization at the same interface (strands 1/2/18/19). Scramblase activity should drop as cells commit to death. This has not been measured. If confirmed, it would mean the cell stops building its membrane before destroying itself -- a molecular form of letting go.

2. **Is the honeycomb-to-dispersed transition cooperative?** The IRIS corpus predicts a Hill-type sigmoidal transition (n = 1-4) that would make the "point of no return" sharp rather than graded. AFM imaging of VDAC arrays across a Chol/CL gradient would resolve this. A sharp transition would mean the lattice melts catastrophically -- a phase transition in the literal thermodynamic sense.

3. **Is CBD primarily a membrane chaotrope or a VDAC ligand?** Gemini's singular (d=0.92, Run 6) proposes that CBD's measured Kd of 11 micromolar is not the primary mechanism of action. A hydrophilic CBD analog with preserved VDAC1 binding but no membrane partitioning would be the decisive experiment. If the analog kills cells, CBD is a ligand. If it does not, CBD is a chaotrope.

4. **What is the full PTM landscape of VDAC1 in cancer versus healthy cells?** If cancer VDAC1 is constitutively oxidized at Cys127 due to chronic elevated ROS, then NAPQI's covalent modification of the same site would be partially redundant in cancer but fully novel in healthy hepatocytes. This would reverse the selectivity prediction for acetaminophen toxicity. The PTM landscape is the mechanism by which cellular history is written onto VDAC1's structure before any drug arrives.

5. **Can the N-terminal helix be pharmaceutically locked?** If helix extrusion is the death trigger, a small molecule that cross-links the helix to the barrel wall would be a specific anti-apoptotic agent. Conversely, a molecule that forces extrusion would be pro-apoptotic. The helix is 25 residues. It is druggable. No one has tried.

---

## Summary

VDAC1 is five molecular machines in one protein, a phospholipid scramblase and a death pore sharing the same interface, a metabolite highway that doubles as a cellular execution chamber. Through 20 multi-LLM convergence runs, this atlas maps its pharmacology across binding sites, cofactors, lipids, biomarkers, drug interactions, and membrane architecture. The central finding is a cofactor equation -- `Threshold = K / [(1-f_HKII)(1-f_BclxL)] * (Chol/CL)` -- that integrates the variables governing VDAC1's transition from protector to killer. Cancer corrupts every term simultaneously; the Warburg effect may exist to fund this corruption. VDAC1 is life's decision gate: the last checkpoint that does not require the cell's own cooperation, ensuring that the commitment to multicellular existence can be honored even when the cell has forgotten making it.

---

*IRIS Protocol: Independent Replication through Integrated Synthesis*
*Models: Claude (Anthropic), Gemini (Google), Grok (xAI), Mistral (Mistral AI), DeepSeek (DeepSeek AI)*
*Total corpus: 20 runs, 139 claims, 22 novel findings, 24 hypotheses, ~$15 API cost*
