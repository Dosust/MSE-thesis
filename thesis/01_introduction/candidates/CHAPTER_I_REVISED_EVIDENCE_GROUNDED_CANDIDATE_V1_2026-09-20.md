# Chapter 1 — Introduction: Research Problem and Scientific Contract

**Status:** EVIDENCE-GROUNDED CANDIDATE v1 — not yet the frozen canonical Chapter I  
**Date:** 2026-09-20  
**Citation standard:** APA 7 author–date  
**Evidence rule:** External scientific claims receive adjacent qualified citations. Thesis-defined scope, research questions, objectives, hypotheses, proposed constructs, and derivations are not cited merely for appearance.  
**Governance note:** The revised GO/RQ/SO/H wording in Sections 1.8–1.11 remains a candidate research-contract revision until a formal authority amendment is approved.

## 1.1 Background and Engineering Context

The electrification of transportation is increasing the operational interaction between electric-power and transportation infrastructures. Mobility increasingly depends on electricity through electric-vehicle charging, electrified fleets, traffic-control functions, and other electrically dependent transportation services. Charging demand and, where available, vehicle-to-grid operation can in turn affect power-system operation. Transportation infrastructure also supports power-system recovery by enabling access for repair crews, equipment, replacement components, mobile generators, storage resources, and other restoration assets (Fan et al., 2024; Unterluggauer et al., 2022; Wang et al., 2026; Wei et al., 2019).

These interactions matter because power and transportation infrastructures do not exist only as physical networks. Their engineering purpose is to provide services. The power system supports electricity service, while the transportation system supports mobility and physical accessibility. A disruption is therefore important not simply because an asset fails, but because that failure may reduce the service available to users or constrain the operation and recovery of another infrastructure system. This service-centered interpretation is consistent with a System-of-Systems view in which infrastructure systems retain their own physical identity while interacting to support broader societal functions (Hall et al., 2016).

Power and Transportation remain distinct systems. The power system has electrical-network physics, electrical states, operating constraints, control actions, and electricity-service requirements. The transportation system has road and mobility-network structure, traffic and accessibility states, route constraints, transportation controls, and mobility-service requirements. Their interaction does not remove these differences. Instead, the interaction creates interfaces through which the state or operation of one system may influence the other (Hall et al., 2016; Ibáñez et al., 2010).

The direction of that influence matters. Electricity availability may affect charging, traffic-control functions, or other electrically dependent transportation services. Transportation conditions may affect power-system restoration by changing whether repair crews and equipment can reach failed assets. Charging activity or mobile electrical resources may also influence electrical demand or available flexibility (Fan et al., 2024; Fotouhi et al., 2017; Unterluggauer et al., 2022; Wang et al., 2026). These mechanisms are not interchangeable:

```math
P\rightarrow T \qquad\text{and}\qquad T\rightarrow P
```

must be established independently.

A relation in one direction does not prove a relation in the other. Each dependency may have its own mechanism, activation condition, magnitude, delay, timescale, uncertainty, and validity domain. Reciprocal interdependence should therefore be used only when relevant dependencies in both directions are sufficiently supported (Ouyang, 2014; Rinaldi et al., 2001).

This thesis uses two complementary views of the coupled infrastructure. The **System-of-Systems view is used primarily to describe its architecture**: Power and Transportation remain distinct constituent systems but interact through explicit interfaces and dependencies. The **complex-dynamical-systems view is used primarily to describe its behavior**: disturbances, controls, feedback, delays, recovery processes, and changing operating conditions can produce behavior that evolves across both space and time (Maier, 1998; Ouyang, 2014; Rinaldi et al., 2001). This architecture–behavior distinction is a **thesis modeling convention adopted for analytical clarity**, not a universal definition separating System-of-Systems and complex-system concepts.

The distinction is important. Knowing that two infrastructures are connected does not determine how they will behave during disruption. Knowing that a physical dependency exists does not determine whether it has a significant dynamic effect. Observing service loss does not determine whether acceptable service could have been maintained or recovered. These unanswered transitions define the engineering problem addressed by this thesis.

---

# 1.2 Coupled Power–Transportation System Context

The physical core of the research consists of Power and Transportation:

```math
P+T.
```

They are modeled as distinct constituent infrastructure systems before their interactions are represented. Their physical states, operating rules, controls, failure processes, and service functions remain system-specific.

Two additional domains affect how this physical system can be understood and managed: **Information** and **Organization**. The resulting thesis representation is therefore organized around `P`, `T`, `I`, and `O`, but these four objects do not have the same physical meaning.

The Information domain represents the processes through which the physical system becomes observable and interpretable. It includes measurements, communication, information availability, information delay, and state estimation where these are required by the model. The Organizational domain represents conditions that determine which technically possible actions can actually be carried out. These may include authority, coordination, personnel, operational priorities, resource availability, and other constraints on feasible action (Chester et al., 2021; Helmrich et al., 2021; Rasoulkhani & Mostafavi, 2018; Rydén Sonesson et al., 2021).

Power and Transportation are therefore the physical constituent systems, while Information and Organization support knowledge and action:

```math
P+T=\text{physical core}, \qquad I+O=\text{supporting domains}.
```

This separation prevents information or organizational conditions from being treated as additional physical infrastructures merely because they affect physical-system behavior.

The research also distinguishes several types of relationship. Two assets may be located near each other without depending on each other. Two system quantities may change together because they are exposed to the same hazard rather than because one causes the other to change. A network connection may provide a possible pathway without establishing a functional dependency (Kivelä et al., 2014; Ouyang, 2014; Rinaldi et al., 2001).

For this reason, structural connection, observed association, causal dependency, and dynamic coupling are treated as different scientific objects. A directional dependency is admitted only when a mechanism explains how a change in one system can produce a consequential change in the other under specified conditions.

Common hazard exposure is treated separately. For example, a flood may simultaneously affect a substation and a road because both lie within the same flooded area. This is a common-cause effect rather than, by itself, a cross-system dependency. A dependency arises only when the resulting condition of one infrastructure subsequently influences the other, such as when an inaccessible road delays repair of an electrical component (Fan et al., 2024; Ouyang, 2014; Rinaldi et al., 2001).

The thesis therefore proceeds from possible interaction to qualified interaction rather than assuming that every interface is causal. A candidate relation may first be identified structurally. Its physical mechanism must then be supported. If its magnitude is required by the dynamic model, that magnitude must also be sufficiently identified or otherwise defensibly parameterized before the relation is used quantitatively.

Mechanisms introduced in Chapter 1 should therefore be understood as **mechanism families**, not as automatically active case-specific couplings. The presence of electric vehicles, charging stations, roads, substations, or repair crews does not by itself prove that a particular dependency is active in a selected case or that its strength is known.

This distinction creates the first major scientific transition of the thesis:

```math
\text{possible interaction} \rightarrow \text{qualified directional dependency} \rightarrow \text{dynamic coupling}.
```

The purpose of the later framework and methodology is to control this transition explicitly.

---

# 1.3 Problem Statement

The central problem addressed by this thesis is not the absence of power-system models, transportation models, infrastructure-interdependency models, resilience metrics, viability/reachability methods, or engineering-decision methods. These already exist in established research areas (Doyen & De Lara, 2010; Ouyang, 2014; Poulin & Kane, 2021; Tong et al., 2025; Vinod & Oishi, 2021; Wei et al., 2019). The problem lies in connecting them without making stronger claims than the available evidence supports.

A network representation can show where interaction may occur, but structure alone does not establish causality. A physical mechanism may be credible, but its magnitude may still be unknown. A dynamic model may generate realistic trajectories, but those trajectories do not show whether the required parameters are identifiable from available observations. A physical response may be technically possible but unavailable in practice because information, authority, coordination, personnel, or resources are insufficient (Chester et al., 2021; Helmrich et al., 2021; Rasoulkhani & Mostafavi, 2018; Rydén Sonesson et al., 2021).

The thesis therefore distinguishes three questions that are often treated as if they were equivalent:

```math
\text{Does the mechanism exist?} \neq \text{Can its magnitude be identified?} \neq \text{Can its magnitude be estimated reliably?}
```

A physically credible dependency may therefore remain unsuitable for quantitative simulation if the information required to specify its dynamic effect is unavailable or too uncertain. Measurement, identification, estimation, simulation, and validation are consequently treated as distinct tasks; successful simulation does not by itself establish adequacy for a real-system context of use.

The same discipline applies to resilience. A service trajectory can show degradation and recovery, but it does not fully answer whether required service could have remained acceptable during the disturbance. If service becomes unacceptable, the trajectory alone does not establish whether an acceptable state is reachable under feasible actions. Nor does it express how confident the engineer should be in those conclusions when important quantities remain uncertain.

Resilience in this thesis therefore concerns both maintaining and recovering acceptable electricity and mobility services under feasible actions and uncertainty. Conventional service and recovery curves remain useful descriptive benchmarks, while viability and reachability address different prospective questions about remaining within or returning to acceptable conditions (Béné & Doyen, 2018; Doyen & De Lara, 2010; Poulin & Kane, 2021; Trucco & Petrenj, 2023; Vinod & Oishi, 2021).

A further problem appears once interventions are introduced. An intervention that improves resilience is not automatically resource-efficient, environmentally preferable, or feasible. Different interventions may produce similar resilience benefits while requiring different levels of expenditure, operational energy, personnel, or carbon emissions; prior infrastructure studies demonstrate that resilience, cost, and greenhouse-gas objectives can create material trade-offs (Mitoulis et al., 2023; Sun et al., 2025; Zou & Chen, 2019). Engineering decisions must therefore evaluate more than resilience improvement alone.

The full problem can be expressed as one end-to-end scientific question:

```math
\boxed{ \begin{aligned} &\text{How can a bounded Power--Transportation system be represented,}\\ &\text{its directional dependencies qualified, their dynamic effects modeled,}\\ &\text{its observable and feasible responses established, its ability to remain}\\ &\text{or recover acceptable services assessed under uncertainty, and the}\\ &\text{consequences of engineering interventions translated into defensible decisions?} \end{aligned} }
```

The central scientific difficulty is therefore not one isolated mathematical method. It is the reliability of the handoffs between structure, causality, dynamics, knowledge, action, resilience, intervention, and decision.

---

# 1.4 Research Gap

The thesis does not assume that existing research lacks the individual methods required for coupled-infrastructure analysis. Network models, interdependency models, dynamic simulation, resilience curves, viability/reachability methods, optimization, and decision analysis all have established literatures (Doyen & De Lara, 2010; Ouyang, 2014; Poulin & Kane, 2021; Tong et al., 2025; Vinod & Oishi, 2021). The research gap instead concerns how these components are connected, qualified, compared, and validated for coupled Power–Transportation resilience within the bounded thesis domain.

The first gap concerns the movement from **structure to causality**. Multilayer graphs and spatial representations can encode multiple relationship types and identify candidate interactions, while infrastructure-interdependency frameworks distinguish such structural or geographic relationships from mechanisms through which one system actually affects another (Kivelä et al., 2014; Ouyang, 2014; Rinaldi et al., 2001). The unresolved thesis question is which candidate relations can be admitted as evidence-qualified directional mechanisms and under what conditions.

The second gap concerns the movement from **causal mechanism to dynamic consequence**. Dynamic coupled P–T models already exist for traffic–power resilience, charging interactions, and resilience-oriented planning (Fotouhi et al., 2017; Wang et al., 2026; Wen et al., 2025). The unresolved thesis handoff is whether an evidence-qualified dynamic representation provides measurable incremental information relative to matched independent or static-coupling representations for service loss, propagation, cascade behavior, or recovery.

The third gap concerns the movement from **physical dynamics to knowledge and feasible action**. A physical state is different from a measurement of that state, and a measurement is different from an estimated state. Even an accurate estimate does not guarantee that the required action is organizationally available. Infrastructure-resilience research shows that information, governance, coordination, human actors, and resource availability can affect response and adaptation (Chester et al., 2021; Helmrich et al., 2021; Rasoulkhani & Mostafavi, 2018; Rydén Sonesson et al., 2021). The unresolved thesis handoff is how these conditions alter feasible response and downstream recovery under matched physical conditions.

The fourth gap concerns the movement from **service trajectories to resilience information**. Conventional performance and recovery curves summarize degradation and recovery but their meaning depends on the chosen performance variable, threshold, horizon, and aggregation rule (Poulin & Kane, 2021; Trucco & Petrenj, 2023). Viability and reachability theory provide different prospective constructs for remaining within constraints or reaching acceptable target conditions under admissible actions and uncertainty (Béné & Doyen, 2018; Doyen & De Lara, 2010; Vinod & Oishi, 2021). The unresolved thesis handoff is whether adding that information produces measurable predictive or decision value beyond the conventional benchmark.

The fifth gap concerns the movement from **resilience diagnosis to intervention evaluation**. Infrastructure studies already show that resilience-oriented alternatives can involve cost, energy, emissions, and other trade-offs rather than a single aligned objective (Mitoulis et al., 2023; Sun et al., 2025; Zou & Chen, 2019). The unresolved thesis handoff is therefore whether resilience-effective candidate interventions differ materially in resource requirements, resource efficiency, feasibility, or admitted sustainability consequences under common accounting and uncertainty rules.

The sixth gap concerns the movement from **intervention consequences to engineering decision**. Multiobjective infrastructure studies and resilience reviews emphasize trade-offs among performance, cost, emissions, and other objectives rather than assuming that one-dimensional improvement determines the engineering choice (Mitoulis et al., 2023; Sun et al., 2025; Tong et al., 2025). The unresolved thesis handoff is whether adding admitted resource and sustainability consequences to resilience-based evaluation materially changes the admissible or nondominated decision set, dominance relations, or regret within the declared uncertainty domain.

These six gaps form a connected research problem:

```math
\boxed{ \text{Structure} \rightarrow \text{Causality} \rightarrow \text{Dynamics} \rightarrow \text{Knowledge and Action} \rightarrow \text{Resilience} \rightarrow \text{Intervention Consequences} \rightarrow \text{Decision}. }
```

Identification operates across this chain rather than forming an additional stage. Wherever an unknown quantity must be inferred from observations, the thesis must establish whether that quantity is identifiable and whether its estimation is adequate for the claim being made.

The contribution sought by the research therefore lies not in claiming that the component methods are absent, but in constructing and testing a controlled scientific chain between them. This follows the thesis-wide principle that established components do not automatically imply established handoffs.

---

# 1.5 Sustainable Engineering Significance

The research is a Sustainable Engineering problem because engineering actions used to preserve or restore infrastructure services consume resources and can create environmental or distributional consequences. Resilience and sustainability therefore need not move in the same direction, and infrastructure-recovery studies have documented trade-offs among resilience, cost, and greenhouse-gas outcomes (Chester et al., 2021; Mitoulis et al., 2023).

Four concepts are kept separate throughout the thesis: **resilience effect, intervention effectiveness, resource efficiency, and sustainability consequence**.

A resilience effect describes how an intervention changes the system's ability to maintain or recover required service. Effectiveness asks whether the intervention achieves its declared engineering objective. Resource efficiency considers how much resource is required to obtain that effect. Sustainability consequences describe qualified effects that fall within the declared sustainability accounting boundary.

The planned core resource quantities are direct intervention or recovery cost and operational electrical energy. They are treated as resources rather than being combined into a generic sustainability score.

The principal planned environmental sustainability quantity is carbon-dioxide-equivalent emissions within the qualified operational or partial accounting boundary. Distributional accessibility may be included when its construct, population, opportunity definition, data, and accounting boundary are sufficiently supported.

The quantitative scope therefore does not imply a complete life-cycle sustainability assessment. Embodied emissions, biodiversity, water, public health, macroeconomic consequences, and broad social-sustainability indices remain outside the present confirmatory core unless they are introduced through a formal scope change.

This boundary allows the research to ask a focused engineering question: if two interventions improve resilience, do they require different resources or create different admitted sustainability consequences?

That comparison is important because resilience-oriented alternatives can involve material trade-offs among recovery performance, investment or operating cost, energy use, and carbon emissions (Mitoulis et al., 2023; Sun et al., 2025; Zou & Chen, 2019). The thesis therefore keeps these dimensions visible rather than collapsing them prematurely into one score.

The thesis therefore evaluates resilience and sustainability as related but distinct dimensions of engineering performance.

---

# 1.6 Scope, Boundaries, Assumptions, and Validity Domain

The thesis is intentionally bounded. Its conclusions apply only to the systems, mechanisms, service requirements, hazards, control assumptions, intervention classes, accounting boundaries, and uncertainty conditions for which adequate evidence is established.

The physical scope contains Power and Transportation as the constituent infrastructure systems. Information and Organization support observation and feasible action but are not treated as additional physical infrastructure systems.

The service scope is centered on electricity and mobility. Physical network variables are relevant when they influence these declared services, but a network state is not automatically a service state. Service requirements are established separately from the physical state variables used to simulate the systems.

The spatial scope is determined by the geographic region in which the selected power, transportation, hazard, observation, and interface information can be aligned with sufficient provenance. Spatial overlap is necessary for some interactions but does not by itself prove dependency.

The temporal scope distinguishes data vintage, disturbance time, operational horizon, recovery horizon, and any longer-term transformation horizon. These time concepts are not treated as interchangeable.

The principal planned demonstrator hazard is flooding, subject to the hazard and data qualification established in Chapter 4. The framework itself is not claimed to represent every hazard. Hazard exposure is separated from component damage, failure, and system consequence. A hazard layer can establish where exposure occurs without establishing how a component fails or how service is subsequently affected.

The action scope distinguishes operational or recovery control from persistent engineering intervention. Operational actions act on the existing system, while interventions may change infrastructure structure, capacity, resources, or other persistent properties.

The resource and sustainability scope follows Section 1.5. Cost and operational energy are treated as resource quantities. Qualified carbon-dioxide-equivalent emissions form the principal environmental sustainability consequence, while distributional accessibility remains conditional.

The thesis also separates the scientific domain from the particular datasets or cases used during model development and confirmatory analysis. Development testbeds can be used to verify implementation, explore mechanisms, or qualify methods, but they do not automatically define the final validation domain. The final confirmatory case, datasets, provenance, spatial and temporal alignment, parameter readiness, and execution conditions are therefore established in Chapter 4 rather than fixed in the Introduction. This separation is specifically intended to prevent the case from determining the scientific architecture after the fact.

The conclusions of the thesis are consequently limited by a declared validity domain. Claims made outside that domain require additional evidence rather than extrapolation by assumption.

A final boundary concerns uncertainty. Sources of uncertainty may include hazards, dependency mechanisms, model structure, parameter values, observations, interventions, resource quantities, and accounting assumptions. Probabilistic treatment is used only where probabilities can be justified. Otherwise, robust bounds, scenarios, sensitivity analysis, or other non-probabilistic descriptions are used.

The governing rule is simple:

> **The strength of a thesis claim cannot exceed the strength of the evidence supporting it.**

---

# 1.7 Research Framework and Scientific Logic

The thesis is organized around seven connected scientific stages.

### Stage 1 — Spatiotemporal System-of-Systems Structure

Stage 1 defines the physical systems, services, states, geography, candidate interfaces, and supporting information and organizational domains. Its purpose is to determine what exists, where interaction may occur, and which relationships are structurally admissible.

Stage 1 is not causal. Its output consists of candidate relations requiring further qualification.

### Stage 2 — Evidence-Qualified Directional Dependencies

Stage 2 asks why one system affects another. Candidate relations are evaluated through their direction, physical mechanism, activation conditions, evidence, uncertainty, and validity boundaries.

A mechanism may be accepted conceptually without yet being ready for dynamic simulation. Causal acceptance and numerical readiness therefore remain separate.

### Stage 3 — Physics-Based Hybrid Dynamics

Stage 3 introduces dynamically ready mechanisms into the physical models of Power and Transportation. Each constituent system retains its native physics, while accepted interface mechanisms provide cross-system coupling.

The purpose is not simply to generate trajectories but to test whether dynamic coupling adds meaningful information relative to simpler representations.

### Stage 4 — Observation, Estimation, Organization, and Control

Stage 4 connects physical reality to feasible action. It distinguishes the physical state from measurements and estimated states and then considers how information and organizational conditions affect the actions available to operators.

The essential chain is:

```math
\text{physical state} \rightarrow \text{observation} \rightarrow \text{estimated state} \rightarrow \text{feasible action}.
```

### Stage 5 — Viability, Reachability, and Confidence

Stage 5 asks three questions:

**Can required electricity and mobility services remain acceptable during disruption?**

**If they cannot remain acceptable, can acceptable service be recovered under feasible actions?**

**How strongly can either conclusion be supported under uncertainty?**

Viability addresses remaining within acceptable conditions. Reachability addresses return to acceptable conditions. Confidence is represented probabilistically only where justified; otherwise robustness or scenario coverage is used.

### Stage 6 — Intervention, Resource, and Sustainability Consequences

Stage 6 uses resilience diagnosis to **inform the identification and comparison** of candidate engineering interventions. Each intervention is evaluated through its resilience effect, effectiveness, resource requirements and efficiency, and admitted sustainability consequences.

This stage deliberately preserves the distinction between improving resilience and obtaining that improvement efficiently or sustainably.

### Stage 7 — Engineering Decision and Transformation

Stage 7 evaluates which candidate interventions remain defensible when requirements, resilience, resource use, sustainability consequences, feasibility, and uncertainty are considered jointly.

The default decision structure is multiobjective rather than an arbitrary weighted sustainability score. Requirement screening, feasible alternatives, nondominance, robustness, and regret may therefore be used to support the final comparison. Sequential intervention planning is considered only when the available temporal evidence and validation justify it.

The complete research logic is:

```math
\boxed{ \begin{aligned} &\text{Critical service need}\\ &\rightarrow \text{bounded P--T structure}\\ &\rightarrow \text{qualified directional dependencies}\\ &\rightarrow \text{physics-based coupled dynamics}\\ &\rightarrow \text{observation and feasible action}\\ &\rightarrow \text{remain, recover, and confidence}\\ &\rightarrow \text{intervention, resources, and sustainability consequences}\\ &\rightarrow \text{defensible engineering decision}. \end{aligned} }
```

Evidence qualification, identification, verification, validation, uncertainty analysis, and traceability operate across these stages. They are scientific controls on the framework, not additional infrastructure layers or an eighth research stage.

---

# 1.8 General Research Objective

The general objective of this thesis is:

> **To develop and validate an evidence-grounded mathematical and engineering framework for coupled Power–Transportation infrastructure that connects System-of-Systems structure and qualified directional interdependencies to spatiotemporal dynamics, observation, information and organizational constraints, feasible control, uncertainty-aware service viability and recovery, engineering intervention consequences, and defensible engineering decisions. Engineering interventions are evaluated through their resilience effects, resource requirements and efficiency, and admitted sustainability consequences.**

This objective gives the thesis one end-to-end scientific direction:

```math
\boxed{ \text{Structure} \rightarrow \text{Interdependencies} \rightarrow \text{Dynamics} \rightarrow \text{Knowledge and Action} \rightarrow \text{Resilience} \rightarrow \text{Intervention Consequences} \rightarrow \text{Decision}. }
```

---

# 1.9 Research Questions

The overarching research question is:

### RQ0 — Overarching Research Question

> **How can coupled Power–Transportation infrastructure be represented as an interdependent System of Systems and modeled as a spatiotemporal complex dynamical system to connect qualified directional dependencies, feasible response, uncertainty-aware service resilience, engineering intervention consequences, and defensible engineering decisions?**

The overarching question is decomposed into seven research questions.

### RQ1 — System Structure

> **What systems, services, entities, states, locations, and candidate interfaces constitute the bounded Power–Transportation System of Systems?**

RQ1 establishes what exists and where interaction can occur.

### RQ2 — Directional Causal Dependencies

> **Which candidate relations can be admitted as evidence-qualified directional dependency mechanisms, through what physical mechanism, and under what conditions?**

RQ2 establishes why the systems affect one another rather than assuming causality from connection or association.

### RQ3 — Coupled Dynamics

> **How do dynamically ready dependency mechanisms alter coupled physical states and electricity and mobility service trajectories relative to independent and static-coupling representations?**

RQ3 determines the additional value of representing qualified dependencies dynamically.

### RQ4 — Observation and Feasible Action

> **How do observation, state estimation, information availability, organizational conditions, and feasible control affect response and recovery?**

RQ4 connects physical-system behavior to what can be known and what can actually be done.

### RQ5 — Service Resilience

> **Under what conditions can required electricity and mobility services remain acceptable or be recovered under feasible actions and uncertainty, and what additional engineering information do viability and reachability provide beyond conventional service-recovery measures?**

RQ5 addresses remain, return, and confidence.

### RQ6 — Intervention Consequences

> **How do candidate engineering interventions differ in resilience effectiveness, resource requirements and efficiency, and admitted sustainability consequences under independently qualified requirements, declared accounting boundaries, and uncertainty?**

RQ6 does not derive sustainability requirements from resilience results. Requirements are established independently; resilience diagnosis identifies intervention needs, while intervention analysis evaluates consequences. This correction follows the systems-engineering distinction between requirements and downstream performance evidence.

### RQ7 — Engineering Decision

> **Which candidate intervention or infrastructure transformation is defensible when resilience, resource efficiency, admitted sustainability consequences, feasibility, and uncertainty are evaluated jointly, and under what conditions is sequential adaptation justified?**

RQ7 does not assume in advance that an intervention must occur or that a sequence must exist. Sequential adaptation remains conditional on evidence, temporal structure, and validation.

Together, the questions follow a single progression:

```math
\boxed{ \text{WHAT} \rightarrow \text{WHY} \rightarrow \text{HOW} \rightarrow \text{WHAT CAN BE KNOWN AND DONE} \rightarrow \text{CAN SERVICE REMAIN OR RETURN} \rightarrow \text{WHAT DOES AN INTERVENTION REQUIRE AND CAUSE} \rightarrow \text{WHAT DECISION IS DEFENSIBLE}. }
```

---

# 1.10 Specific Research Objectives

Each research question has one corresponding specific objective.

### SO1 — System Structure

> **Define the bounded Power–Transportation System of Systems in terms of its constituent systems, services, entities, states, spatial support, candidate interfaces, and Information and Organization supporting domains.**

### SO2 — Directional Causal Dependencies

> **Qualify candidate Power–Transportation relations as directional dependency mechanisms by establishing their physical mechanism, direction, activation conditions, evidence basis, uncertainty, and validity boundaries.**

### SO3 — Coupled Dynamics

> **Develop and verify a physics-based hybrid dynamic representation and test the incremental explanatory or predictive information provided by dynamically ready coupling relative to independent and static-coupling representations.**

### SO4 — Observation and Feasible Action

> **Evaluate how measurement, state estimation, information availability, organizational conditions, and feasible control affect response timing, electricity and mobility service trajectories, and recovery.**

### SO5 — Service Resilience

> **Determine uncertainty-aware service viability and recovery reachability, evaluate their incremental information beyond conventional service and recovery representations, and characterize interface criticality where the required evidence permits.**

### SO6 — Intervention Consequences

> **Quantify and compare candidate engineering interventions in terms of resilience effectiveness, resource requirements and resource efficiency, and admitted sustainability consequences within independently justified requirements and declared accounting boundaries.**

### SO7 — Engineering Decision

> **Evaluate candidate interventions or infrastructure transformations jointly in terms of resilience, resource efficiency, admitted sustainability consequences, feasibility, and uncertainty, and evaluate intervention sequences only where temporal decision structure, data, and validation support them.**

The traceability rule is:

```math
RQ_k\Longleftrightarrow SO_k, \qquad k=1,\ldots,7.
```

RQ1 and RQ2 establish the scientific objects and evidence required for the later hypothesis-bearing analysis. RQ3 through RQ7 correspond to H1 through H5.

---

# 1.11 Research Hypotheses and Test Logic

The thesis contains five primary hypotheses. RQ1 and RQ2 are scientific prerequisites rather than additional hypotheses because they establish the system representation and evidence-qualified dependency mechanisms required by later tests.

Each hypothesis is evaluated using a declared comparator, response quantity, uncertainty treatment, and non-support condition. Detailed metrics and numerical thresholds are specified before confirmatory execution in Chapter 4.

### H1 — Dynamic Causal Coupling

> **H1:** Under matched disturbances, initial conditions, service requirements, and exogenous conditions, an evidence-qualified dynamic Power–Transportation coupling representation provides meaningful incremental explanatory or predictive information for prespecified service-loss, propagation, cascade, or recovery outcomes relative to a corresponding static-coupling representation.

Three model levels are compared:

```math
M_0=\text{independent Power and Transportation systems},
```

```math
M_1=\text{static or algebraic coupling},
```

```math
M_2=\text{dynamic causal coupling}.
```

The primary comparison is `M_2` against `M_1`, with `M_0` retained as the uncoupled reference.

H1 is not supported if `M_2` does not provide the preregistered meaningful increase in explanatory, predictive, or decision-relevant information relative to `M_1` within the declared test domain.

### H2 — Information, Organization, and Feasible Control

> **H2:** Under matched physical conditions and disturbances, changes in information availability and organizational conditions produce meaningful differences in state-estimation quality, feasible action, response timing, service trajectories, recovery, or downstream resilience outcomes.

The comparison considers a physical Power–Transportation representation, the same physical system with declared information conditions, and the same system with declared information and organizational conditions.

These are **matched experimental contrasts associated with modeled information and organizational conditions**. They are not interpreted automatically as identified real-world causal effects.

H2 is not supported if the prespecified contrasts fail to produce the required meaningful difference in the declared outcomes.

### H3 — Viability and Recovery-Reachability Information

> **H3:** For the declared Power–Transportation test domain, uncertainty-aware viability and recovery-reachability information provides meaningful incremental predictive or decision-relevant information about future service maintainability and acceptable recovery beyond prespecified conventional service and recovery-curve measures.

The comparison is between conventional service/recovery information and the same information augmented by the Stage-5 resilience representation.

H3 is not supported if the addition of viability, reachability, and uncertainty information does not improve the preregistered predictive or decision criterion by the declared meaningful amount.

### H4 — Intervention, Resource, and Sustainability Consequences

> **H4:** Across the prespecified intervention and scenario set, at least two resilience-effective engineering interventions produce materially different resource requirements, resource efficiencies, or admitted sustainability consequences under the declared comparison rule.

The intervention comparison maintains separate quantities for resilience effect, resources, and sustainability consequences. Core resource quantities include qualified direct cost and operational energy; the principal environmental consequence is qualified `CO_{2e}`. Distributional accessibility and other extensions are included only if their construct and data requirements are satisfied.

H4 is not supported when sufficient qualified alternatives and admitted consequence quantities exist but no material difference is found under the preregistered comparison rule. If the required objects cannot be qualified, H4 remains **NOT TESTED**.

### H5 — Joint Engineering Decision

> **H5:** Under the declared uncertainty domain, incorporating resource efficiency and admitted sustainability consequences together with feasibility and uncertainty materially changes the admissible or nondominated engineering decision set, dominance relations, or decision regret relative to resilience-only evaluation.

The decision analysis remains multiobjective. A universal weighted sustainability score is not assumed unless an independent basis exists for the required weights.

H5 is not supported if the admitted additional information does not materially change the declared decision criterion. If the necessary inputs remain unqualified, H5 remains **NOT TESTED**.

The five confirmatory relationships are therefore:

```math
RQ_3/SO_3\rightarrow H_1, \quad RQ_4/SO_4\rightarrow H_2, \quad RQ_5/SO_5\rightarrow H_3, \quad RQ_6/SO_6\rightarrow H_4, \quad RQ_7/SO_7\rightarrow H_5.
```

RQ1/SO1 and RQ2/SO2 remain prerequisites supporting the validity of H1 and the downstream stages.

---

# 1.12 Proposed Contributions

The contributions presented in this section are **proposed contributions**, not established results. They become supported contributions only when the required evidence, testing, uncertainty analysis, verification, and validation have been completed within the declared validity domain. A supported contribution is also not automatically a globally novel contribution.

### C1 — Bounded Power–Transportation System-of-Systems Representation

The thesis is intended to contribute a service-centered representation of coupled Power–Transportation infrastructure that preserves Power and Transportation as distinct physical constituent systems while representing Information and Organization as supporting domains. The representation links physical entities, services, states, spatial support, and candidate interfaces without treating structural connection as causal evidence.

### C2 — Evidence-Qualified Directional Dependency Representation

The thesis is intended to contribute a mechanism-centered treatment of Power–Transportation dependency in which candidate relations progress from structural possibility to evidence-qualified directional mechanisms and only then, when dynamically ready, to quantitative coupling.

This contribution explicitly separates common exposure, association, directional dependency, reciprocal interdependence, and dynamic coupling.

### C3 — Physics-Based Dynamic Coupling with Controlled Admission

If H1 is supported, the thesis is intended to contribute a coupled dynamic representation in which cross-system terms enter the physical model only through mechanisms that have satisfied the required evidence and numerical-readiness conditions.

The contribution therefore lies not simply in coupling two models but in controlling why and when coupling is scientifically admissible.

### C4 — Observation-, Information-, and Organization-Constrained Response

If H2 is supported, the thesis is intended to contribute an explicit representation of the path from physical state to observation, estimated state, organizationally feasible action, and recovery response.

This contribution recognizes that technically possible control is not necessarily operationally available control.

### C5 — Uncertainty-Aware Viability and Recovery Assessment

If H3 is supported, the thesis is intended to contribute a resilience assessment that augments conventional service and recovery curves with prospective information on whether required electricity and mobility services can remain acceptable, whether acceptable service can be recovered after violation, and how uncertainty affects those conclusions.

### C6 — Intervention and Engineering-Decision Evaluation

If H4 and H5 are supported, the thesis is intended to contribute an engineering evaluation that connects resilience diagnosis to intervention alternatives while keeping resilience effect, resources, resource efficiency, sustainability consequences, feasibility, and uncertainty distinct.

The final decision formulation is intended to identify defensible alternatives or nondominated sets rather than claim a universally optimal solution without a justified preference model.

The contributions therefore follow the same end-to-end structure as the research:

```math
\boxed{ \text{Representation} \rightarrow \text{Qualified Dependency} \rightarrow \text{Dynamics} \rightarrow \text{Knowledge and Feasible Action} \rightarrow \text{Resilience} \rightarrow \text{Intervention} \rightarrow \text{Decision}. }
```

The thesis does not claim novelty for the component ideas individually. System-of-Systems reasoning, infrastructure interdependency, coupled Power–Transportation modeling, EV charging and vehicle-to-grid interaction, resilience curves, viability/reachability, and multiobjective infrastructure decision methods all have established scientific foundations (Doyen & De Lara, 2010; Maier, 1998; Mitoulis et al., 2023; Ouyang, 2014; Poulin & Kane, 2021; Rinaldi et al., 2001; Unterluggauer et al., 2022; Vinod & Oishi, 2021; Wei et al., 2019). Any final novelty claim therefore depends on the specific integrated chain that is actually demonstrated and validated by the completed research and on the separate reproducible novelty audit.

---

# 1.13 Thesis Organization

The remainder of the thesis follows the scientific dependency established in Chapter 1.

**Chapter 2 — Literature Review and Scientific Foundations** examines the evidence required to support the research architecture. It covers infrastructure services, System-of-Systems concepts, directional Power–Transportation dependencies, Information and Organization, hazards and cascading behavior, measurement and identification, resilience, viability and reachability, engineering intervention, resource use, sustainability consequences, and decision-making. The chapter ends by defining the evidence-supported thesis boundary rather than claiming that the individual component methods are absent from the literature.

**Chapter 3 — Conceptual and Mathematical Framework** formalizes the scientific objects introduced in Chapter 1. It defines the Power–Transportation architecture, directional dependency representation, physics-based hybrid dynamics, observation and estimation, feasible-control structure, acceptable-service conditions, viability, recovery reachability, intervention consequences, and decision objects. It also establishes the mathematical handoffs linking the seven stages.

**Chapter 4 — Research Methodology and Experimental Design** determines how the framework is tested. It establishes evidence and source qualification, case and data admissibility, spatial and temporal alignment, measurement models, parameter identification, estimator admission, model realization, numerical verification, scenario construction, matched experimental comparisons, validation, uncertainty quantification, sensitivity analysis, falsification rules, and reproducibility. The specific development and confirmatory cases are introduced here rather than in Chapter 1.

**Chapter 5 — Results** reports the case, data, identification, verification, validation, uncertainty, and hypothesis-test results. H1–H5 are reported only when their required scientific objects and experiments are admissible. Every result is reported with its comparator, uncertainty, meaningful-effect or decision rule, and validity domain.

**Chapter 6 — Discussion and Sustainable Engineering Implications** interprets the results in relation to physical mechanisms, observations, assumptions, alternative explanations, existing literature, resilience theory, resources, sustainability consequences, engineering decisions, transferability, and remaining uncertainty.

**Chapter 7 — Conclusions and Future Work** answers RQ0 and RQ1–RQ7 at the level justified by the completed evidence, records the final status of H1–H5, identifies the contributions that are actually supported, states the validity and generalization limits of the work, and separates established findings from unresolved questions and future research.

The complete thesis argument is therefore:

```math
\boxed{ \text{Problem} \rightarrow \text{Evidence} \rightarrow \text{Mathematical Framework} \rightarrow \text{Qualified Method and Case} \rightarrow \text{Results} \rightarrow \text{Interpretation} \rightarrow \text{Engineering Conclusion}. }
```

Chapter 1 establishes the research contract for that argument. It defines what the thesis studies, why the problem matters, what remains unresolved, what will be tested, which conclusions are admissible, and where the thesis deliberately limits its claims.

This revised version also follows the writing correction identified in your review: **fewer mathematical displays, but greater scientific importance for each one**, rather than turning every conceptual distinction into a boxed equation.

---

# References cited in Chapter 1

The following list contains only sources cited in this Chapter-1 candidate. Entries follow the thesis APA 7 author–date standard. The final thesis must also contain a comprehensive reference list before the appendices.

Béné, C., & Doyen, L. (2018). From resistance to transformation: A generic metric of resilience through viability. *Earth's Future, 6*(7), 979–996. https://doi.org/10.1002/2017EF000660

Chester, M., Underwood, B. S., Allenby, B., Garcia, M., Samaras, C., Markolf, S., Sanders, K., Preston, B., & Miller, T. R. (2021). Infrastructure resilience to navigate increasingly uncertain and complex conditions in the Anthropocene. *npj Urban Sustainability, 1*, Article 4. https://doi.org/10.1038/s42949-021-00016-y

Doyen, L., & De Lara, M. (2010). Stochastic viability and dynamic programming. *Systems & Control Letters, 59*(10), 629–634. https://doi.org/10.1016/j.sysconle.2010.07.008

Fan, J., He, P., Li, C., Zhao, C., & Ji, Y. (2024). A post-disaster restoration model for power-gas-transportation distribution networks considering spatial interdependency and energy hubs. *Electric Power Systems Research, 233*, 110505. https://doi.org/10.1016/j.epsr.2024.110505

Fotouhi, H., Moryadee, S., & Miller-Hooks, E. (2017). Quantifying the resilience of an urban traffic-electric power coupled system. *Reliability Engineering & System Safety, 163*, 79–94. https://doi.org/10.1016/j.ress.2017.01.026

Hall, J. W., Nicholls, R. J., Hickford, A. J., & Tran, M. (2016). Introducing national infrastructure assessment. In J. W. Hall, M. Tran, A. J. Hickford, & R. J. Nicholls (Eds.), *The future of national infrastructure: A system-of-systems approach* (pp. 3–11). Cambridge University Press. https://doi.org/10.1017/CBO9781107588745.002

Helmrich, A., Markolf, S., Li, R., Carvalhaes, T., Kim, Y., Bondank, E., Natarajan, M., Ahmad, N., & Chester, M. (2021). Centralization and decentralization for resilient infrastructure and complexity. *Environmental Research: Infrastructure and Sustainability, 1*(2), 021001. https://doi.org/10.1088/2634-4505/ac0a4f

Ibáñez, E., Gkritza, K., McCalley, J., Aliprantis, D., Brown, R., Somani, A., & Wang, L. (2010). Interdependencies between energy and transportation systems for national long term planning. In *Sustainable and resilient critical infrastructure systems: Simulation, modeling, and intelligent engineering* (pp. 53–76). Springer. https://doi.org/10.1007/978-3-642-11405-2_2

Kivelä, M., Arenas, A., Barthelemy, M., Gleeson, J. P., Moreno, Y., & Porter, M. A. (2014). Multilayer networks. *Journal of Complex Networks, 2*(3), 203–271. https://doi.org/10.1093/comnet/cnu016

Maier, M. W. (1998). Architecting principles for systems-of-systems. *Systems Engineering, 1*(4), 267–284. https://doi.org/10.1002/(SICI)1520-6858(1998)1:4%3C267::AID-SYS3%3E3.0.CO;2-D

Mitoulis, S.-A., Bompa, D. V., & Argyroudis, S. (2023). Sustainability and climate resilience metrics and trade-offs in transport infrastructure asset recovery. *Transportation Research Part D: Transport and Environment, 121*, 103800. https://doi.org/10.1016/j.trd.2023.103800

Ouyang, M. (2014). Review on modeling and simulation of interdependent critical infrastructure systems. *Reliability Engineering & System Safety, 121*, 43–60. https://doi.org/10.1016/j.ress.2013.06.040

Poulin, C., & Kane, M. B. (2021). Infrastructure resilience curves: Performance measures and summary metrics. *Reliability Engineering & System Safety, 216*, 107926. https://doi.org/10.1016/j.ress.2021.107926

Rasoulkhani, K., & Mostafavi, A. (2018). Resilience as an emergent property of human-infrastructure dynamics: A multi-agent simulation model for characterizing regime shifts and tipping point behaviors in infrastructure systems. *PLOS ONE, 13*(11), e0207674. https://doi.org/10.1371/journal.pone.0207674

Rinaldi, S. M., Peerenboom, J. P., & Kelly, T. K. (2001). Identifying, understanding, and analyzing critical infrastructure interdependencies. *IEEE Control Systems Magazine, 21*(6), 11–25. https://doi.org/10.1109/37.969131

Rydén Sonesson, T., Johansson, J., & Cedergren, A. (2021). Governance and interdependencies of critical infrastructures: Exploring mechanisms for cross-sector resilience. *Safety Science, 142*, 105383. https://doi.org/10.1016/j.ssci.2021.105383

Sun, Y., Huang, X., Wang, G., Zhang, X., Qiu, J., & Strbac, G. (2025). Low-carbon traffic resilience-enhanced robust planning of coupled transportation and power distribution network based on modified user equilibrium model. *Applied Energy, 397*, 126258. https://doi.org/10.1016/j.apenergy.2025.126258

Tong, W., Li, H. X., Nasirzadeh, F., Yao, F., & Ji, Y. (2025). Resilience of interdependent infrastructure networks: Review and future directions. *International Journal of Critical Infrastructure Protection, 51*, 100793. https://doi.org/10.1016/j.ijcip.2025.100793

Trucco, P., & Petrenj, B. (2023). Characterisation of resilience metrics in full-scale applications to interdependent infrastructure systems. *Reliability Engineering & System Safety, 235*, 109200. https://doi.org/10.1016/j.ress.2023.109200

Unterluggauer, T., Rich, J., Andersen, P. B., & Hashemi, S. (2022). Electric vehicle charging infrastructure planning for integrated transportation and power distribution networks: A review. *eTransportation, 12*, 100163. https://doi.org/10.1016/j.etran.2022.100163

Vinod, A. P., & Oishi, M. M. K. (2021). Stochastic reachability of a target tube: Theory and computation. *Automatica, 125*, 109458. https://doi.org/10.1016/j.automatica.2020.109458

Wang, S., Lu, Q.-C., Liu, L., Xu, P.-C., Wang, R., & Zhang, L. (2026). Interdependency analysis of coupled power and transportation networks considering the charging decision preferences of EV drivers. *Reliability Engineering & System Safety, 268*, 112005. https://doi.org/10.1016/j.ress.2025.112005

Wei, W., Wu, D., Wu, Q., Shafie-khah, M., & Catalão, J. P. S. (2019). Interdependence between transportation system and power distribution system: A comprehensive review on models and applications. *Journal of Modern Power Systems and Clean Energy, 7*, 433–448. https://doi.org/10.1007/s40565-019-0516-7

Wen, J., Gan, W., Chu, C.-C., Jiang, L., & Luo, J. (2025). Robust resilience enhancement by EV charging infrastructure planning in coupled power distribution and transportation systems. *IEEE Transactions on Smart Grid, 16*(1), 491–504. https://doi.org/10.1109/TSG.2024.3390657

Zou, Q., & Chen, S. (2019). Enhancing resilience of interdependent traffic-electric power system. *Reliability Engineering & System Safety, 191*, 106557. https://doi.org/10.1016/j.ress.2019.106557
