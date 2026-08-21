# Source Artifacts and Current Status

This file records the major artifacts referenced/generated during the chat so future work can distinguish source data, generated analysis, and software scaffolding.

## Core source/workbook artifacts referenced in the chat

- `scopus_Dossiya_review(5).csv` — broad/source CSV supplied in the current conversation; used as the original record source for the Top-10 IDs and K–T context.
- `Top10_Engineering_Sustainability_High_Rigor.xlsx` — high-rigor Top-10 workbook inspected in the current conversation. It contains the current K–T, PFSD, synthesis, visual evidence, visual mapping, and controlled-list structure.
- `Top10_Engineering_Sustainability_Integration_Framework.xlsx` — earlier generated/adapted Top-10 workbook based on the bio-inspiration workbook design.
- `Literature_Review_Framework_Template.xlsx` — earlier generated R1–R4–lambda framework workbook.
- `Column_K_Construction_Screening_Yes_No_Titles.csv` — original K screening reference.
- `Dossiya_216_Eligible_Papers_Only(1).csv` — 216-record K/L/M-eligible extraction dataset referenced in the review history.
- `Coded_Literature_Review_282papers(1).xlsx` — broad coded literature-review workbook visible in the current runtime.

## Full-text / batch assets visible in the current runtime

The working runtime contains many paper PDFs and batch-derived abstract artifacts, including `Batch_01_Verbatim_Abstracts` through `Batch_21_Verbatim_Abstracts` in TXT/DOCX variants, plus numerous construction-sustainability PDFs. These assets are part of the evidence environment but are not individually copied into this GitHub folder by the text-only GitHub contents interface used in this chat.

## Generated software artifact

- `engineering_sustainability_review_modular_python.zip` — modular Python package generated in chat.
- `es_review_smoke_test.xlsx` — synthetic 10-paper workbook smoke test generated during software QA.

The package includes modules for configuration, models, dictionaries, PDF extraction, retrieval, rules, scoring, validation, coverage, mapping, workbook generation, pipeline orchestration, JSON I/O, CLI, and tests.

## Important artifact-status distinction

Generated workbooks and Python tests demonstrate the implementation of the methodology but do not by themselves prove paper-level scientific classifications. Full-text evidence remains authoritative.

## GitHub storage limitation in this archive

The current GitHub connector supports text-file creation/update through the contents API but does not expose a general binary-upload action for local XLSX/PDF/ZIP files. Therefore this archive prioritizes reproducible text specifications and source-code text. Binary artifacts should be committed separately through a Git client or another connector/action when available.

## Reproduction strategy

The combination of:

1. this archive's frozen methodology;
2. the Top-10 paper identifiers/DOIs;
3. the evidence-first relational schema;
4. the Python implementation/source code;
5. the original/full-text PDF corpus;

is intended to make future regeneration of the final evidence workbook possible without relying on conversational memory alone.