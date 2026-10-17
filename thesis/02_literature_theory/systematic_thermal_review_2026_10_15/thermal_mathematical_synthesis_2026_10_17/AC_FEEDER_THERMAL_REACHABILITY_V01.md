# AC feeder + three-state electrothermal constrained reachability — v0.1

**17 October 2026. Status:** Independently source-crosschecked AC *equations*, analytically derived reduced electrothermal/charging formulation, locally tested *synthetic* finite-scenario reachability. **NOT** a calibrated field feeder, official IEEE test-feeder numerical benchmark, current transformer-loading standards implementation, nor a proof of full robust viability or global novelty.

## 0. Primary scientific provenance

The published **MATPOWER AC network equations** establish \(\mathbf I_{\rm bus}=\mathbf Y_{\rm bus}\mathbf V\) and nodal complex-power balance through \(\mathrm{diag}(\mathbf V)\overline{\mathbf I}\). Source: https://matpower.app/manual/matpower/NetworkEquations.html ; AC power flow: https://matpower.app/manual/matpower/PowerFlow.html ; MATPOWER 8.1 User Manual: https://zenodo.org/records/15871661 . This work derives and numerically crosschecks a *two-bus special case*. A separate SciPy nonlinear complex-power root verifies the analytic closed-form solution for eight synthetic load cases. **MATPOWER software itself was NOT run.** Reference IEEE PES 13-node distribution feeder description: https://ewh.ieee.org/soc/pes/dsacom/testfeeders/testfeeders.pdf . **No IEEE-13 data, three-phase unbalanced model, or independent feeder benchmark loaded in v0.1.**

The three independently audited original component publications are Gong et al. 2015 DOI 10.1109/TSG.2014.2365452 (actual transformer oil/top-winding lab tests under DC-equivalent power, not a true measured hot spot or live matched EVSE); Kunlasing et al. 2022 DOI 10.1109/ECTI-CON54298.2022.9795360 (transformer oil PT100/CT monitoring and manually transmitted Zigbee-to-IEC61851 charger current commands, not measured automatically temperature-triggered control); and Krama et al. 2026 DOI 10.1016/j.ecmx.2026.101960 (measured field EVSE rectifier/AC/DC derating, no external upstream utility-transformer thermal data). Raw paired P/charger data remain absent; Susa 2005 and complete IEEE C57.91-2025/IEC 60076-7:2018 mathematics and nameplate thermal criteria remain unverified.

## 1. Complete symbols, mathematical roles and SI units

| Symbol | Precise meaning | Unit and role |
|---|---|---|
| \(t\), \(t_k=k\Delta\), \(\Delta\) | time, start of discrete power stage k, held-stage duration | seconds, independent variable/time grid |
| \(k,N\), \(\omega\in\Omega\) | interval index, number of intervals, weather/load complete-trajectory scenario | count; scenario index |
| \(V_s\) | source/sending-end LV phase-to-neutral complex voltage, chosen positive real as angular reference | V |
| \(V\), \(v=|V|^2\) | receiving-end phase complex voltage, squared magnitude | V, V² |
| \(I\) | per-phase feeder and transformer-secondary current, balanced radial model | A RMS phasor |
| \(R_f,X_f,Z_f=R_f+\mathrm jX_f\) | per-phase feeder resistance, reactance, series impedance | Ω |
| \(\mathrm j^2=-1\), \((\cdot)^*\) | imaginary unit; complex conjugation | operator |
| \(P_b,Q_b\) | *non-EV* receiving-end three-phase real/reactive consumption | W, var |
| \(p=P_{\rm DC}\), \(P_r\), \(\eta\) | delivered DC charging output; maximum DC power; whole-charger AC/DC efficiency | W, W, dimensionless 0<η≤1 |
| \(P_L=P_b+p/\eta\), \(Q_L=Q_b\) | downstream total three-phase real/reactive power consumed; charger reactive consumption assumed zero | W, var |
| \(P_\phi=P_L/3,Q_\phi=Q_L/3\), \(S_\phi=P_\phi+\mathrm jQ_\phi\) | balanced phase consumption | W, var, VA |
| \(R_{\rm tr}\) | referred **per-phase transformer winding resistance** for the same LV-side current | Ω |
| \(H_{\rm tr}=3R_{\rm tr}|I|^2\) | *transformer* winding copper heating | W |
| \(P_{\rm line,loss}=3R_f|I|^2\) | *feeder* resistance heating, excluded from transformer heat nodes | W |
| \(T_w,T_o,T_c\) | effective winding, oil, and charger rectifier/cabinet temperatures; \(x=(T_w,T_o,T_c)^\top\) | K, three dynamic states |
| \(C_w,C_o,C_c\) | thermal lump capacities | J/K |
| \(G_{wo},G_{oa},G_{ca}\) | winding/oil, oil/ambient and charger/ambient conductances | W/K |
| \(A_P,A_E\), \(Q_0,Q_{\rm ext}\) | two physically local ambient temperatures; core/other transformer heat and charger external heat | K, W |
| \(\alpha_c,\ell=\alpha_c(\eta^{-1}-1)\) | allocation fraction of total converter loss to measured effective charger node and implied heat per DC watt | dimensionless |
| \(D_o(T_o),D_c(T_c)\) | **assumed**, not empirically identified, temperature-conditioned allowable DC powers | W |
| \(V_{\min},I_{\max}\) | specified receiving-end voltage floor, per-phase current maximum | V, A |
| \(T_{w,\max},T_{o,\max},T_{c,\max}\) | specified upper limits *for the exact modeled states* (toy, not authentic hotspot/junction thresholds) | K |
| \(E_k,E_{\rm req},t_d\) | delivered cumulative DC-port energy, energy requirement, deadline | J, J, s |
| \(u_k\in\mathcal U\), \(\pi\) | chosen stage DC power, possible nonanticipative future feedback policy | W, state/observation-dependent rule |
| \(\mathcal F_\Delta,\Phi=e^{A\Delta}\) | held-stage exact thermal transition, linear state transition matrix | K-state map; dimensionless |
| \(K_{\rm safe},\mathcal R_{t_d},\mathcal V_k\) | constraint set, reach-avoid initial set, backward feasible sets | sets |
| \(\mathcal W,\mathcal W_k\) | possible full disturbance histories and stage disturbance bounds | scenario sets |

**State semantics:** The winding state is **not measured true hottest spot** in Gong. Charger rectifier proxy is **not semiconductor junction** in Krama. A temperature observation requires sensor/location/calibration map, not identity by assertion. Temperature *differences* and derivatives can be numerically represented in °C for this model; absolute-temperature ageing must use K.

## 2. Derive the two-bus AC algebraic law

Assume a balanced three-phase series feeder with fixed source phase RMS voltage \(V_s\), phase series \(Z_f\), one downstream constant-power consumer. With the load **consumption sign positive**:
\[
\boxed{V_s=V+Z_fI,\qquad S_\phi=P_\phi+\mathrm jQ_\phi=VI^*.}\tag{AC1}
\]
\[
P_L=P_b+\frac{p}{\eta},\quad Q_L=Q_b,\quad P_\phi=P_L/3,\quad Q_\phi=Q_L/3.\tag{AC2}
\]
From \(I=S_\phi^*/V^*\), multiplying the KVL identity by \(V^*\) yields \(V_sV^*=|V|^2+Z_fS_\phi^*\). Writing \(v=|V|^2\) and taking squared magnitudes gives the **exact balance algebra for this two-bus model**:
\[
\boxed{
v^2+\bigl[2(R_fP_\phi+X_fQ_\phi)-|V_s|^2\bigr]v
+(R_f^2+X_f^2)(P_\phi^2+Q_\phi^2)=0.}\tag{AC3}
\]
Define \(B=|V_s|^2-2(R_fP_\phi+X_fQ_\phi)\) [V²] and discriminant \(\mathfrak D=B^2-4(R_f^2+X_f^2)(P_\phi^2+Q_\phi^2)\) [V⁴]. With positive real reference \(V_s\):
\[
\boxed{v_+=\frac{B+\sqrt{\mathfrak D}}2,\quad
V=\frac{v_++Z_f^* S_\phi}{V_s},\quad
I=\left(\frac{S_\phi}{V}\right)^*.}\tag{AC4}
\]
A high-voltage branch is considered only if \(B>0,\mathfrak D\ge0,v_+>0\). This is an **algebraic existence test, not sufficient operational security**; the current and voltage limits and branch regularity must also be enforced. At the fold, branches merge and Jacobian invertibility fails.

Line electrical loss and upstream source injection satisfy:
\[
\boxed{P_{\rm send}=P_L+3R_f|I|^2,\qquad
Q_{\rm send}=Q_L+3X_f|I|^2.}\tag{AC5}
\]
**Critical energy accounting:** \(3R_f|I|^2\) is heat in feeder lines and **must not** be added to transformer winding temperature. Transformer winding loss uses separate \(R_{\rm tr}\) and the physically same LV current. The model does **not** solve the transformer internal source impedance/tap contribution to bus voltage, so it is not yet a realistic multibus substation distribution model.

## 3. Couple AC current to the distinct three effective thermal states

For held power and weather on stage k:
\[
\boxed{\begin{aligned}
C_w\dot T_w&=3R_{\rm tr}|I_k|^2-G_{wo}(T_w-T_o),\\
C_o\dot T_o&=Q_0+G_{wo}(T_w-T_o)-G_{oa}(T_o-A_{P,k}),\\
C_c\dot T_c&=Q_{\rm ext}+\alpha_c(u_k/\eta-u_k)-G_{ca}(T_c-A_{E,k}).
\end{aligned}}\tag{TH1}
\]
Each term in TH1 has W units: capacitance × temperature time derivative, a source term, or a thermal conductance × temperature difference. Winding-to-oil heat cancels when summing the transformer nodes. There is **no speculative direct transformer↔charger thermal conductance**; the physical coupling is via AC electrical loading and allowed power/control.

For fixed \(I_k,A_{P,k},A_{E,k},u_k\) within stage k, let \(x=(T_w,T_o,T_c)^\top\), \(A\) be the constant matrix
\[
A=\begin{pmatrix}
-G_{wo}/C_w&G_{wo}/C_w&0\\
G_{wo}/C_o&-(G_{wo}+G_{oa})/C_o&0\\
0&0&-G_{ca}/C_c
\end{pmatrix},\tag{TH2}
\]
and define
\[
b_k=\begin{pmatrix}
3R_{\rm tr}|I_k|^2/C_w\\
(Q_0+G_{oa}A_{P,k})/C_o\\
(Q_{\rm ext}+\alpha_c(u_k/\eta-u_k)+G_{ca}A_{E,k})/C_c
\end{pmatrix}.
\]
The physical model reduces within each stage to \(\dot x=Ax+b_k\). Since \(A\) is Hurwitz and invertible for positive capacitances/conductances, the thermal flow is **exact** under held input:
\[
\boxed{x_{k+1}=x_k^{eq}+e^{A\Delta}(x_k-x_k^{eq}),\qquad x_k^{eq}=-A^{-1}b_k.}\tag{TH3}
\]
This avoids an uncontrolled forward-Euler discretization error in the three thermal states; numerical matrix exponential remains subject to floating-point tolerance. Within-stage transformer temperatures may have an interior maximum, so the implementation tests stage endpoints and the derivative stationary point where one exists; the charger single thermal compartment is monotone under fixed inputs.

## 4. Simultaneous safe operation and deadline service

For each time t and actual valid power-flow branch:
\[
\boxed{\begin{aligned}
|V(t)|&\ge V_{\min},\qquad |I(t)|\le I_{\max},\\
T_w(t)&\le T_{w,\max},\qquad T_o(t)\le T_{o,\max},\qquad T_c(t)\le T_{c,\max},\\
0\le p(t)&\le \min\{P_r,D_o(T_o(t)),D_c(T_c(t))\}.
\end{aligned}}\tag{SAFE}
\]
**Evidence limit:** every voltage, current and temperature numerical threshold in the companion demonstration is *invented and labeled toy*. True transformer winding hotspot, semiconductor junction, insulation-ageing and protective current limits require actual equipment/source certification. \(D_o\) remains a HYPOTHETICAL power restriction, not an automatic oil-control finding in Kunlasing (2022). EVSE current and manufacturer DC protocol constraints must be mapped correctly.

Charging output energy is defined at the DC port:
\[
\boxed{\dot E_{\rm DC}(t)=p(t)\ \mathrm{W},\quad
E_{\rm DC}(t_d)=\int_0^{t_d}p(t)\,dt\ge E_{\rm req}\ \mathrm{J}.}\tag{SERV}
\]
This is **not** battery-stored energy, SoC, proven mobility trip success or failure. The toy assumes vehicle acceptance is large enough that delivered power equals commanded output for the full stage; actual BMS taper/state and charging arrivals are not modeled.

## 5. Reachability: target, rigorous quantifiers and computed surrogate

**General mathematical robust reach-avoid target** for a nonanticipative policy \(\pi\):
\[
\boxed{\mathcal R_{t_d}=\{(x_0,E_0,q_0):
\exists\pi\ \forall w\in\mathcal W,\
(x^\pi(t),z^\pi(t),q^\pi(t))\in K_{\rm safe}\;\forall t\in[0,t_d],\
E^\pi(t_d)\ge E_{\rm req}\}.}\tag{R1}
\]
Here \(z\) is algebraic AC state, q control/device mode, w disturbance trajectory and \(K_{\rm safe}\) contains electrical, thermal and protocol constraints. **Not computed as a full robust kernel.**

Under independent rectangular stagewise uncertainty and fully observed states, an ideal backward recurrence would be
\[
\boxed{\begin{aligned}
\mathcal V_N&=\{(x,E): E\ge E_{\rm req},\text{ terminal safety}\},\\
\mathcal V_k&=\{(x,E):
\exists u\in\mathcal U\ \forall w\in\mathcal W_k,\
\mathrm{StageSafe}(x,u,w)\land
(\mathcal F_\Delta(x,u,w),E+\Delta u)\in\mathcal V_{k+1}\}.
\end{aligned}}\tag{R2}
\]
Mode, actuator acknowledgement and observations/delays must be included in augmented state for actual partial-observation nonanticipative policies. Whole-trajectory correlated weather scenarios are *not automatically* independent stagewise uncertainty.

**The script instead computes a genuinely narrower finite-scenario open-loop feasibility decision:**
\[
\boxed{\exists(u_0,\ldots,u_{N-1})\in\mathcal U^N\
\forall\omega\in\Omega_{\rm finite}:
\mathrm{StageSafe}_{\omega,k}\ \forall k,\quad
\Delta\sum_k u_k\ge E_{\rm req}.}\tag{R3}
\]
The **same** open-loop power schedule must work for every enumerated scenario. Thus an affirmative result constructs one trajectory-safe schedule for *those discrete disturbance trajectories*, not for every continuous extreme-heat profile or real utility site. Checking the exact thermal held-stage flow and AC balance is valuable computational evidence only within the simplified model.

## 6. Entirely hypothetical reproducible calculation

### Toy equipment and constraints

| Parameter | Value | Unit / meaning |
|---|---:|---|
| \(V_s,R_f,X_f\) | 230,0.15,0.08 | phase RMS V, Ω, Ω |
| \(R_{\rm tr},\eta,P_r\) | 0.025,0.94,12000 | Ω, 1, DC W |
| \(C_w,C_o,C_c\) | 200000,600000,50000 | J/K |
| \(G_{wo},G_{oa},G_{ca}\) | 80,18,22 | W/K |
| \(Q_0,Q_{\rm ext},\alpha_c\) | 130,0,0.70 | W,W,unitless |
| Allowed effective state maxima | 76,72,78 | °C for winding, oil, charger **toy** |
| Voltage floor and RMS current ceiling | 213,49 | phase V, A **toy** |
| Temperature-limit start points and slopes | 65°C oil and charger; 500 and 350 W/K | HYPOTHETICAL derating |
| Initial \(T_w,T_o,T_c\) | 51,50,55 | °C |
| \(N,\Delta,\mathcal U\) | 6,1200,{0,4000,8000,12000} | count, s, W |
| \(t_d,E_{\rm req}\) | 7200,17 | s, kWh DC port |

### Two specified assumed complete disturbance scenarios

| Scenario | Transformer ambient | Charger ambient | Other three-phase P | Other Q |
|---|---:|---:|---:|---:|
| Warm | 35°C | 39°C | 9000 W | 1800 var |
| Extreme | 53°C | 55°C | 12000 W | 2500 var |

**Verified local results:** Source-equation KVL and 3-phase active/reactive power residuals and a separate SciPy nonlinear solver agree for eight synthetic loading configurations. A synthetic one-phase voltage-fold counterexample is correctly rejected for demand beyond its algebraic branch existence. Exhaustive 4^6=4096 schedule enumeration, with both listed full scenarios, finds exactly **one** schedule delivering \(\ge17\) kWh while meeting *all* toy stage and continuous-intra-stage constraints:
\[
\boxed{(12,8,8,8,8,8)\ \mathrm{kW},\qquad E_{\rm DC}(2\,h)=17.333333\ \mathrm{kWh}.}
\]
**Peak effective thermal states:** warm \(T_w=51.000°C,T_o=50.000°C,T_c=58.434°C\); extreme \(T_w=52.539°C,T_o=52.329°C,T_c=70.802°C\), including initial states. A 25-kWh demand is impossible under this 12-kW-for-2h rating because the global energy upper bound is 24 kWh even without other restrictions.

These numbers **cannot** be used as field predictions, hardware limits, charger derating thresholds, real trip-energy obligations, or confidence intervals. "Exactly one schedule" is a property of arbitrary numerical caps, grid and two stipulated scenarios, not a robust system design performance claim.

## 7. Mathematical and experimental next gates

1. **Independent official feeder benchmark:** read original IEEE PES 13-node data and actually run independently implemented three-phase equations against a trusted published/solver reference; compare per-phase V/I/P/Q/loss. Not completed here.
2. **General electrical plant:** actual source/transformer equivalent circuit and tap state, unbalanced LV phases/neutral, network voltage-drop and component-specific current/protection limits; physically observed EVSE reactive and harmonic effects, AC/DC efficiencies, charger BMS limits.
3. **Source-based thermal physics:** inspect original Susa 2005 and current IEEE C57.91-2025/IEC 60076-7:2018 full equations before citing standard-specific thresholds; identify true hotspot vs winding-surface/oil sensor mappings.
4. **Delay/hybrid integration:** integrate prior PR #100 delayed commands and hysteresis plus faults into algebraic-feasible trajectories; specify sample/communication time, control authority, feasibility loss modes, and guard priority. This calculation assumes piecewise-constant power and instantaneous admitted commands.
5. **Robust set:** replace just two full trajectories by justified bounded uncertainty families, calibrated intervals and nonanticipative observation-limited policies; compute certified lower/upper reachable sets with numerical error control.
6. **Original raw measurements:** Krama 1-minute AC/DC and 5-minute rectifier rows still unreceived; require paired utility transformer current/hotspot or measured proxy, charger AC/DC/rectifier/ambient, independent background P/Q/voltage and intervention/control logs. Only with such data can cross-domain causal thermal performance and real service validation be claimed.
7. **Research integrity:** compare against simpler AC+thermal coupling, published dynamic rating and EV charging co-simulation, with identical evidence budget; formal novelty still bounded by unreviewed originals and global searches.

**Conclusion:** A power-flow-equation-grounded electrothermal constraint/reachability prototype exists; its finite scenario result is proved/checked **within assumed mathematics**, while source-specific physical calibration, externally validated grid and full robust viability remain **open**.
