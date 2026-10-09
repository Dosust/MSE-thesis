"""Policy regression tests for Dossiya's authentic-color thesis visuals.

These are static contract checks, NOT image-level inspection or PPTX certification.
"""
import unittest
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
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


    def test_asu_exact_exceptions_and_turquoise(self):
        data = json.loads((ROOT / "deck3" / "references" / "DECK3_SRGB_PALETTE.json").read_text(encoding="utf-8"))
        self.assertEqual(data["policy_version"], "1.6.0")
        self.assertEqual(data["colors"]["asu_maroon"]["hex"], "#8C1D40")
        self.assertEqual(data["colors"]["asu_gold"]["hex"], "#FFC627")
        self.assertEqual(data["colors"]["bright_turquoise"]["hex"], "#6ACEEE")
        self.assertLess(data["colors"]["asu_gold"]["contrast_on_white"], 3)
        self.assertLess(data["colors"]["bright_turquoise"]["contrast_on_white"], 3)
        self.assertEqual(set(data["authored_surfaces"].values()), {"#FFFFFF"})

    def test_exact_srgb_registry(self):
        palette_path = ROOT / "deck3" / "references" / "DECK3_SRGB_PALETTE.json"
        data = json.loads(palette_path.read_text(encoding="utf-8"))
        self.assertEqual(data["color_space"], "sRGB")
        self.assertEqual(data["channel_bits"], 8)
        self.assertEqual(set(data["authored_surfaces"].values()), {"#FFFFFF"})
        self.assertEqual(len(data["colors"]), 13)
        def luminance(values):
            def linear(v):
                c = v / 255
                return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
            return sum(c * linear(v) for c, v in zip((0.2126, 0.7152, 0.0722), values))
        for name, record in data["colors"].items():
            with self.subTest(color=name):
                self.assertEqual("#" + "".join(f"{x:02X}" for x in record["rgb"]), record["hex"])
                if name != "white":
                    contrast = 1.05 / (luminance(record["rgb"]) + .05)
                    if name not in ("asu_gold", "bright_turquoise"):
                        self.assertGreaterEqual(contrast, 4.5)
                    self.assertAlmostEqual(contrast, record["contrast_on_white"], delta=.01)
                    self.assertFalse(record["allowed_as_surface"])


if __name__ == "__main__":
    unittest.main()
