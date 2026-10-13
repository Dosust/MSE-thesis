# Charging pathway — original animation test storyboard V1

**Variant:** separate ten-slide thesis design/training presentation. **Not:** the canonical eight-slide Deck3 master or a modification of frozen research objectives.

**Message:** Ordinary charging transfers power from distribution transformer through a radial AC feeder to a DC charger, where conversion occurs, and then to the vehicle battery.

**Boundary:** Power = P1 transformer, P2 radial three-phase feeder and other customer branches; Electrified Transportation = T1 DC charger/AC-to-DC conversion and T2 EV battery. Interface at T1's grid-side AC input. P3 protection, P4 cooling, T3 EVSE cooling and T4 vehicle HVAC are excluded from this **minimum demonstration** rather than falsely put in the main electrical path.

| Narrative time (seconds) | Progressive reveal | Scientific meaning |
|---|---|---|
| 0.0–0.8 | P1 transformer and two independent system boundaries | Identify where supply begins; not a heat-stress model |
| 0.85–1.85 | AC arrow then P2 radial feeder with customer branches | Normal distribution pathway |
| 2.0–3.0 | AC link, then T1 AC/DC generic block | Conversion boundary is *inside* charger |
| 3.15–4.15 | DC link, then T2 storage pack | One-way ordinary charging direction |
| 4.15–6.0 | Hold complete architecture and explanatory legend | Consolidate; no physical timing implied |

**Arrow ledger:** E01 P1→P2 A normal AC, evidence = general electrical engineering system behavior (illustrative, no real site topology); E02 P2→T1 A normal AC; E03 T1→T2 A DC charging. No dynamic B/C/D/E arrows, no independent thermal state, no measurement, no reverse export.

**Motion status:** Presenter-time staged reveal, **not** physical electricity propagation or verified AC-port dynamic response. Explicit warning in final video frame: not evidence of I2/I3. No quantitative component data, thermal derating, transformer trips or battery BMS limit is created.

**Artwork:** Original SVG components (not reproductions of manufacturers' diagrams). Generic electrical conversion block is symbolic, not a claim about converter internals. White interior, governed 13 authored RGB colors, Times New Roman labels in source and native editable PowerPoint companion. ASU mark not generated.

**QA reference:** `../references/ANIMATION_QA_CHECKLIST_V1.md`. Local demonstrator rendering can be valid while **actual PowerPoint slideshow playback is NOT_RUN**. The source-specific package and render must be independently checked before calling this sample released.
