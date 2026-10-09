"""Synthetic science-category and policy tests; not physical validation."""
import sys
import unittest
from pathlib import Path
R=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(R/"examples"))
from scientific_sanity_gates import charger_input_balance,directional_admission_requirements,causal_event_delay,comparator_matched,approval_from_raster_only

class Deck3AllFormsV2(unittest.TestCase):
    def test_policy_gates(self):
        s=(R/"references/DECK3_ALL_FORMS_WEAKNESS_LEARNING_V2.md").read_text()
        self.assertTrue(all(f"G{i:02}" in s for i in range(1,16)))
        self.assertTrue(all(f"A{i:02}" in s for i in range(1,21)))
        self.assertIn("B13",s)

    def test_skill_and_runtime(self):
        s=(R/"SKILL.md").read_text()
        self.assertIn('version: "1.8.3"',s)
        self.assertIn("DECK3_ALL_FORMS_WEAKNESS_LEARNING_V2.md",s)
        self.assertIn("scientific_gates",(R/"examples/deck3.py").read_text())

    def test_ac_boundary(self):
        self.assertEqual(charger_input_balance(55,50,1)["other_loss_kw"],4)
        self.assertEqual(charger_input_balance(55,50,1,2)["other_loss_kw"],2)
        with self.assertRaises(ValueError): charger_input_balance(40,50,1)

    def test_directional_evidence(self):
        a=directional_admission_requirements("TE_TO_P",{"thermal_state":"hot"})
        self.assertIn("grid_side_ac_observation",a["missing"])
        b=directional_admission_requirements("P_TO_TE",{"thermal_state":"hot"})
        self.assertIn("permissible_supply_rule",b["missing"])

    def test_time_causality(self):
        self.assertIsNone(causal_event_delay(1,3,False))
        self.assertIsNone(causal_event_delay(None,3,True))
        self.assertEqual(causal_event_delay(1,3,True),2)

    def test_comparator_and_image(self):
        x=dict(heat_case=1,asset_case=2,controls_case=3,initial_state_case=4,service_requirement=5,time_horizon=6)
        self.assertTrue(comparator_matched(x,x)["matched"])
        self.assertFalse(comparator_matched(x,dict(x,controls_case=99))["matched"])
        self.assertEqual(approval_from_raster_only(True),"ARTWORK_PROVISIONAL")
