# Coupled Power–Electrified Transportation electrothermal model, version 0 (PROPOSED—not validated)

**Research boundary:** Extreme-heat-driven changes in utility distribution-transformer (P) and grid-connected EV charging equipment (T_e), their electrical exchange and feedback, state-dependent operational restriction, and charging/electricity service over time. **Not** an assumed direct conductive heat-transfer path from geographically separate charger enclosure to transformer. This v0 is a mathematically derived **candidate system**. It has **no identified site parameters, joint fit, or cross-infrastructure validation**. Scientific claim status below is mandatory.

**Evidence anchor:** Gong et al. (2015), IEEE TSG 6(2):648–656, DOI 10.1109/TSG.2014.2365452 (original 9p); Kunlasing et al. (2022), ECTI-CON, DOI 10.1109/ECTI-CON54298.2022.9795360 (original 4p); Krama et al. (2026), ECM:X 31:101960 DOI 10.1016/j.ecmx.2026.101960 (original 16p, prior separately checked). Susa et al. (2005) bibliographic/abstract access only; IEEE C57.91-2025 and IEC 60076-7:2018 official **scope** verified, full numbered normative equations NOT yet inspected. Refer to source-by-source matrix. These original papers are not alleged to contain the derived equations below.

## 0. Semantic and physical architecture

Physical equipment: P = upstream mineral-oil distribution transformer and low-voltage distribution circuit; T_e = electric charging equipment and its connected vehicle/battery. Supporting I = observed measurements, communications, available control; O = operator/dispatch and recovery resources only if represented by explicit constraints; neither is treated as a physical energy-bearing layer unless its own energy dynamics are modeled.

Directed and typed interfaces:
1. **T_e -> P (electrical demand):** charger's AC active/reactive/harmonic input contributes to transformer secondary electrical load, current and thermal losses. This is NOT heat conducted between enclosures.
2. **P -> T_e (electrical supply/constraint):** available grid voltage/current/thermal operating restriction bounds charger's permissible input/charging capability, possibly through metering/ICT/operator command. Gong studies heat-aware schedules; Kunlasing physically tests manually commanded load-based PWM; neither is a direct experimental same-site P-hotspot-to-EVSE thermal receiving trace.
3. **T_e thermal state -> P (electrical feedback):** ambient/rectifier heating can trigger charger offered-power derating (Krama component evidence); ensuing changed AC input may modify transformer loading/temperature after an electrical exchange. This *cross-domain consequence* has not been measured jointly in these papers; sign depends on other demand and delayed recovery/rebound.
4. **Shared climate forcing:** T_a,P(x_P,t), T_a,E(x_E,t) may be correlated, but shared hot weather affecting both units is not directional P->E causality. Treat measurement sites independently where distinct.

No structural/causal edge enters a real case without an explicit component mapping, carrier, sensor/actuator location, orientation and provenance.

## 1. Variables and SI dimensions

- t [s], temperatures T_o (transformer top-oil proxy), T_w (winding thermal state), T_c (charger rectifier/cabinet proxy), T_a,P and T_a,E [K; measured °C may be translated to K; differences have same magnitude].
- **True winding hot-spot** T_H [K] is distinct from Gong's measured top-winding needle T_w,top [K]; T_w in equations is **effective winding state**, not automatically the HST. Mapping T_H=H(T_o,T_w,I,theta_H) is **unidentified** unless justified by fibre-optic calibration/accepted loading guidance. No raw hotspot measurement assumed.
- C_o,C_w,C_c [J K^-1], thermal conductances G_wo,G_oa,G_ca [W K^-1] with G>0 (equivalently R_th=1/G [K W^-1]).
- P_cu,P_core,P_stray,P_AC,P_DC,L_evse,P_base,Q_load [W or var as labeled]; net harmonics I_h [A RMS] and measured fundamental current I_1 [A RMS].
- V_LL [V RMS], Q_sec [var], \eta_b dimensionless, E_DC, E_req [J], T_depart [s], SOC in [0,1].
- Physical/control modes q_P in {normal,restricted,out}, q_E in {rated,derated,off}, q_I in {communicating,unavailable}; these are **candidate engineering abstractions**, not observed mode labels in the source experiments.
- theta = uncertain physical and device parameters, W(t) = admissible climate/load/sensing disturbances, u(t)= available actuation including curtailment/dispatch within an explicit device protocol.

## 2. First-principles candidate thermal energy balances (SI: W = J/s)

Use lumped nodes at the scale justified by observed response. Allocate transformer's electromagnetic losses to winding and oil control volumes consistently:

(PT-1)
\[
C_w(T_w)\,\dot T_w =
P_{\rm cu}(I_{\rm rms},T_w)+P_{{\rm stray},w}(I_h,T_w)
-G_{wo}(T_w,T_o)(T_w-T_o).
\]

(PT-2)
\[
C_o(T_o)\,\dot T_o =
P_{\rm core}(V,f,T_o)+P_{{\rm stray},o}(I_h,T_o)
+G_{wo}(T_w,T_o)(T_w-T_o)
-G_{oa}(T_o,T_{a,P},m_P)(T_o-T_{a,P}).
\]

Physical assumptions at v0: oil and winding states are locally well-mixed *effective* thermal compartments, and all heat-generation terms are appropriately allocated **once**; temperature-dependent cooling, fan modes, solar/ambient forcing and core losses can be refined when equipment specifications/data justify them. The measured top-oil location may not exactly equal the oil lump's volume-average temperature: observation model must retain sensor-location mapping. When C depends strongly on temperature the internal-energy derivative is dU(T)/dt=C(T)\dot T with C=dU/dT; energy balance is still of this form.

Illustrative winding resistance constitutive prior (Gong Eq.11):
\[
R_w(T_w) = R_{w,0}[1+\beta(T_w-T_0)],\qquad
P_{\rm cu}\simeq 3 I_{1,\rm phase}^2 R_{\rm winding,eq}(T_w).
\]
Here R must be defined on the correct three-phase/per-phase and transformer side. For unbalance, use \(\sum_{\phi} I_\phi^2 R_{\phi}\); a single phase-average relation is **not** generally valid. Harmonic/surface/stray heating requires frequencies and manufacturer information, not THD alone; do not multiply source THD directly into an uncalibrated thermal-loss law.

**Transformer stored-energy check:** Add PT-1 and PT-2:
\[
\frac{d}{dt}(U_w+U_o)=P_{\rm cu}+P_{\rm core}+P_{\rm stray,w}+P_{\rm stray,o}-G_{oa}(T_o-T_{a,P}).
\]
The internal exchange \(G_{wo}(T_w-T_o)\) cancels identically. An implementation failing this cancellation double-counts or loses heat.

**Charger effective rectifier/cabinet thermal compartment:** Krama measures mean external rectifier-module sensors, NOT semiconductor junction; charger inlet minus outlet is total electric-conversion/auxiliary loss, NOT specific junction dissipation. Model:
(PT-3)
\[
C_c(T_c)\dot T_c =
\alpha_c(t)\big(P_{\rm AC}(t)-P_{\rm DC}(t)\big)
+Q_{\rm external,c}(t)
-G_{ca}(T_c,T_{a,E},m_E)(T_c-T_{a,E}),
\]
where \(0\le\alpha_c\le1\) is only an effective loss-allocation fraction **under the chosen energy accounting**. \(Q_{\rm external,c}\) [W] can include solar/environmental heating if separately measured or scenario-assumed. Actual thermocouple-average rectifier temperature must be linked by an observation operator to the effective state; neither equality nor alpha is experimentally identified by the three sources. A realistic multi-compartment charger may require module, case and enclosure nodes; do not introduce unidentified junction-temperature state as if observed.

**No direct transformer↔charger conductive term:** Terms \(G_{Pc}(T_P-T_c)\) have no evidence here. Thermal cross-system influence exists indirectly via AC electrical loading, control constraints, and climate.

## 3. Electrical algebraic exchange (consistent side/accounting)

Let \(P_{\rm sec}=P_{\rm base}+\sum_{j=1}^{N_c}P_{{\rm AC},j}\) be **real power delivered on transformer's LV secondary**, measured at a defined connection boundary. The transformer primary power equals \(P_{\rm sec}+P_{\rm tr,loss}\) under quasi-steady energy accounting; transformer internal losses in PT-1/2 are NOT added again to \(P_{\rm sec}\).

For an approximately balanced three-phase secondary at fundamental frequency:
(PT-4)
\[
S_{\rm sec}=\sqrt{P_{\rm sec}^2+Q_{\rm sec}^2},\quad
I_{1,\rm eq}\approx \frac{S_{\rm sec}}{\sqrt{3}V_{LL}}.
\]
If harmonics/non-sinusoidal power are significant, compute RMS per phase and harmonic losses consistently; \(I_{\rm rms}^2=\sum_h I_h^2\) can hold for resolved orthogonal Fourier harmonics in a stationary window, but loss multipliers need spectra/geometry. If feeder voltage drop or unbalance matters, replace PT-4 by a properly parameterized three-phase power-flow DAE \(0=\mathcal F_{\rm PF}(V,\vartheta,P,Q;\mathcal G_P)\).

For every charger at its explicit AC inlet/DC output boundary:
(PT-5)
\[
P_{{\rm AC},j}=P_{{\rm DC},j}+L_j(P_{{\rm AC},j},T_{c,j},m_{E,j}),
\quad P_{\rm AC,j}\ge P_{\rm DC,j}\ge0.
\]
The **offered** DC capability \(P_{\rm off,j}\) is not the **delivered** DC power \(P_{\rm DC,j}\). Charger and vehicle/BMS limits are separate:
(PT-6)
\[
0\le P_{\rm DC,j}\le
\min\left[
D_j(T_{c,j},q_{E,j};\theta_{D,j}),\,
B_j(SOC_j,T_{b,j};\theta_{B,j}),\,
U_j(u_j,q_I),\,
G_j^{\rm electric}(V,I_{\rm cap,P},\ldots)
\right].
\]
Each term has W units and must be an actual DC-equivalent bound at the defined interface; if grid limit is measured in AC W/A, conversion through PT-5 and voltage/power factor is required. The empirical \(D_j\) function is a candidate derating envelope, NOT a globally valid thermal rule derived from Krama's temperature polynomial. It may depend on fan mode, charger firmware and history/hysteresis. **Do not** apply Kunlasing's IEC 61851 AC-control-pilot PWM law as the same physical actuator on Krama's CCS2 DC charger: they are different equipment/control interfaces and require distinct device-specific command maps.

For the charger-side energy service boundary (DC energy delivered to the EV port, not battery stored energy):
(PT-7)
\[
\dot E_{{\rm DC},j}=P_{{\rm DC},j},\qquad E_{{\rm DC},j}(0)=0.
\]
For **battery stored** energy separately:
\[
\dot E_{{\rm batt},j}=\eta_{b,j}(SOC,T_b,P_{\rm DC})P_{{\rm DC},j},
\]
only if battery-side losses/states have evidence; no invented BMS or journey physics.

## 4. Explicit directional interface, feedback and causal scope

T_e -> P: given P_AC from PT-5, electrical balance PT-4 changes I, producing winding Joule heat PT-1 and oil-temperature dynamics PT-2. Gong supports P temperature response to imposed EV-like scheduling, but the laboratory experiment does not measure operating EVSE AC/DC and transformer heat as one field pair.

P -> T_e: upstream transformer load/temp/rating and information/organization enable admissible active power \(U_j\) in PT-6. Kunlasing directly demonstrates **manual** Zigbee command -> charger PWM current-limit modification, **not** oil-temperature-triggered closed-loop control. Gong models heat/life-aware charging schedules; RACE (2025) already simulates hotspot-threshold charging restriction. Any novel threshold-control proposal must exceed this prior art.

T_e heat -> P feedback: Krama directly demonstrates heat-conditioned offered/delivered charger power in one field EVSE; its effect on the upstream transformer through PT-5/PT-4/PT-1/PT-2 remains **calculated/hypothesized absent paired P measurements**. A lower offered power can decrease contemporaneous transformer current, but deferred charging/rebound, other load and PF/harmonics can reverse/complicate the net effect. No monotonic cross-system temperature theorem follows simply from Krama.

Time delays: observation sample/communications/controller delay \(\tau_I\) [s] and physical thermal lags from PT-1–3 are different. A five-minute T_c sensor measurement does not establish one-minute physical crossing time. Any inferred causal delay must propagate actual clock-sync error, discrete measurement support, control logs and model uncertainty.

## 5. Hybrid differential-algebraic system (state + event dynamics)

\[
x(t)=(T_o,T_w,T_c,E_{\rm DC},SOC_{\rm observed?},\ldots),\
z(t)=(P_{\rm AC},P_{\rm DC},V,I,\ldots),\
q(t)=(q_P,q_E,q_I).
\]

(PT-8)
\[
\begin{cases}
\dot x=F_q(x,z,u,w;\theta),\\
0=G_q(x,z,u,w;\theta),\\
y_k=\mathcal H_k(x(t_k),z(t_k),q(t_k);\theta_H)+\varepsilon_k,\\
q(t^+)=\mathcal J(q(t^-),x(t^-),y_{\le t},u(t);g),\quad
x(t^+)=R_q(x(t^-))\ \text{only if physical state reset is justified}.
\end{cases}
\]

Default protective switching changes allowable power/control modes while thermal states remain **continuous** across the switch (no arbitrary instant temperature resets). Example **hypothetical** transformer thermal threshold (NOT measured Kunlasing control):
\(q_P:\mathrm{normal}\to\mathrm{restricted}\) if \(T_{\rm protective}\ge T_{\rm on}\),
and reverse only if \(T_{\rm protective}\le T_{\rm off}<T_{\rm on}\).
Minimum dwell time/actuation delay is needed to prevent rapid chatter or Zeno-like numerical pathologies where appropriate. Keep Kunlasing's reported *electrical load lower than 80%* release rule distinct from such thermal guards.

Observation \(\mathcal H_k\) must specify sensor location, observable proxy, sample integration window and clock. For Krama: T_rect sampled every 5 min; AC/DC offered/delivered and SOC every 1 min. Gong: true hotspot absent; Kunlasing: oil/PT100 measured, raw cross-sensor timestamps not publicly received.

Define measured versus latent clearly: \(y_{oil}\) may be oil thermocouple or PT100, \(y_{w,top}\) is not HST, \(y_{rect}\) is module-sensor average and not junction T_j. Never label \(\hat T_H\) observed.

## 6. Units, positivity, mathematical well-posedness and identifiable structure

**Dimensions:** each thermal LHS \(C_i\dot T_i\) has (J/K)(K/s)=W; G_i(T_i-T_j) has W; electrical P,W and Q,var must not be added as scalars; harmonic THD is dimensionless; E_DC [J] integrates P_DC [W] in seconds; divide by 3.6e6 for kWh. Numerical arrays may be in °C for *differences* but absolute Arrhenius ageing temperature requires Kelvin.

**Energy noncreation:** \(\sum U_i\) for two transformer nodes cancels internal exchange exactly; charger delivered + conversion loss = AC input at the chosen boundary, subject to modeled internal energy-storage accounting. If model uses loss \(P_{\rm AC}-P_{\rm DC}\) as heat and also separately adds all converter losses, it double counts.

**State non-negativity/bounds:** for \(C_i>0,G_{ij}\ge0,Q_{{\rm gen},i}\ge0\), and fixed \(T_a\ge T_{\min}\), the positive heat-network model has inward-pointing derivatives at lower temperature bound \(T_i=T_{\min}\), provided neighboring node temps \(\ge T_{\min}\). This gives a basic invariant lower-temperature domain under specified inputs, **not** a safety or resilience guarantee. E_DC is nondecreasing if \(P_{\rm DC}\ge0\), and must be capped by valid charging window/termination logic. Upper temperature safety is not automatic: enforced constraints/control and feasibility proof are needed.

**Local ODE/DAE solvability assumptions:** C_i bounded positive, constitutive F locally Lipschitz within each mode, algebraic Jacobian \(\partial G_q/\partial z\) nonsingular on the relevant operating branch (index-1 DAE), specified switching guards/dwell rules, and measurable locally bounded exogenous/control inputs. Device switching may introduce non-unique behavior at competing simultaneous guards; event priority must be specified. Do **not** claim global uniqueness/convergence/viability without additional hypotheses.

**Structural identifiability example:** for \(C_c\dot T_c=\alpha L(t)-G(T_c-T_a)\) with only T_c, T_a, and measured total L but unknown \(\alpha,C_c,G\), observations can at best recover \(\alpha/C_c\) and \(G/C_c\) in ideal excitation; jointly scaling \((C_c,\alpha,G)\) leaves \(\dot T_c\) unchanged. Independent heat-allocation, capacitance, cooling or direct heat-flux measurements are necessary to break this invariance. A Krama polynomial predicting P_off is **not** an experimental estimate of \((C_c,G,\alpha)\). Rich input excitation, independent tests and observability rank checks are mandatory before parameter fitting.

## 7. Service viability and reachability (not yet an established theorem)

Thermal/current/electrical safety domain:
\[
K_{\rm safe}=\{x,z,q: T_{\rm equipment}\le T_{\max}\text{ where measurable/defensible};\
I_\phi\le I_\phi^{\max};\ V_{\min}\le |V|\le V_{\max};\
\text{device and communication control constraints valid}\}.
\]
\(T_{\max},I_{\max}\) are equipment-specific nameplate/protection/authorized standards values. No generic threshold from Krama's observed ~55°C rectifier derating or Gong's simulated HST may be substituted for P equipment rating.

**Terminal service obligation** for actual critical charging:
\[
E_{\rm DC,j}(t_{\rm depart,j})\ge E_{\rm req,j}
\]
where both deadline and energy required must be provided externally by real service specification; Gong's departure SoC metric is a simulation proxy, and Krama's charging duration is not a measured trip requirement. A corresponding electricity-service floor can be included for other essential LV loads.

**Robust reach-avoid feasibility** over horizon H under hazard class \(\mathcal W\) (a proposed formal target):
\[
\mathcal R_H=
\{x_0:\exists\pi\in\Pi_{\rm nonanticipative},\ \forall w\in\mathcal W:
 (x^\pi(t),z^\pi(t),q^\pi(t))\in K_{\rm safe}\ \forall t\in[0,H],
\ E_{\rm DC,j}(t_{\rm depart,j})\ge E_{\rm req,j}\ \forall j\}.
\]
This is **not** ordinary invariant viability if service needs a terminal deadline. For disturbances causing unmet transient service, define separate recovery/target set \(K_{\rm recover}\) and a reach-avoid policy with quantified deprivation instead of artificially requiring uninterrupted full service throughout.

When uncertainty is probabilistic rather than set bounded, use chance constraints with a **verified distribution** and confidence, not an invented posterior. Novel contributions must be demonstrated against static coupling and independent component baselines; robust set computations can be approximate with certified discretization error when possible.

## 8. Falsifiable predictions and mathematical verification experiments

H1: With measured load and ambient fixed, an exogenous EVSE AC-current reduction leads to reduced transformer winding heat-generation term; whether measurable T_o or T_w reduction follows depends on heat capacity, cooling and interventions. Test causal response with actual input perturbation and controls.
H2: Measured EVSE temperature changes conditional offered charging capability within its observed validity range; site/device extrapolation must be held out.
H3: Full dynamic coupling may alter recoverable initial-condition region relative to static/decoupled assumptions, under specified safety + service constraints. This is a **to-be-tested hypothesis**, not a novelty conclusion.
H4: Monitoring/control unavailability can change attainable service trajectories; this depends on a documented control architecture and cannot be inferred from two manual charger demonstrations.

Counterfactual ablations must keep hazard realization, electrical loads, resources, timing and control authority matched; static versus dynamic must have the same parameter/observation budget wherever possible.

## 9. Do NOT conclude

- The three papers experimentally demonstrate matched utility-transformer→EVSE or EVSE→utility-transformer **thermal** causal propagation.
- Kunlasing oil temperature automatically triggers its charging curtailment (it measured oil, while manual commands physically tested).
- Gong laboratory top-winding probe measures true winding hottest spot.
- Krama's EVSE-internal “Transformer” in Fig. 4 is an upstream utility P transformer, or its field polynomial is a physics ODE/PINN.
- Transformer heating always rises under extreme heat independent of changed load/control and cooling.
- Existing transformer-aware thermal charging optimization is novel merely for using a temperature limit.
- A mobility trip failure can be concluded from a longer EV charging session alone.
- The IEEE C57.91-2025 or IEC 60076-7:2018 *complete equation sets* have been verified from publisher scope pages.

**State of artifact:** Mathematically formulated v0 with explicit assumptions and falsification targets; no source-validated cross-infrastructure parameterization, no empirical joint model fitting, and no formal theorem proven.


## 10. Analytically proved special-case thermal stability (PROPOSITION)

**Proposition.** Under a fixed ambient temperature \(T_a\), positive constant capacitances \(C_o,C_w>0\), positive constant conductances \(G_{wo},G_{oa}>0\), no internal heat-generation inputs, and no mode switching, the equilibrium of the two-node transformer thermal system is \(T_o=T_w=T_a\), and it is globally asymptotically stable within the unconstrained linear state space.

**Proof.** Write \(\theta_o=T_o-T_a\), \(\theta_w=T_w-T_a\). Then
\[
C_w\dot\theta_w=-G_{wo}(\theta_w-\theta_o),\quad
C_o\dot\theta_o=G_{wo}(\theta_w-\theta_o)-G_{oa}\theta_o.
\]
For \(V(\theta_o,\theta_w)=\frac12 C_o\theta_o^2+\frac12 C_w\theta_w^2\),
\[
\dot V=\theta_o C_o\dot\theta_o+\theta_w C_w\dot\theta_w
=-G_{wo}(\theta_w-\theta_o)^2-G_{oa}\theta_o^2.
\]
Both terms are nonpositive. Equality requires \(\theta_o=0\) and \(\theta_w=\theta_o=0\), so \(\dot V<0\) at every non-equilibrium point. \(V\) is positive definite and radially unbounded. The origin is globally asymptotically stable. \(\square\)

**Limits of theorem:** This does *not* prove stability under real heat generation, time-varying ambient, thermal hysteresis, grid DAE singularities, parameter uncertainty, nonlinear cooling or service constraints, and is NOT an empirically validated new physical finding. Its purpose is to supply a regression/unit-verification target for the passive two-node heat exchange block.

## 11. Necessary charging-service feasibility inequality (PROPOSITION)

Given an actual required delivered DC energy \(E_{\rm req}\) before departure \(t_d\), every feasible trajectory must satisfy
\[
E_{\rm req}\le \int_{0}^{t_d}P_{\rm DC}(t)\,dt
\le\int_{0}^{t_d}\overline P_{\rm DC}(t)\,dt
\]
for any **valid** upper bound \(\overline P_{\rm DC}(t)\) on power achievable by all admissible controls, grid states and thermal modes. If an independently defensible upper power envelope produces \(\int_0^{t_d}\overline P_{\rm DC}(t)\,dt<E_{\rm req}\), no admissible control policy can meet that service obligation.

The inequality follows from \(0\le P_{\rm DC}(t)\le \overline P_{\rm DC}(t)\) almost everywhere and integration. It is **necessary, not sufficient**: network constraints, competing service requests, control delays, thermal-state evolution or other obligations may still prevent meeting the deadline. One may use the trivial bound \(P_{\rm DC}\le P_{\rm rated}\), yielding \(E_{\rm req}\le P_{\rm rated}t_d\) as a weak necessary condition; tighter envelopes must be proved or measured, not asserted.

Neither proposition establishes a full coupled-network viability kernel. They are analytically supported components of a future mathematical verification program.
