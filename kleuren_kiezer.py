# -*- coding: utf-8 -*-
"""
Kleurenkiezer voor gevel en kozijnen (/kleuren-kiezen/).

Alles van deze tool staat in dit ene bestand: de kleuren, de getekende woningen
(inline SVG), de pagina, de CSS en de JavaScript. build.py roept alleen
build_kleurenkiezer() aan en zet op een paar pagina's kleuren_teaser() neer.

Kleurnamen zijn beschrijvend. Het zijn geen merknamen of officiële kleurcodes:
de hexwaarden zijn een benadering voor op het scherm.
"""

import json
import os

from data import PLAATSEN, WONINGEN
from components import page, crumbs, offerte_form, faq_blok, title

PAD = "/kleuren-kiezen/"

# ---------------------------------------------------------------------------
# Kleuren
# ---------------------------------------------------------------------------

# (id, naam, hex, groep) — groep bepaalt de kopjes in het palet.
VERFKLEUREN = [
    ("cremewit", "Crèmewit", "#efe6cf", "Wit en crème"),
    ("gebroken-wit", "Gebroken wit", "#f2efe6", "Wit en crème"),
    ("wit", "Zuiver wit", "#fbfbf8", "Wit en crème"),
    ("zandbeige", "Zandbeige", "#d8c9a8", "Wit en crème"),
    ("lichtgrijs", "Lichtgrijs", "#c8cac7", "Grijs en zwart"),
    ("steengrijs", "Steengrijs", "#8b8f8f", "Grijs en zwart"),
    ("antraciet", "Antraciet", "#3a3e41", "Grijs en zwart"),
    ("zwart", "Diepzwart", "#1c1c1c", "Grijs en zwart"),
    ("gooiers-groen", "Gooiers groen", "#1f3a2c", "Groen"),
    ("monumentengroen", "Monumentengroen", "#34503f", "Groen"),
    ("olijfgroen", "Olijfgroen", "#6b6d47", "Groen"),
    ("salie", "Saliegroen", "#9aa58a", "Groen"),
    ("staalblauw", "Staalblauw", "#3b5068", "Rood en blauw"),
    ("nachtblauw", "Nachtblauw", "#1f2a3c", "Rood en blauw"),
    ("ossenbloed", "Ossenbloedrood", "#6a2420", "Rood en blauw"),
    ("zweeds-rood", "Zweeds rood", "#8b3326", "Rood en blauw"),
    ("bentheimer", "Bentheimer geel", "#d7b56d", "Geel en hout"),
    ("eiken", "Eiken (licht hout)", "#b88a53", "Geel en hout"),
    ("noten", "Noten (middel hout)", "#7b5131", "Geel en hout"),
    ("mahonie", "Mahonie (donker hout)", "#5a2d1f", "Geel en hout"),
]

# (id, naam, steen, steen-variatie, voeg)
STENEN = [
    ("rood", "Rode baksteen", "#9b4a35", "#87402e", "#d6cfc3"),
    ("bruin", "Bruine baksteen", "#6e4a35", "#5f3f2d", "#bfb5a6"),
    ("geel", "Gele baksteen", "#d4b277", "#c4a066", "#efe7d6"),
    ("wit", "Witte gevel (geschilderd of gekeimd)", "#ece8de", "#e2ddd1", "#d3cdc0"),
    ("antraciet", "Antraciet steen", "#4a4a4c", "#3e3e40", "#6b6b6b"),
]

ONDERDELEN = [
    # (sleutel, label, uitleg)
    ("kozijn", "Kozijnen", "Het vaste houtwerk rond ramen en deuren."),
    ("raam", "Draaiende delen", "De ramen die open kunnen."),
    ("deur", "Voordeur", "Ook de garagedeur, als die er is."),
    ("boei", "Boeidelen", "De planken langs de dakrand en de dakkapel."),
    ("gevel", "Gevelsteen", "Kleur van de muur. Meestal blijft die zoals hij is."),
]

TYPES = [
    ("rij", "Rijtjeshuis"),
    ("twee", "Twee-onder-een-kap"),
    ("dertig", "Jaren-30-woning"),
]
TYPE_KORT = {"rij": "Rijtjeshuis", "twee": "2-onder-1-kap", "dertig": "Jaren 30"}

STIJLEN = [
    # (id, naam, kozijn, raam, deur, boei, gevel)
    ("klassiek-gooi", "Klassiek Gooi", "cremewit", "gooiers-groen", "gooiers-groen", "cremewit", "rood"),
    ("modern-antraciet", "Modern antraciet", "antraciet", "antraciet", "zwart", "antraciet", "wit"),
    ("jaren-30", "Jaren 30", "cremewit", "ossenbloed", "monumentengroen", "cremewit", "bruin"),
    ("warm-landelijk", "Warm landelijk", "gebroken-wit", "olijfgroen", "zweeds-rood", "gebroken-wit", "geel"),
    ("natuurlijk-hout", "Natuurlijk hout", "eiken", "eiken", "noten", "antraciet", "antraciet"),
    ("rustig-blauw", "Rustig blauw", "gebroken-wit", "staalblauw", "nachtblauw", "gebroken-wit", "rood"),
]

# Kozijnen-, buiten- en dakkapelpagina's waar de kiezer goed bij past.
KOSTEN_MET_KLEUR = ("kozijnen-schilderen", "huis-schilderen", "dakkapel-schilderen")


# ---------------------------------------------------------------------------
# Tekenhulpjes voor de SVG
# ---------------------------------------------------------------------------

LIJN = 'stroke="rgba(0,0,0,.28)" stroke-width=".8"'


def _r(x, y, w, h, cls="", extra=""):
    c = f' class="{cls}"' if cls else ""
    return f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="{h:g}"{c}{(" " + extra) if extra else ""}/>'


def _glas(x, y, w, h, lood=False):
    out = _r(x, y, w, h, extra='fill="url(#kk-glas)"')
    # schuine weerspiegeling
    out += (f'<polygon points="{x:g},{y + h * .62:g} {x + w * .55:g},{y:g} {x + w * .78:g},{y:g} '
            f'{x:g},{y + h:g}" fill="#fff" opacity=".22"/>')
    if lood:
        out += _r(x, y, w, h, extra='fill="url(#kk-lood)"')
    out += _r(x, y, w, 2.2, extra='fill="#000" opacity=".18"')
    return out


def _vak(x, y, w, h, soort):
    """soort: v = vast glas, d = draaiend deel, l = draaiend deel met glas-in-lood."""
    if soort == "v":
        return _glas(x, y, w, h)
    rand = min(7, w / 6, h / 6)
    return (_r(x, y, w, h, "kr", LIJN)
            + _glas(x + rand, y + rand, w - 2 * rand, h - 2 * rand, lood=(soort == "l")))


def _rij_vakken(x, y, w, h, vakken, f):
    n = len(vakken)
    bw = (w - (n - 1) * f) / n
    return "".join(_vak(x + i * (bw + f), y, bw, h, s) for i, s in enumerate(vakken))


def raam(x, y, w, h, vakken, boven="", bh=0, f=8, dorpel=True):
    """Kozijn met vakken. boven = vakken van het bovenlicht, bh = hoogte daarvan."""
    out = _r(x, y, w, h, "kk", LIJN)
    ix, iy, iw, ih = x + f, y + f, w - 2 * f, h - 2 * f
    if boven:
        out += _rij_vakken(ix, iy, iw, bh, boven, f)
        out += _rij_vakken(ix, iy + bh + f, iw, ih - bh - f, vakken, f)
    else:
        out += _rij_vakken(ix, iy, iw, ih, vakken, f)
    if dorpel:
        out += _r(x - 6, y + h, w + 12, 7, extra='fill="#bdb6ab"')
        out += _r(x - 6, y + h + 5, w + 12, 2, extra='fill="#000" opacity=".15"')
    return out


def deur(x, y, w, h, soort="paneel", bovenlicht=0, f=8, links=False):
    """Voordeur met kozijn. soort: paneel, glas30 of modern."""
    out = _r(x, y, w, h, "kk", LIJN)
    dy = y + f
    if bovenlicht:
        out += _glas(x + f, y + f, w - 2 * f, bovenlicht, lood=(soort == "glas30"))
        dy = y + f + bovenlicht + f
    dx, dw, dh = x + f, w - 2 * f, y + h - dy
    out += _r(dx, dy, dw, dh, "kd", LIJN)
    schaduw = 'fill="#000" opacity=".14"'
    licht = 'fill="#fff" opacity=".10"'
    if soort == "paneel":
        for py, ph in ((dy + 8, dh * .38), (dy + dh * .5, dh * .42)):
            out += _r(dx + 8, py, dw - 16, ph, extra=schaduw)
            out += _r(dx + 10, py + 2, dw - 20, ph - 4, extra=licht)
    elif soort == "glas30":
        out += _r(dx + 8, dy + 8, dw - 16, dh * .36, extra=schaduw)
        out += _glas(dx + 11, dy + 11, dw - 22, dh * .36 - 6, lood=True)
        out += _r(dx + 8, dy + dh * .52, dw - 16, dh * .38, extra=schaduw)
        out += _r(dx + 10, dy + dh * .52 + 2, dw - 20, dh * .38 - 4, extra=licht)
    else:  # modern: smalle glasstrook en lange greep
        out += _glas(dx + dw * .62, dy + 10, dw * .2, dh - 20)
    # brievenbus en kruk
    out += _r(dx + dw * .2, dy + dh * .44, dw * .34, 5, extra='fill="#2b2b2b" opacity=".55"')
    kx = dx + (dw * .14 if links else dw * .84)
    if soort == "modern":
        out += _r(dx + dw * .44, dy + dh * .3, 3.5, dh * .4, extra='fill="#a7adb1"')
    else:
        out += f'<circle cx="{kx:g}" cy="{dy + dh * .52:g}" r="3.2" fill="#c9a646"/>'
    # stoep
    out += _r(x - 8, y + h, w + 16, 6, extra='fill="#b3ada3"')
    return out


def garagedeur(x, y, w, h, f=8):
    out = _r(x, y, w, h, "kk", LIJN)
    out += _r(x + f, y + f, w - 2 * f, h - f, "kd", LIJN)
    yy = y + f + 12
    while yy < y + h - 4:
        out += _r(x + f, yy, w - 2 * f, 1.6, extra='fill="#000" opacity=".16"')
        yy += 14
    return out


def boei(x, y, w, h):
    return (_r(x, y, w, h, "kb", LIJN)
            + _r(x, y + h, w, 7, extra='fill="#000" opacity=".16"'))


# ---------------------------------------------------------------------------
# De drie woningen
# ---------------------------------------------------------------------------

def _rijtjeshuis():
    o = []
    # dak over de hele rij
    o.append('<polygon points="0,172 640,172 640,62 0,62" fill="url(#kk-dak-grijs)"/>')
    o.append(_r(0, 56, 640, 9, extra='fill="#333537"'))
    # gevels: de buren en onze woning
    o.append(_r(0, 172, 640, 228, "ks"))
    # buren: eenvoudige ramen
    for bx in (-110, 560):
        o.append(_r(bx + 18, 200, 150, 88, extra='fill="#f1efe9"'))
        o.append(_r(bx + 26, 208, 134, 72, extra='fill="url(#kk-glas)"'))
        o.append(_r(bx + 18, 282, 150, 96, extra='fill="#f1efe9"'))
        o.append(_r(bx + 26, 290, 134, 80, extra='fill="url(#kk-glas)"'))
    o.append(_r(0, 164, 104, 16, extra='fill="#f1efe9"'))
    o.append(_r(536, 164, 104, 16, extra='fill="#f1efe9"'))
    # dakkapel
    o.append(_r(246, 92, 148, 70, extra='fill="#2f3133"'))
    o.append(_r(246, 96, 10, 64, "kb", LIJN))
    o.append(_r(384, 96, 10, 64, "kb", LIJN))
    o.append(raam(256, 96, 128, 62, "dvd", dorpel=False))
    o.append(_r(240, 156, 160, 8, extra='fill="#6d6f70"'))
    o.append(boei(240, 82, 160, 14))
    # onze boeideel en scheidingen
    o.append(boei(98, 164, 444, 16))
    o.append(_r(100, 180, 3, 220, extra='fill="#000" opacity=".22"'))
    o.append(_r(537, 180, 3, 220, extra='fill="#000" opacity=".22"'))
    # ramen boven
    o.append(raam(128, 204, 176, 86, "dv"))
    o.append(raam(336, 204, 176, 86, "vd"))
    # begane grond
    o.append(deur(128, 282, 68, 118, "paneel", bovenlicht=24))
    o.append(raam(220, 282, 292, 98, "vvv", boven="ddd", bh=24))
    # regenpijp
    o.append(_r(529, 180, 6, 220, extra='fill="#8f9497"'))
    # buren licht vervagen, zodat het midden opvalt
    o.append(_r(0, 50, 100, 350, extra='fill="#fbf8f2" opacity=".55"'))
    o.append(_r(540, 50, 100, 350, extra='fill="#fbf8f2" opacity=".55"'))
    # heg
    o.append('<rect x="214" y="384" width="304" height="18" rx="9" fill="#6f8f4e"/>')
    o.append('<rect x="214" y="384" width="304" height="6" rx="3" fill="#86a463"/>')
    return "".join(o)


def _twee_onder_een_kap():
    o = []
    # garages met plat dak
    for gx in (40, 490):
        o.append(_r(gx, 292, 110, 108, "ks"))
        o.append(garagedeur(gx + 16, 312, 78, 88))
    o.append(boei(34, 278, 118, 14))
    o.append(boei(488, 278, 118, 14))
    # hoofdgebouw
    o.append(_r(150, 206, 340, 194, "ks"))
    o.append('<polygon points="128,208 512,208 432,72 208,72" fill="url(#kk-dak-grijs)"/>')
    o.append(_r(206, 66, 228, 9, extra='fill="#333537"'))
    # schoorsteen
    o.append(_r(380, 40, 26, 50, "ks"))
    o.append(_r(376, 36, 34, 7, extra='fill="#55585b"'))
    o.append(boei(124, 198, 392, 16))
    # linkerhelft en gespiegelde rechterhelft
    o.append(raam(168, 230, 136, 72, "dvd"))
    o.append(raam(336, 230, 136, 72, "dvd"))
    o.append(deur(160, 286, 60, 114, "paneel", bovenlicht=22))
    o.append(deur(420, 286, 60, 114, "paneel", bovenlicht=22, links=True))
    o.append(raam(234, 292, 74, 88, "vd"))
    o.append(raam(332, 292, 74, 88, "dv"))
    # regenpijp op de scheiding
    o.append(_r(317, 214, 6, 186, extra='fill="#8f9497"'))
    # heggen
    o.append('<rect x="20" y="388" width="140" height="14" rx="7" fill="#6f8f4e"/>')
    o.append('<rect x="480" y="388" width="140" height="14" rx="7" fill="#6f8f4e"/>')
    # boom
    o.append(_r(612, 300, 8, 100, extra='fill="#6b5338"'))
    o.append('<circle cx="616" cy="282" r="30" fill="#7c9a58"/><circle cx="600" cy="300" r="20" fill="#6f8f4e"/>')
    return "".join(o)


def _jaren30():
    o = []
    # rechterdeel: lager dak met dakkapel
    o.append(_r(330, 250, 200, 150, "ks"))
    o.append('<polygon points="318,254 554,254 500,82 318,82" fill="url(#kk-dak-rood)"/>')
    o.append(_r(318, 76, 184, 9, extra='fill="#5a2c20"'))
    o.append(_r(468, 50, 26, 70, "ks"))
    o.append(_r(464, 46, 34, 7, extra='fill="#55585b"'))
    o.append(_r(380, 142, 128, 74, extra='fill="#3a2a22"'))
    o.append(_r(380, 154, 8, 60, "kb", LIJN))
    o.append(_r(500, 154, 8, 60, "kb", LIJN))
    o.append(raam(388, 154, 112, 58, "ll", dorpel=False))
    o.append(_r(374, 210, 140, 8, extra='fill="#6d6f70"'))
    o.append(boei(372, 140, 144, 14))
    o.append(boei(326, 244, 226, 16))
    # linkerdeel met puntgevel
    o.append(_r(110, 206, 220, 194, "ks"))
    o.append('<polygon points="106,208 354,208 230,46" class="ks"/>')
    o.append('<polygon points="92,216 230,28 368,216 348,216 230,54 112,216" class="kb" '
             'stroke="rgba(0,0,0,.28)" stroke-width=".8"/>')
    o.append(raam(208, 108, 44, 42, "d", f=6))
    o.append(raam(170, 188, 120, 66, "dd"))
    # erker
    o.append(_r(128, 286, 204, 114, "ks"))
    o.append(_r(128, 286, 8, 114, extra='fill="#000" opacity=".12"'))
    o.append(_r(324, 286, 8, 114, extra='fill="#000" opacity=".12"'))
    o.append(raam(138, 288, 184, 80, "vvv", boven="lll", bh=22))
    o.append(boei(118, 270, 224, 16))
    # voordeur met luifel en raam ernaast
    o.append(deur(352, 284, 60, 116, "glas30", bovenlicht=22))
    o.append(boei(342, 270, 80, 9))
    o.append(raam(434, 286, 80, 84, "vd", boven="l", bh=18))
    # haagje
    o.append('<rect x="120" y="386" width="220" height="16" rx="8" fill="#6f8f4e"/>')
    o.append('<rect x="428" y="388" width="96" height="14" rx="7" fill="#6f8f4e"/>')
    return "".join(o)


def svg_woning():
    """Eén SVG met drie woningtypes; JavaScript toont er één."""
    steen = STENEN[0]
    k = dict((x[0], x[2]) for x in VERFKLEUREN)
    stijl = (f"--c-kozijn:{k['cremewit']};--c-raam:{k['gooiers-groen']};--c-deur:{k['gooiers-groen']};"
             f"--c-boei:{k['cremewit']};--c-steen:{steen[2]};--c-steen2:{steen[3]};--c-voeg:{steen[4]}")
    defs = """<defs>
<style>
.kk{fill:var(--c-kozijn)}.kr{fill:var(--c-raam)}.kd{fill:var(--c-deur)}.kb{fill:var(--c-boei)}.ks{fill:url(#kk-steen)}
.kk-flits-kozijn .kk,.kk-flits-raam .kr,.kk-flits-deur .kd,.kk-flits-boei .kb,.kk-flits-gevel .ks{animation:kkflits .9s ease}
@keyframes kkflits{35%{opacity:.35}}
</style>
<linearGradient id="kk-lucht" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e3eef5"/><stop offset="1" stop-color="#fbf7ef"/></linearGradient>
<linearGradient id="kk-glas" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d5e4ec"/><stop offset="1" stop-color="#8eacbf"/></linearGradient>
<pattern id="kk-steen" width="40" height="14" patternUnits="userSpaceOnUse">
<rect width="40" height="14" fill="var(--c-voeg)"/>
<rect x="1" y="1" width="18" height="5.6" fill="var(--c-steen)"/><rect x="21" y="1" width="18" height="5.6" fill="var(--c-steen2)"/>
<rect x="0" y="8" width="9" height="5.6" fill="var(--c-steen2)"/><rect x="11" y="8" width="18" height="5.6" fill="var(--c-steen)"/><rect x="31" y="8" width="9" height="5.6" fill="var(--c-steen)"/>
</pattern>
<pattern id="kk-dak-grijs" width="18" height="11" patternUnits="userSpaceOnUse">
<rect width="18" height="11" fill="#4a4c4f"/><rect y="8.5" width="18" height="2.5" fill="#35373a"/><rect x="8.5" width="1.2" height="9" fill="#3c3e41"/>
</pattern>
<pattern id="kk-dak-rood" width="18" height="11" patternUnits="userSpaceOnUse">
<rect width="18" height="11" fill="#8a4532"/><rect y="8.5" width="18" height="2.5" fill="#6c3326"/><rect x="8.5" width="1.2" height="9" fill="#743a2b"/>
</pattern>
<pattern id="kk-lood" width="12" height="12" patternUnits="userSpaceOnUse">
<path d="M0 6L6 0L12 6L6 12Z" fill="none" stroke="#3b3b3b" stroke-width=".9" opacity=".7"/>
</pattern>
</defs>"""
    achtergrond = (_r(0, 0, 640, 440, extra='fill="url(#kk-lucht)"')
                   + _r(0, 400, 640, 40, extra='fill="#cfc9be"')
                   + _r(0, 400, 640, 3, extra='fill="#b3ada3"'))
    groepen = "".join(
        f'<g data-type="{t}"{"" if t == "rij" else " display=none"}>{fn()}</g>'
        for t, fn in (("rij", _rijtjeshuis), ("twee", _twee_onder_een_kap), ("dertig", _jaren30)))
    return (f'<svg id="kk-svg" class="kk-svg" viewBox="0 0 640 440" xmlns="http://www.w3.org/2000/svg" '
            f'role="img" aria-label="Getekende woning in de gekozen kleuren" style="{stijl}">'
            f'{defs}{achtergrond}{groepen}</svg>').replace(" display=none", ' display="none"')


# ---------------------------------------------------------------------------
# Losse blokjes voor andere pagina's
# ---------------------------------------------------------------------------

def kleuren_teaser(kop="Twijfel je over de kleur?"):
    """Kort blok met link naar de kleurenkiezer, voor buitenschilderwerk-, kosten- en homepagina."""
    k = dict((x[0], x[2]) for x in VERFKLEUREN)
    bolletjes = "".join(
        f'<i style="background:{k[c]}"></i>'
        for c in ("cremewit", "gooiers-groen", "antraciet", "bentheimer", "ossenbloed", "eiken"))
    return (TEASER_CSS + f'<div class="kk-teaser"><div class="kk-teaser-bol" aria-hidden="true">{bolletjes}</div>'
            f'<div><h3>{kop}</h3><p>Probeer kozijnen, ramen, voordeur en boeidelen in twintig gangbare kleuren '
            f'op een getekende woning. Je ontwerp deel je met één link.</p>'
            f'<a class="btn btn-ghost" href="{PAD}">Open de kleurenkiezer</a></div></div>')


def kleuren_home_sectie():
    return f'<section class="section"><div class="wrap narrow">{kleuren_teaser("Welke kleur krijgen jouw kozijnen?")}</div></section>'


# ---------------------------------------------------------------------------
# De pagina
# ---------------------------------------------------------------------------

def _monument_plaatsen():
    out = []
    for p in PLAATSEN:
        w = WONINGEN.get(p["slug"], ("", "", ""))
        tekst = (p.get("hook", "") + " " + w[0] + " " + w[1]).lower()
        if "monument" in tekst or "stadsgezicht" in tekst or "vesting" in tekst:
            out.append(p)
    return out


def _panel_html():
    typeknoppen = "".join(
        f'<button type="button" class="kk-type{" on" if i == 0 else ""}" data-type="{t}" '
        f'aria-pressed="{"true" if i == 0 else "false"}" aria-label="{n}">'
        f'<span class="kk-lang">{n}</span><span class="kk-kort" aria-hidden="true">{TYPE_KORT[t]}</span></button>'
        for i, (t, n) in enumerate(TYPES))
    onderdelen = "".join(
        f'<button type="button" class="kk-deel{" on" if i == 0 else ""}" data-deel="{s}" '
        f'aria-pressed="{"true" if i == 0 else "false"}"><i class="kk-stip"></i>'
        f'<span><strong>{lab}</strong><small data-naam></small></span></button>'
        for i, (s, lab, _u) in enumerate(ONDERDELEN))
    groepen = []
    for g in dict.fromkeys(x[3] for x in VERFKLEUREN):
        knoppen = "".join(
            f'<button type="button" class="kk-kleur" data-kleur="{i}" style="--kl:{h}" '
            f'aria-label="{n}" title="{n}"><i></i><span>{n}</span></button>'
            for i, n, h, gg in VERFKLEUREN if gg == g)
        groepen.append(f'<div class="kk-groep"><h4>{g}</h4><div class="kk-kleuren">{knoppen}</div></div>')
    stenen = "".join(
        f'<button type="button" class="kk-kleur kk-steen" data-steen="{i}" style="--kl:{s};--kv:{v}" '
        f'aria-label="{n}" title="{n}"><i></i><span>{n}</span></button>'
        for i, n, s, _s2, v in STENEN)
    stijlen = "".join(
        f'<button type="button" class="kk-stijl" data-stijl="{s[0]}">{s[1]}</button>' for s in STIJLEN)
    uitleg = "".join(f'<p class="kk-uitleg" data-uitleg="{s}" hidden>{u}</p>' for s, _l, u in ONDERDELEN)

    return f"""<div class="kk-tool" id="kleurenkiezer">
  <div class="kk-voorbeeld">
    <div class="kk-types" role="group" aria-label="Kies een woningtype">{typeknoppen}</div>
    <div class="kk-plaat">{svg_woning()}</div>
    <p class="kk-hint">Tik op een deel van de woning om het te kiezen. Kleuren op een scherm wijken altijd wat af van echte verf.</p>
  </div>
  <div class="kk-paneel">
    <h2 class="kk-kop">1. Kies een onderdeel</h2>
    <div class="kk-delen" role="group" aria-label="Onderdelen">{onderdelen}</div>
    <h2 class="kk-kop">2. Kies een kleur <span data-actief-label></span></h2>
    {uitleg}
    <div class="kk-palet" data-palet="verf">{"".join(groepen)}</div>
    <div class="kk-palet" data-palet="steen" hidden><div class="kk-kleuren kk-stenen">{stenen}</div></div>
    <h2 class="kk-kop">Of begin met een stijl</h2>
    <div class="kk-stijlen">{stijlen}<button type="button" class="kk-stijl kk-gok" data-gok>Verras me</button></div>
    <p class="kk-uitleg" style="margin:10px 0 0">Meer ideeën, met uitleg per woningtype? Bekijk de <a href="/inspiratie/">inspiratie en stijlgids</a>.</p>
    <div class="kk-acties">
      <a class="btn btn-primary" href="#offerte" data-offerte>Offerte voor deze kleuren</a>
      <button type="button" class="btn btn-ghost" data-deel-link>Deel je ontwerp</button>
      <button type="button" class="btn btn-ghost" data-download>Bewaar als plaatje</button>
    </div>
    <p class="kk-melding" role="status" aria-live="polite"></p>
  </div>
</div>"""


def build_kleurenkiezer(write, out_dir):
    cr, cr_ld = crumbs([("Home", "/"), ("Buitenschilderwerk", "/schilderwerk/buitenschilderwerk/"),
                        ("Kleurenkiezer", None)])

    monumenten = _monument_plaatsen()
    mon_links = ", ".join(f'<a href="/schilder/{p["slug"]}/">{p["naam"]}</a>' for p in monumenten)

    faqs = [
        ("Welke kozijnkleur past bij een rode bakstenen gevel?",
         "Crèmewit en gebroken wit zijn veilige keuzes en passen bij bijna elke rode steen. Wil je meer karakter, "
         "kies dan donkergroen of ossenbloedrood voor de draaiende delen en de voordeur. Antraciet staat strak "
         "bij rode steen, maar maakt de gevel donkerder."),
        ("Kost een andere kleur meer dan dezelfde kleur opnieuw?",
         "Meestal wel. Ga je van licht naar donker of andersom, dan dekt één laag vaak niet. De schilder zet "
         "dan een extra laag, soms ook een grondlaag in een tussenkleur. Dat kost meer verf en meer uren. "
         "Vraag in de offerte of die extra laag erin zit."),
        ("Mag ik zelf de kleur van mijn kozijnen kiezen?",
         "Bij een gewoon koophuis meestal wel. Woon je in een monument of in een beschermd stadsgezicht, vraag "
         "het dan eerst na bij je gemeente: soms heb je een vergunning nodig of gelden er vaste kleuren. "
         "Bij een huurhuis of een VvE vraag je de verhuurder of de VvE om toestemming."),
        ("Klopt de kleur op mijn scherm met de echte verf?",
         "Niet precies. Elk scherm toont kleuren anders, en buiten in de zon ziet verf er ook anders uit dan "
         "binnen. Gebruik de kiezer om een richting te vinden. Vraag je schilder daarna om een kleurstaal of "
         "een proefvlak op je eigen kozijn."),
        ("Wat zijn draaiende delen en boeidelen?",
         "Draaiende delen zijn de ramen die open kunnen, binnen het vaste kozijn. Boeidelen zijn de planken langs "
         "de rand van het dak, de dakkapel en een plat dak. Ze zitten hoog en vangen veel weer, dus ze hebben "
         "vaak als eerste verf nodig."),
    ]
    faq_html, faq_ld = faq_blok(faqs, "Vragen over kleur kiezen")

    app_ld = {
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": "Kleurenkiezer voor gevel en kozijnen",
        "url": "https://topschilder.nl" + PAD,
        "applicationCategory": "DesignApplication",
        "operatingSystem": "Alle browsers",
        "inLanguage": "nl-NL",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"},
    }

    body = f"""{cr}
<section class="section-sm kk-intro tool-hero"><div class="wrap">
  <span class="badge">Gratis tool</span>
  <h1>Kleurenkiezer voor gevel en kozijnen</h1>
  <p class="lead">Hoe staan groene ramen bij jouw rode steen? Of antraciet kozijnen bij een witte gevel? Kies een woning, klik door de kleuren en deel je ontwerp met wie je wilt.</p>
</div></section>
<section class="kk-sectie"><div class="wrap">{_panel_html()}</div></section>

<section class="section"><div class="wrap">
  <div class="grid g2 kk-info">
    <div>
      <h2>Goed om te weten bij jouw keuze</h2>
      <ul class="checklist" data-tips></ul>
    </div>
    <div>
      <h2>Een andere kleur kost vaak extra</h2>
      <p>Schilder je in dezelfde kleur, dan is één nieuwe laag vaak genoeg. Ga je van wit naar antraciet, of van donkergroen naar crème, dan dekt één laag meestal niet. De schilder zet dan een extra laag, en soms eerst een grondlaag in een tussenkleur.</p>
      <p>Dat kost meer verf en meer uren. Hoeveel, hangt af van het aantal kozijnen en de staat van het hout. Kijk bij <a href="/kosten/kozijnen-schilderen/">wat kost kozijnen schilderen</a> voor richtprijzen, en vraag in elke offerte of de extra laag erin zit.</p>
      <div class="callout">
        <p><strong>Monument of beschermd stadsgezicht?</strong> Vraag dan eerst bij je gemeente of je kleur mag. Soms heb je een vergunning nodig of gelden er vaste kleuren. Dat speelt bijvoorbeeld in de oude kernen van {mon_links}. Huur je, of woon je in een VvE? Vraag dan de verhuurder of de VvE.</p>
      </div>
    </div>
  </div>
</div></section>

<section class="section soft" id="offerte-kleuren"><div class="wrap">
  <div class="grid g2" style="gap:48px;align-items:start">
    <div>
      <span class="badge">Van kleur naar offerte</span>
      <h2>Laat je kleuren uitvoeren</h2>
      <p class="lead">Klik op <strong>Offerte voor deze kleuren</strong>. Je kleurkeuze komt dan vanzelf in het formulier, zodat de schilders weten wat je wilt.</p>
      <ul class="checklist">
        <li><strong>Gratis en vrijblijvend.</strong> Je krijgt offertes van maximaal drie schilders uit jouw regio.</li>
        <li><strong>Je kleurlink gaat mee.</strong> De schilder ziet precies welke kleur waar moet.</li>
        <li><strong>Vraag om een kleurstaal.</strong> Een goede schilder laat je de kleur eerst op je eigen kozijn zien.</li>
      </ul>
      <p>Meer weten over het werk zelf? Lees over <a href="/schilderwerk/buitenschilderwerk/">buitenschilderwerk</a>, <a href="/kosten/huis-schilderen/">wat het kost om je huis buiten te laten schilderen</a> en <a href="/gids/wanneer-buiten-schilderen/">wanneer je buiten schildert</a>.</p>
    </div>
    <div>{offerte_form("Offerte voor jouw kleuren", "Gratis · vrijblijvend · maximaal 3 schilders")}</div>
  </div>
</div></section>
{faq_html}"""

    html = page(
        title("Kleurenkiezer voor gevel en kozijnen"),
        "Probeer gratis kleuren voor je kozijnen, ramen, voordeur en boeidelen op een getekende woning. "
        "Deel je ontwerp met een link en vraag offertes aan.",
        PAD, body, [cr_ld, faq_ld, app_ld])
    html = html.replace('<link rel="stylesheet" href="/assets/css/style.css">',
                        '<link rel="stylesheet" href="/assets/css/style.css">'
                        '<link rel="stylesheet" href="/assets/css/kleuren.css">')
    html = html.replace("</body>", '<script src="/assets/js/kleuren.js" defer></script></body>')
    write(PAD, html, prio=0.7)

    _schrijf(os.path.join(out_dir, "assets", "css", "kleuren.css"), KLEUREN_CSS)
    data = {
        "kleuren": [{"id": i, "naam": n, "hex": h} for i, n, h, _g in VERFKLEUREN],
        "stenen": [{"id": i, "naam": n, "steen": s, "steen2": s2, "voeg": v} for i, n, s, s2, v in STENEN],
        "delen": [{"id": s, "label": l} for s, l, _u in ONDERDELEN],
        "types": [{"id": t, "naam": n} for t, n in TYPES],
        "stijlen": [{"id": s[0], "naam": s[1], "kozijn": s[2], "raam": s[3], "deur": s[4], "boei": s[5],
                     "gevel": s[6]} for s in STIJLEN],
    }
    _schrijf(os.path.join(out_dir, "assets", "js", "kleuren.js"),
             "var KK_DATA = " + json.dumps(data, ensure_ascii=False) + ";\n" + KLEUREN_JS)


def _schrijf(pad, inhoud):
    os.makedirs(os.path.dirname(pad), exist_ok=True)
    with open(pad, "w", encoding="utf-8") as f:
        f.write(inhoud)


# ---------------------------------------------------------------------------
# CSS
# ---------------------------------------------------------------------------

KLEUREN_CSS = r'''/* Kleurenkiezer — alleen geladen op /kleuren-kiezen/ (de teaser-stijl staat onderaan en wordt ook elders gebruikt) */
.kk-intro{padding-bottom:12px}
.kk-sectie{padding:8px 0 40px}
.kk-tool{display:grid;grid-template-columns:minmax(0,1.35fr) minmax(0,1fr);gap:28px;align-items:start}
.kk-voorbeeld{position:sticky;top:86px;background:#fff;border:1px solid var(--line);border-radius:var(--radius-lg);padding:14px;box-shadow:var(--shadow)}
.kk-plaat{border-radius:var(--radius);overflow:hidden;background:#f6f1e8}
.kk-svg{display:block;width:100%;height:auto}
.kk-svg .kk,.kk-svg .kr,.kk-svg .kd,.kk-svg .kb,.kk-svg .ks{cursor:pointer}
.kk-svg.kk-klaar .kk,.kk-svg.kk-klaar .kr,.kk-svg.kk-klaar .kd,.kk-svg.kk-klaar .kb{transition:fill .25s}
.kk-types{display:flex;gap:6px;margin-bottom:12px;flex-wrap:wrap}
.kk-type{flex:1 1 0;min-width:0;border:1px solid var(--line);background:var(--bg-soft);border-radius:99px;padding:8px 10px;font:inherit;font-size:.88rem;font-weight:650;color:var(--ink);cursor:pointer;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.kk-type{transition:border-color .15s,background .15s}
.kk-type:hover{border-color:var(--navy-500)}
.kk-type.on{background:var(--accent-soft);border-color:var(--accent);color:var(--ink);box-shadow:0 0 0 3px rgba(244,130,11,.15)}
.kk-kort{display:none}
.kk-hint{font-size:.82rem;color:var(--muted);margin:10px 2px 0}
.kk-paneel{min-width:0;background:#fff;border:1px solid var(--line);border-top:4px solid var(--accent);border-radius:var(--radius-lg);box-shadow:var(--shadow);padding:22px 22px 24px}
@media(max-width:560px){.kk-paneel{padding:18px 16px}}
.kk-kop{font-size:1.08rem;margin:0 0 10px}
.kk-kop span{font-weight:500;color:var(--muted)}
.kk-kop:not(:first-child){margin-top:22px}
.kk-delen{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}
.kk-deel{display:flex;align-items:center;gap:10px;text-align:left;border:1.5px solid var(--line);background:#fff;border-radius:var(--radius);padding:9px 11px;font:inherit;cursor:pointer;min-width:0}
.kk-deel:hover{border-color:var(--navy-500)}
.kk-deel.on{border-color:var(--accent);background:var(--accent-soft);box-shadow:0 0 0 3px rgba(244,130,11,.15)}
.kk-deel span{display:flex;flex-direction:column;min-width:0;line-height:1.25}
.kk-deel strong{font-size:.92rem;color:var(--ink)}
.kk-deel small{font-size:.78rem;color:var(--muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.kk-stip{flex:0 0 26px;height:26px;border-radius:50%;background:var(--kl,#ccc);box-shadow:inset 0 0 0 1px rgba(0,0,0,.18)}
.kk-uitleg{font-size:.88rem;color:var(--muted);margin:-4px 0 10px}
.kk-groep h4{font-size:.78rem;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);margin:10px 0 6px;font-weight:700}
.kk-kleuren{display:grid;grid-template-columns:repeat(auto-fill,minmax(44px,1fr));gap:8px}
.kk-kleur{position:relative;border:0;background:none;padding:0;cursor:pointer;aspect-ratio:1;border-radius:50%}
.kk-kleur i{display:block;width:100%;height:100%;border-radius:50%;background:var(--kl);box-shadow:inset 0 0 0 1px rgba(0,0,0,.2);transition:transform .12s}
.kk-kleur:hover i{transform:scale(1.08)}
.kk-kleur span{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
.kk-kleur.on i{box-shadow:inset 0 0 0 1px rgba(0,0,0,.2),0 0 0 3px #fff,0 0 0 5px var(--accent)}
.kk-kleur:focus-visible{outline:3px solid var(--accent);outline-offset:3px}
.kk-steen i{background:repeating-linear-gradient(0deg,var(--kv) 0 2px,var(--kl) 2px 10px)}
.kk-stenen{grid-template-columns:repeat(auto-fill,minmax(52px,1fr))}
.kk-stijlen{display:flex;flex-wrap:wrap;gap:8px}
.kk-stijl{border:1px solid var(--line);background:#fff;border-radius:99px;padding:7px 14px;font:inherit;font-size:.88rem;font-weight:600;color:var(--ink);cursor:pointer}
.kk-stijl:hover{border-color:var(--navy-500)}
.kk-stijl{transition:border-color .15s,background .15s}
.kk-stijl.on{border-color:var(--accent);background:var(--accent-soft)}
.kk-gok{border-style:dashed}
.kk-acties{display:flex;flex-wrap:wrap;gap:10px;margin-top:24px}
.kk-acties .btn{flex:1 1 auto}
.kk-melding{min-height:1.4em;font-size:.88rem;color:var(--green);font-weight:600;margin:10px 0 0}
.kk-info h2{font-size:1.35rem}
@media(max-width:900px){
  .kk-tool{grid-template-columns:minmax(0,1fr);gap:18px}
  .kk-voorbeeld{top:70px;z-index:5;padding:8px}
  .kk-hint{display:none}
  .kk-types{margin-bottom:8px}
  .kk-types{gap:4px}.kk-type{padding:6px 4px;font-size:.8rem;letter-spacing:-.01em}
  .kk-lang{display:none}.kk-kort{display:inline}
  .sticky-cta{display:none}body{padding-bottom:0}
}
@media(max-width:900px) and (max-height:760px){.kk-plaat{max-height:34vh}.kk-svg{max-height:34vh;margin:0 auto;width:auto;max-width:100%}}
@media(max-width:420px){.kk-kleuren{grid-template-columns:repeat(6,minmax(0,1fr))}.kk-stenen{grid-template-columns:repeat(5,minmax(0,1fr))}.kk-acties .btn{flex-basis:100%}}
'''

# De teaser staat op pagina's zonder kleuren.css; die stijl gaat via een <style>-blok mee.
TEASER_CSS = ('<style>.kk-teaser{display:flex;gap:20px;align-items:center;background:linear-gradient(120deg,#fff4e6,#fff);'
              'border:1.5px solid #f6d9b2;border-radius:var(--radius-lg);padding:22px;margin:28px 0}'
              '.kk-teaser h3{margin-bottom:.3em}.kk-teaser p{font-size:.95rem;margin-bottom:.8em}'
              '.kk-teaser-bol{flex:0 0 92px;display:grid;grid-template-columns:repeat(3,1fr);gap:6px}'
              '.kk-teaser-bol i{display:block;aspect-ratio:1;border-radius:50%;box-shadow:inset 0 0 0 1px rgba(0,0,0,.18)}'
              '@media(max-width:560px){.kk-teaser{flex-direction:column;align-items:flex-start}.kk-teaser-bol{flex-basis:auto;width:110px}}</style>')

# ---------------------------------------------------------------------------
# JavaScript
# ---------------------------------------------------------------------------

KLEUREN_JS = r'''/* Kleurenkiezer — staat in de URL-hash, zodat elk ontwerp een eigen link heeft. */
(function () {
  "use strict";
  var D = KK_DATA;
  var svg = document.getElementById("kk-svg");
  if (!svg) return;

  var kleurById = {}, steenById = {};
  D.kleuren.forEach(function (k) { kleurById[k.id] = k; });
  D.stenen.forEach(function (s) { steenById[s.id] = s; });
  var typeNaam = {};
  D.types.forEach(function (t) { typeNaam[t.id] = t.naam; });
  var deelLabel = {};
  D.delen.forEach(function (d) { deelLabel[d.id] = d.label; });

  var standaard = { type: "rij", kozijn: "cremewit", raam: "gooiers-groen", deur: "gooiers-groen", boei: "cremewit", gevel: "rood" };
  var staat = lees() || Object.assign({}, standaard);
  var actief = "kozijn";
  var melding = document.querySelector(".kk-melding");

  /* ---------------------------------------------------------- hash lezen */
  function lees() {
    if (!location.hash || location.hash.length < 3) return null;
    var q = new URLSearchParams(location.hash.slice(1));
    if (!q.get("kozijn") && !q.get("type")) return null;
    var s = Object.assign({}, standaard);
    if (typeNaam[q.get("type")]) s.type = q.get("type");
    ["kozijn", "raam", "deur", "boei"].forEach(function (d) { if (kleurById[q.get(d)]) s[d] = q.get(d); });
    if (steenById[q.get("gevel")]) s.gevel = q.get("gevel");
    return s;
  }

  function hash() {
    return "type=" + staat.type + "&kozijn=" + staat.kozijn + "&raam=" + staat.raam +
      "&deur=" + staat.deur + "&boei=" + staat.boei + "&gevel=" + staat.gevel;
  }

  function link() { return location.origin + location.pathname + "#" + hash(); }

  /* ------------------------------------------------------------ tekenen */
  function teken() {
    var st = svg.style;
    st.setProperty("--c-kozijn", kleurById[staat.kozijn].hex);
    st.setProperty("--c-raam", kleurById[staat.raam].hex);
    st.setProperty("--c-deur", kleurById[staat.deur].hex);
    st.setProperty("--c-boei", kleurById[staat.boei].hex);
    var g = steenById[staat.gevel];
    st.setProperty("--c-steen", g.steen);
    st.setProperty("--c-steen2", g.steen2);
    st.setProperty("--c-voeg", g.voeg);

    svg.querySelectorAll("g[data-type]").forEach(function (el) {
      if (el.getAttribute("data-type") === staat.type) el.removeAttribute("display");
      else el.setAttribute("display", "none");
    });
    svg.setAttribute("aria-label", omschrijving());

    document.querySelectorAll(".kk-type").forEach(function (b) {
      var on = b.dataset.type === staat.type;
      b.classList.toggle("on", on); b.setAttribute("aria-pressed", on);
    });
    document.querySelectorAll(".kk-deel").forEach(function (b) {
      var d = b.dataset.deel;
      var on = d === actief;
      b.classList.toggle("on", on); b.setAttribute("aria-pressed", on);
      var hex = d === "gevel" ? steenById[staat.gevel].steen : kleurById[staat[d]].hex;
      b.querySelector(".kk-stip").style.setProperty("--kl", hex);
      b.querySelector("[data-naam]").textContent = naamVan(d);
    });
    document.querySelectorAll("[data-uitleg]").forEach(function (p) { p.hidden = p.dataset.uitleg !== actief; });
    var lab = document.querySelector("[data-actief-label]");
    if (lab) lab.textContent = "voor " + deelLabel[actief].toLowerCase();
    var steenModus = actief === "gevel";
    document.querySelector('[data-palet="verf"]').hidden = steenModus;
    document.querySelector('[data-palet="steen"]').hidden = !steenModus;
    document.querySelectorAll(".kk-kleur[data-kleur]").forEach(function (b) {
      var on = !steenModus && b.dataset.kleur === staat[actief];
      b.classList.toggle("on", on); b.setAttribute("aria-pressed", on);
    });
    document.querySelectorAll(".kk-kleur[data-steen]").forEach(function (b) {
      var on = b.dataset.steen === staat.gevel;
      b.classList.toggle("on", on); b.setAttribute("aria-pressed", on);
    });
    document.querySelectorAll(".kk-stijl[data-stijl]").forEach(function (b) {
      var s = D.stijlen.filter(function (x) { return x.id === b.dataset.stijl; })[0];
      b.classList.toggle("on", !!s && ["kozijn", "raam", "deur", "boei", "gevel"].every(function (d) { return s[d] === staat[d]; }));
    });
    tips();
    if (history.replaceState) history.replaceState(null, "", "#" + hash());
  }

  function naamVan(d) {
    var n = d === "gevel" ? steenById[staat.gevel].naam : kleurById[staat[d]].naam;
    return n.replace(/ \(.*\)$/, "");
  }

  function omschrijving() {
    return typeNaam[staat.type] + " met kozijnen in " + naamVan("kozijn").toLowerCase() +
      ", draaiende delen in " + naamVan("raam").toLowerCase() +
      ", voordeur in " + naamVan("deur").toLowerCase() +
      ", boeidelen in " + naamVan("boei").toLowerCase() +
      " en gevel: " + naamVan("gevel").toLowerCase();
  }

  function flits(d) {
    var cls = "kk-flits-" + d;
    svg.classList.remove(cls);
    void svg.getBoundingClientRect();
    svg.classList.add(cls);
    setTimeout(function () { svg.classList.remove(cls); }, 950);
  }

  function zeg(t) {
    if (!melding) return;
    melding.textContent = t;
    clearTimeout(zeg.t);
    zeg.t = setTimeout(function () { melding.textContent = ""; }, 4000);
  }

  /* --------------------------------------------------------------- tips */
  function helderheid(hex) {
    var n = parseInt(hex.slice(1), 16);
    var c = [(n >> 16) & 255, (n >> 8) & 255, n & 255].map(function (v) {
      v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4);
    });
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2];
  }

  function tips() {
    var ul = document.querySelector("[data-tips]");
    if (!ul) return;
    var t = [];
    var verf = ["kozijn", "raam", "deur", "boei"];
    var donker = verf.filter(function (d) { return helderheid(kleurById[staat[d]].hex) < 0.05; });
    if (donker.length) {
      t.push("<strong>Donkere kleur gekozen.</strong> Donkere verf wordt in de zon veel warmer dan lichte. Vraag je schilder om verf die daarvoor geschikt is, zeker op een zuid- of westgevel.");
    }
    var licht = verf.filter(function (d) { return helderheid(kleurById[staat[d]].hex) > 0.7; });
    if (licht.length) {
      t.push("<strong>Lichte kleur gekozen.</strong> Op wit en crème zie je vuil en groene aanslag sneller. Een keer per jaar afwassen houdt je verf langer mooi.");
    }
    if (staat.kozijn === staat.raam) {
      t.push("<strong>Kozijn en raam in één kleur.</strong> Dat oogt rustig en strak, en het is voor de schilder iets minder werk dan twee kleuren.");
    } else {
      t.push("<strong>Ramen in een andere kleur dan het kozijn.</strong> Een klassieke keuze die de ramen laat opvallen. Twee kleuren betekent wel wat meer afplakken en dus iets meer uren.");
    }
    if (verf.some(function (d) { return ["eiken", "noten", "mahonie"].indexOf(staat[d]) > -1; })) {
      t.push("<strong>Houtkleur gekozen.</strong> Dekkende verf in een houtkleur is iets anders dan transparante beits. Wil je de nerf van het hout blijven zien, vraag dan naar beits.");
    }
    if (staat.gevel === "wit") {
      t.push("<strong>Witte gevel.</strong> Is je gevel nu nog baksteen? Schilderen of keimen is een grote klus die je niet zomaar terugdraait. Laat je daar apart over adviseren.");
    }
    t.push("<strong>Nieuwe kleur, extra laag.</strong> Wissel je van licht naar donker of andersom, dan is er vaak een laag meer nodig. Vraag of die in de offerte zit.");
    ul.innerHTML = t.map(function (x) { return "<li>" + x + "</li>"; }).join("");
  }

  /* ------------------------------------------------------------ klikken */
  function kiesDeel(d) { actief = d; teken(); flits(d); }

  document.querySelectorAll(".kk-type").forEach(function (b) {
    b.addEventListener("click", function () { staat.type = b.dataset.type; teken(); });
  });
  document.querySelectorAll(".kk-deel").forEach(function (b) {
    b.addEventListener("click", function () { kiesDeel(b.dataset.deel); });
  });
  document.querySelectorAll(".kk-kleur[data-kleur]").forEach(function (b) {
    b.addEventListener("click", function () { staat[actief] = b.dataset.kleur; teken(); flits(actief); });
  });
  document.querySelectorAll(".kk-kleur[data-steen]").forEach(function (b) {
    b.addEventListener("click", function () { staat.gevel = b.dataset.steen; teken(); });
  });
  document.querySelectorAll(".kk-stijl[data-stijl]").forEach(function (b) {
    b.addEventListener("click", function () {
      var s = D.stijlen.filter(function (x) { return x.id === b.dataset.stijl; })[0];
      ["kozijn", "raam", "deur", "boei", "gevel"].forEach(function (d) { staat[d] = s[d]; });
      teken();
      zeg("Stijl ‘" + s.naam + "’ toegepast. Pas gerust onderdelen aan.");
    });
  });
  var gok = document.querySelector("[data-gok]");
  if (gok) gok.addEventListener("click", function () {
    // Willekeurig, maar met een paar spelregels zodat het er nog als een huis uitziet.
    var lichte = ["cremewit", "gebroken-wit", "wit", "zandbeige", "lichtgrijs"];
    var accent = D.kleuren.map(function (k) { return k.id; });
    function uit(a) { return a[Math.floor(Math.random() * a.length)]; }
    var basis = Math.random() < 0.7 ? uit(lichte) : uit(["antraciet", "zwart", "eiken", "steengrijs"]);
    staat.kozijn = basis;
    staat.boei = Math.random() < 0.8 ? basis : uit(lichte);
    staat.raam = Math.random() < 0.4 ? basis : uit(accent);
    staat.deur = uit(accent);
    staat.gevel = uit(D.stenen).id;
    teken();
    zeg("Nieuwe combinatie. Bevalt hij niet? Klik nog een keer.");
  });

  // Op de tekening zelf klikken kiest dat onderdeel.
  var klasDeel = { kk: "kozijn", kr: "raam", kd: "deur", kb: "boei", ks: "gevel" };
  svg.addEventListener("click", function (e) {
    var el = e.target;
    var c = el.getAttribute && el.getAttribute("class");
    if (c && klasDeel[c]) {
      kiesDeel(klasDeel[c]);
      var paneel = document.querySelector(".kk-paneel");
      if (window.innerWidth <= 900 && paneel) {
        var kop = paneel.querySelectorAll(".kk-kop")[1];
        if (kop) {
          var top = kop.getBoundingClientRect().top;
          var plaat = document.querySelector(".kk-voorbeeld").getBoundingClientRect().bottom;
          if (top > window.innerHeight || top < plaat) {
            window.scrollTo({ top: window.scrollY + top - plaat - 12, behavior: "smooth" });
          }
        }
      }
    }
  });

  window.addEventListener("hashchange", function () {
    var s = lees();
    if (s && hash() !== location.hash.slice(1)) { staat = s; teken(); }
  });

  /* -------------------------------------------------------------- delen */
  var deelKnop = document.querySelector("[data-deel-link]");
  if (deelKnop) deelKnop.addEventListener("click", function () {
    var url = link();
    var tekst = "Mijn kleuren voor de " + typeNaam[staat.type].toLowerCase() + ": " + omschrijving().replace(/^[^ ]+ met /, "") + ".";
    if (navigator.share && window.matchMedia("(pointer:coarse)").matches) {
      navigator.share({ title: "Mijn kleurontwerp", text: tekst, url: url }).catch(function () {});
      return;
    }
    function gelukt() { zeg("Link gekopieerd. Plak hem in een appje of mail."); }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(url).then(gelukt, function () { window.prompt("Kopieer deze link:", url); });
    } else {
      window.prompt("Kopieer deze link:", url);
    }
  });

  /* ---------------------------------------------------- plaatje bewaren */
  var dlKnop = document.querySelector("[data-download]");
  if (dlKnop) dlKnop.addEventListener("click", function () {
    var kloon = svg.cloneNode(true);
    kloon.querySelectorAll('g[display="none"]').forEach(function (g) { g.parentNode.removeChild(g); });
    kloon.removeAttribute("class");
    kloon.setAttribute("width", "1280");
    kloon.setAttribute("height", "880");
    var bron = new XMLSerializer().serializeToString(kloon);
    var img = new Image();
    img.onload = function () {
      var c = document.createElement("canvas");
      c.width = 1280; c.height = 1080;
      var x = c.getContext("2d");
      x.fillStyle = "#ffffff"; x.fillRect(0, 0, c.width, c.height);
      x.drawImage(img, 0, 0, 1280, 880);
      x.fillStyle = "#241906";
      x.font = "700 34px -apple-system, Segoe UI, Roboto, Arial, sans-serif";
      x.fillText("Mijn kleuren: " + typeNaam[staat.type].toLowerCase(), 48, 940);
      x.font = "400 25px -apple-system, Segoe UI, Roboto, Arial, sans-serif";
      x.fillStyle = "#57492f";
      var regels = [
        "Kozijnen: " + naamVan("kozijn").toLowerCase() + "   ·   Draaiende delen: " + naamVan("raam").toLowerCase() + "   ·   Voordeur: " + naamVan("deur").toLowerCase(),
        "Boeidelen: " + naamVan("boei").toLowerCase() + "   ·   Gevel: " + naamVan("gevel").toLowerCase()
      ];
      x.fillText(regels[0], 48, 990);
      x.fillText(regels[1], 48, 1030);
      x.fillStyle = "#f4820b";
      x.font = "700 24px -apple-system, Segoe UI, Roboto, Arial, sans-serif";
      x.textAlign = "right";
      x.fillText("topschilder.nl/kleuren-kiezen", 1232, 1030);
      c.toBlob(function (blob) {
        if (!blob) { zeg("Bewaren lukte niet in deze browser. Maak anders een schermafbeelding."); return; }
        var a = document.createElement("a");
        a.href = URL.createObjectURL(blob);
        a.download = "mijn-kleuren-topschilder.png";
        document.body.appendChild(a); a.click(); a.remove();
        setTimeout(function () { URL.revokeObjectURL(a.href); }, 2000);
        zeg("Plaatje bewaard in je downloads.");
      }, "image/png");
    };
    img.onerror = function () { zeg("Bewaren lukte niet in deze browser. Maak anders een schermafbeelding."); };
    img.src = "data:image/svg+xml;charset=utf-8," + encodeURIComponent(bron);
  });

  /* ------------------------------------------------- naar het formulier */
  var offKnop = document.querySelector("[data-offerte]");
  if (offKnop) offKnop.addEventListener("click", function (e) {
    var form = document.querySelector("form[data-wizard]");
    if (!form) return;
    e.preventDefault();
    var oms = form.querySelector("textarea[name=omschrijving]");
    if (oms) {
      var regel = "Kleurwens: " + omschrijving().charAt(0).toLowerCase() + omschrijving().slice(1) + ". Ontwerp: " + link();
      var oud = oms.value.replace(/^Kleurwens: .*$/m, "").trim();
      oms.value = regel + (oud ? "\n" + oud : "");
    }
    var dienst = [].slice.call(form.querySelectorAll("input[name=dienst]")).filter(function (i) { return i.value === "Buitenschilderwerk"; })[0];
    if (dienst && !dienst.checked) dienst.click();
    var box = document.getElementById("offerte");
    if (box) window.scrollTo({ top: box.getBoundingClientRect().top + window.scrollY - 90, behavior: "smooth" });
    zeg("Je kleuren staan in het formulier.");
  });

  teken();
  setTimeout(function () { svg.classList.add("kk-klaar"); }, 50);
})();
'''
