# Independent KIT PHIL measurements: quantitative evidence decision

**Date:** 2026-11-05  
**Status:** Scientific interpretation of independently measured, original KIT PHIL CSVs analyzed by the user on a Mac and committed to `main` as `a01e64a0`; numerical JSON fetched directly from `main`, not reprocessed here. No merger with the earlier 50-day KIT OLTC campus field records.

## Sources and provenance

- Source controlled hardware-in-the-loop experiment: https://doi.org/10.5281/zenodo.22965111 (KIT five EV models, source 20 ms recordings).
- [Source-derived measurement JSON](INDEPENDENT_EV_LAB_M2_M3_ELECTRICAL_AUDIT_V1.json); [readable summary](INDEPENDENT_EV_LAB_M2_M3_ELECTRICAL_AUDIT_V1.md); [analysis code](../../../tools/independent_ev_lab_voltage_control_audit.py).
- Mac output: `PASS` synthetic test; Python trust store not configured but fallback macOS curl with TLS verification enabled; MD5-publisher verification passed for all five original PHIL files and two TU Dortmund metadata files; 2 JSON/Markdown outputs pushed by user as `a01e64a0`.
- The actual measured CSV headers contain `time_s,U_L1_V,U_L2_V,U_L3_V,I_L1_A,I_L2_A,I_L3_A`. **They do not contain active real power [W], EVSE command/setpoint time, Charging_Status, power factor, SOC or thermal state.** A derived sum of U_RMS × I_RMS has **units VA (apparent power proxy), not real W**.

## Results and detectors

The Python method screened measured mean-of-three-phase voltage changes using a **2 V absolute plateau difference** with baseline (-3,-0.5 s) and post (+0.5,+3 s) windows; no experimental command times were supplied in the files. Current change is post minus pre median mean-of-three-phase current. Sustained current change requires a deviation exceeding the *adaptive* threshold max(0.5 A, 5×pre-event current robust MAD scale) continuously for at least 0.6 s.

| Vehicle | Original samples | Screened measured-voltage transitions (n) | Median absolute detected ΔU (%) | Median absolute detected ΔI (A) | Max absolute detected ΔI (A) |
|---|---:|---:|---:|---:|---:|
| Volkswagen ID.4 | 8,809 | 16 | 2.1931 | 0.0100 | 0.3100 |
| Nissan Leaf | 8,810 | **0** | n/a | n/a | n/a |
| MG4 | 8,810 | 16 | 2.1913 | 0.0100 | 0.3133 |
| Tesla Model 3 | 8,810 | 16 | 2.1960 | 0.0717 | 0.1200 |
| Renault Zoe | 8,810 | 16 | 2.1867 | 0.0333 | 0.0767 |

- **64 screened transitions** in 4 EV traces: 32 positive and 32 negative measured-voltage changes.
- For the 64 screened transitions, none received a non-null `first_sustained_current_deviation_after_screen_time_s` under the programmed **adaptive current deviation ≥max(0.5 A, 5 robust-noise scales) for 0.6 s** criterion. This **does not** prove perfectly constant current or absence of responses below threshold.
- Many ~2.2% voltage changes coincide with very small mean phase-current pre/post differences. This supports **measured small-current-change co-response under the lab's voltage stimulus**; it is **not evidence identifying a specific current-regulation controller**.
- **Nissan Leaf zero-event caution:** Zero means *the 2 V plateau-change screen returned no candidates*. It is not evidence that no voltage disturbance was applied, that the vehicle is unaffected by voltage, or that its charger was disconnected. Check original full-run voltage span, local t=0 signal, 0.5/1/1.5/2/3/5 V threshold sensitivity, and segmentation. A separate versioned diagnostic script has been added: [screening sensitivity](../../../tools/independent_ev_phil_voltage_screen_diagnostics.py).
- The measured nominal sample interval was approximately **0.021 s** (by source `time_s` median), not exactly the 20 ms nominal label. Use measured timestamps for dynamic calculations.

## Independent TU Dortmund controller-state evidence audit

- Source: https://doi.org/10.5281/zenodo.14065331 (separate laboratory, NOT KIT PHIL or KIT OLTC).
- Publisher-checksum-qualified `measurements.csv` contains **142** indexed experiments; **103** index rows are algorithmically flagged as candidate dynamic sessions according to text matching. This is a **metadata filter**, not 103 verified charging-state transitions.
- `parameters.csv` lists **7 relevant controller-state, power/current setpoint or SOC field definitions**, including `ChargingEnabled_WL_H`, `I_Setpoint_WL_H`, `AC_Power_set_ID2`, `AC_Power_set_ID3`, `AC_Power_set_ID4`, `SoC_ID2`, `SoC_ID3`.
- **Still not inspected:** actual measurements of power versus commands in a selected session; controller state transitions and response delay cannot be estimated from metadata descriptions alone. Next source gate is a bounded selected session download/extraction, not treating the whole archive as a previously analyzed measured response.

## Physics-and-evidence conclusion

1. **Measured lab M2 analogue:** a reproducible U-step screen finds 64 detected voltage transitions over four actual EV lab datasets. The Nissan Leaf screen needs independent sensitivity QA.
2. **Measured lab M3 analogue:** phase-current differences around the screened U changes are mostly small (max absolute ~0.3133 A in this screening), and no screened step crosses the adaptive persistent current-response rule. This is an **empirical conditional current observation**, not an established control law, active-power measurement, or real/imaginary-power decomposition.
3. **Control attribution:** no charger command/channel in the KIT PHIL source CSV; Dortmund metadata identifies prospective channels but not yet real paired time traces.
4. **Original field KIT OLTC:** its +11.1/+13.8-second delayed state transitions cannot be explained or negated by transferring laboratory EV models, voltage amplitudes, or response timing to a different unknown field charger. Cross-dataset comparison is hypothesis generation only.
5. **Thermal:** no measured EVSE or transformer thermally conditioned capacity reduction has been validated here.

**Decision:** `LAB_U_CURRENT_ASSOCIATION_OBSERVED_4_OF_5_SCREENED | LEAF_SCREEN_QA_OPEN | LAB_CONTROLLER_LOG_NOT_YET_EVALUATED | FIELD_CAUSALITY_OPEN | THERMAL_VALIDATION_OPEN`.

## Next actions

1. Run [locally cached five-vehicle voltage-screen sensitivity analysis](../../../tools/independent_ev_phil_voltage_screen_diagnostics.py) without downloading new large data; report measured Nissan voltage range and sensitivity before labeling its behavior.
2. Identify one **metadata-matched** TU Dortmund selected charging session where actual `ChargingEnabled`/setpoint and grid-side measured P are simultaneously recorded. Download/extract only the needed session from `dataset_merged.zip` if feasible, preserving publisher SHA/MD5 and codebook.
3. Establish commanded setpoint-change timing versus measured output timing, including hold/filter effects and state transitions, under the chosen **independent laboratory** equipment. Do not extrapolate an 11–14 s field delay.
