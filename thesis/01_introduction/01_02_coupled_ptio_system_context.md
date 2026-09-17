# 1.2 Coupled Power–Transportation–Information–Organization System Context

The engineering context established in Section 1.1 motivates a more precise definition of the system studied in this thesis. The research does not treat all critical infrastructures as a single undifferentiated network. Instead, it focuses on a bounded coupled system whose **physical infrastructure core** consists of electric power and transportation, while information and organizational capabilities are represented explicitly because they influence what is known about the physical system and what actions can be implemented during disruption and recovery. The study context is denoted conceptually as

```math
\boxed{\mathcal S=\{P,T,I,O\}},
```

where

```math
P=\text{Power},\qquad
T=\text{Transportation},\qquad
I=\text{Information},\qquad
O=\text{Organization}.
```

This notation does **not** imply that the four domains are physically equivalent infrastructure networks. In this thesis, `P` and `T` are the two principal physical infrastructure systems, whereas `I` and `O` are supporting domains through which conditions are observed, interpreted, communicated, coordinated, and acted upon. The notation is retained for consistency with the canonical Chapter-I architecture; its typed meaning is defined explicitly in the prose. Multilayer-network theory provides a general framework for systems containing multiple subsystems and relationship types, but the existence of a layer or interlayer edge is a structural representation rather than evidence of a causal mechanism (Kivelä et al., 2014).

The **Power domain `P`** contains the relevant physical assets and electrical relationships required to deliver electricity to loads within the study boundary. At the structural level it may be represented as

```math
\mathcal G_P=(V_P,E_P),
```

where `V_P` denotes relevant buses or assets and `E_P` denotes electrical connections. The **Transportation domain `T`** contains the physical mobility network through which travelers, repair crews, emergency resources, and other relevant flows move, represented structurally as

```math
\mathcal G_T=(V_T,E_T),
```

where `V_T` contains transportation nodes and `E_T` admissible road links or other physical connections. These graphs define structure only; they do not by themselves specify electrical physics, traffic dynamics, failure propagation, or recovery behavior.

The physical coupling between `P` and `T` is represented through **directional dependency mechanisms**. In the power-to-transportation direction,

```math
\boxed{P\rightarrow T},
```

electricity can support traffic-control devices, charging infrastructure, and other electrically dependent transportation assets. Coupled traffic–power studies and reviews of transportation electrification model relationships among charging demand, road-network behavior, and distribution-system constraints (Fotouhi et al., 2017; Wei et al., 2019; Unterluggauer et al., 2022).

The transportation-to-power direction is physically distinct:

```math
\boxed{T\rightarrow P}.
```

Here, transportation conditions can influence activities required for power-system operation or restoration. An important example is **physical accessibility**: damaged roads, congestion, or unavailable routes can change when repair crews or mobile emergency resources reach failed electrical assets. Fan et al. (2024) explicitly couple road states to repair-crew routing in coordinated post-disaster restoration.

These two directions are not collapsed into a generic `P↔T` edge. A **directional dependency mechanism** is accepted only when its source, receiver, mechanism, component mapping, evidence basis, activation conditions, and validity domain can be identified. A reciprocal **interdependency** is then a system-level condition in which the relevant directional dependencies coexist and can interact. Accordingly,

```math
\boxed{
\text{candidate structural relation}
\neq
\text{accepted causal dependency mechanism}.
}
```

The **Information domain `I`** represents what is available for estimating and interpreting the condition of the physical system rather than another physical infrastructure by default. Depending on the experiment, this may include measurements, sensor availability, communication status, delays, missing observations, and state-estimation outputs. Power-grid, ICT, and e-mobility interactions can create additional operational dependencies (Mohamed, 2019), but an ICT network is modeled as a separate physical infrastructure layer only when its components and connectivity are required by the research question.

The **Organizational domain `O`** represents the human and institutional capabilities through which information is converted into action. Relevant properties can include authority, coordination arrangements, repair priorities, personnel and equipment availability, resource allocation, procedures, and response delays. Infrastructure-resilience research shows that adaptive capacity is shaped not only by physical assets but also by institutions, governance, and human–infrastructure interactions (Rasoulkhani & Mostafavi, 2018; Chester et al., 2021; Helmrich et al., 2021).

The four-domain representation therefore separates engineering functions that would otherwise be hidden inside a single coupled-network model. The observation–decision–action loop is represented schematically as

```math
\boxed{
(P,T)
\xrightarrow{\text{observation}}
I
\xrightarrow{\text{interpretation / decision}}
O
\xrightarrow{\text{authorized action}}
(P,T).
}
```

This is an **observation–decision–action abstraction**, not an assertion that `I` and `O` are physical infrastructure networks. Observation is not control; information is not authority; authority is not physical capability; and the existence of a communication path does not guarantee that an intervention can be executed. Hence,

```math
\boxed{
\text{physical topology}
\neq
\text{dependency mechanism}
\neq
\text{observation}
\neq
\text{decision}
\neq
\text{control action}.
}
```

A common external hazard is also not automatically a dependency. If a flood simultaneously damages a power asset and a road segment, the two components share exposure without either necessarily causing the other's state change. Only an identifiable cross-system mechanism—such as loss of electricity disabling a transportation asset or loss of road accessibility delaying electrical repair—is represented as a directional dependency.

The study is **service-oriented rather than purely topological**. The physical systems matter because they provide critical services: `P` supports electricity delivery and `T` supports mobility and accessibility. A component or interface is therefore not important solely because it has high graph-theoretic centrality; its engineering significance ultimately depends on its effect on service trajectories, feasible response, and recovery.

Coupled Power–Transportation modeling is already an established research area. Prior work has quantified resilience in traffic–electric-power systems, reviewed joint transportation–distribution-system models, examined EV charging as an explicit coupling mechanism, and represented transportation accessibility in post-disaster restoration (Fotouhi et al., 2017; Wei et al., 2019; Unterluggauer et al., 2022; Fan et al., 2024). The premise of this thesis is therefore not that P–T systems have never been modeled jointly. Instead, the thesis begins from an evidence-qualified `P–T` physical core and makes `I` and `O` explicit so that subsequent analysis can distinguish **what exists, why a dependency operates, how it evolves, what can be observed, and what actions are physically and organizationally feasible**.

Section 1.3 therefore moves from **what constitutes the study system** to the engineering problem created by the need to connect structure, causal mechanisms, dynamic propagation, observation, feasible action, and service recovery without treating these distinct concepts as interchangeable.

## References cited in Section 1.2

- Chester, M., Underwood, B. S., Allenby, B., Garcia, M., Samaras, C., Markolf, S., Sanders, K., Preston, B., & Miller, T. R. (2021). Infrastructure resilience to navigate increasingly uncertain and complex conditions in the Anthropocene. *npj Urban Sustainability, 1*, Article 4. https://doi.org/10.1038/s42949-021-00016-y
- Fan, J., He, P., Li, C., Zhao, C., & Ji, Y. (2024). A post-disaster restoration model for power-gas-transportation distribution networks considering spatial interdependency and energy hubs. *Electric Power Systems Research, 233*, 110505. https://doi.org/10.1016/j.epsr.2024.110505
- Fotouhi, H., Moryadee, S., & Miller-Hooks, E. (2017). Quantifying the resilience of an urban traffic-electric power coupled system. *Reliability Engineering & System Safety, 163*, 79–94. https://doi.org/10.1016/j.ress.2017.01.026
- Helmrich, A., Markolf, S., Li, R., Carvalhaes, T., Kim, Y., Bondank, E., Natarajan, M., Ahmad, N., & Chester, M. (2021). Centralization and decentralization for resilient infrastructure and complexity. *Environmental Research: Infrastructure and Sustainability, 1*(2), 021001. https://doi.org/10.1088/2634-4505/ac0a4f
- Kivelä, M., Arenas, A., Barthelemy, M., Gleeson, J. P., Moreno, Y., & Porter, M. A. (2014). Multilayer networks. *Journal of Complex Networks, 2*(3), 203–271. https://doi.org/10.1093/comnet/cnu016
- Mohamed, A. A. A. (2019). On the rising interdependency between the power grid, ICT network, and e-mobility: Modeling and analysis. *Energies, 12*(10), 1874. https://doi.org/10.3390/en12101874
- Rasoulkhani, K., & Mostafavi, A. (2018). Resilience as an emergent property of human-infrastructure dynamics: A multi-agent simulation model for characterizing regime shifts and tipping point behaviors in infrastructure systems. *PLOS ONE, 13*(11), e0207674. https://doi.org/10.1371/journal.pone.0207674
- Rinaldi, S. M., Peerenboom, J. P., & Kelly, T. K. (2001). Identifying, understanding, and analyzing critical infrastructure interdependencies. *IEEE Control Systems Magazine, 21*(6), 11–25. https://doi.org/10.1109/37.969131
- Unterluggauer, T., Rich, J., Andersen, P. B., & Hashemi, S. (2022). Electric vehicle charging infrastructure planning for integrated transportation and power distribution networks: A review. *eTransportation, 12*, 100163. https://doi.org/10.1016/j.etran.2022.100163
- Wei, W., Wu, D., Wu, Q., Shafie-khah, M., & Catalão, J. P. S. (2019). Interdependence between transportation system and power distribution system: A comprehensive review on models and applications. *Journal of Modern Power Systems and Clean Energy, 7*, 433–448. https://doi.org/10.1007/s40565-019-0516-7

## Scientific boundary of Section 1.2

This section establishes only the system boundary, domain roles, directional relations, service meaning, and causal safeguards. It does **not** claim a literature gap, global novelty, model superiority, or validated benefit of the `P–T–I–O` representation.