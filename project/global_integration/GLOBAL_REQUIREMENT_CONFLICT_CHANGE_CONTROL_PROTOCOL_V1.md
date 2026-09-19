# Global Requirement Conflict and Change-Control Protocol v1

**Date:** 2026-09-19  
**Status:** NORMATIVE P1.8 CHANGE / CONFLICT GOVERNANCE

## 1. Baseline principle

A requirement baseline is a versioned set:

~~~math
\boxed{
\mathcal R^{base}_v
=
\{(RID_i,Ver_i)\}_{i\in\mathcal I_v}.
}
~~~

Confirmatory scenarios/runs must reference the exact baseline version/hash.

## 2. Change classes

~~~text
SOURCE_CHANGE
INTERPRETATION_CHANGE
FORMALIZATION_CHANGE
SCOPE_CHANGE
THRESHOLD_CHANGE
TYPO_METADATA_ONLY
OTHER
~~~

Only TYPO_METADATA_ONLY may leave executable scientific identity unchanged, and only when the correction has no semantic effect.

## 3. Scientific change identity

Changes to any of the following normally create a new requirement version:
- normalized meaning;
- threshold/target;
- comparison operator;
- units/conversion;
- time/spatial aggregation;
- jurisdiction/applicability;
- hardness;
- authority interpretation;
- mathematical expression;
- experimental materiality criterion.

## 4. Impact propagation

For change \(C_j\):

~~~math
\boxed{
Impact(C_j)
=
(
Models,
Scenarios,
Runs,
Hypotheses,
ComplianceResults,
DecisionResults,
Claims
).
}
~~~

Every changed baselined requirement triggers an impact audit before reuse of previous results.

## 5. Result-inspection firewall

If an outcome-relevant requirement/threshold changes after target results were seen:

~~~math
\boxed{
\text{affected confirmatory result}
\rightarrow
\text{EXPLORATORY}
}
~~~

unless a protected independent confirmatory set/test remains.

## 6. Conflict types

~~~text
NUMERIC
LOGICAL
SCOPE
JURISDICTION
TEMPORAL
AUTHORITY
AGGREGATION
SEMANTIC
OTHER
~~~

Examples:
- two applicable service minima differ;
- one source applies system-wide, another only to critical loads;
- old/new standard editions overlap;
- average and instantaneous limits are confused;
- stakeholder preference conflicts with safety constraint.

## 7. Conflict-resolution sequence

For conflict \(C\):

1. verify both sources/versions;
2. verify applicability and effectivity;
3. check whether statements truly address the same quantity/scope;
4. check unit and aggregation compatibility;
5. determine actual governing authority for the case;
6. document engineering/legal/operator resolution basis;
7. version affected requirement(s);
8. propagate to all downstream objects/results.

P1.8 does not invent legal precedence.

## 8. No "stricter wins" shortcut

~~~math
\boxed{
\min/\max\text{ threshold chosen as stricter}
\not\Rightarrow
\text{valid conflict resolution}.
}
~~~

A stricter number can still be inapplicable, obsolete, differently aggregated, or lower-authority.

## 9. Supersession

When source requirement \(R^{v+1}\) supersedes \(R^v\):

- old version is retained for provenance;
- new version receives new effectivity;
- scenario/run results remain bound to the version actually used;
- re-execution need is assessed;
- historical results are not silently recomputed/relabelled.

## 10. Waivers/exceptions

If an authoritative source documents a waiver/exception:
- preserve waiver ID/source;
- scope;
- duration;
- approving authority;
- affected requirement;
- downstream model/decision effect.

Absence of evidence for enforcement is not a waiver.

## 11. Research-assumption changes

Research assumptions may be altered for sensitivity analysis, but:
- new assumption version is recorded;
- scenario/arm identity changes if scientifically material;
- confirmatory arms preserve preregistered values;
- assumption changes cannot be relabeled source updates.

## 12. Change gate

~~~math
\boxed{
G_{change}
=
G_{reason}
\land G_{authority}
\land G_{version}
\land G_{impact}
\land G_{resultblind}
\land G_{provenance}.
}
~~~

A failed change gate blocks use of the revised requirement in confirmatory execution.
