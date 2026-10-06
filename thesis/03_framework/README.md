# Chapter 3 — Conceptual and Mathematical Framework

**Thesis title:** **Physics-Based Mathematical Engineering of Power–Transportation Interdependencies for Resilience**  
**Current-scope authority:** [`../../project/CANONICAL_EXTREME_HEAT_STATE_TIME_SCOPE_AMENDMENT_V1.md`](../../project/CANONICAL_EXTREME_HEAT_STATE_TIME_SCOPE_AMENDMENT_V1.md)  
**Framework specification:** [`../../project/CONCEPTUAL_FRAMEWORK_SPEC_V2.md`](../../project/CONCEPTUAL_FRAMEWORK_SPEC_V2.md)  
**Status:** CURRENT WORKING FRAMEWORK  
**Date:** 2026-10-06

## Purpose

Derive a mathematically traceable **state-time framework** for how extreme heat changes selected physical states over time, how qualified Power–Transportation interfaces transmit consequences, and how those consequences affect electricity and mobility services and engineering interventions.

The framework is derived from mathematics and mechanism, not from a preselected picture.

---

## System boundary

### External environment

```math
H(x,t)
```

represents extreme-heat forcing.

### System of interest

Selected:

```text
Power P
+
Physical Interfaces I_PT
+
Battery-Electric Road Transportation T
```

Common heat exposure is **not** itself an interdependency.

---

## Structural architecture

```text
P ↔ I_PT ↔ T
```

Every direction must have an independently justified exchanged quantity.

Examples:

```text
P → I_PT      available electrical power / capacity
I_PT → P      charging load / current demand
I_PT → T      delivered charging capability
T → I_PT      vehicle arrival / charging demand
```

---

## State architecture

```math
X(t)=[X_P^\top,Z^\top,X_T^\top]^\top.
```

- `X_P(t)` = selected Power states;
- `Z(t)` = selected interface states;
- `X_T(t)` = selected battery-electric transport states.

`I_PT` (architecture) and `Z(t)` (state) are distinct.

---

## Dynamics

```math
\dot X=F(X,H,u;\theta).
```

Selected components/interfaces retain their own governing physics:

```math
\dot X_i=f_i(X_i,H,L_i,Z_{ji},u_i;\theta_i).
```

Use **minimum sufficient physics**.

---

## Constraints and critical transition

```math
g_i(X_i,t)\le 0.
```

```math
\tau_i^C=\inf\{t:g_i(X_i(t),t)=0\}.
```

Each threshold must have explicit physical/operational meaning and evidence.

---

## Propagation timing

Propagation is not topology alone.

For an admitted event relation:

```math
\delta_{ij}=\tau_j^{response}-\tau_i^{transition}.
```

Before using `δ_ij`, define:
- source event;
- target response;
- interface/mechanism;
- direction;
- timescale;
- service consequence.

---

## Service mapping

```text
physical state
→ functional capability
→ service
```

Current service objects:

```math
Q_P(t),\qquad Q_T(t).
```

Exact service metrics remain **OPEN**.

---

## Parallel derived analyses

Do not impose false serial dependence:

```math
X(t)
\rightarrow
\begin{cases}
\tau_i^C\\
\delta_{ij}\\
Q_P(t),Q_T(t)
\end{cases}
```

---

## Engineering interventions

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
Use observations, validation, intervention outcomes, and recovery evidence to revise future models and design decisions.

---

## Mathematical-visualization rule

Every framework figure must follow:

```text
formal model
→ declared visual encoding
→ deterministic or verified rendering
```

Use:
- `../../.github/skills/engineering-framework-design/SKILL.md`
- `../../.github/skills/scientific-diagram-design/SKILL.md`
- `../../.github/skills/mathematical-visualization-design/SKILL.md`

No arrow, color, icon, shape, geometry, or motion is admitted without a declared scientific purpose.

---

## Exit gate

Chapter 3 is ready only when:

- exact charging context is frozen;
- selected state variables and units are defined;
- directional interface exchanges are qualified;
- governing equations and parameters are evidence-supported;
- thresholds/constraints are defensible;
- service mappings are operationalized;
- intervention targets are explicit;
- assumptions and validity domains are recorded;
- all figures pass semantic, mathematical, and visual QA.
