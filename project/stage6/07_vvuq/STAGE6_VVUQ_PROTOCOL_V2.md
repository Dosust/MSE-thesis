# Stage 6 VVUQ Protocol v2

**Status:** CANONICAL STAGE-6 VVUQ PROTOCOL — v2.1 ALIGNED  
**Effective date:** 2026-09-19  
**Purpose:** extend v1 VVUQ to first-class effectiveness and efficiency objects while retaining sustainability-accounting controls.

## 1. Core distinction

\`\`\`math
\boxed{
\text{verification}
\neq
\text{validation}
\neq
\text{uncertainty propagation}
\neq
\text{normative weighting}.
}
\`\`\`

## 2. Uncertainty taxonomy

Retain v1:

- aleatory;
- epistemic;
- model-form;
- numerical;
- normative/value.

Add explicit intervention-performance uncertainty records for:

- target/threshold uncertainty;
- effectiveness-QOI uncertainty;
- resource inventory uncertainty;
- ratio denominator uncertainty;
- resource boundary/perspective uncertainty.

## 3. Effectiveness V&V

Required checks:

\`\`\`math
\boxed{
G_{6-EFX}
=
G_{target}
\land
G_{QOI}
\land
G_{unit}
\land
G_{agg}
\land
G_{unc}
\land
G_{valid}
\land
G_{prov}.
}
\`\`\`

Verification includes:

- threshold/operator logic;
- target aggregation;
- target-margin sign;
- PASS/FAIL fixtures;
- hard/soft status handling.

Validation includes, as applicable:

- validity of the underlying resilience/service QOI;
- authoritative/stakeholder provenance for hard targets;
- sensitivity to target uncertainty;
- stability of PASS/FAIL classification.

## 4. Efficiency V&V

\`\`\`math
\boxed{
G_{6-EFY}
=
G_{res}
\land
G_{unit}
\land
G_{boundary}
\land
G_{denom}
\land
G_{unc}
\land
G_{valid}
\land
G_{double}.
}
\`\`\`

Verification includes:

- resource-unit consistency;
- incremental/absolute semantics;
- denominator sign/stability;
- ratio reproduction;
- Pareto/dominance logic;
- double-counting flags.

Validation includes:

- resource quantities against independent estimates/specifications;
- cost/time/crew/material/energy source qualification;
- resource-boundary adequacy;
- sensitivity to uncertain denominators.

## 5. Sustainability VVUQ

Retain v1 requirements for:

- environmental activity/factor checks;
- energy/carbon validation;
- accessibility/social verification and validation;
- lifecycle-cost verification;
- physical intervention V&V;
- sampling convergence;
- sensitivity.

## 6. Double-counting audit

For every quantity appearing in both \(\mathbf C_{\rm res}\) and \(\mathbf J_{\rm sus}\), require a role map:

\`\`\`text
quantity
resource role
sustainability role
perspective
time boundary
functional unit
incremental/absolute
double-counting prevention
\`\`\`

No shared value may be counted twice inside the same decision dimension.

## 7. Sampling convergence

Where ensemble analysis is used, monitor convergence of:

- effectiveness PASS/coverage rates;
- efficiency ratios/vector quantities;
- sustainability consequences;
- requirement classification.

No universal sample count is prescribed.

## 8. Classification stability

For effectiveness/requirements, report whether uncertainty changes classification.

If:

\`\`\`math
P(S_{\rm fx}=PASS)
\`\`\`

has justified probabilistic meaning, report it. Otherwise report scenario/interval classification stability.

## 9. Efficiency ratio stability

Where \(\eta=N/D\), report denominator uncertainty and ratio instability.

If the denominator includes zero or changes sign over the qualified uncertainty set, suppress the ratio and report \((N,D)\).

## 10. Decision-interface stability

Stage 6 does not choose the final intervention, but it must report whether Stage-6 classifications change under plausible uncertainty before handoff to Stage 7.

## 11. Claim rule

Every Stage-6 v2 result retains:

\`\`\`math
\boxed{
\text{estimate/status}
+
\text{uncertainty}
+
\text{boundary}
+
\text{provenance}
+
\text{validation domain}.
}
\`\`\`

Significant digits do not create validity.
