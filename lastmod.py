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
