#!/usr/bin/env python3
"""Deck3 reproducible native-PPTX builder and inspector. Requires python-pptx.
Usage: python unified_pptx.py inspect existing.pptx --out inventory.json
       python unified_pptx.py build approved_slides.json output.pptx --palette DECK3_SRGB_PALETTE.json
       python unified_pptx.py qa output.pptx --palette DECK3_SRGB_PALETTE.json
       python unified_pptx.py revise input.pptx output.pptx --slide 3 --old TEXT --new TEXT
The builder preserves editable native text; it does NOT create or certify OMML."""
import argparse
import json
import re
import shutil
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.util import Inches, Pt

M = "{http://schemas.openxmlformats.org/officeDocument/2006/math}"
S = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
PX = "{http://schemas.openxmlformats.org/presentationml/2006/main}"

def save_json(obj, path):
    Path(path).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def inspect(path):
    prs = Presentation(str(path))
    slides = []
    with zipfile.ZipFile(path) as z:
        for i, slide in enumerate(prs.slides, 1):
            xml = z.read("ppt/slides/slide%d.xml" % i)
            root = ET.fromstring(xml)
            omml = sum(1 for node in root.iter() if node.tag in (M+"oMath", M+"oMathPara"))
            shapes = [{"id":s.shape_id, "name":s.name,
                       "type":str(s.shape_type), "x":s.left/914400, "y":s.top/914400,
                       "w":s.width/914400, "h":s.height/914400,
                       "text":s.text if s.has_text_frame else ""}
                      for s in slide.shapes]
            notes = ""
            try:
                if slide.has_notes_slide:
                    notes = slide.notes_slide.notes_text_frame.text
            except (AttributeError, ValueError):
                notes = ""
            slides.append({"slide":i, "shapes":shapes, "notes":notes, "omml_elements":omml})
    return {"width_inches":prs.slide_width/914400, "height_inches":prs.slide_height/914400,
            "slides":slides, "slide_count":len(prs.slides)}

def palette_from(path):
    if not path:
        return None
    obj = json.loads(Path(path).read_text(encoding="utf-8"))
    colors = obj.get("colors", {})
    assert len(colors) == 13, "Canonical 13-color palette required"
    return {k:v["hex"].lstrip("#").upper() for k,v in colors.items()}

def build(manifest, output, palette_path):
    colors = palette_from(palette_path)
    if not colors:
        raise ValueError("Canonical palette path required for Deck3 generation")
    source = json.loads(Path(manifest).read_text(encoding="utf-8"))
    slides = source.get("slides", [])
    if not slides or len(slides) != 13:
        raise ValueError("Approved Chapter 1 build requires precisely 13 source slides")
    prs = Presentation()
    prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
    blank = prs.slide_layouts[6]
    for i, data in enumerate(slides, 1):
        slide = prs.slides.add_slide(blank)
        bg = slide.background.fill
        bg.solid()
        bg.fore_color.rgb = RGBColor.from_string(colors["white"])
        t = slide.shapes.add_textbox(Inches(.7), Inches(.45), Inches(11.95), Inches(.65))
        p = t.text_frame.paragraphs[0]
        p.text = data["title"]
        p.font.size = Pt(27)
        p.font.bold = True
        p.font.color.rgb = RGBColor.from_string(colors["navy"])
        texts = [data.get("message", "")] + data.get("bullets", [])
        for j, txt in enumerate(x for x in texts if x):
            box = slide.shapes.add_textbox(Inches(.8), Inches(1.35+j*.83), Inches(11.8), Inches(.72))
            pp = box.text_frame.paragraphs[0]
            pp.text = txt
            pp.font.size = Pt(21 if j == 0 else 18)
            pp.font.color.rgb = RGBColor.from_string(colors["black"])
        if data.get("source_note"):
            box = slide.shapes.add_textbox(Inches(.8), Inches(6.95), Inches(11.9), Inches(.33))
            pp = box.text_frame.paragraphs[0]
            pp.text = data["source_note"]
            pp.font.size = Pt(10)
            pp.font.color.rgb = RGBColor.from_string(colors["graphite"])
        if data.get("notes"):
            slide.notes_slide.notes_text_frame.text = data["notes"]
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        raise FileExistsError("Output already exists; select a versioned filename")
    prs.save(str(output))
    return inspect(output)

def revise(original, target, slide_no, old, new):
    inp, out = Path(original), Path(target)
    if inp.resolve() == out.resolve() or out.exists():
        raise ValueError("Revise must write a new, previously unused filename")
    prs = Presentation(str(inp))
    if not 1 <= slide_no <= len(prs.slides):
        raise IndexError("Slide not found")
    changed = 0
    for shape in prs.slides[slide_no-1].shapes:
        if shape.has_text_frame:
            for paragraph in shape.text_frame.paragraphs:
                for run in paragraph.runs:
                    if old in run.text:
                        run.text = run.text.replace(old, new)
                        changed += 1
    if not changed:
        raise ValueError("Exact text was not found in a single editable run; no changes saved")
    out.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(out))
    return changed

def qa(path, palette_path=None):
    inv = inspect(path)
    colors = palette_from(palette_path)
    allowed = set(colors.values()) if colors else None
    problems, checks = [], {}
    checks["slide_count"] = "PASS" if inv["slide_count"] == 13 else "FAIL"
    checks["native_shape_inventory"] = "PASS"
    checks["native_omml"] = "PASS" if sum(s["omml_elements"] for s in inv["slides"]) else "NOT_RUN"
    with zipfile.ZipFile(path) as z:
        for name in z.namelist():
            if not re.fullmatch(r"ppt/slides/slide\d+\.xml", name):
                continue
            root = ET.fromstring(z.read(name))
            for node in root.iter():
                if node.tag == S+"gradFill":
                    problems.append(name+": authored gradient")
                if allowed is not None and node.tag == S+"srgbClr":
                    rgb = node.attrib.get("val","").upper()
                    if rgb not in allowed:
                        problems.append(name+": unauthorized color "+rgb)
    checks["palette_xml"] = "NOT_RUN" if allowed is None else ("FAIL" if problems else "PASS")
    checks["no_gradients"] = "FAIL" if any("gradient" in x for x in problems) else "PASS"
    checks["real_render"] = "NOT_RUN"
    checks["desktop_playback"] = "NOT_RUN"
    checks["scientific_validation"] = "NOT_RUN"
    return {"checks":checks,"issues":problems,"slide_count":inv["slide_count"],
            "equation_elements":sum(s["omml_elements"] for s in inv["slides"])}

def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("inspect"); p.add_argument("pptx"); p.add_argument("--out")
    p = sub.add_parser("build"); p.add_argument("manifest"); p.add_argument("output"); p.add_argument("--palette", required=True)
    p = sub.add_parser("qa"); p.add_argument("pptx"); p.add_argument("--palette")
    p = sub.add_parser("revise"); p.add_argument("pptx"); p.add_argument("output"); p.add_argument("--slide", type=int, required=True); p.add_argument("--old", required=True); p.add_argument("--new", required=True)
    a = parser.parse_args()
    if a.cmd == "inspect":
        result = inspect(a.pptx)
        if a.out: save_json(result, a.out)
    elif a.cmd == "build": result = {"built":a.output,"inventory":build(a.manifest,a.output,a.palette)}
    elif a.cmd == "qa": result = qa(a.pptx,a.palette)
    else: result = {"replaced_runs":revise(a.pptx,a.output,a.slide,a.old,a.new),"output":a.output}
    print(json.dumps(result, indent=2, ensure_ascii=False))
if __name__ == "__main__":
    main()
