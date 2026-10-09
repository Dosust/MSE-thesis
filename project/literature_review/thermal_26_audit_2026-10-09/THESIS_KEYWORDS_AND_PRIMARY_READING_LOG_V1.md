# Thesis-derived 26-paper literature-review search and primary-reading log V1

**Date:** 2026-10-09  
**Status:** ACTIVE SCREENING + PARTIAL SOURCE EXTRACTION; **NOT** completion of 26 full texts; no originality claim or model admission.

## 1. Scientific authority

Title: **Physics-Based Mathematical Engineering of Power–Transportation Interdependencies for Resilience**.

Active research focus: thermally conditioned, separately qualified P↔T_e directional interdependencies during extreme heat, represented through physical state and time, with electricity and mobility service consequences.

Preserve frozen objectives verbatim in \`project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md\`, thermal scope, state-time definition, complete T_e system scope, evidence/non-invention, transformer admission ledger and frozen M0/M1/M2 semantics. Search, not a hypothesis of absence, establishes research-gap evidence.

## 2. Derive review dimensions from title, objectives and case architecture

| Concept from title or objective | Controlled synonym/search family | Scientific extraction priority |
|---|---|---|
| Physics-based | conservation laws, thermal network, oil-immersed transformer, heat transfer, electrothermal, equipment tests | physically valid loss/heat equations, cooling class, limits, parameters |
| Mathematical engineering | state space, ODE, differential-algebraic, constitutive law, numerical verification, identifiability | variables/units, assumptions, integration and validation |
| Power | distribution transformer, temperature rise, winding hotspot, top oil, thermal rating, protection | load→temperature→allowed capability (distinguish mechanism from policy) |
| Transportation | EVSE, DC fast charger, thermal derating, battery charging, SOC, road EV, fleet readiness | AC input vs DC output vs battery input, actual device limitation |
| Interdependencies | directional coupling, grid-loading response, operating constraint, interface, feedback | source→receiver, transfer units, activation, evidence |
| Extreme heat | heatwave, hot climate, ambient temperature, converter cooling | common external exposure vs genuine cross-system influence |
| State and time | thermal inertia, transition, causal delay, response time, hybrid events | temporal state equations, first passage, attributable direction |
| Resilience/service | charging completion, electricity adequacy, unmet EV energy, departure requirement | measurable service and required deadline, not generic aging alone |

Suggested focused strings to execute/record in scholarly indexes:
1. \`("distribution transformer" AND ("thermal model" OR "hot spot") AND ("EV charging" OR "electric vehicle") AND ("ambient temperature" OR heat))\`
2. \`(("DC fast charger" OR EVSE) AND ("thermal derating" OR "temperature-dependent power" OR rectifier) AND ("extreme heat" OR "hot climate"))\`
3. \`(("power transportation" OR "traffic power") AND ("dynamic coupling" OR "interdependency") AND (temperature OR thermal))\`
4. \`(("transformer" AND ("dynamic thermal rating" OR "thermal loading limit")) AND ("charging station" OR "electric vehicle fleet"))\`
5. \`(("vehicle charging" OR EV fleet) AND ("departure deadlines" OR "unmet energy") AND ("transformer temperature" OR "thermal limit"))\`
6. \`(("thermal" AND ("cross-system propagation" OR "state-time" OR "event delay")) AND ("power" AND "transportation"))\`

The search must keep dated database, fields, filters, DOI/title dedup, exclusions and accessible full-text status. The 26-paper limit is on **deep synthesis**, not overall discovery. Existing reproducible 687→404→433→200→26 flow remains historical, not a newly repeated search.

## 3. Initial primary reading — verified source evidence and boundaries

### R01 — Hilshey, Hines, Rezaei & Dowds (2013)
- DOI: https://doi.org/10.1109/TSG.2012.2217385
- Primary full source (9 pages): https://phines.w3.uvm.edu/publications/2013/hilshey_2013.pdf
- **Access:** AUTHOR-HOSTED COMPLETE PDF ACCESSED; sections 1–3 and stated conclusions inspected. Not yet a comprehensive equation-by-equation nine-page audit.
- **Problem:** what EV charging travel/schedule uncertainty does to transformer aging; whether thermal-aware charging reduces damage without preventing charging completion.
- **Input data:** residential base loads; measured/source ambient temperature series (Phoenix, Burlington); observed national travel survey profiles sampled to generate arrival/departure and charging loads.
- **Math:** stochastic Monte Carlo travel/vehicle charging model; charging-load equation (paper eq. 1), complex transformer-load composition (paper eq. 2); IEEE C57.91-1995 dynamic transformer thermal model (section III); charging/control rule comparison.
- **Case:** 25 kVA transformer, 12 homes, six sampled EVs, AC Level 1/2. Vehicle arrival, departure, energy-to-full and charging availability are modeled.
- **Finding supported:** ambient heat and charge timing change predicted aging; smart charge reduces modeled aging while meeting many charging needs; simple delayed overnight charge can worsen aging in this setup.
- **Novelty ceiling:** Cannot claim that thermally modeled transformers with EV charging schedules/vehicle energy completion are new. Single residential/AC Level 1–2 example cannot be silently generalized to an industrial DC depot.
- **Remaining full-text extraction:** individual IEEE heat ODE/DAE clauses, exact temperature control activation and numerical assumptions, evaluation limitations, confidence/uncertainty reporting and validation classification.
- **Source check:** author full paper at https://phines.w3.uvm.edu/publications/2013/hilshey_2013.pdf (paper pp. 1–4, 8–9).

### R02 — Gao, Patel, Liu, Wang & Bryson (2017)
- DOI https://doi.org/10.1049/iet-gtd.2016.0722
- Primary published full article: https://ietresearch.onlinelibrary.wiley.com/doi/full/10.1049/iet-gtd.2016.0722
- **Access:** Published full article indexed and substantively inspected in search retrieval; direct page-opening blocked 403. Do **not** assert clause-level independent complete download.
- **Problem:** actual parameterization and prediction accuracy of IEC-type transformer thermal model; EV hosting limits derived from credible temperature prediction.
- **Physics/math:** IEC 60076-7 top-oil and winding hot-spot modeling, thermal time constants, heating exponents, measurement-based parameter refinement and load/aging operating criteria.
- **Physical evidence:** one 1 MVA, 6.6/0.415 kV transformer and heat-run measurements; reported prediction-error improvements for constant/cyclic loading. Paper proposes operating criteria for its study, including HST, top-oil, relative loading and daily loss-of-life, **which are not automatically the permissible thermal setpoints of our unselected transformer**.
- **Novelty ceiling:** Temperature→transformer operating constraints→EV hosting and experimental parameter refinement are already studied. Do not invent a model from standard defaults alone or adopt the studied limits for new hardware.
- **Still needed:** full published PDF/download, exact equations and clause-level operating-policy applicability; independent measured validation details, error metrics and design transferability.

### R03 — Krama, Kamal, Sezer & Bayhan (2026)
- DOI https://doi.org/10.1016/j.ecmx.2026.101960
- Publisher open-access article: https://www.sciencedirect.com/science/article/pii/S2590174526004435
- University research record: https://elmi.hbku.edu.qa/en/publications/impact-of-extreme-climatic-conditions-on-fast-ev-charger-performa/
- **Access:** publisher and university abstracts/highlights inspected, OA complete article still requires page-level full-text extraction. **Not fully read.**
- **Problem:** in situ thermal derating and charging-service impact for an air-cooled commercial 50 kW DC fast charger under Qatar heat.
- **Evidence:** field ambient temperatures approx. 15–55 °C; rectifier thermal response and offered/delivered power; authors separately analyze charger-side and battery-side limitations; seasonal charging duration example.
- **Novelty ceiling:** heat-induced charger derating, altered charging service time, energy and SOC response have already been measured; do not present those as new discoveries.
- **Still needed:** converter constitutive/empirical curve, power-balance units, device-specific temperature threshold, holdout validation method and generalization limits.

### R04 — Visakh & Selvan (2023)
- DOI https://doi.org/10.1016/j.segan.2023.101096
- Publisher https://www.sciencedirect.com/science/article/pii/S2352467723001042
- **Access:** abstract only; publisher lists organizational access/purchase. Complete PDF needed.
- **Prior-art challenge:** EV-induced transformer thermal loading and immediate service-disruption mitigation, with charging-energy consequences; must check exact transformer-side thermal-capability law and control implementation.
- **No page-/equation-level claims until PDF provided.**

### R05 — Ji et al. (2025)
- DOI https://doi.org/10.1016/j.apenergy.2025.126806
- Publisher https://www.sciencedirect.com/science/article/pii/S0306261925015363
- **Access:** abstract/highlights only; complete PDF needed.
- **Prior-art challenge:** tri-level P–T coordination, temperature-aware routing/charging decisions, queues and AC OPF; cannot infer absent transformer/EVSE thermal states solely from abstract.
- **No page-/equation-level claims until PDF provided.**

## 4. Immediate 26-paper selection consequence

The existing \`PROVISIONAL_26_CORE.csv\` has 26 candidates; it is *not frozen*. **Add Gao (2017), DOI 10.1049/iet-gtd.2016.0722 to the mandatory candidate pool and replace a weak generic hazard/restoration paper in the final 26**, rather than expanding core beyond 26. Continue evaluating the remaining most-relevant P thermal physics, EVSE thermal and charging demand studies. Retain exact inclusion/exclusion reasons.

Each paper extraction must document \`problem; apparatus/case; physical quantities and units; input vs parameter vs observation; equations and model family; directional physical mechanisms; state and timing; experimental method; actual findings; author-stated vs reviewer-inferred limitations; verification/validation; uncertainty; model overlap; SO1/2/3 relevance\`.

## 5. Current decision, no fabricated achievement

- **Source inspection actually performed:** one full author PDF partly read; one published article substantively indexed but direct open blocked; three publisher/university abstracts/highlights read.
- **Not performed:** full-text reading of 26 studies, final screening freeze, verified 26 equation registers, equipment-specific thermal law, source-to-receiver causal propagation verification, parameter calibration, novel contribution demonstration.
- **External literature-search connector limitation:** Elicit scholarly API was attempted, but connected account denied API access under its present plan. Public primary publisher/university and author-hosted sources were used instead.
- **User/supervisor handoff:** access to closed PDFs, physical demonstrator equipment specifications, credible fleet operation/deadline, and validation observations/reference bench.
