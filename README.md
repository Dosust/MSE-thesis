# MSE Thesis — Multilayer Interdependent Power–Transportation Infrastructure Resilience

**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Repository:** Active thesis source of truth  
**Framework status:** Seven-stage architecture frozen  
**Research status:** Stage 1 defined; Stage 2 frozen; Stage 3 frozen; Stage 4 next  
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

Therefore

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
I(t)\\
O(t)
\end{bmatrix}.
$$

$P$ and $T$ are the physical systems. $I$ represents sensing, communication, estimation, information quality, latency, synchronization, and signaling. $O$ represents authority, coordination, decision-making, resources, workforce, logistics, mobilization, and intervention capability.

Canonical files:
- [`project/CANONICAL_SYSTEM_DEFINITION.md`](project/CANONICAL_SYSTEM_DEFINITION.md)
- [`project/FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md`](project/FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md)

---

## 2. Scientific objective

The research determines how causal interdependencies among $P$, $T$, $I$, and $O$ shape disruption propagation, coupled system evolution, response capability, recovery, viability, and sustainable transformation.

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

> **Modeling principle:** topology alone is insufficient. Every retained cross-layer relation must have a defensible causal mechanism, a state-dependent effect, and a temporal interpretation.

---

## 3. Canonical seven-stage framework

1. **Multilayer Structure**
2. **Causal Mechanisms**
3. **Coupled Hybrid Multiscale Dynamics**
4. **Feedback & Control**
5. **Viability**
6. **Resilience-to-Sustainability Transformation Interface**
7. **Sustainable Transformation Pathways**

| Stage | Main question | Status |
|---|---|---|
| **1. Multilayer Structure** | What exists? | Canonical |
| **2. Causal Mechanisms** | Why does disruption propagate? | Frozen |
| **3. Coupled Hybrid Multiscale Dynamics** | How, when, and where does it evolve and propagate? | Frozen |
| **4. Feedback & Control** | How does the system observe, decide, and respond? | **Next formalization stage** |
| **5. Viability** | Can acceptable operation be maintained? | To formalize |
| **6. Transformation Interface** | What do resilience results imply for sustainability? | Downstream |
| **7. Sustainable Transformation Pathways** | What should change? | Downstream |

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
I=I_S\cup I_C\cup I_D\cup I_E\cup I_A\cup I_X\cup I_{\tau},
$$

$$
O=O_A\cup O_G\cup O_D\cup O_C\cup O_R\cup O_W\cup O_L\cup O_M\cup O_X\cup O_K.
$$

Stage 1 answers **what exists**. It does not establish causality by itself.

---

## 5. Stage 2 — Interdependency Mechanisms

Stage 2 is **canonical and frozen**.

$$
\{P,T,I,O\}\longrightarrow\mathcal I^{\alpha\beta}.
$$

The directed scope is

$$
\begin{aligned}
\mathcal I=\{&
P\to T,\ T\to P,\ P\to I,\ I\to P,\ P\to O,\ O\to P,\\
&T\to I,\ I\to T,\ T\to O,\ O\to T,\ I\to O,\ O\to I
\}.
\end{aligned}
$$

Equivalently,

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

Stage 3 is now **canonical and frozen**. It maps accepted Stage-2 mechanisms into heterogeneous, delayed, hybrid, multirate evolution without forcing all four layers into one equation class.

The four-layer state remains

$$
Y(t)=
\begin{bmatrix}
x_P(t)\\x_T(t)\\z_I(t)\\z_O(t)
\end{bmatrix},
$$

while the Stage-3 augmented hybrid state is

$$
\widetilde Y(t)=\big(Y(t),m(t)\big).
$$

A canonical Stage-3 representation is

$$
\dot Y_c(t)=F^{m(t)}\!\left[Y_c(t),Y_d(t),Y(t-\boldsymbol\delta),h(\mathbf r,t);\mathcal G(t),\mathcal H_t\right],
$$

with algebraic constraints and event-driven updates

$$
0=G^{m(t)}(Y_c,Y_d,h;\mathcal G),
$$

$$
Y_d^+=R_e(\widetilde Y^-,e),\qquad
m^+=\Delta_m(m^-,\widetilde Y^-,e),\qquad
\mathcal G^+=\Psi(\mathcal G^-,\widetilde Y^-,e,\mathcal H_t).
$$

The temporal rule is

$$
\text{event time}
\neq
\text{causal delay }\delta
\neq
\text{characteristic timescale }\tau.
$$

| Temporal class | Representative quantities |
|---|---|
| Intrinsic | $\tau_P,\tau_T,\tau_I,\tau_O$ |
| Interaction | $\delta_{ij},\tau_{ij},a_{ij}(t),\mathcal H_t$ |
| Disruption | $\tau_H,T_{\rm exp},\tau_C$ |
| Response/viability | $\tau_R,T_{\rm exit},T_{\rm rec}$ |
| Strategic | $\tau_A,\tau_{Tr},t_k,\Delta t_k,T_H$ |

For spatial propagation, Stage 3 introduces component cascade-arrival time

$$
T_C(j)=\inf\{t>t_0:j\text{ enters a predefined disrupted state}\},
$$

and, only where a spatial-front interpretation is physically meaningful,

$$
v_c(t)=\frac{dr_c(t)}{dt}.
$$

Dimensionless timescale ratios remain regime descriptors rather than universal thresholds unless critical values are derived from the coupled dynamics or supported by evidence.

Stage-3 authority: [`project/STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md`](project/STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md)

---

## 7. Stage 4 — Feedback & Control

Stage 4 is the **next framework formalization task**. The observation–decision–action loop is

$$
X\rightarrow y\rightarrow I\rightarrow\widehat X\rightarrow O\rightarrow u\rightarrow X.
$$

For analytical and numerical work,

$$
y=H(X)+\varepsilon_y,\qquad
\widehat X=\mathcal E(y_{[0,t]},I),\qquad
u=\pi(\widehat X,I,O),\qquad
u\in\mathcal U(I,O).
$$

Here the policy symbol is $\pi$ and the physical intervention/action variable is $u$; the final Stage-4 specification will explicitly separate policy, command generation, admissible action set, information constraints, organizational constraints, and response delay.

The scientific question is whether sensing, communication, estimation, authority, coordination, resources, logistics, and organizational delays allow an admissible intervention to arrive before critical degradation.

---

## 8. Stage 5 — Viability

$$
K_{\rm sus}=\{Y:g(Y)\le0\},
$$

and

$$
\mathcal V_{\rm sus}^{u}
=
\operatorname{Viab}_{F,\mathcal U(I,O)}(K_{\rm sus}).
$$

The final finite-horizon, robust, stochastic, or time-varying formulation must be selected from evidence and assumptions and documented explicitly.

Candidate diagnostics include signed distance to the viability boundary, time to viability loss, recovery time, interface criticality, and intervention feasibility.

---

## 9. Stages 6–7 — Resilience to Sustainable Transformation

$$
\underbrace{\text{Stages 1--5}}_{\text{resilience analysis}}
\rightarrow
\underbrace{\text{Stage 6}}_{\text{translation interface}}
\rightarrow
\underbrace{\text{Stage 7}}_{\text{sustainable transformation pathways}}.
$$

Stage 6 converts verified resilience findings into transformation requirements. Stage 7 evaluates what should change for long-term sustainability.

> **Governing principle:** Resilience is analyzed inside the model; sustainability is informed by the model.

---

## 10. Evidence architecture

$$
\text{Literature}
\xrightarrow{\text{systematic review / PRISMA}}
\text{Evidence Structure}
\xrightarrow{\text{formalization}}
(\mathcal G,\mathfrak I,F,J,\tau,I,O,K,\mathcal V,u).
$$

For each proposed interdependency, extraction seeks

$$
(E_i^\alpha,E_j^\beta,M_{ij},w_{ij},\delta_{ij},\tau_{ij},a_{ij},m,\mathcal H_t),
$$

plus disturbance, measured effect, model family, data source, calibration, validation, uncertainty treatment, and limitations.

The thesis preserves

$$
\text{domain evidence}
\neq
\text{transferable methodological evidence}
\neq
\text{mathematical theory}.
$$

Evidence: [`evidence/`](evidence/)  
Methods: [`methods/`](methods/)

---

## 11. Validation and falsification

| Layer | Required validation logic |
|---|---|
| Structure | verify system boundary, taxonomy, and interface mapping |
| Interdependency | require direction + source + mechanism + receiver + effect + evidence |
| Dynamics | check dimensions, native physical laws, limiting cases, event logic, numerical implementation, and synchronization |
| Timescales | separate causal delay from process duration and quantify uncertainty |
| Spatial propagation | validate cascade-arrival definitions and use spatial-front quantities only where physically meaningful |
| Information | test availability, latency, freshness, missing/noisy data, and estimation sensitivity |
| Organization | test organizational states, resources, logistics, event timing, and response delay |
| Control | compare interventions against explicit baselines |
| Viability | verify set computation, boundary behavior, constraints, and sensitivity to model error |
| Transformation | trace recommendations to verified resilience evidence |

A key Stage-3 falsification method is **coupling ablation**: remove a selected Stage-2 coupling under otherwise matched conditions and test whether state trajectory, event order, propagation, recovery, or later viability conclusions change materially and reproducibly.

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
\text{Stage 1: defined}
\rightarrow
\text{Stage 2: frozen}
\rightarrow
\text{Stage 3: frozen}
\rightarrow
\text{Stage 4: next}
\rightarrow
\text{Stage 5: viability}
\rightarrow
\text{Stages 6--7: transformation}.
$$

### Immediate technical program

1. Complete the component-level evidence decomposition of all 12 Stage-2 directions.
2. Parameterize accepted Stage-2 relations with mechanism, effect, delay, timescale, activation, mode, and history.
3. Implement and falsify the frozen Stage-3 hybrid delayed multirate dynamics under explicit subsystem assumptions.
4. Verify event chronology, dynamic topology, cascade-arrival time, and spatial propagation quantities where applicable.
5. Perform coupling ablation and sensitivity/uncertainty analysis for Stage-3 mechanisms.
6. Formalize Stage 4: observation, state estimation, organizational decision processes, admissible actions, and feedback/control.
7. Define and compute Stage-5 admissible and viability sets under declared uncertainty/control assumptions.
8. Validate against physical-only and reduced-coupling baselines.
9. Use only validated resilience results as inputs to Stages 6–7.

---

## 13. Repository authority

| File / directory | Role |
|---|---|
| [`PROJECT_MEMORY.md`](PROJECT_MEMORY.md) | repository and framework authority |
| [`project/CANONICAL_7_STAGE_FRAMEWORK.md`](project/CANONICAL_7_STAGE_FRAMEWORK.md) | frozen seven-stage framework |
| [`project/CANONICAL_SYSTEM_DEFINITION.md`](project/CANONICAL_SYSTEM_DEFINITION.md) | canonical P–T–I–O system identity |
| [`project/FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md`](project/FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md) | framework-level subsystem decomposition |
| [`project/STAGE_2_INTERDEPENDENCY_MECHANISMS.md`](project/STAGE_2_INTERDEPENDENCY_MECHANISMS.md) | frozen Stage-2 causal specification |
| [`project/STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md`](project/STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md) | frozen Stage-3 dynamic specification |
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
- Preserve the canonical seven-stage framework unless an explicit change is approved.
- Treat $P,T$ as physical infrastructure systems and $I,O$ as informational/organizational layers.
- Never infer interdependency from correlation or common exposure alone.
- Distinguish structural connection from causal mechanism.
- Distinguish event time, causal delay, and characteristic timescale.
- Distinguish four-layer state $Y$ from Stage-3 mode $m$ and augmented hybrid state $\widetilde Y$.
- Distinguish states, parameters, disturbances, observations, policies, controls, and modes.
- Do not claim novelty for established concepts or combinations without systematic falsification.
- Do not use generated figures as scientific authority.
- Require equations, assumptions, units, provenance, numerical checks, uncertainty analysis, and baseline comparison before strong conclusions.

> **Target standard:** clear system ontology + causal evidence + mathematical rigor + physical interpretability + falsifiable validation + reproducibility.

---

## 15. Thesis logic

> **Structure tells us where coupling is possible; mechanisms explain why effects occur; dynamics reveal how, when, and where they propagate; feedback and control determine whether intervention can arrive in time; viability determines whether acceptable operation can be maintained; and verified resilience evidence informs sustainable transformation.**

---

## 16. Change control

A canonical thesis object changes only when the revision is explicitly approved, committed with a clear history message, propagated to dependent equations/figures/evidence tables, and checked against the current framework.

Until then, this README and the linked canonical files define the active research direction of the **Master of Science in Engineering (MSE) thesis**.
