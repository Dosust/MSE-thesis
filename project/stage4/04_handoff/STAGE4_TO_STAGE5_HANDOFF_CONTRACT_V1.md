# Stage 4 → Stage 5 Handoff Contract v1

Stage 5 may consume only Stage-4 information/control objects accepted under the declared claim ceiling.

\`\`\`math
\boxed{
I_{4\to5}(t)=
(b_t,\mathbb U_{\widehat Y,t},\mathcal I_t,z_I(t),z_O(t),\mathcal U_{feas}(t))
}
\`\`\`

Mandatory distinctions:

\`\`\`math
Y_t^{phys}\not\equiv b_t,\qquad
\mathcal G_I\neq z_I\neq\mathcal I_t,\qquad
\mathfrak O\neq z_O(t),\qquad
\mathcal U_{phys}\not\equiv\mathcal U_{feas}.
\`\`\`

If a component is unavailable, Stage 5 must remain blocked, use an explicitly declared ideal-information/reference branch, or lower the claim ceiling. Missing components may not be silently replaced with perfect knowledge or unlimited control.

\`\`\`math
\boxed{G_{4\to5}=G_{4-CON}\land G_{4-CASE}\land G_{4-V}\land G_{4-H2}.}
\`\`\`
