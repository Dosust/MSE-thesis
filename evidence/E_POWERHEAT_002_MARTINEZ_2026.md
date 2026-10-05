# E-POWERHEAT-002 - Martinez et al. (2026)

Status: ADMITTED EXTERNAL EVIDENCE
Date admitted: 2026-10-05
Primary use: power-distribution heatwave mechanism, time-resolved operation, service-deficit metrics, probabilistic failure, and operational resilience intervention.

## Source
Martinez, M., Avila, A., Mandal, P., Carr, J. A., Purohit, S., & Khodaei, A. (2026). Grid Resilience Enhancement Under Extreme Heat Wave Events. IET Generation, Transmission & Distribution, 20(1). DOI: 10.1049/gtd2.70362.

## Supported mechanism

Heat-wave trajectory
-> HVAC-driven demand increase
+ temperature-dependent branch derating
-> electrical and thermal stress
-> failure risk and contingency
-> PF/OPF operating state
-> energy not served and voltage-service degradation
-> PV+BESS operational response
-> resilience consequence

## Strong thesis-relevant lessons

1. Extreme heat can act simultaneously on demand and physical network capability.
2. Temperature, demand, branch ratings, contingencies, PV availability, BESS state of charge, and dispatch are updated at 15-minute intervals.
3. Time-resolved simulation is not the same as real-time operation or electromechanical dynamic simulation.
4. Energy Not Served is a clear example of a power-service deficit.
5. Reliability and resilience should remain distinct.
6. Operational intervention should remain downstream of hazard, state, function, and service diagnosis.

## Important boundary

The paper uses quasi-static AC PF/OPF. It explicitly does not model full electromechanical frequency dynamics, inertia, governor response, protection dynamics, communication latency, telemetry loss, cyber contingencies, or controller failures.

Therefore the thesis should use the term time-resolved operation unless an actual online/real-time estimation-control loop is implemented.

## Presentation mapping

- Slide 1: heat can raise electrical demand while reducing network capability.
- Slide 2: power-side heat-to-demand/capability/service models already exist.
- Slide 4: evidence for time-varying temperature -> demand + capacity -> operating state.
- Slide 5: ENS as a service-deficit quantity; reliability and resilience remain distinct.
- Slide 6: precedent for time-resolved PF/OPF with state-dependent limits.
- Slide 7: scenario comparison, probabilistic failure, SOC-constrained intervention, and explicit validity boundaries.
- Slide 8: operational action can be evaluated through service loss rather than component state alone.

## Do not transfer directly

Do not transfer the paper's:
- stress thresholds;
- synthetic household allocation;
- 33-bus numerical results;
- failure weights;
- DER sizes;
- localized frequency proxy as true dynamic frequency.

## Freeze impact

Strengthens:
- extreme heat as a time-varying hazard;
- state/time-dependent power-side capability;
- service-centered assessment;
- reliability is not resilience;
- time-resolved is not real-time dynamic.

Still open:
- exact power component set;
- transportation mode;
- transport-electrification mechanism;
- coupled service metrics;
- exact resilience-capacity label;
- comparator architecture;
- intervention.
