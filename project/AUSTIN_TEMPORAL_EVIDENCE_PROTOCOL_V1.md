# Austin Temporal-Evidence Protocol v1

**Date:** 2026-09-18  
**Case:** `AUS-P5U-2018-V1`  
**Authority:** `CANONICAL_RQ_SO_HYPOTHESES_V3.md`, `AUSTIN_CASE_STUDY_DATA_ADMISSIBILITY_MATRIX_V2.md`  
**Status:** PRE-DATA TEMPORAL SEMANTICS FROZEN

## 1. Purpose

The Austin case mixes an exact 2018 synthetic power benchmark with public transportation/hazard datasets whose publication or current state may be later than 2018. This protocol prevents a current GIS layer from being silently interpreted as 2018 ground truth.

The governing rule is:

```math
\boxed{\text{current availability} \neq \text{historical validity}}
```

Every temporal use must state whether the object is:

```text
EXACT_2018
RETROSPECTIVE_2018_SUBSET
HISTORICAL_2018_OBSERVATION
CURRENT_SENSITIVITY
STATIC_SCENARIO_SUPPORT
```

## 2. Traffic signals

### Source
City of Austin `TRANSPORTATION_signals2/FeatureServer/0`.

The live service is updated daily and is not versioned. It includes `TURN_ON_DATE`, `SIGNAL_STATUS`, `SIGNAL_TYPE`, coordinates, and related attributes.

### Primary retrospective subset
For the 2018 case, the primary signal candidate set is:

```math
\mathcal S_{sig}^{2018*}
=\{s:\operatorname{TURN\_ON\_DATE}(s)\neq\varnothing,\;
\operatorname{TURN\_ON\_DATE}(s)\le 2018\text{-}12\text{-}31\}.
```

This is labeled:

```text
RETROSPECTIVE_2018_SUBSET
```

not `EXACT_2018`.

### Limitation
Because the current layer is non-versioned, signals that existed in 2018 but were later removed may be absent. Therefore this subset is subject to survivorship bias and cannot be used to estimate complete 2018 signal coverage.

### Allowed use
- instantiate at least one evidence-qualified signal location for semisynthetic `P→T` mapping;
- structural/sensitivity analysis of signal-dependent mobility service.

### Prohibited use
- claiming a complete 2018 signal inventory;
- claiming actual 2018 supplying feeder identity;
- inferring actual historical outage behavior from current status fields.

## 3. Radar traffic observations

### Observation source
City of Austin `Radar Traffic Counts` (`i626-g7ub`). The documented historical coverage is 2017-12-16 through 2021-09-09 and the measurement interval is 15 minutes.

The confirmatory candidate observation window is restricted to:

```math
\boxed{2018\text{-}01\text{-}01\le t<2019\text{-}01\text{-}01}.
```

Each observation must retain its `KITS ID`, timestamp, lane/detector identity, volume and any used speed/occupancy field.

### Location source
The `Travel Sensors` dataset (`6yd9-yz29`) is joined by `KITS ID` and is used as retrospective device-location/status metadata. The location table was published later and is not itself an exact 2018 snapshot.

A radar sensor is admissible for 2018 spatial calibration/validation only if:

```text
1. it has ≥1 genuine 2018 radar observation;
2. its KITS ID joins uniquely to a non-null spatial location;
3. its location lies on/near the retained qualified road support under a frozen snap rule;
4. its development/validation role is assigned chronologically or by independent event block;
5. no random row-level split is used.
```

If the location table provides no movement/history field, stationarity of a fixed roadside sensor location is recorded as an explicit assumption, not a verified fact.

## 4. Flood evidence

### Source
City/FEMA-derived FEMA Floodplain layer.

The layer is a static polygon product with `FLOOD_ZONE` and `EFFECTIVE_DATE`. It is not an event-time flood-depth or hydrograph dataset.

### Primary semantics
For the first Austin experiment the flood layer is labeled:

```text
STATIC_SCENARIO_SUPPORT
```

and may be used only to identify spatial susceptibility/exposure and construct a declared synthetic flood scenario.

### Prohibited interpretations
- current polygon geometry is not automatically 2018 flood geometry;
- `FLOOD_ZONE` is not flood depth;
- `EFFECTIVE_DATE` is not event occurrence time;
- overlap does not prove failure;
- common flood exposure does not create a `P↔T` causal edge.

If a historical-event validation claim is later made, an event-specific hazard source with time/depth/intensity information must be separately qualified.

## 5. Temporal gate

Define:

```math
G_{time}=G_{sig}\,G_{traffic}\,G_{flood}.
```

where:

```text
G_sig PASS:
  retrospective signal subset is nonempty inside retained support;
  TURN_ON_DATE missingness is reported;
  survivorship limitation is retained;
  no claim of complete 2018 inventory is made.

G_traffic PASS:
  2018 observations exist for at least one spatially qualified KITS sensor;
  the KITS join is unique/non-null;
  chronology/event-block split is frozen.

G_flood PASS:
  flood polygons intersect at least one retained power or transport asset;
  use remains static scenario support unless separate event evidence is qualified.
```

`G_time=PASS` is necessary but not sufficient for final case admissibility.

## 6. Evidence basis

- City signal service: updated daily, non-versioned; signal layer exposes `TURN_ON_DATE` and current signal attributes.
- Radar Traffic Counts: historical City dataset covering 2017-12-16 to 2021-09-09; `KITS ID` joins to Travel Sensors; 15-minute observations.
- Travel Sensors: retrospective City metadata for removed sensors and their locations/status.
- FEMA Floodplain: static polygon layer with flood-zone classification and effective date.

## 7. Current state

```text
signal source semantics: PASS
signal retrospective extraction: OPEN
radar observation semantics: PASS
2018 radar extraction/join: OPEN
flood semantics: PASS
flood spatial intersection: OPEN
G_time: OPEN
```
