# Phase 0 — 0C Source-Level Existing-Representation Register

**Status:** CORE EVIDENCE PASS — source-level extraction complete for the initial benchmark set; systematic saturation not yet claimed.  
**Repository:** `Dossiya-SE/MSE-thesis`  
**Gate:** Theoretical Decision Gate v1.0  
**Phase:** 0C — Existing-Representation Theory Benchmark  
**Date:** 2026-09-12  

> **Control rule:** This register describes what selected predecessor frameworks explicitly support. It does **not** score the thesis ontologies `M0` or `M1`, and it does not establish novelty.

---

## 1. Extraction schema

For each representation family or source `M_j`, extract:

```math
\boxed{
M_j=
\{
O,R,D,A,I,O^{org},T,U,Q,F,V,L
\}
}
```

where:

| Field | Meaning |
|---|---|
| `O` | principal object/representation |
| `R` | relation semantics |
| `D` | directionality / reciprocity treatment |
| `A` | main assumptions / abstraction level |
| `I` | information/control treatment |
| `O^{org}` | organizational/human treatment |
| `T` | dynamic/time/delay treatment |
| `U` | uncertainty/evidence treatment |
| `Q` | service/capability/consequence treatment |
| `F` | preservation of domain-specific physics |
| `V` | validation/demonstration basis |
| `L` | principal limitation for our Phase-0 question |

Evidence states:

```math
[E]=\text{explicitly supported by source},\qquad
[D]=\text{conservative deduction from explicit source content},
```

```math
[U]=\text{not established from the evidence inspected in this pass}.
```

---

# 2. Core predecessor register

## M01 — Maier: System-of-Systems architecting

**Source:** Maier, M. W. (1998). *Architecting principles for systems-of-systems*. Systems Engineering, 1(4), 267–284. DOI: `10.1002/(SICI)1520-6858(1998)1:4<267::AID-SYS3>3.0.CO;2-D`.

### Extraction

- **O [E]:** constituent systems coordinated as a system-of-systems.
- **R [E]:** architecture strongly associated with communications/standards enabling meaningful interaction among constituents.
- **D [U]:** no explicit typed dependency grammar established from the material inspected here.
- **A [E]:** constituent systems retain meaningful independence; SoS classification matters for architecture.
- **I [E]:** communication standards are central to enabling SoS architecture.
- **O^org [E]:** managerial independence is a defining SoS characteristic.
- **T [U]:** time-varying dependency semantics are not the principal representation in the inspected source material.
- **U [U]:** no explicit epistemic dependency-state representation identified in this pass.
- **Q [E/D]:** SoS constituents collaborate to achieve larger system purposes/capabilities; explicit infrastructure service mathematics is not supplied.
- **F [D]:** constituent identity is preserved; source does not impose one common constituent physics.
- **V [E]:** architecting principles illustrated through existing/proposed systems.
- **L [D]:** strong for SoS identity/architecture, but not a complete dynamic typed infrastructure dependency object.

### Phase-0 significance

Maier is a **hard predecessor for `R1` and `R12`**. Any thesis representation that destroys constituent identity is theoretically weak.

---

## M02 — Rinaldi, Peerenboom & Kelly: Critical-infrastructure interdependency framework

**Source:** Rinaldi, S. M., Peerenboom, J. P., & Kelly, T. K. (2001). *Identifying, understanding, and analyzing critical infrastructure interdependencies*. IEEE Control Systems Magazine, 21(6), 11–25. DOI: `10.1109/37.969131`.

### Extraction

- **O [E]:** critical infrastructures considered as interconnected/mutually dependent complex adaptive systems.
- **R [E]:** infrastructure dependencies/interdependencies; physical and information/communications relations are explicit; additional dimensions characterize interdependencies.
- **D [E]:** direct and indirect cross-infrastructure effects are recognized; dependency and interdependency are explicitly defined.
- **A [E]:** infrastructures operate under interrelated system conditions; interdependency analysis is contextual rather than a pure topology problem.
- **I [E]:** cyber/information/communications dependence is first-class.
- **O^org [D/U]:** organizational dimensions are not sufficiently explicit in the inspected abstract/sections to treat as a complete organizational layer.
- **T [E/D]:** system conditions and interrelated factors imply context dependence; the current pass does not establish a full temporal state equation.
- **U [E/D]:** modeling/simulation challenges and complexity are explicit; no dependency-level evidence-state object is established.
- **Q [E]:** disturbances in one infrastructure can affect other infrastructures and broader regions/economy.
- **F [D]:** conceptual framework is not a common-physics reduction.
- **V [E]:** framework grounded in observed disruptions and modeling challenges; not a single quantitative validation model.
- **L [D]:** excellent conceptual semantics; not by itself a minimal dynamic executable dependency contract.

### Phase-0 significance

We cannot claim novelty for defining infrastructure dependency/interdependency or for recognizing physical/cyber interdependence.

---

## M03 — Johansson & Hassel: Structural + functional interdependency representation

**Source:** Johansson, J., & Hassel, H. (2010). *An approach for modelling interdependent infrastructures in the context of vulnerability analysis*. Reliability Engineering & System Safety, 95(12), 1335–1344. DOI: `10.1016/j.ress.2010.06.010`.

### Extraction

- **O [E]:** network model combining structural and functional properties.
- **R [E]:** functional and geographic interdependencies.
- **D [E]:** failures can traverse to dependent infrastructures and return to the infrastructure of origin.
- **A [E]:** vulnerability-analysis context; graph structure alone is insufficient for desired fidelity.
- **I [D/U]:** information-specific semantics are not a principal explicit layer in the inspected source material.
- **O^org [U]:** no explicit organizational/authority representation established in this pass.
- **T [D]:** propagation is represented conceptually; a general time-varying dependency-state grammar is not established from the inspected material.
- **U [U]:** no explicit dependency evidence/confidence state established.
- **Q [E]:** functional properties are included to improve fidelity/usefulness for vulnerability analysis.
- **F [D]:** functional properties complement topology; full heterogeneous sector physics are not the central formalism.
- **V [E]:** demonstrated with a fictional electrified railway system containing five systems and their interdependencies.
- **L [D]:** strong predecessor for `R2`, `R3`, `R8`, but not complete for information, organization, evidence state and reusable cross-domain dynamics.

---

## M04 — Kivelä et al.: General multilayer-network framework

**Source:** Kivelä, M., Arenas, A., Barthelemy, M., Gleeson, J. P., Moreno, Y., & Porter, M. A. (2014). *Multilayer Networks*. Journal of Complex Networks, 2(3), 203–271. DOI: `10.1093/comnet/cnu016`.

### Extraction

- **O [E]:** multilayer network with multiple subsystems/layers/types of connectivity.
- **R [E]:** multiple relationship types; interlayer and intralayer connectivity; dictionary connecting multilayer, multiplex, interdependent and network-of-networks concepts.
- **D [E/D]:** general network formalism can accommodate directed relations, but direction-specific infrastructure semantics are not supplied automatically.
- **A [E]:** complex systems can contain several subsystems, relation types, and time-changing connectivity.
- **I [D]:** information can be encoded as a layer/relation type, but no infrastructure-information semantics are intrinsic to the framework.
- **O^org [D]:** organizational relations can be encoded structurally, but organizational authority semantics are not intrinsic.
- **T [E]:** changing-in-time connectivity and dynamical processes on multilayer networks are explicit concerns.
- **U [U]:** dependency evidence/confidence is not an intrinsic core object in the general framework.
- **Q [D/U]:** dynamical processes can be studied; infrastructure service semantics are not intrinsic.
- **F [D]:** multilayer network theory is representation-general and does not encode sector governing physics by itself.
- **V [E]:** broad review/unification of multilayer concepts, datasets, diagnostics and dynamic processes.
- **L [D]:** powerful structural language, but semantics, physical mechanism, organization, evidence and service meaning must be supplied externally.

### Phase-0 significance

Putting Power and Transportation into layers is not a defensible novelty claim.

---

## M05 — Nan & Sansavini: Multilayer hybrid infrastructure model

**Sources:**
1. Nan, C., & Sansavini, G. (2015). *Multilayer hybrid modeling framework for the performance assessment of interdependent critical infrastructures*. International Journal of Critical Infrastructure Protection, 10, 18–33. DOI: `10.1016/j.ijcip.2015.06.002`.
2. Nan, C., & Sansavini, G. (2017). *A quantitative method for assessing resilience of interdependent infrastructures*. Reliability Engineering & System Safety, 157, 35–53. DOI: `10.1016/j.ress.2016.08.013`.

### Extraction

- **O [E]:** infrastructure decomposed into interacting subsystem layers.
- **R [E]:** interdependencies between system under control (SUC), operational control system (OCS), and human-organizational social system.
- **D [E]:** dependencies can operate in both directions; SUC can depend on OCS and OCS on SUC.
- **A [E]:** heterogeneous subsystem behaviors require appropriate model forms per layer; hybrid modeling integrates them.
- **I [E]:** OCS/SCADA and communications are explicit.
- **O^org [E]:** human-organizational social system is explicit.
- **T [E]:** hybrid modeling analyzes dynamics during/after disruptive events; 2017 formulation uses time-dependent resilience measures.
- **U [D/U]:** scenario/model uncertainty can be studied, but an evidence-confidence state on every dependency is not explicit in the inspected core description.
- **Q [E]:** infrastructure performance/resilience and failure propagation are explicit outputs.
- **F [E]:** different subsystem-specific models can be developed and integrated; heterogeneous behaviors are preserved.
- **V [E]:** Swiss high-voltage power-supply/SCADA/human-operator case studies and simulation experiments.
- **L [D]:** this is a very strong predecessor. The residual question is whether its layered hybrid architecture supplies a reusable *minimal dependency contract* with explicit evidence status and cross-domain composability, not whether physical/control/human layers exist.

### Phase-0 significance

This source substantially weakens any novelty claim based only on `Physical + Information + Organization` or hybrid multilayer integration.

---

## M06 — Ontology-based critical-infrastructure representations

**Core sources:**
- McNally, R. K., Lee, S.-W., Yavagal, D., & Xiang, W.-N. (2007). *Learning the Critical Infrastructure Interdependencies through an Ontology-Based Information System*. Environment and Planning B, 34(6), 1103–1124. DOI: `10.1068/b32078`.
- Castorini, E., Palazzari, P., Tofani, A., & Servillo, P. (2010). *Ontological Framework to Model Critical Infrastructures and their Interdependencies*. Complexity in Engineering, 2010. DOI: `10.1109/COMPENG.2010.25`.

### Extraction

- **O [E]:** ontology/knowledge-base objects representing infrastructure domains, assets and interdependencies.
- **R [E]:** intradomain and cross-domain interdependencies; formalized domain/dependency knowledge.
- **D [E/D]:** relations can be explicitly represented; detailed causal direction semantics depend on ontology/rules used.
- **A [E]:** reusable domain knowledge and communication across heterogeneous infrastructure expertise are central purposes.
- **I [E/D]:** ontology is an information/knowledge representation layer; infrastructure-control information dynamics are not automatically modeled.
- **O^org [D]:** stakeholders/domain experts and cross-domain knowledge are supported; dynamic authority/resource behavior is not necessarily intrinsic.
- **T [U]:** time-varying relationship dynamics are not central in the inspected descriptions.
- **U [D/U]:** knowledge representation can support explicit missing/qualitative information, but a universal evidence-confidence state is not established here.
- **Q [E/D]:** vulnerability assessment, scenario composition, drills and simulation support are explicit uses.
- **F [E/D]:** Castorini et al. deliberately abstract scenario description from simulation technology, allowing domain-specific simulators underneath.
- **V [E]:** southeastern U.S. case study (McNally et al.); Rome-area realistic scenario/federated simulation (Castorini et al.).
- **L [D]:** strong semantic/interoperability predecessor, weaker as a standalone dynamic physics-and-delay representation.

---

## M07 — NIST Cyber-Physical Systems Framework

**Sources:** NIST SP 1500-201 (2017), *Framework for Cyber-Physical Systems: Volume 1, Overview*; NIST human-aspect elaboration (2018).

### Extraction

- **O [E]:** CPS consisting of interacting digital, analog, physical and human components.
- **R [E]:** interaction/integration through physics and logic; framework organized using facets and aspects/concerns.
- **D [D]:** interaction direction can be represented in architecture/models, but no universal infrastructure dependency-edge object is prescribed.
- **A [E]:** cross-domain reuse is explicit; application domains include energy and transportation.
- **I [E]:** data, timing, logic/digital components are explicit.
- **O^org [E]:** human aspect and business concerns are explicit.
- **T [E]:** timing is a named aspect; a dedicated Timing Annex exists.
- **U [E/D]:** trustworthiness, assurance and lifecycle concerns are explicit; dependency-level epistemic evidence state is not directly prescribed.
- **Q [E]:** CPS are engineered for function through integrated physics and logic.
- **F [E]:** integrated physics and logic are explicit; framework is not restricted to one domain's governing laws.
- **V [E]:** developed through NIST public working groups for cross-domain engineering analysis/design/operation/validation/assurance.
- **L [D]:** highly relevant cross-domain architecture precedent, but not a specific infrastructure dependency grammar.

### Phase-0 significance

Our domain × aspect proposal must be benchmarked carefully against NIST; cross-domain `domain + aspects` thinking is not new.

---

## M08 — ISO/IEC/IEEE 42010:2022 architecture description

**Source:** ISO/IEC/IEEE 42010:2022, *Software, systems and enterprise — Architecture description*.

### Extraction

- **O [E]:** architecture descriptions for entities including systems, systems of systems, enterprises, families/products/services and business domains.
- **R [E]:** architecture concepts expressed through viewpoints/model kinds and their relationships.
- **D [D/U]:** directionality can be encoded by a conforming model, but the standard does not itself define infrastructure dependency semantics.
- **A [E]:** multiple stakeholder concerns require explicit viewpoints; architecture is distinguished from its description.
- **I [D]:** information/cyber concerns can be represented through views but are not prescribed as an infrastructure layer.
- **O^org [D]:** organizational/business concerns can be represented through views but are not prescribed as a dependency dynamic.
- **T [D/U]:** dynamic/time behavior can be modeled through an appropriate viewpoint/model kind; not prescribed by the standard itself.
- **U [D]:** concerns/assumptions can be documented architecturally, but no dependency evidence-state object is prescribed.
- **Q [E/D]:** services and business domains are in scope; the standard structures descriptions rather than defining service-performance equations.
- **F [E/D]:** multiple model kinds can coexist; standard does not force one physics.
- **V [E]:** international architecture-description standard, not an empirical infrastructure model.
- **L [E/D]:** deliberately does not specify architecture methods/models/notations/tools; therefore it is a meta-architecture constraint, not our executable relation grammar.

---

## M09 — Temporal-network infrastructure interdependency model

**Source:** *Modelling infrastructure interdependencies and cascading effects using temporal networks*. Resilient Cities and Structures, 3(3), 2024. DOI: `10.1016/j.rcns.2024.05.002`.

### Extraction

- **O [E]:** temporal graph/network model for lifeline interdependencies and cascading effects.
- **R [E]:** graph dependencies combined with modified inoperability modeling and perturbation rules.
- **D [E/D]:** propagation across dependencies is explicit; exact semantic relation classes depend on model definition.
- **A [E]:** static approaches inadequately capture emergency event sequences.
- **I [U]:** no explicit general information/control layer established from inspected material.
- **O^org [U]:** no explicit organizational/authority layer established from inspected material.
- **T [E]:** event sequence/time effects are the central contribution.
- **U [E]:** model returns failure probabilities; uncertainty is represented probabilistically at outcome level.
- **Q [D]:** cascading failure consequences are modeled; infrastructure service semantics may require external specification.
- **F [D/U]:** graph/inoperability abstraction does not preserve full domain-specific governing physics by itself.
- **V [E]:** methodology demonstrated for disaster/emergency cascading effects.
- **L [D]:** excellent temporal predecessor, but semantics/organization/sector physics remain separate concerns.

---

## M10 — Dynamic coupled Power–Transportation equilibrium

**Source:** Song, Y., Ngoduy, D., Dantsuji, T., & Ding, C. (2025). *Dynamic equilibrium of the coupled transportation and power networks considering electric vehicles charging behavior*. Transportation Research Part A, 199, 104590. DOI: `10.1016/j.tra.2025.104590`.

### Extraction

- **O [E]:** coupled TN–PDN dynamic equilibrium model.
- **R [E]:** EV/FCS interaction links transportation choices/traffic propagation to PDN operation and electricity prices.
- **D [E]:** reciprocal influence is explicit: transportation/charging decisions affect electrical operation; electrical prices/limits influence transportation/charging behavior.
- **A [E]:** EV/GV travel behavior, FCS queueing, mixed traffic propagation and PDN limits are explicitly modeled.
- **I [E/D]:** electricity prices and decision information couple behavior/operation; a general information-infrastructure layer is not the focus.
- **O^org [U]:** institutional authority/coordination is not a principal explicit layer in the inspected model.
- **T [E]:** stochastic dynamic user equilibrium, traffic propagation and queue evolution are explicit.
- **U [E]:** stochastic behavior is explicitly modeled; dependency evidence status is not.
- **Q [E]:** traffic delay, FCS waiting time, power losses and network performance are evaluated.
- **F [E]:** traffic-flow dynamics and AC optimal power flow are modeled distinctly and coupled through interaction variables.
- **V [E]:** numerical case studies compare coupled vs independent operation and evaluate physical/operational outcomes.
- **L [D]:** high-fidelity P–T dynamics but domain-specific; information/organization/evidence semantics and general `P+T+W+...` reuse are not its main purpose.

### Phase-0 significance

This is a strong baseline against any claim that dynamic P–T coupling or preservation of separate P/T physics is itself new.

---

## M11 — Recent interdependent-infrastructure review evidence

**Sources:**
- Tong et al. (2025), *Resilience of interdependent infrastructure networks: Review and future directions*, International Journal of Critical Infrastructure Protection, 51, 100793.
- Ghasemkhani, Basiri, & Nicholson (2026), *Interdependency and uncertainty in the resiliency of infrastructure networks: A comprehensive review*, International Journal of Critical Infrastructure Protection, 100866.

### Extraction

These are **review/gap sources**, not representation candidates to score as standalone models.

[E] Current literature continues to identify:

- temporal/geographic performance evolution,
- dynamic equilibrium,
- interdependency,
- uncertainty,
- interpretable/data-driven resilience modeling,
- holistic trade-offs

as active research needs.

### Phase-0 significance

These reviews support continuing the gate, but **do not prove** that our candidate dependency contract is novel or necessary.

---

# 3. Core evidence synthesis

The benchmark establishes the following with high confidence:

```math
\boxed{
\begin{aligned}
\text{SoS identity} &\rightarrow \text{Maier},\\
\text{dependency semantics} &\rightarrow \text{Rinaldi; Johansson--Hassel},\\
\text{multilayer structure} &\rightarrow \text{Kivela et al.},\\
\text{physical/control/human layers} &\rightarrow \text{Nan--Sansavini},\\
\text{knowledge interoperability} &\rightarrow \text{ontology approaches},\\
\text{cross-domain CPS aspects} &\rightarrow \text{NIST},\\
\text{multi-view architecture} &\rightarrow \text{ISO 42010},\\
\text{time-respecting propagation} &\rightarrow \text{temporal-network models},\\
\text{dynamic P--T physics} &\rightarrow \text{Song et al. and related CPTS models}.
\end{aligned}}
```

Therefore the following novelty claims are **rejected before testing**:

1. `Power and Transportation are interdependent`.
2. `Use multilayer networks for P–T`.
3. `Include physical, information/control, and organization/human dimensions`.
4. `Represent time-varying infrastructure interactions`.
5. `Couple distinct P/T physics through EV/FCS interactions`.
6. `Use ontology/architecture concepts to improve cross-domain interoperability`.

---

# 4. Candidate residual question after the core pass

The evidence currently leaves a narrower unresolved question:

```math
\boxed{
\begin{minipage}{0.86\textwidth}
Can a minimum typed dependency contract provide an interoperable semantic bridge across structural network, sector-physics, informational/control, organizational, temporal, uncertainty/evidence, and service models without replacing the specialized models that already solve those individual concerns?
\end{minipage}
}
```

This is **[H/P]**, not an established gap.

---

# 5. 0C completion condition

This source register is the **core pass**, not evidence of saturation.

Before 0C can be marked `COMPLETE`, perform:

1. backward/forward citation chasing from `M02`, `M03`, `M05`, `M06`, `M07`, `M09`, `M10`;
2. targeted search for any framework explicitly combining all or most of `R1–R12`;
3. targeted search for `reference architecture`, `interoperability`, `dependency grammar`, `typed dependency`, `knowledge graph`, `shared-state SoS`, and `federated infrastructure simulation`;
4. saturation check: no newly identified representation family changes the benchmark taxonomy or closes the candidate residual question;
5. source-level documentation of any contrary framework that appears to dominate the candidate Phase-0 contract.

Until these are complete:

```math
\boxed{\text{0C status = CORE PASS COMPLETE; SATURATION NOT ESTABLISHED}.}
```
