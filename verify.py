# -*- coding: utf-8 -*-
"""Controleert de gegenereerde site op kapotte links, dubbele titels en JSON-LD-fouten."""

import os, re, json, sys, html as htmllib
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ROOT, "site")

pages, titles, descs, canons = {}, Counter(), Counter(), Counter()
problems = []

for dirpath, _, files in os.walk(SITE):
    for fn in files:
        if not fn.endswith(".html"):
            continue
        full = os.path.join(dirpath, fn)
        rel = "/" + os.path.relpath(full, SITE).replace(os.sep, "/")
        url = rel[:-len("index.html")] if rel.endswith("index.html") else rel
        pages[url] = open(full, encoding="utf-8").read()

print(f"HTML-bestanden gevonden: {len(pages)}")

# --- bestaande URL-set opbouwen ---
exists = set(pages.keys())

link_re = re.compile(r'href="(/[^"#?]*)')
img_re = re.compile(r'(?:src|href)="(/assets/[^"]+)"')
missing = defaultdict(list)
asset_missing = set()

for url, html in pages.items():
    # titel / description / canonical
    noindex = 'content="noindex' in html
    t = re.search(r"<title>(.*?)</title>", html, re.S)
    d = re.search(r'<meta name="description" content="(.*?)">', html, re.S)
    c = re.search(r'<link rel="canonical" href="(.*?)">', html)
    if t: titles[t.group(1)] += 1
    if d: descs[d.group(1)] += 1
    if c: canons[c.group(1)] += 1
    if not t: problems.append(f"{url}: geen <title>")
    if not d: problems.append(f"{url}: geen meta description")
    if not c: problems.append(f"{url}: geen canonical")
    if t and len(htmllib.unescape(t.group(1))) > 62:
        problems.append(f"TITEL TE LANG ({len(htmllib.unescape(t.group(1)))}) {url}: {t.group(1)}")
    if d and not noindex and not (110 <= len(htmllib.unescape(d.group(1))) <= 175):
        problems.append(f"DESCRIPTION LENGTE {len(htmllib.unescape(d.group(1)))} {url}")

    # h1 check
    h1s = re.findall(r"<h1[^>]*>", html)
    if len(h1s) != 1:
        problems.append(f"{url}: {len(h1s)} h1-tags")

    # interne links
    for href in link_re.findall(html):
        if href.startswith("/assets/"):
            continue
        target = href if href.endswith("/") else href + "/"
        if href in (".", ""):
            continue
        if target not in exists and href not in exists:
            missing[href].append(url)

    # assets
    for a in img_re.findall(html):
        p = os.path.join(SITE, a.lstrip("/"))
        if not os.path.exists(p):
            asset_missing.add(a)

    # JSON-LD
    for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
        try:
            json.loads(m)
        except Exception as e:
            problems.append(f"{url}: JSON-LD kapot — {e}")

    # onopgeloste template-placeholders
    if "{plaats}" in html or "{d[" in html or "None" in re.sub(r"<script.*?</script>", "", html, flags=re.S):
        if "None" in re.sub(r"<script.*?</script>", "", html, flags=re.S):
            problems.append(f"{url}: letterlijke 'None' in de HTML")

print("\n--- Kapotte interne links ---")
if missing:
    for href, srcs in sorted(missing.items())[:25]:
        print(f"  {href}  (o.a. op {srcs[0]}, {len(srcs)}x)")
else:
    print("  geen")

print("\n--- Ontbrekende assets ---")
print("  " + (", ".join(sorted(asset_missing)) if asset_missing else "geen"))

print("\n--- Dubbele titles ---")
dupes = [(t, n) for t, n in titles.items() if n > 1]
print(f"  {len(dupes)} dubbel" + ("" if not dupes else ": " + str(dupes[:5])))

print("\n--- Dubbele descriptions ---")
dd = [(t, n) for t, n in descs.items() if n > 1]
print(f"  {len(dd)} dubbel" + ("" if not dd else ": " + str([x[0][:60] for x in dd[:5]])))

print("\n--- Dubbele canonicals ---")
dc = [(t, n) for t, n in canons.items() if n > 1]
print(f"  {len(dc)} dubbel" + ("" if not dc else ": " + str(dc[:5])))

print(f"\n--- Overige problemen ({len(problems)}) ---")
for p in problems[:40]:
    print("  " + p)
if len(problems) > 40:
    print(f"  ... en nog {len(problems)-40}")

# sitemap-check
sm = open(os.path.join(SITE, "sitemap.xml"), encoding="utf-8").read()
locs = re.findall(r"<loc>https://topschilder\.nl(.*?)</loc>", sm)
print(f"\n--- Sitemap ---\n  {len(locs)} URL's")
not_on_disk = [l for l in locs if l not in exists]
print(f"  niet op schijf: {not_on_disk[:5] if not_on_disk else 'geen'}")
indexable = {u for u in exists if 'name="robots" content="noindex' not in pages[u]} - {"/404.html"}
not_in_sitemap = sorted(indexable - set(locs))
print(f"  indexeerbaar maar niet in sitemap: {not_in_sitemap[:5] if not_in_sitemap else 'geen'}")

ok = not missing and not asset_missing and not dupes and not dd and not problems and not not_on_disk
print("\n" + ("✅ ALLES OK" if ok else "⚠️  zie punten hierboven"))
sys.exit(0)
