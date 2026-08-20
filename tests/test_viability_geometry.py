import math
import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "methods" / "architecture" / "viability_geometry.py"
spec = importlib.util.spec_from_file_location("viability_geometry", MODULE_PATH)
vg = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(vg)


def test_rectangle_contains_boundaries():
    r = vg.Rectangle(-1, 1, -2, 2)
    assert r.contains((-1, -2))
    assert r.contains((1, 2))
    assert not r.contains((1.00001, 0))


def test_zero_field_is_admissible():
    r = vg.Rectangle(-1, 1, -1, 1)
    zero = lambda x, t: (0.0, 0.0)
    assert vg.trajectory_is_admissible((0.8, -0.9), r, zero, 5.0, 0.05)


def test_hausdorff_identity():
    pts = [(-1.0, 0.0), (0.0, 0.0), (1.0, 0.0)]
    assert math.isclose(vg.hausdorff_distance(pts, pts), 0.0, abs_tol=1e-12)


def test_hausdorff_symmetric():
    a = [(0.0, 0.0), (1.0, 0.0)]
    b = [(0.0, 0.0), (2.0, 0.0)]
    assert math.isclose(vg.hausdorff_distance(a, b), vg.hausdorff_distance(b, a))


def test_dynamic_static_demo_is_finite():
    result = vg.demo_boundary_deformation()
    assert result["n_static"] > 0
    assert result["n_dynamic"] > 0
    assert math.isfinite(result["hausdorff_grid_distance"])
    assert result["hausdorff_grid_distance"] >= 0.0
