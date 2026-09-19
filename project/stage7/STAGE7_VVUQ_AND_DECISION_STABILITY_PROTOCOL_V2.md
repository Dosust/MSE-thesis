# Stage 7 — VVUQ and Decision-Stability Protocol v2

**Status:** CANONICAL STAGE-7 VVUQ PROTOCOL  
**Effective date:** 2026-09-19

## 1. Core distinction

Stage-7 credibility requires more than numerical convergence.

\`\`\`math
\boxed{
\text{algorithm verification}
\neq
\text{input/model validation}
\neq
\text{decision stability}
\neq
\text{normative legitimacy}.
}
\`\`\`

## 2. Verification obligations

Verify:
- feasibility logic;
- objective direction/unit transformations;
- dominance/Pareto calculations;
- normalization;
- set-distance/H5 metric;
- regret;
- robustness/scenario coverage;
- scenario aggregation;
- adaptive triggers/transition logic when active;
- value-model implementation when active.

## 3. Decision-stability object

For decision output \(D\),

\`\`\`math
\boxed{
S_D
=
\mathcal S_D(
D;
\mathbb U_7,
\mathcal M_D,
\mathcal V_7
).
}
\`\`\`

Decision stability assesses whether feasible/nondominated/preferred/H5 conclusions persist under admissible uncertainty and methodological sensitivity.

## 4. Required stability analyses

As applicable:
- Pareto-membership stability;
- admissible-set stability;
- H5 set-distance/regret stability;
- scenario-set sensitivity;
- low-confidence-input removal;
- model-form sensitivity;
- numerical sensitivity;
- requirement-threshold sensitivity;
- normalization sensitivity;
- weight/value sensitivity;
- robustness-definition sensitivity.

## 5. Value sensitivity

If a value model exists, report whether:
- rankings change across plausible weights;
- the preferred alternative changes;
- dominance conclusions remain invariant;
- the unique winner disappears under plausible value uncertainty.

If no valid value model exists, ranking stability is NOT APPLICABLE and the nondominated set remains the appropriate output.

## 6. H5 stability

H5 cannot be adjudicated solely from one fragile specification. Report sensitivity of the primary H5 result to all prespecified non-target uncertainties while preserving the sustainability-information contrast.

Post-result metric switching is prohibited.

## 7. Validation inheritance

Stage 7 inherits upstream validation limitations.

A decision result over synthetic or benchmark inputs remains a synthetic/benchmark decision result.

\`\`\`math
\boxed{
\Lambda_7
\le
\min(\Lambda_3,\Lambda_4,\Lambda_5,\Lambda_6)
}
\`\`\`

for claims depending on those stages.

## 8. Probability semantics

Expected utility, expected regret, VaR/CVaR or probabilistic robustness require justified probabilities.

Without them use scenario/set/robustness language.

## 9. Gate

\`\`\`math
\boxed{
G_{7,VVUQ}
=
G_{\rm algorithm}
\land
G_{\rm input}
\land
G_{\rm uncertainty}
\land
G_{\rm stability}
\land
G_{\rm claim}.
}
\`\`\`

## 10. Claim boundary

Decision stability is always relative to declared alternatives, objectives, uncertainty domain, requirements and value assumptions. It is not universal proof of optimality.
