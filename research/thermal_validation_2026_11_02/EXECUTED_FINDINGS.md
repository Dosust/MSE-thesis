# Executed physical-data research audit — 2026-11-02

**All output is component-level. Field-validated coupled thermal model: BLOCKED.**

## Raw integrity
- Original SINTEF source files authenticated against the publisher MD5 in `01_provenance/source_registry.csv`.
- KU Leuven: 134 charging CSV files, 109 AC and 25 DC, session SHA256 registry.
- Raw files remain unmodified. Calculated SINTEF data are not used as independent measured truth.

## KU Leuven: session-separated 15-minute conditional hindcast
| Vehicle / mode | Test RMSE °C | Nominal 90% interval empirical coverage | Gate |
|---|---:|---:|---|
| BEV1 AC | 0.427 | 53.1% | BLOCKED |
| BEV2 AC | 0.741 | 78.3% | BLOCKED |
| BEV2 DC | 17.192 | 30.4% | BLOCKED |

The maximum BMS temperature sensor is not an independently observed lumped thermal state. Model uses *future observed* current and ambient. Charging power sign/scale and vehicle cooling mechanisms are not yet identified.

## SINTEF: 24-hour conditional hindcast
- Top oil: 1.008 °C RMSE vs persistence 2.002 °C (PROVISIONAL).
- HV hotspot: 3.377 vs persistence 1.710 °C (REJECT).
- LV hotspot: 3.219 vs persistence 1.755 °C (REJECT).
No power-system thermal transfer to a hypothetical distribution transformer is justified. Late-period error bands are descriptive, because evaluation windows overlap.

## EPFL minute-level charging interface
- Actual populated measurements: 61,816 vs documented 64,277; unresolved difference 2,461.
- Reconciled 1,878/1,878 session IDs after time-verified CCS2 global offset of 1,129.
- Both connectors observed concurrently at 6,897 minute stamps; sum above stated 172.5 kW at 111 minute stamps (interpret only after meter/plant boundaries established).
- Median source `P(W)` integration / source Session Energy ratio on 1,878 complete no-gap sessions: 1.150. This is an unresolved consistency difference, **not** efficiency.

## Remaining blockers
- No original **EVSE internal thermal measurements** in the Drive portfolio.
- No proof of **same-site transformer→feeder→charger physical topology** or common timestamps.
- No admitted charger model-specific derating and auxiliary loss law.
- No verified thermal threshold, operational resilience service requirement or measured propagation delay.
- Existing UrbanEV derived energy, Turkish network benchmark and generic resilience CSV cannot substitute for matched field thermal observations.

## Accept/reject rule
All 8 stage results are recorded in `acceptance_gates.csv`. No stage gets PASS merely because executable code ran. The next experiment is diagnostic, not a new accepted synthetic dataset.
