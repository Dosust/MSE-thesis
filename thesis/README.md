# ASU MSE Thesis Document Architecture — Thermal-Interdependency Direction

**Thesis title:** **Engineering of Power–Electrified Transportation Interdependencies for Resilience**  
**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Current scope:** [`../project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md`](../project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md) + [`../project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md`](../project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md)  
**State-time definitions:** [`../project/CANONICAL_STATE_TIME_DEFINITIONS_V1.md`](../project/CANONICAL_STATE_TIME_DEFINITIONS_V1.md)  
**Objective authority:** [`../project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md`](../project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md)  
**Status date:** 2026-10-08

## Governing distinction

```text
scientific architecture ≠ document architecture
```

The scientific architecture defines what is modeled and tested. The thesis architecture defines where evidence, mathematics, methods, results, and limitations are written.

## Current thesis storyline

```text
Extreme heat
→ thermal physical state
→ thermal capability / constraint
→ qualified thermal P ↔ T_e interdependency
→ state-time evolution
→ transition / propagation timing
→ electricity + mobility service consequence
```

State and time are the primary analytical dimensions.

## Canonical state-time distinction

```text
State = current modeled condition needed to determine subsequent evolution.
Time = independent variable through which states, transitions, propagation,
       service consequences, and—where modeled—recovery/degradation are quantified.

full physical state space ≠ active reduced thesis state vector
SOC = energy state, not thermal state
aging/degradation may be a slow state
state ≠ capability ≠ service
```

## Current chapter architecture

| Chapter | Current intended scientific output |
|---|---|
| 1 — Introduction | thermal context, problem, bounded gap, scope, GO, SO1–SO3, working thermal RQs, validity limits |
| 2 — Literature & Theory | extreme heat, thermal component physics, Power–Electrified Transportation thermal coupling, state-time/service theory, closest comparators |
| 3 — Conceptual & Mathematical Framework | thermal-only conceptual chain, thermally active states, directional coupling object, transition and propagation timing, service mapping |
| 4 — Methodology | mechanism qualification, case/data boundary, minimum-sufficient thermal physics, thresholds, VVUQ, validation |
| 5 — Results | thermal trajectories, critical transitions, propagation timing, electricity/mobility service consequences |
| 6 — Discussion | mechanisms, assumptions, validity, engineering meaning, bounded Sustainable Engineering implications |
| 7 — Conclusions | final thermal RQ closure, supported contributions, limitations, future work |

## Chapter 3 mathematical spine

```math
H(t)
\rightarrow
X(t)
\rightarrow
C(t)
\rightarrow
Z_{PT}^{th}(t)
\rightarrow
X_{receiver}(t)
\rightarrow
\{\tau_i^C,\delta_{ij}^{th},Q_P(t),Q_T(t)\}.
```

## Chapter 4 methodological spine

```text
qualify thermal mechanism
→ define thermally active states + constraints
→ define heat forcing/scenarios
→ implement minimum-sufficient physics
→ compute state-time trajectories
→ extract transition / propagation / service quantities
→ verify
→ validate
→ quantify uncertainty
```

A successful simulation is not validation.

## Current status

The General Objective and SO1–SO3 are **FROZEN — CANONICAL**.

The final thermal RQ wording and hypotheses remain **OPEN** and may not broaden the active thermal/state-time scope.

Earlier seven-stage, broad P–T–I–O, RQ/SO/H, viability, sustainability, and decision architectures are historical/provenance unless explicitly re-admitted through a versioned scope amendment.

## Current scientific entry points

- [Thermal interdependency scope](../project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md)
- [Thermal state-time scope amendment](../project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md)
- [Canonical state-time definitions](../project/CANONICAL_STATE_TIME_DEFINITIONS_V1.md)
- [Thermal objectives](../project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md)
- [Electrified Transportation boundary](../project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md)
- [Thermal/resilience/sustainability conceptual framework](../project/CONCEPTUAL_FRAMEWORK_SPEC_V5_THERMAL_SUSTAINABILITY.md)
- [Thermal/resilience/sustainability mathematical framework](../project/MATHEMATICAL_FRAMEWORK_SPEC_V3_THERMAL_SUSTAINABILITY.md)
- [Current authority index](../project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md)

## Preservation rule

Earlier scientific versions remain in Git history/archive for provenance. They do not regain authority unless explicitly reopened.
