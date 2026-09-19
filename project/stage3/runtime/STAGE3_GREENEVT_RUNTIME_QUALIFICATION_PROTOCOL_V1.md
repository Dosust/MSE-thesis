# Stage 3 — GreenEVT Runtime Qualification Protocol V1

**Date:** 2026-09-19  
**Mechanism:** `EV_T_to_P` / Q05  
**Case:** `C_DEV_GREENSBORO_GREENEVT_V1`  
**Status:** PREREGISTERED EXECUTION PROTOCOL

## Objective

Qualify the computational environment required for source-backed execution of:

```math
P_b^{new}(t)=P_b^{base}(t)+N_{EV,b}^{chg}(t)P_{EV}^{chg}.
```

## Frozen identities

GreenEVT commit:

```text
6aff1cac48869ccfa0183643979f5f04b04e1124
```

Critical LFS objects:

```text
data/UDS.db
107778048 bytes
SHA256 74efbe9209bb8c7ad160f0966f01349e3c7fc187d3d0afcb3d1ddbfec1202724

data/sumo_network/greensboro.net.xml
351967227 bytes
SHA256 f0c4cd672a7fd74a5ec1e23cbdb34c6828895af52c1210ee981ef72c79fd7b06
```

Historical SUMO source revision:

```text
98d19a78148690294144002f8e1a18a28e5579cc
```

OpenDSSDirect compatibility wrapper:

```text
OpenDSSDirect.py == 0.9.4
```

This OpenDSSDirect version is a thesis-frozen compatibility implementation, not a claim about GreenEVT's exact historical package version.

## Runtime gate

```math
G_{RUNTIME}
=
G_{DATA}
\land G_{ENV}
\land G_{DSS}
\land G_{SUMO}
\land G_{Q05}
\land G_{SENS}
\land G_{REPRO}
\land G_{PROV}.
```

- `G_DATA`: exact hashes/sizes plus SQLite/XML parse.
- `G_ENV`: immutable environment specification and recorded versions.
- `G_DSS`: Master.dss compile, convergence, non-empty solution, source-load invariant.
- `G_SUMO`: historical SUMO revision plus Greensboro network smoke test and structural invariants.
- `G_Q05`: zero/one/two-EV and zero-coupling fixtures reproduce the frozen coupling law.
- `G_SENS`: separate 7.5 kW source-variant run.
- `G_REPRO`: repeated deterministic microfixture agreement within `1e-12 kW`.
- `G_PROV`: commits, hashes, package/OS manifests, image identity and gate reports preserved.

Decision:

```math
G_{RUNTIME}=PASS
\Rightarrow
G_{impl}(Q05,C_{DEV})=PASS.
```

This does not imply Stage-3 closure, empirical validation, or H1 support.

Failure semantics:
- build incompatibility → `BLOCKED_RUNTIME_COMPATIBILITY`;
- LFS mismatch → `FAIL_SOURCE_IDENTITY`;
- OpenDSS non-convergence → `FAIL_DSS_BASELINE`;
- SUMO runtime failure → `FAIL_SUMO_RUNTIME`;
- Q05 mismatch → `FAIL_IMPLEMENTATION`;
- replicate mismatch → `FAIL_REPRODUCIBILITY`.
