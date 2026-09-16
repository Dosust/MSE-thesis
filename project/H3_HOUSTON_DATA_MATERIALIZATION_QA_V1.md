# H3 Houston Data Materialization and QA v1.0

**Status:** SOURCE FAMILIES QUALIFIED / RAW BYTES NOT YET FROZEN  
**Date:** 2026-09-17  
**Protocol:** EGMIV–TSP  
**Case:** `H3-HOU-FLOOD-V1`  
**Authority:** `H3_DEMONSTRATOR_FREEZE_V1.md`, `H3_THRESHOLD_EVIDENCE_QUALIFICATION_V7.md`, `H3_UNCERTAINTY_AND_PROBABILITY_SPECIFICATION_V1.md`  
**Thesis destination:** Chapter 4 — H3 experimental realization and data/provenance; supports Chapter 3 Stage 5 definitions.

> This file converts the frozen Houston demonstrator into a reproducible data-acquisition and QA specification. It does not assert that the raw data have already been downloaded, clipped, hashed, or validated. H3 execution remains blocked until the materialized files and QA outputs are frozen.

---

## 1. Objective

The immediate task is

```math
\boxed{
\text{source qualification}
\rightarrow
\text{raw-byte materialization}
\rightarrow
\text{hash/provenance freeze}
\rightarrow
\text{spatial QA}
\rightarrow
\text{network/interface QA}
\rightarrow
\text{case-specific H3 registry}.
}
```

The required source families are:

```math
\boxed{
\mathcal D_{H3}
=
\{D_P,D_T,D_S,D_F,D_{\Omega}\},
}
```

where

```text
D_P      = synthetic power-network and load data;
D_T      = roadway/network/traffic-demand data;
D_S      = traffic-signal locations/assets;
D_F      = Harvey flood inundation/depth field;
D_Omega  = Houston study-domain polygon and boundary metadata.
```

---

## 2. Source qualification result

### 2.1 Power data — Texas combined T&D / SMART-DS

**Qualified source:** Texas Combined Transmission–Distribution Test Case and SMART-DS v0.9 distribution data.

Official repository page:
`https://electricgrids.engr.tamu.edu/texas7k-td/`

OEDI S3 explorer:
`https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=SMART-DS/v0.9/`

Public S3 root:

```text
s3://oedi-data-lake/SMART-DS/v0.9/
```

The official Texas combined-case page states that the case is synthetic/fictitious on the geographic footprint of Texas and that the distribution data include OpenDSS files, time-series load profiles, and geographic coordinates. It also explicitly warns that downloading the full root can involve terabytes of data.

**Research citation:** Mateo, C., Postigo, F., Elgindy, T., Birchfield, A., Duenas, P., Palmintier, B., Panossian, N., Gomez, T., de Cuadra, F., Overbye, T., Safdarian, F., & Wallison, D. (2024). Building and validating a large-scale combined transmission & distribution synthetic electricity system of Texas. *International Journal of Electrical Power & Energy Systems, 159*.

**Acquisition rule:** do not recursively download the entire SMART-DS root. First list the required year/scenario/substation objects, then materialize only substations intersecting the Houston study domain plus required electrical boundary substations.

Canonical listing command:

```bash
aws s3 ls "s3://oedi-data-lake/SMART-DS/v0.9/" --no-sign-request
```

Example official single-substation pattern:

```bash
aws s3 cp \
  "s3://oedi-data-lake/SMART-DS/v0.9/2016/Full_Texas/P1U/scenarios/base_timeseries/opendss/p1uhs0_1247/" \
  ./raw/power/p1uhs0_1247/ \
  --recursive --no-sign-request
```

The exact Houston substation IDs remain **OPEN** until geographic-coordinate metadata are enumerated and intersected with the frozen Houston polygon.

### 2.2 Transportation network — H-GAC

**Qualified source:** H-GAC 2025 Transportation Conformity documentation and roadway network files.

Landing page:
`https://www.h-gac.com/transportation-conformity/2025`

The official page identifies:

```text
Appendix C.1  Travel Model Validation;
Appendix C.2  Links, Miles, Centerline, and Lane Miles Summaries;
Appendix C.3  Link Listing and Capacity Staging;
Appendix C.4  Roadway Network Files.
```

Published/updated dates shown by H-GAC include 2025-08-29 for validation material and 2025-10-22 for the link listing and roadway network files.

Current Appendix C.4 link target observed during qualification:
`https://www.h-gac.com/getmedia/e1498b1d-470d-4df9-92bb-2d55b749f524/C4_Roadway-Network-Files`

H-GAC traffic-data page:
`https://www.h-gac.com/traffic-data`

H-GAC states that regional traffic counts, speeds, and vehicle classifications support travel-demand modeling and analysis.

**Acquisition rule:** materialize the official roadway-network archive and associated link/capacity metadata before deriving graph topology. Do not substitute an arbitrary OSM network for the primary H3 transportation layer unless H-GAC materialization fails and a documented change-control decision is made.

### 2.3 Traffic signals — City of Houston Public Works

**Qualified source:** City of Houston Traffic Management GIS.

Map service:
`https://geogimsms.houstontx.gov/arcgis/rest/services/TDO/Traffic_Management_gx/MapServer`

Traffic-signal layer:
`https://geogimsms.houstontx.gov/arcgis/rest/services/TDO/Traffic_Management_gx/MapServer/26`

The service identifies layer 26 as **Traffic Signal**, a point feature layer in the City of Houston Traffic Management service. The service supports JSON, GeoJSON, and PBF query formats.

A second City of Houston traffic-assets service contains signal cabinets and related signal infrastructure:
`https://geogimstest.houstontx.gov/arcgis/rest/services/TDO/TrafficAssets_fs/FeatureServer`

**Primary H3 rule:** use the official traffic-signal point layer for the P→T interface population. Signal cabinets/battery-backup records may be used only as auxiliary information after explicit field/relationship QA.

**Expected query pattern:** ArcGIS REST `query` with `where=1=1`, selected fields, geometry enabled, output CRS EPSG:4326 or the native CRS recorded explicitly, and paginated retrieval if the service record cap is exceeded.

### 2.4 Harvey flood field — USGS/FEMA

**Qualified source:** USGS Hurricane Harvey flood-inundation data release.

DOI:
`https://doi.org/10.5066/F7VH5N3N`

USGS landing page:
`https://www.usgs.gov/data/data-used-characterize-peak-streamflows-and-flood-inundation-resulting-hurricane-harvey`

San Jacinto River data-catalog record:
`https://data.usgs.gov/datacatalog/data/USGS%3A5aa023ebe4b0b1c392e6881b`

USGS states that the release contains flood-inundation polygons, flood-depth rasters, mapped boundaries, and high-water-mark locations for the August–September 2017 event. The San Jacinto record is directly relevant to Houston and documents creation of the final flood-depth raster and inundation polygon from surveyed high-water marks and water-surface elevation data.

**APA 7 data citation:** Garvin, K. M. (2018). *Inundation layers for the San Jacinto River for the August and September 2017 flood event in Texas* [Data set]. U.S. Geological Survey. https://doi.org/10.5066/F7VH5N3N

**Acquisition rule:** materialize the San Jacinto depth raster, inundation polygon, and metadata first. Add adjacent Harvey sub-basins only if spatial QA shows that the frozen Houston polygon is not adequately covered.

### 2.5 Houston study boundary

The frozen geographic domain is the City of Houston municipal polygon plus only network boundary connectors needed for electrical/transport network closure.

The study-boundary source must be an authoritative City of Houston or equivalent government GIS polygon. Exact file/service endpoint remains **OPEN** and must be fixed before clipping.

---

## 3. Raw-data provenance manifest

For every downloaded object, create one immutable manifest row:

| Field | Required |
|---|---|
| `dataset_id` | unique thesis ID |
| `source_authority` | agency/lab/operator |
| `source_title` | exact dataset title |
| `source_url` | exact download/query endpoint |
| `source_version` | version/release/date where available |
| `access_date_utc` | ISO-8601 |
| `license` | exact license/public-domain statement |
| `raw_filename` | untouched downloaded filename |
| `bytes` | raw byte size |
| `sha256` | SHA-256 of raw file |
| `format` | ZIP/SHP/GPKG/GeoJSON/CSV/TIF/OpenDSS/etc. |
| `native_crs` | EPSG/WKT/native datum |
| `temporal_support` | source time/date range |
| `spatial_support` | source domain/bounds |
| `transformations` | `NONE` for raw object |
| `status` | PASS / BLOCKED / REJECTED |

No processed file may replace the raw file in the provenance manifest.

---

## 4. Folder and immutability structure

Use the following local/repository-external data layout:

```text
data/H3-HOU-FLOOD-V1/
  raw/
    power/
    transport/
    signals/
    flood/
    boundary/
  interim/
    power_houston/
    transport_houston/
    signals_houston/
    flood_houston/
  processed/
    spatial_common/
    graph_power/
    graph_transport/
    interfaces_PT/
  qa/
    manifests/
    crs/
    topology/
    interfaces/
    coverage/
```

`raw/` is immutable after hash freeze. All clipping, reprojection, cleaning, snapping, graph construction, and interface generation occur in `interim/` or `processed/`.

Large raw datasets should not be committed to GitHub unless repository policy explicitly allows it. GitHub stores manifests, scripts, checksums, QA summaries, and small reproducibility artifacts.

---

## 5. Spatial reference policy

Each source retains its native CRS in `raw/`. Reprojection occurs only after native CRS is recorded.

The common analysis CRS must satisfy:

```math
G_{CRS}
=
G_{metric}\land G_{Houston}\land G_{datum}\land G_{raster}.
```

Required properties:

```text
projected coordinate system suitable for Houston-scale metric distance/area calculations;
explicit horizontal datum;
known units;
compatible raster/vector transformation path;
no silent on-the-fly reprojection in confirmatory processing.
```

The final common CRS is **OPEN** until the native H-GAC, City of Houston, SMART-DS, USGS raster, and municipal-boundary metadata are inspected together. It must not be selected by preference alone.

---

## 6. Materialization QA gates

### 6.1 Byte-level integrity

For each raw file `f`:

```math
\boxed{
h_f=\operatorname{SHA256}(f).
}
```

PASS if:

```text
file opens/parses;
byte size > 0;
archive integrity test passes where applicable;
SHA-256 recorded;
source endpoint/version/date recorded.
```

### 6.2 CRS and geometry QA

For every vector/raster:

```text
CRS present and parseable;
coordinate bounds plausible for source domain;
geometry type matches source specification;
invalid geometry rate reported;
null-coordinate rate reported;
reprojection round-trip checked on a sample;
raster nodata value and cell size recorded.
```

### 6.3 Houston coverage QA

For dataset `d`, define

```math
C_d
=
\frac{\mu(\Omega_{HOU}\cap\Omega_d)}{\mu(\Omega_{HOU})}.
```

For areal datasets, report `C_d`. For point/network datasets report counts inside Houston, counts intersecting the boundary buffer, and unmatched/out-of-domain records.

No universal acceptable `C_d` is frozen now; adequacy must be judged against the H3 service/interface domain and documented before execution.

---

## 7. Power-network QA

After Houston extraction, record:

```math
N_P=|\mathcal V_P|,
\qquad
M_P=|\mathcal E_P|.
```

Required tests:

```text
all retained buses/nodes have coordinates;
all retained lines/transformers reference existing endpoints;
no unintended duplicate IDs;
connected-component count reported;
isolated load nodes reported;
radial/meshed structure reported by circuit;
OpenDSS parse/compile status recorded;
baseline power-flow convergence recorded;
served-load denominator used by S_P reproducible;
boundary-node inclusion rule audited.
```

If a retained circuit does not compile or baseline load flow does not converge, it cannot enter confirmatory H3 until corrected through source-supported processing or rejected.

---

## 8. Transportation-network QA

After Houston extraction, record:

```math
N_T=|\mathcal V_T|,
\qquad
M_T=|\mathcal E_T|.
```

Required tests:

```text
link-node endpoint consistency;
network connected-component structure;
one-way/direction fields preserved where available;
length, capacity, lanes, free-flow speed and functional-class completeness reported;
zero/negative length or capacity records rejected/flagged;
centroid/connectors distinguished from physical roadway links;
OD/service-demand support documented;
baseline assignment or travel-time calculation reproducible.
```

The transportation graph must preserve the semantics required by `S_T`; a visually connected road map is insufficient.

---

## 9. Flood-field QA

For the USGS raster/polygon:

```text
raster CRS, cell size, extent, nodata and units recorded;
negative depth values rejected/flagged;
depth distribution summarized over Houston overlap;
inundation polygon/raster overlap checked;
Houston coverage fraction reported;
spatial alignment with P/T coordinates verified;
no extrapolation outside mapped flood extent unless explicitly modeled as an assumption.
```

Define the observed stress field only on supported cells:

```math
\eta_F(x)
=
d_F(x)
```

for valid USGS flood-depth cells. Missing/out-of-coverage cells are **not automatically zero flood depth**; missingness and zero must be distinguished.

---

## 10. P→T interface QA — signal electricity dependency

Let `S` be the retained Houston traffic-signal set.

For each signal `s\in S`, construct a reproducible nearest/feasible synthetic power-source mapping only after both coordinate systems pass QA:

```math
\phi_{PT}:S\rightarrow\mathcal V_P^{supply}.
```

Every mapping record must contain:

```text
signal ID;
signal coordinates;
power node/source ID;
power coordinates;
Euclidean/network distance used;
search radius;
matching rule;
alternative candidates count;
ambiguity flag;
manual override = prohibited unless independently documented.
```

Because SMART-DS is synthetic and the City signal layer is real, `phi_PT` is a **demonstrator coupling construction**, not a factual feeder-to-signal utility connection.

QA outputs:

```math
N_{PT}^{sig}=|S|,
\qquad
r_{match}=\frac{N_{matched}}{|S|},
```

plus mapping-distance distribution and unmatched/ambiguous counts.

No match-radius threshold is frozen until the spatial scales of both source datasets are measured.

---

## 11. T→P interface QA — repair accessibility

Let `R_P` be the set of repair-relevant power components and `V_T` the transportation access graph.

Construct

```math
\phi_{TP}:R_P\rightarrow V_T
```

using a declared access-point rule.

Each record must contain:

```text
power component ID and coordinates;
selected roadway access node/link;
access distance;
network component ID;
road-accessibility status under flood scenario;
ambiguity flag.
```

Travel-time coupling then uses the damaged transportation graph:

```math
T_i^{restore}
=
T_i^{dispatch}
+T_i^{travel}(\mathcal G_T(t))
+T_i^{onsite}.
```

The road graph supplies `T_i^{travel}`; dispatch and onsite repair times remain separate uncertain quantities and cannot be inferred from roadway distance alone.

---

## 12. Required network/interface report before threshold closure

The following table must be filled from materialized data before `G_K` can advance:

| Quantity | Symbol | Status now |
|---|---|---|
| power nodes | `N_P` | OPEN |
| power edges | `M_P` | OPEN |
| retained distribution circuits/substations | `N_{sub}` | OPEN |
| baseline power-flow convergence | — | OPEN |
| transportation nodes | `N_T` | OPEN |
| transportation links | `M_T` | OPEN |
| traffic signals in domain | `N_S` | OPEN |
| P→T matched signals | `N_PT^sig` | OPEN |
| P→T match rate | `r_match` | OPEN |
| repair-relevant power components | `N_RP` | OPEN |
| T→P accessible components | `N_TP` | OPEN |
| Harvey raster Houston coverage | `C_F` | OPEN |
| common-analysis CRS | — | OPEN |

---

## 13. Current execution result and blocker

Source discovery/qualification succeeded for the four principal data families:

```math
\boxed{
G_{source,P}=1,
\quad
G_{source,T}=1,
\quad
G_{source,S}=1,
\quad
G_{source,F}=1.
}
```

However, raw-byte materialization could not be completed in the current execution environment. Direct runtime HTTP retrieval of the H-GAC archive failed, and unrestricted external network/DNS access is not available to the local execution container. Therefore no raw file hash, byte count, geometry count, or network dimension is claimed.

This is a **data-access/materialization blocker**, not a scientific failure and not evidence against H3.

```math
\boxed{G_{bytes}=0.}
```

Consequently:

```math
\boxed{
G_{QA}=0,
\qquad
G_K=0,
\qquad
G_U=0,
\qquad
\text{H3 execution NOT AUTHORIZED}.
}
```

The correct action is to preserve the exact source endpoints and acquisition commands, then materialize the files in an environment with normal HTTP/AWS S3 access. No substitute data are fabricated.

---

## 14. Exact restart point

The next admissible action is:

```math
\boxed{
\text{materialize }D_{\Omega}
\rightarrow
D_P
\rightarrow
D_T
\rightarrow
D_S
\rightarrow
D_F
\rightarrow
\text{SHA256 + CRS + geometry/network QA}.
}
```

First dependency: obtain the authoritative Houston municipal boundary because every subsequent source must be clipped/tested against the same frozen domain.

Once raw bytes are available, run the QA gates in Sections 6–12 and update this document with actual filenames, hashes, counts, CRS values, coverage statistics, and PASS/FAIL decisions.

---

## References — APA 7

Garvin, K. M. (2018). *Inundation layers for the San Jacinto River for the August and September 2017 flood event in Texas* [Data set]. U.S. Geological Survey. https://doi.org/10.5066/F7VH5N3N

Mateo, C., Postigo, F., Elgindy, T., Birchfield, A., Duenas, P., Palmintier, B., Panossian, N., Gomez, T., de Cuadra, F., Overbye, T., Safdarian, F., & Wallison, D. (2024). Building and validating a large-scale combined transmission & distribution synthetic electricity system of Texas. *International Journal of Electrical Power & Energy Systems, 159*.

Houston-Galveston Area Council. (2026). *2025 transportation conformity documents and files*. https://www.h-gac.com/transportation-conformity/2025

Houston Public Works. (n.d.). *Traffic Management GIS: Traffic Signal layer* [GIS feature layer]. City of Houston. https://geogimsms.houstontx.gov/arcgis/rest/services/TDO/Traffic_Management_gx/MapServer/26
