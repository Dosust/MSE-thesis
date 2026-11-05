# Candidate F1 — Stochastic EV-to-transformer thermal physics with candidate power-to-transport feedback

**Decision recorded:** 5 November 2026  
**Status:** STRONG CANDIDATE MATHEMATICAL FORMULATION — NOT FINAL, NOT CLAIMED NOVEL, NO SUPERVISOR APPROVAL, NOT VALIDATED.  
**Thesis:** Engineering of Power–Electrified Transportation Interdependencies for Resilience.  
**Scope:** Active extreme-heat thermal SO1–SO3, power ↔ electrified road transport.

## Basis in original peer-reviewed prior art
Qian, K., Zhou, C., Yuan, Y. (2015). *Impacts of high penetration level of fully electric vehicles charging loads on the thermal ageing of power transformers.* IJEPES 65, 102–112. DOI https://doi.org/10.1016/j.ijepes.2014.09.040.

**Existing prior art (NOT thesis novelty):** stochastic EV starting time, initial SOC and charging modes produce aggregate charging demand; a distribution transformer thermal model maps current/load and ambient conditions to top-oil, winding hot-spot temperature (HST), an IEEE-style accelerating aging factor and equivalent aging/life consumption. Source manuscript §II, §III, equations (4),(5),(7)–(10). Existing study used generic UK LV network and actual base load/ambient series with simulated vehicle charging profiles. Related analytic EV cluster-load derivation is attributed by this paper to earlier work (its refs [6], [24]); verify those originals before claiming or adopting their exact distribution.

**Scientific limitation:** This prior work already models T→P hot-spot/aging, so it is not novelty to repeat it. Its charging scenarios and field inputs do not by themselves verify measured, causal P→T thermal derating of an electrically mapped EVSE, nor mobility service loss/recovery. Check independent primary observations before claiming empirical coupled causality.

## Proposed candidate model (our research synthesis, NOT a formula copied from Qian)

### Random EV requirements and exogenous environment
Let \(\omega\in\Omega\) be a stochastic outcome. EV i has random arrival/plug-in time \(\tau_i(\omega)\), initial SOC \(s_{i,0}(\omega)\), charger mode \(m_i(\omega)\), charging need/travel demand \(d_i(\omega)\), departure deadline \(D_i(\omega)\), and physical battery energy capacity \(E_i\). Ambient \(T_a(t,\omega)\) and non-EV network base load \(P_b(t,\omega)\) may be stochastic and correlated. Specify joint law, independence assumptions, units and estimation evidence explicitly.

### Request for EV charging
\[
P_{EV}^{req}(t,\omega)=\sum_{i=1}^{N(\omega)}p_i^{req}(t;\tau_i,s_{i,0},m_i,d_i,\omega).
\]
The charging profiles must respect allowable charger power, arrival/departure, battery energy needs and tapering. Probability law for the total is derived from the **joint** input process, not from unwarranted independent vehicle assumptions.

### Electrical input and physical thermal states
\[
(P_{net},Q_{net})=(P_b+P_{EV}^{del},\ Q_b+Q_{EV}^{del}),\quad
I_{tr}=\mathcal{G}(P_{net},Q_{net},V,\text{topology}),
\]
where \(\mathcal{G}\) is a verified power-flow/equipment relation, not an assumed universal fixed power factor. An illustrative energy-conserving lumped thermal model is
\[
C_o\dot T_o = P_{loss,o}(I_{tr},T_o,T_H)-H_o(T_o,T_a;u_{cool}),\qquad
C_w\dot T_H = P_{loss,w}(I_{tr},T_H)-H_w(T_H,T_o).
\]
These are **candidate model structures only**, with unknown heat partitions, admissible cooling, physical parameters and sensor semantics needing verification. Do not assert identifiability merely from fit. A verified applicable standard dynamic rise model can replace these equations. Modeling true hot-spot maximum versus point sensor temperature must be distinguished.

### Thermal aging (adopted source law, equipment applicability to confirm)
\[
F_{AA}(t,\omega)=\exp\left(\frac{15000}{383}-\frac{15000}{T_H(t,\omega)+273}\right),
\quad L(\omega)=\int_0^{H}F_{AA}(t,\omega)\,dt.
\]
\(L\) is **equivalent aging time** over horizon H, not automatically percentage of physical transformer lifespan. Percentage consumed needs explicitly defined nominal-life reference. Source uses an IEEE-style reference relation and time-weighted aging factor; edition, transformer insulation and reference temperature require verification.

### Proposed P→T feedback layer (not established by Qian 2015)
\[
0\le p_i^{del}(t,\omega)\le p_i^{req}(t,\omega),\qquad
I_{tr}(t,\omega)\in\mathcal{I}_{feasible}(T_o,T_H,T_a,\text{ratings,protection}),
\]
\[
\dot s_i(t,\omega)=\frac{\eta_i(t,\omega)\,p_i^{del}(t,\omega)}{E_i},\qquad
U_i(\omega)=E_i\,[s_i^{target}-s_i(D_i,\omega)]_+ .
\]
\(U_i\) measures energy shortfall at departure in kWh where SOC is a fraction and E_i is kWh. Charging control, operating constraints and deadlines must be evidenced or labeled **scenario assumptions**; a thermal alarm alone is not a measured charger restriction.

### Candidate risk/resilience metrics
- T→P: \(\Delta\mathbb E[L]=\mathbb E[L\mid\text{EV demand scenario}]-\mathbb E[L\mid\text{baseline}]\), interpreted as a controlled scenario contrast rather than automatically causal observational effect.
- State accuracy: held-out HST MAE/RMSE [°C], peak and transition-time error.
- Threshold risk: \(\Pr(\max_{t\in[0,H]}T_H(t,\omega)>T_{lim})\), only with justified equipment-specific T_lim and scenarios.
- P→T: \(\mathbb E[\sum_i U_i]\) [kWh], charging restrictions [kW] and departures below charge target [%], only validated as observed if a connected site and control outcomes are available.
- Propagation: thermal-to-charging restriction delay and EV-load-to-hotspot response lag, with state/input perturbation control or qualified model-based response and uncertainty.

## Comparison program
1. **Historical reference:** reproduce the Qian charging-to-HST-to-aging chain where exact sources/parameters are recoverable; label approximate adaptations.
2. **Physics baselines:** appropriate IEC/IEEE engineering thermal model, simple thermal RC/ODE and, only if necessary, spatial PDE/FVM; numeric convergence and residual audits.
3. **Conditional PINN:** benchmark only if observed HST and physical/boundary residuals support fair training/testing; PINN is a **method**, not a metric or presumed winner.
4. **Proposed coupled system:** add **qualified** temperature-sensitive charging constraints and service equations. Full bidirectional field validation requires synchronous, physically mapped transformer+EVSE control/service data; otherwise model-based scenarios cannot establish field coupling.
5. **Evaluation:** same forcing, input availability, chronological train/calibration/test, no leakage, cost/runtime, uncertainty, extreme-heat out-of-range qualification, parameter identifiability; prespecify metrics and comparison.

## Qualification and next decisions
- Check exact primary Qian analytical charging-cluster predecessor sources, Eq. numbers and assumptions (25 kWh battery, historical charger powers, UK 2010 profiles; NOT universal modern hardware).
- Verify SINTEF HST channel locations/metrology before using as target; current 0.2147 °C RMSE was for TOP OIL, **not** HST. Ambient in recorded SINTEF dataset spans -19.58 to +25.97 °C; no extreme-heat field validation outside it.
- Establish empirical topology, site clocks, EVSE cooling/derating, control trace and demand deadlines before empirical SO3 claims.
- Maintain this as **F1 strong candidate** and compare with other physically justified models and candidate SO1–SO3 metrics after systematic evidence synthesis.
- This candidate does not amend approved review protocol v0.3 or canonical thesis objectives.

**Decision status:** Proposed as first strong stochastic physics-based engineering formulation candidate; formal model choice, novelty boundary, dataset sufficiency and supervisor approval remain OPEN.
