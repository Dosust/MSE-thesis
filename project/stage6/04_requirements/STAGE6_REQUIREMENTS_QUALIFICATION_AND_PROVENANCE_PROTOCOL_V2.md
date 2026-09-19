# Stage 6 Requirements Qualification and Provenance Protocol v2

**Status:** CANONICAL SUPPORTING STAGE-6 REQUIREMENTS PROTOCOL  
**Effective date:** 2026-09-20  
**Supersedes:** `STAGE6_REQUIREMENTS_DERIVATION_PROTOCOL_V1.md` for active framing.  
**RQ/SO/H authority:** `project/CANONICAL_RQ_SO_HYPOTHESES_V4.md`

## 1. Purpose

Stage 6 does **not derive normative requirements from resilience diagnosis or observed intervention outcomes**. It identifies where requirements are relevant, then qualifies candidate requirements from independent authority/evidence.

```math
oxed{
	ext{diagnosis identifies relevance;}
quad
	ext{authority/evidence establishes the requirement}.
}
```

and

```math
oxed{
	ext{observed consequence}

otRightarrow
	ext{normative threshold}.
}
```

## 2. Requirement object

```math
oxed{
r_q=
(
	ext{dimension},
	ext{metric},
mathcal R,
	heta_q,
	ext{unit},
FU_6,
mathcal B,
H,
	ext{beneficiary/perspective},
	ext{authority/provenance},
mathbb U_	heta,
	ext{applicability},
	ext{enforcement status}
).
}
```

A threshold is not promoted by model output.

## 3. Provenance classes

- **A — mandatory/authoritative:** applicable law, regulation, adopted code, binding agency/utility/contractual requirement, or directly applicable mandatory standard.
- **B — formally adopted stakeholder/organizational target:** documented and authorized for the declared case.
- **C — engineering/scientific benchmark:** literature, voluntary guidance, industry convention, or comparison target.
- **D — preregistered research threshold:** thesis-defined classification/sensitivity threshold.

Class C/D must not be silently represented as binding.

## 4. Hard-feasibility admission

A candidate requirement enters a hard Stage-7 feasibility set only if

```math
oxed{
G_{m auth}
land G_{m metric}
land G_{m scope}
land G_{m unit}
land G_{m uncertainty}
land G_{m applicability}
=PASS.
}
```

Otherwise it remains benchmark, target, report-only, sensitivity, BLOCKED, or NOT APPLICABLE according to evidence.

## 5. Typed requirement domains

Requirements may apply to service/resilience, physical/safety feasibility, resource quantities, implementation feasibility, or admitted sustainability consequences. Resource caps and sustainability constraints remain semantically distinct even when both affect Stage-7 admissibility.

## 6. Conflict audit

For hard admitted requirements (K_q),

```math
mathcal K_6^{hard}=igcap_q K_q.
```

If (mathcal K_6^{hard}=arnothing), report a requirement conflict. Do not invent weights to force feasibility.

## 7. Uncertainty and normative disagreement

Separate measurement/model/parameter uncertainty from normative/value disagreement. The latter is not converted to a probability distribution without a justified elicitation model.

## 8. Gate fields

Every active requirement record must contain: exact metric; relation; threshold or report-only state; unit; functional unit; boundary; horizon; beneficiary/cost bearer when relevant; provenance/authority class; uncertainty; applicability; rationale; conflict status; Stage-7 role; and verification/validation method.

## 9. Claim ceiling

Stage 6 may state that an intervention satisfies or violates a **declared qualified requirement** within the specified domain. It may not state that an intervention is globally sustainable or preferred.
