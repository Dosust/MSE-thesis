# Conceptual Framework Specification V2

**Status:** CURRENT WORKING-FROZEN SCIENTIFIC/VISUAL SPECIFICATION  
**Date:** 2026-10-06  
**Supersedes for active work:** `CONCEPTUAL_FRAMEWORK_SPEC_V1.md`  
**Scope authority:** `CANONICAL_EXTREME_HEAT_STATE_TIME_SCOPE_AMENDMENT_V1.md`

## Purpose

Represent how extreme heat changes selected physical states over time, how qualified Power–Transportation interfaces transmit consequences, how electricity and mobility services respond, and where Improve, Adapt, Restore, and Learn act.

This is a conceptual/mathematical framework, not the research-method flowchart.

## Core chain

```text
Extreme Heat
→ Physical System + Interfaces
→ Coupled State-Time Dynamics
→ Transition / Propagation / Service Analysis
→ Engineering Intervention
→ Resilience Outcomes
→ Learning
```

## System boundary

### External
Extreme heat forcing:

```math
H(x,t).
```

### Inside
Selected:

```text
Power P
+
Physical Interfaces I_PT
+
Battery-Electric Road Transportation T
```

Common heat exposure must be shown separately from P–T interdependency.

## Structural architecture

```text
P ↔ I_PT ↔ T
```

Each direction requires an explicit exchange.

Examples:

```text
P → I_PT      available electrical power / capacity
I_PT → P      charging load / current demand
I_PT → T      delivered charging capability
T → I_PT      vehicle arrival / charging demand
```

## State architecture

```math
X(t)=[X_P^\top,Z^\top,X_T^\top]^\top.
```

`I_PT` = interface architecture.  
`Z(t)` = interface state.  
They are not interchangeable.

## Dynamics

```math
\dot X=F(X,H,u;\theta).
```

Component/interface physics remain heterogeneous:

```math
\dot X_i=f_i(X_i,H,L_i,Z_{ji},u_i;\theta_i).
```

Use minimum-sufficient physics.

## Constraints and time

```math
g_i(X_i,t)\le 0.
```

```math
\tau_i^C=\inf\{t:g_i(X_i(t),t)=0\}.
```

Propagation delay, when physically admitted:

```math
\delta_{ij}=\tau_j^{response}-\tau_i^{transition}.
```

## Service

```text
physical state
→ functional capability
→ service
```

Current service objects:

```math
Q_P(t),\qquad Q_T(t).
```

Exact metrics remain OPEN.

## Parallel derived analyses

Do not force false serial dependence.

```math
X(t)
\rightarrow
\begin{cases}
\tau_i^C\\
\delta_{ij}\\
Q_P(t),Q_T(t)
\end{cases}
```

## Engineering controls

### Improve
```math
\theta\rightarrow\theta'.
```

### Adapt
```math
u_A(t).
```

### Restore
```math
u_R(t).
```

### Learn
Observation, validation, and intervention outcomes update future assumptions, parameters, models, and design choices.

## Visual semantics

Default semantic palette:

| Role | Hex |
|---|---|
| external hazard | `#D55E00` |
| physical/empirical system | `#009E73` |
| mathematical dynamics/analysis | `#0072B2` |
| engineering decision/intervention | `#B86E00` |
| neutral information | `#000000` |
| all backgrounds/interiors | `#FFFFFF` |

Color is secondary to labels, arrows, and geometry.

## Mathematical visualization rule

```text
formal model
→ visual encoding
→ renderer
→ verification
```

No icon, arrow, color, motion, or shape is admitted without a declared scientific purpose.

## Open items

- public DC fast charging vs fleet/depot charging;
- exact Power state;
- exact EVSE/interface thermal state;
- exact transport state;
- exact service metrics;
- exact intervention set;
- final narrowed RQ/SO/H.

## Exit gate

The framework can be promoted from working-frozen only after the open model/service objects are frozen and the final figure passes semantic, mathematical, and visual QA.
