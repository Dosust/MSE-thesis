"""Case-independent Stage-1 source-adapter contract.

This module enforces the final v2 Stage-1 evidence/ontology boundary.
It does not encode case-specific causal acceptance or coupling strength.
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
    """Canonical Stage-1 payload emitted by an adapter."""

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
        """Return source, mapping, normalization, and structural QA results."""


def assert_stage1_noncausal(bundle: CanonicalBundle) -> None:
    """Stage 1 may never accept a causal dependency."""
    for rel in bundle.candidate_relations:
        if rel.get("causal_dependency_accepted") is not False:
            raise ValueError(
                "Stage 1 requires causal_dependency_accepted=false for every relation."
            )


def assert_normative_noncausal(bundle: CanonicalBundle) -> None:
    """Normative admissibility must remain separate from scientific causality."""
    for rel in bundle.candidate_relations:
        meta = rel.get("metadata", {})
        norm = meta.get("normative_admissibility")
        if norm in {"PASS", "CONDITIONAL"} and rel.get("causal_dependency_accepted") is True:
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


def assert_stage1_relation_semantics(bundle: CanonicalBundle) -> None:
    """Enforce the v2 core-relation + secondary-metadata contract."""
    structural_case_bases = {
        "ASSET_CROSSWALK",
        "SPATIAL_RELATION",
        "ACCESS_GEOMETRY",
        "GEOGRAPHIC_COEXPOSURE",
    }

    for rel in bundle.candidate_relations:
        record_level = rel.get("record_level")
        scope = rel.get("scope")
        participants = rel.get("participants", [])
        existence = rel.get("structural_existence")
        case_status = rel.get("case_connection_status")
        mechanism_status = rel.get("mechanism_status")
        meta = rel.get("metadata", {})

        if rel.get("strength_status") != "NOT_ESTIMATED_STAGE1":
            raise ValueError("Stage 1 cannot estimate functional coupling strength.")

        if rel.get("causal_dependency_accepted") is not False:
            raise ValueError("Stage 1 cannot accept a causal dependency.")

        if not rel.get("interface_semantics") or not rel.get("exchange_semantics"):
            raise ValueError("Every Stage-1 relation requires interface and exchange semantics.")

        if not rel.get("evidence_refs"):
            raise ValueError("Every Stage-1 relation requires evidence/provenance references.")

        if record_level == "MECHANISM_TEMPLATE":
            if existence != "TEMPLATE_ONLY" or case_status != "NOT_CASE_EVALUATED":
                raise ValueError("Mechanism templates must remain TEMPLATE_ONLY and not case-evaluated.")
            if rel.get("structural_admissibility", {}).get("predicate_pass") is not None:
                raise ValueError("Mechanism templates cannot fabricate a case structural predicate.")

        if record_level == "CASE_RELATION" and existence == "TEMPLATE_ONLY":
            raise ValueError("Case relations cannot use TEMPLATE_ONLY structural existence.")

        if existence == "VERIFIED_STRUCTURAL":
            if record_level != "CASE_RELATION" or case_status != "VERIFIED_STRUCTURAL":
                raise ValueError("VERIFIED_STRUCTURAL is valid only for verified case relations.")
            admission = set(meta.get("admission_basis", []))
            if not admission.intersection(structural_case_bases):
                raise ValueError(
                    "Verified structural case relations require case structural evidence."
                )

        confidence = meta.get("evidence_confidence", {})
        score = confidence.get("score")
        method = confidence.get("method")
        if score is not None and not method:
            raise ValueError(
                "Numeric evidence confidence requires an explicit scoring/calibration method."
            )

        path = meta.get("path")
        mediator_path = meta.get("mediator_path", [])
        if path == "MEDIATED" and not mediator_path:
            raise ValueError("MEDIATED relations require an explicit mediator path.")

        arity = meta.get("arity")
        if arity == "PAIRWISE" and len(participants) != 2:
            raise ValueError("PAIRWISE Stage-1 relations require exactly two participants.")
        if arity == "HIGHER_ORDER" and len(participants) < 3:
            raise ValueError("HIGHER_ORDER relations require at least three participants.")

        participant_layers = {p.get("layer") for p in participants}
        if scope == "INTRA" and len(participant_layers) != 1:
            raise ValueError("INTRA relations must remain within one layer.")
        if scope == "INTER" and len(participant_layers) < 2:
            raise ValueError("INTER relations must involve at least two layers.")
        if scope == "CONTEXT":
            if mechanism_status != "CONTEXT_ONLY":
                raise ValueError("CONTEXT relations require mechanism_status=CONTEXT_ONLY.")
            if rel.get("direction") not in {"UNDIRECTED_SCREENING", "CONTEXT_TO_SYSTEM"}:
                raise ValueError("CONTEXT relations cannot masquerade as P->T or T->P causality.")


def assert_stage1_entity_semantics(bundle: CanonicalBundle) -> None:
    """Require explicit function, resolution, and evidence traceability."""
    for entity in bundle.entities:
        if not entity.get("engineering_functions"):
            raise ValueError("Stage-1 entity requires engineering_functions.")
        if not entity.get("resolution_level"):
            raise ValueError("Stage-1 entity requires resolution_level.")
        if not entity.get("evidence_refs"):
            raise ValueError("Stage-1 entity requires evidence_refs.")