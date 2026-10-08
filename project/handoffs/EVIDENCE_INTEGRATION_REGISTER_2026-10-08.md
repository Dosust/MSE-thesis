# Evidence-Led Integration Register — October 8, 2026

**Status:** WORKING LITERATURE/IMPLEMENTATION DECISION AID, not a completed systematic review, equipment-approved model, or evidence of a novel mechanism.  
**Authority:** `project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md`; `project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md`.  
**Companion handoff:** [SPRING_2027_THESIS_HANDOFF_2026-10-08.md](SPRING_2027_THESIS_HANDOFF_2026-10-08.md)

## 1. Research philosophy and test of contribution

Use established physical and methodological pieces to address a **bounded question**. No large, unprecedented "novelty" claim is needed; **but** merely stacking previously published transformer and charging equations is not sufficient. Evidence qualification, physical coupling, a case-specific model, careful comparisons, independent evidence, uncertainty and service-consequence conclusions are the work to be demonstrated. The claim "nobody did it" cannot be made until relevant full prior art has been compared.

Candidate research question, for analysis **only**, not canonical:
> Can established thermal physics and qualified cross-system relationships be integrated to explain how extreme heat influences required electricity and mobility services through physical state and time, and to identify which consequences matter most for engineering decisions?

Closest prior work shows **EV charging + transformer thermal assessment is not new by itself**. A **more precise, case-specific residual research question is still OPEN**.

## 2. 13-item working source register

These entries preserve **the source identifiers and use restrictions from the previous in-chat 2026-10-08 evidence decision brief**. This turn did not re-audit every complete paper or every standard clause. Each record must still be checked to the required evidence depth before model admission.

| # | Work / source lead | DOI or primary source | Potential role | Important limitation / next check |
|---|---|---|---|---|
| 1 | IEEE C57.91-2025 | https://standards.ieee.org/ieee/C57.91/7163/ | Transformer loading/thermal guidance, current-standard lead | Check exact edition, access and relevant clauses; not a device-specific parameter source by itself |
| 2 | Swift et al. (2001) | https://doi.org/10.1109/61.915478 | Thermal-equivalent-circuit theory | Not automatic evidence for the selected transformer calibration or coupled service |
| 3 | Susa et al. (2005) | https://doi.org/10.1109/TPWRD.2004.835255 | Transient transformer thermal modeling | Operating domain, fitted parameters and transferability require review |
| 4 | Qian et al. (2015) | https://doi.org/10.1016/j.ijepes.2014.09.040 | Prior combined EV load / transformer work | Check exact models, assumptions and validation before deciding what is unresolved |
| 5 | Diahovchenko et al. (2023) | https://doi.org/10.1016/j.epsr.2023.109455 | EV charging impacts on distribution/transformer behavior | Compare exact coupling and temperature methods in full text |
| 6 | Visakh & Selvan (2023) | https://doi.org/10.1016/j.segan.2023.101096 | **Critical prior integration** of EV charging, transformer thermal behavior and mitigation | Read FULL TEXT: distinguish thermally conditioned cross-system mechanisms from ordinary charging load; check service vs temperatures, data and verification/validation |
| 7 | Krama et al. (2026) | https://doi.org/10.1016/j.ecmx.2026.101960 | Measured equipment-specific hot-weather fast-charger behavior / derating | Qatar 50 kW equipment-specific case; underlying synchronized measurements reported available on request; do not generalize the derating law |
| 8 | He et al. (2022) | https://doi.org/10.1371/journal.pone.0275231 | Grid/traffic/charging network planning | Not equipment-level extreme-heat thermal state-time validation |
| 9 | Liu et al. (2024) | https://doi.org/10.1016/j.csite.2024.104444 | Transformer winding spatial temperature/ROM comparison | Model-to-CFD and measured winding profile errors are different; global true hottest-spot observability remains OPEN |
| 10 | Li et al. (2026) | https://doi.org/10.1016/j.epsr.2026.113033 | Sparse-sensor transient winding-field reconstruction | Sensor-level comparison does not establish the error of unobserved global hotspot; check exact measurement |
| 11 | Poulin & Kane (2021) | https://doi.org/10.1016/j.ress.2021.107926 | Resilience/service trajectory concepts | Does not freeze this thesis's `Q_P`/`Q_T` service metrics |
| 12 | Oberkampf & Trucano (2002) | https://doi.org/10.1016/S0376-0421(02)00005-2 | Verification versus validation, model credibility | Methodological authority, not validation of our proposed coupled model |
| 13 | Beichter et al. (2026) open EV charging data | https://zenodo.org/records/17866847 | Candidate time-resolved charging measurements (voltage/current/power/SOC/ambient) | Published fields do not automatically include internal EVSE thermal states, Power-side states or actual mobility service demand |

Additional background studies from prior repository work are in Module 01–02 audits. In particular, P11 Souza et al. (2026) ambient/cooling-conditioned top-oil identification was assessed using one transformer and a chronological holdout; full-state observability and heat transfer remain OPEN. P12 Chen & Su (2013) HST Kalman-estimation concept is currently abstract-level evidence. Do not exaggerate their review depth.

## 3. Separate evidence from methodological inference

| Research layer | Known research building block | Is it sufficient by itself for our thesis? | Missing case-specific item |
|---|---|---|---|
| P thermal state | Transformer top-oil/winding models; loading guidance | No | Selected transformer, model constants, valid states, observations |
| Te thermal state | Charger/battery thermal studies and observed derating | No | Exact device, thermal sensors/limits, suitable time series |
| Direction P→Te | Heat-conditioned Power capability can potentially constrain available charging | **Not yet qualified** | Proven Power state→constraint→EVSE/circuit→delivered service mechanism |
| Direction Te→P | Charging current and loading can affect Power thermal dynamics; thermal derating may alter input behavior | **Not yet qualified** | Evidence that the *heat-conditioned* charger pathway changes receiver Power state/capability/service |
| Shared heat | Heat independently affects both sides | **Not interdependency** | Show cross-system causality beyond common forcing |
| State-time | ODE/DAE and measured temporal trajectories | Not final component model | Admit states, physically meaningful thresholds, initial/operating conditions |
| Criticality ranking | Service deficits, timing, uncertainty | Not an automatic universal importance scalar | Specify service levels, units, case context, comparator and trade-offs |
| Resilience | Required-service maintenance/recovery | Not a metric by itself | Quantified Q_P/Q_T requirements, time horizon and, if modeled, recovery |
| Response | Improve, Adapt, Restore (classes) | No | A feasible evidence-backed candidate response and service comparison |
| Sustainability | Two pathways × environment/economy/society | No | Measurable bounded indicators; data; units; costs/burdens; no forced aggregation |

## 4. Preferred provisional integration and rejected shortcuts

**Option A — baseline:** EV charging demand + transformer temperature. Already significantly represented in prior literature; useful benchmark but not enough of an original story by itself.

**Option B — conditional preferred:** one selected Power asset, one selected charging situation, selected thermal states/capabilities, separately evidence-qualified directional thermal interaction(s), matched comparisons, state-time electricity **and** mobility service consequences with VVUQ. **No equipment/model or novelty is frozen.**

**Option C — deferred:** heat-driven charger harmonics → extra transformer losses and multi-directional heat feedback. Needs device-specific spectra, loss models, field evidence; high over-scoping risk in Spring 2027.

Do not:
- force P↔Te bi-directionality when one or both causal directions fail qualification;
- equate generic electricity transfer, charging demand or shared heat with a thermal interdependency;
- turn an ODE, inverse regression or model fitting into independent validation;
- call a simulated temperature, threshold or delay a measured one;
- use a heat/no-heat scenario difference as proof of a specific coupling contribution;
- call charge time/SOC alone a complete mobility-service outcome;
- transfer a charger derating curve or transformer limit from one equipment type to another without justification.

## 5. Required tests before freezing an integrated model

**Gate A — Source and asset qualification:** the exact asset, charger class, operating constraints and data availability are known, with source licenses and provenance.

**Gate B — Mechanism qualification:** for each direction, document source state/temperature, temperature-sensitive capability, transmission path, receiver response, causal evidence, assumptions, limitations, and effect on `Q_P/Q_T`; assign QUALIFIED, PARTLY SUPPORTED, OPEN or REJECTED.

**Gate C — Modeling:** the admitted reduced physical state, input forcing `H(t)`, candidate law(s), parameter units and data fit/verification are defensible; no frozen generic law.

**Gate D — Matched comparison:** case pairs preserve physically consistent demand, heat, initial state and boundary conditions; a coupling-specific difference is identified without an unphysical disabled constraint.

**Gate E — External evidence / VVUQ:** distinguish numerical verification, calibration, holdout validation, sensitivity and uncertainty; do not report improved predictive performance without an independent benchmark.

**Gate F — Services:** define `Q_P`, `Q_T`, requirements, thresholds and temporal horizon before ranking components or comparing a response.

**Gate G — Bounded assessment:** apply response effectiveness to service and energy efficiency to environmental sustainability. Keep `S_env`, `S_econ`, `S_soc` separate.

## 6. OPEN proposed research questions and hypotheses (for supervisor consideration only)

**RQ1 candidate:** Which thermally sensitive physical states and directional thermal interdependency mechanisms between Power and Electrified Transportation can be independently qualified under extreme heat?

**RQ2 candidate:** How can qualified thermal interdependencies be represented in a minimum-sufficient physics-based model of their evolution and propagation through physical state and time?

**RQ3 candidate:** When do evidence-supported critical thermal transitions occur, how do consequences propagate, and what are the resulting required electricity and mobility service effects?

**H1 candidate (conditional physical/mechanism test):** Under appropriately matched heat/initial conditions, inclusion of a qualified directional thermal mechanism yields a distinguishable receiver-state, capability, timing or required-service consequence relative to a physically consistent comparator, subject to uncertainty. Null/no-effect remains admissible.

**H2 candidate (model-skill test):** Where independent evidence exists, a justified coupled model may predict selected validated thermal transitions and/or service outcomes more accurately than an appropriate simpler comparator. **Not assumed true; not required as frozen objective; must be testable.**

**Response proposition — optional:** A feasible Improve, Adapt or Restore action may reduce required-service deficit, delay unacceptable service loss or improve modeled recovery; sustainability effects may remain negative. Do not claim optimization or effectiveness in advance.

Exact wording and final hypotheses remain **OPEN** until approval and data feasibility.

## 7. Data and reading tasks to do first

1. Obtain/check full text of **Visakh & Selvan 2023** and other closest studies; extract source state, operating limits, actual coupling direction(s), time, service endpoints and *type of validation*.
2. Ask Krama et al. authors for possible equipment-specific synchronized charger temperature, offered/delivered power, current, time, ambient and event context; access is not granted until obtained.
3. Examine Beichter et al. charging dataset metadata/availability: locate actually measured fields and gaps, not assume thermal state data or mobility metrics.
4. Identify a specific transformer/Power asset data/model source and candidate charging setting with credible equipment thermal/operating evidence.
5. Draft measurable electricity and mobility service requirements appropriate to that selected case and propose independent validation.
6. Supervisor approves (or declines) case and model feasibility before admitting exact states/limits/interventions.

The next research action is a **mechanism-to-evidence-to-service qualification matrix**, not an ungrounded claim of universal theory or a large literature survey.
