# Physics and Mathematics Literature Review — Evidence-qualified Synthesis V1

**Prepared:** 2026-10-17 • **Research focus:** Extreme-heat-induced thermal interdependencies between the electrical Power system **P** and Electrified Transportation **Tₑ** • **Status:** DETAILED SOURCE-VERIFIED CORE LITERATURE SYNTHESIS; **NOT** COMPLETED JBI/PRISMA SYSTEMATIC SCOPING REVIEW.

**Frozen thesis title:** *Engineering of Power–Electrified Transportation Interdependencies for Resilience*. Frozen General Objective and SO1–SO3 remain unchanged; this literature synthesis does not authorize any new scope, method, mechanism, dataset or novelty claim.

## Review question and admissible inference

**Scientific question:** How can extreme ambient heat modify physical thermal states, operating constraints and time-dependent electricity/mobility services at a real connection between a utility distribution transformer (P) and EV charging equipment (Tₑ)? Which parts have been measured, merely modeled, independently validated or not yet observed?

**Method:** Registered five Scopus search-stream exports yield **37,376 distinct EIDs**, but only a reproducible AI-assisted *discovery triage*, not final formal human screening. Thirty DOI papers were prioritized. The current synthesis relies on source-verified full-text or author-posted bodies and clearly demotes publisher abstracts/metadata to lower evidence tiers; no search-hit count is misrepresented as included studies. Source-tier language is critical and preserved throughout.

## 1. What physics and mathematics already exist?

### 1.1 Transformer heat and electrical losses (P subsystem)

Lumped thermodynamics, transformer thermal equivalents and loading-guide prior art establish that transformer hotspot/oil temperature depends on winding and no-load electrical loss, cooling conditions, ambient forcing, heat capacity, and dynamic loading. Generic physically dimensioned balance (REVIEWER SYNTHESIS, **not** a verbatim newly fitted source model):

```math
C_P\frac{dT_P}{dt} = P_{\mathrm{loss},P}(V,I_{\mathrm{rms}},I_h,T_P)-Q_{\mathrm{rejection},P}(T_P,T_a,u_{\mathrm{cool}})
```

Here \(C_P\) in J/K, \(P_{\mathrm{loss},P}\) and heat rejection in W, and \(T_P\) is a **named physically observable state** (top oil, lid, winding hotspot, or separate RC states), not a free-floating interchangeable “transformer temperature.” `Q_rejection` can be nonlinear in \(T_P-T_a\); a first-order exponential is a simplification, not a fundamental law. Swift et al. 2001, DOI [10.1109/61.915478](https://doi.org/10.1109/61.915478), establish equivalent-circuit physics with nonlinear convective cooling (abstract verified; **full original IEEE equation text unavailable**).

Source-specific prior art:

- **Godina et al. (2016)**, DOI [10.1016/j.enconman.2016.04.087](https://doi.org/10.1016/j.enconman.2016.04.087), original TU/e-hosted publisher PDF read: hot-spot `theta_H=theta_a+Delta_theta_o+Delta_theta_h`, transient top-oil/winding thermal ODEs, EV charging demand scenarios, simulated transformer loss of life. Actual feeder base-load data DO NOT make model-predicted oil/hotspot values independently measured; EVSE's own temperature is not instrumented here.
- **Villarroel et al. (2017)**, DOI [10.1049/oap-cired.2017.1102](https://doi.org/10.1049/oap-cired.2017.1102), publisher-indexed article body analyzed: 16 internal fibre sensors in a lab 200-kVA transformer, step-load identification then separate overload comparison of genuinely observed winding temperature. Independent original PDF still not obtained; no EVSE.
- **Blomgren et al. (2023)**, DOI [10.1016/j.segan.2023.101048](https://doi.org/10.1016/j.segan.2023.101048), original publisher PDF read: continuous-discrete stochastic heat-balance RC state space `dx=(Ax+Bu)dt+Sigma dW; y=Cx+e` with heating \(\Phi_h=aI_{3\phi}^2+b\), ambient heat transfer and latent RC states. Field target: **measured transformer lid**, not independently measured winding hotspot; field 200/400-kVA cases predict lid with 6h MAE ~0.4–0.6°C. Residential EV ownership downstream is not synchronous EVSE heat/charging instrumentation.
- **Seier et al. (2015)**, DOI [10.1109/TSG.2015.2390624](https://doi.org/10.1109/TSG.2015.2390624), publisher/University of Vermont report chapter abstract verified: thermally instrumented **25-kVA residential service transformer**, data-driven genetic programming alternative to IEEE Annex G; observed internal temperatures and documented Annex G overprediction. The full journal original source equations have NOT been independently retrieved in this tranche.
- **Doolgindachbaporn et al. (2022)**, DOI [10.1109/TPWRD.2021.3123957](https://doi.org/10.1109/TPWRD.2021.3123957), coauthor-posted full article text inspected: measured transformer **winding temperature indicator** (WTI), load, tap positions, ambient, wind and radiation for nine **180–1000 MVA** units, comparing ANN/SVM predictions against an IEEE Annex G reference and held-out utility WTI. A WTI is an **instrument reading indicative of** hotspot, not direct observation of physical internal hottest point; large power-transformer models are not transferable as-is to chosen distribution equipment.
- **Gong et al. (2012)**, DOI [10.1109/EnergyTech.2012.6304673](https://doi.org/10.1109/EnergyTech.2012.6304673), original coauthor-posted article text inspected: a **25-kVA** distribution transformer experimentally heated with a special low-voltage **DC excitation test** permitting oil thermocouples; calibrated observed **top-oil** responses and estimated winding-average temperature indirectly through resistance. **Actual winding hotspot not measured; direct EV charge-control effectiveness left for later work.** This is NOT the Gong (2015) journal article. Its standard top-oil mathematical heat balance can inform validation semantics, but DC excitation test is NOT field-synchronized P↔Tₑ.

**Conclusion P:** First-principles thermal ODEs, nonlinearity, measured P states, statistical identification and component validation all are existing research. The thesis cannot claim to invent transformer heat physics or temperature prediction.

### 1.2 EVSE rectifier heat, loss and operational constraints (Tₑ subsystem)

A dimensionally consistent **reviewer synthesis** of a lumped EVSE heat balance is

```math
C_E\frac{dT_E}{dt}=P_{\mathrm{loss},E}(P_{\mathrm{AC}},P_{\mathrm{DC}},u_E)-Q_{\mathrm{rejection},E}(T_E,T_a,u_{\mathrm{fan}})
```

**In the available data, this is a candidate physics law, NOT an equation fitted and independently validated by Krama.** Actual required \(C_E\), heat-rejection coefficients, cooler/fan actuation, and conversion-loss geometry remain unidentifiable unless data/metadata exist. A measured efficiency identity must use time-aligned electrical port quantities:

```math
P_{\mathrm{loss},E}(t)=P_{\mathrm{in,AC}}(t)-P_{\mathrm{out,DC}}(t),\quad \eta(t)=\frac{P_{\mathrm{out,DC}}(t)}{P_{\mathrm{in,AC}}(t)}.
```

This is **total charger electrical dissipation/storage proxy**, not measured converter junction heat flux. AC power, DC power and thermal sensor timestamps must be aligned and integrated consistently.

**Trentadue et al. (2018)**, DOI [10.3390/en11081937](https://doi.org/10.3390/en11081937), European Commission JRC **original 13-page open publisher article PDF** examined through official institutional repository: **seven chargers/two EVs** tested in a climate chamber at +25°C, +40°C, −15°C and −25°C. Actual input AC and output DC power/current/voltage measured; original pp.3–7 distinguish instantaneous \(\eta=P_{DC}/P_{AC}\) from energy return \(E_{AC}/E_{DC}\). **+40°C often had little adverse effect on tested charging**, whereas cold conditions strongly reduced EV requested/delivered power and overall efficiency through BMS effects. The study demonstrates hardware- and vehicle-dependent nonuniversality; no actual external P transformer heat measurements, rectifier sensor or first-principles charger thermal PDE.

**Krama et al. (2026)**, DOI [10.1016/j.ecmx.2026.101960](https://doi.org/10.1016/j.ecmx.2026.101960), actual **complete original 16-page Elsevier publisher PDF provided by researcher** and independently parsed/visually reviewed: one Qatar **50-kW air-cooled DC charger** at 15–55°C ambient, with four rectifier-mounted sensors averaged (5-min data), two shaded ambient probes (5-min), and charger AC power/harmonics, offered and delivered DC power, SOC (1-min data). The original p3 Eq.(1) \(T_j=T_c+Z_{th}P_{loss}\) is conceptual thermal impedance; **semiconductor junction temperature is NOT measured**. Eqs.(2),(5) are total charger power-loss and efficiency balance; Eqs.(8)–(12) are **least-squares empirical regressions**, not dynamic heat ODE/PDE. Eq.(11) predictive polynomial includes ambient, rectifier rise and cross term; same-charger session holdouts include June \(R^2=0.416\), MAE 5.41 kW, August \(R^2=0.983\), September \(R^2=0.955\). June/August-trained, September-tested \(R^2=0.955\), MAE 1.847 kW (p13). Representative mean hot session offered 20.7kW, delivered 20.1kW, 169min versus winter 50.0kW offered, 32.9kW delivered, 86min (Table 5). **These are real observed charger capability effects** but not an independent *mobility mission* or upstream P thermal receiver validation. Sensor label `Transformer` in paper Fig.4 refers to an **internal charger transformer within Tₑ**, not a utility P transformer.

**Conclusion Tₑ:** Experimental climate-driven charger power/energy efficiency and field charger rectifier thermal derating are established; any thesis uniqueness cannot be “first to correlate charger temperature with power” or “first to model offered power.” Actual raw Krama data remain **requested by author email; no raw rows received**.

### 1.3 Heat PDEs, stochastic ODEs, PINNs and model-selection physics

**Bragone et al. (2022)**, DOI [10.1016/j.epsr.2022.108447](https://doi.org/10.1016/j.epsr.2022.108447), original publisher PDF read: simplified spatial heat diffusion

```math
\rho c_p\frac{\partial T}{\partial t}=k\frac{\partial^2T}{\partial x^2}+q.
```

The PINN embeds this as a residual using measured load/ambient/top-oil as forcing/boundaries, and is primarily compared with a **finite-volume numerical thermal field**, not an independently measured complete internal winding spatial field. **IMPORTANT unit check:** the article combines effective W heat terms with W/m²K and W/mK coefficients in a 1D approximation; transferring to new geometry requires explicit effective source-per-volume normalization (W/m³), spatial length units and heat-loss surface/volume scaling. The trained PINN is not experimental proof of internal spatial field or P↔Tₑ thermal propagation.

**Blomgren (2023)** already demonstrates stochastic physics-based grey-box RC models with actual field data. **Doolgindachbaporn (2022)** demonstrates ANN/SVM can beat a traditional transformer model on WTI of *other equipment class*, not that an ANN automatically outperforms a physically identified Tₑ–P interface model.

**Conclusion methods:** Physics-only thermal ODE/PDE, grey-box, numerical solvers, empirical regression, standard ANN/SVM and PINNs all have prior-art precedents. PINN choice is contingent on real measured target state, identifiability, physical boundary knowledge, observation timing, independent holdouts and improvement over simpler calibrated baselines. Using physics-informed labels does not constitute novelty or physical validity.

### 1.4 Coupled transformer–EV charging control, time and grid service

**Gong et al. (2015)** DOI [10.1109/TSG.2014.2365452](https://doi.org/10.1109/TSG.2014.2365452), publisher/research-profile **abstract only**: explicitly investigates transformer-life-aware EV charging control with experimentally calibrated 25-kVA transformer model and statements about charging strategy validation. **Crucial direct novelty counterexample.** Original journal full text still needed to determine exact thermometer/controller intervention and independently measured EV charging outcome. **Do not import the 2012 conference experiment as proof of the 2015 results.**

**Kunlasing et al. (2022)** DOI [10.1109/ECTI-CON54298.2022.9795360](https://doi.org/10.1109/ECTI-CON54298.2022.9795360), publisher/conference record and author request access only: transformer *load monitoring* and EV charging-control function; **whether measured thermal state triggers EVSE control remains unknown** before IEEE full text.

**Visakh and Selvan (2023)** DOI [10.1016/j.segan.2023.101096](https://doi.org/10.1016/j.segan.2023.101096), original publisher **abstract/body preview, not PDF**: thermal/electrical loading limits, harmonic-dependent loss heating, top-oil/hotspot and minimizing EV charging variance. Authors explicitly frame results as **simulation**, not observed electricity outage. Service interruption is an *estimated risk*, not an actual recorded blackout.

**Balogun et al. / EV-EcoSim (2024)** DOI [10.1109/TSG.2023.3339374](https://doi.org/10.1109/TSG.2023.3339374), original **arXiv author manuscript** text, journal equivalence not reconciled: co-simulation of EVSE, battery, distribution AC power flow and transformer oil/hotspot ODEs, an electrical port identity \(P_{AC}=P_{EV}/\eta\) plus power-factor reactive exchange. Battery cell calibration uses controlled 23°C input; battery thermal state explicitly not modeled, and there is no synchronized same-site observed heat-driven charger derating and receiving transformer thermal outcome. Integrated co-simulation itself already exists.

**Fletcher and Khan / RACE for 2030 (2025)** official final 32-page technical PDF report, [RACE 2025](https://www.racefor2030.com.au/content/uploads/Final-report-0571-FINAL-FINAL.pdf): IEC-style transformer heat transients with a **four-stage transformer-hotspot-temperature-based charger-power hysteresis** and modeled delivered EV charging energy under time-varying demand and ambient/load conditions. Part 1 desktop model/test-informed simulations; Part 2 planned actual instrumented mineral/ester transformer investigations, unconfirmed in current source. **A mathematical P thermal state → charging power constraint is unequivocally already modeled prior art**. The remaining question is *actual* field validation, bidirectional receiving physical thermal states, realistic service need and threshold/delay uncertainty.

**Jia, Donaldson and Zhang (2023)** DOI [10.1049/icp.2023.3126](https://doi.org/10.1049/icp.2023.3126), publisher/conference bibliographic abstract only, ambient-sensitive EV charging profiles and distribution implications; exact full-text equations/measurements not authenticated.

**Bai et al. (2024)** DOI [10.1109/PESGM51994.2024.10688510](https://doi.org/10.1109/PESGM51994.2024.10688510), verified conference abstract, real residential EV charging demand in different ambient regimes with a modeled dynamic transformer rating for expansion planning, no independent paired EVSE rectifier thermal receiving field test verified.

## 2. State-time and causal interface: physical graph vs model behavior

Electrical coupling is at an identifiable **actual port** and controller, not direct heat exchange between all P and Tₑ physical assets:

```math
P \xleftrightarrow[\mathrm{AC\ input/current}]{\mathrm{conditional\ operational\ constraints}} T_e, \quad T_a(t)\rightarrow \{P,T_e\}\quad\text{(common external heat forcing)}.
```

**P→Tₑ** requires: observed/validated P temperature \(T_P(t)\) → documented temperature-*activated* grid transformer protection/dispatch limit \(P_{\mathrm{alloc}}(T_P,\mathrm{history})\) → observed constrained EVSE AC input/charger offered power → separately quantified required electricity/mobility service. Common ambient heat or a modeled hot-spot control without real switch logs does not establish field causal effect.

**Tₑ→P** requires: observed rectifier heat state and manufacturer derating \(T_E(t)\) → actual EVSE AC current, active/reactive input change (not merely DC offered-power change) → changed transformer absolute RMS/harmonic load and losses → independently **measured subsequent** P temperature response controlling other loads and ambient. Charger derating can **decrease P heating**, create shifted load later, or modify harmonic losses; `THDi = I_h/I_1` increasing due to smaller fundamental does NOT prove absolute harmonic current or transformer loss increases.

### State thresholds and service variables

A **candidate definition** (reviewer synthesis, not observed in a paper): for a measured physical state \(T_j(t)\), a first critical exceedance time \(\tau_j=\inf\{t\ge t_0:T_j(t)\ge T_{j,\lim}\}\) presumes a **real documented** \(T_{j,\lim}\), specified sampling, and observed sensor error. If limits are unknown the event is undefined rather than filled in by a convenient threshold. Propagation delay is difference between *qualified* source activation and receiver effect times, not correlation lag under common daily ambient cycle. Mobility service requires an independent departure/route energy obligation \(E_{\mathrm{required}}(t_d)\), not just recorded SOC, session minutes, or kWh delivered. Electricity service similarly requires a duty/availability threshold outside the temperature state.

## 3. Cross-source evidence table

| Source | Physical math | Measured evidence | Validated target | Coupled thermal scope / limit |
|---|---|---|---|---|
| Swift 2001 | nonlinear transformer thermal network | Full IEEE not retrieved | not verified | P heat fundamentals; no Tₑ |
| Gong 2012 | P top-oil transients; resistance-temperature law | 25kVA oil thermocouple test under simulated DC excitation | actual oil vs model | **not** full P–EV field/control validation |
| Gong 2015 | aging-aware EV charging controller | abstract reports 25kVA experimentation | exact validation unknown until full text | potential direct prior-art counterexample |
| Seier 2015 | Annex G vs genetic programming transformer heat | 25kVA instrumented P transformer | measured thermal states described in abstract | no EVSE matched heat |
| Godina 2016 | P oil/hotspot ODEs + EV load scenarios | feeder background loading | P temps only simulated | Tₑ electric demand → modeled P heat |
| Villarroel 2017 | dynamic IEC transformer state model | winding fibre-optic data | measured P winding | no Tₑ |
| Trentadue 2018 | \(\eta=P_{DC}/P_{AC}\) and \(E_{AC}/E_{DC}\) | 7 commercial chargers, 2 EV, climatic chamber | observed input/output charging performance | no utility P transformer heat; +40°C often tolerated |
| Bragone 2022 | 1D heat PDE PINN | actual boundary/loading inputs | numerical FVM field mostly | not observed P inner-field or P–Tₑ |
| Doolgindachbaporn 2022 | ANN/SVM versus IEEE Annex G | 9 large power transformers, WTI/ambient/weather/load | field WTI instrument reading | no small grid-transformer + EVSE coupled test |
| Kunlasing 2022 | monitoring/EV charging control | source body unavailable | unknown | no proof of thermal activation until IEEE source |
| Blomgren 2023 | stochastic RC thermal ODE | 200/400-kVA field P lid; electrical/weather | **measured lid only** | EV ownership not observed EVSE heat data |
| Visakh/Selvan 2023 | IEEE HST/top-oil + charger harmonics + scheduling | simulation; publisher abstract | simulation only | thermal-grid service *risk*, not recorded outage |
| Balogun 2024 | P oil/hotspot ODE + AC P/Q interface co-simulation | battery parameter measured input, grid simulated | integrated numerical simulation | modeled P–Tₑ interface, not heat-driven field response |
| Fletcher/Khan 2025 | IEC P thermal + temperature-conditioned power control | heat-run-informed model | simulation; Part 2 field pending | temperature→charger power already prior art |
| Krama 2026 | approximate `Tj=Tc+Zth Ploss`, empirical quadratic/cross-term | actual EVSE rectifier+ambient+AC/DC+SOC/harmonics | held-out offered-power sessions on one charger | **Tₑ-only**, not upstream P transformer heat |

Each row is a study-dependent evidence ceiling; sources with only abstract remain explicitly restricted. Never assign `INDEPENDENTLY_VALIDATED_COUPLED_INTERFACE` to any row without a measured receiving P or Tₑ state/thermal action.

## 4. Adversarial novelty and research-gap finding

**Established prior art — do not claim “first”:**

1. Transformer ambient/load-dependent thermal ODE/PDE and resistance/cooling models.
2. Field measured/calibrated transformer oil, housing/lid, winding sensor/indicator.
3. EV-demand effects on simulated transformer thermal stresses, aging and technical limits.
4. Transformer-temperature-constrained EV charging control and its modeled energy consequences.
5. Grid/EVSE multiscale power co-simulation including transformer transient heat.
6. Real hot-climate rectifier thermal derating, empirical predicted offered power and operational charging duration.
7. Physics-informed neural networks, nonlinear data-driven predictors and stochastic grey-box transformer thermal models.

**Bounded working gap, NOT established global research absence:** Among physically inspected articles and the limited abstract records above, no independently verified **single site** supplies both actual utility P transformer's thermal response and EVSE's genuine heat-activated controller/capability, along with measured **both directional** thermal state-time propagation and separately defined actual electricity and mobility service obligations with independent coupled-system holdout validation. This possible intersection must be **falsified by continuing comprehensive search, checking RACE Part 2 field study and obtaining Gong 2015/Kunlasing 2022 originals**, not presumed unique. The two directions may independently fail qualification.

**Supervisor-facing bottom line:** Mathematics and thermodynamics must specify *admissible physical states, units, conservation and conditional interface laws first*. The research novelty, if any, lies in **what additional connected mechanisms and testable service/temporal claims survive evidence**, not in a fashionable learning algorithm.

## 5. Conditional methodological strategy (not a selected model)

**Default minimum:** verified \(P_{\mathrm{loss},P}(I,V,\mathrm{THD},T_P)\) and \(Q_P\); \(P_{\mathrm{loss},E}=P_{AC}-P_{DC}\) and \(Q_E\); real operating-limit action mapping; documented port power and the proper heat-state observability; continuous physical time dynamics and discrete thermally activated controls only when documented.

**Physics-only pathway:** derive dimensionally consistent state ODE/PDE or thermal network (and applicable electrical AC balance), check limiting cases, positivity/energy consistency, solver convergence, parameter ranges and sensitivity, and compare component physics to admissible public field anchors; **never call system-level simulation “field validated.”**

**Measured-data pathway (only if lawful suitable raw data):** predeclare state estimator/model identification, training and nonoverlapping heat/event/asset holdouts, uncertainty quantification, model-form/parameter uncertainty and temporal resolution, physics-only baseline and an optional grey-box/PINN alternative. Compare same measured \(T_P,T_E,P_{AC},P_{DC}\) and real relevant service target; account for 1-min electrical vs 5-min thermal sample timing and independent asset transfer. A calibrated empirical \(P_{off}(T)\) is not in itself a physics-informed neural network.

**No available coupled field site:** validate isolated components against their **own** measurements, mark interface numerical coupling **simulation**, and explicitly negotiate scope/evidence standards with adviser once factual barriers are documented. Never fabricate a utility thermal setpoint, charger manufacturer event flag, SOC-to-trip obligation or delay.

## 6. Remaining systematic-review work — transparent completeness register

**Completed:** 5 Scopus search exports with EID count reconciled; 37,376 unique bibliographic candidate IDs; AI-assisted priority triage; 30-paper full-text request queue; Krama **original** publisher article and five previous full source texts, plus JRC 2018 institutional PDF, Gong 2012 author full text, Doolgindachbaporn 2022 author full text and Villarroel publisher-indexed content. A detailed source-specific fulltext **Tranche 1** and Krama original analysis exist in upstream PR #90/#92.

**Not completed:** independent eligibility screening of all 37,376; methodologically validated retrieval sensitivity across all databases (the Trentadue and Balogun seed misses); Scopus search history audit for all five exact executed strings; licensed WoS/IEEE/Compendex full exports; source-specific original full texts for all 30 priorities (especially Gong 2015 and Kunlasing 2022); PRISMA inclusion flow; an independently checked global novelty absence claim; actual original Krama numerical dataset; paired P–Tₑ physical site; system-level causal/independent validation.

**Document label:** `SOURCE_GROUNDED_CORE_PHYSICS_MATH_LITERATURE_SYNTHESIS_COMPLETE_FOR_AVAILABLE_ORIGINALS`. It would be scientifically false to label it `SYSTEMATIC_SCOPING_REVIEW_COMPLETED` or `THESIS_MATHEMATICAL_MODEL_VALIDATED`.
