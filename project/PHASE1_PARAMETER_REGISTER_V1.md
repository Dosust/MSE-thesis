# Phase 1A — Parameter Register v1

![Status](https://img.shields.io/badge/status-PARAMETER%20LOCK%20v1.0-0969DA)
![Phase](https://img.shields.io/badge/phase-1A-1A7F37)

**Frozen:** 2026-09-12  
**Authority:** `PHASE1_EXPERIMENT_SPECIFICATION_V1.md` + `PHASE1_DATA_MANIFEST_V1.md`  
**Purpose:** freeze every parameter class, experimental factor, numerical control, provenance category, uncertainty range, and identifiability status before Phase-1 confirmatory execution.  
**Scope:** Power–Transportation dependency validation only; Stage-5 viability parameters are not active in Phase 1.

---

# 0. Governing distinction

The register enforces

```math
\boxed{
\theta^{fixed}
\neq
\theta^{observed}
\neq
\theta^{estimated}
\neq
\theta^{assumed}
\neq
\theta^{derived}
\neq
\theta^{test\ control}.
}
```

These categories must not be silently mixed during calibration or interpretation.

Claim tags:

```text
[E] external benchmark/data value;
[P] preregistered thesis choice;
[D] derived quantity;
[A] explicit assumption;
[U] unresolved/pending data-derived value.
```

The canonical dependency object remains

```math
\mathfrak d_e=(\mathcal C_e,\Sigma_e,\Pi_e),
```

with mechanism parameters carried by

```math
\Sigma_e=(\Phi_e,\gamma_e,\theta_e,\zeta_e)
```

and evidence/uncertainty by

```math
\Pi_e=(\mathcal P_e,V_e,\mathcal U_e).
```

---

# 1. Parameter-record schema

Every parameter or control quantity is represented by

```math
\mathcal R_{\theta_j}
=
(
ID,
\theta_j,
meaning,
unit,
domain,
source,
status,
value/range,
uncertainty,
estimation,
identifiability,
validation\ data
).
```

No quantity may enter confirmatory code without an entry here or in an explicitly versioned amendment.

---

# 2. Status vocabulary

| Status | Meaning | May be tuned? |
|---|---|---:|
| `BENCHMARK_FIXED [E]` | external benchmark value frozen by source | no |
| `OBSERVED [E]` | measured/recorded input from frozen dataset | no |
| `ESTIMATED_FROM_DCAL [D/P]` | computed only from calibration data by frozen rule | only by declared estimator |
| `EXPERIMENT_FACTOR [P]` | deliberately imposed treatment level | no hidden tuning |
| `ASSUMED_UNCERTAIN [A/P]` | not measured in v1; fixed central value + declared uncertainty range | no calibration to holdout |
| `DERIVED [D]` | computed from states/other registered quantities | no independent tuning |
| `NUMERICAL_CONTROL [P]` | solver/V&V/UQ setting | no after results |
| `PENDING_DATA_DERIVATION [U]` | frozen definition, value unavailable until data acquisition | blocked until resolved |

---

# 3. Power-system benchmark parameters

All electrical benchmark quantities below are `BENCHMARK_FIXED [E]` and may not be calibrated against Phase-1 coupled outcomes.

## 3.1 System-level power parameters

| ID | Symbol | Meaning | Unit | Frozen value/source | Identifiability |
|---|---|---|---|---|---|
| P-001 | `S_base` | MATPOWER system base | MVA | `10` | not estimated |
| P-002 | `V_base` | nominal distribution voltage | kV | `12.66` | not estimated |
| P-003 | `b*` | charging-interface bus | index | `24` `[P]` | design choice, not estimated |
| P-004 | `e_P*` | controlled feeder branch | ordered pair | `(23,24)` `[P]` | design choice, not estimated |
| P-005 | `P_d,24^base` | active base load at bus 24 | MW | `0.420` from source conversion | not estimated |
| P-006 | `Q_d,24^base` | reactive base load at bus 24 | MVAr | `0.200` from source conversion | not estimated |
| P-007 | `V_min,24` | benchmark minimum voltage limit | p.u. | `0.9` | not estimated |
| P-008 | `V_max,24` | benchmark maximum voltage limit | p.u. | `1.1` | not estimated |

## 3.2 Branch-parameter object

Rather than duplicating every branch row as an independent thesis parameter, define the immutable benchmark vector

```math
\vartheta_P^{bench}
=
\{r_{ij},x_{ij},status_{ij},P_{d,j},Q_{d,j}\}_{case33bw}.
```

For the controlled branch:

| ID | Symbol | Meaning | Source unit/value | Simulation treatment |
|---|---|---|---|---|
| P-009 | `r_23,24` | branch resistance | `0.8980 ohm` in source | source converts to p.u. |
| P-010 | `x_23,24` | branch reactance | `0.7091 ohm` in source | source converts to p.u. |
| P-011 | `status_23,24(t)` | branch energization state | dimensionless | scenario/event controlled |

The source file’s own conversion from ohms to per-unit is authoritative. No second undocumented conversion is permitted.

---

# 4. Transportation benchmark parameters

## 4.1 Immutable network parameter objects `[E]`

Define

```math
\vartheta_T^{bench}
=
\{c_a,t_a^0,B_a,\beta_a\}_{a\in\mathcal A_T}.
```

with link-specific `c_a,t_a^0` from the frozen TNTP file and

```math
B_a=0.15,
\qquad
\beta_a=4.
```

for the Sioux Falls links.

| ID | Symbol | Meaning | Unit | Status |
|---|---|---|---|---|
| T-001 | `c_a` | link capacity vector | TNTP benchmark units | `BENCHMARK_FIXED` |
| T-002 | `t_a^0` | free-flow time vector | TNTP benchmark time units | `BENCHMARK_FIXED` |
| T-003 | `B_a` | BPR coefficient | dimensionless | `0.15`, `BENCHMARK_FIXED` |
| T-004 | `beta_a` | BPR exponent | dimensionless | `4`, `BENCHMARK_FIXED` |
| T-005 | `q_od` | OD-demand matrix | TNTP demand units | `BENCHMARK_FIXED` |

## 4.2 Experimental transport controls `[P]`

| ID | Symbol | Meaning | Unit | Frozen value | Status |
|---|---|---|---|---|---|
| T-006 | `n_D` | crew-depot node | index | `1` | `EXPERIMENT_FACTOR` |
| T-007 | `n_F` | repair/charging access node | index | `10` | `EXPERIMENT_FACTOR` |
| T-008 | `e_T^cut` | controlled road closure | directed arcs | `(9,10),(10,9)` | `EXPERIMENT_FACTOR` |

These are experimental placements, not empirical claims about Sioux Falls infrastructure.

---

# 5. EV charging data quantities

Observed session values are inputs, not free parameters.

| ID | Symbol | Meaning | Unit | Status | Source |
|---|---|---|---|---|---|
| EV-001 | `t_conn,n` | session connection time | timestamp | `OBSERVED` | ACN-Data |
| EV-002 | `t_disc,n` | session disconnect time | timestamp | `OBSERVED` | ACN-Data |
| EV-003 | `E_n^delivered` | delivered session energy | kWh | `OBSERVED` | ACN-Data |
| EV-004 | `I_n(t)` / replay trace | charging-current/replay information | source-defined | `OBSERVED` | ACN-Data/ACN-Sim |
| EV-005 | `Delta t` | coupled charging/power interval | min | `5` | `EXPERIMENT_FACTOR [P]` |
| EV-006 | `P_ch(t)` | aggregate charging power | kW or MW | `DERIVED` | ACN-Sim replay |
| EV-007 | `Pbar_ch,cal` | calibration-period mean charging power | same as `P_ch` | `PENDING_DATA_DERIVATION` | `D_cal` only |

No synthetic arrival-rate or synthetic energy-demand distribution replaces observed ACN sessions in v1.

---

# 6. Information-dependency parameters

The information mechanism is intentionally low-dimensional.

## 6.1 Estimated calibration objects `[D/P]`

| ID | Symbol | Meaning | Unit | Estimation rule | Status |
|---|---|---|---|---|---|
| I-001 | `mu_daytype,s` | weekday/weekend × 5-min slot mean power | power | sample mean using `D_cal` only | `PENDING_DATA_DERIVATION` |
| I-002 | `F_epsilon,cal` | empirical forecast-residual distribution | power | empirical distribution of `P_ch-hatP_ch` on `D_cal` | `PENDING_DATA_DERIVATION` |
| I-003 | `P_ref` | reference charging power | power | median `P_ch` over `D_cal` | `PENDING_DATA_DERIVATION` |

These are estimated by direct summary statistics, not optimized against holdout outcomes.

## 6.2 Information treatment levels `[P]`

| ID | Symbol | Meaning | Unit | Frozen levels | Status |
|---|---|---|---|---|---|
| I-004 | `delta_I` | information latency | min | `{0,5,15,30}` | `EXPERIMENT_FACTOR` |
| I-005 | `k_I` | fixed test-controller gain | dimensionless | `1` | `EXPERIMENT_FACTOR` |

Information degradation is

```math
\widetilde P_{ch}(t)
=
\widehat P_{ch}(t-\delta_I)+\varepsilon_I^*(t),
```

where `epsilon_I*` is sampled only from the frozen calibration residual distribution.

## 6.3 Derived controller quantity `[D]`

```math
P_{margin}(t)
```

is derived from the power state and is **not** independently calibrated.

The test controller remains

```math
u_{ch}^{max}(t)
=
\operatorname{clip}\!\left[
P_{margin}(t)-k_I(\widetilde P_{ch}(t+\Delta t)-P_{ref})_+,
0,
\bar P_{site}
\right].
```

`bar P_site` must come from the locked charging-infrastructure executable configuration; it may not be selected post hoc to improve results. Its exact value is `PENDING_SOFTWARE/DATA_LOCK` until the ACN-Sim infrastructure object is frozen.

---

# 7. Organizational/restoration parameters

These are **not field-calibrated values** in Phase 1 v1.

| ID | Symbol | Meaning | Unit | Central value | Epistemic range | Status |
|---|---|---|---|---:|---:|---|
| O-001 | `tau_decision` | authorization/decision delay | min | `15` | `[0,30]` | `ASSUMED_UNCERTAIN [A/P]` |
| O-002 | `tau_mobilization` | crew mobilization delay | min | `15` | `[0,30]` | `ASSUMED_UNCERTAIN [A/P]` |
| O-003 | `tau_repair` | branch repair duration | min | `60` | `[30,120]` | `ASSUMED_UNCERTAIN [A/P]` |
| O-004 | `t_0` | controlled feeder-fault time | local experiment time | `12:00` | none | `EXPERIMENT_FACTOR [P]` |

Crew travel time is derived:

```math
T_{crew}(t)
=
\min_{r\in\mathcal R_T(t)}\sum_{a\in r}t_a(x_a(t)).
```

Restoration time is derived:

```math
T_{restoration}
=
\tau_{decision}
+\tau_{mobilization}
+T_{crew}
+\tau_{repair}.
```

Therefore `T_crew` and `T_restoration` are outputs/derived states, not free parameters.

---

# 8. Synthetic cross-domain mapping parameters `[A/P]`

The following are fixed experimental mappings and carry epistemic—not calibration—uncertainty:

| ID | Mapping | Frozen value | Status |
|---|---|---|---|
| X-001 | charging demand -> power interface | ACN aggregate -> bus 24 | fixed synthetic mapping |
| X-002 | feeder availability -> charging service | branch 23-24 -> charging availability | fixed synthetic mapping |
| X-003 | road access -> restoration location | node 10 -> branch 23-24 repair access | fixed synthetic mapping |

These mappings are not assigned a numeric probability distribution in v1. Their limitation is carried qualitatively in `Pi_e` and in the bounded validation claim.

---

# 9. Parameter-estimation set

A major Phase-1 design objective is to prevent excessive model flexibility.

The only quantities estimated from calibration data are

```math
\boxed{
\Theta_{est}
=
\{\mu_{daytype,s},F_{\varepsilon,cal},P_{ref}\}.
}
```

These use direct frozen estimators, not free optimization.

The benchmark physical parameters satisfy

```math
\boxed{
\Theta_{P,T}^{free}=\varnothing.
}
```

for confirmatory calibration.

The organizational times are uncertain assumptions but are **not** tuned to `D_val`:

```math
\Theta_O^{cal}=\varnothing.
```

This is deliberate: if many continuous parameters were freely optimized, the thesis could fit service trajectories without identifying which dependency mechanism caused the fit.

---

# 10. Identifiability classification

## 10.1 Benchmark-fixed quantities

`P-001` through benchmark vectors and `T-001` through `T-005` are not identification targets. Their uncertainty is benchmark-transfer uncertainty, not within-v1 calibration uncertainty.

## 10.2 Information statistics

`I-001` through `I-003` are estimable directly from `D_cal`. Their practical adequacy is assessed by out-of-time holdout forecast error against persistence.

If additional free continuous mechanism parameters are introduced later, normalized sensitivity analysis is mandatory:

```math
\widetilde S_{ij}
=
\frac{\theta_j}{s_i}
\frac{\partial y_i}{\partial\theta_j}.
```

Severe numerical non-identifiability is flagged when

```math
\frac{\sigma_{min}}{\sigma_{max}}<10^{-8}.
```

This is a thesis diagnostic threshold `[P]`, not a universal theorem.

## 10.3 Organizational quantities

`O-001` through `O-003` are **not identifiable from the Phase-1 v1 empirical data** because no co-located field restoration dataset is being used.

Therefore:

```math
\boxed{
O\text{-times cannot be reported as calibrated or empirically validated parameters in v1.}
}
```

Their effect is tested through epistemic sensitivity/scenario analysis only.

---

# 11. Dependency-level epistemic register `Pi_e`

## 11.1 `D_P^{TP}` — charging demand -> feeder loading

```text
Mechanism evidence: physically established load aggregation + observed charging forcing.
Specific mapping evidence: synthetic benchmark mapping.
Validation status before execution: PENDING.
Primary uncertainty: ACN-to-benchmark transfer and synthetic bus placement.
Maximum v1 claim: benchmark/semi-empirical mechanism support, not city-specific validation.
```

## 11.2 `D_P^{PT}` — feeder availability -> charging availability

```text
Mechanism evidence: electrical service availability is required for charging operation.
Specific mapping evidence: synthetic branch/site mapping.
Validation status before execution: PENDING.
Primary uncertainty: synthetic interface placement and outage abstraction.
```

## 11.3 `D_I` — forecast/latency -> controller

```text
General evidence: timing/data matter in cyber-physical operation.
Exact operator/controller: thesis-specific.
Forecast statistics: estimated from D_cal.
Validation status before execution: PENDING.
Primary uncertainty: transfer from simple forecast/latency experiment to operational control systems.
```

## 11.4 `D_O` — road access/organization -> restoration

```text
General mechanism evidence: access/crew routing can affect restoration timing.
Exact organizational durations: assumed, not measured.
Validation status before execution: PENDING / RESTRICTED BY DESIGN.
Primary uncertainty: decision, mobilization, repair duration and synthetic access mapping.
```

---

# 12. Numerical verification controls

These are **not physical parameters**. They are frozen test controls.

| ID | Quantity | Frozen value | Role |
|---|---|---:|---|
| V-001 | `epsilon_P,max` | `1e-8` | power-equation residual tolerance |
| V-002 | `N_it,P` | `100` | maximum power iterations |
| V-003 | `RG_T,max` | `1e-6` | Frank–Wolfe relative-gap tolerance |
| V-004 | `N_it,T` | `5000` | maximum transport iterations |
| V-005 | `epsilon_Delta t,max` | `1e-3` | 5-min vs 2.5-min output refinement tolerance |
| V-006 | `median(epsilon_E),max` | `0.01` | charging-energy replay acceptance |
| V-007 | deterministic reproducibility tolerance | `1e-12` relative | repeat-run equality |
| V-008 | severe SVD ratio flag | `1e-8` | numerical identifiability warning |

Failure of a numerical tolerance is reported; failed cases may not be deleted because they are inconvenient.

---

# 13. UQ/sensitivity controls

These are preregistered computational controls, not universal methodological constants.

| ID | Quantity | Frozen value |
|---|---|---:|
| UQ-001 | Morris levels `p` | `4` |
| UQ-002 | Morris trajectories `r` | `20` |
| UQ-003 | active-dimension criterion | `d_active <= 10` for Sobol stage |
| UQ-004 | Sobol base sample 1 | `N=1024` |
| UQ-005 | Sobol convergence audit | `N=2048` |
| UQ-006 | stochastic seed | **PENDING software/run lock; must be recorded before first stochastic run** |

The seed may be chosen during the environment/run-manifest step, but once recorded it cannot be changed because another seed yields more favorable results.

---

# 14. Primary derived outputs

The following are outputs, not tunable parameters:

```math
Z_{P1}
=
\begin{bmatrix}
V_{min}\\
T_{Vviol}\\
E_{unserved}^{EV}\\
Q_{mobility}^{charge}\\
T_{crew}\\
T_{restoration}
\end{bmatrix}.
```

Secondary derived outputs include

```math
RMSE_I,\quad MAE_I,\quad P_{peak},\quad E_{loss}.
```

No Stage-5 viability quantity may be used to retune Phase-1 parameters.

---

# 15. Parameter-to-data provenance map

| Parameter/object | Provenance |
|---|---|
| `vartheta_P^bench` | D-PWR-01 immutable MATPOWER case |
| `vartheta_T^bench` | D-TRN-01 immutable TNTP network |
| `q_od` | D-TRN-02 immutable TNTP OD matrix |
| `P_ch(t)` | D-EV-01 -> D-EV-PROC-01 |
| `mu_daytype,s` | D-EV-SPLIT-01 calibration days only |
| `F_epsilon,cal` | calibration residuals only |
| `P_ref` | calibration aggregate power only |
| `delta_I` | preregistered experiment factor |
| `tau_decision,mobilization,repair` | preregistered assumptions/ranges |
| `T_crew` | derived from T network state and route solution |
| `T_restoration` | derived from organization + crew access |

---

# 16. Calibration firewall

After `D_val` is opened, the following are prohibited:

```text
- changing k_I;
- changing delta_I levels;
- changing organizational central values/ranges;
- changing bus/node/link mappings;
- changing the forecast family;
- calibrating feeder or road benchmark parameters;
- changing numerical tolerances;
- redefining primary outputs;
- dropping scenarios on the basis of poor performance.
```

Any such change creates a new experiment version and requires a new independent holdout strategy.

---

# 17. Parameter-lock gate

Define

```math
G_\theta
=
G_{class}
\land G_{units}
\land G_{source}
\land G_{uncertainty}
\land G_{identifiability}
\land G_{firewall}.
```

Current state:

```text
G_class           = PASS
G_units           = PARTIAL — ACN replay power/site limit pending software/data lock
G_source          = PARTIAL — ACN raw acquisition pending
G_uncertainty     = PASS for declared v1 assumptions/ranges
G_identifiability = PASS conceptually; data-derived values pending
G_firewall        = PASS

PHASE-1 PARAMETER RELEASE = NOT YET AUTHORIZED.
```

Parameter release becomes eligible only after the ACN raw/processed data hashes, software environment, ACN-Sim infrastructure configuration, and derived calibration objects are frozen.

---

# 18. Scientific boundary

This register intentionally does **not** create false precision.

```math
\boxed{
\text{unknown value}
\neq
\text{permission to invent a value}.
}
```

If an exact parameter cannot yet be supported, it remains `PENDING` or `ASSUMED_UNCERTAIN` and its epistemic status is carried in `Pi_e`.

The goal is not to maximize the number of calibrated parameters. The goal is to ensure that every parameter entering a causal claim is traceable, dimensionally meaningful, identifiable or explicitly uncertain, and incapable of being silently tuned after results are seen.