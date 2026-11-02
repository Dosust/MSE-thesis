import csv,importlib.util,tempfile,unittest
from pathlib import Path
P=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('check_evidence',P/'tools/check_evidence.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class EvidenceTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory(); self.path=Path(self.tmp.name)
  for templ in (P/'templates').glob('*.csv'):
   (self.path/templ.name).write_text(templ.read_text())
 def tearDown(self):self.tmp.cleanup()
 def add(self,name,values):
  with (self.path/name).open(newline='',encoding='utf8') as f: hdr=next(csv.reader(f))
  with (self.path/name).open('a',newline='',encoding='utf8') as f:
   w=csv.DictWriter(f,hdr);w.writerow(values)
 def test_empty_header_only_pass(self):
  self.assertEqual([],m.check_root(self.path)[0])
 def test_false_coupled_claim_fails(self):
  self.add('thermal_interface_evidence.csv',dict(evidence_id='X',site_id='site',source_id='source',direction='P_TO_TE',source_link='doi:unknown',evidence_tier='CONNECTED_THERMAL_FIELD_VALIDATED',same_site_verified='true',physical_topology_verified='false',clock_sync_verified='true',transformer_thermal_measured='true',evse_thermal_measured='true',directional_mechanism_verified='true',independent_test_pass='true'))
  self.assertTrue(any('connected-field validation without' in e for e in m.check_root(self.path)[0]))
 def test_unqualified_same_premises_is_allowed(self):
  self.add('thermal_interface_evidence.csv',dict(evidence_id='X',site_id='site',source_id='source',direction='P_TO_TE',evidence_tier='MEASURED_SAME_PREMISES_ELECTRICAL',physical_topology_verified='false'))
  self.assertEqual([],m.check_root(self.path)[0])
 def test_invalid_source_duplicate(self):
  for i in range(2):self.add('source_registry.csv',dict(source_id='same',measurement_kind='DIRECT_MEASURED',source_access_status='ACQUIRED_VERIFIED'))
  self.assertTrue(any('duplicate source_id' in e for e in m.check_root(self.path)[0]))
if __name__=='__main__':unittest.main()
