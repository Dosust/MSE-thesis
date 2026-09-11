# MSE Thesis — Multilayer Interdependent Power–Transportation Infrastructure Resilience

**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Repository:** Active thesis source of truth  
**Framework status:** Seven-stage architecture frozen  
**Research status:** Stage 1 defined; Stages 2–4 frozen; Stage 5 next  
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

The research determines how causal interdependencies among $P$, $T$, $I$, and $O$ shape disruption propagation, coupled system evolution, knowledge of system state, organizational response capability, controlled trajectories, viability, and long-term sustainable transformation.

The governing reasoning chain is

$$
\text{Structure}
\rightarrow
\text{Causal Mechanisms}
\rightarrow
\text{Coupled Dynamics}
\rightarrow
\text{Observation and Control}
\rightarrow
\text{Viability}
\rightarrow
\text{Sustainable Transformation}.
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
| **5. Viability** | Can acceptable operation be maintained under disturbance and admissible intervention? | **Next** |
| **6. Transformation Interface** | What do verified resilience results imply for sustainability? | Downstream |
| **7. Sustainable Transformation Pathways** | What should change for long-term sustainability? | Downstream |

Framework authority: [`project/CANONICAL_7_STAGE_FRAMEWORK.md`](project/CANONICAL_7_STAGE_FRAMEWORK.md)

---

## 4. Stage 1 — Multilayer Structure

Stage 1 defines the system ontology and framework-level decomposition:

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

The directed scope is

$$
\mathcal I=
\{
P\to T,\ T\to P,\ P\to I,\ I\to P,\ P\to O,\ O\to P,\ 
T\to I,\ I\to T,\ T\to O,\ O\to T,\ I\to O,\ O\to I
\}.
$$

Equivalently, the framework contains six bidirectional families:

$$
P\leftrightarrow T,\quad
P\leftrightarrow I,\quad
P\leftrightarrow O,\quad
T\leftrightarrow I,\quad
T\leftrightarrow O,\quad
I\leftrightarrow O.
$$

Every accepted interdependency is represented by

$$
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
\right).
$$

The minimum causal structure is

$$
\text{Source}
\rightarrow
\text{Mechanism}
\rightarrow
\text{Receiver}
\rightarrow
\text{Effect}.
$$

Common exposure is not sufficient:

$$
\text{same hazard affects }P\text{ and }T
\not\Rightarrow
P\leftrightarrow T.
$$

A retained relation requires

$$
\alpha\xrightarrow{M_{ij}}\beta.
$$

Stage-2 authority: [`project/STAGE_2_INTERDEPENDENCY_MECHANISMS.md`](project/STAGE_2_INTERDEPENDENCY_MECHANISMS.md)

---

## 6. Stage 3 — Coupled Hybrid Multiscale Dynamics

Stage 3 is **canonical and frozen**. It translates accepted Stage-2 causal objects into heterogeneous dynamic consequences without forcing all layers into the same equation class.

The four-layer state remains

$$
Y(t)=
\begin{bmatrix}
x_P(t)\\
x_T(t)\\
z_I(t)\\
z_O(t)
\end{bmatrix},
$$

with augmented hybrid state

$$
\widetilde Y(t)=\big(Y(t),m(t)\big).
$$

The canonical Stage-3 architecture is a hybrid delayed multirate dynamical system:

$$
\dot Y_c(t)
=
F^{m(t)}
\!\left[
Y_c(t),Y_d(t),Y(t-\boldsymbol\delta),h(\mathbf r,t);
\mathcal G(t),\mathcal H_t
\right],
$$

supplemented by algebraic constraints and event-driven updates:

$$
0=G^{m(t)}(Y_c,Y_d,h;\mathcal G),
$$

$$
Y_d^+=R_e(\widetilde Y^-,e),\qquad
m^+=\Delta_m(m^-,\widetilde Y^-,e),\qquad
\mathcal G^+=\Psi(\mathcal G^-,\widetilde Y^-,e,\mathcal H_t).
$$

The temporal discipline is

$$
\text{event time}
\neq
\text{causal delay }\delta
\neq
\text{characteristic timescale }\tau.
$$

For spatial propagation, Stage 3 may use

$$
T_C(j)=\inf\{t>t_0:j\text{ enters a predefined disrupted state}\},
$$

and, only where a physical spatial-front interpretation is meaningful,

$$
v_c(t)=\frac{dr_c(t)}{dt}.
$$

Stage-3 authority: [`project/STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md`](project/STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md)

---

## 7. Stage 4 — Observation, Organization, Feedback and Control

Stage 4 is **canonical and frozen**.

Its research question is:

> **How is the system observed, interpreted, coordinated and controlled?**

The central conceptual spine is

$$
X(t)
\rightarrow
y(t)
\rightarrow
I(t)
\rightarrow
\widehat X(t)
\rightarrow
O(t)
\rightarrow
u(t)
\rightarrow
X(t).
$$

For mathematical implementation, the intervention variable is denoted by $u(t)$:

$$
X(t)
\rightarrow
y(t)
\rightarrow
I(t)
\rightarrow
\widehat X(t)
\rightarrow
O(t)
\rightarrow
u(t)\equiv u(t)
\rightarrow
X(t).
$$

The critical distinction is

$$
X
\neq
y
\neq
I
\neq
\widehat X
\neq
O
\neq
u.
$$

Stage 4 therefore treats response as a **partially observable socio-technical feedback-control problem**, not as a direct failure-to-optimization mapping.

### Observation and estimation

$$
y_k(t)=H_k[X(t-\delta_k)]+\nu_k(t),
$$

and

$$
(\widehat X(t),\Sigma_X(t))
=
\mathcal E\!\left(y_{[0,t]},z_I(t)\right).
$$

Under partial observability, the framework may use

$$
b_t(x)
=
p\!\left(X(t)=x\mid y_{[0,t]},u_{[0,t)}\right).
$$

### Organizational feasibility

The current information and organizational states constrain the action set:

$$
\mathcal U_{\rm available}(t)
=
\mathcal U[z_I(t),z_O(t)],
$$

so

$$
u(t)\in\mathcal U[z_I(t),z_O(t)].
$$

A technically desirable intervention is not automatically organizationally executable.

### Decision and control

The generic policy is

$$
u(t)
=
\pi[\widehat X(t),z_I(t),z_O(t)].
$$

No particular solver—MPC, MILP, dynamic programming, reinforcement learning, game theory, or otherwise—is frozen into the framework.

### Response time

For a sequential, non-overlapping response path,

$$
\tau_{\rm response}
=
\tau_{\rm sense}
+
\tau_{\rm comm}
+
\tau_{\rm est}
+
\tau_{\rm decision}
+
\tau_{\rm coord}
+
\tau_{\rm mobilization}
+
\tau_{\rm act}.
$$

If processes overlap, $\tau_{\rm response}$ is treated as the completion time of the relevant critical path.

The proposed Stage-4 timing diagnostic is

$$
\Pi_R
=
\frac{\tau_{\rm response}}
{\tau_{\rm cascade}},
$$

with the explicit rule

$$
\Pi_R<1
\not\Rightarrow
\text{successful control}.
$$

$\Pi_R$ is a **proposed thesis diagnostic**, not an established resilience law.

### Stage boundary

$$
\boxed{
\text{Stage 3 produces trajectories;}
\quad
\text{Stage 4 observes and controls them;}
\quad
\text{Stage 5 evaluates their viability.}
}
$$

Stage-4 authority: [`project/STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md`](project/STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md)

---

## 8. Stage 5 — Viability

Stage 5 is the **next formalization stage**.

The admissible region will be defined from explicit engineering, service, informational, organizational, and sustainability constraints:

$$
K_{\rm sus}
=
\{Y:g(Y)\le0\}.
$$

The corresponding controlled viability object is

$$
\mathcal V_{\rm sus}^{u}
=
\operatorname{Viab}_{F,\mathcal U(z_I,z_O)}(K_{\rm sus}).
$$

Stage 5 will determine the exact finite-horizon, robust, stochastic, or time-varying formulation from the declared assumptions and evidence. Candidate quantities include viability-boundary distance, time to viability loss, recovery time, interface criticality, and intervention feasibility.

---

## 9. Stages 6–7 — Resilience to Sustainable Transformation

The framework deliberately separates resilience analysis from long-term transformation:

$$
\underbrace{\text{Stages 1--5}}_{\text{resilience analysis}}
\rightarrow
\underbrace{\text{Stage 6}}_{\text{translation interface}}
\rightarrow
\underbrace{\text{Stage 7}}_{\text{sustainable transformation pathways}}.
$$

Stage 6 translates verified resilience findings into transformation requirements. Stage 7 evaluates what should change in technical, informational, organizational, environmental, and policy architecture to improve long-term sustainability.

> **Governing principle:** resilience is analyzed inside the model; sustainability is informed by verified model results.

---

## 10. Evidence architecture

The thesis uses an evidence-gated workflow:

$$
\text{Literature}
\xrightarrow{\text{systematic review / PRISMA}}
\text{Evidence Structure}
\xrightarrow{\text{formalization}}
(\mathcal G,\mathfrak I,F,J,\tau,I,O,K,\mathcal V,u).
$$

The thesis preserves the distinction

$$
\text{domain evidence}
\neq
\text{transferable methodological evidence}
\neq
\text{mathematical theory}
\neq
\text{thesis-proposed synthesis}.
$$

Evidence labels used in canonical stage files are:

- `[E]` — established literature;
- `[D]` — derived synthesis;
- `[P]` — proposed thesis construct.

All in-text citations and reference lists follow **APA 7th edition**.

Evidence resources: [`evidence/`](evidence/)  
Methods and validation controls: [`methods/`](methods/)

---

## 11. Validation and falsification

| Layer | Required validation logic |
|---|---|
| Structure | verify system boundary, taxonomy, and interface mapping |
| Interdependency | require direction + source + mechanism + receiver + effect + evidence |
| Dynamics | check dimensions, native physical laws, limiting cases, event logic, synchronization, and numerical implementation |
| Timescales | separate causal delay from process duration and quantify uncertainty |
| Spatial propagation | validate cascade-arrival definitions and use spatial-front quantities only where meaningful |
| Observation | test measurement coverage and observability |
| Estimation | quantify error, uncertainty, missing data, asynchrony, and sensitivity |
| Information | test availability, latency, freshness, packet loss, and synchronization |
| Organization | test authority, resources, coordination, logistics, and response delay |
| Control | verify feasibility and compare interventions against explicit baselines |
| Viability | verify set computation, constraints, boundary behavior, and sensitivity to model error |
| Transformation | trace recommendations to validated resilience evidence |

The thesis-wide logic is

$$
\text{Claim}
\rightarrow
\text{Test}
\rightarrow
\text{Falsification Opportunity}
\rightarrow
\text{Evidence-backed Conclusion}.
$$

---

## 12. Current research state

$$
\boxed{
\text{Stage 1: defined}
\rightarrow
\text{Stage 2: frozen}
\rightarrow
\text{Stage 3: frozen}
\rightarrow
\text{Stage 4: frozen}
\rightarrow
\textbf{Stage 5: next}
}
$$

The immediate framework program is to formalize Stage 5 using the controlled trajectories produced by Stages 3–4 and to define the admissible set, controlled viability object, time-to-exit logic, geometric margin, uncertainty treatment, and validation obligations without changing the frozen upstream stages.

---

## 13. Repository authority

| File / directory | Role |
|---|---|
| [`PROJECT_MEMORY.md`](PROJECT_MEMORY.md) | repository and framework authority |
| [`project/THESIS_SCOPE.md`](project/THESIS_SCOPE.md) | current thesis scope |
| [`project/CANONICAL_7_STAGE_FRAMEWORK.md`](project/CANONICAL_7_STAGE_FRAMEWORK.md) | frozen seven-stage framework |
| [`project/CANONICAL_SYSTEM_DEFINITION.md`](project/CANONICAL_SYSTEM_DEFINITION.md) | canonical P–T–I–O system identity |
| [`project/FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md`](project/FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md) | framework-level subsystem decomposition |
| [`project/STAGES_1_2_APA7_EVIDENCE_GROUNDED.md`](project/STAGES_1_2_APA7_EVIDENCE_GROUNDED.md) | APA-7 evidence-grounded Stages 1–2 companion |
| [`project/STAGE_2_INTERDEPENDENCY_MECHANISMS.md`](project/STAGE_2_INTERDEPENDENCY_MECHANISMS.md) | frozen Stage-2 causal specification |
| [`project/STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md`](project/STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md) | frozen Stage-3 dynamic specification |
| [`project/STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md`](project/STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md) | frozen Stage-4 feedback/control specification |
| [`figures/`](figures/) | thesis figures and visual specifications |
| [`evidence/`](evidence/) | literature and evidence artifacts |
| [`methods/`](methods/) | mathematical, computational, review, and validation methods |
| [`provenance/`](provenance/) | provenance and audit records |
| [`archive/`](archive/) | superseded/historical artifacts |
| [`research_archive/`](research_archive/) | historical research material |

Historical P–W–T–SW, waste–drainage, equity-centered, and other superseded architectures are **not the current thesis system** unless explicitly reintroduced through a versioned framework change.

---

## 14. Scientific guardrails

- Use **MSE = Master of Science in Engineering** consistently.
- Use **APA 7th edition** for in-text citations and reference lists.
- Preserve the canonical seven-stage framework unless an explicit versioned change is approved.
- Treat $P,T$ as physical infrastructure systems and $I,O$ as informational/organizational layers.
- Never infer interdependency from correlation or common exposure alone.
- Distinguish structural connection from causal mechanism.
- Distinguish event time, causal delay, and characteristic timescale.
- Distinguish true state, measurement, information condition, estimated state, organizational capability, and executed action.
- Do not claim novelty for established concepts without systematic falsification.
- Do not use generated figures as scientific authority.
- Require equations, assumptions, units, provenance, numerical checks, uncertainty analysis, and baseline comparison before strong conclusions.

> **Target standard:** clear ontology + causal evidence + mathematical rigor + physical interpretability + partially observable control + falsifiable validation + reproducibility.

---

## 15. Thesis logic

> **Structure tells us where coupling is possible; mechanisms explain why effects occur; dynamics reveal how, when, and where they propagate; observation and estimation determine what can be known; organization and control determine what can be executed and whether response arrives in time; viability determines whether acceptable operation can be maintained; and verified resilience evidence informs sustainable transformation.**

---

## 16. Change control

A canonical thesis object changes only when the revision is explicitly approved, committed with a clear history message, propagated to dependent equations, figures, evidence tables, and stage interfaces, and checked against the current framework.

Until then, this README and the linked canonical files define the active research direction of the **Master of Science in Engineering (MSE) thesis**.
