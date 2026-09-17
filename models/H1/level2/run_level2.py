#!/usr/bin/env python3
from __future__ import annotations
import argparse
import json
from pathlib import Path


def clamp01(x: float) -> float:
    return max(0.0, min(1.0, x))


def road_freeflow_h(edge: dict) -> float:
    v = max(float(edge.get("free_speed_kph", 0.0)), 1e-9)
    return float(edge.get("length_km", 0.0)) / v


def run_preview(case: dict) -> dict:
    dt = float(case["dt_h"])
    K = int(case["horizon_steps"])
    d = case["disturbance"]
    start = int(d["start_step"])
    outage_end = start + int(d["charger_outage_steps"])
    charger = case["chargers"][0]
    lam = float(charger["arrival_vph"])
    mu_max = float(charger["capacity_vph"])
    road_by_id = {e["id"]: e for e in case["road_edges"]}
    job = case["repair_jobs"][0]
    ff_access = sum(road_freeflow_h(road_by_id[eid]) for eid in job["road_path"])
    dyn_access = ff_access * float(d["road_congestion_factor"])
    repair = float(job["repair_time_h"])
    restore_m1_h = start * dt + ff_access + repair
    restore_m2_h = start * dt + dyn_access + repair

    q = 0.0
    series = {m: {"power_service": [], "transport_service": [], "queue_veh": []} for m in ("M0", "M1", "M2")}
    for k in range(K):
        t = k * dt
        charger_power_on = not (start <= k < outage_end)
        failed = t >= start * dt
        p0 = 1.0 if not failed else 0.75
        p1 = 1.0 if t >= restore_m1_h or not failed else 0.75
        p2 = 1.0 if t >= restore_m2_h or not failed else 0.75

        # M0 ignores charging feedback; M1 same-step; M2 carries queue memory.
        phi1 = 1.0 if charger_power_on else 0.0
        mu2 = mu_max if charger_power_on else 0.0
        q = max(0.0, q + dt * (lam - mu2))
        demand2 = lam + q / dt if dt > 0 else lam
        phi2 = 1.0 if demand2 <= 1e-12 else min(1.0, mu2 / demand2)
        t0 = 1.0
        t1 = 0.9 + 0.1 * phi1
        t2 = 0.9 + 0.1 * phi2
        for m, ps, ts, qq in (
            ("M0", p0, t0, 0.0),
            ("M1", p1, t1, 0.0),
            ("M2", p2, t2, q),
        ):
            series[m]["power_service"].append(clamp01(ps))
            series[m]["transport_service"].append(clamp01(ts))
            series[m]["queue_veh"].append(max(0.0, qq))

    def loss(xs: list[float]) -> float:
        return sum(1.0 - x for x in xs) * dt

    summary = {}
    for m, s in series.items():
        summary[m] = {
            "power_service_loss_h": loss(s["power_service"]),
            "transport_service_loss_h": loss(s["transport_service"]),
            "max_queue_veh": max(s["queue_veh"]),
            "terminal_queue_veh": s["queue_veh"][-1],
        }
    return {
        "level": 2,
        "mode": "preview",
        "admissible_for_thesis_results": False,
        "model_definitions": {
            "M0": "independent",
            "M1": "static/algebraic coupling",
            "M2": "dynamic causal coupling with interface memory",
        },
        "matched_inputs": True,
        "derived": {
            "static_repair_access_h": ff_access,
            "dynamic_repair_access_h": dyn_access,
            "M1_restoration_h": restore_m1_h,
            "M2_restoration_h": restore_m2_h,
        },
        "summary": summary,
        "series": series,
        "claim_boundary": "software verification only; not empirical evidence and not a realistic-mode result",
    }


def validate_realistic(case: dict) -> dict:
    buses = case.get("power_buses", [])
    roads = case.get("road_edges", [])
    road_ids = {str(r["id"]) for r in roads}
    missing = [b["id"] for b in buses if str(b.get("sumo_edge_id")) not in road_ids]
    gates = {
        "R1_mode_realistic": case.get("mode") == "realistic",
        "R2_nonempty_power_subset": len(buses) > 0,
        "R3_nonempty_road_subset": len(roads) > 0,
        "R4_bus_edges_present_in_reduced_road_set": len(missing) == 0,
        "R5_missing_inputs_explicitly_declared": bool(case.get("synthetic_inputs_required_before_run")),
    }
    return {
        "level": 2,
        "mode": "realistic",
        "execution_status": "BLOCKED_PENDING_FROZEN_EXPERIMENT_INPUTS" if all(gates.values()) else "BLOCKED_GEOMETRY_OR_CROSSWALK",
        "gates": gates,
        "missing_bus_edge_crosswalks": missing,
        "next_required_inputs": case.get("synthetic_inputs_required_before_run", []),
        "claim_boundary": case.get("claim_boundary"),
        "note": "This runner intentionally refuses to invent disturbance/charger/repair parameters for the realistic case. Populate those from frozen evidence or declared sensitivity designs, then bind to OpenDSS/SUMO and the verified M0/M1/M2 engines.",
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", required=True)
    ap.add_argument("--out", default="results.json")
    args = ap.parse_args()
    case = json.loads(Path(args.case).read_text())
    result = run_preview(case) if case.get("mode") == "preview" else validate_realistic(case)
    Path(args.out).write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"written": args.out, "mode": result["mode"], "status": result.get("execution_status", "PREVIEW_COMPLETE")}, indent=2))


if __name__ == "__main__":
    main()
