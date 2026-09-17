# H5 Confirmatory Preregistration v1.0

**Status:** STRUCTURE FROZEN — EXECUTION DEFERRED UNTIL H4/INTERVENTION EVIDENCE PASSES  
**Date:** 2026-09-18  
**Authority:** `CANONICAL_RQ_SO_HYPOTHESES_V3.md`

## 1. Canonical hypothesis

> **H5:** Under the declared uncertainty domain and intervention set, incorporating sustainability consequences into resilience-based engineering evaluation produces a materially different admissible or nondominated intervention set, or materially changes decision regret, relative to resilience-only evaluation.

H5 maps to RQ7/SO7. It is a **joint engineering-decision** hypothesis, not an interface-ranking or generic adaptive-pathway hypothesis.

## 2. Frozen decision-set comparison

For a prespecified feasible intervention set `A_feas`, define a resilience-only decision representation

```math
\mathcal A_R
=\operatorname{ND}_{R}(\mathcal A_{feas})
```

and a joint resilience–sustainability representation

```math
\mathcal A_{RS}
=\operatorname{ND}_{R,S}(\mathcal A_{feas}),
```

where `ND` denotes the nondominated/admissible operator under explicitly oriented objectives and feasibility constraints.

The intervention universe, feasibility constraints, resilience metric, sustainability consequence metrics, and uncertainty domain must be fixed before the confirmatory set comparison.

## 3. Objective orientation

Every objective must have an explicit physical unit and improvement orientation before Pareto/nondominance operations. A canonical internal sign transformation may be used only after the native metrics are fixed, for example

```math
q(a)=[R(a),A(a),-E(a),-G(a),-C(a)]
```

when higher resilience/accessibility and lower energy/carbon/cost are preferred. This sign convention does not authorize arbitrary normalization or weighting.

## 4. Candidate confirmatory outcomes

At least one of the following branches must be frozen before result inspection.

### Branch A — set change

Measure a preregistered distance/difference between the resilience-only and joint decision sets:

```math
D_{set}(\mathcal A_R,\mathcal A_{RS})\ge\delta_{5,set}.
```

The exact set metric must be meaningful for finite intervention sets and fixed before confirmatory execution.

### Branch B — decision regret

Under a preregistered decision rule and uncertainty distribution/set, compare regret for decisions selected by resilience-only versus joint evaluation:

```math
\Delta Regret
=Regret_R-Regret_{RS}.
```

Orientation and materiality `delta_{5,regret}` must be independently frozen.

H5 does not require both branches unless the final preregistration explicitly declares both confirmatory.

## 5. Feasibility gate

An intervention may enter either decision set only if its engineering feasibility is explicitly defined under relevant authority, resource, cost, timing, physical, information and organizational constraints.

A mathematically nondominated but infeasible intervention must not be presented as a recommended transformation.

## 6. Uncertainty rule

Decision-set and regret calculations must use the same frozen uncertainty domain across the two evaluation approaches. The comparison may not give one method more favorable scenarios, tighter uncertainty bounds, or different intervention availability.

Robust/stochastic semantics, scenario weights/probabilities, ambiguity sets, and correlation assumptions remain **OPEN** until evidence allows them to be frozen. Equal probability may not be assumed solely for convenience.

## 7. Sequential transformation

RQ7 permits intervention sequencing only where data and scope justify it. A multi-stage pathway

```math
Y_{k+1}^{struct}=\Psi_{tr}(Y_k^{struct},a_k)
```

is therefore **optional downstream analysis**, not part of H5 by default. H5 can be tested on a prespecified finite intervention set without inventing a multi-period transition model.

## 8. Prohibited shortcuts

- Do not select the intervention set after observing Pareto outcomes.
- Do not choose objective weights post hoc to force a different decision.
- Do not use post-result min/max normalization as confirmatory evidence.
- Do not claim that joint evaluation is better merely because the nondominated set is larger or smaller.
- Do not replace the canonical H5 with adaptive-pathway superiority unless separately versioned and justified.
- Do not issue an engineering recommendation when feasibility/uncertainty gates remain open.

## 9. Falsification/adjudication

H5 is not supported in the declared domain if the joint evaluation does not produce a material preregistered set/regret change relative to resilience-only evaluation.

Allowed states:

```text
SUPPORTED
PARTIAL
NOT SUPPORTED
INCONCLUSIVE
NOT YET TESTABLE
```

## 10. Current state

```text
feasible intervention set: OPEN
resilience metric: OPEN
H4 sustainability consequence vectors: OPEN
uncertainty domain/probabilities: OPEN
set metric or regret branch: OPEN
materiality threshold: OPEN
confirmatory execution: DEFERRED
```
