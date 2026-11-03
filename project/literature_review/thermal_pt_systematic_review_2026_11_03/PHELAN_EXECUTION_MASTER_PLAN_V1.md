# Professor Phelan request — executable scientific research plan (V1)

**Date:** 2026-11-03  
**Status:** EXECUTION PLAN, NOT A COMPLETED SYSTEMATIC REVIEW / VALIDATED PINN / SUPERVISOR APPROVAL.  
**Branch:** `user-data-qualification-2026-11-03` — does not change canonical/frozen thesis scope.  
**Thesis:** *Physics-Based Mathematical Engineering of Power–Electrified Transportation Interdependencies for Resilience.*

## 0. Direct supervisor requirements

**Request P1 — Literature:** Answer, with a thorough reproducible review, *what other people have done* on this specific problem, exactly what was physically measured, mathematically represented, experimentally validated and not yet established.  
**Request P2 — Model choice:** Seek appropriate **experimental data** for a physics-informed neural network / physics-informed ML; if suitable observations do not exist, proceed with a **pure physics model**, with an evidence-based, explicit comparison and stopping criterion. Model selection must not be driven by novelty branding.

## 1. Goal, scope and measurable objectives

**Research goal:** Produce an auditable, primary-source evidence base and defensible physics-vs-PIML decision for frozen SO1–SO3 under extreme heat.

- **O1 Scope:** preserve thermal P↔Tₑ boundary, state/time and required/delivered electricity/mobility services. Exclude unrelated historical RQ/H variants as active authorities.
- **O2 Discovery:** exhaust reasonably accessible scientific databases and technical sources using predeclared searches with all actual retrieved counts and export hashes.
- **O3 Qualification:** every included high-priority scientific claim traces to DOI, primary text, specific equation/page, equipment, measurement and verification/validation status.
- **O4 Synthesis:** explicitly distinguish published mature physics, component empirical evidence, true connected site evidence and unresolved directional mechanism; issue only bounded novelty claim.
- **O5 Experimental sufficiency:** decide separately whether transformer, charger, battery and coupled system have identifiable states with trustworthy observed data, clocks, topology, confounders and heldouts.
- **O6 Modeling:** establish conventional physics baseline; conditionally test PINN/PIML against baselines if data support it; compare physics validity and uncertainty, not just ML fit.
- **O7 Supervisor handoff:** deliver a focused literature memo and a separate dataset/model-choice memo with references, explicit remaining decisions and no unjustified causal claim.

## 2. Already available — retain, do not redo without a scientific reason

| Artifact | Current actual status | Location |
|---|---|---|
| Canonical problem / objectives | FROZEN SO1–SO3 and thermal-only scope | `project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md` |
| Systematic review V1 protocol | DRAFT available; searches and PRESS review unexecuted | `project/literature_review/thermal_pt_systematic_review_2026_11_03/SYSTEMATIC_LITERATURE_REVIEW_PROTOCOL_V1.md` |
| Query and FTEE templates | 8 search families ready; original database exports not populated | same review folder |
| Comparator audit | 10 candidate papers + additional close studies, **not** formal PRISMA inclusions | `project/data_qualification/2026-11-03/TARGETED_LITERATURE_THERMAL_PT_SYSTEMATIC_PROTOCOL_V01.md` |
| Original transformer field data | SINTEF 8,592 hourly samples; STREAM 419,184 station-time P/Q pairs; component/units limitations | `project/data_qualification/2026-11-03/THESIS_RESEARCH_CHECKPOINT_2026-11-03.md` |
| Original vehicle field data | TUM seven local Parquet files, ID1 ~40.4M records; 1023-like thermal anomalies, QA unfinished | `data/field_candidates/2026-11-03/TUM_ID1_FIELD_THERMAL_QA_2026-11-03.md` |
| Laboratory charging and model studies | KU Leuven, OSF, EPFL and working RQ1–RQ11 analyses; no same-site thermal coupling | research checkpoint and Report 1 on this branch |

**Never infer:** a paper count as completeness; experimental test of one component as coupled validation; unrelated measured datasets as same-site observations; training/PDE-collocation points as independent physical test data.

## 3. Work packages / work breakdown structure

- **WP-G: Governance** (5 tracked tasks) — Scope and protocol quality: project authority, PRISMA-P/ScR choice, PRESS search review, change controls.
- **WP-S: Systematic searches** (6 tracked tasks) — Translate/exe source-dated database searches with original exports, hashing and citation chaining.
- **WP-C: Selection** (5 tracked tasks) — Traceable dedup, title/abstract/fulltext decisions, PRISMA counts only from actual records.
- **WP-E: FTEE extraction** (7 tracked tasks) — Primary-source equations, sensor/asset/time, measurement vs simulation, validation and physics tests.
- **WP-Y: Synthesis** (4 tracked tasks) — What is known, where field evidence is weak, SO1–SO3 map, novelty test, thesis chapter.
- **WP-D: Data readiness** (8 tracked tasks) — Original SINTEF/STREAM/TUM and charging data QA; connected field gate; observational identifiability.
- **WP-M: Model selection** (6 tracked tasks) — Conventional physics baseline, PINN/hybrid comparisons conditional on experimental evidence, uncertainty and sign-off.
- **WP-R: Supervisor deliverables** (5 tracked tasks) — References, 2–3 page prior-work memo, 1–2 page data/method memo, research handoff and archive.

**Master task register:** `PHELAN_EXECUTION_TASK_REGISTER_V1.csv`. Every row has ID, activity, dependencies, priority, owner, output, explicit exit gate and initial status. Statuses are grounded in existing repository; planned tasks were not marked done.

## 4. Critical task dependencies and acceptance gates

| Gate | Must pass before claim | Acceptance evidence | If not passed |
|---|---|---|---|
| **L0 — Protocol** | Call work systematic/preregistered | Frozen objective, documented reviewer mode, database strategy and actual search logging | Protocol draft only |
| **L1 — Search** | Claim broadly searched literature | Database outputs with date, full exact strings, limits, exported records and hash; named inaccessible sources | Limited/targeted narrative review only |
| **L2 — Screen** | Claim a systematic included set or PRISMA counts | DOI/title dedup, all screening decisions, full-text exclusions and reconciled arithmetic | Candidates only; no invented PRISMA flow |
| **L3 — Physics evidence** | Say prior paper proves an equation, parameter or numerical result | Primary PDF page/equation, units, BC/IC, equipment, validation domain and source identity | Hypothesis/abstract-level only |
| **L4 — Observed coupling** | Say a directional thermally mediated P↔Tₑ link was field-validated | Dated feeder/transformer–EVSE link, matched source and receiver time series, reason codes, non-EV load, weather/SOC controls | Not established; component-only |
| **D0 — Data eligibility** | Calibrate/validate thermal component | Real unmodified source data, calibrated signal definition, clocks, anomaly QA, representative forcing, independent test | Physics-only/conditional scenario |
| **D1 — PIML method decision** | Use PINN/hybrid as data-supported method | D0 + observable target, identifiable relevant parameters, prespecified physics baseline/validation split/UQ | Physics model remains baseline; optional purely numerical PINN is not a field claim |
| **D2 — Joint PIML** | Claim coupled field-tested PINN | D1 + L4 for needed interface, actual both-side synchronized state and service evidence | Component model only or conditional coupling simulation |
| **S0 — Supervisor-ready** | Report what others did and recommend method | Verified bibliographic corpus, six-domain critical comparisons, bounded gap, evidence-backed data/model recommendation | Explicit working findings plus unresolved questions |

## 5. Two parallel research tracks, one decision meeting

```text
A. LITERATURE:  protocol -> fresh searches -> screening -> FTEE/QA -> gap synthesis
                                     |                         |
                                     +--> methods/data used ----+
                                                                v
B. MEASUREMENTS: existing field source provenance -> QA -> observability/identifiability
                                                                |
                                                                v
                 physics baseline + conditional ML pilot -> method decision -> supervisor memo
```

**The experiments do not substitute for literature completeness, and the literature cannot prove experimental data existence.** Both feed the method-selection gate.

## 6. Suggested execution cadence (planning windows, not promises)

| Window | Activities and dependencies | Concrete checkpoint |
|---|---|---|
| **Week 1** | G01–G05 + S01–S02. Scope, reviewers, query peer-check, protocol version and database access. Parallel: D01; TUM file hashes. | Protocol/search QA accepted; blockers documented |
| **Week 2** | S03–S05; C01–C02. Original exports, hashes and de-dup. Seek primary RACE/Bragone/Gong/Krama/Li full texts. | Reproducible search and screening ledger; no estimated PRISMA numbers |
| **Weeks 3–4** | C03–C05; E01–E06. Full texts, evidence/equation extraction, strict risk/domain appraisal. Parallel D02–D06 access attempts. | Auditable included set, PRISMA flow, study-by-mechanism table |
| **Week 5** | E07; Y01–Y03. Reproduce top comparator laws if data available; establish overlap, disagreement, and bounded gap. | What-others-did matrix and preliminary gap memo |
| **Week 6** | D07, M01–M03. Data/readiness matrix and baseline selection. PINN/hybrid only if measurement gates admit. | A/B/C method decision with evidence and limits |
| **Weeks 7–8 (conditional)** | M04–M06; Y04; R01–R04; final updated search S06 near handoff. | Completed literature synthesis + data/method memo for supervisor |

Windows are **relative planning guides**, not evidence of work performed or a guarantee of access, model success, or delivery on a future schedule. If licensed database access or field telemetry is denied, mark blocked and continue on the scientifically valid path without fabricating substitutes.

## 7. First concrete research sprint: sequenced starting actions

1. **G01/G02:** Reconfirm SO1–SO3 and decide **systematic evidence map with critical synthesis**; specify whether PRISMA 2020 and/or PRISMA-ScR fits the final review type. Both are reporting aids, not correctness proofs.
2. **S01:** Translate the seven search blocks to at least one actual database syntax. Query full terms for thermal transformers, charger derating, same-site measurements, dynamic coupling, PINN, state time and delivered services. Include foundational non-EV transformer models.
3. **G03/S02:** Apply PRESS to the main query, preferably by a qualified independent person. Log missing access rather than silently treating web search as Scopus.
4. **S03/S04:** Run accessible platforms and preserve exact records/export hashes. Start title/abstract corpus only *after* search run.
5. **C01/C02:** DOI dedup and reviewer-declared eligibility. Compare old 325 paper/200 slot lists **only after fresh retrieval** as search coverage diagnostics, not automatic inclusions.
6. **D02/D03:** In parallel, freeze TUM 7-file SHA256 and probe source decoding; retain accepted SINTEF raw checksum and validated/invalid ambient operating domain.
7. **D05/D06:** Seek original Qatar EVSE rectifier/derating data and Li bus-transformer measurement evidence; request one actual mapped transformer–EVSE field installation. No guarantee data will be released.
8. **M01:** Write the minimum conventional physics model from identified/qualified equations, preserving transfer limitations; do not freeze a PINN before D1.

## 8. Data-to-model decision: explicit options

| Observations admitted | Defensible next step | Claim NOT allowed |
|---|---|---|
| **A: No valid thermal observation** | Conservation-based reduced ODE/PDE with verified numerical tests, sensitivity/UQ and labeled scenarios | Empirical calibration, validated PINN or observed coupled resilience |
| **B: Only transformer / battery / EVSE component observations** | Fit/test separate component physics; optionally trial physics-informed ML/PINN on measured component target with heldout baselines | Field validation of physically connected transformer–EVSE |
| **C: Same-site connected thermal + electrical + cause/service observations** | Fit and compare coupled physics, hybrid PIML and PINN with frozen time/site holdout, competing explanations and UQ | Generalized causal claims outside observed regimes or untested robustness |

**Preliminary current branch:** component data exists, but no admitted same-site transformer/EVSE thermal–electrical–service coupling. Thus pure physics baseline is viable now; component PIML pilot is conditional; joint field-validated PINN is **BLOCKED**. A PINN may solve a forward PDE without field data, but that is not Professor Phelan's experimental-data-based modeling justification.

## 9. Rigorous supervisor-ready package and evidence test

- **Deliverable A:** 2–3 page *What previous studies did, and what remains* organized by SO1–SO3, with claim-level primary DOI/page citations, evidence strata and bounded gap.
- **Deliverable B:** Complete versioned search + PRISMA-S log, actual PRISMA selection flow (if searches complete), full-text exclusions, and APA7 reference list. Cite PRISMA 2020 DOI:10.1136/bmj.n71, PRISMA-S DOI:10.1186/s13643-020-01542-z, PRISMA-P DOI:10.1186/2046-4053-4-1, and PRESS DOI:10.1016/j.jclinepi.2016.01.021 where relevant.
- **Deliverable C:** Full FTEE extraction of the closest comparator papers (including Gong, Bragone, RACE, Krama, Li, and other fresh-search inclusions) with equations, sensor locations, observed versus simulated states, baseline metrics and limitations.
- **Deliverable D:** One-page experimental-readiness matrix for SINTEF/STREAM/TUM/EVSE data, hashes, source-data rights and observable states, with P→Tₑ / Tₑ→P cases kept distinct.
- **Deliverable E:** 1–2 page *Physics vs Physics-informed ML* decision memo, baselines, data requirements, independent validation, UQ, and go/no-go justification.
- **Deliverable F:** Reference manager library, scripts, full-text access audit and handoff manifest; no unauthorized upload of paywalled PDFs or private operational records.

**Phelan acceptance test:** Can an independent reader (1) identify the exact prior paper and result for each thesis mechanism; (2) see where an equation came from and what instrument, if any, tested it; (3) reproduce the search/selection decisions; and (4) understand why suitable data support a specific physics-informed model—or why conventional physics is chosen instead?

## 10. Risks, controls and stopping rules

| Risk | Control |
|---|---|
| Database subscriptions/incomplete discovery | Log denied platforms and alternatives; make coverage-qualified claims, not exhaustive claims |
| Reference bias toward known papers | De novo mechanism searches; historical lists used for post-search recall diagnostics only |
| No independent second screener | State single-reviewer limitation; preserve adjudication and targeted audit; AI ≠ second human |
| Abstract-only inference | Claim labeled candidate until full text/page/figure verification |
| Missing raw EVSE field files | Document access-request attempts; continue qualified physics model, not invented sensor data |
| TUM coded temperatures / incorrect channel meaning | Preserve raw; flag 1023-like readings; resolve UDS metadata before calibration |
| Cross-site pseudo-coupling | Strong site/asset/time topology gate; never merge unrelated records as one installation |
| Unidentifiable parameters and overfit PINN | Reduced physically meaningful model, independent temporal/device holdout, persistence baseline, UQ, physical residual |
| Unsupported extreme-heat extrapolation | State exact measured ambient/hardware range and model-only outside-range scenarios |
| Service overclaim | Distinguish charging power/energy proxy from measured travel/departure service and actual recovery |

## 11. Controlled terminology and work statuses

`FOUNDATION_AVAILABLE` means source/project facts already exist; `DRAFT_AVAILABLE` means document prepared but not approved or executed; `OPEN` means not done; `IN_PROGRESS` means partial work verified but full gate open; `EXTERNAL_DEPENDENCY` means access/approval is outside current reach; `BLOCKED_ON_*` and `CONDITIONAL` mean downstream work cannot be promoted until the named upstream evidence passes. No percentage of completion is inferred from task counts.

**Primary authority and baseline:** `project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md`, `project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md`, `project/literature_review/thermal_pt_systematic_review_2026_11_03/SYSTEMATIC_LITERATURE_REVIEW_PROTOCOL_V1.md`, and `project/data_qualification/2026-11-03/THESIS_RESEARCH_CHECKPOINT_2026-11-03.md`.

**External reporting-method sources (checked 2026-11-03):** https://www.prisma-statement.org/prisma-2020 ; https://www.prisma-statement.org/protocols ; https://doi.org/10.1186/s13643-020-01542-z ; https://doi.org/10.1016/j.jclinepi.2016.01.021 ; https://www.prisma-statement.org/scoping .
