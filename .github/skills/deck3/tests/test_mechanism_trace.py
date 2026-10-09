"""Deck3 mechanism trace source-test suite. Not a physics or citation-content test."""
import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from PIL import Image

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE / "examples"))
from mechanism_trace_qa import verify, check
from deck3 import Blocked, figure_records

class MechanismTraceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = json.loads((HERE/"examples"/"mechanism_trace_example.json").read_text(encoding="utf-8"))
    def edited(self):
        return copy.deepcopy(self.source)
    def rejected(self,d,fragment):
        self.assertTrue(any(fragment in e for e in verify(d)["errors"]), verify(d))
    def test_valid_candidate_trace_not_automatically_physics_validated(self):
        r=verify(self.source)
        self.assertEqual(r["errors"],[])
        self.assertEqual(r["status"],"STRUCTURAL_TRACE_PASS_NOT_PHYSICS_VERIFIED")
        self.assertFalse(r["physics_validated"])
        self.assertFalse(r["citation_content_verified"])
    def test_duplicate_object_id_rejected(self):
        d=self.edited(); d["objects"][1]["id"]=d["objects"][0]["id"]
        self.rejected(d,"duplicate object ID")
    def test_unlinked_boundary_member_rejected(self):
        d=self.edited(); d["boundaries"][0]["members"].append("invented")
        self.rejected(d,"boundary member")
    def test_missing_boundary_semantics_rejected(self):
        d=self.edited(); d["boundaries"][0]["meaning"]=""
        self.rejected(d,"boundary lacks meaning")
    def test_missing_arrow_endpoint_rejected(self):
        d=self.edited(); d["arrows"][0]["to"]="not-an-object"
        self.rejected(d,"arrow endpoint")
    def test_unlabeled_arrow_rejected(self):
        d=self.edited(); d["arrows"][0]["label"]=""
        self.rejected(d,"missing label")
    def test_unquantified_arrow_without_open_tag_rejected(self):
        d=self.edited(); d["arrows"][0]["carried_quantity"]=""
        self.rejected(d,"missing carried_quantity")
    def test_missing_physical_law_without_open_tag_rejected(self):
        d=self.edited(); d["arrows"][0]["law_or_operator"]=""
        self.rejected(d,"missing law_or_operator")
    def test_missing_grid_side_ac_gate_for_te_to_p_rejected(self):
        d=self.edited(); d["arrows"][4]["evidence_gate"]="DC output alone"
        self.rejected(d,"grid_side_ac")
    def test_candidate_not_promoted_to_established_without_evidence(self):
        d=self.edited(); d["arrows"][0]["evidence_status"]="ESTABLISHED"
        self.rejected(d,"no source")
    def test_qualified_arrow_requires_explicit_gate(self):
        d=self.edited(); a=d["arrows"][0]; a["evidence_status"]="QUALIFIED";a["sources"]=["DOI-to-verify"]
        a["evidence_gate"]="OPEN"
        self.rejected(d,"qualification gate")
    def test_unsupported_bidir_arrow_type_rejected(self):
        d=self.edited(); d["arrows"][1]["type"]="unverified_bidirectional_magic"
        self.rejected(d,"unknown arrow type")
    def test_physical_cross_sector_relation_not_sequence(self):
        d=self.edited(); d["arrows"][4]["type"]="sequence"
        self.rejected(d,"mere sequence")
    def test_claimed_review_field_must_be_explicit(self):
        d=self.edited(); d["review"]["physics"]="CERTIFIED"
        self.rejected(d,"invalid or absent review.physics")
    def test_corrupted_trace_json_blocked(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"bad.trace.json";p.write_text("{missing",encoding="utf-8")
            self.assertEqual(check(p)["status"],"BLOCKED")
    def test_legacy_png_without_sidecar_is_provisional(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"figure.png"
            Image.new("RGB",(1600,900),"white").save(p)
            rows={"slides":[{"figure":{"file":"figure.png","alt":"Concept example."}}]}
            rec=figure_records(rows,td)[0]
            self.assertEqual(rec["mechanism_trace_qa"]["status"],"TRACE_NOT_REGISTERED_PROVISIONAL")
    def test_malformed_attached_trace_blocks_stage2(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"figure.png"
            Image.new("RGB",(1600,900),"white").save(p)
            (Path(td)/"figure.trace.json").write_text('{"schema":"bad"}')
            rows={"slides":[{"figure":{"file":"figure.png","alt":"Concept example."}}]}
            with self.assertRaises(Blocked):
                figure_records(rows,td)
    def test_valid_attached_trace_passes_structure_only(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)/"figure.png"
            Image.new("RGB",(1600,900),"white").save(p)
            (Path(td)/"figure.trace.json").write_text(json.dumps(self.source))
            rows={"slides":[{"figure":{"file":"figure.png","alt":"Concept example."}}]}
            rec=figure_records(rows,td)[0]
            self.assertEqual(rec["mechanism_trace_qa"]["status"],"STRUCTURAL_TRACE_PASS_NOT_PHYSICS_VERIFIED")
if __name__=="__main__":
    unittest.main()
