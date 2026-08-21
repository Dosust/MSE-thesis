# Bio-Inspired Construction Sustainability Review — Chat Memory Archive

**Archive date:** 2026-08-21  
**Status:** controlled research memory / reproducibility handoff  
**Branch:** `archive/bioinspired-review-chat-2026-08-21`

## Purpose

This folder preserves the scientific decisions, evidence rules, corrections, working artifacts, and next-step protocol developed in the chat concerning the bio-inspired construction sustainability review. It is intended to let a future ChatGPT/Codex/researcher resume the work without reconstructing the logic from memory.

## Non-negotiable evidence rule

Only papers present in the controlled bio-inspiration/construction Scopus corpus are eligible for substantive analysis. Evidence for a focal paper must come from the admitted/saved focal paper evidence. Do not import another paper's evidence, do not silently use general knowledge, and do not convert background mentions into focal implementation.

If the focal saved PDF is unavailable, mark page-level or claim-level fields `PENDING_PDF`, `U`, `NR`, or `NA` rather than guessing.

## Frozen analytical focus

For each eligible focal paper answer:

1. What sustainability assessment method/tool is directly implemented?
2. What specific inputs enter that method/tool, and where do they originate?
3. What engineering/functional performance metrics are measured/calculated/simulated/tested?
4. What sustainability outcomes are actually generated, and what are they specifically?
5. Which engineering-performance metrics actually enter the sustainability assessment, through what transformation, and with what resulting sustainability outcome?

Core chain:

`Assessment tool -> Tool inputs -> Engineering performance -> Sustainability outcomes`

plus the verified linkage:

`Engineering performance -> assessment input/transformation -> sustainability outcome`

## Key distinction

`Author evidence != reviewer interpretation != score/classification`

Extract first. Interpret second. Compare/synthesize only after the evidence layer is frozen.

## Folder map

- `00_SCOPE_CORPUS_AND_EVIDENCE_RULES.md` — binding scope and boundaries.
- `01_CHAT_CHRONOLOGY.md` — chronological decisions from this chat.
- `02_FROZEN_DATA_DICTIONARY.md` — 10-sheet workbook schema and field semantics.
- `03_BIO58_HIGH_RIGOR_STATE.md` — current BIO58 calibration findings and unresolved items.
- `04_ERRORS_CORRECTIONS_AND_CONFLICTS.md` — known errors and corrections that future work must not reintroduce.
- `05_NEXT_STEPS_EXECUTION_PROTOCOL.md` — exact continuation protocol.
- `06_TOP10_REFERENCE_SET.md` — earlier 10-paper engineering-sustainability reference set, explicitly separated from the bio-inspired corpus.
- `07_ZOTERO_TOP10_SUBCOLLECTION.js` — Zotero helper script used in this chat.
- `08_PRESENTATION_CONTEXT.md` — presentation/template context from the start of this chat.
- `09_ARTIFACT_MANIFEST.md` — authoritative files, hashes, and provenance notes.
- `10_AUTHENTIC_USER_REQUESTS.md` — key user requests preserved close to their original wording.
- `state.json` — machine-readable handoff state.

## Critical current state

The Version 1.0 extraction schema is frozen. BIO58 is the calibration paper. The latest high-rigor evidence audit confirms BiSA as the focal assessment architecture, environmental LCA and an economic costing component as embedded methods, and identifies two engineering metrics (residual indentation 0.14 mm; permanent thickness change 0.02 mm) from reviewer-extracted focal evidence. However, the accessible evidence set still does **not** establish a page-anchored direct numeric sustainability output for the BIO58 case; therefore its sustainability-output gate remains unresolved/provisional rather than automatically passing.

The focal PDF binary/page map must be used before closing all `PENDING_PDF` fields.

## Resume rule for future chats

Read this README, then `04_ERRORS_CORRECTIONS_AND_CONFLICTS.md`, `03_BIO58_HIGH_RIGOR_STATE.md`, and `05_NEXT_STEPS_EXECUTION_PROTOCOL.md` before changing any workbook or classification.