# Artifact Index — Chain Architecture Session

This file tells future chats where to find the concrete artifacts referenced in this session.

## 1. Repository

`Dossiya-SE/MSE-thesis`

Default branch at archive start: `main`.

This memory package was created on feature branch:

`chat-memory-chain-architecture-2026-08-21`

## 2. Frozen 325-paper corpus

Canonical frozen-corpus SHA-256 used by the PRISMA/Monte Carlo work:

`047e80b7348190a9da8100758c5f1201cd39059f9318e6298dcda614ecb7813f`

Known repository/online provenance for the frozen corpus and Monte Carlo code should be read from the existing `provenance/` files before creating another copy.

## 3. Exact PRISMA/Monte Carlo prompt

Repository file:

`prompts/PRISMA_MC_325_MASTER_PROMPT.md`

This is the authoritative prompt record corresponding to the dataset-only 325-paper ranking protocol discussed in the chat.

## 4. Monte Carlo output families discussed

Visible package names supplied/used in the session:

- `PRISMA_MC_325_EXECUTED_2026-08-20(3).zip`
- `PRISMA_MC_325_FULL_RUN_RESULTS(3).zip`
- `PRISMA_MC_325_HIGH_RIGOR_RUN_2026-08-20(3).zip`

The repository already contains Monte Carlo methods/results and run summaries under `methods/monte_carlo/`. Future chats must inspect existing run manifests/hashes before assuming these packages are identical.

A known high-rigor 50k run summary is stored under the repository's Monte Carlo final-run documentation, with its full ZIP preserved through the project's existing online archive/provenance mechanism.

## 5. 100k executed output filenames

The executed 100k session produced the requested output family:

1. `01_PRISMA_Gated_All_325.csv`
2. `02_MC_Ranked_Eligible.csv`
3. `03_MC_Top_50.csv`
4. `04_Prior_Rank_Validation_Only.csv`
5. `05_Rank_Acceptability_Matrix.csv`
6. `06_Audit.json`
7. `07_README.txt`
8. executable Python implementation used for the exact run

A ZIP bundle was also created in-session. If future publication work needs exact bytes, use the archived run artifact/provenance path, not a reconstructed table from chat text.

## 6. Framework figures

Already versioned on `main` under:

`figures/thesis_framework_types/`

Files:

- `Type_I_Theory_First_Mathematical_Physics_Framework.webp`
- `Type_II_Inference_Digital_Twin_Framework.webp`
- `Type_III_Design_Optimization_Decision_Framework.webp`
- `README.md`

The figures are optimized repository display copies. The project previously preserved higher-resolution generated-source images separately; use the existing provenance/index before regenerating them.

## 7. User-provided architecture source documents in this session

Two attachment-only source documents were used heavily:

- `Pasted markdown(20260820-081500).md`
  - six interacting chains;
  - full master-chain wording;
  - dedicated lifecycle chain;
  - decision chain;
  - cross-cutting mathematical spine;
  - recommendation to freeze the six-chain wording architecture.

- `Pasted markdown(20260820-083013).md`
  - ranking of chains by mathematical/mathematical-physics depth;
  - Chain I governing-system emphasis;
  - Chain IV viability/reachability emphasis;
  - Chain II inverse-problem role;
  - existence/uniqueness/stability/sensitivity/identifiability hierarchy;
  - effort-allocation heuristic;
  - recommendation to couple Chain I + II + IV with III/V supporting.

These were treated as user-provided source material. Future chats should not silently replace their terminology with a different ontology.

## 8. Existing architecture/project folders

Before adding new architecture material, inspect:

- `methods/architecture/`
- `project/`
- `figures/`
- `conversation/`
- `provenance/`

The repository has been actively developed across multiple thesis conversations, so duplication and stale architecture files are possible.

## 9. Current memory-package files

`conversation/2026-08-21_chain_architecture_memory/`

contains:

- `README.md`
- `FUTURE_CHAT_BOOTSTRAP.md`
- `USER_REQUESTS_VERBATIM.md`
- `SESSION_TIMELINE.md`
- `SIX_CHAIN_MASTER_ARCHITECTURE.md`
- `TYPE_I_II_III_THESIS_FRAMEWORKS.md`
- `LITERATURE_GROUNDED_MATHEMATICS.md`
- `MONTE_CARLO_RANKING_MEMORY.md`
- `ARTIFACT_INDEX.md`
- `DECISIONS_OPEN_QUESTIONS.md`
- `PROVENANCE_AND_AUTHENTICITY.md`

Additional source snapshots/index updates may be added on the same feature branch if required.

## 10. Reproducibility rule

For any future computational or literature claim:

1. identify the exact source file/run;
2. record SHA-256 where available;
3. distinguish raw artifact from narrative summary;
4. distinguish current model version from earlier ranking/model variants;
5. never infer binary/file presence from a filename alone;
6. never claim a file is on `main` until GitHub readback confirms it.