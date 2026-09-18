# Stage 1 Data Abstraction, Ingestion, Cleaning, and Validation Standard v1.1

**Status:** FINAL METHODOLOGICAL STANDARD — READY FOR STAGE-1 FRAMEWORK FREEZE  
**Date:** 2026-09-18  
**Scope:** case-independent Stage-1 structural data processing for coupled Power–Transportation infrastructure  
**Authority:** `STAGE1_MATHEMATICAL_AND_ONTOLOGY_CONTRACT_V1.md`

## 1. Governing principle

Stage 1 must not be designed around Austin, SMART-DS, TxDOT, SUMO, OpenDSS, one GIS vendor, or one file format.

The governing architecture is:

```math
\boxed{
\text{heterogeneous source data}
\rightarrow
\text{source adapter}
\rightarrow
\text{canonical structural representation}
\rightarrow
\text{cleaning/normalization}
\rightarrow
\text{QA/provenance}
\rightarrow
Z_1^{\rm impl}.
}
```

A case study is admissible only if its data can be mapped into the canonical representation without violating semantics or hiding uncertainty.

## 2. Separation of framework closure and case execution

Two gates are mandatory and independent:

```math
\boxed{
G_{1}^{\rm framework}
\neq
G_{1}^{\rm case}.
}
```

`G1_framework` evaluates whether the generic Stage-1 ontology, schemas, adapters, cleaning rules, QA rules, provenance rules, and handoff are complete.

`G1_case` evaluates whether a particular case dataset successfully instantiates those contracts.

Therefore:

```math
\boxed{
G_{1}^{\rm framework}=\mathrm{PASS}
\not\Rightarrow
G_{1}^{\rm case}=\mathrm{PASS}.
}
```

and a failed/blocked Austin instantiation must not invalidate the generic Stage-1 framework.

## 3. Supported source classes

Stage 1 must accept any source that can be deterministically mapped into the canonical structural representation.

| Source class | Examples | Stage-1 role |
|---|---|---|
| vector geospatial | Shapefile, GeoPackage, GeoJSON | assets, roads, boundaries, signals, chargers |
| raster geospatial | GeoTIFF, gridded surfaces | spatial support, co-exposure, contextual masks |
| tabular | CSV, TSV, Parquet, spreadsheets | asset registries, attributes, crosswalks |
| graph/network | GraphML, JSON graph, edge/node tables | explicit topology |
| power-system model | OpenDSS, GridLAB-D, CIM-derived exports, MATPOWER-like tables, SMART-DS packages | P entities/topology/attributes |
| transport-model network | SUMO net, OSM-derived networks, GIS road centerlines | T entities/topology |
| time-indexed records | CSV/Parquet/API snapshots | vintage, asset status, structural availability |
| API snapshot | REST/JSON downloaded and hashed | reproducible source snapshot |
| document/manual metadata | operator manuals, asset catalogs | prior relationship class / interface metadata only |
| normative/authority source | statute, regulation, code, standard, utility/agency procedure | jurisdiction, applicability, requirements, engineering admissibility |

No source format is scientifically privileged. Source semantics and provenance determine admissibility.

## 4. Immutable data zones

Every dataset must move through five zones:

```text
RAW -> STAGING -> CANONICAL -> DERIVED -> RELEASE
```

### RAW
- immutable bytes exactly as obtained;
- cryptographic hash;
- retrieval/access metadata;
- no edits.

### STAGING
- parsed representation;
- source-native field names retained;
- parser diagnostics;
- no semantic harmonization yet.

### CANONICAL
- mapped to Stage-1 typed entities, edges, geometry, services, and provenance;
- units, CRS, temporal semantics, identifiers normalized;
- raw values preserved alongside normalized values where transformation occurred.

### DERIVED
- topology repair products;
- retrospective subsets;
- semisynthetic crosswalks;
- candidate structural relations;
- aggregations.

### RELEASE
- only data objects that pass the declared Stage-1 QA gate;
- complete provenance chain to RAW.

## 5. Canonical intermediate representation (CIR)

Every source adapter must emit one or more of the following canonical tables/objects.

### CIR-1 — Source manifest

```text
source_id
source_type
provider
retrieval_uri_or_reference
retrieved_at
license_or_access
native_format
native_crs
native_units
temporal_semantics
source_vintage
sha256
adapter_id
adapter_version
authority_type
jurisdiction
document_id
edition_or_version
effective_from
effective_to
status
applicability
```

### CIR-2 — Entity table

```text
entity_id
raw_entity_id
layer
entity_type
source_id
geometry_id
state_schema
service_roles
valid_from
valid_to
quality_status
```

### CIR-3 — Intralayer edge table

```text
edge_id
raw_edge_id
layer
source_entity
target_entity
edge_semantics
directionality
source_id
quality_status
```

### CIR-4 — Geometry table

```text
geometry_id
geometry_type
geometry
canonical_crs
source_crs
transform_operation
geometry_validity
repair_log
```

### CIR-5 — Attribute/value table

```text
entity_or_edge_id
attribute_name
raw_value
raw_unit
canonical_value
canonical_unit
normalization_rule
quality_flag
```

### CIR-6 — Service traceability table

```text
entity_id
service_id
structural_role
evidence_status
```

### CIR-7 — Structural candidate relation table

```text
relation_id
source_entity
target_entity
relation_status
asset_crosswalk
interface_hardware
spatial_relation
access_geometry
geographic_coexposure
structural_predicate_pass
provenance_status
causal_dependency_accepted=false
```

### CIR-8 — Assumption register

```text
assumption_id
statement
reason
evidence
consequence
sensitivity_test
```

### CIR-9 — QA ledger

```text
qa_id
object_id
test_name
test_version
result
severity
measured_value
threshold
message
```

### CIR-10 — Authority and requirements register

```text
authority_id
authority_type
authority_name
jurisdiction
document_id
edition_or_version
effective_from
effective_to
status
clause_or_locator
applicability
affected_entity_type
affected_interface_type
requirement_id
service_id
requirement_type
measure
unit
threshold_or_rule
verification_status
source_id
```

CIR-10 records normative applicability and requirement provenance. It does not encode causal mechanisms.

## 6. Adapter contract

Every source-specific adapter must implement the same logical interface:

```text
inspect(source)
validate_source(source)
parse(source)
map_schema(parsed)
normalize(mapped)
emit_canonical(normalized)
report_provenance()
report_quality()
```

An adapter may understand source-specific details, but downstream Stage-1 logic may consume only canonical objects.

Thus:

```math
\boxed{
\text{source-specific semantics belong upstream of the CIR boundary}.
}
```

## 7. Mandatory cleaning and normalization rules

### 7.1 Identifiers
- preserve raw identifiers;
- create stable canonical identifiers;
- no identifier reuse across entity types;
- crosswalks must be explicit and versioned.

### 7.2 Missing values
- no silent imputation;
- distinguish unavailable, not applicable, censored, unknown, and parse failure where possible;
- any imputation is a derived product with method and uncertainty recorded.

### 7.3 Units
- preserve raw value/unit;
- convert only through explicit deterministic transformations;
- record target unit and transformation.

### 7.4 Coordinate reference systems
- source CRS must be declared or source is BLOCKED for spatial use;
- canonical CRS is case-declared;
- transformation operation must be recorded;
- no distance or area calculation in inappropriate angular coordinates.

### 7.5 Geometry
- geometry validity tested before use;
- repair is never silent;
- original geometry retained;
- repair method and before/after diagnostics recorded.

### 7.6 Topology
- snapping, simplification, node merging, island removal, direction repair, and connectivity repair are derived operations;
- tolerances must be declared;
- topology repair must be sensitivity-tested when it can alter conclusions.

### 7.7 Duplicates
- distinguish byte duplicates, identifier duplicates, semantic duplicates, and spatial near-duplicates;
- deduplication rule must be deterministic and auditable.

### 7.8 Temporal semantics
- every source must declare whether it is contemporaneous, retrospective, persistent/static, proxy, or synthetic;
- `valid_from`, `valid_to`, source vintage, and scenario role must not be conflated;
- mixed vintages require an explicit temporal compatibility rule.

### 7.9 Uncertainty and quality
- uncertain location, identity, crosswalk, and attribute values remain uncertain;
- quality is represented explicitly rather than hidden through cleaning;
- use PASS / CONDITIONAL / BLOCKED / EXCLUDE at object or source level as appropriate.

### 7.10 Normative and jurisdictional applicability
- laws, regulations, standards, utility procedures, and agency requirements are typed separately from scientific literature;
- edition/version, status, effective period, jurisdiction, clause/locator, and applicability are preserved;
- a requirement outside its jurisdiction or technical scope cannot be silently applied;
- ownership, operating authority, regulator, utility/supplier, and transport authority are separate attributes where relevant;
- normative conformity cannot set `causal_dependency_accepted=true`;
- superseded requirements remain traceable but cannot be treated as current without an explicit historical-use justification.

## 8. Domain-specific adapter families

### 8.1 Power adapter

Must be able to map source-specific constructs to canonical:

```text
bus/node
line/branch
transformer
load
generator/DER/storage
switch/protection device when retained
substation/feeder hierarchy when available
```

while preserving native electrical semantics.

### 8.2 Transportation adapter

Must map:

```text
road node/intersection
road link/segment
direction
functional class
capacity/speed attributes when structurally needed
signal
charger/charging facility
repair destination/access point
```

while preserving directed traversability semantics.

### 8.3 Supporting-domain adapter

Information and Organization sources may be structurally represented as typed registries rather than forced into physical geometry when geometry is not meaningful.

## 9. Case-independent validation tests

The generic framework must pass synthetic/fixture tests independent of Austin:

| Test | Requirement |
|---|---|
| schema conformance | all canonical objects validate |
| round-trip provenance | every RELEASE object traces to RAW source |
| identifier stability | repeated ingestion yields same canonical IDs under same configuration |
| CRS normalization | known fixture transforms to expected coordinates within tolerance |
| geometry repair audit | invalid geometry is detected and repaired only when configured |
| topology preservation | simple reference network retains known connectivity/direction |
| missingness preservation | null categories survive ingestion without silent filling |
| unit normalization | known unit fixtures convert exactly/within numerical tolerance |
| temporal-role preservation | contemporaneous/proxy/synthetic roles remain distinct |
| authority metadata | jurisdiction, edition/status, effective period and applicability survive ingestion |
| authority applicability | a nonapplicable requirement does not become a model constraint |
| normative/causal separation | standards conformity cannot create a causal dependency |
| causal guardrail | Stage-1 schema cannot set `causal_dependency_accepted=true` |

These tests define framework readiness independently of any case-study dataset.

## 10. Case configuration

A case does not change the framework. It supplies configuration:

```text
case_id
canonical_crs
system_boundary
study_period
service_scope
jurisdiction
authority hierarchy
applicable codes/standards/procedures
source manifests
adapter selection
field mappings
unit mappings
topology tolerances
temporal compatibility rules
structural-candidate rules
QA thresholds
```

Therefore Austin, Greensboro, Singapore, a synthetic benchmark, or another P–T case should instantiate the same framework through configuration and adapters.

## 11. Stage-1 framework gate

`G1_framework = PASS` only when:

```math
\boxed{
\begin{gathered}
\text{ontology frozen}
\land
\text{CIR frozen}
\land
\text{adapter contract frozen}
\land
\text{cleaning rules frozen}
\\
\land
\text{QA/provenance rules frozen}
\land
\text{machine-readable schemas valid}
\land
\text{normative applicability contract valid}
\land
\text{case-independent fixture tests pass}.
\end{gathered}
}
```

## 12. Case gate

`G1_case(case_id) = PASS` only when the selected sources successfully instantiate the framework and produce a reproducible `Z1_impl`.

This gate belongs to case execution / Chapter 4 methodology and must not redefine Stage-1 mathematics.

## 13. Scientific consequence

The thesis can freeze the **Stage-1 methodological framework** without possessing final Austin data.

Any Austin-specific failure then means:

```math
\boxed{
\text{Austin case inadmissible or incomplete}
\neq
\text{Stage-1 framework invalid}.
}
```

If a new data source cannot map into the CIR because the source reveals a genuinely missing semantic class, the framework must be versioned and amended explicitly rather than patched silently.