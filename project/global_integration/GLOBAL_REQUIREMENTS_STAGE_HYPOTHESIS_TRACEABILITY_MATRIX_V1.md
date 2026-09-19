# Global Requirements Stage / Hypothesis Traceability Matrix v1

**Date:** 2026-09-19  
**Status:** NORMATIVE P1.8 CROSS-STAGE REQUIREMENT TRACEABILITY

## 1. Traceability backbone

~~~math
\boxed{
Source/Need
\leftrightarrow
RID
\leftrightarrow
FormalCriterion
\leftrightarrow
StageObject
\leftrightarrow
Gate/QOI
\leftrightarrow
Scenario/Run
\leftrightarrow
Compliance/Result.
}
~~~

Bidirectional traceability is mandatory for hard constraints and confirmatory experimental criteria.

## 2. Stage ownership matrix

| Stage | Requirement-bearing objects | Requirement role |
|---|---|---|
| S1 | scope/entity/service ontology | defines where requirements can attach; does not invent thresholds |
| S2 | mechanism applicability/validity conditions | causal applicability conditions, not service thresholds |
| S3 | physical operating/capability constraints, case/model validity limits | physical/model execution constraints |
| S4 | \(\mathcal U_{phys},\mathcal U_{info},\mathcal U_{org},\mathcal U_{resource}\) | operational feasibility |
| S5 | \(\mathcal K_{req},K,G_{rec},F_{unsafe},T_V,T_R\) | service/safety/recovery admissibility |
| S6 | effectiveness targets, resource constraints, sustainability requirements | intervention performance/consequence requirements |
| S7 | inherited feasibility + decision admissibility | decision feasibility; preferences remain separate |

## 3. Stage 4

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

Each exclusion reason must trace to:
- physical limit;
- information freshness/availability criterion;
- organization authority/approval condition;
- resource availability condition;
- or explicitly labeled research assumption.

No unknown authority/resource condition may be silently treated as unavailable or available.

## 4. Stage 5

The formal requirement carrier is:

~~~math
\mathcal K_{req}
=
\{RID_i:i\in\mathcal I_5\}.
~~~

It generates:

~~~math
K(t),\qquad G_{rec}(t),\qquad F_{unsafe}(t).
~~~

Trace obligations:

| Stage-5 object | Required provenance |
|---|---|
| \(K_{phys}\) | physical/safety source + model mapping |
| \(K_{svc}\) | service requirement + service-map mapping |
| \(K_{op}\) | operational requirement + control/state mapping |
| \(G_{rec}\) | recovery target + deadline/horizon source |
| \(F_{unsafe}\) | safety/emergency/irreversible-failure basis |
| \(T_V,T_R\) | service/decision/recovery horizon rationale |

## 5. Stage 6 effectiveness

Every effectiveness component:

~~~math
Z_{fx,j}(a_k)
=
\mathbf 1[q_j(a_k)\ \mathcal O_j\ \theta_j]
~~~

must trace:

~~~math
RID_j
\rightarrow
(q_j,\mathcal O_j,\theta_j,unit,aggregation)
\rightarrow
Z_{fx,j}.
~~~

Hard and soft targets remain distinct.

## 6. Stage 6 efficiency/resources

Resource vector components:

~~~math
\mathbf C_{res}^{a_k}
~~~

must identify whether each quantity is:
- merely measured/report-only;
- denominator/input to efficiency;
- or a hard resource feasibility constraint.

Only the last role requires a sourced cap/requirement.

## 7. Stage 6 sustainability

For each sustainability component:

~~~math
J_q^{a_k}
~~~

record separately:
- consequence metric provenance;
- factor/data provenance;
- any hard requirement \(RID_q\);
- materiality criterion if used for H4;
- decision objective/preference role.

These are four different roles.

## 8. Stage 7

Decision admissibility:

~~~math
\mathcal A_7^{adm}
=
\{a_k:\text{all applicable hard feasibility requirements PASS}\}.
~~~

Preferences/weights operate only after feasibility unless a different decision framework is explicitly justified.

~~~math
\boxed{
weight
\not\Rightarrow
feasibility.
}
~~~

## 9. H1 traceability

H1 requires:
- model/coupling comparator definitions;
- any physical validity/capability requirements;
- validation acceptance criteria;
- \(\delta_1\) experimental materiality provenance.

Permanent:

~~~math
\delta_1
\neq
\text{physical/service requirement}
~~~

unless independently sourced.

## 10. H2 traceability

H2 requires:
- information availability/freshness criteria;
- organization authority/resource constraints;
- feasible-control rules;
- \(\delta_2\) experimental criterion.

Research assumptions about organization must remain assumption-class records.

## 11. H3 traceability

H3 requires:
- all RIDs defining \(K,G_{rec},F_{unsafe},T_V,T_R\);
- outcome/label criteria;
- primary metric;
- \(\delta_3\).

The same RIDs/versions must be used in matched H3 arms.

## 12. H4 traceability

H4 requires:
- resilience-improvement eligibility rule \(\delta_R\);
- effectiveness requirements/targets;
- resource feasibility constraints if any;
- sustainability factor/boundary definitions;
- \(\delta_{J,q}\) or primary H4 materiality criterion.

Distinguish:

~~~math
\boxed{
\delta_R
\text{ eligibility/materiality rule}
\neq
\text{operator service requirement}
}
~~~

unless separately sourced as such.

## 13. H5 traceability

H5 requires:
- same upstream requirement set across \(\mathcal X_R\) and \(\mathcal X_{R,S}\);
- same feasibility rules;
- same requirement uncertainty treatment;
- same scenario-set membership;
- primary H5 materiality criterion \(\delta_5\).

Only sustainability information changes between H5 arms.

## 14. Trace-completeness gate

For hard requirement or experimental gate \(RID_i\):

~~~math
\boxed{
G_{trace,i}
=
G_{source}
\land
G_{forward}
\land
G_{reverse}
\land
G_{version}
\land
G_{evaluation}.
}
~~~

If a code threshold cannot be reverse-traced to an RID:

~~~text
BLOCKED — UNTRACEABLE THRESHOLD
~~~

not PASS.
