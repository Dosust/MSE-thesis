# E-CPTN-TEMP-002 — Ji et al. (2025)

**Status:** ADMITTED WITH ACCESS LIMITATION — CLOSE TEMPERATURE-AWARE CPTN COMPARATOR  
**Date reviewed:** 2026-10-06  
**Source type:** Peer-reviewed Applied Energy article; full publisher text not openly retrievable in this audit  
**Primary use:** novelty-boundary control for temperature-aware FCS selection/routing, FCS energy scheduling, PDN ACOPF, and tri-level coordination

## Source

Ruihang Ji, Mingbo Niu, Shuai Ma, Hao Su (2025),  
"Tri-level collaborative optimization strategy for coupled power and transportation networks considering energy scheduling of fast charging stations,"  
*Applied Energy*, 401(C), 126806.  
DOI: 10.1016/j.apenergy.2025.126806.

## 1. What is directly supported by accessible publisher/indexed material

The paper develops a tri-level CPTN framework:

```text
Upper level:
EV FCS selection + route scheduling

Middle level:
FCS energy scheduling + charging/discharging price

Lower level:
PDN AC optimal power flow + DLMP
```

It explicitly states that the EV FCS selection and route model accounts for:
- temperature effects;
- queue waiting time.

The FCS is treated as a coupling node / microgrid with:
- PV;
- BESS;
- charging/discharging;
- interaction with the PDN.

## 2. Main reported results

The paper reports improvements in:
- total EV cost;
- total carbon emissions;
- PDN total cost;
- charging-station revenue.

Therefore, temperature-aware optimization inside a coupled road-EV / PDN framework is already established.

## 3. Access limitation

The accessible abstract and indexed section snippets do **not** expose enough detail to verify:
- the exact temperature equation;
- whether temperature affects only EV energy use, or also FCS / PDN physical capability;
- the exact parameter provenance;
- extreme-heat range;
- recovery dynamics;
- physical component thermal states.

Do not infer these missing details.

## 4. Thesis consequence

The paper blocks broad novelty claims such as:

```text
temperature-aware EV routing in CPTN is new
temperature-aware FCS selection in CPTN is new
multi-level coordination of EV/FCS/PDN is new
```

The remaining candidate distinction must be narrower and physically explicit.

## 5. Priority action

If institution/library access becomes available, obtain the full paper and extract:

1. exact temperature-dependent equations;
2. temperature range and data source;
3. affected state/parameter;
4. coupling path;
5. objective functions;
6. service metrics, if any;
7. validation method;
8. recovery/adaptation content;
9. assumptions and validity boundaries.

## 6. Freeze impact

**Rejected as novelty:**
- generic temperature-aware CPTN optimization;
- generic temperature-aware FCS route selection;
- generic EV/FCS/PDN tri-level coordination.

**Still open:**
- explicit heat-dependent component state → physical capability → electricity/mobility service → Improve/Adapt/Restore consequence.
