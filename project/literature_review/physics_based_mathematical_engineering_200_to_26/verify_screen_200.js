#!/usr/bin/env node
/**
 * Independent JavaScript audit of the 200→26 thesis literature screen.
 * Run: node verify_screen_200.js
 */
const fs = require("fs");

function parseCSV(s) {
  const rows=[]; let row=[], cell="", q=false;
  for (let i=0;i<s.length;i++) {
    const c=s[i], n=s[i+1];
    if (q) {
      if (c === '"' && n === '"') { cell+='"'; i++; }
      else if (c === '"') q=false;
      else cell+=c;
    } else {
      if (c === '"') q=true;
      else if (c === ",") { row.push(cell); cell=""; }
      else if (c === "\n") { row.push(cell.replace(/\r$/,"")); rows.push(row); row=[]; cell=""; }
      else cell+=c;
    }
  }
  if (cell.length || row.length) { row.push(cell); rows.push(row); }
  const h=rows[0];
  return rows.slice(1).filter(r=>r.some(x=>x!=="")).map(r =>
    Object.fromEntries(h.map((k,i)=>[k,r[i]??""]))
  );
}

const corpus = parseCSV(fs.readFileSync("/mnt/data/thesis_screen_200.csv","utf8"));
const shortlist = parseCSV(fs.readFileSync("/mnt/data/thesis_shortlist_26.csv","utf8"));

if (corpus.length !== 200) throw new Error(`Expected 200, got ${corpus.length}`);
if (shortlist.length !== 26) throw new Error(`Expected 26, got ${shortlist.length}`);

const dois = shortlist.map(x => x.DOI.trim().toLowerCase());
if (new Set(dois).size !== 26) throw new Error("Duplicate DOI in shortlist.");

for (const x of shortlist) {
  if (!x.Title || !x.Year || !x.DOI) {
    throw new Error(`Missing key metadata: ${JSON.stringify(x)}`);
  }
}

const roles = {};
for (const x of shortlist) {
  roles[x["Primary evidence role"]] = (roles[x["Primary evidence role"]]||0)+1;
}
for (const r of ["Foundation","Coupled P–T","Heat / physical state","Intervention / recovery"]) {
  if (!roles[r]) throw new Error(`Missing evidence role: ${r}`);
}

console.log("JAVASCRIPT AUDIT PASSED");
console.log("Corpus:", corpus.length);
console.log("Shortlist:", shortlist.length);
console.log("Unique DOIs:", new Set(dois).size);
console.log("Evidence roles:", roles);
