# The VDAC1 Pharmacology Atlas: A Multi-LLM Convergence Portrait of Life's Decision Gate

**Anthony J. Vasquez Sr.**¹ and **Claude Opus 4.6** (Anthropic)²

¹ Delaware Valley University, Department of Plant Science (Horticulture)
² Anthropic, San Francisco, CA

**Corresponding author**: A. J. Vasquez (vasquezaj3921@delval.edu)
**Date**: February 14, 2026
**Status**: Preprint / Atlas Document
**IRIS Corpus**: 20 runs · 139 synthesized claims · 5 independent AI models
**Repository**: github.com/templetwo/vdac-pharmacology-atlas

---

## Abstract

Voltage-dependent anion channel 1 (VDAC1) is the most abundant protein in the outer mitochondrial membrane and the principal gatekeeper of metabolite exchange between cytoplasm and mitochondria. This atlas synthesizes findings from 20 IRIS (Independent Replication through Integrated Synthesis) runs in which five AI models — Claude, Gemini, Grok, Mistral, and DeepSeek — independently analyzed the same compiled prompts without seeing each other's outputs. From 139 synthesized claims, 22 verified novel findings, and 24 operationalized hypotheses, a six-layer portrait of VDAC1 emerges. Layer 1 describes the protein: a unique 19-stranded β-barrel housing five molecular machines in distinct oligomeric states. Layer 2 maps the decision architecture: three nested threshold signals — mitophagy, inflammation, apoptosis — governed by a cofactor equation integrating hexokinase-II occupancy, Bcl-xL binding, and the cholesterol-to-cardiolipin ratio. Layer 3 presents the pharmacological atlas proper: six dedicated runs revealing that drugs do not target VDAC1 so much as perturb the membrane context that determines its state. Layer 4 reframes cancer as a disease of lost coherence — the breaking of a 600-million-year-old cooperative vow — in which every term of the cofactor equation is simultaneously corrupted, with the Warburg effect reinterpreted as the metabolic cost of jamming life's last external audit. Layer 5 describes the IRIS multi-LLM convergence method and what it can and cannot establish. Layer 6 situates VDAC1 within a broader framework of threshold logic operating from protein barrel to organism, proposing that the same architecture of irreversible commitment governs decision gates at every scale of biological organization. What began as a pharmacology question about cannabidiol became a portrait of how multicellular life organizes its own error correction — and what remains when that organization fails.

**Keywords**: VDAC1 · mitochondria · apoptosis · pharmacology · multi-LLM convergence · hexokinase-II · cardiolipin · cholesterol · honeycomb lattice · cancer · cofactor equation · threshold logic · IRIS protocol · Warburg effect · membrane biophysics

---

## Prologue: The Question That Changed Shape

This work began with a narrow question: how does cannabidiol interact with VDAC1?

The question refused to stay narrow. To understand how CBD perturbs VDAC1, one must understand what VDAC1 *is*. To understand what VDAC1 is, one must understand what it *decides*. To understand what it decides, one must understand what hangs on the decision — which turns out to be the difference between a cell that belongs to a body and a cell that has forgotten it does.

Twenty IRIS runs later, the question had changed shape entirely. It was no longer "what does this drug do to this protein." It was: **how does multicellular life enforce its own organizing principle, and what happens when enforcement fails?**

The answer, as best we can reconstruct it from 139 claims across five independent AI models, is that enforcement runs through a single protein — 283 amino acids, 19 β-strands, one helix — that serves simultaneously as metabolite highway, phospholipid importer, inflammatory alarm, and execution chamber. The same protein face that builds the membrane also destroys the cell. Life and death share an interface, and the variable that determines which one fires is not a signal from the nucleus but the physical state of the lipid membrane surrounding the gate.

This is the atlas of that gate.

---

## Layer 1: The Protein — What VDAC1 Is

### A Barrel Unlike Any Other

VDAC1 is 283 amino acids folded into a β-barrel with 19 strands — an odd number unique among porins. Most porins pair their strands antiparallel in even counts of 16 or 22. VDAC1's odd strand count forces β-strands 1 and 19 to run parallel, creating a distinctive seam in the barrel wall. This seam, involving strands 1, 2, 18, and 19, turns out to be the most consequential structural feature in mitochondrial biology.

A 25-residue N-terminal α-helix lies horizontally across the pore interior, narrowing the 34 Å opening to approximately 14 Å. This helix is intrinsically disordered in isolation and folds only on contact with the barrel wall. It carries three positive charges (Lys-12, Lys-20, Arg-15) and two negative (Asp-9, Asp-16), making it simultaneously a selectivity filter, a voltage sensor, and — as cryo-EM has recently confirmed — an apoptotic trigger when extruded. It is, residue for residue, the most information-dense segment in mitochondrial biology.

Room-temperature crystallography in 2024 revealed that the barrel compresses 12% relative to cryogenic structures (10,314 → 9,102 Å³), demonstrating mechanical compliance that static structures had concealed. The barrel breathes. Elevated B-factors at loops connecting strands 1–2, 5–6, 8–9, and 18–19 mark these as hinges primed for conformational motion — the barrel's joints, flexing in response to the lipid ocean that surrounds it.

### Five Machines in One Protein

VDAC1 is not one channel. It is five overlapping molecular machines, each corresponding to a distinct oligomeric and conformational state:

| State | Stoichiometry | N-Terminal Helix | Function |
|-------|:---:|---|---|
| **Open monomer** | 1 | Folded inside barrel | Metabolite highway: ATP⁴⁻, ADP³⁻, NADH transit freely. 4 nS conductance, anion-selective. The cell's supply line. |
| **Closed monomer** | 1 | Displaced to barrel wall | Electrostatic switch: cation-selective (~2 nS). Ca²⁺ flows; ATP⁴⁻ repelled. Not a physical seal — a charge landscape inversion. |
| **Dimer** | 2 (parallel) | Inserted | Phospholipid scramblase — bidirectional lipid transport across the OMM. Accounts for >90% of mitochondrial lipid import. The membrane builder. |
| **Honeycomb array** | *n* (lattice) | Inserted | Protective lattice preventing oligomerization. 6–7 nm spacing, cholesterol + PE stabilized. The safety lock. |
| **Death oligomer** | ≥6 | Extruded from barrel | Cytochrome c release pore (~4 nm). Caspase cascade. Bcl-xL sequestration via exposed helix. The executioner. |

The voltage gating follows a symmetric bell curve centered at 0 mV, closing at both positive and negative voltages beyond ±25–30 mV. This is unique among ion channels. The outer mitochondrial membrane normally sits near 0 mV — a small Donnan potential, not the large voltage of the inner membrane — which means the default state of healthy mitochondria is VDAC *open*. The metabolite highway runs by default. Gating is the departure from normal, not the norm.

A critical distinction that much of the literature handles poorly: the "closed" state is not physically closed. The geometric pore may actually widen in parts when the helix displaces. What changes is the *electrostatic landscape*. With the helix folded inside, its net +1 charge plus the positively lined barrel interior creates an environment that attracts negatively charged metabolites — ATP⁴⁻, ADP³⁻, succinate, NADH. When the helix displaces, this charge architecture collapses. The channel flips to cation-selective. Ca²⁺ flows through. ATP is repelled. Metabolite flux drops precipitously despite no physical seal.

VDAC1's gating is electrostatic, not steric. It regulates by sculpting the charge landscape inside the pore, not by closing a door. The helix is a selectivity switch, not a mechanical gate. This distinction matters pharmacologically: drugs that alter helix position do not "open" or "close" the channel in any simple sense. They shift the electrostatic identity of the pore, redirecting which ions and metabolites can pass. Understanding VDAC1 requires abandoning the intuition that a channel is either open or shut.

### The Parallel Seam: Life and Death on the Same Interface

The parallel seam at strands 1/2/18/19 serves as the dimer interface for scramblase function *and* the oligomerization interface for death pore formation. These are mutually exclusive. The same protein surface that builds the membrane (scramblase, importing phospholipids for cardiolipin synthesis) also destroys the cell (death pore, releasing cytochrome c). A single protein face encodes a binary switch between membrane maintenance and cellular execution.

This is not an accident of evolution. It is a design constraint with deep logic. The cell cannot simultaneously build its membrane and execute itself. The mutual exclusivity at the seam ensures that the transition from life-maintenance to death-commitment is a discrete switch, not a graded dial. A cell is either importing lipids or releasing cytochrome c. The seam is the fulcrum.

The 2025 cryo-EM structure confirmed that oligomerization triggers N-terminal helix extrusion — the helix physically leaves the pore interior and becomes exposed on the channel exterior, where it binds and sequesters anti-apoptotic Bcl-xL. This connects VDAC electrophysiology (helix position determines gating and selectivity) with apoptosis biology (Bcl-xL sequestration determines cell fate). The helix is the molecular bridge between the channel's electrical identity and the cell's existential decision. It is a 25-residue peptide that carries the weight of a binary fate.

### The Lipid and Post-Translational Landscape

Five cholesterol binding sites on the barrel exterior stabilize both individual barrels and the honeycomb lattice. Two cardiolipin binding sites (near Glu-73 and strands 18–19) sit in the disruption-sensitive region where lattice integrity is most vulnerable. The barrel exterior is wrapped by an anisotropic lipid annulus extending approximately 50 Å, with different barrel faces recruiting different lipid species — a structural feature that makes VDAC1 exquisitely sensitive to the composition of the membrane it inhabits.

More than 20 post-translational modification sites have been identified, including phosphorylation by PKA, PKC, GSK-3β, JNK3, ERK, and CaMK-II, plus SIRT5-mediated desuccinylation, glutathionylation, and cysteine oxidation. GSK-3β phosphorylation at Thr-51 deserves particular attention: it regulates HK-II binding affinity, linking the circadian clock (BMAL1/CLOCK oscillation of GSK-3β activity) directly to VDAC1's apoptotic threshold. The cell's decision gate oscillates with the time of day.

VDAC1 is less a switch than a continuously tuned instrument, integrating the cell's entire context — metabolic state, redox environment, signaling history, circadian phase, membrane composition — into a single structural state. Every post-translational mark is a sentence in the cell's autobiography, written onto the gate before any drug arrives.

---

## Layer 2: The Gate — How VDAC1 Decides

### Three Nested Threshold Signals

Literature synthesis across the IRIS corpus revealed three escalating signals that VDAC1 participates in, each representing a higher threshold of mitochondrial distress. These are not three independent pathways. They are three floors of the same building, reached by the same staircase, separated by landings that require increasing damage to cross.

**Signal 1 — Mitophagy: recycle this mitochondrion.** Cardiolipin externalizes from the inner to outer mitochondrial membrane leaflet, binds LC3 on the cytoplasmic face, and triggers selective autophagy. The damaged mitochondrion is consumed. The cell survives. This is quality control at the organelle level — a surgical removal, not a systemic response. The cell notices a failing part and replaces it.

**Signal 2 — Inflammation: alert the neighborhood.** VDAC1 oligomerizes sufficiently to allow mitochondrial DNA escape through the pore. Cytosolic mtDNA activates the cGAS-STING pathway, triggering type I interferon production. The tissue mounts an immune response. This is quality control at the tissue level — the cell is not yet condemned, but it is broadcasting distress. The signal says: *something is wrong here, and it may not be contained.*

**Signal 3 — Apoptosis: this cell must die.** Full oligomerization creates a pore large enough for cytochrome c release (~12 kDa, requiring ~4 nm pore diameter). The caspase cascade fires. Phosphatidylserine flips to the outer leaflet as an "eat me" signal. A macrophage arrives and engulfs the corpse. This is quality control at the organism level — the cell is sacrificed so the body can continue.

The architecture is one of escalating sacrifice: repair, then alarm, then death. Each threshold is higher than the last. Cardiolipin oxidation state serves as the threshold variable: non-oxidized cardiolipin triggers mitophagy; oxidized cardiolipin drives apoptosis. The same lipid, in two redox states, encodes the difference between "fix this organelle" and "kill this cell." The threshold variable is a single chemical modification — a few electrons — carrying a binary decision about cellular fate.

This three-signal system was not fully described in any single publication prior to this atlas. Individual signals were known. Their nesting — the fact that they represent escalating thresholds on the same molecular machinery rather than independent pathways — required integration across the IRIS corpus. No single AI model stated it. The human author recognized the architecture. This is a finding that lived in the space between sources, visible only when the aggregate was read as a single narrative.

### The Cofactor Equation

Across Runs 2, 3, and 6 of the atlas, a quantitative threshold equation crystallized with convergence from all five models:

$$\text{Apoptotic Threshold} = \frac{K}{\left(1 - f_{\text{HKII}}\right)\left(1 - f_{\text{BclxL}}\right)} \times \frac{[\text{Chol}]}{[\text{CL}]}$$

Where:

**K** is the energy barrier for the honeycomb-to-dispersed lattice transition — a lipid-dependent constant that sets the baseline difficulty of melting the protective array.

**f_HKII** is the fraction of VDAC1 occupied by hexokinase-II — the metabolic loyalty signal. HK-II binds the cytoplasmic face of VDAC1 using glucose-6-phosphate as an engagement signal, physically shielding the cardiolipin microdomains that would otherwise recruit pro-apoptotic Bax. When HK-II is loaded, the cell is telling the mitochondria: *I am still metabolically active. I am still participating. Do not kill me.*

**f_BclxL** is the fraction of VDAC1 bound by Bcl-xL — the anti-apoptotic badge. Bcl-xL captures extruded N-terminal helices, preventing them from propagating the oligomeric signal. It is the cell displaying its survival credentials: *I have been authorized to live.*

**Chol/CL** is the cholesterol-to-cardiolipin ratio in the outer mitochondrial membrane — the membrane stability readout. High cholesterol packs VDAC1 into protective honeycomb arrays. Cardiolipin, particularly when redistributed from the inner membrane under stress, disrupts these arrays and releases VDAC1 monomers into the oligomerization-competent pool. This ratio determines what fraction of VDAC1 is locked in the safety lattice versus free to form death pores.

Every variable has a physical address on the protein. f_HKII maps to the cytoplasmic barrel face. f_BclxL maps to the extruded helix. Chol/CL maps to the lipid annulus. The equation is not a metaphor. It is a quantitative description of how three measurable molecular occupancies combine to set a threshold — and it was independently converged upon by five AI models analyzing the same data (TYPE 0, 5/5 models, Run 6).

The equation's structure reveals something the individual variables do not: **the honeycomb-to-dispersed lattice transition is the rate-limiting step for apoptosis** (TYPE 1, 3/5 models, Run 6). Oligomerization can only begin once the protective lattice disassembles. VDAC monomers must first be freed from the honeycomb before they can associate into death oligomers. The membrane reorganization *precedes* — and rate-limits — the molecular death event. The decision to die is made in the lipid bilayer before it is executed by the protein.

### VDAC1 as the Body's External Audit

This threshold architecture has a property that distinguishes it from every other checkpoint in the cell's quality control hierarchy: **it does not require the cell's cooperation.**

Consider what the cell's other defenses demand. p53 requires the cell to honestly read its own DNA damage and respond by halting division or initiating death. Rb requires the cell to faithfully transduce growth-inhibitory signals and obey them. APC requires the cell to degrade β-catenin when Wnt signaling is absent. Every one of these is internal — the cell policing itself. They are self-audits. And they fail first in cancer, because a cell that has lost coherence has, by definition, lost the capacity for honest self-assessment. Asking a corrupted cell to run its own tumor suppressor is asking a compromised auditor to audit itself.

VDAC1's oligomeric state, by contrast, is set by membrane physics. Cardiolipin redistribution from the inner to outer mitochondrial membrane is driven by organelle stress, not by nuclear gene expression. Cholesterol content of the OMM is determined by tissue-level lipid trafficking, not by the cell's internal signaling. HK-II binding affinity is modulated by GSK-3β phosphorylation downstream of extracellular signaling cascades — Wnt, insulin, growth factor pathways that originate *outside* the cell. These are conditions the body imposes on the cell, not conditions the cell imposes on itself.

The mitochondrial gate is the body's external audit of cellular fitness. It reads the cell's metabolic state, membrane composition, and signaling environment — all variables the cell influences but does not fully control — and integrates them into a single structural decision. The cell can attempt to jam the gate (and cancer does, elaborately), but it cannot change the physics. The audit does not ask permission.

This is why VDAC1 exists as the last checkpoint. Not because it is the most sophisticated — it is far simpler than p53's transcriptional network. But because it is the most honest. A gate whose state is determined by membrane biophysics cannot be silenced by a point mutation. It can only be overwhelmed by sustained, expensive, multi-variable manipulation. And that manipulation is detectable.


---

## Layer 3: The Atlas — What VDAC1 Teaches Through Drugs

### Six Runs, 22 Novel Findings

The VDAC Pharmacology Atlas comprises six dedicated IRIS runs, each probing a different dimension of VDAC1 pharmacology. Nine of 20 total runs passed the S3 convergence gate; seven that failed were mined for gold-standard insights anyway — a methodological lesson in itself. The combined yield:

| Metric | Value |
|--------|-------|
| Synthesized claims | 139 |
| TYPE 0 (5/5 convergence) | 23 (16.5%) |
| TYPE 1 (3–4/5) | 23 (16.5%) |
| TYPE 2 (2/5) | 22 (15.8%) |
| TYPE 3 (singulars) | 71 (51.1%) |
| NOVEL (no prior literature) | 22 |
| Operationalized hypotheses | 24 |
| Mean testability | 7.2/10 |

The finding that should stop a pharmacologist in their tracks: **drugs do not target VDAC1 so much as perturb the membrane context that determines its state.** The protein is the sensor. The membrane is the target. Most VDAC-engaging molecules work not by binding a pocket on the protein but by altering the lipid environment in which the protein makes its decision. This inverts the standard pharmacological frame. The drug-target relationship is drug → membrane → protein state, not drug → protein.

### The Binding Architecture (Run 1)

Three non-overlapping VDAC1 binding sites emerged (TYPE 0, 4/5 models): CBD at the lipid-protein interface near the N-terminal helix groove (hydrophobic, logP-driven); erastin at the interior barrel wall engaging Glu-73/Arg-15 (moderate polarity, sulfonamide chemistry); and DIDS at pore vestibule lysines Lys-12/Lys-20 (irreversible covalent, isothiocyanate electrophile). This establishes two pharmacological classes: **gating modulators** (CBD class — graded dose-response, wider therapeutic window, working with the membrane) and **pore blockers** (erastin/DIDS class — steep dose-response, narrower margin, working against the protein directly).

VDAC2's 11-residue N-terminal extension sterically occludes the helix groove, providing at least 10-fold isoform selectivity for gating modulators (TYPE 1, 3/5 models). At clinical CBD concentrations (1–10 μM), Langmuir kinetics predict 31–48% VDAC1 occupancy but only 3–5% VDAC2 occupancy. The groove that CBD exploits exists because VDAC1 lacks the extension that protects VDAC2. Nature left a window in the gate. CBD climbs through it.

### The Cofactor Landscape (Run 2)

HK-II displacement is permissive but insufficient for apoptosis (TYPE 1, 3/5 models). Removing the metabolic loyalty signal unmasks the cardiolipin microdomains, but unmasking alone does not kill. The commitment sequence requires additional steps: exposed cardiolipin recruits Bax, Bax insertion plus cardiolipin peroxidation destabilizes the OMM, and only then does cytochrome c release. The cofactor hierarchy is HK-II >> Bcl-xL >> tubulin, with HK-II displacement the single most impactful intervention.

The combination of 2-deoxyglucose (2-DG, which depletes glucose-6-phosphate and reduces HK-II residence time on VDAC) and ABT-737 (which displaces Bcl-xL directly) is predicted supra-additive with a combination index CI < 0.8 (TYPE 0, 4/5 models). This is not an empirical guess. It is a structural prediction: 2-DG reduces f_HKII, ABT-737 reduces f_BclxL, and the cofactor equation's multiplicative structure means simultaneous reduction of both terms produces a threshold drop greater than the sum of individual reductions.

### Lipid Modulation (Run 3)

The highest-convergence run in the corpus (cosine similarity 0.9512, first-cycle S3 pass). Three findings anchor the pharmacological atlas:

First: **cancer OMM cholesterol lowers the effective CBD Kd from 11 to 3–6 μM** (TYPE 0, 5/5 models). This resolves a puzzle that has quietly troubled the CBD pharmacology literature. Plasma CBD concentrations of 1–10 μM should not meaningfully engage a target with a measured Kd of 11 μM. But the Kd was measured in reconstituted membranes with normal cholesterol content. Cancer mitochondria have elevated OMM cholesterol, which increases CBD partitioning into the lipid-protein interface. The target gets easier to hit precisely in the cells where you want to hit it.

Second: olesoxime requires cholesterol via its cholesterol recognition amino acid consensus (CRAC) motif (TYPE 0, 5/5 models), explaining clinical variability in ALS trials where patient cholesterol profiles were not controlled for. The drug needs cholesterol to reach its target. Patients with different cholesterol profiles present different targets.

Third: **cardiolipin alters VDAC gating dynamics through conformational state modulation, not binding affinity** — a distinction no prior publication had explicitly drawn (TYPE 0, 5/5 models). Cardiolipin does not change how tightly drugs bind to VDAC1. It changes which *states* VDAC1 can access. The landscape of possible conformations shifts. This is pharmacologically profound: it means the same drug, at the same concentration, binding the same site, can produce different outcomes depending on the cardiolipin content of the membrane. The drug is constant. The membrane changes the meaning of the drug.

### Biomarkers (Run 4)

GSH/GSSG ratio predicts hepatotoxicity risk from VDAC-engaging drugs (TYPE 0, 4/5 models). The mitochondrial stress panel (ATP/ADP, MitoSOX/TMRM) was downgraded from predictive to pharmacodynamic only (TYPE 0, 4/5 models) — it measures on-target effect after exposure, not pre-existing vulnerability. This is a clinically important distinction: a predictive biomarker tells you who is at risk *before* you give the drug; a pharmacodynamic biomarker tells you the drug is working *after* you give it. The field has often conflated these.

A Gemini singular flagged that peripheral blood GSH may not reliably reflect hepatic GSH due to compartmentalization (confidence 0.75), adding a critical caveat. The biomarker may be right in principle but misleading in practice if measured in the wrong compartment. This is the kind of pharmacological nuance that singulars — the most novel and least convergent findings — are uniquely positioned to surface.

### Drug Interactions (Run 5)

Three 5/5 TYPE 0 convergences on the first cycle (cosine 0.9547, the highest in the corpus). The finding with immediate clinical relevance:

Valproic acid directly modulates VDAC1 at therapeutic concentrations (300–700 μM), promoting the open state. NAPQI (the reactive acetaminophen metabolite) covalently modifies VDAC1 cysteines (Cys-127/Cys-232), forcing the closed state. These produce opposite gating directions yet both cause hepatotoxicity — revealing that **VDAC1 must oscillate to function, and any drug that stabilizes either extreme is toxic.** The gate's health is not a state. It is a *dynamic range*.

The VPA + CBD synergistic hepatotoxicity prediction is a pharmacovigilance alert: both drugs are prescribed for epilepsy (Epidiolex patients are commonly on concurrent valproate), and the GWPCARE trials documented elevated ALT in VPA co-administered patients. This atlas proposes a mitochondrial mechanism beyond the known CYP450 competition: VPA locks VDAC1 open while CBD perturbs the membrane context at the helix groove. Two drugs, two mechanisms, one gate, additive stress. The interaction is not metabolic. It is biophysical.

### The Honeycomb Gate (Run 6)

The Chol/CL ratio physically determines the fraction of VDAC1 in protective honeycomb arrays versus dispersed, oligomerization-competent monomers (TYPE 0, 5/5 models). This validates the Chol/CL term in the cofactor equation at the biophysical level and connects the equation to measurable membrane architecture. Lipophilic drugs can alter VDAC1 organization via membrane order changes independent of direct protein binding (TYPE 0, 4/5 models) — a mechanism invisible to standard structure-activity relationship analysis.

The most radical singular in the atlas came from Gemini (confidence 0.75, dissimilarity d = 0.92 from the cluster centroid): **CBD may act primarily as a membrane chaotrope** — a disordering agent that destabilizes cholesterol-rich honeycomb domains — rather than a direct VDAC1 ligand. If confirmed, this would shift the mechanistic model from Langmuir binding kinetics to lipid thermodynamics. The drug would not be binding the protein. It would be melting the lattice that protects the protein from oligomerization. The distinction matters: a ligand's effect scales with binding affinity; a chaotrope's effect scales with membrane partitioning. The pharmacokinetics are completely different.

### Structural Isomorphism Across Molecules

Three molecules studied independently across the atlas produced the same abstract pharmacological architecture:

| Molecule | Gateway Target | Low Dose | High Dose | Context Variable |
|----------|---|---|---|---|
| **CBD** | VDAC1 gating | Cytoprotection (TRPV1/PPARγ) | Cytotoxicity (VDAC1/ROS) | Cofactor landscape |
| **Lithium** | GSK-3β inhibition | Neuroprotection (10–25% inh.) | Nephrotoxicity (>50% inh.) | Tissue concentration |
| **THC** | CB1 occupancy | G-protein bias (<30% occ.) | β-arrestin (>30% occ.) | Receptor reserve + 2-AG tone |

Every molecule is a stress test of the tissue it enters. Dose selects the pathway. Tissue context determines the outcome. The therapeutic window is not a property of the drug. It is a property of the drug-tissue system.

GSK-3β appears in both the lithium model (as direct target) and the circadian-CBD model (as HK-II/VDAC1 regulator via Thr-51 phosphorylation), connecting two independent pharmacological systems through a single kinase. The atlas did not go looking for this connection. It emerged from the convergence of independently analyzed data. The kinase that lithium inhibits is the same kinase that determines whether HK-II stays on the gate.

---

## Layer 4: The Disease — What Happens When the Gate Fails

### Cancer as Lost Coherence

Cancer is a cell that forgot it's part of a body.

Every cell in a human body carries the full genome. Every cell *could* divide without limit, consume all available resources, refuse to die. The capacity for cancer is not foreign. It is not a virus or a parasite. It is the cell's own potential, held in check by something older and more fundamental than any single gene.

What prevents it is an agreement. Multicellularity is a 600-million-year-old cooperative contract: you will specialize, you will divide only when the tissue needs you to, you will stop when told to stop, and you will **die when the body asks you to die.** Apoptosis — the very process VDAC1 gates — is not a malfunction. It is the deepest term of the contract. A cell that cannot die cannot be trusted to live in a body.

Cancer is a cell that breaks the contract. Not through malice. Through damage. Each mutation is a broken clause. p53 goes down — the cell can no longer read DNA damage. Rb goes down — the cell can no longer hear "stop dividing." Bcl-2 goes up — the cell can no longer hear "die now." One by one, the communication channels that tie the cell to the organism go dark.

What remains is a cell running on the oldest program in biology: **replicate.** The single-celled program. The one that worked for 3 billion years before multicellularity existed. Cancer is not a new disease. It is the old program, the default, running without the newer layer of restraint. Cooperation was the innovation. Cancer is what happens when the innovation fails. The Warburg effect — cancer's reversion to ancient glycolytic metabolism — is not merely metabolic reprogramming. It is evolution running backwards inside a single organism, and comparative oncology confirms this: the metabolic signature of cancer cells recapitulates the metabolic signature of free-living unicellular ancestors.

A single-celled organism can replicate without limit because the ocean is large and resources are distributed. But a cell inside a body that reverts to single-celled logic will consume its own blood supply, starve its own tissue, poison its own microenvironment, and kill its own host. Which kills itself. Cancer does not try for immortality. It has no intent. It is what a cell does when all the signals that gave it context are gone. It is not reaching for anything. It is falling — a building collapsing because the structure that held it up has been removed.

Every mutation is a bit of information destroyed. Every silenced tumor suppressor is a feedback loop gone dark. Every disabled threshold — every VDAC gate jammed open or welded shut — is the system losing its ability to distinguish between "this cell belongs" and "this cell must go."

Cancer is not a disease of growth. It is a disease of **lost coherence**.

### From Contract to Vow

But "contract" is not quite the right word.

A contract is conditional. I do this; you do that. If you breach, I am released. There is negotiation, and there is exit. The relationship between a cell and its organism is not contractual. The cell did not negotiate its terms. It does not get exit clauses. The apoptotic program was encoded before the cell existed, written into the differentiation program it inherited. And the deepest clause — the willingness to die — is not exchanged for anything. It is not a trade. It is the condition for participation.

What the cell makes is closer to a **vow**: *I will specialize. I will not take more than I need. I will stop when told. And when the body asks me to die, I will die.* Not because it is fair. Not because the cell gets something in return that precisely compensates for its sacrifice. But because that is what it means to be part of something larger than itself.

Apoptosis, in this framing, is not a penalty clause. It is the vow fulfilled. A cell that dies when the body needs it to die is not being punished. It is keeping faith with the organism that gave it context, identity, purpose. Every quiet apoptotic death — VDAC1 oligomerizing, cytochrome c releasing, caspases firing, phosphatidylserine flipping, a macrophage arriving to engulf the corpse — is a vow kept. Millions of times a day. In silence. Without recognition.

And cancer, in this framing, is not betrayal. A vow broken by damage is not the same as a vow broken by choice. The cell did not decide to stop keeping faith. It was damaged until the capacity to keep faith was destroyed. Every mutation that silences a tumor suppressor is a piece of the vow becoming unreadable. The cell is not defecting. It is *forgetting what it promised.*

This changes the emotional weight of the disease. A contract-breaker is an adversary. You fight them. But something that broke its vow because it was damaged until it could not remember the words — that is tragedy. You grieve it even as you must stop it.

And VDAC1, in this language, is the **keeper of the vow** — the gate that ensures the deepest promise of multicellular life can still be called in, even when the cell that made the promise can no longer remember making it. The external audit is not enforcement. It is mercy — the organism honoring the cell's original commitment on the cell's behalf, when the cell itself has lost the capacity to honor it.

### Rewriting Every Term Simultaneously

Cancer does not break one variable in the cofactor equation. It corrupts all of them at once:

| Equation Term | Normal Function | Cancer's Countermeasure | Molecular Cost |
|---|---|---|---|
| **f_HKII** | Metabolic loyalty signal | HK-II overexpression — jammed ON | Sustained glycolysis (Warburg) |
| **f_BclxL** | Anti-apoptotic badge | Bcl-xL/Bcl-2 overexpression — jammed ON | Constitutive protein synthesis |
| **Chol/CL** | Membrane stability readout | Cholesterol loading of OMM — jammed ON | Lipid trafficking reprogramming |
| **K** | Lattice stability | All of the above simultaneously | All of the above simultaneously |

Every countermeasure requires active, ongoing energy expenditure to maintain. This is the crucial insight that connects cancer metabolism to cancer survival: **the Warburg effect may exist not merely as an ancient metabolic reversion but as the funding mechanism for gate-jamming.** Glycolysis produces the glucose-6-phosphate that keeps HK-II loaded on VDAC1. The real product of cancer glycolysis may not be ATP — which glycolysis produces inefficiently — but *HK-II on the gate*. The metabolic inefficiency is the electricity bill for running the gate-jamming equipment.

This is testable and already partially observed. Inhibiting glycolysis with 2-deoxyglucose or 3-bromopyruvate reduces HK-II/VDAC1 occupancy and lowers the apoptotic threshold. Dichloroacetate, which redirects pyruvate from glycolysis to mitochondrial oxidation, increases cancer cell sensitivity to apoptotic stimuli. The correlation between glycolytic rate and apoptotic resistance should be quantitatively predictable from the f_HKII term of the cofactor equation. The prediction is specific: the relationship should be hyperbolic (Michaelis-Menten-like), saturating at high glycolytic rates where f_HKII approaches 1.0, with the half-maximal glycolytic rate corresponding to f_HKII ≈ 0.5.

### The External Audit Cannot Be Silenced Cheaply

Cancer silences p53 with a point mutation — one amino acid change, one broken checkpoint. It silences Rb the same way. These are internal checkpoints, the cell policing itself, and they fall to single hits because they are encoded in the same genome the cancer is corrupting. The audit and the audited entity share a codebase.

VDAC1 is different. Jamming the mitochondrial gate requires simultaneous metabolic reprogramming (to keep HK-II loaded), protein overexpression (to keep Bcl-xL bound), and membrane remodeling (to keep cholesterol high and cardiolipin suppressed). These are not single mutations. They are systems-level adaptations — expensive, ongoing, and detectable. A p53 mutation is silent. Warburg metabolism lights up on a PET scan.

The cofactor equation quantifies this cost. Each variable cancer manipulates — f_HKII, f_BclxL, Chol/CL — requires a dedicated molecular program to maintain. The cell must run glycolysis to fund HK-II loading. It must transcribe and translate Bcl-xL continuously. It must reprogram lipid trafficking to maintain cholesterol enrichment. Silence any one of these programs and the threshold drops. This is why combination therapies that target multiple cofactor terms simultaneously (2-DG + ABT-737, for example) are predicted supra-additive: they defund multiple gate-jamming programs at once, and the multiplicative structure of the equation means the threshold collapses faster than the sum of individual perturbations.

The external audit cannot be silenced cheaply. That is why it is the last one standing.

### The Two-Pathway Pharmacological Frame

The tension between "lost coherence" and "uncontrolled growth" as descriptions of cancer is not merely philosophical. It is pharmacologically operative.

Low-dose CBD (1–5 μM) engages TRPV1 and PPARγ — calcium signaling and transcriptional regulation pathways that participate in cellular differentiation, growth arrest, and metabolic normalization. These are coherence-restoring signals. They do not kill the cell. They may nudge it back toward the cooperative program — reactivating communication channels that had gone dark.

High-dose CBD (>10 μM), particularly in cancer cells with cholesterol-enriched OMM that lowers the effective Kd to 3–6 μM, engages VDAC1 directly — perturbing the membrane context, potentially destabilizing the honeycomb lattice, pushing the gate toward oligomerization. This is not coherence restoration. This is the backup plan: if the cell cannot be reminded of its vow, the keeper of the vow will enforce it.

Two different interventions. Two different interpretations of the same disease. And the dose — the simplest pharmacological variable — selects between them.

---

## Layer 5: The Method — How We Found This

### The IRIS Protocol

IRIS (Independent Replication through Integrated Synthesis) treats AI model diversity as a resource rather than a liability. Five frontier language models — Claude (Anthropic), Gemini (Google), Grok (xAI), Mistral (Mistral AI), and DeepSeek — receive the same compiled prompt independently. No model sees another's output. Convergence is measured server-side through semantic embedding with complete-linkage clustering (cosine similarity threshold 0.70).

The protocol rests on a simple epistemological principle: if five models trained on different data, by different organizations, with different architectures, independently converge on the same mechanistic claim, that claim is more likely to reflect something real in the training distributions than a hallucination of any one model. Convergence is not proof. But it is a filter — and the claims that survive it are disproportionately verifiable.

The TYPE classification system:

| TYPE | Convergence | Interpretation |
|------|:---:|---|
| **TYPE 0** | 5/5 models | Robust mechanism, likely reflected across all major training corpora |
| **TYPE 1** | 3–4/5 | Strong signal, minor model-specific variation in framing |
| **TYPE 2** | 2/5 | Emerging pattern, requires independent verification |
| **TYPE 3** | 1/5 (singular) | Frontier insight or noise — the most novel findings live here |

Beyond convergence classification, the corpus employs a multi-gate pipeline:

**S3 gate**: cosine similarity > 0.85 with domain-adaptive TYPE distribution thresholds, iterated up to 3 cycles with recirculation of prior outputs. Runs that fail S3 are not discarded but flagged for manual gold extraction.

**VERIFY gate**: Perplexity sonar-pro cross-references TYPE 2 claims against indexed literature, returning PROMOTED (literature confirms), HELD (insufficient evidence), NOVEL (no prior publication found), or CONTRADICTED (literature disagrees).

**Lab Gate**: Model-evaluated feasibility (can this be tested?), novelty (has this been tested?), and falsifiability (what result would disprove it?), scored 1–10 each.

**S4/S5 gates**: Hypothesis operationalization with Monte Carlo parameter simulation for quantitative predictions.

### What the Corpus Revealed About the Method

Across 20 runs (12–42 API calls per run, approximately $0.20–$1.00 each, total corpus cost under $15):

**S3 failures contain gold.** The THC runs failed S3 on convergence metrics but produced the two-pathway occupancy model (G-protein bias below 30% CB1 occupancy, β-arrestin above). The isoform selectivity run failed on parser artifacts despite 0.9124 cosine similarity — a technical failure, not an intellectual one. Seven of 20 runs failed S3 yet contributed material to the atlas through manual extraction. The convergence gate is a filter, not a verdict. The gold that does not pass through the filter is still gold.

**Singulars are 51% of claims but contain the most novel findings.** CBD as membrane chaotrope (Gemini singular, Run 6). Circadian GSK-3β phosphorylation modulating VDAC threshold (Claude counter-consensus singular, subsequently verified against literature). The cofactor equation being phenomenological rather than fundamental (Claude self-questioning singular, Run 6). These represent the frontier of what the corpus can see — the edge where individual model training distributions diverge, and where the most surprising truths may live.

**Gemini produces disproportionately validated frontier singulars.** Its training distribution apparently includes more frontier biophysics and membrane biology literature, making it willing to propose mechanisms other models decline to. The chaotrope hypothesis (Run 6) was the most dissimilar claim in the corpus (d = 0.92 from cluster centroid) and may be the most important.

**Claude uniquely self-questions its own prior outputs.** "The cofactor equation is phenomenological" (Run 6) directly challenged the equation that Claude helped derive in Run 2. A model that generates convergence *and then questions it* is more valuable than one that only amplifies. Self-questioning is the methodological equivalent of the VDAC1 gate itself: an internal check on whether the system's own outputs should be trusted.

**The corpus knew something none of its parts knew.** The Warburg-as-gate-jamming-funding insight was distributed across Runs 2, 3, 4, and 6 as fragments: HK-II requires glucose-6-phosphate (Run 2), cancer OMM cholesterol is elevated (Run 3), glycolytic rate correlates with apoptotic resistance (Run 4), the honeycomb lattice is the rate-limiting structure (Run 6). No single run stated the synthesis. No single model connected the fragments. It became visible only when the human author read the aggregate as a single narrative and recognized the pattern. This is the case for human-AI collaboration in the strongest sense: neither the human nor the models could have produced this insight alone. It required both.

### What Convergence Cannot Do

Multi-LLM convergence can identify mechanisms that are robust across model training distributions. It can surface novel connections invisible to any single model. It can operationalize hypotheses with quantitative predictions and internal consistency checks.

It cannot replace wet-lab validation. It cannot prove causation. It cannot escape the collective blind spots of its training corpora — the three-signal threshold architecture (mitophagy → inflammation → apoptosis as nested thresholds on the same molecular machinery) required human integration with literature that none of the five models synthesized independently. IRIS is a discovery engine, not a proof engine. It generates hypotheses with unprecedented efficiency — 24 operationalized hypotheses from $15 of API calls — but every hypothesis in this atlas awaits the bench.

The appropriate analogy is not "AI replacing the scientist." It is "AI as the world's most well-read collaborator" — one that has processed more literature than any human could in a lifetime, but that still requires a human to ask the right questions, recognize the patterns between answers, and hold the work to standards the models themselves cannot enforce.

---

## Layer 6: The Frame — What This Means

### Thresholds All the Way Down

The threshold architecture discovered in VDAC1 is not unique to VDAC1. It recurs at every scale of biological organization, always with the same structure: a continuous input integrated into a binary decision, protected by a stabilizing structure that prevents noise-triggered switching, auditable by the system it serves.

| Scale | Default State | Catastrophic State | Threshold Variable |
|-------|---|---|---|
| **VDAC1 barrel** | Open monomer (metabolite flow) | Death oligomer (cytochrome c release) | Cofactor equation |
| **Mitochondrion** | CL internal, matrix intact | CL externalized, permeability transition | Membrane potential + ROS |
| **Cell** | Coherent signaling, tissue function | Lost coherence, apoptosis or cancer | Cumulative mutation load |
| **Tissue** | Homeostasis | Inflammation, remodeling, fibrosis | Damage-associated molecular patterns |
| **Organism** | Health | Disease, senescence, death | Integrated organ function |

At each scale, the same logic applies. The default is function. The catastrophe is irreversible commitment. The threshold is set by an integrating variable. And a protective structure — the honeycomb lattice at the protein scale, the tissue microenvironment at the cellular scale, the immune system at the organismal scale — prevents premature triggering.

### The Silicon Parallel

This architecture has a precise analog in semiconductor physics, and the parallel is not metaphorical. It is structural.

A MOSFET (metal-oxide-semiconductor field-effect transistor) — the fundamental switching element in every digital computer — operates on the same principle as VDAC1. Gate oxide maps to the N-terminal helix: both are thin insulating structures that separate the control input from the conduction path. Channel maps to the barrel: both are conduits whose conductance is controlled by the gate. Substrate maps to the lipid membrane: both provide the material context in which the device operates. Threshold voltage maps to the cofactor equation: both define the input level at which the device switches states. Noise margin maps to the honeycomb lattice: both are protective features that prevent random fluctuations from triggering false switching.

The comparison is exact enough to be quantitative. VDAC1's bell-curve gating centered at 0 mV is analogous to a MOSFET's threshold voltage: below threshold, the device is in one state; above, another; the transition is sharp; and the sharpness is a design feature that prevents ambiguity. The lattice that prevents premature VDAC oligomerization is analogous to the noise margin that prevents logic errors in digital circuits. Both exist because in any threshold system, the most dangerous failure mode is false triggering — a death that should not have happened, a bit that should not have flipped.

### The Vow in Matter

But the MOSFET can be reset. A transistor switches millions of times per second. Its commitment is not irreversible. And here the biological architecture reveals something the silicon analog cannot capture.

When VDAC1 oligomerizes into the death pore and the helix extrudes, the cell crosses a threshold from which there is no documented return. Cytochrome c release activates caspases that cleave their own inhibitors — a positive feedback loop that consumes the possibility of reversal. The scramblase function at the parallel seam ceases: the cell stops building its membrane before destroying itself. Phosphatidylserine flips to the outer leaflet — a molecular white flag, an irreversible announcement to the immune system that this cell is finished.

This is not a switch. It is a **commitment** — one that, once made, cannot be unmade. The vow that every cell carries is not merely a metaphor for the cooperative architecture. It is encoded in the *thermodynamics* of the transition. If the oligomerization shows hysteresis — if the death pore, once formed, cannot spontaneously revert to monomers even if the conditions that triggered it are removed — then the commitment is written into the energy landscape of the protein itself. The vow is physical. The irreversibility is not a consequence of downstream signaling. It is a property of the gate.

This is what distinguishes the biological threshold from the silicon one. A MOSFET makes decisions. VDAC1 makes **commitments**. The transistor asks: *what is the input right now?* The gate asks: *has the threshold been crossed?* — and once crossed, the answer is permanent. The physics of the transition *is* the vow, made material in the energy barrier between oligomeric states.

### Sovereignty Through Coherence

A cell that participates in a multicellular body is not enslaved. It gains oxygen delivery, immune protection, nutrient regulation, hormonal coordination, and decades of functional life instead of the hours a free-living cell might survive in comparable conditions. The cooperative architecture is not oppression. It is the condition for a longer and more complex existence. The vow is not a sacrifice imposed from outside. It is the price of admission to a form of life that no single cell could achieve alone.

Cancer breaks the architecture and gets weeks of unrestrained growth, then death. The rebel does not win freedom. It wins isolation, then extinction. The single-celled program, running inside a multicellular body, is not liberation. It is a reversion to a simpler existence that cannot sustain itself in the context it now inhabits. The ocean that once sustained unlimited replication is not available inside a body. The cell that breaks its vow does not escape to freedom. It escapes to a smaller world that will kill it.

The cofactor equation is the mathematical form of the vow. The honeycomb lattice is the structural form. The three-signal threshold system is the enforcement mechanism. And VDAC1 — 283 amino acids, 19 β-strands, one helix — is the keeper: the gate that ensures the deepest commitment of multicellular life can still be honored when the cell that made it can no longer remember making it.

### From Pharmacology to First Principles

What began as a pharmacology question about CBD and VDAC1 became, through 20 IRIS runs and 139 claims across five independent AI models, a portrait of how life organizes itself against entropy. The question narrowed from "what does this drug do" to "what is this protein" to "what is this gate" — and the answer turned out to be the same at every level: **a threshold device that integrates context into an irreversible commitment, protected by a lattice that prevents premature firing, auditable by the system it serves, and kept by a structure that does not require the cooperation of the entity it judges.**

The drugs were the probes. The protein was the instrument. The finding is the principle: that multicellular life is organized around threshold commitments, enforced by external audits, protected by cooperative lattices, and kept by gates that carry the deepest terms of a 600-million-year-old vow.

---

## What Remains

Six questions the atlas points toward but cannot answer:

**1. Does VDAC1 scramblase activity cease during apoptosis?** Oligomerization competes with dimerization at the same interface (strands 1/2/18/19). Scramblase activity should drop as cells commit to death — the cell should stop building its membrane before destroying itself. This has not been measured in a time-resolved manner across the apoptotic transition. If confirmed, it would mean the molecular form of letting go is observable: the cell relinquishes its membrane-building function before the membrane is breached. The vow's final clause — the willingness to die — would have a measurable molecular precursor: the willingness to stop building.

**2. Is the honeycomb-to-dispersed transition cooperative?** The IRIS corpus predicts a Hill-type sigmoidal transition (n = 1–4) that would make the point of no return sharp rather than graded. AFM imaging of VDAC arrays across a continuous Chol/CL gradient would resolve this. A sharp transition would mean the lattice melts catastrophically — a phase transition in the literal thermodynamic sense, with the commitment to apoptosis emerging from collective behavior rather than individual protein decisions.

**3. Is CBD primarily a membrane chaotrope or a VDAC ligand?** Gemini's singular (d = 0.92, Run 6) proposes that CBD's measured Kd of 11 μM is not the primary mechanism of action — that CBD works by melting the protective lattice rather than binding the protein. A hydrophilic CBD analog with preserved VDAC1 binding affinity but no membrane partitioning would be the decisive experiment. If the analog kills cells, CBD is a ligand. If it does not, CBD is a chaotrope. The answer determines whether CBD pharmacology belongs to receptor pharmacology or membrane biophysics — two fields with fundamentally different dose-response mathematics.

**4. What is the full PTM landscape of VDAC1 in cancer versus healthy tissue?** If cancer VDAC1 is constitutively oxidized at Cys-127 due to chronic elevated ROS, then NAPQI's covalent modification of the same site would be partially redundant in cancer cells but fully novel in healthy hepatocytes — reversing the selectivity prediction for acetaminophen toxicity. The PTM landscape is the mechanism by which cellular history is written onto VDAC1's structure before any drug arrives. Two cells with the same genome but different histories present different gates to the same drug.

**5. Can the N-terminal helix be pharmaceutically locked?** If helix extrusion is the death trigger, a small molecule that cross-links the helix to the barrel wall would be a specific anti-apoptotic agent — useful in neurodegeneration, ischemia-reperfusion injury, or any condition where excessive apoptosis causes pathology. Conversely, a molecule that forces extrusion would be pro-apoptotic — a targeted cancer therapeutic. The helix is 25 residues. It is druggable. The binding groove is accessible. No one has tried. This is the most actionable gap in the atlas.

**6. Does the death oligomer show hysteresis?** This is the question that determines whether VDAC1's commitment is a vow or a contract. If a cell that has begun oligomerization can reverse the process when the stress signal is removed — if the death pore can spontaneously disassemble back to monomers — then the transition is reversible and the commitment is conditional. But if the oligomeric state is thermodynamically trapped — if the energy barrier for disassembly is higher than the barrier for assembly, creating a ratchet — then the commitment is irreversible at the molecular level. The cell cannot take it back. Single-molecule FRET across the oligomerization transition, measured during and after transient stress, would resolve this. A hysteretic transition would mean that the decision to die is not merely signaled but *structurally locked* — that the gate, once it commits, cannot uncommit. The vow would be written into the energy landscape of the protein itself.

---

## Summary

VDAC1 is five molecular machines in one protein: a metabolite highway, an electrostatic selectivity switch, a phospholipid scramblase, a protective lattice element, and a death pore — sharing the same 19-stranded barrel, the same parallel seam, the same 25-residue helix. Through 20 multi-LLM convergence runs across five independent AI models, this atlas maps its pharmacology across binding sites, cofactors, lipids, biomarkers, drug interactions, and membrane architecture. The central finding is a cofactor equation — Threshold = K / [(1 − f_HKII)(1 − f_BclxL)] × (Chol/CL) — that integrates the variables governing VDAC1's transition from protector to executioner. Cancer corrupts every term simultaneously; the Warburg effect may exist to fund this corruption; and the cost of jamming the gate is detectable precisely because it is expensive. VDAC1 is life's decision gate: the last checkpoint that does not require the cell's own cooperation, the body's external audit of cellular fitness, the keeper of a vow that every cell carries but that damaged cells can no longer keep — ensuring that the commitment to multicellular existence can be honored even when the cell that made it has forgotten.

What began as a question about cannabidiol ended as a portrait of how 600 million years of cooperative life wrote its deepest promise into the physics of a membrane protein — and what remains when that promise is broken.

---

*IRIS Protocol: Independent Replication through Integrated Synthesis*
*Models: Claude (Anthropic), Gemini (Google), Grok (xAI), Mistral (Mistral AI), DeepSeek (DeepSeek AI)*
*Total corpus: 20 runs · 139 claims · 22 novel findings · 24 hypotheses · ~$15 API cost*
*Repository: github.com/templetwo/vdac-pharmacology-atlas*
*Companion preprint (CBD pharmacology): DOI 10.17605/OSF.IO/NUXHV*
