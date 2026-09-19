# Chapter 1 — Introduction: Research Problem and Scientific Contract

## 1.1 Background and Engineering Context

The electrification of transportation is increasing the operational interaction between electric-power and transportation infrastructures. Electric-vehicle charging links mobility demand to the location, timing, and availability of electricity supply, while charging demand can influence distribution-system operation and planning (Unterluggauer et al., 2022; Wei et al., 2019). Emerging vehicle-to-grid and mobile-energy applications create additional opportunities for transportation resources to interact with the power system (Oladigbolu et al., 2025).

The relationship also extends beyond normal operation. Transportation conditions can affect power-system restoration because repair crews, equipment, replacement components, and mobile energy resources depend on physical access to damaged electrical assets. Post-disaster restoration studies explicitly show that road conditions can constrain repair routing and coordinated infrastructure recovery (Fan et al., 2024; Lian et al., 2026). Power-to-Transportation and Transportation-to-Power dependencies therefore arise through different physical and operational mechanisms.

These infrastructures matter because they provide services rather than simply because they contain assets. Hall et al. (2016) frame infrastructure assessment around the services produced by coordinated infrastructure systems. Under this interpretation, the power system supports electricity service, whereas the transportation system supports mobility and physical accessibility. A failure becomes important when it changes the ability of these systems to provide the required services or constrains the operation and recovery of another system.

Power and Transportation nevertheless remain distinct constituent systems. Integrated energy–transport studies can model them jointly while retaining their separate network structures, operational logic, and planning variables (Ibáñez et al., 2010). Coupling therefore does not require electrical and transportation physics to be homogenized into one generic network.

Direction is equally important. Electricity availability may affect charging infrastructure and other electrically dependent transportation functions, whereas road availability may affect repair access and restoration of the power system. Charging behavior and mobile electrical resources can create additional Transportation-to-Power effects under appropriate operating conditions (Oladigbolu et al., 2025; Wang et al., 2026). For this thesis,

```math
P\rightarrow T \qquad\text{and}\qquad T\rightarrow P
```

are qualified independently. Evidence of one direction does not establish the other.

The broader infrastructure-interdependency literature likewise distinguishes different forms of dependency and recognizes that cascading consequences can arise when a change in one infrastructure affects another through a functional relationship (Ouyang, 2014; Rinaldi et al., 2001). At the same time, simultaneous exposure to the same hazard does not by itself establish such a relationship. Two assets can fail together because they share a flood footprint without either failure causing the other.

The thesis therefore uses two complementary perspectives. A **System-of-Systems perspective** is used to represent the architecture of distinct constituent systems and their interfaces, while a **complex-dynamical-systems perspective** is used to study how their states, dependencies, disturbances, controls, and recovery processes evolve through time. Systems-of-systems research emphasizes the continued identity and operational characteristics of constituent systems within a larger architecture (Maier, 1998), while infrastructure-interdependency research demonstrates that interactions between constituent infrastructures can generate behavior not captured by isolated-system analysis (Ouyang, 2014; Rinaldi et al., 2001).

For analytical clarity, the thesis therefore adopts the modeling convention

```math
\boxed{ \text{System of Systems}=\text{architectural view}, \qquad \text{complex dynamical system}=\text{behavioral view}. }
```

This is a **thesis modeling convention**, not a claim that the two concepts are universally separate.

The engineering problem consequently extends beyond determining whether Power and Transportation are connected. It concerns whether specific directional mechanisms are supported by evidence, whether those mechanisms materially affect coupled behavior and service trajectories, whether the resulting system condition can be observed and acted upon, and whether critical services can remain acceptable or be recovered under disruption and uncertainty.

---

## 1.2 Coupled Power–Transportation System Context

For this thesis, the physical infrastructure core consists of Power and Transportation:

```math
\boxed{P+T}.
```

Information and Organization are represented as supporting domains:

```math
\boxed{I+O}.
```

This is a thesis-specific ontology. It does not imply that `P`, `T`, `I`, and `O` are four equivalent physical infrastructures.

Power and Transportation are the constituent physical systems because they contain the physical assets, connections, operational states, controls, and service functions required to provide electricity and mobility. This service-centered interpretation is consistent with the infrastructure System-of-Systems framing used by Hall et al. (2016). Power and Transportation also remain separately represented, consistent with integrated energy–transport modeling in which interaction does not require loss of system-specific structure or physics (Ibáñez et al., 2010).

The Information domain represents what can be observed, communicated, or estimated about the physical system. Depending on the experiment, this may include measurement availability, communication status, delays, missing observations, and state estimates. Information-related dependencies are recognized in infrastructure and cyber-physical-system research, but the existence of information flow does not by itself imply that a physical action can be executed (Mohamed, 2019; Rinaldi et al., 2001).

The Organizational domain represents the conditions through which information is converted into feasible action. Relevant conditions may include authority, coordination, priorities, personnel, equipment, resource availability, and response delays. Infrastructure-resilience research increasingly recognizes that institutions, governance arrangements, and human–infrastructure interactions can materially influence response and adaptation (Chester et al., 2021; Helmrich et al., 2021; Rasoulkhani & Mostafavi, 2018).

The resulting thesis representation is therefore

```math
\boxed{ \underbrace{P+T}_{\text{physical infrastructure}} + \underbrace{I+O}_{\text{knowledge and feasible-action support}}. }
```

This representation also requires a strict relationship taxonomy. Multilayer-network theory provides mathematical tools for representing multiple networks and relation types (Kivelä et al., 2014), but the presence of an interlayer edge is not treated in this thesis as evidence of a physical causal mechanism.

A **structural relation** identifies where interaction could occur. A **directional dependency** requires a physically or operationally interpretable mechanism through which a source affects a receiver under specified conditions. A reciprocal **interdependency** requires relevant directional dependencies in both directions. **Dynamic coupling** requires an additional step: the qualified mechanism must be sufficiently specified to enter the governing dynamic model.

The scientific progression is therefore

```math
\boxed{ \text{candidate relation} \rightarrow \text{qualified directional dependency} \rightarrow \text{dynamically admissible coupling}. }
```

For `P\rightarrow T`, candidate mechanisms include electricity supply to charging infrastructure and other electrically dependent transportation functions. Coupled traffic–power studies and reviews document relationships among charging demand, road-network behavior, and distribution-system operating constraints (Fotouhi et al., 2017; Unterluggauer et al., 2022; Wei et al., 2019).

For `T\rightarrow P`, transportation conditions may affect the accessibility required for repair, restoration, or deployment of mobile resources. Fan et al. (2024) explicitly incorporate transportation-network states into post-disaster repair routing. These mechanisms differ physically from `P\rightarrow T` mechanisms and are therefore represented and qualified separately.

Common exposure remains distinct. A flood may affect a road and a power asset simultaneously, but this shared exposure becomes a cross-system dependency only when the resulting state of one system subsequently affects the other through a specified mechanism.

Mechanisms described in Chapter 1 therefore represent **candidate mechanism families**. Their appearance in the conceptual architecture does not establish case-specific causal acceptance, parameter identification, or authorization for dynamic simulation. Those stronger claims require the corresponding evidence and methodological controls developed later in the thesis.

---

## 1.3 Problem Statement

Coupled-infrastructure modeling itself is not absent from the literature. Interdependent infrastructure has been studied using network, simulation, optimization, stochastic, and data-driven approaches, while recent Power–Transportation research includes EV-mediated coupling, transportation-constrained restoration, flood-responsive recovery, emergency-resource coordination, and behavior-dependent charging (Lian et al., 2026; Oladigbolu et al., 2025; Ouyang, 2014; Wang et al., 2026; Wang et al., 2024).

The engineering problem addressed here is instead the reliability of the scientific transitions connecting these components.

A first difficulty is that **structure, causal mechanism, and dynamic effect are not equivalent**. A graph can indicate where interaction is possible without explaining why the receiving system changes state, when the mechanism activates, or how large the resulting effect is. Reviews continue to identify challenges in representing interdependencies, their temporal behavior, uncertainty, and the evidence needed to support coupled-infrastructure inference (Ghasemkhani et al., 2026; Wang et al., 2024).

A second difficulty arises even after a plausible physical mechanism has been identified. Mechanism existence does not establish that its magnitude can be inferred from available observations. The thesis therefore separates three questions:

```math
\boxed{ \text{Does the mechanism exist?} \neq \text{Can its magnitude be identified?} \neq \text{Can the magnitude be estimated adequately?} }
```

Measurement, identification, estimation, and simulation are therefore different scientific tasks. This distinction prevents a numerical coefficient obtained from a computational model from being interpreted automatically as evidence that the underlying physical mechanism has been identified.

A third difficulty is that physical state does not determine feasible response. Infrastructure operators act using imperfect observations, estimated states, information availability, authority, coordination, personnel, and available resources. Human and institutional conditions can therefore alter infrastructure response even when the underlying physical disturbance is similar (Chester et al., 2021; Rasoulkhani & Mostafavi, 2018).

A fourth difficulty concerns resilience itself. Performance and recovery curves are useful for characterizing infrastructure degradation and restoration, but different performance measures and summary metrics capture different properties of the disruption–recovery process (Poulin & Kane, 2021; Trucco & Petrenj, 2023). The question considered in this thesis is therefore not only how service changes through time, but whether required electricity and mobility services can remain acceptable, whether acceptable service can be recovered after violation, and with what confidence those statements can be made under uncertainty.

A final difficulty appears when resilience analysis is translated into intervention. Power–Transportation studies already consider hardening, charging coordination, mobile resources, repair routing, switching, and coordinated recovery (Lian et al., 2026; Oladigbolu et al., 2025). The remaining engineering issue is whether interventions that appear beneficial from a resilience perspective remain equivalent when their resource requirements, efficiency, environmental consequences, feasibility, and uncertainty are considered.

The problem is therefore end-to-end:

```math
\boxed{ \begin{aligned} \text{service requirements} &\rightarrow \text{spatiotemporal P--T System-of-Systems structure} \rightarrow \text{qualified directional dependencies}\\ &\rightarrow \text{complex spatiotemporal coupled dynamics} \rightarrow \text{observation, organization and feasible action}\\ &\rightarrow \text{spatiotemporal remain / recover / confidence} \rightarrow \text{intervention consequences} \rightarrow \text{engineering decision}. \end{aligned} }
```

The research problem is to make each transition scientifically traceable so that the strength of the final engineering conclusion does not exceed the evidence supporting the intermediate steps.

---

## 1.4 Research Gap

The research gap is not that interdependent-infrastructure models, coupled Power–Transportation models, resilience metrics, recovery optimization, viability theory, or multiobjective decision methods do not exist. Substantial work already exists in each of these areas (Ouyang, 2014; Tong et al., 2025; Wang et al., 2024).

The gap is more specific: the evidence reviewed to date does not sufficiently establish all of the **handoffs** needed to move from a candidate cross-system relationship to a defensible engineering decision within the bounded problem considered here.

### G1 — Structure to qualified dependency

Infrastructure research provides established dependency taxonomies and multilayer representations, but terminology and directionality remain important sources of ambiguity when one-way dependencies and reciprocal relationships are treated together (Dasuni et al., 2025).

For this thesis, a structural relationship does not establish a causal dependency. The unresolved handoff is:

```math
\boxed{ \text{candidate structural relation} \rightarrow \text{evidence-qualified directional mechanism}. }
```

This gap supports RQ1 and RQ2.

### G2 — Qualified mechanism to dynamic consequence

Dynamic Power–Transportation models already exist and include hazard-responsive traffic, charging behavior, emergency-resource movement, and multistage recovery (Lian et al., 2026; Wang et al., 2026; Zhang et al., 2026). The unresolved issue is therefore comparative: whether an evidence-qualified dynamic-coupling representation provides meaningful engineering information beyond matched independent or static-coupling representations.

The required comparison is

```math
M_0 \quad\text{vs}\quad M_1 \quad\text{vs}\quad M_2,
```

where `M_0` is independent, `M_1` is static or algebraic coupling, and `M_2` is dynamic causal coupling.

This gap generates RQ3, SO3, and H1.

### G3 — Physical dynamics to knowledge and feasible action

Information, institutional conditions, and human–infrastructure interactions are already recognized as relevant to resilience (Chester et al., 2021; Gim & Miller, 2022; Rasoulkhani & Mostafavi, 2018). The unresolved handoff is whether differences in what can be observed, estimated, authorized, coordinated, and executed materially change the response under matched physical conditions.

This gap generates RQ4, SO4, and H2.

### G4 — Service trajectory to remain, recover, and confidence

Infrastructure-resilience curves remain widely used, but their meaning depends on the performance variable, reference state, threshold, time horizon, and summary metric (Poulin & Kane, 2021; Trucco & Petrenj, 2023). Viability-based approaches provide a different perspective by asking whether a system can remain within an admissible set rather than summarizing only the realized trajectory (Béné & Doyen, 2018).

The unresolved question is whether viability and recovery reachability provide useful incremental information beyond conventional service and recovery measures.

This gap generates RQ5, SO5, and H3.

### G5 — Resilience improvement to intervention consequences

Engineering interventions can improve resilience while imposing different cost, energy, emissions, or accessibility consequences. Infrastructure research already demonstrates meaningful trade-offs among resilience, recovery, cost, and greenhouse-gas outcomes (Mitoulis et al., 2023).

The unresolved handoff is therefore:

```math
\text{resilience improvement} \rightarrow \text{resource and admitted sustainability consequences}.
```

This gap generates RQ6, SO6, and H4.

### G6 — Consequences to engineering decision

Multiobjective infrastructure analysis is already established, and recent reviews emphasize trade-offs rather than single-objective improvement (Tong et al., 2025). The unresolved question is whether adding qualified resource, sustainability, feasibility, and uncertainty information materially changes the decision relative to resilience-only evaluation.

This gap generates RQ7, SO7, and H5.

Together, the six gaps define one dependent research problem:

```math
\boxed{ \text{Structure} \rightarrow \text{Causality} \rightarrow \text{Dynamics} \rightarrow \text{Knowledge and Action} \rightarrow \text{Resilience} \rightarrow \text{Consequences} \rightarrow \text{Decision}. }
```

The thesis is therefore framed as an **integration, incremental-value, and validation problem** rather than as a claim that its individual methods are new.

---

## 1.5 Sustainable Engineering Significance

The Sustainable Engineering significance of this research lies in evaluating how infrastructure interventions affect not only service resilience but also the resources consumed and the consequences generated in achieving that resilience. Contemporary resilience research increasingly recognizes that infrastructure decisions must account for uncertainty, adaptation, and interactions among technical and institutional systems rather than asset robustness alone (Chester et al., 2021).

Resilience, effectiveness, efficiency, and sustainability are not treated as interchangeable concepts.

**Resilience effect** describes the change in the ability of electricity and mobility services to remain acceptable or recover. **Effectiveness** asks whether an intervention achieves its declared engineering objective. **Resource efficiency** considers the resources required to produce that effect. **Sustainability consequences** describe admitted environmental or distributional consequences within a declared accounting boundary.

Existing Power–Transportation research demonstrates the relevance of these trade-offs. Coupled traffic–power resilience studies include budget and repair-resource constraints, while more recent planning studies combine resilience, investment or operating costs, and carbon-related objectives (Sun et al., 2025; Zou & Chen, 2019). More broadly, infrastructure-recovery studies show that resilience, cost, and greenhouse-gas outcomes can lead to different judgments about candidate recovery strategies (Mitoulis et al., 2023).

For the present thesis, direct intervention or recovery cost and operational electrical energy are treated as resource quantities. Carbon-dioxide-equivalent emissions constitute the planned core environmental sustainability consequence. Distributional accessibility remains conditional on adequate construct definition, data, population boundaries, and accounting rules.

This distinction also prevents service quantities from being counted twice. Electricity served, mobility provided, service loss, accessibility required for system function, and recovery time primarily characterize service and resilience. They are not automatically reclassified as independent sustainability outcomes. The interpretation of resilience quantities already depends strongly on the chosen performance measure, normalization, threshold, and time horizon (Poulin & Kane, 2021).

The thesis therefore asks a bounded question: when interventions provide similar resilience benefits, do their resource requirements or admitted sustainability consequences differ enough to change the engineering decision?

It does not assume that they will.

---

## 1.6 Scope, Boundaries, Assumptions, and Validity Domain

The thesis is deliberately bounded to the Power–Transportation problem required by the research questions. It is not intended to reproduce every physical, behavioral, institutional, economic, or environmental process affecting urban infrastructure.

The physical core is `P+T`. Information and Organization affect observation and feasible action but are not modeled as independent physical infrastructure networks unless a specific experiment requires such representation.

The principal service boundary is electricity and mobility. Physical states are included to the fidelity required to determine these services, qualified dependency mechanisms, disturbance effects, and feasible recovery or control.

The spatial boundary is defined by the geographic support over which the selected Power, Transportation, hazard, observation, and interface data can be aligned with sufficient provenance. Geographic co-location alone does not establish dependency.

The temporal boundary distinguishes data vintage, disturbance time, simulation horizon, and recovery horizon. These quantities serve different scientific purposes and are not treated as interchangeable.

Flooding is the principal planned demonstrator hazard, subject to Chapter 4 qualification. Exposure is distinguished from component damage, failure, and service consequence. A flood footprint can therefore establish potential exposure without establishing component failure probability or the resulting system response.

The research distinguishes the spatiotemporal system state `Y(x,t)`, operational or recovery control `u(x,t)`, and persistent engineering intervention `a_k`. Operational control changes how the existing infrastructure is used; an engineering intervention can alter system structure, capacity, redundancy, resources, or persistent operating capability.

The sustainability boundary remains intentionally narrow. Direct cost and operational energy are resource quantities; operational or otherwise explicitly bounded `CO_{2e}` is the principal environmental consequence. Distributional accessibility is conditional. Full life-cycle assessment, embodied-carbon assessment, biodiversity, water, public health, broad social-sustainability indices, and macroeconomic modeling are outside the present confirmatory core.

The thesis also separates its scientific domain from the specific datasets used for development and confirmatory testing. Development testbeds may support implementation, mechanism exploration, and model verification without defining the final empirical validity domain. Case selection, data provenance, spatial and temporal alignment, parameter readiness, and confirmatory execution are therefore established in Chapter 4.

Uncertainty can arise from hazards, dependency mechanisms, model form, parameter values, observations, interventions, resource estimates, and accounting assumptions. Probabilistic representations are used only where probability models are defensible; otherwise uncertainty is represented through scenarios, bounds, sensitivity analysis, or robust formulations.

All final claims are restricted to the systems, mechanisms, parameter ranges, hazards, observations, interventions, accounting boundaries, and validation evidence actually examined.

The governing inference rule is:

```math
\boxed{ \mathrm{Strength}(\text{claim}) \leq \mathrm{Strength}(\text{supporting evidence}). }
```

---

## 1.7 Research Framework and Scientific Logic

Within the bounded domain established in Section 1.6, the thesis uses a seven-stage scientific architecture. The architecture is a **thesis synthesis**, not an established seven-stage framework taken directly from the literature.

It begins with required electricity and mobility services and progresses through structure, causal qualification, dynamics, knowledge and action, resilience, intervention consequences, and decision:

```math
\boxed{ \begin{aligned} \text{Critical service requirements} &\rightarrow \text{Spatiotemporal P--T System-of-Systems structure}\\ &\rightarrow \text{Evidence-qualified directional dependencies}\\ &\rightarrow \text{Complex spatiotemporal coupled dynamics}\\ &\rightarrow \text{Spatiotemporal observation, estimation, organization and feasible control}\\ &\rightarrow \text{Uncertainty-aware spatiotemporal viability and recovery}\\ &\rightarrow \text{Spatially and temporally targeted intervention, resources and sustainability consequences}\\ &\rightarrow \text{Defensible engineering decision}. \end{aligned} }
```

The architecture is compatible with the service-centered System-of-Systems interpretation developed by Hall et al. (2016) and the separate-but-coupled treatment of energy and transportation used by Ibáñez et al. (2010), but the seven-stage integration itself is a proposed thesis construct.

**Stage 1** determines what systems, services, entities, states, spatial locations, temporal characteristics, and candidate interfaces constitute the bounded Power–Transportation System of Systems. It is structural rather than causal.

**Stage 2** determines which candidate relations can be accepted as evidence-qualified directional mechanisms, where and when they activate, and under what operating, hazard, delay, timescale, uncertainty, and validity conditions. Causal acceptance does not automatically establish that a mechanism is numerically ready for simulation.

**Stage 3** introduces dynamically ready mechanisms into the native physical representations of Power and Transportation and determines how their effects evolve and propagate across space and time. The purpose is to determine whether dynamic coupling provides meaningful information beyond simpler matched representations.

**Stage 4** connects the evolving spatiotemporal physical state to distributed observation, estimation, organizational conditions, and feasible control. It distinguishes what physically exists from what can be known and what can actually be done.

**Stage 5** asks where and when required services can remain acceptable, whether they can be recovered after violation, and how uncertainty affects those conclusions. Viability theory provides a formal basis for remain-within-acceptable-set reasoning, while recovery reachability addresses return after service violation (Béné & Doyen, 2018). Conventional performance and recovery measures remain comparators rather than being discarded (Poulin & Kane, 2021).

**Stage 6** uses resilience diagnosis to **inform the identification and comparison** of candidate engineering interventions, including their location, timing, and scale where relevant. Resilience effect, resource requirements, resource efficiency, and admitted sustainability consequences remain separate.

**Stage 7** evaluates which candidate intervention or transformation, including its location, timing, and scale where relevant, remains defensible under requirements, feasibility, uncertainty, resilience evidence, resource requirements, and admitted sustainability consequences. Sequential adaptation remains conditional rather than assumed.

Identification, verification, validation, uncertainty quantification, provenance, and reproducibility operate across the seven stages. They are scientific controls rather than an eighth stage.

---

## 1.8 General Research Objective

The general objective of this thesis is:

> **To develop and validate an evidence-grounded mathematical and engineering framework for coupled Power–Transportation infrastructure that connects spatiotemporal System-of-Systems structure and qualified directional interdependencies to complex spatiotemporal dynamics, observation, information and organizational constraints, feasible control, uncertainty-aware service viability and recovery, engineering intervention consequences, and defensible engineering decisions. Engineering interventions are evaluated through their resilience effects, resource requirements and efficiency, and admitted sustainability consequences.**

Validation is interpreted within the declared context and validity domain of the corresponding model, experiment, and evidence rather than as universal validation of the framework.

---

## 1.9 Research Questions

### RQ0 — Overarching Question

> **How can coupled Power–Transportation infrastructure be represented as an interdependent System of Systems and modeled as a spatiotemporal complex dynamical system to connect qualified directional dependencies, observation- and organization-constrained feasible response, uncertainty-aware service resilience, engineering intervention consequences, and defensible engineering decisions?**

### RQ1 — Spatiotemporal System-of-Systems Structure

> **What constituent systems, supporting Information and Organization domains, services, entities, states, spatial locations, temporal characteristics, and candidate interfaces constitute the bounded Power–Transportation System of Systems, and where and when can interactions occur?**

### RQ2 — Evidence-Qualified Spatiotemporal Directional Dependencies

> **Which candidate Power–Transportation relations can be admitted as evidence-qualified directional dependency mechanisms, through what mechanisms, where and when do they activate, under what operating and hazard conditions, with what delays, characteristic timescales, and uncertainty, and within what validity domain?**

### RQ3 — Complex Spatiotemporal Coupled Dynamics

> **How do qualified and dynamically ready directional dependency mechanisms evolve, interact, and propagate across space and time, and how do they alter coupled physical states and electricity and mobility service trajectories relative to independent and static-coupling representations?**

### RQ4 — Spatiotemporal Observation, Organization, and Feasible Response

> **How do spatially and temporally distributed observations, state estimation, information availability, organizational conditions, and feasible control shape the response and recovery of the evolving coupled Power–Transportation system?**

### RQ5 — Uncertainty-Aware Spatiotemporal Service Resilience

> **Under what spatiotemporal conditions can required electricity and mobility services remain acceptable or be recovered under feasible actions and uncertainty, and what additional engineering information do viability and reachability provide beyond conventional service-recovery measures?**

### RQ6 — Spatiotemporally Targeted Engineering Intervention Consequences

> **How do candidate engineering interventions, characterized by type, location, timing, and scale where relevant, differ in resilience effectiveness, resource requirements and efficiency, and admitted sustainability consequences under independently qualified requirements, declared accounting boundaries, and uncertainty?**

### RQ7 — Defensible Spatiotemporal Engineering Decision

> **Which candidate interventions or infrastructure transformations, including their location, timing, and scale where relevant, remain defensible when resilience, resource efficiency, admitted sustainability consequences, feasibility, and uncertainty are evaluated jointly?**

---

## 1.10 Specific Research Objectives

The objectives mirror the research questions one-to-one.

**SO1.** Define the bounded Power–Transportation System of Systems in terms of constituent systems, supporting Information and Organization domains, services, entities, states, spatial locations, temporal characteristics, and candidate interfaces.

**SO2.** Qualify candidate Power–Transportation relations as directional dependency mechanisms by establishing their mechanism, direction, spatial and temporal activation conditions, operating and hazard conditions, delays, characteristic timescales, evidence basis, uncertainty, and validity boundaries.

**SO3.** Develop and verify a physics-based complex spatiotemporal coupled dynamic representation and test the incremental explanatory or predictive information provided by dynamically ready coupling relative to independent and static-coupling representations.

**SO4.** Evaluate how spatially and temporally distributed measurement, state estimation, information availability, organizational conditions, and feasible control affect response timing, electricity and mobility service trajectories, and recovery.

**SO5.** Determine uncertainty-aware spatiotemporal service viability and recovery reachability, evaluate their incremental information beyond conventional service and recovery representations, and characterize interface criticality where the required evidence permits.

**SO6.** Quantify and compare candidate engineering interventions, including their type, location, timing, and scale where relevant, in terms of resilience effectiveness, resource requirements and efficiency, and admitted sustainability consequences within independently justified requirements and declared accounting boundaries.

**SO7.** Evaluate candidate interventions or infrastructure transformations, including their location, timing, and scale where relevant, jointly in terms of resilience, resource efficiency, admitted sustainability consequences, feasibility, and uncertainty; evaluate intervention sequences only where temporal decision structure, data, and validation support them.

The required traceability is

```math
\boxed{RQ_k\Longleftrightarrow SO_k,\qquad k=1,\ldots,7.}
```

---

## 1.11 Research Hypotheses and Test Logic

The thesis retains five primary confirmatory hypotheses. RQ1 and RQ2 establish the structural and causal prerequisites needed by the downstream tests rather than requiring additional hypotheses.

### H1 — Dynamic Causal Coupling

> **Under matched disturbances, initial conditions, service requirements, and exogenous conditions, an evidence-qualified dynamic Power–Transportation coupling representation provides meaningful incremental explanatory or predictive information for prespecified service-loss, propagation, cascade, or recovery outcomes relative to a corresponding static-coupling representation.**

The primary comparison is `M_2` against `M_1`, with the uncoupled representation `M_0` retained as a reference.

### H2 — Information, Organization, and Feasible Control

> **Under matched physical conditions and disturbances, changes in information availability and organizational conditions produce meaningful differences in state-estimation quality, feasible action, response timing, service trajectories, recovery, or downstream resilience outcomes.**

The corresponding comparisons are interpreted as **matched modeled contrasts**, not automatically as identified real-world causal effects.

### H3 — Viability and Recovery-Reachability Information

> **For the declared Power–Transportation test domain, uncertainty-aware viability and recovery-reachability information provides meaningful incremental predictive or decision-relevant information about service maintainability and acceptable recovery beyond prespecified conventional service and recovery measures.**

### H4 — Intervention Consequences

> **Across the prespecified intervention and scenario set, at least two resilience-effective engineering interventions produce materially different resource requirements, resource efficiencies, or admitted sustainability consequences under the declared comparison rule.**

### H5 — Joint Engineering Decision

> **Under the declared uncertainty domain, incorporating resource efficiency and admitted sustainability consequences together with feasibility and uncertainty materially changes the admissible or nondominated engineering decision set, dominance relations, or decision regret relative to resilience-only evaluation.**

A prerequisite or evidence failure that prevents the intended experiment from being executed results in **NOT TESTED**, not automatic non-support of the hypothesis.

---

## 1.12 Proposed Contributions

The thesis proposes six contribution areas.

**C1 — Bounded service-centered spatiotemporal Power–Transportation System-of-Systems representation.**
The thesis proposes a representation that preserves Power and Transportation as distinct physical constituent systems while using Information and Organization to represent conditions governing knowledge and feasible action.

**C2 — Evidence-qualified directional dependency representation.**
Candidate structural relations progress to directional dependencies only through explicit mechanism and evidence qualification.

**C3 — Controlled admission of dependency mechanisms into complex spatiotemporal coupled dynamics.**
If H1 is supported, the work will provide evidence concerning the incremental value of dynamically representing qualified mechanisms.

**C4 — Observation-, information-, and organization-constrained response.**
If H2 is supported, the work will provide evidence concerning how knowledge and feasible-action conditions change response and recovery.

**C5 — Uncertainty-aware viability and recovery assessment.**
If H3 is supported, the work will provide evidence concerning the additional engineering value of remain–recover–confidence information beyond conventional service-recovery representation.

**C6 — Intervention and decision evaluation.**
If H4 and H5 are supported, the work will provide evidence concerning whether resilience-effective alternatives differ in resource or sustainability consequences and whether those differences alter engineering decisions.

These are proposed contribution categories. Their final status depends on the corresponding evidence, experiment, verification, validation, uncertainty analysis, and validity domain.

```math
\boxed{ \text{proposed contribution} \neq \text{supported contribution} \neq \text{global novelty}. }
```

---

## 1.13 Thesis Organization

Chapter 2 establishes the literature and scientific foundations required by the research questions. It distinguishes established evidence from unresolved handoffs and provides the evidence base for the thesis definitions, mechanisms, comparators, and bounded research gap.

Chapter 3 formalizes the conceptual and mathematical framework. It defines the spatiotemporal Power–Transportation System-of-Systems architecture, dependency representation, complex spatiotemporal coupled dynamics, observation and estimation, feasible-control structure, viability and recovery reachability, intervention consequences, and decision objects.

Chapter 4 specifies the research methodology and experimental design. It establishes source and data qualification, case admissibility, spatial and temporal alignment, measurement models, identification, estimator admission, model verification, scenario design, matched experiments, validation, uncertainty quantification, sensitivity analysis, falsification rules, and reproducibility.

Chapter 5 reports the qualified results, including prerequisite case and model results before the confirmatory H1–H5 findings. Each result is reported with its comparator, uncertainty, decision or materiality criterion, and validity domain.

Chapter 6 interprets those results in relation to mechanisms, assumptions, rival explanations, prior literature, resource requirements, sustainability consequences, engineering decisions, transferability, and remaining uncertainty.

Chapter 7 answers the research questions at the level supported by the completed evidence, records the final hypothesis statuses, identifies supported contributions, states the validity limits of the research, and defines the unresolved research agenda.

The manuscript therefore follows one end-to-end argument:

```math
\boxed{ \text{Problem} \rightarrow \text{Evidence} \rightarrow \text{Framework} \rightarrow \text{Qualified Method} \rightarrow \text{Results} \rightarrow \text{Interpretation} \rightarrow \text{Engineering Conclusion}. }
```

---

# References

For the **final assembled thesis**, I would use one consolidated, alphabetized APA 7 References section in the back matter. The current GitHub practice of keeping `References cited in Section 1.x` blocks is useful for source traceability while drafting, but those duplicated section lists should not become separate bibliographies in the final manuscript.

- Béné, C., & Doyen, L. (2018). From resistance to transformation: A generic metric of resilience through viability. *Earth's Future, 6*(7), 979–996. [https://doi.org/10.1002/2017EF000660](https://doi.org/10.1002/2017EF000660)
- Chester, M., Underwood, B. S., Allenby, B., Garcia, M., Samaras, C., Markolf, S., Sanders, K., Preston, B., & Miller, T. R. (2021). Infrastructure resilience to navigate increasingly uncertain and complex conditions in the Anthropocene. *npj Urban Sustainability, 1*, Article 4. [https://doi.org/10.1038/s42949-021-00016-y](https://doi.org/10.1038/s42949-021-00016-y)
- Dasuni, K. A. L., Palliyaguru, R., Amaratunga, D., & Liyanawatta, T. N. (2025). Redefining ‘dependencies/interdependencies’ of critical infrastructure: A systematic review of the existing knowledgebase. *Sustainable and Resilient Infrastructure, 10*(2), 202–222. [https://doi.org/10.1080/23789689.2024.2403885](https://doi.org/10.1080/23789689.2024.2403885)
- Fan, J., He, P., Li, C., Zhao, C., & Ji, Y. (2024). A post-disaster restoration model for power-gas-transportation distribution networks considering spatial interdependency and energy hubs. *Electric Power Systems Research, 233*, 110505. [https://doi.org/10.1016/j.epsr.2024.110505](https://doi.org/10.1016/j.epsr.2024.110505)
- Fotouhi, H., Moryadee, S., & Miller-Hooks, E. (2017). Quantifying the resilience of an urban traffic-electric power coupled system. *Reliability Engineering & System Safety, 163*, 79–94. [https://doi.org/10.1016/j.ress.2017.01.026](https://doi.org/10.1016/j.ress.2017.01.026)
- Ghasemkhani, A., Basiri, M. A., & Nicholson, C. (2026). Interdependency and uncertainty in the resiliency of infrastructure networks: A comprehensive review. *International Journal of Critical Infrastructure Protection, 54*, 100866. [https://doi.org/10.1016/j.ijcip.2026.100866](https://doi.org/10.1016/j.ijcip.2026.100866)
- Gim, C., & Miller, C. A. (2022). Institutional interdependence and infrastructure resilience. *Current Opinion in Environmental Sustainability, 57*, 101203. [https://doi.org/10.1016/j.cosust.2022.101203](https://doi.org/10.1016/j.cosust.2022.101203)
- Hall, J. W., Nicholls, R. J., Hickford, A. J., & Tran, M. (2016). Introducing national infrastructure assessment. In J. W. Hall, M. Tran, A. J. Hickford, & R. J. Nicholls (Eds.), *The Future of National Infrastructure: A System-of-Systems Approach* (pp. 3–11). Cambridge University Press. [https://doi.org/10.1017/CBO9781107588745.002](https://doi.org/10.1017/CBO9781107588745.002)
- Helmrich, A., Markolf, S., Li, R., Carvalhaes, T., Kim, Y., Bondank, E., Natarajan, M., Ahmad, N., & Chester, M. (2021). Centralization and decentralization for resilient infrastructure and complexity. *Environmental Research: Infrastructure and Sustainability, 1*(2), 021001. [https://doi.org/10.1088/2634-4505/ac0a4f](https://doi.org/10.1088/2634-4505/ac0a4f)
- Ibáñez, E., Gkritza, K., McCalley, J., Aliprantis, D., Brown, R., Somani, A., & Wang, L. (2010). Interdependencies between energy and transportation systems for national long term planning. In *Sustainable and Resilient Critical Infrastructure Systems: Simulation, Modeling, and Intelligent Engineering* (pp. 53–76). Springer. [https://doi.org/10.1007/978-3-642-11405-2_2](https://doi.org/10.1007/978-3-642-11405-2_2)
- Kivelä, M., Arenas, A., Barthelemy, M., Gleeson, J. P., Moreno, Y., & Porter, M. A. (2014). Multilayer networks. *Journal of Complex Networks, 2*(3), 203–271. [https://doi.org/10.1093/comnet/cnu016](https://doi.org/10.1093/comnet/cnu016)
- Lian, X., Song, C., Li, Z., Qiu, L., & Liu, L. (2026). Resilience-oriented emergency resource dispatch for power–transportation coupled networks under rainstorm-induced flood hazards. *Applied Energy, 403*, 127004. [https://doi.org/10.1016/j.apenergy.2025.127004](https://doi.org/10.1016/j.apenergy.2025.127004)
- Maier, M. W. (1998). Architecting principles for systems-of-systems. *Systems Engineering, 1*(4), 267–284. [https://doi.org/10.1002/(SICI)1520-6858(1998)1:4%3C267::AID-SYS3%3E3.0.CO;2-D](https://doi.org/10.1002/\(SICI\)1520-6858\(1998\)1:4%3C267::AID-SYS3%3E3.0.CO;2-D)
- Mitoulis, S.-A., Bompa, D. V., & Argyroudis, S. (2023). Sustainability and climate resilience metrics and trade-offs in transport infrastructure asset recovery. *Transportation Research Part D: Transport and Environment, 121*, 103800. [https://doi.org/10.1016/j.trd.2023.103800](https://doi.org/10.1016/j.trd.2023.103800)
- Mohamed, A. A. A. (2019). On the rising interdependency between the power grid, ICT network, and e-mobility: Modeling and analysis. *Energies, 12*(10), 1874. [https://doi.org/10.3390/en12101874](https://doi.org/10.3390/en12101874)
- Oladigbolu, J., Bakare, M. S., Motlagh, S. G., Mujeeb, A., & Li, L. (2025). A review on transport and power systems planning-operation integrating electric vehicles, energy storage, and other distributed energy resources. *Journal of Energy Storage, 135*, 118419. [https://doi.org/10.1016/j.est.2025.118419](https://doi.org/10.1016/j.est.2025.118419)
- Ouyang, M. (2014). Review on modeling and simulation of interdependent critical infrastructure systems. *Reliability Engineering & System Safety, 121*, 43–60. [https://doi.org/10.1016/j.ress.2013.06.040](https://doi.org/10.1016/j.ress.2013.06.040)
- Poulin, C., & Kane, M. B. (2021). Infrastructure resilience curves: Performance measures and summary metrics. *Reliability Engineering & System Safety, 216*, 107926. [https://doi.org/10.1016/j.ress.2021.107926](https://doi.org/10.1016/j.ress.2021.107926)
- Rasoulkhani, K., & Mostafavi, A. (2018). Resilience as an emergent property of human-infrastructure dynamics: A multi-agent simulation model for characterizing regime shifts and tipping point behaviors in infrastructure systems. *PLOS ONE, 13*(11), e0207674. [https://doi.org/10.1371/journal.pone.0207674](https://doi.org/10.1371/journal.pone.0207674)
- Rinaldi, S. M., Peerenboom, J. P., & Kelly, T. K. (2001). Identifying, understanding, and analyzing critical infrastructure interdependencies. *IEEE Control Systems Magazine, 21*(6), 11–25. [https://doi.org/10.1109/37.969131](https://doi.org/10.1109/37.969131)
- Sun, Y., Huang, X., Wang, G., Zhang, X., Qiu, J., & Strbac, G. (2025). Low-carbon traffic resilience-enhanced robust planning of coupled transportation and power distribution network based on modified user equilibrium model. *Applied Energy, 397*, 126258. [https://doi.org/10.1016/j.apenergy.2025.126258](https://doi.org/10.1016/j.apenergy.2025.126258)
- Tong, W., Li, H. X., Nasirzadeh, F., Yao, F., & Ji, Y. (2025). Resilience of interdependent infrastructure networks: Review and future directions. *International Journal of Critical Infrastructure Protection, 51*, 100793. [https://doi.org/10.1016/j.ijcip.2025.100793](https://doi.org/10.1016/j.ijcip.2025.100793)
- Trucco, P., & Petrenj, B. (2023). Characterisation of resilience metrics in full-scale applications to interdependent infrastructure systems. *Reliability Engineering & System Safety, 235*, 109200. [https://doi.org/10.1016/j.ress.2023.109200](https://doi.org/10.1016/j.ress.2023.109200)
- Unterluggauer, T., Rich, J., Andersen, P. B., & Hashemi, S. (2022). Electric vehicle charging infrastructure planning for integrated transportation and power distribution networks: A review. *eTransportation, 12*, 100163. [https://doi.org/10.1016/j.etran.2022.100163](https://doi.org/10.1016/j.etran.2022.100163)
- Wang, S., Lu, Q.-C., Liu, L., Xu, P.-C., Wang, R., & Zhang, L. (2026). Interdependency analysis of coupled power and transportation networks considering the charging decision preferences of EV drivers. *Reliability Engineering & System Safety, 268*, 112005. [https://doi.org/10.1016/j.ress.2025.112005](https://doi.org/10.1016/j.ress.2025.112005)
- Wang, Y., Zhao, O., & Zhang, L. (2024). Multiplex networks in resilience modeling of critical infrastructure systems: A systematic review. *Reliability Engineering & System Safety, 250*, 110300. [https://doi.org/10.1016/j.ress.2024.110300](https://doi.org/10.1016/j.ress.2024.110300)
- Wei, W., Wu, D., Wu, Q., Shafie-khah, M., & Catalão, J. P. S. (2019). Interdependence between transportation system and power distribution system: A comprehensive review on models and applications. *Journal of Modern Power Systems and Clean Energy, 7*, 433–448. [https://doi.org/10.1007/s40565-019-0516-7](https://doi.org/10.1007/s40565-019-0516-7)
- Zhang, S., Li, Y., Zhang, H., Dui, H., & Cao, Y. (2026). A two-stage resilience enhancement framework for power distribution system coupled with intelligent transportation system. *Reliability Engineering & System Safety*. [https://doi.org/10.1016/j.ress.2026.113032](https://doi.org/10.1016/j.ress.2026.113032)
- Zou, Q., & Chen, S. (2019). Enhancing resilience of interdependent traffic-electric power system. *Reliability Engineering & System Safety, 191*, 106557. [https://doi.org/10.1016/j.ress.2019.106557](https://doi.org/10.1016/j.ress.2019.106557)

One governance point remains before this wording should replace the frozen Chapter 1 in GitHub: the revised **General Objective, RQ6/SO6, RQ7/SO7, and corresponding H4/H5 wording need a versioned authority amendment**. The scientific-writing standard requires that the manuscript and canonical RQ–SO–H authority remain synchronized; better wording cannot be silently substituted for frozen wording.