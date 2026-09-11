# Canonical Dataset / Database Strategy — Final Thesis Framework

**Status:** CANONICAL DATA STRATEGY as of 2026-09-09, subordinate to the final seven-stage thesis framework and valid until explicitly changed by the author.

## 1. Thesis alignment

This data strategy must preserve the canonical framework exactly:

`Multilayer Structure -> Causal Mechanisms -> Coupled Hybrid Multiscale Dynamics -> Feedback & Control -> Viability -> Resilience-to-Sustainability Transformation Interface -> Sustainable Transformation Pathways`

Core state:

`Y(t) = [X_P(t), X_T(t), Z(t), I(t), O(t)]^T`

The datasets are **evidence sources for the framework**. They do not define or replace the framework.

The central empirical question is:

> Can geographically and temporally aligned observations identify how disturbances propagate across Power–Transportation interfaces, how quickly the coupled system degrades and recovers, how information/organizational response modifies that trajectory, and what the resulting resilience findings imply for sustainable transformation?

## 2. Canonical empirical design decision

There is no single open database that directly observes the full `P–T–I–O` system, causal interfaces `Z`, hybrid events `J`, organizational response `O`, and sustainability outcomes at one common resolution.

Therefore the thesis will use a **multi-source, multi-rate data-fusion architecture**, with California as the preferred primary empirical case because high-quality power, transportation, charging, hazard, and environmental data can be geographically aligned there.

Canonical empirical stack:

`D* = D_P ⊕ D_T ⊕ D_Z ⊕ D_h ⊕ D_O/I ⊕ D_sus`

where:

- `D_P` = power operating/outage/recovery evidence,
- `D_T` = transportation operating/disruption/recovery evidence,
- `D_Z` = observable Power–Transportation interface evidence,
- `D_h` = hazard/event forcing,
- `D_O/I` = organizational and information evidence/proxies,
- `D_sus` = downstream sustainability translation evidence.

**Critical rule:** unrelated datasets must never be merged and described as an observed coupled system unless they overlap in event, geography, and time strongly enough to support that claim.

---

# 3. Priority datasets and what the thesis will extract from each

## Tier A — Primary empirical datasets

| Priority | Dataset / database | Thesis construct | What we are looking for | Canonical stages | Primary limitation |
|---|---|---|---|---|---|
| **A1** | **Caltrans Performance Measurement System (PeMS)** | `X_T(t)`, transport events, `tau_T` | Speed, flow, occupancy, incidents, lane closures, congestion onset, propagation, recovery, accessibility/travel-time degradation | 1, 2, 3, 4, 5 | Transportation only; does not prove P→T or T→P causality by itself |
| **A2** | **ORNL EAGLE-I Power Outage Data** | `X_P(t)`, power failure/recovery, `tau_P`, `tau_R` | Outage onset, customers without power, outage peak, restoration trajectory, restoration rate, recovery time, spatial outage spread | 2, 3, 5 | County-level outage counts; not full electrical network state/topology |
| **A3** | **CAISO OASIS** | Power operating context `X_P(t)` | System demand, demand forecast, transmission outage/capacity status, reserves/operating stress, timing of grid-side disturbances | 1, 3, 4, 5 | ISO-scale data are not identical to local distribution outages and may require careful spatial interpretation |
| **A4** | **California EV charger data / CEC EV-CARR + DOE/NREL AFDC** | Direct P–T interface `Z_PT` | Charger location, ports, connector/power capability, operational/reliability status where public, charging-network topology, outage/unavailability signatures | 1, 2, 3, 5 | AFDC is strongest for station topology; CEC reliability reporting availability must be audited before assuming raw high-frequency public access |
| **A5** | **NOAA Storm Events Database + Event Footprint Catalog** | Disturbance `h(x,t)` and event `e_k` | Hazard type, onset/end, spatial footprint, intensity/severity, duration, path, event chronology | 2, 3 | Event Footprint Catalog currently has strongest high-resolution footprints for selected severe-storm hazards; coverage is not uniform across all hazard types |
| **A6** | **DOE-417 Electric Emergency Incident and Disturbance Reports** | Causal event labels, response/action evidence | Event start/end, reported cause, affected load/customers, event class, restoration timing and response/action information where available | 2, 4, 5 | Event reports are not a continuous operational time series and organizational fields may be incomplete or heterogeneous |

### A1. Caltrans PeMS — Transportation physical state and recovery

**Why it is essential:** It provides high-frequency, networked transportation observations rather than a single traffic counter. PeMS integrates detector measurements with incidents and lane closures, enabling explicit study of disruption propagation and recovery.

Primary variables/constructs to derive:

- `q_i(t)` = traffic flow,
- `v_i(t)` = speed,
- `o_i(t)` = occupancy,
- incident / closure indicators,
- travel-time or accessibility degradation,
- network congestion state,
- `t_T^fail`, `t_T^peak`, `t_T^rec`,
- `tau_T`, transport recovery duration,
- propagation lag between detector/segment states.

What the thesis is looking for:

`hazard/event -> transport disruption -> accessibility/travel-time loss -> recovery`

and, after alignment with power events:

`T disruption -> crew/accessibility proxy -> slower P recovery`

The final relation is a **hypothesis to test**, not an assumed fact.

Official source: https://dot.ca.gov/programs/traffic-operations/mpr/pems-source

### A2. ORNL EAGLE-I — Power outage and restoration trajectory

**Why it is essential:** The historic release provides county-level customers-without-power observations at 15-minute intervals, allowing direct reconstruction of outage and restoration trajectories.

Primary variables/constructs to derive:

- `N_out(c,t)` = customers without power,
- outage onset `t_P^fail`,
- maximum outage magnitude,
- time to peak,
- recovery start,
- restoration slope/rate,
- recovery completion `t_P^rec`,
- `tau_P`, `tau_R`,
- resilience/recovery curve features.

What the thesis is looking for:

`h(x,t) -> e_P -> X_P down -> restoration trajectory`

and after alignment with PeMS:

`T accessibility degradation -> change in P restoration rate / recovery time`

Official source: https://impact.ornl.gov/en/datasets/eagle-i-power-outage-data-2014-2022/

DOI: `10.13139/ORNLNCCS/1975202`

### A3. CAISO OASIS — Grid operating context

**Why it is essential:** EAGLE-I measures customer outage consequences; CAISO OASIS adds bulk-system operating context such as demand, transmission outages, capacity status, and market/system conditions.

Primary variables/constructs to derive:

- system demand and forecast error,
- transmission outage indicators,
- available capacity / transfer constraints where relevant,
- reserves / operating stress where available,
- temporal context surrounding major outage events.

What the thesis is looking for:

Whether observed customer outages and recovery occur during identifiable bulk-system stress or transmission outage conditions, without conflating transmission-system state with distribution-level outage state.

Official source: https://www.caiso.com/systems-applications/portals-applications/open-access-same-time-information-system-oasis

### A4. CEC EV-CARR + AFDC — Direct Power–Transportation interface

**Why it is essential:** EV charging infrastructure is one of the most direct observable physical interfaces between electricity and mobility.

Interface concept:

`P -> T : electricity availability -> charger availability / charging service -> mobility capability`

Potential reciprocal mechanisms to examine:

`T -> P : EV charging demand / mobile storage / V2G -> grid operating condition`

Primary variables/constructs to seek:

- station coordinates,
- number of charging ports,
- charger power rating,
- connector type,
- network/operator,
- charger status / uptime / downtime where publicly accessible,
- reason for downtime where available,
- temporal station additions/retirements,
- spatial relation to PeMS corridors and EAGLE-I outage counties.

Important evidence rule:

- **AFDC** can establish charging-station topology and historical/current infrastructure.
- **CEC reliability reporting** is a candidate source for high-frequency charger reliability; public availability and field completeness must be verified before it is used as dynamic `Z_PT(t)` evidence.

Official sources:
- https://afdc.energy.gov/data_download
- https://www.energy.ca.gov/programs-and-topics/programs/clean-transportation-program/zev-infrastructure-data-reporting/ev

### A5. NOAA — Hazard forcing and causal event timing

**Why it is essential:** The causal framework requires exogenous disturbances `h(x,t)` to be separated from endogenous cascade events.

Primary variables/constructs to derive:

- event type,
- start/end time,
- location / polygon footprint,
- intensity/severity,
- duration,
- path length where relevant,
- damage/event narrative when available.

What the thesis is looking for:

`h(x,t) -> e_i^(alpha)`

with explicit temporal precedence before testing any cross-layer propagation mechanism.

Official sources:
- https://www.ncei.noaa.gov/stormevents/
- https://www.ncei.noaa.gov/products/event-footprint-catalog

### A6. DOE-417 — Causal event and organizational response evidence

**Why it is essential:** DOE-417 can provide event chronology, reported causes, affected customers/load, and incident/restoration information that helps distinguish event mechanisms from correlations in sensor data.

Primary constructs to seek:

- reported event cause,
- event start/end,
- load/customers affected,
- assets/areas affected where reported,
- response/action/restoration information where available,
- event classification.

What the thesis is looking for:

`cause -> event -> physical consequence -> response/action -> restoration`

Evidence limitation:

DOE-417 is used as **event-level causal/response evidence**, not as a continuous measurement of organizational state `O(t)`.

Official source: https://doe417.energy.gov/

---

# 4. Tier B — Cross-infrastructure, information, and organizational support

| Priority | Dataset / database | Thesis use | What we are looking for | Canonical stages | Evidence status |
|---|---|---|---|---|---|
| **B1** | **FEMA TEMPO / POST** | Cross-infrastructure impact validation | Energy and transportation impact ranks in common spatial cells; compare simultaneous disruption footprints | 2, 3, 5 | Validation / impact layer, not raw physical state |
| **B2** | **OpenFEMA Public Assistance** | Organizational recovery / investment | Recovery projects, obligations, infrastructure repair/mitigation, long-term response and transformation evidence | 4, 6, 7 | Coarse organizational/policy evidence, not fast control dynamics |
| **B3** | **FCC Broadband Data Collection (BDC)** | Information-system structure | Fixed/mobile service availability, spatial communication accessibility, structural information-layer exposure | 1, 4 | Structural `I` proxy only; not disaster-time communication outage state |

### B1. FEMA TEMPO / POST — Cross-infrastructure validation

**Why it is useful:** FEMA TEMPO provides energy and transportation impact layers in a common spatial framework, including relative transportation impacts and energy impacts derived partly from outage information.

What the thesis is looking for:

- co-located energy and transportation impact cells,
- common event footprints,
- consistency with independently reconstructed EAGLE-I + PeMS disruption states,
- cross-validation of severe event periods.

Important rule:

TEMPO impact ranks are **derived relative impact indicators**. They must not replace the underlying physical variables `X_P` and `X_T` in the dynamic model.

Official source: https://gis.fema.gov/arcgis/rest/services/TEMPO/TEMPO/FeatureServer/layers

### B2. OpenFEMA Public Assistance — Organizational recovery and transformation

**Why it is useful:** It provides evidence about funded repair, replacement, mitigation, and recovery projects after disasters.

What the thesis is looking for:

- project type,
- affected infrastructure category,
- obligated amount / cost,
- repair vs replacement vs mitigation,
- disaster/event linkage,
- geographic location,
- long-term recovery/mitigation actions.

Use in the thesis:

- Stage 4: coarse evidence of organizational/resource response,
- Stage 6: translate recurring resilience weaknesses into investment requirements,
- Stage 7: identify technical/organizational/policy transformation pathways.

Do **not** infer minute-to-minute organizational decision dynamics from this database.

Official source: https://www.fema.gov/data-visualization/public-assistance-program-summary-obligations

### B3. FCC Broadband Data Collection — Information structure

**Why it is useful:** The information component `I` requires evidence on communications availability/capability. FCC BDC provides downloadable fixed and mobile broadband availability data.

What the thesis is looking for:

- spatial broadband/mobile coverage,
- service availability by geography,
- potential information-access vulnerability,
- overlap with critical P–T assets and disruption areas.

Correct interpretation:

`I_struct(x)` = structural communication availability / exposure proxy.

Incorrect interpretation:

`I(t)` = real-time disaster communication performance.

The latter requires a separate outage or operational source and must not be claimed from BDC alone.

Official source: https://help.bdc.fcc.gov/hc/en-us/articles/7682769466395-Broadband-Data-Collection-BDC-FAQs

---

# 5. Tier C — Sustainability transformation data and models

| Priority | Source | Role | What we are looking for | Canonical stages | Important distinction |
|---|---|---|---|---|---|
| **C1** | **EPA eGRID** | Electricity emissions and generation characteristics | Emission rates, generation, resource mix, plant/subregion environmental intensity | 6, 7 | Observational/compiled electricity environmental database |
| **C2** | **DOE / Argonne R&D GREET** | Life-cycle sustainability translation | Energy use, GHG, air pollutants, water use for energy/transport technologies and intervention alternatives | 6, 7 | A life-cycle assessment model, not a resilience observational dataset |

### C1. EPA eGRID — Electricity sustainability factors

What the thesis is looking for:

- `CO2e` / emission-rate factors,
- generation and resource mix,
- electricity environmental intensity by plant/subregion,
- environmental implications of backup generation, restoration energy, electrification, and grid-dependent mobility.

Transformation example:

`resilience intervention u -> change in electricity use / source -> Delta CO2e`

Official source: https://www.epa.gov/egrid

### C2. R&D GREET — Life-cycle transformation model

What the thesis is looking for:

- total energy consumption,
- renewable/non-renewable energy use,
- GHG emissions,
- air-pollutant emissions,
- water consumption,
- life-cycle comparison of alternative technical transformation pathways.

Transformation role:

`Resilience outputs -> Phi_sus -> sustainable transformation requirements`

GREET is deliberately kept **downstream of Stage 5**. It does not change the resilience dynamics in Stages 1–5.

Official source: https://www.energy.gov/cmei/rd-greet-life-cycle-assessment-model

---

# 6. Tier D — Controlled coupled-system benchmark for mathematical verification

## 47-node Transportation + modified IEEE 69-bus Distribution dataset

Repository:
https://github.com/ChrisZKZ/Data-for-47-node-transportation-system-and-69-node-distribution-system

Role:

- verify code and mathematical coupling before empirical fusion,
- test `G_P <-> G_T`, EV charging demand, and interface mappings under controlled conditions,
- perform sensitivity/robustness experiments on `Z`, `tau`, `F`, `J`, and control policies.

What the thesis is looking for:

- transportation-network distance/topology,
- 69-bus distribution data,
- EV charging demand,
- load profiles,
- charging-station planning variables,
- explicit power–transportation coupling assumptions.

**Strict evidence rule:** this is a benchmark / synthetic-or-study-specific test system. It may support **model verification and controlled experiments**, but it must not be presented as empirical validation of real infrastructure resilience.

---

# 7. Mapping datasets to the seven canonical stages

| Canonical stage | Primary evidence sources | Main empirical object |
|---|---|---|
| **1. Multilayer Structure** | PeMS, CAISO, AFDC/CEC, FCC BDC, benchmark system | `G_P`, `G_T`, `Z`, structural `I`; asset/interface topology |
| **2. Causal Mechanisms** | NOAA, DOE-417, PeMS incidents, EAGLE-I, CEC reliability if available | `h`, `e_k`, direction, mechanism, temporal precedence |
| **3. Coupled Hybrid Multiscale Dynamics** | EAGLE-I, PeMS, CAISO, charger status/reliability, benchmark system | `F`, `J`, `tau`, coupled trajectories, recovery dynamics |
| **4. Feedback & Control** | DOE-417, OpenFEMA, CAISO operational context, FCC structural information | response/action evidence, information availability, organizational/resource constraints |
| **5. Viability** | EAGLE-I + PeMS + CAISO + service thresholds | service survival, recovery, non-viable/viable trajectories under constraints |
| **6. Resilience-to-Sustainability Transformation Interface** | eGRID, GREET, OpenFEMA, CEC | emissions, energy, cost, resource, accessibility and adaptation requirements derived from resilience outputs |
| **7. Sustainable Transformation Pathways** | GREET, eGRID, OpenFEMA, CEC and scenario outputs | technical, organizational, environmental and policy transformation alternatives |

---

# 8. Multi-rate data-fusion rule — essential for Stage 3

The sources have different temporal and spatial resolutions. They must **not** be forced into a false common time series by indiscriminate interpolation.

Use asynchronous observation models:

`y_s(t_k) = H_s(Y(t_k)) + epsilon_s(t_k)`

where `s` identifies the data source and `H_s` maps the latent coupled state to the quantity actually observed by that source.

Recommended hierarchy:

- operational dynamic core: 5–15 min where available,
- hourly aggregation for robust cross-source alignment when necessary,
- event-level DOE-417/NOAA evidence retained at native event resolution,
- organizational recovery/project data retained at day/project/event scale,
- sustainability factors retained at their native annual/lifecycle scale.

This multi-rate structure is consistent with **Coupled Hybrid Multiscale Dynamics** and should be treated as a feature of the thesis, not as a preprocessing inconvenience.

---

# 9. Core quantities to estimate

## Power

- outage onset and magnitude,
- `tau_P`, `tau_R`,
- restoration curve and restoration rate,
- service threshold crossings,
- probability/time of recovery.

## Transportation

- congestion/disruption onset,
- speed/flow/occupancy loss,
- accessibility/travel-time increase,
- `tau_T`,
- recovery trajectory,
- closure/incident persistence.

## Cross-layer interfaces

Candidate `P -> T` signals:

- power outage -> charger unavailability,
- power outage -> traffic signal / electrified mobility impairment where data permit,
- grid stress -> charging service reduction.

Candidate `T -> P` signals:

- road/traffic disruption -> crew-access delay proxy,
- accessibility loss -> slower outage restoration,
- mobility/logistics disruption -> longer recovery time.

The thesis must **estimate/test** these mechanisms; they are not assumed simply because both systems are disrupted.

## Information

- structural communication availability,
- observability/data availability where measurable,
- delay/missingness indicators if operational sources can be obtained.

## Organization

- reported response actions,
- restoration decisions/timing where available,
- recovery project/resource allocation,
- event-level and long-term organizational capability indicators.

## Viability

Construct service variables and thresholds such as:

`S_P(t) >= S_P,min`

`S_T(t) >= S_T,min`

and evaluate whether trajectories remain/re-enter the admissible set `K` under disturbance and control.

## Sustainability transformation

From resilience outputs derive:

- energy requirement,
- emissions implication,
- cost/resource requirement,
- accessibility/equity concern,
- adaptation need,
- infrastructure investment priority.

These are **outputs of Stage 5 transformed into inputs for Stages 6–7**.

---

# 10. Causal-identification discipline

A cross-layer relationship is not accepted as a mechanism merely because two time series correlate.

For a candidate mechanism `A -> B`, require as far as data permit:

1. **Temporal precedence:** `A` changes before `B`.
2. **Spatial plausibility:** affected assets/areas can interact physically or operationally.
3. **Mechanistic pathway:** a defensible interface `z_ij^(alpha beta)` exists.
4. **Lag consistency:** estimated delay is physically plausible and repeatable across events.
5. **Confounder control:** weather, time-of-day, day-of-week, demand, planned outages/closures, and common-cause hazards are controlled where relevant.
6. **Counterfactual/baseline:** compare against matched non-event periods/locations or an appropriate model baseline.
7. **Robustness:** results survive alternative windows, thresholds, spatial aggregation, and missing-data treatments.
8. **Evidence hierarchy:** direct measurements > official event reports > derived indicators > structural proxies > assumptions.

---

# 11. Data acceptance criteria

A dataset enters the final thesis evidence stack only if it passes:

- **Provenance:** authoritative/publicly documented source or transparent academic benchmark.
- **Construct validity:** explicit mapping to `X_P`, `X_T`, `Z`, `I`, `O`, `h`, `u`, or sustainability transformation outputs.
- **Temporal metadata:** timestamps adequate for the claimed mechanism.
- **Spatial metadata:** location/geometry adequate for cross-source alignment.
- **Coverage:** sufficient events/periods for repeated testing, not a single anecdote unless used as a case illustration.
- **Missingness audit:** known gaps and coverage limitations documented.
- **Access/reproducibility:** download/API procedure can be documented and repeated.
- **Resolution honesty:** no claim at finer temporal/spatial resolution than the source supports.
- **No proxy inflation:** structural or administrative variables are not described as direct physical/organizational states unless justified.
- **No causal inflation:** correlation is not reported as interdependency mechanism without the causal-identification checks above.

---

# 12. Canonical acquisition order

## Phase 1 — Core physical dynamics

1. Caltrans PeMS
2. ORNL EAGLE-I
3. CAISO OASIS
4. NOAA Storm Events / Event Footprints

Goal:

`h -> X_T and h -> X_P`, then identify event windows with simultaneous P/T impacts.

## Phase 2 — Direct P–T interfaces

5. AFDC charging-station topology
6. CEC EV-CARR / public charger reliability outputs if accessible
7. Coupled 47-node/69-bus benchmark for controlled model verification

Goal:

Estimate or test candidate `Z_PT` and `Z_TP` mechanisms.

## Phase 3 — Information / organization / response

8. DOE-417
9. FEMA TEMPO / POST
10. OpenFEMA Public Assistance
11. FCC BDC

Goal:

Add event cause, response, recovery, information-availability, and organizational evidence without overstating their temporal resolution.

## Phase 4 — Sustainability translation

12. EPA eGRID
13. R&D GREET

Goal:

`Stage-5 resilience outputs -> Stage-6 sustainability transformation requirements -> Stage-7 pathways`.

---

# 13. Preferred primary empirical case

**Preferred jurisdiction:** California.

Reason:

- PeMS supplies dense transportation observations.
- CAISO OASIS supplies power-system operating context.
- EAGLE-I can supply county outage/recovery trajectories where coverage is available.
- CEC/AFDC supplies the EV charging interface.
- NOAA supplies hazards.
- federal DOE/FEMA/FCC sources add event, organizational, and information evidence.
- eGRID/GREET support the resilience-to-sustainability translation.

This choice is **data-driven**, not arbitrary. It should be retained only if the access/coverage audit confirms sufficient overlap across selected events.

---

# 14. Definition of a successful thesis data case

A candidate disaster/event becomes a high-value empirical case only if the following minimum chain can be reconstructed:

`hazard h(x,t)`
`-> P and/or T initiating event`
`-> measurable P/T state degradation`
`-> plausible cross-layer interface`
`-> measurable lag/timescale`
`-> response/recovery trajectory`
`-> viability consequence`
`-> resilience outputs`
`-> sustainability transformation requirements`

The strongest cases will support both directions:

`P -> T`

and

`T -> P`.

If only one direction is supported by data, the thesis must report only that direction rather than forcing bidirectional evidence.

---

# 15. Verification date and official source register

Public source availability/description verified online on **2026-09-09**.

Official sources:

- Caltrans PeMS: https://dot.ca.gov/programs/traffic-operations/mpr/pems-source
- ORNL EAGLE-I: https://impact.ornl.gov/en/datasets/eagle-i-power-outage-data-2014-2022/
- CAISO OASIS: https://www.caiso.com/systems-applications/portals-applications/open-access-same-time-information-system-oasis
- California EV-CARR / charger reporting: https://www.energy.ca.gov/programs-and-topics/programs/clean-transportation-program/zev-infrastructure-data-reporting/ev
- DOE/NREL AFDC: https://afdc.energy.gov/data_download
- NOAA Storm Events: https://www.ncei.noaa.gov/stormevents/
- NOAA Event Footprint Catalog: https://www.ncei.noaa.gov/products/event-footprint-catalog
- DOE-417: https://doe417.energy.gov/
- FEMA TEMPO: https://gis.fema.gov/arcgis/rest/services/TEMPO/TEMPO/FeatureServer/layers
- OpenFEMA Public Assistance: https://www.fema.gov/data-visualization/public-assistance-program-summary-obligations
- FCC BDC: https://help.bdc.fcc.gov/hc/en-us/articles/7682769466395-Broadband-Data-Collection-BDC-FAQs
- EPA eGRID: https://www.epa.gov/egrid
- DOE R&D GREET: https://www.energy.gov/cmei/rd-greet-life-cycle-assessment-model
- Coupled 47-node / 69-bus benchmark: https://github.com/ChrisZKZ/Data-for-47-node-transportation-system-and-69-node-distribution-system

## Governance rule

This file defines the **canonical data strategy**, not a claim that every listed source has already been downloaded or passed the final access/coverage audit. Dataset inclusion in final experiments requires the acceptance criteria in Section 11. Any replacement of the primary stack or change in interpretation must be documented as a new version rather than silently overwritten.
