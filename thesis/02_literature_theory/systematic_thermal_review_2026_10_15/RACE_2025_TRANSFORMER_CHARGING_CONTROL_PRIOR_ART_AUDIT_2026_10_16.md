# Direct prior-art counterexample — Fletcher & Khan / RACE for 2030 (2025)

**Identity:** Fletcher, J. and Khan, O. (2025). *Maximising Electric Vehicle Fast Charging by Improved Thermal Management of Distribution Transformers.* RACE for 2030, Project 23.ET8.R.0571, March 2025, 32-page official [final report PDF](https://www.racefor2030.com.au/content/uploads/Final-report-0571-FINAL-FINAL.pdf).

**Access verification:** Official RACE source PDF opened in web PDF-text viewer, 32 pages; executive summary PDF pp.3–6, technical background pp.8–11 and charging control PDF pp.25–27 inspected in extracted text. Original raw test runs and site field traces **NOT obtained**. No claim that every figure pixel/appendix has been independently audited.

## What is already accomplished (this must shift novelty boundary)

1. **Transformer thermal physics under EV charging:** Uses an IEC 60076-7 based dynamic hot-spot and oil-temperature transformer model with fine time stepping, EV charging profile sequences and ambient/non-EV feeder loading; transformer heating is slower than electrical charging power. Model uses published loading guides and heat-run-informed parameters (PDF pp.3, 8–11).
2. **P-temperature-conditioned EV charging limit:** Implements **four-level hysteresis controller** that dynamically adjusts charger power as *modeled* winding hotspot crosses stated thresholds. Reports predicted electrical energy served versus requested charging demand (PDF pp.25–26; article control analysis). **Therefore mathematical P→Tₑ temperature-triggered capability control and modeled charger service consequences are not unexamined concepts.**
3. **Interdependency timing/charging access:** Investigates varying inter-session gaps/congestion and time-dependent transformer thermal inertia for a modeled 1 MVA transformer and 250 kW charger configurations (PDF executive summary pp.3–5).
4. **Explicit empirical deficit:** Defines Part 1 as desktop/modeling feasibility; **Part 2 proposes two instrumented field transformers**, one with mineral oil and one ester oil, for future longitudinal data, temperature validation and optimized limits. The Part 1 report does NOT establish that Part 2 measurements actually happened or were published (PDF pp.3–6, 29–30).

## How this constrains active thesis

- It is now **incorrect** to say no one has modeled a transformer hot-spot state condition controlling EV charging or charger energy deliveries under ambient/load assumptions.
- The remaining **working novelty hypothesis** must be examined against this and other counterexamples: evidence-qualified *actual* extreme-heat P↔Tₑ directional thermal mechanisms (possibly Tₑ→P charger derating), independently measured and validated propagation/event times, and separately specified electricity and actual **mobility service** requirements. This is a test hypothesis, NOT a confirmed absence of such research.
- Only **actual** field source/receiver time series and operator thermal-limit actions would qualify same-site empirical P→Tₑ; a model hysteresis trigger does not convert predicted charger power to a field observation.
- Part 2 **could contain critical new data and/or prior art**; verify with Essential Energy/RACE/UNSW scholarly publications or authorized data inquiry **before** freezing novelty.
- Quantities such as hot-spot trigger temperatures or MVA emergency multipliers in the report are **scenario-specific**, not transferable general transformer standards/limits for the thesis selected installation.
- A PINN/grey-box model by itself is not novel or preselected.

**Source-level provenance:** https://www.racefor2030.com.au/content/uploads/Final-report-0571-FINAL-FINAL.pdf — cite specific PDF pages indicated above. No copyrighted full text reproduced.
