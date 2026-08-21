# Historical Hypotheses vs Current Formal Propositions

The first memory capsule blurred two naming systems. This file separates them.

## A. Current formal proposition registry

The authoritative current repository registry is **P1–P7** in:

- `project/SCIENTIFIC_PROPOSITIONS.md`
- `config/scientific_propositions.yaml`

These are the current formal propositions used by the scientific architecture and QA.

| ID | Current proposition |
|---|---|
| P1 | Dynamic interfaces materially alter resilience/viability geometry relative to static coupling. |
| P2 | Interface identifiability materially affects reliability of inferred viability. |
| P3 | Interface/system timescale ratios govern the validity of static approximations. |
| P4 | Sustainability and equity constraints deform the viable region beyond technical-operability constraints alone. |
| P5 | Recovery geometry contains information not captured by viability alone. |
| P6 | Waste–drainage–flood feedback shifts coupled P–W–T–SW resilience boundaries. |
| P7 | Reduced models used for decision-making must preserve or conservatively bound viability conclusions. |

## B. Historical hypothesis/target labels used in earlier review and ranking work

The earlier literature architecture used:

```text
H0, H1, H2, H3, H4, H5, H6, H7, T1
```

The frozen 325-record ranking prompt itself ranks the dataset-defined targets:

```text
H1, H2, H3, H4, H5, H6, H7, T1
```

It does not rank H0 as a separate CSV target.

## C. Conceptual crosswalk

The following is a **project-memory crosswalk**, not a claim that the IDs are formally identical in every historical document.

| Historical label | Current conceptual meaning in project memory | Closest current proposition |
|---|---|---|
| H0 | Dynamic identified interfaces deform sustainable/equitable viability/recovery boundaries relative to static models. | P1 |
| H1 | Interface identifiability affects viability reliability. | P2 |
| H2 | Interface/system timescale ratio controls static-coupling approximation validity. | P3 |
| H3 | Viability-boundary deformation defines interface criticality differently from conventional topology/flow importance. | **No direct P1–P7 equivalent; retained as separate hypothesis.** |
| H4 | Sustainability/equity constraints deform viability geometry. | P4 |
| H5 | Recovery requires capture-basin/minimum-time geometry beyond viability alone. | P5 |
| H6 | Waste–drainage–flood feedback shifts coupled P–W–T–SW viability/resilience boundaries. | P6 |
| H7 | Optional time-varying admissible regions / multi-hazard or nonanticipative recovery extension in earlier architecture. | **No exact current P1–P7 equivalent; treat as optional/legacy target until redefined.** |
| T1 | Conservative reduced model preserves or bounds projected full-order viability geometry. | P7 |

## D. Why H3 and H7 must not be silently merged

### H3

H3 is specifically about **interface criticality defined by deformation of viability geometry**. P1 only asks whether dynamic interfaces matter relative to static coupling. A system can satisfy P1 without having defined or validated the H3 criticality metric.

### H7

H7 has been used as an optional/extended target in earlier ranking work. Its exact scientific meaning must be frozen before using it in the final thesis. Do not assume that every H7-ranked paper is direct evidence for one unique final proposition.

## E. Ranking-target rule

The closed-corpus Monte Carlo prompt is constrained to the hypothesis tags already present in the CSV:

```text
H1 H2 H3 H4 H5 H6 H7 T1
```

It must not infer or rewrite those tags using later project memory.

## F. Future naming recommendation

For thesis writing and code, prefer **P1–P7** as the current formal proposition IDs.

When discussing earlier review/ranking outputs, retain the original `H1–H7/T1` labels and explicitly state that they are historical ranking targets.

Use the H-to-P crosswalk only as a documented interpretation layer, never as silent relabeling.