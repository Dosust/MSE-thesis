# SINTEF D01 — Google Drive storage and numeric integrity reconciliation (2026-11-03)

**Decision:** D01 is **ACQUIRED_QA_PROVISIONAL**, not merely a discovered dataset. Do not reacquire solely for discovery and do not mistakenly count SINTEF DynaLoad as independent without source comparison.

## Evidence checked live

1. [D01 existing SINTEF Google Sheet](https://docs.google.com/spreadsheets/d/1gm3daUlCNb10teXLmHVNnm5N_o3lnGxvBOSmoEH2_cU/edit): 2 tabs, source-aligned measured and author-calculated values, **8,592 hourly 2024 records** according to its provenance tab and prior audit.
2. [SINTEF report](https://drive.google.com/file/d/1NEPfqbxqGy7GA6jlFMrWKCJYHXsnYZhl/view): 2026-11-01 research report records original sensor and author-calculated CSV MD5 matches, observation-variable audit, 192 missing hourly timestamps across two gaps, independent chronological holdout tests of a simple empirical transformer-temperature model, and the limitations below. **Those prior hashes were not independently rechecked in the present reconciliation.**
3. [SINTEF source README](https://drive.google.com/file/d/1UiLZG4ABFZOvq6x8rHh3LJUDZlXtBAcY/view): measurement source `Barug2025_sensordata.csv` is explicitly separate from `Barug2025_calculated.csv` (author-calculated model outputs).
4. The existing thesis [master Drive inventory](https://docs.google.com/spreadsheets/d/1zsiI8TPJeI2jKiZqlGj1okBrD6kuBVpw7xHzOxJcV6A/edit) lists D01 as `MEASURED_THERMAL_P`, `ACQUIRED_QA_PROVISIONAL`.
5. Standalone original source measurement CSVs **were not located in the accessible Drive filename searches** in this session; do not confuse the Google Sheet with a verified immutable original CSV archive.

## Severe Google Sheet import-type hazard

The **unified Google Sheet itself must NOT be read as trustworthy quantitative data via numeric `effectiveValue`**:

- On measured **Top oil [degC]**, cell `E2`: displayed `9.3475`; Google `effectiveValue.numberValue=575502`, with `numberFormat.type=DATE`.
- On model-calculated **Top oil (calculated) [degC]**, cell `M2`: displayed `13.02`; `effectiveValue.numberValue=46066`, `numberFormat.type=DATE`.
- Other sensor cells (`Voltage [kV]` B2, `Current [A]` C2, `Ambient [degC]` D2) are stored as `stringValue`, not numeric cells.
- This is not an ordinary formatting inconvenience. A `get_spreadsheet_range(..., value_render_option=UNFORMATTED_VALUE)` download or formula may use corrupt date serials, producing **physically impossible numbers** or invalid model fits.
- We have **not overwritten or "fixed" the source Sheet** by guessing the lost numerical values. The only safe repair is to import the original source-fidelity CSV **with forced decimal-dot numeric typing and timestamp column protected as timestamp**, then compare SHA-256/MD5 and verify spot-checks, ranges, units, sensor missingness, and chronological continuity.
- The original upstream source files and derived research outputs must always remain distinguished.

## Existing scientific findings (2026-11-01 report, not rederived here)

- Measured ambient: **−19.58 to 25.97 °C**. Thus not a measured hot-extreme calibration/validation set.
- Top oil measured range: **3.83–38.86 °C**.
- **192** missing hourly records over two gaps; source timestamps have **unverified timezone**.
- A prior one-step empirical thermal model was fit and tested on a chronological holdout. It does **not** constitute an independently validated physical heat equation or power↔EVSE field coupling.
- No documented same-installation EVSE, connected charger thermal derating, directional coupling, vehicle charging service or SO3 coupled field outcome.

## Corrected status of other priority candidates

- **Slovenia STREAM P/Q and transformer parameters:** source registered; standalone original files not located in the thesis Drive folder. Acquire and verify IDs, units and data-quality gaps.
- **Qatar 50 kW charger:** real charger thermal study; original synchronized telemetry not obtained; request from authors.
- **KIT campus charging:** no original in this checked Drive inventory; field-site / routine operation eligibility and equipment thermal variables remain to be qualified.
- **SINTEF DynaLoad:** author README explicitly states DynaLoad is the funding/project context for the 2024 transformer measurements. Do not count a second transformer installation without separate data provenance.

## Action gates

1. **Preserve** original Google Sheet and existing analysis reports as evidence, read-only.
2. **Recover** original sensor and author-calculated CSV files (from prior verified working archives or original repository), prove source hashes; do **not** re-download only to rediscover the source.
3. **Create a corrected, explicitly versioned numeric working dataset**, with the author's calculated columns separate from observations. Compare 8,592 count, 192-hour gaps, observed ambient/oil ranges, and rows whose Sheet types were corrupted. Recompute holdout statistics against originals.
4. Acquire original **Slovenian** operating data; request **Qatar** synchronized EVSE thermal data; investigate a **single physically connected** transformer/EVSE site.
5. Never claim fully measured transformer–charger thermal coupling or extreme-heat field validation from D01.

**Scope:** This note updates only data-storage/quality status. Canonical scientific objectives and frozen research artefacts remain unchanged.
