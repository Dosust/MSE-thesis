# Full-text tranche 2 — additional accessible prior-art tests

**Date:** 2026-10-17. **Status:** Three additional publicly accessible **original source texts** closely examined; their access levels differ from publisher PDFs. These are research verification notes, **not** final full review selection. Their scientific claims and limits below are source-specific.

## A. Trentadue et al. (2018): original institutional published PDF, 13 pages

**DOI:** [10.3390/en11081937](https://doi.org/10.3390/en11081937). Original European Commission JRC hosted PDF: https://ses.jrc.ec.europa.eu/sites/default/files/publications/evaluation_of_fast_charging.pdf. PDF text viewer, pp.3–11; key experimental Tables 4/5 pp.6–7, original PDF publisher version. This study was missing from the five initial Scopus-query records and must be added by reference/citation-chain selection, NOT counted as a retrieved Search 1–5 EID.

**Physical study:** Seven commercial DC fast-charger units and two EVs in a climate chamber, ambient **25°C, 40°C, −15°C, −25°C**, combinations including CCS and CHAdeMO. Actual measured three-phase AC input and EV plug DC output V/I. The original paper separates efficiency \(\eta=P_{DC}/P_{AC}\) from the **integral energy** ratio \(\mathrm{ERR}=E_{AC}/E_{DC}\) (pp.3–4), which depend on charging SOC and actual power. Charger efficiency at 25°C about 90–93% for normal charging regimes; cold temperatures can force battery-limited power and larger efficiency decline (e.g. 39% one measured case at −25°C), but **+40°C was generally tolerated with minor power changes** in tested hardware (Tables 4/5, original discussion).

**Physics inference:** Ambient-only temperature comparisons do not uniquely separate battery management from EVSE device thermal derating; no rectifier `T_E(t)`, semiconductor junction heat or external P transformer thermometry. Laboratory protocol not an actual extreme-heat P–Tₑ coupled distribution field test. These results provide **counterevidence to an assumption that every charger derates strongly whenever ambient reaches 40°C**, and qualify that Krama's stronger effects at 50–55°C on an air-cooled unit may depend on hardware and exposure threshold.

**Validation tier:** `CHARGER_ELECTRICAL_LAB_OBSERVED`, no first-principles charger thermal ODE and no field-coupled P receiving heat.

## B. Gong et al. (2012): coauthor-posted full 6-page conference manuscript

**DOI:** [10.1109/EnergyTech.2012.6304673](https://doi.org/10.1109/EnergyTech.2012.6304673). Coauthor Rizzoni's public full-text article: https://www.researchgate.net/publication/261459662_Distribution_transformer_tests_for_PEV_smart_charging_control. **Author-posted full source in accessible HTML text**, not an independently downloaded IEEE version; OCR-like page text corrupts some printed equations. Retain exact source formula anchors but visually reverify before computational reuse.

**Physical experiment:** 25-kVA off-the-shelf oil transformer heated under **low-voltage DC test environment** with thermocouple placements to measure oil temperature; output includes top-oil and tank flank gradients. Standard IEC/IEEE thermal top-oil dynamics (original Eq. 8) related load ratio, oil heat rise, ambient, viscosity and time constant. Original Eq. (14) `R_w=R_0(1+alpha DeltaT)` indirectly infers *winding-average temperature rise* via resistance, but not actual internal winding **hotspot** temperature. Authors explicitly state actual winding hotspot thermometry and charging-controller experiments remained future work.

**Validation:** The tested top-oil model was compared against actual measured top-oil steps; under partial DC excitation the power-loss mechanisms may not identically replicate a fully powered AC distribution transformer; don't claim independent utility operating-site validation. A paper about **PEV charging** in title is not automatically a *real coupled EVSE site*.

**Key integrity distinction:** **This is Gong (2012), not Gong et al. (2015)** DOI 10.1109/TSG.2014.2365452. The 2015 journal abstract advertises both EV control and experimental validation, but cannot be assumed to repeat the exact 2012 experiment or include/omit a particular 2015 measured sensor/control action absent that original full text.

**Validation tier:** `MEASURED_P_TOP_OIL_LAB`, `INDIRECT_WINDING_MEAN`, `NOT_MEASURED_HOTSPOT`, `NOT_OBSERVED_P_Te_FIELD_INTERFACE`.

## C. Doolgindachbaporn et al. (2022): coauthor-posted entire IEEE article text

**DOI:** [10.1109/TPWRD.2021.3123957](https://doi.org/10.1109/TPWRD.2021.3123957). Coauthor Wilson's uploaded full article text: https://www.researchgate.net/publication/355861847_Data_Driven_Transformer_Thermal_Model_for_Condition_Monitoring. Southampton author repository PDF identity: https://eprints.soton.ac.uk/453227/1/Data_driven_transformer_thermal_model_for_condition_monitoring.pdf (403 download in current web viewer), so claim **author-posted full article text read**, not verified downloaded publisher PDF.

**Physical scope and data:** Utility **power** transformers (not chosen distribution class): two 180 MVA, four 240 MVA, three 1000 MVA, historical records over **seven years**, measurement variables load, tap position, winding-temperature-indicator (WTI), ambient temperature, wind speed and solar radiation. WTI is an observation of instrument behavior *indicative of* hot-spot temperature, not proof of a direct measured winding maximum. Model classes nonlinear autoregressive ANN and SVM; authors compare to IEEE C57.91 Annex G physics reference and report improved actual field WTI prediction; an incipient anomaly detection demonstration uses measured utility data.

**Math:** ANN/SVM temporal prediction and sum-square measured WTI loss; not a PINN with heat PDE residual and not a new transformer energy conservation law. Its evidence is a counterexample to claims that **only physics-based models have ever been tested against utility transformer temperatures**. The large power asset's thermal capacitance, fan/cooling architecture, network loads and instrumentation differ radically from a 25–400 kVA distribution transformer; no direct model-coefficient transfer without recalibration.

**Validation tier:** `FIELD_WTI_PREDICTION_MEASURED`, `OBSERVATIONAL_AI_BASELINE`, `LARGE_POWER_TRANSFORMERS`, `NO_EVSE_HEAT_OR_INTERFACE`.

## Novelty consequence across these additions

Trentadue adds **actual charger laboratory electricity-power results** and climate-dependent battery/controller confounding; Gong 2012 adds **measured small distribution transformer top-oil transients** under a qualified special lab protocol; Doolgindachbaporn adds **multi-unit measured utility field WTI prediction** with ML models. None is a **same-site** record of extreme-heat-activated EVSE derating with independently measured upstream P thermal receiving response, but this evidence absence is only within the accessed papers, not a universal publication absence.

**Important remaining original-source restrictions:** Gong **2015** and Kunlasing **2022** full IEEE sources still unavailable. Swift **2001** publisher abstract only; Seier **2015** university research report chapter and publisher abstract identified, not an original journal full equation audit. RACE 2025 Part 2 instrumented actual transformer trials not verified as published; Krama original raw row-level dataset **requested, not received**.

## Source and data custody

No articles, PDFs, full copyrighted passages, or bulk Scopus abstracts committed; this file holds concise user-authored physical evidence interpretation and direct original-source links. All safety/physics assertions must be checked against original page-rendered math before use in an operational transformer controller.
