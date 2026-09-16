# Thesis Extension — Resilience-to-Sustainability Causal Translation

**Version:** v1.0  
**Date:** 2026-09-16  
**Status:** SPECIFICATION ONLY — no empirical gate upgraded  
**Authority:** subordinate to `project/CANONICAL_7_STAGE_FRAMEWORK.md`, `project/CANONICAL_DEPENDENCY_CONTRACT_V1.md`, and the existing evidence-first review rules in this folder.

## 1. Purpose

This extension adapts the existing engineering–sustainability integration review architecture to the thesis-specific causal chain

```math
\boxed{
\mathfrak d_e
\rightarrow
F_{\mathcal G}^{m}
\rightarrow
Y_{0:T_R}
\rightarrow
\mathbf R
\rightarrow
\mathbf J_{\rm sus}
\rightarrow
\mathbf a
}
```

without changing the frozen seven-stage framework.

The governing question is

```math
\boxed{
\text{What do evidence-qualified interdependencies teach us about resilience, and how can those findings constrain or motivate defensible sustainability transformations?}
}
```

The extension reuses the existing evidence-first rule

```math
\text{Keyword}\rightarrow\text{Candidate Passage}\rightarrow\text{Author Action}\rightarrow\text{Equation/Procedure}\rightarrow\text{Evidence Code}\rightarrow\text{Interpretation}\rightarrow\text{Score},
```

and the existing integration logic

```math
P_{\rm engineering}\rightarrow F_{\rm integration}\rightarrow S_{\rm sustainability}\rightarrow D_{\rm decision}.
```

## 2. Critical scientific distinction

Resilience and sustainability remain separate objects.

Let

```math
\mathbf R=\mathcal R(Y_{0:T_R})
```

be a vector of resilience diagnostics such as service loss, cascade timing, recovery time, viability margin, time-to-boundary or posterior viable mass.

Let sustainability outcomes be trajectory-dependent functionals

```math
\boxed{
J_j
=
\int_0^{T_L}
\ell_j\!\left(Y(t),u(t),\mathbf a,\omega,t\right)dt
+
\phi_j\!\left(Y(T_L),\mathbf a,\omega\right)
}
```

with declared units, sign convention, system boundary and time horizon.

Therefore

```math
\boxed{\mathbf J_{\rm sus}\neq f(\mathbf R)\quad\text{in general}.}
```

Two alternatives may have similar recovery metrics while producing different carbon, cost, accessibility or resource consequences. A direct mapping `R -> J_sus` is admissible only when the physical/analytical transformation is independently supported.

## 3. Stage-6 role

The canonical Stage-6 operator remains

```math
\Phi_{\rm ST}:(\mathcal R_5,\Lambda_{\rm LT},\mathbf d_6)
\mapsto(c_6,\mathcal D_6,\boldsymbol\zeta_T).
```

This extension does not replace that signature. Instead, quantified sustainability consequence functionals become an auditable component of `\Lambda_{LT}` and of the evidence supporting `\mathbf d_6`.

Define the thesis translation evidence bundle

```math
\boxed{
\mathcal T_{RS}
=
\{\tau_{eij}\}
}
```

where one candidate path is

```math
\tau_{eij}
=
(\mathfrak d_e,M_e,\theta_e,Y_{0:T_R},R_i,J_j,\mathbf a_k,D,U,V,\sigma).
```

Here:
- `d_e` = canonical dependency object;
- `M_e` = physical/functional mechanism;
- `theta_e` = declared mechanism parameter/perturbation;
- `R_i` = resilience diagnostic associated with the trajectory;
- `J_j` = sustainability consequence functional;
- `a_k` = candidate structural transformation, when applicable;
- `D` = evidence/data provenance;
- `U` = uncertainty representation;
- `V` = validation status;
- `sigma` = evidence state.

## 4. Outcome admissibility gate

A candidate sustainability outcome `J_j` is retained only if all six fields are explicit:

```math
\boxed{
A_j
=
\mathbb 1[
Def_j\land Unit_j\land Data_j\land Mechanism_j\land Horizon_j\land Validation_j
]
}
```

where:
1. `Def_j` — unambiguous mathematical definition;
2. `Unit_j` — declared physical/economic/social unit or normalized quantity;
3. `Data_j` — obtainable data or defensible model inputs;
4. `Mechanism_j` — causal connection to P–T–I–O dynamics;
5. `Horizon_j` — event, recovery, annual, lifecycle or other declared horizon;
6. `Validation_j` — independent validation or uncertainty test.

If `A_j=0`, the quantity is not a thesis sustainability outcome; it remains a candidate only.

## 5. Candidate outcome hierarchy — not yet frozen

To preserve MSE tractability, the first evidence audit should prioritize outcomes with direct mechanistic observability:

```math
\mathbf J_{\rm sus}^{cand}
=
\begin{bmatrix}
J_{\rm carbon}\\
J_{\rm cost}\\
J_{\rm accessibility}
\end{bmatrix}
```

with energy/resource flows treated initially as physical mediators unless evidence justifies their use as independent objectives.

Equity should be retained only if a distributional definition and population/geographic data can be qualified, for example

```math
J_{\rm inequity}=\mathcal D\!\left(\{A_g\}_{g\in\mathcal G_{pop}}\right),
```

where `D` is a declared disparity functional and `A_g` is accessibility/service for population group or spatial unit `g`.

No component above is frozen by this document.

## 6. Evidence-qualified causal chain

For every retained dependency, require

```math
\boxed{
\mathfrak d_e
\rightarrow
\Delta F_{\mathcal G}^{m}
\rightarrow
\Delta Y
\rightarrow
\Delta R_i
\quad\text{and/or}\quad
\Delta J_j
}
```

with a source for every arrow.

A resilience metric is not automatically the causal mediator of a sustainability outcome. When the shared state trajectory is the true cause, record the architecture as

```math
\theta_e\rightarrow Y_{0:T}\rightarrow\{R_i,J_j\}
```

rather than forcing

```math
R_i\rightarrow J_j.
```

## 7. Translation sensitivities

For differentiable mechanism parameters and declared direction `v`, define

```math
S_{e,i}^{R}(Y)
=
D_{\theta_e}R_i(Y;\Theta)[v]
```

and

```math
\boxed{
S_{e,j}^{S}
=
D_{\theta_e}J_j(Y,u,\mathbf a,\omega;\Theta)[v].
}
```

For nonsmooth, hybrid or topological perturbations use matched finite or actual intervention contrasts:

```math
\Delta_e R_i
=R_i(\Theta\oplus\Delta_e)-R_i(\Theta),
```

```math
\Delta_e J_j
=J_j(\Theta\oplus\Delta_e)-J_j(\Theta).
```

These are diagnostics, not novelty claims.

## 8. Intervention comparison

For transformation action `a_k`, use matched counterfactual contrasts

```math
\Delta R_i(\mathbf a_k)
=R_i(\mathfrak M_{k+1})-R_i(\mathfrak M_k),
```

```math
\Delta J_j(\mathbf a_k)
=J_j(\mathfrak M_{k+1})-J_j(\mathfrak M_k).
```

The thesis must explicitly allow

```math
\boxed{
\Delta R_i(\mathbf a_p)>\Delta R_i(\mathbf a_q)
\not\Rightarrow
\Delta J_j(\mathbf a_p)>\Delta J_j(\mathbf a_q).
}
```

This is the mathematical reason Stage 7 remains many-objective rather than collapsing resilience and sustainability into a single unvalidated score.

## 9. Evidence states for thesis translation paths

Use:
- `CANDIDATE` — plausible path identified, no qualifying direct evidence yet;
- `SUPPORTED_MECHANISM` — source supports the causal mechanism;
- `QUANTIFIED` — source/data support a quantitative transformation;
- `CALIBRATED` — parameters estimated on qualified data;
- `VALIDATED` — held-out/external/context-of-use validation passed;
- `REJECTED` — evidence contradicts or fails the proposed link.

Blank is never interpreted as support.

## 10. Initial thesis matrix — candidate rows only

| ID | Dependency | Mechanism | Resilience diagnostic | Sustainability consequence candidate | Status |
|---|---|---|---|---|---|
| RS-01 | `P -> T` | feeder/charger outage reduces charging service and creates backlog | mobility service loss; backlog; recovery hysteresis | critical-mobility accessibility; event-related energy/emission consequence | `SUPPORTED_MECHANISM / sustainability mapping pending` |
| RS-02 | `T -> P` | road state changes crew access and restoration delay | power recovery time; service-loss integral | outage-related economic burden; backup-energy/emission consequence | `SUPPORTED_MECHANISM / sustainability mapping pending` |
| RS-03 | `T -> P` | EV charging demand changes electric load | grid stress/service trajectory | marginal energy/carbon consequence; renewable-utilization consequence | `CANDIDATE` |
| RS-04 | `I -> P,T` | observation quality changes state estimate and operational decision | decision error; avoidable service loss | avoidable resource/cost consequence | `CANDIDATE` |
| RS-05 | `O -> u` | crews/resources/authority constrain feasible control | response delay; recovery/viability | cost/accessibility/distributional consequence | `CANDIDATE` |

No candidate sustainability consequence is promoted to validated status by this table.

## 11. Immediate evidence program

The next evidence work is not a new generic review. Extend the existing review with three mapping layers:

```math
M^{IR}_{e i}
=
\sum_p\mathbb 1[paper_p\text{ directly supports }\mathfrak d_e\rightarrow R_i],
```

```math
M^{YS}_{e j}
=
\sum_p\mathbb 1[paper_p\text{ directly implements }Y/\text{consequence}\rightarrow J_j],
```

```math
M^{SD}_{j k}
=
\sum_p\mathbb 1[paper_p\text{ uses }J_j\rightarrow\text{decision/alternative }\mathbf a_k].
```

These are evidence-coverage matrices, not causal coefficients.

The target architecture becomes

```math
\boxed{
\mathfrak d_e
\rightarrow
F_{\mathcal G}^{m}
\rightarrow
Y
\rightarrow
\{\mathbf R,\mathbf J_{\rm sus}\}
\rightarrow
\Phi_{\rm ST}
\rightarrow
\mathbf a.
}
```

## 12. Current scientific decision

The correct next task is to qualify `RS-01` and `RS-02` first because they are already implemented and verified in the H1 M2 demonstrator. This minimizes new model invention and maximizes traceability from evidence to dynamics to sustainability consequence.

No final Stage-6 trigger, sustainability threshold, Pareto frontier, or transformation preference is authorized until the corresponding outcome definitions, data, uncertainty and validation gates pass.
