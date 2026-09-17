# H1 Level 2 — FEMA NFHL Selection-Exposure Protocol v1.0

**Role:** case-selection descriptor only.  
**Status:** `SOURCE_METHOD_FROZEN_DATA_OPEN`.  
**Not:** the Level-2 dynamic flood hazard.

## 1. Scientific role

The feeder-selection feature

```math
E_H(f)=\frac{1}{2}\left(e_P(f)+e_T(f)\right)
```

is a static, pre-simulation descriptor used only to prevent arbitrary spatial-case choice.

```math
e_P=\frac{N_{P,\,SFHA}}{N_P},
\qquad
e_T=\frac{L_{T,\,SFHA}}{L_T}.
```

`E_H` is not flood depth, flood probability, fragility, failure probability, resilience, or H1 evidence.

## 2. Authoritative source

Primary service:

```text
FEMA National Flood Hazard Layer (effective data)
https://hazards.fema.gov/arcgis/rest/services/public/NFHL/MapServer
Flood Hazard Zones layer: 28
```

The acquisition script queries only effective NFHL data and freezes the returned GeoJSON plus retrieval metadata and SHA-256.

## 3. SFHA definition

Use the NFHL `SFHA_TF` field as the primary classifier:

```text
SFHA_TF = 'T'  -> inside Special Flood Hazard Area
SFHA_TF = 'F'  -> not SFHA
```

This avoids silently rebuilding FEMA's classification from zone labels. `FLD_ZONE` and `ZONE_SUBTY` are preserved for audit.

## 4. Spatial coverage

The source acquisition AOI is the published GreenEVT transportation rectangle:

```text
south = 35.894145
west  = -80.198958
north = 36.410277
east  = -79.157255
```

This broad acquisition rectangle is outcome-blind and fixed before feeder selection.

## 5. Missingness rule

Every one of the 61 feeder candidates must receive an explicit coverage state:

```text
C_hazard = TRUE
```

only when the feeder ROI has been evaluated against the frozen NFHL snapshot.

No missing feeder may be interpreted as zero exposure.

```math
\boxed{\text{missing NFHL coverage}\neq E_H=0}
```

If effective NFHL data do not cover a feeder ROI, that feeder receives an explicit noncoverage code and is not silently dropped.

## 6. Geometry operations

After the frozen transport/power geometry is available:

1. project feeder buses, roads and NFHL polygons into a declared local equal-distance/equal-area CRS appropriate to the computation;
2. count power buses intersecting SFHA polygons;
3. intersect road centerlines with the SFHA union and measure exposed length;
4. compute `e_P`, `e_T`, `E_H`;
5. retain numerator/denominator quantities and CRS in the audit table.

Boundary-touch conventions must be declared in the implementation; no visual/manual classification is allowed.

## 7. Claim boundary

The NFHL descriptor is used only for outcome-blind spatial representativeness. The actual Level-2 pluvial flood stressor remains:

```math
\text{design rainfall}
\rightarrow
\text{HEC-RAS 2D}
\rightarrow
[h(x,t),v_w(x,t)]
\rightarrow
\Phi_H.
```

Therefore:

```math
\boxed{E_H\neq\eta(x,t)}.
```
