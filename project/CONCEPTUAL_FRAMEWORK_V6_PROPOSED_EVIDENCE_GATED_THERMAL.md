# Proposed V6 — Evidence-Gated Thermal Interdependency Framework

**Date:** 2026-10-10  
**Status:** PROPOSED V6 / REVIEW REQUIRED / NOT CANONICAL / NOT PHYSICALLY VALIDATED.  
**Assessment inherited from user review:** 84/100 for the previous provisional visual; NOT a score for this newly revised proposal.  
**Official title (unchanged):** Physics-Based Mathematical Engineering of Power–Electrified Transportation Interdependencies for Resilience.  
**Purpose:** Resolve the six stated shortcomings in the previous proposed schematic without changing frozen thesis scope, objectives, physical model status, or canonical framework authorities.

**Authority and precedence:** 
- [Current thesis authority index](CURRENT_THESIS_AUTHORITY_INDEX_V1.md).
- [Current canonical conceptual framework V5](CONCEPTUAL_FRAMEWORK_SPEC_V5_THERMAL_SUSTAINABILITY.md).
- [Current canonical mathematical framework V3](MATHEMATICAL_FRAMEWORK_SPEC_V3_THERMAL_SUSTAINABILITY.md).
- [Frozen research objectives SO1–SO3](CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md).
- [Evidence and non-invention standard](CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md).
- [Physics-adapted causal qualification method](CONCEPTUAL_FRAMEWORK_CAUSAL_QUALIFICATION_APPLICATION_V1.md).
- [Component-function-interface architecture](thermal_sos_functional_architecture/WORKING_SOS_COMPONENT_FUNCTION_INTERFACE_MATRIX_V1.md).
- [29-class candidate thermal-limit inventory](thermal_sos_functional_architecture/EQUIPMENT_SPECIFIC_THERMAL_LIMIT_CANDIDATE_INVENTORY_V1.md).
- [Module 01 model-admission ledger](module_01_transformer_thermal_state_physics/MODULE_01_MODEL_ADMISSION_LEDGER_V1.md).
- [Two-pathway sustainability authority](CANONICAL_SUSTAINABILITY_TWO_PATHWAY_ASSESSMENT_V1.md).
- [Citation and attribution standard](../thesis/00_governance/THESIS_CITATION_AND_REFERENCE_STANDARD_V1.md).

The proposal must NOT supersede V5, V3, the frozen General Objective/SO1–SO3, M0/M1/M2 comparator meanings, complete system boundaries, or equipment/model-admission ledgers. Approval, case evidence, source audits, visual rendering and numerical tests remain separate.

## 1. Single scientific thesis statement

Study whether and how equipment- and rule-qualified thermal states under extreme heat change permissible electrical and charging capabilities across a specified Power (P)–Electrified Transportation (T_e) interface, and measure their attributable timing and electricity/mobility service consequences. Evaluate resilience from required service trajectories, with optional engineering responses; evaluate sustainability through two separate, indicator-based pathways.

The full T_e includes electrically propelled road vehicles, RESS, electric propulsion/auxiliaries, vehicle power-supply circuits, EVSE, physical connections and necessary power-transfer communication/control (bidirectional only where supported). A transformer–DC EVSE–fleet demonstrator is a bounded application subset, not the full system definition.

## 2. Three regions; minimal diagram grammar

### Figure V6A: physical system and external forcing — conceptual, not an adopted equipment model

~~~mermaid
flowchart TB
    H["External extreme-heat forcing H(x,t)"]
    subgraph PH["REGION I — PHYSICAL SYSTEMS"]
      direction LR
      P["Power System P | transformer and feeder"]
      AC["AC physical port | V, I, P_AC, Q_AC"]
      T["Electrified Transportation System T_e | EVSE, connection, vehicle/RESS"]
      P -->|"Ordinary grid-to-EVSE electrical supply"| AC
      AC -->|"Electrical power accepted by EVSE"| T
    end
    H -->|"Shared external exposure"| P
    H -->|"Shared external exposure"| T
    P --> CP["P-side allowable loading C_P | device/policy rule OPEN"]
    T --> CE["EVSE charging capability C_E | selected-device law OPEN"]
    classDef phys fill:#FFFFFF,stroke:#087D43,color:#111827,stroke-width:2px
    classDef bound fill:#FFFFFF,stroke:#334155,color:#111827,stroke-width:1.6px
    classDef candidate fill:#FFFFFF,stroke:#2563EB,color:#111827,stroke-width:1.7px
    class P,T phys
    class H,AC bound
    class CP,CE candidate
~~~

The single ordinary electrical supply path is not proof of either thermal causal direction. EVSE-driven loading influences the Power System through an electrical *demand/load response*, not reverse electricity flow; drawing a reverse power arrow requires documented V2G operation. External heat is common forcing and is not an interface.

### Figure V6B: explicitly distinct conditional thermal-interdependency mechanisms

~~~mermaid
flowchart TB
    PT["I3 — P to T_e [OPEN]<br/>Transformer thermal state → verified loading/protection policy → permitted grid-side AC supply → EVSE/vehicle energy"]
    TP["I2 — T_e to P [OPEN FOR SELECTED CASE]<br/>EVSE heat/thermal control → documented actual AC demand response → transformer current/loss → thermal state"]
    PT -->|"Subject to independent mechanism/data admission"| G["Independent direction-by-direction evidence gate"]
    TP -->|"Subject to independent mechanism/data admission"| G
    classDef mech fill:#FFFFFF,stroke:#2563EB,color:#111827,stroke-width:1.8px
    class PT,TP,G mech
~~~

This is a **relationship qualification flow**, not a feedback-free depiction of continuous physics. I2 and I3 are not accepted merely because a manufacturer law exists for another device. The P→T_e mechanism specifically requires a state-to-implemented-constraint/action link, and T_e→P requires the thermal-to-AC-input response. At the actual power port, AC-input active/reactive power must remain distinct from EVSE DC delivered power and battery terminal power.

**Arrow contract:** Solid arrows in Figure V6A show ordinary physical power transfer or external heat exposure (labels state which), not a thermal-causal inference. Solid arrows in V6B point from candidate claims to the research admission gate (workflow, not physical flow). Dashed arrows, if added in publication rendering, mean *conditional research hypotheses* ONLY when explicitly labelled; do not reuse the same dashed style for controls. Every arrow type must have a caption/legend. Avoid unlabeled generic two-headed causal arrows.

## 3. Model core (T1 proposal, not an admitted constitutive model)

With x_P and x_Te containing only case-admitted dynamic states; H ambient/solar and other external forcing; z algebraic port/operating variables; u operative controls; theta parameter values:

\[
\begin{aligned}
\dot x_P &= f_P(x_P,z,H_P,u_P;\theta_P),\\
\dot x_{T_e} &= f_{T_e}(x_{T_e},z,H_{T_e},u_{T_e};\theta_{T_e}),\\
0&=g(x_P,x_{T_e},z,H,u;\theta),\\
C_P&=\mathcal C_P(x_P^{th},H_P,\mathrm{policy,cooling,history};\theta_{C_P}),\\
C_E&=\mathcal C_E(x_E^{th},H_{T_e},\mathrm{device\ control,history};\theta_{C_E}),\\
(Q_P,Q_{T_e})&=h(x_P,x_{T_e},z,C_P,C_E,u;\theta_Q).
\end{aligned}
\]

**All equipment-specific C_P and C_E functions remain OPEN for the eventual selected case.** If a documented charger limit depends only on ambient exposure or elapsed operation, do not invent a rectifier dynamic state. If case-specific physics demonstrates independent interface memory, an additional dynamic state may be admitted; otherwise 0=g(...) is the default interface form. Transformer top-oil and hotspot are *candidate* active states, not frozen; SOC is an *energy* state, not thermal state.

A representation of the EVSE energy port requires consistent control-volume accounting:

\[
P_{\mathrm{AC,in}}=P_{\mathrm{DC,out}}+P_{\mathrm{loss,EVSE}}
\]

when losses/auxiliaries and measurement boundaries are defined consistently. Reactive power and phase/cable loading remain separate when computing transformer currents. A transformer allowable apparent loading is not identical to charger allowable real input power. A temperature observation is not a temperature *limit*, a limit is not an implemented action, and an action is not proof of service shortfall.

## 4. The four distinct timing quantities

| Quantity | Interpretation | Admission requirement |
|---|---|---|
| t_crit,i | First justified physical/capability boundary crossing or specified event | Source-backed event function, history, threshold and time sampling |
| delta_ij | Attributable source-to-receiver propagation time | Independent source/receiver events plus matched counterfactual, not mere temperature lag |
| t_service,k | First breach of an explicitly defined electricity or mobility service requirement | Q_k(t), Q_req,k(t), and observed/model-valid service quantity |
| t_recovery,k | First return to required service, with specified stability/dwell criterion where needed | Actual recovery experiment/model and declared end condition |

No event or numerical propagation delay may be inferred from an arbitrary illustrative threshold. Charging readiness at a vehicle departure deadline is a mobility-service *proxy* unless a delivered trip is actually observed.

## 5. Figure V6C: model evaluation and intervention feedback

~~~mermaid
flowchart TB
    G["Admit only qualified mechanism, parameter and data"]
    D["Constrained physical state–time model | ODE/DAE + CP/CE + AC port"]
    V["Numerical verification | balance, units, event logic, convergence"]
    M["Matched M0 / M1 / M2 comparisons | M2 only if ready"]
    W["Independent validation + uncertainty / sensitivity assessment"]
    Q["Conditional outputs | critical events and electricity/mobility service trajectories"]
    R["Service resilience assessment | maintain / recover"]
    A["Optional engineering response | Improve / Adapt / Restore"]
    RC["Matched response versus no-response service comparison"]
    S1["Sustainability pathway 1 | direct thermal/service consequence"]
    S2["Sustainability pathway 2 | response consequence"]
    S["Distinct measured environmental / economic / social indicators"]
    SDG["Relevant SDG target and official indicator ONLY if measure matches"]
    G --> D --> V --> M --> W --> Q --> R
    R --> A
    A -->|"Change admissible controls / physical conditions; rerun"| D
    Q --> S1 --> S
    Q --> RC
    A --> RC
    RC --> S2 --> S
    S --> SDG
    classDef mat fill:#FFFFFF,stroke:#2563EB,color:#111827,stroke-width:1.8px
    classDef eva fill:#FFFFFF,stroke:#334155,color:#111827,stroke-width:1.5px
    classDef out fill:#FFFFFF,stroke:#087D43,color:#111827,stroke-width:1.8px
    class G,D,V,M,W mat
    class Q,R,RC eva
    class A,S1,S2,S,SDG out
~~~

This evaluation diagram is a *research workflow*, not another physical system. Its long feedback path represents a new simulation experiment with a specified response and matched reference case, not a post hoc adjustment to observed outcomes.

- M0 = independent P and T_e controlled severed-link counterfactual (not a literal connected depot).
- M1 = static/algebraic qualified electrical interdependency.
- M2 = dynamic causal interdependency ONLY if its *additional* interface-specific dynamics are source- and VVUQ-qualified; intrinsic transformer/charger thermal dynamics alone do not establish M2.
- M0/M1/M2 labels are canonical historical comparator meanings; comparison is not a claim of monotone predictive improvement.
- Numerically verified ≠ independently physically validated. Without usable independent measurements, report bounded/scenario results and OPEN validation rather than a validation PASS.
- Independent validation requires observational and temporal support for the QOI actually claimed; do not transfer generic EV charging records as paired transformer/EVSE field measurements.
- If a response is absent or not admissible, baseline resilience and direct-consequence sustainability can still be evaluated without the intervention branch.

## 6. Bounded sustainability and SDG logic

- Pathway 1: qualified heat/interdependency → baseline affected electricity/mobility service → measured indicators relative to a declared reference.
- Pathway 2: eligible Improve/Adapt/Restore response → *rerun* model → changed states/capabilities/services → separately measured indicators relative to matched no-response extreme-heat case.
- Measure and retain distinct environmental, economic and social quantities with units, time horizon, boundaries and uncertainty; do NOT create an unapproved single sustainable-resilient scalar score.
- SDG mapping: *measured indicator → sustainability dimension → relevant UN target → official SDG indicator only when definition/scale/unit match*. Relevance ≠ achieved SDG impact. This is an interpretation, never a physical driver or additional thesis objective.

## 7. Six-correction acceptance crosswalk

| User's correction | Implementation in proposed V6 | Verification status |
|---|---|---|
| Distinguish P→T_e and T_e→P thermal mechanisms | Independently labeled I3/I2 in V6B; ordinary supply separated in V6A | DESIGN INCLUDED; source/case qualification OPEN |
| Separate C_P and C_E | Distinct capability nodes, laws, operating histories and checks | DESIGN INCLUDED; selected-device quantitative laws OPEN |
| Add numerical verification, validation and UQ | Explicit separate steps V and W in V6C | DESIGN INCLUDED; tests NOT RUN |
| Distinguish critical times, attributable propagation, impact onset and recovery | Four-row timing ontology | DESIGN INCLUDED; time values NOT CALCULATED |
| Interventions rerun model before response evaluation | Optional A → D feedback; RC uses rerun service trajectories | DESIGN INCLUDED; intervention experiments NOT RUN |
| Remove crossing / generic arrows and separate regions | Three smaller diagrams with distinct physical, mechanism, evaluation regions and arrow contract | STRUCTURAL PROPOSAL; final render/readability QA NOT RUN |

## 8. Publication/adoption gates — current status

**Design content:** six corrections specified; limited to documented thesis scope.  
**Exact model and states:** OPEN.  
**Qualified physical I2/I3 mechanisms:** OPEN for selected case, with P→T_e restriction especially blocking.  
**Transformer architecture (oil/dry) and matched EVSE:** OPEN.  
**Numerical verification:** NOT RUN.  
**Independent equipment-level validation:** NOT RUN.  
**Mermaid/static figure rendering and 16:9 readability:** NOT RUN.  
**External-source claim/page-clause audit:** OPEN.  
**Novelty:** OPEN.  
**Scientific adoption:** PROPOSED ONLY; no automatic promotion of V6 to V5/V3 authority.

**Minimum next scientific deliverable:** source-by-clause/device mechanism admission for P-side state→actual operating restriction and T_e-side heat→AC demand, followed by a compatible transformer–charger scenario and independently validatable experiments. Do not add model layers solely to decorate the figure.

---
*This document records a proposed design revision responding to the 84/100 user evaluation, not a completed empirical scientific advance or approved manuscript figure.*
