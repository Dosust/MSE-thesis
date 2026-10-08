# Module 01 Standards Spine V1 — Transformer Thermal-State Physics

**Status:** ACTIVE OFFICIAL-AUTHORITY BACKBONE — CLAUSE-LEVEL AUDIT PARTLY OPEN  
**Effective date:** 2026-10-08  
**Evidence class:** primarily `[A1]`  
**Evidence authority:** `../CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md`

## 1. Purpose

The standards spine defines which transformer quantities, tests, loading concepts, temperature criteria, and measurement procedures should be taken from official authorities rather than invented or inferred from secondary literature.

Standards are **not counted as part of the 200-paper corpus**.

Permanent distinction:

```text
standard definition / procedure / limit
≠
peer-reviewed constitutive model
≠
thesis-derived relation
```

## 2. Current verified official authorities

### S1 — IEEE C57.91-2025

**Title:** IEEE Guide for Loading Mineral-Oil-Immersed Transformers and Step-Voltage Regulators  
**Organization:** IEEE  
**Edition/year:** 2025  
**Current role in Module 01:** loading, ambient-temperature effects, cooling considerations, transformer temperature criteria, and loading/temperature calculation guidance.  
**Authority class:** `[A1]`  
**Official source:** https://standards.ieee.org/ieee/C57.91/7163/

**Current admissible statement:** the guide is an official loading authority for mineral-oil-immersed transformers and addresses temperature/loading criteria and calculation methods.

**Still OPEN pending direct clause-level audit:**
- exact equations to be used;
- exact thermal limits;
- exact clause/table numbers;
- exact treatment applicable to the eventual transformer/cooling architecture.

### S2 — IEEE C57.169-2023

**Title:** IEEE Guide for Determination of Maximum Winding Temperature Rise in Liquid-Immersed Transformers  
**Organization:** IEEE  
**Edition/year:** 2023  
**Current role:** hottest-spot determination, model criteria, direct winding-temperature measurement, sensor-location guidance, and thermal-model development/validation context.  
**Authority class:** `[A1]`  
**Official source:** https://standards.ieee.org/ieee/C57.169/7584/

**Current admissible statement:** this is a current official IEEE authority specifically relevant to winding hottest-spot determination and measurement/model guidance.

**Still OPEN:**
- exact clauses;
- exact measurement requirements;
- exact model-acceptance criteria;
- applicability to the eventual transformer geometry.

### S3 — IEEE C57.12.90-2026

**Title:** IEEE Standard Test Code for Liquid-Immersed Distribution, Power, and Regulating Transformers  
**Organization:** IEEE  
**Edition/year:** 2026  
**Current role:** official transformer test-code context including loss and temperature tests.  
**Authority class:** `[A1]`  
**Official source:** https://standards.ieee.org/ieee/C57.12.90/10944/

**Still OPEN:**
- exact clauses relevant to Module 01;
- exact loss/temperature-test procedure details required by the final case.

### S4 — IEC 60076-1:2011

**Title:** Power transformers — Part 1: General  
**Organization:** IEC  
**Edition/year:** 2011  
**Current role:** general transformer definitions/requirements and parent standard context.  
**Authority class:** `[A1]`  
**Official source:** https://webstore.iec.ch/en/publication/588

### S5 — IEC 60076-2:2011

**Title:** Power transformers — Part 2: Temperature rise for liquid-immersed transformers  
**Organization:** IEC  
**Edition/year:** 2011  
**Current role:** temperature-rise terminology, temperature-rise limits, cooling identification, and temperature-rise test procedures for liquid-immersed transformers.  
**Authority class:** `[A1]`  
**Official source:** https://webstore.iec.ch/en/publication/599

**Current admissible statement:** this standard is directly relevant to experimental temperature-rise testing and the interpretation of measured top-oil/winding temperature behavior.

**Still OPEN:**
- exact clause/table limits;
- exact steady-state criterion and measurement procedure to be used in the thesis;
- exact applicability to the final transformer.

### S6 — IEC 60076-7:2018

**Title:** Power transformers — Part 7: Loading guide for mineral-oil-immersed power transformers  
**Organization:** IEC  
**Edition/year:** 2018  
**Current role:** loading under different ambient conditions, operating temperatures, thermal ageing, overload/loading calculations, and IEC thermal-model guidance.  
**Authority class:** `[A1]`  
**Official source:** https://webstore.iec.ch/en/publication/34351

**Current admissible statement:** IEC 60076-7:2018 is a current official loading/thermal-model authority for mineral-oil-immersed transformers.

**Still OPEN:**
- exact equations and symbols;
- exact parameter recommendations;
- exact differences from current IEEE C57.91-2025;
- case-specific applicability.

### S7 — IEC 60076-14:2013

**Title:** Power transformers — Part 14: Liquid-immersed power transformers using high-temperature insulation materials  
**Organization:** IEC  
**Edition/year:** 2013  
**Role:** conditional authority only if the eventual transformer uses a high-temperature insulation system covered by this standard.  
**Authority class:** `[A1]`  
**Official source:** https://webstore.iec.ch/en/publication/594

**Current status:** `CONDITIONAL / NOT ACTIVE FOR MODELING YET`.

## 3. Authority-use matrix

| Scientific object | Primary official authority candidate | Current status |
|---|---|---|
| Transformer general terminology | IEC 60076-1 | VERIFIED authority identity |
| Temperature-rise definitions/tests | IEC 60076-2 | VERIFIED authority identity; clause-level audit OPEN |
| Loading / operating temperature | IEC 60076-7; IEEE C57.91 | VERIFIED authority identity; direct comparison OPEN |
| Hottest-spot determination/measurement | IEEE C57.169 | VERIFIED authority identity; clause-level audit OPEN |
| Loss / temperature test code | IEEE C57.12.90 | VERIFIED authority identity; clause-level audit OPEN |
| High-temperature insulation systems | IEC 60076-14 | CONDITIONAL |
| Final transformer-specific ratings | Exact manufacturer/certified documentation | OPEN |
| Final transformer-specific thermal limits | Applicable standard + exact manufacturer authority | OPEN |
| Final transformer-specific derating/capability relation | Applicable standard/manufacturer evidence | OPEN |

## 4. Standard-to-paper separation

The standards spine must be used to prevent role confusion.

```text
Standards establish:
terminology
+ ratings / permitted operating concepts
+ test methods
+ loading rules
+ measurement procedures
+ normative limits where specified
```

```text
Papers establish:
physical mechanisms
+ reduced/detailed mathematical models
+ parameter-identification methods
+ experimental observations
+ validation domains
+ limitations
```

Therefore:

```text
standard model ≠ exact component parameterization
paper model ≠ normative loading limit
manufacturer limit ≠ universal physical law
```

## 5. Clause-level audit rule before model freeze

Before any standard equation, limit, threshold, or procedure is used in the thesis, create a provenance record with:

```text
organization
+ standard number
+ title
+ edition/year
+ clause/table/equation
+ exact technical object established
+ applicability conditions
+ direct-access status
+ thesis-use decision
```

If direct access is unavailable, the claim remains:

```text
OPEN — DIRECT STANDARD VERIFICATION REQUIRED
```

## 6. Current standards-spine conclusion

Module 01 has a sufficient official-authority map to continue literature reading, but **not yet sufficient clause-level evidence to freeze transformer thermal limits, exact standard equations, or state-to-capability laws**.
