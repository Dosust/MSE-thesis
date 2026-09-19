# Stage 7 Master Register v2 — Workbook Provenance

**Status:** GENERATED / VERIFIED EXECUTABLE REGISTER  
**Date:** 2026-09-19  
**Artifact:** \`STAGE7_MASTER_REGISTER_V2.xlsx\`

## Exact byte identity

\`\`\`text
size_bytes = 24385
sha256     = a29aedb30dd8855a92cc11968780adea26c3b8db6888752423922471efb67743
git_blob   = 8b0fe00ba3d7ae42dc999fd4749359087a97659d
\`\`\`

The Git-compatible blob value is the hash of the exact generated workbook bytes and can be used to verify any later repository/materialized copy.

## Workbook sheets

1. \`00_Overview\`
2. \`01_Stage6_Input\`
3. \`02_Admissibility\`
4. \`03_Decision_Objectives\`
5. \`04_Pareto_Dominance\`
6. \`05_Value_Firewall\`
7. \`06_H5_Comparator\`
8. \`07_Uncertainty\`
9. \`08_Robustness_Regret\`
10. \`09_Scenario_Discovery\`
11. \`10_Adaptive_Eligibility\`
12. \`11_Benchmark_VVUQ\`
13. \`12_Decision_Stability\`
14. \`13_Gates_Claims\`
15. \`14_Provenance\`
16. \`_Lists\`

## Verification fixtures

\`\`\`text
H5 Jaccard fixture       expected 2/3; observed 0.6666666666666667  PASS
Regret fixture           A=(2,3), B=(0,0)                        PASS
Scenario coverage        A=0.5, B=1.0                            PASS
Formula-error scan       expected 0; observed 0                   PASS
\`\`\`

These are implementation-verification fixtures only.

## Scientific status

The workbook intentionally contains no final:
- preferred intervention;
- stakeholder weights;
- \(\delta_5\);
- unsupported scenario probabilities;
- adaptive triggers;
- H5 result.

\`\`\`text
H5 = NOT TESTED
\`\`\`
