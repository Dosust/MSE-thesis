# Repository Implementation Map — Corrected v2

This file records what is actually present in GitHub versus what is preserved off-repository.

## 1. Root scientific portal

`README.md`

Current role:

- thesis proposition;
- central mathematical architecture;
- state/interface notation;
- hybrid multiscale model;
- P–W–T–SW coupling operator;
- climate forcing and waste/drainage feedback;
- admissibility;
- viability/recovery geometry;
- dynamic/static interface comparison;
- inverse problems/UQ;
- control/design extension;
- Type I/II/III alternatives;
- P1–P7 propositions;
- evidence and computational architecture.

### Known root-README issue discovered in this audit

The current root README contains `\nu` / `\nu_t` in places where the intended control variable is `u` / `u_t`, including the control-set and Type-I/Type-II formulas. This is a LaTeX-symbol typo because `\nu` renders Greek nu. The authoritative mathematical-foundation file uses `u` correctly. Future repository maintenance should correct the root README without changing the mathematical meaning.

The authoritative thesis scope also describes the demonstrator as **urban flooding with waste–drainage–transport feedbacks**, whereas the root README's short demonstrator wording emphasizes drainage/waste and mentions the transport effect separately. The v2 memory uses the authoritative scope wording.

## 2. Authoritative scientific specification

- `project/THESIS_SCOPE.md` — strongest current scope authority.
- `project/MATHEMATICAL_FOUNDATION.md` — current formal mathematical foundation.
- `project/SCIENTIFIC_PROPOSITIONS.md` — P1–P7 proposition/falsification table.
- `config/scientific_propositions.yaml` — machine-readable P1–P7 registry.

## 3. Machine-readable model architecture

- `config/example_model.json`
- `schemas/thesis_model.schema.json`

These are software/model-configuration artifacts, not empirical evidence.

## 4. Numerical architecture code

### Python

`methods/architecture/viability_geometry.py`

Role: small auditable synthetic/reference implementation for finite-grid viability geometry, dynamic/static comparison and set-distance QA.

### Julia

`methods/architecture/CoupledInfrastructure.jl`

Role: coupled-dynamics scaffold / numerical architecture smoke-test layer.

### Tests

`tests/test_viability_geometry.py`

### Status

```text
SYNTHETIC_QA / REFERENCE IMPLEMENTATION
```

not a calibrated or validated P–W–T–SW model.

## 5. Scientific QA workflow

`.github/workflows/scientific-architecture-qa.yml`

Current functions include code/model/schema/figure consistency checks and Julia/Python smoke tests.

Passing the workflow establishes software consistency under its tests, not scientific truth of P1–P7.

## 6. Mathematical art

Folder: `assets/math-art/`

- `master_architecture.svg`
- `dynamic_interface_operator.svg`
- `viability_recovery_geometry.svg`
- `README.md`

These are repository-native SVG scientific figures.

## 7. Generated Type I/II/III images

Folder: `assets/frameworks/`

- `type_i_theory_first_framework.webp`
- `type_ii_digital_twin_framework.webp`
- `type_iii_resilience_by_design_framework.webp`
- `framework_comparison_all_types.webp`
- `README.md`
- `SHA256SUMS.txt`

GitHub contains optimized renderable copies. The framework README/provenance material documents the full-resolution original references where applicable.

## 8. Monte Carlo prompt and run records

Prompts:

- `prompts/PRISMA_Monte_Carlo_325_Single_Dataset_Master_Prompt.md`
- `prompts/PRISMA_MC_325_MASTER_PROMPT.md`

High-rigor run GitHub index:

- `methods/monte_carlo/final_run_2026-08-20/README.md`

Important correction:

The `final_run_2026-08-20/` GitHub directory currently contains the **summary README**, not the entire raw ZIP contents. The README points to the complete online high-rigor ZIP and its SHA-256.

Additional Monte Carlo code/results directories:

- `methods/monte_carlo/code_parts/`
- `methods/monte_carlo/reconstruct_code.py`
- `methods/monte_carlo/results/`

Future chats should inspect what is actually present before stating that every raw output is GitHub-committed.

## 9. Online raw archive

`provenance/ONLINE_ARCHIVE.md`

Current registered byte-preserved items include:

- complete 2026-08-20 session artifact ZIP;
- authoritative `(1)` 325-paper CSV;
- dataset-locked Monte Carlo Python implementation;
- PRISMA/Monte Carlo package.

The high-rigor run README also records a complete-run ZIP in Google Drive. These archive records should be reconciled when building one final provenance inventory.

## 10. Conversation archive

Existing files include:

- `conversation/CURRENT_CONVERSATION_USER_REQUESTS_VERBATIM.md`
- `conversation/CURRENT_CONVERSATION_ASSISTANT_RESPONSES_RECONSTRUCTED.md`
- `conversation/AUTHENTICITY_LIMITS.md`
- `conversation/ASSISTANT_RESPONSE_INDEX.md`
- `conversation/project_history_preserved_request_fragments.md`
- `conversation/2026-08-20_current_thread/`
- `conversation/2026-08-21_chain_framework_segment/`

The exact user-request files have higher transcript authority than project-memory summaries.

## 11. Provenance layer

- `provenance/PROVENANCE.md`
- `provenance/ONLINE_ARCHIVE.md`
- `provenance/INVENTORY.csv`
- `provenance/SHA256SUMS.txt`
- `provenance/GITHUB_PUBLISH_STATUS.md`

These should be used to distinguish GitHub-native artifacts from external byte archives.

## 12. Project memory

Superseded v1:

`project_memory/2026-08-21_chain_architecture/`

Corrected canonical v2:

`project_memory/2026-08-21_chain_architecture_v2/`

Root memory pointer should reference v2.

## 13. Programming-language roles

Use tools only where scientifically justified:

- Markdown + LaTeX — specification/derivation;
- Mermaid — inspectable architecture flow;
- SVG — version-controlled mathematical art;
- Python — numerical geometry, UQ/ranking, tests, audit automation;
- Julia — dynamical-systems/ODE/PDE-oriented numerical work where justified;
- JSON/JSON Schema — model configuration contracts;
- YAML — scientific configuration/registry;
- GitHub Actions — reproducibility and automated QA.

Do not add languages merely to maximize language count.