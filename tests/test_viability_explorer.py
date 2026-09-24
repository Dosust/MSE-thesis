import hashlib
import json
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from models.viability_explorer import (
    DiagonalMetric,
    Parameters,
    State,
    SustainableConstraints,
    annotate_margins,
    build_experiment,
    constraint_margin,
    default_multilayer_graph,
    gaussian_flood,
    graph_snapshot,
    parameter_criticality,
    simulate,
    spatial_hazard,
    train_surrogate,
    validation_rmse,
    vector_field,
)


def test_gaussian_flood_is_bounded_and_peaks_at_declared_amplitude():
    assert gaussian_flood(8.0) == pytest.approx(0.92)
    assert 0.0 <= gaussian_flood(-100.0) <= 1.0
    assert 0.0 <= gaussian_flood(100.0) <= 1.0


def test_vector_field_points_inward_on_service_boundaries():
    p = Parameters()
    low = vector_field(State(0.0, 0.0, 0.0), 0.8, p)
    high = vector_field(State(1.0, 1.0, 1.0), 0.8, p)
    assert low.power >= 0 and low.transport >= 0 and low.interface >= 0
    assert high.power <= 0 and high.transport <= 0 and high.interface <= 0


def test_simulation_is_deterministic_and_bounded():
    a = simulate(duration=4.0, dt=0.05)
    b = simulate(duration=4.0, dt=0.05)
    assert a == b
    assert len(a) == 81
    for s in a:
        s.state.validate()
        assert 0.0 <= s.hazard <= 1.0


def test_rk4_refinement_shows_monotone_terminal_convergence():
    def terminal(dt):
        return simulate(duration=24.0, dt=dt)[-1].state

    def max_norm(a, b):
        return max(
            abs(a.power - b.power),
            abs(a.transport - b.transport),
            abs(a.interface - b.interface),
        )

    s020 = terminal(0.20)
    s010 = terminal(0.10)
    s005 = terminal(0.05)
    s0025 = terminal(0.025)

    e1 = max_norm(s020, s010)
    e2 = max_norm(s010, s005)
    e3 = max_norm(s005, s0025)

    assert e3 < e2 < e1
    assert e3 < 1e-9


def test_constraint_margin_sign_and_metric_semantics():
    c = SustainableConstraints(0.6, 0.6, 0.6)
    m = DiagonalMetric(4.0, 1.0, 1.0)
    assert constraint_margin(State(0.7, 0.8, 0.9), c, m) == pytest.approx(0.2)
    assert constraint_margin(State(0.5, 0.8, 0.9), c, m) == pytest.approx(-0.2)


def test_margin_annotation_matches_sample_count():
    samples = simulate(duration=1.0, dt=0.05)
    annotated = annotate_margins(samples)
    assert len(annotated) == len(samples)
    assert all(s.margin is not None for s in annotated)


def test_parameter_criticality_is_finite_and_reproducible():
    r1 = parameter_criticality(parameter="power_to_transport", duration=6.0, dt=0.05)
    r2 = parameter_criticality(parameter="power_to_transport", duration=6.0, dt=0.05)
    assert r1 == r2
    assert abs(r1.sensitivity) < 100


def test_invalid_parameter_criticality_is_rejected():
    with pytest.raises(ValueError):
        parameter_criticality(parameter="not_a_parameter")


def test_default_multilayer_graph_is_structurally_valid():
    graph = default_multilayer_graph()
    graph.validate()
    node_layers = {n.id: n.layer for n in graph.nodes}
    interfaces = [e for e in graph.edges if e.layer == "interface"]
    assert len(graph.nodes) == 9
    assert len(interfaces) == 2
    assert all(node_layers[e.source] != node_layers[e.target] for e in interfaces)


def test_spatial_hazard_is_bounded_and_spatially_nonuniform():
    center = spatial_hazard(8.0, 0.56, 0.58)
    corner = spatial_hazard(8.0, 0.0, 0.0)
    assert 0.0 <= corner <= center <= 1.0
    assert center > corner


def test_graph_snapshot_contains_bounded_node_and_edge_projections():
    graph = default_multilayer_graph()
    snapshot = graph_snapshot(graph, State(0.8, 0.7, 0.6), 8.0)
    assert set(snapshot["nodes"]) == {n.id for n in graph.nodes}
    assert set(snapshot["edges"]) == {e.id for e in graph.edges}
    assert all(0.0 <= x["hazard"] <= 1.0 for x in snapshot["nodes"].values())
    assert all(0.0 <= x["availability"] <= 1.0 for x in snapshot["nodes"].values())
    assert all(0.0 <= x["activity"] <= 1.0 for x in snapshot["edges"].values())


def test_experiment_payload_has_explicit_epistemic_boundary_and_valid_hash():
    payload = build_experiment(sample_every=10)
    assert payload["schema_version"] == "ive-demo-0.2.0"
    assert payload["status"] == "synthetic_demonstrator_not_empirically_calibrated"
    assert "not a viability kernel" in payload["semantics"]["margin"]
    assert "not physical network-flow solutions" in payload["semantics"]["graph"]
    digest = payload.pop("sha256_without_hash_field")
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    assert hashlib.sha256(canonical).hexdigest() == digest


def test_experiment_contains_required_synchronized_variables():
    payload = build_experiment(sample_every=20)
    row = payload["samples"][0]
    assert {"time", "hazard", "power", "transport", "interface", "margin", "graph_state"} <= set(row)
    assert {"nodes", "edges"} <= set(row["graph_state"])
    assert len(payload["graph"]["nodes"]) == 9


def test_large_time_step_is_rejected_to_protect_numerical_reliability():
    with pytest.raises(ValueError):
        simulate(duration=1.0, dt=0.5)


def test_transparent_ml_surrogate_reconstructs_synthetic_vector_field_on_holdout():
    model = train_surrogate()
    rmse = validation_rmse(model)
    assert max(rmse.values()) < 1e-6


def test_experiment_labels_ml_scope_as_synthetic_only():
    payload = build_experiment(sample_every=20)
    assert payload["ml_surrogate"]["status"] == "trained_and_validated_on_synthetic_simulator_only"
