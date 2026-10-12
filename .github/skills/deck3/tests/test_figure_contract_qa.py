"""Adversarial tests for Deck3 figure-to-research linkage."""
import copy
import json
import sys
import unittest
from pathlib import Path

DECK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(DECK / "examples"))
from figure_contract_qa import validate

ROOT = DECK.parents[2]


class FigureContractQATests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = json.loads((DECK / "examples/figure_contract_slide02_example.json").read_text(encoding="utf-8"))

    def test_reference_fixture_passes_structural_only(self):
        result = validate(self.fixture, ROOT)
        self.assertEqual(result["status"], "STRUCTURAL_CONTRACT_PASS_NOT_SCIENCE_VERIFIED", result)
        self.assertFalse(result["science_validated"])
        self.assertFalse(result["citation_content_verified"])
        self.assertFalse(result["powerpoint_playback_verified"])

    def test_rejects_false_cross_system_causality(self):
        altered = copy.deepcopy(self.fixture)
        altered["science"]["cross_system_causality"] = "ESTABLISHED"
        self.assertEqual(validate(altered, ROOT)["status"], "BLOCKED")

    def test_rejects_unassessed_sustainability_claim(self):
        altered = copy.deepcopy(self.fixture)
        altered["science"]["sustainability_effect"] = "PROVEN_BENEFIT"
        self.assertEqual(validate(altered, ROOT)["status"], "BLOCKED")

    def test_rejects_changed_slide_claim(self):
        altered = copy.deepcopy(self.fixture)
        altered["claim"] = "The external forcing proves reciprocal coupling."
        self.assertEqual(validate(altered, ROOT)["status"], "BLOCKED")

    def test_rejects_unverified_animation(self):
        altered = copy.deepcopy(self.fixture)
        altered["animation"]["click_count"] = 3
        self.assertEqual(validate(altered, ROOT)["status"], "BLOCKED")

    def test_rejects_wrong_figure_or_missing_authority(self):
        for key, value in (("figure_file", "wrong.png"),):
            altered = copy.deepcopy(self.fixture)
            altered[key] = value
            self.assertEqual(validate(altered, ROOT)["status"], "BLOCKED")
        altered = copy.deepcopy(self.fixture)
        altered["source"]["path"] = "nonexistent.md"
        self.assertEqual(validate(altered, ROOT)["status"], "BLOCKED")

    def test_rejects_wrong_design_contract(self):
        for field, value in (("canvas", "#EEEEEE"), ("font", "Arial"), ("aspect_ratio", "4:3")):
            altered = copy.deepcopy(self.fixture)
            altered["visual"][field] = value
            self.assertEqual(validate(altered, ROOT)["status"], "BLOCKED")

    def test_rejects_false_validation_status(self):
        altered = copy.deepcopy(self.fixture)
        altered["verification"]["physical"] = "PASS"
        self.assertEqual(validate(altered, ROOT)["status"], "BLOCKED")


if __name__ == "__main__":
    unittest.main()
