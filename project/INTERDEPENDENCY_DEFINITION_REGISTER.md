# Interdependency Definition Register — Phase 0 v1.0

**Status:** FROZEN FOR THEORETICAL DECISION GATE v1.0  
**Scope:** terminology used to evaluate the current `P–T–I–O` ontology against the Phase-0 candidate representation  
**Change rule:** once comparative scoring begins, a definition may change only through an explicit version increment with a recorded reason and re-run of all affected tests.  
**Evidence rule:** source meaning, thesis-operational meaning, mathematics, boundary and uncertainty are kept separate.

## 1. Register schema

For every term `T_k`, use

```math
\mathcal R_{T_k}
=
\left(
D_k^{source},
S_k,
D_k^{thesis},
M_k,
B_k,
U_k
\right),
```

where:

- `D_k^{source}` = source-supported meaning;
- `S_k` = authoritative/foundational source;
- `D_k^{thesis}` = operational meaning used in this thesis;
- `M_k` = mathematical representation where appropriate;
- `B_k` = explicit boundary: what the term does **not** mean;
- `U_k` = unresolved ambiguity/uncertainty.

Evidence labels:

```math
[E]=\text{established/source-supported},\quad
[D]=\text{derived},\quad
[P]=\text{thesis proposal},\quad
[A]=\text{assumption},\quad
[U]=\text{uncertain/unresolved}.
```

---

## 2. System

### Source meaning `[E]`
ISO/IEC/IEEE 15288, as reproduced by SEBoK, defines a system as a combination of interacting elements organized to achieve one or more stated purposes. SEBoK also retains the general-system definition of a system as a set of elements in interaction.

### Source
- SEBoK, **System (glossary)**, citing ISO/IEC/IEEE 15288:2015 and von Bertalanffy (1968).
- https://sebokwiki.org/wiki/System_(glossary)

### Thesis meaning `[P/E]`
A system is a bounded collection of entities, states, relations and governing rules whose interactions jointly produce one or more functions/services that cannot be specified solely by listing isolated entities.

### Mathematical representation `[P]`

```math
\mathcal S_\alpha
=
\left(
X_\alpha,
F_\alpha,
U_\alpha,
Q_\alpha,
B_\alpha
\right).
```

### Boundary
A system is **not** synonymous with a graph. A graph may represent part of a system structure; it need not contain physics, control, service semantics or organizational state.

### Uncertainty
The exact minimal object required for all infrastructure domains remains part of Phase-0 testing.

---

## 3. Constituent system

### Source meaning `[E]`
System-of-systems literature treats constituents as systems that remain independently meaningful; Maier's operational and managerial independence criteria are the key basis.

### Source
- Maier, M. W. (1998), *Architecting principles for systems-of-systems*, Systems Engineering 1(4), 267–284.
- SEBoK, **System of Systems (SoS) (glossary)**: https://sebokwiki.org/wiki/System_of_Systems_(SoS)_(glossary)

### Thesis meaning `[P/E]`
A constituent infrastructure system is a system that retains a meaningful operational identity, service function and governing model when embedded in the larger infrastructure system-of-systems.

### Mathematical representation `[P]`

```math
\mathcal S_P\neq\mathcal S_T,
\qquad
F_P\neq F_T
\quad\text{in general}.
```

### Boundary
A constituent system is not merely a layer label or arbitrary partition of a network.

### Uncertainty
Power and Transportation clearly satisfy constituent-system status; whether information and organization should be represented as constituent systems or cross-cutting aspects is exactly what the decision gate tests.

---

## 4. System of Systems (SoS)

### Source meaning `[E]`
SEBoK reports two central formulations: separately defined systems operating together toward a common goal, and Maier's operationally and managerially independent components that continue to exist independently when composed.

### Source
- SEBoK, **System of Systems (SoS) (glossary)**.
- Maier (1998).

### Thesis meaning `[P/E]`
A Power–Transportation SoS is a composition of independently meaningful infrastructure systems whose coupled states, services and decisions generate cross-system behavior that cannot be analyzed adequately by treating each constituent in isolation.

### Mathematical representation `[P]`

```math
\mathscr S(t)
=
\mathcal C_{SoS}
\left(
\{\mathcal S_\alpha\},
\mathcal E(t),
\Phi(t)
\right).
```

### Boundary
SoS does not mean that constituent physics are homogenized into one universal law.

### Uncertainty
The exact composition operator `\mathcal C_{SoS}` remains a proposed abstraction until tested.

---

## 5. Interaction

### Source meaning `[E/U]`
Systems definitions establish interaction among elements as fundamental, but no single infrastructure-specific definition found in the initial authoritative search is sufficiently precise for dependency analysis.

### Source basis
- SEBoK, **System (glossary)**.
- SEBoK, **Inter-Node Interaction (glossary)**.

### Thesis meaning `[P]`
An interaction is any admissible exchange, contact, communication, action or mutual influence between entities. Interaction is the broadest relational term in the framework and does **not** by itself establish functional reliance or causality.

### Mathematical representation `[P]`

```math
\chi_{ij}(t)\in\mathcal X_{rel}
```

indicates that an interaction of declared type can occur between entities `i` and `j`.

### Boundary

```math
\text{interaction}\not\Rightarrow\text{dependency}.
```

### Uncertainty
A universal interaction ontology is outside thesis scope; only interaction classes needed to distinguish dependencies are retained.

---

## 6. Interface

### Source meaning `[E]`
SEBoK/ISO terminology defines an interface as a shared boundary between functional units characterized by functions and exchanges, or as a hardware/software component connecting components to pass information.

### Source
- SEBoK, **Interface (glossary)**, citing ISO/IEC 2382-1:1993 and ISO/IEC/IEEE 24765.
- https://sebokwiki.org/wiki/Interface_(glossary)

### Thesis meaning `[P/E]`
An infrastructure interface is the physical, informational or organizational boundary/channel/component through which an interaction or dependency may be realized.

### Mathematical representation `[P]`

```math
\mathcal J_{ij}
=
\left(
B_i\cap B_j,
\mathcal K_{ij}
\right),
```

where `\mathcal K_{ij}` denotes admissible exchange channels/mechanisms at the boundary.

### Boundary

```math
\boxed{\text{interface}\neq\text{dependency}}
```

An interface can exist without one entity being functionally dependent on the other.

### Uncertainty
Some real interfaces are distributed rather than spatially localized; `B_i\cap B_j` is therefore conceptual, not always geometric.

---

## 7. Dependency

### Source meaning `[E]`
Rinaldi, Peerenboom and Kelly (2001) define dependency as a linkage or connection between two infrastructures through which the state of one infrastructure influences or is correlated to the state of the other. Later infrastructure literature commonly distinguishes dependency as unidirectional and interdependency as bidirectional.

### Sources
- Rinaldi, S. M., Peerenboom, J. P., & Kelly, T. K. (2001), *Identifying, understanding, and analyzing critical infrastructure interdependencies*, IEEE Control Systems Magazine, 21(6), 11–25.
- Johansson, J., & Hassel, H. (2010), *An approach for modelling interdependent infrastructures in the context of vulnerability analysis*, Reliability Engineering & System Safety, 95(12), 1335–1344. DOI: 10.1016/j.ress.2010.06.010.

### Thesis meaning `[P]`
A directed dependency `s\rightarrow r` exists in declared context `c` when an admissible change in the source state/output can change the feasible state, function or service of the receiver through a specified or testable mechanism.

The thesis intentionally uses a stronger operational criterion than mere correlation.

### Mathematical representation `[P]`
For service map

```math
Q_r=f_r(X_r,X_s,c),
```

a dependency exists if

```math
\exists\,X_s,X_s'
:\quad
f_r(X_r,X_s,c)
\neq
f_r(X_r,X_s',c).
```

For differentiable local models, a possible local signature is

```math
\frac{\partial Q_r}{\partial X_s}\neq0.
```

### Boundary

```math
\text{correlation}\not\Rightarrow\text{dependency}.
```

Shared hazard exposure or spatial co-location alone is not accepted as a functional dependency without a mechanism.

### Uncertainty
The minimal evidence required to promote an inferred dependency to accepted status is not yet fixed; it will be linked to evidence classes in Phase 0C/0F.

---

## 8. Interdependency

### Source meaning `[E]`
Rinaldi et al. define infrastructure interdependency as a bidirectional relationship in which the state of each infrastructure influences or is reliant upon the state of the other. Johansson and Hassel note that disturbances may traverse to another infrastructure and possibly return to the infrastructure where failure originated.

### Sources
- Rinaldi et al. (2001).
- Johansson & Hassel (2010).

### Thesis meaning `[P/E]`
Two constituent systems are interdependent over a declared context and time horizon when accepted directed dependency paths exist in both directions, whether directly between the same component pair or through mediated paths.

### Mathematical representation `[P]`
Direct reciprocity:

```math
A\rightarrow B
\land
B\rightarrow A.
```

Mediated system-level reciprocity:

```math
\exists\,p_{A\rightarrow B},
\qquad
\exists\,p_{B\rightarrow A}.
```

### Boundary
A single cross-system edge is a dependency, not automatically an interdependency.

### Uncertainty
Whether path-based mediated reciprocity should be called `interdependency` or a separate `feedback interdependency` subclass will be decided during benchmark testing.

---

## 9. Coupling

### Source meaning `[E/U]`
Systems and infrastructure literature use `coupling` broadly for relationships among system elements and for mathematical terms joining otherwise separate subsystem models. No single cross-domain standard definition found in the initial search is sufficiently specific for this thesis.

### Source basis
- SEBoK systems/coupling terminology.
- Kivelä et al. (2014), *Multilayer Networks*, Journal of Complex Networks, 2(3), 203–271. DOI: 10.1093/comnet/cnu016.

### Thesis meaning `[P]`
Coupling is the mathematical or computational realization by which an accepted dependency changes a receiving subsystem's state equation, algebraic constraint, transition logic or feasible-action set.

### Mathematical representation `[P]`

```math
\Phi_e:
(X_s,X_r,z_e,c_e)
\mapsto
\Delta F_r
```

or, for discrete/hybrid logic,

```math
\Phi_e\mapsto\Delta R_r.
```

### Boundary

```math
\boxed{\text{dependency}\neq\text{coupling operator}}
```

The dependency is a relationship in the engineered system; `\Phi_e` is a model representation of its effect.

### Uncertainty
Alternative coupling formalisms may be needed for optimization, co-simulation and logical/organizational relations; Phase 0 tests whether one abstract contract can contain them without forcing one equation form.

---

## 10. Feedback

### Source meaning `[E]`
Control literature defines feedback as routing information about system output/state back into system input/control so subsequent behavior is affected by observed performance.

### Source
- IEEE Technology Navigator, **Feedback / Feedback Control** (used only as a terminology anchor, not as a thesis model).

### Thesis meaning `[P]`
Feedback is a closed directed influence path in which a downstream consequence returns, directly or indirectly, to modify a state, control, constraint or dependency of an upstream system.

### Mathematical representation `[P]`

```math
A
\rightarrow
B
\rightarrow
\cdots
\rightarrow
A.
```

For dynamic coupling,

```math
X_A(t)
\rightarrow
X_B(t+\delta_1)
\rightarrow
X_A(t+\delta_1+\delta_2).
```

### Boundary
Reciprocal structural edges without an active closed dynamic influence need not produce meaningful feedback in a given operating regime.

### Uncertainty
Positive/negative feedback classification is deferred until mechanism-specific models are selected.

---

## 11. Cascade

### Source meaning `[E]`
Recent reliability reviews describe cascading failure as propagation in which failure/degradation of one or more components influences degradation or triggers failure of other components. Infrastructure reviews emphasize chains of induced effects across interconnected systems.

### Sources
- Zhao, Y., Cai, B., Cozzani, V., & Liu, Y. (2025), *Failure dependence and cascading failures: A literature review and research opportunities*, Reliability Engineering & System Safety, 256, 110766. DOI: 10.1016/j.ress.2024.110766.
- Lu, Z. et al. (2025), *Cascading failures in urban infrastructure systems: A comprehensive review of disaster chain mechanisms*, Journal of Infrastructure Intelligence and Resilience, 4(3), 100157. DOI: 10.1016/j.iintel.2025.100157.

### Thesis meaning `[P/E]`
A cascade is a time-ordered sequence of induced state degradations, mode transitions or service losses transmitted through accepted dependency mechanisms, where at least one downstream transition is conditional on an upstream system change.

### Mathematical representation `[P]`

```math
\mathfrak d_{e_1}(t_1)
\Rightarrow
\Delta X_{i_2}(t_2)
\Rightarrow
\mathfrak d_{e_2}(t_2)
\Rightarrow\cdots,
\qquad
t_1\le t_2\le\cdots.
```

### Boundary
Simultaneous failures caused only by a common external hazard are **not** by themselves a cascade. Common-cause failure may initiate or coexist with a cascade, but an induced propagation mechanism must be shown.

### Uncertainty
The exact event/trajectory criterion used to declare cascade onset and termination will be specified in H1 after Phase 0.

---

## 12. Frozen distinctions for the gate

The gate will use the following distinctions unless versioned evidence overturns them:

```math
\boxed{
\text{interaction}
\supset
\text{interface-enabled relation}
\supseteq
\text{dependency}
}
```

but neither containment is assumed to be strictly set-theoretic for every real system; it is a conceptual hierarchy.

The following non-equivalences are mandatory:

```math
\boxed{
\text{interface}
\neq
\text{dependency}
\neq
\text{interdependency}
\neq
\text{coupling operator}
}
```

and

```math
\boxed{
\text{common-cause association}
\neq
\text{causal dependency}
\neq
\text{cascade}.
}
```

---

## 13. Gate consequences

These definitions are **not novelty claims**. They establish the language required to test novelty and adequacy.

Any representation `M` evaluated in Phase 0 must demonstrate that it can preserve these distinctions without ad hoc reinterpretation.
