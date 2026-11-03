# User-supplied datasets — evidence qualification (2026-11-03)

**Thesis:** Engineering of Power–Electrified Transportation Interdependencies for Resilience

**Status:** REVIEW / WORKING EVIDENCE — this record is not a modification to frozen thesis authorities.
**Research scope:** Extreme-heat-driven thermal interdependencies between Power System P and Electrified Transportation System T_e, including their physical state-time effects and electricity/mobility-service consequences.

## Scientific decision

Two uploaded archives are suitable for **supporting** work; neither is, alone, a connected transformer–EVSE thermal field dataset. The other two single CSV files are not admitted as physical thermal calibration/validation evidence.

| Uploaded source | Qualified role | What it cannot show |
|---|---|---|
| Iowa 296-bus 2022 smart-meter archive | Measured hourly node-aggregated energy; derived nodal active-power loads; **assumption-derived** reactive-power loads for 296-node distribution benchmark | Does not contain measured EV charging, ambient or transformer/EVSE temperatures, or source ZIP's OpenDSS topology |
| Li et al. 2026 OSF 94GKC EV charging under power-quality disturbances | **Controlled AC-charging laboratory** measurements; voltage/current and sparse battery signals; supporting electrical response/quality study | Does not directly test extreme heat, DC fast-charger thermal derating, or thermal transformer–EVSE interdependency |
| EV_Battery_Charging_TR_Dataset_with_Notes.csv | Unverified illustrative/algorithmic candidate; quarantine from measured-physics claims | No sensor provenance; exactly generated-looking arithmetic columns; cannot validate thermal or event physics |
| data.csv | Single French charging-station metadata record; not useful for time-series modeling | No synchronized physics. Contains operator contact fields: NEVER commit raw to GitHub |

## Source 1: 296-node distribution-system smart meters — PRIORITY A (supporting electrical topology only)

- Original upload SHA-256: `548edd3840e2e4b8cffb9ccf9752963ce16f3318323910d32503cb4db92a8ad9`.
- Container: 2 Excel workbooks (`Smart Meter Data.xlsx`, `Calculated Nodal P&Q.xlsx`).
- README in each workbook states **296 network nodes** (feeder A 36; B 97; C 163), with hourly energy from January–December 2022.
- Three measured/aggregated load tables have **8760 hourly rows** and respectively **23, 65, 138 bus columns**, for **226 bus-level load series** in the supplied workbooks. **226 is not 296**: a network node is not equivalent to a measured-load column.
- Corresponding `P` sheets (kW) derive hourly demand using `P_k ≈ E_k/[1 h]`, assuming demand is constant throughout an hour.
- Corresponding `Q` sheets (kvar) derive `Q=P tan(arccos(PF))` with randomly selected PF in **[0.90,0.95]**, not measured power factor/reactive power.
- Example first interval, feeder A energy sum 312.204 kWh and derived P sum 312.204 kW; feeder B 346.503; feeder C 882.343, each on the 1 h interval basis. This is a **one-interval equality check**, not a full-sheet QA PASS.
- **OPEN:** request/obtain the matching 296-bus OpenDSS circuit, utility device/feeder connectivity, measurement assumptions, timezone, original license, and transformer ratings. The user ZIP does not include the circuit.
- Research role: baseline loads/uncertainty in a conditional electrical feeder model. EV charging overlay is an explicit simulation assumption until an observed connected installation is available.
- Dataset listing: https://wzy.ece.iastate.edu/testsystem.html (Bu et al., 2019 citation listed on source page).
- Original-user-upload archive in the thesis **Data** Drive folder: https://drive.google.com/file/d/1Fk3jvLBGe_9vyVi1_AAdz8dvUJ753Foq/view

## Source 2: OSF 94GKC EV charging disturbance experiment — PRIORITY B (supporting electrical response only)

- Original upload SHA-256: `38af5d53ff8779b75a746c6d5b29d13c84bedccf21793bdad308ba828151b707`.
- Authored experiment source: Li, H., Zhang, Y., Yang, S., & Liu, X. (2026), `Scientific Data` 13, 403. https://doi.org/10.1038/s41597-026-06768-5
- Original dataset DOI: https://doi.org/10.17605/OSF.IO/94GKC
- Exactly **313 experiment CSVs** in 11 directories (**250 main + 63 extended voltage-sag cases**), with **4,061,379 data records** counted across the submitted CSVs, plus six Python analysis scripts and a README. Recorded rows are not 4 million independent experiments or synchronized thermal measurements.
- Experimental scope from primary paper: controlled laboratory **single-phase 220 V AC** charging and **power-quality disturbances**. This does not replicate an extreme-heat DC-charging/transformer installation.
- The uploaded CSVs present **three actual schemas**: 250 files with 22 header positions, 45 with 5 fields, and 18 with another 5-field encoding variant. The larger schema repeats `HV_Battery_MaxChargeVoltage [V]` twice — header de-duplication must be explicit before any Python `DictReader` mapping.
- `HV_Battery_Temperature` has **23,052 non-empty entries across 4,061,379 records (0.57%)**. Four entries have the implausible value **1538.3**, and typical per-test values are almost constant. Their unit/sensor status and suspect values require the original paper/DAQ review.
- For primary thesis scope, such sparsity does not identify heat-transfer coefficients or validate dynamic thermal derating; treat thermal columns as an audit lead only. The primary paper notes interpolation/filling of lost CAN-FD current signals: retain processing provenance/quality flags.
- **No transformer thermal telemetry or verified physical transformer-to-EVSE topology** is present in supplied archives.
- Original-user-upload archive in thesis **Data** Drive folder: https://drive.google.com/file/d/1Sjdg5TaGWXybjO_8DOlnkzIeSHpVhR4x/view

## Source 3: 500-row battery event file — QUARANTINED / NOT MEASURED EVIDENCE

- SHA-256 `5f6800282627ef30eb382288f6b2207dd9c63692446305ac700f9105a9cc06f3`.
- 500 rows, 24 columns, one-minute timestamps. No authenticated sensor records, calibration, collection protocol or station asset map.
- All **500** `AvgTemp_C` values equal the arithmetic midpoint of recorded `MinTemp_C` and `MaxTemp_C` within numerical precision.
- All **500** `ChargePower_kW` values agree with `PackVoltage_V * ChargeCurrent_A / 1000` within 0.005 kW, the file's two-decimal rounding.
- The filename also appears in Mayingi, Thango, & Okojie (2026) as an input to a 500-sample BMS algorithm experiment (https://doi.org/10.3390/wevj17070359), but **matching a filename does not verify field origin or thermal events**.
- Do not present event flags, reported temperatures or probabilities as actual hardware observations without source-level verification. May be used for code regression/examples explicitly labeled unverified.

## Source 4: one-row charging-station CSV — METADATA ONLY / PRIVACY-LIMITED

- SHA-256 `127ccd2abf9c1b6f368b069d3a2ae7f115d82382f264bb6392b90549e233e2aa`.
- Exactly 1 French charging-station row, 39 attributes including metadata, nominal charger power and operator contact fields.
- No measured time, electric power, ambient temperature, component temperature or asset connectivity.
- Do not copy raw operator emails, telephone numbers, location identifiers or station IDs to GitHub. No model-validation role.

## Admission gates

- **SO1 component evidence:** partial; Iowa electrical feeder and OSF AC charging have credible source types, subject to per-file QA.
- **Topology gate:** BLOCKED_EVIDENCE — no shared installation connecting these separate archives.
- **Observed thermal interdependency:** BLOCKED_EVIDENCE — no synchronized transformer–EVSE thermal state/thermal restriction records.
- **SO2 model:** only independently checked component models and **explicitly conditional simulations**, not field-validated coupling.
- **SO3 services:** conditional/evidence-bounded only. No observed mobility-service degradation or coupled service recovery from these datasets.

## Required next actions

1. Acquire Iowa 296-bus **matching OpenDSS model** and independently verify meter-to-bus mapping, load units and timestamp grid; run bounded power-flow tests.
2. Test one OSF voltage sag experiment using the provided scripts and raw-versus-processed signal provenance. Audit stale, missing, duplicate and invalid temperature records; do not use it for heat calibration.
3. Establish connected thermal equipment/measurement program externally (transformer/EVSE temperatures, currents, cooling/derating/protection and site-level service data).
4. Resolve original data rights before publishing any raw redistribution.

**No canonical files, frozen objectives, or historical artifacts were revised.**

## Addendum — 2026-11-03: two further source-qualified archives

The original Iowa/OSF and quarantine qualifications above remain unchanged. Two *additional* archives were screened and registered as **D17** and **D18**, expanding the consolidated register from **19 to 21** entries.

- **D17: KU Leuven measured/processed EV charging efficiency data** (DOI https://doi.org/10.48804/C5PT0R): 40,873 AC CSV records, 258 timestamped DC AC-input/DC-output observations and additional 150-kW-labeled test tables. Useful for provisional charger electrical-loss and battery-response assessment. **Open:** backward time jumps, instrumentation boundary, one apparent swapped current/voltage heading, overlap with existing D02. **No EVSE internal temperature/protection or transformer link.** Drive original: https://drive.google.com/file/d/1zYktMEjoqXu-ZheGW8HGATwx23_lAcjH/view
- **D18: Najafi transformer fault infrared image data** (DOI https://doi.org/10.17632/8mg8mkc7k5.3): 255 lab thermal images and 45 expert region masks for a single-phase bench transformer. Useful only for optional fault segmentation background. **Not dynamic, radiometric or extreme-heat calibration.** Drive original: https://drive.google.com/file/d/1edhFUnQnM6nU5xtr1HPolQDMDBmuwY_G/view

Read [full new archive qualification, checksums and numerical QA](./UPLOADED_ARCHIVES_QUALIFICATION_2026-11-03.md) and [master inventory CSV](./MASTER_DATA_INVENTORY_2026-11-03.csv). The complementary native [Google Sheets master register](https://docs.google.com/spreadsheets/d/1zsiI8TPJeI2jKiZqlGj1okBrD6kuBVpw7xHzOxJcV6A/edit) is stored in the existing thesis Data folder.

**No direct connected P→T_e or T_e→P field thermal validation is claimed.**

## Original P/Q field-data update — 2026-11-03

**Source-grounded audit:** [SINTEF 2024 and STREAM Slovenian 2025 original-file qualification](./SLOVENIA_STREAM_SINTEF_RAW_AUDIT_2026-11-03.md).

- **D01 (existing SINTEF):** original 8,592-row measured sensor CSV publisher-MD5 verified and stored in [Drive](https://drive.google.com/file/d/1sOEtx-Nlr00n_pLqTdWb4BZI6O35m8Nu/view). NOT a new dataset count; preserve measured versus author-calculated distinction and original CSV numerics because native Sheets locale sometimes coerces values.
- **D19 (new Slovenian operational field):** P and Q originals [P in Drive](https://drive.google.com/file/d/1hZ7pCydBAkfnLf4RU2lTu3LozNvuQ4tO/view), [Q in Drive](https://drive.google.com/file/d/1SQ0ONhiCXK3_Ax--q9j0lUQV7IDACL5I/view). Both publisher-MD5 verified; 34,932 aligned 15-minute UTC timestamps and 12 anonymized transformer station IDs; 419,184 complete station-time P/Q pairs. Missing only 108 final slots of calendar 2025; real-time source units, sign convention and equipment nameplate crosswalk remain open.
- **Research-source registry:** [12-source field candidate register updated on review branch](../../../../data/field_candidates/2026-11-03/field_candidate_register.csv) to reflect that FD-001 and FD-004 are now raw-acquired. FD-005 transformer ratings CSV **not acquired**.
- **Google Sheets:** [Master data inventory](https://docs.google.com/spreadsheets/d/1zsiI8TPJeI2jKiZqlGj1okBrD6kuBVpw7xHzOxJcV6A/edit) and [Verified Field Candidates](https://docs.google.com/spreadsheets/d/1FgsfDBsCP43L6GyRbJ8v0NmUxseL4aJPeRnHBIHJqzk/edit) updated.

**Admissibility boundary:** authentically paired operational electrical P/Q is not observed thermally coupled transformer–EVSE behavior. No P→Tₑ, Tₑ→P or service-resilience field validation is claimed.

## Report 1 — Eleven measured-data and mathematical engineering research questions

**[Open Report 1: RQ1–RQ11 measured-data and mathematical answers](./REPORT_01_MEASURED_DATA_RQ1_RQ7_2026-11-03.md)**

Results generated from publisher-checksum-matched SINTEF transformer sensors, Slovenia paired station P/Q, and the KU Leuven experimental charging archive. RQ1–RQ3 have numerical results, RQ4–RQ5 have qualified component numerical results, while RQ6–RQ7 explicitly retain blocked independent reanalysis pending the original observation rows in the runnable environment. No causal coupled P↔Tₑ or extreme-heat field validation is asserted. New report is working evidence on the review branch only.

**Expanded Report 1 current status (2026-11-03):** RQ1–RQ5 measured component findings maintained; RQ7 independently recalculated from the original OSF 94GKC laboratory archive (313 CSV entries, 18 empty); RQ8 effective parameter estimation and 24h-block bootstrap; RQ9 model sensitivity; RQ10 same-site validity analysis; RQ6 (OPSD raw household records) and actual coupled-service RQ11 remain empirically blocked. [Extension Python source](./REPORT_01_EXTENDED_RQ7_RQ10.py), [derived JSON](./REPORT_01_EXTENSION_RQ7_RQ11_RESULTS.json), [PQ comparison summary](./REPORT_01_RQ7_OSF_BY_CATEGORY.csv). No frozen files or main-branch changes.
