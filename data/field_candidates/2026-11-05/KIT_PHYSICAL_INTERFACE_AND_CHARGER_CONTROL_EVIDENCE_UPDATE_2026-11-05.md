# KIT field electrical interface, controls and evidence transfer — 2026-11-05

**Status:** Publisher-verifiable source/variable audit, **not** a claim of field voltage-to-EV causality.
**Primary source:** KIT 100 ms OLTC campus measurements, https://doi.org/10.5281/zenodo.22826984.
**Preexisting audit:** [KIT exact topology and source constraints](KIT_OLTC_ELECTRICAL_TOPOLOGY_EVIDENCE_AUDIT.md). Do **not** reopen the already-completed source timestamp / hash checks or block supporting system-level analysis on unpublished exact feeder mapping.

## 1. Physical interface gate — findings

- KIT publisher explicitly identifies synchronized campus 110 kV, 20 kV and 0.4 kV electrical metering with charging of electric vehicles among downstream loads and an OLTC voltage-regulation anomaly. Observed voltage changes may propagate through the campus distribution network. These facts establish **campus system co-location and a documented multivoltage supply architecture**, not a specific point-to-point feeder connection between `PMU01_J01` and `EV_SH.J.6`.
- The exact physical parent feeder, MV/LV transformer, tap/switch status and circuit path associated with the 20 kV PMU and low-voltage EV point **remain unverified** in inspected published records. The existing campus architectural references explain why multiple possible paths exist. It would be incorrect to set M1 direct parentage = true on the basis of waveform similarity.
- Publisher describes the OLTC anomaly as inconsistent regulation commands associated with a tap-selector resistor bridge contact-resistance/corrosion issue; this is source-reported fault context, **not** a synchronized time series of OLTC tap commands or charger supervisory signals in the three original schemas inspected.

**M1 classification:** Verified *broader interconnected campus 110/20/0.4-kV infrastructure*. Exact 20 kV PMU → EV-point supply path **NOT VERIFIED**; allow observational M2/M3 study under the user's already-approved system-level scope.

## 2. Missing controller-state gate in the original KIT field data

- Inspected original source fields at the EV 400 V point include three-phase voltage/current/real power/reactive power and fault-phase annotations. Previously extracted 20 kV source includes positive-sequence voltage/current. These electrical signals do **not** directly encode whether charging was authorized, EV connected, user-requested target, battery SOC, charger enable state, charging current/power setpoint, active charging session, or tap-changer control command.
- A multi-step change in measured EV point watts could be a charger setpoint/session transition, but **no claim of a particular controller action is yet evidence-qualified**.
- An **instrument-aligned network/charger controller log**, with event times, would be needed to attribute the two selected +11.1/+13.8 s transitions to a named action. Exact feeder topology would be needed for claims of branch-specific M1/M4, though not for observational, campus-level M2/M3.

## 3. External source identified for controlled EV charging electrical mechanism (different experiment)

**KIT PHIL laboratory set:** https://doi.org/10.5281/zenodo.22965111 (record https://zenodo.org/records/22965111). The KIT authors describe controlled step/ramp 230 V disturbances in an 11 kW AC charging setup (max 16 A) using OPAL-RT and a real-time power amplifier, **20 ms** recordings for Nissan Leaf, Renault Zoe, Volkswagen ID.4, Tesla Model 3 and MG4. These are **different laboratory trials at KIT**, not the 50-day 110/20/400 V field deployment. Available source file descriptions include per-phase voltage/current and time; do not infer that the public CSV contains the EVSE command setpoint, charger state, SoC or a true feeder map unless those columns are confirmed in a downloaded file. Controlled input makes the experiment relevant to testing a voltage perturbation mechanism, **subject to testing design, synchronization and instrumentation limitations**.

**Scientific status:** Strong candidate for **controlled electrical P→EV behavior validation**, *not direct field-event explanation or thermal-field validation*.

## 4. Complementary source with documented charger control/state fields (different laboratory and devices)

**Esser et al., Scientific Data (2025):** https://doi.org/10.1038/s41597-025-05524-5. **Public dataset DOI:** https://doi.org/10.5281/zenodo.14065331 (TU Dortmund Smart Grid Technology Lab, separate experimental equipment and EV fleet). The paper describes **142** laboratory EV charging measurements, both unidirectional and bidirectional, across **8** EVs.

The paper's parameter overview states that **C-type charger observations** include, depending on the charger and experiment, charging status, AC power setpoint, charger output voltage/current/power, battery SoC, and/or charging-enable/current setpoints. **G-type grid observations** include RMS voltage/current, active power and ambient temperature; E-type EV monitoring includes DC voltage/current and ambient temperature where available. Availability is **device/mode-specific**; read `parameters.csv`, `measurements.csv` and selected session files before claiming any named field is present in every run.

These laboratory control data are useful to define measurable competing operating mechanisms and device-state transition patterns. They cannot be retroactively added to the March 10 KIT field timestamps as if they originated from the same EVSE or network.

## 5. What the current measurements support versus what would demonstrate operational dependence

| Question | Evidence now | Claim gate |
|---|---|---|
| M1 broad campus electrical infrastructure? | KIT publisher and prior network study describe 110/20/0.4 kV and EV load category | **SYSTEM-LEVEL STRUCTURE VERIFIED** |
| M1 exact PMU and EV-point feeder path? | No feeder adjacency / MV-LV parent ID | **OPEN** |
| M2 synchronized 20/400 V response? | Two real 100 ms events; signed local voltage changes ±0.7% and same measured strongest-step timestamp at 100 ms resolution | **OBSERVED CO-RESPONSE** |
| M3 delayed EV power-state transitions? | Two measured, sustained post-step state changes; no matched control yet | **OBSERVED TEMPORAL ASSOCIATION** |
| M3 response caused by grid voltage? | No verified EVSE control log, exact path, isolated treatment or adequate controls | **NOT IDENTIFIED** |
| Heat-induced P→EV/EVSE constraint or transport service degradation? | No relevant thermal or mobility-demand field variables from the original KIT trio | **NOT MEASURED** |

## 6. Matched-comparison design before source processing

Run [predeclared quiet-window case/control analysis](../../../tools/kit_m3_matched_quiet_controls.py) using already-derived measured **1 s** source Parquet arrays, for **both event AND controls** (do not compare 1 s control deltas numerically with original 100 ms event estimands).

- Eligible quiet controls: same UTC date, same publisher `fault_phase`, no 20 kV one-second step ≥**0.15%** anywhere in [-20,+30] s, finite EV P / 20 kV V / 400 V in whole window, not within ±180 s of either selected case.
- Match reference pre-event EV power within max(100 W, 20%) and U20 pre voltage within 2%; require a stable pre-power baseline (MAD and maximum deviation gates documented in script).
- Compare **same-window** event-minus-control late-post ΔP (pre -5..-1 s; late-post +20..+30 s), report control sample size and result distribution; separate control and case voltage step sizes.
- Recurring ~30 s OLTC steps may leave **no** valid quiet same-phase controls, in which case output **NO_CLEAN_MATCHED_CONTROLS_AVAILABLE** and do not silently change matching or claim an estimated treatment effect. These 2 cases are one fault episode, not independent trials.
- If strict matching is infeasible, the next best distinct evidence stream is the **controlled** KIT PHIL data and independent EVSE-state recordings, *not* a post hoc fabricated matched control.

**Research decision:** Continue measurement-first; accept no identifiable causal effect if the available source cannot identify one. Preserve measured field KIT dynamics as observational M2/M3 evidence and treat control/state/thermal sources with their correct provenance.