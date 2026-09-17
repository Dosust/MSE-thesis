# H4 Confirmatory Preregistration v1.0

**Status:** STRUCTURE FROZEN — EXECUTION DEFERRED UNTIL UPSTREAM RESILIENCE/INTERVENTION GATES PASS  
**Date:** 2026-09-18  
**Authority:** `CANONICAL_RQ_SO_HYPOTHESES_V3.md`

## 1. Canonical hypothesis

> **H4:** Across the prespecified intervention and scenario set, engineering interventions that produce meaningful resilience improvement are not equivalent in their sustainability consequence vectors; at least two resilience-effective interventions produce materially different accessibility, energy, carbon, or cost consequences under the declared comparison rule.

H4 maps to RQ6/SO6. It tests **consequence heterogeneity**, not the claim that resilience improvement necessarily damages sustainability.

## 2. Upstream eligibility gate

Only interventions that have already passed an independently frozen resilience-effectiveness rule may enter the confirmatory H4 comparison.

For intervention `a` and matched baseline `0`, define an upstream resilience change

```math
\Delta \mathfrak R(a,\omega)
=\mathfrak R(a,\omega)-\mathfrak R(0,\omega).
```

The exact resilience metric/orientation and meaningful-improvement threshold must be frozen upstream. H4 may not redefine resilience effectiveness after sustainability consequences are observed.

## 3. Sustainability consequence vector

For every eligible intervention use the same declared accounting boundary and horizon:

```math
C_{sus}(a)=
\begin{bmatrix}
A(a)\\
E(a)\\
G(a)\\
C(a)
\end{bmatrix},
```

where the components denote accessibility consequence, energy/resource consequence, greenhouse-gas/carbon consequence, and cost consequence. Each component requires a definition, unit, baseline, boundary, time horizon, data/proxy source, uncertainty model, and sign convention before use.

No component may be invented merely to complete the vector. If a component is not supportable, it remains unavailable and H4 scope must be reduced/versioned before execution.

## 4. Matched intervention rule

Each intervention is evaluated against the same scenario realization, hazard, initial state, demand, physical model, observation/control assumptions, accounting horizon, and uncertainty draw as its baseline wherever scientifically possible.

```math
\Delta C_{sus}(a,\omega)
=C_{sus}(a,\omega)-C_{sus}(0,\omega).
```

Intervention comparisons must not mix different hazard severities or accounting boundaries unless that stratification is prespecified.

## 5. Primary confirmatory statement

H4 requires at least two **resilience-effective** interventions `a_i,a_j` for which the prespecified consequence-distance/comparison rule exceeds an independently justified materiality threshold:

```math
D_{sus}\!\left(C_{sus}(a_i),C_{sus}(a_j)\right)\ge\delta_4.
```

`D_sus`, normalization/units, aggregation, and `delta_4` remain **OPEN** until the consequence metrics and their measurement/accounting uncertainty are qualified. Raw heterogeneous units may not be combined through arbitrary normalization or weights.

## 6. Accounting and uncertainty gates

Every consequence metric must declare:

```text
functional unit;
spatial boundary;
temporal/lifecycle boundary;
baseline/comparator;
direct vs indirect contributions;
data year/vintage;
uncertainty source;
missing-data rule;
scenario dependence.
```

Uncertainty must distinguish at least input/data, scenario, model-form/accounting, and numerical uncertainty where relevant.

## 7. Prohibited shortcuts

- Do not choose interventions because they yield visually different sustainability consequences.
- Do not call cost, energy, carbon or accessibility a trade-off unless the sign/magnitude relative to the matched baseline supports it.
- Do not infer lifecycle carbon from operational energy alone.
- Do not normalize incompatible units using post-result min/max ranges for confirmatory testing.
- Do not use H4 to rank interventions overall; H5 is the joint decision test.
- Do not replace the canonical H4 with interface-ranking superiority.

## 8. Falsification/adjudication

H4 is not supported if fewer than two interventions meet the independently frozen resilience-effectiveness criterion, or if eligible interventions do not differ materially in the preregistered consequence comparison.

Allowed states:

```text
SUPPORTED
PARTIAL
NOT SUPPORTED
INCONCLUSIVE
NOT YET TESTABLE
```

## 9. Current state

```text
intervention set: OPEN
resilience-effectiveness threshold: OPEN
accessibility metric/boundary: OPEN
energy metric/boundary: OPEN
carbon metric/boundary: OPEN
cost metric/boundary: OPEN
D_sus: OPEN
delta_4: OPEN
confirmatory execution: DEFERRED
```
