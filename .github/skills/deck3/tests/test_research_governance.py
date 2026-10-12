"""Deck3 repository governance regression checks.

These are structural checks, not physical-model validation or slide render QA.
Run from repository root:
python -m unittest discover -s .github/skills/deck3/tests -p 'test_research_governance.py' -v
"""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
DECK = ROOT / ".github/skills/deck3"
REF = DECK / "references"


class ResearchGovernanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = json.loads((REF / "DECK3_DEPENDENCY_REGISTRY.json").read_text(encoding="utf-8"))
        cls.palette = json.loads((REF / "DECK3_SRGB_PALETTE.json").read_text(encoding="utf-8"))

    def test_declared_scientific_authorities_exist(self):
        for path in self.registry["science_authorities"]:
            with self.subTest(path=path):
                self.assertTrue((ROOT / path).is_file(), path)

    def test_registered_implementation_paths_exist(self):
        for route in self.registry["routes"]:
            for path in route["paths"]:
                with self.subTest(route=route["category"], path=path):
                    self.assertTrue((ROOT / path).is_file(), path)

    def test_palette_is_exactly_thirteen_valid_srgb_tokens(self):
        colors = self.palette["colors"]
        self.assertEqual(len(colors), 13)
        self.assertEqual(self.registry["palette_tokens"], 13)
        self.assertEqual(self.palette["color_space"], "sRGB")
        self.assertEqual(self.palette["channel_bits"], 8)
        for name, token in colors.items():
            with self.subTest(token=name):
                rgb = token["rgb"]
                self.assertEqual(len(rgb), 3)
                self.assertTrue(all(isinstance(v, int) and 0 <= v <= 255 for v in rgb))
                self.assertEqual(token["hex"].upper(), "#" + "".join(f"{v:02X}" for v in rgb))
        for surface, color in self.palette["authored_surfaces"].items():
            with self.subTest(surface=surface):
                self.assertEqual(color.upper(), "#FFFFFF")

    def test_institutional_exception_is_restricted(self):
        self.assertEqual(self.palette["colors"]["asu_gold"]["hex"].upper(), "#FFC627")
        self.assertFalse(self.palette["colors"]["asu_gold"]["allowed_as_surface"])
        self.assertEqual(self.palette["colors"]["asu_maroon"]["hex"].upper(), "#8C1D40")

    def test_presentation_variant_router_and_masters_exist(self):
        router = ROOT / "thesis/presentations/deck3/DECK3_PRESENTATION_MASTER_ROUTER_V1.md"
        short = ROOT / "thesis/presentations/deck3/DECK3_3MIN_8SLIDES_CANONICAL_TEXT_V1.md"
        self.assertTrue(router.is_file())
        self.assertTrue(short.is_file())
        text = router.read_text(encoding="utf-8")
        self.assertIn("eight-slide", text)
        self.assertIn("14-slide", text)
        self.assertIn("distinct artifacts", text)

    def test_mechanism_sidecar_policy_is_fail_closed(self):
        policy = self.registry["current_trace_policy"]
        self.assertEqual(policy["invalid"], "BLOCK_STAGE2_AND_STAGE3")
        self.assertEqual(policy["absent"], "PROVISIONAL_NO_SCIENTIFIC_CERTIFICATION")
        self.assertEqual(policy["structurally_valid"], "NOT_PHYSICS_OR_CITATION_VERIFIED")

    def test_ci_invokes_existing_deck3_tests(self):
        workflow = (ROOT / ".github/workflows/deck3-tests.yml").read_text(encoding="utf-8")
        self.assertIn("unittest discover -s tests", workflow)
        self.assertIn("mechanism_trace_qa.py", workflow)
        self.assertIn("deck3.py text", workflow)


    def test_reference_figure_contract_links_existing_slide_and_evidence(self):
        fixture = json.loads((DECK / "examples/figure_contract_slide02_example.json").read_text(encoding="utf-8"))
        self.assertEqual(fixture["schema"], "deck3-figure-contract-v1")
        self.assertEqual(fixture["status"], "SYNTHETIC_CONCEPTUAL_FIXTURE_NOT_APPROVED_ARTWORK")
        manifest_path = ROOT / fixture["manifest_path"]
        self.assertTrue(manifest_path.is_file())
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        slide = manifest["slides"][fixture["slide_index_1based"] - 1]
        self.assertEqual(slide["kind"], "content")
        self.assertEqual(slide["figure"]["file"], fixture["figure_file"])
        self.assertEqual(slide["message"], fixture["claim"])
        self.assertTrue((ROOT / fixture["source"]["path"]).is_file())
        self.assertEqual(fixture["source"]["external_empirical_support"], "NOT_CLAIMED")
        self.assertEqual(fixture["science"]["cross_system_causality"], "NOT_ESTABLISHED")
        self.assertEqual(fixture["science"]["quantitative_results"], "NONE_CLAIMED")
        self.assertEqual(fixture["science"]["sustainability_effect"], "NOT_ASSESSED")
        self.assertEqual(fixture["visual"]["palette_path"], self.registry["palette_path"])
        self.assertEqual(fixture["visual"]["canvas"], "#FFFFFF")
        self.assertEqual(fixture["visual"]["font"], "Times New Roman")
        self.assertEqual(fixture["visual"]["aspect_ratio"], "16:9")
        self.assertEqual(fixture["animation"]["mode"], "STATIC")
        self.assertEqual(fixture["animation"]["click_count"], 0)
        self.assertEqual(fixture["animation"]["powerpoint_playback"], "NOT_RUN")
        self.assertEqual(fixture["verification"]["physical"], "NOT_VALIDATED")


if __name__ == "__main__":
    unittest.main()
