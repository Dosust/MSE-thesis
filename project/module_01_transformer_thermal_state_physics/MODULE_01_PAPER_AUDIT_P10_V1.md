# Module 01 Paper Audit P10 V1 — Thermal-Hydraulic Physics and Validation Boundary

**Status:** AUDITED AT ACCESSIBLE AUTHOR-PREPROOF EQUATION/RESULT DEPTH; MINIMUM REDUCED-STATE SUFFICIENCY OPEN  
**Effective date:** 2026-10-08  
**Evidence authority:** `project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md`

## P10 — Garelli et al. (2021)

**Title:** Thermo-magnetic-fluid dynamics analysis of an ONAN distribution transformer cooled with mineral oil and biodegradable esters  
**Journal:** *Thermal Science and Engineering Progress*, 23, 100861  
**DOI:** 10.1016/j.tsep.2021.100861  
**Evidence:** [A4] electromagnetic/thermal-hydraulic numerical model + [A3] manufacturer experimental comparisons (limited accuracy).  
**Access:** publisher record and accessible author-manuscript/preproof text. This record is not a final-publisher-PDF verification or a parameter-transfer authorization.

## Physical problem and method

A **315 kVA, 13.2/0.4 kV ONAN distribution transformer** is modeled for mineral-oil versus ester cooling. Electromagnetic FEM computes nonuniform core/winding heat sources, interpolated into the finite-volume conjugate heat-transfer model. Natural convection, oil ducts, core/winding anisotropic effective conduction, tank/radiator conduction, and external-air convection/radiation correlations are represented.

**Author-preproof governing equations:** continuity Eq. (1), incompressible momentum Eq. (2), solid energy Eq. (3), fluid energy Eq. (4). The model uses temperature-dependent density for buoyancy (Boussinesq), viscosity, conductivity and specific heat; no-slip walls; and laminar-flow assumptions. For the modeled mineral oil the paper reports **Re ≈ 280**. External air is **not CFD-resolved**; wall-to-air heat rejection uses correlations. Numerical transient stepping is used to approach **steady state**, not to validate load-step thermal time constants.

Physical chain:

~~~text
Electrical loading → spatial losses q(x) → solid conduction
→ buoyancy/viscosity-dependent oil flow → convective heat transport
→ tank/radiator heat rejection → spatial temperature and flow fields
~~~

This mechanism clarifies the physical meaning of effective heat-transfer resistance. It does **not** uniquely identify a lumped thermal resistance, capacitance, time constant, or number of dynamic states.

## Validation — crucial adverse evidence

For **mineral oil**, Table 1 reports these temperature rises above ambient (K):

| Measurement | Numerical | Experimental | Numerical minus experimental |
|---|---:|---:|---:|
| HV winding average | 44.1 | 55.9 | **−11.8** |
| LV winding average | 44.3 | 52.9 | **−8.6** |
| Top oil | 42.0 | 45.5 | **−3.5** |
| Bottom oil | 27.7 | 29.9 | **−2.2** |

The authors explicitly recognize approximately 12 K and 9 K winding underprediction, citing simplified straight rather than helical channels, omitted blockages/pressboard and effective conduction approximations. Ester results are **simulated**, not independently experimentally validated in this comparison. Manufacturer power-loss data check the electromagnetic model but do not validate winding hot-spot predictions.

A simulation in this paper finds average oil flow through winding ducts about **25% faster than ester** for the investigated device; this is case-specific, not a general fluid-property or capacity rule.

## Thesis consequence and decision

**P10 establishes the detailed heat-transfer mechanism, not a final reduced model.** Spatial loss distribution, buoyancy, viscosity, duct obstruction, and external heat rejection can affect predicted local temperatures. The observed numerical winding discrepancies show that model detail alone does not ensure trustworthy hottest-spot prediction.

Keep:

~~~text
X_P,th = [theta_TO, theta_HS]^T
CANDIDATE — NOT FROZEN
~~~

**Do not promote** duct oil, flow velocity, or radiator temperature to independent active states unless a validated reduced-versus-detailed comparison shows material change in extreme-heat transition timing, hottest-spot prediction, capability, or electricity/mobility service consequences. State-dependent properties may remain algebraic rather than independent dynamic states.

**OPEN:** dynamic minimum-state sufficiency; reduced-parameter identification; prediction uncertainty; ambient extrapolation beyond the evaluated 30°C case; selected-transformer transferability; EV-charging harmonic/duty loading; normative state-to-capability map; service consequences.

**Module-01 disposition:** P01–P10 evidence positions audited at declared (unequal) depths. **Outcome B — MODEL REMAINS OPEN: additional case-specific validation, standards clause audit and VVUQ required.**

## Primary links

- Publisher: https://doi.org/10.1016/j.tsep.2021.100861
- Accessible author preproof: https://www.researchgate.net/publication/349486538_Thermo-magnetic-fluid_dynamics_analysis_of_an_ONAN_distribution_transformer_cooled_with_mineral_oil_and_biodegradable_esters

**Evidence-density rule:** keep only source-backed physics, observed error, validity boundary, and model-admission consequences.
