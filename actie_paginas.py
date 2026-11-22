# -*- coding: utf-8 -*-
"""Landingspagina's voor betaalde social ads (Meta, Pinterest, TikTok): /actie/<slug>/.

- Staan op noindex en niet in de sitemap: ze zijn alleen bedoeld voor advertentieverkeer.
- Kort formulier (2 stappen) dat via dezelfde wizard en dezelfde tabel ('leads') verstuurt als
  het gewone aanvraagformulier. UTM-tags en fbclid worden door app.js opgeslagen en meegestuurd.
- ?regio=<plaats-slug of regio> zet de plaatsnaam in de kop (alleen namen uit een vaste lijst)
  en vult bij een plaats ook het veld Plaats alvast in.

Alleen echte voordelen: gratis, vrijblijvend, maximaal 3 offertes, richtprijzen, 9% btw.
Geen reviews, sterren, aantallen schilders of kortingen.
"""

import json

from data import PLAATSEN, DIENSTEN
from foto_data import FOTOS
from components import page, icon, eur, foto_kader, faq_blok, prijs_balken

_DIENST = {d["slug"]: d for d in DIENSTEN}

REGIO_NAMEN = {p["slug"]: p["naam"] for p in PLAATSEN}
REGIO_GEBIEDEN = {"flevoland": "Flevoland", "gooi": "het Gooi", "veluwe": "de Veluwe",
                  "noordoostpolder": "de Noordoostpolder"}

KEUKEN_BTW_FAQ = ("Betaal ik 9% of 21% btw?",
                  "Dat hangt af van hoe het werk gebeurt en hoe de schilder het factureert. Vraag de schilder om "
                  "het btw-tarief op de offerte te zetten.")
BTW_FAQ = ("Betaal ik 9% of 21% btw?",
           "Voor schilderwerk aan een woning die ouder is dan twee jaar geldt 9% btw, op het werk én de "
           "materialen. Vraag de schilder om dat op de offerte te zetten.")
CONTACT_FAQ = ("Hoeveel schilders nemen contact met mij op?",
               "Maximaal drie. Je gegevens gaan alleen naar die schilders en naar niemand anders. Je zit "
               "nergens aan vast: alle offertes afwijzen mag, zonder uitleg.")
KOSTEN_FAQ = ("Wat kost het aanvragen?",
              "Niets. Aanvragen en vergelijken is gratis. Wij worden betaald door de schilders die je "
              "aanvraag ontvangen.")

ACTIES = [
    {
        "slug": "buitenschilderwerk",
        "dienst": "buitenschilderwerk",
        "title": "Buitenschilderwerk: tot 3 offertes | Topschilder",
        "description": "Laat je kozijnen, deuren en boeidelen schilderen. Vraag gratis en vrijblijvend tot 3 offertes aan bij schilders uit je regio.",
        "badge": "Gratis &amp; vrijblijvend",
        "h1": "Kozijnen laten schilderen<span data-regio></span>?",
        "lead": "Vraag in een minuut tot 3 offertes aan bij schilders uit je regio. Plan nu, dan sta je vooraan als het weer goed is.",
        "omvang_vraag": "Wat moet er geschilderd worden?",
        "omvang": [
            ("Buiten: alleen kozijnen en/of deuren", "Kozijnen of deuren"),
            ("Buiten: kozijnen, deuren en boeidelen", "Kozijnen + boeidelen"),
            ("Buiten: de hele buitenkant", "Hele buitenkant"),
            ("Buiten: weet ik nog niet, graag advies", "Weet ik nog niet"),
        ],
        "prijzen": [("Per kozijn", 90, 190), ("Per dakkapel", 400, 950),
                    ("Buitenkant tussenwoning", 2200, 5500)],
        "prijs_eenheid": "Richtprijzen inclusief materiaal en btw",
        "tools": [("/onderhoudscheck/", "Doe eerst de onderhoudscheck", "Acht vragen: is je schilderwerk aan de beurt?"),
                  ("/schilderweer/", "Bekijk het schilderweer", "Kan er deze week buiten geschilderd worden?"),
                  ("/kleuren-kiezen/", "Kies je kozijnkleur", "Probeer kleuren uit op een huis zoals het jouwe.")],
        "faq": [("Wanneer kan er buiten geschilderd worden?",
                 "Meestal van april tot en met oktober. Het moet droog zijn en minstens een graad of 8 tot 10. "
                 "Goede schilders plannen het voorjaar vaak al in de winter vol, dus vroeg aanvragen helpt."),
                BTW_FAQ, CONTACT_FAQ, KOSTEN_FAQ],
    },
    {
        "slug": "keuken-spuiten",
        "dienst": "spuitwerk",
        "title": "Keuken laten spuiten: tot 3 offertes | Topschilder",
        "description": "Je keukenkastjes in een nieuwe kleur zonder nieuwe keuken. Vraag gratis tot 3 offertes aan voor keuken spuiten bij schilders uit je regio.",
        "badge": "Binnenklus voor de winter",
        "usp3": "Richtprijzen vooraf, zodat je de offertes kunt vergelijken",
        "h1": "Keuken laten spuiten<span data-regio></span>?",
        "lead": "Nieuwe kleur, zelfde keuken. Vraag in een minuut tot 3 offertes aan bij schilders die keukens spuiten.",
        "omvang_vraag": "Hoe groot is je keuken?",
        "omvang": [
            ("Keuken: klein (tot ongeveer 10 fronten)", "Klein, tot 10 fronten"),
            ("Keuken: gemiddeld (ongeveer 16 fronten)", "Gemiddeld, ± 16 fronten"),
            ("Keuken: groot (20 fronten of meer, of eiland)", "Groot, 20+ fronten"),
            ("Keuken: weet ik nog niet", "Weet ik nog niet"),
        ],
        "prijzen": [("Kleine keuken, 10 fronten", 450, 950), ("Gemiddeld, 16 fronten", 720, 1520),
                    ("Groot, 24 fronten", 1080, 2280)],
        "prijs_eenheid": "Richtprijzen: €45 tot €95 per front (deur of la), inclusief materiaal en btw",
        "tools": [("/kosten/keuken-spuiten/", "Wat kost keuken spuiten?", "Rekenvoorbeelden en waar het prijsverschil in zit."),
                  ("/offerte-vergelijken/", "Al een offerte? Laat hem checken", "Leg je offerte naast onze richtprijzen."),
                  ("/kleuren-kiezen/", "Kleuren uitproberen", "Kijk welke kleur je mooi vindt.")],
        "faq": [("Hoelang kan ik mijn keuken niet gebruiken?",
                 "Reken op drie tot vijf werkdagen voor de hele klus. Je keuken is meestal één tot twee dagen niet "
                 "te gebruiken, vooral als de fronten in de werkplaats worden gespoten."),
                KEUKEN_BTW_FAQ, CONTACT_FAQ, KOSTEN_FAQ],
    },
    {
        "slug": "binnenschilderwerk",
        "dienst": "binnenschilderwerk",
        "title": "Binnenschilderwerk: tot 3 offertes | Topschilder",
        "description": "Muren, plafonds, deuren of trap laten schilderen? Vraag gratis en vrijblijvend tot 3 offertes aan bij schilders uit je regio.",
        "badge": "Binnenklus voor de winter",
        "h1": "Binnen laten schilderen<span data-regio></span>?",
        "lead": "Muren, plafonds, deuren of de trap. Vraag in een minuut tot 3 offertes aan bij schilders uit je regio.",
        "omvang_vraag": "Wat moet er geschilderd worden?",
        "omvang": [
            ("Binnen: één kamer", "Eén kamer"),
            ("Binnen: meerdere kamers", "Meerdere kamers"),
            ("Binnen: hele woning", "Hele woning"),
            ("Binnen: deuren, kozijnen of trap", "Deuren of trap"),
        ],
        "prijzen": [("Muren en plafonds, per m²", 10, 22), ("Binnendeur, per stuk", 65, 140),
                    ("Trap, per verdieping", 350, 950)],
        "prijs_eenheid": "Richtprijzen inclusief materiaal en btw",
        "tools": [("/kosten/calculator/", "Bereken je prijs", "Wat kost het schilderen van jouw huis?"),
                  ("/kleuren-kiezen/", "Kleuren uitproberen", "Kijk welke kleur bij je past."),
                  ("/offerte-vergelijken/", "Al een offerte? Laat hem checken", "Leg je offerte naast onze richtprijzen.")],
        "faq": [("Kan binnenschilderwerk ook in de winter?",
                 "Ja. Binnen maakt het weer niet uit, en in de winter hebben veel schilders meer ruimte in hun "
                 "planning dan in het voorjaar."),
                BTW_FAQ, CONTACT_FAQ, KOSTEN_FAQ],
    },
    {
        "slug": "houtrot",
        "dienst": "houtrot-reparatie",
        "title": "Houtrot laten repareren: tot 3 offertes | Topschilder",
        "description": "Zachte plekken in je kozijn of afbladderende verf? Vraag gratis tot 3 offertes aan voor houtrot repareren en schilderen bij schilders uit je regio.",
        "badge": "Gratis &amp; vrijblijvend",
        "h1": "Houtrot in je kozijnen<span data-regio></span>?",
        "lead": "Hoe eerder je het aanpakt, hoe kleiner de reparatie. Vraag in een minuut tot 3 offertes aan.",
        "omvang_vraag": "Hoeveel plekken zie je?",
        "omvang": [
            ("Houtrot: één of twee plekken", "1 of 2 plekken"),
            ("Houtrot: meerdere kozijnen", "Meerdere kozijnen"),
            ("Houtrot: plus schilderwerk van de buitenkant", "Plus schilderwerk"),
            ("Houtrot: weet ik niet, graag advies", "Weet ik niet"),
        ],
        "prijzen": [("Per reparatieplek", 50, 275), ("Kozijnhoek vervangen", 250, 600)],
        "prijs_eenheid": "Richtprijzen inclusief schilderwerk, materiaal en btw",
        "tools": [("/onderhoudscheck/", "Doe de onderhoudscheck", "Zie hoe je schilderwerk ervoor staat."),
                  ("/kosten/kozijnen-schilderen/", "Wat kost kozijnen schilderen?", "Richtprijzen per kozijn."),
                  ("/schilderweer/", "Bekijk het schilderweer", "Kan er deze week buiten gewerkt worden?")],
        "faq": [("Hoe herken ik houtrot?",
                 "Prik met een schroevendraaier in het hout bij de onderkant van het kozijn of de dorpel. Gaat hij "
                 "er makkelijk in, of bladdert de verf en is het hout donker, dan zit er waarschijnlijk houtrot."),
                BTW_FAQ, CONTACT_FAQ, KOSTEN_FAQ],
    },
]

CSS = """<style>
.actie .hero-in{padding-top:44px;padding-bottom:56px}
.actie h1{font-size:clamp(1.9rem,4.4vw,3rem)}
.actie .formcard h2{font-size:1.35rem}
.actie-meer{font-size:.9rem;margin:12px 0 0;text-align:center}
.actie-tools{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;list-style:none;padding:0;margin:0}
.actie-tools a{display:block;height:100%;background:#fff;border:1px solid var(--line);border-radius:var(--radius-lg);padding:18px 20px;text-decoration:none;color:var(--body)}
.actie-tools a:hover{border-color:var(--accent)}
.actie-tools strong{display:block;color:var(--navy);margin-bottom:4px}
.actie-stappen{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;list-style:none;padding:0;margin:0;counter-reset:s}
.actie-stappen li{background:#fff;border-radius:var(--radius-lg);padding:20px;border:1px solid var(--line)}
.actie-stappen li::before{counter-increment:s;content:counter(s);display:inline-grid;place-items:center;width:32px;height:32px;border-radius:50%;background:var(--accent);color:#fff;font-weight:800;margin-bottom:8px}
.actie-stappen h3{font-size:1.05rem;margin:0 0 4px}
.actie-stappen p{margin:0}
@media(max-width:760px){.actie .hero-in{padding-top:28px;padding-bottom:36px;gap:24px}
.actie-tools,.actie-stappen{grid-template-columns:1fr}
.actie .hero-tags{display:none}}
</style>"""


def _form(a):
    d = _DIENST[a["dienst"]]
    keuzes = "".join(
        f'<label><input type="radio" name="omvang" value="{waarde}" data-required><span>{label}</span></label>'
        for waarde, label in a["omvang"])
    return f"""
<div class="formcard" id="offerte">
  <h2>Ontvang tot 3 offertes</h2>
  <p class="sub">Gratis · vrijblijvend · 2 korte stappen</p>
  <div class="steps"><div class="on"></div><div></div></div>
  <form data-wizard data-table="leads" novalidate>
    <input type="hidden" name="dienst" value="{d['naam']}">
    <div class="step active" data-autoadvance="1">
      <div class="field">
        <label>{a['omvang_vraag']}</label>
        <div class="choice">{keuzes}</div>
      </div>
      <div class="err"></div>
      <div class="formnav"><button type="button" class="btn btn-primary" data-next>Volgende</button></div>
    </div>
    <div class="step">
      <div class="row2">
        <div class="field">
          <label for="a-postcode">Postcode</label>
          <input type="text" id="a-postcode" name="postcode" placeholder="3892 AA" required autocomplete="postal-code">
        </div>
        <div class="field">
          <label for="a-plaats">Plaats</label>
          <input type="text" id="a-plaats" name="plaats" placeholder="Zeewolde" required autocomplete="address-level2">
        </div>
      </div>
      <div class="field">
        <label for="a-naam">Naam</label>
        <input type="text" id="a-naam" name="naam" required autocomplete="name" placeholder="Voor- en achternaam">
      </div>
      <div class="row2">
        <div class="field">
          <label for="a-mail">E-mailadres</label>
          <input type="email" id="a-mail" name="email" required autocomplete="email" placeholder="naam@email.nl">
        </div>
        <div class="field">
          <label for="a-tel">Telefoonnummer</label>
          <input type="tel" id="a-tel" name="telefoon" required autocomplete="tel" placeholder="06 12345678">
        </div>
      </div>
      <div class="err"></div>
      <div class="formnav">
        <button type="button" class="btn btn-ghost" data-prev>Terug</button>
        <button type="submit" class="btn btn-primary" data-submit>Verstuur aanvraag</button>
      </div>
      <p class="formfoot">Door te versturen ga je akkoord met onze <a href="/voorwaarden/">voorwaarden</a> en <a href="/privacy/">privacyverklaring</a>. Je gegevens gaan naar maximaal 3 schilders uit jouw regio, die ons betalen om je aanvraag te ontvangen. Andere partijen krijgen ze niet.</p>
    </div>
  </form>
  <div class="success">
    <div class="big">{icon('check', 26)}</div>
    <h2>Aanvraag ontvangen</h2>
    <p>We zoeken nu schilders in jouw regio die bij deze klus passen. Je krijgt meteen een bevestiging per mail, en je hoort doorgaans binnen één werkdag iets van de schilders. Houd ook je spambox even in de gaten.</p>
    <p><a class="btn btn-ghost" href="/prijzen/">Bekijk alvast wat schilderwerk kost</a></p>
  </div>
</div>
<p class="actie-meer"><a href="/offerte-aanvragen/" style="color:#fff">Meer details kwijt? Gebruik het uitgebreide formulier</a></p>"""


def _regio_js():
    data = json.dumps({"p": REGIO_NAMEN, "g": REGIO_GEBIEDEN}, ensure_ascii=False, separators=(",", ":"))
    # Alleen namen uit deze vaste lijst komen in de pagina; vrije tekst uit de URL nooit.
    return ("<script>(function(){var R=" + data + ";var q='';try{q=(new URLSearchParams(location.search)"
            ".get('regio')||'').toLowerCase()}catch(e){}var n=R.p[q]||R.g[q];if(!n)return;"
            "document.querySelectorAll('[data-regio]').forEach(function(e){e.textContent=' in '+n});"
            "var f=document.getElementById('a-plaats');if(R.p[q]&&f&&!f.value)f.value=n;})();</script>")


def _body(a):
    d = _DIENST[a["dienst"]]
    f = FOTOS[a["dienst"]]
    bg = f["hero"]["naam"]
    usps = "".join(f'<li><span class="check">{icon("check", 12)}</span><span>{t}</span></li>' for t in [
        "Gratis en vrijblijvend, je zit nergens aan vast",
        "Maximaal 3 schilders uit je regio nemen contact op",
        a.get("usp3", "9% btw op schilderwerk aan woningen ouder dan 2 jaar"),
    ])
    tools = "".join(f'<li><a href="{href}"><strong>{kop}</strong>{tekst}</a></li>' for href, kop, tekst in a["tools"])
    prijzen = prijs_balken(a["prijzen"], a["prijs_eenheid"],
                           "Dit zijn richtprijzen. De offertes van de schilders zijn leidend: die hangen af van je woning en de staat van het houtwerk.")
    return f"""{CSS}
<section class="hero hero-foto actie">
<img class="hero-bg" src="/assets/fotos/{bg}-800.webp" srcset="/assets/fotos/{bg}-800.webp 800w, /assets/fotos/{bg}-1600.webp 1600w" sizes="100vw" width="1600" height="1067" alt="" loading="eager" fetchpriority="high" decoding="async">
<div class="wrap hero-in">
  <div>
    <span class="badge badge-dark">{a['badge']}</span>
    <h1>{a['h1']}</h1>
    <p class="lead">{a['lead']}</p>
    <ul class="hero-usps">{usps}</ul>
    <ul class="hero-tags"><li>Flevoland</li><li>Het Gooi</li><li>Veluwe</li><li>Zwolle en Kampen</li><li>Amersfoort</li></ul>
  </div>
  <div>{_form(a)}</div>
</div>
</section>
<section class="section"><div class="wrap">
  <div class="grid g2" style="gap:40px;align-items:center">
    <div>
      <span class="badge">Richtprijzen</span>
      <h2>Wat kost {d['naam'].lower() if a['slug'] != 'keuken-spuiten' else 'keuken spuiten'} ongeveer?</h2>
      {prijzen}
    </div>
    <div>{foto_kader(f['hero'], "(max-width:760px) calc(100vw - 40px), 540px")}</div>
  </div>
</div></section>
<section class="section soft"><div class="wrap">
  <h2>Zo werkt het</h2>
  <ol class="actie-stappen">
    <li><h3>Vul het formulier in</h3><p>Twee korte stappen, klaar in ongeveer een minuut.</p></li>
    <li><h3>Wij zoeken schilders</h3><p>Maximaal drie schilders uit je regio die dit werk doen en ruimte hebben.</p></li>
    <li><h3>Jij vergelijkt en kiest</h3><p>Je krijgt de offertes rechtstreeks. Niets naar je zin? Dan zeg je nee.</p></li>
  </ol>
</div></section>
<section class="section"><div class="wrap">
  <h2>Eerst zelf uitzoeken?</h2>
  <ul class="actie-tools">{tools}</ul>
</div></section>
{faq_blok(a['faq'])[0]}
<section class="section-sm"><div class="wrap center">
  <a class="btn btn-primary" href="#offerte">Vraag gratis offertes aan</a>
</div></section>
{_regio_js()}"""


def build_actie_paginas(write):
    for a in ACTIES:
        html = page(a["title"], a["description"], f"/actie/{a['slug']}/", _body(a), noindex=True)
        # De vaste knop onderin springt hier naar het formulier op de pagina zelf.
        html = html.replace('<div class="sticky-cta"><a class="btn btn-primary btn-block" href="/offerte-aanvragen/">',
                            '<div class="sticky-cta"><a class="btn btn-primary btn-block" href="#offerte">')
        write(f"/actie/{a['slug']}/", html, index=False)
