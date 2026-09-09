# Visual Engineering Logic-Map Specification

## Purpose

This file defines the preferred visual grammar for Stage 1 and Stage 1A.

## Do not use

- radial rainbow mind maps;
- compact spider diagrams;
- tiny branch labels;
- decorative central bubbles;
- arbitrary color coding without scientific meaning.

## Preferred layout

Use a **horizontal engineering logic chart** on a white canvas with navy text, cyan connectors, restrained blue section nodes, and consistent rectangular/rounded modules.

### Stage 1 flow

```text
[ Governing Principle ]
        ↓
[ Structural Skeleton 𝒢 ]
        ↓
[ Dependency Status sᵢⱼ ]
        ↓
[ Typed Relation rᵢⱼ ]
        ↓
[ Relation Classes ]
        ↓
[ Evidence Architecture 𝓔 ]
        ↓
[ 𝔐₁ = (𝒢,𝓡,𝒰,𝓗,𝓔,Y₀) ]
        ↓
[ Stage-1 Output ]
        ↓
[ Stage 2 / Stage 3 / Stage 6–7 ]
```

### Stage 1A flow

```math
\boxed{\Omega\rightarrow Q_{adm}\rightarrow S_{ij}\rightarrow r_{ij}\rightarrow\text{Hidden Discovery}\rightarrow\text{Evidence Triangulation}\rightarrow\text{Completeness Audit}\rightarrow\mathfrak M_1^*}
```

## Warning ribbons

```math
\boxed{\text{No edge}\neq\text{No dependency}}
```

```math
\boxed{\text{Shared exposure}\neq\text{Causal dependency}}
```

```math
\boxed{\text{Connectivity}\neq\text{Dependency}\neq\text{Co-exposure}\neq\text{Causality}}
```

## Recommended visual encoding

- Navy: titles and canonical objects.
- Cyan: structural flow/connectors.
- Blue: confirmed structural modules.
- Gray: unresolved/unknown.
- Dashed border: conditional or latent candidate.
- Red should be reserved for invalid/forbidden interpretation, not ordinary nodes.
- Green should be reserved for Stage 6–7 sustainability transformation, preserving the thesis visual hierarchy.

## Design principle

The diagram should read as a **scientific architecture**, not as brainstorming artwork.
