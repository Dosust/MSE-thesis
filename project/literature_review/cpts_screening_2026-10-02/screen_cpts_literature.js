#!/usr/bin/env node
/**
 * Deterministic screening/ranking mirror of the Python pipeline.
 * Usage:
 *   node screen_cpts_literature.js cpts_26_seed.json output.json
 *
 * For a 200-paper run, pass a JSON array of metadata records exported from
 * Crossref/OpenAlex/Scopus/WoS/IEEE (title + abstract strongly recommended).
 */

const fs = require("fs");

const WEIGHTS = {
  rq_fit:20, physics:20, coupling:15, state_time:15,
  service_resilience:10, math_method:10, validation:5, intervention:5
};

const TERMS = {
  power:[/\bpower\b/i,/distribution network/i,/\bgrid\b/i,/transformer/i,/feeder/i,/voltage/i,/optimal power flow/i],
  transport:[/transport/i,/traffic/i,/mobility/i,/route/i,/road network/i,/vehicle/i],
  ev_interface:[/electric vehicle/i,/\bEV\b/i,/charging station/i,/fast charging/i,/charger/i,/vehicle-to-grid/i,/\bV2G\b/i],
  physics:[/thermal/i,/temperature/i,/heat/i,/hottest[- ]spot/i,/state of charge/i,/\bSOC\b/i,/power flow/i,/energy consumption/i,/queue/i],
  dynamic:[/dynamic/i,/time[- ]vary/i,/temporal/i,/spatiotemporal/i,/trajectory/i,/state[- ]dependent/i,/multi[- ]period/i,/real[- ]time/i],
  resilience:[/resilien/i,/recovery/i,/restoration/i,/service disruption/i,/cascad/i,/hazard/i,/failure/i],
  intervention:[/control/i,/optim/i,/dispatch/i,/schedul/i,/routing/i,/pricing/i,/reinforcement learning/i,/model predictive/i],
  validation:[/case study/i,/real[- ]world/i,/field/i,/experiment/i,/validated/i,/benchmark/i,/sensitivity analysis/i,/IEEE \d+/i]
};

const txt = r => `${r.title||""} ${r.abstract||""} ${r.keywords||""}`.toLowerCase();
const has = (t, family) => TERMS[family].some(re => re.test(t));
const grade = (t, family) => {
  const n = TERMS[family].reduce((s,re)=>s+(re.test(t)?1:0),0);
  return n===0?0:n===1?1:n===2?2:n<=4?3:4;
};

function score(r) {
  const t = txt(r);
  const p=has(t,"power"), tr=has(t,"transport"), ev=has(t,"ev_interface");
  const dyn=has(t,"dynamic"), res=has(t,"resilience"), phys=has(t,"physics");
  const grades = {
    rq_fit:(p&&tr&&ev&&(dyn||res||phys))?4:(ev&&phys&&(p||tr))?3:1,
    physics:grade(t,"physics"),
    coupling:(p&&tr&&ev)?4:(ev&&p)?3:(ev&&tr)?2:0,
    state_time:grade(t,"dynamic"),
    service_resilience:grade(t,"resilience"),
    math_method:Math.min(4,[
      /optimization/i,/stochastic/i,/markov/i,/equilibrium/i,/mixed[- ]integer/i,
      /monte carlo/i,/reinforcement learning/i,/queue/i,/power flow/i
    ].reduce((s,re)=>s+(re.test(t)?1:0),0)),
    validation:grade(t,"validation"),
    intervention:grade(t,"intervention")
  };
  let total=0;
  for (const k of Object.keys(WEIGHTS)) total += (grades[k]/4)*WEIGHTS[k];
  return {score:Math.round(total*100)/100, grades};
}

function main() {
  const input = process.argv[2];
  const output = process.argv[3] || "js_ranked.json";
  if (!input) throw new Error("Usage: node screen_cpts_literature.js INPUT.json OUTPUT.json");
  const rows = JSON.parse(fs.readFileSync(input,"utf8"));
  const ranked = rows.map(r => {
    // Seed records may already contain human-audited 0–4 grades. Preserve them if present.
    const humanKeys=["rq_fit","physics","coupling","state_time","service_resilience","math_method","validation_score","intervention"];
    const hasHuman = humanKeys.every(k => Number.isFinite(Number(r[k])));
    if (hasHuman) {
      const g = {
        rq_fit:Number(r.rq_fit), physics:Number(r.physics), coupling:Number(r.coupling),
        state_time:Number(r.state_time), service_resilience:Number(r.service_resilience),
        math_method:Number(r.math_method), validation:Number(r.validation_score),
        intervention:Number(r.intervention)
      };
      let total=0; for (const k of Object.keys(WEIGHTS)) total += (g[k]/4)*WEIGHTS[k];
      return {...r, js_score:Math.round(total*10)/10};
    }
    const s=score(r); return {...r, js_score:s.score, js_grades:s.grades};
  }).sort((a,b)=>b.js_score-a.js_score);
  fs.writeFileSync(output, JSON.stringify(ranked,null,2));
  console.log(JSON.stringify({input_records:rows.length, output_records:ranked.length, top_score:ranked[0]?.js_score},null,2));
}
main();