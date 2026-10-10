# Physics–Mathematics-First Thesis Foundation and Hypothesis-Testing Scope Directive — V1

**Recorded:** 2026-10-10  
**Decision:** USER-APPROVED RESEARCH METHODOLOGY AND SCOPE CLARIFICATION  
**Applies to:** Active MSE thesis research planning, literature evidence extraction, physical mechanisms, model development, mathematical analysis, research hypotheses, numerical investigations, research questions, case selection and interpretation.  
**Authority boundary:** This document records an approved **methodological scope discipline**. It does **not** amend the frozen thesis title, the exact General Objective or SO1–SO3, conceptual V5, mathematical V3, state–time definitions, full Electrified Transportation System boundary, two-pathway sustainability assessment, or the selected eight-component roster. In a conflict, those frozen authorities govern.

## 1. Controlling research-scope statement — user-approved

> This research develops and investigates a physics-based mathematical framework for thermal interdependencies between Power and Electrified Transportation Systems under extreme heat. Its foundation is the formulation and analysis of governing physical laws, coupled state–time dynamics and operating constraints. Data are used to test the research hypotheses and evaluate the validity of predicted interdependencies and service consequences. AI and digital-twin development are excluded from the present scope, although the mathematical foundation may support such applications in future research.

**Central scientific contribution sought:** mathematical understanding of thermally conditioned, physically qualified directional interdependencies and their consequences for required electricity and mobility service resilience—not an AI model, a digital twin or a data-driven prediction system.

**Binding emphasis:** Physics and mathematics are the substantive research work. Data serve **hypothesis testing and the evidence-based evaluation of mathematical predictions** only, as opposed to defining a separate data-analysis, data-driven model-development, AI or digital-twin objective. Data processing required to evaluate an existing physical hypothesis is supporting experimental/scientific method, not a separate scientific product.

## 2. Explicit scientific order

\`\`\`math
\boxed{
\underbrace{\text{Physical Laws}}_{\text{Foundation}}
\longrightarrow
\underbrace{\text{Mathematical Formulation}}_{\text{Core Research}}
\longrightarrow
\underbrace{\text{Testable Hypotheses}}_{\text{Scientific Claims}}
\longrightarrow
\underbrace{\text{Evidence-Based Testing}}_{\text{Use of Data}}
}
\`\`\`

The arrows denote **research reasoning**, not an assertion that the scientific process is a one-pass pipeline: failed hypotheses, conservation tests or insufficient observations require revision of stated assumptions and re-examination of the same physical/mathematical problem. This iteration creates no independent AI, digital-twin or general-purpose data-science track.

| Element | Role in the thesis | Scope discipline |
|---|---|---|
| **Physics** | Establish energy conservation, heat transfer, electrical behavior and physically supported interdependencies. | Device law and interface claims require applicable physical evidence; shared ambient heat or electrical transfer alone is not a thermal interdependency. |
| **Mathematics** | Formulate governing equations, coupled dynamics, constraints, critical transitions and propagation through time. | Derive under explicitly stated assumptions; do not add states, parameters, thresholds or interfaces solely to increase complexity. |
| **Research hypotheses** | State specific, falsifiable predictions about thermal interdependencies and service consequences. | Specify distinguishable mechanism, predicted measurable consequence, controls and credible disconfirming result **before** testing. |
| **Data** | Test hypotheses, assess agreement between mathematical predictions and observations, and establish limitations. | Supporting evidence only; no separate predictive-ML or data-driven research objective. Existing/public data or a justified controlled test may be used if fit for the hypothesis. |
| **AI and digital twins** | **Outside the current research scope.** The physics/mathematics may furnish a foundation for later applications. | Do not design, train, benchmark or claim an AI application/digital twin as a current thesis output. |

## 3. Required mathematical and physical rigor

The active physical and mathematical investigation addresses:

1. **Governing equations.** Start from conservation of electrical/thermal energy, relevant circuit relations and physically admissible heat transfer. Derive reduced relations only with declared control volumes, boundary and initial conditions, valid units and explicit device assumptions.
2. **Coupled dynamics.** Mathematically connect **qualified directional mechanisms**, not arbitrary graph edges or two unrelated thermal states driven by the same heat exposure. Distinguish AC interface quantities, thermal state changes, equipment capability, actually implemented control, service delivery, and interface direction.
3. **State and time.** Treat thermal storage/inertia, evolving physical states, critical events and propagation through time. Define threshold, operating-action, recipient-response, service-shortfall and recovery times separately; a propagation delay needs an evidence-supported source→receiver causal pathway.
4. **Mathematical validity.** Test dimensional/physical consistency, nonnegative energy/loss where applicable, admissible states and conservation residuals; analyze well-posedness and solution properties to the degree justified by the adopted equations (not a blanket claim of a proof). State the parameter/forcing domain where a result applies.
5. **Hypothesis testing with data.** Derive observable implications, define refutable hypotheses, identify needed measurements and matched comparisons, then compare predicted versus observed component/interface/service behavior with measurement and model uncertainty. If the data cannot distinguish two mechanisms, report **not identifiable / unresolved**, not confirmed.
6. **Resilience.** Quantify physically traceable consequences for *required* electricity and mobility services, their maintenance/degradation and recovery when modeled. Charging efficiency, kWh losses, battery readiness and downstream sustainability are supporting outcome quantities, **not stand-alone definitions of resilience**.

**Minimum-sufficient physics:** The thesis must not force eight independent ODEs because eight physical subjects were selected. Algebraic port relationships, hybrid constraints and energy/service outputs are legitimate. Battery SOC is energy state rather than thermal state; heat exposure is forcing, not internal thermal state; cooling P4 and T3 are internal heat-rejection mechanisms rather than separate cross-system interfaces.

## 4. Research hypothesis-testing contract

For each future hypothesis, record **before** inspecting its test results:

| Field | Requirement |
|---|---|
| Physical mechanism | Real source/receiver components, physical input/output ports, direction, heat/temperature-dependence and exclusion of common-cause-only interpretation. |
| Governing mathematics | Conservation-derived relation plus device-appropriate constitutive law, assumptions and validity range, with dimensions/units. |
| Hypothesis and counter-hypothesis | Falsifiable outcome prediction and a physically credible simpler/null alternative (e.g., electrical-only interface, no temperature-conditioned control). |
| Measurable consequence | Observed component state, capability, actual AC interface response, service onset/shortfall, loss, readiness or validated time-to-event, with explicit measurement positions. |
| Testing logic | Independent or otherwise valid comparison controlling relevant ambient conditions, non-EV demand, charging request, initial conditions and temporal alignment; avoid mistaking mere simulation differences for physical validation. |
| Uncertainty and decision | Measurement error, model-form limitations, possible nonidentifiability, declared pass/fail/inconclusive logic and the domain to which results apply. |

**No pre-existing data or validated hypothesis is asserted here.** Numerical simulation can check equation implications and internal consistency, but observational/experimental data appropriate to the hypothesis are needed for empirical corroboration. Mathematical verification, physical validation and hypothesis testing are related but nonidentical scientific activities.

## 5. Strict in-scope and out-of-scope interpretation

**Current research substance:** physical laws; physics-based mathematical formulation and analysis; minimum-sufficient coupled state–time dynamics; thermally conditioned operating limits; directional mechanism qualification; mathematically expressed electricity and mobility services; physically interpretable critical times, propagation and resilience consequences; hypothesis testing against suitable evidence; bounded energy/sustainability consequence interpretation already authorized by canonical scope.

**Not a current independent research product:** machine-learning or artificial-intelligence design/training/optimization; digital-twin architecture/software/data pipelines/live state synchronization; autonomous AI forecasting; general data analytics; broad nonthermal cross-infrastructure coupling; generic road-traffic optimization; adding a new specific research objective for any of these.

**Future-enabling design principle, not future-project execution:** Define precise physical states, equations, observable outputs, identifiable parameters, explicit interfaces and uncertainty/validity domains. These provide rigorous foundations from which other researchers *could* later develop data/AI/digital-twin applications, without making those applications part of this thesis.

## 6. Relationship to approved eight components

The research remains grounded in exactly:

**Power System (P):**
1. P1 — Distribution Transformer
2. P2 — Distribution Feeder
3. P3 — Transformer Protection/Load-Management Hardware
4. P4 — Transformer Cooling Equipment

**Electrified Transportation System (T):**
1. T1 — DC EV Charger
2. T2 — Vehicle Battery Pack
3. T3 — EVSE Cooling Equipment
4. T4 — Vehicle HVAC Equipment

These are **interface-centered component research subjects**, not eight cross-system interfaces and not a claim that eight independent thermal states must be modeled. Distinguish genuine P→T and T→P directional thermal interactions from within-system cooling, energy storage, vehicle HVAC load and the universal AC electricity-supply pathway.

## 7. Unmodified frozen objectives (verbatim)

**General Research Objective**

> To characterize and model thermal interdependencies between the Power System and the Electrified Transportation System under extreme heat, and to quantify how their consequences evolve through physical state and time.

**SO1**

> Identify and qualify the thermally sensitive physical states and directional thermal interdependency mechanisms connecting the Power System and the Electrified Transportation System.

**SO2**

> Develop a physics-based state-time model of the qualified thermal interdependencies and their propagation under extreme heat.

**SO3**

> Quantify critical transition times, interdependency propagation delays, and the resulting electricity and mobility service consequences.

The governing scientific progression **Identify/Qualify → Mathematically Model → Quantify Consequences** is fully compatible with the physics → mathematics → hypotheses → evidence methodological sequence. This directive provides **how** work is conducted, not revised objectives or added hypotheses.

## 8. Traceability and authority

- [Canonical thermal interdependency scope (frozen)](CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md)
- [Canonical frozen research objectives](CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md)
- [Canonical state–time semantics](CANONICAL_STATE_TIME_DEFINITIONS_V1.md)
- [Canonical evidence and non-invention requirements](CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md)
- [Canonical resilience](CANONICAL_RESILIENCE_DEFINITION_V1.md)
- [Canonical sustainability two pathways](CANONICAL_SUSTAINABILITY_TWO_PATHWAY_ASSESSMENT_V1.md)
- [Approved eight-component selection](thermal_sos_functional_architecture/SELECTED_EIGHT_COMPONENTS_WORKING_RESEARCH_BASELINE_V1.md)
- [Eight-component physical/mathematical research dossier](thermal_sos_functional_architecture/EIGHT_COMPONENT_PHYSICS_AND_DIRECTIONAL_INTERFACE_RESEARCH_DOSSIER_V1.md)

**Implementation:** Cite this file in subsequent new physics/mathematics/hypothesis-testing work. Preserve all frozen authorities and existing eight-component names. Do not assume any installation, numerical threshold, selected material parameter, installed control, causal mechanism or confirmed scientific result without evidence.
