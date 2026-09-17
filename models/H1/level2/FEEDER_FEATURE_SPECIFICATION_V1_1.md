# H1 Level 2 — Feeder Selection Feature Specification v1.1

**Status:** `VERSIONED SOURCE-SCHEMA AMENDMENT FROZEN BEFORE FEEDER SELECTION`  
**Frozen:** 2026-09-18  
**Supersedes for execution:** `FEEDER_FEATURE_SPECIFICATION_V1.md` sections 5–6 where source-schema assumptions conflict with the exact uploaded GreenEVT data.  
**Unchanged:** all geometry, road, redundancy, hazard-exposure, eligibility, outcome-blindness, and medoid-selection rules unless explicitly amended below.

## 1. Reason for amendment

The exact materialized GreenEVT objects now pass their frozen byte identities:

- `data/UDS.db`: SHA-256 `74efbe9209bb8c7ad160f0966f01349e3c7fc187d3d0afcb3d1ddbfec1202724`;
- `data/sumo_network/greensboro.net.xml`: SHA-256 `f0c4cd672a7fd74a5ec1e23cbdb34c6828895af52c1210ee981ef72c79fd7b06`.

Source audit then established two schema facts that v1 could not know before materialization:

1. `UDS.db.buses` has no `max_real_power` column. It has `active_load` and `reactive_load`.
2. feeder-level `Long_lat_buscoords.txt` identifiers are GreenEVT bus names (e.g. `udm106`), whereas `parcels.bus_id` references integer `buses.id`.

No `M0/M1/M2` results and no feeder-selection result were used to make this amendment. The amendment is required by source-schema validity, not by desired feeder outcomes.

## 2. Revised selection vector

The v1.1 vector is

```math
\boxed{z_f=[N_P,N_T,N_I,P_0,L_T,R_T,E_H]}
```

where `P_0` replaces the unsupported `P_max` symbol.

## 3. Canonical feeder bus identity

For feeder `f`, the power-node set remains the bus-name set from feeder-level `Long_lat_buscoords.txt`:

```math
V_P^f=\{b_{name}:b_{name}\text{ appears in feeder-level Long_lat_buscoords.txt}\}.
```

The exact uploaded source establishes:

- 153,850 feeder bus-name rows across the 61 feeder directories;
- 153,850 unique bus names;
- zero duplicate `buses.bus` values in `UDS.db`;
- 153,850/153,850 exact matches from feeder bus name to `UDS.db.buses.bus`.

Therefore the canonical database join is

```text
Long_lat bus name
-> buses.bus
-> buses.id
-> parcels.bus_id
```

No direct comparison between a feeder bus name and integer `buses.id` is permitted.

## 4. Revised interface-opportunity feature `N_I`

Let `id(b)` denote the unique integer `buses.id` obtained from exact equality `buses.bus=b`.

Define

```math
I_f^{bus}=\{(b,e): b\in V_P^f,\ e=\text{buses.sumo_edge where buses.bus}=b,\ e\in E_T^f\}
```

and

```math
I_f^{parcel}=\{(b,e): b\in V_P^f,\ \text{parcels.bus_id}=id(b),\ e=\text{parcels.sumo_edge},\ e\in E_T^f\}.
```

Then

```math
\boxed{N_I(f)=|I_f^{bus}\cup I_f^{parcel}|.}
```

Pairs are deduplicated by canonical `(bus_name, sumo_edge)`.

This remains an interface-opportunity descriptor only. It does not make an observed utility-wiring claim.

## 5. Revised electrical-size feature `P_0`

For exact GreenEVT feeder buses, use the source baseline active load:

```math
\boxed{P_0(f)=\sum_{b\in V_P^f}P^{UDS}_{b,0}}
```

with

```text
P^{UDS}_{b,0} = buses.active_load
unit = kW
```

The kW interpretation is source-validated, not assumed: across all 61 feeders, the sum of `UDS.db.buses.active_load` matches the sum of `kW=` values in the corresponding feeder `Loads_original.dss` for all 61/61 feeders, with maximum absolute discrepancy below `5e-11 kW` from floating-point summation.

The 61-feeder aggregate is approximately

```text
627,267.32913 kW
```

`P_0` is therefore a baseline electrical-demand/size descriptor for case selection. It is not feeder capacity, thermal rating, peak-over-time demand, or a resilience metric.

`Loads.dss` may not be substituted because the uploaded GreenEVT package contains EV-modified working loads in that file; the baseline check is against `Loads_original.dss`.

## 6. Eligibility consequence

The v1 computability rule becomes

```math
C_{computable}=1
```

only when every element of

```math
[N_P,N_T,N_I,P_0,L_T,R_T,E_H]
```

is finite and all corresponding source/coverage gates pass.

A feeder with `N_I=0` remains explicitly evaluated but fails `C_interface`; it is not deleted from the 61-row audit matrix.

## 7. Anti-bias rule

The following remain prohibited:

- choosing or rejecting feeders because of `M0/M1/M2` outcomes;
- changing `P_0`, `N_I`, or any other feature after inspecting selected feeder identities without another versioned amendment;
- treating missing flood coverage as zero exposure;
- manually promoting an ineligible feeder.

## 8. Provenance authority

The machine-verifiable source audit is:

```text
artifacts/uploaded_source_audit_v1.json
```

This amendment changes only source-schema interpretation required to make the predeclared outcome-blind selection procedure executable against the exact GreenEVT source.
