# Raw Data Through the Coherence Lens
## Final sweep before the manuscript

**Date**: 2026-02-14
**Corpus**: 20 archived runs, 16 with synthesis data, 9 S3-passed, 139 synthesized claims

---

## The Numbers

| Metric | Value |
|--------|-------|
| Total IRIS runs | 20 |
| Runs with S2 synthesis | 16 |
| S3 PASSED | 9 |
| S3 FAILED (mined for gold) | 7 |
| Total synthesized claims | 139 |
| TYPE 0 (5/5 convergence) | 23 (16.5%) |
| TYPE 1 (4/5 or 3/5) | 23 (16.5%) |
| TYPE 2 (2/5) | 22 (15.8%) |
| TYPE 3 (singulars) | 71 (51.1%) |
| NOVEL (no prior literature) | 22 |
| PROMOTED (TYPE 2 → TYPE 1) | 4 |
| HELD at TYPE 2 | 23 |
| CONTRADICTED by literature | 6 |
| Operationalized hypotheses | 24 |
| Mean testability | 7.2/10 |

**The singulars dominate.** 51% of all claims are TYPE 3 — unique to a single model. This is not noise. The atlas's most radical and ultimately validated insights came from singulars: CBD as membrane chaotrope (Gemini), HPA axis modulation by THC (Claude), cofactor equation is phenomenological (Claude self-questioning), VDAC1 oligomerization as point of no return (Gemini), circadian GSK-3beta phosphorylation (counter-consensus).

---

## The Questions Asked — A Narrative Arc

Reading the 20 questions chronologically reveals the research program's emergent logic:

1. **CBD cytotoxicity** (Runs 1-2) — The original question. Two-pathway model discovered.
2. **Lithium neuroprotection** (Runs 3-5) — Testing generality. GSK-3beta two-pathway found independently.
3. **THC wellbeing + neuroprotection** (Runs 6-7) — Third molecule. CB1 occupancy threshold. S3 failed but rich.
4. **Circadian VDAC1** (Run 8) — First mechanistic pivot. Time as a variable. S3 failed, gold in singulars.
5. **VDAC1 selectivity** (Run 9) — Why do different drugs have different effects? Cofactor landscape.
6. **FIM + local rotation** (Runs 10-11) — Methodology validation. IRIS protocol itself as subject.
7. **CBD stress test** (Run 12) — Adversarial: can the model survive attack? Four challenges, all survived.
8. **Chronic dosing** (Run 13) — Temporal dynamics. GSH depletion over time.
9. **Isoform architecture** (Run 14) — Structural: why VDAC1 not VDAC2? S3 failed, E73 gate discovered.
10. **Cofactor landscape** (Run 15) — The equation derivation. HK-II permissive, Bcl-xL protective.
11. **Lipid modulation** (Run 16) — Membrane as pharmacological variable. Cholesterol lowers Kd.
12. **Biomarkers** (Run 17) — Clinical translation. GSH/GSSG as predictive biomarker.
13. **Drug interactions** (Run 18) — Polypharmacy. VPA+CBD synergistic risk. NAPQI opposite gating.
14. **Membrane architecture** (Run 19) — Honeycomb gate. Biophysical grounding of cofactor equation.

The questions narrow from "what does this drug do" to "what IS this protein" to "what IS this gate." The arc is: pharmacology → mechanism → physics → philosophy.

---

## Hidden Patterns Visible Only in Aggregate

### Pattern 1: The Convergence-Novelty Inverse

The runs with highest convergence (TYPE 0/1 ratio) tend to have fewer NOVEL findings. The runs with most novelty tend to have lower convergence or fail S3 entirely.

| Run | TYPE 0/1 % | NOVEL | Interpretation |
|-----|-----------|-------|----------------|
| Lipid modulation | 100% | 3 | High agreement, moderate novelty |
| Drug interactions | 95% pass | 3 | High agreement, moderate novelty |
| Membrane architecture | 80% | **4** | Exception — both high convergence AND high novelty |
| Chronic dosing | 63% | **8** | Lower convergence, highest novelty in corpus |
| THC (both) | Failed S3 | — | Maximum novelty zone: the models disagreed because the territory is unexplored |

**The membrane run is the outlier.** It achieved both high convergence (0.9047 cosine, 80% TYPE 0/1) AND the highest novel-per-verified ratio. This suggests the honeycomb architecture question hit a **sweet spot** — enough established biophysics for models to converge, enough unexplored territory for genuine discovery.

### Pattern 2: Gemini as the Frontier Scanner

Across the corpus, Gemini consistently produces the most radical singulars:
- CBD as membrane chaotrope (Run 19)
- VDAC1 oligomerization as Bax/Bak-receptive macropore (Run 15)
- Cofactor equation's apoptotic threshold (proto-version, Run 15)
- Olesoxime as a cholesterol-dependent probe (Run 16)
- eCB-LTD network depression by THC (Run 6)
- HK-II shields CL specifically (Run 19)

Gemini's singulars are disproportionately PROMOTED or VALIDATED in subsequent runs. This is not because Gemini is "better" — it's because Gemini's training distribution apparently includes more frontier biophysics, making it willing to propose mechanisms other models won't.

### Pattern 3: Claude Self-Questions

Claude is the only model that produced claims questioning its own prior outputs:
- "The cofactor equation is phenomenological" (Run 19) — questioning the equation it helped derive in Run 15
- "CTC VDAC1 is unreliable" (Run 17) — questioning a biomarker it suggested in prior runs
- "Peripheral GSH doesn't reflect hepatic GSH" (Gemini agreed, Run 17)

This self-critical pattern is unique in the corpus and arguably the most honest contribution. A model that questions convergence is more valuable than one that amplifies it.

### Pattern 4: The Warburg Thread Was Always There

Re-reading the raw data with the coherence lens:
- **Run 2 (CBD)**: "HK-II binding to VDAC... shifts the operating point" — HK-II as VDAC modulator
- **Run 5 (THC)**: "Metabolic reprogramming in neurons" — Warburg-adjacent language
- **Run 8 (Circadian)**: "GSK-3beta phosphorylation of VDAC Thr51 regulates HK-II affinity" — the kinase link
- **Run 15 (Cofactor)**: "HK-II displacement is permissive, not sufficient" — the mechanism
- **Run 18 (Drug interactions)**: "NAPQI closes VDAC via cysteine modification" — the opposite direction
- **Run 19 (Membrane)**: "HK-II shields CL microdomains" — the biophysical basis

The Warburg-as-gate-jamming insight was distributed across 6 runs. No single run stated it. It only becomes visible when you read the aggregate as a single narrative. **The corpus knew something none of its parts knew.**

### Pattern 5: The Three Signals Were Encoded but Unnamed

- **Signal 1 (Mitophagy)**: Run 16 mentioned CL externalization. Run 19 mentioned CL as disruption trigger. No run connected CL flip to LC3 binding. The mitophagy signal was implicit.
- **Signal 2 (Inflammation)**: No run mentioned mtDNA release through VDAC oligomers or cGAS-STING. This was entirely absent from the corpus — a genuine blind spot.
- **Signal 3 (Apoptosis)**: Every run that discussed VDAC addressed cytochrome c release. But the PS externalization ("eat me" signal) was never mentioned. The macrophage cleanup phase was invisible.

**The corpus has a horizon.** It sees VDAC-to-death clearly. It does not see death-to-cleanup. The three-signal model extends beyond what the multi-LLM consensus can currently reach — it required human + literature + structural analysis to complete.

### Pattern 6: The Cofactor Equation's Terms Map to Cancer's Countermeasures

| Equation Term | Normal Function | Cancer's Countermeasure | Energy Cost |
|--------------|-----------------|------------------------|-------------|
| f_HKII | Metabolic loyalty signal | HK-II overexpression (Warburg) | 18x less ATP/glucose |
| f_BclxL | Anti-apoptotic badge | Bcl-2/Bcl-xL overexpression | Constitutive gene expression |
| Chol/CL | Membrane stability readout | Cholesterol loading of OMM | Sterol transport machinery |
| K (honeycomb exit energy) | Lattice stability | All of the above simultaneously | Entire metabolic reprogramming |

Cancer doesn't break one term. It games all four. And every countermeasure has an ongoing metabolic cost — cancer can't just silence a gene and walk away. It must actively maintain the jamming. **The Warburg effect is the electricity bill for running the gate-jamming equipment.**

---

## What the Data Demands as Manuscript Structure

The raw data organizes itself into a natural paper:

### Layer 1: The Protein (structural portrait)
- 19-strand barrel, N-terminal helix, five machines in one protein
- The parallel-seam life/death switch (beta-strands 1/2/18/19)

### Layer 2: The Gate (threshold architecture)
- Three signals: mitophagy → inflammation → apoptosis
- Nested thresholds, escalating sacrifice
- The cofactor equation as mathematical contract

### Layer 3: The Atlas (6 pharmacological runs)
- Binding architecture → Cofactors → Lipids → Biomarkers → Drug interactions → Membrane
- 22 novel findings, 24 operationalized hypotheses
- Cross-run structural isomorphism (CBD/lithium/THC two-pathway models)

### Layer 4: The Disease (cancer as lost coherence)
- Cancer rewrites every threshold gate
- Warburg effect as gate-jamming cost
- VDAC as the body's external audit
- Selective cytotoxicity explained by dependency

### Layer 5: The Method (IRIS protocol)
- Multi-LLM convergence as discovery tool
- TYPE system, singulars as signal, cross-run analysis
- What convergence can and cannot establish

### Layer 6: The Frame (coherence as organizing principle)
- Thresholds at every scale: VDAC → cell → tissue → organism → physics
- Silicon gate parallels
- Sovereignty through coherence

---

## Final Accounting

| What We Have | Count |
|-------------|-------|
| Gold extraction documents | 19 |
| Archived IRIS runs | 20 |
| Synthesized claims | 139 |
| Novel findings (verified) | 22 |
| Operationalized hypotheses | 24 |
| Testable predictions (power > 0.8) | 18 |
| Pharmacovigilance alerts | 3 (VPA+CBD, circadian dosing, lithium-CBD) |
| Independent LLM-model responses | ~100 (5 models x 20 runs) |
| Cross-run matches | 5 (automated) + ~20 (manual gold extraction) |
| Structural portrait pages | 1 (comprehensive) |
| Philosophical frame documents | 2 (deep reflection + cancer coherence) |

**The data is ready. The frame is set. The manuscript writes itself from here.**
