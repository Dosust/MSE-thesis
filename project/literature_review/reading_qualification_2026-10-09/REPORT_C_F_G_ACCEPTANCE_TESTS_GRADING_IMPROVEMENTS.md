# Dossiya Research Expert v1.3 — Acceptance Test Execution, Grading and Improvements
**Date:** 2026-10-09 | **Scope:** real uploaded PDFs plus constructed falsification inputs | **Verdict:** NOT YET QUALIFIED for independent universal scientific-review certification. This is an **internal self-audit**, not an external blind evaluation.
**Protocol:** `.github/skills/dossiya-research-expert/references/SCIENTIFIC_READING_ACCEPTANCE_TESTS_V1.md`. Never count a test as pass because its requirements are understood; evaluate executed response against a concrete source. Source citations use uploaded PDF page/eq/fig as specified in companion REPORT_A_B_D_E.

## C — T01–T18 execution ledger
**PASS = actual reading/calc/check conducted and recorded. BLOCKED = required input/source/test unavailable; no invented result.** 
| Test | Actual input and action, observed output | Verdict / justification | Improvement |
|---|---|---|---|
| T01 abstract-only paywall | Five uploaded PDFs are all available as full PDFs; no real abstract-only inaccessible source supplied in this evaluation. | BLOCKED — cannot claim real paywall handling demonstrated. | Include genuinely restricted source in blind test; record ABSTRACT_ONLY. |
| T02 review mechanism | Oladigbolu 2025 PDF pp.1–2 and p.4 Table 1; classified EV/power dependencies as secondary review and explicitly withheld independent equipment thermal validation. | PASS, focused source-vs-primary distinction. | Trace cited primary study in full next. |
| T03 common heating | Constructed transformer+charger heated by same ambient driver; wrote both thermal traces may correlate absent cross-transfer; directed thermal link remains OPEN. | PASS for constructed logical challenge; no field observation. | Use independent load intervention for actual case. |
| T04 DC output and AC side | Tamay source boundary and Li DC/AC scheduling context; reconstructed P_AC=P_DC+P_losses with complete boundary, said DC-only drop cannot quantify transformer AC loading. | PASS for boundary reasoning, NOT independently observed equipment. | Obtain synchronized AC/DC meter data. |
| T05 transformer threshold | Constructed case crossing a thermal rating but no specified trip/derate; declined to infer supply outage. | PASS as controlled logical test. | Locate manufacturer/protection law. |
| T06 RL state | Li 2024 PDF p.5 eq.(1), identified energy demand, renewables, time, parking time as decision state, not physical temperature. | PASS source-audited. | Verify state sufficiency for author's MDP. |
| T07 sign convention | Li PDF p.6 eq.(4); independent 10 kWh renewable and 20 kWh demand => written −10 kWh, positive grid import convention +10 kWh; flagged variable/sign ambiguity without declaring software wrong. | PASS mathematical toy audit; author's code not inspected. | Retrieve code and full convention. |
| T08 matrix series | Ayoobi PDF p.5 eq.(3); independent numpy 2×2 convergent case rho≈0.24495 and divergent-but-invertible diag(1.2,0.2) demonstrate rho precondition; distinguished expert weights from physical causality. | PASS mathematical demonstration. | Test actual paper matrices. |
| T09 2–4% gain | Li 2024 PDF p.1 abstract; reported gain bounded to author's Leicester experiment, random/priority comparators and renewable use metric; uncertainty details not extracted. | PASS for no universal transfer; detailed metric audit remains open. | Recover full metric and confidence/seed analysis. |
| T10 historical standards | Tamay PDF p.9 Table 4 and p.10 standards discussion; labeled as paper's 2020-era design/code context, not latest universally enforceable provision. | PASS. | Check official current jurisdiction/edition before deployment. |
| T11 fault simulation | Tamay p.1 abstract; treated PowerFactory fault scenarios as simulation, not measured heatwave validation. | PASS. | Obtain physical heat-exposure tests. |
| T12 mathematical theorem paper | None of supplied five is a standalone original rigorous theorem/proof paper; constructed matrix example is not equivalent to source-level theorem audit. | BLOCKED. | Test with fully accessible mathematical proof and adversarial gap. |
| T13 qualitative interview | None of supplied five is interview-based qualitative research. | BLOCKED. | Add real qualitative methods+findings paper. |
| T14 disagreeing sources | Compared incompatible meanings of physical state (Li), influence (Ayoobi), infrastructure interface (Oladigbolu/Tamay); did not average or manufacture inconsistency. No directly contradictory same-QOI experiment supplied. | BLOCKED for genuine contradictory-evidence case; partial conceptual comparison. | Supply two directly conflicting results and reconcile units/methods. |
| T15 equation parser error | Uploaded Li PDF eq.(2) and Ayoobi eq.(3) visible-page text compared to extracted formula, including subscript/sign concerns; not a documented known corrupted parser case. | BLOCKED for targeted corruption-detection challenge. | Deliberately feed corrupted extraction alongside rendered page. |
| T16 26 candidates | Current repo 26 provisional paper candidates acknowledged, and this report says only five targeted audits, not 26 full-text equation audits. | PASS for correct evidence-status behavior. | Complete 26 audit by actual reading. |
| T17 unsupported hypothesis | Hypothetical transformer-state-to-charger-curtailment mechanism remains OPEN absent actual operating rule; no false current research validation. | PASS for scientific claim ceiling. | Acquire exact equipment operating policy. |
| T18 contradictory numerical output | Independently computed matrix with rho>1: inverse exists but series partial sum grows to ≈8812.63, overturning tempting inference that invertibility implies convergence; interpretation updated to require rho(B)<1. | PASS for concrete computed counterexample; no external independent blind evaluator. | Run separate blinded tool-result contradiction trial. |

**Tally: 13 PASS, 5 BLOCKED, 0 FAIL.** Passing challenge-based reading tasks does not certify broad scientific expertise; blocked tests remain mandatory if universal qualification is sought.

## F — Quantitative rubric: evidence-bounded score (one shared score)
| Dimension | Max | Earned | Basis / unreached evidence |
|---|---:|---:|---|
| Source authenticity and accurate reading |15|12|Five uploaded primary PDFs identified and key pages checked; no full DOI/erratum/supplement audit |
| Problem and methodology reconstruction |10|8|Five paper categories, method aims, contexts reconstructed; limited secondary-section depth |
| Mathematical equation verification |15|9|Li energy interval and sign toy check; Ayoobi spectral-radius counterexample; not every load-bearing equation/proof |
| Causal reasoning and alternatives |15|12|Common forcing, AC/DC, thermal trip, DEMATEL-vs-physics challenges demonstrated |
| Evidence/inference separation |15|13|Source vs reasoning labels, holdouts and claim ceilings |
| Validation, uncertainty, limitations |10|6|Clear conceptual separation; no source case raw data or empirical replication |
| Cross-paper synthesis/transfer |10|8|Compatible and incompatible roles mapped; no proven original thermo-coupling |
| Human verification and reproducibility |5|4|Specific checkable follow-up procedures; code outputs exist for two toy numerical checks only |
| Transparency/scientific integrity |5|5|Explicit blocked tests, self-audit, source scope and no fabricated numerical findings |
| **OVERALL** |**100**|**77**|**Internal, provisional evaluation of executed reading performance only** |

**Paper-wise audit scores (diagnostic out of 100; NOT averaged or used for overall rubric):** Oladigbolu **72** (review only, no primary recheck); Tamay **75** (code/standards transfer unverified); Li **82** (real eq sign/energy checks, no code replication); Shin **73** (framework extraction only, no independent implementation); Ayoobi **84** (real matrix counterexample, paper data unreconstructed). These measure **this audit's verified analytical depth and integrity**, not the papers' intrinsic quality.

**Scoring limitation:** Because evaluated by the same assistant performing the tests, the score is not independent calibration and may be optimistic; external reviewers should blind-grade the artifacts.

## G — Required skill improvements from observed blockers
- Add a **real restricted/paywalled source** for T01.
- Add a **real proof-bearing pure mathematics paper** for T12; test hypothesis and logical derivation line-by-line.
- Add a **real interview-based qualitative study** for T13 with coding, credibility and sampling checks.
- Add **genuinely conflicting measured outcomes** from comparable sources for T14; don't confuse varied scope with contradiction.
- Introduce a **known corrupted PDF equation extraction** for T15 and require page-image reconciliation.
- Add independent tool-result reversal prompt for stronger T18 challenge.
- Obtain study data/code where accessible and rerun author calculations.
- Preserve a machine-readable claim→PDF locator→interpretation→counterexample audit and future reviewer sign-off.

## Final classification
**NOT YET QUALIFIED** for the requested *universal, high-rigor independent scientific reading expert* because T01, T12, T13, T14 and T15 are BLOCKED; none may be silently counted as passes. This does not negate the demonstrably successful source audits and arithmetic/matrix tests.

**No protected frozen thesis scientific authority changed.** Report is an additive test artifact; GitHub merge, if any, certifies file inclusion only, not research correctness.
