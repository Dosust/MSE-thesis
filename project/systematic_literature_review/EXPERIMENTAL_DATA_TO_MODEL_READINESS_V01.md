# Experimental data vs mathematical model readiness v1.0

**Date:** 2026-11-03. **Status:** source audit from existing measured-data report and literature; **NOT newly qualified connected thermal field data**. [Scientific RQ1–RQ11 checkpoint](../data_qualification/2026-11-03/THESIS_RESEARCH_CHECKPOINT_2026-11-03.md).

| Dataset/source | Actual measurements and readiness | Models it can credibly inform | What it cannot establish / action |
|---|---|---|---|
| SINTEF Bærug DOI 10.5281/zenodo.17223516 | **8592 hourly measured samples**, load/current, ambient and top-oil, max ambient **25.97°C**; source checked | Transformer one-site conditional temperature response, holdout predictors, possible reduced physical model after proper parameters and boundary | No extreme-hot field transformer case or linked EVSE; effective fitted statistical coefficients ≠ unique loss/cooling/heat capacity; calibrate real physics and compare external |
| STREAM Slovenia DOI 10.5281/zenodo.20927130 | **12 sites × 34932 common quarter-hour P/Q observations** | Electrical loading/temporal demand variability if meter sign, rating and units validated | No measured oil/hotspot or connected charger thermal state; nameplates DOI 10.5281/zenodo.20927801 must be checked |
| KU Leuven DOI 10.48804/C5PT0R | Real lab battery/SOC/current/voltage/charging and thermal channels | Component battery/charging dynamics and electrical AC/DC boundary | Site unrelated to SINTEF; clock reversals, SOC reset and apparatus variables must be verified before thermal fitting |
| OSF DOI 10.17605/OSF.IO/94GKC | Laboratory EV charging under electric supply disturbances, 313 source CSV entries including empty supplements | Battery current/charge response under disturbances and quality assurance; interface confounder exploration | No joint charger thermal + feeding transformer link or heatwave field test; do not equate AC−DC power with observed rejected heat |
| TUM original EV UDS repository | Seven real production EV Parquet logs user-local; ID1 **40,401,700 long-format** readings, ambient up to **39.5°C** in sampled analysis | Vehicle-side external observational data **if decoded and synchronized** | 1023°C-like sentinel/unphysical channels, exact sensors, charging-state overlap, seven hash manifests pending; no modeled heat/field readiness until QC |
| Krama/Qatar DOI 10.1016/j.ecmx.2026.101960 | Commercial 50kW DC charger hot-climate field record in published paper, offered/delivered power and rectifier temperature; **raw on request** | EVSE thermal-derating law conditional on obtaining raw, units, sensors, controls | Published fitted model is not downloadable synchronized dataset or same-source transformer temperatures |
| Li et al. DOI 10.1109/PESGM58988.2026.11693150 | Same-station transformer primary/secondary **electrical** measurements at an operating e-bus depot | Electrical interface, harmonics/loss accounting, physical site boundary | Oil/winding and EVSE-internal thermal signals and operator reason codes **not verified**; need full apparatus/raw |
| RACE 2025 | Simulated EV charge delivery and relative aging with transformer thermal model informed by heat-run tests | Physical model family and conditional intervention comparison | Not published measured severe-heat linked charger–transformer field time series/service outcomes |
| OPSD original RQ6 source | Station/load/EV data lead from old research | Conditional net demand/charging comparison | Co-located EVSE and transformer thermal channels not established; original match and holdout not complete |

## Model admission by observability

**Measured thermal state** is not sufficient on its own. For a candidate equation \(C\dot T=P_{\mathrm{loss}}-Q_{\mathrm{rej}}\), identify current/forcing, loss law, cooling/ambient conditions, sensor location, units, time stamp/variation and independent holdout. A good statistical fit to \(T_{\mathrm{top-oil}}\) does **not** uniquely identify \(C\), \(P_{\mathrm{loss}}\), or heat transfer properties.

**Network interface** requires observed topology, AC meters, time-aligned charger operation, specific transformer thermal/operating limits, explicit actual operator restriction, and battery/charging service requirements. Avoid adding Norway+Slovenia+Qatar+TUM rows as if one physical connected installation.

## Decision gates

- **Component physics baseline**: supported for a qualified transformer component as a research path; actual physical parameters need checking. **Partial**.
- **EVSE field derating inverse model**: source published, raw and exact channel meanings needed. **Data access pending**.
- **Vehicle battery thermal PIML**: only after TUM/Leuven sensor and charging-event QA. **Conditional**.
- **Connected transformer↔EVSE causal PIML**: no jointly qualified observed site; **BLOCKED**.
- **Extremely hot transformer field validation**: none yet from SINTEF range; **BLOCKED in original current record**.
- **Observed fleet missed trip / recovery**: no connected field service observations; **BLOCKED**.

**Next request:** obtain original Qatar data, Li instrumentation/raw measurement boundaries, RACE follow-on field report (if released), connected depot/utility weather+electrical+transformer+charger logs, and experimental controller reason codes. If access not possible, report simulation-only coupling with explicit evidence ceilings.
