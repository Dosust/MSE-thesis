"""Case-independent Stage-1 source-adapter contract.

This module defines interfaces only. It does not encode Austin-specific rules,
causal interdependencies, or scientific conclusions.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, Iterable, List, Mapping, Optional


@dataclass(frozen=True)
class SourceManifest:
    source_id: str
    source_type: str
    provider: str
    native_format: str
    temporal_semantics: str
    source_vintage: str
    sha256: str
    adapter_id: str
    adapter_version: str
    native_crs: Optional[str] = None
    retrieval_reference: Optional[str] = None
    license_or_access: Optional[str] = None
    authority_metadata: Optional[Mapping[str, Any]] = None
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class QARecord:
    object_id: str
    test_name: str
    result: str
    severity: str
    message: str = ""
    measured_value: Optional[Any] = None
    threshold: Optional[Any] = None


@dataclass
class CanonicalBundle:
    """Canonical Stage-1 payload emitted by an adapter.

    The container is intentionally generic. Domain-specific adapters map source
    semantics into these typed records; downstream Stage-1 logic should not
    depend on the original file format.
    """

    entities: List[Dict[str, Any]] = field(default_factory=list)
    intralayer_edges: List[Dict[str, Any]] = field(default_factory=list)
    geometries: List[Dict[str, Any]] = field(default_factory=list)
    attributes: List[Dict[str, Any]] = field(default_factory=list)
    service_traceability: List[Dict[str, Any]] = field(default_factory=list)
    candidate_relations: List[Dict[str, Any]] = field(default_factory=list)
    assumptions: List[Dict[str, Any]] = field(default_factory=list)
    normative_authorities: List[Dict[str, Any]] = field(default_factory=list)
    qa: List[QARecord] = field(default_factory=list)


class Stage1SourceAdapter(ABC):
    """Required interface for every Stage-1 source-specific adapter."""

    manifest: SourceManifest

    @abstractmethod
    def inspect(self) -> Mapping[str, Any]:
        """Return non-destructive source diagnostics before parsing."""

    @abstractmethod
    def validate_source(self) -> Iterable[QARecord]:
        """Validate source integrity and minimum metadata requirements."""

    @abstractmethod
    def parse(self) -> Any:
        """Parse source-native bytes without semantic harmonization."""

    @abstractmethod
    def map_schema(self, parsed: Any) -> Any:
        """Map source-native fields/types into Stage-1 semantic fields."""

    @abstractmethod
    def normalize(self, mapped: Any) -> Any:
        """Normalize identifiers, units, CRS, temporal fields, and nulls."""

    @abstractmethod
    def emit_canonical(self, normalized: Any) -> CanonicalBundle:
        """Emit the case-independent canonical Stage-1 representation."""

    @abstractmethod
    def report_provenance(self) -> Mapping[str, Any]:
        """Return the complete provenance chain for this adapter run."""

    @abstractmethod
    def report_quality(self) -> Iterable[QARecord]:
        """Return all source, mapping, normalization, and structural QA results."""


def assert_stage1_noncausal(bundle: CanonicalBundle) -> None:
    """Enforce the Stage-1/Stage-2 boundary.

    Stage 1 may emit prior-documented or structural-candidate relations only.
    It may never declare a causal dependency accepted.
    """
    for rel in bundle.candidate_relations:
        if rel.get("causal_dependency_accepted") is True:
            raise ValueError(
                "Stage 1 cannot promote a structural relation to an accepted causal dependency."
            )


def assert_normative_noncausal(bundle: CanonicalBundle) -> None:
    """Ensure normative conformity is never promoted to scientific causality."""
    for rel in bundle.candidate_relations:
        if rel.get("normative_admissibility") in {"PASS", "CONDITIONAL"} and rel.get(
            "causal_dependency_accepted"
        ) is True:
            raise ValueError(
                "Normative admissibility cannot establish an accepted causal dependency."
            )


def assert_authority_scope(authority: Mapping[str, Any]) -> None:
    """Validate minimum authority metadata required by Stage 1."""
    required = {
        "authority_id",
        "authority_type",
        "authority_name",
        "jurisdiction",
        "document_id",
        "edition_or_version",
        "status",
        "applicability",
        "verification_status",
    }
    missing = sorted(required.difference(authority))
    if missing:
        raise ValueError(f"Authority record missing required fields: {missing}")
