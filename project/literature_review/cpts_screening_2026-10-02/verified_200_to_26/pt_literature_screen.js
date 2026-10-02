#!/usr/bin/env node
/**
 * Independent JavaScript verifier for the 200 -> 26 thesis literature screen.
 * Input: PT_200_screening_input.json produced by pt_literature_screen.py.
 * Output: PT_26_high_rigor_js.csv and PT_26_js.json.
 *
 * It reproduces the evidence-role architecture used by the Python pipeline:
 *   3 framework reviews, 8 heat-physics papers, 2 closest temperature/PT
 *   comparators, 8 core dynamic P-T papers, 3 service/control papers,
 *   and 2 transferable dynamic-coupling papers.
 *
 * This is title/abstract/metadata screening, not a substitute for full-text review.
 */
const fs = require('fs');
const path = require('path');

const ROOT = '/mnt/data';
const INPUT = path.join(ROOT, 'PT_200_screening_input.json');
const OUT_CSV = path.join(ROOT, 'PT_26_high_rigor_js.csv');
const OUT_JSON = path.join(ROOT, 'PT_26_js.json');

const rows = JSON.parse(fs.readFileSync(INPUT, 'utf8'));

const b = x => Boolean(x);
const contains = (s, re) => re.test(String(s || ''));
const num = x => Number(x || 0);

for (const r of rows) {
  const title = String(r.Title || '');
  const abs = String(r.Abstract || '');
  const isReview = contains(r.Document_Type, /review/i) || contains(title, /review/i);
  const ptTitle = contains(title, /power.*(?:transport|traffic)|(?:transport|traffic).*power/i);
  const evTitle = contains(title, /electric vehicle|\bEV\b|charging/i);
  r.framework_specific = isReview && (ptTitle || (b(r.directPT) && evTitle));
  const tempContext = contains(title, /cold climate|cold-weather|temperature|thermal/i) ||
                      contains(abs, /temperature effects|cold climate|cold-weather|thermal/i);
  r.closest_temp = b(r.directPT) && !b(r.heatTarget) && tempContext;

  const verified = r.provenance === 'fresh_web_seed' ? 1 : 0;
  const targeted = r.provenance === 'targeted_heat_resilience_audit' ? 1 : 0;
  r.role_review = 20*num(r.scope5)+20*num(r.coupling5)+15*num(r.state_time5)+15*num(r.method5)+15*num(r.evidence5)+15*num(r.service5)+45*verified;
  r.role_heat = 28*num(r.physics5)+18*num(r.evidence5)+16*num(r.state_time5)+12*num(r.service5)+12*num(r.method5)+8*num(r.scope5)+6*num(r.coupling5)+35*verified+15*targeted;
  r.role_core = 22*num(r.coupling5)+20*num(r.state_time5)+18*num(r.service5)+14*num(r.scope5)+12*num(r.method5)+8*num(r.evidence5)+6*num(r.intervention5)+35*verified;
  r.role_temp = 22*num(r.physics5)+20*num(r.scope5)+18*num(r.state_time5)+15*num(r.coupling5)+15*num(r.method5)+10*num(r.evidence5)+40*verified;
  r.role_service = 26*num(r.service5)+24*num(r.intervention5)+14*num(r.state_time5)+12*num(r.scope5)+10*num(r.coupling5)+8*num(r.method5)+6*num(r.evidence5);
  r.role_transfer = 24*num(r.state_time5)+22*num(r.coupling5)+20*num(r.service5)+14*num(r.method5)+12*num(r.evidence5)+8*num(r.scope5);
}

const selected = [];
const selectedKeys = new Set();
const anchorRoles = new Map([
  ['10.1049/enc2.12034', 'FRAMEWORK_REVIEW'],
  ['10.1016/j.ress.2025.112005', 'CORE_PT_DYNAMIC'],
  ['10.1016/j.apenergy.2025.126806', 'CLOSEST_TEMP_PT'],
  ['10.1016/j.ecmx.2026.101960', 'HEAT_PHYSICS'],
  ['10.1016/j.apenergy.2024.125051', 'HEAT_PHYSICS']
]);
const roleScore = {
  FRAMEWORK_REVIEW: 'role_review', HEAT_PHYSICS: 'role_heat',
  CLOSEST_TEMP_PT: 'role_temp', CORE_PT_DYNAMIC: 'role_core',
  SERVICE_CONTROL: 'role_service', TRANSFER_DYNAMIC: 'role_transfer'
};

function normDoi(x) { return String(x || '').trim().toLowerCase().replace(/^https?:\/\/(dx\.)?doi\.org\//,'').replace(/^doi:/,''); }
function keyOf(r) { return String(r.dedup_key || (normDoi(r.DOI) ? 'doi:'+normDoi(r.DOI) : 'title:'+String(r.title_norm || r.Title || '').toLowerCase())); }
function add(r, role, scorecol, anchor=false) {
  const key = keyOf(r);
  if (selectedKeys.has(key)) return false;
  selected.push({...r, evidence_role: role, role_score: num(r[scorecol]), anchor_comparator: anchor});
  selectedKeys.add(key); return true;
}

for (const [doi, role] of anchorRoles.entries()) {
  const r = rows.find(x => normDoi(x.DOI) === doi);
  if (!r) throw new Error(`Mandatory anchor missing from 200-paper input: ${doi}`);
  add(r, role, roleScore[role], true);
}

function sortPool(pool, scorecol) {
  return pool.sort((a,b) => num(b[scorecol]) - num(a[scorecol]) || num(b.rigor_score) - num(a.rigor_score) || num(b.coverage_dims) - num(a.coverage_dims));
}
function take(role, total, predicate, scorecol) {
  const already = selected.filter(x => x.evidence_role === role).length;
  const need = Math.max(0, total - already);
  if (!need) return;
  let got = 0;
  for (const r of sortPool(rows.filter(predicate), scorecol)) {
    if (add(r, role, scorecol, false)) {
      got++;
      if (got >= need) break;
    }
  }
  if (got < need) throw new Error(`Could select only ${got}/${need} remaining for ${role}`);
}

take('FRAMEWORK_REVIEW', 3, r => b(r.framework_specific), 'role_review');
take('HEAT_PHYSICS', 8, r => b(r.heatTarget), 'role_heat');
take('CLOSEST_TEMP_PT', 2, r => b(r.closest_temp), 'role_temp');
take('CORE_PT_DYNAMIC', 8, r => b(r.directPT) && (b(r.fD)||b(r.fR)) && !b(r.framework_specific) && !b(r.heatTarget) && !b(r.closest_temp), 'role_core');
take('SERVICE_CONTROL', 3, r => b(r.directPT) && b(r.serviceControl) && !b(r.framework_specific) && !b(r.heatTarget), 'role_service');
take('TRANSFER_DYNAMIC', 2, r => b(r.dynamicInfra) && !b(r.directPT), 'role_transfer');

selected.sort((a,b) => num(b.rigor_score) - num(a.rigor_score) || num(b.coverage_dims) - num(a.coverage_dims));
selected.forEach((r,i)=> r.priority_rank = i+1);
if (selected.length !== 26) throw new Error(`Expected 26, got ${selected.length}`);

const cols = ['priority_rank','evidence_role','Title','Year','DOI','Authors','Source','Document_Type','provenance','Source_URL','rigor_score','coverage_dims','scope5','physics5','state_time5','coupling5','service5','intervention5','method5','evidence5','anchor_comparator'];
function csvCell(v) {
  if (v === null || v === undefined) return '';
  const s = String(v);
  return /[",\n\r]/.test(s) ? '"'+s.replace(/"/g,'""')+'"' : s;
}
const csv = [cols.join(','), ...selected.map(r => cols.map(c => csvCell(r[c])).join(','))].join('\n')+'\n';
fs.writeFileSync(OUT_CSV, csv, 'utf8');
fs.writeFileSync(OUT_JSON, JSON.stringify(selected.map(r => Object.fromEntries(cols.map(c=>[c,r[c]]))), null, 2), 'utf8');

const counts = {};
for (const r of selected) counts[r.evidence_role] = (counts[r.evidence_role] || 0) + 1;
console.log(JSON.stringify({screened: rows.length, selected: selected.length, role_counts: counts, out_csv: OUT_CSV}, null, 2));
console.log('\nTOP 26');
for (const r of selected) console.log(`${String(r.priority_rank).padStart(2,'0')}. [${r.evidence_role}] ${r.Title} (${r.Year}) — ${num(r.rigor_score).toFixed(1)}`);