#!/usr/bin/env python3
"""Structural, invocation, and thesis-guardrail checks for the Dossiya writing skill."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
skill = root / "SKILL.md"
agent = root / "AGENTS.md"
assert agent.is_file(), "AGENTS.md missing"
assert skill.is_file(), "SKILL.md missing"
s = skill.read_text(encoding="utf-8")
assert s.startswith("---\n"), "Missing YAML frontmatter"
front = s.split("---\n", 2)[1]
assert re.search(r"^name:\s*dossiya-writing\s*$", front, re.M), "Incorrect skill name"
assert re.search(r"^description:\s*\S", front, re.M), "Missing description"
assert len(s.splitlines()) < 500, "Skill too long"
assert '"Dossiya, edit this"' in s, "Invocation alias missing"
assert 'plain mention' in s, "Incidental name safeguard missing"
for name in ["VOICE_PROFILE.md", "EXAMPLES.md", "THESIS_GUARDRAILS.md", "EVALUATION_RUBRIC.md"]:
    assert (root / "references" / name).is_file(), f"Missing {name}"
voice = (root / "references" / "VOICE_PROFILE.md").read_text(encoding="utf-8")
assert "Data needs a backbone very solid" in voice, "Authentic sample missing"
g = (root / "references" / "THESIS_GUARDRAILS.md").read_text(encoding="utf-8")
fixed = [
    "To characterize and model thermal interdependencies between the Power System and the Electrified Transportation System under extreme heat, and to quantify how their consequences evolve through physical state and time.",
    "Identify and qualify the thermally sensitive physical states and directional thermal interdependency mechanisms connecting the Power System and the Electrified Transportation System.",
    "Develop a physics-based state-time model of the qualified thermal interdependencies and their propagation under extreme heat.",
    "Quantify critical transition times, interdependency propagation delays, and the resulting electricity and mobility service consequences.",
]
for line in fixed:
    assert line in g, f"Canonical text altered: {line[:45]}"
print("PASS: AGENTS and SKILL present, metadata valid")
print("PASS: Dossiya explicit invocation and incidental-name safety present")
print("PASS: Four voice references and original sample present")
print("PASS: All four frozen objective strings present exactly")
