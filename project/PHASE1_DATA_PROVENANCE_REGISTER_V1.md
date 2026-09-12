# Phase 1C — Data Provenance Register v1

![Status](https://img.shields.io/badge/status-PROVENANCE%20REGISTER%20ACTIVE-0969DA)
![Phase](https://img.shields.io/badge/phase-1C-1A7F37)

**Frozen/initialized:** 2026-09-12  
**Authority:** `PHASE1_DATA_MANIFEST_V1.md` + `PHASE1_CANONICAL_EXECUTION_IDENTITY_V1.md`  
**Purpose:** provide one auditable chain from each external source to every Phase-1 executable input.  
**Rule:** unavailable evidence is recorded as `[U]`; it is never inferred, fabricated, or replaced.

---

## 0. Provenance object

For source object `d`, define

```math
\mathcal P_d
=
(
ID_d,
S_d,
V_d,
H_d,
T_d,
H_{code,T},
H_{out},
\sigma_d
),
```

where

```text
ID_d       = thesis data-object identifier;
S_d        = upstream source/repository/API;
V_d        = immutable upstream version/commit/query;
H_d        = upstream/local integrity identity;
T_d        = deterministic transformation chain;
H_code,T   = code commit implementing transformation;
H_out      = hash of locally materialized/derived output;
sigma_d    = evidence state.
```

Evidence states:

```text
SOURCE_LOCKED
RAW_HASHED
PROCESSED_HASHED
BLOCKED_EXTERNAL_CREDENTIAL
DERIVED_PENDING
```

The scientific chain is

```math
\boxed{
S_d
\rightarrow
V_d
\rightarrow
H_d
\rightarrow
T_d
\rightarrow
H_{out}
\rightarrow
\text{model variable}.
}
```

---

# 1. Power benchmark provenance

## D-PWR-01

```text
source              = MATPOWER/matpower
upstream commit     = 2e0ef79a6c4526858ee923491d92781ad4507fb7
path                = data/case33bw.m
Git blob SHA        = 97e510bee25c543de0453959672fe86b40a999c8
role                = immutable electrical benchmark
model mapping       = bus/branch data -> radial power model
charging interface  = bus 24 [P]
fault branch        = 23 -> 24 [P]
state               = SOURCE_LOCKED
```

No electrical parameter is calibrated against Phase-1 coupled outcomes.

---

# 2. Transportation benchmark provenance

## D-TRN-01 — network

```text
source              = bsstabler/TransportationNetworks (canonical source recorded in data manifest as bsstabler/TransportationNetworks)
upstream commit     = d1639b4ef218c17928ba573e806ddf8ba5e7ae6d
path                = SiouxFalls/SiouxFalls_net.tntp
Git blob SHA        = 66d0eca4ddcfb82f861bea040060deab7a741b2f
role                = immutable transportation-network benchmark
depot node          = 1 [P]
repair/FCS node     = 10 [P]
closure             = 9->10 and 10->9 [P]
state               = SOURCE_LOCKED
```

**Normalization note:** the repository owner string is `bstabler`; any typographical rendering elsewhere must resolve to the exact immutable commit/blob pair above before execution.

## D-TRN-02 — OD demand

```text
source              = bsstabler/TransportationNetworks canonical repository
upstream commit     = d1639b4ef218c17928ba573e806ddf8ba5e7ae6d
path                = SiouxFalls/SiouxFalls_trips.tntp
Git blob SHA        = db70eda57738877811e9ac07c25a567973d3b6a0
published total OD  = 360600
role                = immutable demand benchmark
state               = SOURCE_LOCKED
```

The entire OD table is admissible; no OD pair is removed in response to model outputs.

---

# 3. EV charging provenance

## D-EV-01 — ACN raw source

Frozen request:

```text
source/API          = ACN-Data / Caltech
site                = caltech
start local         = 2019-10-10 00:00:00 America/Los_Angeles
end local           = 2019-12-31 23:59:59 America/Los_Angeles
timeseries          = true
client              = acnportal==0.3.3
acquisition code    = project/phase1_runtime/acquire_acn.py
```

Acquisition execution evidence:

```text
workflow            = Phase 1 authenticated ACN acquisition
workflow run ID     = 34698786730
head SHA            = c509d7de85627dda9f99023aa8acb5b24737cc9d
lock verification   = PASS
credential-presence = FAIL / ACN_API_TOKEN unavailable
raw acquisition     = SKIPPED
raw SHA-256         = UNRESOLVED
state               = BLOCKED_EXTERNAL_CREDENTIAL
```

The failure occurred before any API request/data transformation. Therefore it is an access-state observation, not a data-quality result and not scientific evidence against the model.

---

# 4. ACN derived objects

## D-EV-PROC-01 — 5-minute charging trajectory

```text
input               = D-EV-01
transform           = infrastructure-aware replay/aggregation on 5-min grid
output              = P_ch(t)
output SHA-256       = PENDING
state               = DERIVED_PENDING
blocking dependency = D-EV-01
```

## D-EV-SPLIT-01 — chronological calibration/validation split

```text
input               = QC-passed complete ACN days
rule                = first floor(0.70*N_d) days -> D_cal; remainder -> D_val
calibration list SHA= PENDING
validation list SHA = PENDING
state               = DERIVED_PENDING
blocking dependency = D-EV-PROC-01
```

## D-INF-01 — information calibration products

```text
input               = D_cal only
objects             = slot/daytype means, residual distribution, P_ref
hashes              = PENDING
state               = DERIVED_PENDING
blocking dependency = D-EV-SPLIT-01
```

No `D_val` observation is permitted in these products.

---

# 5. Cross-domain mapping provenance

The synthetic experimental mapping is

```math
\boxed{
P\text{ bus }24
\leftrightarrow
T\text{ node }10
\leftrightarrow
\text{Caltech charging forcing}.
}
```

State:

```text
mapping type        = preregistered synthetic experimental mapping [A/P]
co-located reality  = NO
geographic claim    = PROHIBITED
version             = Phase-1 v1
```

This mapping tests causal/executable dependency mechanics; it does not assert that the three benchmark sources represent one real city.

---

# 6. Integrity gate

Define

```math
G_D
=
G_{PWR}
G_{TRNnet}
G_{TRNod}
G_{ACNraw}
G_{ACNproc}
G_{split}.
```

Current status:

| Gate | State |
|---|---|
| `G_PWR` | `1 / SOURCE_LOCKED` |
| `G_TRNnet` | `1 / SOURCE_LOCKED` |
| `G_TRNod` | `1 / SOURCE_LOCKED` |
| `G_ACNraw` | `0 / BLOCKED_EXTERNAL_CREDENTIAL` |
| `G_ACNproc` | `0 / NOT GENERATED` |
| `G_split` | `0 / NOT GENERATED` |

Therefore

```math
\boxed{G_D=0\quad\text{at present}.}
```

Here `0` means **gate not closed**, not “dataset invalid”.

---

# 7. Exact unblock condition

The ACN raw-data gate closes only when a successful execution of the frozen acquisition workflow records:

```text
record count;
raw byte count;
RAW_SHA256;
acquisition-manifest SHA256;
UTC retrieval time;
acquisition code SHA;
canonical lock SHA;
credential-hygiene PASS.
```

The credential must be supplied through GitHub Actions secret `ACN_API_TOKEN`; it must never be committed or pasted into a thesis artifact.

---

# 8. Current permissible claim

```math
\boxed{
\text{Power/transport source provenance closed}
\quad\land\quad
\text{ACN source identity fixed}
\quad\land\quad
\text{ACN materialization blocked by credential}.
}
```

No empirical validation, H1/H2, or Stage-5 claim can be based on ACN data until `G_D=1`.
