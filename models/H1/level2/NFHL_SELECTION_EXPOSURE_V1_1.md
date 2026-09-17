# H1 Level 2 — Static Flood-Exposure Selection Protocol v1.1

**Authority:** amendment to `NFHL_SELECTION_EXPOSURE_V1.md`; subordinate to `PROTOCOL_V1.md`.  
**Status:** `SOURCE_AUTHORITY_RESOLVED_PAYLOAD_OPEN`.  
**Role:** case-selection descriptor only.  
**Not:** the Level-2 dynamic HEC-RAS flood hazard.

## 1. Scientific object

The frozen feeder-selection hazard descriptor remains

```math
E_H(f)=\frac{1}{2}\left(e_P(f)+e_T(f)\right),
```

with

```math
e_P=\frac{N_{P,\,SFHA}}{N_P},
\qquad
e_T=\frac{L_{T,\,SFHA}}{L_T}.
```

No mathematical meaning is changed by this amendment.

## 2. Provenance hierarchy

The semantic authority remains FEMA's National Flood Hazard Layer / effective FIRM data. For the Greensboro/Level-2 spatial case, the operational retrieval source is the Guilford County GIS implementation of FEMA's effective flood-hazard determinations.

### 2.1 National provenance authority

```text
FEMA National Flood Hazard Layer / effective FIRM data
https://www.fema.gov/flood-maps/national-flood-hazard-layer
```

### 2.2 Operational local implementation

```text
Guilford County GIS
Layer: Flood Zones Effective 06-10-2026
Service:
https://gcgis.guilfordcountync.gov/arcgis/rest/services/GISDV/Watershed_Management/MapServer/12
```

The layer documentation states that the Guilford County, North Carolina flood-hazard determinations became effective on 2026-06-10 following FEMA's final determination process.

The operational local source is admissible only inside its declared Guilford County coverage. It does not replace FEMA as the provenance authority.

## 3. SFHA classifier

The required semantic object is the source's Special Flood Hazard Area flag.

For the original national NFHL service:

```text
SFHA_TF = 'T' -> SFHA
SFHA_TF = 'F' -> not SFHA
```

For the Guilford County local implementation, the schema exposes a numeric `SFHA_TF` field. The executable acquisition code must inspect the layer metadata and accept only one of the preregistered encodings:

```text
string:  'T'/'F'
numeric: 1/0
```

No zone-label reconstruction is allowed when a valid `SFHA_TF` field exists.

## 4. Spatial domain

The retrieval AOI remains the outcome-blind GreenEVT rectangle:

```text
south = 35.894145
west  = -80.198958
north = 36.410277
east  = -79.157255
```

Because the GreenEVT rectangle extends beyond Guilford County, the local layer may only close `C_hazard` for feeder ROIs lying inside documented service coverage. Any feeder ROI outside coverage remains `NONCOVERAGE`, never zero exposure.

## 5. Retrieval and freeze requirements

The acquisition artifact must record:

- service URL;
- retrieval timestamp;
- layer name and spatial reference;
- `SFHA_TF` field type and accepted encoding;
- requested AOI;
- returned feature count;
- exact GeoJSON SHA-256;
- coverage geometry/extent;
- source role (`FEMA_PROVENANCE_GUILFORD_OPERATIONAL_IMPLEMENTATION`);
- explicit claim boundary.

A downloaded layer is not selection-ready until its geometry is intersected with all 61 feeder ROIs and every feeder receives an explicit coverage state.

## 6. Coverage rule

For feeder `f`:

```text
C_hazard(f)=TRUE
```

only when the full feeder ROI has an explicit coverage determination against the frozen effective flood-hazard snapshot.

```math
\boxed{\text{noncoverage}\neq E_H=0}
```

If the operational Guilford layer does not cover a candidate feeder ROI, the candidate receives `NONCOVERAGE_LOCAL_SOURCE`; a later authoritative source may close that gap, but the candidate may not be silently removed.

## 7. Claim boundary

This amendment affects only the static, outcome-blind spatial-selection descriptor. It does not alter the dynamic hazard chain:

```math
\text{design rainfall}
\rightarrow
\text{HEC-RAS 2D}
\rightarrow
[h(x,t),v_w(x,t)]
\rightarrow
\Phi_H.
```

Therefore

```math
\boxed{E_H\neq\eta(x,t)}.
```
