"""Canonical dependency contract primitives.

Implements d_e = (C_e, Sigma_e, Pi_e) without embedding service metrics or
runtime/software metadata inside the dependency primitive.
"""
from dataclasses import dataclass, field
from typing import Any, Callable, Mapping, Optional, Tuple


@dataclass(frozen=True)
class Composition:
    source: str
    source_port: str
    receiver: str
    receiver_port: str
    carrier: str


@dataclass(frozen=True)
class CausalSemantics:
    operator: Callable[[Any, Any, Mapping[str, Any], Any], Any]
    guard: Callable[[Mapping[str, Any]], bool]
    parameters: Mapping[str, Any] = field(default_factory=dict)
    internal_state: Any = None


@dataclass(frozen=True)
class Epistemic:
    provenance: Tuple[str, ...]
    validation_state: str
    uncertainty: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class Dependency:
    composition: Composition
    semantics: CausalSemantics
    epistemic: Epistemic


def evaluate_dependency(
    dependency: Dependency,
    source_state: Any,
    receiver_state: Any,
    context: Optional[Mapping[str, Any]] = None,
) -> Any:
    """Evaluate the declared causal operator iff its guard is active."""
    ctx: Mapping[str, Any] = {} if context is None else context
    if not dependency.semantics.guard(ctx):
        return 0.0
    return dependency.semantics.operator(
        source_state,
        receiver_state,
        dependency.semantics.parameters,
        dependency.semantics.internal_state,
    )
