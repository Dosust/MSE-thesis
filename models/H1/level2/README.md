# H1 Level 2 — Realistic Synthetic Spatial Twin

**Protocol:** `PROTOCOL_V1.md`  
**Feature semantics:** `FEEDER_FEATURE_SPECIFICATION_V1.md`  
**Machine contract:** `config/protocol_v1.json`  
**Current status:** `METHOD_FROZEN_SOURCE_MATERIALIZATION_BLOCKED`  
**Spatial case frozen:** `NO`  
**Confirmatory H1 execution:** `NOT AUTHORIZED`  
**System lineage:** SMART-DS/OpenDSS Greensboro + GreenEVT OSM/SUMO.

## Purpose

Level 2 binds the verified H1 comparators to a spatially realistic synthetic Power–Transportation testbed. Its scientific target is **incremental explanatory/predictive information**, not whether the dynamic model produces numerically better system performance.

```math
M_0=\text{independent},\qquad
M_1=\text{static coupling},\qquad
M_2=\text{dynamic causal coupling}.
```

SMART-DS is realistic synthetic infrastructure, not the actual Greensboro utility network. A held-out SMART-DS feeder tests spatial generalization inside the synthetic testbed; it is not observational validation.

## Current scientific state

```text
METHOD + FEATURE SEMANTICS FROZEN
-> FROZEN GREENEVT COMMIT IDENTIFIED
-> EXACT CRITICAL LFS OBJECT IDENTITIES FROZEN
-> 21-SUBSTATION / 61-FEEDER INVENTORY COMPLETE
-> BLOCKED: CRITICAL LFS BYTES NOT MATERIALIZED IN CURRENT EXECUTION ENVIRONMENT
-> BLOCKED: FEMA-NFHL STATIC EXPOSURE MATRIX NOT YET QUALIFIED
-> NO FEEDER SELECTED
```

The frozen GreenEVT commit is:

```text
6aff1cac48869ccfa0183643979f5f04b04e1124
```

Critical LFS objects are accepted only if their **materialized bytes** match:

```text
data/UDS.db
SHA-256 74efbe9209bb8c7ad160f0966f01349e3c7fc187d3d0afcb3d1ddbfec1202724
size    107778048 bytes

data/sumo_network/greensboro.net.xml
SHA-256 f0c4cd672a7fd74a5ec1e23cbdb34c6828895af52c1210ee981ef72c79fd7b06
size    351967227 bytes
```

An exact LFS pointer establishes intended source identity but **does not** count as materialized data and cannot pass the schema/topology gates.

## Controlled workflow

```text
source acquisition
-> exact-byte audit
-> UDS schema/crosswalk + SUMO topology audit
-> preregistered feeder feature extraction
-> FEMA-NFHL static exposure qualification
-> cryptographic feature-matrix qualification
-> outcome-blind development/held-out selection
-> frozen case manifests
-> canonical dependency materialization
-> coherent HEC-RAS flood field + hazard-response maps
-> parameter freeze
-> matched M0/M1/M2 + ablations
-> V&V
-> UQ/sensitivity
-> independent-reference model-error test
-> later Stage-5 viability geometry
```

## Selection features

`FEEDER_FEATURE_SPECIFICATION_V1.md` freezes the pre-result selection vector before complete values are available:

```math
z_f=[N_P,N_T,N_I,P_{\max},L_T,R_T,E_H].
```

The development case is the robustly standardized global medoid. The held-out case is a conditional second medoid. No `M0/M1/M2` output may enter feature construction or selection.

`E_H` is only a static FEMA-NFHL **case-selection exposure descriptor**. It is not the later HEC-RAS pluvial forcing, a fragility function, or a resilience score.

## Important files

### Scientific controls
- `PROTOCOL_V1.md` — frozen Level-2 scientific protocol.
- `FEEDER_FEATURE_SPECIFICATION_V1.md` — exact pre-data feature semantics.
- `config/protocol_v1.json` — machine-readable protocol.
- `config/protocol_status_v1.json` — current gate state.
- `config/source_manifest_v1.json` — source/method provenance.
- `registries/dependency_registry_v1.csv` — canonical directed dependencies.
- `registries/parameter_registry_v1.csv` — parameter provenance/uncertainty.
- `registries/scenario_matrix_v1.csv` — matched scenarios and ablations.
- `registries/qoi_registry_v1.csv` — H1 outcome families and secondary QOIs.

### Source and spatial-case pipeline
- `acquire_level2.py` — checks out the exact frozen GreenEVT commit before requesting LFS objects.
- `audit_inputs.py` — verifies exact LFS SHA-256/size before DB/network parsing.
- `extract_feeder_features.py` — implements the frozen feature definitions; never selects a feeder.
- `registries/feeder_hazard_exposure_template.csv` — required FEMA-NFHL exposure input schema.
- `qualify_feeder_features.py` — verifies the extraction audit and cryptographically authorizes/blocks the feature matrix.
- `select_feeders.py` — refuses unqualified matrices; deterministic outcome-blind medoid selector.
- `build_reduced_case.py` — materializes only a previously frozen case manifest.

### Current audit artifacts
- `artifacts/input_audit_v1.json` — remote identity/materialization audit.
- `artifacts/feeder_features_v1.csv` — 61-row blocked matrix; predicates false and unknown feature values blank.
- `artifacts/feeder_selection_v1.json` — selection intentionally blocked; feeder IDs null.
- `artifacts/development_case_manifest_v1.json` — placeholder, not frozen.
- `artifacts/heldout_case_manifest_v1.json` — placeholder, not frozen.
- `artifacts/ci_source_materialization_attempt_v1.json` — records CI startup failure without attributing it to GreenEVT data.

## Commands after source bytes become available

```bash
# 1. Frozen acquisition
python acquire_level2.py --dest external/GreenEVT --method git

# 2. Exact-byte + schema/topology audit
python audit_inputs.py \
  --greenevt external/GreenEVT \
  --out artifacts/input_audit_runtime.json

# 3. Extract all non-hazard and supplied static-exposure features
python extract_feeder_features.py \
  --greenevt external/GreenEVT \
  --hazard-exposure artifacts/feeder_hazard_exposure_v1.csv \
  --out artifacts/feeder_features_runtime.csv \
  --audit-out artifacts/feeder_feature_extraction_audit_v1.json

# 4. Cryptographically qualify the matrix
python qualify_feeder_features.py \
  --features artifacts/feeder_features_runtime.csv \
  --extraction-audit artifacts/feeder_feature_extraction_audit_v1.json \
  --out artifacts/feeder_feature_qualification_v1.json

# 5. Only if step 4 returns QUALIFIED
python select_feeders.py \
  --features artifacts/feeder_features_runtime.csv \
  --feature-audit artifacts/feeder_feature_qualification_v1.json \
  --out artifacts/feeder_selection_runtime.json
```

## Preview

The deterministic preview remains software verification only:

```bash
python build_reduced_case.py --preview --out preview_case.json
python run_level2.py --case preview_case.json --out preview_results.json
```

Preview outputs are **not thesis evidence**.

## Hard claim boundary

A realistic synthetic run may establish reproducible model/mechanism differences. It may not establish H1 predictive superiority unless an independent qualified reference, exact primary metrics, V&V acceptance rules, UQ design, R1–R8 data qualification, train/test split, and repository authorization have all been frozen before target-result inspection.
