# Compendex Q0 v2.2 — Strict Screening Codebook

## Scientific target
Strict primary evidence for **direct Power–Transportation resilience**.

A record is included as `I1` when it is a primary study and materially models both a power-system layer and a transportation-system/network layer, with an explicit coupling/interdependency and an operational disturbance, failure, cascading, restoration, recovery, robustness, or resilience mechanism.

## Codes observed in the 60-record deterministic pilot

| Code | Decision | Meaning used in this run |
|---|---|---|
| I1 | Include | Primary study with explicit direct P–T coupling plus resilience/disruption/restoration/recovery mechanism. |
| E1 | Exclude | Wrong system boundary / no modeled power–transportation coupled infrastructure object. |
| E2 | Exclude | EV/charging/power interaction without a transportation-network layer, or generic multi-infrastructure context without direct P–T coupling as analytical object. |
| E3 | Exclude | Review, cybersecurity perspective, or charging/power exposure without a primary direct P–T resilience model. |
| E5 | Exclude | Non-primary container/overview (book, proceedings volume, review/monograph) for the strict primary Q0 precision corpus. |
| E7 | Exclude | Superseded version/preprint when the published version is present in the corpus. |

## Boundary rules
- EVs used only as loads, batteries, storage resources, or charging demand do **not** automatically make a transportation layer.
- A transportation layer requires network/road/traffic/routing/mobility state, constraints, disruption, or restoration that materially interacts with power.
- Multi-sector papers may be included when both P and T are explicit modeled layers even if gas/communication/etc. are also present.
- Reviews can remain secondary/context candidates but are excluded from strict primary precision.
- Generic interdependent-network theory without a P–T infrastructure case is excluded from strict Q0.
- Screening is broader than later extraction flags: inclusion in Q0 does not imply quantified timescale, dynamic organization, formal viability, or optimized control.
