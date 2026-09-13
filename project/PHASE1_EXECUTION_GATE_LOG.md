# Phase 1 — Execution Gate Log

**Updated:** 2026-09-13  
**Purpose:** auditable state of the transition from preregistered experiment design to executable verification/validation.  
**Rule:** status reflects completed evidence, not intended work. Versioned failures remain preserved.

---

## 1. Authority chain

```text
CANONICAL_DEPENDENCY_CONTRACT_V1.md
PHASE1_EMPIRICAL_VALIDATION_PROTOCOL.md
PHASE1_EXPERIMENT_SPECIFICATION_V1.md
PHASE1_DATA_MANIFEST_V1.md
PHASE1_PARAMETER_REGISTER_V1.md
PHASE1_SOFTWARE_ENVIRONMENT_LOCK_V1.md
PHASE1_CANONICAL_EXECUTION_IDENTITY_V1.md
PHASE1_DATA_PROVENANCE_REGISTER_V1.md
PHASE1_VERIFICATION_TEST_MATRIX_V1.md
PHASE1_NUMERICAL_SOLVER_AMENDMENT_V1.md
PHASE1_VERIFICATION_EXECUTION_RESULTS_V1.md
PHASE1_ACN_PROCESSING_PROTOCOL_V1.md
PHASE1_INFORMATION_PROCESSING_PROTOCOL_V1.md
PHASE1_VD06_ROOT_CAUSE_AUDIT_V1.md
PHASE1_ACN_PROCESSING_AMENDMENT_V2.md
```

---

## 2. Current phase state

| Gate | State | Meaning |
|---|---|---|
| canonical dependency contract | `CLOSED` | dependency object remains frozen |
| experiment specification | `CLOSED / PREREGISTERED` | benchmark physics and mappings remain frozen |
| software environment | `CLOSED / G_ENV=1` | canonical locked environment verified |
| public P/T provenance | `CLOSED` | MATPOWER + Sioux Falls immutable identities closed |
| public P/T verification | **`PASS`** | power and transportation benchmark tests pass |
| ACN raw provenance v1 | **`PASS`** | authenticated 2019-10-10 through 2019-12-31 object acquired and hashed |
| ACN processing v1 | **`PASS`** | deterministic v1 transform and chronological split completed |
| `V-D06` v1 | **`FAIL`** | median energy reconstruction error 6.5629% > frozen 1% threshold |
| `V-I04` v1 | **`PASS`** | seasonal-slot RMSE <= persistence RMSE |
| V-D06 forensic audit | **`CLOSED`** | leading mechanisms isolated; v1 result preserved |
| ACN corrective v2 protocol | **`PREREGISTERED`** | prospective correction + fresh holdout frozen |
| v2 development gate | `NOT EXECUTED` | must freeze corrected development parameters/hashes first |
| v2 independent holdout | `NOT ACQUIRED` | 2020-01-01 through 2020-02-29 remains untouched |
| complete Phase-1 verification | **`G_V=0`** | noncompensable gate remains open |
| empirical validation | `BLOCKED` | requires complete verification |
| H1/H2 | `BLOCKED` | requires verified + sufficiently validated model |
| Stage-5 viability/resilience | `BLOCKED` | requires Phase-1 closure |

---

## 3. Canonical environment and public P/T evidence

Environment identity remains anchored to the successful executable head:

```text
environment workflow run = 34700750356
canonical P/T code SHA   = d6d97c7353f6d5694dba73ab840ae3a2548dd593
lock SHA256              = 68c37973b974af1fbf7214bf28a0a7473d4454f98a1678cf2fae703208d12fd4
G_ENV                    = 1
```

Public benchmark verification:

```text
workflow run             = 34700750330
power max residual       = 3.0808688933348094e-14
transport solver         = biconjugate-frank-wolfe
transport iterations     = 645
transport relative gap   = 9.33748496131895e-07
criterion                = <=1e-6 within 5000 iterations
verdict                   = PASS
```

Earlier failed FW/CFW convergence evidence remains preserved in the numerical-solver amendment/audit history. No tolerance or iteration cap was weakened.

---

## 4. ACN v1 acquisition and provenance — blocker closed

The earlier external-credential blocker is closed.

Canonical successful ACN raw/processing run:

```text
workflow run ID              = 34737402122
ACN processing code SHA      = 3611bbd099193b52b0c6a451b8df8b3ff7d0fa9b
ACN raw records              = 2082
ACN raw bytes                = 902786828
RAW_SHA256                   = ac6d9b237d4e6752dd990f42b569f0de90af125455a8ffdff20b53a7f30e35fd
acquisition manifest SHA256  = f268b6b00ee2cf59acabe3b334b57cb8c600c1440cae8137a6d89287a61e6584
processing manifest SHA256   = 7356fb40dc498e12c6917ab2a11ca4d1e1a4ed5289376f9814211c79e0b73f28
information manifest SHA256  = b056c9e3c6f4f6dacae93faac9202b17a26d465b815774f9fc4460bcbf6a0d22
artifact ID                  = 10312341206
artifact digest              = sha256:13f5af89f7da06be91ad9724903fb6d37c07ca2ae1d159ea83862b92580171e7
credential hygiene           = PASS
```

Therefore the v1 data/provenance chain is closed:

```math
\boxed{G_{D,v1}=1.}
```

This does not imply model verification.

---

## 5. ACN v1 scientific verification result

v1 processing produced:

```text
source sessions        = 2082
accepted sessions      = 1776
rejected sessions      = 306
usable days            = 21
calibration days       = 14
validation days        = 7
```

### V-D06 — FAIL

```text
validation days with sessions = 6
median epsilon_E               = 0.06562885747436485
p95 epsilon_E                  = 0.12702262312696583
max epsilon_E                  = 0.14700954955744558
criterion                      = median epsilon_E <= 0.01
verdict                        = FAIL
```

Hence

```math
\boxed{V\!-\!D06_{v1}=0.}
```

The threshold is retained unchanged.

### V-I04 — PASS

```text
RMSE seasonal-slot = 4.517522925614486 kW
RMSE persistence   = 5.446367106976146 kW
criterion          = seasonal-slot <= persistence
verdict            = PASS
```

Hence

```math
\boxed{V\!-\!I04_{v1}=1.}
```

A passing information subgate cannot compensate for the failed energy-reconstruction subgate.

---

## 6. Root-cause audit decision

The preserved post-failure audit is:

```text
project/PHASE1_VD06_ROOT_CAUSE_AUDIT_V1.md
project/phase1_runtime/audit_vd06.py
```

Main findings:

```text
systematic session-level E_recon/E_data median ~= 0.9470;
only 4/1776 accepted sessions begin >5 min after connection;
0/1776 end >5 min before disconnect;
282 sessions were rejected for non-strict current timestamps;
all 282 are duplicate-timestamp cases with no backward time;
778 duplicate pairs exist, 138 with different current values;
long-dwell CA-322 session on 2019-12-27 is corrected by doneChargingTime boundary;
calibration-only diagnostic effective scale ~=221.9 V;
post-failure diagnostic explains exposed validation data but is not confirmatory.
```

Scientific synthesis:

```math
\boxed{
\text{v1 V-D06 failure}
\approx
\text{nominal-voltage/metrology scale mismatch}
+
\text{disconnect-vs-doneChargingTime boundary defect}
}
```

with an additional data-retention problem caused by strict duplicate rejection.

The audit does not claim that 221.9 V is the measured physical voltage at every EVSE.

---

## 7. Prospective v2 corrective gate

The one permitted prospective correction is frozen in:

```text
project/PHASE1_ACN_PROCESSING_AMENDMENT_V2.md
```

It requires, before any new holdout is inspected:

```text
A1 collapse exact duplicate timestamps by deterministic arithmetic mean;
A2 reject genuine backward time and retain the <=5 min gap rule;
A3 use doneChargingTime as the active charging endpoint;
A4 estimate one global effective current-to-energy scale from development data only;
A5 freeze that scale and all development hashes;
A6 acquire a fresh untouched Caltech holdout: 2020-01-01 through 2020-02-29;
A7 retain the original median epsilon_E <=1% criterion;
A8 evaluate the fresh holdout once without retraining.
```

The existing 2019 object is development-only for v2 because its former validation outcomes have already been observed.

If the fresh v2 holdout fails, no third tuning cycle is allowed without new external metrology evidence and formal methodology review.

---

## 8. Versioned data-gate state

```math
\boxed{
G_{D,v1}=1,
\qquad
G_{V,v1}=0,
\qquad
G_{D,v2}=0,
\qquad
G_V=0.
}
```

`G_{D,v2}=0` means the prospective v2 development identity and fresh holdout are not yet materialized. It does not reopen or invalidate the immutable v1 raw-data identity.

---

## 9. Active hard path

```text
B1  implement v2 processor exactly as preregistered;
B2  add synthetic known-answer tests for duplicate collapse and doneChargingTime truncation;
B3  rerun the immutable 2019 development object and freeze V_eff_hat + all v2 development hashes;
B4  close G_DEV,v2 before acquiring the new holdout;
B5  acquire/hash the untouched 2020-01-01 through 2020-02-29 holdout;
B6  execute V-D06_v2 and V-I04_v2 once on the holdout;
B7  complete remaining coupling/temporal/sensitivity/reproducibility gates;
B8  obtain complete G_V=1 before empirical validation/H1/H2.
```

No step may weaken the 1% criterion or tune on the new holdout.

---

## 10. Current scientific interpretation

```math
\boxed{
G_{ENV}=1,
\quad
G_{D,v1}=1,
\quad
V\!-\!D06_{v1}=0,
\quad
V\!-\!I04_{v1}=1,
\quad
G_{D,v2}=0,
\quad
G_V=0.
}
```

Therefore:

```text
VALIDATION              = NOT AUTHORIZED
H1/H2                   = NOT AUTHORIZED
STAGE-5 VIABILITY       = NOT AUTHORIZED
NEXT AUTHORIZED ACTION  = IMPLEMENT + VERIFY v2 DEVELOPMENT ONLY
```
