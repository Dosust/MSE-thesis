# References and Citation Guide — Stage 1 Structural Knowledge Base

## Core references

### Rinaldi, Peerenboom & Kelly (2001)
Rinaldi, S. M., Peerenboom, J. P., & Kelly, T. K. (2001). Identifying, understanding, and analyzing critical infrastructure interdependencies. *IEEE Control Systems Magazine*, 21(6), 11–25. DOI: 10.1109/37.969131.

**Use for:** dependency/interdependency concepts; physical, cyber, geographic, and logical interdependency taxonomy.

**Citation-ready claim:**
> Infrastructure interdependencies should be classified by the mechanism through which one infrastructure affects another, including physical, cyber, geographic, and logical relations (Rinaldi et al., 2001).

### Ouyang (2014)
Ouyang, M. (2014). Review on modeling and simulation of interdependent critical infrastructure systems. *Reliability Engineering & System Safety*, 121, 43–60. DOI: 10.1016/j.ress.2013.06.040.

**Use for:** limits of single modeling paradigms; hidden/invisible interdependencies; network, simulation, agent, and system-based approaches.

**Citation-ready claim:**
> A network representation is useful for interdependent infrastructures but does not by itself capture every functional, dynamic, or latent dependency, and some interdependencies may remain effectively invisible during normal operation (Ouyang, 2014).

### Kivelä et al. (2014)
Kivelä, M., Arenas, A., Barthelemy, M., Gleeson, J. P., Moreno, Y., & Porter, M. A. (2014). Multilayer networks. *Journal of Complex Networks*, 2(3), 203–271. DOI: 10.1093/comnet/cnu016.

**Use for:** heterogeneous multilayer networks, node-layer tuples, intra-layer and inter-layer connectivity.

**Citation-ready claim:**
> Multilayer-network theory allows different node-layer tuples and explicit intra- and inter-layer relations, making it suitable for heterogeneous infrastructure systems whose constituent networks contain different entity classes (Kivelä et al., 2014).

### De Domenico et al. (2013)
De Domenico, M., Solé-Ribalta, A., Cozzo, E., Kivelä, M., Moreno, Y., Porter, M. A., Gómez, S., & Arenas, A. (2013). Mathematical formulation of multilayer networks. *Physical Review X*, 3, 041022. DOI: 10.1103/PhysRevX.3.041022.

**Use for:** tensor/supra-network mathematical formulation.

### Fotouhi, Moryadee & Miller-Hooks (2017)
Fotouhi, H., Moryadee, S., & Miller-Hooks, E. (2017). Quantifying the resilience of an urban traffic-electric power coupled system. *Reliability Engineering & System Safety*, 163, 79–94. DOI: 10.1016/j.ress.2017.01.026.

**Use for:** explicit power–transport coupling, linking variables, transportation accessibility and electrical dependencies.

### Li et al. (2022)
Li, Z., Tang, W., Lian, X., Chen, X., Zhang, W., & Qian, T. (2022). A resilience-oriented two-stage recovery method for power distribution system considering transportation network. *International Journal of Electrical Power & Energy Systems*, 135, 107497. DOI: 10.1016/j.ijepes.2021.107497.

**Use for:** repair crews, mobile storage, road-to-grid recovery coupling.

### Mohamed (2019)
Mohamed, A. A. A. (2019). On the rising interdependency between the power grid, ICT network, and e-mobility: Modeling and analysis. *Energies*, 12(10), 1874. DOI: 10.3390/en12101874.

**Use for:** power–ICT–e-mobility relations and explicit ICT topology.

### Rasoulkhani & Mostafavi (2018)
Rasoulkhani, K., & Mostafavi, A. (2018). Resilience as an emergent property of human-infrastructure dynamics. *PLOS ONE*, 13(11), e0207674. DOI: 10.1371/journal.pone.0207674.

**Use for:** explicit human–infrastructure coupling; organizational actors as part of resilience dynamics.

### Dong et al. (2020)
Dong, S., Li, Q., Farahmand, H., Mostafavi, A., Berke, P. R., & Vedlitz, A. (2020). Institutional connectedness in resilience planning and management of interdependent infrastructure systems. *Journal of Management in Engineering*, 36(6). DOI: 10.1061/(ASCE)ME.1943-5479.0000839.

**Use for:** coordinated actor networks, institutional arrangements, plans, policies, organizational connectedness.

### Yu et al. (2025)
Yu, D. J., Shin, H. C., et al. (2025). Logical interdependencies in infrastructure: What are they, how to identify them, and what do they mean for infrastructure risk analysis? *Risk Analysis*, 45(2), 356–375. DOI: 10.1111/risa.16555.

**Use for:** hidden/logical interdependencies, formal and informal rules, human decisions, rule-based network representations.

**Citation-ready claim:**
> Logical interdependencies should be operationalized through explicit human decisions and formal or informal institutional rules rather than treated as an undefined residual relation (Yu et al., 2025).

### Runge et al. (2019)
Runge, J., Nowack, P., Kretschmer, M., Flaxman, S., & Sejdinovic, D. (2019). Detecting and quantifying causal associations in large nonlinear time series datasets. *Science Advances* / related PCMCI literature.

**Use for:** constrained time-series causal discovery as a candidate-generation/validation layer.

**Important thesis restriction:** causal-discovery output is not automatically an engineering dependency; mechanism and evidence validation remain required.

### Pearl (2009/2010)
Pearl, J. *Causality: Models, Reasoning, and Inference* and related structural-causal-model literature.

**Use for:** distinction between association, intervention, and causation.

## Thesis-ready synthesis paragraph

> The Stage-1 representation is treated as a heterogeneous multilayer structural knowledge base rather than a conventional binary network. Multilayer-network theory provides the formal structure for representing distinct infrastructure layers and explicit inter-layer relations (De Domenico et al., 2013; Kivelä et al., 2014), while infrastructure-interdependency research shows that dependencies may be physical, cyber, geographic, or logical and may not all be visible during normal operation (Rinaldi et al., 2001; Ouyang, 2014). Accordingly, the model distinguishes confirmed dependencies, scope-qualified non-dependencies, conditional dependencies, latent candidates, and unresolved relations. Logical and organizational dependencies are further examined through explicit actor decisions, institutional rules, and coordination structures (Rasoulkhani & Mostafavi, 2018; Dong et al., 2020; Yu et al., 2025). Data-driven causal-discovery methods may be used to generate or test latent candidates, but candidate relations are not promoted to engineering dependencies without mechanistic and evidentiary support.
