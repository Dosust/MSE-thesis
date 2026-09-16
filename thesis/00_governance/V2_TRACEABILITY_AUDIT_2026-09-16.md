# v2.0 Traceability Audit — Research Questions → Objectives → Hypotheses → Stage-5 Metrics → Experiments → Thesis Chapters

**Status:** AUDIT COMPLETE / SYNCHRONIZATION REQUIRED  
**Audit date:** 2026-09-16  
**Framework authority:** `../../project/CANONICAL_7_STAGE_FRAMEWORK_V2.md`  
**Reasoning authority:** `../../project/RESEARCH_REASONING_PROTOCOL.md` v1.2  
**Purpose:** determine whether the thesis research questions, objectives, hypotheses, resilience metrics, experiments, and chapter structure remain one-to-one traceable after adoption of framework v2.0.

> **Change-control rule:** this audit identifies required revisions. It does not silently overwrite the frozen hypothesis architecture in `../../project/RESEARCH_HYPOTHESES.md`. Any H3–H5 change must be made through an explicit versioned hypothesis update before confirmatory execution.

---

## 1. Audit criterion

The required chain is

```math
\boxed{
\text{Research gap}
\rightarrow
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
\text{experiment}
\rightarrow
\text{result}
\rightarrow
\text{chapter}
\rightarrow
\text{engineering conclusion}.
}
```

A chain fails if any scientific object has no upstream justification or no downstream test.

All externally sourced scientific claims in this audit and all subsequent thesis text must use adjacent APA 7 author–date citations under `RESEARCH_REASONING_PROTOCOL.md` v1.2.

---

## 2. Literature-grounded basis for the v2 audit

Performance/recovery curves remain a major conventional language for infrastructure resilience and are useful for summarizing degradation and recovery, but their interpretation depends strongly on the chosen performance measure, target, and summary metric (Poulin & Kane, 2021). Tong et al. (2025), reviewing 101 interdependent-infrastructure-resilience studies, identify dynamic temporal–geographic performance evolution, dynamic assessment, and trade-offs among improvement targets as important future directions. Stochastic target-tube reachability provides a mathematical framework for maximizing the probability that a controlled stochastic system remains within time-varying state constraints, and it contains stochastic viability and stochastic reach–avoid problems as special cases (Vinod & Oishi, 2021).

These sources justify **testing** a viability–reachability–probability resilience formulation against conventional performance-based assessment; they do not justify assuming its superiority in advance.

Information and governance also require explicit treatment rather than being collapsed into physical topology alone. Infrastructure resilience can depend on governance configuration and information mediation (Helmrich et al., 2021), while cross-sector resilience practice is shaped by information sharing, ownership, coordination, institutional arrangements, and other governance mechanisms (Rydén Sonesson et al., 2021).

---

# 3. Current repository audit

| Object | Current state | v2.0 status | Audit decision |
|---|---|---|---|
| Seven-stage framework | `CANONICAL_7_STAGE_FRAMEWORK_V2.md` | viability + reachability + probability integrated | **PASS** |
| Reasoning protocol | v1.1 was citation-general and v1-framework-specific | updated to v1.2 with mandatory APA 7 and v2 chain | **PASS after revision** |
| Research objectives | no single current canonical SO1–SO5 file located in governance | objectives are required for RQ→H traceability | **DEFECT — canonical objectives required** |
| RQ/H traceability | current file maps RQ1–RQ5 directly to old H1–H5 | missing explicit objectives; H3–H5 partly conflict with v2 | **REVISION REQUIRED** |
| H1 | dynamic causal coupling vs independent/static | fully compatible with Stages 1–3 | **PASS** |
| H2 | information/organization alters feasible response/recovery | compatible with Stage 4 | **PASS with notation synchronization** |
| H3 | controlled viability only | Stage 5 now requires viability + reachability + probability and performance-curve benchmark | **MATERIAL REVISION REQUIRED** |
| H4 | viability-sensitive interface ranking | v2 Stage 6 is intervention → resilience + sustainability consequences | **RECLASSIFY as supporting diagnostic/subhypothesis** |
| H5 | adaptive transformation vs fixed pathway | v2 Stage 7 centers engineering decision under joint resilience–sustainability evaluation | **MATERIAL REVISION REQUIRED** |
| Master outline Ch. 3 | still uses v1 stage labels | inconsistent with v2 labels | **REVISION REQUIRED** |
| Master outline Ch. 4 | H3 viability; H4 interface criticality; H5 adaptive transformation | inconsistent with proposed v2 primary tests | **REVISION REQUIRED** |
| Master specification | scientific architecture still says viability → transformation diagnosis → pathways | not synchronized to v2 | **REVISION REQUIRED** |
| Abstract | still describes resilience primarily through controlled viability | incomplete relative to v2 remain/return/confidence core | **TARGETED REVISION REQUIRED** |

---

# 4. Proposed v2 general objective

> **To develop, implement, and validate an evidence-grounded mathematical framework that represents coupled Power–Transportation infrastructure as an interdependent System of Systems, models its spatiotemporal causal dynamics under informational and organizational constraints, quantifies resilience through uncertainty-aware service maintainability and recovery, and evaluates the sustainability consequences of engineering interventions under uncertainty.**

This objective preserves

```math
\boxed{
\text{SoS architecture}
\rightarrow
\text{causal dynamics}
\rightarrow
\text{resilience}
\rightarrow
\text{intervention}
\rightarrow
\text{sustainability consequences}
\rightarrow
\text{decision}.
}
```

---

# 5. Proposed v2 specific objectives, questions, and hypotheses

## SO1 / RQ1 / H1 — Dynamic causal interdependency

### SO1
Formally represent the coupled Power–Transportation System of Systems and determine the incremental explanatory or predictive value of evidence-supported dynamic causal interdependencies for spatiotemporal cascade, service-loss, and recovery trajectories.

### RQ1
> **What incremental explanatory or predictive value does dynamic causal Power–Transportation coupling provide over independent and static-coupling representations for spatiotemporal cascade, service-loss, and recovery trajectories?**

### H1
> **H1:** Explicit dynamic causal Power–Transportation coupling provides measurable incremental explanatory or predictive value over corresponding static-coupling and independent-system representations for preregistered cascade, service-loss, and recovery outcomes.

### Primary comparison

```math
M_0=\text{independent},
\qquad
M_1=\text{static coupling},
\qquad
M_2=\text{dynamic causal coupling},
```

with the primary confirmatory contrast

```math
\boxed{M_2\overset{?}{>}M_1}
```

and $M_0$ retained as the uncoupled baseline.

### Experiment
Matched disturbances and initial conditions across $M_0,M_1,M_2$; compare preregistered cascade, service-loss, spatial-propagation, and recovery outcomes.

### Thesis mapping

```text
Chapter 1: RQ1 / SO1 / H1
Chapter 3: Stages 1–3
Chapter 4.5: H1 experiment
Chapter 5.1: H1 results
Chapter 6: mechanistic interpretation
Chapter 7: answer RQ1 and adjudicate H1
```

---

## SO2 / RQ2 / H2 — Information and organization

### SO2
Quantify how information availability and organizational constraints alter state knowledge, feasible control actions, response timing, and recovery under matched physical disturbances.

### RQ2
> **How do information availability and organizational constraints modify estimated system state, feasible actions, response timing, and recovery under matched physical disturbance conditions?**

### H2
> **H2:** Under matched physical initial conditions and disturbances, changes in information availability and organizational conditions produce measurable differences in feasible controls, response timing, recovery trajectories, and resilience outcomes.

### Nested experiment

```math
\mathscr N_0=P+T,
\qquad
\mathscr N_1=P+T+I,
\qquad
\mathscr N_2=P+T+I+O.
```

Primary intermediate outcomes include estimation error, feasible-control-set change, response delay, and action availability; downstream outcomes include service loss, maintainability, recovery, and recovery probability.

### Thesis mapping

```text
Chapter 1: RQ2 / SO2 / H2
Chapter 3: Stage 4
Chapter 4.6: H2 experiment
Chapter 5.2: H2 results
Chapter 6: physical–organizational interpretation
Chapter 7: answer RQ2 and adjudicate H2
```

---

## SO3 / RQ3 / H3 — Uncertainty-aware viability and reachability resilience

### SO3
Determine whether uncertainty-aware viability and reach–avoid measures provide incremental prediction or decision information beyond conventional performance/recovery-curve metrics.

### RQ3
> **Do uncertainty-aware viability and reach–avoid measures provide incremental decision-relevant information beyond conventional performance/recovery curves, and with what probabilistic confidence?**

### H3
> **H3:** The combined viability–reachability resilience object provides measurable incremental predictive or decision-relevant information on service maintainability and recovery beyond prespecified conventional performance/recovery-curve metrics.

The mathematical basis is consistent with stochastic reachability theory, where target-tube reachability contains stochastic viability and stochastic reach–avoid formulations as special cases (Vinod & Oishi, 2021). Performance curves remain the benchmark rather than being discarded (Poulin & Kane, 2021).

### Canonical Stage-5 resilience object

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

### Conventional comparator

```math
\boxed{Q(t)\rightarrow R_{\rm curve}.}
```

### Required Stage-5 metrics

| Metric | Engineering meaning | Confirmatory status |
|---|---|---|
| $\mathcal V_{\alpha,T}$ | states from which acceptable service can be maintained over horizon $T$ with declared confidence $\alpha$ | core |
| $\mathcal R_{\beta,T}$ | states from which acceptable recovery can be reached while avoiding unacceptable states with declared confidence $\beta$ | core |
| $\rho_{\mathcal V}$ | proximity to viability-boundary loss | secondary/core diagnostic |
| $T_{\mathcal V}$ | time to loss of maintainability | core temporal diagnostic |
| $T_{\rm rec}$ | recovery time | benchmark-compatible diagnostic |
| $P_{\rm viable}$ | probability of maintaining acceptable operation under declared model/policy | core uncertainty diagnostic |
| $P_{\rm recover}$ | probability of acceptable recovery under declared model/policy | core uncertainty diagnostic |
| $R_{\rm curve}$ | conventional degradation/recovery representation | benchmark |

The exact probability model, threshold values $\alpha,\beta$, horizon $T$, acceptable set $K$, recovery target $G_{\rm rec}$, failure set $F$, and incremental-skill metric must be preregistered before confirmatory H3 execution.

### Experiment
Use matched states/scenarios and compare:

```math
\text{conventional performance/recovery predictors}
```

against

```math
\text{conventional predictors}
+
\mathfrak R_T.
```

Possible preregistered decision metrics include future-constraint-violation discrimination, calibration, warning lead time, intervention classification, or another decision-relevant metric justified before testing. No metric is selected retrospectively because it favors the proposed formulation.

### Thesis mapping

```text
Chapter 1: RQ3 / SO3 / H3
Chapter 2: performance curves; viability; reachability; uncertainty
Chapter 3: Stage 5
Chapter 4.7: H3 experiment
Chapter 5.3: H3 results
Chapter 6: incremental-value interpretation
Chapter 7: answer RQ3 and adjudicate H3
```

---

## SO4 / RQ4 / H4 — Intervention and sustainability consequences

### SO4
Formulate resilience-informed engineering interventions and quantify their effects on coupled-system trajectories, resilience, accessibility, operational energy use, carbon emissions, cost, and other outcomes only where causal mechanisms and data support inclusion.

### RQ4
> **How do resilience-informed engineering interventions alter coupled-system trajectories and thereby affect resilience, accessibility, operational energy use, carbon emissions, cost, and other evidence-supported sustainability outcomes?**

### H4
> **H4:** Resilience-improving interventions do not necessarily improve all sustainability outcomes simultaneously; tested interventions can produce measurable synergies, trade-offs, or burden shifting across evidence-supported sustainability outcomes.

This formulation avoids assuming that all sustainability indicators share the same desirable algebraic direction.

### Experiment
For each prespecified intervention $a_k$,

```math
\boxed{
a_k
\rightarrow
Y^{a_k}(x,t)
\rightarrow
\left(
\Delta\mathfrak R^{a_k},
\Delta\mathbf J_{\rm sus}^{a_k}
\right).
}
```

with candidate core outcomes

```math
\mathbf J_{\rm sus}
=
[J_{\rm access},J_{\rm energy},J_{\rm carbon},J_{\rm cost}]^{\top},
```

subject to the evidence/data acceptance gate for every outcome.

### Interface criticality disposition
The current primary H4 on viability-sensitive interface ranking should not be deleted. It should be migrated to a **supporting Stage-6 diagnostic/subhypothesis** because interface criticality helps select intervention targets but does not itself close the resilience-to-sustainability question.

### Thesis mapping

```text
Chapter 1: RQ4 / SO4 / H4
Chapter 3: Stage 6
Chapter 4.8: intervention-consequence experiment
Chapter 5.4: intervention-consequence results
Chapter 6: resilience–sustainability synergies/trade-offs/burden shifting
Chapter 7: answer RQ4 and adjudicate H4
```

---

## SO5 / RQ5 / H5 — Engineering decision under uncertainty

### SO5
Determine how joint resilience–sustainability evaluation under uncertainty changes the feasible or nondominated set of engineering interventions relative to resilience-only evaluation.

### RQ5
> **How does joint resilience–sustainability evaluation under uncertainty alter infrastructure intervention decisions relative to resilience-only evaluation?**

### H5
> **H5:** Under a predefined disturbance and uncertainty ensemble, incorporating sustainability consequences into intervention evaluation produces a measurable change in the feasible or nondominated intervention set relative to resilience-only evaluation.

### Decision objects

```math
\mathcal A_R^{\star}
\qquad\text{versus}\qquad
\mathcal A_{R,S}^{\star}.
```

A set-change functional must be fixed before confirmatory testing:

```math
\boxed{
D\!\left(\mathcal A_R^{\star},\mathcal A_{R,S}^{\star}\right)
\overset{?}{>}0.
}
```

The exact $D$ may be a preregistered set-overlap, dominance, hypervolume, or decision-change measure only after its engineering interpretation and assumptions are justified.

### Adaptive-transformation disposition
The current primary H5 on adaptive transformation should be retained as a **candidate Stage-7 extension or secondary hypothesis** if data, scope, and computational budget justify sequential adaptive decisions. It should not remain the primary H5 solely because it existed in v1.

### Thesis mapping

```text
Chapter 1: RQ5 / SO5 / H5
Chapter 3: Stage 7
Chapter 4.9: joint-decision experiment
Chapter 5.5: joint-decision results
Chapter 6: decision implications under uncertainty
Chapter 7: answer RQ5 and adjudicate H5
```

---

# 6. One-to-one v2 traceability matrix

| Objective | Research question | Primary hypothesis | Framework responsibility | Primary metric/decision object | Experiment | Results section |
|---|---|---|---|---|---|---|
| SO1 | RQ1 | H1 | Stages 1–3 | trajectory/cascade/service/recovery difference | $M_0/M_1/M_2$ matched comparison | Ch. 5.1 |
| SO2 | RQ2 | H2 | Stage 4 | estimation, feasible-control, response-time, recovery differences | $P+T$ vs $+I$ vs $+I+O$ | Ch. 5.2 |
| SO3 | RQ3 | H3 | Stage 5 | $\mathfrak R_T$ vs $R_{\rm curve}$; incremental decision/prediction skill | matched prospective resilience comparison | Ch. 5.3 |
| SO4 | RQ4 | H4 | Stage 6 | $(\Delta\mathfrak R,\Delta\mathbf J_{\rm sus})$ | intervention replay under matched scenarios | Ch. 5.4 |
| SO5 | RQ5 | H5 | Stage 7 | $D(\mathcal A_R^{\star},\mathcal A_{R,S}^{\star})$ | resilience-only vs joint R–S decision | Ch. 5.5 |

This matrix is the recommended v2 primary-hypothesis architecture because every primary hypothesis answers a distinct engineering question and produces a distinct decision object.

---

# 7. Required synchronization actions

## Gate A — now complete

- [x] framework v2.0 created;
- [x] spatiotemporal requirement introduced;
- [x] resilience core expanded from viability-only to viability + reachability + probability;
- [x] reasoning protocol updated to v1.2;
- [x] mandatory APA 7 adjacent in-text citation discipline established;
- [x] v2 traceability audit completed.

## Gate B — required before new H3–H5 confirmatory work

- [ ] create/version `RESEARCH_HYPOTHESES_V2.md` or explicitly version-update the canonical hypothesis file;
- [ ] replace the old RQ/H traceability file with a v2 RQ→SO→H→metric→experiment→chapter specification while retaining v1 provenance;
- [ ] synchronize `THESIS_MASTER_OUTLINE.md` Chapter 3 Stage 5–7 labels and Chapter 4/5 H3–H5 experiment titles;
- [ ] synchronize `ASU_MSE_THESIS_MASTER_SPECIFICATION_V1.md` scientific architecture to framework v2;
- [ ] revise the proposal abstract so Stage 5 no longer reads as controlled viability alone;
- [ ] preregister H3 definitions of $K,G_{\rm rec},F,T,\alpha,\beta$ and the incremental decision-skill metric;
- [ ] preregister H4 sustainability outcome acceptance gates and intervention set;
- [ ] preregister H5 uncertainty ensemble and set-change decision functional.

## Gate C — execution

Only after Gate B closes may new v2 H3–H5 confirmatory execution begin.

Existing frozen H1 execution controls remain governed by their own files and are not reopened by this audit.

---

# 8. Audit conclusion

The v2 framework is internally coherent, but the repository is **not yet fully traceable** because the current objectives, H3–H5 hypothesis architecture, traceability matrix, master outline, master specification, and abstract still contain v1 assumptions.

The scientifically defensible v2 chain is

```math
\boxed{
RQ_i
\rightarrow
SO_i
\rightarrow
H_i
\rightarrow
\text{metric}
\rightarrow
\text{experiment}
\rightarrow
\text{result}
\rightarrow
\text{engineering conclusion}.
}
```

The major conceptual correction is concentrated in Stage 5:

```math
\boxed{
\text{resilience}
=
\text{remain acceptable}
+
\text{return to acceptable operation}
+
\text{quantify confidence under uncertainty},
}
```

where the plus signs denote conceptual composition, not scalar addition.

The thesis must test the incremental engineering value of this formulation against established performance/recovery assessment rather than assume superiority. This is consistent with the literature on resilience curves and stochastic reachability (Poulin & Kane, 2021; Vinod & Oishi, 2021) and with recent interdependent-infrastructure research priorities emphasizing dynamic evolution, spatial propagation, and multi-target resilience improvement (Tong et al., 2025).

---

# References

Helmrich, A., Markolf, S., Li, R., Carvalhaes, T., Kim, Y., Bondank, E., Natarajan, M., Ahmad, N., & Chester, M. (2021). Centralization and decentralization for resilient infrastructure and complexity. *Environmental Research: Infrastructure and Sustainability, 1*(2), Article 021001. https://doi.org/10.1088/2634-4505/ac0a4f

Poulin, C., & Kane, M. B. (2021). Infrastructure resilience curves: Performance measures and summary metrics. *Reliability Engineering & System Safety, 216*, 107926. https://doi.org/10.1016/j.ress.2021.107926

Rydén Sonesson, T., Johansson, J., & Cedergren, A. (2021). Governance and interdependencies of critical infrastructures: Exploring mechanisms for cross-sector resilience. *Safety Science, 142*, 105383. https://doi.org/10.1016/j.ssci.2021.105383

Tong, W., Li, H. X., Nasirzadeh, F., Yao, F., & Ji, Y. (2025). Resilience of interdependent infrastructure networks: Review and future directions. *International Journal of Critical Infrastructure Protection, 51*, 100793. https://doi.org/10.1016/j.ijcip.2025.100793

Vinod, A. P., & Oishi, M. M. K. (2021). Stochastic reachability of a target tube: Theory and computation. *Automatica, 125*, 109458. https://doi.org/10.1016/j.automatica.2020.109458
