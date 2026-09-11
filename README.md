# MSE Thesis — Multilayer Interdependent Power–Transportation Infrastructure Resilience

**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Repository:** Active thesis source of truth  
**Framework:** Canonical seven-stage architecture  
**Current state:** Stage 1 defined; Stage 2 frozen; Stage 3 is the next formalization stage  
**Last major update:** 2026-09-11

> **Repository rule:** All active thesis development is maintained in `Dossiya-SE/MSE-thesis`. Historical material may remain in archive or project-memory locations for provenance, but it does not override the current canonical specification.

---

## 1. Thesis system

The thesis studies a **multilayer interdependent infrastructure system** with two physical infrastructure systems and two interacting non-physical layers:

$$
P,T=\text{physical infrastructure systems},
\qquad
I,O=\text{informational and organizational layers}.
$$

The canonical system set is

$$
\mathcal S=\{P,T,I,O\}.
$$

The most precise system description is:

> **A multilayer physical–informational–organizational interdependent Power–Transportation infrastructure system.**

At framework level, the integrated state is

$$
Y(t)=
\begin{bmatrix}
x_P(t)\\
x_T(t)\\
I(t)\\
O(t)
\end{bmatrix}.
$$

Here:

- $P$ — Power infrastructure system;
- $T$ — Transportation infrastructure system;
- $I$ — sensing, communication, estimation, information availability, quality, latency, synchronization, and signaling;
- $O$ — authority, decision-making, coordination, resources, workforce, logistics, mobilization, restoration management, and learning.

Information and Organization are **not additional physical infrastructure sectors**. They are explicit interacting layers that affect what the system knows, what actions are feasible, and how quickly intervention can occur.

**Canonical files**

- [`project/CANONICAL_SYSTEM_DEFINITION.md`](project/CANONICAL_SYSTEM_DEFINITION.md)
- [`project/FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md`](project/FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md)

---

## 2. Scientific objective

The research objective is to determine how causal interdependencies among $P$, $T$, $I$, and $O$ shape disruption propagation, coupled system evolution, response capability, recovery, viability, and the transition from resilience analysis to sustainable transformation.

The governing reasoning chain is

$$
\text{Structure}
\rightarrow
\text{Causal Mechanisms}
\rightarrow
\text{Dynamics}
\rightarrow
\text{Feedback \& Control}
\rightarrow
\text{Viability}
\rightarrow
\text{Sustainable Transformation}.
$$

> **Modeling principle:** Topology alone is insufficient. Every retained cross-layer relation must have a defensible causal mechanism, a state-dependent effect, and a temporal interpretation.

---

## 3. Canonical seven-stage framework

The seven-stage architecture is frozen unless an explicit, versioned change is approved.

$$
\begin{aligned}
1.&\ \text{Multilayer Structure}\\
2.&\ \text{Causal Mechanisms}\\
3.&\ \text{Coupled Hybrid Multiscale Dynamics}\\
4.&\ \text{Feedback \& Control}\\
5.&\ \text{Viability}\\
6.&\ \text{Resilience-to-Sustainability Transformation Interface}\\
7.&\ \text{Sustainable Transformation Pathways}
\end{aligned}
$$

| Stage | Role | Main question | Status |
|---|---|---|---|
| **1. Multilayer Structure** | P–T–I–O architecture | **What exists?** | Canonical |
| **2. Causal Mechanisms** | Cross-layer cause–effect pathways | **Why does disruption propagate?** | Frozen |
| **3. Coupled Hybrid Multiscale Dynamics** | Continuous dynamics + discrete events + delays + timescales | **How and when does it evolve?** | Next formalization stage |
| **4. Feedback & Control** | Information, organization, decisions, intervention | **How does the system respond?** | Architecture established |
| **5. Viability** | Survival/recoverability under constraints | **Can it survive?** | Mathematical development follows |
| **6. Resilience-to-Sustainability Transformation Interface** | Translate resilience results into transformation requirements | **What do resilience results imply for sustainability?** | Downstream synthesis |
| **7. Sustainable Transformation Pathways** | Technical, organizational, environmental, and policy transformation | **What should change for long-term sustainability?** | Downstream synthesis |

**Framework authority:** [`project/CANONICAL_7_STAGE_FRAMEWORK.md`](project/CANONICAL_7_STAGE_FRAMEWORK.md)

---

## 4. Stage 1 — Multilayer Structure

Stage 1 defines the system boundary and the framework-level decomposition of $P$, $T$, $I$, and $O$.

### Power system $P$

$$
P=P_G\cup P_{Tr}\cup P_D\cup P_{DER}\cup P_C\cup P_{TP}.
$$

Generation, transmission, distribution, DER/storage, charging power infrastructure, and traction-power supply.

### Transportation system $T$

$$
T=T_R\cup T_B\cup T_U\cup T_H\cup T_M.
$$

Road transportation, electric buses, urban rail, regional/heavy electrified rail, and multimodal transfer.

### Information layer $I$

$$
I=I_S\cup I_C\cup I_D\cup I_E\cup I_A\cup I_X\cup I_{\tau}.
$$

Sensing, communication, data, estimation, automation/signaling, cross-domain interoperability, timing, synchronization, positioning, and information freshness.

### Organizational layer $O$

$$
O=O_A\cup O_G\cup O_D\cup O_C\cup O_R\cup O_W\cup O_L\cup O_M\cup O_X\cup O_K.
$$

Actors, governance, decisions, coordination, resources, workforce, logistics, restoration management, cross-sector collaboration, and learning/adaptation.

Stage 1 answers the structural question only. A structural connection does not automatically imply a causal interdependency.

---

## 5. Stage 2 — Interdependency Mechanisms

Stage 2 is **canonical and frozen**.

It defines how the four subsystems causally affect one another:

$$
\{P,T,I,O\}
\longrightarrow
\mathcal I^{\alpha\beta}.
$$

### Complete directed scope

$$
\begin{aligned}
\mathcal I=\{&P\to T,\ T\to P,\ P\to I,\ I\to P,\ P\to O,\ O\to P,\\
&T\to I,\ I\to T,\ T\to O,\ O\to T,\ I\to O,\ O\to I\}.
\end{aligned}
$$

Equivalently, the thesis audits six bidirectional interdependency families:

$$
P\leftrightarrow T,
\quad
P\leftrightarrow I,
\quad
P\leftrightarrow O,
\quad
T\leftrightarrow I,
\quad
T\leftrightarrow O,
\quad
I\leftrightarrow O.
$$

### Canonical interdependency object

Every accepted component-level interdependency is represented by

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
\right),
\qquad
\alpha,\beta\in\{P,T,I,O\},\ \alpha\neq\beta.
$$

| Element | Meaning |
|---|---|
| $E_i^\alpha$ | source entity/component |
| $E_j^\beta$ | receiving entity/component |
| $M_{ij}$ | causal transmission mechanism |
| $w_{ij}$ | interdependency strength |
| $\delta_{ij}$ | causal delay |
| $\tau_{ij}$ | characteristic mechanism timescale |
| $a_{ij}$ | activation state or condition |
| $m$ | operating/failure mode |
| $\mathcal H_t$ | relevant system/event history |

An arrow alone is insufficient. The minimum accepted logic is

$$
\text{Source}
\rightarrow
\text{Mechanism}
\rightarrow
\text{Receiver}
\rightarrow
\text{Effect}.
$$

### Causal admissibility rule

Common exposure is not itself interdependency:

$$
\text{same hazard affects }P\text{ and }T
\;\not\Rightarrow\;
P\leftrightarrow T.
$$

A retained relation requires a causal transmission mechanism:

$$
\alpha\xrightarrow{M_{ij}}\beta.
$$

**Stage-2 authority:** [`project/STAGE_2_INTERDEPENDENCY_MECHANISMS.md`](project/STAGE_2_INTERDEPENDENCY_MECHANISMS.md)

---

## 6. Stage 3 — Coupled Hybrid Multiscale Dynamics

The next major scientific task is to map accepted Stage-2 causal objects into a coupled dynamic model.

A target continuous-state representation is

$$
\dot Y(t)=F_m\!\left(Y(t),Y(t-\delta),u(t),\eta(t);\theta,\mathcal G(t)\right),
$$

with discrete state or mode transitions

$$
Y^{+}=J_e\!\left(Y^{-},e\right).
$$

The model must distinguish continuous evolution, discrete events, delays, heterogeneous timescales, state/history dependence, external disturbances, and admissible controls.

A central temporal rule is

$$
\text{event time}\neq\text{causal delay }\delta\neq\text{characteristic timescale }\tau.
$$

### Temporal classes

$$
\begin{aligned}
\text{Intrinsic:}&\quad \tau_P,\tau_T,\tau_I,\tau_O,\\
\text{Interaction:}&\quad \delta_{ij},\tau_{ij},a_{ij}(t),\mathcal H_t,\\
\text{Disruption:}&\quad \tau_H,T_{\rm exp},\tau_C,\\
\text{Response/viability:}&\quad \tau_R,T_{\rm exit},T_{\rm rec},\\
\text{Strategic:}&\quad \tau_A,\tau_{Tr},t_k,\Delta t_k,T_H.
\end{aligned}
$$

Dimensionless ratios such as

$$
\Gamma_{\alpha\beta}=\frac{\tau_\alpha}{\tau_\beta}
$$

are treated as **regime descriptors**, not universal thresholds, unless a threshold is derived from the coupled dynamics or supported by evidence.

---

## 7. Stage 4 — Observation, Organization, Feedback and Control

The physical system is not assumed to respond autonomously. The canonical observation–decision–action loop is

$$
X
\rightarrow
y
\rightarrow
I
\rightarrow
\widehat X
\rightarrow
O
\rightarrow
u
\rightarrow
X.
$$

The control action is denoted consistently by $u(t)$, so the implemented loop is

$$
X
\rightarrow
y
\rightarrow
I
\rightarrow
\widehat X
\rightarrow
O
\rightarrow
u
\equiv
u(t)=u(t)
\rightarrow
X.
$$

The mathematical implementation is

$$
y=H(X)+\varepsilon_y,
\qquad
\widehat X=\mathcal E(y_{[0,t]},I),
\qquad
u=\pi(\widehat X,I,O),
\qquad
u\in\mathcal U(I,O).
$$

The scientific problem is whether sensing, communication, estimation, organizational authority, coordination, resources, logistics, and decision delays allow an admissible intervention to arrive before critical system degradation.

---

## 8. Stage 5 — Viability

Stage 5 asks whether acceptable system trajectories can be maintained under disturbance and admissible intervention.

The admissible region is constructed from explicit engineering, service, informational, organizational, and sustainability constraints:

$$
K_{\rm sus}=\{Y:g(Y)\le 0\}.
$$

A controlled viability formulation is

$$
\mathcal V_{\rm sus}^{u}
=
\operatorname{Viab}_{F,\mathcal U(I,O)}(K_{\rm sus}).
$$

The exact finite-horizon, robust, stochastic, or time-varying formulation must be selected from evidence and assumptions and documented explicitly.

Candidate diagnostics include signed distance to the viability boundary, time to viability loss, recovery time, interface criticality, and intervention feasibility under information and organizational constraints. Their final definitions, scaling, uncertainty treatment, and numerical computation remain Stage-5 tasks.

---

## 9. Stages 6–7 — Resilience to sustainable transformation

The framework deliberately separates resilience analysis from long-term transformation:

$$
\underbrace{\text{Stages 1--5}}_{\text{resilience analysis}}
\rightarrow
\underbrace{\text{Stage 6}}_{\text{translation interface}}
\rightarrow
\underbrace{\text{Stage 7}}_{\text{sustainable transformation pathways}}.
$$

Stage 6 converts verified resilience findings into transformation requirements. Stage 7 evaluates what should change in the technical, informational, organizational, environmental, or policy architecture for long-term sustainability.

> **Governing principle:** Resilience is analyzed inside the model; sustainability is informed by the model.

---

## 10. Evidence architecture

The thesis uses a systematic, evidence-gated workflow. Literature is used to establish, parameterize, compare, or falsify specific causal mechanisms and mathematical objects.

The evidence-to-model chain is

$$
\text{Literature}
\xrightarrow{\text{systematic review / PRISMA}}
\text{Evidence Structure}
\xrightarrow{\text{formalization}}
(\mathcal G,\mathfrak I,F,J,\tau,I,O,K,\mathcal V,u).
$$

For each proposed interdependency, extraction should seek, where available,

$$
(E_i^\alpha,E_j^\beta,M_{ij},w_{ij},\delta_{ij},\tau_{ij},a_{ij},m,\mathcal H_t),
$$

plus disturbance, measured effect, model family, data source, calibration, validation, uncertainty treatment, and reported limitations.

The repository preserves the distinction

$$
\text{domain evidence}
\neq
\text{transferable methodological evidence}
\neq
\text{mathematical theory}.
$$

A method demonstrated in another infrastructure domain may justify a modeling technique, but it does not automatically constitute empirical evidence for Power–Transportation behavior.

Evidence resources are maintained under [`evidence/`](evidence/) and methods under [`methods/`](methods/).

---

## 11. Validation and falsification

Every mathematical layer creates a corresponding validation obligation.

| Layer | Required validation logic |
|---|---|
| **Structure** | verify system boundary, component taxonomy, and interface mapping |
| **Interdependency** | require direction + source + mechanism + receiver + effect + evidence |
| **Dynamics** | check dimensions, physical laws, limiting cases, mode logic, and numerical implementation |
| **Timescales** | separate delay from process duration; quantify uncertainty and context dependence |
| **Information** | test observability, latency, missing/noisy data, and estimation sensitivity |
| **Organization** | test authority, coordination, resources, logistics, and response-delay constraints |
| **Control** | compare interventions against explicit baselines under common scenarios |
| **Viability** | verify set computation, boundary behavior, constraint satisfaction, and sensitivity to model error |
| **Transformation** | trace recommendations to verified resilience evidence |

The scientific logic is

$$
\text{Claim}
\rightarrow
\text{Test}
\rightarrow
\text{Falsification Opportunity}
\rightarrow
\text{Evidence-backed Conclusion}.
$$

Mathematical sophistication alone is not evidence of usefulness. Each method must answer a defined research question and, where appropriate, be compared with a simpler baseline.

---

## 12. Current research state

The active progression is

$$
\text{Stage 1: defined}
\rightarrow
\text{Stage 2: frozen}
\rightarrow
\text{Stage 3: dynamics/timescales}
\rightarrow
\text{Stage 4: feedback/control}
\rightarrow
\text{Stage 5: viability}
\rightarrow
\text{Stages 6--7: transformation}.
$$

### Immediate technical program

1. Complete the component-level decomposition of all 12 Stage-2 directional interdependencies.
2. Attach evidence, mechanism, carrier/effect, delay, timescale, activation, mode, and history to every accepted relation.
3. Map accepted Stage-2 objects into Stage-3 hybrid multiscale equations.
4. Quantify temporal competition between disruption propagation and information/organizational response.
5. Close the Stage-4 observation–decision–action loop.
6. Define and compute Stage-5 admissible and viability sets under declared uncertainty/control assumptions.
7. Validate against physical-only and reduced-coupling baselines.
8. Use only validated resilience results as inputs to Stages 6–7.

---

## 13. Repository authority

| File / directory | Role |
|---|---|
| [`PROJECT_MEMORY.md`](PROJECT_MEMORY.md) | repository and framework authority |
| [`project/CANONICAL_7_STAGE_FRAMEWORK.md`](project/CANONICAL_7_STAGE_FRAMEWORK.md) | frozen seven-stage framework |
| [`project/CANONICAL_SYSTEM_DEFINITION.md`](project/CANONICAL_SYSTEM_DEFINITION.md) | canonical P–T–I–O system identity |
| [`project/FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md`](project/FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md) | full framework-level subsystem decomposition |
| [`project/STAGE_2_INTERDEPENDENCY_MECHANISMS.md`](project/STAGE_2_INTERDEPENDENCY_MECHANISMS.md) | frozen Stage-2 causal specification |
| [`figures/`](figures/) | figures and visual specifications |
| [`evidence/`](evidence/) | literature and evidence artifacts |
| [`methods/`](methods/) | mathematical, computational, review, and validation methods |
| [`provenance/`](provenance/) | provenance and audit records |
| [`archive/`](archive/) | superseded/historical artifacts |
| [`research_archive/`](research_archive/) | historical research material |

### Authority hierarchy

$$
\text{Current canonical project files}
>
\text{Current validated evidence}
>
\text{Historical project memory}
>
\text{Archived figures or drafts}.
$$

Historical P–W–T–SW, waste–drainage, equity-centered, or other superseded architectures are **not the current thesis system** unless explicitly reintroduced through a versioned framework change.

---

## 14. Scientific guardrails

- Use **MSE = Master of Science in Engineering** consistently.
- Preserve the canonical seven-stage framework unless an explicit change is approved.
- Treat $P,T$ as physical infrastructure systems and $I,O$ as informational/organizational layers.
- Never infer interdependency from correlation or common exposure alone.
- Distinguish structural connection from causal mechanism.
- Distinguish event time, causal delay, and characteristic timescale.
- Distinguish states, parameters, disturbances, observations, controls, and modes.
- Do not claim novelty for established concepts without systematic falsification.
- Treat proposed mathematical objects as candidate contributions until evidence closes the novelty question.
- Do not use generated figures as scientific authority.
- Require reproducible equations, assumptions, units, provenance, numerical checks, uncertainty analysis, and baseline comparison before strong conclusions.

> **Target scientific standard:** Clear system ontology + causal evidence + mathematical rigor + physical interpretability + falsifiable validation + reproducibility.

---

## 15. One-sentence thesis logic

> **Structure tells us where coupling is possible; mechanisms explain why effects occur; dynamics reveal how and how fast they propagate; feedback and control determine whether intervention can arrive in time; viability determines whether acceptable operation can be maintained; and verified resilience evidence informs sustainable transformation.**

---

## 16. Change control

A change to a canonical thesis object is valid only when it is explicitly approved, committed with a clear version/history message, propagated to dependent equations/figures/evidence tables, and checked for inconsistency with the current framework.

Until such a change is approved, this README and the linked canonical files define the active research direction of the **Master of Science in Engineering (MSE) thesis**.
