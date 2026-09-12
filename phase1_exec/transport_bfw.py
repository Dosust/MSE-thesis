"""Biconjugate Frank-Wolfe verification solver for the frozen Sioux Falls UE.

This module is intentionally separate from the original Phase-1 CFW solver so
that the numerical amendment is auditable.  The recurrence is a deterministic
Python translation of the CFW/BFW equations in Mitradjieva & Lindberg and the
independent TrafficAssign.jl implementation.  It changes only the search
direction; the frozen Beckmann objective, BPR costs, all-or-nothing oracle,
relative-gap definition, tolerance, and iteration cap remain unchanged.
"""
from math import isfinite
from typing import Dict, Mapping, Sequence, Tuple

from .transport import (
    Edge,
    RoadLink,
    _line_search_to_target,
    all_or_nothing,
    bpr_derivative,
    bpr_time,
    relative_gap,
)


def _dir_cfw(
    links: Sequence[RoadLink],
    flow: Mapping[Edge, float],
    flow_fw: Mapping[Edge, float],
    flow_cfw: Mapping[Edge, float],
    d_fw: Mapping[Edge, float],
    d_cfw: Mapping[Edge, float],
    tau: float,
    delta: float,
) -> Tuple[Dict[Edge, float], Dict[Edge, float]]:
    d_bar = {edge: (1.0 - tau) * d_cfw[edge] for edge in flow}
    h = {
        (link.u, link.v): bpr_derivative(link, flow[(link.u, link.v)])
        for link in links
    }
    numerator = sum(d_bar[e] * h[e] * d_fw[e] for e in flow)
    denominator = sum(
        d_bar[e] * h[e] * (d_fw[e] - d_bar[e]) for e in flow
    )

    if abs(denominator) <= 1e-30:
        alpha = 0.0
    else:
        ratio = numerator / denominator
        if not isfinite(ratio) or ratio < 0.0:
            alpha = 0.0
        elif ratio <= 1.0 - delta:
            alpha = ratio
        else:
            alpha = 1.0 - delta

    new_target = {
        e: alpha * flow_cfw[e] + (1.0 - alpha) * flow_fw[e]
        for e in flow
    }
    new_direction = {e: new_target[e] - flow[e] for e in flow}
    return new_target, new_direction


def _dir_bfw(
    links: Sequence[RoadLink],
    flow: Mapping[Edge, float],
    flow_fw: Mapping[Edge, float],
    flow_bfw: Mapping[Edge, float],
    flow_bfw_pred: Mapping[Edge, float],
    d_fw: Mapping[Edge, float],
    d_bfw: Mapping[Edge, float],
    d_bfw_pred: Mapping[Edge, float],
    tau: float,
    tau_pred: float,
) -> Tuple[Dict[Edge, float], Dict[Edge, float]]:
    d_bar = {e: (1.0 - tau) * d_bfw[e] for e in flow}
    d_bar_bar = {
        e: (1.0 - tau) * (1.0 - tau_pred) * d_bfw_pred[e]
        for e in flow
    }
    h = {
        (link.u, link.v): bpr_derivative(link, flow[(link.u, link.v)])
        for link in links
    }

    mu_num = -sum(d_bar_bar[e] * h[e] * d_fw[e] for e in flow)
    mu_den = sum(
        d_bar_bar[e] * h[e] * (flow_bfw_pred[e] - flow_bfw[e])
        for e in flow
    )
    if abs(mu_den) <= 1e-30:
        mu = 0.0
    else:
        mu = mu_num / mu_den
        if not isfinite(mu):
            mu = 0.0
    mu = max(0.0, mu)

    nu_den = sum(d_bar[e] * h[e] * d_bar[e] for e in flow)
    if abs(nu_den) <= 1e-30 or abs(1.0 - tau) <= 1e-30:
        nu = 0.0
    else:
        nu = -sum(d_bar[e] * h[e] * d_fw[e] for e in flow) / nu_den
        nu += mu * tau / (1.0 - tau)
        if not isfinite(nu):
            nu = 0.0
    nu = max(0.0, nu)

    beta_fw = 1.0 / (1.0 + mu + nu)
    beta_bfw = nu * beta_fw
    beta_pred = mu * beta_fw

    new_target = {
        e: beta_fw * flow_fw[e]
        + beta_bfw * flow_bfw[e]
        + beta_pred * flow_bfw_pred[e]
        for e in flow
    }
    new_direction = {e: new_target[e] - flow[e] for e in flow}
    return new_target, new_direction


def biconjugate_frank_wolfe_user_equilibrium(
    links: Sequence[RoadLink],
    od: Mapping[Tuple[int, int], float],
    gap_tol: float = 1e-8,
    max_iter: int = 5000,
    delta: float = 1e-6,
) -> Tuple[Dict[Edge, float], int, float]:
    """Solve separable static UE using the frozen BFW recurrence.

    Returns ``(link_flows, iterations, relative_gap)``.  A return at
    ``max_iter`` with gap above ``gap_tol`` is a verification failure; the
    solver never silently relaxes the acceptance criterion.
    """
    if not (0.0 < delta < 1.0):
        raise ValueError("delta must lie strictly between 0 and 1")

    free_costs = {(link.u, link.v): link.free_time for link in links}
    flow = all_or_nothing(links, free_costs, od)

    flow_bfw: Dict[Edge, float] = dict(flow)
    flow_bfw_pred: Dict[Edge, float] = dict(flow)
    d_bfw: Dict[Edge, float] = {e: 0.0 for e in flow}
    d_bfw_pred: Dict[Edge, float] = {e: 0.0 for e in flow}

    tau = 1.0
    tau_pred = 1.0
    stage = "FW"

    for iteration in range(1, max_iter + 1):
        gap = relative_gap(links, flow, od)
        if gap <= gap_tol:
            return flow, iteration, gap

        costs = {
            (link.u, link.v): bpr_time(link, flow[(link.u, link.v)])
            for link in links
        }
        flow_fw = all_or_nothing(links, costs, od)
        d_fw = {e: flow_fw[e] - flow[e] for e in flow}

        if stage == "FW":
            flow_bfw = dict(flow_fw)
            d_bfw = dict(d_fw)
            stage = "CFW"
        elif stage == "CFW":
            flow_bfw_pred = dict(flow_bfw)
            d_bfw_pred = dict(d_bfw)
            flow_bfw, d_bfw = _dir_cfw(
                links,
                flow,
                flow_fw,
                flow_bfw,
                d_fw,
                d_bfw,
                tau,
                delta,
            )
            stage = "BFW"
        else:
            new_target, new_direction = _dir_bfw(
                links,
                flow,
                flow_fw,
                flow_bfw,
                flow_bfw_pred,
                d_fw,
                d_bfw,
                d_bfw_pred,
                tau,
                tau_pred,
            )
            flow_bfw_pred = dict(flow_bfw)
            d_bfw_pred = dict(d_bfw)
            flow_bfw = new_target
            d_bfw = new_direction

        tau_pred = tau
        tau = _line_search_to_target(links, flow, flow_bfw)
        if tau > 1.0 - gap_tol:
            stage = "FW"

        flow = {e: flow[e] + tau * d_bfw[e] for e in flow}

    return flow, max_iter, relative_gap(links, flow, od)
