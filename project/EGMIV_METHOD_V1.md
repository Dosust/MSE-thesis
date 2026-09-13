# EGMIV Method v1.0

**Canonical name:** Evidence-Grounded Mechanistic Interdependency and Validation Method  
**Acronym:** EGMIV  
**Status:** canonical working method for thesis evidence-to-model execution  
**Date frozen:** 2026-09-13

## Purpose

EGMIV is the method used to build and test the seven-stage thesis architecture. The seven-stage framework defines **what the scientific architecture is**; EGMIV defines **how evidence is converted into mechanisms, mathematical models, competing representations, falsifiable experiments, and validated engineering claims**.

```math
\boxed{
\text{Evidence}
\rightarrow
\text{Mechanism}
\rightarrow
\text{Interdependency}
\rightarrow
\text{Mathematical Model}
\rightarrow
\text{Validation}
}
```

The governing rule is:

```math
\boxed{
\text{No interdependency without direction + mechanism + mapping + type + evidence.}
}
```

## Canonical execution chain

```math
\boxed{
\begin{aligned}
&\text{evidence discovery}
\rightarrow \text{eligibility / screening}
\rightarrow \text{mechanism extraction}
\rightarrow \mathfrak I_{ij}^{\alpha\beta}\\
&\rightarrow \text{graph-to-dynamics mapping}
\rightarrow \text{competing representations}
\rightarrow \text{matched experiments}\\
&\rightarrow \text{uncertainty + falsification}
\rightarrow \text{physical validation}
\rightarrow \text{viability / criticality / intervention}.
\end{aligned}
}
```

## Canonical interdependency object

```math
\boxed{
\mathfrak I_{ij}^{\alpha\beta}
=
\left(
E_i^\alpha,
E_j^\beta,
M_{ij},
w_{ij},
\delta_{ij},
\tau_{ij},
a_{ij},
m,
\mathcal H_t
\right)
}
```

Every modeled dependency must expose its source, receiver, mechanism, strength or uncertain parameterization, delay, characteristic timescale, activation condition, mode/type, and hazard/context domain.

## Evidence admissibility

EGMIV distinguishes at least four epistemic uses of evidence:

1. **Topology/structure evidence** — enough to justify that a directional mechanism exists.
2. **Model-form evidence** — enough to justify a mathematical coupling form.
3. **Parameterization evidence** — enough to estimate numerical parameters.
4. **Validation evidence** — independent or held-out evidence used to test the model.

A literature statement is not automatically a validated coupling law.

## Competing-model rule

EGMIV prohibits validating only the preferred model. For H1, the frozen comparison is:

```math
\boxed{
M_0=\text{independent},\qquad
M_1=\text{static/algebraic coupling},\qquad
M_2=\text{dynamic causal coupling}.
}
```

The preferred model must earn its complexity under matched scenarios, physical constraints, uncertainty analysis, and held-out validation.

## Parameter rule

No numerical parameter may be introduced solely for convenience and later treated as empirical evidence.

Parameter provenance priority is:

```math
\boxed{
\text{measured/site data}
>
\text{peer-reviewed/full-text evidence}
>
\text{benchmark data}
>
\text{sensitivity-only assumption}.
}
```

## Falsification and nesting

A more complex representation must reproduce simpler limits when the added mechanisms are removed:

```math
\boxed{
M_2\rightarrow M_1
\quad\text{as dynamic memory/delay}\rightarrow0
}
```

and

```math
\boxed{
M_1,M_2\rightarrow M_0
\quad\text{when interface maps are removed}.
}
```

Failure of these limiting cases invalidates the implementation before scientific inference.

## Physical admissibility

Every candidate model must satisfy dimensional consistency, conservation laws, topology/physics constraints, and declared numerical tolerances. A lower statistical error cannot compensate for physically impossible behavior.

## Invocation convention

When the instruction is **“use EGMIV deeply”**, the required behavior is:

- trace each claim to admissible evidence;
- instantiate the mechanism directionally;
- preserve source notation before thesis mapping where applicable;
- compare rival models rather than only the preferred formulation;
- avoid invented numerical parameters;
- enforce units, conservation, physical feasibility, and nested limits;
- propagate uncertainty;
- predeclare decision/falsification gates;
- separate calibration from validation;
- accept a conclusion only after the model survives the relevant validation gates.

## Relationship to the seven-stage framework

```math
\boxed{
\text{Seven-stage framework}=\text{scientific architecture}
}
```

```math
\boxed{
\text{EGMIV}=\text{method for constructing and testing that architecture}.
}
```

EGMIV does not replace FTEE. FTEE is the evidence-to-equation extraction protocol inside the broader EGMIV pipeline.

## Current H1 state

As of 2026-09-13:

```math
\boxed{
\text{H1 evidence}
\rightarrow
\mathfrak I_{PT}
\rightarrow
\{M_0,M_1,M_2\}
\rightarrow
\text{M0 implementation}
\rightarrow
\text{M0 verification PASS}
\rightarrow
\mathbf{M_1\ next}.
}
```

The authenticated Scopus/WoS/Compendex/IEEE confirmatory search remains a separate required evidence-completion task and has not been replaced by public discovery.