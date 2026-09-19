# Data-Use and Claim Firewall V1

## Permanent scientific rules

```math
\boxed{\text{No parameter is empirical because it is plausible.}}
```

```math
\boxed{\text{No model input is real because its units look realistic.}}
```

```math
\boxed{\text{No official source supports a claim outside its spatial, temporal, semantic, and measurement domain.}}
```

```math
\boxed{\text{No synthetic quantity is relabeled as observed reality.}}
```

```math
\boxed{\text{No missing operational datum is silently imputed into a confirmatory experiment.}}
```

## Mandatory source record

Every admitted datum must identify:
- Claim_supported;
- Claim_not_supported;
- Reality_level;
- Authority_class;
- Scientific_role;
- Case_match;
- Calibration_use;
- Validation_use;
- Known_uncertainty;
- Processing/transformation provenance.

## Examples

### EIA/ERCOT
May support regional power boundary conditions and plausibility envelopes.  
Does not by itself support feeder voltage, charger power, or Greensboro operation.

### EIA-861 / utility reliability
May support annual/system reliability envelopes.  
Does not by itself provide event-level dynamic restoration trajectories.

### NREL workplace charging data
May support external empirical charging distributions/calibration.  
Does not constitute Greensboro/Austin case validation.

### GreenEVT/SMART-DS
May support source-backed realistic-synthetic coupled development/benchmarking.  
Does not constitute observed utility feeder topology.

### NIST resilience guidance
May support requirement/performance-goal methodology.  
Does not supply arbitrary numerical service thresholds for this case.

## Claim ceiling

```math
\Lambda(d)
=
\text{maximum claim justified by }d.
```

Every downstream claim must satisfy:

```math
Claim\subseteq\Lambda(d_1)\cap\cdots\cap\Lambda(d_n).
```
