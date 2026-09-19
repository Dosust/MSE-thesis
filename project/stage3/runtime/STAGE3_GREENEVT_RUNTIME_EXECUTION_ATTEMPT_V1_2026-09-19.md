# Stage 3 GreenEVT Runtime Qualification — Execution Attempt V1

**Date:** 2026-09-19  
**Workflow:** `Stage 3 GreenEVT Runtime Qualification`  
**Run ID:** `35439846744`  
**Initial Job ID:** `105888650952`  
**Rerun Job ID:** `105889240833`  
**Head SHA of original run:** `6fbee3da39a6f3f03cffbb8c30ee9c982e609f7c`

## Initial attempt

GitHub reported:

```text
workflow status   = completed
workflow result   = failure
job result        = failure
executed steps    = 0
downloadable logs = unavailable
```

The job returned no step summaries and the job-log endpoint returned no log blob.

## Controlled rerun

The failed workflow job was rerun once. GitHub created job `105889240833` and again reported:

```text
job result        = failure
executed steps    = 0
downloadable logs = unavailable
```

The job-step endpoint returned an empty list. The job-log retrieval returned `404 BlobNotFound`.

This repeated result establishes only that execution was blocked before any declared workflow step ran. It does not identify the underlying GitHub/runner account or infrastructure cause.

## Scientific classification

```math
\boxed{
\text{BLOCKED-EXECUTION-ENVIRONMENT}
}
```

This is **not**:

```math
\text{FAIL}_{DATA},
\quad
\text{FAIL}_{DSS},
\quad
\text{FAIL}_{SUMO},
\quad
\text{FAIL}_{Q05},
\quad
\text{FAIL}_{REPRO},
\quad
\text{FAIL}_{PROV}.
```

No runtime gate was actually executed, so no scientific PASS or FAIL may be inferred.

## Current gate state

```text
G_DATA    = NOT EXECUTED
G_ENV     = NOT EXECUTED
G_DSS     = NOT EXECUTED
G_SUMO    = NOT EXECUTED
G_Q05     = NOT EXECUTED
G_SENS    = NOT EXECUTED
G_REPRO   = NOT EXECUTED
G_PROV    = PARTIAL (workflow/run/rerun identity preserved)
G_RUNTIME = BLOCKED
```

## Implementation hardening after the blocked run

Static audit identified and corrected four control issues before the next valid execution:

1. `G_ENV` now verifies exact Python 3.11.16 and the exact checked-out historical SUMO source commit.
2. `G_SUMO` now tests both direct network loading and a deterministic configuration+route microfixture on the frozen Greensboro network.
3. `G_PROV` is now an executed evidence gate rather than a hard-coded `True`.
4. Runtime gates are collected independently so one scientific failure does not suppress unrelated evidence; the aggregate gate remains authoritative.

## Required next execution route

Execute the hardened runtime package on a Linux/amd64 Docker-capable environment that can:

1. start a job successfully;
2. run Docker containers;
3. access GitHub and GreenEVT Git-LFS or the upstream fallback archive;
4. build the frozen historical SUMO revision;
5. install the frozen OpenDSSDirect compatibility wrapper;
6. retain the generated `runtime_artifacts/` evidence bundle.

The authoritative workflow remains:

```text
.github/workflows/stage3-greenevt-runtime-qualification.yml
```

A successful runner execution must be audited before changing `G_RUNTIME`.
