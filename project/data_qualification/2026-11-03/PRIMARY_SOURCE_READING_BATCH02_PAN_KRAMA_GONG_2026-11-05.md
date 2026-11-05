# Primary-source reading batch 02: Pan, Krama, Gong, and strongest contrary cases
**Date:** 2026-11-05. **Scope:** frozen SO1–SO3 thermal Power–Electrified Transportation under extreme heat. **Status:** paper-critical partial source extraction, NOT formal screening or PRISMA eligible-inclusion decision.

## 1. Pan et al. (2025) — physics and decision-model limitation

**Bibliography:** Pan C, Chen W, Zhou C, Zhou W, *Distribution network planning considering active response of EVs and DTR of cables and transformers*, *High Voltage* 10(2), 279–293 (2025). Original Wiley publisher DOI: https://doi.org/10.1049/hve2.70024 ; original full page: https://ietresearch.onlinelibrary.wiley.com/doi/full/10.1049/hve2.70024 (full-page direct retrieval 403 in this pass; published equation excerpt available through publisher-indexed public search results).

**Source section 4, original equation numbering (not novel equations):**
- Top-oil ODE (6): `tau_o * d(theta_TO)/dt = -theta_TO + theta_amb + Delta(theta_TO,U)`.
- Ultimate rise (7): `Delta(theta_TO,U) = Delta(theta_TO,R) * ((K^2*R+1)/(R+1))^nu`, where `K=I_TR/I_TR,rated`, R = load/no-load losses at rated current.
- Backward Euler implicit time-discretization (8): `theta_TO,t = [tau_o/(tau_o+dt)] theta_TO,t-1 + [dt/(tau_o+dt)] [theta_amb,t + Delta(theta_TO,U,t)]`.
- Winding/hotspot dynamic ODE (13): `tau_w * d(theta_HS)/dt = -theta_HS + theta_TO + Delta(theta_HS,U)`, and (14): `Delta(theta_HS,U) = Delta(theta_HS,R) * K^(2mu)`.
- **Crucial source simplification** (15): set the *winding time derivative* to zero on **hourly dispatch** grounds (`tau_w` typically 7–8 minutes), and set `mu=1`. Thus `theta_HS,t = theta_TO,t + Delta(theta_HS,R) K_t^2`.
- **Source explicitly states this can underestimate hot-spot temperatures for fast load changes.** This simplification is not justified for arbitrary short EV peak load events. Retain both state derivatives at minute-level and compare timescale assumptions; do not attribute measured fast-charger data to the paper.
- Original paper studies DTR for cables and transformer inside a bi-level distribution planning/active EV response optimization with 13-node synthetic case study; 4.8% cost savings and 96% uplift are case-simulation metrics, **not installed-site measured service or validation**. Publisher states raw data available on request. Terms like DTR "temperature-aware capacity" must not be treated as a logged operator's measured thermal restriction in service.
- **Novelty falsification:** integrating modeled transformer DTR and EV active response is already published. **Potential thesis contribution:** coupling physically qualified minute-scale winding/oil and EVSE temperatures to *observed* restriction and service timestamps, if data permit.

Sources: https://ietresearch.onlinelibrary.wiley.com/doi/full/10.1049/hve2.70024 and https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/hve2.70024. Publisher-indexed original search snippets with exact equations; direct publisher page 403; figure inspection not claimed.

## 2. Krama et al. (2026) — EVSE actual extreme-heat field data

**Bibliography:** Krama A, Kamal N, Sezer N, Bayhan S, *Impact of extreme climatic conditions on fast EV charger performance: field experimental insights from Qatar*, *Energy Conversion and Management: X*, 31, article 101960 (Sep 2026), DOI https://doi.org/10.1016/j.ecmx.2026.101960. Original publisher article: https://www.sciencedirect.com/science/article/pii/S2590174526004435 ; institutional author metadata: https://elmi.hbku.edu.qa/en/publications/impact-of-extreme-climatic-conditions-on-fast-ev-charger-performa/.

- **Study evidence F3:** in situ, commercial 50-kW air-cooled DC EVSE monitored over ambient 15–55°C; instrumented internal rectifier temperature, charger offered and delivered power, electrical efficiency, current THD and EV battery SOC.
- Publisher abstract says near-normal offered output under moderate conditions and strong restriction once rectifier approached ~55°C. Offered power drop described as up to **35–40 kW**, efficiency decrease ~**5–8 percentage points** (source says 5–8%; do not change to percentage points without denominator), winter/summer tested SOC charging time **86 vs 169 min**. Publisher highlight: rectifier temperature explains over 96% of variation in offered power, a statistical fit not by itself identification of every causal confounder.
- Source abstract distinguishes charger-offered power from EV-accepted/delivered charging; cross-session and temporal validation are reported. Exact regression form, data partitions, thermocouple placements, sensor calibration, thermal control-event reason codes, and uncertainty **still require original full-text/field raw data**. Publisher full article direct open returned 403, so do not claim equation-level audit here. Data on request.
- Supplying grid transformer identity/oil/hotspot not documented in this source review; measured charger derating is **not validated transformer-to-charger thermally causal field coupling**.
- **Potential related precursor:** Sezer and Bayhan, *Performance Assessment of an Electric Vehicle Fast Charger In Hot Arid Climate of Qatar*, 2025 ICTEA proceedings, https://journals.library.torontomu.ca/index.php/ictea/article/view/2606 (wireless sensors and a 50-kW Qatar fast charger). Compare original sensor installation, sessions and overlapping data to Krama journal article before treating them as independent experiments; **shared-study family is plausible but NOT confirmed.**

## 3. Gong et al. (2015) — crucial thermal experiment predecessor

**Bibliography:** Gong Q, Midlam-Mohler S, Serra E, Marano V, Rizzoni G, *PEV Charging Control Considering Transformer Life and Experimental Validation of a 25 kVA Distribution Transformer*, *IEEE Transactions on Smart Grid* 6(2):648–656 (2015), DOI https://doi.org/10.1109/TSG.2014.2365452. Original paper full text not retrieved; DOI and publication metadata from institutional/IEEE citations and public abstract (not a verified figure/equation extraction). 
- Public article abstract reports experiments calibrating thermal model on an actual 25 kVA transformer and evaluating a charging-control policy considering transformer aging and charging demand quality. **Observed experiment** must be separated from **simulated EV sessions** until full paper methods and measurements inspected.
- **Family predecessor:** Qiuming Gong, 2012 Ohio State PhD, *PEV Charging Control Considering the Distribution Transformer Life*, https://etd.ohiolink.edu/acprod/odb_etd/r/etd/search/10?clear=10&p10_accession_num=osu1354550558 ; institutional doctoral abstract reports dynamic hot-spot transformer model, season/peak demand, load prediction with actual utility consumption, stochastic charging quality, public station arrival/departure and queuing/wait time. This proves such *model categories* already exist, **not** their physical in-field joint validation.
- First full paper reading priority: sensor positions, calibration protocol, load profiles, control intervention, field/lab separation, model parameters, validation split, quantitative service metrics, and overlap with 2012 dissertation.

Sources: https://www.researchgate.net/publication/273393355_PEV_Charging_Control_Considering_Transformer_Life_and_Experimental_Validation_of_a_25_kVA_Distribution_Transformer (publisher article abstract repost), https://dblp.org/rec/journals/tsg/GongMSMR15 and OhioLINK institutional dissertation abstract.

## 4. Soltani et al. (2026) — further novel-claim falsification, ALREADY V5 LIT-0554

Original open article https://doi.org/10.1016/j.ecmx.2026.102022, *Temperature-aware stochastic joint planning of fast charging stations and distributed energy resources capturing regulatory incentives*, Sep 2026. Models temperature dependence of EV energy demand, charging constraints and efficiency, ESS operation, and service deficit within two-stage stochastic MILP; numerical IEEE 33/69-bus cases, with cold-climate dominance. **Modeled temperature-aware multi-asset planning and fleet energy deficits are also prior art.** Does not claim instrumented connected transformer winding/EVSE rectifier thermal state and causal service timestamps. Source's simulated numbers not transferable as field evidence. **Already present in V5**, do not add new LIT ID.

## 5. Derived thesis-method audit
The source equations do not constitute a new method by themselves. For any proposed integrated model, identify:
1. Power transformer `theta_o(t)`, `theta_h(t)` and rated current with physics-consistent temperature-dependent loss terms and verified time constants.
2. EVSE rectifier thermal state `theta_r(t)`, ambient and cooling; **source-controlled offered power** and explicit electrical meter boundary.
3. EV battery SOC, current limit/acceptance and requested-versus-offered-versus-delivered power; distinguish EV BMS taper from charger thermal limit.
4. Measured timestamps `t_thermal_limit`, `t_command`, `t_actual_power_change`, `t_service_deadline` and censored observations; report timescale and timebase/clock uncertainty.
5. Physics-only ODE/DAE/FVM versus any PINN with independent matched splits and proper UQ; no PINN claim from model-name novelty.

**No new primary field data, experiment, calibrated full coupling, formal human screening, or global novelty verdict is asserted.**
