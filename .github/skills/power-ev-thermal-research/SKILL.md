---
name: power-ev-thermal-research
description: Execute evidence-grounded electrical-and-thermal interdependency research for the active Power System–Electrified Transportation thesis, from source acquisition through physics-based derivation, VVUQ and resilience consequences. Activate when auditing KIT/OPSD/SINTEF/EPFL/KU Leuven/EVSE/bus-depot field data, connected topology, model calibration, or state-time thermal coupling.
---

# Power–Electrified Transportation Thermal Research — Orchestrator V1

**Scope:** The frozen thesis title is *Engineering of Power–Electrified Transportation Interdependencies for Resilience* (canonical title V3, dated 2026-10-15). The **active** scientific scope is extreme-heat-conditioned **thermal interdependencies** of the distinct Power System **P** and Electrified Transportation System **T_e**, and their consequences **through physical state and time**. This is NOT a generic power–transportation, power–water, cyber, I/O, flood, or full transportation-network thesis. The canonical *full* T_e contains vehicles/RESS/propulsion/auxiliaries, the vehicle supply circuit, EVSE, charging connection, and required charging communications/control; a chosen charging case is only a bounded application.

## Mandatory first reads and precedence

1. Read `AI_RESEARCH_INSTRUCTIONS.md`, `project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md`, `project/CANONICAL_THESIS_TITLE_V3.md`, `project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md` and `project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md` from the current repository.
2. Read `project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md`, `project/CANONICAL_STATE_TIME_DEFINITIONS_V1.md`, `project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md`, `project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md`, `project/CANONICAL_RESILIENCE_DEFINITION_V1.md`, `project/CANONICAL_SUSTAINABILITY_TWO_PATHWAY_ASSESSMENT_V1.md`, `project/RESEARCH_DECISION_AND_FREEZE_PROTOCOL_V1.md`, and `thesis/00_governance/THESIS_CITATION_AND_REFERENCE_STANDARD_V1.md` §0A.
3. Read `project/DOSSIYA_REALITY_FIRST_40_TO_8_COMPONENT_SELECTION_PROTOCOL_V1.md` when selecting physical components/ports. Consult active authority index for other current binding files. ASU/institutional authority and supervisor-approved decisions outrank this skill. This skill **does not amend frozen content**.
4. Read `references/authority-and-evidence-status.md`, `references/evidence-gates.md`, and `references/csv-data-contracts.md` in this skill bundle when starting a workflow. If sources are unavailable, record `BLOCKED_EXTERNAL_ACCESS`; do not claim to have read them.

## Operating principle

**Reality → physical connection → measured mechanism → admissible equations → numerical verification → independent validation → service-level resilience claim.**

Use `LEARN → VERIFY → FORMULATE → DERIVE → TEST → VALIDATE → SYNTHESIZE → ADVANCE`. Advance autonomously through independently admissible stages; record blocked prerequisites rather than substituting guesses. No claim of asynchronous work unless an actual runner/automation is scheduled.

## Eight collaborating skills (activate as needed)

| Code | Module (path under `.github/skills/`) | Primary deliverable |
|---|---|---|
| S1 | `thesis-scientific-data-acquisition/SKILL.md` | original-source registry, checksums, license, acquisition log |
| S2 | `thesis-electrical-topology/SKILL.md` | verified asset-level one-line topology, electrical interface map |
| S3 | `thesis-python-data-engineering/SKILL.md` | quality-audited, unit- and time-normalized **but unmerged** measured data |
| S4 | `thesis-thermal-physics/SKILL.md` | heat balances, component-specific thermal model candidates, physical validity |
| S5 | `thesis-mathematical-modeling/SKILL.md` | traceable state-space equations, directional coupling, constraints and limiting cases |
| S6 | `thesis-system-identification/SKILL.md` | parameter provenance, diagnostics and uncertainty, conditional predictions |
| S7 | `thesis-vvuq-experimental-design/SKILL.md` | independent tests, competing baselines, leakage checks and uncertainty analysis |
| S8 | `thesis-resilience-engineering/SKILL.md` | service consequences, thresholds, propagation and bounded resilience indicators |

## Research execution and gates

1. **S1 Acquire & register** original measurement objects; verify publisher DOI, raw URLs, license, equipment, unit/time definitions, original SHA-256, raw-versus-calculated status. Save immutable originals; search results are candidates not data.
2. **S2 Verify physical network** feeder/transformer/EVSE/vehicle identities and exact circuit edges from single-line diagrams and operator metadata. Document AC grid boundary/connector boundary; grid import measured at a building does not identify the transformer supplying it.
3. **S3 Qualify measurements** as raw observed / aggregated observed / interpolated / calculated / synthetic; resolve UTC/timezone, sampling, units, sign conventions, missing intervals, sensor location and meter semantics. Do NOT join unrelated installations on timestamps; preserve original raw and transformation code.
4. **S4 Derive minimum-sufficient physics** for accepted transformers, charger cooling/derating, battery thermal response. Distinguish ambient *forcing*, actual thermal *state*, *capability* and delivered *service*. Source all constitutive laws and operating limits; do not infer manufacturer derating from an arbitrary threshold.
5. **S5 Formulate conditional candidates**: `x_dot_P = f_P(x_P,z_PT,T_a,u_P;theta_P)`; `x_dot_Te = f_Te(x_Te,z_PT,T_a,u_T;theta_Te)`. Treat these as structural placeholders **not admitted constitutive equations**; define units, states, algebraic interface/port, causality, direction, event timing and tested coupling removal. Label new derivations `T1`.
6. **S6 Identify** model parameters only with observational support and fit/holdout separation; test structural and practical identifiability, parameter boundary hits, confounding, sensor placement, current sign and unmeasured cooling. Model fitting does not by itself qualify physics.
7. **S7 VVUQ**: verify dimensions, conservation, numerical convergence, limiting cases; perform group/time/site-held-out testing versus persistence and uncoupled/ablated alternatives; report errors, intervals, calibration, uncertainty propagation and domain shift. Do not turn conditional hindcasts using *future measured inputs* into prospective forecasts.
8. **S8 Quantify consequences** only after service needs/thresholds/operator evidence are defined. Separate state→capability→electricity/mobility service→resilience over horizon. Two sustainability pathways only if bounded verified indicators and functional units are available; SDG linkage only with justified target/indicator definitions.

## Required evidence decisions for each direction

- `P→T_e`: prove a **thermally conditioned** Power-side state/capability/restriction changes feasible charging and a measured or explicitly modeled T_e/service consequence. Connection or charging power alone does not establish thermal P→T_e.
- `T_e→P`: prove T_e charging/thermal behavior changes Power-side loading/heat/limits **with identifiable feeder/transformer linkage**, or explicitly label as a hypothetical modeled direction.
- For either direction, require site/circuit ID, synchronization and measurement-boundary semantics before using the words **coupled field validation**. A conceptual bidirectional arrow proves neither direction.


## ECE6378 / RPG Lab learning overlay — validated 2026-11-02

**Activation rule:** When selecting an ML method, adapting power-flow code, processing grid/EV measurements, training a prediction model, or claiming ML-assisted optimization, read `references/ECE6378_VERIFIED_LEARNING_MAP.md`, `references/RPGLAB_CODE_TRANSFER_PROTOCOL.md`, and `references/PHYSICS_CONSTRAINED_ML_VVUQ.md`. Also activate `.github/skills/thesis-physics-constrained-ml/SKILL.md` as a *cross-cutting support module*, not a ninth frozen thesis objective or substitute for S1–S8.

**Source boundary:** ECE6378 is a *2026 Fall in-progress course* (Xingpeng Li, University of Houston; page dated Oct. 29, 2026). Its page lists 27 lectures, but Lectures 19–27 are **tentative**; full editable slides, notebooks and assignments are **planned after the semester**, not currently verified as released. A course outline is NOT proof of contents of inaccessible slides or assignments. All external-method transfer must cite the original resource and check applicable license. The course teaches power-system/ML methods; it does **not** itself qualify transformer/EVSE heat-transfer physics, equipment derating, directional thermal causality, field synchronization or coupled-system resilience.

**Learning-to-research translation:** Follow the complete 27-lecture table in `references/ECE6378_LEARNING_MATRIX.csv`, not just the highest-priority topics. First master meter semantics/time-aware preprocessing, evidenced physical topology, AC/DC/DistFlow assumptions, and leakage-resistant model evaluation (L2–8, L10–11, L14); then learn interpretable models and DNN optimization (L9, L12–13, L16–18); explore graph/time-series learning and ML-accelerated or embedded optimization only when network data and constraint prerequisites are met (tentative L19–27). Treat short-circuit/fault and frequency regulation as supporting context, not new standalone thesis goals.

**Evidence-based model comparator contract:** Pre-register equal-horizon and equal-input-comparability `M0` (source-admitted physics), `M1` (nonphysical statistical baseline), `M2` (physics + controlled residual candidate). Report data leakage, conditioning on observed *future* exogenous signals, out-of-domain exposure, physical residuals, solver feasibility, and computational cost. Never say `M2` is better based only on a lower MAE on the training/selection set; never interpret a relaxed constraint penalty as exact physical feasibility. Run `tools/check_ml_experiments.py --root <results-directory>` against nonempty filled ML experiment registers *in addition* to the existing G0–G8 checks. A syntax/schema PASS is not a physics, causal, or field-validation PASS.

**RPG Lab open-source transfer:** The distribution EV/DDCP notebooks are network *planning and electrical constraint* examples, not measured thermal-state field data. GNN-reduced OPF predicts constraint relevance, not a physical topology. Feasibility-layer SCUC is generation scheduling methodology, not validated charging derating. Compare all adapted algorithms against the simpler physics/network formulation under the same data, test conditions and solver tolerances. Do not assume benchmark-network parameters apply to KIT, OPSD or a field transformer.

## Non-negotiable stop / block rules

- `G0–G8` in `references/evidence-gates.md` govern admission. If no synchronized same-site connected transformer/EVSE thermal measurements exist: set `G7=BLOCKED_EVIDENCE`; **never** label a coupled thermal model `FIELD_VALIDATED`.
- A failed battery predictive baseline or parameters fixed at optimization bounds: block physical identification / predictive qualification, even with small MAE.
- SINTEF Norwegian ambient measurements are not field validation at extreme heat without demonstrated transfer validity; EPFL charging power is not verified feeder power; OPSD co-premises EV/grid meters are not verified transformer-level thermal measurements.
- Never fabricate measurements, citations, DOIs, standard clauses, parameters, uncertainty bands, heat limits, causal directions, novelty or validation performance. Keep `A1–A5 / T1 / OPEN` source classes.
- Research dataset tiers: `METADATA_ONLY`, `MEASURED_UNCOUPLED`, `MEASURED_SAME_PREMISES_ELECTRICAL`, `MEASURED_CONNECTED_ELECTRICAL`, `MEASURED_CONNECTED_THERMAL`, `SYNTHETIC`, `UNKNOWN`. Upgrade only with recorded evidence, not terminology.
- Respect research-ethics access/consent, publisher licenses, API terms, site rate limits, institutional restrictions; never bypass access controls. Never push proprietary/bulk raw data or credentials to GitHub.

## Outputs and scientific release contract

Create under a dated, noncanonical `results/YYYY-MM-DD_<run-id>/` (unless the user provides another directory):
- `source_registry.csv` — original files and SHA-256, source identity, licensing and access; register missing values as blank/OPEN.
- `asset_topology.csv` — only evidenced physical connections; missing diagram → OPEN edge.
- `observations.csv` — long-form observed measurements **with source/site/asset/time/channel/units/origin flags**; no false cross-site alignment.
- `thermal_interface_evidence.csv` — directional mechanism, evidence, field status and blockers.
- `equation_register.csv` and `parameter_register.csv` — admission, dimensional check, provenance, ranges and validation domain.
- `validation_register.csv` — exact train/val/test split, baselines, errors, intervals, horizon, leakage risks and claims.
- `execution_ledger.csv` plus concise `README.md` — PASS/FAIL/BLOCKED, exact command, code revision, dataset hashes, what remains OPEN.

Use header templates under `templates/`; call `python .github/skills/power-ev-thermal-research/tools/check_evidence.py --root results/<run>` before promoting any claim. A checker PASS confirms register logic, **not** scientific or coupled-field validation.

## Immediate case study queue (no fabricated completion)

1. KIT campus multilevel synchronized electrical measurements: obtain **one-line topology**, asset mapping, exact EV supply path, raw channel list; establish whether heat measurements exist.
2. Bus-depot 2,000-kVA transformer study: raw simultaneous primary/secondary/harmonic observations, actual temperature channels and provenance; thermal loss inferred from harmonics ≠ measured winding temperature.
3. Qatar hot-climate charger study: request timestamped charger internal temperatures, inlet ambient, cooling/derating actions, P input/output and upstream transformer identifiers. Request-only data stay `BLOCKED_EXTERNAL_ACCESS`.
4. OPSD co-premises 15-min EV/grid data: retain cumulative-vs-interval meter semantics, timezone, source-imputation flags, and verified EV/grid calculations; no transformer thermal attribution.
5. SINTEF, KU Leuven, EPFL: independently audit component model and meter boundaries; preserve prior failed/provisional gates, not upgrade via integration.

**Definition of done:** A final scientific claim is published only with a traceable raw source, physical mechanism, equation/parameter provenance, executed verification, appropriate independent validation, uncertainty and explicitly bounded applicability. Otherwise release a reproducible, accurately labeled partial result and a blocker record.
