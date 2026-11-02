# Thesis Drive Dataset Engineering Pipeline V3

Read-only Python pipeline for **measured components at separate physical sites**.

## What this version actually runs

1. SHA-256 registry of available Google Drive exports and source-role classification.
2. Nested KU Leuven BEV archive (`doi-10.48804-8kpdtw.zip`), signal unit dictionary from `CAN.dbc`, complete AC/DC session QA, 5-min and 15-min nonoverlapping window construction, chronological session-held-out fit/validation/test for three effective candidate models of BMS MIN/MAX temperature (with observed future inputs), comparison against persistence and held-out fixed-width interval coverage. Rejects saturation values >20kW in `BMSdissipation312` and never calls the channel measured heat/cooling power.
3. SINTEF measured transformer CSV, separate top-oil/HV hot-spot effective conditional dynamics (training Jan-Jun 2024, validation Jul-Sep, test Oct-Dec). Does not estimate a transferrable 350kVA transformer operating restriction.
4. EPFL session workbook and 2 large measurement workbook tabs. Parses original XLSX files via streaming ZIP/XML in the standard library (no extraction, no alternative spreadsheet package). Confirms 1,878 session IDs and reconciles the second CCS sheet's local session numbering with session-summary global IDs 1130-1878 using exact matching start times. Checks contiguous trapezoidal energy integration against session-reported energies, and records gaps and anomalies.
5. Optional UrbanEV archive filename inventory if that ZIP is present locally. Very large archives need external download or streaming through authorized connector; the 320MB Dryad archive was not mounted because Google Drive limits single-file downloads via this connector to 256MiB. No simulated "field observations" are invented.
6. Explicit PASS/PROVISIONAL/BLOCKED gate ledger in `00_FINAL_GATE_REPORT.json`.

## Requirements

Python 3.10+; `numpy`, `scipy`.

```
python -m pip install numpy scipy
```

## Run in this ChatGPT environment (the Drive-exported files already mounted at `/mnt/data`)

```
python /mnt/data/Thesis_Drive_Pipeline_V3/run_thesis_data_pipeline.py \
    --drive-dir /mnt/data \
    --out /mnt/data/Thesis_Drive_Pipeline_V3/results
```

Quick test of code and equations:

```
python /mnt/data/Thesis_Drive_Pipeline_V3/run_thesis_data_pipeline.py --self-test
```

If the EPFL raw workbook is slow, first run the vehicle and transformer tests with `--skip-epfl-raw`. You may use `--epfl-max-rows 5000` for a fast **incomplete demo**, but those results must not be reported as a full audit.

## Run from Google Colab with Google Drive mounted

```python
from google.colab import drive
drive.mount('/content/drive')
# Copy run_thesis_data_pipeline.py into the notebook working directory.
# Replace folder path below with your actual mounted Google Drive location.
!python run_thesis_data_pipeline.py --drive-dir '/content/drive/MyDrive/Data' --out '/content/drive/MyDrive/thesis_outputs'
```

The script intentionally does **not** open a public Drive URL or request OAuth tokens. The Drive folder must be mounted or exported using access you already have.

## Scientific interpretation

- **AC and DC vehicle thermal predictors are not validated physical battery models.** Outputs are *conditional hindcasts*, using real electrical/ambient/management signals observed over the prediction horizon. A statistical signal proxy must not be described as actual cooling heat.
- Pack minimum/maximum channels are distinct sensor extrema, **not average pack temperature**.
- Source data are kept intact; no data from independent installations are joined into one claimed field site.
- EPFL `P (W)` power-accounting boundaries must be verified. Reported session energy is **not** assumed to equal time-integrated grid-side energy. The observed discrepancy is a discrepancy, **not a directly measured efficiency**.
- SINTEF measured ambient range is restricted to the climate actually observed; extreme heat is an extrapolation outside that domain.
- The package does **not** qualify SO1 directional thermal coupling or SO3 field critical-propagation events.

## Output files

- `01_source_registry.csv` – source SHA-256, DOI and semantic role.
- `02_KU_Leuven_CAN_dictionary.json` – CAN signal definitions, units.
- `02_KU_Leuven_session_QA.csv` – flags and completeness per file.
- `02_KU_Leuven_splits_{5,15}min.csv` – frozen session-level splits.
- `02_KU_Leuven_predictions_{5,15}min.csv` – test predictions for MIN/MAX temperatures.
- `02_KU_Leuven_report.json` – candidate fits and model qualification.
- `03_SINTEF_report.json` – multistate conditional model results and uncertainty limitations.
- `04_EPFL_measurement_session_audit.csv` – all 1,878 session linkages and energy discrepancies.
- `04_EPFL_report.json` – reconciliation and electrical interface gate.
- `00_FINAL_GATE_REPORT.json` – overall gate ledger.

## Frozen research conclusions

**Physical directional coupling is BLOCKED**, because no measured transformer thermal state, EVSE internal thermal state and verified common electrical connection are jointly present. Candidate component models remain provisional or blocked. No source or output may be promoted to field-validated coupled data based on these artifacts alone.
