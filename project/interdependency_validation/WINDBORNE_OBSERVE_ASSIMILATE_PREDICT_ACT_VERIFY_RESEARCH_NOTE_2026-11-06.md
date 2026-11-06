# WindBorne methods as a research analogue for validating thermal P–EV interdependencies

**Date:** 2026-11-06
**Status:** FUTURE RESEARCH / INNOVATION WATCHLIST — NOT VALIDATED, NOT EXECUTED, NOT A NOVELTY CLAIM.
**Scope:** Physically conditioned, time-state-dependent Power ↔ Electrified Transportation thermal interdependencies under extreme heat, corresponding to existing frozen SO1–SO3.
**Authority:** JBI-guided scoping protocol v0.3 remains a researcher-approved *working* protocol, without recorded supervisor signoff. This engineering inspiration is **NOT** an automatically included peer-reviewed systematic-review record.

## 1. Core research insight

WindBorne demonstrates a practical systems-engineering logic: capture qualified observations → estimate current state → forecast future state and uncertainty → deliver decision-relevant forecasts → compare against strong independent benchmarks.

**Thesis translation, not an alleged WindBorne architecture:** OBSERVE → SENSOR/PROVENANCE QA → ESTIMATE → PHYSICS-BASED COUPLED PREDICTION → UNCERTAINTY/FORECAST FUSION → THERMAL-STATE-CONSTRAINED CHARGING CONTROL → VERIFY SERVICE AND RECOVERY.

The thesis should pursue scientific advance **module by module**: a candidate mechanism, its law, its measurements, its independent validation, its benefit to downstream decisions, and a clean negative-control or ablation. Merely adding AI or combining modules is not evidence of originality.

## 2. Public-source evidence — verified 2026-11-06

| Source | Company-documented facts | Transferable idea; limitation |
| --- | --- | --- |
| [GSB observation API](https://api.windbornesystems.com/atlas/version_1/observations/in-situ-data/) | Long-duration atmospheric sounding balloons measure temperature, humidity, pressure, wind, location and time. API documentation describes 10-second onboard observation cadence, periodic transmission and automated QC, with unequal variable acceptance rates. | Explicit physical sensor/operator/latency and QC audit. **Balloon data are not grid current, transformer HST, EVSE temperature, charger control or mobility service data.** |
| [WindBorne AI DA (2025)](https://windbornesystems.com/blog/windborne-ai-da) | Distinguishes estimating current atmospheric state from forecasting the future; describes combining noisy heterogeneous observations, company-reported performance on one meteorological benchmark. | Real measured data must correct hidden physical states; company performance is not independently reproduced. Do NOT claim proprietary DA was a Kalman filter. |
| [WeatherMesh-6 documentation](https://api.windbornesystems.com/models-measurements/about-our-models/weathermesh-6/) | Global model roughly 0.25-degree, 128-member ensemble, hourly initialization and 15-day horizon; multiple observational inputs, ±15-minute assimilation window. The regional model is different. | Ensemble ambient-temperature forcings and probabilistic predictions **if accessible**. Coarse-grid ambient cannot replace calibrated local site temperatures without verification; historical datasets are subject to separate access. |
| [MetaMesh (2026)](https://windbornesystems.com/blog/introducing-metamesh) | Deterministic blended point forecast, using AI and numerical weather model inputs; lead/variable/region/season-dependent weighting, ongoing update and blocked validation description. Company-reported improvements. | Compare dynamically fused predictions against *best single* forecast and all non-fused baselines, with correct chronological validation. **MetaMesh is not WeatherMesh's 128-member ensemble** and public information does not make proprietary blend coefficients available. |
| [Forecast products](https://windbornesystems.com/products/forecasts) | Forecast variants, spatial and temporal coverage and historical-data access differ by product and version. | Archive source model/version/forecast issue time/valid time; do not assume API access or retrospective availability. |

**Terminology warning:** "Transformer" machine learning in weather forecasting is not an electrical distribution transformer.

## 3. Mathematical synthesis proposed for the thesis

### 3.1 States, topology and observed quantities

For transformers b and EV charging sessions i, use a *candidate* state vector:

\[
x(t)=[\theta_{\mathrm{oil},b},\theta_{\mathrm{hotspot},b},T_{\mathrm{EVSE},i},T_{\mathrm{battery},i},SOC_i,\ldots]^T.
\]

Assign every state to (a) direct sensor, (b) model-derived and independently calibrated, (c) unobserved scenario state or (d) not identifiable. EVSE internal temperature must not be inferred from EV battery temperature.

Explicitly track parent transformer → feeder/phase → charger/EV relationship. Without certified network connectivity and clock alignment, a cross-site combined time series is a **synthetic coupled scenario**, not field validation.

### 3.2 Electrical interface (conditional)

\[
P_b(t)=P_{\mathrm{base},b}(t)+\sum_{i\in\mathcal E(b)}p_i^{AC}(t)-P_{\mathrm{DER},b}(t),
\quad
Q_b(t)=Q_{\mathrm{base},b}(t)+\sum_{i\in\mathcal E(b)}q_i^{AC}(t)-Q_{\mathrm{DER},b}(t).
\]

Network electrical feasibility is \(g_{\mathcal N}(V,I,P,Q)=0\), with correct phase, metering and sign conventions. Optional charger reactive power must satisfy real converter capabilities, e.g. \(p_i^2+q_i^2\le S_{i,\max}^2\) only for verified controllable P/Q hardware. RMS voltage × RMS current does NOT always equal active power.

### 3.3 Heat balances and thermal memory

A dimensionally consistent illustrative reduced model:

\[
C_o\dot\theta_o=P_{\mathrm{loss}}(I,\theta)-H_o(\theta_o-T_a),\qquad
C_w\dot\theta_h=P_{\mathrm{winding}}(I,\theta)-H_w(\theta_h-\theta_o).
\]

Here C [J/K], P [W], H [W/K]. Identify parameters only from sufficient measured excitation. Compare against independently implemented IEC 60076-7 / IEEE C57.91-type thermal baselines; do not call these simple illustrative equations the exact standards. Thermal-temperature evolution is not, on its own, a measured derating command or observed lost transformer life.

An optional EVSE component is

\[
C_c\dot T_c=P_{\mathrm{converter\ loss}}-H_c(T_c-T_a)
\]

if source data and coefficients support it. The battery SOC law requires AC-to-DC efficiency, auxiliary loads and consistent units, such as \(dSOC_i/dt=p_i^{DC}/E_i\) with energy in joules and power in watts.

### 3.4 Hidden-state estimation, NOT invented observations

Propose
\[
x_{k+1}=f_\vartheta(x_k,u_k,T_{a,k})+w_k,\quad
y_k=h_{\mathcal M}(x_k)+v_k,
\]

with explicit observation operator \(h_{\mathcal M}\), quantified noise and a verified sampling clock. A Kalman-family filter is a **candidate experiment**, not known WindBorne source code. For an EKF illustrative update:

\[
K_k=P_k^-H_k^T(H_kP_k^-H_k^T+R_k)^{-1},\quad
\hat x_k^+=\hat x_k^-+K_k[y_k-h(\hat x_k^-)].
\]

Check observability and identifiability before assimilation; a fitted SINTEF HST trace does not thereby reveal an unmeasured EVSE temperature or charger restriction.

### 3.5 Ensemble forecast → thermally constrained event risk

If genuine archived forecast member trajectories or clearly labeled statistically qualified weather scenarios \(T_{a}^{(m)}\) exist, propagate each with the same physically calibrated system:

\[
\hat p_{\mathrm{cross}}=
M^{-1}\sum_{m=1}^M
\mathbf1\{\max_{1\le\ell\le H}\theta_{h,k+\ell}^{(m)}>\theta_{\lim}\}.
\]

This empirical fraction is **not automatically a calibrated probability**. Validate event calibration and sharpness on independent observed HST exceedances where available (Brier score, reliability, proper scoring); label simulated high-heat event rates as simulated. Keep forecast issue time strictly before any target event; do not mistake a later reanalysis for an operational forecast.

### 3.6 Service and decisions

The energy deficit for session i is illustratively

\[
U_i=\max\left(0,E_i^{\mathrm{requested}}-\int_{t_i^{arr}}^{t_i^{dep}}p_i^{DC}(t)\,dt\right).
\]

This is an energy-service proxy, **not evidence of an actually canceled trip**. Constraints include verified network, charger, voltage, transformer temperature, EV battery and time/departure requirements.

A candidate multiobjective predictive control problem is to minimize the expectation of appropriately scaled electrical-loss energy, thermal-ageing proxy, and unmet charging energy subject to state equations and operational constraints. Compare best single baseline and ablative variants before any positive performance claim.

### 3.7 Event times and recovery

\[
t_{\rm cross}=\inf\{t:\theta_h(t)>\theta_{\lim}\},\quad
t_{\rm restrict}=\inf\{t:\text{recorded thermal-related charger restriction imposed}\}.
\]

The signed \(\Delta t=t_{\rm restrict}-t_{\rm cross}\) may be negative if restrictions are preventive. An unrecorded hypothetical restriction is a **scenario policy**, not an observed P→T event.

Recovery must be defined by restoration of a physical or service threshold, duration of restoration and pre-disturbance baseline. A drop in HST alone does not show recovery of vehicle charging or transport service.

## 4. Seven interdependency validation gates

| Gate | What constitutes valid evidence | Main alternative explanation |
| --- | --- | --- |
| I1 T→P electricity | Physically mapped charger P/Q with feeder transformer I,V and timestamps | Other loads, DER, phase error or unverified parent mapping |
| I2 T→P thermal | Matched charge/asset electrical signals, ambient T, top-oil/HST and heat model | Ambient/weather and non-EV baseline loads explain HST |
| I3 P→T restriction | Recorded transformer/voltage constraint, control decision and measured EVSE response | BMS, charger cooling or user-session completion caused the power reduction |
| I4 Service effect | Requested vs delivered kWh by deadline, with session/mission evidence | No user-requested energy; do not infer actual missed mobility |
| I5 Propagation delay | Synced event states and pre-defined change-point logic | Clock offset, aggregation or common cause |
| I6 Recovery | Restored control and independently verified resumed electricity/charging service | Only temperature or voltage returned to baseline |
| I7 Sustainability | Electrical losses, valid thermal ageing proxy and documented emissions accounting if claimed | Energy loss is not CO2; ageing acceleration is not observed life lost |

Proposed P→T and T→P chains are **separate proofs**. A T→P loading/HST association does not establish bidirectional causality.

## 5. Source and dataset qualification now

- **SINTEF Barug measured transformer:** approximately 8,592 hourly measurements of transformer current, ambient, oil/HST; strong component candidate for reduced physics and state estimation. Not observed extreme heat or an EV-connected parent transformer. Source-original CSV is authoritative; a previously assessed Drive Google Sheet suffered numeric-to-date coercion. Historical ambient max around 25.97°C.
- **KIT 50-day OLTC campus:** electricity/voltage/charging co-response source candidate; physical topology/phase and non-EV baseline attribution require further verification, not synchronized HST.
- **KIT PHIL / OSF laboratory:** component EV power-quality/electrical measurement; no same-site transformer HST; no automatic real-W inference from RMS U×I.
- **Slovenia STREAM P/Q:** measured electrical loading candidate once sign, units, ratings and station map are confirmed; not co-sited with SINTEF thermal sensors.
- **KU Leuven / EPFL / TUM EV:** distinct charger/battery components, with time, channel, sentinel and thermal-sensor boundary checks; battery temperatures are not charger semiconductor temperatures.
- **Iowa 296-node:** measured/derived household loads and assumed, not observed, Q; no verified feeder schematic in user archive.
- **WindBorne/other meteorological forecasts:** *possible* boundary inputs after source access, coordinate/height correction, issue-time provenance and local ambient validation. No WindBorne API downloads or integration were performed for this note.

**Current connected-system status:** Based on previous Drive–GitHub audit, no verified same-site dataset jointly supplies ambient, parent transformer electrical+HST, EVSE P/Q and charging control, plus requested/delivered service. Recheck this gate if new evidence arrives; NEVER merge separate installations as one measured system.

## 6. Falsifiable experiments and ablations

Run in the following order, using fixed input data/split and physically matched constraints:

1. **Thermal component baseline:** persistent temperature / standard thermal ODE / calibrated reduced ODE / ODE+estimator on independent chronological SINTEF splits. Compare HST MAE/RMSE, peak time, residual heat balance, confidence intervals and parameter identifiability.
2. **Charging component:** verify converter P/Q and thermal behavior, AC vs DC boundaries, user session deadlines; independent measured holdouts where possible.
3. **Coupling:** only after physical links are verified or an explicit synthetic network mapping exists; check no-load EV, no-temperature effect, no-thermal-memory and disconnected-network negative controls.
4. **Forecast value:** compare static ratings, state-aware without forecast, weather forecast only, assimilation-updated, ensemble uncertainty and optional blended forecast (if source forecasts available). Do not train on the scoring window.
5. **Mechanism ablations:** remove transformer thermal inertia; remove EVSE cooling/derating; remove parent-feeder electrical effects; remove uncertainty; remove service deadlines. Quantify which mechanism changes critical crossing time and unmet demand.
6. **Service and resilience:** compare critical-transition timing, false alarms, actual/simulated restrictions, recovery delay, charging kWh requested/delivered and thermal violations. If user trips are not observed, label service as proxy.
7. **Energy and sustainability:** compare real network loss, ageing acceleration as proxy, and emissions only with justified grid factors. Estimate paired uncertainty and do not cherry-pick one hot day.

### Hypotheses (not yet accepted or validated)

H1. Thermal memory predicts critical restrictions better than static thermal rating during matched hot-demand scenarios.
H2. Qualified observation assimilation improves held-out transformer HST or event-risk estimates beyond calibrated physics-only ODE.
H3. Coupling transformer thermal constraints to charging-power capability changes unmet service and recovery estimates vs electricity-only/schedule-only model.
H4. Forecast ensembles/fusion improve out-of-sample service decisions beyond the best feasible single forecast, accounting for operational latency and computation.

Pre-register endpoints, baselines, temperature-domain support, forecast-issue chronology and statistical testing before running comparisons. "Novelty" is open: closest papers on EV charging, thermal ageing, reactive-power control and service outcomes must be compared.

## 7. Execution protocol and hold points

LEARN → VERIFY → FORMULATE → DERIVE → TEST → VALIDATE → SYNTHESIZE → ADVANCE.

| Hold point | Pass condition | Status as of this note |
| --- | --- | --- |
| G0 Provenance | Original DOI/metadata, units/time/source checksums | Partial |
| G1 Physical topology | Same-site electrically verified transformer–charger pairing | OPEN |
| G2 Thermal observability | Genuine matched oil/HST/current/ambient; identifiable model | Transformer component only |
| G3 Actual P→T restriction | Grid/transformer restriction command with EVSE power response | OPEN |
| G4 Service consequences | Requested and delivered charge by departure; recovery observed | OPEN |
| G5 Forecast calibration | Out-of-time observed weather and threshold event scores | NOT RUN |
| G6 Comparative decision benefit | Physically feasible best-baseline improvement with ablations | NOT RUN |
| G7 Scientific novelty | Validated advantage + full closest-prior-art boundary | NOT ESTABLISHED |

### Versioned future deliverables (not created now)
- interdependency_link_register.csv — source/target asset, parent topology, direction, sensor, clock, unit, observed/synthetic status, alternative causes.
- observation_state_observability_matrix.csv — state equations, sensor observation operator, identifiability, uncertainty.
- transformer_thermal_validation_report.md — original CSV and source hashes, splits, fitted physical parameter diagnostics, independent holdout.
- forecast_issue_time_manifest.csv — model, initialization/valid time, location, variables/units, members, availability.
- matched_coupling_ablations.csv — shared physical scenarios, controls, reproducible seeds, per-mechanism differences.
- evidence_and_novelty_gates.md — PASS/FAIL/BLOCKED status with provenance and exact justification.

## 8. Prohibited inference boundaries

- Do NOT say WindBorne has demonstrated P–T electrical/thermal coupling.
- Do NOT present WindBorne company benchmarks as independently reproduced thesis improvements.
- Do NOT treat WeatherMesh Global as measured local ambient temperature or MetaMesh as a 128-member ensemble.
- Do NOT treat cross-site SINTEF+KIT+TUM+Slovenia as synchronized field observations.
- Do NOT report coupling-based recovery or trip cancellations without service and event evidence.
- Do NOT say optimized electricity losses prove CO2 savings without emissions information.
- Do NOT report unverified novelty or an experiment as completed.

**Disposition:** RETAIN for later SO1 interface-observability design, SO2 state-time thermal/charging estimation and SO3 critical timing/charging-service model validation. No new measured data, AI training or climate-forecast API use is claimed.

## Source links
1. https://api.windbornesystems.com/atlas/version_1/observations/in-situ-data/
2. https://windbornesystems.com/blog/windborne-ai-da
3. https://api.windbornesystems.com/models-measurements/about-our-models/weathermesh-6/
4. https://windbornesystems.com/blog/introducing-metamesh
5. https://windbornesystems.com/products/forecasts
6. https://github.com/alliander-opensource/transformer-thermal-model — open-source IEC thermal model lead, not benchmarked against thesis measurements in this note.
