# H3 Houston Boundary Materialization — Execution Attempt v1.0

**Date:** 2026-09-17  
**Case:** `H3-HOU-FLOOD-V1`  
**Protocol:** EGMIV–TSP  
**Thesis destination:** Chapter 4 — H3 data realization / provenance  
**Authority:** `H3_HOUSTON_BOUNDARY_FREEZE_V1.md`, `H3_HOUSTON_DATA_MATERIALIZATION_QA_V1.md`  
**Result:** **BLOCKED_EXTERNAL_EXECUTION — NOT A SCIENTIFIC FAILURE**

---

## 1. Objective

Execute the first materialization gate:

```math
\boxed{
D_{\Omega}\text{ raw bytes}
\rightarrow
\text{SHA256}
\rightarrow
\text{geometry / class / CRS QA}
\rightarrow
G_{\Omega,QA}=1.
}
```

No SMART-DS Houston extraction is scientifically admissible before this gate closes because the same `Omega_core` must define the clipping/service domain.

---

## 2. Execution route added to the repository

Two executable artifacts were added:

```text
methods/h3/materialize_houston_boundary.py
.github/workflows/h3-houston-boundary-materialization.yml
```

The Python runner is designed to:

```text
1. query the authoritative City of Houston boundary layer;
2. preserve the untouched primary ArcGIS FeatureSet JSON;
3. compute SHA-256 and byte size;
4. retrieve a WGS84 derivative solely for geometry QA;
5. verify SERVICE_TY classes;
6. reject null/empty/invalid geometry without silent repair;
7. construct Omega_core, Omega_limited and Omega_legal only as processed derivatives;
8. compute area in EPSG:2278;
9. independently cross-check against the secondary City-hosted COH City Limits layer;
10. produce an immutable manifest, QA JSON and execution summary.
```

Pinned spatial dependencies in the workflow:

```text
Python 3.11
Shapely 2.0.6
pyproj 3.7.0
```

The workflow uploads raw, processed and QA objects as a GitHub Actions artifact rather than committing large/raw evidence directly to the repository.

---

## 3. GitHub execution attempt

Workflow commit:

```text
c72354809e1132779fd7173fbe958dad7ba450e0
```

Workflow run:

```text
name:       H3 Houston boundary materialization
run_id:     35150698128
head_sha:   c72354809e1132779fd7173fbe958dad7ba450e0
event:      push
status:     completed
conclusion: failure
job_id:     104977978792
runner_id:  0
steps:      []
```

The job terminated before any workflow step was assigned/executed. No runner was attached (`runner_id=0`) and the job record contains no step executions.

As an external-control check, the repository's pre-existing `Python package` workflow on the same commit also completed as `failure` within the same interval. Therefore the observed H3 workflow failure cannot be interpreted as evidence that the boundary acquisition/QA code itself failed.

---

## 4. Scientific interpretation

The correct state is:

```math
\boxed{
G_{\Omega,source}=1,
\qquad
G_{\Omega,bytes}=0,
\qquad
G_{\Omega,QA}=0.
}
```

and

```text
BOUNDARY MATERIALIZATION = NOT EXECUTED
H3 = NOT TESTED
```

No raw file, checksum, feature count, FULL/LIMITED count, area, multipart count, invalid-geometry count, or clipped Houston geometry is claimed from this failed execution route.

The blocker is an execution-environment / GitHub Actions runner condition, not a failed scientific hypothesis and not a failed data-quality test.

---

## 5. Evidence-control rule

The following are prohibited until an actual run produces bytes:

```text
claiming G_Omega_bytes = 1;
claiming G_Omega_QA = 1;
inferring feature counts from renderer metadata;
constructing a polygon from the published layer extent;
substituting a third-party Houston boundary solely for convenience;
starting confirmatory SMART-DS Houston clipping as though Omega_core were frozen numerically.
```

---

## 6. Exact restart condition

Execution may resume immediately when either:

```text
A. GitHub Actions can assign a runner to the committed workflow; or
B. methods/h3/materialize_houston_boundary.py is run in any network-enabled environment and its raw/QA outputs are returned unchanged.
```

Required output identity before scientific continuation:

```text
coh_city_limits_primary_raw.json
coh_city_limits_manifest.json
houston_boundary_qa.json
houston_boundary_summary.txt
houston_core_full_service.geojson
houston_legal_full_plus_limited.geojson
houston_limited_service.geojson (when LIMITED features exist)
```

Then verify:

```math
\boxed{G_{\Omega,QA}=1}
```

before advancing to:

```math
\boxed{D_P\text{ — SMART-DS Houston inventory/extraction}.}
```

---

## 7. Code-control identity

```text
materialization script commit: cf21084d49c5d20359b05d475d7fc5922c54b6a7
workflow commit:              c72354809e1132779fd7173fbe958dad7ba450e0
workflow run:                 35150698128
workflow job:                 104977978792
```

No confirmatory H3 inference is authorized by this execution attempt.
