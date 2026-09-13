# Phase 1C — V-D06 Root-Cause Audit v1

![Status](https://img.shields.io/badge/status-POST--FAILURE%20FORENSIC%20AUDIT-BF8700)
![Gate](https://img.shields.io/badge/V--D06-FAIL-D1242F)

**Frozen:** 2026-09-13  
**Scope:** diagnose the preserved Phase-1 v1 ACN energy-reconstruction failure without changing the v1 threshold, raw data, chronological split, H1/H2, or Stage-5 quantities.  
**Method:** `LEARN -> VERIFY -> FORMULATE -> DERIVE -> TEST -> VALIDATE -> SYNTHESIZE -> ADVANCE`.

---

## 0. Governing scientific rule

```math
\boxed{
\text{FAIL}\rightarrow\text{DIAGNOSE}\rightarrow\text{EXPLAIN}
\rightarrow\text{AMEND only if justified}
}
```

The forbidden path is

```math
\text{FAIL}\rightarrow\text{change threshold}\rightarrow\text{PASS}.
```

The v1 result is immutable historical evidence and remains `FAIL` even if a later version succeeds.

Claim tags:

```text
[E] observed/external evidence;
[D] derived mathematical consequence;
[H] diagnostic hypothesis;
[P] proposed next-step design;
[A] assumption;
[U] unresolved.
```

---

# 1. LEARN — immutable evidence object `[E]`

Canonical failed scientific run:

```text
workflow                    = Phase 1 authenticated ACN acquisition
run ID                      = 34737402122
head/code SHA               = 3611bbd099193b52b0c6a451b8df8b3ff7d0fa9b
lock SHA256                 = 68c37973b974af1fbf7214bf28a0a7473d4454f98a1678cf2fae703208d12fd4
raw records                 = 2082
raw bytes                   = 902786828
raw SHA256                  = ac6d9b237d4e6752dd990f42b569f0de90af125455a8ffdff20b53a7f30e35fd
acquisition manifest SHA256 = f268b6b00ee2cf59acabe3b334b57cb8c600c1440cae8137a6d89287a61e6584
processing manifest SHA256  = 7356fb40dc498e12c6917ab2a11ca4d1e1a4ed5289376f9814211c79e0b73f28
information manifest SHA256 = b056c9e3c6f4f6dacae93faac9202b17a26d465b815774f9fc4460bcbf6a0d22
artifact ID                 = 10312341206
artifact digest             = sha256:13f5af89f7da06be91ad9724903fb6d37c07ca2ae1d159ea83862b92580171e7
```

The workflow completed raw acquisition, provenance freeze, ACN raw-to-processed transformation, and information processing before the scientific subgate failed.

Observed v1 subgates:

```math
\boxed{V\!-\!D06=\mathrm{FAIL}},
\qquad
\boxed{V\!-\!I04=\mathrm{PASS}}.
```

For `V-D06`:

```text
validation days with sessions = 6
median epsilon_E               = 0.06562885747436485
p95 epsilon_E                  = 0.12702262312696583
max epsilon_E                  = 0.14700954955744558
frozen threshold               = median epsilon_E <= 0.01
```

For `V-I04`:

```text
RMSE seasonal-slot = 4.517522925614486 kW
RMSE persistence   = 5.446367106976146 kW
criterion          = seasonal-slot <= persistence
verdict            = PASS
```

Therefore `V-I04` is not the blocker. `V-D06` is the active ACN scientific blocker.

---

# 2. VERIFY — confirm that the failure is not an acquisition or execution-path failure `[E/D]`

The following steps passed in Run 34737402122:

```text
environment/hash lock                    PASS
synthetic ACN/information fixtures       PASS
credential presence                      PASS
raw ACN acquisition                      PASS
raw provenance freeze                    PASS
ACN raw-to-5-min transformation          PASS
information processing                   PASS
credential hygiene                       PASS
artifact upload                          PASS
```

The prior `ModuleNotFoundError` from Run 34735300852 was already corrected before Run 34737402122. It is therefore not a candidate explanation for `V-D06`.

The independent forensic implementation is:

```text
project/phase1_runtime/audit_vd06.py
```

It is diagnostic only and cannot modify the v1 artifacts.

---

# 3. FORMULATE — candidate mechanisms `[H]`

The audit tests the following non-exclusive mechanisms.

```text
H_A  numerical integration defect;
H_B  incomplete current-trace support near connection/disconnection;
H_C  semantic mismatch between ACN-Sim nominal 208 V and metered ACN-Data energy;
H_D  post-charge/idle current floor integrated until disconnect rather than doneChargingTime;
H_E  duplicate-timestamp QC is too destructive for this raw API representation;
H_F  isolated session anomalies dominate one or more validation-day errors.
```

No hypothesis is accepted merely because it improves the failed metric. The observed signature must match the mechanism.

---

# 4. DERIVE — diagnostic signatures `[D]`

## 4.1 Voltage-scale signature

With v1 nominal voltage `V_0=208 V`, session reconstruction is

```math
E_{208,n}
=
\frac{208}{1000\times3600}
\int I_n(t)dt.
```

If a multiplicative voltage/metrology scale dominates, define the implied effective voltage

```math
V_{eff,n}
=
208\frac{E_{data,n}}{E_{208,n}}.
```

A systematic under-reconstruction with relatively stable `V_eff,n` supports a scale mismatch more strongly than a numerical integration defect.

## 4.2 Active-charging boundary signature

ACN-Data documents `doneChargingTime` as the time of the last non-zero current draw recorded. A session with long parking dwell after charging may therefore satisfy

```math
\int_{connection}^{disconnect}I(t)dt
>
\int_{connection}^{doneChargingTime}I(t)dt
```

if the measured trace contains a non-zero idle/sensor floor after active charging.

## 4.3 Duplicate timestamp signature

Strict v1 requires

```math
t_1<t_2<\cdots<t_n.
```

If violations are exact equal timestamps rather than true backward time, the issue is a multivalued observation at one time instant rather than chronological reversal.

---

# 5. TEST — observed forensic results `[E/D]`

## 5.1 Raw/session retention

```text
source sessions            = 2082
accepted by v1             = 1776
rejected by v1             = 306
usable complete days       = 21
calibration days           = 14
validation days            = 7
```

The strict QC therefore retained only 21 of the candidate calendar days after the left-boundary, DST, and rejected-active-session rules were applied.

## 5.2 Time-support test

Among the 1776 v1-accepted sessions:

```text
first current sample >5 min after connection = 4 sessions
last current sample >5 min before disconnect = 0 sessions
```

The four late-start cases are not sufficient to explain the systematic ~6% validation-day under-reconstruction. In particular, the principal v1 validation cohorts are not characterized by widespread missing trace support.

**Audit assessment:** `H_B` is not supported as the primary mechanism.

## 5.3 Nominal-voltage/systematic-scale test

Across v1-accepted nonzero-energy sessions using the original disconnect boundary:

```text
median E_recon / E_data          = 0.9470403314584039
median absolute relative error   = 0.054545454545454605
```

Thus the dominant population tendency is approximately 5.3% under-reconstruction at the session level.

Using only the original calibration subset and cropping at `doneChargingTime`, the robust implied global effective voltage is

```math
\boxed{V_{eff,cal}=221.91218340366663\ \mathrm{V}}.
```

This is **not** declared to be the physical feeder voltage. It is a calibration-only effective metrology scale summarizing the relationship between measured current and the independent `kWhDelivered` field.

Official ACN-Data documentation identifies `chargingCurrent` as measured EVSE current and `kWhDelivered` as session energy. ACN-Sim is a simulator that uses an infrastructure model; the nominal `208 V` simulator quantity therefore cannot automatically be treated as a 1%-accuracy metrology measurement for every ACN-Data session.

**Audit assessment:** `H_C` is strongly supported as the leading explanation for the systematic scale component, but the exact physical source of the scale difference remains `[U]` without independent voltage-meter evidence.

## 5.4 `doneChargingTime` / idle-floor test

Cropping the reconstruction at `doneChargingTime` instead of `disconnectTime` changes the population median only slightly:

```text
median E_recon / E_data        = 0.9466837295115336
median absolute relative error = 0.0538437236908402
```

Therefore the active-charging boundary is not the main explanation for the systematic ~5-6% scale difference.

However, it resolves a major isolated failure mechanism. The largest validation-session outlier is:

```text
sessionID       = 2_39_78_360_2019-12-27 18:08:38.243155
spaceID         = CA-322
kWhDelivered    = 6.032 kWh
v1 disconnect reconstruction ~= 14.14 kWh
session duration             = 51.83 h
doneChargingTime reconstruction = 6.030928315405669 kWh
```

The raw session reports `doneChargingTime` about two hours after connection while the vehicle remains connected for more than two days. Integrating the low non-zero current floor throughout the entire parking dwell produces the extreme over-reconstruction.

**Audit assessment:** `H_D` is strongly supported for the 2019-12-27 outlier and is a semantic boundary defect in v1, even though it does not explain the global scale bias.

## 5.5 Duplicate-timestamp test

Of the 306 v1-rejected sessions, 282 were rejected because charging-current timestamps were not strictly increasing.

For those 282 sessions:

```text
sessions with exact duplicate timestamps and no backward time = 282
exact duplicate adjacent timestamp pairs                       = 778
pairs with identical current value                             = 640
pairs with different current values                            = 138
sessions containing >=1 different-value duplicate             = 107
```

A separate deterministic diagnostic that collapses equal-time observations and retains the original `<=5 min` gap rule shows that 287 of the 306 v1-rejected sessions become structurally admissible; only 19 remain rejected for genuine missing-object/gap failures. Under this diagnostic, 70 calendar days would be structurally usable rather than 21, including 48 weekdays and 22 weekend days.

This result is **diagnostic only**. It does not rewrite v1 QC.

**Audit assessment:** `H_E` is strongly supported. The v1 strict inequality confounds duplicate timestamps with true chronological reversal and causes substantial data loss.

## 5.6 Controller reference consequence

Under v1 processing:

```text
calibration 5-min slots = 4032
zero-power slot fraction = 0.5550595238095238
mean P_ch                = 3.2089673141534387 kW
median P_ch / P_ref      = 0.0 kW
```

Hence

```math
\boxed{P_{ref}=0}.
```

This is mathematically consistent with the preregistered median rule. It is not itself a software bug. But because v1 QC reduced the dataset to only 21 usable days, the engineering usefulness of a zero reference for the later controller must be re-evaluated after corrected preprocessing on an independent holdout.

---

# 6. VALIDATE — diagnostic cross-check without claiming v1 PASS `[D]`

A post-failure diagnostic combines two physically motivated changes:

```text
1. integrate active charging only through doneChargingTime;
2. estimate one global effective voltage scale from the original calibration subset only.
```

Applying that calibration-only scale to the **already exposed** v1 validation days gives:

```text
median validation-day epsilon_E = 0.004830166593458883
max validation-day epsilon_E    = 0.008871621547181262
```

Thus every nonempty v1 validation day is below 1% under this diagnostic formulation.

This result is **not confirmatory evidence**, because the formulation was designed after observing the v1 failure. It establishes only that the identified mechanisms are quantitatively capable of explaining the observed failure.

Therefore:

```math
\boxed{
\text{diagnostic fit on exposed data}
\neq
\text{independent validation}
}
```

---

# 7. SYNTHESIZE — root-cause decision

The evidence supports a two-part root cause:

```math
\boxed{
\text{V-D06 failure}
\approx
\text{nominal-voltage/metrology scale mismatch}
+
\text{disconnect-vs-doneChargingTime boundary error}
}
```

with a separate data-retention problem:

```math
\boxed{
\text{strict duplicate rejection}
\rightarrow
\text{large loss of structurally usable sessions/days}.
}
```

More precisely:

| Candidate | Decision | Evidence |
|---|---|---|
| numerical integration defect | `NOT SUPPORTED AS PRIMARY` | systematic scale remains under exact piecewise-linear replay |
| missing trace boundaries | `NOT SUPPORTED AS PRIMARY` | only 4/1776 late-start cases; no widespread early-end deficit |
| nominal 208-V metrology equivalence | `NOT SUPPORTED` | robust calibration-implied scale ~221.9 V |
| disconnect as active-energy endpoint | `REJECT FOR v2` | CA-322 long-dwell outlier collapses from ~14.14 to 6.03 kWh at doneChargingTime |
| strict rejection of equal timestamps | `REJECT FOR v2` | 282 duplicate-only sessions; no backward time |
| v1 1% threshold | `RETAIN` | no evidence justifies weakening the criterion |

The audit does **not** prove the physical voltage at every EVSE is 221.9 V. It proves that treating the simulator's nominal 208 V as a universal 1%-accuracy metrology conversion is not supported by the observed current/energy relationship.

---

# 8. ADVANCE — controlled prospective correction `[P]`

The next admissible action is a versioned v2 amendment with a fresh, untouched temporal holdout.

The amendment must:

```text
1. preserve Run 34737402122 and V-D06=FAIL permanently;
2. collapse exact duplicate timestamps deterministically rather than classify them as time reversal;
3. use doneChargingTime as the active-charging integration endpoint;
4. estimate one global effective current-to-energy scale from development data only;
5. retain the original <=1% median V-D06 criterion;
6. reacquire a newly frozen future ACN window that has not been inspected;
7. evaluate v2 only once on that independent holdout;
8. keep validation, H1/H2 and Stage-5 blocked until the corrected verification gate closes.
```

The prospective design is frozen separately in:

```text
PHASE1_ACN_PROCESSING_AMENDMENT_V2.md
```

If the independent v2 holdout fails the unchanged 1% criterion, no third tuning cycle is permitted without new external metrology evidence and a formal methodology review.

---

# 9. Current gate implication

```math
\boxed{
G_{ENV}=1,
\qquad
G_{ACNraw}=1,
\qquad
G_{ACNproc,v1}=1,
\qquad
V\!-\!D06_{v1}=0,
\qquad
V\!-\!I04_{v1}=1,
\qquad
G_V=0.
}
```

Therefore:

```text
empirical validation = BLOCKED
H1/H2                 = BLOCKED
Stage-5 viability     = BLOCKED
```

The scientific result is not "the thesis failed." The result is that the first metrology reconstruction specification was falsified at its preregistered threshold, and the failure mechanism has now been isolated sufficiently to justify one prospective corrective experiment.

---

# 10. External semantic sources

Primary dataset semantics:

```text
https://ev.caltech.edu/dataset
```

ACN-Data identifies `chargingCurrent` as measured current, `kWhDelivered` as delivered session energy, and `doneChargingTime` as the time of the last non-zero current draw recorded.

ACN-Sim context:

```text
https://ev.caltech.edu/simulator.html
https://github.com/zach401/acnportal
```

These sources justify the semantic distinction between observed ACN-Data fields and ACN-Sim's infrastructure model. They do not independently establish the physical voltage responsible for the ~221.9-V effective scale inferred from the development data.
