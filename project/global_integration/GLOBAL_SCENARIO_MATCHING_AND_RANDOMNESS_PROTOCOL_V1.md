# Global Scenario Matching and Randomness Protocol v1

**Date:** 2026-09-19  
**Status:** NORMATIVE P1.6 MATCHING / RNG CONTROL

## 1. Matched-comparison principle

For two arms \(a,b\) in comparison group \(c\):

~~~math
\boxed{
\omega_{r,a}\sim_c\omega_{r,b}
}
~~~

iff every prespecified held-constant field is identical by reference/hash and every difference is contained in the prespecified changed-field set.

Define:

~~~math
H_c=\text{held fields},
\qquad
\Delta_c=\text{allowed changed fields}.
~~~

Then:

~~~math
\boxed{
f_a=f_b\ \forall f\in H_c,
\qquad
Differences(a,b)\subseteq\Delta_c.
}
~~~

A hidden difference is a match failure.

## 2. Comparison-group manifest

Every comparison group records:

~~~text
comparison_group_id
hypothesis
baseline_arm_id
treatment_arm_ids
held_constant_fields
allowed_changed_fields
scenario_root_ids
scenario_set_id
randomness_rule
probability_semantics
freeze_version
freeze_hash
status
~~~

## 3. Randomness architecture

Use named streams rather than one opaque global seed whenever multiple stochastic sources exist.

Seed record:

~~~text
seed_set_id
stream_name
semantic_quantity
generator
generator_version
seed_or_substream
draw_protocol
common_random_number_group
applicable_stages
freeze_hash
status
~~~

Examples of semantic streams:
- hazard_residual;
- demand_variation;
- component_failure;
- repair_duration;
- observation_noise;
- information_latency;
- organizational_delay;
- intervention_performance.

## 4. Common-random-number rule

Common random numbers are used only when the random quantity has the same semantic meaning across arms.

~~~math
\boxed{
CRN(a,b)
\Rightarrow
same\ stochastic\ quantity
+
compatible\ draw\ protocol.
}
~~~

If an intervention/model changes whether a stochastic quantity exists, do not force a meaningless shared draw. Record N/A or a treatment-specific stream.

## 5. Draw-order robustness

A single sequential PRNG stream may produce different downstream draws when one arm consumes a different number of random values.

Therefore, for confirmatory matched comparisons prefer:
- named independent streams;
- counter-based generators/substreams; or
- an explicitly frozen draw schedule.

This is a reproducibility control, not a requirement to use a particular software library.

## 6. Seed/probability firewall

~~~math
\boxed{
\text{seed}
\neq
\text{distribution evidence}.
}
~~~

~~~math
\boxed{
\text{number of sampled scenarios}
\neq
\text{event probability}.
}
~~~

A scenario weight/probability requires its own scientific justification.

## 7. Freeze timing

The comparison-group and seed manifests must be frozen before confirmatory target-result inspection.

Post-result RNG or scenario changes require versioned amendment and may invalidate confirmatory status.

## 8. Result-blind scenario inclusion

Scenario inclusion/exclusion rules are based on:
- domain membership;
- data quality;
- admissibility;
- preregistered stratification;
- computational feasibility rules frozen before result inspection.

A scenario cannot be removed because it weakens H1–H5.

## 9. Match audit outputs

For every comparison group produce:
- held-field equality report;
- allowed-difference report;
- seed-stream equality/compatibility report;
- root/hash consistency report;
- PASS/BLOCKED/FAIL match status.
