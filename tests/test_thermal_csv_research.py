"""Behavioral unit tests. Fixtures are synthetic and never empirical evidence."""
import csv
import json
import tempfile
import unittest
from pathlib import Path
from scripts.thermal_csv_research import TABLES, audit, execute, put_csv

class ThermalCSVResearchTests(unittest.TestCase):
 def setUp(self):
  self.temp=tempfile.TemporaryDirectory()
  self.addCleanup(self.temp.cleanup)
  self.base=Path(self.temp.name)
  self.repo=self.base/"repo";self.repo.mkdir()
  self.src=self.base/"inputs";self.src.mkdir()
  self.out=self.base/"output"
 def table(self,name,rows):
  put_csv(self.src/(name+".csv"),TABLES[name],rows)
 def result(self):
  return execute(self.repo,self.src,self.out)
 def test_missing_data_blocks_science_but_generates_contracts(self):
  info=self.result()
  self.assertEqual(info["populated_schema_pass"],0)
  self.assertEqual(info["physical_validations"],0)
  self.assertEqual(len(list((self.out/"templates").glob("*.csv"))),14)
  with (self.out/"research_status.csv").open(newline="",encoding="utf-8") as h:
   status=list(csv.DictReader(h))
  self.assertEqual(len(status),16)
  self.assertEqual(next(r for r in status if r["module"]=="R07")["status"],"BLOCKED_EVIDENCE")
  self.assertEqual(next(r for r in status if r["module"]=="R16")["status"],"OUT_OF_SCOPE_DEFERRED")
  gate=json.loads((self.out/"gate_results.json").read_text())
  self.assertEqual(gate["G6"]["status"],"NOT_TESTED")
 def test_schema_rejects_duplicate_key(self):
  row=dict(installation_id="x",timestamp_utc="2026-08-01T01:00:00Z",ambient_c="42",evidence_id="E1")
  self.table("weather_heat",[row,row])
  result,rows=audit(self.src/"weather_heat.csv","weather_heat")
  self.assertEqual(result["status"],"SCHEMA_FAIL")
  self.assertIn("duplicate_primary_key",result["errors"])
 def test_rejects_invalid_timestamps_and_nonfinite_numbers(self):
  self.table("weather_heat",[dict(installation_id="x",timestamp_utc="2026-08-01 01:00:00",
                                 ambient_c="nan",evidence_id="E1")])
  state,_=audit(self.src/"weather_heat.csv","weather_heat")
  self.assertEqual(state["status"],"SCHEMA_FAIL")
  self.assertIn("invalid_utc",state["errors"])
  self.assertIn("invalid_number",state["errors"])
 def test_referential_integrity_rejects_unverified_source(self):
  self.table("equipment_assets",[dict(asset_id="p",installation_id="site",
                subsystem="P",component_type="distribution_transformer",evidence_id="UNVERIFIED")])
  info=self.result()
  self.assertEqual(info["referential_errors"],1)
  self.assertEqual(info["physical_validations"],0)
 def test_linked_records_remain_candidates_not_validation(self):
  self.table("source_evidence",[dict(evidence_id="E1",source_uri="synthetic:unit-test",
                                   source_type="SYNTHETIC_TEST_FIXTURE",evidence_class="T1",
                                   verified_status="NOT_EMPIRICAL")])
  self.table("equipment_assets",[
   dict(asset_id="p",installation_id="s",subsystem="P",component_type="distribution_transformer",evidence_id="E1"),
   dict(asset_id="t",installation_id="s",subsystem="T_e",component_type="dc_evse",evidence_id="E1")])
  self.table("physical_connections",[dict(connection_id="C1",installation_id="s",
                  source_asset="p",target_asset="t",connection_type="electrical_ac",evidence_id="E1")])
  stamp="2026-08-01T11:00:00Z"
  self.table("transformer_telemetry",[dict(installation_id="s",asset_id="p",timestamp_utc=stamp,
                       top_oil_c="70",winding_c="82",p_total_kw="105",p_non_ev_kw="51",evidence_id="E1")])
  self.table("evse_telemetry",[dict(installation_id="s",asset_id="t",timestamp_utc=stamp,
                       evse_c="61",p_ac_kw="54",p_dc_kw="50",p_requested_kw="55",evidence_id="E1")])
  info=self.result()
  self.assertEqual(info["candidate_linked_pairs"],1)
  self.assertEqual(info["physical_validations"],0)
  with (self.out/"linked_observation_candidates.csv").open(newline="",encoding="utf-8") as h:
   pairs=list(csv.DictReader(h))
  self.assertIn("NOT_VALIDATION",pairs[0]["status"])
  with (self.out/"ac_power_accounting_residuals.csv").open(newline="",encoding="utf-8") as h:
   residuals=list(csv.DictReader(h))
  self.assertEqual(len(residuals),1)
  self.assertAlmostEqual(float(residuals[0]["unresolved_balance_kw"]),0.0)
  self.assertIn("NOT_VALIDATED",residuals[0]["status"])
 def test_two_unconnected_sites_not_merged(self):
  self.table("source_evidence",[dict(evidence_id="E1",source_uri="synthetic:fixture",
      source_type="TEST",evidence_class="T1",verified_status="UNVERIFIED")])
  self.table("equipment_assets",[
    dict(asset_id="p",installation_id="one",subsystem="P",component_type="distribution_transformer",evidence_id="E1"),
    dict(asset_id="t",installation_id="two",subsystem="T_e",component_type="dc_evse",evidence_id="E1")])
  stamp="2026-08-01T11:00:00Z"
  self.table("transformer_telemetry",[dict(installation_id="one",asset_id="p",timestamp_utc=stamp,evidence_id="E1")])
  self.table("evse_telemetry",[dict(installation_id="two",asset_id="t",timestamp_utc=stamp,evidence_id="E1")])
  self.assertEqual(self.result()["candidate_linked_pairs"],0)

if __name__=="__main__":
 unittest.main()
