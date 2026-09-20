## 1.3 Problem Statement

Coupled-infrastructure modeling is not absent from the literature. Interdependent infrastructure has been studied through network, simulation, optimization, stochastic, and data-driven methods. Recent Power–Transportation studies include charging-mediated coupling, transportation-constrained restoration, flood-responsive recovery, emergency-resource coordination, and behavior-dependent charging (Lian et al., 2026; Oladigbolu et al., 2025; Ouyang, 2014; Wang et al., 2024; Wang et al., 2026).

The engineering problem addressed by this thesis is instead the **reliability of the scientific transitions connecting these capabilities**.

First, **structure does not establish a qualified directional dependency**. A graph can show where interaction is possible without explaining why the receiver changes state, when the mechanism activates, or whether the resulting effect is large enough to matter. Recent review evidence continues to identify challenges associated with representing infrastructure interdependencies and uncertainty and with connecting these representations to resilience assessment (Ghasemkhani et al., 2026; Wang et al., 2024).

Second, **mechanism existence does not establish numerical identifiability**. Even where a physical mechanism is plausible, its magnitude may not be uniquely inferable from available observations. The thesis therefore distinguishes:

```math
\boxed{ \text{Does the mechanism exist?} \neq \text{Can its magnitude be identified?} \neq \text{Can its magnitude be estimated adequately?} }
```

Measurement, identification, estimation, simulation, and validation consequently perform different scientific functions. A numerical coefficient produced by a model is not, by itself, evidence that the corresponding real-system dependency has been identified.

Third, **physical possibility does not establish feasible action**. Operators respond through observations, estimated states, information availability, communication, authority, coordination, personnel, and resources. Information and organizational conditions can therefore alter response and recovery even when the physical disturbance is held constant (Chester et al., 2021; Rasoulkhani & Mostafavi, 2018).

Fourth, **a realized service trajectory does not completely characterize resilience**. Performance and recovery curves provide important information about degradation and restoration, but their interpretation depends on the selected service variable, reference state, threshold, horizon, and summary metric (Poulin & Kane, 2021; Trucco & Petrenj, 2023). A different engineering question is whether required service can remain within acceptable conditions and, after violation, whether acceptable service can be recovered under feasible actions and uncertainty.

Finally, **resilience improvement does not by itself determine an engineering decision**. Candidate interventions can produce similar resilience effects while requiring different direct intervention or recovery costs and operational energy, and while producing different admitted carbon-dioxide-equivalent consequences within the declared accounting boundary. Additional resource or distributional quantities are included only where independently qualified. Infrastructure studies already demonstrate trade-offs among resilience, recovery, cost, and greenhouse-gas consequences (Mitoulis et al., 2023; Sun et al., 2025; Zou & Chen, 2019).

The research problem is therefore end-to-end:

```math
\boxed{ \begin{aligned} \text{service requirements} &\rightarrow \text{spatiotemporal P--T structure}\\ &\rightarrow \text{qualified directional dependencies}\\ &\rightarrow \text{complex spatiotemporal coupled dynamics}\\ &\rightarrow \text{observation, organization, and feasible action}\\ &\rightarrow \text{service resilience under uncertainty}\\ &\rightarrow \text{intervention consequences}\\ &\rightarrow \text{engineering decision}. \end{aligned}}
```

The scientific requirement is to make every transition traceable so that the strength of the final engineering conclusion does not exceed the evidence supporting the intermediate steps.
