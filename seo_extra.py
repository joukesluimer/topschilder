# -*- coding: utf-8 -*-
"""
Technische vindbaarheid (features-sessie). Alles in deze module, zodat build.py klein blijft.

build.py roept aan:
- verrijk(pad, html) in write(), vóór het wegschrijven. Dat doet per pagina:
  1. preload van het hero-beeld (de <img> met fetchpriority="high"), met exact dezelfde
     srcset en sizes, zodat de browser niet twee keer downloadt;
  2. ItemList-schema op de overzichtspagina's (tools, kosten, kennisbank, gidsen, diensten,
     werkgebied);
  3. een blok "Ook handig" met gerelateerde pagina's op kosten-, kennisbank-, gids-, dienst- en
     toolpagina's. Alleen links die nog niet op de pagina staan, gekozen op onderwerp.
- schrijf_image_sitemap(out, urls) na build_sitemap(): sitemap-images.xml met alle foto's per
  indexeerbare pagina, plus een regel in robots.txt.

De gerelateerde links komen uit de data (KOSTEN, ARTIKELEN, TOOLS, DIENSTEN, GIDSEN). Die pagina's
worden altijd gebouwd, dus er ontstaan geen dode links; verify.py controleert dat nog eens.
"""

import html as htmllib
import json
import os
import re
import sys

from data import SITE, DIENSTEN, PLAATSEN
from kosten_data import KOSTEN
from kennis_artikelen import ARTIKELEN
from tools import TOOLS

# ---------------------------------------------------------------------------
# Onderwerpen: trefwoorden in url en titel -> tags
# ---------------------------------------------------------------------------
TAGS = {
    "buiten": ["kozijn", "buiten", "gevel", "boeidel", "houtrot", "dakkapel", "schutting", "onderhoud",
               "weer", "kalender", "kunststof", "impregn"],
    "binnen": ["binnen", "muur", "muren", "plafond", "latex", "behang", "trap", "radiator", "keuken",
               "stuc", "tegel", "schimmel", "beton", "verf"],
    "hout": ["kozijn", "deur", "trap", "boeidel", "houtrot", "schutting", "lak", "beits", "keuken", "radiator"],
    "kosten": ["kosten", "prijs", "offerte", "calculator", "uurtarief", "btw", "m2"],
    "kleur": ["kleur", "inspiratie"],
    "verf": ["verf", "sikkens", "sigma", "histor", "latex", "spuit", "lak", "voorstrijk"],
}


# Vaste koppelingen die altijd voorgaan (beide kanten op)
PAREN = [
    ("/onderhoudscheck/", "/onderhoudskalender/"),
    ("/gids/verf-berekenen/", "/verfcalculator/"),
    ("/kosten/calculator/", "/verfcalculator/"),
    ("/kennisbank/hoe-vaak-buitenschilderwerk/", "/onderhoudskalender/"),
    ("/gids/wanneer-buiten-schilderen/", "/onderhoudskalender/"),
    ("/kosten/huis-schilderen/", "/onderhoudskalender/"),
    ("/kosten/schilderen-per-m2/", "/verfcalculator/"),
    ("/schilderwerk/binnenschilderwerk/", "/verfcalculator/"),
    ("/schilderwerk/buitenschilderwerk/", "/onderhoudskalender/"),
]
_PAAR = {(a, b) for a, b in PAREN} | {(b, a) for a, b in PAREN}


def _zone(tags):
    if "binnen" in tags and "buiten" not in tags:
        return "binnen"
    if "buiten" in tags and "binnen" not in tags:
        return "buiten"
    return None


def _tags(*teksten):
    t = " ".join(teksten).lower()
    tags = {tag for tag, woorden in TAGS.items() if any(w in t for w in woorden)}
    if {"binnen", "buiten"} <= tags:
        # "buitenmuur" of "kozijnen binnen": het letterlijke woord beslist
        if "buiten" in t and "binnen" not in t:
            tags.discard("binnen")
        elif "binnen" in t and "buiten" not in t:
            tags.discard("buiten")
    return tags


def _gidsen():
    """GIDSEN staat in build.py; die draait als __main__. Buiten de build: lege lijst."""
    main = sys.modules.get("__main__")
    return [(f"/gids/{s}/", t, o) for s, t, o in getattr(main, "GIDSEN", [])]


_REG = None


def _register():
    global _REG
    if _REG is not None:
        return _REG
    reg = []
    main = sys.modules.get("__main__")
    for t in TOOLS:
        if main is None or callable(getattr(main, t["bouwer"], None)):
            reg.append({"url": t["pad"], "titel": t["titel"], "oms": t["kort"], "soort": "Tool",
                        "tags": _tags(t["pad"], t["titel"], t["kort"], t["tekst"])})
    for k in KOSTEN:
        reg.append({"url": f"/kosten/{k['slug']}/", "titel": k["h1"].split(":")[0], "oms": k["kort"],
                    "soort": "Kosten", "tags": _tags(k["slug"], k["h1"]) | {"kosten"}})
    for a in ARTIKELEN:
        reg.append({"url": f"/kennisbank/{a['slug']}/", "titel": a["titel"], "oms": a["kort"], "soort": "Kennisbank",
                    "tags": _tags(a["slug"], a["titel"])})
    for url, t, o in _gidsen():
        reg.append({"url": url, "titel": t, "oms": o, "soort": "Gids", "tags": _tags(url, t)})
    for d in DIENSTEN:
        reg.append({"url": f"/schilderwerk/{d['slug']}/", "titel": d["naam"], "oms": d["kort"], "soort": "Dienst",
                    "tags": _tags(d["slug"], d["naam"])})
    _REG = reg
    return reg


def _heeft_blok(pad):
    if pad.startswith(("/kosten/", "/kennisbank/", "/gids/", "/schilderwerk/")) and pad.count("/") == 3:
        return True
    return pad in {t["pad"] for t in TOOLS}


# seo-ronde 5: bij gelijke score krijgt de pagina die het minst vaak gekozen is voorrang,
# zodat niet steeds dezelfde (alfabetisch eerste) pagina's in "Ook handig" staan.
_GEKOZEN = {}


def gerelateerd(pad, html, n=6):
    reg = _register()
    zelf = next((r for r in reg if r["url"] == pad), None)
    if zelf is None:
        return []
    al = set(re.findall(r'href="(/[^"#?]*)"', html))
    kandidaten = []
    for r in reg:
        if r["url"] == pad or r["url"] in al:
            continue
        if (pad, r["url"]) in _PAAR:
            kandidaten.append((99, r))
            continue
        z1, z2 = _zone(zelf["tags"]), _zone(r["tags"])
        if z1 and z2 and z1 != z2:
            continue  # geen buitenklus onder een binnenklus en andersom
        score = len(zelf["tags"] & r["tags"])
        if score == 0:
            continue
        if r["soort"] != zelf["soort"]:
            score += 0.5  # liever een mix: van kosten naar tool en kennisbank
        if r["soort"] == "Tool":
            score += 0.25
        kandidaten.append((score, r))
    kandidaten.sort(key=lambda x: (-x[0], _GEKOZEN.get(x[1]["url"], 0), x[1]["url"]))
    # maximaal 2 per soort, zodat het geen lijst met alleen kostenpagina's wordt
    gekozen, per_soort = [], {}
    for _, r in kandidaten:
        if per_soort.get(r["soort"], 0) >= 2:
            continue
        gekozen.append(r)
        _GEKOZEN[r["url"]] = _GEKOZEN.get(r["url"], 0) + 1
        per_soort[r["soort"]] = per_soort.get(r["soort"], 0) + 1
        if len(gekozen) == n:
            break
    return gekozen


_BLOK_CSS = ("<style>.ook{border-top:1px solid var(--line)}.ook h2{font-size:1.35rem;margin:0 0 16px}"
             ".ook-lijst{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}"
             "@media(max-width:860px){.ook-lijst{grid-template-columns:repeat(2,minmax(0,1fr))}}"
             "@media(max-width:520px){.ook-lijst{grid-template-columns:minmax(0,1fr)}}"
             ".ook-lijst a{display:block;height:100%;background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:14px 16px;color:var(--body);text-decoration:none}"
             ".ook-lijst a:hover{border-color:var(--navy-500)}.ook-lijst a:hover strong{text-decoration:underline}"
             ".ook-lijst a:focus-visible{outline:3px solid #ffb15c;outline-offset:2px}"
             ".ook-lijst small{display:block;font-size:.74rem;font-weight:750;text-transform:uppercase;letter-spacing:.04em;color:#7a3f00}"
             ".ook-lijst strong{display:block;color:var(--ink);margin:2px 0}"
             ".ook-lijst span{display:block;font-size:.9rem;line-height:1.45}</style>")


def _blok(items):
    li = "".join(
        f'<li><a href="{r["url"]}"><small>{r["soort"]}</small><strong>{r["titel"]}</strong>'
        f'<span>{r["oms"]}</span></a></li>' for r in items)
    return (f'<section class="section-sm ook" aria-labelledby="ook-kop"><div class="wrap">'
            f'<h2 id="ook-kop">Ook handig</h2><ul class="ook-lijst">{li}</ul></div></section>{_BLOK_CSS}')


# ---------------------------------------------------------------------------
# ItemList op overzichtspagina's
# ---------------------------------------------------------------------------

def _itemlist(pad):
    reg = _register()
    if pad == "/tools/":
        items = [(r["url"], r["titel"]) for r in reg if r["soort"] == "Tool"]
        naam = "Gratis tools voor je schilderklus"
    elif pad == "/kosten/":
        items = [(r["url"], r["titel"]) for r in reg if r["soort"] == "Kosten"]
        naam = "Kosten van schilderwerk per klus"
    elif pad == "/gids/":
        items = [(r["url"], r["titel"]) for r in reg if r["soort"] == "Gids"]
        naam = "Gidsen over schilderwerk"
    elif pad == "/schilderwerk/":
        items = [(r["url"], r["titel"]) for r in reg if r["soort"] == "Dienst"]
        naam = "Diensten schilderwerk"
    elif pad == "/werkgebied/":
        items = [(f"/schilder/{p['slug']}/", f"Schilder in {p['naam']}") for p in sorted(PLAATSEN, key=lambda p: p["naam"])]
        naam = "Werkgebied: schilders per plaats"
    else:
        return None
    if not items:
        return None
    return {"@context": "https://schema.org", "@type": "ItemList", "name": naam,
            "numberOfItems": len(items),
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": SITE["url"] + u, "name": t}
                                for i, (u, t) in enumerate(items)]}


# ---------------------------------------------------------------------------
# Preload van het hero-beeld
# ---------------------------------------------------------------------------

def _preload(html):
    m = re.search(r'<img\b[^>]*fetchpriority="high"[^>]*>', html)
    if not m or 'rel="preload" as="image"' in html:
        return html
    tag = m.group(0)
    attr = dict(re.findall(r'\b(src|srcset|sizes)="([^"]*)"', tag))
    if "src" not in attr:
        return html
    link = f'<link rel="preload" as="image" href="{attr["src"]}"'
    if "srcset" in attr:
        link += f' imagesrcset="{attr["srcset"]}"'
        if "sizes" in attr:
            link += f' imagesizes="{attr["sizes"]}"'
    link += ' fetchpriority="high">'
    return html.replace('<link rel="stylesheet" href="/assets/css/style.css">',
                        link + '<link rel="stylesheet" href="/assets/css/style.css">', 1)


_KOSTEN = {f"/kosten/{k['slug']}/": k for k in KOSTEN}


def _service(pad):
    """Service-schema met prijsrange voor een kostenpagina (uit kosten_data.py)."""
    k = _KOSTEN.get(pad)
    if not k:
        return None
    dienst = next((d["naam"] for d in DIENSTEN if d["slug"] == k["dienst"]), "Schilderwerk")
    return {"@context": "https://schema.org", "@type": "Service",
            "serviceType": dienst,
            "name": k["klus"][:1].upper() + k["klus"][1:],
            "provider": {"@id": SITE["url"] + "/#organization"},
            "areaServed": {"@type": "Country", "name": "Nederland"},
            "description": f"Richtprijs {k['kort']}. Vergelijk offertes van maximaal drie schilders.",
            "offers": {"@type": "AggregateOffer", "priceCurrency": "EUR",
                       "lowPrice": k["van"], "highPrice": k["tot"]}}


# ---------------------------------------------------------------------------
# seo-ronde 5: nazorg op de JSON-LD van alle pagina's
# ---------------------------------------------------------------------------
_ORG = {"@type": "Organization", "@id": SITE["url"] + "/#organization", "name": "Topschilder",
        "url": SITE["url"] + "/", "logo": {"@type": "ImageObject", "url": SITE["url"] + "/assets/merk/icon-512.png",
                                          "width": 512, "height": 512}}
# Eerste publicatie volgens git (eerste commit waarin de pagina voorkomt)
_GEPUBLICEERD = {"/gids/": "2026-11-10", "/inspiratie/": "2026-11-22", "/kennisbank/": "2026-11-22"}
_VANDAAG = __import__("datetime").date.today().isoformat()
_LD = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)


def _nazorg(pad, html):
    """- Article: volledige auteur en uitgever (met logo), dateModified (wordt in write() de echte
         lastmod), datePublished uit git en een afbeelding (og:image als er geen is).
       - Service: Topschilder voert het werk niet zelf uit maar brengt klant en schilder samen,
         dus "broker" in plaats van "provider".
       - Organization: logo erbij."""
    og = re.search(r'<meta property="og:image" content="([^"]+)"', html)

    def fix(m):
        try:
            j = json.loads(m.group(1))
        except ValueError:
            return m.group(0)
        if not isinstance(j, dict):
            return m.group(0)
        t = j.get("@type")
        if t == "Article":
            j["author"] = _ORG
            j["publisher"] = _ORG
            j.setdefault("dateModified", _VANDAAG)
            if "datePublished" not in j:
                d = next((v for k, v in _GEPUBLICEERD.items() if pad.startswith(k)), None)
                if d:
                    j["datePublished"] = d
            if "image" not in j and og:
                j["image"] = og.group(1)
        elif t == "Service" and "provider" in j:
            j["broker"] = j.pop("provider")
        elif t == "Organization" and "logo" not in j and j.get("@id") == _ORG["@id"]:
            j["logo"] = _ORG["logo"]
        else:
            return m.group(0)
        return '<script type="application/ld+json">' + json.dumps(j, ensure_ascii=False) + "</script>"

    return _LD.sub(fix, html)


def verrijk(pad, html):
    if not html.startswith("<!DOCTYPE"):
        return html
    html = _preload(html)
    if '"ItemList"' not in html:
        il = _itemlist(pad)
        if il:
            html = html.replace("</head>", '<script type="application/ld+json">'
                                + json.dumps(il, ensure_ascii=False) + "</script></head>", 1)
    if '"@type": "Service"' not in html:
        sv = _service(pad)
        if sv:
            html = html.replace("</head>", '<script type="application/ld+json">'
                                + json.dumps(sv, ensure_ascii=False) + "</script></head>", 1)
    if _heeft_blok(pad) and '<footer class="footer">' in html and 'class="section-sm ook"' not in html:
        items = gerelateerd(pad, html)
        if len(items) >= 3:
            html = html.replace('<footer class="footer">', _blok(items) + '<footer class="footer">', 1)
    return _nazorg(pad, html)


# ---------------------------------------------------------------------------
# Image-sitemap
# ---------------------------------------------------------------------------

def _x(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;"))


def schrijf_image_sitemap(out, urls):
    """Per indexeerbare pagina de content-foto's (niet logo's, iconen of renders zonder alt)."""
    regels, n_beeld = [], 0
    for pad in sorted({u for u, *_ in urls}):
        bestand = os.path.join(out, pad.strip("/"), "index.html") if pad != "/" else os.path.join(out, "index.html")
        try:
            html = open(bestand, encoding="utf-8").read()
        except OSError:
            continue
        gezien, beelden = set(), []
        for tag in re.findall(r"<img\b[^>]*>", html):
            src = re.search(r'\bsrc="(/assets/fotos/[^"]+)"', tag)
            alt = re.search(r'\balt="([^"]*)"', tag)
            if not src or not alt or not alt.group(1).strip():
                continue
            # grootste variant uit de srcset, anders de src
            srcset = re.search(r'\bsrcset="([^"]+)"', tag)
            url = src.group(1)
            if srcset:
                kandidaten = [d.strip().split(" ")[0] for d in srcset.group(1).split(",") if d.strip()]
                url = kandidaten[-1] if kandidaten else url
            if url in gezien:
                continue
            gezien.add(url)
            beelden.append((url, htmllib.unescape(alt.group(1))))
        if not beelden:
            continue
        n_beeld += len(beelden)
        regels.append(f"<url><loc>{SITE['url']}{pad}</loc>" + "".join(
            f"<image:image><image:loc>{SITE['url']}{_x(u)}</image:loc><image:caption>{_x(a)}</image:caption></image:image>"
            for u, a in beelden[:1000]) + "</url>")
    xml = ('<?xml version="1.0" encoding="UTF-8"?>'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
           'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">' + "".join(regels) + "</urlset>")
    with open(os.path.join(out, "sitemap-images.xml"), "w", encoding="utf-8") as f:
        f.write(xml)
    robots = os.path.join(out, "robots.txt")
    if os.path.exists(robots):
        tekst = open(robots, encoding="utf-8").read()
        if "sitemap-images.xml" not in tekst:
            with open(robots, "a", encoding="utf-8") as f:
                f.write(f"Sitemap: {SITE['url']}/sitemap-images.xml\n")
    return len(regels), n_beeld


# ---------------------------------------------------------------------------
# Lichte JS-verkleining en de stap na de build
# ---------------------------------------------------------------------------

def verklein_js(out):
    """Haalt inspringing, lege regels en hele commentaarregels (//) uit de JS in site/assets/js/.

    Regeleinden blijven staan, dus automatische puntkomma's werken precies als voorheen.
    Bestanden met template-literals (backticks) slaan we over: daar kan witruimte betekenis hebben.
    """
    map_ = os.path.join(out, "assets", "js")
    voor = na = 0
    for naam in sorted(os.listdir(map_)):
        if not naam.endswith(".js"):
            continue
        pad = os.path.join(map_, naam)
        tekst = open(pad, encoding="utf-8").read()
        if "`" in tekst:
            continue
        regels = [r.strip() for r in tekst.split("\n")]
        nieuw = "\n".join(r for r in regels if r and not r.startswith("//")) + "\n"
        voor, na = voor + len(tekst), na + len(nieuw)
        with open(pad, "w", encoding="utf-8") as f:
            f.write(nieuw)
    return voor, na


def na_build(out, urls):
    """Na build_sitemap(): image-sitemap en JS-verkleining."""
    pag, beelden = schrijf_image_sitemap(out, urls)
    voor, na = verklein_js(out)
    print(f"  image-sitemap: {pag} pagina's, {beelden} foto's; JS {voor // 1024} kB -> {na // 1024} kB")
