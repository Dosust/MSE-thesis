---
name: thesis-electrical-topology
description: Evidence-controlled electrical network engineering for the active extreme-heat Power System–Electrified Transportation thermal-interdependency thesis; follow the orchestrator and repository canonical governance.
---

# Electrical network engineering

**Prerequisite:** Load `.github/skills/power-ev-thermal-research/SKILL.md` and its current authority/gates before using this module.

## Trigger and objective
Activate when anyone asserts a transformer connects to an observed EVSE, vehicle depot, feeder, household EV meter or public fast charger. Determine physical network topology and directional thermal interface context.

## Steps
1. Collect and provenance-tag official single-line diagrams, GIS feeder identifiers, equipment/circuit IDs, utility commissioning documents, meter locations and voltage levels.
2. Construct a **typed**, directed asset-edge map: transformer HV/LV bus → feeder → service meter → EVSE AC input → DC output / battery charging boundary, with actual site and circuit identifiers. Unknown edges stay OPEN; do not infer from coincident timestamps, generic voltage or geographic proximity.
3. Check voltage transformation, phase count, sign conventions, P/Q/S balance, measured electrical losses, harmonics and protection/thermal limit meaning. Use NetworkX graph checks; use pandapower only with documented physical network data and parameter evidence.
4. For `T_e→P`, confirm a measured charging load contributes to the exact transformer/feeder and address other loads, PV/export, demand confounding and switching states.
5. For `P→T_e`, confirm a thermal-conditioned transformer/feeder limit is *actually enforced/affects feasible charging*, not just coincident with lower charging power.

## Outputs and gate
`asset_topology.csv`, topology diagram with evidence per edge, meter-boundary register, known confounders and direction-specific decision. PASS for a documented electrical connection only; this **does not** automatically pass thermal interdependency validation. Lack of a one-line diagram or equivalent operator evidence is `BLOCKED_EVIDENCE`.

### ECE6378 / RPG Lab overlay (S2)
Practice L2–4 and L10–11: derive per-unit P/Q/S, AC nodal balance, DC/LAC and radial DistFlow assumptions, voltage drop, thermal current rating and N-1 contingency. Reproduce EV impact/violation checks from [RPG Lab's five-notebook DDCP workflow](https://rpglab.github.io/resources/DistGrid-EV-DDCP-Python/) **on its cited benchmark** before transferring to a verified field circuit. Require one-line map and unique bus/edge identifiers for KIT/EVSE claims. Current-rating overload ≠ directly observed transformer temperature; OPF constraint ≠ verified thermal derating action. Export `network_feasibility.csv` and `asset_topology.csv`. See `references/RPGLAB_CODE_TRANSFER_PROTOCOL.md` at orchestrator root.
