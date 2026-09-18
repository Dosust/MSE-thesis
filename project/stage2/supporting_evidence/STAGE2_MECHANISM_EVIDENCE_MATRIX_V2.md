# Stage 2 Mechanism Evidence Matrix v2

**Status:** ACTIVE PRIOR-EVIDENCE MAP — NOT A CAUSAL-ACCEPTANCE TABLE  
**Date:** 2026-09-18  
**Primary ledger:** `STAGE2_CLAIM_LEVEL_EVIDENCE_LEDGER_V2.md`

## 1. Codes

| Code | Meaning |
|---|---|
| `D` | direct mechanism precedent |
| `S` | supporting structural/method precedent |
| `A` | activation/context evidence |
| `T` | timing/delay/travel evidence |
| `U` | uncertainty precedent |
| `P` | parameter/heterogeneity precedent |
| `O` | organizational/logical evidence |
| `F` | useful for falsification/alternative-explanation design |
| `—` | not relied upon |

These codes describe **evidence role**, not evidence strength or causal probability.

## 2. Matrix

| Source | P→T signal power | P→T charging service | T→P repair access | T→P charging demand | T→P V2G/mobile support | Org/info mediation | Main Stage-2 use |
|---|---|---|---|---|---|---|---|
| Rinaldi et al. (2001) | S/A/F | S/A/F | S/A/F | S/A/F | S/A/F | S/O/F | dependency/context taxonomy; common-cause guardrail |
| McNally et al. (2007) | S | S | S | S | S | S | case/entity/interface mapping |
| Ouyang (2014) | S | S | S | S | S | S | method selection; alternative modeling families |
| Filippini & Silva (2014) | S | S | S | S | S | S | functional exchange/service semantics |
| Nan & Sansavini (2015) | S | S | S | S | S | O | multilayer technical/control/organizational structure |
| Zhou et al. (2020) | S | S | S | S | S | S | interface variables/parameters |
| Hruska et al. (2021) | S | S | S | S | S | S | source→service/flow→receiver dependency profiles |
| Fotouhi et al. (2017) | **D/A** | S | **D/A/T** | — | — | — | direct coupled traffic-power mechanisms |
| Anokhin et al. (2021) | — | — | **D/A/T/U** | — | S/A | — | disrupted-route/mobile-resource restoration mechanism |
| Zhu et al. (2021) | **D/A/T/U/F** | — | — | — | — | — | explicit power-loss→signal-loss→traffic-capacity model; exposes non-transferable outage-to-signal assumption |
| Yu et al. (2025 issue) | — | — | — | — | — | **O/A/U/F** | rule-mediated paths and evidence-scope caveats |
| Lu et al. (2025) | — | S/P/U | — | **D/P/U** | — | — | charging/FCS heterogeneity and later parameter sensitivity |
| Zhang et al. (2025) | **D/A/T** | — | **D/A/T** | — | — | S | phase-specific bidirectional power-road mechanism |
| Shi et al. (2024) | — | — | **D/T/U/P** | — | — | — | stochastic traffic-congestion/travel-time uncertainty |
| Fan et al. (2024) | — | — | **D/A/T** | — | — | — | road-state-constrained repair routing/restoration feasibility |
| Repair-sequencing study (2025), DOI 10.1080/10286608.2025.2602872 | **D/A/T** | — | **D/A/T** | — | — | — | two-way signal-outage and crew-arrival mechanism in one model |
| Liu et al. (2026) | — | — | **D/A/T/U** | — | S/A | — | real-time MEG routing/travel time affects distribution restoration |
| Yan et al. (2024), DOI 10.1002/est2.681 | S | — | S/A | — | S/A | — | mobile energy-storage support possibilities; not direct thesis V2G proof |

## 3. P0 evidence interpretation

### P→T signal power

The active evidence base is now sufficient to justify **case testing of the mechanism family**, because multiple studies explicitly represent power-service failure affecting traffic signals and traffic-system performance.

It is **not** sufficient to establish the thesis-case relation because equipment connection, backup supply, thresholds and fallback modes remain case-specific.

### T→P repair access

The active evidence base is sufficient to justify **case testing of the mechanism family** because multiple studies explicitly constrain repair/mobile-resource routing by road connectivity, travel time or road state.

It is **not** sufficient to establish the thesis-case relation because the exact target asset, task, crew/resource, access point, route set and alternatives remain case-specific.

## 4. P1 evidence boundary

`M2-PT-02` and `M2-TP-02` retain relevant charging/FCS precedent but require dedicated operational and case evidence.

`M2-TP-03` remains the weakest direct-evidence mechanism in the active core. Mobile-energy-resource literature can support the broader mechanism family, but it must not be relabeled as direct EV-based V2G evidence without explicit bidirectional EV/EVSE/aggregator evidence.

## 5. No ranking rule

~~~math
\boxed{
D,S,A,T,U,P,O,F
\neq
\text{weights}
\neq
\text{probabilities}
\neq
q_e^{evid}
}
~~~

This matrix is categorical traceability only.
