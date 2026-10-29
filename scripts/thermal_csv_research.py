#!/usr/bin/env python3
"""Thermal thesis CSV evidence-readiness audit; never an empirical validation."""
from __future__ import annotations
import argparse, csv, hashlib, json, math
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

TABLES = {
 "source_evidence": "evidence_id source_uri source_type evidence_class verified_status",
 "coupling_mechanism_tests": "mechanism_id direction source_asset target_asset evidence_id test_status",
 "equipment_assets": "asset_id installation_id subsystem component_type evidence_id",
 "physical_connections": "connection_id installation_id source_asset target_asset connection_type evidence_id",
 "weather_heat": "installation_id timestamp_utc ambient_c evidence_id",
 "transformer_telemetry": "installation_id asset_id timestamp_utc top_oil_c winding_c p_total_kw p_non_ev_kw evidence_id",
 "evse_telemetry": "installation_id asset_id timestamp_utc evse_c p_ac_kw p_dc_kw p_requested_kw evidence_id",
 "vehicle_charging_sessions": "session_id installation_id evse_asset_id arrival_utc departure_utc required_kwh delivered_kwh evidence_id",
 "operator_events": "event_id installation_id asset_id timestamp_utc event_type action_record evidence_id",
 "identified_models": "model_id component equation_reference parameters_reference validation_status evidence_id",
 "validation_predictions": "prediction_id model_id asset_id timestamp_utc observed_value predicted_value unit split evidence_id",
 "service_requirements": "requirement_id installation_id service_type unit requirement_source evidence_id",
 "case_scenarios": "scenario_id baseline_id heat_event_id intervention_id scenario_type evidence_id",
 "sustainability_indicators": "indicator_id scenario_id dimension value unit boundary period evidence_id",
}
TABLES = {k: tuple(v.split()) for k,v in TABLES.items()}
KEYS = {
 "weather_heat": ("installation_id","timestamp_utc"),
 "transformer_telemetry": ("installation_id","asset_id","timestamp_utc"),
 "evse_telemetry": ("installation_id","asset_id","timestamp_utc"),
}
NUMERIC = {"ambient_c","top_oil_c","winding_c","p_total_kw","p_non_ev_kw",
 "evse_c","p_ac_kw","p_dc_kw","p_requested_kw","required_kwh","delivered_kwh",
 "observed_value","predicted_value","value"}
MODULES = {
 "R01":"source_evidence",
 "R02":"source_evidence weather_heat transformer_telemetry evse_telemetry",
 "R03":"equipment_assets physical_connections",
 "R04":"weather_heat",
 "R05":"transformer_telemetry equipment_assets",
 "R06":"evse_telemetry vehicle_charging_sessions",
 "R07":"evse_telemetry transformer_telemetry physical_connections operator_events",
 "R08":"transformer_telemetry evse_telemetry operator_events physical_connections",
 "R09":"identified_models physical_connections transformer_telemetry evse_telemetry",
 "R10":"operator_events transformer_telemetry evse_telemetry",
 "R11":"identified_models validation_predictions",
 "R12":"identified_models validation_predictions",
 "R13":"service_requirements vehicle_charging_sessions",
 "R14":"case_scenarios operator_events service_requirements",
 "R15":"case_scenarios sustainability_indicators service_requirements",
}
GOVERNANCE = ("project/CANONICAL_THESIS_TITLE_V3.md",
 "project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md",
 "project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md",
 "project/PHYSICS_MATHEMATICS_FIRST_HYPOTHESIS_TESTING_SCOPE_DIRECTIVE_V1.md")
def put_csv(path, columns, rows):
 path.parent.mkdir(parents=True,exist_ok=True)
 with path.open("w",newline="",encoding="utf-8") as f:
  writer=csv.DictWriter(f,fieldnames=columns,extrasaction="ignore")
  writer.writeheader();writer.writerows(rows)
def valid_utc(value):
 try:
  t=datetime.fromisoformat(value.replace("Z","+00:00"))
  return t.tzinfo is not None and t.utcoffset().total_seconds()==0
 except (ValueError,AttributeError,OverflowError):return False
def audit(path,name):
 result={"table":name,"sha256":"","row_count":0,"status":"MISSING","errors":""}
 if not path.is_file():return result,[]
 result["sha256"]=hashlib.sha256(path.read_bytes()).hexdigest()
 issues=[];rows=[];seen=set()
 try:
  with path.open(newline="",encoding="utf-8-sig") as f:
   rd=csv.DictReader(f);header=rd.fieldnames or []
   if not set(TABLES[name]).issubset(header):issues.append("missing_required_headers")
   if len(set(header))!=len(header):issues.append("duplicate_headers")
   for line,row in enumerate(rd,2):
    if line>2000002:issues.append("row_limit");break
    if None in row:issues.append("unexpected_columns");continue
    if not any(str(x or "").strip() for x in row.values()):continue
    rows.append(row)
    pk=KEYS.get(name,(TABLES[name][0],))
    key=tuple((row.get(c) or "").strip() for c in pk)
    if not all(key):issues.append("blank_primary_key_at_"+str(line))
    if key in seen:issues.append("duplicate_primary_key_at_"+str(line))
    seen.add(key)
    for col,value in row.items():
     if not value:continue
     if col.endswith("_utc") and not valid_utc(value):issues.append("invalid_utc_at_"+str(line))
     if col in NUMERIC:
      try:
       number=float(value)
       if not math.isfinite(number) or (col in {"required_kwh","delivered_kwh","p_requested_kw"} and number<0):raise ValueError()
      except ValueError:issues.append("invalid_number_at_"+str(line))
 except (OSError,UnicodeError,csv.Error) as ex:issues.append(type(ex).__name__)
 result.update(row_count=len(rows),status=("SCHEMA_FAIL" if issues else "SCHEMA_PASS" if rows else "EMPTY"),
  errors=";".join(issues[:25]))
 return result,rows
def linked_pairs(data):
 assets={r["asset_id"]:r for r in data["equipment_assets"] if r.get("asset_id")}
 graph=defaultdict(lambda:defaultdict(set))
 for c in data["physical_connections"]:
  s,t,site=c.get("source_asset"),c.get("target_asset"),c.get("installation_id")
  if c.get("connection_type")=="electrical_ac" and s in assets and t in assets and site:
   if assets[s].get("installation_id")==site==assets[t].get("installation_id"):graph[site][s].add(t)
 ttimes=defaultdict(set);etimes=defaultdict(set)
 for name,destination,ctype in (("transformer_telemetry",ttimes,"distribution_transformer"),
                                 ("evse_telemetry",etimes,"dc_evse")):
  for r in data[name]:
   site,aid=r.get("installation_id"),r.get("asset_id")
   if aid in assets and assets[aid].get("installation_id")==site and assets[aid].get("component_type")==ctype:
    destination[(site,aid)].add(r["timestamp_utc"])
 out=[]
 for (site,src),stamps in sorted(ttimes.items()):
  seen={src};todo=[src]
  while todo:
   for tgt in graph[site].get(todo.pop(),set())-seen:seen.add(tgt);todo.append(tgt)
  for (site2,tgt),other in sorted(etimes.items()):
   common=stamps & other
   if site==site2 and tgt in seen and common:
    out.append({"installation_id":site,"transformer_asset":src,"evse_asset":tgt,
                "aligned_timestamps":len(common),"status":"CANDIDATE_ONLY_NOT_VALIDATION"})
 return out
def ac_accounting(data,pairs):
 """Observed AC residual; never treat it as losses or verified conservation."""
 transformers={(r["installation_id"],r["asset_id"],r["timestamp_utc"]):r
               for r in data["transformer_telemetry"]}
 evse={(r["installation_id"],r["asset_id"],r["timestamp_utc"]):r
       for r in data["evse_telemetry"]}
 grouped=defaultdict(set)
 for pair in pairs:
  key=(pair["installation_id"],pair["transformer_asset"])
  grouped[key].add(pair["evse_asset"])
 results=[]
 for (site,transformer),evse_ids in sorted(grouped.items()):
  for (s,a,time),record in transformers.items():
   if (s,a)!=(site,transformer):continue
   try:
    total=float(record["p_total_kw"]);other=float(record["p_non_ev_kw"])
    matched=[evse[(site,c,time)] for c in evse_ids if (site,c,time) in evse]
    if len(matched)!=len(evse_ids):continue
    inputs=[float(r["p_ac_kw"]) for r in matched]
    if not all(math.isfinite(v) for v in [total,other,*inputs]):continue
   except (ValueError,TypeError,KeyError):continue
   sum_evse=sum(inputs)
   results.append({"installation_id":site,"transformer_asset":transformer,
      "timestamp_utc":time,"p_transformer_kw":total,"p_non_ev_kw":other,
      "sum_evse_ac_kw":sum_evse,"unresolved_balance_kw":total-other-sum_evse,
      "status":"BOUNDARY_LOSSES_AND_SENSOR_ERRORS_NOT_VALIDATED"})
 return results

def execute(repo,input_dir,out):
 out.mkdir(parents=True,exist_ok=True)
 readiness=[];data={}
 for name,columns in TABLES.items():
  put_csv(out/"templates"/(name+".csv"),columns,[])
  audit_result,observations=audit(input_dir/(name+".csv"),name)
  readiness.append(audit_result)
  data[name]=observations if audit_result["status"]=="SCHEMA_PASS" else []
 ids={r["evidence_id"] for r in data["source_evidence"] if r.get("evidence_id")}
 assets={r["asset_id"]:r for r in data["equipment_assets"] if r.get("asset_id")}
 problems=[]
 for table,rows in data.items():
  if table=="source_evidence":continue
  for i,row in enumerate(rows,2):
   if row.get("evidence_id") not in ids:problems.append({"table":table,"line":i,"error":"unverified_evidence_reference"})
   if table in {"evse_telemetry","transformer_telemetry","operator_events"}:
    aid=row.get("asset_id")
    if aid not in assets or assets[aid].get("installation_id")!=row.get("installation_id"):
     problems.append({"table":table,"line":i,"error":"unknown_or_wrong_installation_asset"})
 pairs=linked_pairs(data) if not problems else []
 residuals=ac_accounting(data,pairs) if not problems else []
 put_csv(out/"ac_power_accounting_residuals.csv",("installation_id","transformer_asset",
  "timestamp_utc","p_transformer_kw","p_non_ev_kw","sum_evse_ac_kw",
  "unresolved_balance_kw","status"),residuals)
 put_csv(out/"dataset_readiness.csv",("table","sha256","row_count","status","errors"),readiness)
 put_csv(out/"referential_integrity.csv",("table","line","error"),problems)
 put_csv(out/"linked_observation_candidates.csv",
  ("installation_id","transformer_asset","evse_asset","aligned_timestamps","status"),pairs)
 good={r["table"] for r in readiness if r["status"]=="SCHEMA_PASS"}
 status=[]
 for module,raw in MODULES.items():
  needed=set(raw.split());missing=sorted(needed-good)
  label="BLOCKED_EVIDENCE" if missing or problems else "DATA_PRESENT_NOT_SCIENTIFICALLY_VALIDATED"
  objective=("SO1" if module in {"R01","R02","R03","R04","R07","R08"} else
             "SO2" if module in {"R05","R06","R09","R11","R12"} else
             "SO3" if module in {"R10","R13"} else "SUPPORTING")
  status.append({"module":module,"objective":objective,"status":label,
                 "missing_data":",".join(missing),"physical_validation":"NOT_TESTED"})
 status.append({"module":"R16","objective":"OUT_OF_SCOPE","status":"OUT_OF_SCOPE_DEFERRED",
                "missing_data":"AI/ML excluded by current directive","physical_validation":"NOT_APPLICABLE"})
 put_csv(out/"research_status.csv",("module","objective","status","missing_data","physical_validation"),status)
 gates={f"G{i}":{"status":"NOT_TESTED","scope":"scientific gate, not automated software QA"} for i in range(9)}
 gates["G0"]["status"]="PASS" if all((repo/p).is_file() for p in GOVERNANCE) else "BLOCKED"
 gates["G0"]["scope"]="presence of canonical files only; no faculty approval"
 if problems or any(r["status"]=="SCHEMA_FAIL" for r in readiness):
  gates["G1"]["status"]="BLOCKED"
 (out/"gate_results.json").write_text(json.dumps(gates,indent=2),encoding="utf-8")
 summary={"run_type":"EVIDENCE_READINESS_NOT_PHYSICAL_VALIDATION",
  "generated_utc":datetime.now(timezone.utc).isoformat(),
  "total_tables":len(TABLES),"populated_schema_pass":len(good),
  "schema_fail":sum(r["status"]=="SCHEMA_FAIL" for r in readiness),
  "referential_errors":len(problems),"candidate_linked_pairs":len(pairs),
  "ac_balance_rows_unverified":len(residuals),
  "physical_validations":0,"source_sha256":{r["table"]:r["sha256"] for r in readiness if r["sha256"]}}
 (out/"research_manifest.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
 (out/"RESULTS_SUMMARY.md").write_text(
  "# Thermal thesis CSV evidence qualification\n\n"
  +f"Populated schema-qualified tables: {len(good)}/{len(TABLES)}.\n\n"
  +f"CSV errors: {summary['schema_fail']}; referential errors: {len(problems)}.\n\n"
  +f"Physically connected and time-aligned candidate pairs: {len(pairs)}.\n\n"
  +"Independent physical validation: NOT PERFORMED.\n\n"
  +"Schema checks do not establish causal directional thermal relationships or validated physics.\n",
  encoding="utf-8")
 return summary
def main():
 parser=argparse.ArgumentParser()
 parser.add_argument("--repo",type=Path,default=Path("."))
 parser.add_argument("--input-dir",type=Path,default=Path("research_data/thermal_inputs"))
 parser.add_argument("--output-dir",type=Path,default=Path("research_outputs/thermal_csv"))
 parser.add_argument("--strict-input",action="store_true")
 a=parser.parse_args()
 result=execute(a.repo,a.input_dir,a.output_dir)
 print(json.dumps(result,indent=2))
 if a.strict_input and (result["schema_fail"] or result["referential_errors"]):raise SystemExit(2)
if __name__=="__main__":main()
