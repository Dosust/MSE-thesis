#!/usr/bin/env python3
"""Fail-closed P3 case/data qualification and execution-readiness summary."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Mapping

from methods.austin_case.admissibility import case_is_admissible, load_contract
from methods.austin_case.preconfirmatory import load_registry

CASE_ID = "AUS-P5U-2018-V1"

NORMALIZED_OPEN_GATE_STATE = {
    "G1_power_materialization": "BLOCKED",
    "G2_common_spatial_support": "DEFERRED",
    "G3_transport_topology": "DEFERRED",
    "G4_traffic_observations": "DEFERRED",
    "G5_p_to_t_mapping": "BLOCKED",
    "G6_t_to_p_repair_access": "BLOCKED",
    "G7_flood_exposure": "BLOCKED",
    "G8_qc_provenance": "DEFERRED",
}

RUNTIME_EVIDENCE = {
    "raw_v4": "raw_materialization_manifest_v4.json",
    "service_area": "austin_energy_service_area_manifest.json",
    "radar_prejoin": "radar_2018_prejoin_manifest.json",
    "travel_sensor_schema": "travel_sensor_schema_resolution_manifest.json",
}


def _read_json_if_present(path: Path) -> tuple[bool, Any | None]:
    if not path.exists():
        return False, None
    return True, json.loads(path.read_text(encoding="utf-8"))


def normalized_gate_states(contract: Mapping[str, Any]) -> dict[str, str]:
    gates = contract["gates"]
    if bool(contract.get("final_case_admissibility")):
        return {gate: "PASS" for gate in gates}

    out: dict[str, str] = {}
    for gate, raw in gates.items():
        if raw == "PASS":
            out[gate] = "PASS"
        else:
            out[gate] = NORMALIZED_OPEN_GATE_STATE.get(gate, "DEFERRED")
    return out


def runtime_evidence_summary(root: Path) -> dict[str, Any]:
    qa = root / "qa"
    result: dict[str, Any] = {}
    for evidence_id, filename in RUNTIME_EVIDENCE.items():
        path = qa / filename
        present, obj = _read_json_if_present(path)
        row: dict[str, Any] = {
            "path": str(path),
            "present": present,
            "scientific_effect": "EVIDENCE_PRESENCE_ONLY_NO_GATE_PROMOTION",
        }
        if isinstance(obj, Mapping):
            for key in (
                "case_id",
                "status",
                "state",
                "schema_status",
                "G4_traffic_observations",
            ):
                if key in obj:
                    row[key] = obj[key]
            if evidence_id == "raw_v4" and isinstance(
                obj.get("temporal_gate"), Mapping
            ):
                row["temporal_gate"] = dict(obj["temporal_gate"])
        result[evidence_id] = row
    return result


def build_readiness(
    contract: Mapping[str, Any],
    registry: Mapping[str, Any],
    root: Path,
) -> dict[str, Any]:
    if contract.get("case_id") != CASE_ID or registry.get("case_id") != CASE_ID:
        raise ValueError("P3 readiness received inconsistent case IDs")

    admissible = case_is_admissible(contract)
    return {
        "schema_version": "1.0",
        "case_id": CASE_ID,
        "p3_control_status": "PASS",
        "case_execution_status": "PASS" if admissible else "BLOCKED",
        "final_case_admissibility": admissible,
        "selection": {
            "candidate_subregion": contract["selection"]["candidate_subregion"],
            "candidate_is_frozen": contract["selection"]["candidate_is_frozen"],
            "selection_uses_hypothesis_results": contract["selection"][
                "selection_uses_hypothesis_results"
            ],
        },
        "contract_gate_states": dict(contract["gates"]),
        "p3_normalized_gate_states": normalized_gate_states(contract),
        "runtime_evidence": runtime_evidence_summary(root),
        "hypotheses": {f"H{i}": "NOT_TESTED" for i in range(1, 6)},
        "scientific_firewalls": [
            "P2 design PASS does not imply data PASS",
            "data PASS does not imply case-execution PASS",
            "case-execution PASS does not imply hypothesis support",
            "runtime evidence presence does not promote a contract gate",
            "BLOCKED prerequisite is not negative hypothesis evidence",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--contract", default="config/austin_case_admissibility_v3.json"
    )
    parser.add_argument(
        "--preregistry", default="config/austin_preconfirmatory_registry_v1.json"
    )
    parser.add_argument("--root", default="data/AUS-P5U-2018-V1")
    parser.add_argument(
        "--output",
        default=(
            "data/AUS-P5U-2018-V1/qa/"
            "p3_case_execution_readiness_manifest.json"
        ),
    )
    args = parser.parse_args()

    contract = load_contract(args.contract)
    registry = load_registry(args.preregistry)
    result = build_readiness(contract, registry, Path(args.root))

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
