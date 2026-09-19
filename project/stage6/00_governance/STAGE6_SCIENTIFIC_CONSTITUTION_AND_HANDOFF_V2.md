# Stage 6 Scientific Constitution and Handoff v2

**Status:** CANONICAL STAGE-6 v2 DESIGN AUTHORITY  
**Effective date:** 2026-09-19  
**Controlling amendment:** \`project/CANONICAL_INTERVENTION_PERFORMANCE_AMENDMENT_V2_1.md\`  
**Supersedes for active Stage-6 governance:** \`STAGE6_SCIENTIFIC_CONSTITUTION_AND_HANDOFF_V1.md\`  
**Empirical closure:** NOT IMPLIED.

## 1. RQ6 / SO6 / H4

Stage 6 retains the current RQ6, SO6 and H4 meanings. The v2 constitution operationalizes the intervention-performance distinction required by the v2.1 amendment.

## 2. Scientific purpose

\`\`\`math
\boxed{
\mathfrak R_T
\rightarrow
\mathcal D_R
\rightarrow
a_k
\rightarrow
\mathfrak M^{a_k}
\rightarrow
Y^{a_k}
\rightarrow
\left(
\Delta\mathfrak R^{a_k},
\mathcal E_{\rm fx}^{a_k},
\mathcal E_{\rm fy}^{a_k},
\Delta\mathbf J_{\rm sus}^{a_k}
\right)
\rightarrow
\mathcal K_{\rm sus}^{cand}.
}
\`\`\`

Stage 6 does not select the preferred intervention. Stage 7 performs the final engineering decision.

## 3. Upstream input

\`\`\`math
\boxed{
I_{5\to6}
=
\left(
\mathfrak R_T,
\mathcal D_R,
\Lambda_5,
\mathbb U_5,
\mathcal G,
\mathbb I^{qualified},
F_{\mathcal G}^{m},
\mathcal U_{\rm feas},
K,
G_{\rm rec},
F_{\rm unsafe}
\right).
}
\`\`\`

Unknown upstream empirical values remain OPEN/DEFERRED and may not be invented.

## 4. Canonical Stage-6 constitution

\`\`\`math
\boxed{
\mathcal C_6^{v2}
=
\left(
I_{5\to6},
\mathcal A_6,
a_0,
\Phi_a,
FU_6,
\mathcal B_{LC},
\mathbf T_{\rm fx},
\mathcal E_{\rm fx},
\mathbf C_{\rm res},
\mathcal E_{\rm fy},
\mathbf J_{\rm sus},
\mathcal A_R^{+},
\mathcal A_{\rm fx}^{+},
\mathcal K_{\rm sus}^{cand},
\mathbb U_6,
\mathcal H_4,
I_{6\to7}
\right).
}
\`\`\`

## 5. Intervention object

\`\`\`math
\mathfrak M^{a_k}
=
\Phi_a(\mathfrak M^0,a_k).
\`\`\`

Each intervention records target, mechanism, location, magnitude, timing, service life, resources and implementation constraints.

\`\`\`math
\boxed{u(t)\neq a_k.}
\`\`\`

Operational control remains Stage 4–5; \(a_k\) is a strategic intervention.

## 6. Resilience change

Stage 6 receives and recomputes, under the intervention realization as required,

\`\`\`math
\Delta\mathfrak R^{a_k}.
\`\`\`

Resilience is a system property. It is not identical to intervention effectiveness.

## 7. Effectiveness

\`\`\`math
\boxed{
\mathcal E_{\rm fx}(a_k)
=
\mathcal F_{\rm fx}
(
\text{achieved outcome},
\mathbf T_{\rm fx}^{a_k}
).
}
\`\`\`

The target set is prospectively defined and provenance-tagged.

The effectiveness-qualified set is:

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

This is distinct from:

\`\`\`math
\mathcal A_R^{+}
=
\{
a_k:\Delta\mathcal M_R(a_k)\ge\delta_R
\}.
\`\`\`

## 8. Efficiency

\`\`\`math
\boxed{
\mathcal E_{\rm fy}(a_k)
=
\mathcal F_{\rm fy}
(
\text{achieved outcome},
\mathbf C_{\rm res}^{a_k}
).
}
\`\`\`

Efficiency remains vectorial or ratio/Pareto based unless a scalar aggregation is independently justified.

Existing \(\eta_{R,m}\) diagnostics are retained only where numerically and physically admissible.

## 9. Sustainability consequences

The core vector remains:

\`\`\`math
\boxed{
\mathbf J_{\rm sus}^{a_k}
=
\begin{bmatrix}
J_{\rm access}^{a_k}\\
J_{\rm energy}^{a_k}\\
J_{\rm carbon}^{a_k}\\
J_{\rm cost}^{a_k}
\end{bmatrix}.
}
\`\`\`

Additional outcomes require qualified causal linkage, inventory, units, boundary, uncertainty and validation.

## 10. Permanent scientific distinctions

\`\`\`math
\boxed{
\text{Resilience}
\neq
\text{Effectiveness}
\neq
\text{Efficiency}
\neq
\text{Sustainability}
\neq
\text{Stage-7 preference}.
}
\`\`\`

Also:

\`\`\`math
\Delta\mathfrak R>0
\not\Rightarrow
\mathcal E_{\rm fx}=PASS,
\`\`\`

\`\`\`math
\mathcal E_{\rm fx}=PASS
\not\Rightarrow
\mathcal E_{\rm fy}\text{ favorable},
\`\`\`

\`\`\`math
\mathcal E_{\rm fy}\text{ favorable}
\not\Rightarrow
\Delta\mathbf J_{\rm sus}\text{ favorable}.
\`\`\`

## 11. Accounting boundary firewall

\`\`\`math
\boxed{
T_5\neq H_{LC}.
}
\`\`\`

Disruption/recovery horizon and lifecycle accounting horizon remain separate.

Shared resource/sustainability quantities must declare their separate accounting roles and double-counting control.

## 12. H4 execution sequence

\`\`\`math
\boxed{
\mathcal A_6
\rightarrow
G_{6-PHY}
\rightarrow
\Delta\mathfrak R
\rightarrow
\mathcal E_{\rm fx}
\rightarrow
\mathcal E_{\rm fy}
\rightarrow
\Delta\mathbf J_{\rm sus}
\rightarrow
H4.
}
\`\`\`

H4 remains a consequence-heterogeneity test; it is not rewritten as an efficiency or effectiveness hypothesis.

## 13. Stage-6 gate architecture

\`\`\`math
\boxed{
\begin{aligned}
G_6={}&
G_{6-CON}\land
G_{6-IN}\land
G_{6-SCOPE}\land
G_{6-INT}\land
G_{6-BASE}\land
G_{6-FU}\land
G_{6-PHY}\\
&\land
G_{6-EFX}\land
G_{6-EFY}\land
G_{6-SOC}\land
G_{6-ENV}\land
G_{6-ECO}\land
G_{6-REQ}\land
G_{6-UQ}\\
&\land
G_{6-BENCH}\land
G_{6-H4}\land
G_{6-PROV}\land
G_{6-CLAIM}\land
G_{6-HANDOFF}.
\end{aligned}
}
\`\`\`

Design-level PASS may coexist with empirical execution DEFERRED.

## 14. Stage-6 output

\`\`\`math
\boxed{
O_6=
\left(
\mathcal A_6^{qual},
\Delta\mathfrak R,
\mathcal E_{\rm fx},
\mathcal E_{\rm fy},
\Delta\mathbf J_{\rm sus},
\mathcal K_{\rm sus}^{cand},
\mathbb U_6,
\Lambda_6,
\Pi_6
\right).
}
\`\`\`

## 15. Handoff

\`\`\`math
\boxed{
I_{6\to7}^{v2}
=
O_6.
}
\`\`\`

Stage 7 may use only records whose required validity gates pass.

## 16. Data firewall

\`\`\`math
\boxed{
D_{\rm available}\rightarrow\mathcal R_6^{case},
\qquad
D_{\rm available}\not\rightarrow\mathcal C_6^{v2}.
}
\`\`\`

Actual target values, resource quantities, efficiency results, sustainability results and H4 outcomes remain DEFERRED until qualified execution.

## 17. Claim boundary

The v2 constitution establishes the intervention-performance architecture. It does not establish that any intervention is effective, efficient, sustainable, or preferable.
