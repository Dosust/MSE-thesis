# Provenance

## Scope

This repository was populated from artifacts available in the active MSE thesis conversation/session on 2026-08-20 and from the user's existing private GitHub repository `Dossiya-SE/MSE-thesis`.

## Provenance classes

- `AUTHENTIC_USER_REQUEST`: verbatim user-visible request text.
- `ASSISTANT_GENERATED_PROMPT`: generated prompt saved as an exact artifact.
- `ASSISTANT_GENERATED_CODE`: generated executable code.
- `DERIVED_DATASET`: table produced by deduplication, ranking, filtering, or audit.
- `SOURCE_DATASET`: dataset supplied or designated as an input during the conversation.
- `BINARY_REPORT_OR_WORKBOOK`: generated report/workbook/preview/archive.
- `SUMMARY_NOT_VERBATIM`: explanatory index or project summary.

## Scientific caution

Corpus sizes from different audits are not additive unless deduplicated. The 325-row Monte Carlo protocol is a closed-corpus analysis and may not import earlier corpora as ranking evidence.

## Conversation caution

The repository does not expose hidden chain-of-thought, system instructions, developer instructions, secrets, credentials, or private connector internals. These are not user-facing conversation content.
