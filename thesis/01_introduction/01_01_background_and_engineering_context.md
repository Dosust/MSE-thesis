## 1.1 Background and Engineering Context

Electricity and mobility are critical infrastructure services. Their provision depends on distinct physical systems, but transportation electrification is increasing the number and importance of interfaces between electric-power and transportation infrastructures. Electric-vehicle charging connects mobility demand to the location, timing, capacity, and availability of electricity supply, while charging demand can affect distribution-system operation and planning. Vehicle-to-grid and mobile-energy applications create additional pathways through which transportation resources may interact with the power system when the required technical and operating conditions are present (Oladigbolu et al., 2025; Unterluggauer et al., 2022; Wei et al., 2019).

The interaction extends beyond normal operation. Power-system restoration depends on physical access for repair crews, equipment, replacement components, mobile generators, and other restoration resources. Transportation disruption can therefore constrain access to damaged electrical assets and alter restoration timing (Fan et al., 2024; Lian et al., 2026).

The engineering significance of these infrastructures follows from the services they provide rather than from their assets alone. The power system provides electricity service, whereas the transportation system provides mobility and physical accessibility. A disruption becomes consequential when it reduces one of these services or constrains the operation or recovery of the other system. This service-centered interpretation is consistent with infrastructure System-of-Systems reasoning, in which constituent systems retain their identities while contributing to broader service functions (Hall et al., 2016).

Power and Transportation nevertheless remain physically distinct systems. Power networks obey electrical laws, operating constraints, and electrical-control requirements. Transportation networks represent roads, traffic, routing, accessibility, mobility demand, and transportation-control processes. Their interaction does not require their native physical descriptions to be replaced by one homogeneous network. Integrated energy–transport studies instead show that distinct systems can remain separately represented while selected states, flows, constraints, or decisions are coupled (Ibáñez et al., 2010).

Directionality is therefore fundamental. Electricity availability can affect charging infrastructure and other electrically dependent transportation functions. Transportation availability can affect repair access and power-system restoration. Charging behavior and mobile electrical resources can create additional Transportation-to-Power effects under appropriate operating conditions (Fan et al., 2024; Fotouhi et al., 2017; Wang et al., 2026).

For this thesis,

```math
\boxed{ P\rightarrow T \not\Rightarrow T\rightarrow P }
```

because evidence of a dependency in one direction does not establish a dependency in the reverse direction. Each direction can have a different mechanism, activation condition, magnitude, delay, characteristic timescale, uncertainty, and validity domain.

Structural proximity must also be distinguished from functional dependency. Two assets can be exposed simultaneously to the same flood without either asset causing the state change of the other. Common exposure can therefore generate correlated disruption without establishing a cross-system directional dependency (Ouyang, 2014; Rinaldi et al., 2001).

Two complementary perspectives are used to represent the resulting coupled infrastructure. The **System-of-Systems perspective** describes architecture: constituent systems, services, entities, interfaces, and relations. The **complex-dynamical-systems perspective** describes behavior: how physical states, disturbances, dependencies, feedback, controls, delays, and recovery processes evolve through space and time. Systems-of-systems theory emphasizes the continued identity of constituent systems within a larger architecture, whereas infrastructure-interdependency research shows that cross-system interaction can produce behavior that isolated-system analysis does not represent (Maier, 1998; Ouyang, 2014; Rinaldi et al., 2001).

For analytical clarity, this thesis adopts the modeling convention

```math
\boxed{ \text{System of Systems} = \text{architectural view}, \qquad \text{complex dynamical system} = \text{behavioral view}. }
```

This convention is specific to the thesis and is not presented as a universal separation between the two concepts.

The engineering problem therefore extends beyond determining whether Power and Transportation are connected. It requires establishing which cross-system relations are scientifically admissible as directional dependencies, what those dependencies do dynamically, what operators can observe and feasibly do while the system evolves, whether required services can remain acceptable or recover, and how intervention consequences affect the final engineering decision.
