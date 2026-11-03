import hashlib
import json
import math
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent))
from audit_uploaded_ev_archive import haversine_km, sha256_file

class DataAuditTests(unittest.TestCase):
    def test_geo_zero_distance(self):
        self.assertAlmostEqual(haversine_km(32.78,-96.8,32.78,-96.8),0.0,places=9)
    def test_geo_one_degree_latitude(self):
        self.assertTrue(110.9<haversine_km(0,0,1,0)<111.3)
    def test_file_hash(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'x';p.write_bytes(b'evidence-qualification')
            self.assertEqual(sha256_file(p),hashlib.sha256(b'evidence-qualification').hexdigest())
    def test_zip_integrity(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'x.zip'
            with zipfile.ZipFile(p,'w') as z:z.writestr('hello.csv','value\n42\n')
            with zipfile.ZipFile(p) as z:self.assertIsNone(z.testzip())
    def test_quarantine_gate(self):
        d=json.loads((Path(__file__).resolve().parent.parent/'audit_results.json').read_text())
        self.assertEqual(d['field_measurement_status'],'NOT_QUALIFIED')
        self.assertFalse(d['has_verified_transformer_charger_topology'])
        self.assertFalse(d['has_evse_internal_temperature'])
        self.assertFalse(d['has_transformer_temperature'])

if __name__=='__main__':unittest.main()
