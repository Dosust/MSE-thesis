"""Tests for the scientific infographic skill's executable examples.

Run: python -m unittest discover -s tests -v
No test data are real thermal/EVSE measurements.
"""
import math
import sys
import tempfile
import unittest
from pathlib import Path
from xml.etree import ElementTree as ET

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE / "examples"))

import figures  # noqa: E402
import mathematical_metrics as metrics  # noqa: E402


class ModelIndependentMathTests(unittest.TestCase):
    def test_first_passage_linear_interpolation(self):
        actual = metrics.first_downward_threshold_time([0.,1.,2.],[.9,.7,.4],.5)
        self.assertAlmostEqual(actual, 5./3., places=12)

    def test_initial_event(self):
        self.assertEqual(metrics.first_downward_threshold_time([0.,1.],[.4,.8],.5), 0.)

    def test_absent_event(self):
        self.assertIsNone(metrics.first_downward_threshold_time([0.,1.],[.9,.8],.5))

    def test_irregular_time(self):
        self.assertAlmostEqual(
            metrics.first_downward_threshold_time([0.,2.,5.],[1.,.8,.2],.5),
            3.5)

    def test_time_must_be_strictly_increasing(self):
        with self.assertRaises(ValueError):
            metrics.first_downward_threshold_time([0.,1.,1.],[.9,.7,.4],.5)

    def test_nonfinite_rejected(self):
        with self.assertRaises(ValueError):
            metrics.first_downward_threshold_time([0.,1.],[math.nan,.2],.5)

    def test_mismatched_length(self):
        with self.assertRaises(ValueError):
            metrics.first_downward_threshold_time([0.,1.,2.],[.8,.2],.5)

    def test_propagation_delay(self):
        self.assertEqual(metrics.propagation_delay(3.,5.),2.)

    def test_noncausal_time_order_is_flagged(self):
        with self.assertRaises(ValueError):
            metrics.propagation_delay(5.,3.)

    def test_exact_positive_gap_linear_crossings(self):
        area = metrics.positive_service_deficit_integral(
            [0.,1.,2.],[1.,.4,1.],[.8,.8,.8],
            time_unit="unitless",service_unit="unitless")
        self.assertAlmostEqual(area, 4./15., places=12)

    def test_full_constant_deficit(self):
        area = metrics.positive_service_deficit_integral(
            [0.,2.],[.3,.3],[.8,.8],time_unit="h",service_unit="MW")
        self.assertAlmostEqual(area, 1.0, places=12)

    def test_missing_units_rejected(self):
        with self.assertRaises(ValueError):
            metrics.positive_service_deficit_integral(
                [0.,1.],[.3,.3],[.8,.8],time_unit="",service_unit="MW")


class ScientificFigureTests(unittest.TestCase):
    def test_registered_semantics(self):
        figures.check_registry()

    def test_parallel_heat_has_no_cross_system_edge(self):
        cross = [e for e in figures.REGISTER["04"]["edges"]
                 if e[0] in {"P","Te"} and e[1] in {"P","Te"}]
        self.assertEqual(cross, [])

    def test_full_te_scope_is_retained(self):
        self.assertTrue(figures.SCOPE_TE.issubset(
            figures.REGISTER["03"]["included_te"]))

    def test_candidate_grid_side_gate_present(self):
        self.assertIn("grid-side AC input", figures.REGISTER["05"]["required_gates"])

    def test_all_svg_outputs_are_valid_xml_with_white_background(self):
        with tempfile.TemporaryDirectory() as folder:
            paths = figures.write_all(Path(folder))
            self.assertEqual(len(paths),3)
            for path in paths:
                self.assertGreater(path.stat().st_size,100)
                root = ET.parse(path).getroot()
                self.assertTrue(root.tag.endswith("svg"))
                rectangles = [e for e in root.iter() if e.tag.endswith("rect")]
                self.assertTrue(rectangles)
                self.assertTrue(all(e.attrib.get("fill") == "#FFFFFF"
                                    for e in rectangles))
                # Edits are real SVG objects, not a flattened image.
                self.assertFalse(any(e.tag.endswith("image") for e in root.iter()))

    def test_all_external_claim_slides_have_source_note(self):
        for factory in (figures.scene03, figures.scene04, figures.scene05):
            texts = [e.text or "" for e in factory().iter() if e.tag.endswith("text")]
            self.assertTrue(any("Sources:" in t for t in texts))


if __name__ == "__main__":
    unittest.main()
