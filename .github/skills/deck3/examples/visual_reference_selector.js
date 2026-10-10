#!/usr/bin/env node
"use strict";
// Deck3 160-brief selector. No source asset becomes cleared through ranking.
const fs = require("fs");
function csv(text) {
 const out=[];let row=[],value="",quoted=false;
 for(let i=0;i<text.length;i++){const c=text[i];
  if(c==='"'){if(quoted&&text[i+1]==='"'){value+='"';i++;}else quoted=!quoted;}
  else if(c===','&&!quoted){row.push(value);value="";}
  else if((c==='\n'||c==='\r')&&!quoted){if(c==='\r'&&text[i+1]==='\n')i++;row.push(value);if(row.some(x=>x!==""))out.push(row);row=[];value="";}
  else value+=c;
 }if(quoted)throw Error("Unterminated CSV quote");
 if(value||row.length){row.push(value);out.push(row);}
 const head=out.shift();if(!head)throw Error("Missing CSV header");
 return out.map((r,i)=>{if(r.length!==head.length)throw Error("Invalid CSV columns at record "+(i+1));return Object.fromEntries(head.map((k,j)=>[k,r[j]]));});
}
function validate(samples,sources){
 const errors=[];const srcIds=new Set(sources.map(x=>x.source_id));const ids=new Set();
 if(samples.length!==160)errors.push("expected 160, received "+samples.length);
 if(sources.length!==13)errors.push("expected 13 sources, received "+sources.length);
 for(const r of samples){
  if(ids.has(r.sample_id))errors.push("duplicate "+r.sample_id);ids.add(r.sample_id);
  if(!srcIds.has(r.source_id))errors.push("unresolved "+r.sample_id+" source "+r.source_id);
  if(!["NATIVE_SCHEMATIC","HYBRID_SCENE"].includes(r.mode))errors.push("bad mode "+r.sample_id);
  if(r.reuse_status!=="NOT_CLEARED")errors.push("unexpected rights status "+r.sample_id);
 }
 for(let n=3;n<=12;n++){
  const g=samples.filter(r=>Number(r.slide)===n);
  if(g.length!==16)errors.push("slide "+n+" has "+g.length);
  let concepts={};for(const x of g)(concepts[x.visual_concept]??=[]).push(x.mode);
  if(Object.keys(concepts).length!==8)errors.push("slide "+n+" != 8 concepts");
  for(const [name,modes] of Object.entries(concepts))if(modes.slice().sort().join(",")!=="HYBRID_SCENE,NATIVE_SCHEMATIC")errors.push("slide "+n+" duplicate mode for "+name);
 }
 return errors;
}
const targets={
 3:["AC electrical port","P/T_e physical boundaries","Port measurement V I P Q","Transformer equipment","EVSE equipment"],
 4:["Common ambient forcing","Transformer thermal inertia","EVSE cooling response","Battery thermal balance"],
 5:["P to T_e candidate chain","T_e to P candidate chain","Actual grid-side AC mediation","Shared heat confounding","Operating restriction gate","Service versus charging power"],
 6:["Research gap integration","Transformer ageing evidence","EVSE heat evidence","Service interruption risk"],
 7:["Inquiry stages","RQ1 evidence qualification","RQ2 thermal state model","RQ3 service outcome"],
 8:["Exact objective preservation","Objective-to-output trace","General objective hierarchy"],
 9:["Forty-class boundary map","AC quantities V I P Q","Transformer 633 to 634 candidate","Thermal versus electrical boundaries"],
 10:["Energy conservation control volume","Dynamic vs algebraic states","Discrete operating modes"],
 11:["IEEE 13 B0 unmodified case","B1 documented EVSE modification","Verification validation split","IEEE 123 transfer"],
 12:["Direct sustainability consequence","Required electricity and mobility service","Environmental accounting","Social access implication"]
};
function rank(samples,slide) {
 if(!Number.isInteger(slide)||slide<3||slide>12)throw Error("Slides 1,2,13,14 do not have infographics");
 return samples.filter(x=>+x.slide===slide).map(r=>{
 const concepts=targets[slide]||[],ix=concepts.indexOf(r.visual_concept);
 const relevance=ix<0?12:Math.max(18,30-2*ix);
 const mechanism=ix<0?12:Math.max(17,25-ix);
 const evidence=r.source_id?10:0; // source lead only; NOT source verified
 const economy=r.mode==="NATIVE_SCHEMATIC"?10:7;
 const editability=r.mode==="NATIVE_SCHEMATIC"?10:5;
 const clarity=3;
 const score=relevance+mechanism+evidence+economy+editability+clarity;
 return {...r,score,score_breakdown:{relevance,mechanism,evidence_lead:evidence,economy,editability,clarity},rights_gate:"OPEN_NOT_CLEARED",physics_gate:"OPEN_UNQUALIFIED",approved:false};
 }).sort((a,b)=>b.score-a.score||a.sample_id.localeCompare(b.sample_id));
}
if(require.main===module){
 const [samplesFile,sourcesFile,slideArg]=process.argv.slice(2);
 if(!samplesFile||!sourcesFile){console.error("Usage: node visual_reference_selector.js samples_160.csv sources_13.csv [slide 3..12]");process.exit(2)}
 const samples=csv(fs.readFileSync(samplesFile,"utf8")),sources=csv(fs.readFileSync(sourcesFile,"utf8"));
 const errors=validate(samples,sources);if(errors.length){console.error(JSON.stringify({status:"CATALOG_FAIL",errors},null,2));process.exit(1)}
 const slides=slideArg?[Number(slideArg)]:Array.from({length:10},(_,i)=>i+3);
 console.log(JSON.stringify({status:"CATALOG_STRUCTURAL_PASS_NOT_SCIENCE_APPROVAL",total:samples.length,sources:sources.length,results:slides.map(s=>({slide:s,ranked:rank(samples,s)}))},null,2));
}
module.exports={csv,validate,rank};
