# Project — Current Thermal-Interdependency Thesis Architecture

**Thesis title:** **Physics-Based Mathematical Engineering of Power–Transportation Interdependencies for Resilience**  
**Thermal focus authority:** [`CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md`](CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md)  
**State-time scope amendment:** [`CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V3.md`](CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V3.md)  
**Objective authority:** [`CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md`](CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md)  
**Conceptual framework:** [`CONCEPTUAL_FRAMEWORK_SPEC_V4_THERMAL.md`](CONCEPTUAL_FRAMEWORK_SPEC_V4_THERMAL.md)  
**Mathematical framework:** [`MATHEMATICAL_FRAMEWORK_SPEC_V2_THERMAL.md`](MATHEMATICAL_FRAMEWORK_SPEC_V2_THERMAL.md)  
**Authority index:** [`CURRENT_THESIS_AUTHORITY_INDEX_V1.md`](CURRENT_THESIS_AUTHORITY_INDEX_V1.md)  
**Status date:** 2026-10-07

## Active research problem

The active thesis studies **only thermal interdependencies between the Power System and Electrified Transportation System and their consequences through physical state and time**.

```text
Extreme heat
→ thermal physical state
→ thermal capability / constraint
→ qualified thermal P ↔ T_e interdependency
→ state-time evolution
→ critical transition / propagation timing
→ electricity + mobility service consequence
```

Non-thermal Power–Transportation interdependencies are outside the active analytical scope unless required strictly as boundary conditions, constraints, or supporting variables for a thermal mechanism.

## Active physical scope

```text
Power System P
↔
Electrified Transportation System T_e
```

EVSE belongs to `T_e`. Coupling/interface variables do not constitute a third physical system.

Battery-electric road transportation with grid-connected charging remains the bounded application subset. Exact charging context remains open.

## Frozen objective contract

**General Objective**

> To characterize and model thermal interdependencies between the Power System and the Electrified Transportation System under extreme heat, and to quantify how their consequences evolve through physical state and time.

**SO1 — Identify and qualify**

> Identify and qualify the thermally sensitive physical states and directional thermal interdependency mechanisms connecting the Power System and the Electrified Transportation System.

**SO2 — Model state-time evolution**

> Develop a physics-based state-time model of the qualified thermal interdependencies and their propagation under extreme heat.

**SO3 — Quantify consequences**

> Quantify critical transition times, interdependency propagation delays, and the resulting electricity and mobility service consequences.

## Active mathematical outputs

```math
X_P^{th}(t),quad
X_{T_e}^{th}(t),quad
Z_{PT}^{th}(t),quad
	au_i^C,quad
delta_{ij}^{th},quad
Q_P(t),quad
Q_T(t).
```

## Open objects

- exact charging context;
- exact thermally active states;
- exact thermal thresholds;
- exact electricity and mobility service metrics;
- validation data/case;
- final thermal RQ wording;
- hypotheses;
- optional thermal intervention set;
- final novelty claim.

## Historical material

Earlier seven-stage, broad P–T–I–O, RQ0/RQ1–RQ7, SO1–SO7, H1–H5, viability, sustainability, and engineering-decision packages remain preserved for provenance and reusable methods only. They do not control the active thesis where they conflict with the thermal-only authorities.

## Governing rule

```text
thermal mechanism
→ state
→ time
→ service consequence
```

No broader architecture may override this chain without an explicit versioned scope change.


## Thermal paper-reading school

The active literature-transfer method is:

- [`THERMAL_PAPER_SCHOOL_V2.md`](THERMAL_PAPER_SCHOOL_V2.md)
- [`../tools/thermal_paper_school_v2.py`](../tools/thermal_paper_school_v2.py)

Permanent chain:

```text
Claim
→ Evidence
→ Validity domain
→ Limitation
→ Remaining unknown
→ Gap-closing test
→ Thesis-transfer decision
```

This method is used to prevent subsystem literature from being transferred into the active thermal model without explicit validity, scale, time, and service checks.
