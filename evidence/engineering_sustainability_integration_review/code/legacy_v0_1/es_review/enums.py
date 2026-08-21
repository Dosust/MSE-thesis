from __future__ import annotations
from enum import Enum

class YesNo(str, Enum):
    YES = "Yes"
    NO = "No"

class EvidenceStatus(str, Enum):
    SUPPORTED = "SUPPORTED"
    NR = "NR"   # investigated, not reported
    U = "U"     # genuinely unclear/ambiguous
    NA = "NA"   # not applicable

class Provenance(str, Enum):
    AUTHOR_GENERATED = "AUTHOR_GENERATED"
    AUTHOR_IMPLEMENTED = "AUTHOR_IMPLEMENTED"
    AUTHOR_VALIDATED = "AUTHOR_VALIDATED"
    ESTABLISHED_METHOD_APPLIED = "ESTABLISHED_METHOD_APPLIED"
    SECONDARY = "SECONDARY"
    DISCUSSED = "DISCUSSED"
    SUPPLIER = "SUPPLIER"
    ASSUMED = "ASSUMED"
    NR = "NR"
    U = "U"
    NA = "NA"

class FormulaType(str, Enum):
    AUTHOR_FORMULA = "AF"
    REVIEWER_RECONSTRUCTION = "RR"
    NO_FORMULA = "NF"

class ValidationLevel(str, Enum):
    NO = "No"
    APPLIED = "Applied"
    INTERNAL = "Internal"
    EXTERNAL = "External"

class PerformanceFamily(str, Enum):
    MECHANICAL = "Mechanical"
    STRUCTURAL = "Structural"
    DURABILITY = "Durability"
    SERVICE_LIFE = "Service life"
    THERMAL = "Thermal"
    ENERGY = "Energy"
    ACOUSTIC = "Acoustic"
    FIRE = "Fire"
    GEOTECHNICAL = "Geotechnical"
    PAVEMENT = "Pavement"
    FUNCTIONAL = "Functional/serviceability"
    RELIABILITY = "Reliability/resilience"
    OPTIMIZATION = "Optimization/surrogate"
    OTHER = "Other"

class SustainabilityDimension(str, Enum):
    ENVIRONMENTAL = "Environmental"
    ECONOMIC = "Economic"
    SOCIAL = "Social"
    INTEGRATED = "Integrated"

class DecisionType(str, Enum):
    RANKING = "Ranking"
    SELECTION = "Selection"
    OPTIMIZATION = "Optimization"
    SCREENING = "Screening"
    PRIORITIZATION = "Prioritization"
    TRADEOFF = "Trade-off"
    ROBUST = "Robust selection"
    SCENARIO = "Scenario selection"
    NONE = "None"

class IntegrationClass(str, Enum):
    F0 = "F0"
    F1 = "F1"
    F2A = "F2a"
    F2B = "F2b"
    F2C = "F2c"
    F2D = "F2d"
    F3A = "F3a"
    F3B = "F3b"
    F3C = "F3c"
    F3D = "F3d"
    F3E = "F3e"
    F3F = "F3f"
    F3G = "F3g"

class MethodFamily(str, Enum):
    LCA = "LCA"
    LCC = "LCC"
    LCSA = "LCSA"
    SLCA = "S-LCA"
    MCDA = "MCDA"
    MIVES = "MIVES"
    OPTIMIZATION = "Optimization"
    MACHINE_LEARNING = "Machine learning"
    EMERGY = "Emergy"
    INDEX = "Integrated index"
    OTHER = "Other"

class Tier(str, Enum):
    PERFECT = "PERFECT"
    TIER_A = "Tier A"
    NOT_TIER_A = "Not Tier A"
