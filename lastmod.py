# -*- coding: utf-8 -*-
"""Echte lastmod-datums voor de sitemap.

Voorheen kreeg elke URL bij elke build de datum van vandaag. Google negeert lastmod
als die altijd verandert. Nu onthouden we per URL een vingerafdruk (hash) van de
inhoud. Alleen als de inhoud echt verandert, schuift de datum op.

- De hash negeert header, footer, scripts en datums in de tekst ("bijgewerkt op ..."),
  zodat een nieuwe menulink of de dag van de build geen nieuwe lastmod geeft.
- De gegevens staan in lastmod.txt (regel per URL: pad, hash, datum) en horen in git.
  .gitattributes zet dat bestand op merge=union: botsen twee branches, dan blijven
  beide regels staan. Bij het inlezen wint per URL de regel met de nieuwste datum,
  en de volgende build schrijft het bestand weer netjes en zonder dubbelen weg.
- Draait de build in GitHub Actions zonder bijgewerkt lastmod.txt, dan krijgt een
  gewijzigde pagina gewoon de datum van vandaag. Er gaat dus niets mis, alleen
  wordt de datum niet bewaard tot iemand lokaal bouwt en commit.
"""

import hashlib
import os
import re

BESTAND = os.path.join(os.path.dirname(os.path.abspath(__file__)), "lastmod.txt")

_WEG = [
    re.compile(r"<head>.*?(?=<title>)", re.S),          # alles in <head> voor de titel
    re.compile(r"<link [^>]*>|<meta (?!name=\"description\")[^>]*>", re.S),
    re.compile(r"<script\b.*?</script>", re.S),
    re.compile(r"<header\b.*?</header>", re.S),
    re.compile(r"<footer\b.*?</footer>", re.S),
    re.compile(r"\b\d{4}-\d{2}-\d{2}\b|\b\d{2}-\d{2}-\d{4}\b|\b\d{4}/\d{2}\b"),
]

_hashes = {}


def vingerafdruk(html):
    for patroon in _WEG:
        html = patroon.sub("", html)
    return hashlib.sha1(html.encode("utf-8")).hexdigest()[:12]


def onthoud(pad, html):
    _hashes[pad] = vingerafdruk(html)


def _lees():
    oud = {}
    if not os.path.exists(BESTAND):
        return oud
    with open(BESTAND, encoding="utf-8") as f:
        for regel in f:
            delen = regel.strip().split("\t")
            if len(delen) != 3 or delen[0].startswith("#"):
                continue
            pad, h, datum = delen
            if pad not in oud or datum > oud[pad][1]:
                oud[pad] = (h, datum)
    return oud


def echte_datum(pad, html, vandaag):
    """seo-ronde 5: de lastmod-datum van deze pagina, al tijdens het schrijven.
    Zelfde regel als datums(): onveranderde inhoud houdt de oude datum."""
    global _OUD
    if _OUD is None:
        _OUD = _lees()
    oud = _OUD.get(pad)
    return oud[1] if oud and oud[0] == vingerafdruk(html) else vandaag


def zet_datums(pad, html, vandaag):
    """Vervangt de builddatum in "Bijgewerkt op", "Laatst bijgewerkt" en dateModified
    door de echte lastmod. Anders zegt elke pagina bij elke build dat hij vandaag is bijgewerkt."""
    d = echte_datum(pad, html, vandaag)
    if d == vandaag:
        return html
    nl_v, nl_d = f"{vandaag[8:10]}-{vandaag[5:7]}-{vandaag[:4]}", f"{d[8:10]}-{d[5:7]}-{d[:4]}"
    return (html.replace(f'"dateModified": "{vandaag}"', f'"dateModified": "{d}"')
                .replace(f"Laatst bijgewerkt: {vandaag}", f"Laatst bijgewerkt: {d}")
                .replace(f"Bijgewerkt op {nl_v}", f"Bijgewerkt op {nl_d}"))


_OUD = None


def datums(vandaag):
    """Geeft {pad: datum} voor alle onthouden pagina's en werkt lastmod.txt bij."""
    oud = _lees()
    uit = {}
    for pad, h in _hashes.items():
        if pad in oud and oud[pad][0] == h:
            uit[pad] = oud[pad][1]
        else:
            uit[pad] = vandaag
    with open(BESTAND, "w", encoding="utf-8") as f:
        f.write("# pad\thash\tdatum (wordt door build.py bijgewerkt; zie lastmod.py)\n")
        for pad in sorted(uit):
            f.write(f"{pad}\t{_hashes[pad]}\t{uit[pad]}\n")
    return uit
