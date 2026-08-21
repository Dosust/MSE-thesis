# Future Chat Bootstrap — Corrected v2

Use this file when a new chat must continue the thesis without reconstructing the project from memory.

## Step 1 — Read the canonical v2 state

Read, in order:

1. `project_memory/2026-08-21_chain_architecture_v2/00_CANONICAL_STATE.md`
2. `project_memory/2026-08-21_chain_architecture_v2/01_SIX_CHAINS_CANONICAL_AND_EXPANDED.md`
3. `project_memory/2026-08-21_chain_architecture_v2/02_MATHEMATICAL_MODEL_AND_OBJECTS.md`
4. `project_memory/2026-08-21_chain_architecture_v2/03_HYPOTHESIS_PROPOSITION_CROSSWALK.md`
5. `project_memory/2026-08-21_chain_architecture_v2/06_MONTE_CARLO_AND_PRISMA_STATE.md`
6. `project_memory/2026-08-21_chain_architecture_v2/11_DECISION_LOG.md`
7. `project_memory/2026-08-21_chain_architecture_v2/12_OPEN_QUESTIONS_AND_NEXT_ACTIONS.md`
8. `project_memory/2026-08-21_chain_architecture_v2/13_AUTHENTICITY_PROVENANCE_RULES.md`
9. `project_memory/2026-08-21_chain_architecture_v2/14_CORRECTION_LOG.md`
10. `project_memory/2026-08-21_chain_architecture_v2/PROJECT_MEMORY.json`

## Step 2 — Reopen authoritative files relevant to the requested task

At minimum consider:

- `project/THESIS_SCOPE.md`
- `project/MATHEMATICAL_FOUNDATION.md`
- `project/SCIENTIFIC_PROPOSITIONS.md`
- `config/scientific_propositions.yaml`
- `prompts/PRISMA_Monte_Carlo_325_Single_Dataset_Master_Prompt.md`
- `methods/monte_carlo/final_run_2026-08-20/README.md`
- `provenance/ONLINE_ARCHIVE.md`
- `conversation/AUTHENTICITY_LIMITS.md`

Do not use memory as a replacement for the source when precision matters.

## Step 3 — State the recovered project state before major work

A future chat should be able to state:

```text
Working thesis:
Mathematical Physics of Sustainable Infrastructure Resilience

Precise formulation:
Equity-Constrained Viability of Coupled Power–Water–Transportation–Solid-Waste Systems with Dynamic Interfaces under Climate Stress

System:
P-W/Drainage-T-SW

Demonstrator:
urban flooding with waste–drainage–transport feedbacks

Core MSE contribution:
dynamic coupling → admissibility → viability → recovery

Upstream support:
interface identification / inverse problems / UQ

Downstream extensions:
control / design / optimization / decision

Central object:
∂V_R
```

## Step 4 — Preserve the six-chain ontology

Compact chains:

```text
I   Physics → Structure → Interfaces → Dynamics
II  Observe → Identify → Estimate → Predict
III Hazard → Failure → Service Loss → Consequences
IV  Admissibility → Viability → Resilience → Recovery → Control
V   Design → Operate → Maintain → Restore → Plan → Adapt
VI  Evaluate → Trade off → Decide → Implement → Learn
```

Use the expanded v2 decomposition when deeper layers are needed.

## Step 5 — Preserve proposition naming correctly

Current formal thesis propositions:

```text
P1-P7
```

Historical closed-corpus/literature targets:

```text
H1-H7/T1
```

Earlier project hypothesis H0 also exists.

Do not silently merge the IDs. Use the crosswalk file.

## Step 6 — Preserve Monte Carlo scope correctly

Frozen logical dataset:

`Thesis_Final_Unique_Papers_325_2026-08-20(1).csv`

SHA-256:

`047e80b7348190a9da8100758c5f1201cd39059f9318e6298dcda614ecb7813f`

A `(4)` copy used by the archived high-rigor run has the same hash.

Interpret all rankings **within the locked corpus**.

The later comparison treated:

```text
FULL_RUN_RESULTS = closest controlling frozen-formula implementation
HIGH_RIGOR_RUN   = sensitivity replication
EXECUTED         = alternative-model stress test
```

Do not average raw scores across these incompatible models.

## Step 7 — Route any new task into the chain ontology

Before solving a new research question, identify:

1. which chain(s) it belongs to;
2. which mathematical object is being defined/estimated/computed;
3. what literature already establishes;
4. what is a proposed thesis contribution;
5. what evidence/test could falsify it;
6. whether the result is definition, theorem, numerical QA, corpus-derived result or empirical validation.

## Step 8 — Current recommended next task

Unless the user redirects the work:

> Deeply decompose Chain I sector-by-sector — Power, Water/Drainage, Transportation, Solid Waste — before freezing the coupled forward model.

For each sector, recover governing equations, assumptions, states, units, controls, failure modes, timescales, literature precedents, well-posedness conditions and unresolved mathematical questions.

## Canonical continuation prompt

> Continue the MSE thesis using `project_memory/2026-08-21_chain_architecture_v2/` as the corrected recall layer and the linked repository artifacts as scientific authority. Preserve the P–W/Drainage–T–SW sector set, urban flooding with waste–drainage–transport feedbacks, the distinction `xi → eta`, the dynamic interface state `Z`, the sustainable/equitable admissible set `K_R`, viability kernel `V_R`, recovery/capture set `C_R`, and central boundary `∂V_R`. Keep P1–P7 separate from historical H0–H7/T1 labels. Treat the core MSE contribution as dynamic coupling → admissibility → viability → recovery, with identification/UQ upstream and control/design downstream. Do not infer global novelty from the locked 325-record ranking. Distinguish source evidence, definitions, hypotheses, synthetic QA, corpus-derived results, and empirical validation. Before new model development, state which chain/layer the work belongs to and what existing literature already establishes.
