"""Infrastructure Viability Explorer synthetic demonstrator."""

from .core import Derivative, Parameters, Sample, State, gaussian_flood, simulate, vector_field
from .experiment import build_experiment, write_experiment
from .geometry import (
    CriticalityResult,
    DiagonalMetric,
    SustainableConstraints,
    annotate_margins,
    constraint_margin,
    minimum_margin,
    parameter_criticality,
)
from .graph import (
    Edge,
    MultilayerGraph,
    Node,
    default_multilayer_graph,
    graph_payload,
    graph_snapshot,
    spatial_hazard,
)
from .surrogate import LinearVectorFieldSurrogate, train_surrogate, validation_rmse

__all__ = [
    "CriticalityResult", "LinearVectorFieldSurrogate", "Derivative", "DiagonalMetric",
    "Edge", "MultilayerGraph", "Node", "Parameters", "Sample", "State",
    "SustainableConstraints", "annotate_margins", "build_experiment",
    "constraint_margin", "default_multilayer_graph", "gaussian_flood", "graph_payload",
    "graph_snapshot", "minimum_margin", "parameter_criticality", "simulate",
    "spatial_hazard", "train_surrogate", "validation_rmse", "vector_field",
    "write_experiment",
]
