# KIT PHIL five-EV phase-aware quantitative audit — V2

**Correction:** Inactive zero phase channels must not dilute single-phase EV RMS voltage/current. V1 is retained unchanged for auditability.
**Source:** https://doi.org/10.5281/zenodo.22965111; all files must pass source MD5.
**Evidence boundary:** U and I measured; VA proxy is not real W; event time inferred, no command-state log; different source from KIT OLTC field.

| EV | Active phases | V1 mean-all-phase candidates | V2 phase-aware candidates | Near t=0 ΔU (V) | Near t=0 ΔI (A) |
|---|---:|---:|---:|---:|---:|
| Volkswagen ID.4 | 3 | 16 | 16 | -5.0033 | 0.0 |
| Nissan Leaf | 1 | 0 | 16 | -4.98 | -0.06 |
| MG4 | 3 | 16 | 16 | -5.0033 | 0.0033 |
| Tesla Model 3 | 3 | 16 | 16 | -5.0133 | 0.07 |
| Renault Zoe | 3 | 16 | 16 | -5.01 | -0.03 |

**Event-wise measured voltage and current changes, detector timing and phase-specific changes:** see V2 JSON.
**Causality status:** controlled voltage perturbation test context, but exact source commands and charger state not recorded in these CSVs. No field KIT OLTC event attribution or thermal inference.
