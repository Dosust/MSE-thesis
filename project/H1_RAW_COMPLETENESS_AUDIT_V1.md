# EGMIV H1 Public-Event Raw Completeness Audit v1.0

**Status:** SOURCE-LEVEL AUDIT COMPLETE — ROW-LEVEL COMPLETENESS NOT YET SUFFICIENT TO FREEZE TRAIN/TEST  
**Date:** 2026-09-14  
**Method:** EGMIV

## 1. Gate purpose

For source `d` and event `e`, completeness is treated as

```math
\mathcal C_{d,e}=(A,T,S,Q,M,V),
```

where `A` = authoritative accessibility, `T` = event-time support, `S` = spatial compatibility, `Q` = required native quantities, `M` = missingness identifiability and `V` = published validation/quality information.

A file's existence does **not** prove validation completeness.

## 2. Event family

| ID | Event | Role |
|---|---|---|
| E0 | Tropical Storm Fay — 2020-07-10 | lower-severity wind/tree event |
| E1 | Tropical Storm Isaias — 2020-08-04 onward | extreme wind/tree restoration event |
| E2 | Dec-2022 wind/rain storm — 2022-12-23 | moderate event |
| E3 | Dec-2023 wind/rain storm — 2023-12-18 | moderate-high; public road closures |
| E4 | Apr-2024 coastal wind/rain storm — 2024-04-03/04 | moderate-high |

## 3. Source-level findings

### NYISO P-58B

The official Real-Time Actual Load archive explicitly contains the event months: July/August 2020, December 2022, December 2023 and April 2024. Archive-period availability therefore passes for E0–E4. This establishes file existence, not event-window row completeness.

### TLC HVFHV

The official TLC portal publishes monthly High Volume FHV parquet files for the event months. TLC states that submitted trip records cannot be guaranteed complete/accurate and gives a specific COVID-era submission-extension caveat for 2020. Thus

```math
A_{TLC}=1\not\Rightarrow M_{TLC}=1.
```

Modern HVFHV schemas include request, pickup and drop-off timestamps plus pickup/drop-off taxi-zone IDs. Nevertheless public completed-trip tables do not enumerate every cancelled/unserved latent trip request, so frozen requested OD demand remains a counterfactual reconstruction problem.

### DOT Traffic Speeds

The official dataset has operated since 2017 and contains speed, travel time, status, timestamp, link ID, link geometry, borough and link name. It is suitable for road-state validation but not complete OD-demand truth.

### NYC 311

The 2020-present dataset covers E0–E4 structurally. It is reporting-driven; absence of a 311 record cannot be interpreted as physical absence of an obstruction.

### EAGLE-I

The peer-reviewed EAGLE-I description establishes 15-minute county-level outage records. A critical limitation is explicit:

```math
\boxed{\text{zero-outage rows are omitted}}
```

and a missing county-time record can indicate either true zero outage or a data-collection gap. The dataset does not distinguish those cases.

Therefore

```math
\boxed{\text{absence of an EAGLE-I row}\not\equiv\text{zero outage}.}
```

The public version now extends through 2024, but the peer-reviewed technical-validation statistics relied on here characterize the 2014–2022 release period. E3/E4 therefore carry an extra quality-provenance flag.

### Con Edison / NY DPS

Public official evidence provides event/restoration truth:

- E0: Tropical Storm Fay actual outage jobs = 126 in the Con Edison Isaias filing;
- E1: Isaias filing reports 5,089 outage jobs, 4,378 down wires, 454 damaged poles and region-specific restoration start times;
- E2: public restoration report records nearly 13,000 customers restored with ongoing work;
- E3: public report records tree/wind damage and eight road closures in Bronx/Westchester;
- E4: public reports document large Bronx/Westchester outages and restoration activity.

These are strong event/milestone observations but not individual crew-route/job trajectories.

## 4. Completeness matrix

| Event | NYISO | EAGLE-I | TLC | DOT | 311 | ConEd/DPS | Overall |
|---|---|---|---|---|---|---|---|
| E0 | A | B | B | A/B | B | C | **B / conditional** |
| E1 | A | B | B | A/B | B | A | **B+ / conditional** |
| E2 | A | A/B | A/B | A/B | B | A | **A-/B+; strongest calibration candidate** |
| E3 | A | B* | A/B | A/B | B | A | **B+; strong held-out candidate** |
| E4 | A | B* | A/B | A/B | B | A | **B+; strong held-out candidate** |

`B*` means the 2023/2024 EAGLE-I extension is available but requires separate quality provenance beyond the 2014–2022 peer-reviewed validation characterization.

## 5. Split decision

The preregistered order is

```math
\text{raw completeness}\rightarrow\text{freeze train/test}.
```

The source-level audit proves event-period availability and identifies intrinsic missingness limitations, but event-window row-level timestamp/gap/null/duplicate/spatial-coverage metrics are not yet frozen for all required sources.

Therefore

```math
\boxed{D_{train},D_{test}\ \textbf{remain UNFROZEN}.}
```

A **candidate only**, recorded before model-result inspection, is

```math
\boxed{D_{train}^{cand}=\{E0,E2\}},
```

```math
\boxed{D_{test}^{cand}=\{E1,E3,E4\}}.
```

Rationale: E0 supplies a lower-severity 2020 event; E2 supplies a later moderate event within the peer-reviewed EAGLE-I quality period; E1 is deliberately withheld as the extreme event; E3/E4 are later independent events. No held-out event may migrate to training because of model performance.

## 6. Row-level eligibility rules — frozen before model fitting

- **R1 Timestamp integrity:** parseable timestamps and declared timezone.
- **R2 Event-window support:** pre-event, impact and recovery phases needed for the source's role.
- **R3 Missingness interpretability:** missing values cannot silently become physical zero.
- **R4 Spatial support:** retained observations lie within declared validation geography.
- **R5 Quantity validity:** native fields preserve their physical meaning and units.
- **R6 No held-out repair:** held-out data cannot be imputed/selected using model residuals.
- **R7 Publisher quality flags retained:** known caveats enter uncertainty rather than being deleted.
- **R8 Non-adaptive exclusion:** a data-ineligible event is not moved to training or replaced after seeing model performance.

## 7. Current gate decision

Completed:

```math
\boxed{\text{source existence}+\text{event-period availability}+\text{schema suitability}+\text{intrinsic missingness audit}.}
```

Not yet completed:

```math
\boxed{\text{event-window row-level coverage/missingness quantification}.}
```

Therefore

```math
\boxed{\textbf{RAW COMPLETENESS = PARTIAL / STRUCTURAL PASS}}
```

and

```math
\boxed{\textbf{TRAIN/TEST = CANDIDATE, NOT FROZEN}.}
```

## 8. Next admissible operation

For every downloadable event/source pair, extract immutable event-window metrics:

```math
N_{rows},\ t_{min},\ t_{max},\ \Delta t\text{ distribution},\ \text{null rates},\ \text{duplicate rate},\ \text{spatial coverage}.
```

Then apply R1–R8. Only after this may the candidate split become active. No calibration or confirmatory H1 run is authorized before that gate passes.