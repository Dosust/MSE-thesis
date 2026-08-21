# Decisions, Frozen Choices, and Open Research Questions

## A. Decisions treated as frozen unless new evidence requires revision

### A1. Use six interacting chains, not one giant linear chain

Frozen ontology:

1. Physical system
2. Observation/inference/prediction
3. Hazard/failure/consequence
4. Resilience/viability/recovery
5. Engineering design/operation/adaptation
6. Sustainability/equity/governance/decision

### A2. Distinguish chains from cross-cutting layers

- Chain = scientific transformation/progression.
- Layer = method, information structure, constraint, or value system acting across several chains.

### A3. Keep optimization cross-cutting

Optimization should not be placed as a single lifecycle stage after design. It can act on:

- design;
- operation;
- restoration;
- maintenance;
- planning;
- adaptation;
- policy/resource allocation.

### A4. Keep physical state, function, service, and consequence separate

Do not collapse:

`physical state → functional capacity → critical service → societal consequence`

into one resilience score.

### A5. Keep viability and recovery separate

- viability: can admissibility be maintained?
- reachability: what states can be reached?
- recoverability: can an inadmissible state return?
- recovery: what trajectory/process returns it?
- control: what intervention changes the trajectory?

### A6. Current thesis center

Primary mathematical center:

`Chain I + Chain IV`

Strong support:

`Chain II`

Chain III supplies hazard/failure/cascade mechanisms.

Chains V–VI provide engineering and decision demonstrations/constraints.

### A7. Current preferred thesis type

**Type I — theory-first mathematical physics** is the strongest present MSE fit.

Type II and III remain coherent alternatives/extensions.

### A8. Evidence discipline

Every equation/claim must be distinguished as:

- established/source-specific;
- canonical/general mathematical form;
- thesis-proposed synthesis.

### A9. Novelty discipline

Do not claim novelty for mature theories by themselves. Novelty must be falsified against the literature and concentrated in the integration/problem structure.

## B. Provisional thesis mathematical objects

These are working synthesis objects, not yet frozen as novel contributions:

### B1. Coupled hybrid state model

`M(X,m) Xdot = F(X,Z,m,u,eta;theta)`

### B2. Dynamic interface state/operator

`Z_ij(t)` or a more rigorous interface operator/law to be defined from sector physics and literature.

### B3. Service map

`Y = pi(X,Z,m)`

Need to define service variables, aggregation, population exposure mapping, and critical-service thresholds rigorously.

### B4. Sustainable/equitable admissible set

`K_SE`

Need to determine whether sustainability/equity constraints are state constraints, path constraints, cumulative constraints, terminal constraints, or multiple nested sets.

### B5. Viability / capture / reachability objects

- `Viab(K_SE)`
- reachable failure/avoid sets
- `Capt(K_SE)`

Need exact deterministic/robust/stochastic definitions and horizon conventions.

## C. Highest-priority open mathematical questions

### C1. What exactly is a dynamic infrastructure interface mathematically?

Need to decide whether an interface is best represented as:

- state variable;
- operator;
- constitutive relation;
- algebraic constraint;
- switching law;
- capacity function;
- boundary condition;
- graph/inter-layer edge with endogenous weight;
- hybrid combination of the above.

This should be derived from real P–W–T–SW mechanisms, not chosen only for mathematical convenience.

### C2. What is the minimal coupled model that remains physically meaningful?

The full P–W–T–SW system may be too high-dimensional for theorem-level analysis and HJ reachability.

Need a defensible reduction:

`full physical model → conservative reduced model → viability/reachability model`

with quantified approximation/model-reduction error if possible.

### C3. Well-posedness

For the selected reduced model:

- existence?
- uniqueness?
- continuous dependence?
- global vs local solution?
- positivity/invariance of physical states?
- treatment of algebraic constraints and switching?

### C4. Stability and interface-induced transitions

Can interface strength/condition trigger:

`stable service → degradation → cascade/critical transition`?

Need Lyapunov, spectral, bifurcation, monotonicity, input-to-state stability, or hybrid stability tools as appropriate.

### C5. Identifiability / inverse problem

Can dynamic interface parameters/structures be identified from realistic observations?

Need to distinguish:

- structural identifiability;
- practical identifiability;
- observability;
- posterior uncertainty;
- non-identifiability equivalence classes.

### C6. Uncertainty propagation into viability geometry

A particularly strong candidate research gap:

`D_obs → (G_hat_ij, theta_hat_ij) → Sigma_theta → V_sus,eq`

Need a mathematically defensible measure such as expected/set-distance error between true and inferred viability/recovery sets.

### C7. Service mapping

How should sector physical states map to:

- functionality;
- critical service;
- population served;
- equity-relevant service distribution?

This mapping may be one of the most consequential modelling choices.

### C8. Sustainability/equity geometry

Need to avoid arbitrary constraints. Determine literature-grounded indicators and whether they belong in:

- admissible state set;
- cumulative trajectory functional;
- multiobjective layer;
- robust decision layer;
- or a nested combination.

### C9. HJ/HJI tractability

High-dimensional HJ methods suffer from the curse of dimensionality.

Need to decide among:

- low-dimensional reduced HJ model;
- decomposition;
- monotone structure;
- reachable-set approximations;
- barrier certificates;
- neural approximations/operator learning as comparison/future extension;
- rare-event methods for stochastic variants.

### C10. Control vs optimization scope

The MSE thesis should likely first establish **feasible control/recoverability** before attempting a large global optimal-design problem.

Question order:

`Does a recovery control exist? → Which controls are robust? → Which one is optimal?`

## D. Highest-priority literature tasks

1. Deep Chain I literature map: sector physics → topology → interfaces → coupled dynamics → cascades.
2. Deep Chain IV map: viability → reachability → recoverability → resilience/control.
3. Chain II identifiability/UQ map.
4. Identify papers that explicitly model dynamic interfaces rather than static dependencies.
5. Identify papers that connect interface uncertainty to reachable/viable sets.
6. Identify papers that embed sustainability/equity as hard dynamic constraints rather than post-hoc metrics.
7. Separate generic mathematical foundations from infrastructure-specific implementations.

## E. Reproducibility tasks for future chats

For each candidate theorem/model:

- record exact source references;
- write all assumptions explicitly;
- define all spaces/domains/units;
- distinguish physical variables from service variables;
- state deterministic/stochastic setting;
- state time horizon;
- define admissible controls/disturbances;
- prove or cite well-posedness before simulation;
- verify numerical convergence;
- perform sensitivity/UQ;
- preserve code, config, seed, hashes, and output manifests.

## F. Current research objective — working wording

> Establish conditions under which a dynamically coupled P–W–T–SW infrastructure system with explicit interface mechanisms is well posed, identifiable, stable, sustainably/equitably viable, recoverable, and controllable under climate-driven disturbance and uncertainty.

This is a working objective and must still be narrowed to a feasible MSE theorem/computation scope.