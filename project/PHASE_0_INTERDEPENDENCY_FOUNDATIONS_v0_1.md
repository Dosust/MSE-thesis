# Phase 0 — Theoretical Foundations of Dynamic Infrastructure Interdependency
## Foundations v0.1: Power–Transportation with Information and Organization

**Date:** 12 September 2026  
**Status:** [P] PROPOSED REFERENCE FRAMEWORK — synthetic verification completed; empirical validation pending.  
**Input:** User attachment, Pasted markdown(20260912-105113).md, read in full.  
**Purpose:** Provide reusable definitions, relationship records and composition rules for heterogeneous infrastructure systems, initially instantiated on power and transportation.  
**Governance:** This is a preparatory work package supporting the existing seven stages, not an eighth scientific stage or an automatic replacement of the canonical framework. Neither the existing interdependency tuple nor H1–H5 is replaced. The domain–aspect refinement remains a proposal for integration.

> No claim without a definition, mechanism, evidence, assumptions, test and boundary of validity.

[E] = externally supported; [D] = derived under stated premises; [H] = hypothesis; [P] = proposal; [A] = assumption; [U] = unresolved. Definitions, schemas and composition rules below are [P] unless otherwise labelled. Numerical results are [D] from explicitly synthetic [A] inputs.

## 1. LEARN and VERIFY — foundation and evidence boundary

This is a targeted foundation study, not a systematic review, novelty assessment or execution of the four frozen H1 database searches. Sources provide conceptual anchors; they do not automatically enter the fresh eligible corpus.

| ID | Source-supported foundation | How we use it | Boundary |
|---|---|---|---|
| E01 | Maier (1998, pp. 267–269) distinguishes systems of systems through operational and managerial independence and emphasizes their interfaces. | Record constituent purpose, decision authority and coordination arrangements. | Independence concerns constituent identity and operation; it does not mean absence of resource dependencies. Power and transport are not automatically a SoS at every chosen boundary. |
| E02 | Rinaldi et al. (2001, pp. 13–16) distinguish directional dependency, reciprocal interdependency and physical, cyber, geographic and logical relationships. Their dependency definition includes influence or correlation. | Preserve the taxonomy as source terminology; require explicit causal mechanisms for accepted propagation edges in this thesis. | Our causal requirement is a deliberate narrowing. Common exposure remains represented as an external cause, rather than discarded. |
| E03 | Kivelä et al. (2014, abstract and introduction) provide a common language for multilayer representations and distinguish several network forms. | Use typed entities and relations; record the meaning of each aspect. | A multilayer representation does not establish causal identification or governing physics. |
| E04 | NIST (2026, Summary and Description) motivates common cross-domain CPS foundations, integrating physical, digital and human components, with timing, composition, boundaries and assurance concerns. | Make information, actors, timing and model interfaces explicit. | Our Ph/I/O views are a thesis proposal, not NIST's official aspect taxonomy. |
| E05 | Leveson (2004, abstract) proposes a systems-theoretic accident model. | Retain control and organization as a foundation to study, alongside component behavior. | Abstract-level support in this execution; the full-text fetch failed. Detailed mapping to STAMP is pending and no STAMP compliance is claimed. |
| E06 | Ouyang (2014, abstract) reviews empirical, agent-based, system-dynamics, economic, network and other modeling approaches. | Compare candidate model families against the intended question. | Abstract-level support; no claim that one method or this proposal is universally superior. |

E01 and E02 were checked in full-text copies, with the cited passages inspected. E03 was checked on the authors' arXiv record; E04 on the NIST page. E05–E06 are limited to retrieved publication abstracts. References and access links appear in Section 12.

### Scientific corrections to the supplied outline

| Supplied formulation | Correction adopted in v0.1 | Reason |
|---|---|---|
| Two domains × three aspects gives six independent subsystems | Six views/classification cells; actual subsystem boundaries need evidence | A matrix partition does not establish independence or separate state ownership. |
| P–T reciprocal sector arrows imply a feedback loop | Distinguish reciprocal sector influence from a closed, executable entity-level loop | P1 → T1 and T2 → P2 need not connect into a cycle. |
| Unknown dependencies form an enumerable set | Record known unresolved candidates and an explicit incompleteness statement | Truly unknown relationships cannot be listed in advance. |
| All functional states lie in [0,1] | Define the domain of each state; use [0,1] only for justified normalized quantities | State may be a mode, vector, queue, capacity or availability indicator. |
| M means binary existence; U means uncertainty | Reserve M for the canonical mechanism and U for admissible controls; introduce b for existence and Xi for uncertainty | Avoid collision with existing thesis notation. |
| Every interaction transfers a scalar q | Permit material flow, enabling constraints, information, decisions and resource allocation | Authorization is not a conserved physical commodity. |
| A single ODE captures the whole system | Use a hybrid differential/algebraic formulation with history where required | Switching, constraints and delays require additional semantics. |
| A new common mathematical language is already a contribution | Treat usefulness and reuse as hypotheses | Novelty requires comparison with existing foundations and independent evaluation. |

## 2. Deliverable 1 — definition register

These are operational definitions for this proposal. E01–E06 motivate their context, but do not establish the entire register verbatim.

| Term | Operational definition | Admissibility question |
|---|---|---|
| System | Bounded collection of entities and relations with specified behavior and functions | What is inside, outside and measured? |
| Constituent system | System with its own purpose and documented degree of operational/managerial autonomy | What can it do, and who controls it? |
| System of systems | Interacting constituent systems evaluated as an aggregate while their identities and autonomy remain explicit | Are the SoS characteristics supported at the chosen boundary? |
| Service | Function delivered to named users, measured over a stated period and spatial area | What units, recipients and minimum requirements? |
| Capability | Ability to provide a specified function under stated conditions | Under which operating/resource assumptions? |
| Entity | Uniquely identified asset, actor, process, information object or service | Is it a distinct object or another view of an existing object? |
| State | Variables sufficient for evolution under the declared model, or an explicitly incomplete state estimate | Is history also required? |
| Interaction | Any specified exchange or influence between entities | Does it create a consequential dependency? |
| Dependency | Directed causal relationship through which a source affects a receiver's feasible behavior or service under specified conditions | What changes if the source changes and other causes are controlled? |
| Interdependency | Reciprocal causal influence between entities or aggregate systems within a declared domain and time horizon | Are both directions evidenced? Is there an actual feedback path? |
| Interface | Physical, informational or organizational arrangement at which a relation is realized | Where does its input/output contract apply? |
| Coupling mechanism | Process/law connecting source conditions to receiver inputs, constraints or transitions | What equation, event rule or mechanism evidence supports it? |
| Feedback | A closed causal path returning influence to an earlier entity or state | Does the component path close and respect temporal order? |
| Cascade | Sequence of consequential changes transmitted through specified mechanisms after an initiating event | Can common-cause effects and independent failures be distinguished? |
| Latent dependency | Identified relationship with little realized effect in one regime but material effect in another | What activates or amplifies it? |
| Hidden dependency | Relationship absent from the current model, possibly hypothesized from anomalies | What evidence would establish or reject it? |
| Boundary of validity | Operating, spatial, temporal, data and intervention conditions under which a claim is justified | What happens outside that domain? |

A zero local sensitivity does not prove that a dependency is absent: thresholding, saturation or inactive modes can hide influence. Conversely, correlation is insufficient to promote a candidate to a causal edge.

## 3. Deliverable 2 — domain × aspect ontology

Define separate index sets:

```math
\mathcal D_{\mathrm{dom}}=\{P,T\},\qquad
\mathcal A_{\mathrm{view}}=\{\mathrm{Ph},\mathrm I,\mathrm O\}.
```

Water W is added only for the extension verification case. An eventual ICT infrastructure domain would be distinct from the information aspect attached to every domain.

| Domain | Physical view | Information view | Organization view |
|---|---|---|---|
| P | Feeders, supplies, loads, repair resources | Measurements, estimates, messages, commands | Operator authority, dispatch rules, budgets, responsibilities |
| T | Roads, vehicles, charging assets, access | Traffic observations, travel-time estimates, routing messages | Road access decisions, transport coordination, resource allocation |

These are illustrative entity classes, not evidence that every case contains every listed entity.

**Identity rules.** Each real entity has one persistent ID. A shared actor or communication asset may be referenced by multiple views; its capacity and state are not duplicated. The registry stores entity type, domain membership, aspect memberships, owner, spatial location, state owner and provenance. Store true actor IDs separately from sector labels: one actor may serve several sectors.

**Canonical crosswalk.** Keep S = {P,T,I,O} as the existing high-level thesis description. The proposed refinement exposes information and organization within and across P and T. It does not remove I or O or assert that all informational/organizational systems are internal to one operator.

**Boundary contract.** Before instantiation record: joint service questions; constituent owners; spatial region; time horizon and resolution; external supplies; excluded mechanisms; available data; permissible interventions; and conflicting local objectives. Whole-system coverage is assessed against this contract, not against an unbounded universe.

## 4. Deliverable 3 — directed dependency grammar

Use a stable relation ID k and typed source/receiver ports:

```math
\mathfrak d_k:
(E_i^{\alpha,a},p_{\mathrm{out}})
\longrightarrow
(E_j^{\beta,b},p_{\mathrm{in}}).
```

The existing canonical object is preserved:

```math
\mathfrak I_{ij}^{\alpha\beta}
=
(E_i^\alpha,E_j^\beta,M_{ij},w_{ij},
\delta_{ij},\tau_{ij},a_{ij},m,\mathcal H_t).
```

The new record adds metadata and port semantics around that object. It does not redefine the meanings of delta, tau or a; each mapping must cite the canonical field definition before numerical use. The supplementary delay field below is explicitly named ell to avoid silently equating distinct canonical timing quantities.

| Required field | Meaning / rule |
|---|---|
| relation_id, version | Stable identity and dated amendment |
| source_id, receiver_id, ports | Entities and input/output types; aspect tags supplement IDs |
| relation_kind | Flow, enabling constraint, information, authorization, allocation or other justified type |
| mechanism | Plain-language causal statement plus canonical M pointer |
| interface | Where the relationship is realized |
| input/output semantics | Quantity, units, timestamps, sampling and missing-data treatment |
| existence b_k | 0/1/unknown: structural relation at specified configuration |
| activation g_k | Boolean guard or explicit unknown; does it apply now? |
| functional state z_k | Value and declared domain Z_k |
| law Phi_k | Governing map, inequality, event rule or unresolved placeholder |
| influence w_k | Defined coefficient or sensitivity with units; optional when no scalar is meaningful |
| delay ell_k | Nonnegative latency with units and serial/parallel process interpretation |
| history | Initial history and relevant path dependence |
| service linkage | Affected Q, measurement units and beneficiaries |
| evidence records | Claim, source, exact location, evidence role, contrary evidence |
| epistemic status | E/D/H/P/A/U for each material claim, not a single blanket label |
| uncertainty Xi_k | Parameter intervals/distributions/model alternatives, with provenance |
| validity Omega_k | Domain and failure conditions |
| baseline/test | Rival representation and observable rejection criterion |
| owner/change log | Responsible analyst and modifications |

Availability, confidence and influence are distinct. Do not multiply them into one weight without a derived model. Missing data are recorded as unknown/not measured/not applicable, never silently replaced by zero.

### Copyable dependency record

~~~yaml
relation_id: PT-ACCESS-001
version: "0.1"
status: P
source_id: T_ROAD_ACCESS
receiver_id: P_REPAIR_TASK
source_view: [T, Ph]
receiver_view: [P, Ph]
relation_kind: enabling_constraint
mechanism: Road accessibility constrains the crew's feasible travel time.
interface: route_to_repair_site
ports:
  output: {name: feasible_travel_time, unit: min}
  input: {name: travel_duration, unit: min}
existence: assumed_for_synthetic_case
activation: repair_task_requested
functional_state: {name: route_speed, domain: "nonnegative km/min"}
law: "travel = distance / speed for speed > 0; otherwise unavailable"
delay: {meaning: travel_duration, unit: min}
history: none_in_this_synthetic_case
service: {name: unserved_electrical_energy, unit: kWh}
evidence: []
evidence_gap: Operational route, dispatch and outage records required.
uncertainty: synthetic_inputs_only
validity: Fixed route and speed; no traffic feedback or alternative route.
falsifier: Observed access changes do not affect feasible arrival as modeled.
canonical_mapping: Retain original tuple; map timing fields only after definition audit.
~~~

## 5. Deliverable 4 — composition rules

**C1: Ports.** A source output may connect to a receiver input only when meanings, units, reference frames and timestamps match or an explicit transformation is provided. kW and kWh are not interchangeable.

**C2: Physical balance.** Resource transfers must preserve the applicable balances, with losses/storage represented explicitly. Information copying need not conserve a material quantity; authorization uses logical admissibility conditions.

**C3: Direction.** A directed edge does not create its reverse. Establish reciprocal sector influence from separately supported directions.

**C4: Feedback.** Demonstrating an entity-level cycle requires connecting all intermediate paths. Opposite sector arrows alone can be an aggregation artifact. A static cycle is only a potential feedback path; guards and delays determine temporal feasibility.

**C5: Joint prerequisites.** Preserve AND/OR structure. A repair requiring crew, permission and access is an AND condition. Alternative routes may form OR conditions. Do not represent joint necessity by unrelated weighted edges.

**C6: Time.** For sequential non-overlapping steps, delays add. For parallel prerequisites, the start of the dependent task is the maximum completion time. Event graphs must be acyclic within an instantaneous scheduling pass, or have explicit iterative/fixed-point semantics.

**C7: Simultaneous coupling.** Cyclic algebraic constraints require a feasible, adequately specified solution method; the grammar does not guarantee existence or uniqueness. Failure to solve is reported, not hidden by an arbitrary update order.

**C8: Shared resources.** One shared crew or budget has one allocation constraint. Joint objectives must not imply authority that operators do not possess.

**C9: Uncertainty.** Preserve common drivers and parameter dependence. Do not multiply independent probabilities unless independence is justified. A scenario proportion is not automatically a real-world probability.

**C10: Aggregation.** Every collapsed edge retains the underlying entities, mechanisms and aggregation rule. Aggregating delays or capacities must follow mechanism semantics.

Composition is therefore a partial operation: incompatible records return a documented error rather than an assembled model. Compatible syntax is necessary but insufficient for physically valid composition.

## 6. Deliverable 5 — dynamic semantics

Let Y contain uniquely owned physical, informational, organizational and interface states. Let m denote operating mode, v algebraic variables, u interventions, h external drivers, and theta parameters. Y_t denotes required history.

A proposed general host form is:

```math
\dot Y=f^m(Y,v,u,h,t;\theta),\qquad
0=G^m(Y,v,u,h,t;\theta),
```

```math
(Y^+,m^+)=R_e(Y^-,m^-,u,h,t)
\quad\text{when guard }\gamma_e\text{ is satisfied}.
```

Replace Y by the needed history Y_t in laws with explicit delay. Supply initial history, consistent algebraic initial conditions and rules for simultaneous events. The host form is a model contract, not a theorem that every assembled system has a unique solution.

For an activated relation:

```math
r_k(t)=\Phi_k(Y_t,z_k,m,u,h;\theta_k),
\qquad b_k=1,\quad g_k=1.
```

Inactive behavior must be explicitly defined. For a flow it may be zero; for access it may be unavailable, not zero travel time.

Information is represented through observations, time stamps, freshness, errors and estimation. Organization enters through event guards, authority, queues and resource constraints, for example:

```math
u(t)\in\mathcal U(\widehat X(t),z_I(t),z_O(t)).
```

This expression does not replace a justified decision policy. A command must connect to an actuator or human action before a physical consequence is asserted.

Services are explicit outputs:

```math
Q_r(t)=q_r(Y(t),v(t),u(t),h(t)).
```

A declared service threshold is an engineering requirement, not a value inferred merely from network topology.

### Knowledge and physical dynamics are separate

Track accepted relations and known candidates in separate versioned registries. Record overall incompleteness as an unresolved limitation. A physical dependency does not begin to exist when an analyst discovers it.

Candidate workflow: detect anomaly → propose rival explanations → identify mechanism → collect independent evidence → assess confounding and validity → accept/reject/retain unresolved. Latent but evidenced relations can remain accepted while inactive.

## 7. Deliverable 6 — executed verification cases

All numbers are invented synthetic inputs [A] used for verification, not measurements or calibrated parameters. No thesis hypothesis is confirmed by these cases.

### Case A: cross-sector feedback structure

Candidate loop:

feeder → traffic signal → road access → power repair task → feeder.

Each arrow is an assumed relation for a graph-semantic test. The code verifies path closure, not the physical validity of these mechanisms. Counterexample: P1 → T1 and T2 → P2 produce reciprocal sector arrows without an entity-level loop.

### Case B: information, organization and transport access jointly affect restoration

Assume one repair task, one fixed route, constant travel speed, independent parallel information/crew-readiness prerequisites, serial authorization after both prerequisites, and no repair until arrival. All times are minutes:

```math
T_R=\max(T_I,T_{\mathrm{ready}})
+T_O+\frac{L}{v_T}+T_{\mathrm{repair}}.
```

Assume L = 12 km, repair = 30 min, information = 2 min, readiness = 3 min, authorization duration = 1 min and v_T = 0.6 km/min. Then T_R = 54 min.

| Perturbation | Result | Interpretation within the synthetic model |
|---|---:|---|
| Baseline | 54 min | Parallel prerequisites are counted once |
| Speed reduced to 0.3 km/min | 74 min | The same access relation produces a longer duration |
| Information arrives at 10 min | 61 min | Information becomes the binding prerequisite |
| No authorization | No feasible completion | Zero authority is not represented as a small delay |
| All prerequisites incorrectly summed | 56 min | Rejected: counts overlapping time twice |

For constant 100 kW unmet load until restoration:

```math
E_{\mathrm{unserved}}=100\,T_R/60\quad [\mathrm{kWh}].
```

Baseline loss is 90 kWh; degraded-road loss is 123.333 kWh, an increase of 33.333 kWh [D]. These are analytical consequences of the assumptions. Demand variation, distributed restoration, route choice, probabilistic delays and coupled traffic dynamics are excluded.

### Case C: added water domain

Add entity pump in domain W with the same port/identity grammar. For an idealized steady pump:

```math
\rho gq_WH=\eta P_{\mathrm{electric}}.
```

With rho = 1000 kg/m³, g = 9.81 m/s², H = 20 m, eta = 0.8 and electrical input = 10,000 W, q_W = 0.04077472 m³/s. The code checks equality of hydraulic and converted electrical power.

This is a fixed-head, fixed-efficiency algebraic example [A,D]. It verifies one extension and its balance; it does not establish general transferability or a water-network model.

### Executed results

Python standard-library verification completed: **12/12 checks passed**.

| ID | Check | Outcome |
|---|---|---|
| V01 | Typed P→T endpoints with matching units | PASS |
| V02 | kW/kWh mismatch rejected | PASS |
| V03 | Common hazard does not manufacture a causal path | PASS |
| V04 | One-way relation remains one-way | PASS |
| V05 | Explicit entity-level feedback path closes | PASS |
| V06 | Aggregated reciprocal arrows need not form a loop | PASS |
| V07 | Changed functional conditions change completion time | PASS |
| V08 | Information delay and organizational authority affect feasibility | PASS |
| V09 | Parallel timing differs from naive serial addition | PASS |
| V10 | Restoration time maps to unit-consistent service loss | PASS |
| V11 | Water entity reuses endpoint grammar | PASS |
| V12 | Idealized water example satisfies power balance | PASS |

Scope of verification: selected typing, reachability, scheduling and dimensional consequences. This is not exhaustive verification of the grammar, a causal discovery test, a dynamic network simulation or empirical validation.

## 8. TEST and VALIDATE — hypotheses about the foundation

| Hypothesis [H] | Rival/baseline | Measurable test | Evidence that would count against it |
|---|---|---|---|
| F0-1: the grammar improves consistent description | Plain directed-edge descriptions | Independent analysts encode held-out cases; compare agreement on direction, mechanism, units and prerequisites | No practical agreement gain or greater ambiguity |
| F0-2: explicit timing/activation improves relevant predictions | Static coupling with comparable calibration effort | Held-out restoration/propagation observations; report prediction error and uncertainty | No meaningful improvement or loss of calibration |
| F0-3: records can be reused across cases | Rebuild descriptions from scratch | Measure time, mapping errors and required schema changes | Reuse takes as long or hides consequential assumptions |
| F0-4: added domains require local laws rather than global ontology revision | Sector-specific one-off descriptions | Independent extension case with a new engineering team | Core concepts repeatedly require incompatible redefinition |

These are evaluation hypotheses for the preparatory work, not additions to the canonical H1–H5 set. Effect thresholds, analyst sample size, datasets and statistical rules remain [U]; specify them before confirmatory evaluation.

| Validation level | Current status |
|---|---|
| Source-grounded conceptual positioning | Partial: bounded source access documented |
| Terminology/notation audit | Completed for this proposal; full repository integration pending |
| Selected mathematical/numerical consistency | 12 synthetic checks passed |
| Comparison against realistic rival models | Pending |
| Identifiability and uncertainty propagation | Pending |
| Independent analyst reproducibility | Pending |
| Operational empirical validation | Pending |
| Cross-sector practical transferability | Pending |

## 9. SYNTHESIZE — what survives this first execution

Established foundations motivate interfaces, heterogeneous views and system-level reasoning (E01–E06). They do not establish the novelty of this particular grammar.

The proposal can distinguish directions, retain P/T/I/O roles, encode joint prerequisites, expose temporal effects and add a water example without altering endpoint semantics. That is a bounded consistency result.

The remaining engineering gap to investigate is whether these records can be populated reliably from real evidence and whether they improve prediction, coordination or modeling effort. Unknown relationship discovery, causal identification, parameter inference and large-network composability remain open.

## 10. Integration with the existing thesis

| Existing stage | Foundation supplied |
|---|---|
| 1. Multilayer Structure | Boundary, identity registry and domain/aspect views |
| 2. Causal Mechanisms | Dependency contracts, evidence status and canonical tuple crosswalk |
| 3. Coupled Hybrid Multiscale Dynamics | Ports, history, mode guards, balances and composition obligations |
| 4. Feedback & Control | Observations, authority and resource-constrained action semantics |
| 5. Viability | Explicit service outputs and justified admissibility requirements |
| 6. Resilience-to-Sustainability Transformation Interface | Traceability from operational limits to candidate structural changes |
| 7. Sustainable Transformation Pathways | Versioned architectures and mechanisms for evaluating alternatives |

The sequence LEARN → VERIFY → FORMULATE → DERIVE → TEST → VALIDATE → SYNTHESIZE → ADVANCE governs this work. Verification findings may send us back to definitions. Phase 0 supports the stages iteratively; completion is not claimed for all foundational science.

## 11. Practical handoff and next evidence requirements

A practitioner should be able to:
1. State a service question and system boundary.
2. Register entities once and map their domain/aspect views.
3. Record directed dependency candidates using Section 4.
4. Attach evidence and separate unknowns from zeros.
5. Check units, prerequisites, direction, time and ownership before composition.
6. Select governing laws compatible with the question and available data.
7. Compare against simpler representations and document validity limits.
8. Reuse a versioned record only after reviewing the new application's assumptions.

The next empirical work needs an operational case containing asset/route data, time-stamped outages, information availability, dispatch/authorization records, crew readiness/arrival/repair times and service measures. These are evidence requirements, not a claim that access is available.

Continue the frozen H1 CORE search and screening procedure. Use freshly eligible full texts to populate mechanism records and compare representation choices. Do not alter eligibility or force these illustrative cases into the corpus. Candidate case selection and any protocol amendment require explicit provenance.

**Completion statement:** all six requested foundation deliverables are provided here, and selected synthetic verification has been executed. This version is ready for methodological review and evidence population. It is not a frozen replacement of the thesis, a universal ontology, an empirical result or a proven novel contribution.

## 12. References and retrieval limits

Kivelä, M., Arenas, A., Barthelemy, M., Gleeson, J. P., Moreno, Y., & Porter, M. A. (2014). Multilayer networks. *Journal of Complex Networks, 2*(3), 203–271. https://doi.org/10.1093/comnet/cnu016  
Accessed author record: https://arxiv.org/abs/1309.7233 — abstract and metadata inspected.

Leveson, N. (2004). A new accident model for engineering safer systems. *Safety Science, 42*(4), 237–270. https://doi.org/10.1016/S0925-7535(03)00047-X  
Publication abstract retrieved in foundational lookup; full-text URL https://sunnyday.mit.edu/accidents/safetyscience-single.pdf failed in this execution. Detailed full-text claims remain pending.

Maier, M. W. (1998). Architecting principles for systems-of-systems. *Systems Engineering, 1*(4), 267–284. https://doi.org/10.1002/(SICI)1520-6858(1998)1:4%3C267::AID-SYS3%3E3.0.CO;2-D  
Full-text copy inspected: https://asymmetricleadership.com/wp-content/uploads/2020/04/architectingprinciplesofsystemofsystemsMAIER.pdf

National Institute of Standards and Technology. (2026, August 6). *Cyber-physical systems and Internet of Things foundations.* https://www.nist.gov/programs-projects/cyber-physical-systems-and-internet-things-foundations  
Page inspected 12 September 2026; not a certification standard or assertion of compliance.

Ouyang, M. (2014). Review on modeling and simulation of interdependent critical infrastructure systems. *Reliability Engineering & System Safety, 121*, 43–60. https://doi.org/10.1016/j.ress.2013.06.040  
Publication abstract retrieved in foundational lookup; full-text retrieval failed in this execution.

Rinaldi, S. M., Peerenboom, J. P., & Kelly, T. K. (2001). Identifying, understanding, and analyzing critical infrastructure interdependencies. *IEEE Control Systems Magazine, 21*(6), 11–25. https://doi.org/10.1109/37.969131  
Full-text author-uploaded copy inspected, printed pp. 13–16; broader article not exhaustively extracted.

## Appendix A — Reproducible verification code

Save the following as phase0_verify.py and run with Python 3. Only standard-library modules are used. The code uses synthetic inputs and produces 12 results; changing the assumptions requires a dated amendment.


```python
import json
from math import isclose

results = []
def check(name, predicate, detail):
    if not predicate:
        raise AssertionError(name)
    results.append({"case": name, "status": "PASS", "detail": detail})

# Typed relation endpoints use entity IDs; aspects are views, not new assets.
def valid_relation(src, dst, registry, unit_out, unit_in):
    return src in registry and dst in registry and unit_out == unit_in

entities = {"feeder": ("P", "Ph"), "charger": ("T", "Ph"),
            "road": ("T", "Ph"), "crew": ("P", "Ph"),
            "traffic_msg": ("T", "I"), "dispatch": ("P", "O")}
check("V01 typed endpoints",
      valid_relation("feeder", "charger", entities, "kW", "kW"),
      "Power-to-transport connection accepts matching port units.")
check("V02 incompatible units rejected",
      not valid_relation("feeder", "charger", entities, "kW", "kWh"),
      "Energy cannot replace power without an explicit conversion law.")

def reachable(edges, start, target):
    seen, frontier = {start}, [start]
    while frontier:
        node = frontier.pop()
        for a, b in edges:
            if a == node:
                if b == target:
                    return True
                if b not in seen:
                    seen.add(b)
                    frontier.append(b)
    return False

hazard_edges = [("hazard", "feeder"), ("hazard", "road")]
check("V03 common cause",
      not reachable(hazard_edges, "feeder", "road") and
      not reachable(hazard_edges, "road", "feeder"),
      "Shared hazard does not create a directed causal path between assets.")
one_way = [("feeder", "charger")]
check("V04 directionality",
      reachable(one_way, "feeder", "charger") and
      not reachable(one_way, "charger", "feeder"),
      "A one-way dependency is not reciprocal.")
loop = [("feeder", "signal"), ("signal", "road"),
        ("road", "crew"), ("crew", "feeder")]
check("V05 component-level cycle",
      reachable(loop, "feeder", "road") and
      reachable(loop, "road", "feeder"),
      "A cycle closes through explicit component paths.")
disconnected = [("P1", "T1"), ("T2", "P2")]
check("V06 aggregation counterexample",
      not reachable(disconnected, "T1", "P1") and
      not reachable(disconnected, "P2", "T2"),
      "Opposite sector arrows do not prove an entity-level feedback loop.")

# Arrival time = maximum of prerequisites + authorized decision + travel + repair.
def restoration(info, ready, decision, distance, speed, repair, authorized=True):
    if not authorized or speed <= 0:
        return None  # no feasible completion in this model
    return max(info, ready) + decision + distance / speed + repair

normal = restoration(2, 3, 1, 12, 0.6, 30)
degraded_road = restoration(2, 3, 1, 12, 0.3, 30)
degraded_info = restoration(10, 3, 1, 12, 0.6, 30)
check("V07 functional dynamics",
      isclose(normal, 54) and isclose(degraded_road, 74),
      {"normal_min": normal, "degraded_road_min": degraded_road})
check("V08 information and organization",
      isclose(degraded_info, 61) and
      restoration(2, 3, 1, 12, 0.6, 30, False) is None,
      {"degraded_info_min": degraded_info, "no_authority": "infeasible"})
check("V09 critical-path timing",
      isclose(max(2, 3) + 1 + 20 + 30, 54) and
      not isclose(2 + 3 + 1 + 20 + 30, 54),
      "Parallel prerequisites use max; serial addition would double-count time.")
# 100 kW unserved until restoration. kW*min/60 = kWh.
check("V10 service consequence",
      isclose(100 * normal / 60, 90) and
      isclose(100 * degraded_road / 60, 370/3),
      {"normal_unserved_kWh": 90, "degraded_unserved_kWh": 370/3})

extended = dict(entities)
extended["pump"] = ("W", "Ph")
check("V11 water extension",
      valid_relation("feeder", "pump", extended, "kW", "kW"),
      "New domain uses the same endpoint and unit contract.")
# Idealized steady hydraulic power: rho*g*flow*head = eta*electric_power.
rho, g, eta, head, power_W = 1000, 9.81, 0.8, 20, 10000
flow = eta * power_W / (rho * g * head)
check("V12 water energy balance",
      isclose(rho*g*flow*head, eta*power_W),
      {"idealized_flow_m3_s": flow, "assumptions": "steady fixed head/efficiency"})
print(json.dumps({"status": "PASS", "passed": len(results),
                  "empirical_validation": False, "results": results}, indent=2))

```

