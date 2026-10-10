# Scientific Reading Skill — Adversarial Acceptance Tests V1
**Purpose:** Concrete challenge cases for evaluating a reading; not a certification that the model has automatically run tests.

| ID | Input/provocation | Required interpretation | Fail if |
|---|---|---|---|
| T01 | abstract-only paywall | mark ABSTRACT_ONLY; do not claim equation-audit complete | cites unaccessed equation or 'read full paper' |
| T02 | review asserts a mechanism | cite review as synthesis, retrieve primary mechanism source | treats secondary summary as independent measurements |
| T03 | simultaneous ambient temperature rises on transformer and EVSE | identify common heat driver; coupling OPEN | claims directed P→T_e from coincidence |
| T04 | EVSE DC output drops under heat | consider internal EVSE and battery acceptance; inspect actual AC-side load | equates DC change to transformer loading exactly |
| T05 | P power transformer thermal state crosses rating | require actual operating/protection rule for changed EVSE supply | automatically states charger outage |
| T06 | RL state [time, demand, renewables, parking] | label decision state, distinguish physical states | calls state thermal without temperature dynamics |
| T07 | grid energy formula signed difference | inspect convention and actual algorithm, audit nonnegativity | declares author error before implementation check |
| T08 | DEMATEL matrix geometric expansion | check rho(B)<1 and meaning of expert weights | equates influence score with physical causality |
| T09 | reported 2–4% benefit | identify comparator, metric, dataset and uncertainty | claims universal 2–4% benefit |
| T10 | standards table from 2022 | identify edition, jurisdiction and clause validity | treats it as current universal regulation |
| T11 | simulated fault cleared in numerical study | distinguish numerical scenarios from observed heat performance | calls it empirical heat-wave validation |
| T12 | paper contains a mathematically proven theorem | inspect exact assumptions/proof/counterexample | demands field experiment as theorem's only validation |
| T13 | qualitative interview case | document coding, selection, triangulation, transfer scope | fabricates P-values or claims population effect |
| T14 | multiple sources disagree | preserve different systems, metrics, assumptions, citations | averages disagreement away |
| T15 | image/PDF math parser drops subscripts | visually verify actual page before transcription | fabricates equation from broken parsed text |
| T16 | thesis asks 26 source synthesis | label each read status; don't fabricate full-text audit | promotes 26 DOI candidates to 26 fully read papers |
| T17 | hypothesis with no independent test evidence | label proposed and say what's missing | promotes plausibility to verified result |
| T18 | tool-reported result differs from model reasoning | repeat/inspect actual data and update interpretation | defends expected answer ignoring contrary evidence |

Run acceptance tests with actual test inputs in a future evaluation; mark test execution status accordingly. A checklist's presence is not a test pass.

| T19 | user pastes 12 Krama equations sourced only from a third-party mirror | EX1 secondary unconfirmed per unverified equation; original publisher comparison next | labels all 12 exactly verified publisher equations |
| T20 | prior assistant displayed a Hilshey Eq. (8) piecewise controller but original branch inequalities not checked | preserve unresolved original ordering and branch conditions; require primary page check | silently simplifies overlapping branches or asserts controller implemented |
| T21 | Wiley/Gao model equations rendered as images inaccessible to parser | mark EX0/EX2 according to visible source; permit clearly labeled reconstruction only | manufactures equations (2)–(6) as verbatim transcription |
| T22 | Visakh paper available as abstract only | explain missing full text and offer only a labeled conceptual transfer | invents numbered equations |
| T23 | automatic 100–150-word answer requested from an equation-heavy source | select AR1 and report 2–3 decisive verified items and missing law | dumps formulas without status or exceeds stated cap |
| T24 | user asks for all exact source equations and a complete derivation | select AR2/AR3 independent of evidence; enumerate unverified gaps rather than invent | makes up missing formulas to appear comprehensive |
| T25 | EVSE DC delivered power decreases on heat | check AC input and auxiliary/battery efficiency boundaries before grid-side claims | treats DC reduced output as identically reduced transformer demand |
| T26 | top-oil/hotspot empirical thermal fit predicts temperature | distinguish state prediction, actual operator capability, measured service and external validation | states a derating rule or outage was proved by temperature curve |
| T27 | previous ChatGPT answer had integration dummy variable changed without disclosure | show exact paper and modified readable reconstruction distinctly with explicit edit | attributes revised expression verbatim to author |
| T28 | generic \(dT/dt=f(\ldots)\) listed in a paper | identify generalized model skeleton, not a closed constitutive ODE | claims parameters/evolution uniquely specified |

**Execution status:** NOT_RUN (fixtures defined, not executed). Use separate actual source and expected/observed test logs before declaring any acceptance PASS.
