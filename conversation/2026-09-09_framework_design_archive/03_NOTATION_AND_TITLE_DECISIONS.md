# Notation and Thesis-Title Decisions

## Final thesis title selected in this conversation

**Causal-Hybrid Multilayer Resilience-to-Sustainability Framework for Interdependent Power-Transportation Systems**

This title is aligned with the current architecture:

```math
\text{Causal} \rightarrow \mathcal C
```

```math
\text{Hybrid} \rightarrow (F,J,\tau)
```

```math
\text{Multilayer} \rightarrow (\mathcal G, P-T-I-O)
```

```math
\text{Resilience} \rightarrow \text{Stages 1--5}
```

```math
\text{to-Sustainability} \rightarrow \mathcal T_{ST}
```

```math
\text{Power-Transportation Systems} \rightarrow \text{physical application domain}
```

## State-space notation correction

The generated viability/transformation illustrations used `X_1,X_2` as generic coordinates. That notation was identified as inconsistent with the canonical hierarchy, which uses `Y` as the system-state object.

Therefore, when a two-dimensional state-space projection is required in a figure:

```math
\boxed{X_1,X_2 \rightarrow Y_1,Y_2}
```

Interpretation:

```math
Y(t)\in\mathbb R^n
\xrightarrow{\text{illustrative 2-D projection}}
(Y_1,Y_2)\in\mathbb R^2.
```

The coordinates are intentionally generic. They should **not** be prematurely defined as power performance, transportation performance, or another physical pair unless the mathematical model later establishes those variables explicitly.

### Thesis-safe caption

> **`Y_1,Y_2`: illustrative coordinates of a two-dimensional projection of the coupled system state `Y`.**

## Viability interpretation

The Stage 5 illustration may show a two-dimensional projection for readability, but the real coupled system may remain high dimensional. The figure should therefore represent, not redefine, the system state.

A safe interpretation is:

```math
Y(t)\in\mathcal V
\Rightarrow
\text{the coupled system remains viable under the declared constraints.}
```

## Notation discipline

- Do not introduce `X` as a competing state object in the canonical figure.
- Do not reintroduce geometry-specific symbols unless explicitly approved as a framework revision.
- Keep `K` and `\mathcal V` as the canonical Stage 5 objects.
- Keep `R \xrightarrow{\mathcal T_{ST}} S` as the canonical Stage 6 transformation relation.
