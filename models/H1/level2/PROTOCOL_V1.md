# H1 Level 2 Experimental Protocol v1.0

**Authority:** subordinate to `project/CANONICAL_RQ_SO_HYPOTHESES_V3.md`, `project/CANONICAL_DEPENDENCY_CONTRACT_V1.md`, and repository scientific-governance files.  
**Method:** EGMIV — Evidence-Grounded Mechanistic Interdependency and Validation.  
**Status:** `METHOD_FROZEN_INPUTS_OPEN`.  
**Confirmatory H1 execution:** `NOT AUTHORIZED`.  
**Frozen:** 2026-09-18.

## 1. Scientific purpose

Level 2 is not an intervention comparison. Its H1 purpose is to test whether an evidence-grounded dynamic causal coupling model provides incremental explanatory or predictive information relative to simpler representations under matched Power–Transportation disturbances and initial conditions.

```math
M_0=\text{independent},\qquad
M_1=\text{static/algebraic coupling},\qquad
M_2=\text{dynamic causal coupling}.
```

A larger service loss under `M2` is not evidence against `M2`; it can be the consequence of representing memory, queues, congestion, delayed access, or delayed restoration that a simpler model omits. Conversely, a difference between models is not evidence that `M2` is more accurate. Accuracy requires an independent qualified reference.

The primary H1 direction is therefore

```math
E_q^{(M)}=d_q(y_q^{(M)},y_q^{R}),
\qquad
\Delta E_{21}^{(q)}=E_q^{(M_1)}-E_q^{(M_2)}.
```

Only when `y^R` is independently qualified and the metric is frozen may `Delta E_21 > 0` be interpreted as error reduction. Without such a reference, report only model divergence such as

```math
\Delta Q_{21}=Q(M_2)-Q(M_1),
```

and label it as omitted-dynamics effect, not predictive superiority.

## 2. Experimental object

The controlled Level-2 object is

```math
\boxed{
\Omega_{L2}^{*}
=
(G_P,G_T,\mathcal D_{PT},\eta,\Phi_H,\Theta,\mathcal S,
\mathcal Q,\mathcal U,\mathcal R,\varepsilon,\Pi)
}
```

where `D_PT` is a set of canonical directed dependency objects, not a competing dependency ontology.

Every active dependency follows the canonical thesis contract

```math
\mathfrak d_e=(\mathcal C_e,\Sigma_e,\Pi_e),
```

with composition/interface semantics, causal/domain semantics, and epistemic/provenance semantics kept distinct.

## 3. Gate 1 — outcome-blind spatial case selection

The first scientific case must be a feeder-centered Greensboro ROI, not the full regional model. Candidate feeders are eligible only when

```math
C_{geo}\land C_{road}\land C_{interface}\land C_{hazard}\land C_{computable}=1.
```

Only pre-simulation features may be used for selection:

```math
z_f=[N_P,N_T,N_I,P_{max},L_T,R_T,E_H].
```

The implementation in `select_feeders.py` robustly standardizes these features. The development feeder is the global medoid. The held-out feeder is a conditional second medoid chosen to improve feature-space coverage after the development medoid is fixed. No `M0/M1/M2` result may enter either selection.

The held-out feeder is a **spatial generalization case on realistic synthetic infrastructure**. It is not observational validation.

## 4. Gate 2 — canonical directed dependencies

The required Level-2 directed mechanisms are registered in `registries/dependency_registry_v1.csv`:

1. `EV_T_to_P`: EV/charging arrivals change electrical loading;
2. `EV_P_to_T`: power availability changes charging/mobility service;
3. `SIGNAL_P_to_T`: power availability changes signal control/capacity;
4. `REPAIR_T_to_P`: road state changes crew access and therefore power restoration timing.

`EV_T_to_P` and `EV_P_to_T` inherit GreenEVT/SMART-DS method/data lineage but still require case-specific parameter freezing. `SIGNAL_P_to_T` and local `REPAIR_T_to_P` mappings remain `INFERRED_PENDING_VERIFICATION` unless direct local evidence is acquired.

No spatially inferred signal-to-bus relation may be described as observed Greensboro wiring.

## 5. Gate 3 — flood forcing and hazard-response separation

The primary hazard is a pluvial-flood stress test because a coherent inundation field can affect road mobility, repair accessibility, and evidence-supported ground-level electrical equipment while retaining explicit mechanism boundaries.

As of the 2026-09-18 source audit, NOAA's Atlas 15 page still identifies Atlas 14 as the current precipitation-frequency standard and Atlas 15 as under development. Therefore Atlas 14 remains primary until formal supersession is documented and this protocol is versioned. Atlas 15 preliminary products, if used, are sensitivity inputs only.

The physical chain is

```math
\text{design rainfall}
\rightarrow
\text{HEC-RAS 2D}
\rightarrow
\eta(x,t)=[h(x,t),v_w(x,t)]
\rightarrow
\Phi_H.
```

Terrain/soil/land-cover evidence is drawn from USGS 3DEP, USDA-NRCS SSURGO, and USGS NLCD respectively. Candidate storm durations are 1 h, 6 h, and 24 h at the declared AEP. Duration is selected in a **hazard-only** screen using a predeclared infrastructure-exposure functional, before examining any M0/M1/M2 response.

Road response must use a documented depth-speed/capacity relation within its validity domain plus an explicit safety closure rule. Direct flood-depth failure is restricted to evidence-supported ground-level electrical equipment. Flood depth alone must not be used to fail overhead lines; a separate wind/treefall/scour/pole-foundation mechanism would be required.

## 6. Gate 4 — matched scenario matrix and ablations

For every realization `r`, shared stochastic inputs are identical across models:

```math
\omega_r^{M_0}=\omega_r^{M_1}=\omega_r^{M_2}.
```

Matched quantities include hazard field, demand, EV trips, vulnerability draws, repair-duration draws, initial state, and random seed. The main design covers `H0`, `H_moderate`, and `H_severe`. M2 mechanism ablations isolate EV coupling, signal-power coupling, repair-access coupling, and the full dynamic model.

The exact design is frozen structurally in `registries/scenario_matrix_v1.csv`; scenario magnitudes and seed manifest remain open.

## 7. Gate 5 — parameter evidence hierarchy

Parameter precedence is

```math
\text{DATASET}
>
\text{AUTHORITATIVE EXTERNAL}
>
\text{PEER-REVIEWED CALIBRATION}
>
\text{UNCERTAIN PRIOR}
>
\text{EXPLICIT ASSUMPTION}.
```

Every parameter record must carry unit, source, distribution, bounds, aleatory/epistemic type, evidence grade, and validation pointer. An unknown value stays `OPEN`; it is never silently converted to a deterministic default.

The current registry is `registries/parameter_registry_v1.csv`.

## 8. Gate 6 — verification and validation

The hierarchy is

```math
\text{code verification}
\rightarrow
\text{solution verification}
\rightarrow
\text{submodel validation}
\rightarrow
\text{coupled prediction assessment}.
```

Code verification includes conservation, dimensional identities, and exact nested limits. Solution verification includes time-step/grid refinement. Submodel validation uses source/reference data appropriate to the power, transport, and flood components. Coupled prediction assessment requires an independent qualified reference.

No universal `20%` or similar acceptance threshold is authorized. Acceptance is QOI-specific and uncertainty-aware. Numerical thresholds remain open until the reference quantity, numerical uncertainty, input uncertainty, and context of use are qualified.

## 9. Gate 7 — uncertainty quantification

The mandatory order is

```math
\text{uncertainty registry}
\rightarrow
\text{screening}
\rightarrow
\text{global sensitivity}
\rightarrow
\text{propagation}.
```

Aleatory and epistemic sources are kept distinct. Morris screening may be used when dimension is high. For influential independent parameters, scrambled Sobol sampling is the default global-sensitivity method. With second-order indices disabled, SALib requires `N(D+2)` model evaluations. Base `N` is doubled from 256 upward until a **predeclared** convergence rule is met; the convergence tolerance itself is not yet frozen.

A flood realization is spatially coherent. Road depths must never be sampled independently edge-by-edge.

## 10. Gate 8 — QOIs and H1 decision logic

The primary H1 outcome families follow the canonical hypothesis:

- cascade;
- service loss;
- spatial propagation;
- recovery.

The exact predictive/explanatory distance for each family remains open until a valid reference is qualified, then must be frozen before confirmatory results are inspected.

Secondary engineering outcomes include `J_P`, `J_T`, ENS, `T95_P`, `T95_T`, EV queue burden, repair-access time, and transport delay. These describe consequences and mechanisms; they are not automatically model-accuracy measures.

`rho_g` is explicitly deferred:

```math
\text{qualified Level-2 trajectories}
\rightarrow
K
\rightarrow
\mathcal V/\mathcal R
\rightarrow
g_\psi
\rightarrow
\rho_g.
```

This prevents circular use of the later viability geometry to select the Stage-3 dynamic model that will supply its trajectories.

## 11. Claim ladder and falsification

Allowed claims depend on the closed gate:

| State | Maximum claim |
|---|---|
| preview fixture | software/mechanism verification only |
| realistic synthetic developmental run | reproducible model differences on a realistic synthetic case |
| qualified independent reference + frozen metrics | predictive/explanatory comparison |
| all H1 preregistration/data gates closed | confirmatory H1 test |

H1 is not supported merely because `M2 != M1`. For a preregistered QOI family, evidence favoring M2 requires the frozen incremental-information criterion to be met with uncertainty reported. Failure to meet it is a valid scientific result. Software/data qualification failure is `NOT TESTED`, not falsification.

## 12. Current executable gate state

`validate_protocol.py` audits the machine protocol and registries. Current expected result:

```text
structural protocol: PASS
registries: PASS
method status: METHOD_FROZEN_INPUTS_OPEN
confirmatory_ready: FALSE
```

The open freeze gates are intentionally explicit: development/held-out feeder IDs, hazard magnitudes/geometry, seed manifest, parameter distributions, independent reference, exact primary metrics, numerical validation thresholds, R1-R8 qualification, train/test split, UQ convergence rule, and repository authorization.

No one may set these flags to `true` merely to make the runner proceed; each requires its stated evidence artifact.

## 13. Ordered execution from here

1. acquire and audit GreenEVT/SMART-DS source bytes;
2. construct the feeder pre-simulation feature table;
3. execute `select_feeders.py` and freeze development/held-out IDs;
4. materialize and audit the canonical dependency crosswalks;
5. acquire/version hazard inputs and run hazard-only duration selection;
6. freeze parameter distributions and the common-random-number seed manifest;
7. close source-specific component V&V gates;
8. qualify the independent H1 reference and freeze exact QOI metrics/falsification rules;
9. freeze UQ convergence criteria;
10. only then authorize matched realistic/confirmatory execution.

This sequence is deliberately irreversible with respect to outcome-dependent choices: once a selection, threshold, or metric is frozen, changing it after examining target results requires a versioned protocol amendment and sensitivity disclosure.
