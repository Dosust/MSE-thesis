# H1 Level 2 — Source and Provenance Register

**Retrieval audit date:** 2026-09-17  
**Purpose:** freeze the public lineage used to construct the Level-2 realistic synthetic spatial twin.

## S1 — SMART-DS Greensboro electrical distribution data

- Dataset: *SMART-DS Synthetic Electrical Network Data OpenDSS Models for SFO, GSO, and AUS*.
- Publisher: Open Energy Data Initiative (OEDI), National Renewable Energy Laboratory.
- Public landing page: https://data.openei.org/submissions/2981
- Role in Level 2: realistic synthetic Greensboro electrical distribution topology, OpenDSS models, geolocation and load-model lineage.
- Evidence status: **SOURCE DATA — SYNTHETIC, NOT OBSERVED UTILITY TOPOLOGY**.
- Claim boundary: OEDI describes these as realistic large-scale synthetic U.S. distribution models and reports validation against thousands of utility feeders for statistical and operational similarity.

## S2 — GreenEVT coupled Greensboro testbed

- Paper: Gustav Nilsson, Alejandro D. O. Aquino, Samuel Coogan, Daniel K. Molzahn, *GreenEVT: Greensboro Electric Vehicle Testbed*.
- arXiv: https://arxiv.org/abs/2305.12722
- Repository: https://github.com/GreenEVT/GreenEVT
- Upstream `main` audited at commit: `6aff1cac48869ccfa0183643979f5f04b04e1124`.
- Role in Level 2: OpenDSS/SUMO co-simulation lineage, Greensboro OSM-derived transport network, vehicle/parcel/bus/road crosswalk workflow, and reproducible data-acquisition path.
- Evidence status: **SOURCE TESTBED / METHODS LINEAGE**.
- Claim boundary: use of GreenEVT does not convert synthetic SMART-DS assets into observed Greensboro utility assets.

## S3 — OpenStreetMap/SUMO transport geometry

- Transport source lineage: OpenStreetMap road data converted to SUMO by GreenEVT.
- Role in Level 2: authentic public road geography and microscopic transport-network geometry.
- Evidence status: **PUBLIC GEOSPATIAL SOURCE + MODEL TRANSFORMATION**.
- Claim boundary: SUMO demand, incidents, repair routes, vehicle behavior and any thesis hazard realization remain model inputs unless separately sourced and documented.

## Frozen provenance rule

For every Level-2 variable or relation, record one of:

```text
SOURCE_DATA
SOURCE_METHOD
DERIVED_FROM_SOURCE
SYNTHETIC_EXPERIMENT_INPUT
CALIBRATED_PARAMETER
UNCERTAINTY_PARAMETER
```

No `SYNTHETIC_EXPERIMENT_INPUT` may be reported as an observed Greensboro value. No Level-2 result may be described as empirical validation of H1.
