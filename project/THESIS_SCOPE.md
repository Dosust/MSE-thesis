# MSE Thesis Scope

## Working title

**Mathematical Physics of Sustainable Infrastructure Resilience**

Current precise formulation:

*Equity-Constrained Viability of Coupled Power–Water–Transportation–Solid-Waste Systems with Dynamic Interfaces under Climate Stress*

## Physical system

- Power (P)
- Water / drainage (W)
- Transportation (T)
- Solid Waste (SW)

Primary demonstrator: **urban flooding with waste–drainage–transport feedbacks**.

## Central scientific object

The principal object is the sustainable/equitable viability boundary

$$
\boxed{\partial\mathcal V_R}.
$$

The thesis asks how dynamic interfaces, uncertainty, climate stress, sustainability/equity constraints, and admissible interventions deform this boundary and the associated recovery geometry.

## Governing architecture

$$
\boxed{
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
\mathcal U_{recovery}
}
$$

The core scientific question is:

> How accurately must dynamic cross-infrastructure interfaces be identified and represented before sustainable/equitable viability and recovery predictions can be trusted?

Three derived questions structure the mathematical program:

1. **What moves the viability boundary?**
2. **How uncertain is that boundary?**
3. **What interventions or designs move it in a favorable direction?**

## Mathematical foundation

The formal definitions, assumptions, viability/recovery geometry, inverse problem, timescale ratio, control layer, and downstream design formulation are maintained in:

- [`MATHEMATICAL_FOUNDATION.md`](MATHEMATICAL_FOUNDATION.md)
- [`SCIENTIFIC_PROPOSITIONS.md`](SCIENTIFIC_PROPOSITIONS.md)

## Evidence strategy

The thesis uses two linked but non-interchangeable tracks:

1. **PRISMA / evidence falsification and precedent search** — establishes what has been studied, by which methods, under which evidence limits.
2. **Mathematical development and falsification** — identification/inverse problems, dynamic coupling, timescale regimes, viability/reachability, recovery/capture geometry, sustainability/equity constraints, uncertainty, control, and reduced-model validation.

Evidence has authority over the starting architecture: a direct precedent is a successful falsification result, not a failure.

## Scope discipline

The MSE thesis does not require an original contribution at every downstream layer simultaneously. The core mathematical contribution is centered on **dynamic coupling → admissibility → viability → recovery**, with identification/UQ as upstream support and control/design as structured extensions.
