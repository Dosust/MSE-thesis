# H4--H5 Confirmatory Preregistration v1.0

**Date:** 2026-09-18  
**Authority:** `CANONICAL_RQ_SO_HYPOTHESES_V3.md`  
**Status:** COMPARISON LOGIC FROZEN / NUMERICAL MATERIALITY THRESHOLDS OPEN / EXECUTION DEFERRED

## 1. Purpose

This file replaces any obsolete interpretation of H4 as an interface-ranking hypothesis or H5 as an automatically adaptive pathway hypothesis. Interface criticality remains a supporting Stage-5/6 diagnostic; adaptive sequencing remains optional unless separately preregistered.

The active tests are:

```math
H_4:
a_k\rightarrow(\Delta\mathfrak R^{a_k},\Delta\mathbf J_{sus}^{a_k}),
```

```math
H_5:\mathcal A_R^\star\quad\text{vs}\quad\mathcal A_{R,S}^\star.
```

## 2. Scientific basis

Resilience-enhancing infrastructure actions can differ materially in lifecycle cost, emissions and other sustainability consequences; therefore resilience gain alone is insufficient to identify a sustainable intervention. Peer-reviewed infrastructure studies explicitly evaluate trade-offs among resilience, cost and carbon, including Liu et al. (2024), https://doi.org/10.1016/j.scs.2024.105647; Mitoulis et al. (2023), *Transportation Research Part D*; and Zhu & Zhang (2026), https://doi.org/10.1016/j.ress.2025.111797. Multi-objective decision formulations are consequently appropriate when objectives are kept explicit rather than hidden in an unqualified scalar score.

Power--transportation resilience studies also show that uncertainty and restoration/response decisions can materially change coupled-system outcomes (Li et al., 2025, https://doi.org/10.1109/TSG.2024.3420753).

These sources justify the comparison architecture; they do **not** predetermine that H4 or H5 will be supported.

## 3. Intervention eligibility

Let `a_0` denote the matched no-intervention/baseline strategy and let `A` be the prespecified candidate-intervention set.

For every candidate `a`:

```math
\Delta\mathfrak R(a)=\mathfrak R(a)-\mathfrak R(a_0).
```

An intervention is **resilience-effective** only when it passes all physical/VVUQ gates and satisfies the preregistered resilience materiality rule:

```math
\boxed{a\in\mathcal A_{eff}\iff\Delta\mathfrak R(a)\ge\delta_R.}
```

`delta_R` remains OPEN until it can be set from engineering significance, observation uncertainty and numerical uncertainty without inspecting confirmatory intervention outcomes.

## 4. Sustainability consequence vector

Use explicit objective components rather than an arbitrary weighted index:

```math
\boxed{
\mathbf J_{sus}(a)
=
\begin{bmatrix}
-A(a)\\
E(a)\\
G(a)\\
C(a)
\end{bmatrix}
}
```

where all components are oriented so lower is better:

- `A`: accessibility/service accessibility; stored as `-A` in the minimization vector;
- `E`: declared-boundary energy use;
- `G`: declared-boundary greenhouse-gas emissions in CO2e;
- `C`: declared-boundary cost.

The accounting boundary, functional unit, time horizon and data provenance for each component must be frozen before H4 execution. Operational GHG must not be called lifecycle GHG unless construction/material/end-of-life stages are actually included.

## 5. Matched counterfactual rule

For each scenario `omega` and intervention `a`, compare against `a_0` using identical:

```text
initial state;
hazard realization;
demand realization;
model parameters not caused by the intervention;
observation stream assumptions;
random-number stream / seed where applicable;
solver settings and numerical tolerances.
```

Only the declared intervention changes.

## 6. H4 -- intervention-consequence heterogeneity

Canonical H4:

> Across the prespecified intervention and scenario set, engineering interventions that produce meaningful resilience improvement are not equivalent in their sustainability consequence vectors; at least two resilience-effective interventions produce materially different accessibility, energy, carbon, or cost consequences under the declared comparison rule.

For each sustainability component `k`, define

```math
D_{4,k}(a,b)=J_{sus,k}(a)-J_{sus,k}(b).
```

Before confirmatory execution freeze component-specific materiality thresholds `delta_{4,k}` in native units. H4 is supported in the declared domain only if:

```math
\boxed{
\exists a,b\in\mathcal A_{eff},\;a\neq b,\;\exists k:
\operatorname{CI}_{95\%}(|D_{4,k}(a,b)|)>\delta_{4,k}
}
```

under the preregistered paired uncertainty procedure.

No claim of “trade-off” is made merely because two interventions differ. A resilience--sustainability trade-off requires a resilience improvement together with a deterioration in at least one declared sustainability component relative to the matched baseline. Synergy requires improvement in resilience and in the relevant sustainability component.

### H4 non-support

H4 is not supported if the qualified resilience-effective interventions are indistinguishable within all preregistered sustainability materiality tolerances. If fewer than two interventions satisfy the resilience-effectiveness gate, H4 is `NOT TESTABLE IN THE DECLARED SET`, not automatically unsupported.

## 7. H5 -- joint resilience--sustainability decision

Define the resilience-only nondominated/admissible set:

```math
\mathcal A_R^\star
=ND\{\text{resilience objectives/constraints over }\mathcal A\},
```

and the joint set:

```math
\mathcal A_{R,S}^\star
=ND\{\text{resilience and }\mathbf J_{sus}\text{ over }\mathcal A\}.
```

For a finite intervention set, define a transparent set-change diagnostic:

```math
\boxed{
D_{set}
=1-
\frac{|\mathcal A_R^\star\cap\mathcal A_{R,S}^\star|}
{|\mathcal A_R^\star\cup\mathcal A_{R,S}^\star|}.
}
```

`D_set=0` means identical sets. `delta_5>0` is a preregistered materiality threshold and remains OPEN until the decision use and finite-set resolution are frozen.

Primary H5 criterion:

```math
\boxed{D_{set}\ge\delta_5}
```

with decision regret under declared uncertainty retained as a secondary confirmatory route only if its loss function is frozen before results.

### H5 non-support

H5 is not supported if the joint analysis does not materially change the admissible/nondominated decision set or the separately preregistered regret metric. H5 is `NOT TESTED` if H4 outcomes, accounting boundaries, uncertainty models or intervention set are not yet qualified.

## 8. Uncertainty and statistics

Use paired scenario-level differences. Bootstrap/resample independent scenario/event units rather than correlated time points. Preserve separately:

```text
parameter/process uncertainty;
observation uncertainty;
model-form sensitivity;
finite-sample uncertainty;
numerical error.
```

A p-value alone is not a materiality decision. Effect direction, native units, uncertainty interval and engineering tolerance must all be reported.

## 9. Hard execution gates

H4 requires:

```math
G_{H4}=G_{H1/H2/H3}\land G_A\land G_R\land G_J\land G_{U4}\land G_{\delta4}\land G_{data4}=1.
```

H5 requires:

```math
G_{H5}=G_{H4}\land G_{decision}\land G_{\delta5}\land G_{U5}=1.
```

Current state:

```text
H4 = DEFERRED_UPSTREAM
H5 = DEFERRED_H4

delta_R = OPEN
delta_4,k = OPEN
delta_5 = OPEN
```

No threshold may be chosen from confirmatory H4/H5 outcomes.
