# CSV contracts, field semantics and physical boundary rules

Templates are *header-only* under `templates/` and contain no invented measurements. Plain UTF-8 CSV, stable source IDs, ISO-8601 UTC strings and decimal dot are required. Keep raw original source headers unmodified in `raw/`.

## Registers

- `source_registry.csv`: source and original-file identity, DOI, URL, owner, license, size, SHA-256, sample period, channel list, raw/synthetic classification and acquisition status; **one row per source file/version**.
- `asset_topology.csv`: site ID, upstream/downstream assets, voltage interface, one-line source, circuit ID, topology VERIFIED/OPEN, evidence status; never infer edges from coincident time samples.
- `observations.csv`: **long-form** `source_id,site_id,asset_id,timestamp_utc,channel,observed_value,unit,origin_kind,quality_status,interpolated,raw_sha256,measurement_boundary` + raw record pointer; never aggregate by erasing origin kind.
- `thermal_interface_evidence.csv`: each row corresponds to a **directional** mechanism and source/circuit, with separate booleans for site, topology, clocks, direct P and EVSE thermals, mechanism and independent test. Automated gate checker prohibits unsupported promotion.
- `equation_register.csv`: original E1/E2/E3/E4, external A1–A5 or T1, physical interpretation, variables/units, initial/boundary conditions, evidence/validation status, equation audit.
- `parameter_register.csv`: model/asset, symbol, units, source, case validity, fit method/partition, bound hit, uncertainty, declared transferability.
- `validation_register.csv`: asset/site/domain, partition IDs, baseline metrics and model metrics, leakage check, interval coverage, run hash, qualified claim.
- `execution_ledger.csv`: gate, run date, test command, PASS/FAIL/BLOCKED, evidence link, blocker, next action.

## Quality and physical invariants

1. For cumulative energy `E_k` (kWh), interval-average `P_k=(E_k-E_{k-1}) / Δt_hours` in kW only with **verified cumulative meter semantics** and adjacent uncontaminated time bins; reject reset/reversal/flagged interpolation.
2. Exogenous ambient temperature is a forcing unless a specific state model justifies it; no pseudo sensor mean estimated from BMS extrema without evidence.
3. `P_station_AC`, `P_grid_import`, `P_connector_DC` and `E_session` may have **different measurement boundaries**. Their apparent difference is not charger electrical loss without fully matched time/boundaries.
4. Published data provider counts, raw records, processed records, complete-case records and interpolated/winsorized records are reported separately.
5. A CSV row lacking source/site/asset/time/channel/unit/origin cannot support validation and should be blocked or placed in a separate exception table.
6. Raw observations never have `origin_kind=SYNTHETIC`. Provisional inferred/calculated quantities must have separate columns and provenance.
7. Measurements from SINTEF, EPFL, OPSD and KU Leuven are **distinct physical installations** unless a real circuit/network link and shared instrumented site are independently evidenced. Never join or correlate across installations as if connected.
