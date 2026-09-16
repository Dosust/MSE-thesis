# Autonomous Thesis Execution Protocol v1.0

**Status:** ACTIVE WORKING CONTROL PROTOCOL  
**Authorization date:** 2026-09-16  
**Repository:** `Dossiya-SE/MSE-thesis`  
**Method:** EGMIV + thesis-wide reasoning protocol  
**Purpose:** execute the thesis research program sequentially with the minimum necessary user interruption while preserving scientific, ASU, and repository controls.

## 1. Governing principle

```math
\boxed{
\text{Execute automatically when scientifically admissible;}
\quad
\text{block explicitly when evidence, access, or human authority is required.}
}
```

Autonomy never permits inventing data, evidence, parameters, validation, ASU requirements, or approvals.

## 2. Authority hierarchy

```math
\boxed{
\text{ASU Graduate College}
>
\text{SSEBE/MSE requirements}
>
\text{chair/GSC decisions}
>
\text{approved style guide}
>
\text{canonical thesis files}
>
\text{working proposals}.
}
```

A lower-level rule cannot override a higher-level authority.

## 3. Scientific execution chain

All substantive work follows

```math
\boxed{
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
}
```

The EGMIV mechanism chain remains

```math
\boxed{
\text{Evidence}
\rightarrow
\text{Mechanism}
\rightarrow
\text{Interdependency}
\rightarrow
\text{Mathematical Model}
\rightarrow
\text{Competing Test}
\rightarrow
\text{Validation}
\rightarrow
\text{Engineering Claim}.
}
```

## 4. Current autonomous execution queue

The active novelty-and-foundation phase is executed in this order:

```math
\boxed{
\begin{aligned}
1.&\ \text{FTEE/EGMIV extraction of the ASU prior-work corpus}\\
2.&\ \text{global novelty falsification searches F0/F1/F2}\\
3.&\ \text{freeze established vs unresolved knowledge}\\
4.&\ \text{derive }\mathfrak d\rightarrow\mathfrak I\rightarrow\mathcal G_{\mathfrak I}(t)\\
5.&\ \text{formalize }p(Y\mid D)\text{ and }\mathcal U(z_I,z_O)\\
6.&\ \text{derive evidence-grounded }K_{\rm sus}\\
7.&\ \text{compute/test controlled }\mathcal V_{\rm sus}\\
8.&\ \text{derive and benchmark }S_{ij}^{\mathcal V}\\
9.&\ \text{preserve operational-control vs structural-transformation separation}\\
10.&\ \text{run matched falsifiable experiments and VVUQ}.
\end{aligned}
}
```

No downstream task may be upgraded to confirmatory status while an upstream prerequisite is scientifically blocking it.

## 5. Candidate novelty objects

Until globally falsified/qualified, the strongest candidate contributions remain

```math
\boxed{
\begin{aligned}
N_1 &: \text{causal dynamic }P\!\!-​T\!\!-​I\!\!-​O\text{ dependency grammar} && [H/U]\\
N_2 &: p(Y\mid D)\rightarrow\mathcal V_{\rm sus} && [H/U]\\
N_3 &: \mathcal V_{\rm sus}\rightarrow S_{ij}^{\mathcal V} && [H/U].
\end{aligned}
}
```

They must never be described as established novelty before global search and competing-method audit.

## 6. Scientific gates

A task advances only when its gate passes.

| Gate | Requirement |
|---|---|
| `G_A` Novelty | no equivalent integrated method identified within the qualified search domain |
| `G_B` Representation | `\mathfrak d`, `\mathfrak I`, and `\mathcal G_{\mathfrak I}` have explicit semantics, assumptions, units/domains where applicable, and admissible evidence |
| `G_C` Physics | constituent P and T models independently pass physical/numerical verification |
| `G_D` Coupling | nested limits and coupling-removal limits pass; matched baselines are available |
| `G_E` Uncertainty | uncertainty is propagated through the relevant chain rather than reported only post hoc |
| `G_F` Viability | `K_{\rm sus}`, controls, horizon, constraints, and viability computation are physically/mathematically defensible |
| `G_G` Criticality | viability-sensitive ranking is benchmarked against simpler structural/flow rankings under equal intervention conditions |

A failed gate produces a `FAIL` or `BLOCKED_*` state, not a forced continuation.

## 7. Execution status vocabulary

Only the following states are used:

- `PENDING` — not yet executed.
- `RUNNING` — actively being executed in the current active session.
- `PASS` — predefined gate satisfied.
- `FAIL` — predefined test/gate failed.
- `BLOCKED_EXTERNAL_ACCESS` — required authenticated, restricted, paywalled, or unavailable data/tool cannot be accessed.
- `BLOCKED_HUMAN_DECISION` — advisor/GSC/ASU/user authorization is inherently required.
- `BLOCKED_EVIDENCE` — evidence is insufficient to support the next scientific step.
- `DEFERRED_DEPENDENCY` — a prerequisite has not passed.
- `SUPERSEDED` — replaced by a newer controlled artifact.

## 8. No-question blocking rule

When a task is blocked, the workflow does **not** invent a substitute and does not automatically ask the user to resolve it.

Instead it shall:

1. record the exact blocker;
2. preserve all completed evidence/provenance;
3. mark dependent work `DEFERRED_DEPENDENCY`;
4. continue with the next scientifically independent task;
5. surface the blocker in the execution status/log.

Examples include authenticated Scopus/WoS/Compendex/IEEE execution, restricted utility datasets, advisor/GSC approval, ASU iPOS actions, and proprietary full text.

## 9. Evidence substitution rule

```math
\boxed{\text{Public support evidence}\neq\text{formal confirmatory corpus}.}
```

Public web evidence may develop theory, identify candidates, and audit plausibility. It may not silently replace an authenticated database search, held-out validation set, restricted primary data, or a required institutional approval.

## 10. Frozen-file protection

Frozen canonical files are not silently rewritten because new evidence appears.

New evidence first enters a versioned working/amendment artifact, for example:

`HYPOTHESIS_REFINEMENT_AFTER_ASU_AUDIT_V1.md`

Only after the amendment is scientifically reconciled may a canonical file be intentionally revised and its change documented.

## 11. Repository write discipline

For GitHub writes:

1. search/fetch before update;
2. obtain the current blob SHA for an existing file;
3. perform same-path writes sequentially;
4. use explicit commit messages;
5. verify the resulting file/directory state after mutation;
6. never overwrite provenance with a cleaner narrative.

## 12. Reproducibility and provenance

Every substantive output should expose, where applicable:

```math
\boxed{
\text{claim}
\rightarrow
\text{source/data}
\rightarrow
\text{mechanism}
\rightarrow
\text{equation/model}
\rightarrow
\text{assumptions}
\rightarrow
\text{test}
\rightarrow
\text{uncertainty}
\rightarrow
\text{validation domain}
\rightarrow
\text{thesis location}.
}
```

Search dates, search strings, source identifiers, model versions, code versions, parameter provenance, and blocked states must be retained.

## 13. Operational vs strategic decisions

The existing distinction remains mandatory:

```math
u(t)=\text{operational control},
\qquad
\mathbf a_k=\text{strategic transformation}.
```

Operational recovery optimization may not silently replace Stage-6/Stage-7 transformation logic.

## 14. Session persistence rule

Execution can proceed autonomously while an active tool-enabled session is running. It does not continue invisibly after the session stops. Persistent GitHub status/log files are therefore the restart point: on the next active run, work resumes from the first non-passed, non-blocked admissible task without requiring the research plan to be reconstructed.

## 15. Completion condition

The autonomous program is not complete because all files exist. It is complete only when every thesis-critical claim either:

- passes its evidence, model, test, uncertainty, and validation gates within a declared domain; or
- is explicitly rejected, bounded, or recorded as unresolved.

The final contribution is whatever survives the subtraction

```math
\boxed{
\mathcal N_{\rm thesis}
=
\mathcal C_{\rm proposed}
-
\mathcal C_{\rm ASU}
-
\mathcal C_{\rm external}
}
```

under the qualified search and validation domains.