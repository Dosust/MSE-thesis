# MSE Thesis — Adaptive Visual CI Infrastructure Exception

![Status](https://img.shields.io/badge/status-HISTORICAL%20%2F%20SUPERSEDED-6B7280)

> **ARCHIVE WARNING:** This file is a historical CI/visual-governance record from 2026-08-22. Its P–W–T–SW and earlier chain notation is preserved only for provenance and is **not current thesis scientific authority**. For current P–T–I–O mathematics and framework status, start with [`README.md`](README.md) and [`THESIS_SCOPE.md`](THESIS_SCOPE.md).

**Date:** 2026-08-22  
**Scope:** V4 presentation changes only

- `assets/math-art/master_architecture.svg`
- `project/MATHEMATICAL_PRESENTATION_V3.md`

## Scientific non-change assertion

At the time of this historical exception, the change did not modify the then-current thesis numerical model, viability algorithms, proposition registry, model schema, example model, Julia dynamics, tests, data, empirical evidence, or frozen research architecture.

The historical scientific chain recorded at that time was

$$
\mathcal D_{obs}
\rightarrow
(\widehat{\mathcal G},\widehat\theta,\Sigma_\theta)
\rightarrow
\mathcal F_{dyn}
\rightarrow
K_R
\rightarrow
\mathcal V_R
\rightarrow
\mathcal C_R
\rightarrow
\mathcal U_{recovery}.
$$

> **Historical notation only:** The equation above is retained to document the 2026-08-22 state of the project. It must not be substituted for the current seven-stage P–T–I–O architecture.

## Direct file audit

The committed V4 SVG was inspected against the presentation contract. It had:

- native SVG/XML structure;
- stable `viewBox="0 0 1800 1050"`;
- accessible title and description;
- `@media(prefers-color-scheme:dark)` semantic theme switching;
- no raster image dependency;
- no color inversion filter;
- explicit P–W–T–SW dynamics under the historical architecture;
- observation, identification, dynamic model, admissibility, viability, recovery and control kept distinct;
- `K_R`, `V_R`, `C_R`, dynamic-interface and uncertainty objects retained;
- P1–P7 falsification gate retained;
- theme-independent topology, labels and geometry.

The historical presentation standard preserved the distinction

```text
source differential geometry
!= geometric visual metaphor
!= formally defined thesis geometry
```

and the theme-invariance condition

$$
\mathcal I(F_{\mathrm{light}})=\mathcal I(F_{\mathrm{dark}}).
$$

## Existing QA inspection

The repository's then-existing QA definitions remained unchanged and fail-closed. Their declared checks included:

- Python compilation and viability-geometry tests;
- proposition registry validation;
- JSON Schema + example-model validation;
- XML parsing of mathematical SVGs;
- Julia coupled-model smoke test;
- Python matrix lint/test workflow.

The underlying files used by those gates were inspected and were not changed by the visual PR.

## GitHub Actions execution-layer blocker

For the V4 head, all three independently defined workflows reported failure:

- Python package;
- Scientific Architecture QA;
- temporary Adaptive Thesis Visual Audit.

For the temporary adaptive audit, the Actions job completed as `failure` while exposing an empty step list. Attempts to retrieve logs returned `BlobNotFound`. The same zero-step behavior was observed on the existing gates and also existed on the earlier V3 visual PR.

Classification:

```text
ZERO-STEP ACTIONS FAILURE
!=
DEMONSTRATED SCIENTIFIC TEST FAILURE
```

The temporary workflow was removed before merge so it did not add a permanently failing gate.

## One-time merge exception

A one-time, file-scoped CI-infrastructure exception was authorized for that historical adaptive presentation PR because:

1. the change was limited to native SVG + presentation governance;
2. the then-current scientific architecture and executable research files were unchanged;
3. the changed SVG was directly audited against its invariants;
4. the observed CI failure occurred before exposed executable steps;
5. no failed scientific assertion, unit test, schema check, or Julia check was demonstrated for that change.

This exception expired when the V4 visual PR was merged or closed. It does not authorize bypassing CI for future model, data, code, calibration, empirical, or thesis-claim changes.
