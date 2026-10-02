#!/usr/bin/env python3
"""
High-rigor literature screening pipeline for:
Physics-Based Mathematical Engineering of Power–Transportation
Interdependencies for Resilience.

Scientific logic:
FRAMEWORK -> METHOD -> FINDINGS -> LIMITATIONS -> SYNTHESIS -> CONTRIBUTION

Important:
- This script performs title/abstract pre-screening and prioritization.
- It does NOT infer full-text findings from titles.
- It keeps author-stated limitations separate from reviewer-inferred limitations.
- A final 26-paper core must receive manual/full-text verification.
"""

from __future__ import annotations
import argparse, csv, hashlib, json, re, sys, time
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen

SEARCH_FAMILIES = [
    "coupled power transportation network electric vehicle charging interdependency",
    "traffic electric power coupled system resilience",
    "dynamic coupled transportation power EV charging behavior",
    "power transportation resilience recovery electric vehicle",
    "fast charging station queue power transportation network",
    "distribution transformer EV charging hottest spot thermal aging",
    "extreme heat electric vehicle energy consumption charging demand",
    "fast EV charger thermal derating extreme heat",
    "smart charging transformer thermal constraint EV",
    "vehicle to grid coupled power transportation resilience",
    "dynamic traffic assignment coupled power distribution network",
    "state dependent interdependency infrastructure resilience power transportation",
]

WEIGHTS = {
    "rq_fit": 20,
    "physics": 20,
    "coupling": 15,
    "state_time": 15,
    "service_resilience": 10,
    "math_method": 10,
    "validation": 5,
    "intervention": 5,
}

TERM_FAMILIES = {
    "power": [r"\bpower\b", r"distribution network", r"\bgrid\b", r"transformer", r"feeder", r"voltage", r"optimal power flow"],
    "transport": [r"transport", r"traffic", r"mobility", r"route", r"road network", r"vehicle"],
    "ev_interface": [r"electric vehicle", r"\bEV\b", r"charging station", r"fast charging", r"charger", r"vehicle-to-grid", r"\bV2G\b"],
    "physics": [r"thermal", r"temperature", r"heat", r"hottest[- ]spot", r"state of charge", r"\bSOC\b", r"power flow", r"energy consumption", r"queue"],
    "dynamic": [r"dynamic", r"time[- ]vary", r"temporal", r"spatiotemporal", r"trajectory", r"state[- ]dependent", r"multi[- ]period", r"real[- ]time"],
    "resilience": [r"resilien", r"recovery", r"restoration", r"service disruption", r"cascad", r"hazard", r"failure"],
    "intervention": [r"control", r"optim", r"dispatch", r"schedul", r"routing", r"pricing", r"reinforcement learning", r"model predictive"],
    "validation": [r"case study", r"real[- ]world", r"field", r"experiment", r"validated", r"benchmark", r"sensitivity analysis", r"IEEE \d+"],
}

def norm(s):
    return re.sub(r"\s+", " ", (s or "").strip()).lower()

def has_any(text, patterns):
    return any(re.search(p, text, flags=re.I) for p in patterns)

def dedupe(records):
    seen_doi, seen_title, out = set(), set(), []
    for r in records:
        doi = norm(r.get("doi"))
        title = re.sub(r"[^a-z0-9]+", " ", norm(r.get("title")))
        key_title = " ".join(title.split())
        if doi and doi in seen_doi:
            continue
        if key_title and key_title in seen_title:
            continue
        if doi: seen_doi.add(doi)
        if key_title: seen_title.add(key_title)
        out.append(r)
    return out

def gate(record):
    """Hard relevance gate. Keeps either direct CPTS papers or required physics-module papers."""
    text = norm(" ".join([record.get("title",""), record.get("abstract",""), record.get("keywords","")]))
    p = has_any(text, TERM_FAMILIES["power"])
    t = has_any(text, TERM_FAMILIES["transport"])
    ev = has_any(text, TERM_FAMILIES["ev_interface"])
    phys = has_any(text, TERM_FAMILIES["physics"])
    direct_cpts = p and t and ev
    physics_module = ev and phys and (p or t)
    return direct_cpts or physics_module

def grade_0_4(text, family):
    pats = TERM_FAMILIES[family]
    hits = sum(1 for p in pats if re.search(p, text, flags=re.I))
    if hits == 0: return 0
    if hits == 1: return 1
    if hits == 2: return 2
    if hits <= 4: return 3
    return 4

def score(record):
    text = norm(" ".join([record.get("title",""), record.get("abstract",""), record.get("keywords","")]))
    # RQ fit is deliberately strict: needs P + T + EV/charging + either dynamic/resilience/heat.
    p = has_any(text, TERM_FAMILIES["power"])
    t = has_any(text, TERM_FAMILIES["transport"])
    ev = has_any(text, TERM_FAMILIES["ev_interface"])
    dyn = has_any(text, TERM_FAMILIES["dynamic"])
    res = has_any(text, TERM_FAMILIES["resilience"])
    phys = has_any(text, TERM_FAMILIES["physics"])
    rq_fit = 4 if (p and t and ev and (dyn or res or phys)) else 3 if (ev and phys and (p or t)) else 1

    grades = {
        "rq_fit": rq_fit,
        "physics": grade_0_4(text, "physics"),
        "coupling": 4 if (p and t and ev) else 3 if (ev and p) else 2 if (ev and t) else 0,
        "state_time": grade_0_4(text, "dynamic"),
        "service_resilience": grade_0_4(text, "resilience"),
        "math_method": min(4, sum(bool(re.search(x,text,re.I)) for x in [
            r"optimization", r"stochastic", r"markov", r"equilibrium", r"mixed[- ]integer",
            r"monte carlo", r"reinforcement learning", r"queue", r"power flow"
        ])),
        "validation": grade_0_4(text, "validation"),
        "intervention": grade_0_4(text, "intervention"),
    }
    total = sum((grades[k]/4.0)*WEIGHTS[k] for k in WEIGHTS)
    return round(total, 2), grades

def classify(record):
    text = norm(" ".join([record.get("title",""), record.get("abstract","")]))
    if re.search(r"review", text): return "review"
    if re.search(r"extreme heat|thermal derating|ambient temperature|hottest[- ]spot|thermal aging|thermal ageing", text):
        return "thermal_physics"
    if re.search(r"resilien|restoration|recovery|hazard|hurricane|flood|typhoon|cascad", text):
        return "resilience"
    if re.search(r"dynamic|spatiotemporal|equilibrium|state[- ]dependent", text):
        return "dynamic_coupling"
    return "cpts_method"

def select_diverse_26(scored):
    """
    Diversity-constrained selection. Prevents 26 near-duplicate optimization papers.
    Quotas are targets, not claims about the population.
    """
    quotas = {"review":4, "thermal_physics":6, "resilience":6, "dynamic_coupling":7, "cpts_method":3}
    selected, used = [], set()
    by_class = {k:[] for k in quotas}
    for r in scored:
        by_class.setdefault(r["strand"], []).append(r)
    for strand, q in quotas.items():
        for r in by_class.get(strand, [])[:q]:
            key = r.get("doi") or r.get("title")
            if key not in used:
                selected.append(r); used.add(key)
    # Fill shortages globally.
    for r in scored:
        if len(selected) >= 26: break
        key = r.get("doi") or r.get("title")
        if key not in used:
            selected.append(r); used.add(key)
    return sorted(selected[:26], key=lambda r: -r["score"])

def fetch_crossref(target=200):
    """
    Best-effort discovery from Crossref.
    For a formal review, replace/add Scopus/WoS/IEEE exports and preserve raw files.
    """
    pool = []
    rows_per_query = max(25, (target // len(SEARCH_FAMILIES)) + 10)
    for query in SEARCH_FAMILIES:
        url = (
            "https://api.crossref.org/works?"
            f"query.bibliographic={quote(query)}&"
            "filter=from-pub-date:2010-01-01,until-pub-date:2026-12-31,type:journal-article&"
            f"rows={rows_per_query}"
        )
        req = Request(url, headers={"User-Agent":"CPTS-Literature-Screen/1.0 (mailto:research@example.com)"})
        with urlopen(req, timeout=30) as response:
            obj = json.load(response)
        for item in obj["message"]["items"]:
            title = (item.get("title") or [""])[0]
            abstract = re.sub(r"<[^>]+>", " ", item.get("abstract",""))
            authors = "; ".join(
                " ".join(filter(None,[a.get("given",""),a.get("family","")]))
                for a in item.get("author",[])
            )
            issued = item.get("published-print") or item.get("published-online") or item.get("issued") or {}
            date_parts = issued.get("date-parts", [[None]])[0]
            pool.append({
                "title":title,
                "abstract":abstract,
                "authors":authors,
                "year":date_parts[0] if date_parts else None,
                "journal":(item.get("container-title") or [""])[0],
                "doi":item.get("DOI",""),
                "url":item.get("URL",""),
                "search_query":query,
            })
        time.sleep(0.2)
    pool = dedupe(pool)
    return pool

def read_csv(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def write_csv(path, rows):
    if not rows:
        return
    cols = sorted({k for r in rows for k in r})
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader(); w.writerows(rows)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", help="CSV/RIS-derived metadata export converted to CSV")
    ap.add_argument("--seed-json", help="Human-audited seed JSON; preserves 0–4 coded dimensions")
    ap.add_argument("--retrieve", action="store_true", help="Retrieve candidate records from Crossref")
    ap.add_argument("--target", type=int, default=200)
    ap.add_argument("--outdir", default="screening_output")
    args = ap.parse_args()

    out = Path(args.outdir); out.mkdir(parents=True, exist_ok=True)
    if args.seed_json:
        records = json.loads(Path(args.seed_json).read_text(encoding="utf-8"))
        # Seed mode is for verified/manual title-abstract evidence coding, not API discovery.
        scored = []
        for r in records:
            rr = dict(r)
            if all(k in rr for k in ["rq_fit","physics","coupling","state_time","service_resilience","math_method","validation_score","intervention"]):
                g = {
                    "rq_fit": float(rr["rq_fit"]), "physics": float(rr["physics"]),
                    "coupling": float(rr["coupling"]), "state_time": float(rr["state_time"]),
                    "service_resilience": float(rr["service_resilience"]), "math_method": float(rr["math_method"]),
                    "validation": float(rr["validation_score"]), "intervention": float(rr["intervention"])
                }
                rr["score"] = round(sum((g[k]/4.0)*WEIGHTS[k] for k in WEIGHTS), 2)
            scored.append(rr)
        scored.sort(key=lambda x: -float(x.get("score",0)))
        final26 = scored[:26]
        write_csv(out/"01_deduplicated_pool.csv", records)
        write_csv(out/"02_title_abstract_eligible.csv", scored)
        write_csv(out/"03_priority_26.csv", final26)
        manifest = {
            "raw_unique_records": len(records), "title_abstract_eligible": len(scored),
            "priority_core": len(final26), "mode":"human_audited_seed",
            "warning":"Seed mode validates the screening engine on the curated evidence set; it is not the 200-record discovery run.",
            "scientific_logic":"FRAMEWORK -> METHOD -> FINDINGS -> LIMITATIONS -> SYNTHESIS -> CONTRIBUTION",
            "review_philosophy":"ADOPT -> ADAPT -> TEST -> COMPARE -> IMPROVE"
        }
        (out/"run_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
        print(json.dumps(manifest, indent=2))
        return
    elif args.input:
        records = read_csv(args.input)
    elif args.retrieve:
        records = fetch_crossref(args.target)
    else:
        ap.error("Use --seed-json FILE.json, --input FILE.csv, or --retrieve")

    records = dedupe(records)
    raw_n = len(records)
    eligible = [r for r in records if gate(r)]

    scored = []
    for r in eligible:
        s, grades = score(r)
        rr = dict(r)
        rr.update(grades)
        rr["score"] = s
        rr["strand"] = classify(r)
        scored.append(rr)
    scored.sort(key=lambda x: -x["score"])

    final26 = select_diverse_26(scored)

    write_csv(out/"01_deduplicated_pool.csv", records)
    write_csv(out/"02_title_abstract_eligible.csv", scored)
    write_csv(out/"03_priority_26.csv", final26)

    manifest = {
        "raw_unique_records": raw_n,
        "title_abstract_eligible": len(scored),
        "priority_core": len(final26),
        "warning": (
            "Priority 26 is a title/abstract screen. Full-text extraction must verify "
            "framework, method, findings, author-stated limitations, validation, and assumptions."
        ),
        "scientific_logic": "FRAMEWORK -> METHOD -> FINDINGS -> LIMITATIONS -> SYNTHESIS -> CONTRIBUTION",
        "review_philosophy": "ADOPT -> ADAPT -> TEST -> COMPARE -> IMPROVE",
    }
    (out/"run_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(json.dumps(manifest, indent=2))

if __name__ == "__main__":
    main()