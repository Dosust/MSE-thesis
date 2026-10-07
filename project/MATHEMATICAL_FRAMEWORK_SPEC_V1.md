# Mathematical Framework Specification V1

**Status:** CURRENT WORKING MATHEMATICAL-FRAMEWORK SPECIFICATION  
**Date:** 2026-10-07  
**Scope authorities:** `CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md` + `CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md` + `CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V3.md`  
**Conceptual counterpart:** `CONCEPTUAL_FRAMEWORK_SPEC_V3.md`

## 1. Purpose

Formalize the thesis focus on **thermal interdependencies between the Power System and Electrified Transportation System and their consequences through state and time**.

The framework does not represent every Power–Transportation interdependency. Non-thermal relations enter only when required as boundary conditions, coupling quantities, controls, or constraints for a thermal mechanism.

## 2. Extreme-heat forcing

\[
H(t)
=
[T_{\mathrm{amb}}(t),G_s(t),v_w(t),\ldots].
\]

Only forcing variables required by the governing thermal models are retained.

## 3. Thermal state

Power-system thermal states:

\[
X_{P,th}(t).
\]

Electrified Transportation thermal states:

\[
X_{T_e,th}(t).
\]

Coupled thermal state:

\[
X_{th}(t)
=
\begin{bmatrix}
X_{P,th}^{\top}(t) & X_{T_e,th}^{\top}(t)
\end{bmatrix}^{\top}.
\]

The Electrified Transportation System composition is broader than the active thermal-state vector. A component is modeled dynamically only when its thermal state is required to explain the thermal interdependency or its service consequence.

## 4. Thermal-conditioned coupling object

\[
Z_{PT}(t)
=
\mathcal Z
\left(
X_{P,th}(t),
X_{T_e,th}(t),
D(t),
u(t);
\theta_Z
\right).
\]

`Z_PT` contains the exchanged quantities, coupling conditions, or interface states required to represent the thermal interdependency, such as power, energy, current, charging demand, charging capability, or bidirectional transfer where supported.

`Z_PT` is not a third physical infrastructure system.

## 5. State-time dynamics

A general differential-algebraic structure is:

\[
\dot X_{th}
=
F_{th}
\left(
X_{th},H,Z_{PT},u;\theta
\right),
\]

\[
0
=
G
\left(
X_{th},Z_{PT},D,u;\theta
\right).
\]

Component laws remain heterogeneous. A transformer thermal model, EVSE thermal model, battery thermal model, connector thermal model, or auxiliary-load model is used only when required by the thermal mechanism being tested.

## 6. Thermal capability and constraints

For component or subsystem \(i\):

\[
C_i(t)
=
\mathcal C_i
\left(
X_{i,th}(t),
Z_{PT}(t);
\theta_i
\right),
\]

with operating or service-relevant constraint:

\[
g_i
\left(
X_{i,th}(t),
C_i(t),
Z_{PT}(t),
t
\right)
\le 0.
\]

This preserves the distinction:

\[
\text{thermal state}
\neq
\text{functional capability}
\neq
\text{service}.
\]

## 7. Thermal interdependency

A directional thermal interdependency is represented only when a thermally conditioned change in a source system changes the state, capability, or service consequence of the coupled receiver through an explicit physical pathway.

Conceptually:

\[
X_{P,th}
\rightarrow
Z_{PT}
\rightarrow
\{X_{T_e,th},C_{T_e},Q_T\}
\]

for \(P\rightarrow T_e\), and

\[
X_{T_e,th}
\rightarrow
Z_{PT}
\rightarrow
\{X_{P,th},C_P,Q_P\}
\]

for \(T_e\rightarrow P\), when the reverse thermal mechanism is physically supported.

Common heat exposure alone does not satisfy this definition.

## 8. Critical thermal transition time

For a physically justified thermal threshold:

\[
\tau_i^C
=
\inf
\left\{
t:
g_i
\left(
X_{i,th}(t),C_i(t),Z_{PT}(t),t
\right)
=0
\right\}.
\]

The threshold must have a physical or operational basis.

## 9. Thermal-interdependency propagation timing

For a qualified source transition and physically linked receiver response:

\[
\delta_{ij}^{th}
=
t_j^{\mathrm{response}}
-
\tau_i^C.
\]

This quantity is used only when the source–receiver thermal mechanism is established. It is not graph distance and is not automatically a cascade metric.

## 10. Service trajectories

\[
Q_P(t)
=
G_P
\left(
X_{th}(t),Z_{PT}(t)
\right),
\]

\[
Q_T(t)
=
G_T
\left(
X_{th}(t),Z_{PT}(t)
\right).
\]

Service requirements are represented separately:

\[
Q_P(t)\ge Q_P^{req}(t),
\qquad
Q_T(t)\ge Q_T^{req}(t).
\]

Exact service definitions remain OPEN until their operational indicators and thresholds are frozen.

## 11. Verification and validation

The framework requires separate checks for:

- governing-equation and dimensional consistency;
- numerical verification and convergence;
- parameter and threshold provenance;
- comparison with empirical, experimental, or benchmark thermal behavior;
- service-level validation where appropriate;
- uncertainty and sensitivity;
- declared validity boundaries.

Permanent rule:

\[
\text{simulation}
\neq
\text{validation}.
\]

## 12. Engineering interventions

### Improve

\[
\theta' = \theta + \Delta\theta.
\]

Improve changes baseline thermal capability, design, or physical parameters before the heat event.

### Adapt

\[
u_A(t).
\]

Adapt changes operation while thermal states evolve.

### Restore

\[
u_R(t).
\]

Restore changes the post-degradation recovery trajectory.

An intervention is included only when it changes a thermal state, thermal capability, thermal-interdependency consequence, or electricity/mobility service outcome.

## 13. Resilience performance

A structural resilience functional may be written as:

\[
R
=
\mathcal R
\left(
Q_P(\cdot),
Q_T(\cdot),
\tau^C,
\delta^{th},
\theta',
u_A,
u_R
\right).
\]

The exact resilience metric remains OPEN.

## 14. Bounded sustainability consequences

Sustainability is not modeled as a separate broad system. Consequences are admitted only when they arise from the bounded resilience interventions and are supported by a declared accounting boundary.

A consequence vector may be represented as:

\[
S
=
[S_{env},S_{econ},S_{service}]^{\top},
\]

with exact indicators left OPEN until data and accounting boundaries are frozen.

Resilience improvement does not imply sustainability improvement.

## 15. Visual encoding requirement

Every mathematical figure must preserve the active chain:

`extreme heat → thermal state → thermal capability/constraint → thermal interdependency → state-time consequence → service consequence → resilience response`

No non-thermal interdependency is shown as part of the active thesis mechanism unless it is explicitly labeled as a supporting boundary condition or constraint.

## 16. Terminology rule

Use **qualify** consistently.

In objectives and scope statements, name the physical object or variable class directly.

Use **Electrified Transportation System**; do not use “standards-defined” as part of the system name.
