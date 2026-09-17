# MSE Thesis — Multilayer Interdependent Power–Transportation Infrastructure Resilience

> **Current scientific authorities (2026-09-17):**  
> Framework: [`project/CANONICAL_7_STAGE_FRAMEWORK_V2.md`](project/CANONICAL_7_STAGE_FRAMEWORK_V2.md)  
> RQ–SO–H: [`project/CANONICAL_RQ_SO_HYPOTHESES_V3.md`](project/CANONICAL_RQ_SO_HYPOTHESES_V3.md)  
> Chapter I: [`project/CANONICAL_CHAPTER_I_CONTENT_AND_FLOW_V2.md`](project/CANONICAL_CHAPTER_I_CONTENT_AND_FLOW_V2.md)  
> Writing/inference: [`thesis/00_governance/SCIENTIFIC_WRITING_AND_INFERENCE_STANDARD_V1.md`](thesis/00_governance/SCIENTIFIC_WRITING_AND_INFERENCE_STANDARD_V1.md)

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
**Updated:** 2026-09-17

> **Repository rule:** active thesis development belongs in `Dossiya-SE/MSE-thesis`. Historical/archive material is provenance only and cannot override current canonical files.

> **Evidence-use rule:** scientific literature justifies questions, mechanisms, mathematics, comparators and engineering relevance. Literature support is not proof of novelty; novelty remains a separate reproducible search/audit gate.

---

## Proposal-stage abstract

The increasing electrification and operational coupling of transportation and electricity services motivates a systems-level representation of Power–Transportation infrastructure that preserves constituent-system physics while making directional interdependencies, information flows, organizational constraints and feasible controls explicit. This thesis represents the physical core as an interdependent Power–Transportation System of Systems and models its behavior as a spatiotemporal complex dynamical system with state-, time- and mode-dependent interdependency mechanisms.

The research investigates how evidence-qualified coupling mechanisms shape disturbance propagation, cascading behavior, service degradation and recovery; how observation, state estimation, information availability, organizational capability and control modify feasible responses; and under what conditions critical services can remain acceptable or recover under uncertainty. Resilience is represented through viability, recovery reachability and confidence/probability where probabilistic treatment is evidence-supported. Conventional performance/recovery curves remain a comparator rather than being discarded.

The thesis then evaluates engineering interventions by distinguishing effectiveness, resource efficiency and sustainability consequences. Sustainability outcomes are limited to dimensions for which mechanisms, data and accounting boundaries can be defended, including accessibility, operational energy, carbon and cost where applicable. Joint resilience–sustainability engineering decisions are evaluated under feasibility and uncertainty. Interface criticality is treated as a supporting diagnostic; adaptive or sequential transformation pathways remain a supporting extension unless separately activated and preregistered.

The intended contribution is an evidence-grounded, falsifiable and uncertainty-aware mathematical and engineering framework that links structure, causal interdependency, hybrid dynamics, knowledge and feasible action, resilience limits, intervention consequences and defensible infrastructure decisions. Quantitative superiority or performance claims are withheld until the corresponding preregistered experiments, validation and uncertainty analyses are completed.

---

# Chapter 1 — Introduction

## 1.1 Background and Engineering Context

Critical infrastructure systems provide essential services required for the functioning of modern societies, including electricity, mobility, communications, water, and other services that support economic activity and public welfare. Although these infrastructures are often designed, operated, and regulated as distinct systems, their performance is increasingly shaped by cross-system dependencies. A dependency exists when the state or operation of one infrastructure depends on another, while an interdependency involves reciprocal relationships through which changes in one system can influence another and potentially propagate back to the originating system (Rinaldi et al., 2001). Research on interdependent critical infrastructure has consequently moved beyond isolated-network analysis toward representations capable of capturing interactions, cascading effects, and recovery across multiple infrastructure systems (Ouyang, 2014).

Within this broader infrastructure context, **electric power and transportation form a particularly important coupled system**. The increasing electrification of transportation strengthens this coupling because electric-vehicle charging introduces spatially and temporally varying electricity demand into distribution networks, while charging availability and electrified mobility depend on the operating condition of the power system. Reviews of integrated transportation and power-distribution systems identify coordination among transportation demand, charging infrastructure, and electrical networks as an important joint planning and operational problem (Wei et al., 2019; Unterluggauer et al., 2022).

The coupling is **directional and potentially reciprocal**. In the power-to-transportation direction, `P→T`, electrical service enables transportation functions such as traffic-control devices, charging infrastructure, and other electrically dependent transportation assets. In the transportation-to-power direction, `T→P`, the condition of the road network can influence power-system recovery because repair crews and mobile emergency resources must physically reach damaged electrical assets. Fan et al. (2024), for example, explicitly model the dependence of repair-crew routing on transportation-network road states in coordinated post-disaster restoration, demonstrating the engineering relevance of spatial accessibility to infrastructure recovery.

These interactions become especially important under disruptive conditions. A disturbance that initially affects one infrastructure can modify the operating conditions of another through an active dependency mechanism, creating indirect service losses or cascading effects. Rinaldi et al. (2001) established a foundational framework for identifying and analyzing critical-infrastructure interdependencies, while Ouyang (2014) reviewed multiple modeling approaches for representing interdependent infrastructure behavior and cascading consequences. This distinction is important for the present research: **simultaneous exposure to the same hazard is not, by itself, sufficient to establish an interdependency**. A rigorous interdependency claim requires an identifiable relationship through which the state or service of a source system affects a receiving system.

The resulting engineering problem has both an **architectural** and a **behavioral** dimension. Systems-of-systems research emphasizes that constituent systems can retain operational and managerial characteristics while participating in a larger architecture whose behavior depends on their interactions (Maier, 1998). Infrastructure-interdependency research, in turn, emphasizes that coupled infrastructures can exhibit system-level behavior that cannot be inferred solely from isolated constituent networks (Rinaldi et al., 2001; Ouyang, 2014). Accordingly, this thesis deliberately distinguishes the two viewpoints:

```math
\boxed{
\text{System of Systems}
=
\text{architectural representation}
}
```

and

```math
\boxed{
\text{Complex dynamical system}
=
\text{behavioral representation}.
}
```

The first identifies **what systems, components, interfaces, and relationships exist**; the second addresses **how their states evolve, interact, propagate disruption, and recover through time**. This distinction is used here as a thesis modeling convention derived from the complementary roles of systems-of-systems architecture and interdependent-infrastructure dynamics; it is not presented as a universal definition from a single source.

Physical connectivity alone, however, does not determine infrastructure response. The effect of a disruption also depends on whether system conditions can be observed, whether available information correctly represents those conditions, and whether organizations possess the authority, coordination capability, personnel, equipment, and time required to implement feasible actions. Rinaldi et al. (2001) explicitly recognize that infrastructure interactions may occur not only through physical relationships but also through information and communications dependencies. For the present thesis, these considerations motivate a distinction between the **physical infrastructure core**, Power and Transportation, and the supporting **Information and Organizational domains**, which affect how the physical system is observed and acted upon. Their precise definitions and boundaries are introduced in Section 1.2.

The central engineering concern is therefore not simply whether Power and Transportation networks are connected. It is whether identifiable interdependencies materially alter system trajectories under disturbance; whether the resulting coupled behavior changes the maintenance and recovery of electricity and mobility services; and whether feasible operational actions can prevent or reverse unacceptable degradation. This requires progression from structural knowledge to causal mechanisms, from causal mechanisms to time-dependent dynamics, and from dynamics to observable and controllable service behavior. A static representation of connectivity may identify where interactions are possible, but it does not by itself establish **why an effect propagates, when it occurs, how large it becomes, or whether the system can recover**.

This thesis consequently takes the physical coupling between Power and Transportation as its engineering core and treats Information and Organization as supporting domains governing observation, interpretation, coordination, resources, and control. The resulting study object is introduced conceptually as

```math
\boxed{
\underbrace{P+T}_{\text{physical infrastructure core}}
+
\underbrace{I+O}_{\text{supporting domains}}
}
```

where the presence of a layer or relation does not automatically imply causal significance. Each cross-system relationship must later be supported by an explicit mechanism, admissible evidence, defined mathematical representation, and stated validity domain. This provides the foundation for Section 1.2, which defines the coupled `P–T–I–O` system boundary and the specific relationships considered in the thesis.

### References cited in Section 1.1

- Fan, J., He, P., Li, C., Zhao, C., & Ji, Y. (2024). A post-disaster restoration model for power-gas-transportation distribution networks considering spatial interdependency and energy hubs. *Electric Power Systems Research, 233*, 110505. https://doi.org/10.1016/j.epsr.2024.110505
- Maier, M. W. (1998). Architecting principles for systems-of-systems. *Systems Engineering, 1*(4), 267–284. https://doi.org/10.1002/(SICI)1520-6858(1998)1:4%3C267::AID-SYS3%3E3.0.CO;2-D
- Ouyang, M. (2014). Review on modeling and simulation of interdependent critical infrastructure systems. *Reliability Engineering & System Safety, 121*, 43–60. https://doi.org/10.1016/j.ress.2013.06.040
- Rinaldi, S. M., Peerenboom, J. P., & Kelly, T. K. (2001). Identifying, understanding, and analyzing critical infrastructure interdependencies. *IEEE Control Systems Magazine, 21*(6), 11–25. https://doi.org/10.1109/37.969131
- Unterluggauer, T., Rich, J., Andersen, P. B., & Hashemi, S. (2022). Electric vehicle charging infrastructure planning for integrated transportation and power distribution networks: A review. *eTransportation, 12*, 100163. https://doi.org/10.1016/j.etran.2022.100163
- Wei, W., Wu, D., Wu, Q., Shafie-khah, M., & Catalão, J. P. S. (2019). Interdependence between transportation system and power distribution system: A comprehensive review on models and applications. *Journal of Modern Power Systems and Clean Energy, 7*, 433–448. https://doi.org/10.1007/s40565-019-0516-7

---

## Canonical entry points

| File | Role |
|---|---|
| [`thesis/README.md`](thesis/README.md) | ASU-facing thesis document architecture |
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

H1 M0/M1/M2 implementations and confirmatory design are advanced/frozen as applicable; row-level raw-data retrieval/qualification remains the active blocking gate before calibration or confirmatory execution. H2 empirical qualification remains open. H3–H5 remain blocked until their hypothesis-specific preregistration, data, metric, accounting-boundary and VVUQ gates close.

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
