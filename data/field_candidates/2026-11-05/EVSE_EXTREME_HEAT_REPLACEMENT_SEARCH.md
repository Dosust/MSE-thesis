# EVSE extreme-heat field-data replacement: search, screening and bounded portfolio decisions

**Recorded:** 2026-11-05  
**Related acquisition:** [KIT 110/20/0.4 kV original-file and time-QA report](KIT_OLTC_22826984_ACQUISITION_AUDIT.md)  
**Current thesis authority:** [Official title V3](../../../project/CANONICAL_THESIS_TITLE_V3.md), [SO1–SO3](../../../project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md), [thermal-only scope V4](../../../project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md), [evidence rule](../../../project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md).

## 1. Question and target dataset definition

**User question:** Is there any measured operational EVSE heat/temperature and power-derating dataset in **United States, United Kingdom, European Union or Africa**, or a defensible **combination** of separately measured datasets, that could replace unavailable raw Qatar extreme-heat EVSE data?

Reference study: **Krama et al. (2026)**, DOI https://doi.org/10.1016/j.ecmx.2026.101960. Previously screened source describes measured commercial DC fast charger behavior in extreme heat, with ambient/rectifier temperatures and charging power/SOC. **Raw logs available on author request; no public original dataset independently acquired.**

Strongest desired same-site evidence:
- timestamp and time zone plus precise measurement location/instrument identity;
- true ambient temperature and **EVSE internal thermally relevant sensor** (rectifier/converter or another exactly identified critical component);
- actual offered/requested charging power, electrical input/output and delivered power/current;
- cooling/fan/derating setpoints or recorded temperature-linked curtailment events;
- charger nameplate/converter/cooling metadata, controller state, calibration, error/quality flags and source provenance;
- vehicle SOC and charge-by-departure requirement if seeking SO3 mobility service;
- independently observed transformer/feeder thermal state + confirmed connected transformer→EVSE topology for a stronger coupled-field claim.

No single item is mandatory for every narrower component-level study. However, **missing thermal sensors prohibit a measured EVSE-internal temperature model**, and data from two unrelated installations do **not** become one same-site empirical dataset when combined.

## 2. Scientific reading list and raw-data access decisions

This is a record of source screening, **not** a declaration that raw files have been downloaded. Respect the paper-specific availability statement.

| Source | DOI / record | Reported data role | Original-data status at this checkpoint | Decision |
|---|---|---|---|---|
| Fletcher & Khan, RACE (2025) | https://www.racefor2030.com.au/content/uploads/Final-report-0571-FINAL-FINAL.pdf | Transformer thermal inertia + charger control and numerical scenarios | No verified downloadable original raw field file; report discusses follow-on field work | Use model/method report; inquire whether later field observations exist |
| Bragone et al. (2022) | https://doi.org/10.1016/j.epsr.2022.108447 | Transformer heat-transfer PDE/PINN vs numerical solver | No verified original raw dataset | Retain mathematical method; inquire about experimental input values |
| Krama et al. (2026) | https://doi.org/10.1016/j.ecmx.2026.101960 | Extreme-heat commercial DC EVSE ambient/rectifier temperature and charging derating | On author request; no public original CSV verified | **Primary new thermal-field acquisition target** |
| Pan et al. (2025) | https://doi.org/10.1049/hve2.70024 | Dynamic thermal rating + EV response/control | Research data on request; publication lists supplementary material, not confirmed full raw time series | Request underlying measurements and simulation-case metadata |
| Li, Chang & Lu (2026) | https://doi.org/10.1109/PESGM58988.2026.11693150 | Connected bus-depot transformer and charging electrical signals | No verified public original raw dataset | Request original linked electric measurements, station mapping, thermal sensors if available |
| Acker et al. (2025/2026) | https://doi.org/10.1007/s41104-025-00157-7 | Battery/coolant thermal dynamics; separate from EVSE temperature | Authors state no permission to share underlying data | Retain as component physics; do not treat as acquisition route |

These statements concern **what was verified during this screening**. “No publicly verified file found” does **not** imply the data can never be obtained.

## 3. Step-by-step repository search attempts

### 3.1 First Python metadata screening program

Program delivered to user: search_evse_thermal_field_datasets.py. It was designed to query four public repository metadata APIs:
- https://zenodo.org/ (Zenodo);
- https://api.datacite.org/ (DataCite);
- https://api.figshare.com/ (Figshare);
- https://datadryad.org/ (Dryad).

Intended output files: priority_candidates.csv, priority_region_hints.csv, all_screened_metadata.csv, screening_summary.json, api_errors.txt.

**Actual execution outcome in the ChatGPT runtime:** syntax/execution workflow passed, **32 live API requests attempted, 0 succeeded because environment requests were blocked**, and 0 repository candidates were verified by those API queries. Therefore the zero candidate count is **not negative evidence** about actual public availability. No new raw dataset was downloaded by this execution.

The user was instructed to run the program on Mac with internet:

~~~bash
python3 "$HOME/Downloads/search_evse_thermal_field_datasets.py" \
  --per-query 20 \
  --out "$HOME/Downloads/EVSE_Heat_Dataset_Search"
~~~

**User Mac execution output of this program:** not supplied yet. Do not claim the user's Mac search succeeded.

### 3.2 Follow-up public-web and source inventory screening

A separate web source search (not the blocked Python API process) yielded candidates with distinct scientific roles:

| Candidate | Location | Primary/source link | Original raw-data evidence | Distinct contribution |
|---|---|---|---|---|
| US DOE EVs@Scale NextGen EVSE characterization report | United States | https://www.nrel.gov/docs/fy25osti/93967.pdf | Report contains test findings/plots; standalone numeric temperature-time CSV not verified | High-power charger thermal/connector heating and thermally constrained power in controlled temperature tests. **Connector/cable ≠ internal rectifier sensor**. |
| KIT campus charging characterization | Germany | https://zenodo.org/records/17866847 | Repository candidate; internal EVSE temperature not identified | Electrical+ambient; no verified EVSE thermal derating |
| KIT OLTC multivoltage | Germany | https://zenodo.org/records/22826984 | **Three original Parquet files later acquired and MD5-verified on user's Mac** | Synchronized-range electrical 110/20/0.4 kV measurements; no temperature column |
| EPFL level 3 charging records | Switzerland | https://github.com/DESL-EPFL/Level-3-EV-charging-dataset | Existing thesis audit; not new | EVSE session electrical behavior; no verified rectifier temperature |
| SINTEF transformer sensors | Norway | https://zenodo.org/records/17223516 | Existing thesis audit; not new | Transformer internal thermal measurements; no co-site EVSE measurements |
| KU Leuven BEV records | Belgium | https://rdr.kuleuven.be/dataset.xhtml?persistentId=doi%3A10.48804%2F8KPDTW | Existing thesis audit; not new | Vehicle/battery-side heat response, not EVSE internal thermals |
| Caltech ACN charging logs | United States | https://ev.caltech.edu/dataset | Existing candidate; charge sessions/current, no internal thermal states verified | Potential charge-by-departure service proxy |
| South African bus depot digital-twin study | South Africa | https://www.mdpi.com/2071-1050/18/21/10826 | Underlying full operational OCPP raw record access not verified | Real session histories used in a modeled service-consequence study; modeled missed trips **not observed field failures** |
| Li bus-transformer charging study | Location/source as published | https://doi.org/10.1109/PESGM58988.2026.11693150 | Raw series not verified | Potential same-site transformer and charging electrical interface |

**UK or other African complete rectifier/EVSE thermal raw dataset:** none independently confirmed in this screening. Do **not** generalize that none exists worldwide.

### 3.3 Second, broader screening and portfolio program

Program delivered to user: search_evse_replacement_v2.py.

- Earlier execution generated a 10-source assessment, four candidate portfolios, a source register and unresolved-gap report.
- Its offline/source-based screening **did not deliver a fully verified public Qatar-equivalent original thermal dataset**.
- Intended Mac run for live repository queries:

~~~bash
python3 "$HOME/Downloads/search_evse_replacement_v2.py" \
  --live \
  --per-query 20 \
  --out "$HOME/Downloads/EVSE_Replacement_V2"
~~~

**User Mac execution results of V2:** not supplied as of this record. The fact the assistant generated local analysis outputs is **not proof of a successful live repository discovery**.

## 4. Research decision: role-specific data combination, not false field merging

Provisional **model-building portfolio**:
1. **US DOE EVSE testing:** candidate charger connector/cable thermal power-limiting mechanism from experimental report. **Raw numbers unavailable/not verified**; not identical to Qatar measured internal rectifier thermal data. Cannot independently calibrate a time-resolved internal EVSE rectifier model using paper plots alone without qualified extraction/uncertainty.
2. **EPFL charging sessions:** preserve previously audited real DC power/session series for a **separate charging electrical** component.
3. **SINTEF transformer field observations:** preserve previously audited transformer thermal time series for a **separate transformer thermal** component.
4. **KIT OLTC multivoltage:** new user-local verified original files supply **electrical** measurement context; full row-level time/topology qualification pending. **Not** an original same-site transformer+EVSE thermal series.
5. **South African bus depot study or Caltech ACN:** potential **service-input** time series / departure demand, only if original underlying records and semantics are verified; reported simulated missed trips are not measured service failures.

The portfolio may support physically constrained **scenario simulation** with independently calibrated component pieces and declared assumptions. It does **not** establish one observed 2026 multisite temperature/power trajectory, a field-proven directional thermal effect, or validation of a complete coupled SoS under extreme heat.

## 5. Evidence-status decisions and next acquisition targets

| Requirement | New sufficient data in hand? | Best current target |
|---|---|---|
| Commercial EVSE internal temperature and ambient in extreme heat | **NO** | Krama original logs from corresponding author |
| Actually recorded charger thermal derating and controller/cooling status | **NO** | Krama original logs; DOE test raw measurements if releasable (connector/cable validity domain only) |
| Verified 110 kV→20 kV→EV electrical topology | **NOT YET** | Publisher KIT diagram/instrument metadata; user Mac KIT files provide electrical series |
| Same-site EVSE and transformer temperatures | **NO** | New connected operating-site campaign / cooperation |
| Actual charge-by-departure service linked to measured thermal limits | **NO** | Coordinated charger and fleet/depot raw logs; model-only trip deficits remain model results |
| Independent high-ambient transformer validation | **NO** | Real independent hot-weather transformer temperature + load + cooling + ambient logs |

## 6. Non-duplication and provenance

Prior thesis work on SINTEF, EPFL and KU Leuven already exists. **Do not restart acquisition or claim novelty by recombining them**. Existing QA findings do not become new field campaigns. KIT's three files are **newly acquired user-local data** in this exchange; their detailed checksums, schemas and timestamp spans belong in the [KIT report](KIT_OLTC_22826984_ACQUISITION_AUDIT.md).

All source locations and data-access statuses in this note reflect screening as of 2026-11-05 and are **not** an exhaustive audit of all global repositories.

## 7. Immediate research actions

1. Ask Krama's corresponding author for anonymized original rectifier/ambient, charger power, derating/cooling and timebase data.
2. Ask US DOE/NREL for underlying original EVSE characterization temperature/power files, metadata, connector vs rectifier sensor identity and licensing; **do not digitize report plots as exact measured data without an uncertainty record**.
3. Ask Li/Pan investigators for original transformer/charging or DTR files, station topology and their actual scope of thermal sensors.
4. Complete KIT timestamp every-row QA and electrical topology audit; file only source-supported conclusions.
5. Investigate African/UK operational operator datasets with explicit internal EVSE temperature fields, not merely geographic metadata or charging-session counts.
6. Register each actual new raw file with site, sensor/channel names, units, clock, license, file hash, original/source traceability and G0–G7 status.

**Final checkpoint:** **NO fully verified, publicly downloadable equivalent of the Qatar operational EVSE internal extreme-heat derating dataset has been obtained** in this workflow. An independent-source component simulation is **possible in principle**, not proof of a measured joint thermal interdependency.
