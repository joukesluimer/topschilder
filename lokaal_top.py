# -*- coding: utf-8 -*-
"""Lokale gids voor de 10 plaatsen met het meeste zoekvolume op 'schilder <plaats>'.

Volume: Semrush, database nl, opgehaald 27 november 2026 (maandelijks zoekvolume).
Elke bewering op de pagina komt uit een bron die hieronder staat:
  - woningen en bouwjaren per wijk/buurt: BAG en CBS (plaats_cijfers.py)
  - monumenten en beschermde gezichten: RCE (plaats_cijfers.py) en de gemeente (KLEUR)
  - klimaat: KNMI, langjarige gemiddelden 1991-2020 van het dichtstbijzijnde hoofdstation
  - zoet water: Rijkswaterstaat
  - kozijnen en hout per bouwperiode: TIJDVAKKEN (bronnen per regel)
  - prijs: de landelijke richtprijs maal de regiofactor uit data.PRIJSINDEX, uitdrukkelijk benoemd
    als afgeleide en niet als gemeten lokale prijs.
Verzin hier geen feiten. Wat niet te onderbouwen is, laat je weg.
"""

from data import DIENSTEN, PRIJSINDEX, lokale_prijs
from plaats_cijfers import CIJFERS, META
from lokaal_bronnen import KLEUR, TIJDVAKKEN, TIJDVAK_BRONNEN

# slug -> zoekvolume 'schilder <plaats>' (Semrush nl, november 2026)
VOLUME = {"amersfoort": 1300, "almere": 720, "zwolle": 590, "lelystad": 320, "hilversum": 320,
          "harderwijk": 210, "zeewolde": 170, "ermelo": 170, "nunspeet": 170, "kampen": 170}
TOP10 = list(VOLUME)

# Ronde plaatsen 2 (27 november 2026): de 15 overige plaatsen waarvoor het CBS buurtcijfers heeft.
# De 10 kleine dorpen in de Noordoostpolder zonder CBS-buurten blijven buiten de gids: zonder
# buurtcijfers valt er per buurt niets te onderbouwen.
RONDE2 = ["nijkerk", "huizen", "bussum", "dronten", "emmeloord", "weesp", "putten", "bunschoten-spakenburg",
          "naarden", "urk", "elburg", "blaricum", "genemuiden", "biddinghuizen", "swifterbant"]
LOKAAL = TOP10 + RONDE2

# ---------------------------------------------------------------- klimaat (KNMI)
KNMI_URL = "https://cdn.knmi.nl/knmi/map/page/klimatologie/klimaatatlas/tabel/stationsdata/klimtab_9120_{}.pdf"
KNMI_WIND_URL = "https://www.knmi.nl/over-het-knmi/nieuws/neerslag-de-bilt-windrichting-precipitation-netherlands-wind-direction"
RWS_URL = "https://www.rijkswaterstaat.nl/water/vaarwegenoverzicht/ijsselmeer"
ADLER_URL = ("https://www.adler-verven.nl/Content/Downloads/ARL/Bauten/nl/arl_504_werkrichtlijn-voor-het-coaten-van-"
             "niet-maatvaste-en-beperkt-maatvaste-componenten_onderhoud-en-renovatie-_nl.pdf")

# KNMI, langjarige gemiddelden 1991-2020, jaarwaarden
STATIONS = {
    260: dict(naam="De Bilt", wind=3.6, neerslag=855, regendagen=132, vocht=81, vorst=53, zon=1715),
    269: dict(naam="Lelystad", wind=4.4, neerslag=824, regendagen=133, vocht=83, vorst=53, zon=1771),
    273: dict(naam="Marknesse", wind=4.2, neerslag=805, regendagen=130, vocht=84, vorst=48, zon=1798),
    278: dict(naam="Heino", wind=3.2, neerslag=774, regendagen=130, vocht=83, vorst=62, zon=1713),
    275: dict(naam="Deelen", wind=3.8, neerslag=868, regendagen=135, vocht=82, vorst=65, zon=1644),
    240: dict(naam="Schiphol", wind=5.0, neerslag=850, regendagen=133, vocht=82, vorst=43, zon=1780),  # ronde plaatsen 2
}


# station, hemelsbreed (km, afgerond, schatting), water in de buurt, Noordzeekust hemelsbreed (km, schatting)
LIGGING = {
    "amersfoort": (260, 16, "aan de Eem, landinwaarts", 63),
    "almere": (269, 22, "aan het Gooimeer, IJmeer en Markermeer", 45),
    "zwolle": (278, 14, "aan de IJssel en het Zwarte Water", 100),
    "lelystad": (269, 7, "aan het Markermeer en het IJsselmeer", 58),
    "hilversum": (260, 14, "landinwaarts, tussen heide en bos", 47),
    "harderwijk": (269, 15, "aan het Wolderwijd, tegen de Veluwe", 72),
    "zeewolde": (269, 14, "aan het Wolderwijd en Nuldernauw, in de open polder", 67),
    "ermelo": (269, 19, "aan de Veluwerand, met veel bos", 73),
    "nunspeet": (269, 20, "aan de Veluwerand, tussen bos en Veluwemeer", 82),
    "kampen": (273, 17, "aan de IJssel, vlak bij het Ketelmeer", 87),
    # ronde plaatsen 2: zelfde rekenwijze (haversine vanaf een benaderd centrum, afgerond; schatting)
    "nijkerk": (260, 25, "aan de rand van de Gelderse Vallei, vlak bij het Nijkerkernauw", 67),
    "huizen": (260, 22, "aan het Gooimeer", 48),
    "bussum": (260, 19, "landinwaarts in het Gooi, tussen heide en bos", 44),
    "dronten": (269, 15, "in de open polder van Oostelijk Flevoland", 74),
    "emmeloord": (273, 9, "midden in de open Noordoostpolder", 72),
    "weesp": (240, 17, "aan de Vecht en het Amsterdam-Rijnkanaal", 35),
    "putten": (269, 23, "aan de Veluwerand, niet ver van het Nuldernauw", 73),
    "bunschoten-spakenburg": (260, 21, "aan het Eemmeer", 59),
    "naarden": (260, 22, "vlak bij het Gooimeer en het Naardermeer", 44),
    "urk": (273, 20, "aan het IJsselmeer", 65),
    "elburg": (269, 21, "aan het Veluwemeer", 84),
    "blaricum": (260, 20, "aan de rand van het Gooi, vlak bij het Gooimeer", 50),
    "genemuiden": (273, 13, "aan het Zwarte Water, vlak bij het Zwarte Meer", 94),
    "biddinghuizen": (269, 12, "in de open polder, vlak bij het Veluwemeer", 74),
    "swifterbant": (269, 14, "in de open polder van Oostelijk Flevoland", 68),
}
# soort water of ligging: bepaalt de zin over zout (meer = IJsselmeergebied, zoet volgens Rijkswaterstaat)
WATER = {"amersfoort": "rivier", "zwolle": "rivier", "kampen": "rivier", "hilversum": "land", "bussum": "land",
         "nijkerk": "meer", "weesp": "rivier", "genemuiden": "rivier", "dronten": "polder", "emmeloord": "polder",
         "swifterbant": "polder", "putten": "meer", "ermelo": "land", "nunspeet": "meer"}
TWEEDE_STATION = {"harderwijk": 275, "ermelo": 275, "nunspeet": 275}  # Veluwerand: Deelen ter vergelijking


def _nl(n):
    return f"{n:,}".replace(",", ".")


def _k(x):
    return f"{x:.1f}".replace(".", ",")


def _eur(n):
    return "€" + _nl(int(round(n)))


def _wijknaam(naam):
    import re
    return re.sub(r"^Wijk \d+\s*", "", naam).strip() or naam


def is_top(p):
    """True voor de plaatsen met een lokale gids (top 10 op zoekvolume plus ronde plaatsen 2)."""
    return p["slug"] in LOKAAL and p["slug"] in LIGGING and LIGGING[p["slug"]][0] in STATIONS


def tijdvak(jaar):
    for tot, label, kozijn, aandacht in TIJDVAKKEN:
        if jaar < tot:
            return label, kozijn, aandacht
    return TIJDVAKKEN[-1][1:]


def gebieden(p):
    """Wijken (grote steden) of buurten (middelgrote plaatsen), gesorteerd op mediaan bouwjaar."""
    c = CIJFERS[p["slug"]]
    w = c.get("wijken") or []
    if len(w) >= 3:
        return w, "wijk"
    return c.get("buurten") or [], "buurt"


# ---------------------------------------------------------------- data-gestuurde formulering
# Dezelfde feiten, maar de zin hangt af van de cijfers van de plaats. Zo staat er niet op 25
# pagina's woord voor woord dezelfde alinea.
def gevel_zin(p, s):
    """Welke gevel het zwaarst te lijden heeft. Bronnen: KNMI (windrichting), ADLER ARL 504 (intervallen)."""
    c = CIJFERS[p["slug"]]
    e = c.get("cbs_kern") or c.get("cbs_gemeente") or {}
    if s["wind"] >= 4.2:
        return (f"Bij zoveel wind telt de stand van je huis extra. Volgens het KNMI heeft in De Bilt 61% van de dagen met "
                f"neerslag zuidwestenwind; die gevel vangt dus de meeste slagregen, de zuidkant de meeste zon. ADLER noemt in zijn werkrichtlijn als onderhoudsinterval voor een lichte "
                f"dekkende lak op staand houtwerk: tot 15 jaar als het beschut zit, 10 jaar als het op het weer staat. Vraag de schilder om per gevel te kijken in plaats van alles tegelijk.")
    if (e.get("meergezins_pct") or 0) >= 35:
        return (f"Bij een appartementencomplex kun je de gevels apart laten bekijken. De meeste regen komt hier, net als "
                f"in heel Nederland, met zuidwestenwind (KNMI). Die kant slijt het eerst; de noord- en oostkant houden "
                f"het volgens verffabrikant ADLER duidelijk langer vol. Een VvE kan zo het werk spreiden.")
    if s["vorst"] >= 60:
        return (f"Met {s['vorst']} vorstdagen per jaar gaat water in kieren en scheurtjes vaker bevriezen en uitzetten. "
                f"Houd daarom de kitnaden dicht. Verder geldt ook hier: de zuidwestgevel krijgt de meeste regen (KNMI), "
                f"en houtwerk dat op het weer staat, moet volgens ADLER eerder opnieuw in de verf dan beschut hout.")
    return (f"Het KNMI meldt dat de meeste regendagen in Nederland zuidwestenwind hebben. Daardoor krijgt de "
            f"zuidwestgevel de meeste slagregen, en de zuidkant de meeste zon. Verffabrikant ADLER schrijft dat "
            f"houtwerk dat op het weer en de zon staat, duidelijk korter beschermd blijft dan beschut houtwerk. Laat "
            f"de schilder daarom per gevel kijken: de beschutte noord- of oostkant kan vaak langer mee.")


def monument_zin(p, mon, gez):
    """Wat de telling van de RCE betekent voor wie gaat schilderen."""
    n = p["naam"]
    if gez:
        return (f"Woon je binnen het beschermde gezicht van {n}, dan gelden de regels uit het omgevingsplan van de "
                f"gemeente, ook als je huis zelf geen monument is. Hetzelfde opnieuw schilderen is onderhoud. Een "
                f"nieuwe kleur of een ander soort verf kan een vergunning vragen. Laat de schilder het kleurnummer "
                f"van de huidige verf noteren, dan kun je dat bij de gemeente laten zien.")
    if mon >= 20:
        return (f"Een rijksmonument mag je onderhouden zonder vergunning, zolang het uiterlijk niet verandert. Met "
                f"{_nl(mon)} monumenten in {n} komt een schilder hier geregeld oude panden tegen. Vraag of de schilder "
                f"ervaring heeft met oud hout en met verf die daarbij past, zoals lijnolieverf.")
    if mon > 0:
        return (f"Met {'één monument' if mon == 1 else _nl(mon) + ' monumenten'} speelt dit in {n} maar bij weinig "
                f"huizen. Woon je in zo'n pand, overleg dan eerst met de gemeente als je een andere kleur of verfsoort "
                f"wilt. Voor gewoon onderhoud in dezelfde kleur heb je geen vergunning nodig.")
    return (f"Rijksmonumenten zijn er in {n} niet, dus voor de meeste huizen zijn de regels voor kleur de enige "
            f"die tellen. Twijfel je over een felle kleur, vraag het dan vooraf aan de gemeente.")


def prijs_zin(p, factor, verschil, richting):
    n, prov = p["naam"], p["provincie"]
    if richting == "boven":
        return (f"Wat schilders in {n} precies vragen, houdt niemand openbaar bij. Wij nemen daarom onze landelijke "
                f"richtprijs en rekenen die om met een factor {factor} voor {prov}: {verschil}. Dat getal is een "
                f"<strong>afgeleide</strong>, geen meting in {n}. Je eigen prijs hangt af van je huis, de staat van het "
                f"hout en hoe vol de agenda van de schilder is.")
    if richting == "onder":
        return (f"Een openbare lijst met schildersprijzen per gemeente bestaat niet. Daarom staat hieronder onze "
                f"landelijke richtprijs, keer {factor} voor {prov}. Dat is {verschil}, dus iets goedkoper dan het "
                f"midden van het land. Lees het als een <strong>afgeleide</strong>, niet als een prijs die in {n} is "
                f"gemeten. Wat jij betaalt, hangt af van je huis en van het werk dat nodig is.")
    return (f"Er bestaat geen openbare statistiek van schildersprijzen per gemeente. Daarom rekenen we eerlijk terug: "
            f"we nemen onze landelijke richtprijs en vermenigvuldigen die met een regiofactor voor {prov} van {factor}. "
            f"Dat is {verschil}. Zie het als een <strong>afgeleide</strong>, niet als een gemeten prijs in {n}. De echte "
            f"prijs hangt af van je huis, de staat van het werk en de agenda van de schilder.")


def intro_zin(p):
    n = p["naam"]
    c = CIJFERS[p["slug"]]
    b = c["bag"]
    soort = gebieden(p)[1]
    if b["klassen"][0][2] >= 25:
        return (f"In {n} is {b['klassen'][0][2]}% van de woningen van vóór 1945. Hieronder lees je wat dat betekent "
                f"voor je kozijnen, per {soort}, en wat het weer, de regels voor kleur en de prijs eraan toevoegen.")
    if b["vanaf_2005_pct"] >= 30:
        return (f"{n} groeit nog: {b['vanaf_2005_pct']}% van de woningen is van 2005 of later. Hieronder per {soort} "
                f"welke kozijnen je kunt verwachten, wat het klimaat met je verf doet, wat de gemeente zegt over kleur "
                f"en wat schilderwerk hier ongeveer kost.")
    if b["jaren_1975_1994_pct"] >= 30:
        return (f"Een groot deel van {n} is gebouwd tussen 1975 en 1995 ({b['jaren_1975_1994_pct']}%). Hieronder de "
                f"feiten per {soort}: bouwjaren, kozijnen, klimaat, kleurregels en een eerlijke prijsindicatie.")
    return (f"Wat maakt schilderwerk in {n} anders dan elders? Hieronder de feiten die ertoe doen: hoe oud de huizen "
            f"zijn, welke kozijnen je per {soort} tegenkomt, wat het weer met je verf doet, welke regels er gelden voor "
            f"kleur, en wat het ongeveer kost.")


# ---------------------------------------------------------------- blokken
def bouwgolven(p):
    """De drie jaren waarin de meeste woningen zijn gebouwd, en wat dat nu betekent."""
    c = CIJFERS[p["slug"]]
    per = c["bag"]["per_jaar_vanaf_1940"]
    nu = int(META["opgehaald"][:4])
    top = sorted(range(len(per)), key=lambda i: -per[i])[:3]
    jaren = sorted(1940 + i for i in top)
    lijst = ", ".join(f"{j} ({_nl(per[j - 1940])} woningen)" for j in jaren[:-1]) + f" en {jaren[-1]} ({_nl(per[jaren[-1] - 1940])} woningen)"
    jongste = max(jaren)
    leeftijd = nu - jongste
    if leeftijd < 8:
        fase = (f"De woningen uit {jongste} zijn nu {leeftijd} jaar oud. Fabrieksmatig afgelakte kozijnen krijgen hun eerste "
                f"buitenbeurt meestal na zes tot acht jaar, dus die straten komen er de komende jaren aan.")
    else:
        fase = (f"Ook de jongste van deze golven, uit {jongste}, is al {leeftijd} jaar oud. Bij een beurt om de zes tot acht jaar "
                f"hebben die huizen er zo'n {leeftijd // 8} tot {leeftijd // 6} achter de rug. Hele straten uit hetzelfde jaar "
                f"komen vaak tegelijk aan de beurt.")
    # welke wijk of buurt het dichtst bij de jongste golf ligt (mediaan bouwjaar, CBS/BAG)
    rijen = [r for r in gebieden(p)[0] if r.get("mediaan_bouwjaar") and r.get("woningen", 0) >= 100]
    waar = ""
    if rijen:
        r = min(rijen, key=lambda r: (abs(r["mediaan_bouwjaar"] - jongste), -r["woningen"]))
        if abs(r["mediaan_bouwjaar"] - jongste) <= 6:
            waar = (f"Kijk je per {gebieden(p)[1]}, dan zit {_wijknaam(r['naam'])} met een mediaan bouwjaar van "
                    f"{r['mediaan_bouwjaar']} ({_nl(r['woningen'])} woningen) het dichtst bij dat jaar. ")
    return (f"<p>Volgens de BAG zijn in {p['naam']} de meeste woningen gebouwd in {lijst}. {fase} {waar}"
            f"Woon je in zo'n straat, kijk dan wanneer de buren laten schilderen: een schilder die al in de straat staat, "
            f"hoeft maar één keer zijn steiger en spullen te brengen.</p>")


def wijk_tabel_top(p, max_rijen=10):
    """De grootste wijken of buurten, gegroepeerd per bouwperiode. De typering per periode staat één keer;
    per wijk staan het aantal woningen en het mediane bouwjaar (CBS/BAG)."""
    rijen, soort = gebieden(p)
    if len(rijen) < 3:
        return ""
    keuze = sorted(sorted(rijen, key=lambda r: -r["woningen"])[:max_rijen], key=lambda r: r["mediaan_bouwjaar"] or 0)
    groepen = []  # [(label, kozijn, aandacht, [rijen])]
    gemengd = []
    for r in keuze:
        v45 = r.get("voor_1945_pct") or 0
        if v45 >= 35 and r["mediaan_bouwjaar"] >= 1945:
            gemengd.append(r)  # oude kern met latere invulling: de mediaan zegt hier weinig
            continue
        label, kozijn, aandacht = tijdvak(r["mediaan_bouwjaar"])
        if groepen and groepen[-1][0] == label:
            groepen[-1][3].append(r)
        else:
            groepen.append((label, kozijn, aandacht, [r]))

    def namen(rs):
        return "; ".join(f"<strong>{_wijknaam(r['naam'])}</strong> ({_nl(r['woningen'])} woningen, mediaan {r['mediaan_bouwjaar']})"
                         for r in rs)
    tr = [f"<tr><th scope=\"row\">{label}</th><td>{namen(rs)}</td><td>{kozijn}<br><small><strong>Let op:</strong> {aandacht}</small></td></tr>"
          for label, kozijn, aandacht, rs in groepen]
    if gemengd:
        tr.append("<tr><th scope=\"row\">Gemengd</th><td>" + "; ".join(
            f"<strong>{_wijknaam(r['naam'])}</strong> ({r.get('voor_1945_pct')}% van vóór 1945, mediaan {r['mediaan_bouwjaar']})" for r in gemengd)
            + "</td><td>Oude houten kozijnen naast latere bouw<br><small><strong>Let op:</strong> oude panden vragen veel voorwerk; "
              "bij monumenten kleur en verfsoort vooraf afstemmen</small></td></tr>")
    oudst, jongst = keuze[0], keuze[-1]
    return f"""<h3>Per {soort}: welke kozijnen en welk hout je kunt verwachten</h3>
  <p>Het bouwjaar zegt veel over de kozijnen. In {_wijknaam(oudst['naam'])} is de helft van de woningen van vóór {oudst['mediaan_bouwjaar']}; in {_wijknaam(jongst['naam'])} van na {jongst['mediaan_bouwjaar']}. Hieronder de {len(keuze)} grootste {soort}en, per bouwperiode, met wat in die periode gebruikelijk was. Dat is een typering, geen opname: veel huizen hebben inmiddels nieuwe of kunststof kozijnen.</p>
  <div class="tablewrap"><table class="lt-wijken"><thead><tr><th scope="col">Bouwperiode</th><th scope="col">{soort.capitalize()} (CBS)</th><th scope="col">Gebruikelijk in die periode, en waar je op let</th></tr></thead><tbody>{''.join(tr)}</tbody></table></div>"""


def zout_zin(p, water, kust):
    """Zin over zout en vocht, afhankelijk van de ligging (WATER). Standaard: aan het IJsselmeergebied."""
    n, soort = p["naam"], WATER.get(p["slug"], "meer")
    if soort == "rivier":
        return (f"{n} ligt {water}. Dat is zoet rivierwater, en de Noordzee is hemelsbreed zo'n {kust} kilometer weg. "
                f"De zoute zeewind die aan de kust verf en metaal aantast, komt hier dus niet. Wel vocht: houtwerk dicht "
                f"bij het water droogt na een bui langzamer op.")
    if soort == "land":
        return (f"{n} ligt {water}, op zo'n {kust} kilometer van de Noordzeekust (hemelsbreed). Zeezout is daarmee geen "
                f"factor. Bomen wel: in de schaduw blijft hout langer nat en groeit sneller groene aanslag. Laat die "
                f"vóór het schilderen goed weghalen.")
    if soort == "polder":
        return (f"{n} ligt {water}. Er staan weinig bomen of heuvels die de wind breken. Het water in de buurt hoort bij "
                f"het IJsselmeergebied, en dat is volgens Rijkswaterstaat zoet. De kust ligt zo'n {kust} kilometer "
                f"verderop (hemelsbreed). Je verf heeft hier dus last van wind en regen, niet van zout.")
    return (f"Zout speelt hier nauwelijks een rol. {n} ligt {water}; dat water is zoet. Het IJsselmeer is sinds de "
            f"Afsluitdijk (1932) een zoetwatermeer, volgens Rijkswaterstaat het grootste van Nederland. De Noordzeekust ligt "
            f"hemelsbreed zo'n {kust} kilometer verderop. Zoute zeewind, die verf en metaal aan de kust sneller aantast, is hier "
            f"dus geen factor; vocht en wind wel.")


def klimaat_blok(p, kort=False):
    st_nr, km, water, kust = LIGGING[p["slug"]]
    s = STATIONS[st_nr]
    db = STATIONS[260]
    if st_nr == 260:
        vergelijk = "De Bilt is ook het station waarmee het KNMI het landelijke klimaat beschrijft."
    else:
        meer = "meer" if s["wind"] > db["wind"] else "minder"
        vergelijk = (f"Dat is {meer} wind dan in De Bilt ({_k(db['wind'])} m/s), het station in het midden van het land. ")
        if s["wind"] - db["wind"] >= 0.5:
            vergelijk += "Meer wind betekent dat regen harder tegen de gevel slaat en dat houtwerk vaker nat wordt."
    tweede = ""
    if p["slug"] in TWEEDE_STATION:
        t = STATIONS[TWEEDE_STATION[p["slug"]]]
        tweede = (f" {p['naam']} ligt tussen het open polderstation Lelystad en het Veluwestation {t['naam']} "
                  f"({_k(t['wind'])} m/s wind, {t['vorst']} vorstdagen). Aan de bosrand zal het minder waaien dan in de polder, "
                  f"maar dat is een inschatting, geen meting.")
    zout = zout_zin(p, water, kust)
    if kort:
        return (f"Het dichtstbijzijnde KNMI-station, {s['naam']} (zo'n {km} km), meet gemiddeld {_k(s['wind'])} m/s wind, "
                f"{s['regendagen']} dagen per jaar met minstens 1 mm regen en een luchtvochtigheid van {s['vocht']}%. "
                f"De meeste regen komt met zuidwestenwind, dus de zuidwestgevel krijgt het zwaarst te verduren. {vergelijk.strip()}")
    return f"""<h3>Klimaat: wind, vocht en zout</h3>
  <p>Het dichtstbijzijnde hoofdstation van het KNMI is {s['naam']}, hemelsbreed zo'n {km} kilometer van {p['naam']}. Over 1991–2020 mat het KNMI daar:</p>
  <div class="tablewrap"><table class="lt-klimaat"><tbody>
    <tr><th scope="row">Gemiddelde windsnelheid</th><td class="num">{_k(s['wind'])} m/s</td></tr>
    <tr><th scope="row">Neerslag per jaar</th><td class="num">{s['neerslag']} mm</td></tr>
    <tr><th scope="row">Dagen met minstens 1 mm regen</th><td class="num">{s['regendagen']}</td></tr>
    <tr><th scope="row">Gemiddelde luchtvochtigheid</th><td class="num">{s['vocht']}%</td></tr>
    <tr><th scope="row">Vorstdagen (minimum onder 0 °C)</th><td class="num">{s['vorst']}</td></tr>
    <tr><th scope="row">Zonuren per jaar</th><td class="num">{_nl(s['zon'])}</td></tr>
  </tbody></table></div>
  <p>{vergelijk.strip()}{tweede} {gevel_zin(p, s)}</p>
  <p>{zout}</p>"""


def kleur_blok(p, kort=False):
    c = CIJFERS[p["slug"]]
    k = KLEUR.get(p["slug"])
    mon = c.get("rijksmonumenten", 0) - c.get("rijksmonumenten_archeologisch", 0)
    gez = c.get("beschermde_gezichten") or []
    feiten = []
    if mon:
        feiten.append(f"{_nl(mon)} gebouwde rijksmonumenten" if mon > 1 else "één gebouwd rijksmonument")
    if gez:
        feiten.append("de rijksbeschermde gezichten " + " en ".join(
            [", ".join(gez[:-1]), gez[-1]] if len(gez) > 1 else gez) if len(gez) > 1 else f"het rijksbeschermde gezicht {gez[0]}")
    zin = (f"Volgens de Rijksdienst voor het Cultureel Erfgoed heeft {p['naam']} {' en '.join(feiten)}. " if feiten else "")
    regels = k["regels"] if k else ""
    link = (f' Lees het na op <a href="{k["url"]}" rel="nofollow noopener" target="_blank">de pagina van de gemeente {p["gemeente"]}</a>.'
            if k and k.get("url") else "")
    if kort:
        return (zin + regels + link).strip()
    extra = f"<p>{k['extra']}</p>" if k and k.get("extra") else ""
    return f"""<h3>Monumenten, beschermd gezicht en kleur</h3>
  <p>{zin}{regels}{link}</p>
  {extra}
  <p>{monument_zin(p, mon, gez)}</p>"""


def prijs_blok(p):
    idx = PRIJSINDEX.get(p["provincie"], 1.0)
    rijen = []
    for d in DIENSTEN:
        van, tot = lokale_prijs(d, p)
        rijen.append(f"<tr><td><a href=\"/schilder/{p['slug']}/{d['slug']}/\">{d['naam']}</a></td>"
                     f"<td class=\"num\">{_eur(d['prijs_van'])} – {_eur(d['prijs_tot'])}</td>"
                     f"<td class=\"num\"><strong>{_eur(van)} – {_eur(tot)}</strong></td><td>{d['prijs_eenheid']}</td></tr>")
    factor = f"{idx:.2f}".replace(".", ",")
    richting = "onder" if idx < 0.99 else ("op" if idx < 1.01 else "boven")
    pct = abs(round((idx - 1) * 100))
    verschil = f"{pct}% {richting} het landelijk gemiddelde" if richting != "op" else "gelijk aan het landelijk gemiddelde"
    return f"""<h3>Prijsindicatie voor {p['naam']}</h3>
  <p>{prijs_zin(p, factor, verschil, richting)}</p>
  <div class="tablewrap"><table class="lt-prijs"><thead><tr><th scope="col">Klus</th><th scope="col" class="num">Landelijk</th><th scope="col" class="num">Afgeleid voor {p['naam']}</th><th scope="col">Eenheid</th></tr></thead><tbody>{''.join(rijen)}</tbody></table></div>
  <p>Hoe we aan de landelijke prijzen komen, staat op <a href="/prijzen/">de prijzenpagina</a>. Per klus vind je meer detail bij <a href="/kosten/">kosten per klus</a>.</p>"""


def bronnen_top(p):
    st_nr = LIGGING[p["slug"]][0]
    k = KLEUR.get(p["slug"]) or {}
    delen = [
        f'klimaat: KNMI, <a href="{KNMI_URL.format(st_nr)}" rel="nofollow noopener" target="_blank">langjarige gemiddelden 1991–2020, station {STATIONS[st_nr]["naam"]}</a>'
        + (f' en <a href="{KNMI_URL.format(TWEEDE_STATION[p["slug"]])}" rel="nofollow noopener" target="_blank">station {STATIONS[TWEEDE_STATION[p["slug"]]]["naam"]}</a>' if p["slug"] in TWEEDE_STATION else ""),
        f'windrichting: <a href="{KNMI_WIND_URL}" rel="nofollow noopener" target="_blank">KNMI</a>',
        f'zoet water: <a href="{RWS_URL}" rel="nofollow noopener" target="_blank">Rijkswaterstaat</a>',
        f'verweringsrichting: <a href="{ADLER_URL}" rel="nofollow noopener" target="_blank">ADLER, werkrichtlijn ARL 504</a>',
    ]
    if k.get("bron"):
        delen.append(k["bron"])
    delen.append("kozijnen per bouwperiode: " + TIJDVAK_BRONNEN)
    delen.append("afstanden hemelsbreed zijn afgeronde schattingen; prijzen: landelijke richtprijs van Topschilder maal regiofactor")
    selectie = ("Zoekvolume en selectie: Semrush, november 2026." if p["slug"] in VOLUME else
                "Selectie: plaatsen in ons werkgebied waarvoor het CBS cijfers per buurt publiceert.")
    return f'<p class="pc-bron"><small>Bronnen van de gids (BAG, CBS en RCE: zie de bronnen bij de cijfers hierboven): {"; ".join(delen)}. {selectie}</small></p>'


def lokaal_sectie(p):
    """Sectie 'lokale gids' voor /schilder/<plaats>/ van de top 10. Leeg voor de overige plaatsen."""
    if not is_top(p) or p["slug"] not in CIJFERS:
        return ""
    return f"""<section class="section soft" id="lokale-gids"><div class="wrap narrow prose">
  <h2>Schilderwerk in {p['naam']}: de lokale gids</h2>
  <p>{intro_zin(p)}</p>
  <h3>Bouwgolven: wanneer jouw straat aan de beurt is</h3>
  {bouwgolven(p)}
  {wijk_tabel_top(p)}
  {klimaat_blok(p)}
  {kleur_blok(p)}
  {prijs_blok(p)}
  {bronnen_top(p)}
</div></section>"""


# ---------------------------------------------------------------- plaats-dienstpagina
def lokaal_dienst_blok(d, p):
    """Lokaal blok per dienst voor /schilder/<plaats>/<dienst>/ van de top 10."""
    if not is_top(p) or p["slug"] not in CIJFERS:
        return ""
    slug = d["slug"]
    rijen, soort = gebieden(p)
    rijen = [r for r in rijen if r.get("mediaan_bouwjaar")]
    groot = sorted(rijen, key=lambda r: -r["woningen"])[:8]
    zinnen = []
    if slug in ("buitenschilderwerk", "houtrot-reparatie"):
        oud = sorted(groot, key=lambda r: r["mediaan_bouwjaar"])[:3]
        if oud:
            delen = []
            for r in oud:
                _, kozijn, _ = tijdvak(r["mediaan_bouwjaar"])
                delen.append(f"{_wijknaam(r['naam'])} (mediaan {r['mediaan_bouwjaar']}, {kozijn.split(';')[0].split(',')[0].lower()})")
            zinnen.append(f"Van de {len(groot)} grootste {soort}en zijn de oudste {', '.join(delen[:-1])} en {delen[-1]}." if len(delen) > 1 else f"De oudste grote {soort} is {delen[0]}.")
        zinnen.append(klimaat_blok(p, kort=True))
        if slug == "buitenschilderwerk":
            kb = kleur_blok(p, kort=True)
            if kb:
                zinnen.append(kb)
        else:
            zinnen.append("Houtrot begint waar water blijft staan: onderdorpels, kozijnhoeken en de onderkant van deuren. "
                          "Met zoveel regendagen loont het om die plekken elk voorjaar even te prikken.")
    elif slug in ("binnenschilderwerk", "spuitwerk", "behangen"):
        tel = {}
        for r in rijen:
            label = tijdvak(r["mediaan_bouwjaar"])[0]
            tel[label] = tel.get(label, 0) + r["woningen"]
        tot = sum(tel.values()) or 1
        top = sorted(tel.items(), key=lambda x: -x[1])[:3]
        verdeling = ", ".join(f"{round(100 * n / tot)}% in {soort}en uit {lab}" for lab, n in top)
        zinnen.append(f"Kijk je naar het mediane bouwjaar per {soort}, dan woont in {p['naam']} {verdeling}.")
        tekst = {
            "binnenschilderwerk": "In oudere wijken zijn plafonds hoger en zitten er vaker oude pleisterlagen, in wijken uit 1975 tot 1995 vaak spachtelputz en structuurplafonds, en in nieuwbouw kale wanden die een voorstrijklaag nodig hebben.",
            "spuitwerk": "In wijken uit de jaren zeventig tot negentig zitten vaak nog originele binnendeuren met meerdere lagen kwastverf; spuiten geeft daar het meeste verschil. In nieuwbouw gaat spuitwerk vaker over latex op kale wanden.",
            "behangen": "In vooroorlogse en naoorlogse wijken zit vaker oud behang in meerdere lagen, wat het strippen duurder maakt. In jongere wijken zijn de wanden vlakker en kan vliesbehang vaak direct op de voorbehandelde muur.",
        }[slug]
        zinnen.append(tekst)
    elif slug == "zakelijk-schilderwerk":
        c = CIJFERS[p["slug"]]
        e = c.get("cbs_kern") or c.get("cbs_gemeente") or {}
        if e.get("corporatie_pct") is not None:
            zinnen.append(f"In {p['naam']} is {e['corporatie_pct']}% van de woningen van een corporatie en {e.get('meergezins_pct', 0)}% een appartement of andere meergezinswoning (CBS). Dat schilderwerk loopt meestal via een meerjarenonderhoudsplan.")
        kb = kleur_blok(p, kort=True)
        if kb:
            zinnen.append(kb)
    if not zinnen:
        return ""
    return (f"<h3>{d['naam']} in {p['naam']}: lokale feiten</h3><p>{' '.join(zinnen)}</p>"
            f'<p>Alles op een rij, met bronnen: <a href="/schilder/{p["slug"]}/#lokale-gids">de lokale gids voor {p["naam"]}</a>.</p>')
