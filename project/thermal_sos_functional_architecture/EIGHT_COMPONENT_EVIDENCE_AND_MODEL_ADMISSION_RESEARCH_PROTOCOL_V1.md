# Eight Components — Research Evidence Extraction, Interfaces and Model-Admission Protocol V1

**Date:** 2026-10-10. **Status:** INVESTIGATION PLAN, NOT COMPLETED TESTS.  
**Authority:** [Exact user-selected eight](SELECTED_EIGHT_COMPONENTS_WORKING_RESEARCH_BASELINE_V1.md) and [deep physics dossier](EIGHT_COMPONENT_PHYSICS_AND_DIRECTIONAL_INTERFACE_RESEARCH_DOSSIER_V1.md). No change to approved roster, canonical objective wording, conceptual V5, mathematical V3, full Electrified Transportation system boundary, or frozen M0/M1/M2 meanings.

## 1. Evidence levels — no conflation

- **L — Published class-level mechanism:** specific article/standard documents a phenomenon/model in its studied technology.
- **S — Scientific architecture selection:** strong and nonduplicative role in our named outputs and directional pathway.
- **E — Equipment-specific eligibility:** compatible technology, actual sensor, geometry, rated power, installed operating rule and parameter validity identified.
- **V — Independent scientific validation:** implemented reduced model passes energy/units/numerical tests, independent measured state/service predictions, uncertainty and operational action checks within scope.

**Current status:** all eight have S (user-approved selection); all eight have a type of L support with varying directness. No component has demonstrated E+V in one joint selected case. There is no eight-component field experiment, no executed numerical ablations, and no valid claimed bidirectional causal thermal propagation.

## 2. Detailed evidence and scientific question per selected component

| ID | Need to establish from literature (L) | Inputs/states/measurements required at E/V | Science test and admissible simplification |
|---|---|---|---|
| **P1** | Applicable transformer oil/dry family; winding/core loss→temperature equations; cooling rating and actual permissible operating condition | Transformer kVA, oil type, I,V,P,Q, ambient, top oil/hotspot measurement/estimate and control state | Predict independently measured T and action timing vs static thermal envelope; maintain loss and electrical boundary if reduced |
| **P2** | Feeder technology-dependent losses/heating/ampacity and network constraints | Actual cable/overhead topology, R,X, phase I/V, heat exposure and rated current | Compare algebraic AC feeder with dynamic thermal feeder; retain detailed temperature only if time/energy/service QOI changes beyond errors |
| **P3** | Real electrical protective/load-management hardware and its exact deployed temperature/current/time-to-action mapping | Controller/relay model, installed settings, enabled 49T or operator load action, switching/permission event logs | Compare real control response vs constant allowable power; alarm alone is not an actuating intersystem law |
| **P4** | Installed transformer radiator/natural circulation or independently switched fans; applicable heat-rejection models | Cooling class, fan/pump duty/flow if installed, ambient, radiator/oil T, auxiliary power | Replace separate cooler with aggregate P1 cooling coefficient; detailed P4 if control and state produce independently validated timing/service information |
| **T1** | Actual EVSE AC-to-DC loss, rectifier thermal response and offered-power derating literature | Device nameplate, AC P/Q and I/V, DC offered vs delivered V/I, rectifier/cabinet T, thermal command logs | Compare dynamic rectifier temperature with device-authorized ambient-only derating; test AC actual response and charging completion |
| **T2** | Battery electrochemical/thermal physics, SOC and BMS charging constraints | Terminal V/I/energy, SOC, pack temperatures, BMS requested/allowed I and actual energy required at departure | Compare energy-only storage and explicitly thermal charge-acceptance model; require source-conditioned charging limitation for added thermal state |
| **T3** | Cooling physics, powered auxiliary demand and effect on T1 rectifier T/derating | Charger fan/flow/ambient, fan auxiliary AC W, rectifier T, thermal modes | Aggregate T1 heat-rejection law vs separate cooler; keep separate only if added power/time-history prediction can be observed |
| **T4** | Vehicle HVAC auxiliary energy response to extreme heat vs propulsion energy | Observed trip Wh/km, route/distance, ambient, SOC before/after trip, HVAC compressor electric W if possible, departure schedule | Replace compressor model with measured whole-vehicle temperature-conditioned energy demand; prove later charging-schedule influence before T4→P feedback claim |

Each ID is a presentation label; legacy 20+20 mapping: P1=P02; P2=P10; P3=P08; P4=P05; T1=T01; T2=T11; T3=T04; T4=T17. Literature V2 reconstruction (19+21) uses conflicting reference IDs: DO NOT recycle.

## 3. Research questions for each component: focused and testable

1. **P1:** Which loss/thermal-state model is the least detailed one that predicts an admissible load-temperature/capability transition in time?
2. **P2:** When do feeder resistance, voltage drop, or thermal ampacity materially change charging power and aggregate losses?
3. **P3:** Is any temperature-sensitive load permission or trip **really implemented**, and does it limit the charger, as opposed to producing an alarm or insulation-aging estimate only?
4. **P4:** Is transformer cooling independently switched/dynamic, or simply an identifiable heat rejection law inside P1?
5. **T1:** Does rectifier temperature (beyond coincident outdoor temperature) explain actual offered DC power **and** measured AC power draw over time?
6. **T2:** Is pack accepted charge limited by SOC/temperature or solely by EVSE, and which energy state is needed to determine deadline readiness?
7. **T3:** Does distinct fan/pump status improve independently observed conversion losses, auxiliary demand and derating timing beyond the integrated EVSE representation?
8. **T4:** How much measured ambient-related trip energy is attributed to HVAC versus propulsion, and does that excess energy causally change subsequent charging demand and transformer loading?

## 4. Specific interface evidentiary experiments

### I2 — Transportation → Power

**Exposure/manipulation:** variation in T1 rectifier thermal state or T3 heat rejection at matched ambient, similar charging request and SOC/temperature-controlled T2 acceptance.  
**Source output:** *measured* EVSE AC input real and reactive P/Q, V/I, including auxiliary cooling power.  
**Receiver:** P2 branch-current/loss and P1 transformer measured/estimated thermal response, controlling non-EV electrical loads.  
**Crucial controls:** do not infer AC input from offered DC charger power, do not equate charger internal T changes caused by ambient with an intersystem causal influence, do not conflate EV battery-limited taper with EVSE-limited derating.  
**Decision:** label I2 qualified only when physically consistent source→receiver response/uncertainty and appropriate counterfactual can be sustained.

### I3 — Power → Transportation

**Source:** P1 thermal state plus P4 cooling history.  
**Action:** P3 documented **implemented** temperature-conditioned permissible loading/curtailment/connection interruption.  
**Receiver:** allowed EVSE AC supply, T1 offered/delivered charging power, T2 accepted pack energy and deadline readiness.  
**Critical evidence:** actual parameterized loading policy (not just generic C57.91 advisory temperature), relay wiring/permissions/controller trace.  
**Decision:** if no deployed thermal-sensitive constraint exists, *I3 remains OPEN*; it may be investigated only as a labeled intervention design scenario, not as observed installed causality.

### T4 energy-demand closure

**Needed chain:** vehicle actual trip duty and heat → T4 HVAC demand (not vehicle-level heat alone) → measured consumed battery energy → required next trip/charging energy → charging session availability and requested AC load → I2.  
**If lacking trip/charger schedule pairing:** T4 remains an internal **service-demand** component; this does not invalidate its inclusion in the research roster but blocks direct cross-boundary causal attribution.

## 5. Model and observation map

| Observation | Instrument/source | Variable or QOI identified | Invalid substitution |
|---|---|---|---|
| Ambient and site heat | Weather station at device or justified spatial source | External H(t), cooling boundary | Common ambient temperature ≠ directed coupling |
| Three-phase EVSE AC V/I/P/Q and transformer feeder flow | Calibrated synchronized AC meters | I1 input and I2 load response; P2/P1 loss | DC offered power ≠ measured AC power |
| Transformer oil/winding thermal sensing or supported estimator | Device sensors/model and logged controls | P1 thermal time constant/threshold | Insulation ageing ≠ outage |
| Transformer permitted-power commands, relay/status | Utility/manufacturer/controller logs | P3 I3 action | Temperature alarm ≠ breaker trip |
| EVSE rectifier / converter temperature | Device instrument at known sensor location | T1 heat response and possible derating | Ambient temperature alone ≠ internal junction temperature |
| EVSE fan/cooling auxiliary P and duty | Actual T3 device energy/controller log | T3 heat rejection and AC aux | Rejected heat ≠ extra electrical consumption |
| DC EVSE offered and delivered P, battery terminal P | DC charger logs + onboard BMS/port power | T1 capability vs actual T2 acceptance | Charger offered power ≠ stored energy |
| Battery SOC/temperature and departure/route logs | Vehicle BMS + service schedule | T2 readiness, temperature acceptance, T4 travel duty | Ready vehicle ≠ completed transport |
| Trip-level energy/route/HVAC use | Vehicle energy telemetry and distance | T4 HVAC and Y3 Wh/km | Total vehicle consumption cannot isolate compressor without component data |

## 6. Non-compensatory scientific gates (selection vs model admission)

- **G0:** correctly identify real physical equipment and parent/child overlap; source physics does not multiply hardware objects or thermal losses.
- **G1:** document one physically compatible transformer–feeder–DC EVSE–road vehicle architecture; without it do not assert specific thermal law/limit.
- **G2:** verify component-appropriate losses, thermal balance and *real* permitted capability/operating rule. Reviews support principles but not device parameters.
- **G3:** classify participation in I1, I2, I3, I4, I5, I6 correctly; internal cooling/HVAC is not automatically across-boundary coupling.
- **G4:** predeclare output materiality (temperature, loss kWh, charger conversion %, energy per trip, readiness, first service shortfall, response/recovery). Compare detailed and physically consistent reduced model using independently checked outputs; no invented numerical weights or pass thresholds.
- **G5:** establish observation positions, parameter-identifiability, uncertainty, numerical verification, and independent held-out field or applicable experimental data.
  
**No single paper passes all G0–G5 for our eight-system combination.** The file intentionally does not mark these requirements as completed.

## 7. Conservation and mathematical checks

1. **Dimensional:** $C_{th}$ [J/K] × $\dot T$ [K/s] = [W]; feeder $I^2R$ [W]; heat rejection [W]; accumulated energies [J or kWh].
2. **Electrical:** transformer primary power, loss and secondary power accounted with sign and three-phase P/Q; feeder losses and EVSE AC input separated from non-EV facility demand.
3. **EVSE:** real AC energy = DC port energy + electronics loss + fan/pump/other EVSE auxiliary energy + accounted internal storage/residual. No extra cooling heat in electric-loss sum.
4. **Battery:** EVSE DC port ≠ battery terminal power ≠ chemical stored energy; SOC is energy/charge state, not temperature.
5. **Vehicle trip:** energy consumed = traction + HVAC + other measured auxiliary energy under consistent battery output/time basis.
6. **Time:** resample/align sensor and command timestamps; declare latency/sampling windows and calendar/tz; do not treat correlational lag as propagation delay.
7. **Validation:** independent period/vehicle/site/operating-window holdout as supported; evaluate model residual structure, calibration-versus-test distinction and uncertainty.
8. **Reduced-model ablation:** replacing P4 or T3 separate thermal state with integrated heat rejection is scientifically legitimate; replacing P2 conductor temp with algebraic power flow may suffice if no thermal conductor constraint; T4 HVAC may be an external time-dependent demand rather than another thermal state.
9. **Model comparison:** M0 controlled severed-influence counterfactual, M1 evidence-supported algebraic electric interface, M2 additionally justified *causal dynamic* thermal interface. More ODEs alone do not prove M2.

## 8. End-to-end study execution order

**E0** Freeze selected roster, presentation aliases and **6 outcome boundaries** (this file, not new thesis objectives).  
**E1** Literature source-specific extraction: physics, equation, units, technology, operating limits, measurement type, uncertainty and transferability **per component**.  
**E2** Map eight equipment blocks, physical containment P4⊂P1/T3⊂T1, and interface I1–I3 separate from within-system I4–I6.  
**E3** Define device technology and lawful controls; obtain necessary nameplate, cooling, protection, AC/DC, BMS/vehicle and weather evidence.  
**E4** Preregister minimum-sufficient state candidates and algebraic ports; avoid assuming eight thermal ODEs.  
**E5** Check component isolation, observability, state/parameter identifiability, and thermal/electric conservation; run numerical verification and held-out model validation.  
**E6** Check I2 and I3 independently; do not claim bidirectional coupling if only I2 is demonstrated.  
**E7** Quantify SO3 timings, service curves, electricity/charging efficiency, mobility energy use when measured, readiness, and recovery only as modeled.  
**E8** Assess two sustainability pathways using environmental/economic/social data and evidence-bounded UN target relevance.

**Stop conditions:** NO_SUPPORTED_P3_RULE; NO_T1_AC_INPUT_RESPONSE; NO_MEASURED_THERMAL_STATE; NO_IDENTIFIABLE_SOC_OR_SERVICE; NO_INDEPENDENT_TEST. Record scientifically, then pursue feasible lower-fidelity or scenario-only analysis without fabricating a substitute.

## 9. Source register and provenance standards

Direct literature anchors: [Hilshey et al. 2013](https://doi.org/10.1109/TSG.2012.2217385); [Pan et al. 2025](https://doi.org/10.1049/hve2.70024); [Li et al. 2024](https://doi.org/10.1049/hve2.12345); [Krama et al. 2026](https://doi.org/10.1016/j.ecmx.2026.101960); [Bernardi et al. 1985](https://doi.org/10.1149/1.2113792); [Parker et al. 2025](https://doi.org/10.1016/j.apenergy.2024.125051); [Rahman et al. 2024 review](https://doi.org/10.1109/ACCESS.2024.3385429); [ABB RET615 manufacturer documentation](https://library.e.abb.com/public/e5e9f20ae5454e14a5572a13ec67e88a/RET615ANSI_appl_201230_ENb.pdf); [IEEE C57.91-2025 scope](https://standards.ieee.org/ieee/C57.91/7163/); [UN SDG indicator definitions](https://unstats.un.org/sdgs/metadata/).

**Evidence control:** every promoted physical model parameter or law must record the originating paper's exact device, page/equation or the standard's valid clause, dimensions, temperature range, assumptions, fidelity, manufacturer/software implementation, provenance and independent test. DOI existence or common engineering practice does not suffice for case-specific validation.

**Note:** IEEE normative clauses are licensed and have not all been consulted; Elicit academic connector API access was denied under current connected plan; Wiley Scholar Gateway was temporarily unreachable; publisher/author sources plus existing repository literature were used for this document.
