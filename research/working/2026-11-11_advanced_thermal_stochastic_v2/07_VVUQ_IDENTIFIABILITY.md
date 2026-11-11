# Report 7: Numerical verification, inverse-model conditioning, and uncertainty

## Conditional ODE numerical verification

The fitted first-order thermal equation has an analytic one-hour zero-order-hold response. For a declared **dimensionless fixed-forcing test**, explicit Euler and RK4 were evaluated against exact integration:

| Substeps/hour | Euler abs error (dimensionless) | RK4 abs error (dimensionless) |
|---:|---:|---:|
| 1 | 2.5341e-03 | 3.2366e-08 |
| 2 | 1.2283e-03 | 1.9475e-09 |
| 4 | 6.0496e-04 | 1.1943e-10 |
| 8 | 3.0024e-04 | 7.3937e-12 |
| 16 | 1.4957e-04 | 4.5991e-13 |

Convergence is evidence about solver correctness for the selected ODE, *not* the validity of the transformer heat-transfer assumptions.

## Local inverse conditioning

The centered finite-difference sensitivity matrix used coordinates log(tau), temperature offset, and current-square gain. Its unit-column singular values are **1.308459, 0.998367, 0.539627** and standardized condition number **2.4247**.

**Important negative finding:** This three-parameter one-step fit is **not nearly singular** under this *local column-normalized* sensitivity diagnostic. Claims of proven nonidentifiability from calendar drift alone would be unsupported. However, normalized conditioning does not establish global uniqueness or correct thermal laws. The tau profile is provided in `sintef_tau_profile.png` and full `RESULTS.json` but is **not** a formal likelihood-based interval.

| Period | Pairs | Effective tau (h) | Measured ambient range (°C) |
|---|---:|---:|---|
| Jan-Apr | 2,758 | 15.9818 | -19.58 to 16.22 |
| May-Aug | 2,951 | 8.2944 | 6.99 to 25.97 |
| Sep-Dec | 2,878 | 13.5708 | -5.86 to 25.34 |

The periods have different ambient and charging-current distributions, so the observed tau variation is not a controlled parameter-identifiability proof. Plausible alternatives include model-form inadequacy and forcing-dependent effective dynamics.

## Chronological residual interval experiment

- Fit: 5,153 initial sequential one-hour pairs (60% of source rows, excluding gap-crossers).
- Calibrate using 1,717 subsequent pairs.
- Evaluate against 1,717 later pairs.
- Nominal two-sided 90% absolute-residual radius: **0.390310 °C**; observed subsequent coverage: **95.282%** and fixed full width **0.780619 °C**.

This differs from the prior model/split's **90.7%** coverage and from the earlier parameter-only 90% band's approximately **8%** coverage. These experiments have different calibration constructions and must not be treated as interchangeable. Sequential calibration/evaluation observations are temporally dependent; no rigorous exchangeability or high-temperature coverage guarantee has been established. Measurement noise, modeling discrepancy and future forcing are not fully quantified.

## Extrapolation and safe interpretation

The maximum SINTEF measured ambient temperature is **25.97 °C**. Thus all 30°C-plus scenarios are outside measured support and are not empirical validation. No qualified insulation-aging operating threshold permits honest critical transition time or remaining-life inference.

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
