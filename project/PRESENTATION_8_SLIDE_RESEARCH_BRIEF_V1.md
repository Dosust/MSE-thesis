# 8-Slide MSE Research Presentation Brief — V1

**Status:** ACTIVE WORKING PRESENTATION BRIEF  
**Effective date:** 2026-10-05  
**Repository:** `Dossiya-SE/MSE-thesis`  
**Official thesis title:** **Physics-Based Mathematical Engineering of Power–Transportation Interdependencies for Resilience**

## Canonical thermal-interdependency focus — FROZEN 2026-10-07

Authorities:
- `project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md`
- `project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md`

> **The thesis focuses only on thermal interdependencies between the Power System and Electrified Transportation System and on their consequences through state and time.**

Presentation rules:
- every slide must remain inside the thermal-interdependency scope;
- state and time are the primary analytical dimensions;
- do not present generic Power–Transportation coupling as the thesis object;
- do not present non-thermal interdependencies as active mechanisms;
- non-thermal quantities may appear only as boundary conditions, coupling variables, controls, or constraints required for a thermal mechanism;
- preserve the chain: extreme heat → thermal state → thermal capability/constraint → thermal interdependency → state-time consequence → electricity/mobility service consequence → resilience interpretation; sustainability then has two pathways: direct consequence and engineering-response consequence;
- use **qualify** consistently;
- name the physical object or variable class directly in objectives and scope statements.

## Canonical resilience definition — FROZEN 2026-10-07

Authority: `project/CANONICAL_RESILIENCE_DEFINITION_V1.md`

> **Resilience is the ability of the coupled Power and Electrified Transportation systems to maintain or recover required electricity and mobility services as thermal states and thermal interdependencies evolve over time.**

Presentation rules:
- resilience is evaluated at the **service level through time**;
- component survival is not resilience;
- preserve **Thermal State ≠ Capability ≠ Service ≠ Resilience**;
- use service requirements (Q_P(t) \ge Q_P^{req}(t)) and (Q_T(t) \ge Q_T^{req}(t)) when operationalized;
- a service deficit occurs when (Q_k(t) < Q_k^{req}(t));
- the central question is: **Can required service be maintained, and if not, how quickly and effectively can it be recovered?**
- minimum service level, service deficit, disruption duration, and recovery time may characterize the service trajectory;
- Improve, Adapt, and Restore are engineering response classes, not the definition of resilience.

## Canonical two-pathway sustainability assessment — FROZEN 2026-10-07

Authority: `project/CANONICAL_SUSTAINABILITY_TWO_PATHWAY_ASSESSMENT_V1.md`

> **Sustainability in this thesis is assessed through two pathways: (1) the direct environmental, economic, and social consequences of thermal interdependencies on electricity and mobility services, and (2) the environmental, economic, and social consequences of engineering responses used to improve, adapt, or restore those services. Both pathways are evaluated within a declared system boundary and time horizon.**

Presentation rule: show **one sustainability framework with two clearly labeled pathways**.

```text
Pathway 1 — Direct consequence
Thermal Interdependency
→ Electricity + Mobility Service Consequence
→ Environmental / Economic / Social

Pathway 2 — Engineering-response consequence
Improve / Adapt / Restore
→ Changed State / Capability / Service
→ Environmental / Economic / Social
```

Dimension content:

```text
Environmental → energy use; energy efficiency; electrical/conversion losses; GHG emissions; material/resource burden
Economic → operating; maintenance/replacement; intervention; service-disruption cost
Social → access; continuity; affordability; equity; safety
```

Use only measurable, scope-relevant indicators.

SDG rule:

```text
Measured Sustainability Indicator
→ Sustainability Dimension
→ Relevant SDG Target / Indicator
```

Do not map a broad dimension directly to an SDG number. Exact SDG targets remain open until indicators are operationalized.

## Canonical effectiveness / energy-efficiency placement — FROZEN 2026-10-07

Authority: `project/CANONICAL_EFFECTIVENESS_ENERGY_EFFICIENCY_PLACEMENT_V1.md`

```text
Effectiveness → Resilience / Engineering-Response Assessment
Energy Efficiency → Environmental Sustainability
```

Presentation rules:
- effectiveness asks whether Improve, Adapt, or Restore achieves the intended service/resilience result;
- energy efficiency belongs under environmental sustainability;
- never merge effectiveness with energy efficiency;
- never imply that an effective resilience response is automatically sustainable.

```text
Effectiveness ≠ Energy Efficiency ≠ Sustainability
Effective Resilience Response ≠ Sustainable Response
```

## Canonical Electrified Transportation scope — FROZEN 2026-10-07

Authority: `project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md`

> **In this thesis, the electrified transportation system comprises the electrically propelled road vehicle, its rechargeable energy-storage system, electric propulsion and auxiliary electrical systems, the vehicle power-supply circuit, electric-vehicle supply equipment, the physical charging connection, and the communication and control functions required for electrical power transfer, including bidirectional transfer where supported (ISO 6469; ISO 5474; ISO 15118; IEC 61851; IEC 62196).**

Presentation rules:
- call the system **Electrified Transportation System**;
- do not use “standards-defined” as part of its name;
- keep the external Power System distinct;
- treat EVSE, the charging connection, and communication/control as part of the Electrified Transportation System scope;
- treat battery-electric road transport, bus/fleet, public fast charging, or depot charging as bounded application subsets;
- do not imply that every listed subsystem must be modeled at identical fidelity;
- keep mobility service separate from the technical system.

## 1. Purpose

This file is the persistent working source for the current **8-slide Master of Science in Engineering research presentation**.

It is designed for both humans and AI systems. It records:
- what is already decided;
- what remains open;
- which evidence is admissible for each slide;
- how new findings are converted into presentation content;
- which statements must not be repeated or silently redefined.

This file does **not** silently replace canonical thesis authorities. Where the current presentation workstream is narrower than older canonical files, the difference is recorded explicitly as a working amendment requirement rather than hidden.

## 2. Governing research method

The presentation uses the repository-wide **Canonical Research Reasoning Protocol**, **EGMIV Method**, and **Research Decision and Freeze Protocol V1** (`project/RESEARCH_DECISION_AND_FREEZE_PROTOCOL_V1.md`).

Primary reasoning chain:

```text
LEARN
→ VERIFY
→ FORMULATE
→ DERIVE
→ TEST
→ VALIDATE
→ SYNTHESIZE
→ ADVANCE
```

Interdependency qualification rule:

```text
No interdependency without:
direction + physical mechanism + mapping + type + evidence.
```

For presentation content, apply this additional capture sequence:

```text
STANDARDIZE
→ ESTABLISH EVIDENCE
→ QUALIFY MECHANISM
→ BOUND SCOPE
→ MAP TO SLIDE
→ ASSIGN EPISTEMIC STATUS
→ SAVE
→ FREEZE WHEN JUSTIFIED
```

A presentation claim is admitted only if it is:
1. relevant to the research question;
2. relevant to service/function;
3. physically interpretable;
4. evidence-supported or explicitly thesis-defined;
5. compatible with available data/modeling;
6. tractable for an MSE thesis;
7. useful to one of the eight presentation slides.

## 3. Anti-repetition / freeze rule

Once a decision is marked **FROZEN**, later work builds from it rather than reopening it.

A frozen item is reopened only for:
- new contradictory evidence;
- infeasibility;
- a change required by the chair/committee;
- a formal scope amendment.

Do not reopen a decision merely because a different wording appears attractive.

## 4. Current decision ledger

| Object | Current decision | Status | Notes |
|---|---|---|---|
| Thesis title | Physics-Based Mathematical Engineering of Power–Transportation Interdependencies for Resilience | **FROZEN** | Canonical title authority |
| Core infrastructure systems | Power + Transportation | **FROZEN** | Preserve thesis meaning |
| Hazard for current presentation workstream | Extreme heat | **FROZEN — CURRENT** | Controlled by current thermal-interdependency scope authority |
| Interdependency focus | Thermal interdependencies between Power and Electrified Transportation only | **FROZEN — CANONICAL** | Non-thermal relations enter only when required to represent a thermal mechanism |
| Performance lens | Functioning + serviceability + reliability | **WORKING-FROZEN** | Used to characterize service performance before/through resilience assessment |
| Primary outcome | Electricity and mobility service trajectories interpreted for resilience | **FROZEN INTERPRETATION / METRICS OPEN** | Resilience is service-level and state-time; exact metrics remain open |
| Transport mode | Road transport → battery-electric road transportation | **WORKING-FROZEN** | Chosen through the five canonical scope gates; see `project/ROAD_VS_RAIL_SCOPE_GATE_DECISION_V1.md` |
| Electrical dependency architecture | Battery-mediated electric mobility through grid-connected EV charging | **WORKING-FROZEN** | Exact charging context remains open |
| V2G | Not active by default | **OPEN/EXCLUDED UNLESS JUSTIFIED** | Do not equate interdependency with reverse electrical flow |
| Energy efficiency | Secondary performance/sustainability criterion | **WORKING-FROZEN** | Evaluate after service requirement is defined |
| “Real-time” control | Terminology not frozen | **OPEN** | Use only if live/online estimation-control requirements are actually modeled |
| Exact resilience capacity label | Not frozen | **OPEN** | Do not prematurely label the thesis as only adaptive/absorptive/restorative |
| Engineering action sequence | Improvement/enhancement → adaptation → restoration | **WORKING-FROZEN** | Improvement is the engineering starting objective; adaptation and restoration are subsequent response phases |
| Sustainability framework | Direct consequence + engineering-response consequence | **FROZEN — CANONICAL TWO-PATHWAY** | Both use environmental, economic, and social dimensions |
| Effectiveness placement | Resilience / engineering-response assessment | **FROZEN** | Did the response maintain or recover required service? |
| Energy-efficiency placement | Environmental sustainability | **FROZEN** | Useful service relative to energy input; exact functional basis remains open |
| SDG linkage | Measured indicator → dimension → relevant SDG target/indicator | **FROZEN RULE** | Exact targets remain open until measurement |
| Comparator architecture | Needs reconciliation with canonical M0/M1/M2 repository state and current narrower M0/M1 discussion | **OPEN** | No silent replacement |

## 5. Scientific distinctions that must remain visible

```text
system ≠ graph ≠ interface ≠ service
state ≠ functionality ≠ serviceability ≠ reliability ≠ resilience
interdependency ≠ bidirectional electrical power flow
electric transport energy ≠ generic transport energy
reliability ≠ resilience
verification ≠ validation
effectiveness ≠ efficiency ≠ sustainability
proposed ≠ established ≠ tested ≠ validated
```

## 6. Current performance logic

The current service-centered reasoning is:

```text
Extreme-heat forcing
→ physical state
→ functional capability
→ serviceability
→ service trajectory
→ reliability / resilience assessment
→ operational intervention
```

Interpretation:
- **State** explains physical condition.
- **Functioning** asks whether intended function can still be performed.
- **Serviceability** asks whether delivered electricity/mobility service remains acceptable.
- **Reliability** asks whether acceptable performance is sustained consistently over the declared operating domain.
- **Resilience** is the ability to maintain or recover required electricity and mobility services as thermal states and thermal interdependencies evolve over time.
- **Energy efficiency** is evaluated only after the service delivered is defined.
- **Operational control** is the engineering response layer, not the resilience outcome itself.

### Engineering action sequence

The presentation should show the thesis engineering purpose in this order:

```text
IMPROVE
→ ADAPT
→ RESTORE
```

- **Improve:** use physics-based mathematical engineering to identify and test changes that improve functioning, serviceability, reliability, or service margins relative to a baseline.
- **Adapt:** use time-varying state information to adjust operation during extreme heat.
- **Restore:** recover degraded electricity and mobility services toward their declared acceptable/reference levels.

This is an **engineering action sequence**, not a claim that "improvement" is a standard resilience category.

The scientific chain remains:

```text
Extreme heat
→ physical state
→ functionality
→ serviceability
→ reliability
→ engineering action
→ resilience consequence
```

### Resilience interpretation

The presentation must not define resilience as Improve → Adapt → Restore.

Use the canonical definition:

> **Resilience is the ability of the coupled Power and Electrified Transportation systems to maintain or recover required electricity and mobility services as thermal states and thermal interdependencies evolve over time.**

The engineering response sequence remains:

```text
Improve → Adapt → Restore
```

but it is evaluated by how it changes the service trajectory, service deficit, disruption duration, recovery time, or other justified resilience descriptors.

## 7. Current 8-slide scientific backbone

### Slide 1 — Engineering problem and motivation
**Question answered:** Why does the problem matter?

Target message:
> Electrified transportation creates a direct dependency between transportation service and electrical supply. Extreme heat can alter the physical states that govern electrical capability and transport energy requirements, potentially changing delivered service.

Required content:
- exact transport-electrification mechanism after mode selection;
- extreme-heat forcing as a time-dependent event;
- one clear service consequence;
- no research-gap claim yet.

### Slide 2 — Established knowledge and bounded unresolved handoff
**Question answered:** What is already established, and what specifically remains to be tested?

Structure:
```text
Established Power–Transportation models
+
Established thermal/electrification physics
→
bounded unresolved handoff
```

Candidate handoff:
```text
heat-dependent physical state
→ functional capability
→ serviceability
→ electricity / mobility service consequence
```

Do not use “nobody has studied this” without a reproducible novelty audit.

### Slide 3 — Scope and system boundary
**Question answered:** Exactly what is inside and outside the thesis?

Must show:
- Power system;
- defined electrified transportation mode;
- defined electricity-dependency mechanism;
- extreme heat;
- functioning, serviceability, reliability;
- explicit exclusions.

Do not lock road transport, rail, charging-only, V2G, transformer physics or real-time control until their scope gates pass.

### Slide 4 — Physical mechanism and state evolution
**Question answered:** How does the hazard physically propagate?

Core logic:
```text
T_amb(t)
→ x_P(t), x_T(t)
→ capability / requirement
→ function
→ service
```

Every arrow must have:
- a physical mechanism;
- evidence or thesis derivation;
- units/semantics;
- assumptions;
- validity domain.

### Slide 5 — Functioning, serviceability and reliability
**Question answered:** What performance is actually being evaluated before resilience is calculated?

Required distinctions:
- functioning = ability to perform intended function;
- serviceability = acceptable level of delivered service;
- reliability = consistency/probability of acceptable function/service over the declared domain.

Primary service variables must be defined and operationalized before final slide wording is frozen.

### Slide 6 — Mathematical model and controlled comparison
**Question answered:** What mathematical representation tests the research question?

Minimum content:
- state vector(s);
- forcing/input;
- physical constraints;
- service outputs;
- comparator(s);
- held-constant conditions.

Comparator labels remain **OPEN** until current narrowed work is reconciled with canonical repository M0/M1/M2 definitions.

### Slide 7 — Experiment, intervention and VVUQ
**Question answered:** How will the research distinguish a real engineering effect from model artefact?

Required:
- matched scenarios;
- one bounded intervention if activated;
- verification;
- validation;
- uncertainty;
- sensitivity;
- falsification/non-support condition;
- validity boundary.

### Slide 8 — Contribution and engineering decision value
**Question answered:** What useful information will the thesis produce?

Contribution must be expressed conditionally:
- when does representing the relevant physical states change service/resilience conclusions?
- when is a simpler representation adequate?
- when does the intervention change engineering action?
- what remains outside the validation domain?

Do not state expected findings as achieved results.

## 8. Evidence candidate already admitted for presentation development

### E-HEAT-001 — Extreme heat must be represented through time
**Epistemic status:** [E] external evidence  
**Candidate slides:** 1 and 4  
**Source:** Ragone, F., Wouters, J., & Bouchet, F. (2017). *Computation of extreme heat waves in climate models using a large deviation algorithm*. arXiv:1709.03757.

Supported use:
- heat waves can be treated as rare and persistent temperature anomalies;
- duration matters;
- a time-averaged temperature observable is used to characterize heat-wave events;
- return-time estimation is a separate probabilistic problem.

Presentation consequence:
```text
Do not represent the hazard only as one static temperature.
Use a declared T_amb(t) event trajectory or time-resolved temperature forcing.
```

Boundary:
- this source supports **hazard representation**;
- it does not establish a Power–Transportation interdependency;
- the GKLT rare-event algorithm is not automatically part of the thesis method.

### E-POWERHEAT-001 — Dynamic power-system thermal capability under heatwaves
**Epistemic status:** [E] external evidence  
**Candidate slides:** 1, 2, 4, 5, 6, 7, 8  
**Evidence note:** `evidence/E_POWERHEAT_001_GUPTA_VERMA_2026.md`

Supported presentation use:
- extreme heat can change power-system component capability through thermal mechanisms;
- transmission ampacity and generator capacity can be represented as temperature/weather dependent;
- capability loss can propagate to electrical service deficit;
- EENS/LOLE/SOP illustrate service/reliability-oriented outcome measures;
- static versus time-varying physical-capacity representation is a legitimate controlled-model comparison;
- sensitivity analysis is necessary when thermal assumptions can alter conclusions.

Boundary:
- power-side evidence only;
- does not select the Transportation mode;
- does not establish P–T coupling laws;
- study-specific thresholds and IEEE-57 numerical results are not transferable thesis parameters.

## 9. Open research decisions that must be resolved before the 8 slides are frozen

1. Which electrified transportation mode produces the strongest combination of:
   - electricity dependence;
   - service relevance;
   - observable states;
   - data availability;
   - tractable modeling;
   - defensible MSE scope?

2. Which electrical-dependency architecture is adopted:
   - continuous electric traction;
   - battery-mediated electric mobility;
   - another evidence-qualified architecture?

3. What exact service variables operationalize:
   - electricity service;
   - mobility service;
   - serviceability threshold;
   - reliability?

4. What exact heat-event trajectory and validity domain are used?

5. What comparator architecture is scientifically and governance-consistent?

6. What intervention, if any, is narrow enough to test without changing the thesis into a control-design thesis?

## 10. Content admission record for future findings

Every strong new item should be saved in this format:

```text
ID:
Date:
Slide candidate:
Statement:
Epistemic status: [E]/[D]/[H]/[P]/[A]/[U]/[R]
Source / authority:
Exact support:
Physical mechanism:
Why it matters to service:
Assumptions:
Validity boundary:
Decision: ADMIT / HOLD / REJECT
Freeze status: OPEN / WORKING-FROZEN / FROZEN
Reopen condition:
```

## 11. Rule for any AI or human continuing the work

Before drafting or revising the 8-slide presentation:

1. read the canonical thesis title;
2. read the canonical research reasoning protocol;
3. read EGMIV;
4. read this presentation brief;
5. inspect the current decision ledger;
6. do not reopen frozen items;
7. do not promote an OPEN item to established fact;
8. add strong new evidence to the content admission record;
9. preserve source-to-claim traceability;
10. make every slide answer one scientific question.

## 12. Presentation quality criterion

The presentation is ready only when the audience can answer:

```text
1. What exact engineering problem is studied?
2. What is already established?
3. What is the bounded unresolved handoff?
4. What physical system and dependency are inside the scope?
5. What physical mechanism is modeled?
6. What performance/service quantities are measured?
7. What controlled experiment tests the claim?
8. What engineering decision becomes better informed?
```

If any answer is unclear, the slide set is not yet frozen.


## Evidence update - E-POWERHEAT-002

Source note: `evidence/E_POWERHEAT_002_MARTINEZ_2026.md`

Use for Slides 1, 2, 4, 5, 6, 7 and 8:
- extreme heat can increase electrical demand while reducing branch capability;
- time-resolved state and capability updates are relevant;
- ENS is a service-deficit measure;
- reliability and resilience remain distinct;
- time-resolved quasi-static PF/OPF should not be described as full dynamic operation.

Boundary: power-side evidence only. It does not decide transport mode or coupled P-T equations.


## Evidence update - E-THERMALSTATE-001 and E-THERMALMODEL-001

Evidence notes:
- `evidence/E_THERMALSTATE_001_DANILOV_ROMANENKO_2025.md`
- `evidence/E_THERMALMODEL_001_ZOCHOLL_GUZMAN_2000.md`

Presentation use:
- physics-based mathematical engineering can improve state estimation/monitoring by coupling electrical and thermal equations;
- conductor temperature and thermal history can materially alter currents, losses, thermal margins and protection decisions;
- "improvement first" should mean improvement relative to a declared baseline in model adequacy, functioning, serviceability, reliability, or operating decision quality;
- added mathematics is justified only when the added physical state changes an engineering conclusion.

Boundary:
- these sources support power-side physics and model adequacy;
- they do not establish transport-side mechanisms, P-T coupling, adaptation, or restoration.


## Presentation engineering-response cycle

Use the supporting engineering-response sequence:

```text
IMPROVE → ADAPT → RESTORE → LEARN → IMPROVE
```

Presentation meaning:
- **Improve:** strengthen future service capability relative to a baseline.
- **Adapt:** modify operation as physical states evolve.
- **Restore:** return degraded electricity and mobility service to an acceptable/reference level.
- **Learn:** use evidence from disturbance and recovery to improve the next design/operating decision.

Do not present this sequence as the definition of resilience. The canonical definition is the ability of the coupled Power and Electrified Transportation systems to maintain or recover required electricity and mobility services as thermal states and thermal interdependencies evolve over time. Improve, Adapt, Restore, and Learn describe engineering response and learning.

For slide logic, use:
```text
physical state
→ functionality
→ serviceability
→ service trajectory
```
with reliability evaluated over the declared service domain and resilience evaluated by whether required service is maintained or recovered through the evolving disturbance and recovery trajectory. Improve–Adapt–Restore effectiveness is assessed by how those responses change that service trajectory.


## Evidence update - E-CONTEXT-HEAT-001

Source note: `evidence/E_CONTEXT_HEAT_001_MITIGA_2024.md`

Use only as contextual/motivational evidence:
- extreme heat can threaten infrastructure, business continuity, workers and assets;
- proactive vulnerability assessment and adaptation are decision-relevant;
- useful mainly for Slide 1 motivation and Slide 8 engineering value.

Do **not** use this industry article for mechanism equations, model parameters, validation, transport physics, P-T coupling, or novelty claims.


## Evidence update - E-TRANSPORT-IPT-001

Source note: `evidence/E_TRANSPORT_IPT_001_PEARSON_ET_AL_2026.md`

Use for Slides 2, 3, 4, 6, 7, and 8:
- IPT is a specific road-transport electrification technology, not a transport mode;
- the physical charging path is grid supply → power electronics → primary pad → magnetic coupling → secondary pad → battery;
- a coupled IPT interface requires electro-magnetic, solid-thermal, and fluid-thermal physics;
- coupled primary–secondary operation can produce materially different thermal states from a single-pad simplification;
- experimental validation provides a strong precedent for controlled comparison of alternative physical representations;
- this source strongly supports the thesis **IMPROVE** phase: better physical representation can identify safer limits and thermal-management/design opportunities.

Boundary:
- the experiments begin at 20 °C ambient and are not an extreme-heat study;
- this source does not establish road vs rail, generic EVSE physics, Transportation → Power feedback, mobility-service metrics, adaptation, or restoration.


## Evidence update - E-RESILIENCE-001

Source note: `evidence/E_RESILIENCE_001_FATURECHI_MILLER_HOOKS_2014.md`

Use for Slides 2, 5, 6, 7, and 8:
- established resilience literature distinguishes preparedness/robustness, flexibility/adaptability, recovery capability, and resilience;
- pre-event actions can improve resistance, capacity, readiness, and resource availability;
- postevent adaptive actions support flexibility;
- recovery actions restore lost system performance;
- time-dependent disruption profiles provide a basis for minimum performance, recovery time, and area-under-curve service/resilience metrics;
- a two-stage stochastic decision structure provides a precedent for pre-event and postevent intervention optimization under uncertainty.

Presentation mapping:
```text
THESIS: IMPROVE
≈ preparedness / robustness-enhancing pre-event action

THESIS: ADAPT
≈ flexibility / adaptive response

THESIS: RESTORE
≈ recovery capability / restoration
```

Do not claim that Improve → Adapt → Restore is the universal literature definition of resilience. Present it as the thesis operational cycle grounded in established resilience concepts.


## Evidence update - E-DEPENDENCY-TIME-001

Source note: `evidence/E_DEPENDENCY_TIME_001_STERGIOPOULOS_ET_AL_2016.md`

Use for Slides 1, 2, 3, 4, 7, and 8:
- dependency is directional reliance on an input, interaction, or requirement needed for proper function;
- co-location/geographical exposure is not itself functional dependency;
- cascading, escalating, and common-cause failures should be distinguished;
- dependency consequences can evolve through time rather than appear instantaneously;
- reaction time and mitigation-control placement can matter;
- proactive dependency analysis can identify where improvement should be targeted.

Critical boundary:
- this is a graph/risk/fuzzy time-based framework, not a physics-based dynamical model;
- use it to qualify dependency structure and timing, not to supply heat-transfer, power-flow, charging, or transport equations.


## Evidence update - E-INTERDEP-002

Source note: `evidence/E_INTERDEP_002_GANGULY_MUKHERJEE_2022.md`

Use for Slides 2, 3, 4, 5, 7, and 8:
- existing hybrid frameworks already separate intra-infrastructure and inter-infrastructure failure propagation;
- interdependency should be tied to service/state reliance before spatial proximity is used to modulate edge strength;
- time-dependent vulnerability can be modeled probabilistically under incomplete information;
- redundancy can reduce vulnerability in modeled systems and is therefore a candidate improvement lever;
- information sharing and coordination among infrastructure managers can reduce underestimation of interdependent risk;
- vulnerability probability is not the same as serviceability or resilience.

Critical boundary:
- this is an arXiv preprint and should not be treated as peer-reviewed evidence unless publication status is independently verified;
- the method is hybrid simulation/Bayesian, not physics-based;
- synthetic/hypothetical data, independence assumptions, and heuristic interdependency weights are not transferable thesis parameters.


## Evidence update — E-CPTN-TEMP-001 / E-CPTN-TEMP-002

Use mainly for Slides 2, 4, 6, and 7.

### Li & Chang (2024)

Strong open-access comparator showing:

```text
ambient temperature
→ EV auxiliary / energy consumption
→ charging demand
→ station load
→ distribution-network consequence
```

It also uses controlled temperature/speed cases and dynamic charging pricing.

**Presentation consequence:** never imply that temperature-aware EV charging-load modeling is absent.

### Ji et al. (2025)

Strong Applied Energy comparator showing temperature-aware FCS selection/routing inside a tri-level EV–FCS–PDN optimization architecture.

**Presentation consequence:** never imply that temperature-aware CPTN routing/optimization is absent.

### Slide 2 wording direction

Use:

> Temperature-aware coupled road-EV/power models already exist. The unresolved thesis question is whether the relevant heat-dependent physical component states materially change electricity and mobility service trajectories and the engineering actions used to improve, adapt, and restore service.

Keep this statement as a **candidate positioning statement** until the closest literature review is complete.


## Evidence update — E-CPTN-RESILIENCE-003

**Ma et al. (2026), Applied Energy 420, 128158**

Use mainly for Slides 2, 3, 6, 7, and 8.

The paper already provides:
- bilevel resilient pricing-driven CPTN coordination;
- PDN restoration;
- price-aware dynamic traffic and energy assignment;
- EV charging/discharging as decision variables;
- spatio-temporal V2G flexibility;
- restoration trajectories;
- controlled comparison of baseline vs two nonlinear-reformulation methods.

Important thesis boundary:

```text
dynamic CPTN resilience / restoration already exists
```

but the paper does not model extreme-heat forcing or heat-dependent physical component states.

Presentation consequence:

> Do not present restoration, V2G-supported resilience, dynamic traffic-energy coupling, or bilevel coordination as the thesis novelty. Use this paper as the resilience/restoration benchmark against which the heat-physics question must be differentiated.


## Scope update — Road vs Rail gate decision

Authority: `project/ROAD_VS_RAIL_SCOPE_GATE_DECISION_V1.md`

The active presentation workstream now uses:

```text
Road transport
→ battery-electric road transportation
→ grid-connected EV charging
```

Reason for selection:

```text
direct electrification coupling
+ measurable heat-dependent charger states
+ accessible data
+ Master's tractability
+ remaining physics-to-service handoff
```

Do **not** say road was chosen because it has stronger direct electricity dependence than rail. Electric rail has the stronger immediate traction dependence.

Still OPEN:
- public DC fast charging vs fleet/depot charging;
- exact charger thermal state;
- exact service metrics;
- exact intervention.
