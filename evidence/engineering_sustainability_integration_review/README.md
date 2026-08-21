# Engineering–Sustainability Integration Review — Reproducibility Archive

This folder preserves the current frozen understanding of the construction-sustainability literature-review workflow developed in chat. Its purpose is high-rigor recall, reproducibility, and continuity across future chats and research sessions.

## Research object

The review is not simply asking whether a construction paper mentions sustainability. The central analytical chain is:

$$
\boxed{
Q_{\mathrm{construction\ strategy}}
\rightarrow
P_{\mathrm{engineering}}
\rightarrow
F_{\mathrm{integration}}
\rightarrow
S_{\mathrm{sustainability}}
\rightarrow
D_{\mathrm{decision}}
}
$$

The distinctive scientific question is how focal construction/built-environment studies generate engineering/functional performance evidence, implement sustainability assessment methods, connect the two evidence streams, and use the combined evidence in a decision.

## Governing principles

1. **Extract first; interpret second; score third.**
2. **Keywords are retrieval cues, not evidence.** A keyword hit must lead to a supporting passage and verified focal-author action before coding.
3. **No guessing.** Missing/unclear information is coded `NR`, `U`, or `NA` rather than inferred.
4. **Author text is preserved separately from interpretation.** Exact passages, page/section/table/figure/equation location, and author terminology are retained.
5. **The unit of analysis is one focal publication.** One paper may contain multiple P, F, S, and D evidence records.
6. **Engineering performance is not a sustainability output.** Sustainability outputs are kept separate unless the authors explicitly integrate the domains.
7. **Total scores never compensate for failed essential gates.** Eligibility is conjunctive/route-based.
8. **Reviewer-created formulas do not justify maximum integration.** Only author-implemented integration can support $\lambda=3$.
9. **The 10-paper set is a reference-archetype set, not merely a ranking of “best papers.”** All 10 were selected from the adjudicated perfect-score corpus to represent different integration architectures.

## Current corpus history

The broad workflow contained 216 records that had passed the earlier K–M eligibility screen. The available full-text state later used in the project was 202 original PDFs plus 5 additional PDFs = 207 available full texts. A first-review audit identified 40 provisional perfect-score candidates; a second-review audit retained 31 papers at the perfect methodological vector `(3,3,3,3,3)`. Ten papers were then selected as reference archetypes for detailed methodological comparison.

The Python framework previously created in chat generated the scoring/workbook infrastructure; it did not itself automatically prove paper-level scores. Paper-level claims must remain tied to full-text evidence.

## Files in this archive

- `01_DATA_DICTIONARY_AND_BOUNDARIES.md` — frozen definitions for K–T, PFSD, R1–R4, $\lambda$, provenance, validation, and evidence states.
- `02_MATHEMATICAL_SPECIFICATION.md` — formulas, conjunctions, matrices, mappings, and invariants.
- `03_ALGORITHM_AND_PIPELINE.md` — deterministic evidence-first pipeline suitable for direct Python implementation.
- `04_WORKBOOK_AND_DATA_MODEL.md` — relational evidence tables, sheet architecture, columns, row logic, and formula rules.
- `05_TOP10_REFERENCE_SET.md` — the ten selected papers and their intended archetypal role.
- `06_DECISION_LOG_AND_CORRECTIONS.md` — corrections made during discussion and items that must not regress.
- `07_KEYWORD_CONCEPT_DICTIONARIES.md` — controlled P/F/S/D search cues and their boundary conditions.
- `08_IMPLEMENTATION_NOTES.md` — Python architecture, integrity tests, and reproducibility expectations.
- `09_CHAT_MEMORY.md` — compact chronological memory of the reasoning and decisions needed to continue the work in a future chat.
- `10_SOURCE_ARTIFACTS_AND_STATUS.md` — workbook/CSV/PDF/software artifact inventory and binary-storage limitations.
- `11_PROMPT_AND_REQUEST_HISTORY.md` — major user requests and evolving priorities preserved for future chats.
- `12_OPEN_TASKS_AND_FREEZE_CHECKLIST.md` — unresolved items and the exact conditions required before final freeze.
- `code/README.md` — status of the generated Python implementation and required v0.2 changes.
- `code/legacy_v0_1/` — archived core v0.1 Python source modules, tests, source manifest, and QA hashes.

## Source-of-truth hierarchy

When files disagree, use this order:

$$
\boxed{
Decision\ Log
\rightarrow
Data\ Dictionary/Mathematical\ Specification
\rightarrow
Algorithm
\rightarrow
Evidence\ Tables
\rightarrow
Interpretation/Scoring
\rightarrow
Derived\ Workbook
}
$$

The legacy Python code is preserved for reproducibility but is superseded where the decision log documents later methodological corrections.

## Non-negotiable final interpretation

The analytical framework is designed to answer:

> **How do construction and built-environment studies generate engineering-performance evidence, implement sustainability assessment methods, transform or integrate those evidence streams, and use the resulting information to support construction decisions?**

The central bridge of interest is $F_{\mathrm{integration}}$.

## Current implementation priority

The next implementation should build a full evidence dossier for the 10 selected papers rather than compressing them immediately into one-row summaries:

$$
\boxed{Raw\ Evidence\rightarrow Interpretation\rightarrow Scoring\rightarrow Synthesis}
$$

The user should be able to read the extracted content as written in each paper and independently design/validate the interpretation.