# Stage 6 v2.1 Reuse / Amendment Audit v1

**Date:** 2026-09-19  
**Purpose:** determine which Stage-6 v1 artifacts remain scientifically valid under the v2.1 intervention-performance amendment.

## 1. Audit conclusion

\`\`\`math
\boxed{
\text{Stage-6 v2.1 alignment}
=
\text{targeted normalization}
\neq
\text{full redesign}.
}
\`\`\`

The v1 package remains approximately 80% reusable. The required changes are concentrated in intervention-performance typing, H4 operational reporting, VVUQ, closure gates, handoff, workbook and freeze metadata.

## 2. Reuse decisions

| v1 artifact | Decision | Reason |
|---|---|---|
| \`01_scope/STAGE6_SCOPE_BOUNDARY_FUNCTIONAL_UNIT_V1.md\` | **REUSE UNCHANGED** | already distinguishes resilience effectiveness, resource efficiency, lifecycle boundaries and Stage-7 decision; no semantic conflict with v2.1 |
| \`03_accounting/STAGE6_SUSTAINABILITY_ACCOUNTING_PROTOCOL_V1.md\` | **REUSE UNCHANGED** | sustainability accounting remains a separate downstream consequence layer under v2.1 |
| \`04_requirements/STAGE6_REQUIREMENTS_DERIVATION_PROTOCOL_V1.md\` | **REUSE UNCHANGED** | requirement provenance, promotion and conflict logic remain valid; effectiveness targets reuse the same provenance discipline |
| \`STAGE6_EVIDENCE_REGISTER_V1.md\` | **REUSE AS BASE EVIDENCE REGISTER** | evidence still supports scope/accounting/method; v2.1 objects are thesis-derived operationalization and do not require pretending that the external sources define the thesis-specific EFX/EFY tuple |
| \`02_interventions/...V1.md\` | **SUPERSEDED FOR ACTIVE PERFORMANCE SEMANTICS** | contains useful baseline/resource-efficiency material but does not contain first-class \(\mathcal E_{\rm fx}\)/\(\mathcal E_{\rm fy}\) |
| \`05_benchmark/...V1.md\` | **SUPERSEDED BY V2** | lacks explicit EFX/EFY benchmark checks |
| \`06_H4/...V1.md\` | **SUPERSEDED BY V2** | H4 retained, but v2.1 performance fields must be reported explicitly |
| \`07_vvuq/...V1.md\` | **SUPERSEDED BY V2** | lacks dedicated EFX/EFY V&V gates |
| \`09_handoff/...V1.md\` | **SUPERSEDED BY V2** | passes \(\boldsymbol\eta_R\) but not complete \(\mathcal E_{\rm fx},\mathcal E_{\rm fy}\) |
| \`08_closure/...V1.md\` | **SUPERSEDED BY V2** | lacks \(G_{6-EFX},G_{6-EFY}\) |
| \`00_governance/...V1.md\` | **SUPERSEDED BY V2** | main chain jumps from intervention to resilience+sustainability |

## 3. Reuse firewall

Reusing a v1 artifact does not make it higher authority than the v2 constitution.

\`\`\`math
\boxed{
\text{v2 constitution}
>
\text{reused v1 supporting protocol}
}
\`\`\`

where a semantic conflict exists.

## 4. Evidence interpretation

The v2.1 intervention-performance distinction is a thesis governance/engineering operationalization. Existing external evidence supports the underlying accounting and systems-engineering domains, but does not by itself prove:

- any effectiveness threshold;
- any resource vector;
- any efficiency ratio;
- H4;
- any intervention ranking.

## 5. Data boundary

No case-specific value is introduced by this audit.
