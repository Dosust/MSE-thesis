# Phase 0 — 0C Saturation / Contrary-Framework Search — Round 1

**Status:** ROUND 1 COMPLETE — saturation **not reached** because the representation taxonomy changed.  
**Gate:** Theoretical Decision Gate v1.0  
**Date:** 2026-09-12  
**Purpose:** actively search for predecessor frameworks that could subsume, dominate, or make unnecessary the proposed Phase-0 dependency grammar.

> **Adversarial rule:** A newly found predecessor that closes the candidate residual problem is a successful research result. The objective is not to protect the proposed grammar.

---

# 1. Targeted search families

Round 1 targeted the following missing predecessor classes:

```text
S1: shared-state system-of-systems infrastructure models
S2: reference architecture / interoperability models
S3: typed dependency / dependency-logic formalisms
S4: temporal or uncertainty-aware knowledge/semantic models
S5: federated co-simulation / heterogeneous infrastructure integration
S6: physical + cyber/information + organization + service + uncertainty frameworks
```

Search logic intentionally differed from the initial broad interdependency searches.

---

# 2. Newly identified predecessor families

## N01 — Shared-State Complex System-of-Systems model

**Anchor:** Haberlin, R. J., Jr., & Haimes, Y. Y. (2018). *Regional Infrastructures as Complex Systems of Systems: Shared-State Model for Regional Resilience*. Journal of Infrastructure Systems, 24(3), 04018010. DOI: `10.1061/(ASCE)IS.1943-555X.0000421`.

### Explicit source content [E]

The methodology traces critical interconnected/interdependent infrastructure relationships using:

```math
\boxed{
\text{shared/common states}
+
\text{decisions}
+
\text{decision makers}
+
\text{stakeholders}
+
\text{resources}
+
\text{time frame}
+
\text{organizational setups}
}
```

and defines mutual influence through subsystems sharing states and essential entities.

### Threat to Phase 0

This is a **direct challenge** to the candidate dependency tuple because it already moves well beyond physical graph edges and explicitly includes organizational/decision/resource/time objects.

The previous residual statement

```math
\text{“organization + time + resources + state must be added to infrastructure dependencies”}
```

is therefore rejected as a novelty candidate.

### Remaining comparison question [H]

Does the shared-state model explicitly provide, at relation level:

- typed source/receiver semantics;
- physical versus informational versus authority mechanism types;
- structural existence versus functional state versus influence strength;
- explicit causal delay;
- epistemic evidence status distinct from model uncertainty;
- cross-domain mapping into specialized sector governing equations?

These must be checked before any claimed residual difference.

---

## N02 — Critical-infrastructure SoS + federated/HLA simulation

**Anchor:** Eusgeld, I., Nan, C., & Dietz, S. (2011). *“System-of-systems” approach for interdependent critical infrastructures*. Reliability Engineering & System Safety, 96(6), 679–686. DOI: `10.1016/j.ress.2010.12.010`.

### Explicit source content [E]

The paper:

- analyzes infrastructure at single-system and SoS levels;
- distinguishes integrated versus coupled model architectures;
- treats SCADA and systems under control as interdependent;
- discusses aggregating outputs of lower-level models into higher-level models;
- introduces High Level Architecture (HLA) as a promising standard for representing infrastructure interdependencies.

### Threat to Phase 0

The thesis cannot claim novelty for:

```math
\text{heterogeneous models}
\rightarrow
\text{federated/coupled SoS representation}
```

or for preserving separate low-level subsystem models while coupling them at higher level.

The residual issue shifts from **model federation exists?** to **what common semantic contract is needed for meaningful federation?**

---

## N03 — Heterogeneous SoS interoperability reference architecture

**Anchor:** Sadeghi et al. (2024). *Interoperability of heterogeneous Systems of Systems: from requirements to a reference architecture*. Journal of Supercomputing, 80, 8954–8987.

### Explicit source content [E]

The study:

1. elicits interoperability requirements from practitioners/stakeholders;
2. critically reviews conceptual approaches/technologies against those requirements;
3. derives components for an interoperability-fostering reference architecture.

### Threat to Phase 0

This is methodologically close to our own gate logic:

```math
\text{requirements}
\rightarrow
\text{benchmark existing approaches}
\rightarrow
\text{reference architecture}.
```

Therefore the methodology itself is not novel. Phase 0 must differentiate its **infrastructure-interdependency object and tests**, not the generic act of building an interoperability architecture.

---

## N04 — Cross-domain uncertainty-aware semantic reasoning for CI

**Anchor:** *Uncertainty-aware knowledge representation and reasoning in critical infrastructure systems* (2026), Journal of Infrastructure Intelligence and Resilience, 5(3), 100213. DOI: `10.1016/j.iintel.2026.100213`.

### Explicit source content [E]

The framework:

- integrates socio-technical CPS and human-activity data across domains;
- integrates semantic-web techniques with abductive reasoning under uncertainty;
- supports dynamic resilience assessment across domains/sectors;
- is demonstrated with real traffic data plus a simulated cyber-attack affecting emergency services, mobility and public behavior.

### Threat to Phase 0

This substantially weakens the idea that the thesis would be the first to combine:

```math
\text{cross-domain semantics}
+
\text{human dimension}
+
\text{uncertainty}
+
\text{dynamic resilience reasoning}.
```

The residual question must distinguish **uncertainty in reasoning/state** from **epistemic evidence status of a specific dependency assertion** if that distinction remains unsupported.

---

## N05 — Multi-domain physical/functional ontology + service delivery

**Anchor:** Trucco, P., Petrenj, B., Bouchon, S., & Di Mauro, C. (2016). *Ontology-based approach to disruption scenario generation for critical infrastructure systems*. International Journal of Critical Infrastructures, 12(3), 248–272. DOI: `10.1504/IJCIS.2016.079022`.

### Explicit source content [E]

The framework covers:

```math
\{\text{energy},\text{transport},\text{water},\text{telecommunications}\}
```

with each sector described through:

```math
\text{physical ontology}
+
\text{functional ontology}
```

connected through a **service-delivery process model**; hazard/threat ontologies connect to CI systems through vulnerability and dependency/interdependency models.

### Threat to Phase 0

This is a direct predecessor for:

- multi-domain extensibility;
- separating physical and functional semantics;
- cross-infrastructure dependency models;
- service-delivery consequence.

The thesis must not claim that `domain × aspect` plus services is unprecedented.

---

## N06 — Logical/typed dependency formalisms

**Anchors:** Banerjee, Das & Sen (survey, 2017); Banerjee, Basu & Sen (2017) Implicative Interdependency Model.

### Explicit source content [E]

The interdependency-model literature includes explicit logical relationships, including combinations of conjunctive and disjunctive dependencies and Boolean-logic implication formulations for critical-infrastructure entities.

### Threat to Phase 0

The thesis cannot assume that existing interdependency models are only binary edges.

Any proposed grammar must be benchmarked against **logical dependency expressiveness**, not only graph adjacency.

---

## N07 — Knowledge graphs for CI management, temporal gaps and relation prediction

**Anchor:** Chen et al. (2023). *A management knowledge graph approach for critical infrastructure protection: Ontology design, information extraction and relation prediction*. International Journal of Critical Infrastructure Protection, 43, 100634. DOI: `10.1016/j.ijcip.2023.100634`.

### Explicit source content [E]

The framework:

- extends a management ontology;
- addresses cross-industry and cross-time information gaps;
- represents CI protection management knowledge;
- includes relation prediction.

Recent 2026 CI knowledge-graph research further explores dynamic/probabilistic cascade reasoning.

### Threat to Phase 0

A future hidden-dependency/discovery component must not be presented as novel merely because it uses semantic relations or relation prediction.

---

## N08 — Uncertainty taxonomies for interdependent infrastructure

**Anchor:** *Sources of uncertainty in interdependent infrastructure and their implications* (2021/2022 literature).

### Explicit source content [E]

Interdependent-infrastructure literature already distinguishes multiple sources/types of uncertainty and explicitly links knowledge of dependency sources/strengths to intervention against cascading failure.

### Threat to Phase 0

`U_e` cannot remain an undefined “uncertainty” field. Phase 0 must separate at least:

```math
\boxed{
U_e^{phys/model}
\neq
U_e^{epistemic/evidence}
}
```

and prove that the latter provides information not already captured by established uncertainty frameworks.

---

# 3. Saturation result

Round 1 **changed the representation taxonomy**.

New first-class predecessor classes were identified:

```math
\boxed{
\begin{aligned}
&\text{shared-state / shared-essential-entity SoS},\\
&\text{federated/HLA infrastructure SoS},\\
&\text{heterogeneous SoS interoperability reference architecture},\\
&\text{uncertainty-aware semantic CI reasoning},\\
&\text{physical-functional multi-domain service ontology},\\
&\text{logical dependency grammar},\\
&\text{CI knowledge-graph relation prediction}.
\end{aligned}}
```

Therefore, by the preregistered saturation rule:

```math
\boxed{\text{SATURATION NOT REACHED}.}
```

0D remains blocked.

---

# 4. Revised strongest-predecessor set

The strongest challenge set is now:

```math
\boxed{
\begin{aligned}
P_1&=\text{Nan--Sansavini multilayer hybrid model},\\
P_2&=\text{Haberlin--Haimes shared-state SoS model},\\
P_3&=\text{Trucco et al. physical/functional service ontology},\\
P_4&=\text{NIST CPS cross-domain aspects},\\
P_5&=\text{uncertainty-aware CI semantic reasoning},\\
P_6&=\text{Eusgeld--Nan--Dietz HLA/federated SoS},\\
P_7&=\text{dynamic high-fidelity P--T model},\\
P_8&=\text{logical dependency models}.
\end{aligned}}
```

Any candidate Phase-0 object must be tested against this *combined predecessor envelope*.

---

# 5. Candidate residual problem after Round 1

The residual problem becomes narrower again:

```math
\boxed{
\begin{minipage}{0.88\textwidth}
Is there a minimum relation-level contract that can map among shared-state SoS representations, multilayer hybrid physical/control/human models, physical-functional service ontologies, logical dependency models, federated simulation, uncertainty-aware semantic reasoning, and high-fidelity sector models while preserving relation mechanism, state/time semantics, evidence provenance, and measurable service consequence?
\end{minipage}
}
```

Status:

```math
[H/P]\quad\text{still unresolved; substantially narrower than the original Phase-0 idea.}
```

---

# 6. Critical conceptual change

The thesis should no longer ask primarily:

```text
“What fields should we add to represent interdependency?”
```

because many predecessor frameworks already provide rich field sets.

The harder theoretical question is now:

```math
\boxed{
\text{What is the minimum common invariant that permits loss-controlled translation among heterogeneous interdependency representations?}
}
```

This shifts Phase 0 from **feature accumulation** toward **interoperability + minimal sufficient semantics**.

---

# 7. Required Round 2 saturation search

Round 2 must trace the strongest new predecessors and answer whether such a common invariant already exists.

Search priorities:

1. papers citing Haberlin–Haimes shared-state infrastructure SoS;
2. infrastructure/SoS semantic interoperability and model transformation;
3. HLA/FMI/HELICS/federated model interface semantics for infrastructure co-simulation;
4. semantic-web/provenance standards capable of relation-level evidence annotation;
5. typed property-graph / ontology patterns for stateful and temporal relations;
6. recent 2025–2026 critical-infrastructure reference architectures and knowledge graphs;
7. explicit mappings between architecture/ontology objects and governing physical simulation models.

### Round-2 stopping rule

Round 2 reaches saturation only if:

```math
\boxed{
\text{new eligible sources do not introduce a new first-class representation family}
}
```

and either:

```math
\text{(a) no existing common relation invariant is identified},
```

or

```math
\text{(b) an existing invariant is identified and Phase 0 is reframed around adoption/extension rather than invention}.
```

---

# 8. Current gate state

```math
\boxed{
0A=\text{Frozen},\quad
0B=\text{Frozen},\quad
0C=\text{Active — saturation round 2 required},\quad
0D\text{--}0G=\text{Blocked}.
}
```
