import json
from pathlib import Path

from methods.austin_case.admissibility import load_contract
from methods.austin_case.p3_execution_readiness import (
    build_readiness,
    experiment_object_readiness,
    normalized_gate_states,
    repository_execution_status,
)
from methods.austin_case.preconfirmatory import load_registry

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "config" / "austin_case_admissibility_v3.json"
REGISTRY = ROOT / "config" / "austin_preconfirmatory_registry_v1.json"
REPO_READINESS = ROOT / "config" / "p3_repository_execution_readiness_v1.json"


def _repo_readiness():
    return json.loads(REPO_READINESS.read_text(encoding="utf-8"))


def test_current_p3_readiness_is_fail_closed(tmp_path):
    contract = load_contract(CONTRACT)
    registry = load_registry(REGISTRY)
    result = build_readiness(
        contract,
        registry,
        tmp_path / "no-runtime-data",
        _repo_readiness(),
    )

    assert result["p3_control_status"] == "PASS"
    assert result["case_admissibility_status"] == "BLOCKED"
    assert result["repository_execution_status"] == "BLOCKED"
    assert result["experiment_object_readiness_status"] == "BLOCKED"
    assert result["experiment_execution_status"] == "BLOCKED"
    assert result["final_case_admissibility"] is False
    assert result["selection"]["candidate_is_frozen"] is False
    assert result["selection"]["selection_uses_hypothesis_results"] is False
    assert set(result["hypotheses"].values()) == {"NOT_TESTED"}


def test_repository_runner_gate_is_explicit_and_blocking():
    readiness = _repo_readiness()
    assert readiness["gates"]["G_runner"] == "BLOCKED"
    assert repository_execution_status(readiness) == "BLOCKED"


def test_case_admissibility_cannot_authorize_experiment_execution(tmp_path):
    contract = load_contract(CONTRACT)
    registry = load_registry(REGISTRY)
    contract = dict(contract)
    contract["final_case_admissibility"] = True
    contract["selection"] = dict(contract["selection"])
    contract["selection"]["candidate_is_frozen"] = True
    contract["gates"] = {key: "PASS" for key in contract["gates"]}

    result = build_readiness(contract, registry, tmp_path, _repo_readiness())
    assert result["case_admissibility_status"] == "PASS"
    assert result["repository_execution_status"] == "BLOCKED"
    assert result["experiment_execution_status"] == "BLOCKED"


def test_required_object_set_is_fail_closed_until_frozen():
    registry = load_registry(REGISTRY)
    gate = experiment_object_readiness(registry)
    assert gate["notation"] == "O_req(E)"
    assert gate["required_object_set_status"] == "OPEN_NOT_FROZEN"
    assert gate["status"] == "BLOCKED"


def test_current_normalized_gate_state_preserves_blocked_and_deferred():
    contract = load_contract(CONTRACT)
    gates = normalized_gate_states(contract)

    assert gates["G0_canonical_consistency"] == "PASS"
    for gate in (
        "G1_power_materialization",
        "G5_p_to_t_mapping",
        "G6_t_to_p_repair_access",
        "G7_flood_exposure",
    ):
        assert gates[gate] == "BLOCKED"
    for gate in (
        "G2_common_spatial_support",
        "G3_transport_topology",
        "G4_traffic_observations",
        "G8_qc_provenance",
    ):
        assert gates[gate] == "DEFERRED"


def test_runtime_file_presence_cannot_promote_contract_gate(tmp_path):
    qa = tmp_path / "qa"
    qa.mkdir(parents=True)
    (qa / "raw_materialization_manifest_v4.json").write_text(
        json.dumps(
            {
                "case_id": "AUS-P5U-2018-V1",
                "status": "RAW_MATERIALIZATION_ONLY",
                "temporal_gate": {"signal_retrospective_extraction": "PASS"},
            }
        ),
        encoding="utf-8",
    )

    contract = load_contract(CONTRACT)
    registry = load_registry(REGISTRY)
    result = build_readiness(contract, registry, tmp_path, _repo_readiness())

    assert result["runtime_evidence"]["raw_v4"]["present"] is True
    assert (
        result["p3_normalized_gate_states"]["G1_power_materialization"]
        == "BLOCKED"
    )
    assert result["experiment_execution_status"] == "BLOCKED"


def test_source_contract_remains_candidate_not_admissible():
    contract = load_contract(CONTRACT)
    assert contract["status"] == "CANDIDATE_NOT_YET_ADMISSIBLE"
    assert contract["final_case_admissibility"] is False
    assert contract["gates"]["G0_canonical_consistency"] == "PASS"
