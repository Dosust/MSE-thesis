# Mathematical Art Assets

These SVG figures are not decorative illustrations. They are version-controlled scientific diagrams encoding the thesis mathematics.

## Files

### `master_architecture.svg`
Encodes the complete thesis chain:

`observation → identification → dynamic coupling → admissibility → viability → recovery → control → design`

It also displays the P–W–T–SW coupled system, the central geometric object $\partial\mathcal V_R$, and the three governing questions.

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

## Design rule

Mathematical art in this repository must satisfy four conditions:

1. every visual symbol has a declared mathematical meaning;
2. arrows represent specified model relationships or hypotheses, not unexplained decoration;
3. geometry corresponds to definitions in `project/MATHEMATICAL_FOUNDATION.md`;
4. figures remain inspectable as text-based SVG and are automatically XML-validated by GitHub Actions.
