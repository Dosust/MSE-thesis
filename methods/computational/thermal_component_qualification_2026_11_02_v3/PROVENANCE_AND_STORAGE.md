# Thermal component qualification — 2026-11-02 (V3)

**Status:** WORKING COMPUTATIONAL EVIDENCE, not a canonical research amendment.

## Storage and recovery

- Drive dataset root: https://drive.google.com/drive/folders/1qkQIi1YcWDCXiWmNL9mrmxbxsVFHUpgr
- Versioned archive folder: https://drive.google.com/drive/folders/1-wz6XZqCxoLpV7PeQWU8ghu6eI-eojjo
- V3 full archive (source code, source registry, CAN dictionary, split manifests, session QA, predictions, and reports): https://drive.google.com/file/d/18GL8Y8ToO6LEjYYzA6VC53CsZ4k3UF9m/view
- First validation cycle archive: https://drive.google.com/file/d/1GXTRrhNkxAvaZzqZVnbOaa3R0toSl5Rk/view
- KU Leuven sensor diagnostic archive: https://drive.google.com/file/d/1QsI_xCao4nX1qm_qyUmWPZCqHQF92mbw/view

## Original artifact SHA-256 checksums

- Thesis_Drive_Pipeline_V3.zip: `499c0c076f9e7a17d5de172eb2ded74302ac642bfcf0cb1a19619912754cf0ce`
- Thesis_First_Validation_Cycle_2026_11_02.zip: `f317fab6bcff6494fca088bb315a974c11aef5fe0b687c233d6cde0021bb3184`
- KU_Leuven_Sensor_Diagnostics_V2_2026_11_02.zip: `a05d297796392abaa699483c5c5cfacb659f0e6191fc175fe0a3d4e47cc21824`

These are checksums of the source ZIPs verified in the research runtime. The Drive copies should be independently checksummed after retrieval if strict byte-for-byte archive attestation is needed.

## Dataset roles and evidence limits

- SINTEF transformer: measured thermal/electrical time series from a specific 40 MVA device in Norway; transformer component only, model PROVISIONAL.
- KU Leuven BEV: measured AC/DC charging sessions from vehicles in Belgium; vehicle thermal candidate models currently BLOCKED.
- EPFL: measured charging-station electrical and service records in Switzerland; electrical-interface model PROVISIONAL, energy discrepancy unresolved.
- All three are **separate installations**; none proves synchronized same-site transformer–EVSE thermal coupling.
- UrbanEV large archive and additional benchmark are not promoted to coupled-field validation in this run.

## Known blockers and reproducibility rules

1. The vehicle models do not pass the physical-identifiability / independent predictive-validation gate; AC is not consistently better than persistence, DC is data-limited.
2. `BMSdissipation312` is a CAN-decoded signal, not established as measured heat removal; saturation values are flagged.
3. SINTEF 24-hour conditional hindcasts use future observed inputs, not operational predictions; predictive uncertainty and extreme-heat transfer are unqualified.
4. EPFL measurement-vs-session energy discrepancy is not an observed conversion loss until measurement boundaries are reconciled.
5. EVSE internal thermal dynamics and real transformer–EVSE connectivity remain BLOCKED.

To reproduce, obtain the original datasets in the Drive dataset root and use `README.md` plus `run_thesis_data_pipeline.py`. This code does not access Drive automatically; it runs on locally mounted or exported authorized files.

## Governance

This is an additive working research record. Preserve all frozen files under `project/`. Follow `project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md` and current thermal-state-time scope authorities. No synthetic-data result here is upgraded to field-validated evidence.
