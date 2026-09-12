# Phase 1C — Data Provenance Register v1

![Status](https://img.shields.io/badge/status-PUBLIC%20P%2FT%20PROVENANCE%20CLOSED-1A7F37)
![Phase](https://img.shields.io/badge/phase-1C-0969DA)

**Frozen/initialized:** 2026-09-12  
**Updated:** 2026-09-12 after successful immutable public P/T verification  
**Authority:** `PHASE1_DATA_MANIFEST_V1.md` + `PHASE1_CANONICAL_EXECUTION_IDENTITY_V1.md`  
**Purpose:** provide one auditable chain from each external source to every Phase-1 executable input.  
**Rule:** unavailable evidence is recorded as `[U]`; it is never inferred, fabricated, or replaced.

---

## 0. Provenance object

For source object `d`, define

```math
\mathcal P_d=(ID_d,S_d,V_d,H_d,T_d,H_{code,T},H_{out},\sigma_d),
```

where `ID_d` is the thesis data-object identifier, `S_d` the upstream source, `V_d` its immutable version/query, `H_d` the upstream/local integrity identity, `T_d` the deterministic transformation chain, `H_{code,T}` the code revision, `H_out` the derived-output hash and `sigma_d` the evidence state.

The scientific chain is

```math
\boxed{S_d\rightarrow V_d\rightarrow H_d\rightarrow T_d\rightarrow H_{out}\rightarrow\text{model variable}.}
```

Evidence states:

```text
SOURCE_LOCKED
RAW_HASHED
PROCESSED_HASHED
BLOCKED_EXTERNAL_CREDENTIAL
DERIVED_PENDING
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
role                = immutable electrical benchmark
charging interface  = bus 24 [P]
fault branch        = 23 -> 24 [P]
state               = RAW_HASHED
```

Canonical verification evidence on executable head `d6d97c7353f6d5694dba73ab840ae3a2548dd593`:

```text
workflow run        = 34700750330
power balance max   = 3.0808688933348094e-14
solver iterations   = 11
positive-load sign  = PASS
```

No electrical parameter is calibrated against Phase-1 coupled outcomes.

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
role                = immutable transportation-network benchmark
depot node          = 1 [P]
repair/FCS node     = 10 [P]
closure             = 9->10 and 10->9 [P]
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
published total OD  = 360600
state               = RAW_HASHED
```

Canonical schema/identity evidence:

```text
nodes          = 24
links          = 76
OD zones       = 24
OD total       = 360600
BPR alpha      = 0.15
BPR beta       = 4
9->10 present  = yes
10->9 present  = yes
```

Canonical numerical verification after the audited BFW amendment:

```text
workflow run         = 34700750330
executable code SHA  = d6d97c7353f6d5694dba73ab840ae3a2548dd593
solver               = biconjugate-frank-wolfe
iterations           = 645
relative gap         = 9.33748496131895e-07
criterion            = <= 1e-6 within 5000 iterations
scaled node residual = 1.715075976720996e-16
verdict               = PASS
```

The prior CFW failure (`RG=4.215612504228978e-06`) remains archived in `PHASE1_VERIFICATION_EXECUTION_RESULTS_V1.md`; the frozen convergence criterion was not relaxed.

The entire OD table remains admissible; no OD pair was removed in response to model outputs.

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
workflow            = .github/workflows/phase1-acn-acquisition.yml
```

Executed access evidence:

```text
workflow run ID     = 34698786730
head SHA            = c509d7de85627dda9f99023aa8acb5b24737cc9d
lock verification   = PASS
credential-presence = FAIL / ACN_API_TOKEN unavailable
raw acquisition     = SKIPPED
raw SHA-256         = UNRESOLVED
state               = BLOCKED_EXTERNAL_CREDENTIAL
```

The workflow stopped before requesting or transforming ACN records. Therefore this is an access-state observation, not a data-quality failure.

---

# 4. ACN processing chain and immutable-output requirements

Only after `D-EV-01` exists:

```math
D_{raw}\xrightarrow{T_1}D_{parsed}\xrightarrow{T_2}D_{5min}\xrightarrow{T_3}(\mathcal D_{cal},\mathcal D_{val}).
```

## D-EV-PROC-01 — 5-minute charging trajectory

```text
input               = D-EV-01
transform           = infrastructure-aware replay/aggregation on 5-min grid
output              = P_ch(t)
output SHA-256       = PENDING
state               = DERIVED_PENDING
blocking dependency = D-EV-01
```

## D-EV-SPLIT-01 — chronological split

After frozen QC, sort complete usable days chronologically and define

```math
N_{cal}=\lfloor0.70N_d\rfloor.
```

```text
first N_cal usable days -> D_cal
remaining usable days   -> D_val
calibration-list SHA    = PENDING
validation-list SHA     = PENDING
state                   = DERIVED_PENDING
```

with

```math
\mathcal D_{cal}\cap\mathcal D_{val}=\varnothing.
```

## D-INF-01 — information calibration products

```text
input               = D_cal only
objects             = slot/daytype means, residual distribution, P_ref
hashes              = PENDING
state               = DERIVED_PENDING
```

No `D_val` observation is permitted in those calibration products.

---

# 5. Raw-data preservation policy

Every downloaded/raw object is immutable after first successful acquisition.

```math
\boxed{\text{raw data are never overwritten by processing}.}
```

Canonical chain:

```text
data/raw/<source_id>/<immutable object>
    -> deterministic parser/processor at recorded code SHA
    -> data/processed/<derived_id>/<derived object>
    -> SHA-256 for every derived artifact used by the experiment
```

A reported input must trace either to an immutable upstream commit/blob or to a locally captured raw file with SHA-256.

---

# 6. Synthetic cross-domain mapping provenance

```math
\boxed{P\text{ bus }24\leftrightarrow T\text{ node }10\leftrightarrow\text{Caltech charging forcing}.}
```

```text
mapping type        = preregistered synthetic experimental mapping [A/P]
co-located reality  = NO
geographic claim    = PROHIBITED
version             = Phase-1 v1
```

This mapping tests executable dependency mechanics; it does not assert that the three external sources describe one physical city.

---

# 7. Data-to-model trace

| Data object | Model role | Current integrity state |
|---|---|---|
| `D-PWR-01` | bus/branch physics, bus-24 interface | `RAW_HASHED + PUBLIC VERIFICATION PASS` |
| `D-TRN-01` | link capacities/free times/BPR costs | `RAW_HASHED + PUBLIC VERIFICATION PASS` |
| `D-TRN-02` | full OD forcing | `RAW_HASHED + PUBLIC VERIFICATION PASS` |
| `D-EV-01` | observed charging sessions/time series | `BLOCKED_EXTERNAL_CREDENTIAL` |
| `D-EV-PROC-01` | `P_ch(t)` | `DERIVED_PENDING` |
| `D-EV-SPLIT-01` | `D_cal,D_val` | `DERIVED_PENDING` |
| `D-INF-01` | forecast means/error distribution/`P_ref` | `DERIVED_PENDING` |

---

# 8. Integrity gate

Define

```math
G_D=G_{PWR}G_{TRNnet}G_{TRNod}G_{ACNraw}G_{ACNproc}G_{split}.
```

Current state:

| Gate | State |
|---|---|
| `G_PWR` | `1 / RAW_HASHED` |
| `G_TRNnet` | `1 / RAW_HASHED` |
| `G_TRNod` | `1 / RAW_HASHED` |
| `G_ACNraw` | `0 / BLOCKED_EXTERNAL_CREDENTIAL` |
| `G_ACNproc` | `0 / NOT GENERATED` |
| `G_split` | `0 / NOT GENERATED` |

Therefore

```math
\boxed{G_D=0.}
```

Here `0` means complete Phase-1 data provenance is not yet closed. It does not mean any unavailable ACN data are invalid.

---

# 9. Exact ACN unblock condition

The raw ACN gate closes only when the frozen authenticated workflow records:

```text
record count;
raw byte count;
RAW_SHA256;
acquisition-manifest SHA256;
page/object hashes as implemented;
UTC retrieval time;
acquisition code SHA;
canonical lock SHA;
credential-hygiene PASS.
```

The credential must be supplied only as GitHub Actions secret `ACN_API_TOKEN`; it must never be committed or pasted into chat.

---

# 10. Current permissible claim

```math
\boxed{
\text{public P/T provenance closed and public P/T numerical verification passed}
\land
\text{ACN source identity fixed but materialization credential-blocked}.
}
```

No empirical validation, H1/H2 or Stage-5 claim may use ACN-dependent evidence until the complete data and verification gates close.
