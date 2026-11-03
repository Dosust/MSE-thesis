# Original-field CSV audit — SINTEF Bærug 2024 and STREAM Slovenia 2025 (3 November 2026)

**Thesis:** Engineering of Power–Electrified Transportation Interdependencies for Resilience  
**Scope:** Measured power-system components; **no connected EVSE observations or bidirectional P–Tₑ field validation**. Original CSVs stay in Google Drive, not GitHub. This report does not modify frozen scientific authorities.

## Source-identity and checksum gate — PASS for all three originals

| Field file | Publisher DOI | Source MD5, confirmed from uploaded original | SHA-256 (user upload) | Downloaded raw in thesis Drive |
|---|---|---|---|---|
| `Barug2025_sensordata.csv` (user renamed `Barug2025_sensordata(2).csv`) | https://doi.org/10.5281/zenodo.17223516 | `5d81840a2f901f04fded98c3e1097b6e` | `6aa7384867aace7b9e17778decbbdbde280db1fd7983faee08c259b19e51` | https://drive.google.com/file/d/1sOEtx-Nlr00n_pLqTdWb4BZI6O35m8Nu/view |
| `control_measurements_P_2025.csv` | https://doi.org/10.5281/zenodo.20927130 | `6a7fce6170230bcc73b69ba745509dad` | `8278db817c018cfbfeadb08f980309d70187f07b4c8de4686f8fe1a98c141027` | https://drive.google.com/file/d/1hZ7pCydBAkfnLf4RU2lTu3LozNvuQ4tO/view |
| `control_measurements_Q_2025.csv` | https://doi.org/10.5281/zenodo.20927130 | `7b8a9a608b0489c6227ced8cceb08a59` | `78329c2b4a88b25a752391ccad0834ff23a195ebb0131d9990cac4966c07512e` | https://drive.google.com/file/d/1SQ0ONhiCXK3_Ax--q9j0lUQV7IDACL5I/view |

Checked direct source records: [SINTEF on Zenodo](https://zenodo.org/records/17223516); [STREAM Slovenian P/Q data](https://zenodo.org/records/20927130). All three local MD5 values exactly match publisher file manifests; SHA-256 values identify the precise user-uploaded file bytes. **Checksum integrity does not alone prove instrument calibration or causal interpretation.**

## D01 — SINTEF Bærug operational transformer sensors: raw-file confirmation, NOT a new independent dataset

- Physical system: 40 MVA ONAN power transformer operated in Norway; year 2024; **8,592** hourly source observations with **12 original columns** (timestamp + 11 physical measurements), correct publisher checksum.
- Source data include transformer voltage, current, ambient temperature, top and bottom oil, mid-spot HV/LV, hot-spot HV/LV, clamping force and pressure. This upload is the **measured sensor file**; the separately available `Barug2025_calculated.csv` is **author-generated model output**, not measured data.
- Calendar 2024 includes 8,784 hourly slots. There are **192 missing hourly timestamps in exactly two gaps**: (i) after Jan 3 23:00 to before Jan 10 00:00 (144 missing), (ii) after Dec 16 23:00 to before Dec 19 00:00 (48 missing). No malformed, duplicate or backward timestamps.
- Missing cells in the measured file: **3** HV hot-spot; **3** LV hot-spot; **1,162** clamping-force; **1,162** clamping-pressure. Missing timestamps are different from missing sensor cells.
- Observed ambient range: **-19.58 to +25.97°C**; observed top-oil **3.8275 to 38.86°C**, current **8.4125 to 75.1025 A**. Severe high-ambient extrapolation not experimentally validated.
- **Cross-reference:** existing D01 already had modeling and qualified source data; avoid duplicate counting. A native Google Sheet already contains a source-measured/author-calculated union, but regional-locale number coercion makes it unsafe as authoritative raw numeric input. This newly stored raw CSV is the preferred source.
- Sample timestamps have **unverified time-zone semantics** in the SINTEF file. Do not label them UTC without source confirmation.
- Recommended: re-run temperature-model identification with missingness masks, held-out sequential prediction and predictive UQ; compare persistence and independent test-site outcomes. **Still no EVSE physical connection.**

## D19 — STREAM Slovenia paired operational P and Q measurements: NEW acquired field evidence

- Origin: University of Ljubljana STREAM project, operating MV/LV transformer stations in the Ajdovščina distribution grid, western Slovenia; parent network 20/0.4 kV; **source-declared UTC timestamps** every 15 minutes in 2025.
- Each original CSV: **34,932** data rows, 13 columns (`timestamp` + the same 12 anonymized stations: TR1, TR2, TR3, TR4, TR6, TR8, TR9, TR11, TR12, TR14, TR15, TR16).
- **Exact P–Q join on timestamp and station ID:** all **34,932 timestamps and all 12 station columns match in the same order**. There are **419,184 complete paired per-station P/Q observations**, and **838,368 finite original numeric entries** across the two files. There are zero empty/nonfinite data values in these variables.
- Timestamps are strictly increasing with exactly **900 seconds** between each consecutive observation: **0 duplicates, 0 internal gaps, 0 backwards steps**. Both series cover **2025-01-01 00:00:00 UTC to 2025-12-30 20:45:00 UTC**.
- Full nonleap 2025 has **35,040** 15-minute intervals. These datasets stop **108 intervals (27 hours) before the calendar-year end**; do not state they contain every 2025 interval.
- Both signed P and signed Q appear. Example P ranges: TR6 **-360.84 to 258.16** (units as supplied not confirmed from CSV header); TR16 **-80.96 to 627.56**. Example Q ranges: TR12 **-7.6 to 220.48**; TR15 **-23.44 to 201.0**. Negative active power may indicate reverse-flow, but direction/sign and meter reference conventions need source verification. **Retain original signs; do not clip negative entries as errors.**
- `TR1` etc are anonymized transformer-station IDs, not yet an admitted physical feeder-to-charger map. **Missing:** equipment-specific rated power/impedance, measured bus voltage/current at each station, transformer/charger temperature, protection logs, EV charging service and vehicle departures.
- Source companion **NOT YET ACQUIRED in this audit**: [STREAM transformer technical parameters](https://doi.org/10.5281/zenodo.20927801), particularly `transformer_parameters_anon.csv`; publisher says IDs are consistent. Download, verify MD5 `1742e40ca58121aa637eead4d75e474d`, confirm all 12 station matches, nominal kVA, impedance, and losses before assessing thermal/electrical loading.
- **Important units gate:** Original P/Q CSV headers contain only station IDs, not `kW` or `kvar`. Confirm the physical units/sign convention from publisher documentation before calling `S=√(P²+Q²)` kVA, estimating load-to-rating ratios, or treating P as dissipative heat.

### Admissible engineering path

Conditional to confirmed P and Q units:
```math
S_i(t)=\sqrt{P_i(t)^2+Q_i(t)^2},
\quad \rho_i(t)=S_i(t)/S_{i,\mathrm{rated}}.
```

Then verify nameplate/voltage information and network topology before using `S_i(t)` to infer transformer current or copper losses, and independently calibrate any thermal model. **This is an electrical boundary-condition dataset**, not a transformer thermal trajectory and not an EVSE-coupled field experiment. It contributes to *SO1 component-level electrical loading* and *SO2 conditional feeder/transformer loading*, not observed P→Tₑ or Tₑ→P causality or SO3 field mobility outcomes.

## State-of-research guards

1. Source identity/integrity verified **G1 PASS** for three CSVs; schema/timestamp **G2 PARTIAL/PASS for recorded content**; no known P↔Tₑ physical connectivity **G3 BLOCKED**.
2. Even with authentic measured field data, **SO2 cross-system model remains conditional** and **SO3 service consequences remain model-generated** until verified operating evidence is acquired.
3. STREAM Slovenian 2025 and SINTEF Norwegian 2024 are **separate transformers in separate countries/times**: never synchronize as same-site measured loading and temperature.
4. Do not reuse original files in public GitHub or imply all measurements can be published without checking licence and attribution. GitHub stores only QA findings, source hashes and original Drive pointers.
5. Maintain strict isolation between measured, calculated, inferred and synthetic columns.

### Next action

Acquire and qualify the **708-byte STREAM equipment companion file** with rated `sn_mva`, `vn_hv_kv`, `vn_lv_kv`, `vk_percent`, `vkr_percent`, `pfe_kw` and `i0_percent`; check IDs before model application. The central field-data target remains a **physically mapped transformer–EVSE installation with synchronized electrical+thermal+restriction/service observations**.
