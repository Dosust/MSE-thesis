# Priority full-text verification follow-up — thermal P ↔ Tₑ thesis

**Date:** 2026-10-15  
**Evidence method:** Original PDF source + publisher article HTML + third-party textual copy with explicit provenance; not a completed systematic review or a PRISMA screening event.  
**Governing objectives:** current SO1 thermal mechanisms, SO2 physical state-time equations, SO3 transition / propagation and electricity–mobility service consequences.  
**Scope limit:** EVSE and its internal transformer/converter components belong to Electrified Transportation (Tₑ); they are not a separate third physical system or an independently measured Power System distribution transformer.

## Summary of source access

| Record | Obtained this follow-up | Exact access tier | Pages / anchored material | Critical caveat |
| --- | --- | --- | --- | --- |
| **P008 — Godina et al. (2016)** | [Eindhoven University of Technology publisher version PDF](https://pure.tue.nl/ws/files/51547814/1_s2.0_S019689041630334X_main.pdf) | **ORIGINAL_PUBLISHER_VERSION_PDF_TEXT_VERIFIED** | 12 PDF pages including cover, journal pp.206–216, PDF p.5 Eqs.(4)–(24), pp.5–11 scenarios/results | Measured load input profiles + simulated EV charging + modeled transformer thermal outputs. Direct measured HST validation not demonstrated. Figure pixels not inspected (PDF screenshot cache miss). |
| **P010 — Villarroel et al. (2017)** | [IET/CIRED publisher-indexed article text](https://doi.org/10.1049/oap-cired.2017.1102) | **PUBLISHER_INDEXED_ARTICLE_EXCERPTS_EQUATIONS_TABLES** | Journal pp.158–162 (5 pp according to original journal), Sec.2–8; Eqs.(2)–(4), Table 2, Figs.3–6 textual captions | Not a verified downloaded PDF; measurement and independent validation in full publisher article; figure image pixels and raw test traces not inspected. |
| **P001 — Krama et al. (2026)** | [Elsevier open access abstract](https://doi.org/10.1016/j.ecmx.2026.101960), [Hamad Bin Khalifa University bibliographic record](https://elmi.hbku.edu.qa/en/publications/impact-of-extreme-climatic-conditions-on-fast-ev-charger-performa/); [third-party Scribd 16-page text copy](https://www.scribd.com/document/1055961993/Impact-of-Extreme-Climatic-Conditions-on-Fast-EV-Charger-Performance) | **PUBLISHER_ABSTRACT_CONFIRMED; UNVERIFIED_THIRD_PARTY_FULL_TEXT_TRANSCRIPTION consulted** | Official publisher abstract only; third-party text refers to Sect.3–4, Eqs.(5),(8),(9),(11),(12), Fig.3, Fig.9, but not authenticated against publisher PDF | **Original PDF NOT obtained**; equation coefficients/method details from third party remain provisional. Raw measured data “available on request” not acquired. |

### Access limitations honestly retained
The publisher version of Godina was read as original PDF in the web PDF text viewer. PDF screenshot requests failed (cache miss), and direct local download failed due to container DNS/network limitation, so figures could not be visually inspected. The full original article body for Villarroel is publicly indexed as publisher HTML; direct opener sometimes returns HTTP 403 and the publisher's PDF was not acquired. A full third-party transcription of Krama exists but is not publisher-certified. No locally opened numerical dataset, licensed raw measurements, or experimental calibration has been produced by this audit.

## P008 — Godina et al., DOI 10.1016/j.enconman.2016.04.087

**Physical interaction actually investigated:** EV charging at residential or industrial premises is modeled as an additive transformer electrical load; changing charging amount/timing changes inferred transformer load factor; transformer transient thermal model estimates hot-spot temperature; an aging law integrates loss of insulation life.

**Verified mathematical structure, publisher-version PDF journal pp.209–210:**
- Sect.2.2, Eqs.(1)–(3): a log-normal type daily travel-distance probability and a derived initial EV SOC distribution. The EV travel distribution is **assumed/calibrated from an outside travel survey**, not independently observed mobility-service outcome in the island-transformer test.
- Sect.2.3.1, Eqs.(4)–(8): top-oil temperature/temperature-rise dynamics and winding hot-spot rise after load changes, with time constants, load ratio and ambient temperature. In Eq.(8) the total hotspot temperature is expressed as ambient plus the modeled thermal rises; preserve temperature-vs-rise notation when reproducing.
- Sect.2.3.2, Eqs.(9)–(19): ODE/difference-equation forms of the transformer thermal model. **A consistency audit is required before implementing**: the browser's PDF text extraction around Eq.(10) and Eq.(18) has a plus/minus and oil-temperature offset ambiguity; do not silently reconcile or reproduce an unverified variant as mathematically exact.
- Sect.2.3.3, Eqs.(20)–(24): temperature-conditioned paper insulation aging and time-integrated loss-of-life.
- Sect.3.1–3.4: case studies use actual distribution transformer nameplates and baseline electrical demand observations from São Miguel, Azores, while using modeled EV arrival/SOC/charging profiles. Authors explicitly describe computed thermal results as **simulation**.

**Source-supported equations (structural paraphrases, not replacing source equations):**

```math
P_{\mathrm{tr}}(t)=P_{\mathrm{baseline}}(t)+\sum_{j=1}^{N_{\mathrm{EV}}}P_{\mathrm{EV},j}(t);
\qquad
\theta_{\mathrm{HS}}(t)=T_a(t)+\Delta\theta_{\mathrm{TO}}(t)+\Delta\theta_{\mathrm{HS|TO}}(t).
```

```math
\dot{L}_{\mathrm{ins}}(t)=V\bigl(\theta_{\mathrm{HS}}(t)\bigr),
\qquad
L_{\mathrm{ins}}(t_f)=\int_{t_0}^{t_f} V(\theta_{\mathrm{HS}}(t))\,dt.
```

These are equivalent structural relationships, not a verified transcription of every original ODE coefficient. They establish already-existing EV load → transformer **modeled** thermal time evolution. The paper does not establish weather-driven derating feedback from external Power System to EVSE, a matched measured charger/transformer thermal experiment, or actual trip/schedule completion.

**Implication for thesis originality:** EV charging-induced transformer heating/aging and ODE coupling are prior art. Novelty can only arise from a narrower, evidence-qualified extreme-heat **bidirectional or directional capability, propagation-time, observability, uncertainty and validated service** contribution.

## P010 — Villarroel et al., DOI 10.1049/oap-cired.2017.1102

**Physical experiment:** 200 kVA, 11/0.433 kV mineral-oil ONAN distribution transformer equipped with **16 installed internal fibre-optic temperature sensors**; tested at constant 0.7, 1.0, 1.25 p.u. loading to fit transient IEC-model coefficients. External thermocouples measured radiator/oil temperatures; fibre optic thermometers directly measured winding hot-spot temperatures.

**Governing model and parameters (original publisher article Sec.6 and Table 2):** Eq.(2) gives steady-state top-oil rise under transformer load `K` with oil exponent `x`; Eq.(3) gives winding gradient vs load exponent `y`; Eq.(4) defines root-mean-square deviation against actual fibre-optic HST test measurements. Original paper's Table 2:

| Parameter | Case 1 IEC nominal | Case 2 external sensors | Case 3 internal sensors |
| --- | ---: | ---: | ---: |
| Oil exponent `x` | 0.80 | 0.82 | 0.79 |
| Winding exponent `y` | 1.6 | 1.4 | 1.5 |
| Oil time constant `τₒ`, minutes | 180 | 216 | 244 |
| Winding time constant `τw`, minutes | 4.0 | 9.6 | 9.4 |
| Hot-spot factor `H` | 1.1 | 1.1 | 1.5 |

**Independent overload validation:** A distinct two-step load profile of 0.7 p.u. for 17 h → 1.8 p.u. for 2 h → 0.7 p.u. for 4 h was performed. The reported HST RMS deviations were **12.4, 6.2, 2.2 °C** respectively for nominal-IEC parameters, external-sensor-derived parameters and internal fibre-optic-derived parameters (publisher HTML Sec.7.1). The authors additionally report a maximum discrepancy of 4°C for the internally calibrated model.

**Precisely what this validates:** independently observed **transformer winding HST** predictions at controlled transformer equipment. It is not a field experiment of EVSE/transport interdependency and does not verify extreme ambient heat in an operating EV-charging site. It **directly demonstrates that parameter identification and internal sensor placement matter**—a high-value grey-box experimental methodology precedent.

**High-rigor nuance:** Here “independent” means an additional loading-test experiment in the same physical transformer, **not cross-site/device generalization**. An RMSD gain does not justify assuming similar improvement in unrelated transformer/EVSE sites.

## P001 — Krama et al., DOI 10.1016/j.ecmx.2026.101960

**Publisher-supported:** one commercial air-cooled ~50 kW DC fast charger in Qatar with temperatures ~15–55 °C; direct measurements of ambient temperature, internal rectifier temperature, grid-side electrical quantities, offered versus delivered DC charging power, current THD, EV SOC, and observed test charging duration changing from **86 to 169 min**. Publisher abstract reports cross-session and temporal holdout predictive modeling and heat-triggered protective derating (up to 35–40 kW offered-power decline under the tested conditions). Authors: data “available on request”.

**Third-party transcription observed, NOT primary-PDF verified:** a full-page text copy indicates measurements via upstream PQ analyzer, OCPP charger log and wireless cabinet sensors; several quadratic regressions fit `P_offered(T_rect)`, `P_offered(T_ambient)`, hybrid thermal-headroom and `t_charge(T_ambient)`, with cross-session/temporal holdout plots described in Fig.9. Treat these coefficients, test dates, raw sample count, physical sensor mapping and plotted goodness-of-fit values as **provisional** pending an original publisher PDF check; a scraped hosted copy is not a certified source.

**Critical Power System boundary:** the transcription describes a temperature sensor on a *transformer component inside the fast charger cabinet*. This **must not be interpreted as measuring the external electrical distribution transformer in the Power System**. Grid-side voltage/current at the charger's input may show power-quality consequences but not observed external feeder-transformer hot-spot temperature or proven cross-system thermal cascade.

**What is established vs still open:** strong **EVSE component experimental field evidence** and charging-session service evidence, **not** a time-synchronized distribution-transformer ↔ EVSE ↔ actual mobility-trip field dataset. The original publisher PDF, its numerical plots, internal temperature-sensor installation locations, model coefficients and actual raw timestamped files are not verified in this audit.

## Integrated implications for SO1–SO3

| Objective | Evidence now stronger | What remains blocked |
| --- | --- | --- |
| SO1 Qualify directional mechanisms | Godina: modeled EV charging→transformer heat; Krama: observed EVSE heat derating; Villarroel: instrumented grid component thermal physics | Direct matched sector-to-sector measured thermal causal link and tested directionality |
| SO2 Thermal state-time model | Godina's ODEs, Villarroel's independent parameter fits, previous Blomgren grey-box stochastic RC models, Bragone PINN and EV-EcoSim preexisting equations | Specific minimum states/parameters physically identifiable with accessible raw records |
| SO3 Critical times and service | Krama's charger-session charging duration; transformer load/thermal inertia/aging time curves, optically instrumented overload transients | Actual matched cross-interface propagation delay, electricity-service deficits, trip/schedule fulfillment and recovery observed across P↔Tₑ |

**Review decision:** Do NOT claim no prior-art coupling, do NOT assume AI's superiority or freeze physics-informed grey-box; do NOT promote 3 candidates to systematic “included studies”. One additional original PDF (Godina) and one publisher-indexed original article text (Villarroel) have been qualified since the first audit, while Krama remains publisher-abstract + third-party full-transcription level.

**Next evidence gate:** obtain the official Krama publisher PDF (or an institution-supplied original/author-accepted manuscript), request raw charger measurements with a clear data-rights statement, and obtain site-matched distribution transformer inputs/temperatures if claiming empirical coupled-system causal validation. The actual 15-paper pilot corpus is not a systematic review.

### Retrieval channel precision (2026-10-15)
The full indexed publisher article text for Villarroel was accessed through the search provider's publisher-indexed snippets and displayed source excerpts. Directly opening the publisher DOI returned an HTTP 403; no publisher PDF was obtained, locally rendered, or pixel-checked. Attempted LibKey resolution returned a cache miss. The connected Wiley Scholar Gateway also returned an internal connector error. Treat Villarroel as publisher-indexed article text **not a downloaded full publisher file**.\n