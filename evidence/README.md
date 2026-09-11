# Evidence Layer

![Role](https://img.shields.io/badge/role-evidence%20%26%20review%20records-0969DA)
![Authority](https://img.shields.io/badge/framework%20authority-project%2F-6B7280)

This directory contains literature-review protocols, extraction records, evidence matrices and other source-grounding artifacts. It **does not define the canonical thesis ontology or mathematical framework**.

## Authority boundary

The active scientific source of truth is under [`../project/`](../project/), especially:

- [`../project/THESIS_SCOPE.md`](../project/THESIS_SCOPE.md)
- [`../project/CANONICAL_7_STAGE_FRAMEWORK.md`](../project/CANONICAL_7_STAGE_FRAMEWORK.md)
- [`../project/CANONICAL_SYSTEM_DEFINITION.md`](../project/CANONICAL_SYSTEM_DEFINITION.md)
- frozen stage-specific specifications.

Evidence files may use local variables, review categories or extraction schemas that are valid **within their own protocol**. Such local notation must not silently override P–T–I–O notation in the canonical framework.

## Evidence discipline

Every review/extraction workflow should preserve:

1. source identity and bibliographic anchor;
2. explicit inclusion/exclusion boundary;
3. direct distinction between source-reported evidence and reviewer-derived coding;
4. provenance for numerical values, equations and classifications;
5. no stronger claim than the source supports;
6. APA 7 author–date citation and DOI conventions in thesis-facing outputs;
7. a clear note when the evidence artifact predates the frozen seven-stage framework.

## Rendering discipline

Markdown evidence records should use the same repository display contract where practical:

- inline math `$...$`;
- display math `$$...$$`;
- readable tables rather than oversized mathematical arrays;
- no decorative color without a semantic label;
- local notation defined before use.

The automated linter checks machine-detectable Markdown issues without rewriting historical evidence content.

## Current evidence collections

`engineering_sustainability_integration_review/` is a bounded evidence-synthesis workflow. Its data dictionary and extraction rules remain local to that review; it does not redefine the canonical P–T–I–O system or frozen stage objects.
