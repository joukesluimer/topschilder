# -*- coding: utf-8 -*-
"""Kennisbank: hub op /kennisbank/ en artikelen op /kennisbank/{slug}/.

De inhoud staat in kennis_artikelen.py. build.py roept build_kennisbank(write, TODAY) aan;
dienst- en kostenpagina's halen hun links op met kennis_links_dienst() en kennis_links_kosten().
"""

import html as htmllib

from data import SITE, DIENSTEN
from kosten_data import KOSTEN
from foto_data import FOTOS, FOTOS_PAGINA, FOTO_HOME
from foto_extra import NIEUW
from components import page, crumbs, faq_blok, cta_blok, foto, title, eur
from kennis_artikelen import ARTIKELEN

GEPUBLICEERD = "2026-11-22"

# Bestaande gidsen die in de hub meedoen (niet dupliceren: we linken ernaar).
GIDSEN_IN_HUB = [
    ("/gids/wanneer-buiten-schilderen/", "Wanneer kun je buiten schilderen?",
     "De beste maanden, de minimale temperatuur en schilderen na regen.", "Voorbereiden en uitvoeren", "steiger-langs-amsterdamse-woning"),
    ("/gids/btw-schilderwerk/", "Btw op schilderwerk: 9% of 21%?",
     "Wanneer het lage tarief geldt en hoe je je offerte controleert.", "Offerte, kosten en btw", "potje-met-penselen"),
    ("/gids/verf-berekenen/", "Hoeveel verf heb je nodig?",
     "Liters per m² voor muurverf, grondverf en lak, met rekenhulp.", "Verf kiezen", "verfbak-kwasten-en-roller-zwartwit"),
]

GROEPEN = ["Verf kiezen", "Voorbereiden en uitvoeren", "Schade en onderhoud", "Offerte, kosten en btw"]

DIENST_ARTIKELEN = {
    "binnenschilderwerk": ["plafond-schilderen-zonder-strepen", "latex-of-muurverf", "verf-op-waterbasis-of-terpentinebasis"],
    "buitenschilderwerk": ["welke-verf-voor-kozijnen", "kozijnen-schuren-en-voorbereiden", "grondverf-of-voorlak"],
    "houtrot-reparatie": ["houtrot-herkennen-en-herstellen", "kozijnen-schuren-en-voorbereiden", "verfschade-en-garantie"],
    "spuitwerk": ["verf-op-waterbasis-of-terpentinebasis", "grondverf-of-voorlak", "latex-of-muurverf"],
    "behangen": ["behang-verwijderen", "latex-of-muurverf", "goede-offerte-schilderwerk"],
    "zakelijk-schilderwerk": ["goede-offerte-schilderwerk", "verfschade-en-garantie", "verf-op-waterbasis-of-terpentinebasis"],
}

# seo-ronde 4: nieuwe artikelen bij de dienstpagina's (alleen als ze bestaan)
for _dienst, _extra in {
    "binnenschilderwerk": ["nieuw-stucwerk-schilderen", "schimmel-op-muur"],
    "buitenschilderwerk": ["hoe-vaak-buitenschilderwerk", "sikkens-sigma-of-histor"],
    "houtrot-reparatie": ["verf-bladdert-af"],
    "spuitwerk": ["trap-verven"],
    "behangen": ["nieuw-stucwerk-schilderen"],
}.items():
    DIENST_ARTIKELEN[_dienst] = DIENST_ARTIKELEN[_dienst] + [s for s in _extra if any(a["slug"] == s for a in ARTIKELEN)]

_PER_SLUG = {a["slug"]: a for a in ARTIKELEN}
_KOSTEN = {k["slug"]: k for k in KOSTEN}
_DIENST = {d["slug"]: d for d in DIENSTEN}


def _alle_fotos():
    """Alle foto's op naam, zodat een artikel er een kan kiezen."""
    fs = {f["naam"]: f for f in [FOTO_HOME] + list(FOTOS_PAGINA.values())}
    for groep in FOTOS.values():
        fs.update({f["naam"]: f for f in groep.values()})
    fs.update(NIEUW)
    return fs


FOTO_OP_NAAM = _alle_fotos()
HUB_FOTO = NIEUW["grachtenhuizen-met-woonboten"]


def _url(slug):
    return f"/kennisbank/{slug}/"


def _link(slug):
    a = _PER_SLUG[slug]
    return f'<a href="{_url(slug)}">{a["titel"].split(":")[0]}</a>'


def kennis_links_dienst(dienst_slug):
    """Blok 'Meer weten?' voor een dienstpagina."""
    slugs = DIENST_ARTIKELEN.get(dienst_slug, [])
    if not slugs:
        return ""
    items = "".join(f"<li>{_link(s)}</li>" for s in slugs)
    return (f'<h2>Meer weten?</h2><p>Praktische uitleg uit onze <a href="/kennisbank/">kennisbank</a>:</p>'
            f'<ul>{items}</ul>')


def kennis_links_kosten(kosten_slug, dienst_slug):
    """Korte reeks links voor de regel 'Ook handig' op een kostenpagina."""
    slugs = [a["slug"] for a in ARTIKELEN if kosten_slug in a["kosten"]]
    for s in DIENST_ARTIKELEN.get(dienst_slug, []):
        if s not in slugs:
            slugs.append(s)
    return " · ".join(_link(s) for s in slugs[:3])


def _kosten_blok(a):
    rijen = ""
    for ks in a["kosten"]:
        k = _KOSTEN[ks]
        btw = "excl. btw" if k.get("excl_btw") else "incl. materiaal en btw"
        rijen += (f'<tr><td><a href="/kosten/{ks}/">{(k.get("kruimel") or k["klus"].removeprefix("een ")).capitalize()}</a></td>'
                  f'<td class="num">{eur(k["van"])} – {eur(k["tot"])} {k["eenheid"]}<br><small>{btw}</small></td></tr>')
    if a.get("dienst"):
        d = _DIENST[a["dienst"]]
        rijen += (f'<tr><td><a href="/schilderwerk/{d["slug"]}/">{d["naam"]}</a></td>'
                  f'<td class="num">{eur(d["prijs_van"])} – {eur(d["prijs_tot"])} {d["prijs_eenheid"]}</td></tr>')
    return f"""<div class="callout">
  <h2 style="margin-top:0">Wat kost het?</h2>
  <p>Liever laten doen? Dit zijn onze richtprijzen, gemiddeld over Nederland. Klik door voor rekenvoorbeelden en de prijs in jouw regio.</p>
  <div class="tablewrap"><table>
    <thead><tr><th>Klus</th><th>Richtprijs</th></tr></thead>
    <tbody>{rijen}</tbody>
  </table></div>
  <p><a class="btn btn-primary" href="/offerte-aanvragen/">Vraag gratis offertes aan</a></p>
</div>"""


def _artikel(a, write, today):
    url = _url(a["slug"])
    kort_kruimel = a["titel"].split(":")[0]
    cr, cr_ld = crumbs([("Home", "/"), ("Kennisbank", "/kennisbank/"), (kort_kruimel, None)])
    f = FOTO_OP_NAAM[a["foto"]]
    secties = "".join(f"<h2>{t}</h2>{h}" for t, h in a["secties"])
    stappen = "".join(f"<li><strong>{t}.</strong> {p}</li>" for t, p in a["stappen"])
    bronnen = "".join(f'<li><a href="{htmllib.escape(u)}" rel="nofollow noopener">{htmllib.escape(lab)}</a></li>'
                      for lab, u in a["bronnen"])
    extra = "".join(f'<li><a href="{u}">{t}</a></li>' for u, t in a.get("extra_links", []))
    verder = "".join(f"<li>{_link(s)}</li>" for s in a["gerelateerd"]) + extra
    faq_html, faq_ld = faq_blok(a["faq"], "Veelgestelde vragen")
    credit = ""
    if f["licentie"] not in ("CC0", "CC0 1.0", "Public domain"):
        credit = (f'<p class="foto-credit"><small>Foto: {htmllib.escape(f["maker"])}, '
                  f'<a href="{htmllib.escape(f["licentie_url"])}" rel="nofollow noopener license">{f["licentie"]}</a>, '
                  f'via <a href="{htmllib.escape(f["bron"])}" rel="nofollow noopener">Wikimedia Commons</a> '
                  f'(<a href="/fotoverantwoording/">bewerkt</a>).</small></p>')

    body = f"""{cr}
<article class="section-sm"><div class="wrap narrow prose">
  <span class="badge">Kennisbank</span>
  <h1>{a['titel']}</h1>
  <p class="lead">{a['intro']}</p>
  <p><small>Bijgewerkt op {today[8:10]}-{today[5:7]}-{today[:4]} · door de redactie van Topschilder</small></p>
  {foto(f, "(max-width:760px) calc(100vw - 40px), 720px", boven_vouw=True)}
  {credit}
  <div class="callout"><p><strong>Kort antwoord:</strong> {a['kort_antwoord']}</p></div>
  {secties}
  <h2 id="stappen">Stap voor stap</h2>
  <ol>{stappen}</ol>
  {_kosten_blok(a)}
  <h2>Bronnen</h2>
  <ul style="font-size:.9rem">{bronnen}</ul>
  <p><small>Technische gegevens verschillen per product en per versie van het technische blad. Volg altijd de aanwijzingen op het blik of in het actuele blad van de verf die je gebruikt.</small></p>
  <h2>Verder lezen</h2>
  <ul>{verder}</ul>
</div></article>
{faq_html}
{cta_blok("Liever een vakman?", "Vraag gratis en vrijblijvend offertes aan bij maximaal drie schilders uit jouw regio en vergelijk ze naast elkaar.")}"""

    art_ld = {
        "@context": "https://schema.org", "@type": "Article",
        "headline": a["titel"], "description": a["description"],
        "image": SITE["url"] + f"/assets/fotos/{f['naam']}-1600.webp",
        "inLanguage": "nl-NL", "datePublished": GEPUBLICEERD, "dateModified": today,
        "author": {"@id": SITE["url"] + "/#organization"},
        "publisher": {"@id": SITE["url"] + "/#organization"},
        "mainEntityOfPage": SITE["url"] + url,
        "isPartOf": {"@type": "CollectionPage", "@id": SITE["url"] + "/kennisbank/"},
    }
    # seo-ronde 4: het stappenplan ook als HowTo-schema
    howto_ld = {
        "@context": "https://schema.org", "@type": "HowTo",
        "name": a.get("howto_naam") or a["titel"].split(":")[0],
        "description": a["kort_antwoord"],
        "image": art_ld["image"], "inLanguage": "nl-NL",
        "step": [{"@type": "HowToStep", "position": i + 1, "name": t, "text": p,
                  "url": SITE["url"] + url + "#stappen"}
                 for i, (t, p) in enumerate(a["stappen"])],
    }
    write(url, page(title(a["seo_titel"]), a["description"], url, body, [cr_ld, faq_ld, art_ld, howto_ld]), prio=0.7)


def _kaart(href, titel_, oms, f=None):
    beeld = foto(f, "(max-width:600px) calc(100vw - 40px), 360px") if f else ""
    return (f'<div class="card">{beeld}<h3 style="font-size:1.08rem"><a href="{href}">{titel_}</a></h3>'
            f'<p>{oms}</p><p><a class="go" href="{href}">Lees meer →</a></p></div>')


def _hub(write, today):
    cr, cr_ld = crumbs([("Home", "/"), ("Kennisbank", None)])
    blokken = ""
    for g in GROEPEN:
        kaarten = "".join(_kaart(_url(a["slug"]), a["titel"], a["kort"], FOTO_OP_NAAM[a["foto"]])
                          for a in ARTIKELEN if a["groep"] == g)
        kaarten += "".join(_kaart(h, t, o, FOTO_OP_NAAM[fn]) for h, t, o, gg, fn in GIDSEN_IN_HUB if gg == g)
        blokken += f'<h2 style="margin-top:38px">{g}</h2><div class="grid g3" style="margin-top:16px">{kaarten}</div>'
    kosten = "".join(f'<li><a href="/kosten/{k["slug"]}/">Wat kost {k["klus"]}?</a></li>' for k in KOSTEN)
    body = f"""{cr}
<section class="section-sm"><div class="wrap">
  <div class="narrow prose">
    <span class="badge">Kennisbank</span>
    <h1>Kennisbank schilderwerk</h1>
    <p class="lead">Praktische uitleg over verf, voorbereiding, schade en offertes. Of je nu zelf de kwast oppakt of een schilder inhuurt: hier lees je hoe het hoort, met stappenplannen en bronnen.</p>
    {foto(HUB_FOTO, "(max-width:760px) calc(100vw - 40px), 720px", boven_vouw=True)}
  </div>
  {blokken}
  <div class="narrow prose" style="margin-top:38px">
    <h2>Wat kost schilderwerk?</h2>
    <p>Bij elk artikel staat wat het kost om het te laten doen. Alle richtprijzen per klus:</p>
    <ul>{kosten}</ul>
    <p>Heb je al een offerte? <a href="/offerte-vergelijken/">Laat hem gratis checken</a> of lees <a href="/kennisbank/goede-offerte-schilderwerk/">wat er in een goede offerte staat</a>.</p>
  </div>
</div></section>
{cta_blok()}"""
    items = [{"@type": "ListItem", "position": i + 1, "url": SITE["url"] + _url(a["slug"]), "name": a["titel"]}
             for i, a in enumerate(ARTIKELEN)]
    lijst_ld = {"@context": "https://schema.org", "@type": "CollectionPage", "@id": SITE["url"] + "/kennisbank/",
                "name": "Kennisbank schilderwerk", "inLanguage": "nl-NL",
                "mainEntity": {"@type": "ItemList", "itemListElement": items}}
    write("/kennisbank/", page(title("Kennisbank schilderwerk: verf, voorbereiding en offertes"),
          "Praktische uitleg over schilderwerk: welke verf voor kozijnen, nieuw stucwerk schilderen, schimmel op de muur, verf die bladdert, tegels verven en een goede offerte.",
          "/kennisbank/", body, [cr_ld, lijst_ld]), prio=0.8)


def build_kennisbank(write, today):
    for a in ARTIKELEN:
        _artikel(a, write, today)
    _hub(write, today)


def fotogroepen():
    """Voor de fotoverantwoording: foto's per kennisbankartikel (alleen nieuwe of nog niet vermelde)."""
    groepen = [("Kennisbank", [HUB_FOTO])]
    groepen += [(f"Kennisbank: {a['titel'].split(':')[0]}", [FOTO_OP_NAAM[a["foto"]]]) for a in ARTIKELEN]
    return groepen
