# Workbook and Relational Data Model

## 1. Recommended evidence-first structure for only the 10 papers

The final Top-10 analytical file should not be a compressed 20-column screening CSV. The preferred architecture is relational and evidence-first.

### Primary tables

1. `01_Papers` — bibliographic master, exactly 10 rows.
2. `02_KLM_Evidence` — exact evidence behind K, L/SM, M decisions.
3. `03_NT_Evidence` — exact passages supporting N–T.
4. `04_P_Engineering` — one row per engineering-performance evidence item.
5. `05_F_Integration` — one row per candidate/confirmed engineering–sustainability linkage.
6. `06_S_Sustainability` — one row per quantified sustainability result.
7. `07_D_Decision` — one row per ranking/selection/optimization/trade-off evidence item.
8. `08_Method_Architecture` — method-family components and procedure evidence.
9. `09_Validation` — application/internal/external validation evidence.
10. `10_Methods_Mentioned` — T/backward-snowballing methods/tools.
11. `11_Interpretation` — human/analyst interpretation after extraction.
12. `12_Scoring` — R1–R4–lambda only after interpretation.

This structure allows one paper to have multiple evidence records and prevents loss of information.

## 2. `01_Papers`

`Paper_ID | Top10_Rank | Original_CSV_ID | Authors | Title | Year | Journal | DOI | PDF_Identity_Status | PDF_Path_or_Reference`

## 3. `02_KLM_Evidence`

`Paper_ID | Field(K/L/M) | Exact_Passage | Page | Section | Table_Figure_Equation | Author_Action | Evidence_Status | Decision`

## 4. `03_NT_Evidence`

`Paper_ID | Field(N/O/P/Q/R/S/T) | Exact_Passage | Page | Section | Table_Figure_Equation | Author_Terminology | Controlled_Extraction | Evidence_Status`

## 5. `04_P_Engineering`

`P_Record_ID | Paper_ID | Exact_Passage | Page | Section | Table_Figure_Equation | Family | Metric_As_Written | Method_As_Written | Result_As_Written | Unit_As_Written | Alternative_As_Written | Comparator_As_Written | Origin | Author_Generated | Evidence_Status`

## 6. `05_F_Integration`

`F_Record_ID | Paper_ID | Preceding_Context | Exact_Passage | Following_Context | Page | Section | Equation_As_Written | Table_Figure | Source_Variable_As_Written | Transformation_As_Written | Target_As_Written | Alternative_Linkage_Evidence | Traceable_Alternatives | Causal_Verb_or_Operator | Candidate_F_Class | Formula_Type(AF/AC/RR/NF) | Evidence_Status`

Final lambda belongs in scoring, not in the raw extraction table.

## 7. `06_S_Sustainability`

`S_Record_ID | Paper_ID | Exact_Passage | Page | Section | Table_Figure_Equation | Method_As_Written | Method_Family | Dimension | Indicator_As_Written | Result_As_Written | Unit_As_Written | Functional_Basis_As_Written | Alternative_As_Written | Method_Generated | Evidence_Status`

## 8. `07_D_Decision`

`D_Record_ID | Paper_ID | Exact_Passage | Page | Section | Table_Figure_Equation | Decision_Type_Candidate | Alternatives_As_Written | Decision_Rule_As_Written | Ranking_As_Written | Selected_Alternative_As_Written | Optimization_Objective_As_Written | Tradeoff_As_Written | Sensitivity_Robustness | Evidence_Status`

## 9. `08_Method_Architecture`

Use one row per method component:

`Paper_ID | Method_Family | Component_Name | Component_Status(REPORTED/PARTIAL/NR/NA/U) | Exact_Passage | Page | Section`

This keeps R2 components machine-readable rather than concatenated in one text cell.

## 10. `09_Validation`

`Paper_ID | Validation_Level(No/Applied/Internal/External) | Validation_Mechanism | Exact_Passage | Page | Section | Independent_Data_or_Case | Notes`

## 11. `10_Methods_Mentioned`

`Paper_ID | Method_Name_As_Written | Canonical_Method_Name | Context | Page | Section | Focal_or_Referenced | Include_for_Backward_Snowballing`

## 12. `11_Interpretation`

`Paper_ID | N_Summary | O_Numbered_Core_Elements | P_Procedure_Chain | Q_Strategy_Summary | R_Domain_Summary | S_Validation_Summary | T_Methods_Summary | PFSD_Chain | Analyst_Notes`

## 13. `12_Scoring`

`Paper_ID | R1 | R1_Reason | R2 | R2_Reason | R2_RC | R3 | R3_Reason | R4 | R4_Reason | Lambda | Lambda_Reason | Perfect_Status | Tier_A_Status`

Perfect status is derived, never typed:

```excel
=IF(AND(R1=3,R2=3,R3=3,R4=3,Lambda=3),"PERFECT","NOT PERFECT")
```

Tier A:

```excel
=IF(AND(R1=3,R2>=2,R3=3,R4=3,Lambda>=2),"Tier A","Not Tier A")
```

## 14. Derived comparative workbook sheets

After evidence is frozen, derive:

- `K_T_Screening_Extraction`
- `PFSD_Detailed_Extraction`
- `Table_1_Comparative_Synthesis`
- `Table_1_Visual_Evidence`
- `Table_2_Visual_Mapping`

Source-of-truth hierarchy:

```math
Raw\ Evidence\rightarrow Interpretation\rightarrow Scoring\rightarrow Derived\ Synthesis.
```

## 15. Visual evidence matrix

Use the complete frozen taxonomy, including zero-coverage categories. Zero is scientifically informative and should not be hidden by dropping a category.

Cell coding: `**` direct focal implementation/generation; `*` secondary/discussed; blank not identified. Coverage values must be formula-derived.

## 16. Mapping matrix

Raw mapping counts should be deterministically derived from paper-level PFSD mappings, not typed independently.

Resolve the taxonomy conflict between `LCSA + outranking` and `Hybrid MCDM` before freeze. The mat-foundation paper is specifically LCSA + NAHP-G + ELECTRE IS; retaining both mechanism categories while coding that paper only as Hybrid MCDM creates an empty/redundant LCSA+outranking column.

## 17. Evidence passage quality

Use complete sentences/paragraphs rather than arbitrary character-window snippets. Preserve original wording; do not paraphrase exact-passage fields.