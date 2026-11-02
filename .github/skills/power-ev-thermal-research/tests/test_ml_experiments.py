import csv
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
from check_ml_experiments import check_root, REQUIRED

class EvidenceLearningTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.root=Path(self.temp.name)
        self.file=self.root/'ml_experiment_register.csv'
        self.headers=sorted(REQUIRED)

    def tearDown(self):self.temp.cleanup()

    def write(self, rows):
        with self.file.open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=self.headers);w.writeheader();w.writerows(rows)

    def base(self):
        return dict(experiment_id='e1',comparison_group='c1',model_family='M0',model_id='m0',
          target_channel='top_oil',target_unit='C',site_id='s1',asset_id='tr1',source_id='src1',raw_sha256='h1',
          input_information_set='weather_known',horizon_minutes='60',train_manifest='train.csv',
          validation_manifest='val.csv',test_manifest='test.csv',independent_heldout='true',
          uses_observed_future_inputs='false',physical_topology_verified='false',
          transformer_temperature_measured='true',evse_temperature_measured='false',
          claimed_connected_thermal_field_validation='false',source_domain_extreme_heat_verified='false',
          physics_constraints_verified='false',experiment_status='EXPLORATORY',
          test_mae='1',baseline_mae='2',test_rmse='1.2',baseline_rmse='2.2',n_test='30',notes='test')

    def test_blank_is_schema_only(self):
        self.write([])
        self.assertEqual(check_root(self.root)[0],[])
        self.assertTrue(check_root(self.root,True)[0])

    def test_measured_component_does_not_claim_coupled(self):
        self.write([self.base()]);self.assertEqual(check_root(self.root,True)[0],[])

    def test_field_claim_without_evse_thermometer_blocked(self):
        x=self.base();x['experiment_status']='CONNECTED_THERMAL_FIELD_VALIDATED';x['claimed_connected_thermal_field_validation']='true'
        self.write([x]);self.assertIn('evse_temperature_measured',str(check_root(self.root)[0]))

    def test_field_claim_cannot_use_observed_future(self):
        x=self.base();x.update(physical_topology_verified='true',evse_temperature_measured='true',
          physics_constraints_verified='true',claimed_connected_thermal_field_validation='true',
          experiment_status='CONNECTED_THERMAL_FIELD_VALIDATED',uses_observed_future_inputs='true')
        self.write([x]);self.assertIn('conditional hindcast',str(check_root(self.root)[0]))

    def test_comparison_requires_M0_M1(self):
        x=self.base();x.update(model_family='M2',model_id='hybrid',experiment_status='COMPARATIVE_CLAIM')
        self.write([x]);self.assertIn('missing M0',str(check_root(self.root)[0]))

    def test_comparison_rejects_different_test_partitions(self):
        r=[self.base() for _ in range(3)]
        for i,m in enumerate(('M0','M1','M2')):
            r[i].update(experiment_id=f'x{i}',model_id=m,model_family=m,experiment_status='COMPARATIVE_CLAIM')
        r[2]['test_manifest']='other_test.csv'
        self.write(r);self.assertIn('identical site/target',str(check_root(self.root)[0]))

    def test_valid_comparator_schema(self):
        r=[]
        for i,m in enumerate(('M0','M1','M2')):
            row=self.base();row.update(experiment_id=f'x{i}',model_id=m,model_family=m,experiment_status='COMPARATIVE_CLAIM')
            r.append(row)
        self.write(r);self.assertEqual(check_root(self.root,True)[0],[])

if __name__=='__main__':unittest.main()
