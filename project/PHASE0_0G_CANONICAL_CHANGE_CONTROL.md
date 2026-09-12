# Phase 0G — Canonical Change-Control Plan

**Status:** AUTHORIZED CHANGE SCOPE AFTER FINAL THEORETICAL GATE  
**Decision source:** `PHASE0_0G_FINAL_THEORETICAL_DECISION.md`  
**Purpose:** translate the 0G decision into a controlled versioned update without altering components that 0G retained.

---

## 1. Authorized change

Only the Stage-2 dependency/interdependency representation is authorized for canonical revision.

Current flat form:

```math
\mathfrak I_{ij}^{\alpha\beta}
=
(E_i^\alpha,E_j^\beta,M_{ij},w_{ij},\delta_{ij},\tau_{ij},a_{ij},m,\mathcal H_t).
```

Authorized target form:

```math
\mathfrak d_e^{min}
=
(\mathcal C_e,\Sigma_e,\Pi_e),
```

with

```math
\mathcal C_e=(s_e,p_e^s,r_e,p_e^r,\chi_e),
```

```math
\Sigma_e=(\Phi_e,\gamma_e,\theta_e,\zeta_e),
```

```math
\Pi_e=(\mathcal P_e,V_e,\mathcal U_e).
```

Global realization and service maps:

```math
\mathcal X:\Sigma_e\mapsto\Xi_e,
```

```math
Q=G(Y).
```

---

## 2. Components explicitly retained

The following must remain unchanged during the canonical revision:

```text
canonical ontology/system identity: S={P,T,I,O};
P,T as physical infrastructure systems;
I,O as informational/organizational layers;
seven-stage framework order and role;
separate domain physics F_P and F_T;
current thesis scope centered on Power–Transportation;
0A terminology distinctions;
0B R1–R12 / G1–G5 logic unless a future versioned gate reopens them.
```

---

## 3. Field migration table

| Existing concept | Canonical treatment after revision |
|---|---|
| source/receiver | retained in `C_e` |
| interface/interaction point | made explicit through `p_e^s,p_e^r` |
| exchanged quantity/signal/authority | retained as typed carrier `chi_e` |
| mechanism `m` | formalized as coupling/transition operator `Phi_e` |
| activation/context `a,c` | represented through guard/context `gamma_e` |
| delay/latency | mechanism parameter/operator history in `theta_e`/`Sigma_e` |
| dependency state `z` | optional internal state `zeta_e` |
| history `H_t` | optional state/history-domain semantics in `Sigma_e` |
| uncertainty/evidence | structured in `Pi_e` |
| relation class `rho` | derived/reporting classification |
| structural indicator `M` | derived from edge/admissibility membership |
| influence weight `w` | derived under declared metric/operating point |
| executable implementation `Xi` | generated/referenced through global `X` map |
| service consequence | evaluated through system-level `Q=G(Y)` |

---

## 4. Canonical files that may require versioned update

The following files should be audited and revised only where they directly contain the old dependency object or its derived semantics:

```text
CANONICAL_SYSTEM_DEFINITION.md
CANONICAL_7_STAGE_FRAMEWORK.md
FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md
MATHEMATICAL_FOUNDATION.md
RESEARCH_HYPOTHESES.md
MINIMAL_SUFFICIENT_EXPERIMENTAL_REALIZATION.md
```

The seven-stage file should receive only notation/object consistency edits if needed; its stage sequence and scientific role remain unchanged.

---

## 5. Required consistency checks after revision

The revision is not complete until all of the following hold:

```text
1. one canonical dependency definition is used everywhere;
2. no active canonical file presents rho, M or w as universally primitive;
3. no file conflates physical dependency state with epistemic evidence status;
4. Phi_e preserves the receiving domain law rather than replacing F_P/F_T;
5. delay/history are represented only when physically/operationally relevant;
6. organizational dependencies can use hybrid/logical semantics without artificial physical-flow equations;
7. execution metadata is distinct from real-world dependency semantics;
8. service consequence remains traceable as Delta d -> Delta X -> Delta Q;
9. old notation remains in provenance files only, clearly marked superseded;
10. Git history records the canonical version increment.
```

---

## 6. Prohibited change creep

The canonical update must not introduce:

```text
- a new ontology;
- an eighth stage;
- new advanced mathematics not required by the dependency problem;
- a new novelty claim;
- empirical claims not supported by calibrated data;
- new dependency fields unless required by an explicit failed consistency test.
```

If any of these becomes necessary, a new gate version must be opened rather than silently expanding v1.0.

---

## 7. Post-revision scientific task

After the canonical revision is complete, the next task is empirical/model validation, not further conceptual expansion.

For selected Power–Transportation dependencies:

```math
\text{evidence}
\rightarrow
\Phi_e,\gamma_e,\theta_e
\rightarrow
\Xi_e
\rightarrow
\Delta X
\rightarrow
\Delta Q.
```

The first calibrated case should contain at least one physical relation, one information-mediated relation, and one organizational/restoration relation so that all three parts of the revised contract are exercised.
