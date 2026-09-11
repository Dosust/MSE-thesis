# FTEE v1.0 Save Record

**Date:** 2026-09-11  
**Repository:** `Dossiya-SE/MSE-thesis`  
**Source:** user-supplied `Pasted markdown(20260911-055828).md`  
**Canonical working file:** `project/FULL_TEXT_EVIDENCE_TO_EQUATION_EXTRACTION_PROTOCOL_FTEE_V1.md`  
**Protocol status:** PILOT-READY / NOT YET FROZEN

## Scientific preservation

The saved FTEE v1.0 retains the supplied methodology's core commitments:

- evidence-unit rather than paper-level extraction;
- exact source-location provenance;
- raw source notation before thesis canonicalization;
- R/C/T/P provenance classes distinct from `[E]/[D]/[P]` scientific status;
- mechanism extraction before equation extraction;
- separate mechanism, mathematical-form and validation evidence;
- equation extraction with variables, parameters, assumptions, bounds, IC/BC, domain and numerical procedure;
- dimensional/unit audit;
- parameter and timescale provenance;
- explicit assumption registry;
- VVUQ separation of verification, validation, calibration, sensitivity and uncertainty quantification;
- explicit validation referent and validation domain;
- uncertainty-source extraction;
- P–T–I–O transferability classification;
- mapping to $H_1$–$H_5$;
- duplicate extraction / disagreement resolution where feasible;
- explicit missingness codes;
- prohibition on silent equation completion;
- source extraction separated from thesis model synthesis;
- evidence-unit and governing-equation acceptance gates;
- the boundary that FTEE qualifies evidence but does not choose the demonstrator.

## Display normalization

The repository version uses GitHub-safe fenced `math` blocks, consistent second-level numbered headings, repaired Markdown tables, and Markdown equation labels instead of `\tag{...}`. These are presentation changes and do not alter the scientific protocol.

## Freeze boundary

FTEE v1.0 is **not frozen yet**. The supplied protocol explicitly requires the extraction table/codebook to be piloted on a deliberately heterogeneous subset of ranked papers spanning the five primary hypotheses and multiple model types. Ambiguities should be resolved and the codebook frozen before full-scale full-text extraction.

## Workflow position

```math
325\text{-paper closed-corpus ranking}
\rightarrow
H_1-H_5\text{ priority evidence set}
\rightarrow
\text{FTEE pilot/codebook freeze}
\rightarrow
\text{full-text extraction}
\rightarrow
\text{candidate demonstrator components}
\rightarrow
\text{candidate demonstrator architectures}
\rightarrow
\text{V\&V feasibility comparison}
\rightarrow
\mathcal M_D^*.
```
