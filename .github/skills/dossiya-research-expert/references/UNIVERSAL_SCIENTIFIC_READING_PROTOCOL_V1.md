# Universal Scientific Reading, Reconstruction and Interpretation Protocol V1
**Effective:** 2026-10-09 | **Status:** ACTIVE SKILL GUIDANCE, subordinate to canonical science/evidence authorities
**Source inspiration:** user's five-paper critical-reading analysis, 2026-10-09; five uploaded articles. Not a claim that any of those papers validates this protocol.

## 0. Purpose and non-negotiable interpretation rule
Use for **any research paper** (empirical, theoretical, simulation/modeling, reviews, systematic reviews/meta-analysis, method/design, qualitative, mixed-methods, case study, AI/ML, normative/standards, protocols and perspectives). Adapt the audit to the paper's purpose; never demand randomized experimentation from pure mathematics or treat a review as original equipment measurement.

Separate **SOURCE STATEMENT [S]** (what authors reported), **RECONSTRUCTION [R]** (faithful re-expression), **INFERENCE [I]** (reader-derived implication), **HYPOTHESIS [H]** (unverified explanation), **VERIFIED CHECK [V]** (independent recalculation/source checking), **UNRESOLVED [U]**, **CONTRADICTION [X]** and **NOT APPLICABLE [NA]**. These are skill-local reading tags, NOT replacements for the repository's governing epistemic labels.

Do not promote [I] or [H] to [S] or [V]. **What the authors write != what the interpreter concludes != what evidence independently demonstrates.**
For externally sourced scientific claims, use adjacent verified APA 7 author–year citations and precise source locator (page, table, figure, equation, or supplementary item) in the analysis/evidence ledger. Never fabricate a page, DOI, equation or quotation.

## 1. Entry and source authenticity
1. Read current canonical repository authority and evidence/non-invention rules before making thesis claims.
2. Record DOI/URL, complete metadata, article version (preprint, accepted, version of record), publication date, correction/retraction/erratum status when verifiable, retrieval date, full-text access status, supplemental data/code availability, and any conflicts.
3. Disambiguate **PDF page vs printed page**, source text vs figure/scan. Check visible rendered pages when extraction loses subscripts, Greek symbols, superscripts, diagrams or table alignment. No unsupported OCR or reconstruction.
4. Classify text types (abstract, method, measured result, discussion, cited third-party claim, conjecture). Author's reported findings are evidence that *authors report* them, not automatic independently confirmed truth.
5. Declare access as ABSTRACT_ONLY, PARTIAL_TEXT, FULL_TEXT_CHECKED, or FULL_TEXT+SUPPLEMENT_CHECKED; scope conclusions accordingly.

## 2. Type-specific branches
| Type | Core extraction | Primary validity threat |
|---|---|---|
| Controlled empirical/experimental | question, sample/equipment, intervention/comparator, instrument, outcome, design, statistics, calibration, replication | confounding, leakage, bias, uncertainty |
| Observational/field | population, exposure, controls, selection, temporality, instruments, missingness, causal identification | association mistaken for causation |
| Simulation/computational engineering | physical boundaries, state/operator, governing equations, parameters, algorithm, discretization, verification, validation, QoI | code success mistaken for physical truth |
| AI/ML/optimization | target, objective/reward, features/state/actions, constraints, data split, hyperparameters, baselines, metrics, distribution shift | optimization of wrong proxy; train/test leakage |
| Pure mathematical/theoretical | axioms/definitions, hypotheses, theorem/proof, logical dependency, existence/uniqueness, counterexamples, scope | proof gap, hidden assumption, false generalization |
| Systematic review/meta-analysis | preregistration, database/search/date, duplicates, selection, risk of bias, heterogeneity, effect combination, publication bias | selective inclusion, inappropriate pooling |
| Narrative/scoping review | search coverage, thematic synthesis, claims traced to original studies, disagreements, omissions | secondary-source authority laundering |
| Qualitative/interpretive | sampling, researcher position, coding, triangulation, counterexamples, saturation/credibility, transfer limits | unsupported generalization |
| Framework/design/DEMATEL/MCDM | construct definitions, source selection, scoring, normalizing, mathematical assumptions, expert selection, agreement, sensitivity | perceived influence misread as physical causality |
| Standard/guideline/regulation | issuing body, edition, jurisdiction, enforceability, exact clause, conditions, supersession | expired code applied as universal requirement |
| Commentary/editorial/protocol | argument, proposed work, forecasts, assumptions, provenance | proposal represented as completed result |

For hybrid papers, run every applicable branch. If a method is only described, label **PROPOSED**, not EXECUTED or VALIDATED.

## 3. Evidence extraction: five-pass reading cycle
**Pass A — Problem and contribution:** Precisely transcribe/paraphrase the research question, declared gap, objective, paper type, system/context, stated novelty; contrast claimed vs demonstrated contribution.
**Pass B — System and method:** Map actual components, boundary, inputs, functions, state, control, outcomes, equations, parameter/data origin, measured or simulated context, comparison and uncertainty.
**Pass C — Figure/table/equation audit:** Visit key figures and table notes. Reconstruct at least critical equations with all variables/units/constraints and mathematical preconditions. Recalculate selected claims if feasible. Check nondimensionalization, matrix inverse/spectral radius, loss sign, energy-vs-power, percentages and confidence intervals. Do NOT silently repair published equations; record proposed correction as [I] and request evidence.
**Pass D — Claim stress test:** Distinguish comparison vs causal identification, shared forcing vs directed interaction, modeled vs measured, validity in-sample vs holdout, correlation vs experimentally justified mechanism. Form plausible rival explanations and discriminating evidence. Inspect failure modes, null findings, sensitivity, negative controls and alternative parameterizations.
**Pass E — Synthesis and transfer:** State paper-supported findings, author's stated limitations, reviewer-derived limitations separately, what thesis would require before transfer, nearest overlap/novelty challenge, and proposed follow-up tests.

Run these passes iteratively, revisiting earlier passages as a mismatch appears. The final interpretation must preserve contradictions and uncertainty rather than smoothing them away.

## 4. Mechanistic interpretation contract
For any asserted relationship, create a directed mechanism record:
- Source component and **measured** source quantity
- Carrier/transfer across explicitly defined boundary and units
- Receiver component, state and governing physical transformation
- Conditions, limits, constitutive law and evidentiary source
- Expected observable/time-scale/lag and quantitative prediction where justified
- Common causes, controls, counterfactual, alternative explanations
- Whether asserted relationship is topology, statistical association, expert scoring, information/control, physical flux, or *verified causal response*
- Status (CANDIDATE / CONDITIONAL / QUALIFIED / REJECTED / OPEN)

**Thesis-specific guardrails**: Power P and full Electrified Transportation T_e remain separate; EVSE belongs to T_e; thermal extreme-heat scope only. Shared ambient heating is not cross-system coupling; T_e→P requires AC-grid-side power/current to electrical loss and thermal state evidence; P→T_e requires real transformer-state-to-permitted-supply operating rule. State != capability != delivered service. M0 independent, M1 algebraic, M2 independently qualified causal dynamic coupling. Evidence source can be historical but must not be falsely called validation of current case.

## 5. Mathematical reconstruction minimum
For each load-bearing equation record:
`equation_id`, source page/equation, literal symbolic transcription (where accessible), physical/math meaning, variables+units, domain, stated assumptions, boundary+initial conditions, type (identity/evolution/empirical fit/optimization constraint/objective/statistic/heuristic), derivation/proof status, admissibility, and test.
- Distinguish **dimensionally incorrect**, **not well-defined**, **ambiguous signs**, **missing controls**, and **different conventions**.
- For discrete-time integrals, inspect time-unit conversion and variable semantics.
- For matrix geometric series `B(I-B)^(-1)`, evaluate conditions including spectral radius `rho(B)<1`; invertibility alone need not guarantee series convergence.
- For reinforcement-learning decision state, never automatically infer physical temperature state.
- For stochastic modeling, inspect tail behavior and distributional assumptions; synthetic samples are not independent field measurements.
- For standards, only use the applicable edition and device jurisdiction.
Mathematical objections must cite source and show the exact reasoning or counterexample; preserve provisional status until independently reproduced.

## 6. Human-scientist check (observable protocol, not claim about hidden cognition)
For each major interpretation, write:
(a) What did I **observe in the document**? 
(b) What is my **paraphrase**?
(c) What extra principles do I invoke?
(d) Exactly what inference follows, and which assumptions?
(e) How could a competent researcher falsify or modify this?
(f) What apparatus, code, raw data, expert consultation or alternate evidence could decide?
(g) What remains unknown?
A human may bring first-hand measurement, apparatus knowledge and situated judgment; these are *possible additional evidence channels*, not proof that an interpretation is right. AI cannot claim firsthand empirical observation.

## 7. Cross-paper synthesis; no homogenization
Maintain per-paper evidence status and traceable conflicts. Compare only after aligning:
- Populations/equipment and context of use
- Quantities, energy/power and physical boundaries
- Time horizon, spatial scale, units
- Equations, experiment and uncertainty
- Baselines, metrics, human decision/objective
- Empirical status vs normative proposal
- Meaning of terms such as state, resilience, efficiency, causal, validation
A discrepancy can reflect differing assumptions, scale or metric, not author error. Do not merge a decision-optimization state with a thermal state, DEMATEL influence with physical causality, or simulation with validation.

## 8. Required deliverable (adapt depth to task)
1. Full citation and paper classification / access status
2. Authors' problem, question, claimed contribution
3. What I directly read (precise source location)
4. Method + evidence reconstructed, including critical equation/figure/table
5. Results: measured vs simulated vs interpreted
6. What I infer, with visible inferential link and assumptions
7. At least one serious alternative/rival and discriminating test when causal claim is relevant
8. Strengths, limitations (author-stated vs inferred), confidence/claim ceiling
9. What transfers to the thesis, what cannot, and next verification gate
10. Source excerpt/evidence ledger and verdict; cite every substantive externally grounded claim.

**Scale:** Quick reading for triage; focused audit for one claim; full-text mechanistic audit for core studies; multi-study comparison for gap/novelty. Never call quick review 'full-text audited'.

## 9. Pass/fail audit checklist (not a synthetic score for scientific truth)
PASS requires authentic source metadata, checked available full text to claimed depth, bounded text evidence, transparent source-versus-inference separation, mathematical correctness checked where relevant, evidence-matched conclusions, and explicit limitations. Mark NOT_APPLICABLE where warranted. BLOCK if load-bearing equation/claim cannot be read, no independent evidence for asserted physical causality, or citation unsupported. Reviewer disagreement is documented with a specific source locator and test.

## 10. Illustrative training cases (source descriptions, not transferable laws)
- Oladigbolu et al. (2025), DOI 10.1016/j.est.2025.118419: coupled-system review maps operations; does not independently validate the thesis's transformer/charger electrothermal law.
- Tamay & Inga (2022), DOI 10.3390/su14148248: infrastructure design and protection simulation; fault-clearing study != heat-wave thermal derating.
- Li et al. (2024), DOI 10.3390/en17215442: PPO decision state and reward; paper's grid-energy sign and Gaussian weather assumptions warrant source/code audit, not premature accusation.
- Shin et al. (2022), DOI 10.1007/s11251-022-09590-9: iterative five-practice ST/CT modeling framework; education framework != engineering mechanism experiment.
- Ayoobi et al. (2024), DOI 10.1007/s44268-024-00042-6: DEMATEL expert influence scores and matrix series; perceived influence != demonstrated physical causation, convergence matters.

## 11. Reuse and provenance
Do not copy long copyrighted passages. Record brief source locator and concise paraphrase; link verified primary record. Attribute interpretation to analyst; always distinguish what came from the source, canonical repository doctrine and independent engineering reasoning. This skill does not supersede `project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md` or `thesis/00_governance/THESIS_CITATION_AND_REFERENCE_STANDARD_V1.md`.


## 12. Automatic equation extraction companion — 2026-10-10
When asked to extract or explain mathematical equations, apply `AUTOMATIC_EQUATION_EXTRACTION_AND_RESPONSE_LEVELS_V1.md` (this directory). Preserve per-equation transcription tier EX0–EX4 and separate automatic response depth AR0–AR3. Earlier examples from a chat are *candidate transcriptions* until actual source pages are independently checked. This companion augments the source/reader/inference distinction above; it does not relax any authority or requirement to record page/number/units and VVUQ. Scientific formula accuracy and usability are evaluated independently of response verbosity.
