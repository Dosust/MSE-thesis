# DELAYED CONTROL, HYSTERETIC HYBRID MODES, AC NETWORK DAE, AND OBSERVATION OPERATORS — v0.1

**17 October 2026 · CONDITIONAL MATHEMATICAL RESEARCH, NOT FIELD VALIDATION.**
Builds upon [THREE_STATE_ELECTROTHERMAL_THEOREMS_V01.md](THREE_STATE_ELECTROTHERMAL_THEOREMS_V01.md) in stacked PR #99. This document establishes an exact **sufficient small-gain condition for delay-robust incremental stability**, documents a mathematical delayed-feedback destabilization example, proves a mode-independent upper thermal enclosure and nonchattering conditions for a two-threshold relay, gives an AC network DAE with a concrete feasibility-loss example, and defines sensor-specific asynchronous observation maps. All numerical checks use **unmeasured synthetic coefficients**. The full three-state system with all realistic delays, hysteresis, grid dynamics, batteries, vehicle service, and uncertainty is **not** proved globally stable/viable.

## 0. Evidence provenance: no invented physical interface

- Q. Gong et al., IEEE *Transactions on Smart Grid* 2015 6(2):648–656, DOI 10.1109/TSG.2014.2365452, 9-page publisher PDF **original verified**: actual transformer winding-top/oil tests in temperature chamber under imposed **DC loss-equivalent** electric loads; simulated charging schedule and hot-spot distinct from observed top-winding. No simultaneously monitored operating charger + utility transformer.
- P. Kunlasing et al., IEEE ECTI-CON 2022, DOI 10.1109/ECTI-CON54298.2022.9795360, original 4-page PDF **verified**: transformer CT and PT100 oil/ambient measurements, and **manually initiated Zigbee control messages** physically modify IEC 61851 pilot duty cycle and current limit in two charger prototypes; the three-EV automatic overload-management case is simulation. No demonstrated oil-temperature-driven automated intervention.
- A. Krama et al., Elsevier *Energy Conversion and Management: X* 2026 31:101960, DOI 10.1016/j.ecmx.2026.101960, original 16-page publisher PDF **verified**: field rectifier-proxy temperature/EVSE offer and delivered power, with charger sensor temperature ~5-minute and electrical variables ~1-minute. No measured upstream external utility-transformer thermal response. No raw timestamped rows received. EVSE-internal part annotated "Transformer" is NOT the utility P transformer.
- Original Susa et al. (2005) IEEE complete heat equations **not yet inspected**: DOI 10.1109/TPWRD.2004.835255. **IEEE C57.91-2025** is active (issued 2026-03-05) according to https://standards.ieee.org/ieee/C57.91/7163/ ; **IEC 60076-7:2018** scope according to https://webstore.iec.ch/en/publication/34351 . The current complete authoritative equations/safety thresholds have **not** been read or implemented. None of the equations below is attributed verbatim to those standards.

## 1. Scope, glossary, SI dimensions, and governing heat balances

The thermal state is \(x(t)=(T_w(t),T_o(t),T_c(t))^\top\), where \(T_w\) is **effective winding temperature**, \(T_o\) is **effective oil temperature**, and \(T_c\) is **effective charger rectifier/cabinet temperature** [K]; \(t\) is time [s]. A winding needle reading is NOT the actual winding hotspot; a rectifier surface reading is NOT junction temperature.

| Symbol | Meaning | Role and SI unit |
|---|---|---|
| \(C_w,C_o,C_c>0\) | effective winding, oil, charger heat capacities | stored-heat coefficients [J/K] |
| \(g,r,s>0\) | winding↔oil, oil↔local atmosphere, charger↔local atmosphere thermal conductances | heat-flow coefficients [W/K] |
| \(T_w,T_o,T_c\) | three effective thermal states | K; derivative \(\dot T\) [K/s] |
| \(A_P,A_E\) | transformer-local and charger-local ambient temperatures | climate inputs [K] |
| \(p(t)\) | **actual delivered DC power**, conditional on sufficiently accepting battery/vehicle and controller | electrical interface input [W] |
| \(P_{\rm AC}(t)\) | electrical input at charger's AC terminals | electrical input [W] |
| \(P_r\) | charger rated allowable DC output in this idealized scenario | bound [W] |
| \(P_b\) | external non-EV real load measured at transformer secondary | input [W] |
| \(\eta\in(0,1]\) | fixed AC/DC efficiency | conversion parameter [1]; \(P_{\rm AC}=p/\eta\) here ONLY |
| \(R_\phi>0,V_{LL}>0\) | referred per-phase winding resistance [Ω] and RMS line-to-line voltage [V] | balance approximation |
| \(k=R_\phi/V_{LL}^2\) | copper heat vs squared real power constant | [1/W] |
| \(H(p)=k(P_b+p/\eta)^2\) | **effective** winding copper loss | heat production [W] |
| \(h_{\max}=\sup_{0\le p\le P_r}H'(p)\) | global slope of H on admissible power interval | [1]; in this model \(2k(P_b+P_r/\eta)/\eta\) |
| \(Q_0,Q_{\rm ext}\) | other transformer heat allocated to oil and charger external heat | constant sources [W] in proofs |
| \(\alpha\in[0,1]\) | portion of total charger conversion losses allocated to modeled charger node | [1] |
| \(\ell=\alpha(\eta^{-1}-1)\) | effective charger heat produced per DC watt | [1] |
| \(D_o,D_c\) | assumed temperature-conditioned oil and charger DC-power limits | [W], nonincreasing |
| \(L_o,L_c\ge0\) | Lipschitz slopes of \(D_o\) and \(D_c\) | [W/K] |
| \(\tau_o,\tau_c\) | measurement / communication / command latency at oil and charger limit paths | [s] |
| \(q\) | discrete controller operating mode (e.g. normal/restricted/off) | unitless finite set |
| \(E_{\rm DC},E_{\rm req},t_d\) | accumulated DC-port energy and required energy [J], deadline [s] | service variables |
| \(z_{\rm elec}\) | vector of grid complex voltage phasors and AC algebraic unknowns | mixed [V,A] with typed components |
| \(y_{j,k}\) | instrument \(j\)'s observation at timestamp \(t_{j,k}\) | units of corresponding measurement |
| \(w_{j,k}(\tau)\) | normalized time-aggregation weighting kernel | [1/s], integrates to 1 |
| \(\varepsilon_{j,k}\) | observation error | same unit as observed output |
| \(\Theta_{\rm on},\Theta_{\rm off}\) | hypothetical temperature switching thresholds | K, NOT published manufacturer ratings |
| \(\delta_{\min}\) | lower bound between successive hysteresis mode reversals | [s] |
| \(V_s,R_f,V,P_{\rm load}\) | feeder sending voltage [V], lumped real feeder resistance [Ω], receiving voltage [V], receiving real load [W] in scalar DAE example | electrical feasibility |

For constant ambient and fixed feasible electric conditions the candidate conserved thermal balance is
\[
\boxed{\begin{aligned}
 C_w\dot T_w &=H(p)-g(T_w-T_o), &(1a)\\
 C_o\dot T_o &=Q_0+g(T_w-T_o)-r(T_o-A_P), &(1b)\\
 C_c\dot T_c &=Q_{\rm ext}+\ell p-s(T_c-A_E). &(1c)
\end{aligned}}
\]
**Term-by-term role:** \(C_i\dot T_i\) = rate of stored energy [W]; \(H(p),Q_0,Q_{\rm ext},\ell p\) = heat sources [W]; \(g(T_w-T_o)\) = internal winding/oil heat exchange [W] with opposite signs; \(r(T_o-A_P),s(T_c-A_E)\) = ambient heat rejection [W]. No \(G_{P,c}(T_w-T_c)\) conduction exists. Adding 1a+1b cancels exchange and yields \(C_w\dot T_w+C_o\dot T_o=H(p)+Q_0-r(T_o-A_P)\). All terms have W units. \(H\) presumes balanced three-phase unity-PF constant-V resistive heating; Section 5 replaces it with a richer feeder algebraic model where supported.

## 2. Delayed feedback as a functional differential equation

In a fully accepting vehicle demand regime, introduce the **hypothesized** delayed measured-state control
\[
\boxed{p(t)=\min\{P_r,D_o[T_o(t-\tau_o)],D_c[T_c(t-\tau_c)]\}.}\tag{2}
\]
This formula defines \(p\) at time \(t\) from historical oil/charger states and does not express physical heat propagation delay between equipment. Actual measured control protocols can have **held/sampled** histories and different per-device command interfaces; constant transport delays are a mathematical approximation to be validated. If the actual BMS demand is lower than the cap, equation (2) is **false for delivered power**, and actual \(p\) must include the battery demand and dispatcher.

Under bounded delays, locally Lipschitz \(D_o,D_c\) clipped to \([0,P_r]\), and initial *history function* \(\phi:[-\tau_{\max},0]\to\mathbb R^3\) continuous, the delay equation with (1) is well-posed by the method of steps for fixed/bounded measurable environmental inputs; all state trajectories remain bounded for bounded weather, because the passive heating network is Hurwitz and \(p\) is bounded. This is **solution existence and boundedness, not automatically robust stability or safety**.

## 3. Explicit sufficient arbitrary-bounded-delay stability theorem (THEOREM A)

**Statement.** Suppose (i) g,r,s,C_i>0, \(H\) Lipschitz over [0,P_r] with constant \(h_{\max}\ge0\); (ii) fixed constant \(A_P,A_E,Q_0,Q_{\rm ext}\); (iii) \(D_o,D_c\) nonincreasing, globally Lipschitz with constants \(L_o,L_c\ge0\), range [0,P_r]; (iv) **both delayed thermal feedback paths are mode-fixed** and satisfy \(\tau_o,\tau_c\in[0,\tau_{\max}]\) for finite \(\tau_{\max}\); and (v) the small-gain condition
\[
\boxed{\kappa=\frac{h_{\max}L_o}{r}+\frac{\ell L_c}{s}<1.}\tag{3}
\]
Then the delayed three-state model (1)-(2) is **incrementally exponentially stable**: differences of any two trajectories with the same fixed external forcing and appropriately bounded continuous initial histories decay exponentially, with constants depending on \(\tau_{\max}\) and physical parameter bounds. In particular the unique equilibrium from the undelayed fixed-point theorem remains exponentially attracting **for this mode-fixed delayed system**.

**Every term:** \(h_{\max}\) = maximum additional winding heating [W] per charging-power watt [W/W]; \(L_o,L_c\) = reduction-cap slopes [W/K]; \(r,s\) = oil and charger ambient thermal cooling [W/K]; \(\ell\) = charger node heat [W] per DC power [W]. \(\kappa\) is **dimensionless**. The inequality is a **sufficient, possibly highly conservative** stability certificate; \(\kappa\ge1\) does NOT imply unstable control.

**Proof.** For deviations of two solutions, \(e_i=T_i^{(1)}-T_i^{(2)}\), use \(|H(p_1)-H(p_2)|\le h_{\max}|p_1-p_2|\) and min-map Lipschitz inequality:
\[
|p_1(t)-p_2(t)|\le L_o|e_o(t-\tau_o)|+L_c|e_c(t-\tau_c)|.\tag{4}
\]
Set \(v=(|e_w|,|e_o|,|e_c|)^\top\) and use upper Dini derivatives. They satisfy a **positive comparison inequality**
\[
D^+ v(t)\le A_0v(t)+B_o v(t-\tau_o)+B_c v(t-\tau_c),\tag{5}
\]
componentwise, with
\[
A_0=\begin{pmatrix}
-g/C_w&g/C_w&0\\g/C_o&-(g+r)/C_o&0\\0&0&-s/C_c
\end{pmatrix},\quad
B_o+B_c=\begin{pmatrix}h_{\max}/C_w\\0\\\ell/C_c\end{pmatrix}
\begin{pmatrix}0&L_o&L_c\end{pmatrix}.\tag{6}
\]
\(A_0\) is Metzler and Hurwitz; the \(B_i\) are nonnegative matrices. Direct block inversion shows
\[
(-A_0)^{-1}\begin{pmatrix}h_{\max}/C_w\\0\\\ell/C_c\end{pmatrix}
=\begin{pmatrix}h_{\max}(1/g+1/r)\\h_{\max}/r\\\ell/s\end{pmatrix},
\quad
\rho\bigl((-A_0)^{-1}(B_o+B_c)\bigr)=\kappa.\tag{7}
\]
Here \(\rho(M)\) means spectral radius (largest absolute eigenvalue, dimensionless). For \(\kappa<1\), \(A_0+B_o+B_c\) is Hurwitz by the Metzler/nonnegative matrix small-gain criterion; equivalently there exists a strictly positive vector \(w\) with \((A_0+B_o+B_c)w<0\). By continuity select sufficiently small \(\epsilon>0\) [s^-1] with
\[
(A_0+\epsilon I+e^{\epsilon\tau_{\max}}(B_o+B_c))w<0.\tag{8}
\]
A first-exit comparison with \(M w e^{-\epsilon t}\), choosing \(M\) large enough to dominate the initial history on \([-\tau_{\max},0]\), proves \(v_i(t)\le M w_i e^{-\epsilon t}\) for all \(t\ge0\). Hence exponential decay of differences and of displacement from the constant equilibrium. □

**Boundary:** Theorem A does NOT apply automatically to switching modes, state-dependent jumps of control law, variable ambient across the compared trajectories, nonlinear \(\eta(T)\), actual network voltage collapse, implicit battery taper, or arbitrary unbounded latency. The formula assumes a **smooth/Lipschitz** cap and no sensor reset. Although negative feedback may be stable for gains beyond (3), it is not certified by this theorem.

## 4. Delayed-feedback instability counterexample (THEOREM B)

A generic scalar negative-feedback subsystem
\[
\boxed{\dot z(t)=-a_0 z(t)-k_d z(t-\tau),\quad a_0,k_d>0,\ \tau\ge0}\tag{9}
\]
has \(z(t)\) = arbitrary small deviation from equilibrium [e.g. K], \(a_0\) = local passive decay rate [s^-1], \(k_d\) = delayed negative-feedback strength [s^-1], and \(\tau\) = fixed control delay [s]. This is a **mathematical illustration**, NOT an exact measured simplification of Gong/Kunlasing/Krama or the 3-state model.

The characteristic equation is \(\lambda+a_0+k_de^{-\lambda\tau}=0\), where \(\lambda\) [s^-1] is a characteristic root. If \(k_d>a_0\), a purely imaginary root \(\lambda=i\omega\) occurs for
\[
\boxed{\omega=\sqrt{k_d^2-a_0^2},\qquad
\tau_*=\frac{\arccos(-a_0/k_d)}{\omega}.}\tag{10}
\]
Its real crossing slope is
\(\Re(d\lambda/d\tau)=\omega^2/[(1+a_0\tau_*)^2+(\omega\tau_*)^2]>0\).
Therefore roots move into the right half-plane just beyond the first critical delay, so stability may be lost. For purely **synthetic** \(a_0=1/3600\ {\rm s}^{-1}, k_d=3/3600\ {\rm s}^{-1}\), \(\tau_*\simeq2431.84\) s (40.53 min); **this is not an estimated infrastructure delay**. This refutes any general claim that instantaneous stability assures arbitrary-delay stability.

## 5. Hybrid switching and hysteresis with explicit semantics

Let \(q\in\{\text{normal},\text{restricted},\text{off}\}\) be a discrete operational/controller mode (unitless). Thermal state \(x(t)\) remains **continuous** across an ordinary electronic control switch; charger electric power may jump. In each mode define the algebraic admissible DC range \(0\le p(t)\le\overline p_q(x,z_{\rm elec},u)\le P_r\), with mode-specific command interfaces and electrical power conversion. Do not confuse a **simulated** transformer-oil threshold with Kunlasing's **measured electrical overload** messages.

One **hypothetical** oil-temperature guard design is
\[
\text{normal}\to\text{restricted if }T_{o,\rm measured}\ge\Theta_{\rm on},\qquad
\text{restricted}\to\text{normal if }T_{o,\rm measured}\le\Theta_{\rm off},
\quad\Theta_{\rm off}<\Theta_{\rm on}.\tag{11}
\]
\(\Theta_{\rm on/off}\) [K] are proposed **setpoints** with a positive hysteresis gap \(\Delta\Theta=\Theta_{\rm on}-\Theta_{\rm off}>0\) [K]. These are not published transformer winding hot-spot safety limits. A switching command also requires timestamp, device authority, setpoint and acknowledgement; the IEC 61851 PWM pilot demonstration in Kunlasing is NOT automatically interchangeable with CCS2 DC power-management protocols.

**No-chattering lemma:** If an ideal continuous guard uses real \(T_o\), \(|\dot T_o|\le M_o<\infty\) [K/s] on the compact region, and only these two opposite mode transitions are possible (no asynchronous faults or reset), every pair of successive opposite hysteretic switches must be separated by at least
\[
\boxed{\delta_{\min}\ge\Delta\Theta/M_o>0.}\tag{12}
\]
The state must traverse the entire positive temperature gap; integrating \(|\dot T_o|\le M_o\) proves the bound. Thus no infinitely many such reversals occur in finite time. At \(M_o=0\) no temperature-driven reversal occurs; the quotient bound is only used for \(M_o>0\). **Bounded latency, noisy sampled guards, faults and externally forced toggles require separate debounce/dwell logic**. This lemma does not prove closed-loop thermal stability or heating response under hysteretic operation.

**Delayed safety caution:** if an actuator acts at time \(t\) on a temperature sampled \(\tau>0\) seconds earlier and \(|\dot T_o|\le M_o\), then \(|T_o(t)-T_o(t-\tau)|\le M_o\tau\). A threshold must reserve a physically justified sensing/communication/actuation margin, and additional heating after actuation must be bounded. Simply setting \(\Theta_{\rm on}\) equal to a temperature rating is **not** a proof of protection.

**Mode-independent upper temperature bound (COROLLARY):** If all modes enforce \(0\le p(t)\le\bar p\le P_r\) and ambients satisfy \(A_P(t)\le A_P^+\), \(A_E(t)\le A_E^+\), then the previously proved upper enclosure
\[
U_o=A_P^++\frac{Q_0+H(\bar p)}r,\quad
U_w=U_o+\frac{H(\bar p)}g,\quad
U_c=A_E^++\frac{Q_{\rm ext}+\ell\bar p}s \tag{13}
\]
remains forward invariant across arbitrary mode switches **provided x is continuous and inputs remain bounded**. It is a modeled-state enclosure, **not** safety for a latent hotspot/junction or service guarantee. Hysteretic events and switching cannot add impulsive heat or reset temperatures without a separate physical state-reset law.

**Service limits:** \(\dot E_{\rm DC}=p(t)\ge0\), \(E_{\rm DC}(t_d)=\int_0^{t_d}p(t)dt\) [J]. A guaranteed availability schedule \(\underline p(t)\) [W] would suffice for service only when \(\underline p(t)\le p(t)\) is proven under every admissible mode/hazard and \(\int_0^{t_d}\underline p(t)dt\ge E_{\rm req}\). No positive lower power is guaranteed if an unrestricted-length off mode is allowed. Thermal boundedness cannot alone imply actual charging/mobility service.

## 6. Electrical network constraints and DAE solvability

A realistic network model must connect EVSE at **actual AC terminals** to transformer secondary, power flows, feeder limits, reactive energy and voltage before sending power into H:
\[
\boxed{ \mathbf I=\mathbf Y_{\rm bus}\mathbf V,\quad
 S_{i\varphi}=V_{i\varphi}I_{i\varphi}^{*},\quad
 S_{i\varphi}=P_{i\varphi}+{\rm j}Q_{i\varphi}.}\tag{14}
\]
**Every symbol:** \(\mathbf V\) = network complex node/phase voltage phasors [V], \(\mathbf I\) = injected phase currents [A], \(\mathbf Y_{\rm bus}\) = bus admittance matrix [S=Ω^-1], \(i\) = bus index, \(\varphi\) = electrical phase (a,b,c), * = complex conjugation, \(S_{i\varphi}\) = complex power [VA], \(P_{i\varphi}\) = real power [W], \(Q_{i\varphi}\) = reactive power [var], and \({\rm j}^2=-1\). All values must have a consistent **injection vs consumption sign convention** (e.g. consumption = negative injection). Three-phase lines may couple phases; neutral grounding and conductor physics may matter. Harmonic RMS/stray heating is a separate frequency-resolved addition and is not inferred directly from aggregate THD.

Define a branch/model electrical algebraic residual
\[
\boxed{0=\mathcal G_{\rm PF}(z_{\rm elec},x,q,u,w;\theta_{\rm line}),}\tag{15}
\]
where \(\theta_{\rm line}\) includes actual conductor and transformer network parameters; \(u\) contains commands, \(w\) external loads/weather. Voltage, per-phase RMS current, real/reactive power, thermal ampacity, protection and actual AC charger power limits must be enforced; the earlier simple \(I=P/(\sqrt3 V_{LL})\) formula applies **only** to balanced unity-PF loading without neglected harmonic contribution.

**Index-one local DAE gate:** Given a regular feasible operating branch, \(\partial \mathcal G_{\rm PF}/\partial z_{\rm elec}\) must be nonsingular to locally solve algebraic states as functions of differential/control states; then the ODE stability analysis can be extended **only after including the derivative of the algebraic elimination**. Theorem A does NOT automatically survive this additional voltage/power/loss feedback.

**Explicit feeder counterexample (THEOREM C):** For a purely resistive single-phase feeder of sending voltage \(V_s>0\) [V] and line resistance \(R_f>0\) [Ω], with constant real receiving load \(P_{\rm load}\) [W] and receiving terminal voltage \(V\) [V], KVL gives \(I=(V_s-V)/R_f\) [A] and
\[
\boxed{P_{\rm load}=VI=\frac{V(V_s-V)}{R_f}.}\tag{16}
\]
Solving \(V^2-V_sV+R_fP_{\rm load}=0\), real nonnegative voltage requires
\[
\boxed{P_{\rm load}\le\frac{V_s^2}{4R_f}.}\tag{17}
\]
At equality the two algebraic voltage branches merge at \(V=V_s/2\); \(\partial [V(V_s-V)/R_f-P_{\rm load}]/\partial V=(V_s-2V)/R_f=0\), so the local regularity condition fails. This is a **mathematical loss-of-feasibility and algebraic singularity example**, not a prediction for the user's feeder or a complete three-phase load-flow solution. If charger and other load consume \(P_{\rm load}=P_b+p/\eta\), this feeder restricts real charging power more than a charger-only nameplate constraint may indicate. Reactive loads, lower-voltage requirements, transformer capacity and protection make practical limits more restrictive.

**Synthetic check:** \(V_s=230\) V, \(R_f=0.5\) Ω yields \(P_{\rm load,max}=26,450\) W; these are **invented toy numbers**, not feeder measurements.

## 7. Physically meaningful observation and timing operators

Measured data do not equal abstract thermal states by assertion. General discrete reading for instrument \(j\), sample \(k\):
\[
\boxed{y_{j,k}=\int_{\mathcal W_{j,k}}\!w_{j,k}(\tau)\,
  \mathcal H_j[x(\tau),z_{\rm elec}(\tau),q(\tau)]\,d\tau
  +\varepsilon_{j,k},\quad \int_{\mathcal W_{j,k}}w_{j,k}(\tau)d\tau=1.}\tag{18}
\]
**Variables:** \(y_{j,k}\) = actual sensor reading (K, W, A, etc.), \(\mathcal W_{j,k}\) = sampling/integration time support [s], \(w_{j,k}\) = normalized weighting [s^-1], \(\mathcal H_j\) = sensor-location/unit-specific model mapping, \(\varepsilon_{j,k}\) = sensor/model error with same units as y, and \(k\) = sample ordinal. The integral is optional for near-instantaneous instruments (delta-limit sampling). It is not a claim that real sensors follow a known averaging kernel without instrument specifications.

| Reported data source | Actual measured quantity | Model observation map / caution |
|---|---|---|
| Gong (2015) laboratory | top-oil thermocouples, top-winding needle probes, ambient, imposed current/resistance | top-oil \(\mathcal H_{oil}(x)\) requires location/volume mapping; top-winding \(\mathcal H_{top}(x)\) is **not actual HST**; physical chamber currents are DC-equivalent loading |
| Kunlasing (2022) operational prototype | PT100 oil temperature, ambient, transformer CT RMS load, manually commanded pilot PWM | \(\mathcal H_{PT100}(x)\) temperature and \(\mathcal H_{CT}(z_{\rm elec})\) electrical measurement are distinct; PWM/current allowance is an *actuator record*, not oil temperature |
| Krama (2026) single 50-kW EVSE | rectifier external module temperature sensors (mean of channels 1,2,3,7); ambient (mean 9,10); AC/DC and SOC/offer power | \(T_c\) requires explicit rectifier sensor→lump mapping; junction temperature not observed; ~5-min thermal vs ~1-min electrical sample grids; firmware state unknown |

The **offered charger power \(P_{\rm off}\)** and **delivered DC power \(p=P_{\rm DC}\)** are different observations; BMS/vehicle state may bind. Conflating the two incorrectly attributes battery acceptance to charger thermal derating. Timestamp sync errors/5-minute thermal support prevent inferring sub-sample causal ordering without interval uncertainty.

**Structural observability test:** If an idealized sensor measures \(y=(T_o,T_c)\) exactly, and the unforced thermal matrix \(A_0\) and its coefficients are independently known, the linear pair \((A_0,C)\) with
\[
C=\begin{pmatrix}0&1&0\\0&0&1\end{pmatrix}\tag{19}
\]
has observability rank three when \(g>0\): the oil-temperature derivative contains coefficient \(g/C_o\ne0\) multiplying hidden winding state. \(C\) is a *dimensionless state-selection observation matrix*, not a physical capacitance. The observability matrix \(\mathcal O=(C^\top,(CA_0)^\top,(CA_0^2)^\top)^\top\) has rank 3. This statement does **not** prove that actual top oil and rectifier thermistors equal model states, that derivatives are robust to noise, or that unknown heat capacities/conductances are identifiable. In practice \(T_w=T_o+[C_o\dot T_o-Q_0+r(T_o-A_P)]/g\) requires known parameters and differentiating noisy oil temperatures; the effective \(T_w\) remains distinct from true hot-spot.

## 8. Reproducible synthetic checks and falsification gates

Companion [VERIFY_DELAY_HYBRID_DAE_OBSERVATION_V01.py](VERIFY_DELAY_HYBRID_DAE_OBSERVATION_V01.py) independently checks:
1. \(\kappa\) analytically against \(\rho((-A_0)^{-1}(B_o+B_c))\) and negative-real-part eigenvalues in an **illustrative** admissible low-gain case.
2. Scalar delayed feedback critical imaginary crossing and positive crossing derivative.
3. Two-threshold mode reversals across bounded-rate oil temperature.
4. AC real-voltage feeder quadratic roots, fold singularity and no-real-root infeasibility.
5. Full-rank linear observation for oil and charger state selection vs rank deficiency of charger-only observation in the unforced model.
6. Inward vector-field signs for 500 random artificial upper-face/lower-power/ambient cases.

The tests are **code/logic verification**, not new source measurements. Their invented transformer/EVSE capacitances, conductances, charger power, ambient and modes must never be used for real equipment safety limits or actual travel-energy predictions.

**Model falsification / evidence gates before field validity:**
- Acquire or authoritatively verify full Susa (2005) IEEE equations and full current IEEE C57.91-2025/IEC 60076-7:2018 versions before imposing standard-based temperature criteria.
- Obtain device schematics, feeder phase impedances, time-synced upstream LV current/voltage/PF/harmonic spectra, transformer actual oil/top-winding/HST sensors (where permitted), device firmware/control rules, EVSE true AC/DC offered/delivered electrical streams and rectifier thermometry, distinct ambients and sensor-position calibration.
- Identify causal excitation/controlled action and clocks; disaggregate time-invariant common hot weather from directionally actuated electrical consequences; hold out independent temporal events and additional hardware before source-to-receiver causal claims.
- Confirm delay distributions, sample-and-hold behavior, mode logs, oil protection setpoints, firm device DC control interface, and actual battery/vehicle demand; otherwise model them as uncertainty and label hypothetical.
- Check electrical branch and index-1 DAE regularity throughout admissible state/hazard set; explicitly treat no-solution and fault states rather than assuming continued charging service.
- Future formal work: mixed DAE/delay/hybrid safety-barrier conditions with calibrated uncertainty and a provable service reachability kernel. None is demonstrated merely by the present source-comparison and synthetic tests.

## 9. Release status

| Item | Assessment |
|---|---|
| First-law heat balance and electrical-port semantics | **Derived, dimensionally audited under simplified assumptions** |
| Bounded-delay fixed-mode incremental exponential stability | **Proved under conservative small-gain condition (3)** |
| Sufficient condition (3) with gain >=1 | **No conclusion** |
| General delay destabilization | **Proved for separate scalar illustrative counterexample** |
| Two-threshold continuous-sensor hysteresis nonchattering | **Proved under bounded rate, with explicit exclusions** |
| Invariant thermal upper enclosure under arbitrary bounded mode-dependent p | **Proved under continuity and p/weather bounds** |
| AC 1-line voltage fold / loss of algebraic feasibility | **Derived, not equipment-calibrated** |
| Full unbalanced AC DAE solver, physical grid parameterization and preservation of stability | **NOT implemented or validated** |
| Actual oil/winding/rectifier observation equality and cross-device time sync | **NOT validated** |
| Field-validated thermal response across utility P and EVSE charger | **NOT established** |
| Actual service feasibility during faults | **NOT established** |
| Full hybrid/DDE/DAE robust viability and scientific novelty | **NOT proved** |

**Core conclusion:** rigorous restricted delay and hybrid safeguards are available, but extending mathematical consistency to full source-validated complex-system resilience is an **open research task**, not a completed physics result.
