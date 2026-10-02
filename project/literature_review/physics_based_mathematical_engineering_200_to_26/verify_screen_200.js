#!/usr/bin/env node
/**
 * Independent JavaScript audit of the archived 200 → 26 thesis literature screen.
 *
 * Run from any directory:
 *   node verify_screen_200.js
 */

const fs = require("fs");
const path = require("path");

const ROOT = __dirname;

function parseCSV(s) {
  const rows = [];
  let row = [], cell = "", quoted = false;
  for (let i = 0; i < s.length; i++) {
    const c = s[i], n = s[i + 1];
    if (quoted) {
      if (c === '"' && n === '"') { cell += '"'; i++; }
      else if (c === '"') quoted = false;
      else cell += c;
    } else {
      if (c === '"') quoted = true;
      else if (c === ",") { row.push(cell); cell = ""; }
      else if (c === "\n") {
        row.push(cell.replace(/\r$/, ""));
        rows.push(row);
        row = [];
        cell = "";
      } else cell += c;
    }
  }
  if (cell.length || row.length) {
    row.push(cell);
    rows.push(row);
  }
  const header = rows[0];
  return rows.slice(1)
    .filter(r => r.some(x => x !== ""))
    .map(r => Object.fromEntries(header.map((k, i) => [k, r[i] ?? ""])));
}

const corpusPath = path.join(ROOT, "thesis_screen_200.csv");
const shortlistPath = path.join(ROOT, "thesis_shortlist_26.csv");

const corpus = parseCSV(fs.readFileSync(corpusPath, "utf8"));
const shortlist = parseCSV(fs.readFileSync(shortlistPath, "utf8"));

if (corpus.length !== 200) throw new Error(`Expected 200, got ${corpus.length}`);
if (shortlist.length !== 26) throw new Error(`Expected 26, got ${shortlist.length}`);

const dois = shortlist.map(x => (x.DOI || "").trim().toLowerCase());
if (new Set(dois).size !== 26) throw new Error("Duplicate DOI in shortlist.");

for (const x of shortlist) {
  if (!x.Title || !x.Year || !x.DOI) {
    throw new Error(`Missing key metadata: ${JSON.stringify(x)}`);
  }
}

const roles = {};
for (const x of shortlist) {
  roles[x["Primary evidence role"]] = (roles[x["Primary evidence role"]] || 0) + 1;
}

const expected = {
  "Foundation": 5,
  "Coupled P–T": 9,
  "Heat / physical state": 9,
  "Intervention / recovery": 3,
};

for (const [role, count] of Object.entries(expected)) {
  if (roles[role] !== count) {
    throw new Error(`Evidence-role mismatch for ${role}: expected ${count}, got ${roles[role] || 0}`);
  }
}

console.log("JAVASCRIPT AUDIT PASSED");
console.log("Corpus:", corpus.length);
console.log("Shortlist:", shortlist.length);
console.log("Unique DOIs:", new Set(dois).size);
console.log("Evidence roles:", roles);
console.log("Scientific status: priority full-text set; not a novelty claim.");
