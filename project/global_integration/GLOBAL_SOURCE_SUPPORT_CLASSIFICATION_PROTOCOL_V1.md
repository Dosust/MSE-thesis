# Global Source-Support Classification Protocol v1

**Status:** CANONICAL P1.11.6 EVIDENCE-SEMANTICS CONTROL  
**Effective date:** 2026-09-19  
**Purpose:** prevent repository-consistency PASS from being mistaken for direct source support or case validation.

## 1. Two independent axes

Every source-integration audit item shall record:

~~~math
\boxed{
STATUS_i=
(REPO_i,SOURCE_i).
}
~~~

### Repository-consistency axis

~~~text
PASS
BLOCKED
FAIL
DEFERRED
N/A
~~~

### Source-support axis

~~~text
DIRECT
CONCEPTUAL
METHOD_PRECEDENT
THESIS_DERIVED_COMPATIBLE
THESIS_AUTHORITY_CONSISTENT
OTHER_QUALIFIED_SOURCE
CASE_VALIDATED
NONE
BLOCKED
~~~

## 2. Meaning

DIRECT means the supplied source directly supports the bounded proposition.

CONCEPTUAL means the source explicitly motivates the concept but does not validate the thesis implementation.

METHOD_PRECEDENT means the source supports a method family or architecture, not the thesis-specific result.

THESIS_DERIVED_COMPATIBLE means the mathematics/object is constructed by this thesis and is compatible with the source; it must not be attributed to the source.

THESIS_AUTHORITY_CONSISTENT means the item comes from another frozen thesis authority, not from the source under audit.

CASE_VALIDATED requires case-specific validation evidence. No P1.11 source-integration artifact currently receives CASE_VALIDATED merely because a literature source exists.

## 3. PASS-count rule

Historical counts such as 42/42, 36/36, 48/48, 46/46, 50/50 and 54/54 are interpreted as documented **repository-consistency checklist counts**.

They are not:
- machine test coverage;
- independent replication;
- source-support counts;
- empirical validation.

## 4. Machine checks versus scientific judgments

Text/identity/authority invariants may be machine tested.

Scientific judgments such as whether a source directly supports a proposition remain evidence-review judgments and must carry page/section provenance.

## 5. Claim ceiling

~~~math
\boxed{
REPO=PASS
\not\Rightarrow
SOURCE=DIRECT
\not\Rightarrow
CASE\_VALIDATED.
}
~~~
