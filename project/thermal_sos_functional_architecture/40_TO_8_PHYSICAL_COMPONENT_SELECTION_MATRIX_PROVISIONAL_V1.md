# 40-to-8 Physical Component Selection Matrix — provisional screening V1

**Date:** 2026-10-10. **Status:** SCREENED ON SOURCE/MODEL RELEVANCE; ORIGINAL 40 IDENTITY **NOT RECONCILED**; 4+4 shortlist **PROVISIONAL / NOT ADMITTED**; equipment case **OPEN**; ablation **SPECIFIED / NOT RUN**; physical validation **NOT RUN**.

**Data file:** [40-row machine-readable matrix](40_TO_8_COMPONENT_SELECTION_MATRIX_PROVISIONAL_V1.csv). **This is not the original independently verified 19 P + 21 T_e component register.** It is a transparent *reconstructed screening set* (19 P + 21 T_e) made by retaining 29 distinct candidate thermal-*check* rows from the current GitHub register and adding 11 explicitly named candidate component *proposals* grounded in the working functional architecture. Several of those 40 are subcomponents, operating rules, overlapping assemblies, or alternatives; they are intentionally **not counted as 40 unique physical components**. This source-identity shortfall blocks G0 approval of the overall historical 40. The 40 original components must still be recovered/reconciled before a true 40→8 final selection.

## Scientific authorities and method
- [Reality-first selection protocol](../DOSSIYA_REALITY_FIRST_40_TO_8_COMPONENT_SELECTION_PROTOCOL_V1.md)
- [Working component/interface architecture](WORKING_SOS_COMPONENT_FUNCTION_INTERFACE_MATRIX_V1.md)
- [29 thermal-limit checks (12 P, 17 T_e)](EQUIPMENT_SPECIFIC_THERMAL_LIMIT_CANDIDATE_INVENTORY_V1.md)
- [Frozen research objectives](../CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md)
- [Transformer model admission](../module_01_transformer_thermal_state_physics/MODULE_01_MODEL_ADMISSION_LEDGER_V1.md)
- [Current conceptual V5](../CONCEPTUAL_FRAMEWORK_SPEC_V5_THERMAL_SUSTAINABILITY.md), [mathematical V3](../MATHEMATICAL_FRAMEWORK_SPEC_V3_THERMAL_SUSTAINABILITY.md), [preferred provisional V6](../CONCEPTUAL_FRAMEWORK_V6_PROPOSED_EVIDENCE_GATED_THERMAL.md)

**Important:** row-level model evidence and a generic equipment standard are not an actual admissible device, identified case parameter, validated numerical limit or passed G1/G4/G5. IEC/IEEE titles referenced here were scope-checked only; no full licensed standard-clause audit was performed. The external datasets listed are possible inputs, not paired transformer+charger field measurements.

## 1. Reconciliation and gate result

| Population | Rows | Status |
|---|---:|---|
| Source traceable to 29-item thermal-*limit* register | 29 | Exact source labels preserved, but ontology heterogeneous |
| Proposed reconciliation additions | 11 | Clearly labeled extensions; NOT claimed to be original 40 |
| Provisional screening file | 40 (19 P + 21 T_e) | Structural/literature screening performed; G0 historical reconciliation OPEN |
| Candidate eight selected from this reconstruction | 4 P + 4 T_e | **Illustrative shortlist only**, not passed |
| G1 selected equipment compatible case | 0 of 40 confirmed | OPEN |
| G5 ablation tests | 0 of 40 executed | NOT_RUN |
| Independently validated directional thermal laws | 0 selected-case | OPEN |

### Why no candidate passes all six gates
G0 physical-object type was classified, but provenance match to original 40 is not verified. G1 cannot pass until a mutually compatible installation is identified. G2 indicates physical mechanism from a paper/law, never transfers a numerical law by default. G3 remains conditional because the actual P→T_e operating and T_e→P AC response laws are not independently observed. G4 is partial because equipment parameters and synchronized validation data are not supplied. G5 requires actual leave-one-out calculations with a declared QOI, not a plausible narrative. **Thus there are zero scientifically approved model components in this deliverable.**

**Gate interpretation:** PASS only after source+case+test. OPEN is not failure; FAIL on G0 means not a distinct physical component; MERGE/SPLIT prevents double counting. No weight or total score can override any hard gate.

## 2. Complete 40-row compact screening matrix

In each row, **G1 = OPEN**, **G5 = NOT_RUN**, selected-case **G3 = CONDITIONAL**. The CSV contains the full function, thermal mechanism, directional/service role, literature citation/URL, applicable standard/scope, dataset limitations, all six gates and ablation hypothesis.

| ID | System | Candidate name | G0 object type | G2 physics | Current action |
|---|---|---|---|---|---|
| P01 | P | Oil-immersed transformer — winding | MERGE | PUBLISHED_MECHANISM_NOT_CASE | MERGE_WITH_PARENT |
| P02 | P | Oil-immersed transformer — oil | MERGE | PUBLISHED_MECHANISM_NOT_CASE | MERGE_WITH_PARENT |
| P03 | P | Transformer insulation and lifetime | MERGE | PUBLISHED_MECHANISM_NOT_CASE | MERGE_WITH_PARENT |
| P04 | P | Transformer core and metallic parts | MERGE | PUBLISHED_MECHANISM_NOT_CASE | MERGE_WITH_PARENT |
| P05 | P | Transformer tank, bushings and terminals | SPLIT | CONDITIONAL_PHYSICS | SPLIT_BEFORE_ADMISSION |
| P06 | P | Transformer cooling | CANDIDATE_PHYSICAL | PUBLISHED_MECHANISM_NOT_CASE | PROVISIONAL_SHORTLIST |
| P07 | P | Transformer normal/emergency operation | FAIL | PUBLISHED_MECHANISM_NOT_CASE | NOT_PHYSICAL_COMPONENT |
| P08 | P | Overhead feeder conductors | ALTERNATIVE | CONDITIONAL_PHYSICS | ARCHITECTURE_ALTERNATIVE |
| P09 | P | Underground distribution cables | ALTERNATIVE | CONDITIONAL_PHYSICS | ARCHITECTURE_ALTERNATIVE |
| P10 | P | Switchgear, breakers, busbars, protection | SPLIT | CONDITIONAL_PHYSICS | SPLIT_BEFORE_ADMISSION |
| P11 | P | Dry-type transformer (alternative architecture) | ALTERNATIVE | CONDITIONAL_PHYSICS | ARCHITECTURE_ALTERNATIVE |
| P12 | P | Upstream power-electronics / converters (if actually present) | ALTERNATIVE | CONDITIONAL_PHYSICS | OPEN_CASE |
| P13 | P | Oil-immersed distribution transformer — integrated assembly | CANDIDATE_PHYSICAL | PUBLISHED_MECHANISM_NOT_CASE | PROVISIONAL_SHORTLIST |
| P14 | P | Distribution feeder circuit — integrated segment | CANDIDATE_PHYSICAL | CONDITIONAL_PHYSICS | PROVISIONAL_SHORTLIST |
| P15 | P | Circuit breaker — physical switching device | CANDIDATE_PHYSICAL | CONDITIONAL_PHYSICS | PROVISIONAL_SHORTLIST |
| P16 | P | Thermal protective relay — physical controller | CANDIDATE_PHYSICAL | PUBLISHED_MECHANISM_NOT_CASE | OPEN_CASE |
| P17 | P | Voltage regulator / autotransformer | ALTERNATIVE | CONDITIONAL_PHYSICS | OPEN_CASE |
| P18 | P | Instrument transformer / temperature-sensor module | CANDIDATE_PHYSICAL | OPEN | OPEN_CASE |
| P19 | P | Grid-edge DER inverter (if actually installed) | ALTERNATIVE | CONDITIONAL_PHYSICS | OPEN_CASE |
| T01 | T_e | EVSE enclosure/cabinet | MERGE | PUBLISHED_MECHANISM_NOT_CASE | MERGE_WITH_PARENT |
| T02 | T_e | EVSE rectifier/converter | MERGE | PUBLISHED_MECHANISM_NOT_CASE | MERGE_WITH_PARENT |
| T03 | T_e | EVSE semiconductor junctions | MERGE | CONDITIONAL_PHYSICS | MERGE_WITH_PARENT |
| T04 | T_e | EVSE power modules | MERGE | PUBLISHED_MECHANISM_NOT_CASE | MERGE_WITH_PARENT |
| T05 | T_e | EVSE active cooling | CANDIDATE_PHYSICAL | PUBLISHED_MECHANISM_NOT_CASE | PROVISIONAL_SHORTLIST |
| T06 | T_e | EVSE AC input stage | MERGE | PUBLISHED_MECHANISM_NOT_CASE | MERGE_WITH_PARENT |
| T07 | T_e | EVSE DC output stage | MERGE | PUBLISHED_MECHANISM_NOT_CASE | MERGE_WITH_PARENT |
| T08 | T_e | Physical charging cable | CANDIDATE_PHYSICAL | CONDITIONAL_PHYSICS | PROVISIONAL_SHORTLIST |
| T09 | T_e | Charging connector/contact | CANDIDATE_PHYSICAL | CONDITIONAL_PHYSICS | OPEN_CASE |
| T10 | T_e | Vehicle inlet | CANDIDATE_PHYSICAL | CONDITIONAL_PHYSICS | OPEN_CASE |
| T11 | T_e | Battery cells / RESS | MERGE | PUBLISHED_MECHANISM_NOT_CASE | MERGE_WITH_PARENT |
| T12 | T_e | Battery pack | CANDIDATE_PHYSICAL | PUBLISHED_MECHANISM_NOT_CASE | PROVISIONAL_SHORTLIST |
| T13 | T_e | Battery management system (BMS) | FAIL | PUBLISHED_MECHANISM_NOT_CASE | NOT_PHYSICAL_COMPONENT |
| T14 | T_e | Battery thermal management | CANDIDATE_PHYSICAL | PUBLISHED_MECHANISM_NOT_CASE | OPEN_CASE |
| T15 | T_e | Onboard charger (only if used) | ALTERNATIVE | CONDITIONAL_PHYSICS | ARCHITECTURE_ALTERNATIVE |
| T16 | T_e | Traction inverter / motor | SPLIT | CONDITIONAL_PHYSICS | SPLIT_BEFORE_ADMISSION |
| T17 | T_e | Vehicle HVAC / auxiliaries | SPLIT | CONDITIONAL_PHYSICS | SPLIT_BEFORE_ADMISSION |
| T18 | T_e | DC EV charging station — integrated EVSE assembly | CANDIDATE_PHYSICAL | PUBLISHED_MECHANISM_NOT_CASE | PROVISIONAL_SHORTLIST |
| T19 | T_e | BMS embedded hardware/control unit | CANDIDATE_PHYSICAL | PUBLISHED_MECHANISM_NOT_CASE | OPEN_CASE |
| T20 | T_e | Traction battery pack — complete installed assembly | CANDIDATE_PHYSICAL | PUBLISHED_MECHANISM_NOT_CASE | PROVISIONAL_SHORTLIST |
| T21 | T_e | Charging power-transfer communication controller | CANDIDATE_PHYSICAL | CONDITIONAL_PHYSICS | OPEN_CASE |
  
## 3. Provisional 4+4 physical portfolio — NOT FINAL

This is a deliberately stress-tested **candidate portfolio**; it is not a claim that a transformer must have a separate cooler, that an air-cooled charger must have a separate fan state, or that an independent switchgear thermal ODE is needed. The chosen eight will be replaced if case evidence or G5 shows redundancy.

| Sector | Candidate | Why initially considered | Dominant issue to resolve |
|---|---|---|---|
| Power | **P13** Oil-immersed distribution transformer — integrated assembly | Loss→oil/winding transient thermal response | RECONSTRUCTED candidate; transformer type/rating/thermal parameters/operation unknown |
| Power | **P14** Distribution feeder circuit — integrated segment | Load losses, optional conductor heating | RECONSTRUCTED; topology and overhead vs underground technology OPEN |
| Power | **P15** Circuit breaker — physical switching device | Contact temperature; thermal trip if specified | RECONSTRUCTED; breaker vs unrelated protective trip mechanism OPEN |
| Power | **P06** Transformer cooling | Ambient-dependent cooling and switching | Is cooling independently actuated and measured or passive integrated radiator? |
| T_e | **T18** DC EV charging station — integrated EVSE assembly | Rectifier loss, heat storage/cooling, thermal derating | RECONSTRUCTED; need compatible named DCFC and time-aligned AC/DC/temperature |
| T_e | **T05** EVSE active cooling | Convection/flow and cooling duty under hot ambient | Cooling independently adjustable? data on fan/pump and parasitic load missing |
| T_e | **T08** Physical charging cable | I2R heat/current rating under ambient cooling | Cable rating/thermal measurement and route unknown |
| T_e | **T20** Traction battery pack — complete installed assembly | Pack thermal conditioning and accepted-current limit | RECONSTRUCTED; same physical pack as T12, requires deduplication; SOC not measured in ACN |

### Portfolio conflicts (explicit)
- P13 transformer may already include P06 cooler. Count P06 separately **only if** physically distinct, independently controllable/measured, relevant to thermal transition, and non-redundant relative to a transformer cooling-mode law. Otherwise substitute another eligible actual P component.
- T18 EVSE necessarily contains converter/cabinet and may already include T05 cooling. Count T05 separately only under the same independence and ablation criteria. **An EVSE power converter and the EVSE complete assembly must never be counted as two independent components without justified distinct boundaries.**
- T08 cable without T09 connector must still enforce the connector's documented limits at the AC/DC system boundary if necessary; T09 can be an algebraic constraint without becoming ninth component.
- P14 must be instantiated as **one actual feeder technology**, not simultaneous overhead and underground network structures. P15 physical breaker must have actual thermal action if used for P→T_e restriction.
- T20 and T12 are overlapping representations of the same battery pack: retain only one. The BMS (T13/T19) may be operating logic rather than another component.
- IEEE 13-node and 123-node are **electrical benchmarks**; they do not establish transformer/EVSE thermal validation or a physical installation.

## 4. Leave-one-out ablation matrix — specified tests, not observed results

**Reference B:** Run the full **qualified** reduced case under fixed equipment, ambient heat, base non-EV load, charging requests, controls, initial states and data/parameter assumptions. Remove exactly one *model component representation*, replacing it with the physically appropriate fixed-boundary, algebraic equivalent or aggregate model; do not remove the real grid connection or charging service. Refit only if the preregistered comparison permits it.

| Removed | Physically consistent reduced alternative | Primary QOI and predicted discriminant (HYPOTHESIS) | Test status |
|---|---|---|---|
| P13 transformer | Static efficiency/thermal-capability input, no dynamic transformer temperature | Transformer hot-spot/error; P→T_e restriction timing if actuated; HYPOTHESIS: state-time changed | NOT_RUN |
| P14 feeder | Idealized algebraic AC port with same requested power | AC voltage/current losses, limits, charger input and service; HYPOTHESIS: may be negligible if stiff feeder | NOT_RUN |
| P15 breaker | Documented thermal dispatch/limit only or fixed available supply, no unsupported trip | First supply interruption/event and delivered electricity; HYPOTHESIS: irrelevant if no actual breaker action | NOT_RUN |
| P06 transformer cooler | Integrate documented cooling into P13 instead of separate cooler dynamics | Top-oil/hotspot and recovery; HYPOTHESIS: identical if cooler not independently switched | NOT_RUN |
| T18 EVSE | Manufacturer documented ambient-to-power algebraic law, preserve AC/DC conservation | Rectifier thermal timing, available power, actual AC demand; HYPOTHESIS: dynamic model adds no value absent internal memory data | NOT_RUN |
| T05 EVSE cooler | Equivalent prescribed thermal rejection/derating curve within T18 | Derating onset, delivered power, auxiliary AC energy; HYPOTHESIS: redundant absent independently switched cooling | NOT_RUN |
| T08 charging cable | Documented fixed permissible transfer current/connector constraints | First current limiting event, charging kWh, departure energy; HYPOTHESIS: dynamic heating possibly unnecessary | NOT_RUN |
| T20 battery pack | Energy balance and documented charge-acceptance envelope; omit detailed pack thermal PDE | Departure energy, accepted current/power, charging completion; HYPOTHESIS: energy-only model adequate unless BMS thermal restrictions bind | NOT_RUN |

**Formal decision rule:** Retain an extra dynamic/physical component only if (i) it is actually distinct and present, (ii) its removal causes a material change in the preregistered state/critical-time/service QOI *relative to observation or independently checked physical truth*, not just disagreement with a more elaborate simulation, and (iii) the additional complexity is identifiable with available data. Tolerances and uncertainty must be specified *before testing*, using sensor accuracy, service requirements and physical impact; they are **OPEN**, not arbitrary universal percentages. If outputs cannot be validated, interpret ablation as conditional sensitivity, not scientific proof of necessity.

### QOIs and counterfactual tests
- Temperature `T_top-oil, T_hotspot, T_rectifier` where equipment/sensors support them; AC apparent input `S=P+jQ` and DC output separate; energy to EV; electricity-service shortfall; charging departure-energy readiness proxy.
- First admitted thermal boundary event; first actual operating action; first service shortfall; recovery time only when modeled; cross-system propagation delay only with independent event identification and matched/identifiable source–receiver causation.
- **M0** independently severed tested mechanism (controlled counterfactual); **M1** admissible static/algebraic coupling; **M2** extra *physically qualified* dynamic interdependency. M2 is not automatically enabled merely by two thermal ODEs. Comparator results **NOT_RUN**.

## 5. Case-level gate to execute next

1. Recover the true 19 P + 21 T_e source names (not merely their count), reconcile with all 40 reconstruction rows, and drop duplicates/functions/limits before choosing independent equipment.
2. Select **a real compatible transformer/charger configuration**: oil-immersed versus dry-type, feeder technology, thermal cooling, DC/AC port, equipment ratings and duty; reconcile rated transformer kVA with charger AC demand.
3. Obtain manufacturer thermal operating rule *and actual implemented protective response* (P-side) and EVSE temperature-conditioned AC input/power (T_e-side), or explicitly bound claim to model scenarios.
4. Extract exact clauses, manufacturer model/version, sensing location, calibration/test evidence, and design measurement synchronized on same installation; public weather/ACN alone do not validate full interdependency.
5. Form a **nonredundant** candidate portfolio, preregister leave-one-out/QOI criteria, execute physically consistent simulations and held-out validation where possible, then either admit 4+4 or document fewer eligible components.

## 6. External evidence registry (scope checked; no site-specific transfer approved)

- Hilshey et al. (2013): https://doi.org/10.1109/TSG.2012.2217385 — oil transformer thermal/aging simulation with EV charging.
- Krama et al. (2026): https://doi.org/10.1016/j.ecmx.2026.101960 — observed air-cooled DCFC heat derating, site-specific and data on request.
- Qian et al. (2015): https://doi.org/10.1016/j.ijepes.2014.09.040 — transformer aging under EV charging, scenario-specific.
- Bernardi et al. (1985): https://doi.org/10.1149/1.2113792 — general battery energy/thermal balance.
- IEEE C57.91-2025: https://standards.ieee.org/ieee/C57.91/7163/ — oil transformer loading; licensed clauses must be checked.
- IEC 60076-7:2018: https://webstore.iec.ch/en/publication/34351 — oil transformer loading; licensed.
- IEC 60076-12:2008: https://webstore.iec.ch/en/publication/592 — dry-type transformers; equipment alternative.
- IEEE 738-2023: https://standards.ieee.org/ieee/286/10207/ — overhead conductor current-temperature.
- IEC 60853: https://webstore.iec.ch/en/publication/3711 — cyclic/emergency cable rating, clause applicability pending.
- IEC 61851-23:2023: https://webstore.iec.ch/en/publication/32973 — DC EVSE equipment scope.
- IEC 62196-3:2026: https://webstore.iec.ch/en/publication/86314 — DC/AC-DC coupler dimensional compatibility; does not itself supply site-specific connector temperature limit.
- ACN-Data: https://ev.caltech.edu/dataset — charging current and sessions; **NOT EVSE internal temperature or observed BMS SOC**.
- NOAA Global Hourly: https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database — weather forcing only.

**Conclusion:** The requested 40-row analysis and 8 removal-test specifications are delivered as transparent **provisional screening**. The original complete forty-component source was not independently recovered, so numerical 40→8 scientific selection remains OPEN. This document does not change canonical V5/V3 or the frozen thesis objectives.
