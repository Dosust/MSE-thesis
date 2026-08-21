# Canonical Thesis Memory Capsule v2 — 2026-08-21

**Status:** corrected canonical memory snapshot for future thesis chats.  
**Supersedes:** `project_memory/2026-08-21_chain_architecture/` for recall purposes.  
**Does not delete or rewrite:** the v1 capsule, conversation archive, prompts, code, figures, Monte Carlo archives, source datasets, or provenance records.

## Why v2 exists

A second audit against the repository's authoritative files found several issues in v1 that required correction rather than silent overwrite:

1. the primary demonstrator was incompletely summarized; the authoritative scope says **urban flooding with waste–drainage–transport feedbacks**;
2. the core thesis architecture was mixed with the broader long-term design/decision chain; the authoritative MSE scope centers on **dynamic coupling → admissibility → viability → recovery**, with identification/UQ upstream and control/design as extensions;
3. the current formal proposition registry **P1–P7** was too casually merged with the historical hypothesis labels **H0–H7/T1**;
4. the Monte Carlo memory needed to distinguish the frozen logical dataset name `(1)` from a byte-identical `(4)` copy used in the archived high-rigor run;
5. transcript recovery needed stricter separation between text directly visible in the current segment, older request text already preserved in GitHub, and reconstructed scientific summaries;
6. the repository's closed-corpus `HIGH_RIGOR_RUN` archive and the later comparative conclusion that `FULL_RUN_RESULTS` is the closest implementation of the frozen title-scoring rule must be kept distinct.

See [`14_CORRECTION_LOG.md`](14_CORRECTION_LOG.md).

## Authoritative scientific sources used for this audit

The v2 capsule was reconciled primarily against:

- `project/THESIS_SCOPE.md`
- `project/MATHEMATICAL_FOUNDATION.md`
- `project/SCIENTIFIC_PROPOSITIONS.md`
- `config/scientific_propositions.yaml`
- `prompts/PRISMA_Monte_Carlo_325_Single_Dataset_Master_Prompt.md`
- `methods/monte_carlo/final_run_2026-08-20/README.md`
- `provenance/ONLINE_ARCHIVE.md`
- `conversation/CURRENT_CONVERSATION_USER_REQUESTS_VERBATIM.md`
- `conversation/CURRENT_CONVERSATION_ASSISTANT_RESPONSES_RECONSTRUCTED.md`
- current visible conversation turns and the v1 memory capsule for audit comparison.

## Correct current thesis identity

**Working title:** *Mathematical Physics of Sustainable Infrastructure Resilience*.

**Current precise formulation:** *Equity-Constrained Viability of Coupled Power–Water–Transportation–Solid-Waste Systems with Dynamic Interfaces under Climate Stress*.

**Physical system:** Power (P), Water/Drainage (W), Transportation (T), Solid Waste (SW).

**Primary demonstrator:** **urban flooding with waste–drainage–transport feedbacks**.

## Core MSE architecture

```text
D_obs
→ (G_hat, theta_hat, Sigma_theta)
→ F_dyn
→ K_R
→ V_R
→ C_R
→ U_recovery
```

The core contribution is centered on:

```text
dynamic coupling
→ admissibility
→ viability
→ recovery
```

with **identification/UQ upstream** and **control/design downstream as structured extensions**.

The central geometric object is:

```text
∂V_R
```

## Broader long-term research program

The broader program extends beyond the core MSE:

```text
observe
→ infer
→ model
→ stress/failure
→ viability/recovery
→ control
→ design
→ optimize
→ decide
→ implement/learn
```

This broader program must not be mistaken for a claim that one MSE thesis will make equal original contributions at every stage.

## Read order for future chats

1. [`00_CANONICAL_STATE.md`](00_CANONICAL_STATE.md)
2. [`01_SIX_CHAINS_CANONICAL_AND_EXPANDED.md`](01_SIX_CHAINS_CANONICAL_AND_EXPANDED.md)
3. [`02_MATHEMATICAL_MODEL_AND_OBJECTS.md`](02_MATHEMATICAL_MODEL_AND_OBJECTS.md)
4. [`03_HYPOTHESIS_PROPOSITION_CROSSWALK.md`](03_HYPOTHESIS_PROPOSITION_CROSSWALK.md)
5. [`04_TYPE_I_II_III_FRAMEWORKS.md`](04_TYPE_I_II_III_FRAMEWORKS.md)
6. [`05_LITERATURE_EVIDENCE_MAP.md`](05_LITERATURE_EVIDENCE_MAP.md)
7. [`06_MONTE_CARLO_AND_PRISMA_STATE.md`](06_MONTE_CARLO_AND_PRISMA_STATE.md)
8. [`07_REPOSITORY_IMPLEMENTATION_MAP.md`](07_REPOSITORY_IMPLEMENTATION_MAP.md)
9. [`08_CONVERSATION_MEMORY_INDEX.md`](08_CONVERSATION_MEMORY_INDEX.md)
10. [`09_USER_REQUESTS_VISIBLE_VERBATIM.md`](09_USER_REQUESTS_VISIBLE_VERBATIM.md)
11. [`10_ASSISTANT_OUTPUTS_RECONSTRUCTED.md`](10_ASSISTANT_OUTPUTS_RECONSTRUCTED.md)
12. [`11_DECISION_LOG.md`](11_DECISION_LOG.md)
13. [`12_OPEN_QUESTIONS_AND_NEXT_ACTIONS.md`](12_OPEN_QUESTIONS_AND_NEXT_ACTIONS.md)
14. [`13_AUTHENTICITY_PROVENANCE_RULES.md`](13_AUTHENTICITY_PROVENANCE_RULES.md)
15. [`14_CORRECTION_LOG.md`](14_CORRECTION_LOG.md)
16. [`15_USER_SUPPLIED_CHAIN_REFERENCE_VERBATIM.md`](15_USER_SUPPLIED_CHAIN_REFERENCE_VERBATIM.md)
17. [`16_ASSERTION_REGISTRY.csv`](16_ASSERTION_REGISTRY.csv)
18. [`17_CHAIN_LITERATURE_MATRIX.csv`](17_CHAIN_LITERATURE_MATRIX.csv)
19. [`PROJECT_MEMORY.json`](PROJECT_MEMORY.json)
20. [`manifest.json`](manifest.json)
21. [`validate_memory.py`](validate_memory.py)

## Future-chat authority hierarchy

Use the following order when resolving conflicts:

```text
1. authoritative source artifact / exact current repository file
2. verified transcript/source text
3. corrected v2 memory capsule
4. superseded v1 memory capsule
5. model memory / recollection
```

## Non-negotiable epistemic rule

Never convert:

- a literature ranking into proof of global novelty;
- a synthetic software test into empirical validation;
- a mathematical definition into an observed fact;
- a candidate mechanism into a measured causal effect;
- a reconstructed summary into a verbatim transcript;
- a downstream research possibility into a frozen MSE contribution.
