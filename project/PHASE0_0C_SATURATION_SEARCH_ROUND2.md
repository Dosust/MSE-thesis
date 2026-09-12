# Phase 0 — 0C Saturation Search Round 2

**Status:** COMPLETE ROUND 2 / saturation not yet closed  
**Decision gate:** `THEORETICAL_DECISION_GATE_PROTOCOL_V1.md`  
**Requirements:** frozen `R1–R12`  
**Purpose:** adversarial search for an existing formalism that already supplies the common invariant/translation layer needed across heterogeneous infrastructure-interdependency representations.

---

## 1. Round-2 question

```math
\boxed{\text{Does an existing formalism already define the common invariant needed to translate among heterogeneous infrastructure representations without loss of engineering meaning?}}
```

The candidate representation families examined in this round are:

```text
1. shared-state complex SoS models;
2. semantic/model interoperability frameworks;
3. distributed-simulation interoperability standards;
4. model-exchange/co-simulation interfaces;
5. multi-domain infrastructure co-simulation frameworks;
6. ontology/knowledge-graph semantic middleware;
7. recent infrastructure/digital-twin interoperability approaches.
```

This round is not allowed to infer novelty from absence of one exact phrase.

---

## 2. Evidence classes

### C2.1 — Shared-state SoS theory [E]

Haberlin & Haimes (2018) model interdependent regional infrastructures as complex systems of systems by tracing critical interconnections/interdependencies through shared/common states together with decisions, decision makers, stakeholders, resources, time frame, and organizational setups.

Haimes (2018) further argues that the genesis of SoS interdependencies can be understood through shared states and other essential entities including decisions, resources, functions, policies, decision makers, stakeholders, and organizational setups.

**Implication:** a Phase-0 dependency object cannot claim novelty merely from adding state, organization, resources, actors, decisions, or time.

### C2.2 — Semantic CPS model integration [E]

NIST's semantic CPS work combines model-based systems engineering, requirements traceability, domain ontologies, physical/software component hierarchies, and discrete/continuous simulation in a common semantic environment.

**Implication:** semantic connection between heterogeneous component/model types and physical simulation is an established research direction.

### C2.3 — SoS interoperability reference architecture [E]

Sadeghi et al. (2024) derive domain-agnostic interoperability requirements for heterogeneous SoSs, review conceptual/technical approaches, and propose a reference architecture for interoperability-fostering frameworks. The paper explicitly discusses SOSI, MoBIE, ontology reuse, federated interoperability, semantic integration, and data/model transformation.

**Implication:** 'a reusable framework for heterogeneous SoS interoperability' is not a sufficient standalone contribution.

### C2.4 — HLA distributed-simulation interoperability [E]

IEEE 1516-2025 defines the High Level Architecture (HLA) as a common architecture for interconnecting interacting simulations. The HLA family separates framework/rules, federate interface services, and object-model format/syntax.

Key boundary:

```math
\boxed{\text{HLA standardizes simulation federation/interchange responsibilities; it does not by itself define the physical meaning of an infrastructure dependency.}}
```

### C2.5 — FMI model exchange and co-simulation [E]

The Functional Mock-up Interface (FMI) standard defines standardized containers and APIs for dynamic model exchange, co-simulation, and scheduled execution. FMI enables heterogeneous subsystem models to be executed together while retaining internal solvers or exposing model equations/partitions depending on interface type.

Key boundary:

```math
\boxed{\text{FMI provides model-exchange/execution semantics, not a complete infrastructure-interdependency ontology.}}
```

### C2.6 — HELICS multi-domain infrastructure co-simulation [E]

HELICS provides scalable co-simulation in which heterogeneous simulators exchange values and remain time-synchronized. Its documented use spans electric power, communications, markets, end-use, natural gas, and transportation models.

Key boundary:

```math
\boxed{\text{HELICS operationalizes cross-domain simulator interaction; it does not establish that an exchanged variable corresponds to a causally valid infrastructure dependency.}}
```

### C2.7 — Recent semantic-hub / ontology-driven model interoperability [E]

Recent 2026 work continues to develop ontology-driven semantic hubs, model translation/transformation, digital-twin semantic middleware, physical/cyber asset integration, and ontology/knowledge-graph backbones.

**Implication:** semantic normalization, model mapping, and cross-lifecycle translation are active and increasingly mature research areas.

---

## 3. Critical distinction produced by Round 2 [D]

Round 2 reveals that at least four different objects are often conflated:

```math
\boxed{
\begin{aligned}
\mathcal R^{phys} &: \text{real-world functional/causal dependency},\\
\mathcal R^{sem} &: \text{semantic meaning/alignment between representations},\\
\mathcal R^{sim} &: \text{runtime exchange/synchronization between simulators},\\
\mathcal R^{org} &: \text{organizational/decision relation}.
\end{aligned}}
```

These are related but not equivalent.

Therefore:

```math
\boxed{
\text{semantic interoperability}
\neq
\text{simulation interoperability}
\neq
\text{physical dependency}
\neq
\text{organizational dependency}
}
```

A valid infrastructure framework must declare which object is being represented at each step.

---

## 4. Candidate common-invariant question after Round 2 [P]

The earlier candidate tuple

```math
\mathfrak d_e=(s,r,\rho,m,q,M,z,w,\delta,c,U,\mathcal H)
```

is now considered potentially over-specified.

Round 2 suggests that the deeper invariant may be closer to a typed transformation relation:

```math
\boxed{
\mathfrak d_e:
(\mathsf S_e,\mathsf R_e,\mathsf C_e)
\mapsto
\Delta \mathsf R_e
}
```

or, for state-based models,

```math
\boxed{
X_r^{+}=\Phi_e(X_r,X_s,c_e)
}
```

with additional metadata layered around the invariant rather than placed inside its irreducible core.

**Status:** proposed only; not frozen.

---

## 5. Round-2 comparison against the common-invariant requirement

| Family | Preserves internal domain model | Defines exchange/runtime interface | Defines semantic alignment | Represents organizational entities | Defines real-world causal dependency semantics | Candidate universal invariant? |
|---|---:|---:|---:|---:|---:|---:|
| Shared-state SoS | 2 | 0–1 | 1 | 2 | 1–2 | partial |
| NIST semantic CPS | 2 | 1 | 2 | 1 | 1 | partial |
| SoS interoperability reference architecture | 2 | 1–2 | 2 | 1–2 | 0–1 | partial |
| HLA | 2 | 2 | 1 | 0–1 | 0 | no |
| FMI | 2 | 2 | 0–1 | 0 | 0 | no |
| HELICS | 2 | 2 | 0–1 | 0–1 | 0–1 | no |
| Ontology/KG semantic hubs | 1–2 | 1 | 2 | 0–1 | 0–1 | partial |

Scoring uses the frozen interpretation:

```text
0 = absent / not represented;
1 = indirect or implementation-specific;
2 = explicit first-class support.
```

These scores are diagnostic, not a final ranking, and remain source-bounded.

---

## 6. Strong falsification result

Round 2 rejects the following candidate novelty statements:

```text
- We are the first to preserve heterogeneous subsystem models while coupling them.
- We are the first to create an interoperability layer for heterogeneous SoSs.
- We are the first to use ontology/semantic mappings to connect heterogeneous models.
- We are the first to represent interdependent SoSs through shared states plus organizational entities.
- We are the first to couple independent infrastructure simulators dynamically.
```

These claims are prohibited unless a future exhaustive search establishes a much narrower statement.

---

## 7. Residual research problem after Round 2

No source identified in this round simultaneously provides all of the following as one minimal formal object:

```math
\boxed{
\begin{array}{l}
\text{(i) real-world directed functional/causal infrastructure relation,}\\
\text{(ii) preserved domain-specific physics,}\\
\text{(iii) time/state/context dependence,}\\
\text{(iv) explicit evidence status of the relation claim,}\\
\text{(v) service consequence,}\\
\text{(vi) translation into semantic and simulation interfaces.}
\end{array}}
```

However, this is **not yet an established gap** because the search has not reached saturation.

The candidate residual question is now:

```math
\boxed{
\text{Can a minimal typed dependency invariant bridge real-world causal meaning, semantic representation, and executable model coupling while preserving sector physics and evidence provenance?}
}
```

---

## 8. Why 0C does not close after Round 2

Round 2 introduced representation families that were not explicit in Round 1:

```text
- general SoS interoperability reference architectures;
- HLA simulation federation standards;
- FMI model-exchange/co-simulation standards;
- semantic CPS simulation frameworks;
- modern semantic-hub/model-transformation approaches.
```

Under the preregistered saturation rule:

```math
\boxed{\text{new representation family changes taxonomy}\Rightarrow\text{0C remains open}.}
```

---

## 9. Round-3 search target

Round 3 must now search for formalisms explicitly combining **causal/functional relation semantics with model interoperability** rather than searching generic infrastructure interdependency.

Required search clusters:

```text
1. typed relation / relation ontology / causal semantics for system interfaces;
2. SysML / MBSE dependency and interface metamodels;
3. Functional Mock-up / HLA semantic annotation extensions;
4. FMI variable dependency semantics and model-variable causality;
5. causal knowledge graphs for cyber-physical/infrastructure systems;
6. provenance/evidence standards for relation assertions (PROV-O, nanopublication-style claims, evidence ontologies);
7. ontology-to-equation / ontology-to-simulation mappings;
8. category-theoretic / compositional systems engineering formalisms, if engineering-relevant;
9. recent 2025–2026 infrastructure interoperability reviews that explicitly compare semantic, causal and executable coupling.
```

### Round-3 falsification question

```math
\boxed{
\text{Does any existing formalism already bind }\{
\text{typed relation semantics},
\text{causal mechanism},
\text{evidence provenance},
\text{state/time dependence},
\text{executable coupling}
\}\text{ in a reusable infrastructure-independent object?}
}
```

If yes, Phase 0 must adopt/extend that formalism. If no and the taxonomy stabilizes, 0C may be eligible for closure.

---

## 10. Round-2 verdict

```text
0C status: OPEN
Saturation: NOT REACHED
Dominating predecessor: NOT YET IDENTIFIED
Candidate residual contribution: NARROWED AGAIN
0D permission: BLOCKED
```

No change is authorized to the frozen thesis ontology or seven-stage framework.