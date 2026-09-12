# Phase 1A — Data Manifest v1

![Status](https://img.shields.io/badge/status-DATA%20LOCK%20v1.0-0969DA)
![Phase](https://img.shields.io/badge/phase-1A-1A7F37)

**Frozen:** 2026-09-12  
**Authority:** `PHASE1_EXPERIMENT_SPECIFICATION_V1.md` + `PHASE1_EMPIRICAL_VALIDATION_PROTOCOL.md`  
**Purpose:** freeze the external benchmark/data identity, provenance, transformations, inclusion/exclusion rules, and integrity controls used by the Phase-1 Power–Transportation executable demonstrator before confirmatory execution.  
**Scope:** data lock only; software versions and numerical implementation are frozen separately in `PHASE1_SOFTWARE_ENVIRONMENT_LOCK_V1.md`.

---

## 0. Governing evidence discipline

The thesis reasoning sequence remains

```math
\text{LEARN}\rightarrow\text{VERIFY}\rightarrow\text{FORMULATE}\rightarrow\text{DERIVE}\rightarrow\text{TEST}\rightarrow\text{VALIDATE}\rightarrow\text{SYNTHESIZE}\rightarrow\text{ADVANCE}.
```

For data provenance, the operational chain is

```math
\boxed{
\text{source}
\rightarrow
\text{immutable raw object}
\rightarrow
\text{documented transformation}
\rightarrow
\text{derived model input}
\rightarrow
\text{experiment}.
}
```

Claim tags:

```text
[E] externally established benchmark/data fact;
[P] preregistered thesis choice;
[D] derived transformation/rationale;
[A] explicit assumption;
[U] unresolved/acquisition-pending item.
```

**Non-negotiable rule:** no source, time window, file, benchmark mapping, filtering rule, or transformation may be silently changed after confirmatory results are inspected. A substantive change requires a new manifest version.

---

# 1. Data-lock status

The Phase-1 source identities are now frozen.

```text
POWER BENCHMARK       LOCKED
TRANSPORT NETWORK     LOCKED
TRANSPORT OD MATRIX   LOCKED
ACN SOURCE/WINDOW     LOCKED
ACN RAW EXPORT HASH   PENDING ACQUISITION
DERIVED ACN HASHES    PENDING ACQUISITION/PROCESSING
```

Therefore:

```math
\boxed{
\text{benchmark identity locked}
\neq
\text{all raw data physically acquired and hashed}.
}
```

Confirmatory execution remains **blocked** until every entry marked `BLOCKING-PENDING` below is resolved and recorded without changing the preregistered source/window.

---

# 2. Source registry

## D-PWR-01 — Baran–Wu / MATPOWER 33-bus distribution benchmark `[E]`

| Field | Frozen value |
|---|---|
| Source repository | `MATPOWER/matpower` |
| Repository commit | `2e0ef79a6c4526858ee923491d92781ad4507fb7` |
| Source path | `data/case33bw.m` |
| Git blob SHA | `97e510bee25c543de0453959672fe86b40a999c8` |
| Case format | MATPOWER case format v2 |
| Base MVA | `10 MVA` |
| Base voltage | `12.66 kV` |
| Charging-interface bus | bus `24` `[P]` |
| Controlled fault branch | `23 -> 24` `[P]` |
| Primary fields used | bus `Pd,Qd,Vmax,Vmin`; branch `r,x,status`; network topology |
| Calibration permitted? | **No** for benchmark electrical parameters |
| Integrity status | **LOCKED** by immutable Git commit + blob SHA |

The source file cites Baran & Wu (1989) and converts branch impedances from ohms to per-unit and loads from kW/kVAr to MW/MVAr inside the case definition.

### Required transformation `[D/P]`

The benchmark remains unchanged except for the declared charging injection at bus 24:

```math
p_{24}(t)=p_{24}^{base}+P_{ch}(t).
```

The controlled branch outage changes only the declared branch state for `23 -> 24` during the restoration experiment.

### Prohibited transformations

```text
- no impedance tuning;
- no benchmark load tuning to improve coupled results;
- no bus remapping after results are viewed;
- no alternative feeder substituted inside v1.
```

---

## D-TRN-01 — Sioux Falls network `[E]`

| Field | Frozen value |
|---|---|
| Source repository | `bstabler/TransportationNetworks` |
| Repository commit | `d1639b4ef218c17928ba573e806ddf8ba5e7ae6d` |
| Source path | `SiouxFalls/SiouxFalls_net.tntp` |
| Git blob SHA | `66d0eca4ddcfb82f861bea040060deab7a741b2f` |
| Nodes | `24` |
| Directed links | `76` |
| BPR coefficient | `B_a = 0.15` |
| BPR exponent | `beta_a = 4` |
| Depot node | `1` `[P]` |
| Charging/repair access node | `10` `[P]` |
| Controlled road closure | `(9,10)` and `(10,9)` `[P]` |
| Primary fields used | init node, terminal node, capacity, free-flow time, B, power |
| Calibration permitted? | **No** for published benchmark link parameters |
| Integrity status | **LOCKED** by immutable Git commit + blob SHA |

The frozen link-time function is

```math
t_a(x_a)=t_a^0\left[1+B_a\left(\frac{x_a}{c_a}\right)^{\beta_a}\right].
```

No roadway parameter is retuned to reproduce a desired restoration effect.

---

## D-TRN-02 — Sioux Falls OD demand matrix `[E]`

| Field | Frozen value |
|---|---|
| Source repository | `bstabler/TransportationNetworks` |
| Repository commit | `d1639b4ef218c17928ba573e806ddf8ba5e7ae6d` |
| Source path | `SiouxFalls/SiouxFalls_trips.tntp` |
| Git blob SHA | `db70eda57738877811e9ac07c25a567973d3b6a0` |
| Zones | `24` |
| Published total OD flow | `360600` demand units |
| Primary use | baseline user-equilibrium assignment and resulting link travel times |
| Calibration permitted? | **No** |
| Integrity status | **LOCKED** by immutable Git commit + blob SHA |

The entire published OD matrix is used. No OD pair is removed because it produces an inconvenient route or congestion result.

---

## D-EV-01 — Caltech ACN charging sessions `[E/P]`

| Field | Frozen value |
|---|---|
| Data family | ACN-Data / Caltech Adaptive Charging Network |
| Site | `caltech` |
| Start | `2019-10-10 00:00:00 America/Los_Angeles` |
| End | `2019-12-31 23:59:59 America/Los_Angeles` |
| Exchange interval | `5 min` `[P]` |
| Required session fields | session/station identity, connection time, disconnect time, delivered energy; time-series current/pilot information required by the replay pipeline |
| Intended executable layer | ACN-Sim replay using the Caltech infrastructure definition |
| Raw immutable export | **BLOCKING-PENDING** |
| Exact client/API version | **BLOCKING-PENDING software lock** |
| SHA-256 of raw export | **BLOCKING-PENDING** |
| Calibration/validation split | chronological 70/30 after frozen quality filtering |

### Why the window is frozen `[D]`

The Phase-1 experiment specification selected the post-10-October-2019 period to avoid the documented legacy timezone issue in earlier ACN web-interface records. The source/window may not be changed because another interval gives a more favorable result.

### Acquisition rule `[P]`

The first successful reproducible extraction must be written to an immutable raw file and accompanied by:

```text
- extraction timestamp in UTC;
- exact query/site/window;
- API/client package + version;
- record count;
- byte size;
- SHA-256 hash;
- field/schema snapshot;
- acquisition script commit SHA.
```

If the frozen source/window cannot be acquired reproducibly, Phase 1 v1 is **blocked**. A different charging dataset requires `PHASE1_DATA_MANIFEST_V2.md`; it may not be substituted silently.

---

# 3. Raw-data preservation policy

For every acquired external dataset:

```math
\boxed{
\text{raw file is immutable}.
}
```

Raw objects must be stored separately from processed objects. Processing scripts read raw data and write new derived files; they never overwrite raw data.

Minimum naming rule:

```text
data/raw/<source_id>/<immutable_source_file>
data/processed/<derived_id>/<derived_file>
```

Every file used in a reported result must be traceable to either:

```text
1. immutable upstream commit + Git blob SHA; or
2. locally captured immutable file + SHA-256.
```

A Git blob SHA is recorded as repository provenance; SHA-256 is required for downloaded/generated local data artifacts.

---

# 4. ACN quality-control and completeness rule `[P]`

A calendar day enters the usable ACN set only if:

```text
1. all required timestamps parse in America/Los_Angeles;
2. every used session satisfies connect_time < disconnect_time;
3. delivered energy is finite and nonnegative;
4. station/session identifiers required for replay are present;
5. no active-session time-series corruption prevents the declared replay/reconstruction;
6. the aggregation procedure can generate the full 288-slot 5-minute daily grid.
```

A 5-minute interval with **no active charging demand** is assigned zero demand and is not treated as missing data.

A day with an active session whose required replay information is missing/corrupt is excluded **before** the chronological calibration/validation split and logged with an exclusion reason.

No exclusion may be based on model prediction error or coupled-system outcome.

---

# 5. Derived-data objects

## D-EV-PROC-01 — Aggregate charging trajectory `[D/P]`

The executable charging trajectory is generated on the frozen 5-minute grid from the acquired ACN sessions through the locked ACN-Sim infrastructure/replay pipeline.

```math
P_{ch}(t_k)=\sum_{n\in\mathcal N_{active}(t_k)}P_n(t_k).
```

**Important:** raw current values are not converted to power with an invented universal voltage. Site power is obtained through the infrastructure-aware executable replay/configuration. This avoids silently imposing an unsupported electrical conversion.

Required processed-artifact record:

```text
file name;
row count;
start/end timestamps;
units;
processing-code commit;
software environment ID;
SHA-256.
```

Status: `BLOCKING-PENDING` until acquisition + software lock are complete.

---

## D-EV-SPLIT-01 — Calibration/validation partition `[P]`

After the frozen completeness filter, sort usable complete days chronologically.

Let `N_d` be the resulting number of days and

```math
N_{cal}=\lfloor0.70N_d\rfloor.
```

Then

```math
\mathcal D_{cal}=\{\text{first }N_{cal}\text{ usable days}\},
```

```math
\mathcal D_{val}=\{\text{remaining usable days}\}.
```

with

```math
\mathcal D_{cal}\cap\mathcal D_{val}=\varnothing.
```

The exact list of dates and its SHA-256 must be frozen immediately after data QC and before any holdout metric is inspected.

---

## D-INF-01 — Information calibration products `[D/P]`

Only `D_cal` may produce:

```math
\mu_{weekday/weekend,s},
```

```math
\varepsilon_I(t)=P_{ch}(t)-\widehat P_{ch}(t),
```

and the empirical calibration residual distribution used for information-degradation experiments.

Also define

```math
P_{ref}=\operatorname{median}_{t\in D_{cal}}P_{ch}(t).
```

These products are **derived calibration objects**, not external measurements and not permitted to use `D_val`.

Each derived object must receive its own SHA-256 and processing-code commit.

---

# 6. Power/transport transformation rules

## 6.1 Power `[E/D]`

Use the values and conversions implemented by the frozen `case33bw.m` source. The experiment must not separately reinterpret the source units inconsistently with MATPOWER.

The only Phase-1 transformation is the explicit added charging load and declared branch status event.

## 6.2 Transportation `[E/D]`

Read capacities and free-flow times directly from `SiouxFalls_net.tntp`; read the full OD matrix from `SiouxFalls_trips.tntp`.

The baseline user-equilibrium solution is a **derived numerical object** and therefore must record solver/environment version, convergence result and output hash when produced.

The road closure changes only the two preregistered directed arcs `(9,10)` and `(10,9)`.

---

# 7. Synthetic cross-domain mapping `[A/P]`

The experiment maps

```math
\boxed{
P\text{ bus }24
\leftrightarrow
T\text{ node }10
\leftrightarrow
\text{Caltech ACN forcing}.
}
```

This is a controlled **synthetic experimental mapping**, not an observed geographic relation.

Therefore the data manifest explicitly prohibits claims that these sources describe one physical city or one real utility/transport system.

The mapping is fixed for v1 and may not be relocated after viewing results.

---

# 8. Data-to-model variable map

| Data object | Raw/derived field | Model variable | Unit/status |
|---|---|---|---|
| D-PWR-01 | `Pd,Qd` | `p_j,q_j` | MW, MVAr after source conversion |
| D-PWR-01 | branch `r,x,status` | branch-flow parameters/state | per-unit after source conversion |
| D-PWR-01 | bus 24 | receiving charging-load interface | fixed mapping `[P]` |
| D-TRN-01 | capacity | `c_a` | benchmark demand/time convention |
| D-TRN-01 | free-flow time | `t_a^0` | benchmark time units |
| D-TRN-01 | `B,power` | `B_a,beta_a` | dimensionless |
| D-TRN-02 | OD demand | `q_{od}` | benchmark demand units |
| D-EV-01 | session timing + replay traces | active charging sessions | observed forcing |
| D-EV-PROC-01 | aggregate replay power | `P_ch(t)` | kW/MW after explicit conversion record |
| D-INF-01 | slot means | `hat P_ch(t)` | same power unit as `P_ch` |
| D-INF-01 | residual empirical distribution | `epsilon_I` | same power unit as `P_ch` |

Any additional data-to-model mapping added later requires a versioned amendment.

---

# 9. Leakage-prevention rules

The following are prohibited:

```text
- using D_val to choose forecast structure;
- using D_val to change latency levels;
- using D_val to choose the feeder bus or road node;
- tuning benchmark impedances/capacities against coupled outcomes;
- deleting validation days because model error is large;
- using Stage-5 viability outcomes to select Phase-1 data;
- replacing the fixed dataset after seeing H1/H2 results.
```

Once `D_val` is opened, any substantive model/data change creates a new experiment version and new independent holdout requirement.

---

# 10. Integrity ledger

| ID | Immutable identity available now? | Local SHA-256 available now? | Blocking? |
|---|---:|---:|---:|
| D-PWR-01 | yes — commit + blob SHA | not required yet for repository source; required if downloaded | no |
| D-TRN-01 | yes — commit + blob SHA | not required yet for repository source; required if downloaded | no |
| D-TRN-02 | yes — commit + blob SHA | not required yet for repository source; required if downloaded | no |
| D-EV-01 | source/window yes | **no** | **yes** |
| D-EV-PROC-01 | no — not generated | **no** | **yes** |
| D-EV-SPLIT-01 | no — not generated | **no** | **yes** |
| D-INF-01 | no — not generated | **no** | **yes** |

This table must be updated only with acquisition/processing metadata; changing any frozen source identity requires v2.

---

# 11. Data-release gate

The data layer is released for executable model verification only when all conditions hold:

```math
\boxed{
G_D
=
G_{source}
\land G_{integrity}
\land G_{QC}
\land G_{split}
\land G_{provenance}.
}
```

where:

```text
G_source      = all frozen sources acquired/resolvable;
G_integrity   = immutable identifiers/hashes recorded;
G_QC          = preregistered quality rules executed and logged;
G_split       = calibration/validation date lists frozen;
G_provenance  = processing-code/environment references recorded.
```

Current status:

```text
G_source      = PARTIAL
G_integrity   = PARTIAL
G_QC          = PENDING
G_split       = PENDING
G_provenance  = PARTIAL

PHASE-1 DATA RELEASE = NOT YET AUTHORIZED.
```

---

# 12. References / provenance anchors

- Baran, M. E., & Wu, F. F. (1989). *Network reconfiguration in distribution systems for loss reduction and load balancing*. IEEE Transactions on Power Delivery, 4(2), 1401–1407. DOI: 10.1109/61.25627.
- MATPOWER `case33bw.m`, repository `MATPOWER/matpower`, frozen commit `2e0ef79a6c4526858ee923491d92781ad4507fb7`.
- TransportationNetworks Sioux Falls TNTP files, repository `bstabler/TransportationNetworks`, frozen commit `d1639b4ef218c17928ba573e806ddf8ba5e7ae6d`.
- LeBlanc, L. J., Morlok, E. K., & Pierskalla, W. P. (1975). *An efficient approach to solving the road network equilibrium traffic assignment problem*. Transportation Research.
- Lee, Z. J., Li, T., & Low, S. H. (2019). ACN-Data: analysis and applications of an open EV charging dataset.
- Lee et al. (2021). ACN-Sim: data-driven simulation of electric vehicle charging networks.
- `PHASE1_EXPERIMENT_SPECIFICATION_V1.md` is authoritative for the frozen experimental mapping/window; this manifest is authoritative for data provenance/integrity.