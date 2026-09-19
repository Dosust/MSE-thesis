# Case Role Authority V1

**Status:** FROZEN — CASE-ROLE SEMANTICS ONLY  
**Effective date:** 2026-09-19  
**Scope:** development, external-evidence, and confirmatory-case roles  
**Scientific effect:** role synchronization only; this file does **not** make any case empirically admissible, does not change H1–H5, and does not authorize confirmatory execution.

## 1. Authority hierarchy

This case-role authority is subordinate to the current thesis authorities and preserves their case semantics:

1. `project/CANONICAL_RQ_SO_HYPOTHESES_V3.md`
2. `project/CANONICAL_7_STAGE_FRAMEWORK_V2.md`
3. frozen Chapter I, especially `thesis/01_introduction/01_06_scope_boundaries_and_assumptions.md`
4. `project/AUSTIN_CASE_STUDY_DATA_ADMISSIBILITY_MATRIX_V3.md`
5. current Stage-2/3/4 case-specific evidence packages
6. `project/reality_evidence/` operational-evidence governance

The frozen Chapter-I scope identifies `AUS-P5U-2018-V1` as a **candidate case**, not an admissible empirical case. The Austin admissibility matrix independently preserves the same status.

## 2. Frozen case roles

### C_DEV — Greensboro / GreenEVT / SMART-DS

**Case-role ID:** `C_DEV_GREENSBORO_GREENEVT_V1`

**Role:** development, source-backed realistic-synthetic coupling, software/model verification, mechanism implementation, benchmark construction, and pre-confirmatory H1–H3 development.

Permitted uses include:
- Stage-1/2/3 structure/mechanism/model development;
- source-backed GreenEVT/SMART-DS coupled implementation;
- Stage-2 case-specific mechanism qualification within the declared synthetic-testbed validity domain;
- Stage-3 benchmark/development and limiting-case verification;
- Stage-4 development experiments when clearly labeled;
- Stage-5 B0/B1/B2-type method verification and development.

Claim ceiling:

```math
oxed{
C_{DEV}

eq
C_{CONF}
}
```

and

```math
oxed{
	ext{realistic-synthetic Greensboro power topology}

eq
	ext{observed Greensboro utility feeder}.
}
```

GreenEVT/SMART-DS may not be promoted to confirmatory case status without a versioned case-role amendment issued **before** inspecting the proposed confirmatory outcome.

---

### C_EXT — Austin operational reality

**Case-role ID:** `C_EXT_AUSTIN_OPERATIONAL_V1`

**Role:** external real-world operational, event, hazard, utility, transportation, and organizational evidence.

Permitted uses include:
- regional/utility plausibility envelopes;
- independent external evidence when admissibility and independence gates pass;
- organizational/response evidence;
- event-replay development;
- service/recovery context;
- external validation evidence only where the model quantity, geography, time, support, and measurement semantics match.

Examples include ERCOT, Austin Energy, Austin TPW, NWS/NOAA, City traffic/incident data, and emergency plans.

Permanent rule:

```math
oxed{
	ext{Austin operational evidence}

eq
	ext{Austin 2018 integrated confirmatory case by default}.
}
```

---

### C_CONF — Austin `AUS-P5U-2018-V1`

**Case-role ID:** `C_CONF_AUS_P5U_2018_V1`

**Role:** current **candidate confirmatory / held-out integrated case**, consistent with frozen Chapter I.

Current status:

```text
CANDIDATE — NOT YET ADMISSIBLE
CONFIRMATORY EXECUTION — NOT AUTHORIZED
```

The controlling admissibility gate remains:

```math
G_{AUS}
=
prod_{k=0}^{8}G_k.
```

Only `G_AUS=PASS` may make the candidate case admissible for its declared confirmatory use.

This case uses SMART-DS as a synthetic power benchmark embedded in Austin-relevant spatial/observational support; it must never be described as proprietary Austin Energy feeder topology.

## 3. Temporal firewall — Austin 2018 vs Austin 2025

The Austin May 28–29, 2025 microburst is classified under `C_EXT`.

```math
oxed{
omega_{Austin,2025}

eq
C_{CONF,Austin,2018}.
}
```

Therefore 2025 event evidence may support:
- external hazard/response plausibility;
- organizational structure/response evidence;
- event-replay methodology;
- external validation only for quantities whose temporal/geographic semantics genuinely match.

It may **not** be used as case-matched empirical validation of the 2018 `AUS-P5U-2018-V1` realization without a separately defined, versioned temporal-bridging protocol and admissibility audit.

## 4. Role separation rule

```math
oxed{
C_{DEV}

eq
C_{EXT}

eq
C_{CONF}
}
```

The same city or source may participate in more than one scientific role only when:
- the role is declared prospectively;
- calibration/validation independence is preserved;
- temporal and spatial support are compatible;
- the claim ceiling is explicit;
- no source is reused to create a circular validation.

## 5. Cross-stage use

| Stage | C_DEV | C_EXT | C_CONF |
|---|---|---|---|
| S1 | development structure/crosswalk | external structural/context evidence | candidate confirmatory structure after gates |
| S2 | mechanism development/qualification in declared synthetic validity domain | external mechanism evidence | candidate case mechanism qualification after gates |
| S3 | model development/verification/source-backed benchmark | operational/hazard external reference | confirmatory physical realization after gates |
| S4 | development observation/control experiments | organizational/operational external evidence | confirmatory observation/control after gates |
| S5 | method/benchmark viability-reachability work | external event/recovery reference | confirmatory B3/H3 after gates |
| S6 | intervention-method development only | external intervention/accounting evidence | confirmatory H4 only after upstream gates |
| S7 | decision-method development only | external feasibility/governance evidence | confirmatory H5 only after upstream gates |

## 6. Scientific non-effects

This freeze does not:
- close `G_{2\to3}`;
- resolve the 7.2/7.5 kW charging parameter discrepancy;
- materialize GreenEVT Git-LFS objects;
- close Stage-3 case gates;
- close Stage-4 measurement/organization gates;
- compute Stage-5 B3/H3;
- make Austin admissible;
- support or reject H1–H5.

## 7. Change control

Any change to the role of `C_DEV`, `C_EXT`, or `C_CONF` requires a versioned amendment with:
1. reason for change;
2. affected hypotheses/stages;
3. calibration/validation impact;
4. case-admissibility impact;
5. leakage/outcome-inspection audit;
6. updated Chapter-I synchronization note if needed.

No case-role change may be justified by favorable target outcomes.
