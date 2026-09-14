# EGMIV H1 Demonstrator Qualification v1.0

**Status:** COMPLETE — public demonstrator = PARTIAL PASS  
**Date:** 2026-09-14  
**Method:** EGMIV — Evidence-Grounded Mechanistic Interdependency and Validation

## Decision

The proposed public demonstrator is retained only as a **partial-pass** validation architecture:

```math
\boxed{\mathcal D_{H1}^{public}=\mathcal D_{NYC}\cup\mathcal D_{ACN}}
```

with:

- `D_NYC`: multi-source NYC/Con Edison storm-event arm;
- `D_ACN`: Caltech ACN-Data charging-component arm.

This combination is sufficient for H1a matched representation testing plus aggregate/event and component validation, but it is **not sufficient for the strongest pre-registered H1b claim**.

The validation rules are not weakened to force a full pass.

---

## Audited NYC sources

### NYISO P-58B

Official Real-Time Actual Load archive. August 2020 is explicitly archived. Native resolution is 5-minute real-time dispatch load. Zone J is New York City, but Con Edison tariff documentation shows that parts of the upper Bronx are in Zone I. Therefore public Zone-J load is an aggregate electrical observation, not a one-to-one spatial match to TLC taxi zones or road links.

### EAGLE-I

Public ORNL/Figshare outage dataset covering 2014–2024 at 15-minute county resolution. It provides customer-outage trajectories suitable for outage/restoration timing. Customer-outage fraction is not numerically identical to the frozen demand-weighted power-service metric `S_P`.

### NYC TLC trip records

Public monthly/annual trip data. 2020 and later periods are available. Pickup/drop-off timestamps and taxi-zone IDs support completed OD-flow construction for the TLC/FHV subsystem. Public records represent trips that occurred and do not directly enumerate all latent/unserved/cancelled mobility requests. Therefore requested OD demand still requires an independently validated counterfactual-demand model.

### NYC DOT Traffic Speeds

Public Socrata dataset with speed, travel time, timestamp, link ID, link geometry/polyline, borough and link name. Historical 2020 support is established. It is admissible for road-state validation, not complete OD-demand truth.

### NYC 311

Public 2020-present Socrata data with timestamp, complaint type/descriptor and geography. It can support geolocated obstruction evidence, but is reporting-driven and cannot serve as a complete physical inventory. It must be triangulated with utility/agency records and traffic state.

### Con Edison / NY DPS

Official event/restoration evidence is available. For Tropical Storm Isaias, public materials document the 4 August 2020 event, thousands of downed wires/poles and outage jobs, region-specific start-of-restoration times, prolonged restoration and official restoration milestones.

Public evidence supports the aggregate causal chain

```math
\text{storm}\rightarrow\text{trees/wires/road obstruction}\rightarrow\text{field restoration operations}\rightarrow\text{power restoration}.
```

However, no verified public dataset exposes individual repair-job/crew trajectories of the form

```math
\text{crew/path}\rightarrow\text{departure}\rightarrow\text{arrival}\rightarrow\text{repair start/end}.
```

Therefore microscopic road-to-crew-to-repair validation is not publicly supported.

---

## ACN-Data arm

ACN-Data exposes real charging sessions with connection/disconnection times, done-charging time, delivered kWh, station/site IDs, measured-current time series, pilot-signal time series and optional user inputs such as requested kWh and requested departure. API use requires registration/token access.

This arm is admissible for charger-interface parameterization and component validation:

```math
\lambda_c,\;E_c,\;p_c^{ch},\;\mu_c,\;q_c.
```

But ACN is not temporally/geographically part of the NYC storm events and cannot be represented as same-event system-level truth.

---

## Temporal-overlap decision

For the Isaias system arm, the event window

```math
T_E^{Isaias}=[2020\text{-}08\text{-}04,\;2020\text{-}08\text{-}12]
```

is structurally covered by NYISO, EAGLE-I, TLC, DOT Traffic Speeds, NYC 311 and official Con Edison/DPS event records.

Thus

```math
\boxed{T^\star_{Isaias}\neq\varnothing}.
```

The coarsest confirmed primary observation interval is EAGLE-I at 15 minutes. The candidate validation clock is therefore

```math
\boxed{\Delta_{val}=15\;\text{min}}
```

subject to final raw timestamp inspection. Finer model, NYISO and DOT outputs must be aggregated to this clock; false upsampling is prohibited.

---

## Spatial-overlap decision

Fine-scale spatial compatibility does **not** fully pass.

```math
G_{NYISO\,J}\neq G_{TLC/DOT}
```

at road/taxi-zone scale. Zone J is aggregate and excludes parts of the upper Bronx that belong to Zone I; EAGLE-I is county-level; TLC/DOT operate at taxi-zone/link scale.

Therefore the NYC arm is admissible for aggregate event/state comparison, but not for claims of exact fine-scale P–T spatial co-validation without additional utility/subzone data.

---

## Event family

A single Isaias event is insufficient for confirmatory H1b. The current candidate family for the same broad overhead wind/tree mechanism is:

| ID | Event | Date | Role |
|---|---|---|---|
| E0 | Tropical Storm Fay | 2020-07-10 | lower-severity candidate; 126 outage jobs reported |
| E1 | Tropical Storm Isaias | 2020-08-04 to 2020-08-12 | extreme stress candidate |
| E2 | Dec 2022 wind/rain storm | 2022-12-23 | moderate candidate |
| E3 | Dec 2023 wind/rain storm | 2023-12-18 | moderate-high; public report includes road closures |
| E4 | Apr 2024 coastal wind/rain storm | 2024-04-03 to 2024-04-04 | moderate-high candidate |

Train/test membership remains **unfrozen** until raw completeness, missingness and observation coverage are quantified for E0–E4.

Required condition remains

```math
D_{train}\cap D_{test}=\varnothing
```

with at least two independent held-out validation events for any mechanism class claimed confirmatory.

---

## Hard-gate outcome

| Gate | NYC system arm | ACN arm |
|---|---|---|
| authoritative access | PASS | CONDITIONAL PASS |
| event/time coverage | PASS | N/A same-event |
| exact spatial compatibility | **PARTIAL / FAIL fine-scale** | N/A |
| semantic state mapping | PARTIAL PASS | PASS component |
| disturbance/restoration truth | PASS aggregate | N/A |
| uncertainty quantifiable | PASS in principle | PASS in principle |
| independent event family | PASS candidate family | session-level only |
| microscopic road→crew→repair truth | **FAIL public data** | N/A |
| charger dynamic truth | N/A | PASS |
| direct full H1b `S_P,S_T` truth | **FAIL / PARTIAL** | FAIL system-level |

---

## Scientific adjudication of the demonstrator

### NYC system arm

```math
\boxed{\textbf{PARTIAL PASS}}
```

Admissible for real-event disturbance timing, aggregate outage/restoration trajectories, aggregate grid-load trajectories, TLC-subsystem completed OD trajectories, road-state dynamics, obstruction evidence, restoration milestones and aggregate mechanism validation.

Not admissible, with currently verified public sources, for direct microscopic crew-path/job validation, exact fine-scale P–T spatial co-validation, or fully direct observation of both frozen service metrics without reconstruction/proxy layers.

### ACN arm

```math
\boxed{\textbf{PASS FOR COMPONENT VALIDATION}}
```

but

```math
\boxed{\text{ACN}\not\Rightarrow\text{system-level H1b validation}.}
```

### Full H1b status

```math
\boxed{\textbf{BLOCKED WITH PUBLIC DATA AT THE STRONGEST PRE-REGISTERED LEVEL}}
```

unless additional independent data close the identified gaps.

---

## Missing evidence required to upgrade H1b

1. geolocated utility repair-job/crew logs with timestamps;
2. power-service observations spatially coextensive with the transport domain;
3. sufficiently complete requested-mobility observations or independently validated demand reconstruction;
4. ideally event-linked EV charging observations if charging is claimed at system-event scale.

---

## Next EGMIV gate

Proceed on two parallel tracks.

### Track A — public demonstrator execution

```math
E0\ldots E4
\rightarrow
\text{raw completeness audit}
\rightarrow
\text{freeze train/test split}
\rightarrow
\text{observation operators}
\rightarrow
u_{obs}
\rightarrow
\epsilon
\rightarrow
\text{H1a/UQ}.
```

### Track B — H1b data escalation

Seek restricted/partner data for crew/job trajectories, finer electric service/outage records and mobility request/completion truth.

If Track B fails, H1b must be reported as **not fully testable with public data** rather than upgrading aggregate/component validation into system validation.

---

## Lock statement

```math
\boxed{\text{NYC/ACN is selected as a PARTIAL-PASS public demonstrator, not complete H1b truth.}}
```

This status may be upgraded only by new independent data that pass the already-frozen observation and validation gates.
