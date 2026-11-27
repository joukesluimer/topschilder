# -*- coding: utf-8 -*-
"""
Onderhoudscheck: "Is jouw schilderwerk aan de beurt?"

Een losse pagina (/onderhoudscheck/) met negen korte vragen, een onderhoudsmeter
als uitslag, richtprijzen uit kosten_data.py, een agendaherinnering (.ics) die in
de browser wordt gemaakt en een knop die het offerteformulier vast invult.
Er wordt niets opgeslagen of verstuurd tot iemand zelf het offerteformulier verstuurt.

build.py roept alleen build_onderhoudscheck(write) aan en gebruikt teaser_home()
en teaser_kort() voor de links vanaf andere pagina's. CSS en JS staan in deze
module zelf, zodat assets.py niet hoeft te veranderen.
"""

import json
import math
import re

from components import page, crumbs, offerte_form, faq_blok, foto, foto_alleen_desktop, title, eur
from foto_data import FOTOS
from kosten_data import KOSTEN, PRIJSBANDEN

PAD = "/onderhoudscheck/"

# Foto's voor de zelfcheck. Bron: ~/Desktop/Topschilder/Gratis content (kopie, niet bewerkt
# in die map). Webversies in fotos/. Staan ook op /fotoverantwoording/ (zie build.py).
_BEW = "Bijgesneden tot 3:2 (uit {}), verkleind naar 1600, 800 en 400 px breed en omgezet naar WebP."
FOTOS_ONDERHOUDSCHECK = [
    {"naam": "verweerde-blauwe-houten-schutting",
     "alt": "Verweerde blauwe houten schutting waar de verf grotendeels af is en het grijze hout bloot ligt",
     "w": 1600, "h": 1067, "titel": "Alt Blau Holz-Zaun.jpg", "maker": "ZeWrestler",
     "licentie": "CC BY-SA 3.0", "licentie_url": "https://creativecommons.org/licenses/by-sa/3.0",
     "bron": "https://commons.wikimedia.org/wiki/File:Alt_Blau_Holz-Zaun.jpg",
     "bewerking": _BEW.format("5184 × 3127 px")},
    {"naam": "hout-met-blokvormige-scheuren-close-up",
     "alt": "Close-up van hout met blokvormige scheuren en witte schimmeldraden",
     "w": 1600, "h": 1067, "titel": "Merule sur Douglas 3.jpg", "maker": "Jiròni B.",
     "licentie": "CC BY-SA 4.0", "licentie_url": "https://creativecommons.org/licenses/by-sa/4.0",
     "bron": "https://commons.wikimedia.org/wiki/File:Merule_sur_Douglas_3.jpg",
     "bewerking": _BEW.format("2048 × 1536 px")},
    {"naam": "aangetast-houten-balk-met-meetlint",
     "alt": "Door bruinrot aangetaste, brokkelige houten balk met een meetlint ernaast",
     "w": 1600, "h": 1067, "titel": "Braunfaeule Holz FI20070208.jpg", "maker": "Mätes II.",
     "licentie": "CC BY-SA 3.0", "licentie_url": "https://creativecommons.org/licenses/by-sa/3.0",
     "bron": "https://commons.wikimedia.org/wiki/File:Braunfaeule_Holz_FI20070208.jpg",
     "bewerking": _BEW.format("2288 × 1447 px")},
]
_F = {f["naam"]: f for f in FOTOS_ONDERHOUDSCHECK}

# Bronnen voor de onderhoudstermijnen (gelezen in november 2026)
BRONNEN_TERMIJN = {
    "nbvt": ("Nederlandse Bond van Timmerfabrikanten en Stichting Garantiefonds Timmerwerk, brochure Onderhoud van houten gevelelementen (onderhoudsschema voor de eigenaar-bewoner)", "https://www.gilskozijnen.nl/uploads/file/Onderhoud%20van%20houten%20gevelelementen.pdf"),
    "sikkens": ("Helwig Stipt, Onderhoudsvoorschriften houten kozijnen, april 2021 (schema voor kozijnen afgewerkt met Sikkens Concept II+)", "https://stiptkozijnen.nl/Content/Docs/Helwig%20Stipt%20-%20Onderhoudsvoorschriften.pdf"),
    "sigma": ("Van de Vin ramen en kozijnen, Onderhoudsvoorschriften kozijnen, april 2011 (afgewerkt met Sigma Coatings)", "https://www.vandevin.nl/upload/e01303_vinEasyfitOnderhoudsvoor.pdf"),
    "dejong": ("De Jong Kozijnen, Onderhoud van houten gevelelementen", "https://dejongkozijnen.nl/onderhoud-van-houten-gevelelementen/"),
    "koopmans": ("Koopmans Verf, Hoe herken en repareer je houtrot? (november 2022)", "https://www.koopmansverf.nl/klushulp/hoe-herken-en-repareer-je-houtrot/"),
    "vanassen": ("Schildersbedrijf Van Assen, Hoe vaak buiten schilderen? (oktober 2026)", "https://schildersbedrijfvanassen.nl/blog/hoe-vaak-buiten-schilderen"),
    "homedeal": ("Homedeal, Kozijnen onderhoud (juni 2026)", "https://www.homedeal.nl/kozijnen/onderhoud-kozijnen/"),
}


def _bl(k, kort):
    return f'<a href="{BRONNEN_TERMIJN[k][1]}" rel="nofollow noopener" target="_blank">{kort}</a>'


# ---------------------------------------------------------------------------
# Prijzen: alles komt uit kosten_data.py, niets verzonnen
# ---------------------------------------------------------------------------

def _kosten(slug):
    return next(k for k in KOSTEN if k["slug"] == slug)


def _band(tekst):
    """Haalt '€1.500 – €3.500' uit een voorbeeldregel van de kostenpagina."""
    m = re.search(r"€([\d.]+)\s*–\s*€([\d.]+)", tekst)
    assert m, f"Geen prijsband gevonden in: {tekst}"
    return int(m.group(1).replace(".", "")), int(m.group(2).replace(".", ""))


def prijzen():
    huis = _kosten("huis-schilderen")["voorbeelden"]
    kozijn = PRIJSBANDEN["buitenkozijn"]
    return {
        "woning": {
            "tussen": _band(huis[0][2]),
            "hoek": _band(huis[1][2]),
            "vrijstaand": _band(huis[2][2]),
        },
        "kozijn": (kozijn["van"], kozijn["tot"]),
        "steiger": (PRIJSBANDEN["steiger"]["van"], PRIJSBANDEN["steiger"]["tot"]),
        "houtrot": (PRIJSBANDEN["houtrot_plek"]["van"], PRIJSBANDEN["houtrot_plek"]["tot"]),
    }


# ---------------------------------------------------------------------------
# Iconen voor de antwoordknoppen (eigen, eenvoudige lijntekeningen)
# ---------------------------------------------------------------------------

IC = {
    "nieuw": '<path d="M5 12l4 4 10-10"/>',
    "kalender": '<rect x="4" y="5" width="16" height="15" rx="2"/><path d="M4 10h16M9 3v4M15 3v4"/>',
    "klok": '<circle cx="12" cy="12" r="8"/><path d="M12 8v4l3 2"/>',
    "oud": '<circle cx="12" cy="12" r="8"/><path d="M12 8v4l3 2"/><path d="M4 4l3 3"/>',
    "vraag": '<circle cx="12" cy="12" r="8"/><path d="M9.6 9.5a2.5 2.5 0 1 1 3.4 2.3c-.6.3-1 .8-1 1.5v.4"/><path d="M12 17h.01"/>',
    "zon": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
    "schaduw": '<path d="M7 17h10a4 4 0 0 0 0-8 5.5 5.5 0 0 0-10.6 1.5A3.3 3.3 0 0 0 7 17z"/>',
    "water": '<path d="M3 9c2 0 2-1.5 4.5-1.5S9.5 9 12 9s2.5-1.5 4.5-1.5S19 9 21 9"/><path d="M3 14c2 0 2-1.5 4.5-1.5S9.5 14 12 14s2.5-1.5 4.5-1.5S19 14 21 14"/><path d="M3 19c2 0 2-1.5 4.5-1.5S9.5 19 12 19s2.5-1.5 4.5-1.5S19 19 21 19"/>',
    "goed": '<circle cx="12" cy="12" r="8"/><path d="M8.5 12.3l2.3 2.3 4.7-4.9"/>',
    "beetje": '<path d="M5 19l5-5 3 3 6-6"/><path d="M15 11h4v4"/>',
    "veel": '<path d="M12 4l9 16H3z"/><path d="M12 10v4M12 17h.01"/>',
    "vinger": '<path d="M9 11V5.5a1.5 1.5 0 0 1 3 0V11"/><path d="M12 10.5a1.5 1.5 0 0 1 3 0V12a1.5 1.5 0 0 1 3 0v3a6 6 0 0 1-6 6h-1a6 6 0 0 1-5-2.7l-2-3a1.5 1.5 0 0 1 2.4-1.8L9 15"/>',
    "naad": '<rect x="4" y="4" width="16" height="16" rx="1"/><path d="M12 4v6l-2 2 2 2v6"/>',
    "sleutel": '<path d="M14 4l6 6-9 9H5v-6z"/><path d="M12.5 5.5l6 6"/>',
    "tussen": '<path d="M2 20V11l4-4 4 4v9M10 20V11l4-4 4 4v9M18 20v-9l2-2 2 2v9" opacity=".45"/><path d="M10 20V11l4-4 4 4v9"/>',
    "hoek": '<path d="M3 20V11l5-5 5 5v9"/><path d="M13 20v-9l4-4 4 4v9" opacity=".45"/>',
    "vrijstaand": '<path d="M5 20V11l7-6 7 6v9z"/><path d="M10 20v-5h4v5"/>',
    "flat": '<rect x="6" y="3" width="12" height="18" rx="1"/><path d="M9 7h2M13 7h2M9 11h2M13 11h2M9 15h2M13 15h2"/>',
}


def ic(naam):
    return (f'<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor" '
            f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{IC[naam]}</svg>')


# ---------------------------------------------------------------------------
# De vragen. Per antwoord: waarde, label, toelichting, icoon, toon (kleurstreep)
# ---------------------------------------------------------------------------

VRAGEN = [
    ("leeftijd", "Wanneer is de buitenkant voor het laatst geschilderd?",
     "Het gaat om de kozijnen, deuren en boeidelen. Een schatting is goed genoeg.",
     [("0-2", "Minder dan 3 jaar", "Nog vrij vers", "nieuw", "g"),
      ("3-5", "3 tot 5 jaar", "Halverwege", "kalender", "g"),
      ("6-8", "6 tot 8 jaar", "Het gangbare moment", "klok", "o"),
      ("8+", "Meer dan 8 jaar", "Of het is me te lang", "oud", "r"),
      ("onbekend", "Weet ik niet", "Bijvoorbeeld net verhuisd", "vraag", "n")]),
    ("ligging", "Welke kant van je huis heeft het zwaarst te verduren?",
     "Kijk naar de kant met de meeste kozijnen, of waar de verf er het slechtst uitziet.",
     [("zon", "Zuid of west", "Volle zon en de meeste regen", "zon", "o"),
      ("schaduw", "Noord of oost", "Weinig zon", "schaduw", "g"),
      ("open", "Open ligging", "Aan het water of in de polder", "water", "o"),
      ("onbekend", "Weet ik niet", "Of het verschilt per kant", "vraag", "n")]),
    ("afwerking", "Hoe is het houtwerk afgewerkt?",
     "Kijk naar de kozijnen. De kleur bepaalt hoe warm de verf in de zon wordt, en dus hoe snel hij slijt.",
     [("licht", "Lichte dekkende verf", "Wit, crème, lichtgrijs of pastel", "zon", "g"),
      ("donker", "Donkere dekkende verf", "Antraciet, donkergroen, donkerblauw, zwart", "schaduw", "o"),
      ("transparant", "Transparant", "Je ziet de houtnerf: beits of blanke lak", "naad", "r"),
      ("onbekend", "Weet ik niet", "Of het is gemengd", "vraag", "n")]),
    ("bladderen", "Zie je verf die afbladdert?",
     "Let vooral op de onderkant van kozijnen, op dorpels en op de hoeken.",
     [("nee", "Nee, het zit goed", "Gesloten verflaag", "goed", "g"),
      ("beetje", "Hier en daar", "Kleine plekjes of blaasjes", "beetje", "o"),
      ("veel", "Grote stukken", "Ik zie kaal of grijs hout", "veel", "r")]),
    ("krijten", "Veeg met je vinger over de verf. Wat zie je?",
     "Verf die lang in de zon zit wordt poederig. Dat heet krijten.",
     [("nee", "Mijn vinger blijft schoon", "De verf glanst nog", "goed", "g"),
      ("beetje", "Een beetje wit poeder", "De glans is wat dof", "vinger", "o"),
      ("veel", "Duidelijk krijt", "Dof en poederig", "veel", "r")]),
    ("naden", "Hoe zien de naden en de kit eruit?",
     "Kijk waar stukken hout op elkaar aansluiten en langs het glas.",
     [("dicht", "Alles is dicht", "Kit is nog soepel", "goed", "g"),
      ("scheurtjes", "Haarscheurtjes", "Kleine lijntjes in de verf", "naad", "o"),
      ("open", "Open naden of losse kit", "Hier kan water in", "veel", "r")]),
    ("zacht", "Druk met een sleutel in de dorpel en de onderhoeken. Hoe voelt het hout?",
     "Doe dit op de plekken waar water blijft staan. Hard hout is goed nieuws.",
     [("hard", "Hard", "De sleutel gaat er niet in", "goed", "g"),
      ("twijfel", "Ik twijfel", "Donkere plekken of iets zacht", "vraag", "o"),
      ("zacht", "Zacht", "De sleutel zakt erin", "sleutel", "r")]),
    ("woning", "In wat voor woning woon je?",
     "Dan kunnen we laten zien wat het ongeveer kost.",
     [("tussen", "Tussenwoning", "Voor- en achtergevel", "tussen", "n"),
      ("hoek", "Hoekwoning of twee-onder-een-kap", "Met een zijgevel", "hoek", "n"),
      ("vrijstaand", "Vrijstaand", "Houtwerk rondom", "vrijstaand", "n"),
      ("appartement", "Appartement", "Eigen kozijnen of VvE", "flat", "n")]),
    ("bouw", "Wanneer is je woning gebouwd?",
     "Ongeveer is goed. Het zegt iets over het houtwerk.",
     [("voor1945", "Voor 1945", "Vooroorlogs", "oud", "n"),
      ("1945-1980", "1945 – 1980", "Wederopbouw en jaren 70", "kalender", "n"),
      ("1980-2000", "1980 – 2000", "Jaren 80 en 90", "kalender", "n"),
      ("na2000", "Na 2000", "Nieuwere woning", "nieuw", "n")]),
]

LABELS = {k: {v: lbl for v, lbl, *_ in opts} for k, _, _, opts in VRAGEN}


# ---------------------------------------------------------------------------
# Onderhoudsmeter (halve cirkel met vier vakken)
# ---------------------------------------------------------------------------

METER_KLEUREN = ["#0f8a5f", "#e2a80c", "#f4820b", "#c0392b"]
METER_LABELS = ["Goed", "Binnenkort", "Nu doen", "Houtrot-risico"]


def _punt(cx, cy, r, graden):
    a = math.radians(graden)
    return cx + r * math.cos(a), cy + r * math.sin(a)


def meter_svg(klein=False):
    cx, cy, r = 120, 120, 92
    vakken = ""
    for i, kleur in enumerate(METER_KLEUREN):
        a1, a2 = 180 + i * 45 + 1.2, 180 + (i + 1) * 45 - 1.2
        x1, y1 = _punt(cx, cy, r, a1)
        x2, y2 = _punt(cx, cy, r, a2)
        vakken += (f'<path d="M{x1:.1f} {y1:.1f}A{r} {r} 0 0 1 {x2:.1f} {y2:.1f}" '
                   f'stroke="{kleur}" stroke-width="24" fill="none"/>')
    naald = ('<g class="ohc-naald" style="transform:rotate(-80deg)">'
             f'<path d="M{cx} {cy - 80}L{cx - 6} {cy}L{cx + 6} {cy}z" fill="#241906"/></g>'
             f'<circle cx="{cx}" cy="{cy}" r="10" fill="#241906"/><circle cx="{cx}" cy="{cy}" r="4" fill="#fff"/>')
    tekst = ""
    if not klein:
        tekst = ('<text x="20" y="146" font-size="12" fill="#6f6047">Goed</text>'
                 '<text x="220" y="146" font-size="12" fill="#6f6047" text-anchor="end">Houtrot</text>')
    return (f'<svg class="ohc-meter" viewBox="0 0 240 {150 if not klein else 132}" role="img" '
            f'aria-label="Onderhoudsmeter van goed tot houtrot-risico">{vakken}{naald}{tekst}</svg>')


# ---------------------------------------------------------------------------
# Teasers voor andere pagina's
# ---------------------------------------------------------------------------

def teaser_home():
    return f"""<section class="section">
<div class="wrap">
  <div class="ohc-teaser">
    <div class="ohc-teaser-meter">{meter_svg(klein=True)}</div>
    <div>
      <span class="badge">Nieuw · 2 minuten</span>
      <h2>Is jouw schilderwerk aan de beurt?</h2>
      <p>Twijfel je of het al tijd is? Beantwoord negen korte vragen over je kozijnen en je ziet meteen of het nog goed is, binnenkort moet of nu. Met wat het ongeveer kost en het beste moment om te plannen.</p>
      <p style="margin:0"><a class="btn btn-primary" href="{PAD}">Doe de onderhoudscheck</a></p>
    </div>
  </div>
</div>
</section>{TEASER_CSS}"""


def teaser_kort():
    return (f'<div class="callout"><p><strong>Twijfel je of het al tijd is?</strong> '
            f'Doe de <a href="{PAD}">onderhoudscheck</a>: in negen korte vragen zie je of je '
            f'schilderwerk nog goed is, binnenkort moet of nu, en wat het ongeveer kost.</p></div>')


TEASER_CSS = """<style>
.ohc-teaser{display:grid;grid-template-columns:220px minmax(0,1fr);gap:36px;align-items:center;background:linear-gradient(120deg,#fff4e6,#fff);border:1.5px solid #f6d9b2;border-radius:var(--radius-lg);padding:30px 34px}
.ohc-teaser-meter svg{width:100%;height:auto}
.ohc-teaser .ohc-naald{transform-origin:120px 120px;transform:rotate(-25deg)!important}
@media(max-width:700px){.ohc-teaser{grid-template-columns:1fr;gap:10px;padding:24px 20px}.ohc-teaser-meter{max-width:180px}}
</style>"""


# ---------------------------------------------------------------------------
# De pagina
# ---------------------------------------------------------------------------

def _vraag_html(i, sleutel, vraag, hint, opties):
    knoppen = "".join(
        f'<button type="button" class="ohc-opt ohc-t-{toon}" data-v="{v}">'
        f'<span class="ohc-ico">{ic(icoon)}</span>'
        f'<span class="ohc-txt"><span class="ohc-lbl">{lbl}</span><span class="ohc-sub">{sub}</span></span></button>'
        for v, lbl, sub, icoon, toon in opties
    )
    return (f'<fieldset class="ohc-q" data-key="{sleutel}"{"" if i == 0 else " hidden"}>'
            f'<legend class="ohc-vraag">{vraag}</legend>'
            f'<p class="ohc-hint">{hint}</p>'
            f'<div class="ohc-opts">{knoppen}</div></fieldset>')


def build_onderhoudscheck(write):
    p = prijzen()
    data = {
        "prijzen": p,
        "labels": LABELS,
        "meter": METER_LABELS,
    }
    vragen = "".join(_vraag_html(i, *v) for i, v in enumerate(VRAGEN))
    houtrotfoto = FOTOS["houtrot-reparatie"]["hero"]
    bladderfoto = FOTOS["houtrot-reparatie"]["sectie"]

    cr, cr_ld = crumbs([("Home", "/"), ("Onderhoudscheck", None)])

    hero = f"""{cr}
<section class="section-sm ohc-hero tool-hero" data-ohc>
<div class="wrap">
  <div class="ohc-grid">
    <div class="ohc-intro">
      <span class="badge">Gratis tool · 2 minuten · niets opgeslagen</span>
      <h1>Is jouw schilderwerk aan de beurt?</h1>
      <p class="lead">Negen korte vragen over je kozijnen, deuren en boeidelen. Daarna zie je op de onderhoudsmeter hoe je ervoor staat, wat je nu het beste doet en wat het ongeveer kost.</p>
      <ul class="checklist ohc-usps">
        <li>Direct een uitslag, zonder e-mailadres</li>
        <li>Richtprijzen voor jouw type woning</li>
        <li>Het beste moment om te plannen, en een herinnering in je agenda</li>
      </ul>
      <div class="ohc-introfoto">{foto_alleen_desktop(bladderfoto, "560px")}</div>
    </div>
    <div class="formcard ohc-card" aria-live="polite">
      <div class="ohc-quiz">
        <div class="ohc-top">
          <span class="ohc-teller">Vraag <b>1</b> van {len(VRAGEN)}</span>
          <button type="button" class="btn-link ohc-terug" hidden>← Terug</button>
        </div>
        <div class="ohc-balk"><i style="width:{100 / len(VRAGEN):.1f}%"></i></div>
        {vragen}
        <noscript><p class="callout">Zet JavaScript aan om de onderhoudscheck te doen. Je kunt ook meteen <a href="/offerte-aanvragen/">offertes aanvragen</a>.</p></noscript>
      </div>
      <div class="ohc-uitslag" hidden>
        <p class="ohc-kicker">Jouw uitslag</p>
        <div class="ohc-meterwrap">{meter_svg()}</div>
        <h2 class="ohc-niveau"></h2>
        <p class="ohc-samenvatting"></p>
        <div class="ohc-acties">
          <button type="button" class="btn btn-primary btn-lg ohc-naar-offerte">Vul het offerteformulier vast in</button>
          <p class="ohc-klein">We zetten je uitslag in het formulier. Je kiest zelf of je het verstuurt.</p>
        </div>
        <div class="ohc-blokken"></div>
        <div class="ohc-agenda">
          <h3>Zet een herinnering in je agenda</h3>
          <p class="ohc-agenda-tekst"></p>
          <div class="ohc-agenda-rij">
            <label for="ohc-datum" class="ohc-sr">Datum van de herinnering</label>
            <input type="date" id="ohc-datum">
            <button type="button" class="btn btn-ghost ohc-ics">Download (.ics)</button>
          </div>
          <p class="ohc-klein">Het agendabestand wordt op je eigen toestel gemaakt. We slaan niets op en versturen niets.</p>
        </div>
        <p class="ohc-opnieuw"><button type="button" class="btn-link ohc-reset">Opnieuw doen</button></p>
      </div>
    </div>
  </div>
</div>
</section>"""

    w = p["woning"]
    kaart = lambda id_, titel, f, tekst: (
        f'<article class="ohc-sig" id="check-{id_}">{foto(f, "(max-width:640px) calc(100vw - 40px), 360px")}'
        f'<div class="ohc-sig-tekst"><h3>{titel}</h3>{tekst}</div></article>')
    signalen = f"""<section class="section soft" id="zelf-checken"><div class="wrap">
  <div class="prose ohc-sec-intro">
    <h2>Zo check je zelf je schilderwerk</h2>
    <p>Je hoeft geen schilder te zijn om te zien of je houtwerk een beurt nodig heeft. De onderhoudsschema's van de timmerindustrie adviseren om het houtwerk elk jaar na te lopen ({_bl("nbvt", "NBvT/SGT")}). Doe dat op een droge dag, het liefst na de winter, en let op deze vier signalen.</p>
  </div>
  <div class="ohc-sigs">
    {kaart("afbladderen", "1. Afbladderen", houtrotfoto, "<p>Loszittende verf, blaasjes of schilfers. Begin onder aan de kozijnen en bij de dorpels: daar blijft water het langst staan. Bladdert het ver, dan zit er vaak al vocht achter. <small>Op de foto: afbladderende verf op een rottende raamdorpel.</small></p>")}
    {kaart("scheuren", "2. Scheuren", _F["hout-met-blokvormige-scheuren-close-up"], f"<p>Begin het met haarscheurtjes in de verf, vooral in hoeken en op naden waar stukken hout samenkomen. Door een scheur of open naad loopt water achter de verf. Krimpscheuren in de verflaag kunnen ook op houtrot wijzen ({_bl('koopmans', 'Koopmans')}). <small>Op de foto: rot dat al ver is, met blokvormige scheuren en schimmeldraden. Zo ver wil je het niet laten komen.</small></p>")}
    {kaart("kaal", "3. Kale plekken", _F["verweerde-blauwe-houten-schutting"], f"<p>Grijs, kaal hout op scherpe kanten en randen. Die slijten het eerst, net als de onderdorpels aan de zonkant ({_bl('nbvt', 'NBvT/SGT')}). Kaal hout neemt vocht op; wacht dan niet langer. <small>Op de foto: verf die bijna helemaal is verweerd.</small></p>")}
    {kaart("zacht", "4. Zachte plekken", _F["aangetast-houten-balk-met-meetlint"], f"<p>Druk met een priem, sleutel of schroevendraaier in de dorpel en de onderhoeken. Gaat hij er makkelijk in, dan is het hout zacht en zit er waarschijnlijk houtrot ({_bl('koopmans', 'Koopmans')}). Schilder daar nooit overheen. <small>Op de foto: hout dat door bruinrot brokkelig is geworden.</small></p>")}
  </div>
  <p class="ohc-extra"><strong>Nog twee snelle tests:</strong> veeg met je vinger over de verf. Blijft er wit poeder aan je vinger, dan krijt de verf en wordt de laag dunner. En kijk naar de kit langs het glas: die moet soepel zijn en goed aansluiten.</p>
</div></section>

<section class="section" id="termijnen"><div class="wrap narrow prose">
  <h2>Hoe vaak moet je buiten laten schilderen?</h2>
  <p>Er is geen vaste termijn, maar de timmerindustrie en de verffabrikanten geven wel onderhoudsschema's. Die gaan uit van goed aangebracht schilderwerk en een gemiddelde ligging. De schilder controleert het houtwerk dan een jaar voordat het bijwerken gepland staat, en schuift het schema op als het nog goed is.</p>
  <div class="tablewrap"><table class="ohc-termijn">
    <thead><tr><th>Afwerking</th><th>Bijwerken</th><th>Nieuwe laag</th><th>Bron</th></tr></thead>
    <tbody>
      <tr><td><strong>Dekkend, lichte kleur</strong><br><small>wit, crème, lichtgrijs</small></td><td>na ± 3 jaar</td><td>na ± 6 jaar</td><td>{_bl("nbvt", "NBvT/SGT")}; Sikkens-schema: 4 en 7 jaar ({_bl("sikkens", "Helwig Stipt")}); Sigma-schema: nieuwe laag na 7 jaar ({_bl("sigma", "Van de Vin")})</td></tr>
      <tr><td><strong>Dekkend, donkere kleur</strong><br><small>antraciet, donkergroen, zwart</small></td><td>na ± 2 jaar</td><td>na ± 4 jaar</td><td>{_bl("nbvt", "NBvT/SGT")}; Sikkens-schema: 3 en 5 jaar ({_bl("sikkens", "Helwig Stipt")})</td></tr>
      <tr><td><strong>Transparant</strong><br><small>beits of lak waar de nerf doorheen te zien is</small></td><td>elk jaar</td><td>om de 2 jaar</td><td>{_bl("nbvt", "NBvT/SGT")}, {_bl("sikkens", "Helwig Stipt")}, {_bl("sigma", "Van de Vin")}</td></tr>
    </tbody>
  </table></div>
  <p class="ohc-klein">Ter vergelijking: schildersbedrijven en prijssites noemen voor dekkend schilderwerk als vuistregel 6 tot 8 jaar ({_bl("vanassen", "Van Assen")}) of 5 tot 7 jaar ({_bl("homedeal", "Homedeal")}).</p>

  <h3>Wat de termijn korter of langer maakt</h3>
  <ul>
    <li><strong>Zonkant of schaduwkant.</strong> Aan de zonkant (zuid en west) slijt de verf sneller dan aan de schaduwkant of onder een ruime dakgoot of een balkon. Verpoederen begint meestal op de onderdorpels aan de zonkant ({_bl("nbvt", "NBvT/SGT")}, {_bl("dejong", "De Jong Kozijnen")}).</li>
    <li><strong>Kleur.</strong> Donkere kleuren worden in de zon veel warmer. Het hout krimpt en zwelt dan meer en de verf breekt sneller af. Daarom het kortere schema voor donkere kleuren. Een middenkleur op een zeer zonnige, beschutte zuidgevel valt ook onder dat schema ({_bl("sikkens", "Helwig Stipt")}).</li>
    <li><strong>Hardhout of naaldhout.</strong> Dekkende verf kan op beide. Transparante systemen mogen niet op elke houtsoort. Bij naaldhout zoals vuren wordt een lichte kleur aangeraden ({_bl("sikkens", "Helwig Stipt")}, {_bl("sigma", "Van de Vin")}). Twijfel je wat je hebt, vraag het de schilder bij de opname.</li>
    <li><strong>Kust of open polder.</strong> Voor een ligging aan zee, open water of in de open polder noemen de schema's geen apart getal. Wind, regen en vocht belasten de verf daar extra. Ons advies: houd daar de korte kant van het schema aan en loop het houtwerk elk jaar na.</li>
    <li><strong>Schoonhouden.</strong> Was het houtwerk mee als je de ramen lapt. Vuil houdt vocht vast; schoon houtwerk gaat langer mee ({_bl("nbvt", "NBvT/SGT")}).</li>
  </ul>

  <h2>Wat kost een buitenbeurt?</h2>
  <div class="tablewrap"><table>
    <thead><tr><th>Woning</th><th>Richtprijs buitenkant</th></tr></thead>
    <tbody>
      <tr><td>Tussenwoning</td><td class="num">{eur(w['tussen'][0])} – {eur(w['tussen'][1])}</td></tr>
      <tr><td>Hoekwoning of twee-onder-een-kap</td><td class="num">{eur(w['hoek'][0])} – {eur(w['hoek'][1])}</td></tr>
      <tr><td>Vrijstaande woning</td><td class="num">{eur(w['vrijstaand'][0])} – {eur(w['vrijstaand'][1])}</td></tr>
      <tr><td>Per buitenkozijn</td><td class="num">{eur(p['kozijn'][0])} – {eur(p['kozijn'][1])}</td></tr>
      <tr><td>Houtrot herstellen, per plek</td><td class="num">{eur(p['houtrot'][0])} – {eur(p['houtrot'][1])}</td></tr>
    </tbody>
  </table></div>
  <p><small>Richtprijzen inclusief 9% btw en materiaal, prijspeil 2026, van onze pagina's over <a href="/kosten/huis-schilderen/">een huis schilderen</a> en <a href="/kosten/kozijnen-schilderen/">kozijnen schilderen</a>. Reken je hele klus uit met de <a href="/kosten/calculator/">huiscalculator</a>. De echte prijs hangt af van de staat van het houtwerk, de bereikbaarheid en de regio.</small></p>

  <h3>Bronnen</h3>
  <ol class="ohc-bronnen">{"".join(f'<li><a href="{u}" rel="nofollow noopener" target="_blank">{t}</a></li>' for t, u in BRONNEN_TERMIJN.values())}</ol>
</div></section>"""


    offerte = f"""<section class="section"><div class="wrap">
  <div class="grid g2" style="gap:48px;align-items:start">
    <div class="prose">
      <h2>Liever meteen weten wat het bij jou kost?</h2>
      <p class="lead">Vraag gratis offertes aan bij maximaal drie schilders uit jouw regio. Na de check vullen we je uitslag alvast voor je in.</p>
      <ul class="checklist">
        <li>De schilder kijkt ter plekke naar je houtwerk; de check is een eerste indruk</li>
        <li>Je vergelijkt de offertes en kiest zelf, of niet</li>
        <li>Gratis en vrijblijvend</li>
      </ul>
      <p>Heb je al een offerte? <a href="/offerte-vergelijken/">Laat hem checken</a>.</p>
    </div>
    <div>{offerte_form("Offertes voor je buitenschilderwerk", "Vier korte vragen · gratis en vrijblijvend")}</div>
  </div>
</div></section>"""

    faqs = [
        ("Hoe weet ik of mijn kozijnen geschilderd moeten worden?",
         "Let op vier signalen: afbladderende verf, scheurtjes en open naden, kale plekken op randen en de zonkant, en zacht hout bij de dorpels en onderhoeken. Veeg ook even over de verf: wit poeder op je vinger betekent dat de verf krijt. Zie je een of meer signalen, dan is een beurt meestal binnen een jaar of twee verstandig. Bij zacht hout laat je het eerst nakijken."),
        ("Hoe vaak moet je buitenschilderwerk laten doen?",
         "Volgens het onderhoudsschema van de Nederlandse Bond van Timmerfabrikanten en het Garantiefonds Timmerwerk: bij lichte dekkende verf bijwerken na ongeveer 3 jaar en een nieuwe laag na ongeveer 6 jaar, bij donkere kleuren na 2 en 4 jaar, en transparant elk jaar bijwerken met om de 2 jaar een nieuwe laag. De zonkant en een open ligging vragen vaak eerder onderhoud."),
        ("Is de zonkant echt eerder aan de beurt?",
         "Ja. Aan de zuid- en westkant slijt de verf sneller dan aan de schaduwkant, en een donkere kleur maakt dat erger omdat het hout in de zon warmer wordt. Dat staat ook in de onderhoudsadviezen van timmerfabrikanten. Laat de zonkant zo nodig apart bijwerken, dan hoeft niet alles tegelijk."),
        ("Hoe herken je houtrot?",
         "Houtrot zit vaak bij dorpels, onderhoeken van kozijnen en de onderkant van deuren. Het hout voelt zacht als je er met een priem of schroevendraaier in drukt, en je ziet vaak krimpscheuren of afbladderende verf. Schilder nooit over houtrot heen. Wat herstel kost, lees je bij <a href=\"/schilderwerk/houtrot-reparatie/\">houtrot reparatie</a>."),
        ("Wat kost buitenschilderwerk?",
         "Voor de buitenkant van een tussenwoning rekenen we met €1.500 tot €3.500, inclusief 9% btw en materiaal. Per buitenkozijn is dat €90 tot €190. Meer prijzen per woningtype vind je bij <a href=\"/schilderwerk/buitenschilderwerk/\">buitenschilderwerk</a> en op <a href=\"/kosten/huis-schilderen/\">wat kost een huis schilderen</a>."),
        ("Wordt mijn uitslag opgeslagen?",
         "Nee. De check werkt helemaal in je browser. Ook het agendabestand wordt op je eigen toestel gemaakt. Pas als je zelf het offerteformulier verstuurt, gaan je gegevens naar maximaal drie schilders."),
        ("Is de uitslag hetzelfde als het oordeel van een schilder?",
         "Nee. De check geeft een eerste indruk op basis van wat jij ziet en van de algemene onderhoudsschema's. Een schilder beoordeelt het houtwerk ter plekke en kan dan ook zeggen of er houtrot onder de verf zit."),
    ]
    faq_html, faq_ld = faq_blok(faqs, "Veelgestelde vragen over de onderhoudscheck")

    app_ld = {
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": "Onderhoudscheck schilderwerk",
        "url": "https://topschilder.nl" + PAD,
        "applicationCategory": "UtilitiesApplication",
        "operatingSystem": "Alle browsers",
        "inLanguage": "nl-NL",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"},
        "description": "Negen korte vragen over je buitenschilderwerk, met een uitslag van goed tot houtrot-risico, richtprijzen en het beste moment om te plannen.",
    }

    data_tag = ('<script type="application/json" id="ohc-data">'
                + json.dumps(data, ensure_ascii=False).replace("</", "<\\/") + "</script>")

    body = hero + signalen + offerte + faq_html + PAGE_CSS + data_tag + PAGE_JS

    write(PAD, page(
        title("Onderhoudscheck: is je schilderwerk aan de beurt?"),
        "Doe de gratis onderhoudscheck: negen korte vragen en je ziet of je buitenschilderwerk goed is, binnenkort moet of nu. Met richtprijzen en het beste moment.",
        PAD, body, [cr_ld, faq_ld, app_ld]), prio=0.8)


# ---------------------------------------------------------------------------
# CSS (alleen voor deze pagina)
# ---------------------------------------------------------------------------

PAGE_CSS = """<style>
/* zelfcheck met foto's, termijnentabel, checklist in de uitslag */
.ohc-sec-intro{max-width:720px;margin-bottom:22px}
.ohc-sigs{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px}
@media(max-width:760px){.ohc-sigs{grid-template-columns:minmax(0,1fr)}}
.ohc-sig{background:#fff;border:1px solid var(--line);border-radius:var(--radius-lg);overflow:hidden;min-width:0;scroll-margin-top:90px}
.ohc-sig .foto{margin:0}
.ohc-sig .foto img{display:block;width:100%;height:auto;aspect-ratio:3/2;object-fit:cover;border-radius:0}
.ohc-sig-tekst{padding:16px 18px}
.ohc-sig-tekst h3{font-size:1.08rem;margin:0 0 6px}
.ohc-sig-tekst p{font-size:.95rem;margin:0}
.ohc-sig-tekst small{display:block;margin-top:8px;color:var(--muted);font-size:.82rem}
.ohc-extra{max-width:720px;margin:20px 0 0;font-size:.97rem}
.ohc-termijn{font-size:.92rem}
.ohc-termijn td{vertical-align:top}
.ohc-termijn td small{color:var(--muted)}
@media(max-width:640px){.ohc-termijn thead{display:none}.ohc-termijn tr{display:block;border-bottom:1px solid var(--line);padding:8px 0}.ohc-termijn td{display:block;border:0;padding:2px 0}.ohc-termijn td:nth-child(2)::before{content:"Bijwerken: ";font-weight:650}.ohc-termijn td:nth-child(3)::before{content:"Nieuwe laag: ";font-weight:650}}
.ohc-bronnen{font-size:.88rem}
.ohc-bronnen li{margin:4px 0;overflow-wrap:anywhere}
.ohc-check{list-style:none;padding:0;margin:0}
.ohc-check li{margin:0 0 8px}
.ohc-check label{display:flex;gap:10px;align-items:flex-start;cursor:pointer;font-size:.95rem;margin:0;font-weight:400}
.ohc-check input{margin-top:4px;flex:0 0 auto;width:18px;height:18px;accent-color:var(--accent)}
.ohc-check input:checked+span{color:var(--muted)}
[data-ohc] [hidden]{display:none!important}
.ohc-grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,520px);gap:48px;align-items:start}
.ohc-hero.klaar .ohc-grid{grid-template-columns:minmax(0,1fr);max-width:760px;margin:0 auto}
.ohc-hero.klaar .ohc-intro{display:none}
.ohc-usps{margin-top:6px}
.ohc-introfoto{margin-top:22px}
.ohc-introfoto img{border-radius:var(--radius)}
@media(max-width:980px){.ohc-grid{grid-template-columns:minmax(0,1fr);gap:22px}.ohc-introfoto,.ohc-usps{display:none}}
.ohc-card{min-width:0;border-top:4px solid var(--accent)}
@media(max-width:600px){.ohc-intro .lead{font-size:1rem;margin-bottom:0}.ohc-intro h1{margin-bottom:.35em}}
.ohc-top{display:flex;justify-content:space-between;align-items:center;min-height:28px;font-size:.9rem;color:var(--muted)}
.ohc-teller b{color:var(--ink)}
.ohc-balk{height:5px;border-radius:99px;background:var(--line);margin:8px 0 20px;overflow:hidden}
.ohc-balk i{display:block;height:100%;background:var(--accent);border-radius:99px;transition:width .3s ease}
.ohc-q{border:0;margin:0;padding:0;min-width:0;animation:fade .22s ease}
.ohc-vraag{font-size:1.28rem;font-weight:750;color:var(--ink);line-height:1.25;padding:0;margin:0 0 6px;letter-spacing:-.01em}
.ohc-hint{font-size:.93rem;color:var(--muted);margin:0 0 16px}
.ohc-opts{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
@media(max-width:480px){.ohc-opts{grid-template-columns:minmax(0,1fr)}}
.ohc-opt{display:flex;align-items:center;gap:12px;text-align:left;font:inherit;color:var(--ink);background:#fff;border:1.5px solid var(--line);border-left-width:5px;border-radius:var(--radius);padding:12px 14px;cursor:pointer;min-height:64px;transition:border-color .15s,background .15s,transform .1s}
.ohc-opt:hover{border-color:var(--navy-500);background:var(--bg-soft)}
.ohc-opt:active{transform:scale(.98)}
.ohc-opt:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
.ohc-opt.gekozen{border-color:var(--accent);background:var(--accent-soft);box-shadow:0 0 0 3px rgba(244,130,11,.15)}
.ohc-t-g{border-left-color:#0f8a5f}.ohc-t-o{border-left-color:#e2a80c}.ohc-t-r{border-left-color:#c0392b}.ohc-t-n{border-left-color:var(--line)}
.ohc-ico{flex:0 0 40px;height:40px;border-radius:10px;background:var(--bg-soft);display:grid;place-items:center;color:var(--navy-500)}
.ohc-txt{display:flex;flex-direction:column;min-width:0}
.ohc-lbl{font-weight:700;line-height:1.25}
.ohc-sub{font-size:.84rem;color:var(--muted);line-height:1.3;margin-top:2px}
.ohc-kicker{text-transform:uppercase;letter-spacing:.06em;font-size:.78rem;font-weight:750;color:var(--muted);margin:0 0 4px;text-align:center}
.ohc-meterwrap{max-width:300px;margin:0 auto}
.ohc-meter{width:100%;height:auto;display:block}
.ohc-naald{transform-origin:120px 120px;transition:transform 1.1s cubic-bezier(.3,1.4,.5,1)}
.ohc-niveau{text-align:center;margin:8px 0 6px;font-size:clamp(1.5rem,3vw,2rem)}
.ohc-samenvatting{text-align:center;max-width:56ch;margin:0 auto 22px}
.ohc-blokken{display:grid;gap:12px;margin-bottom:22px}
.ohc-blok{border:1px solid var(--line);border-radius:var(--radius);padding:16px 18px;background:#fff}
.ohc-blok h3{font-size:1.02rem;margin:0 0 6px;display:flex;gap:8px;align-items:center}
.ohc-blok h3 span{display:inline-grid;place-items:center;width:26px;height:26px;border-radius:8px;background:var(--accent-soft);color:var(--accent-dark);font-size:.85rem}
.ohc-blok p,.ohc-blok ul{font-size:.95rem;margin:0 0 6px}
.ohc-blok p:last-child,.ohc-blok ul:last-child{margin-bottom:0}
.ohc-blok .ohc-prijs{font-size:1.3rem;font-weight:800;color:var(--ink);margin:2px 0 4px}
.ohc-blok figure{margin:10px 0 0}
.ohc-blok figure img{border-radius:10px}
.ohc-acties{text-align:center;margin:0 0 22px}
.ohc-acties .btn{width:100%;max-width:420px;white-space:normal}
.ohc-klein{font-size:.84rem;color:var(--muted);margin:8px 0 0}
.ohc-agenda{background:var(--bg-soft);border-radius:var(--radius);padding:18px}
.ohc-agenda h3{font-size:1.02rem;margin:0 0 4px}
.ohc-agenda-tekst{font-size:.95rem;margin:0 0 10px}
.ohc-agenda-rij{display:flex;gap:10px;flex-wrap:wrap}
.ohc-agenda-rij input{flex:1 1 160px;min-width:0;font:inherit;padding:10px 12px;border:1.5px solid var(--line);border-radius:10px;background:#fff;color:var(--ink)}
.ohc-agenda-rij .btn{flex:0 0 auto}
.ohc-sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}
.ohc-opnieuw{text-align:center;margin:16px 0 0}
.ohc-n0 .ohc-niveau{color:#0f8a5f}.ohc-n1 .ohc-niveau{color:#a87a00}.ohc-n2 .ohc-niveau{color:#d96f00}.ohc-n3 .ohc-niveau{color:#c0392b}
@media(max-width:480px){.ohc-card{padding:20px 16px}.ohc-vraag{font-size:1.15rem}.ohc-blok{padding:14px}}
@media(prefers-reduced-motion:reduce){.ohc-naald,.ohc-balk i{transition:none}.ohc-q{animation:none}}
</style>"""


# ---------------------------------------------------------------------------
# JavaScript (alleen voor deze pagina, draait volledig in de browser)
# ---------------------------------------------------------------------------

PAGE_JS = r"""<script>
(function () {
  "use strict";
  var root = document.querySelector("[data-ohc]");
  if (!root) return;
  var DATA = JSON.parse(document.getElementById("ohc-data").textContent);
  var P = DATA.prijzen, L = DATA.labels;
  var vragen = [].slice.call(root.querySelectorAll(".ohc-q"));
  var quiz = root.querySelector(".ohc-quiz"), uitslag = root.querySelector(".ohc-uitslag");
  var teller = root.querySelector(".ohc-teller b"), balk = root.querySelector(".ohc-balk i");
  var terug = root.querySelector(".ohc-terug"), card = root.querySelector(".ohc-card");
  var ans = {}, idx = 0, res = null;

  function euro(n) { return "\u20ac" + String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g, "."); }
  function band(b) { return euro(b[0]) + " \u2013 " + euro(b[1]); }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  function toon(i) {
    idx = i;
    vragen.forEach(function (q, n) { q.hidden = n !== i; });
    teller.textContent = i + 1;
    balk.style.width = ((i + 1) / vragen.length * 100) + "%";
    terug.hidden = i === 0;
    var k = vragen[i].dataset.key;
    [].forEach.call(vragen[i].querySelectorAll(".ohc-opt"), function (b) {
      b.classList.toggle("gekozen", ans[k] === b.dataset.v);
      b.setAttribute("aria-pressed", ans[k] === b.dataset.v ? "true" : "false");
    });
  }

  function naarBoven(el) {
    var top = el.getBoundingClientRect().top + window.scrollY - 90;
    if (Math.abs(window.scrollY - top) > 60) window.scrollTo({ top: top, behavior: "smooth" });
  }

  vragen.forEach(function (q, n) {
    q.addEventListener("click", function (e) {
      var b = e.target.closest(".ohc-opt");
      if (!b) return;
      ans[q.dataset.key] = b.dataset.v;
      [].forEach.call(q.querySelectorAll(".ohc-opt"), function (x) { x.classList.toggle("gekozen", x === b); });
      setTimeout(function () {
        if (n < vragen.length - 1) {
          toon(n + 1);
          var f = vragen[n + 1].querySelector(".ohc-opt");
          if (f && document.activeElement && document.activeElement.classList.contains("ohc-opt")) f.focus({ preventScroll: true });
        } else {
          bereken();
        }
      }, 170);
    });
  });
  terug.addEventListener("click", function () { if (idx > 0) toon(idx - 1); });

  /* ------------------------------------------------------------ uitslag */
  function bereken() {
    var a = ans, s = 0;
    // leeftijd van de verflaag tegenover de termijn voor een nieuwe laag (zie INTERVAL)
    var iv = INTERVAL[a.afwerking] || INTERVAL.onbekend;
    var jaren = { "0-2": 1, "3-5": 4, "6-8": 7, "8+": 10 }[a.leeftijd];
    var ratio = jaren ? jaren / iv.nieuw : null;
    s += ratio === null ? 2 : ratio < 0.5 ? 0 : ratio < 0.9 ? 1.5 : ratio < 1.3 ? 3.5 : 5;
    s += { zon: 1, open: 1, schaduw: 0, onbekend: 0.5 }[a.ligging] || 0;
    s += { nee: 0, beetje: 2, veel: 4 }[a.bladderen] || 0;
    s += { nee: 0, beetje: 1, veel: 2 }[a.krijten] || 0;
    s += { dicht: 0, scheurtjes: 1, open: 3 }[a.naden] || 0;
    s += { hard: 0, twijfel: 2, zacht: 0 }[a.zacht] || 0;
    s += { voor1945: 0.5, "1945-1980": 0.5 }[a.bouw] || 0;

    var n;
    if (a.zacht === "zacht") n = 3;
    else if (s >= 7) n = 2;
    else if (s >= 3) n = 1;
    else n = 0;
    if (n < 2 && (a.bladderen === "veel" || a.naden === "open" || (ratio !== null && ratio >= 1.3))) n = 2;
    if (n < 1 && (a.zacht === "twijfel" || (ratio !== null && ratio >= 0.9))) n = 1;

    // positie van de naald binnen het vak: hoe hoger de score, hoe verder
    var grenzen = [[0, 3], [3, 7], [7, 14], [0, 1]];
    var g = grenzen[n], frac = n === 3 ? 0.55 : Math.max(0.12, Math.min(0.88, (s - g[0]) / (g[1] - g[0])));
    var hoek = -90 + n * 45 + frac * 45;
    res = { n: n, s: s, hoek: hoek, iv: iv, ratio: ratio };
    toonUitslag();
  }

  /* Termijnen uit de onderhoudsschema's van de timmerindustrie (NBvT/SGT) en
     de verffabrikanten: bijwerken en een geheel nieuwe laag, in jaren. */
  var INTERVAL = {
    licht: { bij: 3, nieuw: 6, naam: "lichte dekkende verf" },
    donker: { bij: 2, nieuw: 4, naam: "donkere dekkende verf" },
    transparant: { bij: 1, nieuw: 2, naam: "een transparant systeem" },
    onbekend: { bij: 3, nieuw: 6, naam: "dekkende verf (we gaan uit van een lichte kleur)" }
  };

  function waarom() {
    var a = ans, iv = res.iv, r = [];
    r.push("Bij " + iv.naam + " rekenen de onderhoudsschema's van de timmerindustrie met bijwerken na ongeveer " + iv.bij + " jaar en een nieuwe laag na ongeveer " + iv.nieuw + " jaar." + (a.afwerking === "transparant" ? " Transparant moet dus eigenlijk elk jaar even worden nagelopen." : ""));
    if (res.ratio !== null) {
      r.push(res.ratio >= 1.3 ? "Je laatste beurt is duidelijk langer geleden dan die termijn." :
        res.ratio >= 0.9 ? "Je laatste beurt zit rond die termijn." :
        res.ratio >= 0.5 ? "Je zit ongeveer halverwege die termijn: een goed moment om te controleren en klein onderhoud te doen." :
        "Je laatste beurt is nog vrij recent.");
    } else r.push("Je weet niet wanneer er voor het laatst is geschilderd. Daarom tellen de signalen die je ziet extra zwaar.");
    if (a.ligging === "zon") r.push("De zon- en regenkant (zuid en west) slijt sneller dan de schaduwkant. Daar zie je het eerst kale plekken en verpoedering, vooral op de onderdorpels.");
    if (a.ligging === "open") r.push("Bij een open ligging aan het water of in de polder krijgt de verf veel wind en regen. De schema's noemen daarvoor geen apart getal; wij raden aan om de kortste termijn aan te houden.");
    if (a.afwerking === "donker" && (a.ligging === "zon" || a.ligging === "open")) r.push("Een donkere kleur op de zonkant wordt veel warmer dan een lichte. Het hout krimpt en zwelt meer, waardoor de verf sneller loslaat.");
    var sig = { bladderen: { beetje: "Je ziet hier en daar afbladderende verf.", veel: "Je ziet grote stukken afbladderende verf of kaal hout: daar trekt vocht in." },
      krijten: { beetje: "De verf krijt een beetje: de toplaag wordt dunner.", veel: "De verf krijt duidelijk: de beschermende laag is grotendeels weg." },
      naden: { scheurtjes: "Er zitten haarscheurtjes in de naden.", open: "Er zijn open naden of losse kit: daar loopt water achter de verf." },
      zacht: { twijfel: "Je twijfelt over zachte of donkere plekken: laat die nakijken.", zacht: "Het hout bij de dorpels of hoeken is zacht: dat wijst op houtrot." } };
    Object.keys(sig).forEach(function (k) { if (sig[k][a[k]]) r.push(sig[k][a[k]]); });
    return "<ul>" + r.map(function (x) { return "<li>" + x + "</li>"; }).join("") + '</ul><p><a href="#termijnen">Waar deze termijnen vandaan komen</a></p>';
  }

  function checklist() {
    var items = [["afbladderen", "Afbladderen", "Loszittende verf of blaasjes, vooral onder aan kozijnen en op dorpels."],
      ["scheuren", "Scheuren", "Haarscheurtjes in de verf en open naden waar stukken hout samenkomen."],
      ["kaal", "Kale plekken", "Grijs, kaal hout op scherpe kanten en op de zonkant."],
      ["zacht", "Zachte plekken", "Prik met een schroevendraaier in dorpels en onderhoeken: geeft het hout mee?"]];
    return '<ul class="ohc-check">' + items.map(function (i) {
      return '<li><label><input type="checkbox"> <span><strong>' + i[1] + ".</strong> " + i[2] + ' <a href="#check-' + i[0] + '">Zo ziet het eruit</a></span></label></li>';
    }).join("") + "</ul><p class=\"ohc-klein\">Vink af wat je bent nagelopen. Er wordt niets opgeslagen.</p>";
  }

  function moment() {
    var m = new Date().getMonth() + 1;
    if (m >= 11 || m <= 2) return "Vraag nu offertes aan, dan sta je op tijd in de planning voor april tot juni. Wie in het voorjaar pas belt, staat achteraan in de rij.";
    if (m <= 6) return "Het seizoen is begonnen en schilders plannen nu de zomer vol. Vraag snel offertes aan, of mik op september en oktober: dan is het vaak droog en hebben schilders meer ruimte.";
    if (m <= 8) return "Mik op september of oktober. Dan is het vaak droog en mild, en hebben schilders meer ruimte dan in het voorjaar.";
    return "Het buitenseizoen loopt tot en met oktober. Lukt het niet meer, plan dan voor het voorjaar en vraag in januari of februari offertes aan.";
  }

  function kostenBlok() {
    var w = a_woning(), regels = "";
    if (w) {
      regels = '<p class="ohc-prijs">' + band(P.woning[w]) + '</p><p>Richtprijs voor de buitenkant van een ' + esc(L.woning[ans.woning].toLowerCase()) + ', met kozijnen, deuren en boeidelen.</p>';
    } else {
      regels = '<p class="ohc-prijs">' + band(P.kozijn) + ' per kozijn</p><p>In een appartementencomplex regelt de VvE het buitenschilderwerk meestal voor het hele gebouw. Heb je eigen kozijnen, dan is dit de richtprijs per kozijn.</p>';
    }
    regels += "<ul>";
    if (res.n === 3 || ans.zacht === "twijfel") regels += "<li>Houtrot herstellen: " + band(P.houtrot) + " per plek</li>";
    if (w) regels += "<li>Steiger of hoogwerker, als die nodig is: " + band(P.steiger) + " per gevel</li>";
    var bron = w ? "/kosten/huis-schilderen/" : "/kosten/kozijnen-schilderen/";
    regels += '</ul><p><a href="' + bron + '">Zo is deze prijs opgebouwd</a> \u00b7 <a href="/kosten/kozijnen-schilderen/">kozijnen schilderen</a></p>';
    return blok("\u20ac", "Wat het ongeveer kost", regels);
  }
  function a_woning() { return ans.woning === "appartement" ? null : ans.woning; }

  function blok(icoon, titel, html) {
    return '<div class="ohc-blok"><h3><span>' + icoon + "</span>" + titel + "</h3>" + html + "</div>";
  }

  var BOUW = {
    "voor1945": "Bij een vooroorlogse woning zitten vaak veel oude verflagen op het houtwerk. Een schilder kijkt dan extra goed naar lagen die loslaten en naar naden die zijn gaan werken.",
    "1945-1980": "Bij woningen uit deze periode zijn de kozijnen vaak van zachtere houtsoorten. Open naden laten daar sneller houtrot toe, dus houd de dorpels en onderhoeken goed in de gaten.",
    "1980-2000": "Bij woningen uit deze periode is het houtwerk vaak nog goed als het op tijd is onderhouden. Let vooral op de dorpels en de onderhoeken.",
    "na2000": "Nieuwere kozijnen hebben vaak een goede fabrieksafwerking, maar ook daarvoor rekenen de onderhoudsschema's met een nieuwe laag na ongeveer zes jaar bij een lichte kleur en vier jaar bij een donkere. Zijn je kozijnen van kunststof? Dan gaat het vooral om deuren en boeidelen."
  };

  function toonUitslag() {
    var n = res.n, a = ans;
    var titels = ["Je schilderwerk is in orde", "Binnenkort aan de beurt", "Nu laten schilderen", "Kans op houtrot: laat het nakijken"];
    var samen = [
      "De verflaag beschermt je houtwerk nog goed. Met een beetje onderhoud houd je dat zo.",
      "Er zijn de eerste signalen van slijtage. Plan een schilderbeurt in de komende een tot twee jaar, dan voorkom je houtrot.",
      "De verflaag beschermt je houtwerk niet goed meer. Laat het in het eerstvolgende schilderseizoen doen, voordat er water in het hout trekt.",
      "Zacht hout bij dorpels of hoeken wijst vaak op houtrot. Laat een schilder het zo snel mogelijk bekijken: houtrot breidt zich uit zolang het nat blijft."
    ];
    var nu = [
      "<ul><li>Was je kozijnen een of twee keer per jaar met water en een scheutje allesreiniger. Vuil houdt vocht vast.</li><li>Kijk elk voorjaar even naar de kit en de dorpels.</li><li>" + (a.leeftijd === "0-2" ? "Reken op klein onderhoud na ongeveer " + res.iv.bij + " jaar en een nieuwe laag na ongeveer " + res.iv.nieuw + " jaar na de vorige beurt." : "Doe de check volgend jaar nog eens; de schema's adviseren een jaar voor het bijwerken een controle.") + "</li></ul>",
      "<ul><li>Maak foto's van de plekken die je opvallen, dan kan een schilder sneller een prijs geven.</li><li>Laat losse kit en kleine scheurtjes alvast bijwerken; dat voorkomt erger.</li><li>Vraag op tijd offertes aan, zodat je kunt kiezen wanneer het past.</li></ul>",
      "<ul><li>Vraag offertes aan bij een paar schilders en vergelijk ze.</li><li>Vraag in de offerte naar de voorbereiding, het aantal lagen en hoe eventuele houtrot wordt afgerekend.</li><li>Wacht niet nog een winter: vocht en vorst maken de schade groter.</li></ul>",
      "<ul><li>Laat een schilder het houtwerk ter plekke beoordelen. Vaak is houtrot met een reparatie op te lossen, zonder het kozijn te vervangen.</li><li>Vraag om een stelpost met een maximum voor houtrot, niet om &quot;houtrot in regie&quot;.</li><li>Laat het herstel en het schilderen in \u00e9\u00e9n keer doen.</li></ul>"
    ];

    var blokken = blok("#", "Waarom dit advies", waarom());
    blokken += blok("#", "Wat je nu doet", nu[n]);
    blokken += blok("#", "Loop het zelf even na", checklist());
    if (n === 3) blokken += blok("!", "Houtrot herstellen", '<p>Een schilder haalt het rotte hout weg en vult het aan met een houtreparatiemiddel of een nieuw stuk hout. Lees <a href="/schilderwerk/houtrot-reparatie/">hoe houtrot reparatie werkt en wat het kost</a>.</p>');
    if (n >= 1) blokken += kostenBlok();
    if (n >= 1) blokken += blok("#", "Het beste moment", "<p>" + moment() + '</p><p><a href="/gids/wanneer-buiten-schilderen/">Wanneer kun je buiten schilderen?</a></p>');
    if (a.bouw && BOUW[a.bouw]) blokken += blok("#", "Over jouw woning", "<p>" + BOUW[a.bouw] + "</p>" + (a.ligging === "zon" || a.ligging === "open" ? "<p>Jouw zware kant krijgt veel zon, regen of wind. Die kant heeft vaak eerder een beurt nodig dan de rest.</p>" : ""));
    if (n === 0) blokken += kostenBlok();

    uitslag.className = "ohc-uitslag ohc-n" + n;
    uitslag.querySelector(".ohc-niveau").textContent = titels[n];
    uitslag.querySelector(".ohc-samenvatting").textContent = samen[n];
    var nr = 0;
    uitslag.querySelector(".ohc-blokken").innerHTML = blokken.replace(/<span>#<\/span>/g, function () { return "<span>" + (++nr) + "</span>"; });
    uitslag.querySelector(".ohc-naar-offerte").textContent = n === 0 ? "Toch al een prijs? Vul het offerteformulier in" : "Vul het offerteformulier vast in";

    // herinnering
    var d = herinnerDatum(n), tekst = [
      "Kies wanneer je de check opnieuw wilt doen. Wij stellen over een jaar voor, in het voorjaar.",
      "Een geheugensteuntje om op tijd offertes aan te vragen, zodat je in het voorjaar kunt laten schilderen.",
      "Een geheugensteuntje om deze week offertes aan te vragen.",
      "Een geheugensteuntje om deze week een schilder te laten kijken."
    ][n];
    uitslag.querySelector(".ohc-agenda-tekst").textContent = tekst;
    var inp = uitslag.querySelector("#ohc-datum");
    inp.min = iso(new Date());
    inp.value = iso(d);

    quiz.hidden = true;
    uitslag.hidden = false;
    root.classList.add("klaar");
    var naald = uitslag.querySelector(".ohc-naald");
    naald.style.transform = "rotate(-80deg)";
    naarBoven(card);
    setTimeout(function () { naald.style.transform = "rotate(" + res.hoek.toFixed(1) + "deg)"; }, 250);
    uitslag.querySelector(".ohc-niveau").setAttribute("tabindex", "-1");
    uitslag.querySelector(".ohc-niveau").focus({ preventScroll: true });
  }

  /* ---------------------------------------------------------- agenda */
  function iso(d) { return d.getFullYear() + "-" + ("0" + (d.getMonth() + 1)).slice(-2) + "-" + ("0" + d.getDate()).slice(-2); }
  function herinnerDatum(n) {
    var t = new Date(); t.setHours(12, 0, 0, 0);
    if (n >= 2) { t.setDate(t.getDate() + 7); return t; }
    if (n === 1) {
      // 15 januari: op tijd offertes aanvragen voor het voorjaar
      var j = new Date(t.getFullYear(), 0, 15, 12);
      if (j - t < 14 * 864e5) j = new Date(t.getFullYear() + 1, 0, 15, 12);
      return j;
    }
    var m = new Date(t.getFullYear() + 1, 2, 1, 12); // 1 maart volgend jaar
    if (m - t > 18 * 30 * 864e5) m = new Date(t.getFullYear(), 2, 1, 12);
    return m;
  }
  function icsTekst(s) { return String(s).replace(/\\/g, "\\\\").replace(/;/g, "\\;").replace(/,/g, "\\,").replace(/\r?\n/g, "\\n"); }
  function vouw(r) { var o = ""; while (r.length > 60) { o += r.slice(0, 60) + "\r\n "; r = r.slice(60); } return o + r; }
  function samenvatting() {
    var k = ["leeftijd", "ligging", "afwerking", "bladderen", "krijten", "naden", "zacht", "woning", "bouw"];
    var namen = { leeftijd: "Laatst geschilderd", ligging: "Zwaarste kant", afwerking: "Afwerking", bladderen: "Afbladderen", krijten: "Krijten", naden: "Naden en kit", zacht: "Hout bij dorpels", woning: "Woning", bouw: "Bouwperiode" };
    return k.filter(function (x) { return ans[x]; }).map(function (x) { return namen[x] + ": " + L[x][ans[x]]; });
  }
  root.querySelector(".ohc-ics").addEventListener("click", function () {
    var v = root.querySelector("#ohc-datum").value;
    if (!/^\d{4}-\d{2}-\d{2}$/.test(v)) return;
    var start = new Date(v + "T12:00:00"), eind = new Date(start.getTime() + 864e5);
    var d1 = v.replace(/-/g, ""), d2 = iso(eind).replace(/-/g, "");
    var nu = new Date().toISOString().replace(/[-:]/g, "").replace(/\.\d+/, "");
    var titel = ["Onderhoudscheck schilderwerk opnieuw doen", "Offertes buitenschilderwerk aanvragen", "Offertes buitenschilderwerk aanvragen", "Schilder laten kijken naar houtrot"][res.n];
    var oms = "Uitslag onderhoudscheck: " + DATA.meter[res.n] + ".\n" + samenvatting().join("\n") + "\n\nOpnieuw doen of offertes aanvragen: https://topschilder.nl/onderhoudscheck/";
    var r = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Topschilder.nl//Onderhoudscheck//NL", "CALSCALE:GREGORIAN", "METHOD:PUBLISH",
      "BEGIN:VEVENT", "UID:" + Date.now().toString(36) + Math.random().toString(36).slice(2, 10) + "@topschilder.nl", "DTSTAMP:" + nu,
      "DTSTART;VALUE=DATE:" + d1, "DTEND;VALUE=DATE:" + d2, "SUMMARY:" + icsTekst(titel), "DESCRIPTION:" + icsTekst(oms),
      "URL:https://topschilder.nl/onderhoudscheck/", "TRANSP:TRANSPARENT",
      "BEGIN:VALARM", "ACTION:DISPLAY", "DESCRIPTION:" + icsTekst(titel), "TRIGGER:PT9H", "END:VALARM",
      "END:VEVENT", "END:VCALENDAR"].map(vouw).join("\r\n") + "\r\n";
    var blob = new Blob([r], { type: "text/calendar;charset=utf-8" });
    var url = URL.createObjectURL(blob), link = document.createElement("a");
    link.href = url; link.download = "herinnering-schilderwerk.ics";
    document.body.appendChild(link); link.click(); link.remove();
    setTimeout(function () { URL.revokeObjectURL(url); }, 4000);
  });

  /* ------------------------------------------ offerteformulier invullen */
  root.querySelector(".ohc-naar-offerte").addEventListener("click", function () {
    var box = document.getElementById("offerte");
    var form = box && box.querySelector("form[data-wizard]");
    if (!form) { location.href = "/offerte-aanvragen/?dienst=Buitenschilderwerk"; return; }
    var dienst = res.n === 3 ? "Houtrot reparatie" : "Buitenschilderwerk";
    var planning = ["Nog aan het ori\u00ebnteren", "Over 3-6 maanden", "Binnen 1-3 maanden", "Zo snel mogelijk"][res.n];
    function kies(naam, waarde) {
      [].forEach.call(form.querySelectorAll('input[name="' + naam + '"]'), function (i) { i.checked = i.value === waarde; });
    }
    kies("dienst", dienst);
    kies("planning", planning);
    var oms = form.querySelector('textarea[name="omschrijving"]');
    if (oms && (!oms.value || oms.value.indexOf("Onderhoudscheck") === 0)) {
      oms.value = ("Onderhoudscheck: " + DATA.meter[res.n] + ". " + samenvatting().join(". ") + ".").slice(0, 900);
    }
    var actief = form.querySelector(".step.active");
    var eerste = form.querySelector(".step");
    if (actief === eerste) { var nx = eerste.querySelector("[data-next]"); if (nx) nx.click(); }
    naarBoven(box);
    setTimeout(function () { var pc = form.querySelector('input[name="postcode"]'); if (pc && !pc.value) pc.focus({ preventScroll: true }); }, 500);
  });

  root.querySelector(".ohc-reset").addEventListener("click", function () {
    ans = {}; res = null;
    uitslag.hidden = true; quiz.hidden = false; root.classList.remove("klaar");
    toon(0);
    naarBoven(card);
  });

  toon(0);
})();
</script>"""
