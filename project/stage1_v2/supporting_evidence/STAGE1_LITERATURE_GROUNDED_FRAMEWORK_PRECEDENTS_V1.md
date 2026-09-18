> **STATUS: SUPERSEDED — RETAINED FOR PROVENANCE.**
> Active supporting-evidence authority is `STAGE1_LITERATURE_GROUNDED_FRAMEWORK_PRECEDENTS_V2.md`.
> Do not use this v1 file for new evidence-traceability decisions.

# Stage 1 Literature-Grounded Framework Precedents v1.0

**Status:** SUPPORTING EVIDENCE — DOES NOT AMEND THE FROZEN STAGE-1 FRAMEWORK  
**Date:** 2026-09-18  
**Scope:** Literature precedents for the organization and visual design of Stage 1 — *Spatiotemporal Multilayer System-of-Systems Structure*  
**Frozen authority:** `project/STAGE1_FINAL_FRAMEWORK_V2.md`, `project/STAGE1_MATHEMATICAL_AND_ONTOLOGY_CONTRACT_V2.md`, `project/STAGE1_DATA_ABSTRACTION_AND_INGESTION_STANDARD_V2.md`, and `thesis/00_governance/STAGE1_FRAMEWORK_FREEZE_2026-09-18.md`  
**Companion bibliography:** `STAGE1_LITERATURE_GROUNDED_FRAMEWORK_PRECEDENTS_V1.bib`

---

## 1. Purpose

This document records the literature basis for organizing the frozen Stage-1 framework into a thesis figure that is easier to understand without weakening its scientific controls.

The central Stage-1 question remains:

```math
\boxed{
\text{What exists, how is it organized, and where could }P\text{ and }T\text{ interact?}
}
```

The literature supports a sequence in which the analyst first defines the infrastructure context, then represents the systems and their internal structure, then identifies possible cross-system interfaces, and only afterward proceeds to causal qualification, dynamic coupling, and resilience analysis. This sequence is consistent with the conceptual interdependency framework of [Rinaldi, Peerenboom, and Kelly (2001)](https://doi.org/10.1109/37.969131), ontology-based intra/cross-domain representation by [McNally et al. (2007)](https://doi.org/10.1068/b32078), the interdependent-infrastructure modeling review of [Ouyang (2014)](https://doi.org/10.1016/j.ress.2013.06.040), the structure-to-dynamics separation of [Filippini and Silva (2014)](https://doi.org/10.1016/j.ress.2013.09.010), multilayer infrastructure representation by [Nan and Sansavini (2015)](https://doi.org/10.1016/j.ijcip.2015.04.003), and interface-based heterogeneous model integration by [Zhou et al. (2020)](https://doi.org/10.1016/j.ijcip.2020.100391).

The strongest conclusion from this precedent scan is:

```math
\boxed{
\text{system context}
\rightarrow
\text{semantic structure}
\rightarrow
\text{candidate interfaces}
\rightarrow
\text{evidence-grounded relation records}
\rightarrow
\text{causal qualification}
\rightarrow
\text{dynamics}
\rightarrow
\text{resilience}
}
```

The first four elements are the concern of the frozen Stage-1 framework. Causal qualification belongs to Stage 2, and coupled dynamics belong to Stage 3.

---

## 2. Search and evidence protocol

This was a targeted scientific precedent scan rather than a systematic review. The objective was not to rank papers, but to identify peer-reviewed studies that provide direct methodological precedent for at least one frozen Stage-1 function.

The scan prioritized papers that satisfy one or more of the following conditions:

1. define infrastructure dependency/interdependency concepts or dimensions;
2. distinguish within-system from cross-system relations;
3. use ontology, GIS, multilayer, functional, or interface representations;
4. separate structural representation from dynamic propagation or resilience analysis;
5. provide direct Power–Transportation coupling examples;
6. make organizational/logical relations explicit;
7. distinguish relation existence from later coupling-strength quantification.

Publication metadata and major methodological claims were checked against publisher pages, DOI records, or scholarly indexing sources. No source in this supporting set is being used as case-specific proof of a causal Power–Transportation relation.

This distinction is mandatory:

```math
\boxed{
\text{literature precedent}
\neq
\text{case-specific structural verification}
\neq
\text{accepted causal interdependency}.
}
```

---

## 3. Literature extraction matrix

| ID | Reference | Main contribution | Stage-1 precedent | Frozen objects supported | Boundary / non-transfer rule |
|---|---|---|---|---|---|
| L01 | [Rinaldi, Peerenboom, & Kelly (2001)](https://doi.org/10.1109/37.969131) | Conceptual framework for critical-infrastructure dependencies/interdependencies; system conditions and relation types. | System context, direction, mechanism family, operating context. | $\sigma_e$, $d_e$, $m_e^{\rm cand}$, $c_e^{\rm cand}$, contextual reasoning. | Taxonomy does not prove a case-specific relation. |
| L02 | [McNally et al. (2007)](https://doi.org/10.1068/b32078) | Ontology + GIS representation of intradomain and cross-domain infrastructure interdependencies. | Semantic entities, INTRA/INTER distinction, spatial representation. | $E_i^\alpha$, $r_i$, $\mathcal R_{\rm intra}$, $\mathcal R_{\rm inter}$. | Ontological or spatial representation is not causal proof. |
| L03 | [Ouyang (2014)](https://doi.org/10.1016/j.ress.2013.06.040) | Review of empirical, agent-based, system-dynamics, economic, and network approaches to interdependent infrastructures. | Evidence-before-modeling logic; method choice; context-dependent relations. | $\mathcal E_e$, $b_e$, $c_e^{\rm cand}$. | Review coverage is not case evidence. |
| L04 | [Filippini & Silva (2014)](https://doi.org/10.1016/j.ress.2013.09.010) | Functional-relation representation followed by structural and then dynamic resilience analysis. | Strong precedent for structure first, dynamics later. | $\gamma_e$, $\Phi_e$, structural/causal boundary. | Dynamic propagation and resilience calculations remain outside Stage 1. |
| L05 | [Nan & Sansavini (2015)](https://doi.org/10.1016/j.ijcip.2015.04.003) | Multilayer hybrid representation of heterogeneous interdependent infrastructures. | Layered physical/operational/human-organizational decomposition. | $\mathcal S=\{P,T,I,O\}$ conceptually; $h_e$, $\ell_e$. | Their layer decomposition does not replace the frozen $P,T,I,O$ ontology. |
| L06 | [Zhou et al. (2020)](https://doi.org/10.1016/j.ijcip.2020.100391) | Infrastructure profiling, infrastructure-specific model choice, and designed interfaces linking heterogeneous models. | System → model/representation → interface workflow. | $\gamma_e$, $\Phi_e$, $\mathcal E_e$, interface semantics. | Their failure-propagation implementation belongs beyond Stage 1. |
| L07 | [Hruska, McGillivary, & Edsall (2021)](https://doi.org/10.18278/jcip.2.2.6) | Functional decomposition and directed multidimensional graphs for cross-sector dependency analysis. | Function/service-centered relation semantics and scalable decomposition. | $f_i$, $\Phi_e$, $\ell_e$, service traceability. | Functional decomposition alone does not establish case-specific causality. |
| L08 | [Fotouhi, Moryadee, & Miller-Hooks (2017)](https://doi.org/10.1016/j.ress.2017.01.026) | Two-layer urban traffic–power model with explicit linking variables and logical constraints. | Direct Power–Transportation architectural precedent. | candidate $P\to T$, candidate $T\to P$, $\gamma_e$, $\Phi_e$. | Their modeled interdependencies cannot be transferred automatically to a new case. |
| L09 | [Anokhin et al. (2021)](https://doi.org/10.1111/poms.13393) | Power restoration coordinated with transportation constraints, mobile power sources, and repair crews. | Direct recovery-activated $T\to P$ mechanism family. | $m_e^{\rm cand}$, $c_e^{\rm cand}=\mathrm{recovery}$, $\Phi_e$. | A nearby road does not by itself establish a restoration-access dependency. |
| L10 | [Yu et al. (2025)](https://doi.org/10.1111/risa.16555) | Rule-mediated logical interdependencies represented through syntactic and network forms. | Explicit organizational/logical relation representation. | $O$ domain, $m_e^{\rm cand,org}$, $\mathcal E_e^{\rm rules}$. | Organizational relations must remain distinct from physical $P\leftrightarrow T$ mechanisms. |
| L11 | [Lu et al. (2025)](https://doi.org/10.1016/j.energy.2025.135330) | Supply-demand-based dependency quantification with heterogeneous fast-charging stations. | Demonstrates that dependency magnitude depends on interface function and operating context. | later-stage $w_e$, heterogeneity attributes, $\Phi_e$. | Strength estimation presupposes a qualified coupling structure; Stage 1 therefore defers $w_e$. |

---

## 4. Detailed source extraction

### 4.1 Rinaldi, Peerenboom, and Kelly (2001) — conceptual interdependency foundation

**Reference:** Rinaldi, S. M., Peerenboom, J. P., & Kelly, T. K. (2001). *Identifying, understanding, and analyzing critical infrastructure interdependencies*. IEEE Control Systems Magazine, 21(6), 11–25. [https://doi.org/10.1109/37.969131](https://doi.org/10.1109/37.969131).

**Problem addressed.** The paper develops a conceptual framework for understanding critical-infrastructure dependency and interdependency in systems where effects can propagate directly and indirectly across infrastructures.

**Representation.** Infrastructure interdependencies are treated as relationships conditioned by infrastructure characteristics, operating states, spatial scales, temporal scales, and multiple interdependency types. The paper is foundational for distinguishing one-directional dependence from reciprocal interdependence and for recognizing physical, cyber, geographic, and logical forms.

**Evidence/method.** The contribution is primarily conceptual and taxonomic, informed by observed infrastructure disruptions and system behavior rather than by a single quantitative identification algorithm.

**Stage-1 transfer.** The paper supports:
- explicit system context before relation analysis;
- directionality of relations;
- mechanism-family classification;
- operating/activation context;
- separation of common geographic exposure from other forms of interaction.

In the frozen notation, the closest mapping is to $\sigma_e$, $d_e$, $m_e^{\rm cand}$, and $c_e^{\rm cand}$.

**Non-transfer boundary.** A relation category from Rinaldi et al. is not evidence that a specific pair of assets in a study case is structurally connected or causally interdependent. The thesis must still satisfy the frozen Stage-1 evidence/provenance rules and Stage-2 causal qualification.

---

### 4.2 McNally et al. (2007) — ontology + GIS precedent for INTRA/INTER structure

**Reference:** McNally, R. K., Lee, S.-W., Yavagal, D., & Xiang, W.-N. (2007). *Learning the Critical Infrastructure Interdependencies through an Ontology-Based Information System*. Environment and Planning B: Planning and Design, 34(6), 1103–1124. [https://doi.org/10.1068/b32078](https://doi.org/10.1068/b32078).

**Problem addressed.** The paper argues that infrastructure analysis needs knowledge of interactions within an infrastructure domain and interactions across infrastructure domains.

**Representation.** It combines ontology-based object modeling with GIS and explicitly distinguishes **intradomain** and **cross-domain** interdependencies. The relations can be represented diagrammatically and geographically.

**Evidence/method.** The methodology is demonstrated on a case study in the southeastern United States using ontology/GIS integration.

**Stage-1 transfer.** This is one of the strongest precedents for the frozen sequence:

```math
\boxed{
\text{semantic entity}
\rightarrow
\text{INTRA structure}
\rightarrow
\text{INTER candidate space}
\rightarrow
\text{spatial representation}
}
```

It supports $E_i^\alpha$, $r_i$, $\mathcal R_{\rm intra}$ and $\mathcal R_{\rm inter}$.

**Non-transfer boundary.** A geographic or ontological link must not be treated as a causal dependency. This aligns directly with the frozen rules:

```math
\boxed{
\text{proximity}\neq\text{dependency},
\qquad
\text{representation}\neq\text{causal proof}.
}
```

---

### 4.3 Ouyang (2014) — evidence and modeling-method organization

**Reference:** Ouyang, M. (2014). *Review on modeling and simulation of interdependent critical infrastructure systems*. Reliability Engineering & System Safety, 121, 43–60. [https://doi.org/10.1016/j.ress.2013.06.040](https://doi.org/10.1016/j.ress.2013.06.040).

**Problem addressed.** The review organizes the principal methods used to model and simulate interdependent critical infrastructure systems.

**Representation/method taxonomy.** It covers empirical, agent-based, system-dynamics, economic, and network-based approaches and compares how different methods represent interdependent systems.

**Stage-1 transfer.** The main lesson is methodological ordering: relation type, available evidence, and system context should be understood before choosing a downstream model. This supports the frozen evidence/provenance object $\mathcal E_e$, admission basis $b_e$, and activation context $c_e^{\rm cand}$.

**Non-transfer boundary.** A review can establish a transferable mechanism family or modeling precedent, but it cannot verify the existence of a relation in the thesis case. Therefore literature-only candidates remain literature-supported candidates until case evidence is available.

---

### 4.4 Filippini and Silva (2014) — structure before dynamics and resilience

**Reference:** Filippini, R., & Silva, A. (2014). *A modeling framework for the resilience analysis of networked systems-of-systems based on functional dependencies*. Reliability Engineering & System Safety, 125, 82–91. [https://doi.org/10.1016/j.ress.2013.09.010](https://doi.org/10.1016/j.ress.2013.09.010).

**Problem addressed.** The paper develops a systems-of-systems resilience methodology centered on functional relationships among components.

**Representation.** It first builds a conceptual representation of components and functional dependencies, analyzes structural properties, and then extends the model to dynamic failure propagation and resilience assessment.

**Stage-1 transfer.** This is a strong precedent for the thesis boundary:

```math
\boxed{
\text{structural/functional representation}
\rightarrow
\text{dynamic model}
\rightarrow
\text{resilience analysis}.
}
```

For the thesis, Stage 1 intentionally stops at the first term. It can record interface semantics $\gamma_e$ and exchanged/enabled quantity or service $\Phi_e$, but it cannot yet introduce propagation laws.

**Non-transfer boundary.** Failure propagation, times to failure, recovery times, and resilience response are not Stage-1 outputs.

---

### 4.5 Nan and Sansavini (2015) — multilayer heterogeneous infrastructure architecture

**Reference:** Nan, C., & Sansavini, G. (2015). *Multilayer hybrid modeling framework for the performance assessment of interdependent critical infrastructures*. International Journal of Critical Infrastructure Protection, 10, 18–33. [https://doi.org/10.1016/j.ijcip.2015.04.003](https://doi.org/10.1016/j.ijcip.2015.04.003).

**Problem addressed.** The paper responds to the difficulty of representing heterogeneous, tightly coupled infrastructures with a single homogeneous model.

**Representation.** It uses a multilayer hybrid modeling framework and separates different subsystem/layer functions so that appropriate models can be assigned while preserving an integrated view.

**Stage-1 transfer.** This supports the use of explicit typed layers and the distinction between the physical infrastructure core and supporting information/operational/human-organizational domains. It is conceptually consistent with the frozen thesis ontology:

```math
\boxed{
\mathcal S=\{P,T,I,O\},
\qquad
\mathcal S_{\rm phys}=\{P,T\},
\qquad
\mathcal S_{\rm sup}=\{I,O\}.
}
```

It also supports explicit hierarchy/orientation $h_e$ and modeling resolution $\ell_e$.

**Non-transfer boundary.** The paper's exact layer decomposition is not adopted as thesis authority. The frozen $P,T,I,O$ ontology governs.

---

### 4.6 Zhou et al. (2020) — infrastructure → representation → interface

**Reference:** Zhou, S., Yang, Y., Ng, S. T., Xu, J. F., & Li, D. (2020). *Integrating data-driven and physics-based approaches to characterize failures of interdependent infrastructures*. International Journal of Critical Infrastructure Protection, 31, 100391. [https://doi.org/10.1016/j.ijcip.2020.100391](https://doi.org/10.1016/j.ijcip.2020.100391).

**Problem addressed.** The paper argues that heterogeneous infrastructures should not all be forced into the same modeling methodology because they differ in physical knowledge, data availability, operating mechanisms, and failure characteristics.

**Framework.** Zhou et al. organize their framework around three major modules:
1. understand/profile each target infrastructure;
2. select an appropriate data-driven or physics-based representation for each infrastructure;
3. design interfaces that operationalize interactions between infrastructures and connect the selected models through variables/parameters.

**Stage-1 transfer.** This is probably the closest methodological precedent for the organization of the thesis figure:

```math
\boxed{
\text{system characterization}
\rightarrow
\text{infrastructure representation}
\rightarrow
\text{explicit interface}.
}
```

It strongly supports $\gamma_e$ as explicit interface semantics and $\Phi_e$ as the quantity/service associated with the interface.

**Non-transfer boundary.** Zhou et al. continue into failure propagation. The frozen Stage-1 framework must stop earlier. A designed interface or associated variable does not itself establish a case-specific causal dependency.

---

### 4.7 Hruska, McGillivary, and Edsall (2021) — functional decomposition and cross-sector dependency language

**Reference:** Hruska, R., McGillivary, K., & Edsall, R. (2021). *A Functional All-Hazard Approach to Critical Infrastructure Dependency Analysis*. Journal of Critical Infrastructure Policy, 2(2), 103–123. [https://doi.org/10.18278/jcip.2.2.6](https://doi.org/10.18278/jcip.2.2.6).

**Problem addressed.** The All-Hazards Analysis methodology seeks a common functional basis for analyzing interconnected infrastructure systems across sectors.

**Representation.** Infrastructure systems are decomposed functionally and represented through directed multidimensional graphs. The approach is intended to support evaluation of cross-sector dependencies before, during, and after disruption.

**Stage-1 transfer.** The strongest contribution to Stage 1 is the focus on **function and service** rather than anonymous graph adjacency. This supports the frozen entity function $f_i$, exchanged/enabled service $\Phi_e$, modeling resolution $\ell_e$, and the service/requirement traceability chain.

**Non-transfer boundary.** A function-level relation can justify investigating an intersystem candidate, but case-specific causal acceptance still requires Stage 2.

---

### 4.8 Fotouhi, Moryadee, and Miller-Hooks (2017) — direct Power–Transportation architecture

**Reference:** Fotouhi, H., Moryadee, S., & Miller-Hooks, E. (2017). *Quantifying the resilience of an urban traffic-electric power coupled system*. Reliability Engineering & System Safety, 163, 79–94. [https://doi.org/10.1016/j.ress.2017.01.026](https://doi.org/10.1016/j.ress.2017.01.026).

**Problem addressed.** The paper quantifies resilience in an urban coupled traffic–electric-power system while explicitly representing interactions between the two lifelines.

**Representation.** It uses a two-layer traffic–power representation. Interdependencies are represented through linking variables and logical constraints rather than by treating all cross-layer edges as equivalent.

**Stage-1 transfer.** This is the strongest direct precedent for displaying the physical $P/T$ core and separating candidate directions:

```math
\boxed{
P\rightarrow T
\qquad
T\rightarrow P.
}
```

The paper provides direct precedent for mechanism families such as electrical support of transportation functionality and transportation constraints on power restoration.

**Non-transfer boundary.** The study models specified cross-system links. Those links must not be automatically transferred to a different case. In Stage 1 they remain mechanism templates or structurally admissible candidates until case-specific evidence is attached.

---

### 4.9 Anokhin et al. (2021) — recovery-activated transportation-to-power relation

**Reference:** Anokhin, D., Dehghanian, P., Lejeune, M. A., & Su, J. (2021). *Mobility-As-A-Service for Resilience Delivery in Power Distribution Systems*. Production and Operations Management, 30(8), 2492–2521. [https://doi.org/10.1111/poms.13393](https://doi.org/10.1111/poms.13393).

**Problem addressed.** The work coordinates mobile power resources and repair crews while accounting for both energy- and transportation-network constraints during disaster recovery.

**Stage-1 transfer.** It provides strong evidence for a recovery-mode candidate mechanism:

```math
\boxed{
T\rightarrow P:
\quad
\text{transport accessibility}
\rightarrow
\text{power-restoration feasibility/time}.
}
```

This directly supports $m_e^{\rm cand}$, $\Phi_e$ and, especially, activation context:

```math
c_e^{\rm cand}=\mathrm{recovery}.
```

**Non-transfer boundary.** Spatial proximity of a road to a power asset is insufficient. The road must actually support a relevant restoration route, crew, mobile-power-resource movement, or other case-specific restoration function.

---

### 4.10 Yu et al. (2025) — organizational and logical interdependencies

**Reference:** Yu, D. J., Shin, H. C., Olivier, T., Garcia, M., Meerow, S., & Park, J. (2025). *Logical interdependencies in infrastructure: What are they, how to identify them, and what do they mean for infrastructure risk analysis?* Risk Analysis, 45(2), 356–375. [https://doi.org/10.1111/risa.16555](https://doi.org/10.1111/risa.16555).

**Problem addressed.** The paper addresses the difficulty of operationalizing logical interdependencies and focuses on formal/informal rules and human decisions that coordinate infrastructure systems.

**Representation.** Rule statements are translated into syntactic and network forms, and network motifs are used to identify logical interdependency patterns.

**Stage-1 transfer.** This is a strong precedent for keeping the organizational domain $O$ explicit and for representing rule-mediated relationships separately from purely physical $P\leftrightarrow T$ relations. It supports organizational candidate mechanism metadata and rule-based provenance.

**Non-transfer boundary.** Organizational/logical relations can coexist with physical, geographic, and cyber relations, but they must not be collapsed into a single undifferentiated physical edge.

---

### 4.11 Lu et al. (2025) — existence is not strength

**Reference:** Lu, Q.-C., Wang, S., Xu, P.-C., Li, J., Meng, X., & Hussain, A. (2025). *Modeling the dependency relationship of coupled power and transportation networks*. Energy, 320, 135330. [https://doi.org/10.1016/j.energy.2025.135330](https://doi.org/10.1016/j.energy.2025.135330).

**Problem addressed.** The paper develops a supply-demand-based method for quantifying dependency in coupled power and transportation networks while accounting for heterogeneity of fast-charging stations.

**Representation.** Dependency magnitude changes with interface characteristics, charging price, redundancy, EV penetration, network position, and failure conditions.

**Stage-1 transfer.** The paper strongly reinforces the frozen distinction:

```math
\boxed{
I_e^{\rm struct}
\neq
w_e
\neq
q_e^{\rm evid}.
}
```

The existence of an interface and the magnitude of dependency are different scientific questions.

**Non-transfer boundary.** The dependency-strength calculation assumes a coupled relation structure. Therefore Stage 1 must not infer $w_e$ before relation qualification:

```math
\boxed{
w_e=\mathrm{NOT\_ESTIMATED\_STAGE1}.
}
```

---

## 5. Synthesis: what the literature supports

The papers do not all solve the same problem. Their value is complementary.

### 5.1 Level A — System context

Rinaldi et al. establish that infrastructure interdependencies must be interpreted with respect to system characteristics and operating conditions, while Nan and Sansavini show the importance of layered representation for heterogeneous infrastructures ([Rinaldi et al., 2001](https://doi.org/10.1109/37.969131); [Nan & Sansavini, 2015](https://doi.org/10.1016/j.ijcip.2015.04.003)).

Therefore the first visual level should answer:

```math
\boxed{
\text{WHAT SYSTEM ARE WE STUDYING?}
}
```

and show the frozen objects:

```math
\Omega_{\rm sys}^{+},
\qquad
\mathcal S=\{P,T,I,O\}.
```

### 5.2 Level B — Infrastructure structure

McNally et al. provide direct precedent for intradomain/cross-domain separation and spatial ontology, while Filippini and Silva show why structural/functional representation should precede dynamic propagation ([McNally et al., 2007](https://doi.org/10.1068/b32078); [Filippini & Silva, 2014](https://doi.org/10.1016/j.ress.2013.09.010)).

The second visual level should answer:

```math
\boxed{
\text{WHAT EXISTS AND HOW IS EACH SYSTEM ORGANIZED?}
}
```

with:

```math
G_P=(V_P,E_P,\lambda_P),
\qquad
G_T=(V_T,E_T,\lambda_T),
\qquad
E_i^\alpha,
\qquad
r_i.
```

### 5.3 Level C — Cross-system interface space

Zhou et al. provide the clearest methodological precedent for making interfaces explicit rather than using generic cross-layer connections, while Fotouhi et al. provide direct Power–Transportation precedent for two-layer coupling ([Zhou et al., 2020](https://doi.org/10.1016/j.ijcip.2020.100391); [Fotouhi et al., 2017](https://doi.org/10.1016/j.ress.2017.01.026)).

This level should answer:

```math
\boxed{
\text{WHERE COULD }P\text{ AND }T\text{ INTERACT?}
}
```

and show candidate directions separately:

```math
\boxed{
P\rightarrow T
\qquad\qquad
T\rightarrow P
}
```

with interface/service semantics:

```math
\gamma_e,
\quad
\Phi_e,
\quad
d_e,
\quad
m_e^{\rm cand},
\quad
c_e^{\rm cand}.
```

The correct label is **structurally admissible candidate relations**, not accepted causal interdependencies.

### 5.4 Evidence layer

Ouyang provides the broader evidence/modeling context, Hruska et al. provide function-centered dependency reasoning, and Yu et al. show how organizational/rule evidence can be represented explicitly ([Ouyang, 2014](https://doi.org/10.1016/j.ress.2013.06.040); [Hruska et al., 2021](https://doi.org/10.18278/jcip.2.2.6); [Yu et al., 2025](https://doi.org/10.1111/risa.16555)).

The evidence layer should answer:

```math
\boxed{
\text{IS THE CANDIDATE STRUCTURALLY AND EVIDENTIALLY DEFENSIBLE?}
}
```

The frozen relation record is:

```math
\boxed{
\mathfrak r_e^{(1)}
=
(
\mathcal V_e,
\sigma_e,
\Gamma_e^{\rm str},
\gamma_e,
\Phi_e,
d_e,
m_e^{\rm cand},
c_e^{\rm cand},
s_e,
\mathcal E_e
).
}
```

The secondary metadata remains:

```math
\boxed{
a_e=
(
h_e,
\pi_e,
\kappa_e,
\ell_e,
b_e,
q_e^{\rm evid},
\chi_e^{\rm norm}
).
}
```

### 5.5 G1 freeze gate

The explicit six-gate contract:

```text
G1-B  boundary explicit
G1-E  entities semantically defined
G1-I  intralayer structures physically defensible
G1-R  intersystem relation candidates explicitly characterized
G1-P  provenance traceable
G1-C  premature causal claims prevented
```

is a thesis governance mechanism. The reviewed literature provides foundations for the ingredients, but this targeted scan did not identify a paper reproducing the exact G1-B/E/I/R/P/C PASS/FAIL/BLOCKED freeze contract.

Therefore the figure must distinguish:

- **literature-grounded scientific ingredients**, and
- **thesis-defined Stage-1 governance integration**.

This avoids overstating novelty or attributing the thesis gate architecture to a source that does not contain it.

---

## 6. Recommended literature-grounded Stage-1 figure architecture

The thesis figure should use **three scientific levels + one evidence layer + one gate**:

```text
┌─────────────────────────────────────────────────────────────┐
│ STAGE 1 — STRUCTURAL FOUNDATION FOR P–T INTERDEPENDENCY     │
│ What exists, how is it organized, and where could P and T   │
│ interact?                                                   │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│ LEVEL A — SYSTEM CONTEXT                                    │
│ Ω_sys+                      𝒮 = {P,T,I,O}                   │
│ Space • Time • Infra • Service • Mode • Jurisdiction       │
│ Question: WHAT SYSTEM ARE WE STUDYING?                      │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│ LEVEL B — INFRASTRUCTURE STRUCTURE                          │
│ Power: G_P               Transportation: G_T                │
│ Semantic entities: E_i^α    Geometry: r_i                   │
│ INTRA: P→P, T→T                                            │
│ Question: WHAT EXISTS AND HOW IS EACH SYSTEM ORGANIZED?     │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│ LEVEL C — CROSS-SYSTEM INTERFACE SPACE                     │
│                  candidate P → T                            │
│            POWER P ───────────────▶ TRANSPORT T             │
│            POWER P ◀─────────────── TRANSPORT T             │
│                  candidate T → P                            │
│ γ_e • Φ_e • d_e • m_e^cand • c_e^cand                     │
│ Γ_e^str = structurally admissible?                          │
│ CONTEXT kept separate: η→P, η→T                            │
│ Question: WHERE COULD THE SYSTEMS INTERACT?                 │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│ EVIDENCE LAYER                                              │
│ Literature • GIS • asset records • operator evidence       │
│ standards/requirements • empirical observations            │
│                         ↓                                   │
│                  𝔯_e^(1)                                   │
│ WHO? WHERE? WHAT? DIRECTION? HOW? WHEN? EVIDENCE?           │
│ I_e^struct ≠ w_e ≠ q_e^evid                                │
│ w_e = NOT_ESTIMATED_STAGE1                                 │
└─────────────────────────────┬───────────────────────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │ G1 FREEZE GATE   │
                    │ B E I R P C      │
                    └────────┬─────────┘
                             │ PASS
                             ▼
                    ┌──────────────────┐
                    │ Z_1^impl+        │
                    │ STAGE-1 HANDOFF  │
                    └────────┬─────────┘
                             │
                             ▼
                          STAGE 2
                    CAUSAL QUALIFICATION
```

---

## 7. Why this organization is preferable to five equal boxes

The framework is easier to understand when the boxes have different scientific roles.

**Levels A–C are ontological/structural.** They progressively answer system, entity/network, and interface questions.

**The evidence layer is epistemic.** It asks what evidence supports retention of a candidate and records provenance, confidence, and normative applicability.

**G1 is governance.** It does not describe another infrastructure phenomenon; it decides whether the Stage-1 representation is admissible for handoff.

This separation prevents a common visual error: presenting ontology, evidence, and validation gates as if they were all equivalent physical stages of the infrastructure.

The resulting high-level logic is:

```math
\boxed{
\text{DEFINE}
\rightarrow
\text{STRUCTURE}
\rightarrow
\text{LOCATE POSSIBLE INTERACTIONS}
\rightarrow
\text{GROUND IN EVIDENCE}
\rightarrow
\text{FREEZE/HANDOFF}.
}
```

---

## 8. Scientific guardrails that must remain visible or in the figure caption

The literature supports the importance of distinguishing multiple relation types and interfaces, but the thesis figure must retain the frozen scientific safeguards:

```math
\boxed{
\begin{aligned}
\text{topology}&\neq\text{function},\\
\text{proximity}&\neq\text{dependency},\\
\text{correlation}&\neq\text{causality},\\
\text{standardized interface}&\neq\text{case-specific connection},\\
\text{case connection}&\neq\text{causal mechanism},\\
\text{common cause}&\neq\text{cross-infrastructure dependency},\\
I_e^{\rm struct}&\neq w_e\neq q_e^{\rm evid}.
\end{aligned}
}
```

A compact figure can display only the master rule:

```math
\boxed{
\text{structural possibility}
\neq
\text{causal interdependency}.
}
```

The full set should then appear in the caption or accompanying methodology text.

---

## 9. Literature-grounded novelty boundary

The reviewed literature establishes substantial precedent for the **ingredients** of the framework:

- infrastructure-interdependency concepts and context;
- ontology-based entity representation;
- intradomain/cross-domain distinction;
- functional dependencies and service semantics;
- multilayer architecture;
- heterogeneous infrastructure-specific modeling;
- explicit interface design;
- direct traffic–power coupled-system models;
- restoration-access $T\to P$ mechanisms;
- organizational/logical interdependencies;
- quantitative dependency-strength models.

Accordingly, the thesis should **not** claim that entity representation, multilayer modeling, functional dependency, interface modeling, $P\to T$, $T\to P$, or coupling-strength analysis are individually novel.

The defensible thesis contribution at Stage 1 is the **controlled synthesis and governance architecture** that makes these ingredients interoperable while preserving strict boundaries among:

```math
\boxed{
\text{structural admissibility},
\quad
\text{case evidence},
\quad
\text{causal qualification},
\quad
\text{coupling strength},
\quad
\text{evidence confidence},
\quad
\text{normative admissibility}.
}
```

A careful wording is:

> Existing studies provide established foundations for infrastructure taxonomies, ontology-based intra/cross-system representation, functional dependencies, multilayer architectures, interface-based model coupling, logical interdependencies, and direct Power–Transportation interaction models. The Stage-1 framework synthesizes these foundations into a controlled structural workflow that separates structural admissibility, evidence provenance, causal qualification, coupling strength, evidence confidence, and normative admissibility before dynamic resilience analysis ([Rinaldi et al., 2001](https://doi.org/10.1109/37.969131); [McNally et al., 2007](https://doi.org/10.1068/b32078); [Filippini & Silva, 2014](https://doi.org/10.1016/j.ress.2013.09.010); [Zhou et al., 2020](https://doi.org/10.1016/j.ijcip.2020.100391); [Fotouhi et al., 2017](https://doi.org/10.1016/j.ress.2017.01.026)).

This statement is a synthesis claim. It should not be converted into an exhaustive novelty claim unless a systematic novelty review is separately completed.

---

## 10. Visual precedents to use

The following four papers are the strongest **visual-architecture precedents** for the eventual Stage-1 thesis figure:

| Precedent | Visual principle to borrow | Thesis translation |
|---|---|---|
| [McNally et al. (2007)](https://doi.org/10.1068/b32078) | Ontology + geographic representation; intra/cross-domain separation. | Entity/network layer followed by explicit INTRA/INTER distinction. |
| [Zhou et al. (2020)](https://doi.org/10.1016/j.ijcip.2020.100391) | Infrastructure → modeling/representation → interface workflow. | System context → infrastructure structure → cross-system interface space. |
| [Filippini & Silva (2014)](https://doi.org/10.1016/j.ress.2013.09.010) | Structural representation precedes dynamic propagation and resilience. | Stage 1 visually ends before causal/dynamic analysis. |
| [Fotouhi et al. (2017)](https://doi.org/10.1016/j.ress.2017.01.026) | Two-layer traffic–power representation with explicit linking relations. | Central physical $P/T$ core with separate candidate $P\to T$ and $T\to P$ arrows. |

The visual structures should be used as **scientific precedents**, not copied graphically. The thesis figure should be an original synthesis governed by the frozen Stage-1 ontology and notation.

---

## 11. Suggested thesis figure caption

> **Figure X. Evidence-grounded Stage-1 structural framework for coupled Power–Transportation interdependency analysis.** Stage 1 defines the system context, semantic entities and intralayer structures, identifies structurally admissible cross-system interface candidates, and records each candidate through an evidence- and provenance-controlled relation object before the six-gate G1 handoff. The organization synthesizes established concepts from critical-infrastructure interdependency taxonomy, ontology/GIS, functional-dependency, multilayer, interface-integration, and direct traffic–power modeling literature ([Rinaldi et al., 2001](https://doi.org/10.1109/37.969131); [McNally et al., 2007](https://doi.org/10.1068/b32078); [Filippini & Silva, 2014](https://doi.org/10.1016/j.ress.2013.09.010); [Nan & Sansavini, 2015](https://doi.org/10.1016/j.ijcip.2015.04.003); [Zhou et al., 2020](https://doi.org/10.1016/j.ijcip.2020.100391); [Fotouhi et al., 2017](https://doi.org/10.1016/j.ress.2017.01.026)). Structural admissibility does not imply causal interdependency; causal qualification is deferred to Stage 2.

---

## 12. References

1. Rinaldi, S. M., Peerenboom, J. P., & Kelly, T. K. (2001). Identifying, understanding, and analyzing critical infrastructure interdependencies. *IEEE Control Systems Magazine, 21*(6), 11–25. [https://doi.org/10.1109/37.969131](https://doi.org/10.1109/37.969131)

2. McNally, R. K., Lee, S.-W., Yavagal, D., & Xiang, W.-N. (2007). Learning the Critical Infrastructure Interdependencies through an Ontology-Based Information System. *Environment and Planning B: Planning and Design, 34*(6), 1103–1124. [https://doi.org/10.1068/b32078](https://doi.org/10.1068/b32078)

3. Ouyang, M. (2014). Review on modeling and simulation of interdependent critical infrastructure systems. *Reliability Engineering & System Safety, 121*, 43–60. [https://doi.org/10.1016/j.ress.2013.06.040](https://doi.org/10.1016/j.ress.2013.06.040)

4. Filippini, R., & Silva, A. (2014). A modeling framework for the resilience analysis of networked systems-of-systems based on functional dependencies. *Reliability Engineering & System Safety, 125*, 82–91. [https://doi.org/10.1016/j.ress.2013.09.010](https://doi.org/10.1016/j.ress.2013.09.010)

5. Nan, C., & Sansavini, G. (2015). Multilayer hybrid modeling framework for the performance assessment of interdependent critical infrastructures. *International Journal of Critical Infrastructure Protection, 10*, 18–33. [https://doi.org/10.1016/j.ijcip.2015.04.003](https://doi.org/10.1016/j.ijcip.2015.04.003)

6. Zhou, S., Yang, Y., Ng, S. T., Xu, J. F., & Li, D. (2020). Integrating data-driven and physics-based approaches to characterize failures of interdependent infrastructures. *International Journal of Critical Infrastructure Protection, 31*, 100391. [https://doi.org/10.1016/j.ijcip.2020.100391](https://doi.org/10.1016/j.ijcip.2020.100391)

7. Hruska, R., McGillivary, K., & Edsall, R. (2021). A Functional All-Hazard Approach to Critical Infrastructure Dependency Analysis. *Journal of Critical Infrastructure Policy, 2*(2), 103–123. [https://doi.org/10.18278/jcip.2.2.6](https://doi.org/10.18278/jcip.2.2.6)

8. Fotouhi, H., Moryadee, S., & Miller-Hooks, E. (2017). Quantifying the resilience of an urban traffic-electric power coupled system. *Reliability Engineering & System Safety, 163*, 79–94. [https://doi.org/10.1016/j.ress.2017.01.026](https://doi.org/10.1016/j.ress.2017.01.026)

9. Anokhin, D., Dehghanian, P., Lejeune, M. A., & Su, J. (2021). Mobility-As-A-Service for Resilience Delivery in Power Distribution Systems. *Production and Operations Management, 30*(8), 2492–2521. [https://doi.org/10.1111/poms.13393](https://doi.org/10.1111/poms.13393)

10. Yu, D. J., Shin, H. C., Olivier, T., Garcia, M., Meerow, S., & Park, J. (2025). Logical interdependencies in infrastructure: What are they, how to identify them, and what do they mean for infrastructure risk analysis? *Risk Analysis, 45*(2), 356–375. [https://doi.org/10.1111/risa.16555](https://doi.org/10.1111/risa.16555)

11. Lu, Q.-C., Wang, S., Xu, P.-C., Li, J., Meng, X., & Hussain, A. (2025). Modeling the dependency relationship of coupled power and transportation networks. *Energy, 320*, 135330. [https://doi.org/10.1016/j.energy.2025.135330](https://doi.org/10.1016/j.energy.2025.135330)

---

## 13. Repository governance note

This document is **supporting evidence only**. It does not change the frozen Stage-1 ontology, mathematical objects, controlled vocabularies, G1 gates, machine schemas, or Stage-1 → Stage-2 boundary.

If a future literature review justifies a semantic change to a frozen Stage-1 object, the change must follow the explicit amendment/unfreeze procedure in:

`thesis/00_governance/STAGE1_FRAMEWORK_FREEZE_2026-09-18.md`.

Until such an amendment is approved:

```math
\boxed{
G_1^{\rm framework}=\mathrm{PASS\ —\ FROZEN}.
}
```
