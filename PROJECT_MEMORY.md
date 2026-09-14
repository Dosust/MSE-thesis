# Project Memory Entry Point

![Framework](https://img.shields.io/badge/stages%201--7-FROZEN-1A7F37)
![Method](https://img.shields.io/badge/EGMIV-v1.0-0969DA)
![H1 Models](https://img.shields.io/badge/M0%20M1%20M2-VERIFIED-1A7F37)
![Prereg](https://img.shields.io/badge/H1%20confirmatory%20design-FROZEN-1A7F37)
![Thresholds](https://img.shields.io/badge/provenance-PARTIALLY%20FROZEN-9A6700)

## Repository authority — updated 2026-09-14

The sole active repository is `Dossiya-SE/MSE-thesis`. The thesis-wide citation standard is APA 7. The canonical reasoning protocol is `project/RESEARCH_REASONING_PROTOCOL.md`; the named evidence-to-model execution method is `project/EGMIV_METHOD_V1.md`.

## Active H1 authority

1. `project/H1_MATHEMATICAL_MODEL_SPECIFICATION_V1.md`
2. `project/H1_CONFIRMATORY_PREREGISTRATION_V1.md`
3. `project/H1_THRESHOLD_PROVENANCE_V1.md` — **current threshold authority**
4. `models/H1/M0/`, `models/H1/M1/`, `models/H1/M2/`
5. `evidence/H1/07_audit/`
6. `project/H1_FRESH_EVIDENCE_SEARCH_PROTOCOL_V1.md`

## Canonical scientific state

```math
\mathcal S=\{P,T,I,O\},
```

with H1 confined to the physical Power–Transportation boundary

```math
\mathcal G_{H1}=\mathcal G_P\cup\mathcal G_T\cup\mathcal C.
```

The competing H1 representations are

```math
\boxed{M_0=\text{independent},\qquad M_1=\text{static/algebraic coupling},\qquad M_2=\text{dynamic causal coupling}.}
```

Verification state:

- M0: 13/13 passed.
- M1: 13/13 M1-specific passed.
- M2: 29/29 full M1+M2 regression passed.

Nested limits pass:

```math
M_1\rightarrow M_0,
\qquad
M_2\rightarrow M_1.
```

All benchmark effect sizes remain verification-only and `BENCHMARK_TEST_HARNESS_ONLY`.

## H1 confirmatory pre-registration — frozen v1.0

Primary comparison: **M2 vs M1**. M2 vs M0 is secondary.

Scenario universe:

```math
\Omega_H=\Omega_0\cup\Omega_C\cup\Omega_O\cup\Omega_R\cup\Omega_J\cup\Omega_D.
```

Primary statistic:

```math
D_{PT}^{2,1}(\omega)=\frac1T\int_0^T\left[\left(\frac{S_P^{M_2}-S_P^{M_1}}{\epsilon_P}\right)^2+\left(\frac{S_T^{M_2}-S_T^{M_1}}{\epsilon_T}\right)^2\right]^{1/2}dt,
```

```math
\Theta_{repr}=\mathbb E_{\omega\sim\Omega_H}[D_{PT}^{2,1}(\omega)].
```

Thresholds may not be selected from observed M2−M1 effects.

## Threshold provenance — executed v1.0

The threshold study follows

```math
\text{evidence}\rightarrow\text{native quantity}\rightarrow\text{mapping}\rightarrow\text{uncertainty}\rightarrow\text{admissibility}\rightarrow\epsilon.
```

### Numerical uncertainty — frozen for minimal demonstrator v1

Using M2 refinement from `Delta t=0.00125 h` to `0.000625 h`, with an additional finer check at `0.0003125 h`:

```math
\boxed{u_{num,P}=0.000416667}
```

```math
\boxed{u_{num,T}=0.001281963}
```

corresponding to approximately `0.0417%` and `0.1282%` of full service scale.

The current H1 minimal-demonstrator confirmatory time step is therefore frozen at

```math
\boxed{\Delta t=0.00125\;\mathrm{h}=4.5\;\mathrm{s}}.
```

If topology, CTM cell size, event discretization or solver changes materially, rerun this numerical provenance.

### Power observation uncertainty — not frozen

IEC meter accuracy classes provide instrument-performance evidence only. They do not capture the full uncertainty of

```math
S_P(t)=\frac{\sum_i\omega_i p_i^{srv}(t)}{\sum_i\omega_i p_i^d(t)},
```

because outage-period demand contains a counterfactual component.

Required structure:

```math
u_{obs,P}=\mathcal U(u_{meter},u_{counterfactual\ demand},u_{aggregation},u_{temporal},\Sigma_P).
```

Conditional instrument-only examples are recorded in the evidence ledger; they are not final thresholds.

### Transportation observation uncertainty — not frozen

FHWA detector accuracy/QA evidence does not directly equal uncertainty in

```math
S_T=\frac{\text{weighted completed OD flow}}{\text{weighted requested OD flow}}.
```

Required structure:

```math
u_{obs,T}=\mathcal U(u_{count},u_{OD},u_{coverage},u_{trajectory\ matching},u_{temporal},\Sigma_T).
```

### Engineering significance — not universal

Power-resilience evidence does not support a universal `u_eng,P`; transportation performance guidance does not support a universal `u_eng,T` for our service ratio. Both must be tied to the selected demonstrator's service requirements.

Therefore:

```math
\boxed{\epsilon_P\;\text{NOT YET FROZEN},\qquad\epsilon_T\;\text{NOT YET FROZEN},\qquad\epsilon_{pred}\;\text{NOT YET COMPUTABLE}.}
```

This restriction prevents borrowing incompatible voltage, SAIDI/SAIFI, LOTTR/TTI or arbitrary round-number thresholds.

## Formal H1 evidence status

Authenticated execution of the frozen Scopus, Web of Science Core Collection, Compendex and IEEE Xplore H1 CORE searches remains pending. Public evidence remains supportive/provisional only. Final H1 confirmation is prohibited until the formal corpus is completed and reconciled.

## Immediate next task — current

The admissible progression is now

```math
\boxed{M_0,M_1,M_2\;\checkmark\rightarrow\text{pre-registration}\;\checkmark\rightarrow\text{numerical threshold provenance}\;\checkmark\rightarrow\mathbf{observation\ architecture+service\ requirements}\rightarrow\epsilon_P,\epsilon_T\rightarrow\text{confirmatory UQ}.}
```

The next task is to define the **actual validation observation architecture** for Power and Transportation and the **case-specific engineering service requirements**. Only then can `u_obs,P`, `u_obs,T`, `u_eng,P`, `u_eng,T`, `epsilon_P`, `epsilon_T`, and later `epsilon_pred` be frozen. Do not run final H1a confirmatory comparisons before this gate is complete.