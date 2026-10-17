# THREE-STATE POWER–ELECTRIFIED-TRANSPORTATION ELECTROTHERMAL MATHEMATICS v0.1

**Status:** mathematically proven restricted results + standalone *synthetic* numerical verification; **NOT** a fitted or field-validated model, **NOT** an IEEE/IEC compliance demonstration, **NOT** proof of novelty. Date 2026-10-17. Extension of reduced 2-state theoretical PR #98. The component evidence is from independently audited *original* Gong (2015), Kunlasing (2022), Krama (2026) papers in parent branches. Susa et al. (2005) complete original and IEEE C57.91-2025/IEC 60076-7:2018 complete normative equations remain **not fully verified**. No original Krama time-series or synchronized EVSE/upstream-transformer dataset received.

## 0. Source provenance and semantic limits

- Gong Q. et al. (2015), *PEV Charging Control Considering Transformer Life and Experimental Validation of a 25 kVA Distribution Transformer*, DOI 10.1109/TSG.2014.2365452; **lab test top winding / oil, true hot spot not directly measured**; electric load trajectories mimic PEV charging, not matched real EVSE field data.
- Kunlasing P. et al. (2022), *Transformer Load Monitoring and EV Charging Control Function*, DOI 10.1109/ECTI-CON54298.2022.9795360; **PT100 oil temperature observation** and **manual** Zigbee/IEC 61851 pilot actuation on 2 EV chargers; automatic 3-EV load management simulated, oil-temperature-triggered closed-loop action not physically demonstrated.
- Krama A. et al. (2026), *Impact of extreme climatic conditions on fast EV charger performance: field experimental insights from Qatar*, DOI 10.1016/j.ecmx.2026.101960; **field EVSE rectifier temperature and AC/DC power**, empirical derating curves, **no field upstream utility-transformer thermal sensor**. EVSE-internal transformer in illustration is not the grid P transformer.
- Susa D. et al. (2005), DOI 10.1109/TPWRD.2004.835255; article **identity and abstract** independently confirmed, but exact full original equations not checked. Official active **IEEE C57.91-2025**, published 2026-03-05, superseding C57.91-2011: https://standards.ieee.org/ieee/C57.91/7163/. Official **IEC 60076-7:2018** description https://webstore.iec.ch/en/publication/34351. This artifact does **not** claim the following proposed ODEs are quoted from either standard.

## 1. Meaning and units of every symbol

All temperatures may be **represented numerically in °C** in simulation because the balances depend on *temperature differences* and *rates*; SI dimension notation is K and K/s. Absolute-temperature-dependent ageing laws would require **Kelvin**.

| Symbol | Definition | SI unit / role |
|---|---|---|
| \(t\) | time | s, independent variable |
| \(x=(T_w,T_o,T_c)^\top\) | effective winding, oil and charger rectifier/cabinet thermal states | K, three-state vector |
| \(\dot T_i=dT_i/dt\) | time derivative of state \(i\) | K s^-1 |
| \(C_w,C_o,C_c\) | positive lumped effective thermal capacitances | J K^-1 |
| \(g=G_{wo}\) | winding→oil thermal conductance | W K^-1 |
| \(r=G_{oa}\) | oil→ambient thermal conductance | W K^-1 |
| \(s=G_{ca}\) | charger→ambient thermal conductance | W K^-1 |
| \(A_P(t),A_E(t)\) | transformer-local and charger-local ambient-temperature inputs | K |
| \(Q_0\) | core and/or fixed losses allocated **once** to oil compartment | W |
| \(Q_{\rm ext}\) | effective charger external heat gain allocated once (constant for propositions) | W |
| \(P_b\) | other balanced secondary real-power demand | W |
| \(p=P_{\rm DC}\) | **delivered DC power**, equals offered/available cap only when vehicle demand can accept full offer and controller requests it | W |
| \(P_{\rm AC}\) | charger electrical input | W |
| \(\eta\) | constant charger electrical conversion efficiency | 0 < η ≤1, dimensionless |
| \(\alpha\) | fraction of entire conversion loss thermally allocated to modeled charger thermal compartment | 0≤α≤1, dimensionless |
| \(\ell=\alpha(\eta^{-1}-1)\) | charger node heat [W] per DC output [W] | dimensionless, ≥0 |
| \(V_{LL}\) | fixed three-phase line-to-line RMS voltage | V |
| \(R_\phi\) | fixed equivalent per-phase resistance, correctly referred to monitored side | Ω |
| \(k=R_\phi/V_{LL}^2\) | power-dependent copper-loss coefficient | W^-1 |
| \(H(p)=k(P_b+p/\eta)^2\) | transformer winding Joule heat under balanced unity-PF approximation | W |
| \(h=H'(p)\) | derivative of transformer copper heat with DC charging power | dimensionless, ≥0 for P_b,p≥0 |
| \(P_r\) | maximum admissible charger DC power in this abstraction | W |
| \(D_o(T_o),D_c(T_c)\) | **assumed** transformer-oil-condition and charger-condition DC-equivalent power caps | W; continuous nonincreasing |
| \(a=-\partial p/\partial T_o,\ b=-\partial p/\partial T_c\) | local nonnegative **negative-feedback sensitivities** in differentiable regimes | W K^-1 |
| \(T_{w,\max},T_{o,\max},T_{c,\max}\) | upper bounds on *these exact effective/observed states*, if physically justified | K; not supplied by source papers |
| \(E_{\rm DC}(t)=\int_0^t p(\tau)d\tau\) | accumulated port-level delivered DC energy | J |
| \(E_{\rm req},t_d\) | actual charging-energy requirement [J] and deadline [s], externally supplied | J, s |
| \(J\) | Jacobian of thermal ODE vector field, **not** an objective value | s^-1 |
| \(\lambda\) | complex eigenvalue spectral variable of J | s^-1 |

**Source-interpretation guard:** \(T_w\ne\) *measured winding hot spot* by default; Gong observed top-winding not true hot-spot. \(T_c\ne T_j\) semiconductor junction. \(T_o\) is an effective oil state that must be associated with a real sensor position/mapping before physical calibration. Without a measured manufacturer safety bound and a validated mapping these variables cannot be declared safe from a numerical inequality.

## 2. Reduced physical energy model and electric coupling

**Assumptions for mathematical theorems:**

(A1) \(C_w,C_o,C_c,g,r,s>0\) constant; independent constant ambient \(A_P,A_E\), constant \(Q_0,Q_{\rm ext}\ge0\).

(A2) \(0<\eta\le1\), \(0\le\alpha\le1\), \(P_b\ge0\), \(R_\phi\ge0\), \(V_{LL}>0\); balanced three-phase, unity PF, quasi-steady electrical response at the chosen boundary. No harmonic, unbalance, feeder voltage-drop, converter idle consumption, or winding resistance temperature feedback in this restricted proof.

(A3) In the high-demand saturated operating regime the delivered power instantaneously equals
\[
p(T_o,T_c)=\min\{P_r,D_o(T_o),D_c(T_c)\},\quad 0\le D_o,D_c\le P_r,
\tag{M1}
\]
where \(D_o,D_c\) are continuous nonincreasing. **D_o is a hypothetical temperature-based control authority, NOT an effect proven by Kunlasing.** In general low demand, actual delivered power is **at most** this cap, not necessarily equal.

(A4) For global existence/uniqueness of trajectories require these caps locally (or globally) Lipschitz; for differentiable-branch stability require the resulting p be continuously differentiable near equilibrium with \(a,b\ge0\). Neither hypothesis is valid automatically across min-law ties/saturation switching.

(A5) Electrical AC/DC energy accounting uses \(P_{\rm AC}=p/\eta\) and whole-charger electrical losses \(L_{\rm total}=P_{\rm AC}-p=(\eta^{-1}-1)p\). The charger state receives \(\alpha L_{\rm total}=\ell p\), while \((1-\alpha)L_{\rm total}\) is lost to other excluded compartments/ambient, not double-counted.

Three-state temperature evolution:
\[
\boxed{\begin{aligned}
C_w\dot T_w &=H(p)-g(T_w-T_o), &&(M2)\\
C_o\dot T_o &=Q_0+g(T_w-T_o)-r(T_o-A_P), &&(M3)\\
C_c\dot T_c &=Q_{\rm ext}+\ell p-s(T_c-A_E). &&(M4)
\end{aligned}}
\]
\[
\boxed{H(p)=\frac{R_\phi}{V_{LL}^2}\left(P_b+\frac p\eta\right)^2,\quad
P_{\rm AC}=\frac p\eta.}\tag{M5}
\]

**Physical why:** winding Joule heat, winding→oil heat exchange, oil→air heat rejection, rectifier effective heat from a subset of AC/DC conversion losses, and charger→air rejection. External transformer and EVSE are **not** connected by a term \(G_{Pc}(T_P-T_c)\): there is no assumed spatial heat conduction. Oil-state power restriction is an **information/control interface**; charger→transformer influence is a change of **electrical** loading.

**Dimensional check:** \(C_i\dot T_i=(\mathrm{J/K})(\mathrm{K/s})=\mathrm W\). Conductance × temperature difference \(=(\mathrm{W/K})\mathrm K=\mathrm W\). \(H\) has W, because \(R_\phi/V_{LL}^2\) has Ω/V²=1/W. Total P vs reactive Q are never added in the simplified electric balance; no service/winding hot-spot temperature limit imported from a standard.

**First-law cancellation:**
\[
\frac{d}{dt}(U_w+U_o)=C_w\dot T_w+C_o\dot T_o
=H(p)+Q_0-r(T_o-A_P).\tag{M6}
\]
The internal \(g(T_w-T_o)\) cancels, demonstrating no artificial energy creation across the transformer's two internal nodes. Full charger's remaining unmodeled converter heat \((1-\alpha)L_{\rm total}\) is not in U_c; applying all L_total to U_c while also adding other device heat would double-count.

## 3. Equilibrium theorem: exact existence and uniqueness (THEOREM 1)

**Conditions:** (A1)–(A3), \(P_r>0\), and \(H(p)\) continuous nondecreasing for \(p\in[0,P_r]\) (true for M5 given A2).

At equilibrium with trial power \(p\):
\[
\boxed{\begin{aligned}
T_o(p)&=A_P+\frac{Q_0+H(p)}r,&&(E1)\\
T_w(p)&=T_o(p)+\frac{H(p)}g,&&(E2)\\
T_c(p)&=A_E+\frac{Q_{\rm ext}+\ell p}s.&&(E3)
\end{aligned}}
\]
These are *effective* steady temperatures; neither an equipment rating nor a source-paper measurement.

Define \(L(p)=\min\{P_r,D_o(T_o(p)),D_c(T_c(p))\}\). Both \(T_o(p)\) and \(T_c(p)\) are nondecreasing, so \(L(p)\) is continuous **nonincreasing**. The scalar root function \(F(p)=p-L(p)\) is continuous with \(F(0)\le0\), \(F(P_r)\ge0\). For \(p_2>p_1\),
\(F(p_2)-F(p_1)=(p_2-p_1)-(L(p_2)-L(p_1))\ge p_2-p_1>0\).
By IVT there is **exactly one** root \(p^*\). Equations E1–E3 then specify exactly one thermal equilibrium. □

**Important:** equilibrium uniqueness does **not** prove equipment safety, stable dynamics, real delivered electricity/transport service, or convergence under time-varying heat. If BMS demand is lower than the offered power, A3 fails and equilibrium conditions must be revised.

**Comparative statics (COROLLARY):** Holding every other parameter fixed, increasing \(A_P\) cannot increase the unique equilibrium delivered charging power \(p^*\); similarly increasing \(A_E\) cannot increase \(p^*\). Proof: for each fixed p, a hotter ambient raises the associated effective T_o or T_c, cannot raise their nonincreasing D limit, and hence cannot increase L; the unique root of strictly increasing \(F=p-L\) can only shift weakly downward. **This is a monotonicity theorem for p only**. It does *not* imply transformer oil temperature always increases under extreme heat, because derating alters H(p), nor imply cumulative delivered energy always decreases when users defer charging.

## 4. Local exponential stability in the full 3-state differentiable model (THEOREM 2)

Assume a continuously differentiable cap \(p(T_o,T_c)\) near the equilibrium (e.g. strict-active branch of min law or smoothly blended cap), satisfying \(\partial p/\partial T_o=-a\le0\), \(\partial p/\partial T_c=-b\le0\), and define \(h=H'(p^*)\ge0\).

The exact thermal Jacobian \(J=\partial(\dot T_w,\dot T_o,\dot T_c)/\partial(T_w,T_o,T_c)\) is
\[
\boxed{J=
\begin{pmatrix}
-\frac g{C_w}&\frac{g-ha}{C_w}&-\frac{hb}{C_w}\\
\frac g{C_o}&-\frac{g+r}{C_o}&0\\
0&-\frac{\ell a}{C_c}&-\frac{s+\ell b}{C_c}
\end{pmatrix}.}\tag{J1}
\]

**Read the columns:** Winding temperature affects oil by physical conductance g; oil temperature affects winding both by physical return conductance g and by hypothetical power restriction \(-ha\); charger temperature affects winding by \(-hb\), because electrical load changes Joule heat; oil affects charger by \(-\ell a\) through limited charging power. There is NO conductive thermal transformer↔charger entry.

For legible Routh–Hurwitz analysis, define all six *rates* [s^-1]:
\[
A=\frac g{C_w}>0,\quad B=\frac g{C_o}>0,\quad
R=\frac r{C_o}>0,\quad S=\frac s{C_c}>0,\quad
F=\frac{ha}{C_w}\ge0,\quad M=\frac{\ell b}{C_c}\ge0,\quad U=A+B+R.
\tag{J2}
\]
Uppercase R here is an inverse-oil-cooling time scale **not the physical winding resistance \(R_\phi\)**. \(F\) quantifies transformer-power feedback on winding heating per oil temperature change; \(M\) quantifies charger heat change per charger temperature change. An additional off-diagonal product identity cancels cross terms.

Direct determinant expansion for the characteristic polynomial yields
\[
\det(\lambda I_3-J)=\lambda^3+c_1\lambda^2+c_2\lambda+c_3,\tag{J3}
\]
where
\[
\boxed{\begin{aligned}
c_1&=U+S+M,\\
c_2&=AR+BF+U(S+M),\\
c_3&=S(AR+BF)+MAR.
\end{aligned}}\tag{J4}
\]
Each coefficient is strictly positive (including a=b=0), and the final cubic Routh–Hurwitz inequality is
\[
\boxed{c_1c_2-c_3
=U(AR+BF)+MBF+U(U+S+M)(S+M)>0.}\tag{J5}
\]
Thus \(c_1>0,c_2>0,c_3>0,c_1c_2>c_3\); the Routh–Hurwitz criterion gives \(\Re(\lambda_i)<0\) for all three eigenvalues. Since the nonlinear vector field is \(C^1\) near the equilibrium, **local exponential stability** follows from the linearization theorem. □

**Scope:** This is a three-state proof for the *reduced physical laws* M1–M5, **not** a proof for all thermoelectric transformer models, realistic network algebraic constraints, variable efficiency, loss-dependent winding resistance, battery taper, delayed control, feedback switching at nonsmooth cap ties, or global convergence. Importantly, \(\det J<0\) at these stable 3D equilibria; demanding \(\det J>0\) as in 2×2 Routh–Hurwitz would be wrong. The actual cubic uses \(\det(-J)=c_3>0\).

## 5. Existence, boundedness and extreme-heat forcing

If \(D_o,D_c\) are locally Lipschitz and remain clipped in [0,P_r], then p(x) and H(p(x)) are globally Lipschitz in x under globally Lipschitz caps, and the ODE vector field is globally Lipschitz for fixed bounded inputs. For finite initial state and bounded measurable \(A_P(t),A_E(t)\), standard Carathéodory ODE theory gives a unique absolutely continuous solution for all \(t\ge0\). Temperatures remain bounded for bounded inputs because the passive thermal matrix
\[
A_0=\begin{pmatrix}
-g/C_w &g/C_w&0\\
g/C_o&-(g+r)/C_o&0\\
0&0&-s/C_c
\end{pmatrix}
\]
is Hurwitz, and all exogenous/source forcing is bounded by clipped p. This guarantees **finite trajectories**, not thermal safety or deadline service.

Extremely hot weather is introduced by the two **measured-location** forcing inputs \(A_P(t),A_E(t)\); no assumption that those two timeseries are equal or independently causal is permitted. Fixed-ambient equilibrium results cannot be applied instantaneously to a rapid heat-wave step unless quasi-static approximation error is justified.

An exact variation-of-constants identity under any bounded power input:
\[
x(t)=e^{A_0t}x(0)+\int_0^t e^{A_0(t-\tau)}v(p(\tau),A_P(\tau),A_E(\tau))\,d\tau,\tag{D1}
\]
where
\[
v=(H(p)/C_w,\;[Q_0+rA_P]/C_o,\;[Q_{\rm ext}+\ell p+sA_E]/C_c)^\top.
\]
This represents heat-wave memory and distinct thermal time scales; it is **not** an independent observed causal propagation law.

## 6. Robust inward-pointing safety enclosure (PROPOSITION 3)

Assume every ambient disturbance satisfies \(A_P(t)\le A_P^+\), \(A_E(t)\le A_E^+\), and delivered charging power \(0\le p(t)\le\bar p\le P_r\). For \(Q_0,Q_{\rm ext}\ge0\) and nondecreasing H, define
\[
\boxed{\begin{aligned}
U_o&=A_P^++\frac{Q_0+H(\bar p)}{r},\\
U_w&=U_o+\frac{H(\bar p)}g,\\
U_c&=A_E^++\frac{Q_{\rm ext}+\ell\bar p}s.
\end{aligned}}\tag{S1}
\]
\(U_i\) are **derived conservative temperature enclosure bounds**, not manufacturer safety limits. If initial \(x(0)\) satisfies \(T_w(0)\le U_w,T_o(0)\le U_o,T_c(0)\le U_c\), then
\(\mathcal K=\{x:T_w\le U_w,T_o\le U_o,T_c\le U_c\}\) is forward invariant **for every admissible ambient realization and any power trajectory within [0,\bar p]**.

**Proof at each upper boundary:** if \(T_w=U_w,T_o\le U_o\), then \(C_w\dot T_w\le H(\bar p)-g(U_w-U_o)=0\). If \(T_o=U_o,T_w\le U_w\), then \(C_o\dot T_o\le Q_0+g(U_w-U_o)-r(U_o-A_P^+)=0\). If \(T_c=U_c\), then \(C_c\dot T_c\le Q_{\rm ext}+\ell\bar p-s(U_c-A_E^+)=0\). Thus the vector field points inward on each boundary, giving forward invariance by standard comparison/invariance arguments (with the Lipschitz assumption); the three-state inequalities do not depend on unmeasured heat transfer from an adjacent charger. □

**Qualification:** Only if credible equipment-specific **limits of the exact represented states** satisfy \(U_w\le T_{w,\max}\), \(U_o\le T_{o,\max}\), \(U_c\le T_{c,\max}\) does this particular enclosure imply those *modeled-state* temperatures remain under those limits. There is no guarantee on an **unmeasured true hotspot**, junction temperature, rated voltage, harmonics, winding insulation, breaker timing, or mobility operations. Enclosure may be overly conservative.

## 7. Constructive, sufficient charging service guarantee under fixed power (PROPOSITION 4)

Service specification: actual departure time \(t_d>0\) [s], DC-port energy \(E_{\rm req}\ge0\) [J]; effective delivered DC energy \(\dot E_{\rm DC}=p(t)\) [W]. Battery stored energy is distinct and may require additional efficiency state. Define a **chosen constant dispatch power** \(p_0\in[0,P_r]\), not the necessarily saturated p from M1; it is feasible only if the controller can command it and vehicle/BMS accepts it throughout [0,\(t_d\)].

Under the ambient bounds and physical assumptions of Proposition 3, calculate \(U_o(p_0),U_w(p_0),U_c(p_0)\) by S1 with \(\bar p=p_0\). Assume:
\[
\boxed{
\begin{cases}
x(0)\le U(p_0)\quad\text{componentwise},\\
U_i(p_0)\le T_{i,\max}\ \text{for each actually validated safety state},\\
p_0\le D_o(U_o(p_0)),\qquad p_0\le D_c(U_c(p_0)),\\
E_{\rm req}\le p_0t_d.
\end{cases}}\tag{S2}
\]
Then commanding constant delivered DC power \(p(t)\equiv p_0\) for the required window is **constructively feasible within this simplified model**: by Proposition 3 temperatures never exceed the bounds; by nonincreasing D and \(T_o\le U_o,T_c\le U_c\) neither power cap forces curtailment; the assumed battery acceptance and control capacity permit p_0, and \(E_{\rm DC}(t_d)=p_0t_d\ge E_{\rm req}\). □

**Why important:** proves existence of at least one thermally safe *model trajectory satisfying the actual DC-port charging obligation*, not merely a stable equilibrium. This is a **sufficient, very restrictive certificate**, NOT a necessary one or complete viability kernel. Failure of S2 does not show service impossible; a time-varying optimal policy or a different enclosure could still succeed. Real vehicle SOC, taper, network voltages and protection conditions require separate verification.

The general **necessary impossibility bound** remains: if \(\int_0^{t_d}\bar p_{\rm adm}(t)\,dt<E_{\rm req}\) for a verified global upper admissible power envelope \(\bar p_{\rm adm}(t)\), the specified DC-port service is impossible. Determining an independent defensible envelope is itself an evidence gate.

## 8. Delay and switching: explicit limitation and counterexample

Stability theorem 2 assumes instantaneous differentiable feedback. The separate delayed linear negative-feedback system
\[
\dot z(t)=-a_0z(t)-k_d z(t-\tau),\quad k_d>a_0>0,\tag{X1}
\]
illustrates why stable instantaneous negative feedback can **lose stability** with sufficiently large latency. Here z is scalar deviation (arbitrary), \(a_0,k_d\) are rates [s^-1], \(\tau\) is delay [s]. Substituting \(z=e^{\lambda t}\) gives the characteristic equation \(\lambda+a_0+k_de^{-\lambda\tau}=0\). Imaginary roots appear at \(\omega=\sqrt{k_d^2-a_0^2}\), \(\tau_*=\arccos(-a_0/k_d)/\omega\). For the explicitly **synthetic** rates \(a_0=1/3600\ \mathrm{s}^{-1}\), \(k_d=3/3600\ \mathrm{s}^{-1}\), the first crossing is \(\tau_*\approx2431.84\,\mathrm{s}\) (40.53 min). This is a *general mathematical caution*, NOT an identified delay of transformer–EVSE equipment or an exact reduction of M2–M4.

Under min ties, relay hysteresis or communications outages, p can be nonsmooth/piecewise mode-dependent. Theorem 2 does not prove stability for arbitrary switching or reset law. Future hybrid analysis must define sensor latency, event priorities, hysteresis, dwell bounds, power electronics interface-specific control laws and thermal-state continuity at modes.

## 9. Observability, identification and validation gates

**Observability conditional statement:** If coefficients \(C_o,g,r,Q_0\) and ambient \(A_P(t)\) are known, the noiseless oil dynamics imply
\[
T_w=T_o+\frac{C_o\dot T_o-Q_0+r(T_o-A_P)}g,\qquad g>0.\tag{O1}
\]
Thus continuous exact oil temperature and known parameters can **in theory reconstruct effective winding state**. In practice differentiation amplifies measurement error; parameters are uncertain; the inferred \(T_w\) remains an **effective** thermal state and cannot be called true winding hotspot. For locally linearized dynamics with y=(To,Tc), observability rank can be 3 when g>0, but local observability does not imply practical identifiability or good parameter precision.

**Structural parameter-identifiability issue:** with only one effective charger temperature, ambient and total AC/DC loss but unknown \(C_c,s,\alpha\), the single charger ODE identifies only ratios \(s/C_c\) and \(\alpha/C_c\) under ideal excitation. Scaling \(C_c,s,\alpha,Q_{\rm ext}\) by the same factor (while maintaining physical alpha range) gives identical trajectories; independent parameter/calorimetric knowledge, fan measurements, additional sensor states, or controlled heat experiments are needed.

**Validated evidence status:**
- Original Gong physical response supports separate **P component** sensitivity under synthetic EV load schedules, not a matched full P–charger heating field test.
- Original Kunlasing physical manual command response supports **control actuation**, not actual oil-temperature threshold triggering or observed transformer thermal consequence of automatic curtailment.
- Original Krama field record supports **charger-side derating**, not matched upstream transformer thermal impact; raw data unavailable and their reported June leave-one-session-out predictive performance is substantially weaker than other sessions.
- Exact current IEEE/IEC normative formulas, safety thresholds and Susa 2005 full original remain **source access gates**.

**Required independent tests for this three-state implementation:** dimension/signed-energy conservation, source-attributed parameter definitions, time-step refinement and analytic Jacobian finite differences in smooth branches, algebraic char polynomial coefficient checks, mode-boundary tests and nonsmooth guard handling, admissible ambient order and enclosure assertions, mission service boundary tests, parameter structural rank, fixed-effect/source control baselines, and eventual paired cross-infrastructure real thermal/electrical observations.

## 10. Audit disposition

**MATHEMATICALLY DERIVED under A1–A5:** equilibrium existence/uniqueness (Theorem 1); negative-real-part three-state Jacobian eigenvalues and local exponential stability at smooth active regions (Theorem 2); upper-box forward invariance (Proposition 3); constructive sufficient *model* charging service under constant controlled DC port power (Proposition 4); comparative equilibrium ambient→power monotonicity; sample delay loss-of-stability caution.

**NUMERICALLY VERIFIED ONLY ON SYNTHETIC PARAMETERS:** bisection equilibrium, three active branches, analytic vs finite-difference J, 3×3 RH coefficient identity, loss and energy cancellation, invariant enclosure inequalities, ambient monotonicity, and an explicitly conditional constant-power feasibility example.

**NOT ESTABLISHED:** stability at nonsmooth ties/delayed controls; actual manufacturer transformer hotspot constraints, charger junction temperatures, physical P-EVSE synchronized causal thermal coupling, true traffic/mobility trip service, independent charger/site validation, parameter estimation from Krama, full current IEEE/IEC compliance, or original research novelty.

Use these results as a **conditional mathematical baseline**, not a full thesis resilience proof.
