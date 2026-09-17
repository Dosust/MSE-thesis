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

## 1.2 Coupled Power–Transportation–Information–Organization System Context

The engineering context established in Section 1.1 motivates a more precise definition of the system studied in this thesis. The research does not treat all critical infrastructures as a single undifferentiated network. Instead, it focuses on a bounded coupled system whose **physical infrastructure core** consists of electric power and transportation, while information and organizational capabilities are represented explicitly because they influence what is known about the physical system and what actions can be implemented during disruption and recovery. The resulting study context is denoted conceptually as

```math
\boxed{
\mathcal S=\{P,T,I,O\},
}
```

where

```math
P=\text{Power},\qquad
T=\text{Transportation},\qquad
I=\text{Information},\qquad
O=\text{Organization}.
```

This notation does not imply that the four domains are physically equivalent infrastructure networks. In this thesis, `P` and `T` are the two principal **physical infrastructure systems**, whereas `I` and `O` are supporting domains through which system conditions are observed, interpreted, communicated, coordinated, and acted upon. This distinction is deliberate. Multilayer-network theory provides a general framework for systems containing multiple subsystems and multiple types of relationships, but the existence of a layer or interlayer edge is a structural representation rather than evidence of a causal mechanism (Kivelä et al., 2014).

The **Power domain `P`** represents the physical assets and network relationships required to generate, transmit, distribute, and deliver electricity to infrastructure loads relevant to the coupled system. At the structural level it may be represented by a graph

```math
\mathcal G_P=(V_P,E_P),
```

where `V_P` denotes relevant power-system assets or buses and `E_P` denotes electrical connections. The **Transportation domain `T`** represents the physical mobility network through which travelers, repair crews, emergency resources, and other relevant flows move. Its structural representation may similarly be written as

```math
\mathcal G_T=(V_T,E_T),
```

where `V_T` contains transportation nodes such as intersections or relevant facilities and `E_T` contains road links or other admissible physical connections. These graph representations define **system structure**; they do not by themselves specify power-flow physics, traffic-flow dynamics, failure propagation, or recovery behavior. Those mechanisms are introduced only after their physical and causal meaning has been established.

The physical coupling between `P` and `T` is represented directionally rather than by treating the two networks as generically “connected.” In the power-to-transportation direction,

```math
\boxed{P\rightarrow T},
```

electricity can support transportation functions such as traffic-control devices and electric-vehicle charging infrastructure. Coupled traffic–power studies have represented such relationships through explicit linking variables and logical constraints, while the broader transportation-electrification literature models interactions among charging demand, road-network behavior, and power-distribution operating constraints (Fotouhi et al., 2017; Wei et al., 2019; Unterluggauer et al., 2022).

The reciprocal transportation-to-power direction is conceptually distinct:

```math
\boxed{T\rightarrow P}.
```

Here, transportation conditions influence activities required for power-system operation or restoration. A particularly important recovery mechanism is **physical accessibility**: damaged roads, congestion, or unavailable routes can affect when repair crews and mobile emergency resources reach failed electrical assets. Fan et al. (2024), for example, explicitly couple road states to repair-crew routing in coordinated infrastructure restoration. Such restoration models confirm that `T→P` is not merely a topological relationship but can operate through identifiable logistical mechanisms.

These two directions must not be collapsed into a single undifferentiated `P↔T` edge. A reciprocal interdependency exists only when the corresponding directional mechanisms are actually present under the conditions being studied. This follows the broader infrastructure-interdependency literature, which distinguishes the state dependence of one infrastructure on another and emphasizes physical, cyber/informational, geographic, and logical dimensions of interdependency (Rinaldi et al., 2001). Accordingly, this thesis adopts the stricter engineering rule

```math
\boxed{
\text{candidate relation}
\neq
\text{accepted causal dependency}.
}
```

A cross-system relation enters the model only after its **source, receiver, mechanism, component mapping, evidence basis, and validity conditions** are identified.

The **Information domain `I`** is introduced for a different purpose. It represents the information available for understanding the physical system rather than another physical infrastructure by default. Depending on the specific experiment, this can include measurements, sensor availability, communication status, delays, missing observations, state-estimation outputs, and other information used to infer the condition of `P` and `T`. The distinction matters because modern power and transportation operation increasingly depend on sensing and communication, and power-grid, ICT, and e-mobility interactions can create additional pathways through which disturbances or information losses affect system operation (Mohamed, 2019). In this thesis, however, an ICT network is not automatically promoted to a third physical infrastructure layer merely because information is important. Such a network is modeled explicitly only when its physical components and connectivity are necessary to answer the research question.

The **Organizational domain `O`** represents the human and institutional capabilities that determine how information is converted into action. Relevant organizational properties can include decision authority, coordination arrangements, repair priorities, personnel and equipment availability, resource allocation, operating procedures, and response delays. This distinction is supported by infrastructure-resilience research showing that physical assets alone do not determine adaptive capacity: institutions allocate responsibilities and rights, establish constraints and incentives, and shape how infrastructure actors interpret and respond to changing conditions (Chester et al., 2021). Helmrich et al. (2021) similarly show that infrastructure resilience has both network and governance dimensions and identify information as an important mediator between them. Human–infrastructure modeling further demonstrates that resilience behavior may emerge from interaction between engineered systems and human actors rather than from physical topology alone (Rasoulkhani & Mostafavi, 2018).

The four-domain representation therefore separates several relationships that would otherwise be hidden inside a single coupled-network model. Measurements of power and transportation conditions can be represented schematically as

```math
P,T\rightarrow I,
```

information used for situational awareness and decision formation as

```math
I\rightarrow O,
```

and authorized interventions as

```math
O\rightarrow P,T.
```

These arrows represent **different engineering functions**. Observation is not control; information is not authority; authority is not physical capability; and the existence of a communication path does not guarantee that an intervention can be executed. The purpose of distinguishing `I` and `O` is therefore not to increase the number of layers, but to prevent sensing, estimation, decision-making, resource availability, and physical action from being mathematically conflated.

This produces an important ontological separation for the thesis:

```math
\boxed{
\text{physical topology}
\neq
\text{dependency}
\neq
\text{observation}
\neq
\text{decision}
\neq
\text{control action}.
}
```

Similarly, a common external hazard is not automatically an interdependency. If a flood simultaneously damages a power asset and a road segment, both components may share a common exposure without either component causing the state change of the other. Only an identifiable cross-system mechanism—such as loss of electricity disabling a transportation asset or loss of road accessibility delaying electrical repair—is represented as a directional dependency. This safeguard prevents spatial co-location and common-cause failure from being misinterpreted as causal coupling.

The study is also **service-oriented rather than purely topological**. The physical networks matter because they provide critical services: `P` supports electricity delivery and `T` supports mobility and accessibility. Consequently, a component or interface is not considered important solely because it possesses a high graph-theoretic centrality. Its engineering significance ultimately depends on how its condition affects service trajectories, feasible response, and recovery. This is consistent with coupled P–T research in which explicit interdependencies alter transportation performance and restoration feasibility rather than merely changing network connectivity (Fotouhi et al., 2017; Fan et al., 2024).

Coupled power–transportation modeling is already an established research area. Prior work has quantified resilience in traffic–electric-power systems, reviewed joint transportation–distribution-system models, examined EV charging as an explicit cross-system coupling mechanism, and represented transportation accessibility in post-disaster restoration (Fotouhi et al., 2017; Wei et al., 2019; Unterluggauer et al., 2022; Fan et al., 2024). Therefore, the scientific premise of this thesis is **not** that power and transportation have never been modeled jointly. Instead, the thesis begins from an evidence-qualified `P–T` physical core and makes `I` and `O` explicit so that subsequent chapters can distinguish **what exists, why a dependency operates, how it evolves, what can be observed, and what actions are physically and organizationally feasible**.

Accordingly, the system context established in this section can be summarized as

```math
\boxed{
\underbrace{P+T}_{\text{physical infrastructure}}
\quad
\overset{\text{observation, information, authority and resources}}{\longleftrightarrow}
\quad
\underbrace{I+O}_{\text{supporting decision domains}},
}
```

with every cross-domain relation subject to evidence and mechanism qualification. This bounded system definition provides the foundation for Section 1.3, which moves from **what constitutes the study system** to the specific engineering problem created by the need to connect structure, causal mechanisms, dynamic propagation, observation, feasible action, and service recovery without treating these distinct concepts as interchangeable.

### References cited in Section 1.2

- Chester, M., Underwood, B. S., Allenby, B., Garcia, M., Samaras, C., Markolf, S., Sanders, K., Preston, B., & Miller, T. R. (2021). Infrastructure resilience to navigate increasingly uncertain and complex conditions in the Anthropocene. *npj Urban Sustainability, 1*, Article 4. https://doi.org/10.1038/s42949-021-00016-y
- Fan, J., He, P., Li, C., Zhao, C., & Ji, Y. (2024). A post-disaster restoration model for power-gas-transportation distribution networks considering spatial interdependency and energy hubs. *Electric Power Systems Research, 233*, 110505. https://doi.org/10.1016/j.epsr.2024.110505
- Fotouhi, H., Moryadee, S., & Miller-Hooks, E. (2017). Quantifying the resilience of an urban traffic-electric power coupled system. *Reliability Engineering & System Safety, 163*, 79–94. https://doi.org/10.1016/j.ress.2017.01.026
- Helmrich, A., Markolf, S., Li, R., Carvalhaes, T., Kim, Y., Bondank, E., Natarajan, M., Ahmad, N., & Chester, M. (2021). Centralization and decentralization for resilient infrastructure and complexity. *Environmental Research: Infrastructure and Sustainability, 1*(2), 021001. https://doi.org/10.1088/2634-4505/ac0a4f
- Kivelä, M., Arenas, A., Barthelemy, M., Gleeson, J. P., Moreno, Y., & Porter, M. A. (2014). Multilayer networks. *Journal of Complex Networks, 2*(3), 203–271. https://doi.org/10.1093/comnet/cnu016
- Mohamed, A. A. A. (2019). On the rising interdependency between the power grid, ICT network, and e-mobility: Modeling and analysis. *Energies, 12*(10), 1874. https://doi.org/10.3390/en12101874
- Rasoulkhani, K., & Mostafavi, A. (2018). Resilience as an emergent property of human-infrastructure dynamics: A multi-agent simulation model for characterizing regime shifts and tipping point behaviors in infrastructure systems. *PLOS ONE, 13*(11), e0207674. https://doi.org/10.1371/journal.pone.0207674
- Rinaldi, S. M., Peerenboom, J. P., & Kelly, T. K. (2001). Identifying, understanding, and analyzing critical infrastructure interdependencies. *IEEE Control Systems Magazine, 21*(6), 11–25. https://doi.org/10.1109/37.969131
- Unterluggauer, T., Rich, J., Andersen, P. B., & Hashemi, S. (2022). Electric vehicle charging infrastructure planning for integrated transportation and power distribution networks: A review. *eTransportation, 12*, 100163. https://doi.org/10.1016/j.etran.2022.100163
- Wei, W., Wu, D., Wu, Q., Shafie-khah, M., & Catalão, J. P. S. (2019). Interdependence between transportation system and power distribution system: A comprehensive review on models and applications. *Journal of Modern Power Systems and Clean Energy, 7*, 433–448. https://doi.org/10.1007/s40565-019-0516-7

### Scientific boundary of Section 1.2

This section establishes only

```math
\boxed{
\text{system boundary}
\rightarrow
\text{domain roles}
\rightarrow
\text{directional relations}
\rightarrow
\text{service meaning}
\rightarrow
\text{causal safeguards}.
}
```

It does **not** claim a literature gap, novelty, model superiority, or validated benefit of the `P–T–I–O` representation. Those claims belong to Sections 1.3–1.4 and later hypothesis testing.

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
