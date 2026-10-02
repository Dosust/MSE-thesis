#!/usr/bin/env python3
"""Build the formatted evidence workbook from the repository CSV files.

Requires the OpenAI artifact_tool package used in the thesis workspace.
No bibliography decisions are made here; this script only renders the
archived screening tables into a readable XLSX evidence workbook.
"""

from pathlib import Path
import csv
from artifact_tool import Workbook, SpreadsheetFile

ROOT = Path(__file__).resolve().parent
CORPUS_CSV = ROOT / "thesis_screen_200.csv"
SHORTLIST_CSV = ROOT / "thesis_shortlist_26.csv"
OUT = ROOT / "Physics_Based_Mathematical_Engineering_200_to_26.xlsx"

def read_csv(path):
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

corpus = read_csv(CORPUS_CSV)
shortlist = read_csv(SHORTLIST_CSV)

if len(corpus) != 200:
    raise SystemExit(f"Expected 200 corpus records, found {len(corpus)}")
if len(shortlist) != 26:
    raise SystemExit(f"Expected 26 priority records, found {len(shortlist)}")

wb = Workbook.create()
summary = wb.worksheets.add("Protocol & Summary")
allsh = wb.worksheets.add("Corpus 200")
shortsh = wb.worksheets.add("Shortlist 26")
extractsh = wb.worksheets.add("Deep Extraction 26")

summary_rows = [
    ["Physics-Based Mathematical Engineering: 200 → 26 Literature Screen", ""],
    ["Guiding RQ", "How do time-varying physical states and interdependencies between Power and Transportation systems determine service degradation and recovery under extreme heat, and how can targeted operational interventions reduce the resulting coupled service deficits?"],
    ["Scientific philosophy", "FRAMEWORK → METHOD → FINDINGS → LIMITATIONS → SYNTHESIS → CONTRIBUTION."],
    ["Corpus", "Exactly 200 archived records."],
    ["Priority evidence set", "26 papers: 5 Foundations | 9 Coupled P–T | 9 Heat/physical-state | 3 Intervention/recovery."],
    ["Critical distinction", "Author-stated limitation ≠ thesis-inferred limitation ≠ research contribution."],
    ["Next stage", "Full-text extraction before any definitive gap or novelty claim."],
]
summary.get_range(f"A1:B{len(summary_rows)}").values = summary_rows
summary.merge_cells("A1:B1")
summary.get_range("A1").format = {
    "fill": "#87CEFA",
    "font": {"bold": True, "size": 16, "color": "#1F2937"},
    "horizontal_alignment": "center",
    "vertical_alignment": "center",
}
summary.get_range(f"A2:A{len(summary_rows)}").format = {
    "fill": "#EAF7FF",
    "font": {"bold": True, "color": "#1F2937"},
}
summary.get_range(f"A1:B{len(summary_rows)}").format.wrap_text = True
summary.get_range(f"A1:A{len(summary_rows)}").format.column_width = 25
summary.get_range(f"B1:B{len(summary_rows)}").format.column_width = 80

corpus_cols = list(corpus[0].keys())
all_values = [corpus_cols] + [[r.get(c, "") for c in corpus_cols] for r in corpus]
allsh.get_range_by_indexes(0, 0, len(all_values), len(corpus_cols)).values = all_values
allsh.freeze_panes.freeze_rows(1)
allsh.get_range_by_indexes(0, 0, 1, len(corpus_cols)).format = {
    "fill": "#87CEFA",
    "font": {"bold": True, "color": "#1F2937"},
    "horizontal_alignment": "center",
    "vertical_alignment": "center",
    "wrap_text": True,
}
allsh.get_range_by_indexes(1, 0, len(corpus), len(corpus_cols)).format.wrap_text = True

short_cols = list(shortlist[0].keys())
short_values = [short_cols] + [[r.get(c, "") for c in short_cols] for r in shortlist]
shortsh.get_range_by_indexes(0, 0, len(short_values), len(short_cols)).values = short_values
shortsh.freeze_panes.freeze_rows(1)
shortsh.get_range_by_indexes(0, 0, 1, len(short_cols)).format = {
    "fill": "#00BFFF",
    "font": {"bold": True, "color": "#FFFFFF"},
    "horizontal_alignment": "center",
    "vertical_alignment": "center",
    "wrap_text": True,
}
shortsh.get_range_by_indexes(1, 0, len(shortlist), len(short_cols)).format.wrap_text = True

deep_cols = [
    "Primary evidence role", "Authors", "Title", "Year", "DOI",
    "Framework", "Method / mathematics", "Physics represented", "Findings",
    "Author-stated limitations", "Our inferred limitation", "Assumptions",
    "Validation", "Relevance: adopt / adapt / compare / avoid",
    "Possible improvement for RQ", "Full-text verification status",
]
deep_rows = [deep_cols]
for r in shortlist:
    deep_rows.append([
        r.get("Primary evidence role", ""), r.get("Authors", ""), r.get("Title", ""),
        r.get("Year", ""), r.get("DOI", ""),
        "TO EXTRACT", "TO EXTRACT", "TO EXTRACT", "TO EXTRACT",
        "TO EXTRACT",
        "DO NOT FILL until separated from author-stated limitation",
        "TO EXTRACT", "TO EXTRACT", "TO EXTRACT",
        "Only after evidence synthesis", "Pending full-text review",
    ])
extractsh.get_range_by_indexes(0, 0, len(deep_rows), len(deep_cols)).values = deep_rows
extractsh.freeze_panes.freeze_rows(1)
extractsh.get_range_by_indexes(0, 0, 1, len(deep_cols)).format = {
    "fill": "#1F2937",
    "font": {"bold": True, "color": "#FFFFFF"},
    "horizontal_alignment": "center",
    "vertical_alignment": "center",
    "wrap_text": True,
}
extractsh.get_range_by_indexes(1, 0, len(shortlist), len(deep_cols)).format.wrap_text = True

# Bounded widths: keep the workbook readable without uncontrolled autofit.
for sheet in [allsh, shortsh, extractsh]:
    used_cols = 22 if sheet.name == "Corpus 200" else 16
    for j in range(used_cols):
        width = 14
        if j in (1, 2): width = 30 if j == 1 else 42
        if sheet.name == "Deep Extraction 26" and j >= 5: width = 30
        sheet.get_range_by_indexes(0, j, max(2, len(shortlist) + 1), 1).format.column_width = width

SpreadsheetFile.export_xlsx(wb).save(str(OUT))
print(OUT)
