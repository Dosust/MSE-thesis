# Reproducibility Protocol for Future Chats and Thesis Work

## 1. Purpose

This protocol defines how future chats, code runs, figures, literature claims, mathematical objects and design artifacts should be recorded so the project remains scientifically auditable.

## 2. Minimum provenance record

Every important artifact or claim should be traceable through:

\[
\boxed{
\text{source}
\rightarrow
\text{mathematical object}
\rightarrow
\text{implementation}
\rightarrow
\text{run/configuration}
\rightarrow
\text{verification}
\rightarrow
\text{claim}
\rightarrow
\text{figure/table}
}
\]

Minimum fields:

- `claim_id`
- `claim_type`
- `source_id/url/doi/file_id`
- `source_version/date`
- `source_hash` where available
- `mathematical_object_id`
- `assumptions`
- `units/dimensions`
- `code_repository`
- `commit_sha`
- `script/notebook`
- `runtime/environment`
- `random_seed`
- `configuration_hash`
- `input_hashes`
- `output_hashes`
- `test_status`
- `tolerance/error_metric`
- `figure/table_id`
- `limitations`

## 3. Claim classes

Every statement should be classified as exactly one primary type:

### SOURCE_FACT
Directly supported by a source/document/dataset.

### MODEL_ASSUMPTION
Introduced to make the mathematical model tractable or meaningful.

### COMPUTED_RESULT
Produced by code/numerical experiment with reproducible inputs/configuration.

### RESEARCH_HYPOTHESIS
A falsifiable project proposition not yet established.

### FORMAL_RESULT
A proved theorem, verified certificate, or rigorously established mathematical result under explicit assumptions.

### DESIGN_CHOICE
A modeling, software, visualization or architecture decision.

### RECONSTRUCTED_MEMORY
Recovered from prior conversation context but not a verbatim source.

### UNVERIFIED_HISTORICAL_NOTE
Preserved because it may matter, but not yet checked.

## 4. Evidence levels

Use the S0–S4 evidence/status system:

- `S0` authoritative taxonomy/standard/official source;
- `S1` formal ontology relation;
- `S2` theorem/formal mathematical relation;
- `S3` peer-reviewed literature-supported relation;
- `S4` project hypothesis/proposed relation.

Do not infer S2 from S3, or S3 from S4.

## 5. Frozen thesis scope gate

Before new model development, verify that the proposed task respects the current frozen scope:

- executable sectors = P–T–W;
- Solid Waste = extension;
- core formal distinction = safe recovery reachability vs post-recovery controlled viability;
- required set semantics = `K_hard`, `K_R`, `K_R^V`, `B_R`;
- urban climate-stressed demonstrator;
- explicit service/equity/resource/administrative constraints;
- AI optional and subordinate to the physics/formal baseline.

Any scope change must be explicitly labeled `PROPOSED_SCOPE_CHANGE` until the user approves a new freeze.

## 6. Mathematical object registry

At minimum, register:

- state variables and dimensions;
- interface states/operators;
- disturbance/hazard variables;
- discrete modes;
- service maps;
- deprivation/cost/environment augmented states;
- admissible/hard sets;
- viable set/kernel;
- recovery/capture basin;
- controls/actions;
- design/intervention variables;
- objective/cost function;
- uncertainty sets/posteriors;
- solver/value functions.

Each object should record units, domain/codomain and interpretation.

## 7. Code verification gates

Before using code output as thesis evidence, require tests appropriate to the object.

### Physics/dynamics
- conservation residuals;
- dimensional consistency;
- boundary/initial condition tests;
- numerical convergence/stability;
- interface directionality tests.

### Observation/inference
- identifiability/observability diagnostics;
- calibration/posterior predictive checks;
- data leakage checks;
- OOD/domain-shift tests where ML is involved.

### Recovery/viability
- analytic/toy benchmark agreement;
- set-semantics tests (`K_hard` vs `K_R`);
- non-anticipative control chronology;
- grid/discretization convergence where applicable;
- boundary/classification error reporting.

### Optimization/OR
- feasibility checks;
- primal/dual or optimality-gap checks where available;
- sensitivity/robustness analysis;
- discrete decision consistency;
- budget/resource accounting.

### AI/surrogates
- physical residual checks;
- extreme-event/failure-region error;
- calibration/uncertainty;
- OOD performance;
- decision-classification fidelity relative to the reference model.

## 8. Monte Carlo rule

For stochastic experiments, store:

- pseudo-random generator/library version;
- seed;
- number of draws;
- distribution family and parameters;
- correlation/dependence assumptions;
- chunking/parallelism strategy;
- summary statistics and confidence intervals;
- convergence diagnostics;
- full configuration hash.

A large sample count does not validate an invalid distributional assumption.

## 9. Literature/PRISMA rule

Novelty claims require:

1. explicit search protocol;
2. database/source list;
3. deduplication;
4. inclusion/exclusion criteria;
5. single exclusion reason per excluded record where required;
6. counterevidence search;
7. primary-source verification for decisive claims;
8. evidence maturity labeling (peer-reviewed, preprint, official documentation, etc.);
9. claim-to-source ledger.

Do not use a Monte Carlo ranking before literature eligibility/admissibility gates.

## 10. Taxonomy/ontology rule

- Duke 2002 = optional educational browse taxonomy.
- MSC2020 = canonical scholarly classification.
- SKOS/RDF/OWL = typed ontology.
- OpenMath/OMDoc/MMT/theorem provers = mathematical semantics/formal dependency.

Taxonomy hierarchy must never be interpreted automatically as prerequisite, theorem dependency or physical causality.

## 11. Figure/design reproducibility

For each scientific visual, preserve:

- mathematical source object(s);
- data/model run IDs;
- plotting/generation code;
- SVG/PDF/vector source if available;
- raster export hash;
- Figma file/page/frame IDs if composed in Figma;
- typography/color theme file;
- annotation/source references;
- design-state label.

Reference visual principle:

\[
\boxed{\text{mathematics should become the visible structure, not merely text inside boxes}.}
\]

## 12. Future-chat startup checklist

Before a future chat changes the project:

1. read root conversation-memory README;
2. read correction ledger;
3. read frozen v0.5 state;
4. read current task-specific source files;
5. inspect live external state if the task depends on GitHub/Figma/current literature;
6. state whether a proposed change is `analysis`, `candidate`, or `frozen`;
7. do not silently overwrite a frozen decision.

## 13. Final thesis claim gate

A main thesis claim is eligible for final use only when it has:

\[
\boxed{
\text{literature rationale}
+
\text{defined mathematical object}
+
\text{implementation/formal derivation}
+
\text{verification/falsification}
+
\text{explicit limitation}
}
\]

If any term is missing, the claim remains provisional.
