# H3 Houston Boundary Freeze v1.0

**Status:** SOURCE + DOMAIN SEMANTICS FROZEN / RAW GEOMETRY BYTES BLOCKED  
**Date:** 2026-09-17  
**Protocol:** EGMIV–TSP  
**Case:** `H3-HOU-FLOOD-V1`  
**Thesis destination:** Chapter 4 — H3 case realization/data provenance; supports Chapter 3 Stage 5 service-domain definitions.  
**Upstream authority:** `H3_DEMONSTRATOR_FREEZE_V1.md`, `H3_HOUSTON_DATA_MATERIALIZATION_QA_V1.md`

> This file closes the previously open Houston study-boundary **source and semantics**. It does not claim that the polygon geometry has been downloaded, hashed, dissolved, or area-validated. Raw-byte materialization remains blocked in the current execution environment.

---

## 1. Thesis routing

```math
\boxed{
\text{H3 Houston demonstrator}
\rightarrow
D_{\Omega}
\rightarrow
\text{P/T/signal/flood clipping}
\rightarrow
\text{network/interface QA}
\rightarrow
\text{case-specific }K,G_{rec},F,T_V,T_R.
}
```

Boundary choice matters because every service denominator, network extraction, flood-coverage statistic, and P↔T interface count depends on the same spatial support.

---

## 2. Authoritative primary source

**Authority:** City of Houston / MyCity Houston / COHGIS.  
**Service:** `HoustonMap/Administrative_Boundary`  
**Layer:** `Houston City Limit` (Layer 0)  
**Primary endpoint:**

```text
https://mycity2.houstontx.gov/gisweb01/rest/services/HoustonMap/Administrative_Boundary/MapServer/0
```

The official ArcGIS layer is a polygon feature layer. Its display/semantic field is `SERVICE_TY`; the live renderer exposes the classes `FULL` (Full service) and `LIMITED` (Limited Service). The service supports JSON, GeoJSON and PBF queries. Its published map-service spatial reference is ESRI 102100 / EPSG 3857.

**Secondary official verification endpoint:**

```text
https://geohwp.houstontx.gov/arcgis/rest/services/02_BaseData_Boundaries/COH/FeatureServer/7
```

This official City of Houston feature layer is also named `COH City Limits`, uses `SERVICE_TY`, reports polygon geometry, supports GeoJSON/JSON/PBF, and is published in NAD83 / Texas South Central StatePlane (ESRI 102740 / EPSG 2278). It reports a layer update timestamp of 2022-07-22. The secondary endpoint is used only as an independent City-hosted geometry/attribute consistency check after raw bytes are materialized.

### Source authority qualification

City of Houston Planning and Development states that its GIS division creates and maintains the City's underlying geospatial data and performs annexation-boundary confirmation. COHGIS states that its data are public-domain reference data but should not be relied upon for specific applications without independent verification. Therefore the source is authoritative for the study-domain boundary, while the thesis must still perform independent geometry/CRS/topology QA before analytical use.

```math
\boxed{
G_{\Omega,identity}=1,
\quad
G_{\Omega,authority}=1,
\quad
G_{\Omega,semantics}=1,
\quad
G_{\Omega,query}=1.
}
```

---

## 3. Full-service versus limited-purpose boundary semantics

City of Houston Planning distinguishes:

- **general-purpose/full-service annexation:** property becomes part of the City's general-purpose boundaries and is subject to City regulations, taxes, and services;
- **limited-purpose annexation:** typically implemented through a Strategic Partnership Agreement; the agreement specifies which regulations/services apply and the area does not receive the same general-purpose service obligations.

The City GIS city-limit layer preserves this distinction through `SERVICE_TY = FULL | LIMITED`.

A single dissolved polygon would therefore mix two different municipal-service regimes. For a thesis whose Stage-5 quantities explicitly evaluate **service admissibility and recovery**, that mixing is not acceptable by default.

The following nested spatial objects are now frozen:

```math
\boxed{
\Omega_{\rm legal}
=
\operatorname{dissolve}
\{g:\operatorname{SERVICE\_TY}(g)\in\{FULL,LIMITED\}\},
}
```

```math
\boxed{
\Omega_{\rm core}
=
\operatorname{dissolve}
\{g:\operatorname{SERVICE\_TY}(g)=FULL\},
}
```

```math
\boxed{
\Omega_{\rm limited}
=
\operatorname{dissolve}
\{g:\operatorname{SERVICE\_TY}(g)=LIMITED\}.
}
```

### Primary H3 rule

```math
\boxed{\Omega_{HOU}:=\Omega_{\rm core}}
```

for primary service denominators, asset-in-domain counts, flood-coverage denominator, and P/T/signal clipping.

`Omega_legal` is retained as the legal City-limit envelope and `Omega_limited` is retained as a separate contextual/sensitivity domain. Limited-purpose polygons are **not silently discarded** and are **not silently merged** into the primary service domain.

This is a refinement of the frozen demonstrator phrase “City of Houston municipal polygon,” not a change of geographic case. It makes the spatial support compatible with the thesis's service-based state sets.

---

## 4. Boundary-connector rule

Electrical and roadway graph closure may require nodes/links outside `Omega_core`.

Define

```math
\mathcal V^{boundary}
=\{v\notin\Omega_{core}:v\text{ is minimally required to preserve graph/network boundary conditions}\}.
```

Every such object must carry

```text
is_boundary_connector = 1
in_service_denominator = 0
boundary_reason = documented
```

unless a later case-specific service requirement explicitly says otherwise.

No exterior component may be added merely to improve connectivity statistics or H3 performance.

---

## 5. Frozen raw acquisition contract

Raw acquisition must preserve the City-hosted geometry before any reprojection/dissolve.

### Preferred raw ArcGIS JSON request

```text
BASE = https://mycity2.houstontx.gov/gisweb01/rest/services/HoustonMap/Administrative_Boundary/MapServer/0/query
where=1=1
outFields=*
returnGeometry=true
f=json
```

No `outSR` is requested for the immutable raw object; the server-native spatial reference is retained in the response. Any EPSG:4326 GeoJSON is an **interim/derived** object, not the raw provenance object.

Expected raw path:

```text
data/H3-HOU-FLOOD-V1/raw/boundary/coh_city_limits_raw.json
```

Expected manifest path:

```text
data/H3-HOU-FLOOD-V1/qa/manifests/coh_city_limits_manifest.json
```

Repository stores the acquisition script, manifest/checksum after execution, and QA summary; large raw files remain repository-external unless later repository policy allows them.

---

## 6. Mandatory post-download QA

Raw boundary bytes pass only if all applicable checks succeed:

```math
\boxed{
G_{\Omega,bytes}
\land
G_{\Omega,parse}
\land
G_{\Omega,geom}
\land
G_{\Omega,CRS}
\land
G_{\Omega,class}
\land
G_{\Omega,valid}
\land
G_{\Omega,crosscheck}
=1.
}
```

Required checks:

```text
HTTP response successful and nonempty;
SHA-256 frozen;
ArcGIS JSON parses;
geometry type = polygon;
spatial reference recorded from response;
SERVICE_TY field exists;
all observed SERVICE_TY values enumerated;
FULL class exists;
LIMITED class retained if present;
null/invalid geometry rate reported;
geometry validity tested before and after dissolve;
raw feature count recorded;
FULL/LIMITED feature counts recorded;
legal/core/limited areas computed only in a suitable projected CRS;
secondary City-hosted endpoint cross-check performed;
no silent repair of invalid geometries;
all geometry repairs logged and sensitivity checked if material.
```

The City-hosted source disclaimer requires independent verification; therefore a successful download alone does not close `G_Omega_QA`.

---

## 7. Current execution result

Source and semantic qualification are closed:

```math
\boxed{G_{\Omega,source}=1.}
```

The current container cannot resolve the City of Houston host through direct external DNS, and the browsing tool exposes metadata but not the raw ArcGIS query payload as a downloadable local file. Therefore:

```math
\boxed{
G_{\Omega,bytes}=0,
\qquad
G_{\Omega,QA}=0.
}
```

The following quantities remain intentionally **NOT CLAIMED**:

```text
raw byte size;
SHA-256;
raw feature count;
FULL/LIMITED feature counts;
polygon area;
number of multipart components;
invalid geometry count;
final common analysis CRS;
final clipping artifact.
```

This is a data-access blocker, not a scientific failure.

---

## 8. Exact next admissible action

Run the frozen boundary acquisition script in a network-enabled environment, then freeze:

```math
\boxed{
\text{bytes}
\rightarrow
\text{SHA256}
\rightarrow
\text{native CRS/fields}
\rightarrow
\text{geometry QA}
\rightarrow
\Omega_{legal},\Omega_{core},\Omega_{limited}
\rightarrow
\text{cross-check}
\rightarrow
G_{\Omega,QA}.
}
```

Only after `G_Omega_QA=1` may the power, road, signal, and flood source families be clipped to the primary H3 service domain.

---

## References / authoritative sources

City of Houston Planning and Development Department. (n.d.). *Annexation*. https://www.houstontx.gov/planning/Annexation/

City of Houston. (n.d.). *GIS @ Houston: About GIS / COHGIS*. https://mycity.houstontx.gov/about.html

City of Houston. (n.d.). *Houston City Limit — Administrative Boundary, Layer 0*. https://mycity2.houstontx.gov/gisweb01/rest/services/HoustonMap/Administrative_Boundary/MapServer/0

City of Houston. (n.d.). *COH City Limits — FeatureServer Layer 7*. https://geohwp.houstontx.gov/arcgis/rest/services/02_BaseData_Boundaries/COH/FeatureServer/7
