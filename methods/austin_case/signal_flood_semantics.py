"""Fail-closed temporal/causal semantics for Austin signal and flood sources."""
from __future__ import annotations

from typing import Any, Mapping

SIGNAL_ENDPOINT = (
    "https://services.arcgis.com/0L95CJ0VTaxqcmED/ArcGIS/rest/services/"
    "TRANSPORTATION_signals2/FeatureServer/0"
)
FLOOD_ENDPOINT = "https://maps.austintexas.gov/gis/rest/Shared/Floodplain/MapServer/1"


class SignalFloodSemanticsError(ValueError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise SignalFloodSemanticsError(message)


def validate_semantics(registry: Mapping[str, Any]) -> dict[str, Any]:
    _require(registry.get("case_id") == "AUS-P5U-2018-V1", "unexpected Austin case ID")
    _require(registry.get("status") == "SOURCE_SEMANTICS_FROZEN_EXECUTION_OPEN", "invalid registry status")

    signal = registry.get("signal")
    flood = registry.get("flood")
    causal = registry.get("causal_semantics")
    _require(isinstance(signal, Mapping), "signal registry required")
    _require(isinstance(flood, Mapping), "flood registry required")
    _require(isinstance(causal, Mapping), "causal semantics required")

    _require(signal.get("endpoint") == SIGNAL_ENDPOINT, "signal endpoint drift")
    _require(signal.get("strict_2018_snapshot") is False, "current signal layer cannot be labeled a 2018 snapshot")
    _require(signal.get("actual_feeder_assignment_claim_allowed") is False, "semisynthetic mapping cannot claim actual feeder truth")
    _require(signal.get("role") == "CURRENT_SIGNAL_LOCATION_REFERENCE_FOR_SEMISYNTHETIC_P_TO_T_MAPPING", "invalid signal role")

    _require(flood.get("endpoint") == FLOOD_ENDPOINT, "flood endpoint drift")
    fields = set(flood.get("required_fields", []))
    _require({"FLOOD_ZONE", "EFFECTIVE_DATE"} <= fields, "flood zone/effective-date fields required")
    _require(flood.get("role") == "STATIC_HAZARD_EXPOSURE_REFERENCE", "invalid flood role")
    for key in (
        "event_time_depth_supported",
        "event_time_velocity_supported",
        "road_closure_supported_without_separate_model",
        "failure_probability_supported_without_separate_model",
    ):
        _require(flood.get(key) is False, f"{key} must remain false without a qualified dynamic model")

    _require(causal.get("flood_is_common_cause") is True, "flood must remain a common-cause hazard")
    _require(causal.get("flood_is_p_to_t_edge") is False, "flood cannot be mislabeled P→T")
    _require(causal.get("flood_is_t_to_p_edge") is False, "flood cannot be mislabeled T→P")

    if registry.get("final_signal_flood_admissibility") is True:
        _require(signal.get("raw_materialized") is True, "final signal gate requires raw materialization")
        _require(signal.get("spatial_overlap_verified") is True, "final signal gate requires spatial overlap")
        _require(signal.get("mapping_verified") is True, "final signal gate requires reproducible semisynthetic mapping")
        _require(flood.get("raw_materialized") is True, "final flood gate requires raw materialization")
        _require(flood.get("effective_date_audited") is True, "final flood gate requires effective-date audit")
        _require(flood.get("spatial_overlap_verified") is True, "final flood gate requires asset overlap")

    return {
        "case_id": registry["case_id"],
        "signal_temporal_semantics": "PASS",
        "flood_static_semantics": "PASS",
        "common_cause_semantics": "PASS",
        "final_execution_gate": "PASS" if registry.get("final_signal_flood_admissibility") else "OPEN",
    }
