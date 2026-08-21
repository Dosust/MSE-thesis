# Research Memory — Six Interacting Scientific Chains

**Repository:** `Dossiya-SE/MSE-thesis`  
**Module:** `2026-08-21_six_chain_mathematical_physics_review`  
**Snapshot time:** `2026-08-21T20:01:00+08:00`  
**Purpose:** rigorous recall, provenance, reproducibility, and future-chat continuity for the literature-grounded mathematical/physical ontology of sustainable and resilient infrastructure systems.

## Scientific status

The six-chain architecture is a **thesis/review synthesis**. No claim is made that one prior paper proposed the complete six-chain framework. Individual layers, mathematical methods, equations, and conceptual distinctions are anchored in the literature.

## Core architecture

1. **Physical System** — Physics → Structure → Interfaces → Dynamics, expanded to physical laws → components → topology → interfaces/interdependencies → states/flows → dynamics → cascades.
2. **Observation & Inference** — measurement → observability → identification → calibration → state estimation → data assimilation → uncertainty quantification → prediction.
3. **Stress & Consequence** — hazard → exposure → vulnerability → fragility → damage/failure → cascade → functional loss → service loss → societal consequences → risk/criticality.
4. **Viability & Response** — preparedness → absorption → robustness → viability → reachability → service continuity → recoverability → restoration → resource allocation → adaptive control → new state.
5. **Engineering Lifecycle** — requirements → design → deployment → commissioning → operation → monitoring → aging → maintenance → repair/replacement → retrofit/expansion → planning → adaptation → transformation → decommissioning/circularity.
6. **Societal Decision Cycle** — evaluate → sustainability/equity/economics/governance → trade off → decide → implement → observe outcomes → learn/update.

## Cross-cutting mathematical engines

ODE/PDE/DAE; dynamical systems; network science; probability; statistics; Bayesian inference; inverse problems; uncertainty quantification; optimization; control; viability/reachability; game theory; numerical analysis; AI/ML; decision theory; MCDA; robust decision making.

## Critical distinctions frozen in this snapshot

- topology ≠ interdependency ≠ interface mechanism
- physical damage ≠ component functionality ≠ delivered service ≠ societal consequence
- resilience ≠ sustainability
- recovery/restoration is explicit and not buried inside “resilience”
- optimization is a cross-cutting method, not a lifecycle stage
- societal evaluation is normative/institutional, not another physical stage
- the architecture is six **interacting** chains, not one giant causal arrow

## Start here in a future chat

Read these in order:

1. `FUTURE_CHAT_BOOTSTRAP.md`
2. `SCIENTIFIC_STATE.json`
3. `FROZEN_DISTINCTIONS.md`
4. `CHAIN_LAYER_MATRIX.csv`
5. `MEMORY_MASTER.md`

## Full folder navigation

- `MEMORY_MASTER.md` — consolidated human-readable research memory.
- `USER_REQUESTS_VERBATIM.md` — exact visible user requests from this subthread.
- `ASSISTANT_OUTPUT_INDEX_RECONSTRUCTED.md` — explicit reconstructed assistant-output history.
- `SIX_CHAIN_ONTOLOGY.md` — canonical chain/layer architecture.
- `FORMULA_CATALOGUE.md` — representative equations and mathematical structures.
- `FROZEN_DISTINCTIONS.md` — scientific corrections that should not regress.
- `REVIEW_PAPER_CONCEPT.md` — proposed paper, objectives, sections and extraction schema.
- `ANCHOR_REFERENCES.md` — DOI-level literature anchors.
- `anchors.bib` — machine-readable seed bibliography.
- `CHAIN_LAYER_MATRIX.csv` — machine-readable ontology for systematic-review coding.
- `SCIENTIFIC_STATE.json` — compact machine-readable frozen state.
- `PROVENANCE.md` — authenticity, copyright and citation rules.
- `FUTURE_CHAT_BOOTSTRAP.md` — handoff instructions for future conversations.
- `DRAWIO_REGENERATION.py` — deterministic editable Draw.io generator driven by `CHAIN_LAYER_MATRIX.csv`.
- `VALIDATION.md` — QA result for Draw.io regeneration and XML parsing.
- `MANIFEST.md` — semantic inventory of the preserved research memory.

## Reproduction

From this folder:

```bash
python DRAWIO_REGENERATION.py
```

This regenerates an editable `Six_Chain_Ontology_Regenerated.drawio`. The regeneration workflow was validated successfully; see `VALIDATION.md`.

## Provenance rule

Do not infer that a citation beside a generic equation means the paper printed that exact equation. Unless exact equation provenance has been verified, the citation anchors the **scientific layer/method family**. The complete six-chain architecture remains an integrated synthesis to be tested and refined through the formal literature review.
