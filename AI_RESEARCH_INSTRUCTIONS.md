# AI Research Instructions — Active Thesis Entry Point

**Status:** MANDATORY AI ENTRY POINT  
**Effective date:** 2026-10-08  
**Repository:** `Dossiya-SE/MSE-thesis`

Any AI system, research agent, coding assistant, literature-review agent, visualization agent, or autonomous workflow acting on this repository must load the current authority index first:

```text
project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md
```

and must load the evidence/non-invention authority before generating scientific content:

```text
project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md
```

## Mandatory scientific behavior

```text
No invention fills an evidence gap.
If it cannot be traced, it is not frozen.
If it cannot be verified, it remains OPEN.
If it is thesis-derived, it is labeled thesis-derived / T1.
If it is transferred, transferability must be justified.
If evidence conflicts, the conflict is reported.
```

Every scientific claim should use the strongest appropriate provenance class:

```text
[A1] Official standard / code / normative authority
[A2] Exact manufacturer / certified technical documentation
[A3] Peer-reviewed experiment / field measurement
[A4] Peer-reviewed mathematical / physics model
[A5] Recognized textbook / engineering handbook / authoritative theory
[T1] Thesis-derived from A1–A5 evidence
[OPEN] Not yet established
```

## Mandatory load order

1. `project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md`
2. `project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md`
3. `project/CANONICAL_THESIS_TITLE_V1.md`
4. `project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md`
5. `project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md`
6. `project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md`
7. `project/CANONICAL_STATE_TIME_DEFINITIONS_V1.md`
8. other authorities listed by the current authority index as required by the task.

## Prohibited behavior

An AI must not invent or silently infer:
- bibliographic metadata;
- DOI or standard references;
- standard clauses;
- equations presented as established;
- equipment limits or ratings;
- material properties;
- thermal constants;
- derating curves;
- battery/BMS limits;
- service requirements;
- uncertainty bounds;
- validation results;
- numerical findings.

A generic equation or plausible engineering assumption may be discussed as a **candidate** or **generic form**, but it must not be frozen or represented as the final thesis model without source-specific qualification.

## 200-paper school

For literature work, also load:

```text
project/THERMAL_PAPER_SCHOOL_V2.md
project/THERMAL_200_PAPER_SCHOOL_V3_1_EVIDENCE_CONTROLLED.md
```

The target of 200 papers is a coverage target, not permission to invent bibliographic records.

## Governance

If any older file conflicts with the current authority index, use the current authority.

Historical files are provenance only where they conflict.

This entry point does not replace the canonical authorities; it makes them discoverable and mandatory for AI systems.
