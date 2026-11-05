# Optimization Candidate OPT-2 — Harmonic-aware transformer aging / optimal charging time planning

**Date:** 2026-11-05  
**Decision:** Strong alternative/complementary method **candidate**, to compare with OPT-1 Qian et al. (2015) stochastic EV demand and thermal-aging planning. **NOT** an adopted controller; **NOT** new or established global optimum; **NOT** supervisor-approved or validated in current project.  
**Thesis:** Engineering of Power–Electrified Transportation Interdependencies for Resilience; SO1–SO3 unchanged.

## Source and precise claim
Gómez, J. C. & Morcos, M. M. (2003), *Impact of EV battery chargers on the power quality of distribution systems*, IEEE Transactions on Power Delivery, 18(3), 975–981, DOI https://doi.org/10.1109/TPWRD.2003.813873.
The abstract reports developing a **program** that accounts for modeled distribution transformer life consumption as a function of charger characteristics and charging algorithm, positioning the program as a distribution **planning and management tool**; it states the tool **can be applied** to select optimum charging time using existing load, ambient temperature and time of day. Its documented core physical emphasis includes **charger harmonic currents**. The available abstract does **not** establish source-code availability, a closed-form optimizer, achieved global optimality, deployment as real-time control, independent measured HST, or validated P→T feedback. Check original IEEE full text before making any of these claims.

Related OPT-1: Qian, K., Zhou, C. & Yuan, Y. (2015), *Impacts of high penetration level of fully electric vehicles charging loads on the thermal ageing of power transformers*, IJEPES 65, 102–112, DOI https://doi.org/10.1016/j.ijepes.2014.09.040; models stochastic initial SOC/start time/charging mode/EV penetration with transformer HST/aging and compares charging scenarios. Its optimum charging-time application is **likewise proposed/indicated**, not by itself evidence of a tested globally optimal joint aging-and-service controller.

## Complementary methodological roles
| Dimension | OPT-1 — Qian 2015 | OPT-2 — Gómez & Morcos 2003 |
|---|---|---|
| Core variation | Probabilistic vehicle arrival, initial SOC, charger mode, penetration | Charger current waveform/THD and charging algorithm; existing load, ambient and time of day |
| Physical mechanism | Coincident fundamental/total transformer loading → HST → equivalent aging | Fundamental + harmonic-sensitive transformer losses → heating/aging |
| Use | Stochastic thermal demand and charging-time scenario benchmark | Harmonic-aware planning and charger-choice/scheduling benchmark |
| Evidence ceiling | Model-based T→P aging and comparative scheduling | Model-based T→P power quality and aging; no demonstrated P→T causal control feedback from abstract |

## Proposed project model synthesis (not verbatim from either paper)
Decision variables: feasible per-vehicle charging schedule `u_{i,k}`, optionally charger-type selection `m_i` and actual control policy `π`. Random scenarios `ω` include base loading, ambient forcing, EV arrivals, required battery energy, departure deadlines, EV penetration and harmonic spectra conditioned on charge power/mode.

**Objective (single-criterion example):**
\[
\min_{\pi\ \mathrm{nonanticipative}} \mathbb E_\omega\left[\Delta t\sum_k F_{AA}(T_{H,k}(\omega))\right]
\]
subject to verified grid loading/voltage limits, thermal equations, charger restrictions, and EV energy-by-departure demands. Alternatively permit slack `U_i≥0` with explicit large penalty or Pareto-optimize aging vs unmet mobility energy instead of claiming all deadlines feasible.

**Electrical losses (candidate schematic form, equipment-specific):**
\[
P_{loss}(t)=P_{core}(t)+\sum_{h=1}^{H}R_{ac,h}(T)I_{h,rms}(t)^2+P_{other}(t).
\]
Avoid double counting winding, eddy and stray losses; source transformer harmonic loss equations and frequency response from original full text and equipment/standards. Define `THD_I=sqrt(sum_{h≥2}I_h²)/I_1` but do not assume THD alone uniquely determines harmonic losses, since spectral distribution and frequency-sensitive losses matter.

**Thermal state and consequence:** verified ODE/DAE or standard energy balances → observed/estimated winding HST → IEEE-style equivalent aging factor and life-consumption time. Introduce *temperature-driven allowable charging-power constraints* only when actual physical protection/rating/control relation is qualified; otherwise label as scenario control assumptions.

## Direct/indirect thesis relevance
- SO1: candidate charger harmonics / charging timing **T→P** mechanisms; no measured P→T interface proven.
- SO2: augment and compare existing stochastic electrothermal model with spectrum-dependent physical losses, while retaining simple benchmark and proper uncertainty.
- SO3: possible charging service trade-offs and transition timing under thermal constraints, but require observed controls and deadlines (or scenario-based rather than empirical claims).

## Benchmark gates
1. Extract original 2003 equations, hardware, experiment-vs-simulation conditions, program inputs/outputs, whether optimization algorithm truly existed, and harmonic measurements.
2. Define same scenarios and transformer/charger parameters for comparison to OPT-1; isolate incremental effect of harmonics (with/without), stochastic loading (deterministic/probabilistic), and charging schedules.
3. Compare aging-equivalent hours and HST RMSE only where independent measured HST exists; thermal-limit timing, unmet kWh, departure failures, computational cost, physical constraints and uncertainty.
4. Existing measured SINTEF transformer current/HST sensor archives **lack verified charger harmonic spectra and same-site EVSE mapping**; cannot assert empirical harmonics→thermal effect or causal P→T restriction from these files.
5. Evaluate whether OPT-2 adds decision quality beyond OPT-1. Condition full harmonic extension on data and thesis scope/time feasibility; do not automatically expand the canonical thesis to power-quality research.
6. Retain conditional PINN as separate **model-class benchmark**, not an optimization objective or measure of actual interdependency.

## Status
**OPT-2 = STRONG CANDIDATE METHOD FOR COMPARISON, NOT SELECTED FINAL.**  
Combined aging-aware optimization = **prospective mathematical derivation; established broad concept**, with novelty subject to recent prior-art falsification and experiment/validation.

Linked project evidence: `F1_CHARGING_TIME_OPTIMIZATION_DERIVATION_2026-11-05_V1.md`, `GOMEZ_MORCOS_2003_CHARGER_HARMONICS_PLANNING_TOOL_CANDIDATE_2026-11-05.md`, `STOCHASTIC_EV_TRANSFORMER_COUPLED_FORMULATION_CANDIDATE_F1_2026-11-05.md`.
