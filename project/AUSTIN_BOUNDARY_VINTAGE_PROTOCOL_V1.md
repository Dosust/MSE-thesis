# Austin Boundary Vintage Protocol v1.0

**Date:** 2026-09-18  
**Case:** `AUS-P5U-2018-V1`  
**Status:** PRIMARY SOURCE FROZEN / RAW GEOMETRY QA OPEN

## 1. Problem

The Austin case combines SMART-DS 2018 with public municipal/utility layers of different vintages. The study boundary must therefore be selected before spatial clipping without using H1--H5 outcomes.

## 2. Primary boundary

The primary municipal support is frozen as the City-hosted layer:

```text
City_of_Austin_full_purpose_boundary / FeatureServer/0
https://services.arcgis.com/0L95CJ0VTaxqcmED/arcgis/rest/services/City_of_Austin_full_purpose_boundary/FeatureServer/0
ArcGIS item: 46a37551e8b64f098f29a2f991df5e9d
last data edit: 2019-04-04
native CRS: EPSG:3857
geometry: polygon
```

This source is preferred for the primary semisynthetic case because:

1. its semantics are explicitly **Austin full purpose boundary**;
2. its 2019 snapshot is temporally closer to SMART-DS 2018 than the continuously edited 2026 jurisdiction layer;
3. it is City-hosted and queryable in JSON/GeoJSON/PBF;
4. using it does not imply that the municipal boundary equals Austin Energy's electric service territory.

The case is still not an exact 2018 historical reconstruction; the one-year boundary-vintage offset is recorded explicitly.

## 3. Sensitivity/cross-check boundaries

Two independent cross-checks are retained:

### Current City jurisdiction

```text
BOUNDARIES_jurisdictions / FeatureServer/0
JURISDICTION_TYPE = FULL
native CRS: EPSG:2277
```

This continuously maintained City layer is used only to quantify whether later annexation/jurisdiction changes materially affect the selected 2018-era spatial support.

### Austin Energy service area

```text
UTILITIESCOMMUNICATION_austin_energy_service_area / FeatureServer/0
```

This utility polygon is a geographic cross-check only. It does **not** reveal actual feeder topology or validate a synthetic SMART-DS-to-signal electrical assignment.

## 4. QA rules

The primary boundary passes only if raw bytes are materialized and hashed and:

```text
geometry type = polygon/multipolygon;
geometry nonempty;
geometry valid or any repair is explicitly logged;
native CRS identity retained in provenance;
derived EPSG:4326 representation agrees topologically after reprojection;
feature count and area are reported;
P5U asset points/lines have feature-level intersection tests;
current-jurisdiction and Austin-Energy cross-check differences are reported.
```

Area must be computed in an appropriate projected CRS, not directly in latitude/longitude.

## 5. Boundary sensitivity

Let `Omega_2019` be the primary full-purpose boundary and `Omega_current` the current full-purpose jurisdiction. Report at minimum:

```math
r_{\Delta\Omega}
=
\frac{\operatorname{Area}(\Omega_{2019}\triangle\Omega_{current})}
{\operatorname{Area}(\Omega_{2019})}.
```

Also report how many retained power assets, signals, radar sensors and road links change membership under the two boundaries. Boundary sensitivity is descriptive and cannot be used to choose the boundary that produces a stronger hypothesis effect.

## 6. Evidence

The City ArcGIS service identifies `City_of_Austin_full_purpose_boundary` as a polygon layer in EPSG:3857 and reports its last edit on 2019-04-04. The current `BOUNDARIES_jurisdictions` layer explicitly codes `FULL` as `FULL PURPOSE`, uses EPSG:2277, and is continuously edited in 2026. These two sources justify the primary-vintage versus current-sensitivity distinction; they do not make the Austin case a historical reconstruction.
