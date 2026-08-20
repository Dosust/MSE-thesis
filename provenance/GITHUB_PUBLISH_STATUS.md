# GitHub publish status

Repository: `Dossiya-SE/MSE-thesis`  
Visibility: **private**  
Branch: `main`

## Published directly to GitHub

The repository currently contains:

- the project README and current thesis scope;
- conversation authenticity/provenance rules;
- verbatim current-conversation user requests that are available in the visible thread;
- a correctly labeled reconstructed/indexed assistant-response record;
- the exact 325-paper closed-corpus PRISMA + Monte Carlo master prompt;
- the artifact inventory and SHA-256 provenance registry;
- online-archive pointers for the complete raw artifact bundle.

## Raw byte archive online

A byte-preserving ZIP of the active 2026-08-20 thesis session is stored in the user's connected Google Drive and linked from:

`provenance/ONLINE_ARCHIVE.md`

Archive SHA-256:

`6d2682356ad0ba4a879c3ee398f4fc65fa60f4b2b9899e5e369820dfa1f92e8c`

A separate ZIP for the 325-paper PRISMA + Monte Carlo package is also stored online and linked from the same file.

## Artifact-byte inventory

`provenance/INVENTORY.csv` records exact file names, byte sizes, and SHA-256 values for the source datasets, derived corpora, prompts, Python code, workbooks, reports, previews, and ZIP packages prepared in the active session.

## GitHub connector boundary

The GitHub text writer available in this session accepts UTF-8 text directly. It does not expose a mounted-local-file argument for arbitrary binary artifacts. Large/binary session artifacts are therefore preserved in the online byte archive and indexed cryptographically from GitHub rather than being falsely described as GitHub-committed files.

This is an explicit provenance distinction, not a loss of the artifacts.
