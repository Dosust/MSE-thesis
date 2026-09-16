# MSE Thesis — Multilayer Interdependent Power–Transportation Infrastructure Resilience

![Degree](https://img.shields.io/badge/degree-MSE-0969DA)
![Citation](https://img.shields.io/badge/citations-APA%207-8250DF)
![Framework](https://img.shields.io/badge/stages%201--7-FROZEN-1A7F37)
![Method](https://img.shields.io/badge/EGMIV-v1.0-0969DA)
![Hypotheses](https://img.shields.io/badge/H1--H5%20logic-FROZEN-1A7F37)
![H1 Models](https://img.shields.io/badge/M0%20M1%20M2-VERIFIED-1A7F37)
![H1 Prereg](https://img.shields.io/badge/confirmatory%20design-FROZEN-1A7F37)
![H1 Data](https://img.shields.io/badge/raw%20row%20retrieval-PENDING-B42318)
![Thesis Control](https://img.shields.io/badge/ASU%20thesis%20architecture-CURRENT-0969DA)

**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Repository:** active thesis source of truth  
**Framework status:** complete seven-stage conceptual and mathematical framework frozen  
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

The increasing electrification and interdependence of urban infrastructure are creating tightly coupled power–transportation systems whose resilience depends not only on physical network structure, but also on dynamic interdependencies, information availability, organizational response, and feasible control actions. However, existing resilience studies commonly treat these dimensions separately, rely on static dependency representations, or evaluate recovery primarily through service-loss metrics, providing limited insight into whether a disrupted system remains controllably capable of satisfying critical service and sustainability constraints. To address this gap, this study develops a **multilayer dynamics and controlled-viability framework for interdependent power–transportation systems**, explicitly integrating physical, informational, and organizational mechanisms. First, a multilayer interdependency representation is formulated to map state-, time-, and mode-dependent power–transportation interactions into coupled hybrid multiscale dynamics, enabling explicit characterization of disruption propagation and cascading effects. Second, an observation–organization–control layer is introduced to represent sensing, estimation, communication, coordination, resource availability, and response delays, thereby linking system state information to feasible intervention sets. Third, controlled viability theory is used to characterize the set of states from which sustainability and service constraints can remain satisfied under admissible controls, together with viability margins, time-to-viability loss, and interface-level criticality measures. Finally, adaptive transformation pathways are formulated as viability-constrained, many-objective transitions between alternative infrastructure architectures under deep uncertainty. The framework will be evaluated through a minimal sufficient power–transportation–information–organization demonstrator using physics-based simulation, verification and validation, uncertainty quantification, competing-model comparisons, and hypothesis-driven experiments. The study aims to establish when dynamic interdependencies, information and organizational constraints, viability-based indicators, and adaptive infrastructure transformation materially improve the characterization and management of infrastructure resilience.

> **Results rule:** quantitative performance claims are intentionally omitted at this stage. Numerical improvements will be added only after the relevant confirmatory hypotheses have been tested.

---

## Canonical entry points

| File | Role |
|---|---|
| [`thesis/README.md`](thesis/README.md) | **ASU-facing thesis document architecture and control entry point** |
| [`thesis/00_governance/ASU_MSE_THESIS_MASTER_SPECIFICATION_V1.md`](thesis/00_governance/ASU_MSE_THESIS_MASTER_SPECIFICATION_V1.md) | ASU/SSEBE + scientific thesis master specification |
| [`project/README.md`](project/README.md) | active mathematical/project dashboard |
| [`project/RESEARCH_REASONING_PROTOCOL.md`](project/RESEARCH_REASONING_PROTOCOL.md) | canonical thesis-wide reasoning, verification, validation, falsification and synthesis protocol |
| [`project/EGMIV_METHOD_V1.md`](project/EGMIV_METHOD_V1.md) | canonical evidence-grounded model-construction/validation method |
| [`project/THESIS_SCOPE.md`](project/THESIS_SCOPE.md) | frozen thesis scope |
| [`project/CANONICAL_7_STAGE_FRAMEWORK.md`](project/CANONICAL_7_STAGE_FRAMEWORK.md) | frozen seven-stage framework |
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

## Frozen scientific framework

```math
\begin{aligned}
\underbrace{\mathcal S}_{1}
&\rightarrow
\underbrace{\mathfrak I}_{2}
\rightarrow
\underbrace{F_{\mathcal G}^{m}}_{3}\\
&\rightarrow
\underbrace{X\rightarrow y\rightarrow I\rightarrow\widehat X\rightarrow O\rightarrow u}_{4}\\
&\rightarrow
\underbrace{K_{\mathrm{sus}},\mathcal V,\rho,T_{\mathcal V},T_K}_{5}\\
&\rightarrow
\underbrace{\Phi_{\mathrm{ST}}\rightarrow(c_6,\mathcal D_6,\boldsymbol\zeta_T)}_{6}\\
&\rightarrow
\underbrace{\mathfrak P_{\mathrm{ST}}}_{7}.
\end{aligned}
```

The primary confirmatory set is

```math
\mathbb H=\{H_1,H_2,H_3,H_4,H_5\}.
```

The seven-stage architecture and H1–H5 scientific logic are frozen. Hypothesis-specific thresholds, scenario domains and decision rules are fixed only through their declared preregistration/evidence gates.

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

The `thesis/` directory now contains the ASU requirements matrix, master outline, claim/evidence ledger, RQ–H traceability, model/experiment/validation matrix, artifact registry, completion gates, proposal workspace, chapter workspaces and appendices.

---

## Current H1 execution gate

```math
\boxed{M_0=\text{independent},\quad M_1=\text{static/algebraic coupling},\quad M_2=\text{dynamic causal coupling}.}
```

Current project authority records the model implementations and H1 confirmatory design as verified/frozen as applicable. The active blocking gate is **row-level raw-data retrieval and qualification**. The candidate train/test split cannot be activated until the predeclared R1–R8 data gates pass; no H1 calibration or confirmatory execution is authorized before that activation.

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

Complete the H1 row-level raw-data retrieval and run the frozen qualification executor through the R1–R8 gates. Only after the data roles and split are activated may calibration and the preregistered H1 confirmatory comparison proceed.
