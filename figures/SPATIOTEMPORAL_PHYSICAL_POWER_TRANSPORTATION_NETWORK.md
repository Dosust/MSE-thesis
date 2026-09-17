# Spatiotemporal Physical Power-Transportation Network

**Status:** FINAL / CANONICAL PHYSICAL NETWORK REPRESENTATION  
**Frozen:** 2026-09-17  
**Role:** canonical Class-I physical Power–Transportation network figure for the thesis  
**Exact visual title:** `Spatiotemporal Physical Power-Transportation Network`  
**Intended image asset name:** `Spatiotemporal Physical Power-Transportation Network.png`  
**Source image dimensions:** 1536 × 1024 px  
**Source image mode:** RGBA  
**Source image SHA-256:** `b2f0d9c2b37e869bd41f3a4aac7b0d26145d8a787aebfae21da9d5023af7bba5`

## Canonical role

This figure is the thesis **physical network representation** and the frozen physical core that Class II must augment without changing the underlying Power–Transportation topology or physical interdependency semantics.

## Frozen visual semantics

- Upper layer: **Power network**.
- Lower layer: **Transportation network**.
- Physical interdependencies:
  - orange dashed downward — **Signal-power dependency** (`P → T`);
  - green dashed upward — **Repair-access dependency** (`T → P`).
- Power topology retains separate meanings for substation nodes, power bus nodes, power lines/feeders, power transformers, switches/disconnectors, loads, and generators.
- Transportation topology retains separate meanings for road links, intersection nodes, repair-access nodes, traffic signals, Origin, Destination, OD path, repair route, and repair crew.
- Traffic signals are attached devices at transportation intersection nodes rather than independent graph nodes.
- OD and repair paths follow transportation road topology.
- Repair crew is a mobile agent on the repair route.
- Information and Organization layers are excluded from this physical-core figure.
- Hazard forcing is excluded from this physical-core figure.
- Legend convention is **symbol → meaning only**, with white background.

## Ontology guardrail

```math
\boxed{
\text{Node}\neq\text{Edge}\neq\text{Path}\neq\text{Asset}\neq\text{Agent}\neq\text{Interdependency}
}
```

The required physical dependency geometries are:

```math
\boxed{P\rightarrow T:\;E_P/V_P\rightarrow A_T^{signal}}
```

and

```math
\boxed{T\rightarrow P:\;\Pi_T^{repair}\rightarrow V_P/E_P.}
```

## Freeze rule

Do not alter the physical topology, symbol meanings, path semantics, interdependency directions, relation colors, or legend convention in downstream thesis figures unless this canonical representation is explicitly revised and versioned.
