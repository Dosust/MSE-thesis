# First-pass critical evidence synthesis — 2026-11-03

**Status:** Evidence-qualified ***pilot synthesis*** of individually inspected publisher texts. Not a systematic-review result or an exhaustive claim that no other studies exist. Each record is a **candidate pending full-text eligibility and independent second screening**.

## Priority source-by-source findings

| Study | Source-grounded experimental or computational content | What its evidence does NOT establish | Potential role in review |
|---|---|---|---|
| [Krama et al. (2026), Qatar extreme-climate DC charger](https://doi.org/10.1016/j.ecmx.2026.101960) | Open full text: 50-kW CCS2 charger; a vehicle; internal temperature sensors including rectifier components (±1°C, five-minute sample), external ambient, power analyzer with AC input and DC output, offered/delivered power, SoC. Ambient period roughly 15–55°C; temperature and power channels timestamp aligned to within one sampling interval; original dataset on request. | Does not provide a verified connected transformer with measured top-oil/hot-spot and service. Its rectifier temperature limit is equipment-specific, not universal. | **B — MOST DIRECT EVSE THERMAL FIELD DATA ACQUISITION LEAD** |
| [2017 CIRED 11-kV distribution transformer thermal experiments](https://doi.org/10.1049/oap-cired.2017.1102) | 200-kVA ONAN transformer, 16 internal fibre-optic sensors, load-dependent temperature rises and separate overload transient. | No measured EV charging station, documented same-site EVSE or combined field service. | **A — thermal model calibration/independent transient test benchmark** |
| [Zakaria et al. (2024), EV hosting capacity with thermal rating](https://doi.org/10.1049/gtd2.13025) | Actual UK trial EV charging inputs (roughly 200 EVs as reported in methods), UK household/substation and weather data; Monte Carlo simulation and static-vs-dynamic ratings on an IEEE 33-bus test system. | **Measured input data do not mean the IEEE 33-bus transformer/EVSE network is physically observed.** No site-level charger rectifier temperature validation. | **C — clear benchmark for measured boundary conditions + transparent conditional network simulation** |
| [Bragone et al. (2022), transformer thermal PINN](https://doi.org/10.1016/j.epsr.2022.108447) | Real transformer top-oil, ambient and load-factor inputs; 1D heat diffusion PDE; PINN compared with finite-volume numerical solution. | No EVSE heat/derating field data and not evidence a PINN must outperform a simpler independently fitted physical transformer model at new sites. | **A/D — competing methods, numerical verification and potential PINN feasibility criteria** |
| [Residual-based attention transformer PINN (2025)](https://doi.org/10.1016/j.engappai.2024.109556) | Publisher article reports spatial transformer winding temperature estimates and fibre-optic validation on a transformer at a floating PV plant. | Data declared confidential; no physically linked EVSE internal thermals; limited independent reproduction from public data. | **A/D — spatial measurement and model-method comparison** |
| [Qian et al. (2015), transformer ageing from EV charging](https://doi.org/10.1016/j.ijepes.2014.09.040) | Stochastic modelling links EV charging time/SoC/loading and ambient conditions to transformer thermal ageing. | Abstract does not establish measured EVSE internal temperature or external heatwave-validation site. Full-text model and data assessment outstanding. | **C — early coupled loading/thermal modelling candidate** |
| [Ahmed et al. (2026), review of EV charging impact on networks](https://doi.org/10.1016/j.apenergy.2025.126961) | Open structured review discusses network thermal stress, voltage, smart charging and mitigation. | Secondary synthesis **cannot be counted as independent measured field evidence**; its cited original studies require independent appraisal. | **C — backward and forward citation mining only** |
| [Azeem et al. (2026), distribution transformer EV loading](https://doi.org/10.1016/j.epsr.2025.112663) | Abstract reports comparative 200/375-kVA transformer and EV loading effects; discusses temperature and electrical loading. | Original experimental physical setup vs simulation/model-based numbers and same-site EVSE mappings are not established by the abstract alone. | **C — high-priority full-text classification** |

## Provisional mechanism-state evidence matrix

| Required state or mechanism | Support at this early stage | Limitation |
|---|---|---|
| Transformer load/ambient→top-oil and winding dynamics | Direct transformer original experiments exist (e.g. 2017 CIRED), plus independent SINTEF measured data | Different equipment/cooling/ambient and no mapped EVSE field connection |
| EVSE ambient→internal rectifier temperature→offered-power derating | Qatar field study directly measures charger side and reports specific thermal limits | Data on request; original raw numerical reproduction pending |
| Actual time-dependent transformer electrical loading due to charging | Actual EV charging load inputs plus network simulation in Zakaria 2024 | Actual same-site transformer meter and charger circuit not proven for the modelled network |
| Transformer thermal restriction→EVSE delivered power/service change | Published simulations suggest mechanisms and decisions | Field service and protection action documentation missing in current corpus |
| Birectional T_e→P thermal conditioned EV charging power | Plausible as conditional demand feedback; no simultaneously observed heatwave charger–transformer trajectory in inspected records | Requires measured charger control, grid/asset identity, electrical time alignment and causal qualification |
| Parameter identifiability/UQ under extreme heat | Established generic methods and transformer model studies exist | Need genuine observed high-ambient test and independent installations |
| Spatial/temporal physics-informed models | Bragone 2022 and 2025 RBA-PINN demonstrate approaches | No automatic evidence of superiority under field coupled extreme heat; compare to physics-only on same holdout |

## Preliminary gap hypothesis (NOT a claim of literature-wide absence)

> Among the records verified in this pilot, original transformer thermal observations and original extreme-heat EVSE rectifier measurements appear in **different studies/sites**, while studies combining actual EV inputs with network thermal ratings often run a modelled distribution network. The first-pass evidence therefore does not establish simultaneously observed transformer↔EVSE thermal feedback, transition times and mobility service loss at a physically mapped common installation.

This **hypothesis must be actively falsified** through the formal systematic search. If we discover a study with measured synchronized transformer hot-spot/top-oil + EVSE internal temperatures + actual charger power limits and delivery for the same facility, its data and methods become a top-priority inclusion, not an inconvenient exception.

## Literature-first decision for Professor Phelan

**What is scientifically defensible now:** Start with energy-balance equations and physics-only top-oil / EVSE temperature models; validate independently on original component observations; use real loading and temperatures as boundary conditions; reserve cross-component coupling for an explicitly conditional model until same-site evidence exists.

**What would make PINN justified:** The selected physical PDE or inverse problem requires spatial reconstruction or partial observations, boundary and parameter information are qualified, independent non-training thermal sensors/conditions exist for evaluation, and PINN materially outperforms simple physics/numerical methods without leakage. A more complicated model is not itself evidence of a contribution.

## Full-review next checks

1. Confirm author/date/DOI and experimental setup for every source above; attach exact full-text page/table quotations and extract to schema.
2. Search references/citations of the Qatar, 2017 transformer and Zakaria papers for a truly same-site dual-thermal dataset or verified field intervention.
3. Run the four-stream Scopus, Web of Science and IEEE Xplore searches where permitted, export exact search results/hashes, dedup, independent full-text appraisal, document exclusions.
4. Only after this search, finalize a supported precise novelty claim and method-selection rule for the thesis.
