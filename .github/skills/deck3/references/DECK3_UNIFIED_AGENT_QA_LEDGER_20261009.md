# Deck3 unified agent — QA and release evidence (2026-10-09)

## Changes actually committed
- Unified intent router and routing contract linked into current Deck3 skills/workflow/dependency registry.
- Editable PPTX build, inspect, revision and structural QA CLI.
- Native object inventory includes shape positions, texts, note contents, master/layout counts and OMML element presence.
- QA checks 13-slide count, saved slide geometry, authored slide sRGB colors and gradients. Other visual/scientific gates remain separate.
- Integration tests and CI workflow added; simulated source text is **not** the approved Chapter 1 manuscript.

## Verified vs not verified
| Gate | State | Evidence |
|---|---|---|
| GitHub source files committed | PASS | PR #69 changed files |
| GitHub intent router first scenario sweep | PARTIAL | 10/11 passed; 'update colors' bug located and patched afterward |
| Installed python-pptx note write/read API in local Python | PASS | isolated library behavior check (not full Deck3 CLI) |
| CI on latest head | FAIL | Five GitHub Actions workflows reported failure; full logs unavailable to connector |
| Actual integrated Python tests | NOT_RUN | No successful CI job or accessible complete logs |
| Approved source extraction/complete current 13-slide deck build | NOT_RUN | Approved source PPTX/text not supplied to this execution environment |
| Mathematical native Office Math conversion | NOT_IMPLEMENTED | XML presence inspector only, no conversion proof |
| Rendered slide comparison | NOT_RUN | No complete real-deck render inspected |
| Desktop PowerPoint editing and playback | NOT_RUN | Microsoft PowerPoint not exercised |
| Equipment physics, service relationships and sources | OPEN | requires case-specific evidence |
| Final release certification | BLOCKED | unresolved CI and scientific/rendered/OMML gates |

## Scope limitations of implemented utilities
- The 13-slide builder is a text-first native PPTX baseline **not** a scientifically complete Deck3 stage-3 presentation. It does not reproduce existing approved template masters or create native OMML, validated equipment diagrams, intelligent layout or animation.
- The edit operation substitutes text **only when the exact old string occurs within an editable run**; it never changes underlying equations or raster graphics. Run-level replacement intentionally fails closed otherwise.
- The QA operation does not certify scientific physics, visual readability, theme/master palette, notes fidelity, animation playback or current file contents against the frozen thesis copy.
- Code-based checks cannot be counted as user-deck QA until run on the actual input source.

## Required remediation before merging
1. Diagnose five failing GitHub Actions jobs from actual runner logs / GitHub web interface; reproduce and repair errors, then obtain green test results.
2. Run CLI inspect/build/revise/qa tests with Python 3.11 and Node 20, including notes and geometry assertions.
3. Locate the user-approved exact 13-slide Chapter 1 source and test faithful reproduction without overwriting it.
4. Integrate real template geometry and native OMML source-to-PPTX conversion, then compare saved XML and rendered equations.
5. Verify figure-evidence sidecars and 13-color palette across slide, theme/master and authored assets.
6. Inspect resulting 13-slide contact sheet and actual PowerPoint editability/playback where claimed.
7. Keep the PR open until all mandatory release gates pass; do not merge by assuming CI failures are unrelated.
