/**
 * Scaledex diorama: two random Kanto Scale World figures on a small grass slab.
 *
 * Built on the Diorama kit (https://github.com/sloemo01/diorama, MIT, see
 * LICENSE-diorama.txt): camera.js, orbit.js, lighting.js, post.js (classic
 * pixel preset), geometry.js and detail.js are copied from its templates.
 *
 * Units are centimetres of the real figure, so the two Pokémon stand at their
 * true 1/20 heights next to each other. Figures are flat photo cut-outs that
 * always face the camera (the kit's "flat cut-out against white paper").
 * The scene is a pure function of t: hops and grass sway, nothing random per frame.
 */
import * as THREE from 'three';
import { CAMERA, createCamera, updateCamera } from './camera.js';
import { createDioramaOrbit } from './orbit.js';
import { createLighting } from './lighting.js';
import { PixelPost } from './post.js';
import { C, FIGURE_SLOTS, medianCut, buildPalette } from './palette.js';
import { roundedBoxGeometry, mulberry32 } from './geometry.js';
import { mesh, contactShadow } from './detail.js';

const SLAB = { hx: 10.5, hz: 7, grass: 0.35, soil: 1.25 };

const mat = (hex, opts = {}) => new THREE.MeshStandardMaterial({ color: hex, roughness: 0.92, metalness: 0, flatShading: true, ...opts });

function buildSlab(scene) {
  const g = new THREE.Group();
  const { hx, hz, grass, soil } = SLAB;
  const top = mesh(g, roundedBoxGeometry(hx * 2, grass, hz * 2, 0.12, 2), mat(C.grass2), 0, -grass / 2, 0, { castShadow: false });
  top.receiveShadow = true;
  mesh(g, roundedBoxGeometry(hx * 2 - 0.08, soil, hz * 2 - 0.08, 0.1, 2), mat(C.soil2), 0, -grass - soil / 2 + 0.02, 0, { castShadow: false });
  // two strata bands on the soil face
  mesh(g, new THREE.BoxGeometry(hx * 2 - 0.02, 0.12, hz * 2 - 0.02), mat(C.soil1), 0, -grass - 0.38, 0, { castShadow: false });
  mesh(g, new THREE.BoxGeometry(hx * 2 - 0.02, 0.1, hz * 2 - 0.02), mat(C.soil3), 0, -grass - 0.9, 0, { castShadow: false });

  const rand = mulberry32(151);
  // dirt path: overlapping flat discs crossing the slab front-left to back-right
  const pathMat = mat(C.soil0);
  for (let i = 0; i <= 14; i++) {
    const u = i / 14;
    const x = -hx + 0.8 + u * (hx * 2 - 1.6);
    const z = Math.sin(u * Math.PI * 1.3 + 0.4) * 2.6 + 1.2 - u * 2.4;
    const r = 1.05 + rand() * 0.35;
    const d = mesh(g, new THREE.CylinderGeometry(r, r, 0.04, 14), pathMat, x, 0.02, z, { castShadow: false });
    d.scale.z = 0.7;
  }
  // stepping stones on the path
  const stoneMat = mat(C.stone0);
  for (let i = 0; i < 6; i++) {
    const u = 0.08 + i * 0.16;
    const x = -hx + 0.8 + u * (hx * 2 - 1.6);
    const z = Math.sin(u * Math.PI * 1.3 + 0.4) * 2.6 + 1.2 - u * 2.4;
    const s = mesh(g, new THREE.CylinderGeometry(0.42, 0.48, 0.12, 7), stoneMat, x + (rand() - 0.5) * 0.4, 0.07, z + (rand() - 0.5) * 0.4);
    s.rotation.y = rand() * Math.PI;
  }
  // rocks
  const rockMats = [mat(C.stone1), mat(C.stone2)];
  for (const [x, z, s] of [[-8.6, -5.2, 1.0], [-7.6, -5.8, 0.6], [8.9, 5.3, 0.8], [7.4, -5.6, 0.55], [-9.2, 4.9, 0.5]]) {
    const r = mesh(g, new THREE.DodecahedronGeometry(s, 0), rockMats[Math.floor(rand() * 2)], x, s * 0.45, z);
    r.scale.y = 0.7;
    r.rotation.set(rand(), rand() * 3, rand());
  }
  // trees in the two back corners
  const trunk = mat(C.wood), leafA = mat(C.leaf), leafB = mat(C.grass3);
  for (const [x, z, s] of [[-8.3, -4.6, 1.0], [8.4, -3.2, 0.8]]) {
    mesh(g, new THREE.CylinderGeometry(0.28 * s, 0.4 * s, 4.2 * s, 7), trunk, x, 2.1 * s, z);
    mesh(g, new THREE.IcosahedronGeometry(2.0 * s, 0), leafA, x, 5.0 * s, z);
    mesh(g, new THREE.IcosahedronGeometry(1.4 * s, 0), leafB, x + 0.9 * s, 6.3 * s, z + 0.4 * s);
    mesh(g, new THREE.IcosahedronGeometry(1.2 * s, 0), leafB, x - 1.0 * s, 5.9 * s, z - 0.3 * s);
  }
  // grass tufts and flowers (swayed in update)
  const tufts = [];
  const tuftMats = [mat(C.grass3), mat(C.grass4), mat(C.grass1)];
  const flowerMats = [mat(C.red), mat(C.yellow), mat(C.pink), mat(C.paper)];
  for (let i = 0; i < 46; i++) {
    const x = (rand() * 2 - 1) * (hx - 0.6);
    const z = (rand() * 2 - 1) * (hz - 0.6);
    if (Math.abs(z - (Math.sin(((x + hx) / (2 * hx)) * Math.PI * 1.3 + 0.4) * 2.6 + 1.2 - ((x + hx) / (2 * hx)) * 2.4)) < 1.3) continue;
    if (Math.abs(x) < 6 && z > -2.5 && z < 3.5) continue; // keep the figures' stage clear
    const tuft = new THREE.Group();
    tuft.position.set(x, 0, z);
    const m = tuftMats[i % 3];
    for (let k = 0; k < 3; k++) {
      const b = mesh(tuft, new THREE.ConeGeometry(0.12, 0.7 + rand() * 0.5, 4), m, (k - 1) * 0.12, 0.35, (rand() - 0.5) * 0.15);
      b.rotation.z = (k - 1) * 0.35;
    }
    if (i % 4 === 0) mesh(tuft, new THREE.IcosahedronGeometry(0.17, 0), flowerMats[(i >> 2) % 4], 0, 0.95, 0);
    g.add(tuft);
    tufts.push({ obj: tuft, ph: rand() * 6.28 });
  }
  scene.add(g);
  return { group: g, tufts };
}

/** Try each URL in turn (local copy, original host, Scaledex photo). */
async function loadFirst(urls) {
  let err;
  for (const u of urls) {
    try { return await loadFigure(u); } catch (e) { err = e; }
  }
  throw err;
}

/**
 * Load a figure image, turn a white studio background into alpha (flood fill
 * from the border; transparent PNG sprites pass through) and crop to the
 * opaque bounding box so the plane height equals the figure height.
 */
function loadFigure(url) {
  return new Promise((resolve, reject) => {
    const img = new Image();
    img.crossOrigin = 'anonymous';
    img.onload = () => {
      const scale = Math.min(1, 512 / img.naturalHeight);
      const w = Math.max(2, Math.round(img.naturalWidth * scale));
      const h = Math.max(2, Math.round(img.naturalHeight * scale));
      const cv = document.createElement('canvas');
      cv.width = w; cv.height = h;
      const ctx = cv.getContext('2d', { willReadFrequently: true });
      ctx.drawImage(img, 0, 0, w, h);
      const id = ctx.getImageData(0, 0, w, h);
      const d = id.data;
      const bg = (i) => {
        const r = d[i], gg = d[i + 1], b = d[i + 2];
        return r > 228 && gg > 228 && b > 228 && Math.max(r, gg, b) - Math.min(r, gg, b) < 20;
      };
      const seen = new Uint8Array(w * h);
      const stack = [];
      for (let x = 0; x < w; x++) { stack.push(x, (h - 1) * w + x); }
      for (let y = 0; y < h; y++) { stack.push(y * w, y * w + w - 1); }
      while (stack.length) {
        const p = stack.pop();
        if (seen[p]) continue;
        seen[p] = 1;
        if (!bg(p * 4)) continue;
        d[p * 4 + 3] = 0;
        const x = p % w, y = (p / w) | 0;
        if (x > 0) stack.push(p - 1);
        if (x < w - 1) stack.push(p + 1);
        if (y > 0) stack.push(p - w);
        if (y < h - 1) stack.push(p + w);
      }
      let x0 = w, y0 = h, x1 = -1, y1 = -1;
      for (let y = 0; y < h; y++) for (let x = 0; x < w; x++) {
        if (d[(y * w + x) * 4 + 3] > 24) { if (x < x0) x0 = x; if (x > x1) x1 = x; if (y < y0) y0 = y; if (y > y1) y1 = y; }
      }
      if (x1 < 0) { reject(new Error('empty ' + url)); return; }
      ctx.putImageData(id, 0, 0);
      const cw = x1 - x0 + 1, ch = y1 - y0 + 1;
      const out = document.createElement('canvas');
      out.width = cw; out.height = ch;
      out.getContext('2d').drawImage(cv, x0, y0, cw, ch, 0, 0, cw, ch);
      const samples = [];
      const step = Math.max(1, Math.floor((w * h) / 4000));
      for (let p = 0; p < w * h; p += step) {
        if (d[p * 4 + 3] > 128) samples.push(d[p * 4], d[p * 4 + 1], d[p * 4 + 2]);
      }
      resolve({ canvas: out, aspect: cw / ch, samples });
    };
    img.onerror = () => reject(new Error('image ' + url));
    img.src = url;
  });
}

function makeFigure(fig, info) {
  const tex = new THREE.CanvasTexture(info.canvas);
  tex.colorSpace = THREE.SRGBColorSpace;
  tex.anisotropy = 4;
  const h = fig.h, w = h * info.aspect;
  const plane = new THREE.Mesh(
    new THREE.PlaneGeometry(w, h),
    new THREE.MeshBasicMaterial({ map: tex, alphaTest: 0.5, side: THREE.DoubleSide, toneMapped: false })
  );
  plane.position.y = h / 2;
  const group = new THREE.Group();
  group.add(plane);
  return { group, plane, w, h, tex };
}

/**
 * `pair`: optional fixed cast [{n, ja, dex, h, img: [url, ...]}]; without it two
 * random characters are drawn from `data` and the roll button draws again.
 */
export function startDiorama({ canvas, data, pair: fixedPair, namesEl, rollBtn, resetBtn, statusEl }) {
  const renderer = new THREE.WebGLRenderer({ canvas, antialias: false, alpha: true });
  renderer.setPixelRatio(1);
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFShadowMap;
  renderer.outputColorSpace = THREE.LinearSRGBColorSpace;
  renderer.toneMapping = THREE.NoToneMapping;

  const scene = new THREE.Scene();
  scene.background = null;
  createLighting(renderer, scene);
  const slab = buildSlab(scene);

  let cast = [];
  let k = 1; // scenery scale: the slab and props shrink or grow with the pair
  const post = new PixelPost(renderer, 1600, 1);
  const camera = createCamera(16 / 9, fitPoints([]));
  const orbit = createDioramaOrbit(camera, canvas, { target: CAMERA.target, minDistance: 10, maxDistance: 400 });
  orbit.controls.enableZoom = false; // page scroll must keep working over the canvas

  let t0 = performance.now();
  let busy = false;

  function fitPoints(figs) {
    const hx = SLAB.hx * k, hz = SLAB.hz * k, depth = (SLAB.grass + SLAB.soil) * k;
    const pts = [];
    for (const y of [0, -depth]) for (const [x, z] of [[-hx, -hz], [hx, -hz], [hx, hz], [-hx, hz]]) pts.push(new THREE.Vector3(x, y, z));
    pts.push(new THREE.Vector3(-8.3 * k, 7.5 * k, -4.6 * k));
    for (const f of figs) {
      const p = f.group.position;
      for (const dx of [-f.w / 2, f.w / 2]) pts.push(new THREE.Vector3(p.x + dx, f.h + 0.4, p.z));
    }
    return pts;
  }

  function aspect() {
    const r = canvas.getBoundingClientRect();
    return Math.max(0.3, r.width / Math.max(1, r.height));
  }

  function solveHero() {
    const maxH = Math.max(4, ...cast.map((f) => f.h));
    CAMERA.target.set(0, maxH * 0.3, 0.4 * k);
    updateCamera(camera, aspect(), fitPoints(cast));
    orbit.controls.target.copy(CAMERA.target);
    orbit.heroTarget.copy(CAMERA.target);
    orbit.heroPosition.copy(camera.position);
    orbit.controls.update();
  }

  function resize() {
    const r = canvas.getBoundingClientRect();
    post.setSize(Math.max(2, Math.round(r.width)), Math.max(2, Math.round(r.height)));
    solveHero();
  }

  function pickPair() {
    const byChar = new Map();
    for (const f of data) {
      if (!byChar.has(f.cid)) byChar.set(f.cid, []);
      byChar.get(f.cid).push(f);
    }
    const chars = [...byChar.values()];
    const a = Math.floor(Math.random() * chars.length);
    let b = Math.floor(Math.random() * (chars.length - 1));
    if (b >= a) b++;
    const one = (list) => list[Math.floor(Math.random() * list.length)];
    return [one(chars[a]), one(chars[b])];
  }

  async function roll() {
    if (busy) return;
    busy = true;
    if (rollBtn) rollBtn.disabled = true;
    if (statusEl) statusEl.textContent = 'Đang tải…';
    try {
      const pair = fixedPair || pickPair();
      const infos = await Promise.all(pair.map((f) => loadFirst([].concat(f.img))));
      for (const f of cast) { scene.remove(f.group); scene.remove(f.shadow); f.tex.dispose(); f.plane.geometry.dispose(); f.plane.material.dispose(); }
      cast = pair.map((f, i) => Object.assign(makeFigure(f, infos[i]), { data: f }));
      // stand side by side with a small gap, the taller one a little further back
      const [A, B] = cast;
      // scenery follows the pair: wide enough for both, tall props around the taller one
      k = Math.min(2.2, Math.max(0.28, (A.w + B.w) / 11, Math.max(A.h, B.h) / 6.5));
      slab.group.scale.setScalar(k);
      const gap = 0.9 * k;
      A.group.position.set(-(gap / 2 + A.w / 2), 0, (A.h >= B.h ? -0.6 : 0.9) * k);
      B.group.position.set(gap / 2 + B.w / 2, 0, (B.h > A.h ? -0.6 : 0.9) * k);
      for (const f of cast) {
        scene.add(f.group);
        f.shadow = contactShadow(scene, f.group.position.x, 0, f.group.position.z, 1, 0.55);
        f.shadow.scale.set(f.w * 0.95, Math.max(0.8, f.w * 0.4), 1);
        f.phase = cast.indexOf(f) * 2.1; // deterministic: the scene is a function of t
      }
      // palette: fixed scene ramps + colours from both photos
      const samples = infos.flatMap((x) => x.samples);
      const pal = buildPalette(medianCut(samples, FIGURE_SLOTS));
      post.uniforms.uPalette.value = pal.map((c) => new THREE.Vector3(c[0], c[1], c[2]));
      t0 = performance.now();
      solveHero();
      if (namesEl) {
        namesEl.innerHTML = pair.map((f) => '<b>#' + String(f.dex).padStart(3, '0') + ' ' + f.n + '</b> <small>' + f.ja + ' · ' + f.h + ' cm</small>').join(' &nbsp;vs&nbsp; ');
      }
      if (statusEl) statusEl.textContent = '';
    } catch (e) {
      if (statusEl) statusEl.textContent = 'Không tải được ảnh, thử lại nhé.';
    } finally {
      busy = false;
      if (rollBtn) rollBtn.disabled = false;
    }
  }

  function update(t) {
    for (const f of cast) {
      // small idle hop every ~2.6 s, scaled to the figure
      const s = Math.sin((t / 2.6) * Math.PI * 2 + f.phase);
      const hop = Math.pow(Math.max(0, s), 6) * Math.min(0.6, 0.08 * f.h + 0.1);
      f.plane.position.y = f.h / 2 + hop;
      const k = 1 - hop / (f.h * 0.6 + 0.6);
      f.shadow.material.opacity = 0.55 * k;
      // cylindrical billboard: always face the camera around the vertical axis
      const p = f.group.position;
      f.group.rotation.y = Math.atan2(camera.position.x - p.x, camera.position.z - p.z);
    }
    for (const tf of slab.tufts) tf.obj.rotation.z = Math.sin(t * 1.3 + tf.ph) * 0.06;
  }

  let visible = true;
  let raf = 0;
  function frame() {
    raf = 0;
    if (!visible) return;
    update((performance.now() - t0) / 1000);
    post.render(scene, camera);
    raf = requestAnimationFrame(frame);
  }
  function play() { if (!raf && visible) raf = requestAnimationFrame(frame); }

  new IntersectionObserver((es) => { visible = es[0].isIntersecting; play(); }).observe(canvas);
  new ResizeObserver(resize).observe(canvas);
  if (rollBtn) rollBtn.addEventListener('click', roll);
  if (resetBtn) resetBtn.addEventListener('click', () => orbit.reset());

  resize();
  roll();
  play();
  return { roll, reset: orbit.reset };
}
