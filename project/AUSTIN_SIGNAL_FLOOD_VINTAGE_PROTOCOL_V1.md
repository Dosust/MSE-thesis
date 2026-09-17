# Austin Signal and Flood Temporal-Semantics Protocol v1

**Status:** PRE-DATA FREEZE — source semantics fixed; feature-level execution remains open.  
**Date:** 2026-09-18  
**Case:** `AUS-P5U-2018-V1`

## 1. Purpose

Prevent current Austin GIS layers from being misrepresented as 2018 event truth in the 2018 SMART-DS case.

## 2. Traffic-signal source

Primary source identity:

- City of Austin `TRANSPORTATION_signals2/FeatureServer/0`
- maintained by Austin Transportation Department / Arterial Management Division;
- updated daily;
- source CRS EPSG:2277;
- role: **current signal-location evidence and semisynthetic P→T mapping support**.

### Frozen rule

The current signal layer is **not** an archival 2018 signal inventory unless an independent installation/vintage attribute or archival source proves that an individual signal existed in 2018.

Therefore:

```text
current signal point + SMART-DS bus proximity
    -> permissible semisynthetic interface candidate
    != verified historical 2018 feeder-to-signal dependency.
```

No signal may be presented as an actual Austin Energy feeder assignment.

## 3. Flood source

Primary flood source:

- City of Austin / FEMA Floodplain layer;
- polygon geometry;
- source CRS EPSG:2277;
- attributes include `FLOOD_ZONE` and `EFFECTIVE_DATE`;
- role: **static hazard/exposure support**.

### Frozen rule

A FEMA flood-zone polygon supports statements such as:

```text
asset lies inside/outside a declared mapped flood-hazard zone.
```

It does **not** by itself support:

```text
flood depth at time t;
road closure at time t;
component failure probability at time t;
repair delay;
hazard duration;
water velocity.
```

Those quantities require a separately qualified event/hydraulic/fragility/passability model.

## 4. Temporal admissibility

For a 2018 case:

- flood features may be used only with their `EFFECTIVE_DATE` recorded;
- if a feature's effective date postdates the intended historical state, it must be labeled `RETROSPECTIVE_STATIC_HAZARD_REFERENCE` unless an archival FEMA/FIRM source establishes applicability to 2018;
- current traffic-signal points must be labeled `CURRENT_ASSET_LOCATION_REFERENCE` unless 2018 existence is independently established.

## 5. P→T mapping semantics

The default admissible mapping is thesis-derived and semisynthetic:

```math
\mathcal M_{P\to T}^{sig}: s_j \mapsto b_i
```

where `s_j` is a retained City signal location and `b_i` is an eligible SMART-DS synthetic bus/component under a declared spatial/engineering mapping rule.

Required metadata:

```text
signal source/vintage;
power source/vintage;
CRS transformation;
mapping rule;
maximum mapping distance/tolerance;
ambiguity/tie rule;
backup-power assumption;
uncertainty class;
statement that the assignment is semisynthetic.
```

The mapping cannot be called empirical feeder truth.

## 6. Flood-to-network semantics

Flood remains a common-cause pathway:

```math
\eta_F\to P,
\qquad
\eta_F\to T,
```

not a P↔T dependency.

A dynamic failure/passability law may be introduced later only as a separately sourced model:

```math
P(\text{failure/passability}\mid h,t,\theta_F).
```

## 7. Final gates

Signal gate may pass only if:

1. raw signal features are materialized and hashed;
2. current-vs-2018 temporal semantics are explicit;
3. retained points overlap the frozen case support;
4. the semisynthetic mapping is reproducible and uncertainty-aware;
5. no actual feeder assignment is claimed.

Flood gate may pass only if:

1. raw polygons are materialized and hashed;
2. `FLOOD_ZONE` and `EFFECTIVE_DATE` are retained;
3. overlap with retained assets is executed;
4. static exposure is kept distinct from dynamic hazard intensity;
5. any failure/passability function is separately qualified.

## 8. Current state

```text
Signal source identity: PASS
Signal temporal semantics: PASS
Signal raw materialization: OPEN
2018 signal existence evidence: OPEN / not required for semisynthetic current-reference mapping if labeled correctly
P→T mapping: OPEN
Flood source identity: PASS
Flood static-hazard semantics: PASS
Flood raw materialization: OPEN
Flood effective-date audit: OPEN
Dynamic flood model: OPEN
Final signal/flood admissibility: NOT YET PASS
```

## 9. Evidence anchors

- Austin signal service: https://services.arcgis.com/0L95CJ0VTaxqcmED/ArcGIS/rest/services/TRANSPORTATION_signals2/FeatureServer
- Austin/FEMA flood layer: https://maps.austintexas.gov/gis/rest/Shared/Floodplain/MapServer/1
