# Thermal Interdependency, Energy Use and Mobility Service — 40-Component Priority Ranking V1

**Date:** 2026-10-10  
**Status:** PROVISIONAL 20+20 LITERATURE-INFORMED *RESEARCH PRIORITY*; **0 admitted hardware models**; G1 and G5 OPEN; G4 ablations NOT_RUN. 
**Governing scope:** Frozen GO/SO1-SO3 and canonical V5/V3 remain unchanged. Energy-use and energy-efficiency are declared **downstream sustainability/engineering indicators**, not a silent replacement for SO3 or a new general objective.

## 1. The precise decision question

Which **physically credible components**, when individually qualified and represented at the **minimum necessary mathematical fidelity**, can explain extreme-heat-conditioned changes in:
(a) transformer/feeder electrical input and thermal capability;
(b) grid-side AC energy delivered to EVSE versus charger delivered DC / battery accepted energy;
(c) charging by required deadline and actual mobility service when observed;
(d) heat and intervention effects on efficiency, emissions or costs if data support them?

Ranking addresses **expected scientific leverage**, NOT temperature magnitude, watts of heating, carbon savings, numerical efficiency or actual causal impact. Those outcomes cannot be inferred from published precedent alone.

## 2. Ranking criteria (non-compensatory)

1. G0 component taxonomy: actual equipment vs contained subassembly/instrument/control; prevent duplicate thermal states.
2. G1 reality: must exist in one compatible nameplate/topology/cooling/charging system.
3. G2 thermal phenomenon: heating/storage/rejection/derating supported by equipment-applicable physics.
4. G3 interface or service relevance: participates in testable directional P→T_e or T_e→P mechanism, or is essential to required service.
5. G4 incremental quantitative value: **leave-one-component-model-out** compared with a physically consistent algebraic/aggregate alternative changes independently assessed heat/critical time/energy/service QOIs beyond predeclared sensor/service uncertainties.
6. G5 validation feasibility: measured variables, identifiable parameters, independent reference/holdout, numerical conservation/uncertainty.

Order is a **qualitative expert-priority ordinal** informed by (i) relevance to frozen thermal interdependency and SO3 service, (ii) energy/mobile QOIs, (iii) physics/literature support, (iv) expected independent need. **No invented weighted score or fitted data.** High/Medium/Low are **ordinal screening opinions**, not physical measurements. '*' denotes conditional assumptions; even High labels are not physical admission. Instruments can be **mandatory for measurements** while ranked lower as independent *thermal model* components. Alternative case technologies are ranked low in the proposed oil-transformer/off-board-DC topology, not universally unimportant.

Method precedents: NRC (2008) [PIRT importance × knowledge ranking](https://www.nrc.gov/regulations-legislation/nureg-series-publications/publications-prepared-by-nrc-contractors/next-generation-nuclear-plant-phenomena-identification-and-ranking-tables-pirts-nuregcr-6944/v1); Villaverde (2019), [observability and identifiability](https://doi.org/10.1155/2019/8497093).

## 3. Power System — all 20 ranked

| Rank | Registry ID | Candidate (unchanged original label) | Thermal | Interface | Energy/mobility | Priority |
|---:|---|---|---|---|---|---|
| 1 | P02 | Oil-immersed distribution transformer | High | High* | High | **TOP4 PROVISIONAL** |
| 2 | P10 | Distribution feeder conductor/cable | High | High | High | **TOP4 PROVISIONAL** |
| 3 | P08 | Transformer protection/loading controller | Medium* | High* | High* | **TOP4 PROVISIONAL** |
| 4 | P05 | Transformer cooling assembly | High* | Medium* | Medium | **TOP4 PROVISIONAL** |
| 5 | P09 | Feeder head breaker | Medium* | High* | High* | BACKUP / SUPPORT |
| 6 | P04 | Tank/passive radiator | High | Medium | Medium | BACKUP / SUPPORT |
| 7 | P17 | AC power meter | Low | High | High | BACKUP / SUPPORT |
| 8 | P07 | Transformer thermal sensor | Low | Medium | Medium | BACKUP / SUPPORT |
| 9 | P13 | Distribution busbar/switchgear | Medium* | Medium | Medium | BACKUP / SUPPORT |
| 10 | P06 | Bushings/terminals | Medium* | Medium | Low | LOWER FOR THIS CASE |
| 11 | P11 | Cable termination | Medium* | Medium | Low | LOWER FOR THIS CASE |
| 12 | P12 | Cable splice/line joint | Medium* | Medium | Low | LOWER FOR THIS CASE |
| 13 | P15 | Voltage regulator | Medium* | Medium | Medium | LOWER FOR THIS CASE |
| 14 | P14 | Pole-mounted recloser | Medium* | Medium | Medium* | LOWER FOR THIS CASE |
| 15 | P18 | SCADA/RTU hardware | Low | Medium | Medium | LOWER FOR THIS CASE |
| 16 | P01 | Upstream supply terminal | Low | High | Medium | LOWER FOR THIS CASE |
| 17 | P03 | Dry-type transformer | High* | High* | High* | ALTERNATIVE |
| 18 | P16 | Capacitor bank | Low | Medium | Low | LOWER FOR THIS CASE |
| 19 | P19 | DER inverter | High* | Medium* | Medium* | LOWER FOR THIS CASE |
| 20 | P20 | Grid battery inverter | High* | Medium* | Medium* | LOWER FOR THIS CASE |

Top four justification:
- **P02 transformer:** physically necessary losses/thermal memory, EV load effects and conditional operating capability (Hilshey et al. 2013, https://doi.org/10.1109/TSG.2012.2217385).
- **P10 feeder:** real electrical transfer and loss/thermal rating, where needed; Pan et al. (2025), https://doi.org/10.1049/hve2.70024. Thermal ODE NOT necessarily required.
- **P08 protection/loading controller:** strongest **missing** P thermal→actual permissible AC transfer link. ABB manual provides manufacturer functionality precedent, not proof controller actually curtails/trips at selected site: https://library.e.abb.com/public/e5e9f20ae5454e14a5572a13ec67e88a/RET615ANSI_appl_201230_ENb.pdf. An abstract *operating rule* does not count as a fourth physical device: demand hardware identity; if absent promote P09 only with proven relay-to-breaker thermal action.
- **P05 cooling assembly:** heat rejection/temperature response; Li et al. (2024) demonstrate 110 kV ONAF thermofluid validation: https://doi.org/10.1049/hve2.12345. Selected transformer might instead be ONAN, in which case integrate passive cooling into P02 and replace P05 only when the alternative independently qualifies.

## 4. Electrified Transportation — all 20 ranked

| Rank | Registry ID | Candidate (unchanged original label) | Thermal | Interface | Energy/mobility | Priority |
|---:|---|---|---|---|---|---|
| 1 | T01 | Off-board DC EVSE converter | High | High* | High | **TOP4 PROVISIONAL** |
| 2 | T11 | Vehicle battery pack | High* | High | High | **TOP4 PROVISIONAL** |
| 3 | T04 | EVSE cooling system | High* | Medium* | High | **TOP4 PROVISIONAL** |
| 4 | T17 | Vehicle HVAC compressor | Medium | Medium* | High | **TOP4 PROVISIONAL** |
| 5 | T08 | DC charging cable | High* | Medium* | Medium* | BACKUP / SUPPORT |
| 6 | T09 | Charging connector/contact | High* | Medium* | Medium* | BACKUP / SUPPORT |
| 7 | T12 | Battery management ECU | Low | Medium* | High | BACKUP / SUPPORT |
| 8 | T13 | Battery cooling circuit | High* | Low | Medium | BACKUP / SUPPORT |
| 9 | T07 | EVSE AC meter | Low | High | High | BACKUP / SUPPORT |
| 10 | T06 | EVSE rectifier T sensor | Low | Medium | Medium | LOWER FOR THIS CASE |
| 11 | T05 | EVSE cabinet/ventilation | Medium | Medium | Medium | LOWER FOR THIS CASE |
| 12 | T03 | EVSE DC output module | High* | Medium | Medium | LOWER FOR THIS CASE |
| 13 | T10 | Vehicle charging inlet | Medium* | Medium* | Medium | LOWER FOR THIS CASE |
| 14 | T02 | EVSE input contactor/filter | Medium | Medium | Medium | LOWER FOR THIS CASE |
| 15 | T15 | Traction inverter | High* | Low | Medium | LOWER FOR THIS CASE |
| 16 | T16 | Traction motor | High* | Low | Medium | LOWER FOR THIS CASE |
| 17 | T20 | Charging communications controller | Low | Medium | High | LOWER FOR THIS CASE |
| 18 | T19 | Vehicle DC-DC converter | Medium | Low | Low | LOWER FOR THIS CASE |
| 19 | T18 | Cabin HVAC blower | Low | Low | Medium | LOWER FOR THIS CASE |
| 20 | T14 | Onboard AC charger | High* | Medium* | Medium | ALTERNATIVE |

Top four justification:
- **T01 EVSE converter:** direct temperature-dependent charger derating and AC/DC losses (Krama et al. 2026, https://doi.org/10.1016/j.ecmx.2026.101960), but site-specific AC-input transfer still OPEN.
- **T11 battery pack:** accepted terminal energy, SOC and real departure energy requirement. A battery thermal model is conditional (Bernardi et al. 1985, https://doi.org/10.1149/1.2113792).
- **T04 EVSE cooling:** heat rejection, thermal limitations and auxiliary energy; standalone cooling dynamics require separate installed actuators, timestamps and materiality (Krama et al. 2026).
- **T17 vehicle HVAC compressor:** upgraded relative to earlier connector/cable portfolio **only for explicitly requested energy-use/mobility QOIs**. Parker et al. (2025) measured **vehicle-level auxiliary-energy** response to heat (https://doi.org/10.1016/j.apenergy.2024.125051). It does **not** independently measure this particular compressor's power, so component-specific isolation, route data and charging-demand timing remain OPEN. If the bounded application models only station charging with supplied departure kWh, treat HVAC as external temperature-dependent demand input and test **T08 cable** as the fourth physical component instead.

**Alternatives:** T08 charging cable model thermal temperature-rise evidence (Zhang et al. 2023, https://doi.org/10.1080/10407782.2023.2285374), but no case-specific binding current limit. T09 charging connector/contact also conditional. T12 BMS charge acceptance is required as a control constraint, not necessarily a separate temperature state or hardware subsystem. Ranking differs from the earlier 4+4 inventory **deliberately and transparently**, it is not a retroactive source edit.

## 5. Quantities of interest / measurement chain

- **Heat and state:** verified equipment T(t), heat loss/rejection, actual control setting, temperature limit crossing `t_C` only if documented.
- **Energy:** feeder/transformer losses [kWh]; EVSE AC real input [kWh]; offered/delivered DC power/energy [kW/kWh]; accepted battery terminal energy [kWh]; auxiliary/HVAC/cooling energy [kWh]; total service basis.
- **Mobility service:** required vs accepted kWh by departure timestamp; fraction of vehicles ready on time; *actual* completed km/trips ONLY if observed or defensible route evidence exists.
- **Efficiency:** `useful defined mobility service / matched electrical energy input` **after** specifying numerator, denominator, boundary, time and functional unit. Do not simply equate charger efficiency with transport system efficiency.
- **Resilience:** electricity service and mobility service deficit/degradation/recovery from time trajectories; temperature or energy efficiency alone ≠ resilience.

Mathematical architecture, when admitted: transformer/converter thermal ODEs **where observed and needed**, algebraic AC interface and loss balance; battery energy state; HVAC energy demand map conditional; switches/cooling modes only when implemented. Never impose eight thermal ODEs. M0 independent controlled counterfactual, M1 qualified algebraic, M2 *directionally qualified dynamic causal* only. Physical effect and site-specific measured causal validation remain OPEN.

## 6. Sustainability and SDGs — derived from evidence, not selection scores

**Pathway 1:** direct heat/thermal-interdependency consequences (matched baseline vs heat-only). **Pathway 2:** added documented engineering-response consequences (heat + Improve/Adapt/Restore vs matched heat-only). Compare loss kWh, charger/cooling/HVAC input, service, justified GHG/cost/equity data under identical boundaries and conventions. Improving resilience can increase energy use or material burdens.

Potential *thematic* SDG 7.3 (energy efficiency), 9.4 (resource-efficient infrastructure), 11.2 (transport access), 13.1/13.2 (climate resilience/mitigation governance) links need a measured-indicator-to-exact-target rationale. Local kWh/km or charging readiness **are not** official 7.3.1 GDP energy intensity or 11.2.1 public transport access. See official UN: https://unstats.un.org/sdgs/metadata/.

## 7. Permanent provenance and next action

The IDs here match the **20+20 local physical candidate register** (P02 transformer; T01 EVSE). The independently created V2 literature matrix used **a conflicting 19+21 reconstruction** (P13 transformer; T18 EVSE). These are different identifier schemes, not evidence that an item changed physical identity. **Resolve the master 40 G0 taxonomy / aliases before freezing official thesis component IDs.** Do not treat the exact count as a physically necessary invariant.

**Research campaign:** select one compatible real transformer-feeder-DC EVSE-vehicle case; obtain actual thermal restriction/controller and synchronized AC-port, DC-port, temperature and energy/departure logs; assess compressor versus cable need by selected energy/mobility QOIs; preregister materiality and measurement-error tolerances; run component exclusion and M0/M1/M2 as allowed; promote no component to admitted until G0–G5 pass.

**Current result: 40 screened / 8 research priorities / 0 fully equipment-validated, 0 ablation tests completed.**
