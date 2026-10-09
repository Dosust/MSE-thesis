# Dossiya Expert v1.3 — Five-Paper Independent Reading and Interpretation Audit
**Date:** 2026-10-09 | **Role:** adversarial self-assessment, not external expert certification
**Access:** All five user-uploaded complete PDF files were accessible locally; locally extracted text and inspected displayed page images. FULL_TEXT_AVAILABLE does **not** mean every equation/page was manually checked: inspection depth below is **FOCUSED_AUDIT**. For claims not audited in depth, status OPEN.
**Source types:** Reviews, design/simulation, RL/optimization, educational integrative review, framework/DEMATEL. Original published reports are not automatically independently replicated.

## A1: Oladigbolu et al. (2025), Journal of Energy Storage 135, 118419
DOI: https://doi.org/10.1016/j.est.2025.118419. PDF 38 pages. Type: narrative/critical technical review.
**[S]** PDF pp.1–2 abstract and §§1.1–1.2: surveys coupled power-transport networks, EV/DER/mobile energy-resource operations and resilience. PDF p.4 Table 1 classifies resilience-planning methods, contribution and limitations; PDF p.6 §§2.6–2.7 discuss tractability, fidelity, observability and uncertainties.
**[R]** Review connects EV travel/charge decisions, location/time of electricity loads and electrical operations; topology and operational relationships are not automatically experimentally established thermal cause.
**[I]** Charging AC load may affect power equipment thermal response through loss and energy accumulation; this draws on independent physics, not the review's validated transformer-case data.
**[H]/rivals:** Concurrent heat forcing can raise both transformer and charger temperature. A feedback connection in a systems diagram is not proof of a temperature-operated supply constraint.
**[V]** Source type/sections/table verified against uploaded PDF. No independently rerun primary experiment.
**Human check:** Trace cited primary studies; align actual AC feeder current, load, ambient forcing, transformer thermal observations, charger protection logs. **Thesis transfer:** literature navigation and context only; directional thermal mechanism remains OPEN.

## A2: Tamay & Inga (2022), Sustainability 14, 8248
DOI: https://doi.org/10.3390/su14148248. PDF 21 pages. Type: EVSE design / bibliometric synthesis / electrical simulation.
**[S]** PDF p.1 abstract reports DIgSILENT PowerFactory analyses of active/reactive power, voltage, current and phase/ground/three-phase short circuits; simulations conditional on fault clearing. PDF p.9 Table 4 contains charging ratings; PDF p.10 describes 2020-code installation/protection conditions.
**[R]** The model evaluates an electrical fault/protection context; not a thermal derating experiment.
**[I]** Need distinguish feeder-side AC flow, charger-side conversion, battery acceptance and fleet deadline outcomes. Conditional accounting: P_AC = P_DC + P_losses including auxiliaries for precisely matched boundary.
**[H]/rivals:** Fault cleared ≠ thermal resilience during heat wave; nominal rating ≠ actual heat-conditioned capability.
**[V]** Mathematical boundary distinction verified conceptually, not a replication of PowerFactory runs. Jurisdiction and latest standards edition remain UNCHECKED, hence no contemporary legal compliance conclusion.
**Human check:** single-line drawing, transformer and EVSE model, installation code edition, protection/settings, manufacturer thermal data. **Thesis transfer:** architecture and electrical boundary; not thermal coupling law.

## A3: Li, Dai, Goldrick, Kotter, Aslam & Ali (2024), Energies 17, 5442
DOI: https://doi.org/10.3390/en17215442. PDF 21 pages. Type: data-supported RL/optimization simulation.
**[S]** PDF p.1 abstract reports PPO charging policy evaluated using Leicester fleet case information and 2–4% renewable-energy utilization improvement over paper's specified random and priority charging comparators. PDF p.5 eqs.(1–2) define decision state and 15-minute charging energy updates. PDF p.6 eqs.(3–5) express reward and grid-energy terms; PDF p.8–9 Gaussian-weather modeling.
**[R]** Decision state [required energy, renewable generation, time, parking time] is not necessarily a physically sufficient thermodynamic state. 15 min = 0.25 h: 20 kW charging for one interval corresponds to 5 kWh, valid when using kW and hours.
**[V]** Independently computed 10 kWh renewables minus 20 kWh charge demand => −10 kWh under paper's written subtraction; conventional nonnegative grid import is +10 kWh in that simple case. This flags a variable-definition/sign issue requiring implementation check, **not proof of author software error**.
**[I]** RL choices constrain EV/fleet performance, but do not independently establish transformer thermal dynamics.
**[H]/rivals:** Relative RL gain may depend on baselines, generated scenarios, constraints, distributions and reward weights; reported 2–4% not universal.
**Human check:** obtain code, reimplement reward sign and grid export/import convention, align time-unit conversion, rerun seeds and holdout unseen fleet/weather periods; audit extreme-temperature distribution tails. **Thesis transfer:** scheduling/deadlines can define service and controls only if genuinely needed; no qualified P→T_e law.

## A4: Shin et al. (2022), Instructional Science 50, 933–960
DOI: https://doi.org/10.1007/s11251-022-09590-9. PDF 28 pages. Type: integrative educational review/framework.
**[S]** PDF p.5 Fig.1 and modeling-practice paragraph identify M1 characterize problem, M2 define boundary, M3 design/construct model, M4 test/evaluate/debug, M5 use for explanation/prediction/design. PDF p.6 articulates iterative connections between systems and computational thinking; PDF pp.6–7 disclose literature-search method and 80→55 screening.
**[R]** Scientific model building benefits from explicit boundaries, causal reasoning, time, and iterative computational checking.
**[I]** Paper can guide an interpretation workflow for engineering sources; the paper did **not** validate equipment-specific physical thermal transfer laws.
**[H]/rivals:** Classroom modeling pedagogy is not experimental evidence that a particular causal inference has been identified in a transformer/charger.
**[V]** Five modeling practices, Figure 1 and source classification verified against PDF; no independent educational effectiveness replication.
**Human check:** inspect coded literature synthesis and pedagogical transfer assumptions, test learning workflow on independent engineers and evaluate review consistency. **Thesis transfer:** methodology of thinking and auditing, not parameter values.

## A5: Ayoobi, Inceoğlu & Inceoğlu (2024), Smart Construction and Sustainable Cities 2, 18
DOI: https://doi.org/10.1007/s44268-024-00042-6. PDF 24 pages. Type: SLR/framework + expert-DEMATEL influence analysis.
**[S]** PDF p.4 Fig.1 screens building/vernacular records and routes indicator selection to DEMATEL; PDF p.5 eqs.(1–3) uses expert influence matrix and total influence expansion T=B+B²+…=B(I−B)⁻¹. PDF p.6 eqs.(4–5) derives row/column influence values.
**[R]** B^k represents length-k paths in an expert-scored influence graph under ordinary matrix multiplication, not an observed physical transfer coefficient.
**[V]** Independent matrix test with B=[[0,0.2],[0.3,0]] has rho≈0.24495 and B(I−B)⁻¹ matches 40-term sum to floating-point precision. For B=diag(1.2,0.2), I−B is invertible, yet 40-term first sum ≈8812.63 vs algebraic matrix expression −6; the infinite series diverges. Therefore rho(B)<1 (or equivalent convergence demonstration) is essential to that equality. These are **constructed test matrices**, not authors' expert weights.
**[I]** Model can organize assessed influence between design indicators, but does not empirically establish physical causation or a heat-flow law.
**[H]/rivals:** Expert selection, scale, normalized score sensitivity and unmeasured confounders may change apparent prominence; calling diagram 'cause-and-effect' exceeds what scoring alone independently proves.
**Human check:** retrieve original expert matrices, independently normalize, verify spectral radius, reviewer agreement, uncertainty and robustness to scale/threshold. **Thesis transfer:** procedural evidence synthesis only; DEMATEL does not substitute actual thermodynamics.

## B — Equation/mechanism audit crosswalk
| ID | Source+locator | Reconstruction/test | Status |
|---|---|---|---|
| M01 | Li PDF p.5 eq.(2) | 0.25 h × charging kW gives kWh for 15 min; example 20 kW gives 5 kWh | CHECKED DIMENSION |
| M02 | Li PDF p.6 eq.(4) | renewable−demand may be negative for positive grid import; toy 10−20=−10 vs import +10; code/sign unknown | FLAGGED, NOT 'AUTHORS WRONG' |
| M03 | Li PDF p.9 weather Gaussian assumption | distribution family does not guarantee extreme-tail realism | INFERRED LIMITATION |
| M04 | Ayoobi PDF p.5 eq.(3) | convergent 2×2 example tested; divergent invertible counterexample tested | CHECKED MATHEMATICAL CONDITION |
| M05 | Tamay PDF p.1 electrical fault simulations | a simulated cleared fault does not validate heatwave dynamics | INFERENCE BOUNDARY |
| M06 | Oladigbolu review PDF pp.1–2 | charging load links network operations, not evidence of specific transformer thermal protection | REVIEW-ONLY |
| M07 | Shin PDF p.5 Figure 1 | modeling iterations and boundary-setting; not a physical transfer equation | METHODS-ONLY |

## D — Cross-paper synthesis
The papers cover five distinct epistemic roles: system-level narrative review; engineering electrical design/fault simulation; RL decision optimization; education-framework modeling practice; expert-indicator sustainability integration. Together they support a **multi-method reading workflow** but not a shared experimentally verified unification theory. Distinguish physical model, decision state, expert judgment, observed outcomes and explanatory framework. Incompatibilities include units, physical boundaries, causal identification and evidence depth.

## E — Human reviewer verification plan
1. Independently inspect source page and rendered equation/figure.
2. Translate into observable variables with units, boundaries and timestamps.
3. Recreate calculations with source inputs, not arbitrary examples; label toy tests as toy tests.
4. Identify competing causes and design measurement/control that discriminates.
5. Decide what claim transfers to real Power–Electrified Transportation device, using case-specific specs; mark unobservable directions OPEN.
6. Challenge an interpretation with contrary data; revise ledger rather than conceal uncertainty.
**Full-text audit status:** NOT fully completed for all pages/equations; these are targeted source-grounded inspections. 
