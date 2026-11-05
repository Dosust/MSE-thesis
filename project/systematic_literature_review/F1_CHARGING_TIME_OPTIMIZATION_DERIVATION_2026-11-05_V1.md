# F1 extension — Optimal EV charging time from transformer thermal aging (candidate derivation)
**Date:** 2026-11-05  
**Status:** proposed mathematical extension, NOT an original-paper algorithm reproduction; NOT NOVELTY VERIFIED; NOT FIELD VALIDATED; NOT final thesis formulation.  
**Thesis scope:** thermal power ↔ electrified transport under extreme heat, SO1–SO3 unchanged.

## Source-specific attribution
Qian, K., Zhou, C. & Yuan, Y. (2015), *Impacts of high penetration level of fully electric vehicles charging loads on the thermal ageing of power transformers*, IJEPES 65:102–112, DOI 10.1016/j.ijepes.2014.09.040. Author's manuscript https://researchonline.gcu.ac.uk/ws/files/6078356/FEV_transformer_paper_IJEPS2014oct.pdf. Original source §II models uncertain initial SOC, start times and charging modes; §IV Scenario C at printed p. 8 says **real-time electricity prices** determine economic start time and smart charging shifts load toward valley hours. The conclusion says the method **can be applied** to determine optimum charging times as a function of existing loads and ambient temperature. **Do not misrepresent this as proof that the paper solved the general stochastic thermally constrained joint service/aging optimization formulated below.**

**Direct role:** Use the paper's EV-load distribution → transformer electrical loading → HST → thermal aging chain as a physical benchmark, with existing loads and weather as explicit inputs.
**Implicit role (derived inference):** Thermal inertia makes present-day optimal start time state dependent: transformer initial temperature and recent charging history matter as well as ambient and instantaneous base-load troughs. Nighttime is not always optimal; deferment may miss mobility deadlines. Feedback power→transport is conditional on actual permissible grid/EVSE controls, not automatically observed.
**New candidate problem (our derivation, not guaranteed novel):** optimize charging times/powers against HST-driven aging and departure energy deficits with stochastic ambient/load/arrival conditions, equipment-specific temperature constraints, and dynamic service consequences.

## Physically constrained candidate discrete-time model
Time steps k=0,…,K−1, duration Δt; vehicles i=1,…,n; scenario ω. Let p_{i,k}(ω) be grid-side delivered charging power, a_i(ω) arrival time, d_i(ω) departure, E_i battery usable energy, η_i charging efficiency, s_{i,k} SOC, and E_i^{req} required energy at departure. Charging decisions must be nonanticipative in real-time use (depending only on observed history, not future realized weather/arrivals).

\[
P_{EV,k}(\omega)=\sum_i p_{i,k}(\omega),\qquad
P_{net,k}=P_{base,k}+P_{EV,k}.
\]
A measured or solved electrical relation maps `P_net,k, Q_net,k, V_k` and topology to `I_tr,k`. Under verified balanced three-phase assumptions `I_tr,k≈sqrt(P_net,k²+Q_net,k²)/(sqrt(3) V_LL,k)`; otherwise use source-appropriate power flow and phases.

A phenomenological first-order candidate thermal recursion (NOT universal transformer physics) is
\[
T_{H,k+1}=aT_{H,k}+(1-a)T_{a,k}+bI_{tr,k}^2+c_k,
\quad 0<a<1,\ b\ge0,
\]
with `c_k` standing for qualified constant/auxiliary heat inputs if physically justified. Prefer a properly parameterized two-state oil/winding transformer thermal model/standard for final physics; calibrate against observed HST and verify identifiability. Real HST may differ from a point sensor named HST.

Aging equation following cited model (verify applicable reference temperature, insulation type and standard):
\[
F_{AA}(T_H)=\exp\!\left(\frac{15000}{383}-\frac{15000}{T_H+273}\right),\quad
L=\Delta t\sum_{k=1}^{K}F_{AA}(T_{H,k}).
\]
L is equivalent accelerated insulation-aging *time* (if Δt hours, units hours), not direct failure probability or physical years left.

Vehicle dynamics and constraints:
\[
s_{i,k+1}=s_{i,k}+\frac{\eta_i\Delta t}{E_i}p_{i,k},\quad
0\le p_{i,k}\le \bar p_{i,k}\mathbf1\{a_i\le k<d_i\},
\]
\[
U_i=E_i[\,s_i^{target}-s_{i,d_i}\,]_+\quad\text{(kWh unmet at departure)}.
\]
SOC saturation, taper/thermal power limits, initial SOC and EVSE-specific charger/electric losses must be added as equipment evidence permits.

Proposed objective (units consistent via conversion penalty λ):
\[
\min_{\pi\ \mathrm{nonanticipative}}\quad
\mathbb E_\omega\!\left[
\Delta t\sum_{k=1}^{K}F_{AA}(T_{H,k}(\omega))
+\lambda\sum_i U_i(\omega)
\right]
\]
subject to transformer ratings and physical temperature bounds (equipment specific), network electrical constraints and charging availability/deadlines. Alternative: impose `U_i=0` as hard deadline feasibility and minimize aging; run a Pareto analysis instead of asserting an arbitrary λ. Optional risk constraints, only when quantified: `Pr(max_k T_H,k>T_lim)≤ε`. The nature of the thermal limit (manufacturer/utility setting/protection) must be justified.

## Mathematical derivative: why optimum time depends on thermal memory
With the stated **one-state simplification**, fixed external inputs and a locally differentiable current `I_k(P_{net,k})`, a small increment in charging at time j changes a later HST by
\[
\frac{\partial T_{H,m}}{\partial p_{i,j}}=
2b\,I_{tr,j}\frac{\partial I_{tr,j}}{\partial P_{EV,j}}\,a^{m-j-1},
\qquad m\ge j+1.
\]
The aging-factor derivative is
\[
\frac{dF_{AA}}{dT_H}=F_{AA}(T_H)\frac{15000}{(T_H+273)^2}>0.
\]
Therefore the local marginal aging impact of **additional power in time slot j** is
\[
\boxed{\frac{\partial L}{\partial p_{i,j}}=
2bI_{tr,j}\frac{\partial I_{tr,j}}{\partial P_{EV,j}}
\,\Delta t\sum_{m=j+1}^{K}
F_{AA}(T_{H,m})\frac{15000}{(T_{H,m}+273)^2}
a^{m-j-1}}
\]
for this simplified recursion, disregarding feedback of p on later P/schedules and any control coupling. Positive for ordinary importing I, showing current forcing and future thermal memory. If network flow has nonlinearities or reverse flow, derivative sign and impacts must be computed from actual power flow. With energy equivalence for shifting p from slot j to l, unconstrained local optimal scheduling tends to reduce high **marginal thermal aging cost** slots and use lower ones, constrained by charging deadlines and mobility loss. **Instantaneous lowest base load is not guaranteed optimal** due to ambient, prior HST, thermal inertia, cooling and feasible mobility windows. This expression is a candidate sensitivity derivation, **not present as such in Qian 2015 and not yet empirically validated**.

## Direct measurement and validation gates
- Calibrate transformer model with measured component HST and loading on safe chronological split. Existing SINTEF report uses 8,589 HV and LV HST sensor-named rows per channel; verify sensor mapping, units and validity and note observed ambient only to +25.97 °C.
- Validate EV request/departure distributions and any connections/control. With no synchronized connected transformer↔EVSE field heat/control data, output is a **physics-based coupled scenario**, not observed causal control feedback.
- Compare against uncontrolled, off-peak, price-optimized, aging-only and joint aging/service policies under identical scenarios; assess accuracy, physical constraint violations, aged-equivalent hours, unmet energy (kWh), critical times/delays, uncertainties and computational cost. PINN remains conditional alternate modeling method, not a replacement for physics or a new metric by itself.
- Model predictive control, recourse and nonanticipativity must be justified for real-time claims; stochastic look-ahead with realized future input information is only a perfect-information oracle reference.

## Novelty falsification required
This scheduling–aging concept has already been extended in prior studies. Examples:
- Diahovchenko (2024), *Analyzing the influence of electric vehicle charging scheduling on distribution transformer lifespan*, Heliyon 10:e39904, DOI https://doi.org/10.1016/j.heliyon.2024.e39904: charging schedules, transformer aging, ambient and power quality with fuzzy logic, mostly simulation.
- Nie et al. (2026), *Multi-objective optimization of distribution transformer degradation and consumer profit in the presence of electric vehicles*, Electric Power Systems Research 253:112522, DOI https://doi.org/10.1016/j.epsr.2025.112522: jointly transformer aging and EV profit with centralized scheduling. Do NOT claim "first aging-aware charging optimization".
- Further compare to prior thermo-electrical EVSE derating, dynamic rating, network coupled feedback and stochastic viability papers before selecting a novelty claim.

**Status:** Important candidate control/optimization derivation downstream of F1; formal choice depends on SO relevance, reviewer-screened systematic evidence, verified source parameters, available observations and supervisor.
