import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "examples" / "unified_pptx.py"
ROUTER = ROOT / "examples" / "unified_agent_router.js"
PALETTE = ROOT / "references" / "DECK3_SRGB_PALETTE.json"

def call(*args):
    return subprocess.run(args, check=True, capture_output=True, text=True)

class UnifiedDeck3Tests(unittest.TestCase):
    def test_route_regressions(self):
        scenarios = [
            ("Deck3", "status"), ("Deck3 figure slide 6", "figure"),
            ("Deck3 update colors", "ecosystem_update"), ("Deck3 math slide 10", "math"),
            ("Deck3 animate slide 9", "animate"), ("Deck3 QA", "audit"),
            ("Deck3 all", "all"), ("Deck3 slide 22", "blocked")]
        for prompt, expected in scenarios:
            with self.subTest(prompt=prompt):
                self.assertEqual(json.loads(call("node", str(ROUTER), prompt).stdout)["intent"], expected)

    def test_template_build_revision_and_qa(self):
        slides = [{"title":f"Approved title {i}", "message":f"Approved message {i}",
                   "bullets":["Evidence-based point"],"source_note":"Source retained",
                   "notes":"Assumption and limitation"} for i in range(1,14)]
        with tempfile.TemporaryDirectory() as td:
            p=Path(td); manifest=p/"source.json"; manifest.write_text(json.dumps({"slides":slides}))
            out=p/"deck-v1.pptx"; edited=p/"deck-v2.pptx"
            call(sys.executable,str(CLI),"build",str(manifest),str(out),"--palette",str(PALETTE))
            inv=json.loads(call(sys.executable,str(CLI),"inspect",str(out)).stdout)
            self.assertEqual(inv["slide_count"],13)
            self.assertIn("Approved message 9",[x["text"] for x in inv["slides"][8]["shapes"]])
            qa=json.loads(call(sys.executable,str(CLI),"qa",str(out),"--palette",str(PALETTE)).stdout)
            self.assertEqual(qa["checks"]["slide_count"],"PASS")
            self.assertEqual(qa["checks"]["palette_xml"],"PASS")
            self.assertEqual(qa["checks"]["native_omml"],"NOT_RUN")
            self.assertEqual(qa["checks"]["real_render"],"NOT_RUN")
            call(sys.executable,str(CLI),"revise",str(out),str(edited),"--slide","9",
                 "--old","Approved message 9","--new","Approved corrected message")
            after=json.loads(call(sys.executable,str(CLI),"inspect",str(edited)).stdout)
            before=json.loads(call(sys.executable,str(CLI),"inspect",str(out)).stdout)
            self.assertEqual(before["slides"][8]["shapes"][1]["text"],"Approved message 9")
            self.assertEqual(after["slides"][8]["shapes"][1]["text"],"Approved corrected message")
            self.assertEqual(after["slides"][7]["shapes"],before["slides"][7]["shapes"])
            self.assertEqual(after["slides"][8]["notes"],before["slides"][8]["notes"])
            with self.assertRaises(subprocess.CalledProcessError):
                call(sys.executable,str(CLI),"revise",str(out),str(edited),"--slide","9",
                     "--old","Approved message 9","--new","Unsafe overwrite")
if __name__=="__main__":
    unittest.main()
