# Mathematics Taxonomy Crosswalk — Duke 2002 vs MSC2020

## Purpose

The user supplied Duke University's 2002 **"Core Subject Taxonomy for Mathematical Sciences Education"** and asked for the project memory/knowledge architecture to be double-checked. The key correction is that this Duke taxonomy and MSC2020 serve different purposes and must not be merged semantically.

## A. Duke 2002: educational browse taxonomy

Source URL:
`https://sites.math.duke.edu/education/mathnsdl02/math-taxonomy-0202-1web.htm`

Source identity:
- "Final" Draft, February 2002;
- proposed by the Mathematical Sciences Conference Group on Digital Educational Resources;
- primary goal: provide a common subject taxonomy to which participating digital educational libraries/collections could map their internal subject taxonomies;
- design goal: human browsability with roughly limited branching per level.

Top-level categories:

1. Elementary Mathematics
2. Logic and Foundations
3. Algebra and Number Theory
4. Discrete Mathematics
5. Geometry
6. Calculus
7. Analysis
8. Differential and Difference Equations
9. Statistics and Probability
10. Applied Mathematics
11. Mathematics History

### Project role

Use Duke 2002 only as an optional **human-learning/navigation view** for explaining how mathematical topics relate pedagogically or browse-wise.

Do **not** treat a parent-child edge in this tree as:
- a theorem dependency;
- a prerequisite relation;
- physical causation;
- methodological necessity;
- evidence that one field is mathematically contained in another in the modern research sense.

## B. MSC2020: canonical scholarly research classification

Official sources:
- `https://msc2020.org/`
- `https://mathscinet.ams.org/mathscinet/msc/msc2020.html`
- `https://zbmath.org/classification/`

MSC2020 is maintained jointly by Mathematical Reviews and zbMATH and is the current Mathematics Subject Classification used to categorize mathematical research literature.

### Project role

Use MSC2020 as the **canonical research subject classification layer** for:
- literature indexing;
- mapping papers/methods to research areas;
- PRISMA corpus classification;
- identifying mathematical breadth/coverage;
- reproducible subject coding.

Do not transform MSC2020 into a causal or prerequisite graph. MSC codes classify subjects; they do not prove mathematical dependency.

## C. Four-layer mathematical knowledge architecture

The project should represent mathematical knowledge through four distinct layers.

### Layer 1 — Human educational navigation
Optional Duke 2002 educational taxonomy.

### Layer 2 — Research subject classification
MSC2020 / MSC2020-SKOS.

### Layer 3 — Typed semantic ontology
SKOS + RDF/OWL 2 relations such as:
- `broader/narrower`;
- `usesTheory`;
- `definesObject`;
- `implementsMethod`;
- `solvesTask`;
- `appliedToDomain`;
- `supportsClaim`;
- `requiresAssumption`.

### Layer 4 — Formal mathematical dependency
Definitions, axioms, assumptions, lemmas, theorems, proof objects and computational certificates represented through systems such as OMDoc/MMT, OpenMath and theorem provers.

A rigorous edge is therefore not simply

\[
A\to B,
\]

but

\[
\boxed{A\xrightarrow[\text{source/version/evidence}]{\text{typed relation}}B.}
\]

## D. Crosswalk for this thesis

The mappings below are project mappings, not claims that the taxonomies are equivalent.

| Thesis mathematical need | Duke 2002 navigation area | Typical MSC2020 research areas to inspect | Thesis role |
|---|---|---|---|
| Governing ODE/PDE dynamics | Differential and Difference Equations; Analysis | ODE/PDE/dynamical-systems classes | Chain I governing physics |
| Differential geometry / geometric mechanics | Geometry; Calculus; Analysis | Differential geometry; global analysis; mechanics-related classes | geometric structure, Port-Hamiltonian alternatives |
| Functional analysis/operator theory | Analysis | Functional analysis; operator theory | well-posedness, semigroups, PDE operators |
| Probability / stochastic processes | Statistics and Probability | Probability theory and stochastic processes | hazards, stochastic dynamics, uncertainty |
| Statistics / Bayesian inference | Statistics and Probability | Statistics | inverse inference, calibration, posterior UQ |
| Numerical analysis | Analysis | Numerical analysis | solvers, convergence, error control |
| Graph/network structure | Discrete Mathematics | Graph theory/combinatorics/network-relevant codes | infrastructure topology/interdependencies |
| Optimization / optimal control | Discrete Mathematics; Applied Mathematics; Calculus of Variations | calculus of variations, optimal control, optimization, OR-related codes | Chains IV–VI decision/control |
| Game theory | Discrete Mathematics | game theory/economics-related codes | adversarial disturbances, governance/strategic actors |
| Mathematical physics | Applied Mathematics | mathematical physics / mechanics / PDE-related MSC classes | Chain I physical foundations |
| Logic/formal proof | Logic and Foundations | mathematical logic and foundations | verification/formalization |
| AI/computation | Discrete Mathematics; Applied Mathematics | computer science, numerical/optimization/statistical learning-related codes | surrogate/acceleration layer only |

## E. Thesis-specific mathematical spine

The crosswalk should not force every mathematical topic into the thesis. The high-value spine is still:

\[
\boxed{
\text{Governing dynamics}
\rightarrow
\text{dynamic interfaces}
\rightarrow
\text{inverse/observational uncertainty}
\rightarrow
\text{service/admissibility sets}
\rightarrow
\text{reachability/viability}
\rightarrow
\text{minimum intervention/control}
}
\]

with the associated disciplines:

- nonlinear ODE/PDE and hybrid dynamical systems;
- network/interdependency mathematics;
- inverse problems and identifiability;
- probability, Bayesian inference and UQ;
- reachability, viability theory and Hamilton–Jacobi methods;
- control theory;
- optimization/Operations Research;
- numerical analysis and verified computation.

## F. Evidence/status rules for taxonomy mappings

Every mapping from a thesis object to a mathematical subject must carry a relation/status tag:

- `TAXONOMY_DUKE2002` — educational browse mapping;
- `MSC2020` — research classification mapping;
- `ONTOLOGY` — explicitly typed semantic relation;
- `THEOREM` — formal mathematical dependency/result;
- `LITERATURE` — supported by peer-reviewed application literature;
- `PROJECT` — proposed thesis relation/hypothesis.

This prevents visually attractive but scientifically invalid arrows.

## G. Version rule

Duke 2002 is preserved because the user explicitly supplied it and because it is useful for educational navigation. It does **not** replace MSC2020. If a future taxonomy is added, preserve the source/version and never silently overwrite the earlier scheme.
