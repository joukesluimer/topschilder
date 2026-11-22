# -*- coding: utf-8 -*-
"""
Inspiratie en stijlgids (/inspiratie/).

Kleurcombinaties per woningtype, getekend op dezelfde SVG-woningen als de
kleurenkiezer (kleuren_kiezer.py), plus een binnen-sectie en een stijlgids.
Elke stijl heeft een knop die de kleurenkiezer opent met die kleuren in de
URL-hash.

Alles van deze pagina staat in dit bestand: de stijlen, drie extra getekende
woningen (Gooise villa, monument, nieuwbouw), de pagina, de CSS en de
JavaScript. build.py roept alleen build_inspiratie() aan en zet op een paar
pagina's inspiratie_teaser() neer.

Sinds de inhoudsronde (inspiratie-content) heeft elke kleur een RAL Classic-code
met de officiële naam en een hexwaarde als benadering (zie inspiratie_gids.py), en
heeft elk woningtype een eigen gids op /inspiratie/{type}/ met echte foto's van
Wikimedia Commons (foto_data.FOTOS_INSPIRATIE, ook op /fotoverantwoording/).
"""

import json
import os

from components import page, crumbs, offerte_form, faq_blok, title, foto
from data import PLAATS_BY_SLUG
from foto_data import FOTOS_INSPIRATIE
from inspiratie_gids import KLEURCODES, BRONNEN, GIDSEN, ONDERHOUD_ALGEMEEN, bron, kleur_label
from kleuren_kiezer import (VERFKLEUREN, STENEN, TYPES as KIEZER_TYPES, PAD as KIEZER_PAD,
                            LIJN, _r, _glas, raam, deur, boei, svg_woning,
                            _rijtjeshuis, _twee_onder_een_kap, _jaren30, _monument_plaatsen)

PAD = "/inspiratie/"

# Naam en hex komen van de RAL-code die we per kleur aanhouden (inspiratie_gids.KLEURCODES).
KLEUR = {i: ((KLEURCODES[i][0], KLEURCODES[i][2]) if i in KLEURCODES else (n, h)) for i, n, h, _g in VERFKLEUREN}
STEEN = {i: (n, s, s2, v) for i, n, s, s2, v in STENEN}

ONDERDELEN = (("kozijn", "Kozijnen"), ("raam", "Ramen"), ("deur", "Voordeur"), ("boei", "Boeidelen"))

# (sleutel, naam, korte naam voor de filterknop)
WONINGTYPES = [
    ("jaren30", "Jaren-30-woning", "Jaren 30"),
    ("jaren70", "Jaren-70-rijtjeshuis", "Jaren 70"),
    ("villa", "Gooise villa", "Villa"),
    ("polder", "Polderwoning in Flevoland", "Polder"),
    ("monument", "Monument in een vestingstad", "Monument"),
    ("nieuwbouw", "Moderne nieuwbouw", "Nieuwbouw"),
]
WONINGTYPE_NAAM = {k: n for k, n, _ in WONINGTYPES}

# Welke woning van de kleurenkiezer het dichtst bij elk woningtype ligt.
KIEZER_TYPE = {"jaren30": "dertig", "jaren70": "rij", "villa": "twee",
               "polder": "twee", "monument": "rij", "nieuwbouw": "rij"}

STIJLEN = [
    {"id": "jaren30-klassiek", "type": "jaren30", "naam": "Klassiek jaren 30",
     "kozijn": "cremewit", "raam": "monumentengroen", "deur": "ossenbloed", "boei": "cremewit", "gevel": "bruin",
     "waarom": "Crème kozijnen lijsten de kleine ruiten en het glas-in-lood mooi in. Diepgroen in de ramen en "
               "een rode voordeur passen bij de warme bruine steen en de rode pannen. Zo blijft het rijke "
               "karakter van de woning zichtbaar.",
     "tip": "Heb je glas-in-lood? Laat de schilder dat goed afplakken en niet meeschilderen."},
    {"id": "jaren30-licht", "type": "jaren30", "naam": "Rustig en licht",
     "kozijn": "gebroken-wit", "raam": "gebroken-wit", "deur": "nachtblauw", "boei": "gebroken-wit", "gevel": "rood",
     "waarom": "Alles in één lichte tint maakt de gevel rustig. Het metselwerk en de erker krijgen dan de "
               "aandacht. Eén donkerblauwe voordeur geeft houvast.",
     "tip": "Met veel kleine ruiten zie je vuil op lichte verf snel. Een keer per jaar afwassen helpt."},
    {"id": "jaren70-strak", "type": "jaren70", "naam": "Strak opgefrist",
     "kozijn": "antraciet", "raam": "antraciet", "deur": "bentheimer", "boei": "antraciet", "gevel": "bruin",
     "waarom": "Woningen uit de jaren 70 hebben vaak brede kozijnen en een donkere steen. In antraciet ogen "
               "die kozijnen slanker en rustiger. Een warmgele voordeur zorgt dat het huis niet somber wordt.",
     "tip": "Donkere verf wordt in de zon heet. Vraag om verf die daarvoor geschikt is, zeker op het zuiden."},
    {"id": "jaren70-vriendelijk", "type": "jaren70", "naam": "Licht en vriendelijk",
     "kozijn": "cremewit", "raam": "salie", "deur": "olijfgroen", "boei": "cremewit", "gevel": "geel",
     "waarom": "Bij gele steen werken crème kozijnen en zachtgroene ramen vriendelijk en licht. De olijfgroene "
               "deur maakt het af. Een goede keuze als je huis wat warmer mag ogen.",
     "tip": "Woon je in een rij? Kijk ook naar de buren. Een rij in dezelfde kleuren oogt rustig."},
    {"id": "villa-klassiek", "type": "villa", "naam": "Gooise klassieker",
     "kozijn": "cremewit", "raam": "gooiers-groen", "deur": "gooiers-groen", "boei": "cremewit", "gevel": "rood",
     "waarom": "Groen met crème is in Nederland al heel lang een gewone combinatie. Het donkergroen van ramen, "
               "deur en luiken staat rustig bij het riet en de tuin. Het crème houdt het geheel licht.",
     "tip": "Luiken krijgen in deze tekening de kleur van de voordeur. Zo blijft het bij twee kleuren."},
    {"id": "villa-landhuis", "type": "villa", "naam": "Landhuis in wit en zwart",
     "kozijn": "wit", "raam": "wit", "deur": "zwart", "boei": "wit", "gevel": "wit",
     "waarom": "Een witte gevel met zwarte luiken en voordeur geeft een frisse landhuisstijl. Het contrast is "
               "groot. Dat werkt het best bij een duidelijke, symmetrische voorgevel.",
     "tip": "Is je gevel nu baksteen? Schilderen of keimen draai je niet zomaar terug. Laat je daar apart over adviseren."},
    {"id": "polder-zacht", "type": "polder", "naam": "Zacht polderpalet",
     "kozijn": "gebroken-wit", "raam": "salie", "deur": "olijfgroen", "boei": "gebroken-wit", "gevel": "rood",
     "waarom": "Zachte groentinten passen bij het open, groene land rond de woning. Gebroken wit is minder fel "
               "dan zuiver wit en oogt daardoor rustiger in het volle licht.",
     "tip": "In de open polder staat houtwerk vol in zon en wind. Lichte kleuren worden minder heet."},
    {"id": "polder-blauw", "type": "polder", "naam": "Fris grijsblauw",
     "kozijn": "lichtgrijs", "raam": "staalblauw", "deur": "nachtblauw", "boei": "lichtgrijs", "gevel": "geel",
     "waarom": "Grijsblauw bij gele steen geeft een frisse uitstraling die past bij de ruime lucht boven het "
               "vlakke land. Lichtgrijs is een rustig alternatief voor wit.",
     "tip": "Twee-onder-een-kap? Het oogt het mooist als beide helften bij elkaar passen. Overleg met je buren."},
    {"id": "monument-ingetogen", "type": "monument", "naam": "Historisch en ingetogen",
     "kozijn": "cremewit", "raam": "cremewit", "deur": "monumentengroen", "boei": "cremewit", "gevel": "rood",
     "waarom": "Rustige, gebroken tinten op kozijnen en ramen en één donkere voordeur. Dat laat de verhoudingen "
               "van een oude gevel spreken: de hoge ramen, de roeden en de kroonlijst.",
     "tip": "Bij een monument vraag je de gemeente vooraf welke kleur mag. Soms heb je een vergunning nodig."},
    {"id": "monument-rood", "type": "monument", "naam": "Diep rood accent",
     "kozijn": "cremewit", "raam": "ossenbloed", "deur": "ossenbloed", "boei": "cremewit", "gevel": "bruin",
     "waarom": "Een diep wijnrood, dicht bij wat vaak ossenbloedrood heet, in de ramen en de deur geeft een "
               "historische gevel kleur, zonder dat het schreeuwt. Het past goed bij donkere baksteen.",
     "tip": "Ook in een beschermd stadsgezicht kan een kleurwissel vergunningplichtig zijn. Vraag het na."},
    {"id": "nieuwbouw-antraciet", "type": "nieuwbouw", "naam": "Modern antraciet",
     "kozijn": "antraciet", "raam": "antraciet", "deur": "eiken", "boei": "zwart", "gevel": "wit",
     "waarom": "Antraciet kozijnen op een lichte gevel geven strakke lijnen, die passen bij grote glasvlakken. "
               "Een deur in houtkleur voegt wat warmte toe.",
     "tip": "Veel nieuwbouw heeft kunststof of aluminium kozijnen. Die kun je laten schilderen, maar dat vraagt "
            "een eigen voorbehandeling. Vraag ernaar in de offerte."},
    {"id": "nieuwbouw-hout", "type": "nieuwbouw", "naam": "Warm natuurlijk",
     "kozijn": "eiken", "raam": "eiken", "deur": "noten", "boei": "antraciet", "gevel": "antraciet",
     "waarom": "Houtkleuren tegen een donkere steen ogen warm en eigentijds. De antraciet boeidelen sluiten aan "
               "bij de steen, zodat het hout de aandacht krijgt.",
     "tip": "Wil je de nerf van het hout blijven zien? Vraag dan naar transparante beits in plaats van dekkende verf."},
]


# ---------------------------------------------------------------------------
# Drie extra woningen, met de tekenhulpjes van de kleurenkiezer
# ---------------------------------------------------------------------------

def _luik(x, y, w, h):
    """Houten luik in de kleur van de voordeur, met lamellen."""
    out = _r(x, y, w, h, "kd", LIJN)
    yy = y + 8
    while yy < y + h - 6:
        out += _r(x + 4, yy, w - 8, 2, extra='fill="#000" opacity=".16"')
        yy += 9
    return out


def _schuifraam(x, y, w, h, f=6):
    """Hoog schuifraam met roeden: twee delen boven elkaar, elk met zes ruitjes."""
    out = _r(x, y, w, h, "kk", LIJN)
    ix, iw = x + f, w - 2 * f
    vh = (h - 2 * f - 3) / 2
    for vy in (y + f, y + f + vh + 3):
        out += _r(ix, vy, iw, vh, "kr", LIJN)
        out += _glas(ix + 4, vy + 4, iw - 8, vh - 8)
        # roeden: twee staand, één liggend
        for i in (1, 2):
            out += _r(ix + 4 + (iw - 8) * i / 3 - 1, vy + 4, 2.2, vh - 8, "kr")
        out += _r(ix + 4, vy + vh / 2 - 1, iw - 8, 2.2, "kr")
    out += _r(x - 5, y + h, w + 10, 6, extra='fill="#d9d3c8"')
    return out


def _villa():
    o = []
    # tuin en hoofdgebouw
    o.append(_r(110, 236, 420, 164, "ks"))
    # rieten dak, met een zachte rand
    o.append('<path d="M74 252 L188 64 Q320 40 452 64 L566 252 Q320 266 74 252Z" fill="url(#kk-riet)"/>')
    o.append('<path d="M74 252 Q320 266 566 252 L566 258 Q320 274 74 258Z" fill="#000" opacity=".18"/>')
    # schoorsteen
    o.append(_r(414, 44, 30, 54, "ks"))
    o.append(_r(410, 40, 38, 7, extra='fill="#55585b"'))
    # dakkapel in het riet
    o.append(_r(268, 132, 104, 70, extra='fill="#4a3b26"'))
    o.append(raam(276, 140, 88, 58, "dd", dorpel=False))
    o.append('<path d="M250 140 Q320 92 390 140 L384 146 Q320 104 256 146Z" fill="url(#kk-riet)"/>')
    o.append(boei(262, 198, 116, 9))
    # ramen met luiken
    for wx in (150, 394):
        o.append(_luik(wx - 30, 270, 26, 100))
        o.append(_luik(wx + 100, 270, 26, 100))
        o.append(raam(wx, 270, 96, 100, "dd", boven="ll", bh=22))
    # voordeur met luifel
    o.append(boei(282, 274, 76, 10))
    o.append(_r(282, 284, 76, 4, extra='fill="#000" opacity=".15"'))
    o.append(deur(290, 290, 60, 110, "paneel", bovenlicht=20))
    # tuin
    o.append('<rect x="96" y="384" width="180" height="18" rx="9" fill="#6f8f4e"/>')
    o.append('<rect x="364" y="384" width="180" height="18" rx="9" fill="#6f8f4e"/>')
    o.append(_r(40, 300, 9, 100, extra='fill="#6b5338"'))
    o.append('<circle cx="44" cy="280" r="34" fill="#7c9a58"/><circle cx="26" cy="300" r="22" fill="#6f8f4e"/>')
    o.append(_r(594, 316, 8, 84, extra='fill="#6b5338"'))
    o.append('<circle cx="598" cy="298" r="28" fill="#6f8f4e"/>')
    return "".join(o)


def _monument():
    o = []
    # buren: links gepleisterd, rechts lichtere steen; vaag, zodat het midden opvalt
    o.append(_r(0, 120, 196, 280, extra='fill="#e6dccb"'))
    o.append(_r(444, 70, 196, 330, extra='fill="#c9b79b"'))
    for bx, top in ((24, 150), (110, 150), (468, 110), (560, 110)):
        for vy in (top, top + 110):
            o.append(_r(bx, vy, 56, 84, extra='fill="#f1efe9"'))
            o.append(_r(bx + 6, vy + 6, 44, 72, extra='fill="url(#kk-glas)"'))
    o.append(_r(0, 108, 196, 14, extra='fill="#f1efe9"'))
    o.append(_r(444, 58, 196, 14, extra='fill="#f1efe9"'))
    # dak achter de kroonlijst
    o.append('<polygon points="206,64 434,64 400,26 240,26" fill="url(#kk-dak-grijs)"/>')
    # gevel
    o.append(_r(200, 90, 240, 310, "ks"))
    # kroonlijst met klossen
    o.append(_r(190, 62, 260, 26, "kb", LIJN))
    o.append(_r(186, 58, 268, 7, "kb", LIJN))
    for kx in range(200, 444, 20):
        o.append(_r(kx, 88, 8, 8, "kb", LIJN))
    o.append(_r(190, 96, 260, 3, extra='fill="#000" opacity=".14"'))
    # bovenverdiepingen: drie hoge schuiframen
    for wx in (220, 294, 368):
        o.append(_schuifraam(wx, 118, 52, 92))
        o.append(_schuifraam(wx, 230, 52, 98))
    # strek boven de ramen
    for wx in (220, 294, 368):
        o.append(_r(wx - 4, 110, 60, 6, extra='fill="#000" opacity=".14"'))
    # begane grond: deur met bovenlicht en twee ramen
    o.append(_r(200, 296, 240, 4, extra='fill="#000" opacity=".12"'))
    o.append(deur(288, 300, 64, 100, "paneel", bovenlicht=26))
    o.append(_schuifraam(218, 314, 54, 74))
    o.append(_schuifraam(368, 314, 54, 74))
    o.append(_r(0, 50, 196, 350, extra='fill="#fbf8f2" opacity=".5"'))
    o.append(_r(444, 50, 196, 350, extra='fill="#fbf8f2" opacity=".5"'))
    return "".join(o)


def _nieuwbouw():
    o = []
    # hoofdvolume met steil zadeldak zonder overstek
    o.append(_r(120, 204, 260, 196, "ks"))
    o.append('<polygon points="114,208 386,208 250,64" fill="url(#kk-dak-grijs)"/>')
    o.append('<polygon points="106,212 250,56 394,212 382,212 250,72 118,212" class="kb" '
             'stroke="rgba(0,0,0,.28)" stroke-width=".8"/>')
    # glas in de kop van het dak
    o.append(raam(216, 128, 68, 72, "vd", f=5, dorpel=False))
    # grote glaspui en raam boven
    o.append(raam(144, 220, 212, 40, "vvd", f=6, dorpel=False))
    o.append(raam(144, 276, 168, 124, "vvd", f=7, dorpel=False))
    # zijvolume met plat dak
    o.append(_r(380, 268, 190, 132, "ks"))
    o.append(boei(374, 256, 202, 14))
    o.append(deur(400, 296, 58, 104, "modern"))
    o.append(raam(476, 296, 76, 56, "v", f=6, dorpel=False))
    # strak tuintje
    o.append(_r(320, 380, 50, 20, extra='fill="#9aa58a"'))
    o.append('<rect x="472" y="384" width="98" height="16" rx="3" fill="#6f8f4e"/>')
    o.append(_r(60, 316, 6, 84, extra='fill="#6b5338"'))
    o.append('<circle cx="63" cy="300" r="26" fill="#7c9a58"/>')
    return "".join(o)


HUIZEN = {
    "jaren30": _jaren30, "jaren70": _rijtjeshuis, "villa": _villa,
    "polder": _twee_onder_een_kap, "monument": _monument, "nieuwbouw": _nieuwbouw,
}
HUIS_OMSCHRIJVING = {
    "jaren30": "jaren-30-woning met erker en puntgevel",
    "jaren70": "rijtjeshuis met dakkapel",
    "villa": "vrijstaande villa met rieten dak en luiken",
    "polder": "twee-onder-een-kap met garages",
    "monument": "smal historisch pand met kroonlijst en hoge schuiframen",
    "nieuwbouw": "moderne woning met steil dak en veel glas",
}

_IDS = ("kk-lucht", "kk-glas", "kk-steen", "kk-dak-grijs", "kk-dak-rood", "kk-lood", "kk-riet")
_RIET = ('<pattern id="kk-riet" width="16" height="10" patternUnits="userSpaceOnUse">'
         '<rect width="16" height="10" fill="#8a7550"/><path d="M0 9L4 1M5 10L9 2M10 9L14 1" '
         'stroke="#6f5d3d" stroke-width="1.3"/><path d="M2 10L6 2M12 10L16 2" stroke="#a08a62" stroke-width=".9"/>'
         '</pattern>')


def _defs():
    s = svg_woning()
    d = s[s.index("<defs>") + 6:s.index("</defs>")]
    d = d[:d.index("<style>")] + d[d.index("</style>") + 8:]
    return d + _RIET


DEFS = _defs()


def svg_stijl(st, n, klasse="ip-svg"):
    """Eén woning in de kleuren van een stijl. n maakt de id's binnen de SVG uniek."""
    steen = STEEN[st["gevel"]]
    defs = (DEFS.replace("var(--c-steen2)", steen[2]).replace("var(--c-steen)", steen[1])
            .replace("var(--c-voeg)", steen[3]))
    huis = HUIZEN[st["type"]]()
    # Vaste fill in plaats van de klassen: style.css gebruikt .kd al voor de werkgebiedkaart.
    huis = (huis.replace('class="kk"', f'fill="{KLEUR[st["kozijn"]][1]}"')
            .replace('class="kr"', f'fill="{KLEUR[st["raam"]][1]}"')
            .replace('class="kd"', f'fill="{KLEUR[st["deur"]][1]}"')
            .replace('class="kb"', f'fill="{KLEUR[st["boei"]][1]}"')
            .replace('class="ks"', 'fill="url(#kk-steen)"'))
    achtergrond = (_r(0, 0, 640, 440, extra='fill="url(#kk-lucht)"')
                   + _r(0, 400, 640, 40, extra='fill="#cfc9be"')
                   + _r(0, 400, 640, 3, extra='fill="#b3ada3"'))
    inhoud = f"<defs>{defs}</defs>{achtergrond}{huis}"
    for i in _IDS:
        nieuw = i.replace("kk-", f"ip{n}-")
        inhoud = inhoud.replace(f'id="{i}"', f'id="{nieuw}"').replace(f"url(#{i})", f"url(#{nieuw})")
    label = (f"Tekening van een {HUIS_OMSCHRIJVING[st['type']]}: kozijnen "
             f"{_naam(st['kozijn'])}, ramen {_naam(st['raam'])}, voordeur {_naam(st['deur'])}, "
             f"boeidelen {_naam(st['boei'])}")
    return (f'<svg class="{klasse}" viewBox="0 0 640 440" xmlns="http://www.w3.org/2000/svg" '
            f'role="img" aria-label="{label}">{inhoud}</svg>')


def _naam(kleur_id):
    n = KLEUR[kleur_id][0]
    return n.split(" (")[0].lower()


def kiezer_link(st):
    return (f"{KIEZER_PAD}#type={KIEZER_TYPE[st['type']]}&kozijn={st['kozijn']}&raam={st['raam']}"
            f"&deur={st['deur']}&boei={st['boei']}&gevel={st['gevel']}")


# ---------------------------------------------------------------------------
# Losse blokjes voor andere pagina's
# ---------------------------------------------------------------------------

TEASER_CSS = ('<style>.ip-teaser{background:#fff;border:1px solid var(--line);border-radius:var(--radius-lg);'
              'padding:22px;margin:28px 0;box-shadow:var(--shadow)}.ip-teaser h3{margin-bottom:.3em}'
              '.ip-teaser p{font-size:.95rem;margin-bottom:.8em}.ip-teaser-types{display:flex;flex-wrap:wrap;'
              'gap:8px;margin:0 0 14px;padding:0;list-style:none}.ip-teaser-types a{display:inline-flex;'
              'align-items:center;gap:8px;border:1px solid var(--line);border-radius:99px;padding:6px 12px 6px 6px;'
              'font-size:.88rem;font-weight:600;color:var(--ink);background:var(--bg-soft);text-decoration:none}'
              '.ip-teaser-types a:hover{border-color:var(--accent)}.ip-teaser-types i{display:inline-flex;'
              'border-radius:99px;overflow:hidden;box-shadow:inset 0 0 0 1px rgba(0,0,0,.15)}'
              '.ip-teaser-types b{display:block;width:11px;height:20px}</style>')


def inspiratie_teaser(kop="Inspiratie per woningtype"):
    """Blok met een link per woningtype naar de inspiratiepagina."""
    eerste = {}
    for st in STIJLEN:
        eerste.setdefault(st["type"], st)
    knoppen = "".join(
        f'<li><a href="{PAD}#{k}"><i aria-hidden="true">'
        + "".join(f'<b style="background:{KLEUR[eerste[k][d]][1]}"></b>' for d in ("kozijn", "raam", "deur"))
        + f'</i>{kort}</a></li>'
        for k, _n, kort in WONINGTYPES)
    return (TEASER_CSS + f'<div class="ip-teaser"><h3>{kop}</h3>'
            f'<p>Welke kleuren passen bij een jaren-30-woning, een villa of een monument? Bekijk '
            f'{len(STIJLEN)} uitgewerkte combinaties, met uitleg waarom ze werken.</p>'
            f'<ul class="ip-teaser-types">{knoppen}</ul>'
            f'<a class="btn btn-ghost" href="{PAD}">Bekijk de inspiratie</a></div>')


def inspiratie_home_sectie():
    return f'<section class="section-sm"><div class="wrap narrow">{inspiratie_teaser("Inspiratie voor jouw huis")}</div></section>'


# ---------------------------------------------------------------------------
# De pagina
# ---------------------------------------------------------------------------

def _kaart(st, n):
    chips = "".join(
        f'<li><i style="background:{KLEUR[st[d]][1]}"></i><span><small>{lab}</small>{KLEUR[st[d]][0]}'
        + (f'<em>{KLEURCODES[st[d]][1]}</em>' if KLEURCODES.get(st[d], ("", None))[1] else '<em>beits, geen RAL</em>')
        + '</span></li>'
        for d, lab in ONDERDELEN)
    chips += (f'<li><i class="ip-steen" style="--s:{STEEN[st["gevel"]][1]};--v:{STEEN[st["gevel"]][3]}"></i>'
              f'<span><small>Gevel</small>{STEEN[st["gevel"]][0].split(" (")[0]}</span></li>')
    kort = dict(KIEZER_TYPES)[KIEZER_TYPE[st["type"]]].lower()
    omschrijving = (f"stijl ‘{st['naam']}’ ({WONINGTYPE_NAAM[st['type']].lower()}): kozijnen {kleur_label(st['kozijn'])}, "
                    f"ramen {kleur_label(st['raam'])}, voordeur {kleur_label(st['deur'])}, boeidelen {kleur_label(st['boei'])}")
    return f"""<article class="ip-kaart" id="{st['id']}" data-type="{st['type']}">
  <div class="ip-plaat">{svg_stijl(st, n)}</div>
  <div class="ip-tekst">
    <a class="ip-label" href="{PAD}{st['type']}/">{WONINGTYPE_NAAM[st['type']]}</a>
    <h3>{st['naam']}</h3>
    <ul class="ip-chips">{chips}</ul>
    <p>{st['waarom']}</p>
    <p class="ip-tip"><strong>Tip:</strong> {st['tip']}</p>
    <div class="ip-knoppen">
      <a class="btn btn-primary" href="{kiezer_link(st)}">Probeer deze stijl</a>
      <a class="btn btn-ghost" href="#offerte" data-offerte="{omschrijving}">Offerte</a>
    </div>
    <p class="ip-noot">Opent de kleurenkiezer met vergelijkbare kleuren, op een {kort}.</p>
  </div>
</article>"""


GLANS = [
    ("Mat", "ip-glans-mat",
     "Voor muren en plafonds. Mat verbergt kleine oneffenheden het best. Kies in een gang of kinderkamer "
     "een matte muurverf die je kunt afnemen."),
    ("Zijdeglans", "ip-glans-zijde",
     "Voor keuken, badkamer en houtwerk binnen, zoals deuren, kozijnen en plinten. Goed af te wassen en "
     "minder gevoelig voor vlekken dan mat."),
    ("Hoogglans", "ip-glans-hoog",
     "Voor deuren, trapleuningen en plinten die veel te verduren hebben. Heel slijtvast, maar je ziet elke "
     "deuk en elk oneffen plekje."),
]

# (muur, deur, naam, uitleg) — eigen tekeningen van een deur in een muur
DEUREN = [
    ("#efe8da", "gooiers-groen", "Donkergroen bij warm wit",
     "Rustig en klassiek. Werkt in een hal met veel deuren: elke deur wordt een duidelijk vlak."),
    ("#f4f3ef", "zwart", "Zwart bij koel wit",
     "Strak en grafisch. Kies voor het deurblad zijdeglans, dan blijft het goed schoon te maken."),
    ("#d9ddd6", "bentheimer", "Okergeel bij zacht grijs",
     "Speels en warm. Een mooie manier om een donkere gang wat op te vrolijken."),
]


def _deur_svg(muur, deur_kleur, n):
    hexd = KLEUR[deur_kleur][1]
    return (f'<svg class="ip-deur-svg" viewBox="0 0 200 220" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">'
            f'<rect width="200" height="220" fill="{muur}"/>'
            f'<rect y="196" width="200" height="24" fill="#c9b08a"/><rect y="196" width="200" height="3" fill="#000" opacity=".1"/>'
            f'<rect y="186" width="200" height="10" fill="#fbfaf6"/>'
            f'<rect x="58" y="30" width="84" height="168" fill="#fbfaf6" stroke="rgba(0,0,0,.18)" stroke-width=".8"/>'
            f'<rect x="65" y="37" width="70" height="159" fill="{hexd}"/>'
            f'<rect x="73" y="47" width="54" height="62" fill="#000" opacity=".12"/>'
            f'<rect x="75" y="49" width="50" height="58" fill="#fff" opacity=".07"/>'
            f'<rect x="73" y="121" width="54" height="64" fill="#000" opacity=".12"/>'
            f'<rect x="75" y="123" width="50" height="60" fill="#fff" opacity=".07"/>'
            f'<rect x="122" y="112" width="10" height="3.5" rx="1.5" fill="#b8a46a"/>'
            f'<rect x="150" y="70" width="34" height="44" fill="#fff" stroke="#b9a37c" stroke-width="3"/>'
            f'<rect x="156" y="78" width="22" height="28" fill="#c9d6c4"/>'
            f'<path d="M14 196 q6-40 22-52 q-4 26 2 52z" fill="#7c9a58"/><rect x="12" y="176" width="26" height="20" rx="3" fill="#b36b4a"/>'
            f'</svg>')



# ---------------------------------------------------------------------------
# inspiratie-content: foto's, kleurcodes, bronnen en de gidsen per woningtype
# ---------------------------------------------------------------------------

KORT_PER_TYPE = {
    "jaren30": "Erker, glas-in-lood en veel houtwerk.",
    "jaren70": "Brede kozijnen, dakkapel en een donkere steen.",
    "villa": "Luiken, lijsten en grote kozijnen.",
    "polder": "Houten gevels in zon en wind.",
    "monument": "Hoge ramen, kroonlijst en soms een vergunning.",
    "nieuwbouw": "Strak, veel glas, hout of kunststof.",
}


def _e(t):
    return t.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;")


def foto_met_bijschrift(f, sizes, boven_vouw=False, kort=False):
    """Foto uit foto_data met een bijschrift en de naamsvermelding die de licentie vraagt."""
    tekst = "" if kort else f'{_e(f["onderschrift"])} '
    credit = (f'<span class="ip-credit">Foto: {_e(f["maker"])}, '
              f'<a href="{f["licentie_url"]}" rel="license nofollow noopener" target="_blank">{f["licentie"]}</a>, '
              f'<a href="{f["bron"]}" rel="nofollow noopener" target="_blank">Wikimedia Commons</a></span>')
    html = foto(f, sizes, boven_vouw)
    return html.replace("</figure>", f'<figcaption>{tekst}{credit}</figcaption></figure>')


def types_sectie(kop="Kies je woningtype", h="h2"):
    kaarten = ""
    for k, naam, _kort in WONINGTYPES:
        f = FOTOS_INSPIRATIE[k][0]
        kaarten += (f'<a class="ip-type" href="{PAD}{k}/">'
                    f'{foto(f, "(max-width:640px) calc(50vw - 28px), (max-width:1000px) 30vw, 360px")}'
                    f'<span class="ip-type-tekst"><strong>{naam}</strong><small>{KORT_PER_TYPE[k]}</small></span></a>')
    return (f'<section class="section-sm ip-types-sec"><div class="wrap"><{h} class="ip-types-kop">{kop}</{h}>'
            f'<p class="ip-smal">Per woningtype een gids met foto’s uit de regio: wat je schildert, waar je op let, '
            f'onderhoud en kleuren met RAL-code.</p>'
            f'<div class="ip-types">{kaarten}</div></div></section>')


def kleurcodes_tabel(ids):
    rijen = ""
    for i in ids:
        naam, ral, hexw, noot = KLEURCODES[i]
        rijen += (f'<tr><td><i class="ip-staal" style="background:{hexw}"></i></td><td><strong>{naam}</strong>'
                  f'{("<br><small>" + noot + "</small>") if noot else ""}</td>'
                  f'<td>{ral or "geen RAL-code"}</td><td><code>{hexw.upper()}</code></td></tr>')
    return (f'<div class="ip-tabel-wrap"><table class="ip-codes"><thead><tr><th><span class="sr-only">Staal</span></th>'
            f'<th>Kleur</th><th>Code</th><th>Hex (scherm)</th></tr></thead><tbody>{rijen}</tbody></table></div>')


def bronnen_lijst(sleutels):
    items = "".join(f'<li><a href="{BRONNEN[k][1]}" rel="nofollow noopener" target="_blank">{BRONNEN[k][0]}</a></li>'
                    for k in sleutels)
    return f'<ul class="ip-bronnen">{items}</ul>'


def _kleur_ids(stijlen):
    gezien = []
    for st in stijlen:
        for d in ("kozijn", "raam", "deur", "boei"):
            if st[d] not in gezien:
                gezien.append(st[d])
    return gezien


def _woorden(html):
    import re
    tekst = re.sub(r"<[^>]+>", " ", html)
    return len(tekst.split())


def build_gids(write, sleutel, n_start):
    g = GIDSEN[sleutel]
    naam = WONINGTYPE_NAAM[sleutel]
    url = f"{PAD}{sleutel}/"
    cr, cr_ld = crumbs([("Home", "/"), ("Inspiratie", PAD), (naam, None)])
    fotos = FOTOS_INSPIRATIE[sleutel]
    stijlen = [st for st in STIJLEN if st["type"] == sleutel]
    kaarten = "".join(_kaart(st, n_start + i) for i, st in enumerate(stijlen))
    kenmerken = "".join(f"<p>{p}</p>" for p in g["kenmerken"])
    onderdelen = "".join(f"<li><strong>{t}.</strong> {u}</li>" for t, u in g["onderdelen"])
    letop = "".join(f"<li>{t}</li>" for t in g["letop"])
    kleuren = "".join(f"<p>{p}</p>" for p in g["kleuren"])
    kosten = "".join(f'<li><a href="{u}">{t}</a></li>' for u, t in g["kosten"])
    plaatsen = ", ".join(f'<a href="/schilder/{s}/">{PLAATS_BY_SLUG[s]["naam"]}</a>'
                         for s in g["plaatsen"] if s in PLAATS_BY_SLUG)
    andere = "".join(f'<li><a href="{PAD}{k}/">{n}</a></li>' for k, n, _ in WONINGTYPES if k != sleutel)
    tweede = (f'<div class="ip-gids-foto2">{foto_met_bijschrift(fotos[1], "(max-width:760px) calc(100vw - 40px), 720px")}</div>'
              if len(fotos) > 1 else "")
    bronnen = list(dict.fromkeys(g["bronnen"] + ["ral", "ral-hex"]))

    tekst = f"""
  <p class="lead">{g['intro']}</p>
  <h2>Kenmerken van dit woningtype</h2>
  {kenmerken}
  <h2>Wat wordt er geschilderd?</h2>
  <ul class="checklist">{onderdelen}</ul>
  {tweede}
  <h2>Waar let je op?</h2>
  <ul class="ip-letop">{letop}</ul>
  <h2>Onderhoud</h2>
  <p>{ONDERHOUD_ALGEMEEN}</p>
  <p>{g['onderhoud']}</p>
  <h2>Welke kleuren passen erbij?</h2>
  {kleuren}"""

    faq_html, faq_ld = faq_blok([
        (f"Hoe vaak moet ik een {naam.lower()} laten schilderen?",
         "Gemiddeld zit er ongeveer vijf jaar tussen twee schilderbeurten, maar dat hangt af van de verf, de "
         "kwaliteit van het werk en hoeveel zon en regen het hout vangt. Kijk elk voorjaar zelf even na."),
        ("Kloppen de RAL-codes met de kleur op mijn scherm?",
         "De codes kloppen; de kleur op je scherm is een benadering. Vraag de schilder om een staal of een "
         "proefvlak op je eigen kozijn voordat je kiest."),
    ], f"Vragen over een {naam.lower()}")

    body = f"""{cr}
<section class="section-sm ip-gids"><div class="wrap narrow">
  <span class="badge">Inspiratie per woningtype</span>
  <h1>{g['h1']}</h1>
  {foto_met_bijschrift(fotos[0], "(max-width:760px) calc(100vw - 40px), 720px", boven_vouw=True)}
  <div class="prose">{tekst}</div>
</div></section>

<section class="section-sm soft"><div class="wrap">
  <h2>Twee uitgewerkte kleurcombinaties</h2>
  <p class="ip-smal">Probeer een combinatie in de <a href="{KIEZER_PAD}">kleurenkiezer</a>, of vraag er direct een offerte voor aan.</p>
  <div class="ip-grid ip-grid-2">{kaarten}</div>
  <p class="ip-schermnoot">De tekeningen zijn voorbeelden. Kleuren op een scherm wijken altijd wat af van echte verf.</p>
</div></section>

<section class="section-sm"><div class="wrap narrow">
  <h2>De kleuren met hun RAL-code</h2>
  <p>RAL Classic is een Duitse kleurnorm die schilders en verfwinkels in heel Nederland kennen. Met de code mengt de verfwinkel de kleur bij elk merk. De namen in deze tabel zijn de officiële RAL-namen; welke code bij een stijl hoort, is ons voorstel.</p>
  {kleurcodes_tabel(_kleur_ids(stijlen))}
  <div class="grid g2 ip-verder">
    <div><h3>Kosten</h3><ul>{kosten}<li><a href="/kosten/calculator/">Reken je eigen huis door</a></li></ul></div>
    <div><h3>Verder kijken</h3><ul><li><a href="{KIEZER_PAD}">Zelf kleuren kiezen in de kleurenkiezer</a></li><li><a href="/onderhoudscheck/">Doe de onderhoudscheck</a></li><li><a href="/schilderwerk/buitenschilderwerk/">Buitenschilderwerk</a></li><li><a href="/schilderwerk/houtrot-reparatie/">Houtrot laten repareren</a></li></ul></div>
  </div>
  <p>Schilders in de buurt van dit soort woningen vind je onder meer in {plaatsen}.</p>
  <h3>Andere woningtypes</h3>
  <ul class="ip-andere">{andere}</ul>
  <h3>Bronnen</h3>
  {bronnen_lijst(bronnen)}
</div></section>

<section class="section" id="offerte-inspiratie"><div class="wrap">
  <div class="grid g2" style="gap:48px;align-items:start">
    <div>
      <span class="badge">Van idee naar offerte</span>
      <h2>Laat je {naam.lower()} schilderen</h2>
      <p class="lead">Klik bij een combinatie op <strong>Offerte</strong>; die komt dan vanzelf in het formulier.</p>
      <ul class="checklist">
        <li><strong>Gratis en vrijblijvend.</strong> Je krijgt offertes van maximaal drie schilders uit jouw regio.</li>
        <li><strong>Vraag om een kleurstaal.</strong> Een goede schilder laat je de kleur eerst op je eigen kozijn zien.</li>
      </ul>
    </div>
    <div>{offerte_form("Offerte voor jouw nieuwe kleuren", "Gratis · vrijblijvend · maximaal 3 schilders")}</div>
  </div>
</div></section>
{faq_html}"""

    artikel_ld = {
        "@context": "https://schema.org", "@type": "Article", "headline": g["h1"],
        "description": g["description"], "inLanguage": "nl-NL",
        "image": f"https://topschilder.nl/assets/fotos/{fotos[0]['naam']}-1600.webp",
        "mainEntityOfPage": f"https://topschilder.nl{url}",
        "publisher": {"@type": "Organization", "name": "Topschilder", "url": "https://topschilder.nl/"},
    }
    html = page(title(g["titel"]), g["description"], url, body, [cr_ld, artikel_ld, faq_ld])
    html = html.replace('<link rel="stylesheet" href="/assets/css/style.css">',
                        '<link rel="stylesheet" href="/assets/css/style.css">'
                        '<link rel="stylesheet" href="/assets/css/inspiratie.css">')
    html = html.replace("</body>", '<script src="/assets/js/inspiratie.js" defer></script></body>')
    write(url, html, prio=0.6)
    return _woorden(tekst)


def kleurnamen_sectie():
    alle = _kleur_ids(STIJLEN)
    return f"""<section class="section-sm" id="kleurcodes"><div class="wrap narrow prose">
  <span class="badge">Kleurnamen en codes</span>
  <h2>Waar komen de kleurnamen vandaan?</h2>
  <p>Namen als monumentengroen, grachtengroen of ossenbloedrood klinken als vaste kleuren, maar dat zijn ze niet. Elk verfmerk maakt er een eigen versie van. Daarom staat bij elke kleur op deze pagina een RAL-code: daarmee weet de verfwinkel precies welke kleur je bedoelt.</p>
  <ul>
    <li><strong>Groen met wit is een oude Nederlandse combinatie.</strong> Het {bron("olm-kozijn", "Nederlands Openluchtmuseum")} schrijft dat groene kozijnen eerst iets voor deftige huizen waren, omdat de verf duur was. Toen in de negentiende eeuw het goedkopere standgroen op de markt kwam, kozen veel mensen alsnog voor groen.</li>
    <li><strong>Monumentengroen is minder oud dan het klinkt.</strong> Volgens het {bron("olm-gebouwen", "Openluchtmuseum")} bestaat het pas sinds de twintigste eeuw. Daarvoor werd groen gebruikt van grijsgroen tot helder lichtgroen.</li>
    <li><strong>Groen verkleurt.</strong> Groen dat uit geel en blauw pigment is gemengd, wordt in de zon blauwer, en standgroen wordt donkerder met de jaren ({bron("olm-kozijn", "bron")}).</li>
    <li><strong>Ossenbloed was echt bloed.</strong> In de Middeleeuwen werd ossenbloed gebruikt als bindmiddel voor verf ({bron("olm-kozijn", "bron")}). De rode kleur die nu zo heet, is gewone verf.</li>
  </ul>
  <h3>Alle kleuren op deze pagina</h3>
  <p>De codes en namen komen uit de {bron("ral", "officiële RAL-lijst")}. De hexwaarde is een benadering voor je scherm, overgenomen uit de {bron("ral-hex", "Wikipedia-lijst van RAL-kleuren")}. Welke code bij een stijl hoort, is ons voorstel.</p>
  {kleurcodes_tabel(alle)}
</div></section>"""


def build_inspiratie(write, out_dir):
    cr, cr_ld = crumbs([("Home", "/"), ("Buitenschilderwerk", "/schilderwerk/buitenschilderwerk/"),
                        ("Inspiratie", None)])

    filters = ('<button type="button" class="ip-filter on" data-filter="alle" aria-pressed="true">Alles</button>'
               + "".join(f'<button type="button" class="ip-filter" data-filter="{k}" aria-pressed="false" '
                         f'aria-label="{n}">{kort}</button>' for k, n, kort in WONINGTYPES))
    kaarten = "".join(_kaart(st, i + 1) for i, st in enumerate(STIJLEN))
    ankers = "".join(f'<span class="ip-anker" id="{k}"></span>' for k, _n, _k in WONINGTYPES)
    snel = " · ".join(f'<a href="#{k}">{n}</a>' for k, n, _ in WONINGTYPES)

    glans = "".join(
        f'<div class="ip-glans"><div class="ip-glans-staal {cls}" aria-hidden="true"></div>'
        f'<h3>{n}</h3><p>{t}</p></div>' for n, cls, t in GLANS)
    deuren = "".join(
        f'<figure class="ip-deur">{_deur_svg(m, d, i)}<figcaption><strong>{n}</strong>{u}</figcaption></figure>'
        for i, (m, d, n, u) in enumerate(DEUREN))

    monumenten = _monument_plaatsen()
    mon_links = ", ".join(f'<a href="/schilder/{p["slug"]}/">{p["naam"]}</a>' for p in monumenten)
    mon_zin = (f" Denk aan de oude kernen van {mon_links}." if mon_links else "")

    faqs = [
        ("Welke kleur kozijnen past bij mijn huis?",
         "Kijk eerst naar wat blijft: de kleur van de steen, het dak en eventueel glas-in-lood. Kies daar één "
         "rustige basiskleur bij voor kozijnen en boeidelen, en één accent voor de voordeur of de ramen. Op "
         "deze pagina zie je per woningtype twee uitgewerkte voorbeelden."),
        ("Kost een kleurwissel meer dan opnieuw dezelfde kleur?",
         "Meestal wel. Ga je van licht naar donker of andersom, dan dekt één laag vaak niet. Er komt dan een "
         "extra laag bij, soms eerst een grondlaag in een tussenkleur. Dat kost meer verf en meer uren. Vraag "
         "in de offerte of die extra laag erin zit."),
        ("Mag ik de kleur van mijn monument zelf kiezen?",
         "Niet altijd. Bij een monument of een pand in een beschermd stadsgezicht kan een andere kleur "
         "vergunningplichtig zijn, of heeft de gemeente kleuren die passen. Vraag het vooraf na bij je "
         "gemeente. Huur je of woon je in een VvE? Vraag dan de verhuurder of de VvE."),
        ("Welke glansgraad kies ik binnen?",
         "Mat voor muren en plafonds, zijdeglans voor houtwerk en vochtige ruimtes, en hoogglans voor deuren "
         "en leuningen die veel te verduren hebben. Hoe hoger de glans, hoe beter af te wassen, maar hoe meer "
         "je oneffenheden ziet."),
        ("Kloppen de kleuren in de tekeningen met echte verf?",
         "De RAL-codes kloppen, maar de kleur op je scherm is een benadering. Elk scherm toont kleuren anders, "
         "en buiten ziet verf er in de zon anders uit dan binnen. Geef de RAL-code door aan je schilder en vraag "
         "om een kleurstaal of een proefvlak op je eigen kozijn."),
    ]
    faq_html, faq_ld = faq_blok(faqs, "Vragen over kleur en stijl")

    lijst_ld = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "Kleurcombinaties per woningtype",
        "numberOfItems": len(STIJLEN),
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1,
             "name": f"{st['naam']} ({WONINGTYPE_NAAM[st['type']].lower()})",
             "url": f"https://topschilder.nl{PAD}#{st['id']}"}
            for i, st in enumerate(STIJLEN)
        ],
    }

    body = f"""{cr}
<section class="section-sm ip-intro"><div class="wrap">
  <span class="badge">Inspiratie en stijlgids</span>
  <h1>Welke kleuren passen bij jouw huis?</h1>
  <p class="lead">Een jaren-30-woning vraagt om andere kleuren dan een strakke nieuwbouwwoning. Hier vind je per woningtype een gids met foto’s, en twee kleurcombinaties voor kozijnen, ramen, voordeur en boeidelen, met RAL-codes en uitleg waarom ze werken. Bevalt er een? Probeer hem in de <a href="{KIEZER_PAD}">kleurenkiezer</a> en pas hem aan.</p>
  <p class="ip-snel">Direct naar: {snel}</p>
</div></section>
{types_sectie()}

<section class="ip-galerij"><div class="wrap">
  {ankers}
  <div class="ip-filters" role="group" aria-label="Filter op woningtype" hidden>{filters}</div>
  <p class="ip-telling" role="status" aria-live="polite"></p>
  <div class="ip-grid">{kaarten}</div>
  <p class="ip-schermnoot">De tekeningen zijn voorbeelden, geen foto's. Kleuren op een scherm wijken altijd wat af van echte verf; bij elke kleur staat de RAL-code.</p>
</div></section>
{kleurnamen_sectie()}

<section class="section soft"><div class="wrap">
  <h2>Zo kies je zelf een combinatie</h2>
  <p class="lead ip-smal">Staat jouw huis er niet tussen? Met deze vijf stappen kom je een heel eind.</p>
  <ol class="ip-stappen">
    <li><h3>Begin bij wat blijft</h3><p>De steen, het dak en het glas veranderen niet. Leg een foto van je gevel naast de kleuren die je overweegt.</p></li>
    <li><h3>Eén basiskleur</h3><p>Geef kozijnen en boeidelen meestal dezelfde, rustige kleur. Dat houdt de gevel bij elkaar.</p></li>
    <li><h3>Eén accent</h3><p>Kies één plek voor een sprekende kleur: de voordeur, de ramen of allebei. Meer accenten maken het druk.</p></li>
    <li><h3>Kijk naar de straat</h3><p>In een rij of bij een twee-onder-een-kap kijk je ook naar de buren. Bij een VvE gelden vaak vaste kleuren.</p></li>
    <li><h3>Proef eerst</h3><p>Vraag de schilder om een proefvlak op je eigen kozijn. Bekijk het in de ochtend en in de avond.</p></li>
  </ol>
</div></section>

<section class="section" id="binnen"><div class="wrap">
  <span class="badge">Binnen</span>
  <h2>Kleur en glans binnen</h2>
  <p class="lead ip-smal">Binnen draait het minder om stijl en meer om licht, gebruik en onderhoud. Drie dingen om op te letten.</p>
  <h3 class="ip-subkop">1. De juiste glansgraad</h3>
  <div class="ip-glanzen">{glans}</div>
  <div class="grid g2 ip-binnen">
    <div>
      <h3 class="ip-subkop">2. Kleur in kleine ruimtes</h3>
      <ul class="checklist">
        <li><strong>Licht en warm</strong> houdt een kleine kamer of gang open. Gebroken wit oogt vaak zachter dan zuiver wit.</li>
        <li><strong>Muur en plafond in één kleur</strong> laat de randen vervagen. De ruimte voelt dan minder hokkerig.</li>
        <li><strong>Plinten en deuren in de muurkleur</strong> geven rust: er zijn minder lijnen die het oog vangen.</li>
        <li><strong>Durf ook donker.</strong> Een donkere kleur maakt een toilet of werkkamer niet groter, maar wel knus. Dat kan juist mooi zijn.</li>
      </ul>
    </div>
    <div>
      <h3 class="ip-subkop">3. Deuren in een contrastkleur</h3>
      <p>Een binnendeur in een andere kleur dan de muur is een kleine klus met veel effect. Schilder alleen het deurblad, of deur en kozijn samen. Een donkere deur laat ook minder snel vieze plekken van handen zien dan een witte.</p>
    </div>
  </div>
  <div class="ip-deuren">{deuren}</div>
  <p>Binnen laten schilderen? Lees meer over <a href="/schilderwerk/binnenschilderwerk/">binnenschilderwerk</a>.</p>
</div></section>

<section class="section soft"><div class="wrap">
  <div class="grid g2 ip-eerlijk">
    <div>
      <h2>Een nieuwe kleur kost vaak extra</h2>
      <p>Schilder je in dezelfde kleur, dan is één nieuwe laag vaak genoeg. Ga je van wit naar antraciet, of van donkergroen naar crème, dan dekt één laag meestal niet. Er komt dan een extra laag bij, en soms eerst een grondlaag in een tussenkleur.</p>
      <p>Dat kost meer verf en meer uren. Hoeveel, hangt af van het aantal kozijnen en de staat van het hout. Kijk bij <a href="/kosten/kozijnen-schilderen/">wat kost kozijnen schilderen</a> voor richtprijzen, en vraag in elke offerte of de extra laag erin zit.</p>
    </div>
    <div>
      <h2>Monument of beschermd stadsgezicht?</h2>
      <p>Woon je in een monument of in een beschermd stadsgezicht? Vraag dan eerst bij je gemeente of je kleur mag. Soms heb je een vergunning nodig of gelden er vaste kleuren.{mon_zin}</p>
      <div class="callout"><p><strong>Huur je, of woon je in een VvE?</strong> Vraag dan vooraf de verhuurder of de VvE. Vaak liggen de buitenkleuren vast.</p></div>
    </div>
  </div>
</div></section>

<section class="section" id="offerte-inspiratie"><div class="wrap">
  <div class="grid g2" style="gap:48px;align-items:start">
    <div>
      <span class="badge">Van idee naar offerte</span>
      <h2>Laat je nieuwe kleuren uitvoeren</h2>
      <p class="lead">Klik bij een stijl op <strong>Offerte</strong>. Die stijl komt dan vanzelf in het formulier, zodat de schilders weten wat je wilt.</p>
      <ul class="checklist">
        <li><strong>Gratis en vrijblijvend.</strong> Je krijgt offertes van maximaal drie schilders uit jouw regio.</li>
        <li><strong>Eerst je eigen kleuren proberen?</strong> In de <a href="{KIEZER_PAD}">kleurenkiezer</a> pas je elke stijl aan en deel je je ontwerp met één link.</li>
        <li><strong>Vraag om een kleurstaal.</strong> Een goede schilder laat je de kleur eerst op je eigen kozijn zien.</li>
      </ul>
      <p>Meer over het werk zelf: <a href="/schilderwerk/buitenschilderwerk/">buitenschilderwerk</a>, <a href="/kosten/huis-schilderen/">wat het kost om je huis buiten te laten schilderen</a> en de <a href="/onderhoudscheck/">onderhoudscheck</a>.</p>
    </div>
    <div>{offerte_form("Offerte voor jouw nieuwe kleuren", "Gratis · vrijblijvend · maximaal 3 schilders")}</div>
  </div>
</div></section>
{faq_html}"""

    html = page(
        title("Inspiratie: kleuren per woningtype"),
        "Kleurcombinaties voor kozijnen, ramen, voordeur en boeidelen per woningtype, met uitleg. "
        "Probeer elke stijl in de kleurenkiezer en vraag gratis offertes aan.",
        PAD, body, [cr_ld, lijst_ld, faq_ld])
    html = html.replace('<link rel="stylesheet" href="/assets/css/style.css">',
                        '<link rel="stylesheet" href="/assets/css/style.css">'
                        '<link rel="stylesheet" href="/assets/css/inspiratie.css">')
    html = html.replace("</body>", '<script src="/assets/js/inspiratie.js" defer></script></body>')
    write(PAD, html, prio=0.7)

    # inspiratie-content: één gids per woningtype
    n = len(STIJLEN) + 1
    for k, _naam, _kort in WONINGTYPES:
        woorden = build_gids(write, k, n)
        n += 2
        if woorden < 400:
            print(f"  LET OP: gids {k} heeft maar {woorden} woorden lopende tekst")

    _schrijf(os.path.join(out_dir, "assets", "css", "inspiratie.css"), INSPIRATIE_CSS)
    data = {"types": {k: n for k, n, _ in WONINGTYPES}}
    _schrijf(os.path.join(out_dir, "assets", "js", "inspiratie.js"),
             "var IP_DATA = " + json.dumps(data, ensure_ascii=False) + ";\n" + INSPIRATIE_JS)


def _schrijf(pad, inhoud):
    os.makedirs(os.path.dirname(pad), exist_ok=True)
    with open(pad, "w", encoding="utf-8") as f:
        f.write(inhoud)


# ---------------------------------------------------------------------------
# CSS
# ---------------------------------------------------------------------------

INSPIRATIE_CSS = r'''/* Inspiratie en stijlgids — alleen geladen op /inspiratie/ */
.ip-intro{padding-bottom:8px}
.ip-intro .lead{max-width:68ch}
.ip-snel{font-size:.9rem;color:var(--muted);margin:0}
.ip-snel a{font-weight:600}
.ip-galerij{padding:12px 0 56px}
.ip-anker{display:block;height:0;scroll-margin-top:84px}
.ip-filters{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 6px}
.ip-filters[hidden]{display:none}
.ip-filter{border:1px solid var(--line);background:#fff;border-radius:99px;padding:8px 16px;font:inherit;font-size:.9rem;font-weight:650;color:var(--ink);cursor:pointer}
.ip-filter:hover{border-color:var(--navy-500)}
.ip-filter.on{background:var(--navy);border-color:var(--navy);color:#fff}
.ip-filter:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
.ip-telling{font-size:.85rem;color:var(--muted);min-height:1.3em;margin:4px 0 14px}
.ip-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px}
.ip-kaart{display:flex;flex-direction:column;background:#fff;border:1px solid var(--line);border-radius:var(--radius-lg);overflow:hidden;box-shadow:var(--shadow);scroll-margin-top:90px;transition:box-shadow .2s,transform .2s}
.ip-kaart:hover{box-shadow:var(--shadow-lg);transform:translateY(-2px)}
.ip-kaart[hidden]{display:none}
.ip-kaart:target{outline:3px solid var(--accent);outline-offset:2px}
.ip-plaat{background:#f6f1e8;border-bottom:1px solid var(--line)}
.ip-svg{display:block;width:100%;height:auto}
.ip-tekst{display:flex;flex-direction:column;flex:1;padding:16px 18px 18px}
.ip-label{font-size:.74rem;text-transform:uppercase;letter-spacing:.07em;font-weight:700;color:var(--accent-dark)}
.ip-tekst h3{font-size:1.2rem;margin:.15em 0 .55em}
.ip-chips{list-style:none;padding:0;margin:0 0 12px;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:6px 10px}
.ip-chips li{display:flex;align-items:center;gap:8px;min-width:0;font-size:.85rem;line-height:1.2;color:var(--ink)}
.ip-chips i{flex:0 0 22px;height:22px;border-radius:50%;box-shadow:inset 0 0 0 1px rgba(0,0,0,.2)}
.ip-chips i.ip-steen{border-radius:5px;background:repeating-linear-gradient(0deg,var(--v) 0 2px,var(--s) 2px 8px)}
.ip-chips span{display:flex;flex-direction:column;min-width:0}
.ip-chips small{font-size:.7rem;color:var(--muted);text-transform:uppercase;letter-spacing:.05em}
.ip-tekst p{font-size:.94rem;margin:0 0 .7em}
.ip-tip{background:var(--bg-soft);border-radius:var(--radius);padding:9px 12px;font-size:.86rem!important;color:var(--body)}
.ip-knoppen{display:flex;gap:8px;margin-top:auto;padding-top:6px}
.ip-knoppen .btn{flex:1 1 auto;padding:11px 14px;font-size:.92rem;text-align:center}
.ip-knoppen .btn-ghost{flex:0 1 auto}
.ip-noot{font-size:.76rem!important;color:var(--muted);margin:8px 0 0!important}
.ip-schermnoot{font-size:.85rem;color:var(--muted);margin:18px 0 0}
.ip-smal{max-width:64ch}
.ip-stappen{list-style:none;counter-reset:ip;padding:0;margin:26px 0 0;display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:16px}
.ip-stappen li{counter-increment:ip;background:#fff;border:1px solid var(--line);border-radius:var(--radius-lg);padding:18px 16px}
.ip-stappen li::before{content:counter(ip);display:grid;place-items:center;width:34px;height:34px;border-radius:50%;background:var(--accent);color:#fff;font-weight:800;margin-bottom:10px}
.ip-stappen h3{font-size:1.02rem;margin:0 0 .3em}
.ip-stappen p{font-size:.9rem;margin:0}
.ip-subkop{font-size:1.15rem;margin:28px 0 12px}
.ip-glanzen{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}
.ip-glans{border:1px solid var(--line);border-radius:var(--radius-lg);padding:14px;background:#fff}
.ip-glans h3{font-size:1.02rem;margin:12px 0 .25em}
.ip-glans p{font-size:.9rem;margin:0}
.ip-glans-staal{height:110px;border-radius:var(--radius);background:#2f5141;position:relative;overflow:hidden}
.ip-glans-mat{background:linear-gradient(160deg,#35594a,#2c4c3e)}
.ip-glans-zijde{background:radial-gradient(ellipse 70% 55% at 30% 25%,rgba(255,255,255,.28),rgba(255,255,255,0) 70%),linear-gradient(160deg,#3a604f,#26453a)}
.ip-glans-hoog{background:linear-gradient(115deg,rgba(255,255,255,0) 30%,rgba(255,255,255,.55) 38%,rgba(255,255,255,0) 46%),radial-gradient(ellipse 50% 35% at 72% 22%,rgba(255,255,255,.7),rgba(255,255,255,0) 70%),linear-gradient(160deg,#3d6553,#1f3c31)}
.ip-binnen{margin-top:8px;gap:32px}
.ip-deuren{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;margin:8px 0 24px}
.ip-deur{margin:0;background:#fff;border:1px solid var(--line);border-radius:var(--radius-lg);overflow:hidden;display:grid;grid-template-columns:130px minmax(0,1fr);align-items:center}
.ip-deur-svg{display:block;width:100%;height:auto}
.ip-deur figcaption{padding:12px 14px;font-size:.9rem}
.ip-deur figcaption strong{display:block;color:var(--ink);margin-bottom:.15em}
.ip-eerlijk{gap:40px}
.ip-eerlijk h2{font-size:1.35rem}
@media(max-width:1000px){.ip-grid{grid-template-columns:repeat(2,minmax(0,1fr))}.ip-stappen{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:640px){
  .ip-snel{display:none}
  .ip-grid,.ip-glanzen{grid-template-columns:minmax(0,1fr)}
  .ip-stappen{grid-template-columns:minmax(0,1fr)}
  .ip-filters{flex-wrap:nowrap;overflow-x:auto;margin:0 -20px 6px;padding:2px 20px 6px;scrollbar-width:none}
  .ip-filters::-webkit-scrollbar{display:none}
  .ip-filter{flex:0 0 auto}
  .ip-glans-staal{height:70px}
}
@media(max-width:900px){.ip-deuren{grid-template-columns:minmax(0,1fr);gap:10px}}
@media(max-width:420px){.ip-deur{grid-template-columns:110px minmax(0,1fr)}}
@media(prefers-reduced-motion:reduce){.ip-kaart{transition:none}.ip-kaart:hover{transform:none}}

/* inspiratie-content: woningtypes met foto, gidsen, kleurcodes */
.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.ip-label{text-decoration:none}
.ip-label:hover{text-decoration:underline}
.ip-chips em{display:block;font-style:normal;font-size:.72rem;color:var(--muted)}
.ip-types-sec{padding-top:8px}
.ip-types-kop{font-size:1.35rem;margin-bottom:.2em}
.ip-types{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin-top:14px}
.ip-type{display:flex;flex-direction:column;background:#fff;border:1px solid var(--line);border-radius:var(--radius-lg);overflow:hidden;color:var(--ink);text-decoration:none;box-shadow:var(--shadow);transition:box-shadow .2s,transform .2s}
.ip-type:hover{box-shadow:var(--shadow-lg);transform:translateY(-2px)}
.ip-type .foto{margin:0}
.ip-type img{display:block;width:100%;height:auto;aspect-ratio:3/2;object-fit:cover}
.ip-type-tekst{display:flex;flex-direction:column;padding:10px 14px 13px}
.ip-type-tekst strong{font-size:1rem}
.ip-type-tekst small{font-size:.85rem;color:var(--muted);line-height:1.35}
.ip-gids h1{margin:.2em 0 .5em}
.ip-gids .foto{margin:0 0 6px}
.ip-gids .foto img,.ip-gids-foto2 img{display:block;width:100%;height:auto;border-radius:var(--radius-lg)}
.foto figcaption{font-size:.84rem;color:var(--muted);margin-top:6px;line-height:1.4}
.ip-credit{display:block;font-size:.76rem}
.ip-credit a{color:inherit}
.ip-gids-foto2{margin:22px 0}
.ip-letop li{margin-bottom:.45em}
.ip-grid-2{grid-template-columns:repeat(2,minmax(0,1fr))}
.ip-tabel-wrap{overflow-x:auto;margin:14px 0 22px}
.ip-codes{width:100%;border-collapse:collapse;font-size:.92rem}
.ip-codes th,.ip-codes td{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line);vertical-align:top}
.ip-codes th{font-size:.78rem;text-transform:uppercase;letter-spacing:.05em;color:var(--muted)}
.ip-codes small{color:var(--muted)}
.ip-codes td:nth-child(3),.ip-codes td:nth-child(4){white-space:nowrap}
.ip-staal{display:inline-block;width:28px;height:28px;border-radius:6px;box-shadow:inset 0 0 0 1px rgba(0,0,0,.2)}
.ip-verder ul,.ip-andere{padding-left:1.1em}
.ip-andere{display:flex;flex-wrap:wrap;gap:4px 22px}
.ip-bronnen{font-size:.86rem;padding-left:1.1em}
.ip-bronnen li{margin-bottom:.3em;overflow-wrap:anywhere}
@media(max-width:1000px){.ip-types{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:640px){
  .ip-types{gap:10px}
  .ip-type-tekst small{display:none}
  .ip-grid-2{grid-template-columns:minmax(0,1fr)}
  .ip-codes{font-size:.84rem}
  .ip-codes th,.ip-codes td{padding:7px 5px}
  .ip-codes th{white-space:normal;font-size:.7rem}
  .ip-codes code{font-size:.76rem}
  .ip-staal{width:20px;height:20px}
}
'''

# ---------------------------------------------------------------------------
# JavaScript
# ---------------------------------------------------------------------------

INSPIRATIE_JS = r'''/* Inspiratie — filter op woningtype (ook via #woningtype in de URL) en stijl naar het formulier. */
(function () {
  "use strict";
  var D = IP_DATA;
  var balk = document.querySelector(".ip-filters");
  var kaarten = [].slice.call(document.querySelectorAll(".ip-kaart"));
  var telling = document.querySelector(".ip-telling");
  koppelOfferte();
  if (!balk || !kaarten.length) return;
  balk.hidden = false;

  function filter(type) {
    if (type !== "alle" && !D.types[type]) type = "alle";
    var n = 0;
    kaarten.forEach(function (k) {
      var zien = type === "alle" || k.dataset.type === type;
      k.hidden = !zien;
      if (zien) n++;
    });
    balk.querySelectorAll(".ip-filter").forEach(function (b) {
      var on = b.dataset.filter === type;
      b.classList.toggle("on", on);
      b.setAttribute("aria-pressed", on);
      if (on && balk.scrollWidth > balk.clientWidth) balk.scrollLeft = Math.max(0, b.offsetLeft - balk.offsetLeft - 20);
    });
    if (telling) telling.textContent = type === "alle" ? n + " stijlen" : n + " stijlen voor: " + D.types[type].toLowerCase();
  }

  balk.querySelectorAll(".ip-filter").forEach(function (b) {
    b.addEventListener("click", function () {
      var t = b.dataset.filter;
      filter(t);
      if (history.replaceState) history.replaceState(null, "", t === "alle" ? location.pathname : "#" + t);
    });
  });

  function vanHash() {
    var h = location.hash.slice(1);
    // de browser springt zelf naar het anker met die naam boven de filterknoppen
    if (D.types[h]) { filter(h); return; }
    // #stijl-id: toon alles, de browser springt zelf naar de kaart
    filter("alle");
  }
  window.addEventListener("hashchange", function () {
    var h = location.hash.slice(1);
    if (D.types[h]) filter(h);
  });
  vanHash();

  /* Stijl in het offerteformulier zetten */
  function koppelOfferte() {
  document.querySelectorAll("[data-offerte]").forEach(function (a) {
    a.addEventListener("click", function (e) {
      var form = document.querySelector("form[data-wizard]");
      if (!form) return;
      e.preventDefault();
      var oms = form.querySelector("textarea[name=omschrijving]");
      if (oms) {
        var regel = "Kleurwens: " + a.dataset.offerte + ".";
        var oud = oms.value.replace(/^Kleurwens: .*$/m, "").trim();
        oms.value = regel + (oud ? "\n" + oud : "");
      }
      var dienst = [].slice.call(form.querySelectorAll("input[name=dienst]")).filter(function (i) { return i.value === "Buitenschilderwerk"; })[0];
      if (dienst && !dienst.checked) dienst.click();
      var box = document.getElementById("offerte");
      if (box) window.scrollTo({ top: box.getBoundingClientRect().top + window.scrollY - 90, behavior: "smooth" });
    });
  });
  }
})();
'''
