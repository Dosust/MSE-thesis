# Project Memory Entry Point

![Framework](https://img.shields.io/badge/stages%201--7-FROZEN-1A7F37)
![Method](https://img.shields.io/badge/EGMIV-v1.0-0969DA)
![Hypotheses](https://img.shields.io/badge/H1--H5%20logic-FROZEN-1A7F37)
![Search](https://img.shields.io/badge/evidence%20search-FRESH%20FROM%20ZERO-1A7F37)
![FTEE](https://img.shields.io/badge/FTEE%20v2.0-CURRENT-0969DA)
![H1](https://img.shields.io/badge/M0%20M1%20M2-VERIFIED-1A7F37)
![325 Corpus](https://img.shields.io/badge/325--paper%20corpus-SECONDARY%20AUDIT-9A6700)

## Repository authority — updated 2026-09-14

The sole active repository is `Dossiya-SE/MSE-thesis`. `Dossiya-SE/Optimization-for-sustainability-and-resilience` is historical/reference only.

The thesis-wide citation standard is **APA 7th edition**. Proposed thesis constructs remain `[P]` until validation justifies another status.

The thesis-wide reasoning protocol remains [`project/RESEARCH_REASONING_PROTOCOL.md`](project/RESEARCH_REASONING_PROTOCOL.md), and the named evidence-to-model execution method is [`project/EGMIV_METHOD_V1.md`](project/EGMIV_METHOD_V1.md): **Evidence-Grounded Mechanistic Interdependency and Validation (EGMIV)**.

## Active authority order

1. [`project/README.md`](project/README.md)
2. [`project/RESEARCH_REASONING_PROTOCOL.md`](project/RESEARCH_REASONING_PROTOCOL.md)
3. [`project/EGMIV_METHOD_V1.md`](project/EGMIV_METHOD_V1.md)
4. [`project/THESIS_SCOPE.md`](project/THESIS_SCOPE.md)
5. [`project/CANONICAL_7_STAGE_FRAMEWORK.md`](project/CANONICAL_7_STAGE_FRAMEWORK.md)
6. [`project/CANONICAL_SYSTEM_DEFINITION.md`](project/CANONICAL_SYSTEM_DEFINITION.md)
7. [`project/FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md`](project/FULL_SYSTEM_OF_SYSTEMS_DEFINITION.md)
8. [`project/STAGE_2_INTERDEPENDENCY_MECHANISMS.md`](project/STAGE_2_INTERDEPENDENCY_MECHANISMS.md)
9. [`project/STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md`](project/STAGE_3_COUPLED_HYBRID_MULTISCALE_DYNAMICS.md)
10. [`project/STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md`](project/STAGE_4_OBSERVATION_ORGANIZATION_FEEDBACK_CONTROL.md)
11. [`project/STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md`](project/STAGE_5_CONTROLLED_SUSTAINABLE_VIABILITY.md)
12. [`project/STAGE_6_RESILIENCE_TO_SUSTAINABILITY_TRANSITION.md`](project/STAGE_6_RESILIENCE_TO_SUSTAINABILITY_TRANSITION.md)
13. [`project/STAGE_7_SUSTAINABLE_TRANSFORMATION_PATHWAYS.md`](project/STAGE_7_SUSTAINABLE_TRANSFORMATION_PATHWAYS.md)
14. [`project/RESEARCH_HYPOTHESES.md`](project/RESEARCH_HYPOTHESES.md)
15. [`project/ENGINEERING_CONFIRMATORY_HYPOTHESIS_MATRIX.md`](project/ENGINEERING_CONFIRMATORY_HYPOTHESIS_MATRIX.md)
16. [`project/H1_MATHEMATICAL_MODEL_SPECIFICATION_V1.md`](project/H1_MATHEMATICAL_MODEL_SPECIFICATION_V1.md)
17. [`project/MINIMAL_SUFFICIENT_EXPERIMENTAL_REALIZATION.md`](project/MINIMAL_SUFFICIENT_EXPERIMENTAL_REALIZATION.md)
18. [`project/FRESH_SEARCH_FULL_TEXT_EVIDENCE_TO_EQUATION_PROTOCOL_FTEE_V2.md`](project/FRESH_SEARCH_FULL_TEXT_EVIDENCE_TO_EQUATION_PROTOCOL_FTEE_V2.md)
19. [`project/H1_FRESH_EVIDENCE_SEARCH_PROTOCOL_V1.md`](project/H1_FRESH_EVIDENCE_SEARCH_PROTOCOL_V1.md)

## Canonical scientific state

```math
\mathcal S=\{P,T,I,O\},
```

with $P,T$ as physical infrastructure systems and $I,O$ as informational and organizational layers.

The primary confirmatory set remains

```math
\mathbb H=\{H_1,H_2,H_3,H_4,H_5\}.
```

The canonical interdependency object remains

```math
\mathfrak I_{ij}^{\alpha\beta}
=
\left(E_i^\alpha,E_j^\beta,M_{ij},w_{ij},\delta_{ij},\tau_{ij},a_{ij},m,\mathcal H_t\right).
```

## H1 formal evidence status

The frozen H1 formal CORE search remains

```math
Q_{H_1}^{\rm CORE}=B_P\land B_T\land B_I,
```

with $B_D$ diagnostic only. Authenticated execution in Scopus, Web of Science Core Collection, Compendex and IEEE Xplore is still pending. Public evidence remains supportive/provisional and does not replace the confirmatory corpus.

## H1 competing-model state

The physical boundary remains

```math
\mathcal G_{H1}=\mathcal G_P\cup\mathcal G_T\cup\mathcal C.
```

The three competing representations are now all implemented and verification-frozen:

```math
\boxed{M_0=\text{independent},\qquad M_1=\text{static/algebraic coupling},\qquad M_2=\text{dynamic causal coupling}.}
```

### M0

Package: [`models/H1/M0/`](models/H1/M0/)  
Status: **verified — 13 passed, 0 failed**.

### M1

Package: [`models/H1/M1/`](models/H1/M1/)  
Status: **verified — 13 M1-specific tests passed, 0 failed**.

M1 is memoryless. Requested EV charging power maps exactly once into electrical demand; bus energization limits same-step served power; no charger queue or dynamic repair state exists. The nested limit satisfies

```math
M_1\rightarrow M_0
```

when interface maps are removed.

### M2

Scientific record: [`models/H1/M2/`](models/H1/M2/)  
Status: **verified — full M1+M2 regression 29 passed, 0 failed**.

M2 adds only the dynamic states necessary to test temporal coupling beyond M1:

```math
q_c(k),\qquad d_j(k),\qquad r_j(k),
```

for charger backlog, repair-crew path progress and repair progress.

Physical charger memory is

```math
q_c(k+1)=\max\{0,q_c(k)+\Delta t[\lambda_c(k)-\mu_c(k)]\}.
```

The mandatory nesting condition passes:

```math
\boxed{M_2\rightarrow M_1\quad\text{when charger memory is suppressed and dynamic repair is disabled}.}
```

Dynamic repair also reduces exactly to the M1 static free-flow travel delay when road occupancy is zero and all path cells are available.

### Analytical M2 checks

Persistent-overload benchmark:

```math
\lambda=900\;\mathrm{veh/h},\qquad \mu_{max}=720\;\mathrm{veh/h},
```

so queue growth is analytically `180 veh/h`. Over `1.8 h`, predicted backlog is `324 vehicles`; simulation gives `324.0000000000011`.

Temporary-outage benchmark: a `0.2 h` outage at `600 veh/h` creates `120 vehicles` of backlog. Post-restoration spare service capacity is `120 veh/h`, so the closed-form clearance time is `1.0 h`; simulation clears from `t=0.6 h` to `t=1.6 h` exactly.

Dynamic repair benchmark S3R: static free-flow restoration is `0.14 h`; state-dependent repair under initially congested roads is `0.19 h` with unchanged power network and repair productivity.

These are verification/analytical-consistency results only. They are **not** confirmatory H1 effect sizes and remain `BENCHMARK_TEST_HARNESS_ONLY`.

## Deliberate M2 boundary

The minimal M2 keeps the CTM state identical to M1 and lets charger backlog modify mobility service through FCFS current-arrival fulfillment. This isolates interface memory from additional route-choice/rerouting behavior. Richer queue spillback, route choice, price response, multi-crew allocation and informational/organizational dynamics remain deferred unless evidence and H1 validation require them.

## Immediate next task — current

The executable model-construction sequence is complete:

```math
\boxed{M_0\;\checkmark\rightarrow M_1\;\checkmark\rightarrow M_2\;\checkmark.}
```

The next EGMIV operation is **H1a pre-registration before confirmatory comparison**:

```math
\boxed{
M_0,M_1,M_2
\rightarrow
\Omega_H\text{ matched scenario set}
\rightarrow
\varepsilon_{repr},\varepsilon_{pred}\text{ predeclaration}
\rightarrow
\text{parameter/UQ plan}
\rightarrow
\text{held-out validation design}.
}
```

We must freeze the scenario universe, primary outcomes, engineering-resolution thresholds, uncertainty distributions, sensitivity method, stopping rules, and validation split **before** examining confirmatory M0/M1/M2 results. No final H1 conclusion is permitted until these gates and the authenticated four-database evidence corpus are complete.