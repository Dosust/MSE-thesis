# Thesis conceptual framework — physics-adapted operational application V1

**Status:** ACTIVE COMPANION / REVIEWABLE METHOD, NOT A CANONICAL SCOPE OR OBJECTIVE AMENDMENT.
**Basis:** User-provided *How to Construct a Scientifically Rigorous Conceptual Framework*, 2026-10-10, with methodological references to Jabareen (2009), Hernán and Robins, Baron and Kenny (1986), and MacKinnon et al. (2007). Bibliographic facts and specific causal-method claims require the usual source-level check before publication.
**Authority:** `project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md`, `project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md`, `project/CONCEPTUAL_FRAMEWORK_SPEC_V5_THERMAL_SUSTAINABILITY.md`, `project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md`, `project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md`, `project/CANONICAL_SUSTAINABILITY_TWO_PATHWAY_ASSESSMENT_V1.md`.
Do not rewrite those frozen files. Neither a hypothesized path nor a conceptual diagram establishes causality.

## Research-specific framework
External extreme heat `H(x,t)` (forcing, **not** an internal state) → temperature/energy evolution of distinct Power `P` and Electrified Transportation `T_e` equipment → physically supported thermal capability/limits → **separately qualified** P→T_e and T_e→P mechanism candidates → events/propagation in state–time → electricity and mobility service outputs → resilience interpretation; two sustainability assessment pathways remain downstream.

### System and ontology
- **Systems:** `P` and `T_e` remain distinct. EVSE belongs to `T_e`. AC interface is a port/coupling object, **not** a third system.
- **Forcing:** ambient heat, radiant exposure and other admissible external conditions; shared heat is a competing common-cause explanation.
- **States:** minimum justified thermal states (e.g., transformer hot spot, EVSE thermal state); battery SOC only where the mobility service mapping needs its energy dynamics; degradation only where admissible.
- **Inputs/controls:** load, charging commands, cooling/protection settings; measured operating controls must not be drawn as free physical fluxes.
- **Algebraic observables:** grid-side `V_AC`, `I_AC`, `P_AC`, `Q_AC`; AC input is not automatically DC charging output.
- **Capability/constraint:** physically sourced operating restrictions or charging capability maps, distinct from the measured thermal state.
- **Service:** thresholded electricity and mobility requirements, not simply a transformer temperature or EVSE rated kW.
- **Outputs:** conditional critical-transition time, directional propagation delay (only if causally qualified), service consequences, resilience, and sustainability effects in two pathways.

## Research-question and relationship specification
| Relationship ID | Proposed relation | Required mechanism/evidence | Rival/alternative | Status |
|---|---|---|---|---|
| F-P | external extreme heat → transformer thermal response | heat-balance law, loading, cooling, admissible transformer type | electrical loading, cooling policy | CANDIDATE / parameters OPEN |
| F-T | external extreme heat → EVSE thermal response | actual charger topology and derating-control characterization | load-dependent converter losses | CANDIDATE / device data OPEN |
| P2T | transformer thermal state → qualified operational restriction → grid AC capability → EVSE charging capability | verified limit/control and measurable port quantities | same heat simultaneously reducing EVSE capability without transmission | CANDIDATE, NOT VALIDATED |
| T2P | EVSE thermal state → control response → changed AC input → transformer losses/thermal response | measured or technically defined AC-demand map under intervention | concurrent grid demand and ambient forcing | CANDIDATE, NOT VALIDATED |
| C-S | conditionally qualified mechanism → required electricity/mobility service consequence over time | explicit service requirements, timing and comparator | service unaffected despite component temperature rise | OPEN |
| S-R | service trajectory → resilience interpretation | frozen resilience definition and reference service requirement | no accepted service metric | INTERPRETATION RULE |
| S-D | service consequence → direct environmental/economic/social sustainability effects | measured indicators, boundary, horizon and factors | unavailable valuation/emissions factors | CONDITIONAL |
| I-S | Improve/Adapt/Restore → changed service relative to matched case → sustainability dimensions | engineering response parameters, comparators and indicator accounting | intervention costs and rebound | CONDITIONAL |

**No invented data**: IEEE 13-node B0 reproduction, B1 EVSE augmentation, IEEE 123-node primary application and component-level thermal validity remain governed by separate verification and data gates. Forty candidate registry entries are **not** 40 qualified dynamic states.

## Six relationships that must not be conflated
1. Structural connection ≠ functional or thermal causal dependence.
2. Shared extreme-heat forcing ≠ directional P↔T_e propagation.
3. External boundary temperature ≠ inward heat-flow-rate `W`.
4. Dynamic state ≠ operating capability ≠ service ≠ resilience.
5. Proposed mechanism ≠ identified causal effect ≠ physically validated model.
6. Conceptual framework ≠ theoretical foundations ≠ differential-algebraic equation model ≠ numerical experiment.

## When generic causal variables are appropriate
- A **mediator** is a causal-path role for a precisely defined intervention/outcome pair, not an automatic name for an electrical interface, heat store or operational state.
- **Effect modification** (moderation) may describe how an admitted response changes with ambient temperature or controls; this does not require a superficial `XZ` regression.
- A **confounder/common cause** (e.g., ambient heat) is handled with matched scenarios, physics, measurement and explicit causal assumptions. Adjusting for downstream effects can induce bias; never add a control because a dataset contains it.
- **Statistical regressions** are admissible only for declared estimation/identification tasks with suitable data and assumptions; physical conservation laws and hybrid DAEs remain primary when justified.

## Framework operationalization and falsification procedure
For **each** proposed relationship register: (1) source/target and ontological types; (2) system/control-volume boundary; (3) arrow type, sign, units and admissible mechanism; (4) evidence source and rights/quotation status; (5) counter-hypothesis and confounding; (6) measured/estimable quantities; (7) time order and delay definition; (8) experimental comparator or physical derivation; (9) uncertainty and missing data; (10) scientific decision PASS, FAIL, OPEN, NOT_RUN.

SO1 identifies and qualifies candidate states/directions. SO2 builds the **minimum sufficient** admitted state-time model, with laws/bounds/units. SO3 quantifies **only supported** transitions, propagation and service consequences (no manufactured threshold crossings). These map to frozen objectives without adding objectives or asserting a result.

## Representation and QA
A scientific framework figure includes only necessary state, boundary, forcing, port, constraint, service and research-logic objects. Dashed / explicitly conditional arrows for proposed effects; distinct arrow semantics for AC power, heat exchange, control, measurement, causal claims, and workflow. Every externally sourced claim requires adjacent author–year citation. In Deck3: 14 slides, infographic Slides 3–12 only, exact approved palette, pure white interiors, Times New Roman, 16:9; equations are native math where supported. Do not infer causal verification from a generated diagram/animation.
