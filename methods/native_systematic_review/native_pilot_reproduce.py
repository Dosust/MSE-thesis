#!/usr/bin/env python3
"""
Native PRISMA pilot utility for MSE-thesis external database exports.

Standard-library only. No pandas/openpyxl.

Functions:
- audit raw CSV and SHA-256
- canonical DOI/title-year keys
- exact duplicate diagnostics
- deterministic development/validation samples
- Wilson 95% intervals from screened decision files
- prospective DOI anchor recovery
- exact-key overlap/Jaccard with comparison CSVs

This script does NOT replace human/scientific eligibility screening.
"""

from __future__ import annotations
import argparse, csv, hashlib, json, math, re, sys, unicodedata
from pathlib import Path
from typing import Dict, List, Tuple, Iterable, Set

csv.field_size_limit(sys.maxsize)

DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.I)

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def norm_text(s: str) -> str:
    s = unicodedata.normalize("NFKC", s or "")
    s = s.lower().strip()
    s = re.sub(r"\s+", " ", s)
    return s

def norm_title(s: str) -> str:
    s = norm_text(s)
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()

def norm_doi(s: str) -> str:
    s = (s or "").strip().lower()
    m = DOI_RE.search(s)
    return m.group(0).rstrip(".,;)") if m else ""

def find_field(headers: List[str], candidates: Iterable[str]) -> str:
    lookup = {h.lower().strip(): h for h in headers}
    for c in candidates:
        if c.lower() in lookup:
            return lookup[c.lower()]
    return ""

def load_csv(path: Path) -> Tuple[List[str], List[Dict[str,str]]]:
    with path.open("r", newline="", encoding="utf-8-sig") as f:
        r = csv.DictReader(f)
        if not r.fieldnames:
            raise ValueError("CSV has no header row.")
        return r.fieldnames, list(r)

def resolve_fields(headers: List[str]) -> Dict[str,str]:
    return {
        "title": find_field(headers, ["Title", "Document Title"]),
        "doi": find_field(headers, ["DOI"]),
        "year": find_field(headers, ["Publication year", "Publication Year", "Year"]),
        "id": find_field(headers, ["Accession number", "Accession Number", "EID", "Document Identifier"]),
        "abstract": find_field(headers, ["Abstract"]),
        "doctype": find_field(headers, ["Document type", "Document Type"]),
        "source": find_field(headers, ["Source", "Source title", "Publication Title"]),
        "authors": find_field(headers, ["Author", "Authors"]),
    }

def record_key(row: Dict[str,str], fm: Dict[str,str]) -> str:
    doi = norm_doi(row.get(fm["doi"], "")) if fm["doi"] else ""
    if doi:
        return "doi:" + doi
    title = norm_title(row.get(fm["title"], "")) if fm["title"] else ""
    year = (row.get(fm["year"], "") or "").strip() if fm["year"] else ""
    return f"titleyear:{title}|{year}"

def deterministic_rank(seed: str, phase: str, run_id: str, key: str) -> str:
    return hashlib.sha256(f"{seed}|{phase}|{run_id}|{key}".encode("utf-8")).hexdigest()

def wilson(k: int, n: int, z: float = 1.959963984540054) -> Tuple[float,float]:
    if n <= 0:
        return (float("nan"), float("nan"))
    p = k/n
    den = 1 + z*z/n
    center = (p + z*z/(2*n))/den
    half = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))/den
    return center-half, center+half

def prepare(args):
    raw = Path(args.raw)
    headers, rows = load_csv(raw)
    fm = resolve_fields(headers)
    for req in ("title","year"):
        if not fm[req]:
            raise ValueError(f"Required field not found: {req}")

    keyed = []
    for i,row in enumerate(rows, start=1):
        key = record_key(row,fm)
        keyed.append((i,key,row))

    counts = {}
    for _,k,_ in keyed:
        counts[k] = counts.get(k,0)+1
    dup_keys = sorted([k for k,v in counts.items() if v>1])

    years=[]
    outside=[]
    for i,_,row in keyed:
        try:
            y=int((row.get(fm["year"],"") or "").strip())
            years.append(y)
            if args.year_min is not None and y < args.year_min: outside.append(i)
            if args.year_max is not None and y > args.year_max: outside.append(i)
        except Exception:
            pass

    n = min(args.n, len(keyed))
    dev_sorted = sorted(keyed, key=lambda t: deterministic_rank(args.seed,"development",args.run_id,t[1]))
    dev = dev_sorted[:n]
    dev_keys={k for _,k,_ in dev}
    remaining=[x for x in keyed if x[1] not in dev_keys]
    val_n=min(args.n,len(remaining))
    val=sorted(remaining,key=lambda t: deterministic_rank(args.seed,"validation",args.run_id,t[1]))[:val_n]

    outdir=Path(args.outdir); outdir.mkdir(parents=True,exist_ok=True)

    sample_headers=["Sample_ID","Raw_Index","Record_Key"]+headers
    for phase,sample in [("development",dev),("validation",val)]:
        out=outdir/f"{args.run_id}_{phase}_sample.csv"
        with out.open("w",newline="",encoding="utf-8") as f:
            w=csv.DictWriter(f,fieldnames=sample_headers)
            w.writeheader()
            for j,(idx,key,row) in enumerate(sample,start=1):
                rec={"Sample_ID":j,"Raw_Index":idx,"Record_Key":key}
                rec.update(row); w.writerow(rec)

    anchors=[]
    if args.anchors:
        wanted=[norm_doi(x) for x in args.anchors.split(",") if norm_doi(x)]
        doi_set={norm_doi(row.get(fm["doi"],"")) for _,_,row in keyed} if fm["doi"] else set()
        anchors=[{"doi":d,"retrieved":d in doi_set} for d in wanted]

    audit={
        "run_id":args.run_id,
        "raw_file":raw.name,
        "sha256":sha256_file(raw),
        "rows":len(rows),
        "fields":len(headers),
        "resolved_fields":fm,
        "canonical_unique":len(set(k for _,k,_ in keyed)),
        "duplicate_key_count":len(dup_keys),
        "year_min_observed":min(years) if years else None,
        "year_max_observed":max(years) if years else None,
        "outside_year_rule_count":len(set(outside)),
        "development_n":len(dev),
        "validation_n":len(val),
        "seed":args.seed,
        "anchors":anchors,
    }
    (outdir/f"{args.run_id}_audit.json").write_text(json.dumps(audit,indent=2),encoding="utf-8")
    print(json.dumps(audit,indent=2))

def analyze(args):
    path=Path(args.screened)
    headers,rows=load_csv(path)
    if "Decision" not in headers:
        raise ValueError("Screened file must contain a Decision column.")
    screened=[r for r in rows if norm_text(r.get("Decision","")) in ("include","exclude")]
    inc=sum(1 for r in screened if norm_text(r.get("Decision",""))=="include")
    lo,hi=wilson(inc,len(screened))
    print(json.dumps({
        "screened":len(screened),
        "included":inc,
        "precision":inc/len(screened) if screened else None,
        "wilson95":[lo,hi],
    },indent=2))

def keyset(path: Path) -> Set[str]:
    headers,rows=load_csv(path); fm=resolve_fields(headers)
    return {record_key(r,fm) for r in rows}

def compare(args):
    a=keyset(Path(args.a)); b=keyset(Path(args.b))
    inter=len(a&b); union=len(a|b)
    print(json.dumps({
        "A_unique":len(a),"B_unique":len(b),
        "overlap":inter,"union":union,
        "jaccard":inter/union if union else None,
        "A_only":len(a-b),"B_only":len(b-a)
    },indent=2))

def main():
    ap=argparse.ArgumentParser()
    sp=ap.add_subparsers(dest="cmd",required=True)

    p=sp.add_parser("prepare")
    p.add_argument("--raw",required=True)
    p.add_argument("--run-id",required=True)
    p.add_argument("--outdir",required=True)
    p.add_argument("--seed",default="20260907")
    p.add_argument("-n",type=int,default=30)
    p.add_argument("--year-min",type=int)
    p.add_argument("--year-max",type=int)
    p.add_argument("--anchors",default="")
    p.set_defaults(func=prepare)

    a=sp.add_parser("analyze")
    a.add_argument("--screened",required=True)
    a.set_defaults(func=analyze)

    c=sp.add_parser("compare")
    c.add_argument("--a",required=True)
    c.add_argument("--b",required=True)
    c.set_defaults(func=compare)

    args=ap.parse_args(); args.func(args)

if __name__=="__main__":
    main()
