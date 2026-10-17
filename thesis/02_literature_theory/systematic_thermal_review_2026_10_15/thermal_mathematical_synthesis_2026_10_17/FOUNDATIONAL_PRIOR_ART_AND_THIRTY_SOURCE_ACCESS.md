# Priority literature synthesis, prior art, and access boundaries (17 October 2026)

## Audit universe and completeness claims

The **30-priority-DOI register** is an acquisition/extraction **queue**, NOT evidence of 30 completed original-full-text scientific reviews. Its as-of-current status:
- **Six original publisher PDF full texts verified within priority 30:** Gong (2015); Kunlasing (2022); Godina et al. (2016); Blomgren et al. (2023); Bragone et al. (2022); Krama et al. (2026).
- **One original author-accepted manuscript** in 30: Qian et al. (2015), DOI 10.1016/j.ijepes.2014.09.040, author accepted version, not publisher final.
- **One original publisher indexed article text** in 30: Villarroel et al. (2017), DOI 10.1049/oap-cired.2017.1102; independent PDF and exact coefficient/transcription cross-check incomplete.
- **Twenty-two priority original full texts** still not verified in this 30-paper acquisition tranche. Their DOI records, abstracts or publicly shown material can inform *triage* but cannot provide claimed source-specific equation numbers, instrument settings or independent validation until the originals are read.
- Additional **outside** this exact 30 register: Balogun et al. 2024 EV-EcoSim author manuscript (arXiv:2401.04705, DOI 10.1109/TSG.2023.3339374) and RACE for 2030 2025 original 32-page institutional technical report (Project 23.ET8.R.0571) were previously audited. These are not to be counted as 30-priority fulltext completions.
- **Original raw rows are not received** for Krama, Gong or Kunlasing. The user reported sending Krama's corresponding-author data request; this is not an independently verified email-send event.

## Source-version hierarchies

1. Exact publisher PDF (IEEE/Elsevier) read against rendered pages and DOIs; record page and equipment mapping.
2. Authorized author-accepted manuscript, explicitly NOT conflated with publisher proof/final.
3. Publisher indexed article body (exact source page not independently inspected).
4. Original publisher bibliographic/abstract statements (no original full-text).
5. Prior audit or third-party index (never count as original).
6. Hypothesis/proposed equation (clearly delimited, NO source attribution).

## Foundational transformer heat physics

**Susa, Lehtonen and Nordman (2005)**, *Dynamic Thermal Modelling of Power Transformers*, IEEE Transactions on Power Delivery 20(1), 197–204, DOI 10.1109/TPWRD.2004.835255. Aalto University institutional record verifies citation identity; publisher/author abstract describes dynamic top-oil and hot-spot thermal models including viscosity/loss dependence, with 250-, 400- and 605-MVA fibre-optic transformer tests. **Original IEEE full paper NOT acquired and detailed formulae NOT transcribed** in this tranche. Associated Susa 2005 original doctoral monograph exists at AaltoDoc (https://aaltodoc4.aalto.fi/items/a85f70fe-76ad-4053-b305-03f55071067d), but a thesis monograph is NOT proof of verbatim original IEEE paper equations. **Next action:** ASU institutional IEEE copy, verify exact dynamic equations, loss nonlinearities, boundary/initial conditions, measured vs modeled hotspot and fibre sensor positions. Sources: https://research.aalto.fi/en/publications/dynamic-thermal-modelling-of-power-transformers/ ; https://doi.org/10.1109/TPWRD.2004.835255 .

**IEEE loading standard status correction:** IEEE **C57.91-2025 is currently active** and published 2026-03-05, superseding C57.91-2011 (inactive/reserved). Official IEEE SA primary status: https://standards.ieee.org/ieee/C57.91/7163/ . It covers load-dependent thermal ratings, temperature criteria, ageing, modes and cooling conditions. **Only official scope/status verified; original complete standard contents NOT read.** Do not cite numerical hotspot limits or copy assumed Annex-G formula with current-2025 normative authority until ASU authorized original inspected.

**IEC 60076-7:2018** official IEC primary metadata: https://webstore.iec.ch/en/publication/34351 . Guide for mineral-oil-immersed power transformers, ambient/thermal loading/insulation ageing; revised thermal models stated on official product page. **Only full scope/public summary verified, original technical formula pages not inspected**. When implementing compare device type/cooling to standard applicability, validate selected equation edition and test type before compliance claims.

**Gong et al. (2015)** original source confirms dynamic transformer model fundamentally credited to Susa [22] and prior Gong [18], while Gon g's Eq.(1) is **load ARMA** and Eq.(9) is calibration loss. The observed top-winding is **not** actual measured hotspot; normalized thermal time constants depend on location/equipment and should not be swapped for hotspot time constant.

## Additional fulltext-derived prior art from existing thesis source audit

| Source | Governing model/observable | Evidence class | Interdependency conclusion |
|---|---|---|---|
| Godina et al. (2016), DOI 10.1016/j.enconman.2016.04.087, original publisher PDF previously read | IEC-style top-oil/winding thermal transients and ageing under EV load profiles | Measured baseline loading + simulated EV profiles/transformer thermal output | EV electric demand→modeled P heating is NOT novel |
| Blomgren et al. (2023), DOI 10.1016/j.segan.2023.101048, original publisher PDF previously read | Stochastic RC oil/lid thermal state with measured transformer current, weather and lid; 6h lid MAE ~0.4–0.6°C | P-device field lid validation only | Measured lid is NOT hotspot, nor paired EVSE thermal state |
| Bragone et al. (2022), DOI 10.1016/j.epsr.2022.108447, original publisher PDF previously read | Simplified 1D heat PDE with thermal PINN; field oil/ambient boundaries vs finite volume | Measured boundary + **numerical** internal field reference | PINN vs FVM is NOT independently measured spatial winding-field validation; verify volumetric unit normalization |
| Qian et al. (2015), DOI 10.1016/j.ijepes.2014.09.040, author accepted manuscript | Thermal hotspot/insulation-ageing under stochastic EV electrical demand and weather | Real load/weather inputs + simulation charging profiles | Source explicitly does not model ambient's direct effect on EV charging battery behavior |
| Villarroel et al. (2017), DOI 10.1049/oap-cired.2017.1102, publisher indexed fulltext sections | IEC-style oil/hotspot and direct optical winding sensors in transformer lab | P hardware HST calibration plus independent overload test | No connected EVSE or cross-domain thermal receiver |
| Balogun et al. (2024 EV-EcoSim), DOI 10.1109/TSG.2023.3339374, original author arXiv MS | Transformer thermal ODE + electric EVSE real/reactive power exchange in grid/charger co-simulation | Co-simulation + battery component experimental parameter input; journal version not reconciled | Multiscale electric EVSE↔transformer model itself is existing prior art |
| RACE for 2030 (2025) project 23.ET8.R.0571 official report | IEC-type transformer HST thermal evolution and four-level hotspot-temperature hysteresis charging curtailment | Standards/heat-run informed **simulation**; instrumented phase 2 results not confirmed | Temperature-conditioned P transformer restriction of charging is ALSO existing prior art |

Detailed previously extracted source locators remain in \`fulltext_extraction_2026_10_16/EQUATIONS_PHYSICS_EVIDENCE_REGISTER.csv\`. Do not elevate a model-only validation to hardware field proof, or a paper indexed body to exact source PDF.

## New public bibliographic/abstract triage — NOT new original-fulltext completion

- **Seier, Hines, Frolik et al. (2015)**, *Data-Driven Thermal Modeling of Residential Service Transformers*, DOI 10.1109/TSG.2015.2390624; indexed abstract indicates physically instrumented 25-kVA residential transformer and comparison against IEEE Annex G. Original IEEE paper not acquired. https://doi.org/10.1109/TSG.2015.2390624
- **Doolgindachbaporn et al. (2022)**, *Data Driven Transformer Thermal Model for Condition Monitoring*, DOI 10.1109/TPWRD.2021.3123957; IEEE abstract reports nine transformer measurement cases (180, 240, 1000 MVA) and machine-learning thermal comparison. Original complete equations not read. https://doi.org/10.1109/TPWRD.2021.3123957
- **Bai et al. (2024)**, *Residential Electric Vehicle Charging Demand Analysis for Distribution Transformer Expansion Planning Considering Dynamic Transformer Rating*, DOI 10.1109/PESGM51994.2024.10688510; abstract describes real EV charging profiles under varying ambient T and dynamic transformer rating. Original conference full text unverified. https://doi.org/10.1109/PESGM51994.2024.10688510
- **Jia, Donaldson and Zhang (2023)**, *Impact of temperature on EV charging and the distribution network*, DOI 10.1049/icp.2023.3126; original IET record verified but full paper not obtained. https://doi.org/10.1049/icp.2023.3126
- **Visakh and Selvan (2023)**, *Analysis and mitigation of the impact of electric vehicle charging on service disruption of distribution transformers*, DOI 10.1016/j.segan.2023.101096; publisher preview/abstract indicates modeled overload/thermal impact. Do not imply actual observed distribution-transformer service interruption. https://doi.org/10.1016/j.segan.2023.101096

## Novelty exclusion and falsification

**Already established in prior art:**
(a) P transformer thermal ODEs, standards and ageing under EV load;
(b) empirically tested P transformer temperature response under EV-like scheduled electrical loads;
(c) monitoring utility transformer oil and controlling EV charger current via an ICT interface;
(d) empirical extreme-heat EVSE offered-power derating;
(e) transformer-hotspot-conditioned charging-control simulations;
(f) two-way grid/charger **electrical** co-simulation.

**Not yet established by these sources as a combined independent field result:** a time-synchronized real operating EVSE thermal state, intervention/limit signal, actual AC/DC electrical exchange, utility transformer oil/winding thermal receiving response, independent confounder-controlled attribution, and critical EV trip/departure energy service requirement under extreme ambient stress.

That last statement is a **bounded gap in the sources actually reviewed**, not a globally proven novelty claim or assertion that the full 30-paper/global search is complete.

## Acquisition queue — recommended order

1. Susa et al. (2005) full original IEEE article through ASU; original current IEEE C57.91-2025 and IEC 60076-7:2018 via authorized institutional standards access. Check equations/editions and avoid derivative copies claiming compliance.
2. Highest-priority unread EV+heat experiment: Seier et al. (2015), Doolgindachbaporn et al. (2022), Bai et al. (2024), Jia et al. (2023), and Visakh and Selvan (2023); prioritize full source availability and equation/validation detail, not citation count.
3. Complete the 22 remaining priority originals iteratively using DOI-authenticated institutional access or lawful author manuscripts; archive DOI, version, source pages, figures, sensor metadata, controlled actions and validation labels.
4. Krama raw experiment author response awaited; **do not hold theoretical derivation**, but do not claim identified charger \(C_c,G_{ca},\alpha\) or joint site validity without appropriate observations.

**Outcome of this tranche:** original-source comparative synthesis completed for three critical papers; foundational availability/status assessed; v0 physics derived; VVUQ tests specified. No universal novelty proof, no thesis-specific experimental validation, no complete 30-fulltext review yet.
