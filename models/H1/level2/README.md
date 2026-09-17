# H1 Level 2 — Realistic Synthetic Spatial Twin

**Protocol:** `PROTOCOL_V1.md`  
**Machine contract:** `config/protocol_v1.json`  
**Current status:** `METHOD_FROZEN_INPUTS_OPEN`  
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

## Controlled workflow

```text
source acquisition/audit
-> pre-simulation feeder features
-> outcome-blind development/held-out selection
-> frozen case manifest
-> canonical dependency registry
-> coherent flood field + hazard-response maps
-> parameter freeze
-> matched M0/M1/M2 + ablations
-> V&V
-> UQ/sensitivity
-> independent-reference model-error test
-> later Stage-5 viability geometry
```

## Files

- `PROTOCOL_V1.md` — human-readable frozen scientific protocol.
- `config/protocol_v1.json` — machine-readable gate state.
- `config/source_manifest_v1.json` — authoritative data/method provenance.
- `config/protocol_status_v1.json` — generated current gate audit.
- `config/case_manifest_template.json` — non-executable template that becomes the sole authority for realistic case geometry after feeder selection.
- `registries/dependency_registry_v1.csv` — directed Level-2 dependencies under the canonical thesis dependency contract.
- `registries/parameter_registry_v1.csv` — parameter provenance/uncertainty registry.
- `registries/scenario_matrix_v1.csv` — matched comparison and ablation design.
- `registries/qoi_registry_v1.csv` — H1 primary families, secondary outcomes, and deferred `rho_g`.
- `registries/feeder_features_template.csv` — required inputs to outcome-blind feeder selection.
- `select_feeders.py` — deterministic pre-result feeder selector.
- `validate_protocol.py` — structural/freeze/authorization guard.
- `acquire_level2.py`, `audit_inputs.py`, `render_level2_map.py` — source acquisition, audit and visualization tooling.
- `build_reduced_case.py` — validates and materializes only a previously frozen case manifest; it no longer ranks/selects buses internally.
- `run_level2.py` — preview fixture and protocol-bound realistic-run gate.

## Commands

```bash
python acquire_level2.py --dest external/GreenEVT
python audit_inputs.py --greenevt external/GreenEVT --out input_audit.json
python select_feeders.py --features registries/feeder_features.csv --out feeder_selection.json
# after feeder selection + audited bus/road extraction, freeze a copy of config/case_manifest_template.json
python build_reduced_case.py --greenevt external/GreenEVT --case-manifest config/case_manifest_development.json --protocol config/protocol_v1.json --out case_bundle.json
python validate_protocol.py --protocol config/protocol_v1.json --root . --out config/protocol_status_v1.json
python run_level2.py --case case_bundle.json --protocol config/protocol_v1.json --out results.json
```

The deterministic preview remains available only for software verification:

```bash
python build_reduced_case.py --preview --out preview_case.json
python run_level2.py --case preview_case.json --out preview_results.json
```

Preview outputs are **not thesis evidence**.

## Hard claim boundary

A realistic synthetic run may establish reproducible model/mechanism differences. It may not establish H1 predictive superiority unless an independent qualified reference, exact primary metrics, V&V acceptance rules, UQ design, data qualification and repository authorization have all been frozen before result inspection.
