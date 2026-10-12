# Deck3 evidence-preserving release contract — V1
Status: Proposed review-gate extension; does not replace canonical Deck3 palette, routing skills or existing QA policy.

## Source manifest required for each figure or deck
Each authored visual must identify: source file path and immutable commit; scientific claim IDs; GO/SO; component/ I1-I6 mapping; each arrow's physical meaning and epistemic label; equation/source authority; units; and SYNTHETIC / ANALYTICAL / OBSERVATIONAL / INDEPENDENTLY_VALIDATED provenance.
Use white canvas and panel interiors and exact currently approved repository palette. No unsupported causal arrows, unknown thresholds, invented sensor measurements, or unlabeled synthetic results.

## Acceptance gates
D0 source identity and scope verified; D1 math/content provenance checked; D2 directionality and evidence rendering checked; D3 figure and image visual inspection; D4 actual slide build / overflow / accessibility and editable asset check; D5 current baseline regression tests; D6 approved author/reviewer release.
Record PASS / FAIL / BLOCKED / NOT_TESTED for every gate and link to actual artifacts. Do not infer D4 from the presence of code or from image generation.
No asset is RELEASED unless D0-D6 are PASS with non-self-attested reviewer authorization.

## Initial acceptance report
D0-D6 = NOT_TESTED for this new governance package. Earlier Deck3 PR #69 reports CI and rendering gaps; no inference that these are fixed here.
