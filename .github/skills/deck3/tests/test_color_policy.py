"""Policy regression tests for Dossiya's authentic-color thesis visuals.

These are static contract checks, NOT image-level inspection or PPTX certification.
"""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DECK3 = ROOT / "deck3" / "SKILL.md"
INFOGRAPHIC = ROOT / "scientific-infographic-design" / "SKILL.md"
DIAGRAM = ROOT / "scientific-diagram-design" / "SKILL.md"


class AuthenticColorPolicyTests(unittest.TestCase):
    def test_all_relevant_skills_are_in_sync(self):
        for path in (DECK3, INFOGRAPHIC, DIAGRAM):
            with self.subTest(skill=path):
                content = path.read_text(encoding="utf-8").lower()
                self.assertIn("#ffffff", content)
                self.assertIn("magenta", content)
                self.assertIn("purple", content)
                self.assertIn("yellow", content)
                self.assertIn("gold", content)
                self.assertIn("authentic", content)
                self.assertIn("gradient", content)
                self.assertIn("shadow", content)

    def test_deck3_records_photography_exception_and_no_purple_design(self):
        text = DECK3.read_text(encoding="utf-8").lower()
        self.assertIn("photographic authenticity exception", text)
        self.assertIn("forbidden as designed colors", text)
        self.assertIn("panel", text)
        self.assertIn("review", text)


if __name__ == "__main__":
    unittest.main()
