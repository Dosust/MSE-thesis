# Global Requirement Verification / Validation / Compliance Protocol v1

**Date:** 2026-09-19  
**Status:** NORMATIVE P1.8 REQUIREMENT QUALITY AND EVALUATION CONTROL

## 1. Four separate questions

~~~math
\boxed{
\text{requirement-quality verification}
\neq
\text{need/requirement validation}
\neq
\text{system/model validation}
\neq
\text{compliance evaluation}.
}
~~~

### Requirement-quality verification
Is the requirement statement/formalization usable, consistent, unambiguous enough, traceable and verifiable?

### Need/requirement validation
Does the requirement correctly represent the relevant need/authority/context?

### System/model validation
Is the model adequate for the context of use? Governed by P1.7.

### Compliance evaluation
Does a specific scenario/run/intervention satisfy the frozen requirement?

## 2. Requirement-quality checklist

Before BASELINED/PASS, check as applicable:
- unique ID/version;
- one controlled meaning;
- necessary role/rationale;
- correct terminology;
- source/authority;
- traceability;
- measurable/evaluable variables;
- explicit units;
- explicit direction/operator;
- aggregation;
- scope/applicability;
- feasibility/consistency;
- no conflict with active baseline;
- evaluation method.

This is informed by ISO/IEC/IEEE 29148 requirements-engineering processes and NASA Appendix C good-requirement/traceability checklists.

## 3. Need/requirement validation

Validation evidence may include:
- direct applicable regulation/standard text;
- operator confirmation/policy;
- stakeholder elicitation;
- engineering/safety analysis;
- empirical evidence supporting a derived criterion;
- institutional policy for thesis-process requirements.

The evidence class depends on requirement type.

A literature citation alone does not validate that a threshold is an operator requirement.

## 4. Formalization verification

For source statement \(S\) translated to \(g(x,t;\kappa)\), verify:
- sign/direction;
- units;
- variable/QOI mapping;
- time aggregation;
- spatial/population aggregation;
- boundary conditions;
- equality/strictness semantics;
- threshold source;
- code implementation.

Where possible, use PASS/FAIL boundary fixtures.

## 5. Compliance margin

For \(q\ge\theta\):

~~~math
m=q-\theta.
~~~

For \(q\le\theta\):

~~~math
m=\theta-q.
~~~

Positive margin denotes satisfaction under the declared sign convention.

But:

~~~math
\boxed{
m
\text{ without uncertainty}
\neq
\text{certain compliance}.
}
~~~

## 6. Compliance uncertainty

Compliance evaluation must combine relevant:
- measurement uncertainty;
- state-estimation uncertainty;
- model/input uncertainty;
- numerical uncertainty;
- requirement/interpretation uncertainty.

If probability semantics are justified, probabilistic compliance may be reported.

Otherwise use interval/set/scenario classification stability.

## 7. Hard-requirement evaluation

For hard requirement set \(\mathcal H\):

~~~math
\boxed{
PASS_{hard}
\iff
Compliance_i=PASS
\quad
\forall i\in\mathcal H.
}
~~~

No compensatory weighting is allowed across hard requirements.

## 8. Soft-target evaluation

Soft targets may generate:
- attainment status;
- margin;
- distance;
- report-only vector;
- effectiveness information.

Failure of a soft target does not automatically imply infeasibility.

## 9. Unknown/BLOCKED requirement

If the requirement itself is BLOCKED/DEFERRED:

~~~math
\boxed{
Compliance=\text{UNRESOLVED}.
}
~~~

Do not choose a placeholder threshold merely to produce PASS/FAIL.

## 10. Requirement baseline versus result

~~~math
\boxed{
RequirementBaselineID
\neq
ScenarioID
\neq
ComplianceResultID.
}
~~~

The same requirement baseline can evaluate many scenarios.

## 11. H1–H5 use

Experimental materiality criteria are verified for:
- prospective freeze;
- calculation;
- traceability;
- correct endpoint.

They are not validated as real-system service requirements unless independently sourced.

## 12. Evaluation gate

~~~math
\boxed{
G_{comp}
=
G_{req}
\land
G_{input}
\land
G_{QOI}
\land
G_{unit}
\land
G_{aggregation}
\land
G_{uncertainty}
\land
G_{implementation}
\land
G_{provenance}.
}
~~~

If \(G_{comp}\neq PASS\), the requirement cannot support a confirmatory compliance claim.

## 13. Wording control

Allowed:
- "Requirement RID-X is sourced from [authority], applies under [scope], and is represented as [criterion]."
- "Scenario S satisfied RID-X under the declared uncertainty/evaluation rule."
- "Compliance is unresolved because the threshold/applicability evidence is blocked."

Prohibited:
- "industry standard" with no identified standard;
- "operator requirement" with only a research paper;
- "regulatory limit" with no applicable regulation;
- "safe" based only on a thesis assumption.
