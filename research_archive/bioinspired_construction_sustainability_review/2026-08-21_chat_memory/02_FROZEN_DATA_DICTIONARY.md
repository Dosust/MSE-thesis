# Frozen Version 1.0 Data Dictionary

The 10-sheet schema is frozen. Do not add/remove/change columns simply because a later paper is difficult. Use `Other`, `U`, `NR`, `NA`, or an audit note first. Schema changes require an explicit protocol revision.

## 00_Control

Stores:
- version;
- corpus rule;
- RQ1–RQ5;
- evidence states;
- review states;
- linkage states;
- validation levels;
- controlled performance/input/outcome vocabularies.

## 01_Papers

One row per eligible focal paper.

Core fields:
- `Paper_ID`
- `Original_Corpus_ID`
- `Authors`
- `Title`
- `Year`
- `Journal`
- `DOI`
- `Document_Type`
- `Corpus_Source`
- `Full_Text_Source`
- `Full_Text_Status`
- `Identity_Status`
- `Eligibility_Status`
- `Review_Status`

## 02_Assessment_Tools

One row per directly implemented sustainability assessment method/component.

Core fields:
- `Tool_Record_ID`
- `Paper_ID`
- `Tool_Name_As_Written`
- `Tool_Acronym_As_Written`
- `Tool_Type`
- `Tool_Purpose_As_Written`
- `Directly_Implemented`
- `Application_or_Case`
- `Procedure_Summary`
- `Evidence_Summary`
- `PDF_Page`
- `Section`
- `Table_Figure_Equation`
- `Source_URL_or_File`
- `Evidence_Status`
- `Human_Review_Status`

Boundary: a background mention is not an implemented tool.

## 03_Tool_Inputs

One row per documented assessment input.

Core fields:
- `Input_Record_ID`
- `Paper_ID`
- `Tool_Record_ID`
- `Input_As_Written`
- `Input_Category`
- `Input_Value_As_Written`
- `Input_Unit_As_Written`
- `Input_Source_As_Written`
- `Input_Origin`
- `Author_Generated`
- `Engineering_Performance_Input`
- `Alternative_or_Scenario`
- `Evidence_Summary`
- `PDF_Page`
- `Section`
- `Table_Figure_Equation`
- `Reviewer_Notes`
- `Source_URL_or_File`
- `Evidence_Status`
- `Human_Review_Status`

Controlled input categories:
- Engineering
- Material
- Environmental
- Economic
- Social
- Geometric
- Operational
- Life-cycle
- Contextual
- Database/background
- Other

## 04_Engineering_Performance

One row per engineering/functional metric.

Core fields:
- `P_Record_ID`
- `Paper_ID`
- `Metric_As_Written`
- `Performance_Family`
- `Method_As_Written`
- `Method_Type`
- `Result_As_Written`
- `Value`
- `Unit_As_Written`
- `Alternative_As_Written`
- `Comparator_As_Written`
- `Author_Generated`
- `Evidence_Summary`
- `PDF_Page`
- `Section`
- `Table_Figure_Equation`
- `Source_URL_or_File`
- `Evidence_Status`
- `Human_Review_Status`

Controlled performance families:
- Structural
- Mechanical/material
- Thermal
- Energy
- Lighting/daylighting
- Durability/service-life
- Moisture/water
- Acoustic
- Ventilation/airflow
- Material efficiency
- Functional/serviceability
- Reliability/resilience
- Other

Do not replace the author's terminology with the controlled family.

## 05_Sustainability_Outcomes

One row per method-generated sustainability outcome/aspect.

Core fields:
- `S_Record_ID`
- `Paper_ID`
- `Tool_Record_ID`
- `Dimension`
- `Indicator_As_Written`
- `Result_As_Written`
- `Value`
- `Unit_As_Written`
- `Alternative_As_Written`
- `Functional_Basis`
- `Method_Generated`
- `Evidence_Summary`
- `PDF_Page`
- `Section`
- `Table_Figure_Equation`
- `Source_URL_or_File`
- `Evidence_Status`
- `Human_Review_Status`

Controlled dimensions:
- Environmental
- Economic
- Social
- Integrated

Critical rule: engineering metrics do not satisfy the sustainability-output requirement merely because they are numerically favorable.

## 06_Performance_Tool_Linkage

One row per candidate/verified engineering-to-assessment linkage.

Core fields:
- `Link_Record_ID`
- `Paper_ID`
- `P_Record_ID`
- `Tool_Record_ID`
- `S_Record_ID`
- `Engineering_Variable_As_Written`
- `Tool_Input_As_Written`
- `Transformation_As_Written`
- `Sustainability_Target_As_Written`
- `Alternative_Linkage`
- `Evidence_Summary`
- `Preceding_Context_Summary`
- `Following_Context_Summary`
- `PDF_Page`
- `Section`
- `Equation_or_Figure`
- `Source_URL_or_File`
- `Candidate_Linkage_Type`
- `Final_Linkage_Type`
- `Evidence_Status`
- `Human_Review_Status`

Linkage states:
- L0 no demonstrated connection
- L1 parallel/coexisting evidence
- L2 direct engineering input/modifier to sustainability assessment
- L3 explicit integrated evidence-to-decision architecture
- U unresolved

## 07_Validation

One row per validation claim.

Core fields:
- `Validation_Record_ID`
- `Paper_ID`
- `Validation_Target`
- `Validation_Method_As_Written`
- `Validation_Result_As_Written`
- `Validation_Level`
- `Evidence_Summary`
- `PDF_Page`
- `Section`
- `Source_URL_or_File`
- `Evidence_Status`
- `Human_Review_Status`

## 08_Paper_Interpretation

Derived, human-reviewed paper-level synthesis. Do not use it as a raw evidence source.

Fields summarize:
- assessment tool;
- principal inputs;
- engineering evidence;
- environmental/economic/social/integrated outcomes;
- engineering-to-sustainability linkage;
- strengths;
- weaknesses;
- evidence gaps;
- reviewer conclusion;
- interpretation status.

Direction of derivation:

`Sheets 02–07 -> Sheet 08`

not the reverse.

## 09_Audit_Log

Every correction, unresolved claim, legacy conflict, source limitation, or schema/version event is recorded here.

Core fields:
- `Audit_ID`
- `Paper_ID`
- `Audit_Date`
- `Affected_Record`
- `Issue_Type`
- `Original_State`
- `Corrected_State`
- `Reason`
- `Evidence_or_Source`
- `Reviewer`
- `Status`

## Numerical integrity

Never silently:
- convert units;
- round values;
- convert ratios to percentages;
- infer denominators;
- infer functional units;
- infer missing comparator values.

Preserve the original value/unit string and add any later derived quantity in a separate explicitly reviewer-derived field if the protocol is extended.