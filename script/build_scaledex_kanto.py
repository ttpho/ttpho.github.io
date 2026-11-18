"""Build scaledex/index.html: the Kanto list of Pokemon Scale World figures.

Data comes from the Scaledex project (https://github.com/ttpho/Scaledex):
data/scaledex.json, published at https://huyla1903.github.io/Scaledex/data/scaledex.json.

Usage:
    python script/build_scaledex_kanto.py                 # download the live JSON
    python script/build_scaledex_kanto.py path/to/scaledex.json
"""
import html
import json
import os
import sys
import urllib.request
from datetime import date

DATA_URL = "https://huyla1903.github.io/Scaledex/data/scaledex.json"
IMAGE_BASE = "https://huyla1903.github.io/Scaledex/data/"
REGION = "kanto"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scaledex", "index.html")

TYPE_VI = {
    "normal": "Thường", "fighting": "Giác đấu", "flying": "Bay", "poison": "Độc", "ground": "Đất",
    "rock": "Đá", "bug": "Côn trùng", "ghost": "Ma", "steel": "Thép", "fire": "Lửa", "water": "Nước",
    "grass": "Cỏ", "electric": "Điện", "psychic": "Siêu linh", "ice": "Băng", "dragon": "Rồng",
    "dark": "Bóng tối", "fairy": "Tiên",
}
TYPE_COLOR = {
    "normal": "#9fa19f", "fighting": "#ff8000", "flying": "#81b9ef", "poison": "#9141cb", "ground": "#915121",
    "rock": "#afa981", "bug": "#91a119", "ghost": "#704170", "steel": "#60a1b8", "fire": "#e62829",
    "water": "#2980ef", "grass": "#3fa129", "electric": "#e5b800", "psychic": "#ef4179", "ice": "#3dcef3",
    "dragon": "#5060e1", "dark": "#624d4e", "fairy": "#ef70ef",
}
STATUS_VI = {"legendary": "Huyền thoại", "mythical": "Thần thoại", "powerhouse": "Powerhouse"}
ROLE_VI = {
    "protagonist": "Nhân vật chính", "rival": "Đối thủ", "professor": "Giáo sư", "gym": "Gym Leader",
    "e4": "Tứ Thiên Vương", "champion": "Nhà vô địch", "boss": "Trùm", "clan": "Thủ lĩnh",
    "teammz": "Team MZ", "friend": "Bạn bè", "merchant": "Thương nhân", "detective": "Thám tử",
}
CHANNEL_VI = {
    "supermarket": "Siêu thị (quầy kẹo)", "convenience": "Cửa hàng tiện lợi", "hobby": "Hobby shop",
    "pokecen": "Pokémon Center", "pbandai": "Premium Bandai", "pbandai_std": "Premium Bandai (bán lẻ)",
    "other": "Khác",
}


def load(argv):
    if len(argv) > 1:
        with open(argv[1], encoding="utf-8") as f:
            return json.load(f)
    req = urllib.request.Request(DATA_URL, headers={"User-Agent": "scaledex-kanto-builder"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def e(s):
    return html.escape(str(s), quote=True) if s is not None else ""


def img_url(fig):
    rel = fig.get("imageTrim") or fig.get("image")
    return IMAGE_BASE + rel if rel else fig.get("imageUrl", "")


def role_text(role, d):
    key, _, sub = role.partition(":")
    text = ROLE_VI.get(key) or d["roles"].get(key, {}).get("en", key)
    if sub:
        text += " · " + TYPE_VI.get(sub, sub.capitalize())
    return text


def build(d):
    today = date.today().isoformat()
    figs = {f["id"]: f for f in d["figures"]}
    prods = {p["id"]: p for p in d["products"]}

    chars = []
    for c in d["characters"]:
        cf = [figs[i] for i in c["figures"] if i in figs and REGION in figs[i].get("regions", [figs[i]["region"]])]
        if cf:
            chars.append((c, cf))
    pokemon = sorted([x for x in chars if x[0]["kind"] == "pokemon"], key=lambda x: x[0]["dex"])
    trainers = sorted([x for x in chars if x[0]["kind"] == "trainer"], key=lambda x: x[0].get("order") or 999)

    n_figs = sum(len(cf) for _, cf in chars)
    types_used = sorted({t for c, _ in pokemon for t in c.get("types") or []}, key=lambda t: list(TYPE_VI).index(t))

    def release_rows(fig):
        rows = []
        for pid in fig.get("productIds", []):
            p = prods.get(pid)
            if p:
                rows.append(p)
        rows.sort(key=lambda p: p.get("date") or "9999")
        out = []
        for p in rows:
            upcoming = (p.get("date") or "") > today
            price = "¥{:,}".format(p["priceJPY"]) if p.get("priceJPY") else "—"
            chans = ", ".join(CHANNEL_VI.get(ch, ch) for ch in p.get("channels") or [])
            name = e(p.get("nameEn") or p.get("nameJa"))
            if p.get("url"):
                name = '<a href="{}" target="_blank" rel="noopener">{}</a>'.format(e(p["url"]), name)
            tags = ""
            if p.get("rerelease"):
                tags += ' <span class="sd-tag">Tái bản</span>'
            if upcoming:
                tags += ' <span class="sd-tag sd-up">Sắp ra mắt</span>'
            out.append(
                "<li><span class=\"sd-rel-date\">{}</span> {}{}<br><small>{} · <b>{}</b></small></li>".format(
                    e(p.get("date") or p.get("dateText") or "?"), name, tags, e(chans), price))
        return "".join(out)

    def card(c, cf):
        kind = c["kind"]
        if kind == "pokemon":
            num = "#{:03d}".format(c["dex"])
            chips = "".join('<span class="sd-type" style="--tc:{}">{}</span>'.format(TYPE_COLOR.get(t, "#888"), e(TYPE_VI.get(t, t)))
                            for t in c.get("types") or [])
            if c.get("status"):
                chips += '<span class="sd-badge">{}</span>'.format(e(STATUS_VI.get(c["status"], c["status"])))
        else:
            num = "Trainer"
            chips = "".join('<span class="sd-badge">{}</span>'.format(e(role_text(r, d))) for r in c.get("roles") or [])
        first = cf[0]
        years = sorted({f.get("firstYear") for f in cf if f.get("firstYear")})
        search = " ".join(filter(None, [c["nameEn"], c["nameJa"], num, " ".join(c.get("types") or []),
                                        " ".join(TYPE_VI.get(t, "") for t in c.get("types") or [])])).lower()
        variants = []
        for i, f in enumerate(cf, 1):
            h = f.get("heightCm")
            htxt = "{} cm".format(h) if h else ("~{} cm (ước tính)".format(f["heightEst"]) if f.get("heightEst") else "")
            label = f.get("labelEn") or ("Bản {} ({})".format(i, f.get("firstYear") or "?") if len(cf) > 1 else "Bản thường")
            variants.append(
                '<details class="sd-fig"><summary><img loading="lazy" src="{img}" alt="{alt}"><span>{label}{h}</span></summary>'
                '<ul class="sd-rel">{rels}</ul></details>'.format(
                    img=e(img_url(f)), alt=e(c["nameEn"] + " " + (f.get("labelEn") or "")),
                    label=e(label), h=(" · " + e(htxt)) if htxt else "", rels=release_rows(f) or "<li>Chưa có thông tin phát hành</li>"))
        return (
            '<article class="sd-card" data-cid="{cid}" data-kind="{kind}" data-types="{types}" data-search="{search}">'
            '<div class="sd-img"><img loading="lazy" src="{img}" alt="{name}"></div>'
            '<div class="sd-body"><div class="sd-num">{num}</div>'
            '<h3>{name} <small lang="ja">{ja}</small></h3>'
            '<div class="sd-chips">{chips}</div>'
            '<div class="sd-meta">{nfig} mô hình · từ năm {year}</div>'
            '{variants}</div></article>'
        ).format(cid=e(c["id"]), kind=kind, types=" ".join(c.get("types") or []), search=e(search),
                 img=e(img_url(first)), name=e(c["nameEn"]), ja=e(c["nameJa"]), num=num, chips=chips,
                 nfig=len(cf), year=years[0] if years else "?", variants="".join(variants))

    type_buttons = "".join('<button type="button" class="sd-type sd-filter-type" data-type="{t}" style="--tc:{c}">{n}</button>'.format(
        t=t, c=TYPE_COLOR[t], n=e(TYPE_VI[t])) for t in types_used)

    def fig_h(f):
        return f.get("heightCm") or f.get("heightEst")

    gallery_items = []
    max_h = 0
    for c, cf in pokemon + trainers:
        for f in cf:
            h = fig_h(f)
            if not h:
                continue
            max_h = max(max_h, h)
            label = c["nameEn"] + (" ({})".format(f["labelEn"]) if f.get("labelEn") else "")
            gallery_items.append(
                '<figure class="sd-g-item" data-cid="{cid}" data-h="{h}" style="--h:{h}" title="{t}">'
                '<span class="sd-g-fig"><img loading="lazy" src="{img}" alt="{t}"></span><figcaption>{name}<br><b>{hs} cm</b></figcaption></figure>'.format(
                    cid=e(c["id"]), h=h, t=e("{} · {} cm".format(label, h)), img=e(img_url(f)), name=e(label),
                    hs=("~" if not f.get("heightCm") else "") + str(h)))
    max_cm = int(max_h) + 2

    dio = []
    for c, cf in pokemon:
        for f in cf:
            h = fig_h(f)
            if h and (f.get("imageTrim") or f.get("image")):
                dio.append({"cid": c["id"], "n": c["nameEn"] + (" ({})".format(f["labelEn"]) if f.get("labelEn") else ""),
                            "ja": c["nameJa"], "dex": c["dex"], "h": h, "img": img_url(f)})
    dio_json = json.dumps(dio, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

    return TEMPLATE.format(
        dio_json=dio_json,
        gallery_items="\n".join(gallery_items), max_cm=max_cm,
        generated=e(d.get("generated", "")),
        n_poke=len(pokemon), n_trainer=len(trainers), n_figs=n_figs,
        type_buttons=type_buttons,
        pokemon_cards="\n".join(card(c, cf) for c, cf in pokemon),
        trainer_cards="\n".join(card(c, cf) for c, cf in trainers),
    )


TEMPLATE = """---
layout: page
title: "Scaledex · Kanto"
subtitle: "Danh sách Pokémon Scale World 1/20 (Bandai) - vùng Kanto"
full-width: true
---
<!-- Generated by script/build_scaledex_kanto.py from Scaledex data ({generated}). Do not edit by hand. -->
<style>
  .sd {{ --sd-bg:#fff; --sd-card:#fff; --sd-line:#d7e9ee; --sd-muted:#5b7680; --sd-accent:#2aa6dc; max-width:1200px; margin:0 auto; }}
  .sd-hero {{ background:#fff; color:#0f3443; border:1px solid var(--sd-line); border-radius:16px; padding:20px 24px; margin-bottom:16px; }}
  .sd-hero h2 {{ margin:0 0 6px; font-weight:800; }}
  .sd-hero p {{ margin:4px 0; }}
  .sd-stats b {{ font-size:1.2em; }}
  .sd-tools {{ position:sticky; top:56px; z-index:5; background:var(--sd-bg); border:1px solid var(--sd-line); border-radius:12px; padding:10px; margin-bottom:16px; display:flex; flex-wrap:wrap; gap:8px; align-items:center; }}
  .sd-tools input {{ flex:1 1 220px; min-width:0; padding:8px 12px; border:1px solid var(--sd-line); border-radius:8px; font-size:16px; }}
  .sd-tools .sd-seg button {{ border:1px solid var(--sd-line); background:#fff; padding:6px 12px; border-radius:8px; cursor:pointer; }}
  .sd-tools .sd-seg button.on {{ background:var(--sd-accent); color:#fff; border-color:var(--sd-accent); }}
  .sd-types {{ display:flex; flex-wrap:wrap; gap:6px; width:100%; }}
  .sd-type {{ display:inline-block; background:var(--tc); color:#fff; border-radius:999px; padding:2px 10px; font-size:12px; font-weight:700; border:2px solid transparent; }}
  button.sd-type {{ cursor:pointer; opacity:.55; }}
  button.sd-type.on {{ opacity:1; border-color:#0f3443; }}
  .sd-badge {{ display:inline-block; background:#0f3443; color:#fff; border-radius:999px; padding:2px 10px; font-size:12px; font-weight:700; }}
  .sd h2.sd-sec {{ margin:24px 0 12px; font-weight:800; }}
  .sd-grid {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(260px,1fr)); gap:14px; }}
  .sd-card {{ background:var(--sd-card); border:1px solid var(--sd-line); border-radius:14px; overflow:hidden; display:flex; flex-direction:column; box-shadow:0 2px 8px rgba(15,52,67,.06); }}
  .sd [hidden] {{ display:none !important; }}
  .sd-img {{ display:block; background:#fff; aspect-ratio:4/3; padding:8px; overflow:hidden; box-sizing:border-box; }}
  .sd-img img {{ width:100%; height:100%; object-fit:contain; }}
  .sd-body {{ padding:10px 12px 12px; }}
  .sd-num {{ color:var(--sd-muted); font-weight:700; font-size:13px; }}
  .sd-body h3 {{ margin:2px 0 6px; font-size:18px; font-weight:800; }}
  .sd-body h3 small {{ color:var(--sd-muted); font-weight:400; font-size:13px; }}
  .sd-chips {{ display:flex; flex-wrap:wrap; gap:4px; margin-bottom:6px; }}
  .sd-meta {{ color:var(--sd-muted); font-size:13px; margin-bottom:6px; }}
  .sd-fig {{ border-top:1px dashed var(--sd-line); padding-top:6px; margin-top:6px; }}
  .sd-fig summary {{ cursor:pointer; display:flex; align-items:center; gap:8px; font-size:14px; font-weight:600; list-style:none; }}
  .sd-fig summary::-webkit-details-marker {{ display:none; }}
  .sd-fig summary::after {{ content:"▾"; margin-left:auto; color:var(--sd-muted); }}
  .sd-fig[open] summary::after {{ content:"▴"; }}
  .sd-fig summary img {{ width:40px; height:40px; object-fit:contain; background:#fff; border-radius:8px; }}
  .sd-rel {{ list-style:none; padding:0; margin:6px 0 0; font-size:13px; }}
  .sd-rel li {{ padding:4px 0; border-bottom:1px solid #f0f4f5; }}
  .sd-rel-date {{ color:var(--sd-muted); font-variant-numeric:tabular-nums; }}
  .sd-tag {{ background:#ffe9a8; color:#6b4b00; border-radius:6px; padding:0 6px; font-size:11px; font-weight:700; white-space:nowrap; }}
  .sd-tag.sd-up {{ background:#ffd0d0; color:#8a1010; }}
  .sd-empty {{ color:var(--sd-muted); text-align:center; padding:24px; }}
  .sd-gal {{ --px:12; --cap:34px; border:1px solid var(--sd-line); border-radius:14px; overflow:hidden; background:#fff; }}
  .sd-gal-stage {{ overflow-x:auto; display:flex; align-items:flex-end; gap:14px; padding:16px 20px 0;
    min-height:calc(var(--maxcm) * var(--px) * 1px + var(--cap) + 24px); box-sizing:border-box; background:#fff; }}
  .sd-g-item {{ flex:0 0 auto; margin:0; display:flex; flex-direction:column; align-items:center; }}
  .sd-g-fig {{ display:block; margin-bottom:6px; }}
  .sd-g-fig img {{ display:block; height:calc(var(--h) * var(--px) * 1px); width:auto; mix-blend-mode:multiply; }}
  .sd-g-item figcaption {{ height:var(--cap); box-sizing:border-box; padding-top:4px; width:100%; min-width:48px;
    font-size:10px; line-height:1.25; text-align:center; color:var(--sd-muted); white-space:nowrap; }}
  .sd-g-item figcaption b {{ color:#0f3443; }}
  .sd-dio {{ border:1px solid var(--sd-line); border-radius:14px; overflow:hidden; background:#fff; }}
  .sd-dio canvas {{ display:block; width:100%; aspect-ratio:16/9; min-height:300px; max-height:70vh; image-rendering:pixelated; outline:none; touch-action:pan-y; cursor:grab; }}
  .sd-dio-bar {{ display:flex; flex-wrap:wrap; gap:10px; align-items:center; padding:10px 12px; border-top:1px solid var(--sd-line); font-size:14px; }}
  .sd-dio-bar small {{ color:var(--sd-muted); }}
  .sd-dio-hint {{ color:var(--sd-muted); font-size:13px; margin:6px 0 0; }}
  .sd-gal-ctl {{ display:flex; flex-wrap:wrap; gap:12px; align-items:center; margin:0 0 8px; font-size:14px; color:var(--sd-muted); }}
  .sd-gal-ctl select, .sd-gal-ctl input {{ vertical-align:middle; }}
  .sd-shuffle {{ border:1px solid var(--sd-line); background:#fff; color:#0f3443; padding:4px 12px; border-radius:8px; cursor:pointer; font-size:14px; }}
  .sd-shuffle:hover {{ border-color:var(--sd-accent); color:var(--sd-accent); }}
  .sd-foot {{ color:var(--sd-muted); font-size:13px; margin-top:24px; }}
  @media (max-width:480px) {{ .sd-grid {{ grid-template-columns:repeat(2,minmax(0,1fr)); gap:10px; }} .sd-body h3 {{ font-size:15px; }} .sd-hero {{ padding:16px; }} }}
</style>

<div class="sd">
  <div class="sd-hero">
    <h2>Pokémon Scale World · Kanto</h2>
    <p>Danh sách mô hình <strong>Pokémon Scale World 1/20 (Bandai)</strong> vùng Kanto: Pokémon, trainer, chiều cao và các đợt phát hành (ngày, kênh bán, giá JPY).</p>
    <p class="sd-stats"><b>{n_poke}</b> Pokémon · <b>{n_trainer}</b> trainer · <b>{n_figs}</b> mô hình</p>
  </div>

  <div class="sd-tools">
    <input id="sd-q" type="search" placeholder="Tìm tên (EN / 日本語), số dex, hệ…" aria-label="Tìm kiếm">
    <div class="sd-seg" role="group">
      <button type="button" data-kind="all" class="on">Tất cả</button>
      <button type="button" data-kind="pokemon">Pokémon</button>
      <button type="button" data-kind="trainer">Trainer</button>
    </div>
    <div class="sd-types">{type_buttons}</div>
  </div>

  <h2 class="sd-sec" id="diorama">Diorama · 2 Pokémon ngẫu nhiên</h2>
  <div class="sd-dio">
    <canvas id="sd-dio-canvas" aria-label="Diorama hai mô hình Pokémon Scale World"></canvas>
    <div class="sd-dio-bar">
      <button type="button" id="sd-dio-roll" class="sd-shuffle">🎲 Chọn 2 Pokémon khác</button>
      <button type="button" id="sd-dio-reset" class="sd-shuffle">↺ Góc nhìn ban đầu</button>
      <span id="sd-dio-names"></span>
      <small id="sd-dio-status">Đang tải diorama…</small>
    </div>
  </div>
  <p class="sd-dio-hint">Kéo để xoay. Hai mô hình giữ đúng tỉ lệ chiều cao thật với nhau (1/20); đế và cảnh vật co giãn theo cặp được chọn. Dựng bằng bộ <a href="https://github.com/sloemo01/diorama">Diorama</a> (Three.js, MIT).</p>
  <script type="application/json" id="sd-dio-data">{dio_json}</script>

  <h2 class="sd-sec" id="gallery">Gallery · tỉ lệ 1/20</h2>
  <div class="sd-gal-ctl">
    <label>Phóng to <input id="sd-zoom" type="range" min="6" max="30" value="12"></label>
    <label>Sắp xếp <select id="sd-sort"><option value="dex">Theo số dex</option><option value="h-asc">Thấp → cao</option><option value="h-desc">Cao → thấp</option><option value="random">Ngẫu nhiên</option></select></label>
    <button type="button" id="sd-shuffle" class="sd-shuffle" title="Xáo trộn ngẫu nhiên">🎲 Ngẫu nhiên</button>
    <span>Ảnh được đặt cạnh nhau theo đúng chiều cao thật của mô hình. Danh sách lọc theo ô tìm kiếm phía trên.</span>
  </div>
  <div class="sd-gal" id="sd-gal" style="--maxcm:{max_cm}">
    <div class="sd-gal-stage" id="sd-stage">
{gallery_items}
    </div>
  </div>

  <h2 class="sd-sec" id="pokemon">Pokémon</h2>
  <div class="sd-grid" data-sec="pokemon">
{pokemon_cards}
  </div>

  <h2 class="sd-sec" id="trainer">Trainer</h2>
  <div class="sd-grid" data-sec="trainer">
{trainer_cards}
  </div>
  <p class="sd-empty" id="sd-empty" hidden>Không tìm thấy mô hình nào.</p>

  <p class="sd-foot">
    Dữ liệu: <a href="https://github.com/ttpho/Scaledex">Scaledex</a> (cập nhật {generated}) ·
    Nguồn gốc: <a href="https://www.bandai.co.jp/candy/pokemonscaleworld/lineup/">Bandai official dex</a>.
    Giá là giá bán lẻ tại Nhật (đã gồm thuế, hàng quầy kẹo tính theo hộp). Hình ảnh © Bandai / Pokémon.
  </p>
</div>

<script>
(function () {{
  var q = document.getElementById("sd-q");
  var kind = "all", types = {{}};
  var cards = Array.prototype.slice.call(document.querySelectorAll(".sd-card"));
  var gItems = Array.prototype.slice.call(document.querySelectorAll(".sd-g-item"));
  var stage = document.getElementById("sd-stage"), gal = document.getElementById("sd-gal");
  function apply() {{
    var hide = {{}};
    var s = q.value.trim().toLowerCase(), any = false, active = Object.keys(types);
    var shown = {{ pokemon: 0, trainer: 0 }};
    cards.forEach(function (c) {{
      var ok = (kind === "all" || c.dataset.kind === kind) &&
        (!s || c.dataset.search.indexOf(s) >= 0) &&
        (!active.length || active.some(function (t) {{ return (" " + c.dataset.types + " ").indexOf(" " + t + " ") >= 0; }}));
      c.hidden = !ok;
      if (!ok) hide[c.dataset.cid] = 1;
      if (ok) {{ any = true; shown[c.dataset.kind]++; }}
    }});
    ["pokemon", "trainer"].forEach(function (k) {{
      var show = shown[k] > 0;
      document.getElementById(k).hidden = !show;
      document.querySelector('[data-sec="' + k + '"]').hidden = !show;
    }});
    document.getElementById("sd-empty").hidden = any;
    gItems.forEach(function (g) {{ g.hidden = !!hide[g.dataset.cid]; }});
  }}
  q.addEventListener("input", apply);
  document.getElementById("sd-zoom").addEventListener("input", function () {{ gal.style.setProperty("--px", this.value); }});
  var sortSel = document.getElementById("sd-sort");
  function sortGallery() {{
    var mode = sortSel.value, list = gItems.slice();
    if (mode === "random") {{
      for (var i = list.length - 1; i > 0; i--) {{ var j = Math.floor(Math.random() * (i + 1)), t = list[i]; list[i] = list[j]; list[j] = t; }}
    }} else if (mode !== "dex") {{
      list.sort(function (a, b) {{ var d = a.dataset.h - b.dataset.h; return mode === "h-asc" ? d : -d; }});
    }}
    list.forEach(function (g) {{ stage.appendChild(g); }});
    stage.scrollLeft = 0;
  }}
  sortSel.addEventListener("change", sortGallery);
  document.getElementById("sd-shuffle").addEventListener("click", function () {{ sortSel.value = "random"; sortGallery(); }});
  document.querySelectorAll(".sd-seg button").forEach(function (b) {{
    b.addEventListener("click", function () {{
      kind = b.dataset.kind;
      document.querySelectorAll(".sd-seg button").forEach(function (x) {{ x.classList.toggle("on", x === b); }});
      apply();
    }});
  }});
  document.querySelectorAll(".sd-filter-type").forEach(function (b) {{
    b.addEventListener("click", function () {{
      var t = b.dataset.type;
      if (types[t]) delete types[t]; else types[t] = 1;
      b.classList.toggle("on", !!types[t]);
      apply();
    }});
  }});
}})();
</script>

<script type="importmap">
{{ "imports": {{
  "three": "https://cdn.jsdelivr.net/npm/three@0.170.0/build/three.module.js",
  "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.170.0/examples/jsm/"
}} }}
</script>
<script type="module">
  const canvas = document.getElementById("sd-dio-canvas");
  const status = document.getElementById("sd-dio-status");
  let started = false;
  const io = new IntersectionObserver(async (es) => {{
    if (started || !es[0].isIntersecting) return;
    started = true; io.disconnect();
    try {{
      const {{ startDiorama }} = await import("{{{{ '/scaledex/diorama/main.js' | relative_url }}}}");
      startDiorama({{
        canvas, statusEl: status,
        data: JSON.parse(document.getElementById("sd-dio-data").textContent),
        namesEl: document.getElementById("sd-dio-names"),
        rollBtn: document.getElementById("sd-dio-roll"),
        resetBtn: document.getElementById("sd-dio-reset"),
      }});
    }} catch (e) {{
      console.error(e);
      status.textContent = "Trình duyệt không hỗ trợ WebGL / module.";
    }}
  }}, {{ rootMargin: "200px" }});
  io.observe(canvas);
</script>
"""


def main():
    d = load(sys.argv)
    out = os.path.normpath(OUT)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(build(d))
    print("Wrote", out)


if __name__ == "__main__":
    main()
