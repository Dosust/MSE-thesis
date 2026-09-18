# Stage 1 Generic Data Processing Layer

**Status:** ACTIVE IMPLEMENTATION SUPPORT  
**Authority:** `../../project/STAGE1_DATA_ABSTRACTION_AND_INGESTION_STANDARD_V1.md`  
**Structural contract:** `../../project/STAGE1_MATHEMATICAL_AND_ONTOLOGY_CONTRACT_V1.md`

## Purpose

This directory contains case-independent implementation scaffolds for ingesting heterogeneous Stage-1 data and converting them into the canonical structural representation.

```text
RAW SOURCE
   ↓
SOURCE ADAPTER
   ↓
STAGING
   ↓
CANONICAL INTERMEDIATE REPRESENTATION
   ↓
CLEAN / NORMALIZE / QA / PROVENANCE
   ↓
STAGE-1 STRUCTURAL HANDOFF
```

Austin-specific code belongs in `../austin_case/` and must consume this generic contract rather than redefine it.

## Required adapter behavior

Every adapter must expose:

```text
inspect
validate_source
parse
map_schema
normalize
emit_canonical
report_provenance
report_quality
```

Source-specific logic must stop at the canonical-representation boundary.

## Canonical outputs

Adapters may emit:

- source manifests;
- entities;
- intralayer edges;
- geometries;
- normalized attributes;
- service traceability rows;
- Stage-1 structural candidate relations;
- assumptions;
- QA records.

## Scientific guardrails

1. Raw data are immutable.
2. No silent imputation.
3. No silent geometry or topology repair.
4. Source CRS, units, temporal role, vintage, and provenance are preserved.
5. Every normalized value is traceable to a raw value and transformation.
6. Stage 1 cannot set `causal_dependency_accepted=true`.
7. A semisynthetic crosswalk is always labelled semisynthetic.
8. Case-specific thresholds/tolerances are configuration, not framework constants.

## Framework versus case

`G1_framework` tests whether this generic processing architecture is complete and works on controlled fixtures.

`G1_case(case_id)` tests whether a particular case source package can successfully instantiate it.

A case failure does not invalidate the generic framework.