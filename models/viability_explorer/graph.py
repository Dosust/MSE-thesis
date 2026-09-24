"""Explicit synthetic multilayer graph and spatial visualization projection.

The graph is structural scaffolding for the demonstrator. It does not solve
AC/DC power flow or dynamic traffic assignment. Node and edge states are
derived projections of the reduced sector state plus local hazard exposure.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import exp

from .core import State, gaussian_flood


@dataclass(frozen=True)
class Node:
    id: str
    layer: str
    x: float
    y: float
    role: str
    vulnerability: float = 0.6

    def validate(self) -> None:
        if self.layer not in {"power", "transport"}:
            raise ValueError(f"unsupported layer: {self.layer}")
        if not (0.0 <= self.x <= 1.0 and 0.0 <= self.y <= 1.0):
            raise ValueError(f"node {self.id} coordinates must lie in [0,1]^2")
        if self.vulnerability < 0.0:
            raise ValueError("vulnerability must be non-negative")


@dataclass(frozen=True)
class Edge:
    id: str
    source: str
    target: str
    layer: str
    capacity: float = 1.0

    def validate(self) -> None:
        if self.layer not in {"power", "transport", "interface"}:
            raise ValueError(f"unsupported edge layer: {self.layer}")
        if self.capacity <= 0.0:
            raise ValueError("capacity must be positive")


@dataclass(frozen=True)
class MultilayerGraph:
    nodes: tuple[Node, ...]
    edges: tuple[Edge, ...]

    def validate(self) -> None:
        node_ids = [n.id for n in self.nodes]
        edge_ids = [e.id for e in self.edges]
        if len(node_ids) != len(set(node_ids)):
            raise ValueError("node IDs must be unique")
        if len(edge_ids) != len(set(edge_ids)):
            raise ValueError("edge IDs must be unique")
        for node in self.nodes:
            node.validate()
        known = set(node_ids)
        lookup = {n.id: n for n in self.nodes}
        for edge in self.edges:
            edge.validate()
            if edge.source not in known or edge.target not in known:
                raise ValueError(f"edge {edge.id} references an unknown node")
            a, b = lookup[edge.source], lookup[edge.target]
            if edge.layer == "interface" and a.layer == b.layer:
                raise ValueError("interface edges must connect different layers")
            if edge.layer in {"power", "transport"} and (a.layer != edge.layer or b.layer != edge.layer):
                raise ValueError(f"{edge.layer} edge must remain within its declared layer")


def default_multilayer_graph() -> MultilayerGraph:
    """Return the deterministic synthetic P–T graph used by v0.2."""

    graph = MultilayerGraph(
        nodes=(
            Node("P0", "power", 0.12, 0.28, "source", 0.45),
            Node("P1", "power", 0.28, 0.18, "substation", 0.55),
            Node("P2", "power", 0.30, 0.52, "substation", 0.70),
            Node("P3", "power", 0.18, 0.76, "load", 0.65),
            Node("T0", "transport", 0.68, 0.18, "junction", 0.45),
            Node("T1", "transport", 0.84, 0.28, "junction", 0.55),
            Node("T2", "transport", 0.70, 0.52, "junction", 0.75),
            Node("T3", "transport", 0.86, 0.72, "junction", 0.70),
            Node("T4", "transport", 0.66, 0.82, "depot", 0.60),
        ),
        edges=(
            Edge("EP0", "P0", "P1", "power"),
            Edge("EP1", "P1", "P2", "power"),
            Edge("EP2", "P2", "P3", "power"),
            Edge("EP3", "P0", "P3", "power"),
            Edge("ET0", "T0", "T1", "transport"),
            Edge("ET1", "T0", "T2", "transport"),
            Edge("ET2", "T1", "T3", "transport"),
            Edge("ET3", "T2", "T3", "transport"),
            Edge("ET4", "T2", "T4", "transport"),
            Edge("ET5", "T3", "T4", "transport"),
            Edge("EI0", "P2", "T2", "interface", 0.9),
            Edge("EI1", "P3", "T4", "interface", 0.8),
        ),
    )
    graph.validate()
    return graph


def spatial_hazard(time: float, x: float, y: float, *, sigma: float = 0.34) -> float:
    """Project the temporal flood pulse into a smooth normalized spatial field."""

    if sigma <= 0.0:
        raise ValueError("sigma must be positive")
    if not (0.0 <= x <= 1.0 and 0.0 <= y <= 1.0):
        raise ValueError("coordinates must lie in [0,1]^2")
    temporal = gaussian_flood(time)
    center_x, center_y = 0.56, 0.58
    r2 = (x - center_x) ** 2 + (y - center_y) ** 2
    value = temporal * exp(-r2 / (2.0 * sigma * sigma))
    return min(1.0, max(0.0, value))


def graph_snapshot(graph: MultilayerGraph, state: State, time: float) -> dict:
    """Create data-only graph states for synchronized visualization.

    Availability is a declared projection:
        sector_service * exp(-vulnerability * local_hazard)

    Edge activity is the minimum endpoint availability, additionally multiplied
    by the reduced interface-health state for interface edges. These quantities
    are visualization/diagnostic proxies, not physical network-flow solutions.
    """

    graph.validate()
    state.validate()
    node_states: dict[str, dict[str, float]] = {}
    for node in graph.nodes:
        hazard = spatial_hazard(time, node.x, node.y)
        sector_service = state.power if node.layer == "power" else state.transport
        availability = sector_service * exp(-node.vulnerability * hazard)
        node_states[node.id] = {
            "hazard": hazard,
            "availability": min(1.0, max(0.0, availability)),
        }

    edge_states: dict[str, dict[str, float]] = {}
    for edge in graph.edges:
        base = min(
            node_states[edge.source]["availability"],
            node_states[edge.target]["availability"],
        )
        if edge.layer == "interface":
            base *= state.interface
        edge_states[edge.id] = {
            "activity": min(1.0, max(0.0, base)),
        }

    return {"nodes": node_states, "edges": edge_states}


def graph_payload(graph: MultilayerGraph) -> dict:
    graph.validate()
    return {
        "nodes": [
            {
                "id": n.id,
                "layer": n.layer,
                "x": n.x,
                "y": n.y,
                "role": n.role,
                "vulnerability": n.vulnerability,
            }
            for n in graph.nodes
        ],
        "edges": [
            {
                "id": e.id,
                "source": e.source,
                "target": e.target,
                "layer": e.layer,
                "capacity": e.capacity,
            }
            for e in graph.edges
        ],
    }
