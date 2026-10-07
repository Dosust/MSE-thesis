## 1.6 Scope, Boundaries, Assumptions, and Validity Domain

> **Active-scope override — 2026-10-07.** The September text below is retained as a frozen provenance snapshot. Current thesis work is controlled by `../../project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md`, `../../project/CANONICAL_THERMAL_INTERDEPENDENCY_SCOPE_V1.md`, and `../../project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V3.md`. The active scope is **thermal interdependencies only** and their consequences through **state and time**. Extreme heat is the active hazard; battery-electric road transport is a bounded application subset; non-thermal Power–Transportation interdependencies are outside the active research scope except where required to represent a thermal mechanism; mobility service remains distinct from the technical system.

The thesis is deliberately bounded to the Power–Transportation problem defined by the research questions. It is not intended to reproduce every physical, behavioral, institutional, economic, or environmental process affecting infrastructure.

### Electrified Transportation System boundary

> **In this thesis, the electrified transportation system comprises the electrically propelled road vehicle, its rechargeable energy-storage system, electric propulsion and auxiliary electrical systems, the vehicle power-supply circuit, electric-vehicle supply equipment, the physical charging connection, and the communication and control functions required for electrical power transfer, including bidirectional transfer where supported (ISO 6469; ISO 5474; ISO 15118; IEC 61851; IEC 62196).**

This boundary is controlled by `project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md`. EVSE and the physical charging connection belong to the Electrified Transportation System `T_e`; the external Power system remains distinct. Power–Transportation interface/coupling variables represent cross-system exchange, constraints, or dependency conditions and do not define a third physical infrastructure system.

| BoundaryIncludedNot inferred or outside the confirmatory core |                                                                                |                                                                    |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------ |
| Physical infrastructure                                       | Power + Electrified Transportation                                              | Other physical infrastructure sectors                              |
| Supporting domains                                            | Information + Organization                                                     | Automatic treatment of `I` and `O` as equivalent physical networks |
| Primary services                                              | Electricity + mobility                                                         | Universal welfare or comprehensive societal-service modeling       |
| Interaction                                                   | Qualified `P\rightarrow T` and `T\rightarrow P` mechanisms                     | Co-location or common exposure treated as dependency               |
| Hazard                                                        | Extreme heat as the active hazard, subject to model/data qualification          | Generalization to all hazards                                      |
| Intervention                                                  | Operational/recovery control and persistent engineering interventions          | Unbounded intervention families                                    |
| Resources                                                     | Qualified direct cost and operational energy                                   | Complete economic accounting                                       |
| Environmental consequence                                     | Qualified `CO_{2e}` within the declared boundary                               | Full life-cycle sustainability assessment                          |
| Distributional quantity                                       | Accessibility where construct and data requirements are satisfied              | Broad social-sustainability index                                  |
| Validity                                                      | Tested systems, mechanisms, ranges, scenarios, and accounting boundaries       | Universal generalization                                           |

The physical core is `P+T_e`, with `T_e` restricted to the canonical Electrified Transportation System boundary defined above. Information and Organization affect observation and feasible action but are not treated as independent physical infrastructure networks unless a specific experiment requires such a representation.

The principal service boundary is electricity and mobility. Physical states are represented only to the fidelity required to determine these services, qualified dependency mechanisms, disturbance effects, and feasible Improve/Adapt/Restore actions. Canonical system-scope membership does not require equal-fidelity modeling of every listed transportation component; model activation remains governed by minimum sufficient physics.

The spatial boundary is the geographic support over which Power, Transportation, hazard, observation, and interface data can be aligned with sufficient provenance. Geographic co-location alone does not establish dependency.

The temporal boundary distinguishes data vintage, disturbance time, causal delay, characteristic timescale, simulation horizon, and recovery horizon. These quantities serve different scientific purposes and are not treated as interchangeable.

Extreme heat is the active hazard under the current thesis scope, subject to Chapter 4 model/data qualification. Thermal exposure is distinguished from physical-state change, derating or degradation, component/interface transition, and service consequence. Common heat exposure of Power and Electrified Transportation therefore does not by itself establish a Power–Transportation dependency or interdependency.

The thesis also distinguishes the evolving physical state `Y(x,t)`, operational or recovery control `u(x,t)`, and persistent engineering intervention `a_k`. Operational control changes how existing infrastructure is used; a persistent intervention can alter structure, capacity, redundancy, resource availability, or operating capability.

Development testbeds can support implementation, mechanism exploration, numerical verification, and methodological development without defining the final empirical validity domain. Case selection, data provenance, spatial and temporal alignment, parameter readiness, and confirmatory admissibility are therefore established in Chapter 4.

Uncertainty can arise from hazards, dependency mechanisms, model form, parameters, observations, interventions, resource estimates, and accounting assumptions. Probabilistic representations are used only where their probability semantics are defensible. Otherwise, uncertainty is represented through scenarios, bounds, sensitivity analysis, or robust formulations.

All final claims are restricted to the systems, mechanisms, parameter ranges, hazards, observations, interventions, accounting boundaries, and validation evidence actually examined.

The governing inference rule is

```math
\boxed{ \operatorname{Strength}(\text{claim}) \le \operatorname{Strength}(\text{supporting evidence}). }
```
