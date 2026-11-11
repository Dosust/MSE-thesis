# Report 3: SINTEF state evolution, hot-spot observations, and aging gate

## Chronological model outcome

- 6,012 training pairs; 2,576 holdout pairs; 8,592 observed records.
- Effective time constant **10.9825 h**; offset **13.4806 °C**; gain at **training-median current Iref = 22.25875 A:** **0.4747 °C**. The previous run's gain used a different reference current, so do not compare numerical gain values without unit-normalizing.
- Holdout model RMSE **0.216529 °C**, MAE **0.149854 °C**; persistence RMSE **0.251699 °C**, MAE **0.144981 °C**. Model improves RMSE and worsens MAE.
- Maximum recorded ambient **25.97 °C**; zero observed hours at/above 30 °C. The model does not validate extreme-heat behavior.

## Time-state permutation, new experiment

From **106** distinct 24-hour uninterrupted holdout windows:

- Constant for each model scenario: same initial T, same 24 observed ambient values in their original order, same 24 observed current values permuted.
- Invariant: sum of normalized squared current, which is a conditional current-heating proxy.
- Median absolute *final* oil temperature difference, descending vs ascending current sequence: **0.354859 °C**.
- Median absolute *maximum* oil-temperature difference: **0.218256 °C**.
- Largest absolute final difference: **0.742560 °C**.

This demonstrates the temporal weighting of the **fitted reduced physical model**, not observed intervention effectiveness or measured EV-load thermal propagation. See `sintef_load_order_cases.csv` for every heldout window, and `sintef_load_order.png` for the distribution.

## Winding temperature sensor questions

| Measurement | Paired records | Fraction below measured top-oil | Measured temperature range | Empirical p95 |
|---|---:|---:|---|---:|
| HV named 'Hot-spot' | 8,589 | **84.11%** | 5.64–30.31 °C | 26.448 °C |
| LV named 'Hot-spot' | 8,589 | **70.94%** | 8.90–30.51 °C | 26.951 °C |

Measured winding sensor readings can differ from the theoretical maximum winding-temperature location; a lower reading is not by itself evidence of a faulty sensor. The relationship is a reason to **verify instrument positions, measured versus calculated hot-spot definitions and the insulation model** before applying an aging acceleration coefficient.

**No equipment-specific thermal limit or insulation-aging rate has been established.** The p95 values above are data distribution descriptors, never safety thresholds or remaining-life estimates. The candidate aging law cannot be used to claim genuine life loss without verified transferability.

## Scientific interpretation

Reduced ODE predictions are consistent with finite effective thermal inertia and explain why the *ordering* of load exposure can matter. Period-specific time constants may reflect different ambient-current correlations, load excitation, unmodeled states, sensor biases or changes in the model's validity domain. Calendar variation must not be conflated with proof of structural non-identifiability. Aging and extreme-heat propagation remain blocked; no thermal P-to-transport or transport-to-P causation observed here.

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
