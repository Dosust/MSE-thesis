# 40-to-8: Literature Qualification and Resilience–Sustainability–SDG Traceability V1

**Date:** 2026-10-10  
**Status:** WORKING / LITERATURE-QUALIFIED CONCEPTS ONLY; NO 4+4 EQUIPMENT PORTFOLIO ADMITTED; ORIGINAL 40 COMPONENT IDENTITIES NOT RECONCILED; NO CASE-SPECIFIC NUMERICAL LAWS OR VALIDATION RESULTS.  
**Source review depth:** Selected primary publisher abstracts / full open publisher pages, one official protection manual and official UN SDG target definitions; NOT exhaustive systematic review; article paywall limitations expressly retained.
**Purpose:** Test the scientific reasons to retain, aggregate or replace **four Power and four Electrified Transportation component candidates** before building mathematical models. Physics/thermal engineering and state-time/service consequences govern selection. Resilience, two-pathway sustainability and SDG relevance are downstream outputs, NOT selection justification by thematic resemblance.

Governing:
- [Reality-first 40-to-8 protocol](../DOSSIYA_REALITY_FIRST_40_TO_8_COMPONENT_SELECTION_PROTOCOL_V1.md)
- [Provisional 40-row CSV and gate status](40_TO_8_COMPONENT_SELECTION_MATRIX_PROVISIONAL_V1.csv)
- [Provisional 4+4 portfolio and eight ablation specifications](40_TO_8_PHYSICAL_COMPONENT_SELECTION_MATRIX_PROVISIONAL_V1.md)
- [Frozen objectives](../CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md)
- [Canonical two-pathway sustainability assessment](../CANONICAL_SUSTAINABILITY_TWO_PATHWAY_ASSESSMENT_V1.md)
- [Preferred proposed V6; not canonical](../CONCEPTUAL_FRAMEWORK_V6_PROPOSED_EVIDENCE_GATED_THERMAL.md)

## A. What a paper can and cannot validate

A published **model family** or verified experiment may establish physics, observables and candidate methods; it does not automatically qualify the **exact selected equipment** or transfer its parameters, operating policy, limits or effects. A review supports mechanism screening, NOT primary validation. An equipment manufacturer manual describes **available or configuration-dependent** controller functions, NOT evidence the relay actually tripped in our future installation.

Use four literature gates before interpreting G0–G5:
1. **L1 Physics:** a source specifies actual heat generation/storage/rejection or a verified thermal-control mechanism for relevant equipment type.
2. **L2 Mathematics:** reproducible conservation/constitutive/control model or directly documented capability function, with variables, boundary, operating assumptions.
3. **L3 Observability:** identify what was *actually* measured vs simulated; name needed temperature/current/power/switching signals. Synthetic benchmarks are not synchronized field data.
4. **L4 Transfer + service:** establish equipment/scale/technology compatibility, and a testable link to electricity or mobility service. Without a transfer match: CONDITIONAL.
5. **L5 Necessity:** after assembling a compatible case, remove the component's independent model block and compare preregistered state-time, service QOIs with valid measurements; no numerical ablation has been run.

**Distinguish component selection from model states:** 4+4 physical blocks are not 8 ODE states; a physical component can be represented by algebraic constraints and an internally mounted cooling device may not justify a separate block.

## B. Four Power candidates — literature judgment

| Proposed physical block | Primary evidence: method/findings and depth | Useful physics/mathematics and data | L1/L2/L3 preliminary verdict | Keep or challenge |
|---|---|---|---|---|
| **P13 Oil-immersed transformer, integrated assembly** | **Hilshey et al. (2013)** simulated oil-transformer oil/winding/hotspot thermal response, temperature-dependent insulation aging, Monte Carlo EV charging; actual utility protection not tested. **Pan et al. (2025)** uses transient top-oil/hotspot + dynamic thermal rating in EV/grid planning. [Hilshey](https://doi.org/10.1109/TSG.2012.2217385); [Pan](https://doi.org/10.1049/hve2.70024). Publisher/full primary sources available. | Candidate top-oil/hotspot ODEs; load losses, heat storage, cooling and weather. Hilshey NHTS and historical ambient are mixed observed/simulated inputs; actual transformer type/parameters/thermometers absent. | **STRONG model-family support / CASE OPEN** | **Retain focal P component** if installed transformer compatible; dry-type P11 is a different model family, not an additional simultaneous block. Aging output ≠ measured interruption. |
| **P14 Distribution feeder (choose underground cable P09 OR overhead conductor P08)** | **Marshall et al. (2013)** numerical transient heat transfer around three underground cables driven by survey-derived EV loads; effects on simulated cable temperatures/degradation. **Pan et al. (2025)** models dynamic thermal ratings of cables/transformers. [Marshall](https://doi.org/10.1016/j.epsr.2012.12.006) (publisher abstract/sections); [Pan](https://doi.org/10.1049/hve2.70024) (open paper). | AC Kirchhoff/power flow, Joule losses; buried cable heat diffusion if necessary; weather/soil needed. Published cable heat predictions ≠ case-matched measured feeder failure. | **STRONG physics, CONDITIONAL detailed thermal states / CASE OPEN** | Retain electrical transfer; test reduced algebraic feeder versus separate heat equation. One actual feeder technology and length/rating required. |
| **P15 Circuit breaker (actual physical switch, NOT automatic thermal-coupling mechanism)** | **ABB RET615 protection manual** explicitly indicates thermal-overload 49T alarm/operation function exists but **is not configured by default to trip circuit breaker** in the referenced configuration. [ABB manual](https://library.e.abb.com/public/e5e9f20ae5454e14a5572a13ec67e88a/RET615ANSI_appl_201230_ENb.pdf). Manufacturer manual, NOT peer-reviewed experimental evidence. | Actual switch position, protection action logs and electrical availability; relay thermal logic may be algebraic/hybrid; hot transformer alone does not certify a trip. Device settings unknown. | **THERMAL ACTION FOR SELECTED SITE NOT QUALIFIED** | **Challenge** as mandatory fourth independent block. Include breaker logic only if actual state→relay/operator→switch/supply action exists. Could be present hardware but still no temperature-triggered role. |
| **P06 Transformer cooling device (if independently controllable/observable)** | **Li et al. (2024)** validated oil-natural/air-forced transformer thermofluidic predictions in temperature-rise tests; geometry and oil circulation affect cooling, but this is not evidence an independent cooling-state module is needed in a reduced EV/transformer case. [Li](https://doi.org/10.1049/hve2.12345) (open publisher abstract). | Heat-rejection law (Q_{cool}) and cooling mode; oil/ambient/radiator/fan status, time. No compatible device cooling telemetry supplied. | **THERMAL PHYSICS SUPPORTED, SEPARATE BLOCK CONDITIONAL** | **Challenge**: test integrated transformer cooling parameter versus separate fan/pump block. Never count a passive radiator as a second independently necessary device solely to satisfy 4 P. |

## C. Four Electrified Transportation candidates — literature judgment

| Proposed physical block | Primary evidence: method/findings and depth | Useful physics/mathematics and data | L1/L2/L3 preliminary verdict | Keep or challenge |
|---|---|---|---|---|
| **T18 DC EV charging equipment (integrated)** | **Krama et al. (2026)** physically measured an air-cooled DC fast charger in Qatar: ambient/rectifier temperature, offered and delivered DC power, AC electrical indicators, conversion efficiency and charging outcomes; strongest direct extreme-heat derating support, but its case is NOT our installation. [Krama](https://doi.org/10.1016/j.ecmx.2026.101960) (publisher full/abstract; raw data on request). | AC/DC energy balance (P_{AC}=P_{DC}+P_{loss}) for matching control volume; candidate empirical derating (C_E) tied to measured variable only; NO inferred general junction equation. Need synchronized measured P,Q at AC port under derating. | **STRONG measured mechanism / TRANSFER OPEN** | **Retain focal T_e component**, with a named compatible model, conversion boundaries and actual thermal-capability curve. |
| **T05 EVSE active cooling device (if physically distinct)** | **Krama et al. (2026)** documents charger heat limitation; **IEEE Access 2024 power-electronics thermal-management review** catalogs active/passive cooling and active thermal control, but is a review, not validation for a specific EVSE fan/pump. [IEEE Access review](https://doi.org/10.1109/ACCESS.2024.3385429). | Lumped or resolved heat balance and cooling state only if temperature, airflow/pump/fan command and auxiliaries independently measured. Specific cooler absent. | **MECHANISM SUPPORTED GENERALLY / CASE + SEPARATE BLOCK OPEN** | **Challenge**: use EVSE aggregate cooling/derating if separate cooler supplies no uniquely necessary service QOI. |
| **T08 Physical DC charging cable (distinguish connector T09)** | **Zhang et al. (2023)** proposed/evaluated a cable equivalent thermal circuit with measured temperature-rise comparison; **Liang et al. (2025)** experimentally checked connector CFD then simulated contact resistance/current/ambient effects and trained an LSTM. [Cable](https://doi.org/10.1080/10407782.2023.2285374) (abstract accessible), [connector](https://doi.org/10.1016/j.ijthermalsci.2025.110139) (abstract/sections accessible). | (I^2R) heat and thermal RC; actual cable or connector thermal limit and enforced current-decrease command required to link to delivered vehicle energy. Published heating ≠ our installation current limiting. | **GOOD LOCAL HEAT PHYSICS / SERVICE LIMIT CONDITIONAL** | **Conditional**; include thermal ODE if connection actually limits charging; otherwise assign a rated current constraint and eliminate separate thermal state. T08 vs T09 needs a device-level test. |
| **T12 Traction battery pack with BMS acceptance as an operating rule** | **Bernardi et al. (1985)** energy balance, and **Thakur et al. (2023)** review of fast-charging battery thermal management show heat generation/cooling relevance; **Waldmann et al. (2017)** analyzes fast-charge thermal considerations. [Bernardi](https://doi.org/10.1149/1.2113792), [Thakur review](https://doi.org/10.1016/j.applthermaleng.2023.120303), [fast-charge thermal paper](https://doi.org/10.1016/j.jpowsour.2017.07.009). Reviews are NOT device-specific validation. | Stored-energy balance (dot E_B=P_{battery}) with battery-terminal boundary; (P_{battery}le C_B(T_B,SOC,...)) only when supported by vehicle/BMS evidence. Need pack temperatures, SOC, accepted charge current, vehicle deadline. | **STRONG PHYSICS / BMS LAW + OBSERVATIONS OPEN** | **Retain energy/service-relevant physical pack**. Start energy-only; add thermal state only if case data show pack temperature affects acceptance/required service. DO NOT treat charging readiness as observed transport trips. |

## D. Alternative competition — essential for a four-per-sector decision

- **P15 vs P16/P07:** Physical breaker versus thermal relay/operator rule. The breaker might physically exist, but the thermal rule may be mere configuration. If no actual temperature-driven switching, do not count the breaker as a distinct thermal mechanism.
- **P06 vs integrated P13:** Additional fan/radiator dynamic state only if separately observable and alters temperature, loading or recovery outputs.
- **P14 (P08 vs P09):** An overhead line uses weather/solar/wind-dependent conductor physics; a buried cable uses soil/insulation conduction physics. Choose one before writing thermal equations.
- **T05 vs integrated T18:** Avoid counting a device and its indispensable internal cooler as separate *independently necessary models* unless data and leave-one-out tests warrant it.
- **T08 vs T09:** Charging cable bulk resistance and connector contact resistance may produce different thermal limits. Select whichever actually limits current; not both by default.
- **T12 vs T19/T14:** A battery pack is physically necessary for stored energy; BMS is operating logic and cooling module is internal device. Do not count them as extra unless independently modeled and necessary.
- **Unmodeled alternates:** Vehicle HVAC, traction electric drive and vehicle-side inlet are in the canonical full T_e scope, but only enter active case if actual demand/service consequence requires them.

## E. How mathematics, physics and thermal engineering connect to resilience and sustainability

This is the **one admissible reasoning chain**, NOT five independent reasons to add components:

1. **Physics**: observed electrical loading/cooling/heat (	o) evidence-qualified temperature or energy state.
2. **Mathematics**: minimum state ODE/DAE and algebraic AC/DC interface; manufacturer/operator thermal-capability curves only for compatible device.
3. **Thermal engineering**: qualified temperature-to-current/power constraints, cooling and, if implemented, protection actions.
4. **Electricity/mobility services**: actual supplied power and time-window energy, delivered versus required; readiness is a proxy unless trips measured.
5. **Resilience**: compare maintaining or recovering required electricity/mobility services through time, baseline and matched Improve/Adapt/Restore reruns.
6. **Sustainability Pathway 1**: direct thermal-interdependency service-related electricity losses/emissions (if justified factor), economic costs, access/continuity; each with units, baseline and horizon.
7. **Sustainability Pathway 2**: matched response-versus-no-response changes in those same measurable indicators, including intervention cooling energy/material/maintenance costs.
8. **SDG relevance ONLY after indicators:** UN **SDG 7 target 7.1** (reliable modern energy access), **SDG 9 target 9.1** (resilient infrastructure), **SDG 11 target 11.2** (accessible transport) may be thematically relevant, but the official indicators 7.1.1 (population with electricity access), 9.1.2 (passenger/freight volume), and 11.2.1 (access to public transport) are NOT equivalent to our local transformer charging kWh or EV ready-departure proxy. Exact SDG indicator alignment is currently **NOT_YET_MEASURABLE**. Do not call local converter efficiency official SDG 7.3.1 (primary-energy intensity per GDP). UN authorities: https://sdgs.un.org/goals/goal7 ; https://sdgs.un.org/goals/goal9 ; https://sdgs.un.org/goals/goal11 .

## F. Proposed literature decision (not physical validation)

| Decision class | Candidate blocks | Reason |
|---|---|---|
| **Strongest literature case for inclusion as physical assemblies** | **P13 transformer; T18 DC charger** | Closest published temperature-dependent behavior directly linked to EV charging and AC power demand |
| **Strong necessity for the service/transfer boundary, but maybe only reduced model** | **P14 feeder; T12 battery pack** | Electrical-transfer constraint and stored-energy/departure readiness |
| **Do not automatically count as separate physical/dynamic models** | P06 transformer cooler; P15 breaker; T05 charger cooler; T08 charging cable | Require case-specific identity, implemented action, measurement and ablation proof; connector T09 may replace T08 if contact heating dominates |

**Literature evidence cannot by itself approve eight components.** The correct scientific conclusion is **four equipment/system roles are strongly motivated**, while the exact remaining 2+2 independently necessary blocks are OPEN. If a physically documented 4+4 installation has no independent cooler/switch/cable dynamics, prefer a **smaller model** while retaining the requested 4+4 as a screened case-inventory target rather than inventing eight dynamical subsystems.

## G. Next actual evidence-gated research actions

1. Recover and reconcile original 40 candidate component identities separately from the 29 thermal-limit checks and 11 reconstructed entries.
2. Identify a feasible equipment case with compatible transformer kVA, feeder, EVSE AC demand, charger topology and battery type.
3. Obtain the following physical data: transformer top-oil/hotspot and loading; actual power-limit/relay trip action; EVSE rectifier/cabinet temperature and AC P/Q input, DC power output and cooling response; connector current/temperature if limited; battery accepted energy/SOC and battery operating envelope.
4. Reconstruct cited paper equations **verbatim from full paper** before importing coefficients; standards clause / version read remains open; numerical parameters must be certified to case.
5. Predeclare G5 exclusions and retained QOIs; run matched independent-condition/no-coupling (M0), algebraic (M1), and only qualified dynamic-coupling (M2), numerical verification, held-out observational validation/UQ. No numerical tests or physical validation performed in this literature note.

**Frozen governance:** General Objective + SO1–SO3, Conceptual V5 and Mathematical V3 unchanged; V6 preferred provisional only. No eighth-component admission or verified causal propagation claim is made.
