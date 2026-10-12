#!/usr/bin/env python3
"""Fail-closed static governance checks. This is NOT physical validation."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
gov = (ROOT / "project/governance/THERMAL_AGENTIC_RESEARCH_GOVERNANCE_V1.md").read_text()
reg = (ROOT / "project/governance/THERMAL_RESEARCH_EXECUTION_REGISTER_V1.md").read_text()
baseline = (ROOT / "project/thermal_sos_functional_architecture/SELECTED_EIGHT_COMPONENTS_WORKING_RESEARCH_BASELINE_V1.md").read_text()
scope = (ROOT / "project/PHYSICS_MATHEMATICS_FIRST_HYPOTHESIS_TESTING_SCOPE_DIRECTIVE_V1.md").read_text()
objectives = (ROOT / "project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md").read_text()
ids = ["P1", "P2", "P3", "P4", "T1", "T2", "T3", "T4"]
for token in ids:
    assert re.search(rf"\b{token}\b", gov), f"missing governance component {token}"
    assert re.search(rf"\b{token}\b", baseline), f"missing baseline component {token}"
for token in ("I1","I2","I3","I4","I5","I6"):
    assert re.search(rf"\b{token}\b", gov), f"missing interface {token}"
for n in range(1, 17):
    assert f"R{n:02d}" in gov, f"missing rule R{n:02d}"
for n in range(9):
    assert f"G{n}" in gov, f"missing gate G{n}"
for so in ("SO1","SO2","SO3"):
    assert so in objectives and so in scope and so in reg
assert "AI and digital-twin development are excluded" in scope
assert "BLOCKED_EVIDENCE" in reg
assert "independent physical validation" in gov.lower()
assert "older Austin/flood/seven-objective" in reg
print("PASS: structural governance assertions only; NOT scientific validation.")
