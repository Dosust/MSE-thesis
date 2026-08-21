# Code Archive

This folder preserves the Python implementation state developed in chat for reproducibility.

## Status

The generated modular package (`engineering_sustainability_review_modular_python.zip`) was a **v0.1 logic/workbook scaffold**. It passed a synthetic perfect-vector self-test and a 10-record workbook smoke test, but it predates the final evidence-dossier preference and the later `AF/AC/RR/NF` formula-type correction.

Therefore:

- `legacy_v0_1/` preserves the original generated source logic for reproducibility.
- The methodological authority is the specification in the parent folder, especially `01_DATA_DICTIONARY_AND_BOUNDARIES.md`, `03_ALGORITHM_AND_PIPELINE.md`, and `06_DECISION_LOG_AND_CORRECTIONS.md`.
- A future v0.2 implementation should use multiple evidence rows per paper and derive summaries/matrices downstream.
- Do **not** interpret the legacy code as proof that any real paper is perfect; real-paper classifications remain evidence dependent.

## Legacy v0.1 modules

The chat-generated package contained configuration, enums, data models, keyword dictionaries, PDF I/O, retrieval, method rules, scoring, validation, coverage, mapping, workbook generation, pipeline orchestration, JSON I/O, CLI, examples, and tests.

## Required v0.2 changes

1. Add `AC` = author causal/process architecture to formula types.
2. Replace one-summary-row-per-paper PFSD storage with relational P/F/S/D evidence records.
3. Keep full exact passages and context before interpretation.
4. Store method-family R2 components as rows/fields rather than concatenated text.
5. Derive visual and mapping matrices from validated evidence tables.
6. Resolve `LCSA + outranking` versus `Hybrid MCDM` taxonomy redundancy.
7. Include zero-coverage categories in visual taxonomies.
8. Preserve `→` only for verified analytical dependence and `||` for parallel evidence.

The legacy code is archived to preserve the exact computational path that produced the earlier QA results.