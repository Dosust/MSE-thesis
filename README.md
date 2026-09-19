# MSE Thesis — Multilayer Interdependent Power–Transportation Infrastructure Resilience

> **Current scientific authorities (2026-09-19):**  
> Framework: [`project/CANONICAL_7_STAGE_FRAMEWORK_V2.md`](project/CANONICAL_7_STAGE_FRAMEWORK_V2.md)  
> RQ–SO–H: [`project/CANONICAL_RQ_SO_HYPOTHESES_V3.md`](project/CANONICAL_RQ_SO_HYPOTHESES_V3.md)  
> Chapter I: [`project/CANONICAL_CHAPTER_I_CONTENT_AND_FLOW_V2.md`](project/CANONICAL_CHAPTER_I_CONTENT_AND_FLOW_V2.md)  
> Writing/inference: [`thesis/00_governance/SCIENTIFIC_WRITING_AND_INFERENCE_STANDARD_V1.md`](thesis/00_governance/SCIENTIFIC_WRITING_AND_INFERENCE_STANDARD_V1.md)  
> P–T SoS / complex-dynamics interpretation: [`project/CANONICAL_PT_SOS_COMPLEX_DYNAMICS_AMENDMENT_V1_1.md`](project/CANONICAL_PT_SOS_COMPLEX_DYNAMICS_AMENDMENT_V1_1.md)

![Degree](https://img.shields.io/badge/degree-MSE-0969DA)
![Citation](https://img.shields.io/badge/citations-APA%207-8250DF)
![Framework](https://img.shields.io/badge/stages%201--7-v2.0-1A7F37)
![Resilience](https://img.shields.io/badge/core-viability%20%2B%20reachability%20%2B%20probability-0969DA)
![Method](https://img.shields.io/badge/EGMIV-v1.0-0969DA)
![Traceability](https://img.shields.io/badge/RQ--SO--H-v3.0%20CURRENT-1A7F37)
![H1](https://img.shields.io/badge/raw%20row%20qualification-PENDING-B42318)
![Thesis Control](https://img.shields.io/badge/ASU%20thesis%20architecture-CURRENT-0969DA)

**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Repository:** active thesis source of truth  
**Physical core:** Power + Transportation (`P+T`)  
**Supporting domains:** Information + Organization (`I+O`)  
**Framework:** canonical seven-stage framework v2.0  
**Research logic:** RQ0 + RQ1–RQ7, SO1–SO7, H1–H5 under canonical v3.0  
**Execution method:** EGMIV — Evidence-Grounded Mechanistic Interdependency and Validation Method  
**Citation standard:** APA 7 author–date internally; final style subject to chair approval and ASU precedence  
**Updated:** 2026-09-19

> **Repository rule:** active thesis development belongs in `Dossiya-SE/MSE-thesis`. Historical/archive material is provenance only and cannot override current canonical files.

> **Evidence-use rule:** scientific literature justifies questions, mechanisms, mathematics, comparators and engineering relevance. Literature support is not proof of novelty; novelty remains a separate reproducible search/audit gate.

---

## Proposal-stage abstract

**The rapid electrification of transportation is strengthening the dependence between power and transportation infrastructures that jointly deliver electricity and mobility services.** This coupling can improve performance, but it can also create pathways through which disturbances, operational constraints, and recovery limitations propagate from one system to the other. Existing studies often represent these relationships through network connectivity, fixed dependencies, or aggregate resilience measures. A central research need is therefore to connect evidence-supported causal mechanisms with dynamic service behavior, feasible response, and engineering decisions under uncertainty.

This thesis develops an evidence-grounded mathematical and engineering framework for coupled power–transportation infrastructure, viewed as a **system of systems with spatiotemporal complex dynamics**. Power and transportation are represented as distinct physical systems with their own topology, physics, controls, failure modes, and service functions. Information and organizational capabilities are treated as supporting domains that determine what can be observed, coordinated, resourced, and acted upon. The framework links system structure, causal interdependencies, coupled dynamics, observation and control, resilience assessment, intervention consequences, and engineering decision-making.

A key principle is that **structural connection, causal dependency, dynamic coupling, service loss, and resilience are not equivalent**. Interdependencies enter the dynamic model only when their direction, mechanism, evidence, and uncertainty are sufficiently specified. Resilience is evaluated by asking whether critical electricity and mobility services can remain within acceptable conditions during disruption and, when they cannot, whether acceptable service can be recovered. These questions are represented through viability and reachability, with uncertainty treated explicitly rather than collapsed into a single resilience score.

Engineering interventions are assessed separately for resilience improvement, effectiveness, resource efficiency, and qualified sustainability consequences. Direct cost and operational energy are treated as resource consequences, while carbon-dioxide-equivalent emissions form the planned core sustainability consequence; distributional accessibility remains conditional on defensible data and accounting boundaries. The framework is structured for matched model comparisons, preregistered hypotheses, uncertainty analysis, verification, and validation. Its purpose is to determine when coupled services remain feasible, why recovery succeeds or fails, which interdependencies materially affect resilience, and how that evidence can support defensible infrastructure decisions without overstating what the data can establish.

---

## Chapter 1 — Introduction

Chapter-I prose is maintained only in [`thesis/01_introduction/`](thesis/01_introduction/README.md) to prevent parallel versions in the project dashboard.

| Section | Current thesis source |
|---|---|
| 1.1 Background and Engineering Context | [`01_01_background_and_engineering_context.md`](thesis/01_introduction/01_01_background_and_engineering_context.md) |
| 1.2 Coupled P–T–I–O System Context | [`01_02_coupled_ptio_system_context.md`](thesis/01_introduction/01_02_coupled_ptio_system_context.md) |
| 1.3 Problem Statement | [`01_03_problem_statement.md`](thesis/01_introduction/01_03_problem_statement.md) |
| 1.4 Research Gap | [`01_04_research_gap.md`](thesis/01_introduction/01_04_research_gap.md) |
| 1.5 Sustainable Engineering Significance | next drafting task |

Current Chapter-I progression:

```math
\boxed{
\text{Context}
\rightarrow
\text{System definition}
\rightarrow
\text{Engineering problem}
\rightarrow
\text{Evidence-supported gap}
\rightarrow
\text{Sustainable-engineering significance}
}
```

---

## Canonical entry points

| File | Role |
|---|---|
| [`thesis/README.md`](thesis/README.md) | ASU-facing thesis document architecture |
| [`thesis/01_introduction/README.md`](thesis/01_introduction/README.md) | Chapter-I source index and coherence controls |
| [`thesis/00_governance/ASU_MSE_THESIS_MASTER_SPECIFICATION_V1.md`](thesis/00_governance/ASU_MSE_THESIS_MASTER_SPECIFICATION_V1.md) | ASU/SSEBE + scientific thesis master specification |
| [`thesis/00_governance/THESIS_MASTER_OUTLINE.md`](thesis/00_governance/THESIS_MASTER_OUTLINE.md) | seven-chapter thesis outline |
| [`thesis/00_governance/RQ_SO_H_TRACEABILITY_V3.md`](thesis/00_governance/RQ_SO_H_TRACEABILITY_V3.md) | current RQ → SO → H → method/result/chapter traceability |
| [`thesis/00_governance/SCIENTIFIC_WRITING_AND_INFERENCE_STANDARD_V1.md`](thesis/00_governance/SCIENTIFIC_WRITING_AND_INFERENCE_STANDARD_V1.md) | claim/evidence/inference writing standard |
| [`thesis/00_governance/CLAIM_EVIDENCE_REGISTER.md`](thesis/00_governance/CLAIM_EVIDENCE_REGISTER.md) | epistemic claim ledger |
| [`thesis/00_governance/MODEL_EXPERIMENT_VALIDATION_MATRIX.md`](thesis/00_governance/MODEL_EXPERIMENT_VALIDATION_MATRIX.md) | experiment/baseline/VVUQ/falsification control |
| [`project/README.md`](project/README.md) | active mathematical/project dashboard |
| [`project/CANONICAL_7_STAGE_FRAMEWORK_V2.md`](project/CANONICAL_7_STAGE_FRAMEWORK_V2.md) | canonical seven-stage framework v2.0 |
| [`project/CANONICAL_RQ_SO_HYPOTHESES_V3.md`](project/CANONICAL_RQ_SO_HYPOTHESES_V3.md) | current RQ0 + RQ1–RQ7 + SO1–SO7 + H1–H5 |
| [`project/CANONICAL_CHAPTER_I_CONTENT_AND_FLOW_V2.md`](project/CANONICAL_CHAPTER_I_CONTENT_AND_FLOW_V2.md) | current Chapter-I authority |
| [`project/RESEARCH_REASONING_PROTOCOL.md`](project/RESEARCH_REASONING_PROTOCOL.md) | evidence, reasoning, falsification and synthesis protocol |
| [`project/EGMIV_METHOD_V1.md`](project/EGMIV_METHOD_V1.md) | evidence-grounded model-construction/validation method |

Legacy v1/v2 files remain provenance only where a newer authority explicitly supersedes them.

---

## Canonical scientific framework

```math
\boxed{
\text{Spatiotemporal SoS Structure}
\rightarrow
\text{Evidence-Grounded Causal Interdependencies}
\rightarrow
\text{Physics-Based Hybrid Multiscale Dynamics}
\rightarrow
\text{Observation / Estimation / Organization / Control}
\rightarrow
\text{Viability + Reachability + Probability}
\rightarrow
\text{Intervention + Sustainability Consequences}
\rightarrow
\text{Engineering Decision / Transformation}
}
```

The resilience core is

```math
\boxed{
\text{Resilience}
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
\mathfrak R_T
=
\left(
\mathcal V_{\alpha,T_V},
\mathcal R_{\beta,T_R},
\rho_{\mathcal V},
T_{\mathcal V},
T_{\rm rec},
P_{\rm viable},
P_{\rm recover}
\right).
}
```

---

## Canonical RQ–SO–H logic

```math
\boxed{
RQ_i
\rightarrow
SO_i
\rightarrow
\mathcal H(i)
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

Primary tests:

```math
H_1:\ M_2\ \text{vs}\ M_1\ \text{vs}\ M_0,
```

```math
H_2:\ P+T\ \text{vs}\ P+T+I\ \text{vs}\ P+T+I+O,
```

```math
H_3:\ R_{\rm curve}\ \text{vs}\ R_{\rm curve}+\mathfrak R_T,
```

```math
H_4:\ a_k\rightarrow(\Delta\mathfrak R^{a_k},\Delta\mathbf J_{\rm sus}^{a_k}),
```

```math
H_5:\ \mathcal A_R^{\star}\ \text{vs}\ \mathcal A_{R,S}^{\star}.
```

Interface criticality is a supporting diagnostic. Adaptive/sequential transformation is a supporting Stage-7 extension unless separately activated.

---

## Thesis-wide writing standard

```math
\boxed{
\text{Question}
\rightarrow\text{Objective}
\rightarrow\text{Object}
\rightarrow\text{Assumptions}
\rightarrow\text{Method}
\rightarrow\text{Comparator}
\rightarrow\text{Evidence}
\rightarrow\text{Uncertainty}
\rightarrow\text{Result}
\rightarrow\text{Inference}
\rightarrow\text{Validity domain}
}
```

No factual claim without admissible evidence; no mathematical object without semantics; no model without assumptions and validity domain; no confirmatory hypothesis without comparator and non-support logic; no result without uncertainty where relevant; no conclusion beyond the validation domain.

---

## ASU thesis control

The `thesis/` directory maintains the official-requirement mapping, master outline, claim/evidence ledger, RQ/SO/H traceability, scientific writing standard, model/experiment/validation matrix, artifact registry and completion gates.

Current official ASU Graduate College formatting requirements are tracked separately from internal scientific conventions. ASU/Graduate College, SSEBE and committee/chair requirements take precedence over repository rules.

---

## Current execution state

H1 M0/M1/M2 software fixtures are verified at their declared benchmark/test-harness level, but accepted case M2 execution is **not authorized**: `EV_T_to_P` has Stage-2 causal PASS and Stage2→3 BLOCKED status, while `EV_P_to_T`, `SIGNAL_P_to_T`, and `REPAIR_T_to_P` remain case-causally BLOCKED. Exact runtime binding, case qualification, reference/QOI/VVUQ controls, and the remaining data gates must close before confirmatory H1 execution. H2 empirical qualification remains open. H3–H5 remain blocked until their hypothesis-specific preregistration, data, metric, accounting-boundary and VVUQ gates close.

```math
\boxed{
\text{H1 raw-data qualification}
\parallel
\text{H2 empirical qualification}
\parallel
\text{H3 preregistration closure}
\rightarrow
\text{H4 intervention/accounting preregistration}
\rightarrow
\text{H5 joint-decision preregistration}
}
```