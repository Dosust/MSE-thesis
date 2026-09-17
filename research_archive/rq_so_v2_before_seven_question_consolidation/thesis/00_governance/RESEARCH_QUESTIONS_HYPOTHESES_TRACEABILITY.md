# Research Question–Hypothesis Traceability Matrix

**Purpose:** guarantee that every research question is answered by a defined method and that every hypothesis appears consistently in methodology, results, discussion and conclusion.

## Governing chain

```math
\boxed{
RQ_i
\rightarrow H_i
\rightarrow \text{mechanism}
\rightarrow \text{model/baseline}
\rightarrow \text{data/domain}
\rightarrow \text{metric}
\rightarrow \text{result}
\rightarrow \text{discussion}
\rightarrow \text{conclusion}.
}
```

## Overarching system question

### RQ0
Can a causal, dynamic, evidence-grounded representation of physical, informational and organizational interdependencies improve the characterization and engineering management of coupled power–transportation resilience and sustainable transformation?

### Organizing hypothesis

`H_SYS`: physical-network structure alone is insufficient when causal interdependencies, dynamics, information, organization and feasible control materially influence propagation, viability and transformation pathways.

`H_SYS` is decomposed into `H1–H5`; it is not decided by one isolated statistical test.

## Traceability matrix

| RQ / H | Core question | Mechanism | Comparator / baseline | Primary decision object | Methodology location | Results location | Discussion / conclusion |
|---|---|---|---|---|---|---|---|
| RQ1 / H1 | Does dynamic causal P–T interdependency materially change disruption/service trajectories? | state/time/mode-dependent cross-system coupling | `M0` independent; `M1` static/algebraic; `M2` dynamic causal | `\Theta_{repr}` / declared trajectory difference and H1 decision gates | Ch.4.5 | Ch.5.1 | Ch.6.2–6.4 / Ch.7.1–7.2 |
| RQ2 / H2 | Do informational and organizational states materially change feasible response and recovery? | sensing/communication/estimation/authority/coordination alter `\mathcal U` and response time | physical-only vs +I vs +I+O nested models | response-set/timing + downstream service outcomes | Ch.4.6 | Ch.5.2 | Ch.6.2–6.7 / Ch.7.1–7.2 |
| RQ3 / H3 | Do controlled-viability quantities add decision-relevant information beyond conventional service/recovery metrics? | future maintainability differs from instantaneous performance | conventional predictor set vs conventional+viability | prespecified predictive/decision skill | Ch.4.7 | Ch.5.3 | Ch.6.2–6.6 / Ch.7.1–7.3 |
| RQ4 / H4 | Does viability-sensitive interface ranking identify better intervention targets than static/flow rankings? | interface perturbation changes dynamics → viability functional | degree, betweenness, flow vs `S_{ij}^{\mathcal V}` | `\Delta\mathcal M_{\mathcal V}` under equal budget | Ch.4.8 | Ch.5.4 | Ch.6.4–6.7 / Ch.7.1–7.4 |
| RQ5 / H5 | Do adaptive transformation pathways outperform fixed sequences under deep uncertainty? | trigger-based policy adapts to evolving regime/state/history | best prespecified fixed pathway vs adaptive policy | robustness/satisficing metric and objective vector `\mathbf J` | Ch.4.9 | Ch.5.5 | Ch.6.6–6.8 / Ch.7.1–7.5 |

## H1 current execution state

Repository authority currently records:

```math
\boxed{M_0=\text{independent},\quad M_1=\text{static/algebraic},\quad M_2=\text{dynamic causal}.}
```

- H1 model implementations: verified at current repository state.
- H1 confirmatory design/preregistration: frozen.
- Row-level acquisition/audit executor: code verified.
- Raw event-row retrieval and qualification: pending/blocking.
- Candidate train/test split: not frozen until row-level R1–R8 gates pass.
- Confirmatory H1 calibration/run: not authorized before that activation.

## Traceability defect rules

A defect exists if any of the following occurs:

1. an RQ has no hypothesis/developmental objective or no method;
2. a hypothesis is introduced in Chapter 1 but absent from Chapter 4;
3. a Chapter 5 result has no Chapter 4 method or is not marked exploratory;
4. a Chapter 6 interpretation lacks a registered result/evidence chain;
5. a Chapter 7 conclusion is stronger than the corresponding evidence/test supports;
6. a threshold/decision rule is introduced after observing confirmatory results without an explicit exploratory amendment.

## Change control

Hypothesis logic remains governed by `../../project/RESEARCH_HYPOTHESES.md`. This file maps that canonical logic into the thesis document; it does not silently redefine the hypotheses.
