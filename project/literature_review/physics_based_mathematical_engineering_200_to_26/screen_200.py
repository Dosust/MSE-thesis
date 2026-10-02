#!/usr/bin/env python3
"""
Screen exactly 200 papers to a 26-paper high-rigor evidence set for:

Physics-Based Mathematical Engineering of Power–Transportation
Interdependencies for Resilience

Scientific rule:
  FRAMEWORK -> METHOD -> FINDINGS -> LIMITATIONS -> SYNTHESIS -> CONTRIBUTION

This script separates:
1) machine triage (transparent title/abstract/metadata scoring), from
2) scientific confirmation (domain-balanced inclusion of foundational,
   coupled P–T, heat/thermal, and intervention/recovery evidence).

The final 26 are NOT treated as proof of novelty. They are the priority
full-text evidence set for reconstructing the existing science.
"""

from artifact_tool import Blob, SpreadsheetFile, Workbook
from pathlib import Path
import csv, json, re, unicodedata

BASE_XLSX = Path("/mnt/data/Master_Bibliography_209_ORGANIZED.xlsx")
ADDITIONS_JSON = Path("/mnt/data/targeted_additions_30.json")
OUT_CORPUS = Path("/mnt/data/thesis_screen_200.csv")
OUT_SHORT = Path("/mnt/data/thesis_shortlist_26.csv")
OUT_JSON = Path("/mnt/data/thesis_shortlist_26.json")
OUT_XLSX = Path("/mnt/data/Physics_Based_Mathematical_Engineering_200_to_26.xlsx")

FINAL = {
"10.1109/37.969131": ("Foundation", "Defines infrastructure dependency/interdependency and a defensible vocabulary for coupling."),
"10.1016/j.ress.2013.06.040": ("Foundation", "Maps the principal modeling families for interdependent critical infrastructure systems."),
"10.1193/1.1623497": ("Foundation", "Establishes quantitative service-performance and recovery concepts for infrastructure resilience."),
"10.1016/j.ress.2011.09.002": ("Foundation", "Makes resilience explicitly time-dependent and links disruption, restoration, and performance."),
"10.1016/j.trb.2010.10.001": ("Foundation", "Provides a multilayer mathematical framework for heterogeneous infrastructure interdependencies."),

"10.1016/j.ress.2017.01.026": ("Coupled P–T", "Explicitly models coupled traffic and electric-power resilience with linking variables and stochastic optimization."),
"10.1007/s40565-019-0516-7": ("Coupled P–T", "Reviews the mathematical building blocks of power–transportation interdependence, including traffic equilibrium and power flow."),
"10.1016/j.ijepes.2022.108058": ("Coupled P–T", "Models EV-mediated cascading propagation between transportation and power networks."),
"10.1186/s42162-022-00249-w": ("Coupled P–T", "Represents joint stochastic operation of transportation and power-distribution networks."),
"10.1016/j.energy.2025.135330": ("Coupled P–T", "Quantifies P–T dependency using supply–demand relations and heterogeneous fast-charging stations."),
"10.1016/j.ress.2025.112005": ("Coupled P–T", "Shows that EV charging decisions can change measured P–T interdependency under disruption."),
"10.1016/j.est.2025.118419": ("Coupled P–T", "Decision-oriented review connecting network models, resilience, EV flexibility, and implementable controls."),
"10.1016/j.rser.2025.115786": ("Coupled P–T", "Synthesizes current mathematical coordination, optimization, uncertainty, and resilience methods for P–T systems."),
"10.1016/j.apenergy.2026.128158": ("Coupled P–T", "Couples dynamic traffic-energy assignment, V2G, and distribution-system restoration in a resilience decision model."),

"10.1080/23789689.2018.1448668": ("Heat / physical state", "Connects extreme heat with interdependent urban infrastructure stress and resilience."),
"10.1016/j.segan.2026.102137": ("Heat / physical state", "Dynamically maps heatwave weather variables to thermal limits and power-system resilience."),
"10.1049/gtd2.70362": ("Heat / physical state", "Models distribution-grid resilience under extreme heat with reduced capacity and elevated demand."),
"10.1016/j.ecmx.2026.101960": ("Heat / physical state", "Provides field evidence of temperature-driven fast-charger thermal derating and longer charging time."),
"10.1016/j.segan.2023.101096": ("Heat / physical state", "Links EV charging to transformer thermal state, service disruption, and controlled-charging mitigation."),
"10.1049/gtd2.13025": ("Heat / physical state", "Uses weather-dependent dynamic thermal ratings to quantify EV hosting limits and charging control."),
"10.1016/j.apenergy.2024.125051": ("Heat / physical state", "Quantifies how extreme heat changes EV energy use, driving range, and future grid charging demand."),
"10.1038/s44333-024-00008-2": ("Heat / physical state", "Links temperature and traffic to electric-bus energy states, depot charging, and grid loading."),
"10.3390/su15097375": ("Heat / physical state", "Directly couples ambient temperature, battery charging performance, and electric-bus depot scheduling."),

"10.1007/978-981-96-4856-6_5": ("Intervention / recovery", "Tests coordinated EV charging/V2G as an operational resilience action during extreme heat."),
"10.1109/TTE.2024.3400289": ("Intervention / recovery", "Uses EV mobility and V2G as cross-system restoration resources under natural hazards."),
"10.1016/j.segan.2025.101747": ("Intervention / recovery", "Provides a staged defend–respond–restore architecture for coupled P–T resilience.")
}

FINAL = {k.lower(): v for k, v in FINAL.items()}

def norm(s):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFKD", str(s or "")).lower()).strip()

def has(text, terms):
    return any(t in text for t in terms)

def score(rec):
    text = norm(" ".join(str(rec.get(k, "") or "") for k in [
        "Title", "Abstract", "Author Keywords", "Relevance note",
        "What is evaluated: interface type / system / resilience dimension / quantified outcome",
        "Procedure (how is it used?)", "Core elements (as named in the paper)"
    ]))
    pt = 0
    if (re.search(r"(coupl|interdepend|interconnect).{0,60}(power|electric).{0,60}(transport|traffic)", text)
        or re.search(r"(power|electric).{0,60}(transport|traffic).{0,60}(coupl|interdepend|interconnect)", text)):
        pt = 4
    elif has(text, ["power", "distribution network", "grid"]) and has(text, ["electric vehicle", "ev charging", "charging station", "v2g", "electric bus", "fleet"]) and has(text, ["transport", "traffic", "mobility", "vehicle"]):
        pt = 3
    elif has(text, ["electric vehicle", "ev charging", "charging station", "v2g", "electric bus", "fleet"]) and has(text, ["grid", "power", "transformer", "feeder", "distribution"]):
        pt = 2

    heat = 0
    if has(text, ["extreme heat", "heatwave", "heat wave", "hot climate", "extreme climatic"]):
        heat += 3
    if has(text, ["thermal derating", "ambient temperature", "hot-spot", "hottest-spot", "top-oil", "thermal rating"]):
        heat += 2
    elif has(text, ["thermal", "temperature"]):
        heat += 1
    heat = min(4, heat)

    state = 0
    if has(text, ["time-varying", "time varying", "dynamic", "spatiotemporal", "spatio-temporal", "trajectory", "multi-period", "temporal evolution"]):
        state += 2
    if has(text, ["state of charge", "soc", "physical state", "operational state", "thermal state", "hot-spot", "top-oil"]):
        state += 1
    if has(text, ["capacity", "derating", "loading", "equilibrium"]):
        state += 1
    state = min(4, state)

    service = 0
    if has(text, ["resilience", "recovery", "restoration", "rapidity"]):
        service += 2
    if has(text, ["service", "load shedding", "travel time", "mobility", "functionality", "service disruption", "deficit", "performance"]):
        service += 1
    service = min(4, service)

    method_groups = [
        ["differential", "dynamical", "dae", "state-space", "system dynamics"],
        ["thermal model", "heat transfer", "ieee 738", "iec thermal", "hot-spot"],
        ["power flow", "optimal power flow", "traffic assignment", "user equilibrium", "variational inequality"],
        ["optimization", "mixed-integer", "mixed integer", "bilevel", "bi-level", "stochastic", "monte carlo", "linear programming", "nonlinear programming", "reinforcement learning", "agent-based"],
    ]
    method = sum(1 for g in method_groups if has(text, g))

    action = 0
    if has(text, ["controlled charging", "smart charging", "scheduling", "dispatch", "v2g", "reconfiguration", "routing", "pricing", "storage", "hardening", "intervention", "mitigation"]):
        action += 2
    if has(text, ["control", "restore", "restoration", "management"]):
        action += 1
    action = min(3, action)

    validation = 0
    if has(text, ["field", "experimental", "measured", "real-world", "real world"]):
        validation += 2
    if has(text, ["case study", "validated", "validation", "simulation results", "ieee 33", "test network", "data"]):
        validation += 1
    if rec.get("Validation"):
        validation = max(validation, 1)
    validation = min(3, validation)

    doi = norm(rec.get("DOI", ""))
    foundation = 1 if doi in {
        "10.1109/37.969131",
        "10.1016/j.ress.2013.06.040",
        "10.1193/1.1623497",
        "10.1016/j.ress.2011.09.002",
        "10.1016/j.trb.2010.10.001",
        "10.1038/nature08932",
    } else 0

    interaction_bonus = 0
    if pt >= 3 and heat >= 2: interaction_bonus += 5
    if pt >= 3 and state >= 2: interaction_bonus += 3
    if state >= 2 and heat >= 2: interaction_bonus += 2
    if service >= 2 and action >= 2: interaction_bonus += 2
    if pt >= 3 and service >= 2: interaction_bonus += 2

    total = pt + heat + state + service + method + action + validation + 6*foundation + interaction_bonus
    return {
        "PT": pt, "HeatThermal": heat, "StateTime": state, "ServiceRecovery": service,
        "MathPhysics": method, "Intervention": action, "Validation": validation,
        "Foundation": foundation, "InteractionBonus": interaction_bonus, "Total": total
    }

wb0 = SpreadsheetFile.import_xlsx(Blob.load(str(BASE_XLSX)))
sh0 = wb0.worksheets.get_item("Master 209")
values = sh0.get_range("A1:AK210").values
headers = values[0]
master = [dict(zip(headers, row)) for row in values[1:]]

base170 = []
for r in master[:170]:
    q = dict(r)
    q["Corpus source"] = "Existing verified master bibliography (first 170 by prior sorted rank)"
    q["Source URL"] = q.get("Open Access URL") or (f"https://doi.org/{q.get('DOI')}" if q.get("DOI") else "")
    base170.append(q)

with open(ADDITIONS_JSON, "r", encoding="utf-8") as f:
    additions = json.load(f)
assert len(additions) == 30
for r in additions:
    r["Corpus source"] = "Targeted current-scope web update"
    r["Source URL"] = r.get("URL", "")

corpus = base170 + additions
assert len(corpus) == 200

for idx, r in enumerate(corpus, start=1):
    s = score(r)
    r.update({f"Score {k}": v for k, v in s.items()})
    r["Screen ID"] = idx
    r["Machine eligible"] = (
        s["Foundation"] == 1
        or (s["PT"] >= 2 and (s["StateTime"] + s["ServiceRecovery"] + s["MathPhysics"] + s["Intervention"]) >= 3)
        or (s["HeatThermal"] >= 2 and (s["PT"] >= 1 or s["ServiceRecovery"] >= 1)
            and (s["StateTime"] + s["MathPhysics"] + s["Validation"]) >= 2)
    )
    doi = norm(r.get("DOI", ""))
    if doi in FINAL:
        role, reason = FINAL[doi]
        r["Final 26"] = "YES"
        r["Primary evidence role"] = role
        r["Why retained"] = reason
    else:
        r["Final 26"] = "NO"
        r["Primary evidence role"] = ""
        r["Why retained"] = ""

chosen = [r for r in corpus if r["Final 26"] == "YES"]
assert len(chosen) == 26, f"Expected 26 selected papers, found {len(chosen)}"
assert len({norm(r.get("DOI","")) for r in chosen}) == 26, "Duplicate DOI in final 26"

corpus_cols = [
    "Screen ID","Corpus source","Authors","Title","Year","Source title","DOI","Source URL",
    "Score PT","Score HeatThermal","Score StateTime","Score ServiceRecovery",
    "Score MathPhysics","Score Intervention","Score Validation","Score Foundation",
    "Score InteractionBonus","Score Total","Machine eligible",
    "Final 26","Primary evidence role","Why retained"
]
with open(OUT_CORPUS, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=corpus_cols, extrasaction="ignore")
    w.writeheader(); w.writerows(corpus)

short_cols = [
    "Primary evidence role","Authors","Title","Year","Source title","DOI","Source URL",
    "Why retained","Score PT","Score HeatThermal","Score StateTime","Score ServiceRecovery",
    "Score MathPhysics","Score Intervention","Score Validation","Score Total"
]
chosen_sorted = sorted(chosen, key=lambda r: (
    ["Foundation","Coupled P–T","Heat / physical state","Intervention / recovery"].index(r["Primary evidence role"]),
    int(r.get("Year") or 0), r.get("Title","")
))
with open(OUT_SHORT, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=short_cols, extrasaction="ignore")
    w.writeheader(); w.writerows(chosen_sorted)
with open(OUT_JSON, "w", encoding="utf-8") as f:
    json.dump(chosen_sorted, f, ensure_ascii=False, indent=2)

wb = Workbook.create()
summary = wb.worksheets.add("Protocol & Summary")
allsh = wb.worksheets.add("Corpus 200")
shortsh = wb.worksheets.add("Shortlist 26")
extractsh = wb.worksheets.add("Deep Extraction 26")

summary_rows = [
    ["Physics-Based Mathematical Engineering: 200 → 26 Literature Screen", ""],
    ["Guiding RQ", "How do time-varying physical states and interdependencies between Power and Transportation systems determine service degradation and recovery under extreme heat, and how can targeted operational interventions reduce the resulting coupled service deficits?"],
    ["Scientific philosophy", "Understand existing science first: FRAMEWORK → METHOD → FINDINGS → LIMITATIONS → SYNTHESIS → CONTRIBUTION."],
    ["Corpus construction", "170 records from the existing verified 209-paper master bibliography + 30 targeted current-scope records = exactly 200 screened records."],
    ["Machine triage", "Transparent metadata/abstract scores: P–T relevance, heat/thermal physics, state/time, service/recovery, math/physics method, intervention, validation."],
    ["Scientific confirmation", "Final 26 are domain-balanced priority papers; machine score does not substitute for full-text judgment."],
    ["Critical distinction", "Author-stated limitation ≠ our inferred limitation ≠ thesis contribution."],
    ["Final evidence roles", "5 Foundations | 9 Coupled P–T | 9 Heat/physical-state | 3 Intervention/recovery"],
    ["Next step", "Full-text extraction of Framework, Method, Findings, Author-stated Limitations, Assumptions, Validation, Relevance, and candidate adaptation."],
]
summary.get_range(f"A1:B{len(summary_rows)}").values = summary_rows
summary.merge_cells("A1:B1")
summary.get_range("A1").format = {
    "fill":"#87CEFA","font":{"bold":True,"size":16,"color":"#1F2937"},
    "horizontal_alignment":"center","vertical_alignment":"center"
}
summary.get_range("A2:A9").format = {"font":{"bold":True,"color":"#1F2937"},"fill":"#EAF7FF"}
summary.get_range("A1:B9").format.wrap_text = True
summary.get_range("A1:A9").format.column_width = 24
summary.get_range("B1:B9").format.column_width = 80
summary.get_range("A1:B9").format.autofit_rows()

all_rows = [corpus_cols] + [[r.get(c,"") for c in corpus_cols] for r in corpus]
allsh.get_range(f"A1:V{len(all_rows)}").values = all_rows
allsh.freeze_panes.freeze_rows(1)
allsh.get_range("A1:V1").format = {
    "fill":"#87CEFA","font":{"bold":True,"color":"#1F2937"},
    "horizontal_alignment":"center","vertical_alignment":"center","wrap_text":True
}
allsh.get_range(f"A2:V{len(all_rows)}").format.wrap_text = True
for col in ["C","D","G","H","U","V"]:
    allsh.get_range(f"{col}1:{col}{len(all_rows)}").format.column_width = 30 if col not in ["D","V"] else 42
for col in ["A","E","I","J","K","L","M","N","O","P","Q","R","S","T"]:
    allsh.get_range(f"{col}1:{col}{len(all_rows)}").format.column_width = 13
allsh.get_range(f"T2:T{len(all_rows)}").conditional_formats.add_custom('=T2="YES"', {"fill":"#DDF5FF","font":{"bold":True}})

short_rows = [short_cols] + [[r.get(c,"") for c in short_cols] for r in chosen_sorted]
shortsh.get_range(f"A1:P{len(short_rows)}").values = short_rows
shortsh.freeze_panes.freeze_rows(1)
shortsh.get_range("A1:P1").format = {
    "fill":"#00BFFF","font":{"bold":True,"color":"#FFFFFF"},
    "horizontal_alignment":"center","vertical_alignment":"center","wrap_text":True
}
shortsh.get_range(f"A2:P{len(short_rows)}").format.wrap_text = True
for c,wid in {"A":22,"B":28,"C":44,"D":9,"E":25,"F":24,"G":30,"H":46}.items():
    shortsh.get_range(f"{c}1:{c}{len(short_rows)}").format.column_width = wid
for c in list("IJKLMNOP"):
    shortsh.get_range(f"{c}1:{c}{len(short_rows)}").format.column_width = 12

deep_cols = [
    "Primary evidence role","Authors","Title","Year","DOI",
    "Framework","Method / mathematics","Physics represented","Findings",
    "Author-stated limitations","Our inferred limitation","Assumptions",
    "Validation","Relevance: adopt / adapt / compare / avoid",
    "Possible improvement for RQ","Full-text verification status"
]
deep_rows = [deep_cols]
for r in chosen_sorted:
    deep_rows.append([
        r["Primary evidence role"],r.get("Authors",""),r.get("Title",""),r.get("Year",""),r.get("DOI",""),
        "TO EXTRACT","TO EXTRACT","TO EXTRACT","TO EXTRACT",
        "TO EXTRACT","DO NOT FILL until separated from author-stated limitation","TO EXTRACT",
        "TO EXTRACT","TO EXTRACT","Only after evidence synthesis","Pending full-text review"
    ])
extractsh.get_range(f"A1:P{len(deep_rows)}").values = deep_rows
extractsh.freeze_panes.freeze_rows(1)
extractsh.get_range("A1:P1").format = {
    "fill":"#1F2937","font":{"bold":True,"color":"#FFFFFF"},
    "horizontal_alignment":"center","vertical_alignment":"center","wrap_text":True
}
extractsh.get_range(f"A2:P{len(deep_rows)}").format.wrap_text = True
for c,wid in {"A":22,"B":26,"C":42,"D":9,"E":24}.items():
    extractsh.get_range(f"{c}1:{c}{len(deep_rows)}").format.column_width = wid
for c in list("FGHIJKLMNOP"):
    extractsh.get_range(f"{c}1:{c}{len(deep_rows)}").format.column_width = 30

SpreadsheetFile.export_xlsx(wb).save(str(OUT_XLSX))

roles = {}
for r in chosen_sorted:
    roles[r["Primary evidence role"]] = roles.get(r["Primary evidence role"],0) + 1

print("SCREEN COMPLETE")
print(f"Corpus screened: {len(corpus)}")
print(f"Machine-eligible pool: {sum(1 for r in corpus if r['Machine eligible'])}")
print(f"Final high-rigor priority set: {len(chosen_sorted)}")
print("Role balance:", roles)
print("Outputs:")
for p in [OUT_CORPUS, OUT_SHORT, OUT_JSON, OUT_XLSX]:
    print(" -", p)
