# Systematic Literature Review Protocol — v0.1

**Start:** 2026-11-03  
**Status:** Version-controlled, *not externally preregistered*, subject to supervisor review before formal screening.  
**Thesis title (frozen):** Engineering of Power–Electrified Transportation Interdependencies for Resilience  
**Scope (frozen):** Thermal physical states and **directional** interdependencies between the power system and electrified transportation during extreme heat. Other disturbances, economics, planning and power-quality-only studies are auxiliary, not the primary endpoint.  
**Objective authorities:** SO1 qualify thermally sensitive directional mechanisms; SO2 physics-based state-time dynamics; SO3 critical transitions, propagation delays, required electricity/mobility service consequences.

## Primary research question

What experimentally supported thermal states and physical mechanisms link distribution/power transformers and EV charging equipment under extreme heat; how have their time-dependent, electrical and thermal dynamics been mathematically modelled, verified and validated; and what evidence supports causal interdependency, propagation, service consequences and transfer to another installation?

## Subquestions and streams

- **A: Power transformer physics** — loss mechanisms and thermal heat balance; top-oil/winding/hot-spot; cooling and heat capacity, model parameter identifiability, high-ambient validity.
- **B: EVSE + relevant vehicle boundary** — charger rectifier/heatsink/cooling temperature and thermal derating; offered versus accepted charging power, AC/DC metering, vehicle SoC and battery heat **only when relevant to an EVSE thermal mechanism**.
- **C: Physical Power↔Electrified Transport interdependencies** — verified supplying transformer/feeder/EVSE topology, measured or simulated charger loads, bidirectional operational restrictions, thermal transitions and electricity/mobility services.
- **D: Mathematical and verification methods** — differential-state models, parameter identifiability, numerical V&V, UQ, physics-informed and physics-only alternatives, transferability. Mathematical methods papers may be retained as *supporting theory*, not counted as primary installation evidence.

## Evidence question framework (engineering adaptation)

- **Systems/assets:** transformer; feeder/distribution circuit; DC/AC EVSE; EV and battery only as bounded electrical/thermal input/output.
- **Forcing/exposure:** ambient/extreme heat, charging/load variation, heat rejection/cooling state; secondary measured electrical disturbances if relevant to a thermal mechanism.
- **Outcomes:** measured T, I, V, P, Q, delivered EV charging power, thermal derating, protection, threshold time, propagation delay, service deficit/recovery, model uncertainty.
- **Study designs:** original field measurements, controlled lab observations, physics-derived simulation with empirical parameters, analytical models and methodological validation benchmarks—each **stratified**, never pooled as the same evidence strength.
- **Comparators:** IEC/IEEE thermal laws or simpler RC/physical models, persistence/ambient-only baselines, alternative numerical methods, measured independent holdouts; simulation scenarios where explicitly labelled.

## Eligibility — title/abstract then full-text

**Include as primary eligible** if original work contains **at least one**: (i) measured transformer temperature/load and a testable thermal model/mechanism; (ii) original EVSE internal thermal/cooling/derating telemetry and a testable model/mechanism; (iii) an explicit physical or modelled transformer/feeder→charger thermal/electrical interaction with measurable time/state/service outcomes; (iv) original experimental/numerical verification of thermal-model parameters, uncertainty or transfer within these system classes. Simulation-only studies are eligible as **MODEL ONLY** with separate evidence tagging.

**Supporting not primary:** standards, methods/theory, relevant reviews, electrical-only/vehicle-only datasets and infrastructure inventories for reference mining or signal-boundary definitions. Do **not** treat an abstract or a review's second-hand claims as raw measured evidence.

**Exclude from primary synthesis:** location-only charging directories, pure economics/attitudes, battery thermal runaway/chemistry unrelated to charging power/grid thermal interface, non-EV unrelated cooling, static reliability without time-dependent heat or service, other electric transport cases without analogous physical interface, vendor marketing without reproducible evidence, duplicate republications (retain most complete report). Exclude records with insufficient details only after attempting accessible full text; retain full explicit reason.

**Temporal and language policy:** Search through **2026-11-03 inclusive**, no filter on year at initial information retrieval so foundational work is not lost; record original publication date and edition. Do not impose a search-language filter. Assess English and French full text directly; flag other-language records for translation rather than silently exclude. Peer-reviewed articles, full conference proceedings, university theses and original data-repository technical papers can be eligible; tag peer-review status; preprints require additional caution. Source type is not equivalent to evidence quality.

## Source discovery

Execute database-specific reproducible searches in **Scopus, Web of Science Core Collection, IEEE Xplore**, and relevant engineering publisher indexes **if actually accessible**, plus Crossref/OpenAlex/Google Scholar as recorded supplements, backwards/forwards citation searching, and targeted original repositories (Zenodo, OSF, KU Leuven, KIT, SINTEF). PubMed is not a core database for the engineering question. For every run capture platform, collection, local date/time, complete exact pasted executed query, API/web version, date/subject filters, raw count, download RIS/BibTeX/CSV or identifier list, export filename and SHA-256. Mark inaccessible databases **NOT RUN**; do not imply searched.

## Screening, deduplication and second-reviewer constraint

1. Preserve source exports immutable; deduplicate DOI (normalize case/URL), then normalized title+year+author, manually check same-study duplicate data.
2. Title/abstract screening using above written criteria; record **include / exclude (reason code) / unclear**, supporting class A–D.
3. Full-text verification with study design and instrument details; assign original evidence type *FIELD SAME SITE* vs *FIELD SEPARATE SITE* vs *LAB* vs *SIMULATED WITH MEASURED INPUTS* vs *SYNTHETIC* vs *THEORY/REVIEW*.
4. Second human reviewer independently screens eligibility for defensible dual-reviewer claims. An AI assistant's parallel recheck is **not independent human screening**. Until a reviewer is assigned, mark single-screener evidence and log unresolved disagreement for supervisor adjudication.
5. Record exclusions with mutually intelligible reasons at full text: E1 wrong system; E2 no thermal/time mechanism; E3 wrong study type/nonprimary; E4 missing full text/insufficient description; E5 duplicate; E6 publication after cutoff; E7 wrong exposure/outcome.
6. **PRISMA totals are blank until actual export, deduplication and screening.** A seed list or results page does not equal formal database records identified.

## Critical appraisal and bias / evidence grading (custom engineering domains, NOT a validated universal score)

Rate each domain **LOW CONCERN / SOME CONCERN / HIGH CONCERN / NOT REPORTED / NOT APPLICABLE** with 1–2 source-specific sentences:
- Q1 measurement authenticity (instrument type, calibration, resolution, raw availability, error bounds);
- Q2 representativeness (real field vs lab vs synthetic; equipment/cooling/rating/heatwave exposure);
- Q3 physical connectivity and direction (same feeder/transformer/EVSE IDs, topology, intervention);
- Q4 temporal and confounding integrity (synchronized clocks, initial states, other loads, SOC, PV, season, ambient);
- Q5 physical formulation (heat/energy conservation, signed units and AC/DC measurement boundaries);
- Q6 model verification and independent validation (solver/time convergence, split before tuning, baseline, errors, serial dependence);
- Q7 uncertainty (sensors, calibration, structure, forcing, extrapolation, interval coverage);
- Q8 transfer (new equipment/site independent test; explicit tested applicability limits);
- Q9 reproducibility (DOI, publicly accessible code/data, equipment and parameter disclosure).
These ratings are **not** to be combined into an unsupported numeric quality index. Synthesize evidence by design, and give most weight to physically connected measured, reproducible, independently validated studies. Unknown is not a pass.

## Data extraction (predefined)

Use [EVIDENCE_EXTRACTION_TEMPLATE.csv](./EVIDENCE_EXTRACTION_TEMPLATE.csv) for each full-text eligible study. Include identifiers, exact quote/page for key equation/claim, model class, variables/units, nameplate, temperatures, sensors, system boundary/connectivity, thermal exposure range, sampling and duration, interventions, forcing, source vs processed/synthetic data, calibration/test split, VVUQ, conclusions and limitations. Do not invent missing cells. Link to original data/code where licensed.

## Synthesis plan

Evidence-map all eligible original works by **stream × study design × physically measured states × same-site topology × extreme-heat exposure × model type × validation level**. Narrative synthesis with mechanistic equation and parameter tables will be primary. Do **not** meta-analyze heterogeneous RMSEs or cooling coefficients from incompatible sensors, units and sites. A quantitative pooling step requires pre-specified physically comparable estimands, suitable common measurement boundaries, uncertainty and heterogeneity analysis. Track negative and unidentifiable findings.

## Claims and stopping conditions

- A true **measured coupled field thermal interdependency** requires verified asset/feeder ID, common clocks, relevant temperatures, actual power/charger restrictions and measured service—not separate-site data merged as if co-located.
- **Physics-based simulation** remains useful but cannot be marketed as field validation.
- A reported PINN improvement must beat independently tested physics-only and basic statistical baselines with no data leakage; otherwise physics-only remains default.
- Heatwave/external-site transfer requires actual high-ambient and new-site/hardware measurements, not ±5°C virtual forcing around a Norwegian moderate-ambient site.
- Close the review only when all available planned databases and citation-chaining routes have either complete evidence logs or documented inaccessible status, screens/exclusions and critical appraisals are finalized, and PRISMA totals reconcile. This protocol cannot guarantee that a relevant paper does not exist.

## Protocol amendments and governance

Record all amendments before implementing them with version/date/reason/expected change to sensitivity and specificity. Do not silently change inclusion rules after screening the results. Supervisor review and independent human second screening remain outstanding.

**Methodology:** [PRISMA 2020](https://doi.org/10.1136/bmj.n71), [PRISMA-S](https://doi.org/10.1186/s13643-020-01542-z). Their checklists are reporting guides, not a methodological quality certificate. **This v0.1 is ready for prospective application; it is not yet a completed systematic review.**
