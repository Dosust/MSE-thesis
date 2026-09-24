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
from .surrogate import LinearVectorFieldSurrogate, train_surrogate, validation_rmse

__all__ = [
    "CriticalityResult", "LinearVectorFieldSurrogate", "Derivative", "DiagonalMetric",
    "Parameters", "Sample", "State", "SustainableConstraints", "annotate_margins",
    "build_experiment", "constraint_margin", "gaussian_flood", "minimum_margin",
    "parameter_criticality", "simulate", "train_surrogate", "validation_rmse",
    "vector_field", "write_experiment",
]
