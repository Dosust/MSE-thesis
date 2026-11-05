# F1 — Three driver factors for EV-related transformer thermal aging: evidence-to-assumption register

**Date:** 2026-11-05  
**Status:** RESEARCHER-SELECTED EVIDENCE-BASED STARTING POINT; assumptions to be tested, NOT validated site-specific findings, NOT final model, NOT supervisor approval.  
**Thesis:** Engineering of Power–Electrified Transportation Interdependencies for Resilience. Scope limited to thermally conditioned power ↔ electrified road transportation and active SO1–SO3.

## Primary-source provenance
Qian, K.; Zhou, C.; Yuan, Y. (2015). *Impacts of high penetration level of fully electric vehicles charging loads on the thermal ageing of power transformers*. *International Journal of Electrical Power & Energy Systems*, 65, 102–112. https://doi.org/10.1016/j.ijepes.2014.09.040. Journal online version 2014; use 2015 volume citation. University author's manuscript: https://researchonline.gcu.ac.uk/ws/files/6078356/FEV_transformer_paper_IJEPS2014oct.pdf. Publisher/abstract: https://www.sciencedirect.com/science/article/abs/pii/S0142061514005912.

**What the paper says:** Within its UK generic low-voltage distribution-system **model and scenarios**, ambient temperature, fully electric vehicle (FEV) penetration level and EV charging start time are the main factors impacting modeled distribution-transformer life expectancy. The authors also explicitly model stochastic initial battery state-of-charge (SOC), charging modes and starting times, using actual input base-load and ambient records and simulated EV charge/aging response. Smart charging showed favorable modeled life-consumption reduction in its studied scenarios. This is **model-based prior art**, not independent field-observed universal factor ranking.

## Variable dictionary and mechanistic qualification
| Symbol | Variable | Status in proposed model | Physical path | Unit/observation |
|---|---|---|---|---|
| T_a(t,ω) | Ambient air temperature | External forcing; random time series or measured scenario | Heat exchange, top-oil/winding HST | °C; original weather observations in source study |
| ρ_EV | EV penetration fraction | Scenario/penetration parameter; **define exact population denominator** | Determines number of EV charging requests, not automatically simultaneity | 0–1 or %; penetration scenario |
| τ_i(ω) | Vehicle plug-in/charging start time | Random per-vehicle input or decision variable under controlled smart charging | Coincidence with base load and other charging | time/date or time-of-day; source distribution to verify |
| s_i0(ω) | Initial battery SOC | Random state | Determines required energy/duration | dimensionless 0–1 |
| m_i(ω) | Charging mode/type | Vehicle/charger categorical parameter | Available power, charging curve, converter loss | mode; equipment-specific kW |
| P_b(t) | Base (non-EV) electrical load | Measured/qualified operating input | Coincident transformer current / copper losses | kW and reactive power as relevant |
| θ_tr | Transformer thermal/rating parameters | Asset-specific physical parameters with uncertainty | Losses, cooling, thermal inertia, allowable limit | units by parameter; **not interchangeable across assets** |
| u_c(t) | Charging schedule/curtailment policy | Decision/control assumption | Charging coincidence, feedback power → transport | bounded charging power kW |
| T_H(t,ω) | Winding hotspot or qualified sensor approximation | Physical state/model output | Drives thermal aging and possible limits | °C |
| F_AA(t,ω), L(ω) | Accelerated aging factor and equivalent aging time | **Model-derived consequence metrics**, not direct observed lifetime | Nonlinear functional of HST | dimensionless and equivalent hours |

## Proposed testable, explicitly conditional hypotheses
- **H1 (ambient, ceteris paribus):** Under fixed load, comparable cooling, thermal parameters and control conditions, warmer ambient forcing may increase HST and estimated thermal aging. Evaluate gradient and nonlinear effects; hotter ambient does not independently identify cause from unadjusted field correlation.
- **H2 (penetration):** Higher EV penetration can increase expected coincident transformer current and aging **only to the extent it translates into additional delivered charging load**. Test scenarios with the same base load/weather and distinct EV count/demand; smart charging and charging-location shifts can alter results.
- **H3 (start-time coincidence):** Charging start-time distributions alter overlap with base demand and ambient peaks. The favorable shift is **case-specific**, not universally night/day; compare schedules at equal energy-service requirements.
- **H4 (interactions):** Ambient × penetration × timing may create nonlinear thresholds/aging amplification. Test interactions and uncertainty rather than presupposing dominance order.
- **H5 (SOC/mode controls):** Initial SOC, charger class, charging taper/efficiency and base load are required covariates; not every influential input was ranked 'main' in this source.

## Proposed minimal mathematical structure (ours, NOT copied verbatim from paper)
For scenario ω:
\[
P_{EV}^{req}(t,\omega)=\sum_{i=1}^{N(\rho_{EV},\omega)}p_i^{req}(t;\tau_i,s_{i0},m_i,\omega).
\]
\[
P_{net}(t,\omega)=P_b(t,\omega)+P_{EV}^{del}(t,\omega),\quad
I_{tr}(t,\omega)=\mathcal G(P_{net},Q_{net},V,\text{topology}).
\]
Using an appropriate equipment-qualified thermal ODE/standard model:
\[
T_H(t,\omega)=T_a(t,\omega)+\Delta T_{TO}(t,\omega)+\Delta T_{H|TO}(t,\omega).
\]
Adopted reference IEEE-style aging factor from Qian 2015, subject to applicability and exact original equations/units:
\[
F_{AA}(t,\omega)=\exp\left[\frac{15000}{383}-\frac{15000}{T_H(t,\omega)+273}\right],
\qquad
L(\omega)=\int_0^H F_{AA}(t,\omega)\,dt.
\]
This integrates equivalent accelerated *aging time* (if t in hours, L in equivalent hours), **not directly observed years of life or absolute lifespan**. Nominal life, insulation chemistry, aging reference and standard edition are explicit separate parameters if a percentage of life consumed is reported.

Summarize as a model-functional relationship:
\[
L=\mathcal F[T_a,\rho_{EV},\{\tau_i\},\{s_{i0}\},\{m_i\},P_b,\theta_{tr},u_c].
\]
The ranking of effects is **to be estimated for specified physical operating conditions**, not stipulated in advance.

## Identification, design and verification gates
1. Separate **source findings** (Qian UK model-based factor ranking) from **our candidate hypotheses** (H1–H5) and actual validated test results (none for this new model).
2. Define ρ_EV denominator and the physical transformer–charger topology; distinguish EV *penetration* from actual coincident kW delivered.
3. Create matched scenario or factorial design varying T_a, EV penetration, charging timing and interactions, while tracking base demand, SOC, charging mode, feeder, cooling and power factor. Preserve joint probabilities if inputs correlated.
4. Report effects relative to baseline: ΔE[L], ΔHST peak, probability of threshold exceedance and sensitivity indices **with uncertainty**, not just regression correlation or a universal top-three claim.
5. Anchor component-model validation to observed SINTEF HST-labelled channels after sensor semantics QA; Norwegian ambient range **-19.58°C to +25.97°C**, so no independent extreme-hot-climate validation outside data.
6. The existing F1 source establishes **T→P** (EV load → transformer heat → aging); an actual **P→T** restriction requires verified transformer limits/protection and charger-control/service evidence. If absent, report P→T feedback and service consequences as **physics-based scenario simulation**.
7. Maintain PINN only as conditional methodological benchmark, compared fairly with conventional thermal ODE/standards; neither PINN nor HST RMSE nor aging alone demonstrates observed bidirectional interdependency.
8. Submit these source-derived candidate assumptions through the ongoing JBI review extraction, with human-reviewer source eligibility still pending.

## Pending decisions
- Precise charging penetration denominator and scenario distributions.
- Direct measured-versus-simulated asset constraints; transformer type, cooling and ambient time resolution.
- Whether factor importance changes after additional prior art and formal sensitivity analysis.
- Final selection of SO1–SO3 metrics and supervisor review.

**Related:** `STOCHASTIC_EV_TRANSFORMER_COUPLED_FORMULATION_CANDIDATE_F1_2026-11-05.md`; `PRIMARY_EXTRACTION_QIAN_ZHOU_YUAN_2015_2026-11-05.md`; `HST_CANDIDATE_METRIC_DECISION_2026-11-05_V1.md`; `PINN_COMPARATIVE_BENCHMARK_CANDIDATE_2026-11-05_V1.md`. All previous records remain unchanged.
