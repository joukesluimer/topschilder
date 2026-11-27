// Meet FCP, LCP, CLS, TBT en bytes per pagina met headless Chrome (mobiel, Slow-4G-achtig, CPU 4x).
import { spawn } from "node:child_process";
const base = process.argv[2], paths = process.argv.slice(3);
const CH = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const port = 9333;
const ch = spawn(CH, ["--headless=new", `--remote-debugging-port=${port}`, "--no-first-run", "--disable-extensions",
  `--user-data-dir=${process.env.TMPDIR}/perfprof${Date.now()}`, "about:blank"], { stdio: "ignore" });
const sleep = ms => new Promise(r => setTimeout(r, ms));
let ver;
for (let i = 0; i < 50; i++) { try { ver = await (await fetch(`http://127.0.0.1:${port}/json/list`)).json(); break; } catch { await sleep(200); } }
const tgt = ver.find(t => t.type === "page");
const ws = new WebSocket(tgt.webSocketDebuggerUrl);
await new Promise(r => ws.onopen = r);
let id = 0; const pend = new Map(); const evs = [];
ws.onmessage = m => { const d = JSON.parse(m.data); if (d.id && pend.has(d.id)) { pend.get(d.id)(d); pend.delete(d.id); } else evs.push(d); };
const send = (method, params = {}) => new Promise(r => { const i = ++id; pend.set(i, r); ws.send(JSON.stringify({ id: i, method, params })); });
await send("Page.enable"); await send("Network.enable"); await send("Runtime.enable");
await send("Network.setCacheDisabled", { cacheDisabled: true });
await send("Emulation.setDeviceMetricsOverride", { width: +(process.env.W||1350), height: 940, deviceScaleFactor: 1, mobile: false });
await send("Emulation.setCPUThrottlingRate", { rate: 1 });
await send("Network.emulateNetworkConditions", { offline: false, latency: 40, downloadThroughput: 10e6 / 8, uploadThroughput: 750e3 / 8 });
await send("Page.addScriptToEvaluateOnNewDocument", { source: `
 window.__m={lcp:0,cls:0,tbt:0,lcpEl:''};
 new PerformanceObserver(l=>{for(const e of l.getEntries()){window.__m.lcp=e.startTime;window.__m.lcpEl=(e.element&&(e.element.tagName+' '+(e.element.currentSrc||e.element.className||'')).slice(0,90))||''}}).observe({type:'largest-contentful-paint',buffered:true});
 new PerformanceObserver(l=>{for(const e of l.getEntries()) if(!e.hadRecentInput) window.__m.cls+=e.value}).observe({type:'layout-shift',buffered:true});
 new PerformanceObserver(l=>{for(const e of l.getEntries()) window.__m.tbt+=Math.max(0,e.duration-50)}).observe({type:'longtask',buffered:true});` });
const rows = [];
for (const p of paths) {
  evs.length = 0;
  await send("Page.navigate", { url: base + p });
  for (let i = 0; i < 200 && !evs.some(e => e.method === "Page.loadEventFired"); i++) await sleep(100);
  await sleep(3000);
  const bytes = evs.filter(e => e.method === "Network.loadingFinished").reduce((s, e) => s + e.params.encodedDataLength, 0);
  const nreq = evs.filter(e => e.method === "Network.requestWillBeSent").length;
  const r = await send("Runtime.evaluate", { returnByValue: true, expression: `(()=>{const n=performance.getEntriesByType('navigation')[0];const f=performance.getEntriesByName('first-contentful-paint')[0];return {fcp:f?f.startTime:0,load:n.loadEventEnd,...window.__m,x:${process.env.EXPR||'0'}}})()` });
  const v = r.result.result.value;
  rows.push({ p, fcp: Math.round(v.fcp), lcp: Math.round(v.lcp), cls: +v.cls.toFixed(3), tbt: Math.round(v.tbt), load: Math.round(v.load), kB: Math.round(bytes / 1024), req: nreq, lcpEl: v.lcpEl, x: v.x });
}
console.table(rows);
console.log(JSON.stringify(rows));
ws.close(); ch.kill();
