// Gedeelde bouwstenen voor de tool-renders (huiscalculator, kleurenkiezer, inspiratie).
// three.js r160, alles procedureel: texturen worden in een canvas getekend.
import * as THREE from 'three';
import { mergeVertices } from 'three/addons/utils/BufferGeometryUtils.js';

export { THREE };

/* ------------------------------------------------------------------ */
/* Hulpjes                                                              */
/* ------------------------------------------------------------------ */

export function rng(seed) {
  let a = seed >>> 0;
  return () => {
    a |= 0; a = (a + 0x6d2b79f5) | 0;
    let t = Math.imul(a ^ (a >>> 15), 1 | a);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

function hash3(x, y, z) {
  let h = x * 374761393 + y * 668265263 + z * 2147483647;
  h = (h ^ (h >>> 13)) * 1274126177;
  return ((h ^ (h >>> 16)) >>> 0) / 4294967296;
}

export function noise3(x, y, z) {
  const xi = Math.floor(x), yi = Math.floor(y), zi = Math.floor(z);
  const xf = x - xi, yf = y - yi, zf = z - zi;
  const s = (t) => t * t * (3 - 2 * t);
  const u = s(xf), v = s(yf), w = s(zf);
  let r = 0;
  for (let dx = 0; dx < 2; dx++) for (let dy = 0; dy < 2; dy++) for (let dz = 0; dz < 2; dz++) {
    const wt = (dx ? u : 1 - u) * (dy ? v : 1 - v) * (dz ? w : 1 - w);
    r += wt * hash3(xi + dx, yi + dy, zi + dz);
  }
  return r;
}

export function fbm(x, y, z, oct = 4) {
  let a = 0.5, f = 1, r = 0;
  for (let i = 0; i < oct; i++) { r += a * noise3(x * f, y * f, z * f); f *= 2.03; a *= 0.5; }
  return r;
}

function canvas(w, h) {
  const c = document.createElement('canvas');
  c.width = w; c.height = h;
  return c;
}

let MAX_ANISO = 8;

function tex(c, color = true, repeatMeters = null) {
  const t = new THREE.CanvasTexture(c);
  t.wrapS = t.wrapT = THREE.RepeatWrapping;
  t.anisotropy = MAX_ANISO;
  if (color) t.colorSpace = THREE.SRGBColorSpace;
  if (repeatMeters) t.repeat.set(1 / repeatMeters[0], 1 / repeatMeters[1]);
  t.needsUpdate = true;
  return t;
}

// hoogtekaart (grijswaarden-canvas) -> normal map
function heightToNormal(hc, strength = 2) {
  const w = hc.width, h = hc.height;
  const src = hc.getContext('2d').getImageData(0, 0, w, h).data;
  const out = canvas(w, h);
  const ctx = out.getContext('2d');
  const img = ctx.createImageData(w, h);
  const H = (x, y) => src[(((y + h) % h) * w + ((x + w) % w)) * 4] / 255;
  for (let y = 0; y < h; y++) for (let x = 0; x < w; x++) {
    const dx = (H(x + 1, y) - H(x - 1, y)) * strength;
    const dy = (H(x, y + 1) - H(x, y - 1)) * strength;
    let nx = -dx, ny = dy, nz = 1;
    const l = Math.hypot(nx, ny, nz);
    nx /= l; ny /= l; nz /= l;
    const i = (y * w + x) * 4;
    img.data[i] = (nx * 0.5 + 0.5) * 255;
    img.data[i + 1] = (ny * 0.5 + 0.5) * 255;
    img.data[i + 2] = (nz * 0.5 + 0.5) * 255;
    img.data[i + 3] = 255;
  }
  ctx.putImageData(img, 0, 0);
  return out;
}

function speckle(ctx, w, h, n, alpha, r, light = true) {
  for (let i = 0; i < n; i++) {
    const v = light ? 255 : 0;
    ctx.fillStyle = `rgba(${v},${v},${v},${Math.random() * alpha})`;
    ctx.fillRect(Math.random() * w, Math.random() * h, r * Math.random() + 0.5, r * Math.random() + 0.5);
  }
}

// UV's in meters, per vlak afhankelijk van de normaal (box-mapping)
export function worldUV(geo) {
  if (!geo.attributes.normal || !geo.index) geo.computeVertexNormals();
  const p = geo.attributes.position, n = geo.attributes.normal;
  const uv = new Float32Array(p.count * 2);
  for (let i = 0; i < p.count; i++) {
    const ax = Math.abs(n.getX(i)), ay = Math.abs(n.getY(i)), az = Math.abs(n.getZ(i));
    let u, v;
    if (az >= ax && az >= ay) { u = p.getX(i) * Math.sign(n.getZ(i) || 1); v = p.getY(i); }
    else if (ax >= ay) { u = -p.getZ(i) * Math.sign(n.getX(i) || 1); v = p.getY(i); }
    else { u = p.getX(i); v = p.getZ(i); }
    uv[i * 2] = u; uv[i * 2 + 1] = v;
  }
  geo.setAttribute('uv', new THREE.BufferAttribute(uv, 2));
  return geo;
}

export function box(w, h, d, mat, x = 0, y = 0, z = 0, opts = {}) {
  const g = new THREE.BoxGeometry(w, h, d);
  g.translate(x, y, z);
  if (opts.worldUV !== false) worldUV(g);
  const m = new THREE.Mesh(g, mat);
  m.castShadow = opts.cast !== false;
  m.receiveShadow = true;
  return m;
}

export function cylBetween(a, b, r, mat, seg = 12) {
  const len = a.distanceTo(b);
  const g = new THREE.CylinderGeometry(r, r, len, seg, 1, false);
  const m = new THREE.Mesh(g, mat);
  m.position.copy(a).add(b).multiplyScalar(0.5);
  m.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), b.clone().sub(a).normalize());
  m.castShadow = true; m.receiveShadow = true;
  return m;
}

/* ------------------------------------------------------------------ */
/* Texturen                                                             */
/* ------------------------------------------------------------------ */

// Baksteen in halfsteensverband. Waalformaat: 210x50 mm, voeg 12 mm.
export function brickTextures(opts = {}) {
  const { hue = 12, sat = 52, light = 36, varL = 7, mortar = '#c2bbae', seed = 1, soldier = false } = opts;
  const R = rng(seed);
  const pitchX = 0.222, pitchY = 0.0625;
  const nx = soldier ? 24 : 6, ny = soldier ? 1 : 24;
  const bw = soldier ? pitchY : pitchX, bh = soldier ? pitchX : pitchY;
  const ppm = 768; // pixels per meter
  const W = Math.round(nx * bw * ppm), H = Math.round(ny * bh * ppm);
  const c = canvas(W, H), hc = canvas(W, H), rc = canvas(W, H);
  const ctx = c.getContext('2d'), hx = hc.getContext('2d'), rx = rc.getContext('2d');
  ctx.fillStyle = mortar; ctx.fillRect(0, 0, W, H);
  speckle(ctx, W, H, W * H / 60, 0.18, 2, false);
  hx.fillStyle = '#303030'; hx.fillRect(0, 0, W, H);
  rx.fillStyle = '#f2f2f2'; rx.fillRect(0, 0, W, H);
  const joint = 0.011 * ppm;
  for (let row = 0; row < ny; row++) {
    const off = soldier ? 0 : (row % 2) * 0.5;
    for (let col = -1; col <= nx; col++) {
      const x = (col + off) * bw * ppm + joint / 2;
      const y = row * bh * ppm + joint / 2;
      const w = bw * ppm - joint, h = bh * ppm - joint;
      const L = light + (R() - 0.5) * 2 * varL;
      const Hh = hue + (R() - 0.5) * 8;
      const S = sat + (R() - 0.5) * 14;
      ctx.fillStyle = `hsl(${Hh},${S}%,${L}%)`;
      ctx.fillRect(x, y, w, h);
      // gebakken verloop + vlekjes
      const g = ctx.createLinearGradient(x, y, x + w, y + h);
      g.addColorStop(0, `rgba(255,220,190,${R() * 0.12})`);
      g.addColorStop(1, `rgba(40,10,0,${R() * 0.22})`);
      ctx.fillStyle = g; ctx.fillRect(x, y, w, h);
      for (let k = 0; k < w * h / 30; k++) {
        const dark = R() < 0.5;
        ctx.fillStyle = dark ? `rgba(40,15,5,${R() * 0.25})` : `rgba(255,210,170,${R() * 0.15})`;
        ctx.fillRect(x + R() * w, y + R() * h, 1 + R() * 2.5, 1 + R() * 2.5);
      }
      if (R() < 0.12) { // gesinterde, donkere kop
        ctx.fillStyle = `rgba(30,12,8,${0.15 + R() * 0.25})`;
        ctx.fillRect(x + (R() < 0.5 ? 0 : w * 0.6), y, w * 0.4, h);
      }
      hx.fillStyle = '#d8d8d8'; hx.fillRect(x + 1, y + 1, w - 2, h - 2);
      hx.fillStyle = '#ffffff'; hx.fillRect(x + 3, y + 3, w - 6, h - 6);
      const rv = (200 + R() * 40) | 0;
      rx.fillStyle = `rgb(${rv},${rv},${rv})`;
      rx.fillRect(x, y, w, h);
    }
  }
  speckle(hx, W, H, W * H / 40, 0.2, 2, false);
  const size = [nx * bw, ny * bh];
  return {
    map: tex(c, true, size),
    normalMap: tex(heightToNormal(hc, 3.5), false, size),
    roughnessMap: tex(rc, false, size),
  };
}

export function brickMaterial(opts = {}) {
  const t = brickTextures(opts);
  return new THREE.MeshStandardMaterial({ ...t, roughness: 1, normalScale: new THREE.Vector2(1, 1), envMapIntensity: 0.5 });
}

// Oud-Hollandse pannen (OVH): golvend profiel, rijen met overlap.
export function roofMaterial(opts = {}) {
  const { hue = 13, sat = 62, light = 40, seed = 7, glazed = false } = opts;
  const R = rng(seed);
  const tw = 0.21, th = 0.30, nx = 6, ny = 5, ppm = 640;
  const W = Math.round(nx * tw * ppm), H = Math.round(ny * th * ppm);
  const c = canvas(W, H), hc = canvas(W, H);
  const ctx = c.getContext('2d'), hx = hc.getContext('2d');
  const pw = tw * ppm, ph = th * ppm;
  for (let row = 0; row < ny; row++) {
    for (let col = 0; col < nx; col++) {
      const x0 = col * pw, y0 = H - (row + 1) * ph; // v loopt omhoog; canvas y omlaag
      const L = light + (R() - 0.5) * 9, Hh = hue + (R() - 0.5) * 6, S = sat + (R() - 0.5) * 12;
      for (let px = 0; px < pw; px++) {
        const t = px / pw;
        const prof = Math.sin(t * Math.PI * 2 - Math.PI / 2) * 0.5 + 0.5; // 0..1 golf
        const shade = 0.78 + 0.32 * Math.cos((t - 0.3) * Math.PI * 2) * 0.5;
        ctx.fillStyle = `hsl(${Hh},${S}%,${L * shade}%)`;
        ctx.fillRect(x0 + px, y0, 1.2, ph);
        const hv = Math.round(70 + prof * 150);
        hx.fillStyle = `rgb(${hv},${hv},${hv})`;
        hx.fillRect(x0 + px, y0, 1.2, ph);
      }
      // onderrand (neus) donker: schaduw van de overlap op de pan eronder
      const g = ctx.createLinearGradient(0, y0 + ph - ph * 0.16, 0, y0 + ph);
      g.addColorStop(0, 'rgba(0,0,0,0)'); g.addColorStop(1, 'rgba(25,8,2,0.55)');
      ctx.fillStyle = g; ctx.fillRect(x0, y0 + ph * 0.84, pw, ph * 0.16);
      const g2 = ctx.createLinearGradient(0, y0, 0, y0 + ph * 0.25);
      g2.addColorStop(0, 'rgba(255,230,200,0.14)'); g2.addColorStop(1, 'rgba(0,0,0,0)');
      ctx.fillStyle = g2; ctx.fillRect(x0, y0, pw, ph * 0.25);
      const gh = hx.createLinearGradient(0, y0, 0, y0 + ph);
      gh.addColorStop(0, 'rgba(0,0,0,0.0)'); gh.addColorStop(0.92, 'rgba(255,255,255,0.25)'); gh.addColorStop(1, 'rgba(0,0,0,0.9)');
      hx.fillStyle = gh; hx.fillRect(x0, y0, pw, ph);
      // verwering en mos-vlekjes
      for (let k = 0; k < 140; k++) {
        ctx.fillStyle = R() < 0.85 ? `rgba(30,12,6,${R() * 0.18})` : `rgba(90,95,50,${R() * 0.25})`;
        ctx.beginPath(); ctx.arc(x0 + R() * pw, y0 + R() * ph, 0.5 + R() * 2.5, 0, 7); ctx.fill();
      }
      ctx.fillStyle = 'rgba(20,6,2,0.5)'; ctx.fillRect(x0 + pw - 1.5, y0, 1.5, ph);
    }
  }
  const size = [nx * tw, ny * th];
  return new THREE.MeshStandardMaterial({
    map: tex(c, true, size), normalMap: tex(heightToNormal(hc, 5), false, size),
    roughness: glazed ? 0.38 : 0.82, metalness: 0, envMapIntensity: glazed ? 1.2 : 0.5,
  });
}

// Gelakt hout: egale lak met heel subtiele houtnerf in de normal map.
export function paintMaterial(hex, opts = {}) {
  if (!paintMaterial._n) {
    const c = canvas(256, 1024), x = c.getContext('2d');
    x.fillStyle = '#808080'; x.fillRect(0, 0, 256, 1024);
    for (let i = 0; i < 90; i++) {
      const gv = Math.random() < 0.5 ? 0 : 255;
      x.strokeStyle = `rgba(${gv},${gv},${gv},0.06)`;
      x.lineWidth = 1 + Math.random() * 3;
      const px = Math.random() * 256;
      x.beginPath(); x.moveTo(px, 0);
      for (let y = 0; y <= 1024; y += 64) x.lineTo(px + Math.sin(y * 0.01 + i) * 6, y);
      x.stroke();
    }
    paintMaterial._n = tex(heightToNormal(c, 1.2), false, [0.3, 1.2]);
  }
  return new THREE.MeshPhysicalMaterial({
    color: new THREE.Color(hex), roughness: opts.roughness ?? 0.32, metalness: 0,
    clearcoat: opts.clearcoat ?? 0.35, clearcoatRoughness: 0.25,
    normalMap: paintMaterial._n, normalScale: new THREE.Vector2(0.35, 0.35), envMapIntensity: 0.9,
  });
}

export function concreteMaterial(hex = '#b9b4aa', size = 1.0, seed = 3, roughness = 0.9) {
  const R = rng(seed);
  const c = canvas(512, 512), x = c.getContext('2d');
  x.fillStyle = hex; x.fillRect(0, 0, 512, 512);
  for (let i = 0; i < 9000; i++) {
    x.fillStyle = R() < 0.5 ? `rgba(0,0,0,${R() * 0.12})` : `rgba(255,255,255,${R() * 0.12})`;
    x.fillRect(R() * 512, R() * 512, 1 + R() * 2, 1 + R() * 2);
  }
  return new THREE.MeshStandardMaterial({ map: tex(c, true, [size, size]), roughness, envMapIntensity: 0.5 });
}

// Grijze trottoirtegels 30x30 met voegen
export function pavingMaterial(opts = {}) {
  const { tile = 0.3, n = 4, hex = [150, 146, 138], seed = 11, joint = '#7d786f' } = opts;
  const R = rng(seed);
  const ppm = 1024 / (tile * n);
  const c = canvas(1024, 1024), x = c.getContext('2d'), hc = canvas(1024, 1024), hx = hc.getContext('2d');
  x.fillStyle = joint; x.fillRect(0, 0, 1024, 1024);
  hx.fillStyle = '#000'; hx.fillRect(0, 0, 1024, 1024);
  const tp = tile * ppm, j = 5;
  for (let i = 0; i < n; i++) for (let k = 0; k < n; k++) {
    const v = (R() - 0.5) * 22;
    x.fillStyle = `rgb(${hex[0] + v},${hex[1] + v},${hex[2] + v - 2})`;
    x.fillRect(i * tp + j / 2, k * tp + j / 2, tp - j, tp - j);
    for (let s = 0; s < 1600; s++) {
      x.fillStyle = R() < 0.5 ? `rgba(0,0,0,${R() * 0.18})` : `rgba(255,255,255,${R() * 0.14})`;
      x.fillRect(i * tp + R() * tp, k * tp + R() * tp, 1 + R() * 2, 1 + R() * 2);
    }
    if (R() < 0.35) { // vlek / verkleuring
      x.fillStyle = `rgba(60,55,40,${R() * 0.12})`;
      x.beginPath(); x.arc(i * tp + R() * tp, k * tp + R() * tp, 10 + R() * 40, 0, 7); x.fill();
    }
    hx.fillStyle = '#fff'; hx.fillRect(i * tp + j, k * tp + j, tp - 2 * j, tp - 2 * j);
  }
  const s = [tile * n, tile * n];
  return new THREE.MeshStandardMaterial({ map: tex(c, true, s), normalMap: tex(heightToNormal(hc, 2), false, s), roughness: 0.92, envMapIntensity: 0.5 });
}

export function grassMaterial(seed = 5) {
  const R = rng(seed);
  const S = 1024;
  const c = canvas(S, S), x = c.getContext('2d'), hc = canvas(S, S), hx = hc.getContext('2d');
  x.fillStyle = '#4f7a2c'; x.fillRect(0, 0, S, S);
  hx.fillStyle = '#404040'; hx.fillRect(0, 0, S, S);
  for (let i = 0; i < 90000; i++) {
    const px = R() * S, py = R() * S, len = 3 + R() * 9, a = -Math.PI / 2 + (R() - 0.5) * 1.2;
    const L = 22 + R() * 26, H = 78 + R() * 26;
    x.strokeStyle = `hsla(${H},${48 + R() * 20}%,${L}%,0.9)`;
    x.lineWidth = 1 + R() * 1.2;
    x.beginPath(); x.moveTo(px, py); x.lineTo(px + Math.cos(a) * len, py + Math.sin(a) * len); x.stroke();
    const hv = 60 + R() * 195 | 0;
    hx.strokeStyle = `rgb(${hv},${hv},${hv})`; hx.lineWidth = 1;
    hx.beginPath(); hx.moveTo(px, py); hx.lineTo(px + Math.cos(a) * len, py + Math.sin(a) * len); hx.stroke();
  }
  // grote vlekken voor variatie
  for (let i = 0; i < 40; i++) {
    x.fillStyle = R() < 0.5 ? `rgba(120,140,40,${R() * 0.08})` : `rgba(20,50,10,${R() * 0.1})`;
    x.beginPath(); x.arc(R() * S, R() * S, 40 + R() * 160, 0, 7); x.fill();
  }
  return new THREE.MeshStandardMaterial({ map: tex(c, true, [1.6, 1.6]), normalMap: tex(heightToNormal(hc, 1.5), false, [1.6, 1.6]), roughness: 0.95, envMapIntensity: 0.4 });
}

export function leafMaterial(opts = {}) {
  const { hue = 95, light = 26, seed = 9, size = 0.8 } = opts;
  const R = rng(seed);
  const S = 512;
  const c = canvas(S, S), x = c.getContext('2d'), hc = canvas(S, S), hx = hc.getContext('2d');
  x.fillStyle = `hsl(${hue},40%,${light * 0.45}%)`; x.fillRect(0, 0, S, S);
  hx.fillStyle = '#000'; hx.fillRect(0, 0, S, S);
  for (let i = 0; i < 7000; i++) {
    const px = R() * S, py = R() * S, r = 3 + R() * 5, a = R() * Math.PI;
    const L = light * (0.6 + R() * 0.9);
    x.fillStyle = `hsl(${hue + (R() - 0.5) * 22},${38 + R() * 25}%,${L}%)`;
    x.beginPath(); x.ellipse(px, py, r, r * 0.55, a, 0, 7); x.fill();
    const hv = 100 + R() * 155 | 0;
    hx.fillStyle = `rgb(${hv},${hv},${hv})`;
    hx.beginPath(); hx.ellipse(px, py, r, r * 0.55, a, 0, 7); hx.fill();
  }
  return new THREE.MeshStandardMaterial({ map: tex(c, true, [size, size]), normalMap: tex(heightToNormal(hc, 3), false, [size, size]), roughness: 0.85, envMapIntensity: 0.45 });
}

export function asphaltMaterial() {
  const c = canvas(512, 512), x = c.getContext('2d');
  x.fillStyle = '#4b4a49'; x.fillRect(0, 0, 512, 512);
  for (let i = 0; i < 30000; i++) {
    x.fillStyle = Math.random() < 0.5 ? `rgba(0,0,0,${Math.random() * 0.3})` : `rgba(255,255,255,${Math.random() * 0.15})`;
    x.fillRect(Math.random() * 512, Math.random() * 512, 1 + Math.random() * 2, 1 + Math.random() * 2);
  }
  return new THREE.MeshStandardMaterial({ map: tex(c, true, [2, 2]), roughness: 0.95, envMapIntensity: 0.4 });
}

/* ------------------------------------------------------------------ */
/* Renderer, lucht en licht                                             */
/* ------------------------------------------------------------------ */

export const RENDER_W = 2400, RENDER_H = 1650; // 1,5x supersampling voor 1600x1100

export function makeSkyMaterial() {
  return new THREE.ShaderMaterial({
    side: THREE.BackSide, depthWrite: false, fog: false,
    uniforms: {
      top: { value: new THREE.Color('#4f8fd0') },
      mid: { value: new THREE.Color('#9cc4e6') },
      horizon: { value: new THREE.Color('#e9eef0') },
      ground: { value: new THREE.Color('#8f9a86') },
      sunDir: { value: new THREE.Vector3(-0.5, 0.6, 0.4).normalize() },
      sunBoost: { value: 0.0 },
    },
    vertexShader: `varying vec3 vW; void main(){ vec4 w = modelMatrix*vec4(position,1.0); vW = w.xyz; gl_Position = projectionMatrix*viewMatrix*w; }`,
    fragmentShader: `uniform vec3 top; uniform vec3 mid; uniform vec3 horizon; uniform vec3 ground; uniform vec3 sunDir; uniform float sunBoost; varying vec3 vW;
      void main(){
        vec3 d = normalize(vW - cameraPosition);
        float h = d.y;
        vec3 c = mix(horizon, mid, smoothstep(0.0, 0.18, h));
        c = mix(c, top, smoothstep(0.15, 0.75, h));
        c = mix(c, ground, smoothstep(0.0, -0.08, h));
        float s = max(dot(d, sunDir), 0.0);
        c += vec3(1.0, 0.85, 0.6) * (pow(s, 8.0) * 0.25 + pow(s, 600.0) * sunBoost);
        gl_FragColor = vec4(c, 1.0);
        #include <tonemapping_fragment>
        #include <colorspace_fragment>
      }`,
  });
}

export function setup(opts = {}) {
  const renderer = new THREE.WebGLRenderer({ antialias: true, preserveDrawingBuffer: true });
  renderer.setPixelRatio(1);
  renderer.setSize(RENDER_W, RENDER_H, false);
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = opts.exposure ?? 1.0;
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  MAX_ANISO = renderer.capabilities.getMaxAnisotropy();
  document.body.appendChild(renderer.domElement);

  const scene = new THREE.Scene();
  const sunDir = new THREE.Vector3(...(opts.sunDir ?? [-0.62, 0.62, 0.48])).normalize();

  const sky = new THREE.Mesh(new THREE.SphereGeometry(400, 48, 24), makeSkyMaterial());
  sky.material.uniforms.sunDir.value.copy(sunDir);
  scene.add(sky);
  scene.fog = new THREE.Fog('#e3e9e8', opts.fogNear ?? 45, opts.fogFar ?? 220);

  // omgevingskaart voor reflecties (glas, lak, zink)
  const envScene = new THREE.Scene();
  const envSky = new THREE.Mesh(new THREE.SphereGeometry(100, 48, 24), makeSkyMaterial());
  envSky.material.uniforms.sunDir.value.copy(sunDir);
  envSky.material.uniforms.sunBoost.value = 8.0;
  envSky.material.toneMapped = false;
  envScene.add(envSky);
  // een paar donkere 'bomen/huizen' aan de horizon, zodat het glas iets te spiegelen heeft
  const darkMat = new THREE.MeshBasicMaterial({ color: '#3d4a3a' });
  const houseMat = new THREE.MeshBasicMaterial({ color: '#8a5a48' });
  const R = rng(42);
  for (let i = 0; i < 26; i++) {
    const a = R() * Math.PI * 2, r = 60;
    const isHouse = R() < 0.4;
    const m = new THREE.Mesh(isHouse ? new THREE.BoxGeometry(10 + R() * 10, 8 + R() * 6, 6) : new THREE.SphereGeometry(5 + R() * 6, 12, 8), isHouse ? houseMat : darkMat);
    m.position.set(Math.cos(a) * r, isHouse ? 2 : 4 + R() * 4, Math.sin(a) * r);
    m.lookAt(0, m.position.y, 0);
    envScene.add(m);
  }
  const pmrem = new THREE.PMREMGenerator(renderer);
  scene.environment = pmrem.fromScene(envScene, 0.015).texture;

  const hemi = new THREE.HemisphereLight('#cfe3f7', '#8a8070', opts.hemi ?? 0.9);
  scene.add(hemi);

  const sun = new THREE.DirectionalLight('#ffe4bf', opts.sun ?? 3.4);
  sun.position.copy(sunDir).multiplyScalar(60);
  sun.castShadow = true;
  sun.shadow.mapSize.set(4096, 4096);
  const sc = opts.shadowSize ?? 18;
  Object.assign(sun.shadow.camera, { left: -sc, right: sc, top: sc, bottom: -sc, near: 1, far: 160 });
  sun.shadow.bias = -0.0003;
  sun.shadow.normalBias = 0.025;
  sun.shadow.radius = 4;
  scene.add(sun, sun.target);

  const camera = new THREE.PerspectiveCamera(opts.fov ?? 32, RENDER_W / RENDER_H, 0.1, 900);
  return { renderer, scene, camera, sun, hemi, sunDir };
}

// Camera met horizontale kijkrichting en 'shift lens', zodat verticale lijnen verticaal blijven.
export function archCamera(camera, pos, target, shiftY = 0) {
  camera.position.set(...pos);
  camera.lookAt(target[0], pos[1], target[2]);
  camera.setViewOffset(RENDER_W, RENDER_H, 0, -shiftY * RENDER_H, RENDER_W, RENDER_H);
  camera.updateProjectionMatrix();
}

/* ------------------------------------------------------------------ */
/* Kozijnen, ramen en deuren                                            */
/* ------------------------------------------------------------------ */

// Glas: donker en spiegelend (lucht en bomen uit de omgevingskaart), interieur schemert erdoor.
export const GLASS = () => new THREE.MeshPhysicalMaterial({
  color: '#26303a', metalness: 0.1, roughness: 0.03, ior: 1.9, specularIntensity: 1,
  envMapIntensity: 2.4, transparent: true, opacity: 0.8, depthWrite: false,
});

function interior(group, w, h, wallT, colors) {
  // donkere 'kamer' achter het glas met vitrage en gordijnen
  const roomMat = new THREE.MeshStandardMaterial({ color: '#221e1b', roughness: 0.95, side: THREE.BackSide });
  const room = new THREE.Mesh(new THREE.BoxGeometry(w + 0.6, h + 0.6, 1.4), roomMat);
  room.position.set(0, h / 2, -wallT - 0.7 + 0.001);
  room.receiveShadow = true;
  group.add(room);
  const vitrage = new THREE.MeshStandardMaterial({ color: '#f3efe6', roughness: 0.9, transparent: true, opacity: 0.22, side: THREE.DoubleSide });
  const v = new THREE.Mesh(new THREE.PlaneGeometry(w + 0.1, h * 0.55), vitrage);
  v.position.set(0, h * 0.42, -0.24);
  group.add(v);
  const curtain = new THREE.MeshStandardMaterial({ color: colors?.curtain ?? '#b9a88a', roughness: 0.95 });
  for (const s of [-1, 1]) {
    const cg = new THREE.PlaneGeometry(Math.min(0.35, w * 0.22), h + 0.1, 12, 1);
    const p = cg.attributes.position;
    for (let i = 0; i < p.count; i++) p.setZ(i, Math.sin(p.getX(i) * 40) * 0.025);
    cg.computeVertexNormals();
    const cm = new THREE.Mesh(cg, curtain);
    cm.position.set(s * (w / 2 - Math.min(0.35, w * 0.22) / 2 + 0.05), h / 2, -0.32);
    cm.receiveShadow = true;
    group.add(cm);
  }
}

/**
 * Raam in een muuropening. Oorsprong: midden-onder van de opening, in het gevelvlak.
 * opts: cols (vakken), topH (hoogte bovenlicht, 0 = geen), topGrid [kolommen, rijen] roeden per bovenlichtvak
 */
export function makeWindow(w, h, frameMat, opts = {}) {
  const { cols = 1, topH = 0, topGrid = [2, 2], reveal = 0.09, wallT = 0.3, sillMat, glassMat = GLASS(), lowerGrid = null } = opts;
  const sashMat = opts.sashMat ?? frameMat;
  const g = new THREE.Group();
  const fw = 0.075, fd = 0.11, zf = -reveal - fd / 2; // kozijnhout
  const add = (m) => { g.add(m); return m; };
  // kozijn: stijlen, bovendorpel, onderdorpel (iets dikker en schuin)
  add(box(fw, h, fd, frameMat, -w / 2 + fw / 2, h / 2, zf));
  add(box(fw, h, fd, frameMat, w / 2 - fw / 2, h / 2, zf));
  add(box(w, fw, fd, frameMat, 0, h - fw / 2, zf));
  const dorpel = box(w, 0.07, fd + 0.03, frameMat, 0, 0.035, zf + 0.015);
  add(dorpel);
  // raamdorpelstenen (geglazuurd, donker) onder het kozijn, naar buiten aflopend
  const sm = sillMat ?? new THREE.MeshStandardMaterial({ color: '#2a2d33', roughness: 0.35, envMapIntensity: 1 });
  const sill = box(w + 0.12, 0.05, reveal + 0.07, sm, 0, -0.02, -reveal / 2 + 0.025);
  sill.rotation.x = 0.16;
  add(sill);
  // tussendorpel (kalf) en middenstijlen
  const lowTop = topH > 0 ? h - topH : h;
  if (topH > 0) add(box(w, fw, fd, frameMat, 0, lowTop - fw / 2, zf));
  const innerW = w - 2 * fw;
  const colW = innerW / cols;
  for (let i = 1; i < cols; i++) {
    const x = -w / 2 + fw + i * colW;
    add(box(fw * 0.9, h - fw, fd, frameMat, x, h / 2, zf));
  }
  // glas
  const glassZ = -reveal - fd * 0.55;
  const glass = new THREE.Mesh(new THREE.PlaneGeometry(innerW, h - fw), glassMat);
  glass.position.set(0, (h - fw + 0.07) / 2, glassZ);
  g.add(glass);
  // ramen (draaiende delen) met eigen profiel, roeden in het bovenlicht
  const sw = 0.055, sd = 0.05;
  for (let i = 0; i < cols; i++) {
    const cx = -w / 2 + fw + colW * (i + 0.5);
    const x0 = cx - colW / 2 + 0.006, x1 = cx + colW / 2 - 0.006;
    const y0 = 0.07, y1 = lowTop - (topH > 0 ? fw : fw);
    const bw = x1 - x0, bh = y1 - y0, sz = glassZ + sd / 2 + 0.004;
    add(box(sw, bh, sd, sashMat, x0 + sw / 2, (y0 + y1) / 2, sz));
    add(box(sw, bh, sd, sashMat, x1 - sw / 2, (y0 + y1) / 2, sz));
    add(box(bw, sw, sd, sashMat, (x0 + x1) / 2, y1 - sw / 2, sz));
    add(box(bw, sw * 1.3, sd, sashMat, (x0 + x1) / 2, y0 + sw * 0.65, sz));
    if (lowerGrid) {
      const [gc, gr] = lowerGrid, rw = 0.024;
      for (let a = 1; a < gc; a++) add(box(rw, bh, 0.028, sashMat, x0 + sw + (bw - 2 * sw) * a / gc, (y0 + y1) / 2, glassZ + 0.016));
      for (let b = 1; b < gr; b++) add(box(bw, rw, 0.028, sashMat, (x0 + x1) / 2, y0 + sw + (bh - 2 * sw) * b / gr, glassZ + 0.016));
    }
    if (topH > 0) {
      const ty0 = lowTop, ty1 = h - fw, th = ty1 - ty0;
      const [gc, gr] = topGrid, rw = 0.024;
      for (let a = 1; a < gc; a++) add(box(rw, th, 0.03, sashMat, x0 + bw * a / gc, (ty0 + ty1) / 2, glassZ + 0.018));
      for (let b = 1; b < gr; b++) add(box(bw, rw, 0.03, sashMat, (x0 + x1) / 2, ty0 + th * b / gr, glassZ + 0.018));
    }
  }
  interior(g, w, h, wallT, opts.colors);
  return g;
}

/**
 * Voordeur met kozijn, bovenlicht met roeden, paneeldeur met klein raampje, brievenbus en knop.
 */
export function makeDoor(w, h, frameMat, doorMat, opts = {}) {
  const { topH = 0.42, reveal = 0.12, wallT = 0.3, glassMat = GLASS(), metal } = opts;
  const g = new THREE.Group();
  const fw = 0.08, fd = 0.12, zf = -reveal - fd / 2;
  const add = (m) => { g.add(m); return m; };
  add(box(fw, h, fd, frameMat, -w / 2 + fw / 2, h / 2, zf));
  add(box(fw, h, fd, frameMat, w / 2 - fw / 2, h / 2, zf));
  add(box(w, fw, fd, frameMat, 0, h - fw / 2, zf));
  const leafTop = h - topH;
  add(box(w, fw, fd, frameMat, 0, leafTop - fw / 2, zf)); // kalf
  // bovenlicht met roeden
  const innerW = w - 2 * fw, glassZ = zf - 0.01;
  const tg = new THREE.Mesh(new THREE.PlaneGeometry(innerW, topH - fw), glassMat);
  tg.position.set(0, leafTop + (topH - fw) / 2, glassZ);
  g.add(tg);
  for (let a = 1; a < 3; a++) add(box(0.024, topH - fw, 0.03, frameMat, -innerW / 2 + innerW * a / 3, leafTop + (topH - fw) / 2, glassZ + 0.02));
  // deurblad
  const lw = innerW - 0.01, lh = leafTop - fw - 0.01, lz = zf + 0.0, ld = 0.045;
  const ly0 = 0.005;
  const leaf = new THREE.Group();
  leaf.position.set(0, ly0, lz);
  g.add(leaf);
  const st = 0.11; // stijl/regelbreedte
  leaf.add(box(lw, lh, ld * 0.6, doorMat, 0, lh / 2, -0.006)); // achterplaat (paneel)
  leaf.add(box(st, lh, ld, doorMat, -lw / 2 + st / 2, lh / 2, 0));
  leaf.add(box(st, lh, ld, doorMat, lw / 2 - st / 2, lh / 2, 0));
  leaf.add(box(lw, st, ld, doorMat, 0, lh - st / 2, 0));
  leaf.add(box(lw, st * 1.6, ld, doorMat, 0, st * 0.8, 0));
  const winBottom = lh * 0.62;
  leaf.add(box(lw, st * 0.8, ld, doorMat, 0, winBottom - st * 0.4, 0)); // regel onder raampje
  leaf.add(box(lw, st * 0.8, ld, doorMat, 0, lh * 0.36, 0)); // middenregel
  // verdiepte panelen met opstaande rand (profiel)
  const pw = lw - 2 * st;
  for (const [pa, pb] of [[st * 1.6, lh * 0.36 - st * 0.4], [lh * 0.36 + st * 0.4, winBottom - st * 0.8]]) {
    const ph = pb - pa;
    leaf.add(box(pw - 0.06, ph - 0.06, ld * 0.75, doorMat, 0, (pa + pb) / 2, -0.002));
  }
  // raampje met roeden
  const wy0 = winBottom, wy1 = lh - st, wh = wy1 - wy0;
  const dg = new THREE.Mesh(new THREE.PlaneGeometry(pw, wh), glassMat);
  dg.position.set(0, (wy0 + wy1) / 2, -0.01);
  leaf.add(dg);
  leaf.add(box(0.022, wh, 0.03, doorMat, 0, (wy0 + wy1) / 2, -0.004));
  leaf.add(box(pw, 0.022, 0.03, doorMat, 0, wy0 + wh / 2, -0.004));
  // beslag
  const brass = metal ?? new THREE.MeshStandardMaterial({ color: '#c9a35a', metalness: 1, roughness: 0.3 });
  leaf.add(box(0.26, 0.05, 0.012, brass, 0, lh * 0.36, ld / 2 + 0.006));
  const knob = new THREE.Mesh(new THREE.SphereGeometry(0.03, 16, 12), brass);
  knob.position.set(lw / 2 - st * 0.55, lh * 0.47, ld / 2 + 0.035);
  knob.castShadow = true;
  leaf.add(knob);
  leaf.add(box(0.035, 0.18, 0.012, brass, lw / 2 - st * 0.55, lh * 0.47, ld / 2 + 0.006));
  // stoep: hardstenen dorpel en betonnen opstap
  const stone = new THREE.MeshStandardMaterial({ color: '#4c4f52', roughness: 0.6 });
  add(box(w + 0.1, 0.08, reveal + 0.1, stone, 0, -0.04, -reveal / 2 + 0.05));
  interior(g, w, h, wallT, { curtain: '#3c342c' });
  return g;
}

/* ------------------------------------------------------------------ */
/* Woningblok                                                           */
/* ------------------------------------------------------------------ */

function wallWithHoles(len, height, holes, thickness) {
  const s = new THREE.Shape();
  s.moveTo(0, 0); s.lineTo(len, 0); s.lineTo(len, height); s.lineTo(0, height); s.lineTo(0, 0);
  for (const [x, y, w, h] of holes) {
    const p = new THREE.Path();
    p.moveTo(x, y); p.lineTo(x, y + h); p.lineTo(x + w, y + h); p.lineTo(x + w, y); p.lineTo(x, y);
    s.holes.push(p);
  }
  return new THREE.ExtrudeGeometry(s, { depth: thickness, bevelEnabled: false });
}

function planeFromPoints(pts, uOrigin, uDir, vDir, mat) {
  // driehoek of vierhoek (convex) met UV's in meters langs de goot (u) en de helling (v)
  const pos = [], uv = [];
  const tris = pts.length === 3 ? [[0, 1, 2]] : [[0, 1, 2], [0, 2, 3]];
  for (const t of tris) for (const i of t) {
    const p = pts[i];
    pos.push(p.x, p.y, p.z);
    const d = p.clone().sub(uOrigin);
    uv.push(d.dot(uDir), d.dot(vDir));
  }
  const g = new THREE.BufferGeometry();
  g.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
  g.setAttribute('uv', new THREE.Float32BufferAttribute(uv, 2));
  g.computeVertexNormals();
  const m = new THREE.Mesh(g, mat);
  m.castShadow = true; m.receiveShadow = true;
  return m;
}

/**
 * Een blok woningen (twee-onder-een-kap of rij) met schilddak.
 * units: [{ width, door: 'L'|'R', frame: hex, door: hex, brick: material }]
 */
export function buildBlock(opt) {
  const {
    units, depth = 8.2, eaveH = 5.75, pitch = 50, overhang = 0.5, wallT = 0.3,
    roofMat = roofMaterial(), fasciaHex = '#efe7d4', sideWindow = 'left',
  } = opt;
  const W = units.reduce((a, u) => a + u.width, 0);
  const g = new THREE.Group();
  const anchors = { units: [] };
  const zinc = new THREE.MeshStandardMaterial({ color: '#a9adaf', metalness: 0.7, roughness: 0.42 });
  const fasciaMat = paintMaterial(fasciaHex);
  const darkBrick = opt.plinthMat ?? brickMaterial({ hue: 10, sat: 35, light: 22, seed: 99 });

  let x0 = -W / 2;
  units.forEach((u, idx) => {
    const frameMat = paintMaterial(u.frame);
    const sashMat = u.sash ? paintMaterial(u.sash) : frameMat;
    const doorMat = paintMaterial(u.doorColor ?? u.frame, { clearcoat: 0.5 });
    const brick = u.brick;
    const soldier = u.soldier ?? brickMaterial({ soldier: true, hue: 11, sat: 45, light: 30, seed: 20 + idx });
    const w = u.width;
    const doorRight = u.door === 'R';
    const L = (t) => doorRight ? t : w - t; // positie vanaf linkerkant unit, gespiegeld
    // maten
    const mainW = Math.min(2.5, w * 0.42), mainH = 1.95, mainY = 0.8, mainX = L(w * 0.36);
    const doorW = 1.05, doorH = 2.55, doorY = 0.18, doorX = L(w - 0.95);
    const up1W = 1.75, up1H = 1.4, upY = 3.55, up1X = mainX;
    const up2W = 0.85, up2H = 1.3, up2X = doorX;
    const holes = [
      [mainX - mainW / 2, mainY, mainW, mainH],
      [doorX - doorW / 2, doorY, doorW, doorH],
      [up1X - up1W / 2, upY, up1W, up1H],
      [up2X - up2W / 2, upY + 0.1, up2W, up2H],
    ];
    const wg = wallWithHoles(w, eaveH, holes, wallT);
    wg.translate(x0, 0, -wallT);
    worldUV(wg);
    const wall = new THREE.Mesh(wg, brick);
    wall.castShadow = true; wall.receiveShadow = true;
    g.add(wall);
    // plint (donkere klinkers), iets voor de gevel, onderbroken bij de deur
    const pH = 0.5;
    const dl = doorX - doorW / 2, dr = doorX + doorW / 2;
    const segs = [[0, dl], [dr, w]].filter(([a, b]) => b - a > 0.01);
    for (const [a, b] of segs) g.add(box(b - a, pH, 0.02, darkBrick, x0 + (a + b) / 2, pH / 2, 0.01));
    // rollagen boven de openingen
    for (const [hx, hy, hw, hh] of holes) {
      g.add(box(hw + 0.12, 0.225, 0.025, soldier, x0 + hx + hw / 2, hy + hh + 0.1125, 0.012));
    }
    // ramen en deur
    const add = (obj, x, y) => { obj.position.set(x0 + x, y, 0); g.add(obj); return obj; };
    add(makeWindow(mainW, mainH, frameMat, { cols: 3, topH: 0.5, topGrid: [3, 2], wallT, sashMat }), mainX, mainY);
    add(makeWindow(up1W, up1H, frameMat, { cols: 2, topH: 0.42, topGrid: [3, 2], wallT, sashMat }), up1X, upY);
    add(makeWindow(up2W, up2H, frameMat, { cols: 1, topH: 0, wallT, lowerGrid: [2, 3], sashMat }), up2X, upY + 0.1);
    add(makeDoor(doorW, doorH, frameMat, doorMat, { wallT }), doorX, doorY);
    // luifel boven de deur
    const canopy = new THREE.MeshStandardMaterial({ color: '#d9d4c8', roughness: 0.85 });
    g.add(box(doorW + 0.5, 0.1, 0.62, canopy, x0 + doorX, doorY + doorH + 0.28, 0.31));
    g.add(box(doorW + 0.52, 0.04, 0.64, paintMaterial(u.frame), x0 + doorX, doorY + doorH + 0.35, 0.31));
    anchors.units.push({
      x0, w, main: { x: x0 + mainX, y: mainY, w: mainW, h: mainH }, door: { x: x0 + doorX, y: doorY, w: doorW, h: doorH },
      up1: { x: x0 + up1X, y: upY, w: up1W, h: up1H },
    });
    x0 += w;
  });

  // zijgevels
  for (const side of [-1, 1]) {
    const holes = [];
    if ((sideWindow === 'left' && side === -1) || sideWindow === 'both') {
      holes.push([2.2, 3.6, 0.9, 1.25]);
      holes.push([4.6, 0.95, 1.1, 1.3]);
    }
    let wg;
    if (side === -1) {
      wg = wallWithHoles(depth, eaveH, holes, wallT);
      wg.rotateY(Math.PI / 2); wg.translate(-W / 2, 0, 0);
    } else {
      wg = wallWithHoles(depth, eaveH, holes.map(([hx, hy, hw, hh]) => [depth - hx - hw, hy, hw, hh]), wallT);
      wg.rotateY(-Math.PI / 2); wg.translate(W / 2, 0, -depth);
    }
    worldUV(wg);
    const wall = new THREE.Mesh(wg, units[side === -1 ? 0 : units.length - 1].brick);
    wall.castShadow = true; wall.receiveShadow = true;
    g.add(wall);
    const sx = side * W / 2;
    const fm = paintMaterial(units[side === -1 ? 0 : units.length - 1].frame);
    for (const [hx, hy, hw, hh] of holes) {
      const win = makeWindow(hw, hh, fm, { cols: 1, topH: hh > 1.28 ? 0.38 : 0, topGrid: [2, 2], wallT, lowerGrid: hh > 1.28 ? null : [2, 2] });
      win.position.set(sx, hy, -hx - hw / 2);
      win.rotation.y = side * Math.PI / 2;
      g.add(win);
      const sold = units[0].soldier ?? brickMaterial({ soldier: true, hue: 11, sat: 45, light: 30, seed: 31 });
      const r = box(0.025, 0.225, hw + 0.12, sold, sx + side * 0.012, hy + hh + 0.1125, -hx - hw / 2);
      g.add(r);
    }
    g.add(box(0.02, 0.5, depth, darkBrick, sx + side * 0.01, 0.25, -depth / 2));
  }
  // achtergevel
  g.add(box(W, eaveH, wallT, units[0].brick, 0, eaveH / 2, -depth + wallT / 2));

  // ---- dak ----
  const o = overhang;
  const yE = eaveH + 0.2; // onderkant pannen bij de goot
  const zf = o, zb = -depth - o, xL = -W / 2 - o, xR = W / 2 + o;
  const run = (zf - zb) / 2, rise = run * Math.tan(pitch * Math.PI / 180);
  const yR = yE + rise, zm = (zf + zb) / 2;
  const V = (x, y, z) => new THREE.Vector3(x, y, z);
  const slopeLen = Math.hypot(run, rise);
  const fU = V(1, 0, 0), fV = V(0, rise, -run).normalize();
  g.add(planeFromPoints([V(xL, yE, zf), V(xR, yE, zf), V(xR - run, yR, zm), V(xL + run, yR, zm)], V(xL, yE, zf), fU, fV, roofMat));
  const bU = V(-1, 0, 0), bV = V(0, rise, run).normalize();
  g.add(planeFromPoints([V(xR, yE, zb), V(xL, yE, zb), V(xL + run, yR, zm), V(xR - run, yR, zm)], V(xR, yE, zb), bU, bV, roofMat));
  const lU = V(0, 0, 1), lV = V(run, rise, 0).normalize();
  g.add(planeFromPoints([V(xL, yE, zb), V(xL, yE, zf), V(xL + run, yR, zm)], V(xL, yE, zb), lU, lV, roofMat));
  const rU = V(0, 0, -1), rV = V(-run, rise, 0).normalize();
  g.add(planeFromPoints([V(xR, yE, zf), V(xR, yE, zb), V(xR - run, yR, zm)], V(xR, yE, zf), rU, rV, roofMat));
  // nok- en hoekkeper-vorsten
  const ridgeMat = roofMat.clone(); ridgeMat.color = new THREE.Color('#e0c8bb');
  const vr = 0.1;
  g.add(cylBetween(V(xL + run, yR + 0.02, zm), V(xR - run, yR + 0.02, zm), vr, ridgeMat));
  for (const [a, b] of [[V(xL, yE, zf), V(xL + run, yR, zm)], [V(xR, yE, zf), V(xR - run, yR, zm)], [V(xL, yE, zb), V(xL + run, yR, zm)], [V(xR, yE, zb), V(xR - run, yR, zm)]]) {
    g.add(cylBetween(a.clone().add(V(0, 0.03, 0)), b.clone().add(V(0, 0.03, 0)), vr * 0.9, ridgeMat));
  }
  // overstek: boeidelen (rondom), onderkant (gootklos-plafond), mastgoot
  const fH = 0.26, fT = 0.035;
  const soffitMat = paintMaterial('#f4f1ea', { clearcoat: 0 });
  const fy = eaveH + 0.2 - fH / 2 + 0.04;
  g.add(box(xR - xL + fT * 2, fH, fT, fasciaMat, 0, fy, zf + fT / 2));
  g.add(box(xR - xL + fT * 2, fH, fT, fasciaMat, 0, fy, zb - fT / 2));
  g.add(box(fT, fH, zf - zb, fasciaMat, xL - fT / 2, fy, zm));
  g.add(box(fT, fH, zf - zb, fasciaMat, xR + fT / 2, fy, zm));
  const sy = eaveH + 0.2 - fH + 0.05;
  g.add(box(xR - xL, 0.02, o, soffitMat, 0, sy, o / 2, { cast: false }));
  g.add(box(xR - xL, 0.02, o, soffitMat, 0, sy, -depth - o / 2, { cast: false }));
  g.add(box(o, 0.02, depth, soffitMat, xL + o / 2, sy, -depth / 2, { cast: false }));
  g.add(box(o, 0.02, depth, soffitMat, xR - o / 2, sy, -depth / 2, { cast: false }));
  // vulling tussen muur en dak (zodat er geen kier zichtbaar is)
  g.add(box(W, 0.9, wallT, units[0].brick, 0, eaveH + 0.45, -wallT / 2));
  // zinken goot (halfrond) langs voor- en zijkanten
  const gutterR = 0.07;
  const gy = yE - 0.03;
  const gutter = (a, b) => {
    const len = a.distanceTo(b);
    const geo = new THREE.CylinderGeometry(gutterR, gutterR, len, 16, 1, true, Math.PI / 2, Math.PI);
    const m = new THREE.Mesh(geo, new THREE.MeshStandardMaterial({ color: '#a9adaf', metalness: 0.7, roughness: 0.42, side: THREE.DoubleSide }));
    m.position.copy(a).add(b).multiplyScalar(0.5);
    m.quaternion.setFromUnitVectors(V(0, 1, 0), b.clone().sub(a).normalize());
    m.castShadow = true;
    return m;
  };
  const go = fT + gutterR * 0.9;
  g.add(gutter(V(xL - go, gy, zf + go), V(xR + go, gy, zf + go)));
  g.add(gutter(V(xL - go, gy, zb - go), V(xL - go, gy, zf + go)));
  g.add(gutter(V(xR + go, gy, zf + go), V(xR + go, gy, zb - go)));
  g.add(gutter(V(xR + go, gy, zb - go), V(xL - go, gy, zb - go)));
  // gootrand (kraal) en hemelwaterafvoeren op de hoeken
  for (const s of [-1, 1]) {
    const px = s * (W / 2 + 0.12), pz = 0.12;
    g.add(cylBetween(V(px, 0.05, pz), V(px, eaveH - 0.1, pz), 0.04, zinc));
    g.add(cylBetween(V(px, eaveH - 0.12, pz), V(s * (W / 2 + o + 0.02), gy - 0.06, zf + go - 0.1), 0.04, zinc));
    g.add(box(0.1, 0.03, 0.06, zinc, px, 2.2, pz - 0.06));
    g.add(box(0.1, 0.03, 0.06, zinc, px, 4.4, pz - 0.06));
  }
  // schoorstenen op de woningscheidende muren
  const chimMat = units[0].brick;
  const capMat = concreteMaterial('#bdb7ad', 1);
  const chimneys = opt.chimneys ?? [0];
  for (const cx of chimneys) {
    const ch = rise + 1.1;
    g.add(box(0.95, ch, 0.62, chimMat, cx, yE + ch / 2 + 0.1, zm - 0.2));
    g.add(box(1.12, 0.09, 0.8, capMat, cx, yE + ch + 0.14, zm - 0.2));
    g.add(box(1.0, 0.12, 0.68, darkBrick, cx, yE + ch - 0.1, zm - 0.2));
    for (const dx of [-0.22, 0.22]) g.add(cylBetween(V(cx + dx, yE + ch + 0.15, zm - 0.2), V(cx + dx, yE + ch + 0.42, zm - 0.2), 0.08, new THREE.MeshStandardMaterial({ color: '#9c5a3c', roughness: 0.8 })));
  }
  // dakkapellen aan de voorkant, boven het hoofdraam
  if (opt.dormers !== false) {
    const tp = Math.tan(pitch * Math.PI / 180);
    anchors.units.forEach((au, i) => {
      const u = units[i];
      const fm = paintMaterial(u.dormerFrame ?? u.frame);
      const cheekMat = paintMaterial(u.dormerCheek ?? fasciaHex);
      let cx = au.main.x;
      const dw = 2.35, zD = -0.65;
      const yb = yE + (zf - zD) * tp, dh = 1.5, yt = yb + dh;
      const zt = zf - (yt + 0.2 - yE) / tp - 0.2;
      // niet op het schuine schilddeel zetten
      const hipX = (zf - zt) + 0.25;
      cx = Math.min(Math.max(cx, xL + hipX + dw / 2), xR - hipX - dw / 2);
      const len = zD - zt;
      const ct = 0.07;
      for (const sx of [-1, 1]) g.add(box(ct, dh + 0.35, len, cheekMat, cx + sx * (dw / 2 - ct / 2), yb - 0.35 + (dh + 0.35) / 2, zD - len / 2));
      const ww = 1.75, wh = 1.02, wy = yb + 0.24;
      const ft = 0.06, fz = zD - ft / 2;
      g.add(box((dw - ww) / 2, dh + 0.35, ft, cheekMat, cx - dw / 2 + (dw - ww) / 4, yb - 0.35 + (dh + 0.35) / 2, fz));
      g.add(box((dw - ww) / 2, dh + 0.35, ft, cheekMat, cx + dw / 2 - (dw - ww) / 4, yb - 0.35 + (dh + 0.35) / 2, fz));
      g.add(box(ww, wy - (yb - 0.35), ft, cheekMat, cx, (wy + yb - 0.35) / 2, fz));
      g.add(box(ww, yt - (wy + wh), ft, cheekMat, cx, (yt + wy + wh) / 2, fz));
      const win = makeWindow(ww, wh, fm, { cols: 2, topH: 0.3, topGrid: [3, 1], wallT: 0.06, reveal: 0.0, sillMat: zinc, sashMat: u.sash ? paintMaterial(u.sash) : fm });
      win.position.set(cx, wy, zD);
      g.add(win);
      // plat dak met overstek en boeideel
      const ov = 0.16;
      g.add(box(dw + ov * 2, 0.2, len + ov, fasciaMat, cx, yt + 0.1, zD - len / 2 + ov / 2));
      g.add(box(dw + ov * 2 + 0.02, 0.025, len + ov + 0.02, zinc, cx, yt + 0.21, zD - len / 2 + ov / 2));
    });
  }
  // zachte contactschaduw (nep-AO) op de grond langs de gevels
  {
    const c = document.createElement('canvas'); c.width = 4; c.height = 128;
    const x = c.getContext('2d');
    const gr = x.createLinearGradient(0, 0, 0, 128);
    gr.addColorStop(0, 'rgba(0,0,0,0.55)'); gr.addColorStop(0.35, 'rgba(0,0,0,0.18)'); gr.addColorStop(1, 'rgba(0,0,0,0)');
    x.fillStyle = gr; x.fillRect(0, 0, 4, 128);
    const t = new THREE.CanvasTexture(c);
    const aoMat = new THREE.MeshBasicMaterial({ map: t, transparent: true, depthWrite: false, polygonOffset: true, polygonOffsetFactor: -2 });
    const strip = (len, cx, cz, rot) => {
      const geo = new THREE.PlaneGeometry(len, 0.7);
      geo.rotateX(-Math.PI / 2);
      const m = new THREE.Mesh(geo, aoMat);
      m.position.set(cx, 0.075, cz);
      m.rotation.y = rot;
      m.renderOrder = 2;
      return m;
    };
    // PlaneGeometry: v=1 aan de -z-kant na rotatie; die kant tegen de muur
    g.add(strip(W, 0, 0.35, 0));
    g.add(strip(depth, -W / 2 - 0.35, -depth / 2, -Math.PI / 2));
    g.add(strip(depth, W / 2 + 0.35, -depth / 2, Math.PI / 2));
  }
  anchors.W = W; anchors.depth = depth; anchors.eaveH = eaveH; anchors.fasciaY = fy; anchors.zf = zf; anchors.xL = xL; anchors.xR = xR; anchors.yR = yR;
  g.userData = anchors;
  return g;
}

/* ------------------------------------------------------------------ */
/* Tuin en straat                                                       */
/* ------------------------------------------------------------------ */

export function ground(mat, w, d, x, z, y = 0) {
  const geo = new THREE.PlaneGeometry(w, d);
  geo.rotateX(-Math.PI / 2);
  geo.translate(x, y, z);
  // UV in meters
  const p = geo.attributes.position, uv = geo.attributes.uv;
  for (let i = 0; i < p.count; i++) uv.setXY(i, p.getX(i), -p.getZ(i));
  const m = new THREE.Mesh(geo, mat);
  m.receiveShadow = true;
  return m;
}

export function blob(radius, mat, seed = 1, detail = 4, squash = [1, 1, 1], amp = 0.28) {
  let geo = new THREE.IcosahedronGeometry(radius, detail);
  geo.deleteAttribute('uv'); geo.deleteAttribute('normal');
  geo = mergeVertices(geo);
  const p = geo.attributes.position;
  const v = new THREE.Vector3();
  for (let i = 0; i < p.count; i++) {
    v.fromBufferAttribute(p, i);
    const n = fbm(v.x * 1.6 / radius + seed, v.y * 1.6 / radius, v.z * 1.6 / radius, 4);
    const fine = noise3(v.x * 9 / radius, v.y * 9 / radius + seed, v.z * 9 / radius);
    v.multiplyScalar(1 + (n - 0.5) * amp * 2 + (fine - 0.5) * 0.08);
    v.set(v.x * squash[0], v.y * squash[1], v.z * squash[2]);
    p.setXYZ(i, v.x, v.y, v.z);
  }
  geo.computeVertexNormals();
  worldUV(geo);
  const m = new THREE.Mesh(geo, mat);
  m.castShadow = true; m.receiveShadow = true;
  return m;
}

// Gesnoeide haag: doos met vervormd, iets afgerond oppervlak.
export function hedge(w, h, d, mat, seed = 3) {
  const geo = new THREE.BoxGeometry(w, h, d, Math.max(2, Math.round(w * 10)), Math.round(h * 10), Math.round(d * 10));
  const p = geo.attributes.position;
  const v = new THREE.Vector3();
  for (let i = 0; i < p.count; i++) {
    v.fromBufferAttribute(p, i);
    // hoeken afronden
    const r = 0.12;
    const cx = Math.max(Math.abs(v.x) - (w / 2 - r), 0), cy = Math.max(v.y - (h / 2 - r), 0), cz = Math.max(Math.abs(v.z) - (d / 2 - r), 0);
    const k = Math.hypot(cx, cy, cz);
    if (k > r) { const f = r / k; v.x -= Math.sign(v.x) * cx * (1 - f); v.y -= cy * (1 - f); v.z -= Math.sign(v.z) * cz * (1 - f); }
    const n = fbm(v.x * 2.2 + seed, v.y * 2.2, v.z * 2.2, 4) - 0.5;
    const fine = noise3(v.x * 14, v.y * 14 + seed, v.z * 14) - 0.5;
    const s = 1 + n * 0.12 + fine * 0.05;
    if (v.y > -h / 2 + 0.01) { v.x *= 1 + (s - 1) * 0.6 / Math.max(w, 1); v.z += Math.sign(v.z) * (s - 1) * 0.3; v.y += (v.y > h / 2 - 0.15 ? (s - 1) * 0.5 : 0); }
    p.setXYZ(i, v.x, v.y + h / 2, v.z);
  }
  geo.computeVertexNormals();
  worldUV(geo);
  const m = new THREE.Mesh(geo, mat);
  m.castShadow = true; m.receiveShadow = true;
  return m;
}

// Bladkaartjes: kleine, alfa-geteste vlakjes met een tros blaadjes.
export function leafCardMaterial(opts = {}) {
  const { hue = 95, light = 30, sat = 45, seed = 1, small = false } = opts;
  const R = rng(seed);
  const S = 256, c = canvas(S, S), x = c.getContext('2d');
  const n = small ? 60 : 38;
  for (let i = 0; i < n; i++) {
    const a = R() * Math.PI * 2, r = Math.sqrt(R()) * 100;
    const px = 128 + Math.cos(a) * r, py = 128 + Math.sin(a) * r;
    const len = (small ? 9 : 16) + R() * (small ? 7 : 12), ang = R() * Math.PI * 2;
    const L = light * (0.55 + R() * 0.9);
    x.fillStyle = `hsl(${hue + (R() - 0.5) * 24},${sat + (R() - 0.5) * 20}%,${L}%)`;
    x.beginPath(); x.ellipse(px, py, len, len * 0.48, ang, 0, 7); x.fill();
    x.strokeStyle = `hsla(${hue},30%,${L * 0.6}%,0.6)`; x.lineWidth = 1.2;
    x.beginPath(); x.moveTo(px - Math.cos(ang) * len, py - Math.sin(ang) * len); x.lineTo(px + Math.cos(ang) * len, py + Math.sin(ang) * len); x.stroke();
  }
  if (opts.flowers) {
    for (let i = 0; i < 22; i++) {
      const a = R() * Math.PI * 2, r = Math.sqrt(R()) * 95;
      const px = 128 + Math.cos(a) * r, py = 128 + Math.sin(a) * r;
      for (let k = 0; k < 9; k++) {
        x.fillStyle = k % 3 ? opts.flowers : '#ffffff';
        x.globalAlpha = 0.85;
        x.beginPath(); x.arc(px + (R() - 0.5) * 16, py + (R() - 0.5) * 16, 3 + R() * 3, 0, 7); x.fill();
      }
      x.globalAlpha = 1;
    }
  }
  const t = tex(c, true);
  t.wrapS = t.wrapT = THREE.ClampToEdgeWrapping;
  return new THREE.MeshStandardMaterial({ map: t, alphaTest: 0.45, side: THREE.DoubleSide, roughness: 0.75, envMapIntensity: 0.5 });
}

const _q = new THREE.Quaternion(), _m = new THREE.Matrix4(), _s = new THREE.Vector3(), _n = new THREE.Vector3(), _z = new THREE.Vector3(0, 0, 1), _rq = new THREE.Quaternion();
function cards(points, size, mat) {
  const geo = new THREE.PlaneGeometry(size, size);
  const im = new THREE.InstancedMesh(geo, mat, points.length);
  points.forEach(([p, nrm, sc], i) => {
    _n.copy(nrm).normalize();
    _q.setFromUnitVectors(_z, _n);
    _rq.setFromAxisAngle(_n, Math.random() * Math.PI * 2);
    _q.premultiply(_rq);
    _s.set(sc, sc, sc);
    _m.compose(p, _q, _s);
    im.setMatrixAt(i, _m);
  });
  im.castShadow = true; im.receiveShadow = true;
  return im;
}

/** Bladermassa uit een paar trossen: een donkere kern plus duizenden bladkaartjes. */
export function foliage(clusters, center, opts) {
  const { mat, coreMat, count = 3000, size = 0.5, seed = 1, jitter = 0.55 } = opts;
  const R = rng(seed);
  const g = new THREE.Group();
  const pts = [];
  const total = clusters.reduce((a, c) => a + c.r * c.r, 0);
  for (const cl of clusters) {
    const core = blob(cl.r * 0.82, coreMat, seed + cl.r, 2, [1, 0.9, 1], 0.2);
    core.position.copy(cl.c);
    g.add(core);
    const k = Math.round(count * cl.r * cl.r / total);
    for (let i = 0; i < k; i++) {
      const d = new THREE.Vector3(R() * 2 - 1, R() * 2 - 1, R() * 2 - 1).normalize();
      const rr = cl.r * (0.72 + 0.32 * Math.pow(R(), 0.5));
      const p = cl.c.clone().addScaledVector(d, rr);
      const outward = p.clone().sub(center).normalize().multiplyScalar(0.6).add(d.clone().multiplyScalar(0.4));
      outward.add(new THREE.Vector3(R() - 0.5, R() - 0.5, R() - 0.5).multiplyScalar(jitter * 2));
      pts.push([p, outward, 0.7 + R() * 0.6]);
    }
  }
  g.add(cards(pts, size, mat));
  return g;
}

export function tree(x, z, height, mat, trunkMat, seed = 1, coreMat) {
  const g = new THREE.Group();
  const R = rng(seed);
  const V = (a, b, c) => new THREE.Vector3(a, b, c);
  const top = V((R() - 0.5) * 0.4, height * 0.55, (R() - 0.5) * 0.4);
  g.add(cylBetween(V(0, 0, 0), top, height * 0.028, trunkMat, 10));
  for (let i = 0; i < 5; i++) {
    const a = R() * Math.PI * 2;
    g.add(cylBetween(V(0, height * (0.4 + R() * 0.15), 0), V(Math.cos(a) * height * 0.22, height * (0.62 + R() * 0.1), Math.sin(a) * height * 0.22), height * 0.012, trunkMat, 6));
  }
  const cw = height * 0.32, cy = height * 0.6;
  const clusters = [{ c: V(0, cy, 0), r: height * 0.24 }];
  for (let i = 0; i < 9; i++) {
    const a = R() * Math.PI * 2, r = 0.5 + R() * 0.5;
    clusters.push({ c: V(Math.cos(a) * r * cw, cy + (R() - 0.4) * height * 0.28, Math.sin(a) * r * cw), r: height * (0.11 + R() * 0.07) });
  }
  const center = V(0, cy, 0);
  const area = clusters.reduce((a, c) => a + c.r * c.r, 0);
  g.add(foliage(clusters, center, { mat, coreMat: coreMat ?? darkLeaf(), count: Math.round(area * 75), size: 0.55, seed }));
  g.position.set(x, 0, z);
  return g;
}

let _darkLeaf;
function darkLeaf() {
  return _darkLeaf ??= new THREE.MeshStandardMaterial({ color: '#203a17', roughness: 0.95 });
}

export function shrub(x, z, r, mat, seed = 1) {
  const V = (a, b, c) => new THREE.Vector3(a, b, c);
  const R = rng(seed);
  const clusters = [{ c: V(0, r * 0.75, 0), r: r * 0.85 }];
  for (let i = 0; i < 4; i++) {
    const a = R() * Math.PI * 2;
    clusters.push({ c: V(Math.cos(a) * r * 0.45, r * (0.55 + R() * 0.4), Math.sin(a) * r * 0.45), r: r * (0.45 + R() * 0.2) });
  }
  const g = foliage(clusters, V(0, r * 0.6, 0), { mat, coreMat: darkLeaf(), count: Math.round(r * r * 900), size: 0.2, seed });
  g.position.set(x, 0, z);
  return g;
}

/** Geschoren haag met bladkaartjes op het oppervlak. */
export function leafyHedge(w, h, d, mat, coreMat, seed = 1) {
  const R = rng(seed);
  const g = new THREE.Group();
  const core = hedge(w - 0.06, h - 0.04, d - 0.06, coreMat, seed);
  g.add(core);
  const pts = [];
  const dens = 260;
  const faces = [
    [w * d, (p) => p.set((R() - 0.5) * w, h, (R() - 0.5) * d), new THREE.Vector3(0, 1, 0)],
    [w * h, (p) => p.set((R() - 0.5) * w, R() * h, d / 2), new THREE.Vector3(0, 0, 1)],
    [w * h, (p) => p.set((R() - 0.5) * w, R() * h, -d / 2), new THREE.Vector3(0, 0, -1)],
    [d * h, (p) => p.set(w / 2, R() * h, (R() - 0.5) * d), new THREE.Vector3(1, 0, 0)],
    [d * h, (p) => p.set(-w / 2, R() * h, (R() - 0.5) * d), new THREE.Vector3(-1, 0, 0)],
  ];
  for (const [area, sample, nrm] of faces) {
    const n = Math.round(area * dens);
    for (let i = 0; i < n; i++) {
      const p = sample(new THREE.Vector3());
      p.addScaledVector(nrm, (R() - 0.6) * 0.07);
      const o = nrm.clone().add(new THREE.Vector3(R() - 0.5, R() - 0.5, R() - 0.5).multiplyScalar(1.1));
      pts.push([p, o, 0.7 + R() * 0.6]);
    }
  }
  g.add(cards(pts, 0.16, mat));
  return g;
}

/* ------------------------------------------------------------------ */
/* Maatlijnen                                                           */
/* ------------------------------------------------------------------ */

const lineMat = new THREE.MeshBasicMaterial({ color: '#ffffff', toneMapped: false, transparent: true, opacity: 0.92 });

function labelSprite(text, scale = 0.5) {
  const c = canvas(512, 160), x = c.getContext('2d');
  x.font = '600 76px "Helvetica Neue", Helvetica, Arial, sans-serif';
  const tw = x.measureText(text).width;
  const w = tw + 70, h = 112, x0 = (512 - w) / 2, y0 = (160 - h) / 2;
  x.shadowColor = 'rgba(0,0,0,0.25)'; x.shadowBlur = 10; x.shadowOffsetY = 3;
  x.fillStyle = '#ffffff';
  x.beginPath(); x.roundRect(x0, y0, w, h, h / 2); x.fill();
  x.shadowColor = 'transparent';
  x.fillStyle = '#f4820b';
  x.beginPath(); x.arc(x0 + 34, 80, 9, 0, 7); x.fill();
  x.fillStyle = '#2b2116';
  x.textBaseline = 'middle';
  x.fillText(text, x0 + 52, 83);
  const t = new THREE.CanvasTexture(c);
  t.colorSpace = THREE.SRGBColorSpace;
  t.anisotropy = MAX_ANISO;
  const s = new THREE.Sprite(new THREE.SpriteMaterial({ map: t, toneMapped: false, depthTest: false, transparent: true }));
  s.scale.set(scale * 512 / 160, scale, 1);
  s.renderOrder = 10;
  return s;
}

// Maatlijn tussen a en b met eindstreepjes (loodrecht, richting 'tick') en een labeltje.
export function dimension(a, b, text, tick, labelOffset = new THREE.Vector3(), scale = 0.5) {
  const g = new THREE.Group();
  const t = 0.022;
  const mk = (p, q) => {
    const len = p.distanceTo(q);
    const m = new THREE.Mesh(new THREE.BoxGeometry(t, len, t), lineMat);
    m.position.copy(p).add(q).multiplyScalar(0.5);
    m.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), q.clone().sub(p).normalize());
    m.renderOrder = 5;
    return m;
  };
  g.add(mk(a, b));
  const tk = tick.clone().normalize().multiplyScalar(0.13);
  for (const p of [a, b]) g.add(mk(p.clone().sub(tk), p.clone().add(tk)));
  // kleine pijlpunten (schuine streepjes, architectennotatie)
  const dir = b.clone().sub(a).normalize();
  for (const p of [a, b]) {
    const sl = dir.clone().add(tick.clone().normalize()).normalize().multiplyScalar(0.07);
    g.add(mk(p.clone().sub(sl), p.clone().add(sl)));
  }
  const lab = labelSprite(text, scale);
  lab.position.copy(a).add(b).multiplyScalar(0.5).add(labelOffset);
  g.add(lab);
  return g;
}

/* ------------------------------------------------------------------ */
/* Export                                                               */
/* ------------------------------------------------------------------ */

function shrinkTo(src, w, h) {
  const c = canvas(w, h), x = c.getContext('2d');
  x.imageSmoothingEnabled = true; x.imageSmoothingQuality = 'high';
  x.drawImage(src, 0, 0, w, h);
  return c;
}

async function encode(c, maxBytes = 180 * 1024) {
  let q = 0.85, data;
  for (;;) {
    data = c.toDataURL('image/webp', q);
    const bytes = Math.round((data.length - data.indexOf(',') - 1) * 0.75);
    if (bytes <= maxBytes || q <= 0.35) return { data, q, bytes };
    q = Math.round((q - 0.05) * 100) / 100;
  }
}

export function installExport(renderer, base) {
  installCrop(renderer);
  window.exportAll = async () => {
    const c1600 = shrinkTo(renderer.domElement, 1600, 1100);
    const c800 = shrinkTo(c1600, 800, 550);
    const c400 = shrinkTo(c800, 400, 275);
    const out = [];
    for (const [c, w] of [[c1600, 1600], [c800, 800], [c400, 400]]) {
      const { data, q, bytes } = await encode(c);
      const name = `${base}-${w}.webp`;
      const r = await fetch('/save', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ name, data }) });
      out.push({ name, q, bytes, ok: (await r.json()).ok });
    }
    return out;
  };
}

// Hulpje bij het afstellen: uitsnede (in renderpixels) opslaan als debug-crop.webp
export function installCrop(renderer) {
  window.crop = async (x, y, w, h) => {
    const c = canvas(w, h);
    c.getContext('2d').drawImage(renderer.domElement, x, y, w, h, 0, 0, w, h);
    const data = c.toDataURL('image/webp', 0.9);
    await fetch('/save', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ name: 'debug-crop.webp', data }) });
    return 'ok';
  };
}

export function pageStyle() {
  const s = document.createElement('style');
  s.textContent = 'html,body{margin:0;background:#222;height:100%;display:flex;align-items:center;justify-content:center}canvas{max-width:100vw;max-height:100vh;width:auto!important;height:auto!important;aspect-ratio:1600/1100}';
  document.head.appendChild(s);
}
