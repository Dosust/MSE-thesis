# Level-2 Canonical Data

This directory implements the source-role decisions in `CANONICAL_DATA_ARCHITECTURE_V1.md`.

## Policy

`source_registry_v1.csv` is the frozen source-role registry.

`acquire_canonical_data.py` retrieves reproducible study-area extracts where direct machine access and redistribution are appropriate.

The GreenEVT study rectangle is:

```text
[-80.198958, 35.894145, -79.157255, 36.410277]  EPSG:4326
```

## Storage classes

### Git-committable

Small federal/public study-area vectors, metadata, query responses, checksums and event-specific tabular extracts may be stored in `materialized/` when below practical GitHub file-size limits.

### External authoritative raw

Large raster/archive sources remain external and are represented by a stable URL/DOI, query, version and SHA-256 after acquisition. Examples include 1-m 3DEP tile collections, full Annual NLCD bundles and national outage archives.

After the outcome-blind development/held-out feeder IDs are frozen, large physical inputs are cropped to the hydraulically justified HEC-RAS domains before any repository inclusion decision.

## Current highest-priority materialization

```math
\text{FEMA NFHL}\rightarrow E_H(1{:}61)\rightarrow
\text{feature qualification}\rightarrow f_D,f_H.
```

No file in this directory authorizes confirmatory H1 execution by itself.
