#!/usr/bin/env python3
"""Deck3: native-text scientific PPTX -> audited independent images -> final PPTX.

Requires python-pptx and Pillow; no web, invented model data, image generation,
font files, or graphical content embedded in the TEXT stage.

Commands: text | figures (asset audit) | assemble | all.
Scientific source/physics QA remains the responsibility of the scientific skills.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import zipfile
from pathlib import Path

from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.enum.text import MSO_ANCHOR
from pptx.util import Inches, Pt
from asset_color_qa import check_figure_source
from pptx_color_qa import check as check_pptx_colors

PALETTE_PATH = Path(__file__).resolve().parents[1] / "references" / "DECK3_SRGB_PALETTE.json"
with PALETTE_PATH.open(encoding="utf-8") as _palette_file:
    PALETTE = json.load(_palette_file)["colors"]


def token_rgb(name):
    r, g, b = PALETTE[name]["rgb"]
    return RGBColor(r, g, b)


WHITE = token_rgb("white")
INK = token_rgb("black")
NAVY = token_rgb("navy")
BLUE = token_rgb("blue")
GRAY = token_rgb("graphite")
FONT = "Times New Roman"
WIDTH, HEIGHT = 13.333333, 7.5


class Blocked(ValueError):
    """Required scientific or content input is absent; do not invent substitute."""


def load_manifest(path):
    path = Path(path)
    data = json.loads(path.read_text(encoding="utf-8"))
    slides = data.get("slides", [])
    if not slides:
        raise Blocked("Manifest must contain a nonempty ordered 'slides' array.")
    filenames = set()
    for n, row in enumerate(slides, 1):
        kind = row.get("kind")
        if kind not in {"title", "outline", "content", "references"}:
            raise Blocked(f"Slide {n}: unexpected kind {kind!r}.")
        if not isinstance(row.get("title"), str) or not row["title"].strip():
            raise Blocked(f"Slide {n}: missing title.")
        if kind in {"content", "outline"}:
            if not row.get("message") or len(row.get("bullets", [])) != 3:
                raise Blocked(f"Slide {n}: exactly one message and three points required.")
            if kind == "content" and not row.get("source_note"):
                raise Blocked(f"Slide {n}: source_note (citation / canonical attribution) required.")
            if row.get("layout", "standard") not in {"standard", "long_objectives"}:
                raise Blocked(f"Slide {n}: unsupported layout.")
        if kind == "references" and not row.get("entries"):
            raise Blocked(f"Slide {n}: complete reference entries required.")
        if "figure" in row:
            if kind != "content":
                raise Blocked(f"Slide {n}: figure slot only permitted on content slides.")
            figure = row["figure"]
            filename = Path(str(figure.get("file", "")))
            if filename.name != str(figure.get("file", "")) or filename.suffix.lower() != ".png":
                raise Blocked(f"Slide {n}: figure.file must be one PNG basename.")
            if not figure.get("alt"):
                raise Blocked(f"Slide {n}: figure alt text required.")
            if filename.name in filenames:
                raise Blocked(f"Slide {n}: duplicate figure filename.")
            filenames.add(filename.name)
    for objective in data.get("frozen_strings", []):
        all_content = "\n".join(str(s.get(k, "")) for s in slides for k in ("title", "message"))
        all_content += "\n" + "\n".join(x for s in slides for x in s.get("bullets", []))
        if objective not in all_content:
            raise Blocked("Frozen objective string not present verbatim: " + str(objective)[:100])
    return data


def put(slide, x, y, width, height, value, size, color=INK, bold=False):
    shape = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(width), Inches(height))
    frame = shape.text_frame
    frame.clear()
    frame.word_wrap = True
    frame.vertical_anchor = MSO_ANCHOR.TOP
    frame.margin_left = Inches(.005)
    frame.margin_right = Inches(.005)
    frame.margin_top = Inches(.01)
    frame.margin_bottom = Inches(.005)
    p = frame.paragraphs[0]
    p.text = str(value)
    p.font.name = FONT
    p.font.size = Pt(size)
    p.font.bold = bold
    p.font.color.rgb = color
    p.space_after = Pt(0)
    return shape


def slot_for(row):
    """A reservation in inches; not a drawn placeholder object."""
    if not row.get("figure"):
        return None
    if row.get("layout", "standard") == "long_objectives":
        return (8.65, 3.25, 4.02, 3.38)
    return (3.67, 2.05, 8.95, 4.91)


def usable_bounds(row):
    return (.70, 2.05, 11.92, 4.91)


def geometry_share(bounds, region):
    x, y, w, h = bounds
    rx, ry, rw, rh = region
    area = max(0, min(x+w, rx+rw)-max(x, rx)) * max(
        0, min(y+h, ry+rh)-max(y, ry))
    return area / (rw * rh)


def validate_slot(row):
    slot = slot_for(row)
    if slot is None or row.get("layout") == "long_objectives":
        return
    share = geometry_share(slot, usable_bounds(row))
    if not .70 <= share <= .80:
        raise Blocked(f"Figure slot occupancy outside 70–80%: {share:.3f}")


def make_text(manifest_path, output_path):
    data = load_manifest(manifest_path)
    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(WIDTH), Inches(HEIGHT)
    blank = prs.slide_layouts[6]
    for n, row in enumerate(data["slides"], 1):
        slide = prs.slides.add_slide(blank)
        slide.background.fill.solid()
        slide.background.fill.fore_color.rgb = WHITE
        kind = row["kind"]
        if kind == "title":
            put(slide, .80, .58, 11.7, .43, data.get("institution", "SCIENTIFIC PRESENTATION"), 16, BLUE, True)
            put(slide, .80, 1.55, 11.8, 2.4, row["title"], 35, NAVY, True)
            put(slide, .80, 4.65, 11.7, 1.0, row.get("subtitle", ""), 23, INK)
        elif kind == "references":
            put(slide, .75, .45, 11.8, .65, row["title"], 31, NAVY, True)
            entries = row["entries"]
            if len(entries) > 9:
                raise Blocked(f"Slide {n}: too many references; create another references slide.")
            for i, entry in enumerate(entries):
                y = 1.42 + i * (5.65 / max(1, len(entries)))
                put(slide, .81, y, 11.74, 5.05 / max(1, len(entries)),
                    entry, max(13, 18.0 - .7 * max(0, len(entries) - 4)), INK)
        else:
            figure = kind == "content" and bool(row.get("figure"))
            long = row.get("layout") == "long_objectives"
            put(slide, .69, .40, 11.95, .65, row["title"], 31, NAVY, True)
            # The manifest's message/bullet labels are editorial metadata, never audience copy.
            # Keep the substantive strings visible and native/editable; do not draw
            # the literal template labels "MAIN MESSAGE" or "THREE KEY POINTS".
            put(slide, .71, 1.30, 11.92, 1.32 if long else 1.18,
                row["message"], 18 if long else 21, INK)
            # Only a meaningful content hierarchy label is retained for objectives.
            if long:
                put(slide, .72, 2.85, 6.6, .26, "SPECIFIC OBJECTIVES", 12, BLUE, True)
            if figure and not long:
                validate_slot(row)
            starts = (3.17, 4.32, 5.48) if long else (
                (2.23, 3.77, 5.31) if figure else (3.13, 4.29, 5.45))
            for j, (y, bullet) in enumerate(zip(starts, row["bullets"]), 1):
                put(slide, .75, y+.04, .34, .33, f"{j:02}", 13, BLUE, True)
                bullet_width = (6.85 if long else 2.37) if figure else 11.1
                bullet_size = (15.2 if long else 14.3) if figure else (18 if long else 21)
                put(slide, 1.17, y, bullet_width, 1.37 if figure and not long else .99, bullet, bullet_size, INK)
            if row.get("source_note"):
                put(slide, .72, 7.04, 11.65, .22, row["source_note"], 10, GRAY)
        put(slide, 12.51, 7.04, .37, .25, f"{n:02}", 9, GRAY)
        try:
            slide.notes_slide.notes_text_frame.text = row.get("notes", "")
        except (AttributeError, ValueError):
            pass
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(out))
    reopened = Presentation(str(out))
    if len(reopened.slides) != len(data["slides"]):
        raise AssertionError("Slide count changed on save.")
    for s in reopened.slides:
        if any(x.shape_type == MSO_SHAPE_TYPE.PICTURE for x in s.shapes):
            raise AssertionError("A figure leaked into Stage 1.")
    print(f"PASS stage 1: {len(reopened.slides)} editable text-only slides, white reserved figure regions, {out}")
    return out


def figure_records(data, folder, slide=None):
    folder = Path(folder)
    records, missing = [], []
    for n, row in enumerate(data["slides"], 1):
        if slide is not None and n != slide:
            continue
        if not row.get("figure"):
            continue
        filename = row["figure"]["file"]
        source = folder / filename
        if not source.is_file():
            missing.append(f"Slide {n}: {source}")
            continue
        if source.suffix.lower() != ".png":
            raise Blocked(f"Slide {n}: PNG required for reliable PPTX composition.")
        try:
            with Image.open(source) as im:
                im.verify()
            with Image.open(source) as im:
                width, height = im.size
        except Exception as error:
            raise Blocked(f"Slide {n}: invalid figure PNG {source}: {error}") from error
        if width < 640 or height < 420:
            raise Blocked(f"Slide {n}: image below minimum 640×420 pixels.")
        source_color_qa = check_figure_source(source, row["figure"].get("source_kind"))
        if source_color_qa["status"] == "BLOCKED":
            raise Blocked(f"Slide {n}: authored figure source failed exact Deck3 palette gate: "
                          + "; ".join(source_color_qa["errors"]))
        records.append({
            "slide": n, "file": filename, "width_px": width, "height_px": height,
            "sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
            "alt": row["figure"]["alt"], "status": "ASSET_PRESENT_NOT_PHYSICALLY_VALIDATED",
            "authored_color_source_qa": source_color_qa,
        })
    if missing:
        raise Blocked("Figure assets required before assembly:\n" + "\n".join(missing))
    return records


def text_register(prs):
    return [[sh.text for sh in slide.shapes if sh.has_text_frame] for slide in prs.slides]


def notes_register(prs):
    return [s.notes_slide.notes_text_frame.text if s.has_notes_slide else None for s in prs.slides]


def assemble(manifest_path, text_pptx, figure_directory, output, qa_path=None):
    data = load_manifest(manifest_path)
    records = figure_records(data, figure_directory)
    # Native editable text, lines and backgrounds must pass before any figure is admitted.
    native_colors = check_pptx_colors(text_pptx)
    if native_colors["errors"]:
        raise Blocked("Stage-1 native PPTX has noncanonical authored colors: "
                      + "; ".join(native_colors["errors"][:12]))
    before = Presentation(str(text_pptx))
    if len(before.slides) != len(data["slides"]):
        raise Blocked("Input text PPTX does not match manifest slide count.")
    if any(sh.shape_type == MSO_SHAPE_TYPE.PICTURE for s in before.slides for sh in s.shapes):
        raise Blocked("Assembly input must be the Stage-1 text-only PPTX; image found.")
    old_text, old_notes = text_register(before), notes_register(before)
    for rec in records:
        n = rec["slide"]
        slide = before.slides[n-1]
        slot = slot_for(data["slides"][n-1])
        x, y, w, h = slot
        validate_slot(data["slides"][n-1])
        ratio = min(w/rec["width_px"], h/rec["height_px"])
        pw, ph = rec["width_px"]*ratio, rec["height_px"]*ratio
        px, py = x+(w-pw)/2, y+(h-ph)/2
        picture = slide.shapes.add_picture(
            str(Path(figure_directory)/rec["file"]),
            Inches(px), Inches(py), width=Inches(pw), height=Inches(ph))
        picture.name = f"Deck3 | independent infographic | Slide {n:02}"
        picture._element._nvXxPr.cNvPr.set("descr",rec["alt"])
        rec["geometry_in"] = [round(z, 4) for z in (px, py, pw, ph)]
        row = data["slides"][n-1]
        rec["usable_content_bounds_in"] = list(usable_bounds(row))
        rec["figure_slot_bounds_in"] = list(slot)
        rec["reserved_share"] = round(geometry_share(slot, usable_bounds(row)), 4)
        rec["placed_picture_share"] = round(
            geometry_share((px, py, pw, ph), usable_bounds(row)), 4)
        rec["effective_meaningful_visual_share"] = None
        rec["effective_share_verified"] = False
        rec["layout_exception"] = (
            "LONG_OBJECTIVES_REQUIRES_MANUAL_REVIEW"
            if row.get("layout") == "long_objectives" else None)
        if row.get("layout") != "long_objectives" and not (
                .70 <= rec["placed_picture_share"] <= .80):
            raise Blocked(
                f"Slide {n}: placed figure share {rec['placed_picture_share']:.1%}; "
                "recompose the figure for the dominant slot aspect ratio.")
        rec["preserved_aspect_ratio"] = abs(pw/ph-rec["width_px"]/rec["height_px"]) < 1e-9
        if not rec["preserved_aspect_ratio"]:
            raise AssertionError(f"Slide {n}: distorted image.")
    out = Path(output)
    out.parent.mkdir(parents=True, exist_ok=True)
    before.save(str(out))
    final_colors = check_pptx_colors(out)
    if final_colors["errors"]:
        raise Blocked("Assembled PPTX authored-color audit failed: "
                      + "; ".join(final_colors["errors"][:12]))
    after = Presentation(str(out))
    if text_register(after) != old_text:
        raise AssertionError("Text was changed during figure insertion.")
    if notes_register(after) != old_notes:
        raise AssertionError("Speaker notes were changed during figure insertion.")
    for n, slide in enumerate(after.slides, 1):
        expected = int(bool(data["slides"][n-1].get("figure")))
        found = sum(sh.shape_type == MSO_SHAPE_TYPE.PICTURE for sh in slide.shapes)
        if found != expected:
            raise AssertionError(f"Slide {n}: {found} images; expected {expected}.")
    if not zipfile.is_zipfile(out):
        raise AssertionError("Output is not a valid PowerPoint ZIP archive.")
    with zipfile.ZipFile(out) as archive:
        if archive.testzip() is not None:
            raise AssertionError("PowerPoint ZIP integrity failed.")
    report = {
        "status": "GEOMETRY_PASS_EFFECTIVE_OCCUPANCY_SCIENCE_AND_RENDER_UNVERIFIED",
        "slides": len(after.slides),
        "source_text_unchanged": True,
        "source_notes_unchanged": True,
        "image_count": len(records),
        "color_source_preflight": [
            {"slide": rec["slide"], "status": rec["authored_color_source_qa"]["status"]}
            for rec in records
        ],
        "color_certification": "NOT_CERTIFIED_FROM_ASSET_SOURCE_OR_ASSEMBLY_ALONE",
        "native_color_qa": final_colors["status"],
        "native_color_values": final_colors["visible_srgb_counts"],
        "figure_records": records,
        "manual_required": [
            "Verify figure physics and citation-to-claim mapping",
            "Render EVERY slide and inspect at presentation and thumbnail scale",
            "Inspect true text bounds, contrast, arrow meanings and reading order",
            "Inspect meaningful nonblank figure coverage; picture bounds alone cannot certify occupancy",
            "Review dense frozen-objectives slide exceptions at presentation size",
            "Inspect native PPTX authored colors and SVG/raster source provenance; do not infer color certification from file integrity",
            "Block public final/approved status while any figure is raster-only without verified source"
        ],
    }
    if qa_path:
        Path(qa_path).parent.mkdir(parents=True, exist_ok=True)
        Path(qa_path).write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"CHECK stage 3: {len(after.slides)} slides, {len(records)} figures, exact text/notes retained, {out}")
    return report


def main(argv=None):
    p = argparse.ArgumentParser(description="Deck3 scientific presentation workflow")
    subs = p.add_subparsers(dest="command", required=True)
    t = subs.add_parser("text", help="Build text PPTX with truly blank figure spaces")
    t.add_argument("--manifest", required=True)
    t.add_argument("--out", required=True)
    f = subs.add_parser("figures", help="Audit existing standalone scientific PNG assets")
    f.add_argument("--manifest", required=True)
    f.add_argument("--figures", required=True)
    f.add_argument("--slide", type=int)
    f.add_argument("--report")
    a = subs.add_parser("assemble", help="Insert approved independent images without stretching")
    a.add_argument("--manifest", required=True)
    a.add_argument("--text-pptx", required=True)
    a.add_argument("--figures", required=True)
    a.add_argument("--out", required=True)
    a.add_argument("--qa")
    all_p = subs.add_parser("all", help="Compose all stages; stops when actual image assets are absent")
    all_p.add_argument("--manifest", required=True)
    all_p.add_argument("--figures", required=True)
    all_p.add_argument("--output-dir", required=True)
    args = p.parse_args(argv)
    try:
        if args.command == "text":
            make_text(args.manifest, args.out)
        elif args.command == "figures":
            records = figure_records(load_manifest(args.manifest), args.figures, args.slide)
            print(f"PASS stage 2 asset audit: {len(records)} independent PNG figures present.")
            if args.report:
                Path(args.report).write_text(json.dumps(records, indent=2), encoding="utf-8")
        elif args.command == "assemble":
            assemble(args.manifest, args.text_pptx, args.figures, args.out, args.qa)
        elif args.command == "all":
            folder = Path(args.output_dir)
            folder.mkdir(parents=True, exist_ok=True)
            base = folder / "deck3_stage1_text.pptx"
            make_text(args.manifest, base)
            # Explicit stop here when scientifically authored image assets do not exist.
            figure_records(load_manifest(args.manifest), args.figures)
            assemble(args.manifest, base, args.figures,
                     folder / "deck3_final.pptx", folder / "deck3_qa.json")
    except Blocked as exc:
        print("BLOCKED: " + str(exc), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
