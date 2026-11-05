# KIT independent PHIL voltage-screen sensitivity audit

**Distinct from the 50-day KIT campus field data.**

| Vehicle | Whole-run mean voltage span (V) | Screened 2 V transitions | Pre/post near t=0 ΔU (V) | Qualification |
|---|---:|---:|---:|---|
| Volkswagen ID.4 | 40.097 | 16 | -5.0033 | TWO_VOLT_EVENT_SCREEN_RETURNED_CANDIDATES |
| Nissan Leaf | 13.420 | 0 | -1.66 | NO_2V_EVENTS_DESPITE_GT_2V_RUN_RANGE_REQUIRES_SCREEN_QA |
| MG4 | 40.183 | 16 | -5.0033 | TWO_VOLT_EVENT_SCREEN_RETURNED_CANDIDATES |
| Tesla Model 3 | 40.037 | 16 | -5.0133 | TWO_VOLT_EVENT_SCREEN_RETURNED_CANDIDATES |
| Renault Zoe | 40.643 | 16 | -5.01 | TWO_VOLT_EVENT_SCREEN_RETURNED_CANDIDATES |

See JSON for thresholds 0.5, 1.0, 1.5, 2.0, 3.0 and 5.0 V, per-vehicle sample coverage and largest 1 s voltage change.

A zero at the 2 V screen is NOT by itself a finding of no voltage perturbation, charging interruption, or a particular car controller response.
