# H3 Harvey Hazard Source Qualification v1.0

**Status:** SOURCE HIERARCHY QUALIFIED / RAW BYTES + FULL-DOMAIN HAZARD QA OPEN  
**Date:** 2026-09-17  
**Protocol:** EGMIV–TSP  
**Case:** `H3-HOU-FLOOD-V1`  
**Thesis destination:** Chapter 4 — H3 hazard realization, provenance, and uncertainty support  
**Upstream authority:** `H3_DEMONSTRATOR_FREEZE_V1.md`

> This file refines the already-frozen Harvey hazard branch into an evidence-controlled source hierarchy. It does **not** change the demonstrator city, hazard, recovery-origin semantics, or H3 hypothesis. It prevents the USGS San Jacinto product from being misused as a full-Houston flood field and prevents unverified FEMA archive replicas from being treated as authoritative raw evidence without byte-level QA.

---

## 1. Scientific destination

The H3 demonstrator requires a post-impact flood-stress field that can be overlaid on the qualified power and transportation layers:

```math
\boxed{\eta_F(x)=d_H(x)}
```

where `d_H(x)` is the qualified Harvey maximum flood depth at location `x`, or a qualified inundation-state variable if depth is unavailable.

For this demonstrator, `eta_F` is a **post-impact spatial stress field**, not a full hydrodynamic time series. The recovery origin remains

```math
\boxed{t_R^0=\text{declared post-impact damage-assessment epoch}.}
```

The required scientific chain is

```math
\boxed{
\text{Harvey source evidence}
\rightarrow
\text{raw immutable bytes}
\rightarrow
\text{CRS/support/NoData QA}
\rightarrow
\eta_F(x)
\rightarrow
\text{exposure}
\rightarrow
\text{qualified fragility/passability}
\rightarrow
\text{component state}.
}
```

Hard separation:

```math
\boxed{
\text{flood depth/exposure}
\neq
\text{power failure}
\neq
\text{road closure/passability failure}.
}
```

No component failure probability is authorized by this source qualification.

---

## 2. Tier H-A — direct USGS San Jacinto flood evidence

### 2.1 Identity

Primary direct federal source:

```text
U.S. Geological Survey
Inundation layers for the San Jacinto River for the August and September 2017 flood event in Texas
Science Data Catalog item: USGS:5aa023ebe4b0b1c392e6881b
DOI family: 10.5066/F7VH5N3N
Publication year: 2018
Data period: 2017-08-25 to 2017-09-01
```

The USGS data release documents four relevant geospatial object classes:

```text
bnd_west / bnd_east       -> mapped-area support boundaries;
hwm_west / hwm_east       -> high-water-mark observations;
polygon_west / polygon_east -> mapped flood-inundation extents;
depth_west / depth_east   -> flood-depth rasters.
```

The depth rasters were derived from surveyed high-water-mark / streamgage-supported water-surface elevations and clipped to the mapped-area boundary.

### 2.2 Evidence-supported spatial extent

The federal data catalog reports the San Jacinto item spatial envelope as

```text
west  = -95.956288999997
south =  29.854958
 east = -95.031034000003
north =  30.624028
```

and the narrative states that the mapped products cover the West and East Fork San Jacinto system and tributaries, including Cypress Creek, Spring Creek and the reach to Lake Houston Dam.

This is **not equivalent to the City of Houston full-service domain**.

Therefore the following rule is frozen:

```math
\boxed{
D_{USGS}
=\text{union of the source-provided mapped-area support polygons},
}
```

and

```math
\boxed{
d_{USGS}(x)\text{ is admissible only for }x\in D_{USGS}.}
```

Outside `D_USGS`:

```math
\boxed{\text{USGS NoData/outside support} \neq 0\text{ ft} \neq \text{dry}.}
```

The USGS San Jacinto product therefore serves as **Tier H-A direct federal evidence and overlap-validation data**, not by itself as the full-Houston hazard surface.

### 2.3 Methodological uncertainty boundary

USGS explicitly limits the mapped area to high-water-mark-supported reaches; where flood extent was uncertain, the mapped-area boundary was aligned with the flood-inundation polygon extent. The USGS Scientific Investigations Report states that 19 inundation maps were created from high-water marks and streamgage data to document maximum flood depth.

Consequently:

```math
\boxed{
\text{absence outside source support}
\Rightarrow
\text{unknown},
\text{ not non-flooded}.
}
```

This support mask must propagate into later exposure and uncertainty calculations.

---

## 3. Tier H-B — FEMA Harris County candidate full-domain operational field

The frozen H3 domain needs substantially broader Houston coverage than the San Jacinto subset. A FEMA Harvey archive preserved by CUAHSI HydroShare identifies the direct FEMA Natural Hazard Risk Assessment Program Harvey products:

```text
Harris County AOIs and inundation boundaries:
https://data.femadata.com/FIMA/NHRAP/Harvey/Harris_AOIandBoundaries.zip

Harris County depth grid:
https://data.femadata.com/FIMA/NHRAP/Harvey/Harris_Mosaic_dgft.zip
```

The archive description attributes these FEMA products to modeled preliminary observations based on observed water levels at stream gauges interpolated along rivers, with high-water marks incorporated as available and extents validated using remote sensing.

This source is scientifically relevant because Harris County contains the Houston study domain. However, exact archive contents, raster CRS, cell size, NoData convention, units, timestamp/version, spatial support, and internal provenance have **not yet been byte-verified in this repository**.

Therefore:

```math
\boxed{G_{FEMA-Harris,source}=1}
```

but

```math
\boxed{
G_{FEMA-Harris,raw}=0,
\quad
G_{FEMA-Harris,QA}=0.
}
```

The Harris County grid is the **preferred candidate full-domain operational field** only if raw QA establishes adequate overlap with `Omega_core` and internally consistent depth semantics.

No numerical resolution is frozen for `Harris_Mosaic_dgft.zip` until its actual metadata and raster are inspected.

---

## 4. Tier H-C — FEMA 3 m composite archive as fallback/cross-check

CUAHSI HydroShare preserves metadata for a FEMA Harvey flood-depth product described as:

```text
horizontal resolution: 3 m;
published by FEMA: 2017-11-15;
format: Esri ArcGIS geodatabase;
source inputs: HCFCD, USGS and other high-water marks;
elevation inputs: 1 m / 3 m LiDAR and IfSAR;
archived full product: approximately 39–41 GB compressed resource family.
```

Archive/replica identifiers include:

```text
HydroShare legacy DOI: 10.4211/hs.165e2c3e335d40949dbf501c97827837
replacement resource: e8768f4cb4d5478a96d2b1cbd00d9e85
TACC archived file: FEMA_Harvey_Depths_3m.gdb.zip
```

A peer-reviewed Houston study also describes FEMA Region 6's Harvey inundation footprint as a GIS raster containing flood-depth values and covering Texas counties affected by Harvey.

This source is **not preferred for first materialization** because it is extremely large and its current repository copy is an archive/replica rather than a currently verified original FEMA byte stream. It is retained as:

```text
fallback if the Harris County FEMA product is unavailable/inadequate;
full-domain cross-check if computationally justified;
provenance comparison source.
```

It may not be substituted silently for Tier H-B.

---

## 5. Frozen hazard-source hierarchy

```math
\boxed{
H_A=\text{USGS San Jacinto direct federal evidence},
}
```

```math
\boxed{
H_B=\text{FEMA Harris County candidate operational field},
}
```

```math
\boxed{
H_C=\text{archived FEMA 3 m composite fallback/cross-check}.
}
```

Roles are distinct:

| Source | Primary role | Current state |
|---|---|---|
| USGS San Jacinto | direct observed/HWM-supported reference, support-aware validation | source qualified, raw bytes open |
| FEMA Harris County | candidate full-Houston operational depth field | source qualified, raw/QA open |
| FEMA 3 m composite archive | fallback and large-area cross-check | archive provenance qualified, raw/QA open |

No source is yet declared the final numerical `eta_F(x)` field because byte-level materialization and Houston-domain coverage QA have not passed.

---

## 6. Coverage gate

After `Omega_core` becomes available, compute source support coverage:

```math
\boxed{
C_s
=
\frac{\mu(\Omega_{core}\cap D_s)}{\mu(\Omega_{core})}.
}
```

For the finally selected operational hazard source `s*`, report at minimum:

```text
coverage fraction C_s*;
covered and uncovered area;
NoData fraction within covered support;
number/fraction of P assets with qualified hazard values;
number/fraction of T links/nodes with qualified hazard values;
number/fraction of traffic signals with qualified hazard values.
```

No minimum acceptable `C_s` value is invented here. The acceptance criterion must be chosen before H3 outcomes are inspected and must be consistent with the intended claim domain.

If coverage is insufficient:

```math
\boxed{G_{F,coverage}=0\Rightarrow\text{CASE DATA GATE FAILED / H3 NOT TESTED}.}
```

Do not extrapolate depth outside observed/model support merely to force full coverage.

---

## 7. Depth and support semantics

For any source raster `s`, define three separate objects:

```math
D_s(x)\in\{0,1\}
```

= documented source support,

```math
M_s(x)\in\{0,1\}
```

= valid measurement/model cell within support, and

```math
d_s(x)\ge 0
```

= depth only when valid.

The operational representation must preserve

```math
\boxed{
\text{outside support}
\neq
\text{NoData inside support}
\neq
0\text{ depth}.
}
```

A binary flood indicator may be derived only after the source's zero/NoData semantics are verified:

```math
z_F(x)=\mathbf 1\{d_s(x)>0\},\qquad x\in D_s,\ M_s(x)=1.
```

---

## 8. Cross-source comparison rule

If both FEMA and USGS depths are materialized, the overlap region is

```math
\Omega_{FU}
=
D_{FEMA}\cap D_{USGS}.
```

After CRS, units, support and raster alignment are verified, compute descriptive disagreement diagnostics such as

```math
\Delta d(x)=d_{FEMA}(x)-d_{USGS}(x),
```

with preregistered summaries including median bias, MAE, RMSE and robust quantiles where mathematically admissible.

These statistics characterize **source disagreement**; they do not establish either source as truth outside its validity domain.

Do not resample before preserving original source statistics and CRS metadata. Continuous-depth resampling and binary-inundation resampling must use different justified methods.

---

## 9. Exposure versus damage

For power component `i` and transportation element `e`, first compute exposure only:

```math
\eta_{P,i}=\eta_F(x_i),
```

```math
\eta_{T,e}=\mathcal A_e[\eta_F],
```

where `A_e` is a later-frozen line/segment aggregation operator (for example maximum, quantile or sampled profile) chosen before outcome inspection.

Then, and only after a separate evidence gate, map exposure to state:

```math
q_{P,i}=\Phi_P(\eta_{P,i};\theta_P),
```

```math
q_{T,e}=\Phi_T(\eta_{T,e};\theta_T).
```

`Phi_P` and `Phi_T` are not defined by this hazard-source step. If qualified fragility/passability models are unavailable, H3 must use bounded scenario states rather than fabricated probabilities.

---

## 10. Materialization and QA implementation

Executable utility:

```text
methods/h3/materialize_harvey_hazard.py
```

The utility is designed to:

```text
1. freeze USGS Science Data Catalog metadata;
2. query the USGS ScienceBase item and inventory attached files;
3. preserve any downloaded USGS raw objects with SHA-256;
4. materialize the FEMA Harris County depth/AOI archives when reachable;
5. protect against accidental multi-tens-of-gigabytes fallback download unless explicitly requested;
6. preserve HTTP metadata, final URL, byte count and SHA-256;
7. inventory ZIP members without trusting filenames;
8. write a machine-readable manifest;
9. never treat successful download as raster/geometry QA.
```

Raster and vector inspection must subsequently report:

```text
file format;
CRS and vertical/depth units;
raster dimensions/cell size;
NoData value and count;
finite min/max and physically implausible values;
spatial bounds;
geometry validity for support/inundation polygons;
source-support coverage relative to Omega_core;
raw and processed hashes;
all reprojection/resampling operations.
```

Raw source files are immutable after hash freeze.

---

## 11. Execution attempt in current runtime

A direct network test from the current execution container to the USGS metadata endpoint failed with a DNS-resolution error (`Temporary failure in name resolution`). This is an execution-environment blocker, not a source failure.

Therefore no raw flood raster, support polygon, ZIP member, CRS, pixel count, depth range, checksum, or coverage fraction is claimed in this file.

```math
\boxed{
G_{F,source}=1,
\quad
G_{F,prep}=1,
\quad
G_{F,raw}=0,
\quad
G_{F,QA}=0,
\quad
G_{F,coverage}=0.
}
```

---

## 12. Exact next hazard sequence

```math
\boxed{
\text{raw USGS/FEMA bytes}
\rightarrow
\text{SHA256 + archive inventory}
\rightarrow
\text{CRS/units/NoData/support QA}
\rightarrow
G_{\Omega,QA}=1
\rightarrow
\text{Houston coverage QA}
\rightarrow
\text{freeze operational }\eta_F(x).
}
```

Recommended execution order:

```text
1. USGS San Jacinto metadata + file inventory;
2. FEMA Harris_AOIandBoundaries.zip;
3. FEMA Harris_Mosaic_dgft.zip;
4. only if needed, FEMA 3 m composite archive;
5. coverage and source-overlap comparison after Omega_core exists.
```

---

## 13. Hard prohibitions

Do not:

```text
treat the USGS San Jacinto footprint as full City of Houston coverage;
convert outside-USGS-support cells to zero depth;
assume FEMA Harris raster resolution/CRS/NoData before raw inspection;
use the 39–41 GB FEMA archive merely because it is comprehensive;
blend FEMA and USGS rasters without a frozen harmonization rule;
interpret flood depth directly as asset failure probability;
count common flood exposure as a P↔T causal dependency;
claim historical 2017 infrastructure reconstruction;
proceed to H3 confirmatory execution before hazard coverage and uncertainty gates close.
```

---

## References

Garvin, K. M. (2018). *Inundation layers for the San Jacinto River for the August and September 2017 flood event in Texas*. U.S. Geological Survey data release. https://doi.org/10.5066/F7VH5N3N

Watson, K. M., Harwell, G. R., Wallace, D. S., Welborn, T. L., Stengel, V. G., & McDowell, J. S. (2018). *Characterization of peak streamflows and flood inundation of selected areas in southeastern Texas and southwestern Louisiana from the August and September 2017 flood resulting from Hurricane Harvey* (Scientific Investigations Report 2018-5070). U.S. Geological Survey. https://doi.org/10.3133/sir20185070

Federal Emergency Management Administration (FEMA). (2026). *FEMA - Harvey Flood Depths Grid* [Archived HydroShare resource]. HydroShare. https://doi.org/10.4211/hs.165e2c3e335d40949dbf501c97827837

Chakraborty, J., Collins, T. W., & Grineski, S. E. (2019). Exploring the environmental justice implications of Hurricane Harvey flooding in Greater Houston, Texas. *American Journal of Public Health, 109*(2), 244–250. (Used here only to corroborate the provenance and broad spatial use of the FEMA Region 6 inundation grid; the federal/archival sources remain primary for data acquisition.)
