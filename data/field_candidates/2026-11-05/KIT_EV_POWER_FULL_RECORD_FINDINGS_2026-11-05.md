# KIT measured EV-point real-power distribution — full 50-day audit

**Date:** 2026-11-05
**Scientific classification:** Actual Mac-local measured electrical observations from the original KIT multivoltage OLTC data, as reported in the user's Terminal transcript; not independently reproduced in the GitHub/ChatGPT runtime.
**Source:** https://doi.org/10.5281/zenodo.22826984
**Processing:** [GitHub diagnostic script](../../../tools/kit_ev_power_50day_diagnostic.py) on user-local precomputed `ev400_1s.parquet` (1-second finite-only 100 ms averages).
**Related:** [first voltage events and selected power measurements](KIT_EV_POWER_AND_CROSS_VOLTAGE_FIRST_RESULTS_2026-11-05.md).

## Verified-from-user-Terminal results

- Terminal confirmed GitHub repository `git pull`: `Already up to date.`
- Program built-in check: `PASS: synthetic self-test; not a measured KIT finding`.
- **Valid 1-second EV-point real-power entries:** 4,318,576 (derived from the measured three phase power channels).
- **Minimum signed measured total three-phase power:** -3.64297 W.
- **Maximum signed measured total three-phase power:** 9,628.0013 W.
- **Maximum absolute measured power:** 9,628.0013 W, at **2026-03-03T12:15:33+00:00**.
- **Seconds with |P| ≥ 100 W:** 101,951 (2.360755% of valid 1-second entries).
- **Seconds with |P| ≥ 500 W:** 101,930 (2.360269% of valid 1-second entries; 28.3139 hours of sampled seconds).
- **Seconds with |P| ≥ 1,000 W:** 100,211 (2.320464% of valid 1-second entries).
- **Seconds with |P| ≥ 3,000 W:** 85,703 (1.98452% of valid 1-second entries).
- Earliest five printed examples with ≥500 W begin **2026-02-09T12:19:30+00:00** and show measured 5,904.18195 W, 7,879.25976 W, 7,947.77909 W, 8,007.05802 W, 8,024.10236 W, labeled `pre_fault` by the source.
- Program reported JSON file under Mac path `~/Downloads/KIT_OLTC_Electrical_Results/ev_power_50day_diagnostic.json`; the file was **not uploaded into this conversation or GitHub**.

## Interpretation

**Established:** The original EV-labeled measurement point recorded substantial active electrical power exchange in parts of the 50-day interval. This **resolves** the earlier concern that the EV-point power channel might record only a few watts throughout the dataset.

**Previously measured:** The 60 strongest 20 kV one-second step candidates selected by the separate capped event-screening algorithm all had finite **pre-event** EV power medians, with maximum |P| of only **3.76885 W** and 0/60 pre-event means exceeding 500 W. The source can therefore show substantial EV-point power elsewhere without those two findings contradicting each other.

**Unresolved:** Whether qualified 20 kV voltage-disturbance events overlap with the **higher-power** EV operating intervals, including the relevant pre/post windows; exact meter sign convention, battery-side charging activity, feeder parentage and thermal states remain not independently verified.

**Not admissible:** Equating ≥500 W with a definitively verified battery charging state; inferring equipment thermal derating, directionally causal feeder propagation or improved/degraded mobility service from power alone.

## Next test: power-conditioned voltage-event screening

Run a **new targeted analysis of already generated `grid20_1s.parquet`, `grid110_1s.parquet` and `ev400_1s.parquet`**. For each 20 kV one-second step candidate meeting the existing **0.15% exploratory threshold**, distinguish whether the **pre-event median** of the measured EV-point total real power (seconds -20..-6) has finite magnitude ≥500 W. Count the number of eligible candidate disturbances during active-power periods **before** applying an arbitrary top-60 cap, keep independent candidates at least 45 seconds apart, calculate pre/post 110/20/400 V responses and EV power delta only when valid. If none exist, report zero transparently. If they exist, analyze them without implying causal or thermal field validation. No original 129.6M record rerun.

**Scope authority:** [Thermal interdependency scope](../../../project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md), [Evidence standard](../../../project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md).

**Checkpoint:** Whole-record EV measured power proven to reach ~9.6 kW; overlap with qualified voltage steps remains **PENDING**.