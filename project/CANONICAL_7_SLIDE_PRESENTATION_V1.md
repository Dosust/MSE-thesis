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


---

# CANONICAL VISUAL SPECIFICATION — 7-SLIDE PRESENTATION

**Status:** CANONICAL — PRESENTATION VISUAL LAYER  
**Rule:** The slide wording above is frozen. The specifications below define only the illustration, spatial organization, and visual grammar. They must not introduce new scientific claims or replace slide text.

## Global visual grammar

- **Canvas:** 16:9 landscape; white or very light neutral background.
- **Primary colors:** Light Sky Blue \`#87CEFA\`, Deep Sky Blue \`#00BFFF\`, navy/charcoal, white. **No gold.**
- **Power layer:** navy / Deep Sky Blue.
- **Transportation layer:** Light Sky Blue / charcoal.
- **Cross-system mechanism:** thin Deep Sky Blue directional arrow; never a generic bidirectional arrow unless both directions are separately evidenced.
- **Inputs:** circles / spheres.
- **Physical systems or models:** rectangles / cuboids.
- **Qualification gates:** diamonds.
- **Dynamic evolution:** trajectories, layered surfaces, vector fields, or time-space manifolds.
- **Interventions:** cone / triangular wedge.
- **Decision narrowing:** pyramid / trapezoid / Pareto frontier.
- **Uncertainty:** translucent envelope, distribution, interval band, or scenario cloud.
- **Cross-cutting traceability:** thin lower rail for evidence, provenance, V&V, UQ, falsification, and reproducibility.
- Every visual element must encode a scientific role; avoid decorative geometry.

---

## Slide 1 — Background

### Visual purpose
Show **two physically distinct systems** and one concrete feedback pathway without implying that all P–T relations are symmetric.

### Recommended composition
- **Left half:** Power network as a layered cuboid: substation → feeder → charger / signal.
- **Right half:** Transportation network as a road-network layer: intersections → vehicles → repair route.
- **Between them:** two separate directional arrows:
  - upper arrow \(P\rightarrow T\)
  - lower arrow \(T\rightarrow P\)
- **Bottom strip:** four-step cascade matching the existing slide formula:
  power outage → signal failure → congestion → repair delay.
- Add a subtle \((x,t)\) coordinate grid behind the two systems to encode space-time dependence.

### Geometry
\[
\boxed{
\text{Power cuboid}
\;\xrightleftarrows[\,T\to P\,]{\,P\to T\,}\;
\text{Transportation cuboid}
}
\]

### Avoid
Do not draw one undifferentiated double-headed coupling edge as the only mechanism depiction.

---

## Slide 2 — What Exists and What Is Missing

### Visual purpose
Show that **many capabilities already exist**, while the thesis gap is the unresolved connection among them.

### Recommended composition
- **Top row:** six compact capability nodes:
  Charging | Equilibrium | Operation | Resilience | Restoration | Planning.
- Represent each as a separate rounded rectangle or hexagonal cell to show that these are established but differently scoped modeling capabilities.
- **Middle:** a sequence of heterogeneous model blocks with visibly different internal structures, emphasizing different assumptions, scales, uncertainty treatments, and objectives.
- **Center-right:** a broken bridge / unclosed handoff between “system structure” and “engineering decision.”
- **Bottom:** the exact thesis-gap equation already on the slide, visually spanning the broken bridge.
- A small EV/fast-charging icon may sit near the “Why now?” line, but should not dominate the slide.

### Geometry
\[
\boxed{
\{\text{existing capabilities}\}
\longrightarrow
\text{unresolved scientific handoffs}
\longrightarrow
\text{thesis gap}
}
\]

### Avoid
Do not portray the literature as absent or scientifically inadequate in general; the visual must show **existing strength + unresolved integration**.

---

## Slide 3 — Research Question and Objective

### Visual purpose
Map **RQ0 → seven question/objective pairs → one complete research chain**.

### Recommended composition
- **Top center:** RQ0 inside one large ellipse or capsule spanning the slide width.
- **Middle:** seven numbered nodes \(1\ldots7\) arranged left-to-right along one scientific spine:
  Structure → Mechanisms → Dynamics → Response → Resilience → Intervention → Decision.
- **Under each node:** a small paired marker \(RQ_k\leftrightarrow SO_k\).
- **Bottom:** group the seven nodes into three brackets:
  - RQ1–RQ2
  - RQ3–RQ5
  - RQ6–RQ7
- Use the existing objective equation as the central spine rather than adding more prose.

### Geometry
\[
\boxed{
RQ_0
\Downarrow
\left[
RQ_1\leftrightarrow SO_1
\rightarrow\cdots\rightarrow
RQ_7\leftrightarrow SO_7
\right]
}
\]

### Avoid
Do not add hypotheses here; Slide 3 is about the research contract, not testing.

---

## Slide 4 — Three-Framework Architecture

### Visual purpose
Make the **three framework responsibilities** immediately distinguishable.

### Recommended composition
Use three large connected modules occupying the full width:

1. **Framework I — Architecture**
   - shape: cuboid / layered System-of-Systems stack
   - show Power and Transportation as separate layers with candidate interfaces.

2. **Framework II — Behavior**
   - shape: central dynamic manifold / trajectory surface
   - include state evolution, observation, control, and viable/recoverable regions.

3. **Framework III — Change**
   - shape: intervention cone feeding a Pareto / decision pyramid
   - show engineering change narrowing toward defensible alternatives.

- Connect modules with thick solid handoff arrows \(F_I\rightarrow F_{II}\rightarrow F_{III}\).
- Place a thin **Systems Engineering** rail underneath:
  Requirements → Architecture → Model → V&V → Decision.
- Carry a subtle \((x,t)\) axis across Frameworks I and II.

### Geometry
\[
\boxed{
\underbrace{F_I}_{\text{Architecture}}
\rightarrow
\underbrace{F_{II}}_{\text{Behavior}}
\rightarrow
\underbrace{F_{III}}_{\text{Change}}
}
\]

### Avoid
Do not visually collapse the seven stages into only three stages; the three frameworks are groupings of the seven-stage authority.

---

## Slide 5 — Framework I: Qualify the Coupling

### Visual purpose
Show the conversion **candidate relation → qualified mechanism → dynamically ready mechanism**.

### Recommended composition
Use a strict **Input → Transform → Output** pipeline.

### Input
Five circles/spheres:
- systems/services
- location
- time
- evidence
- candidate interface

### Transform
- **Step 1:** typed P–T graph cuboid.
- **Step 2:** candidate-interface diamond.
- **Step 3:** qualification gate composed of six thin filters:
  Direction | Mechanism | Activation | Delay | Uncertainty | Validity.
- Use a crossed-out proximity symbol beside the gate to reinforce:
  co-location ≠ dependency.
- Use two separate arrows \(P\to T\) and \(T\to P\) to reinforce directionality.

### Output
One sealed output block:
\[
\mathcal I^{ready}
\]
feeding directly toward Framework II.

### Geometry
\[
\boxed{
\text{Evidence + structure}
\rightarrow
\mathcal I^{cand}
\rightarrow
\mathcal I^{qualified}
\rightarrow
\mathcal I^{ready}
}
\]

### Avoid
Do not show coupling strength as already known unless it has passed identification/estimation requirements.

---

## Slide 6 — Framework II: From Mechanisms to Resilience

### Visual purpose
Show how a qualified mechanism becomes **physical behavior → knowledge → feasible action → resilience**.

### Recommended composition
Use four connected zones:

1. **Physical dynamics**
   - dynamic surface / state trajectory \(Y(x,t)\)
   - separate Power and Transportation states feeding the coupled trajectory.

2. **Observation and estimation**
   - sensor icon / sphere producing \(y\)
   - estimator producing \(\widehat Y\)
   - uncertainty envelope around the estimate.

3. **Feasible action**
   - control gate producing \(\mathcal U_{\rm feas}\)
   - visibly distinguish “physically possible” from “operationally feasible.”

4. **Resilience geometry**
   - acceptable set \(K\)
   - inner viable set \(\mathcal V\)
   - recovery arrow toward \(\mathcal R\)
   - boundary / distance cue for resilience margin if space permits.

### Geometry
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

Use three visually distinct resilience cues:
- **Remain:** trajectory staying inside \(\mathcal V\)
- **Return:** trajectory re-entering acceptable region
- **Uncertainty:** translucent envelope/scenario fan

### Avoid
Do not use only a generic resilience curve; the purpose is to show the added viability/recovery structure while retaining conventional metrics as comparators.

---

## Slide 7 — Framework III: Intervention, Decision, and Test

### Visual purpose
Combine **engineering intervention, consequence evaluation, decision filtering, and hypothesis comparison** in one coherent final slide.

### Recommended composition

### Upper two-thirds — intervention to decision
- **Input:** resilience diagnosis from Framework II as a small viable/recovery surface.
- **Intervention:** cone / triangular wedge \(a_k\).
- **Modified system:** cuboid \(\mathfrak M^{a_k}\).
- **Consequences:** diamond \(\mathcal C(a_k)\) branching into small icons/axes for:
  resilience | resources | efficiency | sustainability | feasibility | uncertainty.
- **Decision:** Pareto scatter / frontier feeding a narrow decision pyramid ending at
  \(\mathcal A_{\rm joint}^{\star}\).

### Lower third — H1 comparison
Three parallel lanes:
- \(M_0\): independent systems
- \(M_1\): static coupling
- \(M_2\): evidence-qualified dynamic coupling

Route the three lanes into a common comparison gate labelled only by the existing slide text/formula. Use progressively richer geometry, not progressively brighter color, to avoid implying that \(M_2\) is automatically superior before testing.

### Final footer
Use the existing complete-story chain:
Reality → Evidence → Mechanisms → Behavior → Resilience → Intervention → Decision.

### Geometry
\[
\boxed{
a_k
\rightarrow
\mathcal C(a_k)
\rightarrow
\mathcal A_{\rm joint}^{\star}
}
\]

and

\[
\boxed{
M_0\quad\text{vs.}\quad M_1\quad\text{vs.}\quad M_2
}
\]

### Avoid
Do not visually crown \(M_2\) as the winner. H1–H5 are tests; the outcome is not predetermined.

---

## Publication and slide-production rules

1. **Do not rewrite, shorten, or add scientific claims to the canonical slide text.**
2. Use the visual specifications as a separate design layer.
3. Keep citations visible in the final deck.
4. Use **Times New Roman** for slide text; preserve the requested approximate hierarchy of 41–20 pt.
5. Equations should remain vector-rendered where possible.
6. Prefer editable vector geometry (SVG, TikZ, native PowerPoint shapes) over raster illustrations.
7. Keep each slide to one dominant visual system rather than several unrelated pictures.
8. Maintain white space; visuals should clarify the argument, not decorate it.
9. Use the official blue palette and **no gold**.
10. Any future visual change that alters scientific meaning must be checked against the Chapter I and canonical framework authorities.
