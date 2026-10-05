# E-TRANSPORT-IPT-001 — Pearson et al. (2026)

**Status:** ADMITTED EXTERNAL EVIDENCE  
**Date admitted:** 2026-10-05  
**Source type:** Peer-reviewed research paper  
**Primary use:** Transport-electrification interface physics; coupled multi-physics modeling; improvement-first engineering logic  
**Do not use as:** direct extreme-heat evidence or system-level P–T resilience proof

## Source

Connor Pearson, Willsen Wijaya, Seho Kim, Feiyang Jackman Lin, Grant Covic, Tom Allen, Simon Bickerton.  
"Multi-physics study on the thermal response of a coupled inductive power transfer pad."  
Applied Thermal Engineering 304 (2026) 132769.  
DOI: 10.1016/j.applthermaleng.2026.132769.

## 1. Standardized classification

```text
Transport mode
→ Road transport
→ Battery-electric vehicle
→ Wireless charging
→ Inductive Power Transfer (IPT)
→ Coupled primary–secondary charging pads
```

IPT is therefore a specific **battery-mediated road-electrification technology**, not a transport mode.

## 2. Physical interface architecture

The paper describes the energy-transfer chain:

```text
AC grid supply
→ rectifier
→ inverter / high-frequency AC
→ primary ground-side IPT pad
→ magnetic coupling
→ secondary vehicle-side pad
→ rectification / conditioning
→ EV battery
```

This is a concrete Power → Transportation electrification pathway.

Important distinction:
- this paper establishes the local charging-interface physics;
- it does not establish a full system-level Transportation → Power feedback law.

## 3. Qualified physical mechanism

The coupled IPT interface contains interacting electro-magnetic, thermal, and fluid mechanisms:

```text
electrical excitation / magnetic coupling
→ litz conduction loss + ferrite hysteresis loss + aluminium eddy-current loss
→ solid heat conduction
→ convection + radiation
→ component temperature
→ safe operating limit / power-transfer capability / reliability
```

The numerical framework couples:
- electro-magnetics;
- solid heat conduction;
- fluid dynamics.

The paper uses a hybrid transient/quasi-static scheme because the underlying physics operate on different characteristic time scales.

## 4. Strong engineering finding

The coupled primary–secondary configuration behaves materially differently from an isolated single-pad representation.

The paper reports:
- higher temperatures in coupled systems than equivalent single-pad systems;
- discrepancies that increase with transmitted power under close coupling;
- thermal response depending on magnetic coupling, operating current, geometry, convection, and radiation;
- up to 120% higher steady-state temperature in the coupled system in the authors' tested comparison;
- reduced passive heat-dissipation capability in close coupling;
- consequences for safe operating limits, power-transfer capacity, reliability, and safety.

Thesis lesson:

```text
isolated component model
≠ physically coupled interface model
```

and:

```text
coupling can change the physical state enough to change engineering conclusions
```

## 5. Improvement-first relevance

This paper strongly supports the thesis starting logic:

```text
PHYSICS-BASED MATHEMATICAL ENGINEERING
→ resolve the actual coupled interface
→ identify thermal bottlenecks and safe limits
→ identify an engineering improvement
→ test whether service capability improves
```

The authors explicitly recommend considering the coupled thermal response during design and discuss additional thermal-management measures to extend operating capability.

Therefore, for the thesis-defined resilience cycle:

```text
IMPROVE → ADAPT → RESTORE
```

this paper is strongest evidence for **IMPROVE**.

It does not directly validate the Adapt or Restore phases.

## 6. Model-fidelity lesson

A major methodological lesson is:

```text
single-pad simplification
vs.
coupled electro-magnetic–thermal–fluid representation
```

The paper experimentally validates the numerical framework and reports generally small model-to-experiment temperature discrepancies in its tested domain.

This supports our general thesis principle:

```text
added physical fidelity is justified only if it changes a relevant engineering prediction or decision
```

## 7. Important extreme-heat boundary

This paper is **not an extreme-heat study**.

Its experiments were performed in a controlled chamber with an initial ambient temperature of 20 °C, specifically to obtain repeatable thermal tests.

Therefore:

```text
internal electro-thermal heating evidence
≠ extreme ambient heat evidence
```

The paper can support the component/interface thermal model structure, but any use under extreme heat requires a separately justified ambient-temperature boundary condition and validation.

## 8. Service interpretation

The paper does not directly define a mobility-service metric.

What it establishes is a physical capability chain:

```text
thermal state
→ safe IPT operating limit
→ power-transfer capability
→ charging capability
```

A thesis service link such as:

```text
charging capability
→ SOC / vehicle availability
→ mobility service
```

must be established separately.

## 9. Presentation mapping

| Slide | Use |
|---|---|
| 1 — Problem | Electrified road transport can depend on a physically constrained charging interface |
| 2 — Established knowledge | Multi-physics thermal behavior of coupled IPT charging interfaces is already studied |
| 3 — Scope | Candidate road-electrification technology; do not treat IPT as the transport mode itself |
| 4 — Physical mechanism | Excellent mechanism chain from electromagnetic loss to thermal state and power-transfer capability |
| 5 — Service | Physical capability evidence only; mobility-service mapping remains to be built |
| 6 — Mathematical model | Strong precedent for coupled multi-physics equations and hybrid time-scale treatment |
| 7 — VVUQ | Experimental validation, uncertainty, mesh independence, controlled comparison |
| 8 — Engineering value | Strong support for improvement-first engineering through better coupled-interface design/thermal management |

## 10. What this paper does NOT establish

It does not establish:
- extreme-heat ambient degradation;
- road vs rail as the final thesis choice;
- generic EVSE thermal behavior;
- Transportation → Power system feedback;
- coupled electricity–mobility service metrics;
- adaptation policy;
- restoration dynamics;
- thesis resilience metric.

## 11. Admission decision

```text
ADMIT:
IPT as a road-electrification technology
P → T energy-transfer architecture
coupled electro-magnetic–thermal–fluid mechanism
coupling-dependent thermal state
safe operating / transfer-capability consequences
experimental validation precedent
improvement-first design logic

HOLD:
IPT as a possible thesis transport-interface candidate

REJECT AS DIRECT TRANSFER:
20 °C test conditions as extreme-heat evidence
study-specific pad geometry
study-specific 10–100 mm spacing
study-specific numerical temperatures
study-specific thermal-management design as thesis intervention
```

## 12. Freeze impact

Strengthens:
- physics-based mathematical engineering as an improvement method;
- the rule that physically coupled interfaces should be modeled as coupled when coupling materially changes state;
- the need to distinguish component thermal state from service outcome.

Still OPEN:
- road vs rail;
- wired vs wireless charging;
- exact transport-electrification mechanism;
- exact service metrics;
- adaptation strategy;
- restoration strategy;
- final comparator architecture.
