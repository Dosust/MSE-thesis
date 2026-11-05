# Data acquisition and screening log (2026-11-05)

Current thesis: Engineering of Power–Electrified Transportation Interdependencies for Resilience.

## Documents

- [KIT multivoltage original-file acquisition and audit](KIT_OLTC_22826984_ACQUISITION_AUDIT.md). Mac search, source download, resume errors, three MD5 PASS results, 129.6 million source rows, original columns, 50-day matching time spans, full 129.6-million-row timestamp-grid PASS (zero mismatches), status gates and outstanding verification.
- [KIT campus physical electrical topology evidence audit](KIT_OLTC_ELECTRICAL_TOPOLOGY_EVIDENCE_AUDIT.md). Source-level three-transformer 110/20 kV and multi-branch MV/LV connections confirmed, but exact 110 kV PMU04 to 20 kV PMU01 to 400 V EV SH.J.6 feeder route NOT VERIFIED. Requires node/transformer/switch-map from dataset custodian.
- [EVSE extreme-heat dataset search and portfolio](EVSE_EXTREME_HEAT_REPLACEMENT_SEARCH.md). Qatar original-data availability, study screening, regional repository search, independent component-data options and missing measured thermal validation.
- [Streaming every-row timestamp script](../../../tools/kit_oltc_timestamp_audit.py). Checks each Parquet timestamp against the same 100 ms UTC grid and saves a JSON report. The user independently reported all-row PASS via an earlier inline batch scan; this committed script has no submitted JSON output yet.

## Working checkpoint

KIT is **user-local acquired and original-MD5 verified** (three files). Schemas and row-group time spans have been checked. **Every recorded timestamp matched the expected 100 ms UTC grid (129,600,000/129,600,000; zero mismatches), according to the user's Terminal readback**. Campus-level 110/20/0.4 kV physical architecture is **publisher- and literature-supported**. The **exact three-sensor physical parentage**, independent sensor clock calibration, sensor-level field documentation, thermal mechanisms, and service outcomes remain **OPEN**. The Mac original files are not stored in this GitHub repository.

This working log is governed by [current scope](../../../project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md), [SO1–SO3](../../../project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md) and [non-invention standard](../../../project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md). No frozen thesis authority is amended.
