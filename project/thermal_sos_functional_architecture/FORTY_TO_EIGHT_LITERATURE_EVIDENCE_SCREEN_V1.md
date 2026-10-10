# Literature evidence screen — provisional 40-to-8 shortlist (2026-10-10)

**Status:** Initial literature-level evidence review; **8 provisional priorities; 0 equipment-specific fully admitted**. Governed by the frozen thermal-only objectives, the full separate Power and Electrified Transportation system definitions, and [40-to-8 component register](FORTY_TO_EIGHT_COMPONENT_SELECTION_REGISTER_V1.md).

**Method:** Adapt the established PIRT importance-versus-knowledge approach and observability/identifiability criteria. Evidence of an existing general physical phenomenon is not evidence of installed equipment, measured control actuation, numerical limits or a validated Power–Transportation thermal interdependency. The cited source may support the class of a candidate but not a joint real case.

## Literature review of eight provisional component classes

| Candidate | Primary evidence and what it proves | Verdict / next gate |
|---|---|---|
| **P02 Oil transformer** | Hilshey et al. (2013): simulated winding/oil heating, ageing and temperature-informed EV charging. IEEE C57.91-2025: oil-transformer thermal loading and cooling guide. | **Strong physical-model precedent.** Actual rating, temperature data and transformer-to-supply operating policy OPEN. |
| **P05 Transformer cooling** | IEEE C57.91-2025 explicitly addresses how different cooling methods affect transformer loading capability. | **Conditional subassembly.** Confirm forced cooling exists; passive ONAN may require only a heat-transfer parameter or P04 radiator, not an independent active fan. |
| **P08 Transformer protection/loading controller** | Hilshey's charger *scheduling* algorithm and Visakh & Selvan's (2023) modeled mitigation do not establish an actual installed transformer thermal relay/controller. | **Most important missing P→T_e gate.** Must obtain implemented utility/manufacturer limits, command/event logs and permissible AC-supply response. |
| **P10 Feeder conductor/cable** | IEEE 738-2023 governs temperature/current calculation for *bare overhead conductors*; IEC 60287-1-1:2023 governs *steady-state insulated cable* current rating and losses. | **Strong electrical/thermal family, conditional thermal state.** Identify overhead versus cable; prove a thermal feeder limit matters to a service output. |
| **T01 DC EVSE converter** | Krama et al. (2026) field-tested an air-cooled fast charger: temperatures, offered vs delivered DC power, efficiency and derating. | **Strong direct class-level experimental precedent.** Device-specific thermal law and synchronized AC-side input/auxiliary power still OPEN. |
| **T04 EVSE cooling** | Krama et al. (2026) documents hot-climate performance of one air-cooled charger; the converter thermal response depends on heat-rejection conditions. | **Moderate supporting physics.** Confirm installed fan/flow/control and cooling electrical demand; otherwise merge with T01. |
| **T09 Charging connector/contact** | Li et al. (2025) used numerical thermal-management analysis for high-power connector heating. IEC 62196-3:2026 governs high-power connector compatibility; it is not proof of an actual temperature-triggered derating rule. | **Weakest of eight for independent thermal modeling.** Require contact T/current-limit/event; otherwise reserve and screen T08 DC cable or T12 BMS instead. |
| **T11 Vehicle battery pack (RESS)** | Gao et al. (2021) reports calibrated/road-tested temperature-dependent electrochemical/BMS modeling; Katrašnik et al. (2021) supplies high-fidelity multiscale mechanisms. | **Strong model family.** Admit a simple energy/SOC equation; introduce battery thermal dynamics only when actual BMS limits alter charging/service. |

## Non-compensatory component-admission gates

- **G0 classification:** distinguish actual device vs parent subassembly vs function, service, interface, instrument; avoid double counting.
- **G1 real case:** compatible topology, nameplate, converter AC/DC port, cooling and site exposure verified.
- **G2 thermal mechanism:** equipment-appropriate conservation, cooling, losses and implemented temperature-to-capability rule, units and uncertainty.
- **G3 direction:** contributor to a qualified Power→Transportation or Transportation→Power thermal-dependent mechanism or indispensable mobility/electricity-service path.
- **G4 materiality:** changes one named SO1/SO2/SO3 quantity of interest compared with a scientifically justified simplified alternative.
- **G5 feasibility:** accessible observations, parameters, observability/identifiability and independent validation/holdout route.

**Literature does not pass G1/G4/G5 by itself.** M0/M1/M2 should be attempted only when their respective interface hypotheses are admissible. An ordinary electrical connection and two temperatures responding to the same heat event are not reciprocal thermal propagation.

## Research and societal assessment chain

**SO1** physical states and independently qualified thermal mechanisms → **SO2** minimum-sufficient electrical and thermal ODE/DAE model → **SO3** critical times, attributable delays and required electricity/mobility services. Evaluate resilience as maintenance/recovery of **services**, not just component survival. Rerun the model for supported **Improve/Adapt/Restore** responses.

**Sustainability pathway 1:** direct environmental, economic and social service consequences under heat versus the reference scenario. **Pathway 2:** additional response consequences versus the heat-only case. Same boundaries, units and indicators. Count cooling energy and intervention cost as potential burdens. SDG 7.3, 9.4, 11.2 and 13.1/13.2 are possible target-level alignments only when an actual indicator supports the link. Charger efficiency is **not** official GDP-based indicator 7.3.1; transformer losses are **not** official 9.4.1 CO2 per value added; vehicle readiness is **not** official 11.2.1 population public-transport access.

## Core verified bibliographic starting points

- Hilshey et al. (2013), IEEE Transactions on Smart Grid. https://doi.org/10.1109/TSG.2012.2217385
- Visakh & Selvan (2023), Sustainable Energy, Grids and Networks. https://doi.org/10.1016/j.segan.2023.101096
- Krama et al. (2026), Energy Conversion and Management: X. https://doi.org/10.1016/j.ecmx.2026.101960
- Li et al. (2025), Applied Thermal Engineering, article 127680. https://doi.org/10.1016/j.applthermaleng.2025.127680
- Gao et al. (2021), Energy, 221, 119688. https://doi.org/10.1016/j.energy.2020.119688
- Katrašnik et al. (2021), Energy Conversion and Management, 236, 114036. https://doi.org/10.1016/j.enconman.2021.114036
- IEEE C57.91-2025 https://standards.ieee.org/ieee/C57.91/7163/
- IEEE 738-2023 https://standards.ieee.org/ieee/738/10207/
- IEC 60287-1-1:2023 https://webstore.iec.ch/en/publication/68118
- IEC 62196-3:2026 https://webstore.iec.ch/en/publication/86314
- Villaverde (2019) identifiability/observability https://doi.org/10.1155/2019/8497093
- UN SDG indicator metadata (2026): https://unstats.un.org/sdgs/metadata/

**Known limitations:** Full paid standards' clauses and every cited article's full text have not all been audited; selected equipment and source-specific data are unknown. No physical experiments, G4 sensitivity tests, or full G5 independent-validation checks have been run. The eight remain **provisional**, not a frozen final four-plus-four selection.
