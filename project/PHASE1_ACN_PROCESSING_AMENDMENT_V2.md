# Phase 1C — ACN Processing Amendment v2

![Status](https://img.shields.io/badge/status-PROSPECTIVE%20CORRECTIVE%20PROTOCOL-0969DA)
![v1](https://img.shields.io/badge/V--D06%20v1-PRESERVED%20FAIL-D1242F)

**Frozen:** 2026-09-13  
**Trigger:** preserved `V-D06` failure in workflow run `34737402122`.  
**Authority:** `PHASE1_VD06_ROOT_CAUSE_AUDIT_V1.md`.  
**Boundary:** corrective ACN processing and independent re-verification only. No H1/H2, no Stage-5 viability, no retroactive rewriting of v1.

---

## 0. Non-negotiable history

The v1 result remains:

```math
\boxed{V\!-\!D06_{v1}=\mathrm{FAIL}}
```

with

```text
median validation epsilon_E = 0.06562885747436485
frozen criterion            = <= 0.01
```

v2 is a new model/data-processing specification. A future v2 PASS cannot be reported as if v1 had passed.

The amendment changes only mechanisms falsified or rendered ambiguous by the v1 forensic audit. The primary threshold is not weakened.

---

# 1. Corrective design logic

```math
\boxed{
\text{v1 failure}
\rightarrow
\text{root-cause audit}
\rightarrow
\text{prospective correction}
\rightarrow
\text{fresh untouched holdout}
\rightarrow
\text{single evaluation}
}
```

The existing 2019-10-10 through 2019-12-31 object is now **development evidence only** for v2. Its old v1 validation days have been observed and therefore cannot provide independent confirmation of the v2 amendment.

---

# 2. v2 development object

Development source remains the immutable v1 raw object:

```text
site       = caltech
window     = 2019-10-10 00:00:00 through 2019-12-31 23:59:59 America/Los_Angeles
raw SHA256 = ac6d9b237d4e6752dd990f42b569f0de90af125455a8ffdff20b53a7f30e35fd
records    = 2082
```

v2 may use this object to estimate processing/calibration parameters because no v2 claim will be validated on it.

---

# 3. Amendment A — exact duplicate timestamps

## 3.1 Distinguish equality from reversal

For each current or pilot trace in the original supplied order:

```math
\Delta t_j=t_{j+1}-t_j.
```

v2 distinguishes:

```text
Delta t < 0  -> genuine backward time -> REJECT
Delta t = 0  -> repeated observation at one timestamp -> COLLAPSE
Delta t > 0  -> preserve
```

No sorting is permitted. Sorting could conceal true chronology defects.

## 3.2 Deterministic collapse operator

If `m` values share an identical timestamp `t*`, v2 maps them to one value using the arithmetic mean:

```math
I^*(t^*)
=
\frac{1}{m}\sum_{j:t_j=t^*} I_j.
```

The same operator is applied to `pilotSignal`.

This is the unique minimizer of

```math
\min_c\sum_{j:t_j=t^*}(I_j-c)^2,
```

so the rule has a defined mathematical meaning rather than an outcome-driven choice.

After duplicate collapse, the original gap rule remains unchanged:

```math
\boxed{\Delta t_{gap}\le5\text{ min}.}
```

A larger gap still causes rejection.

No interpolation, smoothing or imputation is introduced merely to rescue a session.

---

# 4. Amendment B — active charging endpoint

ACN-Data documents `doneChargingTime` as the time of the last non-zero current draw recorded.

For v2, active EV charging energy is reconstructed only on

```math
[c_n,\,e_n],
\qquad
 e_n=\min(doneChargingTime_n,disconnectTime_n).
```

The session is rejected if:

```text
connectionTime is invalid;
disconnectTime is invalid;
doneChargingTime is missing/invalid;
doneChargingTime < connectionTime;
connectionTime >= disconnectTime.
```

The current trace is never integrated through the full parking dwell after `doneChargingTime` for the active-charging quantity `P_ch`.

This prevents the v1 long-dwell failure mode in which a low non-zero current/sensor floor accumulates artificial energy after charging is complete.

---

# 5. Amendment C — global effective current-to-energy scale

The v1 audit shows that ACN-Sim's nominal `208 V` parameter is not supported as a universal 1%-accuracy metrology conversion between ACN-Data measured current and `kWhDelivered`.

v2 therefore estimates **one global scalar only** from the v2 development object.

For every development session that passes v2 structural QC and has positive `kWhDelivered`, define

```math
A_n
=
\int_{c_n}^{e_n}I_n(t)dt
\quad[\mathrm{A\,s}].
```

The session-implied effective voltage is

```math
V_{eff,n}
=
\frac{1000\times3600\;E_{data,n}}{A_n}.
```

The frozen robust development estimator is

```math
\boxed{
\widehat V_{eff}
=
\operatorname{median}_{n\in D_{dev}}V_{eff,n}.
}
```

Only one global scalar is estimated. No station-specific voltage fitting, day-specific correction, validation-driven scaling, or per-session normalization is allowed.

The corrected active charging power is

```math
P_n^{v2}(t)
=
\frac{\widehat V_{eff} I_n(t)}{1000}.
```

and

```math
P_{ch}^{v2}(t)=\sum_nP_n^{v2}(t).
```

The development estimate `V_eff_hat`, the exact eligible-session count, code SHA and output hash must be frozen **before the independent v2 holdout is acquired**.

---

# 6. v2 development calibration gate

Before any new holdout acquisition, execute and freeze:

```text
v2 duplicate-collapse QC;
v2 active-charging truncation;
development usable-day ledger;
V_eff_hat;
v2 development P_ch(t);
weekday/weekend slot means;
leave-one-day-out residual distribution;
P_ref;
all SHA-256 identities.
```

The development stage produces no PASS/FAIL claim for `V-D06_v2`.

Required gate:

```math
\boxed{G_{DEV,v2}=1}
```

before opening the new holdout.

---

# 7. Fresh independent holdout — frozen before acquisition

The new ACN holdout is frozen as:

```text
source/API          = ACN-Data / Caltech
site                = caltech
start local         = 2020-01-01 00:00:00 America/Los_Angeles
end local           = 2020-02-29 23:59:59 America/Los_Angeles
timeseries          = true
client              = acnportal==0.3.3
role                = independent v2 verification holdout
```

This window has not been acquired or inspected in the thesis workflow at the time this protocol is frozen.

The first local date `2020-01-01` is excluded from complete-day site-load analysis as the same left-censored query boundary rule used in v1.

There is no daylight-saving transition inside January-February 2020 in `America/Los_Angeles`; nevertheless the generic exact-24-hour check remains active.

No session or day may be removed because its v2 energy error is unfavorable.

---

# 8. Independent v2 energy criterion — unchanged

On the fresh holdout, for each usable connection-date cohort `d`:

```math
E_{sim,v2}(d)
=
\sum_{n:\,date(c_n)=d}
\frac{\widehat V_{eff}}{1000\times3600}
\int_{c_n}^{e_n}I_n(t)dt,
```

```math
E_{data}(d)
=
\sum_{n:\,date(c_n)=d}kWhDelivered_n,
```

```math
\epsilon_{E,v2}(d)
=
\frac{|E_{sim,v2}(d)-E_{data}(d)|}
{\max(E_{data}(d),10^{-12})}.
```

The primary acceptance threshold is retained exactly:

```math
\boxed{
\operatorname{median}_{d\in D_{holdout}}
\epsilon_{E,v2}(d)\le0.01.
}
```

Report median, p95 and maximum. Only the median threshold is the preregistered primary gate unless a separate amendment is frozen before acquisition.

---

# 9. Information model under v2

Because v2 changes the charging trajectory, all information quantities are recomputed from the v2 **development object only**:

```text
weekday/weekend 5-min slot means;
leave-one-day-out residual distribution;
P_ref = median development P_ch;
latency levels = {0,5,15,30} min unchanged;
P_site_cap = 150 kW unchanged;
controller gain k_I = 1 unchanged.
```

The fresh holdout receives no retraining.

The v2 information verification criterion remains:

```math
\boxed{RMSE_{slot}\le RMSE_{persistence}.}
```

The old v1 `V-I04=PASS` remains preserved but does not substitute for evaluation of the changed v2 trajectory.

---

# 10. Reproducibility requirements

The v2 chain is

```math
D_{dev,raw}
\rightarrow
T_{v2}
\rightarrow
\widehat V_{eff},\Theta_{I,v2}
\rightarrow
\text{freeze hashes}
\rightarrow
D_{holdout,raw}
\rightarrow
T_{v2}
\rightarrow
V\!-\!D06_{v2},V\!-\!I04_{v2}.
```

Freeze at minimum:

```text
development raw SHA;
development processor code SHA;
development manifest SHA;
V_eff_hat value + file hash;
development day-list hashes;
information-parameter hashes;
holdout raw SHA;
holdout acquisition manifest SHA;
holdout processed manifest SHA;
verification report SHA;
workflow run/job IDs;
artifact ID + artifact digest;
credential-hygiene PASS.
```

---

# 11. Decision rule

```math
G_{ACN,v2}=1
\iff
G_{DEV,v2}=1
\land
V\!-\!D06_{v2}=1
\land
V\!-\!I04_{v2}=1
\land
G_{repro,v2}=1.
```

If `V-D06_v2` fails the unchanged 1% median criterion on the fresh holdout:

```text
STOP.
Do not fit another scale to the holdout.
Do not weaken the threshold.
Do not introduce station/day-specific corrections.
Classify the current-to-energy metrology relation as unresolved for the declared 1% requirement.
Require new external voltage/meter evidence or redesign of the verification observable under a formal methodology review.
```

This is the final permitted corrective cycle under the current Phase-1 design.

---

# 12. Gate boundary

Even a successful v2 ACN gate establishes only corrected charging-data verification.

```math
\boxed{
G_{ACN,v2}=1
\not\Rightarrow
G_V=1
\not\Rightarrow
G_{VAL}=1
\not\Rightarrow
H_1/H_2.
}
```

Remaining coupling, temporal, parameter/sensitivity and complete reproducibility gates must still close before empirical validation and confirmatory H1/H2 execution.
