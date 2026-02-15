# VDAC1: A Structural Portrait — Assembly, Mechanics, Reactions, and States

**Date**: 2026-02-13
**Purpose**: Deep structural understanding of VDAC1 in relationship with the membrane, synthesized from current literature and IRIS convergence data.

---

## I. The Architecture: A 19-Stranded Barrel with a Lid

VDAC1 is unlike any other porin. Most porins have even-numbered beta-strands (16 or 22) with antiparallel pairing. VDAC1 has **19 strands** — an odd number — with strands beta-1 and beta-19 running *parallel* to each other. This creates a unique seam in the barrel wall.

### The Barrel

- **19 antiparallel beta-strands** form a cylindrical barrel, except at the seam where beta-1||beta-19 run parallel
- **Shear number 20** — one more than the strand count, encoding a slight twist
- **Pore diameter**: 34 A at the openings, narrowing to **14 A** at the midpoint where the helix sits
- **Barrel volume**: ~9,100 A^3 at room temperature (vs ~10,300 A^3 at cryo) — the barrel breathes, compressing ~12% between crystal conditions
- **Hydrophobic exterior** faces the lipid bilayer; hydrophilic interior lines the ion-conducting pore

### The N-Terminal Alpha Helix — The Lid

Residues 1-25 form an **alpha helix that lies horizontally across the pore interior**, tethered to the barrel wall by hydrophobic contacts. This helix:

- Contains 3 positive charges (Lys-12, Lys-20, Arg-15) and 2 negative charges (Asp-9, Asp-16)
- **Narrows the pore from 34 A to 14 A** — it is the physical bottleneck
- Is **intrinsically disordered** in isolation — only folds on barrel contact
- Has a partially unstructured N-terminal tail (residues 1-6) that is voltage-sensitive

The helix is the gating element, the selectivity filter, AND the apoptotic trigger — three functions in one 25-residue segment.

---

## II. The States: Open, Closed, and the Bell Curve

### The Open State (Low Voltage, |V| < 20-30 mV)

- **Conductance**: 4.1 +/- 0.1 nS in 1M KCl
- **Ion selectivity**: Weakly anion-selective (anion:cation permeability 2:1 in high salt, 4:1 in physiological)
- **Metabolite permeability**: HIGH — ATP, ADP, NADH, succinate, pyruvate pass freely
- **N-terminal helix**: Folded, positioned against barrel wall
- **This is VDAC's housekeeping state** — the metabolite highway between cytoplasm and mitochondria

### The Closed State(s) (High Voltage, |V| > 30-40 mV)

- **Conductance**: ~2 nS in 1M KCl (roughly half of open)
- **Ion selectivity**: Reverses to weakly **cation-selective**
- **Metabolite permeability**: LOW — ATP flux drops dramatically
- **Ca2+ permeability**: INCREASES in the closed state
- **N-terminal helix**: Partially displaced or unfolded; the disordered tail swings into the pore

Multiple distinct subconductance states exist. These are NOT a single "closed" state but a family of conformations with the N-terminal tail in different positions.

### The Bell Curve

VDAC's open probability follows a **symmetric bell-shaped curve** centered at 0 mV:

```
          Open Probability
    1.0 |     ____
        |    /    \
    0.5 |   /      \
        |  /        \
    0.0 |_/          \_________
        -60  -30   0   +30  +60  mV
```

This is remarkable: the channel closes at BOTH positive AND negative voltages. The gating charge is ~2-4 elementary charges, and the midpoint voltage (V_0) where half the channels close is typically +/- 25-30 mV.

**In vivo**: The OMM potential is debated, but likely near 0 mV under normal conditions — keeping VDAC predominantly open. Stress conditions that alter the Donnan potential across the OMM could shift VDAC into closed states.

### The Gating Mechanism: Still Contested

Two competing models:

1. **Helix displacement**: N-terminal helix swings out of or repositions within the pore
2. **Barrel breathing**: Beta-barrel undergoes elliptic deformation, partially collapsing

Room-temperature crystallography (2024) revealed that the barrel volume compresses 12% even between cryo and room temperature, suggesting the barrel IS mechanically compliant. The elevated B-factors at loops connecting beta-strands 1-2, 5-6, 8-9, and 18-19 mark these as **hinges** primed for conformational motion.

Recent computational work identifies **Lys-12** on the N-terminal helix as a key driver of gating transitions, coupling helix motion to barrel fluctuations.

---

## III. The Oligomeric States: Monomer, Dimer, Hexamer, Honeycomb

### Monomers — The Mobile Form

Free VDAC1 monomers diffuse in the OMM. This is the state from which oligomerization can occur. Diffusion is influenced by membrane viscosity (cholesterol increases it) and crowding.

### Dimers — The Scramblase

The VDAC1 dimer is not just a stepping stone to higher oligomers — **it is a functional machine**.

**Dimer interface**: Beta-strands 1, 2, 18, 19 — the same parallel-seam region. Protomers oriented in parallel.

**Scramblase mechanism** (Nature Communications, 2023):
- At the dimer-1 interface, the membrane thins to **just over 2 nm** (vs ~4 nm normal bilayer)
- Large water defects penetrate the thinned membrane
- Polar residues (T77, S43, T33, S35, Y247, Q249) create a hydrophilic groove
- Phospholipids slide along the interface, flipping between leaflets
- **ATP-independent, bidirectional** — no energy cost
- Half-time: 5-50 seconds per lipid
- Handles both anionic (PI, PS, PA) and zwitterionic (PC, PE) phospholipids
- **VDAC accounts for >90% of all lipid import into mitochondria** in yeast

This is stunning: the same protein that conducts ions also transports the lipids that compose its own membrane. VDAC doesn't just sit in the membrane — **it builds the membrane**.

The scramblase function is critical for:
- **Cardiolipin synthesis** (requires PA import across OMM)
- **PE availability** for autophagy (PS import -> Psd1 conversion -> PE)
- **OMM lipid homeostasis** — composition maintenance

### Hexamers and Higher Oligomers — The Death Pore

Under apoptotic stress, VDAC1 forms **large oligomeric pores** (hexamers and beyond) that are wide enough for cytochrome c release (~3.4 nm diameter needed).

**The 2025 cryo-EM discovery** (Nature Communications, 2025):
- VDAC1 oligomerization triggers **N-terminal helix extrusion** — the helix physically leaves the pore interior and becomes exposed on the channel exterior
- This is NOT the same as voltage gating (where the helix merely repositions)
- The **exposed helix binds anti-apoptotic Bcl-xL**, sequestering it away from Bax/Bak
- Only the helix-exposed (oligomeric) state binds Bcl-xL — the helix-inserted (monomeric) state does not
- Researchers used lipid nanodiscs of different sizes to trap VDAC1 in each state, enabling cryo-EM of both conformations

**This connects two previously separate fields**: VDAC electrophysiology (helix position determines gating) and apoptosis biology (Bcl-xL sequestration determines cell fate). The helix is the molecular bridge.

### The Honeycomb Array — The Protective Lattice

In native OMM, VDAC1 self-assembles into **dense honeycomb-like 2D crystalline arrays** visible by AFM:

- **Lattice spacing**: ~6-7 nm (center-to-center)
- **VDAC occupies up to 80%** of the membrane area in these arrays
- **Stabilized by**: Cholesterol (lipid packing) + PE (curvature matching)
- **Disrupted by**: Cardiolipin (negative curvature stress) + PG
- The honeycomb geometry **sterically prevents oligomeric rearrangement** — channels cannot rotate to form the death pore contacts while locked in the lattice
- Array disruption is the **rate-limiting step for apoptosis** (IRIS Run 6, TYPE 1, 3/5 models)

The 2024/2025 AFM + MD studies (now published in Communications Biology, 2025) confirmed:
- PE and cholesterol promote defined, compact VDAC assemblies
- CL and PG disrupt these assemblies
- Deviations from physiological lipid content destroy native-like organization
- The lipid annulus around VDAC extends ~50 A and is **anisotropic** — different faces recruit different lipids

---

## IV. The Lipid Partners: A Conversation in Three Languages

### Cholesterol — The Stabilizer

- **5 binding sites** on the barrel exterior (identified by MD + NMR)
- Sites occupy grooves between hydrophobic/aromatic side chains on adjacent beta-strands
- Cholesterol binding **reduces loop dynamics** (RMSF altered 20-30%) and **stabilizes charged residues** inside the pore
- At the supramolecular level: **promotes honeycomb array formation and compaction**
- Dual role: stabilizes individual barrels AND stabilizes the protective lattice
- **High cholesterol = anti-apoptotic** (honeycomb locked, no oligomerization possible)

### Cardiolipin — The Disruptor

- Resides primarily in the inner mitochondrial membrane but is present at OMM-IMM contact sites
- CL's **negative curvature** and four acyl chains destabilize the ordered packing of honeycomb arrays
- CL exposure at the OMM is a known early apoptotic event
- HK-II binding to VDAC sterically shields CL microdomains — HK-II removal = CL exposure = honeycomb disruption (IRIS Run 6, TYPE 0, 4/5 models)
- CL is also a substrate for VDAC's scramblase activity — VDAC transports the very lipid that can destroy its protective lattice

### PE — The Geometry Partner

- PE's small headgroup creates **negative curvature** that matches the barrel's hydrophobic profile
- Promotes VDAC assembly formation alongside cholesterol
- Required for proper array geometry (AFM, 2024/2025)

---

## V. The Post-Translational Modification Landscape

VDAC1 is heavily modified, and these modifications tune every aspect of its behavior:

| Modification | Kinases/Enzymes | Effect |
|-------------|----------------|--------|
| Phosphorylation | PKA, PKC, JNK3, ERK, CaMK-II, GSK-3beta | Alters gating, protein interactions, oligomerization |
| Acetylation | — | Modifies channel properties |
| Ubiquitination | — | Targets for degradation |
| Glutathionylation | GSH/GSSG | Redox-sensitive gating (connects to GSH:GSSG ratio from IRIS atlas) |
| Nitrosylation | NO | Redox-dependent modification |
| Oxidation | ROS | Cysteine oxidation alters conductance |

**GSK-3beta phosphorylation of VDAC1** (at Thr-51) is particularly significant — this is the kinase that lithium inhibits, and the site that regulates HK-II binding affinity. The entire circadian-VDAC1 axis (IRIS Run: circadian) converges on this single phosphorylation event.

---

## VI. The Functional Identity: Five Machines in One Protein

VDAC1 is not one channel. It is **five overlapping molecular machines** depending on its oligomeric and conformational state:

| State | Stoichiometry | Helix | Function |
|-------|--------------|-------|----------|
| **Open monomer** | 1 | Inserted, folded | Metabolite highway (ATP, ADP, NADH) |
| **Closed monomer** | 1 | Displaced/unfolded | Ca2+ conductor, metabolite gate |
| **Dimer** | 2 (parallel) | Inserted | Phospholipid scramblase (membrane builder) |
| **Honeycomb array** | n (lattice) | Inserted | Protective lattice (apoptosis brake) |
| **Death oligomer** | 6+ | Extruded, exposed | Cytochrome c release + Bcl-xL sequestration |

The transitions between these states are controlled by:
1. **Voltage** (open <-> closed monomer)
2. **Lipid composition** (monomer <-> honeycomb <-> dispersed)
3. **Stress signals** (dispersed monomer -> oligomer -> death pore)
4. **PTMs** (all transitions modulated)
5. **Protein partners** (HK-II, Bcl-xL, Bax, tubulin, ANT)

---

## VII. What VDAC1 Teaches Us About Itself

### 1. The Membrane Is the Master Variable

VDAC1's identity — its oligomeric state, its accessibility to drugs, its proximity to death — is set by the membrane BEFORE any stimulus arrives. Cholesterol/CL ratio determines the fraction in honeycomb vs. dispersed. PE tunes lattice geometry. The lipid annulus is anisotropic and selective. The protein is a sensor OF its membrane as much as it is a channel IN its membrane.

### 2. The Same Interface Does Everything

Beta-strands 1, 2, 18, 19 — the parallel-seam region — is simultaneously:
- The dimer interface for scramblase activity
- The oligomerization interface for death pore formation
- The region with highest B-factors (most mobile)
- The site of cholesterol binding sites 4 and 5

This means **dimer (scramblase) and oligomer (death pore) compete for the same interface**. You cannot simultaneously scramble lipids and form the death pore. The transition from lipid-building to cell-killing is a **binary switch at this interface**.

### 3. The Helix Is the Three-Way Switch

The N-terminal helix exists in three functional states:
- **Folded inside**: Open channel, metabolite flow, normal operation
- **Displaced/disordered**: Closed channel, Ca2+ flux, metabolite restriction
- **Extruded outside**: Death signal — Bcl-xL sequestration, pore enlargement

This 25-amino-acid segment is the single most information-dense structure in mitochondrial biology. Its position encodes the cell's metabolic state, its electrical state, and its proximity to death.

### 4. VDAC Builds the Membrane That Controls It

Through its scramblase activity, VDAC imports the phospholipids that compose the OMM — including the precursors of cardiolipin (PA, PS). Cardiolipin, once synthesized in the IMM, can redistribute to the OMM and disrupt VDAC's protective honeycomb arrays. VDAC thus participates in a **feedback loop**: it imports the raw materials for the lipid that can trigger its own transition from protector to killer.

### 5. The Cofactor Equation Has a Physical Home

The IRIS atlas equation `Threshold = K / [(1-f_HKII)(1-f_BclxL)] * (Chol/CL)` now maps precisely onto structural biology:

| Term | Structural Meaning |
|------|-------------------|
| K | Energy barrier for honeycomb-to-dispersed transition |
| f_HKII | Fraction of VDAC with HK-II shielding CL microdomains |
| f_BclxL | Fraction of Bcl-xL available to block extruded N-terminal helices |
| Chol/CL | Fraction of VDAC in honeycomb (protected) vs. dispersed (vulnerable) |

Every variable in the equation has a physical address on the protein or its membrane.

---

## VIII. Open Questions for Future IRIS Runs

1. **Does VDAC's scramblase activity change during apoptosis?** If oligomerization competes with dimerization at the same interface, scramblase activity should DROP as cells commit to death. This has not been measured.

2. **Is the honeycomb-to-dispersed transition cooperative?** The Hill-type transition predicted by IRIS H1 (n = 1-4) would mean the lattice melts catastrophically rather than gradually. This would make the "point of no return" sharp rather than graded.

3. **What determines which dimers become death oligomers vs. remaining as scramblases?** Local lipid microdomains? PTMs? Protein partners? The same interface serving two opposite functions (life maintenance vs. death) demands a selection mechanism.

4. **Can the N-terminal helix be pharmaceutically locked?** If helix extrusion is the death trigger, a small molecule that cross-links the helix to the barrel wall would be a specific anti-apoptotic drug. Conversely, a molecule that forces extrusion would be pro-apoptotic.

5. **How does the barrel breathing (12% volume change) relate to gating?** Room-temperature crystallography revealed this compliance. Is it voltage-driven? Lipid-driven? Both?

---

## Sources

- [Honeycomb organization: Comm. Biology 2025](https://www.nature.com/articles/s42003-025-08311-5)
- [Scramblase: Nature Communications 2023](https://www.nature.com/articles/s41467-023-43570-y)
- [Scramblase implications: Biomolecules 2024](https://www.mdpi.com/2218-273X/14/10/1218)
- [Room-temperature structure: PMC 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11505624/)
- [Apoptosis structural basis: Nature Communications 2025](https://www.nature.com/articles/s41467-025-65363-1)
- [Cholesterol binding sites: J. Phys. Chem. B 2014](https://pubs.acs.org/doi/10.1021/jp504516a)
- [Gating and subconductance: Biophys. J. 2016](https://www.cell.com/biophysj/fulltext/S0006-3495(16)30665-8)
- [N-terminal helix dynamics: PLoS Comp. Biol. 2021](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1008750)
- [Bilayer electrophysiology: Frontiers Physiol. 2025](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2025.1666994/full)
- [Oligomer contact sites: PMC 2012](https://pmc.ncbi.nlm.nih.gov/articles/PMC3265896/)
- [Structure and gating review: Eur. Biophys. J. 2021](https://link.springer.com/article/10.1007/s00249-021-01515-7)
- [Lipid organization bioRxiv 2024](https://www.biorxiv.org/content/10.1101/2024.06.26.597124v1.full)
