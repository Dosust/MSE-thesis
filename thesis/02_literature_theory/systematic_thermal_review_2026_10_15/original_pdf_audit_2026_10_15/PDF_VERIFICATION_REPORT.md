# First original-paper verification — rigorously bounded audit

**Executed:** 2026-10-15  
**Control:** Current thermal-only Power System (P) ↔ Electrified Transportation System (T_e) SO1–SO3  
**Systematic-review status:** NOT SCREENED; only prioritized full-text evidence verification, independent of PRISMA selection.

## Executive evidence result
Three primary scholarly PDF artifacts were **opened and read** through the accessible PDF text viewer. Equation numbers, result sections, captions and numerical tables were inspected in text. Attempted page-image renders/screenshot of figure pixels returned cache/fetch errors. Therefore **no graphical figure was visually verified**. Original files were not saved in the GitHub repository; these links point to the official/open research sources. No copyrighted full text is reproduced here.

| ID | Original accessible artifact | Source pages | Evidence-verification status |
| --- | --- | ---: | --- |
| P002 Blomgren et al. 2023 | [DTU Orbit publisher version](https://backend.orbit.dtu.dk/ws/portalfiles/portal/320475870/1_s2.0_S2352467723000565_main.pdf) | 15 (including cover) | Original-PDF text, table captions, equations and validation section inspected |
| P003 Bragone et al. 2022 | [DiVA Portal publisher version](https://www.diva-portal.org/smash/get/diva2:1683236/FULLTEXT01.pdf) | 7 (including cover) | Original-PDF text, equations, table/figure captions and method comparison inspected |
| P007 Balogun et al. | [arXiv 2401.04705v1 author manuscript](https://arxiv.org/pdf/2401.04705) | 13 | Author-manuscript PDF text, governing equations, tabular simulated outputs inspected; **journal version NOT verified equivalent** |

See [CLAIM_EQUATION_REGISTER.csv](CLAIM_EQUATION_REGISTER.csv) for **19 individually anchored claims**; [ALL_CANDIDATE_ACCESS_STATUS.csv](ALL_CANDIDATE_ACCESS_STATUS.csv) covers all 15 pilot leads without claiming 15 PDFs reviewed.

## 1. P002 — Blomgren et al. (2023): grey-box transformer model

**Paper:** *Grey-box modeling for hot-spot temperature prediction of oil-immersed transformers in power distribution networks*. DOI [10.1016/j.segan.2023.101048](https://doi.org/10.1016/j.segan.2023.101048).

### Governing mathematics
Continuous-discrete linear stochastic state-space Eqs (1)-(2), journal p.5 (PDF p.6):

```math
dX_t = (A X_t + B u_t)\,dt + \Sigma\,dW_t,
\qquad y_k=C X_k+e_k.
```

Physics-motivated RC thermal balances then receive input heat loss and ambient heat exchange. In a one-state example, Eq. (7) journal p.7 (PDF p.8) can be paraphrased as

```math
\frac{dT_i}{dt}=\frac{\Phi_h+(T_a-T_i)/R_{ia}}{C_i}.
```

**Physics meaning:** resistance/capacitance thermal network, load-current heating, ambient heat exchange. It is **not a first-principles full oil-flow/winding spatially resolved PDE**.

### What was experimentally observed
Section 3 and Table 1, PDF p.5: two three-phase 10/0.4 kV distribution transformers (400 and 200 kVA), both on actual Danish low-voltage feeders; voltage/current/phase-neutral load, transformer lid/radiator, enclosure temperature and ambient weather. Initial electrical meter acquisition at 1 s filtered to 30 min; meteorological data at 10 min filtered to 30 min. November 2021 data chosen for training and testing (about 80/20 split). Both feeders had approximately five to ten EV-owning customers; **however the model does not separately observe charge-station heat, charging-session load or vehicle travel service**.

### What was validated and what was NOT
Main reported target is transformer **lid temperature** `T_lid`, which the paper itself distinguishes from internal winding hottest-spot `T_HS`. Cross-correlation yields approximately 2.5±0.75 h (400kVA) and 1.75±0.5 h (200kVA) lags from aggregate current-squared to lid-temperature response (Sec.4.4, PDF pp.9-10). These are **intra-transformer aggregate-load thermal delays**, not measured cross-sector P/T propagation. Independent holdout and model-order residual checks support its component-level temperature forecasts, with six-hour-ahead MAE reported about 0.4–0.6°C and predictive intervals (Fig. 8, 10, 11 captions; PDF pp.10-13). The paper explicitly recommends direct optical winding thermal validation for an improved hot-spot interpretation (Sec.5.4 and 6.1, PDF pp.12,14). Authors explicitly have no permission to release experiment time series (Data availability PDF p.14).

**Thesis consequence:** strong grey-box identification, uncertainty and response-lag precedent, but not matched EV charging heat -> transformer field validation and not an independently established winding-hot-spot uncertainty guarantee.

## 2. P003 — Bragone et al. (2022): transformer PINN with FVM benchmark

**Paper:** *Physics-informed neural networks for modelling power transformer's dynamic thermal behaviour*. DOI [10.1016/j.epsr.2022.108447](https://doi.org/10.1016/j.epsr.2022.108447).

### Governing mathematics
Eqs (1)-(3), journal p.2 (PDF p.3), use a 1D heat diffusion model

```math
k\frac{\partial^2T}{\partial x^2}+q
=\rho c_p\frac{\partial T}{\partial t},
\quad q=P_0+P_K(t)-h(T-T_a(t)).
```

Boundary temperatures `T(0,t)=T_a(t)` and `T(H,t)=T_o(t)`. Eqs (6)-(11) and Fig.2 cover PDE residual and boundary/input-data losses. Initial-condition data not available in the figure/model description (Fig.3 caption, PDF p.4). Reported effective thermal coefficients deliberately stand in for unmodeled convection/oil buoyancy; height `H=1m` is an explicit simplification (PDF p.4).

### Data and validation boundary
Real transformer ambient temperature, top-oil temperature and load-factor measurements provide temporal forcing and boundary inputs. They use first 100 hours of data and compare approximated interior temperature with **finite-volume numerical output** (50 spatial nodes; Fig. 5, Table 2/3, PDF pp.5-6). Thus, independent measured internal temperature-field accuracy was **not established by the primary FVM comparison**. Authors explicitly state in their Conclusion, PDF p.6, that their PINN could not outperform the finite-volume method for the data considered and note substantial computational expense.

**Thesis consequence:** PINN is not an intrinsically more reliable physics model; match errors, compute cost, field evidence and observation quality against physical baseline. No coupled P↔T_e heat propagation experiment.

## 3. P007 — EV-EcoSim: coupled simulation prior art

**Paper:** *EV-EcoSim: A grid-aware co-simulation platform for the design and optimization of electric vehicle charging infrastructure*. DOI [10.1109/TSG.2023.3339374](https://doi.org/10.1109/TSG.2023.3339374).

**Version limitation:** accessible [arXiv:2401.04705v1](https://arxiv.org/pdf/2401.04705) (13 PDF pages), not journal version of record. Exact publisher-paper equivalence remains unverified and must be checked before citing journal page numbers.

### Explicit coupling physics
Section II, Fig.1, PDF pp.2-3, gives simulator module/data exchange. Equations (13)-(14), PDF p.6, model transformer top-oil and hottest-spot dynamic temperatures with ambient temperature, loading ratio and thermal time constants; Eqs (16)-(17) provide AC-side EVSE active/reactive load from EV charging power and efficiency/power factor. GridLAB-D passes network voltage and load quantities per timestep (Sec.II G, PDF p.6). Section IV simulated case studies use the IEEE 123-bus system, generated EV charging profiles, Pecan Street building-load inputs, transformer aging maps and cost/voltage impact tables (PDF pp.8-10).

### Exactly what is NOT included
In Sec.II A (PDF p.3), the authors assume controlled **23°C** battery-cell operation and explicitly state they **do not model battery internal thermal states**. They acknowledge other temperatures would require experiments. Thus, **the EV-EcoSim coupling itself is prior art, but that paper does not establish field-validated joint extreme-heat transformer + EVSE + battery thermal dynamics or observed mobility-service completion**.

**Thesis consequence:** any novel claim must go beyond simply writing `P <-> T_e`, adding top-oil ODEs, or invoking co-simulation. Evidence-qualified cross-interface thermal transitions and service-level predictions could be examined, subject to novelty and data verification.

## Evidence boundaries and next audit steps

- PDF manuscript/full-text access is **not raw measured trajectories**. None of the three has DA-2 verified raw measurement files in this workflow.
- Exact published journal table and figure numbers are supported by accessible PDF text/captions; **figure pixel-level interpretation remains unverified** because screenshot rendering failed.
- A source may say “experimental data” while its published validation target is a simulated field or externally observed case temperature. Separate *model input measurements*, *measured test outputs*, and *synthetic reference values*.
- All 15 pilot items remain `NOT SCREENED`; PDF audit is not PRISMA inclusion.
- Prioritize next `P001` Krama (charger field heat study) and `P008` Godina (charging→transformer hot-spot modeling prior art), followed by `P010` Villarroel (optically instrumented internal transformer temperatures). Their PDFs have **not been obtained** in this pass.
- To verify a genuinely cross-system claim, demand common equipment IDs and synchronized grid-side/EVSE physical-state measurements with event times, then independent evaluation of observed service impacts.

**Scientific next milestone:** demonstrate what prior literature supports with primary-source evidence, and decide whether any candidate measurement can empirically identify an explicitly thermal `P -> T_e` or `T_e -> P` interface law. This manuscript audit alone does not qualify any dataset or determine Option B's adoption.
