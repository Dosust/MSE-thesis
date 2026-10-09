const COLORS={bg:"#FFFFFF",grid:"#416985",sky:"#0072B2",deep:"#176B42",ink:"#000000",muted:"#555D66",danger:"#B4232C",white:"#FFFFFF"};

const $=(id)=>document.getElementById(id);
const canvases={network:$("network"),phase:$("phase"),timeline:$("timeline")};
let data=null,index=0,playing=false,lastFrame=0,accumulator=0;

function ctx2d(canvas){
  const dpr=Math.max(1,Math.min(2,window.devicePixelRatio||1));
  const rect=canvas.getBoundingClientRect();
  const w=Math.max(1,Math.round(rect.width*dpr));
  const h=Math.max(1,Math.round(rect.width*(canvas.height/canvas.width)*dpr));
  if(canvas.width!==w||canvas.height!==h){canvas.width=w;canvas.height=h}
  const ctx=canvas.getContext("2d");
  ctx.setTransform(dpr,0,0,dpr,0,0);
  return {ctx,w:rect.width,h:rect.width*(430/(canvas.id==="timeline"?1400:900))};
}
function line(ctx,x1,y1,x2,y2,color=COLORS.grid,width=1,dash=[]){
  ctx.save();ctx.strokeStyle=color;ctx.lineWidth=width;ctx.setLineDash(dash);ctx.beginPath();ctx.moveTo(x1,y1);ctx.lineTo(x2,y2);ctx.stroke();ctx.restore();
}
function text(ctx,s,x,y,size=12,color=COLORS.muted,align="left",weight=500){
  ctx.save();ctx.fillStyle=color;ctx.font=`${weight} ${size}px ui-monospace, SFMono-Regular, Menlo, monospace`;ctx.textAlign=align;ctx.fillText(s,x,y);ctx.restore();
}
function circle(ctx,x,y,r,fill,stroke=null,width=1){
  ctx.beginPath();ctx.arc(x,y,r,0,Math.PI*2);ctx.fillStyle=fill;ctx.fill();if(stroke){ctx.strokeStyle=stroke;ctx.lineWidth=width;ctx.stroke()}
}
function clear(ctx,w,h){ctx.clearRect(0,0,w,h);ctx.fillStyle=COLORS.bg;ctx.fillRect(0,0,w,h)}
function rgba(hex,alpha){
  const n=parseInt(hex.slice(1),16),r=(n>>16)&255,g=(n>>8)&255,b=n&255;
  return `rgba(${r},${g},${b},${alpha})`;
}

function drawNetwork(s){
  const {ctx,w,h}=ctx2d(canvases.network);clear(ctx,w,h);
  const L=42,R=42,T=38,B=38,pw=w-L-R,ph=h-T-B;
  const xy=node=>[L+node.x*pw,T+node.y*ph];
  const nodeById=Object.fromEntries(data.graph.nodes.map(n=>[n.id,n]));
  const gs=s.graph_state;

  text(ctx,"POWER",L+pw*.18,24,11,COLORS.sky,"center",800);
  text(ctx,"TRANSPORT",L+pw*.78,24,11,COLORS.deep,"center",800);
  text(ctx,"graph-driven projection",w-18,24,10,COLORS.muted,"right",600);

  for(const node of data.graph.nodes){
    const [x,y]=xy(node),state=gs.nodes[node.id],hazard=state.hazard;
    if(hazard>0.01){
      /* no decorative hazard halo: encode hazard using labeled outlines */
    }
  }

  for(const edge of data.graph.edges){
    const a=nodeById[edge.source],b=nodeById[edge.target];
    const [x1,y1]=xy(a),[x2,y2]=xy(b);
    const activity=gs.edges[edge.id].activity;
    const color=edge.layer==="power"?COLORS.sky:edge.layer==="transport"?COLORS.deep:COLORS.white;
    const dash=edge.layer==="interface"?[5,5]:[];
    line(ctx,x1,y1,x2,y2,rgba(color,.20+.75*activity),1.2+4.3*activity,dash);
  }

  for(const node of data.graph.nodes){
    const [x,y]=xy(node),state=gs.nodes[node.id];
    const layerColor=node.layer==="power"?COLORS.sky:COLORS.deep;
    const availability=state.availability,hazard=state.hazard;
    const fill=availability<.45?COLORS.danger:layerColor;
    circle(ctx,x,y,7+8*availability,fill,COLORS.white,.7);
    if(hazard>.25) circle(ctx,x,y,12+10*hazard,"rgba(0,0,0,0)",COLORS.danger,1.2);
    text(ctx,node.id,x,y+3,9,COLORS.ink,"center",800);
  }

  const interfaces=data.graph.edges.filter(e=>e.layer==="interface");
  text(ctx,`${data.graph.nodes.length} nodes · ${data.graph.edges.length} edges · ${interfaces.length} interfaces`,w/2,h-16,10,COLORS.muted,"center",650);
}

function drawPhase(s){
  const {ctx,w,h}=ctx2d(canvases.phase);clear(ctx,w,h);
  const L=64,R=24,T=30,B=50,pw=w-L-R,ph=h-T-B;
  const x=v=>L+v*pw,y=v=>T+(1-v)*ph;
  for(let g=0;g<=1.0001;g+=.2){line(ctx,x(g),T,x(g),T+ph,COLORS.grid,.7);line(ctx,L,y(g),L+pw,y(g),COLORS.grid,.7)}
  const xp=x(data.constraints.min_power),yt=y(data.constraints.min_transport);
  ctx.save();ctx.fillStyle=COLORS.white;ctx.fillRect(xp,T,L+pw-xp,yt-T);ctx.strokeStyle=COLORS.sky;ctx.setLineDash([5,5]);ctx.strokeRect(xp,T,L+pw-xp,yt-T);ctx.restore();
  text(ctx,"T",24,h/2,13,COLORS.ink,"center",800);text(ctx,"P",L+pw/2,h-14,13,COLORS.ink,"center",800);
  text(ctx,"declared sustainability thresholds",L+pw-8,T+18,10,COLORS.sky,"right",700);
  ctx.save();ctx.strokeStyle=COLORS.sky;ctx.lineWidth=1.4;ctx.beginPath();
  data.samples.forEach((q,j)=>{const xx=x(q.power),yy=y(q.transport);if(j===0)ctx.moveTo(xx,yy);else ctx.lineTo(xx,yy)});ctx.stroke();ctx.restore();
  ctx.save();ctx.strokeStyle=COLORS.sky;ctx.lineWidth=2.5;ctx.beginPath();
  data.samples.slice(0,index+1).forEach((q,j)=>{const xx=x(q.power),yy=y(q.transport);if(j===0)ctx.moveTo(xx,yy);else ctx.lineTo(xx,yy)});ctx.stroke();ctx.restore();
  const r=7+9*s.interface;circle(ctx,x(s.power),y(s.transport),r,s.margin>=0?COLORS.sky:COLORS.danger,COLORS.white,1);
  text(ctx,`C_PT=${s.interface.toFixed(3)}`,x(s.power),Math.max(18,y(s.transport)-r-10),10,COLORS.ink,"center",700);
}

function drawTimeline(){
  const {ctx,w,h}=ctx2d(canvases.timeline);clear(ctx,w,h);
  const L=58,R=20,T=25,B=38,pw=w-L-R,serviceH=h*.62;
  const x=i=>L+i/(data.samples.length-1)*pw,y=v=>T+(1-v)*serviceH;
  [0,.25,.5,.75,1].forEach(v=>{line(ctx,L,y(v),L+pw,y(v),COLORS.grid,.7);text(ctx,v.toFixed(2),L-8,y(v)+4,10,COLORS.muted,"right")});
  const series=[["power",COLORS.sky],["transport",COLORS.deep],["interface",COLORS.white],["hazard","#555D66"]];
  series.forEach(([key,color])=>{ctx.save();ctx.strokeStyle=color;ctx.lineWidth=key==="hazard"?1.2:2;ctx.beginPath();data.samples.forEach((s,i)=>{const xx=x(i),yy=y(s[key]);i?ctx.lineTo(xx,yy):ctx.moveTo(xx,yy)});ctx.stroke();ctx.restore()});
  const bandTop=T+serviceH+34,bandH=h-bandTop-B;
  const minM=Math.min(...data.samples.map(s=>s.margin))-.03,maxM=Math.max(...data.samples.map(s=>s.margin))+.03;
  const ym=m=>bandTop+(maxM-m)/(maxM-minM)*bandH;
  line(ctx,L,ym(0),L+pw,ym(0),COLORS.muted,1,[4,4]);
  ctx.save();ctx.strokeStyle=COLORS.sky;ctx.lineWidth=2;ctx.beginPath();data.samples.forEach((s,i)=>{const xx=x(i),yy=ym(s.margin);i?ctx.lineTo(xx,yy):ctx.moveTo(xx,yy)});ctx.stroke();ctx.restore();
  text(ctx,"margin",L,bandTop-10,10,COLORS.sky);text(ctx,"0",L-8,ym(0)+4,10,COLORS.muted,"right");
  const cx=x(index);line(ctx,cx,T,cx,h-B,COLORS.deep,1.2,[3,4]);
  text(ctx,"P",w-184,18,10,COLORS.sky);text(ctx,"T",w-150,18,10,COLORS.deep);text(ctx,"C_PT",w-110,18,10,COLORS.white);text(ctx,"η",w-52,18,10,"#555D66");
  text(ctx,"time",L+pw/2,h-10,10,COLORS.muted,"center");
}

function updateDom(s){
  $("clock").value=`t = ${s.time.toFixed(2)}`;
  [["m-hazard",s.hazard],["m-power",s.power],["m-transport",s.transport],["m-interface",s.interface],["m-margin",s.margin]].forEach(([id,v])=>{$(id).textContent=v.toFixed(4);$(id).classList.toggle("negative",id==="m-margin"&&v<0)});
}
function render(){
  const s=data.samples[index];$("time").value=String(index);drawNetwork(s);drawPhase(s);drawTimeline();updateDom(s);
}
function frame(ts){
  if(!playing)return;
  if(!lastFrame)lastFrame=ts;
  accumulator+=ts-lastFrame;lastFrame=ts;
  const interval=120/Number($("speed").value);
  while(accumulator>=interval){accumulator-=interval;index=(index+1)%data.samples.length}
  render();requestAnimationFrame(frame);
}
function setPlaying(next){
  playing=next;$("play").textContent=playing?"Pause":"Play";lastFrame=0;accumulator=0;if(playing)requestAnimationFrame(frame);
}
function buildQA(){
  const qa=$("qa"),rmse=data.ml_surrogate.holdout_rmse;
  const interfaces=data.graph.edges.filter(e=>e.layer==="interface").length;
  const rows=[
    ["Data status",data.status],
    ["Graph",`${data.graph.nodes.length} nodes / ${data.graph.edges.length} edges / ${interfaces} interfaces`],
    ["ML scope",data.ml_surrogate.status],
    ["RMSE · dP/dt",Number(rmse.power).toExponential(2)],
    ["RMSE · dT/dt",Number(rmse.transport).toExponential(2)],
    ["RMSE · dC/dt",Number(rmse.interface).toExponential(2)],
    ...data.criticality.map(d=>[`Sensitivity · ${d.parameter}`,Number(d.sensitivity).toFixed(5)])
  ];
  qa.replaceChildren(...rows.map(([a,b])=>{const row=document.createElement("div");row.className="qa-row";const x=document.createElement("span"),y=document.createElement("span");x.textContent=a;y.textContent=b;row.append(x,y);return row}));
}
async function init(){
  try{
    const response=await fetch("demo-data.json",{cache:"no-store"});if(!response.ok)throw new Error(`HTTP ${response.status}`);
    data=await response.json();
    if(data.schema_version!=="ive-demo-0.2.0"||!Array.isArray(data.samples)||data.samples.length<2||!data.graph)throw new Error("unexpected data schema");
    $("time").max=String(data.samples.length-1);
    $("status").textContent=`${data.samples.length} samples · ${data.schema_version}`;
    $("fingerprint").textContent=`SHA-256 model record: ${data.sha256_without_hash_field}`;
    buildQA();render();
    if(!matchMedia("(prefers-reduced-motion: reduce)").matches)setPlaying(true);
  }catch(error){$("status").textContent="data load failed";console.error(error)}
}
$("play").addEventListener("click",()=>setPlaying(!playing));
$("time").addEventListener("input",e=>{index=Number(e.target.value);render()});
window.addEventListener("resize",()=>data&&render());
init();
