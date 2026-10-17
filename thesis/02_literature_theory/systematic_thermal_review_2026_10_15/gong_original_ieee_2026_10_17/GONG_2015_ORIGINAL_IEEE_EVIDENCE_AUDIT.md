# Gong et al. (2015) — ORIGINAL IEEE publisher PDF: thermal physics, controls, and experimental-evidence audit

**Access event:** 2026-10-17. Full nine-page original IEEE Xplore PDF supplied by the researcher through ASU-authorized access. The file remains in authorized local conversation storage and is NOT uploaded to this repository.
**Verified identity:** Q. Gong, S. Midlam-Mohler, E. Serra, V. Marano, G. Rizzoni, *PEV Charging Control Considering Transformer Life and Experimental Validation of a 25 kVA Distribution Transformer*, IEEE Transactions on Smart Grid **6**(2), 648–656, March 2015. DOI: https://doi.org/10.1109/TSG.2014.2365452. Publisher authorization watermark says ASU download 2026-10-17 05:26:41 UTC. Local SHA-256 **88fe4d90b8bad8eca82d9a598b3ba49135943a17b1a6c5217682b271a8b0f0b2**; 9 PDF pages.
**Source standard:** Exact original equation numbers and printed journal pages below. The numerical thermal differential equations in the control model are chiefly **adopted/cited** from Susa et al. (2005), IEEE C57.91, and Gong et al. (2012), NOT independently laid out in detail as standalone thermal ODEs in this 2015 paper. Do not attribute a made-up full ODE to Gong (2015).

## Physical architecture and scope
- One **25-kVA residential oil-immersed distribution transformer**, six-house/six-PEV *simulation* setup, predictive aggregate PEV charging coordination (pp. 649–651).
- Measured experiment: programmable environmental chamber, **DC current fed to both windings** with compensation to reproduce losses of AC operation; no real PEV charge station is a measured experimental component (pp. 651–652). This tests a P transformer's response to imposed thermal/electrical load schedules, **not** simultaneous matched utility-transformer ↔ working EVSE measurements.
- The controllable coupling is **EV charging scheduled aggregate electrical load u(s) → transformer winding/oil heat**, and optimized response of PEV charging schedules to modeled transformer life. A field-observed charger rectifier-temperature-to-upstream-transformer-temperature propagation is NOT measured.

## Full equation map and semantic guardrails
| Source | Relationship/source function | What is and is not established |
|---|---|---|
| Eq. (1), p. 650 | Ambient-temperature-augmented ARMA load forecast, using lagged base-load ratio L and ambient temperature theta_amb. Model orders M1=M2=48 using hourly Columbus, OH base load/ambient data. | **Forecast/data-driven**, NOT heat-balance equation. Prediction horizon 12–24 h; repeated updates limit accumulation of forecast error. |
| Eq. (2), p. 650 | Minimize summed forecast-horizon transformer insulation loss of life J_lol = sum_s f(theta_oil,theta_hs,u,theta_amb,Delta t_s). | Hotspot theta_hs is **model-estimated**, not directly measured. Transformer aging functional f is adopted from prior thermal model. |
| Eq. (3), p. 650 | Charging energy-demand balance, sum_s u(s) Delta t_s = sum_k Delta SoC_k C_k + delta(l). | delta(l) encodes unknown future arrivals; charging energy fulfillment is a planning constraint, not observed real-vehicle delivery in thermal experiments. |
| Eq. (4), p. 650 | Aggregate controllable charging power cap u(s) <= sum_k g(Delta SoC_k). | Battery charging curve bounds (not empirically heat-conditioned EVSE derating). |
| Eqs. (5)-(6), p. 651 | Source-defined departure-charge satisfaction proxy f_sat = mean(Delta SoC) + range(SoC), and weighted joint objective J = alpha J_lol + gamma f_sat, expressed as minimization. | **Sign/normalization ambiguity:** the paper describes maximizing satisfaction but prints a positive weighted minimization; do not implement this unchanged without verifying meaning of Delta SoC and signs in Gong's cited [19]. |
| Eq. (7), p. 652 | Transformer loss decomposition P_loss = P_dc + P_ac. | Experimental electrical *loss accounting*, not an independently fitted first-principles spatial heat equation. |
| Eq. (8), p. 652 | Equivalent DC test-current compensation: I_total^2 R_w = I_dc^2 R_w + P_ac. | P_ac ≈ 51 W is stated for this particular transformer; DC excitation models heating rather than reproducing real energization/AC electromagnetic behavior. |
| Eq. (9), p. 653 | Top-oil calibration discrepancy J_oil = (theta_oil,sim(t) - theta_oil,test(t))^2. | Paper describes search/minimization across tested data; printed equation does not itself specify aggregate over time. No fully specified held-out calibration-split statistics. |
| Eq. (10), p. 653 | Winding resistance R_w = V_w / I_w. | Direct electrical measurement during resistance experiments. |
| Eq. (11), p. 654 | Winding resistance vs temperature: R_w = R_0(1 + beta Delta T). | Primary beta=0.0044071 K^-1; secondary beta=0.0043361 K^-1. Component-specific measured coefficients, not universal. |

## Sensors and boundary semantics (pp. 651–652, Fig. 2)
- **4 top-oil sensors**, **4 oil-depth sensors**, **4 tank sensors**, **2 ambient sensors**; **2 hypodermic needle probes near the top of the windings**. Authors explicitly say top-winding temperature is **not true hot-spot temperature**.
- Programmed environmental chamber ambient time series; DC test-current profiles based on load ratio/scheduled charge profiles.
- Sensor models listed (NI acquisition, OMEGA thermocouples/needle probes) but full point-by-point uncertainty and raw test observations are not published in this PDF. No formal out-of-sample multi-transformer/sensor-position validation.
- **Mathematical state guard:** observed winding top T_w,top(t) != latent true maximum hotspot T_hs(t); experimentally measured oil T_o(t) != winding hotspot; observed transformer P temperature != observed EVSE internal heat.

## Calibration values and physical time scales (p. 653 Table II)
Table II fit values [load ratio K: rated oil rise °C, rated oil tau minutes, fitted winding rise °C, fitted winding tau minutes]:
- K=0.4: 50,100,18,26
- K=0.6: 50,180,16,52
- K=0.8: 40,155,15,42
- K=1.0: 35,155,16,46
- K=1.2: 32,165,18,60
- K=1.3: 30,150,17,56
The paper discusses the simulation-model **true hot-spot** winding rise 30 °C and time constant **6 min**, while measured **top-winding** fitted time constants are much slower (43–60 min near K=1). These are not interchangeable states. Rated oil model initially takes 38 °C and 150 min (p. 653). The varying Table II fit values are not a universally identifiable constitutive material law.

## Validation and scope (pp. 650–655)
1. **Control schedules and forecast (simulation):** six houses/six PEVs, baseline utility base-load profiles and survey-derived plug-in/departure times, Monte Carlo initial SoC; ARMA model with real base-load updates. In Table I, strategy B changes reported F_EOA 0.3867 → 0.3521 with updates, but the mathematical definition of the performance metric is not re-derived here (cited [19]); avoid rebranding this as field kWh or temperature accuracy.
2. **Component calibration (physical):** stepped thermal load ratios K = 0.4,0.6,0.8,1.0,1.2,1.3. Figure 4 compares modeled vs tested oil-temperature response at K=0.8.
3. **Control validation (physical P testbed):** same transformer under programmed ambient temperatures and schedules, 6-h thermal warmup; compare prescribed charging-load schedules on *measured top-winding* temperature (Fig. 7). Figure 6 shows **simulated hotspot**, Fig. 7 **observed top-winding**. Optimized schedules reduce measured top-winding peak relative to average charging load. No physical vehicle/EVSE charging session measured.
4. **Varying load+ambient challenge (physical P testbed):** Fig. 8 compares measured and modeled top-winding and top-oil traces. Authors report **maximum absolute prediction errors <2 °C for top-winding** and **<4 °C for top-oil** (p. 655). Same tested transformer; do not call this independent site/external-device validation. No MAE, RMSE, time-aligned dataset or uncertainty bounds provided for that test.

## Scientific novelty and thesis model implications
**Demonstrated prior art**: (a) transformer-aware EV charging scheduling, (b) physics-based transformer thermal response plus life minimization in charging optimization, (c) experimental *P component* model calibration and P temperature-peak reductions caused by imposed scheduled electrical loads, (d) time-varying ambient in P chamber. Consequently claims of 'first EV charging control incorporating transformer thermal life' or 'first experimentally validated P transformer heat response to scheduled EV-equivalent loading' are untenable.

**Not demonstrated here**: real EVSE internal T_ch(t)/limiter/AC-DC output observed jointly with utility transformer T_P(t), time-synchronized receipt of EVSE heat-conditioned electrical action at P equipment, actual electric-mobility trip/departure service completion, an empirically identified full dynamic two-way thermal receiving relationship, distinct geographical-site replication, or measured utility HST. DC-equivalent test heating is **not physical heat conducted from charger to transformer**.

**Candidate coupled physics architecture (thesis derivation, not Gong's original equations):**
- Transformer energy balance C_P dT_P/dt = P_loss,P(I_P,theta) - Q_reject,P(T_P,T_a); electrical input I_P reflects EVSE AC demand and other loads.
- EVSE thermal energy balance C_E dT_E/dt = P_loss,E(P_AC,P_DC,theta) - Q_reject,E(T_E,T_a); controls constrain offered power if actual derating law exists.
- Electrical P→T_E capacity/demand and T_E→P AC load feedback must be separately causal-tested; **do not** invent a direct material conduction term between geographically separated units.
- Test P side with measured top-oil or top-winding (never label an unobserved hotspot 'measured'); use Krama for charger-side measurements with separate same-site P sensor gap.
- The RACE 2025 temperature-triggered charger controller and Gong 2015 measured transformer thermal schedule-effect both already constrain novelty.

## Next gates
- Kunlasing et al. (2022), DOI 10.1109/ECTI-CON54298.2022.9795360: original IEEE paper still not obtained. Author/IEEE access route required; do not infer transformer thermal probe or heat-triggered charger controller from the title.
- Crosscheck Gong [18] (2012 IEEE Smart Grid), [19] (2012 IEVC), [22] (Susa 2005) for governing thermal dynamic equations and service objective meaning. Do not silently assign their exact equations to this PDF.
- Krama 2026: original experimental raw data still not received, despite user reporting request sent; separate validation gate.
