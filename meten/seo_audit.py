# Technische SEO-audit van site/ (alleen lezen). Gebruik: python3 meten/seo_audit.py site  (LINKS=1 voor linkdetails)
import os, re, json, sys, html as H
from collections import Counter, defaultdict, deque

SITE = sys.argv[1] if len(sys.argv) > 1 else "site"
pages = {}
for dp, _, fs in os.walk(SITE):
    for fn in fs:
        if fn.endswith(".html"):
            rel = "/" + os.path.relpath(os.path.join(dp, fn), SITE)
            url = rel[:-10] if rel.endswith("index.html") else rel
            pages[url] = open(os.path.join(dp, fn), encoding="utf-8").read()

idx = {u: h for u, h in pages.items() if 'content="noindex' not in h}
def typ(u):
    p = u.strip("/").split("/")
    if u == "/": return "home"
    if p[0] == "schilder": return "plaats" if len(p) == 2 else "plaats-dienst"
    return p[0] if len(p) == 1 else p[0] + "/*"

def txt(s): return re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", "", s))).strip()

out = defaultdict(list)
# 1. titels
for u, h in idx.items():
    t = txt(re.search(r"<title>(.*?)</title>", h, re.S).group(1))
    d = H.unescape(re.search(r'<meta name="description" content="(.*?)">', h, re.S).group(1))
    h1 = txt(re.search(r"<h1[^>]*>(.*?)</h1>", h, re.S).group(1))
    c = re.search(r'<link rel="canonical" href="(.*?)">', h).group(1)
    if len(t) < 30: out["titel kort"].append((len(t), u, t))
    if len(t) > 60: out["titel >60"].append((len(t), u, t))
    if len(d) < 120 or len(d) > 160: out["descr buiten 120-160"].append((len(d), u))
    if c != "https://topschilder.nl" + u: out["canonical"].append((u, c))
    if 'hreflang' in h: out["hreflang"].append(u)
    if not h.startswith("<!DOCTYPE html>\n<html lang=\"nl\">"): out["lang"].append(u)
    if h1.lower() == t.lower(): out["h1==titel"].append(u)
    if len(h1) > 80: out["h1 lang"].append((len(h1), u, h1))
    if not re.search(r'og:image"', h): out["geen og:image"].append(u)
    out["_titels"].append((u, t, h1, d))
th = Counter(t.split("|")[0].strip().lower() for _, t, _, _ in out["_titels"])
out["titelstam dubbel"] = [(n, k) for k, n in th.items() if n > 1]
h1c = Counter(h1.lower() for _, _, h1, _ in out["_titels"])
out["h1 dubbel"] = [(n, k) for k, n in h1c.items() if n > 1]

# 2. links
link_re = re.compile(r'<a\b[^>]*href="(/[^"#?]*)[^"]*"[^>]*>(.*?)</a>', re.S)
inl = defaultdict(set); graph = defaultdict(set); anchors = defaultdict(Counter)
body_inl = defaultdict(set)
for u, h in pages.items():
    m = re.search(r"<main\b.*?</main>", h, re.S)
    main = m.group(0) if m else h
    for href, a in link_re.findall(h):
        t = href if href.endswith("/") or "." in href.split("/")[-1] else href + "/"
        if t in pages and t != u:
            graph[u].add(t); inl[t].add(u)
    for href, a in link_re.findall(main):
        t = href if href.endswith("/") else href + "/"
        if t in pages and t != u:
            body_inl[t].add(u)
            an = txt(a)
            if not an:
                al = re.search(r'aria-label="([^"]+)"', a) or re.search(r'alt="([^"]+)"', a)
                an = "[leeg]" + (al.group(1) if al else "")
            anchors[t][an[:70]] += 1
depth = {"/": 0}; q = deque(["/"])
while q:
    x = q.popleft()
    for y in graph[x]:
        if y not in depth: depth[y] = depth[x] + 1; q.append(y)
out["diepte"] = Counter(depth.get(u, 99) for u in idx)
out["diep>=4"] = sorted((depth.get(u, 99), u) for u in idx if depth.get(u, 99) >= 4)
out["weinig body-inlinks (<3)"] = sorted((len(body_inl[u]), u) for u in idx if len(body_inl[u]) < 3)
GEN = {"lees meer", "meer", "klik hier", "hier", "bekijk", "lees verder", "meer info", "meer weten", "bekijk alles"}
gen = Counter()
for t, c in anchors.items():
    for a, n in c.items():
        if a.lower().rstrip(" →›»") in GEN or a.startswith("[leeg]"): gen[(a, t)] += n
out["generieke ankers"] = gen.most_common(40)

# 3. schema
types = defaultdict(Counter); errs = []
for u, h in idx.items():
    for blk in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
        try: j = json.loads(blk)
        except Exception as e: errs.append((u, "json", str(e))); continue
        items = j.get("@graph", [j]) if isinstance(j, dict) else j
        for it in items:
            tp = it.get("@type"); types[typ(u)][str(tp)] += 1
            if tp in ("Review", "AggregateRating") or "aggregateRating" in it or "review" in it:
                errs.append((u, "REVIEW", tp))
            if tp == "BreadcrumbList":
                for i, e in enumerate(it["itemListElement"], 1):
                    if e.get("position") != i: errs.append((u, "bc pos", i))
                    if i < len(it["itemListElement"]) and "item" not in e: errs.append((u, "bc item", i))
            if tp == "FAQPage":
                for qq in it["mainEntity"]:
                    if not qq.get("acceptedAnswer", {}).get("text"): errs.append((u, "faq leeg", qq.get("name")))
            if tp in ("Article", "BlogPosting"):
                for k in ("headline", "datePublished", "author", "image", "dateModified"):
                    if k not in it: errs.append((u, "article mist", k))
                if len(it.get("headline", "")) > 110: errs.append((u, "headline>110", len(it["headline"])))
            if tp == "HowTo":
                if not it.get("step"): errs.append((u, "howto zonder step", ""))
            if tp == "Service":
                for k in ("name", "areaServed"):
                    if k not in it: errs.append((u, "service mist", k))
                if "provider" not in it and "broker" not in it: errs.append((u, "service zonder provider/broker", ""))
            if tp == "ItemList":
                for e in it.get("itemListElement", []):
                    if "url" not in e and "item" not in e: errs.append((u, "itemlist", e)); break
            if tp == "LocalBusiness" or tp == "HomeAndConstructionBusiness":
                errs.append((u, "localbusiness", ""))
            if isinstance(it, dict):
                s = json.dumps(it)
                for m in re.findall(r'"(?:url|item|image|@id)": "([^"]+)"', s):
                    if m.startswith("/"): errs.append((u, "relatieve url", m))
                    elif m.startswith("https://topschilder.nl/"):
                        p = m[len("https://topschilder.nl"):].split("#")[0]
                        if not (p in pages or os.path.exists(SITE + p)): errs.append((u, "schema-url dood", m))
out["schema per type"] = {k: dict(v) for k, v in sorted(types.items())}
out["schema fouten"] = errs[:60]; out["schema fouten n"] = len(errs)

# 4. gewicht
def fsize(p):
    p = p.split("?")[0].split("#")[0]
    f = SITE + p
    return os.path.getsize(f) if os.path.isfile(f) else 0
w = []; imgprob = Counter(); blocking = Counter()
for u, h in idx.items():
    head = h.split("</head>")[0]
    css = sum(fsize(x) for x in re.findall(r'<link rel="stylesheet" href="([^"]+)"', h))
    inl_css = sum(len(x) for x in re.findall(r"<style[^>]*>(.*?)</style>", h, re.S))
    js = sum(fsize(x) for x in re.findall(r'<script[^>]*src="(/[^"]+)"', h))
    inl_js = sum(len(x) for x in re.findall(r"<script(?![^>]*ld\+json)[^>]*>(.*?)</script>", h, re.S))
    imgs = re.findall(r"<img\b[^>]*>", h)
    isz = 0
    for i, tag in enumerate(imgs):
        src = re.search(r'\ssrc="([^"]+)"', tag)
        lazy = 'loading="lazy"' in tag
        if not lazy: isz += fsize(src.group(1)) if src else 0
        if not re.search(r'\swidth=', tag) or not re.search(r'\sheight=', tag): imgprob["geen width/height"] += 1; out["_wh"].append((u, tag[:120]))
        if src and src.group(1).endswith((".jpg", ".png", ".jpeg")) and "srcset" not in tag: imgprob["jpg/png zonder srcset"] += 1
        if src and "/fotos/" in src.group(1) and "srcset" not in tag: imgprob["foto zonder srcset"] += 1; out["_nosrcset"].append((u, tag[:140]))
        if i == 0 and lazy and "/fotos/" in tag: imgprob["eerste foto lazy"] += 1
        if "srcset" in tag and "sizes=" not in tag: imgprob["srcset zonder sizes"] += 1
    for s in re.findall(r"<script\b[^>]*>", head):
        if "src=" in s and "defer" not in s and "async" not in s and "module" not in s: blocking[s] += 1
    for s in re.findall(r'<link rel="stylesheet"[^>]*>', head): blocking[s] += 1
    w.append((len(h.encode()), css, inl_css, js, inl_js, isz, len(imgs), u))
out["imgprob"] = imgprob; out["blokkerend"] = blocking.most_common(10)
w.sort(reverse=True)
out["zwaarste html"] = [(a // 1024, u) for a, *_, u in w[:12]]
import statistics as st
out["mediaan"] = {"html kB": st.median(x[0] for x in w) / 1024, "css": st.median(x[1] for x in w) / 1024,
                  "inline css": st.median(x[2] for x in w) / 1024, "js": st.median(x[3] for x in w) / 1024,
                  "inline js": st.median(x[4] for x in w) / 1024, "img eager kB": st.median(x[5] for x in w) / 1024}
out["zwaarst eager img"] = sorted(((x[5] // 1024, x[7]) for x in w), reverse=True)[:10]
out["zwaarst js"] = sorted(((x[3] // 1024, x[7]) for x in w), reverse=True)[:8]

for k, v in out.items():
    if k.startswith("_"): continue
    n = len(v) if hasattr(v, "__len__") else v
    if isinstance(v, int): print(f"\n## {k}: {v}"); continue
    print(f"\n## {k} ({n})")
    if isinstance(v, dict): print(json.dumps(v, ensure_ascii=False, default=str, indent=0)[:3000])
    else:
        for x in list(v)[:int(os.environ.get("N", 25))]: print("  ", x)

if os.environ.get("LINKS"):
    print("\n## minste body-inlinks (indexeerbaar, geen plaats-dienst)")
    for n, u in sorted((len(body_inl[u]), u) for u in idx if typ(u) != "plaats-dienst")[:25]: print("  ", n, u)
    print("\n## plaats-dienst minste body-inlinks")
    for n, u in sorted((len(body_inl[u]), u) for u in idx if typ(u) == "plaats-dienst")[:8]: print("  ", n, u)
    a2t = defaultdict(set)
    for t, c in anchors.items():
        for a in c: a2t[a.lower()].add(t)
    print("\n## zelfde ankertekst -> meerdere doelen")
    for a, ts in sorted(a2t.items(), key=lambda x: -len(x[1]))[:25]:
        if len(ts) > 1: print("  ", len(ts), repr(a), sorted(ts)[:4])
