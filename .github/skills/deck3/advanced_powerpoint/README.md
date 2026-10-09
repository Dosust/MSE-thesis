# Advanced Deck3 — PowerPoint Engineering and Animation

**Status:** INSTALLED AS A SCIENTIFIC DESIGN / QA EXTENSION (2026-10-09).
**Parent authority:** [Deck3 SKILL.md](../SKILL.md), v1.6.1.
**Color authority:** [DECK3_SRGB_PALETTE.json](../references/DECK3_SRGB_PALETTE.json), immutable current v1.6 registry.

This extension provides a full source- and evidence-conscious skill specification for editable vector diagrams, nonlinear arrow geometry, PowerPoint animation pathways, mathematics, charts, sources and release gates. **It is not a separately validated PowerPoint automation engine**, and cannot supersede the parent Deck3 scientific authority.

## Installed structure

| File | Purpose |
|---|---|
| `SKILL.md` | Full advanced engineering skill and 12-route decision matrix |
| `references/ROUTES_AND_MICROSKILLS.md` | 25 methods and their scope/limitations |
| `references/CHAPTER1_ANIMATION_MAP.md` | Six priority and four optional Chapter 1 reveal specifications |
| `references/OFFICIAL_SOURCE_REGISTRY.md` | Vendor capability evidence (not physics validation) |
| `references/ACCEPTANCE_AND_TESTS.md` | Acceptance gates and negative tests |
| `references/INSTALL_AND_ROLLOUT.md` | Recorded installation and uncompleted runtime roadmap |
| `examples/advanced_manifest_example.json` | Eight objects, six candidate arrows, four OnClick groups |
| `examples/chapter1_v2_animation_baseline.json` | Archived, specification-only Chapter 1 v2 animation plan |
| `examples/geometry_and_manifest_qa.py` | Structural, exact sRGB, arrow geometry and click-order checks |
| `tests/test_advanced_contract.py` | 22 positive/negative local regression cases |

## Color contract

**Do not copy or hardcode a second 13-color palette.** At runtime the checker loads the canonical parent `references/DECK3_SRGB_PALETTE.json` and fails if it is missing. Exact 8-bit sRGB identifiers only. White canvas, boxes, interiors, headings and legends. ASU Maroon `#8C1D40` may be a heading; ASU Gold `#FFC627` is only a nonessential accent, not critical text or a thin evidence-bearing arrow. Bright Turquoise `#6ACEEE` has the same nonessential limitation. Check contrast of critical text and graphics, plus distinct shapes/markers.

Real photograph colors remain authentic; code that scans all image pixels and rejects nonpalette colors would be invalid.

## Run checks

From `.github/skills/deck3/advanced_powerpoint`:

```bash
python -m unittest discover -s tests -v
python examples/geometry_and_manifest_qa.py examples/advanced_manifest_example.json
```

The installed parent GitHub Actions workflow `.github/workflows/deck3-tests.yml` now includes these commands. These tests cover example schema, evidence-status discipline, SVG-equivalent Bézier mathematics, exact approved colors, nonwhite fills, essential-arrow contrast, and click specifications.

## Release limits

- **INSTALLED / SPECIFIED:** The skill and documented routes.
- **LOCAL STRUCTURAL QA:** 22 tests passed on the staged code and 8-object example.
- **CI:** Workflow updated; independent GitHub Actions completion was not confirmed in the installer session.
- **NOT VERIFIED:** Real native PowerPoint effect creation/playback, actual PPTX shape inspection, file-level color audit of arbitrary decks, actual 70–80% meaningful-figure coverage, real equipment parameters, physical models or validation.

Use the parent skill's frozen scientific evidence and citation rules. A shape animation never establishes a thermal causal mechanism. Existing user-approved thesis decks remain unchanged.
