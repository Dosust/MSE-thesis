"""Deck3 regression tests: structure, note preservation, gating, aspect ratio.

Synthetic blank PNGs are ONLY file/geometry fixtures, not scientific figures.
Run: python -m unittest discover -s tests -v
"""
import json
import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(DIR / "examples"))

from deck3 import Blocked, assemble, figure_records, load_manifest, make_text, main, notes_register, text_register, slot_for, usable_bounds, geometry_share


class Deck3EndToEndTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.manifest = self.root / "manifest.json"
        self.figure_dir = self.root / "figures"
        self.figure_dir.mkdir()
        self.stage = self.root / "stage1.pptx"
        self.final = self.root / "final.pptx"
        self.qa = self.root / "qa.json"

        self.data = {
            "deck_name": "Synthetic QA example",
            "slides": [
                {"kind": "title", "title": "Test Example", "subtitle": "Not thesis data", "notes": "Title note."},
                {"kind": "content", "title": "Independent forcing",
                 "message": "Two separate pathways are illustrated.",
                 "bullets": ["System A.","System B.","Cross-system effect not asserted."],
                 "source_note": "Internal design example (not domain literature)",
                 "notes": "Test scientific status: schematic only.",
                 "figure": {"file": "figure_02.png", "alt": "Independent schematic diagram."}},
                {"kind": "content", "layout": "long_objectives", "title": "Long objective test",
                 "message": "Long research aim remains verbatim and must never be truncated.",
                 "bullets": ["One full objective.", "Second full objective.", "Third full objective."],
                 "source_note": "Internal canonical figure example.",
                 "notes": "Long objective exactness test.",
                 "figure": {"file": "figure_03.png", "alt": "Objective outputs."}},
                {"kind": "references", "title": "References",
                 "entries": ["Internal example — no external scientific assertion."],
                 "notes": "Source records."}
            ],
            "frozen_strings": ["Long research aim remains verbatim and must never be truncated."]
        }
        self.manifest.write_text(json.dumps(self.data), encoding="utf-8")

    def make_images(self):
        # Contrasting aspect ratios to test CONTAIN instead of deformation.
        Image.new("RGB", (1600, 900), "white").save(self.figure_dir / "figure_02.png")
        Image.new("RGB", (1000, 1000), "white").save(self.figure_dir / "figure_03.png")

    def test_manifest_rejects_missing_exact_three_bullets(self):
        self.data["slides"][1]["bullets"].pop()
        self.manifest.write_text(json.dumps(self.data), encoding="utf-8")
        with self.assertRaises(Blocked):
            load_manifest(self.manifest)

    def test_manifest_rejects_frozen_string_missing(self):
        self.data["frozen_strings"] = ["This was never in the source text."]
        self.manifest.write_text(json.dumps(self.data), encoding="utf-8")
        with self.assertRaises(Blocked):
            load_manifest(self.manifest)

    def test_text_stage_is_editable_and_has_no_images(self):
        make_text(self.manifest, self.stage)
        prs = Presentation(str(self.stage))
        self.assertEqual(len(prs.slides), 4)
        self.assertFalse(any(s.shape_type == MSO_SHAPE_TYPE.PICTURE
                             for slide in prs.slides for s in slide.shapes))
        self.assertIn(self.data["slides"][1]["message"], text_register(prs)[1])
        self.assertIn(self.data["slides"][2]["bullets"][2], text_register(prs)[2])
        self.assertIn("Test scientific status", notes_register(prs)[1])
        # Presenter-facing content must never expose authoring metadata labels.
        visible = [text for slide_text in text_register(prs) for text in slide_text]
        self.assertNotIn("MAIN MESSAGE", visible)
        self.assertNotIn("THREE KEY POINTS", visible)
        self.assertIn("SPECIFIC OBJECTIVES", visible)


    def test_stage_2_blocks_missing_image(self):
        with self.assertRaises(Blocked):
            figure_records(load_manifest(self.manifest), self.figure_dir)

    def test_single_slide_audit_does_not_require_other_slides(self):
        Image.new("RGB", (900, 600), "white").save(self.figure_dir / "figure_02.png")
        r = figure_records(load_manifest(self.manifest), self.figure_dir, slide=2)
        self.assertEqual(len(r), 1)
        self.assertEqual(r[0]["slide"], 2)

    def test_assembly_keeps_text_and_notes_and_aspect_ratio(self):
        self.make_images()
        make_text(self.manifest, self.stage)
        baseline = Presentation(str(self.stage))
        original_text = text_register(baseline)
        original_notes = notes_register(baseline)
        report = assemble(self.manifest, self.stage, self.figure_dir, self.final, self.qa)
        final = Presentation(str(self.final))
        self.assertEqual(text_register(final), original_text)
        self.assertEqual(notes_register(final), original_notes)
        self.assertEqual([sum(s.shape_type == MSO_SHAPE_TYPE.PICTURE for s in slide.shapes)
                          for slide in final.slides], [0, 1, 1, 0])
        self.assertTrue(all(x["preserved_aspect_ratio"] for x in report["figure_records"]))
        self.assertTrue(self.qa.is_file())
        self.assertIn("GEOMETRY_PASS", report["status"])
        self.assertFalse(report["figure_records"][0]["effective_share_verified"])
        self.assertGreaterEqual(report["figure_records"][0]["placed_picture_share"], .70)
        self.assertEqual(report["figure_records"][1]["layout_exception"], "LONG_OBJECTIVES_REQUIRES_MANUAL_REVIEW")

    def test_dominant_geometry_for_standard_slides(self):
        row = self.data["slides"][1]
        reserved = geometry_share(slot_for(row), usable_bounds(row))
        self.assertGreaterEqual(reserved, .70)
        self.assertLessEqual(reserved, .80)

    def test_incompatible_source_aspect_ratio_blocks_assembly(self):
        self.make_images()
        Image.new("RGB", (900, 1800), "white").save(
            self.figure_dir / "figure_02.png")
        make_text(self.manifest, self.stage)
        with self.assertRaisesRegex(Blocked, "placed figure share"):
            assemble(self.manifest, self.stage, self.figure_dir, self.final, self.qa)

    def test_all_without_images_exits_with_blocked_status(self):
        code = main(["all", "--manifest", str(self.manifest),
                     "--figures", str(self.figure_dir), "--output-dir", str(self.root / "build")])
        self.assertEqual(code, 2)
        self.assertTrue((self.root / "build" / "deck3_stage1_text.pptx").is_file())
        self.assertFalse((self.root / "build" / "deck3_final.pptx").exists())

    def test_all_after_images_exists_produces_final(self):
        self.make_images()
        out = self.root / "build"
        code = main(["all", "--manifest", str(self.manifest),
                     "--figures", str(self.figure_dir), "--output-dir", str(out)])
        self.assertEqual(code, 0)
        self.assertTrue((out / "deck3_final.pptx").is_file())
        self.assertTrue((out / "deck3_qa.json").is_file())


if __name__ == "__main__":
    unittest.main()
