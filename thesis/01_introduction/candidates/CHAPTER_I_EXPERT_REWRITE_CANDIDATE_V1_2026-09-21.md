# Chapter 1 — Introduction: Research Problem and Scientific Contract

> **Candidate status:** Expert rewrite candidate — non-canonical until approved.  
> **Canonical controls preserved:** P+T / I+O ontology, RQ0–RQ7, SO1–SO7, H1–H5, seven-stage framework, scope, and validity logic.  
> **Editorial objective:** increase scientific information density without weakening evidence, mathematics, or traceability.

## 1.1 Background and Engineering Context

Electricity and mobility are critical infrastructure services delivered by physically distinct systems whose interfaces are increasing with transportation electrification. Electric-vehicle charging links mobility demand to the location, timing, capacity, and availability of electricity supply, while charging demand can alter distribution-system operation and planning. Vehicle-to-grid and mobile-energy applications add further Transportation-to-Power pathways when their technical and operating conditions are satisfied (Oladigbolu et al., 2025; Unterluggauer et al., 2022; Wei et al., 2019).

The coupling also affects recovery. Repair crews, replacement components, mobile generators, and other restoration resources require physical access to damaged electrical assets; transportation disruption can therefore delay power-system restoration (Fan et al., 2024; Lian et al., 2026).

The engineering problem is service-centered rather than asset-centered. Power infrastructure provides electricity; transportation infrastructure provides mobility and physical accessibility. Each system retains its own physics, topology, controls, and failure processes, while selected states, flows, constraints, or decisions can interact across systems (Hall et al., 2016; Ibáñez et al., 2010).

Directionality is therefore essential. Electricity availability can affect electrically dependent transportation functions, while transportation conditions can affect power restoration and, under qualified conditions, charging or mobile-energy behavior can affect the power system (Fan et al., 2024; Fotouhi et al., 2017; Wang et al., 2026). For this thesis,

\`\`\`math
\boxed{P\rightarrow T\not\Rightarrow T\rightarrow P}
\`\`\`

because evidence for one direction does not establish the reverse mechanism. The two directions can differ in mechanism, activation condition, magnitude, delay, characteristic timescale, uncertainty, and validity domain.

Structural proximity is also insufficient. A common flood can expose a road and an electrical component simultaneously without either infrastructure causing the other's state change; common exposure can therefore create correlated disruption without establishing directional dependency (Ouyang, 2014; Rinaldi et al., 2001).

The thesis consequently uses two complementary views. The **System-of-Systems view** represents architecture—constituent systems, services, entities, interfaces, and relations—whereas the **complex-dynamical-systems view** represents behavior—state evolution, disturbances, dependencies, feedback, controls, delays, and recovery (Maier, 1998; Ouyang, 2014; Rinaldi et al., 2001). The thesis-specific convention is

\`\`\`math
\boxed{\text{System of Systems}=\text{architectural view},\qquad
\text{complex dynamical system}=\text{behavioral view}.}
\`\`\`

The research problem therefore extends beyond showing that Power and Transportation are connected. It requires determining which relations are admissible as directional dependencies, what they do dynamically, what operators can know and feasibly do, whether required services can remain acceptable or recover, and how intervention consequences change the engineering decision.

---

## 1.2 Coupled Power–Transportation System Context

The thesis physical core is

\`\`\`math
\boxed{P+T},
\`\`\`

where \(P\) denotes the Power system and \(T\) the Transportation system. Information and Organization are supporting domains:

\`\`\`math
\boxed{I+O}.
\`\`\`

This ontology does not treat \(P,T,I,O\) as four equivalent physical infrastructures. Power and Transportation remain separate physical systems so that coupling does not erase system-specific physics or operational logic (Hall et al., 2016; Ibáñez et al., 2010).

The **Information domain** represents what can be measured, communicated, or estimated about the evolving physical system, including observation availability, communication status, missing data, delays, forecasts, and state estimates. Information availability does not by itself make an action executable (Mohamed, 2019; Rinaldi et al., 2001).

The **Organizational domain** represents the conditions through which information becomes feasible action, including authority, coordination, priorities, personnel, equipment, resource availability, and response delay. Human and institutional conditions can materially affect infrastructure response and adaptation (Chester et al., 2021; Helmrich et al., 2021; Rasoulkhani & Mostafavi, 2018).

The working ontology is therefore

\`\`\`math
\boxed{
\underbrace{P+T}_{\text{physical infrastructure}}
+
\underbrace{I+O}_{\text{knowledge and feasible-action support}}.
}
\`\`\`

The relationship taxonomy is stricter than the graph representation. A **structural relation** identifies where interaction could occur. A **directional dependency** additionally requires an interpretable mechanism, direction, activation conditions, evidence, and validity domain. A reciprocal **interdependency** requires relevant directional dependencies in both directions. **Dynamic coupling** requires sufficient specification for the qualified mechanism to enter the governing model.

Thus,

\`\`\`math
\boxed{
\text{candidate relation}
\rightarrow
\text{qualified directional dependency}
\rightarrow
\text{dynamically admissible coupling}.
}
\`\`\`

Multilayer-network mathematics can represent multiple layers and interlayer edges, but an interlayer edge is not treated here as evidence of causal or functional dependency (Kivelä et al., 2014).

Candidate \(P\rightarrow T\) mechanisms include electricity supply to charging infrastructure and other electrically dependent transportation functions; direct coupled studies document interactions among charging, transportation behavior, and distribution-system constraints (Fotouhi et al., 2017; Unterluggauer et al., 2022; Wei et al., 2019). Candidate \(T\rightarrow P\) mechanisms include transportation access required for repair and restoration; Fan et al. (2024) explicitly incorporate transportation-network states into post-disaster repair routing.

These Chapter-I mechanisms remain **candidate mechanism families**. Their inclusion does not establish case-specific dependency acceptance, parameter identifiability, numerical readiness, or authorization for dynamic simulation.

---

## 1.3 Problem Statement

Coupled-infrastructure modeling is not absent from the literature. Interdependent infrastructure has been represented through network, simulation, optimization, stochastic, and data-driven methods, while recent Power–Transportation studies address charging-mediated coupling, transportation-constrained restoration, flood-responsive recovery, emergency-resource coordination, and behavior-dependent charging (Lian et al., 2026; Oladigbolu et al., 2025; Ouyang, 2014; Wang et al., 2024; Wang et al., 2026).

The engineering problem addressed by this thesis is the **reliability of the scientific transitions connecting these capabilities**.

First, structure does not establish a qualified directional dependency. A graph can identify possible interaction without establishing mechanism, direction, activation, magnitude, or engineering relevance. Reviews continue to identify unresolved challenges in representing infrastructure interdependencies, uncertainty, and resilience consequences (Ghasemkhani et al., 2026; Wang et al., 2024).

Second, mechanism existence does not establish numerical identifiability. Even when a mechanism is physically admissible, its parameters may not be uniquely inferable from available observations. Transportation inverse-learning research shows that data quality, observation resolution, parameterization, and the balance between data fit and model consistency materially affect parameter recovery and out-of-sample generalization (Liu & Yin, 2026). The thesis therefore distinguishes

\`\`\`math
\boxed{
\text{mechanism existence}
\neq
\text{parameter identifiability}
\neq
\text{adequate parameter estimation}.
}
\`\`\`

Third, physical possibility does not establish feasible action. Operators act through measurements, estimated states, communication, authority, coordination, personnel, and resources; differences in those conditions can alter response and recovery even under matched physical disturbances (Chester et al., 2021; Rasoulkhani & Mostafavi, 2018).

Fourth, a realized service trajectory does not completely characterize resilience. Performance and recovery curves quantify degradation and restoration, but their interpretation depends on the chosen service variable, reference state, threshold, horizon, and summary metric (Poulin & Kane, 2021; Trucco & Petrenj, 2023). The distinct engineering questions are whether required service can remain acceptable and, after violation, whether acceptable service can be recovered under feasible actions and uncertainty.

Finally, resilience improvement does not determine the engineering decision. Interventions can produce similar resilience effects while requiring different direct intervention or recovery costs, operational energy, and admitted carbon-dioxide-equivalent consequences within the declared accounting boundary (Mitoulis et al., 2023; Sun et al., 2025; Zou & Chen, 2019).

The research problem is therefore end-to-end:

\`\`\`math
\boxed{
\begin{aligned}
\text{service requirements}
&\rightarrow \text{spatiotemporal P--T structure}
\rightarrow \text{qualified directional dependencies}\\
&\rightarrow \text{complex coupled dynamics}
\rightarrow \text{knowledge and feasible action}\\
&\rightarrow \text{service resilience under uncertainty}
\rightarrow \text{intervention consequences}
\rightarrow \text{engineering decision}.
\end{aligned}
}
\`\`\`

Every transition must be traceable so that the final engineering conclusion is no stronger than the evidence supporting the intermediate steps.

---

## 1.4 Research Gap

The research gap is not the absence of interdependent-infrastructure models, coupled Power–Transportation models, resilience measures, recovery optimization, viability theory, or multiobjective decision methods. Substantial work exists in each area (Ouyang, 2014; Tong et al., 2025; Wang et al., 2024).

The bounded gap is that the reviewed evidence does not by itself close every scientific handoff required to move from a candidate cross-system relation to a defensible engineering decision. Each handoff follows

\`\`\`math
\boxed{
\text{established capability}
\rightarrow
\text{documented limitation}
\rightarrow
\text{unresolved handoff}
\rightarrow
\text{thesis test}.
}
\`\`\`

### 1.4.1 G1 — Structure to Qualified Directional Dependency

Dependency taxonomies and multilayer representations are established, but structural relations, one-way dependencies, and reciprocal interdependencies can be conflated when mechanism and direction are not kept explicit (Dasuni et al., 2025; Kivelä et al., 2014; Ouyang, 2014).

\`\`\`math
\boxed{
\text{candidate structural relation}
\rightarrow
\text{evidence-qualified directional dependency}.
}
\`\`\`

RQ1 defines the bounded system and candidate interfaces; RQ2 tests whether each candidate relation satisfies the required mechanism, direction, activation, evidence, uncertainty, and validity conditions.

### 1.4.2 G2 — Qualified Directional Dependency to Dynamic Consequence

Dynamic P–T models already represent charging interactions, hazard-responsive traffic, emergency-resource movement, and multistage recovery (Lian et al., 2026; Wang et al., 2026; Zhang et al., 2027). Their existence does not establish the incremental engineering value of dynamically representing a qualified mechanism rather than using a simpler matched representation.

\`\`\`math
\boxed{
M_0\quad\text{vs.}\quad M_1\quad\text{vs.}\quad M_2
}
\`\`\`

where \(M_0\) represents independent systems, \(M_1\) static or algebraic coupling, and \(M_2\) evidence-qualified dynamic coupling. This handoff generates RQ3, SO3, and H1.

### 1.4.3 G3 — Physical Dynamics to Knowledge and Feasible Action

Information availability, institutional conditions, coordination, and human–infrastructure interaction are recognized as relevant to infrastructure resilience (Chester et al., 2021; Gim & Miller, 2022; Rasoulkhani & Mostafavi, 2018). The unresolved handoff is whether differences in observation, estimation, authorization, coordination, and executable action materially alter response and recovery under matched physical conditions. This handoff generates RQ4, SO4, and H2.

### 1.4.4 G4 — Service Trajectory to Viability, Recovery, and Uncertainty Qualification

Performance and recovery curves remain widely used, but their interpretation depends on the selected performance variable, reference state, threshold, horizon, and summary metric (Poulin & Kane, 2021; Trucco & Petrenj, 2023). Viability asks whether acceptable conditions can be maintained, whereas reachability asks whether an acceptable target can be reached under specified dynamics, controls, and uncertainty (Béné & Doyen, 2018; Doyen & De Lara, 2010; Vinod & Oishi, 2021).

The unresolved handoff is whether viability and recovery reachability provide meaningful incremental information beyond conventional service and recovery measures. This handoff generates RQ5, SO5, and H3.

### 1.4.5 G5 — Resilience Effect to Intervention Consequences

Resilience-effective interventions can differ in direct intervention or recovery cost, operational energy, and admitted environmental consequences; existing studies show that resilience, recovery, cost, and greenhouse-gas objectives can favor different strategies (Mitoulis et al., 2023; Sun et al., 2025; Zou & Chen, 2019).

\`\`\`math
\boxed{
\text{resilience effect}
\rightarrow
\text{resource and admitted sustainability consequences}.
}
\`\`\`

This handoff generates RQ6, SO6, and H4.

### 1.4.6 G6 — Intervention Consequences to Engineering Decision

Multiobjective infrastructure analysis is established, and recent resilience research emphasizes explicit trade-offs rather than assuming that improvement in one criterion determines the engineering choice (Tong et al., 2025). The unresolved question is whether resource efficiency, admitted sustainability consequences, feasibility, and uncertainty materially change the admissible or nondominated decision set relative to resilience-only evaluation. This handoff generates RQ7, SO7, and H5.

Together,

\`\`\`math
\boxed{
\text{Structure}
\rightarrow
\text{Qualified Dependency}
\rightarrow
\text{Dynamics}
\rightarrow
\text{Knowledge and Action}
\rightarrow
\text{Resilience}
\rightarrow
\text{Consequences}
\rightarrow
\text{Decision}.
}
\`\`\`

Identification operates across the chain whenever unknown quantities must be inferred from observations; it is therefore a cross-cutting requirement rather than an additional stage. The thesis is framed as an **integration, incremental-value, and validation problem**, not as a claim that its component methods are individually new.

---

## 1.5 Sustainable Engineering Significance

The Sustainable Engineering significance of this research lies in determining whether resilience-effective infrastructure interventions differ materially in the resources they require and the admitted sustainability consequences they create.

Four quantities remain distinct. **Resilience effect** describes how an intervention changes the ability of electricity and mobility services to remain acceptable or recover. **Effectiveness** asks whether the intervention achieves its declared engineering objective. **Resource efficiency** relates an engineering effect to the resources required to obtain it. **Sustainability consequence** denotes an admitted environmental or distributional consequence evaluated within a declared accounting boundary.

These quantities need not move together. Infrastructure-recovery studies demonstrate trade-offs among resilience, cost, energy, and greenhouse-gas objectives, while coupled P–T studies include budget, investment, operating-cost, recovery-resource, and carbon-related considerations (Mitoulis et al., 2023; Sun et al., 2025; Zou & Chen, 2019).

The thesis therefore uses a narrow consequence boundary. Direct intervention or recovery cost and operational electrical energy are treated as resource quantities. Carbon-dioxide-equivalent emissions are the principal planned environmental sustainability consequence within the qualified accounting boundary. Distributional accessibility is included only if its construct, population boundary, data, and accounting rules can be independently justified.

This separation prevents double counting: electricity served, mobility provided, service loss, accessibility required for infrastructure operation, and recovery time primarily describe service and resilience; they are not automatically independent sustainability outcomes.

The bounded Sustainable Engineering question is:

> **When candidate interventions produce resilience benefits, do their resource requirements, resource efficiencies, or admitted sustainability consequences differ enough to affect the engineering decision?**

The thesis does not assume that they will.

---

## 1.6 Scope, Boundaries, Assumptions, and Validity Domain

The thesis is bounded to the Power–Transportation problem defined by the research questions. It does not attempt to reproduce every physical, behavioral, institutional, economic, or environmental process affecting infrastructure.

| Boundary | Included | Not inferred or outside the confirmatory core |
|---|---|---|
| Physical infrastructure | Power + Transportation | Other physical infrastructure sectors |
| Supporting domains | Information + Organization | Automatic treatment of \(I\) and \(O\) as equivalent physical networks |
| Primary services | Electricity + mobility | Universal welfare or comprehensive societal-service modeling |
| Interaction | Qualified \(P\rightarrow T\) and \(T\rightarrow P\) mechanisms | Co-location or common exposure treated as dependency |
| Hazard | Flooding as principal planned demonstrator, subject to Chapter 4 qualification | Generalization to all hazards |
| Intervention | Operational/recovery control and persistent engineering interventions | Unbounded intervention families |
| Resources | Qualified direct cost and operational energy | Complete economic accounting |
| Environmental consequence | Qualified \(CO_{2e}\) within the declared boundary | Full life-cycle sustainability assessment |
| Distributional quantity | Accessibility where construct and data requirements are satisfied | Broad social-sustainability index |
| Validity | Tested systems, mechanisms, ranges, scenarios, and accounting boundaries | Universal generalization |

The physical core is \(P+T\); Information and Organization affect observation and feasible action but are not independent physical infrastructure networks unless a specific experiment requires such a representation.

The spatial boundary is the geographic support over which Power, Transportation, hazard, observation, and interface data can be aligned with sufficient provenance. Co-location alone does not establish dependency. The temporal boundary distinguishes data vintage, disturbance time, causal delay, characteristic timescale, simulation horizon, and recovery horizon.

Flooding is the principal planned demonstrator, subject to Chapter 4 qualification. Exposure, damage, component failure, and service consequence remain distinct; a flood footprint can establish potential exposure without establishing failure probability or system response.

The thesis also distinguishes the evolving physical state \(Y(x,t)\), operational or recovery control \(u(x,t)\), and persistent engineering intervention \(a_k\). Operational control changes how existing infrastructure is used; a persistent intervention can alter structure, capacity, redundancy, resource availability, or operating capability.

Development testbeds support implementation, mechanism exploration, numerical verification, and methodological development but do not define the final empirical validity domain. Chapter 4 therefore controls case selection, data provenance, spatial/temporal alignment, parameter readiness, and confirmatory admissibility.

Uncertainty can arise from hazards, dependency mechanisms, model form, parameters, observations, interventions, resource estimates, and accounting assumptions. Probability is used only when its semantics are defensible; otherwise uncertainty is represented through scenarios, bounds, sensitivity analysis, or robust formulations.

All final claims are restricted to the systems, mechanisms, parameter ranges, hazards, observations, interventions, accounting boundaries, and validation evidence actually examined:

\`\`\`math
\boxed{
\operatorname{Strength}(\text{claim})
\le
\operatorname{Strength}(\text{supporting evidence}).
}
\`\`\`

---

## 1.7 Research Framework and Scientific Logic

Within the bounded domain above, the thesis uses a seven-stage scientific architecture. The integration is a **thesis synthesis**, not a seven-stage framework adopted from one external source.

\`\`\`math
\boxed{
\begin{aligned}
\text{Critical service requirements}
&\rightarrow \text{Spatiotemporal P--T SoS structure}
\rightarrow \text{Qualified directional dependencies}\\
&\rightarrow \text{Complex coupled dynamics}
\rightarrow \text{Observation, estimation, organization, and feasible control}\\
&\rightarrow \text{Uncertainty-aware viability and recovery}
\rightarrow \text{Intervention consequences}
\rightarrow \text{Defensible engineering decision}.
\end{aligned}
}
\`\`\`

The architecture is compatible with service-centered System-of-Systems reasoning and separate-but-coupled energy–transport modeling (Hall et al., 2016; Ibáñez et al., 2010).

**Stage 1 — Spatiotemporal System-of-Systems Structure.** Define the bounded systems, services, entities, states, locations, temporal characteristics, and candidate interfaces without inferring dependency.

**Stage 2 — Evidence-Qualified Directional Dependencies.** Qualify candidate relations by mechanism, direction, activation conditions, operating/hazard context, delay, timescale, uncertainty, evidence, and validity; dependency acceptance does not imply numerical readiness.

**Stage 3 — Complex Spatiotemporal Coupled Dynamics.** Admit only dynamically ready mechanisms into native P and T models and test whether dynamic coupling adds meaningful information beyond matched independent and static representations.

**Stage 4 — Observation, Estimation, Organization, and Feasible Control.** Connect the physical state to what can be measured, estimated, communicated, authorized, coordinated, and executed:

\`\`\`math
Y\rightarrow y\rightarrow\widehat Y\rightarrow(I,O)\rightarrow\mathcal U_{\mathrm{feas}}\rightarrow u.
\`\`\`

**Stage 5 — Uncertainty-Aware Service Resilience.** Test whether required services can remain acceptable or recover under feasible actions and uncertainty, while retaining conventional service/recovery measures as explicit comparators (Béné & Doyen, 2018; Poulin & Kane, 2021; Vinod & Oishi, 2021).

**Stage 6 — Engineering Intervention Consequences.** Compare candidate interventions by resilience effectiveness, resource requirements, resource efficiency, and admitted sustainability consequences, with type, location, timing, and scale included where relevant.

**Stage 7 — Defensible Engineering Decision.** Evaluate qualified alternatives jointly under resilience, resource efficiency, admitted sustainability consequences, feasibility, and uncertainty without assuming a universal scalar optimum.

Identification, parameter provenance, verification, validation, uncertainty quantification, sensitivity, provenance, and reproducibility operate across the seven stages. In particular, inverse identification strengthens the Stage 2→3 handoff where unknown model quantities must be inferred from observations (Liu & Yin, 2026); it does not create an eighth stage.

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

The thesis proposes six contribution areas. At the Chapter-I stage they remain **proposed contributions**; their final status depends on evidence, experiment, verification, validation, uncertainty analysis, and validity domain.

### C1 — Bounded Service-Centered Spatiotemporal Power–Transportation System-of-Systems Representation

A bounded P–T representation that preserves Power and Transportation as distinct physical systems while representing Information and Organization as supporting domains governing knowledge and feasible action. The intended contribution is the thesis-specific integration, not the System-of-Systems concept itself.

### C2 — Evidence-Qualified Directional Dependency Representation

A mechanism-centered progression that separates common exposure, structural relation, observed association, directional dependency, reciprocal interdependency, and dynamic coupling; candidate relations become dependencies only after explicit qualification.

### C3 — Controlled Admission of Dependency Mechanisms into Coupled Dynamics

If H1 is supported, evidence concerning the incremental engineering value of dynamically representing qualified P–T mechanisms relative to simpler matched representations. The proposed contribution is controlled admission based on evidence and dynamic readiness, not coupling alone.

### C4 — Observation-, Information-, and Organization-Constrained Response

If H2 is supported, evidence concerning how observation, state estimation, information availability, organizational conditions, and feasible control alter response and recovery within the declared domain.

### C5 — Uncertainty-Aware Viability and Recovery Assessment

If H3 is supported, evidence concerning whether viability and recovery reachability add predictive or decision-relevant information beyond conventional service-recovery measures.

### C6 — Intervention and Engineering-Decision Evaluation

If H4 and H5 are supported, evidence concerning whether resilience-effective interventions differ materially in resource requirements, resource efficiency, or admitted sustainability consequences and whether those differences alter the engineering decision set.

The contribution chain is

\`\`\`math
\boxed{
\text{Representation}
\rightarrow
\text{Qualified Dependency}
\rightarrow
\text{Dynamics}
\rightarrow
\text{Feasible Response}
\rightarrow
\text{Resilience}
\rightarrow
\text{Intervention}
\rightarrow
\text{Decision}.
}
\`\`\`

The thesis does not claim novelty for the component ideas individually; System-of-Systems reasoning, infrastructure interdependency, coupled P–T modeling, resilience curves, viability/reachability, and multiobjective infrastructure decision analysis have established foundations (Doyen & De Lara, 2010; Maier, 1998; Ouyang, 2014; Poulin & Kane, 2021; Rinaldi et al., 2001; Vinod & Oishi, 2021; Wei et al., 2019).

The governing contribution boundary is

\`\`\`math
\boxed{
\text{proposed contribution}
\neq
\text{supported contribution}
\neq
\text{validated contribution}
\neq
\text{global novelty}.
}
\`\`\`

---

## 1.13 Thesis Organization

The remainder of the thesis executes the scientific contract established here.

**Chapter 2 — Literature Review and Scientific Foundations** establishes and critically synthesizes the evidence and theory needed to define mechanisms, comparators, concepts, and the bounded research gap.

**Chapter 3 — Conceptual and Mathematical Framework** formalizes the P–T architecture, dependency objects, coupled dynamics, observation/estimation, feasible control, service acceptability, viability, recovery reachability, intervention consequences, and decision objects.

**Chapter 4 — Research Methodology and Experimental Design** converts the research contract into reproducible tests through evidence qualification, case/data admissibility, alignment, identification, model realization, VVUQ, matched experiments, falsification rules, and reproducibility controls.

**Chapter 5 — Results** reports qualified prerequisite, model, and confirmatory results with comparator, uncertainty, materiality/decision criterion, validity domain, and hypothesis status.

**Chapter 6 — Discussion and Sustainable Engineering Implications** interprets supported results against mechanisms, assumptions, rival explanations, prior literature, resource and sustainability consequences, transferability, and remaining uncertainty.

**Chapter 7 — Conclusions and Future Work** answers RQ0 and RQ1–RQ7 at the level justified by the evidence, records H1–H5 status, identifies supported contributions, states validity limits, and defines unresolved work.

The thesis therefore follows

\`\`\`math
\boxed{
\text{Problem}
\rightarrow
\text{Evidence}
\rightarrow
\text{Mathematical Framework}
\rightarrow
\text{Qualified Method}
\rightarrow
\text{Results}
\rightarrow
\text{Interpretation}
\rightarrow
\text{Engineering Conclusion}.
}
\`\`\`

Chapter 1 defines what is studied, why it matters, what remains unresolved, what will be tested, what evidence is required, and the conditions under which later engineering conclusions are admissible.

# References

Béné, C., & Doyen, L. (2018). From resistance to transformation: A generic metric of resilience through viability. *Earth's Future, 6*(7), 979–996. [https://doi.org/10.1002/2017EF000660](https://doi.org/10.1002/2017EF000660)

Chester, M., Underwood, B. S., Allenby, B., Garcia, M., Samaras, C., Markolf, S., Sanders, K., Preston, B., & Miller, T. R. (2021). Infrastructure resilience to navigate increasingly uncertain and complex conditions in the Anthropocene. *npj Urban Sustainability, 1*, Article 4. [https://doi.org/10.1038/s42949-021-00016-y](https://doi.org/10.1038/s42949-021-00016-y)

Dasuni, K. A. L., Palliyaguru, R., Amaratunga, D., & Liyanawatta, T. N. (2025). Redefining ‘dependencies/interdependencies’ of critical infrastructure: A systematic review of the existing knowledgebase. *Sustainable and Resilient Infrastructure, 10*(2), 202–222. [https://doi.org/10.1080/23789689.2024.2403885](https://doi.org/10.1080/23789689.2024.2403885)

Doyen, L., & De Lara, M. (2010). Stochastic viability and dynamic programming. *Systems & Control Letters, 59*(10), 629–634. [https://doi.org/10.1016/j.sysconle.2010.07.008](https://doi.org/10.1016/j.sysconle.2010.07.008)

Fan, J., He, P., Li, C., Zhao, C., & Ji, Y. (2024). A post-disaster restoration model for power-gas-transportation distribution networks considering spatial interdependency and energy hubs. *Electric Power Systems Research, 233*, 110505. [https://doi.org/10.1016/j.epsr.2024.110505](https://doi.org/10.1016/j.epsr.2024.110505)

Fotouhi, H., Moryadee, S., & Miller-Hooks, E. (2017). Quantifying the resilience of an urban traffic-electric power coupled system. *Reliability Engineering & System Safety, 163*, 79–94. [https://doi.org/10.1016/j.ress.2017.01.026](https://doi.org/10.1016/j.ress.2017.01.026)

Ghasemkhani, A., Basiri, M. A., & Nicholson, C. (2026). Interdependency and uncertainty in the resiliency of infrastructure networks: A comprehensive review. *International Journal of Critical Infrastructure Protection, 54*, 100866. [https://doi.org/10.1016/j.ijcip.2026.100866](https://doi.org/10.1016/j.ijcip.2026.100866)

Gim, C., & Miller, C. A. (2022). Institutional interdependence and infrastructure resilience. *Current Opinion in Environmental Sustainability, 57*, 101203. [https://doi.org/10.1016/j.cosust.2022.101203](https://doi.org/10.1016/j.cosust.2022.101203)

Hall, J. W., Nicholls, R. J., Hickford, A. J., & Tran, M. (2016). Introducing national infrastructure assessment. In J. W. Hall, M. Tran, A. J. Hickford, & R. J. Nicholls (Eds.), *The future of national infrastructure: A system-of-systems approach* (pp. 3–11). Cambridge University Press. [https://doi.org/10.1017/CBO9781107588745.002](https://doi.org/10.1017/CBO9781107588745.002)

Helmrich, A., Markolf, S., Li, R., Carvalhaes, T., Kim, Y., Bondank, E., Natarajan, M., Ahmad, N., & Chester, M. (2021). Centralization and decentralization for resilient infrastructure and complexity. *Environmental Research: Infrastructure and Sustainability, 1*(2), 021001. [https://doi.org/10.1088/2634-4505/ac0a4f](https://doi.org/10.1088/2634-4505/ac0a4f)

Ibáñez, E., Gkritza, K., McCalley, J., Aliprantis, D., Brown, R., Somani, A., & Wang, L. (2010). Interdependencies between energy and transportation systems for national long term planning. In *Sustainable and resilient critical infrastructure systems: Simulation, modeling, and intelligent engineering* (pp. 53–76). Springer. [https://doi.org/10.1007/978-3-642-11405-2_2](https://doi.org/10.1007/978-3-642-11405-2_2)

Kivelä, M., Arenas, A., Barthelemy, M., Gleeson, J. P., Moreno, Y., & Porter, M. A. (2014). Multilayer networks. *Journal of Complex Networks, 2*(3), 203–271. [https://doi.org/10.1093/comnet/cnu016](https://doi.org/10.1093/comnet/cnu016)

Lian, X., Song, C., Li, Z., Qiu, L., & Liu, L. (2026). Resilience-oriented emergency resource dispatch for power–transportation coupled networks under rainstorm-induced flood hazards. *Applied Energy, 403*, 127004. [https://doi.org/10.1016/j.apenergy.2025.127004](https://doi.org/10.1016/j.apenergy.2025.127004)

Liu, Z., & Yin, Y. (2026). Constructing transportation network equilibrium models from empirical data: An inverse learning perspective. *Transportation Research Part B: Methodological, 214*, 103597. [https://doi.org/10.1016/j.trb.2026.103597](https://doi.org/10.1016/j.trb.2026.103597)

Maier, M. W. (1998). Architecting principles for systems-of-systems. *Systems Engineering, 1*(4), 267–284. [https://doi.org/10.1002/(SICI)1520-6858(1998)1:4%3C267::AID-SYS3%3E3.0.CO;2-D](https://doi.org/10.1002/\(SICI\)1520-6858\(1998\)1:4%3C267::AID-SYS3%3E3.0.CO;2-D)

Mitoulis, S.-A., Bompa, D. V., & Argyroudis, S. (2023). Sustainability and climate resilience metrics and trade-offs in transport infrastructure asset recovery. *Transportation Research Part D: Transport and Environment, 121*, 103800. [https://doi.org/10.1016/j.trd.2023.103800](https://doi.org/10.1016/j.trd.2023.103800)

Mohamed, A. A. A. (2019). On the rising interdependency between the power grid, ICT network, and e-mobility: Modeling and analysis. *Energies, 12*(10), 1874. [https://doi.org/10.3390/en12101874](https://doi.org/10.3390/en12101874)

Oladigbolu, J., Bakare, M. S., Motlagh, S. G., Mujeeb, A., & Li, L. (2025). A review on transport and power systems planning-operation integrating electric vehicles, energy storage, and other distributed energy resources. *Journal of Energy Storage, 135*, 118419. [https://doi.org/10.1016/j.est.2025.118419](https://doi.org/10.1016/j.est.2025.118419)

Ouyang, M. (2014). Review on modeling and simulation of interdependent critical infrastructure systems. *Reliability Engineering & System Safety, 121*, 43–60. [https://doi.org/10.1016/j.ress.2013.06.040](https://doi.org/10.1016/j.ress.2013.06.040)

Poulin, C., & Kane, M. B. (2021). Infrastructure resilience curves: Performance measures and summary metrics. *Reliability Engineering & System Safety, 216*, 107926. [https://doi.org/10.1016/j.ress.2021.107926](https://doi.org/10.1016/j.ress.2021.107926)

Rasoulkhani, K., & Mostafavi, A. (2018). Resilience as an emergent property of human-infrastructure dynamics: A multi-agent simulation model for characterizing regime shifts and tipping point behaviors in infrastructure systems. *PLOS ONE, 13*(11), e0207674. [https://doi.org/10.1371/journal.pone.0207674](https://doi.org/10.1371/journal.pone.0207674)

Rinaldi, S. M., Peerenboom, J. P., & Kelly, T. K. (2001). Identifying, understanding, and analyzing critical infrastructure interdependencies. *IEEE Control Systems Magazine, 21*(6), 11–25. [https://doi.org/10.1109/37.969131](https://doi.org/10.1109/37.969131)

Sun, Y., Huang, X., Wang, G., Zhang, X., Qiu, J., & Strbac, G. (2025). Low-carbon traffic resilience-enhanced robust planning of coupled transportation and power distribution network based on modified user equilibrium model. *Applied Energy, 397*, 126258. [https://doi.org/10.1016/j.apenergy.2025.126258](https://doi.org/10.1016/j.apenergy.2025.126258)

Tong, W., Li, H. X., Nasirzadeh, F., Yao, F., & Ji, Y. (2025). Resilience of interdependent infrastructure networks: Review and future directions. *International Journal of Critical Infrastructure Protection, 51*, 100793. [https://doi.org/10.1016/j.ijcip.2025.100793](https://doi.org/10.1016/j.ijcip.2025.100793)

Trucco, P., & Petrenj, B. (2023). Characterisation of resilience metrics in full-scale applications to interdependent infrastructure systems. *Reliability Engineering & System Safety, 235*, 109200. [https://doi.org/10.1016/j.ress.2023.109200](https://doi.org/10.1016/j.ress.2023.109200)

Unterluggauer, T., Rich, J., Andersen, P. B., & Hashemi, S. (2022). Electric vehicle charging infrastructure planning for integrated transportation and power distribution networks: A review. *eTransportation, 12*, 100163. [https://doi.org/10.1016/j.etran.2022.100163](https://doi.org/10.1016/j.etran.2022.100163)

Vinod, A. P., & Oishi, M. M. K. (2021). Stochastic reachability of a target tube: Theory and computation. *Automatica, 125*, 109458. [https://doi.org/10.1016/j.automatica.2020.109458](https://doi.org/10.1016/j.automatica.2020.109458)

Wang, S., Lu, Q.-C., Liu, L., Xu, P.-C., Wang, R., & Zhang, L. (2026). Interdependency analysis of coupled power and transportation networks considering the charging decision preferences of EV drivers. *Reliability Engineering & System Safety, 268*, 112005. [https://doi.org/10.1016/j.ress.2025.112005](https://doi.org/10.1016/j.ress.2025.112005)

Wang, Y., Zhao, O., & Zhang, L. (2024). Multiplex networks in resilience modeling of critical infrastructure systems: A systematic review. *Reliability Engineering & System Safety, 250*, 110300. [https://doi.org/10.1016/j.ress.2024.110300](https://doi.org/10.1016/j.ress.2024.110300)

Wei, W., Wu, D., Wu, Q., Shafie-khah, M., & Catalão, J. P. S. (2019). Interdependence between transportation system and power distribution system: A comprehensive review on models and applications. *Journal of Modern Power Systems and Clean Energy, 7*, 433–448. [https://doi.org/10.1007/s40565-019-0516-7](https://doi.org/10.1007/s40565-019-0516-7)

Zhang, S., Li, Y., Zhang, H., Dui, H., & Cao, Y. (2027). A two-stage resilience enhancement framework for power distribution system coupled with intelligent transportation system. *Reliability Engineering & System Safety, 277*, 113032. [https://doi.org/10.1016/j.ress.2026.113032](https://doi.org/10.1016/j.ress.2026.113032)

Zou, Q., & Chen, S. (2019). Enhancing resilience of interdependent traffic-electric power system. *Reliability Engineering & System Safety, 191*, 106557. [https://doi.org/10.1016/j.ress.2019.106557](https://doi.org/10.1016/j.ress.2019.106557)
