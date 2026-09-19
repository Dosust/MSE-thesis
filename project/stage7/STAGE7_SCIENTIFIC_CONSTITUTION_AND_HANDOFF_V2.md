# Stage 7 Scientific Constitution and Final Decision Handoff v2

**Status:** CANONICAL STAGE-7 DESIGN AUTHORITY — v2.1 aligned  
**Effective date:** 2026-09-19  
**Stage:** 7 — Engineering Decision and Adaptive Transformation  
**RQ/SO/H authority:** \`project/CANONICAL_RQ_SO_HYPOTHESES_V3.md\`  
**Framework authority:** \`project/CANONICAL_7_STAGE_FRAMEWORK_V2.md\`  
**Intervention-performance authority:** \`project/CANONICAL_INTERVENTION_PERFORMANCE_AMENDMENT_V2_1.md\`  
**Upstream handoff:** \`project/stage6/09_handoff/STAGE6_TO_STAGE7_HANDOFF_CONTRACT_V2.md\`  
**Empirical H5 closure:** NOT IMPLIED.

## 1. RQ7 / SO7 / H5

### RQ7

> **What should be changed, where, when and in what sequence to achieve effective, efficient and sustainable infrastructure transformation under feasibility constraints and uncertainty?**

### SO7

> **Evaluate candidate infrastructure transformations and, where justified, intervention sequences using effectiveness, efficiency, sustainability, feasibility and uncertainty to support engineering decisions.**

### H5

> **Under the declared uncertainty domain and intervention set, incorporating sustainability consequences into resilience-based engineering evaluation produces a materially different admissible or nondominated intervention set, or materially changes decision regret, relative to resilience-only evaluation.**

H5 is not assumed true.

## 2. Universal Stage-7 contract

\`\`\`math
\boxed{
\mathfrak S_7
=
(
RQ_7,
SO_7,
H_5,
I_7,
O_7,
\mathcal M_7,
\Theta_7,
G_7,
U_7,
E_7,
\Lambda_7
).
}
\`\`\`

Equivalent decision constitution:

\`\`\`math
\boxed{
\mathcal C_7
=
(
I_{6\to7},
\mathcal A_7^{adm},
\mathbf Z_7,
\mathcal P_7,
D_R,
D_{R,S},
\mathbb U_7,
\mathcal V_7,
\mathcal H_5,
VVUQ_7,
\Lambda_7
).
}
\`\`\`

## 3. Stage-7 input

Stage 7 consumes exactly:

\`\`\`math
\boxed{
I_{6\to7}^{v2}
=
(
\mathcal A_6^{qual},
\Delta\mathfrak R,
\mathcal E_{\rm fx},
\mathcal E_{\rm fy},
\Delta\mathbf J_{\rm sus},
\mathcal K_{\rm sus}^{cand},
\mathbb U_6,
\Lambda_6,
\Pi_6
).
}
\`\`\`

No input dimension is silently collapsed or discarded.

## 4. Candidate record

\`\`\`math
\boxed{
\mathbf Z_7(a_k)
=
(
\Delta\mathfrak R^{a_k},
\mathcal E_{\rm fx}^{a_k},
\mathcal E_{\rm fy}^{a_k},
\Delta\mathbf J_{\rm sus}^{a_k},
F^{a_k},
\mathbb U^{a_k},
\Lambda^{a_k},
\Pi^{a_k}
).
}
\`\`\`

## 5. Feasibility first

\`\`\`math
\boxed{
\mathcal A_7^{adm}
=
\{a_k\in\mathcal A_6^{qual}:G_{7,F}(a_k)=PASS\}.
}
\`\`\`

The permanent distinction is:

\`\`\`math
\boxed{
\text{infeasible}
\neq
\text{dominated}
\neq
\text{unpreferred}.
}
\`\`\`

## 6. Decision sequence

\`\`\`math
\boxed{
\text{feasibility}
\rightarrow
\text{native-unit objectives}
\rightarrow
\text{dominance/Pareto}
\rightarrow
\text{robustness/regret}
\rightarrow
\text{preference model, if justified}.
}
\`\`\`

A value model is not required for design closure.

## 7. Pareto set

For consistently oriented objectives:

\`\`\`math
\boxed{
\mathcal P_7
=
\operatorname{Pareto}(\mathcal A_7^{adm}).
}
\`\`\`

Pareto membership is descriptive under declared dimensions. It does not identify a unique implementation choice.

## 8. Value firewall

\`\`\`math
\boxed{
\text{evidence}
\neq
\text{requirement}
\neq
\text{stakeholder preference}
\neq
\text{weight}.
}
\`\`\`

If no legitimate value model exists:

\`\`\`math
\boxed{
\text{do not invent weights}.
}
\`\`\`

## 9. H5 primary comparator

The primary H5 comparison is:

\`\`\`math
\boxed{
\mathcal A_R^\star
\quad\text{vs}\quad
\mathcal A_{R,S}^\star.
}
\`\`\`

Using the common frame:

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

define

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

Thus sustainability information is the primary changed information block.

## 10. H5 set-change metric

An admissible finite-set metric is

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

The materiality threshold \(\delta_5\) remains DEFERRED until justified and prospectively frozen.

A preregistered regret/dominance-change metric may replace it when scientifically better matched to the decision structure.

## 11. Deep uncertainty

\`\`\`math
\boxed{
\text{risk}
\neq
\text{deep uncertainty}.
}
\`\`\`

The Stage-7 uncertainty object is:

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

Scenario frequency is not probability without a justified probability model.

## 12. Robustness and regret

Robustness must be metric-specific and scenario-domain-specific.

For declared loss:

\`\`\`math
\boxed{
Reg(a,\omega)
=
L(a,\omega)
-
\min_{a'\in\mathcal A_7^{adm}}L(a',\omega).
}
\`\`\`

Scenario discovery may identify:

\`\`\`math
\boxed{
\Omega_{vuln}(a)
=
\{\omega:\text{declared failure for }a\}.
}
\`\`\`

It remains diagnostic, not a probability estimator.

## 13. Adaptive extension

Adaptive pathways are conditional:

\`\`\`math
\boxed{
\text{adaptive pathways}
\neq
\text{mandatory Stage-7 method}.
}
\`\`\`

They may be activated only if \(G_{7,ADAPT}=PASS\).

Otherwise the primary one-stage/static H5 decision analysis remains the Stage-7 obligation.

## 14. Benchmark ladder

\`\`\`math
\boxed{
B_{7,0}
\rightarrow
B_{7,1}
\rightarrow
B_{7,2}
\rightarrow
B_{7,3}.
}
\`\`\`

- \(B_{7,0}\): analytic fixtures;
- \(B_{7,1}\): synthetic intervention table;
- \(B_{7,2}\): complete synthetic Stage6→7 handoff;
- \(B_{7,3}\): qualified thesis case.

Only \(B_{7,3}\), with all preregistration/VVUQ gates closed, may support confirmatory H5.

## 15. Decision stability

Stage-7 VVUQ must assess:

- admissible-set stability;
- Pareto-membership stability;
- H5 set/regret stability;
- model/scenario sensitivity;
- requirement sensitivity;
- normalization sensitivity;
- value sensitivity when applicable;
- low-confidence-input removal.

Correct algorithm implementation is not sufficient for a stable engineering decision.

## 16. Design gates

\`\`\`math
\boxed{
\begin{aligned}
G_{7,DESIGN}={}&
G_{7-CON}
\land G_{7-IN}
\land G_{7-ADM}
\land G_{7-OBJ}
\land G_{7-PARETO}
\land G_{7-VALUE}\\
&\land G_{7-UQ}
\land G_{7-ROB}
\land G_{7-REGRET}
\land G_{7-H5}
\land G_{7-BENCH}
\land G_{7-VVUQ}\\
&\land G_{7-CLAIM}
\land G_{7-PROV}.
\end{aligned}
}
\`\`\`

\(G_{7,ADAPT}\) is separate and conditional.

## 17. Stage-7 output

The rigorous default output is:

\`\`\`math
\boxed{
O_7
=
(
\mathcal A_7^{adm},
\mathcal P_7,
\mathcal A_R^\star,
\mathcal A_{R,S}^\star,
D_{\mathcal A},
Reg,
Rob,
\Omega_{vuln},
S_D,
\Lambda_7
).
}
\`\`\`

Only if a legitimate decision/value rule exists may Stage 7 additionally report:

\`\`\`math
a^\star
\quad\text{or, conditionally,}\quad
(a_1^\star,\ldots,a_n^\star).
\`\`\`

## 18. Claim ladder

### \(\Lambda_{7,0}\) — specification only
Decision architecture frozen; no case execution.

### \(\Lambda_{7,1}\) — algorithm/fixture verification
Pareto, feasibility, H5 metric, regret and robustness fixtures pass.

### \(\Lambda_{7,2}\) — synthetic decision evidence
Full synthetic Stage6→7 decision machinery verified.

### \(\Lambda_{7,3}\) — qualified case decision analysis
Real/qualified case executed with VVUQ but not necessarily confirmatory H5.

### \(\Lambda_{7,4}\) — confirmatory H5 adjudication
Requires preregistered H5 metric/materiality, qualified inputs, matched comparison, and Stage-7 VVUQ.

No claim may exceed inherited upstream claim ceilings.

## 19. Protected DEFERRED fields

This constitution does not freeze:

- preferred intervention;
- stakeholder weights;
- \(\delta_5\);
- final normalization constants;
- unsupported scenario probabilities;
- final robustness threshold;
- final regret threshold;
- adaptive triggers/pathway;
- H5 result.

## 20. Scientific firewall

\`\`\`math
\boxed{
\text{design closure}
\neq
\text{decision execution}
\neq
\text{H5 support}
\neq
\text{normative legitimacy}.
}
\`\`\`
