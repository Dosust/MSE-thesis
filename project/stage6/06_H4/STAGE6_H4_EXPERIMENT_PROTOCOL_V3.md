# Stage 6 H4 Experiment Protocol v3

**Status:** CANONICAL STAGE-6 H4 PROTOCOL — RQ/SO/H v4 ALIGNED  
**Effective date:** 2026-09-20  
**Supersedes:** `STAGE6_H4_EXPERIMENT_PROTOCOL_V2.md` for primary H4 interpretation.  
**Hypothesis authority:** `project/CANONICAL_RQ_SO_HYPOTHESES_V4.md`  
**Empirical status:** H4 NOT TESTED.

## 1. Official H4

> **H4:** Across the prespecified intervention and scenario set, at least two resilience-effective engineering interventions produce materially different resource requirements, resource efficiencies, or admitted sustainability consequences under the declared comparison rule.

This protocol tests consequence heterogeneity among **resilience-effective** alternatives. Interface criticality remains a supporting diagnostic and is not primary H4.

## 2. Experimental unit and matched conditions

For intervention (a_k) and scenario (omega_s),

```math
e=(a_k,omega_s,Y_0,mathfrak M^0,u/pi,FU_6,mathcal B,H,Pi).
```

Across matched intervention arms, hold fixed all quantities not explicitly designated as intervention-dependent, including hazard realization, initial state, service requirements, functional unit, accounting boundaries, horizon, data/factor versions, and uncertainty semantics.

## 3. Physical and causal qualification

```math
a_kinmathcal A_6^{qual}
iff
G_{6-PHY}(a_k)=PASS
land
G_{6-CAUSAL}(a_k)=PASS
land
G_{6-BOUNDARY}(a_k)=PASS.
```

Missing mandatory evidence produces BLOCKED/NOT TESTED, not a zero consequence.

## 4. Resilience-effective eligibility

```math
oxed{
mathcal A_{H4}
=
mathcal A_R^+
=
{a_kinmathcal A_6^{qual}:
Deltamathcal M_R(a_k)gedelta_R}.
}
```

The resilience functional (mathcal M_R), aggregation rule, and (delta_R) must be prospectively frozen.

## 5. Typed intervention-consequence object

For every H4-eligible intervention,

```math
oxed{
mathcal C_6(a_k)
=
left(
Deltamathfrak R^{a_k},
mathbf r^{a_k},
mathcal E_{m fx}^{a_k},
mathcal E_{m fy}^{a_k},
Deltamathbf J_{m sus}^{a_k},
mathbb U^{a_k},
Lambda^{a_k}
ight).
}
```

The types are distinct:

```math
oxed{
	ext{resilience effect}

eq
	ext{resource requirement}

eq
	ext{resource efficiency}

eq
	ext{sustainability consequence}.
}
```

### Resource vector

The core admitted resource vector is

```math
oxed{
mathbf r_{m core}^{a_k}
subseteq
left(
C_{m direct}^{a_k},
E_{m op}^{a_k}
ight),
}
```

with crew/person-hours or other resources admitted only through the sustainability/resource governance process.

### Resource efficiency

(mathcal E_{m fy}) must be computed only from qualified resource quantities and a declared achieved-effect denominator. No universal scalar efficiency score is assumed.

### Admitted sustainability consequences

The core admitted environmental sustainability consequence is

```math
oxed{
mathbf J_{m sus,core}^{a_k}
subseteq
left(
CO_{2e}^{a_k}
ight).
}
```

Distributional accessibility/equity is conditional on construct, population, geography, data, and accounting qualification. Cost and operational energy are not relabeled as sustainability solely because they enter the decision.

## 6. Material-difference test

For native-unit resource dimensions (rinmathcal Q_r), efficiency dimensions (einmathcal Q_{fy}), and admitted sustainability dimensions (sinmathcal Q_{sus}), prospectively freeze materiality thresholds
(delta_{r,r}>0), (delta_{fy,e}>0), and (delta_{sus,s}>0).

Define

```math
D_r(a_i,a_j)=
max_{rinmathcal Q_r}
rac{|r_r(a_i)-r_r(a_j)|}{delta_{r,r}},
```

```math
D_{m fy}(a_i,a_j)=
max_{einmathcal Q_{fy}}
rac{|mathcal E_{{m fy},e}(a_i)-mathcal E_{{m fy},e}(a_j)|}{delta_{fy,e}},
```

and

```math
D_{m sus}(a_i,a_j)=
max_{sinmathcal Q_{sus}}
rac{|Delta J_s(a_i)-Delta J_s(a_j)|}{delta_{sus,s}}.
```

The primary H4 material-difference detector is

```math
oxed{
D_4(a_i,a_j)=
max{D_r,D_{m fy},D_{m sus}}.
}
```

Primary confirmatory condition:

```math
oxed{
exists a_i,a_jinmathcal A_R^+:
D_4(a_i,a_j)ge1.
}
```

This is a heterogeneity detector, not a weighted sustainability utility function.

## 7. Secondary analyses

Matched-resilience, matched-effectiveness, and matched-resource analyses may be preregistered to reduce confounding by intervention scale. Interface-criticality targeting may be evaluated as a supporting diagnostic against structural/flow baselines, but such a test is not H4 unless separately authorized.

## 8. Uncertainty and VVUQ

Uncertainty must be propagated separately for (Deltamathfrak R), (mathbf r), (mathcal E_{m fx}), (mathcal E_{m fy}), and (Deltamathbf J_{m sus}). Probability is used only when a probability model is defensible; otherwise use scenario, interval, sensitivity, or robust semantics.

## 9. Adjudication

**SUPPORTED:** at least two qualified resilience-effective interventions exist and the preregistered (D_4) criterion is satisfied with required VVUQ.

**NOT SUPPORTED:** a valid comparison executes with at least two qualified resilience-effective interventions and (D_4<1) under the preregistered aggregation rule.

**NOT TESTED:** any prerequisite blocks the intended experiment, including an insufficient intervention set, missing resource/efficiency/sustainability quantities required by the registered test, invalid boundaries, failed qualification, or failed VVUQ.

## 10. Claim boundary

Stage 6 may report intervention effects and typed consequences. It does not select the preferred intervention; that is Stage 7.
