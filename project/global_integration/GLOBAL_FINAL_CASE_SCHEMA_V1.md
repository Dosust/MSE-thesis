# Global Final-Case Schema v1

**Date:** 2026-09-19  
**Status:** CANONICAL GLOBAL PRE-DATA CASE CONTRACT  
**Stage scope:** Stage 1→7  
**Case values:** DEFERRED unless independently qualified  
**Empirical effect:** none.

## 1. Scientific purpose

P1.5 defines **what constitutes an admissible thesis case** before final case data are inspected or bound.

The core scientific object remains:

~~~math
\boxed{
\mathcal S_{\rm case}
=
(
\mathcal G,
Y_0,
\theta,
\eta,
T,
K,
G_{\rm rec},
F_{\rm unsafe},
\mathcal U_{\rm feas},
\mathcal A,
\Omega
).
}
~~~

P1.5 wraps this object in an auditable case package:

~~~math
\boxed{
\mathfrak C_{\rm case}
=
(
ID_{\rm case},
\mathcal S_{\rm case},
\mathcal M_{\rm case},
\Pi_{\rm case},
\Lambda_{\rm case},
S_{\rm case}
).
}
~~~

where:
- \(ID_{\rm case}\): immutable case identifier;
- \(\mathcal M_{\rm case}\): field-level metadata dictionary;
- \(\Pi_{\rm case}\): provenance graph/ledger;
- \(\Lambda_{\rm case}\): maximum defensible case claim ceiling;
- \(S_{\rm case}\): case qualification status.

Permanent:

~~~math
\boxed{
\text{case value}
\neq
\text{case evidence}
\neq
\text{case provenance}
\neq
\text{case admissibility}.
}
~~~

## 2. External scientific foundations

P1.5 uses the following standards and research principles as design guidance, while thesis-specific semantics remain governed by the repository authorities.

1. W3C PROV-O models provenance through entities, activities and agents and supports interoperable provenance exchange [1].
2. FAIR emphasizes findability, accessibility, interoperability and reusability for data, algorithms, tools and workflows [2].
3. ISO 19115-1:2014 is the current published metadata standard for geographic information and covers identification, extent, quality, spatial/temporal aspects and spatial reference; a replacement edition is under development [3].
4. ISO 19157-1:2023 defines principles and procedures for geographic-data quality description, evaluation and reporting [4].
5. OGC WKT-CRS provides a formal representation for coordinate reference systems and coordinate operations [5].
6. OGC SensorThings separates observations, sensors, locations and observed features, supporting explicit observation provenance [6].
7. CF Metadata Conventions define variable, spatial and temporal metadata for environmental/gridded data; the latest released CF version is 1.13 (December 2025) [7].
8. The BIPM SI Brochure, 9th edition updated in 2026, is the controlling external reference for SI units [8].
9. JCGM GUM provides the international framework for expression and propagation of measurement uncertainty; JCGM 101 covers Monte Carlo propagation [9].
10. NASA-STD-7009B and NASA-HDBK-7009B require modeling/simulation credibility, verification, validation, uncertainty and acceptance criteria to be tied to intended use [10].
11. NIST digital-twin credibility work likewise emphasizes verification, validation and UQ across the digital-twin lifecycle [11].
12. JSON Schema Draft 2020-12 provides a machine-readable mechanism for structural and conditional data validation [12].

These sources do not validate this thesis case. They justify the metadata/provenance/VVUQ architecture.

## 3. Canonical field metadata object

For every case field \(f\), define:

~~~math
\boxed{
\begin{aligned}
\mathfrak m_f
=(
&ID_f,
Def_f,
Type_f,
Shape_f,
Class_f,
Unit_f,
Space_f,
Time_f,\\
&Src_f,
Ver_f,
Transform_f,
Role_f,
U_f,
Q_f,
Ref_f,
G_f,\\
&Status_f,
Owner_f,
Consumer_f,
Validity_f,
Hash_f,
License_f,
\Lambda_f
).
\end{aligned}
}
~~~

| Component | Scientific meaning |
|---|---|
| \(ID_f\) | immutable field identifier |
| \(Def_f\) | exact physical/mathematical definition |
| \(Type_f\) | graph, vector, field, set, parameter, forcing, action set, intervention set, domain |
| \(Shape_f\) | scalar/vector/matrix/network/time series/raster/collection |
| \(Class_f\) | physical / epistemic / requirement / control / intervention / validity-domain |
| \(Unit_f\) | quantity, native/source unit, canonical unit, conversion rule |
| \(Space_f\) | CRS, geometry support, extent, spatial resolution |
| \(Time_f\) | timestamp/interval, timezone, temporal resolution |
| \(Src_f\) | source class and source identifier |
| \(Ver_f\) | source/data/model version/date |
| \(Transform_f\) | ordered derivation/transformation chain |
| \(Role_f\) | calibration/validation/benchmark/confirmatory/operational/none |
| \(U_f\) | uncertainty representation and dependence |
| \(Q_f\) | measured data-quality evidence |
| \(Ref_f\) | P1.4 reference/validation class |
| \(G_f\) | field admissibility gate |
| \(Status_f\) | PASS/BLOCKED/FAIL/DEFERRED/N/A |
| \(Owner_f\) | scientific owning stage |
| \(Consumer_f\) | downstream consuming stages |
| \(Validity_f\) | domain of intended use |
| \(Hash_f\) | integrity/hash identity where applicable |
| \(License_f\) | access/reuse/license status |
| \(\Lambda_f\) | maximum defensible claim from field |

## 4. Provenance contract

Following the W3C PROV entity–activity–agent pattern [1], every derived case object must expose:

~~~math
\boxed{
\text{source entity}
\rightarrow
\text{transformation activity}
\rightarrow
\text{derived entity}
\rightarrow
\text{model input}
\rightarrow
\text{result}.
}
~~~

A source citation alone is insufficient.

Each transformation record must include, when applicable:

~~~text
source_id
source_version
acquisition_date
activity_id
activity_description
software
software_version
parameters
input_hash
output_hash
responsible_agent
timestamp
notes
~~~

If a field is reconstructed or inferred, the reconstruction method is part of provenance and must remain distinguishable from direct observation.

## 5. Unit contract

Each dimensional quantity must record:

~~~math
\boxed{
(
\text{quantity},
\text{source unit},
\text{canonical unit},
\text{conversion rule},
\text{unit authority}
).
}
~~~

SI is preferred where physically appropriate, using the BIPM SI Brochure [8]. No silent conversion is permitted.

~~~math
G_{unit}(f)
=
\begin{cases}
PASS,&\text{units defined and dimensionally compatible},\\
BLOCKED,&\text{unit meaning unresolved},\\
FAIL,&\text{documented dimensional incompatibility}.
\end{cases}
~~~

## 6. Spatial and temporal contract

For every spatially indexed field, require as applicable:

~~~math
\boxed{
(
CRS,
datum,
geometry,
extent,
resolution,
coordinate\ operation,
spatial\ quality
).
}
~~~

ISO 19115-1 and ISO 19157-1 motivate explicit metadata and data-quality reporting [3,4], while OGC WKT-CRS provides the CRS representation model [5].

For every time-indexed field require:

~~~math
\boxed{
(
t_{start},
t_{end},
timezone,
temporal\ reference,
sampling/resolution,
clock/synchronization\ status
).
}
~~~

For environmental/gridded hazard data, record the dataset's CF convention/version where applicable [7].

## 7. Observation contract

When a field depends on observations, preserve:

~~~math
\boxed{
\text{sensor}
\neq
\text{location}
\neq
\text{observed property}
\neq
\text{feature of interest}
\neq
\text{observation}.
}
~~~

This follows the semantic separation used by OGC SensorThings [6].

Every observation-derived case field must identify:
- observed property;
- feature/entity represented;
- sensor/source;
- measurement time;
- receive time if relevant;
- unit;
- quality;
- missingness;
- uncertainty;
- transformation to model state/QOI.

## 8. Uncertainty contract

A generic flag such as "uncertain = yes" is prohibited.

~~~math
\boxed{
U_f
=
(
Class_U,
Representation_U,
Parameters_U,
Dependence_U,
Source_U,
Propagation_U,
Validation_U
).
}
~~~

Allowed uncertainty classes include:

~~~text
ALEATORY
EPISTEMIC
MODEL_FORM
NUMERICAL
MEASUREMENT
REQUIREMENT
PERFORMANCE
VALUE
MIXED
~~~

Representations may include distributions, intervals, sets, ensembles, covariance structures, samples, scenario domains or another justified form.

Measurement-uncertainty reporting should remain compatible with JCGM GUM principles [9].

Probability is not assigned unless probability semantics are justified.

## 9. Data-quality contract

For relevant fields:

~~~math
\boxed{
Q_f
=
(
completeness,
consistency,
positional\ accuracy,
thematic\ accuracy,
temporal\ quality,
coverage,
lineage
).
}
~~~

ISO 19157-1 distinguishes describing/evaluating quality from deciding whether quality is sufficient for an application [4]. Therefore:

~~~math
\boxed{
\text{measured data quality}
\neq
\text{required data-quality threshold}.
}
~~~

## 10. P1.4 reference-class binding

Each field must use an explicit P1.4 class, e.g.:

~~~text
VALIDATION_EVIDENCE
VALIDATION_REFERENCE
REFERENCE_SOLUTION
REFERENCE_CALCULATION
EVIDENCE_SOURCE_REFERENCE
EXTERNAL_PRACTICE/FACTOR_REFERENCE
SYNTHETIC_TRUTH
GROUND_TRUTH
QUALIFIED_CASE
AUXILIARY_COUNTERFACTUAL_MODEL
NONE
~~~

No unnamed "reference" is permitted.

A synthetic source cannot be promoted to empirical ground truth.

## 11. Source classes

Every source is classified as one or more of:

~~~text
DIRECT_MEASUREMENT
DERIVED_OBSERVATION
CALIBRATED
INFERRED
MANUFACTURER
AUTHORITATIVE_DATABASE
REGULATORY
STANDARD
OPERATOR
STAKEHOLDER
PEER_REVIEWED_LITERATURE
HIGHER_FIDELITY_MODEL
SYNTHETIC
SENSITIVITY_ONLY
RESEARCH_ASSUMPTION
OTHER
~~~

Permanent:

~~~math
\boxed{
\text{SENSITIVITY_ONLY}
\not\Rightarrow
\text{CALIBRATED}
\not\Rightarrow
\text{VALIDATED}.
}
~~~

## 12. Field-specific scientific requirements

### 12.1 Coupled graph \(\mathcal G\)

~~~math
\boxed{
\mathcal G
=
(
\mathcal G_P,
\mathcal G_T,
\mathcal C_{PT},
\mathcal M_{geo},
Ver_{\mathcal G}
).
}
~~~

Must record entity/edge IDs and types, topology/direction, geometry and CRS, interface/crosswalk IDs, source/version, structural evidence/provenance, topology QA and qualified dependency linkage.

Spatial proximity alone cannot create causal coupling.

Owner: Stage 1/2. Consumers: Stages 2–7.

### 12.2 Initial physical state \(Y_0\)

~~~math
\boxed{
Y_0
=
Y^{phys}(t_0\mid\mathcal G(t_0),m_0,\mathbb I_0^{active}).
}
~~~

Must record common \(t_0\), state definition and units, measurement/reconstruction source, synchronization, discrete mode, active dependency context and uncertainty.

~~~math
Y_0^{measured}
\neq
Y_0^{estimated}
\neq
Y_0^{assumed}.
~~~

Owner: Stage 3. Consumers: Stages 3–7.

### 12.3 Parameters \(\theta\)

~~~math
\boxed{
\theta_i
=
(
name,
definition,
value/range,
unit,
source,
method,
U,
dependence,
validity,
status
).
}
~~~

Must distinguish measured, calibrated, inferred, manufacturer, literature, authoritative and sensitivity-only sources.

Owner: Stage 2/3, with later-stage parameters owned locally.

### 12.4 Hazard forcing \(\eta\)

~~~math
\boxed{
\eta=\eta(\mathbf r,t;\xi_\eta).
}
~~~

Must record hazard type, physical variable, unit, CRS/spatial support, grid/resolution where applicable, temporal support, source/version, observed/reanalysis/synthetic status and uncertainty.

Owner: Stage 3. Consumers: Stages 3–7.

### 12.5 Dynamic horizon \(T\)

Must record start/end, time unit, dynamic purpose, engineering justification, numerical-window relationship and scenario consistency.

~~~math
\boxed{
T_{dynamic}
\neq
H_{LC}
}
~~~

unless explicitly demonstrated otherwise.

Owner: Stage 3/5. Consumers: Stages 3–7.

### 12.6 Viable/acceptable set \(K\)

~~~math
\boxed{
K
=
\{x_R:g_j(x_R,t)\le0,\ j=1,\ldots,m\}
}
~~~

or another explicitly defined equivalent.

Every constraint must identify expression, variable/unit, threshold, authority class, scope/jurisdiction, effective date, uncertainty and requirement ID.

Owner: Stage 5. Consumers: Stages 5–7.

### 12.7 Recovery target \(G_{rec}\)

Must define target state/service condition, deadline/horizon, units, authority/requirement ID, uncertainty and relationship to \(K\).

Owner: Stage 5. Consumers: Stages 5–7.

### 12.8 Forbidden set \(F_{unsafe}\)

Must define forbidden condition, physical/safety basis, units, requirement/authority provenance, uncertainty and temporal applicability.

Owner: Stage 5. Consumers: Stages 5–7.

### 12.9 Feasible operational controls \(\mathcal U_{feas}\)

~~~math
\boxed{
\mathcal U_{feas}
=
\mathcal U_{phys}
\cap
\mathcal U_{info}
\cap
\mathcal U_{org}
\cap
\mathcal U_{resource}.
}
~~~

Every constraint must identify its source, units, availability, stage and uncertainty.

Owner: Stage 4. Consumers: Stages 5–6 and inherited decision context.

### 12.10 Strategic interventions \(\mathcal A\)

Each intervention:

~~~math
\boxed{
a_k
=
(
ID,
class,
target,
location,
operator,
parameters,
timing,
resources,
implementation,
service\ life,
accounting\ boundary,
eligibility,
provenance
).
}
~~~

It must be executable as:

~~~math
\mathfrak M^{a_k}
=
\Phi_a(\mathfrak M^0,a_k).
~~~

~~~math
\boxed{u(t)\neq a_k.}
~~~

Owner: Stage 6. Consumers: Stages 6–7.

### 12.11 Validity/case domain \(\Omega\)

~~~math
\boxed{
\Omega_{case}
=
\Omega_x
\times
\Omega_t
\times
\Omega_{hazard}
\times
\Omega_{operating}
\times
\Omega_{model}
\times
\Omega_{uncertainty}.
}
~~~

This is the admissible domain, not the scenario sample.

~~~math
\boxed{
\Omega_{case}
\neq
\{\omega_s\}_{s=1}^{N}.
}
~~~

P1.6 will define scenario realizations \(\omega_s\in\Omega_{case}\).

Owner: global integration with stage-specific components. Consumers: all.

## 13. Requirement-authority firewall

Constraint provenance classes include:

~~~text
REGULATORY
STANDARD
OPERATOR
STAKEHOLDER
ENGINEERING
RESEARCH_ASSUMPTION
~~~

~~~math
\boxed{
\text{RESEARCH_ASSUMPTION}
\neq
\text{AUTHORITATIVE_REQUIREMENT}.
}
~~~

P1.5 stores requirement IDs and provenance. P1.8 will own the global requirements registry.

## 14. Field admissibility gate

~~~math
\boxed{
\begin{aligned}
G_f={}&
G_{semantic}
\land G_{type}
\land G_{unit}
\land G_{spatial}
\land G_{temporal}
\land G_{source}\\
&\land G_{provenance}
\land G_{quality}
\land G_{uncertainty}
\land G_{reference}
\land G_{validity}
\land G_{ownership}.
\end{aligned}
}
~~~

Statuses:

~~~text
PASS
BLOCKED
FAIL
DEFERRED
N/A
~~~

- PASS: all mandatory evidence/provenance for current intended use is present;
- BLOCKED: required evidence/information is unavailable or unresolved;
- FAIL: available evidence violates a declared admissibility criterion;
- DEFERRED: value intentionally not yet bound at pre-data stage;
- N/A: gate does not apply.

## 15. Case-level gate

~~~math
\boxed{
\begin{aligned}
G_{P1.5}={}&
G_{schema}
\land G_{type}
\land G_{unit}
\land G_{provenance}
\land G_{space-time}
\land G_{quality}\\
&\land G_{uncertainty}
\land G_{reference}
\land G_{ownership}
\land G_{handoff}
\land G_{claim}.
\end{aligned}
}
~~~

At design level, P1.5 may PASS while all numerical case values remain DEFERRED.

At case execution level, a field required by the selected experiment must be PASS before it can support confirmatory claims.

## 16. Case status and claim ceiling

Case-level status:

~~~text
SCHEMA_ONLY
PARTIALLY_BOUND
EXECUTION_READY
VALIDATED_FOR_DECLARED_USE
BLOCKED
FAILED
~~~

These are not hypothesis outcomes.

~~~math
\boxed{
\Lambda_{case}
\le
\min_{f\in F_{required}}
\Lambda_f.
}
~~~

A strong downstream algorithm cannot repair a weak upstream case field.

## 17. Machine-readable implementation

The normative machine structure is GLOBAL_FINAL_CASE_SCHEMA_V1.schema.json using JSON Schema Draft 2020-12 [12].

It:
- requires all eleven core field records;
- permits values to remain absent when status is DEFERRED/BLOCKED;
- requires a bound value when a field is declared PASS;
- constrains statuses, stages, source classes, reference classes and data roles;
- prohibits undeclared top-level properties;
- carries the P1.5 metadata/provenance/UQ/admissibility structure.

## 18. P1.5 package

1. GLOBAL_FINAL_CASE_SCHEMA_V1.md
2. GLOBAL_FINAL_CASE_SCHEMA_V1.schema.json
3. GLOBAL_FINAL_CASE_FIELD_DICTIONARY_V1.md
4. GLOBAL_FINAL_CASE_SOURCE_PROVENANCE_TEMPLATE_V1.csv
5. GLOBAL_FINAL_CASE_ADMISSIBILITY_GATE_MATRIX_V1.md
6. GLOBAL_FINAL_CASE_REFERENCE_CLASS_MATRIX_V1.md
7. GLOBAL_FINAL_CASE_UNCERTAINTY_TEMPLATE_V1.md
8. P1_5_FINAL_CASE_SCHEMA_AUDIT_V1_2026-09-19.md
9. P1_5_FINAL_CASE_SCHEMA_MANIFEST_V1.json

## 19. Protected DEFERRED items

P1.5 does not select or invent final city/region, feeder/substation IDs, road subnetwork, interface crosswalks, hazard magnitude/event, initial physical values, parameter values/distributions, final horizons, requirement thresholds, feasible-control bounds, intervention set, scenario IDs/probabilities, or H1–H5 result.

## 20. External references

[1] W3C, PROV-O: The PROV Ontology, W3C Recommendation, 2013. https://www.w3.org/TR/prov-o/  
[2] Wilkinson et al., The FAIR Guiding Principles for scientific data management and stewardship, Scientific Data 3, 160018 (2016). https://doi.org/10.1038/sdata.2016.18  
[3] ISO, ISO 19115-1:2014 Geographic information — Metadata — Part 1: Fundamentals. https://www.iso.org/standard/53798.html  
[4] ISO, ISO 19157-1:2023 Geographic information — Data quality — Part 1: General requirements. https://www.iso.org/standard/78900.html  
[5] OGC, Well-known text representation of coordinate reference systems. https://www.ogc.org/standards/wkt-crs/  
[6] OGC, SensorThings API Standard. https://www.ogc.org/standards/sensorthings/  
[7] CF Community, CF Conventions and Conformance; latest released version 1.13 (December 2025). https://cfconventions.org/conventions.html  
[8] BIPM, The International System of Units (SI), 9th edition, updated 2026. https://www.bipm.org/en/publications/si-brochure  
[9] JCGM/BIPM, Guides in Metrology: JCGM 100, 101 and related GUM publications. https://www.bipm.org/en/committees/jc/jcgm/publications  
[10] NASA, NASA-STD-7009B and NASA-HDBK-7009B. https://standards.nasa.gov/systems-and-subsystem-test  
[11] NIST, Credibility Consideration for Digital Twins in Manufacturing. https://www.nist.gov/publications/credibility-consideration-digital-twins-manufacturing  
[12] JSON Schema, Draft 2020-12. https://json-schema.org/draft/2020-12

## 21. Repository authority snapshot

- GLOBAL_SYMBOL_AND_ONTOLOGY_REGISTRY_V1.md @ 6f389265ac6e449e814534a7e61e12918a2224aa
- GLOBAL_STAGE_HANDOFF_MATRIX_V1.md @ 711128daad5f150016cf994e1c6da497c3c84bb7
- GLOBAL_BASELINE_BENCHMARK_REFERENCE_REGISTRY_V1.md @ b46e393d37f1bc979d7cf2f351d0d586f31898c1
- GLOBAL_H1_H5_MASTER_PREREGISTRATION_V1.md @ 9b80cb8a2bbb882b53ed5dd3f86d007596e0e9f6
- STAGE1_FINAL_FRAMEWORK_V2.md @ 65fe99930245a68259608cf3b59cc29606bbe605
- STAGE3_STATE_INPUT_OUTPUT_QOI_ONTOLOGY_V2.md @ 80dd965391c672df303e46ace919a5dd6bf11ec5
- STAGE4_SCIENTIFIC_CONSTITUTION_AND_HANDOFF_V1.md @ 450440fd06088202c1266303cddf9b0e0c2a4c8c
- STAGE5_SCIENTIFIC_CONSTITUTION_AND_HANDOFF_V1.md @ 3742632c3a0eda97ec4b6fb85aeb81cb334ed4c2
- STAGE6_SCIENTIFIC_CONSTITUTION_AND_HANDOFF_V2.md @ 3493142f685c9520ee7f6bdf001a3dea131f2649
- STAGE7_SCIENTIFIC_CONSTITUTION_AND_HANDOFF_V2.md @ 38a71356b3c99d35d5b73f7b70fb7d32452f71d4

## 22. Freeze interpretation

~~~math
\boxed{
G_{P1.5}^{design}=PASS
}
~~~

means only that the case schema and admissibility architecture are complete and auditable. It does not mean a final case has been selected, bound, validated or used to test H1–H5.
