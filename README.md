# MSE Thesis — Multilayer Interdependent Power–Transportation Infrastructure Resilience

**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Repository:** Active thesis source of truth  
**Framework status:** Seven-stage architecture frozen  
**Research status:** Stage 1 defined; Stages 2–5 frozen; Stage 6 next  
**Citation standard:** APA 7th edition author–date  
**Updated:** 2026-09-11

> **Repository rule:** all active thesis development belongs in `Dossiya-SE/MSE-thesis`. Historical material is retained only for provenance and does not override current canonical files.

---

## 1. Thesis system

The thesis studies a **multilayer interdependent infrastructure system** with

$$
P,T=\text{physical infrastructure systems},
\qquad
I,O=\text{informational and organizational layers}.
$$

Therefore,

$$
\mathcal S=\{P,T,I,O\}.
$$

> **Canonical description:** A multilayer physical–informational–organizational interdependent Power–Transportation infrastructure system.

At framework level,

$$
Y(t)=
\begin{bmatrix}
x_P(t)\\
x_T(t)\\
z_I(t)\\
z_O(t)
\end{bmatrix}.
$$

$P$ and $T$ are the physical infrastructure systems. $I$ represents sensing, communication, information quality, latency, synchronization, estimation support, and signaling. $O$ represents authority, coordination, decision making, resources, workforce, logistics, mobilization, and intervention capability.

Canonical system files:

- [`project/CANONICAL_SYSTEM_DEFINITION.md`](project/CANONICAL_SYSTEM_DEFINITION.md)
- [`project/FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md`](project/FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md)

---

## 2. Scientific objective

The research determines how causal interdependencies among $P$, $T$, $I$, and $O$ shape disruption propagation, coupled evolution, knowledge of system state, organizational response capability, controlled trajectories, viability, and long-term sustainable transformation.

$$
\begin{aligned}
\text{Structure}
&\rightarrow \text{Causal Mechanisms}
\rightarrow \text{Coupled Dynamics}\\
&\rightarrow \text{Observation and Control}
\rightarrow \text{Viability}\\
&\rightarrow \text{Resilience-to-Sustainability Interface}
\rightarrow \text{Transformation}.
\end{aligned}
$$

> **Modeling principle:** topology alone is insufficient. Every retained cross-layer relation must have a defensible causal mechanism, a state-dependent effect, and a temporal interpretation.

---

## 3. Canonical seven-stage framework

1. **Multilayer Structure**
2. **Causal Mechanisms**
3. **Coupled Hybrid Multiscale Dynamics**
4. **Observation, Organization, Feedback and Control**
5. **Viability**
6. **Resilience-to-Sustainability Transformation Interface**
7. **Sustainable Transformation Pathways**

| Stage | Main question | Status |
|---|---|---|
| **1. Multilayer Structure** | What exists? | Canonical |
| **2. Causal Mechanisms** | Why and through what mechanism does one component/layer affect another? | **Frozen** |
| **3. Coupled Hybrid Multiscale Dynamics** | How, when, and where do effects evolve and propagate? | **Frozen** |
| **4. Observation, Organization, Feedback and Control** | How is the system observed, interpreted, coordinated, and controlled? | **Frozen** |
| **5. Viability** | Under what conditions can acceptable functions be maintained, and how far and how long is the system from unacceptable states? | **Frozen** |
| **6. Transformation Interface** | What do verified resilience results imply for sustainability? | **Next** |
| **7. Sustainable Transformation Pathways** | What should change for long-term sustainability? | Downstream |

Framework authority: [`project/CANONICAL_7_STAGE_FRAMEWORK.md`](project/CANONICAL_7_STAGE_FRAMEWORK.md)

---

## 4. Stage 1 — Multilayer Structure

$$
P=P_G\cup P_{Tr}\cup P_D\cup P_{DER}\cup P_C\cup P_{TP},
$$

$$
T=T_R\cup T_B\cup T_U\cup T_H\cup T_M,
$$

$$
I=I_S\cup I_C\cup I_D\cup I_E\cup I_A\cup I_X\cup I_\tau,
$$

$$
O=O_A\cup O_G\cup O_D\cup O_C\cup O_R\cup O_W\cup O_L\cup O_M\cup O_X\cup O_K.
$$

Stage 1 answers **what exists and where interactions can occur**. It does not establish causality by itself.

Evidence-grounded Stage 1–2 companion: [`project/STAGES_1_2_APA7_EVIDENCE_GROUNDED.md`](project/STAGES_1_2_APA7_EVIDENCE_GROUNDED.md)

---

## 5. Stage 2 — Interdependency Mechanisms

Stage 2 is **canonical and frozen**.

$$
\begin{aligned}
\mathcal I=\{&P\to T,\ T\to P,\ P\to I,\ I\to P,\ P\to O,\ O\to P,\\
&T\to I,\ I\to T,\ T\to O,\ O\to T,\ I\to O,\ O\to I\}.
\end{aligned}
$$

Every accepted interdependency is represented by

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

Stage-2 authority: [`project/STAGE_2_INTERDEPENDENCY_MECHANISMS.md`](project/STAGE_2_INTERDEPENDENCY_MECHANISMS.md)

---

## 6. Stage 3 — Coupled Hybrid Multiscale Dynamics

Stage 3 is **canonical and frozen**. It translates accepted Stage-2 causal objects into heterogeneous dynamic consequences.

$$
Y(t)=
\begin{bmatrix}
x_P(t)\\x_T(t)\\z_I(t)\\z_O(t)
\end{bmatrix},
\qquad
\widetilde Y(t)=\big(Y(t),m(t)\big).
$$

Its architecture is a hybrid delayed multirate dynamical system with continuous/quasi-continuous dynamics, algebraic constraints, discrete events, mode switching, dynamic topology, causal delays, and heterogeneous timescales.

The temporal discipline is

$$
\text{event time}\neq\text{causal delay }\delta\neq\text{characteristic timescale }\tau.
$$

For spatial propagation,

$$
T_C(j)=\inf\{t>t_0:j\text{ enters a predefined disrupted state}\},
$$

and, only where physically meaningful,

$$
v_c(t)=\frac{dr_c(t)}{dt}.
$$

Stage-3 authority: [`project/STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md`](project/STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md)

---

## 7. Stage 4 — Observation, Organization, Feedback and Control

Stage 4 is **canonical and frozen**.

> **Research question:** How is the system observed, interpreted, coordinated and controlled?

The conceptual spine is

$$
X(t)\rightarrow y(t)\rightarrow I(t)\rightarrow\widehat X(t)\rightarrow O(t)\rightarrow u(t)\rightarrow X(t).
$$

The critical distinction is

$$
X\neq y\neq I\neq\widehat X\neq O\neq u.
$$

Observation and estimation use

$$
y_k(t)=H_k[X(t-\delta_k)]+\varepsilon_k(t),
$$

$$
(\widehat X(t),\Sigma_X(t))
=
\mathcal E\!\left(y_{[0,t]},z_I(t)\right).
$$

Under partial observability,

$$
b_t(x)=p\!\left(X(t)=x\mid y_{[0,t]},u_{[0,t)}\right).
$$

Organizational feasibility and control are represented by

$$
\mathcal U_{\rm available}(t)=\mathcal U\!\left(z_I(t),z_O(t)\right),
$$

$$
u(t)=\pi\!\left(\widehat X(t),z_I(t),z_O(t)\right),
\qquad
u(t)\in\mathcal U\!\left(z_I(t),z_O(t)\right).
$$

For a sequential, non-overlapping response path,

$$
\begin{aligned}
\tau_{\rm response}={}&\tau_{\rm sense}+\tau_{\rm comm}+\tau_{\rm est}
+\tau_{\rm decision}\\
&+\tau_{\rm coord}+\tau_{\rm mobilization}+\tau_{\rm act}.
\end{aligned}
$$

If processes overlap, $\tau_{\rm response}$ is the completion time of the relevant critical path.

The Stage-4 diagnostic

$$
\Pi_R=\frac{\tau_{\rm response}}{\tau_{\rm cascade}}
$$

is a **proposed thesis diagnostic [P]**, not an established resilience law.

Stage-4 authority: [`project/STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md`](project/STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md)

---

## 8. Stage 5 — Controlled Sustainable Viability

Stage 5 is **canonical and frozen** at the framework level.

> **Research question:** Under what conditions can acceptable functions be maintained, and how far and how long is the system from unacceptable states?

The Stage-5 hierarchy is

$$
K_{\rm sus}
\rightarrow
\mathcal V_{\rm sus}^{u,T}
\rightarrow
\partial\mathcal V
\rightarrow
\{\rho,T_{\mathcal V},T_K\}
\rightarrow
\{S_{\mathcal V},S_K,S_{ij}^{\mathcal V}\}.
$$

The acceptable constraint set is

$$
K_{\rm sus}(t)
=
\{Y:g_r(Y,t)\le0,\ r=1,\ldots,n_K\},
$$

where each threshold must be independently justified. The finite-horizon controlled viability set is

$$
\mathcal V_{\rm sus}^{u,T}
=
\left\{
Y_0\in K_{\rm sus}:
\exists u(\cdot)\in\mathcal U,
\ Y^u(t)\in K_{\rm sus}\ \forall t\in[0,T]
\right\}.
$$

The framework preserves the distinction

$$
Y\notin\mathcal V_{\rm sus}^{u,T}
\not\Rightarrow
Y\notin K_{\rm sus},
$$

so the loss-of-viability boundary $\partial\mathcal V$ is not the same as the actual acceptability boundary $\partial K_{\rm sus}$.

### Robust and stochastic extensions

For bounded/adversarial uncertainty,

$$
\mathcal V_{\rm rob}^{T}
=
\left\{
Y_0:\exists\pi\in\Pi_{\rm adm},\ \forall\xi\in\Xi,
\ Y^{\pi,\xi}(t)\in K_{\rm sus}\ \forall t\in[0,T]
\right\}.
$$

For probabilistic uncertainty,

$$
\mathcal V_{\varepsilon}^{T}
=
\left\{
Y_0:\exists\pi,
\ \Pr[Y^{\pi}(t)\in K_{\rm sus}\ \forall t\in[0,T]]\ge1-\varepsilon
\right\}.
$$

Thus,

$$
\text{robust viability}\neq\text{stochastic viability}.
$$

### Geometric and temporal margins

A normalized Euclidean/weighted distance is the baseline:

$$
\widetilde Y=D^{-1}(Y-Y_{\rm ref}),
\qquad
\rho_E=d(\widetilde Y,\partial\widetilde{\mathcal V}).
$$

The proposed state-dependent extension is

$$
\rho_g=d_{g_\psi}(Y,\partial\mathcal V),
\qquad
g_\psi(Y)\succ0.
$$

$\rho_g$ is explicitly a **proposed thesis construct [P]** and must outperform justified geometric baselines before any stronger claim is made.

Two temporal margins are retained:

$$
T_{\mathcal V}
=\inf\{t>0:Y(t)\notin\mathcal V_{\rm sus}^{u,T-t}\},
$$

$$
T_K
=\inf\{t>0:Y(t)\notin K_{\rm sus}\}.
$$

Stage 4 connects to Stage 5 through

$$
S_{\mathcal V}=T_{\mathcal V}-\tau_{\rm response},
\qquad
S_K=T_K-\tau_{\rm response},
$$

and the proposed dimensionless diagnostics

$$
\Pi_{\mathcal V}=\frac{\tau_{\rm response}}{T_{\mathcal V}},
\qquad
\Pi_K=\frac{\tau_{\rm response}}{T_K}.
$$

These timing quantities are **[P] thesis diagnostics**, not universal resilience laws.

### Interface sensitivity

Because viability boundaries need not be smooth, finite perturbation is the primary proposed sensitivity:

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

Stage-5 authority: [`project/STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md`](project/STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md)

---

## 9. Stages 6–7 — Resilience to Sustainable Transformation

$$
\underbrace{\text{Stages 1--5}}_{\text{resilience analysis}}
\rightarrow
\underbrace{\text{Stage 6}}_{\text{translation interface}}
\rightarrow
\underbrace{\text{Stage 7}}_{\text{sustainable transformation pathways}}.
$$

Stage 6 translates verified resilience findings into transformation requirements. Stage 7 evaluates what should change for long-term sustainability.

> **Governing principle:** resilience is analyzed inside the model; sustainability is informed by verified model results.

---

## 10. Evidence and validation architecture

The thesis uses an evidence-gated workflow:

$$
\begin{aligned}
\text{Literature}
&\xrightarrow{\text{systematic review / PRISMA}}
\text{Evidence Structure}\\
&\xrightarrow{\text{formalization}}
(\mathcal G,\mathfrak I,F,J,\tau,I,O,K,\mathcal V,u).
\end{aligned}
$$

The thesis distinguishes

$$
\text{domain evidence}\neq\text{transferable methodology}\neq\text{mathematical theory}\neq\text{thesis-proposed synthesis}.
$$

Canonical stage files use `[E]` for established literature, `[D]` for derived synthesis, and `[P]` for proposed thesis constructs. All in-text citations and reference lists follow **APA 7th edition**.

The validation logic is

$$
\text{Claim}\rightarrow\text{Test}\rightarrow\text{Falsification Opportunity}\rightarrow\text{Evidence-backed Conclusion}.
$$

---

## 11. Current research state

| Stage | Status |
|---|---|
| **1 — Multilayer Structure** | Defined |
| **2 — Causal Mechanisms** | Frozen |
| **3 — Coupled Hybrid Multiscale Dynamics** | Frozen |
| **4 — Observation, Organization, Feedback and Control** | Frozen |
| **5 — Viability** | Frozen |
| **6 — Resilience-to-Sustainability Transformation Interface** | **Next** |
| **7 — Sustainable Transformation Pathways** | Downstream |

The first five stages now form the mathematical chain

$$
\{P,T,I,O\}
\rightarrow
\mathfrak I
\rightarrow
\{F,\mathcal G,m\}
\rightarrow
\{\widehat X,\mathcal U,u,\tau_{\rm response}\}
\rightarrow
\{K_{\rm sus},\mathcal V,\partial\mathcal V,\rho,T_{\mathcal V},T_K\}.
$$

---

## 12. Repository authority

| File / directory | Role |
|---|---|
| [`PROJECT_MEMORY.md`](PROJECT_MEMORY.md) | repository and framework authority |
| [`project/THESIS_SCOPE.md`](project/THESIS_SCOPE.md) | current thesis scope |
| [`project/CANONICAL_7_STAGE_FRAMEWORK.md`](project/CANONICAL_7_STAGE_FRAMEWORK.md) | frozen seven-stage framework |
| [`project/CANONICAL_SYSTEM_DEFINITION.md`](project/CANONICAL_SYSTEM_DEFINITION.md) | canonical P–T–I–O system identity |
| [`project/FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md`](project/FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md) | framework-level subsystem decomposition |
| [`project/STAGES_1_2_APA7_EVIDENCE_GROUNDED.md`](project/STAGES_1_2_APA7_EVIDENCE_GROUNDED.md) | APA-7 evidence-grounded Stages 1–2 companion |
| [`project/STAGE_2_INTERDEPENDENCY_MECHANISMS.md`](project/STAGE_2_INTERDEPENDENCY_MECHANISMS.md) | frozen Stage-2 specification |
| [`project/STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md`](project/STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md) | frozen Stage-3 specification |
| [`project/STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md`](project/STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md) | frozen Stage-4 specification |
| [`project/STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md`](project/STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md) | frozen Stage-5 specification |
| [`evidence/`](evidence/) | literature and evidence artifacts |
| [`methods/`](methods/) | mathematical, computational, review, and validation methods |
| [`provenance/`](provenance/) | provenance and audit records |

Historical P–W–T–SW, waste–drainage, equity-centered, and other superseded architectures are **not the current thesis system** unless explicitly reintroduced through a versioned framework change.

---

## 13. Scientific guardrails

- Use **MSE = Master of Science in Engineering** consistently.
- Use **APA 7th edition** for in-text citations and reference lists.
- Preserve the canonical seven-stage framework unless an explicit versioned change is approved.
- Treat $P,T$ as physical infrastructure systems and $I,O$ as informational/organizational layers.
- Never infer interdependency from correlation or common exposure alone.
- Distinguish structural connection from causal mechanism.
- Distinguish event time, causal delay, and characteristic timescale.
- Distinguish true state, measurement, information condition, estimated state, organizational capability, and executed action.
- Distinguish acceptability $K_{\rm sus}$ from maintainability $\mathcal V_{\rm sus}^{u,T}$.
- Keep robust and stochastic viability mathematically separate.
- Keep HJ value functions and geometric distance conceptually separate.
- Treat $g_\psi$, $\rho_g$, $S_{\mathcal V}$, $S_K$, $\Pi_{\mathcal V}$, $\Pi_K$, and $S_{ij}^{\mathcal V}$ as proposed constructs until validated.
- Do not claim novelty for established concepts without systematic falsification.
- Require equations, assumptions, units, provenance, numerical checks, uncertainty analysis, and baseline comparison before strong conclusions.

> **Target standard:** clear ontology + causal evidence + hybrid dynamics + partially observable control + viability theory + geometric/temporal diagnostics + falsifiable validation + reproducibility.

---

## 14. Thesis logic

> **Structure tells us where coupling is possible; mechanisms explain why effects occur; dynamics reveal how, when, and where they propagate; observation and estimation determine what can be known; organization and control determine what can be executed and whether response arrives in time; viability separates what is acceptable from what remains maintainable and measures proximity to loss; verified resilience evidence then informs sustainable transformation.**

---

## 15. Change control

A canonical thesis object changes only when the revision is explicitly approved, committed with a clear history message, propagated to dependent equations, figures, evidence tables, and stage interfaces, and checked against the current framework.

Until then, this README and the linked canonical files define the active research direction of the **Master of Science in Engineering (MSE) thesis**.
