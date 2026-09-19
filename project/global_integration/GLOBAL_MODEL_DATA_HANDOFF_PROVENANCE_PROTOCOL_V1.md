# Global Model/Data Handoff Provenance Protocol v1

**Status:** CANONICAL CROSS-MODEL INFORMATION-HANDOFF CONTROL  
**Effective date:** 2026-09-19  
**Scope:** all material data/result transfers among Stage 1–7 computational, estimation, resilience, sustainability and decision modules  
**Scientific owner:** P1.11.2 information architecture  
**Empirical effect:** NONE

## 1. Purpose

This protocol makes computational orchestration scientifically auditable without confusing software links with physical interdependencies.

~~~math
\boxed{
\text{physical coupling}
\neq
\text{software coupling},
\qquad
\text{data handoff}
\neq
\text{causal proof}.
}
~~~

## 2. Handoff record

Each material transfer receives an immutable \`HID\`.

Required fields:

~~~text
handoff_id
producer_stage
producer_model
producer_model_version
producer_code_hash
producer_run_id
producer_result_id
source_object
source_variable
source_unit
source_spatial_support
source_temporal_support
source_semantics
transformation_id
transformation_description
spatial_mapping_rule
temporal_mapping_rule
semantic_mapping_rule
unit_conversion_rule
uncertainty_input_ids
uncertainty_propagation_rule
receiver_stage
receiver_model
receiver_model_version
target_object
target_variable
target_unit
target_spatial_support
target_temporal_support
scenario_root_id
experimental_arm_id
run_id
data_version
requirement_baseline_id
vvuq_record_id
validity_domain
claim_ceiling
gate_status
provenance_record
created_at
supersedes_handoff_id
~~~

## 3. Admission gate

~~~math
\boxed{
G_H
=
G_{identity}
\land
G_{units}
\land
G_{space}
\land
G_{time}
\land
G_{semantics}
\land
G_U
\land
G_{version}
\land
G_{validity}
\land
G_{provenance}.
}
~~~

If any mandatory gate fails, the transfer is BLOCKED for confirmatory use.

## 4. Alignment rule

Alignment operations may include:
- coordinate transformation;
- spatial join;
- network-location mapping;
- interpolation;
- aggregation/disaggregation;
- temporal resampling;
- lag/delay application;
- unit conversion;
- categorical/ontology translation.

Every transformation must preserve its own identifier and parameters.

No transformation may silently create precision or certainty not present in the source.

## 5. Uncertainty rule

Transformations must either:
1. propagate registered uncertainty;
2. add/register transformation uncertainty; or
3. explicitly justify why uncertainty is unaffected.

~~~math
\boxed{
\text{provenance}
\neq
\text{uncertainty quantification}.
}
~~~

Both are required where scientifically applicable.

## 6. Versioning rule

A change in any of the following creates a new handoff version or ID:
- producer model/version;
- source variable semantics;
- alignment/transformation rule;
- receiver semantics;
- units;
- scenario/run lineage;
- uncertainty treatment;
- validity domain.

Historical records remain immutable.

## 7. Confirmatory trace

A confirmatory result must be reverse-traceable:

~~~math
\boxed{
ResultID
\leftrightarrow
RunID
\leftrightarrow
HID
\leftrightarrow
SourceResult/DataVersion
\leftrightarrow
Model/CodeVersion
\leftrightarrow
ScenarioID
\leftrightarrow
RequirementBaseline
\leftrightarrow
VVUQRecord.
}
~~~

## 8. Examples of prohibited shortcuts

BLOCKED:
- "SUMO supplied traffic" with no variable/unit/run/version.
- nearest feeder assigned to signal with no proxy status.
- yearly demand copied into an hourly solver without temporal mapping rule.
- coordinate join performed with unknown CRS.
- interpolation treated as measured truth.
- result plot used as validation evidence.
- database edge labeled as causal dependency without Stage-2 qualification.
- output copied between modules without uncertainty lineage.

## 9. Relationship to existing controls

This protocol complements, and does not replace:
- \`GLOBAL_STAGE_HANDOFF_MATRIX_V1.md\`;
- \`GLOBAL_UNCERTAINTY_VVUQ_CONTROL_V1.md\`;
- \`GLOBAL_REQUIREMENTS_PROVENANCE_CONTROL_V1.md\`;
- \`GLOBAL_SCENARIO_ID_AND_PROPAGATION_SCHEMA_V1.md\`;
- \`GLOBAL_CLAIM_EVIDENCE_RESULT_CONTROL_V1.md\`.

Stage handoffs define scientific producer/consumer semantics.

This protocol defines the computational/data lineage required when those semantics are executed.
