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
}


def foto(f, sizes, boven_vouw=False):
    """Responsieve <img> voor een foto uit foto_data.py."""
    n = f["naam"]
    laden = 'loading="eager" fetchpriority="high"' if boven_vouw else 'loading="lazy"'
    alt = f["alt"].replace("&", "&amp;").replace('"', "&quot;")
    return (f'<figure class="foto"><img src="/assets/fotos/{n}-800.webp" '
            f'srcset="/assets/fotos/{n}-800.webp 800w, /assets/fotos/{n}-1600.webp 1600w" '
            f'sizes="{sizes}" width="{f["w"]}" height="{f["h"]}" alt="{alt}" {laden} decoding="async"></figure>')


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
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml"><meta property="og:image" content="https://topschilder.nl/assets/merk/logo.svg">
<link rel="stylesheet" href="/assets/css/style.css">
{ld}
</head>"""


def header():
    diensten_nav = ""
    return f"""<header class="header">
<div class="wrap header-in">
  <a class="logo" href="/" aria-label="Topschilder.nl, naar de homepage">
    <img src="/assets/merk/logo.svg" alt="Topschilder.nl — de schilder bij u in de buurt" width="843" height="367">
  </a>
  <button class="burger" aria-label="Menu" aria-expanded="false">☰</button>
  <nav class="nav">
    <a href="/schilderwerk/">Diensten</a>
    <a href="/werkgebied/">Werkgebied</a>
    <a href="/prijzen/">Wat kost het?</a>
    <a href="/offerte-vergelijken/">Offerte laten checken</a>
    <a href="/voor-schilders/">Voor schilders</a>
    <a class="btn btn-primary" href="/offerte-aanvragen/">Offertes aanvragen</a>
  </nav>
</div>
</header>{diensten_nav}"""


def footer():
    dl = "".join(f'<li><a href="/schilderwerk/{d["slug"]}/">{d["naam"]}</a></li>' for d in DIENSTEN)
    return f"""<footer class="footer">
<div class="wrap">
  <div class="footer-grid">
    <div>
      <a class="logo" href="/" aria-label="Topschilder.nl"><img src="/assets/merk/logo-wit.svg" alt="Topschilder.nl" width="843" height="367" loading="lazy"></a>
      <p style="margin-top:14px;max-width:34ch">Vergelijk vrijblijvend offertes van schilders bij jou in de buurt. Gratis, zonder verplichtingen en met maximaal drie bedrijven die contact opnemen.</p>
      <p><a href="/offerte-aanvragen/" style="color:#ffd9ab;font-weight:700">Offertes aanvragen →</a></p>
    </div>
    <div>
      <h4>Diensten</h4>
      <ul>{dl}</ul>
    </div>
    <div>
      <h4>Handig</h4>
      <ul>
        <li><a href="/prijzen/">Prijzen &amp; tarieven</a></li>
        <li><a href="/offerte-vergelijken/">Offerte laten checken</a></li>
        <li><a href="/werkgebied/">Alle plaatsen</a></li>
        <li><a href="/over-ons/">Over Topschilder</a></li>
        <li><a href="/contact/">Contact</a></li>
      </ul>
    </div>
    <div>
      <h4>Schilders</h4>
      <ul>
        <li><a href="/voor-schilders/">Aanmelden als schilder</a></li>
        <li><a href="/voor-schilders/#tarieven">Wat kost een lead?</a></li>
        <li><a href="/voor-schilders/#exclusief">Exclusieve leads</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bot">
    <div>© {SITE['oprichting']}–2026 {SITE['naam']} · KvK {SITE['kvk']}</div>
    <div><a href="/privacy/">Privacy</a> · <a href="/voorwaarden/">Algemene voorwaarden</a> · <a href="/cookies/">Cookies</a> · <a href="/fotoverantwoording/">Fotoverantwoording</a></div>
  </div>
</div>
</footer>"""


def sticky_cta(label="Gratis offertes aanvragen"):
    return f'<div class="sticky-cta"><a class="btn btn-primary btn-block" href="/offerte-aanvragen/">{label}</a></div>'


def scripts():
    return '<script src="/assets/js/config.js"></script><script src="/assets/js/app.js" defer></script>'


HONEYPOT = (
    '<div aria-hidden="true" style="position:absolute;left:-9999px;top:-9999px">'
    '<label>Website<input type="text" name="website" tabindex="-1" autocomplete="off"></label>'
    '</div>'
)


def page(title, description, canonical, body, jsonld=None, body_attrs="", noindex=False):
    # Honeypot in elk formulier: bots vullen dit veld, echte bezoekers zien het niet.
    body = body.replace(" novalidate>", " novalidate>" + HONEYPOT)
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

def offerte_form(title="Ontvang gratis 3 offertes", sub="Gemiddeld binnen 24 uur reactie · Volledig vrijblijvend"):
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
    <p>We zoeken nu schilders in jouw regio die bij deze klus passen. Je hoort doorgaans binnen één werkdag iets — houd ook je spambox even in de gaten.</p>
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
    <h2>Zo werkt het</h2>
    <p class="lead">Eén aanvraag, meerdere prijzen. Je hoeft niet zelf bedrijf voor bedrijf af te bellen.</p>
  </div>
  <ol class="steps3">
    <li>
      <h3>Vertel wat je nodig hebt</h3>
      <p>Vier korte vragen over de klus, het pand en de planning. Klaar in ongeveer een minuut.</p>
    </li>
    <li>
      <h3>Wij zoeken de match</h3>
      <p>We koppelen je aanvraag aan maximaal drie schilders{waar} die dit type werk daadwerkelijk doen en op dit moment ruimte hebben.</p>
    </li>
    <li>
      <h3>Vergelijk en kies zelf</h3>
      <p>Je ontvangt de offertes rechtstreeks van de schilders. Bevalt het niet? Dan zeg je gewoon nee — je zit nergens aan vast.</p>
    </li>
  </ol>
</div>
</section>"""


def waarom_blok():
    items = [
        ("shield", "Voorgeselecteerde bedrijven",
         "We werken alleen met schildersbedrijven met een geldige KvK-inschrijving en aansprakelijkheidsverzekering. Klachten betekenen dat we de samenwerking stopzetten."),
        ("euro", "Prijsverschillen zijn groot",
         "De ene schilder rekent voor hetzelfde werk meer dan de andere, en uit één offerte zie je dat niet. Vergelijken is letterlijk het best betaalde uur van je klus."),
        ("clock", "Snel duidelijkheid",
         "Je aanvraag gaat dezelfde dag door naar schilders in jouw regio. Meestal heb je binnen één werkdag de eerste reactie."),
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
    <h2>Waarom via Topschilder</h2>
    <p class="lead">Omdat één offerte je geen idee geeft of je een goede prijs betaalt.</p>
  </div>
  <div class="grid g4">{cards}</div>
</div>
</section>"""


def dienst_cards(plaats_slug=None, plaats_naam=None, exclude=None):
    out = []
    for d in DIENSTEN:
        if exclude and d["slug"] == exclude:
            continue
        url = f"/schilder/{plaats_slug}/{d['slug']}/" if plaats_slug else f"/schilderwerk/{d['slug']}/"
        titel = f"{d['naam']}{' in ' + plaats_naam if plaats_naam else ''}"
        out.append(
            f'<a class="card reveal" href="{url}">'
            f'{foto(FOTOS[d["slug"]]["hero"], "(max-width:600px) calc(100vw - 40px), (max-width:900px) 45vw, 340px") if d["slug"] in FOTOS else illustratie(d["slug"])}'
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
