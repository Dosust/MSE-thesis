# H1 Level 2 — Transport Source Recovery Protocol v1.0

**Authority:** subordinate to `PROTOCOL_V1.md`; does not change H1, model definitions, or confirmatory authorization.  
**Status:** `RECOVERY_METHOD_FROZEN_NOT_EXECUTED`.  
**Purpose:** define what is scientifically admissible if the frozen GreenEVT SUMO Git-LFS payload cannot be materialized directly.

## 1. Preferred source remains the frozen GreenEVT byte object

The authoritative transportation object remains:

```text
GreenEVT commit: 6aff1cac48869ccfa0183643979f5f04b04e1124
path: data/sumo_network/greensboro.net.xml
Git-LFS oid sha256: f0c4cd672a7fd74a5ec1e23cbdb34c6828895af52c1210ee981ef72c79fd7b06
size: 351967227 bytes
```

A reconstructed network can never be called byte-equivalent GreenEVT unless the frozen object itself is later obtained and compared.

## 2. Published source-method constraints

The GreenEVT paper states that the transportation network was imported from OpenStreetMap using SUMO `osmWebWizard`. The published rectangular extent is:

```text
south = 35.894145
west  = -80.198958
north = 36.410277
east  = -79.157255
```

The paper reports the following network-level properties:

```text
SUMO nodes:              50,109
SUMO edges:             118,289
signalized junctions:       914
total road length:        28,216 km   [as printed/extracted from Table I]
total lane length:        30,625 km   [as printed/extracted from Table I]
```

These values are **validation invariants**, not sufficient proof of equality.

## 3. Reconstruction branch

If exact LFS materialization remains unavailable, a transport candidate may be generated only from:

1. an explicitly versioned OpenStreetMap snapshot covering the published rectangle;
2. an explicitly versioned SUMO/osmWebWizard toolchain;
3. deterministic command/configuration files committed to this repository;
4. no outcome information from M0/M1/M2.

The candidate must be labeled:

```text
RECONSTRUCTED_TRANSPORT_CANDIDATE
```

until validation is complete.

## 4. Validation gates

The candidate must pass, at minimum:

```text
T1_geometry_bounds
T2_node_count
T3_edge_count
T4_signalized_junction_count
T5_total_road_length
T6_total_lane_length
T7_XML_parse_and_connectivity
T8_reconstruction_provenance
```

`T2`–`T4` are compared directly with the published integer invariants. Length quantities are reported with discrepancy because the publication does not state the rounding convention; no arbitrary tolerance is authorized in this protocol.

If any published invariant differs, the candidate is classified:

```text
RECONSTRUCTED_SURROGATE_NOT_GREENEVT_EQUIVALENT
```

and cannot replace the original GreenEVT transport object for the frozen Level-2 case without a versioned protocol amendment.

Even if every published invariant matches, the strongest admissible classification is:

```text
GREENEVT_BENCHMARK_MATCH_CANDIDATE
```

not `BYTE_EQUIVALENT`, because GreenEVT explicitly notes preprocessing/manual road corrections may be needed and aggregate invariants do not prove edge-level identity.

## 5. Interface/crosswalk boundary

Transport reconstruction does not reconstruct the GreenEVT `UDS.db` crosswalk automatically. Bus→edge and parcel→edge relations must either:

- come from the exact frozen `UDS.db`; or
- be regenerated from the frozen GreenEVT preprocessing algorithm and separately labeled `RECONSTRUCTED_CROSSWALK`.

A reconstructed crosswalk is not observed utility wiring and cannot be promoted to `EVIDENCE_SUPPORTED` merely because it is spatially plausible.

## 6. Use restrictions

A reconstructed candidate may be used for software development, sensitivity analysis, or a separately versioned realistic-synthetic experiment. It may not silently enter the frozen confirmatory H1 pipeline.

```math
\boxed{
\text{published-method reconstruction}
\neq
\text{original GreenEVT bytes}
}
```

Any transition from reconstruction to the primary Level-2 experiment requires an explicit provenance decision recorded before model outcomes are inspected.
