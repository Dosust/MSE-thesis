# Thermal Interdependency Dataset Acquisition and Evidence Register V1

**Date:** 2026-10-13  
**Status:** WORKING ACQUISITION AND QUALIFICATION REGISTER — NOT AN EXPERIMENTAL VALIDATION CLAIM  
**Repository:** `Dossiya-SE/MSE-thesis`  
**Scope:** Power System (P) and Electrified Transportation System (T) electrical–thermal interfaces under extreme heat.  
**Inventory convention:** **14 entries** = five core sources/requirements, six supplementary publicly discoverable datasets/sources, and three conditional evidence requirements. **Not all 14 are downloadable datasets**: D04 is a peer-reviewed thermal-parameter publication; D12–D14 are measurement requirements, not identified public repositories.

## 0. Governing authorities and frozen boundaries

This working inventory is subordinate to:

- [Canonical evidence and non-invention standard](../CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md)
- [Frozen general and specific research objectives](../CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md)
- [Approved eight components](SELECTED_EIGHT_COMPONENTS_WORKING_RESEARCH_BASELINE_V1.md)
- [Eight-component evidence and model-admission protocol](EIGHT_COMPONENT_EVIDENCE_AND_MODEL_ADMISSION_RESEARCH_PROTOCOL_V1.md)
- [Directional physical-interface dossier](EIGHT_COMPONENT_PHYSICS_AND_DIRECTIONAL_INTERFACE_RESEARCH_DOSSIER_V1.md)
- [Canonical thermal scope](../CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md)

**Do not change** GO/SO1–SO3, three working research questions, two candidate hypotheses, component identities, I1–I7 classification, or conditional model status merely because a dataset becomes available. Source discovery and download do not establish equipment eligibility, identifiability, causality, or physical validation.

### Central I2 question

Determine whether the **actual measured charger grid-side** active/reactive demand \((P_{\rm AC},Q_{\rm AC})\) is identifiable as a function of internal rectifier temperature, EVSE cooling/thermal modes, battery acceptance, request and other relevant operating factors. Only subsequently investigate the conditional influence of *measured or qualified* AC demand on P2 loading and P1 temperature.

\[
(T_r,u_{T3},SOC,P_{\rm req},V_{\rm AC},\ldots)
\longrightarrow (P_{\rm AC},Q_{\rm AC})
\longrightarrow I_{P2},I_{P1}
\longrightarrow \theta_{P1}(t).
\]

**Common ambient temperature is an external forcing, not proof of a cross-system influence.** An experiment with charger and transformer measurements from different sites cannot be presented as field validation of a joint installation.

## 1. Core evidence sources and requirements (D01–D05)

| ID | Source, primary link | Relevant physical quantities | Access/evidence state as of this register | Permitted use and limitation |
|---|---|---|---|---|
| **D01** | [Schultis & Ilo: TU Wien LV Test Grids v1](https://doi.org/10.17632/hgh8c99tnx.1) | 160 kVA 20/0.4 kV transformer; 20Cable feeder topology, line impedances, customer loads, published electrical solution | **Previously acquired/reconstructed in research workflow**; verify original workbook, hashes and reconstruction artifacts in the current execution environment | P1/P2 reproducible electrical benchmark and conditional charging-scenario response. Not the actual Qatar charging network or a thermal experiment |
| **D02** | [Krama et al. (2026): Qatar Siemens CPC50 experiment](https://doi.org/10.1016/j.ecmx.2026.101960); [Sezer & Bayhan (2025) conference study](https://journals.library.torontomu.ca/index.php/ictea/article/view/2606) | Charger ambient and rectifier temperatures, observed AC input/DC output, thermal derating, SOC, charging duration, efficiency, power quality; request original synchronized AC P/Q and controller traces | **Published physical evidence; raw synchronized observations not acquired**. Public text/figures are not an independently admitted numerical dataset; request data from authors | Primary T1/T3 thermal-derating precedent and prospective direct I2 identification; **reactive-power time-series availability not independently established** |
| **D03** | [Esser et al. (2025) open AC/DC charging profiles](https://zenodo.org/records/14065331) | Measured grid-side active/reactive power, charger/DC variables, SOC, charging commands/setpoints, ambient where documented | **Public repository**, files to acquire and audit; first inspect `measurements.csv` and `parameters.csv` | Open AC/DC interface identification and method validation on its **own** equipment; no established internal rectifier-temperature derating |
| **D04** | [Najar et al. (2017) transformer top-oil thermal modeling](https://doi.org/10.1016/j.applthermaleng.2017.03.061) | Published experimentally fitted ONAN thermal parameters, including 160 kVA example | **Published parameter authority; not an admitted raw field dataset** | Conditional 160 kVA thermal surrogate, with cooling-family and parameter-transfer limitations. Do not interpret the source's matching kVA as proof of TU Wien equipment equivalence |
| **D05** | [Bærug et al. (2025) measured 40 MVA ONAN transformer data](https://zenodo.org/records/17223516) | Hourly measured current, voltage, ambient, top oil, bottom oil, winding temperatures and clamping quantities | **Uploaded and audited in preceding research work**; 2024 measurement series. Separate real-data holdout evaluation reported (MAE 0.907 K; RMSE 1.156 K); these values require the associated V3 code/results for independent reproduction | Separate equipment-specific 40 MVA physical-time model evaluation only; never substitute fitted parameters for the TU Wien–Najar 160 kVA model. The source's calculated file is **not measured ground truth** |

The **CPC50 bottleneck (D02)** is an *identified thermal state → actual measured grid-side AC demand* law, not the mere presence of published charger AC measurements. An independently evaluated charger law still does not validate the TU Wien–Najar composite installation.

## 2. Supporting publicly discoverable sources (D06–D11)

| ID | Dataset and official entry | Evidence to inspect in original files | Recommended role | Status / caution |
|---|---|---|---|---|
| **D06** | [EPFL Level-3 EV charging data](https://github.com/DESL-EPFL/Level-3-EV-charging-dataset) | Measured AC charging power, station setpoint `Pset`, vehicle request `Preq`, SOC, session times | Separate charger-request versus realized-demand comparison; candidate alternative electrical interface | Public repository; **internal charger thermal state not established** |
| **D07** | [KIT / Beichter et al. (2026)](https://zenodo.org/records/17866847) | Per-phase AC active/reactive power, V/I, charger setpoints, SOC, ambient, sample intervals and phase boundaries | Independent AC P/Q interface and operating-regime benchmark | Public repository; acquire lower-frequency files first; **internal rectifier temperature not verified** |
| **D08** | [Shenzhen Autosun–PolyU charging data](https://data.mendeley.com/datasets/c7gg94tmvz/3) | Charging port V/I/P, SOC, charging-gun temperature(s), interruption codes, timestamps | Investigate connector-temperature-associated charging outcomes | Public numerical dataset; **connector temperature ≠ internal rectifier temperature**; published field list does not establish grid-side AC P/Q |
| **D09** | [KU Leuven charging datasets](https://doi.org/10.48804/C5PT0R) | Charger/vehicle charging voltage, current, power and battery temperature; identify exact AC/DC metering boundary | Independent battery acceptance and conversion/energy accounting comparison | Public repository; **grid-side Q and internal EVSE temperature not established** |
| **D10** | [KU Leuven high-resolution BEV dynamics](https://doi.org/10.48804/8KPDTW) | Battery/SOC, charging/trip energy, temperature, vehicle operation and measurement boundary | Conditional T2/T4 battery, readiness or trip-energy support where records meet required conditions | Open-data publication; no direct CPC50 internal-temperature law and grid-side reactive-power series not established |
| **D11** | [NASA POWER weather data](https://power.larc.nasa.gov/) | Hourly or otherwise documented ambient temperature, radiation and matching site/time representation | External thermal forcing and declared extreme-heat **scenario** construction | Open meteorological source; site/microclimate representativeness, resolution and contemporaneous alignment must be qualified |

**Public download ≠ admitted evidence.** These repositories should be checked at the file/variable/sensor/operating-envelope level. Session profiles may have different devices, temperatures, meters and sampling rates. Never splice sources into a fictional synchronized experiment.

## 3. Conditional evidence requirements (D12–D14)

| ID | Requirement, not yet a public dataset | Required fields / action | When mandatory |
|---|---|---|---|
| **D12 — P3 / I3** | **Installed** temperature-conditioned transformer protection, control, or load-management traces | Equipment model, enabled rule/setting, measured/estimated P1 thermal input, actual actuator/permission/relay event, timestamp, EVSE AC response; advisory alarms alone are insufficient | Before qualifying candidate I3/H2 as implemented physical P→T restriction |
| **D13 — T4 / I6** | Paired vehicle HVAC / real trip / subsequent charging sessions | Time, ambient, route/distance, traction versus HVAC energy (or justified decomposition), vehicle SOC/temperature, next charging request and availability | Only when investigating delayed vehicle-service-demand thermal effect; not an automatic ninth component |
| **D14 — SO3 service response** | Case-specific electricity and mobility required/delivered-service time series | Required electricity supply, delivered power/energy, charging energy, required departure SOC/time, interruption/recovery markers, service definitions, uncertainty | Before claiming empirically observed cross-sector service resilience or recovery. Conditional scenario outputs must be explicitly labeled modeled |

## 4. Open experimental precedents and software (not new dataset-register IDs)

- [KEBA–AIT 2026, climate-chamber testing of a 320 kW DC fast charger](https://dewesoft.com/blog/dc-fast-charger-climate-chamber-testing): public technical report on thermal derating/recovery and synchronized AC/DC instrumentation; **raw numerical time series have not been located publicly**. Relevant independent literature precedent, not admitted measurement data.
- [Alliander open-source transformer thermal model](https://github.com/alliander-opensource/transformer-thermal-model): independently implemented numerical thermal formulation; **software is not field measurement evidence**. Agreement of recurrences under matched inputs does not establish equipment validation.

## 5. Minimum synchronized CPC50 measurement contract

**Requested joint per-session record**

\[
\mathcal D_{T1}=\{t,\ T_a,\ T_r,\ u_{T3},\
P_{\rm req},\ P_{\rm offer},\ P_{\rm DC,delivered},\
P_{\rm AC,actual},\ Q_{\rm AC,actual},\
V_{\rm AC},\ SOC\}.
\]

Also request: **session/device IDs**, sample frequency and synchronization accuracy; meter location and calibration; AC three-phase V/I/P/Q and sign conventions; charger fan/pump auxiliary input; rectifier temperature sensor location; temperature-limit/derating controller state; DC port V/I; battery/BMS requested/accepted power, SOC/pack temperature; network supply voltage; uncertainty; preconditioning and cooling; charger rated ambient envelope; missingness and data access terms. **Offered DC ≠ delivered DC ≠ battery accepted DC ≠ grid-side AC**. Input-current THD ≠ measured AC reactive power or quantified harmonic transformer losses.

### Evidence admission gates

1. **Source identity and raw integrity:** official repository/publisher version, file list, hashes, units, device and meter identity; license/redistribution conditions.
2. **Synchronize measurement and time:** timestamps, clock zone, AC/DC measurement interval, temperature sensor latency, missing/duplicate records and transition windows.
3. **Qualify physical metering boundaries:** grid-side AC P/Q, DC-port delivery and auxiliary cooling on compatible electrical and temporal bases; conservation checks.
4. **Classify operating regime:** charger thermal-limited versus BMS/SOC/battery-limited, charging request, grid-voltage effects, fan mode and startup/shutdown.
5. **Test thermal variation and confounding:** device rectifier temperature independent enough of common ambient, operating load and SOC; matched comparisons where possible.
6. **Identify bounded law only if supported:** train/test separation by complete sessions and time, physically sensible parameters, residual analysis, uncertainties and validity domain; no reliance on summary curves alone.
7. **Link to P1/P2 conservatively:** use independently measured or qualified AC demand as conditional load input. TU Wien–Najar outputs remain **scenario predictions**, not an installed Qatar feeder observation.
8. **Admit physical I2 only with adequate evidence:** receiver response and attribution as required by the approved component/interface protocol; a successful stand-alone charger regression is narrower than coupled physical validation.

**Stop outcomes:** `NO_SYNCHRONIZED_RAW_AC`, `NO_INTERNAL_THERMAL_STATE`, `BATTERY_LIMITED_UNRESOLVED`, `NO_IDENTIFIABLE_TEMPERATURE_EFFECT`, `NO_EQUIPMENT_VALID_RECEIVER`, `NO_INDEPENDENT_HOLDOUT`. A blocker is a research result; do not invent data, parameter values or validated causal arrows.

## 6. Prioritized acquisition and execution sequence

| Order | Dataset/task | First actionable operation | Completion criterion |
|---|---|---|---|
| **1** | **D02 Qatar CPC50 original data** | Request synchronized per-session AC/DC/temperature and controller records from the corresponding authors; clarify whether true AC Q is available | Documented access decision and, if obtained, raw file identity/measurement contract |
| **2** | **D03 Esser** | Acquire `measurements.csv` and `parameters.csv`; inventory eligible DC sessions before full archives | AC/DC port and signal mapping with source-preserving IDs |
| **3** | **D06 EPFL** | Acquire session and measurement tables; inspect `Pset`/`Preq`/actual AC P | Verified electrical boundary, temporal and request regime mapping |
| **4** | **D08 Shenzhen** | Download and audit thermal charging-port signals and interruption codes | Qualified **connector-only** thermal observation contract |
| **5** | **D07 KIT** | Inspect low-frequency electrical and weather files; defer very large waveform archive | Session-specific P/Q and temperature/context eligibility |
| **6** | **D09–D10 KU Leuven** | Acquire selectively where battery/BMS/HVAC evidence is actually required | Documented relevance to selected T2/T4 model question |
| **7** | **D11 meteorology** | Acquire source weather only for declared site, time and spatial interpretation | Transparent common-heat forcing and scenario assumptions |
| **8** | **D12–D14** | Pursue only as their mechanism/service gates become active | Specific admissible field/operating evidence or explicit OPEN decision |

Priority is **not** based only on file size or availability: the original internal charger-temperature-to-AC measurement chain is the dominant open I2/H1 gate.

## 7. Current evidence decision and non-transferability

- **TU Wien P1/P2:** electrical benchmark already reconstructed in prior work; no matched Qatar distribution field measurements.
- **Najar 160 kVA:** published fitted ONAN parameters support a **conditional surrogate**, not proven TU Wien actual thermal hardware constants.
- **Bærug 40 MVA:** separate held-out measured-temperature evaluation with V3 results reported; not transferable as TU Wien 160 kVA coefficients.
- **Qatar CPC50:** published experimental thermal derating and AC measurement architecture; synchronized numerical dataset **not admitted**. Actual grid-side AC \(P,Q\) temperature-conditioned constitutive law **unidentified**.
- **Esser / EPFL / KIT:** open electrical-interface data candidates. Their distinct hardware do **not** inherit CPC50 thermal response.
- **Shenzhen:** connector thermal observation candidate, not evidence of converter rectifier thermal state.
- **I2/H1:** candidate thermally mediated T→P response **not established**.
- **I3/H2:** actual installed P3 thermally conditioned restriction **not established**.
- **SO3:** service-resilience effects of a real coupled installation **unverified**; scenario-based consequences remain conditional.

**No new objective, hypothesis, physical component, thermal law, model layer, or coupled-system validation is approved by this inventory.** It is a practical source-selection and evidence-acquisition record under the frozen thesis governance.
