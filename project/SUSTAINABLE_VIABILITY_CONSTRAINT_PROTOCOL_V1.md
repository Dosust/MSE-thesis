# Sustainable Viability Constraint Protocol v1.0

**Date:** 2026-09-16  
**Status:** PREREGISTERED STRUCTURE / THRESHOLDS NOT FROZEN  
**Stage:** 5 — Controlled Sustainable Viability  
**Authority:** subordinate to canonical system/framework files and evidence protocols

## 1. Purpose

Define how service, physical, environmental/sustainability and other admissibility requirements may enter the acceptability set `K_sus` without inventing thresholds or confusing objectives with hard constraints.

## 2. Core definition

Let `R` denote the set of declared constraints. Then

```math
\boxed{
K_{\rm sus}(t;\kappa)
=
\left\{
Y:\ g_r(Y,t;\kappa_r)\le0,\ r\in R
\right\}.
}
```

Each `kappa_r` is a threshold/requirement with explicit provenance.

The controlled viable set is

```math
\boxed{
\mathcal V_{\rm sus}^{u,T}
=
\left\{
Y_0\in K_{\rm sus}(0):
\exists u(\cdot),
\ u(t)\in\mathcal U(Y,z_I,z_O,t),
\ Y^u(t)\in K_{\rm sus}(t)\ \forall t\in[0,T]
\right\}.
}
```

## 3. Constraint registry

Every constraint must have a record containing at least:

```text
constraint ID;
mathematical expression g_r;
physical/service meaning;
variable(s) and units;
threshold kappa_r and units;
source/authority;
time aggregation/window;
spatial aggregation;
hard constraint vs soft objective;
uncertainty representation;
validity domain;
calibration role;
validation role;
status: proposed / evidence-supported / frozen / rejected.
```

No threshold is frozen because it appears convenient for simulation.

## 4. Constraint classes

The registry may contain, when justified, the following classes.

### 4.1 Physical admissibility

Examples:

```text
network operating bounds;
component capacity;
power balance;
queue/flow conservation;
nonnegative storage/queue states;
protection/safety limits.
```

### 4.2 Critical service requirements

Define service maps

```math
Q_P(Y,t),\qquad Q_T(Y,t).
```

A minimum-service constraint may take the form

```math
Q_P(Y,t)\ge \underline Q_P(t),
```

or

```math
Q_T(Y,t)\ge \underline Q_T(t),
```

only when the corresponding thresholds have documented engineering/service provenance.

### 4.3 Sustainability requirements

Potential quantities include emissions, energy intensity, renewable integration or other sustainability burdens, but a sustainability metric enters `K_sus` only if it represents an actual admissibility requirement rather than merely a preference.

For example,

```math
C(Y,t)\le \overline C(t)
```

is admissible only if `C`, its temporal accounting and `overline C` are justified.

### 4.4 Equity/distributional requirements

Equity may enter as a constraint only if the protected population, service measure, aggregation and threshold are operationally defined. Otherwise it belongs in the Stage-7 many-objective vector rather than in `K_sus`.

## 5. Hard constraints vs objectives

The thesis must distinguish

```math
\boxed{
\text{must remain satisfied}
\neq
\text{prefer to improve}.
}
```

Hard requirements belong in `K_sus`. Trade-off objectives belong in an optimization vector such as `J`.

A cost, carbon or equity quantity must not be promoted to a hard viability constraint merely to create a smaller viable set.

## 6. Temporal semantics

A threshold may be:

```text
instantaneous;
rolling-window;
cumulative over horizon;
maximum-duration violation;
recovery-by-deadline;
service-energy/area-under-curve requirement.
```

Its mathematical form must match the actual engineering requirement.

When a cumulative requirement is needed, augment the state instead of applying a non-Markov constraint informally. For example,

```math
\dot c(t)=\ell_C(Y(t),u(t)),
```

with

```math
c(t)\le \overline c.
```

## 7. Uncertainty and robust/stochastic variants

A deterministic `K_sus` is the baseline. If uncertain thresholds or states are used, the uncertainty interpretation must be explicit.

A chance requirement such as

```math
\Pr(g_r(Y,t)\le0)\ge1-\alpha_r
```

is permitted only when a defensible probability model exists.

Under deep uncertainty without justified probabilities, use robust/scenario/satisficing formulations rather than artificial probability distributions.

## 8. Minimum-mathematics rule

The baseline viability calculation should use the simplest defensible geometry and dynamics. Additional Riemannian/learned geometry, stochastic kernels or augmented states are added only when the engineering requirement demands them or they demonstrate decision value relative to the baseline.

## 9. Constraint-selection evidence gate

A candidate constraint enters the confirmatory `K_sus` only after:

1. its engineering meaning is explicit;
2. its units and scale are verified;
3. the threshold source is independently documented;
4. its time/spatial aggregation is specified;
5. its uncertainty is characterized;
6. it is not redundant with another constraint unless redundancy is intentional;
7. sensitivity to plausible threshold variation is assessed;
8. the final value is frozen before confirmatory viability testing.

## 10. Viability horizon

The horizon `T` must be tied to the problem being tested, for example:

```text
cascade-response horizon;
emergency restoration horizon;
daily operational horizon;
longer strategic planning horizon.
```

No single horizon is universal across all hypotheses.

## 11. Stage-4 dependency

Feasible control is inherited from Stage 4:

```math
u(t)\in\mathcal U(Y,z_I,z_O,t).
```

Therefore degradation of information/organization can shrink the viable set even when physical `K_sus` is unchanged.

This mechanism is central to the H2/H3 bridge.

## 12. Verification before viability computation

Before computing `V_sus`:

```text
constituent P/T physics verified;
canonical dependency realizations verified;
controls and bounds verified;
K_sus constraint registry frozen;
initial-condition domain declared;
solver/discretization convergence checked;
uncertainty treatment frozen;
horizon frozen.
```

## 13. Current blocking state

The protocol structure is ready, but actual `K_sus` is **not frozen** because the thesis has not yet qualified all service/sustainability thresholds for the final demonstrator.

```math
\boxed{
\text{STRUCTURE}=\text{PASS},
\qquad
\text{THRESHOLD PROVENANCE}=\text{BLOCKED\_EVIDENCE},
\qquad
\text{VIABILITY COMPUTATION}=\text{DEFERRED}.
}
```
