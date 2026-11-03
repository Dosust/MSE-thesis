# Uploaded EV charging/routing archive — evidence qualification V1

**Audit date:** 2026-11-03  
**Thesis:** Engineering of Power–Electrified Transportation Interdependencies for Resilience  
**Status:** WORKING / QUARANTINED SOURCE — not admitted as measured physical-model evidence.  
**Canonical rules:** `project/CANONICAL_THESIS_TITLE_V3.md`, `project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md`, and `project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md`.

## 1. Original archive and provenance

- User upload: `archive.zip`, preserved unchanged.
- SHA-256 (whole ZIP): `cd590c860a9b2dd5d72bdfa61e2a8d18e09315faf2e10a832fd9206dd97ff62c`.
- Contents: `ev_charging_dataset.csv` (64,945 rows, 28 columns); `location_dataset.csv` (31 nodes, four columns).
- ZIP CRC integrity: **PASS**. File-level SHA-256 values are in `audit_results.json`.
- File names and schema closely match **EV Charging Load Dataset and Optimal Routing**, Kaggle: https://www.kaggle.com/datasets/datasetengineer/ev-charging-load-dataset-and-optimal-routing . This is a **candidate origin**, not verified identity or measurement provenance; the exact uploaded-source license and generation protocol remain **OPEN**.
- Private original is preserved in the thesis Google Drive `Data` folder under `QUARANTINE_UNVERIFIED_EV_Charging_Routing_UserOriginal_2026-11-03.zip`: https://drive.google.com/file/d/1-XY4-xDP5sfpbv3gPzTyHhjJ0ZJR2nYj/view
- Original CSVs are **not** committed to GitHub, because raw redistribution rights and measurement authenticity have not been established.

## 2. Detailed checks from actual source bytes

| Test | Observed | Scientific interpretation |
|---|---:|---|
| Charging data rows and attributes | 64,945 × 28 | Large table alone does not imply measured observations |
| Timestamp span | 2017-01-01 00:00 to 2024-05-30 00:00 | Consecutive hourly labels; no hourly timestamp gaps |
| Missing cells | 0 | Completeness does not imply physical validity |
| Unique vehicle IDs | 1 (`106`) | Cannot treat rows as diverse vehicles |
| Distinct battery capacities for that single vehicle ID | 61,733 | Physically incompatible with one stable battery pack across the time series unless IDs/fields have undocumented semantics |
| Unique charging-station IDs | 1 (`2`) | Cannot identify a network of installed chargers |
| Distinct `Session_Start_Hour` values | 1 (`6`) | Does not represent observed start-hour diversity |
| `Weekday` mismatches (Monday=0) | 55,612 / 64,945 (85.6%) | The weekday coding is undocumented; the diagnostic uses conventional Monday=0 |
| `Energy_Drawn_kWh > Charging_Rate_kW × Time_Spent_Charging_mins/60` | 20,027 / 64,945 (30.8%) | Contradiction **if** the listed rate is the maximum sustained session power and reported duration covers the full energy transfer; variable semantics unverified |
| `Charging_Load_kW > Charging_Rate_kW` | 15,372 / 64,945 (23.7%) | Contradiction **if** values have the same electrical boundary/rating meaning |
| Temperature range | 0–40°C | This is not a measured oil/winding/charger-temperature channel; no extreme-heat experiment identified |
| Clear conditions with positive precipitation | 32,328 / 32,328 | Labels and precipitation inconsistent if they refer to the same instant, location and weather interval |
| Reported destination distance less than 80% of geodesic distance | 5,097 / 64,945 | Inconsistent if geographic coordinates and distance refer to the same origin–destination pair |
| Location entries | 31 | Abstract `(x,y)` node coordinates and facility categories; **no edge list, topology, travel network or power-system network** |

All checks are reproducible using `audit_uploaded_ev_archive.py`, with exact recorded outputs in `audit_results.json`, `quality_gates.csv`, `dataset_register.csv` and `variable_dictionary.csv`.

**Important inference bound:** The data strongly resemble algorithmically generated examples, but exact generation is **not proven**. Some apparent contradictions could reflect undocumented field definitions. The correct classification is `UNVERIFIED; LIKELY SYNTHETIC`, not `confirmed fake` and not `real sensor field data`.

## 3. Limited useful role for this thesis

1. **Scientific Python testing:** test CSV ingestion, unit conversion, input validation, schema checks, chronology checks, label leakage checks and fault handling using expressly **unverified/illustrative** data.
2. **Conditional benchmark of charging scheduling or service-index software:** demonstrate how code responds to varying inputs; any quantitative performance is **internal software-test performance only**, not physically validated charging-service resilience.
3. **Illustrative graph/route processing:** use 31 abstract nodes as a toy geography **after generating/documenting** a separate assumed edge list. Nodes called `Power Plant` do not confer verified electricity-network connectivity.

**Explicitly prohibited research transfers:** do not infer measured charger behavior, a 7-year actual vehicle history, battery thermal derating, transformer limits, heat-transfer coefficients, causal `P→T_e` or `T_e→P` effects, or observed resilience from this archive. No equipment or sensor metadata qualify these claims.

## 4. Admission to thesis research objectives

| Objective | Status | Reason |
|---|---|---|
| SO1 — qualifying physically directed thermal mechanisms | **NOT ADMITTED** | No verified equipment identity, transformer–EVSE topology, or measured component thermal states |
| SO2 — physics-based state–time coupling model | **NOT ADMITTED FOR CALIBRATION/VALIDATION** | No temperature dynamics or measured physical coupling |
| SO3 — measured service resilience and sustainability | **NOT ADMITTED** | No verified electricity/mobility-service requirement or real operational records |
| Reproducible software methods | **ADMISSIBLE, CLEARLY SYNTHETIC/ILLUSTRATIVE** | Suitable for testing code robustness independent of physical-science claims |

## 5. Next evidence-qualified research steps

Continue using the separately audited **Iowa 296-node smart-meter archive** for conditional power-flow experiments, and **SINTEF transformer observations** and source-qualified charging thermal studies for component investigations. Find the actual feeder–transformer–EVSE topology and synchronized heat/temperature telemetry needed for cross-system physical validation. Do **not** merge these separate installations as if they were one observed system.

## 6. Verification steps

```bash
python audit_uploaded_ev_archive.py /path/to/archive.zip /path/to/output \
  'https://drive.google.com/file/d/1-XY4-xDP5sfpbv3gPzTyHhjJ0ZJR2nYj/view'
python -m unittest discover -s tests -v
```

The checks establish input integrity and internally detected inconsistencies, **not validation of any physical model**.

## 7. Citable source links (provenance leads; claim-level support remains bounded)

- [Original candidate Kaggle listing](https://www.kaggle.com/datasets/datasetengineer/ev-charging-load-dataset-and-optimal-routing).
- [A public repository using matching filenames](https://github.com/SarthakSingh-96/EV-Charging-Optimization-using-Stochastic-Dynamic-Programming). This repository describes a dataset as “real-world” but does not establish sensor provenance for the uploaded ZIP.
- Thesis identity and scope: canonical **private** repository files cited above; not external literature.
