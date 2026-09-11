# MSE Thesis — Multilayer Interdependent Power–Transportation Infrastructure Resilience

**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Repository status:** Active thesis repository  
**Framework status:** Seven-stage architecture frozen; Stage 1 system definition canonical; Stage 2 interdependency mechanisms frozen  
**Last major framework update:** 2026-09-11

> **Repository rule.** This repository is the sole active GitHub source of truth for the thesis. Historical architectures may remain under archive or project-memory paths for provenance, but they do not override the current canonical framework.

---

## 1. Thesis system

The thesis studies a

```math
\boxed{\textbf{Multilayer interdependent infrastructure system}}
```

with

```math
\boxed{P,T=\text{physical infrastructure systems}}
```

and

```math
\boxed{I,O=\text{informational and organizational layers}}.
```

The canonical system class is therefore:

> **A multilayer physical informational organizational interdependent Power–Transportation infrastructure system.**

Let

```math
\boxed{\mathcal S=\{P,T,I,O\}.}
```

The integrated state is represented at framework level by

```math
\boxed{
Y(t)=
\begin{bmatrix}
x_P(t)\\
x_T(t)\\
I(t)\\
O(t)
\end{bmatrix}.
}
```

The thesis does **not** treat Information and Organization as additional physical infrastructure sectors. Their role is to represent observation, communication, estimation, authority, coordination, decision-making, resources, mobilization, and intervention capability.

Canonical specification: [`project/CANONICAL_SYSTEM_DEFINITION.md`](project/CANONICAL_SYSTEM_DEFINITION.md)  
Full framework-level decomposition: [`project/FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md`](project/FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md)

---

## 2. Scientific objective

The research objective is to establish a rigorous mathematical and engineering framework that explains how interdependencies among Power, Transportation, Information, and Organization shape disruption propagation, system evolution, response capability, viability, and long-term sustainable transformation.

The governing reasoning chain is

```math
\boxed{
\text{Structure}
\rightarrow
\text{Causal Mechanisms}
\rightarrow
\text{Dynamics}
\rightarrow
\text{Feedback and Control}
\rightarrow
\text{Viability}
\rightarrow
\text{Sustainability Transformation}
}
```

The central modeling principle is:

```math
\boxed{
\text{Topology alone is insufficient: every retained cross-layer relation must have a causal mechanism, state dependence, and temporal interpretation.}
}
```

The thesis therefore moves from **what exists**, to **why effects propagate**, to **how and when they evolve**, to **whether intervention can preserve acceptable system behavior**.

---

## 3. Canonical seven-stage framework

The seven-stage architecture is frozen and must not be changed without explicit versioned approval.

```math
\boxed{
\text{Multilayer Structure}
\rightarrow
\text{Causal Mechanisms}
\rightarrow
\text{Coupled Hybrid Multiscale Dynamics}
\rightarrow
\text{Feedback \& Control}
\rightarrow
\text{Viability}
\rightarrow
\text{Resilience-to-Sustainability Transformation Interface}
\rightarrow
\text{Sustainable Transformation Pathways}
}
```

| Stage | Role | Main question | Current status |
|---|---|---|---|
| **1. Multilayer Structure** | P–T–I–O architecture | **What exists?** | **Canonical** |
| **2. Causal Mechanisms** | Cross-layer cause–effect pathways | **Why does disruption propagate?** | **Frozen** |
| **3. Coupled Hybrid Multiscale Dynamics** | Coupling + continuous dynamics + discrete events + timescales | **How and when does it evolve?** | Next formalization stage |
| **4. Feedback & Control** | Information, organization, decisions, intervention | **How does the system respond?** | Architecture established; formalization follows Stage 3 |
| **5. Viability** | Survival/recoverability under constraints | **Can it survive?** | Mathematical development planned |
| **6. Resilience-to-Sustainability Transformation Interface** | Translate resilience findings into transformation requirements | **What do resilience results imply for sustainability?** | Downstream synthesis |
| **7. Sustainable Transformation Pathways** | Technical, organizational, environmental and policy transformation | **What should be changed for long-term sustainability?** | Downstream synthesis |

Canonical framework authority: [`project/CANONICAL_7_STAGE_FRAMEWORK.md`](project/CANONICAL_7_STAGE_FRAMEWORK.md)

---

## 4. Stage 1 — Multilayer Structure

Stage 1 defines the system boundary and the internal decomposition of the four interacting subsystems.

### Power `P`

```math
\boxed{P=P_G\cup P_{Tr}\cup P_D\cup P_{DER}\cup P_C\cup P_{TP}}
```

representing generation, transmission, distribution, DER/storage, charging infrastructure, and traction-power supply.

### Transportation `T`

```math
\boxed{T=T_R\cup T_B\cup T_U\cup T_H\cup T_M}
```

representing road transport, electric buses, urban rail, regional/heavy electrified rail, and multimodal transfer.

### Information `I`

```math
\boxed{I=I_S\cup I_C\cup I_D\cup I_E\cup I_A\cup I_X\cup I_{\tau}}
```

representing sensing, communications, data, estimation, automation/signaling, cross-domain interoperability, and timing/synchronization.

### Organization `O`

```math
\boxed{O=O_A\cup O_G\cup O_D\cup O_C\cup O_R\cup O_W\cup O_L\cup O_M\cup O_X\cup O_K}
```

representing actors, governance, decisions, coordination, resources, workforce, logistics, restoration management, cross-sector collaboration, and learning/adaptation.

Stage 1 answers only the structural question. It does not, by itself, establish that every possible cross-layer arrow is causal.

---

## 5. Stage 2 — Interdependency Mechanisms

Stage 2 is now **canonical and frozen**.

The complete directed scope is

```math
\boxed{
\mathcal I=
\{
P\!\to\!T,T\!\to\!P,
P\!\to\!I,I\!\to\!P,
P\!\to\!O,O\!\to\!P,
T\!\to\!I,I\!\to\!T,
T\!\to\!O,O\!\to\!T,
I\!\to\!O,O\!\to\!I
\}.
}
```

Equivalently, six bidirectional interdependency families are audited:

```math
\boxed{
P\leftrightarrow T,\quad
P\leftrightarrow I,\quad
P\leftrightarrow O,\quad
T\leftrightarrow I,\quad
T\leftrightarrow O,\quad
I\leftrightarrow O.
}
```

Every accepted component-level interdependency is represented by

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
\right),
\qquad
\alpha,\beta\in\{P,T,I,O\},\ \alpha\neq\beta.
}
```

where the model must identify the source entity, receiving entity, causal mechanism, strength, delay, characteristic timescale, activation condition, operating mode, and relevant history.

The minimum causal chain is

```math
\boxed{
\text{Source}
\rightarrow
\text{Mechanism}
\rightarrow
\text{Receiver}
\rightarrow
\text{Effect}.
}
```

### Causal admissibility rule

Correlation, co-location, simultaneous failure, or exposure to the same hazard is not sufficient evidence of interdependency:

```math
\boxed{
\text{common exposure}\neq\text{causal interdependency}.
}
```

A retained relation requires a defensible transmission mechanism:

```math
\boxed{\alpha\xrightarrow{M_{ij}}\beta.}
```

This rule is fundamental to the thesis because it prevents common-cause effects from being misclassified as cross-system dependence.

Stage-2 authority: [`project/STAGE_2_INTERDEPENDENCY_MECHANISMS.md`](project/STAGE_2_INTERDEPENDENCY_MECHANISMS.md)

---

## 6. Stage 3 — Coupled Hybrid Multiscale Dynamics

The next major scientific task is to transform the Stage-2 causal architecture into a dynamic model.

The target framework is a coupled state evolution of the form

```math
\boxed{
\dot Y(t)=F_m\!\left(Y(t),Y(t-\delta),u(t),\eta(t);\theta,\mathcal G(t)\right),
\qquad
Y^{+}=J_e\!\left(Y^{-},e\right),
}
```

with continuous physical/informational/organizational evolution, discrete events or mode changes, delayed cross-layer effects, and heterogeneous process timescales.

The temporal architecture must keep distinct:

```math
\boxed{
\text{event time}\neq\text{causal delay }\delta\neq\text{process timescale }\tau.
}
```

Representative time classes to be formalized and evidenced are:

```math
\boxed{
\begin{aligned}
\text{Intrinsic:}&\ \tau_P,\tau_T,\tau_I,\tau_O,\\
\text{Interaction:}&\ \delta_{ij},\tau_{ij},a_{ij}(t),\mathcal H_t,\\
\text{Disruption:}&\ \tau_H,T_{\rm exp},\tau_C,\\
\text{Response/viability:}&\ \tau_R,T_{\rm exit},T_{\rm rec},\\
\text{Strategic:}&\ \tau_A,\tau_{Tr},t_k,\Delta t_k,T_H.
\end{aligned}
}
```

Dimensionless ratios such as

```math
\Gamma_{\alpha\beta}=\frac{\tau_\alpha}{\tau_\beta}
```

will be used only as regime descriptors unless a critical threshold is derived from the coupled dynamics or supported by evidence.

No universal timescale ordering or response threshold will be assumed without validation.

---

## 7. Stage 4 — Observation, Organization, Feedback and Control

The physical system is not assumed to respond autonomously. The control architecture is

```math
\boxed{
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
}
```

Conceptually:

```math
\boxed{
\text{REALITY}
\rightarrow
\text{OBSERVE}
\rightarrow
\text{KNOW}
\rightarrow
\text{DECIDE}
\rightarrow
\text{ACT}.
}
```

A generic representation is

```math
\boxed{
y=H(X)+\nu_y,\qquad
\widehat X=\mathcal E(y_{[0,t]},I),\qquad
u=\pi(\widehat X,I,O),\qquad
u\in\mathcal U(I,O).
}
```

The scientific question is not merely whether a control exists, but whether information quality, communication latency, organizational delay, authority, resources, logistics, and coordination allow an admissible intervention to arrive before critical system degradation.

---

## 8. Stage 5 — Controlled Sustainable Viability

Stage 5 asks whether acceptable system trajectories can be maintained under disturbance and admissible intervention.

The admissible region will be defined from explicit engineering, service, informational, organizational, and sustainability constraints:

```math
\boxed{K_{\rm sus}=\{Y:g(Y)\le0\}.}
```

The corresponding controlled viability object is

```math
\boxed{
\mathcal V_{\rm sus}^{u}
=\operatorname{Viab}_{F,\mathcal U(I,O)}(K_{\rm sus}).
}
```

The exact finite-horizon, robust, stochastic, or time-varying formulation must be selected from the evidence and model assumptions and documented explicitly; it will not be changed silently between analyses.

Candidate geometric diagnostics include the system's distance to the viability boundary and time to loss of viability, but their final definitions, normalization, uncertainty treatment, and computational method remain subject to formal Stage-5 development and validation.

---

## 9. Stages 6–7 — From Resilience Evidence to Sustainable Transformation

The framework deliberately separates resilience analysis from long-term transformation.

```math
\boxed{
\underbrace{\text{Stages 1--5}}_{\text{resilience analysis}}
\rightarrow
\underbrace{\text{Stage 6}}_{\text{translation interface}}
\rightarrow
\underbrace{\text{Stage 7}}_{\text{sustainable transformation pathways}}.
}
```

Stage 6 translates verified resilience results—critical mechanisms, temporal bottlenecks, control limitations, and viability constraints—into transformation requirements.

Stage 7 evaluates what should change in the technical, informational, organizational, environmental, or policy architecture to improve long-term system sustainability.

The governing principle is:

```math
\boxed{
\textbf{Resilience is analyzed inside the model; sustainability is informed by the model.}
}
```

---

## 10. Evidence architecture

The thesis uses a systematic, evidence-gated workflow. Literature is not collected only to summarize papers; it is used to support or falsify specific mathematical objects and causal mechanisms.

The evidence-to-model chain is

```math
\boxed{
\text{Literature}
\xrightarrow{\text{systematic review / PRISMA}}
\text{evidence structure}
\xrightarrow{\text{formalization}}
(\mathcal G,\mathfrak I,F,J,\tau,I,O,K,\mathcal V,u).
}
```

For each proposed interdependency, the evidence extraction should seek, where reported:

```math
\boxed{
(E_i^\alpha,E_j^\beta,M_{ij},w_{ij},\delta_{ij},\tau_{ij},a_{ij},m,\mathcal H_t)
}
```

plus disturbance type, measured outcome, model family, data source, calibration, validation method, uncertainty treatment, and limitations.

### Evidence discipline

The repository must preserve the distinction

```math
\boxed{
\text{domain evidence}
\neq
\text{transferable methodological evidence}
\neq
\text{mathematical theory}.
}
```

A method demonstrated in another infrastructure domain may justify a modeling technique, but it is not automatically empirical evidence for Power–Transportation behavior.

Evidence resources are maintained under [`evidence/`](evidence/) and methodological controls under [`methods/`](methods/).

---

## 11. Validation and falsification strategy

Every major mathematical layer creates a corresponding validation obligation.

| Layer | Required validation logic |
|---|---|
| **Structure** | verify component/system boundary and explicit interface mapping |
| **Interdependency** | direction + mechanism + source/receiver + evidence; reject common-cause-only relations |
| **Dynamics** | dimensional consistency, physical laws, limiting cases, event logic, numerical verification |
| **Timescales** | distinguish delay from characteristic process time; quantify uncertainty and context dependence |
| **Information** | test observability, latency, missing/noisy data, estimation sensitivity |
| **Organization** | test decision/coordination/resource constraints and response delays |
| **Control** | compare admissible interventions against explicit baselines under common scenarios |
| **Viability** | verify set computation, boundary behavior, constraint satisfaction, and sensitivity to model error |
| **Transformation** | trace each recommendation back to verified resilience evidence rather than qualitative assertion |

The general rule is

```math
\boxed{
\text{Claim}\rightarrow\text{observable or mathematical test}\rightarrow\text{falsification opportunity}\rightarrow\text{evidence-backed conclusion}.
}
```

No method is considered useful merely because it is mathematically sophisticated. It must answer a defined scientific question and survive comparison with a simpler baseline where appropriate.

---

## 12. Current research state

The current progression is:

```math
\boxed{
\underbrace{\text{Stage 1}}_{\text{defined}}
\rightarrow
\underbrace{\text{Stage 2}}_{\text{frozen}}
\rightarrow
\underbrace{\text{Stage 3}}_{\text{next: formalize dynamics and timescales}}
\rightarrow
\underbrace{\text{Stage 4}}_{\text{formalize feedback/control}}
\rightarrow
\underbrace{\text{Stage 5}}_{\text{compute/test viability}}
\rightarrow
\underbrace{\text{Stages 6--7}}_{\text{translate validated resilience evidence into transformation}}
}
```

The immediate technical program is:

1. complete the component-level decomposition of all 12 Stage-2 directional interdependencies;
2. attach evidence, mechanism, carrier/effect, delay, timescale, activation and mode information to each accepted relation;
3. map the accepted Stage-2 objects into the Stage-3 coupled hybrid multiscale equations;
4. establish the temporal competition between disruption propagation and information/organizational response;
5. close the Stage-4 observation–decision–action loop;
6. define and compute the Stage-5 admissible and viability sets under declared uncertainty/control assumptions;
7. validate the framework against simpler physical-only or reduced-coupling baselines;
8. use only validated resilience results as inputs to Stages 6–7.

---

## 13. Repository authority and organization

The principal current sources of truth are:

| File / directory | Role |
|---|---|
| [`PROJECT_MEMORY.md`](PROJECT_MEMORY.md) | current repository and framework authority |
| [`project/CANONICAL_7_STAGE_FRAMEWORK.md`](project/CANONICAL_7_STAGE_FRAMEWORK.md) | frozen seven-stage architecture |
| [`project/CANONICAL_SYSTEM_DEFINITION.md`](project/CANONICAL_SYSTEM_DEFINITION.md) | canonical P–T–I–O system identity |
| [`project/FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md`](project/FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md) | framework-level subsystem decomposition |
| [`project/STAGE_2_INTERDEPENDENCY_MECHANISMS.md`](project/STAGE_2_INTERDEPENDENCY_MECHANISMS.md) | frozen Stage-2 causal scope |
| [`figures/`](figures/) | thesis figures and visual specifications |
| [`evidence/`](evidence/) | literature/evidence artifacts |
| [`methods/`](methods/) | mathematical, computational, review and validation methods |
| [`provenance/`](provenance/) | provenance and audit records |
| [`archive/`](archive/) and [`research_archive/`](research_archive/) | superseded/historical material |

### Authority rule

When an older file conflicts with the current framework, use the following priority:

```math
\boxed{
\text{current canonical project files}
>
\text{current validated evidence}
>
\text{historical project memory}
>
\text{archived figures or drafts}.
}
```

Historical P–W–T–SW, waste–drainage, equity-centered, or other superseded architectures retained in repository history are **not the current thesis system** unless explicitly reintroduced through a versioned framework change.

---

## 14. Scientific guardrails

This repository follows the following thesis-wide rules:

- use **MSE = Master of Science in Engineering** consistently;
- preserve the canonical seven-stage framework unless a change is explicitly approved;
- treat `P,T` as physical infrastructure systems and `I,O` as informational/organizational layers;
- never infer interdependency from correlation or common exposure alone;
- distinguish structural connection from causal mechanism;
- distinguish event time, causal delay, and characteristic timescale;
- distinguish physical state, information state, organizational state, parameters, and controls;
- do not claim novelty for individual established concepts without systematic falsification;
- label proposed mathematical objects as candidate contributions until the evidence review closes the relevant novelty question;
- do not use a generated figure as scientific authority;
- require reproducible equations, assumptions, units, data provenance, numerical checks, uncertainty analysis, and baseline comparison before strong conclusions.

The target standard is:

```math
\boxed{
\textbf{clear system ontology}
+
\textbf{causal evidence}
+
\textbf{mathematical rigor}
+
\textbf{physical interpretability}
+
\textbf{falsifiable validation}
+
\textbf{reproducibility}.
}
```

---

## 15. One-sentence thesis logic

> **Structure tells us where coupling is possible; mechanisms explain why effects occur; dynamics reveal how and how fast they propagate; feedback and control determine whether intervention arrives effectively; viability determines whether acceptable operation can be maintained; and the resulting resilience evidence informs sustainable transformation.**

---

## 16. Change control

A change to a canonical thesis object is valid only when it is explicitly approved, committed with a clear message, propagated to dependent files/figures, and checked for inconsistency with the current framework.

Until such a change is made, this README and the linked canonical specifications define the active research direction of the **Master of Science in Engineering (MSE) thesis**.
