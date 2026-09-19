# Real-World Operational Evidence Plan V1

**Date:** 2026-09-19  
**Scope:** thesis-wide, Stages 1–7  
**Status:** ACTIVE METHODOLOGICAL CONTROL

## 1. Objective

Close the gap between mathematical architecture and empirical/operational evidence by requiring every scientific object to identify the real observable, authoritative source, case relationship, uncertainty, and admissible claim it supports.

## 2. Minimum real-world evidence set

The thesis requires 18 controlled reality objects:

| ID | Required reality | Stage use | Minimum evidence |
|---|---|---|---|
| RW-01 | Power-network structure | S1–S3 | feeder/bus/asset topology or declared realistic-synthetic equivalent |
| RW-02 | Transportation-network structure | S1–S3 | road graph, capacities, intersections, signal locations |
| RW-03 | P–T interface locations | S1–S3 | chargers, signal-power points, repair-access relationships |
| RW-04 | Power operating conditions | S3–S5 | load, generation, voltage/power-flow proxies |
| RW-05 | Transportation operating conditions | S3–S5 | flow, speed, queues, travel time |
| RW-06 | EV charging behavior | S2–S5 | session start/end, kWh, kW, charger type/location |
| RW-07 | P→T mechanism evidence | S2–S5 | specifications, outage behavior, operations records |
| RW-08 | T→P mechanism evidence | S2–S5 | charging/load relation; repair-access/restoration evidence |
| RW-09 | Hazard forcing | S3–S6 | observed event intensity, footprint, timing |
| RW-10 | Failure/outage events | S3–S5 | event start, affected assets/customers/service |
| RW-11 | Recovery trajectories | S3–S6 | restoration timestamps, service recovery |
| RW-12 | Measurement/sensor reality | S4–S5 | sensor type, sampling, uncertainty, missingness |
| RW-13 | Information reality | S4–S5 | latency, availability, communications, alerts |
| RW-14 | Organizational reality | S4–S7 | authority, roles, crews, dispatch, coordination |
| RW-15 | Service requirements | S1,S5–S7 | acceptable service/recovery goals and source authority |
| RW-16 | Population/opportunity reality | S5–S7 | population, jobs, critical services, OD structure |
| RW-17 | Intervention reality | S6–S7 | asset size, materials, cost, lifetime, installation |
| RW-18 | Environmental/economic factors | S6–S7 | electricity carbon, materials, energy, costs |

## 3. Cross-stage reality chain

```math
\begin{aligned}
&\text{asset reality} &&\rightarrow S_1,\\
&\text{mechanism reality} &&\rightarrow S_2,\\
&\text{operation + hazard reality} &&\rightarrow S_3,\\
&\text{measurement + information + organization reality} &&\rightarrow S_4,\\
&\text{service + failure/recovery reality} &&\rightarrow S_5,\\
&\text{intervention + lifecycle + social reality} &&\rightarrow S_6,\\
&\text{feasibility + governance + decision reality} &&\rightarrow S_7.
\end{aligned}
```

## 4. Acquisition pathways

Permitted evidence pathways:
- official APIs/open data;
- official reports/plans;
- peer-reviewed or curated research datasets;
- source-backed project datasets;
- formal agency/utility requests;
- authorized restricted data;
- literature/model proxies when explicitly classified as proxy;
- scenario assumptions when explicitly classified as scenario.

## 5. Storage rule

```math
\boxed{
\text{GitHub}
=
\text{code + schemas + manifests + hashes + small admissible data}
}
```

```math
\boxed{
\text{large/restricted raw data}
=
\text{external controlled storage}
}
```

For externally stored data, GitHub must preserve source URL/API, query parameters, retrieval date, version, expected size, SHA-256, license, and acquisition script where possible.

## 6. Acquisition priority

P0: GreenEVT LFS materialization; Stage-3 charging-parameter authority; case-role declaration.  
P1: Greensboro GIS/NCDOT transport; NOAA hazards; NCDOT incidents; charging inventory; utility reliability.  
P2: observed EV charging sessions; Austin event replay; operator procedures.  
P3: Census LODES/ACS; EPA eGRID; intervention quantities/costs.  
P4: restricted SCADA/AMI/crew/communications logs.

## 7. Claim rule

A source may be used only for the role and domain it can support.

Example:

```text
ERCOT hourly system load
SUPPORTS:
- Texas regional power boundary conditions
- regional plausibility envelope

DOES NOT SUPPORT:
- Austin distribution-feeder voltage
- individual EV charging-station power
- Greensboro power operations
```
