"""Deck3 v1.8.1 regression: file presence never certifies a scientific infographic."""
import sys
import tempfile
import unittest
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "examples"))
from deck3 import figure_records

class MediaRoutingTests(unittest.TestCase):
    def test_raster_without_source_has_explicit_unreviewed_image_gate(self):
        with tempfile.TemporaryDirectory() as folder:
            Image.new("RGB", (1672, 941), "white").save(Path(folder) / "picture.png")
            rows={"slides":[{"kind":"content","figure":{"file":"picture.png","alt":"Conceptual test only"}}]}
            rec=figure_records(rows, folder)[0]
            self.assertEqual(rec["image_composition_review"],"NOT_REVIEWED_NO_EXPLANATORY_PANEL_GATE")
            self.assertFalse(rec["ready_for_certified_assembly"])
            self.assertFalse(rec["native_individual_object_editability"])
            self.assertEqual(rec["mechanism_trace_qa"]["status"],"TRACE_NOT_REGISTERED_PROVISIONAL")
    def test_media_routing_standard_is_connected_to_main_skill(self):
        policy=(ROOT/"references/DECK3_MEDIA_ROUTING_AND_FAIL_CLOSED_IMAGE_QA_V1.md")
        self.assertTrue(policy.is_file())
        main=(ROOT/"SKILL.md").read_text(encoding="utf-8")
        self.assertIn("DECK3_MEDIA_ROUTING_AND_FAIL_CLOSED_IMAGE_QA_V1.md", main)
    def test_new_policy_does_not_authorize_silent_slide_count_change(self):
        p=(ROOT/"references/DECK3_MEDIA_ROUTING_AND_FAIL_CLOSED_IMAGE_QA_V1.md").read_text(encoding="utf-8")
        self.assertIn("13-slide",p)
        self.assertIn("eight slides",p)
        self.assertIn("independently editable",p)
    def test_cli_does_not_claim_stage2_compliance_from_png_integrity(self):
        code=(ROOT/"examples/deck3.py").read_text(encoding="utf-8")
        self.assertIn("ASSET INTEGRITY ONLY",code)
        self.assertNotIn("PASS stage 2 asset audit",code)

if __name__ == "__main__":
    unittest.main()
