#!/usr/bin/env python3
"""Find public research datasets and safely acquire small original measurement CSVs.

Research target: measured Power--Electrified Transportation system interdependencies,
particularly transformer/EVSE/battery thermal dynamics, grid and charger load,
site electrical connectivity, state-time interactions and extreme-heat forcing.

Use: python fielddata_scraper.py --out fielddata_output
     python fielddata_scraper.py --download-small-csv --max-file-mb 5 \
       --max-api-calls 35 --out fielddata_output

Requires requests. No credentials, browser scraping, paywall bypass, or synthetic
measurement creation. ALL source discoveries are metadata candidates until
raw records and shared hardware topology are independently verified.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import html
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
from typing import Any

import requests

ZENODO = "https://zenodo.org/api/records"
DATACITE = "https://api.datacite.org/dois"
GITHUB = "https://api.github.com/search/repositories"
TIMEOUT = 12
USER_AGENT = "Physics-Infrastructure-Research/2.0 (metadata and public measurement acquisition)"

# Metadata-only seed list from publisher landing pages: the full OPSD series,
# EPFL spreadsheets and KU Leuven archive exceed the requested 5 MB CSV cap.
KNOWN = [
    dict(id="OPSD-household-2020", repo="OPSD", title="Household Data 2020-04-15 (CoSSMic)",
         doi="", landing="https://data.open-power-system-data.org/household_data/2020-04-15/",
         synopsis="Real household and small-business grid energy, EV charging energy and PV at some same premises; published intervals have interpolation or filled gaps.",
         evidence="P_T_ELECTRICAL_COLOCATED_MEASUREMENTS;NOT_TRANSFORMER_THERMAL", verified_same_transformer="NO"),
    dict(id="SINTEF-Zenodo-17223516", repo="Zenodo", title="40 MVA operating transformer temperatures, Norway 2024",
         doi="10.5281/zenodo.17223516", landing="https://zenodo.org/records/17223516",
         synopsis="Direct transformer sensor observations: current, voltage, ambient, winding/hotspot and oil temperature, no EVSE connectivity evidence.",
         evidence="MEASURED_TRANSFORMER_THERMAL;NO_CONNECTED_EVSE", verified_same_transformer="NO"),
    dict(id="EPFL-CCS", repo="GitHub", title="EPFL Level-3 charging station", doi="",
         landing="https://github.com/DESL-EPFL/Level-3-EV-charging-dataset",
         synopsis="Charging power, control and SOC measurements in XLSX files. No same-site transformer or EVSE internal temperature observed.",
         evidence="MEASURED_EVSE_ELECTRICAL;NO_THERMAL_COLOCATION", verified_same_transformer="NO"),
    dict(id="KU-Leuven-BEV", repo="KU Leuven", title="BEV Energy Dynamic Data V2",
         doi="10.48804/8KPDTW", landing="https://rdr.kuleuven.be/dataset.xhtml?persistentId=doi:10.48804/8KPDTW",
         synopsis="Measured battery temperatures and CAN charging records. No documented physical coupling to SINTEF or EPFL.",
         evidence="MEASURED_VEHICLE_THERMAL;NO_SAME_SITE_P_TO_TE", verified_same_transformer="NO"),
]

SOURCE_COLS = ["source_id","repository","title","doi","landing_url","publication_year", "resource_type",
               "metadata_excerpt","relevance_score","data_evidence_status","same_site_EV_grid_evidence",
               "transformer_thermal_measured","EVSE_internal_temp_measured","transformer_to_EVSE_topology_verified",
               "directional_thermal_causality_verified","scientific_role","discovery_method"]
FILE_COLS = ["source_id","repository","file_name","file_size_bytes","download_url","csv_candidate",
             "measurement_claim_from_metadata","license","download_eligible","eligibility_reason"]
DOWNLOAD_COLS = ["source_id","file_name","download_url","status","bytes","sha256","relative_path","detail"]
QUERY_COLS = ["service","query","http_status","records_found","api_calls_after","error"]

ZENODO_QUERIES = [
    'electric vehicle charging measurements power grid',
    'transformer temperature sensor dataset',
    'charging station electricity demand real world',
    'EV charging thermal field measurements',
]
DATACITE_QUERIES = [
    'electric vehicle charging transformer dataset',
    'electric vehicle charging station measurements',
    'transformer winding temperature monitoring dataset',
]
GITHUB_QUERIES = [
    'electric vehicle charging real-world data in:description,readme',
    'power transformer temperature dataset in:description,readme',
]


def clean(t: Any, maxlen=2000):
    if not t:
        return ""
    x = re.sub(r"<[^>]*>", " ", str(t))
    return re.sub(r"\s+", " ", html.unescape(x)).strip()[:maxlen]


def flatten_title(a):
    if isinstance(a, str): return a
    if isinstance(a, dict): return a.get("title") or a.get("name") or ""
    if isinstance(a, list): return " ".join(flatten_title(z) for z in a[:3])
    return ""


def relevance(text):
    txt = text.lower()
    terms = [
        (r"\b(transformer|distribution feeder|substation)\b", 3),
        (r"\b(charging station|evse|electric vehicle|bev|fast.charging)\b", 3),
        (r"\b(temperature|thermal|hot.spot|heatwave|heat wave)\b", 2),
        (r"\b(grid import|load profile|power|electricity demand|voltage|current)\b", 2),
        (r"\b(measured|measurement|monitoring|metered|real.world|observed|sensor)\b", 2),
        (r"\b(coupled|interdependen|co.located|same.site|connected)\b", 2),
    ]
    return sum(n for pat, n in terms if re.search(pat, txt))


def claim_measured(text):
    """A conservative metadata-level label, never proof of physical observation."""
    s = text.lower()
    if re.search(r"\b(synthetic|simulated|simulation data|generated dataset|numerical experiment)\b", s):
        return "UNRESOLVED_OR_SYNTHETIC"
    if re.search(r"\b(measured|measurement|metered|monitoring|real.world|observed|field data|sensor data|recorded)\b", s):
        return "CLAIMED_MEASURED_METADATA_ONLY"
    return "NOT_ESTABLISHED_METADATA_ONLY"


def role(s):
    s = s.lower()
    roles=[]
    if re.search("transformer|substation",s):roles.append("TRANSFORMER_COMPONENT")
    if re.search("charging|evse|electric vehicle|bev",s):roles.append("CHARGING_OR_VEHICLE")
    if re.search("temperature|thermal|hot.spot",s):roles.append("THERMAL")
    if re.search("grid|electricity|load|energy|power",s):roles.append("ELECTRICAL")
    return ";".join(roles) or "CONTEXT_ONLY"


class Budget:
    """Counts all HTTP requests, including downloads, redirects and failed attempts."""
    def __init__(self, max_calls, timeout):
        self.max_calls=max_calls
        self.used=0
        self.timeout=timeout
        self.offline_reason=""
        self.session=requests.Session()
        self.session.headers.update({"User-Agent":USER_AGENT,"Accept":"application/json"})

    def request(self, method, url, *, params=None, stream=False, redirect_host=None):
        if self.offline_reason:
            raise RuntimeError("Network unavailable: "+self.offline_reason)
        if self.used>=self.max_calls:
            raise RuntimeError("HTTP request budget exhausted")
        parsed=urlparse(url)
        if parsed.scheme != "https":
            raise ValueError("Only HTTPS is permitted")
        allowed = {"api.github.com","api.datacite.org","zenodo.org"}
        if parsed.hostname not in allowed:
            raise ValueError("Source host is not allowlisted")
        self.used+=1
        try:
            r=self.session.request(method,url,params=params,timeout=self.timeout,stream=stream,allow_redirects=False)
            if 300<=r.status_code<400:
                # Reject redirects to arbitrary download hosts or private networks.
                loc=r.headers.get("Location","")
                r.close()
                from urllib.parse import urljoin
                target=urljoin(url,loc)
                hp=urlparse(target).hostname or ""
                if hp!="zenodo.org" and not hp.endswith(".zenodo.org"):
                    raise ValueError("Untrusted redirect host: "+hp)
                return self.request(method,target,stream=stream)
            r.raise_for_status()
            return r
        except requests.exceptions.ConnectionError as exc:
            self.offline_reason="DNS/network connection failed"
            raise RuntimeError(self.offline_reason) from exc


def csvout(path,headers,rows):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("w",newline="",encoding="utf-8") as f:
        writer=csv.DictWriter(f,fieldnames=headers,extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def read_json(budget, url, params):
    r=budget.request("GET",url,params=params)
    try: return r.json(),r.status_code
    finally:r.close()


def zenodo_rows(rec):
    md=rec.get("metadata") or {}
    record_id=str(rec.get("id") or "")
    title=clean(md.get("title"))
    excerpt=clean(md.get("description"))
    s=title+" "+excerpt
    license_val="; ".join(str(v.get("id") or v.get("title") or "") for v in md.get("rights",[]) if isinstance(v,dict))
    srow={"source_id":"zenodo:"+record_id,"repository":"Zenodo","title":title,
          "doi":(rec.get("pids",{}).get("doi",{}) or {}).get("identifier") or "",
          "landing_url":(rec.get("links") or {}).get("self_html") or "https://zenodo.org/records/"+record_id,
          "publication_year":str(md.get("publication_date") or "")[:4],
          "resource_type":(md.get("resource_type") or {}).get("id",""),
          "metadata_excerpt":excerpt,"relevance_score":relevance(s),
          "data_evidence_status":claim_measured(s),"same_site_EV_grid_evidence":"NOT_VERIFIED",
          "transformer_thermal_measured":"NOT_VERIFIED", "EVSE_internal_temp_measured":"NOT_VERIFIED",
          "transformer_to_EVSE_topology_verified":"NOT_VERIFIED",
          "directional_thermal_causality_verified":"NOT_VERIFIED",
          "scientific_role":role(s),"discovery_method":"ZENODO_API_RECORD"}
    frows=[]
    # Zenodo API representations: files may be a dict with entries OR a list.
    file_field=rec.get("files") or {}
    if isinstance(file_field,dict):
        entries=file_field.get("entries") or {}
    elif isinstance(file_field,list):
        entries=file_field
    else:
        entries=[]
    if isinstance(entries,dict): files=list(entries.values())
    elif isinstance(entries,list): files=entries
    else:files=[]
    for f in files:
        if not isinstance(f,dict):continue
        name=f.get("key") or f.get("filename") or ""
        size=f.get("size")
        url=(f.get("links") or {}).get("content") or ""
        is_csv=name.lower().endswith(".csv")
        measured=claim_measured(s+" "+name)
        valid=is_csv and measured=="CLAIMED_MEASURED_METADATA_ONLY" and not re.search("calculated|synthetic|simulated|example",name,re.I)
        frows.append({"source_id":srow["source_id"],"repository":"Zenodo","file_name":name,
                      "file_size_bytes":size,"download_url":url,"csv_candidate":is_csv,
                      "measurement_claim_from_metadata":measured,"license":license_val,
                      "download_eligible":valid,"eligibility_reason":"CANDIDATE_ONLY_PENDING_ROW_QA" if valid else "NOT_AN_ORIGINAL_MEASUREMENT_CSV"})
    return srow,frows


def datacite_row(d):
    a=d.get("attributes") or {}
    ti=flatten_title(a.get("titles"))
    descriptions=a.get("descriptions") or []
    desc=clean(" ".join(x.get("description","") for x in descriptions if isinstance(x,dict)))
    s=ti+" "+desc
    return {"source_id":"doi:"+str(a.get("doi") or d.get("id") or ""),
            "repository":"DataCite","title":ti,"doi":a.get("doi") or d.get("id") or "",
            "landing_url":a.get("url") or "","publication_year":a.get("publicationYear") or "",
            "resource_type":(a.get("types") or {}).get("resourceTypeGeneral") or "",
            "metadata_excerpt":desc,"relevance_score":relevance(s),
            "data_evidence_status":claim_measured(s),"same_site_EV_grid_evidence":"NOT_VERIFIED",
            "transformer_thermal_measured":"NOT_VERIFIED","EVSE_internal_temp_measured":"NOT_VERIFIED",
            "transformer_to_EVSE_topology_verified":"NOT_VERIFIED",
            "directional_thermal_causality_verified":"NOT_VERIFIED",
            "scientific_role":role(s),"discovery_method":"DATACITE_METADATA_ONLY"}


def github_row(d):
    s=str(d.get("name") or "")+" "+str(d.get("description") or "")
    return {"source_id":"github:"+str(d.get("full_name") or ""),"repository":"GitHub",
            "title":d.get("full_name") or "","doi":"","landing_url":d.get("html_url") or "",
            "publication_year":"","resource_type":"software/repository",
            "metadata_excerpt":clean(d.get("description")),"relevance_score":relevance(s),
            "data_evidence_status":claim_measured(s),"same_site_EV_grid_evidence":"NOT_VERIFIED",
            "transformer_thermal_measured":"NOT_VERIFIED","EVSE_internal_temp_measured":"NOT_VERIFIED",
            "transformer_to_EVSE_topology_verified":"NOT_VERIFIED",
            "directional_thermal_causality_verified":"NOT_VERIFIED",
            "scientific_role":role(s),"discovery_method":"GITHUB_REPOSITORY_METADATA_ONLY"}


def safe_name(s):
    x=re.sub(r"[^A-Za-z0-9._-]+","_",str(s)).strip("._")
    return x[:110] or "file.csv"


def download_small(budget,f,root,max_bytes):
    out={k:f.get(k,"") for k in ("source_id","file_name","download_url")}
    out.update(status="SKIPPED",bytes="",sha256="",relative_path="",detail="")
    size=f.get("file_size_bytes")
    try: size=int(size)
    except (TypeError,ValueError):size=None
    if not f.get("download_eligible"):
        out["detail"]="Not supported as original measurement CSV from metadata"
        return out
    if size is None:
        out["detail"]="Source size unknown; refusing unbounded download"
        return out
    if size>max_bytes:
        out["detail"]="Published file size above user cap"
        return out
    if size<=0:
        out["detail"]="Source size invalid"
        return out
    url=f.get("download_url") or ""
    if urlparse(url).hostname!="zenodo.org":
        out["detail"]="Direct original file URL not verified on Zenodo"
        return out
    destdir=root/"original_small_csv"
    destdir.mkdir(parents=True,exist_ok=True)
    file_name=safe_name(f["source_id"])+"__"+safe_name(f["file_name"])
    if not file_name.lower().endswith(".csv"):file_name+=".csv"
    dest=destdir/file_name
    if dest.exists():
        out.update(status="EXISTS_UNMODIFIED",bytes=dest.stat().st_size,
                   sha256=hashlib.sha256(dest.read_bytes()).hexdigest(),relative_path=str(dest.relative_to(root)),
                   detail="Existing file was not overwritten; independent provenance check recommended")
        return out
    part=dest.with_suffix(".csv.part")
    n=0;dig=hashlib.sha256()
    try:
        response=budget.request("GET",url,stream=True)
        try:
            content_length=response.headers.get("Content-Length")
            if content_length and int(content_length)>max_bytes:
                out.update(status="SKIPPED_SIZE",detail="HTTP Content-Length above cap")
                return out
            ct=response.headers.get("Content-Type","").lower()
            if "text/html" in ct:
                out.update(status="SKIPPED_CONTENT_TYPE",detail="HTML is not original CSV")
                return out
            with part.open("wb") as fh:
                for chunk in response.iter_content(chunk_size=65536):
                    if not chunk:continue
                    n+=len(chunk)
                    if n>max_bytes:
                        out.update(status="SKIPPED_SIZE",detail="Stream exceeded 5 MB cap; partial file deleted")
                        return out
                    dig.update(chunk);fh.write(chunk)
        finally:response.close()
        if n<10:
            out.update(status="SKIPPED_CONTENT",detail="Insufficient bytes")
            return out
        # Reject HTML and binary accidentally served with misleading content type.
        with part.open("rb") as fh: head=fh.read(2048)
        if b"\x00" in head or b"<html" in head.lower() or b"<!doctype html" in head.lower():
            out.update(status="SKIPPED_CONTENT",detail="File is not plaintext CSV")
            return out
        with part.open("rb") as fh:
            h=fh.readline(65536)
        if b"," not in h and b";" not in h and b"\t" not in h:
            out.update(status="SKIPPED_CONTENT",detail="No delimited CSV header detected")
            return out
        part.replace(dest)
        out.update(status="DOWNLOADED_UNQUALIFIED_MEASUREMENT_CANDIDATE",bytes=n,sha256=dig.hexdigest(),
                   relative_path=str(dest.relative_to(root)),detail="Source data acquired; sensor/field/topology semantics still require audit")
        return out
    except Exception as exc:
        out.update(status="ERROR",detail=(type(exc).__name__+": "+str(exc))[:250])
        return out
    finally:part.unlink(missing_ok=True)


def known_csv_file_metadata():
    return [
        {"source_id":"zenodo:17223516","repository":"Zenodo","file_name":"Barug2025_sensordata.csv",
         "file_size_bytes":873041,"download_url":"https://zenodo.org/api/records/17223516/files/Barug2025_sensordata.csv/content",
         "csv_candidate":True,"measurement_claim_from_metadata":"CLAIMED_MEASURED_METADATA_ONLY",
         "license":"CC BY 4.0","download_eligible":True,"eligibility_reason":"KNOWN_VERIFIED_PUBLIC_SOURCE_FILE_METADATA"},
        {"source_id":"zenodo:17223516","repository":"Zenodo","file_name":"Barug2025_calculated.csv",
         "file_size_bytes":480949,"download_url":"https://zenodo.org/api/records/17223516/files/Barug2025_calculated.csv/content",
         "csv_candidate":True,"measurement_claim_from_metadata":"AUTHOR_CALCULATED_NOT_MEASURED",
         "license":"CC BY 4.0","download_eligible":False,"eligibility_reason":"DERIVED_MODEL_OUTPUT_EXCLUDED"},
        {"source_id":"OPSD-household-2020","repository":"OPSD","file_name":"household_data_15min_singleindex.csv",
         "file_size_bytes":58*1024*1024,"download_url":"https://data.open-power-system-data.org/household_data/2020-04-15/household_data_15min_singleindex.csv",
         "csv_candidate":True,"measurement_claim_from_metadata":"PROCESSED_INTERPOLATED_MEASUREMENTS",
         "license":"CC BY 4.0","download_eligible":False,"eligibility_reason":"ABOVE_5_MB_CAP;SOME_INTERPOLATION"},
    ]


def run(args):
    out=Path(args.out).expanduser().resolve()
    out.mkdir(parents=True,exist_ok=True)
    budget=Budget(args.max_api_calls,args.timeout)
    sources=[];files=known_csv_file_metadata();queries=[]
    for k in KNOWN:
        sources.append({"source_id":k["id"],"repository":k["repo"],"title":k["title"],
            "doi":k["doi"],"landing_url":k["landing"],"publication_year":"",
            "resource_type":"published study/dataset","metadata_excerpt":k["synopsis"],
            "relevance_score":relevance(k["title"]+" "+k["synopsis"]),
            "data_evidence_status":"KNOWN_SOURCE_DESCRIPTION_NOT_CROSS_SYSTEM_VALIDATION",
            "same_site_EV_grid_evidence":"PUBLISHED_SAME_PREMISES_METERS" if k["repo"]=="OPSD" else "NOT_VERIFIED",
            "transformer_thermal_measured":"PUBLISHED_SINTEF_MEASUREMENT" if k["id"].startswith("SINTEF") else "NOT_VERIFIED",
            "EVSE_internal_temp_measured":"NOT_VERIFIED",
            "transformer_to_EVSE_topology_verified":"NOT_VERIFIED",
            "directional_thermal_causality_verified":"NOT_VERIFIED",
            "scientific_role":role(k["title"]+" "+k["synopsis"]),
            "discovery_method":"PREVERIFIED_PUBLICATION_LANDING_PAGE_NOT_LIVE_QUERY"})
    tasks=[("Zenodo",ZENODO,q,{"q":q,"size":args.per_query}) for q in ZENODO_QUERIES]
    tasks += [("DataCite",DATACITE,q,{"query":q,"page[size]":args.per_query}) for q in DATACITE_QUERIES]
    tasks += [("GitHub",GITHUB,q,{"q":q,"per_page":args.per_query}) for q in GITHUB_QUERIES]
    # Fetch specific, already-known measured source using the official API.
    tasks.insert(0,("Zenodo",ZENODO+"/17223516","KNOWN_SINTEF_RECORD",{}))
    seen={x["source_id"] for x in sources}
    for service,url,query,params in tasks:
        log={"service":service,"query":query,"http_status":"","records_found":0,"api_calls_after":budget.used,"error":""}
        if args.offline:
            log.update(http_status="OFFLINE",error="Explicit --offline: no API requests")
        elif budget.offline_reason:
            log.update(http_status="UNAVAILABLE",error=budget.offline_reason)
        elif budget.used>=budget.max_calls:
            log.update(http_status="BUDGET_EXHAUSTED",error="Max HTTP calls already reached")
        else:
            try:
                data,status=read_json(budget,url,params)
                log["http_status"]=status
                if service=="Zenodo":
                    records=[data] if query=="KNOWN_SINTEF_RECORD" else (data.get("hits") or {}).get("hits") or []
                else:
                    records=data.get("data",[]) if service=="DataCite" else data.get("items",[])
                log["records_found"]=len(records)
                for rec in records:
                    if service=="Zenodo":sr,fr=zenodo_rows(rec);files.extend(fr)
                    elif service=="DataCite":sr=datacite_row(rec)
                    else:sr=github_row(rec)
                    if sr["source_id"] not in seen:
                        sources.append(sr);seen.add(sr["source_id"])
            except Exception as exc:
                log.update(http_status="ERROR",error=(type(exc).__name__+": "+str(exc))[:250])
        log["api_calls_after"]=budget.used
        queries.append(log)
        if args.sleep and not args.offline and not budget.offline_reason:time.sleep(args.sleep)
    # Deduplicate exact Zenodo candidate file keys; preserve source-provenance.
    keyed={}
    for f in files:
        k=(f["source_id"],f["file_name"])
        if k not in keyed or f.get("eligibility_reason")=="KNOWN_VERIFIED_PUBLIC_SOURCE_FILE_METADATA":keyed[k]=f
    files=list(keyed.values())
    max_bytes=int(args.max_file_mb*1_000_000)
    downloads=[]
    if args.download_small_csv:
        for f in files:
            if not f.get("csv_candidate"):continue
            # all download attempts will be logged; no inaccurate success claims.
            if args.offline or budget.offline_reason:
                status="OFFLINE" if args.offline else "NETWORK_UNAVAILABLE"
                downloads.append({"source_id":f["source_id"],"file_name":f["file_name"],
                     "download_url":f["download_url"],"status":status,"bytes":"","sha256":"",
                     "relative_path":"","detail":"Acquisition unavailable; not downloaded"})
                continue
            downloads.append(download_small(budget,f,out,max_bytes))
    csvout(out/"repository_evidence_register.csv",SOURCE_COLS,sources)
    csvout(out/"public_original_csv_candidates.csv",FILE_COLS,files)
    csvout(out/"repository_search_log.csv",QUERY_COLS,queries)
    csvout(out/"download_log.csv",DOWNLOAD_COLS,downloads)
    gates=[
        {"objective":"SO1","claim":"Measured thermal physics of constituent systems", "status":"PARTIAL_COMPONENT_ONLY", "reason":"Separate vehicle, transformer and EVSE measurements; no verified connected site"},
        {"objective":"SO2","claim":"Directional P-to-Te and Te-to-P thermal propagation", "status":"BLOCKED", "reason":"Synchronized same-site transformer + EVSE temperatures and documented feeder wiring unavailable"},
        {"objective":"SO2","claim":"Premises EV charging electricity vs grid imports", "status":"AVAILABLE_AS_CONTEXT_ONLY", "reason":"OPSD same-site premise metering but published file exceeds 5 MB and is partly interpolated"},
        {"objective":"SO3","claim":"Mobility and electric-service consequences", "status":"PARTIAL_SERVICE_PROXIES", "reason":"Charging sessions available; mobility requirements and verified coupled failures missing"},
        {"objective":"EVIDENCE","claim":"No invented integrated field dataset", "status":"ENFORCED", "reason":"No cross-installation synchronization or unsupported cause/effect claims"},
    ]
    csvout(out/"thesis_SO1_SO3_gates.csv",["objective","claim","status","reason"],gates)
    manifest={"timestamp_UTC":datetime.now(timezone.utc).isoformat(),"api_call_budget":args.max_api_calls,
        "http_calls_used":budget.used,"network_status":budget.offline_reason or ("explicitly_offline" if args.offline else "connected_or_no_error"),
        "sources_including_static_known":len(sources),"candidate_csv_and_files":len(files),
        "successful_new_original_csv_downloads":sum(x["status"].startswith("DOWNLOADED") for x in downloads),
        "download_file_cap_bytes":max_bytes,"download_flag":args.download_small_csv,
        "scientific_scope":"METADATA DISCOVERY AND COMPONENT-LEVEL ACQUISITION; NO SAME-SITE THERMAL FIELD PROOF",
        "out_dir":str(out),"files_written":["repository_evidence_register.csv","public_original_csv_candidates.csv","repository_search_log.csv","download_log.csv","thesis_SO1_SO3_gates.csv","run_manifest.json"]}
    (out/"run_manifest.json").write_text(json.dumps(manifest,indent=2),encoding="utf-8")
    print(json.dumps(manifest,indent=2))
    return manifest


def selftest():
    sample={"id":17223516,"metadata":{"title":"Measured power transformer thermal monitoring","description":"sensor measurements 2024","rights":[{"id":"cc-by-4.0"}]},
            "files":{"entries":{"test.csv":{"key":"test.csv","size":100,"links":{"content":"https://zenodo.org/files/test.csv"}},
                                "calculated.csv":{"key":"calculated.csv","size":200,"links":{"content":"https://zenodo.org/files/calculated.csv"}}}}}
    sr,fs=zenodo_rows(sample)
    assert sr["transformer_to_EVSE_topology_verified"]=="NOT_VERIFIED"
    assert fs[0]["download_eligible"] is True
    assert fs[1]["download_eligible"] is False
    # Regression: Zenodo API search responses sometimes use a file list.
    sample["files"] = list(sample["files"]["entries"].values())
    _, fs_alt = zenodo_rows(sample)
    assert len(fs_alt)==2 and fs_alt[0]["file_name"]=="test.csv"
    assert claim_measured("simulated synthetic dataset")!="CLAIMED_MEASURED_METADATA_ONLY"
    assert relevance("EV charging thermal power transformer measured")>3
    print("SELFTEST PASS: provenance, metadata-only claims, exclusions, scoring")


def main():
    p=argparse.ArgumentParser(description=__doc__,formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument("--out",default="fielddata_output",help="Output directory for evidence CSVs")
    p.add_argument("--download-small-csv",action="store_true",help="Attempt direct public original measurement CSV downloads")
    p.add_argument("--max-file-mb",type=float,default=5,help="Hard maximum download size per file (decimal MB)")
    p.add_argument("--max-api-calls",type=int,default=35,help="Maximum combined HTTP calls, including downloads/redirects/failures")
    p.add_argument("--per-query",type=int,default=8,help="Max search hits requested per repository query")
    p.add_argument("--timeout",type=int,default=12,help="HTTP request timeout seconds")
    p.add_argument("--sleep",type=float,default=0.0,help="Seconds between search requests")
    p.add_argument("--offline",action="store_true",help="Generate known-source CSV registers without HTTP requests")
    p.add_argument("--self-test",action="store_true",help="Run built-in deterministic parser checks")
    args=p.parse_args()
    if args.self_test:return selftest()
    if args.max_file_mb<=0 or args.max_api_calls<1 or args.per_query<1 or args.timeout<1:
        p.error("--max-file-mb, --max-api-calls, --per-query, --timeout must be positive")
    run(args)


if __name__=="__main__":main()
