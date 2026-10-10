#!/usr/bin/env node
"use strict";
const assert=require("assert");
const {csv,validate,rank}=require("./visual_reference_selector.js");
const quote=x=>'"'+String(x).replace(/"/g,'""')+'"';
const sourceRows=Array.from({length:13},(_,i)=>({source_id:'S'+i}));
const names={3:["Feeder topology","Transformer equipment","AC electrical port","EVSE equipment","Vehicle charging connection","P/T_e physical boundaries","Electrical load feedback","Port measurement V I P Q"],4:["Common ambient forcing","Oil winding thermal response","Transformer thermal inertia","EVSE cooling response","Battery thermal balance","Conductor weather inputs","Exposure history and duration","Physical control volume boundaries"],5:["P to T_e candidate chain","T_e to P candidate chain","Actual grid-side AC mediation","Shared heat confounding","Operating restriction gate","Service versus charging power","Conditional counterfactual","Supported direction classification"]};
const samples=[];let j=1;
for(let n=3;n<=12;n++)for(let k of (names[n]||Array.from({length:8},(_,i)=>'Unique '+n+' '+i)))for(let mode of ["NATIVE_SCHEMATIC","HYBRID_SCENE"])samples.push({sample_id:'D3-'+String(j++).padStart(3,'0'),slide:String(n),visual_concept:k,mode,source_id:'S0',reuse_status:'NOT_CLEARED'});
assert.strictEqual(samples.length,160);
assert.deepStrictEqual(validate(samples,sourceRows),[]);
const r=rank(samples,5);assert.strictEqual(r.length,16);assert(r.every(x=>x.approved===false));assert(r.every(x=>x.rights_gate==="OPEN_NOT_CLEARED"));
assert(r[0].score>=r[r.length-1].score);
assert.throws(()=>rank(samples,14));
const s='sample_id,visual_concept,mode\n"D3-001","AC, port","HYBRID_SCENE"\n';
assert.strictEqual(csv(s)[0].visual_concept,"AC, port");
const corrupt=samples.map(x=>({...x}));corrupt[0].source_id="UNKNOWN";assert(validate(corrupt,sourceRows).some(x=>x.includes("unresolved")));
console.log("PASS: 160 unique, per-slide candidates, rank, rights fail-closed, quoted CSV, missing-source rejection, invalid-slide rejection");
