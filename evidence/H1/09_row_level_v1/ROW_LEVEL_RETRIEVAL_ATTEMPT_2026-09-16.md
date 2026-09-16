# H1 Row-Level Retrieval Attempt — 2026-09-16

**Method:** EGMIV  
**Purpose:** attempt activation of the frozen H1 row-level audit without weakening R1–R8 or substituting metadata for raw rows.  
**Decision:** `RAW ROW-LEVEL GATE REMAINS PENDING`.

## 1. Frozen objects respected

The execution used the existing immutable registry and event windows:

- `source_query_registry_v1.csv`
- `event_windows_v1.csv`
- R1–R8 from `project/H1_RAW_COMPLETENESS_AUDIT_V1.md`

Candidate split remains only

```math
D_{train}^{cand}=\{E0,E2\},\qquad
D_{test}^{cand}=\{E1,E3,E4\}.
```

No event was moved between roles and no source was substituted after observing model behavior.

---

## 2. Public endpoint re-verification

### NYISO P-58B — power load

The official NYISO P-58B index remains live and exposes monthly archived ZIP files. The index explicitly lists the required historical months, including July 2020, August 2020, December 2022, December 2023 and April 2024.

The July-2020 archive resolves to the frozen endpoint:

`https://mis.nyiso.com/public/csv/pal/20200701pal_csv.zip`

A direct retrieval was attempted in the active runtime. The web reader resolved the exact archive URL but returned a cache-miss for the binary ZIP; the container download attempt also failed. Therefore archive existence is verified, but row-level bytes were not obtained.

**Decision:** source accessibility metadata `PASS`; R1–R5 row-level audit `NOT EXECUTED`.

### NYC TLC HVFHV — completed OD evidence

The official TLC Trip Record Data portal remains live and publishes monthly High Volume FHV records in Parquet, including all event months required by E0–E4. TLC explicitly states that FHV trip submissions cannot be guaranteed complete or accurate, and its 2020 publication retains the COVID-era submission-extension caveat.

This confirms the frozen semantic restriction:

```math
\text{completed HVFHV trips}\neq\text{all requested OD demand}.
```

The current runtime did not materialize the large event-month Parquet bodies.

**Decision:** archive/schema availability `PASS`; row-level R1–R8 `NOT EXECUTED`.

### NYC DOT Traffic Speeds — road state

The official NYC Open Data dataset `i4gi-tjb9` remains live. Current metadata identifies `data_as_of`, `link_id`, `speed`, `travel_time`, `status`, `borough`, `link_name`, and `link_points`; the dataset is updated frequently and is suitable as link-state telemetry.

The public API endpoint is machine-readable, but the active web reader did not expose arbitrary historical SoQL result bodies as downloadable raw files and direct Python/container network access is unavailable. No historical event-window row count was inferred from current metadata.

**Decision:** schema/API `PASS`; historical event-window row audit `NOT EXECUTED`.

### NYC 311 — obstruction-support evidence

The official `erm2-nwe9` dataset remains live and exposes service-request timestamps, complaint/problem descriptors, status and geography. The source is reporting-driven; absence of a record remains inadmissible as evidence of absence of an obstruction.

No event-window raw extraction was completed in this runtime.

**Decision:** source/schema `PASS`; row-level obstruction audit `NOT EXECUTED`.

### EAGLE-I — power outage

Figshare DOI `10.6084/m9.figshare.24237376` is currently version 3 and covers 2014–2024 at 15-minute county-level resolution. The full item is approximately 9.54 GB. The public version includes the 2024 extension.

The size/distribution prevents complete materialization in the current chat runtime. The frozen missing-row rule remains:

```math
\text{absence of an EAGLE-I county-time row}\not\equiv\text{zero outage}.
```

**Decision:** source/version coverage `PASS`; row-level R1–R8 `NOT EXECUTED`.

---

## 3. What was and was not established

Established in this execution:

```math
\boxed{
\text{official endpoint still live}
+\text{event-month archive existence}
+\text{schema/semantic compatibility rechecked}
}
```

Not established:

```math
\boxed{
N_{rows},\ t_{min},\ t_{max},\ \Delta t\text{ distribution},\
\text{null rates},\ \text{duplicate rate},\ \text{event-window spatial coverage}
}
```

for every required event/source pair.

Therefore metadata-level accessibility is **not** promoted to row-level completeness.

---

## 4. Gate result

```math
\boxed{\textbf{RAW ROW-LEVEL GATE = PENDING}}
```

and

```math
\boxed{D_{train},D_{test}\ \textbf{remain UNFROZEN}.}
```

Consequently the following remain scientifically unauthorized:

- final H1 calibration;
- confirmatory M0/M1/M2 effect-size adjudication;
- empirical `u_obs,P`, `u_obs,T` estimation from these sources;
- `epsilon_pred` calculation;
- H1b predictive-validation claim.

The next valid transition is unchanged:

```math
\text{materialize raw bodies}
\rightarrow
\text{immutable hashes}
\rightarrow
\text{event-window row audit}
\rightarrow
R1\text{--}R8
\rightarrow
\text{freeze train/test}.
```

No synthetic or metadata-derived substitute is authorized.
