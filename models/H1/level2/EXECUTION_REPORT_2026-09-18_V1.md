# H1 Level 2 — Source/Spatial-Case Execution Report v1

**Date:** 2026-09-18  
**Method:** EGMIV  
**Scientific role:** execution/governance record only; not H1 evidence.  
**Target gate:** source qualification → feeder features → outcome-blind development/held-out case freeze.

## 1. Starting objective

The intended transition was

```math
\text{GreenEVT source audit}
\rightarrow
\text{61-feeder feature extraction}
\rightarrow
\text{outcome-blind feeder selection}
\rightarrow
\text{development/held-out case freeze}.
```

No `M0/M1/M2` result was inspected or used for feeder selection in this execution.

## 2. Source identity findings

The upstream source is frozen to GreenEVT commit

```text
6aff1cac48869ccfa0183643979f5f04b04e1124
```

Two selection-critical files are Git-LFS objects. Their exact frozen identities are:

```text
data/UDS.db
SHA-256 74efbe9209bb8c7ad160f0966f01349e3c7fc187d3d0afcb3d1ddbfec1202724
size    107778048 bytes

data/sumo_network/greensboro.net.xml
SHA-256 f0c4cd672a7fd74a5ec1e23cbdb34c6828895af52c1210ee981ef72c79fd7b06
size    351967227 bytes
```

An exact LFS pointer is accepted as evidence of intended object identity but is not materialized data. It cannot pass DB schema, crosswalk, topology, or feature-extraction gates.

## 3. Source acquisition status

### Local runtime

The current execution runtime could not resolve the external GitHub/maintainer download hosts for Git/LFS materialization. Therefore the actual LFS bytes were not obtained locally.

### GitHub Actions attempt

Workflow `H1 Level2 Frozen Source Audit` was committed and triggered. Its job ended with `runner_id=0` and no reported workflow steps. The repository's pre-existing Python-package workflow on the same push showed the same pre-step failure pattern.

Therefore the CI event is classified as:

```text
EXECUTION_ENVIRONMENT_BLOCK_ONLY
```

It is **not** evidence of corrupt/unavailable GreenEVT LFS content.

## 4. Feeder inventory

The frozen OpenDSS master redirects and feeder directories establish:

```text
21 substation groups
61 feeder directories
```

The exact source inventory is stored separately in:

```text
artifacts/feeder_inventory_v1.csv
```

The current selection matrix contains the same 61 feeder IDs, but all unqualified feature values remain blank and all eligibility predicates remain `FALSE`.

No zero is used as a missing-value substitute.

## 5. Feature semantics frozen before complete feature values

`FEEDER_FEATURE_SPECIFICATION_V1.md` now freezes

```math
z_f=[N_P,N_T,N_I,P_{\max},L_T,R_T,E_H]
```

before complete values are observable.

The definitions are:

```math
N_P=|V_P^f|,
```

where `V_P^f` is the de-duplicated feeder bus set from the feeder-level coordinate file;

```math
N_T=|E_T^f|,
\qquad
L_T=\sum_{e\in E_T^f}\ell_e/1000,
```

where `E_T^f` is the set of non-internal passenger SUMO edges intersecting the deterministic feeder convex hull;

```math
R_T=
\frac{|E_U^f|-|V_U^f|+c_f}{|E_U^f|},
```

for the simple undirected road projection;

```math
N_I=|I_f|,
```

where `I_f` is the de-duplicated source-derived bus/parcel-to-SUMO-edge interface-opportunity pair set;

```math
P_{\max}=\sum_{b\in V_P^f} P_{b,\max}^{UDS},
```

with no authorized fallback when `max_real_power` is absent;

and

```math
E_H=\frac12(e_P+e_T),
```

using effective FEMA-NFHL Special Flood Hazard Area exposure only as a **static case-selection descriptor**.

`E_H` is not HEC-RAS forcing, a fragility relation, or a resilience metric.

## 6. Anti-bias execution chain implemented

The selection software now requires:

```text
exact frozen source bytes
-> source/schema/topology audit
-> feature extraction
-> explicit FEMA coverage determination for all 61 feeders
-> feature-matrix qualification
-> SHA-256 binding
-> outcome-blind selector
```

`select_feeders.py` will reject:

- an unqualified matrix;
- a matrix from the wrong upstream commit;
- a matrix with mismatched eligible-feeder set;
- a post-qualification matrix edit whose SHA-256 differs;
- fewer than two eligible feeders.

The feature-qualification gate additionally rejects a population in which even one feeder lacks an explicit FEMA-NFHL coverage determination. Thus source missingness cannot silently remove a feeder from the candidate population.

## 7. Software-control checks executed

### LFS identity guard

Local regression checks verified:

```text
exact UDS pointer identity: accepted as identity, not materialization
wrong UDS SHA-256: rejected
exact SUMO pointer identity: accepted as identity, not materialization
```

Result:

```text
3 passed
```

### Feature qualification / tamper guard

A local synthetic 61-row software fixture verified:

1. one missing FEMA determination blocks qualification;
2. a complete qualified matrix receives a SHA-256 authorization;
3. the outcome-blind selector returns distinct development/held-out IDs on the fixture;
4. editing the CSV after qualification causes selector rejection.

Result:

```text
1 passed
```

These tests establish software-control behavior only. They do not establish H1, Greensboro validity, feeder eligibility, or model accuracy.

## 8. Current gate result

```math
\boxed{
\text{METHOD + FEATURE SEMANTICS FROZEN}
\rightarrow
\text{SOURCE IDENTITIES FROZEN}
\rightarrow
\text{61-FEEDER INVENTORY COMPLETE}
\rightarrow
\text{BLOCKED: LFS BYTES + NFHL EXPOSURE}
}
```

Current authoritative status:

```text
spatial_case_frozen = false
confirmatory_ready  = false
```

No development feeder ID exists yet. No held-out feeder ID exists yet.

## 9. Scientific interpretation

This execution is classified as:

```text
NOT TESTED — SOURCE/EXPOSURE QUALIFICATION INCOMPLETE
```

It is neither support for nor falsification of H1.

The correct next transition, when source bytes become accessible, is:

```text
materialize exact UDS.db + greensboro.net.xml
-> verify SHA-256/size
-> run UDS/SUMO audit
-> compute all source-derived feeder features
-> qualify effective-NFHL exposure for all 61 feeders
-> cryptographically qualify feature matrix
-> execute frozen medoid selector
-> freeze development/held-out case manifests
```

No manual feeder choice is admissible in place of this sequence.
