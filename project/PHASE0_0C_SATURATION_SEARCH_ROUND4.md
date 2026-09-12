# Phase 0 — 0C Saturation Search Round 4

**Status:** COMPLETE — no new first-class representation family identified; 0C eligible for bounded closure.  
**Repository:** `Dossiya-SE/MSE-thesis`  
**Gate:** `THEORETICAL_DECISION_GATE_PROTOCOL_V1.md`  
**Purpose:** test whether compositional open-system mathematics already subsumes the proposed Phase-0 dependency contract once causal evidence, organizational meaning, provenance and service consequence are added.

---

## 1. Frozen Round-4 question

Can a compositional open-system formalism be extended or decorated with causal evidence and infrastructure service semantics so completely that a separate Phase-0 dependency contract is unnecessary?

### Falsification rule

If an existing formalism already supplies, as first-class and reusable objects:

```math
\mathcal B=\{B_1,\ldots,B_8\},
```

with:

| ID | Binding |
|---|---|
| `B1` | typed source/receiver and system identity |
| `B2` | evidence-supported real-world causal mechanism |
| `B3` | state/time dependence |
| `B4` | semantic representation/interchange |
| `B5` | provenance/evidence status of the relation claim |
| `B6` | executable/numerical coupling |
| `B7` | compositional extension to new domains |
| `B8` | mapping to engineering service consequence |

then Phase 0 must adopt/extend that formalism instead of proposing a separate dependency contract.

---

# 2. Evidence families examined

Round 4 focused only on the strongest Round-3 challenger class and its engineering realizations:

1. wiring diagrams and operads for open dynamical systems;
2. structured cospans;
3. decorated cospans and generalized decorated cospans;
4. categorical semantics of cyber-physical systems;
5. behavioral/safety contracts as algebras over wiring diagrams;
6. category-theoretic systems-engineering interoperability;
7. compositional System Dynamics / syntax-to-semantics mappings;
8. translation from systems-engineering models to executable simulation models;
9. co-simulation realization through FMI/HELICS.

No generic infrastructure-interdependency searches were added in this round. This was an adversarial test of the compositional-systems candidate only.

---

# 3. R4-P1 — Wiring diagrams + open dynamical-system algebras

**Evidence status:** `[E] foundational mathematical systems theory`.

Vagner, Spivak and Lerman formalize a category/operad of typed boxes and wiring diagrams. The wiring diagram is the interconnection **syntax**; algebras assign semantic content such as general or linear differential systems.

The key separation is:

```math
\boxed{\text{typed compositional syntax}\neq\text{domain dynamical semantics}.}
```

A box contains typed input/output ports but initially has no differential-equation semantics. Different algebras can populate the same wiring architecture with different mathematical behaviors.

### Round-4 implication

This directly supports the idea that the thesis should avoid placing all semantics into one monolithic dependency tuple. It also means that typed interfaces and compositionality are established prior art.

### Missing relative to the Phase-0 gate

The wiring-diagram formalism does not automatically establish:

```text
- that a real infrastructure dependency exists;
- the evidence/provenance supporting that claim;
- institutional authority or organizational responsibility;
- resilience/service consequence;
- a specific FMI/HELICS execution binding.
```

These can potentially be added through separate algebras/decorations, but are not supplied simply by the wiring syntax.

---

# 4. R4-P2 — Structured cospans

**Evidence status:** `[E] mathematical open-systems theory`.

Structured cospans represent an open system as

```math
L(a)\rightarrow x\leftarrow L(b),
```

and compose open systems through categorical composition. Established examples include electrical circuits, Petri nets and chemical reaction networks.

### Capability

```text
open-system boundary/interface      very strong
composition                         very strong
hierarchical assembly               strong
domain extensibility                strong
causal evidence                     not intrinsic
provenance of relation claim        not intrinsic
organizational authority semantics  domain-supplied
service consequence                 domain-supplied
execution binding                   external realization required
```

### Interpretation

Structured cospans are a strong candidate for the **compositional skeleton**, not a complete infrastructure-interdependency semantics.

---

# 5. R4-P3 — Decorated cospans

**Evidence status:** `[E] mathematical open-systems theory`.

Decorated cospans explicitly permit an open-system cospan to carry additional internal data through a decoration functor. In general form, a morphism can be represented by a cospan

```math
X\rightarrow N\leftarrow Y
```

plus a decoration associated with `N`.

The decoration can, in principle, carry rich domain data.

### Major challenge to Phase 0

This means the following idea is already generic mathematics:

```math
\boxed{\text{composable relation/interface skeleton}+\text{attachable domain metadata}.}
```

Therefore Phase 0 must **not** claim novelty merely for attaching mechanism, timing, uncertainty, organization or provenance metadata to an interdependency object.

### Critical limitation

The decorated-cospan machinery guarantees compositional structure of the chosen decorations; it does not itself certify that a decoration is scientifically valid, physically causal or empirically supported.

Hence:

```math
\boxed{\text{ability to attach causal evidence}\neq\text{validation of causal evidence}.}
```

This distinction is retained as central to the thesis.

---

# 6. R4-P4 — Categorical CPS semantics and contracts

**Evidence status:** `[E] peer-reviewed cyber-physical systems theory`.

Categorical CPS research uses wiring diagrams to relate architecture and behavior and introduces behavioral/safety contracts as an algebra over the same compositional syntax.

A contract can constrain allowable input/output behavior:

```math
R\subseteq X_{in}\times X_{out}.
```

This is significant because it shows that requirements/acceptable behaviors can already be composed alongside dynamical semantics.

### Consequence

The thesis cannot claim novelty for:

```text
- compositional constraints;
- compositional safety contracts;
- linking architecture to behavior through wiring diagrams;
- horizontal/vertical composition of heterogeneous system views.
```

### Remaining limitation

Contracts constrain admissible behavior; they do not by themselves establish the real-world causal mechanism or the provenance of the infrastructure-dependency assertion. They also do not automatically provide the sustainability/service semantics required later in the thesis.

---

# 7. R4-P5 — Systems-engineering interoperability via category theory

**Evidence status:** `[E] NIST systems-engineering research`.

NIST explicitly investigates category theory as a foundation for semantic interoperability among heterogeneous system representations, including SysML-like models and mathematical/dynamical models.

The key engineering principle is:

```math
\text{model}_A\xrightarrow{F}\text{model}_B
```

with a structure-preserving mapping `F`.

Recent NIST work continues to treat compositional structures in systems engineering as an active research and tool-development area rather than a solved industrial standard.

### Consequence

Model-translation/interoperability itself is not novel. What remains potentially thesis-specific is the infrastructure-interdependency specialization and validation of which semantics must be preserved.

---

# 8. R4-P6 — Compositional System Dynamics

**Evidence status:** `[E] recent mathematical modeling research`.

Recent compositional System Dynamics work uses attributed categorical structures, structured cospans and functorial mappings to separate diagram syntax from semantics, compose stock-flow models and map among representations.

This strengthens the finding that:

```math
\boxed{\text{common syntax}+\text{multiple semantic realizations}}
```

is established beyond control/dynamical-systems examples.

It also demonstrates software implementation through AlgebraicJulia-like ecosystems.

### Limitation

The work is not an infrastructure-specific evidence/provenance theory and does not make organizational authority or validated cross-infrastructure causality automatic.

---

# 9. R4-P7 — Executable realization remains a separate layer

Existing engineering standards and tools demonstrate that executable coupling is already well handled through mechanisms such as FMI and HELICS.

A model relation may be executed as

```math
u_i(t)\rightarrow y_j(t)
```

through a co-simulation interface while each subsystem retains its internal solver/model.

However:

```math
\boxed{\text{executable variable exchange}\neq\text{proof of real-world causal dependency}.}
```

Therefore the thesis must retain a distinction between:

```math
\mathcal R^{real},\quad
\mathcal R^{sem},\quad
\mathcal R^{math},\quad
\mathcal R^{exec}.
```

---

# 10. Round-4 dominance test

The strongest compositional predecessor envelope is:

```math
\mathcal P_{ACT}=
\{\text{wiring diagrams},\text{open-system algebras},\text{structured cospans},\text{decorated cospans},\text{contracts},\text{functorial model mappings}\}.
```

Against the binding requirements:

| Binding | ACT/open-systems envelope |
|---|---|
| `B1` typed participants/interfaces | **Explicit** |
| `B2` real-world causal mechanism | **Can encode; not automatically established** |
| `B3` state/time dependence | **Explicit through suitable dynamical semantics** |
| `B4` semantic representation | **Explicit** |
| `B5` evidence/provenance status | **Can decorate/encode; not a native causal-validation rule** |
| `B6` executable coupling | **Requires implementation/mapping; not intrinsic to abstract syntax** |
| `B7` compositional extension | **Explicit and strong** |
| `B8` service consequence | **Can encode via chosen semantics/contracts; infrastructure meaning not supplied generically** |

### Result

The ACT/open-systems envelope is a **mathematical backbone candidate**, but it is not a complete drop-in infrastructure-interdependency theory.

No Round-4 source was found that simultaneously provides:

```math
\text{compositionality}
+\text{validated infrastructure causality}
+\text{evidence provenance}
+\text{organizational meaning}
+\text{service consequence}
+\text{executable realization}
```

as one ready-to-use, infrastructure-independent formalism.

This is a **bounded search result**, not a universal non-existence claim.

---

# 11. Main deduction [D]

The Round-4 result argues against both extremes:

```text
Extreme A: invent one huge universal dependency tuple.
Extreme B: assume generic category theory alone provides infrastructure meaning.
```

The more defensible candidate architecture is layered:

```math
\boxed{
\mathfrak D_e=
(\mathcal C_e,\Sigma_e,\Pi_e,\Xi_e)
}
```

where:

- `C_e` = compositional/interface skeleton;
- `Sigma_e` = domain semantics and causal mechanism;
- `Pi_e` = provenance/evidence/uncertainty qualification;
- `Xi_e` = executable realization.

This object is **not adopted**. It is the candidate architecture to be tested in 0D–0F.

A service mapping remains external but linked:

```math
Q_k=G_k(X,\mathfrak D),
```

so that the engineering requirement remains:

```math
\Delta\mathfrak D\rightarrow\Delta X\rightarrow\Delta Q.
```

---

# 12. Saturation assessment

Rounds 1–3 each introduced a new first-class representation family and therefore failed the preregistered saturation rule.

Round 4 did **not** introduce a new first-class family. It deepened the already identified compositional/open-systems family through:

```text
- structured cospans;
- decorated cospans;
- behavioral contracts;
- functorial interoperability;
- compositional System Dynamics;
- executable realization mappings.
```

No dominating predecessor was identified that makes the Phase-0 engineering specialization unnecessary.

Therefore, under the preregistered stopping rule:

```math
\boxed{\text{0C HAS REACHED BOUNDED REPRESENTATION-FAMILY SATURATION}.}
```

This means only that the targeted representation-family search is sufficiently stable to proceed to comparative testing. It does **not** establish novelty and does **not** prove that no omitted paper/formalism exists.

---

# 13. 0C conclusion

The source evidence supports the following bounded conclusions:

**[E]** Generic compositionality, typed interfaces, open systems, metadata/decorations, behavioral contracts, semantic interoperability and executable co-simulation are established prior art.

**[D]** A monolithic dependency tuple is not theoretically justified merely because many attributes are relevant.

**[D]** A layered relation architecture is more compatible with established separation between composition syntax, domain semantics, provenance and execution.

**[U]** It remains unknown whether the current frozen thesis ontology `M0={P,T,I,O}` or the candidate domain × aspect ontology `M1=D×A` provides the better engineering representation under the frozen requirements.

**[U]** It remains unknown which fields/layers of the candidate dependency representation are actually necessary for explanation, prediction and decision.

These unknowns belong to 0D–0F.

---

# 14. Gate transition

0C is now eligible to close.

The next formal phase is:

```math
\boxed{\text{0D — Formalize competing representations }M_0\text{ and }M_1\text{ under identical semantics and test boundaries}.}
```

No `RETAIN / REVISE / REPLACE` decision is permitted until 0D, 0E and 0F are complete.
