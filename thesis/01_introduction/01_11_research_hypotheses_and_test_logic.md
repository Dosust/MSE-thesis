# 1.11 Research Hypotheses and Test Logic

Sections 1.8–1.10 define the research destination, questions, and specific objectives. This section states the subset of claims subjected to falsifiable tests. The thesis retains exactly five primary hypotheses, H1–H5. RQ1/SO1 and RQ2/SO2 carry developmental and evidence-qualification obligations supporting H1; they do not require additional hypotheses.

Each hypothesis is controlled by four elements: **comparator**, **response**, **uncertainty treatment**, and **non-support logic**. Detailed equations, scenario construction, statistical procedures, VVUQ implementation, and preregistration belong to Chapter 4.

## H1 — Dynamic causal interdependency

> **H1:** Under matched Power–Transportation disturbances and initial conditions, an evidence-grounded dynamic causal coupling representation provides measurable incremental explanatory or predictive information for preregistered cascade, service-loss, spatial-propagation, and recovery outcomes relative to corresponding static-coupling and independent-system representations.

**Mapping:** RQ3/SO3, with RQ1/SO1 and RQ2/SO2 as developmental inputs.

```math
M_0=\text{independent }P+T,\qquad
M_1=\text{static/algebraic }P\text{--}T\text{ coupling},\qquad
M_2=\text{dynamic causal }P\text{--}T\text{ coupling}.
```

**Comparator:** primary $M_2$ versus $M_1$, with $M_0$ as the uncoupled reference.  
**Response:** preregistered cascade, service-loss, spatial-propagation, and recovery quantities.  
**Uncertainty:** matched hazard realizations, initial states, service requirements, and exogenous conditions across all comparators.  
**Non-support:** H1 is not supported if $M_2$ fails to provide the preregistered meaningful incremental information relative to $M_1$ within the declared validity domain.

## H2 — Information, organization, and feasible control

> **H2:** Under matched physical states and disturbances, changes in information availability and organizational conditions produce measurable differences in state-estimation quality, feasible control actions, response timing, recovery trajectories, and Stage-5 resilience outcomes.

**Mapping:** RQ4/SO4.

```math
\mathscr N_0=P+T,\qquad
\mathscr N_1=P+T+I,\qquad
\mathscr N_2=P+T+I+O.
```

**Comparator:** $\mathscr N_1-\mathscr N_0$ isolates the modeled information effect; $\mathscr N_2-\mathscr N_1$ isolates the modeled organizational effect.  
**Response:** state-estimation quality, feasible-control change, response timing, service trajectory, recovery, and Stage-5 resilience quantities.  
**Uncertainty:** physical state and disturbance are matched while only declared information/organizational conditions are perturbed.  
**Non-support:** H2 is not supported if the preregistered information/organization contrasts do not produce the minimum declared effect in the specified intermediate and downstream outcomes.

## H3 — Uncertainty-aware viability and reachability resilience

> **H3:** For the declared Power–Transportation test domain, the combined uncertainty-aware viability–reachability resilience object provides measurable incremental predictive or decision-relevant information about future service maintainability and acceptable recovery beyond prespecified conventional performance/recovery-curve metrics.

**Mapping:** RQ5/SO5.

```math
R_{\mathrm{curve}}
\quad\text{versus}\quad
R_{\mathrm{curve}}+\mathfrak R_T.
```

The Stage-5 object preserves

```math
\mathfrak R_T=
\left(
\mathcal V_{\alpha,T},
\mathcal R_{\beta,T},
\rho_{\mathcal V},
T_{\mathcal V},
T_{\mathrm{rec}},
P_{\mathrm{viable}},
P_{\mathrm{recover}}
\right),
```

so Stage 5 represents **remain + return + confidence**, not viability alone.

**Comparator:** prespecified conventional performance/recovery-curve information versus the same benchmark augmented by $\mathfrak R_T$.  
**Response:** preregistered incremental predictive or decision-relevant skill.  
**Uncertainty:** viability/reachability are evaluated under the declared uncertainty model and feasible-control set; probability is used only when probabilistically justified.  
**Non-support:** H3 is not supported if adding $\mathfrak R_T$ fails to improve the preregistered predictive or decision metric by the declared meaningful amount. Interface criticality remains a supporting diagnostic, not the primary H3 claim.

## H4 — Engineering intervention and sustainability consequences

> **H4:** Across the prespecified intervention and scenario set, engineering interventions that produce meaningful resilience improvement are not equivalent in their sustainability consequence vectors; at least two resilience-effective interventions produce materially different accessibility, energy, carbon, or cost consequences under the declared comparison rule.

**Mapping:** RQ6/SO6.

The H4 evaluation preserves the distinction

```math
\boxed{
\text{effectiveness}
\neq
\text{resource efficiency}
\neq
\text{sustainability consequence}.
}
```

```math
a_k
\rightarrow
\left(
\Delta\mathfrak R^{a_k},
\Delta\mathbf J_{\mathrm{sus}}^{a_k}
\right).
```

**Comparator:** qualified resilience-effective interventions compared under the same admitted sustainability-consequence rule.  
**Response:** differences in admitted cost, operational-energy, carbon/GHG, accessibility, or other qualified consequence quantities within declared accounting boundaries.  
**Uncertainty:** physical, model-form, parameter, observation, intervention/resource, and accounting uncertainties are propagated consistently where relevant.  
**Non-support/BLOCKED:** if enough qualified interventions and admitted metrics exist but no material consequence difference is found, H4 is not supported; if the intervention set or sustainability metrics fail admission/data/VVUQ gates, H4 is **BLOCKED**, not failed. Interface criticality may support target selection but is not the primary H4 test.

## H5 — Joint resilience–sustainability engineering decision

> **H5:** Under the declared uncertainty domain and intervention set, incorporating sustainability consequences into resilience-based engineering evaluation produces a materially different admissible or nondominated intervention set, or materially changes decision regret, relative to resilience-only evaluation.

**Mapping:** RQ7/SO7.

```math
\mathcal A_R^{\star}
\quad\text{versus}\quad
\mathcal A_{R,S}^{\star}.
```

**Comparator:** resilience-only engineering evaluation versus joint resilience–sustainability evaluation.  
**Response:** preregistered change in admissible/nondominated sets, dominance relations, or decision regret.  
**Uncertainty:** probabilistic measures are used only when defensible probabilities exist; otherwise robust, satisficing, regret, or scenario-coverage measures are used.  
**Non-support/BLOCKED:** if admitted sustainability information does not materially change the declared engineering decision, H5 is not supported; if the required sustainability inputs have not passed admission and VVUQ gates, H5 remains **BLOCKED**.

## Hypothesis traceability and status rule

```math
\boxed{
\begin{aligned}
RQ_1/SO_1,\;RQ_2/SO_2
&\rightarrow
\text{developmental/evidence obligations supporting }H_1,\\
RQ_3/SO_3 &\rightarrow H_1,\\
RQ_4/SO_4 &\rightarrow H_2,\\
RQ_5/SO_5 &\rightarrow H_3,\\
RQ_6/SO_6 &\rightarrow H_4,\\
RQ_7/SO_7 &\rightarrow H_5.
\end{aligned}
}
```

```math
\boxed{
7\ \text{research questions}\not\Rightarrow 7\ \text{hypotheses}.
}
```

Confirmatory execution requires the relevant comparator, response definition, meaningful-effect threshold or decision rule, uncertainty/scenario domain, aggregation rule, and validity domain to be frozen before the confirmatory run. Numerical thresholds and final H3–H5 decision metrics remain open until their evidence and data-qualification gates close. This preserves the PASS/FAIL/BLOCKED distinction established in Section 1.7 without importing Chapter-4 derivations into Chapter 1.
