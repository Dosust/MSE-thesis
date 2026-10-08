# Implementation Contract — Optional VisQuill GDK

## 0. Prerequisite
A selected visual problem must pass `TOOL_FIT_DECISION.md`. All scientific semantics and frozen research rules have priority over interaction. If the user asked for a static figure, do not create a browser application.

## 1. Write the view contract before software
Record:
- Main question: what physical/scientific fact does interaction reveal?
- Audience and output: browser demo vs static SVG/PPTX/PDF fallback.
- Canonical system scope, particular bounded displayed subset, external heat input.
- Evidence-qualified P→Te/Te→P directions; candidate/unqualified statuses in text.
- Required data field(s), units, time coordinates, valid conditions, and provenance for EVERY plotted variable.
- Visual mapping: what determines position, length, line, color, opacity, time animation, and interaction.
- No arbitrary threshold, temperature, failure or temporal lag for visual effect.

## 2. Solver/graphics separation
Keep model computation in a separately verified scientific workflow (for example Python). Export a documented data schema for the interactive browser. Illustrative schema below (NOT the final approved physics model):

```json
{
  "dataset_status": "synthetic-demo-only",
  "scenario_id": "demo-reference",
  "time_unit": "s",
  "temperature_unit": "K",
  "time_s": [0, 60, 120],
  "states": {"illustrative_temperature_K": [300, 301, 303]},
  "service": {},
  "provenance": ["NOT A THESIS EXPERIMENT"],
  "qualified_directed_mechanisms": []
}
```

The graphic must not promote `illustrative_temperature_K` to a real transformer or EVSE temperature or convert it into a real capacity or mobility service. For real projects require consistent data-array lengths, monotone time, finite values, units, source tags, missing-value handling and data quality checks. Keep measurement and model prediction separately identified.

## 3. Scaffold and build
Official entry:
```bash
npm create visquill@latest
```
Or, in an already approved TypeScript browser package:
```bash
npm install @visquill/visquill-gdk
```

Then:
- Record `node`, npm, VisQuill package and scaffold versions in the deliverable.
- Read the generated `package.json` to determine dev/build/test commands; do not assume any one package runner.
- Use vendor API reference for the exact installed release.
- Keep graphics in separate folder such as `visualization/visquill-prototype`, **only after user asks to build**.
- Avoid extra frameworks, paid map tiles, sensitive repositories, API keys and external data exposure.
- Pin dependency versions and commit a lockfile only when an actual working project exists.
- Use a CSS class prefix; write visuals as labels and constrained reactive geometry.
- Clean up the RvgGraphic on unmount using `graphic.dispose()` or the documented equivalent.

## 4. Use only proven API until current version is checked
Official examples on vendor site show:
- `import { VisQuill, Reactive, Circles, Attach } from "@visquill/visquill-gdk"`
- `VisQuill.create(div, "graphic-prefix-")`
- `graphic.canvas.handles.disk("name", {x, y})`
- `graphic.canvas.visuals.circle("name")`
- `Reactive.do([handle], () => { Circles.circleAt(handle, radius, circle) })`
- `graphic.canvas.text.label("", "name")` with `Attach.pointToPoint(...)`.
- `RvgGraphic.dispose()` is documented in vendor API.

Do not claim an API exists just because it sounds plausible. The small `examples/reactive_geometry_demo.ts` uses only vendor-documented names but is **not runtime-tested in this skill creation**.

## 5. Suggested first thesis prototype — only after scientific evidence
If the supervisor approves the case and physically qualified direction(s) and the solver output exists, a single view may show:
- a full-system label with a *bounded visible case* clearly indicated;
- physical states and valid constraints, with temperature or load values linked to the data;
- at most the justified directional arrows; label `CANDIDATE` or `OPEN` visibly;
- model time scrubber linked to fixed scenario arrays (no speculative interpolation);
- a distinct derived capability view and separate `Q_P(t)` / `Q_T(t)` metrics **only if defined**;
- external heat as a forcing input outside the two systems;
- a comparison view only if scenarios have matched assumptions.

A generic draggable handle is merely a graphics demonstration; it must not be presented as the user’s real coupled thermal mechanism.

## 6. Test pyramid
**Static:** YAML name/description; links to scientific skills; attribution and non-invention terms; package and API names.
**TypeScript:** install sanctioned dependency in isolated web project, compile/typecheck.
**Browser smoke:** ensure SVG renders, handle follows correct coordinates, text visible, no console errors, responsiveness, keyboard/accessibility or usable alternative.
**Scientific:** checks against authoritative register, dimensional units, correct status, citations, no false causal arrow, no data fabrication, no hidden changes to model.
**Publication:** standalone PNG/SVG (render/inspect), thesis PDF figures work without JavaScript, source and attribution visible as required by license.

## 7. Status report
Every implementation report must say separately:
- "skill configured" vs "VisQuill package installed";
- "TypeScript typechecked" vs "browser rendered";
- "graphics demo worked" vs "physical model scientifically validated";
- "static export delivered" vs "interactive public deployment";
- "research data measured / computed / synthetic".

An agent must never claim these stronger results merely because the skill exists.
