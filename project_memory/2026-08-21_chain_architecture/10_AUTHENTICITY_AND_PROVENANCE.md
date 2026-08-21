# Authenticity, Provenance and Reproducibility Rules

## 1. Why this file exists

The repository contains a mixture of exact transcripts, reconstructed summaries, mathematical definitions, proposed models, generated images, synthetic numerical demonstrations, literature metadata and closed-corpus ranking outputs. Future chats must not collapse these into one evidence category.

## 2. Authenticity classes

### A. Verbatim transcript
May be labeled **verbatim** only when the exact user-visible text is preserved from the conversation/source.

Existing authoritative locations include:

- `conversation/2026-08-20_current_thread/`
- `conversation/CURRENT_CONVERSATION_USER_REQUESTS_VERBATIM.md`

### B. Reconstructed assistant summary
Must be labeled **reconstructed**, **summary**, or **project-state synthesis**.

Existing example:

- `conversation/CURRENT_CONVERSATION_ASSISTANT_RESPONSES_RECONSTRUCTED.md`

### C. Scientific synthesis
Files in this memory capsule are mostly scientific synthesis. They preserve the current project state but are not a word-for-word transcript.

### D. Source artifact
Datasets, prompts, code and generated images retain their own file/hash provenance. Do not rewrite them and then call the rewrite the original.

## 3. Hidden/private material exclusion

Do not archive or claim to archive:

- hidden chain-of-thought;
- system/developer instructions;
- credentials, API keys, secrets;
- private connector internals;
- material the user did not see and is not part of a legitimate project artifact.

## 4. Evidence-state classes

Each scientific claim should be identifiable as one of:

1. `VERIFIED_FULL_TEXT` — proposition supported by inspected full text/evidence anchor;
2. `VERIFIED_METADATA` — bibliographic identity verified but proposition not fully anchored;
3. `CORPUS_DERIVED` — result derived from a declared dataset/protocol;
4. `MATHEMATICAL_DEFINITION` — formal definition/theory, not empirical evidence;
5. `PROPOSED_HYPOTHESIS` — thesis claim awaiting falsification;
6. `SYNTHETIC_QA` — computation on synthetic/reference data/models;
7. `EMPIRICAL_RESULT` — calibrated/observed result with declared data;
8. `PENDING` — not yet verified/completed.

## 5. Literature citation rule

The memory file `05_LITERATURE_ANCHORS.md` records literature already invoked in the conversation. Before thesis/publication use, recover the exact authoritative corpus/PDF record and verify:

- authors;
- title;
- year;
- venue;
- DOI;
- exact pages/equations/claims used;
- whether the cited source truly supports the proposition.

Do not use memory alone as a final bibliographic authority.

## 6. PRISMA / ranking rule

Closed-corpus ranking supports only corpus-relative statements. It does not prove:

- global literature completeness;
- global novelty;
- the universally best paper;
- the scientifically necessary number of papers.

Keep PRISMA search/screening separate from Monte Carlo importance ranking.

## 7. Numerical-model rule

The committed architecture code under `methods/architecture/` is currently a **reference/synthetic QA implementation** unless a later file explicitly documents calibration and validation.

Passing software tests means:

- code executes as expected under the tests;
- invariants/schemas pass;
- synthetic geometry behavior is reproducible.

It does **not** mean:

- real P–W–T–SW dynamics are validated;
- a hypothesis is empirically confirmed;
- a theorem has been proved.

## 8. Mathematical-claim rule

Distinguish proof from computation.

Examples:

- numerical trajectory existence is not a proof of existence for all admissible initial conditions;
- one converged optimizer is not a proof of global uniqueness;
- finite-grid viability is an approximation, not the exact viability kernel;
- an HJ numerical solution requires consistency/stability/convergence assumptions to justify approximation to the viscosity solution;
- a reduced model requires an explicit preservation/error statement before using its viability set as a decision guarantee.

## 9. Image provenance

Generated framework images are stored in `assets/frameworks/` with hashes and references to full-resolution originals.

Repository-native mathematical art is stored in `assets/math-art/` as SVG.

Do not present generated conceptual graphics as observed empirical data.

## 10. Binary/raw archive

Large/raw artifacts that could not be directly committed through the active GitHub connector are tracked through `provenance/ONLINE_ARCHIVE.md`, `provenance/INVENTORY.csv` and `provenance/SHA256SUMS.txt`.

A GitHub link to an index is not equivalent to the raw bytes being stored in GitHub.

## 11. Versioning rule

When a scientific definition, proposition, dataset lock or model architecture changes:

1. document the amendment date;
2. state the old and new definitions;
3. state why the change was made;
4. identify affected code/figures/results;
5. rerun dependent QA/analysis;
6. avoid retroactively describing earlier runs as if they used the amended protocol.

## 12. Future-chat rule

A future chat should never say “I remember that X was proven/verified” solely because this memory capsule says it. It should inspect the linked authoritative artifact/evidence state before making a high-stakes scientific claim.

The memory capsule is designed for **high recall**, while the source/provenance files provide **high evidential authority**.