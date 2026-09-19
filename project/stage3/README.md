# Stage 3 — Physics-Based Hybrid Multiscale Dynamics

**RQ3:** *How, when, and where do accepted interdependency mechanisms evolve and propagate through the coupled system?*

**Current status:** `DESIGN/PROTOCOL V2 FROZEN / EMPIRICAL STAGE NOT CLOSED`

## Authority chain

### Design/protocol authority — frozen v2
1. `STAGE3_STAGE2_TO_STAGE3_INPUT_AND_READINESS_CONTRACT_V2.md`
2. `STAGE3_STATE_INPUT_OUTPUT_QOI_ONTOLOGY_V2.md`
3. `STAGE3_SCIENTIFIC_CONSTITUTION_V2.md`
4. `STAGE3_HYBRID_TIME_MULTIRATE_SEMANTICS_V2.md`
5. `STAGE3_MODEL_FAMILY_SELECTION_PROTOCOL_V2.md`
6. `STAGE3_SCENARIO_SCHEMA_V2.md`
7. `STAGE3_UNCERTAINTY_BENCHMARK_VVUQ_PROTOCOL_V2.md`
8. `STAGE3_TO_STAGE4_HANDOFF_CONTRACT_V2.md`
9. `STAGE3_V2_INTERNAL_CONTRADICTION_AUDIT_V1_2026-09-19.md`
10. `STAGE3_DESIGN_PROTOCOL_FREEZE_V2.md`
11. `STAGE3_FINALIZATION_MANIFEST_V2.json`

### Empirical/execution authority — still open
- `STAGE3_EXECUTION_AND_CLOSURE_AUDIT_V1_2026-09-19.md`
- `STAGE3_GATE_RESULTS_V1_2026-09-19.csv`
- `STAGE3_SCENARIO_MATRIX_CAUSAL_COMPATIBILITY_AUDIT_V1_2026-09-19.md`
- `STAGE3_GREENEVT_SOURCE_MATERIALIZATION_STATUS_V1.md`
- `STAGE3_EV_CHARGING_PARAMETER_AUTHORITY_V1.md`
- `STAGE3_EV_T_TO_P_READINESS_AUDIT_V2.md`

The root `project/STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md` is supporting theory/provenance, not active Stage-3 governance.

## Executed empirical closure state

The authoritative execution/closure audit reports:

```text
TOTAL   = 17
PASS    = 1
BLOCKED = 11
OPEN    = 5
```

Therefore:

```math
oxed{	extbf{STAGE 3 = NOT CLOSED}}
```

Scientific classification:

```text
NOT TESTED / BLOCKED BY PREREQUISITE EVIDENCE
```

This is not support for or falsification of H1.

## Accepted causal mechanism

The current GreenEVT/SMART-DS development case has one Stage-2 causal PASS:

```text
EV_T_to_P
```

The source-level GreenEVT audit confirms:

```math
mathcal A_v(t)
=
mathbf1[
ev_v=1
land
charging_start_vle tle charging_end_v
]
```

and

```math
P_b^{new}(t)
=
P_b^{base}
+
N_{EV,b}^{chg}(t)P_{EV}^{chg}.
```

### Q05 parameter authority — updated

For the `C_DEV` source-backed GreenEVT benchmark:

```math
oxed{
P_{EV,0}^{chg}=7.2 {m kW}
}
```

is frozen as the published GreenEVT default.

The source-code 7.5 kW setting is retained as a nonprobabilistic implementation-sensitivity variant:

```math
oxed{
mathcal U_{P_{EV}}^{src}={7.2,7.5} {m kW}.
}
```

This closes `G_theta` and the source-discrepancy component of `G_U` for this declared development benchmark use only. It is **not** empirical Greensboro charger calibration and does not transfer to Austin.

Aggregate Stage2→3 readiness remains:

```math
oxed{
G_{2	o3}(EV_{T	o P},C_{DEV})=BLOCKED
}
```

because exact audited GreenEVT bytes and the required solver stack are not currently bound in the active execution environment for source-backed runtime implementation verification.

## GreenEVT materialization status

```math
oxed{
G_{SRC-ID}=PASS
quad
eqquad
G_{RUNTIME-DATA}=PASS.
}
```

The frozen upstream LFS OIDs match the previously audited full-object SHA-256 values exactly. Source identity therefore passes; current execution-local materialization remains blocked.

## Excluded Stage-2 relations

The following remain excluded from accepted Stage-3 causal coupling:

- `SIGNAL_P_to_T`
- `EV_P_to_T`
- `REPAIR_T_to_P`

## Research-derived Stage-3 execution order

```text
claim/QOI/resolution
→ causal admission
→ interface implementability
→ model-class selection
→ minimal states
→ time/hybrid semantics
→ well-posedness
→ physics/conservation
→ executable coupling
→ multiscale/synchronization
→ stability/boundedness
→ identifiability/uncertainty
→ numerical verification
→ verification/validation
→ QOI freeze
→ matched M0/M1/M2 experiment
```

## Current blocking objects

The H1/Level-2 protocol still has open:
- exact runtime binding of GreenEVT critical LFS objects and solver stack;
- development and held-out feeder freeze;
- complete static flood exposure / feature-matrix qualification;
- hazard values and geometry;
- remaining parameter distributions relevant to activated model components;
- common-random-number seed manifest;
- independent reference;
- exact primary QOI metrics;
- numerical validation thresholds;
- R1–R8 data qualification;
- train/test split;
- UQ convergence;
- repository confirmatory authorization.

No missing item may be replaced with an undocumented default merely to make Stage 3 run.

The existing H1 scenario matrix remains unauthorized for current causal M2 execution until versioned against the v2 generic scenario schema and latest Stage2→3 readiness ledger.

## Preview boundary

The deterministic preview is software verification only. Its queue/memory behavior is not automatically a GreenEVT-qualified Q05 mechanism.

## Design-freeze result

```math
oxed{
G_{3,DESIGN}=PASS
qquad	ext{and}qquad
G_{3,CONTRADICTION}=PASS;(18/18)
}
```

This is architecture closure only. Empirical Stage 3 remains **NOT CLOSED / NOT TESTED**.

## Immediate execution priority

```math
oxed{
	ext{bind exact GreenEVT bytes + solver stack}
ightarrow
G_{impl}
ightarrow
G_{2	o3}(Q05)
ightarrow
	ext{source-backed Stage-3/B2 execution}.
}
```
