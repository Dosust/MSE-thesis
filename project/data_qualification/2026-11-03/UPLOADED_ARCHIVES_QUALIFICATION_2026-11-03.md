# Qualification of Two Newly Uploaded Research Archives — 2026-11-03

**Project:** Engineering of Power–Electrified Transportation Interdependencies for Resilience  
**Evidence status:** Source-authenticated auxiliary/component datasets; **NO demonstrated physically connected transformer–EVSE thermal validation**.  
**Archive handling:** Original ZIP bytes kept in Google Drive; only source pointers, hashes and derived QA results are recorded here. This document does not modify frozen research claims.

## Source A — D17: KU Leuven EV charging datasets

- **Dataset:** Aboubacar Yasko, M.; Driesen, J.; Martinez, W. (2025). *EV charging datasets*. KU Leuven RDR, version 1. DOI: https://doi.org/10.48804/C5PT0R
- **License on repository:** CC BY 4.0.
- **Original submitted ZIP:** `doi-10.48804-c5pt0r.zip`; SHA-256 `8d52252aff2ec78f9967c96f728dbc5df55948a6ab15fdd1565318236e0d0aa9`.
- **Authenticated source:** All ten dataset payload files matched individual MD5 checksums published by KU Leuven (five XLSX, four CSV, one README; a separate ZIP manifest was also present); ZIP CRC passed.
- **Drive original:** https://drive.google.com/file/d/1zYktMEjoqXu-ZheGW8HGATwx23_lAcjH/view
- **Source context:** Experimental real-vehicle AC/DC charging research at EnergyVille. Both measured and processed/averaged signals occur; precise metering, synchronization, input/output boundaries and signal units still require the accompanying method description.

### File-level computational screening

| Original file | Numeric records | Measured fields / QA flags |
|---|---:|---|
| Figure6_AC1.csv | 7,598 | AC charger line power, V/I, vehicle battery V/I, SoC and pack temperature; **5 backward timestamp steps** |
| Figure6_AC2.csv | 4,252 | Same channels; **6 backward timestamp steps** |
| Figure7_AC1.csv | 15,083 | Same channels; chronological 1-second steps in file order |
| Figure7_AC2.csv | 13,940 | Same channels; **1 backward time jump**; about **10.34% missing** `TotalChargeKWh3D2` entries |
| Figure10.xlsx | 111 + 147 | Two 30-second AC-input/DC-output/vehicle-battery power traces, battery thermal state; second test **suspected current/voltage channel-header swap** |
| Figure13.xlsx | 1,521 + 2,887 + 2,889 | 150-kW-label charging tests; DC/battery power and vehicle temperature; **no time column** and sample interval not admitted |
| Figure1, Figure4, Figure11.xlsx | Small summary sheets | Vehicle technical categories and summary electrical-efficiency quantities; not new independent installations |

Total AC CSV records: **40,873** (not 40,873 independent charging sessions).

Calculated **within-file** median ratio `max(0, -V_batt I_batt)/(1000 P_AC)`:
- Figure6_AC1: 0.9282
- Figure6_AC2: 0.9357
- Figure7_AC1: 0.9470
- Figure7_AC2: 0.9469

`ChargeLinePower264` is treated provisionally as kW; `BattVoltage132` as V and negative `RawBattCurrent132` as charging battery current A. **Unit convention and vehicle auxiliary loads must be verified before interpreting these ratios as total efficiency.**

Calculated **within-file** median DC fast-charger conversion ratio `P_DC/P_AC` in Figure10:
- EV1_DC1: **0.9261** (111 points)
- EV1_DC2: **0.9262** (147 points)

For illustrative high-input-load observations where recorded AC power exceeded 30 kW and DC output exceeded 20 kW, median measured **AC-minus-DC power**:
- EV1_DC1: **3.589 kW** (87 points)
- EV1_DC2: **3.549 kW** (116 points)

These are **electrical power-balance differences**, not measurements of heat rejected by a particular EVSE element. They may support a conditional converter-loss heat-source model **only after confirming measurement boundaries, switching/auxiliary losses and applicable energy accounting**.

**Additional quality block:** In Figure10 EV1_DC2 the median purported `FC_dcCurrent` is approximately 368 while `FC_dcVoltage` is approximately 123, whereas the vehicle battery voltage is approximately 368 V. In EV1_DC1 corresponding medians are about 123 A and 369 V. This suggests a current/voltage label swap for EV1_DC2; the raw file was not modified, and the mapping must be checked against the authors' instrumentation record.

**Independence block:** D17 and already registered D02 (KU Leuven `10.48804/8KPDTW`) originate from the same research environment. Their measurement-session overlap and hardware identity have not been ruled out; D17 must not be called independent external validation of D02.

**Admissible thesis use:** SO1 charger/vehicle electrical boundary and battery-response mechanisms; SO2 conditional P-to-electrified-transport model parameterization or sensitivity/ablation. **Not admissible:** empirical transformer–EVSE thermal interdependency, observed EVSE internal derating/protection dynamics, independent model validation without overlap audit, or SO3 field service outcomes.

## Source B — D18: Mendeley transformer infrared images

- **Dataset:** Najafi, M.; Baleghi, Y.; Mirimani, S. M. (2021). *Thermal images dataset, Transformer, 1 phase dry type*, version 3. DOI: https://doi.org/10.17632/8mg8mkc7k5.3
- **License:** Repository listing CC BY 4.0; bundled README also reserves rights and requests citation, so preserve source attribution.
- **Original submitted ZIP:** `8mg8mkc7k5-3.zip`; SHA-256 `2a2cb52a39ff264bad1ba9f5aadab62f03bf7f73ac9b484090672030989391e7`; ZIP CRC passed.
- **Drive original:** https://drive.google.com/file/d/1edhFUnQnM6nU5xtr1HPolQDMDBmuwY_G/view
- **Camera and setup (bundled PDF):** Dali-tech thermal camera; 1-kW, 220-V, single-phase dry-type transformer; nominal ambient 23°C; healthy condition and eight experimentally introduced winding short-circuit configurations.

### Internal archive inspection

- `IR_trans_bmp.rar`: **255 color BMPs** across 9 test/fault categories, each inspected sample 320 × 240 RGB, plus one README text file.
- `Ground-truth-Transformer.rar`: **45 expert segmentation mask BMPs** under `gt` paths and **45 corresponding image/reference BMPs** under `lastsumtest`; these 90 stored BMPs do **not** equal 90 independent segmentation annotations.
- RAR archive listings were parsed and representative BMPs decoded and checked (not a pixel-by-pixel audit of all 255 images).

**Physical limits:** These are colorized infrared **images**, not radiometrically calibrated temperature fields or time-resolved transformer oil/hot-spot records; the single reported ambient setup (23°C) is **not an extreme-heat experiment**. Induced bench faults are not a field-scale transformer thermal-derating experiment.

**Admissible use:** Background or exploratory computer vision for laboratory transformer fault localization and annotated segmentation. **Not admissible:** transformer thermal ODE calibration, distribution-transformer hot-spot prediction, field extreme-heat transfer, EVSE temperature evidence, or P↔T_e validation.

## Scientific status of the combined uploads

| Thesis objective | Newly supported | Still blocked |
|---|---|---|
| SO1 | Additional AC/DC charger electrical conversion and vehicle battery-temperature observations; transformer visual-fault background | No verified charger-to-transformer asset mapping, same-site clocks/temperature measurements or actual thermal restrictions |
| SO2 | Conditional converter-loss parameterization and sensitivity tests are possible | No independently validated connected thermal equations/coefficients; no direct charger heat/derating telemetry |
| SO3 | Electrical-loss inputs can enter a bounded scenario if sources/assumptions are qualified | No observed electricity–mobility service consequences or comparable field sustainability impacts |

**Critical non-conflation:** Do not synchronize D01 SINTEF transformer time series with D17 KU Leuven charging records as though obtained from a common installation. Common ambient exposure and direct causal coupling also must remain distinct.

## Priority follow-up

1. Obtain the charging experiment's instrumentation/definition of `ChargeLinePower264`, AC input, charger DC output, onboard auxiliaries, battery charging-current sign convention and DC2 voltage/current column mapping.
2. Correct **analysis copies only** by sorting/segmenting timestamp discontinuities; document the algorithm, preserve originals and verify the 1-second observation claim where applicable.
3. Compare vehicle/test identifiers and session metadata with D02 to establish independent validation eligibility.
4. If supported, estimate a power-dependent charger-loss function with uncertainty and test against independent charger boundary measurements; avoid interpreting loss as heat without a thermal balance.
5. Keep higher-priority acquisition focused on verified physical transformer–EVSE connections with synchronized electrical, thermal and protection/derating telemetry.

**Disposition:** D17 = **high-value, provisionally admissible component evidence**; D18 = **low-priority supplementary measured imaging**. Neither closes the thesis's central observed P↔T_e thermal-coupling gap.
