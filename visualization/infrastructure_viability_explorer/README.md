# Infrastructure Viability Explorer — synthetic demonstrator v0.1

This directory contains a deterministic browser visualization driven by data generated from the thesis repository's reduced power–transport demonstrator.

## Run

From the repository root:

1. Run: python tools/run_viability_explorer.py
2. Run: python -m http.server 8000
3. Open: http://localhost:8000/visualization/infrastructure_viability_explorer/

## Scientific boundary

The demonstrator is intentionally narrow:

- systems: Power P plus Transportation T;
- hazard: one smooth synthetic flood-intensity pulse;
- state: normalized power service, transport service, and interface health;
- dynamics: interpretable reduced ODE integrated by deterministic fixed-step RK4;
- geometry: signed distance to declared sustainability thresholds under a diagonal metric;
- ML: transparent ridge-regression surrogate trained and validated only against the synthetic simulator;
- criticality: finite-difference model sensitivity of minimum constraint margin.

The threshold set is **not** a computed viability kernel. The criticality diagnostic is **not** causal identification. The ML hold-out error is **not** evidence of real-world predictive skill.

## Rendering rule

The browser consumes demo-data.json; it does not recompute or invent model states. Animation is therefore a view of reproducible computational output, not decorative motion.

## Palette

No gold-family colors are used. Primary accents are Light Sky Blue rgb(135, 206, 250) / #87CEFA and Deep Sky Blue rgb(0, 191, 255) / #00BFFF.
