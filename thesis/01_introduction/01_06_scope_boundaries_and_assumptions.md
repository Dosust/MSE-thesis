## 1.6 Scope, Boundaries, Assumptions, and Validity Domain

> **Active-scope override — 2026-10-07.** The September text below is retained as a frozen provenance snapshot. For current thesis work, system composition and current hazard/state-time scope are controlled by `../../project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md` and `../../project/CANONICAL_EXTREME_HEAT_STATE_TIME_SCOPE_AMENDMENT_V2.md`. In current work, `T_e` means **Electrified Transportation System** as defined by the canonical scope authority; extreme heat is the active hazard; battery-electric road transport is a bounded application subset; mobility service remains distinct from the technical system.

The thesis is deliberately bounded to the Power–Transportation problem defined by the research questions. It is not intended to reproduce every physical, behavioral, institutional, economic, or environmental process affecting infrastructure.

| BoundaryIncludedNot inferred or outside the confirmatory core |                                                                                |                                                                    |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------ |
| Physical infrastructure                                       | Power + Transportation                                                         | Other physical infrastructure sectors                              |
| Supporting domains                                            | Information + Organization                                                     | Automatic treatment of `I` and `O` as equivalent physical networks |
| Primary services                                              | Electricity + mobility                                                         | Universal welfare or comprehensive societal-service modeling       |
| Interaction                                                   | Qualified `P\rightarrow T` and `T\rightarrow P` mechanisms                     | Co-location or common exposure treated as dependency               |
| Hazard                                                        | Flooding as principal planned demonstrator, subject to Chapter 4 qualification | Generalization to all hazards                                      |
| Intervention                                                  | Operational/recovery control and persistent engineering interventions          | Unbounded intervention families                                    |
| Resources                                                     | Qualified direct cost and operational energy                                   | Complete economic accounting                                       |
| Environmental consequence                                     | Qualified `CO_{2e}` within the declared boundary                               | Full life-cycle sustainability assessment                          |
| Distributional quantity                                       | Accessibility where construct and data requirements are satisfied              | Broad social-sustainability index                                  |
| Validity                                                      | Tested systems, mechanisms, ranges, scenarios, and accounting boundaries       | Universal generalization                                           |

The physical core is `P+T`. Information and Organization affect observation and feasible action but are not treated as independent physical infrastructure networks unless a specific experiment requires such a representation.

The principal service boundary is electricity and mobility. Physical states are represented to the fidelity required to determine these services, qualified dependency mechanisms, disturbance effects, and feasible recovery or control.

The spatial boundary is the geographic support over which Power, Transportation, hazard, observation, and interface data can be aligned with sufficient provenance. Geographic co-location alone does not establish dependency.

The temporal boundary distinguishes data vintage, disturbance time, causal delay, characteristic timescale, simulation horizon, and recovery horizon. These quantities serve different scientific purposes and are not treated as interchangeable.

Flooding is the principal planned demonstrator hazard, subject to Chapter 4 qualification. Exposure is distinguished from damage, component failure, and service consequence. A flood footprint can therefore establish potential exposure without establishing failure probability or the resulting system response.

The thesis also distinguishes the evolving physical state `Y(x,t)`, operational or recovery control `u(x,t)`, and persistent engineering intervention `a_k`. Operational control changes how existing infrastructure is used; a persistent intervention can alter structure, capacity, redundancy, resource availability, or operating capability.

Development testbeds can support implementation, mechanism exploration, numerical verification, and methodological development without defining the final empirical validity domain. Case selection, data provenance, spatial and temporal alignment, parameter readiness, and confirmatory admissibility are therefore established in Chapter 4.

Uncertainty can arise from hazards, dependency mechanisms, model form, parameters, observations, interventions, resource estimates, and accounting assumptions. Probabilistic representations are used only where their probability semantics are defensible. Otherwise, uncertainty is represented through scenarios, bounds, sensitivity analysis, or robust formulations.

All final claims are restricted to the systems, mechanisms, parameter ranges, hazards, observations, interventions, accounting boundaries, and validation evidence actually examined.

The governing inference rule is

```math
\boxed{ \operatorname{Strength}(\text{claim}) \le \operatorname{Strength}(\text{supporting evidence}). }
```
