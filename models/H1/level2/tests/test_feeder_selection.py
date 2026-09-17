from __future__ import annotations
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("select_feeders", ROOT / "select_feeders.py")
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)


def test_selection_is_outcome_blind_and_distinct():
    rows = []
    for i, x in enumerate([0.0, 1.0, 2.0, 8.0]):
        rows.append({
            "feeder_id": f"F{i}",
            "C_geo": "true", "C_road": "true", "C_interface": "true", "C_hazard": "true", "C_computable": "true",
            "N_P": str(100 + x), "N_T": str(200 + 2*x), "N_I": str(10 + x), "P_max": str(5 + x),
            "L_T": str(20 + x), "R_T": str(1 + x/10), "E_H": str(x/10)
        })
    result = mod.select(rows)
    assert result["outcome_blind"] is True
    assert result["development_feeder_id"] != result["heldout_feeder_id"]
    assert result["n_eligible"] == 4
