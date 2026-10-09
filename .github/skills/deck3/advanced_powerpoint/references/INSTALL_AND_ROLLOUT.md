# Integration Plan — Add Advanced PowerPoint Skills to Existing Deck3

**Installed integration status (2026-10-09):** The advanced reference extension is installed under `.github/skills/deck3/advanced_powerpoint/` and linked from the main `.github/skills/deck3/SKILL.md` (v1.6.1). The stages below describe the original planned rollout; their path/branch instructions are superseded by this installation. Native animation production features remain subject to the listed runtime and PowerPoint playback gates.

## Actual installed commands and color authority

- Canonical colors: `.github/skills/deck3/references/DECK3_SRGB_PALETTE.json` — DO NOT duplicate, alter, approximate or supplement this file.
- Advanced manifest test: `cd .github/skills/deck3/advanced_powerpoint && python -m unittest discover -s tests -v`.
- Example structural/color check: `python examples/geometry_and_manifest_qa.py examples/advanced_manifest_example.json` (from the same working directory).
- Repository CI: `.github/workflows/deck3-tests.yml` now runs both core Deck3 and the advanced extension tests on changes.
- The validator checks exact sRGB tokens, white authored interiors, essential-arrow contrast, object IDs, relation semantics, and click ordering. It does not verify native PowerPoint playback, actual PPTX object colors, image pixels, or physical validity.

## Historical deployment plan (for reference only)

1. Keep the existing `.github/skills/deck3/SKILL.md` as canonical. Do **not** replace it wholesale.
2. Copy the proposed skills `SKILL.md` into the repo as `.github/skills/deck3/references/ADVANCED_POWERPOINT_SKILLS_V1.md` (or register a separately named skill, subject to your loader conventions).
3. Copy supporting `references/*.md` and `examples/*.py`, `examples/*.json`, `tests/*.py` into `.github/skills/deck3/...`; prefix filenames if they conflict with existing names.
4. Update existing `.github/skills/deck3/SKILL.md` only by adding this reference under its relevant advanced animation / scientific-diagram section:

```markdown
## Advanced native PowerPoint and animation extension
For `Deck3 animate`, `Deck3 curved-arrows`, `Deck3 native-shapes`,
`Deck3 math`, `Deck3 vector-icons`, `Deck3 playback-QA`, and
`Deck3 advanced all`, load
`references/ADVANCED_POWERPOINT_SKILLS_V1.md` and its relevant
`references/ROUTES_AND_MICROSKILLS.md`,
`references/CHAPTER1_ANIMATION_MAP.md`,
`references/ACCEPTANCE_AND_TESTS.md` and
`references/OFFICIAL_SOURCE_REGISTRY.md`.
The extension cannot supersede current Deck3 palette/figure-occupancy
requirements, frozen thesis science, exact wording, evidence citations,
or existing Stage-1/2/3 approved baselines.
Do not advertise the new effects as implemented until tests demonstrate it.
```

5. Preserve the current **exact `references/DECK3_SRGB_PALETTE.json`** from your repository. Never override it from an older lesson or generic science palette.
6. Commit on a feature branch; inspect diffs and run project tests before opening a PR. Do not auto-merge without evaluating compatibility with the current Stage 1/2/3 code.

## Suggested new commands vs actual implemented features

| Proposed command | What must exist before marking implemented |
|---|---|
| `Deck3 curved-arrows` | Object registry, connection-point/Bezier generator and endpoint/arrowhead tests |
| `Deck3 native-shapes` | Deterministic source geometry and exact shape names |
| `Deck3 math` | Supported math rendering path, round-trip screenshot check, units/source audits |
| `Deck3 animate` | Named object groups, effect writer, importer test, native PowerPoint user playback |
| `Deck3 morph` | Two-slide named object IDs, Morph transition write/test, reviewer playback |
| `Deck3 accessibility` | Reading order/alt text, contrast evaluator, GUI Accessibility Checker evidence |
| `Deck3 advanced all` | Successful end-to-end implementation, not just manifest generation |

## Proposed engineering phases

- **Phase 0:** accept source and design skill text. This package.
- **Phase 1:** implement geometry and editable icon subsystem + unit tests.
- **Phase 2:** implement Slide 5 evidence-gated four-click native animation prototype, keep fallback.
- **Phase 3:** desktop PowerPoint playback and accessibility validation.
- **Phase 4:** port to Slides 3,4,9,10,12; total 26 click groups. Keep 7,8,11,13 optional.
- **Phase 5:** verify full Chapter 1 text/notes fidelity and diagram occupancy; publish reviewed release.
- **Phase 6:** reusable methods for other thesis chapters/defense rather than hard-coding thermal content.

## Core scientific acceptance

The animation skill must not create reciprocal thermal dependence simply because the two systems are connected by electrical power. Do not infer grid thermal changes from charger DC output without grid-side AC measurements/qualified transfer law. Preserve full T_e scope; external heat forcing; thermal state versus capability versus actual transfer versus required electricity/mobility service; VVUQ distinctions; resilience and two bounded sustainability pathways.

## Dependencies

Core: Python 3.x, `python-pptx`, XML/ZIP verification, optionally Pillow for preview checks. Alternative graphics: SVG renderer. Animation: commercial Aspose.Slides optional; Windows desktop PowerPoint or manually authored native animations optional. Don't assume Mac or Linux supports PowerPoint COM; OOXML is cross-platform for generation but still needs target-reader validation. Avoid storing credentials in the skill package. No font files distributed.

## Evidence and output discipline

The only authority for scientific physics is the project's current canonical evidence standard and cited domain sources. Vendor docs establish UI/API features. Tests record executed assertions only. Do not change existing user-approved deck content during a skill-only upgrade.