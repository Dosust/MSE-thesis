# Primary-source reading: Qian, Zhou & Yuan (2015) — EV charging / transformer thermal aging

**Reading date:** 2026-11-05  
**Evidence status:** Original university-hosted author-accepted manuscript text and publisher/journal bibliographic metadata inspected; full published layout/figures and independent original data/code reproduction remain unverified. **Researcher screening and JBI formal inclusion not yet performed.**  
**Article:** Qian, K., Zhou, C., & Yuan, Y. (2015). *Impacts of high penetration level of fully electric vehicles charging loads on the thermal ageing of power transformers.* *International Journal of Electrical Power & Energy Systems, 65*, 102–112. DOI: https://doi.org/10.1016/j.ijepes.2014.09.040  
**Historical ambiguity resolved:** Online release 2014-10-17; publication issue February 2015. Use 2015 in citation. Manuscript displayed an extra Jiaqing Zhao author not in final journal metadata; preserve identity variant but follow final publisher bibliographic entry until checked.
**Sources:** University author's manuscript https://researchonline.gcu.ac.uk/ws/files/6078356/FEV_transformer_paper_IJEPS2014oct.pdf ; institutional publication https://researchonline.gcu.ac.uk/en/publications/impacts-of-high-penetration-level-of-fully-electric-vehicles-char/ ; publisher https://www.sciencedirect.com/science/article/abs/pii/S0142061514005912.

## Research problem and evidence role
Model **Transportation-to-Power (T→P)**: stochastic EV charging profiles → feeder/transformer electrical loading → winding hot-spot temperature (HST) → transformer insulation-aging/loss of life. **Strong provisional CORE model comparator** for SO1/SO2; supporting charging policy scenario comparator for SO3, but formal human JBI eligibility pending.

## Original equations inspected (author manuscript printed equation numbers)
- Eq. (1) assigns vehicle initial state of charge as a travel-distance-derived variable, under linear range/SOC and days-between-charge assumptions. Probabilistic travel distance, charging start time, charging mode feed vehicle power demands; units/parameters must be reconciled to current vehicles if reproduced.
- Eq. (3) piecewise charging power curve, including taper after an initial plateau. Paper's illustrative assumptions: 3.5 kW Mode 1; 6.6 kW Mode 2; 40 kW Modes 3/4 for its 25-kWh vehicle battery (period- and apparatus-dependent, **not** modern charging standards).
- Eq. (4): time-averaged equivalent thermal aging factor: `F_EQA = (Σ_n F_AA,n Δt_n)/(Σ_n Δt_n)`; 48 half-hour periods per modeled day.
- Eq. (5): `F_AA,n = exp(15000/383 - 15000/(Θ_H,n + 273))`; paper cites IEEE C57.91-1995; Kelvin reference convention and edition applicability must be checked before transcribing to thesis model.
- Eq. (7): `Θ_H,n = Θ_A,n + ΔΘ_TO,n + ΔΘ_H,n`, i.e., ambient + top-oil rise + winding hotspot gradient over top oil. Subsequent manuscript equations model thermal transients with oil/winding time constants.
- Table III: **assumed** two-transformer thermal characteristics: for 33/11.5 kV vs 11/0.433 kV equipment, top-oil rated rises 65 vs 55 °C, hotspot-over-oil rises 30 vs 20.3 °C, oil thermal time constants 3.5 vs 3.0 h, winding time constants 4.8 vs 10 minutes (values adopted from cited sources, not individually field-fitted in this study).
- The model considers both ambient and load-driven temperature variation; do not treat HST as an independently measured validation outcome.

## Data, scenarios and evidence ceiling
- Study system: generic UK 33/11/0.4 kV model with residential, industrial and commercial feeders; original UK load profiles and half-hourly 2010 Scottish meteorological ambient input; **transformer hot spots and incremental loss-of-life are calculated**.
- Scenario A uncontrolled domestic, B off-peak domestic, C smart domestic, D public charging shift. EV penetration sensitivity 0–50%.
- Main modeled finding: EV penetration, charging start time and ambient temperature affect transformer aging; coordinated smart charging generally mitigates modeled life consumption. Relocation of charging to commercial/industrial zones may shift—not eliminate—transformer congestion or aging.
- Critical explicit paper limitation: ambient temperature effects on **EV battery charging characteristics** omitted, despite ambient being an input to transformer thermal behavior (original manuscript discussion around Eq. 6). Weekday-focus and illustrative charger profiles also limit generalization.
- No independent measured winding-HST validation, no direct EVSE rectifier temperature or thermal derating, no observed feeder topology/control feedback closing P→T, and no observed mobility service delay presented in inspected manuscript. Avoid stronger global absence claims without full materials audit.

## Benchmarking transfer to our thesis
**Provisional comparator:** reproduce the paper's `EV demand → transformer load → HST → FAA/life loss` scenario chain (subject to source data and parameter access); compare with physically appropriate transformer ODE/DAE and the conditional PINN benchmark using **identical temperatures, loads, splits, available forcings and computational budgets**. Independent SINTEF measured HV/LV HST named sensor channels may validate component-level prediction, **not** this UK network or extreme-heat coupled field interaction by themselves.
- Physical metrics: HST MAE/RMSE [°C], thermal-limit onset [min] when thresholds observed, aging acceleration/relative life consumption [dimensionless, hours or % with proper context].
- Coupled-system metrics for proposed future work: whether increasing thermal state causes allowed charging power derating, delivered-versus-requested energy [kWh], delay/departure service [min, %] and lag, **only field-causal if connected observations or controlled interventions justify**; otherwise labeled modeled counterfactuals.
- Mandatory falsification: a T→P modeled thermal aging chain **already existed by 2015**; novelty cannot be asserted merely for linking EV charging to transformer temperature/aging, introducing stochastic starting SOC, or simulating smart charging.

## Review action and unresolved verification
1. Human reviewers assess eligibility under approved researcher protocol v0.3 and record source/decision separately from this analyst extraction.
2. Confirm final journal manuscript author differences (repository lists four on draft while publisher cites three), print equation notation, measured-versus-assumed parameters, original references and table values.
3. Check reproducibility: original real-load and ambient series downloadable? scenario code available? numerical step size and transformer table consistent?
4. Assess applicability to modern high-power EVSE and extreme heat; do not import 2015 scenario assumptions as measured 2026 system facts.
5. Cross-compare with Bragone 2022 transformer PINN/FVM and Qian et al. 2015 physically driven aging, then use evidence gates to determine robust HST and interdependency metrics.
