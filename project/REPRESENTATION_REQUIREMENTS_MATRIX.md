# Representation Requirements Matrix — Phase 0 v1.0

**Status:** FROZEN BEFORE COMPARATIVE SCORING  
**Purpose:** define what an infrastructure-interdependency representation must be able to express before comparing the frozen thesis ontology `M_0` with the Phase-0 candidate `M_1`.  
**Anti-bias rule:** these requirements and test cases are fixed before either representation is scored. Any later modification requires a version increment and invalidates prior comparative scoring.

## 1. Competing representations

### Baseline `M_0` — current canonical thesis ontology

```math
M_0:\qquad
\mathcal S=\{P,T,I,O\},
```

with `P,T` as physical infrastructure systems and `I,O` as informational and organizational layers.

### Candidate `M_1` — domain × aspect ontology

```math
M_1:\qquad
(\alpha,a)\in\mathcal D\times\mathcal A,
```

with

```math
\mathcal D=\{P,T,W,ICT,\ldots\},
\qquad
\mathcal A=\{Ph,In,Or\}.
```

For the MSc test case:

```math
\begin{array}{c|ccc}
 & Ph & In & Or\\ \hline
P & P^{Ph} & P^{In} & P^{Or}\\
T & T^{Ph} & T^{In} & T^{Or}
\end{array}
```

No result in this file presumes that `M_1` is superior.

---

## 2. Scoring rule

For representation `M` and requirement `R_k`, define

```math
s_k(M)\in\{0,1,2\},
```

where:

- `0` = the requirement cannot be represented without changing the ontology or adding an external formalism;
- `1` = representable, but only implicitly, ambiguously, or through ad hoc conventions not native to the representation;
- `2` = represented explicitly, consistently, and without changing the core grammar.

The unweighted diagnostic score is

```math
S_{diag}(M)=\sum_{k=1}^{12}s_k(M).
```

**Important:** `S_diag` is descriptive only. It cannot by itself decide RETAIN/REVISE/REPLACE because a high total score can conceal a fatal deficiency.

---

## 3. Frozen requirements

| ID | Requirement | Exact capability demanded | Failure condition | Verification evidence |
|---|---|---|---|---|
| `R1` | Constituent-system identity | Preserve Power and Transportation as independently meaningful engineered systems with their own states, services, controls and boundaries | `P` or `T` becomes only an arbitrary layer label with no independent system semantics | V1, V4, V5 + system definition audit |
| `R2` | Mechanism explicitness | Represent **why/how** a relation affects the receiver, not only that an edge exists | Relation can be encoded only as adjacency/correlation with no mechanism semantics | V1–V4 + dependency-object audit |
| `R3` | Directionality | Distinguish `P→T` from `T→P`, direct from mediated reciprocity, and dependency from interdependency | Direction is lost, forced symmetric, or ambiguously inferred | V1, V4 |
| `R4` | Informational relations | Represent sensing, communication, information quality, estimation/signaling and information-mediated cross-domain effects | Information must be collapsed into physical state or represented outside the ontology | V2 |
| `R5` | Organizational relations | Represent authority, coordination, decision, resources, mobilization and organizational cross-domain effects | Organizational mechanisms are only free-text metadata or cannot alter feasible action/state | V3 |
| `R6` | State dependence | Allow the effective importance/state of a dependency to change with operating state, disturbance, control or recovery | Every relation is structurally fixed and functionally constant | V1, V4 + dynamic-state test |
| `R7` | Time and delay | Distinguish event time, causal delay/latency, characteristic timescale and time-varying relation state | Temporal behavior can only be represented by external annotation or one undifferentiated time scalar | V2–V4 |
| `R8` | Feedback and mediated reciprocity | Represent `P→T→P` loops even when reciprocal influence is not between the same component pair | Only direct pairwise bidirectional edges count as interdependency | V4 |
| `R9` | Evidence/uncertainty status | Distinguish physical relation state from our confidence/evidence about whether the relation exists or is parameterized correctly | Epistemic uncertainty is conflated with physical failure probability or omitted | V1–V5 + evidence audit |
| `R10` | Service consequence | Connect relation changes to system state and measurable service/capability consequence | Representation ends at topology/ontology and cannot support `Δd→ΔX→ΔQ` | V1, V4 |
| `R11` | Physics preservation | Preserve separate domain laws such as `F_P` and `F_T` while enabling cross-domain coupling | Unification requires replacing domain physics with one generic network rule | V1, V4 + governing-law audit |
| `R12` | Extensibility/composability | Add a third infrastructure domain without redesigning the dependency grammar or reclassifying existing domains inconsistently | Adding Water/ICT requires a new ontology or new relation formalism | V5 |

All twelve requirements are **substantive** because the research objective explicitly includes physical, informational, organizational, dynamic, evidential, service and extensibility concerns. No requirement may be dropped after scoring begins because a candidate performs poorly on it.

---

## 4. Essential decision gates

The theoretical decision is not a weighted popularity contest. Five non-compensable gates are defined.

### `G1` — Ontological correctness

A candidate must preserve category distinctions and avoid contradictions among system, aspect, interface, dependency, interdependency and coupling.

Relevant requirements:

```math
\{R_1,R_2,R_3\}.
```

### `G2` — Dynamic causal adequacy

A candidate must represent state-dependent, time-dependent, directional mechanisms and mediated feedback.

Relevant requirements:

```math
\{R_2,R_3,R_6,R_7,R_8\}.
```

### `G3` — Socio-technical adequacy

A candidate must represent information and organization as active mechanisms capable of changing system evolution or feasible control, not merely annotations.

Relevant requirements:

```math
\{R_4,R_5\}.
```

### `G4` — Engineering adequacy

A candidate must preserve domain physics and map relation changes to service consequences.

Relevant requirements:

```math
\{R_{10},R_{11}\}.
```

### `G5` — Reusability and evidence discipline

A candidate must separate epistemic uncertainty from physical state and remain composable when a new infrastructure domain is added.

Relevant requirements:

```math
\{R_9,R_{12}\}.
```

A representation that fails any complete gate cannot be selected as the final canonical replacement regardless of `S_diag`.

---

## 5. Frozen verification cases

The same cases must be encoded under `M_0` and `M_1`. No representation receives a tailored easier case.

### `V1` — EV charging: reciprocal physical coupling

Power-to-transport:

```math
P^{Ph}_{feeder}
\rightarrow
T^{Ph}_{FCS}
\rightarrow
Q_{mobility}.
```

Transport-to-power:

```math
T^{Ph}_{EV\ arrival}
\rightarrow
P^{Ph}_{charging\ demand}
\rightarrow
P^{Ph}_{feeder\ loading}.
```

Required demonstration:

1. preserve direction;
2. distinguish the two mechanisms;
3. preserve power and transport physics;
4. produce a service consequence.

### `V2` — Information-mediated coupling

```math
T^{In}_{EV\ forecast}
\rightarrow
P^{In}_{controller}
\rightarrow
P^{Ph}_{setpoint}.
```

Required demonstration:

1. information is not confused with the physical transport system;
2. information quality/latency can change the receiving control action;
3. the chain can terminate in a physical consequence.

### `V3` — Organizational coupling

```math
T^{Or}_{road\ authority}
\rightarrow
T^{Ph}_{access}
\rightarrow
P^{Or}_{crew\ mobilization}
\rightarrow
P^{Ph}_{restoration}.
```

Required demonstration:

1. authority/coordination is distinct from physical accessibility;
2. organizational state can alter feasible action or response time;
3. the effect can propagate into restoration/service outcomes.

### `V4` — Mediated feedback/cascade

```math
P^{Ph}\downarrow
\rightarrow
T^{Ph}_{charging/signals}\downarrow
\rightarrow
T_{travel}\uparrow
\rightarrow
T_{crew}\uparrow
\rightarrow
T^{P}_{restoration}\uparrow.
```

Required demonstration:

```math
P\rightarrow T\rightarrow P
```

without forcing a reciprocal edge between the same asset pair.

The representation must distinguish common-cause failure from induced propagation.

### `V5` — Extensibility stress test

Add Water as a third domain:

```math
\mathcal D' = \{P,T,W\}.
```

Required demonstration:

1. no core dependency field is redefined;
2. existing `P–T` relations retain the same semantics;
3. `W` receives its own physics `F_W`;
4. new `P–W`, `T–W`, information and organizational relations use the same grammar.

---

## 6. Complexity audit

Representational richness is not automatically improvement. For each model record:

```math
C(M)
=
\left(
N_{objects},
N_{relation\ types},
N_{required\ parameters},
N_{assumptions},
N_{ad\ hoc\ exceptions},
N_{external\ formalisms}
\right).
```

No arbitrary scalar complexity weight is used in v1.0. Complexity is compared component-wise.

A richer candidate is justified only when the added structure resolves a documented deficiency or changes explanation, identifiability, prediction or engineering decision.

---

## 7. Comparative hypothesis

### Null proposition

```math
H_{0,GATE}:
M_1\text{ provides no necessary representational or engineering capability beyond }M_0.
```

### Alternative proposition

```math
H_{1,GATE}:
M_1\text{ resolves at least one material deficiency of }M_0
```

without violating domain physics or introducing unjustified complexity.

This is a theoretical/model-comparison proposition, not a frequentist statistical hypothesis unless later experiments provide stochastic observables.

---

## 8. Decision rule — frozen before scoring

### RETAIN `M_0`

Return **RETAIN** when:

1. `M_1` adds no capability needed by `R_1–R_{12}` that cannot already be represented cleanly in `M_0`; or
2. any apparent improvement is only notational while engineering interpretation and test outcomes are unchanged; or
3. `M_1` introduces additional ontological/parameter complexity without resolving a documented failure of `M_0`.

### REVISE `M_0`

Return **REVISE** when:

1. one or more components of `M_1` materially improve clarity, composability or mechanism representation;
2. `M_0` can absorb those improvements without replacing its entire system identity; and
3. the resulting hybrid revision passes `G1–G5` better than either unmodified representation.

### REPLACE `M_0` with `M_1`

Return **REPLACE** only when all are true:

1. `M_0` fails at least one non-compensable gate `G1–G5` on the frozen cases;
2. the failure cannot be repaired without changing the fundamental ontology of `M_0`;
3. `M_1` passes all five gates without an ad hoc exception on `V1–V5`;
4. `M_1` preserves `F_P\neq F_T` and adds `F_W` in `V5` without grammar redesign;
5. the additional complexity of `M_1` is traceably necessary for at least one explanatory, identification, prediction or decision capability.

This high threshold protects the frozen thesis from unnecessary framework churn.

---

## 9. Required result table

After Phase 0C–0F, fill this table without changing the requirements.

| Requirement | `M_0` score | `M_1` score | Evidence | Case(s) | Complexity consequence | Verdict |
|---|---:|---:|---|---|---|---|
| R1 | TBD | TBD | TBD | V1/V4/V5 | TBD | TBD |
| R2 | TBD | TBD | TBD | V1–V4 | TBD | TBD |
| R3 | TBD | TBD | TBD | V1/V4 | TBD | TBD |
| R4 | TBD | TBD | TBD | V2 | TBD | TBD |
| R5 | TBD | TBD | TBD | V3 | TBD | TBD |
| R6 | TBD | TBD | TBD | V1/V4 | TBD | TBD |
| R7 | TBD | TBD | TBD | V2–V4 | TBD | TBD |
| R8 | TBD | TBD | TBD | V4 | TBD | TBD |
| R9 | TBD | TBD | TBD | V1–V5 | TBD | TBD |
| R10 | TBD | TBD | TBD | V1/V4 | TBD | TBD |
| R11 | TBD | TBD | TBD | V1/V4 | TBD | TBD |
| R12 | TBD | TBD | TBD | V5 | TBD | TBD |

No score may be entered without an evidence note or explicit derivation.
