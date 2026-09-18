# 1.11 Research Hypotheses and Test Logic

Sections 1.8–1.10 define the overall research destination, the questions to be answered, and the specific accomplishments required. This section states the subset of claims that are **falsifiably tested**. The thesis retains exactly five primary hypotheses, (H_1)–(H_5). RQ1/SO1 and RQ2/SO2 carry developmental and evidence-qualification obligations supporting H1; they do not require additional hypotheses.

The test architecture follows four rules. First, each hypothesis is evaluated through a declared comparator rather than by demonstrating only that a proposed model can produce an output. Second, confirmatory response quantities and aggregation rules must be fixed before confirmatory execution. Third, uncertainty treatment must be consistent with the evidence available; scenario frequencies are not interpreted as probabilities unless a defensible probability model exists. Fourth, failure to meet the preregistered comparison criterion is reported as **non-support within the declared validity domain**, not hidden through post hoc metric substitution.

## H1 — Dynamic causal interdependency

> **H1:** Under matched Power–Transportation disturbances and initial conditions, an evidence-grounded dynamic causal coupling representation provides measurable incremental explanatory or predictive information for preregistered cascade, service-loss, spatial-propagation, and recovery outcomes relative to corresponding static-coupling and independent-system representations.

**Question/objective mapping:** RQ3/SO3, with developmental inputs from RQ1/SO1 and RQ2/SO2.

The comparator architecture is

```math
M_0=	ext{independent }P+T,
qquad
M_1=	ext{static/algebraic }P	ext{--}T	ext{ coupling},
qquad
M_2=	ext{dynamic causal }P	ext{--}T	ext{ coupling}.
```

The primary confirmatory contrast is (M_2) against (M_1), with (M_0) retained as the uncoupled reference. Candidate response classes include cascade timing, number of failed components, service loss, spatial propagation, and recovery time; the exact response vector, distance/skill measure, meaningful-effect threshold, and scenario aggregation rule must be frozen before confirmatory testing.

**Uncertainty treatment.** The same hazard realizations, initial states, service requirements, and exogenous conditions are used across (M_0,M_1,M_2). Uncertain inputs are propagated consistently across the matched comparison so that differences are attributable to coupling representation rather than unequal disturbance samples.

**Non-support condition.** H1 is not supported in the declared domain if (M_2) fails to provide at least the preregistered meaningful incremental explanatory or predictive information relative to (M_1).

## H2 — Information, organization, and feasible control

> **H2:** Under matched physical states and disturbances, changes in information availability and organizational conditions produce measurable differences in state-estimation quality, feasible control actions, response timing, recovery trajectories, and Stage-5 resilience outcomes.

**Question/objective mapping:** RQ4/SO4.

The nested comparison is

```math
mathscr N_0=P+T,
qquad
mathscr N_1=P+T+I,
qquad
mathscr N_2=P+T+I+O,
```

where (mathscr N_1-mathscr N_0) isolates the modeled information effect and (mathscr N_2-mathscr N_1) isolates the modeled organizational effect. Candidate response classes include state-estimation error, feasible-control-set change, response delay, service loss, recovery time, and viability/recovery probabilities. The exact intermediate and downstream responses and their meaningful-effect criteria must be preregistered.

**Uncertainty treatment.** Physical initial condition, physical damage, hazard realization, and other exogenous physical conditions are held matched while only prespecified information and organizational conditions are perturbed. Observation, information, and organizational uncertainties are represented explicitly rather than absorbed into physical-state uncertainty.

**Non-support condition.** H2 is not supported if the prespecified information/organization contrasts fail to produce the minimum preregistered effect in the declared intermediate and downstream outcomes over the tested domain.

## H3 — Uncertainty-aware viability and reachability resilience

> **H3:** For the declared Power–Transportation test domain, the combined uncertainty-aware viability–reachability resilience object provides measurable incremental predictive or decision-relevant information about future service maintainability and acceptable recovery beyond prespecified conventional performance/recovery-curve metrics.

**Question/objective mapping:** RQ5/SO5.

The comparison is

```math
R_{m curve}
quad	ext{versus}quad
R_{m curve}+mathfrak R_T,
```

with the Stage-5 resilience object preserving

```math
mathfrak R_T
=
left(
mathcal V_{alpha,T},
mathcal R_{eta,T},
ho_{mathcal V},
T_{mathcal V},
T_{m rec},
P_{m viable},
P_{m recover}
ight).
```

Thus Stage 5 evaluates **remain + return + confidence** rather than viability alone. The primary response is the incremental predictive or decision-relevant skill obtained by adding (mathfrak R_T) to the prespecified conventional benchmark. The exact skill measure, (K), recovery target, forbidden set, horizon, probability/confidence levels, and meaningful-effect threshold must be frozen before confirmatory execution.

**Uncertainty treatment.** Viability and reachability are evaluated under the declared uncertainty model and feasible-control set. Probability is used only when its stochastic interpretation is justified; otherwise the analysis must use an explicitly nonprobabilistic robustness formulation rather than relabel scenario frequencies as probabilities.

**Non-support condition.** H3 is not supported if adding (mathfrak R_T) fails to improve the preregistered predictive or decision metric by at least the declared meaningful amount within the tested domain. Interface criticality remains a supporting diagnostic and is not the primary H3 claim.

## H4 — Engineering intervention and sustainability consequences

> **H4:** Across the prespecified intervention and scenario set, engineering interventions that produce meaningful resilience improvement are not equivalent in their sustainability consequence vectors; at least two resilience-effective interventions produce materially different accessibility, energy, carbon, or cost consequences under the declared comparison rule.

**Question/objective mapping:** RQ6/SO6.

The core intervention logic is

```math
a_k
ightarrow
left(
Deltamathfrak R^{a_k},
Deltamathbf J_{m sus}^{a_k}
ight),
```

with effectiveness, resource efficiency, and sustainability kept distinct. The comparison is made **among qualified resilience-effective interventions**, not between arbitrary alternatives. The principal response is the difference in admitted sustainability-consequence vectors under a preregistered distance, dominance, or decision rule.

At the current Chapter-I freeze, direct cost, operational electrical energy, and operational/partial carbon are planned core consequence families but remain **confirmatory-CONDITIONAL** until their case data, intervention definitions, accounting boundaries, and VVUQ requirements pass the admission gates. Distributional accessibility and crew-hours remain conditional extensions. Therefore H4 defines the hypothesis architecture but is not considered confirmatory-ready merely because the hypothesis is stated here.

**Uncertainty treatment.** Intervention performance and admitted consequence quantities are evaluated over the same qualified scenario/uncertainty ensemble, with accounting uncertainty separated from physical, model-form, parameter, observation, and intervention-resource uncertainty where relevant.

**Non-support condition.** H4 is not supported if qualified resilience-effective interventions are indistinguishable under the preregistered admitted sustainability-consequence comparison within the tested domain, or if too few interventions/metrics pass the qualification gates to make the planned comparison. In the latter case the result is **BLOCKED**, not evidence for or against H4. Interface criticality may support target selection but is not the primary H4 test.

## H5 — Joint resilience–sustainability engineering decision

> **H5:** Under the declared uncertainty domain and intervention set, incorporating sustainability consequences into resilience-based engineering evaluation produces a materially different admissible or nondominated intervention set, or materially changes decision regret, relative to resilience-only evaluation.

**Question/objective mapping:** RQ7/SO7.

The decision comparison is

```math
mathcal A_R^{star}
quad	ext{versus}quad
mathcal A_{R,S}^{star},
```

where the exact decision construction—such as constrained optimum, Pareto/nondominated set, satisficing set, or robust decision set—must be fixed before confirmatory execution. The principal response is a preregistered change in admissible/nondominated sets, dominance relations, or decision regret.

H5 inherits the sustainability-admission requirements of H4. A joint resilience–sustainability decision cannot be declared confirmatory-ready until the sustainability quantities used in the decision rule have passed their data, accounting-boundary, feasibility, and VVUQ gates.

**Uncertainty treatment.** If defensible scenario probabilities are available, probabilistic decision measures may be used. Under deep uncertainty, scenario frequencies must not be interpreted as probabilities; robust, satisficing, regret, or scenario-coverage measures are used instead.

**Non-support condition.** H5 is not supported if resilience-only and joint resilience–sustainability evaluation are not materially different under the preregistered decision metric, or if admitted sustainability information does not alter the declared engineering decision within the tested uncertainty domain. If sustainability inputs have not passed their admission gates, H5 remains **BLOCKED** rather than being adjudicated.

## Hypothesis traceability and scientific status

The final question–objective–hypothesis mapping is

```math
oxed{
egin{aligned}
RQ_1/SO_1,;RQ_2/SO_2
&ightarrow
	ext{developmental/evidence obligations supporting }H_1,\\
RQ_3/SO_3 &ightarrow H_1,\\
RQ_4/SO_4 &ightarrow H_2,\\
RQ_5/SO_5 &ightarrow H_3,\\
RQ_6/SO_6 &ightarrow H_4,\\
RQ_7/SO_7 &ightarrow H_5.
end{aligned}
}
```

Consequently,

```math
oxed{
7 	ext{research questions}

otRightarrow
7 	ext{hypotheses}.
}
```

For every hypothesis, confirmatory execution requires the relevant comparator, response definition, meaningful-effect threshold or decision rule, scenario/uncertainty ensemble, aggregation rule, and validity domain to be frozen before the confirmatory run. Numerical thresholds such as (delta_1,ldots,delta_5), Stage-5 probability/confidence levels, and final H3–H5 decision metrics remain open until their evidence and data qualification gates close. This prevents post hoc threshold selection and preserves the distinction among **PASS**, **FAIL**, and **BLOCKED** established in Section 1.7.

Section 1.12 next states the proposed contributions in conditional proposal language; no contribution is treated as demonstrated until the corresponding evidence, validation, and hypothesis chain closes.
