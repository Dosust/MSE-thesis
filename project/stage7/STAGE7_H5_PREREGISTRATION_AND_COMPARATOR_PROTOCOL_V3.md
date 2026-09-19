# Stage 7 — H5 Preregistration and Comparator Protocol v3

**Status:** CANONICAL H5 OPERATIONAL PROTOCOL — RQ/SO/H v4 ALIGNED  
**Effective date:** 2026-09-20  
**Supersedes:** `STAGE7_H5_PREREGISTRATION_AND_COMPARATOR_PROTOCOL_V2.md`  
**Hypothesis authority:** `project/CANONICAL_RQ_SO_HYPOTHESES_V4.md`  
**Empirical status:** H5 NOT TESTED.

## 1. Official H5

> **H5:** Under the declared uncertainty domain, incorporating resource efficiency and admitted sustainability consequences together with feasibility and uncertainty materially changes the admissible or nondominated engineering decision set, dominance relations, or decision regret relative to resilience-only evaluation.

This protocol tests a **joint engineering-decision formulation**. It does not isolate sustainability as the only changed information block.

## 2. Decision records

For each candidate (a_k), define the resilience-only decision record

```math
mathcal X_R(a_k)=
left(
Deltamathfrak R^{a_k},
F^{a_k},
mathbb U^{a_k},
Lambda^{a_k}
ight),
```

and the joint decision record

```math
oxed{
mathcal X_{m joint}(a_k)=
left(
Deltamathfrak R^{a_k},
mathbf r^{a_k},
mathcal E_{m fy}^{a_k},
Deltamathbf J_{m sus}^{a_k},
F^{a_k},
mathbb U^{a_k},
Lambda^{a_k}
ight).
}
```

Effectiveness (mathcal E_{m fx}) may be an admissibility/interpretation field in both arms; it is not silently conflated with efficiency.

## 3. Comparator

```math
oxed{
mathcal A_R^star
quad	ext{vs}quad
mathcal A_{m joint}^star.
}
```

The exact construction—feasible set, Pareto/nondominated set, satisficing set, robust set, or regret-based set—must be prospectively frozen.

Feasibility and uncertainty are governing conditions in both arms so the experiment does not attribute changes caused by inconsistent domains to resource/sustainability information. The substantive added decision dimensions in the joint arm are qualified resource-efficiency and admitted sustainability consequence information.

## 4. No arbitrary scalarization

Native-unit feasibility screening and Pareto/dominance analysis precede any weighting. A weighted utility is permitted only when its authority, preference elicitation, and sensitivity analysis are independently justified.

## 5. Primary change metrics

For finite sets, an admissible set-change metric is

```math
D_{mathcal A}
=
1-
rac{
|mathcal A_R^starcapmathcal A_{m joint}^star|
}{
|mathcal A_R^starcupmathcal A_{m joint}^star|
}.
```

Dominance-relation change or regret change may be primary if preregistered before target results are inspected.

The materiality threshold (delta_5) or equivalent engineering criterion remains DEFERRED until justified.

## 6. Matched conditions

Hold constant across arms: intervention universe; physical/service evidence; feasibility rule; scenario set; uncertainty representation; resilience model; numerical tolerances; provenance versions; and common normalization rules.

## 7. Deep uncertainty

If probabilities are not scientifically defensible, scenario frequencies are not probabilities. Use robustness, satisficing, regret, or scenario-coverage measures as appropriate.

## 8. Adjudication

**SUPPORTED:** a valid preregistered comparison executes and the declared material-change criterion is satisfied.

**NOT SUPPORTED:** the comparison executes validly and the material-change criterion is not satisfied.

**NOT TESTED:** any prerequisite blocks valid execution, including an inadequate intervention set, unresolved comparator construction, unsupported uncertainty semantics, missing resource/sustainability information required by the joint arm, failed VVUQ, or an unfrozen materiality rule.

## 9. Falsification

H5 is not supported if the joint decision formulation does not materially change the declared decision set, dominance relations, or regret relative to resilience-only evaluation within the tested uncertainty domain.

## 10. Adaptive pathway firewall

Adaptive/sequential transformation remains a conditional Stage-7 extension. It is not primary H5 and may be activated only if the temporal decision structure, data, and validation justify a sequential problem.

## 11. Claim boundary

This protocol tests whether the added joint engineering information changes the decision. It does not predetermine a unique preferred intervention.
