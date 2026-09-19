# Global Requirement Authority / Type Matrix v1

**Date:** 2026-09-19  
**Status:** NORMATIVE P1.8 AUTHORITY AND SEMANTIC CONTROL

## 1. Two independent axes

Every record has both:

~~~math
\boxed{
Kind(R_i)
\quad\text{and}\quad
Authority(R_i).
}
~~~

They are not interchangeable.

A requirement kind describes what role the statement plays.
An authority class describes why/how the statement has standing.

## 2. Authority matrix

| Authority class | May establish hard requirement? | Conditions | May be overridden by thesis preference? |
|---|---|---|---|
| LAW_REGULATION | yes, when applicable | jurisdiction/effectivity/applicability verified | NO |
| MANDATED_STANDARD | yes, when contract/regulation/operator mandates it | mandate and edition verified | NO |
| VOLUNTARY_STANDARD | only if adopted for case/design | adoption rationale/scope explicit | preference cannot silently override adopted rule |
| CONTRACTUAL | yes within contract scope | contract authority/applicability verified | NO |
| OPERATOR_POLICY | yes within operator authority | current policy/version/scope verified | NO |
| OPERATOR_ENGINEERING | yes/soft depending source | operator standing and scope verified | not silently |
| STAKEHOLDER_ELICITED | may define service/target need | elicitation/authority/population scope documented | requires governance when conflicting |
| SAFETY_ENGINEERING | may define safety criterion | derivation/evidence/owner approval explicit | not by ordinary preference |
| CASE_ENGINEERING_DERIVED | may define design criterion | parent/rationale/verification explicit | may change only through change control |
| PEER_REVIEWED_EVIDENCE | supports derivation; normally not authority by itself | interpretation + case applicability required | N/A |
| MANUFACTURER_SPECIFICATION | constrains component capability if applicable | model/version/conditions verified | cannot exceed documented component envelope without evidence |
| EXPERIMENTAL_PREREGISTRATION | governs experiment/adjudication only | frozen prospectively | not a real-system authority by default |
| RESEARCH_ASSUMPTION | NO external authority | must remain labeled assumption | may be varied/sensitivity-tested |
| VALUE_MODEL | preference/decision role only | elicitation/value provenance required | not a feasibility authority |
| INSTITUTIONAL_POLICY | governs thesis/program process | institutional scope verified | does not define case physics/service by default |

## 3. Kind × hardness rules

| Kind | Default hardness | Allowed promotion condition |
|---|---|---|
| EXTERNALLY_IMPOSED_REQUIREMENT | hard according to source | none; source controls semantics |
| OPERATOR_REQUIREMENT | source-dependent | operator source + applicability |
| STAKEHOLDER_REQUIREMENT | soft or hard depending governance | explicit authority/decision rule |
| ENGINEERING_DERIVED_REQUIREMENT | case-dependent | traceable derivation + approval |
| SAFETY_CRITERION | HARD_SAFETY when qualified | safety derivation/authority |
| SERVICE_CRITERION | hard or soft | case service authority |
| RECOVERY_CRITERION | hard or soft | case recovery authority |
| CONTROL_FEASIBILITY_CONSTRAINT | HARD_FEASIBILITY | physical/info/org/resource basis |
| EFFECTIVENESS_TARGET | SOFT_TARGET by default | promote only if independent hard requirement |
| RESOURCE_CONSTRAINT | HARD_FEASIBILITY when cap is sourced | resource authority/source |
| SUSTAINABILITY_REQUIREMENT | source-dependent | independent requirement, not metric existence |
| DECISION_FEASIBILITY_CONSTRAINT | HARD_FEASIBILITY | inherited/qualified feasibility authority |
| EXPERIMENTAL_PREREGISTRATION_CRITERION | EXPERIMENTAL_GATE | never promoted from observed effect size |
| RESEARCH_ASSUMPTION | ASSUMPTION | cannot self-promote |
| VALUE_PREFERENCE | PREFERENCE | cannot become feasibility constraint without new authority |
| INSTITUTIONAL_REQUIREMENT | hard for thesis process | institutional scope only |

## 4. Non-promotion rules

~~~math
\boxed{
\text{peer-reviewed evidence}
\not\Rightarrow
\text{regulation}
}
~~~

~~~math
\boxed{
\text{manufacturer nominal value}
\not\Rightarrow
\text{operator requirement}
}
~~~

~~~math
\boxed{
\text{simulation default}
\not\Rightarrow
\text{engineering requirement}
}
~~~

~~~math
\boxed{
\text{objective}
\not\Rightarrow
\text{constraint}
}
~~~

~~~math
\boxed{
\text{preference}
\not\Rightarrow
\text{feasibility}.
}
~~~

## 5. Stage-specific role matrix

| Requirement domain | Primary owner | Typical consumers |
|---|---|---|
| physical/safety | S3/S5 depending object | S3–S7 |
| operational control | S4 | S5–S7 |
| service/recovery | S5 | S5–S7 |
| effectiveness | S6 | S6–S7 |
| resource efficiency/constraints | S6 | S6–S7 |
| sustainability | S6 | S6–S7 |
| decision feasibility | S7, inherited from upstream | S7 |
| experimental method/materiality | owning hypothesis stage/global preregistration | H1–H5 adjudication |
| thesis institutional | INSTITUTIONAL | manuscript/degree process |

## 6. Source evidence versus authority

A source can be strong evidence but have no authority to impose a requirement.

Example:

~~~math
\boxed{
\text{high-quality empirical paper}
\neq
\text{case operator mandate}.
}
~~~

Conversely an applicable legal/operator requirement may be authoritative even when the thesis does not independently estimate its optimality.

## 7. Applicability dominates convenience

Before using an external requirement:

~~~math
\boxed{
G_{app}
=
G_{jurisdiction}
\land
G_{effective}
\land
G_{asset/population}
\land
G_{condition}
\land
G_{version}.
}
~~~

If \(G_{app}\neq PASS\), the record cannot be applied as an authoritative case constraint.
