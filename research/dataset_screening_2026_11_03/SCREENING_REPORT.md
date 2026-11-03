# Dataset screening — 2026-11-03

**Official V3 thesis title:** Engineering of Power–Electrified Transportation Interdependencies for Resilience

**Governance:** `project/CANONICAL_THESIS_TITLE_V3.md`; `project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md`; frozen thermal-only, extreme-heat state-time scope. No change to frozen scientific objectives.

**Evidence policy:** Source metadata, landing-page data descriptions, and spot-inspected remote text are **not equivalent** to original raw-data download, checksum validation, full-column QA, or independent model validation. Nothing screened below establishes measured same-site transformer-to-EVSE thermal coupling.

## Decision summary

| ID | Source | What we verified on 2026-11-03 | Admission | Role |
|---|---|---|---|---|
| KU-C5PT0R | [KU Leuven RDR DOI 10.48804/C5PT0R](https://doi.org/10.48804/C5PT0R) | EnergyVille real-car charging measurements, 10 files (4 AC-labelled CSVs, 5 XLSX, 1 Readme); CSV sample viewed remotely: 1-s offset-aware timestamps, BMS pack max/min temperatures, BMS cooling targets, SOC, charge-line power/voltage/current, battery voltage/current, charging-power limit. Published 2025-03-05, CC BY 4.0. | **CANDIDATE / not raw-data admitted** | Electrical conversion and battery-side thermal validation; possible charge-energy boundary reconciliation |
| OSF-94GKC | [Li et al., Scientific Data 2026](https://doi.org/10.1038/s41597-026-06768-5), [OSF](https://osf.io/94gkc/) | Lab-controlled single-phase **220 V AC** full-vehicle charging under 10 imposed power-quality event types. CAN-FD signals include battery voltage/current/SOC/temperature and charging max power; 23.0 MB research archive and 16.9 kB validation-code archive publicly listed. | **CONDITIONAL / not raw-data admitted** | Isolated electrical disturbances and battery responses only, if their thermal interpretation is actually necessary |
| KAG-ZARA | [Kaggle battery charging dataset](https://www.kaggle.com/datasets/zara2099/ev-battery-charging-and-thermal-runaway-dataset) | Page describes 500 one-minute rows, 24 columns of battery/charger IDs, battery states and event labels; equipment logger, independent instrument calibration and raw provenance unverified. | **REJECT for thesis field validation** | Outside minimum-sufficient EVSE/transformer thermal mechanism; retain citation only |
| GLOBAL-OCM | [Global EV Infra GitHub](https://github.com/tarekmasryo/global-ev-infra-dataset) | 2025 cross-sectional Open Charge Map-derived location/port/rating inventory; no time-series temperature/power logs. Reported classification `is_fast_dc` inferred from power >=50 kW. | **REJECT for SO1–SO3 thermal validation** | Geographical context only; no physics admission |
| US-NLR | [NLR Alternative Fuels charging ports API](https://developer.nlr.gov/docs/transportation/alt-fuel-stations-v1/ev-charging-units/) | Official charging-port CSV API; API key required; inventory not internal temperature telemetry. | **REJECT** | Station inventory only |
| EUROPE | [EU data portal](https://data.europa.eu/data/datasets/62cd9911c0f97379d7b2213c~~1?locale=en), [French transport data](https://transport.data.gouv.fr/datasets?format=csv&locale=en&type=charging-stations) | User-provided EU/France station-inventory leads; precise linked EU page file schema not verified in this cycle. | **REJECT** | Not thesis thermal measurements |
| UK-DFT | [Official UK EVCI tables](https://www.gov.uk/government/statistical-data-sets/electric-vehicle-charging-infrastructure-statistics-data-tables-evci) | Public chargers by geography and power-band statistics (updated through July 2026 on page). | **REJECT** | Aggregate infrastructure statistics |
| AUS-NSW | [Transport for NSW open data](https://opendata.transport.nsw.gov.au/data/dataset/?tags=nsw&tags=Electric&tags=EV&license_id=cc-by&organization=transport-opendata-hub&res_format=CSV) | User-provided filtered charging-station directory; detailed schema not independently inspected in this cycle. | **REJECT** | Station locations only |

## Primary-source technical findings

### KU Leuven C5PT0R: actual CSV sample, not a new DC-EVSE thermal field dataset

Landing page confirms 4 CSV files: `Figure6_AC1.csv`, `Figure6_AC2.csv`, `Figure7_AC1.csv`, `Figure7_AC2.csv`, plus 5 spreadsheet figure files and Readme. In one remote original-file text inspection of `Figure6_AC1.csv` (Dataverse fileId=228264), the header is:

`timestamps,BMSdissipation312,BMSinletActiveCoolTarget312,BMSinletActiveHeatTarget312,BMSinletPassiveTarget312,BMSmaxPackTemperature,BMSminPackTemperature,SOCave292,TotalChargeKWh3D2,ChargeLinePower264,ChargeLineVoltage264,ChargeLineCurrent264,BattVoltage132,RawBattCurrent132,pmax`

A sample shows timestamps `2024-10-03 10:18:28.513050112+02:00`, then one-second increments. This is useful for a test of charger-side line power vs battery-side power and battery temperature dynamics, **subject to verification of channel naming, phase count, units, current sign, boundary, SOC and timestamp semantics**. In particular, `BMSmaxPackTemperature` is **vehicle battery/BMS**, not EVSE internal rectifier temperature; `BMSinletActiveCoolTarget312` is a reported target, not an independently measured charger cooling state. Do not interpret `TotalChargeKWh3D2` as session energy without calibration and units verification.

The prior 134-session KU Leuven analysis belongs to a DIFFERENT source: [DOI 10.48804/8KPDTW](https://doi.org/10.48804/8KPDTW). Never conflate it with C5PT0R. No verified raw DC time-series CSV has been identified in the C5PT0R file list despite the title/description mentioning AC and DC charging.

**Next:** obtain original complete 6.1 MB archive and verify publisher MD5 per file; map and audit all ten files; check power/energy dimensional consistency and independently verify charging boundaries. Until executed, status remains CANDIDATE.

### OSF 94GKC: controlled PQ response, not extreme heat

The peer-reviewed article documents actual vehicle tests under 10 imposed electrical disturbances with synchronized CAN-FD data, including `Time [s]`, `HV_Battery_Current [A]`, `HV_Battery_Voltage [V]`, `HV_Battery_SOC [%]`, `HV_Battery_Temperature` and `HV_Charging_MaxPower [W]`. The imposed disturbances occur on a 220 V single-phase AC test installation. The article reports replacement of missing CAN-FD samples using adjacent-value averages; timing of transition events requires a raw-vs-preprocessed provenance check. No measured transformer top-oil/hotspot or charger rectifier/heatsink temperature is demonstrated.

**Next:** download and checksum original OSF archive and code; distinguish measured channels from interpolated records and imposed stimulus; only analyze where a thermal-relevant supporting electrical response is necessary. Do **not** transplant its AC charging dynamics as measured DC EVSE derating.

### Kaggle battery data: not a thesis thermal-interdependency field-validation asset

The dataset page advertises 500 rows, one-minute timestamps and 24 columns, including battery temperature and event classifications. Independent field-device identity, acquisition instrumentation, physical topology, error model, and trace continuity were not authenticated. Its safety event labels are not evidence of field-validated charger cooling or transformer restrictions. Do not include this in thermal law identification, training or coupled validation, and do not present as field-proven.

### Station directories: exclude from active thesis models

Tarek Masryo, NLR/AFDC, EU/France, UK Department for Transport and NSW are primarily inventories or statistics. They do not provide synchronized transformer/charger temperature and power trajectories, charger-side thermal control commands, or a verified same-site electrical topology. Retain links only in **SCREENED / CONTEXT-ONLY** register; do not download or archive their large CSV inventories in the thesis validation pipeline.

## Status against frozen SO1–SO3

- **SO1:** Component measurements can support individual mechanisms, but **no verified same-site directional P→Tₑ or Tₑ→P thermal mechanism** is provided here.
- **SO2:** KU C5PT0R can inform electrical/vehicle component balances after raw QA; OSF may support electrical perturbation sensitivity if needed. Neither validates a coupled electrothermal state-time model.
- **SO3:** Charging energy and time may support narrowly bounded service proxies after meter definitions, but no documented critical electricity/mobility requirement, coupled transition delay, or field thermal restriction is established.
- **Coupled thermal field validation: BLOCKED.**

## Current priority (do not divert from existing pipeline)

1. P1: verify **KIT** actual physical connectivity and synchronized measurement channels; seek same-site transformer- and EVSE-temperature data.
2. P1: request original **Qatar measured DC EVSE rectifier temperature / offered-versus-delivered power / derating** dataset; qualify equipment and sensing.
3. P1: correct **SINTEF** winding-hot-spot model failure and **KU Leuven 8KPDTW** DC vehicle thermal model failure; retain independent holdouts.
4. P2: acquire/audit **C5PT0R** original archive as distinct charger electrical/battery component evidence; no power-system coupling claim.
5. P3: optionally screen **OSF 94GKC** if electrical disturbance behavior becomes a qualified explanatory variable.
6. Archive all station inventories and Kaggle battery safety records as **rejected/context-only**, without active modelling or raw acquisition.

## Sources, method and remaining verification limit

Source review performed 2026-11-03 using public publisher landing pages, the article's Methods/Data Records and original KU Dataverse CSV text response, official station-inventory descriptions and source repository READMEs. Full new original archives were **not downloaded to the thesis workspace**, and no raw-file MD5/SHA256 or full dataset QA was completed in this cycle. Therefore the GitHub entry and Google Drive companion are a **screening and next-action record**, not a declaration that new validation data were acquired.

This record is additive and does not edit frozen project/ authorities or supersede executed 2026-11-02 component validation gates.
