# 1.6 Scope, Boundaries, and Assumptions

The research problem established in Sections 1.1–1.5 spans interacting physical infrastructures, disturbance propagation, information and organizational constraints, resilience, engineering intervention, and sustainability consequences. A useful model of such a problem cannot represent every physical, institutional, behavioral, environmental, and economic process simultaneously. Infrastructure-resilience models are necessarily purpose-dependent abstractions whose credibility depends on whether the modeled functions, mechanisms, assumptions, data, and decision variables are appropriate to the question being addressed (Alderson et al., 2015; Ganguly & Mukherjee, 2023). This section therefore defines the scope within which subsequent mathematical models, experiments, and conclusions are intended to be valid. The boundary is deliberately narrower than the broader coupled-infrastructure problem introduced previously.

## 1.6.1 System and interdependency scope

The physical engineering core of the thesis comprises electric Power (P) and road Transportation (T), while Information (I) and Organization (O) are retained as supporting domains governing what can be observed, interpreted, authorized, coordinated, and implemented:

```math
\boxed{
\mathcal S=\{P,T,I,O\},
\qquad
\underbrace{P+T}_{\text{physical core}}
+
\underbrace{I+O}_{\text{supporting domains}}.
}
```

The System-of-Systems viewpoint defines this architectural boundary; the complex-dynamical viewpoint subsequently represents behavior within it. Power is modeled only to the fidelity required to represent relevant network structure, electricity-service state, component availability, coupling mechanisms, and feasible restoration or control actions. Transportation is modeled to the fidelity required to represent road connectivity, mobility and accessibility, travel conditions, disruption effects, and transportation-dependent access of relevant recovery resources. Detailed electromagnetic transients, protection-system operation, wholesale electricity markets, complete transmission-system behavior, and microscopic representation of all travelers are outside the core unless a specific research question requires their activation.

Cross-system coupling is likewise bounded. A relationship is admitted to the coupled model only when a directional mechanism can be specified through a source, receiver, physical or operational mechanism, activation condition, effect, evidence status, and validity domain. In particular, the study considers (P\rightarrow T) mechanisms where loss or availability of electrical service affects an eligible transportation function, and (T\rightarrow P) mechanisms where transportation conditions constrain eligible power-system recovery or mobile-resource access. Studies of coupled power and transportation restoration demonstrate that road availability can materially constrain repair crews and mobile energy resources and that assuming unconstrained access can distort restoration analysis (Anokhin et al., 2021; Liu et al., 2026). Simultaneous exposure of power and transportation assets to the same hazard is treated as **common exposure**, not by itself as evidence of causal dependency.

## 1.6.2 Spatial, temporal, and hazard boundaries

Spatial and temporal boundaries are treated as scientific properties of the model rather than incidental metadata. The study distinguishes the spatial support of the modeled case from municipal jurisdiction, utility service territory, and the unknown exact service territory of individual real-world assets. It likewise distinguishes source-data vintage, disturbance time, simulation horizon, and recovery horizon:

```math
\boxed{
\text{data vintage}
\neq
\text{disturbance time}
\neq
\text{simulation horizon}
\neq
\text{recovery horizon}.
}
```

The present case-study implementation is provisionally bounded to the `AUS-P5U-2018-V1` Austin configuration using the 2018 SMART-DS power benchmark and temporally compatible transportation evidence. It remains a **candidate case rather than an admissible empirical case** until the predefined power-materialization, spatial-overlap, transportation-topology, observation, cross-system mapping, hazard, and provenance gates pass. The SMART-DS network is therefore treated as a synthetic benchmark embedded within Austin-relevant spatial and observational support, not as proprietary Austin Energy feeder topology. This wording follows the current case authority, which classifies the case as **CANDIDATE CASE ONLY — NOT YET ADMISSIBLE**.

Flood is the primary candidate physical hazard for confirmatory coupled-disruption analysis. However, hazard representation is explicitly separated into exposure, physical damage or availability, and subsequent system consequence:

```math
\boxed{
\text{hazard footprint}
\neq
\text{fragility}
\neq
\text{failure probability}
\neq
\text{system consequence}.
}
```

This distinction is important because post-disaster infrastructure studies frequently prescribe damage states or failure scenarios rather than deriving them from a complete hazard process, while more detailed approaches use fragility or probabilistic hazard models (Xu et al., 2026). Accordingly, a static floodplain intersection may establish spatial exposure but does not establish event-time inundation depth, component fragility, or failure probability. Heat and other hazards are outside the primary confirmatory hazard scope unless separately qualified before the relevant experiment. Spatial and temporal scales used for hazard, network behavior, cross-system propagation, and restoration must remain mutually compatible (Kong & Simonovic, 2019).

## 1.6.3 States, operational controls, and infrastructure transformations

The thesis distinguishes the condition of the system from actions taken within the existing system and from persistent changes to the system:

```math
\boxed{
Y(t)\neq u(t)\neq a_k,
}
```

where (Y(t)) denotes the coupled system state, (u(t)) denotes feasible operational control using the existing architecture, and (a_k) denotes a candidate persistent engineering intervention. Operational controls may include routing, switching, dispatch, repair scheduling, or temporary coordination when supported by the relevant experiment. Candidate transformations may include hardening, redundancy, added storage or renewable capacity, charging-infrastructure modification, or persistent information/coordination capability when these alternatives pass the applicable evidence, feasibility, and data gates.

This distinction prevents emergency operation from being mislabeled as infrastructure transformation. Candidate transformations are generated and compared as engineering alternatives, but their desirability is not assumed. Engineering-design and human-centered/design-thinking principles may support later problem framing and generation of alternatives; systems-engineering research shows that such approaches can assist stakeholder-needs definition, requirements, architecture, design generation, prototyping, and validation (Weiland & Knizhnik, 2022). They do not replace the hypothesis testing, verification, validation, sensitivity analysis, and bounded inference governed by EGMIV-6.

## 1.6.4 Resilience and sustainable-engineering assessment boundary

The principal performance boundary is service-oriented. Power-system performance concerns required electricity service, whereas transportation performance concerns required mobility and aggregate accessibility. Recovery time and related Stage-5 quantities characterize resilience rather than sustainability. The thesis therefore preserves

```math
\boxed{
\text{service/resilience}
\neq
\text{resource use}
\neq
\text{sustainability consequence}.
}
```

The Stage-6/7 sustainability boundary follows the pre-H4/H5 admission audit rather than an unrestricted sustainability checklist. Direct intervention or recovery cost and operational electrical energy are the principal planned resource/efficiency quantities; operational or explicitly partial carbon/GHG is the principal planned environmental consequence. Crew/person-hours, fuel energy, and distributional accessibility remain conditional extensions. Full multi-category life-cycle assessment, embodied/material carbon, water consumption, biodiversity, public-health assessment, broad social-sustainability indices, and regional macroeconomic or employment modeling are outside the current quantitative core. The current governance explicitly retains this narrow scope and records that no conditional sustainability metric is yet authorized for confirmatory H4/H5 execution.

Consequently,

```math
\boxed{
\text{operational carbon}
\neq
\text{embodied carbon}
\neq
\text{full life-cycle carbon},
}
```

and any quantitative consequence is interpreted only within its declared spatial, temporal, process, reference-case, and accounting boundaries.

## 1.6.5 Uncertainty and modeling assumptions

Assumptions and uncertainties are treated as distinct scientific objects. An assumption is a declared simplification or proposition used to construct a tractable model; uncertainty describes incomplete knowledge or variability affecting model inputs, structure, observations, interventions, or consequences. Infrastructure-model outputs can be strongly conditioned by both parameter uncertainty and structural assumptions, particularly where direct validation data are sparse; systematic uncertainty and sensitivity analysis are therefore necessary to identify conclusions that depend critically on uncertain inputs or assumptions (Ganguly & Mukherjee, 2023; Salwey et al., 2026).

The thesis distinguishes, at minimum,

```math
\boxed{
\mathbf U=
\left\{
U_\eta,
U_{\mathbb I},
U_{\rm model},
U_\theta,
U_{\rm obs},
U_{\rm int},
U_{\rm acc}
\right\},
}
```

representing hazard, dependency/interface, model-form, parameter, observation/state-estimation, intervention/resource, and sustainability-accounting uncertainties, respectively. Their mathematical representation and propagation are deferred to Chapters 3 and 4.

The principal modeling assumptions are that (P) and (T) constitute the physical infrastructure core; (I) and (O) constrain observation and feasible action but are not modeled as complete physical networks unless required by a specified experiment; only evidence-qualified directional dependencies enter confirmatory coupled dynamics; synthetic or semisynthetic assets are not interpreted as proprietary real-world infrastructure without independent evidence; service-acceptability thresholds are declared before confirmatory evaluation; and sustainability consequences are interpreted only within their admitted accounting boundaries. Each material assumption is required to have an explicit rationale, consequence for inference, and sensitivity or validation route rather than being treated as an invisible modeling convenience.

## 1.6.6 Exclusions and validity domain

The thesis is not intended to constitute an all-sector urban-infrastructure model, a complete electricity-market or transmission-stability study, a microscopic model of all human travel behavior, a complete physical ICT-network model, an all-hazards assessment, a full life-cycle assessment, or an ecological, public-health, or macroeconomic impact model. These exclusions are deliberate controls on inference rather than claims that the excluded processes are unimportant. Similarly, conclusions derived from a qualified Austin benchmark configuration cannot be generalized automatically to other cities, utilities, hazards, coupling mechanisms, or infrastructure scales.

The resulting validity domain can therefore be expressed conceptually as

```math
\boxed{
\mathcal D_{\rm valid}
\subseteq
\mathcal S_{\rm modeled}
\times
\mathbb I_{\rm qualified}
\times
\mathcal H_{\rm declared}
\times
\Theta_{\rm tested}
\times
\mathcal B_{\rm accounting}.
}
```

Claims from the thesis are restricted to this domain and to the verification, validation, sensitivity, and uncertainty evidence actually obtained. Defining these boundaries establishes the research space within which the seven-stage framework can operate. Section 1.7 therefore moves from the **bounded research domain** defined here to the **research framework and scientific handoffs** used to analyze it.
