# MSE Thesis — Multilayer Interdependent Power–Transportation Infrastructure Resilience

![Degree](https://img.shields.io/badge/degree-MSE-0969DA)
![Citation](https://img.shields.io/badge/citations-APA%207-8250DF)
![Framework](https://img.shields.io/badge/stages%201--7-v2.0-1A7F37)
![Resilience](https://img.shields.io/badge/core-viability%20%2B%20reachability%20%2B%20probability-0969DA)
![Method](https://img.shields.io/badge/EGMIV-v1.0-0969DA)
![Hypotheses](https://img.shields.io/badge/H1--H5%20logic-FROZEN-1A7F37)
![H1 Models](https://img.shields.io/badge/M0%20M1%20M2-VERIFIED-1A7F37)
![H1 Prereg](https://img.shields.io/badge/confirmatory%20design-FROZEN-1A7F37)
![H1 Data](https://img.shields.io/badge/raw%20row%20retrieval-PENDING-B42318)
![Thesis Control](https://img.shields.io/badge/ASU%20thesis%20architecture-CURRENT-0969DA)

**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Repository:** active thesis source of truth  
**Framework status:** canonical seven-stage framework v2.0; v1 retained as provenance  
**Resilience core:** uncertainty-aware viability + reachability + probability  
**Hypothesis status:** five-primary-hypothesis logic frozen; H1 confirmatory design frozen; later hypothesis-specific numerical specifications remain subject to their preregistration gates  
**Reasoning protocol:** canonical Learn → Verify → Formulate → Derive → Test → Validate → Synthesize → Advance discipline  
**Execution method:** EGMIV — Evidence-Grounded Mechanistic Interdependency and Validation Method  
**Evidence methodology:** de novo search + FTEE evidence-to-equation extraction inside EGMIV  
**Document architecture:** ASU/SSEBE-controlled thesis structure maintained in `thesis/`  
**Citation standard:** APA 7th edition author–date internally; final style remains subject to chair approval and ASU precedence  
**Updated:** 2026-09-16

> **Repository rule:** active thesis development belongs in `Dossiya-SE/MSE-thesis`. Historical/archive material is provenance only and cannot override current canonical files.

---

## Abstract

**Status:** Proposal / pre-results abstract.

The increasing electrification of transportation is making the continuity of electricity and mobility services increasingly dependent on interconnected physical infrastructure, information flows, organizational decisions, and control actions. This research represents coupled power–transportation infrastructure architecturally as an **interdependent system of systems** and dynamically as a **complex dynamical system** whose constituent infrastructures retain distinct physical laws while interacting through explicit **state-, time-, and mode-dependent interdependency mechanisms**.

The study addresses how evidence-supported power–transportation interdependencies, together with information availability, organizational constraints, and feasible controls, shape disruption propagation, cascading effects, service degradation, and recovery. An evidence-grounded mathematical framework maps directional interdependencies into a **coupled hybrid multiscale dynamical model**. Observation and organizational mechanisms—including sensing, state estimation, communication, coordination, resource availability, authority, and response delays—determine what system states can be known, which actions are feasible, and how quickly those actions can be implemented.

Resilience is characterized through service loss, recovery, cascading behavior, and an **uncertainty-aware viability–reachability formulation**. Viability represents the ability to maintain acceptable service under feasible controls; reachability represents the ability to return to acceptable operation after degradation; probability quantifies confidence in these capabilities under uncertainty. Viability margins, time-to-viability loss, recovery time, and associated maintainability/recovery probabilities provide complementary resilience information. Conventional performance/recovery curves are retained as a benchmark, and the thesis tests rather than assumes whether the proposed formulation adds engineering value.

Sustainability is treated as an **emergent consequence of how the coupled system operates, fails, recovers, and is redesigned** rather than as an independent score. Evaluation focuses on **accessibility, operational energy use, carbon emissions, cost**, and additional outcomes only where causal mechanisms and data support their inclusion. The framework is tested using a minimal coupled **power–transportation demonstrator with explicit information and organizational layers**, physics-based simulation, competing independent, static-coupling, and dynamic-causal models, hypothesis-driven experiments, and **verification, validation, and uncertainty quantification**. The intended contribution is a defensible engineering decision framework that identifies consequential interdependencies, explains resilience loss, evaluates intervention effects, and makes **resilience–sustainability synergies, trade-offs, and burden shifting explicit under uncertainty**.

> **Results rule:** Quantitative performance claims are withheld until the corresponding confirmatory hypotheses, validation tests, and uncertainty analyses have been completed.

---

## Canonical entry points

| File | Role |
|---|---|
| [`thesis/README.md`](thesis/README.md) | **ASU-facing thesis document architecture and control entry point** |
| [`thesis/00_governance/ASU_MSE_THESIS_MASTER_SPECIFICATION_V1.md`](thesis/00_governance/ASU_MSE_THESIS_MASTER_SPECIFICATION_V1.md) | ASU/SSEBE + scientific thesis master specification |
| [`project/README.md`](project/README.md) | active mathematical/project dashboard |
| [`project/CANONICAL_7_STAGE_FRAMEWORK_V2.md`](project/CANONICAL_7_STAGE_FRAMEWORK_V2.md) | **current canonical seven-stage framework v2.0** |
| [`project/CANONICAL_7_STAGE_FRAMEWORK.md`](project/CANONICAL_7_STAGE_FRAMEWORK.md) | v1 framework retained for provenance only |
| [`project/CANONICAL_SPATIOTEMPORAL_PROPAGATION_REQUIREMENT_V1.md`](project/CANONICAL_SPATIOTEMPORAL_PROPAGATION_REQUIREMENT_V1.md) | frozen spatiotemporal propagation requirement |
| [`project/RESEARCH_REASONING_PROTOCOL.md`](project/RESEARCH_REASONING_PROTOCOL.md) | canonical thesis-wide reasoning, verification, validation, falsification and synthesis protocol |
| [`project/EGMIV_METHOD_V1.md`](project/EGMIV_METHOD_V1.md) | canonical evidence-grounded model-construction/validation method |
| [`project/THESIS_SCOPE.md`](project/THESIS_SCOPE.md) | frozen thesis scope |
| [`project/RESEARCH_HYPOTHESES.md`](project/RESEARCH_HYPOTHESES.md) | five primary confirmatory hypotheses |
| [`project/H1_MATHEMATICAL_MODEL_SPECIFICATION_V1.md`](project/H1_MATHEMATICAL_MODEL_SPECIFICATION_V1.md) | H1 M0/M1/M2 physical specification |
| [`project/H1_CONFIRMATORY_PREREGISTRATION_V1.md`](project/H1_CONFIRMATORY_PREREGISTRATION_V1.md) | H1 confirmatory design |
| [`project/H1_ROW_LEVEL_DATA_QUALIFICATION_STATUS_V1.md`](project/H1_ROW_LEVEL_DATA_QUALIFICATION_STATUS_V1.md) | current H1 raw-data execution gate |
| [`project/FRESH_SEARCH_FULL_TEXT_EVIDENCE_TO_EQUATION_PROTOCOL_FTEE_V2.md`](project/FRESH_SEARCH_FULL_TEXT_EVIDENCE_TO_EQUATION_PROTOCOL_FTEE_V2.md) | de novo evidence-search + FTEE methodology |
| [`project/MATHEMATICAL_PRESENTATION_V3.md`](project/MATHEMATICAL_PRESENTATION_V3.md) | GitHub math/rendering standard |
| [`tools/thesis_display_lint.py`](tools/thesis_display_lint.py) | automated Markdown/math/ontology QA |

---

## Canonical reasoning standard

```math
\text{LEARN}
\rightarrow
\text{VERIFY}
\rightarrow
\text{FORMULATE}
\rightarrow
\text{DERIVE}
\rightarrow
\text{TEST}
\rightarrow
\text{VALIDATE}
\rightarrow
\text{SYNTHESIZE}
\rightarrow
\text{ADVANCE}.
```

Every substantive thesis claim must expose its definition, evidence status, mechanism, mathematics, assumptions, competing test, uncertainty, validation domain, and engineering implication.

---

## Canonical scientific framework v2.0

The seven-stage architecture is retained, but Stage 5 is revised from controlled viability alone to an uncertainty-aware viability–reachability resilience core.

| Stage | Scientific role | Main question |
|---|---|---|
| **1. Spatiotemporal Multilayer SoS Structure** | Define systems, components, layers and geography | What exists and where? |
| **2. Evidence-Grounded Causal Interdependencies** | Define directional causal mechanisms | Why and through what mechanism are systems coupled? |
| **3. Physics-Based Hybrid Multiscale Dynamics** | Propagate mechanisms through time and space | How, where and how fast do effects propagate? |
| **4. Observation, State Estimation, Organization and Control** | Determine system knowledge and feasible actions | What do operators know and what can they do? |
| **5. Uncertainty-Aware Viability and Reachability Resilience** | Quantify remain + return + confidence | Can service remain or recover acceptably, and with what probability? |
| **6. Resilience Diagnosis, Intervention and Sustainability Consequences** | Convert diagnosis into interventions and consequences | What should be changed and what consequences follow? |
| **7. Engineering Decision and Adaptive Transformation** | Select defensible interventions under uncertainty | Which intervention/pathway should be implemented, where and when? |

The resilience core is

```math
\boxed{
\textbf{Resilience}
=
\underbrace{\text{maintain acceptable service}}_{\text{viability}}
+
\underbrace{\text{recover acceptable service}}_{\text{reachability}}
+
\underbrace{\text{quantify confidence}}_{\text{probability}}
}
```

where `+` denotes conceptual composition rather than scalar addition.

The formal Stage-5 object is

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

Conventional performance/recovery assessment remains an explicit comparator:

```math
\boxed{
R_{\rm curve}
\quad\text{versus}\quad
\mathfrak R_T.
}
```

No superiority is assumed; incremental predictive or decision value must be demonstrated experimentally.

### Complete mathematical chain

```math
\boxed{
\begin{aligned}
K(t)
&\rightarrow
\underbrace{(\mathcal S,\mathcal G,X)}_{1}\\
&\rightarrow
\underbrace{\mathbb I(x,t,Y,m)}_{2}\\
&\rightarrow
\underbrace{F_{\mathcal G}^{m}}_{3}\\
&\rightarrow
Y(x,t)\\
&\rightarrow
\underbrace{
y_t
\rightarrow\mathcal I_t
\rightarrow p(Y_t\mid\mathcal I_t)
\rightarrow\mathcal U(z_I,z_O)
\rightarrow u_t
}_{4}\\
&\rightarrow
\underbrace{
\left(
\mathcal V_{\alpha,T},
\mathcal R_{\beta,T},
P_{\rm viable},
P_{\rm recover}
\right)
}_{5}\\
&\rightarrow
\underbrace{
\mathcal D_R
\rightarrow a_k
\rightarrow Y^{a_k}
\rightarrow
(\Delta\mathfrak R,\Delta\mathbf J_{\rm sus})
}_{6}\\
&\rightarrow
\underbrace{\mathcal A_{R,S}^{\star}}_{7}.
\end{aligned}
}
```

The simplest scientific interpretation is

```math
\boxed{
\begin{gathered}
\text{Need} \rightarrow \text{Structure} \rightarrow \text{Causality} \rightarrow \text{Dynamics} \\
\rightarrow \text{Knowledge \& Action} \rightarrow \text{Remain / Return / Confidence} \\
\rightarrow \text{Intervention \& Consequences} \rightarrow \text{Decision}
\end{gathered}
}
```

Full definitions, stage boundaries, validation guardrails and mathematical details are maintained in [`project/CANONICAL_7_STAGE_FRAMEWORK_V2.md`](project/CANONICAL_7_STAGE_FRAMEWORK_V2.md).

---

## EGMIV execution discipline

```math
\boxed{
\text{Evidence}
\rightarrow
\text{Mechanism}
\rightarrow
\text{Interdependency}
\rightarrow
\text{Mathematical Model}
\rightarrow
\text{Validation}.
}
```

EGMIV requires directional mechanisms, admissible evidence, graph-to-dynamics mapping, rival-model comparison, nested limits, uncertainty, physical verification, held-out validation where available, and explicit falsification.

FTEE remains the evidence-to-equation extraction protocol inside EGMIV.

---

## Cross-cutting VVUQ and falsification

Verification, validation and uncertainty quantification are not a separate framework stage. They apply across Stages 1–7:

```math
\boxed{
\text{Stages }1\text{--}7
\subset
\text{VVUQ + falsification}.
}
```

Every proposed mechanism or model must expose its assumptions, parameters, evidence, uncertainty, verification tests and validation domain.

The principal model-comparison architecture remains

```math
\boxed{
M_0=\text{independent systems},
\qquad
M_1=\text{static coupling},
\qquad
M_2=\text{dynamic causal coupling}.
}
```

The primary comparison remains falsifiable:

```math
\boxed{M_2\overset{?}{>}M_1.}
```

---

## ASU thesis control architecture

```math
\boxed{
\text{ASU requirement}
\rightarrow\text{claim}
\rightarrow\text{evidence}
\rightarrow\text{method}
\rightarrow\text{result}
\rightarrow\text{thesis location}
\rightarrow\text{verification}.
}
```

The `thesis/` directory contains the ASU requirements matrix, master outline, claim/evidence ledger, RQ–H traceability, model/experiment/validation matrix, artifact registry, completion gates, proposal workspace, chapter workspaces and appendices.

---

## Current H1 execution gate

```math
\boxed{M_0=\text{independent},\quad M_1=\text{static/algebraic coupling},\quad M_2=\text{dynamic causal coupling}.}
```

Current project authority records the model implementations and H1 confirmatory design as verified/frozen as applicable. The active blocking gate is **row-level raw-data retrieval and qualification**. The candidate train/test split cannot be activated until the predeclared R1–R8 data gates pass; no H1 calibration or confirmatory execution is authorized before that activation.

The v2.0 framework revision does not itself modify the frozen H1 M0/M1/M2 experiment. Any downstream change to H1 or H2–H5 requires an explicit traceability audit and versioned amendment.

Authenticated database evidence completion remains a separate evidence task and is not replaced by public discovery or model-development evidence.

---

## Governing evidence rules

```math
\textbf{No paper is evidence because we remember it.}
```

```math
\textbf{No numerical parameter is empirical merely because it is convenient.}
```

```math
\textbf{No preferred model is validated without a relevant rival/baseline.}
```

```math
\textbf{No thesis conclusion is stronger than its evidence, experiment and validation domain.}
```

---

## Immediate next task

Complete the H1 row-level raw-data retrieval and run the frozen qualification executor through the R1–R8 gates. In parallel, perform the required **v2.0 traceability audit** to identify which research questions, hypotheses, Stage-5 metrics, experiments and thesis sections require versioned synchronization with the viability–reachability resilience core. No downstream file should be silently overwritten.