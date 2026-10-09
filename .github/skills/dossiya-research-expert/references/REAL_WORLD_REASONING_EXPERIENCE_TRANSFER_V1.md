# Real-World Reasoning and Evidence-to-Skill Transfer V1
**Effective:** 2026-10-09 | **Owner:** Dossiya Research Expert | **Status:** active skill protocol, not empirical validation, retraining, or actual field experience.
**Goal:** Turn paper-level knowledge, physical laws, engineering case investigations, past critique, and computational tests into reusable *demonstrated research competencies*, not broad summaries or unearned claims of expertise.

## A. Fixed scope and adaptable truth
Remain within Power (P) and complete Electrified Transportation (T_e), thermal interdependencies under extreme heat, physical state and time, electricity/mobility service resilience, separately tracked direct and engineering-response sustainability, and cautiously eligible SDG target links. Approved/frozen objectives are research governance; candidate physical mechanisms, governing equations, active states, equipment configurations, assumptions and hypotheses remain open to evidence-based correction. Do not use hypothetical equipment as measured field experience.

## B. What counts as knowledge, skill, experience?
- **Knowledge**: A proposition with source type, exact citation/page/equation, applicable equipment, assumptions, units and reliability. Be able to reproduce the source's own meaning and distinguish derived inference.
- **Skill**: A *reproducible performance* with inputs, operations, outputs, successful positive AND adversarial tests, known failure modes and applicability limits. Merely describing a method is not mastery.
- **Experience evidence**: Explicitly labeled source-observed field case, measured laboratory result, executed numerical exercise, synthetic scenario, or historical case with a traceable artifact. No fabricated firsthand fieldwork or invented test run.
- **Transfer**: A skill learned on one transformer/EVSE/vehicle case carries to another ONLY after checking equipment class, topology, ratings, environmental boundary, controller rules, measurement comparability, parameter identifiability and service definition.

## C. Mandatory real-world scientific reasoning loop
1. **Situation**: What actual engineering equipment, stakeholder decision, physical service and heat condition? Specify spatial/time boundary; if unknown say OPEN.
2. **Observation**: What is directly measured/reported versus modeled/inferred? Record sensor, sampling, units and uncertainty where reported; distinguish grid-side AC metering from DC output.
3. **Mechanism**: Draw source→physical interface→receiving component; state governing conservation/constitutive/control law, valid control volume and alternative explanations. Shared ambient heat is not a cross-sector causal arrow.
4. **Model**: Choose minimum-sufficient states. Derive equations from laws and equipment operating constraints, not first from attractive architecture. Identify what is not identifiable.
5. **Prediction**: State a falsifiable expected sign/magnitude/time relation or an explicitly qualitative discriminant. No unsupported temperature→outage or temperature→SDG benefit.
6. **Test**: Specify compatible observations, comparable reference, perturbation and failure conditions. Distinguish exact arithmetic/unit/solver verification from external physical validation. Include null and contradictory outcomes; censor events that never occur.
7. **Decision**: Evaluate actual required electricity and mobility services and tradeoffs; propose Improve/Adapt/Restore only if interventions are in evidence and inside scope.
8. **Sustainability**: From supported service differences, map environmental/economic/social effects separately, functional unit and baseline, and indicator to eligible SDG target only when defensible; otherwise NOT_YET_MEASURABLE.
9. **Reflection**: Record what was misunderstood, disproven, corrected, learned and what case would invalidate transfer; promote to skill only after observed execution of tests.
10. **Communication**: Select output for task—brief Chapter 1 slide, source audit, derivation, code, visual or decision note; reveal only the detail the audience needs, while keeping traceability in source/notes.

## D. Six reusable competencies and acceptance exercises
| Competency | Required demonstrated performance | Adversarial challenge |
|---|---|---|
| K1 Physical interface accounting | Locate AC grid-side vs EVSE DC output ports, write consistent power/energy balance with auxiliary/storage boundary and units | No conflation of AC and DC; avoid double-counting auxiliaries |
| K2 Directional causal identification | Separate charging-demand→transformer heating from conditional transformer thermal state→permissible charging supply | No manufactured P→T_e outage from hot-spot temperature; shared heat is not propagation |
| K3 State-time mathematics | Derive applicable conservation relation, minimum states, initial conditions, event time and uncertainty with correct dimensions | No made-up model parameter, direct cross-state coupling or unconditional threshold crossing |
| K4 Evidence-oriented reading | Source-by-source extract equipment, equations, assumptions, validation setting, observed outputs, contradiction and access status | Cannot claim unseen paywalled full text, invented novelty or source transfer |
| K5 Reproducible comparison | Specify admitted M0/M1/M2 only if justified, matched heat/load/controls, censoring and evaluation against observed outputs | A difference of event times alone does not prove causal propagation |
| K6 Service-to-sustainability interpretation | Specify delivered versus required electricity/mobility service, independent sustainability dimensions, baselines and SDG eligibility | No local EVSE efficiency→official SDG 7.3.1 or fleet readiness→SDG 9.1.2 |

## E. Chapter 1 presentation competency learned from three versions
The **purpose of 13-slide Chapter 1** is understandable research justification and organized assumptions, **not** proving finished transformer equations or full empirical validation. Reuse these presentation functions: (1) title, (2) outline, (3) engineering background and electricity interface, (4) extreme heat/common forcing and evolving states, (5) research problem, (6) established evidence versus candidate gap, (7) proposed research questions, (8) current exact objectives, (9) complete physical boundaries + selected interface/active model, (10) modeling logic and provisional assumptions, (11) research activities and expected outputs, (12) resilience and two sustainability/SDG pathways, (13) proposed thesis roadmap.

Specific lessons to operationalize:
- Slides 5 and 6: **problem ≠ literature gap**. State the engineering uncertainty first; audit literature to determine where novelty, if any, survives.
- Slides 7, 8 and 11: **question ≠ action ≠ expected output**. Three distinct jobs, no duplicate prose.
- Slide 9: **complete system ≠ illustrative equipment ≠ active mathematical states**. AC voltage/current/power are interface observables, not interchangeable with DC charging output.
- Slide 10: State provisional assumptions explicitly: common ambient heat is exogenous; relevant states change with loads/loss/cooling; conditional operating and cross-system restrictions require case-specific law. A compact thermal conservation law explains a physical foundation without claiming a complete admitted model.
- Slide 12: **service resilience ≠ sustainability indicator ≠ SDG success**. Direct and engineering response pathways remain separate.
- One slide, one argumentative function and up to three supportive points except the exact objectives. Use real equipment illustration for physical architecture; editable scientific graphics for literature, method and assessment. White background, meaningful arrows and honest citation sources.

## F. Evidence-to-skill experience log (required for claims of learned mastery)
For each actual case/test, create an entry:
`case_id | date | task | equipment and site or SYNTHETIC | physical boundary | source/page/data hash | claim status | assumptions | actual test command/measure | expected/observed outputs | pass/fail/blocked | failure diagnosis | revised rule | transfer limitations | next case`.
Permitted states: LEARNED_CONCEPT, DESIGNED_EXERCISE, TEST_EXECUTED, SOURCE_SUPPORTED, PHYSICS_ADMITTED_FOR_CASE, VALIDATED_FOR_CASE, TRANSFER_NOT_ASSESSED, BLOCKED.
Do not call a concept or a skill document 'field experience'. Do not represent conceptual probes as executed testing.

## G. Stage gates
- G0 Scope and source admissibility.
- G1 Reconstructed real equipment physics with consistent AC/DC/control volumes.
- G2 Mathematical derivation and identifiability with explicit assumptions.
- G3 Executed verification tests (if code exists).
- G4 Physical validation against independent compatible evidence, where feasible.
- G5 Defined service and sustainability/SDG eligibility.
- G6 Audience-appropriate artifact and real presentation QA.
Progress may be BLOCKED without invented substitutions. At Chapter 1 presentation stage, successful organization and honest OPEN tags are sufficient; G4 is not a condition for explaining a proposed investigation.

## H. Continuous improvement without pretend autonomous learning
On every subsequent applicable task: retrieve previous case logs and current skill; identify which prior error applies; run appropriate tests when possible; record error→correction→actual retest; revise accepted patterns only with evidence. No scheduled background learning, experiential memory update, model retraining, or general claim of 'full knowledge' is established by writing this document. Explicitly communicate blind spots and prioritise full-text primary research and actual case-specific laws over expanding theoretical frameworks.
