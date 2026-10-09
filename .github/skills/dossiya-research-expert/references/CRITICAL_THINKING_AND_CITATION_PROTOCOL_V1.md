# Dossiya Research Expert — Critical Thinking and Citation Protocol V1

**Status:** Active skill guidance; subordinate to the canonical scientific authorities.
**Effective:** 2026-10-09
**Mode:** Applies on demand to research analysis, literature reading, model evaluation, mechanism qualification, thesis decisions, and scientific writing. It is not a frozen scientific finding or a lesson plan.

## Purpose

Produce answers that could withstand a skeptical engineering thesis examination. Use references to **test claims**, not decorate them. Ask what would falsify a conclusion and distinguish evidence that a mechanism exists from evidence that a selected implementation predicts it accurately.

## Mandatory authority and source discipline

First load `AI_RESEARCH_INSTRUCTIONS.md`, `project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md`, `project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md` and `thesis/00_governance/THESIS_CITATION_AND_REFERENCE_STANDARD_V1.md`; follow all other relevant active thesis authorities. Frozen objectives, system composition and scope remain unchanged.

Every substantive **external** physics, mathematical-model, empirical, normative or literature claim must have an immediately adjacent **verified** source with APA 7 author–date attribution in academic text. Check author names, year, actual title, DOI, edition, claim location, study boundaries and exact evidence before citation. Do not infer equations or findings from an abstract; record full-text status. When a source is inaccessible or claims cannot be checked, state `[OPEN — full-text/source verification required]`. A search snippet, secondary summary or an attractive bibliography is not validation.

Use provenance per claim: `[A1]` standard; `[A2]` exact equipment document; `[A3]` empirical experiment; `[A4]` peer-reviewed model; `[A5]` established theory; `[T1]` transparent thesis derivation; `[OPEN]` not established. An internal GitHub authority can support a scope or definition, **not an external physical finding**.

## Eleven critical-thinking tests — apply selectively, not mechanically

1. **Precisely frame the unknown.** Identify physical systems, service, operating horizon, research question and the required decision. Separate topic, context, scientific problem and empirically supported literature gap.
2. **Disaggregate claims.** Separate observed measurement, theoretical assumption, standard requirement, mathematical inference, model output, validation result, and proposed thesis synthesis.
3. **Physical conservation.** Check units, energy and power boundaries, heat generation versus transferred electricity, loss accounting, cooling, rated versus delivered power and feasibility.
4. **State semantics.** Distinguish exogenous heat forcing, internal state, capability/constraint, actual interface flow, control/action, degradation, service output, resilience and sustainability. A changing variable is not automatically a dynamic state.
5. **Direction and alternative explanations.** For each P→T_e or T_e→P thermal dependency identify source state/condition, interface transfer law, receiving change, measured outputs, alternative shared-heat explanation, and a counterfactual test. Neither an electrical connection nor simultaneous heating proves thermal propagation.
6. **Exact law and limits.** Locate each constitutive relation and operational limit in the correct standard clause, manufacturer document or independently evaluated study. Do not invent thermal derating, emergency curtailment or shutdown from a temperature crossing.
7. **Mathematical properties.** Evaluate well-posedness, initial/boundary conditions, continuity/constraint switching, physical admissibility, observability, identifiability and parameter correlation **where materially relevant**. Do not falsely imply that a generic DAE is validated.
8. **Time attribution.** Distinguish thermal constant, first threshold crossing, source activation, interface-effect onset, receiver response, propagation delay, service disruption, and recovery. Delay requires defined triggering event and causal attribution, not two correlated timestamp peaks.
9. **Evidence transfer.** Check exact equipment architecture, cooling mode, climate, charger class, fleet/service boundary, observation location, sample size and uncertainty before transferring a published parameter or empirical curve.
10. **Challenge strongest prior art.** Identify closest papers that could already resolve the claim. Compare their equations, physics, state/forcing distinction, services, experiments and independent validation. State overlap and rival hypotheses. Never declare novelty from missing mentions or abstract-only search.
11. **Verification, validation and sensitivity.** Separately evaluate implementation/solver verification, parameter calibration, independent predictive validation, uncertainty quantification and decision sensitivity. Model complexity or altered simulation outputs alone do not establish greater accuracy.

## Evidence extraction record for each studied paper

Record: bibliographic identity + persistent access + full text accessed yes/no + question + system boundary + source and receiver + forcing + states and units + exact equation number/page and source + assumptions and constitutive laws + state-to-capability mapping + exchange + service definitions + case data and parameter origins + experimental protocol + validation and uncertainty + real limitations + strongest overlap with thesis + transferability verdict (`ADOPT/ADAPT/TEST/COMPARE/EXCLUDE/OPEN`) + SO1/SO2/SO3 relevance.

When a source claims a result numerically, report only numbers checked in the primary paper, together with conditions and denominator/unit. Do not report a fit statistic as causal identification or validated transferability.

## Research answer output — concise by default

For a substantive research assessment, use only the necessary sections:
- **Scientific question and boundary**
- **Verified evidence with adjacent citations**
- **Physical / mathematical reasoning** (classify equations as A1–A5, T1, OPEN)
- **Most serious competing explanation or disconfirming test**
- **Verdict:** ESTABLISHED / SUPPORTED FOR SOURCE DOMAIN / CANDIDATE / OPEN / EXCLUDED
- **Exactly what observation or source would change the verdict**

Avoid false precision, unsupported scoring, invented thresholds, extensive generic mathematics, lecture/quiz unless expressly requested.

## Thesis-specific qualification example

**Question:** Do falling EVSE charging power and transformer temperature during the same extreme-heat period demonstrate a T_e→P thermal interdependency?

**Answer:** No. `[T1: causal interpretation]` The shared forcing and independent charger derating can explain parallel changes. To qualify T_e→P, establish that EVSE-delivered/requested power changes transformer electrical loading, and that this load change affects transformer thermal evolution under matched heat forcing. Verify calibrated or measured electrical quantities, an applicable transformer loss/thermal model, time ordering and a causal/counterfactual comparison; exclude alternative load and control changes. State-to-capability P→T_e requires a **separate** documented limit and actual curtailed flow. Those source-specific laws remain OPEN until evidenced.

## Anti-fabrication release gate

Before release, inspect each external scientific sentence and each equation: **Does the adjacent citation support precisely this mechanism, equipment, operating range and strength of claim?** If not, weaken, qualify, omit or mark OPEN. Every intended final freeze also requires `project/RESEARCH_DECISION_AND_FREEZE_PROTOCOL_V1.md` and authorized evidence. This protocol does not itself freeze research questions, state vectors, laws, paper selections, models or outcomes.
