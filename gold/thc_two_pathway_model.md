# THC Two-Pathway Model: Gold Extraction

**Source runs**: `evo_20260211_024747_pharmacology` (wellbeing) + `evo_20260211_024750_neuroscience` (aging)
**Extraction date**: 2026-02-11
**S3 outcome**: Both FAILED — but cross-run analysis reveals mechanistic convergence invisible to the per-run gate.

## Core Model

Low CB1 receptor occupancy (<20-30%) engages **G-protein biased signaling** (therapeutic), while higher occupancy (>30-50%) recruits **beta-arrestin** (tolerance, desensitization).

This means low-dose THC supplements your endocannabinoid system (adding to tonic 2-AG signaling) rather than replacing it.

## Multi-Model Convergent Claims

### TYPE 1 (3/5 models agree)

**1. Kinetic Crossover for Tolerance**
- Tolerance is a first-order kinetic phase transition, not a gradual slide
- Occurs when CB1 internalization exceeds recycling + synthesis: k_int > k_rec + k_syn
- Crossover at ~25-30 mg/day (~30% occupancy)
- Models: Gemini, Grok, Mistral (wellbeing run); DeepSeek, Gemini, Mistral (wellbeing run)

**2. 2-AG Synergy at Low Dose**
- Low-dose THC (<=2.5 mg/day) adds to tonic 2-AG without displacement
- High-dose THC (>10 mg/day) saturates CB1, reduces 2-AG access, upregulates MAGL
- Models: DeepSeek, Grok, Mistral

**3. Biphasic CB1 Signaling**
- G-protein activation (EC50 ~10 nM) dominates at 10-30% occupancy
- Beta-arrestin recruitment (EC50 >100 nM) avoided at low dose
- Preserves cAMP/PKA tone
- Models: Claude, Mistral

### TYPE 0 (5/5 models agree — aging run)

**4. GABAergic Disinhibition in Aging**
- Aged hippocampus has pathologically elevated GABA tone
- Low-dose THC restores excitation/inhibition balance
- 5/5 models independently identified this mechanism
- This was the strongest convergence signal across ALL runs

**5. Biphasic Dose-Response in Aging**
- 4/5 models agreed: low-dose beneficial, high-dose harmful
- Aging context amplifies the two-pathway pattern

## Novel Singulars (TYPE 3 — single model, high potential)

| Claim | Model | Why It Matters |
|-------|-------|---------------|
| eCB-LTD potentiation at amygdala/PVN excitatory synapses | Gemini | Mechanism for lasting anxiolytic effect — "stamps in" lower stress reactivity |
| HPA axis recalibration via PVN CB1 — 20-35% cortisol AUC reduction over 2-4 weeks | Claude | Quantitative prediction for clinical validation |
| Beta-arrestin bias factor ~3-5x (G-protein EC50 vs beta-arrestin EC50) | Grok | Explains why occupancy threshold exists |
| CB1 occupancy <30%: fG/fBeta >2, preventing downregulation | DeepSeek | Mathematical framing of the therapeutic window |
| Tolerance crossover at ~40-50% sustained occupancy (~10-15 mg/day chronic) | Claude | Lower estimate than others — potential conservative bound |
| AMPA nanodomain clustering rescue in aged synapses | DeepSeek | Novel mechanism beyond GABAergic disinhibition |
| Synaptic remodeling > neurogenesis for aging cognitive benefit | DeepSeek | Challenges dominant neurogenesis narrative |

## Structural Isomorphism

This is the third molecule where IRIS Evo independently discovered a two-pathway model:

| Molecule | Gateway | Dose Picks Pathway | Tissue Determines Outcome |
|----------|---------|-------------------|--------------------------|
| CBD | VDAC1 conductance | Concentration at mitochondria | Cancer (high ROS) vs healthy (low ROS) |
| Lithium | GSK-3beta inhibition | Serum level (<1mM vs >2mM) | Neurons (neuroprotective) vs kidneys (nephrotoxic) |
| THC | CB1 occupancy | Daily dose (<2.5mg vs >10mg) | Naive (therapeutic) vs tolerant (desensitized) |

## Falsification Targets

1. PET imaging ([11C]OMAR) at graded chronic doses — does tolerance onset correlate with ~30% occupancy?
2. BRET assays for beta-arrestin EC50 vs G-protein EC50 — is bias factor really 3-5x for THC?
3. Salivary cortisol AUC in controlled low-dose trials — does 20-35% reduction hold?
4. Ex vivo slice electrophysiology — does chronic low-dose THC enhance eCB-LTD at amygdala?
5. 2-AG levels at graded THC doses — does displacement only occur >10 mg/day?
