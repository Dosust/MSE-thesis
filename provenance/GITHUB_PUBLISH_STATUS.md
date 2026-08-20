# GitHub publish status

Repository: `Dossiya-SE/MSE-thesis`  
Visibility: **private**  
Branch: `main`

## Published directly to GitHub

The repository contains the version-controlled thesis research record, including:

- project README and current thesis scope;
- conversation authenticity/provenance rules;
- verbatim current-conversation user requests available in retained context;
- ordered current-thread transcript parts containing user-visible requests and assistant outputs;
- preserved historical request fragments only where exact wording was available;
- correctly labeled assistant-response index/reconstruction records;
- exact generated PRISMA / Monte Carlo master prompts;
- Monte Carlo audit, convergence summary, robust Top-50 result, and current-thread code snapshot/reconstruction utility;
- mathematical-physics architecture material;
- artifact inventory and SHA-256 provenance registry;
- online-archive pointers for the complete raw artifact bundle.

## Raw byte archive online and independently verified

The byte-preserving active-session archive is stored in the user's connected Google Drive and linked from `provenance/ONLINE_ARCHIVE.md`.

### Complete active-session bundle

`MSE-thesis-current-session-artifacts-2026-08-20.zip`

- Size: `2,703,060 bytes`
- SHA-256: `6d2682356ad0ba4a879c3ee398f4fc65fa60f4b2b9899e5e369820dfa1f92e8c`
- Connected-Drive readback: **PASS**
- Independent downloaded-byte SHA-256 verification: **PASS**

### Authoritative 325-paper CSV

`Thesis_Final_Unique_Papers_325_2026-08-20(1).csv`

- Size: `215,584 bytes`
- SHA-256: `047e80b7348190a9da8100758c5f1201cd39059f9318e6298dcda614ecb7813f`
- Connected-Drive readback: **PASS**
- Independent downloaded-byte SHA-256 verification: **PASS**

### Dataset-locked Monte Carlo Python artifact

`prisma_monte_carlo_rank_325.py`

- Size: `43,640 bytes`
- SHA-256: `5de1e80817b05456b6969f986828bbb6af6272709d88e73a9062daa332c76a15`
- Connected-Drive readback: **PASS**
- Independent downloaded-byte SHA-256 verification: **PASS**

A separate current-thread Python snapshot is preserved as split GitHub source under `methods/monte_carlo/code_parts/`; its distinct SHA-256 is documented there. The two code artifacts are not conflated.

### PRISMA + Monte Carlo package

`PRISMA_Monte_Carlo_325_Single_Dataset_Package.zip`

- Size: `22,192 bytes`
- SHA-256: `0994fa11d97f31630240e9a73bf898afbbcffb0c0fd88b87a2b6f878390b1191`
- Connected-Drive readback: **PASS**
- Independent downloaded-byte SHA-256 verification: **PASS**

## Artifact-byte inventory

`provenance/INVENTORY.csv` records exact file names, byte sizes, and SHA-256 values for source datasets, derived corpora, prompts, Python code, workbooks, reports, previews, and ZIP packages prepared in the active session.

## Authenticity boundary

- Exact user-visible text is labeled verbatim only when exact wording is actually available.
- Older missing wording is not reconstructed and called authentic.
- Generated prompts/code are separated from authentic user requests.
- Hidden chain-of-thought, system/developer instructions, secrets, credentials, and connector internals are not included as conversation content.
- The current assistant message cannot become a prior authentic transcript entry before it has actually been sent; the archive therefore has an explicit cutoff marker for the in-progress turn.

## GitHub connector boundary

The GitHub writer available in this session accepts UTF-8 repository content but does not expose a mounted-local-file argument for arbitrary binary artifacts. Large/binary artifacts are therefore preserved in the verified online byte archive and indexed cryptographically from GitHub instead of being falsely described as directly committed binary files.

No incomplete Base64 archive is treated as authoritative.
