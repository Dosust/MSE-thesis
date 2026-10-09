# Dossiya Expert — Thermal Interdependency Literature Audit and Handoff v1
**Date:** 2026-10-09  
**Status:** WORKING EVIDENCE AUDIT; NOT full-text synthesis; no novelty or model freeze  
**Scientific precedence:** frozen thermal scope, state/time definitions, system boundary, exact GO/SO1–SO3 and model-admission ledgers. Historical broad intervention/recovery research is not reinstated.

## 1. What was completed
1. Retrieved two distinct existing GitHub sets of 26 DOI records each (initial seed and verified-screen priority list). **47 distinct DOI keys across both**; five DOI keys overlap (metadata capitalization and normalization still requires manual checks). Existing 687→404→433→200→26 screening history preserved untouched.
2. Produced `PROVISIONAL_26_CORE.csv` with 26 unique DOI candidates chosen for the current thermal-only scope, not ranked by publication quality. DOI/title metadata predominantly transcribed from historical repository records; **not independently confirmed for every row**. Some lower-priority transfer studies were retained only to fill transparent provisional slots; they should be substituted if stronger directly relevant empirical or mechanistic papers pass full-text review.
3. Checked public external source material for the five nearest initial comparator papers; available level varied. **Hilshey full author-hosted 9-page paper retrieved and inspected at article/introduction level**, while Visakh, Krama, Ji, and Wang are checked against publisher abstracts/metadata, *not fully reconstructed*. The record below distinguishes this from completed full-text review.
4. No canonical title/scope/objective, module admission, parameter, state vector, thermal threshold, research questions, or claimed novelty was frozen or modified.

## 2. Five comparator evidence and limits (source-aware)

| DOI | Available evidence checked | Already studied / demonstrated | What remains open for thesis | Level |
|---|---|---|---|---|
| `10.1109/TSG.2012.2217385` Hilshey et al. (2013) | Author-hosted IEEE article PDF `https://phines.w3.uvm.edu/publications/2013/hilshey_2013.pdf` | EV travel-derived charging schedules, IEEE dynamic transformer temperature, ambient forcing, smart-charge thermal aging; reports sensitivity to charging timing | Does not on its own establish the exact charger-temperature→grid AC-power→transformer or transformer capability→fleet deadline path | SOURCE FULL TEXT ACCESSIBLE; PARTIAL EXTRACTION |
| `10.1016/j.segan.2023.101096` Visakh & Selvan (2023) | Elsevier publisher page `https://www.sciencedirect.com/science/article/pii/S2352467723001042` | Addresses EV-induced distribution transformer overload/heat and immediate service-disruption mitigation | Extract exact state-to-capability/protection rule and operational definition; no assumptions about automatic thermal curtailment | PUBLISHER ABSTRACT |
| `10.1016/j.ecmx.2026.101960` Krama et al. (2026) | Elsevier publisher OA abstract `https://www.sciencedirect.com/science/article/pii/S2590174526004435` | Field experiment: air-cooled DC fast-charger derating in Qatar under extreme ambient temperatures; temperature-sensitive offered power | Full EVSE temperature and AC input/load accounting, device transferability, thermal controls and mobility deadline outcome | PUBLISHER ABSTRACT; OA FULL TEXT NEEDS EXTRACTION |
| `10.1016/j.apenergy.2025.126806` Ji et al. (2025) | Elsevier publisher abstract `https://www.sciencedirect.com/science/article/pii/S0306261925015363` | Tri-level P–T/FCS scheduling; temperature in EV routing model; charging queues and ACOPF | Determine whether transformer/EVSE evolving thermal states and matched service-event timing already modeled; cannot assert absent from abstract alone | PUBLISHER ABSTRACT |
| `10.1016/j.ress.2025.112005` Wang et al. (2026) | Elsevier publisher abstract `https://www.sciencedirect.com/science/article/pii/S0951832025012049` | Charging/V2G preferences affect dynamic P–T interdependency under earthquakes | Identify whether thermal constitutive equations included; abstract does not authorize a negative absence claim | PUBLISHER ABSTRACT |

**Do not cite the five rows as fully verified equation-level full-text analyses.** In particular, the Hilshey study already has temperature-dependent control and tracking of charging opportunities: never claim no one has modeled transformer temperatures with vehicle schedules, or that charging deadlines are novel by themselves.

## 3. Correct research gap statement (provisional)

*Research problem:* Physical connectivity and shared heat do not establish a directional thermal interdependency. For a specified P–T_e thermal interface, determine admissible heat-conditioned source→receiver effects, their activation/timing, and electricity/mobility service significance.

*Knowledge-gap candidate, not demonstrated novelty:* Whether the closest integrated studies already provide a sufficiently supported and validated representation connecting transformer thermal state, applicable operating capability/curtailment law, EVSE thermal limit, AC input charging power, vehicle energy delivery and **declared mobility service** under extreme-heat forcing.

*Potential value:* Test whether physics-qualified state-time coupling materially changes prespecified service or transition conclusions relative to a matched simpler baseline. Different numerical curves are not proof of superiority.

## 4. Mandatory directional mechanism ledger

| ID | Path | Mechanism | Gate | Current assessment |
|---|---|---|---|---|
| H | extreme heat → P and T_e separately | common environmental forcing | External forcing not interdependency; ambient ≠ internal system state | CONCEPT ADMITTED |
| TP1 | T_e → P | charging load at **AC grid boundary** alters transformer loading and thermal evolution | AC/DC boundary and efficiency, transformer thermal law, measurable charging-demand response | PHYSICALLY SUPPORTED FAMILY; selected case OPEN |
| PT1 | P → T_e | transformer temperature/state-dependent **actual operating capability/policy** limits facility AC power then delivered vehicle energy | compatible transformer technology, standard/operating law, charger limits, service deadline | CANDIDATE, CRITICAL GATE OPEN |
| TE1 | within T_e | EVSE internal heat derates offered charging power | EVSE device data, derating curve and charger AC-input response | COMPONENT THERMAL RESPONSE; not itself P→T_e |
| S1 | energy delivery → mobility | battery energy at departure meets declared functional requirement | fleet schedule, required energy, readiness vs actual mobility distinction | SERVICE TRANSLATION CANDIDATE |

Bidirectional arrows must not be drawn as established if PT1 is open. Do not invent reverse direction or label thermal correlation as propagation. Delays require controlled directional source event and receiver response, not arbitrary thermal-curve time difference.

## 5. Mathematical architecture — *not frozen*

Conditional conceptual representation:
```math
\dot X=F(X,Z,H,u;\theta),\quad 0=G(X,Z,H,u;\theta),\quad Q=\mathcal S(X,Z,u).
```
ODE/DAE status awaits actual admitted state dynamics and algebraic boundaries; candidate transformer top-oil/hot-spot, EVSE temperature and SOC are not frozen. SOC is energy state; heat is forcing. Need transformer architecture, IEC/IEEE standard clause-level admissibility, state-to-capability law, reproducible numeric verification, feasible parameter identification and independent validation.

Charging AC input, DC offered power and battery terminal energy **must not be put in a single minimum-power equation without efficiency and unit-consistent conversion**.

## 6. What remains (gates by sequence)

G0. Verify bibliographic metadata / retraction corrections and author/title/DOI for every candidate (DOI matching alone inadequate).

G1. Screen all 47 union items + targeted added research for exact current thermal-only question; document keep/exclude reasons. Provisional core is **exactly 26 unique DOI items**, but no final freeze and no full-text completion.

G2. Replace weak generic transfer / flood / restoration / market-control slots with indispensable missing primary physics, transformer thermal limit operating policy, EVSE data, valid AC grid constraint, fleet deadlines, state identifiability/VVUQ. Formal standards maintained in separate normative register, not counted as journal papers.

G3. Acquire accessible full texts legally; record full text availability; perform page/equation/location extraction. Distinguish model structure, measured parameters, calibration and validation.

G4. For each retained paper create `source_metadata, boundary, governing_laws, state, time, heat_forcing, input_AC, thermal_mechanism, direction, state_to_capability, service, equations/provenance, verification, empirical_validation, uncertainty, actual_findings, author_limits, reviewer_inferences, novelty_overlap`.

G5. Explicitly review **closest prior art** paper-by-paper, including what is already integrated, not merely missing keywords. Finish standards plus module model admission audit.

G6. Set the source/receiver event and timing definitions, baseline M0/M1/M2 controlled physical differences, outcome and uncertainty measures **before experiments**. Freeze only through explicit scientific decision protocol.

G7. Populate Deck3 Slide 6 with verified source-by-claim evidence (not a decorative claim of missing literature), and Slides 5/7/9/10 with accepted directionality, RQs, system subset and prospective test details.

## 7. Together: minimum needed decisions and evidence

The user/supervisor should provide or approve (1) access to locked full texts via ASU/NUS institutional libraries, particularly closest comparators; (2) a credible specific transformer/charger topology and technical specifications or permission to use a traceable standard synthetic case; (3) defined vehicle fleet/departure/mobility service requirements; (4) whether measured transformer and AC EVSE input data exist; (5) acceptance of the candidate demonstrator and final RQ wording **after** novelty and data-gate review.

Do not request all at once: tackle institutional full-text access first, then feasibility choice after evidence review.

## 8. Release verdict

**COMPLETED:** preliminary GitHub corpus reconciliation, a 26-item provisional register, five closest-article *source-level* comparison, mechanism gate register, and sequenced handoff.

**INCOMPLETE/BLOCKED:** 26 full-text reconstructions, full metadata validation, exact originality evidence, operating-rule admission, parameter calibration, empirical validation, final model/claim freeze, final Deck3 cited slides.

No generated presentation is certified. No claim about GitHub Actions is made.
