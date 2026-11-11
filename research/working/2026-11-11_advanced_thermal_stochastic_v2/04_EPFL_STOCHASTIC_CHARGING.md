# Report 4: EPFL original-session stochastic characterization

**Original session records:** 1,878, across two CCS connectors (1,129 CCS1; 749 CCS2). **Original populated one-minute power rows:** 61,816, not the larger sparse worksheet row extent. The first 1,129 session IDs are CCS1 and the remaining IDs require a connector-specific offset for power-record matching, as verified by the original replay.

## Descriptive joint behavior

| Statistic | Result |
|---|---|
| Observed session stay duration, 10th / median / 90th percentile (h) | 0.200, 0.483, 0.883 |
| Recorded achieved session energy, 10th / median / 90th percentile (kWh) | 11.052, 29.367, 55.479 |
| Arrival hour, 10th / median / 90th percentile (local source clock, unverified time zone) | 9.017, 15.183, 20.738 |
| Recorded session maximum-power field, 10th / median / 90th percentile (kW) | 51.615, 97.655, 160.074 |
| Spearman stay duration versus recorded energy | **0.6638** |

The positive association does not imply why sessions ended or that more flexible scheduling is operationally available.

## Empirical day-block bootstrap

**1,865** completed sessions in a single calendar day, over **221** such observed days. Daily maximum session concurrency: median **2.0**, mean **1.7059**. Empirical bootstrap: 1,500 replacement resamples of entire days, 95% percentile interval **[1.6425, 1.7647]** for mean within-sample daily maximum concurrency.

Entire days are the resampling blocks, preserving the recorded within-day link between session times, durations and energy outcomes. This does **not** establish independence across days, station demand nonstationarity, population growth, or applicability to another installation. It is a conditional descriptive interval, not an operational reliability guarantee.

## Separate 16-day LP replay

The exact prior original-data replay reports 16 solvable selected high-use days, 232 day-specific session occurrences, and median **44.0092%** reduction relative to a hypothetical immediate/front-loaded power schedule. The optimization uses achieved recorded energy as a target, and the source power-discrepancy audit remains unresolved. This is **not** an observed reduction and does not imply improved energy efficiency, reduced cost, emissions reduction, thermal derating avoidance, or trip/service improvements.

## What cannot be inferred

- EPFL session timestamps do not reveal the driver's explicit requested departure time or minimum energy obligation.
- The station's power cap is not necessarily the transformer or vehicle's validated rating.
- Day resampling does not permit claims about EV market penetration or power-system thermal aging.
- Without actual co-located transformer and feeder measurements, modeled demand shifts are not quantitative inputs to SINTEF's thermal physics.

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
