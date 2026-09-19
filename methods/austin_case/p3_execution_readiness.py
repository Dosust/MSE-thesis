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

REQUIRED_REPOSITORY_GATES = (
    "G_runner",
    "G_syntax",
    "G_tests",
    "G_authority_lint",
    "G_case_instrument",
)

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


def repository_execution_status(repo_readiness: Mapping[str, Any]) -> str:
    gates = repo_readiness.get("gates")
    if not isinstance(gates, Mapping):
        raise ValueError("repository readiness must contain gates")
    missing = [gate for gate in REQUIRED_REPOSITORY_GATES if gate not in gates]
    if missing:
        raise ValueError(f"repository readiness missing gates: {missing}")

    states = [str(gates[gate]) for gate in REQUIRED_REPOSITORY_GATES]
    if "FAIL" in states:
        return "FAIL"
    if "BLOCKED" in states:
        return "BLOCKED"
    if any(state in {"DEFERRED", "OPEN", "NOT_TESTED"} for state in states):
        return "DEFERRED"
    if all(state == "PASS" for state in states):
        return "PASS"
    raise ValueError(f"unsupported repository gate states: {states}")


def experiment_object_readiness(registry: Mapping[str, Any]) -> dict[str, Any]:
    """Fail closed until each experiment has a frozen O_req(E) mapping."""
    required = registry.get("experiment_required_objects")
    if not isinstance(required, Mapping):
        return {
            "required_object_set_status": "OPEN_NOT_FROZEN",
            "status": "BLOCKED",
            "notation": "O_req(E)",
            "reason": (
                "No versioned experiment_required_objects mapping exists; "
                "experiment execution cannot be authorized."
            ),
        }

    per_experiment: dict[str, str] = {}
    for experiment_id, record in required.items():
        if not isinstance(record, Mapping):
            per_experiment[str(experiment_id)] = "BLOCKED"
            continue
        object_states = record.get("object_readiness")
        if not isinstance(object_states, Mapping) or not object_states:
            per_experiment[str(experiment_id)] = "BLOCKED"
            continue
        states = [str(value) for value in object_states.values()]
        per_experiment[str(experiment_id)] = (
            "PASS" if all(value == "PASS" for value in states) else "BLOCKED"
        )

    overall = (
        "PASS"
        if per_experiment and all(value == "PASS" for value in per_experiment.values())
        else "BLOCKED"
    )
    return {
        "required_object_set_status": "FROZEN",
        "status": overall,
        "notation": "O_req(E)",
        "per_experiment": per_experiment,
    }


def build_readiness(
    contract: Mapping[str, Any],
    registry: Mapping[str, Any],
    root: Path,
    repo_readiness: Mapping[str, Any],
) -> dict[str, Any]:
    if contract.get("case_id") != CASE_ID or registry.get("case_id") != CASE_ID:
        raise ValueError("P3 readiness received inconsistent case IDs")

    admissible = case_is_admissible(contract)
    case_status = "PASS" if admissible else "BLOCKED"
    repo_status = repository_execution_status(repo_readiness)
    object_gate = experiment_object_readiness(registry)
    object_status = str(object_gate["status"])
    experiment_status = (
        "PASS"
        if case_status == "PASS"
        and repo_status == "PASS"
        and object_status == "PASS"
        else "BLOCKED"
    )

    return {
        "schema_version": "1.1",
        "case_id": CASE_ID,
        "p3_control_status": "PASS",
        "case_admissibility_status": case_status,
        "repository_execution_status": repo_status,
        "repository_execution_gates": dict(repo_readiness["gates"]),
        "experiment_object_readiness_status": object_status,
        "experiment_object_readiness": object_gate,
        "experiment_execution_status": experiment_status,
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
            "case admissibility PASS does not imply repository execution PASS",
            "case admissibility PASS does not imply experiment execution PASS",
            "repository execution PASS does not imply experiment object readiness",
            "experiment execution PASS does not imply hypothesis support",
            "pre-runner assignment failure is not a test or data-gate failure",
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
    parser.add_argument(
        "--repo-readiness",
        default="config/p3_repository_execution_readiness_v1.json",
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
    repo_readiness = json.loads(
        Path(args.repo_readiness).read_text(encoding="utf-8")
    )
    result = build_readiness(contract, registry, Path(args.root), repo_readiness)

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
