module CoupledInfrastructure

"""
Minimal Julia scaffold for the canonical P–T–I–O thesis architecture.

This module is a **software-QA toy model**, not a calibrated thesis model and not
empirical evidence. Its purpose is to keep the current system ontology explicit:
Power and Transportation are physical systems; Information and Organization are
interacting layers that can modify coupled trajectories and feasible response.
"""

export ModelParameters, LAYER_ORDER, ptio_rhs!, interdependency_signal,
       feasible_control_scale

const LAYER_ORDER = (:P, :T, :I, :O)

Base.@kwdef struct ModelParameters
    # Intrinsic relaxation/decay rates for normalized toy states [P,T,I,O].
    decay::NTuple{4,Float64} = (0.25, 0.20, 0.30, 0.15)

    # coupling[target, source]. Diagonal terms remain zero. These coefficients
    # are synthetic software-test values; they are not thesis estimates.
    coupling::Matrix{Float64} = [
        0.00  0.10  0.18  0.16;
        0.22  0.00  0.14  0.12;
        0.16  0.10  0.00  0.20;
        0.12  0.18  0.15  0.00
    ]

    # Synthetic hazard sensitivity of the four normalized states.
    hazard_gain::NTuple{4,Float64} = (0.35, 0.40, 0.25, 0.20)
end

"""
Return a simple Stage-2/3 transmission signal for a toy causal edge.

`strength` corresponds to an interdependency-strength parameter, `activation`
corresponds to the Stage-2 activation state, and `delay_attenuation` is only a
numerical placeholder for software tests. A real delayed model must implement
history explicitly rather than interpreting this helper as a physical delay law.
"""
function interdependency_signal(
    source_state::Real,
    strength::Real,
    activation::Real,
    delay_attenuation::Real = 1.0,
)
    0.0 <= activation <= 1.0 || throw(ArgumentError("activation must lie in [0,1]"))
    delay_attenuation >= 0.0 || throw(ArgumentError("delay_attenuation must be non-negative"))
    return activation * strength * delay_attenuation * source_state
end

"""
Map normalized information/organization capability to a conservative control
availability scale in [0,1].

This helper encodes only the qualitative Stage-4 statement that information and
organization constrain feasible action. It is not the canonical control policy.
"""
function feasible_control_scale(zI::Real, zO::Real)
    return clamp(min(zI, zO), 0.0, 1.0)
end

"""
Toy coupled P–T–I–O dynamics.

State order:   x = [P, T, I, O]
Control order: u = [uP, uT, uI, uO]
Hazard input:  h >= 0

The off-diagonal coupling matrix is interpreted as source-to-target influence:
`coupling[i,j]` maps state j into the derivative of state i. The function is
intentionally transparent so CI can detect ontology drift and basic numerical
failures. It does not replace the Stage-3 hybrid/delayed/multirate equations.
"""
function ptio_rhs!(dx, x, u, h::Real, p::ModelParameters)
    length(x) == 4 || throw(DimensionMismatch("x must follow [P,T,I,O]"))
    length(u) == 4 || throw(DimensionMismatch("u must follow [uP,uT,uI,uO]"))
    length(dx) == 4 || throw(DimensionMismatch("dx must have length 4"))
    size(p.coupling) == (4, 4) || throw(DimensionMismatch("coupling must be 4x4"))
    h >= 0.0 || throw(ArgumentError("hazard intensity must be non-negative"))

    for i in 1:4
        coupling_term = 0.0
        for j in 1:4
            i == j && continue
            coupling_term += p.coupling[i, j] * x[j]
        end
        dx[i] = -p.decay[i] * x[i] + coupling_term + u[i] - p.hazard_gain[i] * h
    end
    return nothing
end

end # module
