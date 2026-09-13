# Phase 1C — Data Provenance Register v1

![Status](https://img.shields.io/badge/status-v1%20PROVENANCE%20CLOSED%20%2F%20v2%20PENDING-BF8700)
![Phase](https://img.shields.io/badge/phase-1C-0969DA)

**Frozen/initialized:** 2026-09-12  
**Updated:** 2026-09-13 after authenticated ACN acquisition, v1 processing, preserved `V-D06` failure, and v2 preregistration.  
**Authority:** `PHASE1_DATA_MANIFEST_V1.md` + `PHASE1_CANONICAL_EXECUTION_IDENTITY_V1.md` + `PHASE1_VD06_ROOT_CAUSE_AUDIT_V1.md`.  
**Rule:** unavailable evidence is recorded explicitly; failed verification never erases valid data provenance.

---

## 0. Provenance object

For source object `d`, define

```math
\mathcal P_d=(ID_d,S_d,V_d,H_d,T_d,H_{code,T},H_{out},\sigma_d),
```

with scientific chain

```math
\boxed{S_d\rightarrow V_d\rightarrow H_d\rightarrow T_d\rightarrow H_{out}\rightarrow\text{model variable}.}
```

Evidence states used here:

```text
SOURCE_LOCKED
RAW_HASHED
PROCESSED_HASHED
SPLIT_HASHED
INFORMATION_HASHED
VERIFICATION_FAIL_PRESERVED
V2_DEVELOPMENT_PENDING
V2_HOLDOUT_PENDING
```

---

# 1. Power benchmark provenance

## D-PWR-01

```text
source              = MATPOWER/matpower
upstream commit     = 2e0ef79a6c4526858ee923491d92781ad4507fb7
path                = data/case33bw.m
Git blob SHA        = 97e510bee25c543de0453959672fe86b40a999c8
local raw SHA-256   = b40831eeb444669ae876e2996f0dda9f05cd83e81b314b8dfca51e4890cca95d
local raw bytes     = 4866
charging interface  = bus 24
fault branch        = 23 -> 24
state               = RAW_HASHED
```

Verification evidence:

```text
workflow run        = 34700750330
code SHA            = d6d97c7353f6d5694dba73ab840ae3a2548dd593
power balance max   = 3.0808688933348094e-14
positive-load sign  = PASS
```

---

# 2. Transportation benchmark provenance

## D-TRN-01 — network

```text
source              = bstabler/TransportationNetworks
upstream commit     = d1639b4ef218c17928ba573e806ddf8ba5e7ae6d
path                = SiouxFalls/SiouxFalls_net.tntp
Git blob SHA        = 66d0eca4ddcfb82f861bea040060deab7a741b2f
local raw SHA-256   = ace99b24cec69c273ff0cf3d6d074110177f0cc0ae24b0c7a9f4f4cb5e27635c
local raw bytes     = 3136
state               = RAW_HASHED
```

## D-TRN-02 — OD demand

```text
source              = bstabler/TransportationNetworks
upstream commit     = d1639b4ef218c17928ba573e806ddf8ba5e7ae6d
path                = SiouxFalls/SiouxFalls_trips.tntp
Git blob SHA        = db70eda57738877811e9ac07c25a567973d3b6a0
local raw SHA-256   = 56f9566857f3f66730fd5c4232258d7ee3ac2931a476526331afd062f4958de7
local raw bytes     = 10859
published OD total  = 360600
state               = RAW_HASHED
```

Canonical numerical verification:

```text
workflow run         = 34700750330
solver               = biconjugate-frank-wolfe
iterations           = 645
relative gap         = 9.33748496131895e-07
criterion            = <=1e-6 within 5000 iterations
scaled node residual = 1.715075976720996e-16
verdict               = PASS
```

---

# 3. EV charging provenance — v1 raw object

## D-EV-01-v1

Frozen request:

```text
source/API          = ACN-Data / Caltech
site                = caltech
start local         = 2019-10-10 00:00:00 America/Los_Angeles
end local           = 2019-12-31 23:59:59 America/Los_Angeles
timeseries          = true
client              = acnportal==0.3.3
workflow            = .github/workflows/phase1-acn-acquisition.yml
```

Successful materialization:

```text
workflow run ID     = 34737402122
code SHA            = 3611bbd099193b52b0c6a451b8df8b3ff7d0fa9b
acquired UTC        = 2026-09-13T04:48:07Z
raw records         = 2082
raw bytes           = 902786828
RAW_SHA256          = ac6d9b237d4e6752dd990f42b569f0de90af125455a8ffdff20b53a7f30e35fd
manifest SHA256     = f268b6b00ee2cf59acabe3b334b57cb8c600c1440cae8137a6d89287a61e6584
credential hygiene  = PASS
state               = RAW_HASHED
```

The earlier `BLOCKED_EXTERNAL_CREDENTIAL` state is historical only. Authentication and raw acquisition are now closed.

---

# 4. ACN v1 processed object

## D-EV-PROC-01-v1

Transformation:

```math
D_{raw,v1}
\rightarrow
\text{schema/QC}
\rightarrow
P_{ch}^{5min}
\rightarrow
(D_{cal},D_{val}).
```

Observed identities:

```text
source sessions             = 2082
accepted sessions           = 1776
rejected sessions           = 306
usable days                 = 21
calibration days            = 14
validation days             = 7
processing manifest SHA256  = 7356fb40dc498e12c6917ab2a11ca4d1e1a4ed5289376f9814211c79e0b73f28
power_5min SHA256           = cce60bc99e303418cbf16623948b82c78ac84cedb35560493fc84fed8330e1e5
session_qc SHA256           = 7ef40e581399dc0f744e2e409c6626e02066e0a46ac3c6a74e57a8facafa81c9
excluded_days SHA256        = 45c4cdca3f2f034d96803d86d24adba996b11ae9dab8a138952adb05373cfaa7
usable_days SHA256          = 8416da9a6023e0be30900aaaabb977bd0f7e702490b6bfe611b9cde91df2dd31
calibration_days SHA256     = f0373785d3fa73f9a0fec1425de4d1b78f746507a231911cf79e0710d0495f8e
validation_days SHA256      = c9f3b90dc5c23b14ca971b599720a4f5161ce6b16da65a0c681089016a385643
energy_reconstruction SHA256= 7a0855c9f422c697829aa8a49bc6db1e6264cb47eedd6b19cb4dc166e129b8e5
state                       = PROCESSED_HASHED + SPLIT_HASHED
```

These are valid immutable v1 processing identities even though `V-D06` failed.

---

# 5. Information-processing provenance — v1

## D-INF-01-v1

```text
information manifest SHA256  = b056c9e3c6f4f6dacae93faac9202b17a26d465b815774f9fc4460bcbf6a0d22
slot means SHA256             = 913de23bfc6d8d8324e17a586403808fc80dbedbcccb398f68eedc1614d96b8e
LOO residuals SHA256          = 2549258f0ee38a2abe15bb7e5f0a56182beea9fdec9c2f1deababf1a2058a8ac
P_ref                         = 0.0 kW
P_site_cap                    = 150.0 kW
latencies                     = 0,5,15,30 min
state                         = INFORMATION_HASHED
```

Verification result:

```text
RMSE seasonal-slot = 4.517522925614486 kW
RMSE persistence   = 5.446367106976146 kW
V-I04              = PASS
```

---

# 6. v1 verification result attached to provenance

Data integrity and model verification are separate.

For the same immutable v1 object:

```text
V-D06 median epsilon_E = 0.06562885747436485
V-D06 threshold        = <=0.01
V-D06                  = FAIL
V-I04                  = PASS
```

Therefore:

```math
\boxed{
G_{D,v1}=1
\quad\land\quad
G_{V,v1}=0.
}
```

A failed verification gate does not invalidate the raw or processed hashes.

---

# 7. Forensic audit provenance

The post-failure diagnostic is versioned separately:

```text
report = project/PHASE1_VD06_ROOT_CAUSE_AUDIT_V1.md
code   = project/phase1_runtime/audit_vd06.py
```

It is diagnostic only. It does not modify `D-EV-01-v1`, `D-EV-PROC-01-v1`, the v1 threshold, or the v1 verdict.

Principal observed audit facts include:

```text
282 sessions rejected for non-strict charging-current timestamps;
all 282 exhibit exact duplicate timestamps without backward time;
778 duplicate pairs total;
138 duplicate pairs contain different current values;
long-dwell CA-322 session is inconsistent when integrated to disconnect but aligns when truncated at doneChargingTime;
calibration-only effective current-to-energy scale is about 221.9 V in the exposed diagnostic subset.
```

The inferred scale is not promoted to an external physical-voltage fact.

---

# 8. Prospective v2 provenance objects

The corrective protocol is frozen in:

```text
project/PHASE1_ACN_PROCESSING_AMENDMENT_V2.md
```

## D-EV-DEV-01-v2

```text
source raw object   = D-EV-01-v1
role                = v2 development/calibration only
processor           = duplicate collapse + doneChargingTime truncation + global effective-scale calibration
processor SHA       = PENDING
V_eff_hat           = PENDING
output hashes       = PENDING
state               = V2_DEVELOPMENT_PENDING
```

The old v1 validation days are not independent v2 confirmation because they have already been inspected.

## D-EV-HOLDOUT-01-v2

Frozen untouched request:

```text
source/API          = ACN-Data / Caltech
site                = caltech
start local         = 2020-01-01 00:00:00 America/Los_Angeles
end local           = 2020-02-29 23:59:59 America/Los_Angeles
timeseries          = true
client              = acnportal==0.3.3
role                = independent v2 verification holdout
raw SHA256          = PENDING
manifest SHA256     = PENDING
state               = V2_HOLDOUT_PENDING
```

This holdout must not be acquired until `G_DEV,v2=1` and the development scale/parameter hashes are frozen.

---

# 9. Synthetic cross-domain mapping provenance

The experimental mapping remains:

```math
\boxed{P\text{ bus }24\leftrightarrow T\text{ node }10\leftrightarrow\text{Caltech charging forcing}.}
```

```text
mapping type        = preregistered synthetic experimental mapping
co-located reality  = NO
geographic claim    = PROHIBITED
```

No change to the synthetic mapping is introduced by the ACN v2 processing correction.

---

# 10. Versioned integrity gates

For v1:

```math
G_{D,v1}
=
G_{PWR}G_{TRNnet}G_{TRNod}G_{ACNraw,v1}G_{ACNproc,v1}G_{split,v1}=1.
```

For active prospective v2:

```math
G_{D,v2}
=
G_{DEV,v2}G_{ACNholdout,v2}G_{ACNproc,v2}G_{repro,v2}.
```

Current state:

| Gate | State |
|---|---|
| `G_PWR` | `1` |
| `G_TRNnet` | `1` |
| `G_TRNod` | `1` |
| `G_ACNraw,v1` | `1` |
| `G_ACNproc,v1` | `1` |
| `G_split,v1` | `1` |
| `G_D,v1` | **`1`** |
| `G_DEV,v2` | `0 / PENDING` |
| `G_ACNholdout,v2` | `0 / NOT ACQUIRED` |
| `G_D,v2` | **`0`** |

Thus:

```math
\boxed{G_{D,v1}=1,\qquad G_{D,v2}=0.}
```

---

# 11. Current permissible claim

```math
\boxed{
\text{public P/T provenance closed}
\land
\text{ACN v1 raw/processed provenance closed}
\land
\text{v1 V-D06 failed at the frozen threshold}
\land
\text{prospective v2 development/holdout provenance remains open}.
}
```

No empirical validation, H1/H2, or Stage-5 claim is authorized until the corrected v2 ACN gate and the remaining complete verification gates close.
