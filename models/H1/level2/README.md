# H1 Level 2 — Realistic Synthetic Spatial Twin

**Protocol:** `PROTOCOL_V1.md`  
**Feature semantics:** `FEEDER_FEATURE_SPECIFICATION_V1.md`  
**Transport recovery:** `TRANSPORT_SOURCE_RECOVERY_V1.md`  
**NFHL selection exposure:** `NFHL_SELECTION_EXPOSURE_V1.md`  
**Machine contract:** `config/protocol_v1.json`  
**Current status:** `METHOD_FEATURE_AND_RECOVERY_SEMANTICS_FROZEN_SOURCE_DATA_OPEN`  
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
-> GREENEVT COMMIT FROZEN
-> EXACT CRITICAL LFS OBJECT IDENTITIES FROZEN
-> 21-SUBSTATION / 61-FEEDER INVENTORY COMPLETE
-> PUBLISHED GREENEVT TRANSPORT BOUNDS/INVARIANTS FROZEN
-> TRANSPORT SOURCE-RECOVERY METHOD FROZEN
-> FEMA NFHL SELECTION-EXPOSURE ACQUISITION METHOD FROZEN
-> BLOCKED: CRITICAL GREENEVT LFS PAYLOADS NOT MATERIALIZED IN CURRENT RUNTIME
-> OPEN: EFFECTIVE FEMA NFHL SNAPSHOT NOT YET MATERIALIZED
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

## Published transport recovery invariants

GreenEVT reports the transportation network as an OpenStreetMap import created with SUMO `osmWebWizard` over the rectangle:

```text
south = 35.894145
west  = -80.198958
north = 36.410277
east  = -79.157255
```

and reports:

```text
SUMO nodes              50,109
SUMO edges             118,289
signalized junctions       914
road length             28,216 km  [as published]
lane length             30,625 km  [as published]
```

`TRANSPORT_SOURCE_RECOVERY_V1.md` allows a separately labeled reconstruction candidate when original bytes are inaccessible. Matching aggregate invariants can support only `GREENEVT_BENCHMARK_MATCH_CANDIDATE`; it **cannot** establish byte- or edge-level equivalence.

## Controlled workflow

```text
source acquisition
-> exact-byte audit OR explicitly labeled source-recovery branch
-> UDS schema/crosswalk + SUMO topology audit
-> preregistered feeder feature extraction
-> effective FEMA-NFHL snapshot + all-61 coverage qualification
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

The case-selection exposure feature is

```math
E_H=\tfrac12(e_P+e_T),
```

where `e_P` is the fraction of feeder buses in the effective FEMA Special Flood Hazard Area and `e_T` is the fraction of selected road length in that area. `E_H` is **not** the later HEC-RAS pluvial forcing, a fragility function, failure probability, or resilience score.

## Important files

### Scientific controls
- `PROTOCOL_V1.md` — frozen Level-2 scientific protocol.
- `FEEDER_FEATURE_SPECIFICATION_V1.md` — exact pre-data feature semantics.
- `TRANSPORT_SOURCE_RECOVERY_V1.md` — recovery/equivalence rules when the original SUMO LFS payload is unavailable.
- `NFHL_SELECTION_EXPOSURE_V1.md` — static FEMA selection-exposure protocol.
- `config/protocol_v1.json` — machine-readable protocol.
- `config/protocol_status_v1.json` — current gate state.
- `config/source_manifest_v1.json` — source/method provenance and published validation invariants.
- `registries/dependency_registry_v1.csv` — canonical directed dependencies.
- `registries/parameter_registry_v1.csv` — parameter provenance/uncertainty.
- `registries/scenario_matrix_v1.csv` — matched scenarios and ablations.
- `registries/qoi_registry_v1.csv` — H1 outcome families and secondary QOIs.

### Source and spatial-case pipeline
- `acquire_level2.py` — checks out the exact frozen GreenEVT commit before requesting LFS objects.
- `audit_inputs.py` — verifies exact LFS SHA-256/size before DB/network parsing.
- `validate_transport_candidate.py` — audits reconstructed SUMO candidates against GreenEVT published invariants; never authorizes feeder selection itself.
- `fetch_nfhl_sfha.py` — reproducibly acquires effective FEMA SFHA polygons over the frozen GreenEVT rectangle.
- `extract_feeder_features.py` — implements the frozen feature definitions; never selects a feeder.
- `registries/feeder_hazard_exposure_template.csv` — required FEMA-NFHL exposure input schema.
- `qualify_feeder_features.py` — verifies the extraction audit and cryptographically authorizes/blocks the feature matrix.
- `select_feeders.py` — refuses unqualified matrices; deterministic outcome-blind medoid selector.
- `build_reduced_case.py` — materializes only a previously frozen case manifest.

### Current audit artifacts
- `artifacts/input_audit_v1.json` — source identity/materialization audit.
- `artifacts/feeder_source_inventory_v1.csv` — raw 61-feeder source discovery inventory.
- `artifacts/feeder_features_v1.csv` — 61-row blocked matrix; predicates false and unknown feature values blank.
- `artifacts/feeder_selection_v1.json` — selection intentionally blocked; feeder IDs null.
- `artifacts/development_case_manifest_v1.json` — placeholder, not frozen.
- `artifacts/heldout_case_manifest_v1.json` — placeholder, not frozen.
- `artifacts/ci_source_materialization_attempt_v1.json` — CI startup failure without attribution to GreenEVT data.
- `artifacts/source_recovery_attempt_v1.json` — exact record of download/materialization attempts and recovery status.

## Commands when source access is available

```bash
# 1. Preferred exact GreenEVT acquisition
python acquire_level2.py --dest external/GreenEVT --method git

# 2. Exact-byte + schema/topology audit
python audit_inputs.py \
  --greenevt external/GreenEVT \
  --out artifacts/input_audit_runtime.json

# 3. Independently freeze effective FEMA SFHA geometry
python fetch_nfhl_sfha.py \
  --out artifacts/nfhl_sfha_greenevt_aoi_v1.geojson \
  --metadata-out artifacts/nfhl_sfha_greenevt_aoi_v1.metadata.json

# 4. After all 61 feeder exposure values are qualified, extract the complete matrix
python extract_feeder_features.py \
  --greenevt external/GreenEVT \
  --hazard-exposure artifacts/feeder_hazard_exposure_v1.csv \
  --out artifacts/feeder_features_runtime.csv \
  --audit-out artifacts/feeder_feature_extraction_audit_v1.json

# 5. Cryptographically qualify the matrix
python qualify_feeder_features.py \
  --features artifacts/feeder_features_runtime.csv \
  --extraction-audit artifacts/feeder_feature_extraction_audit_v1.json \
  --out artifacts/feeder_feature_qualification_v1.json

# 6. Only if step 5 returns QUALIFIED
python select_feeders.py \
  --features artifacts/feeder_features_runtime.csv \
  --feature-audit artifacts/feeder_feature_qualification_v1.json \
  --out artifacts/feeder_selection_runtime.json
```

If the original SUMO object remains unavailable, any reconstructed candidate must first be audited separately:

```bash
python validate_transport_candidate.py \
  --network reconstructed/greensboro.net.xml \
  --out artifacts/transport_reconstruction_validation.json
```

That audit does not make the reconstructed object equivalent to the original GreenEVT bytes.

## Preview

The deterministic preview remains software verification only:

```bash
python build_reduced_case.py --preview --out preview_case.json
python run_level2.py --case preview_case.json --out preview_results.json
```

Preview outputs are **not thesis evidence**.

## Hard claim boundary

A realistic synthetic run may establish reproducible model/mechanism differences. It may not establish H1 predictive superiority unless an independent qualified reference, exact primary metrics, V&V acceptance rules, UQ design, R1–R8 data qualification, train/test split, and repository authorization have all been frozen before target-result inspection.
