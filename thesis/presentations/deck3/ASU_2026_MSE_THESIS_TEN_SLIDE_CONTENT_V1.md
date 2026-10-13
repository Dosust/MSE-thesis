# MSE Thesis — Official ASU 2026 Ten-Slide Presentation Content V1

**Status:** User-requested **working presentation variant**; native Google Slides created 2026-10-13. Not a research science freeze, a separate canonical eight-slide/three-minute Deck3 variant, or validated coupled-system result.

**Native Google Slides:** https://docs.google.com/presentation/d/1q6ts7HL1tlmJeo5ac8NROHOCASTbU4LlIK0TVNR87Ls/edit?usp=drivesdk

## Slide 1 — Thesis Title
**Physics-Based Mathematical Engineering of Power–Electrified Transportation Interdependencies for Resilience**
- Extreme heat; physical state and time; required electricity/mobility services; sustainability.
- Dossiya Dakou — Arizona State University — MSE Sustainable Engineering.
- October 2026.

## Slide 2 — Presentation Outline
**Main message:** From industrial challenges to physics-based modeling, service resilience and sustainability.
1. Research Foundation — Background, industry motivation, research gap, objectives.
2. Engineering Investigation — Eight-component architecture, thermal dynamics, methodology.
3. Research Progress & Assessment — Evidence, service resilience, sustainability, remaining work.

## Slide 3 — Research Background & Industrial Motivation
**Main message:** Power distribution and EV charging share an electrical connection; common ambient heat does not itself establish thermal interdependency.
1. Power: transformer, feeder, equipment loading, loss and cooling conditions.
2. Transportation: DC charger, vehicle battery, charging capability/readiness.
3. Industry: utilities manage transformer loads and thermal margins; charging operators manage delivered power and service schedules.
*Source anchors:* Hilshey et al. (2013), DOI 10.1109/TSG.2012.2217385; Krama et al. (2026), DOI 10.1016/j.ecmx.2026.101960.

## Slide 4 — Research Problem, Gap & Objectives
**Main message:** Temperature-mediated cross-system interactions and their service consequences are not yet qualified for the selected integrated case.
- SO1: Identify/qualify thermally sensitive states and independently directional interdependencies.
- SO2: Model qualified mechanisms and state–time evolution under extreme heat.
- SO3: Quantify supported critical transitions, propagation delays and electricity/mobility service consequences.
**Governing frozen objective authority on main:** `project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md`; presentation points are compact summaries, **not substitutes for its verbatim text**. Researcher-approved V2 amendment is unmerged PR #76 as of this snapshot.

## Slide 5 — Physical System Architecture
**Main message:** Eight selected components; physical electrical transfer versus separate cooling/protection roles.
- P1 transformer; P2 feeder; P3 transformer protection/load-management hardware; P4 transformer cooling.
- T1 DC EV charger; T2 vehicle battery pack; T3 EVSE cooling; T4 vehicle HVAC.
- AC P1→P2→T1; DC T1→T2. Cooling/measurement/conditional control are not extra series energy stages.
**Evidence status:** Working equipment portfolio, not a validated installed topology or eight state ODEs.

## Slide 6 — Research Methodology
**Main message:** Physical laws + source/measurement qualification precede coupled-system claims.
1. Evidence qualification and physical/electrical/thermal metering.
2. Electrical network + minimum sufficient thermal-state modeling: `xdot=f(x,z,u,H;theta)`, `0=g(x,z,u,H;theta)`.
3. Independent T_e→P and P→T_e comparisons; uncertainty, service resilience and bounded sustainability when supported.
**Definitions:** `H(t)` external forcing; `z` algebraic electrical port quantities. No numerical model law/parameter admitted solely by graphic representation.

## Slide 7 — Work Completed & Preliminary Evidence
**Main message:** Research foundation and separate power-model evidence advanced; site-matched cross-sector validation OPEN.
1. Official title, objective/scope decisions and eight working components documented.
2. TU Wien 20Cable electrical benchmark reconstructed; any 50 kW charging scenario conditional, not actual Qatar grid field measurements.
3. Bærug independent 40 MVA measured transformer series: 8,592 hourly observations and reported held-out MAE 0.907 K. Qatar CPC50 50 kW charger field evidence supports charger thermal derating, not coupled I2/I3 verification.
*Provenance:* `project/research_checkpoints/2026-10-12/SCIENTIFIC_CHECKPOINT_V1.md` in PR #77; Krama et al. (2026). Original datasets and holdout code are required to reproduce numbers independently.

## Slide 8 — Service Resilience & Sustainability
**Main message:** Resilience = maintain/recover required electricity/mobility services; sustainability = environmental, economic and social consequences of disturbance and engineering responses.
1. Test `Q_P(t) >= Q_P,req(t)` and `Q_T(t) >= Q_T,req(t)`; deficit/recovery only with defined service demands and timelines.
2. Pathway 1: direct qualified thermal/service consequences in environmental/economic/social indicators.
3. Pathway 2: Improve/Adapt/Restore and changed service; compare separately across those same dimensions.
**Distinction:** resilience improvement does not imply sustainability improvement; no observed service deficit or indicator results claimed.

## Slide 9 — Remaining Work & Research Plan
**Main message:** Proposed schedule only (Oct 2026–Apr 2027).
1. Oct–Nov: actual equipment and source audit; pursue original synchronized charger temperature/cooling/AC P/Q and required service records.
2. Dec–Jan: develop/verify admitted coupled laws, compare independently directional hypotheses, quantify model uncertainty.
3. Feb–Apr: resilience service assessment, supported sustainability indicators, indicator-traceable SDG interpretation, documentation/writing.
**Stop conditions:** no public charger dataset, no installed P3 restriction evidence, no service thresholds, or no independent validation must remain explicit OPEN rather than be fabricated.

## Slide 10 — Thank You
**Main message:** Physical understanding, service-level resilience and sustainable engineering consequences.
- Physical mechanisms and admitted temperature-mediated interactions.
- Maintaining/recovering required electricity and mobility services.
- Environmental/economic/social trade-offs of engineering decisions.
**Questions and Discussion.** Dossiya Dakou, ASU MSE Sustainable Engineering.

---

## Release notes
- Deck: exact 10-slide editable Google Slides using user's supplied 2026 ASU theme; `Google Slides` is the presentation's live working file. A local 10-slide PPTX derivative exists independently.
- Figure contents: current native deck uses editable scientific text/shapes **without verified embedded real-world equipment photographic pixels**. Continue source-licensed image integration per Deck3 photography first-law when the image phase is executed.
- Cite every external scientific statement near the slide claim. Separately documented transformer and Qatar charger cases must **never** be passed off as one real-world installation.
- Do not silently promote numerical benchmark simulation to physical-field validation, candidate coupling to proven causality, or SDG thematic association to official measured indicators.
