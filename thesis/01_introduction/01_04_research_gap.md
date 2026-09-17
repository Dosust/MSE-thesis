# 1.4 Research Gap

Section 1.3 established that the engineering problem is not simply to represent interconnected infrastructure, but to preserve a traceable progression from infrastructure structure and causal interdependency to dynamic behavior, feasible response, service-level resilience, intervention consequences, and engineering decision-making. The purpose of this section is therefore narrower: to determine which links in that progression are already sufficiently developed in the literature and which remain insufficiently established for the bounded Power–Transportation problem considered in this thesis.

Research on interdependent critical infrastructure is already extensive. Modeling approaches include empirical, network-based, agent-based, system-dynamics, economic, stochastic, optimization, and increasingly data-driven formulations (Ouyang, 2014). More recent systematic reviews confirm substantial advances in multiplex-network representations, resilience assessment, recovery strategies, uncertainty treatment, and intervention modeling, while continuing to identify challenges involving interdependency representation, high-resolution observations, multi-hazard conditions, performance-evolution mechanisms, uncertainty, interpretable models, and trade-offs among resilience objectives (Wang et al., 2024; Tong et al., 2025; Ghasemkhani et al., 2026).

The same qualification is necessary for coupled Power–Transportation systems. Recent work already considers joint power–transport operation and planning, electric vehicles and distributed energy resources, transportation-dependent power restoration, flood-responsive traffic conditions, emergency-resource dispatch, behavioral charging decisions, and communication-mediated Power–Transportation interactions (Oladigbolu et al., 2025; Lian et al., 2026; Wang et al., 2026; Zhang et al., 2026). Coupled P–T modeling itself is therefore **not** the research gap.

The evidence synthesis instead indicates a more specific research need: existing studies provide substantial solutions for individual parts of the resilience problem, but the present review has not yet established a sufficiently integrated and comparatively validated treatment that connects **evidence-qualified directional interdependencies, state- and time-dependent physical dynamics, observation and organizational constraints, feasible control, service-level viability and recovery, intervention consequences, and sustainable-engineering decisions under uncertainty**. This overall need is decomposed below into six bounded gaps.

## 1.4.1 G1 — From structural interconnection to evidence-qualified causal interdependency

A substantial literature already exists for classifying and representing infrastructure dependencies and interdependencies. Rinaldi et al. (2001) provided a foundational taxonomy of infrastructure interdependencies, while multilayer and multiplex-network approaches now permit multiple infrastructure systems and several classes of cross-system relationship to be represented explicitly. More recent reviews confirm that such structural representations have become important tools for interdependent-infrastructure resilience analysis.

A structural relation, however, is not equivalent to a causal mechanism. Dasuni et al. (2025), following a systematic review of the dependency/interdependency literature, report continuing fragmentation in classification and specifically identify the risk of obscuring the **direction** of dependency when dependency and reciprocal interdependency are treated interchangeably. This distinction can become consequential during emergencies because a model must identify which system influences which other system, through what mechanism, and under what conditions.

For the present thesis, this issue is particularly important because several physically different phenomena can appear as cross-layer relationships. Electricity supplying a traffic-control device, EV charging demand loading a distribution feeder, road accessibility constraining repair crews, and a flood simultaneously damaging a road and an electrical component do not describe the same causal object. In particular,

```math
\boxed{
\text{common hazard exposure}
\neq
\text{cross-system causal dependency}.
}
```

Likewise,

```math
\boxed{
\text{structural connection}
\neq
\text{demonstrated interdependency mechanism}.
}
```

The first research gap is therefore not the absence of infrastructure-interdependency taxonomies. It is the need, within the bounded P–T study, for a reproducible transition from a **candidate structural relationship** to an **evidence-qualified directional mechanism** whose source, receiver, mechanism, activation conditions, parameters, uncertainty, and validity domain are explicitly recorded.

Formally,

```math
\boxed{
G_1:
\quad
\text{structural relation}
\not\Rightarrow
\text{evidence-qualified causal interdependency}.
}
```

This gap establishes the foundation for **RQ1–RQ2 and SO1–SO2**. Its role is developmental and evidentiary: the thesis must first determine what entities and interfaces exist and then establish which proposed cross-system relations are sufficiently supported to enter the dynamic model.

---

## 1.4.2 G2 — Incremental value of dynamic causal interdependency modeling

The literature no longer supports a broad claim that interdependent-infrastructure models are static. Contemporary P–T studies include time-dependent traffic evolution, hazard-responsive road conditions, dynamic emergency-resource dispatch, multi-stage restoration, stochastic recovery, and behavior-dependent EV charging. Lian et al. (2026), for example, combine flood-routing and traffic-flow models with dynamic emergency-resource dispatch, while Wang et al. (2026) explicitly represent EV-driver charging preferences and disaster-dependent risk perception in P–T interdependency analysis.

Similarly, recent Transportation–Communication–Power research has modeled multilayer cascading failures and coupled pre-disruption protection with post-disruption adaptive recovery (Zhang et al., 2026). Consequently, neither “dynamic coupling” nor “adaptive recovery” can defensibly be presented as absent from the literature.

The unresolved question is more demanding. Different dynamic representations impose different assumptions concerning coupling strength, activation, delay, mode switching, hazard evolution, recovery resources, and behavioral response. Reviews of interdependent-infrastructure resilience continue to identify needs for improved treatment of performance-evolution mechanisms, temporal and geographic behavior, uncertainty, observations, and multi-hazard processes (Wang et al., 2024; Tong et al., 2025; Ghasemkhani et al., 2026).

Accordingly, the scientific question is not whether a more complicated dynamic model can be constructed. It is whether **evidence-qualified dynamic causal coupling provides material explanatory, predictive, or decision-relevant information beyond simpler representations under matched conditions**.

The corresponding gap is

```math
\boxed{
G_2:
\quad
\text{dynamic interdependency exists in the literature,}
\quad
\text{but its incremental value must be demonstrated}.
}
```

This motivates the controlled hierarchy

```math
\boxed{
M_0
\quad\text{vs}\quad
M_1
\quad\text{vs}\quad
M_2,
}
```

where `M_0` represents independent systems, `M_1` a static or algebraic coupling representation, and `M_2` an evidence-qualified dynamic causal-coupling model. Their comparison must preserve common disturbances, initial conditions, parameter assumptions, controls, and evaluation horizons so that any observed difference can be attributed as far as possible to model structure rather than unmatched experimental conditions.

This gap generates **RQ3, SO3, and H1**. Importantly, H1 must permit a negative result: if `M_2` does not produce a practically meaningful improvement beyond numerical, parameter, or model uncertainty for the tested regime, the hypothesis is not supported in that regime.

---

## 1.4.3 G3 — From physical state evolution to observation- and organization-constrained feasible response

Infrastructure resilience is not determined exclusively by physical topology and physical state. Institutional and socio-technical infrastructure research has shown that rules, responsibilities, coordination arrangements, information, and institutional relationships can influence infrastructure planning, operation, adaptation, and recovery. Gim and Miller (2022), for example, distinguish vertical, lateral, and longitudinal institutional interdependencies and argue that infrastructure resilience analysis should extend beyond physical interdependencies alone.

Information and state estimation are likewise not absent from interdependent-infrastructure research. Integrated state-estimation frameworks have already been developed for coupled infrastructure systems, including interdependent water–energy networks (Moazeni et al., 2020). Recent P–T research also includes communication networks explicitly; Zhang et al. (2026), for example, formulate the coupled problem as a Transportation–Communication–Power system.

The gap can therefore not be stated as “existing models ignore information” or “organization has not been considered.” Instead, the relevant engineering question is whether different **information and organizational conditions materially alter feasible response and recovery when the underlying physical disturbance is held constant**.

For the present thesis,

```math
X(t)
```

represents the physical state, whereas the implemented response depends on what is estimated, what information is available, and what organizational capabilities permit:

```math
\boxed{
u(t)
=
\pi\!\left(
\hat X(t),I(t),O(t)
\right).
}
```

Two systems with identical physical states `X(t)` may therefore admit different realized actions if their state estimates, communication availability, authority, coordination, personnel, equipment, or response delays differ. The unresolved issue is whether these differences are large enough to alter critical-service trajectories and recovery outcomes in the bounded P–T system.

Thus,

```math
\boxed{
G_3:
\quad
X(t)
\text{ alone does not establish the feasible response set.}
}
```

This motivates the matched comparison

```math
\boxed{
P+T
\quad\text{vs}\quad
P+T+I
\quad\text{vs}\quad
P+T+I+O,
}
```

without treating `I` and `O` as additional physical infrastructure networks by default.

The gap generates **RQ4, SO4, and H2**.

---

## 1.4.4 G4 — From aggregate performance recovery to remain–return–confidence resilience

Infrastructure-resilience curves and summary metrics are well established. Poulin and Kane (2021) systematically review resilience curves and show that the literature contains multiple categories of performance measures, targets, thresholds, and summary metrics. They also demonstrate that assumptions concerning performance representation and metric construction can materially affect interpretation. Trucco and Petrenj (2023) likewise compare properties, strengths, and limitations of resilience metrics for networked and interdependent infrastructure applications.

Consequently, the present thesis does not treat conventional performance and recovery curves as invalid. They remain an explicit comparator.

Nor is **viability theory itself novel**. Viability analysis is an established mathematical framework for determining whether system dynamics and admissible controls can satisfy state constraints. Béné and Doyen (2018) have already used viability analysis to formalize resilience and recovery in social–ecological systems, including the concept of returning to a viability domain after disruption. More generally, Hamilton–Jacobi reachability and viability theory constitute mature mathematical fields. The thesis therefore cannot base a contribution claim merely on introducing a viability kernel or reachable set.

The more precise research question is whether applying controlled viability and recovery reachability to **evidence-qualified coupled P–T dynamics and explicit service constraints** yields information that conventional resilience curves do not provide for the same engineering decision.

The thesis separates three questions:

```math
\boxed{
\begin{aligned}
\textbf{Remain:}\quad&
\text{Can required coupled services remain within admissible limits?}\\[1mm]
\textbf{Return:}\quad&
\text{If those limits are violated, can acceptable service be recovered}\\
&\text{within an admissible horizon?}\\[1mm]
\textbf{Confidence:}\quad&
\text{How strongly are these conclusions supported under uncertainty?}
\end{aligned}}
```

The research gap is therefore comparative:

```math
\boxed{
G_4:
\quad
\text{Does }
\mathfrak R_T
\text{ provide incremental engineering information beyond }
R_{\rm curve}\text{?}
}
```

This gives the explicit comparator

```math
\boxed{
R_{\rm curve}
\quad\text{vs}\quad
R_{\rm curve}+\mathfrak R_T.
}
```

The gap generates **RQ5, SO5, and H3**. If the viability/reachability representation does not materially change service classification, diagnosis, intervention targeting, or another preregistered decision relative to conventional resilience analysis, then incremental value has not been demonstrated.

---

## 1.4.5 G5 — From resilience improvement to effectiveness, efficiency, and sustainability consequences

A wide range of infrastructure-resilience interventions is already available in both general and P–T-specific research. The contemporary coupled Power–Transportation literature considers hardening, charging coordination, EV and mobile-energy resources, network reconfiguration, repair routing, distributed resources, stochastic and robust optimization, and coordinated pre- and post-disruption actions (Oladigbolu et al., 2025). Recent dynamic P–T studies further demonstrate adaptive emergency-resource deployment and recovery optimization under hazard conditions (Lian et al., 2026; Zhang et al., 2026).

Resilience and sustainability are also already connected in infrastructure research. Mitoulis et al. (2023), for example, formulate transportation-infrastructure recovery using resilience, greenhouse-gas emissions, and cost and explicitly evaluate trade-offs among these outcomes. Thus, the thesis cannot claim that resilience–sustainability integration is absent.

The remaining issue for the present P–T problem is whether interventions that appear similar when viewed only through resilience can differ materially once the **resources consumed and sustainability consequences of obtaining that resilience** are evaluated under a common accounting boundary.

This requires three concepts to remain distinct:

```math
\boxed{
\text{effectiveness}
\neq
\text{efficiency}
\neq
\text{sustainability}.
}
```

An intervention may be effective because it improves recovery, but inefficient because the improvement requires disproportionately large resources. Likewise, an intervention can improve resilience while producing larger energy, carbon, cost, accessibility, or other sustainability burdens.

For candidate actions `a_1` and `a_2`, it is therefore possible that

```math
\mathfrak R^{a_1}
\approx
\mathfrak R^{a_2},
```

while

```math
\mathcal E_{\rm fy}(a_1)
\neq
\mathcal E_{\rm fy}(a_2)
```

or

```math
\mathbf J_{\rm sus}^{a_1}
\neq
\mathbf J_{\rm sus}^{a_2}.
```

The resulting gap is:

```math
\boxed{
G_5:
\quad
\text{resilience improvement alone does not establish}
\quad
\text{efficient or sustainable intervention performance}.
}
```

This gap generates **RQ6, SO6, and H4**. Sustainability dimensions will only be included where their physical mechanism, data, units, system boundary, and accounting assumptions can be defended.

---

## 1.4.6 G6 — From resilience diagnosis to defensible joint engineering decision

The final gap concerns how resilience information affects engineering choice. Multi-objective infrastructure optimization is itself well established, and recent resilience literature increasingly incorporates cost, environmental impacts, reliability, equity, recovery time, or other competing outcomes. Tong et al. (2025) specifically identify the need for more holistic resilience analysis that recognizes trade-offs among objectives, while Mitoulis et al. (2023) provide a concrete example of joint resilience–sustainability–cost evaluation.

The present research question is consequently not whether multi-objective optimization can be performed. It is whether the sustainability and efficiency consequences produced by the **same coupled P–T analysis** materially change the admissible or nondominated infrastructure interventions relative to a resilience-only decision.

Let

```math
\mathcal A_R^\star
```

denote the set selected using resilience-oriented criteria, and let

```math
\mathcal A_{R,S}^\star
```

denote the corresponding admissible or nondominated set when the declared sustainability consequences and feasibility constraints are included. The central question becomes

```math
\boxed{
G_6:
\quad
\mathcal A_R^\star
\overset{?}{=}
\mathcal A_{R,S}^\star.
}
```

If the sets remain equivalent within uncertainty and predefined engineering-materiality thresholds, the additional sustainability formulation has not demonstrated decision value for that regime. Conversely, a material difference would identify conditions under which a resilience-only decision omits consequences relevant to sustainable-engineering design.

This gap generates **RQ7, SO7, and H5**.

---

## 1.4.7 Synthesis of the Research Gap

The six research gaps are not independent deficiencies. They form a sequential scientific argument:

```math
\boxed{
\begin{aligned}
G_1:\;&
\text{Structure}
\rightarrow
\text{evidence-qualified causality},\\[1mm]
G_2:\;&
\text{Causality}
\rightarrow
\text{validated dynamic consequence},\\[1mm]
G_3:\;&
\text{Physical dynamics}
\rightarrow
\text{observation- and organization-constrained action},\\[1mm]
G_4:\;&
\text{Dynamics + feasible action}
\rightarrow
\text{remain / return / confidence},\\[1mm]
G_5:\;&
\text{Resilience diagnosis}
\rightarrow
\text{effectiveness / efficiency / sustainability consequences},\\[1mm]
G_6:\;&
\text{Intervention consequences}
\rightarrow
\text{defensible engineering decision}.
\end{aligned}}
```

The principal research gap can therefore be stated as follows:

> **Existing research provides substantial and increasingly sophisticated solutions for individual components of interdependent-infrastructure resilience, including dependency classification, multilayer modeling, dynamic disturbance propagation, stochastic and adaptive recovery, information and communication coupling, resilience metrics, viability and reachability theory, and resilience–sustainability optimization. Within the bounded Power–Transportation problem considered in this thesis, however, the evidence reviewed to date has not established a sufficiently traceable and comparatively validated chain connecting evidence-qualified directional interdependencies to hybrid physical dynamics; observation-, information-, and organization-constrained feasible actions; service-level maintainability and recovery under uncertainty; intervention effectiveness, efficiency, and sustainability consequences; and the resulting engineering decision.**

This formulation deliberately defines the thesis as an **integration, incremental-value, and validation problem**, rather than claiming novelty for its individual mathematical or engineering ingredients.

Accordingly, the research logic becomes

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

A proposed contribution is supported only if the corresponding comparison demonstrates material incremental value within its declared uncertainty and validity domain. Failure to demonstrate such value must narrow the contribution rather than be interpreted as a failure of the overall research process.

Finally, the gaps established in this section must not be interpreted as proof of global novelty. They represent the bounded conclusions of the current evidence synthesis:

```math
\boxed{
\text{evidence-supported research gap}
\neq
\text{global novelty proof}.
}
```

Any closer prior work identified during the continuing literature and novelty audit must therefore be treated as **counterevidence that narrows the relevant claim**, not excluded because it conflicts with the proposed contribution. This is consistent with the EGMIV-6 rule that claim strength must not exceed evidence strength.

## References cited in Section 1.4

- Béné, C., & Doyen, L. (2018). From resistance to transformation: A generic metric of resilience through viability. *Earth's Future, 6*(7), 979–996. https://doi.org/10.1002/2017EF000660
- Dasuni, K. A. L., Palliyaguru, R., Amaratunga, D., & Liyanawatta, T. N. (2025). Redefining ‘dependencies/interdependencies’ of critical infrastructure: A systematic review of the existing knowledgebase. *Sustainable and Resilient Infrastructure, 10*(2), 202–222. https://doi.org/10.1080/23789689.2024.2403885
- Ghasemkhani, A., Basiri, M. A., & Nicholson, C. (2026). Interdependency and uncertainty in the resiliency of infrastructure networks: A comprehensive review. *International Journal of Critical Infrastructure Protection, 54*, 100866. https://doi.org/10.1016/j.ijcip.2026.100866
- Gim, C., & Miller, C. A. (2022). Institutional interdependence and infrastructure resilience. *Current Opinion in Environmental Sustainability, 57*, 101203. https://doi.org/10.1016/j.cosust.2022.101203
- Lian, X., Song, C., Li, Z., Qiu, L., & Liu, L. (2026). Resilience-oriented emergency resource dispatch for power–transportation coupled networks under rainstorm-induced flood hazards. *Applied Energy, 403*, 127004. https://doi.org/10.1016/j.apenergy.2025.127004
- Mitoulis, S.-A., Bompa, D. V., & Argyroudis, S. (2023). Sustainability and climate resilience metrics and trade-offs in transport infrastructure asset recovery. *Transportation Research Part D: Transport and Environment, 121*, 103800. https://doi.org/10.1016/j.trd.2023.103800
- Moazeni, F., Khazaei, J., & Mitra, P. (2020). An integrated state-estimation framework for interdependent water and energy systems. *Journal of Hydrology, 590*, 125393. https://doi.org/10.1016/j.jhydrol.2020.125393
- Oladigbolu, J., Bakare, M. S., Motlagh, S. G., Mujeeb, A., & Li, L. (2025). A review on transport and power systems planning-operation integrating electric vehicles, energy storage, and other distributed energy resources. *Journal of Energy Storage, 135*, 118419. https://doi.org/10.1016/j.est.2025.118419
- Ouyang, M. (2014). Review on modeling and simulation of interdependent critical infrastructure systems. *Reliability Engineering & System Safety, 121*, 43–60. https://doi.org/10.1016/j.ress.2013.06.040
- Poulin, C., & Kane, M. B. (2021). Infrastructure resilience curves: Performance measures and summary metrics. *Reliability Engineering & System Safety, 216*, 107926. https://doi.org/10.1016/j.ress.2021.107926
- Rinaldi, S. M., Peerenboom, J. P., & Kelly, T. K. (2001). Identifying, understanding, and analyzing critical infrastructure interdependencies. *IEEE Control Systems Magazine, 21*(6), 11–25. https://doi.org/10.1109/37.969131
- Tong, W., Li, H. X., Nasirzadeh, F., Yao, F., & Ji, Y. (2025). Resilience of interdependent infrastructure networks: Review and future directions. *International Journal of Critical Infrastructure Protection, 51*, 100793. https://doi.org/10.1016/j.ijcip.2025.100793
- Trucco, P., & Petrenj, B. (2023). Characterisation of resilience metrics in full-scale applications to interdependent infrastructure systems. *Reliability Engineering & System Safety, 235*, 109200. https://doi.org/10.1016/j.ress.2023.109200
- Wang, S., Lu, Q.-C., Liu, L., Xu, P.-C., Wang, R., & Zhang, L. (2026). Interdependency analysis of coupled power and transportation networks considering the charging decision preferences of EV drivers. *Reliability Engineering & System Safety, 268*, 112005. https://doi.org/10.1016/j.ress.2025.112005
- Wang, Y., Zhao, O., & Zhang, L. (2024). Multiplex networks in resilience modeling of critical infrastructure systems: A systematic review. *Reliability Engineering & System Safety*. https://doi.org/10.1016/j.ress.2024.110300
- Zhang, S., Li, Y., Zhang, H., Dui, H., & Cao, Y. (2026). A two-stage resilience enhancement framework for power distribution system coupled with intelligent transportation system. *Reliability Engineering & System Safety*. https://doi.org/10.1016/j.ress.2026.113032

### Scientific boundary of Section 1.4

Section 1.4 establishes **research needs supported by the present evidence base**. It does **not** establish global novelty.

```math
\boxed{
\text{gap evidence}
\neq
\text{novelty proof}.
}
```

Novelty claims remain conditional on the separate reproducible novelty audit. Any newly identified close predecessor must narrow the relevant gap rather than be excluded.