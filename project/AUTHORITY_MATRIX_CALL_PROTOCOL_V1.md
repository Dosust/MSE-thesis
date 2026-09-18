# Authority Matrix Call Protocol v1

## Purpose

This protocol makes the regulatory and standards authority matrix a reusable governance control for the thesis.

## Canonical artifact

`project/governance/Regulatory_Standards_Authority_Matrix_Greensboro_Simple.xlsx`

## Call alias

```
@AUTHORITY-MATRIX
```

The alias means: consult the canonical authority matrix before making a standards-, regulation-, jurisdiction-, interface-, feasibility-, or stage-gate claim.

## Automatic call conditions

Call `@AUTHORITY-MATRIX` whenever a task involves any of the following:

- a thesis stage `S1-S7`, handoff object `Z1-Z7`, or gate `G1-G7` and an engineering requirement;
- ISO, IEC, IEEE, NERC, FERC, NCUC, FHWA/MUTCD, NCDOT, Duke Energy, North Carolina electrical requirements, or Greensboro implementation;
- power/transport interface admissibility, EV/EVSE, V2G, DER interconnection, traffic signals, distribution-system information exchange, or power automation;
- claims that an intervention is legally, technically, or operationally feasible;
- selection of service thresholds, risk criteria, continuity/recovery requirements, or asset-management decision criteria;
- any statement that a standard, code, regulation, utility procedure, or agency manual "requires", "governs", "permits", or "prohibits" something.

## Resolver logic

1. Identify the thesis locus: `S_i`, `Z_i`, or `G_i`.
2. Filter the matrix by Stage and Thesis Locus.
3. Apply authority precedence:
   ```
   Law / enforceable regulation
   > regulator / utility procedure
   > agency engineering manual
   > consensus / international standard
   > thesis scientific governance
   ```
   This is an applicability hierarchy, not a statement that scientific truth is determined by legal authority.
4. Check `Jurisdiction`, `Binding Status`, `Applicability`, `Edition / Status`, and `Exact Clause / Section`.
5. If the row is `CONDITIONAL`, prove that its jurisdiction and technical scope apply before using it as a constraint.
6. If a standard or regulation may have changed, verify the current official source before freezing a claim.
7. Preserve the scientific boundary:
   ```
   standard-defined interface
   != case-specific interdependency
   != scientifically validated causal mechanism
   ```
8. Return the applicable authority ID(s), document, clause, jurisdiction, and consequence for the thesis object.

## Evidence-status rule

- `CL-VERIFIED`: clause/section was checked against an accessible source.
- `SCOPE-VERIFIED`: official publisher/authority scope was verified, but detailed clause text was not fully available.
- `THESIS`: thesis-defined scientific or governance object.
- `MIXED`: combines external engineering authority with thesis validation/governance.

Do not silently upgrade `SCOPE-VERIFIED` to `CL-VERIFIED`.

## Scientific boundary

The matrix constrains architecture, interfaces, requirements, admissibility, and engineering decisions. It does not replace:

- evidence-grounded causal qualification in Stage 2;
- physics/hybrid dynamics in Stage 3;
- state-estimation mathematics in Stage 4;
- viability/reachability mathematics in Stage 5;
- intervention consequence models in Stage 6;
- the thesis optimization rule in Stage 7.

## Case-specific rule

For the Greensboro / North Carolina case, check the U.S. and North Carolina authority layer before relying on a general ISO/IEC/IEEE reference where a more specific legal, regulator, utility, or transport-authority requirement applies.

## Update control

Whenever a cited authority changes edition, legal status, effective date, or jurisdictional applicability:

1. update the workbook;
2. record the access date;
3. preserve the superseded row or version history where scientifically relevant;
4. update this protocol only if the call logic changes.

## Invocation examples

- "Use @AUTHORITY-MATRIX for Stage 1 EV/EVSE interfaces."
- "Use @AUTHORITY-MATRIX to test whether this Stage 6 intervention is feasible in North Carolina."
- "Before freezing G5, use @AUTHORITY-MATRIX to trace the service threshold to a legitimate requirement."
