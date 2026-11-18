/**
 * Scaledex diorama palette (64 entries, the length the PixelPost shader declares).
 *
 * 24 fixed scene entries (paper, grass, soil, stone, wood, flowers, ink) plus
 * 40 entries that are re-extracted from the two figure photos every time a new
 * pair is drawn, so a yellow Pikachu or a purple Gengar keeps its colours after
 * the palette snap. Scene materials only use the fixed `C` colours below.
 */
export const C = {
  paper: '#ffffff',
  cream: '#f3eddf',
  grass0: '#d7ec9a', grass1: '#a9d46a', grass2: '#7fb84a', grass3: '#5a9a35', grass4: '#3c7426',
  soil0: '#c9a678', soil1: '#a57f55', soil2: '#7f5d3c', soil3: '#5c4029', soil4: '#3d2a1c',
  stone0: '#e1ddd3', stone1: '#bdb8ad', stone2: '#938f86', stone3: '#6b6862',
  wood: '#8a5a34', leaf: '#4f8f3a',
  red: '#e2493b', yellow: '#f4cf3c', pink: '#f29bb7',
  ink0: '#2c2a26', ink1: '#14130f',
};

export const SCENE_HEX = Object.values(C);
export const FIGURE_SLOTS = 64 - SCENE_HEX.length;

const hexToRgb = (hex) => {
  const n = parseInt(hex.slice(1), 16);
  return [((n >> 16) & 255) / 255, ((n >> 8) & 255) / 255, (n & 255) / 255];
};

// Neutral greys fill the figure slots until the first pair is analysed.
const FILL = Array.from({ length: FIGURE_SLOTS }, (_, i) => {
  const v = Math.round(40 + (i / (FIGURE_SLOTS - 1)) * 200).toString(16).padStart(2, '0');
  return '#' + v + v + v;
});

export const PALETTE_HEX = SCENE_HEX.concat(FILL);
export const PALETTE_RGB = PALETTE_HEX.map(hexToRgb);

/**
 * Median-cut quantisation of opaque figure pixels into `count` sRGB colours.
 * `pixels` is a flat [r,g,b, r,g,b, ...] array of 0..255 values.
 */
export function medianCut(pixels, count) {
  const pts = [];
  for (let i = 0; i < pixels.length; i += 3) pts.push([pixels[i], pixels[i + 1], pixels[i + 2]]);
  if (!pts.length) return [];
  let boxes = [pts];
  while (boxes.length < count) {
    let bi = -1, bestRange = -1, bestCh = 0;
    boxes.forEach((b, i) => {
      if (b.length < 2) return;
      for (let ch = 0; ch < 3; ch++) {
        let lo = 255, hi = 0;
        for (const p of b) { if (p[ch] < lo) lo = p[ch]; if (p[ch] > hi) hi = p[ch]; }
        // weight by population so big flat areas get more shades
        const r = (hi - lo) * Math.sqrt(b.length);
        if (r > bestRange) { bestRange = r; bi = i; bestCh = ch; }
      }
    });
    if (bi < 0) break;
    const b = boxes[bi].sort((p, q) => p[bestCh] - q[bestCh]);
    const mid = b.length >> 1;
    boxes.splice(bi, 1, b.slice(0, mid), b.slice(mid));
  }
  return boxes.map((b) => {
    const s = [0, 0, 0];
    for (const p of b) { s[0] += p[0]; s[1] += p[1]; s[2] += p[2]; }
    return s.map((v) => v / b.length / 255);
  });
}

/** Full 64-entry palette: scene entries first, then the figure colours. */
export function buildPalette(figureRgb) {
  const out = SCENE_HEX.map(hexToRgb).concat(figureRgb.slice(0, FIGURE_SLOTS));
  while (out.length < 64) out.push(out[out.length - 1] || [1, 1, 1]);
  return out;
}
