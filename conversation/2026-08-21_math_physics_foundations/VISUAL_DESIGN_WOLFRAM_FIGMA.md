# Wolfram / Figma Scientific Visual-Design Memory

## 1. Design reference

The Stephen Wolfram Physics Project visual summary and the April 2020 essay were used as the design reference for a high-density scientific framework aesthetic.

Key lesson:

\[
\boxed{\text{Do not design boxes describing mathematics; make the mathematics itself become the visual structure.}}
\]

The earlier card-based Figma attempt was judged far below the reference fidelity and should not be used as the master direction.

---

## 2. What the Wolfram reference actually relies on

The article exposes Wolfram Language computational-graphics constructs such as:

- `ResourceFunction["WolframModel"]`
- `ResourceFunction["WolframModelPlot"]`
- `ResourceFunction["MultiwaySystem"]`
- `LayeredGraphPlot`
- `Graph`
- `GraphicsGrid`
- `GraphicsRow`

Wolfram also publishes `WolframPhysicsProjectStyleData` for project graph styles.

A representative example used in the conversation was:

```wolfram
ResourceFunction[
  "WolframModel"
][
  {{0, 1}, {0, 2}, {0, 3}} ->
  {{1, 2}, {3, 2}, {3, 4}, {4, 3}, {4, 4}},
  {{0, 0}, {0, 0}, {0, 0}},
  20,
  "CausalGraph"
] // LayeredGraphPlot
```

The authoritative sources reviewed did **not** establish which external application, if any, was used for the final poster composition. Do not claim Illustrator/InDesign as fact without evidence.

---

## 3. Visual grammar to reproduce

High-fidelity characteristics:

- open dark field instead of a card-grid dashboard,
- one dominant central causal/multiway structure,
- hundreds of fine edges where scientifically meaningful,
- spatial hypergraph/networks,
- causal graph and multiway alternatives,
- branchial/lifecycle pathways,
- sparse explanatory labels,
- very thin line weights,
- substantial negative space,
- high information density without conventional PowerPoint hierarchy,
- small state glyphs rather than large text boxes,
- mathematical equations embedded as annotations,
- multiple related graph representations of the same underlying system.

Suggested semantic palette from the session templates:

- charcoal background: approximately `#121314`
- cyan/blue: physical/spatial graph
- orange: causal/update/interface relations
- red: failure/critical trajectories
- magenta: branchial/alternative-state relations
- green: viability/recovery/safe paths
- gray: annotation/projection/evidence guides

These exact hex values are project styling choices, not claims of exact Wolfram brand values.

---

## 4. Preferred production pipeline

\[
\boxed{\text{Wolfram Language computation}\to\text{SVG/PDF vectors}\to\text{Figma editable composition}\to\text{PDF/SVG/PNG export}.}
\]

Use Wolfram for mathematical graph generation when the graph has genuine computational meaning. Use Figma for layout, typography, editable annotations, and composition.

Draw.io is useful for clean causal/system diagrams but was judged less suitable than Figma for matching the complex Wolfram poster grammar.

---

## 5. Figma status

A Figma file was created during the session:

`https://www.figma.com/design/Iss9o33vEjRmHaODdkeuc6`

It contains an early boxed version and a later Wolfram-fidelity rebuild direction. The **Wolfram-fidelity rebuild** should be treated as the design direction; the boxed version should not be propagated.

Observed improvements in the rebuild direction:

- open field,
- central multiway/causal structure,
- dense spatial hypergraph,
- thin causal edges,
- sparse annotations,
- separate branchial and service/viability views.

Remaining goal: continue forensic reconstruction against the visual reference rather than merely polishing an infographic.

---

## 6. How the seven thesis candidates should become visuals

### Candidate 1 — Unified Sustainable Viability

Use viability/state-space geometry, causal evolution, lifecycle branchial alternatives, and central admissibility/viability structure.

### Candidate 2 — Dynamic Interface Identification

The poster itself should show:

- observed data streams,
- inferred interface graph,
- posterior distributions,
- uncertainty trajectories,
- deformed viability boundaries.

### Candidate 3 — Port-Hamiltonian Physics

Use energy-flow/port geometry, storage/dissipation structures, interconnection maps, and stability/passivity annotations.

### Candidate 4 — Stochastic Hybrid Physics

Use sample paths, mode-switching causal graphs, topology-changing events, failure/recovery branches, and rare-event structures.

### Candidate 5 — Lifecycle OR

Use state/action networks, branch-and-bound/decision-tree logic, network-flow structures, Pareto fronts, and multi-timescale pathways.

### Candidate 6 — People-Centric Service Viability

Use physical-state graph → service zones → population/service constraints → equity-aware viability geometry.

### Candidate 7 — Verified Scientific AI

Use physical system ↔ observations ↔ learned operator ↔ uncertainty ↔ formal safety/verification ↔ control in a closed computational loop.

---

## 7. Reproducibility assets

Session-generated source/template files are archived under this capsule's `reproducibility/` folder where possible, including Wolfram Language source and theme parameters.
