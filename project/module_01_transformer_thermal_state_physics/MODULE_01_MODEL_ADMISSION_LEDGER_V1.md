# Module 01 Model-Admission Ledger V1

**Status:** ACTIVE CONTROL LEDGER — NO FINAL TRANSFORMER MODEL FROZEN  
**Effective date:** 2026-10-08  
**Evidence basis:** Module 01 P01–P08 checkpoint  
**Authority:** project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md

## 1. Purpose

This ledger prevents a working literature insight from being silently promoted into the active thesis model.

Allowed statuses:

~~~text
ADMITTED CONCEPT
CANDIDATE
OPEN
EXCLUDED
~~~

A concept can be admitted while its numerical parameterization remains OPEN.

## 2. Current ledger

| Scientific object | Status | Evidence basis | Current rule |
|---|---|---|---|
| Conservation of thermal energy | **ADMITTED CONCEPT** | A5/A4 foundational physics + P01–P05 | May govern model derivation; exact reduced form still case dependent |
| Electrical/core/load losses as thermal sources | **ADMITTED CONCEPT** | P01–P05 | Exact loss decomposition remains OPEN |
| Ambient temperature as external forcing | **ADMITTED CONCEPT** | P01–P07 + state-time authority | Do not place ambient temperature inside internal transformer state |
| Thermal capacitance / effective thermal mass creates memory | **ADMITTED CONCEPT** | P01–P05 | Exact capacitance definition/value remains OPEN |
| Nonlinear heat rejection | **ADMITTED CONCEPT** | P01–P03 | Exact constitutive law remains OPEN |
| Temperature-dependent oil viscosity | **ADMITTED CONCEPT** | P03/P05 | Exact oil property law remains OPEN |
| Temperature-dependent winding/load loss | **ADMITTED CONCEPT** | P03 | Exact formulation remains OPEN |
| Transformer construction affects thermal dynamics | **ADMITTED CONCEPT** | P04/P05 | Parameter transfer requires architecture compatibility |
| Top-oil temperature theta_TO | **CANDIDATE ACTIVE STATE** | P01–P07 | Strongly supported but not yet frozen |
| Winding hottest-spot temperature theta_HS | **CANDIDATE ACTIVE STATE — PHYSICALLY MEASURABLE BUT SPATIALLY CONDITIONAL** | P02–P08 | Embedded fiber-optic sensing supports direct local measurement; true global hottest spot still depends on sensor placement/spatial model |
| X_P,th = [theta_TO, theta_HS]^T | **CANDIDATE REDUCED STATE VECTOR [T1]** | P01–P08 synthesis | Must still survive P09–P10 spatial/model-fidelity audit |
| Oil time constant tau_o | **CANDIDATE DYNAMIC DESCRIPTOR** | P03–P06 | **SUPPORTED CONCEPT**; numerical law/value OPEN and case-specific |
| Winding time constant tau_w | **CANDIDATE DYNAMIC DESCRIPTOR** | P03/P04 | Numerical value OPEN |
| Effective thermal resistance R_th | **OPEN / MODEL-SPECIFIC** | P01–P05 | Do not assume constant; exact units/form depend on model |
| Effective thermal capacitance C_th | **OPEN / MODEL-SPECIFIC** | P01–P05 | Must define represented thermal mass and provenance |
| Heat-transfer exponents n, m | **OPEN / MODEL- AND COOLING-SPECIFIC** | P01–P05 | No numerical adoption without exact provenance |
| Oil-viscosity curve mu(T) | **OPEN** | P03/P05 | Requires exact fluid/property authority and range |
| Exact transformer governing ODEs | **OPEN** | P01–P05 | No equation frozen before P06–P10 + standards audit |
| Bottom-oil / duct-oil / tank / radiator states | **OPEN** | Not yet sufficiently audited | Admit only if materially required |
| Spatial temperature field T(x,t) | **REFERENCE / HIGH-FIDELITY CANDIDATE, NOT ACTIVE** | P07 | Use to test reduced-state sufficiency; do not adopt unless spatial detail changes thesis-relevant outputs |
| Top-oil thermal limit | **OPEN** | Current standard/manufacturer audit pending | No numerical limit allowed yet |
| Hottest-spot thermal limit | **OPEN** | Current standard/manufacturer audit pending | No numerical limit allowed yet |
| Transformer allowable electrical capability C_P(t) | **OPEN** | State-to-capability authority not yet established | Must come from standard/equipment evidence |
| C_P = C_P(X_P,th) | **OPEN** | Not established by P01–P05 | Critical future handoff |
| Electricity service Q_P | **OPEN** | Service definition not frozen | Do not derive from thermal state yet |
| EV-depot thermal transferability | **OPEN** | Module 4 evidence not yet audited | No EV-specific claim from P01–P05 |
| Harmonic-loss contribution from EV charging | **OPEN** | Module 4 evidence pending | Do not add until qualified |
| Transformer aging state A_tr | **OPEN / SUPPORTING CANDIDATE** | Separate degradation module required | Do not activate in event-scale state vector yet |

## 3. Current model-admission rule

A candidate enters the active transformer state model only if all are satisfied:

~~~text
physically legitimate
+ dynamically required
+ materially affects a thesis output
+ observable/estimable or otherwise defensibly parameterized
+ compatible with selected transformer architecture
+ supported by standards/evidence
+ validation strategy exists
~~~

## 4. Current prohibitions

Do not yet write as canonical:

~~~text
X_P,th = [theta_TO, theta_HS]^T
~~~

Do not yet assign:

~~~text
tau_o = ...
tau_w = ...
R_th = ...
C_th = ...
n = ...
m = ...
theta_HS,lim = ...
theta_TO,lim = ...
~~~

Do not yet state:

~~~text
thermal limit reached
→ transformer must derate by X%
~~~

unless an exact current standard/manufacturer authority establishes that relation for the eventual case.

## 5. Freeze condition

No Power-side thermal model freeze is allowed until:

1. P09–P10 are audited and P06–P08 evidence remains consistent;
2. the standards spine is audited to clause/equation level where required;
3. the selected transformer architecture is defined;
4. parameter provenance is feasible;
5. the candidate state vector passes the minimum-sufficient-physics test;
6. VVUQ requirements are declared;
7. the state-to-capability handoff is independently established.
