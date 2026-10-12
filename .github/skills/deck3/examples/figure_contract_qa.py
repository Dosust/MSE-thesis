"""Validate Deck3 figure metadata without certifying scientific truth.

Usage: python examples/figure_contract_qa.py examples/figure_contract_slide02_example.json
This checks linked files, approved tokens and explicit claim limitations only.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def validate(contract: dict, root: Path = ROOT) -> dict:
    errors = []
    def require(condition: bool, message: str) -> None:
        if not condition:
            errors.append(message)

    if not isinstance(contract, dict):
        return {"status": "BLOCKED", "errors": ["contract must be an object"],
                "science_validated": False, "powerpoint_playback_verified": False}
    require(contract.get("schema") == "deck3-figure-contract-v1", "invalid schema")
    try:
        path = root / contract["manifest_path"]
        require(path.is_file(), "missing manifest")
        manifest = json.loads(path.read_text(encoding="utf-8"))
        index = contract["slide_index_1based"]
        require(type(index) is int and 1 <= index <= len(manifest["slides"]), "invalid slide index")
        slide = manifest["slides"][index - 1]
        require(slide["kind"] == "content", "figure must belong to a content slide")
        require(slide["message"] == contract["claim"], "slide message differs from registered claim")
        require(slide["figure"]["file"] == contract["figure_file"], "figure filename mismatch")
    except (KeyError, IndexError, TypeError, ValueError, OSError) as exc:
        errors.append("manifest/slide linkage invalid: " + str(exc))
    try:
        source = contract["source"]
        require(source["type"] == "internal_scope_authority", "fixture source type mismatch")
        require((root / source["path"]).is_file(), "missing source authority")
        require(source["external_empirical_support"] == "NOT_CLAIMED",
                "fixture cannot claim external empirical support")
        science = contract["science"]
        require(science["cross_system_causality"] == "NOT_ESTABLISHED",
                "conceptual fixture cannot establish directional causality")
        require(science["quantitative_results"] == "NONE_CLAIMED",
                "conceptual fixture cannot claim numerical results")
        require(science["sustainability_effect"] == "NOT_ASSESSED",
                "conceptual fixture cannot claim sustainability assessment")
        visual = contract["visual"]
        palette_path = root / visual["palette_path"]
        require(palette_path.is_file(), "missing palette")
        palette = json.loads(palette_path.read_text(encoding="utf-8"))
        require(visual["canvas"] == palette["authored_surfaces"]["canvas"] == "#FFFFFF",
                "nonwhite canvas")
        require(visual["font"] == "Times New Roman", "incorrect Deck3 font")
        require(visual["aspect_ratio"] == "16:9", "incorrect aspect ratio")
        animation = contract["animation"]
        require(animation["mode"] == "STATIC" and type(animation["click_count"]) is int
                and animation["click_count"] == 0, "static fixture must have zero animation clicks")
        require(animation["powerpoint_playback"] == "NOT_RUN", "unverified playback claimed")
        require(contract["verification"]["physical"] == "NOT_VALIDATED",
                "structural contract cannot certify physics")
        require(contract["verification"]["pptx"] == "NOT_RUN", "unverified PPTX claimed")
    except (KeyError, TypeError, ValueError, OSError) as exc:
        errors.append("contract metadata invalid: " + str(exc))
    return {"status": "STRUCTURAL_CONTRACT_PASS_NOT_SCIENCE_VERIFIED" if not errors else "BLOCKED",
            "errors": errors, "science_validated": False,
            "citation_content_verified": False, "powerpoint_playback_verified": False}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("contract_json", type=Path)
    args = parser.parse_args()
    try:
        contract = json.loads(args.contract_json.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(json.dumps({"status": "BLOCKED", "errors": [str(exc)]}))
        raise SystemExit(1)
    result = validate(contract)
    print(json.dumps(result, indent=2))
    raise SystemExit(1 if result["status"] == "BLOCKED" else 0)


if __name__ == "__main__":
    main()
