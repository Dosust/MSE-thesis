# EV-attributable transformer thermal ageing: candidate research metric

**Date:** 2026-11-05. **Status:** candidate metric and literature evidence; no transformer-ageing calculation performed or validated in this decision.
**Thesis:** Engineering of Power–Electrified Transportation Interdependencies for Resilience (official title V3).
**Research contract:** Frozen SO1–SO3 and extreme-heat thermal-only state–time scope unchanged; ageing is a **slow degradation/health indicator** derived from fast thermal dynamics, distinct from temperature, instantaneous capacity, service and resilience.

## Primary literature and prior-art finding

- Qian, K., Zhou, C. and Yuan, Y. (2015). Impacts of high penetration level of fully electric vehicles charging loads on the thermal ageing of power transformers. International Journal of Electrical Power & Energy Systems 65, 102–112. DOI https://doi.org/10.1016/j.ijepes.2014.09.040.
- Publisher abstract: models transformer life consumption stochastically using EV penetration/charging behavior, charging start time, initial EV SOC, charging mode and ambient temperature, with a UK generic LV distribution model and real load-demand inputs. The authors report ambient conditions, EV penetration and charging start time as major drivers, with smart charging generally reducing model-estimated life consumption. **This is established prior art for EV→transformer thermal ageing**, not a new thesis discovery.
- Related prior work: EV charging and transformer HST/ageing using real input data, Godina et al. (2016), DOI https://doi.org/10.1016/j.enconman.2016.04.087; EV ageing mitigation, Diahovchenko et al. (2022), DOI https://doi.org/10.1016/j.rineng.2022.100592; EV penetration with HST and loss of life, Energies (2023), DOI https://doi.org/10.3390/en16124810.

## 1. Physical pathway and observable hierarchy

EV charging sessions [W or kW] + other parent-feeder loads + ambient [degC] → actual transformer phase current/load factor → winding/oil temperature state → winding hot-spot T_H(t) [degC] → relative insulation ageing rate F_AA(t) [dimensionless] → equivalent ageing L_eq [hours].

**Distinguish observed versus derived:** HST may be directly measured by verified winding sensors (SINTEF candidate), while ageing acceleration and equivalent loss of life are **model-derived proxies for insulation deterioration**. They are not direct measurements of degree of polymerization (DP), actual remaining lifetime, or transformer failures. Real remaining-life inference needs insulation condition, age, moisture, oxygen, paper chemistry, sensor placement and calibration evidence.

## 2. Model equations — conditional on qualified insulation assumptions

**Illustrative thermally-upgraded cellulose relation** (widely used reference T_H,ref = 110 degC):

F_AA(t) = exp[15000/383 − 15000/(T_H(t)+273)] .

**Illustrative non-thermally-upgraded-paper IEC relation** (reference 98 degC):

V(t) = 2^[(T_H(t) − 98)/6] .

Do not combine those formulas without verifying paper grade, insulation design, oil/cooling regime and relevant IEC 60076-7 edition. No literal universal ageing threshold follows from either expression.

Over [t0,t1] in **hours**, equivalent ageing is L_eq = integral(F_AA(t) dt), measured in **reference-condition equivalent insulation-ageing hours**. For uneven sampled times use a declared quadrature (e.g. interval-weighted trapezoidal integration); do not simply sum sample values without the actual dt.

Equivalent ageing factor F_EQ = L_eq / (t1−t0), dimensionless. If a justified nominal insulation lifetime L_norm is available, the modeled *percent reference insulation life consumed* may be 100 L_eq/L_norm; do not report remaining years or failure probability without asset-level insulation condition and a validated survival model.

**Coupled comparison:** ΔL_EV = L_eq[ambient, same non-EV load + admitted EV charging] − L_eq[ambient, same non-EV load], in equivalent hours per operating scenario. Explicit assumptions and same initial HST/oil states required. A same-transformer controlled measurement or credible identification is needed to claim observed EV-attributable causality. If those inputs come from disjoint datasets, call the result a *physics-based scenario* only.

## 3. New metric register candidate

| Code | Quantity | Units | Evidentiary claim |
|---|---|---|---|
| H7a relative ageing acceleration | F_AA(T_H), with justified insulation-specific formula | per unit | Modeled ageing rate from observed or validated predicted HST, not direct measured lifetime |
| H7b cumulative equivalent insulation ageing | L_eq = integral F_AA dt | equivalent hours | Modeled ageing burden over a defined horizon; report quadrature, threshold assumptions and propagated HST uncertainty |
| H7c EV-induced marginal ageing | ΔL_EV between qualified with-EV and without-EV counterfactual | equivalent hours; scenario percent difference where denominator meaningful | **T→P thermal-degradation interdependency metric** if electrical parentage and scenario dynamics are qualified |
| H7d ageing-constrained charging | Maximum feasible EV energy/power or charging schedule subject to qualified thermal/ageing budget | kW; kWh | **P→T operating capability** only if validated constraint, topology and charging request available; otherwise model-only decision scenario |

Report F_AA peak, average F_EQ, L_eq, ΔL_EV, hot-hour sensitivity and credible interval bands (if uncertainties calibrated). **Nonlinearity warning:** HST estimation error is amplified by the Arrhenius ageing factor; testing ageing predictions from *measured* HST and from *estimated* HST on a held-out period is critical.

## 4. Benchmarks, thesis objectives and validation gates

- **SO1:** qualify actual transformer load path, ambient exposure, insulation design and HST-to-ageing relation.
- **SO2:** evaluate fast winding/oil ODE/PDE thermal states and slower cumulative ageing trajectory across time; thermal dynamics are not replaced by one ageing score.
- **SO3:** quantify critical time-to-thermal or ageing budget, thermal loading restrictions, loss of charging service and possibly scenario-defined mitigation/recovery; do not confuse asset ageing with immediate mobility outage.
- **IEC/IEEE-type ODE baseline** and **physics-based mechanistic model** are required comparators; **PINN** is a conditional candidate. **FVM** is conditional on available spatial boundary/sensor data and convergence evidence.
- **Same test set:** train/calibrate on designated earlier SINTEF measured winding HST, test chronologically on unseen measured HV/LV HST. For each estimator use identical ageing law/insulation assumption and time horizon when comparing derived F_AA and L_eq; report estimator errors alongside derived-ageing errors.
- **Independent ageing ground truth:** SINTEF measured winding hot-spot temperature does *not* by itself validate real cellulose chemical ageing or remaining life. HST-derived ageing is a second-stage model quantity. Direct DP/furan/chemical-condition data and insulation calibration would be necessary for independent empirical ageing validation.
- **Coupling:** the 40 MVA SINTEF transformer has no verified parent EV charger/EV charging request in inspected public metadata. Its measured HST supports component validation, not field EV-induced ΔL_EV or actual charging restriction.
- **Extreme heat:** Norwegian operating measurements cannot automatically validate heatwave extrapolation. Test only transparent extreme-heat scenarios with parameter/uncertainty sensitivity unless actual high-ambient calibration/validation data exist.

## Scientific decision

Accept **transformer relative thermal ageing and equivalent loss of insulation life as H7 candidate**, with **EV-attributable differential ageing ΔL_EV** a strong candidate T→P interdependency metric. It complements H1 observed-HST validation, H2 headroom, H3 marginal thermal rise and H5 thermal charging/service constraints. The original paper established EV charging–transformer ageing decades before this thesis, so novelty must come from a demonstrably new *qualified coupled state→capability→service* analysis, not from proposing EV-based transformer ageing alone.

**Status:** METRIC_CANDIDATE_REGISTERED | MODEL_FORMULA_CONDITIONAL | NO_HST_OR_AGEING_COMPUTATION_EXECUTED | NO_EV_CONNECTED_HST_MEASUREMENTS | FREEZE_SO1_SO3_UNCHANGED
