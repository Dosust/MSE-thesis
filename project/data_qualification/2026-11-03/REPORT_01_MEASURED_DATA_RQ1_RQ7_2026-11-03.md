# Report 1 — Seven Measured-Data Research Questions: Power–Electrified Transportation

**Date:** 3 November 2026  
**Thesis:** Engineering of Power–Electrified Transportation Interdependencies for Resilience  
**Evidence status:** **Working research report; not a frozen result or validated connected-system model**  
**Scope:** Answers RQ1–RQ7 to the extent supported by authenticated component observations; distinguishes new calculations, prior audited evidence, and unresolved questions.

## Executive answer

| RQ | Scientific answer | Completion |
|---|---|---|
| **RQ1** Transformer electrical/ambient forcing vs temperature | In SINTEF, top-oil has a very strong *observational* correlation with ambient (r=**0.9658**). Squared-current has negative *unadjusted level* correlation with top-oil (r=**−0.8007**) because the measured series combine seasonality and changing operation. This is **not** evidence of current cooling the transformer. A dynamic positive-current-squared model must be judged separately. | **Measured descriptive answer**, causal heat mechanism not identified |
| **RQ2** Dynamic transformer temperature prediction vs baseline | Jan–Jun fit; Jul–Sep calibration; Oct–Dec held-out test. 1-h top-oil **RMSE=0.2147°C** versus persistence **0.2480°C** (≈13.4% lower); **MAE=0.1469°C** versus persistence **0.1409°C** (≈4.2% higher). Six- and 24-hour conditional hindcast RMSE below persistence, with future *observed* ambient/current supplied. | **Same-site chronological validation, provisional** |
| **RQ3** P and Q variability across stations | Slovenian original files contain **34,932** matching 15-min UTC timestamps and **12** anonymized stations, i.e. **419,184 paired station-time P/Q observations**. Station active-power maxima differ; **6.392%** of P and **46.566%** of Q station-time entries are negative. The highest observed positive P value is **627.56 in source units** (TR16). | **Measured descriptive answer**, source units, signs and ratings require verification |
| **RQ4** EV charging electrical and battery-thermal behavior | Four KU Leuven AC experimental files: **40,873 row records**; battery voltage and predominantly negative charging current are recorded, as are pack maximum temperature and SOC. For example, Figure7_AC1 sampled-window SOC rises **39.0→90.3%**, while BMS max temperature falls **30.25→28.75°C**, consistent with charging while cooling is possible. Other files have clock resets and/or nonmonotonic SOC; do not interpret their first-to-last values as a continuous session. | **Measured/processed laboratory component answer; time-order gate partial** |
| **RQ5** EV charging electrical conversion losses | Two Figure10 KU Leuven DC tests at eligible high power give median source-boundary **P_DC/P_AC=0.92635 and 0.92691**, with median **P_AC−P_DC=3.589 kW and 3.549 kW** respectively. These are **electrical input-output differences**, NOT measured heat flux or verified independent charger thermal losses. Prior EPFL energy-balance audit remains unreconciled. | **Provisional converter electrical-boundary result**, thermal efficiency not established |
| **RQ6** Same-premise EV charging vs grid demand/predictability | Prior OPSD audit recorded **116,355 qualified 15-min intervals** for two locations. Its raw household series were **not** available to this Report 1 execution, and OPSD documents gap interpolation/filling. A quantitative charging–grid correlation or forecasting improvement **has not been recomputed and cannot be asserted** from counts alone. | **Not numerically answered in this execution** |
| **RQ7** Charging response to power-quality disturbances | Earlier OSF 94GKC audit covered **313 lab experiments, 4,061,379 row records**. Only **23,052 (0.57%)** battery-temperature cells were nonempty, with documented suspect values. Raw per-experiment waveforms were not available to this Report 1 execution; quantitative disturbance effects on charger power/current and their uncertainty **cannot be reported as independently reproduced**. | **Design/evidence inventory only; quantitative response blocked** |

**Important distinction:** completed descriptive analysis of separate systems does **not** establish a physically connected transformer–EVSE interface, an observed extreme-heat thermal cascade, service-level resilience, or a validated coupled model.

---

## 1. Sources, reproducibility and provenance

### Directly analyzed in this Report 1 execution

1. **SINTEF Bærug 2024, DOI [10.5281/zenodo.17223516](https://doi.org/10.5281/zenodo.17223516)**: measured transformer-only sensor CSV, 8,592 rows, original publisher MD5 **5d81840a2f901f04fded98c3e1097b6e**; [unchanged raw in Google Drive](https://drive.google.com/file/d/1sOEtx-Nlr00n_pLqTdWb4BZI6O35m8Nu/view).
2. **STREAM Slovenia 2025, DOI [10.5281/zenodo.20927130](https://doi.org/10.5281/zenodo.20927130)**: 34,932 rows each in [original P CSV](https://drive.google.com/file/d/1hZ7pCydBAkfnLf4RU2lTu3LozNvuQ4tO/view) and [original Q CSV](https://drive.google.com/file/d/1SQ0ONhiCXK3_Ax--q9j0lUQV7IDACL5I/view), publisher MD5 **6a7fce6170230bcc73b69ba745509dad** and **7b8a9a608b0489c6227ced8cceb08a59**, respectively.
3. **KU Leuven C5PT0R, DOI [10.48804/C5PT0R](https://doi.org/10.48804/C5PT0R)**: user-uploaded experimental ZIP, four Figure6/7 AC CSVs and Figure10 XLSX, [unchanged raw in Drive](https://drive.google.com/file/d/1zYktMEjoqXu-ZheGW8HGATwx23_lAcjH/view); published MD5s of original payload files checked by the earlier archive audit.

### Reused previous audits; *not* recomputed from raw originals in this execution

- **EPFL Level-3 charging**, [source repository](https://github.com/DESL-EPFL/Level-3-EV-charging-dataset): prior detailed [Drive QA report](https://drive.google.com/file/d/1bPmP58__Ifmnhf4WtpTts0GbpeR5m2_B/view). Its declared 64,277 measurement count differs from the prior scan's 61,816 populated measurement rows; energy accounting mismatch unresolved.
- **Open Power System Data (OPSD)**, [household_data 2020-04-15](https://data.open-power-system-data.org/household_data/2020-04-15/): prior D04 report states 116,355 qualified 15-min observations; original processed household rows not mounted in this Report 1 run.
- **OSF 94GKC**, [original dataset DOI](https://doi.org/10.17605/OSF.IO/94GKC), [Li et al. 2026 Scientific Data](https://doi.org/10.1038/s41597-026-06768-5): prior D06/field QA states 313 experiments, 4,061,379 rows; original laboratory experiment files not mounted in this Report 1 run. An earlier original OSF ZIP resides in [Google Drive](https://drive.google.com/file/d/1Sjdg5TaGWXybjO_8DOlnkzIeSHpVhR4x/view).

**Never count combined row records as independent vehicles, installations or charging sessions.** No source here provides same-site, synchronized transformer-and-EVSE thermal measurements.

## 2. RQ1 — How do ambient temperature and electrical loading relate to oil and winding temperatures over time?

**Method:** Descriptive Pearson coefficients across original observed hourly samples. No interpolation across 192 missing hourly timestamps. For all thermal sensor signals, compare measured ambient T_a and squared measured current I² against each measured temperature. Lagged associations are segmented by contiguous time runs.

| Measured temperature state | r with ambient | r with squared current | Valid rows |
|---|---:|---:|---:|
| Top oil | **0.9658** | **−0.8007** | 8,592 |
| Bottom oil | 0.9757 | −0.8094 | 8,592 |
| Mid-spot HV | 0.9305 | −0.6929 | 8,592 |
| Mid-spot LV | 0.9293 | −0.6548 | 8,592 |
| Hot-spot HV | 0.9017 | −0.6231 | 8,589 |
| Hot-spot LV | 0.8310 | −0.4629 | 8,589 |

- Measured ambient is **−19.58 to +25.97°C**; measured top oil **3.8275 to 38.86°C**.
- One-hour measured **Δ(top oil)** has r≈**+0.0439** with I², but r≈**+0.4601** with (ambient−top-oil). These are only simple correlations of different variables, not a partition of heat terms.
- Lagged *level* r(I²_t, T_oil,t+h) remains negative over 0–24 h (for example r≈−0.8007 at 0h, −0.7834 at 24h). Cross-correlation peaks cannot be interpreted as an identified thermal lag without separating slow seasonal forcing, autocorrelation, feedback and electrical operating conditions.
- **Finding:** ambient covaries strongly with absolute transformer temperature in these measurements. The negative raw current-temperature association is **not** a physical cooling law; winter/summer and load profiles are confounders. Thermal inertia is tested more appropriately with a dynamic state equation (RQ2). Causal contributions and heat capacity are not separately identified.

## 3. RQ2 — Does a constrained dynamic model beat persistence?

**Model:**

\[
T_{k+1}=T_k+a(T_{a,k}-T_k)+b(I_k/I_\mathrm{ref})^2+c
\]

with 1-hour steps, constrained a∈[0,1], b≥0 and c≥0. This is a **phenomenological RC-like Euler model**, not a fully identified heat-transfer equation. Fit **January–June**, use **July–September for residual calibration**, reserve **October–December** for test. Exclude any transition crossing a gap.

Fitted Jan–Jun: **a=0.0807461**, **b=0.0693672°C per h at I_ref**, **c=1.0843353°C per h**, **I_ref=29.375 A**. The illustrative relaxation scale \(1/a\) is **12.38 h**, *not an independently validated thermal time constant*.

| Test horizon | Test starts | Model RMSE (°C) | Persistence RMSE (°C) | Model MAE (°C) | Persistence MAE (°C) |
|---|---:|---:|---:|---:|---:|
| 1 h | 2,158 | **0.2147** | 0.2480 | **0.1469** | **0.1409** |
| 6 h | 2,148 | **0.6547** | 1.0209 | 0.4548 | 0.7138 |
| 24 h | 2,112 | **0.9366** | 2.1338 | 0.6870 | 1.6462 |

**Decision:** At the specified split the constrained model is better in test RMSE at all three horizons and in MAE for 6/24h, but worse in **1-h MAE**. The horizons use *observed future ambient and current*—these are **conditional hindcasts**, not true future operational forecasts. Six- and 24-hour evaluation windows overlap; sample error bars would not be independent.

For a residual-based descriptive band: the July–September 95th percentile absolute one-step residual is **0.6055°C**, encompassing **98.01%** of October–December test errors. **Do not call this calibrated 95% predictive uncertainty**, since errors are serially dependent and subject to distribution shift. It does not replace an uncertainty study with identified sensor uncertainty, parameter uncertainty and independent validation.

**Unanswered:** physical coefficients/individual cooling mechanisms; exogenous heat extremes >25.97°C; independent transformer type/site; free-running long-term prediction without known future forcing; transformer-to-charger restrictions.

## 4. RQ3 — How do P and Q vary across the Slovenian stations?

**Measurement check:** Two publisher-verified originals, 12 matching column IDs (TR1, TR2, TR3, TR4, TR6, TR8, TR9, TR11, TR12, TR14, TR15, TR16), 34,932 common **15-min UTC** stamps from 2025-01-01 00:00 to 2025-12-30 20:45. **Zero missing numeric values, duplicate timestamps or internal 15-min gaps.** The full 2025 calendar contains 35,040 quarter-hour positions, so the final **108** are absent.

| Example station | Median signed P (source units) | Maximum positive P (source units) | Negative-P fraction |
|---|---:|---:|---:|
| TR1 | 221.24 | 407.32 | 0.0% |
| TR3 | 45.32 | 157.88 | 12.44% |
| TR6 | 86.56 | 258.16 | 15.59% |
| TR12 | 87.68 | 320.44 | 11.17% |
| TR15 | 86.60 | 382.04 | 14.57% |
| TR16 | 187.38 | **627.56** | 0.83% |

- Across 419,184 station-times, **6.392%** of P values and **46.566%** of Q values are negative. Signs must not be clipped. **The metering/injection sign convention remains unverified**, so reverse-flow attribution is a hypothesis, not established.
- Station-specific contemporaneous r(P,Q) ranges approximately **−0.825 to +0.700**; no universal power factor or signed reactive relationship follows.
- Simple mean signed P across all 12 stations and each month's sampled timestamps (source units): **January 132.02**, **May 65.52**, **December 129.86**; this is an *observed seasonal profile*, not a claim about temperature or grid overload.
- Station source CSVs do **not** supply kW/kvar units in the headers or nameplate ratings, temperatures or EVSE identities. Before using \(S_i=\sqrt{P_i^2+Q_i^2}\) as kVA and \(\rho=S_i/S_{\mathrm{rated},i}\), obtain [STREAM companion equipment parameters](https://doi.org/10.5281/zenodo.20927801), confirm units, ID crosswalk, reference directions and rating basis.

**Decision:** measured operational electrical variation is established; transformer thermal overload, EV charging impact and equipment stress are **not**.

## 5. RQ4 — How do EV charging electrical and battery signals evolve?

**Input:** KU Leuven four AC experimental source CSVs, **7,598 + 4,252 + 15,083 + 13,940 = 40,873 row records**. Measured/processed channels include \`ChargeLinePower264\`, \`ChargeLineVoltage264\`, \`ChargeLineCurrent264\`, \`BattVoltage132\`, \`RawBattCurrent132\`, \`SOCave292\`, \`BMSmaxPackTemperature\`.

| Source file | Rows | Median line power (source units) | Median battery voltage | Median battery current (signed) | Time steps backwards |
|---|---:|---:|---:|---:|---:|
| Figure6_AC1 | 7,598 | 5.4 | 359.3 V | −13.94 A | 5 |
| Figure6_AC2 | 4,252 | 7.4 | 361.1 V | −19.15 A | 6 |
| Figure7_AC1 | 15,083 | 10.7 | 378.6 V | −26.68 A | 0 |
| Figure7_AC2 | 13,940 | 10.6 | 379.9 V | −26.50 A | 1 |

**Selected well-ordered example:** Figure7_AC1, comparing medians of the first 120 and last 120 observed records, SOC **39.0%→90.3%** while measured BMS maximum pack temperature **30.25°C→28.75°C**. Thus battery temperature need **not** increase monotonically during charging; this alone does not identify cooling energy or control logic.

**Data-quality exception:** Other files have decreasing timestamps and some first/last SOC values are even slightly lower, so **do not** conclude they are single uninterrupted sessions or infer physics from apparent first-last changes. Source timestamp order, session boundaries, thermal sensor semantics and charging-current polarity need further instrumentation verification. These are laboratory, not operating-field EVSE experiments.

**Decision:** electrical and battery-temperature trajectories can be described at the component level. EVSE internal temperature, fan cooling/derating or site-level grid-to-mobility propagation cannot be inferred.

## 6. RQ5 — How much electrical power differs across charging converter boundaries?

**KU Leuven Figure10.xlsx** provides simultaneous reported AC input and DC output (both in W). To avoid startup/off-state fractions, predeclare high-load sample eligibility: **P_AC > 30,000 W** and **P_DC > 20,000 W**.

\[
r_{\mathrm{DC/AC}}=\frac{P_\mathrm{DC,out}}{P_\mathrm{AC,in}},\qquad
\Delta P=P_\mathrm{AC,in}-P_\mathrm{DC,out}.
\]

| Experimental test | Eligible observations | Median DC/AC ratio | Median AC minus DC |
|---|---:|---:|---:|
| EV1_DC1 | 87 of 111 | **0.92635** | **3.589 kW** |
| EV1_DC2 | 116 of 147 | **0.92691** | **3.549 kW** |

For four AC files, an independent **provisional battery-electrical-power/AC-line-power proxy** has median **0.9282, 0.9357, 0.9470, 0.9469** respectively. It includes possible auxiliaries/incompatible metering boundaries and therefore must not be marketed as a laboratory total-efficiency certificate.

**Instrument issue:** In Figure10 EV1_DC2, the \`FC_dcCurrent\` and \`FC_dcVoltage\` headings appear possibly interchanged (values around 368 and 123, while battery voltage is ~368 V). The independent explicitly labeled **AC power/DC power** pair was used for the above summary; the heading issue remains a sensor-definition gate.

**EPFL cross-check:** Earlier audit (not a new raw calculation here) identified **1,878 sessions**, **61,816 populated minute observations** versus 64,277 described publicly, and roughly **15% median relative difference** between independently integrated \`P(W)\` and reported session energy. These figures reflect **unreconciled energy-accounting boundaries**, not charger heat or an efficiency penalty. [Source EPFL](https://github.com/DESL-EPFL/Level-3-EV-charging-dataset).

**Decision:** conditional electrical input/output loss estimates are possible. The difference \(\Delta P\) is **not a measured EVSE heat rejection**, and neither dataset proves charger temperature-driven derating in extreme heat.

## 7. RQ6 — How does EV charging affect electricity-demand predictability?

**Status: source available, quantitative question not freshly tested.** Prior D04 OPSD audit cites **116,355 qualified 15-minute intervals across two locations**, with separate EV and electrical household feeds, but source raw records were not passed to this execution. OPSD notes interpolation and past-day filling of gaps; interpolation status must be included as a quality covariate.

**Minimum valid test design when originals are restored:**
- Identify same-premises measured \`grid_import\`, EV charging demand and optional PV/storage, their units and 15-minute interval bases; check whether EV usage is part of the metered net site total.
- Fit chronological baseline \(\widehat P_{\mathrm{grid},t+h}\) using time-of-day/day-of-week and recent measured grid load; compare a second model adding lagged measured EV demand, with **no future realized EV power leaked into predictors**.
- Evaluate same test timestamps with MAE and RMSE and report site-separated results and confidence under autocorrelation; compare results on only noninterpolated rows.
- Do not interpret the prediction improvement as causal impact if EV load is already included in the site meter, or extrapolate to transformer loading with no electrical mapping.

**No computed EV-load coefficient, correlation, prediction score or improvement is claimed in Report 1.**

## 8. RQ7 — How do PQ disturbances influence charging electrical behavior?

**Status: authenticated laboratory data inventory; quantitative question not freshly tested.** Prior OSF 94GKC audit: **313 CSV experiments, 4,061,379 row records**, multiple schemas and disturbance classes, **23,052 nonempty BMS temperature entries (~0.57%)** and suspect values such as 1538.3. The scientific article describes controlled single power-quality disturbances and current/voltage response measurement; it does **not** establish a field heatwave transformer–charger interface.

**Minimum valid experiment design when raw archives are remounted:**
- For each disturbance class and severity, verify source/event time, measured grid voltage/current and charging power channel, units and instrument synchronization.
- Compare a predeclared pre-event baseline window against disturbance and recovery windows **within each experiment**. Compute normalized RMS-voltage deviation, RMS current response, active power ratio, interruption/duration or return-to-baseline time, where sampling resolution and signals permit.
- Aggregate over **experiments** (not millions of serially autocorrelated rows) and stratify by SoC/voltage conditions. Require comparable controls rather than treating unequal SoC events as equivalent.
- Test response uncertainty and exclude invalid temperatures; the sparse battery temperature field is **not sufficient** for temperature-dependent EVSE derating identification.

**No new effect size, sensitivity slope or resilience improvement is claimed in Report 1.**

## 9. Thesis integration and research gates

| Objective | Qualified now | Still missing |
|---|---|---|
| SO1 — characterize physical interfaces | Individual transformer thermal forcing/state (SINTEF), station P/Q operating variability (Slovenia), EV charging electrical/battery response (KU Leuven) | Demonstrated physically mapped transformer↔feeder↔EVSE path, time-aligned bidirectional interaction |
| SO2 — model physical dynamics | Chronological **conditional** transformer hindcast and measured charging power boundaries | Site-validated charger temperature/thermal derating laws, connected observations, extreme-heat transfer, identified uncertainty |
| SO3 — electricity/mobility service resilience | Framework and source candidates for conditional charging-demand modeling | Synchronized actual charging need/delivery, thermal restrictions, propagation/recovery evidence |

**Scientific acceptance statement:** This is **Report 1 on independently observed components**, not an integrated coupled-system empirical validation. Any cross-installation combination in future work must be labeled a **hypothetical or conditional model experiment**, not observations from one site.

## 10. Next report tasks

1. Recover original OPSD rows for **RQ6** and OSF original experiment archive for **RQ7** in the same executable environment; deliver matched baselines and uncertainty, or document gate failures.
2. Obtain [STREAM transformer nameplates and losses](https://doi.org/10.5281/zenodo.20927801); verify station-ID match, kW/kvar, power direction and rated kVA before any overload claim.
3. Resolve the KU Leuven time reversals, SOC discontinuities, session boundaries and AC/DC sensor meanings; verify distinctness from the other KU Leuven battery dataset D02.
4. For RQ2, add independent model families, long-horizon free-running sensitivity, autocorrelation-aware predictive intervals, and heat-range/out-of-distribution evaluation.
5. Pursue a genuinely connected transformer+charger field installation with measured temperatures, protection actions, charging power, demand and service outcomes.

**Audit linkage:** [New-original field-file QA](./SLOVENIA_STREAM_SINTEF_RAW_AUDIT_2026-11-03.md); [KU Leuven source QA](./UPLOADED_ARCHIVES_QUALIFICATION_2026-11-03.md); [Master inventory](./MASTER_DATA_INVENTORY_2026-11-03.csv). Original measurement bytes are retained in the thesis Google Drive Data folder and are deliberately **not committed as new GitHub data files**.

## 11. Python reproduction of selected new numerical results

**Script:** [REPORT_01_REPRODUCE.py](./REPORT_01_REPRODUCE.py). Install \`pandas\`, \`numpy\`, \`scipy\` and \`openpyxl\`, then run:

\`\`\`bash
python REPORT_01_REPRODUCE.py \
  --sintef "Barug2025_sensordata(2).csv" \
  --p control_measurements_P_2025.csv \
  --q control_measurements_Q_2025.csv \
  --evzip doi-10.48804-c5pt0r.zip
\`\`\`

Source-original MD5 hashes are checked before calculations. This compact script independently reproduces **key RQ1–RQ5 numerical metrics**: ambient/current correlations; one-hour chronological RC model/persistence RMSE and MAE; Slovenia synchronized-count/sign fractions; KU Leuven AC source summaries and Figure10 DC power ratios. The larger research run also calculated all-sensor correlations, 6/24-hour conditional hindcasts, station-level statistics and lag profiles; these are detailed above and are not implemented in the compact script. RQ6/RQ7 are explicitly **not** reproduced without their original row-level inputs.

