# Phase 1 — Executable Experiment Specification v1

![Status](https://img.shields.io/badge/status-PREREGISTERED-0969DA)
![Phase](https://img.shields.io/badge/phase-1%20experiment-1A7F37)
![Contract](https://img.shields.io/badge/dependency%20contract-v1.0-1A7F37)

**Preregistered:** 2026-09-12  
**Authority:** `CANONICAL_DEPENDENCY_CONTRACT_V1.md` + `PHASE1_EMPIRICAL_VALIDATION_PROTOCOL.md`  
**Scope:** bounded executable validation of physical, informational and organizational Power–Transportation dependencies before Stage-5 viability/resilience analysis.  
**Rule:** no benchmark, data window, model variant, causal operator, calibration/validation split, primary output, verification tolerance or acceptance rule may be changed after confirmatory results are inspected without a versioned amendment.

---

# 0. Evidence discipline used in this specification

The thesis reasoning protocol is applied explicitly:

```math
\text{LEARN}
\rightarrow
\text{VERIFY}
\rightarrow
\text{FORMULATE}
\rightarrow
\text{DERIVE}
\rightarrow
\text{TEST}
\rightarrow
\text{VALIDATE}
\rightarrow
\text{SYNTHESIZE}
\rightarrow
\text{ADVANCE}.
```

Claim tags used below are:

```text
[E] externally established evidence/standard;
[P] thesis-specific proposal or preregistered engineering choice;
[D] deduction derived from established evidence + thesis scope;
[A] explicit modeling assumption;
[U] unresolved item that cannot yet be claimed as established.
```

The governing rule is:

> **No claim without a definition, mechanism, evidence, assumptions, test and boundary of validity.**

---

# 1. Why Phase 1 must freeze the experiment before simulation

## 1.1 General scientific principle `[E]`

NASA-STD-7009B requires model-and-simulation activities to define their intended use and acceptance criteria as part of model credibility practice; it does not treat “the model runs” as sufficient evidence of credibility (NASA, 2024). ASME V&V 20 likewise distinguishes verification of the computational solution from validation by comparison with data for declared validation variables and points, while accounting for relevant uncertainties (ASME, 2009, reaffirmed 2021).

## 1.2 Application to this thesis `[P]`

We therefore freeze the complete experimental realization **before** observing final comparative results:

```math
\boxed{
\text{Specification}
\rightarrow
\text{Verification}
\rightarrow
\text{Identifiability}
\rightarrow
\text{Calibration}
\rightarrow
\text{Validation}
\rightarrow
\text{Model comparison}
\rightarrow
\text{later resilience experiments}.
}
```

## 1.3 Why this matters for our framework `[D]`

Our Stage-2 object is now

```math
\mathfrak d_e=(\mathcal C_e,\Sigma_e,\Pi_e).
```

If the experiment is changed after observing results, then failure can always be attributed to topology, parameters, solver, dependency form, evidence choice or scenario design. That would weaken falsifiability. A frozen experimental specification makes failure interpretable as scientific evidence rather than another opportunity to redesign the framework.

---

# 2. Exact experimental purpose

The Phase-1 experiment asks a narrower question than the complete thesis:

> **Can the canonical dependency contract be instantiated as executable physical, informational and organizational mechanisms that survive numerical verification and bounded validation without case-specific structural modification?**

Phase 1 does **not** yet test Stage-5 viability geometry, interface-criticality rankings or sustainable transformation pathways.

The required chain is

```math
\boxed{
\text{evidence}
\rightarrow
(\mathcal C_e,\Sigma_e,\Pi_e)
\rightarrow
\Xi_e
\rightarrow
\Delta X
\rightarrow
\Delta Q.
}
```

---

# 3. Experimental boundary

## 3.1 General principle `[E]`

Model credibility is purpose-specific: a model is not simply “valid” in the abstract; its adequacy is judged relative to an intended use and validation domain (NASA, 2024; ASME, 2009/2021). NIST similarly treats cyber-physical systems as integrated physical, digital and human systems whose timing, data, composition and human concerns must be made explicit (Griffor et al., 2017; Wollman et al., 2017).

## 3.2 Thesis application `[P]`

The experimental boundary is a **benchmark-calibrated, semi-empirical Power–Transportation demonstrator**, not a geographic digital twin.

It contains:

```text
Power: IEEE/Baran–Wu 33-bus radial distribution benchmark;
Charging: Caltech ACN-Data + ACN-Sim;
Transportation/access: Sioux Falls 24-node / 76-link benchmark;
Information: charging-demand forecast/latency channel;
Organization: crew authorization/mobilization + road-access restoration path.
```

The experiment intentionally does **not** add Water, telecommunications, rail, V2G, multiple hazards, large-scale agent behavior or additional organizational layers.

## 3.3 Why `[D]`

The objective is mechanism discrimination, not geographic realism. A benchmark-coupled demonstrator permits transparent equations, reproducibility, ablation and controlled comparison. Because the power and road benchmarks are not geographically co-located, the experiment cannot establish city-specific empirical causality. That limitation is frozen now rather than hidden later.

---

# 4. External benchmark and data sources

## 4.1 Distribution system `[E]`

The power subsystem uses MATPOWER `case33bw`, a 33-bus radial distribution system derived from Baran and Wu’s distribution-network work (Baran & Wu, 1989; MATPOWER, `case33bw`). The public case specifies a 12.66-kV system and bus/branch data. Buses 24 and 25 have the largest listed active load, 420 kW; the preregistered tie rule chooses the lowest bus index, so the charging interface is attached to **bus 24**. Its radial parent branch is **23 -> 24**.

Thus

```math
b^*=24,
\qquad
e_P^*=(23,24).
```

No power-network parameter is calibrated to improve Phase-1 results.

## 4.2 Transportation network `[E]`

The Sioux Falls benchmark contains 24 nodes and 76 directed links, with link capacities, free-flow times and BPR parameters in the TNTP dataset. The dataset uses

```math
\alpha_{BPR}=0.15,
\qquad
\beta_{BPR}=4
```

for its links (TransportationNetworks; LeBlanc, Morlok, & Pierskalla, 1975).

Node 10 is fixed as the charging/repair access node. Its published origin-demand total is 45,200 demand units in the TNTP trip table. It is selected deliberately as a high-use stress-test location; **no claim is made that node 10 is a universally optimal charger location**.

The crew depot is fixed at

```math
n_D=1,
```

and the access site is

```math
n_F=10.
```

The controlled road-access disruption removes both directed arcs of the link pair

```math
(9,10),\;(10,9).
```

This location is fixed before simulation because it directly changes access to node 10.

## 4.3 Charging data `[E]`

ACN-Data is an open EV charging dataset developed at Caltech and JPL. It contains charging-session attributes such as connection time, disconnect time, delivered energy, station identity, charging-current time series and pilot-signal time series (Lee, Li, & Low, 2019; ACN-Data portal). The Caltech ACN described by Lee et al. includes Level-2 EVSEs and a 50-kW DC fast charger. ACN-Sim is a data-driven open-source EV charging simulator that can replay ACN-Data sessions and represent charging-network constraints (Lee et al., 2021).

ACN-Sim literature and tutorials commonly use a five-minute interval, so the Phase-1 charging/power exchange interval is fixed as

```math
\Delta t=5\ \text{min}.
```

## 4.4 Exact ACN extraction window `[P]`

Use site

```text
site = caltech
```

and the interval

```text
2019-10-10 00:00:00 America/Los_Angeles
through
2019-12-31 23:59:59 America/Los_Angeles.
```

Why: the ACN portal documents a historical web-interface timezone issue before 10 October 2019. The current API/Python client is reported as corrected, but the post-10-October window removes this known legacy issue from the primary experiment.

The exact API response, extraction code, package versions and SHA-256 hashes must be frozen in a later `PHASE1_DATA_MANIFEST_V1.md` **before execution**.

If the declared data cannot be acquired reproducibly, Phase 1 is blocked rather than silently switching datasets.

---

# 5. Calibration–validation split

## 5.1 General principle `[E]`

Calibration and validation answer different questions. Calibration estimates unknown model quantities; validation evaluates an already-specified/calibrated model against independent evidence. Reusing validation data for tuning destroys the intended independence of the validation comparison (NASA, 2024; ASME, 2009/2021).

## 5.2 Thesis rule `[P]`

After removing days with incomplete/corrupt required fields, order all complete days chronologically.

Let `N_d` be the number of usable days. Define

```math
N_{cal}=\lfloor0.70N_d\rfloor.
```

Then

```math
\mathcal D_{cal}
=
\{\text{first }N_{cal}\text{ complete days}\},
```

```math
\mathcal D_{val}
=
\{\text{remaining complete days}\}.
```

Therefore

```math
\boxed{
\mathcal D_{cal}\cap\mathcal D_{val}=\varnothing.
}
```

No random shuffling is permitted because temporal leakage would weaken the out-of-time validation test.

Validation failure may trigger a **new model version**, but the failed validation result remains part of the audit trail and the new version receives a new holdout dataset or new preregistered split.

---

# 6. Power-system physics

## 6.1 General foundation `[E]`

Baran and Wu developed radial-distribution branch-flow/DistFlow formulations for distribution analysis. The MATPOWER 33-bus benchmark is explicitly sourced to this work (Baran & Wu, 1989; MATPOWER).

## 6.2 Phase-1 equations `[P]`

For radial branch `i -> j`, use the full branch-flow equations

```math
P_{ij}
=
\sum_{k:j\to k}P_{jk}
+p_j
+r_{ij}\ell_{ij},
```

```math
Q_{ij}
=
\sum_{k:j\to k}Q_{jk}
+q_j
+x_{ij}\ell_{ij},
```

```math
v_j
=
v_i
-2(r_{ij}P_{ij}+x_{ij}Q_{ij})
+(r_{ij}^2+x_{ij}^2)\ell_{ij},
```

```math
\ell_{ij}
=
\frac{P_{ij}^2+Q_{ij}^2}{v_i}.
```

The native power law is denoted

```math
F_P.
```

The EV charging load is added only at bus 24:

```math
p_{24}(t)
=
p_{24}^{base}+P_{ch}(t).
```

All other benchmark loads/impedances remain fixed.

## 6.3 Why `[D]`

Using the radial benchmark preserves real electrical conservation/voltage-drop structure while keeping the test small enough for repeated V&V/UQ. It also ensures the dependency enters the receiving power physics rather than replacing it with a generic graph equation.

---

# 7. Transportation and access physics

## 7.1 General foundation `[E]`

The Sioux Falls network is a long-established traffic-assignment test problem originating with LeBlanc et al. (1975). The current TNTP representation uses the link performance function

```math
 t_a(x_a)
=
t_a^0
\left[
1+B_a\left(\frac{x_a}{c_a}\right)^{\beta_a}
\right].
```

For Sioux Falls,

```math
B_a=0.15,
\qquad
\beta_a=4.
```

## 7.2 Thesis application `[P]`

A baseline user-equilibrium assignment is solved by Frank–Wolfe using the published OD matrix. For crew routing, link travel times are evaluated at the resulting baseline flows and updated for declared closures.

Crew travel time is

```math
T_{crew}(t)
=
\min_{r\in\mathcal R_T(t)}
\sum_{a\in r}t_a(x_a(t)).
```

If no path exists,

```math
T_{crew}=+\infty
```

and restoration is infeasible until accessibility is restored.

## 7.3 Why `[D]`

Infrastructure-restoration literature explicitly treats transportation accessibility and crew routing as constraints on restoration timing (e.g., work-crew routing and coupled transportation–crew–grid restoration studies). We therefore represent road accessibility as a mechanism affecting feasible restoration, not as a generic correlation between road and grid damage.

---

# 8. Canonical dependency instances exercised in Phase 1

The canonical contract is

```math
\mathfrak d_e=(\mathcal C_e,\Sigma_e,\Pi_e).
```

Phase 1 uses three dependency **families**. The physical family contains two directed edges because interdependency is constructed from directed dependencies, not from an undifferentiated bidirectional arrow.

## 8.1 `D_P` — physical Power–Transportation pair `[P]`

### Transportation -> Power

```math
D_P^{TP}:
T_{charging\ demand}
\rightarrow
P_{bus\ 24}.
```

Compositional object:

```math
\mathcal C_{TP}
=
(T_{ACN},p_{ACN}^{out},P_{24},p_{24}^{load},P_{ch}).
```

Causal operator:

```math
\Phi_{TP}:
P_{ch}(t)
\mapsto
p_{24}^{base}+P_{ch}(t).
```

### Power -> Transportation

```math
D_P^{PT}:
P_{branch\ 23-24}
\rightarrow
T_{charging\ availability}.
```

Define energization guard

```math
\gamma_{PT}(t)
=
\mathbf 1_{\{e_P^*\;\text{energized at }t\}}.
```

Then

```math
A_{ch}(t)=\gamma_{PT}(t).
```

During the controlled feeder fault,

```math
\gamma_{PT}=0,
```

so sessions connected through the experimental charging interface cannot receive energy until restoration.

### Why `[D]`

The two directed relations preserve the asymmetry required by the canonical dependency definition: EV charging changes electrical loading, while power availability changes charging service. They are not forced into one symmetric scalar edge.

---

# 9. `D_I` — information-mediated dependency

## 9.1 General principle `[E]`

NIST’s CPS framework treats data and timing/latency as first-class concerns in systems integrating physical and computational components (Griffor et al., 2017; Wollman et al., 2017). ISO 15118-20 specifies EV–EVSE communication requirements, including messages supporting electricity transfer and bidirectional power-transfer use cases (ISO, 2022). These standards establish the importance of communication/timing; they do **not** prescribe our forecast model.

## 9.2 Thesis-specific information model `[P]`

The transport-origin signal is the aggregate charging-demand forecast

```math
\widehat P_{ch}(t+\Delta t).
```

The calibration model is deliberately simple:

```math
\widehat P_{ch}(d,s)
=
\mu_{weekday/weekend,s},
```

where `s` is the 5-minute time-of-day slot and `mu` is estimated only from `D_cal`.

If a slot has fewer than five calibration observations, use the all-day-type same-slot mean. No machine-learning model is introduced in Phase 1.

The empirical forecast residuals are

```math
\varepsilon_I(t)
=
P_{ch}(t)-\widehat P_{ch}(t).
```

Information degradation is imposed through

```math
\widetilde P_{ch}(t)
=
\widehat P_{ch}(t-\delta_I)
+\varepsilon_I^{*}(t),
```

where `epsilon_I*` is sampled only from the calibration residual distribution.

Prescribed latency levels are

```math
\delta_I\in\{0,5,15,30\}\ \text{min}.
```

## 9.3 Test controller `[P]`

The controller is intentionally transparent rather than optimized:

```math
u_{ch}^{max}(t)
=
\operatorname{clip}
\left[
P_{margin}(t)
-k_I
\left(
\widetilde P_{ch}(t+\Delta t)-P_{ref}
\right)_+,
0,
\bar P_{site}
\right],
```

with

```math
k_I=1.
```

`P_ref` is the median calibration-period aggregate charging power and `P_margin(t)` is the instantaneous feeder-side charging margin obtained from the power model.

This controller is a **test policy**, not a claim of industrial optimality.

## 9.4 Why `[D]`

A simple fixed controller makes the causal test interpretable:

```math
\text{information quality/latency}
\rightarrow
u_{ch}^{max}
\rightarrow
P_{ch}
\rightarrow
X_P,Q_{mobility}.
```

If an advanced controller were simultaneously introduced, improved performance could be attributed either to the dependency representation or to controller sophistication.

---

# 10. `D_O` — organizational/access restoration dependency

## 10.1 General evidence `[E]`

Restoration research models work-crew routing through transportation networks and shows that access constraints can delay restoration of disrupted infrastructure. Recent coupled transportation–crew–grid formulations likewise treat damaged or degraded road accessibility as a constraint on deployment of repair resources.

## 10.2 Thesis realization `[P]`

The controlled power fault opens

```math
e_P^*=(23,24)
```

at

```math
t_0=12{:}00\ \text{local experiment time}.
```

The crew starts at Sioux Falls node 1 and must reach node 10.

The organizational guard is

```math
\gamma_O(t)
=
\mathbf 1_{\{authorization=1\}}
\mathbf 1_{\{crew\ available=1\}}
\mathbf 1_{\{\mathcal R_T(t)\neq\varnothing\}}.
```

Primary experiment assumptions are

```math
\tau_{decision}=15\ \text{min},
```

```math
\tau_{mobilization}=15\ \text{min},
```

```math
\tau_{repair}=60\ \text{min}.
```

These values are **[A/P] controlled assumptions, not empirically validated repair-time estimates**.

Restoration time is

```math
T_{restoration}
=
\tau_{decision}
+\tau_{mobilization}
+T_{crew}
+\tau_{repair}.
```

The outage branch is re-energized only at `T_restoration`.

The epistemic ranges used later for uncertainty analysis are

```math
\tau_{decision}\in[0,30]\ \text{min},
```

```math
\tau_{mobilization}\in[0,30]\ \text{min},
```

```math
\tau_{repair}\in[30,120]\ \text{min}.
```

## 10.3 Why `[D]`

This construction isolates the mechanism

```math
\text{road accessibility}
\rightarrow
\text{crew arrival}
\rightarrow
\text{repair completion}
\rightarrow
\text{power/charging restoration}.
```

It does not pretend that the assumed organizational delays are measured field data. Therefore `D_O` cannot receive an unrestricted empirical-validation claim in Phase 1 v1.

---

# 11. Multi-rate execution architecture

The experiment does not force all systems onto one artificial physics/timescale.

Charging and feeder coupling use

```math
\Delta t=5\ \text{min}.
```

The distribution power flow is solved quasi-statically at each charging interval.

The road user-equilibrium state is solved for the baseline network and the crew route is recomputed when accessibility changes.

Organizational/restoration events occur at discrete event times.

Thus

```math
\boxed{
F_P\neq F_T
}
```

and

```math
\boxed{
\text{continuous/quasi-static physics}
+\text{discrete events}
+\text{different timescales}
}
```

are preserved.

---

# 12. Competing model variants

## 12.1 H1 physical-coupling family `[P]`

Freeze:

```math
\mathscr C_0
=
\text{independent }P+T.
```

`C0` removes both physical cross-domain operators:

```math
\Phi_{TP}=0,
\qquad
\Phi_{PT}=0.
```

Freeze:

```math
\mathscr C_1
=
\text{static P--T coupling}.
```

`C1` uses the calibration-period mean charging power

```math
P_{ch}(t)=\overline P_{ch,cal}
```

while energized, together with the same binary feeder-availability mapping.

Freeze:

```math
\mathscr C_2
=
\text{dynamic causal coupling}.
```

`C2` uses the time-varying 5-minute ACN-derived charging trajectory and the explicit energization/restoration guard.

All other equations and parameters remain identical.

## 12.2 H2 socio-technical family `[P]`

```math
\mathscr N_0=P+T
```

uses dynamic physical coupling with ideal information and immediate organizational availability.

```math
\mathscr N_1=P+T+I
```

adds the declared latency/error process and the fixed information-dependent test controller.

```math
\mathscr N_2=P+T+I+O
```

adds the access/crew/restoration mechanism.

This is a nested mechanism comparison; the physical laws remain unchanged.

---

# 13. Phase-1 primary outputs

Stage-5 viability quantities are prohibited as Phase-1 primary outcomes.

The primary mechanism-level vector is

```math
Z_{P1}
=
\begin{bmatrix}
V_{min}\\
T_{Vviol}\\
E_{unserved}^{EV}\\
Q_{mobility}^{charge}\\
T_{crew}\\
T_{restoration}
\end{bmatrix},
```

where

```text
V_min = minimum bus-voltage magnitude;
T_Vviol = duration outside the benchmark voltage band;
E_unserved^EV = requested minus delivered EV energy;
Q_mobility^charge = fraction of requested charging energy delivered by departure;
T_crew = crew travel time;
T_restoration = feeder-branch restoration time.
```

Secondary outputs are

```math
RMSE_I,
\qquad
MAE_I,
\qquad
P_{peak},
\qquad
E_{loss}.
```

No `rho`, viability kernel, viability boundary or viability sensitivity is computed until Phase 1 closes.

---

# 14. Parameter provenance and identifiability register

## 14.1 General principle `[E]`

Identifiability analysis asks whether parameter values can be uniquely or sufficiently constrained by the available observations. Profile-likelihood methods, for example, distinguish structural/practical non-identifiability and can support confidence intervals, experimental planning and model reduction (Raue et al., 2009).

## 14.2 Phase-1 parameter classes `[P]`

| Parameter class | Examples | Status | Free calibration? |
|---|---|---|---:|
| benchmark power | `r_ij,x_ij,Pd,Qd` | external benchmark | no |
| benchmark road | `c_a,t_a^0,B_a,beta_a` | external benchmark | no |
| charging observations | arrivals, departures, current, delivered kWh | observed | no |
| information statistics | `mu_slot`, empirical residual distribution | estimated from `D_cal` | yes |
| information latency | `delta_I` | prescribed experiment factor | no |
| controller gain | `k_I=1` | fixed test policy | no |
| organization times | decision/mobilization/repair | epistemic assumptions | no hidden calibration |

This intentionally keeps the freely estimated parameter set small.

## 14.3 Sensitivity/identifiability diagnostic `[P]`

For every free continuous parameter, compute normalized finite-difference sensitivities

```math
\widetilde S_{ij}
=
\frac{\theta_j}{s_i}
\frac{\partial y_i}{\partial\theta_j},
```

where `s_i` is the declared output scale.

Use singular-value diagnostics on `S`. A ratio

```math
\frac{\sigma_{min}}{\sigma_{max}}<10^{-8}
```

is flagged as severe numerical non-identifiability **[P diagnostic threshold]**. It does not by itself prove structural non-identifiability.

If more than two continuous parameters are later added to a mechanism, profile likelihood or another justified identifiability method becomes mandatory before confirmatory calibration.

---

# 15. Verification before validation

## 15.1 General principle `[E]`

Verification asks whether the equations and numerical implementation are solved correctly; validation asks whether model outputs agree adequately with independent evidence for the intended use. ASME V&V 20 formalizes this distinction for computational models, while NASA-STD-7009B frames V&V/UQ as model-credibility activities rather than a single pass/fail simulation event.

## 15.2 Mandatory limit tests `[P]`

### Dependency removal

```math
\Phi_e=0
\Rightarrow
\text{corresponding uncoupled baseline recovered}.
```

### Guard removal

```math
\gamma_e=0
\Rightarrow
\text{only that dependency is inactive}.
```

### Zero-delay limit

```math
\delta_I\rightarrow0
\Rightarrow
\text{zero-delay information model recovered}.
```

### No-road-disruption limit

Restoring links `(9,10)` and `(10,9)` must recover the baseline crew-route solution.

### No-feeder-fault limit

Keeping branch `(23,24)` energized must remove the restoration event without altering unrelated system equations.

---

# 16. Numerical verification tolerances

The following are thesis-specific preregistered tolerances `[P]`, not universal standards.

## 16.1 Power solver

Maximum normalized equation residual:

```math
\epsilon_P\le10^{-8}.
```

Maximum iteration count:

```math
N_{it,P}=100.
```

Failure to converge is recorded as a model failure; it is not removed from the scenario set.

## 16.2 Transportation assignment

Frank–Wolfe relative gap:

```math
RG\le10^{-6}.
```

Maximum iterations:

```math
N_{it,T}=5000.
```

## 16.3 Time-step refinement

For each scalar primary output `z`, compare the 5-minute realization to a 2.5-minute refinement on the designated verification day:

```math
\epsilon_{\Delta t}(z)
=
\frac{|z_{5min}-z_{2.5min}|}
{\max(|z_{2.5min}|,s_z)}.
```

Require

```math
\epsilon_{\Delta t}(z)\le10^{-3}
```

for all continuous numerical outputs whose algorithms support the refinement.

## 16.4 Charging-energy reconstruction

For each complete validation day,

```math
\epsilon_E
=
\frac{|E_{sim}-E_{data}|}{E_{data}}.
```

Require median daily

```math
\operatorname{median}(\epsilon_E)\le0.01
```

for the ACN replay layer before the charging trajectory is admitted into coupled tests.

## 16.5 Reproducibility

For deterministic runs with identical inputs and environment lockfile, outputs must agree to

```math
10^{-12}
```

relative numerical tolerance, except explicitly stochastic quantities generated from a recorded random seed.

---

# 17. Validation hierarchy and what can actually be claimed

This section deliberately limits claims.

## 17.1 Level V0 — code/solution verification `[P]`

Checks equations, residuals, limits, convergence and reproducibility.

## 17.2 Level V1 — component/data validation `[P]`

The charging-data/forecast subsystem is assessed on `D_val` using observed ACN sessions.

Forecast metrics:

```math
RMSE_I
=
\sqrt{\frac1N\sum_t(P_{ch}(t)-\widehat P_{ch}(t))^2},
```

```math
MAE_I
=
\frac1N\sum_t|P_{ch}(t)-\widehat P_{ch}(t)|.
```

A persistence forecast

```math
\widehat P_{pers}(t+\Delta t)=P_{ch}(t)
```

is the mandatory data baseline.

The seasonal-slot forecast is retained only if its holdout RMSE is no worse than persistence. This is a model-selection rule, not a thesis hypothesis result.

## 17.3 Level V2 — benchmark-physics validation/verification `[P]`

Distribution and transport models must reproduce their benchmark equations/known baseline solutions to the declared numerical tolerances.

This is **benchmark credibility**, not empirical validation of an actual co-located city.

## 17.4 Level V3 — coupled-mechanism discrimination `[P]`

`C0`, `C1`, `C2` and `N0`, `N1`, `N2` are compared under exactly the same forcing/scenarios.

Because the power and road benchmarks are synthetically aligned, V3 establishes whether the coupling mechanism changes the controlled demonstrator as predicted. It does not establish that the exact magnitude transfers to a real city.

---

# 18. Calibration prohibition and model-version rule

No parameter from the external power or transport benchmark may be adjusted to make coupled results appear more realistic.

Only quantities explicitly marked `estimated from D_cal` may be estimated.

After `D_val` is opened:

```text
- no retuning;
- no data-window change;
- no output deletion;
- no scenario deletion;
- no benchmark remapping.
```

A substantive change creates

```text
PHASE1_EXPERIMENT_SPECIFICATION_V2.md
```

and v1 results remain archived.

---

# 19. Uncertainty classification

## 19.1 General principle `[E]`

The JCGM Guide to the Expression of Uncertainty in Measurement provides a general framework for expressing/propagating measurement uncertainty, including Monte Carlo propagation in its supplements. Global sensitivity methods such as Morris screening and Sobol indices address a different question: which uncertain inputs materially drive model-output variation (JCGM, 2008; Morris, 1991; Sobol, 2001).

## 19.2 Thesis classification `[P]`

### Aleatory / observed variability

```text
- day-to-day EV session arrivals;
- charging demand conditional on the observed ACN population;
- empirical forecast residual resampling.
```

### Epistemic / model uncertainty

```text
- organizational delays;
- repair duration;
- assumed road-disruption severity;
- mapping of benchmark P bus 24 to benchmark T node 10;
- generalization from benchmark-coupled demonstrator to real infrastructure.
```

These two classes are not merged into one probability distribution without justification.

---

# 20. Sensitivity-analysis sequence

## 20.1 General evidence `[E]`

Morris elementary-effects designs are intended for screening influential inputs in computational models with multiple factors (Morris, 1991). Sobol variance-based indices quantify contributions of individual variables/groups to output variance and can be estimated by Monte Carlo/quasi-Monte Carlo methods (Sobol, 2001).

## 20.2 Thesis procedure `[P]`

First execute Morris screening on epistemically uncertain continuous factors using

```text
levels p = 4;
trajectories r = 20;
fixed random seed recorded in the run manifest.
```

Factors with negligible elementary effects on **all** primary outputs are removed from the expensive global stage but remain documented.

If the active uncertain dimension after screening satisfies

```math
d_{active}\le10,
```

compute Sobol first-order and total-order indices using base sample

```math
N=1024.
```

Repeat with

```math
N=2048
```

for convergence auditing of the reported sensitivity ranking.

If rankings materially change, no converged Sobol claim is made.

---

# 21. Controlled disruption scenario

The primary disruption is a **mechanism stress test**, not a calibrated flood/heat event.

At

```math
t_0=12{:}00,
```

apply simultaneously:

```text
1. open distribution branch 23 -> 24;
2. close Sioux Falls road links 9 -> 10 and 10 -> 9;
3. keep all other benchmark components unchanged.
```

The scenario is deliberately small enough that the causal chain remains identifiable:

```math
\text{road disruption}
\rightarrow
T_{crew}
\rightarrow
T_{restoration}
\rightarrow
A_{ch}
\rightarrow
E_{unserved}^{EV}.
```

No hazard-specific probability is assigned.

---

# 22. Model-comparison discipline

## 22.1 General principle `[E]`

A more complex model should not be preferred merely because it can reproduce more behaviors. It must provide additional explanatory/predictive value relevant to its intended use while its added parameters/assumptions remain credible. This is consistent with purpose-specific credibility and uncertainty practice in model V&V (NASA, 2024; ASME, 2009/2021).

## 22.2 Phase-1 decision rule `[P]`

Phase 1 does **not** yet set the final thesis `delta_1` or `delta_2` confirmatory thresholds from `H_1/H_2`.

Reason: those thresholds must be engineering-meaningful and must not be chosen from final validation outcomes.

Phase 1 instead produces the quantities needed to set them from:

```text
- calibration-only variability;
- physical operating limits;
- independent engineering standards where applicable;
- predeclared service requirements.
```

Final `H_1/H_2` thresholds must be frozen in a separate confirmatory matrix **after Phase-1 dependency validation but before H1/H2 confirmatory testing**.

---

# 23. Acceptance categories

Every dependency family ends Phase 1 in exactly one category:

```text
VALIDATED WITHIN DECLARED DOMAIN
VALIDATED WITH RESTRICTIONS
NOT SUPPORTED
```

There is no post hoc category called “needs more tuning.”

## 23.1 `D_P` maximum claim in v1 `[D]`

Because the P and T benchmark systems are synthetically aligned rather than observed as one co-located infrastructure, `D_P` can receive at most

```text
VALIDATED WITH RESTRICTIONS
```

in Phase 1 v1.

## 23.2 `D_I` maximum claim in v1 `[D]`

The forecast/information relationship may be validated against held-out ACN data, but its effect on the synthetic feeder remains benchmark-specific. Therefore its overall coupled claim can also receive at most

```text
VALIDATED WITH RESTRICTIONS.
```

## 23.3 `D_O` maximum claim in v1 `[D]`

Because organizational/repair delays are prescribed assumptions rather than field-estimated data, `D_O` can receive at most

```text
VALIDATED WITH RESTRICTIONS.
```

unless a future version supplies independent observed crew/access/restoration data.

This restriction is a feature of the method, not a weakness to hide.

---

# 24. Canonical-contract adequacy test

Across `D_P`, `D_I` and `D_O`, test whether the same structure

```math
\mathfrak d_e=(\mathcal C_e,\Sigma_e,\Pi_e)
```

can represent all cases without adding a new top-level primitive.

The contract passes Phase 1 structural adequacy only if:

```text
- source/receiver and interface are expressible through C_e;
- mechanism/state/context are expressible through Sigma_e;
- evidence status/uncertainty are expressible through Pi_e;
- Xi_e can be produced/referenced without becoming a new physical primitive;
- Delta d -> Delta X -> Delta Q is traceable;
- no case-specific top-level field is introduced.
```

Failure of any item reopens the dependency contract through versioned change control rather than silent expansion.

---

# 25. Execution software architecture

The numerical implementation will use Python with a version-locked environment.

The intended modules are:

```text
power/          radial branch-flow solver + case33bw parser
transport/      Sioux Falls parser + Frank–Wolfe + Dijkstra routing
charging/       ACN-Data extraction + ACN-Sim replay
coupling/       canonical dependency operators and event guards
validation/     metrics, convergence, identifiability, UQ
experiments/    C0/C1/C2 and N0/N1/N2 runners
```

The exact Python/package versions are **not guessed in this document**. They become frozen in the execution manifest generated from the environment actually used.

If FMI is later used for model exchange, it is an implementation realization `Xi_e`; FMI 3.0.2 defines standardized dynamic-model exchange/co-simulation interfaces and exposed variable dependencies, but it is not evidence that a real-world dependency exists (Modelica Association, 2024).

---

# 26. Required pre-run artifacts

Confirmatory execution remains blocked until the following are committed:

```text
PHASE1_DATA_MANIFEST_V1.md
PHASE1_PARAMETER_REGISTER_V1.md
PHASE1_SOFTWARE_ENVIRONMENT_LOCK_V1.md
PHASE1_VERIFICATION_TEST_MATRIX_V1.md
PHASE1_CONFIRMATORY_H1_H2_MATRIX_V1.md
```

The data manifest must include source URLs/DOIs, extraction timestamps, query parameters, raw-file hashes and licenses/usage conditions.

---

# 27. Validation boundary

The strongest permitted Phase-1 statement is:

> A bounded, reproducible benchmark-calibrated demonstrator was used to verify and partially validate the executable realization of the canonical physical, informational and organizational dependency contract under declared Power–Transportation mechanisms.

The following claims are prohibited from Phase 1 v1 alone:

```text
- universal empirical validity of the dependency contract;
- city-scale predictive accuracy;
- proof that bus 24/node 10 represents a real geographic interface;
- hazard-specific resilience probability;
- viability-kernel superiority;
- universal organizational-delay distributions;
- novelty solely from using DistFlow, Sioux Falls, ACN-Data, ACN-Sim, FMI or standard sensitivity methods.
```

---

# 28. Phase-1 stopping rule

Phase 1 can advance to confirmatory `H_1/H_2` only when:

```text
1. all numerical verification tests pass;
2. data/calibration/validation separation is audited;
3. no unauthorized parameter tuning has occurred;
4. each dependency has an explicit Pi_e evidence state;
5. primary output definitions are unchanged;
6. model variants C0/C1/C2 and N0/N1/N2 are reproducible;
7. uncertainty/sensitivity diagnostics have been completed;
8. confirmatory H1/H2 thresholds are frozen without using final validation outcomes.
```

Only after H1/H2 mechanism tests are completed should Stage 5 be reopened.

The scientific transition remains

```math
\boxed{
\text{Phase 0: representation theory}
\rightarrow
\text{Phase 1: executable dependency credibility}
\rightarrow
\text{H1/H2 confirmatory mechanism tests}
\rightarrow
\text{Phase 2: resilience/viability experiments}.
}
```

---

# References

- **ASME.** (2009, reaffirmed 2021). *V&V 20 — Standard for Verification and Validation in Computational Fluid Dynamics and Heat Transfer.* American Society of Mechanical Engineers. https://www.asme.org/codes-standards/find-codes-standards/standard-for-verification-and-validation-in-computational-fluid-dynamics-and-heat-transfer/2009
- **Baran, M. E., & Wu, F. F.** (1989). Network reconfiguration in distribution systems for loss reduction and load balancing. *IEEE Transactions on Power Delivery, 4*(2), 1401–1407. https://doi.org/10.1109/61.25627
- **Griffor, E. R., Greer, C., Wollman, D. A., & Burns, M. J.** (2017). *Framework for Cyber-Physical Systems: Volume 1, Overview.* NIST SP 1500-201. https://doi.org/10.6028/NIST.SP.1500-201
- **ISO.** (2022). *ISO 15118-20:2022 Road vehicles — Vehicle to grid communication interface — Part 20.* https://www.iso.org/standard/77845.html
- **JCGM.** (2008). *JCGM 100:2008 — Evaluation of measurement data — Guide to the expression of uncertainty in measurement.* BIPM. https://doi.org/10.59161/JCGM100-2008E
- **LeBlanc, L. J., Morlok, E. K., & Pierskalla, W. P.** (1975). An efficient approach to solving the road network equilibrium traffic assignment problem. *Transportation Research, 9*(5), 309–318. https://doi.org/10.1016/0041-1647(75)90030-1
- **Lee, Z. J., Li, T., & Low, S. H.** (2019). ACN-Data: Analysis and Applications of an Open EV Charging Dataset. *Proceedings of the Tenth ACM International Conference on Future Energy Systems*, 139–149. https://doi.org/10.1145/3307772.3328313
- **Lee, Z. J., Sharma, S., Johansson, D., & Low, S. H.** (2021). ACN-Sim: An Open-Source Simulator for Data-Driven Electric Vehicle Charging Research. *IEEE Transactions on Smart Grid, 12*(6), 5113–5123. https://doi.org/10.1109/TSG.2021.3103156
- **MATPOWER.** `case33bw` — 33-bus distribution test case derived from Baran and Wu. https://matpower.org/docs/ref/matpower6.0b2/case33bw.html
- **Modelica Association.** (2024). *Functional Mock-up Interface Specification 3.0.2.* https://fmi-standard.org/docs/3.0.2/
- **Morris, M. D.** (1991). Factorial Sampling Plans for Preliminary Computational Experiments. *Technometrics, 33*(2), 161–174. https://doi.org/10.1080/00401706.1991.10484804
- **NASA.** (2024). *NASA-STD-7009B — Standard for Models and Simulations.* https://standards.nasa.gov/standard/nasa/nasa-std-7009
- **Raue, A., Kreutz, C., Maiwald, T., Bachmann, J., Schilling, M., Klingmüller, U., & Timmer, J.** (2009). Structural and practical identifiability analysis of partially observed dynamical models by exploiting the profile likelihood. *Bioinformatics, 25*(15), 1923–1929. https://doi.org/10.1093/bioinformatics/btp358
- **Sobol, I. M.** (2001). Global sensitivity indices for nonlinear mathematical models and their Monte Carlo estimates. *Mathematics and Computers in Simulation, 55*(1–3), 271–280. https://doi.org/10.1016/S0378-4754(00)00270-6
- **TransportationNetworks.** Sioux Falls TNTP network and trip table. https://github.com/bstabler/TransportationNetworks/tree/master/SiouxFalls
- **Wollman, D. A., Weiss, M. A., Li-Baboud, Y., Griffor, E. R., & Burns, M. J.** (2017). *Framework for Cyber-Physical Systems: Volume 3, Timing Annex.* NIST SP 1500-203. https://doi.org/10.6028/NIST.SP.1500-203
- **Work-crew routing evidence:** *Work crew routing problem for infrastructure network restoration.* (2018). *Transportation Research Part B, 118*, 66–89. https://doi.org/10.1016/j.trb.2018.10.001
