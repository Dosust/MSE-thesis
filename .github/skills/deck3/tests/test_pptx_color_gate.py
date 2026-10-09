"""Regression tests: authored PPTX slide sRGB compliance is mandatory before assembly."""
import sys
import tempfile
import unittest
from pathlib import Path
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.util import Inches

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE / "examples"))
from pptx_color_qa import check
from deck3 import Blocked, assemble

def fixture(path, *, text=(0,0,0), background=(255,255,255)):
    prs = Presentation()
    s=prs.slides.add_slide(prs.slide_layouts[6])
    s.background.fill.solid()
    s.background.fill.fore_color.rgb=RGBColor(*background)
    box=s.shapes.add_textbox(Inches(1),Inches(1),Inches(5),Inches(1))
    para=box.text_frame.paragraphs[0]
    para.text="Provisional scientific text"
    para.font.color.rgb=RGBColor(*text)
    prs.save(path)

class NativePptxColorTests(unittest.TestCase):
    def test_approved_body_text_and_white_background_pass(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"ok.pptx"
            fixture(p)
            self.assertEqual(check(p)["status"],"EXPLICIT_SLIDE_COLOR_SOURCE_PASS_NOT_RENDER_CERTIFIED")
    def test_legacy_body_text_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"bad.pptx"
            fixture(p,text=(22,30,41))
            self.assertIn("off-palette",str(check(p)["errors"]))
    def test_nonwhite_background_rejected_even_when_palette_color(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"bad.pptx"
            fixture(p,background=(18,48,74))
            self.assertIn("nonwhite",str(check(p)["errors"]))
    def test_absent_explicit_white_background_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"bad.pptx"
            prs=Presentation()
            s=prs.slides.add_slide(prs.slide_layouts[6])
            s.shapes.add_textbox(Inches(1),Inches(1),Inches(2),Inches(1)).text="Hello"
            prs.save(p)
            self.assertIn("background absent",str(check(p)["errors"]))
    def test_approved_semantic_power_blue_pass(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"ok.pptx"
            fixture(p,text=(0,114,178))
            self.assertEqual(check(p)["errors"],[])

if __name__=="__main__":
    unittest.main()
