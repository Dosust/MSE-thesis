"""Structural, color, animation-contract and Bezier tests; not PowerPoint playback."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "examples"))
from geometry_and_manifest_qa import validate, load_palette, contrast_on_white, bezier, bezier_head_angle

class AdvancedDeck3Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sample = json.loads((ROOT / "examples" / "advanced_manifest_example.json").read_text(encoding="utf-8"))
    def edited(self):
        return copy.deepcopy(self.sample)
    def test_valid_source_grounded_fixture(self):
        self.assertEqual(validate(self.sample), [])
    def test_no_duplicate_object_identifiers(self):
        d = self.edited()
        d["objects"][1]["id"] = d["objects"][0]["id"]
        self.assertIn("duplicate object IDs", validate(d))
    def test_unknown_arrow_endpoint_rejected(self):
        d = self.edited()
        d["relations"][0]["to"] = "ghost"
        self.assertTrue(any("invalid arrow endpoint" in x for x in validate(d)))
    def test_candidate_is_not_falsely_established(self):
        d = self.edited()
        d["relations"][0]["evidence_status"] = "ESTABLISHED"
        self.assertTrue(any("promoted" in x for x in validate(d)))
    def test_whiteness(self):
        d = self.edited()
        d["panel_fill_hex"] = "#F8F8F8"
        self.assertIn("non-white diagram/slide interior", validate(d))
    def test_unapproved_authored_token(self):
        d = self.edited()
        d["authored_color_tokens"].append("random_pink")
        self.assertTrue(any("unapproved authored color" in x for x in validate(d)))
    def test_exact_canonical_token_hex(self):
        d = self.edited()
        d["objects"][0]["color_hex"] = "#0072B3"
        self.assertTrue(any("canonical exact sRGB" in x for x in validate(d)))
    def test_gold_critical_text_forbidden(self):
        d = self.edited()
        d["objects"][0].update(color_token="asu_gold", color_role="essential_text")
        self.assertTrue(any("low-contrast critical" in x for x in validate(d)))
    def test_gold_nonessential_accent_allowed(self):
        d = self.edited()
        d["objects"][0].update(color_token="asu_gold", color_role="nonessential_accent")
        self.assertEqual(validate(d), [])
    def test_no_colored_box_interior(self):
        d = self.edited()
        d["objects"][0]["fill_hex"] = "#EEEEEE"
        self.assertTrue(any("non-white authored object fill" in x for x in validate(d)))
    def test_no_gradients(self):
        d = self.edited()
        d["gradient"] = True
        self.assertTrue(any("gradient/shadow/texture" in x for x in validate(d)))
    def test_unapproved_arrow_color(self):
        d = self.edited()
        d["relations"][0]["stroke_color_token"] = "random_gold"
        self.assertTrue(any("unapproved arrow color" in x for x in validate(d)))
    def test_gold_essential_arrow_forbidden(self):
        d = self.edited()
        d["relations"][0]["stroke_color_token"] = "asu_gold"
        self.assertTrue(any("low-contrast essential arrow" in x for x in validate(d)))
    def test_arrow_stroke_hex_exactness(self):
        d = self.edited()
        d["relations"][0].update(stroke_color_token="teal", stroke_hex="#006D71")
        self.assertTrue(any("arrow color differs from canonical exact sRGB" in x for x in validate(d)))
    def test_click_order(self):
        d = self.edited()
        d["animation"]["click_groups"][1]["click"] = 1
        self.assertTrue(any("sequence" in x for x in validate(d)))
    def test_auto_advance_forbidden(self):
        d = self.edited()
        d["animation"]["automatic_advance"] = True
        self.assertTrue(any("animation contract" in x for x in validate(d)))
    def test_canonical_registry(self):
        p = load_palette()
        self.assertEqual(len(p["colors"]), 13)
        self.assertEqual(p["colors"]["asu_maroon"]["hex"], "#8C1D40")
        self.assertEqual(p["colors"]["asu_gold"]["hex"], "#FFC627")
        self.assertEqual(p["authored_surfaces"]["canvas"], "#FFFFFF")
    def test_black_and_white_contrast(self):
        self.assertAlmostEqual(contrast_on_white("#000000"), 21.0)
        self.assertAlmostEqual(contrast_on_white("#FFFFFF"), 1.0)
    def test_bezier_endpoints(self):
        pts = ((0, 0), (1, 1), (2, 1), (3, 0))
        self.assertEqual(bezier(*pts, 0), (0, 0))
        self.assertEqual(bezier(*pts, 1), (3, 0))
    def test_bezier_tangent(self):
        self.assertAlmostEqual(bezier_head_angle((2, 1), (3, 0)), -45)
    def test_bezier_degenerate_tangent(self):
        with self.assertRaises(ValueError):
            bezier_head_angle((3, 0), (3, 0))
    def test_bezier_invalid_param(self):
        with self.assertRaises(ValueError):
            bezier((0, 0), (0, 0), (1, 1), (2, 2), 1.2)

if __name__ == "__main__":
    unittest.main()
