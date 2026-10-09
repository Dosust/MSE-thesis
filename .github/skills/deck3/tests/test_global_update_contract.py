"""Ensure every active Deck3-adjacent skill references the global update contract."""
import unittest
from pathlib import Path

SKILLS_ROOT = Path(__file__).resolve().parents[2]
GITHUB_ROOT = SKILLS_ROOT.parent
CONTRACT = SKILLS_ROOT / "deck3" / "references" / "DECK3_GLOBAL_UPDATE_CONTRACT.md"
DEPENDENTS = [
    SKILLS_ROOT / "deck3" / "SKILL.md",
    SKILLS_ROOT / "scientific-infographic-design" / "SKILL.md",
    SKILLS_ROOT / "scientific-diagram-design" / "SKILL.md",
    SKILLS_ROOT / "mathematical-visualization-design" / "SKILL.md",
    SKILLS_ROOT / "engineering-framework-design" / "SKILL.md",
    SKILLS_ROOT / "dossiya-writing" / "SKILL.md",
    GITHUB_ROOT / "copilot-instructions.md",
]


class GlobalUpdateTests(unittest.TestCase):
    def test_contract_exists_and_covers_whole_pipeline(self):
        text = CONTRACT.read_text(encoding="utf-8").lower()
        for required in ("text/writing", "figure and image", "assembly/output", "runtime and qa", "memory scope", "partial implementation"):
            self.assertIn(required, text)

    def test_all_dependent_skills_link_contract(self):
        for path in DEPENDENTS:
            with self.subTest(path=str(path)):
                self.assertTrue(path.is_file())
                contents = path.read_text(encoding="utf-8")
                self.assertIn("DECK3_GLOBAL_UPDATE_CONTRACT.md", contents)
                self.assertIn("update Deck3", contents)

    def test_palette_has_thirteen_tokens(self):
        import json
        palette = json.loads((SKILLS_ROOT / "deck3" / "references" / "DECK3_SRGB_PALETTE.json").read_text(encoding="utf-8"))
        self.assertEqual(len(palette["colors"]), 13)


if __name__ == "__main__":
    unittest.main()
