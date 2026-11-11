# Report 2: Governing equations, physical semantics, and hypotheses

## A. Reduced oil-temperature dynamics

Conservation of energy motivates the conditional lumped relation

\[
 C_\mathrm{eff}\,\frac{d T_o}{dt}=P_{\mathrm{loss,eff}}(I,T_o)-H_{\mathrm{eff}}(T_o-T_a).
\]

A restricted effective one-hour map tested using SINTEF's measurements is

\[
 T_{o,t+1}=a T_{o,t}+(1-a)\left[T_{a,t}+d+g\big(I_t/I_\mathrm{ref}\big)^2\right],\qquad a=\exp(-1/\tau).
\]

The time unit in the exponential is one hour. The parameters \(\tau\) (hours), \(d\) (°C), and \(g\) (°C at current reference) are **effective regression coefficients**, not a uniquely identified transformer heat capacity, resistance or winding material property. The reference current is the training-subset median, not rated load. The fitted model contains no reactive-power loss decomposition, transient winding hot-spot constitutive equation or independent EVSE thermal state.

**Numerical verification** uses the exact zero-order-hold solution of the linear ODE and checks Euler versus RK4 timestep refinement. Model fit uses chronological 70%/30% split, with timestamp-contiguous one-hour pairs only; no crossing of missing-data gaps.

## B. Local inverse-problem sensitivity

Let \(\theta=(\log\tau,d,g)\). Define \(J_{ik}=\partial\widehat T_{i+1}/\partial\theta_k\), estimated by centered numerical differences; use singular values of column-normalized \(J\) as a **relative local conditioning diagnostic**, not a global proof of uniqueness. Construct a fixed-\(\tau\) objective profile by re-estimating the two linear parameters \(d\) and \(g\) for each grid value. This profile is not a confidence interval because the temporal residual structure and variance model have not been proven.

## C. Equal-current-square timing test

For each 24-hour uninterrupted observed SINTEF holdout window, define measured \(q_k=(I_k/I_\mathrm{ref})^2\). Compare the original ordering with descending and ascending permutations of **the same 24 recorded values**; initial oil temperature and the measured ambient-temperature path remain identical. Thus \(\sum_k q_k\) is exactly invariant. The fitted oil-temperature model still changes because its impulse-response kernel weights recent heating differently from earlier heating. This is *not* equal electrical energy, because voltage, power factor and load conversion are not held/verified across the permutations. This is not an EV-charging experiment.

## D. EPFL recorded-session evidence and offline LP

Let session \(i\) have observed arrival \(a_i\), departure \(b_i\), reported achieved energy \(E_i\), and the recorded session-field power maximum \(P_i^\max\). Define an **offline hypothetical** decision \(p_{it}\) and aggregate peak variable \(z\):

\[
 \min z,\quad 0\le p_{it}\le P_i^\max,\quad
 \sum_{t\in[a_i,b_i)}p_{it}\Delta t\ge E_i,\quad
 \sum_i p_{it}\le z.
\]

The numerical experiment uses one-minute decisions and only sessions whose observed windows are feasible. This is *not* an operational EV charging command; \(E_i\) is not independently established user-requested energy, and \(P_i^\max\) is not a verified charger manufacturer's rating. The comparison baseline is separate hypothetical immediate/front-loaded charging, *not measured site operation*.

## E. Model-based thermal EV scheduling is BLOCKED

A genuine EV charging to transformer dynamic mapping would require equipment topology, base load, AC voltage and power factor, allowable load, transformer thermal-loss relation, ambient forcing compatible with site, control constraints, and temporal synchronization. EPFL and SINTEF do not share these measurements. Therefore the candidate

\[
 \min_{\{p_{it}\}}\max_t T_{\mathrm{transformer}}(t)
\]

is **not numerically implemented** with arbitrary coupling coefficients or invented constraints. This is a deliberate evidence gate, not solver inability.

## F. Aging and reactive-power gates

A proposed insulation life acceleration formula requires applicable insulation type, temperature-location definition and a cited law applicable to this exact transformer before numerical interpretation. Percentile thresholds computed from measured data are *sample quantiles*, not physical safety limits.

If P and Q are in compatible physical units, one may calculate apparent power as \(S=\sqrt{P^2+Q^2}\). The current STREAM audit does not prove that requirement or the station electrical nameplates, so only a **numeric native-unit norm** is reported, not a loading percentage or thermal-loss reduction.

## Falsifiable experiments executed

- H1: whether a single effective thermal parameter set is stable across three 2024 calendar periods. Result: **it varies**; this alone neither proves structural nonidentifiability nor identifies the source of variation.
- H2a: whether measured current temporal order matters to fitted oil temperatures under equal integral of current squared. Result: **yes in the fitted model**, across 106 held-out windows.
- H2b: whether the EPFL data independently reveal charging arrival/stay/achieved-energy dependencies. Result: **yes descriptively**; causal EV penetration and linked transformer thermal effects are unresolved.
- H3: thermal-constrained EPFL optimization versus peak-only scheduling. **BLOCKED** for missing power-to-thermal transfer.
- H4: uncertainty in fitted thermal model. Partial: a chronological residual-band diagnostic, with no exchangeability guarantee or qualified critical threshold.
- H5: can STREAM station P/Q establish thermal losses? **BLOCKED** without units, voltage, ratings and exact topology.
