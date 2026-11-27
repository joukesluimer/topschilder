# -*- coding: utf-8 -*-
"""Data-gestuurde variatie in de vaste blokken van /schilder/<plaats>/ (ronde plaatsen 2).

De vaste blokken (dienstkaarten, 'Zo werkt het', de prijsalinea, de buurplaatsen en de slot-CTA)
stonden op alle 35 plaatspagina's woord voor woord hetzelfde. Hier krijgen ze per plaats een
formulering die volgt uit de eigen cijfers van die plaats: bouwjaren en wijken (BAG/CBS),
eigendom en woningtype (CBS) en monumenten (RCE), allemaal uit plaats_cijfers.py.

Regels:
  - geen nieuwe claims over schilders, reviews of aantallen bedrijven;
  - de belofte blijft overal gelijk: maximaal drie offertes, gratis, je zit nergens aan vast;
  - alles wat hier staat, is af te leiden uit plaats_cijfers.py of data.py.

Werkt als nabewerking op de HTML: build.py roept varieer_plaats(p, body) aan. Elke vervanging
zoekt een exacte zin; staat die zin er niet (meer), dan gebeurt er niets.
"""

import re

from data import DIENSTEN, PRIJSINDEX, lokale_prijs
from plaats_cijfers import CIJFERS, META

JAAR = int(META["opgehaald"][:4])


def _nl(n):
    return f"{n:,}".replace(",", ".")


def _eur(n):
    return "€" + _nl(int(round(n)))


def _naam(r):
    return re.sub(r"^Wijk \d+\s*", "", r["naam"]).strip() or r["naam"]


def _kort(naam):
    """Lange CBS-namen ('Appel, Driedorp, Kruishaar en ...') inkorten tot het eerste deel."""
    return re.split(r",| en ", naam)[0].strip()


def feiten(p):
    """Alles wat de vaste blokken nodig hebben, uit de open data van de plaats."""
    c = CIJFERS.get(p["slug"])
    if not c:
        return None
    b = c["bag"]
    e = c.get("cbs_kern") or c.get("cbs_gemeente") or {}
    w = c.get("wijken") or []
    rijen, soort = (w, "wijk") if len(w) >= 3 else (c.get("buurten") or [], "buurt")
    rijen = [r for r in rijen if r.get("mediaan_bouwjaar") and r.get("woningen", 0) >= 50]
    groot = sorted(rijen, key=lambda r: -r["woningen"])[:8]
    op_jaar = sorted(groot, key=lambda r: r["mediaan_bouwjaar"])
    mon = c.get("rijksmonumenten", 0) - c.get("rijksmonumenten_archeologisch", 0)
    return dict(
        woningen=b["woningen"], med=b["mediaan_bouwjaar"], dominant=b["dominant"],
        voor45=b["klassen"][0][2], voor75=b["voor_1975_pct"], groei=b["jaren_1975_1994_pct"],
        jong=b["vanaf_2005_pct"], oudste=b.get("oudste_bouwjaar"),
        koop=e.get("koop_pct"), corp=e.get("corporatie_pct"), eengezins=e.get("eengezins_pct"),
        meergezins=e.get("meergezins_pct"),
        soort=soort if op_jaar else None,
        oud=_kort(_naam(op_jaar[0])) if op_jaar else None,
        oud_jaar=op_jaar[0]["mediaan_bouwjaar"] if op_jaar else None,
        jong_g=_kort(_naam(op_jaar[-1])) if len(op_jaar) > 1 else None,
        jong_jaar=op_jaar[-1]["mediaan_bouwjaar"] if len(op_jaar) > 1 else None,
        grootste=_kort(_naam(groot[0])) if groot else None,
        mon=mon, gezichten=c.get("beschermde_gezichten") or [],
        idx=PRIJSINDEX.get(p["provincie"], 1.0),
    )


# ---------------------------------------------------------------- per blok
def _lead_diensten(p, f):
    n = p["naam"]
    if f["voor45"] >= 25:
        return (f"Een kwart of meer van de huizen in {n} is van vóór 1945. Daar zit het werk vaak in oude kozijnen en "
                f"verflagen. Kies hieronder je klus voor de richtprijs en een aanvraag.")
    if f["jong"] >= 35:
        return (f"Veel woningen in {n} zijn na 2005 gebouwd. Daar gaat het vaak om een eerste beurt of om binnenwerk. "
                f"Per klus zie je de richtprijs en kun je direct aanvragen.")
    if f["groei"] >= 35:
        return (f"In {n} komt een groot deel van de huizen uit 1975 tot 1995. Die zijn toe aan hun derde of vierde "
                f"buitenbeurt. Open een klus voor prijzen en een aanvraag.")
    return (f"De woningen in {n} lopen in bouwjaar sterk uiteen. Open een klus voor de richtprijs in {p['provincie']} "
            f"en vraag daar meteen offertes aan.")


def _kaart(d, p, f):
    """Korte tekst op de dienstkaart, gekoppeld aan de woningvoorraad."""
    s = d["slug"]
    oud, jong = f["oud"], f["jong_g"]
    if s == "binnenschilderwerk":
        if oud and jong and oud != jong:
            return f"Muren, plafonds en deuren, in een oud huis in {oud} of nieuwbouw in {jong}"
        return "Muren, plafonds, deuren en trappen, ook bij oude pleisterlagen"
    if s == "buitenschilderwerk":
        if (f["eengezins"] or 0) >= 80:
            return f"Kozijnen en boeidelen; {f['eengezins']}% van de woningen hier is een eengezinshuis"
        if (f["meergezins"] or 0) >= 35:
            return f"Kozijnen en gevels; bij de {f['meergezins']}% appartementen loopt dit vaak via de VvE"
        return f"Kozijnen, gevels, boeidelen en dakkapellen van de {_nl(f['woningen'])} woningen"
    if s == "houtrot-reparatie":
        if f["voor75"] >= 40:
            return f"Rot in oude kozijnen uitfrezen of vervangen; {f['voor75']}% is van vóór 1975"
        return "Zachte plekken in dorpels en hoeken uitfrezen, vullen of vervangen"
    if s == "spuitwerk":
        if f["groei"] >= 25:
            return "Binnendeuren uit de jaren 80 en 90, keukenkastjes en kozijnen strak spuiten"
        return "Deuren, keukenfronten en kozijnen glad en strak spuiten"
    if s == "behangen":
        if f["voor75"] >= 50:
            return "Oud behang strippen en nieuw vlies- of glasvezelbehang plakken"
        return "Vliesbehang, glasvezel, fotobehang en wandbekleding"
    if s == "zakelijk-schilderwerk":
        if (f["corp"] or 0) >= 30:
            return f"Kantoren, scholen en complexen; {f['corp']}% van de woningen is van een corporatie"
        return "Kantoren, winkels, VvE's en bedrijfspanden, buiten werktijd als het moet"
    return d["kort"]


def _stappen(p, f):
    """Lead en drie stappen van 'Zo werkt het', met wat voor deze plaats handig is om te noemen."""
    n = p["naam"]
    if f["soort"] and f["grootste"]:
        lead = (f"Of je nu in {f['grootste']} woont of in een andere {f['soort']} van {n}: je vult één keer je klus in "
                f"en krijgt prijzen terug van schilders in de buurt.")
    else:
        lead = f"Eén aanvraag voor {n}, meerdere prijzen terug. Bellen langs bedrijven is niet nodig."
    if f["med"] < 1960:
        stap1 = ("Vier vragen over je klus en je huis. Noem het bouwjaar als je dat weet: bij oude kozijnen rekent een "
                 "schilder anders.")
    elif f["med"] >= 1995:
        stap1 = ("Vier vragen over je klus en je huis. Is het je eerste schilderbeurt na de oplevering? Zet dat erbij, "
                 "dan weet de schilder dat er weinig voorwerk is.")
    else:
        stap1 = ("Vier vragen over je klus, het pand en wanneer het moet. Weet je wanneer er voor het laatst is "
                 "geschilderd? Dat helpt bij de prijs.")
    waar = f", van {f['oud']} tot {f['jong_g']}," if f["oud"] and f["jong_g"] and f["oud"] != f["jong_g"] else ""
    stap2 = (f"We sturen je aanvraag naar maximaal drie schilders die in {n}{waar} werken, dit soort klus doen en nu "
             f"ruimte hebben.")
    if (f["koop"] or 0) >= 70:
        stap3 = ("De offertes komen rechtstreeks van de schilders. Jij beslist als eigenaar; past het niet, dan zeg "
                 "je nee en zit je nergens aan vast.")
    else:
        stap3 = ("Je krijgt de offertes rechtstreeks. Huur je, overleg dan eerst met de verhuurder wie wat betaalt. "
                 "Nee zeggen kan altijd.")
    return lead, stap1, stap2, stap3


def _uurtarief(p, f):
    van, tot = lokale_prijs(next(d for d in DIENSTEN if d["slug"] == "buitenschilderwerk"), p)
    if f["idx"] >= 1.03:
        return (f"Een offerte noemt dat uurtarief zelden. Meestal krijg je een prijs per kozijn of per m². "
                f"Voor buitenwerk komt dat hier uit op ongeveer {_eur(van)} tot {_eur(tot)} per kozijn.")
    if f["idx"] <= 0.97:
        return (f"Op de offerte zie je dat uurtarief meestal niet terug. Schilders rekenen per stuk of per m²; "
                f"een kozijn buiten kost in deze regio ongeveer {_eur(van)} tot {_eur(tot)}.")
    return (f"Dat uurtarief staat zelden op een offerte. De meeste schilders geven een vaste prijs per kozijn of "
            f"per m², rond {_eur(van)} tot {_eur(tot)} per kozijn buiten.")


def _tabel_noot(p, f):
    if f["voor75"] >= 50:
        extra = "Bij oude kozijnen met veel lagen verf kom je eerder aan de bovenkant."
    elif f["jong"] >= 30:
        extra = "Bij jonge woningen met gave kozijnen zit je vaker aan de onderkant."
    else:
        extra = "De staat van het hout en de bereikbaarheid bepalen waar je uitkomt."
    return (f"<p><small>Richtprijzen voor {p['provincie']}, met materiaal en btw (behalve waar excl. btw staat). "
            f"{extra} Vraag meerdere offertes aan.</small></p>")


def _woningmix(p, f):
    if (f["eengezins"] or 0) >= 75:
        return ("Bij eengezinswoningen heeft elk huis zijn eigen kozijnen, deuren en boeidelen. Een steiger is vaak "
                "alleen nodig voor de dakkapel of de kopgevel.")
    if (f["meergezins"] or 0) >= 30:
        return ("Bij appartementen beslist meestal de VvE over het buitenwerk. Binnen regel je het zelf, buiten "
                "gaat het per blok en vaak met een hoogwerker.")
    return ("Samen bepalen ze hoeveel kozijnen een huis heeft, of er een steiger moet komen en welke gevel als "
            "eerste aan de beurt is.")


def _buren(p, f):
    if p["inwoners"] >= 40000:
        return (f"Een schilder rijdt voor een klus van een paar dagen vaak twintig tot dertig kilometer. Ook "
                f"schilders uit deze plaatsen in de buurt kunnen dus een offerte geven:")
    return "Veel schilders werken in een straal van 20 tot 30 kilometer. Zoek je in een plaats in de buurt?"


def _cta(p, f):
    n = p["naam"]
    if f["mon"] >= 50:
        return (f"Monument of gewoon huis in {n}? Vul het formulier in. Je krijgt vrijblijvend offertes van maximaal "
                f"drie schilders die hier werken.")
    if f["jong"] >= 35:
        return (f"Nieuwbouw of ouder huis in {n}? Eén formulier is genoeg voor offertes van maximaal drie schilders, "
                f"gratis en zonder verplichting.")
    return (f"Vul het formulier in voor {n}. Maximaal drie schilders uit de buurt sturen je een offerte; jij kiest, "
            f"of je kiest niet.")


def _cta_midden(p, f):
    return f"Eén aanvraag voor je huis in {p['naam']}, maximaal drie offertes terug."


# ---------------------------------------------------------------- nabewerking
def varieer_plaats(p, html):
    """Vervang de vaste zinnen op /schilder/<plaats>/ door een data-gestuurde versie."""
    f = feiten(p)
    if not f:
        return html
    n = p["naam"]
    lead, s1, s2, s3 = _stappen(p, f)
    vervang = [
        ("Klik door voor de richtprijzen per klus en vraag direct offertes aan bij lokale bedrijven.", _lead_diensten(p, f)),
        ("Eén aanvraag, meerdere prijzen. Je hoeft niet zelf bedrijf voor bedrijf af te bellen.", lead),
        ("Vier korte vragen over de klus, het pand en de planning. Klaar in ongeveer een minuut.", s1),
        (f"We koppelen je aanvraag aan maximaal drie schilders in {n} die dit type werk daadwerkelijk doen en op dit moment ruimte hebben.", s2),
        ("Je ontvangt de offertes rechtstreeks van de schilders. Bevalt het niet? Dan zeg je gewoon nee — je zit nergens aan vast.", s3),
        ("In de praktijk zie je dat uurtarief zelden terug op een offerte: het meeste werk wordt aangeboden per vierkante meter of per stuk, omdat je dan vooraf weet waar je aan toe bent.", _uurtarief(p, f)),
        ("<p><small>Indicatieve prijzen inclusief materiaal en btw, tenzij er excl. btw staat. De werkelijke prijs hangt af van de staat van de ondergrond, bereikbaarheid en het seizoen. Vraag altijd meerdere offertes aan.</small></p>", _tabel_noot(p, f)),
        (f"Eén aanvraag, maximaal drie offertes van schilders die in {n} werken.", _cta_midden(p, f)),
        ("Die twee bepalen hoeveel kozijnen er zijn, of er een steiger nodig is en welke gevels het eerst aan de beurt zijn.", _woningmix(p, f)),
        ("De meeste schilders in deze regio werken in een straal van 20 tot 30 kilometer. Zoek je in een buurgemeente?", _buren(p, f)),
        (f"Vul het formulier in en ontvang vrijblijvend offertes van maximaal drie schildersbedrijven die in {n} werken.", _cta(p, f)),
    ]
    for oud, nieuw in vervang:
        html = html.replace(oud, nieuw, 1)
    # dienstkaarten: de korte omschrijving per dienst
    for d in DIENSTEN:
        html = html.replace(f'<h3>{d.get("naam_lang", d["naam"])} in {n}</h3><p>{d["kort"]}</p>',
                            f'<h3>{d.get("naam_lang", d["naam"])} in {n}</h3><p>{_kaart(d, p, f)}</p>', 1)
    return html
