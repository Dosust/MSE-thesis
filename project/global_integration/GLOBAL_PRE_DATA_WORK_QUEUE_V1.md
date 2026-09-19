# Global Pre-Data Integration Work Queue v1

**Date:** 2026-09-19  
**Objective:** reach a thesis-wide Stage 1→7 architecture freeze before inspecting case data.

## P0 — must complete first

### Q0.1 Authority control
- [x] Global authority/supersession map created.
- [ ] Future global master must carry authority status for every source object.
- [ ] Old H4/H5 meanings must be blocked from active experiment sheets.

### Q0.2 Stage-3 current constitution
Create:
- [ ] project/stage3/STAGE3_SCIENTIFIC_CONSTITUTION_V2.md
- [ ] normalized Stage2→3 input contract
- [ ] explicit Stage3→4 handoff contract
- [ ] Stage-3 output/claim object
- [ ] model-family selection schema
- [ ] state/input/output/QOI ontology
- [ ] time/hybrid/multirate schema
- [ ] generic scenario-template rule
- [ ] benchmark/VVUQ schema

No case-specific feeder, hazard, parameter or solver value is required.

### Q0.3 Stage-6 canonical alignment
Explicitly add:

~~~math
\mathcal E_{fx}(a_k)
~~~

for target attainment/effectiveness and:

~~~math
\mathcal E_{fy}(a_k)
~~~

for resource efficiency, separately from:

~~~math
\Delta\mathfrak R^{a_k}
\quad\text{and}\quad
\Delta\mathbf J_{sus}^{a_k}.
~~~

Update:
- [ ] Stage-6 scientific constitution
- [ ] Stage-6 master workbook
- [ ] Stage6→7 handoff
- [ ] Stage-6 freeze/manifest version

### Q0.4 Stage-7 canonical alignment
Update the Stage-7 input/decision architecture to receive:
- [ ] resilience;
- [ ] effectiveness;
- [ ] efficiency;
- [ ] sustainability;
- [ ] feasibility;
- [ ] uncertainty.

Add:
- [ ] project/stage7/README.md
- [ ] project/stage7/STAGE7_DESIGN_PROTOCOL_FREEZE_V1.md
- [ ] project/stage7/STAGE7_FINALIZATION_MANIFEST_V1.json

## P1 — global integration controls

### Q1.1 Global symbol/ontology registry
Required fields:
symbol; definition; type; units; physical/epistemic/decision class; creating stage; consuming stage; assumptions; validity domain; authority; legacy aliases.

### Q1.2 Global handoff matrix
For every I(k→k+1):
producer; consumer; exact object; mandatory fields; units/types; uncertainty; validity; claim ceiling; block/fail behavior.

### Q1.3 H1–H5 master preregistration
Compile:
- MODEL_EXPERIMENT_VALIDATION_MATRIX.md
- current v3 RQ/SO/H
- stage-specific protocols

Freeze the schema for baseline, treatment, held constants, QOI, materiality criterion, scenario domain, VVUQ and support/non-support/not-tested logic.

### Q1.4 Baseline/benchmark/reference registry

~~~math
\text{baseline}
\neq
\text{benchmark}
\neq
\text{reference}
\neq
\text{validation evidence}
\neq
\text{ground truth}.
~~~

### Q1.5 Empty final-case schema

~~~math
\mathcal S_{case}
=
(\mathcal G,Y_0,\theta,\eta,T,K,G_{rec},F_{unsafe},
\mathcal U_{feas},\mathcal A,\Omega).
~~~

### Q1.6 Common scenario schema
Define one stable scenario ID propagated through Stages 3–7.

### Q1.7 Global UQ/VVUQ
Use aleatory, epistemic, model-form, numerical, requirement and value/normative uncertainty.

## P2 — master artifact and freeze

- [ ] Build GLOBAL_STAGE1_7_MASTER_REGISTER_V1.xlsx.
- [ ] Run notation conflict audit.
- [ ] Run handoff completeness audit.
- [ ] Run hypothesis/comparator consistency audit.
- [ ] Run requirement-provenance audit.
- [ ] Run claim-evidence audit.
- [ ] Mark data-dependent fields DEFERRED.
- [ ] Create GLOBAL_STAGE1_7_DESIGN_FREEZE_V1.md.
- [ ] Create final manifest/hash record.

## Definition of pre-data done

~~~math
\boxed{
\text{PRE-DATA DONE}
\iff
\text{no unresolved design contradiction remains}
}
~~~

Data-dependent values may remain open/deferred.
