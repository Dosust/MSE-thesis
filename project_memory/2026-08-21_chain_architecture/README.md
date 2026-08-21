# Canonical Thesis Memory Capsule — 2026-08-21

This folder is the **high-rigor recall and reproducibility entry point** for future chats working on the MSE thesis repository.

It consolidates the scientific state reached across the current thesis discussion without replacing the original transcript, source files, prompts, datasets, code, figures, or provenance records already stored elsewhere in the repository.

## Purpose

A future chat should be able to recover, in a controlled order:

1. the current thesis identity and mathematical center;
2. the six-chain scientific ontology and its layers;
3. the three end-to-end thesis alternatives (Type I, II, III);
4. the governing mathematical objects and frozen propositions;
5. the literature anchors already used in the discussion;
6. the PRISMA / closed-corpus Monte Carlo status and its epistemic limits;
7. the implemented repository code, schemas, mathematical art and QA;
8. the exact current-segment user requests that drove this architecture;
9. unresolved questions and the next scientifically valid actions;
10. authenticity/provenance rules that prevent reconstructed material from being mislabeled as verbatim evidence.

## Read order for future chats

1. [`00_EXECUTIVE_MEMORY.md`](00_EXECUTIVE_MEMORY.md)
2. [`01_SCIENTIFIC_STATE.md`](01_SCIENTIFIC_STATE.md)
3. [`02_SIX_CHAINS_AND_LAYERS.md`](02_SIX_CHAINS_AND_LAYERS.md)
4. [`03_MATHEMATICAL_OBJECTS_AND_PROPOSITIONS.md`](03_MATHEMATICAL_OBJECTS_AND_PROPOSITIONS.md)
5. [`04_TYPE_I_II_III_FRAMEWORKS.md`](04_TYPE_I_II_III_FRAMEWORKS.md)
6. [`05_LITERATURE_ANCHORS.md`](05_LITERATURE_ANCHORS.md)
7. [`06_PRISMA_MONTE_CARLO_STATE.md`](06_PRISMA_MONTE_CARLO_STATE.md)
8. [`07_REPOSITORY_IMPLEMENTATION_MAP.md`](07_REPOSITORY_IMPLEMENTATION_MAP.md)
9. [`08_VERBATIM_CURRENT_SEGMENT_REQUESTS.md`](08_VERBATIM_CURRENT_SEGMENT_REQUESTS.md)
10. [`09_OPEN_QUESTIONS_AND_NEXT_ACTIONS.md`](09_OPEN_QUESTIONS_AND_NEXT_ACTIONS.md)
11. [`10_AUTHENTICITY_AND_PROVENANCE.md`](10_AUTHENTICITY_AND_PROVENANCE.md)
12. [`11_FUTURE_CHAT_BOOTSTRAP.md`](11_FUTURE_CHAT_BOOTSTRAP.md)
13. [`PROJECT_MEMORY.yaml`](PROJECT_MEMORY.yaml)
14. [`manifest.json`](manifest.json)

## Canonical scientific spine

```text
observations
→ interface / parameter identification + uncertainty
→ coupled hybrid multiscale dynamics
→ hazard / failure / service mapping
→ sustainability-equity admissibility
→ viability geometry
→ recovery / capture geometry
→ admissible control
→ design / optimization / decision
```

The central geometric object is the viability boundary `∂V_R`. The core thesis question is not merely “how resilient is the system?” but **what moves the sustainable-equitable viability boundary, how uncertain is it, and what interventions/designs move it favorably?**

## Existing authoritative repository locations

- Root scientific portal: `README.md`
- Thesis scope: `project/THESIS_SCOPE.md`
- Mathematical foundation: `project/MATHEMATICAL_FOUNDATION.md`
- Scientific propositions: `project/SCIENTIFIC_PROPOSITIONS.md`
- Machine-readable proposition registry: `config/scientific_propositions.yaml`
- Model schema: `schemas/thesis_model.schema.json`
- Example model: `config/example_model.json`
- Numerical geometry scaffold: `methods/architecture/viability_geometry.py`
- Julia coupled-system scaffold: `methods/architecture/CoupledInfrastructure.jl`
- Mathematical art: `assets/math-art/`
- Type I/II/III generated frameworks: `assets/frameworks/`
- Scientific QA workflow: `.github/workflows/scientific-architecture-qa.yml`
- Conversation authenticity policy: `conversation/AUTHENTICITY_LIMITS.md`
- Current-thread transcript archive: `conversation/2026-08-20_current_thread/`
- Provenance registry: `provenance/`
- Closed-corpus Monte Carlo prompt: `prompts/PRISMA_Monte_Carlo_325_Single_Dataset_Master_Prompt.md`
- Final closed-corpus Monte Carlo run: `methods/monte_carlo/final_run_2026-08-20/`

## Interpretation rule

This memory capsule is a **project-state synthesis**. It may summarize verified, proposed, simulated, or pending material, but those states must remain distinguished. It must never be used to convert a proposal into an established fact, a synthetic QA model into a calibrated thesis result, a corpus-relative ranking into a global literature claim, or a reconstruction into a verbatim transcript.