# User Request / Prompt History — Current Review Thread

This file preserves the intent of the major requests made in the current chat so future sessions can reproduce the direction of work. It does not attempt to reconstruct messages that are unavailable verbatim.

## Core recurring request

The user repeatedly requested a review system with **high rigor**, explicit mathematics, machine-readable logic, reproducibility, and no guessing. The goal is not only to classify papers but to preserve enough evidence that the user can independently read and validate the interpretation.

## Major requests preserved from the thread

### Original K–T interpretation

The user supplied the supervisor-style instructions defining K–M screening and N–T detailed extraction and asked for explanation and rigorous application.

### Eligibility algorithm

The user asked for the full algorithm, mathematical formulas, logic, conjunctions, tiers, and later a route-based non-compensatory design. The user explicitly preferred maintaining hard scientific requirements rather than lowering thresholds simply to hit a target number of papers.

### Core/extended evidence design

The user explored how to broaden from a small core set to about 30 papers while preserving rigor. The preferred logic became explicit routes (Tier A/B1/B2/B3) rather than a compensating total-score threshold.

### Example workbook learning

The user provided a bio-inspiration workbook as an example and asked the assistant to read each sheet rigorously, understand how it was organized, and combine the best insights with the construction-sustainability review algorithm.

### Matrix / mathematics / algorithm / dynamic diagram

The user repeatedly asked to design:

- the matrix;
- mathematical formulas;
- logic and conjunctions;
- the algorithm;
- a dynamic process/state diagram;
- detailed descriptions of each state/step;
- an A3 well-organized design.

### Python implementation

The user asked for full high-rigor Python code implementing the framework and later asked to translate the complete methodological specification directly into a modular Python program.

### Plugin idea

The user asked whether a ChatGPT plugin could be created for the framework. This remained conceptual; the main executable artifact developed was the modular Python framework.

### Perfect-score clarification

The user challenged statements about whether perfect-score papers had actually been identified. The conversation distinguished the framework-only run from paper-level audits, then updated the evidence state from 40 provisional perfect candidates to 31 after second review.

### Top-10 reference papers

The user decided to work with 10 chosen papers and asked that the algorithm, matrices, mathematics, logic, and workbook structure be adapted specifically to those papers while still preserving the general methodology.

### PFSD central chain

The user emphasized and accepted the chain:

$$
P_{engineering}\rightarrow F_{integration}\rightarrow S_{sustainability}\rightarrow D_{decision}.
$$

The user then asked what keywords/concepts should be searched under each element.

### Detailed boundaries

The user requested that every element be defined “as detailed as much as possible and clear about the boundaries and scopes well for each elements.” This led to the frozen data dictionary, scope rules, evidence states, method-specific R2, traceable alternative correspondence, and lambda boundaries.

### Full algorithm to Python

The user asked for the “full algorithm which will lead to Python code” with maximal accuracy and explicitly requested no guessing/errors. The response therefore adopted a fail-closed source-supported-claim policy rather than claiming literal infallibility.

### Workbook verification

The user uploaded `Top10_Engineering_Sustainability_High_Rigor.xlsx` and asked for verification and judgment. The workbook was judged strong but not yet fully frozen; specific corrections were identified in the decision log.

### New preferred evidence format

The user then clarified: **“I prefer a lot about extracting the full content as it was write and put and I will design by myself how I understand.”**

This is the most important current preference. It changes the implementation priority from compact summary-first extraction to a full evidence dossier:

$$
Raw\ Evidence\rightarrow Interpretation\rightarrow Scoring\rightarrow Synthesis.
$$

The final Top-10 database should therefore preserve full relevant source passages, locations, equations/tables/figures, and multiple P/F/S/D records per paper before reducing them to summaries.

### GitHub reproducibility request

The latest request is to double-check errors and put all useful information from the chat into a GitHub folder so future chats can recover the full methodological memory with high rigor and reproducibility. This archive is the result.

## Current instruction priority

If future instructions conflict with earlier compact-workbook designs, the latest evidence-first preference takes priority unless the user explicitly changes it:

> Preserve what the papers actually wrote first; let the user independently design/validate the interpretation afterward.