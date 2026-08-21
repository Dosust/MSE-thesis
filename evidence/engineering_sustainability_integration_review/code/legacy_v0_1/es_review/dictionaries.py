"""Frozen search dictionaries.

IMPORTANT: terms are retrieval cues only. A hit NEVER directly sets a score.
"""

P_KEYWORDS = {
    "Mechanical": [
        "compressive strength", "tensile strength", "flexural strength",
        "modulus", "stiffness", "ductility", "toughness",
        "bond strength", "load capacity"
    ],
    "Structural": [
        "displacement", "drift", "deformation", "structural response",
        "seismic response", "fragility", "damage state", "reliability"
    ],
    "Durability": [
        "service life", "carbonation", "chloride penetration", "freeze-thaw",
        "permeability", "water absorption", "deterioration"
    ],
    "Geotechnical": [
        "settlement", "subgrade modulus", "bearing capacity",
        "soil stiffness", "load-settlement"
    ],
    "Thermal": [
        "thermal conductivity", "thermal resistance", "u-value",
        "heat transfer", "indoor temperature"
    ],
    "Energy": [
        "energy demand", "operational energy", "energy consumption",
        "energy performance"
    ],
    "Acoustic": [
        "sound absorption", "acoustic insulation", "sound transmission"
    ],
    "Fire": [
        "fire resistance", "residual strength", "elevated temperature"
    ],
    "Pavement": [
        "resilient modulus", "rutting", "fatigue", "cracking", "pavement life"
    ],
    "Functional": [
        "serviceability", "comfort", "functionality",
        "performance requirement", "performance threshold"
    ],
}

F_KEYWORDS = {
    "F1_parallel": [
        "compared with", "simultaneously evaluated", "technical and environmental",
        "mechanical and sustainability", "performance and environmental impact",
        "alongside", "separately assessed", "comparative assessment"
    ],
    "F2_directional": [
        "service life", "functional equivalence", "equivalent performance",
        "performance threshold", "minimum strength", "admissible", "admissibility",
        "design thickness", "replacement interval", "maintenance interval",
        "durability-based", "normalized per service life", "adjusted by",
        "dependent on", "influences", "determines", "modifies", "affects",
        "input to lca", "inventory adjustment", "design requirement",
        "performance constraint"
    ],
    "F3_integrated": [
        "sustainability index", "composite index", "integrated index",
        "overall performance", "consolidated index", "eco-efficiency",
        "eco-strength", "carbon intensity", "strength-normalized carbon",
        "performance-normalized", "normalized score", "weighted score",
        "value function", "utility function", "objective function",
        "optimization function", "decision function", "multi-objective optimization",
        "mcdm", "mcda", "ahp", "topsis", "electre", "mives",
        "grey relational analysis", "pareto optimization", "weighted sum",
        "regression model", "surrogate model", "response-damage-loss",
        "causal chain", "decision rule", "ranking model",
        "integrated assessment", "multi-criteria evaluation"
    ],
}

S_KEYWORDS = {
    "Environmental": [
        "lca", "life cycle assessment", "environmental impact", "gwp",
        "global warming potential", "carbon footprint", "co2 emissions",
        "embodied carbon", "embodied energy", "energy consumption",
        "resource depletion", "eutrophication", "acidification",
        "ecotoxicity", "human toxicity", "water consumption",
        "waste generation", "land use"
    ],
    "Economic": [
        "lcc", "life cycle cost", "cost analysis", "initial cost",
        "maintenance cost", "operating cost", "replacement cost",
        "total life-cycle cost", "npv", "net present value",
        "economic performance", "cost-effectiveness"
    ],
    "Social": [
        "s-lca", "social lca", "social sustainability", "worker safety",
        "occupational health", "employment", "stakeholder", "community",
        "accessibility", "wellbeing", "user comfort", "downtime",
        "social cost", "social indicator"
    ],
    "Integrated": [
        "triple bottom line", "tbl", "lcsa",
        "life cycle sustainability assessment", "sustainability score",
        "sustainability index", "environmental-economic-social",
        "economic-social-environmental", "integrated sustainability assessment"
    ],
}

D_KEYWORDS = [
    "optimum", "optimal", "optimized", "preferred", "best alternative",
    "selected alternative", "recommended", "ranking", "rank", "priority",
    "decision", "decision-making", "selection", "choose", "trade-off",
    "compromise solution", "pareto", "feasible solution",
    "design recommendation", "preferred mix", "preferred material",
    "preferred technology", "scenario selection", "alternative selection",
    "design optimization", "sensitivity analysis", "robustness", "robust solution"
]

WEAK_DISCUSSION_VERBS = [
    "discuss", "review", "suggest", "could", "may", "potential",
    "previous studies", "reported by", "according to"
]

STRONG_IMPLEMENTATION_PATTERNS = [
    "we measured", "was tested", "was calculated", "we performed",
    "was assessed", "was evaluated", "was simulated", "was optimized",
    "was integrated", "was used as input", "was normalized", "was weighted"
]
