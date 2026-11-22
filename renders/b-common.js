// Gedeelde bouwstenen voor de tool-renders (b-onderhoud, b-weer, b-offerte).
// Alles procedureel: texturen worden in een canvas getekend, er worden geen
// externe beelden geladen. Openen via een kleine lokale server die de map van de
// repo serveert en bij POST / het meegestuurde base64-webp wegschrijft naar
// fotos/renders/<naam>.webp. In de console: await save().
import * as THREE from 'three';
import { EffectComposer } from 'three/addons/postprocessing/EffectComposer.js';
import { RenderPass } from 'three/addons/postprocessing/RenderPass.js';
import { BokehPass } from 'three/addons/postprocessing/BokehPass.js';
import { OutputPass } from 'three/addons/postprocessing/OutputPass.js';

export const W = 1600, H = 1100;

// ---------------------------------------------------------------- ruis
export function hash2(ix, iy, seed) {
  let h = (Math.imul(ix, 374761393) + Math.imul(iy, 668265263) + Math.imul(seed, 1442695041)) | 0;
  h = Math.imul(h ^ (h >>> 13), 1274126177);
  h ^= h >>> 16;
  return (h >>> 0) / 4294967295;
}
export function noise(x, y, seed = 0) {
  const ix = Math.floor(x), iy = Math.floor(y);
  const fx = x - ix, fy = y - iy;
  const ux = fx * fx * (3 - 2 * fx), uy = fy * fy * (3 - 2 * fy);
  const a = hash2(ix, iy, seed), b = hash2(ix + 1, iy, seed);
  const c = hash2(ix, iy + 1, seed), d = hash2(ix + 1, iy + 1, seed);
  return a + (b - a) * ux + (c - a) * uy + (a - b - c + d) * ux * uy;
}
export function fbm(x, y, seed = 0, oct = 5, lac = 2.03, gain = 0.5) {
  let s = 0, amp = 0.5, norm = 0;
  for (let i = 0; i < oct; i++) {
    s += amp * noise(x, y, seed + i * 17);
    norm += amp; x *= lac; y *= lac; amp *= gain;
  }
  return s / norm;
}
// Voronoi: geeft [F1, F2, celId]
export function voronoi(x, y, seed = 0) {
  const ix = Math.floor(x), iy = Math.floor(y);
  let f1 = 9, f2 = 9, id = 0;
  for (let j = -1; j <= 1; j++) for (let i = -1; i <= 1; i++) {
    const cx = ix + i, cy = iy + j;
    const px = cx + hash2(cx, cy, seed), py = cy + hash2(cx, cy, seed + 7);
    const d = Math.hypot(px - x, py - y);
    if (d < f1) { f2 = f1; f1 = d; id = hash2(cx, cy, seed + 13); } else if (d < f2) { f2 = d; }
  }
  return [f1, f2, id];
}
export const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
export const mix = (a, b, t) => a + (b - a) * t;
export const smooth = (a, b, x) => { const t = clamp((x - a) / (b - a)); return t * t * (3 - 2 * t); };
export function hex(c) { const n = parseInt(c.slice(1), 16); return [(n >> 16) & 255, (n >> 8) & 255, n & 255]; }
export const mix3 = (a, b, t) => [mix(a[0], b[0], t), mix(a[1], b[1], t), mix(a[2], b[2], t)];

// ---------------------------------------------------------------- texturen
export class Layer {
  constructor(w, h) {
    this.w = w; this.h = h;
    this.col = new Uint8ClampedArray(w * h * 4);
    this.height = new Float32Array(w * h);
    this.rough = new Uint8ClampedArray(w * h * 4);
  }
  set(i, rgb, hgt, r) {
    const k = i * 4;
    this.col[k] = rgb[0]; this.col[k + 1] = rgb[1]; this.col[k + 2] = rgb[2]; this.col[k + 3] = 255;
    this.height[i] = hgt;
    const rv = clamp(r) * 255;
    this.rough[k] = rv; this.rough[k + 1] = rv; this.rough[k + 2] = rv; this.rough[k + 3] = 255;
  }
  // per pixel callback(u, v, i) met u,v in 0..1
  fill(fn) {
    const { w, h } = this;
    for (let y = 0; y < h; y++) for (let x = 0; x < w; x++) fn((x + 0.5) / w, (y + 0.5) / h, y * w + x);
    return this;
  }
  toTextures(normalStrength = 2, opts = {}) {
    const map = canvasTex(this.w, this.h, this.col, true);
    const roughnessMap = canvasTex(this.w, this.h, this.rough, false);
    const normalMap = canvasTex(this.w, this.h, heightToNormal(this.height, this.w, this.h, normalStrength, opts.wrap), false);
    for (const t of [map, roughnessMap, normalMap]) {
      t.anisotropy = 16;
      if (opts.repeat) { t.wrapS = t.wrapT = THREE.RepeatWrapping; t.repeat.set(opts.repeat[0], opts.repeat[1]); }
    }
    return { map, roughnessMap, normalMap };
  }
}
export function canvasTex(w, h, data, srgb) {
  const c = document.createElement('canvas'); c.width = w; c.height = h;
  c.getContext('2d').putImageData(new ImageData(data, w, h), 0, 0);
  const t = new THREE.CanvasTexture(c);
  if (srgb) t.colorSpace = THREE.SRGBColorSpace;
  return t;
}
export function heightToNormal(hgt, w, h, strength, wrap = false) {
  const out = new Uint8ClampedArray(w * h * 4);
  const at = (x, y) => {
    if (wrap) { x = (x + w) % w; y = (y + h) % h; } else { x = clamp(x, 0, w - 1); y = clamp(y, 0, h - 1); }
    return hgt[y * w + x];
  };
  for (let y = 0; y < h; y++) for (let x = 0; x < w; x++) {
    const dx = (at(x + 1, y - 1) + 2 * at(x + 1, y) + at(x + 1, y + 1)) - (at(x - 1, y - 1) + 2 * at(x - 1, y) + at(x - 1, y + 1));
    const dy = (at(x - 1, y + 1) + 2 * at(x, y + 1) + at(x + 1, y + 1)) - (at(x - 1, y - 1) + 2 * at(x, y - 1) + at(x + 1, y - 1));
    let nx = -dx * strength, ny = dy * strength, nz = 1;
    const l = Math.hypot(nx, ny, nz); nx /= l; ny /= l; nz /= l;
    const k = (y * w + x) * 4;
    out[k] = (nx * 0.5 + 0.5) * 255; out[k + 1] = (ny * 0.5 + 0.5) * 255; out[k + 2] = (nz * 0.5 + 0.5) * 255; out[k + 3] = 255;
  }
  return out;
}

// Baksteen in halfsteensverband, waalformaat. Maten in meters.
export function brickLayer({ widthM = 2, heightM = 1.5, px = 2048, seed = 3, palette } = {}) {
  const w = px, h = Math.round(px * heightM / widthM);
  const L = new Layer(w, h);
  const bw = 0.21, bh = 0.05, jv = 0.010, jh = 0.012;
  const cw = bw + jv, ch = bh + jh;
  const pal = (palette || ['#7f3a2b', '#8c4433', '#73372a', '#93503b', '#7b4031', '#683027', '#9a5a40', '#86493a', '#57302a', '#8f5a45']).map(hex);
  const mortar = hex('#bdb6aa');
  L.fill((u, v, i) => {
    const X = u * widthM, Y = v * heightM;
    const row = Math.floor(Y / ch);
    const off = (row % 2) * cw * 0.5;
    const col = Math.floor((X + off) / cw);
    const lx = (X + off) - col * cw, ly = Y - row * ch;
    const r = hash2(col, row, seed);
    const base = pal[Math.floor(r * pal.length)];
    const tone = 0.85 + 0.3 * hash2(col, row, seed + 5);
    // afstand tot rand van de steen
    const ex = Math.min(lx, bw - lx), ey = Math.min(ly, bh - ly);
    const inBrick = lx < bw && ly < bh;
    const n1 = fbm(X * 60, Y * 60, seed + 11, 4);
    const n2 = noise(X * 400, Y * 400, seed + 23);
    if (inBrick) {
      const edge = Math.min(ex, ey);
      const bevel = smooth(0, 0.0025 + 0.002 * n1, edge);
      // lichte vlammen/branding per steen
      const flame = fbm(X * 9 + r * 50, Y * 30, seed + 31, 3);
      let c = base.map(x => x * tone * (0.82 + 0.35 * n1) * (0.9 + 0.2 * flame));
      c = mix3(c, [c[0] * 0.55, c[1] * 0.5, c[2] * 0.5], smooth(0.62, 0.9, flame) * 0.6);
      if (n2 > 0.975) c = c.map(x => x * 0.75); // putjes
      if (n2 < 0.04) c = mix3(c, [210, 190, 170], 0.4); // zandkorrels
      const hgt = 0.55 + 0.25 * bevel + 0.12 * n1 + 0.06 * n2 - (n2 > 0.975 ? 0.15 : 0);
      L.set(i, c, hgt, 0.82 + 0.12 * n1);
    } else {
      const c = mortar.map(x => x * (0.86 + 0.22 * n1 + 0.08 * (n2 - 0.5)));
      L.set(i, c, 0.12 + 0.12 * n1 + 0.05 * n2, 0.95);
    }
  });
  return L;
}

// Lucht met stapelwolken als vlak plaatje (voor een achtergrondvlak)
export function skyCanvas({ w = 2048, h = 1024, seed = 5, cloudCover = 0.5, sunU = 0.15, sunV = 0.1, scaleX = 6, scaleY = 9 } = {}) {
  const c = document.createElement('canvas'); c.width = w; c.height = h;
  const g = c.getContext('2d'); const img = g.createImageData(w, h); const d = img.data;
  const top = hex('#5c9ad6'), hor = hex('#cfe3f2');
  for (let y = 0; y < h; y++) for (let x = 0; x < w; x++) {
    const u = x / w, v = y / h;
    let col = mix3(top, hor, Math.pow(v, 1.4));
    // zonnegloed
    const ds = Math.hypot((u - sunU) * 2, v - sunV);
    col = mix3(col, [255, 248, 230], Math.exp(-ds * 3.5) * 0.55);
    // wolken: verticaal samengedrukt, platte onderkant
    const sx = u * scaleX, sy = v * scaleY;
    // stapelwolken: grote bollen (lage frequentie) met bolle randen, platte onderkant
    const field = (X, Y) => {
      const big = fbm(X * 0.55, Y * 0.7, seed + 40, 4);
      const puff = fbm(X * 1.9, Y * 2.2, seed, 5);
      return big * 0.85 + puff * 0.28 - (1 - cloudCover) * 0.75 - 0.06;
    };
    const shape = field(sx, sy) - 0.12 * smooth(0.6, 1.0, v);
    const dens = smooth(0.0, 0.045, shape);
    if (dens > 0) {
      // licht van linksboven: vergelijk met de dichtheid een stukje richting de zon
      const toward = field(sx - 0.06, sy - 0.06);
      const lit = clamp(0.7 + (shape - toward) * 7);
      const core = smooth(0.0, 0.25, shape);
      let cc = mix3([236, 239, 244], [255, 253, 248], lit);
      cc = mix3(cc, [176, 186, 202], core * (1 - lit) * 0.9);
      col = mix3(col, cc, dens);
    }
    const k = (y * w + x) * 4; d[k] = col[0]; d[k + 1] = col[1]; d[k + 2] = col[2]; d[k + 3] = 255;
  }
  g.putImageData(img, 0, 0);
  return c;
}

// Equirect omgeving voor reflecties: lucht, zon linksboven, warme grond.
export function outdoorEnv(renderer, { sunAz = -0.6, sunEl = 0.75, ground = '#8a7a64', brightness = 1, street = false, tint = [1, 1, 1] } = {}) {
  const w = 1024, h = 512;
  const c = document.createElement('canvas'); c.width = w; c.height = h;
  const g = c.getContext('2d'); const img = g.createImageData(w, h); const d = img.data;
  const sx = Math.cos(sunEl) * Math.sin(sunAz), sy = Math.sin(sunEl), sz = Math.cos(sunEl) * Math.cos(sunAz);
  const gr = hex(ground);
  for (let y = 0; y < h; y++) for (let x = 0; x < w; x++) {
    const phi = (x / w) * Math.PI * 2 - Math.PI, th = (0.5 - y / h) * Math.PI;
    const dx = Math.cos(th) * Math.sin(phi), dy = Math.sin(th), dz = Math.cos(th) * Math.cos(phi);
    let col;
    col = mix3(hex('#d8e8f4'), hex('#6fa6dc'), Math.pow(clamp(dy), 0.6));
    const cl = smooth(0.5, 0.75, fbm(phi * 3, th * 8, 9, 5)) * smooth(0, 0.3, dy);
    col = mix3(col, [245, 245, 248], cl * 0.8);
    // zachte overgang naar de grond
    col = mix3(col, mix3(hex('#b9ab95'), gr, smooth(0, 0.3, -dy)), smooth(0.03, -0.03, dy));
    if (street) {
      // huizen aan de overkant: bakstenen band met witte kozijnen en daken
      const roof = 0.12 + 0.1 * Math.abs(Math.sin(phi * 3.0)) + 0.03 * Math.sign(Math.sin(phi * 7));
      if (dy > -0.05 && dy < roof) {
        const bx = Math.floor(phi * 10), win = (Math.abs(((phi * 10) % 1 + 1) % 1 - 0.5) < 0.22) && dy > 0.01 && dy < roof - 0.03;
        let fc = mix3(hex('#8a4a38'), hex('#6e3b30'), hash2(bx, 1, 4));
        if (dy > roof - 0.03) fc = hex('#3d3c3e');
        if (win) fc = Math.abs(((phi * 10) % 1 + 1) % 1 - 0.5) > 0.19 ? hex('#efefea') : hex('#5b6670');
        col = mix3(col, fc, 0.9);
      }
    }
    const dot = dx * sx + dy * sy + dz * sz;
    col = mix3(col, [255, 250, 235], Math.pow(Math.max(0, dot), 200));
    col = col.map((v, k) => Math.min(255, v * brightness * tint[k]));
    const k = (y * w + x) * 4; d[k] = col[0]; d[k + 1] = col[1]; d[k + 2] = col[2]; d[k + 3] = 255;
  }
  g.putImageData(img, 0, 0);
  const t = new THREE.CanvasTexture(c);
  t.mapping = THREE.EquirectangularReflectionMapping; t.colorSpace = THREE.SRGBColorSpace;
  const pm = new THREE.PMREMGenerator(renderer);
  const env = pm.fromEquirectangular(t).texture;
  return { env, equirect: t };
}

// UV's opnieuw zetten vanuit (wereld)posities en normalen
export function remapUV(geom, fn) {
  const g = geom.index ? geom.toNonIndexed() : geom;
  g.computeVertexNormals();
  const p = g.attributes.position, n = g.attributes.normal;
  const uv = new Float32Array(p.count * 2);
  const P = new THREE.Vector3(), N = new THREE.Vector3();
  for (let i = 0; i < p.count; i++) {
    P.fromBufferAttribute(p, i); N.fromBufferAttribute(n, i);
    const [u, v] = fn(P, N);
    uv[i * 2] = u; uv[i * 2 + 1] = v;
  }
  g.setAttribute('uv', new THREE.BufferAttribute(uv, 2));
  return g;
}

// ---------------------------------------------------------------- renderer
export function makeRenderer({ exposure = 1 } = {}) {
  const renderer = new THREE.WebGLRenderer({ antialias: true, preserveDrawingBuffer: true });
  renderer.setPixelRatio(1);
  renderer.setSize(W, H, false);
  renderer.domElement.style.width = '100%';
  renderer.domElement.style.height = 'auto';
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = exposure;
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  document.body.appendChild(renderer.domElement);
  return renderer;
}

// Composer met MSAA en optioneel scherptediepte (bokeh)
export function makeComposer(renderer, scene, camera, bokeh) {
  const rt = new THREE.WebGLRenderTarget(W, H, { type: THREE.HalfFloatType, samples: 4 });
  const composer = new EffectComposer(renderer, rt);
  composer.setPixelRatio(1);
  composer.setSize(W, H);
  composer.addPass(new RenderPass(scene, camera));
  let bokehPass = null;
  if (bokeh) {
    bokehPass = new BokehPass(scene, camera, { focus: bokeh.focus, aperture: bokeh.aperture, maxblur: bokeh.maxblur });
    composer.addPass(bokehPass);
  }
  composer.addPass(new OutputPass());
  return { composer, bokehPass };
}

// Een zachte, warme zon linksboven
export function addSun(scene, { pos = [-4, 6, 4], target = [0, 0, 0], intensity = 3, color = '#ffe3bd', size = 2, mapSize = 4096, near = 0.1, far = 30 } = {}) {
  const sun = new THREE.DirectionalLight(color, intensity);
  sun.position.set(...pos); sun.target.position.set(...target);
  sun.castShadow = true;
  sun.shadow.mapSize.set(mapSize, mapSize);
  const cam = sun.shadow.camera;
  cam.left = -size; cam.right = size; cam.top = size; cam.bottom = -size; cam.near = near; cam.far = far;
  sun.shadow.bias = -0.0002; sun.shadow.normalBias = 0.002;
  scene.add(sun, sun.target);
  return sun;
}

// ---------------------------------------------------------------- opslaan
async function post(name, data) {
  const r = await fetch('/', { method: 'POST', body: JSON.stringify({ name, data }) });
  return r.text();
}
function encode(c, maxBytes = 180000) {
  let q = 0.85, url;
  for (;;) {
    url = c.toDataURL('image/webp', q);
    if (url.length * 0.75 <= maxBytes || q <= 0.5) break;
    q -= 0.05;
  }
  return { url, q: Math.round(q * 100) / 100 };
}
export async function saveAll(srcCanvas, base) {
  const out = [];
  let prev = srcCanvas;
  for (const [w, h] of [[1600, 1100], [800, 550], [400, 275]]) {
    const c = document.createElement('canvas'); c.width = w; c.height = h;
    const g = c.getContext('2d'); g.imageSmoothingEnabled = true; g.imageSmoothingQuality = 'high';
    g.drawImage(prev, 0, 0, w, h);
    const { url, q } = encode(c);
    const size = await post(`${base}-${w}.webp`, url);
    out.push(`${base}-${w}.webp q=${q} ${size}B`);
    prev = c;
  }
  return out.join('\n');
}
