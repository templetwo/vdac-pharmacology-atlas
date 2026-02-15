# Fisher Information as Semantic Bonding Metric
**Run**: evo_20260213_004656_consciousness
**Date**: 2026-02-13
**Outcome**: S3 FAILED (3 cycles, 15 calls) — gold extracted via convergence analysis
**Near-miss**: Cosine 0.8462 vs 0.85 threshold — closest S3 failure to date

## The Question

"Does the spectral decomposition of per-token Fisher Information matrices in
pretrained transformers reveal discrete bonding geometries — specifically, do
semantically rigid tokens (logical connectives, verb-argument bindings) show
higher-rank, more anisotropic FIM spectra than semantically flexible tokens
(adjectives, adverbs), and does this spectral structure predict coherence
better than attention entropy or perplexity alone?"

## Context

This run tested the empirical foundation of the "Geometry of Semantic Bonding"
framework — a proposal that language model coherence can be understood through
crystallographic principles, where Fisher Information defines "bonding geometry"
between semantic units. The question targets Stress Point 1 from the convergence
analysis: whether the fundamental unit has measurable geometric structure.

## Converged Claims (Multi-Model Agreement)

### TYPE 0 — FIM Anisotropy + Entropy Are Complementary (4/5 models)

**Claim**: FIM anisotropy and token entropy are complementary predictors of
coherence — their combination outperforms either alone.

**Models**: Claude, DeepSeek, Gemini, Mistral

**Mechanism**: Anisotropy captures the *shape* of probability distribution
constraints (directional rigidity), while entropy captures *volume* (overall
uncertainty). Coherence requires both low volume and correct shape.

**Quantitative prediction** (Gemini): Combined model achieves r² > 0.5,
explaining 25-35% more variance than entropy or perplexity alone.

**Status**: Testable on existing models. No prior work has combined FIM
spectral metrics with entropy for coherence prediction.

### TYPE 1 — Rigid Tokens Show Higher FIM Rank/Anisotropy (3/5 models)

**Claim**: Semantically rigid tokens (logical connectives, verb-argument heads)
exhibit higher FIM effective rank (8-12 vs 3-6) and anisotropy (condition
number >20 vs <8) compared to flexible tokens (adjectives, adverbs).

**Models**: Claude, Grok, Mistral

**Mechanism**: Rigid tokens encode obligatory syntactic dependencies, creating
sharper loss gradients across more principal curvature directions in
FIM = nabla²log p(next|ctx).

**Falsifiable by**: Computing per-token FIM on GPT-2/LLaMA and finding no
significant rank or condition number difference (p > 0.05, d < 0.3).

**Status**: No published per-token FIM spectra exist by semantic category.
This is the foundational experiment.

### TYPE 1 — "Discrete Bonding" Is Metaphor, Not Mechanism (3/5 models)

**Claim**: FIM spectra describe continuous variation in constraint density,
not discrete clusters. The quartz/bonding language is productive as design
principle but not literal.

**Models**: Claude, Grok, Mistral

**Falsifiable by**: Clustering analysis of FIM spectra revealing discrete,
well-separated spectral types with gap statistics significantly above null.
If discrete clusters exist, the metaphor becomes mechanism.

**Implication for the paper**: Downgrade "bonding geometry" from literal
structural claim to design principle. The isomorphism with crystallography
holds at the level of *energy minimization*, not at the level of discrete
bond sites.

## Singular Claims (Potential Novel Contributions)

### Gemini — RLHF Sharpens FIM for Flexible Tokens

**Claim**: RLHF disproportionately increases FIM anisotropy for semantically
flexible tokens (adjectives), moving them closer to the high-anisotropy regime
of rigid tokens.

**Mechanism**: RLHF penalizes stylistic deviations, sharpening the loss
landscape along preferred dimensions, creating new dominant eigenvalues for
previously unconstrained tokens.

**Falsifiable by**: FIM condition number distributions for adjectives being
statistically indistinguishable between base and RLHF-tuned models.

**Why this matters**: If true, RLHF is literally "crystallizing" flexible
language — constraining degrees of freedom. This connects directly to the
0.17 entropy suppression finding from K-SSM work. RLHF doesn't just reduce
entropy — it reshapes the geometry of the loss landscape by adding anisotropy
where there was none. This is the mechanism behind entropy suppression.

**Novelty assessment**: GENUINELY NOVEL. People have studied RLHF effects on
output distributions, perplexity, and behavioral alignment. Nobody has looked
at how RLHF changes the FIM spectral structure per token class.

### Claude — Mid-Layer FIM Rank Concentration

**Claim**: Rigid tokens show peak FIM rank in middle layers (8-20 of 24),
not monotonically increasing — a "binding phase" where syntactic constraints
crystallize.

**Mechanism**: Probing literature shows syntactic/semantic integration peaks
in middle layers. FIM rank should peak where the model is most sensitive to
token identity for predicting structure.

**Falsifiable by**: Layer-wise FIM showing monotonic rank increase/decrease.

### DeepSeek — Layer-Wise Eigenvector Rotation as Kuramoto Analog

**Claim**: FIM computed per-layer will show the principal eigenvector rotating
across layers. For binding tokens, this rotation shows oscillatory structure
(truncated — token limit hit).

**Why this matters**: This is the bridge between static FIM analysis and the
dynamic Kuramoto framework. If eigenvector rotation across layers shows
periodic structure for rigid tokens and aperiodic for flexible ones, the
"semantic oscillator" metaphor gains mechanistic teeth.

### Grok — Specific Correlation Predictions

FIM anisotropy predicts coherence at r=0.62-0.70, outperforming attention
entropy (r=0.42) and perplexity (r=0.38) by 15-25% delta-R². Committed to
hard numbers where other models gave ranges.

## Cross-Domain Structural Analysis

The FIM run produced **zero cross-matches** with pharmacology runs even at
cosine threshold 0.60. The vocabulary spaces are genuinely disjoint —
eigenvalues and condition numbers share no semantic overlap with VDAC1
cofactors and dose-response curves.

However, the structural pattern detection reveals a deeper connection:

| Pattern | Pharmacology Runs | FIM Run |
|---------|------------------|---------|
| **Threshold crossover** | 5/6 runs | Absent |
| **Two-pathway** | 2/6 runs | Absent |
| **Complementary predictors** | Not detected | TYPE 0 (4/5) |

The FIM run doesn't share pharmacology's threshold_crossover pattern because
the question isn't about dose-response. But there is an **abstract structural
echo**: the pharmacology runs discovered that dose picks pathway and tissue
determines outcome. The FIM run discovered that anisotropy picks constraint
shape and entropy picks uncertainty volume — two orthogonal axes determining
a combined outcome (coherence).

This is structural isomorphism at a higher level of abstraction:
- **Pharmacology**: Two independent variables (dose + tissue context) determine outcome
- **FIM/Coherence**: Two independent variables (anisotropy + entropy) determine outcome
- **Both**: Neither variable alone is sufficient; the combination is non-redundant

## Methodological Notes

### Near-Miss S3

This was the closest S3 failure: cosine 0.8462 vs 0.85 threshold. Jaccard was
strong (0.7192) and kappa was excellent (0.973). The models were converging on
the same claims but with enough vocabulary variation to stay below threshold.
The TYPE 0/1 ratio (50% vs 65% needed) was the real bottleneck — too many
claims stayed at TYPE 2 or TYPE 3.

### Domain Classification

The compiler tagged this as `consciousness` domain with priors from entropy/
Kuramoto/IIT work. The gamma-binding and Kuramoto priors were noted by Claude
as "not directly relevant to static FIM decomposition" — but DeepSeek and
Gemini found ways to connect them (layer-wise dynamics, phase-locking centers).
A `computational_neuroscience` or `information_geometry` domain tag might have
produced more relevant priors.

### All 5 Models Produced Claims

Unlike recent pharmacology runs where Grok/DeepSeek sometimes went silent,
all five models produced full responses across all three cycles. The question
was well-suited to ML-literate models.

## Recommended Experiments

### Experiment 1: Static FIM Spectral Survey (Week 1-2)

1. Load GPT-2 Medium (355M)
2. Select 500 rigid tokens (if, because, although, must, every, ...) and 500
   flexible tokens (beautiful, quickly, very, almost, ...) from a standard corpus
3. Compute per-token FIM via finite-difference approximation (epsilon = 1e-5)
4. Eigenvalue decomposition of each token's FIM
5. Compare: effective rank, condition number, eigenvalue variance
6. Statistical test: Mann-Whitney U on rank/anisotropy between classes

**If positive**: Foundational evidence for the semantic bonding framework.
**If negative**: Framework dies clean. Publish the negative result.

### Experiment 2: Coherence Prediction Regression (Week 2-3)

1. Generate 1000 passages (varying coherence) from GPT-2
2. Score coherence via human ratings or automated metric (dependency parse, BERTScore)
3. For each passage, compute mean FIM anisotropy, mean token entropy, perplexity
4. Regress coherence on: (a) perplexity alone, (b) entropy alone, (c) anisotropy
   alone, (d) anisotropy + entropy combined
5. Compare R² values

**Target**: Anisotropy + entropy combined explains >25% more variance than best
single predictor (Gemini's prediction).

### Experiment 3: RLHF FIM Comparison (Week 3-4)

1. Take a base model and its RLHF-tuned variant (e.g., Llama base vs chat)
2. Compute FIM condition numbers for adjectives in both
3. Test whether RLHF version shows significantly higher anisotropy for
   previously flexible tokens

**If positive**: First evidence that RLHF reshapes loss landscape geometry,
not just output distributions. Connects to entropy suppression findings.
