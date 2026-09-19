# Stage 3 — Hybrid Time and Multirate Semantics v2

**Status:** CANONICAL STAGE-3 TIMING SEMANTICS — DESIGN/PROTOCOL  
**Effective date:** 2026-09-19  
**Authority:** Stage-3 scientific constitution v2; canonical dependency contract v1.  
**Empirical effect:** none. Numerical clock values remain case-deferred.

## 1. Purpose

Stage 3 contains heterogeneous physical processes, discrete events, dynamic dependencies and potentially multiple numerical solvers. A single undifferentiated notion of time is prohibited.

\`\`\`math
\boxed{
t_{event}
\neq
\delta_e
\neq
\tau_e^{char}
\neq
\Delta t_{solver}
\neq
\Delta t_{comm}
\neq
T_{horizon}.
}
\`\`\`

These quantities may numerically coincide in a particular implementation, but they must not be conceptually identified.

## 2. Timing ontology

| Symbol | Meaning | Scientific class |
|---|---|---|
| \(t\) | physical/simulation time coordinate | independent coordinate |
| \(t_k^{event}\) | time an event occurs/is applied | event timestamp |
| \(\delta_e\) | causal/transmission/operational delay inherent to dependency \(e\), when justified | mechanism parameter/history support |
| \(\tau_e^{char}\) | characteristic physical/process timescale | derived mechanism/system descriptor |
| \(\Delta t_P\) | power-model numerical/update step | numerical resolution |
| \(\Delta t_T\) | transport-model numerical/update step | numerical resolution |
| \(\Delta t_{int}\) | interface/coupling evaluation interval | numerical/coupling resolution |
| \(\Delta t_{comm}\) | co-simulation communication/synchronization interval | numerical architecture |
| \(T_{horizon}\) | experiment horizon | design parameter |
| \(t_{obs}\) | observation timestamp | Stage-4 object when observations are constructed |

Observation arrival/receive timing belongs to Stage 4 unless it is itself modeled as a physical communication process required to generate the Stage-4 observation environment.

## 3. Event semantics

An event is

\`\`\`math
e_k=
(t_k^{event},\kappa_k,\iota_k,c_k,\Pi_k),
\`\`\`

where \(\kappa_k\) is event type, \(\iota_k\) target entity/interface, \(c_k\) cause/trigger, and \(\Pi_k\) provenance.

Events may trigger

\`\`\`math
x^+=R_{e_k}(x^-),
\qquad
m^+=\Delta_m(m^-,e_k),
\qquad
\mathcal G^+=\Delta_{\mathcal G}(\mathcal G^-,e_k).
\`\`\`

A numerical communication time is not automatically a physical event.

## 4. Delay semantics

A dependency delay is admissible only when mechanism/evidence supports it. It may be represented by a history domain inside \(\Phi_e\), or by an equivalent augmented-state representation.

\`\`\`math
\boxed{
\text{memory state}
\neq
\text{duplicate delay bookkeeping}.
}
\`\`\`

If a process is Markovized with an explicit state, a second independent delay representation requires separate justification.

## 5. Characteristic timescale

\(\tau_e^{char}\) describes how quickly a physical/process mechanism materially evolves. It is not a solver step and is not evidence by itself.

A reported characteristic timescale must state definition, units, derivation/estimation, uncertainty, validity domain, and whether it is used for model selection or only interpretation.

## 6. Multirate architecture

Let subsystem clocks be

\`\`\`math
\mathcal T_P,\qquad
\mathcal T_T,\qquad
\mathcal T_{PT}.
\`\`\`

No equality of their numerical resolutions is assumed. The requirement is consistency of exchanged variables, event chronology, and QOI accuracy—not identical clocks.

## 7. Coupling/synchronization operator

For federated/partitioned simulation, define

\`\`\`math
\mathcal S_{\Delta t_{comm}}
:
\{Y_P,Y_T,z_{PT}\}
\mapsto
\{\widetilde Y_P,\widetilde Y_T,\widetilde z_{PT}\}.
\`\`\`

The implementation record must specify:

- communication points;
- interpolation/extrapolation;
- zero/first-order hold behavior;
- event ordering;
- algebraic-loop treatment;
- iteration/rollback policy when used;
- convergence/error assessment.

The communication interval is a numerical design choice, not a physical delay.

## 8. Causal ordering

For active mechanism \(e\),

\`\`\`math
s_e
\xrightarrow{\Phi_e,\gamma_e,\delta_e}
r_e.
\`\`\`

A scheduler may use a computational ordering that is mathematically equivalent, but cannot invert the scientific source→receiver semantics.

## 9. Simultaneous events

If events are simultaneous within numerical resolution, the implementation must predeclare one of:

- mathematically simultaneous update;
- deterministic priority;
- fixed-point/iterative resolution;
- scientifically justified tie-breaking.

The rule cannot be chosen after examining H1 outcomes.

## 10. Numerical-step admissibility

A numerical/update step is admissible only if it supports:

\`\`\`text
QOI resolution
+ event resolution
+ mechanism timescale resolution
+ numerical stability
+ convergence
+ reproducibility.
\`\`\`

No universal step size is frozen here.

## 11. Convergence

For influential numerical clock \(h\), solution verification must evaluate a QOI-sensitive error such as

\`\`\`math
E_h(q)=d_q(q_h,q_{h/ref})
\`\`\`

or an equivalent convergence measure.

Acceptance rules must be frozen prospectively and be context/QOI specific.

## 12. Event convergence

For event-driven QOIs, convergence must consider both output and chronology:

\`\`\`math
\Delta q
\quad\text{and}\quad
\Delta t_{event}.
\`\`\`

Similar integrated service loss does not by itself establish equivalent event propagation.

## 13. Cross-domain synchronization checks

Applicable coupled models must test:

- timestamp consistency;
- unit consistency;
- no duplicate event application;
- balance/conservation at physical interfaces where applicable;
- declared limit/monotonicity behavior;
- communication-step sensitivity;
- reproducibility under identical input/seed manifests.

## 14. Stage-4 boundary

Stage 3 outputs physical truth at sufficient temporal resolution. Stage 4 owns measurement/sampling/availability semantics.

\`\`\`math
\boxed{
\Delta t_{solver}
\neq
\Delta t_{measurement}
\neq
\Delta t_{receive}.
}
\`\`\`

The latter two are Stage-4 quantities unless externally prescribed solely for a Stage-3 validation experiment.

## 15. Source cadence versus physical latency

A cadence observed in existing software is implementation evidence only. It does not become empirical physical latency without independent evidence.

## 16. Deferred fields

Remain DEFERRED until case/model qualification:

- all subsystem/interface/communication step sizes;
- experiment horizon;
- physical/operational dependency delays;
- synchronization interpolation rule;
- event tolerance;
- convergence thresholds.

## 17. Claim boundary

This file freezes timing semantics and numerical obligations only. It does not validate a multirate solver, identify real physical delays, or prove a selected timestep adequate.
