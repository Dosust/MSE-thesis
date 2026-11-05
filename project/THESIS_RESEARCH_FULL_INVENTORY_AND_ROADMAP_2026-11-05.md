# Thesis Research — Complete Work Inventory and Scientific Roadmap

**Audit date:** 2026-11-05. **Scope:** Physical thermal Power–Electrified Transportation interdependencies under extreme heat (frozen SO1–SO3).
**Audited evidence:** local version-5 workbook; original screening protocol, 17-study reconciliation, 13-source audit, 98-study queue, 44-task register, original Q0 exports, source data and analysis ZIPs; GitHub working-branch master status.
**Important:** Inventory statistics reflect **records, files, metadata and source-access levels**, not final systematic inclusions, independent studies, accepted scientific findings, or supervisor approval.

## A. Executed and verified — bibliographic and review work

- Q0 original workbook: 687 provenance rows (Scopus 253, IEEE 189, Compendex 245), 404 deduplicated historical master records; historical 200→26 prioritization run remains preserved.
- Master V5: 590 provisional source rows; 555 populated and unique DOI strings; 35 blank DOI fields (not all expected to possess a DOI); **study-family/title-level duplicates remain to check**.
- Relevance classification: 76 CORE_CANDIDATE, 73 SUPPORTING_CANDIDATE, 27 HISTORICAL_BACKGROUND, 233 UNRESOLVED_RELEVANCE and 181 UNRESOLVED_OR_OUT_OF_SCOPE. These are not eligibility decisions.
- Internal JBI-PCC-derived scope/screening protocol dated Nov 3, 2026; **not externally preregistered or supervisor approved**.
- Single AI-rule-assisted title/abstract pass across 590: 98 ADVANCE_FULLTEXT, 126 SECONDARY_BACKGROUND, 259 EXCLUDE_TA_PROVISIONAL, 107 UNCERTAIN_TA. **All 590 full-text decisions remain NOT_SCREENED in control sheet; zero PRISMA-countable**.
- 149 pre-prioritized references (76+73) are a workflow queue, **not** an eligibility or included-study count.
- 98 in full-text retrieval queue. 13 source-audit records: 6 primary publisher method/result section checks, 2 partial original report-text checks, 4 abstract-only, 1 secondary-summary-only. The other 85 were not assessed in the Stage-4 source pass, without assuming they are globally unavailable.
- 39 high-risk screening challenges identified among E/U (16 provisional exclusions + 23 uncertain). 25-study pilot QA sample exists, **no independent reviewer has adjudicated it**. Under protocol, all 366 E/U require human review.
- 17 candidate follow-ups reconciled as **already** present, IDs LIT-0574 to LIT-0590. Ten had DOI strings; seven earlier blanks were completed; no new study IDs added, and two year corrections recorded.
- 11 claim/equation evidence notes retained; 8 candidate gaps; no finalized universal novelty claim.
- GitHub working branch still exposes the earlier **533-record** master. Local 590-record V5 and post-V3 screening materials should **not be described as synced to GitHub** until the actual branch commits are verified.

## B. Reproducible original-data inventory

- **SINTEF transformer**: `Barug2025_sensordata(2).csv` was opened in this audit; 8,592 measured hourly rows, voltage/current, ambient, oil and winding temperature channels. Report-01 source attributes ambient range -19.58 to +25.97 °C; not measured extreme heat.
- **STREAM Slovenia P/Q**: source CSVs opened; 34,932 rows each and 12 TR stations (419,184 station-time P/Q pairs); original units, signed-power conventions, rated assets and physical EVSE topology unresolved.
- **KU Leuven**: original charging archive available; prior AC/DC measurements and battery sensor fields summarized in RQ4–RQ5. Clock reversals and metering boundaries remain unresolved.
- **OSF PQ**: archive available and ZIP integrity passed; prior original experiment-level analyses are exploratory, not same-site transformer–EVSE thermal measurements.
- **TUM**: original seven-vehicle field dataset reported in project record, but original local Parquet files are **not among the audited files mounted here**. Sentinel/decoded-temperature and charging synchronization remain open; do not claim all seven original files were reverified now.
- **RACE, Qatar Krama, connected bus-station Li, Ryklief OCPP**: promising published evidence, but site-specific raw observations, exact thermal-channel coverage, or fully linked service measures remain partial or unavailable.
- **No verified, instrumented, time-synchronized connected transformer–EVSE thermal field installation is demonstrated by the current inventory.**
- Original RQ1–RQ11 Python/result research archive contains 20 entries and passed ZIP integrity. Original stage-1 analysis archive also passed. This audits archive integrity; it **does not prove independent numerical re-execution**.

## C. Mathematical results and remaining qualification

- RQ1: measured associations of transformer temperatures to ambient/load; confounding remains.
- RQ2: SINTEF same-transformer 1h conditional test RMSE 0.21468°C versus persistence 0.24797°C; model 1h MAE 0.14692°C worse than persistence 0.14094°C. 6h/24h tests used observed future forcing (conditional hindcasts; not operational forecasts).
- RQ3: measured P/Q description; ratings/units/topology open.
- RQ4–5: laboratory EV/charge input-output analysis; clock/sensor boundaries and loss-vs-heat attribution open.
- RQ6: no finished leakage-safe original matched site benchmark; status record contains an OPSD benchmark note that must be reconciled with the RQ6 NOT_COMPLETED interpretation.
- RQ7: power-quality experiment comparisons exploratory; not causal thermal interface validation.
- RQ8–9: effective one-step transformer coefficients and bootstrap sensitivity estimated, **physical** loss/cooling/capacity parameters not uniquely identified.
- RQ10: chronological same-transformer holdout done; independent equipment and extreme-heat external validation absent.
- RQ11: viability/service mathematical formulation only, no verified end-to-end service transition/recovery tests.
- SO1: physical interface candidates and component measurements; no complete demonstrated directional thermally caused connected interface.
- SO2: component dynamics and a candidate coupling model; no independently calibrated validated full thermal state-time coupling.
- SO3: service equations/metrics and prior-art simulations; no field-observed dynamic transition/propagation and actual mobility-service deficits under the coupled heat mechanism.
- **Modeling decision:** provisional physics-first ODE/DAE/PDE baseline; no completed fair PINN-versus-physics matched benchmark.

## D. Active review gate audit

| Gate | Recorded evidence/status | Outstanding acceptance condition |
|---|---|---|
| G1 — Scope and eligibility | INTERNAL LOCK ONLY | PCC eligibility and source types fixed in Locked Screening Protocol V1.0, awaiting independent reviewer and supervisor review |
| G2 — Database search provenance | NOT EXECUTED FOR V2 | Native search A–F on accessible databases; dates, queries, filters and raw exports |
| G3 — Source normalization | FIRST-PASS COMPLETE | Reconcile 533 existing + 50 DOI candidates + 7 no-DOI leads; study-family and metadata checks |
| G4 — Abstract eligibility | 590 PRELIMINARY TA DECISIONS | 149 priority plus 441 broader records screened by a single rule-assisted pass; human QA and original export completeness open |
| G5 — Full-text eligibility | NOT STARTED | Locate and assess eligible complete papers; record specific exclusion reasons |
| G6 — Primary scientific extraction | PARTIAL | Reuse historical P01–P14 and 11 claim records; verify primary equations and observations |
| G7 — Synthesis and gap falsification | PRELIMINARY | Compare close predecessors; cite contradictory evidence and evidence limits |
| G8 — Physics vs PINN benchmarking | MODEL CHOICE PROVISIONAL | Physics baseline + qualification of temperature measurements and holdouts |
| G9 — PRISMA flow | NOT AVAILABLE | Calculate only from reconciled formal screen counts after G1–G5 |

## E. All 44 recorded tasks — exact register status

**These are original recorded task statuses from the workbook:** 20 PARTIAL and 24 NOT_STARTED; none marked COMPLETE. Several post-checkpoint artifacts (screening and source audits) were not back-propagated to this official task register, so the register is stale, not proof that no later work happened.

| Task | WP | Priority | Original status | Research activity |
|---|---|---|---|---|
| T01 | WP1 | P0 | PARTIAL | Finalize review objectives and LQ1–LQ6 versus SO1–SO3 |
| T02 | WP1 | P0 | PARTIAL | Lock inclusion/exclusion, F1–F7, amendments and reviewer process |
| T03 | WP1 | P0 | PARTIAL | Define reference IDs, exports, hashes, document rights and file convention |
| T04 | WP1 | P0 | PARTIAL | Translate concepts to database-specific search syntax |
| T05 | WP2 | P0 | NOT_STARTED | Run block A transformer heat plus EV charging searches |
| T06 | WP2 | P0 | NOT_STARTED | Run blocks B EVSE heat and C connected-site evidence searches |
| T07 | WP2 | P0 | NOT_STARTED | Run blocks D coupled dynamics and E PINNs / PIML searches |
| T08 | WP2 | P0 | NOT_STARTED | Run block F standards / numerical methods and supplementary indexes |
| T09 | WP2 | P0 | NOT_STARTED | Citation chasing and recall check against established source seeds |
| T10 | WP3 | P0 | PARTIAL | Merge actual exports and preserve provenance, DOI/title/year |
| T11 | WP3 | P0 | PARTIAL | Deduplicate without merging distinct studies and report versions |
| T12 | WP3 | P0 | NOT_STARTED | Perform complete locked-eligibility title/abstract screening |
| T13 | WP3 | P0 | NOT_STARTED | Retrieve and assess full text and record exclusion reasons |
| T14 | WP4 | P0 | PARTIAL | Bragone transformer PINN source equations and measured inputs |
| T15 | WP4 | P0 | NOT_STARTED | RACE 2025 IEC thermal and EV energy equations audit |
| T16 | WP4 | P0 | NOT_STARTED | Krama Qatar thermal derating primary source and confounders |
| T17 | WP4 | P0 | NOT_STARTED | Li bus charging site transformer metering/topology audit |
| T18 | WP4 | P0 | NOT_STARTED | Cao EV thermal neural Transformer original physical loss audit |
| T19 | WP4 | P1 | PARTIAL | Extract additional priority primary equations with page and validation tags |
| T20 | WP5 | P1 | PARTIAL | Build F1–F7 directional interface evidence map |
| T21 | WP5 | P1 | PARTIAL | Compare physical states, delays, thermal limits and service onset |
| T22 | WP5 | P1 | PARTIAL | Search strongest contrary prior art for proposed novelty claims |
| T23 | WP5 | P1 | PARTIAL | Draft bounded literature findings and unresolved evidence |
| T24 | WP6 | P0 | PARTIAL | Consolidate original measurements, source hashes and permissions |
| T25 | WP6 | P0 | PARTIAL | Audit SINTEF thermometer, load, ambient and chronological testing |
| T26 | WP6 | P0 | NOT_STARTED | TUM seven-file SHA256, sentinel decoding, charging/temperature alignment |
| T27 | WP6 | P0 | NOT_STARTED | Seek Qatar EVSE and Li connected-site raw measurements |
| T28 | WP6 | P1 | PARTIAL | Qualify Slovenia, Leuven, OPSD and OSF units/clocks/boundaries |
| T29 | WP6 | P1 | PARTIAL | Map measured variables to states, parameters and heat conditions |
| T30 | WP7 | P1 | NOT_STARTED | Derive dimensional transformer conservation equations and boundaries |
| T31 | WP7 | P1 | NOT_STARTED | Identify physically estimable thermal coefficients and uncertainty |
| T32 | WP7 | P1 | NOT_STARTED | Run leakage-safe temporal and external-asset validation |
| T33 | WP7 | P1 | NOT_STARTED | Quantify UQ, sensitivity, physical residuals and operating range |
| T34 | WP7 | P1 | PARTIAL | Evaluate PINN/PIML eligibility from measurement/holdout quality |
| T35 | WP7 | P2 | NOT_STARTED | Conditional implementation of physically constrained learning benchmark |
| T36 | WP7 | P2 | NOT_STARTED | Conditional matched pure-physics, persistence, gray-box and PINN test |
| T37 | WP7 | P1 | PARTIAL | Record defensible physics-only or physics-informed method decision |
| T38 | WP8 | P1 | PARTIAL | Draft Chapter 2 evidence review and mathematics |
| T39 | WP8 | P1 | PARTIAL | Prepare source-backed Professor Phelan research briefing |
| T40 | WP8 | P1 | NOT_STARTED | Independent bibliographic, mathematics and reproducibility QA |
| T41 | WP8 | P1 | NOT_STARTED | Obtain and incorporate documented supervisor comments |
| T42 | THESIS-DOWNSTREAM | P3 | NOT_STARTED | Identify physically connected transformer–EVSE thermal site |
| T43 | THESIS-DOWNSTREAM | P3 | NOT_STARTED | Compare genuine uncoupled/static/dynamic connected thermal model |
| T44 | THESIS-DOWNSTREAM | P3 | NOT_STARTED | Demonstrate criticality, service viability and recovery with uncertainty |

## F. Dataset and lead inventory (23 recorded records)

| ID | Evidence source or dataset | Acquisition/QA status | Remaining limitation |
|---|---|---|---|
| D01 | SINTEF transformer | ACQUIRED_QA_PROVISIONAL | Independent transformer thermal model UQ and hot-weather transfer |
| D02 | KU Leuven BEV charging | ACQUIRED_MODEL_BLOCKED | Fix CAN thermal semantics DC sensor observability and holdout |
| D03 | EPFL level-3 charging | ACQUIRED_ELECTRICAL_PROVISIONAL | Reconcile 64277 vs 61816 minutes AC DC power boundary |
| D04 | OPSD household EV grid | 116355_INTERVALS_ELECTRICAL_BENCHMARK_DONE | Meter timing PV other loads actual feeder connection |
| D05 | Iowa 296-node smart meter | ACQUIRED_AUDITED | Download actual OpenDSS and verify asset mapping |
| D06 | OSF 94GKC EV PQ | ACQUIRED_AUDITED | Sparse temp 0.57% DAQ validation and schema reconciliation |
| D07 | DOE ORNL original file audit | 4_MD5_VERIFIED_FILES_22_LINK_LEADS | Original ORNL charging 35 files and full TU Dortmund waveforms |
| D08 | FCP ChargePoint sessions | NEW_PRELIMINARY_ONLY | Provenance privacy licensing session electrical QA |
| D09 | FCP SG temperature price Stanford PV | NEW_PRELIMINARY_ONLY | Verify geography timezone units; never co-locate |
| D10 | SPS Cyprus LV network | SOURCE_INSPECTED_NO_POWERFLOW | Run verified power flow |
| D11 | SPS PyEPlan five-bus | SOURCE_INSPECTED | Resolve P Q identity time/unit meaning |
| D12 | Battery 500-row events | QUARANTINE | Obtain original measurements and instrument metadata |
| D13 | EV routing archive | QUARANTINE_AUDIT_COMPLETE | Original origin and conditional energy semantics |
| D14 | French EVSE station one row | NOT_FOR_MODEL | Do not publish original contact data |
| D15 | Kaggle grid transport resilience 5000 | NOT_PHYSICALLY_VALIDATED | Underlying simulator protocol if reuse |
| D16 | Virtual P Te thermal coupling V1 | 36_RUNS_NUMERICALLY_CHECKED | Physical parameters connected field validation |
| L01 | KIT Campus North | RAW_NOT_ACQUIRED | Topology measurement ID and thermal sensor mapping |
| L02 | Electric-bus station transformer | RAW_NOT_ACQUIRED | Raw simultaneous power transformer temperatures |
| L03 | Qatar charger thermal derating | RAW_ON_REQUEST | Raw temperatures derating and transformer physical path |
| D17 | KU Leuven C5PT0R EV charge efficiency | ACQUIRED_CHECKSUM_VERIFIED_QA_PARTIAL | 4 AC CSVs: 40873 samples; 3 not monotonic; DC2 current/voltage mislabeled suspicion; meter boundaries, test conditions and overlap with D02 must be verified |
| D18 | Najafi transformer thermal images V3 | ACQUIRED_IMAGES_CHECKED_AUXILIARY_ONLY | 255 320x240 RGB BMP + 45 expert ground-truth masks; 23C constant ambient, 1 kW single-phase; no timestamps/oil/hotspot readings; no P-Te linkage |
| D19 | STREAM Slovenia 2025 transformer P/Q | TWO_ORIGINAL_CSV_MD5_VERIFIED_34932_ROWS_12_STATIONS | 15-minute P/Q observations; power units, sign and nameplate companion need verification; no shared EVSE temperature or feeder topology |
| D20 | TUM real-world seven EV UDS thermal logs | USER_LOCAL_7_PARQUET_ACQUIRED_ID1_40401700_ROWS_QA_PENDING | Source local on user Mac; 1023-degree-like thermal codes, sensor semantics, charging overlap, file SHA256 and cross-vehicle QA unresolved |

## G. Ordered next actions and evidence gates

1. **Repository sync & control:** create an immutable V5 manifest/checksums; reconcile original branch master (533 rows) with V5 (590 rows), screening and later audits. Preserve source IDs, DOI/title-year versions, and reviewer history. Fix stale `START HERE` V2 label and maturity/claim links. Pass when exactly one canonical version has bidirectional source provenance.
2. **Protocol and complete searches:** obtain supervisor/reviewer confirmation of PCC scope and review-type; run database-native A–F queries on accessible platforms and record verbatim syntax, dates, exports and hashes. Pass when all platforms and access restrictions are documented.
3. **Human screening QA:** independently adjudicate 259 preliminary excludes and 107 uncertain plus QA sample of advances/background; update reasons and study-family mapping, avoid AI as invented second reviewer. Pass when eligible source set and exclusions are defensible, not merely rule scores.
4. **Full-text retrieval:** original full text for 98 current advance candidates, prioritizing Bragone, Cao, Hilshey/Gong, RACE Part 1/Part 2, Qatar Krama, Li bus station, Ryklief, thermal optical-fiber studies; record actual access/page/equation/data limits. Pass when every included source has a verified study and original experimental extraction.
5. **Formal synthesis and gap falsification:** C1–C6 × SO1–SO3 matrix with competing prior art, which claims are measured vs simulated, study-family/independent experiment linkage, adverse evidence and limitations. Pass before stating novelty.
6. **Field data gates:** fix SINTEF transfer/testing limits, STREAM units/nameplates, KU Leuven & OSF time/sensor conventions, TUM Parquet original hashes/1023-code/charge alignment; seek true same-site instrumented transformer–EVSE topology, heat restriction reason and service measurements. If unavailable, bound the model claim to separate components and conditional simulations.
7. **Physics first and matched tests:** derive conservative heat balances and interface mappings; choose minimum observable states, verify units and limits, identify only estimable coefficients; compare persistence, static/uncoupled/dynamic/coupled, appropriate gray-box and PINN if experimental admissibility passes, on identical holdouts and VVUQ.
8. **SO3 and deliverables:** service thresholds, critical times, propagation/recovery, missed-trip evidence qualification; final verified PRISMA-ScR flow if criteria met, full literature chapter, advisor briefing, research writeup and reproducible scripts.

## H. Scientific integrity and report boundaries

- `590` counts working bibliographic rows; it is **not** 590 formally eligible papers or independent experimental studies.
- `555` counts filled unique DOI strings; it is **not** 555 independently publisher-verified DOIs or unique study families.
- `98` is preliminary rule-assisted advancement; **not** 98 formally included full texts.
- `13` is mixed-depth source auditing; **not** 13 verified whole-paper extractions or replications.
- `17` is an additional November-4 metadata/primary-source audit, **not 17 extra publications**.
- No final PRISMA counts, externally certified novelty, independent coupled field validation or PINN superiority are supported.

**Authoritative working files:** `Unified_Thesis_Research_Master_V5_Reconciled_2026-11-04.xlsx`; `Thesis_Systematic_Screening_Protocol_V1_2026-11-03.md`; `Thesis_Fulltext_Eligibility_and_Novelty_Audit_2026-11-03.md`; `Thesis_17_Paper_Reconciliation_2026-11-04.csv`.
**GitHub snapshot caveat:** The branch `user-data-qualification-2026-11-03` was checked on November 5 and still exposes the 533-row master literature register, not the V5 local file.