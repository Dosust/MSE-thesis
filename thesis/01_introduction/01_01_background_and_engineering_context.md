## 1.1 Background and Engineering Context

The electrification of transportation is increasing the operational interaction between electric-power and transportation infrastructures. Electric-vehicle charging links mobility demand to the location, timing, and availability of electricity supply, while charging demand can influence distribution-system operation and planning (Unterluggauer et al., 2022; Wei et al., 2019). Emerging vehicle-to-grid and mobile-energy applications create additional opportunities for transportation resources to interact with the power system (Oladigbolu et al., 2025).

The relationship also extends beyond normal operation. Transportation conditions can affect power-system restoration because repair crews, equipment, replacement components, and mobile energy resources depend on physical access to damaged electrical assets. Post-disaster restoration studies explicitly show that road conditions can constrain repair routing and coordinated infrastructure recovery (Fan et al., 2024; Lian et al., 2026). Power-to-Transportation and Transportation-to-Power dependencies therefore arise through different physical and operational mechanisms.

These infrastructures matter because they provide services rather than simply because they contain assets. Hall et al. (2016) frame infrastructure assessment around the services produced by coordinated infrastructure systems. Under this interpretation, the power system supports electricity service, whereas the transportation system supports mobility and physical accessibility. A failure becomes important when it changes the ability of these systems to provide the required services or constrains the operation and recovery of another system.

Power and Transportation nevertheless remain distinct constituent systems. Integrated energy–transport studies can model them jointly while retaining their separate network structures, operational logic, and planning variables (Ibáñez et al., 2010). Coupling therefore does not require electrical and transportation physics to be homogenized into one generic network.

Direction is equally important. Electricity availability may affect charging infrastructure and other electrically dependent transportation functions, whereas road availability may affect repair access and restoration of the power system. Charging behavior and mobile electrical resources can create additional Transportation-to-Power effects under appropriate operating conditions (Oladigbolu et al., 2025; Wang et al., 2026). For this thesis,

```math
P\rightarrow T \qquad\text{and}\qquad T\rightarrow P
```

are qualified independently. Evidence of one direction does not establish the other.

The broader infrastructure-interdependency literature likewise distinguishes different forms of dependency and recognizes that cascading consequences can arise when a change in one infrastructure affects another through a functional relationship (Ouyang, 2014; Rinaldi et al., 2001). At the same time, simultaneous exposure to the same hazard does not by itself establish such a relationship. Two assets can fail together because they share a flood footprint without either failure causing the other.

The thesis therefore uses two complementary perspectives. A **System-of-Systems perspective** is used to represent the architecture of distinct constituent systems and their interfaces, while a **complex-dynamical-systems perspective** is used to study how their states, dependencies, disturbances, controls, and recovery processes evolve through time. Systems-of-systems research emphasizes the continued identity and operational characteristics of constituent systems within a larger architecture (Maier, 1998), while infrastructure-interdependency research demonstrates that interactions between constituent infrastructures can generate behavior not captured by isolated-system analysis (Ouyang, 2014; Rinaldi et al., 2001).

For analytical clarity, the thesis therefore adopts the modeling convention

```math
\boxed{ \text{System of Systems}=\text{architectural view}, \qquad \text{complex dynamical system}=\text{behavioral view}. }
```

This is a **thesis modeling convention**, not a claim that the two concepts are universally separate.

The engineering problem consequently extends beyond determining whether Power and Transportation are connected. It concerns whether specific directional mechanisms are supported by evidence, whether those mechanisms materially affect coupled behavior and service trajectories, whether the resulting system condition can be observed and acted upon, and whether critical services can remain acceptable or be recovered under disruption and uncertainty.

---

