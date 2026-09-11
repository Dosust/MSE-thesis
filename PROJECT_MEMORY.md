# Project Memory Entry Point

## Repository authority — 2026-09-11

The sole active repository for this thesis is:

[`Dossiya-SE/MSE-thesis`](https://github.com/Dossiya-SE/MSE-thesis)

All active thesis updates, framework revisions, equations, figures, research notes, evidence records, validation artifacts, and canonical files must be written to **MSE-thesis** unless explicitly instructed otherwise.

The repository [`Dossiya-SE/Optimization-for-sustainability-and-resilience`](https://github.com/Dossiya-SE/Optimization-for-sustainability-and-resilience) is historical/reference only.

For project navigation, start with [`project/README.md`](project/README.md).

---

## Citation and reference standard

The thesis-wide citation standard is **APA 7th edition**: author–date citations, `et al.` for three or more authors in text, alphabetized reference lists, sentence case for article titles, italicized journal title/volume, canonical DOI URLs, and citations attached directly to the claims they support.

A citation must not be used to support a stronger claim than the source establishes. Thesis-proposed mathematical objects remain labeled `[P]` unless evidence justifies a different status.

---

## Current canonical authority

Read the active files in this order:

1. [`project/README.md`](project/README.md) — project dashboard and mathematical-rendering standard
2. [`project/THESIS_SCOPE.md`](project/THESIS_SCOPE.md)
3. [`project/CANONICAL_7_STAGE_FRAMEWORK.md`](project/CANONICAL_7_STAGE_FRAMEWORK.md)
4. [`project/CANONICAL_SYSTEM_DEFINITION.md`](project/CANONICAL_SYSTEM_DEFINITION.md)
5. [`project/FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md`](project/FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md)
6. [`project/STAGES_1_2_APA7_EVIDENCE_GROUNDED.md`](project/STAGES_1_2_APA7_EVIDENCE_GROUNDED.md)
7. [`project/STAGE_2_INTERDEPENDENCY_MECHANISMS.md`](project/STAGE_2_INTERDEPENDENCY_MECHANISMS.md)
8. [`project/STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md`](project/STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md)
9. [`project/STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md`](project/STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md)
10. [`project/STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md`](project/STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md)
11. [`project/MATHEMATICAL_FOUNDATION.md`](project/MATHEMATICAL_FOUNDATION.md)
12. [`project/SCIENTIFIC_PROPOSITIONS.md`](project/SCIENTIFIC_PROPOSITIONS.md)
13. [`project/MATHEMATICAL_PRESENTATION_V3.md`](project/MATHEMATICAL_PRESENTATION_V3.md)
14. [`figures/FRAMEWORK_VISUAL_FIDELITY_PROTOCOL.md`](figures/FRAMEWORK_VISUAL_FIDELITY_PROTOCOL.md)
15. [`provenance/2026-09-11_PROJECT_MATHEMATICAL_DISPLAY_CONTENT_AUDIT.md`](provenance/2026-09-11_PROJECT_MATHEMATICAL_DISPLAY_CONTENT_AUDIT.md)

These files supersede older framework descriptions when conflicts occur.

---

## Current scientific state

The thesis studies

$$
\mathcal S=\{P,T,I,O\},
$$

where

$$
P,T=\text{physical infrastructure systems},
\qquad
I,O=\text{informational and organizational layers}.
$$

Canonical description:

> **A multilayer physical–informational–organizational interdependent Power–Transportation infrastructure system.**

The framework remains frozen as seven stages. Current status is:

| Stage | Status |
|---|---|
| **1 — Multilayer Structure** | Defined / canonical |
| **2 — Causal Mechanisms** | Frozen |
| **3 — Coupled Hybrid Multiscale Dynamics** | Frozen |
| **4 — Observation, Organization, Feedback and Control** | Frozen |
| **5 — Viability** | Frozen as Controlled Sustainable Viability |
| **6 — Resilience-to-Sustainability Transformation Interface** | **Next** |
| **7 — Sustainable Transformation Pathways** | Downstream |

---

## Frozen Stage-2 object

$$
\mathfrak I_{ij}^{\alpha\beta}
=
\left(
E_i^\alpha,E_j^\beta,M_{ij},w_{ij},\delta_{ij},\tau_{ij},a_{ij},m,\mathcal H_t
\right).
$$

A retained relation requires

$$
\alpha\xrightarrow{M_{ij}}\beta,
$$

and common exposure alone is not an interdependency.

---

## Frozen Stage-3 object

The canonical state is

$$
Y(t)=
\begin{bmatrix}
x_P(t)\\x_T(t)\\z_I(t)\\z_O(t)
\end{bmatrix},
$$

with

$$
\widetilde Y(t)=\bigl(Y(t),m(t)\bigr).
$$

Stage 3 owns heterogeneous native subsystem dynamics, causal delay, multiple timescales, discrete events, mode switching, dynamic topology, trajectory uncertainty, cascade-arrival time, and spatial propagation only where a physical spatial-front interpretation is meaningful.

---

## Frozen Stage-4 object

Stage 4 is a closed-loop partially observable socio-technical control process:

$$
X(t)\rightarrow y(t)\rightarrow I(t)\rightarrow\widehat X(t)\rightarrow O(t)\rightarrow u(t)\rightarrow X(t).
$$

Its core objects include

$$
(\widehat X,\Sigma_X)=\mathcal E(y_{[0,t]},z_I),
$$

$$
b_t(x)=p\!\left(X(t)=x\mid y_{[0,t]},u_{[0,t)}\right),
$$

and

$$
u(t)=\pi\!\left(\widehat X(t),z_I(t),z_O(t)\right),
\qquad
u(t)\in\mathcal U\!\left(z_I(t),z_O(t)\right).
$$

Measurement noise is denoted by $\varepsilon_k(t)$, not by the control symbol $u$.

For sequential non-overlapping response processes,

$$
\begin{aligned}
\tau_{\rm response}={}&
\tau_{\rm sense}+\tau_{\rm comm}+\tau_{\rm est}+\tau_{\rm decision}\\
&+\tau_{\rm coord}+\tau_{\rm mobilization}+\tau_{\rm act}.
\end{aligned}
$$

If processes overlap, $\tau_{\rm response}$ is the relevant critical-path completion time.

The diagnostic

$$
\Pi_R=\frac{\tau_{\rm response}}{\tau_{\rm cascade}}
$$

remains a proposed thesis construct `[P]`.

---

## Frozen Stage-5 object

Stage 5 is formalized as **Controlled Sustainable Viability** under the seven-stage label **Viability**.

The acceptable set is

$$
K_{\rm sus}(t)=\{Y:g_r(Y,t)\le0,\ r=1,\ldots,n_K\},
$$

and the primary finite-horizon viability set is

$$
\mathcal V_{\rm sus}^{u,T}
=
\left\{
Y_0\in K_{\rm sus}:
\exists u(\cdot)\in\mathcal U,
\ Y^u(t)\in K_{\rm sus}\ \forall t\in[0,T]
\right\}.
$$

The canonical distinction is

$$
Y\notin\mathcal V_{\rm sus}^{u,T}
\not\Rightarrow
Y\notin K_{\rm sus}.
$$

Robust and stochastic viability remain separate. The temporal quantities are

$$
T_{\mathcal V}=\text{time to loss of maintainability},
\qquad
T_K=\text{time to actual acceptability violation}.
$$

The proposed response slacks are

$$
S_{\mathcal V}=T_{\mathcal V}-\tau_{\rm response},
\qquad
S_K=T_K-\tau_{\rm response},
$$

with dimensionless versions

$$
\Pi_{\mathcal V}=\frac{\tau_{\rm response}}{T_{\mathcal V}},
\qquad
\Pi_K=\frac{\tau_{\rm response}}{T_K}.
$$

The normalized Euclidean/weighted margin $\rho_E$ is the baseline. The state-dependent Riemannian margin $\rho_g$ and interface sensitivity $S_{ij}^{\mathcal V}$ remain proposed `[P]` constructs.

---

## Mathematical rendering rule

Active project files follow [`project/MATHEMATICAL_PRESENTATION_V3.md`](project/MATHEMATICAL_PRESENTATION_V3.md): readable GitHub display math, no long prose inside mathematical boxes, no fragile `\tag` dependence, semantic colors only with redundant labels, and tables for taxonomies/specifications.

The project-wide audit is recorded at [`provenance/2026-09-11_PROJECT_MATHEMATICAL_DISPLAY_CONTENT_AUDIT.md`](provenance/2026-09-11_PROJECT_MATHEMATICAL_DISPLAY_CONTENT_AUDIT.md).

---

## Historical memory

Historical materials remain available for provenance, but any P–W–T–SW, waste–drainage, equity-centered, older six-chain, or other superseded architecture is **not current thesis authority** unless explicitly reintroduced through a versioned change.

Historical material under `project/research_memory/` is marked by [`project/research_memory/README.md`](project/research_memory/README.md).

---

## Next framework task

The next stage is **Stage 6 — Resilience-to-Sustainability Transformation Interface**. It must consume only validated Stage-1 through Stage-5 evidence and must not silently alter the frozen upstream mathematics.
