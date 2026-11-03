# Targeted physics/field comparator literature audit v0.1 — 2026-11-03

**Thesis:** Physics-Based Mathematical Engineering of Power–Electrified Transportation Interdependencies for Resilience.
**Working branch:** user-data-qualification-2026-11-03. **Status:** SOURCE-VERIFIED TARGETED SCOPING PASS, NOT A COMPLETED SYSTEMATIC REVIEW / PRISMA FLOW / NOVELTY PROOF.
**Question:** Which studies observe or model ambient- and load-dependent transformer and EVSE thermal states, thermally constrained bidirectional P↔Tₑ electricity exchange, transition timing and electricity/mobility service effects under extreme heat?

## Primary comparators — source-and-claim grounded

| ID | Study / primary URL | Evidence directly supported | Evidence missing or limits | Thesis use |
|---|---|---|---|---|
| LIT-PT-01 | Krama et al. (2026), *Impact of extreme climatic conditions on fast EV charger performance: field experimental insights from Qatar*, DOI https://doi.org/10.1016/j.ecmx.2026.101960 ; https://elmi.hbku.edu.qa/en/publications/impact-of-extreme-climatic-conditions-on-fast-ev-charger-performa/ | Actual instrumented commercial 50 kW air-cooled DC charger; ambient 15–55 °C; rectifier temperature and offered/delivered power; charging time winter 86 min vs summer 169 min for tested SOC interval; thermal power derating; cross-session/time holdouts **as stated by publisher abstract** | No authenticated raw files acquired (data on request); charger-to-transformer map and transformer thermal observation not presented in abstract; mechanisms/thresholds need full text and raw instrument logs; not demonstrated coupled field validation | **P1 SO1 EVSE thermal derating, SO3 charging-time consequence** |
| LIT-PT-02 | Li, Chang & Lu (2026), *Field Measurement and Analysis of an Electric Bus Charging Station: A Case Study on Transformer Losses and Harmonic Impacts*, DOI https://doi.org/10.1109/PESGM58988.2026.11693150 ; bibliographic summary https://eurekamag.com/research/111/566/111566122.php | Abstract/metadata describe simultaneous electrical measurements on both sides of commercial bus charging station 2,000 kVA transformer, losses and harmonic distortions | Neither internal EVSE temperature nor transformer hot-spot/top-oil field sensing, protection reason codes, and source raw data confirmed from accessible abstract; do not treat calculated losses as measured heat | **P1 SO1 same-site electrical interface / harmonic heating pathway** |
| LIT-PT-03 | Fletcher & Khan (2025), RACE for 2030 final report, PDF https://www.racefor2030.com.au/content/uploads/Final-report-0571-FINAL-FINAL.pdf ; project https://www.racefor2030.com.au/project/taking-the-heat-out-of-electric-vehicle-charging/ | **Full report text examined**: Part 1 desktop IEC 60076-7 dynamic transformer thermal modeling with representative fast-charge profiles; hot-spot/top-oil, winding/oil time constants, variable ambient/non-EV baseline, congestion gap, temperature-aware charging strategy. Practical heat run tests inform parameter discussion. Example report table: winding time constant 4 min, oil 180 min, x=0.8, y=1.6; equipment-specific assumptions | Explicitly calls long-term instrumented **Part 2** future work: not completed in-field transformer-to-EVSE thermal validation in this Part 1 report; its 1MVA, emergency rating, and temperature limits cannot be copied to other installations without verification; harmonics omitted from the adopted IEC thermal model | **P1 SO1/SO2 dynamic physics closest comparator; source reports conditional SO3 EV throughput** |
| LIT-PT-04 | Godina et al. (2016), *Innovative impact assessment of electric vehicles charging loads on distribution transformers using real data*, DOI https://doi.org/10.1016/j.enconman.2016.04.087 | Publisher abstract: two actual transformers in São Miguel; genuine input demand profiles, equipment and EV assumptions; model estimates hot-spot and aging | **Using real input data is not equivalent to measuring transformer hot-spots**; no same-site EVSE internal temperature or observed thermally caused curtailment confirmed | **P1 precedent for calibrated/parameterized transformer thermal aging under charging** |
| LIT-PT-05 | *Controlled workplace charging of electric vehicles: The impact of rate schedules on transformer aging* (2020), DOI https://doi.org/10.1016/j.apenergy.2020.115352 | Publisher abstract: real workplace charging sessions, site-transformer **modeled** lifetime, controlled schedules and station utilization | No published proof in accessible abstract of *measured* transformer winding hot-spots or EVSE internal thermal cause; modeled transformer life differs from observed failure | **P1 physics + operational demand and charging control comparator** |
| LIT-PT-06 | Wen et al. (2025), *Robust Resilience Enhancement by EV Charging Infrastructure Planning in Coupled Power Distribution and Transportation Systems*, DOI https://doi.org/10.1109/TSG.2024.3390657 | Journal abstract: integrated P–T planning, uncertain traffic load, nested column-and-constraint generation, simulations on two coupled networks | Focus is economic/resilience planning, not evidence of temperature-driven internal EVSE transformer heat states or connected operating-site thermal experiments | **P2 SO3 mathematical optimization and coupling architecture, not thermal data validation** |
| LIT-PT-07 | Xiong et al. (2025), *A Real-Time Robust Method for Post-Disaster Load Restoration of Coordinated Power-Transportation System With Vehicle-to-Grid Response*, DOI https://doi.org/10.1109/TSG.2025.3568619 | IEEE abstract: multi-stage robust optimization with dynamic traffic assignment, 33-bus/20-road and 91-bus/35-road numerical test networks | Post-disaster V2G demand/restoration framework, not measured extreme-heat EVSE thermal derating or real same-site transformer/charger temperature field series | **P2 SO3 event, restoration and service scheduling approach, out-of-hazard analog only** |
| LIT-PT-08 | Djamali (2017), *Hundred years of experience in the dynamic thermal modelling of power transformers*, DOI https://doi.org/10.1049/iet-gtd.2016.1321 | Publisher abstract: systematic transformer dynamic thermal models and accuracy/limitations | Review of transformer component only, no verified charging-specific EVSE telemetry | **P1 mathematical physics review** |
| LIT-PT-09 | Qian, Zhou & Yuan (2015), *Impacts of high penetration level of fully electric vehicles charging loads on the thermal ageing of power transformers*, DOI https://doi.org/10.1016/j.ijepes.2014.09.040 | Publisher abstract: stochastic EV charging based on ambient, SOC, start time, charging mode, transformer thermal aging | Simulation/modeling; source excerpts do not establish measured connected EVSE thermal trajectories | **P2 stochastic transformer charging-load forcing** |
| LIT-PT-10 | Diahovchenko et al. (2022), *Mitigation of transformers' loss of life in power distribution networks with high penetration of electric vehicles*, DOI https://doi.org/10.1016/j.rineng.2022.100592 | Publisher abstract: temperature, EV charging and PQ influence on transformer aging, fuzzy-load management and mitigation analysis | No matched monitored EVSE internal temperature and same-site thermal dependency evidenced in source abstract | **P2 uncertainty and charging thermal control comparator** |

## Important standards and systematic-review methods

- IEC 60076-7:2018 authoritative issuer https://webstore.iec.ch/en/publication/34351 : applicable to mineral-oil-immersed transformers, describes load and ambient temperature effects on aging and loading. **The 2025 RACE report's parameter table is case/model-specific; do not blindly assign these values or limits to SINTEF or Slovenian machines.**
- PRISMA 2020 methodology https://www.prisma-statement.org/prisma-2020 ; Page et al. (2021), DOI https://doi.org/10.1136/bmj.n71 . Its 27 reporting items and flow chart are recommended for the **future completed systematic review**, not proof this preliminary search is complete.
- Wiley Scholar Gateway text search on 2026-11-03 returned **15 passages from 14 articles** for thermal-EV-transformer query; sources included Si et al. (2020), DOI https://doi.org/10.1155/2020/6514650 (FEM/heat transfer for transformer) and Shariff et al. (2021), DOI https://doi.org/10.1002/est2.300 (EV fast charger utility review). **A passage-level search is neither a deduplicated article study pool nor a systematic-screened evidence set.** Search-provider summaries require source verification.
- Elicit connector denied API access on 2026-11-03; do not claim Elicit systematic review run.

## Preliminary synthesis: exact unresolved causal chain

Primary sought chain, with **both** independently tested directions:
```
Site ambient heat [measured]
   + site background demand [measured]
   + dated transformer -> feeder -> bus -> EVSE -> vehicle physical mapping [documented]
   + transformer oil / winding temperature and current [measured]
   + verified transformer thermal restriction reason, timing and source effect [logs]
   -> EVSE grid-side supply / offered power changes [measured]
   -> required vs delivered charge, SOC and departure/mobility consequence [measured]
AND
   EVSE internal rectifier/heatsink/cooling thermal state [measured]
   + thermal derating cause, charger requested/allowed power, vehicle SOC confounders [logged]
   -> EVSE grid-side AC load changes [measured]
   -> same transformer current and heat state [measured]
```
**First-pass finding:** the above papers collectively cover major physical and mathematical **components**, but accessible primary-source material has **not established one study with all fields from the same instrumented installation and fully validated two-way thermal propagation plus mobility-service consequences**. This is an evidence search gap, **not yet a proven global research novelty claim**. RACE Part 2 or other later work may close portions; search ongoing literature and field data.

## Scope-correct review protocol (pre-registration draft, not executed PRISMA)

**Study population:** operating distribution transformers, EV charging stations, chargers, road EV fleets. Include laboratory thermal calibration only in a clearly tagged component-physics stratum; exclude from genuine field mechanism proof.

**Phenomena:** transformer top-oil/hot-spot/inertia and rating/aging, EVSE rectifier/heatsink/coolant/battery thermal states, ambient  heat/heat waves, bidirectional power demand, restrictions, thermal derating, dynamic scheduling and service effects.

**Search databases (to be executed with exact exported query/date/count):** Scopus, Web of Science, IEEE Xplore, ScienceDirect, Wiley, Engineering Village/Compendex, institutional repositories, Crossref/OpenAlex and bibliographic citation chaining. The current targeted web/Wiley searches do **not** establish complete database coverage.

**Search blocks** (platform syntax to be adapted and frozen):
1. `("distribution transformer" OR "power transformer") AND ("electric vehicle charging" OR EVSE OR "fast charging") AND ("thermal" OR "hot spot" OR "top oil" OR "dynamic rating")`
2. `("fast charger" OR EVSE OR "rectifier") AND ("ambient temperature" OR "extreme heat" OR "thermal derating" OR "cooling") AND ("field" OR "experiment" OR "measurements")`
3. `("electric bus" OR "charging station") AND (transformer OR feeder) AND ("field measurements" OR "operational" OR "site")`
4. `("power-transportation" OR "power transportation") AND ("resilience" OR "coupling") AND ("time" OR "service" OR "thermal")`
5. Citation followup from RACE report, Krama 2026, Li et al 2026, transformer standards and dynamic thermal reviews.

**Two-axis screening (explicit):**
- Topic relevance: physics/mechanism, mathematics, dynamic state-time, service, extreme heat.
- Evidence category: F1 measured same installation connected thermal + electrical + service; F2 measured same installation but partial thermal/electrical; F3 measured separate operational component; F4 controlled lab experiment; F5 analytical/numerical/optimization; F6 review/standard. A paper with real inputs and a simulated hot-spot cannot be promoted to F1.

**Extraction per study:** title, DOI, year, original PDF/full-text access, engineering asset ID, weather/regime, equipment class/cooling, P bus/EVSE connection, variable/sensor locations/units/time resolution, measured-vs-derived flags, actual raw data access and checksum, governing equations with page/equation numbers, parameter origin and identifiability, restrictions/reason codes, electrical meter boundary, charging SOC/request/derating, service requirements/delivered, errors/holdouts/UQ, observed P→Tₑ and Tₑ→P directional effects, exact explicit study limitations and future-work claims.

**Critical appraisal:** topology proof; direct rather than estimated thermal sensors; separation of ambient vs loading as causes; logged thermal reason vs generic taper; train-test leakage; distinct hardware validation; boundary and units; high-heat generalization; source-to-figure/eq traceability; no joint-field claim from multiple unrelated sites.

**Audit outputs pending:** frozen search log, RIS/CSV deduplicated citations, title/abstract screening with exclusion reasons, primary full-text PDF page/figure/equation table, PRISMA flow denominators (only once actual search complete), risk-of-bias scores, source-to-objective transfer matrix, evidence-backed novelty-gap statement and instrumented minimum field dataset contract.

## Immediate thesis order
1. **Read RACE report fully** with equation/page extraction and distinguish 2025 Part 1 vs any verified subsequent Part 2 results.
2. **Acquire Krama paper full-text and request deidentified field CSV**; verify observed heat-limited charger behavior, instrument specifications and whether transformer side data exist.
3. **Obtain Li/Chang/Lu 2026 full text and accessible source data**: confirm actual bus-transformer connection, primary/secondary sampling, power loss vs measured winding temperature, source data availability.
4. **Compare Godina/Applied Energy and IEC 60076-7**: recreate controlled charging-load forcing and temperature-constraint math from exact equations, not from secondary abstract paraphrase.
5. **Only then** claim a narrowed novelty boundary. Independent field data for SO1–SO3 and component VVUQ remain separate gates.

**No frozen thesis governance documents were edited by this audit.**

## Full-text comparator extraction addendum — Fletcher & Khan (2025)

**Source:** RACE for 2030 final report (2025); `https://www.racefor2030.com.au/content/uploads/Final-report-0571-FINAL-FINAL.pdf`. Numbers below are **report's simulations**, NOT observed field performance.

| Source print page | Setup / observation | Exact modeled result | Evidence boundary |
|---|---|---|---|
| p. 10–11 | IEC 60076-7 transformer oil/winding thermal model, 1 MVA target, charging profiles from 23 EVs; time granularity less than a minute | Parameter example: winding time constant **4 min**, oil **180 min**, model exponents x=0.8, y=1.6; rated top-oil rise 55°C, hot-spot gradient 23°C | Selected model assumptions, not identified from our SINTEF original |
| p. 16, Table 4 | Background non-EV load 0.75 p.u.; charging interval gaps 5 min; different ambient scenarios | Ambient **15–25°C** -> maximum simulated hot-spot **89.8°C**, top-oil **68.1°C**, equivalent aging **0.19**; **35–45°C** -> maximum simulated hot-spot **109.8°C**, top-oil **88°C**, equivalent aging **1.88** | Modeled 1MVA transformer's exposure response; not field-validated extreme-heat effect |
| p. 25, control section | Four-level hot-spot hysteresis power control, 25% power decrements; thresholds given as 100, 103, 107, 110°C | Over 10 simulated hours with 23 EVs, requested **1364 kWh**, delivered **1262 kWh** (~92.5%); authors round to 92% | Thresholds are study-specific engineering examples, NOT universal limits; simulated shortfall is charging energy, not proven missed mobility journeys |
| p. 3–4, executive summary | Study design | **Part 1** desktop simulations supported by heat-run test considerations; two installed fiber-optic instrumented transformers named as proposed **Part 2** long-term field assessment | This publication alone does NOT establish completed in-field P–EVSE thermal coupling |

**Immediate mathematical transfer:** thermal time constants, peak duration and inter-session gap must be tested explicitly, not collapsed into static rated MVA. Use source-specific heat balance equations and identify sensor/rating/vehicle acceptance. Hysteresis-limited delivered energy is an admissible simulated service **proxy** when required energy is defined; actual mobility resilience requires departure/trip outcomes. No claim of a single measured two-way thermal field system.

**Full-text verification note:** Retrieved text from original PDF; web screenshot rendering endpoint returned a fetch/cache error, so the embedded PDF figures themselves were not visually independently audited. Page labels above follow PDF printed pagination.
