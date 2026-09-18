# Stage 1 Data Abstraction, Ingestion, Cleaning, and Validation Standard v2.0

**Status:** **PASS — FROZEN**  
**Date:** 2026-09-18  
**Authority:** `STAGE1_MATHEMATICAL_AND_ONTOLOGY_CONTRACT_V2.md` + `stage1_v2/Stage1_Evidence_and_Ontology_Register_v2_FINAL.md`

## 1. Governing architecture

~~~text
RAW -> STAGING -> CANONICAL -> DERIVED -> RELEASE
~~~

The framework is case-independent. Source-specific semantics terminate at the canonical-representation boundary.

## 2. Supported source classes

Vector geospatial, raster geospatial, tabular, graph/network, power-system model, transport network, time-indexed records, API snapshots, document metadata, normative authority, and explicitly typed other sources.

## 3. Canonical intermediate representation

**CIR-1 Source manifest:** source/provider/retrieval/native format/CRS/units/time/vintage/SHA-256/adapter/access/authority metadata.

**CIR-2 Semantic entities:** identity, layer, type, geometry, engineering functions, state schema, service roles, resolution, evidence references, validity, quality and optional owner/operator/regulator/supplier/authority roles.

**CIR-3 Intralayer edges:** typed same-layer topology, directionality, semantics and provenance.

**CIR-4 Geometry:** original/canonical geometry and CRS, transform, validity and repair log.

**CIR-5 Attributes:** raw/canonical values and units, normalization rule and quality.

**CIR-6 Service/requirement traceability:** entity → function → service → requirement → measure → threshold/rule.

**CIR-7 Stage-1 relation records:** implements the v2 core relation object and secondary metadata.

~~~text
relation_id
record_level
participants
layer_pair
scope
structural_admissibility
interface_semantics
exchange_semantics
direction
candidate_mechanism
mechanism_status
activation_context
evidence_status
evidence_refs
structural_existence
case_connection_status
strength_status
causal_dependency_accepted
metadata.hierarchy_orientation
metadata.path
metadata.mediator_path
metadata.arity
metadata.resolution_level
metadata.admission_basis
metadata.evidence_confidence
metadata.normative_admissibility
provenance_status
~~~

**CIR-8 Assumptions:** statement, reason, evidence, consequence, sensitivity test.

**CIR-9 QA ledger:** object, test/version, result, severity, value, threshold, message.

**CIR-10 Authority/requirements:** authority type, jurisdiction, edition/version, effective period, status, clause, applicability, affected object, requirement/service/measure/unit/rule and verification state.

## 4. Cleaning/normalization rules

No silent imputation. Preserve raw identifiers. Record unit conversion. Require declared CRS. Geometry/topology repair is explicit and logged. Retrieval date, source vintage, validity period and scenario time are distinct. Aggregation/disaggregation is derived and provenance-controlled.

## 5. Relation governance

~~~math
\boxed{I_e^{\rm struct}\neq w_e\neq q_e^{\rm evid}.}
~~~
~~~text
strength_status = NOT_ESTIMATED_STAGE1
causal_dependency_accepted = false
~~~

Templates use record_level=MECHANISM_TEMPLATE and structural_existence=TEMPLATE_ONLY. Case relations use record_level=CASE_RELATION and structural existence CANDIDATE, VERIFIED_STRUCTURAL, UNRESOLVED or EXCLUDED.

A verified structural case relation requires case structural evidence; prior literature, standards or operator documentation alone cannot create VERIFIED_STRUCTURAL status.

A MEDIATED path must identify mediators. A PAIRWISE relation has exactly two participants. Higher-order records are permitted only when pairwise decomposition loses mechanism meaning. CONTEXT records represent shared environment/common cause and cannot be promoted to P→T/T→P causality.

## 6. Evidence confidence

Default evidence confidence is UNSCORED. Numeric confidence requires an auditable scoring/calibration method and provenance.

## 7. Normative applicability

A requirement outside its jurisdiction or technical scope cannot become a model constraint. Normative conformity cannot create causal acceptance.

## 8. Adapter contract

~~~text
inspect
validate_source
parse
map_schema
normalize
emit_canonical
report_provenance
report_quality
~~~

## 9. Framework verification

Fixtures must cover schema/source classes, semantic entities, templates vs case relations, P→T, T→P, INTRA, CONTEXT/common cause, path/arity controls, causal restraint, no Stage-1 strength estimation, confidence discipline, resolution, identifiers, hashes, CRS/units, missingness, geometry/topology QA, temporal role and authority applicability.

## 10. Framework versus case

~~~math
\boxed{G_1^{\rm framework}\neq G_1^{\rm case}(c).}
~~~

## 11. Freeze state

This generic data contract is part of the frozen Stage-1 framework. Source-specific adapters and case configurations may evolve only if they continue to conform to this contract; semantic changes to CIR objects or Stage-1 relation governance require explicit amendment/unfreeze.
