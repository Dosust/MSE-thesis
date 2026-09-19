# Global Pre-Data Work Queue v2

**Date:** 2026-09-19  
**Basis:** deep repository audit of current Stage 1–7 authorities.

## P0 — repair before integration

### P0.1 Authority control
- [x] Global authority/supersession map exists.
- [x] Current H4/H5 meanings identified.
- [x] Legacy dependency notation translation authority identified.
- [x] Repository authority-drift audit completed; carry the verified classifications into the global master workbook.

Authority drift cleanup closure: **PASS — 2026-09-19**. No obsolete H4/H5 file may govern active work; legacy Stage-3 notation is explicitly quarantined.

### P0.2 Stage 3 normalization — COMPLETE
- [x] Create `project/stage3/STAGE3_SCIENTIFIC_CONSTITUTION_V2.md`.
- [x] Define active-notation Stage2→3 input contract.
- [x] Define Stage3 state/input/output/QOI ontology.
- [x] Define model-family selection schema.
- [x] Freeze time/hybrid/multirate semantics at design level.
- [x] Define generic scenario-template schema.
- [x] Define Stage3 benchmark/VVUQ schema.
- [x] Define Stage3→4 handoff.
- [x] Define Stage3 claim ceiling.
- [x] Freeze/version the Stage3 v2 constitution.

Stage 3 design normalization closure: **PASS — DESIGN/PROTOCOL ONLY; empirical Stage 3 remains NOT TESTED.**

### P0.3 Stage 6 v2.1 alignment — COMPLETE
- [x] Add explicit effectiveness `E_fx(a_k)`.
- [x] Add explicit efficiency `E_fy(a_k)` and evidence-supported resource vector.
- [x] Keep `ΔR`, `E_fx`, `E_fy`, and `ΔJ_sus` distinct.
- [x] Update H4 performance reporting while preserving canonical primary H4 eligibility `A_H4 = A_R+`.
- [x] Update Stage6→7 handoff.
- [x] Issue Stage-6 aligned workbook/versioned amendment.
- [x] Issue updated freeze/manifest.

Stage 6 v2.1 alignment closure: **PASS — DESIGN/PROTOCOL V2; empirical Stage 6 remains DEFERRED / H4 NOT TESTED.**

### P0.4 Stage 7 v2.1 alignment — COMPLETE
- [x] Receive resilience + effectiveness + efficiency + sustainability + feasibility + uncertainty.
- [x] Generate and verify Stage-7 workbook v2; exact byte identity recorded.
- [x] Add `project/stage7/README.md`.
- [x] Add searchable Stage-7 constitution/handoff and decision protocols.
- [x] Add design-freeze record.
- [x] Add finalization manifest.

Stage 7 v2.1 alignment closure: **PASS — DESIGN/PROTOCOL V2; empirical Stage 7 remains DEFERRED / H5 NOT TESTED.**

## P1 — global control plane

### P1.0 Governance synchronization — COMPLETE
- [x] Issue PRE_DATA_STAGE1_7_INTEGRATION_AUDIT_V2.md.
- [x] Update global integration README.
- [x] Reconcile current Stage 3/6/7 design status.

### P1.1 Symbol/ontology registry — COMPLETE
- [x] Build GLOBAL_SYMBOL_AND_ONTOLOGY_REGISTRY_V1.md.
- [x] Disambiguate cross-stage symbol collisions.
- [x] Quarantine legacy dependency primitive.

Fields:
`symbol | definition | type | unit | physical/epistemic/decision class | created stage | consuming stages | authority | assumptions | validity | legacy aliases`.

### P1.2 Handoff matrix — COMPLETE
- [x] Build GLOBAL_STAGE_HANDOFF_MATRIX_V1.md.
- [x] Build GLOBAL_CROSS_STAGE_NOTATION_AND_HANDOFF_NORMALIZATION_V1.md.
- [x] Resolve Stage4→5 physical-truth lineage.
- [x] Resolve Stage5→6 producer/consumer mismatch losslessly.
- [x] Run P1 backbone audit: 20/20 PASS.

For every `I(k→k+1)`:
`producer | consumer | object | mandatory fields | units/types | uncertainty | validity | fail/block behavior | claim ceiling`.

### P1.3 H1–H5 master preregistration — COMPLETE
- [x] Create `GLOBAL_H1_H5_MASTER_PREREGISTRATION_V1.md`.
- [x] Freeze the 13-field master object for H1–H5.
- [x] Preserve canonical baseline/treatment/comparator semantics.
- [x] Preserve current H1 mechanism-readiness restrictions.
- [x] Keep unresolved H2/H3/H4/H5 metrics/thresholds DEFERRED.
- [x] Standardize final adjudication as SUPPORTED / NOT SUPPORTED / NOT TESTED.
- [x] Run preregistration audit: 32/32 PASS.

### P1.4 Baseline/benchmark/reference registry — COMPLETE
- [x] Create GLOBAL_BASELINE_BENCHMARK_REFERENCE_REGISTRY_V1.md.
- [x] Define global baseline/comparator subtypes.
- [x] Separate benchmark problem, verification fixture, reference solution, reference calculation and validation evidence.
- [x] Separate synthetic truth from empirical ground truth.
- [x] Type Stage-3/5/6/7 terminal B(k,3) objects as QUALIFIED_CASE, not synthetic benchmark.
- [x] Type H1–H5 baseline roles consistently with P1.3.
- [x] Prohibit unnamed reference roles in future confirmatory documentation.
- [x] Run P1.4 classification audit: 38/38 PASS.

### P1.5 Empty final-case schema — COMPLETE
- [x] Create GLOBAL_FINAL_CASE_SCHEMA_V1.md.
- [x] Create Draft 2020-12 machine schema.
- [x] Create field dictionary for all eleven case objects.
- [x] Create provenance CSV ledger.
- [x] Create admissibility gate matrix.
- [x] Bind P1.4 reference classes.
- [x] Create uncertainty template.
- [x] Preserve all case values as DEFERRED.
- [x] Run combined semantic/machine audit: 58/58 PASS.
```math
\mathcal S_{case}
=
(\mathcal G,Y_0,\theta,\eta,T,K,G_{rec},F_{unsafe},
\mathcal U_{feas},\mathcal A,\Omega).
```

### P1.6 Common scenario schema — COMPLETE
- [x] Separate immutable root scenario, experimental arm, executable run and result identity.
- [x] Create GLOBAL_SCENARIO_ID_AND_PROPAGATION_SCHEMA_V1.md.
- [x] Create Draft 2020-12 machine schema.
- [x] Create scenario field dictionary.
- [x] Create Stage 3→7 propagation matrix.
- [x] Create matched-comparison/randomness protocol.
- [x] Create empty root and seed-manifest templates.
- [x] Freeze H1–H5 matched-field/change-field semantics.
- [x] Preserve scenario-frequency ≠ probability.
- [x] Run combined scenario audit: 52/52 PASS.

### P1.7 Global uncertainty/VVUQ — COMPLETE
- [x] Create GLOBAL_UNCERTAINTY_VVUQ_CONTROL_V1.md.
- [x] Create Draft 2020-12 machine schema.
- [x] Separate uncertainty nature from uncertainty source.
- [x] Freeze probability/dependence/reducibility semantics.
- [x] Create Stage/H1–H5 uncertainty propagation matrix.
- [x] Create global VVUQ gate matrix.
- [x] Create verification/validation/acceptance protocol.
- [x] Create sensitivity/convergence/decision-stability protocol.
- [x] Create credibility/claim-ceiling matrix.
- [x] Create empty uncertainty, VVUQ-activity and context-of-use registers.
- [x] Run combined P1.7 audit: 84/84 PASS.

### P1.8 Global requirements/provenance — NEXT
Unify service, physical, resilience, sustainability and decision constraints without promoting research assumptions into authoritative requirements.

### P1.9 Claim-evidence-result matrix
Every intended thesis conclusion must have:
`claim | stage | evidence/test | validity domain | result status | allowed wording`.

## P2 — master artifact and freeze
- [ ] Build `GLOBAL_STAGE1_7_MASTER_REGISTER_V1.xlsx`.
- [ ] Run notation conflict audit.
- [ ] Run handoff completeness audit.
- [ ] Run hypothesis/comparator consistency audit.
- [ ] Run requirement-provenance audit.
- [ ] Run claim-evidence audit.
- [ ] Mark every case/data-dependent field DEFERRED.
- [ ] Create `GLOBAL_STAGE1_7_DESIGN_FREEZE_V1.md`.
- [ ] Create manifest + SHA-256 record.

## Definition of pre-data complete

```math
\boxed{
\text{PRE-DATA COMPLETE}
\iff
\text{all design contradictions are closed}
}
```

Empirical values, datasets, calibration parameters and confirmatory outcomes are allowed to remain unresolved until the subsequent data-qualification phase.
