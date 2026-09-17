# H1 Level 2 — Feeder Selection Feature Specification v1.0

**Status:** `PRE-DATA SEMANTICS FROZEN`  
**Frozen:** 2026-09-18  
**Authority:** subordinate to `PROTOCOL_V1.md` and the repository canonical H1/dependency authorities.  
**Purpose:** remove computational degrees of freedom from the outcome-blind feeder-selection vector before any complete feeder feature values are available.

## 1. Scientific rule

The Level-2 selection vector remains

```math
z_f=[N_P,N_T,N_I,P_{\max},L_T,R_T,E_H].
```

These quantities are **case-selection descriptors only**. They are not resilience outcomes, H1 metrics, intervention scores, or evidence that one feeder is more important than another. No `M0/M1/M2` output may enter their construction.

A feeder row is selectable only if all seven values are finite and every eligibility gate below passes. Missing or unqualified values remain missing; no imputation is authorized for case selection.

## 2. Feeder identity and power-node set

A feeder `f` is a feeder directory under

```text
data/open_dss/uhs*_1247/uhs*_1247--*/
```

at frozen GreenEVT commit

```text
6aff1cac48869ccfa0183643979f5f04b04e1124
```

The power-node set is

```math
V_P^f=\{b:\ b\text{ appears in the feeder-level Long_lat_buscoords.txt}\}.
```

Repeated bus identifiers are de-duplicated exactly by identifier. Coordinate parsing failures invalidate the row rather than being discarded silently.

### Feature `N_P`

```math
\boxed{N_P(f)=|V_P^f|.}
```

`N_P` therefore measures feeder electrical-node count, not line count, customer count, or a weighted complexity score.

## 3. Spatial feeder envelope

Each feeder bus longitude/latitude is transformed using the coordinate transformation encoded by the frozen SUMO network. The feeder spatial envelope is the convex hull

```math
H_f=\operatorname{conv}\{(x_b,y_b):b\in V_P^f\}.
```

The convex hull is used because it is deterministic and has no tunable radius/buffer parameter. It is a **selection ROI**, not a claim about utility service territory.

`C_geo=1` only if there are at least three distinct valid coordinate points and `area(H_f)>0`.

## 4. Transport subgraph

Let `E_T` be non-internal SUMO edges that allow passenger-vehicle movement in the frozen `greensboro.net.xml`. The feeder transport edge set is

```math
E_T^f=\{e\in E_T:\operatorname{shape}(e)\cap H_f\neq\varnothing\}.
```

The induced node set is the set of from/to SUMO nodes incident to `E_T^f`.

This rule contains no congestion, demand, hazard, restoration, or model-response information.

### Feature `N_T`

```math
\boxed{N_T(f)=|E_T^f|.}
```

The count is over directed non-internal passenger-road SUMO edges.

### Feature `L_T`

```math
\boxed{L_T(f)=\sum_{e\in E_T^f}\ell_e/1000,}
```

where `ell_e` is SUMO edge length in metres. `L_T` is therefore directed road-edge kilometres. No lane multiplier is applied.

### Feature `R_T`

For structural redundancy only, form a simple undirected projection `G_U^f=(V_U^f,E_U^f)` from `E_T^f`, collapsing direction and parallel duplicates. Let `c_f` be its number of connected components. Define normalized cycle rank

```math
\boxed{
R_T(f)=
\frac{|E_U^f|-|V_U^f|+c_f}{|E_U^f|}
}
```

for `|E_U^f|>0`.

`R_T` is a topology descriptor for selection. It is **not** interpreted as operational resilience, travel-time robustness, accessibility, or recovery performance.

`C_road=1` only if `N_T>0`, `L_T>0`, and `R_T` is finite.

## 5. Cross-domain interface-opportunity count `N_I`

GreenEVT spatially associates electrical buses/parcels with SUMO edges. Level 2 preserves the distinction between such source-derived spatial crosswalks and active causal dependencies.

For feeder `f`, define the set of valid source-derived cross-domain location pairs

```math
I_f=
\{(b,e):b\in V_P^f,\ e=\text{buses.sumo_edge}(b),\ e\in E_T^f\}
\cup
\{(b,e):b\in V_P^f,\ \text{parcels.bus_id}=b,\ e=\text{parcels.sumo_edge},\ e\in E_T^f\}.
```

Duplicates are removed exactly by `(bus_id,sumo_edge)` pair.

### Feature `N_I`

```math
\boxed{N_I(f)=|I_f|.}
```

`N_I` is an **interface-opportunity descriptor**. It does not assert that every pair is a charger, traffic signal, repair dependency, or observed utility interconnection.

For audit, direct bus-edge and parcel-edge pair counts are also reported separately.

`C_interface=1` only if:

1. `UDS.db` passes frozen SHA-256, schema and crosswalk audit;
2. every selected pair references a real edge in the frozen SUMO network;
3. `N_I>0`.

Missing mappings are reported; they are never replaced by nearest-neighbour mappings during feeder selection.

## 6. Peak electrical demand `P_max`

For each `b in V_P^f`, the source value is `buses.max_real_power` in the frozen audited GreenEVT `UDS.db`.

```math
\boxed{
P_{\max}(f)=\sum_{b\in V_P^f} P_{b,\max}^{\rm UDS}.
}
```

The database-native unit is preserved and recorded in the output metadata before interpretation. The extractor may not silently substitute `Loads.dss` snapshot kW, zero, mean load, or another statistic when `max_real_power` is absent.

The row is invalid if feeder-bus matching to the audited UDS table is incomplete or if a required `max_real_power` value is null/non-finite.

## 7. Static flood-exposure descriptor `E_H`

`E_H` is a **pre-simulation selection descriptor**, not the Level-2 HEC-RAS forcing and not a component fragility measure.

The source is the effective FEMA National Flood Hazard Layer (NFHL), which FEMA identifies as the definitive digital effective flood-hazard map source. Only effective Special Flood Hazard Area (`SFHA_TF=true`) geometry is used; preliminary/pending layers are excluded from v1.

Define

```math
e_P(f)=\frac{|\{b\in V_P^f:(x_b,y_b)\in SFHA\}|}{N_P(f)}
```

and

```math
e_T(f)=\frac{\sum_{e\in E_T^f}\ell(e\cap SFHA)}{\sum_{e\in E_T^f}\ell_e}.
```

Then

```math
\boxed{E_H(f)=\tfrac12[e_P(f)+e_T(f)].}
```

The equal weighting is a preregistered **selection scaling convention only**; it is not a statement that power and transport flood consequences are physically equal.

`C_hazard=1` only if the effective NFHL query covers the full feeder envelope sufficiently to distinguish mapped non-SFHA area from missing/unmapped hazard data. Unmapped/unknown is never coded as zero exposure.

Because the primary thesis hazard is a later pluvial HEC-RAS stress test, `E_H` must not be used as a substitute for the HEC-RAS depth/velocity field.

## 8. Computability and eligibility

```math
C_{computable}=1
```

only when every element of `z_f` is finite and its source checks pass.

The final feeder eligibility rule remains

```math
\boxed{
C_{geo}\land C_{road}\land C_{interface}\land C_{hazard}\land C_{computable}=1.
}
```

No minimum/maximum feature threshold is introduced in v1. Eligibility is based on data/geometry validity, not on choosing large, highly coupled, highly flooded, or otherwise interesting cases.

## 9. Selection algorithm boundary

After the complete eligible feature matrix is frozen, `select_feeders.py` performs robust median/MAD standardization and chooses the development medoid followed by the conditional held-out coverage medoid.

The following are forbidden before selection:

- inspecting `M0/M1/M2` outcomes by feeder;
- choosing a feeder for visually interesting topology;
- choosing high-load/high-interface/high-flood feeders manually;
- filling missing features with deterministic defaults;
- changing the feature definitions after seeing selected IDs without a versioned amendment.

## 10. Provenance outputs required per row

In addition to the seven selection values, extraction must record at least:

```text
source_commit
feeder_directory
N_P source count
UDS feeder-bus match fraction
bus-edge valid/missing counts
parcel crosswalk pair count
N_T and L_T
undirected V/E/component counts used for R_T
NFHL effective-data retrieval/version timestamp
NFHL coverage status
e_P and e_T
all input file SHA-256 values used where available
```

A row without this audit metadata may not enter the selector.

## References used for source semantics

- Nilsson, G., Aquino, A. D. O., Coogan, S., & Molzahn, D. K. (2023). *GreenEVT: Greensboro Electric Vehicle Testbed*. GreenEVT source commit frozen above.
- Federal Emergency Management Agency. *National Flood Hazard Layer* guidance: NFHL is the effective digital flood-hazard map source; `S_Fld_Haz_Ar` includes flood-zone and SFHA attributes.

These sources support data/mapping semantics. The feature definitions and selection equations above are thesis methodological choices and are not attributed to those sources as established standards.
