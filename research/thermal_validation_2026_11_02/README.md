# All-source thesis scientific validation pipeline

**Thesis**: Physics-based mathematical engineering of Power ↔ Electrified Transportation interdependencies, extreme-heat resilience. Eight evidence stages, strict PASS / PROVISIONAL / BLOCKED.

## Inputs (original Drive data, read-only)
Place these original files together under `/mnt/data` (already available in this session) or another directory:

- `Barug2025_sensordata.csv` and `Barug2025_calculated.csv` — SINTEF, DOI 10.5281/zenodo.17223516. Original sensor MD5 checked against Zenodo.
- `doi-10.48804-8kpdtw.zip` — KU Leuven two-level BEV archive; DOI 10.48804/8KPDTW.
- `Measurement_data.xlsx`, `Session_data.xlsx` — EPFL Level 3 EV charging dataset.

Other optional Drive assets (UrbanEV ZIP, RAR network data, registered-vehicles CSV, generic resilience CSV) are inventory/context only; they are **not** treated as measured field thermal coupling. UrbanEV original ZIP exceeded Google Drive connector's 256 MB download limit in this session; it is not independently audited here.

## Execute

```bash
python -m pip install numpy pandas scipy matplotlib
python /mnt/data/thesis_python_all/run_all.py --data-dir /mnt/data
```

For offline use in a local project folder, copy this directory and the original five named files unchanged; run `python run_all.py --data-dir /path/to/original/files`.

For rerunning everything except the already completed vehicle fit (only when its output files exist inside this folder):

```bash
python run_all.py --data-dir /mnt/data --skip-heavy-vehicle
```

## Outputs

- `01_provenance/`: SHA256 source registry, publisher SINTEF MD5 verification, original KU Leuven CSV fingerprints and QA, contextual source classification.
- `02_vehicle/`: DC raw-model failure diagnostics, unchanged-source session splits, 15-min conditional hindcast, baseline comparison, model parameters, model-selection and uncertainty screens, holdout graphs. Source *future observed* current and ambient are supplied for model predictions. Maximum BMS sensor temperature is NOT established as lumped battery temperature.
- `03_transformer/`: fitted candidate top-oil and hotspot model, 24h conditional hindcast/baseline table, split-holdout error band, observed vs predicted plot. A 40MVA Norwegian asset is **not** a 350kVA distribution transformer.
- `04_epfl/`: minute-level source audit by connector and session, measured P integral comparison with source energy, sessions cross-check via time-verified CCS2 global ID +1129, 172.5-kW shared station apparent exceedance records. The data provider's 64,277-row claim remains unreconciled with 61,816 populated workbook records. P(W) measurement boundary is unverified; do not calculate AC/DC charger efficiency.
- `05_evse/`: missing internal-temperature and thermal-derating data gate.
- `06_coupling/`: independent P→Te and Te→P mechanism claims and evidence conditions; blocked until physical topology and synchronized measurements are documented.
- `07_vvuq/`: no coupled synthetic-data release while blocked.
- `08_services/`: no causal resilience / sustainability outcome release while blocked.
- `acceptance_gates.csv` / `EXECUTED_FINDINGS.md`: written from actual executed numerical results.

## Scientific integrity

- No original data overwritten and no silent gap interpolation.
- Charging-session train/validation/test are separate; overlapping prediction windows are not independent experimental units.
- Model coefficients `alpha`, `beta`, `q0` in the thermal screening are **effective** and may not be uniquely identifiable. The nuisance `q0` is not a measured cooling rate.
- SINTEF author's `calculated.csv` is **not** treated as independent observation truth.
- Avoid interpreting EPFL P(W) as specifically AC input or DC output until source documentation establishes its metering boundary.
- Separate transformer, vehicle, EVSE, network and weather datasets do **not** establish a common physical installation.
- Critical transition times, delays, service deficits, and sustainability indicators cannot be called field validated without the necessary measurements and operating requirements.
