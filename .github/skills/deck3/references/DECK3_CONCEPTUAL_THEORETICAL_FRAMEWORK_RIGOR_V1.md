# Deck3 and Thesis — Theoretical/Conceptual/Physical-Model Coherence Standard V1
Date: 2026-10-10. Status: governing methodology supplement, not evidence that scientific hypotheses have passed.

## Scope and sources
- Thesis: Physics-Based Mathematical Engineering of Power–Electrified Transportation Interdependencies for Resilience. Heat-conditioned P/T_e coupling investigated conditionally.
- The user-supplied English EcoStatiScience methodological synthesis is contextual inspiration, not a governing physical law.
- Research methodology: Jabareen, Y. (2009), *Building a Conceptual Framework: Philosophy, Definitions, and Procedure*, International Journal of Qualitative Methods 8(4), 49–62, DOI:10.1177/160940690900800406. IMPORTANT: this article is a predominantly qualitative/interpretive framework treatment; its variable-based/statistical reading must not be falsely attributed to Jabareen.
- Causal inference methodology: Hernán & Robins, *Causal Inference: What If* (causal identification assumptions are not proved by directed arrows). Do not assert a causal DAG is empirically verified merely from the drawing.
- Thermal device literature: Bernardi et al. (1985), DOI:10.1149/1.2113792, is battery-specific, not transformer validation. Additional transformer/EVSE articles require per-claim verification.

## Four distinct representations (do not collapse)
1. THEORETICAL: conservation of energy, electrical circuit/network equations, heat transfer, dynamical and hybrid systems. Apply only within physical control volumes and validity domains.
2. CONCEPTUAL: selective research-specific relationships between forcing, equipment thermal state, actual operating/control consequences, AC-mediated cross-system behavior, and service requirements. A conceptual arrow is a research proposition or conditionally admitted relation, never proof.
3. MATHEMATICAL: state/control/algebraic/event equations, actual physical units, initial and boundary conditions, parameter domains, observability and uncertainty. A conceptual relation only enters the active model if its governing mechanism and admissible parameters are documented.
4. NUMERICAL/EMPIRICAL: IEEE13 B0 reference reproduction, B1 documented EVSE modification, independent mechanism tests, IEEE123 evaluation, matched counterfactuals, numerical verification, field validation only if real observations exist. Numerical implementation is not empirical validation.

## Thesis-specific selective conceptual framework
External forcing: extreme heat T_a(t), exposure and boundary conditions affect P and T_e independently. Shared exposure ≠ physical propagation.

Candidate P→T_e:
transformer/electrical physical state -> **if justified** applicable operating/protection restriction -> AC supply/EVSE feasible charging capability -> **if defined and shown** battery readiness/mobility service effect.

Candidate T_e→P:
EVSE or battery thermal state -> control/derating response -> actual measured **grid-side AC** V,I,P,Q (not DC-only vehicle power) -> electrical losses/loading -> power-side thermal state / service effect. Derating may lower, not necessarily raise, transformer losses.

Physical electrical port, cooling/ambient and service requirements must not be drawn as the same kind of edge. All carried quantities, time dependence, sign, units, boundary, operator and evidence status shall be recorded.

## Variable/function taxonomy
- Exogenous forcing: T_a(t), weather, independently specified external conditions.
- Physical states: transformer hot-spot/oil temperature only where model and parameters admitted; EVSE/battery temperatures; stored energy as appropriate.
- Algebraic port variables: V_AC,I_AC,P_AC,Q_AC with signs and AC phase conventions; voltages/currents dependent on network model.
- Control actions/modes: EVSE derating, transformer protection, load management; NOT assumed simply due to a threshold unless actual logic documented.
- Device parameters: thermal capacity, loss coefficients, rating and cooling properties with uncertainty; don't confuse constants with measured state variables.
- Disturbances/background loads: realistic paired-comparator controls, not automatic statistical adjustment.
- Observable services: defined electricity service and mobility service, deadlines/required functionality; charging kWh alone not necessarily mobility.
- Uncertainty/evidence: structural uncertainty, unknown coefficients, available observations, competing mechanisms.
- The complete 19+21=40 entry ledger gives physical/functional coverage; not 40 variables, state equations or automatically active diagram nodes. Each entry disposition: active, aggregate, boundary, control/observation, service/conditional, excluded with justification.

## Arrow / hypothesis gate
For each arrow register:
ID; slide; source component/system and destination; relationship type (conservation/physical flow/control/measurement/state dependence/hypothesized propagation/methodological sequence); carried quantity, SI units and sign; physical law or engineering mechanism; assumptions; article/engineering-source evidence + exact adjacent author–year citation if a published claim; support level VERIFIED_LAW / LITERATURE_SUPPORTED_COMPONENT / QUALIFIED_CANDIDATE / OPEN / REJECTED; testable prediction or falsification rule; mathematical equation or observation; relevant service result; uncertainty; current QA and rights.
- Do not require every physical flow/conservation connector to be a separately numbered statistical H1; established laws have derivations and validity conditions.
- For any unverified cross-system arrow require a falsifiable candidate hypothesis or research question with a measurement/experiment that could reject it.
- Distinguish causal design from a mechanism diagram: a directed causal hypothesis is not automatically identified; a physical interconnection does not establish interdependence under the investigated disturbance.

## Example falsifiable tests (not performed)
H_P→T: under specified extreme heat and comparable background electric loading, a documented transformer constraint changes AC charging feasibility and a defined mobility service, relative to a matched admissible baseline. Possible no-effect.
H_T→P: a heat-conditioned EVSE control change alters *grid-side AC* power/current and corresponding transformer loss/temperature trajectories relative to matched charging conditions; sign not prescribed.
H_T: critical times and propagation delays are estimable only after establishing transition definitions, temporal sampling resolution, uncertainty bounds and matched outcomes; censored no-event cases must remain no-event.

## Model (proposal, NOT_RUN)
For a thermally defined control volume, dU_th/dt = P_heat - Qdot_net,out (signs and inclusions depend on CV definition).
General proposed hybrid DAE M_q(x) xdot = f_q(x,z,u,T_a;theta), 0=g_q(x,z,u,T_a;theta), with q discrete operating state. This is a **model architecture**, not a verified device constitutive law or a paper-derived full system result.
Pre-model: identified ports and equipment physics. Post-model: service thresholds and sustainability direct-vs-response analysis separately. Sustainability indicators must not be equated with official SDG indicators without matching specifications.

## Conflict decisions (higher-rigor rule prevails)
1. "Every arrow is hypothesis" is too broad: physical laws, measurements, signals, workflows and candidate causality have distinct semantics. ALL arrows scientifically explained; only *hypothesized* interdependency arrows need candidate H/test.
2. Social-science regression IV/DV/mediator/moderator taxonomy must not be imposed on dynamic engineering states/parameters. Use physical state/input/control/parameter/observable/constraint first. Statistical mediation/moderation terms only if estimand and identification assumptions are defined.
3. Complete 40-component inventory is NOT the conceptual framework. Preserve complete architecture and traceable dispositions but keep active conceptual model minimal sufficient.
4. Theory and conceptual framework are related but not identical; governing equations are a third representation, numeric model a fourth.
5. "Arrow means causality" is false without evidence/identification. Clearly label conditional hypotheses, shared heat confounding, independent mechanisms and uncertainty.
6. Avoid copying external diagram styles. Source rights/AI originality gate still applies.
7. The current user-approved Chapter 1 presentation is 14 slides (Slide 14 journal articles only); older default "13 slides" references are superseded **for this specific version**, without retroactive rewrite.
8. Preserve full exact GO/SO1–SO3 as frozen user-facing objectives, but investigate their hypotheses scientifically rather than assuming mechanisms verified.
9. Times New Roman all authored lettering, exact 13 colors, 16:9 (13 1/3 ×7.5 in), white surfaces, native editable scientific arrows/citations/objects, click-to-reveal and independent desktop playback gate.
10. Evidence-source traceability includes engineering standards/benchmark docs in notes or provenance, while bibliography Slide 14 contains only journal articles.

## Slide-specific application
S3 system architecture and physical interface, not unproven thermal causality;
S4 independent common extreme heat + equipment response;
S5 selective directional conditional research hypothesis;
S6 source-supported component findings vs open nearest prior art;
S7 RQ1 mechanisms / RQ2 mathematical modeling / RQ3 consequences;
S8 exact GO/SO1–SO3, no article falsely claiming authorship;
S9 40 class register vs minimum active subsystems, grid-side AC plane and IEEE bench documentation;
S10 lawful physical balance, distinguish general conservation from battery-specific empirical literature;
S11 B0/B1 and IEEE123 verification/validation/uncertainty and matched comparisons;
S12 electricity/mobility services then direct sustainability vs response (Improve/Adapt/Restore);
S1/2/13/14 other slide roles preserved; Slides 3–12 visuals only.

## Release checks
- Each selected concept justified by problem, theory/literature or explicit assumption.
- Each arrow typed, sourced, units/sign where relevant, evidence-status, related RQ/H and method for possible rejection.
- No empirically established directional impact unless validated.
- Control variables/parameters/forcing separable, no automatic labels as moderators/mediators.
- All 40 entries dispositioned without visual overload.
- Active model translated to observables, operating states, equations and comparisons with explicit uncertainties.
- Figures, palette, citations, native animation targets, real playback and license remain independent PASS/FAIL/OPEN/NOT_RUN gates. Never call "PASS" on instructions alone.
