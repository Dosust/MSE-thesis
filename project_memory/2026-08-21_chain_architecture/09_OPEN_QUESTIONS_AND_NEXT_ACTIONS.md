# Open Questions and Next Scientifically Valid Actions

This file preserves what is **not yet settled** so future chats do not mistake a framework for a finished thesis result.

## A. Immediate scientific understanding task

The next deep-dive task identified in the current discussion is:

> Decompose **Chain I** layer by layer for **Power, Water, Transportation and Solid Waste separately**, with established equations, assumptions, literature precedents and unresolved mathematical questions, before coupling the sectors.

Recommended order:

1. Power-sector physical laws and state variables.
2. Water/drainage physical laws and state variables.
3. Transportation flow dynamics and state variables.
4. Solid-waste accumulation/collection/drainage-blockage dynamics.
5. Cross-sector interdependencies.
6. Actual interface mechanisms.
7. Dynamic interface-state laws.
8. Timescales and mode-switching/failure rules.
9. Well-posedness / stability / sensitivity conditions.
10. Only then freeze the coupled forward model.

## B. Core mathematical questions still open

### B1. Forward-model well-posedness

For the selected coupled model:

- What state space is used?
- ODE, DAE, PDE, hybrid system or differential inclusion?
- What regularity/Lipschitz/monotonicity/constraint assumptions are defensible?
- Under what conditions do solutions exist?
- Under what conditions are they unique?
- Are switching events/Zeno behavior possible?
- Is continuous dependence on initial conditions/parameters guaranteed?

### B2. Interface definition

The thesis still needs an operational definition separating:

- network edge;
- interdependency;
- interface mechanism;
- interface state `Z_ij`;
- interface parameter `theta_ij`;
- interface failure mode.

This definition must be consistent across P–W–T–SW.

### B3. Dynamic versus static coupling

Need to prespecify:

- static baseline;
- dynamic interface law;
- timescale ratio(s);
- state-space error metric;
- viability-boundary error metric;
- threshold for declaring static approximation acceptable/unacceptable.

### B4. Admissible set operationalization

`K_R=K_phys ∩ K_service ∩ K_sus ∩ K_eq` is conceptually frozen, but actual constraints remain to be defined.

Need explicit units/thresholds for:

- physical feasibility;
- critical service continuity;
- sustainability;
- equity;
- possibly resource/budget constraints.

### B5. Service-to-population map

The thesis needs a transparent map from infrastructure state/service to affected population/groups before equity is computed.

### B6. Recovery definition

Need to freeze:

- target viable set;
- recovery horizon;
- admissible control set;
- recovery-time definition;
- whether the capture set is deterministic, robust, stochastic or nonanticipative.

### B7. Interface identifiability

Need to determine:

- what data are realistically observed;
- structural identifiability;
- practical identifiability;
- observability of hidden states;
- posterior/estimation uncertainty;
- how that uncertainty propagates into `V_R` / `C_R`.

### B8. Reduced-order model

If high-dimensional dynamics make viability computation infeasible, define a reduction with an explicit preservation/bounding objective for viability decisions rather than only low trajectory error.

## C. Evidence-review tasks still open

The global systematic-review status must be checked before any novelty freeze.

Potential pending tasks include:

- complete/reconcile Scopus export;
- Web of Science export;
- Compendex export;
- IEEE Xplore export;
- backward/forward citation search;
- deduplication;
- full-text eligibility decisions with one exclusion reason per record;
- extraction of exact evidence anchors for the chain/layer propositions;
- direct falsification search for each candidate gap.

Do not report these as complete unless the current repository/evidence table proves completion.

## D. Literature questions to falsify explicitly

1. Does literature already define dynamic infrastructure interfaces as state variables rather than static edges?
2. Does literature already propagate interface-identification uncertainty into viability/reachability sets?
3. Are timescale regimes for infrastructure interface approximation already characterized?
4. Has viability-boundary deformation already been used as interface criticality?
5. Has sustainability/equity already been imposed as hard viability constraints in coupled infrastructure?
6. Has capture-basin/minimum-recovery-time geometry been computed for coupled P–W–T–SW infrastructure?
7. Has dynamic waste–drainage–flood feedback been embedded in such a viability framework?
8. Do existing reduced-order methods provide conservative viability/reachability guarantees for this setting?

A direct precedent closes or narrows a proposed gap; that is a successful evidence result.

## E. Computational tasks

Current Python/Julia code is synthetic QA only. Future computational work should proceed in gates:

1. define sector equations and dimensions;
2. define interfaces and units;
3. write model schema/config;
4. deterministic forward-model tests;
5. stability/sensitivity tests;
6. observation/inverse-model tests;
7. uncertainty propagation;
8. viability/reachability solver benchmarking;
9. recovery/capture solver;
10. reduced-order comparison;
11. demonstrator calibration/validation;
12. only then policy/design optimization.

## F. Mathematical-art tasks

Existing figures are useful architecture pieces. Next scientific visuals should prioritize:

- phase/state-space viable/recoverable surfaces;
- vector fields around `∂V_R`;
- parameter-to-boundary sensitivity maps;
- dynamic/static boundary overlays;
- timescale-regime diagrams;
- posterior density → viability uncertainty visual;
- P–W–T–SW interface operator with physical units/mechanisms;
- flood/waste/drainage feedback loop;
- recovery-time level sets;
- Pareto front only after design/decision objectives are frozen.

## G. Scope decision still to freeze

Three viable thesis emphases remain:

- Type I theory-first;
- Type II digital-twin/inference-first;
- Type III resilience-by-design.

Current recommendation is Type-I-centered with Type-II upstream machinery and a limited Type-III downstream demonstration. This is a recommendation/state of discussion, not an irrevocable user decision unless later explicitly frozen.

## H. Publication/claim discipline

Never write:

- “globally novel” based only on corpus ranking;
- “mathematically proven” when a result is numerical;
- “validated” when only synthetic smoke tests were run;
- “digital twin” when only a model scaffold exists;
- “unique solution” without a uniqueness argument;
- “interface effect” when only correlation/topology was measured.

## I. Future-chat first action

Before doing new work, a future chat should read:

1. this memory capsule;
2. root `README.md`;
3. `project/MATHEMATICAL_FOUNDATION.md`;
4. `project/SCIENTIFIC_PROPOSITIONS.md`;
5. the current evidence/provenance files relevant to the requested task.

Then state which parts are frozen, which are evidence-supported, and which remain hypotheses.