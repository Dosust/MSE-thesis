"""Regression tests for user-authorized 10-slide progress routing.
Structural correctness does not validate scientific source claims or figure rendering.
"""
import json
import sys
import tempfile
import unittest
from pathlib import Path

from pptx import Presentation

DECK = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(DECK / "examples"))
from deck3 import (Blocked, TEN_PROGRESS_VARIANT, load_manifest, make_text)

TITLES = [
    "Physics-Based Mathematical Engineering of Power–Transportation Interdependencies for Resilience",
    "Outline", "Research Background", "Research Problem, Gap & Objectives",
    "Physical System Architecture", "Research Methodology", "Work Completed",
    "Preliminary Results", "Remaining Work & Research Plan", "Thank You",
]


def sample():
    slides = []
    for i, title in enumerate(TITLES):
        kind = "title" if i == 0 else "outline" if i == 1 else "thanks" if i == 9 else "content"
        row = {"kind": kind, "title": title, "notes": ""}
        if kind == "title":
            row["subtitle"] = "DUMMY TEST ONLY"
        elif kind == "outline":
            row["message"] = "Presentation topics — DUMMY TEST ONLY"
            row["bullets"] = ["Research context", "Physical system", "Methods", "Results"]
        elif kind == "content":
            row["message"] = "DUMMY TEST ONLY"
            row["bullets"] = ["Dummy point A", "Dummy point B", "Dummy point C"]
            row["source_note"] = "Test fixture only; NOT science/experimental evidence"
        slides.append(row)
    return {
        "deck_variant": TEN_PROGRESS_VARIANT,
        "source_record": "USER_APPROVED_2026-10-13_TEN_SLIDE_TOPICS_FIXTURE",
        "institution": "Arizona State University",
        "frozen_strings": [TITLES[0]],
        "slides": slides,
    }


class TenSlideRoutingTests(unittest.TestCase):
    def load(self, obj):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / "manifest.json"
            f.write_text(json.dumps(obj), encoding="utf-8")
            return load_manifest(f)

    def test_exact_ten_variant_and_source_are_accepted_structurally(self):
        self.assertEqual(len(self.load(sample())["slides"]), 10)

    def test_rejects_missing_ninth_or_extra_eleventh(self):
        for n in (9, 11):
            x = sample()
            if n == 9:
                x["slides"].pop()
            else:
                x["slides"].append({"kind": "content", "title": "Extra",
                                     "message": "test", "bullets": ["a", "b", "c"],
                                     "source_note": "test"})
            with self.assertRaises(Blocked):
                self.load(x)

    def test_rejects_unapproved_renaming(self):
        x = sample()
        x["slides"][4]["title"] = "AI Generated System Diagram"
        with self.assertRaises(Blocked):
            self.load(x)

    def test_rejects_unnamed_source(self):
        x = sample()
        del x["source_record"]
        with self.assertRaises(Blocked):
            self.load(x)

    def test_rejects_generic_placeholder_title(self):
        x = sample()
        x["slides"][0]["title"] = "Title"
        with self.assertRaises(Blocked):
            self.load(x)

    def test_outline_and_thanks_do_not_require_three_points(self):
        x = self.load(sample())
        self.assertEqual(len(x["slides"][1]["bullets"]), 4)
        self.assertNotIn("bullets", x["slides"][9])

    def test_rejects_title_image_on_outline_and_thanks(self):
        for index in (1, 9):
            x = sample()
            x["slides"][index]["figure"] = {"file": "illustration.png", "alt": "fixture"}
            with self.assertRaises(Blocked):
                self.load(x)

    def test_renders_four_outline_topics_and_thanks_as_native_editable_text(self):
        with tempfile.TemporaryDirectory() as d:
            mf = Path(d) / "m.json"
            pp = Path(d) / "ten.pptx"
            mf.write_text(json.dumps(sample()), encoding="utf-8")
            make_text(mf, pp)
            prs = Presentation(pp)
            self.assertEqual(len(prs.slides), 10)
            outline = "\n".join(sh.text for sh in prs.slides[1].shapes if sh.has_text_frame)
            self.assertIn("Results", outline)
            thanks = "\n".join(sh.text for sh in prs.slides[9].shapes if sh.has_text_frame)
            self.assertIn("Thank You", thanks)

    def test_production_uses_actual_standards_and_source_first(self):
        policy = (DECK / "references" / "DECK3_PROFESSIONAL_ENGINEERING_VISUAL_REFERENCES_V1.md")
        router = (DECK / "references" / "DECK3_PRESENTATION_VARIANT_ROUTER_V1.md")
        self.assertTrue(policy.is_file())
        self.assertTrue(router.is_file())
        t = policy.read_text(encoding="utf-8")
        for key in ("IEC 60617", "SysML", "INCOSE", "OpenDSS", "Nature",
                    "Manim", "IEEE", "source", "rights", "20Cable"):
            self.assertIn(key, t)

    def test_canonical_scope_and_palette_are_not_modified_by_routing(self):
        palette = json.loads((DECK / "references" / "DECK3_SRGB_PALETTE.json").read_text())
        self.assertEqual(len(palette["colors"]), 13)


if __name__ == "__main__":
    unittest.main()
