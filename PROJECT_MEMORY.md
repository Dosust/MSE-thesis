# Project Memory Entry Point

![Framework](https://img.shields.io/badge/stages%201--7-FROZEN-1A7F37)
![Method](https://img.shields.io/badge/EGMIV-v1.0-0969DA)
![Hypotheses](https://img.shields.io/badge/H1--H5%20logic-FROZEN-1A7F37)
![Search](https://img.shields.io/badge/evidence%20search-FRESH%20FROM%20ZERO-1A7F37)
![FTEE](https://img.shields.io/badge/FTEE%20v2.0-CURRENT-0969DA)
![H1](https://img.shields.io/badge/M0%20M1%20M2-VERIFIED-1A7F37)
![Prereg](https://img.shields.io/badge/H1%20confirmatory%20design-FROZEN-1A7F37)

## Repository authority — updated 2026-09-14

The sole active repository is `Dossiya-SE/MSE-thesis`. The thesis-wide citation standard is APA 7. The reasoning protocol is `project/RESEARCH_REASONING_PROTOCOL.md`; the named evidence-to-model execution method is `project/EGMIV_METHOD_V1.md`.

## Active authority order

1. `project/README.md`
2. `project/RESEARCH_REASONING_PROTOCOL.md`
3. `project/EGMIV_METHOD_V1.md`
4. `project/THESIS_SCOPE.md`
5. `project/CANONICAL_7_STAGE_FRAMEWORK.md`
6. `project/CANONICAL_SYSTEM_DEFINITION.md`
7. `project/FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md`
8. stage-specific frozen specifications
9. `project/RESEARCH_HYPOTHESES.md`
10. `project/ENGINEERING_CONFIRMATORY_HYPOTHESIS_MATRIX.md`
11. `project/H1_MATHEMATICAL_MODEL_SPECIFICATION_V1.md`
12. `project/H1_CONFIRMATORY_PREREGISTRATION_V1.md` — **current confirmatory design authority**
13. `project/MINIMAL_SUFFICIENT_EXPERIMENTAL_REALIZATION.md`
14. `project/FRESH_SEARCH_FULL_TEXT_EVIDENCE_TO_EQUATION_PROTOCOL_FTEE_V2.md`
15. `project/H1_FRESH_EVIDENCE_SEARCH_PROTOCOL_V1.md`

## Canonical scientific state

```math
\mathcal S=\{P,T,I,O\},
```

with P,T as physical infrastructures and I,O as informational and organizational layers. H1 remains confined to the physical P–T boundary

```math
\mathcal G_{H1}=\mathcal G_P\cup\mathcal G_T\cup\mathcal C.
```

The canonical interdependency object remains

```math
\mathfrak I_{ij}^{\alpha\beta}
=
\left(E_i^\alpha,E_j^\beta,M_{ij},w_{ij},\delta_{ij},\tau_{ij},a_{ij},m,\mathcal H_t\right).
```

## H1 formal evidence status

The frozen formal search remains

```math
Q_{H_1}^{CORE}=B_P\land B_T\land B_I,
```

with the dynamic block diagnostic only. Authenticated Scopus, Web of Science Core Collection, Compendex and IEEE Xplore execution remains pending. Public evidence is supportive/provisional only.

## H1 model state

All three competing representations are implemented and verification-frozen:

```math
\boxed{M_0=\text{independent},\qquad M_1=\text{static/algebraic coupling},\qquad M_2=\text{dynamic causal coupling}.}
```

- `models/H1/M0/`: verified 13/13.
- `models/H1/M1/`: verified 13/13 M1-specific gates.
- `models/H1/M2/`: verified full M1+M2 regression 29/29.

Nested limits pass:

```math
M_1\rightarrow M_0
```

when interface maps are removed, and

```math
\boxed{M_2\rightarrow M_1}
```

when charger memory is suppressed and dynamic repair is disabled.

M2 contains only the dynamic objects necessary for H1:

```math
q_c(k),\qquad d_j(k),\qquad r_j(k),
```

representing charging backlog, crew-path progress and repair progress. Benchmark analytical checks remain verification only and are `BENCHMARK_TEST_HARNESS_ONLY`.

## H1 confirmatory pre-registration — frozen v1.0

Canonical file: `project/H1_CONFIRMATORY_PREREGISTRATION_V1.md`.

Machine-readable records: `evidence/H1/08_preregistration/`.

The decisive H1a comparison is M2 vs M1. M2 vs M0 is secondary context.

The matched scenario universe is frozen as

```math
\Omega_H=
\Omega_0\cup\Omega_C\cup\Omega_O\cup\Omega_R\cup\Omega_J\cup\Omega_D,
```

covering intact/null, charging stress, feeder outage, road-to-repair stress, joint disruption and decoupling/zero-memory controls.

For every scenario, M0/M1/M2 receive identical initial state, external disturbance, demand, shared parameter draw, horizon and time step. Common random numbers are mandatory for stochastic comparisons.

### Primary H1a endpoint

For independently derived service-resolution thresholds \(\epsilon_P,\epsilon_T\),

```math
D_{PT}^{2,1}(\omega)=
\frac1T\int_0^T
\left[
\left(\frac{S_P^{M_2}-S_P^{M_1}}{\epsilon_P}\right)^2+
\left(\frac{S_T^{M_2}-S_T^{M_1}}{\epsilon_T}\right)^2
\right]^{1/2}dt,
```

with population statistic

```math
\Theta_{repr}=\mathbb E_{\omega\sim\Omega_H}[D_{PT}^{2,1}(\omega)].
```

### Threshold rule

For service s,

```math
\epsilon_s^{det}=\max(u_{obs,s},u_{num,s}).
```

If an externally defensible engineering tolerance exists,

```math
\boxed{\epsilon_s=\max(u_{eng,s},u_{obs,s},u_{num,s}).}
```

If no defensible \(u_{eng,s}\) exists, H1a may support only **representation-distinguishable**, not **engineering-material**.

No threshold may be chosen from observed M2–M1 effect sizes.

### UQ/statistics lock

- Tier A/B parameters may enter confirmatory UQ/calibration; Tier C remains sensitivity-only.
- Same uncertain draw supplied to M0/M1/M2.
- Sampling precision stops only when the 95% Monte Carlo interval half-width for the primary statistic is no larger than `0.1 × frozen decision scale`.
- Global variance-based sensitivity is allowed only after input-dependence audit.
- Paired bootstrap default: 5,000 resamples; 95% intervals.
- P-values are secondary to effect size + uncertainty + threshold comparison.

### H1a gates

A0 verification/physics; A1 independent threshold validity; A2 95% paired interval for \(\Theta_{repr}\) wholly above 1; A3 UQ robustness; A4 no M2 advantage from greater physical violation.

Adjudication:

- **SUPPORTED** only if A0–A4 pass and engineering tolerances are independently available.
- **REPRESENTATION-DISTINGUISHABLE** if A0–A4 pass but only detectability thresholds exist.
- **PARTIAL** if the effect is confined to a predeclared mechanism stratum.
- **NOT SUPPORTED** otherwise.

### H1b shell

H1b requires independent event/case truth. Synthetic self-generated truth alone cannot confirm it. The primary held-out error is

```math
E_{PT}(M)=\frac1T\int_0^T\|\widehat S_M(t)-S_{obs}(t)\|_Wdt.
```

M2 must beat the best M0/M1 held-out error beyond an independently frozen \(\epsilon_{pred}\), while preserving physics, uncertainty calibration, identifiability and no test-data refitting. If independent truth is unavailable, H1b is **NOT YET TESTABLE**.

## Anti-bias lock

After preregistration:

1. no primary outcome may be changed because another metric produces a stronger result;
2. no threshold may change after viewing confirmatory model differences;
3. no scenario may be removed because it weakens H1;
4. no M2 state/parameter may be added using held-out performance;
5. substantive protocol changes create v2.0 while v1.0 remains archived;
6. benchmark tests remain verification only;
7. final H1 confirmation still requires the authenticated four-database evidence branch.

## Immediate next task — current

The model and confirmatory-design stages are complete:

```math
\boxed{
M_0,M_1,M_2\;\checkmark
\rightarrow
\text{pre-registration}\;\checkmark
\rightarrow
\mathbf{threshold\ provenance\ acquisition}
\rightarrow
\text{scenario/parameter registry freeze}
\rightarrow
\text{confirmatory UQ execution}.
}
```

The next admissible work is to populate `evidence/H1/08_preregistration/threshold_provenance_template.csv` with independent sources for \(u_{obs,P},u_{num,P},u_{eng,P},u_{obs,T},u_{num,T},u_{eng,T}\) and the H1b noise floor. **Do not run final H1a confirmatory comparisons before those fields are frozen.**