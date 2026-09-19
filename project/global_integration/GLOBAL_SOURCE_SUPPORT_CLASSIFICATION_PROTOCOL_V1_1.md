# Global Source-Support Classification Protocol v1.1

**Status:** CANONICAL SUCCESSOR TO V1
**Effective date:** 2026-09-19
**Parent:** GLOBAL_SOURCE_SUPPORT_CLASSIFICATION_PROTOCOL_V1.md
**Purpose:** normalize repository consistency, source support and thesis-case validation as three independent axes.

## 1. Three-axis status

Every source-integration item shall record:

~~~math
\boxed{
STATUS_i=(REPO_i,SOURCE_i,CASE_i).
}
~~~

## 2. Repository-consistency axis

~~~text
PASS
BLOCKED
FAIL
DEFERRED
N/A
~~~

This axis concerns repository/design consistency only.

## 3. Source-support axis

~~~text
DIRECT
CONCEPTUAL
METHOD_PRECEDENT
THESIS_DERIVED_COMPATIBLE
THESIS_AUTHORITY_CONSISTENT
OTHER_QUALIFIED_SOURCE
NONE
BLOCKED
~~~

CASE_VALIDATED is not a source-support category.

## 4. Thesis-case validation axis

~~~text
VALIDATED
PARTIALLY_VALIDATED
NOT_TESTED
BLOCKED
FAIL
N/A
~~~

This axis records validation status in the thesis case/context of use. It does not itself adjudicate H1–H5.

## 5. Example

~~~text
REPO   = PASS
SOURCE = METHOD_PRECEDENT
CASE   = NOT_TESTED
~~~

## 6. Historical interpretation

Earlier two-axis P1.11-family records remain historical snapshots.

Where no separate CASE value was recorded, do not infer validation from SOURCE. For pre-data P1.11 source-integration artifacts, the safe default is:

~~~text
CASE = NOT_TESTED
~~~

unless a later qualified case-validation authority explicitly states otherwise.

## 7. Permanent firewall

~~~math
\boxed{
REPO=PASS
\not\Rightarrow
SOURCE=DIRECT
\not\Rightarrow
CASE=VALIDATED.
}
~~~

And:

~~~math
\boxed{
\text{source support}
\neq
\text{case validation}
\neq
\text{hypothesis outcome}.
}
~~~
