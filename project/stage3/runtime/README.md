# Stage 3 GreenEVT Runtime Qualification

**Status:** IMPLEMENTED AND HARDENED / HOSTED EXECUTION BLOCKED BEFORE FIRST STEP  
**Date:** 2026-09-19  
**Case role:** `C_DEV_GREENSBORO_GREENEVT_V1`

```math
\boxed{
G_{RUNTIME}
=
G_{DATA}
\land
G_{ENV}
\land
G_{DSS}
\land
G_{SUMO}
\land
G_{Q05}
\land
G_{SENS}
\land
G_{REPRO}
\land
G_{PROV}
}
```

A runtime PASS is a software/model implementation qualification result. It is not empirical validation of Greensboro infrastructure and does not close Stage 3.

Implemented controls:
- frozen container/runtime specification;
- exact GreenEVT and SUMO source identities;
- exact LFS byte/hash/size checks;
- independent OpenDSS baseline gate;
- Greensboro SUMO network + config/route microfixture gate;
- source-backed Q05 coupling fixtures for 0/1/2 EVs and disabled coupling;
- 7.2/7.5 kW source-variant execution;
- deterministic replicate comparison;
- evidence-backed provenance gate;
- aggregate runtime decision with no hard-coded gate PASS.

Files:
- `STAGE3_GREENEVT_RUNTIME_QUALIFICATION_PROTOCOL_V1.md`
- `STAGE3_GREENEVT_RUNTIME_LOCK_V1.json`
- `SUMO_SOURCE_LOCK_V1.json`
- `OPENDSS_ENGINE_LOCK_V1.json`
- `requirements-greenevt-v1.txt`
- `Dockerfile.greenevt-v1`
- `STAGE3_GREENEVT_RUNTIME_EXECUTION_ATTEMPT_V1_2026-09-19.md`

Execution scripts live under `models/H1/level2/runtime/`.

Current blocker: GitHub Actions run `35439846744` failed twice before executing any workflow step. No scientific gate has therefore been executed yet.
