## Deck3: repeatable scientific slide workflow

If the user invokes **Deck3 text**, **Deck3 figures**, **Deck3 figures slide N**, **Deck3 assemble**, **Deck3 all**, or numeric aliases **Deck3 1/2/3**, load `.github/skills/deck3/SKILL.md` and `references/WORKFLOW.md`. Stage 1 creates editable main-message/three-point text with genuinely empty infographic slots; Stage 2 creates separate scientific images and keeps their registers; Stage 3 inserts them without distorting images or changing frozen text/citations/notes and requires slide render QA. Missing source or figures are BLOCKED, not fabricated. Always obey all current scientific and in-text citation authorities.

# GitHub Copilot Instructions

Before producing or modifying scientific content in this repository, read and obey:

1. `AI_RESEARCH_INSTRUCTIONS.md`
2. `project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md`
3. `project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md`

Mandatory citation rule (2026-10-08): Load `thesis/00_governance/THESIS_CITATION_AND_REFERENCE_STANDARD_V1.md` §0A. No externally sourced substantive thesis statement anywhere (chat, slides, reports, figures, diagrams, math, code comments) without a visible adjacent verified in-text citation. Bibliography-only citations are insufficient. Cite frozen thesis-specific definitions via their canonical internal files; label proposed/T1/OPEN items accurately without false external attribution. Reject citation-mismatched or fabricated source metadata. Enforce a citation QA check on every deliverable.

Mandatory rule:

```text
Do not invent scientific evidence.
If it cannot be traced, it is not frozen.
If it cannot be verified, it remains OPEN.
If it is thesis-derived, label it T1 / thesis-derived.
If a result is transferred, justify transferability.
```

Permanent scope/terminology check (2026-10-08): read `project/CANONICAL_ELECTRIFIED_TRANSPORTATION_SCOPE_DEFINITION_V1.md` §4A. Use **System Boundary**, never **Boundary Condition**, when describing component membership. The external Power System is distinct. EVSE, charging connections, and required power-transfer communication/control are components of the broader Electrified Transportation System, never the entire definition or a third infrastructure. Preserve complete technical scope != bounded application != active model. Do not silently narrow the frozen system definition or assert unqualified P↔T_e thermal bidirectionality.

Never invent DOI metadata, standards, clauses, equations, thresholds, parameters, equipment ratings, material properties, validation results, or numerical findings. Apply the full current authority index for task-specific thesis scope and terminology.
