"""Integrity and safety regression tests for the executed thesis dataset qualification."""
import csv,json,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parent

class ThesisGateTests(unittest.TestCase):
 def test_sintef_publisher_md5(self):
  j=json.loads((ROOT/'01_provenance/source_registry.json').read_text())
  for name in ('Barug2025_sensordata.csv','Barug2025_calculated.csv'):
   row=next(x for x in j if x['asset']==name)
   self.assertTrue(row['publisher_md5_matches'],f'{name} publisher checksum mismatch')
 def test_epfl_all_session_keys_matched_after_verified_offset(self):
  j=json.loads((ROOT/'04_epfl/epfl_summary.json').read_text())
  self.assertEqual(j['measured_rows_total'],61816)
  self.assertEqual(j['published_minus_populated'],2461)
  self.assertEqual(j['session_workbook']['matched_session_keys'],1878)
  self.assertEqual(j['session_workbook']['unmatched_measurement_session_keys'],0)
  self.assertEqual(j['session_workbook']['CCS2_session_id_offset_for_matching'],1129)
 def test_vehicle_complete_session_split(self):
  with (ROOT/'02_vehicle/session_splits.csv').open() as f:
   r=list(csv.DictReader(f))
  pairs=[x['name'] for x in r]
  self.assertEqual(len(pairs),len(set(pairs)),'same CSV cannot exist in two train/test splits')
 def test_no_field_coupled_claim(self):
  with (ROOT/'acceptance_gates.csv').open() as f:
   r={x['work_package']:x['decision'] for x in csv.DictReader(f)}
  self.assertEqual(r['05_EVSE_Thermal_Law_Evidence'],'BLOCKED')
  self.assertEqual(r['06_Directional_Coupling_Qualification'],'BLOCKED')
  self.assertEqual(r['07_Coupled_Model_VVUQ'],'BLOCKED')
  self.assertEqual(r['08_Service_Resilience_Sustainability_Results'],'BLOCKED')
 def test_sintef_calculated_separate_from_sensor(self):
  rows=json.loads((ROOT/'01_provenance/source_registry.json').read_text())
  measured=next(x for x in rows if x['asset']=='Barug2025_sensordata.csv')
  calc=next(x for x in rows if x['asset']=='Barug2025_calculated.csv')
  self.assertNotEqual(measured['sha256'],calc['sha256'])
  self.assertIn('NOT independent',calc['scientific_classification'])

if __name__=='__main__':unittest.main()
