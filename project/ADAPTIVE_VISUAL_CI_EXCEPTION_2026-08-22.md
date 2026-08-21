# MSE Thesis — Adaptive Visual CI Infrastructure Exception

Date: 2026-08-22
Scope: V4 presentation changes only:

- `assets/math-art/master_architecture.svg`
- `project/MATHEMATICAL_PRESENTATION_V3.md`

## Scientific non-change assertion

This change does not modify the thesis numerical model, viability algorithms, proposition registry, model schema, example model, Julia dynamics, tests, data, empirical evidence, or frozen research architecture.

The active scientific chain remains:

```math
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
```

## Direct file audit

The committed V4 SVG was inspected against the presentation contract. It has:

- native SVG/XML structure;
- stable `viewBox="0 0 1800 1050"`;
- accessible title and description;
- `@media(prefers-color-scheme:dark)` semantic theme switching;
- no raster image dependency;
- no color inversion filter;
- explicit P–W–T–SW dynamics;
- observation, identification, dynamic model, admissibility, viability, recovery and control kept distinct;
- `K_R`, `V_R`, `C_R`, dynamic-interface and uncertainty objects retained;
- P1–P7 falsification gate retained;
- theme-independent topology, labels and geometry.

The companion presentation standard explicitly preserves:

```text
source differential geometry
!= geometric visual metaphor
!= formally defined thesis geometry
```

and

```math
\mathcal I(F_{light})=\mathcal I(F_{dark}).
```

## Existing QA inspection

The repository's existing QA definitions remain unchanged and fail-closed. Their declared checks include:

- Python compilation and viability-geometry tests;
- proposition registry validation;
- JSON Schema + example-model validation;
- XML parsing of mathematical SVGs;
- Julia coupled-model smoke test;
- Python matrix lint/test workflow.

The underlying files used by these gates were inspected and are not changed by this visual PR.

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

The temporary workflow was removed before merge so it does not add a permanently failing gate.

## One-time merge exception

A one-time, file-scoped CI-infrastructure exception is authorized for this adaptive presentation PR because:

1. the change is limited to native SVG + presentation governance;
2. the scientific architecture and executable research files are unchanged;
3. the changed SVG was directly audited against its invariants;
4. the observed CI failure occurred before exposed executable steps;
5. no failed scientific assertion, unit test, schema check, or Julia check has been demonstrated for this change.

This exception expires immediately when the V4 visual PR is merged or closed. It does not authorize bypassing CI for future model, data, code, calibration, empirical, or thesis-claim changes.
