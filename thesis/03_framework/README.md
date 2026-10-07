# Chapter 3 — Conceptual and Mathematical Framework

**Thesis title:** **Physics-Based Mathematical Engineering of Power–Transportation Interdependencies for Resilience**  
**Current-scope authority:** [`../../project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md`](../../project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md)  
**State-time definition authority:** [`../../project/CANONICAL_STATE_TIME_DEFINITIONS_V1.md`](../../project/CANONICAL_STATE_TIME_DEFINITIONS_V1.md)  
**Conceptual framework:** [`../../project/CONCEPTUAL_FRAMEWORK_SPEC_V5_THERMAL_SUSTAINABILITY.md`](../../project/CONCEPTUAL_FRAMEWORK_SPEC_V5_THERMAL_SUSTAINABILITY.md)  
**Mathematical framework:** [`../../project/MATHEMATICAL_FRAMEWORK_SPEC_V3_THERMAL_SUSTAINABILITY.md`](../../project/MATHEMATICAL_FRAMEWORK_SPEC_V3_THERMAL_SUSTAINABILITY.md)  
**Status:** CURRENT ACTIVE FRAMEWORK  
**Date:** 2026-10-08

## Purpose

Chapter 3 formalizes how extreme heat changes selected Power and Electrified-Transportation states through time, how qualified thermal interdependencies transmit consequences, how those consequences affect electricity and mobility services, and how service trajectories support resilience interpretation and bounded downstream sustainability assessment.

## Required section

- [3.1 Canonical State-Time Definitions](03_01_state_time_definitions.md)

## System boundary

```text
Power System P
↔
Electrified Transportation System T_e
```

EVSE belongs to `T_e`. The cross-system coupling object does not form a third physical infrastructure system.

## External forcing

```math
H(x,t)
```

represents extreme-heat forcing.

```text
external forcing ≠ internal system state
```

## State architecture

The thesis distinguishes the full physical state space from the active reduced model state.

```math
X(t)
=
\begin{bmatrix}
X_P^{th}(t)\\
X_{T_e}^{th}(t)\\
X_{T_e}^{en}(t)\\
X^{deg}(t)
\end{bmatrix}_{active}.
```

Only dynamically necessary and evidence-supported blocks are activated.

Examples:

```text
thermal state: transformer top-oil / hot-spot temperature, EVSE temperature
energy state: SOC
slow degradation state: transformer insulation aging/health, only if materially relevant
```

## Coupling architecture

```math
Z_{PT}^{th}(t)
```

represents the thermally relevant cross-system exchange, constraint, or interface condition.

By default it is an algebraic coupling object:

```math
Z_{PT}^{th}(t)
=
\Psi(X,H,u;\theta_Z).
```

It becomes an interface state only when independent dynamics/memory are physically required.

## Dynamics

```math
\dot X(t)
=
F(X,H,u;\theta).
```

Use **minimum sufficient physics**.

## Capability mapping

```math
C(t)=\mathcal C(X(t),H(t);\theta_C).
```

```text
state ≠ capability
```

## Critical transition

For a declared and evidence-supported boundary:

```math
\tau_i^C
=
\inf\{t:g_i(X_i(t),H(t),t)=0\}.
```

A temperature crossing is not automatically a critical transition unless the boundary has physical or operational meaning.

## Propagation timing

For a qualified directional mechanism:

```math
\delta_{ij}^{th}
=
t_j^{response}
-
\tau_i^C.
```

Propagation delay is not graph distance and is not inferred from correlation alone.

## Service mapping

```text
physical / operational state
→ capability
→ cross-system consequence
→ electricity or mobility service
```

```math
Q_P(t),\qquad Q_T(t).
```

```text
state ≠ capability ≠ service
```

## Temporal distinctions

```text
heat-event onset / exposure duration
≠ critical transition time
≠ interdependency propagation delay
≠ service-disruption onset
≠ operational departure deadline
≠ recovery time
≠ degradation / aging horizon
```

## Resilience and sustainability

Resilience is interpreted from service trajectories through time under `CANONICAL_RESILIENCE_DEFINITION_V1.md`.

Sustainability is a bounded downstream assessment under `CANONICAL_SUSTAINABILITY_TWO_PATHWAY_ASSESSMENT_V1.md`.

```text
Thermal State ≠ Capability ≠ Service ≠ Resilience ≠ Sustainability
```

## Exit gate

Chapter 3 is ready only when:

- exact charging/application context is frozen;
- admitted state variables and units are defined;
- forcing and initial conditions are defined;
- directional thermal mechanisms are qualified;
- coupling objects are classified as algebraic or dynamic;
- governing equations and parameters are evidence-supported;
- thresholds/capability laws are defensible;
- service mappings are operationalized;
- transition, propagation, and any recovery/degradation times are precisely defined;
- assumptions, uncertainty, and validity domains are recorded;
- figures pass semantic, mathematical, and visual QA.
