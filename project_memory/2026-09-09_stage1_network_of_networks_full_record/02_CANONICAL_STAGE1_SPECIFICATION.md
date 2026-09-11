# Canonical Stage-1 Specification

## Role

**Stage 1 - Multilayer Structure**  
Role: P-T-I-O architecture  
Main question: **What exists?**

## System

```math
\boxed{\mathscr S=\{\mathcal P,\mathcal T,\mathcal I,\mathcal O\}}
```

## Heterogeneous network-of-networks

```math
\boxed{
\mathfrak N_1=
\left(
\{\mathcal G_P,\mathcal G_T,\mathcal G_I,\mathcal G_O\},
V_C,E_\times,G_{geo},\chi_\times,\Phi_\times,\Theta,
\mathcal E_{prov},\Lambda_{sus}
\right)
}
```

where:

- `\mathcal G_P` - electrical bus/branch topology;
- `\mathcal G_T` - road-junction/directed-road topology;
- `\mathcal G_I` - communication/observation topology only when explicitly modeled;
- `\mathcal G_O` - actor/coordination topology only when explicitly modeled;
- `V_C` - cross-system interface assets, especially EV charging/V2G interfaces;
- `E_\times` - directed inter-system dependencies;
- `G_{geo}` - geographic co-exposure relationships;
- `\chi_\times` - dependency classes/types;
- `\Phi_\times` - exact mechanisms and carriers;
- `\Theta` - fixed model parameters;
- `\mathcal E_{prov}` - evidence provenance;
- `\Lambda_{sus}` - sustainability-ready metadata for Stage 6-7 translation.

## Initial state

```math
\boxed{
Y_0=
\begin{bmatrix}
X_P(0)\\
X_T(0)\\
Z(0)\\
I(0)\\
O(0)
\end{bmatrix}
}
```

## Supra-adjacency

```math
\boxed{
\mathbf A_{sup}=
\begin{bmatrix}
A_P&C_{PT}&C_{PI}&C_{PO}\\
C_{TP}&A_T&C_{TI}&C_{TO}\\
C_{IP}&C_{IT}&A_I&C_{IO}\\
C_{OP}&C_{OT}&C_{OI}&A_O
\end{bmatrix}
}
```

with generally rectangular and directional cross-blocks.

## Stage-1 boundaries

Do not include dynamic/counterfactual objects that belong downstream:

```math
h,e,\tau,F,J,u,K,\mathcal V.
```

## Frozen rules

1. Topology != dependency != parameter != dynamic state.
2. Common hazard exposure != causal dependency.
3. Every directional relation is justified independently.
4. Mediated pathways are not double-counted as direct links.
5. No dependency enters the model without direction + mechanism + component mapping + type + evidence.
6. Sustainability is not a fifth network layer; Stage 1 only preserves sustainability-ready metadata for Stages 6-7.
