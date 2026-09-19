# Global Requirements / Provenance Control v1

**Date:** 2026-09-19  
**Status:** CANONICAL GLOBAL PRE-DATA REQUIREMENTS / PROVENANCE CONTROL  
**Scope:** Stage 1→7 scientific requirements, thresholds, constraints, targets, criteria, preferences, provenance, change control, traceability and compliance semantics  
**Empirical effect:** none.

## 1. Scientific purpose

P1.8 defines which statements are allowed to act as requirements, thresholds, constraints, targets or decision criteria in the thesis, where they came from, how they are translated into mathematics, and which downstream objects they are allowed to control.

Permanent firewall:

~~~math
\boxed{
\text{authoritative requirement}
\neq
\text{engineering-derived criterion}
\neq
\text{research assumption}
\neq
\text{experimental materiality criterion}
\neq
\text{decision preference}.
}
~~~

A numerical value is not a requirement merely because it is useful to a simulation.

## 2. External requirements-engineering basis

P1.8 uses external standards as design guidance only.

1. ISO/IEC/IEEE 29148:2018 is the current published international standard for requirements engineering; ISO reports that it was confirmed in 2024 and is now under revision [1]. It defines requirements-engineering processes over the system/software life cycle.
2. NASA requirements management calls for bidirectional traceability, requirement baselines, evaluation of change requests, and consistency between requirements, concept of operations and architecture/design [2].
3. NASA's Systems Engineering Handbook Appendix C/D/E provides checklists for good requirements, a requirements verification matrix, and validation planning [3].
4. W3C PROV provides entity–activity–agent/derivation concepts suitable for representing the provenance of requirement sources, translations and versions [4].
5. JSON Schema Draft 2020-12 is used for machine-readable structural validation of P1.8 records [5].

These sources do not supply any thesis-specific threshold.

## 3. Requirement identity

Each requirement/criterion is an immutable versioned object:

~~~math
\boxed{
\mathfrak r_i
=
(
RID_i,
Ver_i,
Statement_i,
Domain_i,
Kind_i,
Hardness_i,
Authority_i,
Source_i,
Applicability_i,
Formal_i,
U_i,
Trace_i,
Status_i,
Prov_i,
\Lambda_i
).
}
~~~

A change in scientific meaning creates a new version.

## 4. Requirement-domain taxonomy

~~~text
PHYSICAL
SAFETY
SERVICE
RECOVERY
OPERATIONAL_CONTROL
INFORMATION
ORGANIZATION
EFFECTIVENESS
RESOURCE_EFFICIENCY
SUSTAINABILITY
FEASIBILITY
DECISION
EXPERIMENTAL_METHOD
THESIS_INSTITUTIONAL
OTHER
~~~

THESIS_INSTITUTIONAL requirements, such as ASU format/defense rules, remain separate from the physical/engineering case model unless the requirement is explicitly about research procedure.

## 5. Requirement-kind taxonomy

~~~text
EXTERNALLY_IMPOSED_REQUIREMENT
OPERATOR_REQUIREMENT
STAKEHOLDER_REQUIREMENT
ENGINEERING_DERIVED_REQUIREMENT
SAFETY_CRITERION
SERVICE_CRITERION
RECOVERY_CRITERION
CONTROL_FEASIBILITY_CONSTRAINT
EFFECTIVENESS_TARGET
RESOURCE_CONSTRAINT
SUSTAINABILITY_REQUIREMENT
DECISION_FEASIBILITY_CONSTRAINT
EXPERIMENTAL_PREREGISTRATION_CRITERION
RESEARCH_ASSUMPTION
VALUE_PREFERENCE
INSTITUTIONAL_REQUIREMENT
OTHER
~~~

Kind and authority are separate axes.

## 6. Authority-source taxonomy

Every source has one authority class:

~~~text
LAW_REGULATION
MANDATED_STANDARD
VOLUNTARY_STANDARD
CONTRACTUAL
OPERATOR_POLICY
OPERATOR_ENGINEERING
STAKEHOLDER_ELICITED
SAFETY_ENGINEERING
CASE_ENGINEERING_DERIVED
PEER_REVIEWED_EVIDENCE
MANUFACTURER_SPECIFICATION
EXPERIMENTAL_PREREGISTRATION
RESEARCH_ASSUMPTION
VALUE_MODEL
INSTITUTIONAL_POLICY
OTHER
~~~

Permanent:

~~~math
\boxed{
\text{source class}
\neq
\text{requirement kind}.
}
~~~

For example, a peer-reviewed paper may support an engineering criterion without becoming a regulation.

## 7. Hardness / decision role

~~~text
HARD_ADMISSIBILITY
HARD_SAFETY
HARD_FEASIBILITY
SOFT_TARGET
OBJECTIVE
REPORT_ONLY
ASSUMPTION
PREFERENCE
EXPERIMENTAL_GATE
~~~

A hard requirement may eliminate a state/action/intervention.

A soft target may be reported or used for effectiveness but cannot silently exclude an option.

An objective or preference does not become a requirement unless a separate authority/source establishes it.

## 8. Canonical requirement record

Every record contains at least:

~~~text
requirement_id
version
title
normalized_statement
original_source_summary
domain
kind
hardness
authority_class
authority_entity
source_id
source_uri_or_path
source_version
source_locator
publication_date
effective_start
effective_end
jurisdiction_or_scope
applicability_conditions
parent_requirement_ids
derived_from_requirement_ids
derivation_rationale
owning_stage
consumer_stages
object_or_qoi
mathematical_expression
comparison_operator
threshold_or_target
quantity
source_unit
canonical_unit
conversion_rule
temporal_aggregation
spatial_aggregation
population_or_group_scope
scenario_hazard_scope
uncertainty_id
reference_class
verification_method
validation_or_need_confirmation
compliance_evaluation_method
gate_status
maturity_status
effectivity_status
claim_ceiling
provenance_version
provenance_hash
notes
~~~

## 9. Source-to-mathematics translation

The normative chain is:

~~~math
\boxed{
S_i
\xrightarrow{I_i}
R_i^{norm}
\xrightarrow{T_i}
g_i(x,t;\kappa_i)
\xrightarrow{A_i}
O_k
\xrightarrow{E_i}
Compliance_i.
}
~~~

where:
- \(S_i\): source statement/need;
- \(I_i\): interpretation;
- \(R_i^{norm}\): normalized requirement statement;
- \(T_i\): mathematical translation;
- \(g_i\): executable condition;
- \(A_i\): allocation to stage/object;
- \(O_k\): model/QOI/decision object;
- \(E_i\): evaluation procedure.

Every arrow is provenance-bearing.

## 10. Qualitative-to-quantitative firewall

A qualitative source does not directly authorize a numerical threshold.

~~~math
\boxed{
\text{qualitative requirement}
\not\Rightarrow
\kappa_i=\text{chosen number}.
}
~~~

A numerical translation requires:
- explicit interpretation;
- unit/quantity mapping;
- aggregation rule;
- evidence/rationale for the number;
- uncertainty/ambiguity treatment;
- validity/applicability domain;
- independent approval/source where required.

If these are absent:

~~~text
gate_status = BLOCKED
~~~

rather than filling the value from convenience or desired results.

## 11. Bidirectional traceability

Forward trace:

~~~math
\boxed{
\text{need/source}
\rightarrow
RID
\rightarrow
\text{formal criterion}
\rightarrow
\text{stage object}
\rightarrow
\text{gate/QOI}
\rightarrow
\text{test/evidence/result}.
}
~~~

Reverse trace:

~~~math
\boxed{
\text{constraint/threshold in code or analysis}
\rightarrow
RID
\rightarrow
\text{source/derivation}.
}
~~~

Every hard constraint or confirmatory materiality threshold must be traceable in both directions.

## 12. Parent/derived requirement semantics

A requirement may be externally imposed, inherited, allocated, derived from a parent requirement, or self-derived by engineering design/research logic.

Derived requirement:

~~~math
\boxed{
RID_{child}
\xleftarrow{\text{derived from}}
RID_{parent}.
}
~~~

A self-derived requirement must record:
- reason;
- source design decision/need;
- responsible owner;
- validation/need-confirmation method;
- whether it is authoritative or merely thesis-internal.

Permanent:

~~~math
\boxed{
\text{self-derived}
\not\Rightarrow
\text{externally authoritative}.
}
~~~

## 13. Units and aggregation

Every quantitative criterion must define:

~~~math
\boxed{
(
quantity,
operator,
threshold,
unit,
time\ aggregation,
space\ aggregation,
population/group,
scenario/domain
).
}
~~~

Examples of non-equivalent requirements:

~~~math
S_P(t)\ge0.9\ \forall t
\quad\neq\quad
\frac{1}{T}\int_0^T S_P(t)\,dt\ge0.9.
~~~

Likewise:

~~~math
\text{system-average accessibility}
\neq
\text{minimum accessibility for a declared subgroup}.
~~~

No silent aggregation is allowed.

## 14. Effective date, jurisdiction and applicability

External requirements must retain as applicable:
- jurisdiction;
- issuing authority;
- effective date;
- expiration/supersession date;
- system/assets/population covered;
- triggering operating/hazard condition;
- exceptions/waivers if documented.

A requirement outside its applicability domain cannot be applied merely because it is stricter or convenient.

## 15. Requirement uncertainty versus compliance uncertainty

Permanent distinction:

~~~math
\boxed{
U_{requirement}
\neq
U_{compliance}.
}
~~~

Requirement uncertainty may arise from ambiguous source wording, contested interpretation, uncertain applicability, uncertain threshold/elicitation, or uncertain temporal/spatial scope.

Compliance uncertainty may arise from measurement error, state estimation, model-form error, numerical error, or uncertain future outcomes.

An exact legal threshold may have zero threshold uncertainty but still have nonzero compliance uncertainty.

## 16. Reference-class binding

Each requirement source uses P1.4 reference classes where applicable.

Typical bindings:
- source text / standard / operator specification → EVIDENCE_SOURCE_REFERENCE;
- authoritative numeric limit → REQUIREMENT_THRESHOLD;
- empirical support for a derived criterion → VALIDATION_EVIDENCE or EVIDENCE_SOURCE_REFERENCE;
- research-only threshold → NONE plus EXPERIMENTAL_PREREGISTRATION or RESEARCH_ASSUMPTION authority.

Synthetic truth cannot establish a real-world authoritative requirement.

## 17. Requirement-quality gate

For every \(RID_i\):

~~~math
\boxed{
\begin{aligned}
G_{req,i}={}&
G_{identity}
\land G_{statement}
\land G_{authority}
\land G_{source}
\land G_{trace}\\
&\land G_{unit}
\land G_{scope}
\land G_{aggregation}
\land G_{uncertainty}
\land G_{verifiable}\\
&\land G_{consistent}
\land G_{applicable}
\land G_{provenance}.
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

## 18. Requirement maturity

Maturity is distinct from gate status:

~~~text
DRAFT
SOURCE_IDENTIFIED
QUALIFIED
BASELINED
SUPERSEDED
RETIRED
REJECTED
~~~

Effectivity is distinct again:

~~~text
ACTIVE
FUTURE
EXPIRED
INACTIVE
UNKNOWN
~~~

Permanent:

~~~math
\boxed{
\text{gate status}
\neq
\text{maturity}
\neq
\text{effectivity}.
}
~~~

## 19. Stage 4 requirements

Stage 4 operational feasibility:

~~~math
\mathcal U_{feas}
=
\mathcal U_{phys}
\cap
\mathcal U_{info}
\cap
\mathcal U_{org}
\cap
\mathcal U_{resource}.
~~~

Each limiting condition must trace to an explicit requirement/constraint/assumption record.

Physical capability does not imply information availability or organizational authority.

A research assumption about authority/resources cannot be labeled an operator requirement.

## 20. Stage 5 requirements

Stage 5 owns:

~~~math
\boxed{
\mathcal K_{req},
K,
G_{rec},
F_{unsafe},
T_V,
T_R.
}
~~~

Requirements affecting \(K\) must distinguish physical admissibility, safety, critical service, and operational admissibility.

Permanent:

~~~math
\boxed{
G_{rec}\subseteq K,
\qquad
K\cap F_{unsafe}=\varnothing
}
~~~

when those sets are instantiated under the active Stage-5 semantics.

Sustainability outcomes remain Stage-6 consequences unless an independently sourced hard sustainability requirement explicitly promotes a sustainability quantity into admissibility.

## 21. Stage 6 effectiveness requirements

Effectiveness asks whether declared engineering targets are met.

Hard requirements determine admissibility under the frozen aggregation rule; soft targets are reported separately.

~~~math
\boxed{
\text{hard requirement}
\neq
\text{soft effectiveness target}.
}
~~~

No compensatory weighting across hard and soft targets is allowed unless separately authorized.

Every target records QOI, direction, threshold, units, aggregation, provenance, uncertainty and validity.

## 22. Stage 6 efficiency/resource requirements

Resource quantities such as time, crew, material, energy and cost may define feasibility constraints, efficiency denominators, or report-only consequences.

These roles must be explicit.

~~~math
\boxed{
\text{resource consumption}
\neq
\text{resource constraint}
\neq
\text{efficiency metric}.
}
~~~

No resource value may acquire a hard limit merely because it appears in an efficiency calculation.

## 23. Stage 6 sustainability requirements

Default Stage-6 sustainability objects:

~~~math
\mathbf J_{sus}
=
[
J_{access},
J_{energy},
J_{carbon},
J_{cost}
]^\top
~~~

are consequences/objectives, not automatically hard requirements.

Permanent:

~~~math
\boxed{
\text{sustainability metric}
\neq
\text{sustainability requirement}.
}
~~~

A sustainability dimension becomes a hard constraint only if an independently documented requirement with valid scope/authority defines that constraint.

## 24. Stage 7 requirements and value firewall

Stage 7 receives feasibility and requirement constraints from upstream.

Decision objectives/preferences remain separate.

~~~math
\boxed{
\text{feasibility requirement}
\neq
\text{objective}
\neq
\text{weight/preference}.
}
~~~

A value weight cannot make an infeasible intervention feasible.

An objective cannot be promoted to a hard requirement merely because it produces a preferred decision set.

## 25. Experimental materiality criteria

The confirmatory thresholds:

~~~math
\delta_1,\delta_2,\delta_3,\delta_4,\delta_5
~~~

and analogous preregistered decision/materiality rules are EXPERIMENTAL_PREREGISTRATION_CRITERION unless independently shown to also be engineering requirements.

Permanent:

~~~math
\boxed{
\delta_i
\neq
\text{real-system requirement}
}
~~~

by default.

Their provenance must state how the criterion was chosen and prohibit selection from confirmatory effect sizes.

## 26. Institutional thesis requirements

ASU/SSEBE manuscript, committee, enrollment and defense requirements are retained in the institutional governance layer.

They may constrain thesis process/output, but they do not define \(K\), \(G_{rec}\), \(F_{unsafe}\), \(\mathcal U_{feas}\), \(\mathcal A^{adm}\), or engineering effectiveness/sustainability thresholds.

This prevents institutional process rules from leaking into scientific system semantics.

## 27. Requirement conflicts

A conflict exists when applicable requirements cannot be simultaneously satisfied or their translations are inconsistent.

P1.8 does not impose a universal legal hierarchy.

Conflict resolution records:
- conflicting RIDs;
- applicability/jurisdiction;
- authority and source;
- contradiction type;
- engineering/legal/owner resolution basis;
- accepted requirement/version;
- rejected/superseded status;
- downstream impact.

Permanent:

~~~math
\boxed{
\text{stricter number}
\not\Rightarrow
\text{higher authority}.
}
~~~

Applicable law/regulation cannot be overridden by a thesis preference, but legal/contractual precedence must be determined from the actual case context rather than invented globally.

## 28. Requirement change control

A baselined requirement change must record:

~~~text
change_id
affected_requirement_id
old_version
new_version
reason
initiator
source_change_or_internal_change
approval/authority
effective_date
affected_models
affected_scenarios
affected_hypotheses
affected_results
re-execution_required
target_results_seen_before_change
status
provenance
~~~

If a confirmatory criterion changes after target results are inspected, the affected result is exploratory unless a protected independent confirmatory test remains.

## 29. Requirement provenance model

Using W3C-PROV-style semantics:

~~~math
\boxed{
SourceEntity
\xrightarrow{InterpretationActivity}
NormalizedRequirement
\xrightarrow{FormalizationActivity}
ExecutableCriterion
\xrightarrow{EvaluationActivity}
ComplianceResult.
}
~~~

Agents/software/responsible researchers are recorded where applicable.

Requirement provenance is not just a URL.

## 30. Compliance result identity

Requirement and compliance result are separate:

~~~math
\boxed{
RID_i
\neq
ComplianceResult_{i,r}.
}
~~~

A requirement may remain unchanged while many scenarios/runs generate different compliance results.

Each compliance result references RID/version, run/scenario/result ID, evaluated QOI, uncertainty, margin, PASS/FAIL/UNRESOLVED, and evaluation method.

## 31. Global requirement gate

~~~math
\boxed{
\begin{aligned}
G_{P1.8}^{design}={}&
G_{taxonomy}
\land G_{authority}
\land G_{provenance}
\land G_{traceability}
\land G_{translation}\\
&\land G_{units}
\land G_{scope}
\land G_{uncertainty}
\land G_{conflict}
\land G_{change}\\
&\land G_{stage}
\land G_{valueFW}
\land G_{experimentalFW}
\land G_{claim}.
\end{aligned}
}
~~~

Design PASS does not imply that any final requirement threshold is qualified.

## 32. Protected DEFERRED items

P1.8 does not invent:
- case regulations;
- operator requirements;
- stakeholder thresholds;
- service minimums;
- safety limits;
- recovery deadlines;
- effectiveness targets;
- resource caps;
- sustainability limits;
- feasibility cutoffs;
- experimental \(\delta_i\) values;
- decision weights/preferences;
- legal precedence;
- compliance outcomes;
- H1–H5 results.

## 33. External references

[1] ISO, ISO/IEC/IEEE 29148:2018 — Systems and software engineering — Life cycle processes — Requirements engineering. https://www.iso.org/standard/72089.html  
[2] NASA Systems Engineering Handbook, §6.2 Requirements Management. https://www.nasa.gov/reference/6-2-requirements-management/  
[3] NASA Systems Engineering Handbook, Appendices C–E. https://www.nasa.gov/reference/system-engineering-handbook-appendix/  
[4] W3C, PROV Overview / PROV-O family. https://www.w3.org/TR/prov-overview/  
[5] JSON Schema Draft 2020-12. https://json-schema.org/draft/2020-12

## 34. Repository authority snapshot

- STAGE4_FEASIBLE_CONTROL_SPECIFICATION_V1.md @ ee3e12ed83a5e4d60d755bdd15d19ee4d5bd550b
- STAGE5_SCIENTIFIC_CONSTITUTION_AND_HANDOFF_V1.md @ 3742632c3a0eda97ec4b6fb85aeb81cb334ed4c2
- H3_SERVICE_AND_STATE_SET_SPECIFICATION_V1.md @ 93a65d884e310e0cb07824deb7d0feafe3c98ff2
- STAGE6_EFFECTIVENESS_TARGET_AND_EVALUATION_PROTOCOL_V2.md @ 63f97b824dc8c77c81a33b3149c7a56e46dcd800
- STAGE6_EFFICIENCY_RESOURCE_AND_EVALUATION_PROTOCOL_V2.md @ a509b91bcb169cad6d8d3b8448d694aac8281fff
- STAGE6_REQUIREMENTS_DERIVATION_PROTOCOL_V1.md @ 3f54bc78a40452544946a8bef3f59c633983ed19
- STAGE6_SUSTAINABILITY_ACCOUNTING_PROTOCOL_V1.md @ 61e7e2ee5aa7189b860fb777fc68617ca55d1fb3
- STAGE7_DECISION_OBJECTIVE_AND_VALUE_FIREWALL_V2.md @ 34197e5d40e3e94c4bc98980ca0fddbc4ec4cfbb
- STAGE7_SCIENTIFIC_CONSTITUTION_AND_HANDOFF_V2.md @ 38a71356b3c99d35d5b73f7b70fb7d32452f71d4
- GLOBAL_FINAL_CASE_SCHEMA_V1.md @ 83c66ee25169bb22f6806642a0753fa589d3f42e
- GLOBAL_H1_H5_MASTER_PREREGISTRATION_V1.md @ 9b80cb8a2bbb882b53ed5dd3f86d007596e0e9f6
- GLOBAL_UNCERTAINTY_VVUQ_CONTROL_V1.md @ 9a74b488697b4eedc2e10f1d4c0201c18992b5e5

## 35. Freeze interpretation

~~~math
\boxed{
G_{P1.8}^{design}=PASS
}
~~~

means the requirements/provenance architecture is complete and auditable at design level.

It does not mean a final case requirement has been selected, interpreted, legally validated or satisfied.
