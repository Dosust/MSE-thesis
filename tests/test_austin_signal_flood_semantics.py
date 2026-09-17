import json
from pathlib import Path

import pytest

from methods.austin_case.signal_flood_semantics import (
    SignalFloodSemanticsError,
    validate_semantics,
)

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "config" / "austin_signal_flood_semantics_v1.json"


def registry():
    return json.loads(REGISTRY.read_text(encoding="utf-8"))


def test_repository_registry_passes_semantics_but_remains_open():
    result = validate_semantics(registry())
    assert result["signal_temporal_semantics"] == "PASS"
    assert result["flood_static_semantics"] == "PASS"
    assert result["common_cause_semantics"] == "PASS"
    assert result["final_execution_gate"] == "OPEN"


def test_current_signal_layer_cannot_be_called_2018_snapshot():
    data = registry()
    data["signal"]["strict_2018_snapshot"] = True
    with pytest.raises(SignalFloodSemanticsError, match="2018 snapshot"):
        validate_semantics(data)


def test_semisynthetic_signal_mapping_cannot_claim_actual_feeder_truth():
    data = registry()
    data["signal"]["actual_feeder_assignment_claim_allowed"] = True
    with pytest.raises(SignalFloodSemanticsError, match="actual feeder truth"):
        validate_semantics(data)


def test_static_floodplain_cannot_supply_event_depth_without_model():
    data = registry()
    data["flood"]["event_time_depth_supported"] = True
    with pytest.raises(SignalFloodSemanticsError, match="event_time_depth_supported"):
        validate_semantics(data)


def test_flood_remains_common_cause_not_interdependency_edge():
    data = registry()
    data["causal_semantics"]["flood_is_p_to_t_edge"] = True
    with pytest.raises(SignalFloodSemanticsError, match="P→T"):
        validate_semantics(data)


def test_final_gate_fails_without_materialization_and_overlap():
    data = registry()
    data["final_signal_flood_admissibility"] = True
    with pytest.raises(SignalFloodSemanticsError, match="raw materialization"):
        validate_semantics(data)
