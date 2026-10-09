# Focused literature-to-physics-to-service-to-sustainability/SDG execution V1
**Date:** 2026-10-09
**Status:** RESEARCH EXECUTION DIRECTIVE; does not amend frozen title, thermal scope, GO/SO1-SO3 or claim validated results.
**Official title:** Physics-Based Mathematical Engineering of Power–Electrified Transportation Interdependencies for Resilience.
**Priority:** stop writing broader frameworks; complete critical full-text extraction and model-admission for one physically specified thermally coupled case.

## Permanent SDG rule — MUST NOT BE DROPPED
Retain sustainability **and explicit SDG traceability** in all future thesis literature syntheses, model designs, experimental outputs, interpretation and manuscript planning. Canonical source: `project/CANONICAL_SUSTAINABILITY_TWO_PATHWAY_ASSESSMENT_V1.md`. The binding chain is **measured, source-backed indicator → environmental/economic/social dimension → relevant exact UN SDG target → official indicator if matching**. Do NOT assert that a study-specific equipment indicator measures an official national/global SDG indicator. If no measured indicator, label SDG linkage `OPEN_NOT_DEMONSTRATED`. SDG does not create a fourth research objective or justify additional broad modeling.

## Bounded physical demonstrator (CANDIDATE, NOT FROZEN)
Distribution transformer (P) → feeder/AC meter/interface → DC EVSE + charging connection + electric battery vehicle (bounded T_e subset). Full T_e system composition stays canonical. Extreme heat `H(t)` is external forcing separately on relevant equipment, not cross-system causal proof. Select actual transformer cooling class, EVSE thermal control, AC/DC efficiency and load accounting, vehicle charge requirement and service deadline only from admissible literature/equipment records.

## Eight nested investigation gates
| Gate | Inputs and evidence to acquire | Physics, mathematics, engineering method | Qualified output |
|---|---|---|---|
| 1. Reality | Equipment topology, nameplates, meteorology/siting, timestamps, measurement definition, missingness, controls, source provenance | Draw real AC/DC boundary, equipment functional requirements, measured vs modeled variables | Reproducible physical case and evidence admission ledger |
| 2. P thermal | Load/current and core/copper loss evidence, ambient/cooling, transformer design/sensors | First law: `dU_P/dt=P_loss,P-Q_rej,P`; admit specific heat transfer/thermal capacitance law and operating capability policy only after source audit | Verified choice of thermal state(s), loss/cooling terms, law/units/range |
| 3. T_e thermal/energy | Charger inlet/outlet power, converter losses, operating temperatures, cooling/derating measurements, vehicle demand/SOC/deadline | `dU_C/dt=P_loss,C-Q_rej,C`; AC/DC accounting `P_AC=P_DC+P_loss,EVSE` (auxiliary boundary explicitly specified); `dE_B/dt=P_B,net` after losses/aux accounted | Temperature-conditioned charger power and EV delivered energy (case-specific) |
| 4. Interface | Synchronized AC-side meter, control policies, constraints, source/receiver events | Investigate P→T_e: documented transformer state→permissible supply→EVSE AC input→charging/delivery; T_e→P: charger temperature→AC draw→transformer loading→P thermal dynamics. Each independent causal attribution; ordinary charging alone not thermal interaction | Admitted directional mechanism or explicit failure to qualify |
| 5. Mathematical state-time | Measured/estimable minimum states, inputs, parameters, limit evidence | Conservation-based ODE/DAE with algebraic interface; observation function, estimability/identifiability, dimensional checks; `t_i=inf{t:g_i(X,H,u)=0}` only with qualified threshold; delay between causally attributed events | Minimum sufficient model and identifiable event definitions |
| 6. Experiment + VVUQ | Matched heat/load scenarios, independent holdout, uncertainty distributions | Compare M0 common heat only vs M1 electrical interface vs M2 qualified thermal-state dependence without silently changing other factors; numerical convergence, conservation residual, calibration, held-out validation, sensitivity, alternative explanations | Supported/unsupported state-time and service effect with uncertainty |
| 7. Resilience services | Declared supply/service requirements, vehicle energy by departure, operating time window | `Q_P(t),Q_T(t)` versus `Q_P^req(t),Q_T^req(t)`; deficits, threshold crossing, duration, recovery ONLY when modeled. Avoid treating transformer lifetime or SOC as mobility service automatically | Service trajectories, consequence timing, and evidence-bounded resilience interpretation |
| 8. Sustainability + SDG | Same case/time/boundary as experiment, losses, emissions factors, costs, accessibility/continuity evidence | Pathway A: heat/coupling→services→impact; pathway B: optional improve/adapt/restore response→difference vs heat case. Compute three *separate* dimensions; functional unit and denominators explicit. Then map eligible indicators to SDG targets using official UN metadata | Comparable environmental/economic/social indicators and target-level SDG relevance (or explicit OPEN) |

## Narrow physics and mathematical admission list
- First-law energy balances and AC/DC conservation are foundational; **their chosen lumped ODE, parameter values, temperature-dependent constitutive relation and control rule are not yet admitted**.
- Thermal inertia and possibly convection/radiation: state only if equipment geometry/materials and temperature range support them. No fabricated thermal resistance/capacitance, standard coefficients, thresholds, efficiency or derating curve.
- DAE candidate: `dot X_P=F_P(X_P,Z,H,u;theta_P)`, `dot X_T=F_T(X_T,Z,H,u;theta_T)`, `0=G(X_P,X_T,Z,H,u;theta)`, `Q=S(X_P,X_T,Z,u)`. Do not confuse external heat forcing, SOC energy state, thermal states, capability functions or measured service.
- Key mathematical tasks: state-space construction, well-posedness/units, numerical methods/stiffness as appropriate, sensitivity/uncertainty, parameter identification and observability, event-time definition and error, counterfactual/matched causal comparison, possible interval confidence on service deficit/delay.
- Do not add generic graph theory, optimization, viability/PDE, all-hazard multi-layer dynamics merely for breadth. Add only if a named scientific gate cannot be answered without it.

## Full-text paper reading order / questions
**Priority A: closest overlapping integrated prior art and real equipment laws.**
1. Hilshey et al. (2013), DOI `10.1109/TSG.2012.2217385`: extract transformer dynamic state/parameter equations, EV charge schedule-to-load interface, ambient/load inputs, observation, service timing, validation and exact limitations. Accessible author full text: https://phines.w3.uvm.edu/publications/2013/hilshey_2013.pdf
2. Krama et al. (2026), DOI `10.1016/j.ecmx.2026.101960`: audit experimental fast-charger thermal derating, measured equipment temperatures, offered vs AC-input power, confidence/transferability. Full text required, not yet audited.
3. Visakh & Selvan (2023), DOI `10.1016/j.segan.2023.101096`: extract documented transformer thermal capability vs operational mitigation and measured supply consequences.
4. Ji et al. (2025), DOI `10.1016/j.apenergy.2025.126806`: identify exactly which power/transport/temperature and user service effects are already modeled.
5. Wang et al. (2026), DOI `10.1016/j.ress.2025.112005`: discriminate existing dynamic interdependency innovations from thermal-specific contributions.
Follow with transformer P01-P14 source/standard audits and charger/manufacturer reports where accessible. Current `project/literature_review/thermal_26_audit_2026-10-09/PROVISIONAL_26_CORE.csv` is NOT a full-text-certified set. Do not assert novelty yet.

For **each paper** create a full-text-backed extraction: bibliographic DOI and exact PDF/page; physical device/case; input series and units; control; boundary; laws/equations copied accurately with page refs (summarize if copyrighted); assumptions/ranges; state and output definitions; interface quantities; parameters and provenance; measured data; calibration vs validation; findings with uncertainty; similarities/differences to our exact proposed case; model transferable YES/NO/CONDITIONAL; unresolved contradiction; source-access level. Cite author–date immediately beside each external scientific assertion.

## Candidate minimum dataset columns (DO NOT fabricate rows)
`time_utc`, `ambient_C`, `transformer_loading_A_or_kW`, `transformer_oil_temp_C` if measured, `EVSE_component_temp_C` if measured, `EVSE_AC_input_kW`, `EVSE_DC_output_kW`, `charger_control_limit_kW`, `vehicle_SOC_or_battery_energy`, `vehicle_departure_deadline`, `electricity_service_requirement`, `mobility_service_requirement`, equipment ID, sensor placement/calibration, source/license, uncertainty flags. Data sufficiency depends on the ultimately admitted model; these are candidates, not mandatory universal quantities.

## SDG candidate relevance and exact-match restriction
- **SDG 7:** energy service continuity/access and system/charging losses may be locally relevant to Target 7.1 or 7.3, but **official 7.1.1 measures population with electricity access, and 7.3.1 measures energy intensity of primary energy per GDP**. Charger efficiency or kWh loss is *NOT* either official statistic. Target-level alignment only if justified.
- **SDG 9:** resilient infrastructure, Target 9.1 is a plausible qualitative link. Official 9.1.2 is passenger and freight volumes by transport mode; a single fleet's on-time departures are *NOT* the national SDG statistic.
- **SDG 11:** transport access/service can motivate target-level consideration only when meaningful accessibility/coverage data are available; EV charging availability alone is not official 11.2.1.
- **SDG 13:** emissions consequence can support target-level climate relevance if grid emissions factors and boundary are defensible; **official 13.2.2 is total greenhouse gas emissions per year**, not a local model's avoided emissions.
- **Economic/social metrics:** operating/intervention cost, accessibility/service-disruption duration, distributional equity if recorded. Do not map to an SDG target by superficial word association.
- Exact UN metadata authority: https://unstats.un.org/sdgs/metadata/ ; relevant UN goal pages https://sdgs.un.org/goals/goal7 and https://sdgs.un.org/goals/goal9 .

## Immediate execution queue
1. Full-text inspect and extract Hilshey equations, boundary, empirical method and limits with precise page evidence.
2. Obtain/inspect Krama full text and relevant EVSE thermal control law; avoid assuming transferability.
3. Audit Visakh and the nearest integrated comparisons; write a bounded prior-art matrix / explicit novelty OPEN.
4. Pick equipment-matched available measured data and operating law. If absent, register blocker and continue independent source work; do not manufacture a case.
5. Admit minimum model, write reproducible verification/validation protocol, then derive/resimulate/test and report actual results.
6. After quantitative outputs, report the bounded two-pathway sustainability vector and **target-level SDG trace matrix**, including unsupported/OPEN rows.

**Definition of research progress:** paper equation/measurement extraction + admitted mechanism/model parameter/data + auditable tests. A more elaborate conceptual infographic is not progress toward validation.
