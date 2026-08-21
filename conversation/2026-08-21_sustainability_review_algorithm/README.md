# Sustainability Review Algorithm — Conversation Memory

Date: 2026-08-21
Repository: `Dossiya-SE/MSE-thesis`
Status: authoritative memory package for this conversation segment

## Purpose

This folder preserves the methodological evolution of the sustainability/construction literature-review work discussed in the chat so that future conversations can reproduce the logic without relying on conversational memory.

It records:

- the original K–T screening/extraction logic for the 216-paper review;
- the distinction between 216 eligible records and 202 original full-text PDFs;
- the addition of 5 new full research PDFs, giving 207 available full papers for strict full-text assessment;
- the evolution from coarse OK/NO OK checking toward evidence-grounded field validation;
- the strict R1–R4–L methodological algorithm;
- the Core/Extended Tier A, B1, B2, B3 route logic;
- the separation of methodological eligibility from review relevance;
- the 31-paper candidate-validation pool;
- known provisional/disputed classifications and corrections;
- the final paper-level evidence matrix, provenance codes, quality controls, equations, dynamic state model, and operational algorithm;
- the 2-minute sustainability-history video content developed at the end of the conversation.

## Canonical governing principle

> Extraction determines scoring; scoring must never determine extraction.

The current final architecture is a two-axis, non-compensatory evidence system:

1. **Methodological eligibility** determines whether a paper can enter the analytical corpus.
2. **Review relevance** determines how important an eligible paper is to the synthesis.

Therefore:

`Eligibility != Relevance`

A relevant paper cannot repair a failed methodological gate. A methodologically strong paper may still be only moderately relevant to the final review question.

## Folder contents

- `SESSION_TIMELINE.md` — chronological development and major decisions.
- `USER_REQUESTS_VERBATIM.md` — authentic user instructions and wording preserved from this segment.
- `DECISIONS_AND_CORRECTIONS.md` — errors, inconsistencies, reconciliations, and final resolutions.
- `FINAL_FROZEN_PROTOCOL.md` — authoritative mathematical/methodological protocol.
- `CANDIDATE_POOL_31.md` — exact candidate pool currently retained for validation and relevance scoring.
- `REPRODUCIBILITY_AND_HANDOFF.md` — instructions for future chats/reviewers.
- `VIDEO_SUSTAINABILITY_2MIN.md` — 2-minute sustainability history/dimensions content and source context.

Canonical code/schema mirrors are also stored at repository level under:

- `methods/evidence_gated_review_algorithm.py`
- `schemas/paper_evidence_record.schema.json`

## Data-state distinctions that must not be confused

- **216 papers**: earlier eligible review set after K–M screening.
- **202 papers**: original papers with complete PDF/full-text extraction available in the combined corpus.
- **5 new full papers**: later uploaded and assessed separately.
- **207 full papers**: 202 + 5 available full papers for the strict full-text algorithm.
- **31 papers**: current candidate-validation pool assembled from the strict evidence review. They are not automatically eligible.

## Non-negotiable future-chat rules

1. Do not score a paper from title/abstract alone when full text is available.
2. Do not credit a review paper with methods/results generated only by cited studies.
3. Do not treat case-study application as validation automatically.
4. Keep engineering performance separate from sustainability outcomes.
5. R3 strong evidence must be author-generated.
6. R4 must come from an implemented sustainability method.
7. L must describe an actual engineering–sustainability relationship, not mere co-occurrence.
8. Use exact passages, page/section/table/figure locations, provenance, score implication, and confidence for every score-relevant claim.
9. Apply route logic before relevance scoring.
10. The final number of papers must emerge from the frozen rules; never tune the algorithm to force a target number.
