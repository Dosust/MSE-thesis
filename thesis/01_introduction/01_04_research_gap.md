# 1.4 Research Gap

Section 1.3 established that the engineering problem is not simply to represent interconnected infrastructure, but to preserve a traceable progression from structure and directional dependency mechanisms to dynamic behavior, feasible response, service-level resilience, intervention consequences, and engineering decision-making. The purpose of this section is narrower: to identify which transitions in that progression are already well developed and which remain insufficiently established for the bounded Power–Transportation problem considered in this thesis.

Research on interdependent critical infrastructure is already extensive. Existing approaches include network, agent-based, system-dynamics, empirical, stochastic, optimization, and data-driven formulations (Ouyang, 2014). Recent reviews confirm substantial advances in multiplex representations, resilience assessment, recovery strategies, uncertainty treatment, and intervention modeling while continuing to identify challenges involving interdependency representation, performance evolution, observation quality, uncertainty, multi-hazard conditions, and trade-offs among resilience objectives (Wang et al., 2024; Tong et al., 2025; Ghasemkhani et al., 2026). Coupled Power–Transportation research is similarly mature: recent work already addresses EV-mediated coupling, transportation-constrained restoration, flood-responsive traffic–power dynamics, emergency-resource dispatch, behavior-dependent charging, and communication-aware recovery (Oladigbolu et al., 2025; Lian et al., 2026; Wang et al., 2026; Zhang et al., 2026). **Coupled P–T modeling itself is therefore not the research gap.**

The evidence synthesis instead supports six bounded gaps concerning the **integration, incremental engineering value, and validation** of successive transitions in the proposed reasoning chain.

## 1.4.1 G1 — From structural interconnection to evidence-qualified causal dependency

Infrastructure research already provides established taxonomies and multilayer representations for dependencies and interdependencies. However, a structural relation does not establish why a receiving component changes state, under what conditions that effect becomes active, or whether the relationship is directional or reciprocal. Dasuni et al. (2025) report continuing fragmentation in dependency/interdependency classification and identify the risk of obscuring dependency direction when reciprocal and one-way relationships are treated interchangeably.

For the present thesis, this matters because electricity supply to a transportation asset, EV charging demand on a feeder, road accessibility for repair crews, and common flood exposure are physically different objects. The gap is therefore not the absence of taxonomies but the need for a reproducible transition from a **candidate structural relation** to an **evidence-qualified directional dependency mechanism** with explicit source, receiver, mechanism, activation condition, parameterization, uncertainty, and validity domain:

```math
\boxed{
G_1:\quad
\text{structural relation}
\not\Rightarrow
\text{evidence-qualified causal dependency mechanism}.
}
```

This gap supports **RQ1–RQ2 and SO1–SO2**: RQ1 establishes what exists and where interaction is possible; RQ2 establishes why and through which mechanism an effect can propagate.

## 1.4.2 G2 — Incremental value of dynamic causal coupling

The broad claim that coupled-infrastructure models are static is no longer defensible. Contemporary P–T studies already include dynamic traffic evolution, hazard-responsive accessibility, emergency-resource dispatch, multi-stage restoration, and behavioral charging responses (Lian et al., 2026; Wang et al., 2026; Zhang et al., 2026). The unresolved question is therefore comparative rather than existential: **does an evidence-qualified, state-, time-, and mode-dependent coupling representation materially improve engineering inference relative to simpler representations under matched conditions?**

The gap is expressed through the controlled hierarchy

```math
\boxed{
M_0
\quad\text{vs}\quad
M_1
\quad\text{vs}\quad
M_2,
}
```

where `M_0` represents independent systems, `M_1` static or algebraic coupling, and `M_2` dynamic causal coupling. The comparison must preserve common disturbances, initial conditions, controls, parameters, and assessment horizons. The corresponding gap is therefore

```math
\boxed{
G_2:\quad
\text{dynamic coupling exists, but its incremental engineering value must be tested}.
}
```

This gap generates **RQ3, SO3, and H1**.

## 1.4.3 G3 — From physical dynamics to observation- and organization-constrained feasible response

Information, communication, institutional constraints, and human–infrastructure interactions are already recognized in infrastructure-resilience research (Rasoulkhani & Mostafavi, 2018; Chester et al., 2021; Gim & Miller, 2022). State-estimation frameworks also exist for interdependent infrastructure, and recent P–T work explicitly includes communication-mediated recovery (Moazeni et al., 2020; Zhang et al., 2026). The gap is therefore not that information or organization have never been considered.

The unresolved engineering question is whether, **under the same physical disturbance**, differences in observation quality, state estimation, information availability, authority, coordination, personnel, equipment, or response delay materially change the feasible action set and resulting service trajectories. In the thesis this is represented conceptually as

```math
\boxed{u(t)=\pi\!\left(\hat X(t),I(t),O(t)\right),}
```

so that physical state `X(t)` alone does not determine realized response. The matched comparison is

```math
\boxed{
P+T
\quad\text{vs}\quad
P+T+I
\quad\text{vs}\quad
P+T+I+O.
}
```

This gap generates **RQ4, SO4, and H2**.

## 1.4.4 G4 — From aggregate recovery performance to remain–return–confidence resilience

Performance and recovery curves are established tools for infrastructure-resilience assessment, and the literature already contains multiple performance measures, thresholds, targets, and summary metrics (Poulin & Kane, 2021; Trucco & Petrenj, 2023). Viability and reachability are likewise established mathematical theories; their existence is not a novelty claim. The unresolved question is whether applying them to evidence-qualified coupled P–T dynamics and explicit service constraints provides **incremental decision-relevant information** beyond conventional performance/recovery analysis.

The thesis therefore distinguishes three engineering questions:

```math
\boxed{
\begin{aligned}
\textbf{Remain:}\;&\text{Can required services remain within admissible limits?}\\
\textbf{Return:}\;&\text{If limits are violated, can acceptable service be recovered in time?}\\
\textbf{Confidence:}\;&\text{How strongly are these conclusions supported under uncertainty?}
\end{aligned}}
```

The corresponding resilience object `\mathfrak R_T`, formally defined in Chapter 3, is compared with conventional resilience-curve information:

```math
\boxed{
R_{\rm curve}
\quad\text{vs}\quad
R_{\rm curve}+\mathfrak R_T.
}
```

Thus,

```math
\boxed{
G_4:\quad
\text{the incremental engineering value of remain--return--confidence information must be demonstrated}.
}
```

This gap generates **RQ5, SO5, and H3**.

## 1.4.5 G5 — From resilience improvement to intervention consequences

A wide range of resilience interventions is already present in P–T research, including hardening, charging coordination, EV and mobile-energy resources, network reconfiguration, repair routing, and coordinated recovery (Oladigbolu et al., 2025; Lian et al., 2026). Resilience and sustainability have also been considered jointly; Mitoulis et al. (2023), for example, evaluate recovery using resilience, greenhouse-gas emissions, and cost. The gap is therefore not the absence of resilience–sustainability integration.

The unresolved issue is whether candidate interventions that appear similar in resilience terms differ materially in the **resources required and sustainability consequences** of obtaining that resilience within the same bounded P–T problem. The thesis therefore preserves

```math
\boxed{\text{effectiveness}\neq\text{efficiency}\neq\text{sustainability}.}
```

and evaluates candidate actions through the canonical consequence representation

```math
\boxed{
a_k
\rightarrow
\left(
\Delta\mathfrak R^{a_k},
\Delta\mathbf J_{\rm sus}^{a_k}
\right),
}
```

with resource-efficiency measures declared separately where defensible. This gap generates **RQ6, SO6, and H4**.

## 1.4.6 G6 — From intervention consequences to defensible engineering decision

Multi-objective infrastructure optimization is also well established. Existing studies evaluate combinations of resilience, cost, emissions, reliability, recovery time, and other objectives, and recent reviews emphasize the importance of trade-offs rather than one-dimensional improvement (Tong et al., 2025; Mitoulis et al., 2023). The remaining question is therefore whether incorporating the efficiency and sustainability consequences derived from the same P–T analysis materially changes the admissible or nondominated intervention set relative to a resilience-only decision.

Let `\mathcal A_R^\star` denote the resilience-oriented decision set and `\mathcal A_{R,S}^\star` the corresponding set when declared sustainability consequences, feasibility constraints, and uncertainty are included. The testable gap is

```math
\boxed{
G_6:\quad
\mathcal A_R^\star
\overset{?}{=}
\mathcal A_{R,S}^\star.
}
```

If the sets remain equivalent within uncertainty and predeclared materiality criteria, additional sustainability information has not demonstrated decision value for that regime. This gap generates **RQ7, SO7, and H5**.

## 1.4.7 Synthesis of the Research Gap

The six gaps form one dependent argument rather than six unrelated deficiencies:

```math
\boxed{
\begin{aligned}
G_1 &: \text{structure}\rightarrow\text{qualified causal mechanism},\\
G_2 &: \text{mechanism}\rightarrow\text{validated dynamic consequence},\\
G_3 &: \text{dynamics + knowledge}\rightarrow\text{feasible action},\\
G_4 &: \text{dynamics + action + uncertainty}\rightarrow\text{remain / return / confidence},\\
G_5 &: \text{resilience diagnosis}\rightarrow\text{intervention consequences},\\
G_6 &: \text{consequences + feasibility + uncertainty}\rightarrow\text{engineering decision}.
\end{aligned}}
```

There are **six gaps but seven specific research questions** because `G_1` contains two sequential obligations: **RQ1** establishes the system structure and possible interfaces, while **RQ2** qualifies the causal dependency mechanisms. Thereafter, `G_2\rightarrow RQ3`, `G_3\rightarrow RQ4`, `G_4\rightarrow RQ5`, `G_5\rightarrow RQ6`, and `G_6\rightarrow RQ7`.

The principal gap can therefore be stated as follows:

> **Existing research provides substantial solutions for individual components of interdependent-infrastructure resilience, including dependency classification, multilayer modeling, dynamic propagation, adaptive recovery, information and communication coupling, resilience metrics, viability/reachability theory, and resilience–sustainability optimization. Within the bounded Power–Transportation problem considered here, the evidence reviewed to date has not established a sufficiently traceable and comparatively validated chain connecting evidence-qualified directional dependency mechanisms to hybrid physical dynamics; observation-, information-, and organization-constrained feasible actions; service-level remain–return–confidence resilience; intervention consequences; and the resulting sustainable-engineering decision under uncertainty.**

The thesis is therefore framed as an **integration, incremental-value, and validation problem**, not as a claim that its individual mathematical or engineering ingredients are new. The governing traceability is

```math
\boxed{
G_i
\rightarrow
RQ_i
\rightarrow
SO_i
\rightarrow
H_i
\rightarrow
\text{comparator}
\rightarrow
\text{experiment}
\rightarrow
\text{VVUQ}
\rightarrow
\text{bounded inference}.
}
```

An evidence-supported gap is not proof of global novelty. Any closer prior work identified during the continuing literature and novelty audit must narrow the relevant claim rather than be excluded.

These unresolved transitions are also sustainable-engineering concerns because they affect whether electricity and mobility services can be maintained or recovered using interventions whose resource requirements and broader consequences are acceptable. **Section 1.5 therefore establishes the Sustainable Engineering significance of addressing these gaps.**

## References cited in Section 1.4

- Béné, C., & Doyen, L. (2018). From resistance to transformation: A generic metric of resilience through viability. *Earth's Future, 6*(7), 979–996. https://doi.org/10.1002/2017EF000660
- Chester, M., Underwood, B. S., Allenby, B., Garcia, M., Samaras, C., Markolf, S., Sanders, K., Preston, B., & Miller, T. R. (2021). Infrastructure resilience to navigate increasingly uncertain and complex conditions in the Anthropocene. *npj Urban Sustainability, 1*, Article 4. https://doi.org/10.1038/s42949-021-00016-y
- Dasuni, K. A. L., Palliyaguru, R., Amaratunga, D., & Liyanawatta, T. N. (2025). Redefining ‘dependencies/interdependencies’ of critical infrastructure: A systematic review of the existing knowledgebase. *Sustainable and Resilient Infrastructure, 10*(2), 202–222. https://doi.org/10.1080/23789689.2024.2403885
- Ghasemkhani, A., Basiri, M. A., & Nicholson, C. (2026). Interdependency and uncertainty in the resiliency of infrastructure networks: A comprehensive review. *International Journal of Critical Infrastructure Protection, 54*, 100866. https://doi.org/10.1016/j.ijcip.2026.100866
- Gim, C., & Miller, C. A. (2022). Institutional interdependence and infrastructure resilience. *Current Opinion in Environmental Sustainability, 57*, 101203. https://doi.org/10.1016/j.cosust.2022.101203
- Lian, X., Song, C., Li, Z., Qiu, L., & Liu, L. (2026). Resilience-oriented emergency resource dispatch for power–transportation coupled networks under rainstorm-induced flood hazards. *Applied Energy, 403*, 127004. https://doi.org/10.1016/j.apenergy.2025.127004
- Mitoulis, S.-A., Bompa, D. V., & Argyroudis, S. (2023). Sustainability and climate resilience metrics and trade-offs in transport infrastructure asset recovery. *Transportation Research Part D: Transport and Environment, 121*, 103800. https://doi.org/10.1016/j.trd.2023.103800
- Moazeni, F., Khazaei, J., & Mitra, P. (2020). An integrated state-estimation framework for interdependent water and energy systems. *Journal of Hydrology, 590*, 125393. https://doi.org/10.1016/j.jhydrol.2020.125393
- Oladigbolu, J., Bakare, M. S., Motlagh, S. G., Mujeeb, A., & Li, L. (2025). A review on transport and power systems planning-operation integrating electric vehicles, energy storage, and other distributed energy resources. *Journal of Energy Storage, 135*, 118419. https://doi.org/10.1016/j.est.2025.118419
- Ouyang, M. (2014). Review on modeling and simulation of interdependent critical infrastructure systems. *Reliability Engineering & System Safety, 121*, 43–60. https://doi.org/10.1016/j.ress.2013.06.040
- Poulin, C., & Kane, M. B. (2021). Infrastructure resilience curves: Performance measures and summary metrics. *Reliability Engineering & System Safety, 216*, 107926. https://doi.org/10.1016/j.ress.2021.107926
- Rasoulkhani, K., & Mostafavi, A. (2018). Resilience as an emergent property of human-infrastructure dynamics: A multi-agent simulation model for characterizing regime shifts and tipping point behaviors in infrastructure systems. *PLOS ONE, 13*(11), e0207674. https://doi.org/10.1371/journal.pone.0207674
- Tong, W., Li, H. X., Nasirzadeh, F., Yao, F., & Ji, Y. (2025). Resilience of interdependent infrastructure networks: Review and future directions. *International Journal of Critical Infrastructure Protection, 51*, 100793. https://doi.org/10.1016/j.ijcip.2025.100793
- Trucco, P., & Petrenj, B. (2023). Characterisation of resilience metrics in full-scale applications to interdependent infrastructure systems. *Reliability Engineering & System Safety, 235*, 109200. https://doi.org/10.1016/j.ress.2023.109200
- Wang, S., Lu, Q.-C., Liu, L., Xu, P.-C., Wang, R., & Zhang, L. (2026). Interdependency analysis of coupled power and transportation networks considering the charging decision preferences of EV drivers. *Reliability Engineering & System Safety, 268*, 112005. https://doi.org/10.1016/j.ress.2025.112005
- Wang, Y., Zhao, O., & Zhang, L. (2024). Multiplex networks in resilience modeling of critical infrastructure systems: A systematic review. *Reliability Engineering & System Safety, 250*, 110300. https://doi.org/10.1016/j.ress.2024.110300
- Zhang, S., Li, Y., Zhang, H., Dui, H., & Cao, Y. (2026). A two-stage resilience enhancement framework for power distribution system coupled with intelligent transportation system. *Reliability Engineering & System Safety*. https://doi.org/10.1016/j.ress.2026.113032

## Scientific boundary of Section 1.4

Section 1.4 establishes bounded research needs supported by the present evidence base. It does **not** establish global novelty:

```math
\boxed{\text{evidence-supported research gap}\neq\text{global novelty proof}.}
```

Novelty claims remain conditional on the separate reproducible novelty audit.