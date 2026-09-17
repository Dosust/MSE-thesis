"""Fail-closed validation for versioned Austin case-study admissibility contracts.

This module validates research-control state. It does not download data,
compute scientific parameters, or adjudicate H1--H5. Its purpose is to prevent
an Austin candidate case from being marked admissible before every frozen
pre-result data, temporal-evidence, and mechanism gate has passed.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping


class AustinAdmissibilityError(ValueError):
    """Raised when the Austin admissibility contract violates a frozen rule."""


BASE_AUTHORITIES = {
    "project/CANONICAL_7_STAGE_FRAMEWORK_V2.md",
    "project/CANONICAL_RQ_SO_HYPOTHESES_V3.md",
}
VERSION_AUTHORITIES = {
    "1.0": BASE_AUTHORITIES
    | {"project/AUSTIN_CASE_STUDY_DATA_ADMISSIBILITY_MATRIX_V1.md"},
    "2.0": BASE_AUTHORITIES
    | {
        "project/AUSTIN_CASE_STUDY_DATA_ADMISSIBILITY_MATRIX_V2.md",
        "project/AUSTIN_BOUNDARY_VINTAGE_PROTOCOL_V1.md",
        "project/AUSTIN_ROAD_VINTAGE_PROTOCOL_V1.md",
    },
    "3.0": BASE_AUTHORITIES
    | {
        "project/AUSTIN_CASE_STUDY_DATA_ADMISSIBILITY_MATRIX_V3.md",
        "project/AUSTIN_BOUNDARY_VINTAGE_PROTOCOL_V1.md",
        "project/AUSTIN_ROAD_VINTAGE_PROTOCOL_V1.md",
        "project/AUSTIN_TEMPORAL_EVIDENCE_PROTOCOL_V1.md",
    },
}

REQUIRED_GATE_IDS = (
    "G0_canonical_consistency",
    "G1_power_materialization",
    "G2_common_spatial_support",
    "G3_transport_topology",
    "G4_traffic_observations",
    "G5_p_to_t_mapping",
    "G6_t_to_p_repair_access",
    "G7_flood_exposure",
    "G8_qc_provenance",
)

MANDATORY_DATA_IDS = {"boundary", "power", "road", "signals", "flood"}
TRAFFIC_DATA_IDS = {"traffic_camera", "traffic_radar"}
DERIVED_IDS = {"repair_access", "p_to_t_signal_power_mapping"}
DERIVED_IDS_V3 = DERIVED_IDS | {"traffic_signals_retrospective_2018"}
TXDOT_2018_ROAD = (
    "https://services.arcgis.com/KTcxiTD9dsQw4r7Z/ArcGIS/rest/services/"
    "TxDOT_Roadway_Inventory_2018/FeatureServer/0"
)


def load_contract(path: str | Path) -> dict[str, Any]:
    """Load and validate a JSON contract from disk."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    validate_contract(data)
    return data


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise AustinAdmissibilityError(message)


def _index_unique(
    items: list[Mapping[str, Any]], key: str, label: str
) -> dict[str, Mapping[str, Any]]:
    out: dict[str, Mapping[str, Any]] = {}
    for item in items:
        _require(isinstance(item, Mapping), f"{label} entries must be objects")
        value = item.get(key)
        _require(
            isinstance(value, str) and value,
            f"{label} entry missing non-empty {key}",
        )
        _require(value not in out, f"duplicate {label} {key}: {value}")
        out[value] = item
    return out


def _validate_2018_road_contract(
    families: Mapping[str, Mapping[str, Any]], *, version_label: str
) -> None:
    road = families["road"]
    _require(
        road.get("endpoint") == TXDOT_2018_ROAD,
        f"{version_label} primary road source must remain TxDOT Roadway Inventory 2018",
    )
    _require(
        road.get("inventory_year") == 2018,
        f"{version_label} primary road year must remain 2018",
    )
    _require(
        road.get("strict_2018_snapshot") is True,
        f"{version_label} primary road must be marked exact annual 2018 inventory",
    )
    for item_id in ("road_ctn_sensitivity", "road_city_current_sensitivity"):
        _require(
            item_id in families,
            f"{version_label} missing required road sensitivity family: {item_id}",
        )
        _require(
            families[item_id].get("strict_2018_snapshot") is False,
            f"{item_id} must not be labeled a frozen 2018 snapshot",
        )
        _require(
            families[item_id].get("mandatory") is False,
            f"{item_id} is sensitivity evidence and must remain nonmandatory",
        )


def _validate_v3_temporal_contract(
    data: Mapping[str, Any],
    families: Mapping[str, Mapping[str, Any]],
    derived: Mapping[str, Mapping[str, Any]],
) -> None:
    _require("traffic_radar" in families, "v3 requires historical radar observations")
    _require(
        "radar_sensor_locations" in families,
        "v3 requires retrospective radar sensor-location metadata",
    )

    signals = families["signals"]
    _require(
        signals.get("temporal_role") == "CURRENT_NONVERSIONED_SOURCE",
        "v3 raw signal layer must remain current non-versioned evidence",
    )
    _require(
        signals.get("retrospective_2018_subset_required") is True,
        "v3 requires retrospective 2018 signal filtering",
    )
    _require(
        signals.get("retrospective_date_field") == "TURN_ON_DATE",
        "v3 signal historical filter must use TURN_ON_DATE",
    )
    _require(
        signals.get("retrospective_cutoff") == "2018-12-31T23:59:59.999Z",
        "v3 signal retrospective cutoff drift",
    )

    radar = families["traffic_radar"]
    _require(
        radar.get("temporal_role") == "HISTORICAL_2018_OBSERVATION_WHEN_FILTERED",
        "v3 radar observations must retain the frozen 2018 temporal role",
    )
    _require(
        radar.get("confirmatory_candidate_window") == "2018-01-01 through 2018-12-31",
        "v3 radar confirmatory window must remain calendar-year 2018",
    )
    radar_locations = families["radar_sensor_locations"]
    _require(
        radar_locations.get("temporal_role") == "RETROSPECTIVE_LOCATION_METADATA",
        "v3 radar location table must remain retrospective metadata",
    )
    _require(
        radar_locations.get("required_join_key") == "KITS_ID",
        "v3 radar location join must use KITS_ID",
    )
    _require(
        radar_locations.get("exact_2018_snapshot") is False,
        "v3 retrospective sensor locations cannot claim exact 2018 snapshot status",
    )

    flood = families["flood"]
    _require(
        flood.get("temporal_role") == "STATIC_SCENARIO_SUPPORT",
        "v3 floodplain must remain static scenario support",
    )
    _require(
        flood.get("event_time_depth_available") is False,
        "v3 static floodplain cannot claim event-time depth",
    )
    _require(
        flood.get("historical_2018_event_truth") is False,
        "v3 floodplain cannot claim historical 2018 event truth",
    )

    sig2018 = derived["traffic_signals_retrospective_2018"]
    _require(
        sig2018.get("survivorship_bias") is True,
        "v3 retrospective signal survivorship limitation must remain explicit",
    )
    _require(
        sig2018.get("complete_2018_inventory") is False,
        "v3 retrospective signals cannot claim complete 2018 inventory",
    )

    temporal = data.get("temporal_evidence")
    _require(isinstance(temporal, Mapping), "v3 temporal_evidence object is required")
    _require(
        temporal.get("protocol") == "project/AUSTIN_TEMPORAL_EVIDENCE_PROTOCOL_V1.md",
        "v3 temporal protocol identity drift",
    )
    _require(
        temporal.get("signal_source_semantics") == "PASS",
        "v3 signal source semantics must remain qualified",
    )
    _require(
        temporal.get("flood_static_semantics") == "PASS",
        "v3 flood static semantics must remain qualified",
    )


def validate_contract(data: Mapping[str, Any]) -> None:
    """Validate structural and scientific-control invariants.

    The validator deliberately does not infer PASS from source availability.
    Every gate must be explicitly closed by upstream materialization/QC.
    """
    version = data.get("version")
    _require(version in VERSION_AUTHORITIES, "unsupported Austin contract version")
    _require(data.get("case_id") == "AUS-P5U-2018-V1", "unexpected Austin case_id")
    _require(
        set(data.get("authority", [])) >= VERSION_AUTHORITIES[str(version)],
        "Austin contract is missing canonical authority files",
    )

    selection = data.get("selection")
    _require(isinstance(selection, Mapping), "selection object is required")
    _require(
        selection.get("smartds_version") == "v1.0",
        "SMART-DS version must remain v1.0",
    )
    _require(selection.get("smartds_year") == 2018, "SMART-DS year must remain 2018")
    _require(selection.get("smartds_city_code") == "AUS", "SMART-DS city code must be AUS")
    _require(
        selection.get("candidate_subregion") == "P5U",
        "candidate subregion must remain P5U until versioned change",
    )
    _require(
        selection.get("scenario") == "base_timeseries",
        "unexpected SMART-DS scenario",
    )
    _require(
        selection.get("selection_uses_hypothesis_results") is False,
        "subregion selection must not use H1-H5 outcomes",
    )

    families_raw = data.get("required_data_families")
    _require(
        isinstance(families_raw, list) and families_raw,
        "required_data_families must be non-empty",
    )
    families = _index_unique(families_raw, "id", "data family")
    _require(
        MANDATORY_DATA_IDS <= set(families),
        "one or more mandatory Austin data families are missing",
    )
    _require(
        bool(TRAFFIC_DATA_IDS & set(families)),
        "at least one traffic-observation family is required",
    )
    for item_id in MANDATORY_DATA_IDS:
        _require(
            families[item_id].get("mandatory") is True,
            f"{item_id} must remain mandatory",
        )

    if version in {"2.0", "3.0"}:
        _validate_2018_road_contract(families, version_label=f"v{version[0]}")

    derived_raw = data.get("derived_objects")
    _require(isinstance(derived_raw, list), "derived_objects must be a list")
    derived = _index_unique(derived_raw, "id", "derived object")
    required_derived = DERIVED_IDS_V3 if version == "3.0" else DERIVED_IDS
    _require(
        required_derived <= set(derived),
        "Austin P→T/T→P derived objects are incomplete",
    )

    if version == "3.0":
        _validate_v3_temporal_contract(data, families, derived)

    gates = data.get("gates")
    _require(isinstance(gates, Mapping), "gates object is required")
    _require(
        set(gates) == set(REQUIRED_GATE_IDS),
        "Austin gate set must be exactly G0--G8",
    )
    _require(
        gates["G0_canonical_consistency"] == "PASS",
        "canonical consistency G0 must remain PASS",
    )

    final = data.get("final_case_admissibility")
    _require(isinstance(final, bool), "final_case_admissibility must be boolean")

    all_pass = all(gates[name] == "PASS" for name in REQUIRED_GATE_IDS)
    if final:
        _require(
            all_pass,
            "final Austin admissibility requires every G0--G8 gate to PASS",
        )
        _require(
            selection.get("candidate_is_frozen") is True,
            "final Austin case requires frozen subregion",
        )

        for item_id in MANDATORY_DATA_IDS:
            _require(
                families[item_id].get("source_qualified") is True,
                f"{item_id} source must be qualified",
            )
            _require(
                families[item_id].get("spatial_overlap_verified") is True,
                f"{item_id} spatial overlap is incomplete",
            )

        _require(
            families["power"].get("raw_materialized") is True,
            "final Austin case requires materialized SMART-DS P5U power data",
        )
        _require(
            families["road"].get("network_qa_pass") is True,
            "final Austin case requires road-network QA PASS",
        )
        _require(
            families["signals"].get("synthetic_power_mapping_verified") is True,
            "final Austin case requires verified semisynthetic signal-power mapping",
        )
        _require(
            any(
                families.get(tid, {}).get("spatial_overlap_verified") is True
                for tid in TRAFFIC_DATA_IDS
            ),
            "final Austin case requires at least one traffic-observation family with verified spatial overlap",
        )
        _require(
            derived["repair_access"].get("computable") is True,
            "T→P repair access must be computable",
        )
        _require(
            derived["p_to_t_signal_power_mapping"].get("computable") is True,
            "P→T signal-power mapping must be computable",
        )

        if version == "3.0":
            temporal = data["temporal_evidence"]
            _require(
                temporal.get("G_time") == "PASS",
                "final Austin v3 case requires temporal evidence G_time PASS",
            )
            _require(
                temporal.get("signal_retrospective_extraction") == "PASS",
                "final Austin v3 case requires nonempty retrospective signal extraction",
            )
            _require(
                temporal.get("radar_2018_observation_join") == "PASS",
                "final Austin v3 case requires verified 2018 radar/location join",
            )
            _require(
                temporal.get("flood_asset_intersection") == "PASS",
                "final Austin v3 case requires flood/asset intersection",
            )
            _require(
                derived["traffic_signals_retrospective_2018"].get("computable") is True,
                "final Austin v3 case requires computable retrospective signal subset",
            )
            _require(
                families["traffic_radar"].get("spatial_overlap_verified") is True,
                "final Austin v3 case requires qualified 2018 radar spatial overlap",
            )
            _require(
                families["traffic_radar"].get("chronological_or_event_split_frozen") is True,
                "final Austin v3 case requires frozen chronological/event-block traffic split",
            )
            _require(
                families["radar_sensor_locations"].get("2018_observation_join_verified") is True,
                "final Austin v3 case requires verified radar observation/location join",
            )
    else:
        _require(
            data.get("status") != "ADMISSIBLE_FROZEN",
            "non-final Austin contract cannot claim ADMISSIBLE_FROZEN status",
        )

    prohibitions = data.get("prohibitions")
    _require(
        isinstance(prohibitions, list) and len(prohibitions) >= 6,
        "scientific prohibitions are incomplete",
    )


def case_is_admissible(data: Mapping[str, Any]) -> bool:
    """Return the declared final case state after validation."""
    validate_contract(data)
    return bool(data["final_case_admissibility"])
