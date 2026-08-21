from __future__ import annotations
from typing import Dict, Iterable, Set

from .enums import MethodFamily, IntegrationClass, FormulaType
from .models import PaperRecord

METHOD_ESSENTIALS: Dict[MethodFamily, Set[str]] = {
    MethodFamily.LCA: {
        "functional_unit", "system_boundary", "inventory",
        "data_source", "impact_method", "procedure"
    },
    MethodFamily.LCC: {
        "cost_basis", "time_horizon", "discounting",
        "cost_categories", "procedure"
    },
    MethodFamily.LCSA: {
        "functional_basis", "system_boundary", "dimensions",
        "indicators", "aggregation", "procedure"
    },
    MethodFamily.SLCA: {
        "functional_basis", "stakeholders", "indicators",
        "data_source", "aggregation", "procedure"
    },
    MethodFamily.MCDA: {
        "alternatives", "criteria", "weights",
        "normalization", "aggregation", "decision_rule"
    },
    MethodFamily.MIVES: {
        "alternatives", "criteria", "indicators",
        "value_functions", "weights", "aggregation"
    },
    MethodFamily.OPTIMIZATION: {
        "decision_variables", "objectives", "constraints",
        "model", "solver_or_search", "decision_rule"
    },
    MethodFamily.MACHINE_LEARNING: {
        "dataset", "predictors", "target",
        "model", "training", "validation"
    },
    MethodFamily.EMERGY: {
        "functional_basis", "inventory", "transformities",
        "emergy_calculation", "indicators", "procedure"
    },
    MethodFamily.INDEX: {
        "indicators", "normalization", "weights",
        "aggregation", "decision_rule"
    },
    MethodFamily.OTHER: set(),
}

F1 = {IntegrationClass.F1}
F2 = {IntegrationClass.F2A, IntegrationClass.F2B, IntegrationClass.F2C, IntegrationClass.F2D}
F3 = {
    IntegrationClass.F3A, IntegrationClass.F3B, IntegrationClass.F3C,
    IntegrationClass.F3D, IntegrationClass.F3E, IntegrationClass.F3F,
    IntegrationClass.F3G
}

def linkage_from_integration(record: PaperRecord) -> int:
    """Fail-closed linkage score from verified integration records."""
    valid = [x for x in record.pfsd.integration if x.traceable_alternatives]

    if not valid:
        return 0

    # Highest valid author-implemented architecture wins.
    for x in valid:
        if x.integration_class in F3:
            if not x.author_integrated_architecture:
                continue
            if x.formula_type == FormulaType.REVIEWER_RECONSTRUCTION:
                continue
            return 3

    if any(x.integration_class in F2 for x in valid):
        return 2

    if any(x.integration_class in F1 for x in valid):
        return 1

    return 0

def method_essential_status(record: PaperRecord) -> Dict[str, str]:
    essentials = METHOD_ESSENTIALS.get(record.method_family, set())
    return {k: record.method_components.get(k, "NR") for k in essentials}
