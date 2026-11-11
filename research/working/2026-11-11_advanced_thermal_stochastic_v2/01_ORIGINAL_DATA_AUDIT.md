# Report 1: Original Google Drive dataset audit

**All six original measurement files were already available locally as authenticated Drive-backed sources and were reopened for this run.** No externally retrieved empirical file was used.

| Original file | Bytes | SHA-256 |
|---|---:|---|
| `SINTEF_Barug2025_sensordata_original_MD5verified_2026-11-03.csv` | 873,041 | `6aa7384867aace7b697b9e17778decbbdbde280db1fd7983faee08c259b19e51` |
| `Session_data.xlsx` | 204,514 | `b886943bf86520f24f5a53870886c4c43709d265cbebdd65e1345321e22cc192` |
| `Measurement_data.xlsx` | 23,558,382 | `a0a489e2897ec79235ed914376ab7751ab21c68418543234a60042eaee73a89c` |
| `KU_Leuven_C5PT0R_Measured_EV_Charging_Efficiency_UserOriginal_2026-11-03.zip` | 2,082,895 | `8d52252aff2ec78f9967c96f728dbc5df55948a6ab15fdd1565318236e0d0aa9` |
| `STREAM_Slovenia_control_measurements_P_2025_original_MD5verified.csv` | 3,505,062 | `8278db817c018cfbfeadb08f980309d70187f07b4c8de4686f8fe1a98c141027` |
| `STREAM_Slovenia_control_measurements_Q_2025_original_MD5verified.csv` | 3,978,067 | `78329c2b4a88b25a752391ccad0834ff23a195ebb0131d9990cac4966c07512e` |

## Eligibility and limitations

| Source | Rows | Existing physical observations | Status and unresolved provenance |
|---|---:|---|---|
| SINTEF 2024 transformer | 8,592 | hourly current, voltage, ambient, top/bottom oil, winding sensors | QUALIFIED_COMPONENT (reduced thermal state only); 192 absent hours in two gaps; no verified matched EVSE; no ambient at or above 30 °C |
| EPFL two CCS connectors | 1,878 sessions; 61,816 populated minute-power records | session start, end, delivered energy, power measurement | QUALIFIED_INTERFACE for recorded station power and conditional offline scheduling; measured session energy and integrated power disagree; no confirmed true driver energy requirement or feeder transformer |
| KU Leuven AC charging | 40,873 | BMS pack-temperature readings, charging electrical channels | PROVISIONAL / QUALIFIED_COMPONENT for descriptive pack data only; 12 timestamp reversals; AC/DC metering alignment unresolved; not EVSE rectifier temperature |
| STREAM Slovenia | 34,932 timestamps per P/Q file; 419,184 station-pairs | 12 matching P/Q station channels | PROVISIONAL. Source units, signs, nameplates, thermal states, EVSE mapping unresolved |

**Measured versus derived:** All numbers above are data records and numerical summaries; model-fitted thermal parameters, modeled charging schedules, empirical sample quantiles and projected interval coverage are *derived*, not direct sensors. 'Measured' must not be attached to modeled peak reductions or permuted-load temperature changes.

**EPFL reconciliation:** total session-reported energy: **60441.94 kWh**; contiguous-integrated minute-power energy: **69771.60 kWh**; median absolute fractional energy discrepancy **15.33%**. Only **3.19%** of matched sessions agree within 10%. This does not establish conversion efficiency, electrical losses or meter malfunction; boundaries/processing require original-method verification.

**Harmonic-data gate:** neither STREAM P/Q nor the audited KU Leuven 15-field AC time series by itself establishes a frequency-domain current spectrum. No qualified same-site transformer aging spectral input has been found among these six admitted originals. The wider Drive archive has not been exhaustively proven absent of all possible waveforms.

## Source and authority references

- SINTEF original monitored transformer sensor file, checksum in `ORIGINAL_INPUT_MANIFEST.json`; data description: [Bærug transformer measurements](https://doi.org/10.5281/zenodo.17223516). User-owned original Drive record, not redistribution.
- EPFL original `Measurement_data.xlsx` and `Session_data.xlsx` user-owned Drive copies. See previously audited source register in GitHub. 
- KU Leuven C5PT0R measured EV charging efficiency original archive, authenticated Drive copy. 
- STREAM Slovenia 2025 active/reactive transformer-station monitoring CSV copies, authenticated Drive archive.
- [Qian, Zhou & Yuan (2015), DOI 10.1016/j.ijepes.2014.09.040](https://doi.org/10.1016/j.ijepes.2014.09.040) (abstract and user-supplied summary; full methodological reproduction not claimed).
- [Visakh & Selvan (2022), DOI 10.55730/1300-0632.3819](https://doi.org/10.55730/1300-0632.3819) (published charging scheduling/aging method; no exact reproduction).
- [Pavlićević & Mujović (2022), DOI 10.3390/en15197085](https://doi.org/10.3390/en15197085) (power flow and transformer aging methodology; no exact reproduction).
- Gómez & Morcos (2003), *Impact of EV battery chargers on the power quality of distribution systems*, IEEE Transactions on Power Delivery 18(3), 975–981. Original harmonic spectra required for transfer to Drive data.
- Nishanth (2026), *Physics-Informed Neural Networks for Transient Thermal Analysis and Insulation Life Assessment in Power Transformers*, DOI 10.1109/NE-IECCE69680.2026.11665934. Only available abstract-level method information; AI/PINN is excluded under this thesis's physics-first authority.
- GitHub current authority: [thesis title V3](https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/CANONICAL_THESIS_TITLE_V3.md); [objectives SO1–SO3](https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md); [evidence non-invention standard](https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md); [physics first scope](https://github.com/Dossiya-SE/MSE-thesis/blob/main/project/PHYSICS_MATHEMATICS_FIRST_HYPOTHESIS_TESTING_SCOPE_DIRECTIVE_V1.md).
