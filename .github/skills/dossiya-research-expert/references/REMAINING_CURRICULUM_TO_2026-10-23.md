# Dossiya Research Expert — Remaining Learning and Evidence Gates

**Status:** working educational roadmap (2026-10-09); **NOT** a frozen research plan or ASU deadline authority. Target **October 23, 2026** to finish focused foundational lessons; case/interface/data decision target **October 31, 2026**, subject to supervisor direction. Spring 2027 research/defense gates follow from current repo handoff and current ASU policy checks.

## Core philosophy
Avoid "learn everything before research". Instead ask: **What must I understand to qualify one physically real heat-conditioned mechanism, build the minimum-sufficient model, calculate a defensible service consequence, and defend its credibility?** Learn that, demonstrate it, and immediately apply it. Search only when a new source resolves a specific unknown.

## Learning status as of October 9
- **Written conceptual/model reasoning:** Lessons 01–11 passed as chat examination submissions.
- **Mathematical derivation:** first-order balance, time-event formula, basic 2x2 observability handled in writing; independent derivation under closed-book conditions NOT PROVEN.
- **Numerical methods, practical observation/identification, evidence acquisition, and actual-case model validation:** NOT YET DEMONSTRATED.
- **Lesson 12:** PENDING; weak observability versus numerical estimation reliability.
- **Independent data/case choice, active thermal states, directional coupling laws, equipment parameters, operational limits, validated electricity/mobility services, response set:** OPEN.

## Priority curriculum before October 23

| Time window | Focus | High-value exercise/output | Pass criterion / evidence gate |
|---|---|---|---|
| **Oct 9–10** | **L12**: mathematically observable versus practically reconstructible; noise, weak sensitivity, signal scales | Rank calculation for epsilon=1 and 0.001; compare estimation sensitivity under explicitly synthetic perturbations; short note identifying what is and is not inferred | Correct observability calculation, units/scaling/noise caveat, no real-coupling claim |
| **Oct 11–12** | Heat transfer and model admissibility: conservation, heat sources/rejection, boundary conditions, time constants, one/two-node limitation, temperature gradients | Independently derive and unit-check a lumped thermal model; check equilibrium/limiting conditions; explain when lumped assumption is unsafe | Every term has physical meaning, dimensions and validity assumptions; no generic law promoted as actual transformer model |
| **Oct 13–14** | Candidate Power-side thermal behavior: loading, cooling, temperature sensing, top-oil versus hotspot, real operating restrictions | Two primary-source audits (exact clauses/equipment data if accessible); state-versus-capability map with source links | State, sensor, constraint and control clearly distinguished; equipment-specific limits remain OPEN unless verified |
| **Oct 15–16** | Candidate Electrified Transportation thermal behavior: EVSE/DC charger, AC-side input versus DC-side output, loss/efficiency, vehicle acceptance, charging controls | One exact-study or equipment audit; trace measured heat-conditioned capability through actual charger ports and functions | No unsupported transfer of a derating curve across equipment; identify which current/power side is measured |
| **Oct 17–18** | Qualify directional interfaces: P→T_e and T_e→P separately; common heat confounding; electrical transfer vs thermal conditioning | Mechanism-to-evidence-to-service register; rival explanations and data requirements; select only supportable directional candidate(s) | Source, thermal condition, exchange, receiver and measured service relevance exposed; each arrow QUALIFIED / PARTLY SUPPORTED / OPEN / REJECTED |
| **Oct 19–20** | Reduced state-space and numerical credibility: ODE setup, physics-appropriate interface constraints, solver convergence, sensitivity, stable scenario differences | Minimal synthetic or source-calibrated model verification notebook, with analytical/limiting-case tests and timestep comparison | Reproducible tests executed; label **VERIFIED NUMERICS ONLY** if no independent observations |
| **Oct 21–22** | Service and uncertainty: measured electricity service and declared mobility requirement, arrival/departure, delivered energy vs battery usable energy, event times, parameter uncertainty | One matched-comparator specification and an SO3 metrics table, with source, units, threshold and data status | Distinguish capability/actual charging/service, critical crossing/response delay, nominal margin/guarantee/observed deficit |
| **Oct 23** | **Mastery exit examination and handoff** | 10–15 minute no-notes oral explanation; derivation; source critique; one runnable verified small notebook; list of case/data gaps and supervisor decisions | All critical distinctions correct; code reproducible; evidence gaps honestly OPEN; research feasibility plan approved for discussion |

**Planning discipline:** These are focus blocks, not claims that exact study hours, real observations, full literature review, final model and independent validation can be completed in 14 days. If data/equipment access is unavailable, record the blocker and raise it to the supervisor instead of inventing observations or parameters.

## What Dossiya must still learn (beyond the eleven written passes)

| Knowledge / skill | Why it is necessary | Evidence of actual mastery | Priority |
|---|---|---|---|
| Thermal energy conservation, lumped-model validity and spatial hotspot limits | Physical explanation and model selection | Re-derive, unit-check, limiting-case test and identify simplification failures | Critical |
| Transformer temperature-to-operating-envelope connection | A Power thermal state alone does not establish available electricity | Verified standard/manufacturer/physical model gate for selected asset | Critical |
| EVSE heat-conditioned input/output capability and control | A charger's own derating differs from upstream Power constraint | AC/DC boundary and thermal control evidence for actual equipment | Critical |
| Thermally conditioned P→T_e / T_e→P causal direction | Central SO1; common heat and electrical load alone do not qualify | Two independently examined directional qualification rows | Critical |
| Minimum necessary dynamic states, observability and parameter identifiability | Prevent untestable, excessive models | Admitted-state justification and noise/parameter checks | Critical |
| ODE solver, step-size refinement, conservation and scenario comparators | SO2 numerical correctness | Reproducible code and benchmark/limit tests | Critical |
| Critical transition, source event, interface delay, service time, recovery definitions | SO3 timing inference | Event register and measured/model-derived event algorithms | Critical |
| Q_P/Q_T requirements and actual service loss versus margins | Thesis outcome is service, not simply temperature or charging speed | Units, demand/service assumptions, verified transport task | Critical |
| Measurement design, calibration, uncertainty, independent validation | Model claims bounded by evidence | Data split, sensor mapping, uncertainty report, external validation if feasible | Critical |
| Resilience and two sustainability consequence pathways | Correct bounded interpretation of SO3 | Distinct service effectiveness, economic/environmental/social indicators ONLY if supported by data | Supporting |
| Formal causal identification/controls beyond one selected interface | Not needed for whole network model | Study only if critical direction cannot be distinguished without it | Conditional |
| Large GIS dashboards, VisQuill viewers, universal optimization, all 200 papers at full depth, Lean theorem proving | Not automatically needed to answer SO1–SO3 | Defer unless a real accepted result calls for them | Outside urgent path |

## Hard research gates after the foundational period

### October 24–31 — qualify feasible actual case
Deliver: source/equipment/dataset inventory; exact Power asset and selected bounded T_e application; chosen **qualified or still OPEN** direction(s); physical source-to-receiver mechanism; mobility and electricity requirement definitions; credible model and measurement plan; matched-comparator design; supervisor decision log.

**Stop / narrow** if there is no credible interface evidence, no usable data, no accepted service basis, or a prediction claim cannot be tested. Do not force bidirectional feedback or invent a connection.

### November — mathematical and modeling implementation
Derive/adopt qualified laws and operating constraints; admit only required thermal, energy or control states; implement coupled state-time ODE/hybrid representation where supported; complete solver verification and reproducible numerical tests; document source/parameter provenance.

### December — baseline and initial verification
Finish a bounded executable model with documented operating conditions and valid comparator; analyze critical crossing and propagation definitions; prepare initial uncertainty sensitivity and results.

### January 2027 — independent empirical adequacy / uncertainty
Test predictions against observations not used for calibration where feasible; analyze parameter identifiability and sensor coverage; report domain-limited credibility honestly. If independent data are unavailable, explicitly state that the validation gate remains unmet; do not claim complete physical prediction validation.

### February — SO1–SO3 research results
Qualify the supported causal paths; quantify defensible state-time and electricity/mobility-service consequences. Interpret resilience with declared service requirements; evaluate only supported sustainability consequences and response effects, where data exist.

### March–April — finish and defend
Write/revise complete manuscript, obtain supervisor/committee feedback, submit formatting and defense materials per the **live ASU Graduate College calendar**. Verify graduation filing, defense scheduling, defense completion, format-review and ETD deadlines from ASU directly; do not treat study dates here as formal ASU deadlines. The prior repository handoff lists an April 2027 defense/ETD schedule as working reference.

## Final October 23 mastery exam — observable deliverables
1. Whiteboard or text: draw **full P/T_e system boundary** and selected case subset, distinguish extreme heat from internal state.
2. Derive one conservation law, verify each unit, explain the conditions for lumping and what the model omits.
3. Trace at least one **candidate** direction with thermal source state → verified/pending capability law → electrical interface → receiver physical/functional change → declared electricity and mobility services; mark evidence.
4. Derive/compute a state trajectory and first event time without confusing tau_th with transition/propagation/service onset.
5. Compute an observability matrix and demonstrate why rank does not ensure a robust estimator.
6. Write and run a tiny solver verification with known benchmark, conservation/limit and timestep refinement.
7. Explain calibration, structural/practical identifiability, external validation, uncertainty propagation and data sufficiency.
8. Defend whether adding a justified interaction changes a service-relevant conclusion relative to an appropriate physically valid comparator; distinguish unknown from negative results.

**Pass means foundation-ready for bounded research, not expert certification.** Failure of a core gate directs a targeted short remediation, not a restart of all 12 lessons.

## Sources and reading economy
- Canonical repository science and evidence standards take priority.
- Use an appropriately narrow A1/A2/A3/A4/A5 primary reference for the exact current question; distinguish official guidance from experimentally observed case-specific effects.
- Existing evidence handoff project/handoffs/EVIDENCE_INTEGRATION_REGISTER_2026-10-08.md and the active thermal 200-paper research school already contain screened sources and stated limitations; **do not duplicate 200 full-text reviews** for this two-week goal.
- Cite verified source claims adjacent to each substantive claim. State [OPEN] where full text, exact manufacturer law, dataset or operational constraint has not been established.

## Learning after October 23
Stop separate endless numbered lectures. Learn within actual thesis work: read a source to choose one equation; implement a model to test a state; measure a quantity to validate one prediction; explain a result to respond to one supervisor question. Continue the five-step cycle, but the **artifact** must now be a research deliverable.
