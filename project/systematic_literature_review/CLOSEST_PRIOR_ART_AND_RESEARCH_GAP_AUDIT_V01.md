# Prior-art counterexample and proposed research-gap audit v1.0

**Date:** 2026-11-03. **Status:** preliminary negative-evidence tests; **NOT certified global novelty**. Source-specific claim/evidence in [extraction matrix](./FULLTEXT_MATHEMATICAL_EVIDENCE_MATRIX_V01.csv).

| Proposed novelty (hypothesis) | Strongest currently found predecessor | Judgment and what remains to test |
|---|---|---|
| "First thermal modeling of transformers under EV charging" | Hilshey 2013 DOI 10.1109/TSG.2012.2217385; Gong 2015 DOI 10.1109/TSG.2014.2365452; RACE 2025 report | **REJECT**: transformer+EV thermal charging precedents exist |
| "First real EVSE heat/charging derating" | Krama et al. 2026 DOI 10.1016/j.ecmx.2026.101960; earlier Qatar 2025 conference context | **REJECT**: measured hot-weather commercial charger derating exists |
| "First physics-informed transformer thermal PINN" | Bragone et al. 2022 DOI 10.1016/j.epsr.2022.108447; conference-family/IEEE 2022 papers | **REJECT**: transformer 1D PDE PINN and real field input are prior art |
| "First physics-informed EV thermal predictive model" | Cao et al. 2026 DOI 10.1016/j.applthermaleng.2026.130776; Acker et al. 2025/26 DOI 10.1007/s41104-025-00157-7 (physics/MPC, not a PINN) | **REJECT broad claim**: vehicle thermal physics-informed/control models already exist |
| "First combination of EV response and transformer dynamic thermal ratings" | Pan et al. 2025 DOI 10.1049/hve2.70024 | **REJECT** for planning/modeling; check whether source offers recorded measured connected thermal restriction |
| "First physically connected transformer-to-charger field electrical measurements" | Li/Chang/Lu 2026 DOI 10.1109/PESGM58988.2026.11693150 | **REJECT** for electrical metering; thermal sensors and site-level controls unknown |
| "First model of thermally conditioned charging-energy consequence" | RACE 2025; Krama 2026; Hilshey/Gong | **REJECT** for broad simulated/charger performance link; critical time/mobility-commitment specificity remains |
| "Validated dynamic causal P↔EVSE thermal interface + actual same-site service loss/recovery" | Most relevant current partial predecessors: Li electrical field; Krama charger field; RACE model/heat-run | **OPEN, NOT NOVELTY CERTIFIED**. Search exact same-site transformer+EVSE oil/hotspot/rectifier + AC/DC + restriction events + mobility requirements; inspect literature and field source material |
| "Transport-to-power changes thermal state because charger derates" | General first-law coupling; electrical metering (Li) + charger field derating (Krama) at separate installations | **MECHANISTICALLY PLAUSIBLE but NOT IDENTIFIED AT ONE FIELD SITE**. Concomitant weather, load/SOC/controller and meter-boundary controls essential |
| "Service transition lag is distinct from heat time constant" | Existing transformer dynamic rating, battery charging and infrastructure viability timing | **CANDIDATE RESEARCH REFINEMENT**, not guaranteed new concept; exact strongest timing-specific predecessor search needed |

### Bounded potential contribution, conditional on evidence

> Establish and test a minimal physics-based state–time formulation linking **qualified** transformer and EVSE thermal capability mechanisms to actual electricity and electrified mobility service consequences under common extreme-heat forcing, explicitly distinguishing equipment thermal response, interface activation/propagation time, and service deadline onset; compare to uncoupled/static or simpler learned alternatives under matched validation, and quantify what cannot be identified from separate component datasets.

This is a **candidate objective statement**, not a demonstrated new result. If no instrumented connected field data exist, report **conditional physics modeling of those links**, calibrate only separately observed components, and do not claim a field-validated bidirectional coupling law.

### Requisite falsification searches

- Search site-specific **transformer oil/winding, charger rectifier/heatsink, AC metering, derating events, battery SOC, fleet deadlines** as combined and separate concepts.
- Include operator thermal protection, transformer constraint → charger service; charger temperature → AC power → transformer loading. Search technology-specific terms (DC fast charger/depot/e-bus/EVSE) and 2025–2026 studies.
- Seek full RACE Part 2 or related results and peer-reviewed literature citing Hilshey, Gong, Pan, Bragone, Li and Qatar study.
- Ensure dated database-native searches and manual study-family resolution before public novelty claims.

**Unresolved scientific claim is not a claim of uniqueness.** Explicitly search and report the strongest contradictory evidence before final thesis gap freeze.
