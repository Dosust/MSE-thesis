# KIT 110/20/400 V electrical-response first measured execution checkpoint

**Date:** 2026-11-05  
**Status:** **USER-LOCAL ORIGINAL-SOURCE ANALYSIS EXECUTED SUCCESSFULLY**. Quantitative selected-event electrical effects still require inspecting actual output CSV/JSON and validation.  
**Source:** KIT OLTC multivoltage measurement dataset: https://doi.org/10.5281/zenodo.22826984  
**Executable:** [kit_oltc_electrical_response_analysis.py](../../../tools/kit_oltc_electrical_response_analysis.py)  
**Protocol:** [KIT_OLTC_ELECTRICAL_RESPONSE_ANALYSIS_PROTOCOL_V1.md](KIT_OLTC_ELECTRICAL_RESPONSE_ANALYSIS_PROTOCOL_V1.md)  
**Source integrity:** [KIT original MD5 and full 129.6M timestamp-grid audit](KIT_OLTC_22826984_ACQUISITION_AUDIT.md).

## 1. Provenance of the present results

The user ran the real-data Python program against three previously downloaded, publisher-MD5-verified Parquet files on their MacBook and pasted its Terminal completion output into the thesis conversation. The original bytes and generated output files have **not been uploaded to GitHub or the assistant runtime**. These results are **user-terminal-reported**, not an independent reexecution or verified review of the CSV/JSON data.

**Input folder:** `~/Downloads/KIT_OLTC_22826984/`  
**Output folder:** `~/Downloads/KIT_OLTC_Electrical_Results/`  
**Invocation (from preceding step, unless user changed arguments):**

~~~bash
python3 "$HOME/Downloads/KIT_OLTC_22826984/kit_oltc_electrical_response_analysis.py" \
  --folder "$HOME/Downloads/KIT_OLTC_22826984" \
  --out "$HOME/Downloads/KIT_OLTC_Electrical_Results" \
  --step-threshold-pct 0.15 \
  --max-events 60
~~~

## 2. Execution output confirmed from user Terminal

All three input files were streamed into one-second bins:

| Original sensor file | Checkpoint excerpts | Expected completed one-second bins |
|---|---|---:|
| oltc_fail_110kV_PMU04_TK1_100ms.parquet | 500,000; 1M; ...; 4M computed | 4,320,000 |
| oltc_fail_20kV_PMU01_J01_100ms.parquet | 500,000; 1M; ...; 4M computed | 4,320,000 |
| oltc_fail_400V_EV_SH.J.6_100ms.parquet | 500,000; 1M; ...; 4M computed | 4,320,000 |

The program proceeded through the full-run final summary and returned to the user's normal shell prompt, **without a reported error**. Each original source has 43,200,000 records and was previously row-grid-verified, for a total **129,600,000 original 100 ms observations** used as input. The exact derived row counts and missingness are recorded in the generated `analysis_summary.json`; that file has **not yet been inspected**.

**Terminal final summary, as supplied:**

~~~text
--- SOURCE-GROUNDED KIT ELECTRICAL RESPONSE ---
Original: https://doi.org/10.5281/zenodo.22826984
Candidate 20 kV voltage steps: 60
Events with substantial pre-event EV real-power exchange: 0
Source fault-phase labels (seconds): {'pre_fault': 2464800, 'fault': 592560, 'post_fault': 1262640}
Results: /Users/dossiyadakou/Downloads/KIT_OLTC_Electrical_Results
CONSTRAINT: electrical response only; NO inference of heat-induced derating or exact feeder causality
~~~

## 3. Meaning of the 60 selected voltage-step candidates

The analysis script [event_candidates function](../../../tools/kit_oltc_electrical_response_analysis.py) selects events where the absolute consecutive one-second change in measured `u_pos[V]` at 20 kV is at least **0.15%**, ranks by step magnitude, keeps candidates at least **45 seconds** apart, and stops after at most **60** events. These threshold/separation/cap values are **exploratory software parameters**, **not measured equipment protection limits** or physical tap-change confirmations.

**Therefore:** exactly 60 selected candidates were reported, **not** proof that only 60 20-kV disturbances happened during the 50-day record. The source `fault_phase` labels are operational annotations; their sensor/control semantics require publisher verification.

The reported 1-second fault-phase label counts are:
- `pre_fault`: **2,464,800 seconds**.
- `fault`: **592,560 seconds**.
- `post_fault`: **1,262,640 seconds**.

These counts span the one-second dataset. They do not establish that the 60 strongest candidate events fell in a particular phase; the **event_metrics.csv** should be inspected for this.

## 4. Exact meaning of zero substantial pre-event EV power

The script defines `ev_significant_exchange_pre` for each **selected event**, not for every day or every charging session:

- Aggregate original EV-phase active-power fields `p_L1[W] + p_L2[W] + p_L3[W]` after one-second averaging, **only when all three phase values are finite**.
- For each candidate event at second `i`, take the **pre-event median** over `i-20` through `i-6` seconds, inclusive.
- The Boolean is true **only if** this median is finite and its absolute value is **at least 500 W** (software screening threshold).
- **User-terminal result:** **0 out of the 60 selected candidates** passed that condition.

**Unknown pending data inspection:** Whether those 60 median values are missing/non-finite, exactly zero, below 500 W, above 500 W in *post* windows only, or otherwise affected by source power signal semantics. It is **incorrect** to conclude from this printout that the EV never charged, charger operation was absent during the entire 50-day window, or voltage disturbances never affected EV power.

**Other unresolved interpretation:** the source power-sign convention and EV charge/discharge/standby semantics have not been verified. Do not describe an absolute-power flag as verified battery charging activity.

## 5. What is already supported, what is not

**Supported (at this evidence level):**
- Full original-source stream and one-second aggregate analysis completed on the user Mac, with no reported exception.
- The 60-event selection limit was reached under stated default exploratory settings.
- Zero of the selected events met the stated pre-window real-power magnitude and validity criterion.
- Fault-phase label distribution was reported at one-second granularity.

**Not yet supported:**
- Specific numerical 110/20/400-V voltage change values or EV `ΔP` from the actual event CSV.
- Whether the 60 selected events coincide with observed EV charging.
- Any inference of real power at the 20-kV point, which has only voltage and current fields.
- Branch-specific physical causality, heat-induced EVSE derating, measured transformer/EVSE temperature, thermal state trajectories or SO1–SO3 validation.
- Reliable model accuracy, generalization or uncertainty from a single selection-and-report pass.

## 6. Next action: inspect already computed results (no rerun)

Print concise JSON metadata and CSV examples from:

~~~text
~/Downloads/KIT_OLTC_Electrical_Results/analysis_summary.json
~/Downloads/KIT_OLTC_Electrical_Results/event_metrics.csv
~~~

Check `measured_signal_valid_1s_counts`, `files[*].nonfinite_measurement_statistics`, `event_selection`, and per-event `ev_power_pre_kW`, `ev_power_post_kW`, `ev_power_delta_kW`, `u110_change_pct`, `u20_change_pct`, `u400_change_pct` and `fault_phase_label_at_event`. These differentiate absent EV-point power, invalid signals and non-overlap with the 60 selected voltage events. Check whether source phase signals are in W and what sign denotes charging at this meter.

**Do not rerun original 129.6M-row aggregation merely to inspect existing output.** Preserve the measured data and synthetic test distinction.

## 7. Status

`USER_LOCAL_ORIGINAL_ANALYSIS_COMPLETE | SELECTED_EVENTS_60 | PRE_EVENT_EV_500W_FLAG_0 | EVENT_QUANTIFICATION_REVIEW_PENDING | THERMAL_VALIDATION_NOT_ESTABLISHED`

This dated record is a **working execution log**. It does not amend the frozen official thesis title, scope or SO1–SO3 authorities.
