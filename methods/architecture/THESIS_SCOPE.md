# Architecture-Methods Scope

**Status:** ACTIVE COMPANION / NOT A SECOND SOURCE OF TRUTH  
**Thermal scope:** [`../../project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md`](../../project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md)  
**State-time amendment:** [`../../project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md`](../../project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md)  
**Canonical state-time definitions:** [`../../project/CANONICAL_STATE_TIME_DEFINITIONS_V1.md`](../../project/CANONICAL_STATE_TIME_DEFINITIONS_V1.md)  
**Objective authority:** [`../../project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md`](../../project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md)  
**Conceptual framework:** [`../../project/CONCEPTUAL_FRAMEWORK_SPEC_V5_THERMAL_SUSTAINABILITY.md`](../../project/CONCEPTUAL_FRAMEWORK_SPEC_V5_THERMAL_SUSTAINABILITY.md)  
**Mathematical framework:** [`../../project/MATHEMATICAL_FRAMEWORK_SPEC_V3_THERMAL_SUSTAINABILITY.md`](../../project/MATHEMATICAL_FRAMEWORK_SPEC_V3_THERMAL_SUSTAINABILITY.md)

This directory contains implementation and numerical scaffolds. It does **not** define thesis scope.

## Active scientific model boundary

```text
Power System P
↔
Electrified Transportation System T_e
```

Active scientific focus:

```text
thermal interdependency
+ physical state
+ time
+ electricity/mobility consequence
```

EVSE belongs to `T_e`. Interface/coupling variables do not form a third physical infrastructure system.

## Active mathematical orientation

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

where only dynamically necessary and evidence-supported blocks are activated. `Z_{PT}^{th}` is represented separately as a coupling/exchange object unless independent dynamics require it to be augmented into the state.

State ontology:

```text
SOC is an energy state, not a thermal state
aging/degradation may be a slow state
coupling quantity ≠ state unless independent dynamics require it
```

with primary outputs

```math
\tau_i^C,
\qquad
\delta_{ij}^{th},
\qquad
Q_P(t),
\qquad
Q_T(t).
```

## Legacy scaffold rule

Existing P–T–I–O, viability, seven-stage, sustainability, and decision code in this directory is retained as **software-QA/provenance scaffolding only**.

It may be used to test:
- syntax;
- interfaces;
- numerical utilities;
- reproducibility;
- visualization plumbing.

It does not define:
- active thesis ontology;
- active research questions;
- active hypotheses;
- active thermal state variables;
- final scientific results.

## Admission rule

A computational component becomes part of the active thesis model only after it is explicitly aligned with the thermal-only scope and its equations, parameters, units, thresholds, boundary conditions, verification, validation, uncertainty treatment, and provenance are qualified.

```text
software scaffold ≠ validated scientific model
```
