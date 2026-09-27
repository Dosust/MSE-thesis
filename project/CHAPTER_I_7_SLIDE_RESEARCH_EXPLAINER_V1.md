# Chapter I — Seven-Slide Research Explainer v1

**Canonical thesis title:** **Physics-Based Mathematical Engineering of Power–Transportation Interdependencies for Resilience**  
**Status:** SUPPORTING PRESENTATION SYNTHESIS — NON-CANONICAL  
**Basis:** Frozen Chapter I, canonical seven-stage framework, v4 RQ–SO–H authority, and three-framework supporting synthesis.  
**Purpose:** Explain the research simply and rigorously in no more than seven slides without changing the scientific contract.

---

## Formula-label rule

Use two labels in slide notes where useful:

- **[G] General / established foundation:** concept or mathematical family already established in the literature and adopted by the thesis.
- **[T] Thesis-defined synthesis / object:** integration, notation, handoff, comparator, or architecture defined by this thesis.

The presentation must preserve:

\[
\boxed{
\text{literature evidence}
\neq
\text{thesis synthesis}
\neq
\text{hypothesis}
\neq
\text{validated result}
}
\]

---

# Slide 1 — Background: why Power and Transportation must be studied together

## Main message

**Power and Transportation remain distinct physical systems, but their services and recovery can become directionally coupled.**

## Three bullets

1. EV charging connects mobility demand to the location, timing, capacity, and availability of electricity supply; charging demand can also affect distribution-system operation (Unterluggauer et al., 2022; Wei et al., 2019).
2. Transportation disruption can constrain repair access, crews, mobile resources, and restoration of electrical infrastructure (Fan et al., 2024; Lian et al., 2026).
3. The thesis therefore preserves native P and T physics while treating Information and Organization as supporting domains for knowledge and feasible action (Hall et al., 2016; Ibáñez et al., 2010).

## Formulas

**[T] Thesis ontology**
\[
\boxed{
\underbrace{P+T}_{\text{physical infrastructure}}
+
\underbrace{I+O}_{\text{knowledge and feasible-action support}}
}
\]

**[T] Directionality firewall**
\[
\boxed{P\rightarrow T\not\Rightarrow T\rightarrow P}
\]

## Visual

Large P and T blocks, separate arrows \(P\rightarrow T\) and \(T\rightarrow P\), disturbance field \(\eta(x,t)\), and smaller I/O support blocks.

---

# Slide 2 — What already exists, and what remains unresolved

## Main message

**The gap is not missing methods; it is the reliability of the scientific handoffs connecting them.**

## Three bullets

1. Already established: infrastructure interdependency models, coupled P–T models, resilience/recovery measures, viability/reachability methods, and multiobjective infrastructure decisions (Ouyang, 2014; Tong et al., 2025; Wang et al., 2024).
2. The unresolved problem is moving defensibly from structural possibility to qualified mechanism, dynamics, feasible response, resilience, consequences, and decision.
3. The thesis therefore tests integration and incremental engineering value rather than claiming that the component methods are individually new.

## Formulas

**[T] Gap logic**
\[
\boxed{
\text{established capability}
\rightarrow
\text{documented limitation}
\rightarrow
\text{unresolved handoff}
\rightarrow
\text{thesis test}
}
\]

**[T] Governing inference rule**
\[
\boxed{
\operatorname{Strength}(\text{claim})
\le
\operatorname{Strength}(\text{supporting evidence})
}
\]

## Visual

One horizontal chain:
Structure → Qualified Dependency → Dynamics → Knowledge/Action → Resilience → Consequences → Decision.

---

# Slide 3 — Overall research architecture

## Main message

**Seven scientific stages are grouped into three frameworks, and each output becomes the controlled input to the next framework.**

## Three bullets

1. **Framework I:** determine what exists and which directional P–T mechanisms are admissible.
2. **Framework II:** determine how the system evolves, what can be known/done, and whether services can remain acceptable or recover.
3. **Framework III:** determine how interventions change outcomes and which alternatives remain defensible.

## Formula

**[T] Three-framework grouping**
\[
\boxed{
\underbrace{S_1\leftrightarrow S_2}_{F_I}
\rightarrow
\underbrace{S_3\leftrightarrow S_4\leftrightarrow S_5}_{F_{II}}
\rightarrow
\underbrace{S_6\leftrightarrow S_7}_{F_{III}}
}
\]

**[T] Framework handoff logic**
\[
\boxed{
O_I\rightarrow I_{II},
\qquad
O_{II}\rightarrow I_{III},
\qquad
O_{III}=\mathcal A_{\rm joint}^{\star}
}
\]

## Cross-cutting rigor

Evidence • Provenance • Identification • Verification • Validation • UQ • Falsification • Reproducibility

---

# Slide 4 — Framework I: Structural–Mechanistic Qualification

## Main message

**Framework I decides which apparent P–T relations are scientifically allowed to enter the dynamic model.**

## Three bullets

1. **Plug-in role:** critical services, system boundary, raw evidence, spatial/temporal context, and candidate relations define what must be represented and where interaction could occur.
2. **Transformation role:** structural possibilities are filtered by mechanism, direction, activation, evidence, uncertainty, validity, and dynamic-readiness requirements (Kivelä et al., 2014; Ouyang, 2014; Rinaldi et al., 2001).
3. **Output role for Framework II:** only the graph, qualified/ready mechanisms, parameters, delays/timescales, and validity domain are admitted to coupled dynamics.

## Formulas

**[T] Input**
\[
I_I=
\left(
Q_P,Q_T,
\Omega_{\rm sys}^{+},
D_{\rm raw},
\Pi
\right)
\]

**[T] Transformation**
\[
\boxed{
\mathcal S_{PT}
\rightarrow
\mathfrak G_{PT}(x,t)
\rightarrow
\mathcal I^{cand}
\rightarrow
\mathcal I^{qualified}
\rightarrow
\mathcal I^{ready}
}
\]

**[T] Output**
\[
O_I=
\left(
\mathcal S_{PT},
\mathfrak G_{PT}(x,t),
\mathcal I^{ready},
\Theta,\Delta,\Omega
\right)
\]

## Scientific firewall

\[
\boxed{
\text{co-location}\neq\text{dependency},
\quad
\text{association}\neq\text{causality},
\quad
\text{qualification}\neq\text{dynamic readiness}
}
\]

---

# Slide 5 — Framework II: Dynamic–Operational Resilience

## Main message

**Framework II converts qualified mechanisms into physical behavior, feasible action, and service-resilience information.**

## Three bullets

1. **Plug-in role:** the P–T graph, dynamically ready mechanisms, initial physical state, disturbance, exogenous inputs, and qualified parameters specify the admissible dynamic problem.
2. **Transformation role:** physics generates trajectories; observation/estimation and I/O conditions determine feasible control; viability and reachability evaluate whether required services can remain or recover (Béné & Doyen, 2018; Doyen & De Lara, 2010; Vinod & Oishi, 2021).
3. **Output role for Framework III:** trajectories, service states, feasible actions, viability/recovery sets, resilience margin, and uncertainty qualification become the resilience diagnosis used to design interventions.

## Formulas

**[T] Input**
\[
I_{II}=
\left(
\mathfrak G_{PT},
\mathcal I^{ready},
Y_0^{phys},
\eta,
\nu^{exo},
\Theta
\right)
\]

**[T] Physical state**
\[
\boxed{
Y_3^{phys}(t)=
\left(
x_P(t),x_T(t),z_{PT}(t)
\right)
}
\]

**[G/T] Physics-based dynamic representation adopted by the thesis**
\[
\dot x=F_{\mathcal G}^{m}(x,z,u,\eta;\Theta),
\qquad
0=G_{\mathcal G}^{m}(x,z,u,\eta;\Theta)
\]

**[T] Knowledge/action chain**
\[
\boxed{
Y
\rightarrow
y
\rightarrow
\widehat Y
\rightarrow
(I,O)
\rightarrow
\mathcal U_{\rm feas}
\rightarrow
u
}
\]

**[G] Viability / recovery foundations**
\[
\mathcal V
=
\{Y_0:\exists u(\cdot),Y(t)\in K\},
\]

\[
\mathcal R_T
=
\{Y_0:\exists u(\cdot),Y(\tau)\in G_{\rm rec}\}.
\]

**[T] Output**
\[
O_{II}
=
\left(
Y(t),Q(t),\widehat Y(t),
\mathcal U_{\rm feas},
\mathcal V,\mathcal R,
\rho_{\mathcal V},
\Gamma_U
\right)
\]

---

# Slide 6 — Framework III: Intervention–Decision Engineering

## Main message

**Framework III asks which engineering changes remain defensible after resilience, resources, sustainability consequences, feasibility, and uncertainty are considered jointly.**

## Three bullets

1. **Plug-in role:** resilience diagnosis and candidate interventions define what can be changed and which alternatives must be compared.
2. **Transformation role:** each intervention modifies the system, produces typed consequences, passes feasibility, and is compared through Pareto/dominance and robustness/regret logic (Mitoulis et al., 2023; Tong et al., 2025; Sun et al., 2025; Zou & Chen, 2019).
3. **Output role:** the result is a defensible/nondominated intervention set, not an assumed universal optimum.

## Formulas

**[T] Input**
\[
I_{III}
=
\left(
\mathcal V,
\mathcal R,
\rho_{\mathcal V},
\Gamma_U,
\mathcal A_{cand}
\right)
\]

**[T] Intervention definition**
\[
a_k=
(\text{type},\text{location},\text{timing},\text{scale},\text{resources})
\]

**[T] Intervention transformation**
\[
\boxed{
\mathfrak M
\xrightarrow{a_k}
\mathfrak M^{a_k}
\rightarrow
\mathcal C(a_k)
}
\]

**[T] Consequence object**
\[
\boxed{
\mathcal C(a_k)=
\left(
\Delta\mathfrak R^{a_k},
\mathbf r^{a_k},
\mathcal E_{fx}^{a_k},
\mathcal E_{fy}^{a_k},
\Delta\mathbf J_{\rm sus}^{a_k},
\mathcal F^{a_k},
\mathbf U^{a_k}
\right)
}
\]

**[T] Decision transformation**
\[
\boxed{
\text{feasibility}
\rightarrow
\text{native-unit criteria}
\rightarrow
\text{Pareto/dominance}
\rightarrow
\text{robustness/regret}
}
\]

**[T] Output**
\[
\boxed{
O_{III}=\mathcal A_{\rm joint}^{\star}
}
\]

---

# Slide 7 — What the thesis adds and why it matters

## Main message

**The proposed contribution is the controlled evidence-to-decision integration and the test of whether each added layer provides meaningful engineering information.**

## Three bullets

1. RQ1–RQ2 establish the structural/evidence prerequisites; RQ3–RQ7 test the incremental value of dynamic coupling, I/O-constrained response, viability/reachability, intervention consequences, and joint decision evaluation.
2. The contribution is conditional: representation → qualified dependency → dynamics → feasible response → resilience → intervention → decision.
3. It matters because the final engineering claim remains traceable to the mechanism, evidence, uncertainty, comparator, and validity domain that support it.

## Formulas

**[T] Dynamic-coupling comparator**
\[
\boxed{
M_0
\quad\text{vs.}\quad
M_1
\quad\text{vs.}\quad
M_2
}
\]

where \(M_0\) is the **independent baseline**, \(M_1\) is **prescribed static coupling**, and \(M_2\) is **evidence-qualified dynamic coupling**.

**[T] Comparator definitions**

\[
\boxed{
\begin{aligned}
M_0 &: \text{Independent baseline},
& C_{PT}=C_{TP}=0,\\
M_1 &: \text{Prescribed static coupling},
& z=\Phi(x),\\
M_2 &: \text{Evidence-qualified dynamic coupling},
& z(t)=C(x(t-\delta);\widehat\theta).
\end{aligned}
}
\]

All three model classes have precedents in the literature. The thesis test is whether the evidence-qualified dynamic formulation provides incremental, decision-relevant information beyond the simpler matched baselines.

**[T] Contribution chain**
\[
\boxed{
\text{Representation}
\rightarrow
\text{Qualified Dependency}
\rightarrow
\text{Dynamics}
\rightarrow
\text{Feasible Response}
\rightarrow
\text{Resilience}
\rightarrow
\text{Intervention}
\rightarrow
\text{Decision}
}
\]

**[T] Contribution-status firewall**
\[
\boxed{
\text{proposed contribution}
\neq
\text{supported contribution}
\neq
\text{validated contribution}
\neq
\text{global novelty}
}
\]

---

# One-sentence presentation narrative

> Power and Transportation are distinct physical systems whose directional interactions must first be evidenced and qualified; those mechanisms are then admitted into physics-based dynamics, interpreted through what operators can know and feasibly do, tested for service viability and recovery under uncertainty, and finally used to compare engineering interventions and identify a defensible decision set.

---

# Visual rule

Use a light background, navy/charcoal structure, Light Sky Blue #87CEFA, Deep Sky Blue #00BFFF, and **no gold**. Preserve the input → transform → output grammar and show inter-framework handoffs explicitly.

---

# Citation note

The in-text citations above are inherited from the frozen Chapter-I evidence-controlled narrative. Full reference entries remain governed by the thesis citation/reference register; this presentation file does not replace that authority.
