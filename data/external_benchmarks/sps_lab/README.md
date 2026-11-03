# SPS Lab data and source evidence audit — 2026-11-03

**Thesis:** Engineering of Power–Electrified Transportation Interdependencies for Resilience (canonical V3).  
**Evidence status:** MODEL BENCHMARKS / SOURCE DATA ONLY. **No measured transformer–EVSE thermal field validation.**

## Evidence-qualified decisions

| ID | Dataset | What was actually inspected | Admissible use | Status |
|---|---|---|---|---|
| SPS-CYP-LV-001 | [Cyprus LV suburban Network1](https://github.com/SPS-L/Cyprus-Grids/blob/main/LV_Suburban_Network/Network1.ipynb) | 315 kVA 11/0.4 kV transformer, three feeder networks (24, 8, 29 distribution buses), 109 three-phase customer load nodes, impedances, transformer parameters | SO2 electrical-network benchmark **after independent power-flow verification** | PROVISIONAL — source model, not field data |
| SPS-PYE-5BUS-001 | [PyEPlan 5-bus case](https://github.com/SPS-L/pyeplan/tree/master/examples/5_bus) | Four serial edges 0→1→2→3→4; 3-by-5 demand matrices; generator, time and distance files | Small numerical-input QA, cross-checking parameter semantics | PROVISIONAL — source model, not field data |
| SPS-TSOC-TOOLS-001 | [TSOC-data-analysis](https://github.com/SPS-L/TSOC-data-analysis) | CLI and Python API for grid operations data analyses | S03 software methodology | METHODS ONLY; original operational measurements not demonstrated in this audit |
| SPS-DYNAGNN-001 | [DYNAGNN](https://github.com/SPS-L/DYNAGNN) | Graph-learning code/checkpoint workflow for dynamic activity and adaptive reduction | Optional S05/S06 method | METHODS ONLY; not transformer/charger thermal evidence |

## Direct inspection: Cyprus Network1
- The notebook constructs a PandaPower model with **315 kVA** rated transformer, **11 kV / 0.4 kV**, and explicit impedances.
- Feeder distribution buses: 24 + 8 + 29 = **61**. Load buses: 48 + 32 + 29 = **109**. Baseline load inputs per customer per phase: **0.0004 MW** and **0.000132 Mvar**. Their arithmetic total is **130.8 kW** and **43.164 kvar** *before electrical losses and any hypothetical EV charging*.
- Although the project targets *unbalanced* LV analysis, the notebook's **default load values are equal across phases**. It **does not call a numerical power-flow routine**. Published unbalanced or EV results must be independently reproduced, not inferred from the notebook.
- No EVSE is instantiated and no measured ambient, transformer thermal, or charger thermal series exists in the inspected notebook. It does not establish real transformer→EVSE topology.
- Source blob: `8db604feb7bb70d6b307e77662fd54533c095060`; [license MIT](https://github.com/SPS-L/Cyprus-Grids/blob/main/LICENSE); [cited data DOI](https://doi.org/10.5281/zenodo.17232114).

## Direct inspection: PyEPlan 5-bus
- `elin_dist.csv`: 4 branch rows; `pdem_dist.csv`: 3×5 values; `qdem_dist.csv`: **identical content** to `pdem_dist.csv` (same upstream Git blob SHA). Verify before any physical active/reactive interpretation.
- `dtim_dist.csv`: `dt=365.0`, **unit/semantics unqualified** from CSV alone.
- `cgen_dist.csv`: one generator at bus 0. `rou_dist.csv`: four connectivity/distance rows; route distances **do not establish charger-to-transformer physical topology**.
- `cblt_dist.csv`: 150 cross-section row contains `i5=4036`, suspicious relative to nearby rows. **Quarantined from selected inputs; do not auto-correct**.
- Source files copied under `pyeplan_5bus/` unmodified, with upstream `LICENSE.txt` (Apache-2.0). Upstream provenance is recorded in `source_register.csv`.

## Scientific use / gate

**PASS:** source existence and source-content inspection.  
**NOT YET TESTED:** full network power-flow reproducibility, three-phase unbalance validation, EV integration.  
**BLOCKED:** synchronized field-observed transformer hot-spot/oil and EVSE internal temperatures, AC/DC charger power, ambient heat, actual equipment connectivity, clocks, EV departure demand and interdependency propagation delays.

Use **SO1** only to register hypothetical vs verified physical mechanisms. Use **SO2** for a *conditional* electrical network benchmark after numerical verification. Do not present **SO3** measured thermal service/resilience results from these data.

Next: validate Cyprus power-flow model using a justified unbalanced solver, document power and unit balances; then introduce clearly *hypothetical* EV charging at an identified benchmark bus; continue separate measurement acquisition for thermal calibration/validation.

This report does not change canonical thesis governance or frozen research documents.
