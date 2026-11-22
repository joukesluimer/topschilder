// Voortuin, stoep en straat rond een woningblok (gedeeld door de render-scènes).
import * as C from './a-common.js';
const { THREE } = C;

let cache = null;
function mats() {
  if (cache) return cache;
  cache = {
    grass: C.grassMaterial(5),
    tiles: C.pavingMaterial({ tile: 0.3, n: 4, hex: [158, 152, 142], seed: 11 }),
    path: C.pavingMaterial({ tile: 0.3, n: 4, hex: [176, 160, 140], seed: 12, joint: '#8e8070' }),
    curb: C.concreteMaterial('#c9c4b8', 1.0, 21, 0.85),
    asphalt: C.asphaltMaterial(),
    hedge: C.leafCardMaterial({ hue: 92, light: 30, seed: 9, small: true }),
    hedgeCore: C.leafMaterial({ hue: 95, light: 18, seed: 9, size: 0.7 }),
    shrub: C.leafCardMaterial({ hue: 105, light: 27, seed: 19, small: true }),
    shrub2: C.leafCardMaterial({ hue: 82, light: 33, seed: 29, small: true }),
    bloom: C.leafCardMaterial({ hue: 100, light: 28, seed: 59, small: true, flowers: '#d98fb0' }),
    bloom2: C.leafCardMaterial({ hue: 95, light: 28, seed: 69, small: true, flowers: '#f2efe6' }),
    tree: C.leafCardMaterial({ hue: 86, light: 30, seed: 39 }),
    tree2: C.leafCardMaterial({ hue: 100, light: 25, seed: 49 }),
    trunk: new THREE.MeshStandardMaterial({ color: '#5a4a3c', roughness: 0.9 }),
    soil: C.concreteMaterial('#4a3b2e', 0.8, 5, 1),
  };
  return cache;
}

/**
 * opts.gardenDepth: diepte voortuin; opts.doors: x-posities van paden;
 * opts.extentX: hoe ver gras/stoep links en rechts doorlopen.
 */
export function buildSite(scene, a, opts = {}) {
  const M = mats();
  const gd = opts.gardenDepth ?? 6.2;
  const ext = opts.extentX ?? 40;
  const doors = opts.doors ?? a.units.map((u) => u.door.x);
  const swD = 1.9; // stoepbreedte
  // ondergrond: gras overal achter de stoep
  scene.add(C.ground(M.grass, ext * 2, 60, 0, -30 + gd, 0.0));
  // stoep, band, straat
  scene.add(C.ground(M.tiles, ext * 2, swD, 0, gd + swD / 2, 0.06));
  scene.add(C.box(ext * 2, 0.08, swD, M.tiles, 0, 0.02, gd + swD / 2, { cast: false, worldUV: false }));
  scene.add(C.box(ext * 2, 0.14, 0.15, M.curb, 0, 0.0, gd + swD + 0.075, { cast: false }));
  scene.add(C.ground(M.asphalt, ext * 2, 40, 0, gd + swD + 0.15 + 20, -0.06));
  // tuinpaden naar de voordeuren + strook tegels langs de gevel
  for (const x of doors) {
    scene.add(C.ground(M.path, 1.25, gd, x, gd / 2, 0.025));
    scene.add(C.box(1.33, 0.05, gd, M.curb, x, 0.0, gd / 2, { cast: false }));
  }
  scene.add(C.ground(M.path, a.W + 0.0, 0.6, 0, 0.3, 0.022));
  // borders met aarde langs de gevel
  // lage ligusterhaag langs de stoep, onderbroken bij de paden
  const hH = opts.hedgeH ?? 0.7, hD = 0.55, hz = gd - 0.45;
  const xs = [-ext, ...doors.flatMap((x) => [x - 0.75, x + 0.75]), ext].sort((p, q) => p - q);
  for (let i = 0; i < xs.length; i += 2) {
    const x0 = Math.max(xs[i], -a.W / 2 - 9), x1 = Math.min(xs[i + 1], a.W / 2 + 9);
    if (x1 - x0 < 0.3) continue;
    const h = C.leafyHedge(x1 - x0, hH, hD, M.hedge, M.hedgeCore, i + 1);
    h.position.set((x0 + x1) / 2, 0, hz);
    scene.add(h);
  }
  // struiken bij de hoeken en langs de gevel
  const R = C.rng(opts.seed ?? 77);
  const shrubs = opts.shrubs ?? [
    [-a.W / 2 - 0.9, 1.0, 0.85], [a.W / 2 + 0.9, 1.0, 0.8],
    [-a.W / 2 + 2.6, 1.1, 0.45], [a.W / 2 - 2.6, 1.1, 0.45],
    [-0.9, 1.0, 0.5], [0.9, 1.0, 0.5],
  ];
  shrubs.forEach(([x, z, r], i) => {
    const mat = [M.shrub, M.shrub2, M.bloom, M.shrub2, M.bloom2, M.shrub][i % 6];
    scene.add(C.shrub(x, z, r, mat, 3 + i));
  });
  // bomen achter en naast het huis
  const trees = opts.trees ?? [
    [-a.W / 2 - 6, -6, 9.5], [-a.W / 2 - 2, -14, 11], [a.W / 2 + 5, -9, 10], [3, -17, 12], [-10, -22, 12], [a.W / 2 + 12, -4, 8.5],
  ];
  trees.forEach(([x, z, h], i) => scene.add(C.tree(x, z, h, i % 2 ? M.tree : M.tree2, M.trunk, 11 + i)));
  // bomenrij in de verte (achtertuinen, park) met een lage bosrand ervoor
  if (opts.backTrees !== false) {
    const belt = C.hedge(110, 2.6, 3, M.hedgeCore, 77);
    belt.position.set(0, 0, -24);
    scene.add(belt);
    const RS = C.rng(321);
    for (let i = 0; i < 22; i++) scene.add(C.shrub(-50 + i * 4.6 + RS() * 2, -22.2 - RS() * 1.5, 1.4 + RS() * 1.2, RS() < 0.5 ? M.shrub : M.shrub2, 400 + i));
    const RB = C.rng(123);
    for (let i = 0; i < 16; i++) {
      const x = -45 + i * 6 + (RB() - 0.5) * 3, z = -26 - RB() * 14, h = 9 + RB() * 6;
      scene.add(C.tree(x, z, h, RB() < 0.5 ? M.tree : M.tree2, M.trunk, 200 + i));
    }
  }
  // erfafscheiding: hoge haag aan de zijkanten, achter de rooilijn
  for (const s of [-1, 1]) {
    const hh = C.leafyHedge(0.6, 1.7, a.depth + 4, M.hedge, M.hedgeCore, 30 + s);
    hh.rotation.y = 0;
    hh.position.set(s * (a.W / 2 + 3.2), 0, -a.depth / 2 - 1);
    scene.add(hh);
  }
}
