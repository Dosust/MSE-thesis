"""Fail-closed validator tests; *structural only*, not evidence or physics verification."""
import copy
import json
import unittest
from pathlib import Path

from validate_figure_contract import validate_contract, ContractError

BASE = json.loads((Path(__file__).parent / 'figure_contract_example.json').read_text())


class TestContract(unittest.TestCase):
    def bad(self, mutate):
        data = copy.deepcopy(BASE)
        mutate(data)
        with self.assertRaises(ContractError):
            validate_contract(data)

    def test_reference_example_accepted(self):
        self.assertEqual(validate_contract(BASE)['decision'], 'STRUCTURE_ACCEPTED_NOT_SCIENTIFICALLY_VERIFIED')

    def test_wrong_direction_rejected(self):
        self.bad(lambda d: d['edges'][0].update(source='P2', target='P1'))

    def test_invalid_palette_rejected(self):
        self.bad(lambda d: d['style']['authored_colors'].append('#FF00FF'))

    def test_colored_panel_rejected(self):
        self.bad(lambda d: d['style'].update(panel='#0072B2'))

    def test_false_thermal_interdependency_rejected(self):
        self.bad(lambda d: d['edges'].append(dict(id='E06', source='T1', target='P1', type='CANDIDATE_CAUSAL', evidence_status='MEASURED', label='I2 proven', interface_id='I2', hypothesis='H1')))

    def test_unqualified_candidate_needs_visible_label(self):
        self.bad(lambda d: d['edges'].append(dict(id='E06', source='T1', target='P1', type='CANDIDATE_CAUSAL', evidence_status='CANDIDATE_UNQUALIFIED', label='I2', interface_id='I2', hypothesis='H1')))

    def test_ambient_heat_is_not_physical_interdependence(self):
        self.bad(lambda d: d['edges'][3].update(source='P1', target='T1'))

    def test_explanatory_motion_cannot_claim_physical_time(self):
        self.bad(lambda d: d['animation'].update(physical_time_claim=True))

    def test_physical_time_requires_equations_and_validation_status(self):
        self.bad(lambda d: d['animation'].update(kind='PHYSICAL_TIME', clock='PHYSICAL_MODEL_TIME'))

    def test_evidence_assertion_requires_traceable_source(self):
        self.bad(lambda d: d['edges'][0].update(evidence_status='MEASURED'))

    def test_duplicate_node_id_rejected(self):
        self.bad(lambda d: d['nodes'].append(copy.deepcopy(d['nodes'][0])))

    def test_unqualified_candidate_can_be_encoded(self):
        d = copy.deepcopy(BASE)
        d['edges'].append(dict(id='E06', source='T1', target='P1', type='CANDIDATE_CAUSAL', evidence_status='CANDIDATE_UNQUALIFIED', label='I2 candidate — not yet qualified', interface_id='I2', hypothesis='H1: grid-side AC demand response conditional'))
        self.assertEqual(validate_contract(d)['edges'], 6)

    def test_gold_decorative_role_rejected(self):
        self.bad(lambda d: d['style']['authored_colors'].append('#FFC627'))

    def test_nonexistent_node_endpoint_rejected(self):
        self.bad(lambda d: d['edges'][0].update(target='FOO'))


if __name__ == '__main__':
    unittest.main()
