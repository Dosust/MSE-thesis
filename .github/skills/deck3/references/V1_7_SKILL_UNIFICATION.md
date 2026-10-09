# Deck3 v1.7 — backward-compatible visual-skill unification

**Release character:** additive authoring/routing upgrade; **not** a rewrite of v1.6, not a new frozen science authority, not a new PowerPoint animation engine and not a 75%-geometry implementation. Source of truth for authored color remains the **unaltered** `DECK3_SRGB_PALETTE.json` v1.6.0 with exactly 13 sRGB tokens.

## Why v1.7 exists

Deck3 previously referenced multiple powerful independent figure skills, but the trigger/precedence relationships were spread across large skill files. A new optional [router](../../scientific-visual-orchestration/SKILL.md) now states who owns semantic truth and who may implement or simplify a figure. The [routing contract](../../scientific-visual-orchestration/references/ROUTING_CONTRACT.json) is machine-checkable and intentionally acyclic. [Acceptance gates](../../scientific-visual-orchestration/references/ACCEPTANCE_MATRIX.md) prevent code, diagrams or decorative mathematical art from manufacturing physical evidence.

## Additive behavior

1. Deck3 is still the primary *presentation orchestrator*, retaining original commands and three-stage workflow with native editable text, blank figure slots, independently authored assets, and lossless assembly.
2. Framework, diagram, infographic, mathematical-visualization, advanced-PowerPoint and VisQuill specialists continue to own their individual competencies, equations, boundaries, citation needs and tests. The router selects them; it does not copy them into Deck3 or automatically call every helper.
3. One new specialized [procedural mathematical-art skill](../../procedural-mathematical-art/SKILL.md) teaches pixel coordinates, hashing, cell geometry, distribution transformation and display-time animation. It is optional and synthetic; it never defines infrastructure coupling, real heat fields or novel scientific findings.
4. Chapter-10 concepts are attributed and independently restated; copyrighted shader code is not copied into thesis source. The separate mathematical-art repository remains independently governed.
5. Conflicting legacy "no gold" *blanket* wording has been reconciled with existing v1.6 policy: only exact ASU Gold `#FFC627` is allowed as a small nonessential institutional accent. Any ordinary gold/yellow fill, critical gold line, text or false-contrast mark remains blocked.
6. The palette and the original `examples/deck3.py` binary/functional content remain **bit-identical** to v1.6. The regression suite verifies their Git blob hashes.

## Explicitly unresolved: runtime figure-dominance implementation

The v1.6 policy targets **75% actual meaningful scientific visual area** (70–80% accepted), with exceptions for approved textual/objectives/references slides. The current legacy CLI small-slot figure placement is not certified against that design contract. Neither a text change nor this skill-routing upgrade can remove that gap. A separate engineering PR must update `deck3.py`, compare Stage 1 frozen text/note digests against baseline, assess actual visible figure bounds U/V, render slides, test PPTX import and produce verifiable QA JSON. The baseline remains `TECHNICAL_ONLY / PROVISIONAL` wherever that acceptance gate is not actually passed.

## Source control and nonregression verification

- [Skill unification regression suite](../../scientific-visual-orchestration/tests/test_skill_unification.py) asserts exact **Git blob** snapshots for palette and legacy generator; 13 exact RGB/HEX pairs; authorized surface fills and low-contrast exceptions; paths and acyclic routing; original commands/75% rule/canonical science guardrails; absence of stale blanket gold phrasing.
- [Procedural math checks](../../procedural-mathematical-art/tests/test_procedural_reference.py) test deterministic reference examples and analytic identities.
- Existing Deck3 test suite `test_deck3.py`, color policy `test_color_policy.py`, infographic tests and repository-wide authored color audit stay in effect.
- A clean GitHub Actions run is necessary before declaring the CI-backed release; if hosted jobs fail before execution, report it as **UNVERIFIED**, not as a pass.
- Separately verify actual native PPTX, rendered figure readability, click-playback and human access. A "skill specification present" state is not a "figure rendered and validated" state.

### Local commands

```sh
python -m unittest discover -s .github/skills/scientific-visual-orchestration/tests -p 'test_*.py' -v
python -m unittest discover -s .github/skills/procedural-mathematical-art/tests -p 'test_*.py' -v
python -m unittest discover -s .github/skills/deck3/tests -p test_color_policy.py -v
python .github/skills/deck3/tests/audit_repo_colors.py
```

These checks test source integrity and mathematical/unit properties; they do **not** open slides in Microsoft PowerPoint or calibrate a physical model.
