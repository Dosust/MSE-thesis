# Online Publication Status

Repository: `Dossiya-SE/MSE-thesis`  
Visibility: **private**  
Publication branch: `archive-import`  
Date: 2026-08-20

## Fully online and directly readable

- `00_project_overview/THESIS_SCOPE.md`
- `conversation/README.md`
- `conversation/user_requests_verbatim_2026-08-20.md`
- `conversation/current_request_full_2026-08-20.md`
- `conversation/project_history_preserved_request_fragments.md`
- `conversation/AUTHENTICITY_LIMITS.md`
- `conversation/assistant_final_responses_2026-08-20_part_01.md`
- `conversation/assistant_final_responses_2026-08-20_part_02.md`
- `conversation/assistant_final_responses_2026-08-20_part_03.md`
- `methods/prisma/PRISMA_MC_325_CONDITIONS.md`
- `methods/monte_carlo/MASTER_PROMPT_PRISMA_MONTE_CARLO_325_DATASET_ONLY.txt`
- `methods/monte_carlo/CODE_RECONSTRUCTION.md`
- `archive/BINARY_ARTIFACTS.md`

## Authoritative 325-paper corpus — complete lossless online representation

The authoritative corpus is online under:

`data/authoritative_325_encoded/`

Files:

- `MANIFEST.json`
- `part_01.b64`
- `part_02.b64`
- `part_03.b64`
- `part_04.b64`
- `part_05.b64`

Original source:

`Thesis_Final_Unique_Papers_325_2026-08-20(2).csv`

Original SHA-256:

`047e80b7348190a9da8100758c5f1201cd39059f9318e6298dcda614ecb7813f`

Reconstruction:

```bash
cd data/authoritative_325_encoded
cat part_*.b64 | base64 --decode | gunzip > 'Thesis_Final_Unique_Papers_325_2026-08-20(2).csv'
sha256sum 'Thesis_Final_Unique_Papers_325_2026-08-20(2).csv'
```

The reconstructed SHA-256 must equal the value above.

## Exact Monte Carlo Python source — complete lossless online representation

Online encoded source:

`methods/monte_carlo/prisma_monte_carlo_rank_325.py.gz.b64`

Original Python source SHA-256:

`f128651e3aa2781b1579bdfbf54ed65c11aa8916583e71b731c555356eaf9e8e`

Reconstruction:

```bash
cd methods/monte_carlo
base64 --decode prisma_monte_carlo_rank_325.py.gz.b64 | gunzip > prisma_monte_carlo_rank_325.py
sha256sum prisma_monte_carlo_rank_325.py
```

## Conversation provenance

The repository distinguishes:

- `AUTHENTIC_CURRENT_THREAD` — exact request text available in the active thread;
- `AUTHENTIC_PRESERVED_FRAGMENT` — exact older fragments available from project context, not reconstructed full messages;
- `VISIBLE_ASSISTANT_FINAL_RESPONSE` — visible assistant final-answer text preserved from conversation context;
- generated prompts/method files — separate from authentic user requests.

No hidden chain-of-thought, system/developer messages, or tool-internal payloads are represented as user-visible conversation content.

Where a complete older verbatim transcript is unavailable, the repository says so rather than inventing missing text.

## Binary research artifacts

Large `.zip`, `.xlsx`, `.pdf`, and `.gitbundle` artifacts are **not claimed as directly uploaded through the GitHub connector**. Their exact filenames, byte sizes, and SHA-256 values are recorded in:

`archive/BINARY_ARTIFACTS.md`

This is a connector transport limitation, not a scientific omission. Local repository-ready and Git-bundle packages remain preserved separately.

## Source snapshot

A local compressed snapshot of all currently available non-binary thesis source files was created and SHA-256 hashed. The prior `archive/source_text_snapshot/MANIFEST.json` records that its split-part upload was not completed; this repository does not falsely mark it complete.

Critical source objects needed to reproduce the current literature-ranking protocol are nevertheless already online individually: the 325 corpus, PRISMA/MC conditions, full master prompt, exact Python implementation, thesis scope, and conversation provenance.

## Branch / merge state

All publication work is on `archive-import`.

The branch is deliberately **not merged into `main`** because GitHub merge is a separate write action requiring explicit authorization under the connected GitHub workflow. The materials are already online and accessible in the private repository from the `archive-import` branch.
