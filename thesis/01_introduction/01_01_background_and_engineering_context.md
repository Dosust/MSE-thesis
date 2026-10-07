## 1.1 Background and Engineering Context

Electricity and mobility are distinct critical infrastructure services, but transportation electrification creates direct physical coupling between the Power System and the Electrified Transportation System. Grid-connected charging links electrical capability to vehicle energy availability and mobility, while charging demand or supported reverse transfer can affect Power-system operating conditions.

The active thesis is not a study of all Power–Transportation interdependencies. It is restricted to **thermal interdependencies**: directional dependencies whose activation, magnitude, capacity, timing, or consequence is changed by heat- or temperature-dependent physical states, thermal capability, or thermally conditioned operating limits.

Extreme heat is treated as external forcing. It may affect both systems, but common heat exposure alone does not establish interdependency. The scientific problem begins only when a thermally driven change in one system or in the power-transfer pathway changes the state, capability, or service of the coupled system.

The physical core is:

```text
Power System P
↔
Electrified Transportation System T_e
```

The Electrified Transportation System boundary is controlled by the thesis standards-based scope definition. EVSE belongs to `T_e`; coupling/interface variables represent exchanged quantities, constraints, or dependency conditions and do not constitute a third physical infrastructure system.

The thesis therefore follows one bounded engineering chain:

```text
Extreme heat
→ thermal physical state
→ thermal capability / constraint
→ qualified thermal interdependency
→ state-time evolution
→ electricity and mobility service consequence
```

State and time are the primary analytical dimensions.
