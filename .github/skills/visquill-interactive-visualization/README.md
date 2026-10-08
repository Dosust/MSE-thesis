# VisQuill Interactive Visualization — optional thesis skill

**Purpose:** Offer an opt-in TypeScript/SVG interactive-geometry workflow for the MSE thesis, only when scientific interaction adds more value than a static visual. This is a companion to the existing `scientific-diagram-design`, `engineering-framework-design` and `mathematical-visualization-design` skills.

**Not installed:** Saving these files to GitHub does not install the npm package or a ChatGPT-wide agent; it does not deploy a viewer, run a simulator, or validate thermal equations.

## When to invoke
- "Use the VisQuill skill to assess whether this state-time propagation view should be interactive."
- "Build a VisQuill proof-of-concept for my approved model output; clearly label synthetic data if used."
- "Use VisQuill to visualize confirmed P→Te coupling, and do not draw Te→P without independent evidence."
- "Do NOT use VisQuill; create a static vector thesis figure." (This intentionally bypasses the skill.)

## Where to start
1. `SKILL.md` — activation, scientific contract, QA, routing.
2. `references/TOOL_FIT_DECISION.md` — avoid unnecessary interactive work.
3. `references/IMPLEMENTATION.md` — model–graphics architecture, installation, schema and testing.
4. `references/LICENSE_AND_SOURCES.md` — official docs and attribution.
5. `examples/reactive_geometry_demo.ts` plus `examples/reactive_geometry_demo.css` — **browser graphics demo only, not compiled/runtime-verified here**.
6. `tests/validate_skill.py` — local static/structural integrity test.

Official site: https://visquill.com/  
Official scaffold: `npm create visquill@latest`  
Official package: `npm install @visquill/visquill-gdk`

**Scientific authority remains in the current repository canonical files**; never let library capabilities invent physics, interface directions, states, data or failure thresholds.

## Implementation progress
- [x] Conditional GitHub skill documented.
- [x] Official API, installation and license researched (2026-10-08).
- [x] Source-only illustrative example added.
- [ ] npm dependency installed in a separate approved project.
- [ ] TypeScript typecheck.
- [ ] Browser runtime smoke test.
- [ ] Actual research data and model connected.
- [ ] Scientific figure validation and deployment.

These are intentionally separate milestones.
