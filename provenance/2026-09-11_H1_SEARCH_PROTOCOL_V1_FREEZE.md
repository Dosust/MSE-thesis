# H1 Fresh Evidence Search Protocol v1.0 — Freeze Record

**Date:** 2026-09-11  
**Canonical file:** `project/H1_FRESH_EVIDENCE_SEARCH_PROTOCOL_V1.md`  
**Canonical creation commit:** `22ed47fcf857129660978db3847ad5b8b74e1424`  
**Source SHA-256:** `aedf57f2fd0d4614ba57f5911a598c3a63b25e9f57c3d48a74e1fbf5325a1c59`  
**Status:** FROZEN v1.0 FOR INITIAL DATABASE EXECUTION

## Scientific freeze decision

The first executable search protocol for confirmatory hypothesis $H_1$ is frozen. The primary discovery architecture is

```math
Q_{H_1}^{\rm CORE}=B_P\land B_T\land B_I,
```

while

```math
Q_{H_1}^{\rm DYN}=B_P\land B_T\land B_I\land B_D
```

is retained only as a diagnostic/sensitivity query.

This preserves static-coupling and foundational comparator studies required to discriminate

```math
M_0=\text{independent},\qquad
M_1=\text{static coupling},\qquad
M_2=\text{dynamic causal coupling}.
```

The dynamic/cascade vocabulary therefore does not define the primary discovery universe.

## Frozen execution scope

The v1.0 protocol contains executable translations for:

- Scopus;
- Web of Science Core Collection;
- Compendex / Engineering Village;
- IEEE Xplore.

The initial search imposes no substantive restrictions on year beyond database inception to the search date, geography, hazard, transport mode, power subsystem, language filter, or open-access status.

Eligibility, evidence-role tags, exclusion codes, title/abstract screening logic, and the full-text decision rule are frozen before screening.

## Immutability rule

Once v1.0 is executed, it must never be silently edited. Any change to a term, operator, field, filter, proximity condition, controlled vocabulary term, or coverage rule creates a new version with a documented reason for change.

```math
Q^{v1}\neq Q^{v2}.
```

## Next operation

Execute the four frozen CORE queries in their authenticated database interfaces, preserve the exact executed strings, record result counts, export all raw records, hash the exports, and construct

```math
\mathcal P_{H_1}^{raw}
=
P_{\rm Scopus}\cup P_{\rm WoS}\cup P_{\rm Compendex}\cup P_{\rm IEEE}.
```

Only after raw-corpus construction should DOI/database-ID/title deduplication and title–abstract screening begin.

## Preservation note

The canonical GitHub version preserves the supplied scientific logic. Presentation-only normalization removed fragile `\tag{...}` usage, repaired malformed Markdown table headers, and expressed equation labels as Markdown text so the file follows the repository's GitHub mathematical-display standard.