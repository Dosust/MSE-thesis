# Literature-to-measurement physics and validation crosswalk — v0.1

**Date:** 2026-11-03  
**Project:** Physics-based mathematical engineering of power–electrified transportation interdependencies for resilience under extreme heat.  
**Research branch:** `user-data-qualification-2026-11-03`.  
**Evidence level:** Working source-to-dataset synthesis; **not** a complete systematic literature review, a frozen novelty claim, or evidence of joint connected-field validation.

## 1. What the four critical comparators can actually establish

| Literature or dataset | Measured physical evidence | Modeled physical/mathematical evidence | Known limits | SO objectives |
|---|---|---|---|---|
| **Fletcher & Khan, RACE for 2030 (2025)** [original report](https://www.racefor2030.com.au/content/uploads/Final-report-0571-FINAL-FINAL.pdf) | Practical transformer heat-run tests inform parameter discussion; Part 1 is not verified installed transformer-to-EVSE multi-month monitoring | IEC 60076-7-style transient transformer temperatures, dynamic inertia/rating and temperature-aware charging; example of 1 MVA simulated transformer and 23 EV sessions | Simulation conditions and model coefficients cannot be transferred blindly; Part 2 long-term instrumented field validation is future work in this report | SO1/SO2, modeled SO3 |
| **Krama et al., Qatar (2026)** [DOI](https://doi.org/10.1016/j.ecmx.2026.101960) | Publisher-described field experimental data from a commercial 50-kW DC charger under 15–55°C ambient; operating derating and reported charging-time change (86 min winter to 169 min extreme summer for study conditions) | Thermal/empirical EVSE derating relationships are candidates for source-specific extraction | Raw observations on request; *not* a measured thermal response of the supplying transformer; fuller equations/controls need original paper and raw data | SO1 EVSE, SO3 conditional charging time |
| **Li, Chang & Lu (2026)** [DOI](https://doi.org/10.1109/PESGM58988.2026.11693150) | Abstract describes measurements on both sides of a 2,000-kVA operating bus-charging station transformer, including losses and harmonics | Candidate electrical interface and harmonic-loss model; details require primary full text | Actual thermal sensors, nameplate/loss separation, common site asset map and downloadable raw records not confirmed | SO1 electrical physical interface, supporting SO2 |
| **TUM EV UDS field source (2026 repository)** [original repository](https://github.com/TUMFTM/electric-vehicle-uds-dataset) / [saved audit](https://github.com/Dossiya-SE/MSE-thesis/blob/main/data/field_candidates/2026-11-03/TUM_ID1_FIELD_THERMAL_QA_2026-11-03.md) | Source describes seven production EVs under operational road/charging/parking conditions. User Mac-local ID1 original Parquet readback reports 40,401,700 long-format rows; ambient observed −9.5..39.5°C | Candidate battery thermal model inputs and cross-vehicle tests *after* sensor/charging-state QA | Repeated 1023°C-like ID 1272/1273 readings; original 7-file SHA-256 pending; source bytes not backed up to Drive; EVSE rectifier thermal measurements and supplying transformer mapping absent | SO1/SO2 vehicle component only |

These four are **complementary**, not physically connected equipment. Published/archived authors' claims must retain source-specific conditions. Neither abstract evidence nor a simulation is a same-site measured bidirectional interface.

## 2. Physical quantities that literature helps formulate, versus actual measurement coverage

| Quantity / interface state | General physics candidate | Available measured support | Missing for true interdependency validation |
|---|---|---|---|
| Transformer top-oil/winding thermal state | `C_P dT_P/dt = P_loss,P(I,T_P) - Q_cool,P(T_P,T_a)` | SINTEF 8,592 hourly operational transformer sensor records; RACE physics comparator | Transfer-tested thermal coefficients; extreme-heat monitored operation; measurement of actual supplying transformer for the EVSE |
| Station transformer loading and reactive power | `S = sqrt(P^2+Q^2)` **after units verified** | Slovenia 12 stations × 34,932 15-min P/Q pairs; Li study as partial field-interface comparator | Slovenia P/Q units/sign/nameplates; same-site thermal sensors, EVSE meter boundary and documented topology |
| Vehicle battery thermal and charge states | `C_B dT_B/dt = Q_gen - Q_removed` | KU Leuven controlled charging signals; TUM **vehicle field** pack/battery temperature after QA; OSF PQ charging lab | Verified pack thermal-state definitions, cooling-power/heat source, actual TUM charge synchronization, independently identified coefficients |
| EVSE rectifier/heatsink thermal state and derating | `C_E dT_E/dt = P_loss,E(P_ac,T_E) - Q_cool,E(T_E,T_a)` | Qatar publisher-reported field charger temperature and derating, raw *not acquired*; KU Leuven electrical converter boundary only | Original synchronized rectifier temperature, delivered/grid power, cooling state, rated limit and reason-code logs; charger-to-transformer topology |
| Power→transport restriction | `P_EV <= min(P_site_cap(T_P), P_EVSE_cap(T_E), P_vehicle_accept(SOC,T_B), ...)` | Hypothesized from conservation and thermal-limit research; RACE simulated transformer-aware controller | Observed same-site transformer reason-code curtailment affecting charger output; temporal onset/lag and confounder control |
| Transport→power demand and heating | `I_P(t),P_P(t) <- P_EVSE(t)` with feeder power balance | EV charging curves, Slovenian station P/Q **on different installations**; Li field station transformer electrical data | Actual topology/meters on same site and simultaneous thermal response to charger demand |
| Electricity and mobility services | `unserved_energy = integral(max(0,P_req-P_delivered),dt)` with deadlines | RACE simulated requested 1,364 kWh vs delivered 1,262 kWh over 10 h; Qatar field charging-duration effect | Measured matched service commitments, departures/trips and outages; validated resilience indicators |

**First law is transferable as a governing principle.** Constitutive terms, physical parameters, reduction to a particular RC/ODE model, operating domain and claims about actual installation response require source-specific calibration and independent verification. TUM may aid battery-side field validation only after anomaly and charging-event QA.

## 3. RACE quantitative claims — simulated, not field-caused

The [existing v0.1 protocol's extracted original-report table](./TARGETED_LITERATURE_THERMAL_PT_SYSTEMATIC_PROTOCOL_V01.md) records a 1-MVA model at 0.75 p.u. non-EV loading and five-minute between-session gaps. Illustrative modelled **equivalent aging factor** increases from **0.19** for 15–25°C ambient cases to **1.88** for 35–45°C cases, under the specified study assumptions. This is *modeled aging*, not observed equipment lifetime loss.

For the report's 23 EVs over 10 simulated hours, requested energy is **1,364 kWh**, delivered **1,262 kWh**, shortfall **102 kWh** (7.48% of requested). This is an energy service proxy, **not measured missed vehicle departures**. The original report's selected time constants and hysteresis threshold values are not automatically applicable to SINTEF, Slovenia or another installation.

## 4. Model structure proposed for future independent validation

For power transformer `P` and charger `E`, use a first-law-reduced candidate model only after distinguishing measured states from modeled quantities:

```math
\begin{aligned}
C_P\dot T_P &= P_{\rm loss,P}(I_P,T_P;\theta_P)-Q_{\rm cool,P}(T_P,T_a;\theta_P),\\
C_E\dot T_E &= P_{\rm loss,E}(P_{\rm AC},T_E;\theta_E)-Q_{\rm cool,E}(T_E,T_a;\theta_E),\\
P_{\rm AC} &= \Phi(T_P,T_E,\mathrm{SOC},u,d;\theta_{\rm interface}).
\end{aligned}
```

The electrical interface `Phi` must satisfy a defined feeder topology and equipment power balance; it cannot be calibrated from unrelated country-level datasets by timestamp joining. An actual model requires equipment classes, temperature sensor positions, cooling paths, current-to-loss law, converter thermal law, SOC/vehicle acceptance logic, and documented derating/restriction controls.

Distinguish thermal evolution `tau_thermal`, downstream propagation delay `delta_propagation`, and electricity/mobility service degradation onset `tau_service`. These are **not** interchangeable.

## 5. Immediate prioritized experimental and literature program

1. **RACE source-to-equation verification (SO2):** extract and independently derive the transformer thermal differential/difference equations with page/equation citations, boundary conditions, heat-run calibration and assumptions; demonstrate how SINTEF sensor data inform estimable effective parameters without pretending to identify all losses/capacitance.
2. **Qatar original high-heat EVSE source (SO1):** obtain/request underlying ambient, rectifier/heatsink temperature, power, timing and thermostat/control logs; verify seasonal covariates, equipment model and thermal-versus-SOC derating labels. Until obtained, **no thesis-fitted validated EVSE heat equation**.
3. **Li electric-bus site interface (SO1):** obtain complete paper and any data/author access, verify transformer primary/secondary metering, sign conventions, harmonic-loss calculation, sensor types and whether onsite thermal data exist.
4. **TUM source QA (SO2):** capture all seven original SHA-256 checksums; reconcile 1023°C-like codes, nominal measurement bounds, timezone and charging-state labels before thermal calibration. Then attempt **vehicle-separated** external testing under matched/adjusted parameter conditions.
5. **Connected physics synthesis (SO1–SO3):** compare uncoupled, statically-coupled and dynamically-coupled models under matched design inputs; test thermal sensitivity, parameter identifiability, uncertainty, service thresholds and control trades. Label simulations **conditional**.
6. **Systematic review completion:** execute logged Scopus/IEEE/Web of Science/etc queries, deduplicate and screen, extract primary full text, maintain reproducible reasons for exclusion and report PRISMA 2020 counts *only when the full search has actually run*. Test novelty against later RACE work and all close comparators before making a global novelty claim.

## 6. Scientific evidence gates and priorities

| Gate | Present status | Requirement for promotion |
|---|---|---|
| Literature targeted scoping | 10 studies in first-pass review, RACE full technical extraction | Primary full-text equation-level study extraction and logged database searches for systematic review |
| Transformer component thermal | SINTEF first constrained model, same-site holdout only | Physical parameter identifiability, independent-installation validation and high-heat regime evidence |
| Station electrical component | Slovenia paired P/Q original acquired; unit/nameplate issues | Original units/sign conventions, ratings, electrical balance checks |
| Vehicle thermal field | TUM original files user-local, QA pending | Non-sentinel field channels, charging-time overlap, source hashes, 7-vehicle QA and independent vehicle split |
| EVSE internal thermal field | Qatar study found, raw records on request | Primary time-aligned charger interior temperature/control/power original files |
| Actual coupled Power↔EVSE thermal field | **NOT PROVEN** | A documented same-site feeder connection, synchronized transformer+charger thermal/electrical data and observed equipment restriction reasons |
| SO3 resilient service effects | Reported RACE conditional energy proxy; no real same-site mobility consequences | Defined actual required/delivered energy, vehicle deadlines, system interventions and matched validation |

**Progress:** Retain previously stated *provisional* progress estimates: SO1 35%, SO2 20%, SO3 5%, equal-weight overall 20%. Do not inflate them solely on article identification or dataset acquisition.

**Related:** [Targeted literature protocol](./TARGETED_LITERATURE_THERMAL_PT_SYSTEMATIC_PROTOCOL_V01.md); [Report 1 RQ1–RQ11](./REPORT_01_MEASURED_DATA_RQ1_RQ7_2026-11-03.md); [3 Nov checkpoint](./THESIS_RESEARCH_CHECKPOINT_2026-11-03.md); [master dataset inventory](./MASTER_DATA_INVENTORY_2026-11-03.md).
