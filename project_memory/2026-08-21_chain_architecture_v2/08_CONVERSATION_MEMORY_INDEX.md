# Conversation Memory Index — v2

This file routes future chats to the strongest available source for each part of the project history.

## A. 2026-08-20 current-thread archive

Directory:

`conversation/2026-08-20_current_thread/`

Contains:

- `part001.md`
- `part002.md`
- `part003.md`
- `part004.md`
- `final_response.md`

Use these before reconstructing older wording.

## B. User-request archive

`conversation/CURRENT_CONVERSATION_USER_REQUESTS_VERBATIM.md`

This preserves a set of 2026-08-20 user requests, including literature expansion, deduplication, 207/259 selection, Monte Carlo conditions, the dataset-locked prompt request and the GitHub repository request.

## C. Assistant-response record

`conversation/CURRENT_CONVERSATION_ASSISTANT_RESPONSES_RECONSTRUCTED.md`

This is explicitly labeled reconstructed/indexed and summarizes:

- thesis-wide PRISMA/falsification work;
- 259-paper literature expansion;
- duplicate audit;
- high-priority paper selection;
- PRISMA/Monte Carlo conditions;
- 325-dataset-locked protocol;
- GitHub repository creation/population.

Do not quote it as an exact assistant transcript.

## D. 2026-08-21 chain/framework segment

Directory:

`conversation/2026-08-21_chain_framework_segment/`

Files currently include:

- `USER_REQUESTS_VERBATIM.md`
- `SESSION_SUMMARY.md`

The v2 memory adds stricter provenance by separately storing directly visible current-turn requests in:

`project_memory/2026-08-21_chain_architecture_v2/09_USER_REQUESTS_VISIBLE_VERBATIM.md`

and the user's long pasted chain reference in:

`project_memory/2026-08-21_chain_architecture_v2/15_USER_SUPPLIED_CHAIN_REFERENCE_VERBATIM.md`.

## E. Project-history fragments

`conversation/project_history_preserved_request_fragments.md`

Use only for fragments actually present there. Do not fill missing historical wording from model memory.

## F. Authenticity policy

`conversation/AUTHENTICITY_LIMITS.md`

This remains the repository-level authority on what may be called verbatim/authentic.

## G. Project memory versus transcript

Use:

```text
conversation/*
```

for transcript/source wording.

Use:

```text
project_memory/*
```

for current-state scientific synthesis and continuation instructions.

Use:

```text
provenance/*
```

for artifact identity, hashes, archive status and GitHub-vs-external storage distinctions.

## H. What this v2 capsule intentionally does not contain

It does not claim to preserve:

- hidden chain-of-thought;
- system/developer instructions;
- secrets or credentials;
- connector internals;
- messages whose exact content is no longer recoverable.

## I. Recovery rule

When a future chat asks “what did we say before?”, search in this order:

1. exact conversation file;
2. exact prompt/artifact generated from the conversation;
3. current v2 scientific memory;
4. reconstructed assistant summary;
5. only then model recollection, explicitly labeled uncertain.
