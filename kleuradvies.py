# -*- coding: utf-8 -*-
"""
Kleuradvies (/kleuradvies/ en /kleuradvies/{onderwerp}/).

Pagina's met kleuradvies per onderdeel (kozijnen, voordeur), per ruimte (woonkamer,
slaapkamer, keuken en hal), per lichtval, kleurcombinaties en kleurtrends. De inhoud
staat in kleuradvies_teksten.py; dit bestand bouwt de pagina's, de CSS-stalen en de
CSS (site/assets/css/kleuradvies.css).

Geen foto's nodig: elke combinatie wordt getoond als CSS-staal (een getekende kamer,
een stukje gevel of een kleurbalk). Elke kleur heeft een RAL Classic-code met een
hexwaarde als benadering (zelfde bronnen als inspiratie_gids.py).

build_inspiratie() in inspiratie.py roept build_kleuradvies() aan, zodat build.py
niet hoeft te veranderen. Gekozen onderwerpen en zoekvolumes: zie het docstring van
kleuradvies_teksten.py.
"""

import os
import re

from components import page, crumbs, offerte_form, faq_blok, title
from inspiratie_gids import BRONNEN
from kleuradvies_teksten import PAGINAS, RAL, HUB, EXTRA_BRONNEN

PAD = "/kleuradvies/"


def _e(t):
    return t.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;")


def _hex(code):
    return RAL[code][1]


def _naam(code):
    return RAL[code][0]


# ---------------------------------------------------------------------------
# Stalen
# ---------------------------------------------------------------------------

def _chips(kleuren):
    items = "".join(
        f'<li><i style="background:{_hex(c)}" aria-hidden="true"></i><span><strong>{rol}</strong>'
        f'{_naam(c)}{(" · " + c) if c.startswith("RAL ") else ""}</span></li>' for rol, c, *_ in kleuren)
    return f'<ul class="ka-chips">{items}</ul>'


def _staal_kamer(kl):
    """kl: dict rol->code met 'muur', 'accent', 'hout', 'vloer' (accent/hout optioneel)."""
    muur = _hex(kl["muur"])
    accent = _hex(kl.get("accent", kl["muur"]))
    hout = _hex(kl.get("hout", kl["muur"]))
    vloer = _hex(kl.get("vloer", "RAL 1001"))
    plafond = _hex(kl.get("plafond", "RAL 9010"))
    return (f'<div class="ka-kamer" aria-hidden="true" style="--muur:{muur};--accent:{accent};--hout:{hout};'
            f'--vloer:{vloer};--plafond:{plafond}">'
            f'<span class="ka-k-plafond"></span><span class="ka-k-links"></span><span class="ka-k-achter"></span>'
            f'<span class="ka-k-deur"></span><span class="ka-k-raam"></span><span class="ka-k-vloer"></span>'
            f'<span class="ka-k-plint"></span></div>')


def _staal_gevel(kl):
    steen = _hex(kl["steen"])
    kozijn = _hex(kl["kozijn"])
    raam = _hex(kl.get("raam", kl["kozijn"]))
    deur = _hex(kl.get("deur", kl["kozijn"]))
    boei = _hex(kl.get("boei", kl["kozijn"]))
    return (f'<div class="ka-gevel" aria-hidden="true" style="--steen:{steen};--kozijn:{kozijn};--raam:{raam};'
            f'--deur:{deur};--boei:{boei}">'
            f'<span class="ka-g-boei"></span><span class="ka-g-raam ka-g-r1"></span>'
            f'<span class="ka-g-raam ka-g-r2"></span><span class="ka-g-deur"></span></div>')


def _staal_balk(kleuren):
    delen = "".join(f'<span style="background:{_hex(c)};flex:{(rest[0] if rest and not isinstance(rest[0], str) else 1)}"></span>'
                    for _rol, c, *rest in kleuren)
    return f'<div class="ka-balk" aria-hidden="true">{delen}</div>'


def staal(combo):
    soort = combo.get("soort", "balk")
    # derde veld per kleur: rol in de tekening (muur, accent, hout, vloer / steen, kozijn, raam, deur, boei)
    # of, bij een kleurbalk, het aandeel (bijvoorbeeld 60, 30, 10)
    kl = {rest[0]: c for _r, c, *rest in combo["kleuren"] if rest and isinstance(rest[0], str)}
    if soort == "kamer":
        beeld = _staal_kamer(kl)
    elif soort == "gevel":
        beeld = _staal_gevel(kl)
    else:
        beeld = _staal_balk(combo["kleuren"])
    return (f'<figure class="ka-combo">{beeld}<figcaption><h3>{combo["naam"]}</h3>'
            f'{_chips(combo["kleuren"])}<p>{combo["uitleg"]}</p></figcaption></figure>')


def ral_tabel(codes):
    rijen = "".join(
        f'<tr><td><i class="ka-tstaal" style="background:{_hex(c)}"></i></td><td><strong>{_naam(c)}</strong>'
        f'{("<br><small>" + RAL[c][2] + "</small>") if RAL[c][2] else ""}</td><td>{c}</td>'
        f'<td><code>{_hex(c).upper()}</code></td></tr>' for c in codes)
    return (f'<div class="ka-tabel-wrap"><table class="ka-codes"><thead><tr><th><span class="sr-only">Staal</span>'
            f'</th><th>Kleur</th><th>Code</th><th>Hex (scherm)</th></tr></thead><tbody>{rijen}</tbody></table></div>')


def _codes(p):
    gezien = []
    for combo in p.get("stalen", []):
        for _rol, c, *_ in combo["kleuren"]:
            if c not in gezien and c.startswith("RAL "):
                gezien.append(c)
    for c in p.get("extra_codes", []):
        if c not in gezien:
            gezien.append(c)
    return gezien


def _bron_link(k):
    naam, url = BRONNEN[k] if k in BRONNEN else EXTRA_BRONNEN[k]
    return f'<a href="{url}" rel="nofollow noopener" target="_blank">{naam}</a>'


def _woorden(html):
    return len(re.sub(r"<[^>]+>", " ", html).split())


# ---------------------------------------------------------------------------
# Pagina's
# ---------------------------------------------------------------------------

def _cta(p):
    return f"""<section class="section" id="offerte-kleur"><div class="wrap">
  <div class="grid g2" style="gap:48px;align-items:start">
    <div>
      <span class="badge">Van kleur naar offerte</span>
      <h2>{p['cta_kop']}</h2>
      <p class="lead">{p['cta_tekst']}</p>
      <ul class="checklist">
        <li><strong>Gratis en vrijblijvend.</strong> Je krijgt offertes van maximaal drie schilders uit jouw regio.</li>
        <li><strong>Noem de RAL-code.</strong> Zet de kleurcode in je aanvraag; dan weet de schilder precies wat je bedoelt.</li>
        <li><strong>Vraag om een proefvlak.</strong> Een goede schilder zet de kleur eerst op een klein stuk, zodat je hem in je eigen licht ziet.</li>
      </ul>
    </div>
    <div>{offerte_form(p.get('form_kop', 'Offerte voor je nieuwe kleur'), "Gratis · vrijblijvend · maximaal 3 schilders")}</div>
  </div>
</div></section>"""


def _verder(p):
    links = "".join(f'<li><a href="{u}">{t}</a></li>' for u, t in p["links"])
    andere = "".join(f'<li><a href="{PAD}{q["slug"]}/">{q["kort"]}</a></li>'
                     for q in PAGINAS if q["slug"] != p["slug"])
    return f"""<div class="grid g2 ka-verder">
    <div><h3>Diensten, kosten en tools</h3><ul>{links}</ul></div>
    <div><h3>Meer kleuradvies</h3><ul>{andere}<li><a href="{PAD}">Alle kleuradvies</a></li></ul></div>
  </div>"""


def build_pagina(write, p):
    url = f"{PAD}{p['slug']}/"
    cr, cr_ld = crumbs([("Home", "/"), ("Kleuradvies", PAD), (p["kort"], None)])
    secties = "".join(f'<h2 id="{_id}">{kop}</h2>{inhoud}' if _id else f"<h2>{kop}</h2>{inhoud}"
                      for _id, kop, inhoud in ((s[0], s[1], s[2]) if len(s) == 3 else (None, s[0], s[1])
                                               for s in p["secties"]))
    stalen = "".join(staal(c) for c in p.get("stalen", []))
    codes = _codes(p)
    bronnen = list(dict.fromkeys(p.get("bronnen", []) + ["ral", "ral-hex"]))
    bron_html = "".join(f"<li>{_bron_link(k)}</li>" for k in bronnen)
    faq_html, faq_ld = faq_blok(p["faq"], p.get("faq_kop", "Veelgestelde vragen"))
    stalen_html = (f"""<section class="section-sm soft" id="combinaties"><div class="wrap">
  <h2>{p.get('stalen_kop', 'Kleurcombinaties om te proberen')}</h2>
  <p class="ka-smal">{p.get('stalen_intro', '')}</p>
  <div class="ka-grid">{stalen}</div>
  <p class="ka-noot">De stalen zijn getekend met de hexwaarde van elke RAL-kleur. Op een scherm wijkt een kleur altijd wat af van echte verf. Kies pas na een staal of proefvlak in je eigen licht.</p>
</div></section>""" if stalen else "")

    body = f"""{cr}
<section class="section-sm ka-kop"><div class="wrap narrow">
  <span class="badge">{p['badge']}</span>
  <h1>{p['h1']}</h1>
  <p class="lead">{p['intro']}</p>
  {('<p class="ka-snel">Direct naar: ' + p['snel'] + '</p>') if p.get('snel') else ''}
</div></section>
<section class="section-sm"><div class="wrap narrow prose">{secties}</div></section>
{stalen_html}
<section class="section-sm"><div class="wrap narrow prose">
  <h2>De kleuren met hun RAL-code</h2>
  <p>RAL Classic is een kleurnorm die schilders en verfwinkels in heel Nederland kennen. Met de code mengt de verfwinkel de kleur bij elk merk. De namen zijn de officiële RAL-namen; welke code bij een advies hoort, is ons voorstel.</p>
  {ral_tabel(codes)}
  {_verder(p)}
  <h3>Bronnen</h3>
  <ul class="ka-bronnen">{bron_html}</ul>
</div></section>
{_cta(p)}
{faq_html}"""

    artikel_ld = {
        "@context": "https://schema.org", "@type": "Article", "headline": p["h1"],
        "description": p["description"], "inLanguage": "nl-NL",
        "mainEntityOfPage": f"https://topschilder.nl{url}",
        "publisher": {"@type": "Organization", "name": "Topschilder", "url": "https://topschilder.nl/"},
    }
    html = page(title(p["titel"]), p["description"], url, body, [cr_ld, artikel_ld, faq_ld])
    html = html.replace('<link rel="stylesheet" href="/assets/css/style.css">',
                        '<link rel="stylesheet" href="/assets/css/style.css">'
                        '<link rel="stylesheet" href="/assets/css/kleuradvies.css">')
    write(url, html, prio=0.6)
    return _woorden(secties)


def _hub_kaart(p):
    kleuren = []
    for combo in p.get("stalen", [])[:3]:
        kleuren += [c for _r, c, *_ in combo["kleuren"]][:2]
    strook = "".join(f'<span style="background:{_hex(c)}"></span>' for c in kleuren[:6])
    return (f'<a class="ka-hubkaart" href="{PAD}{p["slug"]}/"><span class="ka-strook" aria-hidden="true">{strook}</span>'
            f'<strong>{p["kort"]}</strong><span>{p["teaser"]}</span></a>')


def build_hub(write):
    cr, cr_ld = crumbs([("Home", "/"), ("Inspiratie", "/inspiratie/"), ("Kleuradvies", None)])
    groepen = ""
    for kop, slugs in HUB["groepen"]:
        kaarten = "".join(_hub_kaart(p) for p in PAGINAS if p["slug"] in slugs)
        groepen += f'<h2>{kop}</h2><div class="ka-hubgrid">{kaarten}</div>'
    faq_html, faq_ld = faq_blok(HUB["faq"], "Vragen over kleur kiezen")
    lijst_ld = {
        "@context": "https://schema.org", "@type": "ItemList", "name": "Kleuradvies van Topschilder",
        "numberOfItems": len(PAGINAS),
        "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": p["kort"],
                             "url": f"https://topschilder.nl{PAD}{p['slug']}/"} for i, p in enumerate(PAGINAS)],
    }
    p = {"cta_kop": "Laat je nieuwe kleur door een vakman zetten",
         "cta_tekst": "Weet je welke kleur je wilt? Vraag gratis offertes aan bij schilders uit je regio.",
         "form_kop": "Offerte voor je schilderwerk"}
    body = f"""{cr}
<section class="section-sm ka-kop"><div class="wrap">
  <span class="badge">Kleuradvies</span>
  <h1>{HUB['h1']}</h1>
  <p class="lead">{HUB['intro']}</p>
</div></section>
<section class="section-sm"><div class="wrap">{groepen}</div></section>
<section class="section-sm soft"><div class="wrap narrow prose">{HUB['tekst']}</div></section>
{_cta(p)}
{faq_html}"""
    html = page(title(HUB["titel"]), HUB["description"], PAD, body, [cr_ld, lijst_ld, faq_ld])
    html = html.replace('<link rel="stylesheet" href="/assets/css/style.css">',
                        '<link rel="stylesheet" href="/assets/css/style.css">'
                        '<link rel="stylesheet" href="/assets/css/kleuradvies.css">')
    write(PAD, html, prio=0.7)


def kleuradvies_blok(kop="Kleuradvies per onderwerp", slugs=None):
    """Kleine linkset voor andere pagina's (inspiratie, kleurenkiezer, gidsen)."""
    ps = [p for p in PAGINAS if slugs is None or p["slug"] in slugs]
    links = "".join(f'<li><a href="{PAD}{p["slug"]}/">{p["kort"]}</a></li>' for p in ps)
    return (f'<div class="ka-blok"><h3>{kop}</h3><ul>{links}</ul>'
            f'<p><a href="{PAD}">Alle kleuradvies bekijken</a></p></div>')


def build_kleuradvies(write, out_dir):
    woorden = {}
    for p in PAGINAS:
        woorden[p["slug"]] = build_pagina(write, p)
    build_hub(write)
    _schrijf(os.path.join(out_dir, "assets", "css", "kleuradvies.css"), CSS)
    print(f"Kleuradvies: {len(PAGINAS)} pagina's + overzicht, "
          f"{sum(woorden.values())} woorden lopende tekst (min. {min(woorden.values())}).")


def _schrijf(pad, inhoud):
    os.makedirs(os.path.dirname(pad), exist_ok=True)
    with open(pad, "w", encoding="utf-8") as f:
        f.write(inhoud)


CSS = r'''
.ka-kop .lead{max-width:62ch}
.ka-snel{font-size:.95rem;color:var(--muted)}
.ka-smal{max-width:66ch}
.ka-noot{font-size:.85rem;color:var(--muted);margin-top:18px}
.ka-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:22px;margin-top:20px}
.ka-combo{margin:0;background:#fff;border:1px solid var(--line);border-radius:var(--radius-lg);overflow:hidden;box-shadow:var(--shadow)}
.ka-combo figcaption{padding:16px 18px 18px}
.ka-combo h3{margin-bottom:.4em}
.ka-combo p{font-size:.95rem;margin:0}
.ka-chips{list-style:none;padding:0;margin:0 0 12px;display:grid;gap:6px}
.ka-chips li{display:flex;gap:10px;align-items:center;margin:0;font-size:.88rem;line-height:1.3}
.ka-chips i{flex:0 0 26px;height:26px;border-radius:6px;border:1px solid rgba(0,0,0,.12)}
.ka-chips strong{display:block;font-size:.78rem;text-transform:uppercase;letter-spacing:.04em;color:var(--muted);font-weight:650}
.ka-balk{display:flex;height:130px}
.ka-balk span{display:block}
/* getekende kamer */
.ka-kamer{position:relative;height:170px;background:var(--muur);overflow:hidden}
.ka-kamer span{position:absolute;display:block}
.ka-k-plafond{left:0;right:0;top:0;height:22px;background:var(--plafond);clip-path:polygon(0 0,100% 0,100% 100%,22% 100%)}
.ka-k-links{left:0;top:0;bottom:0;width:22%;background:var(--accent);clip-path:polygon(0 0,100% 13%,100% 74%,0 100%);filter:brightness(.93)}
.ka-k-achter{left:22%;right:0;top:22px;bottom:44px;background:var(--muur)}
.ka-k-raam{right:12%;top:40px;width:26%;height:62px;background:linear-gradient(160deg,#dfeaf2,#b9cddb);border:6px solid var(--hout);border-radius:2px}
.ka-k-deur{left:32%;top:46px;width:15%;bottom:44px;background:var(--hout);border-radius:2px 2px 0 0;box-shadow:inset 0 0 0 5px rgba(0,0,0,.06)}
.ka-k-vloer{left:0;right:0;bottom:0;height:44px;background:var(--vloer);clip-path:polygon(22% 0,100% 0,100% 100%,0 100%,0 78%)}
.ka-k-plint{left:22%;right:0;bottom:44px;height:6px;background:var(--hout)}
/* stukje gevel */
.ka-gevel{position:relative;height:170px;background:var(--steen);background-image:repeating-linear-gradient(0deg,rgba(255,255,255,.18) 0 1px,transparent 1px 12px);overflow:hidden}
.ka-gevel span{position:absolute;display:block}
.ka-g-boei{left:0;right:0;top:0;height:16px;background:var(--boei);box-shadow:0 3px 0 rgba(0,0,0,.12)}
.ka-g-raam{top:42px;width:24%;height:70px;background:linear-gradient(160deg,#dfeaf2,#a9bfcf);border:7px solid var(--kozijn);box-shadow:inset 0 0 0 4px var(--raam)}
.ka-g-r1{left:9%}.ka-g-r2{left:39%}
.ka-g-deur{right:10%;top:52px;bottom:0;width:20%;background:var(--deur);border:6px solid var(--kozijn);border-bottom:0;border-radius:3px 3px 0 0}
.ka-tabel-wrap{overflow-x:auto;margin:0 0 1.5em}
.ka-codes{width:100%;border-collapse:collapse;font-size:.95rem}
.ka-codes th,.ka-codes td{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line);vertical-align:top}
.ka-tstaal{display:inline-block;width:28px;height:28px;border-radius:6px;border:1px solid rgba(0,0,0,.12)}
.ka-verder{gap:24px;margin:1.5em 0}
.ka-verder ul{padding-left:1.1em}
.ka-bronnen{font-size:.9rem}
.ka-tip{background:var(--accent-soft);border-left:4px solid var(--accent);padding:14px 16px;border-radius:8px;margin:0 0 1.2em}
.ka-hubgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:18px;margin:14px 0 36px}
.ka-hubkaart{display:flex;flex-direction:column;gap:6px;background:#fff;border:1px solid var(--line);border-radius:var(--radius-lg);padding:0 0 16px;overflow:hidden;color:var(--body);text-decoration:none;box-shadow:var(--shadow)}
.ka-hubkaart:hover{text-decoration:none;box-shadow:var(--shadow-lg)}
.ka-hubkaart strong{color:var(--ink);font-size:1.08rem;padding:6px 16px 0}
.ka-hubkaart span:not(.ka-strook){padding:0 16px;font-size:.93rem}
.ka-strook{display:flex;height:54px}
.ka-strook span{flex:1}
.ka-blok{background:#fff;border:1px solid var(--line);border-radius:var(--radius-lg);padding:18px 20px;margin:24px 0}
.ka-blok ul{columns:2;column-gap:24px}
@media(max-width:560px){.ka-blok ul{columns:1}.ka-kamer,.ka-gevel{height:150px}}
'''
