# Dossiya Research Mastery — Lessons 01–12 Record

**Snapshot:** 2026-10-09. **Source:** actual recorded chat examinations in this conversation. **Status:** working educational record; **NOT** primary domain evidence, external examination, credential or proof of independent code/model competence.

## Scoring disclaimer
The values below are **grades previously assigned to submitted chat answers** (not independently proctored scores). They establish that coherent written explanations were presented and evaluated. They do not prove unaided recall, authorship, mathematical independence, equipment handling, numerical reproduction, parameter estimation, physical validation, or real-world expertise. No grade should be silently raised or retrospectively re-awarded.

| Lesson | Essential scientific distinction or test | Last recorded grade | Learning status | Independent practical evidence |
|---|---|---:|---|---|
| **01** | Common extreme-heat forcing ≠ qualified directional thermal interdependency; stipulated mechanism ≠ field evidence | **97/100** | PASSED — chat reasoning | NOT TESTED |
| **02** | Equal measured temperature ≠ necessarily equal equipment allowable capability | **96/100** | PASSED — chat reasoning | NOT TESTED |
| **03** | Thermal time constant ≠ first critical boundary crossing ≠ source-to-receiver propagation delay | **98/100** | PASSED — chat reasoning | NOT TESTED |
| **04** | Thermally restricted power → reduced charging can coexist with fulfilled mobility requirement | **98/100** | PASSED — chat reasoning | NOT TESTED |
| **05** | Energy margin 20→5 kWh, 75% reduction; positive margin and service fulfillment ≠ demonstrated resilience loss | **98/100** | PASSED — chat reasoning | Simple arithmetic only; physical service assessment untested |
| **06** | Nominal +5 kWh; uncertain margin [-5,+10] kWh; range alone ≠ deficit probability; energy deficit ≠ proven service loss | **99/100** | PASSED — chat reasoning | NOT TESTED with measured distribution |
| **07** | Solver agreement with analytical benchmark ≠ independent physical model validation | **98/100** | PASSED — chat reasoning | NO NUMERICAL SOLVER TEST RUN |
| **08** | Calibration fit ≠ structural/practical parameter identifiability ≠ independent predictive validity | **90/100** | PASSED — chat reasoning | NO FIT/IDENTIFIABILITY TEST RUN |
| **09** | Hotspot estimate ≠ mathematical state observability ≠ measured physical hotspot validation | **97/100** | PASSED — chat reasoning | NO OBSERVER/MEASUREMENT TEST RUN |
| **10** | For A=diag(-1,-2), C=[1,0], O rows [1,0],[-1,0]: rank 1, state 2 unobservable from stated output | **100/100** | PASSED — paper calculation | NO COMPUTATIONAL/NOISE TEST |
| **11** | For A=[[-1,1],[0,-2]], C=[1,0], rank(O)=2; T2=y-dot+y (ideal model); this does not verify physical thermal coupling | **100/100** | PASSED — paper calculation | NO COMPUTATIONAL/NOISE TEST |
| **12** | For A=[[-1,epsilon],[0,-2]], C=[1,0], epsilon=1 vs 0.001: full rank for epsilon≠0 but potentially poor practical estimation | **NO ANSWER SUBMITTED** | PENDING — examine next | NOT TESTED |

## Mechanism and inference journey
The early attempts in Lesson 01 initially conflated two systems heating with thermally caused interdependency, and incorrectly inferred transformer stress or a feedback direction. Later written reasoning correctly identified the **source thermal condition → temperature-conditioned power constraint → electrical interface → receiver charging consequence**, with direction evaluated separately and the distinction between a **stipulated hypothetical** and real measured causality.

Do not treat any hypothetical transformer protective power derating as a verified operating law of a selected actual transformer. Threshold, equipment choice, exact charging context, model states, electrical/thermal coupling law, empirical dataset, service requirement, and parameters remain **OPEN** under current project authority.

## Verified *mathematical statements in the teaching cases*
These are elementary derivations under explicit assumptions, **not calibrated transformer/EVSE laws**.

**First-order lumped energy balance:**
- C dT/dt = P_loss - (T-T_a)/R, for uniform effective temperature, positive constant effective C,R, constant ambient temperature and constant heat generation in the elementary solution.
- T_infinity=T_a + R P_loss; T(t)=T_infinity + (T_0-T_infinity)exp[-t/(RC)]; tau_th=RC.
- If T_0<T_lim<T_infinity and this strictly increasing solution applies, t_C=RC ln[(T_infinity-T_0)/(T_infinity-T_lim)]. For any other forcing/temperature trajectory use a more general first-entry event definition, not the special formula.
- Lumped temperature dynamics alone does not determine hotspot, derating law, service outcome, or physical cross-system dependence.

**State/capability/interface/service:** thermal state X(t) ≠ effective allowed capability P_max(t) ≠ delivered P_charge(t) ≠ declared actual mobility service Q_T(t). E_charge=integral P_charge dt measured at stated electrical boundary is not automatically stored battery energy. SOC is an energy state, not a thermal state. External heat is input, not a system state.

**Service margin:** M_E=E_usable,dep - E_req. Positive margin in the stipulated task may coexist with reduced flexibility, but the service outcome depends on trip energy, time, reserve, route and other declared requirements; margin alone is not a complete service or resilience metric.

**Verification/validation:** matching an analytical benchmark checks limited solver functionality; fitting observations estimates parameters; observability concerns reconstructing states from a specified dynamic/measurement model; identifiability concerns recovering unknown parameters; independent validation assesses real-system predictive adequacy for the intended use, quantities and operating domain.

**Observability examples:**
- Uncoupled two-state diagonal A=[[-1,0],[0,-2]], C=[1,0], rank(O)=1.
- Mathematically coupled A=[[-1,1],[0,-2]], C=[1,0], rank(O)=2 and T2=y'+y under ideal known model/derivative (time units/temperature deviation implicit).
- Weak-coupling A=[[-1,epsilon],[0,-2]], C=[1,0] gives O=[[1,0],[-1,epsilon]], determinant epsilon: exact full-rank at nonzero epsilon, but measurement noise and scale/conditioning can make estimation unreliable. This remains **the Lesson 12 unexamined claim**.

## Remaining evidence status (not to be glossed over)
- No independent confirmation that completed answers were produced without assistance or without notes.
- No empirical transformer/EVSE measurements or actual-case protection law were supplied in the lessons.
- No executable reproducibility artifact proves a solver result, calibrated parameter, observer accuracy, numerical convergence or independent validation.
- A high score in a teaching example is not a research-result acceptance gate or permission to freeze any model object.
- Citation web previews in earlier exams are **not** automatically verified full-text references; re-open official/primary documents for any thesis citation, standard edition/clause, case-specific mechanism or numerical transfer.
- Several early scenarios stipulate a mechanism rather than establish it. Remember: **conditional causal story ≠ independent physical demonstration**.

## Next action
1. **Immediately:** conduct Lesson 12, including (a) rank, (b) magnitude/noise explanation, (c) no physical coupling inference; ideally add one small numerical noise/estimation illustration with clearly synthetic data.
2. Then switch from repetitive oral prompts to a **single case-oriented physical derivation and reproducible model exercise** by the October 23 foundational deadline.
3. Update this dated educational ledger by a new version or dated append when a real attempt or artifact exists. Do not overwrite canonical thesis files or fabricate completion.
