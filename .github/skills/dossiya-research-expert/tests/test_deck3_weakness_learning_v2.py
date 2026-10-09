"""Governance/traceability regression tests; NOT proof of physical scientific validity.
Run: python -m unittest .github/skills/dossiya-research-expert/tests/test_deck3_weakness_learning_v2.py
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
V2 = ROOT / "references" / "DECK3_WEAKNESS_TO_VERIFIED_LEARNING_V2.md"

class TestDeck3WeaknessLearning(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.skill = SKILL.read_text(encoding="utf-8")
        cls.protocol = V2.read_text(encoding="utf-8")

    def test_active_expert_references_corrected_v2(self):
        self.assertIn("version: \"1.4.2\"", self.skill)
        self.assertIn("references/DECK3_WEAKNESS_TO_VERIFIED_LEARNING_V2.md", self.skill)

    def test_correct_version_mapping(self):
        text = self.protocol
        for part in ["A13", "B13", "C13",
                     "Pasted text(20261009-151339).txt",
                     "Pasted text (2)(20261009-151345).txt",
                     "Pasted text (3)(4).txt"]:
            self.assertIn(part, text)
        self.assertIn("AC/DC balance belongs to **B13, not A13**", text)
        self.assertIn("M0/M1/M2 belongs to **A13, not B13**", text)

    def test_scope_immutable_but_science_critically_reviewed(self):
        text = self.protocol
        for phrase in ["extreme heat as external forcing",
                       "thermal **interdependencies only**",
                       "physical state and time",
                       "two-way sustainability assessment",
                       "A frozen statement is NOT physically validated"]:
            self.assertIn(phrase,text)

    def test_complete_corrective_rules_and_challenges(self):
        for i in range(1,14):
            self.assertRegex(self.protocol,rf"Rule L{i:02}\b")
        for i in range(1,17):
            self.assertRegex(self.protocol,rf"\| AT{i:02} \|")

    def test_required_negative_and_counterfactual_scenarios(self):
        for item in ["NOT_OBSERVED_IN_HORIZON", "only P→T_e", "only T_e→P",
                     "Neither directional law", "M2 improves simulated service",
                     "Common forcing", "no admitted carrier/port",
                     "no finite delay"]:
            self.assertIn(item, self.protocol)

    def test_coupled_physics_and_validation_not_certified(self):
        for item in ["grid-side AC", "P_losses,incl_aux", "dE_internal/dt",
                     "Matched difference ≠ field validation",
                     "NOT_YET_MEASURABLE", "NOT_TESTED"]:
            self.assertIn(item, self.protocol)

    def test_expert_lesson_not_claimed_as_model_retraining(self):
        self.assertIn("not model retraining", self.protocol.lower())
        self.assertIn("No experimental physics", self.protocol)

if __name__ == "__main__":
    unittest.main()
