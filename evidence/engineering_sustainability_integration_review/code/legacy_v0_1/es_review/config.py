from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, Tuple

@dataclass(frozen=True)
class FrameworkConfig:
    """Frozen framework configuration."""

    expected_papers: int = 10

    # Perfect score and Tier-A thresholds
    perfect_vector: Tuple[int, int, int, int, int] = (3, 3, 3, 3, 3)
    tier_a_threshold: Tuple[int, int, int, int, int] = (3, 2, 3, 3, 2)

    # Direct-evidence matrix weights
    direct_weight: float = 1.0
    secondary_weight: float = 0.5
    absent_weight: float = 0.0

    # Workbook defaults
    max_evidence_rows: int = 2000

    # Controlled sheet names
    sheet_screening: str = "K_T_Screening_Extraction"
    sheet_pfsd: str = "PFSD_Detailed_Extraction"
    sheet_synthesis: str = "Table_1_Comparative_Synthesis"
    sheet_coverage: str = "Table_1_Visual_Evidence"
    sheet_mapping: str = "Table_2_Visual_Mapping"
    sheet_lists: str = "Controlled_Lists"

    # No-guessing controls
    fail_closed: bool = True
    allow_reviewer_formula_for_lambda3: bool = False
    require_evidence_for_max_score: bool = True
