# Deck3 — Revised Chapter 1 Presentation

14 slides · Text-only master · Physics-based research · Evidence-qualified conceptual framework

Thesis: Physics-Based Mathematical Engineering of Power–Electrified Transportation Interdependencies for Resilience

This version integrates the scientific framework developed across the research, mathematical modeling, infographic design and Deck3 workflows.

The presentation follows a strict sequence: physical systems → extreme-heat exposure → research problem → scientific evidence → research questions → objectives → system boundary → mathematical formulation → methodology → engineering consequences.

Published findings receive author–year citations. Proposed mechanisms, hypotheses, mathematical structures and anticipated results are explicitly distinguished from established evidence.

## Slide 1 — Thesis Title

Physics-Based Mathematical Engineering of Power–Electrified Transportation Interdependencies for Resilience

Chapter 1 — Introduction

Dossiya Dakou Master of Science in Engineering (MSE) Sustainable Engineering Arizona State University

## Slide 2 — Presentation Outline

From the engineering problem to a physics-based investigation of infrastructure resilience.

1. Research context: Engineering background, extreme heat, research problem and existing scientific evidence.
2. Research definition: Research questions, objectives, physical system boundaries and candidate interdependencies.
3. Research approach: Governing physics, mathematical modeling, verification, service consequences and sustainability relevance.

## Slide 3 — Engineering Background

Power and Electrified Transportation are distinct physical systems whose operations interact through electrical charging interfaces.

- Power System (P): Electricity generation, conversion, delivery, protection and control support electricity services.
- Electrified Transportation (\\(T_e\\)): Charging infrastructure, batteries, vehicle electronics and propulsion support electric mobility.
- Electrical interaction: EV charging modifies distribution-network loading and may affect transformer thermal ageing (Hilshey et al., 2013; Qian et al., 2015).

Scientific distinction: A physical connection does not, by itself, establish a heat-conditioned causal interdependency.

## Slide 4 — Extreme-Heat Research Context

Extreme heat affects equipment thermal states through physical processes that develop over time.

- Power-side response: Transformer temperature depends on heat generation, cooling conditions and loading history (Hilshey et al., 2013; Qian et al., 2015).
- Transportation-side response: High ambient temperature can limit EVSE charging capability through equipment-specific thermal derating (Krama et al., 2026).
- Battery thermal behavior: Electrochemical processes and electrical operation contribute to battery heat generation (Bernardi et al., 1985).

Scientific distinction: Common ambient heating may produce separate responses without any directional cross-system propagation.

## Slide 5 — Research Problem and Conceptual Framework

Under extreme heat, can temperature-conditioned operating changes propagate between Power and Electrified Transportation systems and affect required services over time?

Candidate P → Tₑ

Transformer thermal state → applicable operating constraint → electrical supply or charging capability → possible mobility-service consequence.

Candidate Tₑ → P

EVSE/battery thermal condition → charging-control response → grid-side AC demand → transformer loading and thermal response.

Existing evidence: EV charging can affect transformer thermal loading and ageing (Hilshey et al., 2013; Qian et al., 2015), while charger thermal derating has been observed under extreme climatic conditions (Krama et al., 2026).

Unresolved question: Whether these component-level mechanisms produce attributable directional propagation, critical transition times and service consequences.

Both directional pathways are conditional research propositions, not confirmed effects.

## Slide 6 — Existing Knowledge and Research Opportunity

The literature establishes relevant equipment behavior, but the proposed coupled mechanisms require further scientific qualification.

- Transformer behavior: EV charging can influence transformer ageing, loading and disruption risk (Hilshey et al., 2013; Qian et al., 2015; Visakh & Selvan, 2023).
- Transportation equipment: Battery energy balances and EVSE thermal derating provide component-level physical foundations (Bernardi et al., 1985; Krama et al., 2026).
- Research opportunity: Examine whether independently supported equipment effects can be connected through measured electrical interfaces to explain state evolution, propagation delays and service consequences.

Novelty boundary: The closest-prior-art comparison remains open; an absence of previous integrated studies is not assumed.

## Slide 7 — Research Questions

The research investigates physical mechanisms, their state–time evolution and their consequences for required services.

RQ1 — Mechanism qualification

Which thermally sensitive physical states and directional interdependency mechanisms can be justified between Power and Electrified Transportation under extreme heat?

RQ2 — Mathematical representation

How can the qualified mechanisms be modeled to represent their evolution, operating constraints and propagation through physical state and time?

RQ3 — Engineering consequences

Under which conditions do critical transitions and attributable propagation delays occur, if any, and what are their consequences for electricity and mobility services?

These questions define the investigation; they do not presume positive coupling results.

## Slide 8 — General and Specific Research Objectives

The objectives translate the research questions into mechanism identification, physics-based modeling and consequence assessment.

General Objective

To characterize and model thermal interdependencies between the Power System and the Electrified Transportation System under extreme heat, and to quantify how their consequences evolve through physical state and time.

SO1 — Identify and qualify

Identify and qualify the thermally sensitive physical states and directional thermal interdependency mechanisms connecting the Power System and the Electrified Transportation System.

SO2 — Develop the mathematical model

Develop a physics-based state-time model of the qualified thermal interdependencies and their propagation under extreme heat.

SO3 — Quantify consequences

Quantify critical transition times, interdependency propagation delays, and the resulting electricity and mobility service consequences.

The previously approved General Objective and SO1–SO3 are retained verbatim.

## Slide 9 — Physical Systems, Components and Interdependency Boundary

The complete infrastructure architecture defines the system scope; the active model retains only components necessary to investigate qualified mechanisms.

- Power System: 19 candidate component and functional entries covering generation, distribution, transformation, conductors, protection, measurement, cooling and operational support.
- Electrified Transportation: 21 candidate entries covering EVSE, charging connections, vehicle batteries, power electronics, thermal management, propulsion, controls and mobility requirements.
- Selected electrical interface: Distribution feeder → transformer → grid-side AC measurement → EVSE → vehicle/battery.

Research configuration

- IEEE 13-node distribution network: B0 reference system and B1 documented EVSE extension.
- Candidate interface: XFM1 transformer, buses 633–634.
- IEEE 123-node distribution network: primary evaluation benchmark.
- Interface variables: \\(V\_{\mathrm{AC}}, I\_{\mathrm{AC}}, P\_{\mathrm{AC}}, Q\_{\mathrm{AC}}\\).

Modeling principle: The 40 entries establish traceable system coverage; they do not represent 40 installed devices, 40 mathematical states or 40 necessary equations.

## Slide 10 — Theoretical Foundations and Physics-Based Mathematical Model

Conservation laws, equipment-specific physical relationships and operational constraints determine the admissible mathematical model.

Theoretical foundations

- Conservation of energy and equipment-specific heat transfer.
- Electrical-network equations and interface power relationships.
- Continuous state evolution, algebraic constraints and discrete control modes.

General thermal-energy balance

\\[ \boxed{ \frac{dU\_{\mathrm{th}}}{dt} = P\_{\mathrm{heat}}-\dot Q\_{\mathrm{net,out}} } \\]

The thermal control volume, energy terms, sign convention and boundary conditions must be defined for each modeled component.

Proposed hybrid mathematical structure

\\[ \boxed{ \begin{aligned} M_q(x)\dot{x} &= f_q(x,z,u,T_a;\theta),\\\ 0 &= g_q(x,z,u,T_a;\theta) \end{aligned} } \\]

Where \\(x\\) represents selected dynamic states, \\(z\\) algebraic variables, \\(u\\) control inputs, \\(T_a\\) ambient thermal forcing, \\(\theta\\) model parameters and \\(q\\) discrete operating modes.

Scientific evidence: Bernardi et al. (1985) provide a battery-specific energy-balance foundation, not validation of the proposed complete coupled-system model.

Model status: Proposed formulation; constitutive relations, parameters and admissibility conditions remain to be qualified.

## Slide 11 — Research Methodology and Verification Strategy

The methodology progresses from component-level evidence to verified electrical models, qualified thermal dynamics and service-consequence assessment.

Stage 1 — Scientific evidence and system qualification

Review relevant physical mechanisms, classify the 40 candidate entries and identify necessary states, interfaces, controls and measurements.

Stage 2 — Electrical reference verification

Reproduce the unmodified IEEE 13-node system (B0), then construct a documented EVSE extension (B1).

Stage 3 — Physics-based model development

Introduce qualified thermal states, loss relationships, cooling processes and applicable operating constraints.

Stage 4 — Directional mechanism investigation

Examine P→Tₑ and Tₑ→P independently using comparable scenarios, grid-side AC quantities and explicit uncertainty assumptions.

Stage 5 — Primary evaluation

Use the IEEE 123-node system to assess the selected modeling approach and quantify defined critical times, propagation delays and service consequences where supported.

Verification boundary: Electrical model verification, thermal-model validation and evidence of cross-system causality are separate requirements.

B0/B1 results, coupled propagation effects and empirical validation have not yet been demonstrated.

## Slide 12 — Resilience, Sustainability and Engineering Consequences

Resilience is evaluated through required electricity and mobility services, while sustainability depends on the consequences of system behavior and engineering responses.

Resilience assessment

- Define required electricity and mobility services.
- Examine thermal-state evolution and operational constraints.
- Quantify service shortfalls, critical transitions and recovery where demonstrable.

Pathway 1 — Direct consequences

Qualified thermal interdependency → change in required service → environmental, economic and social implications.

Pathway 2 — Engineering responses

Improve / Adapt / Restore → change in service relative to a defined reference → environmental, economic and social implications.

Assessment dimensions

- Environmental: Electrical losses, energy use and associated environmental burdens.
- Economic: Operating costs, service interruption and intervention costs.
- Social: Electricity availability, mobility access and disruption consequences.

Published context: Visakh and Selvan (2023) investigate EV-charging-related distribution-transformer service disruption. The two sustainability pathways above are the proposed thesis assessment structure.

SDG relevance: Potential connections to SDGs 7, 9, 11 and 13 require explicitly defined indicators; project measurements are not automatically official UN SDG indicators.

## Slide 13 — Thesis Organization and Immediate Research Priorities

The thesis develops from physical evidence and theoretical foundations toward mathematical modeling, testing and defensible engineering conclusions.

Chapters 1–2 — Foundations

Research context, problem, questions, objectives, literature, physical systems and relevant theories.

Chapters 3–5 — Investigation

Conceptual framework, physical architecture, mathematical formulation, numerical methodology, verification and results.

Chapters 6–7 — Interpretation

Discussion, uncertainty, limitations, resilience and sustainability implications, conclusions and recommendations.

Immediate research priorities

1. Complete the closest-prior-art comparison and qualify the proposed directional mechanisms.
2. Establish the IEEE 13-node B0 reference electrical model and documented B1 EVSE configuration.
3. Define admissible thermal states, constitutive relationships, controls and measurement interfaces.
4. Specify falsifiable tests, comparator scenarios, uncertainty assessment and service metrics.
5. Develop the IEEE 123-node primary evaluation without assuming positive coupling results.

Research principle: A conceptual relationship is not causal evidence; a mathematical formulation is not a validated physical model; and successful numerical execution is not field validation.

## Slide 14 — References

Peer-reviewed journal articles only · Alphabetical order · APA style

Bernardi, D., Pawlikowski, E., & Newman, J. (1985). A general energy balance for battery systems. Journal of The Electrochemical Society, 132(1), 5–12. [https://doi.org/10.1149/1.2113792](https://doi.org/10.1149/1.2113792)

Hilshey, A. D., Hines, P. D. H., Rezaei, P., & Dowds, J. R. (2013). Estimating the impact of electric vehicle smart charging on distribution transformer aging. IEEE Transactions on Smart Grid, 4(2), 905–913. [https://doi.org/10.1109/TSG.2012.2217385](https://doi.org/10.1109/TSG.2012.2217385)

Krama, A., Kamal, N., Sezer, N., & Bayhan, S. (2026). Impact of extreme climatic conditions on fast EV charger performance: Field experimental insights from Qatar. Energy Conversion and Management: X, 31, Article 101960. [https://doi.org/10.1016/j.ecmx.2026.101960](https://doi.org/10.1016/j.ecmx.2026.101960)

Qian, K., Zhou, C., & Yuan, Y. (2015). Impacts of high penetration level of fully electric vehicles charging loads on the thermal ageing of power transformers. International Journal of Electrical Power & Energy Systems, 65, 102–112. [https://doi.org/10.1016/j.ijepes.2014.09.040](https://doi.org/10.1016/j.ijepes.2014.09.040)

Visakh, A., & Selvan, M. P. (2023). Analysis and mitigation of the impact of electric vehicle charging on service disruption of distribution transformers. Sustainable Energy, Grids and Networks, 35, Article 101096. [https://doi.org/10.1016/j.segan.2023.101096](https://doi.org/10.1016/j.segan.2023.101096)

## Scientific alignment of the 14-slide version

| Research requirement                                       | Where addressed |
| ---------------------------------------------------------- | --------------- |
| Physical systems and existing electrical interactions      | Slides 3, 9     |
| Extreme heat as an external forcing                        | Slide 4         |
| Conceptual framework and conditional mechanisms            | Slide 5         |
| Literature-grounded evidence and research opportunity      | Slide 6         |
| Three research questions                                   | Slide 7         |
| Exact General Objective and SO1–SO3                        | Slide 8         |
| Complete 40-entry system inventory versus active model     | Slide 9         |
| Theoretical foundations and mathematical representation    | Slide 10        |
| Numerical verification, scientific testing and uncertainty | Slide 11        |
| Service outcomes, resilience and sustainability            | Slide 12        |
| Research organization and next steps                       | Slide 13        |
| Published journal references                               | Slide 14        |

Three qualifications remain essential. The RQ wording on Slide 7 is a refined working formulation; it must be checked against the authoritative thesis RQ register before freezing. The literature comparison does not yet establish an original research gap conclusively. The proposed equations and directional mechanisms remain unvalidated until the specified scientific tests are completed.

This is the revised text master for Deck3, with distinct theoretical, conceptual, mathematical and numerical levels; selective use of the 40-component inventory; and an evidence-based distinction between established physics and mechanisms under investigation.