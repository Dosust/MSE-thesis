# Research Hypotheses — Complete Seven-Stage Framework

![Framework](https://img.shields.io/badge/framework-1--7%20FROZEN-1A7F37)
![Hypotheses](https://img.shields.io/badge/hypothesis%20logic-FROZEN-1A7F37)
![Thresholds](https://img.shields.io/badge/numerical%20thresholds-NOT%20SET-9A6700)

**Status:** CANONICAL HYPOTHESIS ARCHITECTURE / LOGIC FROZEN  
**Date:** 2026-09-11  
**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Framework:** complete frozen seven-stage P–T–I–O thesis framework  
**Citation standard:** APA 7th edition author–date  
**Change rule:** The scientific logic of the five primary hypotheses is frozen. Numerical thresholds $\delta_1,\ldots,\delta_5$, exact metrics, scenario ensembles, and statistical decision rules remain to be specified *a priori* in the Hypothesis Specification Matrix before confirmatory numerical testing.

> **Authority rule:** This file defines the five primary confirmatory hypotheses. `SCIENTIFIC_PROPOSITIONS.md` remains the broader proposition/falsification registry; its propositions are subordinate tests, mechanisms, diagnostics, or supporting claims and must not be mistaken for additional primary hypotheses.

---

## 1. Hypothesis architecture

The thesis hypotheses follow

$$
\text{Theory}
\rightarrow
\text{Mechanism}
\rightarrow
\text{Hypothesis}
\rightarrow
\text{Prediction}
\rightarrow
\text{Baseline}
\rightarrow
\text{Falsification}.
$$

The framework uses **five primary hypotheses**, rather than one hypothesis per stage.

---

## 2. Overarching scientific hypothesis

### $H_{\mathrm{SYS}}$

Infrastructure resilience and sustainable transformation cannot be adequately characterized from physical-network structure alone because causal interdependencies, dynamics, information, organization, and feasible control jointly determine propagation, viability, and transformation pathways.

This is the theoretical hypothesis. It is not intended to be accepted or rejected through one isolated statistical test. It is decomposed into five falsifiable primary hypotheses.

---

## 3. $H_1$ — Dynamic interdependency hypothesis

### Scientific question

Does representing interdependencies as **dynamic causal mechanisms** materially change predicted disruption propagation compared with static or aggregated network representations?

Stage 2 defines

$$
\mathfrak I_{ij}^{\alpha\beta}
=
\left(
E_i^\alpha,E_j^\beta,M_{ij},w_{ij},\delta_{ij},\tau_{ij},a_{ij},m,\mathcal H_t
\right),
$$

and Stage 3 maps accepted mechanisms into coupled dynamics:

$$
\mathfrak I
\rightarrow
F_{\mathcal G}^{m}
\rightarrow
Y(t).
$$

### Hypothesis

**$H_1$:** Under coupled P–T disturbances, explicitly modeling dynamic interdependency mechanisms produces materially different cascade and service trajectories from static or aggregated coupling models.

### Baselines

$$
M_{1,0}=\text{independent }P+T,
$$

$$
M_{1,1}=\text{static coupled }P\text{--}T,
$$

$$
M_{1,2}=\text{dynamic causal }P\text{--}T\text{ coupling}.
$$

Let

$$
Z_C=
\begin{bmatrix}
T_C\\
N_{\mathrm{fail}}\\
L_{\mathrm{service}}\\
T_{\mathrm{recovery}}
\end{bmatrix}.
$$

The confirmatory prediction is

$$
D\!\left(Z_C^{M_{1,2}},Z_C^{M_{1,0/1}}\right)
\ge\delta_1,
$$

where $D(\cdot,\cdot)$ is a prespecified trajectory/performance difference measure and $\delta_1$ is a scientifically meaningful threshold defined before final testing.

### Falsification criterion

$H_1$ is challenged if

$$
D\!\left(Z_C^{M_{1,2}},Z_C^{M_{1,0/1}}\right)<\delta_1
$$

consistently across the declared scenario domain. In that case, the additional Stage-2/3 coupling complexity would not have demonstrated material value for the tested application.

---

## 4. $H_2$ — Information–organization hypothesis

### Scientific question

Do the informational and organizational layers materially alter resilience relative to a physical-only model?

The Stage-4 causal spine is

$$
X
\rightarrow y
\rightarrow I
\rightarrow\widehat X
\rightarrow O
\rightarrow u
\rightarrow X.
$$

Information degradation changes quantities such as latency, freshness, and estimation error; organizational limitations change decision, coordination, resource, and mobilization capability. These mechanisms affect

$$
\mathcal U(z_I,z_O),
$$

response timing, action quality, and therefore the physical trajectory.

### Hypothesis

**$H_2$:** Information degradation and organizational constraints materially alter the feasible response set, cascade–response competition, and recovery of the coupled infrastructure system relative to a physical-only model.

### Nested models

$$
M_0=P+T,
$$

$$
M_1=P+T+I,
$$

$$
M_2=P+T+I+O.
$$

Hence

$$
M_1-M_0=\text{information effect},
$$

$$
M_2-M_1=\text{organizational effect}.
$$

Representative intermediate responses include

$$
\operatorname{RMSE}(\widehat X,X),
\qquad
\tau_{\mathrm{response}},
\qquad
u(t),
$$

with downstream outcomes such as

$$
L_{\mathrm{service}},
\qquad
T_C,
\qquad
T_{\mathrm{recovery}}.
$$

For a prespecified resilience-output vector $Z_R$,

$$
D\!\left(Z_R^{M_2},Z_R^{M_0}\right)\ge\delta_2.
$$

The response-time mechanism is

$$
\begin{aligned}
\tau_{\mathrm{response}}={}&
\tau_{\mathrm{sense}}
+\tau_{\mathrm{comm}}
+\tau_{\mathrm{est}}
+\tau_{\mathrm{decision}}\\
&+\tau_{\mathrm{coord}}
+\tau_{\mathrm{mobilization}}
+\tau_{\mathrm{act}},
\end{aligned}
$$

for sequential non-overlapping response processes; overlapping processes require the appropriate critical-path interpretation.

### Falsification criterion

$H_2$ is challenged if, across the declared operating range, perturbations of $I$ and $O$ generate negligible changes in $\mathcal U$, $\tau_{\mathrm{response}}$, and the prespecified system outcomes.

---

## 5. $H_3$ — Controlled-viability hypothesis

### Scientific question

Does Stage-5 controlled viability add decision-relevant information beyond conventional service-loss and recovery metrics?

Two states may have approximately identical current service,

$$
S(Y_1)=S(Y_2),
$$

while differing in future maintainability:

$$
Y_1\in\mathcal V,
\qquad
Y_2\notin\mathcal V.
$$

Therefore,

$$
\text{current performance}
\neq
\text{future maintainability}.
$$

### Hypothesis

**$H_3$:** Controlled-viability quantities distinguish impending loss of maintainability that is not fully captured by conventional instantaneous service or recovery metrics.

### Baselines

$$
Q_{\mathrm{conventional}}
=
\{S(t),L_{\mathrm{service}},T_{\mathrm{recovery}}\},
$$

$$
Q_{\mathrm{viability}}
=
\{\rho,T_{\mathcal V},T_K,S_{\mathcal V}\}.
$$

For a future-failure outcome

$$
Y_{\mathrm{fail}}
=
\mathbf 1\!\left\{Y(t+\Delta)\notin K_{\mathrm{sus}}\right\},
$$

the confirmatory prediction is

$$
\operatorname{Skill}
\!\left(Q_{\mathrm{conventional}}+Q_{\mathrm{viability}}\right)
-
\operatorname{Skill}
\!\left(Q_{\mathrm{conventional}}\right)
\ge\delta_3.
$$

`Skill` must later be defined using a justified prediction-error, discrimination, calibration, lead-time, or related metric.

A strong matched-state test seeks $Y_a,Y_b$ with

$$
S(Y_a)\approx S(Y_b),
$$

but

$$
\rho(Y_a)\neq\rho(Y_b),
$$

and tests whether their subsequent futures differ as predicted.

### Falsification criterion

If viability measures fail to improve prediction or discrimination beyond simpler service metrics by at least $\delta_3$, then their additional complexity is not justified for the tested application.

---

## 6. $H_4$ — Interface-criticality hypothesis

### Scientific question

Can viability-sensitive interface rankings identify more valuable intervention targets than static structural centrality?

Let

$$
\theta_{ij}=(w_{ij},\delta_{ij},\tau_{ij},a_{ij}).
$$

Perturbation propagates through

$$
\theta_{ij}
\rightarrow
F
\rightarrow
\mathcal V
\rightarrow
\rho,
$$

producing the Stage-5 interface sensitivity $S_{ij}^{\mathcal V}$.

### Hypothesis

**$H_4$:** Interfaces ranked as highly critical by viability sensitivity identify interventions that improve controlled viability more effectively than rankings based only on static structural centrality.

### Competing ranking models

$$
R_1=\text{degree-based ranking},
$$

$$
R_2=\text{betweenness-based ranking},
$$

$$
R_3=\text{flow-based ranking},
$$

$$
R_4=S_{ij}^{\mathcal V}.
$$

Equal-budget interventions selected from each ranking are compared using outcomes such as

$$
\Delta\mathcal V,
\qquad
\Delta\rho,
\qquad
\Delta T_{\mathcal V},
\qquad
\Delta L_{\mathrm{service}}.
$$

A candidate confirmatory prediction is

$$
\mathbb E[\Delta\mathcal V\mid R_4]
-
\max_{r\in\{1,2,3\}}
\mathbb E[\Delta\mathcal V\mid R_r]
\ge\delta_4.
$$

Equivalent tests may use another prespecified viability outcome.

### Falsification criterion

If structural centrality performs equally well or better under equal intervention budgets across the prespecified scenario ensemble, then $S_{ij}^{\mathcal V}$ has not demonstrated additional intervention value.

---

## 7. $H_5$ — Adaptive-transformation-pathway hypothesis

### Scientific question

Under deep uncertainty, do adaptive trigger-based transformation pathways produce more robust resilience–sustainability–equity trade-offs than fixed intervention sequences?

The fixed comparator is

$$
\Pi_F=[(a_1,t_1),\ldots,(a_N,t_N)],
$$

whereas an adaptive policy uses

$$
a_k
=
\pi_k
\!\left(
\widehat Y_k,
 z_{I,k},
 z_{O,k},
 \mathcal M_k,
 \mathcal H_k
\right).
$$

Uncertain futures satisfy

$$
\omega\in\Omega.
$$

### Hypothesis

**$H_5$:** Across deeply uncertain futures, adaptive transformation policies provide a more robust resilience–sustainability–equity trade-off than fixed intervention sequences with comparable resources.

### Comparison

$$
\Pi_F=\text{best fixed pathway},
$$

$$
\Pi_A=\text{adaptive trigger-based pathway}.
$$

Evaluate both over

$$
\Omega=\{\omega_1,\ldots,\omega_M\}
$$

using the frozen Stage-7 objective vector

$$
\mathbf J
=
\begin{bmatrix}
J_{\mathrm{risk}}\\
J_{\mathrm{service}}\\
J_{\mathrm{cost}}\\
J_{\mathrm{carbon}}\\
J_{\mathrm{inequity}}\\
J_{\mathrm{time}}\\
J_{\mathrm{flexibility}}
\end{bmatrix}.
$$

The hypothesis does **not** require the adaptive pathway to dominate every objective in every scenario. Appropriate confirmatory forms include robust dominance or satisficing, for example

$$
\mathcal R(\Pi_A)
>
\mathcal R(\Pi_F)+\delta_5,
$$

or

$$
P_{\mathrm{sat}}(\Pi_A)
-
P_{\mathrm{sat}}(\Pi_F)
\ge\delta_5.
$$

### Falsification criterion

If the adaptive pathway does not materially improve robustness, or if its flexibility benefit is offset by excessive cost, delay, or implementation burden, then $H_5$ is not supported.

---

## 8. Causal hierarchy of the five hypotheses

The hypotheses are intentionally linked:

$$
H_1:\quad \mathfrak I\rightarrow F,
$$

$$
H_2:\quad I,O\rightarrow\mathcal U,u\rightarrow F,
$$

$$
H_3:\quad F+\mathcal U\rightarrow\mathcal V,
$$

$$
H_4:\quad \mathfrak I\rightarrow S_{ij}^{\mathcal V}\rightarrow\text{intervention value},
$$

$$
H_5:\quad \mathcal V+\Phi_{\mathrm{ST}}\rightarrow\boldsymbol\pi\rightarrow\mathbb M_{\mathrm{sus}}.
$$

Together,

$$
\mathfrak I
\rightarrow
F
\rightarrow
(I,O,u)
\rightarrow
\mathcal V
\rightarrow
S_{ij}^{\mathcal V}
\rightarrow
\text{adaptive transformation}.
$$

---

## 9. Hypothesis-to-stage map

| Hypothesis | Main stages tested | Core scientific claim |
|---|---:|---|
| $H_1$ | 2 → 3 | Dynamic causal coupling matters. |
| $H_2$ | 3 → 4 | Information and organization alter physical resilience. |
| $H_3$ | 4 → 5 | Controlled viability adds information beyond performance curves. |
| $H_4$ | 2 → 5 → 7 | Viability-sensitive interfaces provide better intervention targets. |
| $H_5$ | 5 → 6 → 7 | Adaptive pathways outperform fixed pathways under deep uncertainty. |

---

## 10. Numerical thresholds are deliberately not frozen yet

Do **not** assign arbitrary values such as a 20% improvement threshold without scientific justification.

For now retain

$$
\delta_1,\ldots,\delta_5.
$$

Each threshold must be determined *before confirmatory testing* from one or more justified sources:

- engineering standards;
- literature-derived meaningful effects;
- baseline variability;
- pilot-study evidence;
- decision significance.

Choosing $\delta_i$ after observing final results would undermine confirmatory rigor.

---

## 11. Frozen hypothesis logic

The primary hypothesis set is

$$
\mathbb H
=
\{H_1,H_2,H_3,H_4,H_5\}.
$$

Each hypothesis will ultimately be specified by

$$
\mathscr H_i
=
\left(
T_i,
M_i,
X_i,
Y_i,
B_i,
\Omega_i,
\delta_i,
P_i,
A_i,
C_i,
F_i,
U_i
\right),
$$

where the exact field definitions must be fixed in the Hypothesis Specification Matrix.

The matrix must explicitly freeze, for each hypothesis:

$$
\text{theory}
+
\text{mechanism}
+
\text{variables}
+
\text{baseline}
+
\text{boundary conditions}
+
\text{prediction}
+
\text{rival hypothesis}
+
\text{critical test}
+
\text{falsification criterion}.
$$

---

## 12. Next scientific task

The next rigorous step is **not confirmatory simulation yet**.

It is to construct the **Hypothesis Specification Matrix** for $H_1$–$H_5$, define every field in $\mathscr H_i$, justify $\delta_i$ *a priori*, and only then move to numerical testing.

> **PRIMARY HYPOTHESIS LOGIC: FROZEN. NUMERICAL THRESHOLDS AND TEST SPECIFICATIONS: NOT YET FROZEN.**
