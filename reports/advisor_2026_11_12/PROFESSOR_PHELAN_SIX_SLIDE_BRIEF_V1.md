# Professor Phelan: six-slide thesis evidence briefing

**As of:** 2026-11-12. **Status:** advisor-facing draft. **Target share:** 2026-11-13 evening / 2026-11-14 morning. **Feedback requested:** Monday 2026-11-16.

**Active thesis:** Engineering of Power–Electrified Transportation Interdependencies for Resilience. Current frozen research goal is extreme-heat **thermal** P-T_e interaction, physical state and time, consequences to electricity/mobility service. Frozen objectives: SO1 qualify, SO2 physics-based model, SO3 quantify transition/propagation/service consequences.

## Slide 1. What has Professor Phelan asked?
Literature first; compare governing physics, observations and validation. Consider physics-informed ML only if experimental data are informative enough; otherwise prioritize a physical baseline. **Decision sought:** confirm review sufficiency criteria and minimum testable experiment/site evidence.

## Slide 2. Literature search: where we are
- October Scopus S1-S5 exports: **46,698 aggregated search records**, **37,376 unique EIDs** after cross-query dedup; AI-assisted high-recall priority categorization, **not** 37,376 human inclusion decisions.
- October targeted technical queue: **30 DOI-indexed records** with a distinct **17-study** physics/measurement matrix. A 30-row tracking matrix is **not** 30 completed full-text audits.
- November newer scoped review PR106: **27 seed leads** + 9 exploratory public-web searches, protocol v0.1 and 72-field extraction schema; *separate* from October Scopus corpus, so counts are **not additive**.
- **Stop line:** formal, consolidated current-scope independent eligibility + full-text extraction + validated PRISMA counts **incomplete**. Protocol and stage counts need reconciliation and supervisor review.
Evidence: PRs [#89](https://github.com/Dossiya-SE/MSE-thesis/pull/89), [#93](https://github.com/Dossiya-SE/MSE-thesis/pull/93), [#97](https://github.com/Dossiya-SE/MSE-thesis/pull/97), [#106](https://github.com/Dossiya-SE/MSE-thesis/pull/106).

## Slide 3. What five important prior studies tell us
| Paper | Finding | What it does not prove |
|---|---|---|
| Gong et al. (2015), [DOI](https://doi.org/10.1109/TSG.2014.2365452) | Instrumented 25-kVA transformer and EV-pattern lab thermal loading; oil/winding observations and compared model | No operating same-site EVSE thermal trajectory or directly measured true hot spot |
| Kunlasing et al. (2022), [DOI](https://doi.org/10.1109/ECTI-CON54298.2022.9795360) | Measured transformer oil/load and demonstrated charging-current control | Controller commands were manually initiated; 3-EV overload response simulated; oil-temperature-triggered action not shown |
| Krama et al. (2026), [DOI](https://doi.org/10.1016/j.ecmx.2026.101960) | Original charger paper: extreme-hot-climate charger rectifier/ambient/power measurements | Raw rows still required; no linked transformer temperature |
| Bragone et al. (2022), [DOI](https://doi.org/10.1016/j.epsr.2022.108447) | Transformer thermal 1D PDE/PINN versus numerical finite-volume reference | Not direct validation of joint power/EVSE field heat causality |
| Fletcher and Khan (2025), [institutional report](https://www.racefor2030.com.au/) | Prior art on transformer thermal hysteresis and temperature-conditioned charger power control | A new simple temperature-triggered control cannot alone be claimed novel |

**Provisional gap, subject to falsification:** independently measured thermal state-time interactions between physically mapped transformer/EVSE, transition timing and actual electricity/mobility commitments are not yet established by the examined original set.

## Slide 4. What analyses actually ran
- **SINTEF transformer:** 8,592 hourly original observations. October-December conditional 24-h hindcast top-oil RMSE **0.9366°C versus persistence 2.1338°C**, using future observed weather/loading: **not an operational forecast or extreme-heat validation** (PR105).
- **KU Leuven/EPFL:** charger/vehicle electrical and battery measurements screened; EPFL 1,878 sessions linked but measurement-count and electrical power-boundary discrepancies remain; no EVSE internal thermal signal in portfolio (PR103).
- **Mathematical models:** source-qualified 2-/3-state oil/winding/charger thermal candidate, energy conservation, conditional equilibrium and stability proofs; synthetic reach-avoid study examined **4,096 toy schedules**, not measured field performance (PRs #97-#101).
- **OSF:** 61 qualifying event windows from 313 experiments show exploratory battery-terminal power changes; nonthermal lab PQ evidence, **not** thermal cross-sector causality (PR105).

## Slide 5. Mathematical direction and hard evidence gates
**Candidate:** oil, winding and EVSE-rectifier heat balances -> electrical transfer and device-specific power caps -> temperature-transition times -> charger energy-delivery deadline. This is a physics-based *hypothesis/model*, not validated same-site dynamics.

Three blocks:
1. **Literature evidence:** current-corpus original full-text/competing models/measurements not fully reconciled.
2. **Experiment:** same-site mapped transformer+EVSE, aligned time stamps, sensor provenance, extreme-heat events, raw data access **absent**.
3. **Validation and service:** independently observed command/thermal receiving-state and charging obligation **not established**.

**Method gate:** physics model first; consider grey-box parameter estimation if identifiable; consider PINN only for an independently testable spatial/inverse question with suitable held-out data.

## Slide 6. Exact next work and supervisor requests
**Before sending Friday/Saturday:** freeze these six slides, the five-paper evidence table, links and the explicit stopping point. Do **not** claim systematic review completion.

**After receiving supervisor feedback:**
1. Reconcile October search set, November pilot and older priority queues into one source/DOI/study-family inventory and reproducible PRISMA status.
2. Complete original full-text extraction and counterexample-led novelty search for priority studies. Track equations, sensors, actual controls, observed vs modeled states, validated outcomes, data access.
3. Acquire/review original Krama observations and seek a real same-installation transformer/EVSE dataset. Run data identifiability and independently held-out validation gates before choosing PHY/GREY/PINN.

**Three decisions requested from Prof. Phelan:** (i) approve the bounded mechanism and screening priority; (ii) recommend data collaborators or an acceptable component-level thesis fallback; (iii) agree minimum measured evidence for SO2/SO3 and the model-selection gate.

## Status integrity
This is a cross-PR reporting synthesis; several scientific items are in **open/draft** pull requests rather than approved main-branch research authorities. The historical 7-stage P-T-I-O or four-system power-water-transport-waste scopes are not the active frozen thermal-only objectives. No thesis result is marked experimentally coupled-field validated.
