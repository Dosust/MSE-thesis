from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

from .enums import (
    YesNo, EvidenceStatus, Provenance, FormulaType, ValidationLevel,
    PerformanceFamily, SustainabilityDimension, DecisionType,
    IntegrationClass, MethodFamily
)

@dataclass(frozen=True)
class SourceLocation:
    page: Optional[int] = None
    section: str = ""
    table_or_figure: str = ""

@dataclass(frozen=True)
class EvidenceRecord:
    evidence_id: str
    paper_id: str
    domain: str
    claim: str
    verbatim_passage: str
    location: SourceLocation
    status: EvidenceStatus = EvidenceStatus.SUPPORTED
    provenance: Provenance = Provenance.NR
    formula_type: FormulaType = FormulaType.NO_FORMULA
    author_generated: Optional[bool] = None
    method_generated: Optional[bool] = None
    notes: str = ""

    def is_supported(self) -> bool:
        return self.status == EvidenceStatus.SUPPORTED and bool(self.verbatim_passage.strip())

@dataclass(frozen=True)
class PerformanceEvidence:
    family: PerformanceFamily
    metric: str
    method: str
    result: str
    unit: str
    alternative: str
    comparator: str = ""
    author_generated: bool = False
    evidence_ids: Tuple[str, ...] = ()

@dataclass(frozen=True)
class SustainabilityEvidence:
    method: str
    method_family: MethodFamily
    dimension: SustainabilityDimension
    indicator: str
    result: str
    unit: str
    functional_basis: str
    alternative: str
    method_generated: bool = False
    evidence_ids: Tuple[str, ...] = ()

@dataclass(frozen=True)
class IntegrationEvidence:
    integration_class: IntegrationClass
    source_variable: str
    transformation: str
    target_variable: str
    traceable_alternatives: bool
    author_formula_or_chain: str = ""
    formula_type: FormulaType = FormulaType.NO_FORMULA
    author_integrated_architecture: bool = False
    evidence_ids: Tuple[str, ...] = ()

@dataclass(frozen=True)
class DecisionEvidence:
    decision_type: DecisionType
    alternatives: str
    decision_rule: str
    outcome: str
    sensitivity_or_robustness: str = ""
    evidence_ids: Tuple[str, ...] = ()

@dataclass
class PFSDRecord:
    performance: List[PerformanceEvidence] = field(default_factory=list)
    integration: List[IntegrationEvidence] = field(default_factory=list)
    sustainability: List[SustainabilityEvidence] = field(default_factory=list)
    decisions: List[DecisionEvidence] = field(default_factory=list)

@dataclass(frozen=True)
class ScreeningKLM:
    K: YesNo
    SM: YesNo
    M: YesNo

    @property
    def gate(self) -> int:
        return int(self.K == YesNo.YES and self.SM == YesNo.YES and self.M == YesNo.YES)

@dataclass(frozen=True)
class Scores:
    R1: int
    R2: int
    R3: int
    R4: int
    linkage: int

    def vector(self) -> Tuple[int, int, int, int, int]:
        return (self.R1, self.R2, self.R3, self.R4, self.linkage)

@dataclass
class PaperRecord:
    paper_id: str
    rank: int
    csv_id: str
    authors: str
    title: str
    year: Optional[int]
    journal: str
    doi: str
    pdf_path: str

    # Supervisor columns
    screening: Optional[ScreeningKLM] = None
    N_performance_effects: str = ""
    O_core_elements: str = ""
    P_procedure: str = ""
    Q_construction_strategy: str = ""
    R_what_evaluated: str = ""
    S_validation: str = ""
    T_backward_snowballing: str = ""

    # Analytical layer
    pfsd: PFSDRecord = field(default_factory=PFSDRecord)
    method_family: MethodFamily = MethodFamily.OTHER
    method_components: Dict[str, str] = field(default_factory=dict)
    scores: Optional[Scores] = None

    # Display/synthesis
    framework_type: str = ""
    integration_mechanism_label: str = ""
    transferable_logic: str = ""
    validation_level: ValidationLevel = ValidationLevel.NO

    # Evidence index
    evidence: Dict[str, EvidenceRecord] = field(default_factory=dict)
