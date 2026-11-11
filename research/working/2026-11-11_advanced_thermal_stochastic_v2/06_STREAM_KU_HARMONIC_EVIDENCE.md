# Report 6: KU Leuven, STREAM electrical states and harmonic evidence gates

## KU Leuven BMS-reported pack temperature

| Original file | Records | BMS 'max pack temperature' observed numeric range | Timestamp reversals |
|---|---:|---:|---:|
| `Figure6_AC1.csv` | 7,598 | 23.25–27.75 | 5 |
| `Figure6_AC2.csv` | 4,252 | 25.00–27.25 | 6 |
| `Figure7_AC1.csv` | 15,083 | 27.75–30.50 | 0 |
| `Figure7_AC2.csv` | 13,940 | 27.75–33.00 | 1 |

Total **40,873** readings across four AC testing files; **12** backward timestamp transitions. The source reports BMS pack signals; no independently qualified internal charger rectifier or transformer oil/winding temperature can be inferred. The ranges should be interpreted as **native numeric values with likely temperature semantics from the column names**, requiring instrument specification for certified °C applicability.

A component electrothermal time-constant fit is not promoted until test boundaries and clock reversals are resolved. Thermal charger derating, measured charger losses, and Power-to-transport service propagation remain unproven.

## STREAM Slovenia electrical P and Q

Matched **34,932** timestamps at **12** named station channels, **419,184** paired numeric P/Q entries. The station channel semantics and units are still subject to source verification.

| Station | Median P native | Median Q native | Median numeric sqrt(P²+Q²) | Fraction Q below zero |
|---|---:|---:|---:|---:|
| TR1 | 221.24 | 9.04 | 221.62 | 0.029 |
| TR2 | 153.48 | -6.60 | 154.09 | 0.664 |
| TR3 | 45.32 | -9.60 | 47.15 | 0.776 |
| TR4 | 76.96 | -8.32 | 78.53 | 0.580 |
| TR6 | 86.56 | -24.52 | 96.18 | 0.719 |
| TR8 | 53.72 | 1.60 | 54.04 | 0.381 |
| TR9 | 64.32 | 15.16 | 67.61 | 0.027 |
| TR11 | 40.88 | -9.84 | 42.24 | 0.976 |
| TR12 | 87.68 | 45.32 | 118.22 | 0.062 |
| TR14 | 49.08 | -7.00 | 49.66 | 0.823 |
| TR15 | 86.60 | 62.10 | 132.87 | 0.191 |
| TR16 | 187.38 | 45.88 | 193.36 | 0.361 |

The third numeric column is only a norm in **source-native units**, *not confirmed apparent power in kVA*, because P/Q unit compatibility, station signs, equipment ratings and voltage boundaries are not qualified. No feasible charger reactive-power compensation can be inferred. This is electrical-component analysis, not a measured thermal mechanism.

## Harmonically induced transformer losses

**Blocked:** neither the audited 15-channel KU Leuven AC record nor the STREAM P/Q power rows supplies a verified harmonic amplitude spectrum, current THD, winding resistance/frequency-dependent stray-loss law or measured feeder transformer response. A P/Q pair is mathematically insufficient to identify higher-order waveform harmonics. The 2003 Gómez and Morcos research motivates future waveform qualification, not a current result.

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
