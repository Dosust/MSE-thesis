# PILOT EVIDENCE MATRIX — SOURCE-VISIBLE, NOT ORIGINAL-PDF VERIFIED

**Date:** 2026-10-15  
**Scientific status:** `PILOT PRELIMINARY / ORIGINAL PDF AUDIT NOT DONE / DATA ROW AUDIT NOT DONE`.

Published abstracts, publisher HTML excerpts, institutional records, research-code README files and dataset descriptions were inspected in public web search. Several attempts to open publisher full pages returned 403/429 errors; attempting the author repository PDF led to a request-a-copy page, **not a downloaded PDF**. No DOI listed here has a `PDF_VERIFIED` flag. Direct quotes, formal governing equations, calibration sample sizes, exact figure descriptions or claimed independent testing must be re-extracted from original PDFs before promoting findings to the thesis accepted-core register.

| ID | Evidence reported by primary source / accessible record | Method/data provenance | Boundary and outstanding audit |
| --- | --- | --- | --- |
| P001 [Krama et al. 2026](https://doi.org/10.1016/j.ecmx.2026.101960) | In situ 50 kW DC fast charger with ambient temperature approximately 15–55 °C. Offered versus delivered power, rectifier temperature, charging duration, and reported cross-session/temporal validation. Publisher abstract reports 86 versus 169 min for a tested SOC interval. | **Field charger experiment**; data on request. | Need original PDF equations/figures/data-dictionary and raw data approval; not simultaneous transformer, vehicle trip-completion, and charger thermal observation. |
| P002 [Blomgren et al. 2023](https://doi.org/10.1016/j.segan.2023.101048) | A stochastic grey-box dynamic transformer-temperature estimation/forecast model developed using actual Danish DSO field data; 6-hour MAE reported about 0.4–0.6 °C. | **Field transformer measurement + model**, data explicitly not shareable by authors. | Exact parameter identification and independent split need original PDF audit; NOT a trainable open experimental dataset. |
| P003 [Bragone et al. 2022](https://doi.org/10.1016/j.epsr.2022.108447) | Transformer PINN solving a 1D thermal PDE using operating measurements/boundary conditions, compared with finite-volume calculations. | **Field inputs with numerical reference comparison**. | FVM agreement is not automatically internal-temperature field validation or EV-grid interface validation. Inspect original equations, available observations, train/test split. |
| P004 [Tang et al. 2024](https://doi.org/10.1049/hve2.12435) | PINN transformer 2D temperature fields benchmarked against COMSOL-simulated data, including comparison to DNN; authors explicitly note soft constraints may be violated. | **Primarily simulator-referenced temperature labels**, not demonstrated independent field measurements of complete coupled system. | Need inspect all experimental cases/validation independently; do not promote simulation label to field truth. |
| P005 [Mannapperuma et al. 2025](https://doi.org/10.3390/batteries11090319) | Production EV CAN/instrumented electrothermal pack model under laboratory climate and road driving, with source-reported ambient tests −10 to 45 °C. | **EV-level lab + on-road empirical data**. | Vehicle-battery evidence only; raw data release and sample support not established. |
| P010 [Villarroel et al. 2017](https://doi.org/10.1049/oap-cired.2017.1102) | Experimental 200 kVA 11/0.433 kV transformer with 16 fiber-optic sensors; measurements at 0.7, 1 and 1.25 p.u., then separate overload validation at 1.8 p.u. for 2 hours. | **Controlled instrumented transformer study**. | No direct EVSE observation; raw individual sensor trajectories not yet downloaded or reviewed. |
| P008 [Godina et al. 2016](https://doi.org/10.1016/j.enconman.2016.04.087) | Transformer hot-spot/aging consequences from EV loads for two real distribution transformers using real load and equipment input data. | **Real operational INPUTS plus transformer THERMAL MODEL**, not a validated measured joint P/T heat experiment by default. | A repository lists a PDF but click redirected to request-a-copy; obtain permitted original PDF and audit input/observed state distinction. |
| P007 [Balogun et al. 2023](https://doi.org/10.1109/TSG.2023.3339374) | Grid-aware EV-EcoSim links charging, transformers, batteries, distributed generation and grid simulation; public software. | **Co-simulation**, with proprietary base load used originally. | Simulator outputs do not prove field-interfaced power–EV thermal causality or observed mobility loss. |
| P006 [Guddanti et al. 2025](https://doi.org/10.1038/s41467-025-59749-4) | Study of temperature-sensitive electricity demand and distribution grid vulnerability; original article lists source data and Zenodo supplementary data/code. | **Grid modeling + public data/code links**. | No claimed direct EV charging-field heat interaction. Data files not yet inspected. |
| P011 [Fotouhi et al. 2017](https://doi.org/10.1016/j.ress.2017.01.026); P012 [Zou and Chen 2019](https://doi.org/10.1016/j.ress.2019.106557) | Establish earlier traffic–electric resilience and dynamic interdependency modeling. | **Coupled-system simulation/optimization prior art**. | Contextual, not direct extreme-heat electrothermal tests. |

## Pilot data leads (catalogue only)

- [KIT 2026 measurement record](https://zenodo.org/records/17866847): 16 EVs/18 sessions, AC voltage/current, local ambient; record documents 23.5 GB and Oct–Dec 2025 collection. **Raw observations not downloaded**; not an identified extreme-heat battery/transformer dataset.
- [TUM EV field repository](https://github.com/TUMFTM/electric-vehicle-uds-dataset): pack thermal/ambient states and vehicle operation on real vehicles; raw Parquet LFS **not read**.
- [Qatar 2026 experiment](https://doi.org/10.1016/j.ecmx.2026.101960): field charger study, **raw data on request**.
- [Blomgren 2023](https://doi.org/10.1016/j.segan.2023.101048): measured transformer case, **raw data not shareable by authors**.
- [Godina et al. 2016](https://doi.org/10.1016/j.enconman.2016.04.087): original PDF indicated at institutional site, download **not obtained**.

## Initial thesis implications (questions, not gaps proven)

1. Test separately the thermal effect of grid state on EVSE available power (`P -> T_e`) and EVSE load on transformer state (`T_e -> P`); shared heat forcing is not causal interface evidence.
2. An experimentally identified charger model can support charger power/time prediction **but not** independent real trip-completion evidence without matching mobility observations.
3. A grey-box thermal model has strong transformer precedent; assess novelty only as a *specific independently tested contribution* (e.g. dynamic heat-dependent interface identification, uncertainty in coupling, transition/service timing), not adopting the method itself.
4. Choosing physics-only versus calibrated grey-box versus PINN remains conditional on raw measurement, identifiability, and independent held-out validation.

**Every record remains `NOT SCREENED` and `PDF NOT VERIFIED`.**
