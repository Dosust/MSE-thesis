const COLORS={bg:"#081018",grid:"#22313f",sky:"#87CEFA",deep:"#00BFFF",ink:"#eef8ff",muted:"#91a8b8",danger:"#ff6b7a",white:"#ffffff"};

const $=(id)=>document.getElementById(id);
const canvases={network:$("network"),phase:$("phase"),timeline:$("timeline")};
let data=null,index=0,playing=false,lastFrame=0,accumulator=0;

function ctx2d(canvas){
  const dpr=Math.max(1,Math.min(2,window.devicePixelRatio||1));
  const rect=canvas.getBoundingClientRect();
  const w=Math.max(1,Math.round(rect.width*dpr)),h=Math.max(1,Math.round(rect.width*(canvas.height/canvas.width)*dpr));
  if(canvas.width!==w||canvas.height!==h){canvas.width=w;canvas.height=h}
  const ctx=canvas.getContext("2d");ctx.setTransform(dpr,0,0,dpr,0,0);
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
function clear(ctx,w,h){ctx.clearRect(0,0,w,h);ctx.fillStyle="#081018";ctx.fillRect(0,0,w,h)}

function drawNetwork(s){
  const {ctx,w,h}=ctx2d(canvases.network);clear(ctx,w,h);
  const pad=42,cY=h*.52,pX=w*.23,tX=w*.77,iX=w*.5;
  const hazard=s.hazard;
  ctx.save();ctx.globalAlpha=.07+hazard*.18;ctx.fillStyle=COLORS.deep;ctx.beginPath();ctx.ellipse(w*.5,h*.58,w*.47*(.45+hazard*.55),h*.33*(.45+hazard*.55),0,0,Math.PI*2);ctx.fill();ctx.restore();

  text(ctx,"POWER",pX,34,12,COLORS.sky,"center",800);
  text(ctx,"TRANSPORT",tX,34,12,COLORS.sky,"center",800);
  const powerNodes=[[pX-60,cY-72],[pX+34,cY-72],[pX-60,cY+62],[pX+34,cY+62]];
  const roadNodes=[[tX-52,cY-72],[tX+52,cY-72],[tX-52,cY+62],[tX+52,cY+62]];
  [[0,1],[0,2],[1,3],[2,3]].forEach(([a,b])=>line(ctx,...powerNodes[a],...powerNodes[b],COLORS.grid,4));
  [[0,1],[0,2],[1,3],[2,3],[0,3]].forEach(([a,b])=>line(ctx,...roadNodes[a],...roadNodes[b],COLORS.grid,4));
  const pColor=s.power>=data.constraints.min_power?COLORS.sky:COLORS.danger;
  const tColor=s.transport>=data.constraints.min_transport?COLORS.deep:COLORS.danger;
  powerNodes.forEach(([x,y])=>circle(ctx,x,y,8+8*s.power,pColor,COLORS.white,.8));
  roadNodes.forEach(([x,y])=>circle(ctx,x,y,7+7*s.transport,tColor,COLORS.white,.8));
  const iColor=s.interface>=data.constraints.min_interface?COLORS.sky:COLORS.danger;
  line(ctx,pX+55,cY,iX-24,cY,iColor,2+5*s.interface);
  line(ctx,iX+24,cY,tX-68,cY,iColor,2+5*s.interface);
  circle(ctx,iX,cY,12+16*s.interface,"#0d1821",iColor,3);
  text(ctx,"C_PT",iX,cY+4,11,COLORS.ink,"center",800);
  text(ctx,`P=${s.power.toFixed(3)}`,pX,h-28,12,pColor,"center",700);
  text(ctx,`T=${s.transport.toFixed(3)}`,tX,h-28,12,tColor,"center",700);
  text(ctx,`η=${hazard.toFixed(3)}`,w/2,62,12,COLORS.deep,"center",700);
}

function drawPhase(s){
  const {ctx,w,h}=ctx2d(canvases.phase);clear(ctx,w,h);
  const L=64,R=24,T=30,B=50,pw=w-L-R,ph=h-T-B;
  const x=v=>L+v*pw,y=v=>T+(1-v)*ph;
  for(let g=0;g<=1.0001;g+=.2){line(ctx,x(g),T,x(g),T+ph,COLORS.grid,.7);line(ctx,L,y(g),L+pw,y(g),COLORS.grid,.7)}
  const xp=x(data.constraints.min_power),yt=y(data.constraints.min_transport);
  ctx.save();ctx.fillStyle="rgba(135,206,250,.055)";ctx.fillRect(xp,T,L+pw-xp,yt-T);ctx.strokeStyle=COLORS.sky;ctx.setLineDash([5,5]);ctx.strokeRect(xp,T,L+pw-xp,yt-T);ctx.restore();
  text(ctx,"T",24,h/2,13,COLORS.ink,"center",800);text(ctx,"P",L+pw/2,h-14,13,COLORS.ink,"center",800);
  text(ctx,"declared sustainability thresholds",L+pw-8,T+18,10,COLORS.sky,"right",700);
  ctx.save();ctx.strokeStyle="rgba(135,206,250,.32)";ctx.lineWidth=1.4;ctx.beginPath();
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
  const series=[["power",COLORS.sky],["transport",COLORS.deep],["interface",COLORS.white],["hazard","#5f7d91"]];
  series.forEach(([key,color])=>{ctx.save();ctx.strokeStyle=color;ctx.lineWidth=key==="hazard"?1.2:2;ctx.beginPath();data.samples.forEach((s,i)=>{const xx=x(i),yy=y(s[key]);i?ctx.lineTo(xx,yy):ctx.moveTo(xx,yy)});ctx.stroke();ctx.restore()});
  const bandTop=T+serviceH+34,bandH=h-bandTop-B;
  const minM=Math.min(...data.samples.map(s=>s.margin))-.03,maxM=Math.max(...data.samples.map(s=>s.margin))+.03;
  const ym=m=>bandTop+(maxM-m)/(maxM-minM)*bandH;
  line(ctx,L,ym(0),L+pw,ym(0),COLORS.muted,1,[4,4]);
  ctx.save();ctx.strokeStyle=COLORS.sky;ctx.lineWidth=2;ctx.beginPath();data.samples.forEach((s,i)=>{const xx=x(i),yy=ym(s.margin);i?ctx.lineTo(xx,yy):ctx.moveTo(xx,yy)});ctx.stroke();ctx.restore();
  text(ctx,"margin",L,bandTop-10,10,COLORS.sky);text(ctx,"0",L-8,ym(0)+4,10,COLORS.muted,"right");
  const cx=x(index);line(ctx,cx,T,cx,h-B,COLORS.deep,1.2,[3,4]);
  text(ctx,"P",w-184,18,10,COLORS.sky);text(ctx,"T",w-150,18,10,COLORS.deep);text(ctx,"C_PT",w-110,18,10,COLORS.white);text(ctx,"η",w-52,18,10,"#5f7d91");
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
  const rows=[
    ["Data status",data.status],
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
    if(data.schema_version!=="ive-demo-0.1.0"||!Array.isArray(data.samples)||data.samples.length<2)throw new Error("unexpected data schema");
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
