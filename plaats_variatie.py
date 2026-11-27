# -*- coding: utf-8 -*-
"""Data-gestuurde variatie voor alle plaatspagina's en plaats-dienstpagina's (lokale ronde).

Vervangt algemene vragen en blokken, die op alle 35 plaatsen hetzelfde waren, door vragen en
antwoorden die uit de open data van die plaats volgen (BAG, CBS, RCE in plaats_cijfers.py).
De formulering hangt af van wat de cijfers laten zien, dus twee plaatsen lezen niet hetzelfde.
Geen claims over schilders, reviews of aantallen bedrijven.
"""

import re

from data import lokale_prijs, DIENST_BY_SLUG
from plaats_cijfers import CIJFERS, META
from plaats_content import POLDER, POLDER_VAN, monumenten_telling, eigendom, rangorde

JAAR = int(META["opgehaald"][:4])

# typisch aantal kozijnen per woningtype, zelfde aannames als TYPISCHE_KLUS in build.py
KOZIJNEN = {"klein": 5, "midden": 9, "groot": 15}


def _nl(n):
    return f"{n:,}".replace(",", ".")


def _eur(n):
    return "€" + _nl(int(round(n)))


def _naam(r):
    return re.sub(r"^Wijk \d+\s*", "", r["naam"]).strip() or r["naam"]


def _gebieden(c):
    w = c.get("wijken") or []
    if len(w) >= 3:
        return w, "wijk"
    b = c.get("buurten") or []
    if len(b) >= 3:
        return b, "buurt"
    return [], None


def _grootte(p):
    w = p["woningmix"].lower()
    if "appartement" in w and "eengezins" not in w and "rij" not in w:
        return "klein", "een appartement of kleine woning"
    if any(x in w for x in ("vrijstaand", "villa", "ruime", "boerderij")):
        return "groot", "een ruime of vrijstaande woning"
    return "midden", "een gemiddelde eengezinswoning"


# ---------------------------------------------------------------- vragen voor /schilder/<plaats>/
def vraag_leeftijd(p, c):
    b = c["bag"]
    voor45 = b["klassen"][0][2]
    jong = b["vanaf_2005_pct"]
    oudste = b.get("oudste_bouwjaar")
    if p["slug"] in POLDER_VAN:
        polder, jaar = POLDER[POLDER_VAN[p["slug"]]]
        kern = (f"Jong, zoals overal in de {polder}: die viel in {jaar} droog. De helft van de {_nl(b['woningen'])} woningen "
                f"is van vóór {b['mediaan_bouwjaar']}, de andere helft daarna.")
    elif voor45 >= 20:
        kern = (f"Relatief oud: {voor45}% van de {_nl(b['woningen'])} woningen is van vóór 1945"
                + (f", en het oudste pand in de BAG heeft bouwjaar {oudste}." if oudste and oudste < 1700 else ".")
                + f" De helft is van vóór {b['mediaan_bouwjaar']}.")
    elif jong >= 30:
        kern = (f"Vrij jong: {jong}% van de {_nl(b['woningen'])} woningen is in 2005 of later gebouwd. "
                f"De helft is van na {b['mediaan_bouwjaar']}.")
    else:
        kern = (f"Gemengd. De grootste groep van de {_nl(b['woningen'])} woningen komt uit {b['dominant']}, "
                f"en de helft is van vóór {b['mediaan_bouwjaar']}.")
    return (f"Hoe oud zijn de huizen in {p['naam']}?", f"{kern} {rangorde(p)} Bron: BAG.")


def vraag_eerst(p, c):
    rijen, soort = _gebieden(c)
    if not rijen:
        return None
    rijen = [r for r in rijen if r.get("mediaan_bouwjaar") and r["woningen"] >= 150
             and not re.search(r"verspreide|buitengebied|industrie|bedrijven", r["naam"], re.I)]
    if len(rijen) < 2:
        return None
    oud = min(rijen, key=lambda r: r["mediaan_bouwjaar"])
    # gebied waar de mediane woning precies 6 tot 8 jaar oud is (eerste beurt), of 30-50 jaar (keuze: schilderen of vervangen)
    eerste = [r for r in rijen if 6 <= JAAR - r["mediaan_bouwjaar"] <= 10]
    keuze = [r for r in rijen if 30 <= JAAR - r["mediaan_bouwjaar"] <= 50]
    delen = [f"De oudste {soort} is {_naam(oud)}: daar is de helft van de {_nl(oud['woningen'])} woningen van vóór "
             f"{oud['mediaan_bouwjaar']}. Daar zit het meeste oude houtwerk en de meeste kans op houtrot."]
    if eerste:
        r = max(eerste, key=lambda r: r["woningen"])
        delen.append(f"In {_naam(r)} (mediaan {r['mediaan_bouwjaar']}) zijn veel huizen toe aan hun eerste echte buitenbeurt.")
    if keuze:
        r = max(keuze, key=lambda r: r["woningen"])
        delen.append(f"In {_naam(r)} (mediaan {r['mediaan_bouwjaar']}) staan veel huizen van 30 tot 50 jaar oud: "
                     f"de leeftijd waarop je kiest tussen nog een keer goed schilderen of de kozijnen vervangen.")
    return (f"Welke {soort} in {p['naam']} is het eerst aan schilderwerk toe?", " ".join(delen) + " Bron: BAG en CBS.")


def vraag_vergunning(p, c):
    n, _ = monumenten_telling(c)
    gez = c.get("beschermde_gezichten") or []
    if gez:
        g = " en ".join(gez) if len(gez) <= 2 else ", ".join(gez[:-1]) + " en " + gez[-1]
        a = (f"Soms wel. {p['naam']} heeft {_nl(n)} gebouwde rijksmonumenten en een rijksbeschermd gezicht ({g}). "
             f"Woon je in een monument of binnen dat gezicht, vraag dan bij de gemeente {p['gemeente']} na of een andere kleur mag. "
             f"Dezelfde kleur opnieuw aanbrengen is gewoon onderhoud.")
    elif n >= 5:
        a = (f"Alleen als je in een monument woont. {p['naam']} heeft geen rijksbeschermd stads- of dorpsgezicht, maar wel "
             f"{_nl(n)} gebouwde rijksmonumenten. Voor een gewone woning mag je de kleur meestal zelf kiezen; check wel de "
             f"welstandsregels van de gemeente {p['gemeente']}.")
    elif n:
        a = (f"Meestal niet. {p['naam']} heeft geen beschermd gezicht en {'maar één gebouwd rijksmonument' if n == 1 else f'maar {n} gebouwde rijksmonumenten'}. "
             f"Bij een gewone woning kies je de kleur zelf, binnen de welstandsregels van de gemeente {p['gemeente']}.")
    else:
        a = (f"Meestal niet. Volgens de Rijksdienst voor het Cultureel Erfgoed staat er in {p['naam']} geen gebouwd rijksmonument "
             f"en is er geen beschermd gezicht. Kijk voor de zekerheid of je gemeente welstandsregels heeft voor jouw straat.")
    return (f"Heb ik in {p['naam']} een vergunning nodig voor een andere kleur?", a + " Bron: RCE.")


def vraag_kosten_huis(p, c):
    d = DIENST_BY_SLUG["buitenschilderwerk"]
    van, tot = lokale_prijs(d, p)
    g, omschrijving = _grootte(p)
    n = KOZIJNEN[g]
    return (f"Wat kost het buitenschilderwerk van een huis in {p['naam']}?",
            f"In {p['naam']} gaat het vooral om {p['woningmix']}. Voor {omschrijving} met zo'n {n} kozijnen kom je met "
            f"de richtprijs voor {p['provincie']} ({_eur(van)} tot {_eur(tot)} per kozijn) uit op {_eur(n * van)} tot {_eur(n * tot)}, "
            f"inclusief verf en 9% btw. Houtrot, een steiger of boeidelen komen daar nog bij.")


def vraag_zelf_regelen(p, c):
    e, waar = eigendom(c)
    if e.get("koop_pct") is None:
        return None
    if e["meergezins_pct"] >= 35:
        kern = (f"Lang niet altijd. In {waar} is {e['meergezins_pct']}% van de woningen een appartement of andere meergezinswoning. "
                f"Daar regelt de VvE het buitenschilderwerk, en doe je als bewoner vooral het binnenwerk.")
    elif e["corporatie_pct"] >= 30:
        kern = (f"Dat hangt ervan af. In {waar} huurt {e['corporatie_pct']}% van een corporatie; die regelt het buitenschilderwerk. "
                f"Met {e['koop_pct']}% koopwoningen regelt toch een groot deel van de eigenaren het zelf.")
    else:
        kern = (f"Meestal wel. In {waar} is {e['koop_pct']}% een koopwoning en {e['eengezins_pct']}% een eengezinswoning. "
                f"Dan ben je als eigenaar zelf aan zet, voor binnen én buiten.")
    return (f"Regel ik in {p['naam']} het buitenschilderwerk zelf?", kern + " Bron: CBS.")


def plaats_faq(p, algemeen):
    """Lokale vragen uit de cijfers, aangevuld met maximaal twee algemene vragen."""
    c = CIJFERS.get(p["slug"])
    if not c:
        return algemeen
    vragen = [f(p, c) for f in (vraag_leeftijd, vraag_eerst, vraag_vergunning, vraag_kosten_huis, vraag_zelf_regelen)]
    return [v for v in vragen if v] + [_algemeen_lokaal(p, c, v) for v in algemeen[:2]]


def _algemeen_lokaal(p, c, vraag):
    """Ronde plaatsen 2: de twee algemene vragen met een lokaal cijfer erin (BAG, CBS)."""
    v, a = vraag
    b = c["bag"]
    if v.startswith("Geldt het lage btw-tarief"):
        per = b["per_jaar_vanaf_1940"]
        nieuw = sum(per[2025 - 1940:]) if len(per) > 2025 - 1940 else 0
        if nieuw:
            a = (f"Ja, voor schilderwerk aan een woning die langer dan twee jaar in gebruik is, inclusief de verf. "
                 f"Van de {_nl(b['woningen'])} woningen in {p['naam']} zijn er volgens de BAG {_nl(nieuw)} gebouwd in 2025 of "
                 f"later; daar geldt nog 21%. Voor werk dat verder gaat dan schilderen, zoals nieuw hout inzetten, ook. "
                 f"Staat er 21% over het hele bedrag, vraag dan waarom.")
        return (f"Geldt in {p['naam']} het lage btw-tarief van 9%?", a)
    if v.startswith("Hoeveel schilders"):
        e = c.get("cbs_kern") or c.get("cbs_gemeente") or {}
        if e.get("koop_pct") is not None:
            a = (f"Maximaal drie. Dat is genoeg om te vergelijken, zonder dat je de hele week wordt gebeld. In {p['naam']} "
                 f"is {e['koop_pct']}% van de woningen een koophuis (CBS). Huur je, overleg dan eerst met de verhuurder. "
                 f"Reageren er minder dan drie, dan hebben op dat moment niet meer schilders ruimte.")
    return (v, a)


# ---------------------------------------------------------------- vraag voor /schilder/<plaats>/<dienst>/
def dienst_vraag(d, p):
    """Eén lokale vraag per dienst, in plaats van de algemene vraag over het werkgebied."""
    c = CIJFERS.get(p["slug"])
    if not c:
        return None
    b = c["bag"]
    med = b["mediaan_bouwjaar"]
    leeftijd = JAAR - med
    voor45 = b["klassen"][0][2]
    voor75 = b["voor_1975_pct"]
    groei = b["jaren_1975_1994_pct"]
    jong = b["vanaf_2005_pct"]
    naam, slug = p["naam"], d["slug"]
    if slug == "buitenschilderwerk":
        return (f"Hoeveel schilderbeurten heeft een gemiddeld huis in {naam} al gehad?",
                f"De mediane woning in {naam} is van {med} en dus {leeftijd} jaar oud. Bij een beurt om de zes tot acht jaar zijn dat er "
                f"zo'n {leeftijd // 8} tot {leeftijd // 6}. "
                + ("Na zoveel beurten zit er een dik verfpakket op het hout; laat de schilder kijken of afbijten of afbranden nodig is."
                   if leeftijd >= 40 else
                   "Het hout is dan vaak nog gezond, maar kitnaden en onderdorpels verdienen aandacht." if leeftijd >= 20 else
                   "Veel kozijnen zijn nog fabrieksmatig afgelakt en hebben weinig voorwerk nodig.")
                + " Bron: BAG.")
    if slug == "houtrot-reparatie":
        return (f"Hoeveel huizen in {naam} lopen extra risico op houtrot?",
                f"Houtrot zit vooral in oude houten kozijnen. In {naam} is {voor75}% van de woningen van vóór 1975"
                + (f", waarvan {voor45}% zelfs van vóór 1945" if voor45 >= 5 else "")
                + (f". Nog eens {groei}% komt uit 1975 tot 1995; ook daar kan na dertig jaar vocht achter kapotte kitnaden zitten."
                   if groei >= 20 else ".")
                + " Of jouw kozijnen nog origineel zijn, zie je aan het profiel en aan het aantal verflagen. Bron: BAG.")
    if slug == "binnenschilderwerk":
        if groei >= 30:
            a = (f"{groei}% van de woningen in {naam} komt uit 1975 tot 1995. Toen werd spachtelputz veel gebruikt. Wil je gladde muren, "
                 f"dan komt er eerst stucwerk of glasvlies op; overschilderen kan ook, maar de structuur blijft.")
        elif voor45 >= 15:
            a = (f"{voor45}% van de woningen in {naam} is van vóór 1945. Daar zijn het eerder oude pleisterlagen, scheurtjes en hoge plafonds "
                 f"die tijd kosten. Een schilder vult en schuurt dan eerst flink.")
        else:
            a = (f"De mediane woning in {naam} is van {med}. Bij die leeftijd zijn de muren meestal al eens geschilderd of behangen; "
                 f"de prijs hangt dan vooral af van hoeveel herstel er nodig is.")
        return (f"Zijn de muren in huizen in {naam} vaak glad of met structuur?", a + " Bron: BAG.")
    if slug == "spuitwerk":
        return (f"Zitten er in {naam} nog veel originele binnendeuren?",
                f"Dat kan niemand uit de cijfers halen, maar het bouwjaar geeft een hint. {voor75 + groei}% van de woningen in {naam} is van vóór 1995. "
                f"In huizen van die leeftijd zitten vaak nog de originele opdekdeuren met meerdere lagen kwastverf. Spuiten maakt die weer strak. "
                + (f"In de {jong}% woningen van 2005 of later gaat het vaker om latex spuiten van kale wanden." if jong >= 15 else "")
                + " Bron: BAG.")
    if slug == "behangen":
        return (f"Moet er in {naam} vaak oud behang af?",
                (f"Vaak wel: {voor75}% van de woningen is van vóór 1975, en daar zit regelmatig behang in meerdere lagen. Strippen is dan een aparte post."
                 if voor75 >= 40 else
                 f"Minder vaak dan in een oude stad: {100 - voor75}% van de woningen is van 1975 of later. Toch is strippen bij een eerdere bewoner met behang een aparte post.")
                + " Bron: BAG.")
    if slug == "zakelijk-schilderwerk":
        e, waar = eigendom(c)
        if e.get("corporatie_pct") is None:
            return None
        return (f"Hoeveel woningen in {naam} vallen onder een corporatie of VvE?",
                f"In {waar} is {e['corporatie_pct']}% van de woningen van een corporatie en {e['meergezins_pct']}% een appartement of andere "
                f"meergezinswoning. Corporaties en VvE's plannen schilderwerk meestal via een meerjarenonderhoudsplan, met een vaste cyclus per complex. Bron: CBS.")
    return None
