# Phase 1C — Information Processing Protocol v1

![Status](https://img.shields.io/badge/status-PREREGISTERED%20BEFORE%20ACN%20ACCESS-0969DA)
![Phase](https://img.shields.io/badge/phase-1C-1A7F37)

**Frozen:** 2026-09-12  
**Inputs:** processed ACN 5-minute trajectory + frozen chronological split  
**Boundary:** information-mechanism verification only; no validation-driven model selection and no H1/H2 execution.

---

## 0. Governing separation

```math
\boxed{
D_{cal}\rightarrow\text{fit information statistics}
\qquad\text{while}\qquad
D_{val}\rightarrow\text{verification/evaluation only}.
}
```

No validation-day observation may change the seasonal-slot estimator, latency levels, controller gain, site capacity, or residual-distribution construction.

---

# 1. Frozen charging-site capacity `[E/P]`

The frozen ACN Portal 0.3.3 Caltech infrastructure constructor at upstream commit

```text
14e723b11339e56ca3afd2bf4969f9e4bc8c2623
```

has default arguments

```text
voltage = 208 V
transformer_cap = 150 kW
```

for `caltech_acn()`.

Phase-1 v1 uses that unmodified default infrastructure, therefore

```math
\boxed{\bar P_{site}=150\ \mathrm{kW}.}
```

This resolves the previously pending software/infrastructure quantity in the parameter register. It is not fitted to Phase-1 outcomes.

---

# 2. Day-type/slot estimator `[P]`

For each usable calibration day `d`, each 5-minute slot

```math
s\in\{0,\ldots,287\},
```

and day type

```math
c(d)\in\{\text{weekday},\text{weekend}\},
```

define

```math
\widehat\mu_{c,s}
=
\frac{1}{|D_{cal,c}|}
\sum_{d\in D_{cal,c}}P_{ch}(d,s).
```

A weekday is Monday-Friday and a weekend is Saturday-Sunday in `America/Los_Angeles`.

For any evaluation day `d`, the seasonal-slot forecast is

```math
\widehat P_{slot}(d,s)=\widehat\mu_{c(d),s}.
```

If either day-type class has no calibration day, the processor fails closed. No cross-class fallback is introduced after seeing errors.

---

# 3. Calibration residual distribution `[P/D]`

To avoid evaluating a calibration observation against a mean that contains itself, residuals are formed by leave-one-day-out day-type/slot means.

For calibration day `d`,

```math
\widehat\mu_{c(d),s}^{(-d)}
=
\frac{1}{|D_{cal,c(d)}|-1}
\sum_{
\substack{d'\in D_{cal,c(d)}\\d'\neq d}
}
P_{ch}(d',s).
```

Then

```math
\epsilon_I(d,s)
=
P_{ch}(d,s)-\widehat\mu_{c(d),s}^{(-d)}.
```

The empirical calibration residual distribution is

```math
F_{\epsilon,cal}
=
\operatorname{Empirical}\{\epsilon_I(d,s):d\in D_{cal},s=0,\ldots,287\}.
```

Each day type must therefore contain at least two calibration days. Otherwise Phase-1 v1 fails closed rather than changing the estimator.

---

# 4. Reference power `[P]`

The controller reference is frozen as

```math
\boxed{
P_{ref}
=
\operatorname{median}_{d\in D_{cal},s}P_{ch}(d,s).
}
```

It is estimated from `D_cal` only.

---

# 5. Persistence baseline `[P]`

The persistence benchmark in `V-I04` is now defined before validation values are inspected.

For validation day `d`, let `d^-` be the most recent **usable day strictly before** `d`. The causal same-slot persistence forecast is

```math
\widehat P_{pers}(d,s)=P_{ch}(d^-,s).
```

For later validation days, `d^-` may itself be an earlier validation day because that observation would already have occurred in chronological operation. This does not fit or alter any model parameter.

If no prior usable day exists, that day is not eligible for the paired persistence comparison. The seasonal-slot model is still evaluated on it separately.

The paired validation comparison uses exactly the same slots for both models:

```math
RMSE_{slot}
=
\sqrt{\frac1N\sum(\widehat P_{slot}-P_{ch})^2},
```

```math
RMSE_{pers}
=
\sqrt{\frac1N\sum(\widehat P_{pers}-P_{ch})^2}.
```

The already-frozen `V-I04` criterion remains

```math
\boxed{RMSE_{slot}\le RMSE_{pers}.}
```

Failure is retained as verification evidence; the forecast structure is not upgraded after seeing holdout error inside v1.

---

# 6. Latency operator `[P]`

Frozen latency levels remain

```math
\delta_I\in\{0,5,15,30\}\text{ min},
```

or

```math
m_I=\delta_I/5\in\{0,1,3,6\}\text{ slots}.
```

For a continuous chronological forecast series `f_k`,

```math
\widetilde f_k=f_{k-m_I}.
```

No wrap-around is permitted.

For the first `m_I` slots of a processed sequence with unavailable prehistory, the delayed forecast is explicitly `NA`; those slots are excluded from latency-comparison metrics. They may not be filled with future data, zeros, or copied present values.

For coupled control experiments, a scenario is admissible only if its evaluation interval begins after sufficient prehistory exists. The preregistered noon disturbance therefore has more than the maximum 30-minute prehistory on every usable day.

This boundary convention closes the previously unspecified latency edge case without using observed outcomes.

---

# 7. Error-injection rule `[P]`

When stochastic information degradation is required, residuals are sampled only from `F_{epsilon,cal}` under the frozen random-seed rule.

```math
\widetilde P_{ch}(t)
=
\widehat P_{slot}(t-\delta_I)
+
\epsilon_I^*(t),
\qquad
\epsilon_I^*\sim F_{\epsilon,cal}.
```

Residual draws do not come from `D_val`.

Deterministic verification tests may set

```math
\epsilon_I^*(t)=0
```

to isolate latency/operator behavior. This is a verification case, not a claim that forecast error is zero.

---

# 8. Controller `[P]`

The already-frozen controller remains

```math
u_{ch}^{max}(t)
=
\operatorname{clip}\left[
P_{margin}(t)
-k_I\big(\widetilde P_{ch}(t+\Delta t)-P_{ref}\big)_+,
0,
\bar P_{site}
\right],
```

with

```math
k_I=1,
\qquad
\bar P_{site}=150\ \mathrm{kW}.
```

No gain optimization is permitted.

---

# 9. Required information artifacts

After `G_ACNproc=1`, the information processor must emit and hash:

```text
seasonal_slot_means.csv
calibration_loo_residuals.csv
information_parameters.json
validation_forecasts.csv
information_verification.json
```

At minimum `information_parameters.json` records:

```text
P_ref;
P_site_cap;
calibration-day hashes;
slot-mean hash;
residual hash;
latency levels;
random-seed rule.
```

No H1/H2 output belongs in these artifacts.

---

# 10. Gate interpretation

The information subgate can close only if:

```text
D_cal/D_val separation is respected;
weekday/weekend slot models are estimable;
leave-one-day-out residuals are finite;
latency indexing passes unit tests;
validation RMSE is calculated without retraining;
V-I04 is reported PASS or FAIL without changing the model.
```

```math
\boxed{
G_I=1
\not\Rightarrow
G_V=1
\not\Rightarrow
G_{VAL}=1
\not\Rightarrow
H_1/H_2.
}
```
