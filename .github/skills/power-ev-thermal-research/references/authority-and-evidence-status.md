# Canonical authority and evidence checkpoint

**Snapshot date:** 2026-11-02. This is a working summary of the user's prior research, **not** a substitute for independently reopening the source and latest canonical authority.

- Frozen current title (see `project/CANONICAL_THESIS_TITLE_V3.md` and `project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md`): **Engineering of Power–Electrified Transportation Interdependencies for Resilience**. Prior "Physics-Based Mathematical Engineering of Power–Transportation ..." titles are historical.
- Frozen active scientific scope: extreme-heat-conditioned **thermal** interdependencies Power System **P** ↔ Electrified Transportation System **T_e** through state and time; GO/SO1–SO3 frozen, exact narrowed RQs/hypotheses/variables and novelty OPEN.
- Full T_e composition is canonical (road vehicles, RESS, propulsion/auxiliaries, supply circuit, EVSE, connection and required controls); do **not** redefine it as EVSE alone or a third system. **System boundary** ≠ mathematical boundary condition.
- Claim-level classes A1–A5 = external authorities; T1 = explicitly thesis-derived; OPEN = unestablished. Equation-level E1–E4 and mandatory adjacent verified citations control.

## Working data situation — do NOT promote beyond actual gate

| Source | Previous observed evidence | Qualification / limitation |
|---|---|---|
| OPSD household 15-minute (2020-04-15) | two co-located German sites with measured EV and grid meter channels; ~116,355 QC-filtered consecutive intervals in prior run | same-premises **electrical** evidence only, original cumulative-meter/quality semantics must be retained; no documented connected transformer thermal channels |
| SINTEF Barug2025 | ~8,592 raw transformer measurements; 8,589 previously complete for conditional modeling | transformer oil/HV hot-spot conditional thermal model PROVISIONAL; prior ambient exposure -19.58 to +25.97 °C, not extreme heat |
| EPFL charger | 61,816 populated charging measurement rows; 1,878 sessions | per-connector/station power boundary and 15% session-energy reconciliation unresolved; no internal EVSE temperatures |
| KU Leuven | 134 real vehicle AC/DC charging sessions; battery BMS minimum/maximum temperature channels | battery thermal calibration **BLOCKED_FOR_PHYSICAL_VALIDATION**; no verified mean pack temperature or true cooling flux; effective conditional hindcasts only |
| KIT campus multi-voltage | candidate synchronized electrical records including EV load | require exact one-line topology, asset/feeder identification, direct thermal sensor list before thermal claim |
| Bus-depot transformer study | reported simultaneous primary/secondary electrical observations | direct thermal measurements and raw data not verified; harmonics/loss inference ≠ measured thermal state |
| Qatar EVSE thermal study | reports charger-internal temperature and heat-induced derating in hot ambient | original raw data request-only; upstream transformer sensors not identified |

**Current decisive blocker:** no single independently verified, same-site, electrically connected, clock-synchronized transformer + EVSE thermal field dataset covering both systems and a measured restriction/service effect. Both **directional** field coupling gates remain BLOCKED. Case-study model exploration may proceed, but every output must declare hypothetical links and model limitations.

## Research plan

1. KIT: authoritative single-line topology and EV charging asset mapping.
2. Bus depot: operator/paper author data access for transformer primary/secondary signals, sensors and protection.
3. Qatar: request timestamped rectifier temperatures, cooling/derating and electrical boundaries; seek upstream feeder/transformer information.
4. Independently qualify SINTEF transformer and KU Leuven battery candidates against external temperature domain, physics/parameter identifiability, holdout baselines, uncertainty.
5. Only then attempt coupled state-time and service consequence claims at their actual evidence tier.
