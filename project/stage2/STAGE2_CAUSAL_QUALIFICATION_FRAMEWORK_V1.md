# Stage 2 Causal Qualification Framework v1

**Status:** WORKING SCIENTIFIC FRAMEWORK — NOT FROZEN  
**Date:** 2026-09-18

## 1. Scientific question

> **RQ2: Why and through which mechanisms do components and layers affect each other?**

Stage 2 asks, for every frozen Stage-1 candidate relation `e`:

~~~math
\boxed{\text{Does a genuine causal dependency operate here, why, and under what conditions?}}
~~~

## 2. Input

The only admissible Stage-2 starting object is a Stage-1 relation record:

~~~math
\mathfrak r_e^{(1)}=(\mathcal V_e,\sigma_e,\Gamma_e^{\rm str},\gamma_e,\Phi_e,d_e,m_e^{\rm cand},c_e^{\rm cand},s_e,\mathcal E_e).
~~~

Stage 2 cannot silently edit this object. It can only qualify, reject, or leave unresolved the proposed causal mechanism.

## 3. Required causal questions

For each candidate `e`, Stage 2 must answer:

1. **Source:** which entity/state is the putative cause?
2. **Receiver:** which entity/state responds?
3. **Direction:** what directional claim is being tested?
4. **Interface:** through what physical/operational/information/organizational boundary?
5. **Exchange:** what realized service/resource/information/action crosses or enables the relation?
6. **Mechanism:** why should the receiver respond?
7. **Activation:** under what state/mode/event is the mechanism active?
8. **Response form:** what qualitative/logical/quantitative mapping links source to receiver?
9. **Parameter/timescale:** what parameters, delays or characteristic times are required?
10. **Evidence:** what direct, case, empirical, operational and contrary evidence exists?
11. **Validity:** where, when and for which asset/operating regimes is the claim valid?
12. **Falsification:** what observation would reject or force revision of the claim?

## 4. Causal-evidence workflow

~~~text
Stage-1 candidate r_e^(1)
  -> define exact causal claim
  -> identify interface + realized exchanged signal
  -> specify mechanism family
  -> define activation predicate
  -> verify case connection
  -> assemble evidence portfolio
  -> define response-law class
  -> identify/bound parameters and delay
  -> declare validity domain
  -> declare falsification condition
  -> G2 component gates
  -> PASS / FAIL / BLOCKED
  -> if PASS: causally qualified I_e
  -> if PASS + parameter-ready: eligible for Stage 3
~~~

## 5. Two legitimate evidence routes

### Route A — physics/engineering mechanism

Use where a defensible physical/engineering requirement determines the dependency, for example electrical supply to a signal controller. Required evidence still includes the **case connection** and operating/activation conditions.

~~~math
\boxed{\text{engineering law/requirement}+\text{case connection}+\text{activation}+\text{observational/technical evidence}}
~~~

### Route B — empirical/operational mechanism

Use where the relation is behavioral, organizational, mobility-mediated, or otherwise not fixed by a direct physical law.

~~~math
\boxed{\text{mechanism hypothesis}+\text{case linkage}+\text{temporal/empirical evidence}+\text{alternative-explanation control}}
~~~

No single identification technique is required for all mechanisms.

## 6. Evidence portfolio — never a single default score

~~~math
\boxed{
\mathbf e_e=(
e_{\rm mech},
e_{\rm case},
e_{\rm interface},
e_{\rm activation},
e_{\rm temporal},
e_{\rm empirical},
e_{\rm operational},
e_{\rm contrary}
)}
~~~

The components answer different questions and are not automatically collapsed into one scalar confidence number.

## 7. Parameter status is separate from causal status

~~~math
\boxed{S_e^\theta\in\{\mathrm{UNESTIMATED},\mathrm{BOUNDED},\mathrm{CALIBRATED},\mathrm{VALIDATED}\}}
~~~

A mechanism may pass causal qualification while its magnitude remains unestimated:

~~~math
\boxed{G_2(e)=\mathrm{PASS}\ \not\Rightarrow\ S_e^\theta=\mathrm{VALIDATED}}
~~~

## 8. Common cause is not cross-infrastructure causality

~~~math
\boxed{\eta\rightarrow P,\ \eta\rightarrow T\ \not\Rightarrow\ P\rightarrow T\ \text{or}\ T\rightarrow P}
~~~

## 9. Stage-3 readiness

Causal acceptance and dynamic-model readiness are separate decisions:

~~~math
\boxed{G_{2\to3}(e)=G_2^{\rm causal}(e)\land G_P(e)}
~~~

`G_P` asks whether the mechanism has a sufficiently explicit logical/functional/parameter form for Stage 3 without inventing missing dynamics.

## 10. Primary initial P↔T mechanism families

| ID | Direction | Mechanism family | Stage-2 status |
|---|---|---|---|
| M2-PT-01 | P→T | traffic-signal electrical-service dependency | OPEN |
| M2-PT-02 | P→T | EV charging-service availability dependency | OPEN |
| M2-TP-01 | T→P | restoration/repair-access dependency | OPEN |
| M2-TP-02 | T→P | EV charging-demand effect on distribution system | OPEN |
| M2-TP-03 | T→P | V2G/mobile-storage support dependency | OPEN |

These are prior-evidence mechanism families, not accepted case dependencies.

## 11. Scientific non-claims

Stage 2 does **not** assume:

- that every Stage-1 candidate is causal;
- that reciprocal arrows are simultaneously active;
- that one coupling weight describes all mechanisms;
- that literature evidence establishes a case connection;
- that common hazard exposure is P↔T causality;
- that an accepted mechanism already supplies a validated Stage-3 dynamic law;
- that mechanism acceptance implies resilience benefit or harm.

## 12. Output

Stage 2 outputs an auditable set:

~~~math
\boxed{\mathbb I_{\rm acc}=\{\mathfrak I_e:G_2(e)=\mathrm{PASS}\}}
~~~

with rejected and blocked candidates preserved for traceability.