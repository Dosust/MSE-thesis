# Stage 6 H4 Experiment Protocol v2

> **SUPERSEDED — PROVENANCE ONLY (2026-09-20)**
> Active v4-aligned replacement is specified by the Stage-6 v3 authorities referenced in `project/stage6/README.md`. Do not use this file as the current H4/requirements/handoff/freeze authority.

**Status:** CANONICAL STAGE-6 H4 PROTOCOL — v2.1 ALIGNED  
**Effective date:** 2026-09-19  
**Hypothesis:** canonical H4 unchanged.

## 1. H4

H4 remains a test of material sustainability-consequence heterogeneity among interventions that produce meaningful resilience improvement.

The v2.1 amendment adds explicit effectiveness and efficiency reporting; it does **not** redefine the canonical H4 eligibility condition.

## 2. Experimental unit

\`\`\`math
e=
(
a_k,
\omega_s,
Y_0,
\mathfrak M^0,
u/\pi,
FU_6,
\mathcal B_{LC},
H_{LC}
).
\`\`\`

Only \(a_k\) changes across intervention arms unless another factor is explicitly declared.

## 3. Matched conditions

Freeze/share across arms:

\`\`\`math
\mathcal G,\;
\mathbb I^{qualified},\;
F_{\mathcal G}^{m},\;
Y_0,\;
\eta,\;
\mathcal U_{\rm feas},\;
K,\;
G_{\rm rec},\;
F_{\rm unsafe},\;
FU_6,\;
\mathcal B_{LC},\;
H_{LC},\;
\Omega_6,\;
\text{data/factor versions}.
\`\`\`

Use common random numbers where justified.

## 4. Physical qualification

\`\`\`math
a_k\in\mathcal A_6^{qual}
\iff
G_{6-PHY}(a_k)=PASS
\`\`\`

plus all required upstream mechanism/implementation gates.

## 5. Primary H4 eligibility — canonical preservation

The primary H4 set remains:

\`\`\`math
\boxed{
\mathcal A_{H4}
=
\mathcal A_R^+
=
\{
a_k:
\Delta\mathcal M_R(a_k)\ge\delta_R
\}.
}
\`\`\`

This exactly preserves the canonical hypothesis meaning: the H4 test is conditional on **meaningful resilience improvement**.

\(\delta_R\) remains prospectively frozen from Stage-5 engineering/numerical significance and cannot be selected after viewing H4 results.

## 6. Effectiveness — mandatory first-class performance result

For every \(a_k\in\mathcal A_{H4}\), compute:

\`\`\`math
\mathcal E_{\rm fx}(a_k)
\`\`\`

under the frozen effectiveness-target protocol.

Also define:

\`\`\`math
\mathcal A_{\rm fx}^{+}
=
\{
a_k\in\mathcal A_6^{qual}:
S_{\rm fx}(a_k)=PASS
\}.
\`\`\`

Effectiveness status does not replace the primary H4 eligibility set.

A preregistered secondary stratification may evaluate:

\`\`\`math
\boxed{
\mathcal A_R^+
\cap
\mathcal A_{\rm fx}^{+}
}
\`\`\`

when at least two interventions remain. This secondary analysis cannot be substituted for the primary H4 test after inspecting results.

## 7. Efficiency — mandatory first-class performance result

For every H4-eligible intervention, compute:

\`\`\`math
\mathcal E_{\rm fy}(a_k)
\`\`\`

using only qualified resource dimensions.

Efficiency is reported alongside H4 but is not the primary H4 consequence-heterogeneity endpoint.

## 8. Sustainability outcomes

\`\`\`math
\mathbf J_{\rm sus}^{core}
=
[
J_{\rm access},
J_{\rm energy},
J_{\rm carbon},
J_{\rm cost}
]^\top.
\`\`\`

Each component requires direction, unit, boundary and materiality threshold.

## 9. Material heterogeneity without arbitrary weights

For \(q\in\mathcal Q_6\), let \(\delta_{J,q}>0\) be the prospectively frozen material difference in native units.

\`\`\`math
\boxed{
D_J(a_i,a_j)
=
\max_{q\in\mathcal Q_6}
\frac{
|\Delta J_q(a_i)-\Delta J_q(a_j)|
}{
\delta_{J,q}
}.
}
\`\`\`

This is a material-difference detector, not a sustainability utility score.

Primary H4 condition:

\`\`\`math
\boxed{
\exists a_i,a_j\in\mathcal A_R^+,
\quad
D_J(a_i,a_j)\ge1.
}
\`\`\`

No cross-dimension weights are required.

## 10. Matched-effectiveness analysis

Where a sufficient intervention set exists, compare alternatives within a similar resilience-improvement band:

\`\`\`math
|
\Delta\mathcal M_R(a_i)
-
\Delta\mathcal M_R(a_j)
|
\le
\epsilon_R.
\`\`\`

A secondary target-margin match may also be used if preregistered.

These analyses reduce confounding between sustainability consequence differences and simply different intervention strength.

## 11. Efficiency-matched sensitivity

A diagnostic may compare interventions within similar resource budgets to determine whether consequence heterogeneity is primarily a scale effect.

This remains secondary unless separately preregistered.

## 12. Distributional reporting

Accessibility/social outcomes retain group/area vectors where supported. Favorable aggregate means cannot hide materially adverse declared group effects.

## 13. Uncertainty

Report uncertainty for:

\`\`\`math
\Delta\mathfrak R,\;
\mathcal E_{\rm fx},\;
\mathcal E_{\rm fy},\;
\Delta J_q.
\`\`\`

Probability is used only where probability semantics are justified.

## 14. H4 adjudication

### SUPPORTED

At least two qualified resilience-effective alternatives exist and the preregistered consequence-heterogeneity criterion is met with required uncertainty/VVUQ support.

### NOT SUPPORTED

At least two qualified resilience-effective alternatives exist, the test is valid/executable, and the material-difference criterion is not met.

### NOT TESTED

Any prerequisite gate for the primary H4 test fails, including insufficient resilience-effective alternatives, invalid boundary comparability, failed physical admissibility, missing core consequence data, or failed VVUQ.

Missing effectiveness/efficiency data additionally block the corresponding v2.1 intervention-performance claims and complete Stage6→7 handoff, but do not silently redefine the canonical H4 eligibility condition.

## 15. No Stage-7 decision

Stage 6 reports intervention performance and consequence structure. It does not declare the preferred intervention.
