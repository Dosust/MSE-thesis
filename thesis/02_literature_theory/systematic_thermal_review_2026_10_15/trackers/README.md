# Operational tracker: CSV projection of the eight-sheet Excel template

**Status:** UNEXECUTED / TEMPLATE ONLY; **not an executed systematic review**.

The eight CSV files in this directory are text-based projections of the eight worksheets of `Thermal_PT_Systematic_Review_Execution_Tracker_2026-10-15.xlsx` (local original verified as a valid, eight-sheet XLSX). The GitHub app in this workflow accepts text Git blobs; it did **not** directly upload the binary Excel workbook.

The exports preserve sheet data, labels and draft rows but do not preserve spreadsheet formulas, validation drop-downs, cell styles, or Excel-specific interactivity. Treat the original workbook as the editable spreadsheet master, the CSV files as version-controllable seed templates.

- Original spreadsheet SHA-256: `8c12c1904d1cc15c7e1a409e11f636d31124589992e6537b86714133a9da8493`.
- Original protocol SHA-256: `2b0e3d4c686e51fceef05527f0f754c1256db81346b9b1deb6c339a611488f19`.
- Original pasted execution guide SHA-256: `5b59cf8df1760873105e26b631d37c815e345fcec1ab529480add432c7ce4f69`.
- The SHA-256 values refer to the user-accessible original files, **not** these parsed text projections.

## Record-level rules

1. New search rows must preserve the exact database string, filters, date, count and raw bibliographic export.
2. `NOT RUN` is not a zero-count search. Unentered PRISMA values mean **unknown**, not 0.
3. `SEED ONLY` entries are query-recall sentinels. They have not been screened or included.
4. No row is promoted to `PDF VERIFIED` without inspecting the original PDF and recording page/equation/figure/table anchors.
5. Data-readiness `DA-2` requires opening actual observations. Metadata alone are `DA-1` or lower.
6. The original 2026-10-15 workbook and the protocol are PROPOSED materials pending supervisory/methodological review.
7. Do not equate simulator output, synthetic data, or co-located weather with causal thermal interdependency field validation.

## Sheets

| CSV | Function |
| --- | --- |
| `start_here.csv` | Execution roadmap and method links |
| `search_log.csv` | Exact database-by-query audit trail |
| `screening.csv` | Record/abstract/full-text inclusion and exclusion |
| `pdf_evidence.csv` | Original-PDF physical-equation/claim provenance |
| `data_audit.csv` | Raw data access, physical fields and identification gates |
| `method_compare.csv` | Matched physics / grey-box / PI-ML evidence |
| `prisma.csv` | PRISMA count worksheet; values are unverified until searches run |
| `seed_papers.csv` | Known-item recall tests, not the screened corpus |
