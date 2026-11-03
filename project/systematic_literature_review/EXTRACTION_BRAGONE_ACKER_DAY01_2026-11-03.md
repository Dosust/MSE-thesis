# Day 1 — primary-source mathematical extraction: Bragone 2022 and Acker 2025/2026

**Date:** 3 November 2026. **Stage:** targeted high-priority primary-text extraction, **NOT formal systematic-screened inclusion and NOT new independent model replication**.  
**Source basis:** Bragone journal article original accepted version, KTH DiVA open full text; Acker et al. publisher full-text HTML, Springer Nature.  
**Figures:** Bragone original PDF was indexed as searchable text with figure descriptions, but the independent **web PDF screenshot request failed with cache miss**; **figure-specific assertions require visual rerender**. Acker publisher HTML figure descriptions/text read; figures not independently image-audited.  
**Classification:** Bragone C1(primary), C4/C5(secondary), field inputs F3, model predictions F5. Acker C2(primary), C4/C6(secondary), controlled experimental inputs F4 and model F5 with *controller-performance outcomes evaluated in simulation*. Both S3 (equation-text extracted); S4/S5 are NOT claimed.

## Source S01 — Bragone et al., *Physics-informed neural networks for modelling power transformer’s dynamic thermal behaviour*

Citation: Federica Bragone, Kateryna Morozovska, Patrik Hilber, Tor Laneryd, Michele Luvisotto (2022), *Electric Power Systems Research* **211**, 108447. DOI [10.1016/j.epsr.2022.108447](https://doi.org/10.1016/j.epsr.2022.108447). [Open institutional version (PDF)](https://www.diva-portal.org/smash/get/diva2%3A1683236/FULLTEXT01.pdf). Explicitly use journal DOI when citing published record.

### What the authors physically used

Paper sections 2–3: real transformer **ambient temperature**, **top-oil temperature**, and **load factor** from operational field measurements. The illustrated physics estimates a **height-dependent temperature distribution**, not directly measured 3-D oil/winding temperatures throughout the device. Model vertical height normalized/assumed **H = 1 m**, and tested first **100 hours** of data. The study used numerical finite-volume method (FVM) as its field/space temperature-distribution comparator. It did **not** show a supplying EVSE or transport network.

### Governing equations (paper equations 1–3; section 2.1, printed p. 2)

Let \(T(z,t)\) be model temperature along 1-D vertical coordinate \(z\):
\[
k\partial_{zz}T+q=\rho c_p\partial_tT.
\]
The paper uses effective heating/cooling:
\[
q(z,t)=P_0+P_K(t)-h[T(z,t)-T_a(t)],
\quad P_K(t)\sim\mu K(t)^2 .
\]
Boundary conditions in their printed equation (3):
\[
T(0,t)=T_a(t),\qquad T(H,t)=T_o(t).
\]

Here \(P_0\) represents no-load losses, \(\mu\) rated load losses, \(K\) measured relative loading, \(T_a\) ambient and \(T_o\) **measured top-oil** temperature. Paper Table 1 (printed p. 3) reports example assigned numerical values \(k=50\,\mathrm{W/(m\,K)}\), \(c_p=2000\,\mathrm{J/(kg\,K)}\), \(\rho=900\,\mathrm{kg/m^3}\), \(h=1000\,\mathrm{W/(m^2\,K)}\), \(P_0=15000\,\mathrm{W}\), \(\mu=83000\,\mathrm{W}\), \(H=1\,\mathrm{m}\).

**Important mathematical QA before reuse:** Standard volumetric heat equation expects \(q\) in \(\mathrm{W/m^3}\), while published Table 1 gives \(P_0,\mu\) in W and \(h\) in \(\mathrm{W/(m^2 K)}\). The paper uses a **simplified/effective 1-D heating model** with scaled/effective coefficients (authors acknowledge nonphysical height simplification and artificially increased conduction/cooling coefficients). We must establish a consistent volume/surface/length normalization rather than copy the numerical parameters into a separate transformer. Treat this as a **dimensional-reconciliation question**, not a confirmed error in the paper.

### PINN mechanics (paper equations 6–11; section 2.2)

Physics residual:
\[
f_\theta=\rho c_p\partial_t \widehat T_\theta-k\partial_{zz}\widehat T_\theta-[P_0+P_K-h(\widehat T_\theta-T_a)] .
\]
Loss includes boundary/data terms and PDE residual:
\[
\mathrm{MSE}=\mathrm{MSE}_{T}+\mathrm{MSE}_{P_K}+\mathrm{MSE}_{T_a}+\mathrm{MSE}_{f}.
\]
Authors use automatic differentiation, collocation points and the actual time-dependent measurements. **A small PDE loss is conditional on the assumed physics and normalizations.**

### Actual reported validation and limitation (sections 3–4, printed pp. 4–5)

- Compared PINN spatial solution with **FVM numerical solution**, not directly measured full transformer internal temperature distribution.
- Example selected network: 4 hidden layers × 50 neurons, \(N_u=100\) boundary/data samples, \(N_f=10000\) collocation points, first 100 hours; Table 3 relative \(L_2\) spatial-distribution difference vs FVM **1.45e−1**; Table 4 top-oil comparison **2.59e−2** for this model setting. These are **relative norms**, not RMSE degrees Celsius or an independent external asset prediction.
- Conclusion explicitly says that **with available quantity/type of measurements, PINNs could not outperform FVM**; extensive computation time is a disadvantage. Reported optimization time for best selected architecture ~**7285 seconds** on specified laptop.
- Methodological caution: \(\widehat{T}_o\) is evaluated while actual \(T_o(t)\) is imposed at the upper boundary, so a future forecasting comparison needs a prospective forcing/boundary setup; cannot call this independent long-horizon top-oil prediction without checking leakage and boundary admissibility.
- Not a connected EVSE study, not demonstrated external transformer transfer, not extreme-heat field coupling.

**Direct implication for Phelan:** A transformer thermal PINN is **known prior art**. We must replicate an honest physical FVM/ODE baseline, track whether measured top-oil was a boundary during training/testing, distinguish spatial interpolation from forecasting, and evaluate real holdout and parameter identifiability before deciding PINN value.

## Source S18 — Acker, Hofmann & Konrad, *Predictive battery thermal management for fast charging of electric vehicles using nonlinear model predictive control and dynamic programming*

Source: Lukas Acker, Peter Hofmann, Johannes Konrad. Original paper published online **17 December 2025**, journal volume **11 (2026)**, *Automotive and Engine Technology*. DOI [10.1007/s41104-025-00157-7](https://doi.org/10.1007/s41104-025-00157-7). [Publisher full text](https://link.springer.com/article/10.1007/s41104-025-00157-7).

### Actually measured

Section 2: measured **2019 Audi e-tron 55 quattro** (95 kWh pack, max charging 150 kW); battery, coolant and thermal-control signals from OBD-II, road operation, climate-controlled test-bench charging and battery/coolant characterization. The study distinguishes measured vehicle behavior from its subsequent *simulated controller assessment*. It is a **vehicle battery/coolant** model, not charger-rectifier heat or grid transformer heat.

### Electrical and thermal equations (original equations 1–7, sections 3.1–3.2)

Vehicle BMS charging-current acceptance modeled as:
\[
i_{\mathrm{bat}}=f(T_{\mathrm{bat}},\mathrm{SOC}),
\quad
\dot{\mathrm{SOC}}=\frac{i_{\mathrm{bat}}}{C_{\mathrm{bat}}},
\quad
R_{\mathrm{int}}=\frac{U_{\mathrm{bat}}-U_{\mathrm{OC}}}{i_{\mathrm{bat}}}.
\]
The author's sign convention for \(i_{\mathrm{bat}}\) and SOC change must be preserved when adapting.

Simplified irreversible ohmic heat generation:
\[
\dot Q_{\mathrm{loss}}=R_{\mathrm{int}}i_{\mathrm{bat}}^2 .
\]
Coolant exchange and ambient exchange:
\[
\dot Q_{\mathrm{clnt}}=\dot m_{\mathrm{clnt}}c_{\mathrm{clnt}}
(T_{\mathrm{clnt}}^{\mathrm{bat,in}}-T_{\mathrm{clnt}}^{\mathrm{bat,out}}),
\]
\[
\dot Q_{\mathrm{amb}}=h_{\mathrm{air}}A_{\mathrm{bat}}(T_{\mathrm{amb}}-T_{\mathrm{bat}}).
\]
Battery temperature first-law ODE:
\[
m_{\mathrm{bat}}c_{\mathrm{bat}}\dot T_{\mathrm{bat}}
=\dot Q_{\mathrm{loss}}+\dot Q_{\mathrm{clnt}}+\dot Q_{\mathrm{amb}}.
\]
The paper also models coolant volumes, pump flow, compressor/chiller COP, heater and coolant sensor-volume dynamics (equations 8–16), not an exogenous ideal cooling-power input.

### What validation means here

- Section 3.4 describes physical parameter measurements and *particle swarm optimization* calibration for parameters not directly measured; thermal state comparisons include fast charging with ambient **1°C and 35°C** (figures 8–9) in the source.
- Section 4 evaluates proposed optimization via offline dynamic programming + nonlinear MPC. Publisher abstract states this control improvement was assessed **using a validated high-fidelity simulation model**; any controller kWh and charging-time improvements are not automatically measured changes in real-world mobility.
- It includes coolant-inlet/outlet and battery temperature observations with physically defined hardware, unlike generic UDS IDs whose channel semantics are unresolved.

**Direct implication for thesis datasets:** TUM UDS source IDs 1272/1273 are described as battery-pack inlet/outlet temperatures; these are **not independently confirmed coolant inlet/outlet** readings, and TUM does not provide a verified coolant mass-flow or compressor command here. Thus, **do not estimate coolant heat flux \(\dot m c\Delta T\)** from TUM temperature channels without author-confirmed sensor semantics, flow-rate measurements/assumptions and bound validation. The article is a direct advanced EV battery-physics precedent (C2/C4), not same-site power–transport coupling.

## Joint evidence and novelty boundary

| Proposed thesis claim | Prior art shows | Still unproven here |
|---|---|---|
| Transformer thermal PINN is a new idea | **False:** Bragone 2022 already demonstrates it | No novelty just from adopting PINN |
| Measured vehicle battery/coolant first-law dynamics already studied | **Yes:** Acker measured/parameterized a battery/coolant model | New coupling to site transformer/EVSE power/thermal states, sensor/asset transferability and P↔T interactions |
| Physical cross-subsystem thermal coupling is validated by combining these papers | **No:** unrelated equipment and tests | Actual connected transformer–EVSE thermal controls/time response and service effects |
| General heat-transfer coefficients can be reused directly | **No:** site/equipment/calibration dependent | Identifiability, original dimensions, valid source parameters, independent equipment testing |

## Follow-up verification tasks (do not claim done)

1. Inspect Bragone original PDF printed pp. 2–5 figures 1–5 visually; the web screenshot endpoint returned cache miss. Verify exact spatial-loss normalization/dimensional consistency, boundary data and independent evaluation setup before reproduction.
2. Download publisher-compatible equations and parameter/validation figures for Acker; verify controls and holdout design, whether test measurements were separate from fitting, detailed per-test errors.
3. Populate formal source-screening and extraction templates **only after** the database-native search corpus is registered and pilot records are matched by DOI.
4. Compare against RACE thermal ODE/FVM and SINTEF original measured transformer top-oil. Do not equate a measured boundary with an unseen state.

**No new computational validation, full PRISMA screen, experimental data acquisition or independent reproduction was performed in this extraction.**
