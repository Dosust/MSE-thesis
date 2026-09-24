# Infrastructure Viability Explorer — graph-aware synthetic demonstrator v0.2

This directory contains a deterministic browser visualization driven entirely by data generated from the thesis repository's Python computational layer.

## Run

From the repository root:

1. Run <code>python tools/run_viability_explorer.py</code>.
2. Run <code>python -m http.server 8000</code>.
3. Open <code>http://localhost:8000/visualization/infrastructure_viability_explorer/</code>.

## v0.2 architecture

The demonstrator contains an explicit synthetic multilayer graph:

- **4 power nodes**
- **5 transportation nodes**
- **12 total edges**
- **2 cross-sector interface edges**

The computational chain is:

~~~math
\mathcal G_{PT}
\rightarrow \eta(x,t)
\rightarrow Y(t)
\rightarrow \text{graph projection}
\rightarrow K_{\mathrm{sus}}
\rightarrow \rho_K
\rightarrow \text{diagnostics}
\rightarrow \text{animation}.
~~~

The reduced dynamic state is

~~~math
Y(t)=[P(t),T(t),C_{PT}(t)].
~~~

## Scientific boundary

The graph is structural scaffolding. v0.2 does **not** solve AC/DC power flow, traffic assignment, cascading-outage physics, or a calibrated restoration model.

For each node, local flood exposure is projected from the synthetic spatial hazard field. Node availability is a declared visualization projection combining reduced sector service and local exposure. Edge activity is a diagnostic proxy based on endpoint availability, additionally scaled by $C_{PT}$ for interface edges.

Therefore:

- graph projection ≠ physical network-flow solution;
- threshold set ≠ viability kernel;
- parameter sensitivity ≠ causal identification;
- synthetic ML hold-out accuracy ≠ empirical predictive validity.

## Reliability

- deterministic fixed-step RK4;
- normalized-domain checks;
- RK4 refinement regression;
- multilayer topology validation;
- cross-layer interface validation;
- spatial hazard bounds;
- graph-state bounds;
- deterministic JSON export;
- SHA-256 record fingerprint;
- Python 3.10/3.11/3.12 CI definition;
- JavaScript syntax check;
- no-gold palette contract;
- committed-vs-regenerated numerical comparison;
- Markdown math-render guard for explorer documentation.

## Rendering rule

The browser consumes <code>demo-data.json</code>. It does not recompute the ODE, spatial hazard, node availability, edge activity, sustainability margin, ML error, or sensitivity values.

## Palette

No gold-family colors are used.

- Light Sky Blue: <code>rgb(135, 206, 250)</code> / <code>#87CEFA</code>
- Deep Sky Blue: <code>rgb(0, 191, 255)</code> / <code>#00BFFF</code>
