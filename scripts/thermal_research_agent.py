#!/usr/bin/env python3
"""Fail-closed research task routing and claim admission. No AI services invoked.

This module is an executable *policy router*, not an autonomous LLM implementation
or evidence of validation. Input/output is JSON; no network or secrets accessed.
"""
import argparse
import json
from pathlib import Path

ROLES = {
    "authority": "A0", "literature": "A1", "physics": "A2",
    "mathematics": "A3", "critique": "A4", "verification": "A5",
    "evidence": "A6", "deck3": "A7", "release": "A8",
}
INTERFACES = {"I1", "I2", "I3", "I4", "I5", "I6"}
COMPONENTS = {"P1","P2","P3","P4","T1","T2","T3","T4"}
OBJECTIVES = {"SO1","SO2","SO3"}
GATES = [f"G{i}" for i in range(9)]
RESULTS = {"PASS","FAIL","BLOCKED","NOT_TESTED","NOT_APPLICABLE"}
EVIDENCE = {"L","S","E","V"}
CLAIM_STATES = {"PROPOSED","LITERATURE_SUPPORTED","EQUIPMENT_ELIGIBLE","VALIDATED_IN_DOMAIN","REJECTED","UNRESOLVED"}
RESTRICTED = {"canonical_change","scientific_claim_promotion","merge","external_release","asu_submission"}

def validate_task(task):
    if not isinstance(task, dict):
        raise ValueError("task must be JSON object")
    for key in ("task_id","role","objective","components","interfaces","action"):
        if key not in task: raise ValueError(f"missing {key}")
    if task["role"] not in ROLES: raise ValueError("unknown role")
    if task["objective"] not in OBJECTIVES: raise ValueError("unknown objective")
    if not isinstance(task["components"],list) or not set(task["components"]).issubset(COMPONENTS):
        raise ValueError("invalid components")
    if not isinstance(task["interfaces"],list) or not set(task["interfaces"]).issubset(INTERFACES):
        raise ValueError("invalid interfaces")
    if task["action"] in RESTRICTED:
        return {"task_id":task["task_id"],"agent":ROLES[task["role"]],
                "decision":"BLOCKED_HUMAN_DECISION","reason":"restricted release or authority action"}
    return {"task_id":task["task_id"],"agent":ROLES[task["role"]],
            "decision":"ELIGIBLE_FOR_RESEARCH_ASSISTANCE",
            "reason":"scope and role accepted; no scientific gate implied"}

def validate_claim(claim):
    if not isinstance(claim,dict): raise ValueError("claim must be JSON object")
    required=("claim_id","authority","objective","components","interfaces","mechanism",
              "equations","assumptions","sources","tests","uncertainty",
              "validity_domain","evidence_levels","gate_results","status")
    for key in required:
        if key not in claim: raise ValueError(f"missing claim field {key}")
    if claim["objective"] not in OBJECTIVES: raise ValueError("unknown objective")
    if not set(claim["components"]).issubset(COMPONENTS): raise ValueError("component outside frozen roster")
    if not set(claim["interfaces"]).issubset(INTERFACES): raise ValueError("unrecognized interface")
    if not set(claim["evidence_levels"]).issubset(EVIDENCE): raise ValueError("unknown evidence level")
    if set(claim["gate_results"]) != set(GATES): raise ValueError("all G0-G8 gate verdicts required")
    if any(v not in RESULTS for v in claim["gate_results"].values()): raise ValueError("invalid gate result")
    if claim["status"] not in CLAIM_STATES: raise ValueError("unknown status")
    if claim["status"]=="VALIDATED_IN_DOMAIN":
        if "V" not in claim["evidence_levels"] or claim["gate_results"]["G6"]!="PASS":
            raise ValueError("validation claim requires V evidence and G6 PASS")
        if not claim["sources"] or not claim["tests"] or not claim["validity_domain"]:
            raise ValueError("validated claim lacks independent evidence, tests or domain")
    return {"claim_id":claim["claim_id"],"decision":"SCHEMA_ACCEPTED_NOT_SCIENTIFICALLY_VERIFIED"}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("mode", choices=("task","claim"))
    parser.add_argument("input",type=Path)
    args=parser.parse_args()
    payload=json.loads(args.input.read_text())
    print(json.dumps(validate_task(payload) if args.mode=="task" else validate_claim(payload),indent=2))

if __name__=="__main__": main()
