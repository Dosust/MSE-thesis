from __future__ import annotations
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_preview_pipeline(tmp_path: Path):
    case = tmp_path / "case.json"
    result = tmp_path / "results.json"
    subprocess.run([sys.executable, str(ROOT / "build_reduced_case.py"), "--preview", "--out", str(case)], check=True)
    subprocess.run([sys.executable, str(ROOT / "run_level2.py"), "--case", str(case), "--out", str(result)], check=True)
    data = json.loads(result.read_text())
    assert data["mode"] == "preview"
    assert data["matched_inputs"] is True
    assert data["admissible_for_thesis_results"] is False
    assert data["summary"]["M2"]["max_queue_veh"] > 0
    assert data["derived"]["M2_restoration_h"] > data["derived"]["M1_restoration_h"]
    assert data["summary"]["M2"]["transport_service_loss_h"] >= data["summary"]["M1"]["transport_service_loss_h"]
