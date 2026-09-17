# Seven-question consolidation — 2026-09-17

**Authorization:** user requested that all active question architecture use the seven Chapter-I questions.

**Change type:** WORDING AND TRACEABILITY UPDATE.

**Authority:** `CANONICAL_RQ_SO_HYPOTHESES_V3.md`; Chapter-I flow remains controlled by `CANONICAL_CHAPTER_I_CONTENT_AND_FLOW_V1.md`.

| RQ / SO | Stage | Research question | Specific objective | Test / evidence obligation |
|---|---:|---|---|---|
| RQ1 / SO1 | 1 | What entities exist, what layers constitute the system, and where can interactions occur? | Define the coupled Power–Transportation system boundary, entities, layers, locations, interfaces, states and service requirements, with Information and Organization as supporting domains. | Developmental verification; supports H1 |
| RQ2 / SO2 | 2 | Why and through which mechanisms do components and layers affect each other? | Establish evidence-supported directional causal mechanisms, activation conditions, parameters, uncertainties and validity boundaries linking components and layers. | Mechanism/evidence qualification; supports H1 |
| RQ3 / SO3 | 3 | How, when, and where do accepted interdependency mechanisms evolve and propagate through the coupled system? | Develop and verify a physics-based hybrid multiscale dynamic model and test its incremental explanatory or predictive value against independent and static-coupling representations. | H1 |
| RQ4 / SO4 | 4 | How is the system observed, interpreted, coordinated and controlled? | Evaluate how observation, state estimation, information availability, organizational constraints and feasible control affect response timing, service trajectories and recovery. | H2 |
| RQ5 / SO5 | 5 | Under what conditions can critical coupled services remain acceptable or recover under feasible controls and uncertainty, and what additional engineering information do viability and reachability provide? | Determine uncertainty-aware service viability and recovery reachability, evaluate incremental value beyond conventional performance/recovery curves, and characterize interface criticality as a supporting diagnostic. | H3; separately qualified interface diagnostic |
| RQ6 / SO6 | 6 | What sustainability requirements follow from resilience diagnosis and from the effectiveness, resource efficiency, and sustainability consequences of candidate interventions? | Derive evidence-qualified sustainability requirements from resilience diagnosis and intervention consequences, distinguishing effectiveness, resource efficiency, accessibility, energy, carbon and cost within declared accounting boundaries. | H4; requirements derivation |
| RQ7 / SO7 | 7 | What should be changed, where, when and in what sequence to achieve effective, efficient and sustainable infrastructure transformation under feasibility constraints and uncertainty? | Evaluate candidate infrastructure transformations and, where justified, intervention sequences using effectiveness, efficiency, sustainability, feasibility and uncertainty to support engineering decisions. | H5; H4 intervention-performance inputs |

## Preserved scientific contract

RQ0 remains verbatim from v2. The Chapter-I general objective is retained verbatim. RQ1–RQ4 preserve existing stage-question wording; RQ5–RQ7 consolidate the current Chapter-I meanings with framework v2 and intervention amendment v2.1. H1–H5 claims, comparator identifiers and evidence citations are retained. No H6/H7, result, threshold, model, solver or empirical validation is introduced.

## Historical records

The former v2 canonical specification and two former governance matrices are preserved exactly under `research_archive/rq_so_v2_before_seven_question_consolidation/`. Immutable dated scientific checkpoints and dated audit/closure records retain their original numbering as historical evidence; current entry points route to v3. Git history preserves previous versions of updated active documents.

## Remaining scientific work

The migration closes question-numbering and mapping inconsistencies. It does not close empirical data qualification, H3 computation/threshold gates, or the v2.1 H4/H5 numerical preregistration obligations.

## Verification

- Seven numbered RQs and seven corresponding SOs: PASS.
- RQ0 and all five H1–H5 claim statements preserved: PASS.
- Existing canonical reference list retained: PASS (sources not independently reverified in this wording migration).
- All changed active Markdown files pass the repository Markdown/ontology checks.
- Relative Markdown links in changed active documents resolve against the repository tree: PASS.
- Active old five-question ranges and old direct RQ2/H2, RQ3/H3, RQ4/H4, RQ5/H5 mappings: absent outside explicitly superseded/historical records.
- Full available-worktree lint also reports pre-existing errors in unchanged files and a schema absent from the partial local checkout. No full-repository clean-lint claim is made.

This update changes 54 repository files, including three exact historical snapshots and the machine-readable question mapping. Scientific execution status is not advanced.
