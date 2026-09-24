"""Reproducible experiment and browser-data export for the Viability Explorer."""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict
from pathlib import Path

from .core import Parameters, State, simulate, thin
from .geometry import DiagonalMetric, SustainableConstraints, annotate_margins, parameter_criticality
from .surrogate import train_surrogate, validation_rmse

SCHEMA_VERSION = "ive-demo-0.1.0"


def build_experiment(*, sample_every: int = 4) -> dict:
    params = Parameters()
    constraints = SustainableConstraints()
    metric = DiagonalMetric()
    initial = State(0.96, 0.95, 0.93)

    annotated = annotate_margins(simulate(initial=initial, params=params), constraints, metric)
    samples = list(thin(annotated, sample_every))
    surrogate_rmse = validation_rmse(train_surrogate(params), params)
    diagnostics = [
        parameter_criticality(parameter=name, params=params)
        for name in ("transport_to_power", "power_to_transport", "interface_hazard")
    ]

    payload = {
        "schema_version": SCHEMA_VERSION,
        "status": "synthetic_demonstrator_not_empirically_calibrated",
        "semantics": {
            "state": {
                "power": "normalized power service in [0,1]",
                "transport": "normalized transport service in [0,1]",
                "interface": "normalized P-T interface health in [0,1]",
            },
            "margin": "signed distance-to-threshold proxy under a diagonal metric; not a viability kernel",
            "criticality": "finite-difference model sensitivity; not causal identification",
        },
        "initial_state": asdict(initial),
        "parameters": asdict(params),
        "constraints": asdict(constraints),
        "metric": asdict(metric),
        "samples": [
            {
                "time": round(s.time, 10),
                "hazard": round(s.hazard, 10),
                "power": round(s.state.power, 10),
                "transport": round(s.state.transport, 10),
                "interface": round(s.state.interface, 10),
                "margin": round(float(s.margin), 10),
            }
            for s in samples
        ],
        "ml_surrogate": {
            "status": "trained_and_validated_on_synthetic_simulator_only",
            "model": "transparent ridge regression over declared nonlinear features",
            "holdout_rmse": surrogate_rmse,
        },
        "criticality": [asdict(d) for d in diagnostics],
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    payload["sha256_without_hash_field"] = hashlib.sha256(canonical).hexdigest()
    return payload


def write_experiment(path: str | Path) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(build_experiment(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path
