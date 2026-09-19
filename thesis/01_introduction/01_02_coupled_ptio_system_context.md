## 1.2 Coupled Power–Transportation System Context

For this thesis, the physical infrastructure core consists of Power and Transportation:

```math
\boxed{P+T}.
```

Information and Organization are represented as supporting domains:

```math
\boxed{I+O}.
```

This is a thesis-specific ontology. It does not imply that `P`, `T`, `I`, and `O` are four equivalent physical infrastructures.

Power and Transportation are the constituent physical systems because they contain the physical assets, connections, operational states, controls, and service functions required to provide electricity and mobility. This service-centered interpretation is consistent with the infrastructure System-of-Systems framing used by Hall et al. (2016). Power and Transportation also remain separately represented, consistent with integrated energy–transport modeling in which interaction does not require loss of system-specific structure or physics (Ibáñez et al., 2010).

The Information domain represents what can be observed, communicated, or estimated about the physical system. Depending on the experiment, this may include measurement availability, communication status, delays, missing observations, and state estimates. Information-related dependencies are recognized in infrastructure and cyber-physical-system research, but the existence of information flow does not by itself imply that a physical action can be executed (Mohamed, 2019; Rinaldi et al., 2001).

The Organizational domain represents the conditions through which information is converted into feasible action. Relevant conditions may include authority, coordination, priorities, personnel, equipment, resource availability, and response delays. Infrastructure-resilience research increasingly recognizes that institutions, governance arrangements, and human–infrastructure interactions can materially influence response and adaptation (Chester et al., 2021; Helmrich et al., 2021; Rasoulkhani & Mostafavi, 2018).

The resulting thesis representation is therefore

```math
\boxed{ \underbrace{P+T}_{\text{physical infrastructure}} + \underbrace{I+O}_{\text{knowledge and feasible-action support}}. }
```

This representation also requires a strict relationship taxonomy. Multilayer-network theory provides mathematical tools for representing multiple networks and relation types (Kivelä et al., 2014), but the presence of an interlayer edge is not treated in this thesis as evidence of a physical causal mechanism.

A **structural relation** identifies where interaction could occur. A **directional dependency** requires a physically or operationally interpretable mechanism through which a source affects a receiver under specified conditions. A reciprocal **interdependency** requires relevant directional dependencies in both directions. **Dynamic coupling** requires an additional step: the qualified mechanism must be sufficiently specified to enter the governing dynamic model.

The scientific progression is therefore

```math
\boxed{ \text{candidate relation} \rightarrow \text{qualified directional dependency} \rightarrow \text{dynamically admissible coupling}. }
```

For `P\rightarrow T`, candidate mechanisms include electricity supply to charging infrastructure and other electrically dependent transportation functions. Coupled traffic–power studies and reviews document relationships among charging demand, road-network behavior, and distribution-system operating constraints (Fotouhi et al., 2017; Unterluggauer et al., 2022; Wei et al., 2019).

For `T\rightarrow P`, transportation conditions may affect the accessibility required for repair, restoration, or deployment of mobile resources. Fan et al. (2024) explicitly incorporate transportation-network states into post-disaster repair routing. These mechanisms differ physically from `P\rightarrow T` mechanisms and are therefore represented and qualified separately.

Common exposure remains distinct. A flood may affect a road and a power asset simultaneously, but this shared exposure becomes a cross-system dependency only when the resulting state of one system subsequently affects the other through a specified mechanism.

Mechanisms described in Chapter 1 therefore represent **candidate mechanism families**. Their appearance in the conceptual architecture does not establish case-specific causal acceptance, parameter identification, or authorization for dynamic simulation. Those stronger claims require the corresponding evidence and methodological controls developed later in the thesis.

---

