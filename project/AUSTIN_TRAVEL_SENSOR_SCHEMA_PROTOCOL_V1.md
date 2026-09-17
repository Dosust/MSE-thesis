# Austin Travel Sensors Schema Qualification Protocol v1

**Date:** 2026-09-18  
**Case:** `AUS-P5U-2018-V1`  
**Dataset:** City of Austin Travel Sensors (`6yd9-yz29`)  
**Role:** retrospective location/status metadata supporting the 2018 Radar Traffic Counts KITS-ID join  
**Status:** FIELD MAPPING OPEN — NO FIELD NAME MAY BE GUESSED

## 1. Scientific purpose

The 2018 Radar Traffic Counts identify sensors through `int_id`, documented by the City as KITS ID. The related Travel Sensors table provides location/status metadata, but the exact API field names used for KITS ID and geometry must be verified from the acquired raw schema/rows before the join is executed.

The governing rule is:

```math
\boxed{\text{semantic relationship} \neq \text{verified API field mapping}}
```

## 2. Frozen source identity

```text
Organization: City of Austin
Dataset: Travel Sensors
Dataset ID: 6yd9-yz29
Resource endpoint: https://data.austintexas.gov/resource/6yd9-yz29.json
Temporal role: RETROSPECTIVE_LOCATION_METADATA
Exact 2018 snapshot: FALSE
Join semantics: Radar `int_id` = City KITS ID ↔ Travel Sensors KITS-ID field
```

The City documentation establishes the semantic KITS-ID relationship. It does not authorize guessing the API field identifier.

## 3. Automated schema-observation step

After raw Travel Sensors rows are materialized, software may compute only:

```text
observed top-level keys;
key occurrence counts;
value-type summaries;
non-null counts;
objects containing recognizable coordinate structures;
raw file SHA-256;
row count.
```

This step is descriptive. It may not silently choose the join or coordinate fields.

## 4. Field-mapping freeze gate

The registry `config/austin_travel_sensor_schema_v1.json` may move from `OPEN` to `FROZEN` only when all of the following are recorded:

```text
raw_data_sha256;
raw_row_count;
observed_keys_sha256;
kits_id_key;
location representation:
  either point_key
  or latitude_key + longitude_key;
evidence_basis;
verification result.
```

Every selected field must be present in the observed raw schema.

For a frozen mapping, the executable gate must verify:

1. KITS values are parseable and nonnegative;
2. KITS IDs are unique in the retained location table or duplicate resolution is explicitly versioned;
3. coordinates are finite WGS84 coordinates after any declared transformation;
4. at least one genuine 2018 radar KITS ID joins to a location;
5. missing joins are reported, never imputed;
6. spatial road-overlap remains a separate gate.

## 5. Prohibited shortcuts

- Do not infer field names from display labels alone.
- Do not select the first numeric column as KITS ID.
- Do not infer latitude/longitude from arbitrary numeric pairs.
- Do not impute missing sensor locations.
- Do not label the Travel Sensors table an exact 2018 snapshot.
- Do not use a random row-level traffic split.
- Do not treat a successful KITS join as coupled-system H1b validation.

## 6. Current state

```text
source identity: PASS
semantic KITS relationship: PASS
raw Travel Sensors materialization: OPEN
observed field schema: OPEN
field mapping: OPEN
2018 radar-location join: OPEN
road spatial overlap: OPEN
G4 traffic observations: OPEN
```
