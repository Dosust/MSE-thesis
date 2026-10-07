# Mathematical Framework Specification V3 — Thermal Interdependency, Resilience, and Two-Pathway Sustainability

**Status:** CANONICAL — CURRENT ACTIVE MATHEMATICAL FRAMEWORK  
**Effective date:** 2026-10-07  
**Scope authorities:** `CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md` + `CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md`  
**State-time authority:** `CANONICAL_STATE_TIME_DEFINITIONS_V1.md`  
**State-time alignment date:** 2026-10-08  
**Objective authority:** `CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md`  
**Resilience authority:** `CANONICAL_RESILIENCE_DEFINITION_V1.md`  
**Sustainability authority:** `CANONICAL_SUSTAINABILITY_TWO_PATHWAY_ASSESSMENT_V1.md`  
**Effectiveness / energy-efficiency authority:** `CANONICAL_EFFECTIVENESS_ENERGY_EFFICIENCY_PLACEMENT_V1.md`  
**System-boundary authority:** `CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md`  
**Supersedes for active mathematical work:** `MATHEMATICAL_FRAMEWORK_SPEC_V2_THERMAL.md`

## 1. Purpose

Formalize the active thermal-interdependency state-time problem and its downstream resilience and bounded two-pathway sustainability interpretation.

## Canonical state and time semantics

The mathematical framework uses the canonical definitions in `CANONICAL_STATE_TIME_DEFINITIONS_V1.md`.

```math
\dot X(t)=F(X(t),H(t),u(t);\theta)
```

has the following semantics:

- `X(t)` contains only admitted evolving physical/operational state variables required by the adopted model;
- `H(t)` is external extreme-heat forcing and is not itself a system state;
- `u(t)` is a control/operating input where used;
- `θ` contains parameters, not dynamic states unless explicitly reformulated.

Preserve:

```text
external forcing ≠ system state
physical quantity ≠ state variable ≠ active thesis state
thermal state ≠ operational/energy state
state ≠ capability ≠ service
transition time ≠ propagation delay ≠ service-consequence time ≠ recovery time
```

The exact active state vector remains OPEN. Candidate transformer, EVSE, battery, SOC, degradation, or health variables must pass the minimum-sufficient-physics and state-admission tests before activation.

## 2. Extreme-heat forcing

Let

```math
H(x,t)
```

denote the external extreme-heat forcing field or time series required by the adopted models.

```math
H(x,t) \neq X(t).
```

External heat forcing is not itself a system state.

## 3. Canonical state ontology

State semantics are controlled by `CANONICAL_STATE_TIME_DEFINITIONS_V1.md`.

The active state vector is model-dependent. A useful hierarchy is:

```math
X(t)
=
\begin{bmatrix}
X_P^{th}(t)\\
X_{T_e}^{th}(t)\\
X_{T_e}^{en}(t)\\
X^{deg}(t)
\end{bmatrix}_{active},
```

where only evidence-qualified and dynamically necessary blocks are activated.

- `X_P^{th}(t)`: admitted Power thermal states;
- `X_{T_e}^{th}(t)`: admitted Electrified-Transportation thermal states;
- `X_{T_e}^{en}(t)`: admitted operational/energy states such as SOC;
- `X^{deg}(t)`: admitted slow degradation/health states such as aging, only where materially relevant over the declared horizon.

Therefore:

```text
SOC is a state but not a thermal state
aging/degradation can be a state but is not automatically active
system-scope membership ≠ active model state
```

A generic dynamic representation is

```math
\dot X(t)
=
F\!\left(X(t),H(t),u(t);\theta\right).
```

No universal state vector or governing law is imposed across heterogeneous components.

## 4. External forcing and derived capability

Extreme heat is modeled as external forcing:

```math
H(x,t)\neq X(t).
```

A thermally conditioned capability is generally derived from state:

```math
C(t)=\mathcal C\!\left(X(t),H(t);\theta_C\right),
```

unless the selected physics demonstrates that an additional internal dynamic variable must be augmented into the state.

Thus:

```text
state ≠ capability
```

## 5. Thermal coupling object

Define

```math
Z_{PT}^{th}(t)
```

as the thermally relevant cross-system exchanged quantities, constraints, or interface conditions required to represent a qualified directional thermal dependency.

By default, `Z_{PT}^{th}` is an algebraic coupling object:

```math
Z_{PT}^{th}(t)
=
\Psi\!\left(X(t),H(t),u(t);\theta_Z\right).
```

It is promoted to an interface state only if the adopted physics gives it independent dynamic memory such that its current value is required to predict future evolution:

```math
\dot Z_{PT}^{th}
=
f_Z\!\left(Z_{PT}^{th},X,H,u;\theta_Z\right).
```

Therefore:

```text
coupling quantity ≠ state unless independent dynamics require it
```

and the coupling object is never a third physical infrastructure system.
## 6. Critical transition and propagation timing

For a thermally relevant state or capability constraint

```math
g_i(X_i^{th},H,t)\le 0,
```

define

```math
\tau_i^C
=
\inf\{t:g_i(X_i^{th}(t),H(t),t)=0\}.
```

For an admitted source transition `i` and receiver response `j`,

```math
\delta_{ij}^{th}
=
t_j^{response}-\tau_i^C.
```

Transition time, propagation delay, and recovery time remain distinct.

## 7. Service consequences

```math
Q_P(t)=G_P(X^{th}(t)),
\qquad
Q_T(t)=G_T(X^{th}(t)).
```

Required-service conditions are

```math
Q_P(t)\ge Q_P^{req}(t),
\qquad
Q_T(t)\ge Q_T^{req}(t).
```

A service deficit exists when

```math
Q_k(t)<Q_k^{req}(t).
```

## 8. Resilience interpretation

> **Resilience is the ability of the coupled Power and Electrified Transportation systems to maintain or recover required electricity and mobility services as thermal states and thermal interdependencies evolve over time.**

Candidate service-trajectory descriptors include minimum service level, service deficit, disruption duration, and recovery time.

```text
Thermal State ≠ Capability ≠ Service ≠ Resilience
```

## 9. Effectiveness of an engineering response

Effectiveness belongs to the resilience / engineering-response assessment.

For an engineering response (a), a generic effectiveness functional may be written as:

```math
E_{\mathrm{eff}}(a)
=
\mathcal E\!\left(
Q_P^{a}(\cdot),
Q_T^{a}(\cdot);
Q_P^{H}(\cdot),
Q_T^{H}(\cdot)
\right),
```

where the exact functional (\mathcal E) remains **OPEN** until the final resilience/service metrics are frozen.

Candidate components may include changes in service deficit, minimum service level, disruption duration, or recovery time.

```text
Effectiveness → Resilience / Engineering-Response Assessment
```

## 9. Sustainability vector

Define the sustainability indicator vector

```math
\mathbf S
=
\begin{bmatrix}
\mathbf S_{env}\\
\mathbf S_{econ}\\
\mathbf S_{soc}
\end{bmatrix}.
```

Each block may contain more than one indicator. The vector is not automatically reduced to one scalar score.

Representative indicator families are:

```text
Environmental: energy use, energy efficiency, electrical/conversion losses, GHG emissions, material-resource burden
Economic: operating, maintenance-replacement, intervention, service-disruption cost
Social: access, continuity, affordability, equity, safety
```

Only indicators supported by the scope, data, and causal interpretation are activated.

### Energy efficiency

When activated as an environmental-sustainability indicator:

```math
\eta_E
=
\frac{F_{service}}{E_{in}},
\qquad
I_E
=
\frac{E_{in}}{F_{service}}.
```

The exact useful-service quantity (F_{service}), energy-input boundary, units, and time horizon remain **OPEN**.

```text
Energy Efficiency → Environmental Sustainability
Effectiveness ≠ Energy Efficiency ≠ Sustainability
```

## 10. Three comparison cases

Define:

```math
\mathbf S_0
=
\text{sustainability indicators for the reference/baseline case},
```

```math
\mathbf S_H
=
\text{sustainability indicators under extreme heat without engineering response},
```

```math
\mathbf S_A
=
\text{sustainability indicators under extreme heat with engineering response}.
```

All three cases must use the same indicator definition, units, accounting boundary, time horizon, and comparison convention.

## 11. Pathway 1 — Direct sustainability consequence

The direct sustainability consequence of the thermal disturbance is

```math
\Delta\mathbf S_H
=
\mathbf S_H-\mathbf S_0.
```

This pathway represents:

```text
Thermal Interdependency
→ Electricity + Mobility Service Consequence
→ Environmental + Economic + Social Consequence
```

## 12. Pathway 2 — Engineering-response sustainability consequence

For an engineering response `a` from Improve, Adapt, or Restore, the response consequence is

```math
\Delta\mathbf S_A
=
\mathbf S_A-\mathbf S_H.
```

This pathway represents:

```text
Engineering Response
→ Changed State / Capability / Service
→ Environmental + Economic + Social Consequence
```

Total change relative to the reference case is

```math
\mathbf S_A-\mathbf S_0
=
(\mathbf S_H-\mathbf S_0)
+
(\mathbf S_A-\mathbf S_H).
```

This decomposition is descriptive, not a claim that all sustainability mechanisms are linearly additive in a causal sense.

## 13. Indicator directionality

Every indicator must declare whether larger values are beneficial or burdensome.

Examples:

- larger GHG emissions are burdensome;
- larger service access may be beneficial;
- larger cost is burdensome.

Therefore, the sign of a raw vector difference must not be interpreted uniformly across all indicators.

Any normalization, weighting, or aggregation requires an independent methodological justification.

## 14. Service / functional basis

Where scientifically appropriate, sustainability burdens or costs may be normalized by a declared electricity- or mobility-service functional unit:

```math
\frac{B_{env}}{F_{service}},
\qquad
\frac{C_{econ}}{F_{service}}.
```

The exact functional unit is OPEN until the service metrics and study boundary are frozen. Absolute system-level indicators remain valid when they are the correct decision quantities.

## 15. SDG linkage

SDG mapping is an interpretation step after measurement:

```text
Measured Sustainability Indicator
→ Sustainability Dimension
→ Relevant SDG Target / Indicator
```

No SDG target enters the governing thermal equations. Exact SDG targets remain OPEN until the corresponding measurable indicators are defined.

## 16. Anti-double-counting

A physical consequence may have distinct physical, monetary, and social representations, but these must remain labeled separately.

Do not sum overlapping representations without a justified aggregation method.

## 17. Active outputs

Primary thermal/service outputs:

```math
X_P^{th}(t),
\quad
X_{T_e}^{th}(t),
\quad
Z_{PT}^{th}(t),
\quad
\tau_i^C,
\quad
\delta_{ij}^{th},
\quad
Q_P(t),
\quad
Q_T(t).
```

Bounded downstream sustainability outputs, where activated:

```math
\mathbf S_0,
\quad
\mathbf S_H,
\quad
\mathbf S_A,
\quad
\Delta\mathbf S_H,
\quad
\Delta\mathbf S_A.
```

## 18. Excluded mathematical objects

The active framework does not require:

- generic organizational or information-network state;
- non-thermal dependency states;
- universal sustainability optimization;
- full LCA or social LCA;
- one scalar sustainability score;
- economy-wide economic models;
- all SDGs;
- generic intervention optimization.

## 19. Governing discipline

```text
minimum sufficient thermal physics
+ directional mechanism qualification
+ state-time traceability
+ service-based resilience interpretation
+ bounded two-pathway sustainability accounting
```

No equation or sustainability indicator enters the active thesis merely because it is mathematically or thematically available.
