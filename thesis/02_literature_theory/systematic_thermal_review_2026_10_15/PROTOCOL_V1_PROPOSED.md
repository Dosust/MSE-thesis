# PROPOSED SYSTEMATIC REVIEW PROTOCOL — VERSION 1.0
**Date drafted:** 2026-10-15  
**Status:** Protocol design ONLY; NOT registered, NOT executed as a completed systematic review  
**Scope:** Active 2026-10-07/08 canonical thermal Power–Electrified Transportation thesis scope  
**Official thesis title:** Physics-Based Mathematical Engineering of Power–Transportation Interdependencies for Resilience  
**Purpose:** Respond to Professor Pat Phelan's request for (i) a thorough account of prior work, and (ii) experimental-data-gated choice between physics-only and physics-informed machine learning.

## A. Governing scope and authority
- Read the active `project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md`, `project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md`, `project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md`, `project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md`, `project/CANONICAL_STATE_TIME_DEFINITIONS_V1.md`, and `project/CANONICAL_RESILIENCE_DEFINITION_V1.md`.
- Frozen SO1: identify and qualify thermally sensitive states and directed Power–Electrified Transportation thermal mechanisms.
- Frozen SO2: develop a physics-based state–time representation of qualified thermal mechanisms under extreme heat.
- Frozen SO3: quantify critical transition times, propagation delays, and electricity/mobility-service consequences.
- Minimal-sufficient physics. External heat forcing != internal state; thermal state != capability != service != resilience; co-exposure != causal interdependency; EVSE belongs to the Electrified Transportation System, not a third infrastructure; P→T_e and T_e→P qualified separately.
- The earlier seven-stage broad RQ/SO/H files carry October 7 thermal supersession notices. They remain methodological history, NOT the default active list of seven objectives. Two-pathway sustainability and Improve/Adapt/Restore are bounded downstream context only, not independent main review themes.
- Use the exact separate canonical title authority even if the V4 document header uses a different title string. Do not silently amend frozen canonical files or the old Austin/flood case to fit a heat case.

## B. Review type, title and principal question
**Review type:** Protocol-led systematic evidence mapping PLUS focused systematic critical/narrative synthesis, with separately audited data availability. This is not a systematic review of every generic infrastructure resilience topic and is not a priori a meta-analysis.
**Working title:** *Thermal Interdependencies Between Power and Electrified Transportation Systems Under Extreme Heat: A Systematic Review of Physical Mechanisms, Experimental Evidence, Modeling Methods, and Service Consequences*.
**Main question:** What experimental and computational evidence establishes extreme-heat-dependent physical mechanisms, state–time evolution, directed Power–Electrified Transportation interdependencies, and electricity/mobility-service consequences; which measurement and validation conditions justify each modeling approach?

### Review subquestions
- **SLR-Q1 / SO1:** Which thermal states and directional coupling mechanisms have been theoretically proposed, physically measured, and causally qualified? Under which heat conditions and equipment/application boundaries?
- **SLR-Q2 / SO2:** Which governing equations (heat balance, transformer/line ampacity, EVSE conversion/derating, battery electrothermal, grid power flow/DAE, service mapping) and model families have been used? Are parameters identifiable and validity boundaries reported?
- **SLR-Q3 / SO3:** Which thermal thresholds, critical times, propagation delays, charging-time changes, electricity-service and mobility-service outcomes are measured, predicted, or merely simulated?
- **SLR-Q4 / DATA:** Which raw observations actually exist and are obtainable? Are heat/thermal state, electrical input/output, SOC, control, equipment identity, time, sensor uncertainty and a target service measured in the same experiment/site? Can measurement data be used legally and reproduced?
- **SLR-Q5 / METHOD:** Under matched independent tests, when does physics-only, grey-box/system identification, or PINN/physics-informed residual learning add validated predictive, physical-consistency, uncertainty or computational value?

## C. Corpus architecture: four linked evidence streams
1. **CORE DIRECT COUPLING:** explicit Power ↔ Electrified Transportation thermal interface studies and field experiments. Highest directness for cross-system conclusions.
2. **COMPONENT PHYSICS:** transformer/line thermal state, charger/EVSE thermal derating, battery/BMS electrothermal state, vehicle energy/heat and transportation-service conversion. Supports specific model modules; cannot establish whole-system coupling by itself.
3. **MODELING & VALIDATION:** conventional physical numerical models, stochastic grey-box/system identification, PINNs and other physics-informed ML; estimation/observability, uncertainty, physical hard/soft constraint distinction and independent benchmarks.
4. **DATA & SERVICE:** public/restricted original sensor data, data papers, repository documentation, charging sessions, local electric load, heat weather station data and measured mobility. Assets are recorded separately from publications; a dataset named in an article is not automatically accessible.
**Context only:** general SoS, generic infrastructure resilience and broad sustainability/organization papers may be cited narratively for definitions but are not forced into the active thermal evidence denominator. The existing accepted core list is a *seed*, not a substitute for systematic retrieval.

## D. Search and retrieval protocol
**Database targets:** Scopus, Web of Science Core Collection, IEEE Xplore, Engineering Village/Compendex as accessible; additional publisher-indexed search (ScienceDirect, Springer, Wiley, IET), Crossref/OpenAlex for DOI validation and backward/forward citation tracing, Google Scholar for supplementary citation chasing with explicitly bounded/query-logged procedures; arXiv/preprints in a separate publication-status class. Zenodo, Dryad, Figshare, Data.gov, DOE/OSTI, NASA, NOAA, NREL and institutional repositories for dataset discovery.
**Coverage:** database inception to the final search date (start no later than October 2026); no arbitrary publication-year exclusion. Record earliest/latest publication dates and exact search date. Include eligible English/French studies if feasible; log translation/access limitations; do not assume all-index English completeness. Search may be updated immediately before final thesis submission.

### Independent conceptual blocks (adapt to each database syntax)
- A = (`"extreme heat"` OR heatwave* OR `"ambient temperature"` OR `"thermal derating"` OR `"temperature-dependent"` OR electrothermal OR therm*).
- B = (`"power distribution"` OR `"distribution transformer"` OR `"electrical grid"` OR ampacity OR feeder).
- C = (`"electric vehicle"` OR `"electrified transport"` OR EVSE OR `"fast charg*"` OR `"charging station"` OR `"battery management"`).
- D = (interdependen* OR coupl* OR interface* OR `"co-simulation"` OR `"power-to-transport"` OR `"transport-to-power"`).
- E = (experiment* OR `"field measurement*"` OR `"measured data"` OR `"thermal test*"` OR validat* OR dataset).
- F = (`"physics-informed"` OR PINN* OR `"grey-box"` OR `"gray-box"` OR `"system identification"` OR `"hybrid model"`).
- G = (derat* OR `"charging time"` OR `"service reliability"` OR `"vehicle availability"` OR `"mobility service"` OR `"transition time"`).

### Search lanes; DO NOT conjoin all blocks
- L1 Direct P–T_e thermal interfaces: **A AND B AND C**; sensitivity search **B AND C AND D** without A.
- L2 Charger heat physics: **A AND C AND (charger OR EVSE OR rectifier OR connector)**. Translate to valid per-database syntax.
- L3 Transformer and network heat physics: **A AND B AND (thermal OR temperature OR dynamic-rating OR hotspot)**.
- L4 EV battery / charging / vehicle thermal dynamics: **A AND C AND (battery OR SOC OR BMS OR HVAC OR driving)**.
- L5 Experimental and measured data: **(A AND C AND E)** OR **(A AND B AND E)**; direct repository searches separately.
- L6 Physics-informed method comparators: **F AND (transformer OR EVSE OR charger OR battery OR thermal)**; search physics-only baselines separately to prevent method-selection bias.
- L7 Consequence/response: **A AND C AND G**, plus broader directly coupled service literature **B AND C AND (mobility OR resilience OR service)**.
Use title/abstract/keyword field searching in indexed databases, and controlled vocabulary where available. Avoid results that are only driven by `thermal` used unrelatedly; validate a pilot batch. Exact string, date, filters, syntax, count, database interface and export identifier logged for every run.

### Search sensitivity checks
Known-item sentinel set must be retrievable or the source of omission explicitly diagnosed: Rinaldi 2001 (context), Fotouhi 2017 (direct P–T background), Balogun EV-EcoSim, Blomgren 2023 transformer grey-box, Bragone 2022 transformer PINN, Krama et al. 2026 Qatar charger, Schreiber et al. 2026 TUM EV field. Some sentinel items belong to different streams; the union of lane searches, citation chasing and context-seed register should cover them.
Obtain PRESS-style peer review of full strategies before definitive execution where a qualified person is available.

## E. Eligibility and exclusions, prespecified
**Core include:** English/French peer-reviewed research reporting explicit thermal models, measurements or time-dependent physical constraints for P, T_e or their interface under stated heat/temperature conditions; direct coupled analyses; comparators that evaluate physics vs grey-box vs PINN; relevant verified original datasets and technical reports with sufficient method detail. Studies may be experimental, field observational, numerical or mixed, but are labeled separately.
**Context include (coded separate):** foundational laws, standards/reviews and non-heat coupling models necessary for physical definitions or benchmarking; not treated as direct heat evidence.
**Exclude from primary evidence synthesis:** generic EV adoption, purely economic market forecasts, generic climate vulnerability without thermally resolved mechanisms, unrelated road incidents, articles with no recoverable method or empirical/theoretical claim relevant to the question, duplicated preprint/journal versions (count as a single study), unverified marketing claims; unrelated thermal systems. Do **not** exclude simply because a study contradicts a proposed thesis mechanism.
**Full text unavailable:** label `AWAITING_FULL_TEXT`, do not fabricate equations or infer validation from an abstract. Paywalled papers can be included in identification counts but cannot be represented as PDF-verified.

## F. Selection process and auditability
1. Run each search; export RIS/BibTeX/CSV with immutable search-run ID and results count.
2. Deduplicate first by DOI, then title/authors/year/fuzzy match, inspect multiple reports of one study. Retain original references and duplicate linkage table.
3. Title/abstract screening with independent decisions by two human reviewers if feasible; pilot-calibrate on an agreed sample. If solo, disclose deviation; AI can recommend but does not count as a second human reviewer.
4. Full-text eligibility reviewed by two people independently where feasible; disagreements resolved by recorded consensus/third adjudicator. Record per-paper reason for exclusion.
5. Keep PRISMA flow numbers as `NOT YET MEASURED` until actual exports and selection logs exist: identified, deduplicated, screened, sought, unavailable, excluded by reason, included.
6. Follow backward and forward citations for every directly relevant included study and known major reviews; track these as a separate identification method and deduplicate.
7. Store exact PDF/version and provenance where licenses permit, including DOI, journal/preprint version, section/page/equation/figure/table mappings; no unauthorized distribution of PDFs.

## G. Extraction schema — ONE study per study_ID; separate paper_ID and dataset_ID
**Bibliography:** study_id, paper_id, canonical DOI/title/authors/year, publication status, version, provenance, source registry.
**Boundary:** physical P/T_e system classification, EVSE position in T_e, equipment type/ratings, component vs cross-system, public DCFC vs fleet/depot vs other, geography and heat range.
**Mechanism:** source → recipient direction, heat forcing, thermal state, capability/constraint, exchanged quantity, operational state (SOC etc.), claimed service output, mechanism activation conditions, validity range, shared exposure vs directional effect.
**State and time:** thermal capacitance/time constants, internal thermal state, energy state, slow ageing if admitted, transition threshold, input forcing profile, time resolution, lag/propagation time, recovery time (if genuinely modeled).
**Mathematics:** governing conservation law, ODE/PDE/DAE/algebraic law and discretization, boundary/initial conditions, causal guard/reset, model parameters, observable outputs, solver, code and computational cost.
**Evidence:** lab/field/simulation/synthetic/reanalysis; sensors, accuracy, calibration, experiments and independent devices, sample size and heat events, full-PDF equation/page citation.
**Identifiability:** whether unknown states and parameters can be identified from stated sensors, independent variation/excitation, sensitivity/fisher information/observability/rank evidence, uncertainty sources.
**Validation:** independent site, session, vehicle, temperature regime/time period; baselines under matched inputs/budget; held-out predictions; residuals; energy conservation; thermal-threshold validity; calibration uncertainty; failure cases; limitations.
**Data availability:** DOI/repository URL, access date, direct raw download attempted Y/N, file types/size, checksum if downloaded, field names+units/timezone/sampling, license, missingness QC, same equipment/site/time keys, permissions, data-on-request status, gaps.
**Results/conclusions:** effect size and uncertainty (only if source directly reports), supported claim, contrary evidence, transferability, link to SO1/SO2/SO3, explicit unsupported conclusions.

## H. Dataset readiness / empirical claim classes
- **DA-0:** bibliographic mention only; no accessible documentation.
- **DA-1:** metadata/landing page confirmed, raw observations not opened.
- **DA-2:** actual file downloadable/opened; channels and timestamps inspected.
- **DA-3:** units, sensors, heat span, missingness, independent trajectories and physical consistency audited.
- **DA-4:** parameters and target states identifiable/estimable for bounded component mechanism; permitted reuse and matched holdout established.
- **DA-5:** experimentally observed, traceably aligned power↔T_e thermal interface AND required service response; causality/selection/confounders and independent validation addressed.
Note: DA-5 is not currently achieved by the previously reviewed public datasets. Do not combine geographically unrelated NASA+Qatar+ACN+PeMS files and call them an experimental observation of the complete coupled system.

## I. Critical appraisal (domain-specific; per claim, NO naive total quality score)
Q1 design and measurement provenance; Q2 boundary/state correspondence; Q3 physical and causal mechanism qualification; Q4 exposure and excitation variation; Q5 parameter identifiability; Q6 validation independence/data leakage; Q7 numerical correctness/conservation and solver convergence; Q8 uncertainty/calibration; Q9 transferability and domain of validity; Q10 data/code accessibility/licensing; Q11 reporting of adverse or non-improving baseline results.
Per item: **supported / partial / not demonstrated / not applicable** with the exact paper section/page evidence. High simulation fidelity is not a substitute for field validation. PRISMA itself is a reporting checklist, not a study-quality metric.

## J. Synthesis plan
1. Evidence map by study type × thermal component × directional P→T_e/T_e→P × heat range × measurement class × method × validation maturity.
2. Physics mechanism map: *heat forcing → thermal state → capability limit → cross-system dependency → electricity/mobility service*; distinguish measured and merely hypothesized arrows.
3. Equation comparison: same unit/physical boundary across published transformer, charger, battery and system equations; derive conserved quantities, state/time/parameter maps, differences and missing observables.
4. Independent empirical validation synthesis: report model RMSE/MAE/transition timing and uncertainty only with comparable outputs/conditions; do not pool unrelated metrics across transformers, chargers and vehicles. Where quantitative meta-analysis is unjustified, produce structured narrative synthesis.
5. Data map by observed heat/thermal/electrical/vehicle/mobility/time/site variables; rank suitability for specific model tasks, NOT 'best overall dataset'.
6. Contradictory/null findings, negative controls, publication bias and transferable/unsupported claims explicitly recorded.
7. Thesis gap table: established prior art, exact unproven inference, data requirements, confirmable hypothesis, method options, external-validity ceiling.

## K. Model decision and result gates
- **M0 physics-only:** derive/test relevant conservation, heat balance, power and energy boundaries; parameter ranges/bounds sourced; if no measured target data, claim verified simulation only.
- **M1 grey-box:** if data cover input/output and dynamics, fit identifiable physical parameters with noise/state estimation; test prediction/uncertainty on independent heat episodes.
- **M2 PI-ML/PINN:** if enough measured variation and relevant thermal states/residuals are available, train physically constrained learner, compare against M0, M1 and a well-tuned unconstrained control with matched splits/inputs/computational budget. Soft PINN losses do NOT prove exact physical feasibility.
- Choose M2 only when it demonstrates material incremental value in a prespecified criterion; otherwise choose the simplest validated method. No prediction superiority claim without experiment.
- Separate the model-family names `PHY`, `GREY`, `PIML` from the *older unrelated* thesis M0/M1/M2 uncoupled/static/dynamic labels.

## L. Deliverables and stopping rules
**D0** Approved/reviewed protocol with explicit scope authority and search strategy.
**D1** Database search-log + raw exports + dedup ledger + screening decisions + PRISMA diagram.
**D2** Full-PDF-verified evidence/claim ledger, paper-level equation and empirical-design extractions.
**D3** Public/private dataset availability and raw-file feasibility audit, versioned downloadable-checksum log.
**D4** Heat mechanism/state-time graph, measurement/observability requirements matrix.
**D5** Matched method-comparison plan and selection decision tree.
**D6** Chapter 2 critical systematic narrative with honest limitations and frozen-vs-proposed gap register; one-page advisor memo.
**Stopping:** no 'completed systematic review' unless planned searches are executed, extraction and screening logs auditable, access exclusions documented, and final synthesis follows prespecified logic. Freeze a search cutoff and provide update search before thesis submission.

## M. Pilot and prioritization
**Pilot first:** Review original full PDFs and raw dataset documentation for (i) direct heat-induced EVSE derating; (ii) transformer thermal state; (iii) battery electrothermal response; (iv) actual charging service; and (v) published physics/grey-box/PINN comparisons. Use a small calibration sample only as an *instrument test*, never as the final denominator.
**Highest-value candidate data audits:** Qatar 2026 heat-derating field data (on request), Argonne EV/EVSE measured profiles (access uncertain), TUM UDS raw logs via LFS, NASA thermal battery experiments, KIT charging sessions, ETT-small transformer temperatures, ACN timed current/pilot, Pecan Street EV circuit loads and linked NOAA. Each remains in its own equipment/sample provenance partition until justified coupling is demonstrated.
**First scientific conclusion due to advisor:** identify *what is already known* and *which direct thermal interface data are usable*, then conditionally select the model family.

## N. Review methods authorities (adopt appropriately, not mechanically)
- PRISMA 2020 reporting guideline: https://www.prisma-statement.org/prisma-2020
- PRISMA-P protocol reporting guideline: https://www.equator-network.org/reporting-guidelines/prisma-protocols/
- PRISMA-S reproducible search reporting: https://www.equator-network.org/reporting-guidelines/prisma-s/
- PRESS 2015 search-strategy peer review: https://doi.org/10.1016/j.jclinepi.2016.01.021
- Petersen et al. 2015 systematic evidence mapping: https://doi.org/10.1016/j.infsof.2015.03.007
- Cochrane screening principles (adapt to engineering domain, not claim medical intervention applicability): https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04
- OSF generalized systematic review registration: https://help.osf.io/article/330-welcome-to-registrations

**No registry action, authenticated database search, paper screening, PDF audit, author contact or final model-selection decision was performed solely by creation of this protocol file.**
