# Phase 0 — 0C Saturation Search Round 3

**Status:** COMPLETE — taxonomy changed again; saturation not reached.  
**Repository:** `Dossiya-SE/MSE-thesis`  
**Gate:** `THEORETICAL_DECISION_GATE_PROTOCOL_V1.md`  
**Purpose:** adversarial search for an existing reusable relation formalism that already binds causal meaning, semantic meaning, evidence/provenance, state/time dependence, and executable coupling.

---

## 1. Frozen falsification question

```math
\boxed{
\text{Does an existing formalism already bind causal meaning, semantic meaning, evidence provenance, state/time dependence, and executable coupling into one reusable infrastructure-independent dependency object?}
}
```

If yes, Phase 0 must adopt/extend that formalism rather than invent another dependency grammar.

---

## 2. Targeted representation families searched

Round 3 deliberately targeted representation classes not fully covered in Rounds 1–2:

1. **SysML v2 / KerML relation and interface semantics**;
2. **FMI model-structure, causality and variable-dependency semantics**;
3. **W3C PROV-O qualified influence / provenance relations**;
4. **SysML-v2-to-FMI semantic bridging / model transformation**;
5. **physics-based simulation ontologies separating physical phenomena from simulation artefacts**;
6. **temporal/causal knowledge graphs**;
7. **applied category theory (ACT), wiring diagrams, operads, structured/decorated cospans and open-system composition**;
8. **category-theoretic semantic interoperability in systems engineering**.

---

# 3. Evidence extraction

## R3-P1 — SysML v2 / KerML

**Evidence status:** `[E] standard`.

OMG SysML v2 (formal version 2.0 adopted September 2025) is based on KerML and provides precise machine-readable abstract syntax, APIs and interoperability support for requirements, behavior, structure, analysis and verification.

KerML provides relationships, associations, links, features, multiplicities and directional features. However, the existence of a SysML/KerML relationship does not by itself establish a physically causal infrastructure dependency. OMG issue records also show that direction/association semantics have required clarification and are not equivalent to governing dynamical equations.

**Capability:**

```text
system architecture semantics      strong
source/target relation structure   strong
interface/port/flow representation strong
machine-readable interchange       strong
real-world causal mechanism        domain-supplied, not guaranteed
provenance/evidence of claim       not core purpose
executable physical coupling       requires mapping/toolchain
```

**Phase-0 consequence:** SysML v2/KerML is a strong architecture/metamodel layer, but it does not eliminate the need to distinguish a modeled relationship from an evidence-supported physical/organizational dependency.

---

## R3-P2 — FMI 3.x

**Evidence status:** `[E] standard`.

FMI defines a standardized container/interface for exchanging and executing dynamic models. Its model description exposes variables, causality (`input`, `output`, `parameter`, `independent`, etc.), model structure, output dependencies, state derivatives, events and runtime variable dependencies.

A useful FMI abstraction is:

```math
u\longrightarrow y,
```

with a declared model structure such as

```math
y_i=y_i(u,p,x,t),
```

plus runtime dependency metadata where supported.

**Critical distinction:** FMI `causality` and `dependencies` are simulation-interface semantics. They do not, by themselves, establish that the corresponding real infrastructures are causally dependent in the engineering sense.

**Capability:**

```text
executable model interface         very strong
variable direction/dependencies    strong
state/time/event semantics         strong
sector-model preservation          strong (black-box/container principle)
real-world mechanism provenance    not core purpose
organizational/authority relation  not core purpose
scientific evidence provenance     not core purpose
```

**Phase-0 consequence:** executable dependency semantics already exist; our candidate object must not duplicate FMI model-structure metadata.

---

## R3-P3 — W3C PROV-O

**Evidence status:** `[E] W3C Recommendation`.

PROV-O provides interoperable provenance semantics around:

```math
\text{Entity},\quad \text{Activity},\quad \text{Agent},
```

with relations such as generation, usage, derivation, communication, association and delegation.

Its **qualified influence** pattern is highly relevant. A binary influence can be reified as an intermediate `prov:Influence` object and annotated with additional attributes such as role, plan, time, agent and application-specific metadata.

Conceptually:

```math
A\xrightarrow{\text{influence object}}B
```

where the influence relation itself can carry metadata.

**Capability:**

```text
provenance/evidence interchange    very strong
agent/organization responsibility  strong
qualified relation metadata        strong
time annotation                    strong
physical governing mechanism       not supplied generically
state evolution equations          not supplied
executable simulation coupling     not supplied
```

**Major implication:** the idea of turning a binary relation into a first-class relation object with attachable metadata is not novel. Phase 0 must not claim novelty from reifying an interdependency edge into an object.

---

## R3-P4 — SysML v2 + ontology + FMI semantic bridge

**Evidence status:** `[E] current peer-reviewed MBSE evidence`.

A 2026 framework explicitly links SysML v2 architecture elements to FMI simulation elements through an ontology/knowledge-graph layer. It represents system elements, ports, signals, connections and simulation configurations, and uses ontology rules to validate permitted SysML-to-FMI mappings.

This gives the chain:

```math
\text{architecture object}
\longleftrightarrow
\text{semantic graph}
\longleftrightarrow
\text{FMI executable model}.
```

**This is the closest direct predecessor discovered so far to our proposed `SEMANTICS -> MATHEMATICS -> EXECUTION` bridge.**

**What it does not automatically establish:**

```text
- physical causality of the real infrastructure relation;
- evidence status that the real dependency exists;
- infrastructure-specific resilience/service consequence;
- a universal relation invariant independent of architecture/simulation technologies.
```

**Phase-0 consequence:** semantic-to-executable mapping is already an active research area. Any residual contribution must explicitly include the reality/evidence/mechanism layer, not merely SysML-to-simulation linkage.

---

## R3-P5 — Physics-Based Simulation Ontology (PSO)

**Evidence status:** `[E] 2025 research; preprint/engineering ontology evidence`.

PSO deliberately separates:

```math
\text{PSO-Physics}
\neq
\text{PSO-Sim}.
```

The first describes physical phenomena independently of solver-specific interpretations; the second represents simulation artefacts/inputs for solvers.

This separation is directly relevant to the thesis because it reinforces:

```math
\boxed{\text{physical reality}\neq\text{simulation representation}.}
```

**Limitation relative to Phase 0:** PSO is developed around physics-based engineering simulation rather than a complete physical-information-organization infrastructure SoS dependency theory.

---

## R3-P6 — temporal/causal knowledge graphs

**Evidence status:** `[E] current research`.

Temporal knowledge-graph methods increasingly model long-term causal dependencies and evolving relations. Other recent industrial knowledge-graph work combines provenance, temporal validity and decision traceability.

These methods show that:

```math
\text{relation}\,+\,\text{time}\,+\,\text{causal labels}\,+\,\text{provenance}
```

can already be represented semantically.

**Limitation:** learned or asserted causal graph relations do not automatically provide domain governing equations, executable coupling or physical validation.

---

# 4. New first-class family — compositional systems mathematics

## R3-P7 — wiring diagrams / operads / structured & decorated cospans / open systems

**Evidence status:** `[E] mathematical systems theory`.

Applied category theory supplies a rigorous way to represent and compose **open systems** while separating syntax from semantics.

A structured-cospan form is:

```math
L(a)\rightarrow x\leftarrow L(b),
```

where `x` is a system and the feet represent its boundary/interface.

Wiring-diagram/operadic approaches describe how systems with inputs and outputs are interconnected, while algebras/functors assign different mathematical semantics to the same compositional syntax.

A key pattern is therefore:

```math
\boxed{
\text{common compositional syntax}
\xrightarrow{\text{semantic functor}}
\text{domain-specific mathematics}
}
```

Examples already include electrical circuits, Petri nets, Markov processes, continuous dynamical systems and hybrid/open systems.

This directly challenges the Phase-0 intuition that we must invent a large universal dependency tuple. A deeper solution may instead be:

```math
\boxed{
\text{typed interface/composition structure}
+
\text{separate semantic interpretations}
}
```

where power, transport, information and organization receive different semantics while sharing a compositional language.

**Important limitation:** ACT/open-system formalisms do not automatically provide infrastructure-domain causal evidence, provenance, institutional meaning or resilience service semantics. Those must be supplied as semantic layers or decorations.

---

## R3-P8 — category theory for systems-engineering interoperability

**Evidence status:** `[E] NIST systems-engineering research`.

NIST explicitly identifies category theory as a candidate mathematical foundation for interoperability among heterogeneous systems-engineering formalisms, including SysML-like, software, mathematical and dynamical models. NIST also notes that engineering applications remain substantially at prototype/proof-of-concept level and require further development.

This is highly relevant because it means the thesis should investigate **compositional translation** before inventing a new standalone ontology.

---

# 5. Round-3 binding test

A dominating predecessor would need to make the following first-class in one reusable formalism:

```math
\mathcal B=\{B_1,\ldots,B_8\},
```

with:

| ID | Required binding |
|---|---|
| `B1` | typed source/receiver and system identity |
| `B2` | real-world mechanism / causal meaning |
| `B3` | state/time dependence |
| `B4` | semantic representation/interchange |
| `B5` | provenance/evidence status of the relation claim |
| `B6` | executable/numerical coupling |
| `B7` | compositional extension to new domains |
| `B8` | mapping to engineering service consequence |

### Evidence result

No single Round-3 source was found that explicitly makes all eight bindings first-class.

However, the **combined predecessor envelope** is now much stronger:

```math
\begin{aligned}
\text{SysML/KerML} &\rightarrow B_1,B_4,\\
\text{FMI} &\rightarrow B_3,B_6,\\
\text{PROV-O} &\rightarrow B_4,B_5,\\
\text{SysML--ontology--FMI bridge} &\rightarrow B_1,B_4,B_6,\\
\text{PSO} &\rightarrow B_2,B_4,B_6\text{ (physics-focused)},\\
\text{temporal/causal KG} &\rightarrow B_3,B_4,B_5\text{ (partially)},\\
\text{ACT/open systems} &\rightarrow B_1,B_6,B_7\text{ via compositional semantics}.
\end{aligned}
```

This matrix is qualitative and source-bounded; it is not yet the formal `R1-R12` score used for 0D/0E.

---

# 6. Main scientific deduction [D]

Round 3 suggests that the primitive object may not be a large tuple containing every concern.

A more defensible architecture is potentially **layered**:

```math
\boxed{
\underbrace{\mathcal C_e}_{\text{compositional/interface skeleton}}
+
\underbrace{\Sigma_e}_{\text{domain semantics / mechanism}}
+
\underbrace{\Pi_e}_{\text{provenance/evidence}}
+
\underbrace{\Xi_e}_{\text{executable realization}}
}
```

where:

- `C_e` identifies typed participants and composition/interface structure;
- `Sigma_e` provides the physical/informational/organizational meaning and governing mechanism;
- `Pi_e` states provenance, evidence status and uncertainty of the relation claim;
- `Xi_e` maps the relation into a numerical/executable implementation such as FMI/HELICS/native equations.

This is **not adopted**. It is a derived candidate for future ablation against the original tuple.

The corresponding conceptual chain is:

```math
\boxed{
\text{REALITY}
\xrightarrow{\text{semantic assertion}}
\text{MODEL RELATION}
\xrightarrow{\text{mathematical semantics}}
\text{EXECUTABLE COUPLING}
}
```

with provenance/evidence qualifying the first mapping rather than being mistaken for physical dynamics.

---

# 7. Falsified / weakened candidate claims

Round 3 weakens or rejects the following as novelty claims:

```text
- making relations first-class objects;
- attaching metadata/time/roles to a relation;
- representing model-variable dependencies and causality;
- mapping SysML architecture to FMI simulations;
- separating physical phenomena from simulation artefacts;
- using semantic graphs to integrate heterogeneous engineering models;
- compositional syntax separated from mathematical semantics;
- composing open dynamical systems through typed interfaces.
```

---

# 8. Residual candidate problem after Round 3

The candidate research problem is now narrower:

```math
\boxed{
\begin{minipage}{0.88\textwidth}
Can established compositional-system mathematics and semantic/provenance standards be specialized into a minimal infrastructure-interdependency contract that preserves evidence-supported causal mechanism while allowing consistent translation into heterogeneous executable power, transportation, information and organizational models and measurable service consequences?
\end{minipage}
}
```

The likely contribution, if any, is therefore **specialization + binding + validation**, not invention of generic compositionality, provenance, ontology or co-simulation.

---

# 9. Saturation decision

Round 3 introduced a new first-class predecessor family:

```math
\boxed{\text{compositional open-systems / applied-category-theory formalisms}.}
```

It also introduced a very close semantic-to-executable predecessor:

```math
\boxed{\text{SysML v2 + ontology + FMI semantic integration}.}
```

Therefore, under the preregistered stopping rule:

```math
\boxed{\text{SATURATION NOT REACHED}.}
```

0D remains blocked.

---

# 10. Required Round 4

Round 4 must now focus narrowly on the two strongest new challenges:

1. **compositional systems theory** as the possible mathematical backbone;
2. **semantic/provenance-to-executable binding** as the possible engineering implementation layer.

The frozen Round-4 question is:

```math
\boxed{
\text{Can a compositional open-system formalism be extended/decorated with causal evidence and infrastructure service semantics so completely that a separate Phase-0 dependency contract is unnecessary?}
}
```

Priority evidence targets:

```text
- applied category theory for hybrid/control/port-Hamiltonian/physical systems;
- functorial mappings among SysML/ontology/dynamical models;
- decorated/structured cospans carrying provenance or typed domain semantics;
- causal/evidence annotations on compositional morphisms;
- infrastructure or cyber-physical applications of operads/wiring diagrams;
- formal mappings from compositional structures into FMI/Modelica/HELICS or other executable co-simulation environments;
- service/performance semantics on compositional open systems.
```

Only after this challenge is exhausted can 0C be considered for closure.
