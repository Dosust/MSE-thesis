# 1.1 Background and Engineering Context

Critical infrastructure systems provide essential services required for the functioning of modern societies, including electricity, mobility, communications, water, and other services that support economic activity and public welfare. Although these infrastructures are often designed, operated, and regulated as distinct systems, their performance is increasingly shaped by cross-system dependencies. In this thesis, a **directional dependency** denotes a relationship in which the state or operation of a receiving system depends on a source system, whereas **interdependency** denotes a coupled condition in which reciprocal directional dependencies are present. This terminology preserves directionality while remaining consistent with the broader critical-infrastructure literature on dependency and interdependency (Rinaldi et al., 2001; Ouyang, 2014).

Within this broader infrastructure context, **electric power and transportation form a particularly important coupled system**. The increasing electrification of transportation strengthens this coupling because electric-vehicle charging introduces spatially and temporally varying electricity demand into distribution networks, while charging availability and electrified mobility depend on the operating condition of the power system. Reviews of integrated transportation and power-distribution systems identify coordination among transportation demand, charging infrastructure, and electrical networks as an important joint planning and operational problem (Wei et al., 2019; Unterluggauer et al., 2022).

The coupling is implemented through directional dependency mechanisms. In the power-to-transportation direction,

```math
\boxed{P\rightarrow T},
```

electrical service enables transportation functions such as traffic-control devices, charging infrastructure, and other electrically dependent transportation assets. In the transportation-to-power direction,

```math
\boxed{T\rightarrow P},
```

the condition of the road network can influence power-system recovery because repair crews and mobile emergency resources must physically reach damaged electrical assets. Fan et al. (2024), for example, explicitly model the dependence of repair-crew routing on transportation-network road states in coordinated post-disaster restoration. A reciprocal P–T interdependency exists only when the relevant directional dependency mechanisms are both present under the conditions being analyzed.

These relationships become especially important under disruptive conditions. A disturbance that initially affects one infrastructure can modify another through an active dependency mechanism, creating indirect service losses or cascading effects. Rinaldi et al. (2001) established a foundational framework for identifying and analyzing critical-infrastructure interdependencies, while Ouyang (2014) reviewed multiple approaches for representing interdependent infrastructure behavior and cascading consequences. For the present research, **simultaneous exposure to the same hazard is not, by itself, sufficient to establish a dependency or interdependency**. A causal claim requires an identifiable relationship through which the state or service of a source affects a receiver.

The resulting engineering problem has both an **architectural** and a **behavioral** dimension. Systems-of-systems research emphasizes that constituent systems can retain operational and managerial characteristics while participating in a larger architecture whose behavior depends on their interactions (Maier, 1998). Infrastructure-interdependency research, in turn, emphasizes that coupled infrastructures can exhibit system-level behavior that cannot be inferred solely from isolated constituent networks (Rinaldi et al., 2001; Ouyang, 2014). Accordingly, this thesis uses the complementary modeling convention

```math
\boxed{\text{System of Systems}=\text{architectural representation}}
```

and

```math
\boxed{\text{Complex dynamical system}=\text{behavioral representation}.}
```

The architectural viewpoint identifies **what systems, components, interfaces, and candidate relationships exist**; the behavioral viewpoint addresses **how their states evolve, interact, propagate disruption, and recover through time**. This is a thesis modeling convention derived from the complementary roles of systems-of-systems architecture and interdependent-infrastructure dynamics, not a universal definition asserted from a single source.

Physical connectivity alone does not determine infrastructure response. The effect of a disruption also depends on whether system conditions can be observed, whether available information adequately represents those conditions, and whether organizations possess the authority, coordination capability, personnel, equipment, and time required to implement feasible actions. Rinaldi et al. (2001) recognize information and communications relationships as relevant dimensions of infrastructure interdependence. For the present thesis, these considerations motivate a distinction between the **physical infrastructure core**, Power and Transportation, and the supporting **Information and Organizational domains**, which affect how the physical system is observed and acted upon.

The central engineering concern is therefore not simply whether Power and Transportation networks are connected. It is whether evidence-qualified directional dependency mechanisms materially alter disturbance propagation and service trajectories; whether the resulting coupled behavior changes the maintenance and recovery of electricity and mobility services; and whether feasible actions can prevent or reverse unacceptable degradation. This requires progression from structural knowledge to causal mechanisms, from causal mechanisms to time-dependent dynamics, and from dynamics to observable and controllable service behavior.

This thesis consequently takes Power and Transportation as its physical engineering core and treats Information and Organization as supporting domains governing observation, interpretation, coordination, resources, and control:

```math
\boxed{
\underbrace{P+T}_{\text{physical infrastructure core}}
+
\underbrace{I+O}_{\text{supporting domains}}.
}
```

The presence of a layer or relation does not automatically imply causal significance. Each cross-system relation must later be supported by an explicit mechanism, admissible evidence, a defined mathematical representation, and a stated validity domain. Section 1.2 therefore moves from the general engineering context to the precise system boundary, domain roles, and directional relationships considered in the thesis.

## References cited in Section 1.1

- Fan, J., He, P., Li, C., Zhao, C., & Ji, Y. (2024). A post-disaster restoration model for power-gas-transportation distribution networks considering spatial interdependency and energy hubs. *Electric Power Systems Research, 233*, 110505. https://doi.org/10.1016/j.epsr.2024.110505
- Maier, M. W. (1998). Architecting principles for systems-of-systems. *Systems Engineering, 1*(4), 267–284. https://doi.org/10.1002/(SICI)1520-6858(1998)1:4%3C267::AID-SYS3%3E3.0.CO;2-D
- Ouyang, M. (2014). Review on modeling and simulation of interdependent critical infrastructure systems. *Reliability Engineering & System Safety, 121*, 43–60. https://doi.org/10.1016/j.ress.2013.06.040
- Rinaldi, S. M., Peerenboom, J. P., & Kelly, T. K. (2001). Identifying, understanding, and analyzing critical infrastructure interdependencies. *IEEE Control Systems Magazine, 21*(6), 11–25. https://doi.org/10.1109/37.969131
- Unterluggauer, T., Rich, J., Andersen, P. B., & Hashemi, S. (2022). Electric vehicle charging infrastructure planning for integrated transportation and power distribution networks: A review. *eTransportation, 12*, 100163. https://doi.org/10.1016/j.etran.2022.100163
- Wei, W., Wu, D., Wu, Q., Shafie-khah, M., & Catalão, J. P. S. (2019). Interdependence between transportation system and power distribution system: A comprehensive review on models and applications. *Journal of Modern Power Systems and Clean Energy, 7*, 433–448. https://doi.org/10.1007/s40565-019-0516-7

## Scientific boundary of Section 1.1

Section 1.1 establishes the engineering context and terminology needed for the study. It does not claim that P–T coupling is novel, that any directional dependency mechanism is universally active, or that the proposed representation is superior to existing models.