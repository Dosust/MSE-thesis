# Repository Implementation Map

This file records what was actually implemented in GitHub so future chats can distinguish **implemented artifacts** from proposed work.

## 1. Root scientific portal

`README.md`

Role:

- research proposition;
- central mathematical architecture;
- notation;
- hybrid multiscale model;
- P–W–T–SW coupling operator;
- climate forcing and waste–drainage feedback;
- sustainability/equity admissibility;
- viability and recovery geometry;
- dynamic-interface proposition;
- inverse problems/UQ;
- control/design/optimization;
- Type I/II/III thesis alternatives;
- falsifiable propositions;
- demonstrator;
- evidence architecture;
- computational implementation;
- literature-ranking status;
- repository/provenance/privacy.

## 2. Project mathematical specification

### `project/THESIS_SCOPE.md`
Defines current title, sector set, demonstrator, scientific architecture and evidence strategy.

### `project/MATHEMATICAL_FOUNDATION.md`
Formal mathematical objects and architecture.

### `project/SCIENTIFIC_PROPOSITIONS.md`
Human-readable P1–P7 proposition/falsification plan.

## 3. Machine-readable scientific configuration

### `config/scientific_propositions.yaml`
Machine-readable proposition registry used by QA.

### `config/example_model.json`
Example model instance.

### `schemas/thesis_model.schema.json`
JSON Schema contract for model-configuration structure.

## 4. Numerical/scientific computing layer

### `methods/architecture/viability_geometry.py`
Small auditable Python reference implementation for:

- deterministic finite-horizon admissibility;
- finite-grid viability approximation;
- static and time-varying reference interface fields;
- finite point-cloud Hausdorff distance;
- synthetic dynamic/static boundary-deformation smoke test.

Important status: **synthetic QA/reference layer only**. It is not the calibrated thesis model and does not establish empirical infrastructure conclusions.

### `methods/architecture/CoupledInfrastructure.jl`
Julia scaffold for coupled infrastructure dynamics/multiscale model logic.

### `methods/architecture/README.md`
Implementation architecture and Mermaid documentation.

## 5. Automated tests / QA

### `tests/test_viability_geometry.py`
Python tests for geometry/reference utilities.

### `.github/workflows/scientific-architecture-qa.yml`
Automated scientific-architecture QA that checks:

- Python syntax;
- numerical smoke tests;
- P1–P7 proposition-registry integrity;
- JSON Schema validity;
- example-model validation;
- SVG parsing/validity;
- Julia model smoke tests.

The QA layer verifies implementation consistency, not physical calibration or theorem truth.

## 6. Mathematical art

Folder: `assets/math-art/`

- `master_architecture.svg` — main mathematical/scientific architecture;
- `viability_recovery_geometry.svg` — viable/recoverable/nonrecoverable state-space geometry;
- `dynamic_interface_operator.svg` — P–W–T–SW dynamic coupling representation;
- `README.md` — mathematical-art purpose/documentation.

Design principle: state-space geometry, vector-field/network/operator language, reachable/viability boundaries and formal mathematical structure should dominate; avoid decorative stock-style visuals when explaining scientific mechanisms.

## 7. Generated Type I/II/III frameworks

Folder: `assets/frameworks/`

GitHub-renderable images:

- `framework_comparison_all_types.webp`;
- `type_i_theory_first_framework.webp`;
- `type_ii_digital_twin_framework.webp`;
- `type_iii_resilience_by_design_framework.webp`.

Also:

- `assets/frameworks/README.md`;
- `assets/frameworks/SHA256SUMS.txt`.

The framework README links the byte-preserved PNG originals stored in the connected online archive.

## 8. PRISMA / Monte Carlo

### Prompts

- `prompts/PRISMA_MC_325_MASTER_PROMPT.md`
- `prompts/PRISMA_Monte_Carlo_325_Single_Dataset_Master_Prompt.md`

### Methods/results

- `methods/monte_carlo/code_parts/`
- `methods/monte_carlo/reconstruct_code.py`
- `methods/monte_carlo/results/`
- `methods/monte_carlo/final_run_2026-08-20/`

## 9. Conversation archive

Folder: `conversation/`

Important files:

- `conversation/AUTHENTICITY_LIMITS.md`;
- `conversation/CURRENT_CONVERSATION_USER_REQUESTS_VERBATIM.md`;
- `conversation/CURRENT_CONVERSATION_ASSISTANT_RESPONSES_RECONSTRUCTED.md`;
- `conversation/ASSISTANT_RESPONSE_INDEX.md`;
- `conversation/project_history_preserved_request_fragments.md`;
- `conversation/2026-08-20_current_thread/part001.md` through `part004.md`;
- `conversation/2026-08-20_current_thread/final_response.md`.

The existing transcript/archive should be preferred over reconstructing historical wording from memory.

## 10. Provenance

Folder: `provenance/`

- `PROVENANCE.md`;
- `GITHUB_PUBLISH_STATUS.md`;
- `ONLINE_ARCHIVE.md`;
- `INVENTORY.csv`;
- `SHA256SUMS.txt`;
- `SCIENTIFIC_IMPLEMENTATION_PLAN_2026-08-20.md`.

These records distinguish GitHub-committed text/assets from raw/binary artifacts preserved elsewhere.

## 11. GitHub Actions already present

- `.github/workflows/python-package.yml`
- `.github/workflows/reconstruct-framework-images.yml`
- `.github/workflows/scientific-architecture-qa.yml`

## 12. Current memory-capsule layer

This folder, `project_memory/2026-08-21_chain_architecture/`, is intentionally additive. It does not replace the original source/provenance files. Its role is to give future chats a controlled, high-recall entry point.

## 13. Language/tool roles already frozen

Use languages only where they have a scientific/reproducibility purpose:

- Markdown + LaTeX: scientific narrative and formal equations;
- Mermaid: inspectable architecture diagrams;
- SVG: version-controlled mathematical art;
- Python: numerical geometry, UQ/ranking, tests, data QA;
- Julia: dynamical-systems scaffold and future high-performance dynamics/ODE/PDE work where justified;
- YAML: machine-readable scientific configuration;
- JSON / JSON Schema: model configuration and validation contracts;
- GitHub Actions: continuous QA/reproducibility.

Do not add programming languages merely to maximize language count.