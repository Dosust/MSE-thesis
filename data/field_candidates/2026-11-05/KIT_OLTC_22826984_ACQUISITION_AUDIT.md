# KIT OLTC multivoltage + EV measurements: dated acquisition and qualification audit

**Date:** 2026-11-05  
**Current thesis:** Engineering of Power–Electrified Transportation Interdependencies for Resilience  
**Primary dataset source:** https://zenodo.org/records/22826984  
**User-local originals:** ~/Downloads/KIT_OLTC_22826984/  
**Evidence status:** Original files **acquired and MD5-verified on the user's Mac**, schemas checked, and full **129,600,000-row 100 ms UTC timestamp-grid PASS** (0 mismatches), according to user-supplied Terminal results. **No raw Parquet files uploaded to GitHub or accessed by this research agent.** All findings below are reported from those pasted local logs, not an independent rerun.

## 0. Controlling scientific scope

- [Canonical thesis title V3](../../../project/CANONICAL_THESIS_TITLE_V3.md).
- [Canonical extreme-heat thermal-only scope V4](../../../project/CANONICAL_EXTREME_HEAT_THERMAL_INTERDEPENDENCY_STATE_TIME_SCOPE_AMENDMENT_V4.md).
- [Canonical SO1–SO3](../../../project/CANONICAL_THERMAL_INTERDEPENDENCY_RESEARCH_OBJECTIVES_V1.md): **SO1** qualify thermal states and directional thermal mechanisms between Power P and Electrified Transportation T_e; **SO2** develop a physics-based state-time model under extreme heat; **SO3** quantify transition times, propagation and electricity/mobility-service consequences.
- [Evidence and non-invention standard](../../../project/CANONICAL_EVIDENCE_NON_INVENTION_STANDARD_V1.md). Electric-vehicle supply equipment (EVSE) belongs to T_e, not a third infrastructure system.

The KIT dataset is a candidate for **supporting electrical interface/boundary-condition evidence**. It does not, by itself, establish an extreme-heat-driven thermal interdependency, transformer or EVSE temperature state, thermal power derating, causal directional propagation or mobility-service resilience.

## 1. Discovery and replacement-dataset context

The study needed data complementing or replacing the on-request **Krama et al. (2026)** 50 kW DC charger extreme-heat field observations, DOI https://doi.org/10.1016/j.ecmx.2026.101960. KIT Zenodo record 22826984 was identified as a possible **electrical** complement: multivoltage measurements with an EV charging branch. It is **not equivalent** to measured Qatar EVSE thermal derating. See [separate search audit](EVSE_EXTREME_HEAT_REPLACEMENT_SEARCH.md).

## 2. Step 1: search existing local files

The user first searched HOME by five patterns. No filename match was printed.

~~~bash
find "$HOME" -type f \( \
  -iname "*KIT*voltage*" -o -iname "*22826984*" -o \
  -iname "*electrothermal*" -o -iname "*transformer*EVSE*" -o \
  -iname "*charging*thermal*" \
\) -not -path "*/Library/*" -print 2>/dev/null
~~~

Broader search in Downloads, Documents and Desktop found **only unrelated matches** (e.g. Python library transformers, EndNote source names), not KIT Zenodo record 22826984.

~~~bash
find "$HOME/Downloads" "$HOME/Documents" "$HOME/Desktop" \
  -type f \( -iname "*22826984*" -o -iname "*voltage*" -o \
  -iname "*measurement*" -o -iname "*KIT*" -o \
  -iname "*transformer*" -o -iname "*EVSE*" \) -print 2>/dev/null
~~~

Targeted check excluding virtual environments produced no matching file output:

~~~bash
find "$HOME/Downloads" "$HOME/Documents" "$HOME/Desktop" \
  -type f -not -path "*/.venv/*" \
  -not -path "*/site-packages/*" \
  -not -path "*/node_modules/*" \
| grep -Ei '22826984|OLTC|multivoltage|voltage.fluctuation|110.?kV|20.?kV'
~~~

**Meaning:** no relevant local filenames found in searched folders; filename searches do not rule out data stored inside archives or renamed files.

## 3. Step 2: first download attempt

The following three source files were selected from https://zenodo.org/records/22826984:

| Exact original file | Instrument designation |
|---|---|
| oltc_fail_110kV_PMU04_TK1_100ms.parquet | 110 kV PMU04 TK1 |
| oltc_fail_20kV_PMU01_J01_100ms.parquet | 20 kV PMU01 J01 |
| oltc_fail_400V_EV_SH.J.6_100ms.parquet | 400 V EV SH.J.6 |

~~~bash
mkdir -p ~/Downloads/KIT_OLTC_22826984
cd ~/Downloads/KIT_OLTC_22826984
for file in \
  "oltc_fail_110kV_PMU04_TK1_100ms.parquet" \
  "oltc_fail_20kV_PMU01_J01_100ms.parquet" \
  "oltc_fail_400V_EV_SH.J.6_100ms.parquet"
do
  echo "Downloading: $file"
  curl -fL -C - --retry 5 --retry-delay 5 \
    "https://zenodo.org/records/22826984/files/$file?download=1" \
    -o "$file"
done
ls -lh *.parquet
~~~

**First user-terminal attempt FAILED for all three transfers (curl error 18, premature connection termination):**
- 110 kV: 72% (~663M displayed), 266,149,995 bytes remaining.
- 20 kV: 52% (~374–375M), 352,400,492 bytes remaining.
- 400 V EV: 61% (~627M), 418,590,518 bytes remaining.

Partial bytes were **not** declared complete.

## 4. Step 3: resumed transfers

The previously downloaded bytes were preserved. A retry loop using curl byte-range resumption was executed:

~~~bash
cd "$HOME/Downloads/KIT_OLTC_22826984" || exit 1
for file in \
  "oltc_fail_110kV_PMU04_TK1_100ms.parquet" \
  "oltc_fail_20kV_PMU01_J01_100ms.parquet" \
  "oltc_fail_400V_EV_SH.J.6_100ms.parquet"
do
  echo "Resuming: $file"
  curl --fail --location --continue-at - \
    --retry 15 --retry-delay 10 --retry-all-errors \
    --connect-timeout 30 \
    "https://zenodo.org/records/22826984/files/$file?download=1" \
    --output "$file"
  if [ $? -ne 0 ]; then
    echo "INCOMPLETE: $file"
  else
    echo "Transfer completed: $file"
  fi
done
ls -lh *.parquet
~~~

**Pasted resume output:** 20 kV resumed from byte 392,923,816 and completed the remaining ~336M; 400 V EV resumed from byte 657,923,352 and completed remaining ~399M. Full 110 kV resume log not pasted, but final matching checksum was later reported. Final Mac listing:

~~~text
917M  oltc_fail_110kV_PMU04_TK1_100ms.parquet
711M  oltc_fail_20kV_PMU01_J01_100ms.parquet
1.0G  oltc_fail_400V_EV_SH.J.6_100ms.parquet
~~~

Sizes are human-rounded output, not immutable exact byte counts.

## 5. Step 4: original file-integrity check: PASS on user Mac

The user reported:

~~~text
=== KIT DATASET INTEGRITY CHECK ===
PASS: oltc_fail_110kV_PMU04_TK1_100ms.parquet
PASS: oltc_fail_20kV_PMU01_J01_100ms.parquet
PASS: oltc_fail_400V_EV_SH.J.6_100ms.parquet
~~~

Compared expected publisher MD5s (https://zenodo.org/records/22826984):

| File | Expected MD5 | User-terminal check |
|---|---|---|
| 110kV_PMU04_TK1 | e71d6e8c204290a51c9bf0526296435c | PASS |
| 20kV_PMU01_J01 | c630660151a82604ea853fc10943f91a | PASS |
| 400V_EV_SH.J.6 | e779aa105c45dfbb810bca73171afa0d | PASS |

This supports a claim of **user-local publisher-matching original bytes**, not GitHub upload or independent check in this chat runtime. Preserve raw files. Capture additional local SHA-256 audit when convenient:

~~~bash
cd "$HOME/Downloads/KIT_OLTC_22826984" || exit 1
shasum -a 256 *.parquet > KIT_OLTC_22826984_SHA256_LOCAL.txt
~~~

## 6. Step 5: PyArrow metadata/schema inspection: completed

Mac Python package output: pyarrow **24.0.0**, installed under Python **3.13**. Executed read-only script:

~~~python
import pyarrow.parquet as pq
from pathlib import Path
folder = Path.home() / "Downloads/KIT_OLTC_22826984"
for file in sorted(folder.glob("*.parquet")):
    pf = pq.ParquetFile(file)
    print("FILE:", file.name)
    print("ROWS:", pf.metadata.num_rows)
    print("ROW GROUPS:", pf.num_row_groups)
    print(pf.schema_arrow)
~~~

**Every file:** 43,200,000 rows; 44 row groups. **Sum across files:** 129,600,000 rows, not yet proved 129.6M valid synchronized three-site tuples.

**110 kV (15 columns):** time[UTC] timestamp[us,UTC]; fault_phase string; u_L1[V], u_L2[V], u_L3[V], u_pos[V]; i_L1[A], i_L2[A], i_L3[A], i_pos[A]; f[Hz]; rocof[mHz/s]; p[MW]; q[MVAr]; s[MVA]. Physical numerics are double.

**20 kV (10 columns):** time[UTC] timestamp[us,UTC]; fault_phase string; u_L1[V], u_L2[V], u_L3[V], u_pos[V]; i_L1[A], i_L2[A], i_L3[A], i_pos[A]. Physical numerics are double.

**400 V EV (14 columns):** time[UTC] timestamp[us,UTC]; fault_phase string; u_L1[V], i_L1[A], p_L1[W], q_L1[var]; u_L2[V], i_L2[A], p_L2[W], q_L2[var]; u_L3[V], i_L3[A], p_L3[W], q_L3[var]. Physical numerics are double.

**No reported schema columns:** ambient temperature, transformer top-oil/hot-spot temperature, EVSE rectifier/connector temperature, cooling actuation, EV battery SOC, charger temperature-triggered power derating, required charging energy by departure, mobility-service availability.

**Important:** header units/types are observed from schema; calibration, reference directions, sensor positions, missingness and actual topology remain open.

## 7. Step 6: timestamp metadata boundaries: completed

The user executed PyArrow inspection of each row group's timestamp min/max and first-column statistics. The script checked start/end, expected end under 100 ms, adjacent row-group edge difference and identical time-range endpoints across files. **Output for all three:**

~~~text
START: 2026-02-03 23:00:00+00:00
END:   2026-03-25 22:59:59.900000+00:00
ROWS: 43200000
EXPECTED END: 2026-03-25 22:59:59.900000+00:00
EXPECTED SPAN MATCH: True
ROW-GROUP BOUNDARY ISSUES: 0
FIRST ISSUES: []
IDENTICAL TIME RANGES: True
~~~

Duration: 50 days at nominal 100 ms; 50 × 24 × 3,600 × 10 = 43,200,000 samples **per file**.

**Limitations:** row-group extrema/edges are not a full-row continuity check. Intra-group missing/duplicated/out-of-order timestamps or clock-drift disagreement are still possible; equal windows do not establish electrical connectivity or synchronization to an independent reference clock.

## 8. Step 7: ALL-ROW 100 ms UTC GRID TEST: PASS (user-terminal readback)

**Evidence update received:** 2026-11-05. The user ran the earlier inline Python/PyArrow+NumPy batch scan supplied in conversation (not a separately evidenced run of the subsequently committed repository script). This scans each observed timestamp in file order against the exact expected 100 ms UTC timestamp at the corresponding zero-based row position, with start at 2026-02-03 23:00:00 UTC. It also counts null timestamps as mismatches. **Full console output pasted by user:**

~~~text
FILE: oltc_fail_110kV_PMU04_TK1_100ms.parquet
ROWS CHECKED: 43200000
TIMESTAMP MISMATCHES: 0
RESULT: PASS

FILE: oltc_fail_20kV_PMU01_J01_100ms.parquet
ROWS CHECKED: 43200000
TIMESTAMP MISMATCHES: 0
RESULT: PASS

FILE: oltc_fail_400V_EV_SH.J.6_100ms.parquet
ROWS CHECKED: 43200000
TIMESTAMP MISMATCHES: 0
RESULT: PASS
~~~

**Arithmetic:** 3 × 43,200,000 = **129,600,000 checked rows**, **zero reported timestamp mismatches**. Therefore all three user-local files follow the **same ideal UTC 100 ms grid in strict row order** for the checked window (according to the terminal readback). Unlike §7 metadata min/max, this is a full per-record UTC grid test. It rejects missing/repeated/out-of-order/on-grid-offset timestamps relative to the reference and null timestamps (under the actual inline program logic).

**Remaining validity limits:** This is an **intra-dataset timestamp-coordinate test**, not an external sensor-clock calibration or independent proof that the three instruments measured a common electrical circuit. The source timestamp clock could share systematic errors not detectable by grid checks. The user has **not** uploaded the three Parquet files or a JSON report to this GitHub repository; the evidence is the pasted Terminal transcript, not raw-data readback by the GitHub connector.

The separate committed [KIT timestamp auditor](../../../tools/kit_oltc_timestamp_audit.py) is maintained for reproducibility. Its own JSON output has **not** been submitted as of this update. Do not confuse the earlier successful inline algorithm with execution of that newly committed file.

**Topology evidence update (2026-11-05):** Published KIT Campus North architecture confirms three 110/20 kV input transformers (87 MVA total), two 20 kV buses and multiple MV/LV distribution stations. However, this does **not** establish that the exact source files PMU04_TK1, PMU01_J01 and EV_SH.J.6 are on one parent-child power path. See [source-bound exact-path audit](KIT_OLTC_ELECTRICAL_TOPOLOGY_EVIDENCE_AUDIT.md). G3 remains OPEN for precise sensor wiring and historical switch states.

## 9. Admission gates: statuses are distinct

| Gate | Status | Basis |
|---|---|---|
| G0 operational real-field source | OPEN | Source described multivoltage EV measurements; exact routine-field-versus-controlled-experiment provenance not independently audited. |
| G1 original file acquisition/integrity | USER-LOCAL PASS (MD5) | Three files present and publisher MD5 matched according to pasted Mac output; local SHA-256/GitHub raw-data backup not done. |
| G2 schema, sensors, units/QC | PARTIAL | Variables, types, header units, row/row-group count established; semantic definitions and missingness/open validity checks remain. |
| G3 physical P ↔ T_e topology | CAMPUS NETWORK CONFIRMED; EXACT SENSOR PATH OPEN | Publisher and KIT technical sources support 110/20/0.4 kV campus connectivity, but the PMU04_TK1 → PMU01_J01 → EV_SH.J.6 feeder/transformer map and 2026 switch states are not documented. See topology audit. |
| G4 synchrony/thermal-state adequacy | ELECTRICAL RECORD GRID PASS; THERMAL ABSENT | User-terminal full-row 100 ms UTC grid PASS: 43.2M rows × 3, zero mismatches; independent sensor-clock accuracy, site topology, and all thermal states remain unverified. |
| G5 model validation and uncertainty | NOT STARTED | No KIT model calibration, holdout, uncertainty or validated output. |
| G6 directional thermal effect | NOT ESTABLISHED | No measured temperatures, derating mechanism or heat-driven causality. |
| G7 service-level consequences | NOT ESTABLISHED | No charging-by-departure demand or realized mobility-service outcome. |

## 10. Next verified-action queue (do not repeat completed work)

1. **Provenance:** archive the original full-row timestamp Terminal output or a reproducible JSON report plus local SHA-256 hashes; **do not rerun the completed 129.6M-row check merely to create a new claim**.
2. **Equipment topology:** inspect source publisher metadata/diagram and instrument descriptions to establish whether all 110 kV, 20 kV and 400 V EV measurements lie on the same physical path and verify source IDs.
3. **Signal quality:** streaming checks for null/NaN/Inf, power/current sign conventions, extrema, fault_phase semantics, measurement quality, and sampling/phase labels.
4. **Electrical analysis:** if topology and QA pass, test bounded voltage/power response and event propagation; do not relabel it thermal coupling.
5. **Thermal acquisition:** independently pursue a measured EVSE rectifier/connector internal temperature plus ambient, power and cooling/derating dataset. Do not synthetically relabel KIT measurements as temperatures.
6. **Register update:** place observed/checksum evidence and open gates in master field register; no empirical heat/SO3 validation claim without the respective source.

## 11. Traceability

- **Publisher:** https://zenodo.org/records/22826984.
- **Actual step results:** user's 2026-11-05 Terminal messages (filename search, curl attempts, resume, ls, MD5 PASS, PyArrow schema, metadata time-range audit, and full 129.6M-row 100 ms-grid test with zero reported mismatches).
- **Canonical thesis interpretation:** repository authorities linked in §0.
- **Open/unknown:** actual raw-byte access here, SHA-256, independent external time reference / sensor clock calibration, true network topology, signal-value validity, observed thermal variables, independent model validation, extreme-heat exposure, service-level outcomes.

**This dated acquisition report does not amend or freeze the thesis model or any canonical research objective.**
