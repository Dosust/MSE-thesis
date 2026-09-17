"""Fail-closed validation for the Austin preconfirmatory scientific registry."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping


class PreconfirmatoryRegistryError(ValueError):
    """Raised when a preconfirmatory scientific-control rule is violated."""


EXPECTED_INTERDEPENDENCIES = {"PT_SIGNAL_POWER", "TP_REPAIR_ACCESS"}
EXPECTED_UNCERTAINTY_SOURCES = {
    "hazard", "demand", "repair", "interdependency", "observation", "model_form", "numerical"
}
EXPECTED_HYPOTHESES = {f"H{i}" for i in range(1, 6)}


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise PreconfirmatoryRegistryError(message)


def _index(items: list[Mapping[str, Any]], key: str, label: str) -> dict[str, Mapping[str, Any]]:
    out: dict[str, Mapping[str, Any]] = {}
    for item in items:
        _require(isinstance(item, Mapping), f"{label} rows must be objects")
        value = item.get(key)
        _require(isinstance(value, str) and value, f"{label} row missing {key}")
        _require(value not in out, f"duplicate {label} {value}")
        out[value] = item
    return out


def validate_registry(data: Mapping[str, Any]) -> None:
    _require(data.get("version") == "1.0", "expected version 1.0")
    _require(data.get("case_id") == "AUS-P5U-2018-V1", "unexpected case_id")
    _require(
        data.get("status") == "PRECONFIRMATORY_STRUCTURE_FROZEN_VALUES_OPEN",
        "preconfirmatory registry must not claim executed/final status",
    )

    deps = _index(data.get("interdependencies", []), "id", "interdependency")
    _require(set(deps) == EXPECTED_INTERDEPENDENCIES, "primary Austin mechanism set drifted")
    _require(deps["PT_SIGNAL_POWER"].get("direction") == "P->T", "PT signal direction must be P->T")
    _require(deps["TP_REPAIR_ACCESS"].get("direction") == "T->P", "repair access direction must be T->P")
    for row in deps.values():
        _require(len(row.get("evidence", [])) >= 2, "each mechanism requires multiple evidence anchors")
        _require("OPEN" in str(row.get("status", "")), "mechanism must remain open until mapping/parameters close")

    common = _index(data.get("common_cause_pathways", []), "id", "common-cause pathway")
    flood = common.get("FLOOD_COMMON_CAUSE")
    _require(flood is not None, "flood common-cause pathway is required")
    _require(flood.get("is_interdependency") is False, "common flood exposure must not be labeled interdependency")

    params = _index(data.get("parameter_registry", []), "id", "parameter")
    _require(params, "parameter registry must not be empty")
    for row in params.values():
        _require(str(row.get("status", "")).startswith("OPEN"), "empirical parameters must remain OPEN before data qualification")
        _require(row.get("range") == "OPEN", "parameter range cannot be prefilled without evidence")
        _require(row.get("uncertainty") == "OPEN", "parameter uncertainty cannot be prefilled without evidence")

    thresholds = _index(data.get("threshold_registry", []), "id", "threshold")
    _require({"K_POWER_PHYSICAL", "K_SP", "K_ST", "G_REC", "TV_TR"} <= set(thresholds), "threshold registry incomplete")
    for row in thresholds.values():
        _require("OPEN" in str(row.get("value", "")), "case thresholds must remain open before provenance closes")

    unc = data.get("uncertainty_registry", [])
    _require(isinstance(unc, list) and unc, "uncertainty registry required")
    sources = {row.get("source") for row in unc if isinstance(row, Mapping)}
    _require(EXPECTED_UNCERTAINTY_SOURCES <= sources, "uncertainty-source taxonomy incomplete")
    for row in unc:
        law = str(row.get("probability_law", ""))
        _require(not (law and law not in {"NONE", "NONE_UNTIL_QUALIFIED"}), "probability law frozen before probability-admissibility gate")

    prereg = data.get("preregistration")
    _require(isinstance(prereg, Mapping), "preregistration object required")
    _require(set(prereg) == EXPECTED_HYPOTHESES, "H1-H5 preregistration set must be exact")
    for hid, row in prereg.items():
        _require(row.get("matched_inputs_required") is True, f"{hid} must require matched inputs")
        _require("OPEN" in str(row.get("delta", "")), f"{hid} materiality threshold must remain open")
        _require(row.get("status") in {"NOT_AUTHORIZED", "DEFERRED_UPSTREAM", "DEFERRED_H4"}, f"{hid} cannot be executed yet")

    rules = data.get("global_rules", [])
    text = " ".join(str(x) for x in rules)
    _require("Verification PASS does not imply hypothesis support" in text, "verification/hypothesis separation rule missing")
    _require("Common hazard exposure is not" in text, "common-cause separation rule missing")


def load_registry(path: str | Path) -> dict[str, Any]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    validate_registry(data)
    return data
