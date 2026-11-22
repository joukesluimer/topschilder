# -*- coding: utf-8 -*-
"""Buurt- en wijkcijfers op de plaats-dienstpagina's (/schilder/{plaats}/{dienst}/). Seo-ronde 4.

Waarom: op de dienstpagina's van middelgrote plaatsen was maar zo'n 4% van de tekst uniek.
Dit blok zet per dienst de buurten (of wijken) van die plaats naast elkaar, met wat de
bouwjaren en het eigendom betekenen voor precies die klus. Elke plaats krijgt zo andere
buurtnamen, andere cijfers en per dienst een andere selectie en uitleg.

Regels (zoals in plaats_content.py):
- Alleen cijfers uit plaats_cijfers.py (BAG, CBS), met bron op de pagina.
- Geen claims over schilders, reviews of projecten.
- De uitleg per buurt volgt uit het mediane bouwjaar of het eigendom, niet uit aannames.
"""

from plaats_cijfers import CIJFERS, META
from plaats_content import _wijknaam, _nl, bronnen

JAAR = int(META["opgehaald"][:4])
MAX_RIJEN = 10


def _naam(b):
    n = _wijknaam(b["naam"]).replace(" - ", "-")
    if n.startswith("s "):  # CBS schrijft 's Heerenloo zonder apostrof
        n = "'" + n
    return n


def _gebieden(p):
    """(lijst, 'buurt'|'wijk') of (None, None)."""
    c = CIJFERS.get(p["slug"]) or {}
    if len(c.get("buurten") or []) >= 3:
        return c["buurten"], "buurt"
    if len(c.get("wijken") or []) >= 3:
        return c["wijken"], "wijk"
    return None, None


def _aantal_tussen(p, van, tot):
    b = CIJFERS[p["slug"]]["bag"]
    per = b["per_jaar_vanaf_1940"]
    n = sum(per[max(0, j - 1940)] for j in range(max(van, 1940), tot + 1) if 0 <= j - 1940 < len(per))
    if van < 1940:
        n += b["voor_1940"]
    return n


# ------------------------------------------------------------- uitleg per mediaan bouwjaar
def _buiten(med):
    if med < 1945:
        return "Veel oud houtwerk en details; meer voorwerk per kozijn"
    if med < 1975:
        return "Vaak originele kozijnen met veel oude verflagen; let op houtrot"
    if med < 1995:
        return "Tweede of derde grote beurt; kitnaden en onderdorpels nakijken"
    if med <= JAAR - 9:
        return "Hout meestal gezond; een beurt om de zes tot acht jaar houdt dat zo"
    if med <= JAAR - 6:
        return "Rond nu toe aan de eerste schilderbeurt na de bouw"
    return f"Nog jong; de eerste beurt valt rond {med + 6} tot {med + 8}"


def _binnen(med):
    if med < 1945:
        return "Hoge plafonds en oude pleisterlagen; meer voorwerk"
    if med < 1975:
        return "Soms nog behang of oude olieverf onder de verf; eerst hechting testen"
    if med < 1995:
        return "Vaak spachtelputz of structuurplafonds; glad stucen of strak sauzen"
    if med < 2015:
        return "Meestal vlakke wanden; gewoon sauswerk"
    return "Vaak nog kale wanden; reken op een voorstrijklaag"


def _spuit(med):
    if med < 1975:
        return "Oude paneeldeuren met veel kwastlagen; flink schuren voor het spuiten"
    if med < 1995:
        return "Vaak nog de originele opdekdeuren en kozijnen; spuiten geeft ze een strakke laag"
    if med < 2015:
        return "Deuren meestal fabrieksafgelakt; spuiten vooral bij een nieuwe kleur"
    return "Spuitwerk gaat hier vaker over kale wanden en plafonds (latex)"


def _behang(med):
    if med < 1975:
        return "Grote kans op oud behang, soms in lagen; verwijderen is een aparte post"
    if med < 1995:
        return "Vaak nog vinyl- of structuurbehang; eerst weghalen en de muur egaliseren"
    return "Meestal vlakke wanden; vliesbehang kan vaak direct op de voorbehandelde muur"


# ------------------------------------------------------------- per dienst: selectie, kolommen, tekst
def _config(slug):
    if slug == "buitenschilderwerk":
        return dict(sort=lambda b: b["mediaan_bouwjaar"], kop="Mediaan bouwjaar",
                    waarde=lambda b: str(b["mediaan_bouwjaar"]), uitleg=lambda b: _buiten(b["mediaan_bouwjaar"]),
                    titel="Buitenschilderwerk per {soort}")
    if slug == "houtrot-reparatie":
        return dict(sort=lambda b: -(b.get("voor_1975_pct") if b.get("voor_1975_pct") is not None else b["voor_1945_pct"]),
                    kop="Van vóór 1975",
                    waarde=lambda b: f"{b['voor_1975_pct']}%" if b.get("voor_1975_pct") is not None else f"{b['voor_1945_pct']}% vóór 1945",
                    uitleg=lambda b: ("Veel woningen op de leeftijd waarop houtrot het vaakst voorkomt"
                                      if (b.get("voor_1975_pct") or 0) >= 50 else
                                      "Gemengd: controleer vooral dorpels en kozijnhoeken"
                                      if (b.get("voor_1975_pct") or 0) >= 20 else
                                      "Vooral jongere woningen; houtrot is hier vaak klein en plaatselijk"),
                    titel="Houtrot: waar de oudste woningen staan")
    if slug == "binnenschilderwerk":
        return dict(sort=lambda b: b["mediaan_bouwjaar"], kop="Mediaan bouwjaar",
                    waarde=lambda b: str(b["mediaan_bouwjaar"]), uitleg=lambda b: _binnen(b["mediaan_bouwjaar"]),
                    titel="Binnenschilderwerk per {soort}")
    if slug == "spuitwerk":
        return dict(sort=lambda b: b["mediaan_bouwjaar"], kop="Mediaan bouwjaar",
                    waarde=lambda b: str(b["mediaan_bouwjaar"]), uitleg=lambda b: _spuit(b["mediaan_bouwjaar"]),
                    titel="Spuitwerk per {soort}")
    if slug == "behangen":
        return dict(sort=lambda b: b["mediaan_bouwjaar"], kop="Mediaan bouwjaar",
                    waarde=lambda b: str(b["mediaan_bouwjaar"]), uitleg=lambda b: _behang(b["mediaan_bouwjaar"]),
                    titel="Behangen per {soort}")
    if slug == "zakelijk-schilderwerk":
        return dict(sort=lambda b: (b.get("koop_pct") if b.get("koop_pct") is not None else 101),
                    kop="Koopwoningen",
                    waarde=lambda b: f"{b['koop_pct']}%" if b.get("koop_pct") is not None else "onbekend",
                    uitleg=lambda b: ("Veel huur: onderhoud loopt hier vaak via corporatie of verhuurder"
                                      if (b.get("koop_pct") if b.get("koop_pct") is not None else 100) < 50 else
                                      "Vooral koop; bij appartementen regelt de VvE het buitenwerk"),
                    titel="Huur, koop en VvE per {soort}")
    return None


def _kern_zin(d, p, rijen, soort):
    """Eén of twee zinnen met de belangrijkste uitkomst voor deze dienst."""
    naam, slug = p["naam"], d["slug"]
    oudst = min(rijen, key=lambda b: b["mediaan_bouwjaar"])
    jongst = max(rijen, key=lambda b: b["mediaan_bouwjaar"])
    mv = "buurten" if soort == "buurt" else "wijken"
    if slug == "buitenschilderwerk":
        n = _aantal_tussen(p, JAAR - 8, JAAR - 6)
        return (f"In {_naam(oudst)} is de helft van de woningen van vóór {oudst['mediaan_bouwjaar']}, in {_naam(jongst)} van na "
                f"{jongst['mediaan_bouwjaar']}. Volgens de BAG zijn er in {naam} {_nl(n)} woningen gebouwd tussen {JAAR - 8} en {JAAR - 6}: "
                f"die zijn nu zes tot acht jaar oud, de leeftijd waarop in de fabriek afgelakte kozijnen hun eerste beurt krijgen.")
    if slug == "houtrot-reparatie":
        n = _aantal_tussen(p, 1000, 1974)
        top = rijen[0]
        return (f"{_nl(n)} woningen in {naam} zijn van vóór 1975 (BAG). Het grootste aandeel oudere woningen staat in "
                f"{_naam(top)}" + (f": {top['voor_1975_pct']}% is daar van vóór 1975." if top.get("voor_1975_pct") is not None else ".")
                + " Bij die leeftijd zitten er vaak nog originele houten kozijnen in, en daar begint houtrot meestal: in onderdorpels en kozijnhoeken.")
    if slug == "binnenschilderwerk":
        n = _aantal_tussen(p, 2015, JAAR)
        return (f"Sinds 2015 zijn er in {naam} {_nl(n)} woningen bijgebouwd (BAG); daar gaat het binnen vaak om het eerste sauswerk op kale wanden. "
                f"In {_naam(oudst)}, met een mediaan bouwjaar van {oudst['mediaan_bouwjaar']}, zit het werk eerder in voorwerk en herstel.")
    if slug == "spuitwerk":
        n = _aantal_tussen(p, 1975, 1994)
        return (f"{_nl(n)} woningen in {naam} zijn gebouwd tussen 1975 en 1994 (BAG). In woningen van die leeftijd zitten vaak nog de originele "
                f"binnendeuren en kozijnen, en daar is spuiten een manier om ze strak te krijgen zonder ze te vervangen.")
    if slug == "behangen":
        n = _aantal_tussen(p, 1000, 1974)
        return (f"{_nl(n)} woningen in {naam} zijn van vóór 1975 (BAG). Hoe ouder de woning, hoe groter de kans dat er oud behang "
                f"weg moet voordat er nieuw op kan. Dat zie je terug in de verschillen tussen de {mv} hieronder.")
    if slug == "zakelijk-schilderwerk":
        met = [b for b in rijen if b.get("koop_pct") is not None]
        if not met:
            return ""
        laag = min(met, key=lambda b: b["koop_pct"])
        return (f"In {_naam(laag)} is {laag['koop_pct']}% van de woningen een koopwoning; de rest wordt verhuurd. "
                f"Waar veel huurwoningen staan, besteden corporaties en verhuurders het schilderwerk meestal per complex uit, volgens een meerjarenonderhoudsplan.")
    return ""


def buurt_blok(d, p):
    """HTML-blok voor /schilder/{plaats}/{dienst}/. Leeg als er geen buurt- of wijkcijfers zijn."""
    gebieden, soort = _gebieden(p)
    cfg = _config(d["slug"])
    if not gebieden or not cfg:
        return ""
    rijen = [b for b in gebieden if b.get("mediaan_bouwjaar")]
    if len(rijen) > MAX_RIJEN:  # alleen de grootste buurten, daarna in de volgorde van de dienst
        rijen = sorted(rijen, key=lambda b: -b["woningen"])[:MAX_RIJEN]
    rijen = sorted(rijen, key=cfg["sort"])
    mv = "buurten" if soort == "buurt" else "wijken"
    tabel = "".join(f"<tr><td>{_naam(b)}</td><td class=\"num\">{_nl(b['woningen'])}</td>"
                    f"<td class=\"num\">{cfg['waarde'](b)}</td><td>{cfg['uitleg'](b)}</td></tr>" for b in rijen)
    extra = (f" We tonen de {MAX_RIJEN} {mv} met de meeste woningen." if len(gebieden) > MAX_RIJEN else "")
    c = CIJFERS[p["slug"]]
    return f"""<h3>{cfg['titel'].format(soort=soort)} in {p['naam']}</h3>
  <p>{_kern_zin(d, p, rijen, soort)}</p>
  <div class="tablewrap"><table class="pc-wijken"><thead><tr><th scope="col">{soort.capitalize()} (CBS)</th><th scope="col" class="num">Woningen</th><th scope="col" class="num">{cfg['kop']}</th><th scope="col">Wat dat betekent</th></tr></thead><tbody>{tabel}</tbody></table></div>
  <p><small>Woningen en bouwjaren per {soort} geteld uit de BAG-adressen binnen de CBS-{soort}grens; {mv} met minder dan 100 woningen tellen niet mee.{extra} Het mediane bouwjaar is het jaar waarvoor en waarna evenveel woningen zijn gebouwd.</small></p>
  {bronnen(c, met_wijken=True)}"""


def buurt_faq(d, p):
    """Twee lokale vragen met antwoorden uit de cijfers, of [] als die er niet zijn."""
    gebieden, soort = _gebieden(p)
    c = CIJFERS.get(p["slug"])
    if not gebieden or not c:
        return []
    naam, b = p["naam"], c["bag"]
    rijen = [g for g in gebieden if g.get("mediaan_bouwjaar")]
    oudst = min(rijen, key=lambda g: g["mediaan_bouwjaar"])
    jongst = max(rijen, key=lambda g: g["mediaan_bouwjaar"])
    mv = "buurt" if soort == "buurt" else "wijk"
    vragen = [(f"Hoe oud zijn de woningen in {naam}?",
               f"Volgens de BAG staan er in {naam} {_nl(b['woningen'])} woningen. De helft is gebouwd vóór {b['mediaan_bouwjaar']}. "
               f"De oudste {mv} is {_naam(oudst)} (helft van vóór {oudst['mediaan_bouwjaar']}), de jongste {_naam(jongst)} (helft van na {jongst['mediaan_bouwjaar']}).")]
    slug = d["slug"]
    if slug == "buitenschilderwerk":
        n = _aantal_tussen(p, JAAR - 8, JAAR - 6)
        vragen.append((f"Hoeveel woningen in {naam} zijn toe aan hun eerste buitenbeurt?",
                       f"{_nl(n)} woningen in {naam} zijn gebouwd tussen {JAAR - 8} en {JAAR - 6} (BAG). Kozijnen die in de fabriek zijn afgelakt, "
                       "krijgen meestal na zes tot acht jaar hun eerste schilderbeurt."))
    elif slug == "houtrot-reparatie":
        n = _aantal_tussen(p, 1000, 1974)
        vragen.append((f"Hoeveel woningen in {naam} zijn ouder dan vijftig jaar?",
                       f"{_nl(n)} woningen in {naam} zijn van vóór 1975, volgens de BAG. Bij die leeftijd is de kans op houtrot in dorpels en kozijnhoeken het grootst."))
    elif slug in ("binnenschilderwerk", "spuitwerk"):
        n = _aantal_tussen(p, 2015, JAAR)
        vragen.append((f"Hoeveel nieuwbouw staat er in {naam}?",
                       f"Sinds 2015 zijn er in {naam} {_nl(n)} woningen bijgekomen (BAG). Bij nieuwbouw gaat het binnen vaak om sauzen of latex spuiten op kale wanden, met een voorstrijklaag."))
    elif slug == "behangen":
        n = _aantal_tussen(p, 1000, 1974)
        vragen.append((f"Moet in {naam} vaak eerst oud behang weg?",
                       f"In oudere woningen wel vaker. {_nl(n)} woningen in {naam} zijn van vóór 1975 (BAG); daar zit vaak nog oud of overgeschilderd behang."))
    elif slug == "zakelijk-schilderwerk":
        e = c.get("cbs_kern") if (c.get("cbs_kern") or {}).get("corporatie_pct") is not None else c.get("cbs_gemeente") or {}
        if e.get("corporatie_pct") is not None:
            vragen.append((f"Hoeveel huurwoningen zijn er in {naam}?",
                           f"Volgens het CBS is in {e.get('naam', naam)} {e['huur_pct']}% van de woningen een huurwoning, waarvan {e['corporatie_pct']}% van een corporatie. "
                           "Die laten hun schilderwerk meestal per complex uitvoeren."))
    return vragen
