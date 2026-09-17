#!/usr/bin/env python3
from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path
from typing import Any


class ProtocolError(ValueError):
    pass


def _read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise ProtocolError(f"missing registry: {path}")
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _nonempty(x: Any) -> bool:
    return x is not None and x != "" and x != [] and x != {}


def evaluate_protocol(protocol_path: str | Path, root: str | Path | None = None) -> dict[str, Any]:
    protocol_path = Path(protocol_path)
    p = json.loads(protocol_path.read_text(encoding="utf-8"))
    root_path = Path(root) if root is not None else protocol_path.parent.parent

    required_top = ["authority", "hypothesis", "spatial_case", "interfaces", "hazard", "scenario_design", "parameters", "reference", "qoi", "validation", "uq", "execution_gates"]
    structural = {f"S_{k}": k in p for k in required_top}
    structural["S_H1"] = p.get("hypothesis", {}).get("id") == "H1"
    structural["S_models"] = p.get("hypothesis", {}).get("models") == ["M0", "M1", "M2"]
    structural["S_outcome_blind"] = p.get("spatial_case", {}).get("selection_outcome_blind") is True
    structural["S_rho_deferred"] = str(p.get("qoi", {}).get("rho_g_status", "")).startswith("DEFERRED_TO_STAGE5")
    structural["S_authorization_boolean"] = isinstance(p.get("confirmatory_execution_authorized"), bool)

    dep_path = root_path / p.get("interfaces", {}).get("registry", "")
    par_path = root_path / p.get("parameters", {}).get("registry", "")
    qoi_path = root_path / p.get("qoi", {}).get("registry", "")
    scen_path = root_path / p.get("scenario_design", {}).get("matrix", "")

    registries: dict[str, bool] = {}
    try:
        deps = _read_csv(dep_path)
        required_mech = set(p["interfaces"]["required_directed_mechanisms"])
        registries["R_dependency_mechanisms_present"] = required_mech.issubset({r.get("dependency_id", "") for r in deps})
        registries["R_dependency_provenance_present"] = all(r.get("provenance_source") and r.get("evidence_state") for r in deps)
    except (ProtocolError, KeyError):
        deps = []
        registries["R_dependency_mechanisms_present"] = False
        registries["R_dependency_provenance_present"] = False

    try:
        pars = _read_csv(par_path)
        registries["R_parameter_uncertainty_typed"] = bool(pars) and all(r.get("uncertainty_type") for r in pars)
        registries["R_parameter_source_level_present"] = bool(pars) and all(r.get("source_level") for r in pars)
    except ProtocolError:
        pars = []
        registries["R_parameter_uncertainty_typed"] = False
        registries["R_parameter_source_level_present"] = False

    try:
        qois = _read_csv(qoi_path)
        families = set(p["qoi"]["primary_H1_families"])
        registries["R_primary_qoi_families_present"] = families.issubset({r.get("family", "") for r in qois if r.get("role") == "PRIMARY_H1"})
        registries["R_rho_not_primary"] = not any(r.get("qoi_id") == "rho_g" and r.get("role") == "PRIMARY_H1" for r in qois)
    except (ProtocolError, KeyError):
        qois = []
        registries["R_primary_qoi_families_present"] = False
        registries["R_rho_not_primary"] = False

    try:
        scens = _read_csv(scen_path)
        models = {r.get("model", "") for r in scens if r.get("experiment_class") == "MATCHED_MAIN"}
        registries["R_main_models_present"] = {"M0", "M1", "M2"}.issubset(models)
        registries["R_common_random_group_present"] = all(r.get("common_random_group") for r in scens if r.get("experiment_class") == "MATCHED_MAIN")
    except ProtocolError:
        scens = []
        registries["R_main_models_present"] = False
        registries["R_common_random_group_present"] = False

    s = p.get("spatial_case", {})
    h = p.get("hazard", {})
    q = p.get("qoi", {})
    v = p.get("validation", {})
    u = p.get("uq", {})
    ref = p.get("reference", {})
    scenario = p.get("scenario_design", {})
    freeze = {
        "F_development_feeder": _nonempty(s.get("development_feeder_id")),
        "F_heldout_feeder": _nonempty(s.get("heldout_feeder_id")),
        "F_feeders_distinct": _nonempty(s.get("development_feeder_id")) and _nonempty(s.get("heldout_feeder_id")) and s.get("development_feeder_id") != s.get("heldout_feeder_id"),
        "F_hazard_values": h.get("rainfall_depth_values_frozen") is True and h.get("hydraulic_geometry_frozen") is True,
        "F_seed_manifest": scenario.get("seed_manifest_frozen") is True,
        "F_parameters": p.get("parameters", {}).get("required_parameter_rows_frozen") is True,
        "F_reference": _nonempty(ref.get("qualified_reference_id")),
        "F_primary_metrics": q.get("exact_primary_metrics_frozen") is True,
        "F_validation_thresholds": v.get("numerical_thresholds_frozen") is True,
        "F_R1_R8": v.get("data_qualification_R1_R8") == "PASS",
        "F_split": v.get("candidate_train_test_split") == "FROZEN",
        "F_uq_convergence": u.get("convergence_rule_frozen") is True,
        "F_confirmatory_authorization": p.get("confirmatory_execution_authorized") is True
    }

    all_structural = all(structural.values()) and all(registries.values())
    confirmatory_ready = all_structural and all(freeze.values())
    status = "CONFIRMATORY_READY" if confirmatory_ready else ("METHOD_FROZEN_INPUTS_OPEN" if all_structural else "STRUCTURAL_PROTOCOL_FAILURE")
    return {
        "protocol_id": p.get("protocol_id"),
        "status": status,
        "structural_gates": structural,
        "registry_gates": registries,
        "freeze_gates": freeze,
        "confirmatory_ready": confirmatory_ready,
        "claim_boundary": "A passed structural protocol does not authorize H1 confirmation. Confirmatory claims require every freeze gate and the repository-level authorization gate."
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--protocol", required=True)
    ap.add_argument("--root", default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--require-confirmatory", action="store_true")
    args = ap.parse_args()
    result = evaluate_protocol(args.protocol, args.root)
    text = json.dumps(result, indent=2) + "\n"
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    if result["status"] == "STRUCTURAL_PROTOCOL_FAILURE":
        raise SystemExit(2)
    if args.require_confirmatory and not result["confirmatory_ready"]:
        raise SystemExit(3)


if __name__ == "__main__":
    main()
