# Visual Asset Contract — V1 (structural prototype)

**Producer:** Visual Source Agent supplies inspection/rights ledger; Composition Agent supplies graph/geometry/output; verifier checks the declared contract **without claiming physical, rights or rendered validation**.

Use the example `scripts/deck3_visual_asset_example.json`. Run:

```bash
python scripts/validate_deck3_visual_manifest.py scripts/deck3_visual_asset_example.json
python -m unittest discover -s scripts -p 'test_deck3_visual_manifest.py' -v
```

Required JSON keys:
- `asset_id`, `slide_number` (1..10), `presentation_variant` explicitly `TEN_SLIDE_MSE_TRAINING`, `main_message`, `three_bullets` (exactly three nonempty **authorized** strings), `visual_purpose`, `asset_only=true`, `whole_slide_screenshot=false`, `collage=false`.
- `source_mode`: `EMBED_REAL_PHOTO`, `ORIGINAL_SOURCE_GROUNDED`, or `NO_PHOTO_SCIENTIFICALLY_JUSTIFIED`. `references` array with each `url`, `provider`, `inspected` (bool), `rights_status` enum, `equipment_match` string and `visual_role` string; `embedded_real_photo_count` integer. Direct image embedding requires permission-verified reference and exact photo count. Original-source-grounded hardware requires at least one **declared inspected** photo and zero embedded pixels. No-photo abstract asset needs a nonempty `no_photo_reason`.
- `nodes` of declared `id/system`, and `arrows` with `id,type,source,target,evidence_status,label`; candidate arrows must stay visibly unqualified. The schema is NOT a full electrical simulator and does not itself certify that sources were actually viewed.
- `style` canvas/panel `#FFFFFF`, 16:9, font `Times New Roman`, 13-token `authored_colors`, `gradient=false`, `shadow=false`; ASU Gold limited to a specifically recorded small institutional accent.
- `outputs` PNG/SVG intentions as separate assets, `qa` statuses `NOT_RUN/OPEN/PASS/FAIL` for science, source rights, image render, actual Canva editability. No result may be marked independently verified from passing the JSON checker.

**Fail-closed checks:** unknown graph node/arrow; missing required output; incorrect P/T system membership; unqualified candidate missing `NOT YET QUALIFIED`; invalid color token; photo rights unknown while claiming real photo embedded; asset count collapsed into a collage; declaration of a future milestone as achieved.

**Limitations:** No online inspection, actual copyright assessment, physical laws, OCR/pixel tests, numerical verification, source authenticity, or Canva/PowerPoint app playback/editability are executed by this checker. Its decision is `STRUCTURE_ACCEPTED_NOT_SCIENCE_OR_RIGHTS_VERIFIED`.

Sources list is a **reference catalog only**; ASU/Canva/standards linked technical pages are not automatically licensed for reproduction.
