# Phase 0 — Theoretical Foundation of Dynamic Infrastructure Interdependency

**Status:** ACTIVE WORKING FOUNDATION — not yet canonical.  
**Repository:** `Dossiya-SE/MSE-thesis`  
**Primary test domain:** Power–Transportation.  
**Relation to frozen thesis:** This document tests whether the current flat ontology `S={P,T,I,O}` should be retained or revised. It must not silently override `CANONICAL_SYSTEM_DEFINITION.md`, `FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md`, or the frozen seven-stage framework.

## Research purpose

The objective is not to create another Power–Transportation model. It is to determine whether a reusable mathematical language can represent heterogeneous infrastructure dependencies and interdependencies while preserving domain-specific physics, informational/control relations, organizational decision structures, time dependence, uncertainty, and service consequences.

```math
\boxed{\text{Infrastructure domains}\rightarrow\text{typed dependencies}\rightarrow\text{interdependencies}\rightarrow\text{dynamic SoS}\rightarrow\text{service consequences}}
```

The governing reasoning protocol is:

```math
\boxed{\text{LEARN}\rightarrow\text{VERIFY}\rightarrow\text{FORMULATE}\rightarrow\text{DERIVE}\rightarrow\text{TEST}\rightarrow\text{VALIDATE}\rightarrow\text{SYNTHESIZE}\rightarrow\text{ADVANCE}}
```

---

## 1. Established foundation [E]

### E1 — System-of-systems
A system-of-systems is not merely one large network. Constituent systems retain meaningful operational and managerial identity while contributing to higher-level capabilities. Power and Transportation therefore remain distinct engineered systems after coupling.

### E2 — Infrastructure interdependency
Dependency and reciprocal interdependency are established critical-infrastructure concepts. The contribution cannot be merely the statement that Power and Transportation are interdependent.

### E3 — Multilayer representation
Multilayer and network-of-networks mathematics already provide general representations for multiple node/edge types and cross-layer relations. Putting `P` and `T` into two layers is therefore not sufficient novelty.

### E4 — Physical, informational/control, and organizational dimensions
Existing cyber-physical and infrastructure-resilience frameworks already integrate physical/process, information/control, and human/organizational dimensions. Their inclusion is necessary but is not by itself a novelty claim.

### E5 — Dynamic coupling
Power–Transportation coupling varies with operating state, EV charging behavior, congestion, V2G, disturbances, control, and recovery. Static binary edges therefore cannot be presumed sufficient for every engineering question.

---

## 2. Current thesis ontology and Phase-0 challenge

The current frozen thesis uses

```math
\mathcal S=\{P,T,I,O\},
```

with `P,T` physical infrastructure systems and `I,O` informational and organizational layers.

Phase 0 tests a different abstraction:

```math
\boxed{\mathcal D=\{P,T,W,ICT,\ldots\}}
```

for infrastructure **domains**, and

```math
\boxed{\mathcal A=\{Ph,In,Or\}}
```

for cross-cutting **aspects**.

For the MSc test case:

```math
\begin{array}{c|ccc}
 & Ph & In & Or\\ \hline
P & P^{Ph} & P^{In} & P^{Or}\\
T & T^{Ph} & T^{In} & T^{Or}
\end{array}
```

This avoids treating Power/Transportation and Information/Organization as ontologically equivalent categories. It must, however, be accepted only if it improves representational clarity, composability, and engineering usefulness relative to the current canonical `P–T–I–O` ontology.

---

## 3. Constituent infrastructure system

For domain `alpha`, define

```math
\mathcal S_\alpha=(X_\alpha,F_\alpha,U_\alpha,Q_\alpha,B_\alpha),
```

where:

- `X_alpha`: system state;
- `F_alpha`: domain-specific governing laws;
- `U_alpha`: admissible controls/decisions;
- `Q_alpha`: delivered services/capabilities;
- `B_alpha`: system boundary.

### Foundational rule

```math
\boxed{\text{Common representation does not imply common physics.}}
```

Hence

```math
F_P\neq F_T
```

in general.

---

## 4. Working definitions

### 4.1 Interface [E]
An interface is the boundary, channel, component, or connection through which two functional units interact or exchange material, energy, information, commands, authority, or other relevant quantities.

### 4.2 Directed dependency [P]
Let

```math
Q_A=f_A(X_A,X_B,c).
```

System/entity `A` depends on `B` in declared context `c` when an admissible change in `B` can change the feasible state or service of `A` while the declared exogenous context is held fixed:

```math
\exists X_B,X_B'\;:\; f_A(X_A,X_B,c)\neq f_A(X_A,X_B',c).
```

For a differentiable local model, one possible local signature is

```math
\frac{\partial Q_A}{\partial X_B}\neq0.
```

This derivative is not a universal definition and is not required for non-smooth, hybrid, logical, or threshold dependencies.

### 4.3 Interdependency [E/P]
Direct reciprocal interdependency exists when

```math
A\rightarrow B
\quad\text{and}\quad
B\rightarrow A.
```

System-level interdependency may be mediated. Domains `alpha` and `beta` are interdependent over a declared context/horizon if an admissible dependency path exists from `alpha` to `beta` and another path returns influence from `beta` to `alpha`.

Thus

```math
P_{feeder}\rightarrow T_{charger}\rightarrow T_{road}\rightarrow P_{repair}
```

is a legitimate system-level `P\rightarrow T\rightarrow P` feedback even when no pair of components has a direct reciprocal edge.

### 4.4 Coupling operator [P]
A coupling operator is the mathematical realization of a dependency inside a receiving system model:

```math
\Phi_e:X_s\times X_r\times Z_e\rightarrow\Delta F_r.
```

The dependency is the relationship; `Phi_e` is how that relationship enters the equations or transition logic.

---

## 5. Primitive typed dependency contract [P]

For each directed dependency `e`, the current candidate contract is

```math
\boxed{\mathfrak d_e(t)=\left(s_e,r_e,\rho_e,m_e,q_e,M_e,z_e(t),w_e(t),\delta_e(t),c_e(t),U_e,\mathcal H_{e,t}\right)}
```

with:

| Field | Meaning |
|---|---|
| `s_e` | typed source entity |
| `r_e` | typed receiver entity |
| `rho_e` | relation class |
| `m_e` | physical/informational/organizational mechanism |
| `q_e` | transferred quantity, service, signal, or authority |
| `M_e` | structural existence/admissibility |
| `z_e(t)` | functional availability/state |
| `w_e(t)` | current influence/strength |
| `delta_e(t)` | delay/latency |
| `c_e(t)` | activation/context condition |
| `U_e` | evidence and uncertainty status |
| `H_{e,t}` | relevant history/memory |

Initial relation classes:

```math
\rho_e\in\{Physical\text{-}flow,\;Information/control,\;Organizational/authority,\;Spatial/common\text{-}cause\}.
```

Spatial/common-cause association must not automatically be promoted to a directional functional dependency.

---

## 6. Separate existence, state, and influence

These three objects must not be conflated:

```math
M_e\in\{0,1\}
```

(structural existence),

```math
z_e(t)\in[0,1]
```

(functional state), and

```math
w_e(t)=\omega_e(X(t),z_e(t),h(t),u(t),\mathcal H_{e,t})
```

(dynamic influence).

A relation can therefore exist structurally while being weak in one operating regime and dominant in another.

---

## 7. Epistemic status of dependencies

The physical system and our knowledge of it must remain distinct:

```math
\boxed{\mathcal D=\mathcal D_E\cup\mathcal D_H\cup\mathcal D_U}
```

where:

- `D_E`: evidence-supported dependencies;
- `D_H`: hypothesized/inferred dependencies;
- `D_U`: unknown/unobserved dependencies.

Candidate discovery does not imply acceptance:

```math
\boxed{\text{detect}\rightarrow\text{infer}\rightarrow\text{specify mechanism}\rightarrow\text{verify}\rightarrow\text{accept / retain uncertain / reject}}
```

Therefore

```math
\text{correlation}\neq\text{dependency}\neq\text{causal interdependency}.
```

---

## 8. Dynamic system-of-systems composition [P]

Let

```math
\mathcal V=\bigcup_{\alpha\in\mathcal D}\bigcup_{a\in\mathcal A}\mathcal V_\alpha^a
```

and

```math
\mathcal E(t)=\{\mathfrak d_1(t),\ldots,\mathfrak d_m(t)\}.
```

The proposed SoS representation is

```math
\boxed{\mathscr S(t)=\left(\mathcal D,\mathcal A,\mathcal V,\mathcal E(t),X(t),\mathcal F,\Phi,\mathcal Q,\mathcal U\right)}.
```

Sector-specific laws remain in

```math
\mathcal F=\{F_P,F_T,\ldots\},
```

and cross-system influence enters through

```math
\Phi=\{\Phi_e\}.
```

Continuous dynamics may be written generically as

```math
\dot X=F_q(X,\Phi,u,h),
```

with discrete transitions handled separately for hybrid modes/events.

Dependency state may evolve as

```math
\dot z_e=g_e(z_e,X,h,u;\theta_e),
```

with

```math
w_e=\omega_e(X,z_e,h,u,\mathcal H_{e,t}).
```

The central closed relation is

```math
\boxed{X(t)\rightarrow\mathfrak d(t)\rightarrow\Phi(t)\rightarrow\dot X(t)}.
```

Interpretation: system state changes effective dependencies; dependencies change system-state evolution.

---

## 9. Service/capability semantics

The framework is not accepted merely because it generates a richer graph.

Let

```math
\mathcal Q=\{Q_{electricity},Q_{mobility},Q_{emergency\ access},\ldots\}.
```

A useful representation must support the engineering chain

```math
\boxed{\Delta\mathfrak d\rightarrow\Delta X\rightarrow\Delta Q}.
```

If this cannot be demonstrated, the framework remains a taxonomy rather than an engineering model.

---

## 10. Power–Transportation verification cases

### V1 — EV charging interface

```math
P^{Ph}_{feeder}\rightarrow T^{Ph}_{FCS}\rightarrow Q_{mobility}
```

and

```math
T^{Ph}_{EV\ arrival}\rightarrow P^{Ph}_{charging\ demand}\rightarrow P^{Ph}_{feeder\ loading}.
```

### V2 — Restoration-access feedback

```math
P^{Ph}\downarrow\rightarrow T^{Ph}_{signals/charging}\downarrow\rightarrow T_{travel}\uparrow\rightarrow T_{crew}\uparrow\rightarrow T^P_{restoration}\uparrow.
```

This is a mediated system-level `P\rightarrow T\rightarrow P` feedback.

### V3 — Information-mediated coupling

```math
T^{In}_{EV\ forecast}\rightarrow P^{In}_{controller}\rightarrow P^{Ph}_{setpoint}.
```

### V4 — Organizational coupling

```math
T^{Or}_{road\ authority}\rightarrow O_{access\ decision}\rightarrow P^{Or}_{crew\ mobilization}\rightarrow P^{Ph}_{restoration}.
```

These cases must be used to test necessity of each field in the dependency contract rather than merely demonstrate that the notation can encode them.

---

## 11. Required falsification tests

The Phase-0 representation is retained only if it improves at least one engineering capability relative to simpler baselines.

### T0.1 Representation completeness
Can the grammar encode physical, informational, and organizational dependencies without introducing a new relation formalism for each case?

### T0.2 Directionality
Can it distinguish `P\rightarrow T` from `T\rightarrow P` and direct from mediated reciprocity?

### T0.3 Dynamics
Can the same structural dependency satisfy

```math
w_e(t_1)\neq w_e(t_2)
```

under different system states/contexts?

### T0.4 Composability
Can a third domain such as Water be added without changing the core contract?

### T0.5 Engineering consequence
Can a change in dependency representation produce a measurable change in state or service consequence?

### T0.6 Minimality
Which fields can be removed without losing explanation, prediction, or decision capability?

---

## 12. Phase-0 field-ablation plan

Start with the minimum relation

```math
M_0=(s,r)
```

and add fields incrementally:

```math
\begin{aligned}
M_1&=M_0+m,\\
M_2&=M_1+q,\\
M_3&=M_2+z(t),\\
M_4&=M_3+w(t),\\
M_5&=M_4+\delta(t),\\
M_6&=M_5+c(t),\\
M_7&=M_6+organizational\ semantics,\\
M_8&=M_7+evidence/uncertainty.
\end{aligned}
```

Compare each model on V1–V4 using common metrics for representation loss, prediction error where applicable, decision change, and model complexity.

### Null proposition

```math
H_{0,Phase0}:\;\text{the richer dependency contract adds no material explanatory, predictive, or decision value over a simpler multilayer representation.}
```

If this null cannot be rejected under defensible tests, the core grammar must be simplified.

---

## 13. Relationship to the seven-stage thesis

Phase 0 does not replace the seven stages. It defines the object that the seven stages study.

```math
\boxed{\underbrace{\mathfrak d_e(t),\mathfrak I(t),\mathscr S(t)}_{WHAT\ IS\ STUDIED}\quad+\quad\underbrace{Stages\ 1\text{--}7}_{HOW\ IT\ IS\ STUDIED}}
```

The current seven-stage architecture remains frozen until Phase 0 provides sufficient evidence for a formal versioned ontology revision.

---

## 14. Current Phase-0 verdict

Do not claim novelty for multilayer networks, physical–information–organization decomposition, dynamic coupling, or infrastructure interdependency in general.

The candidate residual contribution is narrower:

```math
\boxed{\text{a minimal typed, dynamic, mechanism-explicit, evidence-aware dependency contract that connects heterogeneous infrastructure models while preserving domain physics and service consequence}.}
```

This remains a **candidate** contribution until benchmarked against existing representation families and tested through the field-ablation programme.
