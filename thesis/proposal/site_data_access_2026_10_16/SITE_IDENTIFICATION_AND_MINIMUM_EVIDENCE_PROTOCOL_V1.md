# Site Identification and Evidence Agreement — Working Protocol V1

**Thesis:** Engineering of Power–Electrified Transportation Interdependencies for Resilience  
**Focus:** Thermal Power System (P) ↔ Electrified Transportation (Tₑ) interdependencies during extreme heat  
**16 October 2026 · STATUS: CANDIDATE SITE SCREENING; NO PHYSICAL SITE SELECTED OR VERIFIED; NO AGREEMENT SIGNED.**  
**Authority:** Canonical V3 title; frozen thermal-only scope; GO + SO1–SO3; prior [physical interface feasibility](../physical_interface_feasibility_2026_10_16/).  
**Approval:** Institution/utility/site/operator approval and safe operation are separate from this academic document. No active field testing or instrument installation is authorized by the protocol.

## Immediate decision contract

**F0 site identity** is PASSED only with: (a) real site and consenting organization/contact, (b) known upstream transformer/feeding arrangement supported by an authorized as-built single-line/supply statement, (c) EVSE make/model/ratings and charger-to-transformer supply mapping, and (d) authority to use at least a sufficiently detailed, non-sensitive inventory. A public map pin or advertised charger name without supply connectivity is insufficient. The transformer ID or site identifiers may be withheld from public research outputs; private custody is acceptable with reproducible pseudonyms and access control.

**F3 observations** is PASSED at a declared **data-quality tier**, not a binary claim of causality. Minimum: lawful read-only time-series access, original clock/units/uncertainty metadata, measurement location, cooling/controller status where relevant, independently identifiable EVSE AC power and Power-side loading, observed thermal state(s), and enough temporal coverage to test the proposed time constants and heat episodes. For experimental directional coupling, P/Tₑ devices must be physically related at the same site and the **temperature-conditioned operating action plus receiving response** supported, not only two temperatures correlated with ambient.

**F7 services** is PASSED for each specific service independently. Electricity-service definition requires a stated requested level and a measurable delivered/curtailed quantity at a defined delivery boundary; mobility service requires an independently specified vehicle/fleet trip/departure or transport obligation and whether the available energy satisfies it. **Session duration and DC charging energy alone are service proxies, not evidence of actual mobility fulfillment.**

### Evidence tiers — what may be claimed

| Tier | Minimum verifiable records | Scientifically admissible claim | Not admissible |
| --- | --- | --- | --- |
| S0 — desk only | Public station listing and published papers | Plausible case category and prior-art mechanism | Verified power transformer/charger topology or validated model |
| S1 — identified case | Written operator permission + documented transformer→charger circuit/asset mapping | Real physical case and data-access readiness | Directional thermal effect based on topology alone |
| S2 — separate component observations | Actual permissible P or Tₑ sensors, provenance, clocks, useful variation and calibration | Observed individual component thermal responses | Joint field P↔Tₑ causality without coupled observations |
| S3 — matched paired observations | Same-site physically mapped P & Tₑ original traces, synchronized ambient/ports/cooling/controls/loads; independently witnessed thermal action and receiving state | Testable, qualified *candidate* directional coupling; measured receiving change subject to confounder tests | Causal proof from time order alone |
| S4 — qualified validation | S3 + admissible constitutive state/parameter model, independence of held-out episodes, confounder/negative control analysis, uncertainty, actual service requirements | Bounded validated directional and service claims according to results | Universal guarantee/generalization to unevaluated sites |

S4 cannot be conferred based on an accuracy score alone. Each direction receives its own evidence tier. A model calibrated on one site/temperature range cannot claim cross-site/extreme-condition transfer without an independent domain test.

## Screening protocol for physical-case candidates

Do not automatically prefer public DC fast charging. Screen (A) public DC fast charging and (B) fleet/depot charging on the *same noncompensatory gates*:

1. **Actual topology:** named consenting operator and verified transformer/EVSE electrical connection or map-to-record access.
2. **P thermal action feasibility:** transformer thermal sensor or validated measured temperature proxy AND possibility to document real derating, rating/protection/operator operating action; without action P→Tₑ field claim is unsupported.
3. **Tₑ thermal response feasibility:** EVSE internal temperature, thermal limitation/controller flag and commanded/actual power, plus AC-side current/real power.
4. **Receivers and confounders:** non-EV load, grid voltage/other curtailment, vehicle SOC taper, cooling action, common ambient heat and clock uncertainty.
5. **Services:** electricity delivered against requirement; BEV departure energy or actual vehicle/fleet demand/mission requirement.
6. **Data permissions:** written rights to inspect/calculate/publish anonymized aggregates, raw storage restrictions and relevant ethics/commercial approvals.
7. **Temporal/thermal excitation:** hot-condition variation and independent evaluation events where physically observed; do not create artificial electrical/thermal stress.

A site is **S1** only after 1 and 6. It may support Tₑ→P but not P→Tₑ; these gates are **independent**. Record `NO ACCESS` or `UNKNOWN`, never fabricate sample sizes. Use read-only authorized telemetry; actual instrument installation, electrical modifications or safety testing remain solely in qualified operator control, outside this protocol.

## Minimum source/receiving requirements

### P→Tₑ field claim
- Source: P equipment thermal state **with exact sensor meaning** (lid vs oil vs verified winding proxy).
- Source activation: real equipment-specific thermal restriction (manufacturer/operator/verified dispatch/protection), with logged event/change and compatible limit; merely high oil temperature is not enough.
- Interface: logged supply/available AC power and EVSE AC/DC setpoints/power at same site.
- Receiver: observable charger charging capability and required electricity/mobility service, while controlling common ambient heat, nonthermal grid limits and vehicle taper.
- Alternative: if no real P-side thermal action exists, report `P2T_UNOBSERVED` and consider only clearly *simulated* thermal restriction sensitivity.

### Tₑ→P field claim
- Source: EVSE thermal sensor plus verified heat-derating flag or equivalent identified limit (separate from vehicle BMS demand/SOC and grid commands).
- Interface: actual synchronized AC real/reactive power and current change at EVSE plus transformer/feeder allocation.
- Receiver: subsequent change in *measured or independently validated* P thermal state, with non-EV load and ambient controls.
- Competing effect: heat-triggered derating might temporarily **reduce** upstream transformer heating and later shift demand/rebound; effect direction is not assumed.
- Alternative: if transformer physical thermal response is not observable, claim `T2P_COMPONENT_OBSERVED_INTERFACE_SIMULATED`, not field causal identification.

### Electricity / mobility semantics
- Charging capability (kW), delivered electrical energy (kWh), charging duration (min), BEV SOC (%) and vehicle readiness are distinct quantities.
- Service requirements (Q_P^{req},Q_T^{req}) must come from a real operator/mission or explicitly registered bounded operational requirement, never selected post hoc.
- Define source, requirement, temporal tolerance, missingness and uncertainty before computing threshold exceedance or recovery.
- Observed heat at P and Tₑ may be **common forcing**. Temporal lag ≠ causal propagation.

## Data request and storage discipline

Ask for **metadata first**: asset/port topology, available channel inventory, typical observation window, sensor placements, per-channel sample interval and clock, events/controls available, and privacy/permission process. Request a permitted de-identified *read-only small sample* only after the operator consents. No site credentials, passwords, protected single-line diagrams, personally identifying vehicle traces, sensitive grid/security layouts, or raw confidential files belong in this public GitHub repository.

Raw files if obtained must remain in an approved secure location under owner agreement; GitHub should store only non-sensitive metadata, schema, pseudonymized provenance/checksums if permitted, and derived release-safe methods/results. Datasets from unrelated facilities cannot be concatenated as a fictitious instrumented P↔Tₑ event.

## Minimum evidence agreement decision — for advisor to decide, not pre-approved

**Track A: full field coupling:** Required = at least S3 observations for one specified direction and appropriate S4 testing for validated conclusions, plus electricity and mobility-service requirements if claiming measured resilience. Both directions may independently fail qualification.

**Track B: restricted component + co-simulation:** Required = authentic independently tested component sensor datasets and verified physics, but cross-system interface outcomes and resilience consequences expressly **simulation-only**; source uncertainty/transfer limitations declared. The advisor must confirm in writing whether such a restricted thesis satisfies SO2 and SO3's intended evidentiary standard and decide any needed scope/result qualification.

**Track C: no defensible outcome:** If neither real site/evidence nor justified component model exists, remain `BLOCKED_EVIDENCE` and return to advisor; do not invent a physical case or claim completed research.

All three options retain the frozen title/GO/SO1–SO3 until an independently approved, versioned scope amendment changes them.

## Next actions, with external dependency explicitly declared

1. Obtain the **city/country or a named university, charging operator, fleet, or utility** whose assets may be evaluated. Nothing in the canonical thesis record identifies the physical host of this *new* candidate experiment.
2. Send an authorization-conscious metadata-first request to the relevant consenting operator (draft saved separately; **NOT SENT**). Request no login/credentials in the communication.
3. Confirm the actual electrical transformer→EVSE mapping and rights with the owner; register F0 then.
4. Request the minimal permissible P/Tₑ channel inventory and two short de-identified synchronized data samples for data-quality inspection; register F3 to actual evidence tier.
5. Ask advisor to sign off on Track A vs B and minimum acceptable services, model/validation bounds, and whether one field-supported direction is sufficient (draft saved separately; **NOT APPROVED**).
6. Continue formal authenticated database query execution and original Krama PDF/raw-data request in parallel on the separate source-review workstream, not as a substitute for site-specific access.

## Research provenance
Source foundation: prior publication audits in draft PR #84 (Blomgren 2023 DOI 10.1016/j.segan.2023.101048; Bragone 2022 DOI 10.1016/j.epsr.2022.108447; Godina 2016 DOI 10.1016/j.enconman.2016.04.087; Balogun EV-EcoSim DOI 10.1109/TSG.2023.3339374; Villarroel 2017 DOI 10.1049/oap-cired.2017.1102; Krama 2026 DOI 10.1016/j.ecmx.2026.101960). None provide confirmed measurements from the proposed single site. This protocol does not itself execute searches or obtain measurements.
