# MSE Thesis — Mathematical Physics of Sustainable Infrastructure Resilience

Private research repository for the MSE thesis program:

**Mathematical Physics of Sustainable Infrastructure Resilience**  
*Equity-Constrained Viability of Coupled Power–Water–Transportation–Solid-Waste Systems with Dynamic Interfaces under Climate Stress*

## Scientific architecture

The current governing architecture is:

`observations → interface identification / uncertainty → dynamic coupled model → sustainability/equity admissible set → viability geometry → recovery/capture geometry`

Physical demonstrator: **Power–Water–Transportation–Solid Waste (P–W–T–SW)**.  
Primary demonstrator hazard: **urban flooding / drainage-waste feedback**.

## Repository structure

- `.github/` — reproducibility/CI workflow material.
- `project/` — current thesis scope and research architecture.
- `conversation/` — preserved current-thread transcript, verbatim user requests, historical request fragments, assistant-response records, and authenticity limits.
- `prompts/` — exact generated PRISMA / Monte Carlo execution prompts available in the project.
- `data/` — frozen-corpus payload/reconstruction material and research-data provenance.
- `methods/architecture/` — mathematical-physics architecture material.
- `methods/monte_carlo/` — Monte Carlo source fragments, reconstruction utility, and ranked-result outputs.
- `archive/` — session snapshot documentation.
- `provenance/` — inventory, SHA-256 registry, online byte-archive links, and publication status.

## Conversation provenance

The current 2026-08-20 user-visible thread is preserved in ordered parts under:

`conversation/2026-08-20_current_thread/`

The repository also contains:

- `conversation/CURRENT_CONVERSATION_USER_REQUESTS_VERBATIM.md`
- `conversation/AUTHENTICITY_LIMITS.md`
- `conversation/CURRENT_CONVERSATION_ASSISTANT_RESPONSES_RECONSTRUCTED.md`

The reconstructed assistant-response file is deliberately **not** labeled verbatim. Exact generated prompts/code are stored separately whenever available. Hidden chain-of-thought, system/developer instructions, secrets, credentials, and connector internals are not part of the user-visible transcript archive.

## Raw artifact archive

The byte-preserving session ZIP, authoritative 325-paper CSV, dataset-locked Monte Carlo Python implementation, and PRISMA + Monte Carlo package are stored online in the user's connected Drive and linked from:

`provenance/ONLINE_ARCHIVE.md`

Their exact hashes are recorded in:

- `provenance/INVENTORY.csv`
- `provenance/SHA256SUMS.txt`

This preserves large/binary artifacts without falsely claiming they were committed to GitHub when the active GitHub connector could not accept mounted binary files directly.

## Important evidence rule

Historical corpus sizes are not added without deduplication. PRISMA governs transparent identification/screening; Monte Carlo ranks robustness **within a specified eligible corpus**. Neither proves global novelty.

## Current single-dataset Monte Carlo lock

The latest ranking protocol is hard-locked to:

`Thesis_Final_Unique_Papers_325_2026-08-20(1).csv`

SHA-256:

`047e80b7348190a9da8100758c5f1201cd39059f9318e6298dcda614ecb7813f`

The 325-row protocol forbids using prior ranking fields as predictors and treats its Top-K result as a ranking **within that locked dataset only**.

## Privacy

This repository is private. It contains research-development history, prompts, datasets, and conversation material intended for thesis provenance and reproducibility.
