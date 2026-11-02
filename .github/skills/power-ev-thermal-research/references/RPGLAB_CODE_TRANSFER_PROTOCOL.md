# RPG Lab open-source examples — transfer/adaptation protocol

These are **methodological references**, not new thesis field datasets. Preserve attribution, inspect actual GitHub commit/repository LICENSE and dependencies before executing or redistributing code. Website states CC BY 4.0; verify repository-specific rights as well.

| Original verified RPG Lab page | What its page actually documents | Permitted thesis use | Invalid inference |
|---|---|---|---|
| [Distribution Grid with EV / DDCP Python, Fang et al. (2026)](https://rpglab.github.io/resources/DistGrid-EV-DDCP-Python/) | Five sequential Jupyter notebooks: EV loading/violation sensitivity; penetration trigger analysis; line-upgrade baseline; DistFlow + BESS planning; BESS operation validation. Code notes include local Windows input paths and licensed Gurobi requirements. | Learn load-bus allocation, feeder voltage/current constraints, sensitivity/ablation and compare alternative interventions. | A line *thermal loading violation* or benchmark feeder is **not** observed transformer winding temperature, verified EVSE cooling or coupled thermal field evidence. |
| [GNN for Reduced OPF, Pham & Li (2022)](https://rpglab.github.io/resources/GNN-R-OPF_Python/) | GNN/DNN/CNN for screening critical power-flow line constraints; IEEE 73-bus test system; TensorFlow/Spektral and Pyomo. | Learn graph construction and screen candidate active constraints on **documented** network; compare with full OPF solution and deterministic baselines. | Learned graph/constraint saliency **does not identify unknown physical circuit edges** or establish causal transformer–EVSE heat effects. |
| [Feasibility Layer Aided ML for SCUC, Ramesh & Li (2023)](https://rpglab.github.io/resources/FL-ML-R-SCUC_Python/) | ML + feasibility stage for day-ahead security-constrained unit commitment on benchmark networks. DOI `10.1109/TPWRS.2023.3266192` published on lab page. | Study exact vs approximate constraint enforcement, solver feasibility checks and computational baseline reporting. | A SCUC feasibility layer does not directly supply any *charger/transformer derating physics* or thermal field validation. |

## Mandatory reproducibility transfer checklist

1. Confirm original page, verified paper metadata and exact code commit/hash, license, actual released input files, versioned Python/library/solver dependencies.
2. Check benchmark semantics (synthetic grid, AC/DC network, radial feeder, line ratings vs measured temperatures); define what is and is not transferred.
3. Substitute only proven equipment/topology/units from the thesis case. Otherwise run an **illustrative benchmark** with explicit synthetic/benchmark status.
4. Reproduce a baseline with published cases and quantify constraint violation and objective/solver gaps, not just a figure.
5. Predeclare transfer hypothesis and same-test conditions: baseline OPF/DistFlow, direct physics, data-driven surrogate, ML+feasibility.
6. Verify power balance, voltage/current, sign, SOC and thermal equipment laws **only where separately established**, solver status, uncertainty and operational time resolution.
7. Archive source hash, attribution, environment, commands, changed files, errors, time spent and output-register locations.
8. Do not expand the frozen thesis into general economic dispatch, BESS expansion planning, fault studies or generic GNNs without a justified thermal-state/service necessity.

### Required first runnable adaptation

Repeat only the **electrical constraint** part of the DDCP case on its *published example network* (assuming code/data/license/solver accessible) and create `network_feasibility.csv`. Measure numerical residuals under increasing EV load, compare unmodified feeder to line upgrades/BESS as *methodology*, and leave thermometer/thermal-state fields blank unless independent temperature observations and equipment heat law are available. A published benchmark is not a field experiment.
