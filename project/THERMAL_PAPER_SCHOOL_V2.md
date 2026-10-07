# Thermal Paper School V2 — Limitation and Gap Framework

**Status:** ACTIVE READING / EVIDENCE-TRANSFER METHOD  
**Effective date:** 2026-10-08  
**Scope:** thermal Power–Electrified Transportation interdependencies; physical state; time; electricity/mobility consequence.  
**State-time definition authority:** `CANONICAL_STATE_TIME_DEFINITIONS_V1.md`  
**State-time authority:** `project/CANONICAL_STATE_TIME_DEFINITIONS_V1.md`

## Canonical state-time reading rule

All paper interpretation must preserve the canonical semantics:

```text
external forcing ≠ system state
physical quantity ≠ state variable ≠ active thesis state
thermal state ≠ operational/energy state
state ≠ capability ≠ service
transition time ≠ propagation delay ≠ service-consequence time ≠ recovery time
```

A paper may establish a physically meaningful quantity without establishing that the quantity belongs in the active thesis state vector. Candidate states are admitted only if their evolution is dynamically required and materially changes the qualified thermal interdependency, capability boundary, service trajectory, validation result, or engineering conclusion.

For every paper that uses a state variable, record:

```text
state identity
→ physical meaning
→ units
→ governing dynamics
→ forcing/input
→ time scale
→ observability
→ capability consequence
→ service materiality
→ thesis-state admission decision
```

## Permanent reading logic

```text
1. Scientific problem
→ 2. Physics
→ 3. Mathematics
→ 4. Method + evidence
→ 5. Engineering interpretation
→ 6. Limitation anatomy
→ 7. Remaining gap + gap-closing test
→ Thesis transfer decision
```

A limitation is a boundary on what can legitimately be inferred, generalized, transferred, measured, or modeled.

## Limitation taxonomy

| Code | Scientific limitation | Governing question |
|---|---|---|
| L1 | Observability | Can the physical state actually be measured or estimated? |
| L2 | Model form | Does the equation omit important physics or rely on restrictive assumptions? |
| L3 | Parameter identifiability | Can required parameters be estimated for the selected case? |
| L4 | Validation domain | Where has the model or experiment actually been validated? |
| L5 | Generalizability | Can a result from one device/site/vehicle transfer to another? |
| L6 | Scale transfer | Does micro/meso behavior materially change macro service? |
| L7 | Time-scale mismatch | Does the mechanism evolve on the same horizon as the thesis experiment? |
| L8 | Coupling omission | Is an important cross-system pathway or feedback missing? |
| L9 | Uncertainty | Are measurement/model/parameter uncertainties quantified and propagated? |
| L10 | Service translation | Does component behavior reach Q_P or Q_T? |
| L11 | Intervention trade-off | Does mitigation introduce energy, cost, power-quality, or other penalties? |

## Canonical state interpretation

The paper school uses the state ontology in `CANONICAL_STATE_TIME_DEFINITIONS_V1.md`.

```text
physical phenomenon ≠ automatically an active state
full physical state space ≠ active reduced thesis state vector
SOC = energy state, not thermal state
aging/degradation can be a slow state
coupling quantity ≠ state unless independent dynamics require it
```

For every candidate state, the reading school must determine whether the variable is physically legitimate, dynamically necessary, materially relevant over the selected horizon, and sufficiently supported by observation, estimation, parameter evidence, and validation.

## Permanent evidence chain

```text
Claim
→ Evidence
→ Validity domain
→ Limitation
→ Remaining unknown
→ Gap-closing test
→ Thesis-transfer decision
```

## Lesson A — Transformer thermal prediction

**Paper:** Guo, Chang, and Lu — *A review of temperature prediction methods for oil-immersed transformers*  
**Source:** https://www.sciencedirect.com/science/article/abs/pii/S0263224124012685  
**Decision:** CORE

### Established
- Top-oil and hot-spot temperature are established transformer thermal states.
- Ambient temperature and loading are drivers of transformer thermal evolution.
- Thermal-circuit, numerical, data-driven, and hybrid models have different fidelity/cost trade-offs.

### Limitations
- Direct hot-spot measurement is difficult.
- Thermal-circuit models require parameter identification.
- Detailed models depend on boundary conditions and can be computationally expensive.
- Temperature prediction alone does not establish electricity-service consequence.

**Codes:** L1, L2, L3, L4, L9, L10.

### What remains
```text
thermal-state prediction
→ validated capability law
→ charging consequence
→ service consequence
```

### Gap-closing test
1. Identify transformer-specific parameters and provenance.
2. Select and validate one minimum-sufficient thermal model.
3. Establish theta_TO/theta_HS → electrical capability mapping.
4. Propagate uncertainty to charging/service outputs.

### Thesis transfer
Candidate active states: `X_P,th = [theta_TO, theta_HS]`.

---

## Lesson B — Transformer cellulose degradation

**Paper:** Jusner et al. — *Thermal stability of cellulose insulation in electrical power transformers — A review*  
**Source:** https://www.sciencedirect.com/science/article/pii/S0144861720313692  
**Decision:** SUPPORTING unless event-scale materiality is demonstrated.

### Established
- Elevated temperature accelerates cellulose degradation.
- Aging can be represented as a legitimate slow degradation state.
- A chemically plausible mechanism is not equivalent to an experimentally demonstrated mechanism.

### Limitations
- Aging usually evolves on a longer horizon than event-scale derating.
- Degradation may not materially change Q_P or Q_T during a short heat event.
- Insulation chemistry introduces additional states and parameters.

**Codes:** L4, L6, L7, L10.

### What remains
Does accumulated aging alter operational capability within the chosen heat-event horizon?

### Gap-closing test
Compare event-scale outputs with and without an aging state. Admit aging only if it materially changes capability, tau^C, delta^th, Q_P, or Q_T.

### State/time rule
```text
fast thermal state != operational/energy state != slow degradation state != capability != service
```

---

## Lesson C — EVSE thermal derating

**Paper:** Krama et al. — *Impact of extreme climatic conditions on fast EV charger performance: field experimental insights from Qatar*  
**Source:** https://www.sciencedirect.com/science/article/pii/S2590174526004435  
**Decision:** CORE MECHANISM EVIDENCE.

### Established
- Field evidence shows heat-induced charger derating and longer charging duration.
- Internal/rectifier temperature can strongly affect offered power.
- Derating can create functional limitation without hardware failure.

### Limitations
- Tested charger, cooling architecture, vehicle, climate, and duty cycle define a narrow validation domain.
- A measured threshold cannot be generalized to all EVSE.
- Public fast-charging evidence does not directly establish fleet/depot parameters.

**Codes:** L4, L5, L8, L10.

### What remains
```text
P_charge,max = f(T_internal, hardware, cooling, control)
```
for the selected depot EVSE.

### Gap-closing test
Match charger topology, cooling, rated power, and control architecture; obtain compatible derating evidence; validate temperature → power → service.

---

## Lesson D — Semiconductor thermal physics

**Paper/topic:** thermal modelling and management of power semiconductors for transportation electrification  
**Source:** https://www.mdpi.com/2032-6653/17/9/465  
**Decision:** SUPPORTING-to-CORE depending on required EVSE fidelity.

### Established
- Electrical losses produce junction-temperature dynamics.
- RC/Foster/Cauer and higher-fidelity methods provide different model resolutions.
- Junction temperature and cycling matter for capability and reliability.

### Limitations
- Junction temperature may be difficult to observe.
- Package/fatigue models can exceed the fidelity required for service analysis.
- Subsystem thermal methods may be mature while realistic mission-level coupling and validation remain incomplete.

**Codes:** L1, L2, L3, L4, L6, L9, L11.

### What remains
Does `T_j` materially improve prediction beyond `T_EVSE` or rectifier temperature?

### Gap-closing test
Compare reduced EVSE temperature model against junction-level model for `P_charge,max`; retain `T_j` only if service prediction changes materially.

---

## Lesson E — Battery thermal management

**Paper:** Hwang et al. — *Review of battery thermal management systems in electric vehicles*  
**Source:** https://doi.org/10.1016/j.rser.2023.114171  
**Decision:** CONDITIONAL.

### Established
- Battery temperature affects charging capability, performance, degradation, and safety.
- SOC is an energy state, not a thermal state.
- BTMS improvements can introduce mass, volume, cost, leakage, complexity, and parasitic-power penalties.

### Limitations
- Limits vary with chemistry, BMS, SOC, cooling design, and manufacturer settings.
- Pack-level cooling benefit does not automatically imply whole-vehicle/fleet service benefit.
- Detailed battery thermal modeling may not change departure readiness.

**Codes:** L2, L3, L4, L5, L6, L9, L10, L11.

### What remains
Does `T_B` materially alter `P_accept,max`, `SOC(t_d)`, or `Q_T`?

### Gap-closing test
Sensitivity analysis with and without temperature-dependent battery charge acceptance; retain `T_B` only if material.

---

## Lesson F — Multiscale battery heat transfer

**Paper:** Sun et al. — *A comprehensive study on heat transfer mechanism and thermal runaway suppression of the lithium-ion battery*  
**Source:** https://www.sciencedirect.com/science/article/pii/S0017931025003680  
**Decision:** SUPPORTING.

### Established
- Battery heat transfer is multiscale.
- Spatial temperature gradients can matter for safety and performance.

### Limitations
- Thermal-runaway evidence is not automatically evidence for normal operational derating.
- High spatial fidelity may not change the infrastructure-service result.
- Parameterization burden grows with fidelity.

**Codes:** L2, L3, L4, L6, L7, L10.

### What remains
Is a lumped `T_B` sufficient, or do spatial hot spots materially change capability/service?

### Gap-closing test
Compare one-node, reduced multi-node, and spatial formulations on the outputs that matter; select the lowest order preserving the consequence.

---

## Lesson G — Hot-climate vehicle/fleet energy

**Paper:** Harasis, Khan, and Massoud — *Operation of EVs in hot climates: Modeling of temperature-driven energy consumption including Li-ion battery energy loss*  
**Source:** https://www.sciencedirect.com/science/article/pii/S2352484725001519  
**Decision:** Potentially CORE for the T_e → P thermal pathway.

### Established
- Ambient temperature affects HVAC/BTMS energy demand.
- Trip energy includes more than traction.
- Increased trip-energy requirement can increase charging demand.

### Limitations
- Relationships are case-dependent on vehicle, route, traffic, occupancy, HVAC, and climate.
- Vehicle-energy validation does not establish transformer thermal consequence.
- Charging schedule and depot configuration mediate the T_e → P handoff.

**Codes:** L4, L5, L6, L8, L9, L10.

### What remains
```text
E_trip
→ charging requirement
→ transformer loading
→ transformer thermal state
```

### Gap-closing test
Calibrate/validate trip-energy model for selected fleet; translate to SOC/charging requirement; propagate through selected transformer model.

---

## Lesson H — Mobility-service translation

**Paper:** Alarrouqi, Bayhan, and Al-Fagih — *An assessment of the energy performance of battery-electric buses in hot environments*  
**Source:** https://researchportal.hbku.edu.qa/en/publications/an-assessment-of-the-energy-performance-of-battery-electric-buses  
**Decision:** CORE for mobility-energy/service translation.

### Established
- Hot-climate operation affects vehicle energy and driving range.
- Energy state must be translated into scheduled mobility capability.

### Limitations
- Driving range is not itself `Q_T`.
- Vehicle-energy evidence does not automatically include EVSE/transformer feedback.
- Service definitions are case-specific.

**Codes:** L4, L5, L6, L8, L10.

### What remains
Define the operational service requirement connecting departure energy/SOC to actual scheduled mobility.

### Gap-closing test
Freeze `SOC_req` or `E_trip + E_reserve`; define `Q_T` as departure readiness and, if data permit, trips served; validate energy → service translation.

---

## Cross-paper handoff gaps

The literature provides many individual pieces. The thesis contribution must be tested at the handoffs:

```text
Heat
→ thermal state
→ capability
→ cross-system exchange
→ operational/energy state
→ electricity or mobility service
```

Priority handoffs:

```text
transformer temperature
→ electrical capability
```

```text
EVSE temperature
→ charging-power capability
```

```text
battery temperature
→ charge acceptance          [only if material]
```

```text
charging power
→ SOC at departure
→ mobility service
```

```text
charging demand
→ transformer loading
→ transformer thermal state
```

## Scientific writing rule

Avoid vague statements such as “few studies exist.”

Write instead:

```text
what is demonstrated
+ evidence used
+ validity domain
+ unsupported inference
+ evidence required to close it
```

## Admission rule

A paper/model may enter the active thesis only when it survives the relevant gates:

```text
physical validity
+ directionality
+ parameter validity
+ scale validity
+ temporal validity
+ service materiality
```

The lowest-fidelity model that preserves the thermal interdependency consequence is preferred.
