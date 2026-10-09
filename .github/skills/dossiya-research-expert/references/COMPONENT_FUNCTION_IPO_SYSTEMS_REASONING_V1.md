# Dossiya Expert — Component–Function–Input/Transformation/Output Systems Reasoning V1

**Status:** On-demand reasoning method, NOT a frozen thesis scientific authority.
**Date:** 2026-10-09
**Purpose:** Start with what a real component does and why it matters, build subsystem and System-of-Systems causal logic, and select mathematics only after the physical process is understood.

## First principle: understand before modeling

Never start by announcing a sophisticated framework, promising a model, or adding equations. Start with:
1. **WHAT** physical object/component exists and where it belongs.
2. **WHY** it exists; its engineering function and intended service contribution.
3. **INPUT** of energy, matter, information/control and external heat forcing at a declared boundary.
4. **TRANSFORMATION** by an identifiable conservation law, constitutive mechanism, component operation or control law; distinguish internal dynamics and thermal-state evolution from external forcing.
5. **OUTPUT** actual physical flow, heat/losses, capability, measured performance, and downstream service.
6. **INTERDEPENDENCY** only if a source condition changes a receiver through a qualified interface mechanism, not merely common heat forcing.
7. **TIME AND EVIDENCE** what evolves, which times matter, and which claim/equation is source-proven, derived or OPEN.

The user's phrase "four information" is not yet an authoritative four-field definition. For a compact first pass use **component/function | inputs | internal transformation | outputs** and record interfaces/time/evidence as necessary qualification fields; avoid claiming the user froze exactly these four fields.

## Hierarchy (levels cannot be collapsed)

- **Component** — equipment with a specific physical function (e.g., transformer, EVSE).
- **Subsystem** — coherent set of components performing an intermediate function (e.g., distribution supply segment, charging subsystem, vehicle energy subsystem).
- **System** — Power System P or full Electrified Transportation System T_e, as defined by frozen scope authority.
- **System of Systems** — two separately functioning and governed systems with qualified directional interactions and system-level service consequences. The SoS level describes architecture; actual coupled behavior must be supported by physics and evidence.
- **Service** — required electricity or mobility function/outcome; never synonym for hardware output.

The full T_e includes road EV, rechargeable energy storage, propulsion/auxiliary systems, vehicle supply circuit, EVSE, physical connector, and necessary power-transfer communications/control, including supported bidirectional transfer. A charging depot/fleet is a bounded application subset, not its complete definition. P remains separate; EVSE is not a third infrastructure.

## Component-to-function matrix (fill per application, never invent constants)

For each component, require:
| Field | Answer/check |
| --- | --- |
| System / subsystem / component | Where located and which upstream/downstream object? |
| Primary function | Why does this component exist; which service does it support? |
| Input(s) | Power/energy, current, thermal environment, information/control; boundary & units |
| Transformation | Physical mechanism and corresponding candidate governing law, energy/heat losses, state evolution |
| Actual output(s) | Delivered power/energy, heat, control signal, etc. Distinguish available from delivered |
| Thermal susceptibility | Which internal state/thermal capability/operating limit changes under heat, with source? |
| Qualified interface | Source→exchange→receiver, independent of shared ambient forcing |
| Timing | Inertia, activation, transition, propagation and service deadline; define event times |
| Service meaning | What measurable required electricity/mobility service may actually change? |
| Evidence | Adjacent verified APA 7 author–date sources; A1–A5 / T1 / OPEN and applicability |
| Admission | Is a dynamic state needed? ADMIT CANDIDATE/OPEN/EXCLUDE under minimum-sufficient physics |

## Example: demonstrate function before complexity

**Power subsystem: distribution transformer.** Function: change voltage while supplying power. Input: upstream AC electricity, downstream aggregate load, ambient temperature as forcing. Transformation: electromagnetic transfer and resistive/core losses creating heat, exchanged with cooling environment; temperature evolves through thermal inertia. Outputs: downstream electrical supply and loss heat. Thermal state→allowable power/curtailment map is OPEN until standards, manufacturer document and operating policy qualify it. Exact model/equipment parameters OPEN.

**T_e charging subsystem: EVSE.** Function: condition and deliver charging power to the vehicle. Inputs: AC supply, vehicle request, cooling environment and control. Transformation: conversion with electrical losses and heat rejection; internal temperature may restrict available charging power with an evidence-backed derating/control law. Outputs: AC input demand, actual DC/battery-side delivered power, heat, charging information. Do not equate throughput with self-consumption.

**T_e energy subsystem: battery.** Function: store energy available to support mobility. Inputs: accepted charging power and thermal-management action; transformation: net stored energy plus losses/heat; output: available energy and discharge to propulsion/auxiliaries. SOC is energy/operational state, not thermal state. Do not assume battery temperature state without materiality/evidence.

**T_e mobility operation:** traction/auxiliary energy demand and declared departure/route requirements translate stored energy into a bounded mobility service proxy. Departure readiness is not necessarily entire delivered mobility service.

## Dynamic-model reasoning order

A **descriptive component chain** is not already an equation. Proceed:
1. Define inputs and outputs at compatible physical/electrical boundaries and units.
2. Identify stored quantities that require dynamic states versus instantaneous algebraic capabilities.
3. Select traceable conservation/constitutive laws; declare initial and boundary conditions.
4. Form physically qualified interface algebraic/operational relations; do not assume reciprocity.
5. Specify externally forced, state-time model and *only* the minimum state vector needed for a prespecified output.
6. Define service threshold, source event, receiver response, timing and observables.
7. Challenge with independent exposure/no coupling baseline and alternative explanations.
8. Numerically verify; validate against independent real evidence where feasible and quantify uncertainty.
9. Retain only mechanisms that change an admitted thesis conclusion.

Candidate descriptive form [T1; not equipment-specific validated law]:
```math
\dot x_P=f_P(x_P,z,H,u;\theta_P),\quad
\dot x_{T_e}=f_{T_e}(x_{T_e},z,H,u;\theta_T),\quad
0=g(x_P,x_{T_e},z,H,u),\quad
(Q_P,Q_T)=h(x_P,x_{T_e},z,u).
```
Interpret H as exogenous heat; z algebraic exchange unless independently dynamic; Q as service output, not temperature.

## DM0 / DM1 / DMF2 terminology gate

The user's spoken labels "DMO zero", "DM zero", "DM one", "DM F of two" and "dynamical modulations" are **not defined by the checked canonical GitHub files**. They may be transcription variants, personal framework labels or references to a particular dynamic-model hierarchy. **DO NOT fabricate expansions, equations, layer meanings or claim them frozen.** Until exact authoritative definitions are provided, mark `[OPEN — notation/ontology]` and work with neutral labels such as **conceptual component map**, **uncoupled dynamic baseline**, **qualified coupled dynamic model**, and **service-output evaluation**, explicitly labeled *temporary descriptors, not aliases for DM0/DM1/DMF2*. If precise identifiers are essential to formalization, request the exact reference; do not block other productive reasoning.

## Response style matching the user's reasoning

Begin: “What is the component? What does it do? Why is its function essential? What enters it? Which physics transforms that input? What leaves it? How does thermal state alter capability? Through which independently supported interface could a different system change? What service, when?” Use concrete component tables before abstract models; explain all arrows. Avoid decorative complexity, encyclopedic component lists, unqualified two-way arrows, invented controls, and unsupported quantified claims.

**Evidence/citations:** Consult `AI_RESEARCH_INSTRUCTIONS.md`, `project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md`, `project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md`, `thesis/00_governance/THESIS_CITATION_AND_REFERENCE_STANDARD_V1.md`, canonical system and state authorities; use verified, adjacent APA 7 author–date citations for external claims. Internal GitHub citations support declared thesis scope only. Maintain original SO1→SO2→SO3 wording and scientific limits.

## QA against purpose

An explanation fails if it shows impressive equations without component functions; confuses charger delivered power with EVSE heat dissipation; calls ambient heat a state; infers causality from shared exposure; conflates transformer thermal state with a verified curtailment threshold; represents SOC as a thermal state; or says a vehicle energy margin alone is full mobility service.
