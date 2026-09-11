# Project Memory Entry Point

## Repository authority — 2026-09-11

The sole active repository for this thesis is:

[`Dossiya-SE/MSE-thesis`](https://github.com/Dossiya-SE/MSE-thesis)

All active thesis updates, framework revisions, equations, figures, research notes, evidence records, validation artifacts, and canonical files must be written to **MSE-thesis** unless the user explicitly instructs otherwise.

The repository [`Dossiya-SE/Optimization-for-sustainability-and-resilience`](https://github.com/Dossiya-SE/Optimization-for-sustainability-and-resilience) is historical/reference only and is not the default thesis destination.

---

## Citation and reference standard — 2026-09-11

The thesis-wide citation standard is **APA 7th edition**.

Use author–date in-text citations, narrative citations where appropriate, `et al.` for three or more authors in text, alphabetized reference lists, sentence case for article titles, italicized journal title and volume, canonical DOI URLs in the form `https://doi.org/...`, and citations attached directly to the claims they support.

Do not treat a citation as evidence for a stronger claim than the source supports. Thesis-proposed mathematical objects must be labeled as thesis syntheses unless a source explicitly defines the same object.

---

## Current canonical authority — 2026-09-11

For the current thesis, read these files in order:

1. [`project/THESIS_SCOPE.md`](project/THESIS_SCOPE.md)
2. [`project/CANONICAL_7_STAGE_FRAMEWORK.md`](project/CANONICAL_7_STAGE_FRAMEWORK.md)
3. [`project/CANONICAL_SYSTEM_DEFINITION.md`](project/CANONICAL_SYSTEM_DEFINITION.md)
4. [`project/FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md`](project/FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md)
5. [`project/STAGES_1_2_APA7_EVIDENCE_GROUNDED.md`](project/STAGES_1_2_APA7_EVIDENCE_GROUNDED.md)
6. [`project/STAGE_2_INTERDEPENDENCY_MECHANISMS.md`](project/STAGE_2_INTERDEPENDENCY_MECHANISMS.md)
7. [`project/STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md`](project/STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md)
8. [`project/STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md`](project/STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md)
9. [`project/STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md`](project/STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md)
10. [`figures/FRAMEWORK_VISUAL_FIDELITY_PROTOCOL.md`](figures/FRAMEWORK_VISUAL_FIDELITY_PROTOCOL.md)
11. [`provenance/2026-09-11_STAGE_3_REFERENCE_AND_NOTATION_AUDIT.md`](provenance/2026-09-11_STAGE_3_REFERENCE_AND_NOTATION_AUDIT.md)
12. [`provenance/2026-09-11_STAGE_4_DISPLAY_RENDERING_AUDIT.md`](provenance/2026-09-11_STAGE_4_DISPLAY_RENDERING_AUDIT.md)

These files supersede older framework descriptions when conflicts occur.

---

## Current scientific state

The thesis studies

$$
\mathcal S=\{P,T,I,O\},
$$

with

$$
P,T=\text{physical infrastructure systems},
\qquad
I,O=\text{informational and organizational layers}.
$$

Canonical description:

> **A multilayer physical–informational–organizational interdependent Power–Transportation infrastructure system.**

The seven-stage framework remains frozen. Current completion is:

| Stage | Status |
|---|---|
| **1 — Multilayer Structure** | Defined |
| **2 — Causal Mechanisms** | Frozen |
| **3 — Coupled Hybrid Multiscale Dynamics** | Frozen |
| **4 — Observation, Organization, Feedback and Control** | Frozen |
| **5 — Viability** | Frozen as Controlled Sustainable Viability |
| **6 — Resilience-to-Sustainability Transformation Interface** | **Next** |
| **7 — Sustainable Transformation Pathways** | Downstream |

---

## Frozen Stage-2 object

Every accepted interdependency uses

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

and common hazard exposure alone is not an interdependency.

---

## Frozen Stage-3 object

The canonical four-layer state remains

$$
Y(t)=[x_P,x_T,z_I,z_O]^\top,
$$

and Stage 3 adds the hybrid operating mode through

$$
\widetilde Y(t)=(Y(t),m(t)).
$$

Stage 3 is responsible for heterogeneous native subsystem dynamics, causal delay, multiple timescales, discrete events, mode switching, dynamic topology, trajectory uncertainty, cascade-arrival time, and spatial propagation only where a spatial-front interpretation is physically meaningful.

---

## Frozen Stage-4 object

Stage 4 is a closed-loop partially observable socio-technical control process:

$$
X(t)\rightarrow y(t)\rightarrow I(t)\rightarrow\widehat X(t)\rightarrow O(t)\rightarrow u(t)\rightarrow X(t).
$$

Its core mathematical objects are

$$
(\widehat X,\Sigma_X)=\mathcal E(y_{[0,t]},z_I),
$$

$$
b_t(x)=p\!\left(X(t)=x\mid y_{[0,t]},u_{[0,t)}\right),
$$

$$
\mathcal U_{\rm available}(t)=\mathcal U\!\left(z_I(t),z_O(t)\right),
$$

and

$$
u(t)=\pi\!\left(\widehat X(t),z_I(t),z_O(t)\right),
\qquad
u(t)\in\mathcal U\!\left(z_I(t),z_O(t)\right).
$$

Measurement noise is denoted by $\varepsilon_k(t)$.

For sequential non-overlapping response processes,

$$
\begin{aligned}
\tau_{\rm response}={}&\tau_{\rm sense}+\tau_{\rm comm}+\tau_{\rm est}+\tau_{\rm decision}\\
&+\tau_{\rm coord}+\tau_{\rm mobilization}+\tau_{\rm act}.
\end{aligned}
$$

If processes overlap, $\tau_{\rm response}$ is the relevant critical-path completion time.

The Stage-4 diagnostic

$$
\Pi_R=\frac{\tau_{\rm response}}{\tau_{\rm cascade}}
$$

remains a **thesis construct [P]**, not an established resilience law.

---

## Frozen Stage-5 object

Stage 5 is formalized as **Controlled Sustainable Viability** while preserving the seven-stage label **Viability**.

The accepted state region is

$$
K_{\rm sus}(t)=\{Y:g_r(Y,t)\le0,\ r=1,\ldots,n_K\},
$$

where every threshold requires independent justification.

The primary finite-horizon controlled viability set is

$$
\mathcal V_{\rm sus}^{u,T}
=
\left\{
Y_0\in K_{\rm sus}:
\exists u(\cdot)\in\mathcal U,
\ Y^u(t)\in K_{\rm sus}\ \forall t\in[0,T]
\right\}.
$$

The distinction

$$
Y\notin\mathcal V_{\rm sus}^{u,T}
\not\Rightarrow
Y\notin K_{\rm sus}
$$

is canonical: loss of maintainability is not the same as actual constraint violation.

Robust and stochastic viability remain distinct:

$$
\text{robust viability}\neq\text{stochastic viability}.
$$

The temporal margins are

$$
T_{\mathcal V}=\text{time to loss of maintainability},
\qquad
T_K=\text{time to actual acceptability violation}.
$$

Stage 4 and Stage 5 connect through

$$
S_{\mathcal V}=T_{\mathcal V}-\tau_{\rm response},
\qquad
S_K=T_K-\tau_{\rm response},
$$

and

$$
\Pi_{\mathcal V}=\frac{\tau_{\rm response}}{T_{\mathcal V}},
\qquad
\Pi_K=\frac{\tau_{\rm response}}{T_K}.
$$

A normalized Euclidean or weighted distance $\rho_E$ is the baseline geometric measure. The state-dependent Riemannian margin

$$
\rho_g=d_{g_\psi}(Y,\partial\mathcal V),
\qquad g_\psi(Y)\succ0,
$$

remains a proposed thesis construct `[P]`.

Interface sensitivity is primarily finite perturbation based:

$$
S_{ij}^{\mathcal V}(\Delta\theta)
=
\frac{
\mathcal M_{\mathcal V}(\theta_{ij}+\Delta\theta)
-
\mathcal M_{\mathcal V}(\theta_{ij})
}{\|\Delta\theta\|},
$$

with

$$
\theta_{ij}=(w_{ij},\delta_{ij},\tau_{ij},a_{ij}).
$$

Differential sensitivity is used only where smoothness is demonstrated.

The Stage-5 status classification is also frozen: established viability/invariance theory remains `[E]`; the thesis-specific $K_{\rm sus}$ application, $g_\psi$, $\rho_g$, $S_{\mathcal V}$, $S_K$, $\Pi_{\mathcal V}$, $\Pi_K$, and $S_{ij}^{\mathcal V}$ remain explicitly proposed `[P]` or derived/proposed `[D/P]` constructs until validated.

---

## Current stage boundary

| Stage | Responsibility |
|---|---|
| **3** | Produces coupled hybrid multiscale trajectories. |
| **4** | Observes, infers, coordinates, and controls them. |
| **5** | Determines acceptability, maintainability, proximity to loss, and interdependency sensitivity. |
| **6** | Translates only validated resilience evidence into sustainability-transition requirements. |

The next framework task is **Stage 6 — Resilience-to-Sustainability Transformation Interface**.

---

## Representation rule

For framework figures and diagrams:

> **CHANGE THE VISUAL HIERARCHY, NOT THE SCIENTIFIC CONTENT.**

Generated illustrations are not scientific authority. Final figures must be checked against the canonical project files.

---

## Evidence and novelty rule

Scientific authority comes from original source artifacts, verified literature/evidence records, equations, data, code, numerical tests, and explicit provenance.

The thesis distinguishes

$$
\text{domain evidence}
\neq
\text{transferable methodology}
\neq
\text{mathematical theory}
\neq
\text{derived synthesis}
\neq
\text{thesis-proposed construct}.
$$

Novelty is not assumed because established components are combined. Candidate contributions remain subject to systematic falsification and baseline comparison.

---

## Historical memory

Earlier project-memory capsules remain available for provenance, including:

- [`project_memory/2026-08-21_chain_architecture_v2/`](project_memory/2026-08-21_chain_architecture_v2/)
- [`project_memory/2026-09-09_canonical_7_stage_framework/`](project_memory/2026-09-09_canonical_7_stage_framework/)

Any P–W–T–SW, waste–drainage, equity-centered, older six-chain, or other superseded architecture inside historical memory is **not current thesis authority** unless explicitly reintroduced through a versioned change.
