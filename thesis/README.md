# ASU MSE Thesis Document Architecture — Current Direction

**Thesis title:** **Physics-Based Mathematical Engineering of Power–Transportation Interdependencies for Resilience**  
**Degree:** Master of Science in Engineering (MSE), Sustainable Engineering  
**Current-scope authority:** [`../project/CANONICAL_EXTREME_HEAT_STATE_TIME_SCOPE_AMENDMENT_V1.md`](../project/CANONICAL_EXTREME_HEAT_STATE_TIME_SCOPE_AMENDMENT_V1.md)  
**Status date:** 2026-10-06

## Governing distinction

```text
scientific architecture ≠ document architecture
```

The scientific architecture defines what is modeled and tested.  
The thesis architecture defines where evidence, mathematics, methods, results, and limitations are written.

ASU Graduate College, SSEBE, and committee requirements remain higher authority for degree and format requirements.

---

## Current thesis storyline

```text
Extreme heat
→ selected physical states
→ Power–Transportation interface mechanisms
→ state-time evolution
→ critical transitions / propagation
→ electricity + mobility service
→ Improve / Adapt / Restore
→ resilience outcome
→ learning
```

The current thesis emphasizes **state and time** rather than the earlier broad all-domain architecture.

---

## Current chapter architecture

| Chapter | Current intended scientific output |
|---|---|
| 1 — Introduction | extreme-heat context, narrowed problem, evidence-qualified gap, scope, current framework, revised RQ/objective/hypothesis set once frozen |
| 2 — Literature & Theory | heat effects, selected component physics, P–T interdependency, state-time/resilience theory, closest comparators, novelty boundary |
| 3 — Conceptual & Mathematical Framework | system boundary, interface architecture, state vector, dynamics, constraints, transition time, propagation delay, service mapping, intervention semantics |
| 4 — Methodology | evidence qualification, selected case/data, minimum-sufficient physics, matched baselines, simulation/estimation, VVUQ, intervention experiments |
| 5 — Results | state trajectories, threshold times, propagation timing, service consequences, intervention effects, uncertainty |
| 6 — Discussion | mechanisms, service meaning, literature comparison, scope/validity limits, engineering implications |
| 7 — Conclusion | RQ closure, contribution boundary, limitations, future mathematical/engineering work |

---

## Chapter 3 mathematical spine

```math
H(x,t)
\rightarrow
X(t)
\rightarrow
\{\tau_i^C,\delta_{ij},Q_P(t),Q_T(t)\}
\rightarrow
\{\text{Improve},\text{Adapt},\text{Restore}\}.
```

with

```math
X(t)=[X_P^\top,Z^\top,X_T^\top]^\top.
```

Chapter 3 must distinguish:

```text
external forcing
≠ physical state
≠ interface architecture
≠ interface state
≠ function
≠ service
≠ engineering action
```

---

## Chapter 4 methodological spine

```text
qualify mechanism
→ select minimum-sufficient physics
→ define states + constraints
→ define matched heat scenarios
→ compute state-time trajectories
→ extract transition / propagation / service quantities
→ apply Improve / Adapt / Restore
→ verify
→ validate
→ quantify uncertainty
→ compare engineering decisions
```

A successful simulation is not validation.

---

## Current reconciliation status

The September 2026 Chapter-I, seven-stage, RQ/SO/H, Austin/P3, broad I/O, and broad sustainability-decision materials are retained as historical/provenance unless explicitly re-admitted.

The final narrowed RQ/SO/H set is **OPEN** and must be rewritten/frozen before confirmatory execution.

Historical entry-point snapshots are preserved under:

`../archive/readme_versions/2026-10-06_pre_reconciliation/`

---

## Current scientific entry points

- [Current scope amendment](../project/CANONICAL_EXTREME_HEAT_STATE_TIME_SCOPE_AMENDMENT_V1.md)
- [Current authority index](../project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md)
- [Decision/freeze protocol](../project/RESEARCH_DECISION_AND_FREEZE_PROTOCOL_V1.md)
- [Conceptual framework V2](../project/CONCEPTUAL_FRAMEWORK_SPEC_V2.md)
- [Scientific writing/inference standard](00_governance/SCIENTIFIC_WRITING_AND_INFERENCE_STANDARD_V1.md)

---

## Preservation rule

No earlier chapter authority is deleted.

When a scientific authority changes:
1. preserve the prior whole version;
2. record its blob/commit identity;
3. create a versioned successor/amendment;
4. state what changed and what did not;
5. retain navigable historical provenance.
