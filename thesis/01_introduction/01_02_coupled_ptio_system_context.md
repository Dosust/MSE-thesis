## 1.2 Coupled Power–Electrified Transportation System Context

The physical infrastructure core is:

```math
\boxed{P\leftrightarrow T_e}
```

where `P` denotes the Power System and `T_e` denotes the Electrified Transportation System.

For this thesis:

> **In this thesis, the electrified transportation system comprises the electrically propelled road vehicle, its rechargeable energy-storage system, electric propulsion and auxiliary electrical systems, the vehicle power-supply circuit, electric-vehicle supply equipment, the physical charging connection, and the communication and control functions required for electrical power transfer, including bidirectional transfer where supported (ISO 6469; ISO 5474; ISO 15118; IEC 61851; IEC 62196).**

EVSE and the physical charging connection belong to `T_e`. The external Power System remains distinct. Mathematical coupling variables may describe power, energy, current, charging demand, charging capability, communication/control conditions, or supported reverse transfer, but they do not form a third physical infrastructure system.

The active research considers only **thermal interdependencies**. A directional relation is active when a heat- or temperature-dependent physical state, thermal capability, or thermally conditioned operating limit changes the cross-system dependency or its consequence.

The directional logic is:

```text
P → T_e:
Power thermal state / temperature-dependent capability
→ electrical capability available to T_e
→ charging capability
→ vehicle energy state / availability
→ mobility consequence
```

and, where physically supported,

```text
T_e → P:
T_e thermal state / temperature-dependent charging or transfer capability
→ charging demand or supported reverse transfer
→ Power-system state / capability consequence
```

Reciprocity is not assumed. Each direction requires independent physical and evidential qualification.

Permanent distinctions are:

```text
common heat exposure ≠ thermal interdependency
connection ≠ directional dependency
thermal state ≠ function ≠ service
interface variable ≠ third physical system
```
