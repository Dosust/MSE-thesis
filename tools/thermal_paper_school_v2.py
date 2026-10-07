"""
Thermal Paper School V2
Limitation-and-gap audit helper.

Primary method:
Claim -> Evidence -> Validity Domain -> Limitation
-> Remaining Unknown -> Gap-Closing Test -> Thesis Transfer Decision
"""

from dataclasses import dataclass
from enum import Enum

class Decision(str, Enum):
    CORE = "CORE"
    SUPPORTING = "SUPPORTING"
    CONDITIONAL = "CONDITIONAL"
    CORE_MECHANISM = "CORE MECHANISM EVIDENCE"

LIMITATIONS = {
    "L1": "Observability",
    "L2": "Model form",
    "L3": "Parameter identifiability",
    "L4": "Validation domain",
    "L5": "Generalizability",
    "L6": "Scale transfer",
    "L7": "Time-scale mismatch",
    "L8": "Coupling omission",
    "L9": "Uncertainty",
    "L10": "Service translation",
    "L11": "Intervention trade-off",
}

STATE_TIME_RULES = [
    "external forcing != system state",
    "physical quantity != state variable != active thesis state",
    "thermal state != operational/energy state",
    "state != capability != service",
    "transition time != propagation delay != service-consequence time != recovery time",
]

READING_PASSES = [
    "Scientific problem",
    "Physics",
    "Mathematics",
    "Method + evidence",
    "Engineering interpretation",
    "Limitation anatomy",
    "Remaining gap + gap-closing test",
]

@dataclass
class PaperAudit:
    lesson: str
    claim: str
    evidence: str
    validity_domain: str
    limitation_codes: list[str]
    remaining_unknown: str
    gap_closing_test: str
    thesis_transfer: str
    decision: Decision

    def validate(self):
        unknown = [x for x in self.limitation_codes if x not in LIMITATIONS]
        if unknown:
            raise ValueError(f"Unknown limitation codes: {unknown}")
        if not self.validity_domain.strip():
            raise ValueError("Validity domain must be explicit.")
        if not self.gap_closing_test.strip():
            raise ValueError("Every remaining unknown requires a gap-closing test.")
        return True

def admission_gate(
    physical_validity: bool,
    directionality: bool,
    parameter_validity: bool,
    scale_validity: bool,
    temporal_validity: bool,
    service_materiality: bool,
):
    gates = {
        "physical_validity": physical_validity,
        "directionality": directionality,
        "parameter_validity": parameter_validity,
        "scale_validity": scale_validity,
        "temporal_validity": temporal_validity,
        "service_materiality": service_materiality,
    }
    return {
        "gates": gates,
        "all_pass": all(gates.values()),
        "failed": [k for k, v in gates.items() if not v],
    }

def state_admission(dynamically_required=False,
                    materially_changes_capability=False,
                    materially_changes_transition_time=False,
                    materially_changes_propagation=False,
                    materially_changes_QP=False,
                    materially_changes_QT=False,
                    materially_changes_validation=False,
                    materially_changes_engineering_conclusion=False):
    """Canonical minimum-sufficient-physics admission rule for a candidate state.

    A physically meaningful quantity is not automatically an active thesis state.
    It must be dynamically required by the adopted model and materially affect at
    least one thesis-relevant mechanism, capability, timing, service, validation,
    or engineering conclusion.
    """
    material = any([
        materially_changes_capability,
        materially_changes_transition_time,
        materially_changes_propagation,
        materially_changes_QP,
        materially_changes_QT,
        materially_changes_validation,
        materially_changes_engineering_conclusion,
    ])
    return dynamically_required and material

if __name__ == "__main__":
    print("Thermal Paper School V2")
    print("Reading method:")
    for i, p in enumerate(READING_PASSES, 1):
        print(f"{i}. {p}")
    print("\nCanonical state-time rules:")
    for rule in STATE_TIME_RULES:
        print(f"- {rule}")
    print("\nLimitation taxonomy:")
    for code, name in LIMITATIONS.items():
        print(f"{code}: {name}")
