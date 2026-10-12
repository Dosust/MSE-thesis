# Scientific Research Checkpoint — 12 October 2026

**Status:** WORKING-FROZEN REPRODUCIBILITY SNAPSHOT — not a frozen physical model.  
**Research:** ASU MSE Sustainable Engineering, temperature-mediated electrical–thermal interdependencies of Power (P) and Electrified Transportation (T_e) under external extreme-heat forcing.  
**Governing science:** project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md; project/RESEARCH_DECISION_AND_FREEZE_PROTOCOL_V1.md; project/module_01_transformer_thermal_state_physics/MODULE_01_MODEL_ADMISSION_LEDGER_V1.md; project/module_02_transformer_thermal_parameter_identification_state_estimation/*.

## Thesis governance — no overwrite
- User-approved 1 General Objective + 3 Specific Objectives amendment remains on **PR #76, OPEN / NOT MERGED** at this checkpoint. Main still uses the predecessor objective file. 3 research questions are provisional; two candidate hypotheses H1/I2 and H2/I3 remain unqualified.
- The I7 price-information scope PR #75 is **MERGED**. I7 is supporting economic/informational decision coupling; not physical heat transfer and not a new research objective.
- Exactly eight selected components: P1 distribution transformer, P2 distribution feeder, P3 transformer protection/load-management hardware, P4 transformer cooling, T1 DC charger, T2 vehicle battery, T3 EVSE cooling, T4 vehicle HVAC. T4/I6 can remain inactive in the minimum model.
- I1 P→T normal AC supply is not inherently temperature-mediated. I2 T→P actual AC-demand influence is **CANDIDATE**. I3 P→T temperature-conditioned implemented P3 restriction is **CONDITIONAL/OPEN**. I4/I5 are internal T equipment functions; I6 conditional delayed demand; I7 supporting pricing. Common H(t) independently forces both systems, not a cross-system arrow.

## Independent evidence streams (do not merge physical identities)
**TU Wien network:** Schultis & Ilo, TUWien_LV_TestGrids V1 (2018), DOI https://doi.org/10.17632/hgh8c99tnx.1. Selected theoretical 20Cable network has 160 kVA, 20/0.4 kV transformer, cable topology and source parameters. Original electrical benchmark reconstructed with quantified residuals. Synthetic CPC50 connection is node (6,0); under imposed 50 kW DC, 95% assumed efficiency, PF 0.98, predicted 377.62 V and 4.760 kW modeled total network resistive losses. These are **conditional** network predictions; losses from the feeder must not be counted as transformer heat.

**Qatar charger:** Sezer & Bayhan (2025) and Krama et al. (2026), DOI https://doi.org/10.1016/j.ecmx.2026.101960, document Siemens CPC50 50 kW DC charger, Aiways U5 battery and temperature-conditioned derating. No synchronized original Qatar charger dataset or matched P1/P2 system has been admitted; the proposed T_r→actual grid-side AC P,Q law remains OPEN. Internal CPC50 transformer measurements do not constitute upstream P1 transformer evidence.

**Najar ONAN surrogate:** Najar et al. (2017), DOI https://doi.org/10.1016/j.applthermaleng.2017.03.061. Separately measured 160 kVA, 20 kV/400 V ONAN experimental transformer yielded x=0.80, rated load-loss ratio R=9.15, fitted tau_o=199 minutes, delta-theta-o-rated=54.87 K. The IEC small-ONAN k11=1 scenario and V1.2 time-stepping are explicitly conditional; do not double-count k11 with fitted effective time constant. Not a validated TU Wien thermal model.

**Bærug ONAN field data:** Bærug, Madshaven & Espedal (2025), Zenodo DOI https://doi.org/10.5281/zenodo.17223516. An **independent** 40 MVA Norwegian transformer dataset, 2024; 8,592 measured hourly rows, 192 omitted timestamps, longest uninterrupted stretch 8,208 hours. Chronological split 4,924 train / 1,642 validation / 1,642 held-out test. Reduced phenomenological current-dependent model held-out: MAE 0.907 K; RMSE 1.156 K; bias (measured−predicted) −0.245 K. Ambient-only baseline MAE 1.141 K, RMSE 1.365 K; ~20.5% and ~15.3% reductions respectively. Fitted tau 433.357 minutes, b 13.5719 K, c 0.5392 K, training current normalization 24.2725 A (NOT rated current). This is an empirical, equipment-specific **predictive assessment**, not validation of Najar/TU Wien or cross-infrastructure I2/I3. Source calculated temperatures are not raw sensor measurements.

## VVUQ and evidence interpretation
- V1.2 previous run reports 20 numerical tests and Euler/RK4 convergence; results remain surrogate simulation and code verification, not physical validation. Separate Alliander-documentation recurrence comparison reached double-precision agreement; external Alliander package runtime was not independently executed.
- Bærug 24-hour moving-block residual-bootstrap results are **descriptive**, not instrument-uncertainty bounds or universally transferable confidence. Timestamp timezone, current measurement side, device loss/cooling details and sensor uncertainty remain unresolved from the README.
- Preserve raw-versus-calculated distinctions. Do not claim observed I2 propagation, verified I3 control, hotspot or aging prediction, SO3 service shortfalls, empirical thermal thresholds or validated resilient service for the TU Wien–Qatar composite.

## Archive integrity and physical storage
Complete byte-preserving project archive contains **33 scientific input/artifact files**, SHA-256 **88ea29ac87ceff5f259b76ce4e61ca32afe1be0d0bf5ca62f1ddc3a8e9556481**, size 5,600,667 bytes. It was verified by ZIP CRC and SHA-256 checks of 33 member files. Saved persistently to user's ChatGPT Library at:
**/MSE_Thesis_Research/MSE_Thesis_All_Uploaded_Research_Data_Checkpoint_2026-10-12.zip**
alongside the full per-file checksum CSV and checkpoint status report. The archive bytes are **not committed to this GitHub PR**; GitHub holds its scientific index and provenance until the binary payload is explicitly imported. Do not imply that the GitHub checkout alone contains raw datasets.

Use DATASET_AND_REPRODUCIBILITY_MANIFEST_V1.csv and OPEN_GATES_AND_NEXT_EXECUTION_V1.md before running the next stage. No existing frozen files are amended by this checkpoint.
