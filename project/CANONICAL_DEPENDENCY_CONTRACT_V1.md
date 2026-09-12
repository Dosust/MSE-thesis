# Canonical Dependency Contract v1

![Authority](https://img.shields.io/badge/authority-CANONICAL-0969DA)
![Version](https://img.shields.io/badge/dependency%20contract-v1.0-1A7F37)
![Ontology](https://img.shields.io/badge/ontology-P--T--I--O%20RETAINED-1A7F37)

**Canonicalized:** 2026-09-12  
**Decision basis:** Phase-0 Theoretical Decision Gate v1.0, especially 0F minimum-sufficiency ablation and 0G final decision.  
**Scope:** Stage-2 directed infrastructure dependencies/interdependencies and their mapping into executable coupled dynamics.  
**Status:** CANONICAL DEPENDENCY REPRESENTATION v1.0.  
**Change rule:** Any structural change to the primitive dependency contract requires a new versioned gate or equivalent preregistered change-control process.

---

## 1. Canonical system boundary retained

The canonical thesis ontology remains

```math
\mathcal S=\{P,T,I,O\},
```

with

```math
P,T=\text{physical infrastructure systems},
\qquad
I,O=\text{informational and organizational layers}.
```

The seven-stage thesis architecture is unchanged.

This file revises only the **Stage-2 dependency/interdependency object**.

---

## 2. Canonical directed dependency object

For each accepted directed dependency `e`, define

```math
\boxed{
\mathfrak d_e
=
(\mathcal C_e,\Sigma_e,\Pi_e)
}
```

where

```math
\boxed{
\mathcal C_e
=
(s_e,p_e^s,r_e,p_e^r,\chi_e)
}
```

is the compositional/interface object,

```math
\boxed{
\Sigma_e
=
(\Phi_e,\gamma_e,\theta_e,\zeta_e)
}
```

is the causal/domain-semantic object, and

```math
\boxed{
\Pi_e
=
(\mathcal P_e,V_e,\mathcal U_e)
}
```

is the epistemic/provenance object.

This three-part structure is the minimum sufficient candidate supported by the Phase-0 ablation for the frozen Power–Transportation test domain.

---

## 3. Compositional/interface object `C_e`

```math
\mathcal C_e
=
(s_e,p_e^s,r_e,p_e^r,\chi_e).
```

| Symbol | Canonical meaning |
|---|---|
| `s_e` | typed source entity |
| `p_e^s` | source interaction point / port / interface location |
| `r_e` | typed receiver entity |
| `p_e^r` | receiver interaction point / port / interface location |
| `chi_e` | exchanged carrier, signal, service, command, authority or resource type |

Direction is encoded by the ordered source–receiver structure:

```math
s_e\rightarrow r_e.
```

`chi_e` is intentionally broader than a physical flow. Admissible examples include:

```text
electrical power;
charging demand;
traffic/access capacity;
forecast/data;
control command;
authority/permission;
crew/resource availability;
logistics constraint.
```

This prevents informational and organizational dependencies from being forced into artificial physical units.

---

## 4. Causal/domain-semantic object `Sigma_e`

```math
\Sigma_e
=
(\Phi_e,\gamma_e,\theta_e,\zeta_e).
```

| Symbol | Canonical meaning |
|---|---|
| `Phi_e` | causal coupling/transition operator describing how source information changes receiver evolution |
| `gamma_e` | activation/context guard |
| `theta_e` | identified/calibrated mechanism parameters, including delay when applicable |
| `zeta_e` | optional internal dependency state or memory |

The mechanism object must be sufficiently explicit to answer:

> Why and by what mathematical mechanism does the source affect the receiver?

A verbal label alone is insufficient when the dependency is used in simulation or prediction.

---

## 5. Continuous dependency realization

For a continuous receiving subsystem,

```math
\dot x_r(t)
=
F_r(x_r,u_r,h_r;\vartheta_r)
+
\gamma_e(t)\,
\Phi_e\!\left(
x_s^{[t-\bar\delta_e,t]},
x_r(t),
\zeta_e(t),
\nu(t);
\theta_e
\right).
```

The domain law remains distinct from the cross-domain coupling:

```math
\boxed{F_r\neq\Phi_e.}
```

In particular,

```math
F_P\neq F_T
```

in general.

The dependency modifies the receiving dynamics; it does not replace the receiving infrastructure physics.

---

## 6. Hybrid, logical and organizational realization

Not every dependency is appropriately represented by a continuous differential term.

For event-driven, logical, authority, restoration, switching or protection mechanisms, use

```math
x_r^+
=
\Psi_e(x_s,x_r,\zeta_e,\nu;\theta_e)
```

when

```math
\gamma_e(Y,h,u,t)=1.
```

This is the preferred representation when a continuous scalar coupling coefficient would be physically meaningless.

Examples include:

```text
road closure / access authorization;
repair-priority decisions;
protection/switching logic;
communication availability states;
resource-release decisions.
```

---

## 7. Internal dependency state and memory

`zeta_e` is optional.

Use

```math
\zeta_e=\varnothing
```

when the dependency is fully determined by source state, receiver state, exogenous context and current parameters.

When the dependency has independent internal state,

```math
\dot\zeta_e
=
g_e(\zeta_e,Y,h,u;\vartheta_e).
```

Examples may include communication availability, information freshness, authorization state, progressive interface degradation or a reduced state representation of relevant memory.

History must not be stored separately when an equivalent Markov state representation is available and justified.

---

## 8. Delay, timing and context

Delay is retained when physically or operationally relevant but is not a universal top-level primitive.

It may appear in

```math
\theta_e
```

or in the operator domain

```math
x_s^{[t-\bar\delta_e,t]}.
```

The thesis must continue to distinguish

```math
\text{event time}
\neq
\text{causal delay}
\neq
\text{characteristic timescale}.
```

Activation/context is governed by

```math
\gamma_e(Y,h,u,t).
```

A binary active/inactive quantity, when needed, is derived as

```math
a_e(t)
=
\mathbf 1_{\{\gamma_e(Y,h,u,t)=1\}}.
```

---

## 9. Epistemic/provenance object `Pi_e`

```math
\Pi_e
=
(\mathcal P_e,V_e,\mathcal U_e).
```

| Symbol | Canonical meaning |
|---|---|
| `P_e` | provenance/source chain supporting the dependency claim or parameterization |
| `V_e` | verification/validation/evidence status |
| `U_e` | epistemic and parameter-uncertainty description |

Recommended evidence states include:

```text
EVIDENCE_SUPPORTED;
MEASURED;
CALIBRATED;
HYPOTHESIZED;
INFERRED_PENDING_VERIFICATION;
REJECTED;
UNKNOWN/UNOBSERVED.
```

The epistemic object must remain distinct from physical system state:

```math
\boxed{
\text{uncertainty about the dependency}
\neq
\text{physical failure state of the dependency}.
}
```

W3C PROV-O or equivalent provenance structures may be used for implementation, but provenance semantics are not claimed as novel.

---

## 10. Executable realization is globally governed

The implementation of the causal semantics is represented by

```math
\boxed{
\mathcal X:\Sigma_e\mapsto\Xi_e
}
```

where `Xi_e` may be:

```text
native ODE/DAE term;
hybrid transition;
optimization constraint;
FMI model-variable/interface realization;
HELICS publication/subscription mapping;
validated numerical function;
other explicitly verified executable representation.
```

`Xi_e` is not a fourth primitive field of every dependency because the same semantic mechanism may admit several implementation technologies.

Executable semantics must never be mistaken for proof that the real-world dependency is physically valid.

---

## 11. Service consequence is system-level

Let

```math
Q(t)=G(Y(t))
```

be the declared service/capability map.

The required engineering chain is

```math
\boxed{
\Delta\mathfrak d_e
\rightarrow
\Delta\dot X_r
\rightarrow
\Delta X
\rightarrow
\Delta Q.
}
```

A dependency that cannot be traced to state or service consequence remains descriptive rather than fully engineering-operational for the thesis.

For controlled intervention analysis, a dependency contribution may be assessed through

```math
\Delta Q_e(t)
=
G(Y_e(t))-G(Y_{-e}(t)),
```

with all other conditions held fixed as far as the experiment permits.

---

## 12. Derived quantities — not universal primitives

The following are derived/reporting objects unless a later versioned experiment demonstrates otherwise.

### Relation class

```math
\rho_e
=
\mathcal R_{class}(\mathcal C_e,\Sigma_e).
```

Useful for indexing and reporting, but not primitive when full mechanism semantics are known.

### Structural existence

For realized dependency set `E`,

```math
M_e
=
\mathbf 1_{\{e\in\mathcal E\}}.
```

Potential/admissible dependencies belong to a separately declared candidate-edge set rather than forcing `M_e` into every realized relation.

### Influence strength

For a differentiable mechanism and declared norm,

```math
w_e(t)
=
\left\|D_{x_s}\Phi_e\right\|.
```

This value depends on operating point, scaling and norm. For non-smooth or hybrid mechanisms, another explicitly defined sensitivity/influence functional must be used.

Therefore a generic unqualified scalar `w_e` is prohibited as a universal primitive.

---

## 13. Canonical interdependency set

Let

```math
\mathbb I(t)
=
\{\mathfrak d_e(t):e\in\mathcal E(t)\}
```

be the active/represented dependency set.

A direct reciprocal interdependency exists when both directed dependencies are present:

```math
A\rightarrow B,
\qquad
B\rightarrow A.
```

A mediated system-level interdependency exists when directed paths return influence across domains, for example

```math
P\rightarrow T\rightarrow P.
```

Direct reciprocity between the same component pair is not required.

---

## 14. Legacy Phase-0 flat representation

The superseded pre-v1 canonical Stage-2 object was

```math
\mathfrak I_{ij}^{\alpha\beta}
=
(E_i^\alpha,E_j^\beta,M_{ij},w_{ij},\delta_{ij},\tau_{ij},a_{ij},m,\mathcal H_t).
```

It is retained only for provenance and interpretation of older Phase-0 files.

### Legacy-to-v1 migration

| Legacy content | v1 canonical location |
|---|---|
| `E_i^alpha,E_j^beta` | `s_e,r_e` in `C_e` |
| interface/channel information | `p_e^s,p_e^r` in `C_e` |
| exchanged quantity/signal/authority | `chi_e` in `C_e` |
| `m` | formalized as `Phi_e` in `Sigma_e` |
| `a_ij` / context | `gamma_e` in `Sigma_e` |
| `delta_ij` | parameter/operator-history semantics in `Sigma_e` |
| `tau_ij` | mechanism/system timescale, reported separately when needed |
| `H_t` | optional `zeta_e` or operator-history domain |
| evidence/uncertainty previously implicit | explicit `Pi_e` |
| `M_ij` | derived edge/admissibility membership |
| `w_ij` | derived influence/sensitivity functional |

Older notation must not be used as the active canonical dependency definition in new thesis text, code or figures.

---

## 15. Minimum executable Power–Transportation dependency set

Phase 1 will begin with three dependency classes so that all three primitive subobjects are exercised.

### `D_P` — physical dependency

```math
P_{feeder}
\rightarrow
T_{FCS}.
```

Representative mechanism: feeder voltage/power availability constrains charging power and therefore charging service/mobility.

### `D_I` — information-mediated dependency

```math
T_{EV\ forecast}
\rightarrow
P_{controller}.
```

Representative mechanism: forecast quality/latency changes the power-side charging/control decision.

### `D_O` — organizational/restoration dependency

```math
T_{road/access}
\rightarrow
P_{crew/restoration}.
```

Representative mechanism: road accessibility and authority/resource constraints alter feasible crew routing and restoration timing.

These are validation fixtures, not the complete thesis dependency set.

---

## 16. Identifiability requirement

Every parameter in `theta_e` used for calibration or prediction must have a declared record containing at least:

```text
symbol;
physical/operational meaning;
units;
source;
estimation/calibration method;
uncertainty model or bound;
identifiability status;
independent validation data;
epistemic status in Pi_e.
```

If a parameter is weakly identifiable or unidentifiable, it must not be silently tuned to obtain desired outputs.

---

## 17. Verification requirements

Before empirical validation, every executable dependency realization must pass at least:

```math
\Phi_e=0
```

recovers the uncoupled receiving model,

```math
\gamma_e=0
```

deactivates the relation,

and, where delay exists,

```math
\delta_e\rightarrow0
```

recovers the declared no-delay limit.

Additional checks include dimensional consistency, conservation where applicable, event-logic consistency, numerical convergence, timestep sensitivity and reproducibility.

---

## 18. Standards and external implementation anchors

The thesis may use the following established external anchors without treating them as thesis inventions:

```text
ISO 15118-20:2022 — EV/EVSE communication and bidirectional power-transfer messages;
FMI 3.0.2 — standardized dynamic-model exchange/co-simulation/scheduled execution;
W3C PROV-O — interoperable provenance semantics;
NASA-STD-7009B — model-and-simulation credibility practices;
ASME VVUQ terminology and applicable V&V guidance;
JCGM 100:2008 and supplements — measurement uncertainty principles.
```

Applicability must be declared per experiment; no standard is used outside its intended technical scope merely for authority.

---

## 19. Scientific claim boundary

This file canonically defines the thesis dependency representation.

It does **not** establish:

```text
universal minimality;
novelty of relation reification, provenance or compositional systems mathematics;
empirical correctness of Phi_e;
identifiability of theta_e;
predictive superiority;
viability/resilience improvement.
```

Those require Phase-1 validation and later Phase-2 resilience/viability experiments.

---

## 20. Canonical statement

> **A thesis dependency is represented as a typed directed interface/composition object, an explicit causal-domain semantic object, and a separate epistemic/provenance object. The causal semantics modify but do not replace the receiving infrastructure physics; executable realization and service consequence are governed by separate system-level maps.**
