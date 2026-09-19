# Stage 7 — Robustness, Regret and Scenario Discovery Protocol v2

**Status:** CANONICAL STAGE-7 DEEP-UNCERTAINTY PROTOCOL  
**Effective date:** 2026-09-19

## 1. Risk versus deep uncertainty

\`\`\`math
\boxed{
\text{risk}
\neq
\text{deep uncertainty}.
}
\`\`\`

Probabilities may be used only when the probability model is scientifically defensible.

Otherwise:

\`\`\`math
\boxed{
\text{scenario frequency}
\neq
\text{probability}.
}
\`\`\`

## 2. Stage-7 uncertainty object

\`\`\`math
\boxed{
\mathbb U_7
=
(
U_{\rm aleatory},
U_{\rm epistemic},
U_{\rm model},
U_{\rm numerical},
U_{\rm requirement},
U_{\rm performance},
U_{\rm value}
).
}
\`\`\`

The Stage-6 uncertainty record is inherited and extended with Stage-7 decision/value uncertainty.

## 3. Robustness semantics

Robustness must be defined prospectively. One nonprobabilistic satisficing coverage measure is

\`\`\`math
R_b(a)
=
\frac{
|\{\omega\in\Omega:a\text{ satisfies the declared requirements in }\omega\}|
}{
|\Omega|
}.
\`\`\`

This is **scenario coverage**, not probability, unless \(\Omega\) is generated from a justified probability measure.

Other robustness metrics are admissible only with explicit meaning, direction and aggregation.

## 4. Regret

For a declared loss \(L(a,\omega)\),

\`\`\`math
\boxed{
Reg(a,\omega)
=
L(a,\omega)
-
\min_{a'\in\mathcal A_7^{adm}}L(a',\omega).
}
\`\`\`

Possible summaries include:
- maximum regret;
- mean/expected regret only when probabilities justify it;
- percentile regret only with probabilistic semantics;
- scenario-wise regret profile;
- satisficing regret threshold, if justified.

The chosen rule must be frozen before H5 target-result inspection.

## 5. Scenario discovery

For intervention \(a_k\), define a vulnerability domain

\`\`\`math
\boxed{
\Omega_{vuln}(a_k)
=
\{\omega:\text{declared decision/requirement failure for }a_k\}.
}
\`\`\`

Scenario discovery may identify combinations of uncertain factors associated with vulnerability.

It is diagnostic and does not transform empirical frequency into probability.

## 6. Scenario construction

Every Stage-7 scenario retains:
- Stage-3 physical scenario identity where applicable;
- Stage-4 information/organization assumptions;
- Stage-5 uncertainty/viability context;
- Stage-6 intervention-performance record;
- Stage-7 value/decision assumptions.

Scenario IDs remain traceable across stages.

## 7. Robustness/regret comparability

Across alternatives, use:
- same scenario ensemble;
- same loss definition;
- same requirement thresholds;
- same missing-data rules;
- same uncertainty semantics.

Changing the scenario set for one intervention requires explicit justification.

## 8. Decision under mixed uncertainty

Where some quantities have defensible probabilities and others do not, use a declared hybrid representation rather than treating all uncertainty as probabilistic.

## 9. Robustness claim firewall

Allowed:
- robust relative to specified metric, scenario set and threshold.

Not allowed:
- robust in general;
- high scenario coverage interpreted as high probability without probability semantics;
- low regret interpreted as sustainability.

## 10. Protected DEFERRED fields

Remain DEFERRED:
- exact robustness threshold;
- final loss function;
- final regret threshold;
- final scenario probabilities;
- final vulnerability classifier;
- Stage-7 preferred intervention.
