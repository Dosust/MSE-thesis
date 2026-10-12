import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1] / "scripts"))
from thermal_research_agent import validate_task,validate_claim,GATES

def task(**changes):
    t={"task_id":"T-001","role":"physics","objective":"SO2",
       "components":["P1","T1"],"interfaces":["I2"],"action":"derive"}
    t.update(changes)
    return t

def claim(**changes):
    c={"claim_id":"C-001","authority":"frozen-thermal-objectives",
       "objective":"SO2","components":["P1","T1"],"interfaces":["I2"],
       "mechanism":"candidate AC-mediated thermal response",
       "equations":["energy balance"],"assumptions":["steady averaged AC boundary"],
       "sources":[],"tests":[],"uncertainty":"not estimated","validity_domain":"",
       "evidence_levels":["S","L"],"gate_results":{g:"NOT_TESTED" for g in GATES},
       "status":"PROPOSED"}
    c.update(changes)
    return c

class TestGovernance(unittest.TestCase):
    def test_research_task(self):
        self.assertEqual(validate_task(task())["agent"],"A2")
    def test_prohibited_action(self):
        self.assertEqual(validate_task(task(action="merge"))["decision"],"BLOCKED_HUMAN_DECISION")
    def test_bad_component(self):
        with self.assertRaises(ValueError): validate_task(task(components=["P99"]))
    def test_unvalidated(self):
        self.assertIn("NOT_SCIENTIFICALLY_VERIFIED",validate_claim(claim())["decision"])
    def test_prevent_false_validation(self):
        with self.assertRaises(ValueError): validate_claim(claim(status="VALIDATED_IN_DOMAIN"))
    def test_bad_gate(self):
        with self.assertRaises(ValueError): validate_claim(claim(gate_results={"G0":"PASS"}))
    def test_bad_evidence(self):
        with self.assertRaises(ValueError): validate_claim(claim(evidence_levels=["MADE_UP"]))
if __name__=="__main__": unittest.main()
