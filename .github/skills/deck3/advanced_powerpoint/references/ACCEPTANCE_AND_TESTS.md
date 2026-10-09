# Deck3 Advanced — Acceptance Gates and Reproducible Tests

This is a **test standard**, not a claim that the full advanced implementation is available today.

## Release contract

| Gate | Automated evidence | Manual evidence | Failure action |
|---|---|---|---|
| G0 source | Baseline PPTX SHA-256, slide count, text and note digests | Author-approved source | Stop on conflict |
| G1 science | Object/relation register contains classification, direction, source, status | Scientifically inspect directional physical path | Stop on unqualified causality |
| G2 colors | All authored design colors match 13-token exact sRGB registry | Verify authentic photographs not recolored | Reject unknown markup color |
| G3 geometry | Curve endpoint/tangent checks, path coordinates and bbox consistency | Inspect crossings, label clearance, arrow target | Re-route |
| G4 math | LaTeX/OMML source, unit check, reconstructed equation | Inspect semantics, indices, signs and variable definitions | Reject unverified equation |
| G5 stage/figure | SVG source present, shapes native where required, no raster-only scientific asset in native-edit mode | Zoom and edit a node in PowerPoint | Mark editability unknown / revise |
| G6 layout | Store actual usable U and content V extents; target effective visual coverage 0.70–0.80 | Inspect against projected display | Re-layout or approved exception |
| G7 timing | Count groups and target names, OnClick triggers, persistent objects, no phantom exit/auto | Verify every step including back navigation | Block native animation release |
| G8 source fidelity | Slide title / GO / SO1–SO3 exact strings, notes/citations preserved; no authoring labels | Scientific readability review | Rebuild from frozen source |
| G9 file/render | PowerPoint ZIP integrity, reopen via library, render each slide and reveal state | Check figures/citations/no overlap | Reject final release |
| G10 accessibility | Every graphic has alt/description, contrast and reading-order register | PowerPoint Accessibility Checker, screen reader if available | Flag as provisional |
| G11 real software | Independent importer recognized effects | Desktop PowerPoint Slide Show (click/remote) | `POWERPOINT_PLAYBACK_UNTESTED` |
| G12 final | Manifest, source figures, code, QA JSON, preview, fallback deck all included | Supervisor/author approval | `PROVISIONAL` until approved |

### Common failures

- **False high-resolution claim:** large PNG is internally tiny diagram with mostly white padding. Remedy: judge bounding box of actual artwork and screen-size typography, not pixel dimensions alone.
- **False native-animation claim:** OOXML timing nodes present but lost on import or not playing in PowerPoint. Remedy: inspect G7/G11 and use click-through fallback.
- **Source mutation:** native-text slide changes while assembling scientific groups. Remedy: compare exact text/notes digests and fail on any unauthorized change.
- **Misleading two-way arrows:** electrically linked systems shown with dual thermal arrows. Remedy: independently qualify each thermal direction; otherwise mark as candidate or omit arrows.
- **Model validity overclaim:** animation depicts a real event time despite no measured/calibrated parameter. Remedy: clearly label hypothetical or remove.
- **Group breakage:** regrouping after adding animations can remove effects (Microsoft Reading Order documentation explicitly cautions about grouping animated objects). Remedy: group first, apply effects later, re-test.
- **Unapproved branding:** visually close substitutes or yellow/gold used for essential information. Remedy: exact current palette, contrast checks and semantic labels.

## Example QA JSON structure

```json
{
  "baseline_sha256": "REAL_CAPTURED_SHA",
  "slide": 5,
  "design_status": "BUILT",
  "evidence_status": "CASE_MECHANISM_OPEN",
  "tests": {
    "frozen_text_identical": null,
    "native_shapes_editable": null,
    "semantic_arrow_register_complete": true,
    "colors_exact": true,
    "onscreen_visual_share": null,
    "timing_xml_valid": null,
    "imported_effects": null,
    "powerpoint_slideshow_pass": null
  },
  "warnings": ["No case-specific P-to-Te or Te-to-P measured thermal mechanism verified"],
  "release": "PROVISIONAL"
}
```

Use `null` (not `true`) for tests not run. DO NOT aggregate unknown into a PASS. The JSON above is a **schema example**, not actual QA results.

## Minimum negative fixtures

1. Diagram with shared heat and a thermal P↔T_e arrow unmarked as candidate must fail G1.
2. Diagram with EVSE outside T_e must fail G1.
3. T_e→P thermal path without grid-side AC input/evidence register must fail G1.
4. PowerPoint with unauthorized altered frozen GO/SO must fail G8.
5. Native GIF/PNG animation counted as individually editable component reveal must fail G5.
6. Unsupported sRGB token or tinted interior must fail G2.
7. Degenerate Bézier tangent with P3=P2 must fail G3.
8. `timing` effects missing a named target or with `AfterPrevious` instead of required manual click must fail G7 unless co-timed within approved click group.
9. Placeholder/candidate thermal coefficient unmarked OPEN must fail G4.
10. Required 11 of 11 Chapter 1 figure slots only 10 filled must fail G5.

## Three independent meanings of quality

- **Structural QA:** does the file satisfy machine-readable constraints?
- **Visual QA:** is it readable and geometrically clear in the actual presentation environment?
- **Scientific QA:** do arrows, equations, references and state/flow/service claims remain scientifically defensible?

No one gate substitutes for the other two.