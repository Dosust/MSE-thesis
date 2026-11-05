# KIT 110/20/400 V responses during high EV-point real-power operation

**Date:** 2026-11-05
**Research status:** First measured source-conditioned electrical responses **QUALIFIED** (descriptive only; not physics/thermal causal validation).
**Provenance:** User-pasted Mac Terminal output of the [GitHub source analysis script](../../../tools/kit_ev_power_conditioned_voltage_events.py) run on 1-second mean Parquet derivatives of original KIT OLTC measurements; raw original 100 ms data previously passed publisher MD5 and strict 129.6 million record UTC timestamp-grid QA. This GitHub summary is **not** an independent re-execution of the local data.
**Original dataset:** https://doi.org/10.5281/zenodo.22826984.
**Earlier reports:** [full 50-day EV-point power](KIT_EV_POWER_FULL_RECORD_FINDINGS_2026-11-05.md), [earlier top-step event screen](KIT_EV_POWER_AND_CROSS_VOLTAGE_FIRST_RESULTS_2026-11-05.md).

## 1. Reported run outcomes

| Criterion / calculation | User Terminal observation |
|---|---:|
| One-second 20 kV absolute positive-sequence voltage steps >=0.15%, excluding 30-second boundary windows | **45,789** |
| Steps with finite EV-point pre-event median power | **45,789** |
| Steps with finite median absolute pre-event EV-point three-phase power >=500 W | **159** |
| Independent selected candidates with minimum 45-second separation and ranked by largest one-second 20-kV step | **60** |
| Selected events with all six finite 110/20/400 V pre/post medians | **60** |

- Computed fraction with substantial power at their pre-event windows: **159 / 45,789 ≈ 0.347%** of one-second voltage-step candidates.
- **IMPORTANT CENSORING:** 60 is exactly the user's configured `--max-events 60`; it is **not** the measured total number of independent qualifying steps. The script ranks 159 power-conditioned candidates by absolute 20-kV voltage-step size, excludes accepted candidates within 45 s, then truncates to at most 60.
- 60/60 finite pre/post voltage medians **does not imply** every single one-second input in each pre/post window is valid, nor does it confirm 60/60 finite **post-event power**; that field must be checked in the output CSV.
- Trigger magnitude at a single adjacent one-second voltage pair is **not** the same metric as pre-event (-20 to -6 s) versus post-event (+5 to +19 s) median voltage change.

## 2. Actual first five event rows

| Time UTC | Source phase label | 1 s 20 kV step magnitude % | EV-point signed pre P W | EV-point signed delta P W | Delta U110 % | Delta U20 % | Delta U400 % |
|---|---|---:|---:|---:|---:|---:|---:|
| 2026-02-09 12:57:51 | pre_fault | 0.16599634 | 8405.07181 | +356.84471 | +0.01079776 | +0.02520488 | +0.13672265 |
| 2026-02-09 15:34:20 | pre_fault | 0.16181407 | 1549.45539 | +0.21659 | -0.01455549 | -0.01945438 | -0.03974856 |
| 2026-02-09 15:36:13 | pre_fault | 0.16112852 | 1549.60554 | +0.22878 | -0.08758008 | -0.08627747 | -0.05586703 |
| 2026-02-09 15:47:49 | pre_fault | 0.19650262 | 785.71312 | +390.11326 | -0.01665258 | -0.02094289 | -0.01759989 |
| 2026-02-12 13:13:34 | pre_fault | 0.17697946 | 8362.31214 | +13.91834 | +0.09841641 | +0.07056944 | +0.07158092 |

Each voltage delta is relative to **its own pre-event median**, which avoids comparing physical volts at different voltage levels as transformer ratios. The 400-V signal uses arithmetic mean of three measured phase voltages and the EV-point power uses sum of three measured phase powers only when all are finite. The source's phase and power-sign/meter semantics require source qualification.

### Methodology check against exact GitHub script

- `select_conditioned_events`: scores |100*(U20[t]-U20[t-1])/U20[t-1]| after filtering invalid/nonpositive consecutive U20, screening at 0.15%; excludes t<30 and t>=N-30.
- Computes pre-event EV-point median from samples t−20 through t−6; requires finite absolute power >=500 W **before** ranking/capping.
- Sorts qualifying candidates by strongest instantaneous 20-kV step, enforces >=45 s minimum between accepted events, stops at selected cap 60.
- `make_result_row`: compares pre t−20..t−6 with post t+5..t+19 medians. Source fault-phase annotation at t comes from the 20 kV dataset. It verifies all six voltage medians finite but does not assert all individual samples within windows are present.
- `ev_delta_power_W_signed` is post-window EV-point power median minus pre-window EV-point power median, **not** a confirmed causal effect or signed battery charging rate.
- The first five displayed events all carry `pre_fault`. **Do not infer that all 60 occur in pre_fault** until the complete event CSV is summarized.

## 3. Scientific interpretation

**New positive evidence:** A subset of 20-kV 1-second voltage step candidates coincides with substantial measured EV-point real-power exchange in the pre-event windows, allowing descriptive cross-voltage electrical response analysis of 110/20/400 V during nontrivial EV-point electrical operation.

**Why this resolves earlier zero:** The initial top-60 strongest-voltage-step screen yielded 0/60 with >=500 W pre-event power. **Applying the EV-power criterion before the top-60 ranking** reveals 159 eligible candidate one-second steps and 60 selected spacing-qualified events. Neither result contradicts the other; the event sampling schemes differ.

**Critical restraint:** The 20 kV and 400 V channels are from the same campus electrical system on the same 100 ms measurement grid, but the dataset output does not alone prove branch-specific feeder causation. Neither a simultaneous step nor a changing EV power reading establishes that the electrical step caused the power change. The source anomaly is electrical OLTC regulation, not an observed extreme-heat thermal disturbance. Thermometer/thermal derating, battery SOC, demand-by-departure and measured mobility service remain absent in the inspected original Parquet variables.

**Present thesis evidence gate:** ELECTRICAL P↔T_e SUPPORTING OBSERVATIONAL DATA; THERMAL SO1–SO3 FIELD VALIDATION NOT ESTABLISHED.

## 4. Next rigorous use of existing output files (no raw reread)

Files produced locally by the user's run:
- ~/Downloads/KIT_OLTC_Electrical_Results/power_conditioned_voltage_step_summary.json
- ~/Downloads/KIT_OLTC_Electrical_Results/power_conditioned_voltage_step_events.csv

1. From all 60 selected events, count source phase labels, check finite **post-event power** and `ev_delta_power_W_signed`, and report median/IQR of voltage changes and power changes with actual sample sizes and the proportion of positive versus negative power shifts.
2. Assess event classification against `fault_phase` metadata and physical plausibility of source voltage magnitudes, power units/sign and meter operating-state context; avoid treating the source labels as independently measured OLTC tap commands.
3. Evaluate **selection sensitivity** to arbitrary step threshold, 45-second spacing and max-60 truncation. If the aim is to count every eligible independent event, repeat only this read of the derived one-second summaries with `--max-events 200` in an evidence-preserving output copy to avoid overwriting the initial 60-event results.
4. For a specific physically interpretable case, inspect original high-resolution 100 ms windows to verify electrical event morphology and local timing; never interpret 1 s means as subsecond propagation timing.
5. Thermal SO1–SO3 validation still requires separate measured thermal/heat/derating data or documented physics-based simulation with explicit limitations.

**Do not upload user original multi-GB Parquet files to GitHub; preserve on MacBook.**

## 5. Follow-up: all 60 selected event EV power deltas (user Terminal)

**Evidence source:** User-pasted Terminal result of a CSV summary applied to the local `power_conditioned_voltage_step_events.csv`, created by the source-constrained program. These are reported results, **not** an independently re-read/uploaded CSV.

| Reported statistic | Value |
|---|---:|
| Selected events | 60 |
| `pre_fault` event labels | 28 |
| `fault` event labels | 31 |
| `post_fault` event labels | 1 |
| Finite signed pre/post EV active-power deltas | 60 / 60 |
| Median **signed** EV-point pre/post power delta | **+0.38806 W** |
| Events with **absolute** EV-point power delta >=100 W | **10 / 60 (16.7%)** |
| Events with **absolute** EV-point power delta >=500 W | **1 / 60 (1.7%)** |

**Correct reading:** The selected event set includes measurable EV-point real-power variations, and a minority exceed exploratory magnitude thresholds. A near-zero *signed* median **does not** demonstrate there is no large response, no effect, no variation, or no charging; use the entire empirical signed/absolute distribution. The event that exceeds 500 W has not yet been identified from its exact time, power before/after or voltage morphology.

**Method:** `ev_delta_power_W_signed` is the post-window (event +5..+19 s) finite median minus pre-window (event -20..-6 s) finite median, based on the 1-second average of sum-of-three measured phase power channels; +/-100 W and +/-500 W are *descriptive selection summaries*, not device thresholds. There is no causal treatment/control, no observed battery charging-state ground truth and no verified thermal variable.

**Phase caveat:** 31 `fault` and 28 `pre_fault` vs only one `post_fault`; the group sizes are dominated by prior event screening and capped, nonrandom selection. Do not compare phase impacts as if samples were balanced or randomly drawn. Source labels are documentation metadata, not necessarily tap-command telemetry.

**Next diagnostic:** Use existing CSV only to list **all 10 rows with |deltaP_EV| >=100 W**, including exact UTC, source phase label, signed before/after power and delta, one-second trigger magnitude, and pre/post 110/20/400 voltage percent changes. In particular investigate the **one |deltaP| >=500 W** event. Verify whether those events reflect charging transitions, ordinary load changes, 1-second averaging artifacts, or a possible voltage-related response; event correlation alone cannot distinguish them.

**Scientific status:** synchronized measured power-voltage co-variation demonstrated; directional power-to-transport causation, EV charging-state confirmation, mobility-service effects and heat-driven state-time thermal SO1–SO3 **NOT ESTABLISHED**.
