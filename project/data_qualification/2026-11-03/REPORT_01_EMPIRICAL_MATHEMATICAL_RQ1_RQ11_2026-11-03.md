# REPORT 1 — Empirical and Mathematical Questions RQ1–RQ11

**Study:** Engineering of Power–Electrified Transportation Interdependencies for Resilience  
**Date:** 2026-11-03  
**Status:** **EVIDENCE-QUALIFIED WORKING REPORT — NOT COUPLED FIELD VALIDATION**  
**Scope authority:** `project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md` (SO1–SO3 frozen; RQ1–RQ11 are supporting investigations, **not** replacements for the frozen questions and not a new mandatory optimization objective).

**Version relation:** Consolidates [previous Report 1 RQ1–RQ7](./REPORT_01_MEASURED_DATA_RQ1_RQ7_2026-11-03.md) with new source-MD5-verified transformer numerical analyses for RQ8–RQ10 and a new, explicitly **exploratory** OSF original-file RQ7 event-window screen. The previous report remains preserved for audit. This report supersedes it as the current **Report 1 answer summary**. It does not modify or reuse measured rows from separate installations as though they were co-located.

## Executive answer: what can be answered now?

| RQ | Numerical / scientific answer | Status |
|---|---|---|
| **RQ1** Transformer ambient, electrical forcing, and temperature | SINTEF (8,592 h): top-oil vs ambient Pearson `r=0.9658`; top-oil vs unadjusted squared current `r=-0.8007`. The negative association does **not** mean current cools a transformer; seasonality and operation confound it. | **Measured association**; physical causal decomposition unproven |
| **RQ2** Physics-constrained transformer temperature prediction | Chronological October–December test: 1-h top-oil `RMSE=0.2147°C`, persistence `0.2480°C`; **MAE worse** (`0.1469` vs `0.1409°C`). Conditional 6-h RMSE `0.6547` vs `1.0209`; 24-h `0.9366` vs `2.1338°C`. | **Same-site conditional hindcast**, not an exogenous operational forecast |
| **RQ3** Operational P/Q variation | STREAM Slovenia: 12 anonymized stations × 34,932 common 15-min UTC records = **419,184 station-time paired P/Q**. Negative P fraction `6.392%`; negative Q fraction `46.566%`. | **Measured electrical operation**; sign, physical units and ratings unverified |
| **RQ4** EV charging V/I/SOC/temperature | KU Leuven C5PT0R four AC CSVs total **40,873 row records**. In Figure7_AC1, first/last 120-record median SOC `39.0→90.3%` and battery maximum temperature `30.25→28.75°C`. | **Vehicle component behavior**, not charger rectifier temperature; other files have clock reversals |
| **RQ5** EV electrical input–output differences | KU Leuven Figure10 DC high-power windows: `P_DC/P_AC=0.92635` (87 records), `0.92691` (116 records); median `P_AC−P_DC=3.589` and `3.549 kW`. | **Provisional electrical boundaries**, not measured equipment heat rejection |
| **RQ6** EV charging influence on grid demand/forecast accuracy | OPSD supplies same-premises grid and EV channels; earlier audit counted **116,355** qualified 15-min intervals at two locations. **No independent forecasting comparison or incremental accuracy estimate is available here** because original rows were not accessible to this analysis. | **NOT QUANTITATIVELY ANSWERED** |
| **RQ7** PQ disturbances and battery electrical response | OSF original 313-CSV nested archive checked. Using strict, file-named `t=20s` event windows and 2–30-s durations, **61 / 74** candidate experiments had active, sufficiently sampled paired battery V/I signals. Across 61, median change in `|I_batt V_batt|` between [10,20) s and the named event window was **−7.881%**; **32/61 (52.46%)** decreased by at least 5%. | **New exploratory temporal association only**; experimental timing/controls and independent causality still unverified |
| **RQ8** Identifiability of thermal parameters | For `T_{k+1}=T_k+a(T_a−T_k)+b(I/I_ref)^2+c`, full Jan–Jun fit `(a,b,c)=(0.080746,0.069367,1.084335)` at hourly step and `I_ref=29.375 A`. Jan–Mar `a=0.04938,c=0.58762` versus Apr–Jun `a=0.11295,c=1.54877`. Full-model test 1-h RMSE `0.21468` vs ambient-plus-constant `0.21921°C`. | **Coefficients estimable numerically** but **individual physical parameters and cross-season invariance NOT established** |
| **RQ9** Prediction sensitivity / UQ | Deterministic conditional 24-h sensitivity: sustained **+5°C** ambient-forcing offset gives **+4.337°C** predicted top-oil change, other forcing fixed. ±10% `a`: median abs output changes **1.20–1.37°C**; ±10% `b`: **0.115°C**; ±10% `c`: **1.165°C**. | **Executed one-at-a-time sensitivity**, **not probabilistic UQ or extreme-heat validation** |
| **RQ10** Operating validity and transferability | Measured SINTEF ambient `[-19.58,+25.97]°C`, current `[8.4125,75.1025] A`, top-oil `[3.8275,38.86]°C`. October–December 1-h test: 263 ambient ≤0°C, 1,482 in (0,10]°C, 413 in (10,20]°C, **zero >20°C**. | **Single-site observed-domain validation only**; no independent cross-site or extreme-heat transfer |
| **RQ11** Thermal constraints and required service | A coupled viability/service formulation can be written (Section 11) with transformer/EVSE thermal states, power limits, required energy and charging deadlines. **No numerical field-derived service availability, interdependency propagation delay or safe control can be claimed.** | **CONDITIONAL MATHEMATICAL PROPOSAL ONLY** |

**Scientific bottom line:** RQ1–RQ5 now have previously audited component results; RQ7 has a newly executed but limited raw-data screen; RQ8–RQ10 have new reproducible transformer-only experiments; RQ6 remains numerically blocked; RQ11 is symbolic. **None establishes an observed extreme-heat, physically connected transformer–EVSE thermal cascade or cross-site transferability.**

---

## 1. Research materials, authentication and separation

### SINTEF original, source integrity PASS
[SINTEF Bærug 2024, DOI 10.5281/zenodo.17223516](https://doi.org/10.5281/zenodo.17223516). The directly processed original `Barug2025_sensordata.csv` has 8,592 rows. **Verified original MD5 `5d81840a2f901f04fded98c3e1097b6e`**. The RQ8–RQ10 script checks this hash before running. The original raw data remain unchanged.

### STREAM Slovenia: separate location and units gate
[Publisher DOI 10.5281/zenodo.20927130](https://doi.org/10.5281/zenodo.20927130) supplies the operational 2025 P and Q time series. Verified in the [source audit](./SLOVENIA_STREAM_SINTEF_RAW_AUDIT_2026-11-03.md). Original P and Q file MD5s match publisher records. No inference about transformer overload until unit/sign, 12-station ID crosswalk and rated capacity from [companion DOI 10.5281/zenodo.20927801](https://doi.org/10.5281/zenodo.20927801) are confirmed.

### KU Leuven: separate AC and DC measurement boundaries
[KU Leuven C5PT0R, DOI 10.48804/C5PT0R](https://doi.org/10.48804/C5PT0R), source ZIP checksum and ten-payload MD5 verified in [archive audit](./UPLOADED_ARCHIVES_QUALIFICATION_2026-11-03.md). This is **not** the previously investigated KU Leuven 8KPDTW dataset; independence of the sessions/hardware has not been proved. Source-file timestamp resets and a possible DC2 current/voltage column swap remain open.

### OSF: raw ZIP acquired and event-response recomputed here
[Li et al. laboratory data OSF 94GKC](https://doi.org/10.17605/OSF.IO/94GKC), [Scientific Data article](https://doi.org/10.1038/s41597-026-06768-5). Original user-uploaded outer ZIP contains a nested original research ZIP with **313 CSV experiments**, plus validation-code ZIP. Outer ZIP SHA256 `38af5d53ff8779b75a746c6d5b29d13c84bedccf21793bdad308ba828151b707`. This is real controlled single-phase AC charging under deliberately applied PQ disturbances; **not an EVSE temperature or transformer heatwave dataset**. Different CSVs have different schemas and missing CAN fields.

### OPSD: available source but no new raw-run confirmation
[OPSD Household Data v2020-04-15](https://data.open-power-system-data.org/household_data/2020-04-15/) is a metered-plus-processed household package. Publisher documents interpolated/filled gaps; nominal 15-min feed values are **interval energy (kWh)**, not instantaneous kW. Do not calculate grid/EV power or forecast skill without rows, interpolation flags, timestamps and a no-lookahead train/test protocol.

No measurement from one source has been synchronized to another source as a common installation.

---

## 2. RQ1 — Transformer electrical forcing versus thermal states

Original SINTEF observational correlations: `r(T_top_oil,T_ambient)=+0.9658` and `r(T_top_oil,I²)=−0.8007`, 8,592 sampled hours. This is a comparison of **absolute levels** across seasonality, not identification of current-induced heating. The thermal balance requires an appropriate positive Joule/stray loss contribution with delayed heat exchange. Temperatures, loading, operating state, measured forcing and sensor errors need joint dynamic identification before assigning physical causal coefficients.

**Answer:** Ambient and oil states co-vary strongly in this installation; unadjusted loading correlation is confounded. See the full six-sensor and lag analysis in the prior Report 1.

## 3. RQ2 — Physically constrained conditional temperature prediction

Adopted 1-hour empirical Euler equation:

```math
T_{k+1}=T_k+a(T_{a,k}-T_k)+b(I_k/I_\mathrm{ref})^2+c
```

with `0≤a≤1`, `b,c≥0`, fit Jan–Jun, residual-calibration period Jul–Sep, held-out Oct–Dec. The intercept `c` folds together unobserved heat sources/model mismatch; individual thermal resistance/capacitance are **not independently measured**.

| Horizon | Qualified starts | Model RMSE °C | Persistence RMSE °C | Model MAE °C | Persistence MAE °C |
|---|---:|---:|---:|---:|---:|
| 1 h | 2,158 | **0.2147** | 0.2480 | 0.1469 | **0.1409** |
| 6 h | 2,148 | **0.6547** | 1.0209 | **0.4548** | 0.7138 |
| 24 h | 2,112 | **0.9366** | 2.1338 | **0.6870** | 1.6462 |

The 6/24-hour recurrence was supplied with **future observed** ambient and current; the results are conditional hindcasts, not ex-ante forecasts. Multi-horizon start windows overlap; errors must not be treated as independent. The 1-h test MAE being worse than persistence is a genuine model limitation.

**Answer:** The mathematical dynamics improve RMSE within these observed forcing conditions, without validating heatwave operation, other transformer types or the individual physical coefficient meanings.

## 4. RQ3 — Transformer station P and Q variability

From Slovenian 2025 originals, 12 stations × 34,932 15-min UTC timestamps = 419,184 P/Q paired station-times; 6.392% signed P and 46.566% signed Q are negative, and positive P at TR16 reaches **627.56 in source units**. Negative values alone do not prove export: meter direction and reference conventions remain unverified. Do not compute station `S=√(P²+Q²)` as kVA until the publisher confirms P in kW and Q in kvar; rated kVA and voltage are also needed before loading ratios.

**Answer:** Spatial/temporal electrical variability is measured. EV charging contributions and thermal overload are **not** established.

## 5. RQ4 — Vehicle charging V/I, SOC and battery temperature

KU Leuven AC source CSV row totals `7,598+4,252+15,083+13,940=40,873`. The well-ordered `Figure7_AC1` example has SOC median first/last 120 records `39.0%→90.3%` and pack-max temperature `30.25→28.75°C`. This demonstrates that the measured battery-pack temperature can fall while energy is being accepted, not that the charging station's own power module is cooling or derating.

**Answer:** Laboratory vehicle charging and battery trajectories are observed; a standalone battery cooling-heat balance remains underidentified.

## 6. RQ5 — Charging electrical power differences

For two `Figure10.xlsx` DC charger experiments, high-power eligibility `P_AC>30 kW`, `P_DC>20 kW`:

| Source test | Qualified samples | Median P_DC/P_AC | Median P_AC−P_DC |
|---|---:|---:|---:|
| EV1_DC1 | 87 | 0.92635 | 3.589 kW |
| EV1_DC2 | 116 | 0.92691 | 3.549 kW |

This numerical difference may contain multiple conversion, meter-boundary, auxiliary and cable contributions. It is **not an independently measured EVSE heat-rejection rate**, rectifier junction temperature, or field thermal derating law.

**Answer:** Electrical input–output differences are quantifiable under the selected tests; physical loss allocation remains open.

## 7. RQ6 — EV and premises/grid demand

**Not answered quantitatively in the present execution.** The previous OPSD data inventory counted 116,355 qualified 15-minute intervals from two premises. But the original source rows needed for a new matched, chronological forecasting comparison were not accessible here. The OPSD publisher explicitly states original meter data were filled/interpolated and 15-minute values are interval energy. A valid future experiment must compare a no-lookahead grid-load baseline to a model adding *past observed EV demand*, at the same timestamps, using correct kWh-to-kW conversion and excluding or separately stratifying interpolated records.

**Do not report an EV forecasting improvement percentage or causal coefficient.**

## 8. RQ7 — Exploratory laboratory PQ event response (NEW raw-data execution)

**Original file selection and screen:** 313 original nested OSF CSV experiments; inspect files whose names contain a `duration` of **2–30 s** and the literal `_Start_20` (**74** eligible by filename). Assume event starts at `t=20s` from metadata and compare a **10–20s pre-event baseline** with the **20–(20+duration)s event interval**. Require ≥30 valid simultaneous battery V/I samples before, ≥20 during, battery V in (200,1000) V, |I|<600 A, baseline median |I|≥1 A and baseline |V·I|≥0.5 kW. **61 of 74** pass; 13 are excluded for inactive baseline charging.

Per experiment compute **the difference between medians of battery-terminal `|V_batt I_batt|/1000` (kW)**; take the median of per-experiment percent changes for each class; do not pool serially repeated raw rows as independent experiments. Result:

| Disturbance folder | Qualified experiments | Median pre-to-event battery-terminal power change |
|---|---:|---:|
| Frequency Deviation | 9 | **+3.18%** |
| Harmonic | 9 | **0.00%** |
| Temporary Overvoltage | 9 | **−89.34%** |
| Voltage Deviation | 9 | **0.00%** |
| Voltage Sag | 9 | **−53.87%** |
| Temporary Undervoltage | 8 | **−88.74%** |
| Voltage Interruption | 4 | **−90.98%** |
| Voltage Swell | 4 | **−19.30%** |
| **All qualified** | **61** | **−7.88%** (heterogeneous distribution) |

Across these 61 experiments, **32** have within-experiment median power at least 5% below baseline. The pooled **25th–75th percentiles of per-experiment percent changes are −88.716% to +1.430%**; this is heterogeneous, NOT a single transferable response law. Note that different disturbance folders and charging conditions are not automatically matched control groups.

**Crucial limitations:**
1. The `20s` event onset was **inferred from filenames** and not independently cross-verified against the actual AC disturbance command waveform; category names and pulse durations require author confirmation. Short disturbances, other start times and the `Sag_extended` dataset were excluded, so this is **not a complete OSF effect estimate**.
2. `|V_batt I_batt|` is **battery terminal power** (with a consistent instantaneous V/I reading), **not** charger AC-input power or measured heat generation.
3. Source files contain sparse/multi-schema CAN data and preprocessed records; possible baseline drift, protective controls, SOC, battery type and shared hardware introduce confounding. Results are **descriptive within-experiment changes**, **not identified causal PQ treatment effects** or validated charger fault recovery.
4. This dataset has no field-tested transformer temperatures, no rectifier/heatsink temperature time series, no extreme-heat intervention, no matched P↔Tₑ physical topology and no independently verified mobility service consequences.

**Scientific answer:** Substantial within-experiment variations in measured battery terminal charging power occur across several named PQ test classes; this is an **exploratory observation**, not proof that any particular thermal mechanism caused those changes. [Experimental per-file table](./REPORT_01_OSF_RQ7_EVENT_RESPONSE_SCREEN.csv).

## 9. RQ8 — Are fitted transformer thermal parameters physically identifiable?

Using same SINTEF hourly model, independent script re-fit on original MD5-verified raw:
- Jan–Jun full fit: `a=0.080746093`, `b=0.069367232 °C/step at I_ref`, `c=1.084335252 °C/step`; `I_ref=29.375 A`.
- Jan–Mar separate fit (2,039 valid transitions): `a=0.049383516, b=0.069462090, c=0.587620710`.
- Apr–Jun separate fit (2,184 valid transitions): `a=0.112953011, b=0.078450553, c=1.548771087`.
- Jan–Jun design-matrix standardized condition number **1.539**; Pearson correlation between `T_a−T` and `(I/I_ref)^2` **−0.406**. These show no immediate simple numerical near-singularity, but **are not a physical structural-identifiability proof**. The sizeable split-to-split coefficient changes and lumped heat term `c` prevent interpreting `a,b,c` as invariant resistance, capacitance, copper loss or uniquely separated heat mechanisms.
- October–December 1-h test RMSE: persistence **0.24797°C**, current-plus-constant **0.24812°C**, ambient-plus-constant **0.21921°C**, full **0.21468°C**. Thus the current-squared term improves this model's RMSE only **0.00453°C** compared with ambient-plus-constant, within one site/season.

**Answer:** The three regression coefficients are numerically estimable under this model, but the measured fields are **insufficient to establish unique, stable physical heat-transfer parameters**. Next test independent physical heat balances, observed losses, model families, period dependence and confidence/identifiability analysis.

## 10. RQ9 — Model sensitivity and uncertainty

New 24-h **deterministic** experiments across October–December starts: measured *future* ambient and current remain available; nominal model evaluated on **2,089** starts limited to Oct 1–Dec 30 for matched one-at-a-time perturbations. Base conditional model RMSE **0.92478°C**; matched persistence **2.10734°C**. This sensitivity subset differs from the 2,112-start full October–December 24-h RQ2 test.

| Single perturbation (24-hour input horizon) | Outcome relative to nominal |
|---|---|
| +5°C to each ambient forcing value | Predicted top-oil **+4.337°C** (in this linear recurrence) |
| −5°C to ambient forcing | Predicted top-oil **−4.337°C** |
| `a` reduced 10% | Median absolute change **1.371°C** |
| `a` raised 10% | Median absolute change **1.197°C** |
| `b` changed ±10% | Median absolute change **0.115°C** |
| `c` changed ±10% | Median absolute change **1.165°C** |
| Current magnitude increased 10% for entire 24h | Median predicted temperature increase **0.241°C** |
| Initial transformer top-oil state +2°C | Model-propagated +0.265°C after 24 h, with fixed forcing |

**Answer:** Predictions are sensitive to ambient forcing and the empirically lumped `a,c` coefficients. **These are chosen perturbation scenarios**, not confidence intervals, uncertainty distributions, or genuine field tests of ambient temperatures above the source range. A future UQ study must quantify sensor, structure, calibration, temporal correlation and external-site uncertainty.

## 11. RQ10 — Where can this model be considered tested?

Full original measured SINTEF ranges: ambient **−19.58 to +25.97°C**, current **8.4125 to 75.1025 A**, top-oil **3.8275 to 38.86°C**.

In held-out **October–December one-hour** transitions, ambient-bin sample sizes and errors are:
- `T_a≤0°C`: **263**, model RMSE **0.1970°C**, persistence **0.2433°C**.
- `0<T_a≤10°C`: **1,482**, model RMSE **0.2105°C**, persistence **0.2466°C**.
- `10<T_a≤20°C`: **413**, model RMSE **0.2391°C**, persistence **0.2556°C**.
- `T_a>20°C`: **0** held-out 1-hour transitions. Hence **no held-out high-ambient claim**.

Full-horizon conditional hindcast RQ2 results are reported above. The single-year, single-transformer dataset does not identify or verify a transfer map `θ_A→θ_B` for other capacities, insulation/cooling arrangements, climate regimes, feeder networks, EV charging behavior or extreme-heat severity.

**Answer:** Tested in a bounded, same-site chronological domain for moderate-ambient forced oil-temperature response. **Generalization to other installation types, prolonged extreme heat and a connected transformer–EVSE installation remains an untested hypothesis**, not an established result.

## 12. RQ11 — Thermal constraints, viability and electricity/mobility service

A purely **conditional**, proposed coupled model (unknown site mapping and parameter values):

```math
C_P\dot T_P=P_{\mathrm{loss},P}(I_P,T_P)-Q_{\mathrm{cool},P}(T_P,T_a)
```

```math
C_E\dot T_E=Q_{\mathrm{gen},E}(P_{\mathrm{AC}},P_{\mathrm{DC}},z_E)-Q_{\mathrm{cool},E}(T_E,T_a,z_E)
```

```math
0\le P_{\mathrm{del}}(t)\le \min\big(\bar P_{\mathrm{grid}}(T_P,t),\bar P_{\mathrm{EVSE}}(T_E,t),\bar P_{\mathrm{vehicle}}(t)\big).
```

Here `T_P` is transformer temperature, `T_E` is **charger internal temperature (not battery temperature)**, `z_E` charger cooling/control state. Site-specific transformer current-flow mapping, P_ac/P_dc metering boundary, heat partition, thermal limit curves, service requirements and delayed propagation must all be *established*. The power-limits expression requires a **common electrical power boundary** or explicit AC/DC conversion; as written it is only a conceptual minimum envelope.

For a required delivered charging energy `E_req` over allowed interval `[0,H]`, define only after the delivery-side power boundary is verified:

```math
E_{\mathrm{unserved}}=\max\left(0,E_{\mathrm{req}}-\int_0^H P_{\mathrm{del,DC}}(t)\,dt\right).
```

Any `T_P≤T_{P,max}`, `T_E≤T_{E,max}` viability test must use source-backed limits, initial conditions and qualified physically connected dynamics. No such complete field trajectory is currently in the evidence package.

**Answer:** One can formulate a conditional viability/service analysis and test numerical logic with labelled hypothetical scenarios. **No measured interdependency propagation time, connected thermal threshold crossing, observed charging-service deficit, verified safe control policy, or improved real-world resilience can yet be reported.**

## 13. Validity, transferability and final admission

`SOURCE-AUTHENTIC FIELD MEASUREMENT ≠ PHYSICAL CAUSAL IDENTIFICATION ≠ MODEL VALIDITY ≠ EXTERNAL TRANSFERABILITY.`

- **Empirical:** SINTEF transformer sensor data, STREAM electrical station data, KU vehicle charging data and OSF laboratory responses are observations of **different assets and research environments**, not a single integrated P↔Tₑ site.
- **Mathematical:** Our SINTEF equation is a constrained empirical RC-like reduction with conditional hindcast validity, NOT uniquely estimated thermal resistances/capacitances or proven heatwave physics.
- **Transfer:** No independent transformer installation or connected thermal EVSE data was used to verify prediction transfer.
- **Scope:** The thesis's frozen SO1 identify/qualify thermal mechanisms; SO2 physics-based state-time dynamics; SO3 transition times, propagation and required electricity/mobility service consequences remain the authorities. These 11 questions are **supporting work**, and RQ11 is optional until physically qualified.
- **Extremes:** Since the instrumented transformer never recorded ambient >25.97°C and held-out test did not include ambient >20°C, an imposed +5°C forcing is numerical sensitivity, **not experimental extreme-heat validation**.

## 14. Executed reproducibility and next validation gates

**Raw originals:** remain in private thesis Google Drive. **This GitHub report stores no original sensitive equipment datasets.** Important original checksums and source DOI are listed above; the script checks original SINTEF MD5; OSF report captures original ZIP SHA256 and per-experiment derived outcomes.

- [Original 7-RQ quantitative report and original RQ1–RQ5 reproduction script](./REPORT_01_MEASURED_DATA_RQ1_RQ7_2026-11-03.md).
- [RQ8–RQ10 independent transformer reproducibility script](./REPORT_01_EXTENDED_TRANSFORMER_REPRODUCE.py).
- [RQ7 original OSF archive response-screening script](./REPORT_01_OSF_RQ7_REPRODUCE.py).
- [RQ7 per-experiment result table](./REPORT_01_OSF_RQ7_EVENT_RESPONSE_SCREEN.csv).
- [Full original-file audits](./SLOVENIA_STREAM_SINTEF_RAW_AUDIT_2026-11-03.md) and [KU Leuven ZIP QA](./UPLOADED_ARCHIVES_QUALIFICATION_2026-11-03.md).

**Next priorities (in scientific order):**
1. Secure author-verified **connected transformer↔feeder↔EVSE topology** with timestamped thermal state, electrical boundary, operating constraints and charger derating events. KIT / Qatar / electric-bus charging leads are highest.
2. Complete RQ6 only with original OPSD 15-minute rows, interpolation flags, kWh→kW interpretation, time/leakage controls and site-separated baseline/augmented holdout evaluation.
3. Author-confirm OSF event onset/offset and compare true matched normal vs disturbed laboratory experiments; include short pulses and non-standard schemas only under explicitly appropriate protocols; verify post-disturbance recovery.
4. For SINTEF: compare physically distinct models, assess parameter identifiability and autocorrelation-aware UQ; secure independent extreme-heat site before claiming transferability.
5. Verify KU Leuven AC/DC measurement definitions, time discontinuities and possible equipment overlap before attempting physical heat-source allocation.

**Decision:** **Report 1 completed as an evidence-qualified question-by-question scientific record; not all 11 RQs are empirically solved.** RQ6 is numerically blocked; RQ11 awaits site-coupled evidence; RQ7 is newly quantified only as descriptive battery-side lab response. No frozen project title/scope/objectives, original raw data or accepted previous validation gates were changed.
