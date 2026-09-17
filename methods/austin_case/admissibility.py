"""Fail-closed validation for the Austin case-study admissibility contract.

This module validates *research-control state*.  It does not download data,
compute scientific parameters, or adjudicate H1--H5.  Its purpose is to prevent
an Austin candidate case from being marked admissible before every frozen
pre-result data and mechanism gate has passed.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping


class AustinAdmissibilityError(ValueError):
    """Raised when the Austin admissibility contract violates a frozen rule."""


REQUIRED_AUTHORITIES = {
    "project/CANONICAL_7_STAGE_FRAMEWORK_V2.md",
    "project/CANONICAL_RQ_SO_HYPOTHESES_V3.md",
    "project/AUSTIN_CASE_STUDY_DATA_ADMISSIBILITY_MATRIX_V1.md",
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


def load_contract(path: str | Path) -> dict[str, Any]:
    """Load and validate a JSON contract from disk."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    validate_contract(data)
    return data


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise AustinAdmissibilityError(message)


def _index_unique(items: list[Mapping[str, Any]], key: str, label: str) -> dict[str, Mapping[str, Any]]:
    out: dict[str, Mapping[str, Any]] = {}
    for item in items:
        _require(isinstance(item, Mapping), f"{label} entries must be objects")
        value = item.get(key)
        _require(isinstance(value, str) and value, f"{label} entry missing non-empty {key}")
        _require(value not in out, f"duplicate {label} {key}: {value}")
        out[value] = item
    return out


def validate_contract(data: Mapping[str, Any]) -> None:
    """Validate structural and scientific-control invariants.

    The validator deliberately does not infer PASS from source availability.
    Every gate must be explicitly closed by upstream materialization/QC.
    """
    _require(data.get("version") == "1.0", "expected Austin contract version 1.0")
    _require(data.get("case_id") == "AUS-P5U-2018-V1", "unexpected Austin case_id")
    _require(
        set(data.get("authority", [])) >= REQUIRED_AUTHORITIES,
        "Austin contract is missing canonical authority files",
    )

    selection = data.get("selection")
    _require(isinstance(selection, Mapping), "selection object is required")
    _require(selection.get("smartds_version") == "v1.0", "SMART-DS version must remain v1.0")
    _require(selection.get("smartds_year") == 2018, "SMART-DS year must remain 2018")
    _require(selection.get("smartds_city_code") == "AUS", "SMART-DS city code must be AUS")
    _require(selection.get("candidate_subregion") == "P5U", "candidate subregion must remain P5U until versioned change")
    _require(selection.get("scenario") == "base_timeseries", "unexpected SMART-DS scenario")
    _require(
        selection.get("selection_uses_hypothesis_results") is False,
        "subregion selection must not use H1-H5 outcomes",
    )

    families_raw = data.get("required_data_families")
    _require(isinstance(families_raw, list) and families_raw, "required_data_families must be non-empty")
    families = _index_unique(families_raw, "id", "data family")
    _require(MANDATORY_DATA_IDS <= set(families), "one or more mandatory Austin data families are missing")
    _require(bool(TRAFFIC_DATA_IDS & set(families)), "at least one traffic-observation family is required")
    for item_id in MANDATORY_DATA_IDS:
        _require(families[item_id].get("mandatory") is True, f"{item_id} must remain mandatory")

    derived_raw = data.get("derived_objects")
    _require(isinstance(derived_raw, list), "derived_objects must be a list")
    derived = _index_unique(derived_raw, "id", "derived object")
    _require(DERIVED_IDS <= set(derived), "Austin P→T/T→P derived objects are incomplete")

    gates = data.get("gates")
    _require(isinstance(gates, Mapping), "gates object is required")
    _require(set(gates) == set(REQUIRED_GATE_IDS), "Austin gate set must be exactly G0--G8")
    _require(gates["G0_canonical_consistency"] == "PASS", "canonical consistency G0 must remain PASS")

    final = data.get("final_case_admissibility")
    _require(isinstance(final, bool), "final_case_admissibility must be boolean")

    all_pass = all(gates[name] == "PASS" for name in REQUIRED_GATE_IDS)
    if final:
        _require(all_pass, "final Austin admissibility requires every G0--G8 gate to PASS")
        _require(selection.get("candidate_is_frozen") is True, "final Austin case requires frozen subregion")
        for item_id in MANDATORY_DATA_IDS:
            _require(families[item_id].get("source_qualified") is True, f"{item_id} source must be qualified")
            _require(
                families[item_id].get("spatial_overlap_verified") is True
                or item_id == "power" and families[item_id].get("raw_materialized") is True,
                f"{item_id} spatial/raw qualification is incomplete",
            )
        _require(
            any(families.get(tid, {}).get("spatial_overlap_verified") is True for tid in TRAFFIC_DATA_IDS),
            "final Austin case requires at least one traffic-observation family with verified spatial overlap",
        )
        _require(derived["repair_access"].get("computable") is True, "T→P repair access must be computable")
        _require(
            derived["p_to_t_signal_power_mapping"].get("computable") is True,
            "P→T signal-power mapping must be computable",
        )
    else:
        _require(
            data.get("status") != "ADMISSIBLE_FROZEN",
            "non-final Austin contract cannot claim ADMISSIBLE_FROZEN status",
        )

    prohibitions = data.get("prohibitions")
    _require(isinstance(prohibitions, list) and len(prohibitions) >= 6, "scientific prohibitions are incomplete")


def case_is_admissible(data: Mapping[str, Any]) -> bool:
    """Return the declared final case state after validation."""
    validate_contract(data)
    return bool(data["final_case_admissibility"])
