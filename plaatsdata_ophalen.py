# -*- coding: utf-8 -*-
"""Haalt open data per plaats op en schrijft plaats_cijfers.py.

Draai dit los (niet tijdens build.py): python3 plaatsdata_ophalen.py
De site zelf doet nooit live API-calls; build.py leest alleen plaats_cijfers.py.

Bronnen (allemaal open data, hergebruik toegestaan):
- BAG, Kadaster, via PDOK-WFS (CC0): bouwjaar van elke woning (verblijfsobject met woonfunctie).
- CBS Kerncijfers wijken en buurten 2024 (tabel 85984NED, CC BY 4.0): eigendom en woningtype.
- CBS Wijk- en buurtkaart 2024 via PDOK (CC BY 4.0): wijk- en buurtgrenzen.
  Alleen de buurten bijwerken (plaatsen van 5.000 tot 40.000 inwoners): python3 plaatsdata_ophalen.py --buurten
- Rijksdienst voor het Cultureel Erfgoed (CC BY 4.0): Rijksmonumentenregister (linked data) en
  geodata van rijksmonumenten en rijksbeschermde stads- en dorpsgezichten.

Tussenresultaten komen in een cache (standaard ~/.cache/topschilder-plaatsdata), zodat
een tweede run snel is. Gooi de cache weg voor verse cijfers.
"""

import datetime
import json
import os
import statistics
import sys
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor

from data import PLAATSEN

CACHE = os.environ.get("PLAATSDATA_CACHE", os.path.expanduser("~/.cache/topschilder-plaatsdata"))
BAG = "https://service.pdok.nl/lv/bag/wfs/v2_0"
WB = "https://service.pdok.nl/cbs/wijkenbuurten/2024/wfs/v1_0"
RCE = "https://services.rce.geovoorziening.nl/rce/wfs"
RCE_SPARQL = "https://api.linkeddata.cultureelerfgoed.nl/datasets/rce/cho/services/cho/sparql"
CBS = "https://opendata.cbs.nl/ODataApi/odata/85984NED/TypedDataSet"

# Naam van de woonplaats in de BAG als die afwijkt van de naam op de site.
BAG_NAAM = {}
GEMEENTECODE = {
    "Zeewolde": "GM0050", "Almere": "GM0034", "Lelystad": "GM0995", "Dronten": "GM0303",
    "Noordoostpolder": "GM0171", "Urk": "GM0184", "Harderwijk": "GM0243", "Ermelo": "GM0233",
    "Putten": "GM0273", "Nijkerk": "GM0267", "Nunspeet": "GM0302", "Elburg": "GM0230",
    "Kampen": "GM0166", "Zwolle": "GM0193", "Zwartewaterland": "GM1896", "Bunschoten": "GM0313",
    "Amersfoort": "GM0307", "Huizen": "GM0406", "Blaricum": "GM0376", "Gooise Meren": "GM1942",
    "Hilversum": "GM0402", "Amsterdam": "GM0363",
}
# Plaatsen waarvoor we per CBS-wijk rekenen (groot genoeg voor zinnige wijkcijfers).
WIJK_MIN_INWONERS = 40000
WIJK_MIN_WONINGEN = 250

# Bouwjaarklassen: (label, van, tot en met)
KLASSEN = [
    ("vóór 1945", 1000, 1944), ("1945–1964", 1945, 1964), ("1965–1974", 1965, 1974),
    ("1975–1984", 1975, 1984), ("1985–1994", 1985, 1994), ("1995–2004", 1995, 2004),
    ("2005–2014", 2005, 2014), ("2015 en later", 2015, 2100),
]
BESTAAND = {"Verblijfsobject in gebruik", "Verblijfsobject in gebruik (niet ingemeten)",
            "Verblijfsobject verbouwd", "Verblijfsobject buiten gebruik"}


def get(url, params, naam, as_json=True, tries=4):
    os.makedirs(CACHE, exist_ok=True)
    pad = os.path.join(CACHE, naam)
    if os.path.exists(pad):
        with open(pad, encoding="utf-8") as f:
            return json.load(f) if as_json else f.read()
    full = url + "?" + urllib.parse.urlencode(params)
    for i in range(tries):
        try:
            req = urllib.request.Request(full, headers={"User-Agent": "topschilder-plaatsdata/1.0"})
            with urllib.request.urlopen(req, timeout=120) as r:
                txt = r.read().decode("utf-8")
            res = json.loads(txt) if as_json else txt
            with open(pad, "w", encoding="utf-8") as f:
                f.write(txt)
            return res
        except Exception as e:  # noqa: BLE001
            if i == tries - 1:
                raise
            print(f"  opnieuw ({e}) {naam}", file=sys.stderr)
            time.sleep(3 * (i + 1))


def fes_eq(prop, val):
    return (f'<fes:Filter xmlns:fes="http://www.opengis.net/fes/2.0"><fes:PropertyIsEqualTo>'
            f'<fes:ValueReference>{prop}</fes:ValueReference><fes:Literal>{val}</fes:Literal>'
            f'</fes:PropertyIsEqualTo></fes:Filter>')


def fes_woningen(woonplaats, band=None):
    jaar = ""
    if band:
        jaar = ("<fes:PropertyIsBetween><fes:ValueReference>bouwjaar</fes:ValueReference>"
                f"<fes:LowerBoundary><fes:Literal>{band[0]}</fes:Literal></fes:LowerBoundary>"
                f"<fes:UpperBoundary><fes:Literal>{band[1]}</fes:Literal></fes:UpperBoundary></fes:PropertyIsBetween>")
    return ('<fes:Filter xmlns:fes="http://www.opengis.net/fes/2.0"><fes:And><fes:PropertyIsEqualTo>'
            f'<fes:ValueReference>woonplaats</fes:ValueReference><fes:Literal>{woonplaats}</fes:Literal>'
            '</fes:PropertyIsEqualTo><fes:PropertyIsLike wildCard="*" singleChar="." escapeChar="!">'
            '<fes:ValueReference>gebruiksdoel</fes:ValueReference><fes:Literal>*woonfunctie*</fes:Literal>'
            f'</fes:PropertyIsLike>{jaar}</fes:And></fes:Filter>')


# ---------------------------------------------------------------- geometrie
def ringen(geom):
    """Alle ringen van een (Multi)Polygon als lijst van coördinatenlijsten."""
    if geom["type"] == "Polygon":
        return [r for r in geom["coordinates"]]
    return [r for poly in geom["coordinates"] for r in poly]


def in_ringen(x, y, rs):
    """Even-odd-regel over alle ringen: werkt ook met gaten en multipolygonen."""
    binnen = False
    for r in rs:
        n = len(r)
        j = n - 1
        for i in range(n):
            xi, yi = r[i][0], r[i][1]
            xj, yj = r[j][0], r[j][1]
            if (yi > y) != (yj > y) and x < (xj - xi) * (y - yi) / (yj - yi) + xi:
                binnen = not binnen
            j = i
    return binnen


def bbox(rs):
    xs = [p[0] for r in rs for p in r]
    ys = [p[1] for r in rs for p in r]
    return min(xs), min(ys), max(xs), max(ys)


# ---------------------------------------------------------------- BAG
def bag_aantal(wp, band=None):
    """Aantal treffers (resultType=hits), om te bepalen of we moeten opsplitsen."""
    import re
    txt = get(BAG, {"service": "WFS", "version": "2.0.0", "request": "GetFeature",
                    "typeNames": "bag:verblijfsobject", "resultType": "hits",
                    "filter": fes_woningen(wp, band)},
              f"hits-{wp}-{band[0] if band else 'alle'}.xml", as_json=False)
    return int(re.search(r'numberMatched="(\d+)"', txt).group(1))


def bag_woningen(wp):
    """Alle woningen (punt + bouwjaar + status) in een woonplaats, in pagina's van 1000.

    De PDOK-WFS staat geen startIndex boven 50.000 toe; grote plaatsen vragen we daarom
    per bouwjaarband op.
    """
    if bag_aantal(wp) <= 50000:
        delen = [(None, f"bag-{wp}")]
    else:
        delen = [((a, b), f"bag-{wp}-bj{a}") for _, a, b in KLASSEN]
    uit = []
    for band, sleutel in delen:
        start = 0
        while True:
            d = get(BAG, {
                "service": "WFS", "version": "2.0.0", "request": "GetFeature",
                "typeNames": "bag:verblijfsobject", "outputFormat": "application/json",
                "count": 1000, "startIndex": start, "sortBy": "identificatie",
                "propertyName": "identificatie,bouwjaar,status,geom",
                "filter": fes_woningen(wp, band),
            }, f"{sleutel}-{start}.json")
            fs = d["features"]
            for f in fs:
                pr = f["properties"]
                if pr["status"] in BESTAAND and pr.get("bouwjaar"):
                    x, y = f["geometry"]["coordinates"][:2]
                    uit.append((x, y, int(pr["bouwjaar"])))
            if len(fs) < 1000:
                break
            start += 1000
    return uit


def woonplaats_geom(wp):
    d = get(BAG, {"service": "WFS", "version": "2.0.0", "request": "GetFeature",
                  "typeNames": "bag:woonplaats", "outputFormat": "application/json",
                  "filter": fes_eq("woonplaats", wp)}, f"wp-{wp}.json")
    fs = [f for f in d["features"] if f["properties"].get("status") == "Woonplaats aangewezen"] or d["features"]
    return [r for f in fs for r in ringen(f["geometry"])]


def verdeling(jaren):
    jaar_nu = datetime.date.today().year
    jaren = [j for j in jaren if 1000 <= j <= jaar_nu]
    tel = [sum(1 for j in jaren if a <= j <= b) for _, a, b in KLASSEN]
    tot = len(jaren)
    return {
        "woningen": tot,
        "klassen": [[lab, n, round(100 * n / tot) if tot else 0] for (lab, _, _), n in zip(KLASSEN, tel)],
        "mediaan_bouwjaar": int(statistics.median(jaren)) if jaren else None,
        "dominant": KLASSEN[tel.index(max(tel))][0] if tot else None,
        "voor_1975_pct": round(100 * sum(1 for j in jaren if j < 1975) / tot) if tot else 0,
        "jaren_1975_1994_pct": round(100 * sum(1 for j in jaren if 1975 <= j <= 1994) / tot) if tot else 0,
        "vanaf_2005_pct": round(100 * sum(1 for j in jaren if j >= 2005) / tot) if tot else 0,
        "jaren30_pct": round(100 * sum(1 for j in jaren if 1920 <= j <= 1940) / tot) if tot else 0,
        "oudste_bouwjaar": min(jaren) if jaren else None,
        # aantal woningen per bouwjaar vanaf 1940 (index 0 = 1940), voor precieze drempels
        "per_jaar_vanaf_1940": [sum(1 for j in jaren if j == y) for y in range(1940, jaar_nu + 1)],
        "voor_1940": sum(1 for j in jaren if j < 1940),
    }


# ---------------------------------------------------------------- CBS
def cbs_rijen(gm):
    nr = gm[2:]
    d = get(CBS, {
        "$filter": f"startswith(WijkenEnBuurten,'GM{nr}') or startswith(WijkenEnBuurten,'WK{nr}')",
        "$select": ("WijkenEnBuurten,SoortRegio_2,AantalInwoners_5,Woningvoorraad_35,"
                    "PercentageEengezinswoning_40,PercentageMeergezinswoning_45,Koopwoningen_47,"
                    "HuurwoningenTotaal_48,InBezitWoningcorporatie_49,InBezitOverigeVerhuurders_50,"
                    "GemiddeldeWOZWaardeVanWoningen_39"),
        "$format": "json"}, f"cbs-{gm}.json")
    namen = get("https://opendata.cbs.nl/ODataApi/odata/85984NED/WijkenEnBuurten", {
        "$filter": f"startswith(Key,'GM{nr}') or startswith(Key,'WK{nr}')", "$format": "json"},
        f"cbsnamen-{gm}.json")
    titel = {n["Key"].strip(): n["Title"].strip() for n in namen["value"]}
    uit = {}
    for r in d["value"]:
        code = r["WijkenEnBuurten"].strip()
        uit[code] = {
            "naam": titel.get(code, code),
            "woningvoorraad": r["Woningvoorraad_35"],
            "koop_pct": r["Koopwoningen_47"],
            "huur_pct": r["HuurwoningenTotaal_48"],
            "corporatie_pct": r["InBezitWoningcorporatie_49"],
            "overige_huur_pct": r["InBezitOverigeVerhuurders_50"],
            "eengezins_pct": r["PercentageEengezinswoning_40"],
            "meergezins_pct": r["PercentageMeergezinswoning_45"],
        }
    return uit


def wijk_geoms(gm):
    d = get(WB, {"service": "WFS", "version": "2.0.0", "request": "GetFeature",
                 "typeNames": "wijkenbuurten:wijken", "outputFormat": "application/json",
                 "propertyName": "wijkcode,wijknaam,gemeentecode,geom",
                 "filter": fes_eq("gemeentecode", gm)}, f"wijken-{gm}.json")
    uit = []
    for f in d["features"]:
        rs = ringen(f["geometry"])
        uit.append((f["properties"]["wijkcode"], f["properties"]["wijknaam"], rs, bbox(rs)))
    return uit


# ---------------------------------------------------------------- RCE
def monumenten_register(wp):
    """Rijksmonumentnummers met een adres in de woonplaats, uit het Rijksmonumentenregister (RCE linked data)."""
    q = ("PREFIX ceo: <https://linkeddata.cultureelerfgoed.nl/def/ceo#> SELECT DISTINCT ?nr WHERE { "
         "?m ceo:rijksmonumentnummer ?nr ; ceo:heeftBasisregistratieRelatie ?b . "
         f'?b ceo:heeftBAGRelatie ?bag . ?bag ceo:woonplaatsnaam "{wp}" . }}')
    d = get(RCE_SPARQL, {"query": q, "format": "json"}, f"rcereg-{wp}.json")
    return {int(r["nr"]) for r in d}  # format=json geeft een platte lijst rijen


def monumenten(rs, wp):
    """Rijksmonumenten in de woonplaats: met een adres in de woonplaats (register) of met een punt
    binnen de woonplaatsgrens (geodata; vangt monumenten zonder adres, zoals bruggen en grafmonumenten).
    Niet elk monument staat in de geodata, en niet elk monument heeft een adres; daarom de vereniging.
    Archeologische monumenten (in de polders vaak scheepswrakken) tellen we apart, want dat zijn geen panden."""
    x0, y0, x1, y1 = bbox(rs)
    ruimtelijk, archeologisch = set(), set()
    start = 0
    while True:
        d = get(RCE, {"service": "WFS", "version": "2.0.0", "request": "GetFeature",
                      "typeNames": "rce:NationalListedMonumentPoints", "outputFormat": "application/json",
                      "count": 5000, "startIndex": start,
                      "bbox": f"{x0},{y0},{x1},{y1},urn:ogc:def:crs:EPSG::28992"},
                f"rce-{int(x0)}-{int(y0)}-{int(x1)}-{int(y1)}-{start}.json")
        fs = d["features"]
        for f in fs:
            x, y = f["geometry"]["coordinates"][:2]
            if in_ringen(x, y, rs):
                ruimtelijk.add(f["properties"]["rijksmonument_nummer"])
                if f["properties"].get("aard_monument") == "archeologisch":
                    archeologisch.add(f["properties"]["rijksmonument_nummer"])
        if len(fs) < 5000:
            break
        start += 5000
    register = monumenten_register(wp)
    alle = register | ruimtelijk
    return {"rijksmonumenten": len(alle), "rijksmonumenten_archeologisch": len(archeologisch - register),
            "rijksmonumenten_register": len(register), "rijksmonumenten_ligging": len(ruimtelijk)}


def gezichten():
    d = get(RCE, {"service": "WFS", "version": "2.0.0", "request": "GetFeature",
                  "typeNames": "rce:Townscapes", "outputFormat": "application/json"}, "rce-townscapes.json")
    uit = []
    for f in d["features"]:
        if f.get("geometry"):
            uit.append((f["properties"].get("NAAM"), ringen(f["geometry"])))
    return uit


def gezichten_in(rs, alle):
    """Rijksbeschermde gezichten die (grotendeels) in de woonplaats liggen; een gedeelde grens telt niet."""
    namen = []
    for naam, grs in alle:
        pts = [p for r in grs for p in r]
        cx = sum(p[0] for p in pts) / len(pts)
        cy = sum(p[1] for p in pts) / len(pts)
        steek = pts[::max(1, len(pts) // 50)]
        binnen = sum(1 for p in steek if in_ringen(p[0], p[1], rs))
        if in_ringen(cx, cy, rs) or binnen > 0.6 * len(steek):
            namen.append(naam)
    return sorted(set(namen))


# ---------------------------------------------------------------- hoofdlijn
def plaats_cijfers(p, alle_gezichten):
    wp = BAG_NAAM.get(p["slug"], p["naam"])
    print(f"- {p['naam']}", file=sys.stderr)
    rs = woonplaats_geom(wp)
    pts = bag_woningen(wp)
    gm = GEMEENTECODE[p["gemeente"]]
    cbs = cbs_rijen(gm)
    res = {"bag": verdeling([j for _, _, j in pts]), "gemeentecode": gm, "cbs_gemeente": cbs.get(gm)}

    # Welke CBS-wijken vormen samen deze woonplaats? Een wijk telt mee als minstens de helft van
    # zijn woningen (CBS) binnen de woonplaats ligt. Dekken die wijken niet de hele gemeente, dan
    # zijn hun gewogen cijfers preciezer dan die van de gemeente (bijv. Weesp binnen Amsterdam).
    alle_wijken = wijk_geoms(gm)
    per_wijk = {}
    for code, naam, wrs, (x0, y0, x1, y1) in alle_wijken:
        per_wijk[code] = (naam, [j for x, y, j in pts if x0 <= x <= x1 and y0 <= y <= y1 and in_ringen(x, y, wrs)])
    gekozen = [code for code, (naam, js) in per_wijk.items()
               if cbs.get(code, {}).get("woningvoorraad") and len(js) >= 0.5 * cbs[code]["woningvoorraad"]]
    alle_met_woningen = [code for code in per_wijk if cbs.get(code, {}).get("woningvoorraad")]
    if gekozen and set(gekozen) != set(alle_met_woningen):
        kern = {"naam": p["naam"], "wijken": [cbs[c]["naam"] for c in gekozen],
                "woningvoorraad": sum(cbs[c]["woningvoorraad"] for c in gekozen)}
        for veld in ("koop_pct", "huur_pct", "corporatie_pct", "overige_huur_pct", "eengezins_pct", "meergezins_pct"):
            paren = [(cbs[c][veld], cbs[c]["woningvoorraad"]) for c in gekozen if cbs[c].get(veld) is not None]
            gewicht = sum(w for _, w in paren)
            kern[veld] = round(sum(v * w for v, w in paren) / gewicht) if gewicht >= 0.8 * kern["woningvoorraad"] else None
        res["cbs_kern"] = kern

    res.update(monumenten(rs, wp))
    res["beschermde_gezichten"] = gezichten_in(rs, alle_gezichten)

    if p["inwoners"] >= WIJK_MIN_INWONERS:
        wijken = []
        for code, (naam, jaren) in per_wijk.items():
            if len(jaren) < WIJK_MIN_WONINGEN:
                continue
            v = verdeling(jaren)
            c = cbs.get(code, {})
            wijken.append({"code": code, "naam": naam, "woningen": v["woningen"],
                           "mediaan_bouwjaar": v["mediaan_bouwjaar"], "dominant": v["dominant"],
                           "voor_1945_pct": v["klassen"][0][2], "jaren30_pct": v["jaren30_pct"],
                           "koop_pct": c.get("koop_pct"), "eengezins_pct": c.get("eengezins_pct")})
        wijken.sort(key=lambda w: (w["mediaan_bouwjaar"] or 0, w["naam"]))
        res["wijken"] = wijken
    return p["slug"], res


# ---------------------------------------------------------------- buurten (seo-ronde 4)
# Middelgrote plaatsen hebben te weinig CBS-wijken (vaak maar één). Daar rekenen we per
# CBS-buurt: bouwjaren uit de BAG-punten binnen de buurtgrens, eigendom en woningtype uit CBS.
BUURT_MIN_INWONERS = 5000
BUURT_MAX_INWONERS = WIJK_MIN_INWONERS
BUURT_MIN_WONINGEN = 100


def cbs_buurt_rijen(gm):
    nr = gm[2:]
    d = get(CBS, {
        "$filter": f"startswith(WijkenEnBuurten,'BU{nr}')",
        "$select": ("WijkenEnBuurten,Woningvoorraad_35,PercentageEengezinswoning_40,"
                    "PercentageMeergezinswoning_45,Koopwoningen_47,HuurwoningenTotaal_48,"
                    "InBezitWoningcorporatie_49"),
        "$format": "json"}, f"cbsbu-{gm}.json")
    uit = {}
    for r in d["value"]:
        uit[r["WijkenEnBuurten"].strip()] = {
            "woningvoorraad": r["Woningvoorraad_35"], "koop_pct": r["Koopwoningen_47"],
            "huur_pct": r["HuurwoningenTotaal_48"], "corporatie_pct": r["InBezitWoningcorporatie_49"],
            "eengezins_pct": r["PercentageEengezinswoning_40"], "meergezins_pct": r["PercentageMeergezinswoning_45"],
        }
    return uit


def buurt_geoms(gm):
    d = get(WB, {"service": "WFS", "version": "2.0.0", "request": "GetFeature",
                 "typeNames": "wijkenbuurten:buurten", "outputFormat": "application/json",
                 "propertyName": "buurtcode,buurtnaam,gemeentecode,geom",
                 "filter": fes_eq("gemeentecode", gm)}, f"buurten-{gm}.json")
    uit = []
    for f in d["features"]:
        if not f.get("geometry"):
            continue
        rs = ringen(f["geometry"])
        uit.append((f["properties"]["buurtcode"], f["properties"]["buurtnaam"], rs, bbox(rs)))
    return uit


def plaats_buurten(p):
    wp = BAG_NAAM.get(p["slug"], p["naam"])
    pts = bag_woningen(wp)
    gm = GEMEENTECODE[p["gemeente"]]
    cbs = cbs_buurt_rijen(gm)
    buurten = []
    for code, naam, rs, (x0, y0, x1, y1) in buurt_geoms(gm):
        jaren = [j for x, y, j in pts if x0 <= x <= x1 and y0 <= y <= y1 and in_ringen(x, y, rs)]
        if len(jaren) < BUURT_MIN_WONINGEN:
            continue
        v = verdeling(jaren)
        c = cbs.get(code, {})
        buurten.append({"code": code, "naam": naam, "woningen": v["woningen"],
                        "mediaan_bouwjaar": v["mediaan_bouwjaar"], "dominant": v["dominant"],
                        "voor_1945_pct": v["klassen"][0][2], "voor_1975_pct": v["voor_1975_pct"],
                        "jaren_1975_1994_pct": v["jaren_1975_1994_pct"], "vanaf_2005_pct": v["vanaf_2005_pct"],
                        "koop_pct": c.get("koop_pct"), "corporatie_pct": c.get("corporatie_pct"),
                        "eengezins_pct": c.get("eengezins_pct")})
    buurten.sort(key=lambda b: (b["mediaan_bouwjaar"] or 0, b["naam"]))
    return p["slug"], buurten


def alleen_buurten():
    """Voegt 'buurten' toe aan de bestaande cijfers, zonder de rest opnieuw op te halen."""
    from plaats_cijfers import CIJFERS as uit
    doel = [p for p in PLAATSEN if BUURT_MIN_INWONERS <= p["inwoners"] < BUURT_MAX_INWONERS]
    with ThreadPoolExecutor(max_workers=4) as ex:
        for slug, buurten in ex.map(plaats_buurten, doel):
            if len(buurten) >= 3:
                uit[slug]["buurten"] = buurten
            print(f"  {slug}: {len(buurten)} buurten", file=sys.stderr)
    return uit


def main():
    if "--buurten" in sys.argv:
        from plaats_cijfers import META as oud
        return schrijf(alleen_buurten(), opgehaald=oud["opgehaald"])
    if "--alleen-monumenten" in sys.argv:
        # Snel bijwerken van alleen de RCE-velden; de rest blijft uit plaats_cijfers.py.
        from plaats_cijfers import CIJFERS as uit
        for p in PLAATSEN:
            rs = woonplaats_geom(BAG_NAAM.get(p["slug"], p["naam"]))
            c = uit[p["slug"]]
            c.pop("rijksmonumenten_gebouwd", None)
            c.update(monumenten(rs, p["naam"]))
        return schrijf(uit)
    alle = gezichten()
    with ThreadPoolExecutor(max_workers=6) as ex:
        uit = dict(ex.map(lambda p: plaats_cijfers(p, alle), PLAATSEN))
    for slug, buurten in (plaats_buurten(p) for p in PLAATSEN
                          if BUURT_MIN_INWONERS <= p["inwoners"] < BUURT_MAX_INWONERS):
        if len(buurten) >= 3:
            uit[slug]["buurten"] = buurten
    schrijf(uit)


def schrijf(uit, opgehaald=None):
    meta = {
        "opgehaald": opgehaald or datetime.date.today().isoformat(),
        "bronnen": {
            "bag": "Basisregistratie Adressen en Gebouwen (Kadaster), via PDOK, CC0",
            "cbs": "CBS, Kerncijfers wijken en buurten 2024 (85984NED), CC BY 4.0",
            "cbs_kaart": "CBS, Wijk- en buurtkaart 2024, via PDOK, CC BY 4.0",
            "rce": "Rijksdienst voor het Cultureel Erfgoed, Rijksmonumentenregister en geodata rijksmonumenten en beschermde gezichten, CC BY 4.0",
        },
        "klassen": [k[0] for k in KLASSEN],
    }
    pad = os.path.join(os.path.dirname(os.path.abspath(__file__)), "plaats_cijfers.py")
    with open(pad, "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""Gegenereerd door plaatsdata_ophalen.py — niet met de hand bewerken.\n\n'
                "Open data per plaats: bouwjaren (BAG), eigendom en woningtype (CBS),\n"
                'rijksmonumenten en beschermde gezichten (RCE). Zie META voor bronnen en peildatum."""\n\n')
        f.write("META = " + json.dumps(meta, ensure_ascii=False, indent=1) + "\n\n")
        f.write("CIJFERS = " + json.dumps(uit, ensure_ascii=False, indent=1).replace(": null", ": None")
                .replace(": true", ": True").replace(": false", ": False") + "\n")
    print(f"geschreven: {pad}", file=sys.stderr)


if __name__ == "__main__":
    main()
