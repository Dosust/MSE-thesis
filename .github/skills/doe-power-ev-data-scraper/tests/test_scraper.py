import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from doe_scraper import Scraper, HrefParser, allowed, safe_name, classify_name

class ScraperTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.s=Scraper(self.tmp.name,delay=0)
 def tearDown(self):self.tmp.cleanup()
 def test_url_allowlist(self):
  self.assertTrue(allowed('https://zenodo.org/api/records/14065331'))
  self.assertFalse(allowed('http://zenodo.org/api/records/14065331'))
  self.assertFalse(allowed('https://zenodo.org.attacker.com/'))
  self.assertFalse(allowed('https://x:pass@zenodo.org/'))
 def test_safe_name(self):self.assertEqual(safe_name('../../a b.csv'),'a_b.csv')
 def test_file_classification(self):
  self.assertEqual(classify_name('foo.csv'),'CANDIDATE_DATA_FILE')
  self.assertEqual(classify_name('loads.dss'),'ELECTRICAL_TOPOLOGY_MODEL')
  self.assertEqual(classify_name('overview.pdf'),'DOCUMENT_NOT_MEASUREMENTS')
 def test_links_and_origins(self):
  p=HrefParser();p.feed('<a href="/file.csv">Data</a>')
  self.assertEqual(p.hrefs,[('/file.csv','Data')])
 def test_no_hallucinated_field_claim(self):
  self.s.add('DOE','METADATA','', 'https://www.energy.gov/oe/power-system-data-analytics', 'some.csv','https://zenodo.org/files/some.csv')
  self.assertEqual(self.s.rows[0]['connected_thermal_field_verified'],'NO')
  self.assertEqual(self.s.rows[0]['direct_link_status'],'DISCOVERED_UNTESTED')
 def test_no_unsafe_link(self):
  self.s.add('DOE','FIELD','','','f.csv','https://evil.example/a.csv')
  self.assertEqual(len(self.s.rows),0)
 def test_duplicate(self):
  a=('S','FIELD','','https://zenodo.org/records/2','x.csv','https://zenodo.org/x.csv')
  self.s.add(*a);self.s.add(*a);self.assertEqual(len(self.s.rows),1)
 def test_zenodo_api_parse(self):
  self.s.logged_json=lambda s,u:{'files':[{'key':'measurements.csv','size':21,'checksum':'md5:abc','links':{'content':'https://zenodo.org/api/records/14065331/files/measurements.csv/content'}}]}
  self.s.zenodo('x','14065331','LAB','doi')
  self.assertEqual(self.s.rows[0]['reported_bytes'],21)
  self.assertTrue(self.s.rows[0]['file_url'].startswith('https://zenodo.org/api/'))
 def test_ornl_only_exposed_file_id(self):
  self.s._walk_files('ORNL','FIELD','','page','dataset',{'record':{'fields':{'file':{'id':'a'*32,'filename':'Original.csv'}}}},'API')
  self.assertEqual(self.s.rows[0]['file_url'],'https://openenergyhub.ornl.gov/api/explore/v2.1/catalog/datasets/dataset/files/'+('a'*32))
 def test_file_signature(self):
  path=Path(self.tmp.name)/'d.csv';path.write_text('timestamp,power\n1,5\n')
  self.assertEqual(self.s.signature(path),'TEXT_DELIMITED')
  path.write_text('<!doctype html>login</html>')
  self.assertEqual(self.s.signature(path),'REJECT_HTML_OR_API_ERROR')
 def test_write_summary(self):
  summary=self.s.write();self.assertFalse(summary['measured_connected_transformer_evse_thermal_field_data_verified'])
  self.assertTrue((Path(self.tmp.name)/'file_candidates.csv').exists())
 def test_aggregate_record_provenance(self):
  self.s._walk_files('n','LAB','doi','page','x',{'file':{'id':'b'*32,'filename':'abc.zip','size':300}},'API')
  self.assertIn('b'*32,self.s.rows[0]['file_url'])
  self.assertEqual(self.s.rows[0]['kind'],'ARCHIVE_CONTENT_UNKNOWN')

if __name__=='__main__':unittest.main()
