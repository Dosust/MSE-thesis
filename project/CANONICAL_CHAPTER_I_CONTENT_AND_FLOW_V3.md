# Chapter 1 — Introduction: Research Problem and Scientific Contract

> **ACTIVE THERMAL-SCOPE SUPERSESSION NOTICE — 2026-10-07**
> This file is retained for historical/provenance purposes. It does **not** control the active thesis where it conflicts with `CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md`, `CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V3.md`, and `CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md`.
> The active thesis studies only thermal Power–Electrified Transportation interdependencies and their consequences through physical state and time.


**Canonical thesis title:** **Physics-Based Mathematical Engineering of Power–Transportation Interdependencies for Resilience**  
**Title authority:** `CANONICAL_THESIS_TITLE_V1.md`

## 1.1 Background and Engineering Context

Electricity and mobility are critical infrastructure services. Their provision depends on distinct physical systems, but transportation electrification is increasing the number and importance of interfaces between electric-power and transportation infrastructures. Electric-vehicle charging connects mobility demand to the location, timing, capacity, and availability of electricity supply, while charging demand can affect distribution-system operation and planning. Vehicle-to-grid and mobile-energy applications create additional pathways through which transportation resources may interact with the power system when the required technical and operating conditions are present (Oladigbolu et al., 2025; Unterluggauer et al., 2022; Wei et al., 2019).

The interaction extends beyond normal operation. Power-system restoration depends on physical access for repair crews, equipment, replacement components, mobile generators, and other restoration resources. Transportation disruption can therefore constrain access to damaged electrical assets and alter restoration timing (Fan et al., 2024; Lian et al., 2026).

The engineering significance of these infrastructures follows from the services they provide rather than from their assets alone. The power system provides electricity service, whereas the transportation system provides mobility and physical accessibility. A disruption becomes consequential when it reduces one of these services or constrains the operation or recovery of the other system. This service-centered interpretation is consistent with infrastructure System-of-Systems reasoning, in which constituent systems retain their identities while contributing to broader service functions (Hall et al., 2016).

Power and Transportation nevertheless remain physically distinct systems. Power networks obey electrical laws, operating constraints, and electrical-control requirements. Transportation networks represent roads, traffic, routing, accessibility, mobility demand, and transportation-control processes. Their interaction does not require their native physical descriptions to be replaced by one homogeneous network. Integrated energy–transport studies instead show that distinct systems can remain separately represented while selected states, flows, constraints, or decisions are coupled (Ibáñez et al., 2010).

Directionality is therefore fundamental. Electricity availability can affect charging infrastructure and other electrically dependent transportation functions. Transportation availability can affect repair access and power-system restoration. Charging behavior and mobile electrical resources can create additional Transportation-to-Power effects under appropriate operating conditions (Fan et al., 2024; Fotouhi et al., 2017; Wang et al., 2026).

For this thesis,

```math
\boxed{ P\rightarrow T \not\Rightarrow T\rightarrow P }
```

because evidence of a dependency in one direction does not establish a dependency in the reverse direction. Each direction can have a different mechanism, activation condition, magnitude, delay, characteristic timescale, uncertainty, and validity domain.

Structural proximity must also be distinguished from functional dependency. Two assets can be exposed simultaneously to the same flood without either asset causing the state change of the other. Common exposure can therefore generate correlated disruption without establishing a cross-system directional dependency (Ouyang, 2014; Rinaldi et al., 2001).

Two complementary perspectives are used to represent the resulting coupled infrastructure. The **System-of-Systems perspective** describes architecture: constituent systems, services, entities, interfaces, and relations. The **complex-dynamical-systems perspective** describes behavior: how physical states, disturbances, dependencies, feedback, controls, delays, and recovery processes evolve through space and time. Systems-of-systems theory emphasizes the continued identity of constituent systems within a larger architecture, whereas infrastructure-interdependency research shows that cross-system interaction can produce behavior that isolated-system analysis does not represent (Maier, 1998; Ouyang, 2014; Rinaldi et al., 2001).

For analytical clarity, this thesis adopts the modeling convention

```math
\boxed{ \text{System of Systems} = \text{architectural view}, \qquad \text{complex dynamical system} = \text{behavioral view}. }
```

This convention is specific to the thesis and is not presented as a universal separation between the two concepts.

The engineering problem therefore extends beyond determining whether Power and Transportation are connected. It requires establishing which cross-system relations are scientifically admissible as directional dependencies, what those dependencies do dynamically, what operators can observe and feasibly do while the system evolves, whether required services can remain acceptable or recover, and how intervention consequences affect the final engineering decision.

---

## 1.2 Coupled Power–Transportation System Context

The physical infrastructure core of the thesis is

```math
\boxed{P+T},
```

where `P` denotes the Power system and `T` denotes the Transportation system.

Information and Organization are supporting domains:

```math
\boxed{I+O}.
```

This is a thesis-specific ontology. It does not imply that `P`, `T`, `I`, and `O` are four equivalent physical infrastructures.

Power and Transportation are the constituent physical systems because they contain the assets, connections, states, controls, failure processes, and service functions required to provide electricity and mobility. They remain separately represented so that coupling does not erase system-specific physics, topology, or operational logic (Hall et al., 2016; Ibáñez et al., 2010).

The **Information domain** represents what can be measured, communicated, or estimated about the physical system. Depending on the experiment, this can include measurement availability, communication status, missing observations, delays, forecasts, and state estimates. Information availability does not by itself establish that a technically possible physical action can be executed (Mohamed, 2019; Rinaldi et al., 2001).

The **Organizational domain** represents conditions through which information becomes feasible action. Relevant conditions can include authority, coordination, priorities, personnel, equipment, resource availability, and response delay. Infrastructure-resilience research shows that human and institutional conditions can materially affect response and adaptation (Chester et al., 2021; Helmrich et al., 2021; Rasoulkhani & Mostafavi, 2018).

The working representation is therefore

```math
\boxed{ \underbrace{P+T}_{\text{physical infrastructure}} + \underbrace{I+O}_{\text{knowledge and feasible-action support}}. }
```

This ontology requires a strict relationship taxonomy.

A **structural relation** identifies where interaction could occur.

A **directional dependency** requires an interpretable physical or operational mechanism through which a source affects a receiver under specified conditions.

A reciprocal **interdependency** requires relevant directional dependencies in both directions.

**Dynamic coupling** requires an additional step: the qualified directional mechanism must be specified sufficiently to enter the governing dynamic model.

The progression is therefore

```math
\boxed{ \text{candidate relation} \rightarrow \text{qualified directional dependency} \rightarrow \text{dynamically admissible coupling}. }
```

Multilayer-network theory provides mathematical tools for representing multiple networks and relation types, but an interlayer edge is not treated in this thesis as evidence of a physical directional dependency (Kivelä et al., 2014).

For `P\rightarrow T`, candidate mechanism families include electricity supply to charging infrastructure and other electrically dependent transportation functions. Coupled traffic–power studies document interactions among charging demand, transportation behavior, and distribution-system operating constraints (Fotouhi et al., 2017; Unterluggauer et al., 2022; Wei et al., 2019).

For `T\rightarrow P`, transportation conditions can affect access required for repair, restoration, or deployment of mobile resources. Fan et al. (2024), for example, incorporate transportation-network states into post-disaster repair routing.

These mechanisms are physically distinct and must therefore be represented and qualified independently.

Common exposure remains separate from dependency. A flood can expose a road and an electrical component simultaneously, but a cross-system dependency is established only when the state of one infrastructure subsequently affects the other through a specified mechanism.

Mechanisms introduced in Chapter 1 are therefore **candidate mechanism families**. Their inclusion in the conceptual architecture does not establish case-specific dependency acceptance, numerical identifiability, parameter readiness, or authorization for dynamic simulation. Those stronger claims require the evidence and methodological controls developed later in the thesis.

---

## 1.3 Problem Statement

Coupled-infrastructure modeling is not absent from the literature. Interdependent infrastructure has been studied through network, simulation, optimization, stochastic, and data-driven methods. Recent Power–Transportation studies include charging-mediated coupling, transportation-constrained restoration, flood-responsive recovery, emergency-resource coordination, and behavior-dependent charging (Lian et al., 2026; Oladigbolu et al., 2025; Ouyang, 2014; Wang et al., 2024; Wang et al., 2026).

The engineering problem addressed by this thesis is instead the **reliability of the scientific transitions connecting these capabilities**.

First, **structure does not establish a qualified directional dependency**. A graph can show where interaction is possible without explaining why the receiver changes state, when the mechanism activates, or whether the resulting effect is large enough to matter. Recent review evidence continues to identify challenges associated with representing infrastructure interdependencies and uncertainty and with connecting these representations to resilience assessment (Ghasemkhani et al., 2026; Wang et al., 2024).

Second, **mechanism existence does not establish numerical identifiability**. Even where a physical mechanism is plausible, its magnitude may not be uniquely inferable from available observations. The thesis therefore distinguishes:

```math
\boxed{ \text{Does the mechanism exist?} \neq \text{Can its magnitude be identified?} \neq \text{Can its magnitude be estimated adequately?} }
```

Measurement, identification, estimation, simulation, and validation consequently perform different scientific functions. A numerical coefficient produced by a model is not, by itself, evidence that the corresponding real-system dependency has been identified.

Third, **physical possibility does not establish feasible action**. Operators respond through observations, estimated states, information availability, communication, authority, coordination, personnel, and resources. Information and organizational conditions can therefore alter response and recovery even when the physical disturbance is held constant (Chester et al., 2021; Rasoulkhani & Mostafavi, 2018).

Fourth, **a realized service trajectory does not completely characterize resilience**. Performance and recovery curves provide important information about degradation and restoration, but their interpretation depends on the selected service variable, reference state, threshold, horizon, and summary metric (Poulin & Kane, 2021; Trucco & Petrenj, 2023). A different engineering question is whether required service can remain within acceptable conditions and, after violation, whether acceptable service can be recovered under feasible actions and uncertainty.

Finally, **resilience improvement does not by itself determine an engineering decision**. Candidate interventions can produce similar resilience effects while requiring different direct intervention or recovery costs and operational energy, and while producing different admitted carbon-dioxide-equivalent consequences within the declared accounting boundary. Additional resource or distributional quantities are included only where independently qualified. Infrastructure studies already demonstrate trade-offs among resilience, recovery, cost, and greenhouse-gas consequences (Mitoulis et al., 2023; Sun et al., 2025; Zou & Chen, 2019).

The research problem is therefore end-to-end:

```math
\boxed{ \begin{aligned} \text{service requirements} &\rightarrow \text{spatiotemporal P--T structure}\\ &\rightarrow \text{qualified directional dependencies}\\ &\rightarrow \text{complex spatiotemporal coupled dynamics}\\ &\rightarrow \text{observation, organization, and feasible action}\\ &\rightarrow \text{service resilience under uncertainty}\\ &\rightarrow \text{intervention consequences}\\ &\rightarrow \text{engineering decision}. \end{aligned}}
```

The scientific requirement is to make every transition traceable so that the strength of the final engineering conclusion does not exceed the evidence supporting the intermediate steps.

---

## 1.4 Research Gap

The research gap is not the absence of interdependent-infrastructure models, coupled Power–Transportation models, resilience measures, recovery optimization, viability theory, or multiobjective decision methods. Substantial work already exists in each of these areas (Ouyang, 2014; Tong et al., 2025; Wang et al., 2024).

The bounded gap addressed here is that the reviewed evidence does not, by itself, close all of the scientific handoffs required to move from a candidate cross-system relation to a defensible engineering decision.

Each gap is therefore expressed through the same logic:

```math
\boxed{ \text{established capability} \rightarrow \text{documented limitation} \rightarrow \text{unresolved handoff} \rightarrow \text{thesis test}. }
```

### 1.4.1 G1 — Structure to Qualified Directional Dependency

Infrastructure dependency taxonomies and multilayer representations are well established, but terminology and directionality can become ambiguous when structural relations, one-way dependencies, and reciprocal interdependencies are treated as equivalent (Dasuni et al., 2025; Kivelä et al., 2014; Ouyang, 2014).

The unresolved handoff is

```math
\boxed{ \text{candidate structural relation} \rightarrow \text{evidence-qualified directional dependency}. }
```

RQ1 defines the bounded system and candidate interfaces. RQ2 determines which candidate relations satisfy the required mechanism, direction, activation, evidence, uncertainty, and validity conditions.

### 1.4.2 G2 — Qualified Directional Dependency to Dynamic Consequence

Dynamic Power–Transportation models already represent charging interactions, hazard-responsive traffic, emergency-resource movement, and multistage recovery (Lian et al., 2026; Wang et al., 2026; Zhang et al., 2027).

Their existence does not establish the incremental engineering value of representing a qualified mechanism dynamically rather than through simpler matched representations.

The thesis therefore compares

```math
\boxed{ M_0 \quad\text{vs.}\quad M_1 \quad\text{vs.}\quad M_2 }
```

where `M_0` represents independent systems, `M_1` static or algebraic coupling, and `M_2` evidence-qualified dynamic coupling.

This handoff generates RQ3, SO3, and H1.

### 1.4.3 G3 — Physical Dynamics to Knowledge and Feasible Action

Information availability, institutional conditions, coordination, and human–infrastructure interactions are recognized as relevant to infrastructure resilience (Chester et al., 2021; Gim & Miller, 2022; Rasoulkhani & Mostafavi, 2018).

The unresolved handoff is whether differences in what can be observed, estimated, authorized, coordinated, and executed produce meaningful changes in response and recovery under matched physical conditions.

This handoff generates RQ4, SO4, and H2.

### 1.4.4 G4 — Service Trajectory to Viability, Recovery, and Uncertainty Qualification

Performance and recovery curves remain widely used, but their interpretation depends on the selected performance variable, reference state, threshold, time horizon, and summary metric (Poulin & Kane, 2021; Trucco & Petrenj, 2023).

Viability methods ask whether a system can remain within an admissible region, while reachability methods address whether a target region can be reached under specified dynamics, controls, and uncertainty (Béné & Doyen, 2018; Doyen & De Lara, 2010; Vinod & Oishi, 2021).

The unresolved handoff is whether viability and recovery reachability provide meaningful incremental information beyond conventional service and recovery measures.

This handoff generates RQ5, SO5, and H3.

### 1.4.5 G5 — Resilience Effect to Intervention Consequences

Infrastructure interventions that improve resilience can differ in direct intervention or recovery cost, operational energy requirements, and admitted environmental consequences. Existing studies show that resilience, recovery, cost, and greenhouse-gas outcomes can lead to different judgments about candidate strategies (Mitoulis et al., 2023; Sun et al., 2025; Zou & Chen, 2019).

The unresolved handoff is

```math
\boxed{ \text{resilience effect} \rightarrow \text{resource and admitted sustainability consequences}. }
```

This handoff generates RQ6, SO6, and H4.

### 1.4.6 G6 — Intervention Consequences to Engineering Decision

Multiobjective infrastructure analysis is well established, and recent resilience research emphasizes trade-offs rather than assuming that improvement in one criterion determines the engineering choice (Tong et al., 2025).

The unresolved question is whether qualified resource efficiency, admitted sustainability consequences, feasibility, and uncertainty materially change the admissible or nondominated decision set relative to resilience-only evaluation.

This handoff generates RQ7, SO7, and H5.

The six gaps form one scientific chain:

```math
\boxed{ \text{Structure} \rightarrow \text{Qualified Directional Dependency} \rightarrow \text{Dynamics} \rightarrow \text{Knowledge and Action} \rightarrow \text{Resilience} \rightarrow \text{Consequences} \rightarrow \text{Decision}. }
```

Identification operates across this chain whenever unknown quantities must be inferred from observations. It is therefore treated as a cross-cutting scientific requirement rather than as an additional stage.

The thesis is consequently framed as an **integration, incremental-value, and validation problem**, not as a claim that its component methods are individually new.

---

## 1.5 Sustainable Engineering Significance

The Sustainable Engineering significance of this research lies in evaluating whether infrastructure interventions that improve service resilience do so with materially different resource requirements and admitted sustainability consequences.

Four concepts are deliberately kept separate.

**Resilience effect** describes how an intervention changes the ability of electricity and mobility services to remain acceptable or recover.

**Effectiveness** asks whether the intervention achieves its declared engineering objective.

**Resource efficiency** relates an engineering effect to the resources required to obtain it.

**Sustainability consequence** describes an admitted environmental or distributional consequence evaluated within a declared accounting boundary.

These quantities need not move in the same direction. Infrastructure-recovery studies demonstrate that resilience, cost, energy, and greenhouse-gas objectives can lead to different judgments about candidate strategies (Mitoulis et al., 2023). Coupled transportation–power studies also include budget, investment, operating-cost, recovery-resource, and carbon-related considerations (Sun et al., 2025; Zou & Chen, 2019).

The present thesis therefore uses a deliberately narrow consequence boundary. Direct intervention or recovery cost and operational electrical energy are treated as resource quantities. Carbon-dioxide-equivalent emissions constitute the principal planned environmental sustainability consequence within the qualified accounting boundary. Distributional accessibility remains conditional on adequate construct definition, population boundaries, data, and accounting rules.

This separation also prevents double counting. Electricity served, mobility provided, service loss, accessibility required for infrastructure operation, and recovery time primarily characterize service and resilience. They are not automatically reclassified as independent sustainability outcomes.

The Sustainable Engineering question is therefore bounded:

> **When candidate interventions produce resilience benefits, do their resource requirements, resource efficiencies, or admitted sustainability consequences differ enough to affect the engineering decision?**

The thesis does not assume that they will.

---

## 1.6 Scope, Boundaries, Assumptions, and Validity Domain

The thesis is deliberately bounded to the Power–Transportation problem defined by the research questions. It is not intended to reproduce every physical, behavioral, institutional, economic, or environmental process affecting infrastructure.

| BoundaryIncludedNot inferred or outside the confirmatory core |                                                                                |                                                                    |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------ |
| Physical infrastructure                                       | Power + Transportation                                                         | Other physical infrastructure sectors                              |
| Supporting domains                                            | Information + Organization                                                     | Automatic treatment of `I` and `O` as equivalent physical networks |
| Primary services                                              | Electricity + mobility                                                         | Universal welfare or comprehensive societal-service modeling       |
| Interaction                                                   | Qualified `P\rightarrow T` and `T\rightarrow P` mechanisms                     | Co-location or common exposure treated as dependency               |
| Hazard                                                        | Flooding as principal planned demonstrator, subject to Chapter 4 qualification | Generalization to all hazards                                      |
| Intervention                                                  | Operational/recovery control and persistent engineering interventions          | Unbounded intervention families                                    |
| Resources                                                     | Qualified direct cost and operational energy                                   | Complete economic accounting                                       |
| Environmental consequence                                     | Qualified `CO_{2e}` within the declared boundary                               | Full life-cycle sustainability assessment                          |
| Distributional quantity                                       | Accessibility where construct and data requirements are satisfied              | Broad social-sustainability index                                  |
| Validity                                                      | Tested systems, mechanisms, ranges, scenarios, and accounting boundaries       | Universal generalization                                           |

The physical core is `P+T`. Information and Organization affect observation and feasible action but are not treated as independent physical infrastructure networks unless a specific experiment requires such a representation.

The principal service boundary is electricity and mobility. Physical states are represented to the fidelity required to determine these services, qualified dependency mechanisms, disturbance effects, and feasible recovery or control.

The spatial boundary is the geographic support over which Power, Transportation, hazard, observation, and interface data can be aligned with sufficient provenance. Geographic co-location alone does not establish dependency.

The temporal boundary distinguishes data vintage, disturbance time, causal delay, characteristic timescale, simulation horizon, and recovery horizon. These quantities serve different scientific purposes and are not treated as interchangeable.

Flooding is the principal planned demonstrator hazard, subject to Chapter 4 qualification. Exposure is distinguished from damage, component failure, and service consequence. A flood footprint can therefore establish potential exposure without establishing failure probability or the resulting system response.

The thesis also distinguishes the evolving physical state `Y(x,t)`, operational or recovery control `u(x,t)`, and persistent engineering intervention `a_k`. Operational control changes how existing infrastructure is used; a persistent intervention can alter structure, capacity, redundancy, resource availability, or operating capability.

Development testbeds can support implementation, mechanism exploration, numerical verification, and methodological development without defining the final empirical validity domain. Case selection, data provenance, spatial and temporal alignment, parameter readiness, and confirmatory admissibility are therefore established in Chapter 4.

Uncertainty can arise from hazards, dependency mechanisms, model form, parameters, observations, interventions, resource estimates, and accounting assumptions. Probabilistic representations are used only where their probability semantics are defensible. Otherwise, uncertainty is represented through scenarios, bounds, sensitivity analysis, or robust formulations.

All final claims are restricted to the systems, mechanisms, parameter ranges, hazards, observations, interventions, accounting boundaries, and validation evidence actually examined.

The governing inference rule is

```math
\boxed{ \operatorname{Strength}(\text{claim}) \le \operatorname{Strength}(\text{supporting evidence}). }
```

---

## 1.7 Research Framework and Scientific Logic

Within the bounded domain established above, the thesis uses a seven-stage scientific architecture. The architecture is a **thesis synthesis**, not an established seven-stage framework taken directly from the literature.

The scientific chain is

```math
\boxed{ \begin{aligned} \text{Critical service requirements} &\rightarrow \text{Spatiotemporal P--T System-of-Systems structure}\\ &\rightarrow \text{Evidence-qualified directional dependencies}\\ &\rightarrow \text{Complex spatiotemporal coupled dynamics}\\ &\rightarrow \text{Observation, estimation, organization, and feasible control}\\ &\rightarrow \text{Uncertainty-aware service viability and recovery}\\ &\rightarrow \text{Targeted intervention consequences}\\ &\rightarrow \text{Defensible engineering decision}. \end{aligned}}
```

The architecture is compatible with service-centered infrastructure System-of-Systems reasoning and with separate-but-coupled treatment of energy and transportation systems (Hall et al., 2016; Ibáñez et al., 2010). The seven-stage integration itself is the thesis construct.

**Stage 1 — Spatiotemporal System-of-Systems Structure.**
This stage defines the bounded systems, services, entities, states, locations, temporal characteristics, and candidate interfaces. It establishes where and when interaction could occur without establishing a directional dependency.

**Stage 2 — Evidence-Qualified Directional Dependencies.**
Candidate relations are evaluated by mechanism, direction, activation conditions, operating and hazard context, delay, characteristic timescale, uncertainty, evidence, and validity domain. Acceptance as a directional dependency does not automatically imply numerical readiness for simulation.

**Stage 3 — Complex Spatiotemporal Coupled Dynamics.**
Dynamically ready mechanisms are introduced into the native physical representations of Power and Transportation. The stage tests whether dynamic coupling provides meaningful information beyond matched independent or static-coupling representations.

**Stage 4 — Observation, Estimation, Organization, and Feasible Control.**
The evolving physical state is connected to what can be measured, estimated, communicated, authorized, coordinated, and executed. Physical possibility is therefore distinguished from operational feasibility.

The conceptual progression is

```math
Y \rightarrow y \rightarrow \widehat Y \rightarrow (I,O) \rightarrow \mathcal U_{\mathrm{feas}} \rightarrow u.
```

**Stage 5 — Uncertainty-Aware Service Resilience.**
The analysis asks whether required services can remain acceptable and, after violation, whether they can be recovered. Viability provides a formal basis for remaining within acceptable conditions, whereas recovery reachability addresses return after service violation. Conventional service and recovery measures remain explicit comparators rather than being discarded (Béné & Doyen, 2018; Poulin & Kane, 2021; Vinod & Oishi, 2021).

**Stage 6 — Engineering Intervention Consequences.**
Resilience diagnosis informs the identification and comparison of candidate interventions. Type, location, timing, and scale are considered where relevant, while resilience effectiveness, resource requirements, resource efficiency, and admitted sustainability consequences remain distinct quantities.

**Stage 7 — Defensible Engineering Decision.**
Candidate alternatives are evaluated jointly under feasibility, resilience evidence, resource efficiency, admitted sustainability consequences, and uncertainty. The output is a defensible decision set rather than an assumed universal optimum.

Identification, verification, validation, uncertainty quantification, provenance, and reproducibility operate across the seven stages. They are cross-cutting scientific controls rather than an eighth stage.

---

## 1.8 General Research Objective

The general objective of this thesis is:

> **To develop and validate an evidence-grounded mathematical and engineering framework for coupled Power–Transportation infrastructure that connects spatiotemporal System-of-Systems structure and qualified directional interdependencies to complex spatiotemporal dynamics, observation, information and organizational constraints, feasible control, uncertainty-aware service viability and recovery, engineering intervention consequences, and defensible engineering decisions. Engineering interventions are evaluated through their resilience effects, resource requirements and efficiency, and admitted sustainability consequences.**

Validation is interpreted within the declared context and validity domain of the corresponding model, experiment, and evidence rather than as universal validation of the framework.

The objective can be read operationally as

```math
\boxed{ \text{Define} \rightarrow \text{Qualify} \rightarrow \text{Model} \rightarrow \text{Respond} \rightarrow \text{Assess} \rightarrow \text{Compare} \rightarrow \text{Decide}. }
```

---

## 1.9 Research Questions

RQ0 is the overarching research question. RQ1–RQ7 decompose it into an ordered scientific sequence from system definition to engineering decision. The short statements below clarify purpose without replacing the canonical wording.

### RQ0 — Overarching Question

**Scientific purpose:** connect the complete P–T problem from representation to defensible engineering decision.

> **How can coupled Power–Transportation infrastructure be represented as an interdependent System of Systems and modeled as a spatiotemporal complex dynamical system to connect qualified directional dependencies, observation- and organization-constrained feasible response, uncertainty-aware service resilience, engineering intervention consequences, and defensible engineering decisions?**

### RQ1 — Spatiotemporal System-of-Systems Structure

**Scientific purpose:** define the bounded system and identify where and when interaction can occur.

> **What constituent systems, supporting Information and Organization domains, services, entities, states, spatial locations, temporal characteristics, and candidate interfaces constitute the bounded Power–Transportation System of Systems, and where and when can interactions occur?**

### RQ2 — Evidence-Qualified Spatiotemporal Directional Dependencies

**Scientific purpose:** determine which candidate relations qualify as directional dependencies and within what conditions they are valid.

> **Which candidate Power–Transportation relations can be admitted as evidence-qualified directional dependency mechanisms, through what mechanisms, where and when do they activate, under what operating and hazard conditions, with what delays, characteristic timescales, and uncertainty, and within what validity domain?**

### RQ3 — Complex Spatiotemporal Coupled Dynamics

**Scientific purpose:** determine what dynamically ready dependencies do relative to simpler representations.

> **How do qualified and dynamically ready directional dependency mechanisms evolve, interact, and propagate across space and time, and how do they alter coupled physical states and electricity and mobility service trajectories relative to independent and static-coupling representations?**

### RQ4 — Spatiotemporal Observation, Organization, and Feasible Response

**Scientific purpose:** determine how knowledge and feasible action shape response and recovery.

> **How do spatially and temporally distributed observations, state estimation, information availability, organizational conditions, and feasible control shape the response and recovery of the evolving coupled Power–Transportation system?**

### RQ5 — Uncertainty-Aware Spatiotemporal Service Resilience

**Scientific purpose:** determine when required services can remain acceptable or recover and whether viability and reachability add engineering information.

> **Under what spatiotemporal conditions can required electricity and mobility services remain acceptable or be recovered under feasible actions and uncertainty, and what additional engineering information do viability and reachability provide beyond conventional service-recovery measures?**

### RQ6 — Spatiotemporally Targeted Engineering Intervention Consequences

**Scientific purpose:** compare candidate interventions through separate resilience, resource, efficiency, and admitted sustainability consequences.

> **How do candidate engineering interventions, characterized by type, location, timing, and scale where relevant, differ in resilience effectiveness, resource requirements and efficiency, and admitted sustainability consequences under independently qualified requirements, declared accounting boundaries, and uncertainty?**

### RQ7 — Defensible Spatiotemporal Engineering Decision

**Scientific purpose:** identify the alternatives that remain defensible after the qualified criteria are considered jointly.

> **Which candidate interventions or infrastructure transformations, including their location, timing, and scale where relevant, remain defensible when resilience, resource efficiency, admitted sustainability consequences, feasibility, and uncertainty are evaluated jointly?**

The research-question sequence is

```math
\boxed{ RQ_1 \rightarrow RQ_2 \rightarrow RQ_3 \rightarrow RQ_4 \rightarrow RQ_5 \rightarrow RQ_6 \rightarrow RQ_7 \rightarrow RQ_0. }
```

The arrows indicate scientific dependency rather than strict mathematical implication.

---

## 1.10 Specific Research Objectives

The specific objectives correspond one-to-one with RQ1–RQ7.

**SO1 — Define.**
Define the bounded Power–Transportation System of Systems in terms of constituent systems, supporting Information and Organization domains, services, entities, states, spatial locations, temporal characteristics, and candidate interfaces.

**SO2 — Qualify.**
Qualify candidate Power–Transportation relations as directional dependency mechanisms by establishing their mechanism, direction, spatial and temporal activation conditions, operating and hazard conditions, delays, characteristic timescales, evidence basis, uncertainty, and validity boundaries.

**SO3 — Model and test.**
Develop and verify a physics-based complex spatiotemporal coupled dynamic representation and test the incremental explanatory or predictive information provided by dynamically ready coupling relative to independent and static-coupling representations.

**SO4 — Evaluate knowledge and feasible response.**
Evaluate how spatially and temporally distributed measurement, state estimation, information availability, organizational conditions, and feasible control affect response timing, electricity and mobility service trajectories, and recovery.

**SO5 — Assess viability and recovery under uncertainty.**
Determine uncertainty-aware spatiotemporal service viability and recovery reachability, evaluate their incremental information beyond conventional service and recovery representations, and characterize interface criticality where the required evidence permits.

**SO6 — Quantify and compare interventions.**
Quantify and compare candidate engineering interventions, including their type, location, timing, and scale where relevant, in terms of resilience effectiveness, resource requirements and efficiency, and admitted sustainability consequences within independently justified requirements and declared accounting boundaries.

**SO7 — Evaluate and decide.**
Evaluate candidate interventions or infrastructure transformations, including their location, timing, and scale where relevant, jointly in terms of resilience, resource efficiency, admitted sustainability consequences, feasibility, and uncertainty; evaluate intervention sequences only where temporal decision structure, data, and validation support them.

The required traceability is

```math
\boxed{ RQ_k\Longleftrightarrow SO_k, \qquad k=1,\ldots,7. }
```

---

## 1.11 Research Hypotheses and Test Logic

The thesis retains five primary confirmatory hypotheses. RQ1 and RQ2 establish the structural and evidence prerequisites required by the downstream tests rather than requiring additional hypotheses.

| HypothesisPrimary comparisonScientific purposeCurrent status |                                                                       |                                                                                     |            |
| ------------------------------------------------------------ | --------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ---------- |
| **H1**                                                       | `M_2` vs. `M_1`, with `M_0` reference                                 | Test incremental value of dynamic coupling                                          | NOT TESTED |
| **H2**                                                       | Matched information/organization contrasts                            | Test effects on estimation, feasible action, response, and recovery                 | NOT TESTED |
| **H3**                                                       | Conventional service/recovery vs. viability–reachability augmentation | Test incremental resilience information                                             | NOT TESTED |
| **H4**                                                       | Qualified intervention alternatives                                   | Test differences in resources, efficiency, and admitted sustainability consequences | NOT TESTED |
| **H5**                                                       | Resilience-only vs. joint decision evaluation                         | Test decision-set, dominance, or regret change                                      | NOT TESTED |

### H1 — Dynamic Causal Coupling

> **Under matched disturbances, initial conditions, service requirements, and exogenous conditions, an evidence-qualified dynamic Power–Transportation coupling representation provides meaningful incremental explanatory or predictive information for prespecified service-loss, propagation, cascade, or recovery outcomes relative to a corresponding static-coupling representation.**

The primary comparison is `M_2` against `M_1`, with `M_0` retained as the uncoupled reference.

### H2 — Information, Organization, and Feasible Control

> **Under matched physical conditions and disturbances, changes in information availability and organizational conditions produce meaningful differences in state-estimation quality, feasible action, response timing, service trajectories, recovery, or downstream resilience outcomes.**

The comparisons are interpreted as matched modeled contrasts and are not automatically interpreted as identified real-world causal effects.

### H3 — Viability and Recovery-Reachability Information

> **For the declared Power–Transportation test domain, uncertainty-aware viability and recovery-reachability information provides meaningful incremental predictive or decision-relevant information about service maintainability and acceptable recovery beyond prespecified conventional service and recovery measures.**

H3 therefore tests incremental engineering information rather than assuming that viability and reachability are superior by definition.

### H4 — Intervention Consequences

> **Across the prespecified intervention and scenario set, at least two resilience-effective engineering interventions produce materially different resource requirements, resource efficiencies, or admitted sustainability consequences under the declared comparison rule.**

Resilience effect, resource requirement, resource efficiency, and sustainability consequence remain separate objects throughout this test.

### H5 — Joint Engineering Decision

> **Under the declared uncertainty domain, incorporating resource efficiency and admitted sustainability consequences together with feasibility and uncertainty materially changes the admissible or nondominated engineering decision set, dominance relations, or decision regret relative to resilience-only evaluation.**

The analysis seeks a defensible decision set. It does not assume a universal scalar objective or universally optimal intervention.

The confirmatory traceability is

```math
\boxed{ RQ_3/SO_3\rightarrow H_1,\quad RQ_4/SO_4\rightarrow H_2,\quad RQ_5/SO_5\rightarrow H_3,\quad RQ_6/SO_6\rightarrow H_4,\quad RQ_7/SO_7\rightarrow H_5. }
```

RQ1/SO1 and RQ2/SO2 provide the structural and dependency-qualification prerequisites supporting H1 and the downstream analyses.

If evidence, data, model readiness, or another prerequisite prevents a confirmatory experiment from being executed, the appropriate status is **NOT TESTED**, not automatic rejection of the hypothesis.

---

## 1.12 Proposed Contributions

The thesis proposes six contribution areas. At the Chapter-I stage these are **proposed contributions**, not established findings. Their final status depends on the corresponding evidence, experiment, verification, validation, uncertainty analysis, and validity domain.

### C1 — Bounded Service-Centered Spatiotemporal Power–Transportation System-of-Systems Representation

The thesis proposes a representation that preserves Power and Transportation as distinct physical constituent systems while representing Information and Organization as supporting domains governing knowledge and feasible action.

The intended contribution is not the System-of-Systems concept itself, but its bounded integration into the specific P–T scientific chain developed by the thesis.

### C2 — Evidence-Qualified Directional Dependency Representation

The thesis proposes a mechanism-centered progression in which candidate structural relations become directional dependencies only after explicit mechanism and evidence qualification.

The representation separates common exposure, structural relation, observed association, directional dependency, reciprocal interdependency, and dynamic coupling.

### C3 — Controlled Admission of Dependency Mechanisms into Coupled Dynamics

If H1 is supported, the thesis will provide evidence concerning the incremental engineering value of dynamically representing qualified P–T mechanisms relative to simpler matched representations.

The intended contribution is therefore not coupling by itself, but the controlled admission of coupling based on evidence and dynamic readiness.

### C4 — Observation-, Information-, and Organization-Constrained Response

If H2 is supported, the thesis will provide evidence concerning how observation, state estimation, information availability, organizational conditions, and feasible control alter response and recovery within the declared domain.

### C5 — Uncertainty-Aware Viability and Recovery Assessment

If H3 is supported, the thesis will provide evidence concerning whether viability and recovery reachability add predictive or decision-relevant information beyond conventional service-recovery measures.

### C6 — Intervention and Engineering-Decision Evaluation

If H4 and H5 are supported, the thesis will provide evidence concerning whether resilience-effective interventions differ materially in resource requirements, resource efficiency, or admitted sustainability consequences and whether those differences alter engineering decisions.

The decision formulation seeks defensible or nondominated alternatives rather than claiming universal optimality without an independently justified preference model.

The contribution chain is

```math
\boxed{ \text{Representation} \rightarrow \text{Qualified Dependency} \rightarrow \text{Dynamics} \rightarrow \text{Feasible Response} \rightarrow \text{Resilience} \rightarrow \text{Intervention} \rightarrow \text{Decision}. }
```

The thesis does not claim novelty for the component ideas individually. System-of-Systems reasoning, infrastructure interdependency, coupled Power–Transportation modeling, resilience curves, viability and reachability, and multiobjective infrastructure decision analysis all have established foundations (Doyen & De Lara, 2010; Maier, 1998; Ouyang, 2014; Poulin & Kane, 2021; Rinaldi et al., 2001; Vinod & Oishi, 2021; Wei et al., 2019).

The governing contribution boundary is therefore

```math
\boxed{ \text{proposed contribution} \neq \text{supported contribution} \neq \text{validated contribution} \neq \text{global novelty}. }
```

---

## 1.13 Thesis Organization

The remainder of the thesis follows the scientific dependency established in Chapter 1.

**Chapter 2 — Literature Review and Scientific Foundations** establishes the evidence and theoretical foundations required by the research questions. It distinguishes established capability from unresolved handoffs and provides the evidence base for the thesis definitions, mechanisms, comparators, and bounded research gap.

**Chapter 3 — Conceptual and Mathematical Framework** formalizes the Power–Transportation architecture, directional-dependency objects, coupled dynamics, observation and estimation, feasible-control structure, acceptable-service conditions, viability, recovery reachability, intervention consequences, and decision objects.

**Chapter 4 — Research Methodology and Experimental Design** converts the research contract into reproducible tests. It establishes evidence and source qualification, case and data admissibility, spatial and temporal alignment, measurement models, identification, estimator admission, model realization, numerical verification, scenario design, matched experiments, validation, uncertainty quantification, sensitivity analysis, falsification rules, and reproducibility.

**Chapter 5 — Results** reports qualified prerequisite, model, and confirmatory results. Each primary result is presented with its comparator, uncertainty treatment, materiality or decision criterion, and validity domain before a hypothesis status is assigned.

**Chapter 6 — Discussion and Sustainable Engineering Implications** interprets the results in relation to physical mechanisms, assumptions, rival explanations, prior literature, resources, admitted sustainability consequences, engineering decisions, transferability, and remaining uncertainty.

**Chapter 7 — Conclusions and Future Work** answers RQ0 and RQ1–RQ7 at the level justified by the completed evidence, records the final H1–H5 statuses, identifies the contributions actually supported by the research, states the limits of validity and generalization, and defines the unresolved research agenda.

The thesis therefore follows one end-to-end argument:

```math
\boxed{ \text{Problem} \rightarrow \text{Evidence} \rightarrow \text{Mathematical Framework} \rightarrow \text{Qualified Method} \rightarrow \text{Results} \rightarrow \text{Interpretation} \rightarrow \text{Engineering Conclusion}. }
```

Chapter 1 establishes the scientific contract for that argument. It defines what the thesis studies, why the problem matters, what remains unresolved, what will be tested, what evidence is required, and under what conditions later engineering conclusions will be scientifically admissible.
