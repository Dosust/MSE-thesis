# Stage 6 Effectiveness Target and Evaluation Protocol v2

**Status:** CANONICAL STAGE-6 EFFECTIVENESS PROTOCOL  
**Effective date:** 2026-09-19  
**Authority:** Canonical Intervention-Performance Amendment v2.1  
**Purpose:** make intervention target attainment explicit and separate it from resilience level or resilience improvement.

## 1. Definition

Effectiveness asks:

> Did intervention \(a_k\) achieve the declared engineering target under the declared scenario/domain?

\`\`\`math
\boxed{
\text{Effectiveness}
=
\text{target attainment}.
}
\`\`\`

It is not resilience itself:

\`\`\`math
\boxed{
\Delta\mathfrak R>0
\not\Rightarrow
\mathcal E_{\rm fx}=PASS.
}
\`\`\`

## 2. Target object

For intervention \(a_k\),

\`\`\`math
\boxed{
\mathbf T_{\rm fx}^{a_k}
=
\{T_{fx,j}^{a_k}\}_{j=1}^{p_k}.
}
\`\`\`

A target record is

\`\`\`math
T_{fx,j}^{a_k}
=
(
q_j,
\circ_j,
\theta_j,
u_j,
A_j,
P_j,
U_j,
V_j
),
\`\`\`

where:

- \(q_j\): Stage-5 resilience/service QOI or declared engineering output;
- \(\circ_j\): comparison operator;
- \(\theta_j\): threshold/target value or target relation;
- \(u_j\): unit;
- \(A_j\): scenario/time/population aggregation rule;
- \(P_j\): provenance/authority;
- \(U_j\): threshold/measurement uncertainty treatment;
- \(V_j\): validation/claim status.

## 3. Target provenance

Each target must be classified as one of:

\`\`\`text
HARD-AUTHORITATIVE
HARD-ADOPTED-STAKEHOLDER
SOFT-TARGET
ENGINEERING-BENCHMARK
RESEARCH-SENSITIVITY
REPORT-ONLY
\`\`\`

A research sensitivity threshold cannot be promoted after seeing results.

## 4. Per-target attainment

For deterministic or threshold-resolved cases:

\`\`\`math
Z_{fx,j}(a_k,\omega)
=
\mathbf 1[
q_j(a_k,\omega)\ \circ_j\ \theta_j
].
\`\`\`

Under probabilistic uncertainty, if probability semantics are justified:

\`\`\`math
P_{fx,j}(a_k)
=
\Pr[
q_j(a_k,\xi)\ \circ_j\ \theta_j
].
\`\`\`

Under deep uncertainty without justified probabilities, report scenario/interval coverage rather than probability.

## 5. Intervention-level effectiveness object

Default representation:

\`\`\`math
\boxed{
\mathcal E_{\rm fx}(a_k)
=
(
\mathbf Z_{\rm fx},
\mathbf P_{\rm fx},
\mathbf C_{\rm fx},
S_{\rm fx}
).
}
\`\`\`

where:

- \(\mathbf Z_{\rm fx}\): target-level pass/fail where applicable;
- \(\mathbf P_{\rm fx}\): justified probability/coverage descriptors;
- \(\mathbf C_{\rm fx}\): continuous target margins in native units;
- \(S_{\rm fx}\): overall intervention effectiveness status under the frozen aggregation rule.

No scalar score is required.

## 6. Overall effectiveness status

The case protocol must freeze one rule before confirmatory results.

Examples:

### All-hard-target rule

\`\`\`math
S_{\rm fx}(a_k)=PASS
\iff
Z_{fx,j}=1
\quad
\forall j\in\mathcal H_k
\`\`\`

for hard requirements \(\mathcal H_k\).

### Mixed hard/soft rule

Hard requirements determine admissibility; soft targets are reported separately.

No compensatory weighting across hard and soft targets is allowed unless separately authorized.

## 7. Effectiveness-qualified set

\`\`\`math
\boxed{
\mathcal A_{\rm fx}^{+}
=
\{
a_k\in\mathcal A_6^{qual}
:
S_{\rm fx}(a_k)=PASS
\}.
}
\`\`\`

This is distinct from the resilience-improving set

\`\`\`math
\mathcal A_R^+
=
\{
a_k:\Delta\mathcal M_R(a_k)\ge\delta_R
\}.
\`\`\`

## 8. Target margin

For target \(q_j\ge\theta_j\), define:

\`\`\`math
m_{fx,j}=q_j-\theta_j.
\`\`\`

For target \(q_j\le\theta_j\),

\`\`\`math
m_{fx,j}=\theta_j-q_j.
\`\`\`

Positive margin means target satisfied under the declared sign convention.

Margin uncertainty must be reported where material.

## 9. Matched conditions

Effectiveness comparisons must retain the Stage-6 matched scenario/baseline conditions. A target cannot be evaluated under a different hazard or service definition merely to improve pass status.

## 10. Effectiveness V&V gate

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

PASS requires:

- target provenance declared;
- QOI validated at required level;
- unit/direction explicit;
- aggregation rule frozen;
- uncertainty rule defined;
- validity domain respected;
- provenance complete.

## 11. Deferred values

Before case execution, remain DEFERRED:

- target numerical values;
- target-specific uncertainty tolerances;
- target aggregation constants;
- final PASS/FAIL status;
- effectiveness-qualified intervention set.

## 12. Claim boundary

A PASS effectiveness result means the declared target was met under the declared conditions. It does not mean the intervention is efficient, sustainable, optimal, or preferred.
