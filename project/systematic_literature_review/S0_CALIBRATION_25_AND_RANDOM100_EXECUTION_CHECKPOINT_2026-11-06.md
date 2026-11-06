# S0 random-25 calibration and random-100 screening execution checkpoint
**Date:** 6 November 2026
**Source-of-truth:** Researcher-approved SLR protocol v0.3 on `user-data-qualification-2026-11-03`; not supervisor-approved, not fully operationally finalized. This file is an *additive, non-authority checkpoint*, not an amendment to frozen SO1–SO3.

## Validated source / sample
- Original S0: **5,662 unique Scopus EIDs**, verified original SHA-256 `4e2bfdb7d38759f3e7b6d12e1b2ea1244e7263c1901a713db1d1048640bdde50`.
- Fixed S0 random100 retained unchanged, seeded `20261105`; fixed targeted30 retained unchanged and must NEVER be pooled with random100.
- Previous 25-paper pilot is **enriched across five lexical groups** (5 per stratum), not uniform random; preserve as a separate stress test.
- **New disjoint reviewer calibration25** drawn by `random.Random(20261106).sample(...,25)` from the remaining **5,532 S0 EIDs**, excluding preselected random100 and targeted30; verified disjointness, unique EIDs, original Scopus title/EID membership. This is random *within the residual frame* and is only a reviewer agreement pilot; it is not a random100 replacement or a population precision sample.

## Operational calibration files (private in connected Drive)
- Reviewer 1 separate workbook (tabs START_HERE, Calibration_25, Screen_100): https://drive.google.com/file/d/1VX4yK4iNHjZxv0adKpUsDEGwtbU7RVPQ/view
- Reviewer 2 separate workbook (same individual blinded schema): https://drive.google.com/file/d/1Lf2DxjFqBZdUXxGqdX4yWApbMxvCbcru/view
- Proposed v0.4 operational codebook (not finalized): https://drive.google.com/file/d/13ckIJILAjMVPlq8EfPZjoHiTeShgJoXl/view
- All uploaded into the private `systematic review data` folder, metadata readback verified: same filenames, proper MIME types, **shared=false**. No R1/R2 identities or decisions were invented.
- The two reviewer workbooks include PREPARED but **BLOCKED** random100 tabs, until human pilot and rule signoff. They should be shared with each human reviewer *individually* only after access and blindness review.

## Verification / formal status
- Program `s0_calibration_and_screening_pipeline.py` generated the 25 and 100 read-only sample workbooks and CSV templates. Local verify: original hash PASS, unique 5,662 PASS, 130 original memberships PASS, 25 no-overlap PASS, ZIP export integrity PASS.
- Calibration agreement calculation executed with blank pilot reviewer templates: **0/25 paired human judgments**, Cohen's κ **NOT ESTIMABLE**, no disagreements adjudicated. Formal random100 screening analysis **refused** absent signed calibration approval, as designed.
- **Single assistant provisional title/abstract evidence pass** across the original random100: `54 ADVANCE`, `25 EXCLUDE_PROVISIONAL`, `12 CONTEXT`, `9 UNCLEAR`. This is **nonhuman, uncalibrated and explicitly researcher-only**; it is stored outside both blind human workbooks. **Not** S0 search precision, not two human reviewers, not a human inclusion count. Some marginal categories require rule clarification and full text; original source metadata remain unchanged.
- No numerical observed human agreement, human adjudication, Wilson search precision, or true reviewer-calibrated classification is available.

## Exact next scientific gates
1. Name/recruit two actual independent human reviewers (identities and conflict declarations); record dates and blindness.
2. Both review same separate random25 and return independent INCLUDE/EXCLUDE/UNCLEAR, reasons and evidence notes.
3. Calculate full 25/25 agreement and κ, adjudicate all differences, resolve open v0.3 eligibility ambiguities (minimum physical core connection, service-only, reviews/proceedings/retracted papers, EID/work identity, accessibility); document researcher/supervisor signoff of v0.4-final before formal sample screening.
4. Independently screen full fixed random100 with finalized rules, resolve conflicts and log full-text UNCLEAR decisions. Then calculate original 100 record-level search precision and Wilson 95% interval with fixed numerator definition.
5. Analyze 30 targeted challenge cases separately for S0 noise; do not mix with random 100 or formal pilot.

**Integrity:** No source Scopus raw bibliographic abstracts or full publisher records committed to GitHub. No frozen thesis authorities altered. All source/user Drive artifacts remain access-restricted; no automatic sharing was performed.
