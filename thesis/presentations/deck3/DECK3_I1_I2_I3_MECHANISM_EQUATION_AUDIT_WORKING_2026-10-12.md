# Deck3 I1–I3 arrow, operator and equation audit — working review (2026-10-12)

**Status:** source-grounded *semantic review*, not case-specific empirical verification, approved figure revision, or amendment to frozen thesis content. **Keep the existing eight selected components, IDs, and diagram geometry.** Do not replace canonical I1–I3 with older broad-scope labels.

## Exact component identities (unchanged)
P1 Distribution Transformer; P2 Distribution Feeder; P3 Transformer Protection/Load-Management Hardware; P4 Transformer Cooling Equipment; T1 DC EV Charger; T2 Vehicle Battery Pack; T3 EVSE Cooling Equipment; T4 Vehicle HVAC Equipment. Their presence in the figure does **not** imply eight intersystem mechanisms or eight ODE states.

## Direction-specific mechanism contracts

| ID | Physically defensible path | Arrow semantic class | Governing relation / necessary data | Status and forbidden inference |
|---|---|---|---|---|
| I1 | P1 secondary → P2 feeder → T1 **grid-side AC** input | P→T_e *electrical supply*, not a thermal-causality arrow | AC port voltage, phase current, real/reactive power and topology; compatible time-stamped meter/control-volume definitions | Physical transfer principle; actual site topology and data OPEN. Does not establish P thermal-state-conditioned restriction. |
| I2 | T1/T3 temperature/cooling and charging operation → T1 **grid-side AC P/Q/current** → P2 feeder loss/loading → P1 loss/temperature response | T_e→P *demand-mediated state influence*; **not reverse electrical energy flow** | Charger AC input measured/derived consistently with DC output, converter loss and auxiliary draw; feeder network and transformer loss/thermal equations; comparable times | CANDIDATE. Charger temperature-to-AC-demand response and P thermal consequence need case-specific evidence; no assumed V2G. |
| I3 | P1 thermal state/operating limit → P3 **installed and enabled** protection/load-management rule → permitted AC supply through P2 → T1 AC input → delivered charge/T2 readiness | P→T_e *state-conditioned control/constraint*, distinct from ordinary I1 | Actual P3 sensor, implemented rule, command path, event logs, permissible AC-power setpoint and charger response | CANDIDATE / blocking evidence gate. Temperature reading, loading guide or advisory alone is **not** evidence of an implemented restriction. |

**Heat:** H(x,t) acts externally on P and T_e; two parallel heat-response arrows are *common forcing*, not I2 or I3.

## Operator and equation semantics

1. **Transformer thermal balance:** `C_w dT_w/dt = P_w,loss(I,T_w) - Qdot_w→o`; `C_o dT_o/dt = P_core,loss + Qdot_w→o - Qdot_P4→amb`. Both sides are watts, `C` J/K, temperature rate K/s. These are **candidate lumped templates**, not equipment-specific admitted laws. P4 heat rejection is counted **once**.
2. **Feeder electrical loss:** `P_feeder,loss = Σ_phase I_phase² R_phase(T)` (W) for justified phase/segment topology and resistance convention. This is a loss, not a second independent source of energy. Overhead and buried feeder heat-transfer operators are not interchangeable.
3. **P3 switching/control:** `m_P(t+) = R_installed(T_sensed, I, timers, m_P, u_P)`. The operator maps observed state and implemented settings to an *actual* discrete action; until installed hardware, enabled logic and logs are evidenced, the rule is OPEN and the arrow must remain conditional.
4. **P4 cooling:** `Qdot_P4 = H_P(T_o,T_a,geometry,u_cool,P)` (W), a heat-rejection operator **inside P**, not a cross-system interface. Electrical fan/pump auxiliary draw must be accounted for separately.
5. **T1 port balance:** `P_AC,EVSE = P_DC,EVSE + P_conv,loss + P_EVSE,aux` (W) only with aligned metering/control-volume assumptions and negligible relevant stored-energy derivative; otherwise include stored-energy change. T3 electrical auxiliaries behind the EVSE AC meter belong in `P_EVSE,aux`; cooling heat rejection is not another conversion loss.
6. **T1 thermal state:** `C_e dT_e/dt = P_conv,heat - Qdot_T3` (W), *candidate simplified* heat balance, adding other exchange terms where required. `P_DC,offered ≤ C_E(T_e,T_a,u_e)` is conditional on documented equipment derating; offered ≠ delivered ≠ battery-accepted power.
7. **T2 energy/SOC:** `dSOC/dt = I_cell,equiv/Q_nom` only after defining current sign, units and efficiency; alternatively `dE_useful/dt = eta_store P_B,terminal` for a calibrated stored-energy model. Do not count both as independent charge-energy additions. SOC is not a thermal state. DC charger output is not necessarily battery-terminal energy.
8. **T3 cooling:** `Qdot_T3 = H_E(T_e,T_a,u_cool,E)` (W) and `P_cool,E = f_aux(u_cool,E,T_a)` (W) where supported; the former is heat removal, the latter electrical auxiliary demand. Do not double count either.
9. **Coupled mathematical model:** `dx_P/dt=f_P(x_P,z,H,u_P;theta_P)`, `dx_Te/dt=f_Te(x_Te,z,H,u_T;theta_T)`, `0=g(x_P,x_Te,z,H,u;theta)`, `Q=h(x_P,x_Te,z,u)`. These are a **candidate DAE structure**, not a validated or identified causal law. `z` is algebraic unless independent interface memory is demonstrated; `Q` is service output, not state. Model closure, units and constitutive maps OPEN.
10. **T4 demand pathway:** hot-weather HVAC draw → trip battery depletion → later required charging → T1 AC demand → P loading. This is a delayed *demand-mediated* candidate, **not** an instantaneous T4→P thermal arrow.

## Figure-preserving correction instructions

- Keep P1–P4 and T1–T4 names, positions, grouping and membership. Add short direct labels on existing arrows where scientifically necessary; do not invent a new legend or extra system.
- Label I1 `AC supply (P→Tₑ)`, I2 `grid-side AC demand → P loading/thermal response (candidate)`, I3 `P3 implemented thermal restriction → AC availability (candidate)`.
- Separate heat-forcing arrows from intersystem causal arrows. Show I2 and I3 as **independently gated candidates**; do not draw a verified reciprocal heat-exchange arrow or a bidirectional electric-energy arrow.
- If an existing arrow bypasses P3 on I3, do not imply automatic transformer-temperature→charger derating; qualify or reroute the arrow **without removing any component**.
- If an existing arrow depicts T1 DC output or T2 battery power as I2's Power-facing quantity, change the **arrow's quantity label** to grid-side AC input P/Q/current and keep DC/battery quantities in T_e.
- Keep direct annotation brief and readable; use the existing approved Deck3 palette and white backgrounds. A figure remains provisional until a concrete slide/asset is identified and visually inspected.

## Required unresolved evidence

Site P1 transformer type/cooling/sensors; P2 feeder topology and AC measurements; P3 installed enabled controller/relay logic, setpoints and actuation logs; T1 actual AC demand vs thermal/cooling/derating and DC output; T2 pack terminal measurements and departure requirement; T3 auxiliary/cooling observations; T4 trip energy and schedule evidence for any demand-mediated claim. Identify event onset, source/receiver delay and recovery **separately**; no numeric threshold or causal attribution without evidence. Source-specific APA references and rights review remain necessary.

**Authorities:** `project/thermal_sos_functional_architecture/SELECTED_EIGHT_COMPONENTS_WORKING_RESEARCH_BASELINE_V1.md`; `project/thermal_sos_functional_architecture/EIGHT_COMPONENT_PHYSICS_AND_DIRECTIONAL_INTERFACE_RESEARCH_DOSSIER_V1.md`; `project/thermal_sos_functional_architecture/WORKING_SOS_COMPONENT_FUNCTION_INTERFACE_MATRIX_V1.md`; higher canonical scope/evidence/state-time documents. **Note:** the working architecture matrix has an older P1–P5 candidate indexing scheme; its row labels must not override the newer approved P1–P4/T1–T4 presentation IDs.
