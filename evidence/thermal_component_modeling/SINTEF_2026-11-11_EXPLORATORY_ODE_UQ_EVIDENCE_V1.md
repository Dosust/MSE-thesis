# SINTEF transformer thermal-state numerical audit — 2026-11-11 (V1)

**Status:** WORKING RESEARCH EVIDENCE / ASSISTANT-EXECUTED EXPLORATORY COMPUTATION; **NOT** PHYSICALLY VALIDATED, THESIS-FROZEN, SUPERVISOR-APPROVED, OR A CONFIRMED POWER–ELECTRIFIED TRANSPORTATION INTERDEPENDENCY.

**Run date:** 2026-11-11. **Evidence class:** [A3] original measured component data; [T1] exploratory thesis-related model and numerical calculations; [OPEN] model transferability, unique physical parameters, operating limits, cross-system thermal causation, and service effects.

**Active scope:** [Current authority index](../../project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md), [frozen SO1–SO3](../../project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md), [non-invention standard](../../project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md), and [physics-first directive](../../project/PHYSICS_MATHEMATICS_FIRST_HYPOTHESIS_TESTING_SCOPE_DIRECTIVE_V1.md). This record adds evidence; it makes **no changes** to these authorities, the thesis title, or the active model.

## 1. Scientific summary (approximately 100 words)

An exploratory analysis of 8,592 hourly SINTEF transformer observations examined physics-based thermal dynamics, parameter identification, numerical verification, and uncertainty. A reduced first-order model achieved top-oil RMSE of 0.2165 °C versus 0.2517 °C for persistence, although MAE worsened slightly. A two-state model improved bottom-oil RMSE to 0.1240 °C versus 0.2324 °C but provided no top-oil advantage. Estimated effective time constants varied with observation spacing, indicating unresolved practical identifiability. Euler and Runge–Kutta tests confirmed convergence for a reduced ODE test; nominal 90% parameter-only bands covered approximately 8% of holdout observations. These results do not establish extreme-heat or coupled-system validation.

## 2. Source provenance and data qualification

- Original primary data: Bærug et al., SINTEF transformer sensor measurements, [Zenodo DOI 10.5281/zenodo.17223516](https://doi.org/10.5281/zenodo.17223516). The source README describes **2024 monitoring of one 40 MVA ONAN oil-filled transformer in southern Norway**; measured sensor CSV must not be confused with the separate calculated-data CSV.
- Source file: `SINTEF_Barug2025_sensordata_original_MD5verified_2026-11-03.csv`, retrieved from the user's Drive archive. SHA-256 **`6aa7384867aace7b9e17778decbbdbde280db1fd7983faee08c259b19e51`**.
- Data span: 2024-01-01 00:00 to 2024-12-31 23:00; **8,592** hourly rows versus **8,784** expected hours. **192 missing hourly timestamps** in two discontinuities (145-hour and 49-hour timestamp steps, corresponding to 144 and 48 missing hours).
- Sensor channels: voltage/current, ambient, top/bottom oil, winding temperatures, and some clamping measurements; 3 missing observations in each winding hot-spot channel. **Maximum ambient temperature 25.97 °C; zero records at or above 30 °C**.
- Ambient–current sample correlation: approximately **−0.8438**, which can confound attempts to attribute fitted thermal coefficients to individual physical effects. The data contain **no verified electrically mapped, co-located EVSE**.

## 3. Methods and exact comparison definition

**One-state candidate:** Effective thermal energy balance, with piecewise-constant hourly inputs,

```math
C_o\frac{dT_o}{dt}=P_{\mathrm{loss}}(I)-H_o(T_o-T_a)
```

and its fitted one-hour reduced map

```math
T_{o,t+1}=aT_{o,t}+(1-a)\left[T_{a,t}+d+g\left(\frac{I_t}{I_{\mathrm{ref}}}\right)^2\right],\quad a=e^{-1/\tau}.
```

- Fit: bounded nonlinear least squares of effective `tau`, `d`, and `g`, using only **consecutive-hour pairs**; predictors measured at time `t` and observed temperature at `t+1`. A single observed current does not decompose copper and core losses.
- Preprocessing reference: `I_ref = 27.58625 A`, median current of **the complete file**; a deterministic feature scale, **not rated current**. Recompute using the training portion only for any future leakage-strict confirmatory run.
- Split: chronological earlier-70%/later-30% by source row index, excluding pairs crossing missing-hour gaps: **6,012 training pairs**, **2,576 holdout pairs**; holdout starts **2024-09-13 14:00**.
- Persistence comparator: `T_hat(t+1)=T(t)`, evaluated on exactly the same holdout pairs.
- The fitted time constant is an **effective** model coefficient, not a separately identified manufacturer heat-capacity/conductance parameter.

**Two-state candidate:** Effective linear top-/bottom-oil balances with ambient exchange, current-squared heating, and cross-zone terms, integrated using the exact linear zero-order-hold state map. Parameters are bounded and estimated using three starts; the fit does not enforce independently verified transformer capacities or reciprocal physical heat flows. Adding an observed oil temperature as a second state does **not** demonstrate inter-system coupling.

## 4. Numerical findings (chronological holdout, °C)

| Temperature and model | Test RMSE | Test MAE | Persistence RMSE | Persistence MAE |
|---|---:|---:|---:|---:|
| Top oil, one-state | **0.2165286612** | **0.1498538712** | 0.2516987404 | 0.1449809092 |
| Top oil, two-state | **0.2165286612** | **0.1498538711** | 0.2516987404 | 0.1449809092 |
| Bottom oil, two-state | **0.1239538454** | **0.0965988615** | 0.2324474014 | 0.1828789713 |

- One-state effective parameter estimates: `tau = 10.982527 h`, `offset = 13.480628 °C`, `current gain at I_ref = 0.729095 °C`. These are estimated empirical/effective coefficients under the stated parameterization.
- Two-state fitted bottom-to-top coefficient: `k_ob = 4.300989e-23 h^-1` (effectively at the nonnegative boundary). Thus added bottom-oil information did not improve top-oil prediction **for this fitted model and holdout**. This **does not** show that real top/bottom oil heat exchange is absent.
- The fitted two-state top-oil-only linear observability diagnostic was severely ill-conditioned (reported condition number approximately `2.34e22`). This is a **local diagnostic of this fitted representation**, not a proof of universal physical non-observability or global identifiability.
- Across earlier experiments with 1-, 6-, 12-, and 24-hour observation spacings, effective time constants changed substantially. This is **evidence of sensitivity to estimation design**, not a formal proof of non-unique intrinsic parameters.

## 5. Numerical verification and uncertainty findings

- For the one-state constant-input ODE test, explicit Euler and classical fourth-order Runge–Kutta were compared with its **analytic one-hour solution**. Errors decreased as the timestep was refined. This verifies the selected numerical test **only**; it does not validate the physical constitutive model.
- Exploratory parameter resampling: **90** moving-block resamples, each using **48 consecutive training-pair indices**. The nominal central 90% **parameter-only** model-output bands covered **0.080357** (about **8.0%**) of held-out observations; mean band width was **0.037785 °C**.
- The above bands omit observation noise, model discrepancy, forcing uncertainty, and nonstationarity. They are **not calibrated 90% predictive intervals**, and their poor coverage alone must not be interpreted as a formal probabilistic safety statement.
- The experiment did **not** establish correct uncertainty distributions for transformer operating limits, nor a certified upper temperature threshold.

## 6. Scientific interpretation and thesis-status gates

| Active objective | Evidence admitted from this experiment | Remaining gate |
|---|---|---|
| **SO1** — physical states and directional mechanisms | Measured transformer thermal components and candidate heat-balance structure | No verified thermally directed P↔T_e link; EVSE data are from separate installations |
| **SO2** — physics-based state/time evolution | Tested reduced component ODE, holdout error, local identifiability diagnostics, solver-convergence test | Manufacturer-calibrated parameters, independent model-form validation, hot-weather transfer and coupled state dynamics **OPEN** |
| **SO3** — critical times, propagation and service outcomes | No experimentally qualified outcome in this run | Actual equipment limits, mapped EVSE control/service requirements and directional propagation evidence **OPEN** |

**Critical inference controls:**
1. Predictive RMSE improvement is **not** physical-model or causal validation; top-oil MAE worsened.
2. The measured ambient range does **not** support empirical validation under extreme heat above 30 °C.
3. The two-state top/bottom-oil model concerns **within-transformer states**, not Power-to-Transportation or Transportation-to-Power interdependencies.
4. No observed transformer loading caused by a linked EV charging site, thermally triggered charger limitation, field service shortfall, or measured thermal propagation delay has been demonstrated.
5. The new 0.2165/0.2517 result is from this **2026-11-11 rerun**. A separate earlier top-oil comparison (0.2147/0.2480 RMSE) used a different analysis/split. **Do not treat the two as identical tests or combine their baselines.**
6. Assistant-generated numerical work must be independently rerun/reviewed by the researcher and submitted to the supervisor before being promoted to an accepted thesis result or claimed as independently performed work.

## 7. Reproducibility and provenance ledger

- Local execution script: `thesis_advanced_experiments_20261111.py` (SHA-256 `eeccf0a62ef98933dea44b76c2dce4bb2bbe6ed33b6213fce8f93fcdaa77cb7d`).
- Local full machine-readable run output: `thesis_execution_20261111/results.json` (SHA-256 `a12c4d7e396287330273c84c05033f91edad95834a2b23cee528012d1ae991d8`).
- Local scientific report: `thesis_execution_20261111/RESEARCH_EXECUTION_REPORT.md` (SHA-256 `fe268ce89b42515fc821c1d9825bdbd14d7f7950572ff94a1ec856b23b894542`).
- Original inputs retained in the researcher's authenticated Drive dataset archive; original raw measurements are **not committed** by this record.
- Supporting independent source checks also included KU Leuven charging data and STREAM active/reactive power, **not used to fit** the presented SINTEF thermal model.
- This GitHub note is **a provenance summary, not a self-contained executable replication package**; the exact script/JSON referenced above are maintained separately unless subsequently committed with their checksums.
- Primary mathematical-method analogues (not fully reproduced): Powell et al. (2020), DOI [10.1016/j.apenergy.2020.115352](https://doi.org/10.1016/j.apenergy.2020.115352); Iaccarino et al. (2011), DOI [10.1016/j.ress.2010.06.030](https://doi.org/10.1016/j.ress.2010.06.030); Schiavazzi et al. (2017), DOI [10.1016/j.cma.2016.09.024](https://doi.org/10.1016/j.cma.2016.09.024); Xu and Darve (2022), DOI [10.1016/j.jcp.2021.110938](https://doi.org/10.1016/j.jcp.2021.110938).

**Review disposition:** WORKING / NOT FROZEN. Admit only component-level exploratory results. Require independent execution audit, sensitivity and identifiability work, equipment-specific parameter/limit evidence, and separate directed-thermal-interface evidence before any stronger claim.
