# EGMIV H1 Validation Observation + Service-Requirement Architecture v1.0

**Status:** STRUCTURE FROZEN — DATA/CASE NOT YET SELECTED  
**Date:** 2026-09-14  
**Scope:** H1 validation architecture for the verified M0/M1/M2 physical Power–Transportation models.

## 1. Purpose

The previous threshold-provenance step established that numerical uncertainty can be quantified now, but final observation and engineering thresholds cannot be frozen until the validation observation system and service requirements are specified.

This architecture therefore freezes **how** real observations and requirements must map into

\[
S_P(t),\qquad S_T(t),\qquad u_{\mathrm{obs},P},\qquad u_{\mathrm{obs},T},
\qquad u_{\mathrm{eng},P},\qquad u_{\mathrm{eng},T}.
\]

It does **not** assign unsupported numerical values.

---

# 2. Governing EGMIV rule

\[
\boxed{
\text{sensor/data}
\rightarrow
\text{native observable}
\rightarrow
\text{state/demand reconstruction}
\rightarrow
\text{service operator}
\rightarrow
\text{uncertainty}
\rightarrow
\text{validation metric}.
}
\]

No sensor accuracy specification is allowed to become a service-ratio uncertainty without this mapping.

No engineering target is allowed to become \(u_{\mathrm{eng}}\) unless it is expressed in the same quantity as the thesis service metric, or a validated transformation exists.

---

# 3. Common validation clock

The simulation time step

\[
\Delta t_{\mathrm{sim}}=4.5\ \mathrm{s}
\]

is a numerical integration resolution, **not an observation resolution**.

Let

\[
\Delta_P^{obs},\qquad \Delta_T^{obs}
\]

be the native power and transportation observation intervals.

The confirmatory comparison must use a common observation interval

\[
\boxed{
\Delta_{\mathrm{val}}
\ge
\max(\Delta_P^{obs},\Delta_T^{obs})
}
\]

chosen so that both data streams can be aggregated without interpolation to a falsely finer resolution.

Model outputs are passed through the same observation operator before comparison:

\[
\boxed{
Y_M(t)
\rightarrow
\mathcal O_{\Delta_{\mathrm{val}}}[Y_M]
\rightarrow
Y_{\mathrm{obs}}.
}
\]

No validation claim may compare a 4.5-s model value directly against a 5-min or 15-min observation as if they had equal temporal resolution.

Once \(\Delta_{\mathrm{val}}\) is selected, the numerical-refinement audit must be repeated **after application of the observation operator**. The existing \(u_{\mathrm{num},P}\) and \(u_{\mathrm{num},T}\) remain conservative pre-observation floors until that final check.

---

# 4. Power observation architecture

## 4.1 Physical quantities

For load/service entity \(i\) and validation interval \(I_m\),

\[
E_{i,m}^{srv}
=
\int_{I_m}p_i^{srv}(t)\,dt
\]

is the actually served electrical energy.

The counterfactual requested energy is

\[
\widehat E_{i,m}^{d}
=
\mathcal B_i(Z_m;\widehat\beta_i),
\]

where \(\mathcal B_i\) is a baseline-demand model and \(Z_m\) may contain weather, calendar, occupancy/operations and other independently observed load drivers.

The observed power-service metric is

\[
\boxed{
S_{P,m}^{obs}
=
\frac{\sum_i\omega_i E_{i,m}^{srv}}
{\sum_i\omega_i\widehat E_{i,m}^{d}}
}.
\]

Using interval **energy** rather than an instantaneous power ratio is required when the field meter reports interval consumption.

## 4.2 Minimum data streams

### P1 — Actual served electricity
Preferred hierarchy:

1. load-/feeder-level AMI or revenue-grade interval metering;
2. SCADA/feeder/substation telemetry with validated downstream allocation;
3. calibrated state-estimation reconstruction with independently measured boundary power.

### P2 — Electrical topology/status
OMS/SCADA/breaker/switch status is required to distinguish:

\[
\text{true zero service}
\neq
\text{telemetry loss}.
\]

Missing communications must **not** automatically be coded as zero electricity service.

### P3 — Counterfactual requested demand
The demand baseline is trained only on intact, non-held-out intervals.

Candidate explanatory variables are limited to independently observed variables available during the event, such as:

- time of day;
- day of week/calendar;
- ambient/weather conditions;
- occupancy/operating schedule where relevant;
- stable seasonal terms.

Held-out event observations cannot be used to refit \(\mathcal B_i\).

### P4 — Criticality/service weights
\(\omega_i\) must come from a documented load/critical-service classification. They may not be tuned to strengthen M2.

## 4.3 Baseline-model validation

Counterfactual demand error is measured through masked-window validation on intact historical periods.

For an intact validation interval:

1. hide the actual demand from the baseline estimator;
2. predict \(\widehat E_{i,m}^{d}\);
3. compare with measured \(E_{i,m}^{d}\);
4. preserve the residual distribution conditional on operating regime.

A pseudo-service reconstruction can be evaluated as

\[
\widehat S_{P,m}^{pseudo}
=
\frac{\sum_i\omega_i E_{i,m}^{obs}}
{\sum_i\omega_i\widehat E_{i,m}^{d}}.
\]

Since the interval is intact, its physical service should be approximately 1 after accounting for ordinary losses/definition conventions.

The error distribution

\[
e_{P,m}
=
\widehat S_{P,m}^{pseudo}-S_{P,m}^{truth}
\]

feeds the observation uncertainty.

## 4.4 Missing data

Missing power data are classified:

- **M0:** truly measured;
- **M1:** reconstructable gap with an independently validated baseline/backfill model;
- **M2:** outage-confirmed physical zero by topology/status evidence;
- **M3:** ambiguous missingness.

M3 intervals are not silently imputed for confirmatory validation.

Any backfilled value remains tagged as modeled, not metered.

---

# 5. Transportation observation architecture

## 5.1 Physical quantities

For OD pair \(w\) and interval \(I_m\),

\[
N_{w,m}^{req}
\]

is requested OD demand and

\[
N_{w,m}^{comp}
\]

is completed OD flow.

The observed transport-service metric is

\[
\boxed{
S_{T,m}^{obs}
=
\min\left[
1,\,
\frac{\sum_w\omega_w N_{w,m}^{comp}}
{\sum_w\omega_w\widehat N_{w,m}^{req}}
\right].
}
\]

The \(\min(1,\cdot)\) operator matches the current frozen model service convention.

## 5.2 Minimum data streams

### T1 — Entry/volume observations
Continuous or short-duration count data support network boundary demand and QA.

### T2 — OD observations
Preferred hierarchy:

1. field/trajectory OD observations or re-identification data;
2. probe-based OD samples combined with count-based expansion;
3. validated regional/subarea OD matrix adjusted to field counts;
4. model-generated OD only — **not admissible as independent H1b truth**.

### T3 — Completed-trip observations
Completed trips require exit/arrival observations or matched trajectories. Segment speed/travel-time data alone do not identify complete OD counts.

### T4 — Travel-time/state observations
Probe or detector travel-time/speed data are used to validate traffic state and event timing, but are not substituted for OD demand.

## 5.3 Requested demand is counterfactual during disruption

Observed roadway volume under congestion may be **capacity-constrained throughput**, not true demand.

Therefore the requested OD demand during a disruption is estimated from an intact-period demand model:

\[
\widehat N_{w,m}^{req}
=
\mathcal D_w(X_m;\widehat\gamma_w),
\]

where \(X_m\) can include calendar, season, planned events and other independently observed demand drivers.

Congested event throughput cannot be used directly as requested demand.

## 5.4 OD baseline validation

Use masked-window validation on intact/comparable periods:

\[
e_{T,w,m}^{req}
=
\widehat N_{w,m}^{req}-N_{w,m}^{req,obs}.
\]

Where full-population OD truth is unavailable, the validation must include:

- probe/sample penetration uncertainty;
- expansion-factor uncertainty;
- count reconciliation error;
- spatial coverage uncertainty;
- temporal aggregation uncertainty.

## 5.5 Missing data

Transportation missingness is classified as:

- directly observed;
- reconstructable from validated neighboring/probe sources;
- structurally unobserved;
- ambiguous.

No missing interval is treated as zero demand or zero completed trips without physical evidence.

---

# 6. Observation-uncertainty propagation

For a generic ratio

\[
S=\frac{A}{B},
\]

with covariance matrix for \(A\) and \(B\),

\[
\boxed{
\operatorname{Var}(S)
\approx
\frac{\sigma_A^2}{B^2}
+
\frac{A^2\sigma_B^2}{B^4}
-
2\frac{A}{B^3}\sigma_{AB}.
}
\]

This delta-method expression is a diagnostic only.

The preferred final procedure is empirical/Monte Carlo propagation of:

- meter/count error;
- baseline-demand predictive residuals;
- expansion/coverage uncertainty;
- time-alignment uncertainty;
- imputation uncertainty;
- covariance/dependence.

Define

\[
u_{\mathrm{obs},P}
=
Q_{0.95}
\left(
|_|_P^{reconstructed}-S_P^{reference}|
pright)
\]

from masked-window/pseudo-event validation plus measurement uncertainty propagation.

Similarly,

\[
u_{\mathrm{obs},T}
=
Q_{0.95}
\left(
|_|_T^{reconstructed}-S_T^{reference}|
\right).
\]

These are frozen **only after** the actual data architecture passes the admissibility gates below.

---

# 7. Observation admissibility gates

## O1 — Quantity validity
Every observation must identify the native measured quantity and its units.

## O2 — Time synchronization
Power, traffic, disturbance and model clocks must share a documented time reference and aggregation convention.

## O3 — Spatial mapping
Every sensor/data object must map deterministically to a power bus/load entity, road cell/link, OD pair or interface.

## O4 — Missingness classification
Missing data must be distinguished from physical zero.

## O5 — Counterfactual-demand validation
Power and transportation demand-reconstruction models must be validated on masked intact periods before event use.

## O6 — Held-out independence
No held-out event contributes to fitting the baseline, selecting covariates, setting thresholds or modifying model structure.

## O7 — Coverage
The validation domain is restricted to spatial/temporal regions for which coverage and uncertainty can be quantified.

## O8 — Observation-operator consistency
Model and field data are compared only after both are transformed to the same \(\Delta_{\mathrm{val}}\), spatial support and metric definition.

Failure of O1–O8 blocks H1b.

---

# 8. Minimum evidence tiers for H1b

## Power

### Tier P-A
- direct interval served-energy data;
- independent outage/topology status;
- intact historical baseline data;
- independently observed demand drivers;
- critical-load mapping.

Eligible for confirmatory H1b if uncertainty is quantified.

### Tier P-B
- feeder/substation telemetry with defensible downstream allocation;
- independent topology/outage records;
- validated aggregate baseline.

Potentially eligible with larger propagated uncertainty.

### Tier P-C
- synthetic/benchmark or model-generated observations.

Verification only; not independent H1b validation truth.

## Transportation

### Tier T-A
- field/probe trajectory or vehicle re-identification supporting OD completion;
- boundary/count observations;
- independently validated requested-demand baseline;
- travel-time/state observations.

Eligible for confirmatory H1b if uncertainty is quantified.

### Tier T-B
- sampled/probe OD plus count-based expansion and documented coverage.

Potentially eligible with penetration/expansion uncertainty.

### Tier T-C
- traffic counts or NPMRDS travel time alone without OD reconstruction.

Useful for state validation but insufficient by itself for \(S_T\).

### Tier T-D
- synthetic/model-generated OD truth.

Verification only; not independent H1b truth.

---

# 9. Service-requirement architecture

Engineering significance is kept separate from mere detectability.

For sector \(s\), define a requirement set

\[
\mathcal K_s^^{%.req}
eq
=
\{g_{s,j}(Y,t)\le0,\ j=1,\dots,J_s\}.
\]

## 9.1 Power requirement examples

Potential requirement objects include:

- minimum service fraction for a documented critical-load class;
- maximum interruption/recovery duration;
- required restoration priority/order;
- minimum energy served over a specified emergency window.

The final source must be a case-specific utility/operator/regulatory/facility requirement.

## 9.2 Transportation requirement examples

Potential requirement objects include:

-� minimum completion/service fraction for a critical OD class;
- maximum corridor or emergency-access delay;
- minimum throughput for an evacuation/emergency corridor;
- recovery-time requirement.

The final source must be a case-specific agency/operator/emergency-management requirement.

---

# 10. How \(u_{\mathrm{eng}}\) may be admitted

A target is not automatically an engineering materiality increment.

For each candidate requirement record, identify:

\[
(\text{metric},\text{target},\text{tolerance},\text{time window},\text{population},\text{hazard domain}).
\]

## Case A — same metric and documented tolerance

If a requirement directly uses \(S_P\) or \(S_T\) and specifies an admissible tolerance \(\delta_s\),

\[
u_{\mathrm{eng},s}=\delta_s
\]

may be admitted after provenance review.

## Case B — different metric with validated transformation

If

\[
R=g(S_s)
\]

and \(g\) is validated and monotone over the relevant domain, the tolerance can be transformed with uncertainty propagation.

## Case C — different metric without validated transformation

Do **not** force it into \(u_{\mathrm{eng},s}\).

Instead, engineering significance is tested as a separate requirement-compliance question:

\[
M_1\in\mathcal K_s^^{req}
\qquad\text{versus}\qquad
M_2\in\mathcal K_s^{%.req}.
\]

This protects the thesis from falsely converting LOTTR, SAIDI, voltage limits or another native metric into a service-ratio percentage.

---

# 11. Service-requirement admissibility gates

## R1 — Authority
The requirement has an identifiable utility, regulator, transportation agency, emergency authority or critical-facility owner.

## R2 — Quantity
The native performance quantity and units are explicit.

## R3 — Context
The applicable service class, spatial domain, hazard/event and time horizon are explicit.

## R4 — Target
The target is documented before confirmatory model comparison.

## R5 — Tolerance
A tolerance/decision band must be explicit if the target is to define \(u_{\mathrm{eng}}\). Decimal formatting alone is not a tolerance.

## R6 — Mapping
Mapping to \(S_P\) or \(S_T\) is direct or independently validated.

## R7 — No model-result tuning
The requirement cannot be selected because one model crosses it and another does not.

---

# 12. Current freeze state

The architecture is now frozen:

\[
\boxed{
\mathcal O_P,\mathcal O_T,
\text{counterfactual-demand protocol},
\text{missing-data protocol},
\text{uncertainty propagation},
\text{requirement admissibility}
}
\]

but the values remain blocked:

\[
\boxed{
u_{\mathrm{obs},P},
u_{\mathrm{obs},T},
u_{\mathrm{eng},P},
u_{\mathrm{eng},T}
\text { require an actual case/data source.}
}
\]

Therefore

\[
\boxed{
\epsilon_P,\epsilon_T,\epsilon_{\mathrm{pred}}
\text { remain unfrozen.}
}
\]

---

# 13. Next executable gate

The next step is **Demonstrator + Validation-Data Selection**.

A candidate case is admissible only if it can satisfy enough of:

\[
\boxed{
\text{P-A/P-B observation}
+
\text{T-A/T-B observation}
+
\text{event truth}
+
\text{service-requirement provenance}.
}
\]

The next EGMIV operation is therefore:

\[
\boxed{
\text{candidate cases}
\rightarrow
\text{data-availability audit}
\rightarrow
\text{observation-tier score}
\rightarrow
\text{requirement-evidence score}
\rightarrow
\text{select minimal sufficient demonstrator}.
}
\]

No final H1 confirmatory simulation should be executed before that gate is passed.

---

# 14. Evidence anchors used to design this architecture

- IEC 62053-22:2020: transformer-operated active-energy meters, classes 0.1S/0.2S/0.5S; type-test scope.
- U.S. DOE FEMP M&V Guidelines v5.0: baseline conditions, measurement, weather/operating adjustments and validation planning.
- U.S. DOE EMIS guidance: expected-usage baseline models, weather/occupancy covariates, gap backfilling and tagging of modeled versus metered data.
- FHWA Traffic Monitoring Guide 2022: distinct volume, speed/travel-time and origin-destination data programs; probe technologies for OD data.
- FHWA Dynamic Traffic Assignment guidance: OD demand is sampled/estimated; congested measured volume may be capacity-constrained throughput rather than true demand.
- FHWA NPMRDS guidance: field-observed probe speed/travel time with 5-minute minimum temporal resolution; not a complete OD-demand source by itself.
- FHWA performance target-setting guidance: transportation targets are evidence/data driven and tied to agency objectives.
- PNNL critical-load resilience work: critical-load weighting has no one-size-fits-all rule.
- ASME VVUQ: verification, validation and uncertainty quantification are distinct credibility activities.
