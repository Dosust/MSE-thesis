# MSE Thesis Mathematical Presentation Standard — V3

This file applies the profile-wide mathematical-display contract to the thesis without changing the frozen thesis scope or claiming that every listed extension is part of the MSE contribution.

## 1. Thesis display hierarchy

The thesis is presented through six mathematically distinct layers:

```text
1. observation / evidence
2. inverse identification + uncertainty
3. hybrid state/interface dynamics
4. admissible state set K_R
5. viability and recovery geometry
6. control/design extensions
```

No figure may collapse these layers into a single unlabeled arrow chain.

## 2. Evidence-state notation

Use the profile vocabulary:

- `[S]` source-grounded mathematics;
- `[D]` derived result;
- `[M]` thesis model/specification;
- `[C]` computed output;
- `[V]` verified result;
- `[E]` empirical evidence/estimate;
- `[H]` research hypothesis;
- `[T]` engineering/design target.

A synthetic QA simulation remains `[C]`/`[V]` as applicable and must not be relabeled `[E]`.

## 3. Canonical state ontology

```math
X(t)=
\begin{bmatrix}
X_P(t)\\
X_W(t)\\
X_T(t)\\
X_{SW}(t)
\end{bmatrix},
```

with distinct interface state `Z(t)`, discrete mode `m(t)`, intervention/control `u(t)`, climate forcing `\xi(t)`, realized hazard `\eta(t)`, uncertain parameters `\theta`, and observation vector `Y(t)`.

The professional visual convention is:

- sector state `X` → blue;
- interface state `Z/G_ij` → violet;
- realized hazard `eta` → red;
- uncertainty/posterior quantities → amber;
- admissible/viable sets → green;
- recovery/control → teal;
- design/optimization → gold;
- source mathematics → indigo;
- unvalidated geometric extensions → dashed magenta.

## 4. Governing hybrid model — [M]

```math
\begin{aligned}
\dot X &= F(X,Z,m,u,\eta;\theta),\\
\varepsilon\dot Z &= G(X,Z,m,\eta;\theta),\\
m^+ &= \Phi(X,Z,m,\eta),\\
Y &= H(X,Z;\theta)+\varepsilon_Y.
\end{aligned}
```

Every figure using this model must visually separate:

1. continuous infrastructure state;
2. dynamic interface state;
3. discrete operating/failure mode;
4. control;
5. forcing/hazard;
6. observation uncertainty.

## 5. Admissibility — [M]

```math
K_R
=
K_{\mathrm{phys}}
\cap
K_{\mathrm{service}}
\cap
K_{\mathrm{sus}}
\cap
K_{\mathrm{eq}}.
```

A plot of `K_R` must identify the actual constraints used to construct it. A generic green region is conceptual only.

## 6. Viability and recovery — [M]

```math
\mathcal V_R
=
\left\{
x_0\in K_R:
\exists u(\cdot)\in\mathcal U,
X(t;x_0,u,\eta,\theta)\in K_R\;\forall t\ge0
\right\},
```

```math
\mathcal C_R
=
\left\{
x_0:
\exists u(\cdot),\exists T<\infty,
X(T;x_0,u)\in\mathcal V_R
\right\},
```

```math
\tau_R(x_0)
=
\inf\left\{
T:\exists u(\cdot),X(T;x_0,u)\in\mathcal V_R
\right\}.
```

The visual system must preserve the distinction

```text
viable
≠ recoverable but currently nonviable
≠ nonrecoverable.
```

## 7. Dynamic-interface comparison — [M/C]

If static and dynamic interface representations are compared, use a declared set-distance quantity such as

```math
\Delta_{\mathcal V}
=
d_H(\mathcal V_{\mathrm{dynamic}},\mathcal V_{\mathrm{static}}).
```

This is a **set-distance diagnostic**, not a curvature measure.

The timescale comparison

```math
\rho_{ij}
=
\frac{\tau_{\mathrm{interface},ij}}
{\tau_{\mathrm{system}}}
```

should be shown through dimensionless regime maps or sensitivity plots, not decorative speed arrows.

## 8. Inverse-problem visualization — [M/C/E]

The inference chain is

```math
\mathcal D_{\mathrm{obs}}
\rightarrow
p(\mathcal G,\theta,Z\mid\mathcal D_{\mathrm{obs}})
\rightarrow
p(\mathcal V_R\mid\mathcal D_{\mathrm{obs}}).
```

A posterior/uncertainty plot must record:

- data source or synthetic-data status;
- likelihood/observation model;
- prior or parameter bounds;
- inference algorithm;
- seed if stochastic;
- credible/ensemble construction;
- convergence/diagnostics where relevant.

## 9. Differential-geometry transfer boundary

The Sochi foundation may support source-grounded displays of metric, connection, curvature, geodesics, Frenet–Serret frames, and Gauss–Bonnet. Those objects do **not** automatically turn `\partial\mathcal V_R` into a Riemannian manifold.

Any thesis extension using

```math
g_V,
\qquad
\Gamma_V,
\qquad
K_{\partial\mathcal V},
\qquad
\kappa[\gamma]
```

must remain `[H]` until the thesis explicitly defines:

1. the state-space differentiable structure;
2. the metric or action functional;
3. regularity assumptions;
4. geometric quantity/estimator;
5. physical interpretation;
6. sensitivity/invariant tests;
7. empirical or mechanistic validation criterion.

Therefore:

```text
source differential geometry
≠ geometric visual metaphor
≠ formally defined thesis geometry.
```

## 10. Figure construction rule

Every final thesis figure should contain or link to:

```text
Figure ID
Mathematical object
Evidence state
Equation/model ID
Parameter domain
Units
Data/synthetic status
Algorithm
Verification
Color semantics
Limitations
Source/provenance
```

## 11. V3 reference visual

The figure

`assets/math-art/thesis_mathematical_architecture_v3.svg`

is the profile-aligned reference architecture. It is an architecture/specification visual, not an empirical result.

## 12. Publication output hierarchy

Use:

```text
LaTeX/TikZ/PGFPlots or Asymptote → exact vector exposition
Python/Julia → numerical plots
PyVista/VTK/Makie → computed 3-D geometry
Blender → only when a mathematical mesh/field is already defined
SVG → repository/profile communication
```

No renderer changes the scientific status of the underlying object.
