# 1.5 Sustainable Engineering Significance

The significance of this research to Sustainable Engineering lies not in treating resilience and sustainability as interchangeable objectives, but in determining how engineering actions that preserve or restore critical infrastructure services also affect the resources consumed and consequences generated in achieving those outcomes. Power and Transportation systems provide distinct but increasingly coupled services, and disruption in one system can alter the performance and recovery conditions of the other. Infrastructure-resilience research therefore increasingly requires analysis that extends beyond isolated asset robustness toward coupled service performance, uncertainty, adaptation, and decision-making across interacting technical and institutional systems (Chester et al., 2021).

For this thesis, the central Sustainable Engineering distinction is

```math
\boxed{
\text{effectiveness}
\neq
\text{efficiency}
\neq
\text{sustainability}.
}
```

**Effectiveness** asks whether an intervention produces the intended engineering outcome—for example, whether it increases the ability to maintain electricity and mobility services or reduces recovery time. **Efficiency** asks what resources are required to obtain that improvement, such as direct expenditure, operational energy, labor, or emergency-resource capacity. **Sustainability** asks whether additional environmental, economic, or distributional consequences arise within a declared accounting boundary. This separation is necessary because an intervention may improve resilience while simultaneously requiring greater energy, expenditure, materials, or emissions. Conversely, an intervention with lower resource use or emissions may provide insufficient service protection. Existing P–T studies already demonstrate the relevance of such trade-offs: resilience-oriented traffic–power models have incorporated budget and repair-resource constraints, while more recent coupled transportation–power planning explicitly considers resilience, investment, operating costs, and carbon emissions (Zou & Chen, 2019; Sun et al., 2025).

Accordingly, the thesis does not define sustainability through a single composite score. Candidate engineering interventions `a_k` are instead evaluated through a typed consequence structure:

```math
\boxed{
\mathcal C(a_k)
=
\left(
\Delta\mathfrak R^{a_k},
\mathbf r^{a_k},
\Delta\mathbf J_{\mathrm{sus}}^{a_k},
\mathcal F^{a_k},
\mathbf U^{a_k}
\right),
}
```

where `\Delta\mathfrak R^{a_k}` represents the change in resilience relative to a declared reference intervention, `\mathbf r^{a_k}` represents resource requirements, `\Delta\mathbf J_{\mathrm{sus}}^{a_k}` represents admitted sustainability consequences, `\mathcal F^{a_k}` represents feasibility constraints, and `\mathbf U^{a_k}` represents uncertainty. Under the present thesis governance, direct intervention or recovery cost, operational energy use, and carbon/GHG consequence constitute the principal quantitative candidates; crew/person-hours and distributional accessibility remain conditional extensions whose use depends on case-specific data and construct validity. Comprehensive life-cycle assessment and unrelated environmental or socioeconomic indicators are not assumed to belong to the core analysis merely because they are generally associated with sustainability.

A second aspect of the significance is the explicit separation of **service performance** from sustainability consequence. Electricity served, mobility provided, unmet trips, aggregate transport accessibility, and recovery time are primarily resilience and service quantities in this framework; they define what the coupled system is required to maintain or recover. They are not automatically relabeled as sustainability outcomes. This distinction is important because resilience metrics already summarize multiple aspects of disruption and recovery, and their interpretation depends strongly on the chosen performance variable, threshold, time horizon, and aggregation procedure (Poulin & Kane, 2021). Treating the same service loss once as a resilience outcome and again as an independent sustainability variable would risk double counting rather than provide additional engineering information.

The Sustainable Engineering value of the proposed framework therefore emerges at the **intervention-comparison level**. Candidate actions will be examined under common disturbance conditions and consistent system boundaries so that changes in resilience can be interpreted together with the resources and consequences required to obtain them. This approach is consistent with prior infrastructure work showing that resilience, cost, and greenhouse-gas outcomes can generate meaningful trade-offs during infrastructure recovery and adaptation (Mitoulis et al., 2023). The thesis extends this reasoning to the coupled P–T problem by asking whether two interventions that produce similar service-resilience outcomes remain equivalent after operational energy, direct cost, carbon, feasibility, and uncertainty are considered.

This distinction becomes especially important for engineering decision-making. The thesis does not assume that adding sustainability information will alter the preferred intervention. Instead, it tests whether the resilience-oriented admissible or nondominated intervention set,

```math
\mathcal A_R^\star,
```

differs materially from the corresponding set obtained when admitted sustainability consequences, resource requirements, feasibility, and uncertainty are included,

```math
\mathcal A_{R,S}^\star.
```

If the two sets remain equivalent within the declared uncertainty and materiality criteria, then the additional sustainability information has not demonstrated decision value for that regime. If they differ, the analysis identifies which resource requirement or sustainability consequence changes the engineering decision. This makes sustainability an experimentally testable part of infrastructure decision support rather than an assumed qualitative benefit.

The Sustainable Engineering contribution of the thesis is therefore deliberately bounded. It does not claim to provide a complete assessment of environmental, social, and economic sustainability, nor does it assume that a more resilient P–T system is necessarily a more sustainable one. Its significance is to establish a traceable path from **critical-service resilience diagnosis to intervention consequence and engineering decision**, while preserving explicit resource, carbon, cost, feasibility, and uncertainty boundaries. In this sense, the research addresses a central engineering question: not only **whether coupled infrastructure can remain operational or recover**, but also **what must be consumed, changed, or traded off to obtain that resilience, and whether those consequences materially alter the infrastructure transformation that should be considered**. This provides the conceptual bridge from the research gaps identified in Section 1.4 to the formal system boundaries, assumptions, inclusions, and exclusions specified in Section 1.6.

## References cited in Section 1.5

- Chester, M., Underwood, B. S., Allenby, B., Garcia, M., Samaras, C., Markolf, S., Sanders, K., Preston, B., & Miller, T. R. (2021). Infrastructure resilience to navigate increasingly uncertain and complex conditions in the Anthropocene. *npj Urban Sustainability, 1*, Article 4. https://doi.org/10.1038/s42949-021-00016-y
- Mitoulis, S.-A., Bompa, D. V., & Argyroudis, S. (2023). Sustainability and climate resilience metrics and trade-offs in transport infrastructure asset recovery. *Transportation Research Part D: Transport and Environment, 121*, 103800. https://doi.org/10.1016/j.trd.2023.103800
- Poulin, C., & Kane, M. B. (2021). Infrastructure resilience curves: Performance measures and summary metrics. *Reliability Engineering & System Safety, 216*, 107926. https://doi.org/10.1016/j.ress.2021.107926
- Sun, Y., Huang, X., Wang, G., Zhang, X., Qiu, J., & Strbac, G. (2025). Low-carbon traffic resilience-enhanced robust planning of coupled transportation and power distribution network based on modified user equilibrium model. *Applied Energy, 397*, 126258. https://doi.org/10.1016/j.apenergy.2025.126258
- Zou, Q., & Chen, S. (2019). Enhancing resilience of interdependent traffic-electric power system. *Reliability Engineering & System Safety, 191*, 106557. https://doi.org/10.1016/j.ress.2019.106557
