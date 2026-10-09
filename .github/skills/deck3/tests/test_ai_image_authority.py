"""Static propagation checks for Deck3 AI image generation governance."""
import unittest
from pathlib import Path

SKILLS = Path(__file__).resolve().parents[2]
ROOT = SKILLS.parent
STANDARD = SKILLS / "deck3/references/DECK3_AI_IMAGE_GENERATION_STANDARD.md"
DEPENDENTS = [
    SKILLS / "deck3/SKILL.md",
    SKILLS / "deck3/references/DECK3_GLOBAL_UPDATE_CONTRACT.md",
    SKILLS / "scientific-infographic-design/SKILL.md",
    SKILLS / "scientific-diagram-design/SKILL.md",
    SKILLS / "mathematical-visualization-design/SKILL.md",
    SKILLS / "engineering-framework-design/SKILL.md",
    ROOT / "copilot-instructions.md",
]


class ImageAuthorityTests(unittest.TestCase):
    def test_standard_contains_pre_render_and_post_render_gates(self):
        doc = STANDARD.read_text(encoding="utf-8").lower()
        for term in ("before generation", "physical state", "serviceability", "evidence status",
                     "stage 1", "stage 2", "stage 3", "human design", "scientific (s)",
                     "colors and geometry (c)", "image and integration (i)",
                     "13 exact", "provisional", "photographs"):
            self.assertIn(term, doc, term)

    def test_all_impacted_instructions_link_new_authority(self):
        for path in DEPENDENTS:
            with self.subTest(path=str(path)):
                doc = path.read_text(encoding="utf-8")
                self.assertIn("DECK3_AI_IMAGE_GENERATION_STANDARD.md", doc)
                self.assertIn("Deck3-governed AI scientific image generation", doc)

    def test_deck3_version_increment(self):
        doc = (SKILLS / "deck3/SKILL.md").read_text(encoding="utf-8")
        self.assertIn('version: "1.7.0"', doc)


if __name__ == "__main__":
    unittest.main()
