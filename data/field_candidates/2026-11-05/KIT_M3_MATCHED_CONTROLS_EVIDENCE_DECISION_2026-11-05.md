# KIT M3 matched quiet controls: evidence decision

**Date:** 2026-11-05
**Source evidence:** User-run Mac computation committed directly to GitHub `main` as `76e1efa8` previously for raw 100 ms M2/M3 and later as `70b6c58e` for one-second matched controls. The reported matched-control data were read directly from current GitHub `main` and the computation script reviewed. No original 50-day data were rerun in the assistant environment.

**Primary measured output:** [Matched-control JSON](KIT_M3_MATCHED_QUIET_CONTROLS_V1.json) and [Markdown summary](KIT_M3_MATCHED_QUIET_CONTROLS_V1.md). **Comparator source:** [Python matched-control script](../../../tools/kit_m3_matched_quiet_controls.py). **Original-resolution results:** [100 ms M2/M3 audit](KIT_M2_M3_100MS_MEASUREMENTS_V1.md).

## Results

| Selected voltage event (UTC, 2026-03-10) | Case 20-kV pre/post voltage change (%) | Case EV-point power change (W) | Eligible quiet controls (n) | Control median power change (W) | Case minus median control change (W) |
|---|---:|---:|---:|---:|---:|
| 15:32:02 | +0.710699 | -422.087790 | 4 | +0.067350 | -422.155140 |
| 15:55:02 | -0.714475 | +407.732690 | **0** | Not estimable | Not estimable |

Each case and its controls use the same **derived 1-second** time grid and identical pre (-5 to -1 s)/late (+20 to +30 s) windows. These numbers are **not** the original 100-ms M2/M3 estimates, which were independently retained.

## Source-informed audit

- Both matched cases come from the *same source-labeled fault episode*. They are **not two independent experiments**.
- The controls require the same UTC day, source fault-phase label, uninterrupted finite voltage and power, no absolute 1-second 20-kV step >=0.15% within -20..+30 s, exclusion within 180 s of either selected event, approximately similar pre-voltage and power, stable pre-power and 60-s spacing between selected controls.
- For 15:32:02: 17,270 strided candidate times on the same UTC day; 4,310 quiet voltage windows; 55 pre-power/voltage matches; 52 pass pre-power stability; **only 4** survive the 60-second separation and ranking.
- Those four selected controls are at **15:25:31, 15:26:31, 15:27:31 and 15:28:41 UTC**. Their pre-event real-power medians are **2,414–2,415 W**; the case pre-event real-power median is approximately **2,039 W**. Thus the observed pre-power mismatch is ~**18.4%**, near the deliberately broad **20% tolerance**; the controls should **not be described as tightly load-matched**. Their cases lie close in time within the same fault episode; 60-second separation does not ensure statistical independence.
- Their EV-point power shifts (W) are **+0.60762, +0.00326, -0.51823, +0.13144**. Median +0.06735 W and quartile interval [-0.12711, +0.25049] W from only four selected controls is descriptive; it is **not** a confidence interval or causal counterfactual. An empirical fraction of 0/4 control magnitudes exceeding the case is not a statistical probability of a causal effect.
- For 15:55:02: **zero** candidate controls pass the load and voltage match after other restrictions; this is a legitimate **no-support / positivity-overlap** limitation, not a value to replace or extrapolate.

## Evidence classification

- **M2 cross-voltage:** observed electrical co-variation at 20 kV/EV-meter 400 V (direct feeder parentage unresolved).
- **M3 electrical operation:** observed stable pre-period and later marked EV-point power change. For the first event, relative to four imperfectly matched quiet windows, the selected event shows a much larger change **as a descriptive association only**.
- **Operational Power→Transport physical dependence:** **NOT VERIFIED**. Necessary additional evidence includes verified interface/charger-state mechanism, credible independent comparison or controlled experiment, and competing-control investigation. Time ordering and a four-window observational comparison cannot meet that causal standard.
- **Second event matched-control effect:** **NOT ESTIMABLE** due to zero qualifying controls.
- **Heat/thermal and mobility service:** **NOT MEASURED** by inspected KIT field channels.

## Next bounded scientific decisions

1. Preserve this first comparison unchanged; do not quietly loosen event thresholds or same-date controls after observing results. If sensitivity analyses are conducted, preregister their alternate criteria, version their outputs separately, and report controls with actual loading mismatch and episode clustering.
2. Seek source-controlled charger state/setpoint information or laboratory voltage-perturbation experiments **as a separate installation/evidence stream**. A controlled laboratory finding cannot be merged into KIT's field system as though its feeder or EV model were identical.
3. If independent field-based inference becomes necessary, seek verified feeder/electrical state/topology and controls spanning independently distinct episodes. The user already approved continuing system-level electrical analysis without repeatedly blocking on the missing feeder-specific map, but any branch-specific causal claim still requires it.
4. Keep the core thesis directed toward physical thermal M5 mechanism via measured temperatures, equipment ratings and viable physics-based models; these KIT electrical observations do not validate extreme-heat thermal resilience.

**Decision:** `MATCHED_ANALYSIS_EXECUTED | FIRST_CASE_DESCRIPTIVE_COMPARISON_N4_IMPERFECT_LOAD_MATCH | SECOND_CASE_NO_CONTROLS | CAUSAL_OPERATIONAL_INTERDEPENDENCY_NOT_ESTABLISHED | THERMAL_VALIDATION_NOT_MEASURED`