# -*- coding: utf-8 -*-
"""
Je huis in een nieuwe kleur (/tools/gevelkleur/).

Vier getekende gevels (jaren 30, rijtjeshuis jaren 70, vrijstaand, herenhuis) met losse vlakken
voor kozijnen, ramen, voordeur, boeidelen, dakgoot en gevel. Met kleuradvies per bouwstijl,
een kleurcheck die waarschuwt bij lastige combinaties en bij donkere kleuren op hout in de zon,
een vergelijking van twee varianten naast elkaar en een plaatje (PNG) om te bewaren of te delen.

Niets dubbel met de kleurenkiezer (/kleuren-kiezen/):
- de kleuren (KLEUREN), de stenen (STENEN) en de tekenhulpjes (raam, deur, boei) komen uit
  kleuren_kiezer.py. Deze tool toont alleen kleurnamen, geen codes.
- het plaatje maakt deelbeeld.js (window.TSDeel), dat ook de onderhoudskalender en de
  verfcalculator gebruiken.
De kleurenkiezer is er om snel kozijnkleuren met codes te kiezen; deze tool is voor de hele gevel,
met advies, waarschuwingen en vergelijken. De pagina's linken naar elkaar.

build.py hoeft hiervoor niets te weten: features.build_features() roept build_gevelkleur() aan.
"""

import json
import os

from components import page, crumbs, offerte_form, faq_blok, title
from kleuren_kiezer import KLEUREN, STENEN, LIJN, _r, raam, deur, boei, garagedeur

PAD = "/tools/gevelkleur/"

# ---------------------------------------------------------------------------
# Onderdelen en kleuren
# ---------------------------------------------------------------------------

DELEN = [
    # sleutel, label, uitleg
    ("gevel", "Gevel", "De muur. Kies de kleur van je steen, of een verfkleur als de gevel geschilderd is of wordt."),
    ("kozijn", "Kozijnen", "Het vaste houtwerk rond ramen en deuren."),
    ("raam", "Ramen", "De delen die open kunnen."),
    ("deur", "Voordeur", "Bij het vrijstaande huis ook de garagedeur."),
    ("boei", "Boeidelen", "De planken langs de dakrand, de dakkapel en de kroonlijst."),
    ("goot", "Dakgoot", "De goot en de regenpijp. Zink kun je ook ongeschilderd laten."),
]

ZINK = {"id": "zink", "naam": "Zink (niet geschilderd)", "hex": "#A3A9AC"}

# Verfkleuren die je op een gevel ziet (geschilderde steen, stucwerk of houten gevelbekleding).
GEVEL_VERF = ["gebroken-wit", "cremewit", "wit", "licht-ivoor", "lichtgrijs", "steengrijs", "kwartsgrijs",
              "antraciet", "zwartgrijs", "olijfgroen", "falurood"]


def _palet(deel):
    if deel == "gevel":
        stenen = [f"s-{s[0]}" for s in STENEN if s[0] in ("rood", "bruin", "geel", "antraciet")]
        return stenen + GEVEL_VERF
    sleutel = "boei" if deel == "goot" else deel
    # eikenhout-look is een uitstraling (beits of folie), geen verfkleur: die laten we weg.
    ids = [k["id"] for k in KLEUREN if sleutel in k["delen"] and k["id"] != "eiken"]
    return (["zink"] + ids) if deel == "goot" else ids


# ---------------------------------------------------------------------------
# Kleuradvies per bouwstijl
# ---------------------------------------------------------------------------
# preset: naam, gevel, kozijn, raam, deur, boei, goot

TYPES = [
    {
        "id": "dertig", "naam": "Jaren-30-woning", "kort": "Jaren 30",
        "advies": "Een jaren-30-huis heeft veel details: een erker, glas-in-lood en vaak een puntgevel. "
                  "Lichte kozijnen in crème of wit laten die details zien. Kleur zet je op de ramen en de voordeur, "
                  "bijvoorbeeld donkergroen, roodbruin of donkerblauw. Bij rode en bruine steen passen warme kleuren het best.",
        "tips": ["Kozijnen en boeidelen licht, ramen en deur in kleur.",
                 "Kies hoogstens twee kleuren naast het wit.",
                 "Helemaal antraciet kan, maar dan vallen de details weg."],
        "regel": "licht_kozijn",
        "presets": [
            ("Klassiek jaren 30", "s-bruin", "cremewit", "bruinrood", "grachtengroen", "cremewit", "cremewit"),
            ("Groen en crème", "s-rood", "cremewit", "dennengroen", "dennengroen", "cremewit", "cremewit"),
            ("Fris met blauw", "s-rood", "wit", "wit", "staalblauw", "wit", "zink"),
        ],
    },
    {
        "id": "zeventig", "naam": "Rijtjeshuis uit de jaren 70", "kort": "Jaren 70",
        "advies": "Een rijtjeshuis uit de jaren 70 heeft grote ramen, brede boeidelen en vaak houten panelen onder de ramen. "
                  "Een rustige, strakke kleur werkt hier goed: antraciet, kwartsgrijs of wit. Brede boeidelen vallen sterk op. "
                  "In een donkere kleur oogt het dak rustiger. Let op de buren: in een rij valt een heel andere kleur snel op.",
        "tips": ["Kozijnen, panelen en boeidelen in één kleur oogt rustig.",
                 "Een voordeur in kleur geeft het huis een eigen gezicht.",
                 "Overleg met de buren als jullie tegelijk schilderen. Dat scheelt vaak in de prijs."],
        "regel": "boei_licht",
        "presets": [
            ("Strak antraciet", "s-bruin", "antraciet", "antraciet", "zwart", "antraciet", "antraciet"),
            ("Warm grijs", "s-rood", "kwartsgrijs", "kwartsgrijs", "bruinrood", "kwartsgrijs", "kwartsgrijs"),
            ("Licht en fris", "s-geel", "wit", "wit", "dennengroen", "wit", "wit"),
        ],
    },
    {
        "id": "vrij", "naam": "Vrijstaand huis", "kort": "Vrijstaand",
        "advies": "Bij een vrijstaand huis heb je de meeste vrijheid, want er zijn geen buren direct naast je. "
                  "Kijk wel naar de omgeving: in het groen passen gedekte kleuren zoals olijfgroen, zand en grijs. "
                  "Een geschilderde lichte gevel met donkere kozijnen oogt modern. Lichte kozijnen bij steen ogen klassiek.",
        "tips": ["Kijk naar de kleur van je dak: die verandert niet mee.",
                 "Laat garagedeur en voordeur bij elkaar passen.",
                 "Proef een kleur op een groot stuk, niet op een klein staaltje."],
        "regel": "",
        "presets": [
            ("Modern licht", "gebroken-wit", "antraciet", "antraciet", "antraciet", "antraciet", "antraciet"),
            ("Landelijk", "s-geel", "licht-ivoor", "olijfgroen", "olijfgroen", "licht-ivoor", "licht-ivoor"),
            ("Klassiek wit", "s-rood", "wit", "wit", "dennengroen", "wit", "wit"),
        ],
    },
    {
        "id": "heren", "naam": "Herenhuis", "kort": "Herenhuis",
        "advies": "Een herenhuis staat vaak in een oude kern of een beschermd stads- of dorpsgezicht. "
                  "Het klassieke beeld: crème of gebroken witte kozijnen en kroonlijst, met ramen en deur in grachtengroen, "
                  "donkerblauw of zwart. Een gepleisterde gevel is vaak gebroken wit of licht grijs. "
                  "Woon je in een monument of beschermd gezicht? Kijk dan eerst wat je gemeente toestaat.",
        "tips": ["Kroonlijst en kozijnen in dezelfde lichte kleur.",
                 "Een donkere voordeur geeft houvast.",
                 "Check de regels bij een monument of in een beschermd gezicht."],
        "regel": "traditioneel",
        "presets": [
            ("Grachtengroen", "s-rood", "cremewit", "grachtengroen", "grachtengroen", "cremewit", "zink"),
            ("Gepleisterd wit", "gebroken-wit", "cremewit", "zwartgroen", "zwart", "cremewit", "cremewit"),
            ("Donkerblauw", "s-bruin", "wit", "staalblauw", "staalblauw", "wit", "wit"),
        ],
    },
]
TYPE_BY_ID = {t["id"]: t for t in TYPES}

# Elke voorbeeldcombinatie moet uit de paletten komen (anders toont de tool een kleur die je niet kunt kiezen).
for _t in TYPES:
    for _p in _t["presets"]:
        for _deel, _kl in zip(("gevel", "kozijn", "raam", "deur", "boei", "goot"), _p[1:]):
            assert _kl in _palet(_deel), (_t["id"], _p[0], _deel, _kl)


# ---------------------------------------------------------------------------
# Tekenen (640 x 440). Klassen: gv gevel, kk kozijn, kr raam, kd deur, kb boeidelen, kg goot.
# ---------------------------------------------------------------------------

def _goot(x, y, w):
    """Dakgoot met een lichtrandje en schaduw eronder."""
    return (f'<rect x="{x:g}" y="{y:g}" width="{w:g}" height="10" rx="4" class="kg" {LIJN}/>'
            + _r(x + 2, y + 1.5, w - 4, 2, extra='fill="#fff" opacity=".28"')
            + _r(x, y + 10, w, 4, extra='fill="#000" opacity=".12"'))


def _pijp(x, y1, y2):
    """Regenpijp met beugels."""
    o = _r(x, y1, 7, y2 - y1, "kg", LIJN) + _r(x + 1.5, y1, 1.6, y2 - y1, extra='fill="#fff" opacity=".22"')
    for by in range(int(y1) + 30, int(y2) - 10, 56):
        o += _r(x - 1.5, by, 10, 3, extra='fill="#000" opacity=".22"')
    return o + _r(x - 3, y2 - 6, 13, 6, "kg", LIJN)


def _heg(x, w, y=386):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="16" rx="8" fill="#6f8f4e"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="6" rx="3" fill="#86a463"/>')


def _boom(x, y, r):
    return (_r(x - 4, y, 9, 400 - y, extra='fill="#6b5338"')
            + f'<circle cx="{x}" cy="{y - r * .5:g}" r="{r}" fill="#7c9a58"/>'
            + f'<circle cx="{x - r * .55:g}" cy="{y + r * .1:g}" r="{r * .62:g}" fill="#6f8f4e"/>')


def _jaren30():
    o = []
    # dak met rode pannen
    o.append('<polygon points="92,216 548,216 474,96 168,96" fill="url(#__P__-dak-rood)"/>')
    o.append(_r(168, 90, 306, 9, extra='fill="#5a2c20"'))
    o.append(_r(430, 52, 26, 60, "gv"))
    o.append(_r(426, 48, 34, 7, extra='fill="#55585b"'))
    # gevel
    o.append(_r(118, 214, 404, 186, "gv"))
    # puntgevel links
    o.append('<polygon points="126,216 232,64 338,216" class="gv"/>')
    o.append(f'<polygon points="108,224 232,46 356,224 336,224 232,74 128,224" class="kb" {LIJN}/>')
    o.append(raam(214, 100, 36, 34, "d", f=5, dorpel=False))
    o.append(raam(172, 150, 120, 58, "dd", boven="ll", bh=14))
    # dakkapel rechts
    o.append(_r(384, 132, 116, 66, extra='fill="#3a2a22"'))
    o.append(_r(384, 142, 8, 54, "kb", LIJN))
    o.append(_r(492, 142, 8, 54, "kb", LIJN))
    o.append(raam(392, 142, 100, 54, "ll", dorpel=False))
    o.append(_r(378, 194, 128, 7, extra='fill="#6d6f70"'))
    o.append(boei(376, 128, 132, 13))
    # goot over de rechterhelft, met regenpijp
    o.append(_goot(336, 212, 214))
    o.append(_pijp(534, 224, 400))
    o.append(_goot(90, 212, 38))
    # erker met plat dakje
    o.append(_r(132, 288, 200, 112, "gv"))
    o.append(_r(132, 288, 8, 112, extra='fill="#000" opacity=".12"'))
    o.append(_r(324, 288, 8, 112, extra='fill="#000" opacity=".12"'))
    o.append(raam(142, 292, 180, 80, "vvv", boven="lll", bh=22))
    o.append(boei(122, 272, 220, 16))
    # bovenverdieping rechts
    o.append(raam(372, 228, 140, 46, "dvd"))
    # voordeur met luifel en raam
    o.append(boei(346, 280, 80, 9))
    o.append(deur(356, 292, 60, 108, "glas30", bovenlicht=20))
    o.append(raam(438, 296, 76, 80, "vd", boven="l", bh=16))
    o.append(_heg(124, 216))
    o.append(_heg(430, 92))
    return "".join(o)


def _jaren70():
    o = []
    # dak over de hele rij
    o.append('<polygon points="0,150 640,150 640,58 0,58" fill="url(#__P__-dak-grijs)"/>')
    o.append(_r(0, 52, 640, 9, extra='fill="#333537"'))
    o.append(_r(0, 168, 640, 232, "gv"))
    # buren: eenvoudige vlakken
    for bx in (-120, 560):
        o.append(_r(bx + 14, 190, 180, 74, extra='fill="#f1efe9"'))
        o.append(_r(bx + 22, 198, 164, 58, extra='fill="url(#kk-glas)"'))
        o.append(_r(bx + 14, 264, 180, 24, extra='fill="#d9d4ca"'))
        o.append(_r(bx + 14, 298, 180, 90, extra='fill="#f1efe9"'))
        o.append(_r(bx + 22, 306, 164, 74, extra='fill="url(#kk-glas)"'))
    o.append(_r(0, 148, 104, 22, extra='fill="#e9e5dc"'))
    o.append(_r(536, 148, 104, 22, extra='fill="#e9e5dc"'))
    # onze brede boeideel met mastgoot
    o.append(boei(100, 146, 440, 22))
    o.append(_goot(100, 168, 440))
    o.append(_r(102, 182, 3, 218, extra='fill="#000" opacity=".2"'))
    o.append(_r(535, 182, 3, 218, extra='fill="#000" opacity=".2"'))
    # bovenverdieping: brede raampartij met paneel eronder (paneel = kozijnkleur)
    o.append(raam(122, 192, 396, 70, "dvvd", dorpel=False))
    o.append(_r(122, 262, 396, 26, "kk", LIJN))
    for px in range(130, 518, 12):
        o.append(_r(px, 264, 1.4, 22, extra='fill="#000" opacity=".16"'))
    o.append(_r(116, 288, 408, 6, extra='fill="#bdb6ab"'))
    # begane grond: deur met zijlicht en pui
    o.append(deur(122, 298, 74, 102, "modern"))
    o.append(raam(196, 298, 26, 102, "v", f=6, dorpel=False))
    o.append(raam(236, 298, 282, 90, "vvd", boven="ddd", bh=20))
    o.append(_pijp(524, 182, 400))
    # buren vervagen
    o.append(_r(0, 46, 100, 354, extra='fill="#fbf8f2" opacity=".55"'))
    o.append(_r(540, 46, 100, 354, extra='fill="#fbf8f2" opacity=".55"'))
    o.append(_heg(232, 290))
    return "".join(o)


def _vrijstaand():
    o = []
    o.append(_r(396, 60, 26, 56, "gv"))
    o.append(_r(392, 56, 34, 7, extra='fill="#55585b"'))
    # garage met plat dak
    o.append(_r(470, 288, 120, 112, "gv"))
    o.append(garagedeur(488, 310, 84, 90))
    o.append(boei(464, 274, 132, 14))
    # hoofdhuis met schilddak
    o.append(_r(148, 212, 324, 188, "gv"))
    o.append('<polygon points="122,216 498,216 420,86 200,86" fill="url(#__P__-dak-grijs)"/>')
    o.append(_r(200, 80, 220, 9, extra='fill="#333537"'))
    o.append(_goot(118, 212, 384))
    o.append(_pijp(154, 226, 400))
    o.append(_pijp(459, 226, 400))
    # dakkapel
    o.append(_r(254, 124, 112, 64, extra='fill="#2f3133"'))
    o.append(_r(254, 132, 8, 56, "kb", LIJN))
    o.append(_r(358, 132, 8, 56, "kb", LIJN))
    o.append(raam(262, 132, 96, 56, "dd", dorpel=False))
    o.append(_r(248, 186, 124, 7, extra='fill="#6d6f70"'))
    o.append(boei(248, 118, 124, 13))
    # ramen en voordeur
    o.append(raam(176, 252, 104, 112, "vv", boven="dd", bh=24))
    o.append(raam(340, 252, 104, 112, "vv", boven="dd", bh=24))
    o.append(boei(282, 256, 56, 8))
    o.append(deur(286, 268, 48, 132, "paneel", bovenlicht=20, f=6))
    o.append(_heg(160, 120))
    o.append(_heg(340, 124))
    o.append(_boom(52, 300, 34))
    return "".join(o)


def _herenhuis():
    o = []
    o.append(_r(0, 128, 196, 272, extra='fill="#e6dccb"'))
    o.append(_r(444, 96, 196, 304, extra='fill="#c9b79b"'))
    for bx, top in ((30, 156), (112, 156), (470, 126), (556, 126)):
        for vy in (top, top + 112):
            o.append(_r(bx, vy, 54, 84, extra='fill="#f1efe9"'))
            o.append(_r(bx + 6, vy + 6, 42, 72, extra='fill="url(#kk-glas)"'))
    o.append('<polygon points="208,62 432,62 402,30 238,30" fill="url(#__P__-dak-grijs)"/>')
    # lijstgevel met kroonlijst en bakgoot erop
    o.append(_r(196, 92, 248, 308, "gv"))
    o.append(_goot(184, 54, 272))
    o.append(_r(186, 66, 268, 24, "kb", LIJN))
    o.append(_r(182, 62, 276, 7, "kb", LIJN))
    for kx in range(198, 440, 22):
        o.append(_r(kx, 90, 8, 8, "kb", LIJN))
    o.append(_r(186, 98, 268, 3, extra='fill="#000" opacity=".14"'))
    o.append(_pijp(200, 68, 400))
    for wx in (222, 296, 370):
        for wy, wh in ((116, 80), (214, 86)):
            o.append(_r(wx - 4, wy - 7, 60, 6, extra='fill="#000" opacity=".14"'))
            o.append(raam(wx, wy, 52, wh, "d", boven="v", bh=18, f=6))
    o.append(_r(196, 306, 248, 4, extra='fill="#000" opacity=".12"'))
    o.append(deur(292, 312, 58, 88, "paneel", bovenlicht=18))
    o.append(raam(220, 318, 56, 64, "d", boven="v", bh=14, f=6))
    o.append(raam(368, 318, 56, 64, "d", boven="v", bh=14, f=6))
    o.append(_r(0, 46, 196, 354, extra='fill="#fbf8f2" opacity=".5"'))
    o.append(_r(444, 46, 196, 354, extra='fill="#fbf8f2" opacity=".5"'))
    return "".join(o)


HUIZEN = (("dertig", _jaren30), ("zeventig", _jaren70), ("vrij", _vrijstaand), ("heren", _herenhuis))


def svg_gevel(prefix="ga"):
    """Eén SVG met alle vier de gevels; JavaScript toont er één. Pattern-id's krijgen `prefix`,
    zodat er twee SVG's naast elkaar kunnen staan met elk een eigen steenkleur."""
    defs = """<defs>
<style>
.gv{fill:url(#__P__-steen)}.kk{fill:var(--c-kozijn)}.kr{fill:var(--c-raam)}.kd{fill:var(--c-deur)}.kb{fill:var(--c-boei)}.kg{fill:var(--c-goot)}
</style>
<linearGradient id="__P__-lucht" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e3eef5"/><stop offset="1" stop-color="#fbf7ef"/></linearGradient>
<linearGradient id="kk-glas" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d5e4ec"/><stop offset="1" stop-color="#8eacbf"/></linearGradient>
<pattern id="__P__-steen" width="40" height="14" patternUnits="userSpaceOnUse">
<rect width="40" height="14" fill="var(--c-voeg)"/>
<rect x="1" y="1" width="18" height="5.6" fill="var(--c-steen)"/><rect x="21" y="1" width="18" height="5.6" fill="var(--c-steen2)"/>
<rect x="0" y="8" width="9" height="5.6" fill="var(--c-steen2)"/><rect x="11" y="8" width="18" height="5.6" fill="var(--c-steen)"/><rect x="31" y="8" width="9" height="5.6" fill="var(--c-steen)"/>
</pattern>
<pattern id="__P__-dak-grijs" width="18" height="11" patternUnits="userSpaceOnUse">
<rect width="18" height="11" fill="#4a4c4f"/><rect y="8.5" width="18" height="2.5" fill="#35373a"/><rect x="8.5" width="1.2" height="9" fill="#3c3e41"/>
</pattern>
<pattern id="__P__-dak-rood" width="18" height="11" patternUnits="userSpaceOnUse">
<rect width="18" height="11" fill="#8a4532"/><rect y="8.5" width="18" height="2.5" fill="#6c3326"/><rect x="8.5" width="1.2" height="9" fill="#743a2b"/>
</pattern>
<pattern id="kk-lood" width="12" height="12" patternUnits="userSpaceOnUse">
<path d="M0 6L6 0L12 6L6 12Z" fill="none" stroke="#3b3b3b" stroke-width=".9" opacity=".7"/>
</pattern>
</defs>"""
    achtergrond = (_r(0, 0, 640, 440, extra='fill="url(#__P__-lucht)"')
                   + _r(0, 400, 640, 40, extra='fill="#cfc9be"')
                   + _r(0, 400, 640, 3, extra='fill="#b3ada3"'))
    groepen = "".join(f'<g data-type="{t}"{"" if t == "dertig" else " display=" + chr(34) + "none" + chr(34)}>{fn()}</g>'
                      for t, fn in HUIZEN)
    svg = (f'<svg class="gk-svg" viewBox="0 0 640 440" xmlns="http://www.w3.org/2000/svg" '
           f'role="img" aria-label="Getekende gevel in de gekozen kleuren">{defs}{achtergrond}{groepen}</svg>')
    return svg.replace("__P__", prefix)


# ---------------------------------------------------------------------------
# Data voor de JavaScript
# ---------------------------------------------------------------------------

def _data():
    kleuren = {k["id"]: {"n": k["naam"], "h": k["hex"]} for k in KLEUREN}
    kleuren["zink"] = {"n": ZINK["naam"], "h": ZINK["hex"]}
    for sid, naam, steen, steen2, voeg in STENEN:
        if sid == "wit":
            continue
        kleuren["s-" + sid] = {"n": naam, "h": steen, "s2": steen2, "v": voeg, "steen": True}
    return {
        "kleuren": kleuren,
        "delen": [{"id": d, "n": n} for d, n, _u in DELEN],
        "palet": {d: _palet(d) for d, _n, _u in DELEN},
        "types": {t["id"]: {"n": t["naam"], "kort": t["kort"], "regel": t["regel"],
                            "presets": [list(p) for p in t["presets"]]} for t in TYPES},
    }


# ---------------------------------------------------------------------------
# Pagina
# ---------------------------------------------------------------------------

def _tool_html():
    types = "".join(
        f'<button type="button" class="gk-type{" on" if i == 0 else ""}" data-type="{t["id"]}" '
        f'aria-pressed="{"true" if i == 0 else "false"}">{t["kort"]}</button>'
        for i, t in enumerate(TYPES))
    delen = "".join(
        f'<button type="button" class="gk-deel{" on" if i == 0 else ""}" data-deel="{d}" '
        f'aria-pressed="{"true" if i == 0 else "false"}"><i class="gk-stip"></i>'
        f'<span><strong>{n}</strong><small data-naam></small></span></button>'
        for i, (d, n, _u) in enumerate(DELEN))
    uitleg = "".join(f'<p class="gk-klein" data-uitleg="{d}"{"" if i == 0 else " hidden"}>{u}</p>'
                     for i, (d, _n, u) in enumerate(DELEN))
    return f"""<div class="gk-tool" id="gevelkleur" data-cmp="0">
  <div class="gk-links">
    <div class="gk-types" role="group" aria-label="Kies je type huis">{types}</div>
    <div class="gk-tabs" role="group" aria-label="Welke variant pas je aan?" hidden>
      <button type="button" class="gk-tab on" data-var="a" aria-pressed="true">Variant A</button>
      <button type="button" class="gk-tab" data-var="b" aria-pressed="false">Variant B</button>
    </div>
    <div class="gk-panes">
      <figure class="gk-pane on" data-pane="a"><figcaption>Variant A</figcaption>{svg_gevel("ga")}</figure>
    </div>
    <p class="gk-klein">Tik op een deel van het huis om het te kiezen. Een scherm toont kleuren nooit precies zoals verf. Kijk altijd naar een echt kleurstaal.</p>
    <div class="gk-acties">
      <button type="button" class="btn btn-ghost" data-vergelijk aria-pressed="false">Vergelijk</button>
      <button type="button" class="btn btn-ghost" data-png>Download als PNG</button>
      <button type="button" class="btn btn-ghost" data-delen hidden>Deel plaatje</button>
      <button type="button" class="btn btn-ghost" data-link>Kopieer link</button>
    </div>
    <p class="gk-melding" role="status" aria-live="polite"></p>
  </div>
  <div class="gk-paneel">
    <h2 class="gk-kop">1. Kies een onderdeel</h2>
    <div class="gk-delen" role="group" aria-label="Onderdelen">{delen}</div>
    <h2 class="gk-kop">2. Kies een kleur <span data-actief></span></h2>
    {uitleg}
    <div class="gk-palet" role="group" aria-label="Kleuren"></div>
    <div class="gk-orient">
      <div class="field"><label for="gk-zon">Welke kant zie je op de tekening?</label>
        <select id="gk-zon"><option value="onbekend" selected>Weet ik niet</option><option value="noord">Noord</option><option value="oost">Oost</option><option value="zuid">Zuid</option><option value="west">West</option></select></div>
      <div class="field"><label for="gk-mat">Waar zijn je kozijnen van?</label>
        <select id="gk-mat"><option value="hout" selected>Hout</option><option value="kunststof">Kunststof</option><option value="aluminium">Aluminium</option></select></div>
    </div>
    <div class="gk-check" aria-live="polite"></div>
    <div class="gk-advies"></div>
    <a class="btn btn-primary btn-block gk-cta" href="#offerte" data-offerte>Offertes voor buitenschilderwerk</a>
  </div>
</div>"""


def build_gevelkleur(write, out):
    cr, cr_ld = crumbs([("Home", "/"), ("Tools", "/tools/"), ("Je huis in een nieuwe kleur", None)])

    hero = f"""{cr}
<section class="section-sm tool-hero gk-hero">
<div class="wrap">
  <div class="gk-intro">
    <span class="badge">Gratis tool · vier soorten huizen · niets opgeslagen</span>
    <h1>Je huis in een nieuwe kleur</h1>
    <p class="lead">Kies je type huis en geef de gevel, kozijnen, ramen, voordeur, boeidelen en dakgoot een kleur. Je krijgt advies dat past bij de bouwstijl, en een waarschuwing als een combinatie lastig is. Twijfel je? Zet twee varianten naast elkaar.</p>
  </div>
  {_tool_html()}
</div>
</section>"""

    stijlen = "".join(
        f'<article class="gk-stijl"><h3>{t["naam"]}</h3><p>{t["advies"]}</p>'
        f'<ul>{"".join(f"<li>{x}</li>" for x in t["tips"])}</ul>'
        f'<p class="gk-presets-k">Probeer: '
        + ", ".join(f'<a href="{PAD}#a={t["id"]},{",".join(p[1:])}" data-preset-link>{p[0]}</a>' for p in t["presets"])
        + '</p></article>'
        for t in TYPES)

    uitleg = f"""<section class="section soft" id="kleuradvies"><div class="wrap">
  <div class="center" style="max-width:680px;margin:0 auto 30px">
    <h2>Kleuradvies per bouwstijl</h2>
    <p class="lead">Elke bouwstijl heeft kleuren die er van oudsher bij horen. Daar hoef je je niet aan te houden, maar het helpt wel bij het kiezen.</p>
  </div>
  <div class="gk-stijlen">{stijlen}</div>
</div></section>
<section class="section"><div class="wrap narrow prose">
  <h2>Zo werkt de tool</h2>
  <p>Kies eerst je type huis. Tik dan op een onderdeel, zoals de kozijnen, en kies een kleur. De tekening verandert meteen mee. Onder de kleuren staat het advies voor jouw bouwstijl, met drie combinaties om mee te beginnen.</p>
  <p>De kleurcheck kijkt naar je hele combinatie. Hij waarschuwt als kozijnen en gevel te veel op elkaar lijken, als je veel verschillende kleuren gebruikt of als twee kleuren net niet bij elkaar passen. Hij let ook op de zon: vul in welke kant van je huis je kleurt en waar je kozijnen van zijn.</p>
  <p>Met <strong>Vergelijk</strong> zet je twee varianten naast elkaar. Met de knop <strong>Download als PNG</strong> bewaar je je ontwerp als plaatje, met de kleurnamen erbij. Dat kun je delen met je huisgenoten of laten zien aan je schilder. Er wordt niets geüpload of opgeslagen.</p>

  <h3 id="warmte">Donkere kleuren op hout in de zon</h3>
  <p>Donkere verf neemt veel meer zonlicht op dan lichte verf. Op de zuid- en westkant wordt donker houtwerk daardoor in de zomer veel warmer. Het hout kan dan gaan werken, er kan hars uit het hout komen en de verf kan blazen of scheuren. Wil je toch antraciet, zwart of donkergroen op houten kozijnen in de zon? Vraag je schilder dan naar verf die daarvoor bedoeld is, of kies een iets lichtere tint. Bij kunststof kozijnen kan een veel donkerdere kleur in de zon het kunststof laten vervormen. Laat een schilder eerst kijken of het kan.</p>

  <h3>Mag je je huis zomaar een andere kleur geven?</h3>
  <p>Voor alleen schilderen in een andere kleur heb je meestal geen vergunning nodig. Wel hebben veel gemeenten een zogenoemde excessenregeling: de gemeente kan optreden tegen kleuren die erg fel zijn of sterk uit de toon vallen. Bij een monument of in een beschermd stads- of dorpsgezicht gelden vaak strengere regels. Kijk in de welstandsnota van je gemeente of vraag het na voordat je begint.</p>

  <h3>Alleen je kozijnkleur kiezen?</h3>
  <p>Wil je vooral weten welke kleur je kozijnen krijgen, met de kleurcodes erbij? Gebruik dan de <a href="/kleuren-kiezen/">kleurenkiezer voor kozijnen en gevel</a>. Daar vind je per kleur de RAL- of NCS-code voor je schilder. Wat het schilderen kost, lees je bij <a href="/kosten/huis-schilderen/">wat kost je huis laten schilderen</a> en <a href="/kosten/kozijnen-schilderen/">kozijnen schilderen</a>. Een geschilderde gevel? Kijk bij <a href="/kosten/gevel-schilderen/">gevel schilderen</a>.</p>
</div></section>"""

    offerte = f"""<section class="section soft" id="offerte-gevel"><div class="wrap">
  <div class="grid g2" style="gap:48px;align-items:start">
    <div class="prose">
      <span class="badge">Van ontwerp naar offerte</span>
      <h2>Je nieuwe kleuren laten schilderen?</h2>
      <p class="lead">Vraag gratis offertes aan voor buitenschilderwerk bij maximaal drie schilders uit jouw regio. Met de knop bij de tool zetten we je kleuren alvast in het formulier.</p>
      <ul class="checklist">
        <li>Gratis en vrijblijvend</li>
        <li>Maximaal drie schilders nemen contact op</li>
        <li>Je kiest zelf of je verder gaat</li>
      </ul>
    </div>
    <div>{offerte_form("Offertes voor buitenschilderwerk", "Gratis · vrijblijvend · maximaal 3 schilders")}</div>
  </div>
</div></section>"""

    faqs = [
        ("Welke kleur kozijnen past bij een jaren-30-huis?",
         "Bij een jaren-30-huis passen lichte kozijnen in crème of wit het best. Kleur zet je op de ramen en de voordeur, "
         "bijvoorbeeld donkergroen, roodbruin of donkerblauw. Zo blijven de details zoals de erker en het glas-in-lood goed zichtbaar."),
        ("Waarom waarschuwt de tool bij donkere kleuren op het zuiden?",
         "Donkere verf neemt veel meer zonlicht op dan lichte verf. Houten kozijnen en boeidelen op het zuiden of westen worden "
         "daardoor veel warmer. Het hout kan gaan werken en de verf kan blazen of scheuren. Met verf die bedoeld is voor donkere "
         "kleuren, of een iets lichtere tint, voorkom je veel problemen. Vraag je schilder ernaar."),
        ("Heb ik een vergunning nodig om mijn huis een andere kleur te geven?",
         "Meestal niet. Wel kan de gemeente optreden tegen kleuren die erg fel zijn of sterk uit de toon vallen. Bij een monument "
         "of in een beschermd stads- of dorpsgezicht gelden vaak strengere regels. Kijk in de welstandsnota van je gemeente of vraag het na."),
        ("Kan ik mijn bakstenen gevel laten schilderen?",
         "Dat kan, maar het is een grote stap. Een geschilderde gevel moet je om de zoveel jaar opnieuw laten doen, en terug naar "
         "kale steen is lastig. Laat eerst een schilder kijken of de steen en de voegen geschikt zijn."),
        ("Kloppen de kleuren op het scherm met echte verf?",
         "Niet precies. Elk scherm toont kleuren anders, en buiten ziet een kleur er door het daglicht weer anders uit. Gebruik de "
         "tool om te kiezen welke kant je op wilt, en kijk daarna naar een echt kleurstaal op je eigen gevel."),
        ("Wat is het verschil met de kleurenkiezer?",
         "Met de kleurenkiezer kies je snel kleuren voor je kozijnen, met de RAL- of NCS-code erbij. Deze tool is voor je hele gevel, "
         "inclusief dakgoot en geschilderde gevel. Je krijgt advies per bouwstijl, een kleurcheck en je kunt twee varianten vergelijken."),
    ]
    faq_html, faq_ld = faq_blok(faqs)

    app_ld = {
        "@context": "https://schema.org", "@type": "WebApplication",
        "name": "Je huis in een nieuwe kleur", "url": "https://topschilder.nl" + PAD,
        "applicationCategory": "DesignApplication", "operatingSystem": "Alle browsers",
        "inLanguage": "nl-NL", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"},
        "description": "Probeer kleuren op vier getekende gevels: jaren 30, rijtjeshuis uit de jaren 70, vrijstaand en herenhuis. "
                       "Met kleuradvies per bouwstijl, een kleurcheck en twee varianten naast elkaar.",
    }

    data_tag = ('<script type="application/json" id="gk-data">'
                + json.dumps(_data(), ensure_ascii=False).replace("</", "<\\/") + "</script>")
    body = (hero + uitleg + offerte + faq_html
            + '<link rel="stylesheet" href="/assets/css/gevelkleur.css">'
            + data_tag + '<script src="/assets/js/deelbeeld.js" defer></script>'
            + '<script src="/assets/js/gevelkleur.js" defer></script>')

    write(PAD, page(
        title("Je huis in een nieuwe kleur: probeer het op je gevel"),
        "Probeer kleuren op je gevel, kozijnen, deur en dakgoot. Met advies per bouwstijl, een kleurcheck en twee varianten naast elkaar. Gratis.",
        PAD, body, [cr_ld, app_ld, faq_ld]), prio=0.8)

    from assets import css_klein
    js = JS.replace("__ADVIES__", json.dumps({t["id"]: t["advies"] for t in TYPES}, ensure_ascii=False))
    for pad, inhoud in (("css/gevelkleur.css", css_klein(CSS)), ("js/gevelkleur.js", js)):
        full = os.path.join(out, "assets", pad)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as f:
            f.write(inhoud)




CSS = r"""
.gk-intro{max-width:740px;margin-bottom:24px}
.gk-tool [hidden]{display:none!important}
.gk-tool{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,380px);gap:28px;align-items:start}
@media(max-width:960px){.gk-tool{grid-template-columns:minmax(0,1fr)}}
.gk-links{min-width:0;position:sticky;top:84px}
@media(max-width:960px){.gk-links{position:static}}
.gk-types,.gk-tabs{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 12px}
.gk-type,.gk-tab{border:1px solid var(--line);background:#fff;border-radius:999px;padding:9px 15px;font:inherit;font-size:.9rem;font-weight:650;color:var(--ink);cursor:pointer;min-height:42px}
.gk-type.on,.gk-tab.on{background:var(--ink);border-color:var(--ink);color:#fff}
.gk-tab.on{background:var(--accent);border-color:var(--accent)}
.gk-type:focus-visible,.gk-tab:focus-visible,.gk-deel:focus-visible,.gk-kleur:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
.gk-panes{display:grid;grid-template-columns:minmax(0,1fr);gap:12px}
.gk-tool[data-cmp="1"] .gk-panes{grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}
.gk-pane{margin:0;border-radius:var(--radius);overflow:hidden;background:#f6f1e8;border:2px solid transparent;position:relative}
.gk-tool[data-cmp="1"] .gk-pane.on{border-color:var(--accent)}
.gk-pane figcaption{display:none;position:absolute;left:8px;top:8px;background:rgba(255,255,255,.92);border-radius:999px;padding:3px 10px;font-size:.78rem;font-weight:700;color:var(--ink)}
.gk-tool[data-cmp="1"] .gk-pane figcaption{display:block}
.gk-svg{display:block;width:100%;height:auto}
.gk-svg .gv,.gk-svg .kk,.gk-svg .kr,.gk-svg .kd,.gk-svg .kb,.gk-svg .kg{cursor:pointer}
.gk-svg.gk-anim .kk,.gk-svg.gk-anim .kr,.gk-svg.gk-anim .kd,.gk-svg.gk-anim .kb,.gk-svg.gk-anim .kg,.gk-svg.gk-anim pattern rect{transition:fill .35s ease}
.gk-klein{font-size:.86rem;color:var(--muted);margin:10px 0 0}
.gk-acties{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}
.gk-acties .btn{flex:1 1 auto;min-height:44px}
.gk-acties [aria-pressed="true"]{background:var(--ink);color:#fff;border-color:var(--ink)}
.gk-melding{min-height:1.4em;font-size:.88rem;color:#0f6e4c;margin:8px 0 0}
.gk-paneel{background:#fff;border:1px solid var(--line);border-radius:var(--radius-lg);box-shadow:var(--shadow);padding:22px;min-width:0}
.gk-kop{font-size:1.05rem;margin:0 0 10px}
.gk-kop+.gk-delen{margin-bottom:18px}
.gk-kop span{font-weight:500;color:var(--muted);font-size:.9rem}
.gk-delen{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:6px}
.gk-deel{display:flex;gap:9px;align-items:center;text-align:left;border:1px solid var(--line);background:#fff;border-radius:10px;padding:8px 10px;font:inherit;cursor:pointer;min-height:48px;min-width:0}
.gk-deel span{min-width:0;display:flex;flex-direction:column}
.gk-deel strong{font-size:.9rem;color:var(--ink)}
.gk-deel small{font-size:.76rem;color:var(--muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.gk-deel.on{border-color:var(--accent);box-shadow:0 0 0 2px rgba(244,130,11,.25)}
.gk-stip{flex:0 0 auto;width:24px;height:24px;border-radius:50%;background:var(--kl,#ddd);box-shadow:inset 0 0 0 1px rgba(0,0,0,.18)}
.gk-palet{display:grid;grid-template-columns:repeat(auto-fill,minmax(64px,1fr));gap:6px;margin:12px 0 16px}
.gk-kleur{border:1px solid var(--line);background:#fff;border-radius:10px;padding:6px 4px;font:inherit;font-size:.7rem;line-height:1.15;color:var(--ink);cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:5px;min-height:70px}
.gk-kleur i{display:block;width:34px;height:34px;border-radius:50%;background:var(--kl);box-shadow:inset 0 0 0 1px rgba(0,0,0,.18)}
.gk-kleur.steen i{background:repeating-linear-gradient(0deg,var(--kv) 0 2px,var(--kl) 2px 9px)}
.gk-kleur[aria-pressed="true"]{border-color:var(--accent);box-shadow:0 0 0 2px rgba(244,130,11,.3);font-weight:700}
.gk-orient{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
.gk-orient .field{margin-bottom:10px}
.gk-orient label{font-size:.82rem}
.gk-orient select{width:100%}
.gk-check{border-radius:12px;padding:14px 16px;margin:4px 0 14px;background:#eef7f1;border:1px solid #bfe0cc}
.gk-check.let{background:#fff6ea;border-color:#f3cf9f}
.gk-check h3{font-size:.98rem;margin:0 0 6px}
.gk-check ul{margin:0;padding-left:18px}
.gk-check li{font-size:.88rem;margin:4px 0}
.gk-check li b{font-weight:700}
.gk-check .tip{color:var(--muted)}
.gk-advies{border-top:1px solid var(--line);padding-top:14px;margin-bottom:16px}
.gk-advies h3{font-size:.98rem;margin:0 0 6px}
.gk-advies p{font-size:.88rem;margin:0 0 10px}
.gk-presets{display:flex;flex-wrap:wrap;gap:6px}
.gk-preset{display:inline-flex;align-items:center;gap:6px;border:1px solid var(--line);background:var(--bg-soft,#faf7f1);border-radius:999px;padding:7px 12px 7px 8px;font:inherit;font-size:.82rem;font-weight:650;color:var(--ink);cursor:pointer;min-height:40px}
.gk-preset i{display:inline-block;width:12px;height:12px;border-radius:50%;margin-right:-9px;box-shadow:0 0 0 1.5px #fff}
.gk-preset i:last-of-type{margin-right:2px}
.gk-stijlen{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:18px}
.gk-stijl{background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:20px}
.gk-stijl h3{margin:0 0 8px}
.gk-stijl p,.gk-stijl li{font-size:.92rem}
.gk-presets-k{margin:10px 0 0;font-weight:600}
@media(max-width:520px){
  .gk-paneel{padding:16px}
  .gk-tool[data-cmp="1"] .gk-panes{gap:6px}
  .gk-pane figcaption{font-size:.7rem;padding:2px 8px;left:5px;top:5px}
  .gk-acties .btn{flex:1 1 45%;padding-left:10px;padding-right:10px;font-size:.9rem}
  .gk-palet{grid-template-columns:repeat(auto-fill,minmax(58px,1fr))}
}
@media(prefers-reduced-motion:reduce){
  .gk-svg.gk-anim .kk,.gk-svg.gk-anim .kr,.gk-svg.gk-anim .kd,.gk-svg.gk-anim .kb,.gk-svg.gk-anim .kg,.gk-svg.gk-anim pattern rect{transition:none}
}
"""

JS = r"""/* Je huis in een nieuwe kleur. Staat in de URL-hash, zodat elk ontwerp een eigen link heeft. */
(function () {
  "use strict";
  var root = document.getElementById("gevelkleur");
  var dataEl = document.getElementById("gk-data");
  if (!root || !dataEl) return;
  var D = JSON.parse(dataEl.textContent);
  var K = D.kleuren, DELEN = ["gevel", "kozijn", "raam", "deur", "boei", "goot"];
  var DEELNAAM = { gevel: "gevel", kozijn: "kozijnen", raam: "ramen", deur: "voordeur", boei: "boeidelen", goot: "dakgoot" };
  var KLASSE = { gv: "gevel", kk: "kozijn", kr: "raam", kd: "deur", kb: "boei", kg: "goot" };
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var $ = function (s, el) { return (el || root).querySelector(s); };
  var $$ = function (s, el) { return [].slice.call((el || root).querySelectorAll(s)); };

  function variantUit(type, p) {
    return { t: type, gevel: p[1], kozijn: p[2], raam: p[3], deur: p[4], boei: p[5], goot: p[6] };
  }
  var st = {
    actief: "a", cmp: false, deel: "gevel", zon: "onbekend", mat: "hout",
    v: { a: variantUit("dertig", D.types.dertig.presets[0]), b: null }
  };

  /* ------------------------------------------------- kleurrekenen */
  function rgb(hex) { var n = parseInt(hex.slice(1), 16); return [n >> 16 & 255, n >> 8 & 255, n & 255]; }
  function lum(hex) {
    var c = rgb(hex).map(function (x) { x /= 255; return x <= 0.03928 ? x / 12.92 : Math.pow((x + 0.055) / 1.055, 2.4); });
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2];
  }
  function contrast(a, b) { var x = lum(a), y = lum(b); return (Math.max(x, y) + 0.05) / (Math.min(x, y) + 0.05); }
  function hsl(hex) {
    var c = rgb(hex).map(function (x) { return x / 255; });
    var mx = Math.max.apply(0, c), mn = Math.min.apply(0, c), l = (mx + mn) / 2, d = mx - mn, h = 0, s = 0;
    if (d) {
      s = d / (1 - Math.abs(2 * l - 1));
      if (mx === c[0]) h = ((c[1] - c[2]) / d) % 6; else if (mx === c[1]) h = (c[2] - c[0]) / d + 2; else h = (c[0] - c[1]) / d + 4;
      h = (h * 60 + 360) % 360;
    }
    return { h: h, s: s, l: l };
  }
  function kleurig(hex) { var x = hsl(hex); return x.s > 0.12 && x.l > 0.12 && x.l < 0.8; }
  function hex(id) { return K[id].h; }
  function naam(id) { return K[id].n; }
  function kort(id) { return naam(id).replace(/ \(.*\)$/, ""); }
  function donker(id) { return lum(hex(id)) < 0.12; }
  function opsom(lijst) { return lijst.length < 2 ? lijst.join("") : lijst.slice(0, -1).join(", ") + " en " + lijst[lijst.length - 1]; }

  /* ------------------------------------------------- tekenen */
  function kleurSvg(svg, v) {
    var g = K[v.gevel], s = svg.style;
    if (g.steen) { s.setProperty("--c-steen", g.h); s.setProperty("--c-steen2", g.s2); s.setProperty("--c-voeg", g.v); }
    else {
      /* geschilderde gevel: steen en voeg in de verfkleur, de voeg een fractie donkerder */
      var c = rgb(g.h).map(function (x) { return Math.round(x * 0.9); });
      s.setProperty("--c-steen", g.h); s.setProperty("--c-steen2", g.h);
      s.setProperty("--c-voeg", "rgb(" + c.join(",") + ")");
    }
    ["kozijn", "raam", "deur", "boei", "goot"].forEach(function (d) { s.setProperty("--c-" + d, hex(v[d])); });
    $$("g[data-type]", svg).forEach(function (el) {
      if (el.getAttribute("data-type") === v.t) el.removeAttribute("display"); else el.setAttribute("display", "none");
    });
    svg.setAttribute("aria-label", "Getekende " + D.types[v.t].n.toLowerCase() + ": " + omschrijving(v));
  }
  function omschrijving(v) {
    return DELEN.map(function (d) { return DEELNAAM[d] + " " + kort(v[d]).toLowerCase(); }).join(", ");
  }

  var paneA = $('[data-pane="a"]'), paneB = null;
  function maakB() {
    if (paneB) return;
    var tmp = document.createElement("div");
    tmp.innerHTML = paneA.outerHTML.replace(/ga-/g, "gb-").replace('data-pane="a"', 'data-pane="b"').replace(">Variant A<", ">Variant B<");
    paneB = tmp.firstChild;
    paneB.classList.remove("on");
    $(".gk-panes").appendChild(paneB);
    paneB.addEventListener("click", klikPlaat);
    if (!reduce) setTimeout(function () { $("svg", paneB).classList.add("gk-anim"); }, 50);
  }

  /* ------------------------------------------------- paneel */
  function huidig() { return st.v[st.actief]; }

  function tekenPalet() {
    var v = huidig(), pal = D.palet[st.deel];
    $(".gk-palet").innerHTML = pal.map(function (id) {
      var k = K[id];
      var stijl = "--kl:" + k.h + (k.steen ? ";--kv:" + k.v : "");
      return '<button type="button" class="gk-kleur' + (k.steen ? " steen" : "") + '" data-kleur="' + id + '" style="' + stijl +
        '" aria-pressed="' + (v[st.deel] === id) + '" title="' + k.n + '"><i></i><span>' + kort(id) + "</span></button>";
    }).join("");
  }

  function tekenAdvies() {
    var t = D.types[huidig().t];
    var tekst = ADVIES[huidig().t] || "";
    $(".gk-advies").innerHTML = "<h3>Advies voor een " + t.n.toLowerCase() + "</h3><p>" + tekst + "</p>" +
      '<div class="gk-presets">' + t.presets.map(function (p, i) {
        var bol = [p[1], p[2], p[3], p[4]].map(function (id) { return '<i style="background:' + hex(id) + '"></i>'; }).join("");
        return '<button type="button" class="gk-preset" data-preset="' + i + '">' + bol + p[0] + "</button>";
      }).join("") + "</div>";
  }

  /* ------------------------------------------------- kleurcheck */
  function check(v) {
    var let_ = [], tip = [], t = v.t, zonnig = st.zon === "zuid" || st.zon === "west";
    var zijde = { noord: "noorden", oost: "oosten", zuid: "zuiden", west: "westen" }[st.zon];
    var gevelHex = hex(v.gevel), geverfd = !K[v.gevel].steen;

    /* 1. warmte */
    if (zonnig) {
      var houtDelen = (st.mat === "hout" ? ["kozijn", "raam", "deur"] : ["deur"]).concat(["boei"]);
      var heet = houtDelen.filter(function (d) { return donker(v[d]); });
      if (heet.length) let_.push("<b>Warmte:</b> " + opsom(heet.map(function (d) { return DEELNAAM[d]; })) +
        " krijgen een donkere kleur op hout dat op het " + zijde + " ligt. Donker hout wordt in de zon veel warmer. Het kan gaan werken en de verf kan blazen of scheuren. Vraag je schilder om verf voor donkere kleuren, of kies een lichtere tint. <a href=\"#warmte\">Meer uitleg</a>");
      if (st.mat === "kunststof" && (donker(v.kozijn) || donker(v.raam)))
        let_.push("<b>Kunststof in de zon:</b> een veel donkerdere kleur kan kunststof kozijnen op het " + zijde + " laten vervormen. Laat een schilder eerst kijken of het kan.");
      if (geverfd && donker(v.gevel)) tip.push("Een donker geschilderde gevel op het " + zijde + " warmt flink op. Kies verf die daarvoor geschikt is.");
    } else if (st.zon === "onbekend") {
      var donkerHout = (st.mat === "hout" ? ["kozijn", "raam", "deur", "boei"] : ["deur", "boei"]).filter(function (d) { return donker(v[d]); });
      if (donkerHout.length) tip.push("Ligt deze kant van je huis op het zuiden of westen? Dan worden de donkere " +
        opsom(donkerHout.map(function (d) { return DEELNAAM[d]; })) + " in de zon flink warm. Kies hierboven de kant voor een gerichte check.");
    }
    if (st.mat === "aluminium") tip.push("Aluminium kozijnen hebben een speciale hechtlaag nodig voordat ze geschilderd worden. Vraag je schilder ernaar.");

    /* 2. kozijn en gevel te gelijk */
    if (contrast(hex(v.kozijn), gevelHex) < 1.35)
      let_.push("<b>Weinig verschil:</b> kozijnen en gevel lijken veel op elkaar. De ramen vallen dan weg in de gevel. Kies een lichtere of donkerdere kozijnkleur.");
    else if (contrast(hex(v.deur), gevelHex) < 1.2)
      tip.push("De voordeur lijkt veel op de gevel en valt weinig op. Een deur in een eigen kleur geeft je huis een gezicht.");

    /* 3. te veel kleuren */
    var kleurDelen = ["kozijn", "raam", "deur", "boei"].concat(geverfd ? ["gevel"] : []);
    var kleuren = {};
    kleurDelen.forEach(function (d) { if (kleurig(hex(v[d]))) kleuren[v[d]] = 1; });
    var n = Object.keys(kleuren).length;
    if (n >= 3) let_.push("<b>Veel kleuren:</b> je gebruikt " + n + " verschillende kleuren. Dat wordt snel onrustig. Kies er hoogstens twee, naast wit, grijs of zwart.");

    /* 4. bijna dezelfde kleur */
    var paren = [["kozijn", "raam"], ["raam", "deur"], ["kozijn", "deur"], ["kozijn", "boei"]];
    for (var i = 0; i < paren.length; i++) {
      var a = v[paren[i][0]], b = v[paren[i][1]];
      if (a === b || !kleurig(hex(a)) || !kleurig(hex(b))) continue;
      var ha = hsl(hex(a)).h, hb = hsl(hex(b)).h, dh = Math.abs(ha - hb); dh = Math.min(dh, 360 - dh);
      if (dh >= 15 && dh <= 70) {
        let_.push("<b>Net niet hetzelfde:</b> " + kort(a).toLowerCase() + " (" + DEELNAAM[paren[i][0]] + ") en " + kort(b).toLowerCase() +
          " (" + DEELNAAM[paren[i][1]] + ") lijken op elkaar, maar zijn net anders. Dat oogt al snel als een vergissing. Kies dezelfde kleur, of twee kleuren die echt verschillen.");
        break;
      }
    }

    /* 5. goot en boeideel */
    if (v.goot !== "zink" && v.goot !== v.boei && contrast(hex(v.goot), hex(v.boei)) > 1.6)
      tip.push("Meestal krijgt de dakgoot dezelfde kleur als de boeidelen. Dan valt de goot minder op.");

    /* 6. per bouwstijl */
    var regel = D.types[t].regel;
    if (regel === "licht_kozijn" && lum(hex(v.kozijn)) < 0.35)
      let_.push("<b>Bouwstijl:</b> bij een jaren-30-huis zijn de kozijnen meestal licht, met kleur op de ramen en de deur. Met donkere kozijnen vallen details zoals de erker en het glas-in-lood weg.");
    if (regel === "traditioneel" && (lum(hex(v.kozijn)) < 0.35 || (geverfd && lum(gevelHex) < 0.3)))
      let_.push("<b>Oude kern:</b> bij herenhuizen in een oude binnenstad zijn kozijnen en kroonlijst meestal crème of gebroken wit. Staat je huis in een beschermd stads- of dorpsgezicht, of is het een monument? Kijk dan eerst wat de gemeente toestaat.");
    if (regel === "boei_licht" && lum(hex(v.boei)) > 0.6)
      tip.push("Brede boeidelen in een lichte kleur vallen sterk op. In een donkere kleur oogt het dak rustiger.");
    if (geverfd && t !== "heren" && t !== "vrij")
      tip.push("Een bakstenen gevel schilderen is een grote stap: daarna moet hij om de zoveel jaar opnieuw, en terug naar kale steen is lastig. Laat eerst een schilder kijken of de steen geschikt is.");

    return { let_: let_, tip: tip };
  }

  function tekenCheck() {
    var r = check(huidig()), el = $(".gk-check");
    el.classList.toggle("let", r.let_.length > 0);
    var kop = r.let_.length ? (r.let_.length === 1 ? "Kleurcheck: één punt om op te letten" : "Kleurcheck: " + r.let_.length + " punten om op te letten")
      : "Kleurcheck: deze combinatie past goed";
    if (st.cmp) kop += " (variant " + st.actief.toUpperCase() + ")";
    var items = r.let_.map(function (x) { return "<li>" + x + "</li>"; })
      .concat(r.tip.map(function (x) { return '<li class="tip">' + x + "</li>"; }));
    if (!items.length) items.push('<li class="tip">Geen botsende kleuren gevonden. Bekijk de kleuren nog wel op een echt staal, buiten in het daglicht.</li>');
    el.innerHTML = "<h3>" + kop + "</h3><ul>" + items.join("") + "</ul>";
  }

  /* ------------------------------------------------- alles bijwerken */
  function teken() {
    var v = huidig();
    kleurSvg($("svg", paneA), st.v.a);
    if (paneB && st.v.b) kleurSvg($("svg", paneB), st.v.b);
    root.setAttribute("data-cmp", st.cmp ? "1" : "0");
    if (paneB) paneB.hidden = !st.cmp;
    paneA.classList.toggle("on", st.actief === "a");
    if (paneB) paneB.classList.toggle("on", st.actief === "b");
    $(".gk-tabs").hidden = !st.cmp;
    $$(".gk-tab").forEach(function (b) { var on = b.getAttribute("data-var") === st.actief; b.classList.toggle("on", on); b.setAttribute("aria-pressed", on); });
    $$(".gk-type").forEach(function (b) { var on = b.getAttribute("data-type") === v.t; b.classList.toggle("on", on); b.setAttribute("aria-pressed", on); });
    $$(".gk-deel").forEach(function (b) {
      var d = b.getAttribute("data-deel"), on = d === st.deel;
      b.classList.toggle("on", on); b.setAttribute("aria-pressed", on);
      b.querySelector(".gk-stip").style.setProperty("--kl", hex(v[d]));
      b.querySelector("[data-naam]").textContent = kort(v[d]);
    });
    $$("[data-uitleg]").forEach(function (p) { p.hidden = p.getAttribute("data-uitleg") !== st.deel; });
    $("[data-actief]").textContent = "voor de " + DEELNAAM[st.deel];
    var vk = $("[data-vergelijk]");
    vk.setAttribute("aria-pressed", st.cmp); vk.textContent = st.cmp ? "Stop vergelijken" : "Vergelijk";
    tekenPalet(); tekenAdvies(); tekenCheck(); schrijfHash();
  }

  /* ------------------------------------------------- hash */
  function geldig(d, id) { return D.palet[d].indexOf(id) >= 0; }
  function code(v) { return [v.t].concat(DELEN.map(function (d) { return v[d]; })).join(","); }
  function leesCode(s) {
    var p = (s || "").split(",");
    if (p.length !== 7 || !D.types[p[0]]) return null;
    var v = { t: p[0] };
    for (var i = 0; i < DELEN.length; i++) { if (!geldig(DELEN[i], p[i + 1])) return null; v[DELEN[i]] = p[i + 1]; }
    return v;
  }
  function link() { return location.href.split("#")[0] + "#" + hashTekst(); }
  function hashTekst() {
    return "a=" + code(st.v.a) + (st.cmp && st.v.b ? "&b=" + code(st.v.b) : "") + "&zon=" + st.zon + "&mat=" + st.mat;
  }
  function schrijfHash() { if (history.replaceState) history.replaceState(null, "", "#" + hashTekst()); }
  function leesHash() {
    var h = location.hash.replace(/^#/, ""); if (h.indexOf("a=") < 0) return;
    var q = {}; h.split("&").forEach(function (x) { var kv = x.split("="); q[kv[0]] = decodeURIComponent(kv[1] || ""); });
    var a = leesCode(q.a), b = leesCode(q.b);
    if (a) st.v.a = a;
    if (b) { st.v.b = b; st.cmp = true; maakB(); }
    if (/^(onbekend|noord|oost|zuid|west)$/.test(q.zon)) st.zon = q.zon;
    if (/^(hout|kunststof|aluminium)$/.test(q.mat)) st.mat = q.mat;
    $("#gk-zon", document).value = st.zon; $("#gk-mat", document).value = st.mat;
  }

  /* ------------------------------------------------- klikken */
  function klikPlaat(e) {
    var pane = e.currentTarget, v = pane.getAttribute("data-pane");
    if (st.cmp && v !== st.actief) st.actief = v;
    var el = e.target;
    while (el && el !== pane) {
      var c = (el.getAttribute && el.getAttribute("class")) || "";
      var d = KLASSE[c.split(" ")[0]];
      if (d) { st.deel = d; break; }
      el = el.parentNode;
    }
    teken();
  }
  paneA.addEventListener("click", klikPlaat);

  root.addEventListener("click", function (e) {
    var b = e.target.closest("button"); if (!b || !root.contains(b)) return;
    var v = huidig();
    if (b.hasAttribute("data-type")) {
      var nt = b.getAttribute("data-type");
      if (nt !== v.t) { st.v[st.actief] = variantUit(nt, D.types[nt].presets[0]); }
    } else if (b.hasAttribute("data-deel")) st.deel = b.getAttribute("data-deel");
    else if (b.hasAttribute("data-kleur")) v[st.deel] = b.getAttribute("data-kleur");
    else if (b.hasAttribute("data-preset")) st.v[st.actief] = variantUit(v.t, D.types[v.t].presets[+b.getAttribute("data-preset")]);
    else if (b.hasAttribute("data-var")) st.actief = b.getAttribute("data-var");
    else if (b.hasAttribute("data-vergelijk")) {
      st.cmp = !st.cmp;
      if (st.cmp) {
        maakB();
        if (!st.v.b) {
          /* begin variant B met de tweede voorbeeldcombinatie van hetzelfde huis */
          st.v.b = variantUit(st.v.a.t, D.types[st.v.a.t].presets[1]);
        }
        st.actief = "b";
        zeg("Variant B staat naast A. Pas B aan, of tik op A om die te wijzigen.");
      } else { st.actief = "a"; zeg(""); }
    } else if (b.hasAttribute("data-png")) { maakPlaatje(function (c) { TSDeel.opslaan(c, bestand()); zeg("Je plaatje wordt gedownload."); }); return; }
    else if (b.hasAttribute("data-link")) { kopieer(); return; }
    else return;
    teken();
  });
  var deelKnop = $("[data-delen]");
  if (window.File && navigator.canShare) {
    try { if (navigator.canShare({ files: [new File([""], "x.png", { type: "image/png" })] })) deelKnop.hidden = false; } catch (err) {}
  }
  deelKnop.addEventListener("click", function () {
    maakPlaatje(function (c) { TSDeel.delen(c, bestand(), "Mijn huis in een nieuwe kleur", "Wat vind jij van deze kleuren?", link()); });
  });
  $("#gk-zon", document).addEventListener("change", function (e) { st.zon = e.target.value; teken(); });
  $("#gk-mat", document).addEventListener("change", function (e) { st.mat = e.target.value; teken(); });

  function zeg(t) { $(".gk-melding").textContent = t; }
  function bestand() { return "gevelkleur-" + st.v.a.t + (st.cmp ? "-vergelijk" : "") + ".png"; }
  function kopieer() {
    var l = link();
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(l).then(function () { zeg("Link gekopieerd. Plak hem in een bericht of in je offerteaanvraag."); }, function () { zeg(l); });
    else zeg(l);
  }

  /* ------------------------------------------------- plaatje (PNG) */
  function svgNaarImg(svg, klaar) {
    var kloon = svg.cloneNode(true);
    kloon.setAttribute("width", "1280"); kloon.setAttribute("height", "880");
    kloon.setAttribute("style", svg.getAttribute("style") || "");
    kloon.classList.remove("gk-anim");
    var bron = new XMLSerializer().serializeToString(kloon);
    var img = new Image();
    img.onload = function () { klaar(img); };
    img.onerror = function () { klaar(null); };
    img.src = "data:image/svg+xml;charset=utf-8," + encodeURIComponent(bron);
  }
  function maakPlaatje(klaar) {
    if (!window.TSDeel) { zeg("Het plaatje lukt niet in deze browser. Maak anders een schermafbeelding."); return; }
    var lijst = st.cmp && paneB ? [["a", paneA], ["b", paneB]] : [["a", paneA]];
    var imgs = [], wacht = lijst.length, mis = false;
    lijst.forEach(function (x, i) {
      svgNaarImg($("svg", x[1]), function (img) {
        imgs[i] = img; if (!img) mis = true;
        if (--wacht) return;
        if (mis) { zeg("Het plaatje lukt niet in deze browser. Maak anders een schermafbeelding."); return; }
        klaar(TSDeel.kaart(function (ctx, k, FONT) { tekenKaart(ctx, k, FONT, lijst, imgs); }, "Je huis in een nieuwe kleur"));
      });
    });
  }
  function legenda(ctx, v, x, y, b, FONT, kolommen, regelH) {
    ctx.textBaseline = "middle";
    DELEN.forEach(function (d, i) {
      var kol = i % kolommen, rij = Math.floor(i / kolommen), kx = x + kol * (b / kolommen), ky = y + rij * regelH;
      ctx.beginPath(); ctx.arc(kx + 9, ky, 9, 0, Math.PI * 2); ctx.fillStyle = hex(v[d]); ctx.fill();
      ctx.lineWidth = 1; ctx.strokeStyle = "rgba(0,0,0,.25)"; ctx.stroke();
      ctx.fillStyle = "#3c290f"; ctx.font = "600 " + (kolommen > 1 ? 15 : 20) + "px " + FONT;
      var label = DEELNAAM[d].charAt(0).toUpperCase() + DEELNAAM[d].slice(1) + ": ";
      ctx.fillText(label, kx + 26, ky);
      var lw = ctx.measureText(label).width;
      ctx.font = "400 " + (kolommen > 1 ? 15 : 20) + "px " + FONT;
      ctx.fillText(kort(v[d]).toLowerCase(), kx + 26 + lw, ky);
    });
  }
  function tekenKaart(ctx, k, FONT, lijst, imgs) {
    var B = TSDeel.B, H = TSDeel.H;
    /* eigen voetregel over die van de standaardkaart heen */
    ctx.fillStyle = "#faf7f1"; ctx.fillRect(0, H - 60, B, 60);
    ctx.fillStyle = "#6f6047"; ctx.font = "500 18px " + FONT; ctx.textBaseline = "alphabetic";
    ctx.fillText("Kleuren op een scherm wijken af van echte verf. Maak je eigen ontwerp op topschilder.nl/tools/gevelkleur/", 48, H - 26);
    if (lijst.length === 1) {
      var v = st.v.a, ih = k.h, iw = ih * 640 / 440;
      ctx.save(); TSDeel.rondRect(ctx, k.x, k.y, iw, ih, 14); ctx.clip(); ctx.drawImage(imgs[0], k.x, k.y, iw, ih); ctx.restore();
      var lx = k.x + iw + 36;
      ctx.fillStyle = "#3c290f"; ctx.font = "800 28px " + FONT; ctx.textBaseline = "alphabetic";
      ctx.fillText(D.types[v.t].n, lx, k.y + 34);
      legenda(ctx, v, lx, k.y + 84, B - 48 - lx, FONT, 1, 50);
    } else {
      var gap = 24, w = (k.b - gap) / 2, h2 = w * 440 / 640;
      lijst.forEach(function (x, i) {
        var vx = k.x + i * (w + gap), v2 = st.v[x[0]];
        ctx.save(); TSDeel.rondRect(ctx, vx, k.y, w, h2, 12); ctx.clip(); ctx.drawImage(imgs[i], vx, k.y, w, h2); ctx.restore();
        ctx.fillStyle = "rgba(255,255,255,.92)"; TSDeel.rondRect(ctx, vx + 10, k.y + 10, 108, 30, 15); ctx.fill();
        ctx.fillStyle = "#3c290f"; ctx.font = "700 16px " + FONT; ctx.textBaseline = "middle";
        ctx.fillText("Variant " + x[0].toUpperCase(), vx + 22, k.y + 25);
        legenda(ctx, v2, vx, k.y + h2 + 18, w, FONT, 2, 22);
      });
    }
  }

  /* ------------------------------------------------- naar het formulier */
  $("[data-offerte]").addEventListener("click", function (e) {
    var form = document.querySelector("form[data-wizard]");
    if (!form) return;
    e.preventDefault();
    var oms = form.querySelector("textarea[name=omschrijving]");
    var v = st.v[st.actief];
    if (oms) {
      var regel = "Kleurwens (" + D.types[v.t].n.toLowerCase() + "): " + omschrijving(v) + ". Ontwerp: " + link();
      var oud = oms.value.replace(/^Kleurwens .*$/m, "").trim();
      oms.value = regel + (oud ? "\n" + oud : "");
    }
    var dienst = [].slice.call(form.querySelectorAll("input[name=dienst]")).filter(function (i) { return i.value === "Buitenschilderwerk"; })[0];
    if (dienst && !dienst.checked) dienst.click();
    var box = document.getElementById("offerte");
    if (box) window.scrollTo({ top: box.getBoundingClientRect().top + window.scrollY - 90, behavior: reduce ? "auto" : "smooth" });
    zeg("Je kleuren staan in het formulier.");
  });

  /* voorbeeldlinks verderop op de pagina: hash lezen zonder herladen */
  window.addEventListener("hashchange", function () { leesHash(); teken(); });
  [].slice.call(document.querySelectorAll("[data-preset-link]")).forEach(function (a) {
    a.addEventListener("click", function () {
      setTimeout(function () { root.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "start" }); }, 0);
    });
  });

  var ADVIES = __ADVIES__;
  leesHash();
  teken();
  if (!reduce) setTimeout(function () { $("svg", paneA).classList.add("gk-anim"); }, 50);
})();
"""
