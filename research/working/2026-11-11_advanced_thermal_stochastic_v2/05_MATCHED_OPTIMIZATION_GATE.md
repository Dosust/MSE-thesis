# Report 5: Matched charging scheduling optimization and thermal-objective feasibility gate

## Re-executed EPFL LP, actual inputs

`epfl_reproduce.py` was rerun against original Drive-backed XLSX files and logged in `EPFL_REPLAY_LOG.txt`. It verified 1,878 sessions, matched source session IDs, decoded 61,816 populated power readings and solved the same 16 selected high-use dates.

| Quantity | Result |
|---|---:|
| Days optimized | 16 |
| Session-day occurrences | 232 |
| Median front-loaded-vs-optimized peak difference | **44.0092%** |
| Maximum LP delivered-energy numerical shortfall | 4.974e-14 kWh |

**The two profiles are counterfactuals.** The LP baseline is a hypothetical one-minute front-load at the session-recorded maximum, not actual logged charging power. The optimization preserves observed achieved session energy *as a declared constraint*, but that energy is not a verified user's charging request. Equipment-level operability, control dynamics, and site-transmission constraints beyond the recorded session timing and declared per-session maxima are not proven.

## M2 thermal-constrained optimization: blocked by missing interface mapping

A valid transformer temperature objective requires an EPFL-specific transformer/network model or a fully qualified transferable mapping from charging AC power and base demand to oil/winding temperature. SINTEF data are from a separate 40 MVA transformer and no source-qualified shared bus/feeder, compatible equipment class, baseline load, charger control or ambient/thermal state links the installations. In addition, observed EPFL session-energy and minute-power integration disagree.

**Disposition:** `BLOCKED_EVIDENCE`. Do not report a numerical thermal-optimal versus peak-optimal trade-off or transformer aging reduction. The matched mathematical formulation remains available in `02_EQUATIONS_AND_HYPOTHESES.md` pending a justified transfer study.

## Conditional science next gate

A valid future M2 needs: (i) documented transformer with nameplate/thermal laws; (ii) base-load and power-factor measurements; (iii) feeder topology and EVSE linkage; (iv) EVSE charger and customer/service capacity constraints; (v) ambient/initial state and heat-transfer consistency; (vi) numerical verification of discretization, feasibility and nonconvex solution status; (vii) matched uncertainty across M0/M1/M2.

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
