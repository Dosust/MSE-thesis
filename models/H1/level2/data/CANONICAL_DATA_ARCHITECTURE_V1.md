# H1 Level-2 Canonical Data Architecture v1.0

**Status:** `FROZEN_SOURCE-ROLE ASSIGNMENT`  
**Frozen:** 2026-09-18  
**Authority:** subordinate to the canonical RQ/SO/Hypotheses, Level-2 protocol, dependency contract, and EGMIV governance.  
**Purpose:** assign one primary data source to each Level-2 scientific role while preventing circular construction/validation and uncontrolled source substitution.

## 1. Core separation

The Level-2 data architecture is

```math
\boxed{
\mathcal D^\star=
\{
D_P,D_T,D_I,D_{EH},D_R,D_{DEM},D_{soil},D_{LC},
D_{hydro},D_T^{obs},D_H^{obs},D_R^{obs},D_P^{obs}
\}.
}
```

The same source must not silently move between incompatible roles. In particular:

```math
D_{BUILD}\neq D_{OBS}
```

whenever an independent observation is available.

### Construction layer

```math
D_{BUILD}=
\{
\text{GreenEVT/SMART-DS},
\text{3DEP},
\text{SSURGO},
\text{Annual NLCD},
\text{USGS hydrography},
\text{Greensboro stormwater},
\text{Greensboro signal GIS}
\}.
```

### Forcing / case-selection layer

```math
D_{FORCE}=
\{
\text{FEMA NFHL},
\text{NOAA Atlas 14}
\}.
```

NFHL is used only for static feeder-selection exposure. Atlas 14 is used for design rainfall forcing.

### Observation layer

```math
D_{OBS}=
\{
\text{NCDOT},
\text{USGS Water/FEV},
\text{NOAA/NCEI},
\text{ORNL EAGLE-I / DOE event-correlated outage data}
\}.
```

## 2. Frozen primary assignment

| Object | Primary source | Exact thesis role | Scientific class |
|---|---|---|---|
| (D_P) | GreenEVT / SMART-DS OpenDSS | realistic-synthetic electrical topology, buses, baseline loads | SYNTHETIC TESTBED |
| (D_T) | GreenEVT SUMO | realistic-synthetic transportation topology | SYNTHETIC TESTBED |
| (D_I) | GreenEVT UDS + Greensboro signal GIS | source-qualified P-T crosswalk opportunities + observed signal locations | DERIVED / ESTABLISHED GEOMETRY |
| (D_{EH}) | FEMA NFHL | effective SFHA polygons for (e_P,e_T,E_H) and outcome-blind feeder selection | STATIC CASE-SELECTION DATA |
| (D_R) | NOAA Atlas 14 / PFDS | design precipitation frequency and temporal forcing candidates | MODEL INPUT |
| (D_{DEM}) | USGS 3DEP | terrain for HEC-RAS 2D | MODEL INPUT |
| (D_{soil}) | USDA-NRCS SSURGO | soil/infiltration parameter evidence | MODEL INPUT / UNCERTAINTY INPUT |
| (D_{LC}) | Annual NLCD Collection 1.2 | land cover + fractional imperviousness | MODEL INPUT |
| (D_{hydro}) | USGS hydrography + Greensboro stormwater GIS | regional hydrography and local urban drainage geometry | MODEL INPUT |
| (D_T^{obs}) | NCDOT traffic products | baseline calibration; incident/closure evidence where temporally aligned | CALIBRATION / PARTIAL VALIDATION |
| (D_H^{obs}) | USGS Water Data + Flood Event Viewer | observed stream stage/flow/HWM/flood-event evidence | INDEPENDENT OBSERVATION |
| (D_R^{obs}) | NOAA/NCEI | historical event rainfall and meteorological observations | INDEPENDENT OBSERVATION |
| (D_P^{obs}) | ORNL EAGLE-I / DOE event-correlated outage dataset | county-level 15-min outage/recovery trajectories | INDEPENDENT OBSERVATION |

## 3. Fixed spatial domain for acquisition

Until development/held-out feeders are frozen, acquisition uses the published GreenEVT bounding rectangle:

```text
west  = -80.198958
south =  35.894145
east  = -79.157255
north =  36.410277
CRS   = EPSG:4326
```

Large raster products are not fully materialized for the whole region unless needed. After outcome-blind feeder selection, HEC-RAS inputs are spatially cropped to the frozen feeder ROIs plus a hydraulically justified buffer/catchment domain.

## 4. Static flood-selection rule

FEMA NFHL is the primary authority for static flood exposure.

```math
e_P(f)=\frac{|\{b\in V_P^f:b\in SFHA\}|}{N_P(f)}
```

```math
e_T(f)=
\frac{\sum_{e\in E_T^f}\ell(e\cap SFHA)}
{\sum_{e\in E_T^f}\ell_e}
```

```math
\boxed{E_H(f)=\tfrac12[e_P(f)+e_T(f)]}
```

NFHL is **not** a substitute for dynamic pluvial inundation:

```math
\boxed{\text{NFHL}\neq h(x,y,t)}
```

## 5. Dynamic flood chain

```math
\boxed{
\text{NOAA Atlas 14}
+
\text{3DEP}
+
\text{SSURGO}
+
\text{Annual NLCD}
+
\text{hydrography/drainage}
\rightarrow
\text{HEC-RAS 2D}
\rightarrow
\eta(x,t)=[h(x,t),v_w(x,t)]
}
```

The spatial support of each source remains explicit. Resampling a coarser product does not create finer information.

## 6. Validation boundary

GreenEVT/SMART-DS data may be used to construct and verify the synthetic testbed, but may not serve as an independent observational reference for H1 predictive claims.

The strongest public partial reference stack is:

```math
\mathcal R_e=
\{
R_{met}^{NCEI},
R_{hyd}^{USGS},
R_T^{NCDOT},
R_P^{EAGLE-I}
\}.
```

If no historical event has temporally compatible observations across all four components, the result must remain:

```text
NO PUBLIC FULLY COUPLED OBSERVATIONAL REFERENCE FOUND
```

and H1 accuracy claims must be limited accordingly.

## 7. Repository storage policy

Git is the scientific **registry and reproducibility layer**, not a dump for national geospatial archives.

### Commit directly

- source registries and provenance metadata;
- checksums;
- exact acquisition scripts;
- small/medium licensed study-area vector extracts;
- small tabular observational extracts;
- derived feeder-level feature tables;
- processing logs.

### Do not commit directly to ordinary Git

- national 1-m DEM archives;
- full Annual NLCD CONUS archives;
- full national SSURGO archives;
- full EAGLE-I/DOE outage archives if large;
- any file exceeding normal GitHub practical limits;
- data whose terms prohibit redistribution.

For such objects, store exact persistent source URL/DOI, version, retrieval query, byte size, checksum after materialization, and local target path. A study-area derivative may be committed only if licensing and size permit.

## 8. Anti-circularity rule

No observation used to calibrate a parameter may be silently reused as an independent confirmatory reference for the same quantity. Every dataset must record one or more explicit roles:

```text
CONSTRUCTION
CASE_SELECTION
FORCING
CALIBRATION
SUBMODEL_VALIDATION
INDEPENDENT_REFERENCE
```

Role changes require a versioned amendment before target results are inspected.

## 9. Immediate execution order

```math
\boxed{
\text{NFHL}
\rightarrow
E_H(1{:}61)
\rightarrow
\text{qualify feature matrix}
\rightarrow
f_D,f_H
\rightarrow
\text{crop 3DEP/SSURGO/NLCD/drainage}
\rightarrow
\text{HEC-RAS forcing}
}
```

Observation acquisition may proceed in parallel, but it cannot influence feeder selection.
