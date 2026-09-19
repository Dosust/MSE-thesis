# Stage 7 — H5 Preregistration and Comparator Protocol v2

**Status:** CANONICAL H5 OPERATIONAL PROTOCOL  
**Effective date:** 2026-09-19  
**Hypothesis authority:** \`project/CANONICAL_RQ_SO_HYPOTHESES_V3.md\`

## 1. Canonical H5 — unchanged

> **H5:** Under the declared uncertainty domain and intervention set, incorporating sustainability consequences into resilience-based engineering evaluation produces a materially different admissible or nondominated intervention set, or materially changes decision regret, relative to resilience-only evaluation.

This protocol operationalizes H5; it does not rewrite it.

## 2. Primary comparison

\`\`\`math
\boxed{
\mathcal A_R^\star
\quad\text{vs}\quad
\mathcal A_{R,S}^\star.
}
\`\`\`

Both arms use the same admissible candidate set and common decision machinery.

## 3. H5 causal-contrast firewall

Define the common frame

\`\`\`math
\mathcal X_{common}
=
(
\mathcal A_7^{adm},
F,
\mathcal E_{\rm fx},
\mathcal E_{\rm fy},
\mathbb U,
\Omega,
\Lambda,
\Pi,
\mathcal M_D
),
\`\`\`

where \(\mathcal M_D\) contains all decision procedures common to both arms.

Then

\`\`\`math
\boxed{
\mathcal X_R
=
\mathcal X_{common}
+
\mathfrak R
}
\`\`\`

and

\`\`\`math
\boxed{
\mathcal X_{R,S}
=
\mathcal X_{common}
+
\mathfrak R
+
\mathbf J_{\rm sus}.
}
\`\`\`

Thus the primary H5 contrast changes only the availability/use of sustainability consequences.

Effectiveness and efficiency may constrain, qualify, stratify, or be reported in both arms, but cannot appear in only one arm and then be attributed to sustainability.

## 4. Decision-set construction

The exact construction must be frozen before confirmatory results. Admissible choices include:

- constrained feasible set;
- Pareto/nondominated set;
- satisficing set;
- robust nondominated set;
- regret-based set.

Method selection must follow the decision question and uncertainty semantics, not mathematical convenience or favorable results.

## 5. Candidate set-change metric

For finite decision sets:

\`\`\`math
\boxed{
D_{\mathcal A}
=
1-
\frac{
|\mathcal A_R^\star\cap\mathcal A_{R,S}^\star|
}{
|\mathcal A_R^\star\cup\mathcal A_{R,S}^\star|
}.
}
\`\`\`

The materiality threshold \(\delta_5\) remains DEFERRED until its engineering/statistical basis is justified.

## 6. Alternative primary metric

A regret-change or dominance-change metric may replace \(D_{\mathcal A}\) only if selected and frozen prospectively.

The primary metric cannot be changed after confirmatory target results are inspected.

## 7. Matched conditions

Hold constant across H5 arms:

- intervention universe;
- feasibility/admissibility rules;
- scenario set;
- uncertainty representation;
- common performance qualification;
- common numerical tolerances;
- common normalization for shared variables;
- evidence versions;
- value model, if used identically.

## 8. H5 outcomes

### SUPPORTED
A valid preregistered comparison executes and the primary material-change criterion is satisfied.

### NOT SUPPORTED
The valid comparison executes and the material-change criterion is not satisfied.

### NOT TESTED
A prerequisite fails, including insufficient admissible alternatives, unresolved decision-set construction, unsupported uncertainty semantics, failed VVUQ, or missing primary metric/materiality rule.

\`\`\`math
\boxed{
\text{prerequisite failure}
\not\Rightarrow
\text{H5 falsification}.
}
\`\`\`

## 9. Falsification

H5 is not supported if sustainability information does not materially change the preregistered decision set/regret/dominance outcome within the tested uncertainty domain.

Null/negative results are retained.

## 10. Adaptive pathway firewall

Adaptive/sequential transformation is not part of the primary H5 contrast unless separately preregistered after the primary decision question is closed.

## 11. Protected DEFERRED fields

Remain DEFERRED:
- \(\delta_5\);
- exact primary set/regret/dominance metric if not already justified;
- final H5 decision-set construction;
- final case scenario set;
- H5 result.

## 12. Claim boundary

This protocol isolates the information added by sustainability. It does not predict that sustainability will change the decision.
