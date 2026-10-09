# Deck3 v1.8.0 — full-ecosystem mechanism-design update audit

**Request:** Install the scientific-design lessons from the user-provided IEEE Transactions on Smart Grid May 2024 p.3116 schematic throughout all Deck3 skills: mechanism-centered diagrams rather than decorative boxes; meaningful boundaries/variable-carrying arrows; physical vs simulation/data/optimization/evaluation separation; editable/revealable presentations; exact current colors and defensible scientific evidence.

**Update status:** **SOURCE_COMMITTED / STATIC_REPOSITORY_AUDIT_PASS / RUNTIME_TESTS_NOT_VERIFIED**. No changes to the thesis's frozen objectives, 13-token palette, existing presentations or previously generated standalone images. Existing assets do not acquire certification retroactively.

## Durable implementation

| Area | Applied | Evidence and limits |
|---|---|---|
| Main deck workflow | CHANGED | Deck3 v1.8.0 entry point loads `DECK3_MECHANISM_TRACEABILITY_STANDARD_V1.md`; new trace gate complements existing science/image/color/design controls |
| Scientific statements/citations | CHANGED guidance; APPROVED TEXT UNCHANGED | Define actual takeaway, evidence and bounded model; no unapproved new claims or frozen RQ/SO rewrites |
| Figure/AI prompt and source graphics | CHANGED guidance | Every essential arrow: endpoints, type, quantity/OPEN, law/operator/OPEN, evidence gate and provenance; user-provided IEEE graphic is inspiration only |
| Domain/system models | CHANGED guidance | Separate physical P/full T_e, active model, external forcing, simulation, observation/identification, control/optimization, service/assessment |
| Scientific arrows, symbols, mathematics | CHANGED guidance | No unnamed causal arrows, ungrounded reverse mechanism or inference of nonlinearity from Bézier curvature; label variables/units if defined |
| Editable vector and PPTX figures | CHANGED guidance | Native shape ID mappings to manifest; vector-first; white interiors, exact canonical sRGB and accessible projected labels |
| Animation | CHANGED guidance | Five optional semantic reveal layers, `Appear` on presenter click, prior elements persistent, reveal arrow with label/evidence |
| Stage 2 audit and Stage 3 assembly | **IMPLEMENTED** | `examples/mechanism_trace_qa.py` checks `<stem>.trace.json`; invalid supplied sidecar BLOCKS; no sidecar reports PROVISIONAL; structurally valid is NOT physics verified |
| Advanced PowerPoint module | CHANGED guidance | Retains previous numerical geometry/click tests; actual desktop playback not demonstrated |
| Unit and integration tests | **18 tests authored** | `tests/test_mechanism_trace.py` includes candidate bidirectional gates, invalid statuses/IDs, missing quantities and assembly integration |
| CI | **CONFIGURED, FAILED REMOTELY** | `.github/workflows/deck3-tests.yml` calls validator and new test file. Last inspected workflow run https://github.com/Dossiya-SE/MSE-thesis/actions/runs/37927528236 concluded failure; exact failed step/runner cause not verified. Do not report tests as passed |
| Root instructions / registry | CHANGED | Copilot instructions, global contract, technical annex, scientific diagram/infographic, mathematical and engineering-framework, writing/research and Advanced PPTX skill guidance synced |
| Legacy example image generators | CHANGED | Explicitly label output `SOURCE-ONLY` and unregistered rather than pretend automatic scientific verification |

## Scientific invariants retained

1. Shared extreme heat as external forcing is not itself a P↔T_e thermal coupling.
2. P→T_e and T_e→P require independent evidence; T_e→P uses a separate **grid-side AC** interface evidence gate, not DC output as a proxy.
3. State, capability, actual electrical transfer, electricity/mobility service, resilience and two downstream sustainability pathways remain distinct.
4. Numerical verification is not empirical validation; control and optimization are not constitutive physics.
5. A manuscript or project citation must support its specific claim. The IEEE image caption alone does not validate its scientific topology/parameters as applied to this thesis.
6. Exact 13 sRGB palette, ASU institutional exceptions, white surfaces, 70–80% effective meaningful-figure target and readable figures remain governed by earlier skills.
7. The full Electrified Transportation System T_e is not reduced to EVSE alone; model subset remains a separate explicit choice.
8. Conceptual generated images and diagram traces cannot themselves certify case-specific physics.

## Repository inspection

A read-back inspection confirmed **16 files** present, main SKILL.md version `1.8.0`, every linked skill contains the trace authority reference, validator is imported and called by Stage 2, missing-sidecar status is explicit, CI contains the CLI example, the ten-category dependency registry is preserved with new `M_mechanism_traceability` gate, and the conceptual example has **8 objects / 6 candidate arrows**. **18 tests are authored.** This was a **static content inspection**, not code execution.

## Tests / blockers / next validation

- Core Deck3/advanced/trace Python test suite on GitHub Actions: **NOT VERIFIED** (recent workflow failure; see existing runner issue #49; new failure cause not independently diagnosed).
- Desktop Microsoft PowerPoint slideshow and native reveal playback: **NOT VERIFIED**.
- Existing 10 AI-generated slide figures and older Chapter 1 PPTX: **UNCHANGED, NOT RETROACTIVELY CERTIFIED**. A rendered diagram can still have labels/citations/physics to correct.
- Automatic correspondence between sidecar object IDs and actual raster-visible shapes: **NOT IMPLEMENTED**. Requires independent visual source review, native shape mapping for editable designs and slide rendering.
- DOI, IEEE page, source title/authors and technical claims from the supplied figure: **NOT VERIFIED FROM ORIGINAL ARTICLE**. This standard does not use them as empirical thesis evidence.
- Effective 70–80% figure occupancy, projection readability, mathematical units and actual causal mechanisms: require case- and deck-specific review.

### Follow-up commands

```bash
cd .github/skills/deck3
python examples/mechanism_trace_qa.py examples/mechanism_trace_example.json
python -m unittest discover -s tests -p 'test_mechanism_trace.py' -v
python -m unittest discover -s tests -v
cd advanced_powerpoint
python -m unittest discover -s tests -v
```

Run on a checked-out repository with installed `python-pptx` and Pillow, and archive real results. Never label a PPTX fully Deck3-certified from these tests alone. The main workflow/CI is configured to run them when GitHub Actions can actually execute.
