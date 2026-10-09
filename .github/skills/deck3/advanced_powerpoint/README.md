> Installed in `.github/skills/deck3/advanced_powerpoint/` as an evidence-gated capability reference. The canonical source of design colors is `../references/DECK3_SRGB_PALETTE.json` in the parent Deck3 folder. Automated tests do **not** verify real PowerPoint playback or thesis physics.\n\n# Proposed Deck3 Advanced PowerPoint Skill Package

**Date:** 2026-10-09  
**Status:** Complete *proposed skill documents* and runnable sample structural tests. **NOT** installed in GitHub, **NOT** proof of implemented PowerPoint animation APIs, **NOT** new thesis scientific authority.

## Intended use

Provide rigorous instructions to future Deck3 agents and human developers on selection and engineering of native PowerPoint science figures, custom curved connectors, mathematical notation, scalable SVG assets, genuine On Click animations, Morph, accessibility, programmatic generation and scientific release QA.

**Current repository remains authoritative:** `https://github.com/Dossiya-SE/MSE-thesis`, specifically `.github/skills/deck3/SKILL.md` (observed current Oct 9 status), `references/DECK3_SRGB_PALETTE.json`, all mandatory thesis and diagram design authorities.

## Package map

| Path in ZIP | Purpose | Proposed target |
|---|---|---|
| `SKILL.md` | Full detailed advanced skill | `.github/skills/deck3/references/ADVANCED_POWERPOINT_SKILLS_V1.md` |
| `references/ROUTES_AND_MICROSKILLS.md` | 25 methods, tool selection, best uses | `.github/skills/deck3/references/ROUTES_AND_MICROSKILLS.md` |
| `references/CHAPTER1_ANIMATION_MAP.md` | 6 required/4 optional slide animation specs | `.github/skills/deck3/references/CHAPTER1_ANIMATION_MAP.md` |
| `references/OFFICIAL_SOURCE_REGISTRY.md` | Microsoft/Office/Aspose/PptxGenJS primary links and limitations | `.github/skills/deck3/references/OFFICIAL_SOURCE_REGISTRY.md` |
| `references/ACCEPTANCE_AND_TESTS.md` | 13 release gates, negative fixtures | `.github/skills/deck3/references/ACCEPTANCE_AND_TESTS.md` |
| `references/INSTALL_AND_ROLLOUT.md` | Non-destructive installation instructions and exact snippet | `.github/skills/deck3/references/INSTALL_AND_ROLLOUT.md` |
| `examples/advanced_manifest_example.json` | Candidate Slide 5 scientific object/arrow/animation example | `.github/skills/deck3/examples/advanced_manifest_example.json` |
| `examples/chapter1_v2_animation_baseline.json` | Previous 2026-10-09 original v2 38-group specification | `.github/skills/deck3/examples/chapter1_v2_animation_baseline.json` |
| `examples/geometry_and_manifest_qa.py` | Structural/Bézier validation, semantic flags | `.github/skills/deck3/examples/geometry_and_manifest_qa.py` |
| `tests/test_advanced_contract.py` | 12 unit regression tests | `.github/skills/deck3/tests/test_advanced_contract.py` |
| `TEST_RESULTS.json` | Actual executed test outcome | Keep with proposed package before integration |

## Verified sample tests

Executed (on this proposed package) with Python standard library:

```bash
python -m unittest discover -s tests -v
python examples/geometry_and_manifest_qa.py examples/advanced_manifest_example.json
```

Expected result: 12 tests pass, example structural checker PASS with 8 objects, 6 candidate relations and 4 click groups. These tests do not prove native PowerPoint slideshow animations, editable OOXML conversion, 75% effective diagram occupancy, or any model's physical validity.

## Engineering status

- **SPECIFIED:** 25 advanced authoring routes, 6 prioritized chapter animation slides, 26 click effects, semantics, geometry and mathematical QA requirements, source registry and exact palette use.
- **TESTED IN THIS PACKAGE:** sample schema/geometry checker with positive and negative fixtures.
- **NOT IMPLEMENTED HERE:** a complete native slide generation engine, a production effect backend for Aspose/OOXML/Morph, a real PowerPoint UI test, a cross-platform exact color inspector for arbitrary PPTX binary contents, or independent physics validation.

## Next integration sequence

Read `references/INSTALL_AND_ROLLOUT.md`. Do not replace the current Deck3 SKILL.md wholesale. Add it as a reference module, preserve the existing authoritative palette and baseline decks, then implement Slide 5 as the reference prototype in a separate feature branch with a native desktop PowerPoint playback check.