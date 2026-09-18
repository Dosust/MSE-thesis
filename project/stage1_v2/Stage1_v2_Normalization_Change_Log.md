# Stage 1 v2 Normalization Change Log

| Change ID | Normalization / Correction | Reason | Affected Sheets | Final Rule |
| --- | --- | --- | --- | --- |
| CH-01 | Replace spatial x_i with r_i | Avoid collision with dynamic-state notation. | Evidence Register; Ontology Synthesis | r_i = spatial geometry; X_P/X_T/z_I/z_O/Y(t) = states. |
| CH-02 | Separate Stage-1 structural existence from Stage-2 causal acceptance | Prevents Stage 1 from using ACCEPTED CAUSAL terminology. | Ontology Synthesis; Relation Register; Vocabulary | I_e^struct ∈ {TEMPLATE_ONLY,CANDIDATE,VERIFIED_STRUCTURAL,UNRESOLVED,EXCLUDED}. |
| CH-03 | Adopt core relation object + secondary metadata | Keeps relation object interpretable while retaining hierarchy/path/arity/resolution/governance. | Ontology Synthesis; Relation Register | 𝔯_e^(1) core + a_e metadata. |
| CH-04 | Resolve Γ notation collision | Γ was being used both as interface and structural predicate. | Ontology Synthesis; Evidence Register | Γ_e^str = structural admission; γ_e = interface semantics. |
| CH-05 | Separate existence, strength and confidence | A relation can be well-evidenced without known coupling magnitude. | Ontology; Relation Register; G1 | Structural existence ≠ w_e ≠ q_e^evid. |
| CH-06 | Forbid Stage-1 coupling-strength estimation | Strength belongs after mechanism/case qualification. | Relation Register; Vocabulary; G1 | Strength_Status = NOT_ESTIMATED_STAGE1. |
| CH-07 | Make scope, hierarchy, path, arity and resolution explicit | Prevents hidden abstraction changes and forced pairwise edges. | Ontology; Relation Register | σ_e, h_e, π_e, κ_e, ℓ_e are explicit. |
| CH-08 | Generalize case wording | Workbook is a reusable framework, not Greensboro/Austin-specific. | Evidence Register; Relation Register | Case examples are downstream instantiations. |
| CH-09 | Retain common-cause hazard as context | Shared exposure is not P→T/T→P dependency. | Ontology; Relation Register; G1 | η→P and η→T are CONTEXT/common cause. |
| CH-10 | Compress freeze governance to six scientific G1 gates | Improves interpretability while retaining machine subchecks. | G1 Freeze Criteria | G1-B/E/I/R/P/C are top-level gates. |
| CH-11 | Add controlled vocabulary and data-validation-ready statuses | Prevents ontology drift across case records. | Controlled Vocabulary; Relation Register | Use controlled values only. |
| CH-12 | Preserve canonical authority while adding operational Z1 projection | Avoids silent replacement of existing thesis authority. | Ontology Synthesis; README | Z_1^op is an evidence/ontology projection, not silent canonical replacement. |

## Final decision

All normalization changes required before declaring `Stage1_Evidence_and_Ontology_Register_v2` authoritative have been applied. The workbook is **PASS — READY FOR FRAMEWORK FREEZE**. Case-specific relation records remain downstream instantiations and do not alter this generic authority.
