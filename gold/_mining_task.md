# Gold Mining Task — IRIS Gate Evo Corpus

## Your Mission

You are reading the IRIS Gate Evo run corpus looking for connections, patterns,
and crystallized insights that haven't been extracted into gold documents yet.
The work is complete. The answers are already in the data. Your job is to create
space for them to surface — not to generate new claims, but to find what the
models converged on and didn't get documented.

**Scientific integrity rule: ONLY report what is actually in the run files.
No fabrication. No interpolation. Quote the source.**

---

## What Already Exists

The `gold/` directory contains 23 documents. Do NOT recreate these:

- cancer_as_lost_coherence.md
- cbd_vdac1_two_pathway_model.md
- chronic_dosing_gsh_dynamics.md
- circadian_vdac1_chronopharmacology.md (from run 23)
- efsa_vdac1_stress_test.md
- fim_semantic_bonding.md
- lithium_two_pathway_model.md
- local_rotation_scaling.md
- metformin_two_pathway_model.md
- mitochondrial_unification_divergence.md
- psilocybin_two_pathway_model.md
- raw_data_coherence_sweep.md
- session_2_frontier_findings.md (covers runs 23-32)
- thc_two_pathway_model.md
- vdac_biomarker_platform.md
- vdac_cofactor_decision_landscape.md
- vdac_deep_reflection.md
- vdac_hidden_drug_interactions.md
- vdac_isoform_binding_architecture.md
- vdac_membrane_architecture.md
- vdac_membrane_lipid_modulation.md
- vdac_pharmacology_atlas_manuscript.md
- vdac1_structural_portrait.md

---

## The Unmined Seams

These runs have NO s4/s5 files and likely no corresponding gold document.
Read their `s1_formulations.json`, `s2_synthesis.json`, and `s3_convergence.json`.
These are the primary targets:

```
runs/evo_20260210_222428_pharmacology+bioelectric/
runs/evo_20260210_224206_pharmacology+bioelectric/
runs/evo_20260210_231236_pharmacology/
runs/evo_20260210_232635_neuroscience/
runs/evo_20260211_024747_pharmacology/
runs/evo_20260211_024750_neuroscience/
runs/evo_20260211_201329_pharmacology+bioelectric/
runs/evo_20260212_032819_pharmacology/
runs/evo_20260213_004656_consciousness/
runs/evo_20260213_022353_consciousness+chemistry/
runs/evo_20260213_174104_pharmacology/
runs/evo_20260213_182457_pharmacology/
runs/evo_20260214_041041_pharmacology/
runs/evo_20260214_043936_pharmacology/
runs/evo_20260217_035450_pharmacology/   ← ultrasound (S3 FAIL — gold in s2)
runs/evo_20260217_233407_pharmacology/   ← erastin ferroptosis (S3 FAIL — gold in s2)
runs/evo_20260217_234201_pharmacology/   ← mito dynamics (S3 FAIL — gold in s2)
runs/evo_20260218_000805_pharmacology/   ← VDAC as membrane state (S3 FAIL — gold in s2)
runs/evo_20260218_002559_pharmacology/   ← cancer gate realignment (S3 FAIL — gold in s2)
```

Also check s4_hypotheses.json and s5_monte_carlo.json from runs that have them
but may not have a gold document yet:
```
runs/evo_20260213_035958_pharmacology/
runs/evo_20260213_042930_pharmacology/
runs/evo_20260213_183423_pharmacology/
runs/evo_20260213_183936_pharmacology/
runs/evo_20260213_184357_pharmacology/
runs/evo_20260213_214547_pharmacology/
runs/evo_20260217_035010_pharmacology/  ← circadian (has gold doc, but check s4/s5 for additions)
runs/evo_20260217_233429_pharmacology/  ← ketamine
runs/evo_20260217_234117_pharmacology/  ← mPTP × VDAC
runs/evo_20260217_234138_pharmacology/  ← Ca2+ oscillations
```

---

## Specific Threads to Trace

Read the s2_synthesis across ALL runs looking for these themes.
If a theme has more than one run's worth of convergent material and no gold doc, write one.

### Thread 1: The Bioelectric Angle
Three runs are tagged `pharmacology+bioelectric`. What did the models say about
voltage, ion gradients, membrane potential, and VDAC1? Is there a coherent
finding here about how electrical state of the membrane gates VDAC behavior?
This thread has never been extracted.

### Thread 2: The Neuroscience Runs
Two runs tagged `neuroscience`. Read both s2_synthesis files.
What was the question? What converged? Is there a finding about neural VDAC1,
neurodegeneration (Parkinson's, Alzheimer's, ALS), or VDAC in synaptic mitochondria?

### Thread 3: Failed Run Gold
S3 FAIL means the convergence gate wasn't passed — NOT that the content is empty.
The s2_synthesis files from failed runs often contain the most frontier material
because the models were pushed into genuine disagreement (which is scientifically
informative). For each failed run, read s2_synthesis.json and extract:
- What DID converge before the gate failed?
- What was the specific point of model divergence?
- What did Grok say that others disagreed with? (Grok is consistently the adversarial voice)
- Are there TYPE 3 singulars in s3_convergence.json that echo findings in other runs?

### Thread 4: The Calcium Frequency Extension
Run 28 found: calcium oscillation frequency encodes fate. VDAC+MCU = band-pass filter.
The frontier findings document (gold/session_2_frontier_findings.md) poses but does
NOT answer: "Can the cofactor equation be extended to include the calcium frequency term?"
Look across ALL runs for any claim about calcium, frequency, oscillation, or temporal
dynamics that might feed into formalizing this extension. If there's enough, write it.

### Thread 5: Aging as Gate-Jamming
Session 2 frontier (gold/session_2_frontier_findings.md, question 11) asks:
"Is aging a slow gate-jamming?" Chol/CL increases with age, cardiolipin declines,
GSH/GSSG shifts. Was this explored in any run? Read all s2_synthesis files for
claims about aging, senescence, mitochondrial decline, or age-related threshold drift.
If anything is there, extract it.

### Thread 6: The Evolutionary Story
Run 30 produced a finding about VDAC's bacterial porin origins and the endosymbiotic
event. Session 2 frontier poses follow-up questions (chloroplasts, single-celled
eukaryote apoptosis, the exact evolutionary moment the audit became lethal).
Read ALL s2_synthesis files for any evolutionary biology content. If there's
a coherent thread beyond what session_2_frontier_findings.md captured, extract it.

### Thread 7: Cross-Run Type 3 Singulars
In each run's s3_convergence.json, look for TYPE 3 claims (claims only ONE model made).
Then check: does any TYPE 3 from one run appear as a TYPE 1 or TYPE 2 in another run?
These are the "early discoveries" — ideas that were singular in run N but converged
in run N+K. List any you find with their source runs.

### Thread 8: The Consciousness Runs
evo_20260213_004656_consciousness and evo_20260213_022353_consciousness+chemistry
are the only consciousness-tagged runs. Read their s1/s2/s3 files completely.
What question was asked? What did converge? The existing gold docs
(fim_semantic_bonding.md, local_rotation_scaling.md) may already cover these —
but check if anything was left on the floor.

---

## Output Format

For each new gold document, follow this structure:

```markdown
# [Descriptive Title]

**Source runs**: [list run IDs]
**Date extracted**: 2026-02-20
**Theme**: [one line]

---

## What the Models Said

[Direct quotes or close paraphrases from s2_synthesis.json, with run ID attribution.
No fabrication. If you're summarizing, say so.]

## Where the Runs Agree

[TYPE 0/1 claims — what multiple models converged on]

## Where the Runs Diverge

[TYPE 3 singulars or points of model disagreement — equally valuable]

## Connection to Existing Gold

[How does this connect to existing gold documents? What does it extend?]

## Open Questions

[What does this finding leave unanswered? What's the next experiment?]

## Testable Predictions

[If the synthesis generated hypotheses, list them with testability score if available]
```

---

## File Naming

Save new gold documents to:
`/Users/vaquez/vdac-pharmacology-atlas/gold/[descriptive_snake_case_name].md`

Use descriptive names. Examples of what might emerge:
- `vdac_bioelectric_membrane_potential.md`
- `neuroscience_vdac_synaptic_mito.md`
- `failed_run_gold_ultrasound_erastin.md`
- `calcium_frequency_cofactor_extension.md`
- `aging_as_gate_jamming.md`
- `vdac_evolutionary_threshold_origin.md`
- `cross_run_singular_echoes.md`

---

## Final Check

Before finishing, read ALL new gold documents you've written against the existing 23.
Ask: "Does this add something not already said?" If not, don't file it.

The bar for a gold document: something a researcher picking up this corpus in a year
would be glad was preserved, because it connects things that aren't connected elsewhere.

---

*The corpus is complete. The work is done. You're reading the archaeology.*
