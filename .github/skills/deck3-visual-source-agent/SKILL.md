---
name: deck3-visual-source-agent
description: Research and qualify real-world equipment photos, standards, icon sets and reusable visual assets before Deck3 Canva-ready illustration production; preserve actual inspection, licensing, provenance and device-specific physical validity.
license: MIT
metadata:
  version: "1.0.0"
  parent_skill: deck3
---
# Deck3 Visual Source Agent V1

**Role:** evidence-and-rights acquisition agent; NOT an image generator, experimenter or scientific-claim validator. Call before **every** individual real-equipment illustrative image or infographic. It produces an auditable per-image source ledger for the Composition Agent.

## Authority and trigger
Read, in precedence order, `AI_RESEARCH_INSTRUCTIONS.md`, `project/CURRENT_THESIS_AUTHORITY_INDEX_V1.md`, `project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md`, `.github/skills/deck3/references/DECK3_REAL_WORLD_REFERENCE_FIRST_LAW_V1.md`, `DECK3_INDIVIDUAL_CANVA_READY_ILLUSTRATION_PROTOCOL_V1.md` and `DECK3_SRGB_PALETTE.json`. Consult `DECK3_VISUAL_REFERENCE_RETRIEVAL_PROTOCOL_V1.md`. Maintain the 8-slide canonical, the 10-slide educational variant, and 13/14-slide working variants separately: never infer which slide deck to overwrite.

## A. Per-image sourcing procedure
1. Receive **exact slide ID and approved variant**, one scientific message and its **three actual bullet points**, the intended placement/visual question, selected real component IDs, and evidence status.
2. Search current online examples **for each item**, emphasizing actual inspected photographs from manufacturers, operators, engineers or user-owned photos; use technical manuals and peer-reviewed engineering figures to verify physical details, not photo appearance.
3. Record actual image viewed, owner/provider, inspected URL, equipment class/variant, what is visible, **what cannot be inferred** (relay settings, ONAN fan, feeder model, battery pack, control law), image author/date where known and connection with the three slide bullets. If inaccessible, set `inspection=NOT_RUN` — not INSPECTED.
4. Assess **image reuse rights independently of scientific use**. Explicit statuses: `PERMISSION_VERIFIED` (license/authorization recorded), `REFERENCE_ONLY` (not cleared for copying), `UNKNOWN`, `REJECTED`. CC licenses may require attribution and share-alike; manufacturer galleries are reference-only unless permissions are established. A branded product photograph is never evidence of site installation.
5. Classify intended use: `EMBED_REAL_PHOTO` only for an inspected image with compatible rights and accurate equipment; `ORIGINAL_SOURCE_GROUNDED` for independent illustrative art from an inspected source; `NO_PHOTO_SCIENTIFICALLY_JUSTIFIED` for abstract workflows, evidence tables, equations, service metrics or timeline images. If physical-photo count is zero, explain why.
6. Verify typography, brand and element rights: ASU logo must be a real authorized file, not AI-drawn; SVG icon sets must carry their own license and style compatibility. For licensed standardized IEC symbols, do not assume downloadable clipart rights.
7. Handoff candidate sources, **rights/equipment exceptions**, source attribution text, known physical features, uncertainty ledger and a signed-off source-selection method to the Composition Agent.

## B. Starting sources, NOT blanket licenses
See `references/DECK3_VISUAL_SOURCE_CATALOG_V1.json` (source status `REFERENCE_CANDIDATE`). Useful families: Hitachi transformer galleries; Eaton Green Motion commercial DC chargers; SEL-787 relay; MAHLE HVAC; EPRI OpenDSS real network test cases; IEC 60617 graphical symbols; NIST community-resilience guides; Font Awesome, Lucide, ASU official design, and Commons item-license pages.

## C. Mandatory evidence objects
Create one JSON manifest per standalone illustration using the Deck3 First Law template and the stricter `../deck3-scientific-composition-agent/references/VISUAL_ASSET_CONTRACT_SCHEMA_V1.md`:
- `source_id,url,provider,source_kind,inspected,rights_status,usage_mode,visual_role,physical_equipment_match,attribution`;
- `embedded_real_photo_count`; no-photo justification;
- trace every device appearance to a source **without upgrading its image to proof of a physical mechanism**.
An agent must not silently assert web inspection, permission or equipment-specific validity because a URL appears in a candidate library.

## Release criteria
**G-SRC1** actual inspection; **G-SRC2** device fit; **G-SRC3** permission/attribution; **G-SRC4** source-to-slide relevance; **G-SRC5** honest reuse-mode declaration. Missing necessary evidence => OPEN/PROVISIONAL and escalate; no substituted AI guesses or unlicensed copying. Do not claim final figure scientific validation from source inspection.
