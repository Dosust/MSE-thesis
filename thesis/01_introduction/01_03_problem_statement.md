## 1.3 Problem Statement

Coupled-infrastructure modeling itself is not absent from the literature. Interdependent infrastructure has been studied using network, simulation, optimization, stochastic, and data-driven approaches, while recent Power–Transportation research includes EV-mediated coupling, transportation-constrained restoration, flood-responsive recovery, emergency-resource coordination, and behavior-dependent charging (Lian et al., 2026; Oladigbolu et al., 2025; Ouyang, 2014; Wang et al., 2026; Wang et al., 2024).

The engineering problem addressed here is instead the reliability of the scientific transitions connecting these components.

A first difficulty is that **structure, causal mechanism, and dynamic effect are not equivalent**. A graph can indicate where interaction is possible without explaining why the receiving system changes state, when the mechanism activates, or how large the resulting effect is. Reviews continue to identify challenges in representing interdependencies, their temporal behavior, uncertainty, and the evidence needed to support coupled-infrastructure inference (Ghasemkhani et al., 2026; Wang et al., 2024).

A second difficulty arises even after a plausible physical mechanism has been identified. Mechanism existence does not establish that its magnitude can be inferred from available observations. The thesis therefore separates three questions:

```math
\boxed{ \text{Does the mechanism exist?} \neq \text{Can its magnitude be identified?} \neq \text{Can the magnitude be estimated adequately?} }
```

Measurement, identification, estimation, and simulation are therefore different scientific tasks. This distinction prevents a numerical coefficient obtained from a computational model from being interpreted automatically as evidence that the underlying physical mechanism has been identified.

A third difficulty is that physical state does not determine feasible response. Infrastructure operators act using imperfect observations, estimated states, information availability, authority, coordination, personnel, and available resources. Human and institutional conditions can therefore alter infrastructure response even when the underlying physical disturbance is similar (Chester et al., 2021; Rasoulkhani & Mostafavi, 2018).

A fourth difficulty concerns resilience itself. Performance and recovery curves are useful for characterizing infrastructure degradation and restoration, but different performance measures and summary metrics capture different properties of the disruption–recovery process (Poulin & Kane, 2021; Trucco & Petrenj, 2023). The question considered in this thesis is therefore not only how service changes through time, but whether required electricity and mobility services can remain acceptable, whether acceptable service can be recovered after violation, and with what confidence those statements can be made under uncertainty.

A final difficulty appears when resilience analysis is translated into intervention. Power–Transportation studies already consider hardening, charging coordination, mobile resources, repair routing, switching, and coordinated recovery (Lian et al., 2026; Oladigbolu et al., 2025). The remaining engineering issue is whether interventions that appear beneficial from a resilience perspective remain equivalent when their resource requirements, efficiency, environmental consequences, feasibility, and uncertainty are considered.

The problem is therefore end-to-end:

```math
\boxed{ \begin{aligned} \text{service requirements} &\rightarrow \text{spatiotemporal P--T System-of-Systems structure} \rightarrow \text{qualified directional dependencies}\\ &\rightarrow \text{complex spatiotemporal coupled dynamics} \rightarrow \text{observation, organization and feasible action}\\ &\rightarrow \text{spatiotemporal remain / recover / confidence} \rightarrow \text{intervention consequences} \rightarrow \text{engineering decision}. \end{aligned} }
```

The research problem is to make each transition scientifically traceable so that the strength of the final engineering conclusion does not exceed the evidence supporting the intermediate steps.

---

