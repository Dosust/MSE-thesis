# Report 8: Evidence-ranked thesis findings and objective traceability

## Evidence status matrix

| Result | Level | What it establishes | Does NOT establish |
|---|---|---|---|
| SINTEF ODE 1h RMSE 0.2165 vs persistence 0.2517 °C | Tested component prediction | Restricted one-step model prediction error | Full physical validation, extreme-heat transportability |
| 106-window equal-current-square permutation: 0.355 °C median final difference | CONDITIONAL MODEL SIMULATION | Thermal inertia makes input timing relevant in the fitted SINTEF one-state model | Actual charging schedule implementation or measured interdependency |
| Seasonal effective tau 15.98, 8.29, 13.57 h | CALIBRATION SENSITIVITY | Estimates depend on estimation regime | Structural non-identifiability proven |
| Hot-spot below top-oil in 84.1% HV and 70.9% LV | Observational sensor check | Sensor-definition and local-temperature questions | Incorrect sensor claim; true maximum winding hot spot; insulation life use |
| EPFL hypothetical 16-day median peak reduction 44.01% | SOLVED OFFLINE OPTIMIZATION | Feasible modeled power redistributions under assumed deadlines/limits | Measured site benefit, user request satisfaction, aging reduction |
| EPFL day-block daily max concurrency mean 1.706 | Descriptive sample statistics | Arrival/dwell concurrency in the archived site record | Other-site demand distribution or EV penetration thermal impact |
| KU Leuven 40,873 temperature/electrical rows | Descriptive component evidence | BMS pack-temperature channels exist | Internal charger thermal derating |
| STREAM 419,184 matching P/Q numeric pairs | Descriptive electrical evidence | Station-time P/Q values exist | Qualified power factor, feeder rating, thermal loss or linked EVSE |
| Empirical residual-band coverage 95.3% | Conditional numerical calibration | Split-specific one-hour residual inclusion | Calibrated physical-probability guarantee or extreme-heat UQ |

## SO1, SO2, SO3

- **SO1 (mechanisms):** Measured transformer and EV/battery component states and electrical interfaces support *candidate* directional mechanisms. Still **NO** independently verified cross-site thermally conditioned source-to-recipient mechanism, EVSE control action or co-located causal response.
- **SO2 (state-time):** Verified execution of reduced transformer ODE and analytical/numerical time integration, model-fit diagnostics, seasonal refits and within-transformer load-order mathematical experiments. **Partial component-level success**, no validated coupled physical state dynamics under extreme heat.
- **SO3 (service and propagation):** Feasible energy-preserving EPFL offline scheduling *under assumed session flexibility*, but not an observed thermal constraint or actual electricity/mobility service shortfall, propagation delay, critical transition or recovery. **BLOCKED for coupled-thermal service evidence.**

## Mapping the five methodological sources without overstating reproduction

| Paper | Transfer made | Reproduction status |
|---|---|---|
| Nishanth (2026), transformer PINN/PDE | Physical heat-balance and temperature-state reasoning for a conventional lumped ODE; not PINN or spatial PDE | `METHODOLOGICAL_ADAPTATION` (full paper/math unavailable; PINN outside scope) |
| Qian, Zhou & Yuan (2015), FEV charging and transformer aging | EPFL observed session arrival/dwell/energy dependence; SINTEF within-transformer load-order timing test | `METHODOLOGICAL_ADAPTATION` only; no original LV transformer/aging experiment reproduced |
| Gómez & Morcos (2003), charging harmonics | Evidence gate for harmonics needed to characterize additional transformer losses | `BLOCKED_MISSING_HARMONIC_DATA` |
| Visakh & Selvan (2022), smart charging aging/cost | EPFL offline peak minimization replay; no real-time tariff or aging model | `PARTIAL_METHOD_ADAPTATION`, not full reproduction |
| Pavlićević & Mujović (2022), EVSE reactive-power effects | STREAM P/Q numeric exploratory assessment only; no qualified thermal/reactive dispatch | `BLOCKED_THERMAL_AND_REACTIVE_CAPABILITY`, preparatory electrical audit only |

## Priorities and blockers

1. **Highest value using current files:** validate the SINTEF sensor taxonomy and manufacturer/insulation condition, investigate actual heat-balance and excitation confounding, and reproduce the same-site load-order result under stronger model-form comparisons.
2. **EPFL:** reconcile minute-power integration and session-energy boundaries; verify station power-cap interpretation, users' required energy/service and charging-control capability. Only then interpret scheduling against operational constraints.
3. **STREAM and KU:** resolve measurement units, sign, pack sensor semantics, timestamp issues and physical interface metadata before moving to electrothermal identification or reactive compensation.
4. **Integrated evidence:** obtain synchronized actual transformer/EVSE topology, voltage/current, temperature, limits, charging control, and customer service records from a truly linked site. Until then all P-to-transport thermally mediated service links remain conditional, not validated.
5. **Standards and supervisor:** obtain authoritative applicable transformer hot-spot and insulation aging law, with temperature sensor definition and nameplate, before asserting rate of aging, remaining life or critical thermal threshold.

## One-paragraph defensible interpretation

The new computations show that a reduced temperature-state model predicts one-hour transformer top-oil behavior more accurately in RMSE than persistence, but not in MAE, and that the order of measured electrical current exposures affects model temperatures even when their squared-current integral is fixed. The analyses also distinguish seasonal calibration variability from actual inverse non-identifiability, quantify EPFL's observed session concurrency and replay the hypothetical peak-minimizing LP, and preserve source-sign/thermal/energy-consistency barriers in the KU Leuven and STREAM files. The work therefore strengthens **component-level mathematical evidence**, while real thermal feedback between power and electrified transportation and extreme-heat service consequences remain scientifically unverified.

## Source and authority references

- SINTEF original monitored transformer sensor file, checksum in `ORIGINAL_INPUT_MANIFEST.json`; data description: [Bærug transformer measurements](https://doi.org/10.5281/zenodo.17223516). User-owned original Drive record, not redistribution.
- EPFL original `Measurement_data.xlsx` and `Session_data.xlsx` user-owned Drive copies. See previously audited source register in GitHub. 
- KU Leuven C5PT0R measured EV charging efficiency original archive, authenticated Drive copy. 
- STREAM Slovenia 2025 active/reactive transformer-station monitoring CSV copies, authenticated Drive archive.
- [Qian, Zhou & Yuan (2015), DOI 10.1016/j.ijepes.2014.09.040](https://doi.org/10.1016/j.ijepes.2014.09.040) (abstract and user-supplied summary; full methodological reproduction not claimed).
- [Visakh & Selvan (2022), DOI 10.55730/1300-0632.3819](https://doi.org/10.55730/1300-0632.3819) (published charging scheduling/aging method; no exact reproduction).
- [Pavlićević & Mujović (2022), DOI 10.3390/en15197085](https://doi.org/10.3390/en15197085) (power flow and transformer aging methodology; no exact reproduction).
- Gómez & Morcos (2003), *Impact of EV battery chargers on the power quality of distribution systems*, IEEE Transactions on Power Delivery 18(3), 975–981. Original harmonic spectra required for transfer to Drive data.
- Nishanth (2026), *Physics-Informed Neural Networks for Transient Thermal Analysis and Insulation Life Assessment in Power Transformers*, DOI 10.1109/NE-IECCE69680.2026.11665934. Only available abstract-level method information; AI/PINN is excluded under this thesis's physics-first authority.
- GitHub current authority: [thesis title V3](https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/CANONICAL_THESIS_TITLE_V3.md); [objectives SO1–SO3](https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md); [evidence non-invention standard](https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md); [physics first scope](https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/PHYSICS_MATHEMATICS_FIRST_HYPOTHESIS_TESTING_SCOPE_DIRECTIVE_V1.md).
