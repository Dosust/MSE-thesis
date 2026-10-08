#!/usr/bin/env python3
"""Static validation; does NOT install or execute VisQuill."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
skill = root / "SKILL.md"
text = skill.read_text(encoding="utf-8")
assert text.startswith("---\n"), "Skill YAML frontmatter absent"
frontmatter = text.split("---\n", 2)[1]
assert re.search(r"^name:\s*visquill-interactive-visualization\s*$", frontmatter, re.M)
assert re.search(r"^description:\s*\S+", frontmatter, re.M)
assert len(text.splitlines()) < 500
for rel in [
    "references/TOOL_FIT_DECISION.md",
    "references/IMPLEMENTATION.md",
    "references/LICENSE_AND_SOURCES.md",
    "examples/reactive_geometry_demo.ts",
    "examples/reactive_geometry_demo.css",
    "README.md",
]:
    assert (root / rel).exists(), f"Missing {rel}"
assert "scientific-diagram-design" in text
assert "CANONICAL_EVIDENCE" in text
assert "not" in text.lower()
assert "Made with VisQuill" in text
assert "graphic.dispose()" in text
assert "State ≠ capability ≠ service" in text
demo = (root / "examples/reactive_geometry_demo.ts").read_text(encoding="utf-8")
for api in ("VisQuill.create", "Reactive.do", "Circles.circleAt", "Attach.pointToPoint"):
    assert api in demo, f"Demo missing documented API {api}"
assert "not compiled/browser-tested" in demo
print("PASS: Skill frontmatter and companion references")
print("PASS: Scientific non-invention, attribution and tool-routing checks")
print("PASS: Vendor-documented API demonstration present")
print("NOTE: TypeScript compiler and browser runtime are NOT executed by this test")
