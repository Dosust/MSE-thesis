module CoupledInfrastructure

"""
Minimal Julia scaffold for the P–W–T–SW hybrid/multiscale model.

This module is a specification aid, not a calibrated thesis model. It makes the
state/interface separation explicit and provides a compact right-hand side for
synthetic tests.
"""

export ModelParameters, infrastructure_rhs!, interface_rhs!, realized_flood_hazard

Base.@kwdef struct ModelParameters
    decay_power::Float64 = 0.30
    decay_water::Float64 = 0.25
    decay_transport::Float64 = 0.20
    decay_waste::Float64 = 0.15
    pw::Float64 = 0.20
    wp::Float64 = 0.15
    pt::Float64 = 0.10
    tw::Float64 = 0.08
    waste_to_drainage::Float64 = 0.25
    flood_gain::Float64 = 0.50
    epsilon_interface::Float64 = 0.10
end

"""
Map exogenous rainfall forcing ξ and waste-related blockage to realized flood
hazard η. The clipping keeps this synthetic reference hazard non-negative.
"""
function realized_flood_hazard(ξ::Real, xsw::Real, p::ModelParameters)
    blockage = max(0.0, p.waste_to_drainage * xsw)
    return max(0.0, p.flood_gain * ξ + blockage)
end

"""
Reference four-sector state dynamics.

State order: x = [P, W, T, SW]
Interface order: z = [zPW, zWP, zPT, zTW]
Control order: u = [uP, uW, uT, uSW]
"""
function infrastructure_rhs!(dx, x, z, u, ξ, p::ModelParameters)
    P, W, T, SW = x
    zPW, zWP, zPT, zTW = z
    uP, uW, uT, uSW = u
    η = realized_flood_hazard(ξ, SW, p)

    dx[1] = -p.decay_power * P + zPW * W + zPT * T + uP - 0.25 * η
    dx[2] = -p.decay_water * W + zWP * P + uW - 0.30 * η
    dx[3] = -p.decay_transport * T + zTW * W + uT - 0.40 * η
    dx[4] = -p.decay_waste * SW + uSW + 0.20 * (1.0 - max(T, 0.0)) + 0.10 * η
    return nothing
end

"""
Reference dynamic-interface model ε ż = G(X,Z,η). The equilibrium coupling
strength changes with sector condition and realized hazard.
"""
function interface_rhs!(dz, x, z, ξ, p::ModelParameters)
    P, W, T, SW = x
    η = realized_flood_hazard(ξ, SW, p)
    target = [
        p.pw * max(P, 0.0),
        p.wp * max(W, 0.0),
        p.pt * exp(-η),
        p.tw * max(T, 0.0),
    ]
    for i in eachindex(z)
        dz[i] = (target[i] - z[i]) / p.epsilon_interface
    end
    return nothing
end

end # module
