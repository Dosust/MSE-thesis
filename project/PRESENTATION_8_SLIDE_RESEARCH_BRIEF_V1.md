# 8-Slide MSE Research Presentation Brief — V1

**Status:** ACTIVE WORKING PRESENTATION BRIEF  
**Effective date:** 2026-10-05  
**Repository:** `Dossiya-SE/MSE-thesis`  
**Official thesis title:** **Physics-Based Mathematical Engineering of Power–Transportation Interdependencies for Resilience**

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
| Hazard for current presentation workstream | Extreme heat | **WORKING-FROZEN** | Requires synchronization with older repository authorities before thesis-wide canonical replacement |
| Interdependency focus | Electricity-based dependency created by transport electrification | **WORKING-FROZEN** | Excludes petrol, diesel, natural gas and other non-electric propulsion-energy pathways |
| Performance lens | Functioning + serviceability + reliability | **WORKING-FROZEN** | Used to characterize service performance before/through resilience assessment |
| Primary outcome | Electricity and mobility service trajectories / resilience | **WORKING-FROZEN** | Interface/component states are mechanisms, not the final outcome |
| Transport mode | Road vs rail / other electrified mode | **OPEN** | Must be selected through evidence + service relevance + tractability gates |
| Electrical dependency architecture | Continuous grid-supplied traction vs battery-mediated electric mobility | **OPEN** | Compare before freezing transport subsystem |
| V2G | Not active by default | **OPEN/EXCLUDED UNLESS JUSTIFIED** | Do not equate interdependency with reverse electrical flow |
| Energy efficiency | Secondary performance/sustainability criterion | **WORKING-FROZEN** | Evaluate after service requirement is defined |
| “Real-time” control | Terminology not frozen | **OPEN** | Use only if live/online estimation-control requirements are actually modeled |
| Exact resilience capacity label | Not frozen | **OPEN** | Do not prematurely label the thesis as only adaptive/absorptive/restorative |
| Engineering action sequence | Improvement/enhancement → adaptation → restoration | **WORKING-FROZEN** | Improvement is the engineering starting objective; adaptation and restoration are subsequent response phases |
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
- **Resilience** evaluates disturbance-driven degradation, persistence/adaptation and recovery of service through time.
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

### Thesis resilience decomposition

For presentation purposes, the thesis operationalizes resilience as:

```text
IMPROVE
→ ADAPT
→ RESTORE
```

- **Improve:** identify and test physics-based changes that improve functioning, serviceability, reliability, or service margin relative to a baseline.
- **Adapt:** adjust operation as extreme heat and system states evolve.
- **Restore:** recover degraded electricity and mobility service toward acceptable/reference levels.

This is the thesis engineering decomposition, not a universal standard definition.

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
- selected electrified transportation mode;
- selected electricity-dependency mechanism;
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

Primary service variables must be selected and operationalized before final slide wording is frozen.

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

2. Which electrical-dependency architecture is selected:
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


## Presentation resilience cycle

Use the thesis-defined cycle:

```text
IMPROVE → ADAPT → RESTORE → LEARN → IMPROVE
```

Presentation meaning:
- **Improve:** strengthen future service capability relative to a baseline.
- **Adapt:** modify operation as physical states evolve.
- **Restore:** return degraded electricity and mobility service to an acceptable/reference level.
- **Learn:** use evidence from disturbance and recovery to improve the next design/operating decision.

Do not present this as a universal resilience standard. Present it as the thesis operational engineering cycle.

For slide logic, use:
```text
physical state
→ functionality
→ serviceability
→ service trajectory
```
with reliability evaluated over the service trajectory and resilience evaluated through disturbance response and Improve–Adapt–Restore effectiveness.


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
