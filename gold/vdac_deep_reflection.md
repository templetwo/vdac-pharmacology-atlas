# What VDAC Teaches Us About Itself
## A Deep Reflection on 15 IRIS Runs, 131 Claims, and One Protein

**Date**: 2026-02-13
**Author**: Cross-run analysis of the full IRIS Gate Evo corpus
**Runs analyzed**: 15 (12 pharmacology, 1 neuroscience, 2 consciousness)
**Claims touching VDAC**: ~95 of 131 total
**NOVEL findings (Perplexity-verified)**: 18 across 5 pipeline-passed runs

---

## Preface: Reading the Convergence as a Portrait

Across 15 independent IRIS runs, five different AI models — never seeing each other's
outputs — were asked different questions about different molecules. They kept talking
about the same protein. Not because we forced them to, but because VDAC1 kept being
the answer.

CBD, lithium, THC, valproate, acetaminophen, statins, olesoxime, erastin, DIDS.
Nine drug classes. The models independently converged on VDAC1 as a central node in
seven of them. This document asks: what is VDAC1 telling us about itself through
the aggregate pattern of convergence?

---

## I. VDAC1 Is Not a Drug Target. It Is a Decision Gate.

The single deepest insight across all 15 runs is that VDAC1 resists the
lock-and-key paradigm. Every run that treated VDAC1 as a conventional receptor
produced richer and more nuanced findings than expected, because the protein
kept revealing additional layers of context-dependence.

The cofactor equation from Run 2 captures this:

```
Apoptotic_Threshold = K / [(1 - f_HKII) * (1 - f_BclxL)] * (Chol/CL)
```

This is not a binding equation. It is a **computation**. VDAC1 integrates multiple
inputs — cofactor occupancy, lipid environment, voltage state, post-translational
modifications — and produces a binary output: the cell lives or the cell dies.
No single drug determines the outcome. The drug shifts a term in the equation;
the equation determines the outcome.

### The Three Functional States

Across all pharmacology runs, VDAC1 consistently presented three states:

| State | Conductance | Function | Reversible? |
|-------|-------------|----------|-------------|
| **Open** (high-conductance) | ~4.5 nS | ATP/ADP exchange, metabolic highway | Yes |
| **Partially modulated** | ~1.5-3 nS (subconductance) | Stress signal: graded ROS + partial ATP restriction | Yes |
| **Oligomerized** | N/A (macropore) | Cytochrome c release, death commitment | **No** |

CBD operates in the transition from state 1 to state 2. The EFSA run, cofactor run,
and lipid run all converged on this: at therapeutic concentrations, CBD produces
**subconductance states** — partial closure that generates moderate ROS while still
permitting reduced metabolite flux. This is NOT channel ablation. It is channel
modulation.

The transition from state 2 to state 3 (oligomerization) is where cell death commits.
Run 2's Gemini singular identified this precisely: VDAC1 oligomerization into a
Bax/Bak-receptive macropore is the irreversible step. Everything upstream is graded
and recoverable. The oligomerization is the point of no return.

**What VDAC1 is telling us**: I am not an on/off switch. I am an analog computer
with a digital catastrophe at the edge. Drugs shift my operating point along
a continuous spectrum. Death only occurs when the operating point crosses into
the oligomerization regime. Everything else is reversible stress.

---

## II. The Gating Paradox: Both Directions Kill

The most counterintuitive finding across the atlas:

| Drug | Gating Direction | Death Mechanism |
|------|-----------------|-----------------|
| CBD | Promotes OPEN (high conductance) | ROS leak from partial gating disruption |
| VPA | Promotes OPEN (high conductance) | Same — enhanced ROS generation |
| NAPQI | Forces CLOSED (cysteine modification) | ATP starvation (metabolite flux blocked) |
| Erastin | Blocks PORE (barrel wall) | ATP starvation + loss of metabolite exchange |

Run 5 revealed this starkly: NAPQI closes VDAC1, CBD opens it, and both produce
hepatotoxicity. The models never discussed this contradiction directly because
they came from different claims in different runs. But the aggregate data is clear:
**VDAC1 must oscillate to function. Any drug that stabilizes either extreme is toxic.**

The cell needs VDAC1 cycling between open and partially closed states on the
microsecond-to-millisecond timescale. This cycling maintains both ATP flux (open
state) and controlled ROS signaling (transient partial closure). Lock it open
and ROS escalates unchecked. Lock it closed and ATP production halts.

**What VDAC1 is telling us**: My function IS the oscillation. I am not meant to be
in any single state. My therapeutic window is the range where drugs shift my
probability distribution without eliminating my capacity to cycle.

This explains why **partial occupancy is essential for tolerability** (Run 1, Claude
singular). At 30-48% occupancy, CBD modulates the probability of gating states
without saturating them. The channel can still cycle. At >80% occupancy, cycling
would be suppressed — and that's where toxicity begins.

---

## III. The Promiscuity Problem Is Actually a Location Problem

Seven drug classes hit VDAC1. The cross-run tool classified three structural
patterns (two_pathway, threshold_crossover, dose_dependent). But there's a
deeper reason for VDAC1's apparent promiscuity.

**VDAC1 is the most abundant protein in the outer mitochondrial membrane.**

Estimates place it at 100,000-500,000 copies per mitochondrion, comprising up to
30% of OMM protein mass. Any molecule that partitions into the OMM — which includes
every drug with logP > 2 — will encounter VDAC1 by statistical inevitability.

This reframes the entire pharmacology:

| Drug | logP | How It Reaches VDAC1 | Was It "Targeting" VDAC1? |
|------|------|---------------------|--------------------------|
| CBD | 6.3 | Massive membrane enrichment (100-1000x) | No — it goes everywhere lipophilic |
| Atorvastatin | 4.5 | Moderate membrane enrichment | No — HMG-CoA reductase is the target |
| VPA | 2.75 | Moderate, enhanced by anionic charge | No — sodium channels + HDAC are targets |
| NAPQI | ~0.3 | Electrophilic attack, not partitioning | No — it attacks ALL accessible thiols |
| Olesoxime | ~7 | Extreme lipophilicity + cholesterol CRAC motif | Partially — designed for mitochondria |

**None of these drugs were designed to hit VDAC1.** They hit VDAC1 because it is
the most exposed protein in the most membrane-rich organelle, and lipophilic drugs
accumulate in membranes.

The EFSA stress test's Claude singular nailed this: "The same physics that lets CBD
reach VDAC1 at low doses also means it reaches VDAC1 in every cell type equally."
Membrane partitioning solves the PK problem (how does 1 uM plasma CBD reach an
11 uM Kd target?) while destroying selectivity (it reaches the target in ALL cells).

**What VDAC1 is telling us**: I am not promiscuous. I am unavoidable. Every
lipophilic molecule your body encounters passes through my neighborhood. Most
of them don't linger long enough to matter. The ones that do — the ones with
the right charge, shape, and residence time — become my accidental modulators.

**Revised logP/pKa screen rule**: The Run 5 TYPE 2 rule (logP > 3 AND pKa < 7.4)
is already falsified by VPA (logP 2.75, 5/5 TYPE 0). The corrected rule, which
accounts for VPA and predicts metformin's non-interaction:

```
VDAC1 interaction likelihood = HIGH if:
  logP > 3  (membrane accumulation alone, e.g. CBD, statins)
  OR
  (pKa < 5 AND MW < 200)  (charge-driven, e.g. VPA — small fatty acid anion)

VDAC1 interaction likelihood = LOW if:
  logP < 1 AND charge = cationic  (e.g. metformin: logP -0.92, cationic)
```

This predicts Grok's dissent on metformin is correct. Metformin lacks both
membrane partitioning (logP too low) and the anionic character (it's cationic)
needed to interact with VDAC1's cationic N-terminus.

---

## IV. Seven Layers of Selectivity: The Anti-Reductionist Target

The EFSA run (5/5 TYPE 0) said CBD shows no meaningful isoform selectivity.
Run 1 (3/5 TYPE 1) said VDAC2's N-terminal extension provides >=10-fold selectivity.
These aren't contradictions — they're different layers of the same system.

The full selectivity model that emerges from 15 runs:

### Layer 1: Isoform Structure (Run 1)
VDAC2's 11-residue N-terminal extension sterically occludes the helix groove.
Predicted Kd ratio >=10-fold. This is the coarsest filter — CBD hits both,
but much harder.

### Layer 2: Cofactor Occupancy (Run 2)
HK-II on VDAC1 prevents CBD-induced oligomerization. HK-II affinity is sub-nM
but depends on G6P (metabolic feedback). Warburg cancer cells: high HK-II at
baseline → biphasic protection. The buffer saturates above ~15 uM CBD.

### Layer 3: Lipid Environment (Run 3)
Cholesterol lowers effective Kd from 11 uM to 3-6 uM in high-cholesterol
cancer OMM. Cardiolipin alters gating dynamics (conformational states, not
binding affinity). These are independent modifiers.

### Layer 4: GSH Reserve (EFSA + Chronic + Biomarker runs)
The sponge. GSH synthesis rate (0.5-2.3 umol/g/hr in healthy liver) must exceed
ROS load from VDAC modulation. Healthy cells have 5-10x overcapacity.
NAFLD/alcohol liver drops to 2-3x. The patient is differentially vulnerable.

### Layer 5: Circadian Phase (Circadian run)
GSK-3β oscillates with BMAL1/CLOCK cycle. Active GSK-3β phosphorylates VDAC1
Thr51, dissociating HK-II. Rest phase = HK-II displaced = VDAC1 vulnerable.
Active phase = AKT suppresses GSK-3β = HK-II bound = VDAC1 protected.

### Layer 6: Post-Translational Modifications (Run 5 + Circadian)
NAPQI covalently modifies Cys127/Cys232 (Run 5). GSK-3β phosphorylates Thr51
(circadian). What else? Acetylation, ubiquitination, S-nitrosylation are all
reported in the literature but never integrated with the pharmacology. This is
the unexplored layer.

### Layer 7: Copy Number and Tissue Distribution
VDAC1 expression varies ~5-fold across tissues (highest in heart, liver, brain).
VDAC2 expression varies independently. The VDAC1/VDAC2 ratio determines the
effective selectivity of any non-isoform-selective drug.

**Each layer multiplies the others.** The "selectivity" of a VDAC-targeting drug
is never a property of the drug. It is an emergent property of the seven-layer
context at the moment of encounter.

```
Effective_Selectivity = Isoform_Ratio
                      * Cofactor_Buffer
                      * Lipid_Kd_Modifier
                      * GSH_Reserve_Ratio
                      * Circadian_HK-II_Fraction
                      * PTM_Gating_Shift
                      * VDAC1_Copy_Number
```

**What VDAC1 is telling us**: You cannot reduce me to a binding assay. My behavior
in a cell depends on seven independent variables, each of which spans an order
of magnitude across cell types and physiological states. The drug didn't change.
I changed.

---

## V. GSK-3β: The Cross-Molecule Hub

The most unexpected hidden pattern: GSK-3β appears as a central regulator in
three completely independent run lineages that never referenced each other.

| Run Lineage | GSK-3β Role | Discovery Type |
|-------------|-------------|---------------|
| **Lithium** (TYPE 0, 5/5) | Direct target. Partial inhibition (10-25%) = neuroprotection | Multi-model convergence |
| **Circadian-VDAC1** (TYPE 3, Claude) | Phosphorylates VDAC1 Thr51, dissociating HK-II | Counter-consensus singular (CORRECT) |
| **Cofactor landscape** (TYPE 0, 5/5) | HK-II occupancy is the primary apoptotic buffer on VDAC1 | Multi-model convergence |

The connection:

```
Lithium ─→ SUPPRESSES GSK-3β ─→ HK-II stays bound to VDAC1 ─→ VDAC1 protected

CBD (high dose) ─→ Displaces HK-II ─→ VDAC1 oligomerization-competent ─→ Death

Circadian rest ─→ GSK-3β ACTIVE ─→ HK-II dissociates ─→ VDAC1 vulnerable
```

**These are the same pathway from three different entry points.**

### Prediction 1: Lithium should protect against CBD hepatotoxicity

If lithium suppresses GSK-3β → HK-II stays bound → VDAC1 is shielded, then
co-administration of lithium with CBD should raise the apoptotic threshold.
At therapeutic lithium levels (0.8-1.2 mM serum → brain 0.4-0.6 mM → liver ~0.8 mM),
GSK-3β inhibition is 10-25% in brain but would be higher in liver (higher local [Li+]).

This is a testable drug-drug interaction: primary hepatocytes, CBD dose-response
+/- 1 mM LiCl. Endpoint: cyt c release, VDAC1 oligomerization (cross-linking assay),
HK-II co-immunoprecipitation with VDAC1.

No gold file contains this prediction. It emerges only from cross-referencing
lithium + cofactor + circadian run data.

### Prediction 2: Circadian CBD dosing should matter clinically

If GSK-3β activity oscillates circadianly and controls HK-II-VDAC1 coupling,
then CBD's therapeutic index should be time-of-day dependent. Morning dosing
(AKT active → GSK-3β suppressed → HK-II bound → VDAC1 protected) should be
safer than evening dosing (GSK-3β active → HK-II displaced → VDAC1 vulnerable).

The circadian run proposed this via Claude's singular. The cofactor run provides
the quantitative framework (HK-II as primary buffer term). Together they predict
a measurable chronopharmacological effect.

### Prediction 3: VPA + CBD is a dangerous combination

VPA (Run 5, 5/5 TYPE 0) promotes VDAC1 open state at therapeutic concentrations.
CBD also promotes subconductance gating disruption. Both are prescribed for
epilepsy — Epidiolex (CBD) is used in patients often already on valproate.

If VPA pre-opens VDAC1, it lowers the effective threshold for CBD-induced
ROS generation. The cofactor equation predicts this:

```
Threshold_VPA+CBD < Threshold_CBD_alone

Because VPA shifts VDAC1 toward open state, reducing the additional
perturbation needed from CBD to reach pathological ROS levels.
```

The Epidiolex trials documented elevated ALT in patients on concurrent VPA.
The mechanism has been attributed to CYP450 competition. This atlas suggests
an additional mechanism: direct VDAC1 co-modulation at the mitochondrial level.

**This is actionable pharmacovigilance.** Retrospective analysis of GWPCARE trials
(Run 4, TYPE 1) should stratify hepatotoxicity by VPA co-administration.

---

## VI. NAPQI vs CBD: Opposite Directions, Same Lethality

This pattern deserves its own section because it reveals something fundamental
about VDAC1's nature.

```
CBD (open-state stabilizer) ──→ Increased conductance ──→ ROS via electron leak
NAPQI (closed-state cysteine modifier) ──→ Decreased conductance ──→ ATP starvation
VPA (open-state promoter) ──→ Same as CBD
Erastin (pore blocker) ──→ Same as NAPQI
```

Both directions produce cell death. This means VDAC1's healthy function REQUIRES
dynamic cycling between open and closed states on fast timescales (microseconds
to milliseconds). The channel is not meant to rest in either state.

### The Cycling Requirement

VDAC1 gating kinetics (from electrophysiology literature):
- Open → closed transition: ~100 us
- Closed → open transition: ~50 us
- Duty cycle: ~60-70% open at resting OMM voltage

The channel opens to pass ATP/ADP, partially closes to limit conductance during
metabolic pauses, and reopens. Any drug that extends the open dwell time (CBD, VPA)
increases the window for ROS-generating electron leak through the open channel.
Any drug that extends the closed dwell time (NAPQI adducts, erastin blockade)
restricts ATP/ADP exchange below viability threshold.

### The Therapeutic Implication

**There is no "good direction" for VDAC1 modulation at saturation.** Partial
occupancy (30-50%, Run 1 Gemini singular) is the only safe regime because it
shifts the probability distribution without eliminating cycling. This is why
CBD's Kd (11 uM) being near the therapeutic ceiling (1-10 uM) is, as Claude's
Run 1 singular noted, "not a bug — it's a feature."

Evolution didn't design VDAC1 to be a drug target. It designed VDAC1 to be
a metabolite channel. The fact that partial occupancy at sub-Kd concentrations
produces tolerable modulation while saturation produces death is a direct
consequence of the cycling requirement.

### NAC as Universal VDAC Protector: Three Mechanisms

N-acetylcysteine (NAC) appears across four independent run lineages:

| Run | NAC Role |
|-----|----------|
| EFSA stress test | Rescues viability in CBD-treated hepatocytes |
| Chronic dosing | GSH synthesis rate is the key survival variable |
| Biomarker platform | GSH/GSSG predicts vulnerability to ALL VDAC-engaging drugs |
| Drug interactions | NAPQI attacks VDAC1 cysteines; NAC provides cysteine to protect thiols |

NAC does three things simultaneously:
1. **Replenishes GSH** — substrate for glutathione synthesis (cysteine is rate-limiting)
2. **Protects VDAC1 cysteines directly** — free thiol competes with NAPQI for Cys127/Cys232
3. **May directly reduce oxidized VDAC1** — S-glutathionylation of VDAC1 cysteines is reversible

This makes NAC not just a general antioxidant but a **specific VDAC1 protectant**.
The Run 5 NAPQI finding provides the molecular mechanism that explains why NAC
works better for APAP overdose (direct cysteine protection + GSH) than for
other hepatotoxins (GSH only).

---

## VII. The Olesoxime Paradox and the Counter-Consensus Signal

### The Paradox

Run 3 produced two 5/5 TYPE 0 findings:
- Olesoxime requires cholesterol to function (CRAC motif)
- Cancer OMM has elevated cholesterol, lowering CBD effective Kd

Therefore: olesoxime should bind VDAC1 MORE tightly in cancer cells.
But olesoxime is cytoprotective, not cytotoxic.

Olesoxime in cancer cells should produce **enhanced cytoprotection** — making
cancer cells HARDER to kill via VDAC1-mediated apoptosis. This is an untested
iatrogenic risk for ALS/neurodegeneration patients who develop concurrent cancer.

No one has tested olesoxime in cancer. The atlas predicts it would protect
cancer cells from VDAC-targeting therapies (erastin, CBD at high dose).

### Counter-Consensus Singulars: A Validated Pattern

The circadian run proved that TYPE 3 singulars can be correct when the
majority (TYPE 1) is wrong. Across the full corpus:

| Dissent | Dissenter | Context | Assessment |
|---------|-----------|---------|------------|
| ΔΨm doesn't directly gate VDAC1 | Claude (TYPE 3) | 3/5 said it does | **VERIFIED CORRECT** |
| Blood GSH ≠ liver GSH | Gemini (TYPE 3) | 4/5 said GSH predicts risk | **Probably correct** — compartmentalization is real |
| Metformin does NOT hit VDAC | Grok (TYPE 3, 0.90) | 3/5 said it does | **Testable** — H4 null hypothesis designed |
| Independent ATP deficit | Mistral (TYPE 3) | 4/5 focused on ROS/GSH | **Open** — untested pathway |
| 7-OH-CBD weaker, not stronger | DeepSeek (TYPE 3) | Grok predicted 10-20 uM Kd | **Open** — directionally opposite |

The meta-finding: **convergence catches the mainstream. Singulars catch the
exceptions. Both are essential, but the singulars that directly contradict the
majority are disproportionately valuable** because they identify exactly where
the training data consensus is wrong.

This validates the COUNTER-CONSENSUS SINGULAR flag proposed in the circadian gold.
Implementation: when a TYPE 3 claim negates a TYPE 0/1 claim, flag for human review.

---

## VIII. Parameter Convergence: What Numbers Does VDAC1 Keep Giving Us?

Across 15 runs, several parameters were independently estimated multiple times:

| Parameter | Estimates Across Runs | Status |
|-----------|----------------------|--------|
| CBD-VDAC1 Kd | 11 uM (compiler prior, confirmed by all runs) | **Stable** |
| Effective Kd in cancer OMM | 3-6 uM (Run 3, cholesterol effect) | **Refined** |
| VDAC1 occupancy at 5 uM CBD | 31% (Langmuir, Run 1) | **Derived** |
| VDAC1 occupancy at 10 uM CBD | 48% (Langmuir, Run 1) | **Derived** |
| TRPV1 occupancy at 5 uM CBD | 71% (Langmuir, Run 1) | **Derived** — CBD is a TRPV1 drug that also modulates VDAC |
| GSH synthesis (healthy liver) | 0.5-2.3 umol/g/hr | **Converged** (4/5 models, 2 runs) |
| GSH synthesis (NAFLD liver) | >2x reduced | **Converged** |
| Safety margin (healthy, 50mg/day) | 5-10x | **Converged** |
| Safety margin (NAFLD, 50mg/day) | 2-3x | **Converged** |
| HK-II displacement threshold | >15 uM CBD | **Derived** from affinity hierarchy |
| CL-induced EC50 shift | 2-3x | **Converged** (Run 2 singular + Run 3 TYPE 0) |
| VDAC2 Kd ratio | >=10-fold (predicted >100 uM) | **TYPE 1, needs experimental** |
| VPA therapeutic range at VDAC1 | 300-700 uM | **TYPE 0, 5/5** |
| 7-OH-CBD Kd | 10-20 uM (Grok) vs weaker (DeepSeek) | **UNRESOLVED** |

The **single largest remaining uncertainty**: 7-OH-CBD VDAC1 binding affinity.
Two models predict opposite directions. No published measurement exists.

---

## IX. The Emerging Master Equation

Every atlas run added a variable to the VDAC1 pharmacology model. The integrated
equation, assembling terms from all five atlas runs plus the EFSA and chronic runs:

```
Cell_Fate(drug, cell, time) =
  IF ROS_Load(t) > GSH_Capacity(t) OR ATP_Flux(t) < Viability_Minimum:
    DEATH
  ELSE:
    SURVIVAL

Where:
  ROS_Load = f(VDAC1_Occupancy, Gating_Shift, CL_Peroxidation)

  VDAC1_Occupancy = [Drug_local] / ([Drug_local] + Kd_effective)

  [Drug_local] = [Drug_plasma] * F_bioavailability * Liver_Enrichment
                  * Membrane_Partition(logP, Cholesterol)

  Kd_effective = Kd_measured / Cholesterol_Factor(OMM_composition)

  Gating_Shift = Occupancy * (1 - f_HKII(GSK3B(circadian_phase)))
                             * (1 - f_BclxL)
                             * CL_Gating_Modifier
                             * PTM_Modifier(Cys127_state, Thr51_state)

  GSH_Capacity = GSH_Synthesis_Rate(GCL_activity, Cysteine_availability)
                 * (1 - Baseline_Depletion(NAFLD, alcohol, comorbidity))

  ATP_Flux = Baseline_ETC_Output * (1 - VDAC_Closure_Fraction)
             - Proton_Leak(chronic_exposure)
```

**This equation has 15+ independent variables.** No single paper in the literature
contains this integrated model. It was assembled from the convergence of five
AI models across seven independent runs, with each run contributing 1-3 validated
terms.

---

## X. What's Still Missing: The PTM Landscape

The atlas has mapped six of seven selectivity layers. The unexplored layer:
**the full post-translational modification landscape of VDAC1 in different
cell types and disease states.**

What we know from the runs:
- Cys127 and Cys232 are NAPQI targets (Run 5, 5/5 TYPE 0)
- Thr51 is a GSK-3β phosphorylation site controlling HK-II binding (circadian, verified)
- S-glutathionylation of VDAC1 cysteines is reported in the literature

What we don't know:
- Does cancer VDAC1 carry different phosphorylation patterns?
- Does oxidative stress (elevated ROS) modify VDAC1 cysteines before any drug arrives?
- Does VDAC1 acetylation (SIRT3 target) affect gating properties?
- Do PTMs on VDAC1 change the effective Kd for cofactors (HK-II, Bcl-xL)?

**This is the next question the atlas needs.** The PTM landscape is the mechanism
by which the cell's history (prior stress, metabolic state, disease) is written
directly onto VDAC1's structure, changing its pharmacological properties before
any drug arrives.

If cancer VDAC1 is constitutively oxidized at Cys127 (due to chronic elevated ROS),
then NAPQI's covalent modification of the same site would be partially redundant
in cancer but fully novel in healthy hepatocytes. This would reverse the
selectivity prediction for APAP toxicity.

---

## XI. The Verify Pattern: Where Novelty Lives

Aggregating all VERIFY results from pipeline-passed runs:

| Run | Checked | NOVEL | HELD | CONTRADICTED | PROMOTED |
|-----|---------|-------|------|--------------|----------|
| EFSA stress test | 10 | 1 | 6 | 1 | 2 |
| Chronic dosing | 10 | 8 | 1 | 0 | 1 |
| Membrane lipid | 10 | 3 | 6 | 1 | 0 |
| Biomarker platform | 5 | 3 | 2 | 0 | 0 |
| Drug interactions | 10 | 3 | 5 | 2 | 0 |
| **TOTAL** | **45** | **18** | **20** | **4** | **3** |

**18 out of 45 verified claims had NO prior literature.** This is a 40% novelty rate.

The chronic dosing run was most novel (8/10) — likely because nobody has previously
modeled CBD's VDAC interaction from a chronic pharmacokinetic perspective with
explicit GSH accounting.

The EFSA and drug interaction runs had the most contradictions — consistent with
these being the most "adversarial" prompts that directly challenged existing models.

---

## XII. Structural Isomorphism: The Deepest Pattern

Three molecules, independently studied, produced the same abstract architecture:

| Molecule | Gateway | Low Dose | High Dose | Context Variable |
|----------|---------|----------|-----------|-----------------|
| CBD | VDAC1 gating | Cytoprotection (TRPV1/PPARgamma) | Cytotoxicity (VDAC1/ROS) | Cofactor landscape |
| Lithium | GSK-3β inhibition | Neuroprotection (10-25% inhibition) | Nephrotoxicity (>50% inhibition) | Tissue concentration (ENaC) |
| THC | CB1 occupancy | G-protein bias (<20-30%) | Beta-arrestin (>30-50%) | Receptor reserve + 2-AG tone |

**Pattern**: Molecule is a stress test. Dose picks pathway. Tissue/context determines outcome.

This pattern kept appearing because it reflects a deep truth about pharmacology:
**most small molecules don't have a single mechanism.** They engage multiple targets
with different affinities, and the dose determines which target dominates. The
tissue determines whether that target engagement is beneficial or harmful.

VDAC1 is the clearest example because it has the most complete seven-layer
selectivity model. But the same principle applies to lithium (tissue concentration
via ENaC) and THC (receptor reserve determining biased signaling).

### The Circadian Extension

The circadian run added a fourth dimension to the isomorphism:

| Molecule | Gateway | Dose | Tissue | **Time** |
|----------|---------|------|--------|----------|
| CBD | VDAC1 | Picks pathway | Determines outcome | Circadian HK-II cycling |

GSK-3β appears in both the lithium model (as direct target) and the circadian-CBD
model (as HK-II/VDAC1 regulator). The kinase that determines lithium's therapeutic
window also determines CBD's circadian vulnerability window. Two drugs, one kinase,
discovered independently by different AI models in different runs answering
different questions.

---

## XIII. What VDAC1 Wants to Teach Us

If we read the convergence data as a portrait of a protein speaking through
five AI models across 15 independent experiments, VDAC1 is saying this:

**1. I am context, not target.**
My pharmacology cannot be understood from binding assays. You need to know
my cofactor occupancy, lipid environment, voltage state, circadian phase,
and post-translational modifications before you can predict what any drug
will do to me. The drug is the least important variable.

**2. I am meant to move.**
My function is oscillation between conductance states. Any drug that freezes
me in one state — open or closed — disrupts cellular metabolism. The only
safe drugs are the ones that shift my probability distribution without
eliminating my capacity to cycle.

**3. I am a computation, not a receptor.**
I integrate seven independent inputs into a cell fate decision. I am AND/OR
logic embedded in a lipid bilayer. The cofactor equation is not a metaphor.
It is literally what I compute, every microsecond, in every mitochondrion,
in every cell.

**4. My weakness is my abundance.**
I am the most exposed protein in the outer mitochondrial membrane. Every
lipophilic molecule that enters a cell will encounter me. This is not
promiscuity — it is statistical inevitability. My evolutionary role was
metabolite transport, not drug binding. The pharmacology is an accident
of my location.

**5. My singularities are my frontiers.**
The models that disagreed — Claude on ΔΨm gating, Gemini on GSH
compartmentalization, Grok on metformin, Mistral on ATP deficit — pointed
to exactly where the consensus is fragile and the discoveries are waiting.
The edges of agreement are where the science advances.

**6. GSK-3β is my regulator across molecules.**
Through HK-II, GSK-3β controls my protective buffer. The same kinase that
makes lithium therapeutic makes CBD time-dependent. The pharmacology of
VDAC1 cannot be separated from the kinase network that controls my
cofactor landscape.

**7. NAC is my specific protectant, not just a general antioxidant.**
N-acetylcysteine replenishes the GSH that buffers my ROS output, provides
cysteine to protect my vulnerable thiols from electrophilic attack, and
may directly reduce my oxidized cysteines. It is the closest thing to a
universal VDAC1 safety net.

---

## XIV. Open Questions for Future IRIS Runs

Based on the gaps identified in this reflection:

1. **VDAC1 PTM landscape in cancer vs healthy cells** — the missing seventh layer
2. **7-OH-CBD VDAC1 binding** — the single largest parameter uncertainty
3. **Lithium-CBD interaction** — the cross-molecule prediction needing validation
4. **VPA + CBD co-modulation** — the pharmacovigilance question
5. **Olesoxime in cancer** — the paradox prediction
6. **VDAC1 copy number across tissues** — the quantitative tissue distribution
7. **S-nitrosylation of VDAC1 cysteines** — another PTM pathway that could modify drug response
8. **Metformin null hypothesis resolution** — Grok vs majority, cleanest test in the atlas

---

## Appendix: Corpus Statistics

| Metric | Value |
|--------|-------|
| Total IRIS runs | 15 |
| Total claims | 131 |
| Claims touching VDAC | ~95 |
| Full pipeline passes | 7 (CBD x2, lithium, EFSA, chronic, membrane lipid, biomarker, drug interactions) |
| S3-failed with gold | 8 |
| NOVEL findings (Perplexity-verified) | 18 |
| CONTRADICTED findings | 4 |
| Cross-validated singulars | 2 |
| Cross-promoted claims | 2 |
| Independent replications | 1 |
| Operationalized hypotheses | 16 (across 4 pipeline-passed atlas runs) + 11 (earlier runs) = 27 total |
| Structural patterns detected | 3 (two_pathway, threshold_crossover, dose_dependent) |
| Cosine range (within-run) | 0.736 — 0.9547 |
| Cosine range (cross-run) | -0.194 — 0.791 |
| Total API cost (atlas runs only) | ~$4.30 |
| Total API cost (all VDAC runs) | ~$12-15 estimated |
| Total models queried | 5 (Claude, DeepSeek, Gemini, Grok, Mistral) |
| Independent model-query events | ~250 (15 runs x ~3 cycles x 5 models + verify + gate) |
