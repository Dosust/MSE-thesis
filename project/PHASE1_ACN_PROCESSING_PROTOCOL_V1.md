# Phase 1C — ACN Processing Protocol v1

![Status](https://img.shields.io/badge/status-PREREGISTERED%20BEFORE%20ACN%20ACCESS-0969DA)
![Phase](https://img.shields.io/badge/phase-1C-1A7F37)

**Frozen:** 2026-09-12  
**Applies to:** the already-frozen Caltech ACN request in `PHASE1_DATA_MANIFEST_V1.md`  
**Boundary:** raw-to-processed verification only; no calibration tuning, holdout model validation, H1/H2, or Stage-5 analysis.

---

## 0. Governing rule

```math
\boxed{
\text{raw authenticated ACN object}
\rightarrow
\text{schema/QC}
\rightarrow
\text{deterministic reconstruction}
\rightarrow
\text{5-min site trajectory}
\rightarrow
\text{chronological split}
\rightarrow
\text{verification artifacts}
}
```

Claim tags:

```text
[E] externally established fact;
[P] preregistered thesis processing choice;
[D] mathematical consequence/rationale;
[A] explicit assumption;
[U] unresolved until raw data exist.
```

No processing rule in this file may be changed after inspecting the resulting validation-day errors without a versioned amendment.

---

# 1. External data semantics `[E]`

The official ACN-Data API documentation states that:

- `/sessions/<site_id>/ts` returns time-series fields;
- `chargingCurrent` is measured EVSE charging current;
- `pilotSignal` is the EVSE pilot-signal time series;
- timestamps are UTC/GMT RFC-1123 values and the session contains the local timezone;
- time-series requests are paginated at one session per page.

Primary source: `https://ev.caltech.edu/dataset`.

The frozen ACN Portal 0.3.3 source at commit

```text
14e723b11339e56ca3afd2bf4969f9e4bc8c2623
```

implements authenticated pagination through `DataClient.get_sessions(..., timeseries=True)` and uses `spaceID` as the EVSE identifier when converting ACN session records into simulator EV objects.

The frozen Caltech ACN infrastructure definition registers its EVSEs at nominal `208 V`, and `ChargingNetwork.voltages` exposes the station-to-voltage mapping. ACN-Sim defines aggregate charging power from EVSE voltages and charging currents as

```math
P_{agg}=V^T I/1000
```

in kW.

These external facts justify the field meaning and infrastructure mapping. They do **not** prescribe the resampling/interpolation choices below.

---

# 2. Required raw-session schema `[P]`

A session is structurally usable only if it contains:

```text
sessionID
spaceID
connectionTime
disconnectTime
kWhDelivered
chargingCurrent
pilotSignal
```

For the time-series objects, v1 expects the documented form

```text
chargingCurrent = {timestamps: [...], current: [...]}
pilotSignal     = {timestamps: [...], pilot: [...]}
```

with equal timestamp/value lengths and at least two samples.

Every timestamp must be timezone-aware. Naive timestamps are rejected.

Every used numeric current/pilot value and `kWhDelivered` must be finite and nonnegative.

An unknown `spaceID` that cannot be mapped to the frozen Caltech ACN EVSE set is rejected rather than assigned an invented voltage.

If the live API schema differs from this documented form, processing stops with a schema error. The schema is not guessed from observed values.

---

# 3. Time-series integrity rule `[P]`

For each current/pilot trace:

```math
t_1<t_2<\cdots<t_n.
```

The maximum admissible consecutive sample gap is frozen at one Phase-1 exchange interval:

```math
\boxed{\Delta t_{gap}\le5\text{ min}.}
```

A larger gap is treated as insufficient information for the declared 5-min replay and the affected session is rejected. Every local day spanned by a rejected session is excluded before calibration/validation splitting.

This is a thesis QC rule, not an ACN universal data-quality standard.

---

# 4. Current-to-power reconstruction `[P/D]`

For accepted session `n`, let the measured charging-current samples be

```math
(t_j,I_{n,j}).
```

Between observed samples, v1 uses deterministic piecewise-linear interpolation:

```math
I_n(t)=\operatorname{lininterp}\{(t_j,I_{n,j})\}.
```

No extrapolation beyond the first/last observed current sample is performed.

The EVSE voltage is obtained from the frozen `caltech_acn().voltages` mapping, not from an invented generic charging voltage. Thus

```math
P_n(t)=\frac{V_n I_n(t)}{1000}\quad[\mathrm{kW}].
```

For each 5-min interval `B_k=[t_k,t_{k+1})`, the interval-average site power is

```math
P_{ch,k}
=
\frac{1}{\Delta t}
\sum_n
\int_{B_k}P_n(t)\,dt,
\qquad
\Delta t=5\text{ min}.
```

The integral is evaluated deterministically by the trapezoidal rule on the observed samples plus inserted bin boundaries.

**No energy-normalization is allowed.** In particular, reconstructed current/power is **not** rescaled to force agreement with `kWhDelivered`. Doing so would make the energy-reconstruction verification nearly tautological.

---

# 5. Independent internal consistency check `[P]`

For each accepted session:

```math
E_{recon,n}
=
\int P_n(t)dt,
```

while `kWhDelivered_n` remains the separate session-level energy field from ACN-Data.

For reporting by local connection date `d`, define

```math
E_{sim}(d)
=
\sum_{n:\,date(c_n)=d}E_{recon,n},
```

```math
E_{data}(d)
=
\sum_{n:\,date(c_n)=d}kWhDelivered_n.
```

Then

```math
\epsilon_E(d)
=
\frac{|E_{sim}(d)-E_{data}(d)|}
{\max(E_{data}(d),10^{-12})}.
```

This clarifies `V-D06`: the day index is a **connection-date cohort** for the independent energy-field consistency check. It is distinct from the calendar-day site-load integration used for `P_ch(t)`.

The already-frozen primary acceptance rule remains

```math
\operatorname{median}_{d\in D_{val}}\epsilon_E(d)\le0.01.
```

No threshold is changed here.

---

# 6. Calendar-day grid and daylight-saving rule `[D/P]`

The analysis timezone remains

```text
America/Los_Angeles
```

and every accepted day must contain exactly

```math
24\times60/5=288
```

five-minute slots, as already frozen in `V-D05`.

The frozen window contains the 2019 fall daylight-saving transition. The local calendar day

```text
2019-11-03 America/Los_Angeles
```

has 25 elapsed hours and therefore cannot satisfy the already-frozen 288-slot definition without collapsing or deleting an hour.

Accordingly, before any ACN data are inspected:

```math
\boxed{2019\text{-}11\text{-}03\;\text{is excluded as DST_NON_24H_DAY}.}
```

No time samples are silently merged to manufacture 288 slots.

---

# 7. Query-boundary rule `[D/P]`

The frozen API query selects sessions by `connectionTime` beginning at local midnight on `2019-10-10`.

A vehicle that connected before the query boundary could still be charging after that boundary but would not be returned by a connection-time filter. Therefore the first calendar day cannot be guaranteed to represent complete site load.

Before data inspection, v1 therefore freezes:

```math
\boxed{2019\text{-}10\text{-}10\;\text{is excluded as LEFT_CENSORED_QUERY_BOUNDARY}.}
```

The raw sessions themselves remain preserved; this exclusion applies only to complete-day site-load analysis and the chronological day split.

---

# 8. Complete-day QC `[P]`

For every remaining local date in the frozen window:

```text
1. the day must be exactly 24 elapsed hours;
2. no rejected/corrupt session may overlap that local day;
3. the deterministic processor must produce all 288 slots;
4. zero active charging is represented by P_ch=0, not missing;
5. exclusion reason must be written to the QC ledger.
```

No day may be excluded because forecast error, power-system stress, H1/H2 effect size, or resilience outcome is unfavorable.

---

# 9. Chronological partition `[P]`

After all frozen QC/exclusions, sort usable days chronologically. With `N_d` usable days:

```math
N_{cal}=\lfloor0.70N_d\rfloor,
```

```math
D_{cal}=\{\text{first }N_{cal}\text{ usable days}\},
\qquad
D_{val}=\{\text{remaining days}\}.
```

and

```math
D_{cal}\cap D_{val}=\varnothing.
```

The exact date lists are hashed before any calibration/validation model comparison.

---

# 10. Required processed artifacts

The processor must emit at minimum:

```text
session_qc.csv
excluded_days.csv
usable_days.txt
calibration_days.txt
validation_days.txt
power_5min.csv
energy_reconstruction.csv
processing_manifest.json
```

Every artifact receives SHA-256 in `processing_manifest.json`.

The processed manifest must also record:

```text
raw canonical SHA-256;
source-session count;
accepted/rejected session counts;
usable/calibration/validation day counts;
5-min grid rule;
energy-reconstruction summary;
processor code SHA through the workflow identity.
```

Raw data are read-only and are never overwritten.

---

# 11. Verification meaning

Passing this processing protocol establishes only that the frozen ACN object has been transformed reproducibly according to the preregistered rules.

```math
\boxed{
G_{ACNproc}=1
\not\Rightarrow
G_V=1
\not\Rightarrow
G_{VAL}=1
\not\Rightarrow
H_1/H_2.
}
```

The full verification gate still requires the information, coupling, temporal, reproducibility, and sensitivity/coherence tests in `PHASE1_VERIFICATION_TEST_MATRIX_V1.md`.
