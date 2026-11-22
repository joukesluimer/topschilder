# -*- coding: utf-8 -*-
"""
Fotogalerij voor /inspiratie/ en de gidsen /inspiratie/{type}/.

- Echte foto's: foto_data.FOTOS_INSPIRATIE (de eerste ronde) en galerij_fotos.FOTOS_GALERIJ
  (deze ronde). Alles van Wikimedia Commons met vrije licentie; maker, licentie en bron
  staan bij elke foto in de lightbox en op /fotoverantwoording/.
- Illustraties: kleurvarianten en een voor-en-na per woningtype, getekend met dezelfde
  SVG-woningen als de kleurenkiezer. Die staan er altijd met het label ‘Illustratie’:
  het zijn geen foto’s van echte huizen of projecten.

Filters (woningtype, kleur, onderdeel, foto of illustratie), lightbox en lazy loading.
CSS en JS staan onderaan; inspiratie.py zet ze achter inspiratie.css en inspiratie.js.
"""

import html as _html

from foto_data import FOTOS_INSPIRATIE
from galerij_fotos import FOTOS_GALERIJ

# Kleur- en onderdeel-labels voor bestaande foto's uit de eerste ronde (naam -> (kleuren, onderdelen))
TAGS_BESTAAND = {
    "jaren30-dubbel-woonhuis-helstlaan-hilversum": (["wit"], ["gevel", "kozijnen"]),
    "jaren30-dubbel-woonhuis-zonnelaan-hilversum": (["wit", "zwart"], ["kozijnen"]),
    "jaren70-rijtjeshuizen-wold-lelystad": (["wit"], ["gevel", "boeidelen"]),
    "villa-landhuis-soestdijkerstraatweg-hilversum": (["wit"], ["gevel", "kozijnen"]),
    "villa-landhuis-zuidereind-hilversum": (["wit"], ["gevel", "luiken"]),
    "polder-wederopbouwboerderij-tollebeek": (["blauw"], ["gevel"]),
    "polder-wederopbouwboerderij-emmeloord": (["groen"], ["gevel"]),
    "monument-zuiderwalstraat-elburg": (["wit", "zwart"], ["luiken", "voordeur"]),
    "monument-ijsselkade-kampen": (["wit", "blauw"], ["voordeur", "kozijnen"]),
    "nieuwbouw-aresstraat-homeruskwartier-almere": (["zwart"], ["gevel"]),
    "nieuwbouw-rijwoningen-homeruskwartier-almere": (["grijs", "rood"], ["gevel"]),
}

KLEUREN = [  # (sleutel, label, staal)
    ("wit", "Wit en crème", "#efebdc"),
    ("grijs", "Grijs", "#a7aca9"),
    ("zwart", "Zwart en antraciet", "#373f43"),
    ("groen", "Groen", "#31403d"),
    ("blauw", "Blauw", "#3e5674"),
    ("rood", "Rood", "#7a2a2e"),
    ("geel", "Geel en oker", "#d2aa6d"),
    ("hout", "Houtkleur", "#b88a53"),
]
KLEUR_LABEL = {k: n for k, n, _ in KLEUREN}

ONDERDELEN = [
    ("gevel", "Gevel"), ("kozijnen", "Kozijnen en ramen"), ("voordeur", "Voordeur"),
    ("luiken", "Luiken"), ("boeidelen", "Boeidelen"), ("interieur", "Interieur"),
    ("voor-en-na", "Voor en na"),
]
ONDERDEEL_LABEL = dict(ONDERDELEN)

# Verfkleur uit de kleurenkiezer -> kleurgroep in het filter
KLEURGROEP = {
    "cremewit": "wit", "gebroken-wit": "wit", "wit": "wit", "lichtgrijs": "grijs",
    "antraciet": "zwart", "zwart": "zwart", "gooiers-groen": "groen", "monumentengroen": "groen",
    "olijfgroen": "groen", "salie": "groen", "staalblauw": "blauw", "nachtblauw": "blauw",
    "ossenbloed": "rood", "bentheimer": "geel", "eiken": "hout", "noten": "hout",
}

# Drie extra kleurvarianten per woningtype (illustraties). Andere combinaties dan de twee
# uitgewerkte stijlen op de pagina, zodat je ziet wat een andere kleur met dezelfde gevel doet.
VARIANTEN = [
    {"type": "jaren30", "naam": "Donkerblauw en crème", "kozijn": "cremewit", "raam": "nachtblauw", "deur": "nachtblauw", "boei": "cremewit", "gevel": "bruin"},
    {"type": "jaren30", "naam": "Olijfgroen met okergele deur", "kozijn": "gebroken-wit", "raam": "olijfgroen", "deur": "bentheimer", "boei": "olijfgroen", "gevel": "rood"},
    {"type": "jaren30", "naam": "Zwartgroen op gele steen", "kozijn": "monumentengroen", "raam": "cremewit", "deur": "monumentengroen", "boei": "monumentengroen", "gevel": "geel"},
    {"type": "jaren70", "naam": "Wit met donkerblauwe deur", "kozijn": "wit", "raam": "wit", "deur": "nachtblauw", "boei": "wit", "gevel": "bruin"},
    {"type": "jaren70", "naam": "Grijsgroen en lichtgrijs", "kozijn": "lichtgrijs", "raam": "salie", "deur": "monumentengroen", "boei": "lichtgrijs", "gevel": "rood"},
    {"type": "jaren70", "naam": "Zwart met houtkleur", "kozijn": "zwart", "raam": "zwart", "deur": "eiken", "boei": "zwart", "gevel": "geel"},
    {"type": "villa", "naam": "Wijnrood en crème", "kozijn": "cremewit", "raam": "ossenbloed", "deur": "ossenbloed", "boei": "cremewit", "gevel": "rood"},
    {"type": "villa", "naam": "Grijsblauw landhuis", "kozijn": "gebroken-wit", "raam": "staalblauw", "deur": "nachtblauw", "boei": "gebroken-wit", "gevel": "wit"},
    {"type": "villa", "naam": "Olijfgroen en wit", "kozijn": "wit", "raam": "olijfgroen", "deur": "olijfgroen", "boei": "wit", "gevel": "bruin"},
    {"type": "polder", "naam": "Antraciet en houtkleur", "kozijn": "antraciet", "raam": "antraciet", "deur": "eiken", "boei": "antraciet", "gevel": "rood"},
    {"type": "polder", "naam": "Wit met groene deur", "kozijn": "wit", "raam": "wit", "deur": "gooiers-groen", "boei": "wit", "gevel": "bruin"},
    {"type": "polder", "naam": "Okergeel accent", "kozijn": "cremewit", "raam": "cremewit", "deur": "bentheimer", "boei": "antraciet", "gevel": "geel"},
    {"type": "monument", "naam": "Grijsblauw historisch", "kozijn": "cremewit", "raam": "staalblauw", "deur": "nachtblauw", "boei": "cremewit", "gevel": "rood"},
    {"type": "monument", "naam": "Zwarte deur, witte lijsten", "kozijn": "wit", "raam": "wit", "deur": "zwart", "boei": "wit", "gevel": "bruin"},
    {"type": "monument", "naam": "Dennengroen op witte gevel", "kozijn": "gooiers-groen", "raam": "cremewit", "deur": "gooiers-groen", "boei": "gooiers-groen", "gevel": "wit"},
    {"type": "nieuwbouw", "naam": "Licht met donkere deur", "kozijn": "lichtgrijs", "raam": "lichtgrijs", "deur": "antraciet", "boei": "antraciet", "gevel": "rood"},
    {"type": "nieuwbouw", "naam": "Zwart en wit", "kozijn": "zwart", "raam": "zwart", "deur": "zwart", "boei": "zwart", "gevel": "wit"},
    {"type": "nieuwbouw", "naam": "Olijfgroen op donkere steen", "kozijn": "olijfgroen", "raam": "olijfgroen", "deur": "noten", "boei": "antraciet", "gevel": "antraciet"},
]

# Voor en na per woningtype: oud (verweerd getekend) -> nieuw
VOOR_NA = {
    "jaren30": ({"kozijn": "wit", "raam": "wit", "deur": "staalblauw", "boei": "wit"},
                {"kozijn": "cremewit", "raam": "monumentengroen", "deur": "ossenbloed", "boei": "cremewit"}, "bruin"),
    "jaren70": ({"kozijn": "noten", "raam": "noten", "deur": "noten", "boei": "noten"},
                {"kozijn": "antraciet", "raam": "antraciet", "deur": "bentheimer", "boei": "antraciet"}, "bruin"),
    "villa": ({"kozijn": "wit", "raam": "wit", "deur": "noten", "boei": "wit"},
              {"kozijn": "cremewit", "raam": "gooiers-groen", "deur": "gooiers-groen", "boei": "cremewit"}, "rood"),
    "polder": ({"kozijn": "eiken", "raam": "eiken", "deur": "eiken", "boei": "eiken"},
               {"kozijn": "gebroken-wit", "raam": "salie", "deur": "olijfgroen", "boei": "gebroken-wit"}, "rood"),
    "monument": ({"kozijn": "wit", "raam": "wit", "deur": "noten", "boei": "wit"},
                 {"kozijn": "cremewit", "raam": "cremewit", "deur": "monumentengroen", "boei": "cremewit"}, "rood"),
    "nieuwbouw": ({"kozijn": "wit", "raam": "wit", "deur": "wit", "boei": "wit"},
                  {"kozijn": "antraciet", "raam": "antraciet", "deur": "eiken", "boei": "zwart"}, "wit"),
}

_N_START = 300  # id-teller voor de SVG's, ver boven die van de stijlkaarten

# Illustraties worden losse .svg-bestanden (lazy geladen, houdt de HTML klein).
SVG_PAD = "/assets/inspiratie/"
_SVG_BESTANDEN = {}


def _bewaar(naam, svg):
    """Bewaar een SVG als bestand; geeft (url, aria-label)."""
    import re
    svg = re.sub(r' class="[^"]*"', "", svg[:svg.index(">")], count=1) + svg[svg.index(">"):]
    _SVG_BESTANDEN[naam] = svg
    m = re.search(r'aria-label="([^"]*)"', svg)
    return f"{SVG_PAD}{naam}.svg", (m.group(1) if m else "")


def schrijf_svgs(out_dir):
    import os
    map_ = os.path.join(out_dir, "assets", "inspiratie")
    os.makedirs(map_, exist_ok=True)
    for naam, svg in _SVG_BESTANDEN.items():
        with open(os.path.join(map_, f"{naam}.svg"), "w", encoding="utf-8") as fh:
            fh.write('<?xml version="1.0" encoding="UTF-8"?>\n' + svg)


def _slug(t):
    import re, unicodedata
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


def _e(t):
    return _html.escape(str(t), quote=True)


def _foto_item(f, typ, kleuren, onderdelen):
    return {"soort": "foto", "type": typ, "kleuren": kleuren, "onderdelen": onderdelen, "f": f}


def foto_items(typ=None):
    """Alle echte foto's, eventueel voor één woningtype."""
    items = []
    for k, lijst in FOTOS_INSPIRATIE.items():
        for f in lijst:
            kl, od = TAGS_BESTAAND.get(f["naam"], ([], ["gevel"]))
            items.append(_foto_item(f, k, kl, od))
    for f in FOTOS_GALERIJ:
        items.append(_foto_item(f, f["type"], f["kleuren"], f["onderdelen"]))
    return [i for i in items if typ is None or i["type"] == typ]


def illustratie_items(typ=None):
    """Kleurvarianten en voor-en-na (getekend). Volgorde: per type eerst voor-en-na."""
    from inspiratie import WONINGTYPES
    items = []
    n = _N_START
    for k, _naam, _kort in WONINGTYPES:
        oud, nieuw, gevel = VOOR_NA[k]
        items.append({"soort": "voorna", "type": k, "oud": dict(oud, type=k, gevel=gevel),
                      "nieuw": dict(nieuw, type=k, gevel=gevel), "n": n,
                      "kleuren": sorted({KLEURGROEP[v] for v in nieuw.values()}), "onderdelen": ["voor-en-na"]})
        n += 3
        for v in VARIANTEN:
            if v["type"] != k:
                continue
            items.append({"soort": "variant", "type": k, "st": v, "n": n,
                          "kleuren": sorted({KLEURGROEP[v[d]] for d in ("kozijn", "raam", "deur", "boei")}),
                          "onderdelen": ["kozijnen", "voordeur", "boeidelen"]})
            n += 1
    return [i for i in items if typ is None or i["type"] == typ]


def _gemengd(fotos, illus):
    """Foto's en illustraties door elkaar: na elke drie foto's een illustratie."""
    uit, fi, ii = [], 0, 0
    while fi < len(fotos) or ii < len(illus):
        for _ in range(3):
            if fi < len(fotos):
                uit.append(fotos[fi]); fi += 1
        if ii < len(illus):
            uit.append(illus[ii]); ii += 1
    return uit


def _type_volgorde(items):
    """Door elkaar op woningtype, zodat de eerste rij al verschillende huizen laat zien."""
    from inspiratie import WONINGTYPES
    per = {k: [i for i in items if i["type"] == k] for k, _n, _ in WONINGTYPES}
    per["binnen"] = [i for i in items if i["type"] == "binnen"]
    uit = []
    while any(per.values()):
        for k in list(per):
            if per[k]:
                uit.append(per[k].pop(0))
    return uit


# ---------------------------------------------------------------------------
# HTML
# ---------------------------------------------------------------------------

def _labels(item, met_type):
    from inspiratie import WONINGTYPE_NAAM
    delen = []
    if met_type:
        delen.append("Binnen" if item["type"] == "binnen" else WONINGTYPE_NAAM[item["type"]])
    if item["soort"] == "foto":
        delen.append(ONDERDEEL_LABEL[item["onderdelen"][0]])
    elif item["soort"] == "voorna":
        delen.append("Voor en na")
    else:
        delen.append("Kleurvariant")
    return " · ".join(delen)


def _data_attr(item):
    return (f'data-type="{item["type"]}" data-kleur="{" ".join(item["kleuren"])}" '
            f'data-onderdeel="{" ".join(item["onderdelen"])}" '
            f'data-soort="{"foto" if item["soort"] == "foto" else "illustratie"}"')


def _tegel_foto(item, met_type, idx):
    f = item["f"]
    n = f["naam"]
    alt = _e(f["alt"])
    credit_kort = f'Foto: {_e(f["maker"])} · {_e(f["licentie"])}'
    info = (f'<p class="gl-lb-tekst">{_e(f["onderschrift"])}</p>'
            f'<p class="gl-lb-credit">Foto: {_e(f["maker"])}, '
            f'<a href="{_e(f["licentie_url"])}" rel="license nofollow noopener" target="_blank">{_e(f["licentie"])}</a>, '
            f'<a href="{_e(f["bron"])}" rel="nofollow noopener" target="_blank">bron: Wikimedia Commons</a>. '
            f'<a href="/fotoverantwoording/">Alle fotovermeldingen</a></p>')
    return (f'<figure class="gl-item" {_data_attr(item)} data-groot="/assets/fotos/{n}-1600.webp" data-i="{idx}">'
            f'<button type="button" class="gl-open" aria-label="Vergroot foto: {alt}">'
            f'<img src="/assets/fotos/{n}-400.webp" srcset="/assets/fotos/{n}-400.webp 400w, /assets/fotos/{n}-800.webp 800w" '
            f'sizes="(max-width:640px) calc(50vw - 26px), (max-width:1000px) 31vw, 300px" width="{f["w"]}" height="{f["h"]}" '
            f'alt="{alt}" loading="lazy" decoding="async"></button>'
            f'<figcaption><span class="gl-tag">{_labels(item, met_type)}</span>'
            f'<span class="gl-bij">{_e(f["onderschrift"])}</span><span class="gl-credit">{credit_kort}</span></figcaption>'
            f'<div class="gl-info" hidden>{info}</div></figure>')


def _kleurregel(st):
    from inspiratie_gids import kleur_label
    return (f'Kozijnen {kleur_label(st["kozijn"])}, ramen {kleur_label(st["raam"])}, '
            f'voordeur {kleur_label(st["deur"])}, boeidelen {kleur_label(st["boei"])}.')


def _kiezer(st):
    from inspiratie import kiezer_link
    return f'<a class="btn btn-primary gl-lb-knop" href="{kiezer_link(st)}">Probeer in de kleurenkiezer</a>'


def _tegel_variant(item, met_type, idx):
    from inspiratie import svg_stijl
    st = item["st"]
    url, label = _bewaar(f'{st["type"]}-kleurvariant-{_slug(st["naam"])}', svg_stijl(st, item["n"]))
    regel = _kleurregel(st)
    info = (f'<p class="gl-lb-tekst"><strong>{_e(st["naam"])}.</strong> {_e(regel)}</p>'
            f'<p class="gl-lb-credit">Illustratie van Topschilder, geen foto van een echt huis. Kleuren op een scherm wijken af van echte verf.</p>'
            f'{_kiezer(st)}')
    return (f'<figure class="gl-item gl-illu" {_data_attr(item)} data-groot="{url}" data-i="{idx}">'
            f'<button type="button" class="gl-open" aria-label="Vergroot illustratie: {_e(st["naam"])}">{_img_svg(url, label)}</button>'
            f'<figcaption><span class="gl-tag">{_labels(item, met_type)}</span>'
            f'<span class="gl-bij">{_e(st["naam"])}</span><span class="gl-credit">Illustratie, geen foto</span></figcaption>'
            f'<div class="gl-info" hidden>{info}</div></figure>')


def _img_svg(url, label):
    return (f'<img class="gl-svg" src="{url}" width="640" height="440" alt="{label}" loading="lazy" decoding="async">')


def _binnen(svg):
    """Alleen de inhoud van een <svg>…</svg>."""
    return svg[svg.index(">") + 1:svg.rindex("</svg>")]


def svg_voor_na(item):
    from inspiratie import svg_stijl, HUIS_OMSCHRIJVING
    n = item["n"]
    na = _binnen(svg_stijl(item["nieuw"], n + 1))
    # zonder eigen lucht: links blijft de lucht van ‘na’ zichtbaar, alleen het huis is verweerd
    voor = _binnen(svg_stijl(item["oud"], n + 2)).replace(f'fill="url(#ip{n + 2}-lucht)"', 'fill="none"')
    c, flt, pat = f"vn{n}-clip", f"vn{n}-oud", f"vn{n}-bladder"
    wit, msk, grp = f"vn{n}-wit", f"vn{n}-masker", f"vn{n}-voor"
    defs = (f'<defs><clipPath id="{c}"><rect class="vn-clip" x="0" y="0" width="320" height="440"/></clipPath>'
            f'<filter id="{flt}" color-interpolation-filters="sRGB"><feColorMatrix type="saturate" values=".4"/>'
            f'<feComponentTransfer><feFuncR type="linear" slope=".85" intercept=".1"/><feFuncG type="linear" slope=".83" intercept=".09"/>'
            f'<feFuncB type="linear" slope=".78" intercept=".07"/></feComponentTransfer></filter>'
            f'<filter id="{wit}"><feFlood flood-color="#fff"/><feComposite in2="SourceAlpha" operator="in"/></filter>'
            f'<mask id="{msk}" maskUnits="userSpaceOnUse" x="0" y="0" width="640" height="400"><use href="#{grp}" filter="url(#{wit})"/></mask>'
            f'<pattern id="{pat}" width="46" height="38" patternUnits="userSpaceOnUse">'
            f'<path d="M6 8q3-3 6 0t5 3l-4 2z" fill="#fff" opacity=".45"/><path d="M28 24q4-2 7 1l-3 3q-3 0-4-4z" fill="#fff" opacity=".35"/>'
            f'<path d="M18 30l1 7M38 6l-1 6M10 20l2 5" stroke="#5b4a36" stroke-width="1.1" opacity=".35"/>'
            f'<circle cx="40" cy="34" r="1.6" fill="#4a3c2c" opacity=".3"/></pattern></defs>')
    label = (f"Illustratie voor en na van een {HUIS_OMSCHRIJVING[item['type']]}: links verweerd houtwerk, "
             f"rechts opnieuw geschilderd. {_kleurregel(item['nieuw'])}")
    lbl = ('<g class="vn-lbl" font-family="system-ui,sans-serif" font-size="17" font-weight="700">'
           '<rect class="vn-lv" x="12" y="12" width="64" height="30" rx="15" fill="rgba(23,32,51,.82)"/>'
           '<text class="vn-tv" x="44" y="32" text-anchor="middle" fill="#fff">Voor</text>'
           '<rect class="vn-ln" x="574" y="12" width="54" height="30" rx="15" fill="#e8590c"/>'
           '<text x="601" y="32" text-anchor="middle" fill="#fff">Na</text></g>')
    return (f'<svg class="gl-svg gl-vn" viewBox="0 0 640 440" xmlns="http://www.w3.org/2000/svg" role="img" '
            f'aria-label="{_e(label)}">{defs}<g>{na}</g>'
            f'<g clip-path="url(#{c})"><g id="{grp}" filter="url(#{flt})">{voor}</g>'
            f'<rect width="640" height="400" fill="url(#{pat})" mask="url(#{msk})"/></g>'
            f'<line class="vn-lijn" x1="320" y1="0" x2="320" y2="440" stroke="#fff" stroke-width="4"/>'
            f'<circle class="vn-knop" cx="320" cy="220" r="15" fill="#fff" stroke="rgba(0,0,0,.25)"/>'
            f'<path class="vn-pijl" d="M313 214l-6 6 6 6M327 214l6 6-6 6" stroke="#172033" stroke-width="2.4" fill="none" '
            f'transform="translate(0 0)"/>{lbl}</svg>')


def _tegel_voorna(item, met_type, idx):
    from inspiratie import WONINGTYPE_NAAM
    naam = WONINGTYPE_NAAM[item["type"]].lower()
    info = (f'<p class="gl-lb-tekst"><strong>Voor en na.</strong> Links verweerd houtwerk, rechts opnieuw geschilderd. '
            f'Nieuw: {_e(_kleurregel(item["nieuw"]))} Schuif om te vergelijken.</p>'
            f'<p class="gl-lb-credit">Illustratie van Topschilder, geen foto van een echt huis.</p>'
            f'{_kiezer(item["nieuw"])}')
    url, label = _bewaar(f'{item["type"]}-voor-en-na', svg_voor_na(item))
    return (f'<figure class="gl-item gl-illu gl-voorna" {_data_attr(item)} data-svg="{url}" data-i="{idx}">'
            f'<button type="button" class="gl-open" aria-label="Vergroot illustratie voor en na: {_e(naam)}">{_img_svg(url, label)}</button>'
            f'<figcaption><span class="gl-tag">{_labels(item, met_type)}</span>'
            f'<span class="gl-bij">Van verweerd naar fris</span><span class="gl-credit">Illustratie, geen foto</span></figcaption>'
            f'<div class="gl-info" hidden>{info}</div></figure>')


def _tegel(item, met_type, idx):
    if item["soort"] == "foto":
        return _tegel_foto(item, met_type, idx)
    if item["soort"] == "voorna":
        return _tegel_voorna(item, met_type, idx)
    return _tegel_variant(item, met_type, idx)


def _knoppen(groep, opties, label):
    knoppen = f'<button type="button" class="gl-f on" data-groep="{groep}" data-waarde="alle" aria-pressed="true">Alles</button>'
    for k, n, *staal in opties:
        sw = f'<i style="background:{staal[0]}"></i>' if staal else ""
        knoppen += (f'<button type="button" class="gl-f" data-groep="{groep}" data-waarde="{k}" aria-pressed="false">'
                    f'{sw}{n}</button>')
    return (f'<div class="gl-fgroep"><span class="gl-flabel" id="gl-l-{groep}">{label}</span>'
            f'<div class="gl-frij" role="group" aria-labelledby="gl-l-{groep}">{knoppen}</div></div>')


def galerij(typ=None, kop="Fotogalerij", intro="", eerst=None, h="h2"):
    """De galerij. Zonder typ: alle woningtypes met een filter op type; met typ: één woningtype."""
    from inspiratie import WONINGTYPES
    if typ:
        items = _gemengd(foto_items(typ), illustratie_items(typ))
    else:
        items = _gemengd(_type_volgorde(foto_items()), _type_volgorde(illustratie_items()))
    met_type = typ is None
    aantal_f = sum(1 for i in items if i["soort"] == "foto")
    aantal_i = len(items) - aantal_f
    kleuren_aanwezig = {k for i in items for k in i["kleuren"]}
    onderdelen_aanwezig = {k for i in items for k in i["onderdelen"]}
    filters = ""
    if met_type:
        filters += _knoppen("type", [(k, kort) for k, _n, kort in WONINGTYPES] + [("binnen", "Binnen")], "Woningtype")
    filters += _knoppen("kleur", [k for k in KLEUREN if k[0] in kleuren_aanwezig], "Kleur")
    filters += _knoppen("onderdeel", [k for k in ONDERDELEN if k[0] in onderdelen_aanwezig], "Onderdeel")
    filters += _knoppen("soort", [("foto", "Foto’s"), ("illustratie", "Illustraties")], "Soort")
    tegels = "".join(_tegel(it, met_type, i) for i, it in enumerate(items))
    meer = (f'<div class="gl-meer-wrap"><button type="button" class="btn btn-ghost gl-meer" hidden>Toon meer</button></div>'
            if eerst else "")
    return f"""<section class="section-sm gl-sec" id="galerij"><div class="wrap">
  <{h} class="gl-kop">{kop}</{h}>
  <p class="gl-intro">{intro or f"{aantal_f} foto’s van echte woningen en {aantal_i} illustraties met kleurideeën. Filter op kleur of onderdeel en klik op een beeld om het groot te zien."}</p>
  <div class="gl-filters" hidden>{filters}</div>
  <p class="gl-telling" role="status" aria-live="polite"></p>
  <div class="gl-grid" data-eerst="{eerst or 0}">{tegels}</div>
  <p class="gl-leeg" hidden>Geen beelden met deze combinatie. <button type="button" class="gl-reset">Wis de filters</button></p>
  {meer}
  <p class="gl-noot">Foto’s: echte woningen, gemaakt door anderen en gedeeld onder een vrije licentie (maker en licentie staan bij elke foto en op de <a href="/fotoverantwoording/">fotoverantwoording</a>). Het zijn geen projecten van Topschilder of van aangesloten schilders. Beelden met het label ‘Illustratie’ zijn tekeningen.</p>
</div></section>"""


def fotogroepen():
    """Groepen voor /fotoverantwoording/."""
    from inspiratie import WONINGTYPES
    groepen = [(f"Inspiratiegalerij: {n}", [f for f in FOTOS_GALERIJ if f["type"] == k]) for k, n, _ in WONINGTYPES]
    groepen.append(("Inspiratiegalerij: binnen", [f for f in FOTOS_GALERIJ if f["type"] == "binnen"]))
    return [(n, l) for n, l in groepen if l]


# ---------------------------------------------------------------------------
# CSS en JS (achter inspiratie.css / inspiratie.js)
# ---------------------------------------------------------------------------

GALERIJ_CSS = r'''
/* === inspiratie-galerij: filters, tegels en lightbox === */
.gl-sec{padding-top:20px}
.gl-kop{margin-bottom:.2em}
.gl-intro{max-width:66ch;color:var(--body);margin:0 0 14px}
.gl-filters{display:grid;gap:10px;margin:0 0 6px;padding:14px;background:#fff;border:1px solid var(--line);border-radius:var(--radius-lg)}
.gl-filters[hidden]{display:none}
.gl-fgroep{display:grid;grid-template-columns:104px minmax(0,1fr);align-items:center;gap:8px}
.gl-flabel{font-size:.74rem;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}
.gl-frij{display:flex;flex-wrap:wrap;gap:6px;min-width:0}
.gl-f{display:inline-flex;align-items:center;gap:6px;border:1px solid var(--line);background:#fff;border-radius:99px;padding:6px 12px;font:inherit;font-size:.86rem;font-weight:600;color:var(--ink);cursor:pointer;white-space:nowrap}
.gl-f i{width:14px;height:14px;border-radius:50%;box-shadow:inset 0 0 0 1px rgba(0,0,0,.2)}
.gl-f:hover{border-color:var(--navy-500,#3b4a6b)}
.gl-f.on{background:var(--navy);border-color:var(--navy);color:#fff}
.gl-f:focus-visible,.gl-open:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
.gl-telling{font-size:.85rem;color:var(--muted);min-height:1.3em;margin:6px 0 10px}
.gl-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px}
.gl-item{margin:0;display:flex;flex-direction:column;background:#fff;border:1px solid var(--line);border-radius:var(--radius-lg);overflow:hidden;box-shadow:var(--shadow);min-width:0}
.gl-item[hidden],.gl-item.gl-weg{display:none}
.gl-open{display:block;width:100%;padding:0;border:0;background:#f3eee5;cursor:zoom-in;position:relative;aspect-ratio:3/2;overflow:hidden}
.gl-open img,.gl-open .gl-svg{display:block;width:100%;height:100%;object-fit:cover;transition:transform .35s ease}
.gl-item:hover .gl-open img,.gl-item:hover .gl-open .gl-svg{transform:scale(1.04)}
.gl-illu .gl-open::after{content:"Illustratie";position:absolute;left:8px;top:8px;background:rgba(23,32,51,.8);color:#fff;font-size:.68rem;font-weight:700;letter-spacing:.04em;padding:3px 8px;border-radius:99px}
.gl-voorna .gl-open::after{content:"Illustratie";top:auto;bottom:8px}
.gl-item figcaption{display:flex;flex-direction:column;gap:2px;padding:9px 11px 11px;font-size:.84rem;line-height:1.35;min-width:0}
.gl-tag{font-size:.68rem;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:var(--accent-dark)}
.gl-bij{color:var(--ink)}
.gl-credit{font-size:.72rem;color:var(--muted);overflow-wrap:anywhere}
.gl-leeg{margin:16px 0;color:var(--muted)}
.gl-reset{border:0;background:none;color:var(--accent-dark);font:inherit;font-weight:700;text-decoration:underline;cursor:pointer;padding:0}
.gl-meer-wrap{text-align:center;margin-top:18px}
.gl-noot{font-size:.82rem;color:var(--muted);margin:18px 0 0;max-width:80ch}
/* lightbox */
.gl-lb{position:fixed;inset:0;z-index:1000;background:rgba(10,14,24,.92);display:flex;align-items:center;justify-content:center;padding:56px 64px 16px}
.gl-lb[hidden]{display:none}
.gl-lb-doos{display:flex;flex-direction:column;max-width:min(1200px,100%);max-height:100%;width:100%;min-height:0}
.gl-lb-beeld{flex:1 1 auto;min-height:0;display:flex;align-items:center;justify-content:center}
.gl-lb-beeld img,.gl-lb-beeld svg{display:block;max-width:100%;max-height:calc(100vh - 220px);width:auto;height:auto;border-radius:8px;background:#222}
.gl-lb-beeld svg,.gl-lb-beeld img[src$=".svg"]{width:min(100%,calc((100vh - 220px) * 1.4545));height:auto}
.gl-lb-onder{color:#e8ebf2;padding:12px 2px 0;font-size:.92rem;max-width:80ch}
.gl-lb-onder p{margin:0 0 .4em}
.gl-lb-onder a{color:#ffd2b8}
.gl-lb-credit{font-size:.8rem;color:#b9c0cf}
.gl-lb-knop{margin-top:6px;padding:9px 16px;font-size:.9rem}
.gl-lb-schuif{display:block;width:100%;max-width:520px;margin:10px auto 0;accent-color:var(--accent)}
.gl-lb-sluit,.gl-lb-vorige,.gl-lb-volgende{position:absolute;border:0;background:rgba(255,255,255,.12);color:#fff;width:46px;height:46px;border-radius:50%;font-size:1.5rem;line-height:1;cursor:pointer;display:grid;place-items:center}
.gl-lb-sluit:hover,.gl-lb-vorige:hover,.gl-lb-volgende:hover{background:rgba(255,255,255,.25)}
.gl-lb-sluit:focus-visible,.gl-lb-vorige:focus-visible,.gl-lb-volgende:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
.gl-lb-sluit{top:10px;right:12px}
.gl-lb-vorige{left:10px;top:50%;transform:translateY(-50%)}
.gl-lb-volgende{right:10px;top:50%;transform:translateY(-50%)}
.gl-lb-teller{position:absolute;top:22px;left:18px;color:#b9c0cf;font-size:.85rem}
body.gl-lb-open{overflow:hidden}
@media(max-width:1000px){.gl-grid{grid-template-columns:repeat(3,minmax(0,1fr))}}
@media(max-width:640px){
  .gl-filters{padding:10px;gap:8px}
  .gl-fgroep{grid-template-columns:minmax(0,1fr);gap:4px}
  .gl-frij{flex-wrap:nowrap;overflow-x:auto;scrollbar-width:none;padding-bottom:2px}
  .gl-frij::-webkit-scrollbar{display:none}
  .gl-f{flex:0 0 auto}
  .gl-grid{grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
  .gl-item figcaption{padding:7px 8px 9px;font-size:.78rem}
  .gl-credit{display:none}
  .gl-lb{padding:56px 8px 10px}
  .gl-lb-vorige,.gl-lb-volgende{top:auto;bottom:12px;transform:none;width:42px;height:42px}
  .gl-lb-onder{padding-bottom:52px;font-size:.86rem}
  .gl-lb-beeld img,.gl-lb-beeld svg{max-height:calc(100vh - 260px)}
}
@media(prefers-reduced-motion:reduce){.gl-open img,.gl-open .gl-svg{transition:none}.gl-item:hover .gl-open img,.gl-item:hover .gl-open .gl-svg{transform:none}}
/* === einde inspiratie-galerij === */
'''

GALERIJ_JS = r'''
/* === inspiratie-galerij: filters, "toon meer" en lightbox === */
(function () {
  "use strict";
  var sec = document.querySelector(".gl-sec");
  if (!sec) return;
  var grid = sec.querySelector(".gl-grid");
  var items = [].slice.call(grid.querySelectorAll(".gl-item"));
  var balk = sec.querySelector(".gl-filters");
  var telling = sec.querySelector(".gl-telling");
  var leeg = sec.querySelector(".gl-leeg");
  var meer = sec.querySelector(".gl-meer");
  var eerst = parseInt(grid.dataset.eerst, 10) || 0;
  var grens = eerst;
  var keuze = { type: "alle", kleur: "alle", onderdeel: "alle", soort: "alle" };
  balk.hidden = false;

  function past(el) {
    if (keuze.type !== "alle" && el.dataset.type !== keuze.type) return false;
    if (keuze.soort !== "alle" && el.dataset.soort !== keuze.soort) return false;
    if (keuze.kleur !== "alle" && (" " + el.dataset.kleur + " ").indexOf(" " + keuze.kleur + " ") < 0) return false;
    if (keuze.onderdeel !== "alle" && (" " + el.dataset.onderdeel + " ").indexOf(" " + keuze.onderdeel + " ") < 0) return false;
    return true;
  }
  function zichtbaar() { return items.filter(function (el) { return !el.hidden && !el.classList.contains("gl-weg"); }); }

  function toon() {
    var n = 0, f = 0, i = 0;
    items.forEach(function (el) {
      var ok = past(el);
      el.hidden = !ok;
      if (ok) {
        n++; if (el.dataset.soort === "foto") f++;
        el.classList.toggle("gl-weg", grens > 0 && n > grens);
      } else el.classList.remove("gl-weg");
    });
    if (meer) meer.hidden = !(grens > 0 && n > grens);
    if (leeg) leeg.hidden = n > 0;
    if (telling) telling.textContent = n + (n === 1 ? " beeld" : " beelden") + " (" + f + " foto’s, " + (n - f) + " illustraties)";
  }

  balk.addEventListener("click", function (e) {
    var b = e.target.closest(".gl-f");
    if (!b) return;
    keuze[b.dataset.groep] = b.dataset.waarde;
    balk.querySelectorAll('.gl-f[data-groep="' + b.dataset.groep + '"]').forEach(function (x) {
      var on = x === b;
      x.classList.toggle("on", on);
      x.setAttribute("aria-pressed", on);
    });
    toon();
  });
  function reset() {
    keuze = { type: "alle", kleur: "alle", onderdeel: "alle", soort: "alle" };
    balk.querySelectorAll(".gl-f").forEach(function (x) {
      var on = x.dataset.waarde === "alle";
      x.classList.toggle("on", on);
      x.setAttribute("aria-pressed", on);
    });
    toon();
  }
  var rs = sec.querySelector(".gl-reset");
  if (rs) rs.addEventListener("click", reset);
  if (meer) meer.addEventListener("click", function () { grens = 0; toon(); });
  // #galerij-polder enz. kiest direct een woningtype
  var h = location.hash.match(/^#galerij-([a-z0-9]+)$/);
  if (h) {
    var bt = balk.querySelector('.gl-f[data-groep="type"][data-waarde="' + h[1] + '"]');
    if (bt) bt.click();
  }
  toon();

  /* ---- lightbox ---- */
  var lb = document.createElement("div");
  lb.className = "gl-lb";
  lb.hidden = true;
  lb.setAttribute("role", "dialog");
  lb.setAttribute("aria-modal", "true");
  lb.setAttribute("aria-label", "Vergroot beeld");
  lb.innerHTML = '<span class="gl-lb-teller"></span><button type="button" class="gl-lb-sluit" aria-label="Sluiten">×</button>' +
    '<button type="button" class="gl-lb-vorige" aria-label="Vorige">‹</button><button type="button" class="gl-lb-volgende" aria-label="Volgende">›</button>' +
    '<div class="gl-lb-doos"><div class="gl-lb-beeld"></div><div class="gl-lb-onder"></div></div>';
  document.body.appendChild(lb);
  var beeld = lb.querySelector(".gl-lb-beeld"), onder = lb.querySelector(".gl-lb-onder");
  var teller = lb.querySelector(".gl-lb-teller");
  var lijst = [], pos = 0, terug = null;

  function schuif(svg, x) {
    var r = svg.querySelector(".vn-clip"); if (!r) return;
    r.setAttribute("width", x);
    svg.querySelector(".vn-lijn").setAttribute("x1", x);
    svg.querySelector(".vn-lijn").setAttribute("x2", x);
    svg.querySelector(".vn-knop").setAttribute("cx", x);
    svg.querySelector(".vn-pijl").setAttribute("transform", "translate(" + (x - 320) + " 0)");
    var lbl = svg.querySelector(".vn-lbl");
    if (lbl) {
      var v = x < 90 ? 0 : 1, n = x > 560 ? 0 : 1;
      lbl.querySelector(".vn-lv").style.opacity = v; lbl.querySelector(".vn-tv").style.opacity = v;
      lbl.querySelector(".vn-ln").style.opacity = n; lbl.lastChild.style.opacity = n;
    }
  }
  function laat(i) {
    pos = (i + lijst.length) % lijst.length;
    var el = lijst[pos];
    beeld.innerHTML = "";
    var img = el.querySelector("img");
    beeld.style.flexDirection = "";
    if (el.dataset.groot) {
      var nw = document.createElement("img");
      nw.src = el.dataset.groot;
      nw.alt = img.alt;
      nw.width = img.width === 640 ? 640 : 1600; nw.height = img.width === 640 ? 440 : 1067;
      beeld.appendChild(nw);
    } else if (el.dataset.svg) {
      var tijdelijk = img.cloneNode();
      tijdelijk.removeAttribute("class"); tijdelijk.loading = "eager";
      beeld.appendChild(tijdelijk);
      var mijn = pos;
      fetch(el.dataset.svg).then(function (r) { return r.text(); }).then(function (t) {
        if (mijn !== pos || lb.hidden) return;
        var d = document.createElement("div");
        d.innerHTML = t.replace(/^<\?xml[^>]*>\s*/, "");
        var s = d.querySelector("svg");
        if (!s) return;
        beeld.innerHTML = "";
        beeld.appendChild(s);
        var r = document.createElement("input");
        r.type = "range"; r.min = 0; r.max = 640; r.value = 320; r.className = "gl-lb-schuif";
        r.setAttribute("aria-label", "Schuif tussen voor en na");
        r.addEventListener("input", function () { schuif(s, r.value); });
        beeld.appendChild(r);
        beeld.style.flexDirection = "column";
      }).catch(function () {});
    }
    onder.innerHTML = el.querySelector(".gl-info").innerHTML;
    teller.textContent = (pos + 1) + " / " + lijst.length;
  }
  function open(el) {
    lijst = zichtbaar();
    terug = document.activeElement;
    lb.hidden = false;
    document.body.classList.add("gl-lb-open");
    laat(lijst.indexOf(el));
    lb.querySelector(".gl-lb-sluit").focus();
  }
  function dicht() {
    lb.hidden = true;
    beeld.innerHTML = "";
    document.body.classList.remove("gl-lb-open");
    if (terug) terug.focus();
  }
  grid.addEventListener("click", function (e) {
    var b = e.target.closest(".gl-open");
    if (b) open(b.closest(".gl-item"));
  });
  lb.querySelector(".gl-lb-sluit").addEventListener("click", dicht);
  lb.querySelector(".gl-lb-vorige").addEventListener("click", function () { laat(pos - 1); });
  lb.querySelector(".gl-lb-volgende").addEventListener("click", function () { laat(pos + 1); });
  lb.addEventListener("click", function (e) { if (e.target === lb || e.target === beeld) dicht(); });
  document.addEventListener("keydown", function (e) {
    if (lb.hidden) return;
    if (e.key === "Escape") dicht();
    else if (e.key === "ArrowLeft" && e.target.type !== "range") laat(pos - 1);
    else if (e.key === "ArrowRight" && e.target.type !== "range") laat(pos + 1);
    else if (e.key === "Tab") {
      var f = [].slice.call(lb.querySelectorAll("button, a, input"));
      var i = f.indexOf(document.activeElement);
      if (e.shiftKey && i <= 0) { e.preventDefault(); f[f.length - 1].focus(); }
      else if (!e.shiftKey && i === f.length - 1) { e.preventDefault(); f[0].focus(); }
    }
  });
  var x0 = null;
  lb.addEventListener("touchstart", function (e) { x0 = e.target.type === "range" ? null : e.touches[0].clientX; }, { passive: true });
  lb.addEventListener("touchend", function (e) {
    if (x0 === null) return;
    var dx = e.changedTouches[0].clientX - x0;
    if (Math.abs(dx) > 50) laat(pos + (dx < 0 ? 1 : -1));
    x0 = null;
  });
})();
/* === einde inspiratie-galerij === */
'''
