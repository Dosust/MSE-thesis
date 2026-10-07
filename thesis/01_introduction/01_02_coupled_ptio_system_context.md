## 1.2 Coupled Power–Transportation System Context

> **Active-scope override — 2026-10-07.** The September text below is retained for provenance. Current active work uses **Power System P ↔ Electrified Transportation System T_e**, with `T_e` composed according to `../../project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md`. EVSE, the physical charging connection, and communication/control belong to the Electrified Transportation System scope; coupling/interface variables may represent exchanged quantities without becoming a third physical infrastructure system.

The physical infrastructure core of the thesis is

```math
\boxed{P+T},
```

where `P` denotes the Power system and `T` denotes the Transportation system.

For the active thesis scope, `T` is specifically the **Electrified Transportation System**. **In this thesis, the electrified transportation system comprises the electrically propelled road vehicle, its rechargeable energy-storage system, electric propulsion and auxiliary electrical systems, the vehicle power-supply circuit, electric-vehicle supply equipment, the physical charging connection, and the communication and control functions required for electrical power transfer, including bidirectional transfer where supported (ISO 6469; ISO 5474; ISO 15118; IEC 61851; IEC 62196).**

This is a thesis-level synthesis across complementary standards series rather than a claim that any one standard independently defines the complete system. EVSE and the physical charging connection belong to `T_e`; the Power–Transportation coupling/interface object represents cross-system exchange, constraints, and dependency conditions and does not constitute a third physical infrastructure system.

Information and Organization are supporting domains:

```math
\boxed{I+O}.
```

This is a thesis-specific ontology. It does not imply that `P`, `T`, `I`, and `O` are four equivalent physical infrastructures.

Power and Transportation are the constituent physical systems because they contain the assets, connections, states, controls, failure processes, and service functions required to provide electricity and mobility. They remain separately represented so that coupling does not erase system-specific physics, topology, or operational logic (Hall et al., 2016; Ibáñez et al., 2010).

The **Information domain** represents what can be measured, communicated, or estimated about the physical system. Depending on the experiment, this can include measurement availability, communication status, missing observations, delays, forecasts, and state estimates. Information availability does not by itself establish that a technically possible physical action can be executed (Mohamed, 2019; Rinaldi et al., 2001).

The **Organizational domain** represents conditions through which information becomes feasible action. Relevant conditions can include authority, coordination, priorities, personnel, equipment, resource availability, and response delay. Infrastructure-resilience research shows that human and institutional conditions can materially affect response and adaptation (Chester et al., 2021; Helmrich et al., 2021; Rasoulkhani & Mostafavi, 2018).

The working representation is therefore

```math
\boxed{ \underbrace{P+T}_{\text{physical infrastructure}} + \underbrace{I+O}_{\text{knowledge and feasible-action support}}. }
```

This ontology requires a strict relationship taxonomy.

A **structural relation** identifies where interaction could occur.

A **directional dependency** requires an interpretable physical or operational mechanism through which a source affects a receiver under specified conditions.

A reciprocal **interdependency** requires relevant directional dependencies in both directions.

**Dynamic coupling** requires an additional step: the qualified directional mechanism must be specified sufficiently to enter the governing dynamic model.

The progression is therefore

```math
\boxed{ \text{candidate relation} \rightarrow \text{qualified directional dependency} \rightarrow \text{dynamically admissible coupling}. }
```

Multilayer-network theory provides mathematical tools for representing multiple networks and relation types, but an interlayer edge is not treated in this thesis as evidence of a physical directional dependency (Kivelä et al., 2014).

For `P\rightarrow T_e`, the active electrification mechanism is Power-system electrical capability supplied to the Electrified Transportation System, thereby affecting EVSE charging capability, vehicle energy state or availability, and ultimately mobility service. Coupled traffic–power studies document interactions among charging demand, transportation behavior, and distribution-system operating constraints (Fotouhi et al., 2017; Unterluggauer et al., 2022; Wei et al., 2019).

For `T_e\rightarrow P`, the active reciprocal mechanism is the electrical demand created by the Electrified Transportation System: vehicle arrival, energy state, charging requirement, and charging control determine EVSE demand and the power/current imposed on the distribution system. Where bidirectional transfer is technologically supported and explicitly admitted, stored vehicle energy may also provide reverse transfer to the Power system. Bidirectional transfer is conditional, not universal.

These directional mechanisms are physically distinct and must therefore be represented and qualified independently.

Common exposure remains separate from dependency. Extreme heat can affect Power-system components and Electrified-Transportation components simultaneously, but common thermal exposure is not a cross-system dependency unless the state or capability of one system subsequently changes the other through a specified Power–Transportation mechanism.

Mechanisms introduced in Chapter 1 are therefore **candidate mechanism families**. Their inclusion in the conceptual architecture does not establish case-specific dependency acceptance, numerical identifiability, parameter readiness, or authorization for dynamic simulation. Those stronger claims require the evidence and methodological controls developed later in the thesis.
