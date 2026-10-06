# Mathematical Visualization Implementation Architecture V1

**Status:** IMPLEMENTATION GUIDE  
**Date:** 2026-10-06  
**Scientific authority:** \`MATHEMATICAL_FRAMEWORK_SPEC_V1.md\`  
**Visualization authority:** \`.github/skills/mathematical-visualization-design/SKILL.md\`

## Goal

Build future thesis visualizations so that mathematical variables and transformations generate the visual state.

## Core architecture

\`\`\`text
MODEL
→ SOLVER / STATE UPDATE
→ DERIVED QUANTITIES
→ VISUAL ENCODING
→ RENDERER
→ INTERACTION
→ QA
\`\`\`

## Model layer

Owns:
- heat forcing;
- subsystem states;
- interface relations;
- constraints;
- interventions;
- service functions;
- sustainability indicators.

It contains no arbitrary drawing coordinates.

## Derived-quantity layer

Computes:
- critical transition times;
- propagation delays;
- service trajectories;
- service deficits;
- recovery time;
- sustainability indicators;
- scenario differences.

## Visual-encoding layer

Maps only declared quantities to visual channels.

Examples:

\[
\tau_i^C\mapsto\text{event marker on time axis},
\]

\[
\delta_{ij}\mapsto\text{temporal separation of events},
\]

\[
Q_k(t)\mapsto\text{service-trajectory height},
\]

\[
g_i(X_i,t)\mapsto\text{feasible/boundary/violation state}.
\]

No visual property may vary without a scientific mapping.

## Renderer choices

### Static thesis figures
Prefer SVG or TikZ.

### Interactive 2D state-time views
Prefer Canvas/p5.js or D3.js.

### High-dimensional state fields
Use WebGL only if required by scale or mathematical dimensionality.

Do not use advanced rendering merely to appear high-tech.

## Interaction contract

A control must map to a model parameter.

Example:

\`\`\`text
heat-duration slider
→ update heat forcing
→ recompute state trajectory
→ recompute transition time/service
→ redraw
\`\`\`

Never animate first and infer the mathematics afterward.

## Validation

Every interactive visualization must pass:
- mathematical correctness check;
- deterministic replay check;
- parameter-to-model mapping check;
- visual semantic check;
- boundary/threshold check;
- grayscale/label readability check.

## Reference principle

The public J.C. Ponce complex-analysis project is used as a reference for the principle of visual-interactive mathematics, not as a visual template.

See:
\`.github/skills/mathematical-visualization-design/resources/JCPONCE_COMPLEX_ANALYSIS_REFERENCE.md\`.
