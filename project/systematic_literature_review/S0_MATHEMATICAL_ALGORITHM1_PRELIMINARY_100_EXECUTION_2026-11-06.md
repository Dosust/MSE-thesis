# S0 Algorithm 1 — rigorous title/abstract decision pipeline (6 November 2026)

## What executed
- Source SHA-256 verified: `4e2bfdb7d38759f3e7b6d12e1b2ea1244e7263c1901a713db1d1048640bdde50`.
- Original S0 5,662 EID-unique bibliographic records and 45 original Scopus fields read, fixed random 100 re-identified and re-replayed with seed `20261105` and exact source row order.
- All 100 original EIDs, titles and records preserved; 30 targeted challenge records separate and excluded from random precision calculation.
- Reproducible **assistant-only / nonhuman** title-abstract evidence assessment completed: 3 CORE_CANDIDATE, 12 SUPPORTING_PHYSICS, 10 SUPPORTING_METHOD, 29 SUPPORTING_SERVICE, 12 BACKGROUND_CONTEXT, 25 provisionally EXCLUDE, 9 UNCLEAR. **Not** human eligibility, confirmed full-text inclusion, search precision or approved reviewer agreement.
- Each nonhuman record has an abstract evidence excerpt, a proposed scientific reason, Q1 physical interface / Q2 transferable physics or method / Q3 service diagnostic, candidate SO annotations, an evidence limitation and a full-text action.
- Current 25-paper independent human calibration: **0/25 paired**; no κ and no signed codebook. Formal random100 human screen: **0/100**. Calculations of κ, reconciliation and Wilson precision are programmed to block without human decisions/signoff. Do not fabricate two human reviewers.

## Reviewer-controlled mathematical methods
- For reviewer r on paper i: evidence vector in {-1,0,+1}^3; conditional decision INCLUDE / EXCLUDE / UNCLEAR; scientific role independent from decision; source evidence and reason code required; every paper exactly one decision.
- Calibration: Po=matches/25; Pe=sum_c n_{1c}n_{2c}/25^2; kappa=(Po-Pe)/(1-Pe), when defined, only from 25 independent complete human pairs.
- Formal 100: both independent complete forms, signed final codebook, source-EID exact matching, documented disagreement resolution.
- Precision only after all 100 human adjudications: (CORE+SUPPORTING)/100; two-sided Wilson 95% CI. BACKGROUND and targeted30 are outside numerator; does not establish recall or completeness.
- Full-text equation-level extraction is intentionally **not initiated** until screening eligibility permits it.

## Artifacts (researcher-only, not shared with blinded reviewers)
- [Private Drive assistant-only workbook](https://docs.google.com/spreadsheets/d/1IavaDHWu7zDaezXEBFXvzUZaL9a8yhBc/edit)
- [Private Drive assistant-only CSV](https://drive.google.com/file/d/1s3_Mr5yojcmZJVvfRSCIdnC9KYuaHGYl/view)
- [Mathematical protocol](https://drive.google.com/file/d/1GlZ1j8hVCzltpDL-zCbGT5WQlHDTMKvr/view)
- Workbooks R1/R2 remain untouched and blinded; proposed codebook v0.4 **NOT FINALIZED**.
- Local Python executable `s0_mathematical_screening_pipeline.py` and verified ZIP are delivered in the associated chat; no raw Scopus records are committed to GitHub.

**Scientific authority:** Existing v0.3 researcher-approved JBI-guided working protocol, not a claim of final supervisor signoff. No frozen SO1–SO3 authority edited.
