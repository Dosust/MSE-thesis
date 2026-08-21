# Open Questions and Next Actions — v2

## 1. Immediate next scientific task

Deeply decompose **Chain I** sector-by-sector before freezing the coupled forward model:

```text
Power
→ Water/Drainage
→ Transportation
→ Solid Waste
→ cross-sector interdependencies
→ explicit interface mechanisms
→ dynamic interface laws
→ characteristic timescales
→ hybrid failure/recovery modes
→ well-posedness/stability/sensitivity
→ coupled-model freeze
```

For each sector/interface, document:

- governing equations;
- states and units;
- algebraic constraints;
- constitutive relations;
- boundary/initial conditions;
- admissible controls;
- characteristic timescales;
- failure/recovery modes;
- empirical/benchmark literature;
- mathematical assumptions;
- unresolved questions.

## 2. Forward-model questions

- ODE, DAE, PDE, hybrid system, differential inclusion, or mixed formulation?
- What state space is appropriate?
- What assumptions guarantee existence?
- What assumptions guarantee uniqueness/well-posedness?
- Are discontinuities/switching/Zeno events possible?
- What stability concept matters for the selected operating regimes?
- What parameter/interface sensitivity must be controlled?

## 3. Interface-definition questions

Need an operational distinction among:

```text
network edge
interdependency
interface mechanism
interface state Z_ij(t)
interface parameter theta_ij
interface failure/recovery mode
```

Need units and causal direction for every retained P–W–T–SW interface.

## 4. Dynamic/static approximation questions

Predeclare:

- static baseline `Z_bar`;
- dynamic law for `Z(t)`;
- characteristic timescales;
- state-trajectory error metric;
- viability-boundary error metric;
- service/recovery error metric;
- tolerance for declaring a static approximation acceptable.

## 5. Admissible-set operationalization

Need explicit definitions for:

- `K_phys`;
- `K_service`;
- `K_sus`;
- `K_eq`.

Each needs measurable variables, units, thresholds and aggregation logic.

## 6. Service-to-population/equity map

Before equity constraints are computed, define:

```text
physical state X
→ service S
→ population/group service exposure
→ equity constraint/metric
```

Do not apply equity directly to infrastructure state variables without this mapping unless explicitly justified.

## 7. Identifiability and observation design

Need to determine:

- what is observable in the demonstrator;
- structural identifiability;
- practical identifiability;
- state observability;
- sensor/measurement requirements;
- posterior/confidence uncertainty;
- propagation of identification uncertainty into `V_R` and `C_R`.

## 8. Recovery formulation

Need to freeze:

- target viable set;
- recovery horizon;
- admissible control set;
- disturbance information structure;
- deterministic/robust/stochastic/nonanticipative formulation;
- recovery-time definition;
- resource constraints.

## 9. Reduced-order model

If full-order viability is computationally infeasible, define a reduction whose objective is not merely low trajectory error but **preservation or conservative bounding of viability/recovery decisions**.

## 10. Literature falsification questions

Search directly for precedents answering:

1. Are dynamic infrastructure interfaces modeled as states rather than static edges?
2. Is interface-identification uncertainty propagated into viability/reachability sets?
3. Are static-coupling approximation errors characterized by interface/system timescale ratios?
4. Has viability-boundary deformation been used as interface criticality?
5. Are sustainability/equity constraints imposed as hard viability constraints in coupled infrastructure?
6. Are capture basins/minimum recovery times computed for comparable coupled infrastructure systems?
7. Has waste–drainage–flood plus transport-access feedback been integrated into such viability analysis?
8. Do reduced-order methods provide conservative viability/reachability guarantees in this domain?

A direct precedent closes/narrows the candidate gap.

## 11. Systematic-review status check

Before final novelty freeze, verify whether the declared database workflow is actually complete. Historical plans included Scopus, Web of Science, Compendex, IEEE Xplore, backward citation and forward citation searching.

Do not state completion without current evidence files/exports.

## 12. Monte Carlo preservation task

The three compared packages should be preserved/indexed together if not already fully registered:

- `EXECUTED` alternative stress-test model;
- `FULL_RUN_RESULTS` closest controlling frozen-formula implementation;
- `HIGH_RIGOR_RUN` sensitivity replication.

A final comparison package should preserve ranks/overlaps and method-compliance differences without averaging raw scores across incompatible models.

## 13. Root README correction task

Known notation issue:

- `\nu` should be `u` in the viability-control set and Type-I mapping;
- `\nu_t` should be `u_t` in Type-II mapping.

Also align the short demonstrator wording with `project/THESIS_SCOPE.md`: **urban flooding with waste–drainage–transport feedbacks**.

## 14. Figure-development task

Future mathematical art should prioritize:

- dynamic/static viability-boundary overlays;
- `∂V_R` sensitivity to interface parameters;
- posterior uncertainty mapped to viability probability;
- timescale-regime diagrams;
- recovery-time level sets;
- service-to-population/equity mapping;
- sector-specific interface mechanisms with physical units;
- demonstrator feedback loops;
- reduced/full model viability comparison.

## 15. Scope guardrail

Do not convert the long-term Type I → Type II → Type III research program into an obligation to deliver equal original contributions in one MSE thesis.

The strongest current MSE center remains:

```text
dynamic interface identification/representation
+ coupled dynamics
+ sustainable/equitable viability
+ recovery geometry
```

with control/design as extensions.