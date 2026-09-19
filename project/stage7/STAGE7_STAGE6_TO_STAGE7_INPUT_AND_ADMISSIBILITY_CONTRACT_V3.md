# Stage 7 — Stage 6→7 Input and Admissibility Contract v3

**Status:** CANONICAL STAGE-7 INPUT / ADMISSIBILITY CONTRACT — RQ/SO/H v4 ALIGNED  
**Effective date:** 2026-09-20  
**Supersedes:** `STAGE7_STAGE6_TO_STAGE7_INPUT_AND_ADMISSIBILITY_CONTRACT_V2.md`  
**Upstream authority:** `project/stage6/09_handoff/STAGE6_TO_STAGE7_HANDOFF_CONTRACT_V3.md`  
**Controlling authorities:** `project/CANONICAL_RQ_SO_HYPOTHESES_V4.md`; seven-stage framework v2; Stage-6 v3 alignment authorities.  
**Empirical effect:** none.

## 1. Exact upstream input

```math
oxed{
I_{6	o7}^{v3}
=
left(
mathcal A_6^{qual},
Deltamathfrak R,
mathbf r,
mathcal E_{m fx},
mathcal E_{m fy},
Deltamathbf J_{m sus},
mathcal K_6^{qualified},
mathbb U_6,
Lambda_6,
Pi_6
ight).
}
```

No field may be silently dropped, merged, scalarized, or relabeled.

## 2. Candidate decision record

For each (a_k),

```math
oxed{
mathbf Z_7(a_k)
=
(
a_k,
Deltamathfrak R^{a_k},
mathbf r^{a_k},
mathcal E_{m fx}^{a_k},
mathcal E_{m fy}^{a_k},
Deltamathbf J_{m sus}^{a_k},
F^{a_k},
mathbb U^{a_k},
Lambda^{a_k},
Pi^{a_k}
).
}
```

## 3. Feasibility before preference

```math
oxed{
G_{7,F}(a_k)
=
G_{m physical}
land
G_{m technical}
land
G_{m resource}
land
G_{m requirement}
land
G_{m implementation}
land
G_{m validity}.
}
```

Only applicable evidence-supported gates are activated.

```math
oxed{
mathcal A_7^{adm}
=
{a_kinmathcal A_6^{qual}:G_{7,F}(a_k)=PASS}.
}
```

## 4. Permanent distinctions

```math
oxed{
	ext{infeasible}

eq
	ext{dominated}

eq
	ext{unpreferred}.
}
```

and

```math
oxed{
mathbf r

eq
mathcal E_{m fy}

eq
mathbf J_{m sus}.
}
```

## 5. Evidence/claim inheritance

```math
oxed{
Lambda_7(a_k)leLambda_6(a_k)
}
```

for claims depending on Stage-6 quantities. Synthetic, benchmark-only, unresolved, or BLOCKED statuses are inherited.

## 6. H5 matched-decision frame

Both H5 arms use the same candidate universe, qualified feasibility machinery, scenario domain, uncertainty semantics, numerical tolerances, provenance versions, and common resilience representation. The comparator protocol determines which additional decision information is admitted in the joint arm.

## 7. Feasibility uncertainty

Use probabilistic feasibility only where justified. Otherwise use interval/set/scenario/robust semantics. Insufficient evidence remains BLOCKED. Scenario frequency is not probability.

## 8. No pseudo-admission

Missing data cannot be replaced by convenient defaults; preference cannot waive hard physical/authoritative constraints; Pareto dominance cannot excuse infeasibility; and solver feasibility is not real-world feasibility evidence.

## 9. Claim boundary

This contract determines which intervention records may enter Stage-7 decision analysis. It does not select the intervention.
