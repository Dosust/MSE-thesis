# Reduced coupled electrothermal model — equilibrium uniqueness, local stability and service tradeoff

**Date:** 2026-10-17. **Mathematical status:** Two proposed results derived/proved *conditional on explicit idealized assumptions*. These are NOT attributed as results proved by Gong (2015), Kunlasing (2022) or Krama (2026), are NOT a novelty verdict, and are NOT a validated field model. See parent COUPLED_ELECTROTHERMAL_HYBRID_MODEL_V0.md for general two-node transformer, charger and DAE/hybrid formulation. The scalar-transformer reduced model here is a tractable mathematical **submodel**, not a replacement for the fuller engineering architecture.

## A. Evidence discipline and equipment boundary

- Gong et al. (2015), original IEEE 9p DOI 10.1109/TSG.2014.2365452: direct top-oil / top-winding **P transformer** response under emulated EV charging schedules; true hotspot not observed, working EVSE not instrumented in that same experiment. Gong's numbered Eq. (1) is load forecasting, not a transformer heat ODE.
- Kunlasing et al. (2022), original IEEE 4p DOI 10.1109/ECTI-CON54298.2022.9795360: transformer PT100 oil monitoring and separately manually commanded Zigbee-to-IEC61851 charger pilot current limitation on two EVs; no demonstrated **oil temperature -> automatic charging command**; three-EV automatic case is simulated.
- Krama et al. (2026), original Elsevier 16p DOI 10.1016/j.ecmx.2026.101960: field observed EVSE rectifier proxy temperature, offered/delivered charger power and derating, but no upstream utility transformer matched temperature response. Original row-level dataset remains unreceived.
- A hypothetical transformer-temperature-conditioned power cap is a modeling **assumption** for this submodel, distinct from Kunlasing's physical overload-control demonstration and the documented earlier heat-aware charging optimization prior art. Neither thermal exchange between remote enclosures nor direct temperature causal field validation is inferred.

## B. Simplifying assumptions (A1–A9)

A1. One **effective transformer thermal state** T_P (K or °C for additive differences), one **effective charger thermal state** T_E; fixed separate local ambients A_P,A_E. T_P is NOT declared true winding hotspot and T_E is NOT semiconductor junction.
A2. Two thermal capacitances C_P,C_E > 0 [J/K]; effective ambient heat conductances G_P,G_E > 0 [W/K], all constant.
A3. Transformer has a constant independent heat term Q_0 >= 0 [W] and phase-equivalent copper heat H(P). Transformer base real demand P_b >= 0 [W], unchanged within the local theorem. Constant balanced three-phase voltage V_LL > 0 [V], unity power factor, no significant harmonic/unbalance effects and constant positive per-phase equivalent resistance R_eq [ohm].
A4. 0 < eta <= 1 is constant overall AC/DC conversion efficiency; P_AC=P/eta where P [W] is **delivered DC power at charger output**, which equals available capped demand only under sufficient vehicle energy acceptance. The charger thermal effective compartment receives a fixed fraction 0 <= alpha <= 1 of modeled whole-charger electrical losses. Define ell = alpha(eta^-1 - 1) >= 0.
A5. Charger external heating Q_ext [W] is constant, nonnegative for the tested equations, not a measured solar-heat forcing.
A6. An operating controller is assumed to cap delivered DC power instantaneously by nonnegative, continuous, *nonincreasing* thermal capability functions D_P(T_P) and D_E(T_E) [W], both bounded by P_rated [W]. D_P is hypothetical equipment-specific available-DC power after appropriate grid AC/DC conversion. This assumes actual control authority, which cannot be concluded from source data. No delayed messages, discrete hysteresis, battery taper, or communication faults.
A7. The charger has sufficient vehicle/BMS demand to absorb P up to these limits; otherwise battery acceptance B(SOC,T_b,t) must enter the min and the stated equilibrium theorem is inapplicable as written if demand is time-varying.
A8. H(P) = k(P_b+P/eta)^2 [W], k=R_eq/V_LL^2 [W^-1] under the balanced, unity-PF, constant-V equivalent; any AC-side feeder/transformer heat accounting is allocated once.
A9. For the *local linearization only*, both D functions are continuously differentiable on the current active smooth regime. The actual min law is nonsmooth at ties/saturation boundaries and cannot be globally differentiated there.

## C. Reduced continuous dynamical system

For P(T_P,T_E) = min{P_rated,D_P(T_P),D_E(T_E)} [W], define

(R1) C_P dT_P/dt = Q_0 + H(P) - G_P (T_P-A_P).

(R2) C_E dT_E/dt = Q_ext + ell P - G_E (T_E-A_E).

(R3) H(P) = k (P_b+P/eta)^2, k=R_eq/V_LL^2.

Temperatures A_P and A_E are allowed to differ. **No direct term proportional to (T_P-T_E) is included**, because the transformer and charger do not have evidence of thermal conduction between enclosures. The coupling occurs only through instantaneous electrical power and explicitly assumed control.

**Units:** C_i dotT_i=(J K^-1)(K s^-1)=W; H and Q terms W; G_i(T_i-A_i)=(W K^-1)K=W. H'(P) is dimensionless W/W; -partial P/partial T_i is W/K. The model excludes reactive/harmonic power-flow phenomena by A3 rather than silently converting var/THD into heat.

## D. Existence and uniqueness of operating equilibrium (PROPOSITION 1)

**Statement.** Under A1–A8, with D_P,D_E continuous and nonincreasing in their respective temperature argument, the reduced system has **exactly one equilibrium** (T_P*,T_E*,P*) with 0<=P*<=P_rated.

**Proof.** At equilibrium, for each candidate scalar P in [0,P_rated], R1–R2 yield unique temperatures

T_P(P) = A_P + [Q_0+H(P)]/G_P,
T_E(P) = A_E + [Q_ext+ell P]/G_E.

Because P_b>=0, k>=0, eta>0, H(P) is nondecreasing over P>=0; hence T_P(P) and T_E(P) are nondecreasing. With D_P,D_E nonincreasing, the map

L(P) = min{P_rated, D_P(T_P(P)),D_E(T_E(P))}

is continuous, nonincreasing, and maps [0,P_rated] into itself. Define F(P)=P-L(P). Since F(0)=-L(0)<=0 and F(P_rated)=P_rated-L(P_rated)>=0, the intermediate value theorem gives a root P*. For 0<=P1<P2<=P_rated, monotonicity implies
F(P2)-F(P1)=(P2-P1)-[L(P2)-L(P1)] >= P2-P1>0.
Thus F is strictly increasing and can have only one root. T_P(P*),T_E(P*) are uniquely determined. QED.

**Theorem scope:** equilibrium uniqueness does **not** imply equipment safety, correct service, global asymptotic stability, or validation. Physical relevance still needs identification of each thermal state and actual control curves.

## E. Local exponential stability on differentiable regimes (PROPOSITION 2)

Define a=-partial P/partial T_P >=0 and b=-partial P/partial T_E >=0 on the smooth active operating branch; h=H'(P*)>=0 and ell>=0. At any equilibrium satisfying the differentiability assumption, linearization in ordered states (T_P,T_E) gives

J =
[ -(G_P + h a)/C_P       -h b/C_P
  -ell a/C_E              -(G_E+ell b)/C_E ].

The trace is

tr J = -(G_P+h a)/C_P -(G_E+ell b)/C_E < 0.

The determinant is

det J = [(G_P+h a)(G_E+ell b)-h ell ab]/(C_P C_E)
      = [G_P G_E+G_P ell b+G_E h a]/(C_P C_E) > 0.

The cancellation of h ell ab is an exact rank-one coupling identity. For a real 2x2 matrix, negative trace and positive determinant imply both eigenvalues have strictly negative real parts. Local exponential stability follows from the standard linearization theorem for a continuously differentiable autonomous ODE. QED.

**Branch semantics:** under a literal min law with a strict unique active charger limit, a=0 and b=-D_E'(T_E)>=0; on the unique active transformer limit, b=0 and a=-D_P'(T_P)>=0. A differentiable general cap that depends on both states can also satisfy a,b>=0 (not asserted to have been measured). At min ties/clip thresholds the Jacobian may not exist; both propositions must be kept distinct (equilibrium uniqueness still applies under mere continuity). Stability under switching, transport delays, changing ambient, nonlinear losses, energy storage, hysteresis, controller faults and electrical-DAE bifurcation is NOT proved.

A further mathematically relevant statement follows if D_P,D_E are globally Lipschitz: P=min of bounded Lipschitz functions is Lipschitz, H on the bounded P interval is Lipschitz, and the RHS of R1–R2 is globally Lipschitz in the two temperature states. Thus the initial-value problem has a unique forward solution for every finite initial state; bounded P and constant ambient/heat terms make temperatures bounded for t>=0 by stable linear heat equations with bounded forcing. This is **solution existence and boundedness**, not global convergence to the unique equilibrium.

## F. Conditional protection-versus-charging tradeoff (COROLLARY)

When the charger-thermal bound is uniquely active, P=D_E(T_E), D_E'(T_E)<=0. Holding the other inputs fixed, instantaneous transformer heat has derivative

dH/dT_E = H'(P) D_E'(T_E) <= 0,

while instantaneous available DC power decreases or remains unchanged:
dP/dT_E=D_E'(T_E)<=0.

Thus a hotter charger can **reduce instantaneous transformer copper heating while also reducing instantaneous charging power** under A3–A8. The physical transformer temperature responds over its own thermal time, not instantaneously. Delayed unmet charging energy, later charge rebounds, time-varying non-EV demand, changing efficiency or harmonic losses can change the horizon-level transformer temperature/ageing effect; **no global net temperature or service sign is inferred**.

## G. Equipment safety vs service viability

At the unique equilibrium, separately evaluate actual equipment operating limits, e.g. T_P*<=T_P,max and T_E*<=T_E,max **only if** these T states represent the safety-rated sensor/thermal quantity correctly. Stable but overheated equilibria are possible; base load alone might violate transformer safety even for P*=0.

Let E_DC(t_d)=int_0^{t_d}P(t)dt be delivered DC energy, not necessarily stored battery energy. An admissible charging mission with actual requirement E_req has necessary condition E_req<=int_0^{t_d}P_bar(t)dt for a proved power envelope. If the model is *already at steady equilibrium* and remains fixed with no battery taper, E_DC(t_d)=P*t_d. Actual transient thermal adaptation, SOC taper and mode transitions invalidate the steady shortcut. For realistic critical service, define actual deadline and energy request, then solve a finite-horizon constrained reach-avoid/viability problem; neither Gong/Kunlasing/Krama provides joint observed service requirements and P-E thermal states.

## H. Reproducible synthetic numerical verification

A standalone Python 3 verifier tests three cases with *arbitrary toy parameters* (charger-limited, transformer-restricted, rated) by scalar bisection for equilibrium P*, checks analytic 2x2 Jacobian against finite differences, checks trace/determinant signs and exact AC/DC accounting. Computations **do not** fit any paper or calculate transformer ratings.

Illustrative numerical outputs of the synthetic verifier, W and °C:
- Charger limit active: P*=22580.071 W, T_P*=71.036°C, T_E*=72.420°C.
- Transformer limit active: P*=8177.897 W, T_P*=79.456°C, T_E*=33.120°C.
- Rated branch: P*=30000.000 W, T_P*=60.572°C, T_E*=49.787°C.

These temperatures and limits are NOT Gong/Kunlasing/Krama measurements, not physical predictions, and not asserted safe. They serve only to catch algebraic and implementation mistakes in the idealized model.

## I. Research next gates

1. Original Susa 2005 IEEE dynamic heat equations and current IEEE/IEC standards full text: inspect lawful originals before standards-based implementation and compare to proposed effective heat balance. Existing PR97 marks them unverified.
2. Extend the 1-node P proof to the actual two-node (oil/winding) + charger **three-state** model with explicit sensor/temperature mappings, then include electrical constraints (not just fixed V and PF). Stabilizing signs in this toy do not transfer automatically.
3. Include distinct P electrical overload control vs hypothetical P temperature action; mark Kunlasing's manually triggered real charger commands separately from its three-EV simulated closed-loop result.
4. Analyze realistic delayed/hysteretic switching or hybrid modes and service objectives. Prove stability only if hypotheses hold; use counterexamples when they fail.
5. Acquire Krama raw 1-min power/5-min rectifier records; test charger baseline parameters/structural identifiability; obtain paired transformer-utility and charger time-series for cross-system validation or remain at source-bounded hypothetical demonstration.
6. Continue remaining 22 priority fulltext acquisitions and global prior-art audit. Do not claim mathematical novelty or validated physics solely because the proposition is newly written for this thesis.

**Proven/verified in this memo:** propositions 1–2 and conditional local power/heating tradeoff under A1–A9, consistency checks on a synthetic example. **Not established:** general coupled three-state stability, formal robust viability kernel, spatial PDE, parameter identification, real thermal causal transfer, service-field validation or novel prior-art boundary.
