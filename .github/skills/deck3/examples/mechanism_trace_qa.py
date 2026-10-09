#!/usr/bin/env python3
"""Structural QA for Deck3 figure mechanism sidecars. NOT scientific validation."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

SCHEMA = "deck3-mechanism-trace-v1"
KINDS = {"physical_system", "active_model", "simulation_environment",
         "experiment", "controller", "assessment", "external_environment", "workflow"}
TYPES = {"physical_flow", "state_influence", "constraint_effect", "control_signal",
         "observation", "data_for_identification", "model_calculation",
         "optimization_decision", "reporting", "sequence"}
STATUSES = {"OPEN", "CANDIDATE", "QUALIFIED", "ESTABLISHED", "THESIS_DEFINED"}
REVIEWS = {"OPEN", "PASS", "FAIL"}
DIRECTIONS = {"P_TO_TE", "TE_TO_P", "NONE"}

def verify(doc: dict) -> dict:
    """Validate internal consistency only; citations/physics must be checked separately."""
    errs = []
    def problem(s): errs.append(s)
    if not isinstance(doc, dict):
        return {"status": "BLOCKED", "errors": ["trace root must be an object"],
                "physics_validated": False}
    if doc.get("schema") != SCHEMA: problem("invalid or absent schema")
    for k in ("figure_id", "takeaway", "science_authority"):
        if not isinstance(doc.get(k), str) or not doc[k].strip():
            problem("missing "+k)
    if doc.get("evidence_status") not in STATUSES:
        problem("invalid figure evidence_status")
    for k in ("assumptions", "limitations"):
        if not isinstance(doc.get(k), list):
            problem(k+" must be a list (may be empty)")
    boundaries = doc.get("boundaries")
    objects = doc.get("objects")
    arrows = doc.get("arrows")
    if not isinstance(boundaries, list) or not boundaries:
        problem("boundaries must be nonempty list")
        boundaries = []
    if not isinstance(objects, list) or not objects:
        problem("objects must be nonempty list")
        objects = []
    if not isinstance(arrows, list):
        problem("arrows must be a list (may be empty for static taxonomy)")
        arrows = []
    bmap, omap = {}, {}
    for b in boundaries:
        if not isinstance(b, dict): problem("malformed boundary"); continue
        bid = b.get("id")
        if not isinstance(bid,str) or not bid.strip() or bid in bmap:
            problem("empty or duplicate boundary ID"); continue
        bmap[bid] = b
        if b.get("kind") not in KINDS: problem("unknown boundary kind: "+bid)
        if not isinstance(b.get("meaning"),str) or not b["meaning"].strip():
            problem("boundary lacks meaning: "+bid)
        if not isinstance(b.get("members"),list):
            problem("boundary members must be list: "+bid)
    for o in objects:
        if not isinstance(o, dict): problem("malformed object"); continue
        oid = o.get("id")
        if not isinstance(oid,str) or not oid.strip() or oid in omap:
            problem("empty or duplicate object ID"); continue
        omap[oid] = o
        if o.get("boundary") not in bmap:
            problem("object parent boundary absent: "+oid)
        if not isinstance(o.get("meaning"),str) or not o["meaning"].strip():
            problem("object meaning absent: "+oid)
        if not isinstance(o.get("kind"),str) or not o["kind"].strip():
            problem("object kind absent: "+oid)
        if o.get("evidence_status") not in STATUSES:
            problem("object evidence_status invalid: "+oid)
    for bid,b in bmap.items():
        for m in b.get("members",[]) if isinstance(b.get("members"),list) else []:
            if m not in omap or omap[m].get("boundary") != bid:
                problem("boundary member does not match object: "+bid+"/"+str(m))
    all_arrow_ids=set()
    for a in arrows:
        if not isinstance(a,dict): problem("malformed arrow"); continue
        aid = a.get("id")
        if not isinstance(aid,str) or not aid.strip() or aid in all_arrow_ids:
            problem("empty or duplicate arrow ID"); continue
        all_arrow_ids.add(aid)
        if a.get("from") not in omap or a.get("to") not in omap:
            problem("arrow endpoint missing: "+aid)
        if a.get("type") not in TYPES: problem("unknown arrow type: "+aid)
        for key in ("label","carried_quantity","interface","law_or_operator","evidence_gate"):
            if not isinstance(a.get(key),str) or not a[key].strip():
                problem("arrow "+aid+" missing "+key+" (use OPEN when unknown)")
        if a.get("direction") not in DIRECTIONS: problem("arrow direction invalid: "+aid)
        if a.get("evidence_status") not in STATUSES:
            problem("arrow evidence_status invalid: "+aid)
        if not isinstance(a.get("sources"), list):
            problem("arrow sources must be list: "+aid)
        elif a.get("evidence_status") in {"QUALIFIED","ESTABLISHED"}:
            if not any(isinstance(s,str) and s.strip() for s in a["sources"]):
                problem("qualified/established arrow has no source: "+aid)
            if str(a.get("evidence_gate", "")).upper() == "OPEN":
                problem("qualified/established arrow lacks qualification gate: "+aid)
        if a.get("direction") == "TE_TO_P" and a.get("type") in {
                "physical_flow","state_influence","constraint_effect"}:
            if "grid_side_ac" not in str(a.get("evidence_gate","")).lower():
                problem("TE_TO_P candidate lacks grid_side_ac evidence gate: "+aid)
        if a.get("direction") in {"P_TO_TE","TE_TO_P"} and a.get("type") == "sequence":
            problem("cross-system mechanism cannot be a mere sequence arrow: "+aid)
        if a.get("from") == a.get("to") and a.get("type") != "control_signal":
            problem("unqualified self-directed arrow: "+aid)
    r = doc.get("review")
    if not isinstance(r,dict):
        problem("missing review record")
    else:
        for key in ("physics","labels","figure","citations","animation"):
            if r.get(key) not in REVIEWS:
                problem("invalid or absent review."+key)
    # Record reviewer claims but never infer physical validation from them.
    return {
        "status": "STRUCTURAL_TRACE_PASS_NOT_PHYSICS_VERIFIED" if not errs else "BLOCKED",
        "errors": errs, "boundaries": len(bmap), "objects": len(omap),
        "arrows": len(all_arrow_ids), "physics_validated": False,
        "citation_content_verified": False,
        "powerpoint_playback_verified": False
    }

def check(path: str | Path) -> dict:
    path = Path(path)
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        return {"status":"BLOCKED","errors":["cannot read trace JSON: "+str(e)],
                "physics_validated":False}
    r = verify(doc)
    r["path"] = str(path)
    return r

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("trace_json", type=Path)
    args=ap.parse_args()
    result=check(args.trace_json)
    print(json.dumps(result,indent=2,ensure_ascii=False))
    raise SystemExit(result["status"]=="BLOCKED")

if __name__=="__main__":
    main()
