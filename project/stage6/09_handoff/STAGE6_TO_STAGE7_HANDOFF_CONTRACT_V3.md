# Stage 6 → Stage 7 Handoff Contract v3

**Status:** CANONICAL STAGE-6→7 HANDOFF — RQ/SO/H v4 ALIGNED  
**Effective date:** 2026-09-20  
**Supersedes:** `STAGE6_TO_STAGE7_HANDOFF_CONTRACT_V2.md`  
**Authority:** `project/CANONICAL_RQ_SO_HYPOTHESES_V4.md`

## 1. Handoff object

```math
oxed{
I_{6	o7}^{v3}
=
left(
mathcal A_6^{qual},
Deltamathfrak R,
mathbf r,
mathcal E_{m fx},
mathcal E_{m fy},
Deltamathbf J_{m sus},
mathcal K_{6}^{qualified},
mathbb U_6,
Lambda_6,
Pi_6
ight).
}
```

No field may be silently dropped, merged, scalarized, or relabeled.

## 2. Typed meanings

- (mathcal A_6^{qual}): qualified candidate interventions;
- (Deltamathfrak R): resilience effect;
- (mathbf r): resource requirements in native units;
- (mathcal E_{m fx}): intervention effectiveness records;
- (mathcal E_{m fy}): resource-efficiency records;
- (Deltamathbf J_{m sus}): admitted sustainability consequences only;
- (mathcal K_6^{qualified}): independently qualified requirements/targets with authority status;
- (mathbb U_6): uncertainty representation;
- (Lambda_6): validity and claim ceilings;
- (Pi_6): evidence/provenance map.

```math
oxed{
mathbf r

eq
mathcal E_{m fy}

eq
mathbf J_{m sus}.
}
```

## 3. Per-intervention record

Every candidate record passed to Stage 7 must preserve intervention definition including type, location, timing, scale/capacity where relevant; resilience effect; resource vector; effectiveness; efficiency; admitted sustainability consequences; feasibility evidence; applicable requirements; uncertainty; provenance; validation status; and claim ceiling.

## 4. No hidden weighting

No weighted scalar is passed as a canonical replacement for the typed record unless a separately justified Stage-7 value model authorizes it.

## 5. Requirement status

Retain authoritative hard constraints, adopted hard targets, soft targets, engineering benchmarks, research-sensitivity thresholds, report-only quantities, and blocked/not-applicable statuses distinctly.

## 6. Uncertainty

Pass probabilistic uncertainty only where justified. Otherwise preserve interval, scenario, robust, sensitivity, or epistemically BLOCKED semantics.

## 7. Handoff gate

```math
oxed{
G_{6-HANDOFF}^{v3}
=
G_{mathcal A}land
G_{Delta R}land
G_rland
G_{EFX}land
G_{EFY}land
G_Jland
G_Kland
G_Uland
G_Lambdaland
G_Pi.
}
```

## 8. Claim boundary

Stage 6 reports what interventions change and what consequences follow. Stage 7 determines which alternatives remain defensible under the declared decision model.
