# MSE Thesis Scope

**Status:** CANONICAL CURRENT ACTIVE SCOPE — 2026-10-08  
**Thermal focus authority:** [`CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md`](CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md)  
**State-time amendment:** [`CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md`](CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md)  
**Canonical state-time definitions:** [`CANONICAL_STATE_TIME_DEFINITIONS_V1.md`](CANONICAL_STATE_TIME_DEFINITIONS_V1.md)  
**Objective authority:** [`CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md`](CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md)  
**Electrified Transportation boundary:** [`CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md`](CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md)

## Permanent active focus

The thesis studies **only thermal interdependencies between the Power System and Electrified Transportation System and their consequences through physical state and time**.

```text
Extreme heat
→ thermal physical state
→ thermal capability / constraint
→ qualified thermal P ↔ T_e interdependency
→ state-time evolution
→ critical transition / propagation timing
→ electricity + mobility service consequence
```

## Physical core

```text
Power System P
↔
Electrified Transportation System T_e
```

EVSE belongs to `T_e`. Coupling/interface variables are mathematical exchange/constraint objects and are not a third physical system.

## Thermal-interdependency rule

A relation is active only when a heat- or temperature-dependent physical state, thermal capability, or thermally conditioned operating limit changes the activation, magnitude, capacity, timing, or consequence of a directional Power–Electrified Transportation dependency.

```text
common heat exposure ≠ thermal interdependency
connection ≠ dependency
thermal state ≠ function ≠ service
```

## Analytical dimensions

Primary dimensions:

```text
state + time
```

Primary derived quantities may include:

```math
\tau_i^C,
\qquad
\delta_{ij}^{th},
\qquad
Q_P(t),
\qquad
Q_T(t).
```

## Canonical meaning of state and time

State and time are governed by `CANONICAL_STATE_TIME_DEFINITIONS_V1.md`.

```text
State:
minimum evolving physical, operational, energy, or degradation variables
needed to characterize the current modeled condition and predict subsequent evolution.

Time:
independent variable through which state evolution, critical transitions,
interdependency propagation, service consequences, and—where modeled—recovery
and degradation are ordered and quantified.
```

Preserve:

```text
full physical state space ≠ active reduced thesis state vector
external forcing ≠ state
thermal state ≠ operational/energy state
fast state ≠ slow degradation/health state
state ≠ capability ≠ service
coupling quantity ≠ state unless independent dynamics require it
```

SOC is an energy state, not a thermal state. Aging/degradation may be a legitimate slow state, but it is activated only when its evolution materially affects the admitted thermal mechanism or consequence over the declared horizon.

## Frozen research objectives

**General Objective**

> To characterize and model thermal interdependencies between the Power System and the Electrified Transportation System under extreme heat, and to quantify how their consequences evolve through physical state and time.

**SO1 — Identify and qualify**

> Identify and qualify the thermally sensitive physical states and directional thermal interdependency mechanisms connecting the Power System and the Electrified Transportation System.

**SO2 — Model state-time evolution**

> Develop a physics-based state-time model of the qualified thermal interdependencies and their propagation under extreme heat.

**SO3 — Quantify consequences**

> Quantify critical transition times, interdependency propagation delays, and the resulting electricity and mobility service consequences.

## Outside active analytical scope

- non-thermal Power–Transportation interdependencies;
- generic repair/logistics dependencies;
- broad Information or Organization layers;
- flooding and other hazards;
- generic sustainability/economic optimization;
- full LCA;
- generic multiobjective transformation;
- non-thermal restoration mechanisms;
- all transportation modes.

These may appear only as context, boundary conditions, limitations, or future work unless explicitly reopened by a new versioned scope decision.

## Open objects

- exact charging context;
- exact thermally active state variables;
- exact thermal thresholds;
- exact electricity and mobility service metrics;
- validation data/case;
- final thermal RQ wording;
- hypotheses;
- optional thermal intervention set;
- final novelty claim.

## Historical scope

Earlier broad seven-stage, P–T–I–O, RQ1–RQ7/H1–H5, broad sustainability, and engineering-decision architectures are retained for provenance and reusable methods. They do not control the active thesis where they conflict with the thermal-only scope.
