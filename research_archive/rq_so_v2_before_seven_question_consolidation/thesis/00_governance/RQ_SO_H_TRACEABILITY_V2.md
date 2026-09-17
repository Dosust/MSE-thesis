# RQ–SO–H Traceability Matrix — v2.0

**Status:** CURRENT THESIS TRACEABILITY CONTROL  
**Effective date:** 2026-09-16  
**Scientific authority:** `../../project/CANONICAL_RQ_SO_HYPOTHESES_V2.md`  
**Framework authority:** `../../project/CANONICAL_7_STAGE_FRAMEWORK_V2.md`  
**Reasoning authority:** `../../project/RESEARCH_REASONING_PROTOCOL.md` v1.2  
**Citation rule:** every externally sourced scientific claim must carry an adjacent verified APA 7 author–date citation.

> **Evidence-use rule:** the literature anchors below justify the scientific questions, mechanisms, comparator choices, and engineering relevance. They do **not** constitute the thesis novelty demonstration. Novelty remains a separate reproducible audit.

---

## Governing chain

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

A broken link is a thesis-control defect.

---

## Overarching research logic

### RQ0

> How can coupled Power–Transportation infrastructure be represented as an interdependent System of Systems and modeled as a spatiotemporal complex dynamical system to quantify the effects of causal interdependencies, information and organizational constraints, uncertainty-aware service maintainability and recovery, and the resilience–sustainability consequences of engineering interventions?

### General objective

> To develop, implement, and validate an evidence-grounded mathematical framework that represents coupled Power–Transportation infrastructure as an interdependent System of Systems, models its spatiotemporal causal dynamics under informational and organizational constraints, quantifies resilience through uncertainty-aware viability and reachability, and evaluates the sustainability consequences of engineering interventions under uncertainty.

Interdependent-infrastructure literature supports explicit treatment of cross-system coupling, cascading behavior, dynamic propagation, and multiple modeling perspectives (Rinaldi et al., 2001; Ouyang, 2014; Tong et al., 2025). Coupled power–transportation studies further establish that EV charging, charging infrastructure, mobility, and V2G create bidirectional operational interactions between the two sectors (Wang et al., 2026; Wen et al., 2025).

---

## Canonical matrix

| ID | Specific objective | Research question | Primary hypothesis | Primary metric / decision object | Experiment / comparator | Framework | Thesis locations | Evidence anchors |
|---|---|---|---|---|---|---|---|---|
| **SO1 / RQ1 / H1** | Represent P–T SoS and test incremental value of dynamic causal interdependency | What incremental explanatory/predictive value does dynamic causal P–T coupling provide over independent/static coupling for cascade, service-loss and recovery trajectories? | `M2` provides measurable incremental information relative to `M1`/`M0` under matched conditions | preregistered trajectory/service/spatial/recovery difference `D(Z_1^{M2},Z_1^{M1})` | `M0` independent vs `M1` static vs `M2` dynamic causal | 1–3 | Ch.1; Ch.3; 4.5; 5.1; Ch.6; Ch.7 | Cross-infrastructure dependencies can propagate failures and require explicit modeling (Rinaldi et al., 2001; Ouyang, 2014); temporal/geographic evolution matters for interdependent resilience (Tong et al., 2025); P–T coupling is state/behavior dependent through EV charging/V2G (Wang et al., 2026). |
| **SO2 / RQ2 / H2** | Quantify effects of information and organization on state knowledge, feasible control, timing and recovery | How do information availability and organizational constraints modify state estimation, feasible actions, response timing and recovery under matched physical disturbance? | Matched physical conditions produce measurably different control/recovery outcomes when `I/O` conditions differ | estimation error, `\Delta\mathcal U`, response time, service loss, `T_rec`, `P_viable`, `P_recover` | `P+T` vs `P+T+I` vs `P+T+I+O` | 4 → 5 | Ch.1; Ch.3; 4.6; 5.2; Ch.6; Ch.7 | Network and governance configurations jointly affect resilience and information is a mediator (Helmrich et al., 2021); empirical cross-sector evidence identifies information-sharing, collaboration, ownership and institutional mechanisms (Rydén Sonesson et al., 2021); communication dependencies affect monitoring/control and cascading processes (Islam et al., 2023). |
| **SO3 / RQ3 / H3** | Test incremental value of uncertainty-aware viability and reachability beyond conventional resilience curves | Do viability and reach–avoid measures add decision-relevant information beyond performance/recovery curves, and with what confidence? | `\mathfrak R_T` adds preregistered predictive/decision skill beyond conventional curve metrics | `\Delta Skill = Skill(Q_conv\cup\mathfrak R_T)-Skill(Q_conv)` | conventional performance/recovery predictors vs conventional + `\mathfrak R_T` | 5 | Ch.1; Ch.2; Ch.3; 4.7; 5.3; Ch.6; Ch.7 | Resilience curves are established but depend on performance/target/summary definitions (Poulin & Kane, 2021); stochastic viability formalizes constraint satisfaction under uncertainty (Doyen & De Lara, 2010); stochastic target-tube reachability subsumes viability and reach–avoid problems (Vinod & Oishi, 2021). |
| **SO4 / RQ4 / H4** | Quantify resilience and sustainability consequences of engineering interventions | How do resilience-informed interventions change trajectories, maintainability/recovery and accessibility, energy, carbon and cost outcomes? | Resilience-effective interventions are not equivalent in their sustainability consequence vectors under the declared comparison rule | `\Delta\mathfrak R`, `\Delta\mathbf J_sus`, and preregistered consequence-distance `D_J` | qualified interventions under matched scenarios/budgets | 6 | Ch.1; Ch.2; Ch.3; 4.8; 5.4; Ch.6; Ch.7 | Resilience and sustainability can involve resource/environmental trade-offs (Sánchez-Silva et al., 2025); infrastructure decisions can produce measurable resilience/economy/CO2e trade-offs (Liu et al., 2024); lifecycle resilience–sustainability evaluation can differentiate restoration strategies (Zhu & Zhang, 2026); P–T charging infrastructure is a valid resilience intervention domain (Wen et al., 2025). |
| **SO5 / RQ5 / H5** | Determine whether joint resilience–sustainability evaluation changes engineering decisions under uncertainty | Does joint R–S evaluation materially change the feasible/nondominated/preferred intervention set relative to resilience-only evaluation? | `\mathcal A_{R,S}^{\star}` differs materially from `\mathcal A_R^{\star}` or changes preregistered regret | set-distance, dominance-change or regret metric fixed before testing | resilience-only vs joint resilience–sustainability decision model | 7 | Ch.1; Ch.2; Ch.3; 4.9; 5.5; Ch.6; Ch.7 | Resilient+sustainable infrastructure requires multicriteria lifecycle and uncertainty-aware decision thinking (Sánchez-Silva et al., 2025); resilience, economy and carbon consequences can change strategy evaluation (Liu et al., 2024); integrated lifecycle analysis can alter preferred repair/investment choices (Zhu & Zhang, 2026); robust P–T planning shows intervention decisions depend on uncertainty (Wen et al., 2025). |

---

## Stage-5 object required by H2–H5

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

The benchmark remains

```math
Q(t)\rightarrow R_{\rm curve}.
```

This is a comparator architecture, not a declaration that `\mathfrak R_T` is superior.

---

## Supporting analyses that are no longer primary H4/H5 claims

### Interface criticality

Interface criticality remains a Stage-6 diagnostic:

```math
\Delta\mathfrak d_e
\rightarrow
\Delta F
\rightarrow
\Delta\mathfrak R_T
\rightarrow
\text{candidate intervention target}.
```

It can become a confirmatory sub-study only after its own baseline, metric, intervention budget, threshold, and falsification rule are preregistered.

### Adaptive transformation pathways

Adaptive trigger-based pathways remain a Stage-7 extension. They are studied only if sequential adaptation is required by the decision problem and supported by data/computational resources.

---

## Preregistration defects that remain open

The RQ/SO/H **logic is frozen**, but confirmatory H3–H5 execution remains blocked until the following are fixed a priori:

```text
H3: K, G_rec, F, T, alpha, beta, uncertainty model, primary Skill metric, delta_3
H4: intervention set, resilience-effective criterion, sustainability accounting boundary, D_J, delta_4
H5: construction of A_R* and A_R,S*, uncertainty treatment, set/regret metric, delta_5
```

For probabilistic quantities, probability distributions require evidentiary support. If such support is absent, use deterministic, interval, possibilistic, or nonprobabilistic robustness representations instead of inventing probabilities.

---

## Results and conclusion gate

Every future result must map backward and forward:

```math
\boxed{
\text{method}
\leftarrow
H_i
\leftarrow
RQ_i
\qquad\text{and}\qquad
H_i
\rightarrow
\text{result}
\rightarrow
\text{qualified conclusion}.
}
```

No Chapter-7 conclusion may exceed the evidence, experiment, uncertainty, or validation domain of its corresponding hypothesis.

---

## References

Full APA 7 references and source-role notes are maintained in `../../project/CANONICAL_RQ_SO_HYPOTHESES_V2.md`. This governance matrix deliberately uses the same author–date citations so that source support remains visible adjacent to the scientific object it justifies.