# Stage 5 Scope and Rendering Audit

**Date:** 2026-09-11  
**Repository:** `Dossiya-SE/MSE-thesis`  
**Canonical target:** `project/STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md`

## Purpose

This audit records how the Stage-5 literature synthesis was converted into the canonical framework-level specification without changing the frozen seven-stage architecture.

## Preserved scientific content

The canonical Stage-5 file preserves the evidence-backed distinctions among:

- constraint set and viability kernel;
- finite-horizon and infinite-horizon viability;
- robust and stochastic viability;
- loss of viability and actual constraint violation;
- geometric distance and Hamilton–Jacobi value functions;
- viability theory and control-barrier certification;
- viability and recoverability after violation;
- established theory `[E]`, derived synthesis `[D]`, and proposed thesis constructs `[P]`.

The key Stage-5 objects retained are

$$
K_{\rm sus},\quad
\mathcal V_{\rm sus}^{u,T},\quad
\partial\mathcal V,\quad
\rho_E,\quad
\rho_g,\quad
T_{\mathcal V},\quad
T_K,\quad
S_{\mathcal V},\quad
S_K,\quad
\Pi_{\mathcal V},\quad
\Pi_K,\quad
S_{ij}^{\mathcal V}.
$$

## Corrections applied

1. Degree-specific `MSc` wording in the source synthesis was not propagated. The thesis uses **MSE = Master of Science in Engineering**.
2. The canonical file remains **framework level only**. Degree-specific implementation language and a fixed reduced-state numerical demonstrator are not made part of the framework definition.
3. The viability projection $Y_V=\mathcal P_V(Y)$ is retained only as a general framework option with an explicit validation obligation.
4. Long boxed equations were replaced by GitHub-compatible display equations, multiline expressions, or tables.
5. Malformed source tables were rebuilt as valid Markdown tables.
6. Equation tags embedded inside display math were removed in favor of readable section-level mathematical definitions.
7. Tracking links and secondary web-source annotations were removed from the canonical bibliography.
8. DOI references use canonical `https://doi.org/...` form and the bibliography follows the thesis APA-7 convention.
9. Proposed quantities $g_\psi$, $\rho_g$, $S_{\mathcal V}$, $S_K$, $\Pi_{\mathcal V}$, $\Pi_K$, and $S_{ij}^{\mathcal V}$ remain explicitly `[P]`; freezing the scope does not convert them into established theory.
10. Stage 5 is formalized as **Controlled Sustainable Viability** under the unchanged seven-stage framework label **Viability**.

## Boundary check

The canonical stage boundaries are now:

| Stage | Responsibility |
|---|---|
| **3** | Generate coupled hybrid multiscale trajectories. |
| **4** | Observe, infer, coordinate, and control those trajectories. |
| **5** | Determine acceptability, maintainability, proximity to loss, and interdependency sensitivity. |
| **6** | Translate only validated resilience evidence into sustainability-transition requirements. |

No Stage-6 or Stage-7 transformation prescription is introduced into Stage 5.

## Result

**Stage 5 is frozen at framework level.** Its evidence-status distinctions, stage boundary, and proposed-versus-established classification are part of the canonical specification.