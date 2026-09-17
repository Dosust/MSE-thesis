# 1.3 Problem Statement

The `P–T–I–O` system defined in Section 1.2 presents an engineering problem that extends beyond identifying whether infrastructure systems are interconnected. Power–Transportation coupling, multilayer infrastructure representations, cascading-failure analysis, transportation-constrained power restoration, electric-vehicle interactions, stochastic recovery optimization, and cyber-physical coupling are already established areas of research (Ouyang, 2014; Wang et al., 2024; Oladigbolu et al., 2025). Recent studies have further demonstrated dynamic flood-responsive Power–Transportation restoration, behavioral charging interdependencies, and multi-stage resilience enhancement (Lian et al., 2026; Wang et al., 2026). Consequently, the scientific problem addressed by this thesis is **not the absence of coupled-infrastructure models**, but the need to establish a traceable engineering connection between **evidence-supported interdependency mechanisms, time-dependent physical behavior, feasible system response, service-level resilience, uncertainty, and infrastructure decision-making**.

A first difficulty is that **structural interconnection and causal interdependency are different scientific objects**. Multilayer and network-of-networks representations can identify components and potential cross-system relations, but an interlayer edge does not by itself establish why a receiving component changes state, under what conditions the relationship becomes active, how large its effect is, or how long propagation takes. Recent systematic reviews continue to identify limitations associated with interdependency representation, dynamic processes, high-resolution observations, and uncertainty in critical-infrastructure resilience models (Wang et al., 2024; Ghasemkhani et al., 2026). The engineering requirement is therefore to move from a candidate structural relation to an evidence-qualified mechanism with explicit source, receiver, activation condition, temporal behavior, and validity domain.

A second difficulty concerns the transition from **causal mechanism to dynamic system behavior**. Coupled infrastructure failures and recovery occur across heterogeneous spatial and temporal scales. Electrical states may respond rapidly, traffic conditions evolve over different operational horizons, physical damage persists until repair, and accessibility or resource constraints may change during restoration. Recent P–T studies demonstrate that these dynamics can be modeled—for example through flood-responsive traffic models, stochastic failure chains, multi-stage restoration, and adaptive resource dispatch—but they also show that conclusions depend strongly on how cross-system dynamics, hazard scenarios, resource availability, and behavioral assumptions are represented (Lian et al., 2026; Wang et al., 2026). Hence, the problem is not merely to introduce time dependence, but to determine whether the assumed interdependency dynamics are sufficiently grounded to support the resulting resilience conclusions.

A third difficulty is that **physical state does not uniquely determine feasible response**. Infrastructure operators act through imperfect measurements, communication systems, estimation processes, organizational structures, resource limitations, and decision authority. Infrastructure-resilience research increasingly recognizes that engineered assets, institutions, human actors, and information processes jointly shape response and adaptation (Rasoulkhani & Mostafavi, 2018; Chester et al., 2021). Cyber-physical-social reviews likewise argue that organizational characteristics and domain-specific knowledge need to be integrated with physical infrastructure analysis when resilience strategies are designed (Dong et al., 2020). Therefore, two identical physical disruption states may admit different responses if sensing quality, information availability, authority, coordination, personnel, or resources differ.

For this reason, the thesis must preserve the distinction

```math
\boxed{
\text{Structure}
\neq
\text{Causality}
\neq
\text{Dynamics}
\neq
\text{Observation}
\neq
\text{Organization}
\neq
\text{Control}.
}
```

These quantities interact, but none can be substituted for another. In systems-engineering terms, an interface must be identified, defined, and controlled with sufficient precision that its consequences for the system can be traced; otherwise, the existence of an interface alone provides insufficient basis for engineering decision-making (INCOSE, 2018).

A fourth difficulty concerns **what is meant by resilience once dynamic interdependencies and feasible actions are represented**. Conventional resilience curves and summary indices provide useful descriptions of degradation and recovery, but the metric literature shows that different measures emphasize different system properties, depend on selected performance targets, and can produce different interpretations (Poulin & Kane, 2021; Trucco & Petrenj, 2023). A single aggregate performance value therefore does not necessarily answer whether critical electricity and mobility services remain above required operating levels, whether recovery to an acceptable state is dynamically feasible, how long that recovery requires, or how uncertain those conclusions are.

The engineering resilience problem in this thesis is consequently formulated around three related but distinct questions:

```math
\boxed{
\begin{aligned}
\textbf{Remain:}\quad
&\text{Can required services remain within acceptable conditions?}\\[2mm]
\textbf{Return:}\quad
&\text{If acceptable conditions are lost, can they be recovered}\\
&\text{within an admissible time horizon?}\\[2mm]
\textbf{Confidence:}\quad
&\text{How strongly can either conclusion be supported under uncertainty?}
\end{aligned}}
```

This formulation does not replace conventional resilience curves; rather, it creates a basis for testing whether viability, recovery reachability, and probabilistic confidence provide **incremental engineering information** beyond conventional performance-based assessment. Whether that additional information is materially useful is a hypothesis to be tested, not assumed.

A fifth difficulty arises when resilience analysis must support an actual infrastructure intervention. Current P–T research already evaluates line hardening, mobile energy storage, EV/V2G resources, repair routing, charging strategies, network switching, and coordinated pre- and post-disaster actions (Lian et al., 2026; Oladigbolu et al., 2025). The remaining engineering requirement for this thesis is therefore not simply to identify an intervention that increases a resilience index, but to distinguish its **effectiveness**, its **resource efficiency**, and its **sustainability consequences** under the same physical scenarios and uncertainty assumptions. Recent reviews explicitly call for more deployable, feasibility-preserving and benchmarked coupled P–T methods, including open datasets, real-world validation, communications-aware recovery, and consideration of economic and operational constraints (Oladigbolu et al., 2025).

The problem is also one of **verification and evidence sufficiency**. General reviews of interdependent infrastructure continue to identify limited data, simplified assumptions, incomplete uncertainty treatment, and practical-validation difficulties as constraints on resilience assessment (Wang et al., 2024; Ghasemkhani et al., 2026). The present thesis must therefore distinguish between a relation proposed because it is plausible, a relation supported by external evidence, a model verified to implement its mathematics correctly, a model calibrated or validated against observations, and a conclusion supported only within the scenarios and uncertainty ranges actually tested.

Accordingly, the core engineering problem is expressed as the following traceability chain:

```math
\boxed{
\begin{aligned}
\text{Service requirements}
&\rightarrow
\text{physical P--T structure}\\
&\rightarrow
\text{evidence-qualified interdependencies}\\
&\rightarrow
\text{hybrid multiscale dynamics}\\
&\rightarrow
\text{observation, organization and feasible control}\\
&\rightarrow
\text{viability, recovery reachability and confidence}\\
&\rightarrow
\text{intervention consequences}\\
&\rightarrow
\text{engineering decision}.
\end{aligned}}
```

The fundamental problem is that each arrow represents a distinct inferential or engineering step. A structural edge cannot be assumed to be a causal mechanism; a causal mechanism cannot be assumed to determine a trajectory without dynamics; a simulated trajectory does not establish feasible recovery without control and resource constraints; a resilience metric does not alone establish service admissibility; and a resilience improvement does not automatically establish that an intervention is efficient or sustainable.

The **problem statement of this thesis** can therefore be stated formally as follows:

> **The engineering problem is to construct and validate an evidence-grounded representation of coupled Power–Transportation infrastructure in which directional interdependency mechanisms are translated into time-, state-, and mode-dependent physical behavior; incomplete information and organizational conditions explicitly constrain feasible response; resilience is evaluated in terms of maintaining and recovering required services under uncertainty; and the resulting information is shown, through matched comparisons and verification/validation, to support defensible intervention and sustainability decisions.**

The literature already solves important subsets of this problem. The thesis must therefore demonstrate **incremental scientific and engineering value over appropriate existing baselines**, rather than claiming novelty from the mere combination of Power, Transportation, Information, Organization, dynamics, recovery, or resilience. The next section consequently asks a more restrictive question: **which links in this complete engineering chain remain insufficiently integrated or validated in the existing evidence base?** That question defines **Section 1.4 — Research Gap**.

## References cited in Section 1.3

- Chester, M., Underwood, B. S., Allenby, B., Garcia, M., Samaras, C., Markolf, S., Sanders, K., Preston, B., & Miller, T. R. (2021). Infrastructure resilience to navigate increasingly uncertain and complex conditions in the Anthropocene. *npj Urban Sustainability, 1*, 4. https://doi.org/10.1038/s42949-021-00016-y
- Dong, S., Mostafavi, A., Wang, H., Gao, J., & Li, X. (2020). Measuring the resilience of cyber-physical systems and communities: A review of the literature. *Journal/venue to be verified before final thesis formatting.*
- Ghasemkhani, A., Basiri, M. A., & Nicholson, C. (2026). Interdependency and uncertainty in the resiliency of infrastructure networks: A comprehensive review. *International Journal of Critical Infrastructure Protection, 54*, 100866. https://doi.org/10.1016/j.ijcip.2026.100866
- Hoff, R. M., & Chester, M. V. (2023). Preparing infrastructure for surprise: Fusing synthetic network, interdependency, and cascading failure models. *Environmental Research: Infrastructure and Sustainability, 3*(2), 025009. https://doi.org/10.1088/2634-4505/acd07d
- INCOSE. (2018). *Systems Engineering Competency Framework*. INCOSE-TP-2018-002-01.0.
- Lian, X., Song, C., Li, Z., Qiu, L., & Liu, L. (2026). Resilience-oriented emergency resource dispatch for power–transportation coupled networks under rainstorm-induced flood hazards. *Applied Energy, 403*, 127004. https://doi.org/10.1016/j.apenergy.2025.127004
- Oladigbolu, J., Bakare, M. S., Motlagh, S. G., Mujeeb, A., & Li, L. (2025). A review on transport and power systems planning-operation integrating electric vehicles, energy storage, and other distributed energy resources. *Journal of Energy Storage, 135*, 118419. https://doi.org/10.1016/j.est.2025.118419
- Ouyang, M. (2014). Review on modeling and simulation of interdependent critical infrastructure systems. *Reliability Engineering & System Safety, 121*, 43–60. https://doi.org/10.1016/j.ress.2013.06.040
- Poulin, C., & Kane, M. B. (2021). Infrastructure resilience curves: Performance measures and summary metrics. *Reliability Engineering & System Safety, 216*, 107926. https://doi.org/10.1016/j.ress.2021.107926
- Rasoulkhani, K., & Mostafavi, A. (2018). Resilience as an emergent property of human-infrastructure dynamics. *PLOS ONE, 13*(11), e0207674. https://doi.org/10.1371/journal.pone.0207674
- Trucco, P., & Petrenj, B. (2023). Characterisation of resilience metrics in full-scale applications to interdependent infrastructure systems. *Reliability Engineering & System Safety, 235*, 109200. https://doi.org/10.1016/j.ress.2023.109200
- Wang, Y., Zhao, O., & Zhang, L. (2024). Multiplex networks in resilience modeling of critical infrastructure systems: A systematic review. *Reliability Engineering & System Safety*. Article details to be bibliographically verified before final thesis formatting.
- Wang, S., Lu, Q.-C., Liu, L., Xu, P.-C., Wang, R., & Zhang, L. (2026). Interdependency analysis of coupled power and transportation networks considering the charging decision preferences of EV drivers. *Reliability Engineering & System Safety, 268*, 112005. https://doi.org/10.1016/j.ress.2025.112005

## Scientific boundary of Section 1.3

This section establishes the **engineering problem**, not the final research-gap or novelty claim. Specifically:

```math
\boxed{
\text{engineering problem}
=
\text{traceability from interdependency evidence to validated decisions}.
}
```

The section intentionally does **not** claim that coupled P–T modeling, dynamic recovery, communication coupling, organizational effects, viability theory, or sustainability analysis are individually novel. The specific literature-supported gaps that justify the thesis questions are reserved for Section 1.4 and must remain bounded by the completed evidence and novelty audits.
