from pathlib import Path
import json
import numpy as np
from egmiv_h1 import Line, RadialNetwork, Cell, Turn, CTMNetwork, M0Runner


def main():
    # Numerical values are benchmark/test-harness values only, not thesis calibration.
    power = RadialNetwork(
        3, 0,
        [Line(0,1,0.005,0.002,2.0), Line(1,2,0.005,0.002,1.0)],
        v_min_pu=0.95, v_max_pu=1.05,
    )
    traffic = CTMNetwork(
        [Cell(1,60,20,150,1800,0), Cell(1,60,20,150,1800,1800)],
        1, [Turn(0,1,0,1.0)], dt_h=0.01,
    )
    runner = M0Runner(power, traffic)

    K = 120
    p = np.tile([0.0,0.15,0.10], (K,1))
    q = np.tile([0.0,0.03,0.02], (K,1))
    line_available = np.ones((K,2), dtype=bool)
    source = np.zeros((K,2,1)); source[:,0,0]=600.0
    occ0 = np.zeros((2,1))
    cell_available = np.ones((K,2), dtype=bool)

    result = runner.run(p,q,line_available,source,occ0,cell_available)
    report = {
        "model": "M0_INDEPENDENT",
        "parameter_status": "BENCHMARK_TEST_HARNESS_ONLY",
        "power_service_min": float(result.power_service.min()),
        "transport_service_final": float(result.transport_service[-1]),
        "cumulative_power_service_loss_h": result.cumulative_power_service_loss_h,
        "cumulative_transport_service_loss_h": result.cumulative_transport_service_loss_h,
        "max_power_balance_residual_pu": max(x.max_power_balance_residual_pu for x in result.power_results),
        "max_traffic_conservation_residual_veh": max(x.max_conservation_residual_veh for x in result.traffic_results),
        "max_voltage_violation_pu": max(x.voltage_violation_pu for x in result.power_results),
        "max_thermal_violation_pu": max(x.thermal_violation_pu for x in result.power_results),
        "completed_trips_by_commodity": result.completed_by_commodity.tolist(),
        "requested_trips_by_commodity": result.requested_by_commodity.tolist(),
    }
    out = Path(__file__).resolve().parents[1] / "reports" / "m0_example_report.json"
    out.write_text(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()