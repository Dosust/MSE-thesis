# Module 01 Paper Audits P06–P07 V1

**Status:** WORKING EVIDENCE RECORD — HIGH-RIGOR / EVIDENCE-DENSE  
**Effective date:** 2026-10-08  
**Evidence authority:** project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md

## Reading rule

~~~text
More information ≠ better information.
Best information = strongest evidence + exact scope + explicit limitation + clear thesis consequence.
~~~

Only information that changes physical understanding, mathematical structure, model admission, validation, or thesis scope is retained.

---

# P06 — Wang et al. (2017)

**Title:** Numerical and experimental validation of variation of power transformers’ thermal time constants with load factor  
**Journal:** Applied Thermal Engineering  
**DOI:** 10.1016/j.applthermaleng.2017.07.167  
**Evidence class:** [A3 + A4]  
**Access status:** publisher metadata/preview verified; complete equation-level full-text audit remains desirable before adopting exact RTTC equations.

## Core result

The paper supports that effective oil and winding thermal time constants vary with loading; they are not universal fixed constants.

~~~text
load factor
→ heat-transfer condition
→ effective thermal response rate
→ tau_oil, tau_w
~~~

It combines derivation, CFD and measurements, strengthening P05's experimental calibration result.

## Thesis consequence

Admit conceptually:

~~~text
tau_oil = function(load, thermal condition, design)
tau_w   = function(load, thermal condition, design)
~~~

but do not freeze any numerical law or exponent.

## Limitation

Application, transformer design, CFD details, extreme-heat range and EV-depot transferability are not established for our final case.

## Decision

**CORE STATE–TIME EVIDENCE.**

---

# P07 — Oliveira et al. (2023)

**Title:** Thermal-hydraulic model for temperature prediction on oil-directed power transformers  
**Journal:** International Journal of Electrical Power & Energy Systems  
**Volume/article:** 151, 109133  
**DOI:** 10.1016/j.ijepes.2023.109133  
**Authors:** M.M. Oliveira, L.H. Medeiros, A.M. Kaminski Jr., C.E.G. Falcão, R.C. Beltrame, V.C. Bender, T.B. Marchesan, M.A. Marin  
**Evidence class:** [A3 + A4]  
**Access status:** publisher abstract, highlights and substantial method description verified; complete equation/parameter audit remains OPEN.

## Scientific problem

Determine detailed **steady-state** oil-flow and temperature distributions in an oil-directed power transformer using a computationally reduced thermal-hydraulic network rather than only top-oil/hot-spot lumped outputs.

## Physical/model architecture

Direct publisher evidence supports:

~~~text
transformer geometry + operating data
→ hydraulic resistance network
→ oil-flow distribution
→ thermal losses
→ finite-volume + thermal-network coupling
→ winding / paper / oil-channel temperatures
→ tank/radiator convection + radiation
~~~

The model iteratively solves coupled hydraulic and thermal resistance networks.

## Mathematical meaning

P07 moves from a small lumped state representation toward a distributed steady-state field representation:

~~~text
reduced model: theta_TO, theta_HS
versus
P07: temperature/flow distribution across winding turns, insulation paper, oil channels, tank/radiators
~~~

The exact governing equations, pressure-drop correlations, boundary conditions and numerical tolerances are **not frozen** because full equation-level audit is incomplete.

## Validation

A transformer prototype used **29 optical-fiber temperature sensors** distributed along the active part and radiators.

The publisher reports a **maximum relative temperature error of 1.31%** for the validated prototype.

This is strong [A3] evidence for that specific model/prototype; it is not a universal transformer-model accuracy claim.

## Most important thesis lesson

~~~text
hot spot ≠ primitive scalar everywhere in the physics
hot spot can emerge from a spatial temperature field
~~~

Therefore:

~~~math
theta_HS = max_(x in winding) T(x)
~~~

is a useful **[T1] interpretation**, not an equation attributed directly to P07.

P07 shows what a two-state reduced model compresses:

- oil-channel flow distribution;
- winding-turn temperature distribution;
- insulation-paper temperature;
- radiator/tank heat rejection;
- geometry-dependent hydraulic resistance.

## What P07 establishes

1. Spatial oil-flow/temperature nonuniformity can be modeled explicitly.
2. Geometry and hydraulic resistance determine oil distribution through cooling channels.
3. Heat losses and oil flow jointly determine detailed winding/oil temperatures.
4. Convection and radiation are relevant at external tank/radiator boundaries in this model.
5. Dense optical-fiber validation can test a detailed thermal-hydraulic model.

## What P07 does not establish

- transient state-time dynamics;
- oil/winding time constants;
- ONAN distribution-transformer validity;
- extreme-heat hazard validity;
- EV-depot loading validity;
- state-to-capability law;
- that detailed TH modeling is necessary for our thesis.

## Thesis-transfer decision

**CORE MODEL-FIDELITY / SPATIAL-PHYSICS EVIDENCE.**

Do **not** automatically adopt the detailed TH model.

Use P07 as a reference model for the question:

~~~text
Does spatial flow/temperature detail materially change
theta_HS, critical transition timing, capability, or service consequence?
~~~

If no, retain the lower-order model.

If yes, add only the minimum spatial states needed.

---

# P06–P07 combined result

P06 strengthens the **time** side:

~~~text
thermal response rate is condition/load dependent
~~~

P07 strengthens the **state/scale** side:

~~~text
lumped thermal states compress a spatial thermal-hydraulic field
~~~

Together:

~~~text
State = reduced representation of a richer physical field.
Time = evolution rate that may itself depend on state, load, and design.
~~~

This makes the next decision sharper:

~~~text
Do theta_TO and theta_HS preserve the thesis-relevant consequence,
or is additional spatial detail required?
~~~

No final Power thermal model is frozen.
