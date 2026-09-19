# Stage 4 Gate Specification v1

## Gate semantics

- \`PASS\`: criterion is satisfied; the accepted object may propagate.
- \`OPEN\`: criterion has not yet been adjudicated/frozen.
- \`BLOCKED\`: a prerequisite definition/evidence/parameter is missing; this is **not** falsification.
- \`FAIL\`: the declared criterion is contradicted/invalid in the tested domain.

\`\`\`math
\boxed{BLOCKED\neq FAIL}
\`\`\`

## A. Constitution gate

\`\`\`math
\boxed{G_{4-CON}=G_{RQ4}\land G_{trace}\land G_{objects}\land G_{semantics}\land G_{math}}
\`\`\`

## B. Case-realization gate

\`\`\`math
\boxed{
G_{4-CASE}=G_{binding}\land G_{data}\land G_{measurement}\land G_{OBS}\land G_E\land G_I\land G_{ORG}\land G_C
}
\`\`\`

## C. V&V gate

\`\`\`math
\boxed{G_{4-V}=G_{code}\land G_{solution}\land G_{submodel}\land G_{calibration}\land G_{validity}}
\`\`\`

where applicable to the selected case and claim.

## D. H2 gate

\`\`\`math
\boxed{G_{4-H2}=G_{prereg}\land G_{matched}\land G_{QOI}\land G_{execution}\land G_{uncertainty}\land G_{decision}}
\`\`\`

A software fixture or unmatched comparison cannot make \(G_{4-H2}\) pass.

## E. Stage-4→5 closure

\`\`\`math
\boxed{G_{4\to5}=G_{4-CON}\land G_{4-CASE}\land G_{4-V}\land G_{4-H2}.}
\`\`\`

No downstream PASS can compensate for an upstream FAIL; BLOCKED prerequisites remain BLOCKED until evidence closes them.
