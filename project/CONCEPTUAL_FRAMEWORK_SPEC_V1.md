# Conceptual Framework Specification V1

**Status:** WORKING-FROZEN VISUAL/SCIENTIFIC SPECIFICATION  
**Date:** 2026-10-06

## Purpose

This file defines the scientific content and visual architecture of the thesis conceptual framework.

It is **not** the research-method figure.

## Core conceptual chain

```text
Extreme heat forcing
→ physical states
→ qualified P–T interdependency
→ functionality
→ electricity and mobility service
→ Improve → Adapt → Restore
→ service/resilience outcomes
```

Compact mathematical representation:

```math
\eta(x,t)
\rightarrow
[x_P(t),x_T(t)]
\xrightarrow{\mathcal I_{PT}}
[F_P(t),F_T(t)]
\rightarrow
[Q_P(t),Q_T(t)]
\rightarrow
\{a_I,a_A,a_R\}
\rightarrow
\mathcal M_R
```

where:
- `η(x,t)` = extreme-heat forcing;
- `x_P,x_T` = selected physical states;
- `I_PT` = qualified directional P–T electrification mechanism;
- `F_P,F_T` = functionality;
- `Q_P,Q_T` = electricity and mobility service;
- `a_I,a_A,a_R` = Improve, Adapt, Restore actions;
- `M_R` = declared service/resilience metrics.

## Required distinctions

```text
common heat exposure ≠ interdependency propagation
co-location ≠ dependency
P → T ≠ T → P
interdependency ≠ V2G
state ≠ service
reliability ≠ resilience
action ≠ outcome
```

## Support domains

Information (I) and Organization (O) are supporting/enabling domains, not the physical core.

They may provide:
- sensing/state estimation;
- communication/data sharing;
- planning;
- resource allocation;
- operational coordination.

They should be drawn below the physical/service pathway with dashed or secondary links.

## Resilience action interpretation

```text
IMPROVE
(pre-event / between events)
→ measurable enhancement relative to baseline

ADAPT
(during evolving disturbance)
→ state-aware operational change

RESTORE
(after service degradation / as disturbance relaxes)
→ return to acceptable service
```

## Visual design rules

1. White canvas.
2. White card/panel backgrounds.
3. Never use colored quadrant backgrounds unless explicitly requested.
4. Use color only for:
   - borders;
   - icons;
   - headings;
   - arrows;
   - small markers.
5. Use large directional arrows.
6. Minimize prose; prefer symbols, equations, icons, and short labels.
7. Keep Power and Transportation visually dominant.
8. Use support-domain links as dashed/secondary.
9. Do not place the governing research protocol in this figure.
10. Do not show any equation whose variables have not been defined.

## Open placeholders

Do not freeze these graphically until the scientific decisions are resolved:
- road vs rail;
- charging vs traction;
- exact state variables;
- exact P–T interface variable;
- exact service metrics;
- exact intervention set.

