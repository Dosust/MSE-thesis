# Physics-Informed Neural Network (PINN) as a comparative benchmark candidate — v1

**Date:** 2026-11-05  
**Thesis:** Engineering of Power–Electrified Transportation Interdependencies for Resilience  
**Status:** USER-SELECTED STRONG CANDIDATE FOR COMPARISON, CONDITIONAL ON EXPERIMENTAL ADEQUACY; **NOT** AN ADOPTED MODEL, NOT A RESULT, NOT A SUPERVISOR-APPROVED CHANGE.  
**Authority:** Active SO1–SO3, approved researcher methodological direction for JBI-informed systematic scoping review; physics and experimental verification remain first principles.

## Decision
A **Physics-Informed Neural Network (PINN)** is retained as an **optional comparative model family / benchmarking candidate** to test against the thesis's future **physics-based state–time model** and conventional baselines. Published PINN transformer HST papers are **prior art and reproduction candidates**, not independently validated baseline results until original methods, data, code, numerical boundary conditions, independent tests and compute costs are checked. Do not assume PINNs are superior or commit the thesis to PINN development before qualification.

## Candidate comparison
| Arm | Role | Admission conditions |
|---|---|---|
| Persistence/simple statistical reference | Trivial forecasting benchmark | Leakage-safe time split, same available input horizon |
| Standard guide / physically justified reduced thermal ODE/DAE | **Required physics-first benchmark** | Appropriate IEC/IEEE edition and transformer type, units, sensor/parameter verification |
| Finite-volume / numerical PDE | Mechanistic spatial comparator *if justified* | Boundary data, mesh/time convergence, compute feasibility and fair equations |
| Conventional calibrated gray-box | Parsimonious data-informed baseline | Same measured data budget and independently evaluated parameters |
| **PINN / physics-informed learning** | **Conditional candidate** for accuracy, physical consistency and data-efficiency comparison | Verified physics residual/boundaries, temperature observation operator, sufficient data, blinded holdout, fair compute/training comparison |
| Proposed coupled physical P↔T state–time model | **Prospective thesis contribution, not yet assumed superior** | Verified interface structure and identifiable parameters or explicitly bounded mechanistic scenario simulation |

## Benchmark requirements and metrics
- **Input consistency:** identical measured forcing, chronological training/calibration/test periods and genuinely available real-time input; separate one-step state estimation, conditional hindcasts and operational forecasts.
- **Target:** separately qualify SINTEF high-voltage and low-voltage **sensor-labeled** HST channels; sensor coordinates/meaning versus actual winding maximum must be checked. Existing 0.2147°C one-hour RMSE is **top-oil** only, not HST.
- **Metrics:** HST RMSE/MAE/bias [°C], error at high temperatures and peaks, threshold-crossing timing [min] where independently verifiable, energy/heat balance residuals, physical constraint violations, predictive uncertainty/coverage, parameter plausibility, training cost and inference latency, data efficiency, variability across seeds, and generalization under documented shift.
- **Fairness:** tune all models on training/validation partitions, report parameter counts and hardware/runtime, repeat stochastic training, guard against temporal leakage and privileged future forcing; only score claims on admissible independent test conditions.
- **Scientific interpretation:** measured transformer-only HST comparison is a **component model result**, not proof of power-to-EVSE heat-induced restriction, bidirectional SoS causality, EV charging delivery, or electric-mobility service resilience. A coupled result requires same-site topology/control/service observations or explicitly labeled modeled scenarios.

## Literature prior art
- **Physics-Informed Neural Networks for Transient Thermal Analysis and Insulation Life Assessment in Power Transformers (2026)**, DOI https://doi.org/10.1109/NE-IECCE69680.2026.11665934: title/abstract-level candidate for exact full-text reproducibility audit; its claimed transient PDE and aging factor remain subject to original equation/method/validation checks.
- **Bragone et al. (2022)**, DOI https://doi.org/10.1016/j.epsr.2022.108447: prior transformer heat-PDE PINN/FVM comparison; earlier project extraction notes that PINN did not outperform FVM under tested conditions, showing the comparison is nontrivial and not novel simply because a PINN is used.
- **Cao et al. (2026)**, DOI https://doi.org/10.1016/j.applthermaleng.2026.130776: EV thermal-management model; **not the power transformer's physical hot-spot model**.

## Stage gates
1. Verify key baseline equations/asset standards and measured HST observability.
2. Derive and test conventional engineering physics model, documenting units, solver convergence and holdouts.
3. Audit original PINN papers (loss/residual, geometry, BC/IC, data volume, actual test set and code) and reproduce if feasible.
4. Only if data support meaningful comparison, benchmark PINN with identical partitions, forcing, and computational budget against physics and gray-box methods.
5. Separately evaluate **interdependency metrics**: thermal-limit times, dynamic power capability, offered-versus-delivered charging, and service loss/recovery, measured if data permit or explicitly scenario-modelled.
6. Determine whether PINN, conventional physics or a hybrid method is merited by predeclared results. **No predetermined winner or final primary metric.**

**Decision record:** HST remains a strong physical validation-metric candidate; PINN remains a strong **methodological benchmark candidate**; the final interdependency metric set and proposed coupled model are **to be determined after evidence review, calibration and rigorous comparative tests**. No changes to canonical SO1–SO3.
