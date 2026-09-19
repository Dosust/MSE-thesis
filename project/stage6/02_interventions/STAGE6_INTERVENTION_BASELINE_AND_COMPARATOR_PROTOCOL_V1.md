# Stage 6 Intervention, Baseline and Comparator Protocol v1

## 1. Intervention eligibility

A candidate \(a_k\) enters Stage 6 only if:

1. its target object exists in the qualified thesis model;
2. its mechanism is physically/organizationally interpretable;
3. required parameters/resources can be defined or bounded;
4. implementation does not rely on an unqualified cross-system causal arrow;
5. its consequences can be mapped to the common functional-service boundary;
6. its lifecycle inventory can be represented at the claim level intended.

## 2. Intervention taxonomy

The design permits the following classes, subject to upstream qualification:

### P — Power-side physical
Examples: capacity reinforcement, redundancy, protection/automation changes, distributed energy/storage, hardened assets.

### T — Transportation-side physical
Examples: corridor hardening/capacity, redundancy, restoration-resource changes, charging-location access changes.

### PT — Qualified coupled-interface
Examples: charging infrastructure siting/sizing or interface-capacity modifications when the relevant P–T mechanism has passed Stage 2/3 qualification.

### I/O — Information/organization
Examples: sensing, communication, coordination, resource/authority changes only where Stage 4 has defined their mechanism and feasible-action effect.

An intervention label is not sufficient; the intervention operator must be executable.

## 3. Primary baseline

\[
\boxed{a_0=\text{status quo / no additional strategic intervention}}
\]

All ordinary operational controls already allowed by \(\mathcal U_{\rm feas}\) remain available.

Thus the intervention contrast is not:

\[
\text{control versus no control},
\]

but:

\[
\boxed{
\text{same operating regime + same scenario}
\quad
a_0
\;\text{versus}\;
a_k.
}
\]

NIST's Economic Decision Guide explicitly uses the status quo/do-nothing condition as the economic reference for resilience investments.

## 4. Business-as-usual alternative

If a literal do-nothing case is physically impossible over \(H_{LC}\) because scheduled replacement/maintenance is unavoidable, define:

\[
a_{\rm BAU}=\text{current-practice / minimum-required lifecycle action}.
\]

The protocol must freeze whether \(a_0\) or \(a_{\rm BAU}\) is the primary counterfactual before confirmatory results are inspected.

## 5. Incremental resilience and sustainability consequences

Under matched scenario \(\omega\),

\[
\Delta\mathfrak R(a_k,\omega)
=
\mathfrak R(\mathfrak M^{a_k},\omega)
-
\mathfrak R(\mathfrak M^{a_0},\omega),
\]

and for each sustainability component \(q\),

\[
\boxed{
\Delta J_q(a_k,\omega)
=
J_q(a_k,\omega)-J_q(a_0,\omega).
}
\]

Sign conventions must be frozen. For burden variables such as carbon/cost/energy, positive \(\Delta J_q\) normally means a larger burden unless the case protocol defines an alternative convention.

## 6. Resilience-effective intervention set

\[
\boxed{
\mathcal A_R^+
=
\left\{
a_k\in\mathcal A_6:
\Delta\mathcal M_R(a_k)\ge\delta_R
\right\}.
}
\]

\(\mathcal M_R\) is a Stage-5-derived decision functional. \(\delta_R\) must be frozen before the H4 confirmatory intervention comparison.

## 7. Comparator architecture

Stage 6 distinguishes baseline from benchmark.

### C0 — status-quo counterfactual

\[
C_0=a_0\text{ or }a_{\rm BAU}.
\]

Purpose: incremental consequence measurement.

### C1 — resilience-effective alternatives

\[
C_1=\mathcal A_R^+.
\]

Purpose: H4 consequence heterogeneity.

### C2 — matched-resilience alternatives

Where possible, compare interventions with similar resilience gain:

\[
\left|
\Delta\mathcal M_R(a_i)
-
\Delta\mathcal M_R(a_j)
\right|
\le
\epsilon_R,
\]

with \(\epsilon_R\) derived prospectively from Stage-5 numerical/engineering resolution.

This is preferred when the scientific goal is to isolate sustainability differences rather than simply compare a strong intervention with a weak one.

### C3 — conventional/current-practice engineering comparator

Include only if a real current-practice or code/utility/agency intervention is available and its scope is comparable.

It is not invented solely to make the thesis method look better.

## 8. Resource efficiency

For positive, resolvable incremental resource use \(R_m(a)>0\),

\[
\eta_{R,m}(a)
=
\frac{\Delta\mathcal M_R(a)}
{\Delta R_m(a)}.
\]

Candidate denominators include incremental cost, energy, material quantity or carbon burden.

Ratio efficiency is not reported if the denominator crosses zero or is indistinguishable from zero relative to uncertainty. In that case report the ordered pair:

\[
\left(
\Delta\mathcal M_R,
\Delta R_m
\right)
\]

rather than stabilizing the ratio with an arbitrary constant.

## 9. No premature Stage-7 decision

Stage 6 may identify:

- resilience-effective interventions;
- dominated interventions on strictly physical/accounting grounds;
- consequence heterogeneity;
- candidate requirements.

It may not declare the “best” intervention by applying unapproved cross-dimensional weights. Multiobjective selection belongs to Stage 7.

## 10. Physics gate

For every \(a_k\):

\[
G_{6-PHY}(a_k)
=
G_P
\land
G_T
\land
G_{PT}
\land
G_{\rm impl}.
\]

Examples of required checks include:

- power balance and electrical operating constraints;
- transport flow/capacity/state admissibility;
- EV/charging energy consistency where applicable;
- topology/connectivity;
- feasible construction/asset sizing;
- interface direction and units;
- consistency with declared intervention service life.

A sustainability result from a physically impossible intervention is invalid.
