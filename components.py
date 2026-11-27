# -*- coding: utf-8 -*-
"""Herbruikbare HTML-componenten voor Topschilder.nl"""

import json
from data import SITE, DIENSTEN
from illustraties import illustratie, voor_na
from foto_data import FOTOS
from data import PLAATSEN
from kaart_data import BREEDTE, HOOGTE, PADEN, PUNTEN
import html as _html

# Zet op True zodra je ECHTE reviews hebt verzameld. Verzonnen reviews op een
# live site zijn in Nederland een misleidende handelspraktijk (ACM) en Google
# straft nep-reviewmarkup af. Laat dit dus op False tot je echte klanten hebt.
SHOW_REVIEWS = False

ICONS = {
    "roller": '<path d="M4 5h11v5H4z"/><path d="M15 7.5h3.5a1.5 1.5 0 0 1 1.5 1.5v2a1.5 1.5 0 0 1-1.5 1.5H12v3"/><rect x="10" y="14" width="4" height="7" rx="1"/>',
    "house": '<path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V21h14V9.5"/><path d="M10 21v-6h4v6"/>',
    "wood": '<path d="M3 7h18v10H3z"/><path d="M7 7v10M12 7v10M17 7v10"/>',
    "spray": '<path d="M9 8h6v13H9z"/><path d="M11 8V4h2v4"/><circle cx="18" cy="4" r="1"/><circle cx="20" cy="7" r="1"/><circle cx="18" cy="10" r="1"/>',
    "wall": '<path d="M3 5h18v14H3z"/><path d="M3 10h18M3 15h18M9 5v5M15 10v5M9 15v4"/>',
    "office": '<path d="M4 21V4h10v17"/><path d="M14 10h6v11"/><path d="M7 8h1M11 8h1M7 12h1M11 12h1M7 16h1M11 16h1M17 14h1M17 18h1"/>',
    "check": '<path d="m5 12 5 5 9-10"/>',
    "shield": '<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/><path d="m9 12 2 2 4-4"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "euro": '<path d="M17 6.5A6.5 6.5 0 0 0 7.2 10M17 17.5A6.5 6.5 0 0 1 7.2 14"/><path d="M4 10h8M4 14h8"/>',
    "users": '<circle cx="9" cy="8" r="3.2"/><path d="M3 20a6 6 0 0 1 12 0"/><path d="M16.5 5.5a3.2 3.2 0 0 1 0 5.6M17 14.6A6 6 0 0 1 21 20"/>',
    "form": '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M9 3v2h6V3"/><path d="M9 11h6M9 15h4"/>',
    "match": '<circle cx="11" cy="11" r="6.5"/><path d="m20 20-4.2-4.2"/><path d="m8.5 11 1.8 1.8 3.4-3.6"/>',
}


def _klein(n):
    """Kleine 400px-variant in de srcset, als die bestaat (scheelt veel op mobiel)."""
    import os
    pad = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fotos", f"{n}-400.webp")
    return f"/assets/fotos/{n}-400.webp 400w, " if os.path.exists(pad) else ""


def foto(f, sizes, boven_vouw=False):
    """Responsieve <img> voor een foto uit foto_data.py."""
    n = f["naam"]
    laden = 'loading="eager" fetchpriority="high"' if boven_vouw else 'loading="lazy"'
    alt = f["alt"].replace("&", "&amp;").replace('"', "&quot;")
    return (f'<figure class="foto"><img src="/assets/fotos/{n}-800.webp" '
            f'srcset="{_klein(n)}/assets/fotos/{n}-800.webp 800w, /assets/fotos/{n}-1600.webp 1600w" '
            f'sizes="{sizes}" width="{f["w"]}" height="{f["h"]}" alt="{alt}" {laden} decoding="async"></figure>')



def foto_alleen_desktop(f, sizes, breekpunt=980):
    """seo-ronde 5: voor een foto die onder `breekpunt` op display:none staat en op desktop
    boven de vouw (vaak de LCP) staat. Niet lazy, maar met een lege bron voor smalle schermen,
    zodat een telefoon hem niet downloadt."""
    leeg = "data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=="
    return (foto(f, sizes)
            .replace("<img ", f'<picture><source media="(max-width:{breekpunt}px)" srcset="{leeg}"><img ', 1)
            .replace(' loading="lazy"', ' loading="eager"', 1)
            .replace("</figure>", "</picture></figure>", 1))

def icon(name, size=23):
    p = ICONS.get(name, ICONS["check"])
    return (
        f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" stroke="currentColor" '
        f'stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'
    )


def eur(n):
    return f"€{n:,}".replace(",", ".")


# ---------------------------------------------------------------------------
# Head / header / footer
# ---------------------------------------------------------------------------

def head(title, description, canonical, jsonld=None, depth_ok=True, noindex=False):
    ld = ""
    if jsonld:
        blocks = jsonld if isinstance(jsonld, list) else [jsonld]
        for b in blocks:
            ld += '<script type="application/ld+json">' + json.dumps(b, ensure_ascii=False) + "</script>"
    robots = '<meta name="robots" content="noindex,follow">' if noindex else ""
    return f"""<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{SITE['url']}{canonical}">
{robots}
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE['naam']}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{SITE['url']}{canonical}">
<meta property="og:locale" content="nl_NL">
<meta name="theme-color" content="#3c290f">
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/assets/merk/apple-touch-icon.png"><meta property="og:image" content="https://topschilder.nl/assets/merk/og-image.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="Topschilder.nl: vergelijk schilders bij jou in de buurt"><meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="/assets/css/style.css">
{ld}
</head>"""


def header():
    diensten_nav = ""
    return f"""<header class="header">
<div class="wrap header-in">
  <a class="logo" href="/" aria-label="Topschilder.nl, naar de homepage">
    <img src="/assets/merk/logo.svg" alt="Topschilder.nl" width="816" height="144">
  </a>
  <button class="burger" type="button" aria-label="Menu" aria-expanded="false" aria-controls="hoofdmenu"><span></span><span></span><span></span></button>
  <nav class="nav" id="hoofdmenu" aria-label="Hoofdmenu">
    <a href="/schilderwerk/"><span class="nav-ic">{icon('roller', 20)}</span>Diensten</a>
    <a href="/werkgebied/"><span class="nav-ic">{icon('house', 20)}</span>Werkgebied</a>
    <a href="/prijzen/"><span class="nav-ic">{icon('euro', 20)}</span>Wat kost het?</a>
    <a href="/offerte-vergelijken/"><span class="nav-ic">{icon('match', 20)}</span>Offerte laten checken</a>
    <a href="/voor-schilders/"><span class="nav-ic">{icon('users', 20)}</span>Voor schilders</a>
    <a class="btn btn-primary" href="/offerte-aanvragen/">Offertes aanvragen</a>
    <p class="nav-noot">Gratis en vrijblijvend · maximaal 3 schilders</p>
  </nav>
</div>
</header>{diensten_nav}"""


def footer():
    dl = "".join(f'<li><a href="/schilderwerk/{d["slug"]}/"><span class="f-ic">{dienst_icoon(d["slug"], 18)}</span>{d["naam"]}</a></li>' for d in DIENSTEN)
    pl = "".join(f'<li><a href="/schilder/{p["slug"]}/">{p["naam"]}</a></li>'
                 for p in sorted((p for p in PLAATSEN if p["prio"] == 1), key=lambda x: x["naam"]))
    return f"""<footer class="footer">
<div class="footer-golf" aria-hidden="true"></div>
<div class="wrap">
  <div class="footer-cta">
    <div>
      <p class="footer-cta-titel">Eén aanvraag, maximaal drie offertes</p>
      <p>Gratis en vrijblijvend. Je kiest zelf of je met een van de schilders verder gaat.</p>
    </div>
    <a class="btn btn-primary" href="/offerte-aanvragen/">Offertes aanvragen</a>
  </div>
  <div class="footer-grid">
    <div>
      <a class="logo" href="/" aria-label="Topschilder.nl"><img src="/assets/merk/logo-wit.svg" alt="Topschilder.nl" width="816" height="144" loading="lazy"></a>
      <p style="margin-top:14px;max-width:34ch">Vergelijk vrijblijvend offertes van schilders bij jou in de buurt. Gratis, zonder verplichtingen en met maximaal drie bedrijven die contact opnemen.</p>
      <ul class="footer-tools">
        <li><a href="/tools/">{icon('match', 18)}Gratis tools</a></li>
        <li><a href="/offerte-vergelijken/">{icon('form', 18)}Offerte laten checken</a></li>
      </ul>
    </div>
    <div>
      <h2 class="fh">Diensten</h2>
      <ul class="footer-diensten">{dl}</ul>
    </div>
    <div>
      <h2 class="fh">Handig</h2>
      <ul>
        <li><a href="/prijzen/">Prijzen &amp; tarieven</a></li>
        <li><a href="/kosten/">Kosten per klus</a></li>
        <li><a href="/gids/">Gids</a></li>
        <li><a href="/kennisbank/">Kennisbank</a></li>
        <li><a href="/werkgebied/">Alle plaatsen</a></li>
        <li><a href="/over-ons/">Over Topschilder</a></li>
        <li><a href="/contact/">Contact</a></li>
      </ul>
      <h2 class="fh" style="margin-top:22px">Schilders</h2>
      <ul>
        <li><a href="/voor-schilders/">Aanmelden als schilder</a></li>
        <li><a href="/voor-schilders/#tarieven">Wat kost een lead?</a></li>
        <li><a href="/voor-schilders/#exclusief">Exclusieve leads</a></li>
      </ul>
    </div>
    <div>
      <h2 class="fh">Werkgebied</h2>
      <ul class="footer-plaatsen">{pl}</ul>
      <p style="margin-top:10px"><a href="/werkgebied/" class="footer-meer">Alle {len(PLAATSEN)} plaatsen →</a></p>
    </div>
  </div>
  <div class="footer-bot">
    <div>© {SITE['oprichting']}–2026 {SITE['naam']} · KvK {SITE['kvk']}</div>
    <div><a href="/privacy/">Privacy</a> · <a href="/voorwaarden/">Algemene voorwaarden</a> · <a href="/cookies/">Cookies</a> · <button type="button" class="cookie-instellingen">Cookie-instellingen</button> · <a href="/fotoverantwoording/">Fotoverantwoording</a></div>
  </div>
</div>
</footer>"""


def sticky_cta(label="Gratis offertes aanvragen"):
    return f'<div class="sticky-cta"><a class="btn btn-primary btn-block" href="/offerte-aanvragen/">{label}<span class="pijl" aria-hidden="true">→</span></a></div>'


def scripts():
    return ('<script src="/assets/js/config.js"></script><script src="/assets/js/toestemming.js" defer></script>'
            '<script src="/assets/js/app.js" defer></script>')


HONEYPOT = (
    '<div aria-hidden="true" style="position:absolute;left:-9999px;top:-9999px">'
    '<label>Website<input type="text" name="website" tabindex="-1" autocomplete="off"></label>'
    '</div>'
)


def page(title, description, canonical, body, jsonld=None, body_attrs="", noindex=False):
    # Honeypot in elk formulier: bots vullen dit veld, echte bezoekers zien het niet.
    body = body.replace(" novalidate>", " novalidate>" + HONEYPOT)
    body = __import__("stijl_v2").zachte_spaties(body)  # design v2: bedragen niet middenin afbreken
    return (
        head(title, description, canonical, jsonld, noindex=noindex)
        + f"<body{(' ' + body_attrs) if body_attrs else ''}>"
        + header() + body + footer() + sticky_cta() + scripts()
        + "</body></html>"
    )


# ---------------------------------------------------------------------------
# Kruimelpad
# ---------------------------------------------------------------------------

def title(base, brand=" | Topschilder", limit=60):
    """Houdt de <title> onder de 60 zichtbare tekens; laat de merknaam vallen als het niet past."""
    vis = len(base.replace("&amp;", "&").replace("&#39;", "'"))
    return base + brand if vis + len(brand) <= limit else base


def desc(*zinnen, limit=158):
    """Bouwt een meta description uit losse zinnen en laat achterste zinnen vallen
    zodra het geheel boven de limiet komt. Zo blijft elke description compleet."""
    zinnen = [z.strip() for z in zinnen if z and z.strip()]
    out = []
    for z in zinnen:
        kandidaat = " ".join(out + [z])
        if len(kandidaat) <= limit:
            out.append(z)
    return " ".join(out) if out else zinnen[0][:limit]


def crumbs(items):
    """items = [(label, url|None), ...] — laatste item is de huidige pagina."""
    parts = [f'<a href="{url}">{label}</a>' if url else label for label, url in items]
    html = '<div class="wrap crumbs">' + '<span>›</span>'.join(parts) + "</div>"
    ld = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": lbl,
             **({"item": SITE["url"] + url} if url else {})}
            for i, (lbl, url) in enumerate(items)
        ],
    }
    return html, ld


# ---------------------------------------------------------------------------
# Offerteformulier (multi-step)
# ---------------------------------------------------------------------------

def offerte_form(title="Ontvang gratis 3 offertes", sub="Gratis · vrijblijvend · maximaal 3 schilders"):
    dienstkeuze = "".join(
        f'<label><input type="radio" name="dienst" value="{d["naam"]}" data-required><span>{d["naam"]}</span></label>'
        for d in DIENSTEN
    )
    return f"""
<div class="formcard" id="offerte">
  <h2>{title}</h2>
  <p class="sub">{sub}</p>
  <div class="steps"><div class="on"></div><div></div><div></div><div></div></div>

  <form data-wizard data-table="leads" novalidate>

    <div class="step active" data-autoadvance="1">
      <div class="field">
        <label>Wat wil je laten doen?</label>
        <div class="choice">{dienstkeuze}</div>
      </div>
      <div class="err"></div>
      <div class="formnav"><button type="button" class="btn btn-primary" data-next>Volgende</button></div>
    </div>

    <div class="step">
      <div class="row2">
        <div class="field">
          <label for="f-postcode">Postcode</label>
          <input type="text" id="f-postcode" name="postcode" placeholder="3892 AA" required autocomplete="postal-code">
        </div>
        <div class="field">
          <label for="f-plaats">Plaats</label>
          <input type="text" id="f-plaats" name="plaats" placeholder="Zeewolde" required autocomplete="address-level2">
        </div>
      </div>
      <div class="field">
        <label>Om wat voor pand gaat het?</label>
        <div class="choice">
          <label><input type="radio" name="pandtype" value="Koopwoning" data-required><span>Koopwoning</span></label>
          <label><input type="radio" name="pandtype" value="Huurwoning" data-required><span>Huurwoning</span></label>
          <label><input type="radio" name="pandtype" value="Appartement / VvE" data-required><span>Appartement / VvE</span></label>
          <label><input type="radio" name="pandtype" value="Bedrijfspand" data-required><span>Bedrijfspand</span></label>
        </div>
      </div>
      <div class="err"></div>
      <div class="formnav">
        <button type="button" class="btn btn-ghost" data-prev>Terug</button>
        <button type="button" class="btn btn-primary" data-next>Volgende</button>
      </div>
    </div>

    <div class="step">
      <div class="field">
        <label>Hoe groot is de klus ongeveer?</label>
        <div class="choice">
          <label><input type="radio" name="omvang" value="Klein (1 ruimte / paar kozijnen)" data-required><span>Klein</span></label>
          <label><input type="radio" name="omvang" value="Gemiddeld (meerdere ruimtes / halve woning)" data-required><span>Gemiddeld</span></label>
          <label><input type="radio" name="omvang" value="Groot (hele woning)" data-required><span>Groot</span></label>
          <label><input type="radio" name="omvang" value="Weet ik niet, graag advies" data-required><span>Weet ik nog niet</span></label>
        </div>
      </div>
      <div class="field">
        <label>Wanneer wil je het laten uitvoeren?</label>
        <div class="choice">
          <label><input type="radio" name="planning" value="Zo snel mogelijk" data-required><span>Zo snel mogelijk</span></label>
          <label><input type="radio" name="planning" value="Binnen 1-3 maanden" data-required><span>Binnen 1–3 maanden</span></label>
          <label><input type="radio" name="planning" value="Over 3-6 maanden" data-required><span>Over 3–6 maanden</span></label>
          <label><input type="radio" name="planning" value="Nog aan het oriënteren" data-required><span>Ik oriënteer me</span></label>
        </div>
      </div>
      <div class="field">
        <label for="f-oms">Korte omschrijving <span class="hint">— optioneel, maar het levert je scherpere offertes op</span></label>
        <textarea id="f-oms" name="omschrijving" placeholder="Bijvoorbeeld: 8 kozijnen aan de voorzijde, laatste keer geschilderd in 2018, bij twee dorpels zit houtrot."></textarea>
      </div>
      <div class="err"></div>
      <div class="formnav">
        <button type="button" class="btn btn-ghost" data-prev>Terug</button>
        <button type="button" class="btn btn-primary" data-next>Volgende</button>
      </div>
    </div>

    <div class="step">
      <div class="field">
        <label for="f-naam">Naam</label>
        <input type="text" id="f-naam" name="naam" required autocomplete="name" placeholder="Voor- en achternaam">
      </div>
      <div class="row2">
        <div class="field">
          <label for="f-mail">E-mailadres</label>
          <input type="email" id="f-mail" name="email" required autocomplete="email" placeholder="naam@email.nl">
        </div>
        <div class="field">
          <label for="f-tel">Telefoonnummer</label>
          <input type="tel" id="f-tel" name="telefoon" required autocomplete="tel" placeholder="06 12345678">
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
    <p>We zoeken nu schilders in jouw regio die bij deze klus passen. Je krijgt meteen een bevestiging per mail. Daarna nemen de schilders zelf contact met je op. Houd ook je spambox even in de gaten.</p>
    <p><a class="btn btn-ghost" href="/prijzen/">Bekijk alvast wat schilderwerk kost</a></p>
  </div>
</div>"""


# ---------------------------------------------------------------------------
# Blokken
# ---------------------------------------------------------------------------

def hoe_werkt_het(plaats=None):
    waar = f" in {plaats}" if plaats else ""
    return f"""<section class="section soft">
<div class="wrap">
  <div class="center" style="max-width:640px;margin:0 auto 44px">
    <span class="badge">In 3 stappen</span>
    <h2>Zo {streep("werkt")} het</h2>
    <p class="lead">Eén aanvraag, meerdere prijzen. Je hoeft niet zelf bedrijf voor bedrijf af te bellen.</p>
  </div>
  <ol class="steps3">
    <li class="reveal">
      <span class="step-ic">{icon('form', 26)}</span>
      <h3>Vertel wat je nodig hebt</h3>
      <p>Vier korte vragen over de klus, het pand en de planning. Klaar in ongeveer een minuut.</p>
    </li>
    <li class="reveal reveal-d1">
      <span class="step-ic">{icon('match', 26)}</span>
      <h3>Wij zoeken de match</h3>
      <p>We koppelen je aanvraag aan maximaal drie schilders{waar} die dit type werk daadwerkelijk doen en op dit moment ruimte hebben.</p>
    </li>
    <li class="reveal reveal-d2">
      <span class="step-ic">{icon('check', 26)}</span>
      <h3>Vergelijk en kies zelf</h3>
      <p>Je ontvangt de offertes rechtstreeks van de schilders. Bevalt het niet? Dan zeg je gewoon nee — je zit nergens aan vast.</p>
    </li>
  </ol>
</div>
</section>"""


def waarom_blok():
    items = [
        ("shield", "Voorgeselecteerde bedrijven",
         "We bellen elke schilder voordat hij aanvragen krijgt en vragen om bewijs van KvK-inschrijving en aansprakelijkheidsverzekering. Bij herhaalde klachten stoppen we de samenwerking."),
        ("euro", "Prijsverschillen zijn groot",
         "De ene schilder rekent voor hetzelfde werk meer dan de andere, en uit één offerte zie je dat niet. Vergelijken is letterlijk het best betaalde uur van je klus."),
        ("clock", "Eén keer je verhaal doen",
         "Je vult één formulier in en krijgt direct een bevestiging per mail. Wij zoeken de schilders erbij; jij hoeft niet zelf rond te bellen."),
        ("users", "Maximaal 3 schilders",
         "Genoeg om echt te kunnen vergelijken, weinig genoeg om niet plat gebeld te worden. Je nummer gaat nooit naar meer partijen dan dat."),
    ]
    cards = "".join(
        f'<div class="card reveal reveal-d{n%4}"><div class="ic">{icon(i)}</div><h3>{t}</h3><p>{p}</p></div>'
        for n, (i, t, p) in enumerate(items)
    )
    return f"""<section class="section">
<div class="wrap">
  <div class="center" style="max-width:620px;margin:0 auto 40px">
    <span class="badge">Waarom wij</span>
    <h2>Waarom via {streep("Topschilder")}</h2>
    <p class="lead">Omdat één offerte je geen idee geeft of je een goede prijs betaalt.</p>
  </div>
  <div class="grid g4">{cards}</div>
  {feiten_blok([
      ("€0", "betaal je voor een aanvraag; de schilders betalen ons"),
      ("3", "schilders maximaal krijgen je aanvraag"),
      ("4", "korte vragen, en je aanvraag staat"),
      (str(len(PLAATSEN)), "plaatsen in ons werkgebied, van Urk tot Hilversum"),
  ])}
</div>
</section>"""


def dienst_cards(plaats_slug=None, plaats_naam=None, exclude=None):
    out = []
    for d in DIENSTEN:
        if exclude and d["slug"] == exclude:
            continue
        url = f"/schilder/{plaats_slug}/{d['slug']}/" if plaats_slug else f"/schilderwerk/{d['slug']}/"
        titel = f"{d.get('naam_lang', d['naam'])}{' in ' + plaats_naam if plaats_naam else ''}"
        chip = f'<span class="card-chip">{dienst_icoon(d["slug"], 27)}</span></figure>'
        beeld = (foto(FOTOS[d["slug"]]["hero"], "(max-width:600px) 92px, (max-width:900px) 45vw, 340px").replace("</figure>", chip)
                 if d["slug"] in FOTOS else illustratie(d["slug"]))
        out.append(
            f'<a class="card card-dienst reveal" href="{url}">'
            f'{beeld}'
            f"<h3>{titel}</h3><p>{d['kort']}</p>"
            f'<div class="price">Vanaf {eur(d["prijs_van"])} {d["prijs_eenheid"]}</div>'
            f'<p style="margin:10px 0 0"><span class="go">Bekijk &amp; vraag offertes aan →</span></p></a>'
        )
    return '<div class="grid g3">' + "".join(out) + "</div>"


def faq_blok(faqs, titel="Veelgestelde vragen"):
    items = "".join(
        f"<details><summary>{q}</summary><div class=\"a\"><p>{a}</p></div></details>"
        for q, a in faqs
    )
    html = f"""<section class="section">
<div class="wrap narrow">
  <h2>{titel}</h2>
  <div class="faq">{items}</div>
</div>
</section>"""
    ld = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ],
    }
    return html, ld


def cta_blok(titel="Klaar om te vergelijken?", tekst=None, knop="Gratis offertes aanvragen"):
    tekst = tekst or "Vul in een minuut het formulier in en ontvang vrijblijvend offertes van maximaal drie schilders uit jouw regio."
    return f"""<section class="section">
<div class="wrap">
  <div class="cta">
    <h2>{titel}</h2>
    <p>{tekst}</p>
    <a class="btn btn-primary btn-lg" href="/offerte-aanvragen/">{knop}</a>
  </div>
</div>
</section>"""


def calculator():
    """Prijsindicator. Rekent met dezelfde richtprijzen als de rest van de site."""
    OMVANG = {
        "binnenschilderwerk":   (10, 200, 45,  "m² muur/plafond",  "Een gemiddelde woonkamer is 45 tot 70 m² wand en plafond."),
        "buitenschilderwerk":   (2,  30,  10,  "kozijnen",         "Een tussenwoning heeft doorgaans 8 tot 14 kozijnen."),
        "houtrot-reparatie":    (1,  12,  3,   "reparatieplekken", "Tel de plekken waar het hout meegeeft als je erin prikt."),
        "spuitwerk":            (1,  20,  6,   "deuren",           "Een keuken telt vaak 10 tot 18 fronten."),
        "behangen":             (10, 120, 30,  "m² wand",          "Eén wand van 4 bij 2,6 meter is ruim 10 m²."),
        "zakelijk-schilderwerk":(4,  80,  16,  "uren",             "Voor grotere projecten werkt een schilder met een vaste aanneemsom."),
    }
    opties = ""
    for d in DIENSTEN:
        mn, mx, start, eenheid, uitleg = OMVANG[d["slug"]]
        opties += (f'<option value="{d["slug"]}" data-van="{d["prijs_van"]}" data-tot="{d["prijs_tot"]}" '
                   f'data-min="{mn}" data-max="{mx}" data-start="{start}" data-eenheid="{eenheid}" '
                   f'data-uitleg="{uitleg}">{d["naam"]}</option>')
    eerste = OMVANG[DIENSTEN[0]["slug"]]
    return f"""<div class="calc" data-calc>
  <h3>Wat kost mijn klus ongeveer?</h3>
  <div class="rij">
    <label for="calc-dienst">Klus</label>
    <select id="calc-dienst">{opties}</select>
  </div>
  <div class="rij">
    <label for="calc-omvang">Omvang</label>
    <input type="range" id="calc-omvang" min="{eerste[0]}" max="{eerste[1]}" value="{eerste[2]}" step="1">
    <span class="waarde" data-aantal></span>
  </div>
  <div class="calc-uit">
    <div class="bedrag" data-bedrag></div>
    <div class="sub" data-sub></div>
  </div>
  <p style="margin:18px 0 0;font-size:.88rem;color:var(--muted)">
    Indicatie inclusief materiaal en btw. De echte prijs hangt af van de staat
    van de ondergrond en de bereikbaarheid. <a href="/offerte-aanvragen/">Vraag gratis drie offertes aan</a>
    voor een prijs die op jouw situatie klopt, of <a data-cta href="/schilderwerk/binnenschilderwerk/">lees waar de prijs door bepaald wordt</a>.
  </p>
</div>"""


def prijstabel(diensten=None, plaats=None):
    """Zonder plaats: landelijke richtprijzen. Met plaats: gecorrigeerd voor de regio."""
    from data import lokale_prijs
    diensten = diensten or DIENSTEN
    rows = ""
    for d in diensten:
        van, tot = lokale_prijs(d, plaats) if plaats else (d["prijs_van"], d["prijs_tot"])
        url = f"/schilder/{plaats['slug']}/{d['slug']}/" if plaats else f"/schilderwerk/{d['slug']}/"
        rows += (f'<tr><td><a href="{url}">{d["naam"]}</a></td>'
                 f'<td class="num">{eur(van)} – {eur(tot)}</td>'
                 f'<td>{d["prijs_eenheid"]}</td></tr>')
    return f"""<div class="tablewrap">
<table>
<thead><tr><th>Type schilderwerk</th><th>Richtprijs</th><th>Eenheid</th></tr></thead>
<tbody>{rows}</tbody>
</table>
</div>
<p><small>Indicatieve prijzen inclusief materiaal en btw, tenzij er excl. btw staat. De werkelijke prijs hangt af van de staat van de ondergrond, bereikbaarheid en het seizoen. Vraag altijd meerdere offertes aan.</small></p>"""


# ---------------------------------------------------------------------------
# Werkgebiedkaart
# ---------------------------------------------------------------------------

def werkgebied_kaart():
    """Eigen SVG-kaart: elke plaats is een gewone link, dus zonder JavaScript werkt hij ook."""
    e = _html.escape
    links_van = {"naarden", "weesp", "bussum", "hilversum", "ermelo", "nijkerk", "amersfoort", "almere", "urk", "espel", "creil", "nagele"}
    boven = {"emmeloord"}
    provs = sorted({p["provincie"] for p in PLAATSEN})
    land = "".join(f'<path class="kl{" ka" if n in provs else ""}" d="{d}"/>' for n, d in PADEN.items())
    pts = ""
    for p in sorted(PLAATSEN, key=lambda x: x["prio"], reverse=True):
        x, y = PUNTEN[p["slug"]]
        lk = p["slug"] in links_van
        kant = "b" if p["slug"] == "kraggenburg" else "t" if p["slug"] in boven else ("l" if lk else "r")
        pts += (f'<a class="kp{" kg" if p["prio"] == 1 else ""}" href="/schilder/{p["slug"]}/" aria-label="Schilder {e(p["naam"])}, {e(p["provincie"])}" '
                f'data-naam="{e(p["naam"])}" data-prov="{e(p["provincie"])}" data-hook="{e(p["hook"])}" data-x="{x}" data-y="{y}" data-l="{kant}">'
                f'<circle class="kh" cx="{x}" cy="{y}" r="20"/><circle class="kd" cx="{x}" cy="{y}" r="9"/>'
                f'<text x="{x + (-16 if lk else 16)}" y="{y + 6}" text-anchor="{"middle" if kant in "tb" else "end" if lk else "start"}" font-size="24">{e(p["naam"])}</text></a>')
    knoppen = '<button type="button" class="chip-k" data-prov="" aria-pressed="true">Alle plaatsen</button>' + "".join(
        f'<button type="button" class="chip-k" data-prov="{e(n)}" aria-pressed="false">{e(n)}</button>' for n in provs)
    return f"""<div class="kaart" data-kaart data-b="{BREEDTE}" data-h="{HOOGTE}">
  <div class="kaart-knoppen" role="group" aria-label="Kaart inzoomen op provincie">{knoppen}</div>
  <div class="kaart-grid">
    <svg viewBox="0 0 {BREEDTE} {HOOGTE}" role="group" aria-label="Kaart met de {len(PLAATSEN)} plaatsen in ons werkgebied. Elke plaats is een link." preserveAspectRatio="xMidYMid slice">
      <rect class="kw" x="-500" y="-500" width="{BREEDTE + 1000}" height="{HOOGTE + 1000}"/>{land}{pts}
    </svg>
    <aside class="kaart-info" aria-live="polite">
      <p class="kaart-prov">Werkgebied</p>
      <h2 class="kaart-naam">Kies een plaats</h2>
      <p class="kaart-hook">Beweeg over de kaart of ga er met de Tab-toets doorheen. Klik op een plaats voor lokale richtprijzen en schilders in de buurt.</p>
      <a class="btn btn-primary kaart-link" href="/offerte-aanvragen/">Offertes aanvragen</a>
    </aside>
  </div>
  <p class="kaart-bron">Kaart: provinciegrenzen en woonplaatsen van <a href="https://www.pdok.nl/" rel="nofollow noopener">PDOK</a> (CBS en Kadaster), <a href="https://creativecommons.org/licenses/by/4.0/deed.nl" rel="nofollow noopener license">CC BY 4.0</a>, vereenvoudigd. Liever een lijst? Alle plaatsen staan hieronder.</p>
</div>"""


# ---------------------------------------------------------------------------
# Prijskaart en CTA halverwege (kosten-, plaats- en plaats-dienstpagina's)
# ---------------------------------------------------------------------------

def prijskaart(van, tot, eenheid, noot, beeld="", knop="Vergelijk offertes", extra=""):
    """Opvallende kaart met de richtprijs, optioneel met foto bovenaan."""
    return f"""<aside class="prijskaart" aria-label="Richtprijs">
  {beeld}
  <div class="prijskaart-in">
    <p class="prijskaart-kop">Richtprijs</p>
    <p class="prijskaart-bedrag">{eur(van)} <span>–</span> {eur(tot)}</p>
    <p class="prijskaart-eenheid">{eenheid}</p>
    <p class="prijskaart-noot">{noot}</p>
    <a class="btn btn-primary btn-block" href="/offerte-aanvragen/">{knop}</a>
    {extra}
  </div>
</aside>"""


def cta_midden(titel, tekst, knop="Gratis offertes aanvragen", href="/offerte-aanvragen/"):
    """Compacte oproep halverwege een lange pagina."""
    return f"""<div class="cta-midden reveal">
  <div class="cta-midden-tekst"><p class="cta-midden-titel">{titel}</p><p>{tekst}</p></div>
  <a class="btn btn-primary" href="{href}">{knop}</a>
</div>"""


# ===========================================================================
# Visuele bouwstenen (ronde 3) — herbruikbaar voor alle pagina's
# ===========================================================================
#
# Alles hieronder is pure HTML + CSS uit style.css (blok "Ronde 3" in assets.py),
# zonder extra bestanden of bibliotheken. Kort overzicht:
#
#   dienst_icoon(slug, size=28)      Eigen tweekleurig SVG-icoon per dienst.
#   streep(tekst)                    Penseelstreek onder een woord in een kop:
#                                    f"<h2>Zo {streep('werkt')} het</h2>"
#   feiten_blok(feiten, bron=None)   Rij met cijfers. ALLEEN controleerbare feiten
#                                    (eigen werkwijze, wetgeving, eigen richtprijzen).
#                                    feiten = [("9%", "btw op ...", "https://bron" of None), ...]
#   stappen_blok(stappen)            Genummerde tijdlijn, voor werkwijzen en gidsen.
#                                    stappen = [("Titel", "Uitleg"), ...]
#   foto_kader(f, sizes, bijschrift) Foto uit foto_data.py met bijschrift en
#                                    makersvermelding (licentie staat op /fotoverantwoording/).
#   prijs_balken(rijen, eenheid)     Visuele prijsvergelijking uit eigen richtprijzen.
#                                    rijen = [("Label", van, tot), ...]
#
# Scrollanimaties: zet class "reveal" (en eventueel "reveal-d1".."reveal-d3") op
# een element; zonder JS of met prefers-reduced-motion staat alles gewoon stil in beeld.

DIENST_ICONEN = {
    # Elk icoon: lijnen in currentColor, vlakken met class "ia" in de accentkleur.
    "binnenschilderwerk": '<rect class="ia" x="5" y="3" width="13" height="5.5" rx="1.6"/><rect x="5" y="3" width="13" height="5.5" rx="1.6"/><path d="M18 5.7h2.2v4.8H12v2.6"/><rect x="10" y="13.1" width="4" height="7.9" rx="1.3"/><path d="M7.5 8.5v2.2"/>',
    "buitenschilderwerk": '<path d="M3 11 12 3.5l9 7.5"/><path d="M5.2 9.6V21h13.6V9.6"/><rect class="ia" x="8" y="11.5" width="8" height="5.6" rx=".8"/><rect x="8" y="11.5" width="8" height="5.6" rx=".8"/><path d="M12 11.5v5.6M8 14.3h8"/>',
    "houtrot-reparatie": '<rect x="2.8" y="8.5" width="15.5" height="8.5" rx="1"/><path d="M5.5 11c2.5 0 3.2 2.6 6.2 2.6"/><path class="ia" d="M13 10.6c1.9-.9 3.9.2 3.9 2.1s-2 3.1-3.9 2.2c-1.4-.7-1.4-3.6 0-4.3z"/><path d="m16.5 4.2 4.3 4.3-1.9 1.9-4.3-4.3z"/><path d="m14.6 6.1-2 2"/>',
    "spuitwerk": '<rect class="ia" x="9" y="2.8" width="4.4" height="4.2" rx=".8"/><path d="M9 2.8h4.4V7"/><rect x="3.5" y="7" width="11" height="5" rx="1.6"/><path d="M14.5 8.6h3M8 12l-1.3 8.4h3.6l1-8.4"/><path d="M19.8 6.6h.01M21 9.5h.01M19.8 12.4h.01" stroke-width="2.6"/>',
    "behangen": '<rect class="ia" x="4.5" y="3" width="13" height="4.8" rx="2.4"/><rect x="4.5" y="3" width="13" height="4.8" rx="2.4"/><path d="M6.5 7.8V21h9V7.8"/><path d="m9 12 2-2 2 2-2 2zM9 17.5l2-2 2 2"/><path d="M20 9v12"/>',
    "zakelijk-schilderwerk": '<path d="M4 21V4.5h10V21"/><path d="M14 10h6v11"/><path d="M7 8h1M10.5 8h1M7 11.5h1M10.5 11.5h1M17 13.5h.5M17 17h.5"/><rect class="ia" x="7.3" y="15.2" width="3.6" height="5.8" rx=".6"/><path d="M2.5 21h19"/>',
}


def dienst_icoon(slug, size=28):
    """Tweekleurig dienst-icoon; valt terug op het gewone icoon uit ICONS."""
    p = DIENST_ICONEN.get(slug)
    if not p:
        d = next((x for x in DIENSTEN if x["slug"] == slug), None)
        return icon(d["icon"] if d else "check", size)
    return (f'<svg class="dicon" viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" '
            f'stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" '
            f'aria-hidden="true">{p}</svg>')


def streep(tekst):
    """Penseelstreek-accent onder een woord of korte zinsdeel in een kop."""
    return f'<span class="streep">{tekst}</span>'


def feiten_blok(feiten, bron=None, donker=False):
    """Cijferblok. Gebruik alleen feiten die je kunt onderbouwen; geef bij wetgeving een bronlink."""
    items = ""
    for n, f in enumerate(feiten):
        waarde, label = f[0], f[1]
        url = f[2] if len(f) > 2 else None
        lbl = f'{label} <a href="{url}" rel="noopener">bron</a>' if url else label
        items += (f'<div class="feit reveal reveal-d{n % 4}"><p class="feit-getal">{waarde}</p>'
                  f'<p class="feit-label">{lbl}</p></div>')
    noot = f'<p class="feiten-noot">{bron}</p>' if bron else ""
    return f'<div class="feiten{" feiten-donker" if donker else ""}">{items}</div>{noot}'


def stappen_blok(stappen, kop_tag="h3"):
    """Visuele tijdlijn met genummerde stappen."""
    li = "".join(
        f'<li class="reveal"><span class="stap-nr" aria-hidden="true">{i + 1}</span>'
        f'<div><{kop_tag}>{t}</{kop_tag}><p>{p}</p></div></li>'
        for i, (t, p) in enumerate(stappen))
    return f'<ol class="stappen">{li}</ol>'


def foto_kader(f, sizes, bijschrift=None):
    """Foto met bijschrift en makersvermelding; de volledige licentie staat op /fotoverantwoording/."""
    img = foto(f, sizes).replace('<figure class="foto">', '').replace("</figure>", "")
    tekst = bijschrift or f["alt"]
    maker = _html.escape(f.get("maker", ""))
    credit = (f' <span class="foto-credit">Foto: <a href="/fotoverantwoording/">{maker}</a>'
              f'{", " + f["licentie"] if f.get("licentie") else ""}</span>') if maker else ""
    return f'<figure class="foto foto-kader reveal">{img}<figcaption>{tekst}{credit}</figcaption></figure>'


def prijs_balken(rijen, eenheid="", noot=None):
    """Horizontale balken van/tot, geschaald op de hoogste prijs. Alleen eigen richtprijzen gebruiken."""
    hoogste = max(t for _, _, t in rijen) or 1
    out = ""
    for label, van, tot in rijen:
        l = round(van / hoogste * 100, 1)
        b = max(round((tot - van) / hoogste * 100, 1), 2)
        out += (f'<li><span class="pb-label">{label}</span>'
                f'<span class="pb-baan" aria-hidden="true"><span class="pb-balk" style="margin-left:{l}%;width:{b}%"></span></span>'
                f'<span class="pb-bedrag">{eur(van)} – {eur(tot)}</span></li>')
    kop = f'<p class="pb-eenheid">{eenheid}</p>' if eenheid else ""
    voet = f'<p class="pb-noot">{noot}</p>' if noot else ""
    return f'<div class="prijs-balken reveal">{kop}<ul>{out}</ul>{voet}</div>'
