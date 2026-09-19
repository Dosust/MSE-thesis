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

### P0.3 Stage 6 v2.1 alignment — NEXT
- [ ] Add explicit effectiveness `E_fx(a_k)`.
- [ ] Add explicit efficiency `E_fy(a_k)` and evidence-supported resource vector.
- [ ] Keep `ΔR`, `E_fx`, `E_fy`, and `ΔJ_sus` distinct.
- [ ] Update H4 screening/decision semantics accordingly.
- [ ] Update Stage6→7 handoff.
- [ ] Issue Stage-6 aligned workbook/versioned amendment.
- [ ] Issue updated freeze/manifest.

### P0.4 Stage 7 v2.1 alignment
- [ ] Receive resilience + effectiveness + efficiency + sustainability + feasibility + uncertainty.
- [ ] Update Stage-7 workbook/version.
- [ ] Add `project/stage7/README.md`.
- [ ] Add searchable Stage-7 constitution/handoff summary.
- [ ] Add design-freeze record.
- [ ] Add finalization manifest.

## P1 — global control plane

### P1.1 Symbol/ontology registry
Fields:
`symbol | definition | type | unit | physical/epistemic/decision class | created stage | consuming stages | authority | assumptions | validity | legacy aliases`.

### P1.2 Handoff matrix
For every `I(k→k+1)`:
`producer | consumer | object | mandatory fields | units/types | uncertainty | validity | fail/block behavior | claim ceiling`.

### P1.3 H1–H5 master preregistration
Freeze the **schema** for:
`baseline | treatment | held constants | QOI | materiality | scenarios | UQ | VVUQ | support | not-support | not-tested`.

Data-dependent numerical values may remain DEFERRED.

### P1.4 Baseline/benchmark/reference registry
Enforce:
```math
\text{baseline}\neq\text{benchmark}\neq\text{reference}
\neq\text{validation evidence}\neq\text{ground truth}.
```

### P1.5 Empty final-case schema
```math
\mathcal S_{case}
=
(\mathcal G,Y_0,\theta,\eta,T,K,G_{rec},F_{unsafe},
\mathcal U_{feas},\mathcal A,\Omega).
```

### P1.6 Common scenario schema
One stable scenario ID propagated through Stages 3–7.

### P1.7 Global uncertainty/VVUQ
Use:
- aleatory;
- epistemic;
- model-form;
- numerical;
- requirement;
- value/normative uncertainty.

### P1.8 Global requirements/provenance
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
