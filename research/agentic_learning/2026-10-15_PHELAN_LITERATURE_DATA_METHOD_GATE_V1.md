# Phelan feedback: literature, data, and model-selection gate (15 October 2026)

**Document status:** NON-CANONICAL / PRELIMINARY EVIDENCE TRIAGE / NOT A COMPLETED SYSTEMATIC REVIEW  
**Reason:** P. Phelan asks (i) what has been done and whether the literature has been reviewed thoroughly; (ii) whether experimental data justify physics-informed neural networks or other physics-informed learning; use physics-only if not.  
**Branch:** `research/agentic-learning-heat-pt-20261015` (not main).  
**Governing rules:** `project/AUTONOMOUS_EXECUTION_PROTOCOL_V1.md`; no frozen thesis edits, no renumbering H1–H5, no Austin/flood case replacement.  
**Research question in this exploratory branch:** conditional extreme-heat electrothermal Power–Electrified Transportation mechanisms. Distinct from frozen Austin/Flood confirmatory pathway.

## 1. What the thesis already reviewed
The existing repository `thesis/02_literature_theory/02_00c_accepted_core_evidence.md` has ~30 **accepted, bounded core entries** including Maier, Rinaldi, Kivelä, Ouyang, Fotouhi, Zou & Chen, Wang, Li, V2Sim, Bruneau, Doyen/De Lara, Vinod/Oishi, and sustainability/recovery literature. 'Accepted' applies only to bounded statements; it is **not** a complete global literature review or validation.  
The existing `02_00d_deeper_research_and_reading_queue.md` already flags P0 uncertainties: exact hybrid P–T formulation; full P→T→P recovery feedback; direct joint state estimation/observability; P–T organizational evidence; direct infrastructure viability and reachability, and more. New advisor feedback calls for a **heat/thermal/PIML/data** focused supplement, not erasing prior work.

## 2. Preliminary heat + coupled-systems precedent matrix — PRIMARY SOURCE METADATA/PUBLISHED TEXT VERIFIED AS AVAILABLE

| Domain | Paper | Supported statement | What it does NOT establish |
|---|---|---|---|
| Interdependencies | Rinaldi et al., 2001, DOI 10.1109/37.969131 | conceptual classification of cross-infrastructure dependency | dynamic electrothermal causal law |
| Coupled P–T resilience | Fotouhi et al., 2017, DOI 10.1016/j.ress.2017.01.026 | linked traffic/electric models and resilience strategies | thermal P–EV battery state identification |
| Coupled P–T optimization | Wen et al., publication IEEE TSG 2025, DOI 10.1109/TSG.2024.3390657 | robust charging-infrastructure planning and disruption response; published online Apr 2024 | direct evidence of realistic coupled heatwave dynamics |
| Temperature-grid safety | Guddanti et al. 2025, DOI 10.1038/s41467-025-59749-4 | climate-temperature impact on distribution-grid vulnerability/safe-operation analysis | coupled PT viability proof |
| Co-simulation | Balogun et al., EV-EcoSim, arXiv 2401.04705, DOI 10.1109/TSG.2023.3339374 | EVSE+distribution+thermal transformer modeling, controls; battery internal temperature excluded (controlled 23°C) | heat-dependent battery internal state validated |
| Field experimental thermal grey box | Blomgren et al., 2023, DOI 10.1016/j.segan.2023.101048 | 2 actual Danish LV distribution transformers; load/weather/thermometry; grey-box stochastic real-time/6h thermal forecast | **data cannot be shared by authors**; not a user-accessible train/validation set |
| Transformer PINN | Tang et al., 2024, DOI 10.1049/hve2.12435 | PINN transformer spatial temperature fields trained/tested against primarily COMSOL reference results, compared with DNN | cannot be treated as field-confirmed coupled PT model; paper notes soft constraints can be violated |
| Electrothermal battery field tests | Mannapperuma et al., 2025, DOI 10.3390/batteries11090319 | electrothermal EV battery pack identification using CAN/dynamometer/real-world driving tests | public release of their raw data NOT verified here |
| Hybrid electrothermal battery lab | Liu et al. 2025, DOI 10.1016/j.apenergy.2025.125633 | experiments on 8 Ah battery over 0–40°C for hybrid physical/data thermal model | not validation of full road + electric distribution system |

**Evidence note:** Precedent exists in every individual domain, including physics-informed neural networks. New-method novelty requires a qualified cross-domain search, prior-method reproduction, scope-matched validation, and explicit evidence; 'we will use PINNs' is not novel by itself.

## 3. Public candidate data: availability is not joined-system observability

| Source / exact URL | Source-reported measurable channels | Access at triage | Strength | Missing before integrated PT inference |
|---|---|---|---|---|
| Caltech ACN-Data `https://ev.caltech.edu/dataset` | plug/connect times; delivered kWh; pilot signal; measured charging current timeseries | registration/token for live API; site offers download | high for charger operating behavior | battery temperature, actual vehicle trips, grid bus status, feeder transformer temperature |
| ACN-Data static `https://github.com/tongxin-li/ACN-Data-Static` | 2018–2020 three-site 85,877 compressed session timeseries files; current, pilot, voltage, power, energy, charge state | repository README read; **raw rows not ingested** | high for EVSE current/power validation | user trip realizations, transformer topology, site heat exposure; empty session JSON path means do NOT expect complete session metadata from it |
| NASA PCoE `https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/` | battery cycling and temperature-dependent laboratory conditions, including 40°C/high-temp randomized duty tests | public zip links listed; raw content not yet inspected | high for **battery component** identification | pack scale, EV charging/site, grid bus, road service |
| NOAA Global Hourly `https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database` | measured temperature, wind etc. | public access catalog, station matching not yet executed | strong external heat forcing at nearest admissible station | local charging-station microclimate, transformer enclosure conditions, correct station/site/date alignment |
| Blomgren et al. Danish LV transformers `https://doi.org/10.1016/j.segan.2023.101048` | 1-second field current/temp (aggregated), site weather, transformer characteristics Nov 2021–Jun 2022 | **BLOCKED_EXTERNAL_ACCESS: 'authors do not have permission to share data'** | strong prior empirical evidence *in paper*, not trainable open dataset | raw sensor data, EVSE-to-transformer linking, transport service |
| Mannapperuma et al. EV CAN pack experiment `https://doi.org/10.3390/batteries11090319` | CAN/dynamometer/driving electrothermal response | publicly visible paper; raw dataset not yet verified | direct EV pack real-world evidence | raw access + joint transformer grid/road data |
| Existing SMART-DS Austin P5U and TxDOT 2018 in canonical thesis | benchmark synthetic grid and 2018 roadway structural sources | existing separate case qualification OPEN; joint data unresolved | topology/synthetic experiments under existing approval | **SMART-DS is synthetic, not experimental observation**; observational heat-linked P–EV–T data not established |

### Sufficient-data decision gate (proposed; do not prematurely classify as passed)
**D1 identity/legal:** inspect source files, permission, dates and licensing.  
**D2 measurement:** confirm actual observed inputs and response channels, sensor calibration, sample counts/time resolution, missingness, outliers.  
**D3 correspondence:** know feeder→transformer→EVSE mapping plus road/EV trip or charging service mapping. Geographic co-location alone is not P→T/T→P causal proof.  
**D4 heat:** station and timestamps align; exposure support and propagation delays defensible; proper distinction ambient air vs component internal temperature.  
**D5 information:** practical identifiability/observability of the parameters and dynamic interface states; enough independent excitation of loading & heat.  
**D6 testing:** chronological/site/heatwave held-out split, nested model baselines, negative controls, parameter and measurement uncertainty, field validation, data leakage checks.  
**D7 scope:** match claims to measured outputs; EV charger measurements alone justify EVSE predictions **not actual mobility service trajectories**.  

If only EVSE time series and NOAA temperatures pass, calibrate **charger-level** response without asserting battery-temp dynamics or a joint grid-traffic PINN. If battery lab experiments pass, calibrate the battery component only. Full cross-sector PINN requires joint observations or independently validated interfaces with propagated uncertainty.

## 4. Formal model selection

Baseline physics DAE/ODE and service maps: `F_phys(X,u,h;theta)=0`; heat balance, AC/DC charging boundary, transport demand/network conservation as warranted by the scope. Start with verified physical operating constraints before ML.

**A. Data insufficient for the desired target:** audited pure physics, sensitivity bounds, synthetic/matched test experiments and transparent uncertainty. No empirical forecast-skill claim.

**B. Moderate data, physically interpretable structure:** system identification / stochastic grey-box model as **first empirical comparator**. Stochastic errors represent unresolved forcing/model discrepancy, with held-out performance.

**C. Sufficient physically informative spatiotemporal data:** physics-informed residual learner or PINN, with transparent residual:
`L = lambda_data L_obs + lambda_phys L_phys + lambda_IC L_IC + lambda_BC L_BC + lambda_constraints L_constraints`.
Weights chosen on proper validation splits; *soft penalty never implies hard physical feasibility*. Compare against physics-only, grey-box and unconstrained ML on same samples, uncertainty and computational budget.

**Important:** A PINN can mathematically approximate a PDE solution using collocation even absent empirical data, but **it would not provide the experimental-learning/validation benefit** intended by Phelan. Do not confuse synthetic labels and experimental measurements.

## 5. Pre-registered systematic/reproducible-review protocol to execute next

**Review question:** For extreme-heat power, electrified transportation and explicit interfaces, which physical, statistical, ML and PINN/physics-informed methods have been developed, and with which *measured* data, assumptions, uncertainty and validated service outcomes?

**Sources to query:** IEEE Xplore, Scopus, Web of Science, Compendex, ScienceDirect, SpringerLink, Wiley, Google Scholar/Crossref for citation snowballing; arXiv tracked separately with published version deduplication. **Authenticated databases are NOT executed in this triage; public web only.**  
**Search blocks (Boolean examples; translate syntax separately per database):**
1. `("power distribution" OR "power grid" OR transformer) AND (transportation OR "electric vehicle" OR EVSE OR charger) AND ("extreme heat" OR heatwave OR thermal OR temperature) AND (coupling OR interdependen* OR co-simulation)`.
2. `(battery OR transformer OR "charging station") AND ("physics-informed neural network" OR PINN OR "grey-box" OR "hybrid physics") AND (experimental OR field OR measurement OR validation)`.
3. `("coupled power transportation" OR "traffic power network") AND (heat OR temperature OR thermal) AND (resilience OR reliability OR service OR recovery)`.
4. `("electrothermal" OR "thermal derating") AND (traffic OR charger OR mobility) AND (dataset OR observation OR measurement)`.
5. `("viability kernel" OR reachability) AND (electrical OR transport OR infrastructure) AND (uncertainty OR control)`.

**Eligibility:** English peer-reviewed primary studies + formal standards; explicit equations/mechanism; P–T direct or heat/battery/transformer adjacent evidence; source/model type, year, version, settings, data provenance tracked. Exclude purely generic citation chains or physics-transfer claims without justified mapping. Record all screened titles (not just selected), database/queries/date, duplicate handling, full-text decisions, access limitations and backwards/forwards citations.

**Extraction sheet columns:** DOI | verified bibliographic identity | direct-PT/adjacent | climate setting | physical objects | interface source→target | exact equations/units | thermal regime | timescales | data (measured/synthetic/benchmark) | sample size | sensors | temporal/spatial correspondence | calibration/heldout | sensitivity | UQ | online latency | comparator/baseline | claim supported | not supported | evidence gate | thesis RQ/SO.

**Review completion gate:** full reproducible search log, duplicate/risk-of-bias screening, included/excluded reasons, citation graph, equation-level FTEE on priority papers, contradictory literature, documented unresolved paywalls, and advisor review where required. **CURRENT: NOT PASSED.**

## 6. Immediate decisions for advisor response

- A Chapter-2 literature foundation exists and is already curated, but a **thorough focused review of extreme-heat coupled electrothermal/transport physics + PINNs/data remains incomplete**.
- Actual experimental evidence exists in charger, battery and transformer subdomains; an open, aligned, observable dataset validating all cross-sector interfaces has NOT been established.
- A field-data experimental PINN should remain conditional, with simple grey-box/system ID considered first where data are sparse.
- Keep physics-based modeling as the unconditional fallback; never assert PINN superiority or scientific novelty without matched held-out validation.
- Do not replace Austin/flood case or canonical H1–H5 with this exploratory heat-specific pathway without explicit scope governance.
