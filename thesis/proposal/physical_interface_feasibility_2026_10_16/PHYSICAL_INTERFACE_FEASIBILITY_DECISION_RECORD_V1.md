# Physical Interface and Experimental Feasibility — Scientific Gate Register

Date: 2026-10-16
Thesis: Engineering of Power–Electrified Transportation Interdependencies for Resilience
Focus: Extreme-heat-induced thermal interdependencies between Power P and Electrified Transportation T_e.
Status: FOR ADVISOR FEASIBILITY REVIEW ONLY. Not an approved experimental site, model, validated result or final methodology.

## Advisor assessment interpreted narrowly
Retain title, focus, General Objective and SO1–SO3 without alteration. Advance to PHYSICAL INTERFACE AND EXPERIMENTAL FEASIBILITY before selecting PHY/GREY/PIML. This assessment is user-supplied; no separate institutional approval is claimed.

## Candidate case, not an installed/approved case
One identifiable distribution transformer supplying one instrumented DC fast EVSE, with upstream Power-side feeder metering and temperature sensing, EVSE internal rectifier/cabinet sensing and controls, independent AC input/DC output metering, and BEV charging sessions linked to a declared service requirement. A ~50 kW charger is a literature-motivated *class* based on Krama et al. 2026, not an identified on-site asset or manufacturer. Utility feeder, transformer kVA/ratings, permissions and EVSE make/model remain OPEN. Fleet/depot is an alternative if it better satisfies synchronized data and vehicle departure requirements.

The transformer is inside P; EVSE, battery and vehicle and charging controls are inside T_e. The AC connection carries electrical quantities and operating decisions; this does not establish direct conductive heat exchange or vehicle-to-grid export. Extreme ambient heat separately forces P and T_e.

## Mechanism P→T_e — NOT QUALIFIED
Required: observable P component thermal state -> documented applicable P thermal rating/protection/operator constraint ACTUALLY activated -> logged AC allocation or limiting action -> observed EVSE AC/DC capability or output consequence -> defined electricity/vehicle service. A transformer temperature rise without an actual temperature-conditioned power restriction does not prove P→T_e. Obtain utility dispatch/event logs, exact asset topology, Power temperature sensor location and EVSE AC/DC meter alignment. References: Blomgren 2023 DOI 10.1016/j.segan.2023.101048; Villarroel 2017 DOI 10.1049/oap-cired.2017.1102.

## Mechanism T_e→P — COMPONENT PRECEDENT; RECEIVER UNQUALIFIED
Required: EVSE internal temperature + evidenced thermal-derating controller -> actual changed AC power/current with controls for EV SOC taper, BMS and grid orders -> P transformer current/loss change -> attributable later measured transformer temperature. Derating may relieve transformer heating, change session timing or shift load later; do not assume cascading harm. Krama 2026 DOI 10.1016/j.ecmx.2026.101960 reports field charger heat derating; Godina 2016 DOI 10.1016/j.enconman.2016.04.087 models EV charging effects on transformer heating/aging; Balogun EV-EcoSim DOI 10.1109/TSG.2023.3339374 co-simulates network and transformer thermal dynamics. Unrelated sites do not constitute synchronized field coupling.

## Measured vs modeled vs unavailable
Published actual transformer CASE/LID observations: Blomgren; not directly winding hotspot.
Published actual optical winding hot spots: Villarroel, a DIFFERENT laboratory transformer, not the proposed feeder.
Published actual EVSE thermal derating: Krama, publisher abstract-level audit; original PDF and raw data not obtained.
Transformer hot-spot in Godina: simulated using physical transformer models and real load input data.
EV-EcoSim grid–charging exchange and transformer thermal response: simulated, not jointly field-observed.
Actual proposed-site Power and EVSE measurements: NONE ACQUIRED.
Actual vehicle departure-energy requirement and observed trip/schedule: NONE ACQUIRED.
Four subscription database systematic searches: NOT RUN; PRISMA counts unknown.

## Minimum candidate mathematical physics (T1 schematic, NOT chosen model)
- Positive unidirectional charge port: eta_wall=P_DC/P_AC,EVSE, including all wall auxiliaries (dimensionless; when AC input >0).
- Transformer thermal balance: C_P dT_P/dt = P_loss,P(I,V,T_P) - (T_P - T_a)/R_th,P. Units: J/K*K/s=W; R=K/W. State sensor target must be defined as case/oil or separately validated winding estimate.
- EVSE thermal balance: C_E dT_E/dt=Q_gen,E(P_AC,P_DC,u) - Q_rej,E(T_E,T_a,u_cool). Terms W, C J/K. Do not double count converter heat, auxiliaries and cooling.
- P→T_e restriction only where observed: S_tr<=S_allow,P(T_P,T_a,history) and P_AC,EVSE<=P_alloc,P actual logged allocation. kVA cannot be converted by subtracting non-EV kW alone; phase RMS/harmonics and Q matter.
- T_e heat limit only if documented: P_DC<=min(P_command,P_allow,E(T_E,T_a,u)). No assumed numeric threshold or battery-BMS limit.
- Event threshold/transition times require a sourced constraint; propagation delay requires independently attributed source/interface/receiver times, not two arbitrary correlated peaks.
- Electricity and vehicle departure-energy requirements must be independently set, not inferred from session time. Delivered charging energy is a proxy, not measured mobility completion.

## Data and validation feasibility decision
A — Preferred: same-site, time-synchronized Power and T_e raw sensors and command/event logs, with independent service requirements; identification and independent holdout possible only after data QA.
B — Restricted: separately measured component-level calibration/validation plus explicitly SIMULATION-ONLY physical cross-interface effects; no field causal claim; supervisor must approve this empirical ceiling.
C — Stop/redesign: absent active thermal mechanism, lawful original data, excitation/identifiability or service requirements. No invented substitute.

The necessary method tests are units, energy conservation/physical residuals, initialization/boundary conditions, sensor position, clock/uncertainty, structural/practical parameter identifiability and independent measured targets, with PHY baseline and GREY/PIML only if warranted. Numerical comparison to FVM is not independent experimental validation (Bragone 2022 DOI 10.1016/j.epsr.2022.108447).

## F0–F8 decision status
F0 real site/equipment topology: BLOCKED.
F1 actual thermal P-side restriction and EVSE receiving response: NOT ESTABLISHED.
F2 EVSE derating to measured P thermal response: COMPONENT EVIDENCE ONLY.
F3 legal raw synchronized P and T_e data: BLOCKED.
F4 admitted physical states/equations: PROPOSED, NOT FROZEN.
F5 parameter identifiability and uncertainty: NOT TESTED.
F6 independent physical validation: NOT TESTED.
F7 electricity and mobility-service requirements: BLOCKED.
F8 systematic prior art search and supervisor feasibility decision: OPEN.

## Next advisor decisions
1. Accept/modify DC fast charging candidate versus instrumented fleet/depot.
2. Require joint field validation or permit component-validated coupled simulation if matched data unavailable.
3. Permit independent qualification of one direction without forcing both.
4. Define measurable electricity and actual vehicle readiness/mobility service requirement.
5. Set required site inventory, data permissions, time-series QA, model-identifiability and proposal milestones.

Current recommendation: Authorize PHYSICAL SITE AND DATA SCREENING, not final model selection, not proof of bidirectional thermal interdependency and not service resilience validation.

## Authority and provenance
Frozen title V3, canonical thermal-only scope V1, extreme-heat V4, state-time definitions V1, resilience definition V1 and exact frozen GO/SO1–SO3 on main remain unchanged. Working proposal draft PR #86 is the parent; preliminary source-paper audit is separate draft PR #84. The present register is an evidence-bounded derivative of those sources and is not a newly executed systematic review.
