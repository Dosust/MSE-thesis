# Mathematical Art Assets

These SVG figures are not decorative illustrations. They are version-controlled scientific diagrams encoding thesis mathematics. The active V4 masters are native adaptive SVGs: light/dark presentation may change, but mathematical/evidence meaning may not.

## Files

### `master_architecture.svg`
Encodes the complete thesis chain:

`observation → identification → dynamic coupling → admissibility → viability → recovery → control → design`

It also displays the P–W–T–SW coupled system and the central research object $\partial\mathcal V_R$.

### `dynamic_interface_operator.svg`
Encodes:

- the four-sector block operator $\mathcal A(t)$;
- dynamic interface states $Z_{ij}(t)$;
- the multiscale interface law $\varepsilon\dot Z=G(\cdot)$;
- the timescale ratio $\rho_{ij}$;
- climate forcing $\xi\to\eta$;
- waste–drainage–flood feedback.

### `viability_recovery_geometry.svg`
Encodes the distinction among:

- admissible region $K_R$;
- viability kernel $\mathcal V_R$;
- recovery/capture set $\mathcal C_R$;
- viability and recovery boundaries;
- admissible recovery trajectories;
- viable, recoverable-nonviable, and nonrecoverable states.

## V4 adaptive rendering invariant

All active mathematical SVGs use a light-default semantic palette with a `prefers-color-scheme: dark` override. Theme changes are constrained by

```math
\boxed{\mathcal I(F_{light})=\mathcal I(F_{dark})}
```

where $\mathcal I$ includes equations, topology, boundaries, trajectory meaning, labels, evidence state and quantitative values.

Raster inversion is prohibited for scientific figures because it can reverse color semantics. Publication-white export is a render profile of the same mathematical object, not a separately redrawn figure.

## Design rule

Mathematical art in this repository must satisfy:

1. every visual symbol has a declared mathematical meaning;
2. arrows represent specified model relationships or hypotheses, not unexplained decoration;
3. geometry corresponds to defined thesis objects and must not upgrade a geometric metaphor into established differential geometry;
4. figures remain inspectable as text-based SVG;
5. each SVG has an accessible `<title>` and `<desc>`;
6. theme changes presentation only;
7. scientific CI/XML validation remains fail-closed when GitHub Actions execution is available.
