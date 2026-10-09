"""Deck3 v1.7 additive-skill tests. Static contracts are not PowerPoint GUI QA."""

from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SKILLS = ROOT / ".github" / "skills"
ROUTER = SKILLS / "scientific-visual-orchestration"
DECK3 = SKILLS / "deck3"

# v1.6 frozen files: a deliberate generator/palette change requires a separate,
# explicitly reviewed PR and matching updated regression baseline.
V16_FROZEN_GIT_BLOBS = {
    "deck3/examples/deck3.py": "5e601b40cb3c1adcdad43940f418f555dbd37850",
    "deck3/references/DECK3_SRGB_PALETTE.json": "dd30d0f882ca76d76e95f01a96193d54e7a8d32c",
}

EXPECTED_RGB = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "navy": (18, 48, 74),
    "blue": (0, 114, 178),
    "slate_blue": (65, 105, 133),
    "teal": (0, 109, 112),
    "cyan_blue": (8, 126, 152),
    "forest_green": (23, 107, 66),
    "deep_red": (180, 35, 44),
    "graphite": (85, 93, 102),
    "asu_maroon": (140, 29, 64),
    "asu_gold": (255, 198, 39),
    "bright_turquoise": (106, 206, 238),
}


def git_blob_sha(path: Path) -> str:
    body = path.read_bytes()
    prefix = b"blob " + str(len(body)).encode("ascii") + b"\x00"
    return hashlib.sha1(prefix + body).hexdigest()


def route_record() -> dict:
    return json.loads(
        (ROUTER / "references/ROUTING_CONTRACT.json").read_text(encoding="utf-8")
    )


class UnificationNonRegressionTests(unittest.TestCase):
    def test_original_palette_and_deck3_runtime_are_bit_identical(self) -> None:
        for relative, expected in V16_FROZEN_GIT_BLOBS.items():
            with self.subTest(file=relative):
                self.assertEqual(git_blob_sha(SKILLS / relative), expected)

    def test_exact_palette_13_tokens_white_panels_no_low_contrast_essentials(self) -> None:
        d = json.loads(
            (DECK3 / "references/DECK3_SRGB_PALETTE.json").read_text(encoding="utf-8")
        )
        self.assertEqual(d["policy_version"], "1.6.0")
        self.assertEqual(d["color_space"], "sRGB")
        self.assertEqual(d["channel_bits"], 8)
        self.assertEqual(set(d["colors"]), set(EXPECTED_RGB))
        self.assertEqual(set(d["authored_surfaces"].values()), {"#FFFFFF"})
        for key, rgb in EXPECTED_RGB.items():
            with self.subTest(color=key):
                self.assertEqual(tuple(d["colors"][key]["rgb"]), rgb)
                self.assertEqual(
                    d["colors"][key]["hex"],
                    "#" + "".join(f"{value:02X}" for value in rgb),
                )
        for low in ("asu_gold", "bright_turquoise"):
            self.assertLess(d["colors"][low]["contrast_on_white"], 3)

    def test_unified_skill_router_paths_resolve_and_have_unique_primary_owner(self) -> None:
        contract = route_record()
        self.assertEqual(contract["schema_version"], "1.0.0")
        self.assertEqual(contract["palette_authority"], str(
            Path(".github/skills/deck3/references/DECK3_SRGB_PALETTE.json")
        ))
        routes = contract["primary_routes"]
        self.assertEqual(len(routes), 8)
        self.assertEqual(len({r["id"] for r in routes}), len(routes))
        self.assertEqual(len({r["primary"] for r in routes}), len(routes))
        for route in routes:
            with self.subTest(route=route["id"]):
                self.assertTrue((ROOT / route["primary"]).is_file())
                self.assertTrue(route["guards"])
                for helper in route["helpers"]:
                    self.assertTrue((ROOT / helper).is_file())

        graph = {r["primary"]: r["helpers"] for r in routes}
        explored: set[str] = set()
        active: set[str] = set()

        def visit(node: str) -> None:
            if node in active:
                self.fail(f"Recursive specialist invocation cycle: {node}")
            if node in explored:
                return
            active.add(node)
            for dependency in graph.get(node, []):
                visit(dependency)
            active.remove(node)
            explored.add(node)

        for node in graph:
            visit(node)

    def test_deck3_v17_declares_existing_protections_and_no_runtime_upgrade(self) -> None:
        text = (DECK3 / "SKILL.md").read_text(encoding="utf-8")
        for essential in (
            'version: "1.7.0"',
            "Deck3 text",
            "Deck3 figures",
            "Deck3 assemble",
            "Deck3 all",
            "Stage 1",
            "Stage 2",
            "Stage 3",
            "75%",
            "70–80%",
            "frozen",
            "T_e",
            "APA",
            "DECK3_SRGB_PALETTE.json",
            "legacy",
            "scientific-visual-orchestration/SKILL.md",
        ):
            with self.subTest(essential=essential):
                self.assertIn(essential, text)
        self.assertIn("no new runtime geometry capability", text.lower())
        self.assertNotIn("No gold unless explicitly requested", text)
        self.assertNotIn("shadows, gold or decorative components", text)

    def test_specialist_skill_content_retained_and_router_links_valid(self) -> None:
        paths = [
            "engineering-framework-design/SKILL.md",
            "scientific-diagram-design/SKILL.md",
            "scientific-infographic-design/SKILL.md",
            "mathematical-visualization-design/SKILL.md",
            "visquill-interactive-visualization/SKILL.md",
            "deck3/advanced_powerpoint/SKILL.md",
        ]
        for path in paths:
            with self.subTest(skill=path):
                source = SKILLS / path
                text = source.read_text(encoding="utf-8")
                self.assertIn("scientific-visual-orchestration", text)
                self.assertGreater(len(text), 2000)
                self.assertIn("SKILL.md", text)
        self.assertIn(
            "No numerical plots without admitted equations/data.",
            (DECK3 / "references/WORKFLOW.md").read_text(encoding="utf-8"),
        )

    def test_scientific_scope_not_replaced_by_shader_study(self) -> None:
        root_skill = (ROUTER / "SKILL.md").read_text(encoding="utf-8")
        shader = (SKILLS / "procedural-mathematical-art/SKILL.md").read_text(
            encoding="utf-8"
        )
        for token in ("Power P", "T_e", "heat", "frozen", "palette"):
            self.assertIn(token, root_skill)
        for token in ("synthetic", "not", "hash", "GLSL", "stochastic"):
            self.assertIn(token.lower(), shader.lower())
        self.assertIn(
            "https://thebookofshaders.com/10/",
            (ROUTER / "references/CHAPTER_10_TRANSFER.md").read_text(encoding="utf-8"),
        )


if __name__ == "__main__":
    unittest.main()
