# -*- coding: utf-8 -*-
"""
Kleurenkiezer voor gevel en kozijnen (/kleuren-kiezen/).

Alles van deze tool staat in dit ene bestand: de kleuren, de getekende woningen
(inline SVG), de pagina, de CSS en de JavaScript. build.py roept alleen
build_kleurenkiezer() aan en zet op een paar pagina's kleuren_teaser() neer.

Kleuren hebben een echte RAL Classic- of NCS-code waar die bestaat. Namen volgen
ralkleuren.com; de hexwaarden komen uit de RAL-lijst op Wikipedia (sRGB-benadering)
en zijn alleen bedoeld voor het scherm. Traditionele namen zonder vaste code
(grachtengroen, eikenhout-look) staan er eerlijk zonder code bij.
"""

import json
import os

from data import PLAATSEN, WONINGEN
from components import page, crumbs, offerte_form, faq_blok, title

PAD = "/kleuren-kiezen/"

# ---------------------------------------------------------------------------
# Kleuren
# ---------------------------------------------------------------------------

DELEN_NAAM = {"kozijn": "kozijnen", "raam": "ramen", "deur": "voordeur", "boei": "boeidelen",
              "gevel": "geschilderde gevel"}

# id, naam, groep, ral, ncs, hex, delen, uitleg. Een id blijft altijd geldig (deellinks);
# vervalt er een, zet hem dan in KLEUR_ALIAS.
KLEUREN = [
    # --- Wit en crème
    dict(id="cremewit", naam="Crèmewit", groep="Wit en crème", ral="9001", hex="#EFEBDC",
         delen="kozijn raam boei gevel",
         uitleg="Een warm wit met een vleugje geel. Minder fel dan zuiver wit, en daardoor rustig bij rode "
                "en bruine baksteen en bij oudere woningen."),
    dict(id="wit", naam="Zuiver wit", groep="Wit en crème", ral="9010", hex="#F7F9EF",
         delen="kozijn raam boei gevel",
         uitleg="Een helder wit dat net iets zachter is dan verkeerswit. Veel gekozen voor houten kozijnen, "
                "ramen en boeidelen."),
    dict(id="verkeerswit", naam="Verkeerswit", groep="Wit en crème", ral="9016", hex="#F7FBF5",
         delen="kozijn raam boei",
         uitleg="Het koelste en witste wit van de drie. Kunststof kozijnen zijn vaak in deze kleur te krijgen, "
                "dus kies hem als je houtwerk daarbij moet aansluiten."),
    dict(id="gebroken-wit", naam="Gebroken wit (grijswit)", groep="Wit en crème", ral="9002", hex="#DDDED4",
         delen="kozijn raam boei gevel",
         uitleg="Gebroken wit is geen vaste kleur: meestal bedoelt men wit met een tikje grijs of geel. "
                "RAL 9002 is de grijze variant; zoek je de gele, kies dan crèmewit."),
    dict(id="licht-ivoor", naam="Licht ivoor", groep="Wit en crème", ral="1015", hex="#E6D2B5",
         delen="kozijn boei gevel",
         uitleg="Een zachte zandkleur, warmer dan crèmewit (officieel: licht ivoorkleurig). Past bij gele en "
                "lichte baksteen en bij landelijke woningen."),
    # --- Grijs en zwart
    dict(id="lichtgrijs", naam="Lichtgrijs", groep="Grijs en zwart", ral="7035", hex="#CBD0CC",
         delen="kozijn raam boei gevel",
         uitleg="Een licht, koel grijs. Rustiger dan wit, en kleine vlekjes vallen er minder op."),
    dict(id="steengrijs", naam="Steengrijs", groep="Grijs en zwart", ral="7030", hex="#939388",
         delen="kozijn raam boei",
         uitleg="Een middengrijs met een warme ondertoon. Een tussenweg voor wie wit te fel en antraciet "
                "te zwaar vindt."),
    dict(id="kwartsgrijs", naam="Kwartsgrijs", groep="Grijs en zwart", ral="7039", hex="#6B695F",
         delen="kozijn raam deur boei",
         uitleg="Een donker grijs met een bruine zweem. Oogt zachter dan antraciet en past goed bij "
                "baksteen in aardetinten."),
    dict(id="antraciet", naam="Antracietgrijs", groep="Grijs en zwart", ral="7016", hex="#373F43",
         delen="kozijn raam deur boei",
         uitleg="Het bekende donkergrijs van moderne kozijnen en dakkapellen. Strak bij een lichte gevel; "
                "op hout in de zon wordt het wel flink warm."),
    dict(id="zwartgrijs", naam="Zwartgrijs", groep="Grijs en zwart", ral="7021", hex="#2E3234",
         delen="kozijn raam deur boei",
         uitleg="Een bijna-zwart grijs. Net iets zachter dan echt zwart en daardoor makkelijker te "
                "combineren met steen en hout."),
    dict(id="zwart", naam="Gitzwart", groep="Grijs en zwart", ral="9005", hex="#0A0A0D",
         delen="deur kozijn raam",
         uitleg="Diep zwart. Mooi op een voordeur en in strakke nieuwbouw. Op grote houten vlakken in de "
                "zon vraagt het om verf die voor donkere kleuren geschikt is."),
    # --- Groen
    dict(id="grachtengroen", naam="Grachtengroen", groep="Groen", ral="", hex="#2B3A31",
         delen="raam deur",
         uitleg="Traditionele naam voor het diepe donkergroen op ramen en deuren in oude binnensteden, ook "
                "wel monumentengroen. Er is geen officiële RAL- of NCS-code: elk verfmerk mengt een eigen "
                "versie, dus kies op een echte kleurstaal."),
    dict(id="dennengroen", naam="Dennengroen", groep="Groen", ral="6009", hex="#26392F",
         delen="raam deur kozijn boei",
         uitleg="Een diep, iets blauwig donkergroen met een vaste RAL-code. Handig als je klassiek groen "
                "zoekt dat elke verfleverancier precies kan namengen."),
    dict(id="zwartgroen", naam="Zwartgroen", groep="Groen", ral="6012", hex="#31403D",
         delen="raam deur kozijn",
         uitleg="Van een afstand lijkt het bijna zwart, van dichtbij zie je het groen. Rustig op ramen en "
                "deuren in rode of bruine steen."),
    dict(id="mosgroen", naam="Mosgroen", groep="Groen", ral="6005", hex="#0F4336",
         delen="deur raam",
         uitleg="Een vol, diep groen met meer kleur dan dennengroen. Valt op als voordeur."),
    dict(id="olijfgroen", naam="Olijfgroen", groep="Groen", ral="6003", hex="#4B573E",
         delen="raam deur boei",
         uitleg="Een gedekt groen met een gele ondertoon. Past bij landelijke woningen en bij hout en riet."),
    dict(id="bleekgroen", naam="Bleekgroen", groep="Groen", ral="6021", hex="#86A47C",
         delen="deur raam",
         uitleg="Een zacht lichtgroen in de richting van salie. Fris op een voordeur of op luiken."),
    # --- Blauw en rood
    dict(id="staalblauw", naam="Staalblauw", groep="Blauw en rood", ral="5011", hex="#232C3F",
         delen="deur raam kozijn",
         uitleg="Zo donker blauw dat het van een afstand bijna zwart oogt. Klassiek op een voordeur, en "
                "mooi bij crèmewitte of witte kozijnen."),
    dict(id="duifblauw", naam="Duifblauw", groep="Blauw en rood", ral="5014", hex="#6C7C98",
         delen="deur raam",
         uitleg="Een grijsachtig middenblauw. Zachter dan staalblauw en fris bij witte kozijnen."),
    dict(id="bruinrood", naam="Bruinrood", groep="Blauw en rood", ral="3011", hex="#7E292C",
         delen="deur raam",
         uitleg="Een donker roodbruin uit de kleurfamilie die traditioneel ossenbloed heet, naar het rode "
                "pigment van ijzeroxide. Klassiek op deuren en ramen van oudere woningen."),
    dict(id="wijnrood", naam="Wijnrood", groep="Blauw en rood", ral="3005", hex="#5E2028",
         delen="deur",
         uitleg="Een diep donkerrood met een paarse zweem. Chic op een voordeur, vooral bij lichte kozijnen."),
    dict(id="falurood", naam="Falu-rood (Zweeds rood)", groep="Blauw en rood", ral="", ncs="S 5040-Y80R",
         hex="#7B352C", delen="gevel boei deur",
         uitleg="Het roestrood van Zweedse houten huizen. In Nederland vooral te zien op houten "
                "bijgebouwen, schuren en gepotdekselde gevels."),
    # --- Geel en bruin
    dict(id="zandgeel", naam="Zandgeel", groep="Geel en bruin", ral="1002", hex="#D2AA6D",
         delen="kozijn boei deur",
         uitleg="Een zachte okergele tint. Voor de traditionele kleur Bentheimer geel (naar de gele "
                "zandsteen) bestaat geen vaste RAL-code; zoek je die, vraag dan een staal."),
    dict(id="okerbruin", naam="Okerbruin", groep="Geel en bruin", ral="8001", hex="#9C6B30",
         delen="kozijn deur",
         uitleg="Een warm goudbruin in de richting van licht hout, maar dan dekkend: de nerf zie je niet."),
    dict(id="eiken", naam="Eikenhout-look", groep="Geel en bruin", ral="", code="houtnerf, geen RAL",
         hex="#B88A53", delen="kozijn raam deur", hout=True,
         uitleg="Geen verfkleur maar een uitstraling: op hout met transparante beits, bij kunststof "
                "kozijnen met houtnerffolie. De kleur op het scherm is alleen een indruk."),
    dict(id="noten", naam="Notenbruin", groep="Geel en bruin", ral="8011", hex="#5A3A29",
         delen="kozijn raam deur", hout=True,
         uitleg="Een middenbruin zoals donker gebeitst hout, maar dekkend. Past bij landelijke woningen "
                "en jaren-30-huizen."),
    dict(id="mahonie", naam="Mahoniebruin", groep="Geel en bruin", ral="8016", hex="#4C2F26",
         delen="deur kozijn", hout=True,
         uitleg="Een diep roodbruin dat lijkt op donker hardhout."),
]
for _k in KLEUREN:
    _k.setdefault("ncs", "")
    _k.setdefault("hout", False)
    if "code" not in _k:
        _k["code"] = ("RAL " + _k["ral"]) if _k["ral"] else (("NCS " + _k["ncs"]) if _k["ncs"] else "geen vaste code")
    _k["delen"] = _k["delen"].split()

KLEUR_BY_ID = {k["id"]: k for k in KLEUREN}

# Oude kleur-id's uit gedeelde links en uit inspiratie.py -> de echte kleur die ervoor in de plaats kwam.
KLEUR_ALIAS = {
    "zandbeige": "licht-ivoor",
    "gooiers-groen": "dennengroen",
    "monumentengroen": "grachtengroen",
    "salie": "bleekgroen",
    "nachtblauw": "staalblauw",
    "ossenbloed": "bruinrood",
    "zweeds-rood": "falurood",
    "bentheimer": "zandgeel",
}

# (id, naam, hex, groep) — de oude vorm, die inspiratie.py nog gebruikt. De aliassen staan er ook in
# (groep "_alias"), zodat oude id's daar blijven werken; het palet zelf leest KLEUREN.
VERFKLEUREN = ([(k["id"], k["naam"], k["hex"], k["groep"]) for k in KLEUREN]
               + [(oud, KLEUR_BY_ID[nieuw]["naam"], KLEUR_BY_ID[nieuw]["hex"], "_alias")
                  for oud, nieuw in KLEUR_ALIAS.items()])

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
    ("boei", "Boeidelen", "De planken langs de dakrand, de dakkapel en de kroonlijst."),
    ("gevel", "Gevelsteen", "Kleur van de muur. Meestal blijft die zoals hij is."),
]

TYPES = [
    ("rij", "Rijtjeshuis"),
    ("twee", "Twee-onder-een-kap"),
    ("dertig", "Jaren-30-woning"),
    ("vrij", "Vrijstaande woning"),
    ("heren", "Herenhuis in een oude kern"),
]
TYPE_KORT = {"rij": "Rijtjeshuis", "twee": "2-onder-1-kap", "dertig": "Jaren 30", "vrij": "Vrijstaand",
             "heren": "Herenhuis"}

STIJLEN = [
    # (id, naam, kozijn, raam, deur, boei, gevel, type, waarom)
    ("klassiek-gooi", "Klassiek groen", "cremewit", "dennengroen", "dennengroen", "cremewit", "rood", "twee",
     "Crèmewit houtwerk met donkergroene ramen en deur: het beeld van veel vooroorlogse woningen. "
     "Werkt op rode en bruine steen."),
    ("jaren-30", "Jaren 30", "cremewit", "bruinrood", "grachtengroen", "cremewit", "bruin", "dertig",
     "Crème kozijnen, roodbruine ramen en een groene deur passen bij donkere steen en rode pannen."),
    ("oude-kern", "Oude binnenstad", "cremewit", "grachtengroen", "grachtengroen", "cremewit", "rood", "heren",
     "Het klassieke beeld in een historische kern. Woon je in een monument of beschermd stadsgezicht, "
     "check dan eerst de regels."),
    ("modern-antraciet", "Modern antraciet", "antraciet", "antraciet", "zwart", "antraciet", "wit", "vrij",
     "Alles donker op een lichte gevel: strak en eigentijds. Kies verf die geschikt is voor donkere kleuren."),
    ("warm-grijs", "Warm grijs", "kwartsgrijs", "kwartsgrijs", "bruinrood", "kwartsgrijs", "rood", "rij",
     "Een zachter alternatief voor antraciet. De roodbruine deur pakt de kleur van de steen op."),
    ("fris-wit", "Wit met zwarte deur", "verkeerswit", "verkeerswit", "zwart", "verkeerswit", "bruin", "rij",
     "Wit kozijn en raam in één kleur oogt rustig; een zwarte voordeur geeft houvast."),
    ("rustig-blauw", "Rustig blauw", "wit", "duifblauw", "staalblauw", "wit", "rood", "dertig",
     "Twee blauwen bij wit houtwerk: fris, en het rood van de steen komt mooi uit."),
    ("warm-landelijk", "Warm landelijk", "licht-ivoor", "olijfgroen", "falurood", "licht-ivoor", "geel", "vrij",
     "Zandkleurig houtwerk met olijfgroen en een rode deur: warm bij gele steen of hout."),
    ("natuurlijk-hout", "Natuurlijk hout", "eiken", "eiken", "noten", "antraciet", "antraciet", "twee",
     "Houtlook voor kozijnen en deur met antraciet boeidelen: modern en toch warm."),
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
# De woningen
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



def _vrijstaand():
    o = []
    # schoorsteen achter het dak
    o.append(_r(402, 58, 26, 54, "ks"))
    o.append(_r(398, 54, 34, 7, extra='fill="#55585b"'))
    # woning met schilddak
    o.append(_r(140, 222, 360, 178, "ks"))
    o.append('<polygon points="116,226 524,226 432,92 208,92" fill="url(#kk-dak-rood)"/>')
    o.append(_r(208, 86, 224, 9, extra='fill="#5a2c20"'))
    # dakkapel
    o.append(_r(262, 128, 116, 66, extra='fill="#3a2a22"'))
    o.append(_r(262, 134, 8, 58, "kb", LIJN))
    o.append(_r(370, 134, 8, 58, "kb", LIJN))
    o.append(raam(270, 134, 100, 58, "dd", dorpel=False))
    o.append(_r(256, 190, 128, 7, extra='fill="#6d6f70"'))
    o.append(boei(256, 122, 128, 12))
    o.append(boei(110, 218, 420, 14))
    # ramen links en rechts, voordeur met luifel in het midden
    o.append(raam(160, 258, 114, 104, "vv", boven="dd", bh=24))
    o.append(raam(366, 258, 114, 104, "vv", boven="dd", bh=24))
    o.append(boei(280, 262, 80, 9))
    o.append(_r(280, 271, 80, 4, extra='fill="#000" opacity=".15"'))
    o.append(deur(290, 276, 60, 124, "paneel", bovenlicht=20))
    # tuin
    o.append('<rect x="132" y="386" width="148" height="16" rx="8" fill="#6f8f4e"/>')
    o.append('<rect x="360" y="386" width="148" height="16" rx="8" fill="#6f8f4e"/>')
    o.append(_r(44, 300, 9, 100, extra='fill="#6b5338"'))
    o.append('<circle cx="48" cy="280" r="34" fill="#7c9a58"/><circle cx="30" cy="300" r="22" fill="#6f8f4e"/>')
    o.append(_r(590, 314, 8, 86, extra='fill="#6b5338"'))
    o.append('<circle cx="594" cy="296" r="28" fill="#6f8f4e"/>')
    return "".join(o)


def _herenhuis():
    o = []
    # buren, vaag, zodat het midden opvalt
    o.append(_r(0, 128, 196, 272, extra='fill="#e6dccb"'))
    o.append(_r(444, 84, 196, 316, extra='fill="#c9b79b"'))
    for bx, top in ((30, 156), (112, 156), (470, 116), (556, 116)):
        for vy in (top, top + 112):
            o.append(_r(bx, vy, 54, 84, extra='fill="#f1efe9"'))
            o.append(_r(bx + 6, vy + 6, 42, 72, extra='fill="url(#kk-glas)"'))
    # dak achter de kroonlijst
    o.append('<polygon points="204,70 436,70 404,34 236,34" fill="url(#kk-dak-grijs)"/>')
    # lijstgevel
    o.append(_r(196, 94, 248, 306, "ks"))
    o.append(_r(186, 68, 268, 24, "kb", LIJN))
    o.append(_r(182, 62, 276, 8, "kb", LIJN))
    for kx in range(198, 440, 22):
        o.append(_r(kx, 92, 8, 8, "kb", LIJN))
    o.append(_r(186, 100, 268, 3, extra='fill="#000" opacity=".14"'))
    # twee verdiepingen met hoge ramen en een bovenlicht
    for wx in (216, 292, 368):
        for wy, wh in ((116, 80), (214, 86)):
            o.append(_r(wx - 4, wy - 7, 64, 6, extra='fill="#000" opacity=".14"'))
            o.append(raam(wx, wy, 56, wh, "d", boven="v", bh=18, f=6))
    # begane grond
    o.append(_r(196, 306, 248, 4, extra='fill="#000" opacity=".12"'))
    o.append(deur(290, 312, 60, 88, "paneel", bovenlicht=18))
    o.append(raam(214, 318, 60, 64, "d", boven="v", bh=14, f=6))
    o.append(raam(366, 318, 60, 64, "d", boven="v", bh=14, f=6))
    o.append(_r(0, 50, 196, 350, extra='fill="#fbf8f2" opacity=".5"'))
    o.append(_r(444, 50, 196, 350, extra='fill="#fbf8f2" opacity=".5"'))
    return "".join(o)


HUIZEN = (("rij", _rijtjeshuis), ("twee", _twee_onder_een_kap), ("dertig", _jaren30),
          ("vrij", _vrijstaand), ("heren", _herenhuis))

def svg_woning():
    """Eén SVG met alle woningtypes; JavaScript toont er één."""
    steen = STENEN[0]
    k = dict((x[0], x[2]) for x in VERFKLEUREN)
    stijl = (f"--c-kozijn:{k['cremewit']};--c-raam:{k['dennengroen']};--c-deur:{k['dennengroen']};"
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
        for t, fn in HUIZEN)
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
        for c in ("cremewit", "dennengroen", "antraciet", "zandgeel", "bruinrood", "eiken"))
    return (TEASER_CSS + f'<div class="kk-teaser"><div class="kk-teaser-bol" aria-hidden="true">{bolletjes}</div>'
            f'<div><h3>{kop}</h3><p>Probeer kozijnen, ramen, voordeur en boeidelen in {len(KLEUREN)} gangbare kleuren '
            f'met RAL-code, op een getekende woning. Je ontwerp deel je met één link.</p>'
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
        f'{TYPE_KORT[t]}</button>'
        for i, (t, n) in enumerate(TYPES))
    onderdelen = "".join(
        f'<button type="button" class="kk-deel{" on" if i == 0 else ""}" data-deel="{s}" '
        f'aria-pressed="{"true" if i == 0 else "false"}"><i class="kk-stip"></i>'
        f'<span><strong>{lab}</strong><small data-naam></small></span></button>'
        for i, (s, lab, _u) in enumerate(ONDERDELEN))
    groepen = []
    for g in dict.fromkeys(k["groep"] for k in KLEUREN):
        knoppen = "".join(
            f'<button type="button" class="kk-kleur" data-kleur="{k["id"]}" style="--kl:{k["hex"]}" '
            f'aria-label="{k["naam"]}, {k["code"]}" title="{k["naam"]} · {k["code"]}"><i></i>'
            f'<span>{k["naam"]}</span></button>'
            for k in KLEUREN if k["groep"] == g)
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
    <div class="kk-kleurinfo" data-kleurinfo><i class="kk-stip"></i><div><p class="kk-ki-kop"><strong data-ki-naam></strong> <span class="kk-code" data-ki-code></span></p><p data-ki-uitleg></p><p class="kk-ki-delen" data-ki-delen></p></div></div>
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


def stijl_link(st):
    """Deellink voor een stijltuple uit STIJLEN."""
    return (f"{PAD}#type={st[7]}&kozijn={st[2]}&raam={st[3]}&deur={st[4]}&boei={st[5]}&gevel={st[6]}")


def _combinaties_html():
    steen = {x[0]: x for x in STENEN}
    kaarten = []
    for st in STIJLEN:
        bol = "".join(
            f'<i style="background:{KLEUR_BY_ID[c]["hex"]}" title="{DELEN_NAAM[d].capitalize()}: '
            f'{KLEUR_BY_ID[c]["naam"]}"></i>'
            for d, c in zip(("kozijn", "raam", "deur", "boei"), st[2:6]))
        bol += f'<i class="kk-cb-steen" style="background:{steen[st[6]][2]}" title="{steen[st[6]][1]}"></i>'
        codes = " · ".join(
            f'{DELEN_NAAM[d]}: {KLEUR_BY_ID[c]["naam"].split(" (")[0].lower()} ({KLEUR_BY_ID[c]["code"]})'
            for d, c in zip(("kozijn", "raam", "deur"), st[2:5]))
        kaarten.append(
            f'<article class="kk-combi"><div class="kk-cb-bol" aria-hidden="true">{bol}</div>'
            f'<h3>{st[1]}</h3><p>{st[8]}</p><p class="kk-cb-codes">{codes}</p>'
            f'<a class="kk-cb-link" href="{stijl_link(st)}" data-combo>Bekijk op een '
            f'{dict(TYPES)[st[7]].lower()}</a></article>')
    return "".join(kaarten)


def _codes_html():
    rijen = []
    for g in dict.fromkeys(k["groep"] for k in KLEUREN):
        items = "".join(
            f'<li><i style="background:{k["hex"]}" aria-hidden="true"></i><div><strong>{k["naam"]}</strong> '
            f'<span class="kk-code">{k["code"]}</span><p>{k["uitleg"]}</p>'
            f'<small>Vaak voor: {", ".join(DELEN_NAAM[d] for d in k["delen"])}</small></div></li>'
            for k in KLEUREN if k["groep"] == g)
        rijen.append(f'<h3>{g}</h3><ul class="kk-codes">{items}</ul>')
    return "".join(rijen)


def build_kleurenkiezer(write, out_dir):
    cr, cr_ld = crumbs([("Home", "/"), ("Buitenschilderwerk", "/schilderwerk/buitenschilderwerk/"),
                        ("Kleurenkiezer", None)])

    monumenten = _monument_plaatsen()
    mon_links = ", ".join(f'<a href="/schilder/{p["slug"]}/">{p["naam"]}</a>' for p in monumenten)
    bron_monument = ("https://www.rijksoverheid.nl/onderwerpen/erfgoed/vraag-en-antwoord/"
                     "heb-ik-een-vergunning-nodig-voor-verbouwing-of-restauratie-van-een-monument")

    faqs = [
        ("Welke kozijnkleur past bij een rode bakstenen gevel?",
         "Crèmewit (RAL 9001) en zuiver wit (RAL 9010) passen bij bijna elke rode steen. Wil je meer karakter, "
         "kies dan een donkergroen zoals dennengroen (RAL 6009) of een roodbruin (RAL 3011) voor de draaiende "
         "delen en de voordeur. Antraciet (RAL 7016) staat strak bij rode steen, maar maakt de gevel donkerder."),
        ("Wat is het verschil tussen crèmewit, zuiver wit en verkeerswit?",
         "Crèmewit (RAL 9001) heeft een gele ondertoon en oogt warm. Zuiver wit (RAL 9010) is helder maar "
         "net iets zachter dan verkeerswit (RAL 9016), het koelste wit. Naast elkaar zie je het verschil "
         "duidelijk; los op een gevel valt vooral op of het wit warm of koel is."),
        ("Wat is het verschil tussen een RAL- en een NCS-code?",
         "RAL Classic is een vaste verzameling kleuren met een nummer van vier cijfers, zoals RAL 7016 voor "
         "antracietgrijs. NCS beschrijft elke kleur met zwartheid, kleurigheid en tint: bij S 5040-Y80R is "
         "de kleur voor 50 procent zwart, voor 40 procent kleurig, en geel met 80 procent rood. Je schilder "
         "kan met beide codes verf laten mengen."),
        ("Welke code heeft grachtengroen of Gooiers groen?",
         "Geen vaste. Het zijn traditionele namen, en elk verfmerk mengt er een eigen versie van. Wil je een "
         "vaste code voor klassiek donkergroen, kies dan bijvoorbeeld dennengroen (RAL 6009) of zwartgroen "
         "(RAL 6012). Woon je in een monument, dan bepaalt de gemeente welke kleur mag."),
        ("Is antraciet of zwart slecht voor houten kozijnen?",
         "Niet als het goed gebeurt. Donkere verf wordt in de zon veel warmer dan lichte, waardoor hout meer "
         "werkt en hars kan uittreden. Vraag je schilder om verf die geschikt is voor donkere kleuren, zeker "
         "op een zuid- of westgevel, en reken op wat vaker onderhoud dan bij wit."),
        ("Kost een andere kleur meer dan dezelfde kleur opnieuw?",
         "Meestal wel. Ga je van licht naar donker of andersom, dan dekt één laag vaak niet. De schilder zet "
         "dan een extra laag, soms ook een grondlaag in een tussenkleur. Dat kost meer verf en meer uren. "
         "Vraag in de offerte of die extra laag erin zit."),
        ("Mag ik zelf de kleur van mijn kozijnen kiezen?",
         "Bij een gewoon koophuis meestal wel. Bij een rijksmonument is schilderen in dezelfde kleur "
         "vergunningvrij onderhoud, maar voor een andere kleur heb je een vergunning nodig. In een beschermd "
         "stadsgezicht kunnen regels in het omgevingsplan gelden. Bij een huurhuis of een VvE vraag je de "
         "verhuurder of de VvE."),
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
  <p class="lead">Hoe staan groene ramen bij jouw rode steen? Of antraciet kozijnen bij een witte gevel? Kies je type woning, probeer {len(KLEUREN)} gangbare buitenkleuren met hun RAL- of NCS-code en deel je ontwerp met wie je wilt.</p>
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
    </div>
  </div>
</div></section>

<section class="section soft kk-advies"><div class="wrap narrow prose">
  <span class="badge">Kleuradvies</span>
  <h2>Zo kies je buitenkleuren die bij je huis passen</h2>
  <p>Een gevel bestaat uit vlakken die je niet verandert, zoals de steen en het dak, en houtwerk dat je wel kunt kiezen. Begin daarom bij wat vastligt. Kijk naar de ondertoon van je steen: rode en bruine baksteen hebben een warme ondertoon, gele steen een lichte en zandkleurige, antraciet steen is koel.</p>
  <ul>
    <li><strong>Rode of bruine steen.</strong> Crèmewit of zuiver wit houtwerk is de veilige basis. Donkergroen, roodbruin of staalblauw op de ramen of de deur geeft karakter zonder te vloeken.</li>
    <li><strong>Gele of lichte steen.</strong> Hier passen wit, licht ivoor en zandgeel goed, met een donkere voordeur in groen, blauw of zwart als accent.</li>
    <li><strong>Witte of lichte gevel.</strong> Dit is het speelveld voor antraciet, zwartgrijs en gitzwart. Wie het zachter wil, kiest kwartsgrijs of steengrijs.</li>
    <li><strong>Antraciet steen.</strong> Kies helder wit voor contrast of zwart voor een rustig, donker geheel.</li>
  </ul>
  <p>Een paar vuistregels helpen. Houd het bij twee, hooguit drie kleuren: één voor kozijnen en boeidelen, eventueel één voor de draaiende delen en één accent op de voordeur. Geef de dakkapel dezelfde kleur als de kozijnen eronder, dan hoort hij bij het huis. En kijk naar de buren: in een rij of een twee-onder-een-kap oogt een gelijke kleur voor het vaste houtwerk vaak rustiger.</p>

  <h2>Licht of donker op hout</h2>
  <p>Donkere kleuren nemen veel meer zonnewarmte op dan lichte. Hout wordt daardoor warmer, zet meer uit en krimpt weer als het afkoelt. Bij harsrijk hout kan hars door de verf heen komen, en naden en verbindingen krijgen het zwaarder. Dat betekent niet dat antraciet of zwart niet kan, wel dat de verf en de voorbereiding erop moeten passen. Er bestaan verven die bedoeld zijn voor donkere kleuren in de zon; vraag je schilder daarnaar, zeker op een zuid- of westgevel.</p>
  <p>Lichte kleuren blijven koeler en zijn milder voor het hout, maar op wit en crème zie je vuil en groene aanslag sneller. Een keer per jaar afwassen met water en een zachte borstel houdt elke kleur langer mooi. Bij kunststof kozijnen gelden aparte regels: daar kies je uit de kleuren en folies die de fabrikant levert.</p>

  <h2>Mag je de kleur zelf kiezen? Welstand, monument en VvE</h2>
  <p>In de meeste gewone woonwijken mag je de kleur van je kozijnen en deur zelf kiezen. Er zijn uitzonderingen:</p>
  <ul>
    <li><strong>Rijksmonument.</strong> Opnieuw schilderen in dezelfde kleur is gewoon onderhoud en vergunningvrij. Wil je een andere kleur, dan heb je wel een omgevingsvergunning nodig (bron: <a href="{bron_monument}" rel="noopener" target="_blank">Rijksoverheid, vergunning voor een monument</a>). Gemeentelijke monumenten hebben vaak vergelijkbare regels.</li>
    <li><strong>Beschermd stadsgezicht en welstand.</strong> In oude kernen kan het omgevingsplan van de gemeente regels stellen aan het uiterlijk van gevels, en soms ook aan kleuren. Dat speelt bijvoorbeeld in {mon_links}. Vraag het na bij je gemeente voordat je een opvallend andere kleur kiest.</li>
    <li><strong>VvE of huur.</strong> In een appartementencomplex beslist de VvE meestal over het buitenschilderwerk, vaak in één kleur voor het hele gebouw. Huur je, dan vraag je de verhuurder om toestemming.</li>
  </ul>
  <p>Twijfel je? Een schilder die vaak in jouw gemeente werkt, kent de regels meestal goed. Noem het in je offerteaanvraag als je huis een monument is.</p>

  <h2>Populaire combinaties</h2>
  <p>Klik op een combinatie om hem in de kiezer te zien. De link kun je ook delen of in je offerteaanvraag plakken.</p>
</div>
<div class="wrap"><div class="kk-combis">{_combinaties_html()}</div></div>
</section>

<section class="section"><div class="wrap">
  <h2>Alle kleuren met RAL- en NCS-code</h2>
  <p class="kk-codes-intro">Geef je schilder de code, dan mengt elke verfleverancier dezelfde kleur. De kleur op je scherm is een benadering: vraag altijd een staal of proefvlak.</p>
  {_codes_html()}
  <p class="kk-bron">Bronnen: namen en nummers volgens de RAL Classic-kleurenlijst (<a href="https://www.ralkleuren.com/ral-classic" rel="noopener" target="_blank">ralkleuren.com</a>); schermkleuren volgens de <a href="https://en.wikipedia.org/wiki/List_of_RAL_colours" rel="noopener" target="_blank">RAL-lijst op Wikipedia</a>; Falu-rood volgens de gangbare NCS-notatie S 5040-Y80R (<a href="https://en.wikipedia.org/wiki/Falu_red" rel="noopener" target="_blank">Wikipedia: Falu red</a>). Topschilder is niet verbonden aan een verfmerk.</p>
</div></section>

<section class="section soft" id="offerte-kleuren"><div class="wrap">
  <div class="grid g2" style="gap:48px;align-items:start">
    <div>
      <span class="badge">Van kleur naar offerte</span>
      <h2>Laat je kleuren uitvoeren</h2>
      <p class="lead">Klik op <strong>Offerte voor deze kleuren</strong>. Je kleurkeuze komt dan met de RAL-codes in het formulier, zodat de schilders weten wat je wilt.</p>
      <ul class="checklist">
        <li><strong>Gratis en vrijblijvend.</strong> Je krijgt offertes van maximaal drie schilders uit jouw regio.</li>
        <li><strong>Je kleurlink gaat mee.</strong> De schilder ziet precies welke kleur waar moet.</li>
        <li><strong>Vraag om een kleurstaal.</strong> Een goede schilder laat je de kleur eerst op je eigen kozijn zien.</li>
      </ul>
      <h3>Wat kost het?</h3>
      <ul class="kk-kosten">
        <li><a href="/kosten/kozijnen-schilderen/">Wat kost kozijnen schilderen?</a></li>
        <li><a href="/kosten/huis-schilderen/">Wat kost je huis buiten laten schilderen?</a></li>
        <li><a href="/kosten/dakkapel-schilderen/">Wat kost een dakkapel schilderen?</a></li>
        <li><a href="/kosten/deuren-spuiten/">Wat kost deuren spuiten?</a></li>
        <li><a href="/kosten/schilder-uurtarief/">Wat is het uurtarief van een schilder?</a></li>
      </ul>
      <p>Meer weten over het werk zelf? Lees over <a href="/schilderwerk/buitenschilderwerk/">buitenschilderwerk</a> en <a href="/gids/wanneer-buiten-schilderen/">wanneer je buiten schildert</a>.</p>
    </div>
    <div>{offerte_form("Offerte voor jouw kleuren", "Gratis · vrijblijvend · maximaal 3 schilders")}</div>
  </div>
</div></section>
{faq_html}"""

    html = page(
        title("Kleurenkiezer voor gevel en kozijnen"),
        "Probeer gratis RAL-kleuren voor je kozijnen, ramen, voordeur en boeidelen op jouw type woning. "
        "Met kleuradvies, regels voor monumenten en een deelbare link.",
        PAD, body, [cr_ld, faq_ld, app_ld])
    html = html.replace('<link rel="stylesheet" href="/assets/css/style.css">',
                        '<link rel="stylesheet" href="/assets/css/style.css">'
                        '<link rel="stylesheet" href="/assets/css/kleuren.css">')
    html = html.replace("</body>", '<script src="/assets/js/kleuren.js" defer></script></body>')
    write(PAD, html, prio=0.7)

    _schrijf(os.path.join(out_dir, "assets", "css", "kleuren.css"), KLEUREN_CSS)
    data = {
        "kleuren": [{"id": k["id"], "naam": k["naam"], "hex": k["hex"], "code": k["code"], "uitleg": k["uitleg"],
                     "delen": [DELEN_NAAM[d] for d in k["delen"]], "hout": k["hout"]} for k in KLEUREN],
        "alias": KLEUR_ALIAS,
        "stenen": [{"id": i, "naam": n, "steen": s, "steen2": s2, "voeg": v} for i, n, s, s2, v in STENEN],
        "delen": [{"id": s, "label": l} for s, l, _u in ONDERDELEN],
        "types": [{"id": t, "naam": n} for t, n in TYPES],
        "stijlen": [{"id": s[0], "naam": s[1], "kozijn": s[2], "raam": s[3], "deur": s[4], "boei": s[5],
                     "gevel": s[6], "type": s[7]} for s in STIJLEN],
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
.kk-type{flex:1 1 auto;min-width:0;border:1px solid var(--line);background:var(--bg-soft);border-radius:99px;padding:8px 10px;font:inherit;font-size:.88rem;font-weight:650;color:var(--ink);cursor:pointer;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.kk-type{transition:border-color .15s,background .15s}
.kk-type:hover{border-color:var(--navy-500)}
.kk-type.on{background:var(--accent-soft);border-color:var(--accent);color:var(--ink);box-shadow:0 0 0 3px rgba(244,130,11,.15)}
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
  .kk-types{gap:4px}
  .kk-type{flex:1 1 auto;padding:5px 8px;font-size:.78rem}
  .sticky-cta{display:none}body{padding-bottom:0}
}
@media(max-width:900px) and (max-height:760px){.kk-plaat{max-height:34vh}.kk-svg{max-height:34vh;margin:0 auto;width:auto;max-width:100%}}
.kk-kleurinfo{display:flex;gap:12px;align-items:flex-start;background:var(--bg-soft);border:1px solid var(--line);border-radius:var(--radius);padding:12px;margin-top:14px}
.kk-kleurinfo .kk-stip{flex:0 0 38px;height:38px}
.kk-kleurinfo p{margin:0 0 4px;font-size:.88rem;line-height:1.45}
.kk-ki-kop{font-size:.95rem!important}
.kk-ki-delen{color:var(--muted);font-size:.8rem!important}
.kk-code{display:inline-block;font-size:.76rem;font-weight:700;letter-spacing:.02em;color:var(--ink);background:#fff;border:1px solid var(--line);border-radius:6px;padding:1px 6px;white-space:nowrap}
.kk-advies h2{margin-top:1.6em}.kk-advies h2:first-of-type{margin-top:.4em}
.kk-combis{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:16px;margin-top:8px}
.kk-combi{background:#fff;border:1px solid var(--line);border-radius:var(--radius-lg);padding:18px;box-shadow:var(--shadow);display:flex;flex-direction:column}
.kk-combi h3{font-size:1.05rem;margin:10px 0 6px}
.kk-combi p{font-size:.9rem;margin:0 0 8px}
.kk-cb-codes{color:var(--muted);font-size:.8rem!important}
.kk-cb-bol{display:flex;gap:6px}
.kk-cb-bol i{display:block;width:30px;height:30px;border-radius:50%;box-shadow:inset 0 0 0 1px rgba(0,0,0,.18)}
.kk-cb-bol .kk-cb-steen{border-radius:6px}
.kk-cb-link{margin-top:auto;font-weight:700}
.kk-codes-intro{max-width:720px}
.kk-codes{list-style:none;padding:0;margin:0 0 8px;display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px}
.kk-codes li{display:flex;gap:12px;align-items:flex-start;border:1px solid var(--line);border-radius:var(--radius);padding:12px;background:#fff;min-width:0}
.kk-codes li>i{flex:0 0 42px;height:42px;border-radius:8px;box-shadow:inset 0 0 0 1px rgba(0,0,0,.18)}
.kk-codes li div{min-width:0}
.kk-codes p{font-size:.88rem;margin:4px 0}
.kk-codes small{color:var(--muted);font-size:.8rem}
.kk-bron{font-size:.82rem;color:var(--muted);margin-top:18px}
.kk-kosten{padding-left:1.1em}.kk-kosten li{margin:4px 0}
@media(max-width:420px){.kk-codes{grid-template-columns:minmax(0,1fr)}.kk-combis{grid-template-columns:minmax(0,1fr)}}
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

  var standaard = { type: "rij", kozijn: "cremewit", raam: "dennengroen", deur: "dennengroen", boei: "cremewit", gevel: "rood" };
  var SLEUTELS = ["type", "kozijn", "raam", "deur", "boei", "gevel"];
  var alias = D.alias || {};
  function kleurId(v) { v = alias[v] || v; return kleurById[v] ? v : null; }
  var staat = lees() || Object.assign({}, standaard);
  var actief = "kozijn";
  var melding = document.querySelector(".kk-melding");

  /* ------------------------------------------------ link lezen (# of ?) */
  // Deellinks staan in de hash (#type=…&kozijn=…). Links met ?type=… werken ook, en oude
  // kleur-id's worden via D.alias omgezet naar de kleur die ervoor in de plaats kwam.
  function params(tekst) {
    var q = new URLSearchParams(tekst || "");
    return (q.get("kozijn") || q.get("type") || q.get("raam") || q.get("deur") || q.get("boei") || q.get("gevel")) ? q : null;
  }
  function lees() {
    var q = params(location.hash.slice(1)) || params(location.search.slice(1));
    if (!q) return null;
    var s = Object.assign({}, standaard);
    if (typeNaam[q.get("type")]) s.type = q.get("type");
    ["kozijn", "raam", "deur", "boei"].forEach(function (d) { var k = kleurId(q.get(d)); if (k) s[d] = k; });
    if (steenById[q.get("gevel")]) s.gevel = q.get("gevel");
    return s;
  }
  // Zoekdeel zonder de kiezer-sleutels (andere parameters, zoals utm, blijven staan).
  function restZoek() {
    var q = new URLSearchParams(location.search.slice(1));
    SLEUTELS.forEach(function (k) { q.delete(k); });
    var r = q.toString();
    return r ? "?" + r : "";
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
    kleurinfo();
    if (history.replaceState) history.replaceState(null, "", location.pathname + restZoek() + "#" + hash());
  }

  function naamVan(d) {
    var n = d === "gevel" ? steenById[staat.gevel].naam : kleurById[staat[d]].naam;
    return n.replace(/ \(.*\)$/, "");
  }

  function codeVan(d) { return d === "gevel" ? "" : kleurById[staat[d]].code; }
  function naamCode(d) {
    var c = codeVan(d);
    return naamVan(d).toLowerCase() + (c ? " (" + c + ")" : "");
  }

  function kleurinfo() {
    var box = document.querySelector("[data-kleurinfo]");
    if (!box) return;
    if (actief === "gevel") {
      var g = steenById[staat.gevel];
      box.querySelector(".kk-stip").style.setProperty("--kl", g.steen);
      box.querySelector("[data-ki-naam]").textContent = g.naam;
      box.querySelector("[data-ki-code]").textContent = "gevel";
      box.querySelector("[data-ki-uitleg]").textContent = "De steen bepaalt welke kleuren rustig staan. Kies je kozijnkleur bij de ondertoon van je steen.";
      box.querySelector("[data-ki-delen]").textContent = "";
      return;
    }
    var k = kleurById[staat[actief]];
    box.querySelector(".kk-stip").style.setProperty("--kl", k.hex);
    box.querySelector("[data-ki-naam]").textContent = k.naam;
    box.querySelector("[data-ki-code]").textContent = k.code;
    box.querySelector("[data-ki-uitleg]").textContent = k.uitleg;
    box.querySelector("[data-ki-delen]").textContent = "Vaak gebruikt voor: " + k.delen.join(", ") + ".";
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
    if (verf.some(function (d) { return kleurById[staat[d]].hout; })) {
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
      if (s.type && typeNaam[s.type]) staat.type = s.type;
      teken();
      zeg("Stijl ‘" + s.naam + "’ toegepast. Pas gerust onderdelen aan.");
    });
  });
  var gok = document.querySelector("[data-gok]");
  if (gok) gok.addEventListener("click", function () {
    // Willekeurig, maar met een paar spelregels zodat het er nog als een huis uitziet.
    var lichte = ["cremewit", "gebroken-wit", "wit", "verkeerswit", "licht-ivoor", "lichtgrijs"];
    var accent = D.kleuren.map(function (k) { return k.id; });
    function uit(a) { return a[Math.floor(Math.random() * a.length)]; }
    var basis = Math.random() < 0.7 ? uit(lichte) : uit(["antraciet", "zwart", "zwartgrijs", "eiken", "kwartsgrijs", "steengrijs"]);
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

  // Combinaties onder de tool: laad de kleuren en scroll terug naar de tekening.
  document.querySelectorAll("a[data-combo]").forEach(function (a) {
    a.addEventListener("click", function (e) {
      var u = new URL(a.href, location.href);
      if (u.pathname !== location.pathname) return;
      e.preventDefault();
      var q = params(u.hash.slice(1));
      if (!q) return;
      staat.type = typeNaam[q.get("type")] ? q.get("type") : staat.type;
      ["kozijn", "raam", "deur", "boei"].forEach(function (d) { var k = kleurId(q.get(d)); if (k) staat[d] = k; });
      if (steenById[q.get("gevel")]) staat.gevel = q.get("gevel");
      teken();
      var tool = document.getElementById("kleurenkiezer");
      if (tool) window.scrollTo({ top: tool.getBoundingClientRect().top + window.scrollY - 80, behavior: "smooth" });
      zeg("Combinatie geladen. Pas gerust onderdelen aan.");
    });
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
      x.fillText("Mijn kleuren: " + typeNaam[staat.type].toLowerCase() + ", " + naamVan("gevel").toLowerCase(), 48, 940);
      x.font = "400 25px -apple-system, Segoe UI, Roboto, Arial, sans-serif";
      x.fillStyle = "#57492f";
      var regels = [
        "Kozijnen: " + naamCode("kozijn") + "   ·   Draaiende delen: " + naamCode("raam"),
        "Voordeur: " + naamCode("deur") + "   ·   Boeidelen: " + naamCode("boei")
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
      var regel = "Kleurwens: " + typeNaam[staat.type].toLowerCase() + "; kozijnen " + naamCode("kozijn") +
        ", draaiende delen " + naamCode("raam") + ", voordeur " + naamCode("deur") + ", boeidelen " + naamCode("boei") +
        ", gevel " + naamVan("gevel").toLowerCase() + ". Ontwerp: " + link();
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
