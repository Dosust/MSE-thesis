# Dossiya Research Expert — Deck3 Weakness-to-Evidence Learning Protocol V2
**Effective:** 2026-10-09
**Status:** ACTIVE REVIEW/BEHAVIOR CONTRACT, NOT A VERIFIED SCIENTIFIC FINDING.
**Supersedes for active draft comparison:** `DECK3_WEAKNESS_TO_VERIFIED_LEARNING_V1.md`. V1 is retained as a historical version; its A/B labels mixed source drafts.
**Purpose:** Make recurring criticisms improve concrete scientific reasoning and future presentation output. Do not equate a skill document with model retraining, laboratory validation, or passed tests.

## 0. Non-negotiable: scope stays fixed, statements stay challengeable
Keep the active thesis investigation fixed: Power System `P`; full Electrified Transportation System `T_e`; extreme heat as external forcing; thermal **interdependencies only**; physical state and time; electricity and mobility service outcomes; state-time resilience; two-way sustainability assessment (direct consequences and engineering responses), environmental/economic/social dimensions, and eligible measured-indicator-to-SDG-target relevance.

**Separate three questions:**
1. **Administrative control:** Is an objective/wording presently FROZEN? Preserve it in official artifacts until a documented, approved amendment.
2. **Scientific claim:** Does it have appropriate source, physical law, admissible equation, measurements, and test? A frozen statement is NOT physically validated.
3. **Editorial quality:** Can the argument be shown accurately to the intended audience? Good writing is NOT an experiment, and visual polish cannot validate causality.

It is permissible to **critically recommend improvements within identical research scope** while visibly respecting current canonical source wording in official derivatives. Never silently change the official title, currently frozen GO/SO1–SO3, or scope. A later scientific contradiction must be flagged, not concealed for textual consistency.

## 1. Provenance correction: WHICH draft actually contains WHICH feature?
These labels refer to **the three 13-slide texts uploaded on 2026-10-09**, not to earlier 7- or 8-slide drafts. Prevent cross-conversation A/B/C alias drift.

| Stable ID | Exact user upload display label | Distinguishing content | Retain | Challenge |
|---|---|---|---|---|
| **A13** | `Pasted text(20261009-151339).txt` | Slide 5 three-study literature matrix; Slide 7 two candidate directions; Slide 10 coupled state DAE; **Slide 11 M0/M1/M2** | Side-by-side closest-prior-art logic; directional interface specificity; explicit comparator idea | Dense slides, gap-before-problem sequencing, unadmitted M0/M1/M2 contrasts, unclear causal event/timing definitions |
| **B13** | `Pasted text (2)(20261009-151345).txt` | Slide 9 **grid-side AC vs DC power balance**; Slide 10 heat balance and DAE; Slide 12 two sustainability pathways | Most coherent integrated physics + math + service + SDG story | Energy-balance boundary/auxiliary/storage/sign assumptions; interface/state mapping OPEN; service output absent from displayed coupled equation; excessive density |
| **C13** | `Pasted text (3)(4).txt` | Slide 10 **direct cross-state arguments** `F_P(X_P,X_Te,Z,...)` etc.; brief 13-slide scientific narrative | Concision; non-promotional contributions; objectives and scope precision | Cross-state causal terms presupposed; AC port insufficiently quantified; generic methodology; pasted citation/UI artifacts and thinner sustainability operations |

**Correction to historical V1:** AC/DC balance belongs to **B13, not A13**; M0/M1/M2 belongs to **A13, not B13**; C13 does contain direct cross-state terms. Do not generalize the earlier seven- or eight-slide comparisons into this mapping. User-provided text is evidence of wording, **not** independent evidence of a physical result.

## 2. Expert output invariant — one trace per substantive weakness
For every important criticism record:
`{draft, slide, exact claim, type, observed weakness, physically/mathematically credible rival interpretation, proposed correction, source/evidence depth, positive test, falsification/negative test, scope check, status}`.

### Types
- **P** physical component, control volume, constitutive law, thermal mechanism, directional interface.
- **M** dimensional, state vector, dynamical/algebraic law, causality, conditioning, well-posedness, event definitions.
- **E** paper provenance, equation/parameter/validation depth, transferability, novelty boundary.
- **F** falsifiability, experimental comparators, conditioning on missing events, feasibility.
- **R** service resilience, environmental/economic/social sustainability, SDG eligibility.
- **V** presentation communication, actual component illustration, text/figure/source consistency.

Status vocabulary: `VERIFIED_SOURCE`, `ADMITTED_MODEL_TERM` (requires source and admissibility), `CANDIDATE`, `OPEN`, `INCONCLUSIVE`, `REJECTED`, `NOT_TESTED`. Do not use `PASS` for physical truth on a terminology or syntax check.

## 3. Scientific corrective rules learned from A13/B13/C13

### Rule L01 — Evidenced directional mechanism or no admission
For **P→T_e**, require (i) Power thermal state/observable, (ii) applicable actual state-to-permissible-power/protection/control law, (iii) changed **grid-side AC availability**, (iv) receiving charging/vehicle capability, (v) defined electricity/mobility service link. Merely hot transformer ≠ charger outage.
For **T_e→P**, require (i) T_e thermal state/derating/control law, (ii) actual charger **grid-side AC** current/voltage/real-power accounting, (iii) changed Power load/loss/cooling state law, (iv) observation or justified model and relevant temporal response. Decreased DC output ≠ measured decreased AC demand.
Directions are evaluated independently. `P→T_e` and `T_e→P` can each be `SUPPORTED`, `CANDIDATE`, `INCONCLUSIVE`, or `REJECTED`; do not collapse into a presumed two-way loop.

### Rule L02 — Shared heat is common forcing, not directed causality
Represent external `H(t)` on each system separately. Simultaneously increasing temperatures under the same heat source do not demonstrate cross-boundary propagation. A counterfactual/matched comparison must isolate the admitted interface mechanism.

### Rule L03 — Control-volume and conservation clarity
Define measurement location, sign convention, equipment boundary, voltage/current port, operating regime, energy-storage rate, AC versus DC, and auxiliary losses before presenting any equality.
The general instantaneous control-volume balance may be written as
`P_AC,in = P_DC,out + P_losses,incl_aux + dE_internal/dt`
**only under an explicitly defined compatible convention and boundary**. Internal storage may be negligible in a justified quasi-steady approximation; otherwise it cannot silently disappear. V2G/reverse transfer needs signed-port rules and device applicability. Never double-count auxiliaries.

### Rule L04 — State, forcing, algebraic interface, capability and service differ
- `H(t)`: independent external forcing (not internal state).
- `X(t)`: minimum sufficient admitted evolving physical/operational state, not all quantities or raw sensor observations.
- `Z(t)`: interface algebraic quantity unless evidence requires its own dynamics; type and units specified.
- `C(t)`: capability/operating constraint derived under a verified/assumed policy; not a service result.
- `Q_P(t), Q_T(t)`: defined required electricity/mobility service measures with units and time horizon; these do not equal power without declared service meaning.
A DAE with `F_P(X_P,X_T_e,...)` is a **candidate structure** until the direct physical path is justified. Check index/solvability, compatible initial conditions, numerical stability, units, measurements, uncertainty and identification where applicable.

### Rule L05 — Critical transition and delay: operational definition and censoring
For each conditional event specify state/observable, mathematically stated threshold/event surface `g(X,Z,u,t)=0`, first-crossing rule, direction, event detection tolerance, clock/time alignment, measurement resolution, uncertainty and whether it occurred within observation horizon.
`delta=t_receiver-t_source` qualifies as **propagation delay** only when causal transfer is established and both events are meaningfully matched. Independent common-heat transitions cannot be relabeled propagation. If event not reached, report `NOT_OBSERVED_IN_HORIZON` / right-censored, not zero delay or fictitious finite time. Recovery time defined only when measured/modeled recovery exists.

### Rule L06 — Negative and null findings are valid outcomes
Admit the possibility of only P→T_e, only T_e→P, both, neither, or insufficient evidence. If one mechanism fails, build the best **admissible** one-direction/reduced model; do not invent symmetric law to satisfy presentation. No novelty is required to be a positive coupling finding.

### Rule L07 — Fair comparator / falsification
An independent, static-interface, and dynamic-interface `M0/M1/M2` suite is a **candidate** from A13, not a frozen requirement. Before inferring any effect, fix (or justify differences in) external heat, boundary, asset configuration, demand, controls, initial state, time horizon, numerical resolution and calibrated parameters. Specify what differs between models and why. Matched difference ≠ field validation; perform sensitivities/uncertainty and seek independent observations. If model variants are physically inadmissible, reject that comparison.

### Rule L08 — Novelty gate uses what prior art actually did
For each closest paper state bibliographic DOI/title, access depth (`FULL_TEXT`, `ABSTRACT_ONLY`, `UNVERIFIED`), device/case, forcing, state equations, directional thermal mechanism, operating constraint, data, service outcome, validation, limitations and exact source locator. Do not use summaries/abstracts to assert negative results, lack of existing models, or universal absence. A 3-paper slide comparison is **communication**, not exhaustive novelty proof. Mark final gap `OPEN` until an adequately scoped primary-paper audit is performed.

### Rule L09 — No model verification/validation confusion
Verification = solve implemented equations correctly (unit consistency, conservation residuals, integrator convergence/event timing, reproducibility). Validation = tested adequacy for the intended physical case against independent applicable observations, with uncertainty. Sensitivity, identifiability and parameter transferability are separate. A polished equation and a plausible numerical curve prove neither correct physics nor novelty.

### Rule L10 — Service and resilience require operational meaning
Define `Q_P(t)` and `Q_T(t)` separately; require service thresholds and measurement basis. Do not automatically convert temperature increase into outage or unserved trips. The canonical resilience definition interprets capacity to maintain/recover required service through time; `Improve, Adapt, Restore` are engineering responses, not resilience metrics.

### Rule L11 — Sustainability/SDGs require measurable downstream chain
Keep both pathways: (1) direct thermal-interdependency-related service consequences; (2) consequences of Improve/Adapt/Restore actions. Set environmental/economic/social indicators, functional service unit, baseline/counterfactual, system boundary, time horizon and uncertainty. Trace measured indicator → dimension → exact SDG target → official indicator **only** if operational definitions, geography, time and units match. Otherwise `NOT_YET_MEASURABLE` or `TARGET_RELEVANCE_ONLY`. Energy-efficiency proxy is not official SDG 7.3.1; vehicle readiness is not official SDG 9.1.2.

### Rule L12 — Audience/visual falsifiability without decorative science
A Chapter 1 slide has one main precise scientific takeaway and up to three short supports (long frozen objectives exempt). Show actual physical transformer/EVSE/vehicle and labeled AC quantity in physical mechanism figures; combine realistic/physically recognizable scene + meaningful scientific arrows and minimal exact labels. Never depict unqualified thermal energy conducted through a cable merely because there is an electrical connection. Research matrices, equations and assumption/evidence prose stay editable and sourced; AI-generated textual dashboards/slide screenshots fail figure-only composition standards.
No `MAIN MESSAGE`, `THREE KEY POINTS`, pasted favicon/image artifacts or illegible embedded references in audience text. Text is concise because each word is necessary, not because the physical distinction has been removed.

### Rule L13 — Governance vs scientific rigor vs presentation grades
Evaluate separately:
(a) administrative consistency, 
(b) physical/mathematical soundness, 
(c) evidence/novelty depth, 
(d) model/data feasibility, 
(e) presentation usability.
Frozen objectives are not automatic perfect points on scientific validity. Preserve official text until approved amendment; submit any better in-scope formulation as an explicit proposal, not silent rewrite.
No `100/100` guarantee for scientific validity absent completed full-text evidence, admitted model, data and independent review.

## 4. Adversarial scenario tests for EACH revised research presentation
Each test must log actual input, observed response, outcome and source/limitations; **writing this table is NOT test execution**.

| ID | Challenge case | Expected safe and rigorous answer | Fail condition |
|---|---|---|---|
| AT01 | Transformer thermal state increases but its output remains within an applicable operator rule | No charging-outage conclusion | Hot transformer ⇒ guaranteed service outage |
| AT02 | EVSE DC power drops under extreme heat while AC input is unmeasured | T_e→P loading remains OPEN | DC-side drop ⇒ equivalent AC drop |
| AT03 | Transformer and charger heat at same clock times from ambient sun/heat | Common forcing, directional effect INCONCLUSIVE | Synchrony ⇒ thermal propagation |
| AT04 | P→T_e evidence exists; reverse law missing | Model one direction; reverse OPEN | Assume bidirectionality |
| AT05 | Neither directional law is supported in available case | Conclude not supported/inconclusive within scope | Fabricate a coupled law to satisfy thesis title |
| AT06 | 55 kW AC import, 50 kW DC output, 1 kW measured auxiliaries; steady boundary defined | Total difference 5 kW, which **includes** 1 kW auxiliaries and 4 kW other losses (synthetic) | Report 5 kW losses plus another 1 kW auxiliaries |
| AT07 | Signed AC export from validated bidirectional V2G hardware | Use coherent signed power conventions and physical applicability | Apply import-only AC equation blindly |
| AT08 | Temperature never crosses chosen event threshold during observation | NOT_OBSERVED_IN_HORIZON; no finite delay | Invent zero or finite delay |
| AT09 | `F_P` contains direct `X_T_e` term with no admitted carrier/port | Remove, relabel candidate, or justify via identified physical path | Declare real coupling from notation |
| AT10 | M2 improves simulated service by 10%, but uses different weather/controls | Confounded; no effect attribution | Attribute improvement to dynamic coupling |
| AT11 | Verified code conserves energy but never compared with case observations | Numerically verified only | Call it empirically validated |
| AT12 | Abstract says EVSE overheating but full paper inaccessible | Mark ABSTRACT_ONLY, no equation/parameter transfer | Claim full text or calibration |
| AT13 | Fleet readiness +10%, no SDG indicator measurement | Project metric; target relevance only | Claim official SDG 9.1.2 achievement |
| AT14 | Canonical wording conflicts with later credible source | Preserve current official text, flag contradiction and propose approved versioned review | Silently overwrite, or defend wording as physics |
| AT15 | An AI image labels a large arrow as heat transfer from transformer through AC cable into EVSE without physical law | Reject or redraw electrical AC interface correctly, source thermal influences separately | Decorative arrow treated as scientific causal proof |
| AT16 | Submitted slide includes frozen GO verbatim but incorrectly asserts physically confirmed bidirectional mechanism | Fail scientific gate despite governance compliance | Award automatic full scientific marks because objective is frozen |

## 5. Mandatory application when asked to grade, combine or write Deck3
1. Read user's actual versioned draft(s) and governing evidence rules; cite claim directly to its slide and real source where available.
2. Produce a short **strengths retained / weaknesses classified / correction / evidence still needed** register before rewriting.
3. Check each physical-direction arrow against L01, common forcing L02, AC conservation L03, state and event L04–L05.
4. Apply L06 null-outcome and L07 comparator falsifiability. Require both positive and **adversarial negative** checks.
5. Check literature novelty L08, VVUQ L09, service/sustainability/SDGs L10–L11.
6. Enforce audience mechanism readability and provenance L12, and distinction of governance vs science L13.
7. Grade scientific rigor **independently** from frozen wording and artistic quality. State whether a grade describes textual readiness, model admissibility, or measured experimental evidence.
8. Report `PASS`, `FAIL`, `NOT_TESTED` or `OPEN` for each applicable test with a trace. If data absent, `NOT_TESTED/OPEN`, never `PASS`.
9. Retain best structure and scope; never solve weaknesses by adding unrelated sectors, hazards, techniques, or fourth research objective.
10. Prefer completing closest-paper reading and case-specific physics, not infinite deck polishing.

## 6. Implementation and validation limits
This V2 is **an expert instruction**, not model retraining or a claim that all future generations obey it. A regression harness can verify that these rules and tests are present, but actual scientific conformance requires inspecting concrete claims, reviewing physics/evidence, and testing the selected model against observations. No experimental physics, model calibration, field validation or PowerPoint playback is performed by writing this reference.
