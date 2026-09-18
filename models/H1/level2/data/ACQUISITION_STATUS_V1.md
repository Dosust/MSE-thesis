# Canonical Data Acquisition Status v1

**Date:** 2026-09-18  
**Architecture:** `CANONICAL_DATA_ARCHITECTURE_V1.md`

## Completed

- canonical source-role architecture frozen;
- primary source registry committed;
- GreenEVT exact source already materialized and audited separately;
- reproducible acquisition script committed;
- GitHub Actions acquisition workflow committed and triggered.

## Runtime acquisition result

### Chat execution container

Direct DNS resolution remains unavailable for the authoritative external GIS/data hosts tested, including FEMA, Greensboro GIS, USGS Water and The National Map. This is an execution-environment network constraint, not evidence of source unavailability.

### GitHub Actions

Workflow run:

```text
H1 Level-2 Canonical Data Acquisition
run id: 35305848433
commit: ccf1c3c52200ab0df23fdcb3c8dc6c0a07f9ce86
conclusion: failure
```

The job returned no executed steps, and the job-log endpoint returned a missing log blob. Therefore the workflow failed before the acquisition code executed.

Classification:

```text
CI/RUNNER EXECUTION FAILURE
!=
DATA SOURCE FAILURE
```

No FEMA/USGS/NCDOT/NOAA source should be marked failed on this basis.

## Current source materialization state

| Source | Role | State |
|---|---|---|
| GreenEVT | P/T synthetic system | MATERIALIZED + AUDITED |
| FEMA NFHL | static E_H | PENDING PAYLOAD |
| NOAA Atlas 14 | design rainfall | SOURCE FROZEN; EVENT VALUES PENDING |
| USGS 3DEP | terrain | PENDING AFTER FEEDER FREEZE |
| SSURGO | soils | PENDING AFTER FEEDER FREEZE |
| Annual NLCD 1.2 | land cover/imperviousness | PENDING AFTER FEEDER FREEZE |
| USGS hydrography | regional drainage | PENDING AFTER FEEDER FREEZE |
| Greensboro stormwater | local drainage | PENDING PAYLOAD + REUSE CHECK |
| Greensboro traffic signals | interface geometry | PENDING PAYLOAD + REUSE CHECK |
| NCDOT traffic | calibration/partial validation | PENDING EVENT/CALIBRATION SELECTION |
| USGS Water/FEV | hydraulic validation | PENDING EVENT SELECTION |
| NOAA/NCEI | observed meteorology | PENDING EVENT SELECTION |
| DOE/ORNL outage data | power validation | PENDING PAYLOAD/EVENT EXTRACTION |

## Scientific next gate

The only dataset required before outcome-blind feeder selection is the complete effective SFHA geometry needed for

```math
E_H(f)=\tfrac12[e_P(f)+e_T(f)],\qquad f=1,\ldots,61.
```

Therefore the acquisition priority remains:

```math
\boxed{
\text{FEMA NFHL payload}
\rightarrow
E_H(1{:}61)
\rightarrow
\text{feature matrix qualification}
\rightarrow
f_D,f_H
}
```

Large HEC-RAS raster inputs are intentionally not downloaded before feeder/catchment freeze because doing so is unnecessary for outcome-blind selection and would add large unneeded archives to the repository.
