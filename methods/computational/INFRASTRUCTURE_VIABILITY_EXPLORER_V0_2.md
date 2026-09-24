# Infrastructure Viability Explorer v0.2 — graph-aware computational specification

## Status

**Synthetic research-software demonstrator. Not a declared thesis result.**

v0.2 extends the v0.1 reduced-dynamics demonstrator with an explicit multilayer Power–Transportation graph and a spatial hazard-to-graph projection. It preserves the rule that visualization consumes computational output rather than inventing scientific state.

## Structural object

The synthetic multilayer graph is

~~~math
\mathcal G_{PT}
=
(\mathcal V_P,\mathcal V_T,\mathcal E_P,\mathcal E_T,\mathcal E_{PT}).
~~~

The current deterministic benchmark contains 4 power nodes, 5 transportation nodes, 10 intra-layer edges, and 2 cross-sector interface edges.

Every node has a normalized coordinate $(x_i,y_i)\in[0,1]^2$, a role label, a layer label, and a non-negative vulnerability coefficient.

## Reduced dynamics

The dynamic state remains

~~~math
Y(t)=[P(t),T(t),C_{PT}(t)]\in[0,1]^3.
~~~

The governing reduced ODE and RK4 solver are unchanged from v0.1. The graph has therefore **not yet been promoted to the governing physical dynamics**.

This distinction is intentional:

~~~math
\text{graph structure}
\neq
\text{network-flow physics}
\neq
\text{causal dynamics}.
~~~

## Spatial hazard projection

The temporal flood pulse is mapped to space through a smooth Gaussian field centered in the normalized domain:

~~~math
\eta_i(t)
=
\eta(t)
\exp\left[
-\frac{(x_i-x_c)^2+(y_i-y_c)^2}{2\sigma^2}
\right].
~~~

This is a synthetic benchmark field, not a calibrated flood-depth surface.

## Node availability projection

For node $i$ in sector $s\in\{P,T\}$,

~~~math
A_i(t)=S_s(t)\exp[-\nu_i\eta_i(t)],
~~~

where $S_s(t)$ is the reduced sector-service state and $\nu_i\ge 0$ is the declared node vulnerability coefficient.

This quantity is a visualization/diagnostic projection, not component reliability inferred from field data.

## Edge activity projection

For intra-layer edge $e=(i,j)$,

~~~math
a_e(t)=\min(A_i(t),A_j(t)).
~~~

For interface edge $e\in\mathcal E_{PT}$,

~~~math
a_e(t)=C_{PT}(t)\min(A_i(t),A_j(t)).
~~~

Again, $a_e$ is not electrical power flow, traffic flow, capacity utilization, or a causal failure probability.

## Browser contract

Python exports:

- graph topology;
- per-node local hazard;
- per-node projected availability;
- per-edge projected activity;
- reduced state trajectory;
- sustainability margin proxy;
- ML hold-out diagnostics;
- parameter-sensitivity diagnostics;
- experiment fingerprint.

JavaScript performs only geometric rendering and user interaction.

## Reliability gates

1. Graph IDs are unique.
2. Node coordinates remain inside the normalized domain.
3. Intra-layer edges remain inside their declared layer.
4. Interface edges connect different layers.
5. Local hazards remain in $[0,1]$.
6. Node availability remains in $[0,1]$.
7. Edge activity remains in $[0,1]$.
8. RK4 solutions remain deterministic and bounded.
9. RK4 refinement error decreases monotonically in the declared regression.
10. Exported data remain reproducible against regenerated Python output.

## Next scientific promotion gate

A future version may promote $\mathcal G_{PT}$ from structural scaffolding into the governing dynamics only after each layer has a defensible physical model and an explicit graph-to-dynamics mapping. Candidate routes include DC power-flow or distribution-service approximations for the power layer and network-flow or dynamic traffic-assignment abstractions for the transportation layer.

Only after admissible control, reachability, and controlled invariance are explicit should the software compute or label a true viability kernel $\mathcal V_{\mathrm{sus}}$ or resilience margin

~~~math
\rho_g
=
d_g\!\left(Y,\partial\mathcal V_{\mathrm{sus}}\right).
~~~
