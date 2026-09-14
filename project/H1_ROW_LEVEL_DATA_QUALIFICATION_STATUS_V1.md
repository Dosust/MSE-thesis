# EGMIV H1 Row-Level Audit Execution Status v1.0

**Status:** ACQUISITION PLAN FROZEN; AUDIT CODE VERIFIED OFFLINE; RAW ROW RETRIEVAL NOT COMPLETED IN THIS CHAT RUNTIME.

## What is frozen

- E0–E4 audit windows and candidate train/test roles.
- Official source endpoint templates.
- Required native fields.
- Native timezone handling.
- NYC county FIPS set for EAGLE-I.
- Missing-data rule: absent EAGLE-I row is never converted to zero.
- TLC rule: completed HVFHV records are not the entire requested-demand population.
- Deterministic row-level metrics: rows, timestamp range, gap distribution, null rates, duplicates, provenance hash.
- R1/R2/R3/R5 machine checks; R4/R6/R7/R8 remain provenance/process gates.

## Retrieval status

The available web evidence verifies the official archives, API schemas and distribution endpoints. This runtime, however, does not provide general outbound network access to Python/container code and the web reader does not return large ZIP/Parquet bodies. Therefore actual event-window row counts/null rates are **not** claimed here.

This is deliberately recorded as a blocked acquisition state, not silently upgraded to PASS.

## Activation condition

The candidate split remains:

\[
D_{train}^{cand}=\{E0,E2\},\qquad
D_{test}^{cand}=\{E1,E3,E4\}
\]

and may become frozen only after the provided executor retrieves the raw data and every required event/source role passes the predeclared R1–R8 gates.

No M0/M1/M2 calibration or H1 confirmatory run is authorized before that activation.
