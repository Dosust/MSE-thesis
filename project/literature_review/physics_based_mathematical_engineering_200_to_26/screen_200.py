#!/usr/bin/env python3
"""
Reproduce and verify the archived 200 → 26 evidence selection for:

Physics-Based Mathematical Engineering of Power–Transportation
Interdependencies for Resilience

Scientific rule:
    FRAMEWORK → METHOD → FINDINGS → LIMITATIONS → SYNTHESIS → CONTRIBUTION

Important:
- thesis_screen_200.csv is the canonical archived screening table.
- The final 26 are a priority full-text evidence set, not proof of novelty.
- Author-stated limitations, thesis-inferred limitations, and candidate
  contributions must remain separate during deep extraction.
"""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CORPUS = ROOT / "thesis_screen_200.csv"
OUT_CSV = ROOT / "thesis_shortlist_26.csv"
OUT_JSON = ROOT / "thesis_shortlist_26.json"

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
    "10.1109/tte.2024.3400289": ("Intervention / recovery", "Uses EV mobility and V2G as cross-system restoration resources under natural hazards."),
    "10.1016/j.segan.2025.101747": ("Intervention / recovery", "Provides a staged defend–respond–restore architecture for coupled P–T resilience."),
}

ROLE_ORDER = {
    "Foundation": 0,
    "Coupled P–T": 1,
    "Heat / physical state": 2,
    "Intervention / recovery": 3,
}

def doi_key(value: str) -> str:
    return (value or "").strip().lower().replace("https://doi.org/", "")

def main() -> None:
    with CORPUS.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    if len(rows) != 200:
        raise SystemExit(f"Expected exactly 200 archived records; found {len(rows)}.")

    # Reapply the frozen evidence-role selection from DOI identity.
    for row in rows:
        role_reason = FINAL.get(doi_key(row.get("DOI", "")))
        if role_reason:
            role, reason = role_reason
            row["Final 26"] = "YES"
            row["Primary evidence role"] = role
            row["Why retained"] = reason
        else:
            row["Final 26"] = "NO"
            row["Primary evidence role"] = ""
            row["Why retained"] = ""

    selected = [r for r in rows if r["Final 26"] == "YES"]
    if len(selected) != 26:
        raise SystemExit(f"Expected 26 selected records; found {len(selected)}.")

    dois = [doi_key(r.get("DOI", "")) for r in selected]
    if len(set(dois)) != 26:
        raise SystemExit("Duplicate DOI detected in the final 26.")

    selected.sort(
        key=lambda r: (
            ROLE_ORDER[r["Primary evidence role"]],
            int(float(r.get("Year") or 0)),
            r.get("Title", ""),
        )
    )

    output_fields = [
        "Primary evidence role", "Authors", "Title", "Year", "Source title",
        "DOI", "Source URL", "Why retained", "Score PT",
        "Score HeatThermal", "Score StateTime", "Score ServiceRecovery",
        "Score MathPhysics", "Score Intervention", "Score Validation",
        "Score Total",
    ]

    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=output_fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(selected)

    with OUT_JSON.open("w", encoding="utf-8") as f:
        json.dump(
            [{k: r.get(k, "") for k in output_fields} for r in selected],
            f,
            ensure_ascii=False,
            indent=2,
        )

    roles = Counter(r["Primary evidence role"] for r in selected)
    expected = {
        "Foundation": 5,
        "Coupled P–T": 9,
        "Heat / physical state": 9,
        "Intervention / recovery": 3,
    }
    if dict(roles) != expected:
        raise SystemExit(f"Unexpected role balance: {dict(roles)}")

    print("SCREEN REPRODUCTION PASSED")
    print("Archived corpus:", len(rows))
    print("Priority evidence set:", len(selected))
    print("Unique DOIs:", len(set(dois)))
    print("Evidence roles:", dict(roles))
    print("Scientific status: priority full-text set; not a novelty claim.")

if __name__ == "__main__":
    main()
