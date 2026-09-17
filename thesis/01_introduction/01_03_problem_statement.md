# 1.3 Problem Statement

The `P–T–I–O` system defined in Section 1.2 presents an engineering problem that extends beyond identifying whether infrastructure systems are connected. Power–Transportation coupling, multilayer infrastructure representation, cascading-failure analysis, transportation-constrained restoration, electric-vehicle interactions, stochastic recovery optimization, and cyber-physical coupling are already established areas of research (Ouyang, 2014; Wang et al., 2024; Oladigbolu et al., 2025). Recent studies further demonstrate flood-responsive P–T restoration, behavior-dependent charging interactions, and multi-stage resilience enhancement (Lian et al., 2026; Wang et al., 2026). The scientific problem addressed by this thesis is therefore **not the absence of coupled-infrastructure models**, but the need to establish a traceable engineering connection between evidence-supported directional dependency mechanisms, time-dependent physical behavior, feasible response, service-level resilience, uncertainty, and infrastructure decision-making.

A first difficulty is that **structure, causal dependency, and dynamics are different scientific objects**. A multilayer representation can identify components and candidate cross-system relations, but an interlayer edge does not by itself establish why a receiver changes state, under what conditions the effect becomes active, how large the effect is, or how it evolves through time. Reviews of interdependent-infrastructure resilience continue to identify limitations associated with interdependency representation, performance evolution, high-resolution observations, and uncertainty (Wang et al., 2024; Ghasemkhani et al., 2026). The engineering requirement is therefore to move from a candidate structural relation to an evidence-qualified directional dependency mechanism and then to a physical dynamic representation whose assumptions and validity domain are explicit.

This requirement follows an explicit systems-thinking progression from visible symptoms toward generative structure and mechanism:

```math
\boxed{
\begin{aligned}
\text{Observed event}
&\rightarrow
\text{recurrent spatiotemporal pattern}\\
&\rightarrow
\text{underlying SoS structure}\\
&\rightarrow
\text{causal dependency mechanism}\\
&\rightarrow
\text{dynamic consequence}\\
&\rightarrow
\text{feasible engineering action}.
\end{aligned}
}
```

This progression prevents observable consequences—such as outages, congestion, or delayed recovery—from being mistaken for their underlying causes and provides the reasoning bridge from System-of-Systems architecture to complex-system dynamics.

A second difficulty is that **physical state does not uniquely determine feasible response**. Infrastructure operators act through measurements, state estimates, information availability, organizational authority, coordination, personnel, equipment, and other resource constraints. Infrastructure-resilience research increasingly recognizes that engineered assets, institutions, and human actors jointly shape response and adaptation (Rasoulkhani & Mostafavi, 2018; Chester et al., 2021). Consequently, two physically similar disruption states may admit different responses if what can be observed, authorized, coordinated, or executed differs. The thesis therefore preserves the distinction

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

A third difficulty concerns the meaning of resilience once dynamic dependencies and feasible actions are represented. Conventional resilience curves and summary metrics provide useful descriptions of degradation and recovery, but different measures capture different system properties and can produce different interpretations (Poulin & Kane, 2021; Trucco & Petrenj, 2023). The engineering question considered here is therefore not only how much performance is lost, but whether critical electricity and mobility services can **remain** within acceptable limits, whether acceptable operation can **return** after those limits are violated, and how strongly either conclusion can be supported under uncertainty. These requirements motivate the later viability, recovery-reachability, and confidence/probability components of the thesis without assuming in advance that they outperform conventional resilience assessment.

Finally, resilience diagnosis must support an engineering intervention. Existing P–T research already evaluates hardening, mobile energy resources, EV/V2G strategies, repair routing, charging control, switching, and coordinated recovery (Oladigbolu et al., 2025; Lian et al., 2026). The remaining engineering requirement is therefore not simply to find an action that improves a resilience metric, but to determine whether candidate actions differ in **effectiveness, resource efficiency, and sustainability consequences** under matched physical scenarios and uncertainty assumptions. Any claimed benefit must also remain bounded by model verification, available validation evidence, sensitivity, and uncertainty.

Accordingly, the core problem of this thesis is the traceability of the full engineering chain

```math
\boxed{
\begin{aligned}
\text{Service requirements}
&\rightarrow
\text{physical P--T structure}
\rightarrow
\text{evidence-qualified dependency mechanisms}\\
&\rightarrow
\text{hybrid multiscale dynamics}
\rightarrow
\text{observation, organization and feasible control}\\
&\rightarrow
\text{viability, recovery reachability and confidence}
\rightarrow
\text{intervention consequences}
\rightarrow
\text{engineering decision}.
\end{aligned}}
```

Each arrow represents a distinct inferential or engineering step. A structural edge cannot be assumed to be a causal mechanism; a causal mechanism cannot determine a trajectory without dynamics; a simulated trajectory does not establish feasible recovery without observation and control constraints; a resilience metric does not alone establish service admissibility; and a resilience improvement does not automatically establish an efficient or sustainable intervention.

The **problem statement of this thesis** is therefore:

> **The engineering problem is to construct and validate an evidence-grounded representation of coupled Power–Transportation infrastructure in which directional dependency mechanisms are translated into time-, state-, and mode-dependent physical behavior; information and organizational conditions constrain feasible response; resilience is evaluated in terms of maintaining and recovering required services under uncertainty; and the resulting information is tested for its ability to support defensible intervention and sustainable-engineering decisions.**

The literature already solves important subsets of this problem. Section 1.4 therefore asks the narrower question required for a defensible research gap: **which transitions in this engineering chain remain insufficiently integrated, comparatively tested, or validated for the bounded P–T problem considered here?**

## References cited in Section 1.3

- Chester, M., Underwood, B. S., Allenby, B., Garcia, M., Samaras, C., Markolf, S., Sanders, K., Preston, B., & Miller, T. R. (2021). Infrastructure resilience to navigate increasingly uncertain and complex conditions in the Anthropocene. *npj Urban Sustainability, 1*, Article 4. https://doi.org/10.1038/s42949-021-00016-y
- Ghasemkhani, A., Basiri, M. A., & Nicholson, C. (2026). Interdependency and uncertainty in the resiliency of infrastructure networks: A comprehensive review. *International Journal of Critical Infrastructure Protection, 54*, 100866. https://doi.org/10.1016/j.ijcip.2026.100866
- Lian, X., Song, C., Li, Z., Qiu, L., & Liu, L. (2026). Resilience-oriented emergency resource dispatch for power–transportation coupled networks under rainstorm-induced flood hazards. *Applied Energy, 403*, 127004. https://doi.org/10.1016/j.apenergy.2025.127004
- Oladigbolu, J., Bakare, M. S., Motlagh, S. G., Mujeeb, A., & Li, L. (2025). A review on transport and power systems planning-operation integrating electric vehicles, energy storage, and other distributed energy resources. *Journal of Energy Storage, 135*, 118419. https://doi.org/10.1016/j.est.2025.118419
- Ouyang, M. (2014). Review on modeling and simulation of interdependent critical infrastructure systems. *Reliability Engineering & System Safety, 121*, 43–60. https://doi.org/10.1016/j.ress.2013.06.040
- Poulin, C., & Kane, M. B. (2021). Infrastructure resilience curves: Performance measures and summary metrics. *Reliability Engineering & System Safety, 216*, 107926. https://doi.org/10.1016/j.ress.2021.107926
- Rasoulkhani, K., & Mostafavi, A. (2018). Resilience as an emergent property of human-infrastructure dynamics: A multi-agent simulation model for characterizing regime shifts and tipping point behaviors in infrastructure systems. *PLOS ONE, 13*(11), e0207674. https://doi.org/10.1371/journal.pone.0207674
- Trucco, P., & Petrenj, B. (2023). Characterisation of resilience metrics in full-scale applications to interdependent infrastructure systems. *Reliability Engineering & System Safety, 235*, 109200. https://doi.org/10.1016/j.ress.2023.109200
- Wang, S., Lu, Q.-C., Liu, L., Xu, P.-C., Wang, R., & Zhang, L. (2026). Interdependency analysis of coupled power and transportation networks considering the charging decision preferences of EV drivers. *Reliability Engineering & System Safety, 268*, 112005. https://doi.org/10.1016/j.ress.2025.112005
- Wang, Y., Zhao, O., & Zhang, L. (2024). Multiplex networks in resilience modeling of critical infrastructure systems: A systematic review. *Reliability Engineering & System Safety, 250*, 110300. https://doi.org/10.1016/j.ress.2024.110300

## Scientific boundary of Section 1.3

This section establishes the **engineering problem**, not the final research-gap or novelty claim. It does not claim that coupled P–T modeling, dynamic recovery, information/organizational effects, viability theory, or sustainability analysis are individually novel. Those claims remain subject to the evidence synthesis of Section 1.4 and the separate reproducible novelty audit.