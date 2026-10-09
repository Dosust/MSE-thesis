"""Numerical property tests for synthetic shader math; not physical validation."""

from __future__ import annotations

import importlib.util
import math
import unittest
from pathlib import Path

MODULE = Path(__file__).resolve().parents[1] / "examples" / "procedural_reference.py"
SPEC = importlib.util.spec_from_file_location("shader_math_reference", MODULE)
assert SPEC and SPEC.loader
shader_math = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(shader_math)


class ProceduralMathematicsTests(unittest.TestCase):
    def test_fract_negative_input_and_range(self) -> None:
        self.assertEqual(shader_math.fract(-1.25), 0.75)
        for i in range(-20, 21):
            y = shader_math.fract(i / 7)
            self.assertGreaterEqual(y, 0)
            self.assertLess(y, 1)
        with self.assertRaises(ValueError):
            shader_math.fract(math.inf)

    def test_fractional_sine_deterministic_but_not_asserted_uniform(self) -> None:
        for x in (-3.0, -0.2, 0.0, 0.4, 10.0):
            value = shader_math.fractional_sine(x)
            self.assertEqual(value, shader_math.fractional_sine(x))
            self.assertGreaterEqual(value, 0)
            self.assertLess(value, 1)

    def test_power_transform_and_theory(self) -> None:
        for gamma in (0.5, 1.0, 2.0, 3.0):
            self.assertEqual(shader_math.power_quantile(0.0, gamma), 0)
            self.assertEqual(shader_math.power_quantile(1.0, gamma), 1)
            previous = -1.0
            for j in range(51):
                y = shader_math.power_quantile(j / 50, gamma)
                self.assertGreaterEqual(y, previous)
                previous = y
        for value, exponent in ((-0.1, 2), (0.5, 0), (1.1, 1), (math.nan, 2)):
            with self.assertRaises(ValueError):
                shader_math.power_quantile(value, exponent)

    def test_cell_coordinates_include_negative_positions(self) -> None:
        index, local = shader_math.cell_position(-0.1, 0.61, 8)
        self.assertEqual(index, (-1, 4))
        self.assertAlmostEqual(local[0], 0.2, delta=1e-13)
        self.assertAlmostEqual(local[1], 0.88, delta=1e-13)
        self.assertTrue(all(0 <= x < 1 for x in local))
        with self.assertRaises(ValueError):
            shader_math.cell_position(0, 0, -2)

    def test_integer_cell_hash_is_seeded_and_finite(self) -> None:
        for i in (-20, -1, 0, 1, 29):
            for j in (-7, 0, 13):
                result = shader_math.hash_cell(i, j)
                self.assertEqual(result, shader_math.hash_cell(i, j))
                self.assertGreaterEqual(result, 0)
                self.assertLess(result, 1)
                self.assertEqual(result * 16777216, int(result * 16777216))
        self.assertNotEqual(shader_math.hash_cell(2, 3, 12), shader_math.hash_cell(2, 3, 13))
        with self.assertRaises(ValueError):
            shader_math.hash_cell(0, 2, -1)

    def test_row_displacement_has_correct_velocity_derivative(self) -> None:
        t, v0, a, omega, phase = 0.7, 0.4, 0.3, 2.3, 0.25
        h = 1e-6
        position = lambda tau: shader_math.row_displacement(tau, v0, a, omega, phase)
        derivative = (position(t + h) - position(t - h)) / (2 * h)
        expected = v0 + a * math.sin(omega * t + phase)
        self.assertAlmostEqual(derivative, expected, delta=2e-10)
        self.assertEqual(position(0.0), 0.0)
        self.assertAlmostEqual(shader_math.row_displacement(t, v0, a, 0, phase), (v0 + a * math.sin(phase)) * t)
        with self.assertRaises(ValueError):
            shader_math.row_displacement(-1.0, v0, a, omega, phase)


if __name__ == "__main__":
    unittest.main()
