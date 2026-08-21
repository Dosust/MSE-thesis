from dataclasses import dataclass
from typing import Literal

Tier = Literal['A', 'B1', 'B2', 'B3', 'EXCLUDE']

@dataclass(frozen=True)
class Scores:
    r1: int
    r2: int
    r3: int
    r4: int
    linkage: int

    def validate(self) -> None:
        for name, value in self.__dict__.items():
            if value not in (0, 1, 2, 3):
                raise ValueError(f'{name} must be in {{0,1,2,3}}, got {value}')

    @property
    def total(self) -> int:
        return self.r1 + self.r2 + self.r3 + self.r4 + self.linkage


def assign_tier(s: Scores) -> Tier:
    """Apply the frozen non-compensatory route logic."""
    s.validate()

    if s.r1 == 3 and s.r2 >= 2 and s.r3 == 3 and s.r4 == 3 and s.linkage >= 2:
        return 'A'
    if s.r1 == 3 and s.r2 >= 2 and s.r3 == 3 and s.r4 == 3 and s.linkage == 1:
        return 'B1'
    if s.r1 == 3 and s.r2 >= 2 and s.r3 == 2 and s.r4 == 3 and s.linkage >= 2:
        return 'B2'
    if s.r1 == 3 and s.r2 >= 2 and s.r3 == 3 and s.r4 == 2 and s.linkage >= 2:
        return 'B3'
    return 'EXCLUDE'


def perfect_methodological_score(s: Scores) -> bool:
    return (s.r1, s.r2, s.r3, s.r4, s.linkage) == (3, 3, 3, 3, 3)


def reproducibility_score(adequate: int, applicable: int) -> float:
    if applicable <= 0:
        raise ValueError('applicable must be > 0')
    if not 0 <= adequate <= applicable:
        raise ValueError('adequate must be between 0 and applicable')
    return adequate / applicable


def base_r2_from_coverage(coverage: float) -> int:
    if not 0 <= coverage <= 1:
        raise ValueError('coverage must be between 0 and 1')
    if coverage < 0.25:
        return 0
    if coverage < 0.50:
        return 1
    if coverage < 0.75:
        return 2
    return 3


def apply_lca_r2_caps(r2: int, functional_unit_reported: bool, system_boundary_reported: bool) -> int:
    """Apply only the frozen LCA-specific caps."""
    if not functional_unit_reported and not system_boundary_reported:
        return min(r2, 1)
    if not functional_unit_reported or not system_boundary_reported:
        return min(r2, 2)
    return r2


def weighted_relevance(z1: int, z2: int, z3: int, z4: int, z5: int) -> float:
    """Frozen Z1-Z5 relevance weights. Each z must be 0..3."""
    values = (z1, z2, z3, z4, z5)
    if any(v not in (0, 1, 2, 3) for v in values):
        raise ValueError('all relevance scores must be in {0,1,2,3}')
    return 0.15*z1 + 0.20*z2 + 0.20*z3 + 0.25*z4 + 0.20*z5


def final_analytical_use(s: Scores, wrs: float, r_min: float = 2.00) -> bool:
    """Eligibility first, then independent relevance threshold."""
    return assign_tier(s) != 'EXCLUDE' and wrs >= r_min


if __name__ == '__main__':
    # Logic checks only; these are not observed paper scores.
    assert assign_tier(Scores(3, 2, 3, 3, 2)) == 'A'
    assert assign_tier(Scores(3, 2, 3, 3, 1)) == 'B1'
    assert assign_tier(Scores(3, 2, 2, 3, 2)) == 'B2'
    assert assign_tier(Scores(3, 2, 3, 2, 2)) == 'B3'
    assert assign_tier(Scores(3, 2, 2, 2, 2)) == 'EXCLUDE'
    assert perfect_methodological_score(Scores(3, 3, 3, 3, 3))
