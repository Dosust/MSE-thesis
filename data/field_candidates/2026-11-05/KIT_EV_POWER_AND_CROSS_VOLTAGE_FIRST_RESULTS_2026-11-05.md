# KIT measured voltage and EV-point power: first quantitative audit

**Date:** 2026-11-05
**Source:** [KIT Zenodo 22826984](https://zenodo.org/records/22826984)
**Execution provenance:** Mac Terminal output pasted by user, calculated from original MD5-verified KIT Parquet data using the [committed analysis script](../../../tools/kit_oltc_electrical_response_analysis.py). This is **not** an independent raw-data rerun.
**Related checkpoint:** [Full original-file analysis](KIT_OLTC_ELECTRICAL_RESPONSE_EXECUTION_CHECKPOINT_2026-11-05.md).
**Status:** FIRST QUANTITATIVE ELECTRICAL FINDINGS, not a thermal model validation.

## 1. Verified finite one-second quantities

All fields are derived finite-only one-second arithmetic means from the original 100 ms electrical measurements; their nominal timeline contains 4,320,000 seconds each.

| Measured derived field | Finite one-second values | Completeness |
|---|---:|---:|
| 110 kV u_pos[V] | 3,780,412 | 87.51% |
| 20 kV u_pos[V] | 3,797,724 | 87.91% |
| 400 V EV three-phase mean voltage | 4,318,576 | 99.97% |
| 400 V EV sum of three-phase active powers | 4,318,576 | 99.97% |
| 20 kV i_pos[A] | 3,797,724 | 87.91% |
| 110 kV p[MW] | 3,777,341 | 87.44% |

EV source raw nonfinite count: 32,921 100 ms samples for **each** original 400 V voltage, active-power and reactive-power phase column. Each underlying phase produced 4,318,576 finite one-second means. A finite mean may contain fewer than ten valid 100 ms samples, so these percentages are **derived-bin availability**, not complete raw-sample QA. These identical counts do not prove invalid samples coincide in time.

## 2. Observed EV active power at the selected 20 kV events

- Candidate voltage events selected by original analysis: **60**. This is a maximum-capped exploratory event subset, not an observed total count of all disturbances.
- Pre-event EV power medians finite: **60/60**.
- Maximum absolute selected pre-event EV three-phase real power: **0.00376885 kW = 3.76885 W**.
- Pre-event |P_EV| >= 500 W: **0/60**.
- The 500 W threshold is software screening only; actual charger state and power sign convention are unverified.
- Therefore the zero flags are **not due to invalid pre-event power medians**. All 60 exist and are unusually small relative to active EV charging power. This does **not** establish no charge event anywhere in 50 days or prove meter scaling/sign.

## 3. First five actual measured event-response rows

The source user Terminal output reports the following independently normalized pre/post medians (pre -20 to -6 seconds; post +5 to +19 seconds), NOT the instantaneous one-second step itself:

| UTC event | Phase label | Delta U110 % | Delta U20 % | Delta U400 % | Pre EV P (kW) | Delta EV P (kW) |
|---|---|---:|---:|---:|---:|---:|
| 2026-02-22 12:25:15 | pre_fault | +0.05046695 | +0.05192761 | +0.21042811 | +0.00238844 | +0.00005807 |
| 2026-02-26 06:41:52 | pre_fault | -0.10167895 | +1.25616016 | +1.43058411 | +0.00275738 | -0.00016361 |
| 2026-03-04 10:40:23 | pre_fault | +0.03782186 | -1.29686204 | -1.29534238 | +0.00294781 | +0.00010906 |
| 2026-03-05 16:32:59 | fault | -0.04827586 | -0.70095302 | -1.14909324 | +0.00253306 | +0.00000221 |
| 2026-03-05 19:08:57 | fault | -0.01568645 | -0.67328374 | -0.47900449 | +0.00281498 | +0.00015749 |

At several selected events, the 20 kV and 400 V relative voltage variations have similar signs and percent magnitudes while 110 kV changes are smaller. These are **descriptive co-responses**, not physical causal transfer/feeder proof. The EV power deltas above are extremely small fractions of a watt.

## 4. Next scientific gate: whole-record EV power range

Use the existing local derived file at Downloads/KIT_OLTC_Electrical_Results/ev400_1s.parquet. No rerun of the original 129.6 million 100 ms samples is necessary.

For every finite complete three-phase one-second entry, calculate sum(p_L1_W, p_L2_W, p_L3_W), signed minimum/maximum, maximum absolute watts, its UTC timestamp, finite sample count, and counts at absolute >=100 W, >=500 W, >=1,000 W and >=3,000 W. Show representative times above 500 W if present.

**If larger values exist elsewhere:** the selected 60 voltage-step events did not sample them in their pre-windows; inspect overlaps with charging-point load state rather than declaring the charger inactive.

**If power never reaches 100 W:** this observed 400 V EV-point series cannot serve as a measured substantial active-charging power example at face value; check source sensor definitions, unit scaling and channel semantics. Do not invent corrections.

## 5. Scientific limits and authority

- The original three files have measured electric variables, **not** temperature/ambient/thermal power derating or battery SOC.
- The 20 kV file has voltage/current but no measured active-power column.
- The source fault-phase labels require documentary interpretation and voltage phase conventions remain to be checked.
- The exact PMU/EV feeder ancestry is unverified but not a prerequisite for user-authorized system-level cross-voltage descriptions.
- The observations do not validate directional extreme-heat thermal SO1-SO3 mechanisms or mobility service resilience.
- Governed by [current scope](../../../project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md) and [non-invention rule](../../../project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md).

**Original numerical provenance:** user's Terminal report on November 5, 2026. Full raw bytes and output files remain user-local; no GitHub claim of original field-data upload.
