# Physics-constrained ML and VVUQ protocol — T1 comparative research proposal

## Define problem and information set before training

Declare: site/asset IDs; topology status; measured prediction target; physical units and sensor meaning; future horizon, input availability at prediction issuance, calibration/validation/test split; exact operating domain; measured vs interpolated/synthetic flags; observation error model. *Future measured inputs* used for integration must be labeled conditional hindcasts. Avoid mixing train/test across the same session, vehicle, transformer or site unless the design explicitly evaluates within-group temporal generalization without leakage.

## Three separately audited comparators

- **M0, physics:** `dx/dt = f_physics(x,u,Ta;theta)`, `y=h(x,u;theta)+noise`, with derived/literature-admitted constitutive laws, initial and mathematical boundary conditions, solver tolerances and parameter provenance. The representation is a **proposed generic structure**, not a validated law for a particular component.
- **M1, data-based:** `yhat(k+h)=g_phi(H_k,I_k)` using only training information allowed at prediction time. Compare persistence/seasonality and linear regression before more flexible learners; separate feeder optimization targets from thermal targets.
- **M2, hybrid residual:** discretized `x_(k+1)=F_physics(x_k,u_k;theta)+r_phi(z_k)`. If residual directly alters conserved physical states, verify that discrete conservation/nonnegative dissipation and exact equipment constraints survive. Prefer learning a physics-admissible parameter/forcing where possible. Numerical residual prediction is not an identified physical heat flux.

**Comparability:** same actual asset/site, raw measurements, horizon, information set, competing benchmark, split manifest, measurement boundary and quality masks. If comparability is impossible, mark models `NOT_COMPARABLE` instead of ranking by RMSE.

## Minimum preregistered tests

1. **Provenance & origin:** raw hash, rights, real observation/aggregate/imputed/synthetic distinction, validation-domain conditions.
2. **Feeder feasibility:** numerical power balance residual, bus voltage, branch current/ampacity, transformer apparent loading, documented protection/rating, solver termination/optimality gap. A penalty loss is not proof of hard feasibility.
3. **Thermal conservation:** state-time derivative consistent with physically admitted heat input/loss/cooling, units, sensor location; check zero-load/steady ambient, heat forcing, limiting cases and events. A line's ampacity constraint is not a thermal ODE.
4. **Data leakage:** same site/session/vehicle splits; no fitted PCA/scaler/feature selector on test; no test-driven hyperparameters; embargo overlapping sliding windows; no future actual weather/current unless conditional hindcast.
5. **Model selection:** validation-only selection; holdout test untouched; report MAE/RMSE/bias and baselines on identical states/timesteps, sample/group count and calibration plots; parameter uncertainty and identifiability including boundary hitting.
6. **Out-of-domain extreme heat:** record actual ambient range and operating regimes; no extreme-heat *field validation* from cold-climate records; separate simulated stress testing from real observations.
7. **Mechanism/causality:** topology + timestamps alone insufficient. Each P→T_e and T_e→P claim requires physically justified perturbation/restriction sequence, observable mediator, confounder controls and matched counterfactual or explicitly qualified assumption. Causal identification may remain OPEN.
8. **Resilience:** service demand, horizon, actual electrical/mobility output, thermal capability and timing must each have source/qualified model; never infer mobility fulfillment from charging energy alone.

## Decision table

| Result | Allowed label |
|---|---|
| Notebook runs; numerical residual checks pass | `SOFTWARE_VERIFIED` or `SIMULATION_VERIFIED` for that implementation only |
| Held-out component observations and appropriate baseline tests pass within declared domain | `COMPONENT_CONDITIONAL_VALIDATED`, with conditions and limitations |
| Documented connected electrical site plus measured power, no temperatures | `MEASURED_CONNECTED_ELECTRICAL`, NOT thermal |
| Field thermal sensors on physically connected equipment, synchronized and independent directional validation passes | candidate `CONNECTED_THERMAL_FIELD_VALIDATED` only after full G0–G7 evidence review |
| No direct coupled data, only separate-installation calibration plus connected synthetic simulation | `HYPOTHETICAL_COUPLED_SIMULATION`, never field-validated |

## Output schema / mandatory checks

Populate `ml_experiment_register.csv` with one record **per trained/evaluated model**, fill qualified status honestly. Run `python .github/skills/power-ev-thermal-research/tools/check_ml_experiments.py --root <results-dir>`; optional nonempty expectation `--require-rows`. Its checks are **syntactic/structural** and cannot demonstrate physics accuracy, exact feasibility or missing field sensors. Empty register templates may pass syntax but never imply completed experiments.
