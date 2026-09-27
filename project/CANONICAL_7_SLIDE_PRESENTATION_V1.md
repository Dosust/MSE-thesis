# CANONICAL 7-SLIDE THESIS PRESENTATION V1

**Status:** CANONICAL — PRESENTATION LAYER  
**Effective date:** 2026-09-27  
**Repository:** \`Dossiya-SE/MSE-thesis\`  
**Scope:** Short 7-slide thesis presentation wording and citation discipline.  
**Authority boundary:** This file is canonical for presentation wording only. It does **not** replace, amend, or override the frozen Chapter I scientific authorities, canonical RQ/SO/H files, or thesis governance documents. If any conflict is found, the scientific authority files govern.

## Canonical story

\[
\boxed{
\text{Reality}
\rightarrow
\text{What exists + Gap}
\rightarrow
\text{Question + Objective}
\rightarrow
\text{Architecture}
\rightarrow
\text{Qualify}
\rightarrow
\text{Resilience}
\rightarrow
\text{Decision + Test}
}
\]

## Citation discipline

1. External literature claims use visible in-text citations in the form \`(Author, Year)\`.
2. Thesis-defined RQ0–RQ7, SO1–SO7, H1–H5, framework labels, and thesis equations are thesis-defined objects and should not receive artificial literature citations.
3. Literature citations support only the claims they actually establish.
4. Existing dynamic, resilience, optimization, restoration, and planning models are treated as prior work; the thesis does not claim those components are individually novel.
5. Slide citations must remain visible through the final presentation version.

---

# Slide 1 — Background

**Power and Transportation are different systems, but they can affect each other during operation and recovery.**

- **P → T:** power supports charging, signals, and electrified mobility.
- **T → P:** transportation supports repair access and restoration.
- Their interaction changes how failures propagate and services recover **across space and time**.

\[
\boxed{P\rightleftarrows T}
\]

**Reality example**

\[
\text{Power outage}
\rightarrow
\text{signal failure}
\rightarrow
\text{congestion}
\rightarrow
\text{repair delay}
\]

**In-text citation:** *(Wei et al., 2019; Fotouhi et al., 2017).*

**Literature role:** Wei et al. review transportation–power interdependence; Fotouhi et al. model coupled traffic–power resilience.

---

# Slide 2 — What Exists and What Is Missing

**Coupled P–T models already exist, but they are built for different purposes and represent coupling differently.**

- Existing work covers **charging, equilibrium, operation, resilience, restoration, and planning**.
- Models differ in **mechanisms, assumptions, spatial–temporal detail, uncertainty, and objectives**.
- The thesis therefore focuses on **qualifying mechanisms before carrying them through the full engineering analysis**.

**In-text citation:** *(Wei et al., 2019; Unterluggauer et al., 2022; Song et al., 2025).*

### Thesis gap

\[
\boxed{
\text{How can valid P--T mechanisms be qualified and carried}
}
\]

\[
\boxed{
\text{from system structure to engineering decision?}
}
\]

### Why now?

Increasing EV and fast-charging integration makes transportation–power coupling more important operationally.

**In-text citation:** *(Wei et al., 2019; Song et al., 2025).*

---

# Slide 3 — Research Question and Objective

### RQ0

**How can coupled P–T systems move from qualified interdependencies to defensible engineering decisions under uncertainty?**

### General objective

**Develop and validate an evidence-grounded mathematical and engineering framework connecting:**

\[
\boxed{
\text{Structure}
\rightarrow
\text{Mechanisms}
\rightarrow
\text{Dynamics}
\rightarrow
\text{Response}
\rightarrow
\text{Resilience}
\rightarrow
\text{Intervention}
\rightarrow
\text{Decision}
}
\]

### Specific questions

- **RQ1–RQ2:** What exists, and which mechanisms are supported?
- **RQ3–RQ5:** What do they do, what can operators do, and can services remain or recover?
- **RQ6–RQ7:** What should change, and which alternatives remain defensible?

\[
\boxed{
RQ_k\Longleftrightarrow SO_k,
\qquad k=1,\ldots,7
}
\]

**Citation rule:** RQ0, RQ1–RQ7, SO1–SO7, and the general objective are thesis-defined research-contract objects. Do not add external citations merely to make them appear supported.

---

# Slide 4 — Three-Framework Architecture

**The research separates architecture, behavior, and engineering change.**

- **Framework I — System of Systems:** define the system and qualify mechanisms.
- **Framework II — Complex Dynamics:** model behavior, feasible response, and resilience.
- **Framework III — Engineering Decision:** evaluate interventions and defensible alternatives.

\[
\boxed{
\underbrace{F_I}_{\text{Architecture}}
\rightarrow
\underbrace{F_{II}}_{\text{Behavior}}
\rightarrow
\underbrace{F_{III}}_{\text{Change}}
}
\]

### Method roles

\[
\text{SoS}=\text{What exists and interacts?}
\]

\[
\text{Complex Dynamics}=\text{How does it evolve across }(x,t)?
\]

\[
\text{Engineering Decision}=\text{What should change?}
\]

**Systems Engineering** connects requirements, architecture, modeling, verification, validation, and decision across the whole process.

**In-text citation:** *(Maier, 1998; INCOSE).*

---

# Slide 5 — Framework I: Qualify the Coupling

**A possible connection is not automatically a valid dependency.**

- Identify **systems, services, locations, time, evidence, and candidate interfaces**.
- Test **direction, mechanism, activation, delay, uncertainty, and validity**.
- Only qualified mechanisms proceed to dynamic modeling.

\[
\boxed{
\mathcal I^{cand}
\rightarrow
\mathcal I^{qualified}
\rightarrow
\mathcal I^{ready}
}
\]

\[
\boxed{
\text{co-location}\neq\text{dependency}
}
\]

\[
\boxed{
P\rightarrow T
\not\Rightarrow
T\rightarrow P
}
\]

### Practical question

\[
\boxed{
\text{What is coupled, where, when, how, and under what conditions?}
}
\]

**In-text citation:** *(Fotouhi et al., 2017).*

**Literature role:** Coupled traffic–power studies demonstrate the need to represent explicit linking relationships rather than treating the two infrastructures as isolated systems.

---

# Slide 6 — Framework II: From Mechanisms to Resilience

**Qualified mechanisms are used to determine system behavior and whether services can remain or recover.**

- **RQ3/H1:** how coupling changes behavior across space and time.
- **RQ4/H2:** what operators can observe, estimate, coordinate, and control.
- **RQ5/H3:** whether electricity and mobility remain acceptable or recover under uncertainty.

\[
\boxed{
Y(x,t)
\rightarrow
\widehat Y(x,t)
\rightarrow
\mathcal U_{\rm feas}(x,t)
\rightarrow
(\mathcal V,\mathcal R)
}
\]

\[
\boxed{
\text{Resilience}
=
\text{Remain}
+
\text{Return}
+
\text{Uncertainty qualification}
}
\]

**In-text citation:** *(Fotouhi et al., 2017; Song et al., 2025).*

**Literature role:** Dynamic and resilience-oriented P–T models already exist; the thesis therefore does not claim dynamic P–T modeling itself as the contribution.

---

# Slide 7 — Framework III: Intervention, Decision, and Test

**The final question is whether better coupling information changes what engineers should do.**

- **RQ6/H4:** compare interventions by **location, timing, scale, resources, and consequences**.
- **RQ7/H5:** evaluate resilience, efficiency, sustainability, feasibility, and uncertainty together.
- **H1–H5:** test whether each additional layer provides useful information beyond a simpler alternative.

\[
\boxed{
a_k
\rightarrow
\mathcal C(a_k)
\rightarrow
\mathcal A_{\rm joint}^{\star}
}
\]

### Primary H1 comparison

\[
\boxed{
M_0
\quad\text{vs.}\quad
M_1
\quad\text{vs.}\quad
M_2
}
\]

\[
\begin{aligned}
M_0 &: \text{Independent systems}\\
M_1 &: \text{Static coupling}\\
M_2 &: \text{Evidence-qualified dynamic coupling}
\end{aligned}
\]

Existing research already uses coupled resilience and intervention optimization, so the thesis does **not** claim that coupling, resilience optimization, or dynamic traffic modeling are individually new.

**In-text citation:** *(Fotouhi et al., 2017; Zou & Chen, 2019).*

### Thesis test

\[
\boxed{
\text{Does qualified coupling information change}
}
\]

\[
\boxed{
\text{resilience understanding, intervention choice, or decision?}
}
\]

### Complete story

\[
\boxed{
\text{Reality}
\rightarrow
\text{Evidence}
\rightarrow
\text{Mechanisms}
\rightarrow
\text{Behavior}
\rightarrow
\text{Resilience}
\rightarrow
\text{Intervention}
\rightarrow
\text{Decision}
}
\]

---

## Short-reference anchors for slide notes / appendix

- **Wei et al. (2019)** — transportation and power-distribution interdependence review. DOI: \`10.1007/s40565-019-0516-7\`
- **Fotouhi et al. (2017)** — coupled traffic–power resilience modeling. DOI: \`10.1016/j.ress.2017.01.026\`
- **Unterluggauer et al. (2022)** — transportation–distribution charging-infrastructure planning review. DOI: \`10.1016/j.etran.2022.100163\`
- **Song et al. (2025)** — dynamic traffic–power coupled equilibrium model. DOI: \`10.1016/j.tra.2025.104590\`
- **Maier (1998)** — System-of-Systems architecting principles.
- **INCOSE** — Systems Engineering definition and life-cycle framing.
- **Zou & Chen (2019)** — coupled infrastructure resilience/intervention optimization.

## Change control

Any future wording change that alters the scientific meaning of:
- RQ0–RQ7,
- SO1–SO7,
- H1–H5,
- the three-framework responsibilities,
- the thesis gap,
- or the claim of novelty,

must first be checked against the canonical Chapter I and governance authorities before this presentation file is revised.
