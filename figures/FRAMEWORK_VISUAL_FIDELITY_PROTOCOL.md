# Framework Visual Fidelity Protocol

**Status:** Mandatory QA protocol for every figure representing the canonical 7-stage thesis framework  
**Authority:** [`../project/CANONICAL_7_STAGE_FRAMEWORK.md`](../project/CANONICAL_7_STAGE_FRAMEWORK.md)  
**Effective date:** 2026-09-09

---

## 1. Governing principle

```math
\boxed{ \textbf{CHANGE THE VISUAL HIERARCHY, NOT THE SCIENTIFIC CONTENT.} }
```

The purpose of visual design is to improve hierarchy, readability, information flow, and engineering communication. It is not permitted to silently alter the scientific framework.

---

## 2. Mandatory invariant checks

A candidate figure is acceptable only if **all** of the following pass.

### A. Stage identity

- [ ] Exactly seven canonical stages are represented.
- [ ] Stage names are verbatim.
- [ ] Stage order is exactly `1 → 2 → 3 → 4 → 5 → 6 → 7`.
- [ ] Stages 1–5 remain the resilience-analysis core.
- [ ] Stage 6 remains the resilience-to-sustainability translation interface.
- [ ] Stage 7 remains the sustainable-transformation endpoint.

### B. Roles and questions

- [ ] Every stage role is copied verbatim from the canonical table.
- [ ] Every main question is copied verbatim from the canonical table.
- [ ] No role is expanded, narrowed, paraphrased, or replaced without an approved framework revision.

### C. Mathematical objects

The only canonical mathematical hierarchy is:

```math
\boxed{ (\mathcal G,Y,Z) \rightarrow \mathcal C \rightarrow (Z,F,J,\tau) \rightarrow (\mathcal H_{\rm obs},\hat Y,I,O,\pi,u) \rightarrow (K,\mathcal V) \rightarrow R \xrightarrow{\mathcal T_{ST}} S }
```

- [ ] Symbols are reproduced exactly when shown.
- [ ] No additional symbol is presented as a canonical core object.
- [ ] No geometry-based object is reintroduced unless separately approved.
- [ ] Stage 6 preserves `R \xrightarrow{\mathcal T_{ST}} S` as the transformation bridge.

### D. Forbidden silent additions

Unless explicitly approved, a canonical framework figure must **not** add:

- SDG panels or SDG numbers;
- new equations;
- new variables;
- application examples;
- downstream-thesis-output panels;
- critical-interface or recovery-bottleneck claims;
- Stage-7 symbols such as `S_T,S_O,S_E,S_P`;
- new pathway categories;
- new interpretations or conclusions.

### E. Visual freedom that is allowed

The designer may change:

- layout;
- hierarchy;
- panel geometry;
- connectors;
- spacing;
- typography;
- color system;
- icons;
- visual grouping;
- visual emphasis;
- orientation;
- white space;
- figure aspect ratio.

These changes are acceptable only if Sections A–D remain invariant.

---

## 3. Deterministic production rule

For final thesis figures requiring exact wording, use a deterministic vector workflow such as:

1. Figma;
2. TikZ/LaTeX;
3. SVG/vector drawing;
4. another editable vector system with exact text placement.

Generative image models may be used for **visual exploration only** unless the final output is manually audited word-for-word against the canonical file.

---

## 4. Figure status labels

Every framework visual should be assigned one of these statuses during production:

| Status | Meaning |
|---|---|
| `CANONICAL-VERIFIED` | Passed every mandatory invariant check |
| `DRAFT-UNVERIFIED` | Design draft not yet audited |
| `ILLUSTRATIVE-NONCANONICAL` | Contains visual/scientific additions and cannot serve as framework authority |
| `SUPERSEDED` | Former representation replaced by a newer verified figure |

Only `CANONICAL-VERIFIED` figures should appear in the final thesis as the authoritative framework representation.

---

## 5. Audit record template

For each final figure, record:

```text
Figure file:
Source format:
Audit date:
Auditor:
Canonical source commit:
Stage identity: PASS / FAIL
Roles: PASS / FAIL
Questions: PASS / FAIL
Mathematical hierarchy: PASS / FAIL
No silent additions: PASS / FAIL
Overall status: CANONICAL-VERIFIED / DRAFT-UNVERIFIED / ILLUSTRATIVE-NONCANONICAL
Notes:
```

---

## 6. Current known non-canonical illustration

The previously generated framework illustration that introduced a downstream-output panel, SDG panel, extra application examples, additional Stage-7 symbols, and other unapproved content must be classified as:

```text
ILLUSTRATIVE-NONCANONICAL
```

It may be retained for design inspiration, but it must not be used as the scientific source of truth.
