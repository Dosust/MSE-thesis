"""Deck3 cross-skill and SVG source-color regression tests, not end-to-end PPTX certification."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[4]
SKILLS = ROOT / ".github" / "skills"
D3 = SKILLS / "deck3"
sys.path.insert(0, str(D3 / "examples"))
from asset_color_qa import audit_svg, check_figure_source, canonical_colors
from deck3 import Blocked, figure_records

class Deck3CrossSkillPaletteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.reg = json.loads((D3 / "references/DECK3_DEPENDENCY_REGISTRY.json").read_text())
        cls.palette = json.loads((D3 / "references/DECK3_SRGB_PALETTE.json").read_text())
    def test_registry_covers_ten_families_and_existing_files(self):
        self.assertEqual(len(self.reg["routes"]), 10)
        for route in self.reg["routes"]:
            for path in route["paths"]:
                self.assertTrue((ROOT/path).is_file(),path)
    def test_all_linked_skills_read_detailed_global_contract(self):
        paths = [p for r in self.reg["routes"] for p in r["paths"] if p.endswith("/SKILL.md")]
        for p in paths:
            self.assertIn("DECK3_GLOBAL_UPDATE_CONTRACT_V1.md",(ROOT/p).read_text(),p)
    def test_primary_global_contract_links_technical_annex(self):
        p = D3 / "references/DECK3_GLOBAL_UPDATE_CONTRACT.md"
        self.assertIn("DECK3_GLOBAL_UPDATE_CONTRACT_V1.md",p.read_text())
    def test_canonical_palette_exact(self):
        self.assertEqual(len(self.palette["colors"]),13)
        self.assertEqual(len(canonical_colors()),13)
        self.assertEqual(self.palette["colors"]["asu_maroon"]["hex"],"#8C1D40")
        self.assertEqual(self.palette["colors"]["asu_gold"]["hex"],"#FFC627")
        self.assertEqual(set(self.palette["authored_surfaces"].values()),{"#FFFFFF"})
    def test_svg_and_pptx_generators_use_current_palette(self):
        for p in ["scientific-infographic-design/examples/figures.py",
                  "scientific-infographic-design/examples/pptx_builder.py"]:
            s=(SKILLS/p).read_text()
            self.assertIn("DECK3_SRGB_PALETTE.json",s)
            self.assertIn("read_text",s)
            self.assertNotIn("#183D63",s)
    def test_exact_svg_colors_pass(self):
        with tempfile.TemporaryDirectory() as td:
            f=Path(td)/"ok.svg"
            f.write_text('<svg xmlns="http://www.w3.org/2000/svg"><rect fill="#FFFFFF" stroke="#0072B2"/></svg>')
            self.assertEqual(audit_svg(f)["status"],"SVG_SOURCE_PALETTE_PASS_NOT_RENDER_CERTIFIED")
    def test_invalid_svg_stroke_blocks(self):
        with tempfile.TemporaryDirectory() as td:
            f=Path(td)/"bad.svg"
            f.write_text('<svg xmlns="http://www.w3.org/2000/svg"><rect fill="#FFFFFF" stroke="#183D63"/></svg>')
            self.assertEqual(audit_svg(f)["status"],"BLOCKED")
    def test_svg_gradient_blocks(self):
        with tempfile.TemporaryDirectory() as td:
            f=Path(td)/"bad.svg"
            f.write_text('<svg xmlns="http://www.w3.org/2000/svg"><linearGradient id="g"/></svg>')
            self.assertEqual(audit_svg(f)["status"],"BLOCKED")
    def test_svg_inline_css_must_obey_colors(self):
        with tempfile.TemporaryDirectory() as td:
            f=Path(td)/"bad.svg"
            f.write_text('<svg xmlns="http://www.w3.org/2000/svg"><path style="stroke:#2670AC;fill:#FFFFFF"/></svg>')
            self.assertEqual(audit_svg(f)["status"],"BLOCKED")
    def test_png_only_not_color_certified(self):
        with tempfile.TemporaryDirectory() as td:
            f=Path(td)/"drawing.png"
            Image.new("RGB",(800,600),"white").save(f)
            self.assertEqual(check_figure_source(f)["status"],"COLOR_NOT_VERIFIED_RASTER_ONLY")
    def test_photo_is_qualified_exception_not_automatic_pass(self):
        with tempfile.TemporaryDirectory() as td:
            f=Path(td)/"photo.png"
            Image.new("RGB",(800,600),"white").save(f)
            self.assertIn("MANUAL_REVIEW",check_figure_source(f,"authentic_photograph")["status"])
    def test_assembly_stage_rejects_bad_svg_companion(self):
        with tempfile.TemporaryDirectory() as td:
            f=Path(td)
            Image.new("RGB",(800,600),"white").save(f/"figure.png")
            (f/"figure.svg").write_text('<svg xmlns="http://www.w3.org/2000/svg"><path stroke="#183D63"/></svg>')
            data={"slides":[{"kind":"content","title":"Synthetic","message":"Hypothetical",
                "bullets":["a","b","c"],"source_note":"Not domain evidence",
                "figure":{"file":"figure.png","alt":"Synthetic shape"}}]}
            with self.assertRaises(Blocked):
                figure_records(data,f)
if __name__ == "__main__":
    unittest.main()
