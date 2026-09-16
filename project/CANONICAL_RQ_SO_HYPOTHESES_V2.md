# Canonical Research Questions, Objectives, and Hypotheses — v2.0

![Authority](https://img.shields.io/badge/authority-CANONICAL-0969DA)
![Logic](https://img.shields.io/badge/RQ--SO--H-v2.0%20FROZEN-1A7F37)
![Citation](https://img.shields.io/badge/APA%207-REQUIRED-8250DF)
![Novelty](https://img.shields.io/badge/novelty-SEPARATE%20GATE-9A6700)

**Status:** CANONICAL v2.0 / SCIENTIFIC LOGIC FROZEN  
**Effective date:** 2026-09-16  
**Framework authority:** `CANONICAL_7_STAGE_FRAMEWORK_V2.md`  
**Reasoning authority:** `RESEARCH_REASONING_PROTOCOL.md` v1.2  
**Execution method:** EGMIV — Evidence-Grounded Mechanistic Interdependency and Validation  
**Citation standard:** APA 7th edition author–date  
**Change rule:** the scientific logic of RQ0, the general objective, SO1–SO5, RQ1–RQ5, and H1–H5 is frozen by this version. Exact numerical thresholds, probability levels, scenario ensembles, data splits, and final confirmatory decision rules remain subject to preregistration and evidence gates.

---

## 0. Evidence-use rule

The articles cited in this specification are used to establish **scientific relevance, mathematical legitimacy, engineering mechanisms, comparator legitimacy, and method appropriateness**. They are **not** used to claim that the thesis is novel.

```math
\boxed{
\text{Literature support}
\rightarrow
\text{justify the question / mechanism / method / comparator}
}
```

is distinct from

```math
\boxed{
\text{Novelty assessment}
\rightarrow
\text{separate reproducible novelty-search and boundary audit}.
}
```

A literature source can justify why a question is scientifically meaningful without demonstrating that nobody has asked it before.

For every externally sourced scientific statement in thesis prose, use an adjacent verified APA 7 citation. Thesis-derived mathematics, hypotheses, assumptions, and proposed constructs must instead be identified as `[D]`, `[H]`, `[A]`, or `[P]` under the reasoning protocol.

---

# 1. Scientific foundation of the research program

Critical infrastructures are interdependent systems whose failures can propagate across sectors, geography, and operational processes; interdependency analysis therefore requires explicit representation of mechanisms rather than isolated network descriptions (Rinaldi et al., 2001; Ouyang, 2014). Recent interdependent-infrastructure resilience synthesis further emphasizes dynamic performance evolution, temporal and geographic propagation, and multi-target resilience improvement (Tong et al., 2025). Coupled power–transportation systems provide a concrete physical realization of these issues because EV charging, charging infrastructure, mobility, and vehicle-to-grid services create bidirectional interactions between the electricity and transportation domains (Wang et al., 2026; Wen et al., 2025).

The thesis therefore uses the following scientific identity:

```math
\boxed{
\text{Power--Transportation System of Systems}
\quad\text{modeled as}\quad
\text{an interdependent complex dynamical system}.
}
```

The physical core is

```math
\boxed{P+T}
```

with information and organization represented as supporting layers:

```math
\boxed{\mathcal S=\{P,T,I,O\}}.
```

The literature supports treating network structure, governance, and information as distinct but interacting domains of infrastructure resilience. In particular, governance configuration affects infrastructure response capabilities and information can mediate the relationship between physical networks and governance (Helmrich et al., 2021). Cross-sector empirical work also shows that information sharing, ownership, coordination, institutional arrangements, and economic incentives affect how interdependency-related risks are managed in practice (Rydén Sonesson et al., 2021).

---

# 2. Overarching research question and general objective

## RQ0 — overarching research question

> **How can coupled Power–Transportation infrastructure be represented as an interdependent System of Systems and modeled as a spatiotemporal complex dynamical system to quantify the effects of causal interdependencies, information and organizational constraints, uncertainty-aware service maintainability and recovery, and the resilience–sustainability consequences of engineering interventions?**

### Why RQ0 is scientifically justified

Interdependent-infrastructure research has long established that cross-sector dependencies can generate cascading consequences that cannot be inferred from isolated infrastructures alone (Rinaldi et al., 2001; Ouyang, 2014). Recent reviews emphasize the need to understand dynamic performance evolution in both time and geography and to consider trade-offs among resilience-improvement objectives (Tong et al., 2025). Power–transportation coupling through EV charging and V2G provides an engineering setting in which power availability changes mobility options while mobile storage and charging decisions can in turn affect grid operation (Wang et al., 2026; Wen et al., 2025).

## General objective

> **To develop, implement, and validate an evidence-grounded mathematical framework that represents coupled Power–Transportation infrastructure as an interdependent System of Systems, models its spatiotemporal causal dynamics under informational and organizational constraints, quantifies resilience through uncertainty-aware viability and reachability, and evaluates the sustainability consequences of engineering interventions under uncertainty.**

The objective is therefore organized as

```math
\boxed{
\text{Structure}
\rightarrow
\text{Causal Interdependency}
\rightarrow
\text{Dynamics}
\rightarrow
\text{Knowledge and Feasible Action}
\rightarrow
\text{Resilience}
\rightarrow
\text{Intervention}
\rightarrow
\text{Sustainability Consequences}
\rightarrow
\text{Decision}.
}
```

---

# 3. SO1 / RQ1 / H1 — Dynamic causal interdependency

## SO1

> **Formally represent the coupled Power–Transportation System of Systems and determine the incremental explanatory or predictive value of evidence-supported dynamic causal interdependencies for spatiotemporal cascade, service-loss, and recovery trajectories.**

## RQ1

> **What incremental explanatory or predictive value does dynamic causal Power–Transportation coupling provide over independent and static-coupling representations for spatiotemporal cascade, service-loss, and recovery trajectories?**

## Scientific justification

Infrastructure interdependencies can create cross-system propagation pathways and cascading failures, which motivates explicit interdependency modeling rather than independent-system analysis (Rinaldi et al., 2001; Ouyang, 2014). Tong et al. (2025) identify temporal and geographic performance evolution as important dimensions of interdependent-infrastructure resilience analysis. In coupled power–transportation systems, EV charging and V2G create bidirectional power–mobility coupling whose strength can vary with system state and user behavior (Wang et al., 2026), while resilience planning studies demonstrate that charging infrastructure and mobile EV resources can materially affect coupled-system performance under contingencies (Wen et al., 2025).

These sources justify **testing dynamic causal coupling**. They do not establish beforehand that the dynamic model must outperform the simpler baselines.

## H1 — Dynamic causal interdependency hypothesis

> **H1:** Under matched Power–Transportation disturbances and initial conditions, an evidence-grounded dynamic causal coupling representation provides measurable incremental explanatory or predictive information for preregistered cascade, service-loss, spatial-propagation, and recovery outcomes relative to corresponding static-coupling and independent-system representations.

## Comparator architecture

```math
M_0=\text{independent }P+T,
```

```math
M_1=\text{static/algebraic }P\text{--}T\text{ coupling},
```

```math
M_2=\text{dynamic causal }P\text{--}T\text{ coupling}.
```

Primary confirmatory contrast:

```math
\boxed{M_2\overset{?}{>}M_1}
```

with `M0` retained as the uncoupled reference.

## Candidate primary response vector

```math
Z_1=
\begin{bmatrix}
T_C\\
N_{\rm fail}\\
L_{\rm service}\\
V_{\rm spatial}\\
T_{\rm recovery}
\end{bmatrix},
```

where `V_spatial` denotes a preregistered spatial-propagation quantity.

## Confirmatory form

```math
D\!\left(Z_1^{M_2},Z_1^{M_1}\right)\ge\delta_1,
```

where `D` and `\delta_1` must be fixed before confirmatory execution.

## Experiment

Use identical hazard realizations, initial states, service requirements, and exogenous conditions across `M0`, `M1`, and `M2`; change only the coupling representation required by the contrast.

## Falsification condition

H1 is not supported in the declared domain if the dynamic model fails to provide at least the preregistered meaningful incremental information relative to `M1` under the declared metric and scenario aggregation rule.

## Framework / thesis mapping

```text
Framework: Stages 1–3
Chapter 1: SO1 / RQ1 / H1
Chapter 2: infrastructure interdependency; P–T coupling; dynamic propagation
Chapter 3: Stages 1–3
Chapter 4.5: H1 experiment
Chapter 5.1: H1 results
Chapter 6: mechanistic interpretation
Chapter 7: answer RQ1 / adjudicate H1
```

---

# 4. SO2 / RQ2 / H2 — Information, organization, and feasible control

## SO2

> **Quantify how information availability and organizational constraints alter state knowledge, feasible control actions, response timing, and recovery under matched physical disturbances.**

## RQ2

> **How do information availability and organizational constraints modify estimated system state, feasible actions, response timing, and recovery under matched physical disturbance conditions?**

## Scientific justification

Infrastructure resilience depends not only on network topology but also on governance, authority, information flow, and the ability to coordinate action. Helmrich et al. (2021) show that physical network configuration and governance configuration are separate but coupled dimensions of resilient infrastructure and identify information as a critical mediator. Rydén Sonesson et al. (2021), using cross-sector document and interview evidence from transportation, energy, and telecommunications, identify information sharing, collaboration, risk ownership, institutional arrangements, and economic factors as mechanisms affecting management of interdependency-related risks. Cyber-physical power-system research likewise documents that communication dependencies affect monitoring, control, protection, cascading failure, and recovery processes (Islam et al., 2023).

These sources justify explicit information and organizational variables in the control architecture; they do not prescribe a specific estimator or controller for this thesis.

## H2 — Information–organization hypothesis

> **H2:** Under matched physical states and disturbances, changes in information availability and organizational conditions produce measurable differences in state-estimation quality, feasible control actions, response timing, recovery trajectories, and Stage-5 resilience outcomes.

## Nested comparison

```math
\mathscr N_0=P+T,
\qquad
\mathscr N_1=P+T+I,
\qquad
\mathscr N_2=P+T+I+O.
```

with

```math
\mathscr N_1-\mathscr N_0
=\text{information-layer effect},
```

```math
\mathscr N_2-\mathscr N_1
=\text{organizational-layer effect}.
```

## Candidate metrics

```math
Z_2=
\left(
\operatorname{RMSE}(\widehat Y,Y),
\Delta\mathcal U,
\tau_{\rm response},
L_{\rm service},
T_{\rm rec},
P_{\rm viable},
P_{\rm recover}
\right).
```

`\Delta\mathcal U` must be operationalized as a declared set-distance, action-availability, feasible-volume, or equivalent control-feasibility metric before confirmatory testing.

## Mechanistic chain

```math
Y
\rightarrow
 y
\rightarrow
\widehat Y
\rightarrow
(z_I,z_O)
\rightarrow
\mathcal U
\rightarrow
u
\rightarrow
Y^{+}.
```

## Experiment

Hold the physical initial condition, physical damage, and hazard realization fixed while perturbing only prespecified information and organizational conditions.

## Falsification condition

H2 is not supported if the prespecified information/organization contrasts fail to produce the minimum preregistered effect in the declared intermediate and downstream outcomes over the test domain.

## Framework / thesis mapping

```text
Framework: Stage 4, with downstream Stage-5 consequences
Chapter 1: SO2 / RQ2 / H2
Chapter 2: information, governance, organization, control
Chapter 3: Stage 4
Chapter 4.6: H2 experiment
Chapter 5.2: H2 results
Chapter 6: physical–informational–organizational interpretation
Chapter 7: answer RQ2 / adjudicate H2
```

---

# 5. SO3 / RQ3 / H3 — Uncertainty-aware viability and reachability resilience

## SO3

> **Determine whether uncertainty-aware viability and reach–avoid measures provide incremental prediction or decision information beyond conventional performance/recovery-curve metrics.**

## RQ3

> **Do uncertainty-aware viability and reach–avoid measures provide incremental decision-relevant information beyond conventional performance/recovery curves, and with what probabilistic confidence?**

## Scientific justification

Resilience curves are widely used to summarize infrastructure performance degradation and recovery through time, but their interpretation depends on the selected performance variable, target, normalization, and summary metric (Poulin & Kane, 2021). Viability theory addresses a different engineering question: whether a controlled system can remain within admissible state and control constraints. Doyen and De Lara (2010) formalize stochastic viability kernels and viable feedbacks under chance constraints. Vinod and Oishi (2021) formulate stochastic target-tube reachability for constrained systems with bounded control authority and show that stochastic viability and stochastic reach–avoid are contained within the same target-tube reachability framework.

Accordingly, performance curves remain the benchmark, while viability and reachability provide candidate prospective measures of **maintainability** and **recoverability under control and uncertainty**. The thesis must test whether these additional mathematical objects change prediction or engineering decisions; their superiority is not assumed.

## H3 — Viability–reachability incremental-information hypothesis

> **H3:** For the declared Power–Transportation test domain, the combined uncertainty-aware viability–reachability resilience object provides measurable incremental predictive or decision-relevant information about future service maintainability and acceptable recovery beyond prespecified conventional performance/recovery-curve metrics.

## Canonical Stage-5 resilience object

```math
\boxed{
\mathfrak R_T(t)
=
\left(
\mathcal V_{\alpha,T},
\mathcal R_{\beta,T},
\rho_{\mathcal V},
T_{\mathcal V},
T_{\rm rec},
P_{\rm viable},
P_{\rm recover}
\right).
}
```

### Viability

```math
\mathcal V_{\alpha,T}(t)
=
\left\{
y:
\exists\pi
\text{ such that }
\Pr^{\pi}
\left[
Y_\tau\in K(\tau),
\forall\tau\in[t,t+T]
\mid\mathcal I_t
\right]\ge\alpha
\right\}.
```

### Reach–avoid recovery

```math
\mathcal R_{\beta,T}(t)
=
\left\{
y:
\exists\pi
\text{ such that }
\Pr^{\pi}
\left[
\tau_{G_{\rm rec}}\le T,
Y_s\notin F\ \forall s<\tau_{G_{\rm rec}}
\mid\mathcal I_t
\right]\ge\beta
\right\}.
```

### Conventional benchmark

```math
Q(t)\rightarrow R_{\rm curve}.
```

## Required definitions before preregistration closes

```math
\boxed{
K,
\quad
G_{\rm rec},
\quad
F,
\quad
T,
\quad
\alpha,
\quad
\beta
}
```

must be defined from service requirements, physical limits, decision requirements, and justified uncertainty models — not chosen after observing confirmatory results.

## Incremental-information test

Let

```math
Q_{\rm conv}=\text{prespecified conventional performance/recovery predictors},
```

and

```math
Q_{\rm vrr}=Q_{\rm conv}\cup\mathfrak R_T.
```

Then test

```math
\boxed{
\operatorname{Skill}(Q_{\rm vrr})
-
\operatorname{Skill}(Q_{\rm conv})
\ge\delta_3.
}
```

The primary `Skill` measure must be preregistered. Candidate classes include future constraint-violation discrimination, calibration, warning lead time, recovery classification, or another engineering-decision metric supported before testing.

## Experiment

Construct matched states/scenarios that are similar under conventional current-performance measures but differ in viability/reachability quantities where possible, then test whether their future constraint satisfaction or recovery outcomes differ in the predicted direction.

## Falsification condition

If adding `\mathfrak R_T` fails to improve the preregistered predictive or decision metric by at least `\delta_3`, the added mathematical complexity is not supported for the tested application.

## Framework / thesis mapping

```text
Framework: Stage 5
Chapter 1: SO3 / RQ3 / H3
Chapter 2: resilience curves; viability; reachability; stochastic uncertainty
Chapter 3: Stage 5
Chapter 4.7: H3 experiment
Chapter 5.3: H3 results
Chapter 6: incremental-value interpretation and limits
Chapter 7: answer RQ3 / adjudicate H3
```

---

# 6. SO4 / RQ4 / H4 — Engineering intervention and sustainability consequences

## SO4

> **Evaluate resilience-informed engineering interventions by quantifying how they change coupled-system trajectories, Stage-5 resilience, and evidence-supported sustainability outcomes.**

## RQ4

> **How do resilience-informed engineering interventions modify coupled-system trajectories, maintainability and recovery, and the resulting accessibility, energy, carbon, and cost consequences?**

## Scientific justification

Infrastructure interventions can improve resilience while also changing cost, energy/material use, emissions, accessibility, and other lifecycle outcomes. Sánchez-Silva et al. (2025) argue that infrastructure planning should consider resilience and sustainability jointly because resilience measures may require scarce resources and can impose environmental costs. Liu et al. (2024) explicitly model trade-offs among infrastructure resilience, safety, economy, and embedded CO2e, showing why engineering interventions should not be evaluated through one objective alone. Zhu and Zhang (2026) similarly integrate lifecycle resilience and sustainability under multi-hazard conditions and show that resilience-oriented repair intensity can create cost and resource trade-offs. In the specific power–transportation domain, Wen et al. (2025) demonstrate that EV charging-infrastructure planning can be formulated as a resilience intervention under uncertainty.

These studies justify measuring sustainability consequences of resilience interventions. They do not imply that every resilience intervention must create a trade-off.

## H4 — Intervention-consequence hypothesis

> **H4:** Across the prespecified intervention and scenario set, engineering interventions that produce meaningful resilience improvement are not equivalent in their sustainability consequence vectors; at least two resilience-effective interventions produce materially different accessibility, energy, carbon, or cost consequences under the declared comparison rule.

This hypothesis tests **consequence heterogeneity**, not the assumption that every resilience improvement damages sustainability.

## Intervention mapping

```math
\boxed{
a_k
\rightarrow
\mathfrak M^{a_k}
\rightarrow
Y^{a_k}(x,t)
\rightarrow
\left(
\Delta\mathfrak R^{a_k},
\Delta\mathbf J_{\rm sus}^{a_k}
\right).
}
```

with the core sustainability vector

```math
\boxed{
\mathbf J_{\rm sus}
=
\begin{bmatrix}
J_{\rm access}\\
J_{\rm energy}\\
J_{\rm carbon}\\
J_{\rm cost}
\end{bmatrix}.
}
```

Additional sustainability outcomes may be added only if their causal mechanism, data support, units, and validation path are established before confirmatory use.

## Resilience-effective intervention set

Let

```math
\mathcal A_R^{+}
=
\left\{
a_k\in\mathcal A:
\Delta\mathcal M_R(a_k)\ge\delta_R
\right\},
```

where `\mathcal M_R` is a preregistered scalar decision functional derived from `\mathfrak R_T` for the specific intervention comparison.

For two resilience-effective interventions `a_i,a_j\in\mathcal A_R^{+}`, test

```math
D_J
\left(
\Delta\mathbf J_{\rm sus}^{a_i},
\Delta\mathbf J_{\rm sus}^{a_j}
\right)
\ge\delta_4.
```

The sustainability distance or decision rule `D_J` must be fixed before confirmatory execution.

## Supporting diagnostic — interface criticality

Viability/reachability-sensitive interface criticality remains scientifically useful as a **Stage-6 diagnostic for proposing intervention targets**, but it is no longer the primary H4 claim.

A supporting chain may be

```math
\Delta\mathfrak d_e
\rightarrow
\Delta F
\rightarrow
\Delta\mathfrak R_T
\rightarrow
\text{candidate intervention target}.
```

Any claim that interface criticality improves targeting must be separately tested against structural/flow baselines before being promoted to a confirmatory conclusion.

## Falsification condition

H4 is not supported if resilience-effective interventions are indistinguishable under the preregistered sustainability consequence metric within the tested domain, or if the intervention set does not contain enough qualified resilience-effective alternatives to make the comparison.

## Framework / thesis mapping

```text
Framework: Stage 6
Chapter 1: SO4 / RQ4 / H4
Chapter 2: resilience interventions; sustainability consequences; trade-offs
Chapter 3: Stage 6
Chapter 4.8: H4 intervention experiment
Chapter 5.4: H4 results
Chapter 6: synergy / trade-off / burden-shifting interpretation
Chapter 7: answer RQ4 / adjudicate H4
```

---

# 7. SO5 / RQ5 / H5 — Joint resilience–sustainability engineering decision

## SO5

> **Determine whether joint resilience–sustainability evaluation under uncertainty changes the admissible or nondominated engineering intervention set relative to resilience-only evaluation.**

## RQ5

> **Does joint resilience–sustainability evaluation under uncertainty materially change the feasible, nondominated, or preferred engineering intervention set relative to resilience-only evaluation?**

## Scientific justification

Infrastructure decision-making is inherently multi-objective when physical resilience, lifecycle cost, environmental consequences, and service outcomes interact. Sánchez-Silva et al. (2025) identify multicriteria lifecycle evaluation, governance, and uncertainty management as central challenges for resilient and sustainable infrastructure. Liu et al. (2024) formulate infrastructure development as a decision problem involving resilience, safety, economic performance, and CO2e consequences. Zhu and Zhang (2026) likewise show that integrated resilience–sustainability evaluation can alter the assessment of repair and investment strategies. Robust planning of coupled power–transportation charging infrastructure also demonstrates that uncertainty can materially affect intervention design and cost trade-offs (Wen et al., 2025).

These sources justify a joint decision formulation. They do not establish in advance that the joint decision set must differ from the resilience-only set.

## H5 — Joint-decision hypothesis

> **H5:** Under the declared uncertainty domain and intervention set, incorporating sustainability consequences into resilience-based engineering evaluation produces a materially different admissible or nondominated intervention set, or materially changes decision regret, relative to resilience-only evaluation.

## Decision sets

Define a resilience-only decision set

```math
\mathcal A_R^{\star}
```

and a joint resilience–sustainability set

```math
\mathcal A_{R,S}^{\star}.
```

The exact construction — constrained optimum, Pareto set, satisficing set, or robust nondominated set — must be fixed in the H5 preregistration.

## Candidate set-change metric

For finite intervention sets, one admissible metric is Jaccard distance:

```math
D_{\mathcal A}
=
1-
\frac{
\left|\mathcal A_R^{\star}\cap\mathcal A_{R,S}^{\star}\right|
}{
\left|\mathcal A_R^{\star}\cup\mathcal A_{R,S}^{\star}\right|
}.
```

A confirmatory form is

```math
D_{\mathcal A}\ge\delta_5.
```

Alternatively, a preregistered regret or dominance-change metric may be used if it better matches the decision structure. The metric must not be changed after viewing confirmatory results because a different metric produces a more favorable conclusion.

## Deep uncertainty rule

If scenario probabilities are not scientifically defensible, scenario frequencies must not be interpreted as probabilities. Use nonprobabilistic robustness, satisficing, regret, or scenario-coverage metrics instead.

## Supporting extension — adaptive transformation

Adaptive trigger-based pathways remain a **secondary Stage-7 extension**, not the primary H5 claim. They may be studied only if the data, computational budget, and decision problem require sequential adaptation after the primary joint-decision question is closed.

## Falsification condition

H5 is not supported if the resilience-only and joint resilience–sustainability decision sets are not materially different under the preregistered set/regret metric, or if sustainability information does not change the declared engineering decision within the tested uncertainty domain.

## Framework / thesis mapping

```text
Framework: Stage 7
Chapter 1: SO5 / RQ5 / H5
Chapter 2: resilient+sustainable decision-making; uncertainty; robust/multicriteria methods
Chapter 3: Stage 7
Chapter 4.9: H5 decision experiment
Chapter 5.5: H5 results
Chapter 6: engineering-decision implications and uncertainty
Chapter 7: answer RQ5 / adjudicate H5
```

---

# 8. Frozen v2 traceability matrix

| Research object | Objective | Research question | Primary hypothesis | Framework stage(s) | Primary comparison |
|---|---|---|---|---|---|
| **SO1 / RQ1 / H1** | dynamic causal interdependency | incremental value of dynamic causal coupling | `M2` adds measurable information beyond `M1`/`M0` | 1–3 | dynamic vs static vs independent |
| **SO2 / RQ2 / H2** | information + organization | effect on knowledge, feasible action, response and recovery | matched physical disturbances differ under `I/O` conditions | 4 → 5 | `P+T` vs `P+T+I` vs `P+T+I+O` |
| **SO3 / RQ3 / H3** | viability + reachability + probability | incremental value beyond resilience curves | `\mathfrak R_T` adds decision/predictive information | 5 | `R_curve` vs `R_curve + \mathfrak R_T` |
| **SO4 / RQ4 / H4** | intervention consequences | resilience and sustainability effects of interventions | resilience-effective interventions have materially different sustainability consequence vectors | 6 | matched qualified interventions |
| **SO5 / RQ5 / H5** | engineering decision | effect of joint R–S evaluation | joint evaluation changes set/regret relative to resilience-only | 7 | `\mathcal A_R^\star` vs `\mathcal A_{R,S}^\star` |

The required thesis-wide chain is now

```math
\boxed{
RQ_i
\rightarrow
SO_i
\rightarrow
H_i
\rightarrow
\text{mechanism}
\rightarrow
\text{metric}
\rightarrow
\text{baseline}
\rightarrow
\text{experiment}
\rightarrow
\text{uncertainty}
\rightarrow
\text{falsification}
\rightarrow
\text{result}
\rightarrow
\text{engineering conclusion}.
}
```

---

# 9. What is frozen and what remains open

## Frozen by v2.0

- overarching RQ0;
- general objective;
- SO1–SO5;
- RQ1–RQ5;
- primary scientific logic of H1–H5;
- assignment of H1–H5 to the seven-stage framework;
- role of performance curves as the H3 benchmark;
- role of viability + reachability + probability as the Stage-5 resilience core;
- reclassification of interface criticality as a Stage-6 supporting diagnostic;
- reclassification of adaptive transformation as a Stage-7 supporting extension;
- requirement that H4 evaluate sustainability consequences of resilience-effective interventions;
- requirement that H5 compare resilience-only with joint resilience–sustainability decision logic.

## Not yet frozen

- `\delta_1,\ldots,\delta_5`;
- exact `\alpha,\beta,T`;
- final definitions of `K`, `G_{\rm rec}`, and `F`;
- final primary H3 skill metric;
- final H4 sustainability distance/decision metric;
- final H5 set-distance/regret metric;
- H3–H5 scenario ensembles;
- H3–H5 data sources and train/validation/test partitioning;
- final probability distributions where uncertainty is probabilistic;
- final confirmatory aggregation rules.

Those items must be frozen through hypothesis-specific preregistration after data/evidence qualification.

---

# 10. Citation-to-claim discipline for this specification

The role of each core source is explicit:

| Source | What it justifies here | What it does **not** establish |
|---|---|---|
| Rinaldi et al. (2001) | infrastructure interdependency as a systems problem; cascading cross-infrastructure effects | thesis novelty or a specific P–T equation |
| Ouyang (2014) | multiple modeling approaches and importance of interdependent-system modeling for resilience | superiority of our model |
| Tong et al. (2025) | current interdependent-infrastructure focus on dynamic, temporal/geographic performance and multi-target improvement | that our framework is unique |
| Wang et al. (2026) | bidirectional/behavior-dependent P–T interdependency through EV charging/V2G | general validity outside its study domain |
| Wen et al. (2025) | resilience intervention/planning in coupled power–transportation systems under uncertainty | that our intervention set is optimal |
| Helmrich et al. (2021) | network + governance dimensions; information as mediator | a calibrated organizational model |
| Rydén Sonesson et al. (2021) | empirical cross-sector governance, coordination, information-sharing mechanisms | universal organizational parameters |
| Islam et al. (2023) | cyber/communication interdependency affecting monitoring/control/cascades in power systems | direct parameter transfer to P–T |
| Poulin & Kane (2021) | legitimacy and limitations of resilience curves as benchmark metrics | inadequacy of every curve-based analysis |
| Doyen & De Lara (2010) | mathematical legitimacy of stochastic viability under chance constraints | infrastructure-specific validation |
| Vinod & Oishi (2021) | stochastic target-tube reachability and relation to viability/reach–avoid | infrastructure-specific superiority |
| Sánchez-Silva et al. (2025) | need for integrated resilience–sustainability lifecycle thinking | our exact sustainability vector |
| Liu et al. (2024) | measurable infrastructure trade-offs among resilience, economy, safety, and CO2e | transfer of their numerical results to our system |
| Zhu & Zhang (2026) | integrated lifecycle resilience–sustainability decision logic under hazards | transferability of tunnel results to P–T |

---

# 11. References — APA 7

Doyen, L., & De Lara, M. (2010). Stochastic viability and dynamic programming. *Systems & Control Letters, 59*(10), 629–634. https://doi.org/10.1016/j.sysconle.2010.07.008

Helmrich, A., Markolf, S., Li, R., Carvalhaes, T., Kim, Y., Bondank, E., Natarajan, M., Ahmad, N., & Chester, M. (2021). Centralization and decentralization for resilient infrastructure and complexity. *Environmental Research: Infrastructure and Sustainability, 1*(2), 021001. https://doi.org/10.1088/2634-4505/ac0a4f

Islam, M. Z., Lin, Y., Vokkarane, V. M., & Venkataramanan, V. (2023). Cyber-physical cascading failure and resilience of power grid: A comprehensive review. *Frontiers in Energy Research, 11*, 1095303. https://doi.org/10.3389/fenrg.2023.1095303

Liu, M., Lu, D.-G., & Faber, M. H. (2024). On CO2 efficiency and trade-offs between sustainability, safety, economy and resilience in infrastructure developments. *Sustainable Cities and Society, 113*, 105647. https://doi.org/10.1016/j.scs.2024.105647

Ouyang, M. (2014). Review on modeling and simulation of interdependent critical infrastructure systems. *Reliability Engineering & System Safety, 121*, 43–60. https://doi.org/10.1016/j.ress.2013.06.040

Poulin, C., & Kane, M. B. (2021). Infrastructure resilience curves: Performance measures and summary metrics. *Reliability Engineering & System Safety, 216*, 107926. https://doi.org/10.1016/j.ress.2021.107926

Rinaldi, S. M., Peerenboom, J. P., & Kelly, T. K. (2001). Identifying, understanding, and analyzing critical infrastructure interdependencies. *IEEE Control Systems Magazine, 21*(6), 11–25. https://doi.org/10.1109/37.969131

Rydén Sonesson, T., Johansson, J., & Cedergren, A. (2021). Governance and interdependencies of critical infrastructures: Exploring mechanisms for cross-sector resilience. *Safety Science, 142*, 105383. https://doi.org/10.1016/j.ssci.2021.105383

Sánchez-Silva, M., Gardoni, P., Val, D. V., Yang, D. Y., Frangopol, D. M., Limongelli, M. P., Honfi, D., Acuña, N., & Straub, D. (2025). Moving toward resilience and sustainability in the built environment. *Structural Safety, 113*, 102449. https://doi.org/10.1016/j.strusafe.2024.102449

Tong, W., Li, H. X., Nasirzadeh, F., Yao, F., & Ji, Y. (2025). Resilience of interdependent infrastructure networks: Review and future directions. *International Journal of Critical Infrastructure Protection, 51*, 100793. https://doi.org/10.1016/j.ijcip.2025.100793

Vinod, A. P., & Oishi, M. M. K. (2021). Stochastic reachability of a target tube: Theory and computation. *Automatica, 125*, 109458. https://doi.org/10.1016/j.automatica.2020.109458

Wang, S., Lu, Q.-C., Liu, L., Xu, P.-C., Wang, R., & Zhang, L. (2026). Interdependency analysis of coupled power and transportation networks considering the charging decision preferences of EV drivers. *Reliability Engineering & System Safety, 268*, 112005. https://doi.org/10.1016/j.ress.2025.112005

Wen, J., Gan, W., Chu, C.-C., Jiang, L., & Luo, J. (2025). Robust resilience enhancement by EV charging infrastructure planning in coupled power distribution and transportation systems. *IEEE Transactions on Smart Grid, 16*(1), 491–504. https://doi.org/10.1109/TSG.2024.3390657

Zhu, Y., & Zhang, Q.-B. (2026). Lifecycle resilience and sustainability trade-offs for underground infrastructure under multi-hazard scenarios. *Reliability Engineering & System Safety, 267*, 111797. https://doi.org/10.1016/j.ress.2025.111797

---

# 12. Next controlled gate

With the v2 RQ–SO–H logic frozen, the next governance sequence is

```math
\boxed{
\text{RQ--SO--H v2}
\rightarrow
\text{thesis traceability synchronization}
\rightarrow
\text{master outline synchronization}
\rightarrow
\text{ASU master-specification synchronization}
\rightarrow
\text{abstract synchronization}
\rightarrow
\text{H3--H5 preregistration}.
}
```

No H3–H5 confirmatory result should be generated before its hypothesis-specific metric, baseline, scenario domain, uncertainty model, threshold, and falsification rule are frozen.