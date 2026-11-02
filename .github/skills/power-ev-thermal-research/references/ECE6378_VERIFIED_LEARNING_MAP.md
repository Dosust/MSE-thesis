# ECE6378 — Verified learning-to-thesis crosswalk (2 November 2026)

**Primary source:** [Xingpeng Li, ECE6378 ML4PS course page, University of Houston, 2026 Fall](https://rpglab.github.io/resources/ECE6378-ML4PS/) (published October 29, 2026). This is **the source's published outline** and teaching aims, **not** an audit of unavailable lecture slide decks/assignments. Complete editable materials are expected *after* semester end, not currently verified. Recordings for L16–L18 are described as released. L19–L27 are explicitly tentative. This is not evidence of user enrollment, proficiency or completed exercises.

## What the source itself teaches (all 27 lectures)

Read the 27-entry `ECE6378_LEARNING_MATRIX.csv` for each exact lecture number, paraphrased topic, research priority, module, practical exercise, expected output and gate. Source-based categories:

- **L1–5:** introduction, electrical/transmission/distribution fundamentals and research Jupyter environments.
- **L6–8:** meters/data, preprocessing, feature engineering and PCA.
- **L9–15:** linear regression, AC/DC/LAC/DistFlow/N-1, classification/SVM, cross-validation/workflow, short circuit/fault location.
- **L16–18:** MLP/forward pass, gradient/backpropagation, hyperparameters, regularization, optimizers.
- **L19–27 (tentative):** network-based ML/GNN, SCUC/OPF operations, accelerated/embedded optimization, frequency dynamics, RNN/LSTM/GRU time series, KNN/trees/ensembles.

## Course emphasis vs thesis-derived protocol

**Verified on course site:** algorithm suitability, measurement source/resolution, separating train/validation/test, using physical laws and operational constraints to check ML predictions, optimization acceleration/embedding and preference for simpler/physical methods where justified.

**Thesis-specific requirement (ours, not a documented course unit):** actual transformer winding/oil heat ODEs, charger heat management and derating laws, equipment-specific thermal parameter identification, physically connected and synchronized P↔T_e direction evidence, causal identification, coupled viability and electricity/mobility service resilience. These MUST be sourced through the applicable external physics/field literature and active thesis authority. Do not attribute them to ECE6378.

## Ordered practice plan with acceptance tests

| Phase | Lectures | Concrete experiment | Acceptance evidence |
|---|---|---|---|
| A — measured electrical network | L2–8, L10–11 (start L6/7/10/11) | Inspect OPSD two-site import/EV cumulative meters; reconstruct known topology on a *separately identified* network, preserving source flags | QA counts, coherent units, meter interpretation, no invented edges, power-flow residual |
| B — simple and physical comparators | L9, L14 and independently sourced heat physics | Reproduce persistence/linear and ODE component baselines under identical admissible inputs/horizons | No site/session leakage, physical residuals, independent holdout and UQ |
| C — complex methods only if needed | L12–13, L16–18, tentative L19/24–27 | Compare small nonlinearity/NN/time-series methods against B; predeclare claim and uncertainty | Selection only on validation, independent test, error and physical feasibility comparison |
| D — constrained network learning | tentative L20–21, L23 and code examples below | Optimize electrical feasibility on verified graph; compare ML-aided and physics-only solvers | Constraint residual, optimum gap, compute time, original network topology provenance |
| E — conditional thermal-to-service model | additional thermal and systems research, not supplied by course | Map thermal-state→capability→actual service with independently supported constraints | G4–G8 pass separately, or BLOCKED with exact missing data |

**Minimum mathematical exercises** (derive/check, not memorize):

1. Calculate P,Q,S and per-unit base conversions; derive power/energy bounds with the same AC/DC meter boundary.
2. Derive distribution nodal balance and a DistFlow approximation with explicit loss/radial/phase assumptions; compare to AC solution within declared domain.
3. State and verify an electrical *current-rating* constraint, then explain why it is NOT a measured temperature trajectory.
4. Derive ODE and measurement equations from separately evidenced heat-transfer laws; verify dimensional consistency and limiting cases.
5. Write independent time-series split policy, holdout inference information set, and compare M0/M1/M2 on equivalent horizon and feasible operating constraints.
6. Quantify parameter identifiability, prediction uncertainty, out-of-domain heat exposure and service consequences without claiming causal field proof.

## Priority and research fit

P1: L2–4, L6–8, L10–11, L14. P2: L5, L9, L12–13, L16–19, L21, L23–25. P3: L1, L15, L20, L22, L26–27. These priorities are **thesis-derived**, not university course grades or prerequisites. Methodological learning never upgrades G7 field evidence.
