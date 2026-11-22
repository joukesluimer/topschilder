# -*- coding: utf-8 -*-
"""
Schilderweer-check: "Kun je deze week buiten schilderen in [plaats]?"

Een losse pagina (/schilderweer/) en een compacte variant voor de plaatspagina's
over buitenschilderwerk (/schilder/{plaats}/buitenschilderwerk/).

De weersverwachting wordt in de browser opgehaald bij MET Norway (Meteorologisk
institutt, api.met.no, Locationforecast 2.0). Wij slaan niets op: er gaan alleen de
coördinaten van de gekozen plaats naar MET Norway (of, bij "mijn locatie", je locatie
afgerond op ongeveer een kilometer).

Voorwaarden MET Norway (nagelezen 22-11-2026, api.met.no/doc/TermsOfService,
/doc/License en /doc/FAQ):
- Gratis, ook commercieel ("including advertising revenue"), onder CC BY 4.0 en
  NLOD 2.0. Geen sleutel of account nodig.
- Naamsvermelding: "Data from MET Norway", met link naar de licentie, en vermelden
  dat we de data bewerken. Ons oordeel per dag is onze eigen berekening en niet de
  verantwoordelijkheid van MET Norway; dat staat op de pagina.
- Browsers mogen de API rechtstreeks aanroepen bij websites met weinig verkeer, als
  het een eenvoudige GET is zonder eigen headers. De browser stuurt dan zelf een
  Origin-header mee als identificatie. Daarom zetten we geen extra headers.
- Samen niet meer dan 20 aanvragen per seconde voor de hele site, coördinaten met
  hooguit 4 decimalen, en de Expires-header respecteren (de browsercache doet dat).
- Groeit het verkeer richting die grens, of wil MET Norway het anders: zet dan een
  kleine proxy met cache neer (zelfde antwoord, eigen User-Agent met contactadres,
  Expires/If-Modified-Since volgen) en vul die als API_URL hieronder in.

build.py roept alleen build_schilderweer(write, OUT) aan en gebruikt
schilderweer_blok(plaats) en schilderweer_gids() voor de links vanaf andere
pagina's. De home linkt via tools.py. CSS en JS staan in deze module en worden als
/assets/css/schilderweer.css en /assets/js/schilderweer.js weggeschreven.
"""

import os

from components import page, crumbs, offerte_form, faq_blok, title
from data import PLAATSEN

PAD = "/schilderweer/"

API_URL = "https://api.met.no/weatherapi/locationforecast/2.0/compact"
BRON = ('Weerdata: <a href="https://www.met.no/en" rel="nofollow noopener">MET Norway</a> '
        '(<a href="https://creativecommons.org/licenses/by/4.0/deed.nl" rel="nofollow noopener">CC BY 4.0</a>), '
        'door ons omgerekend naar een oordeel per dag. Dat oordeel is niet van MET Norway.')

# Midden van de kern, afgerond op twee decimalen (ongeveer een kilometer).
COORD = {
    "zeewolde": (52.33, 5.54), "almere": (52.37, 5.21), "lelystad": (52.52, 5.47),
    "dronten": (52.53, 5.72), "biddinghuizen": (52.45, 5.69), "swifterbant": (52.57, 5.64),
    "emmeloord": (52.71, 5.75), "urk": (52.66, 5.60), "marknesse": (52.71, 5.86),
    "nagele": (52.64, 5.72), "ens": (52.64, 5.83), "kraggenburg": (52.66, 5.90),
    "luttelgeest": (52.74, 5.84), "tollebeek": (52.69, 5.67), "bant": (52.77, 5.75),
    "creil": (52.76, 5.67), "rutten": (52.81, 5.73), "espel": (52.73, 5.62),
    "harderwijk": (52.34, 5.62), "ermelo": (52.30, 5.62), "putten": (52.26, 5.61),
    "nijkerk": (52.22, 5.49), "nunspeet": (52.38, 5.79), "elburg": (52.45, 5.84),
    "kampen": (52.56, 5.91), "zwolle": (52.51, 6.09), "genemuiden": (52.62, 6.04),
    "bunschoten-spakenburg": (52.25, 5.37), "amersfoort": (52.16, 5.39),
    "huizen": (52.30, 5.24), "blaricum": (52.27, 5.25), "naarden": (52.30, 5.16),
    "bussum": (52.27, 5.16), "hilversum": (52.22, 5.18), "weesp": (52.31, 5.04),
}

assert set(COORD) == {p["slug"] for p in PLAATSEN}, "Elke plaats in data.py heeft coördinaten nodig"

STANDAARD = "almere"

# De vuistregels. De JS gebruikt dezelfde grenzen (zie SW_JS); houd ze gelijk.
REGELS = [
    ("Temperatuur", "Overdag minimaal 10 °C",
     "Tussen 5 en 10 °C kan het met verf die daarvoor gemaakt is; dat staat op het blik. "
     "Onder 5 °C droogt en hecht verf slecht. Ook de nacht erna telt: bij nachtvorst kan de verse laag beschadigen."),
    ("Droog", "Geen regen tijdens het werk en de uren erna",
     "Verf moet een paar uur droog kunnen uitharden. En heeft het de nacht ervoor flink geregend, "
     "dan is het hout vaak nog nat. Dan wacht de schilder tot het hout droog is."),
    ("Luchtvochtigheid", "Liefst onder 80%",
     "Bij hoge luchtvochtigheid droogt verf langzaam en kan er condens op het hout komen. "
     "Daarom kijken we ook naar het dauwpunt: het hout moet minstens 3 graden warmer zijn dan het dauwpunt."),
    ("Wind", "Niet harder dan windkracht 4",
     "Bij harde wind droogt verf te snel, waait er stof en blad in en is werken op een ladder of steiger minder veilig."),
    ("Zon en hitte", "Niet boven 30 °C",
     "In de volle zon op een hete dag droogt verf te snel. Dan kan het nog wel, maar vroeg beginnen en met de zon mee werken."),
]

FAQ = [
    ("Bij welke temperatuur kun je buiten schilderen?",
     "De meeste buitenverf heeft minimaal 10 °C nodig, ook tijdens het drogen. Er is verf die al vanaf 5 °C gebruikt kan worden. Kijk altijd op het blik wat de fabrikant aangeeft."),
    ("Hoelang moet het droog blijven na het schilderen?",
     "Reken op een paar uur droog weer na het schilderen, zodat de verf kan uitharden. Hoelang precies verschilt per verf en per temperatuur. Dat staat op het blik."),
    ("Kun je schilderen na een regenbui?",
     "Pas als het hout weer droog is. Een schilder meet dat vaak met een vochtmeter. Na een natte nacht of ochtenddauw begint het werk daarom soms later op de dag."),
    ("Hoe betrouwbaar is de schilderweer-check?",
     "Het is een indicatie op basis van de weersverwachting. Voor de eerste paar dagen is die meestal goed, verder vooruit wordt hij onzekerder. De eerste twee à drie dagen rekenen we per uur, daarna in blokken van zes uur. De schilder en wat er op het verfblik staat zijn altijd leidend."),
    ("Waar komt de weersverwachting vandaan?",
     "Van MET Norway, het Noorse meteorologisch instituut. Dat deelt zijn verwachtingen voor heel Europa als open data. Wij rekenen die verwachting zelf om naar een oordeel per dag; dat oordeel is dus niet van MET Norway."),
    ("Wordt mijn locatie opgeslagen?",
     "Nee. Wij slaan niets op. Je browser vraagt de weersverwachting zelf op bij MET Norway, het Noorse meteorologisch instituut, met alleen de coördinaten van de plaats. Kies je voor mijn locatie, dan rondt je browser die eerst af op ongeveer een kilometer."),
]


# ---------------------------------------------------------------------------
# Teasers en blokken voor andere pagina's
# ---------------------------------------------------------------------------

ZON_IC = ('<svg viewBox="0 0 24 24" width="30" height="30" fill="none" stroke="currentColor" stroke-width="1.8" '
          'stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/>'
          '<path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>')


def schilderweer_gids():
    """Verwijzing in de gids 'wanneer kun je buiten schilderen'."""
    return (f'<div class="callout"><p><strong>Is het deze week schilderweer bij jou?</strong> '
            f'De <a href="{PAD}">schilderweer-check</a> laat per dag zien of het warm, droog en '
            f'windstil genoeg is om buiten te schilderen, voor elke plaats in ons werkgebied.</p></div>')


def schilderweer_blok(plaats=None):
    """Voor de buitenschilderwerkpagina's.

    Met een plaats: een compacte dagstrip die pas laadt als hij in beeld komt.
    Zonder plaats (algemene dienstpagina): alleen een verwijzing.
    """
    if not plaats:
        return (f'<div class="callout"><p><strong>Wanneer kan het bij jou?</strong> '
                f'Kijk in de <a href="{PAD}">schilderweer-check</a> of het de komende dagen '
                f'droog, warm en windstil genoeg is om buiten te schilderen.</p></div>')
    lat, lon = COORD[plaats["slug"]]
    return f"""<div class="sw-compact" data-sw="compact" data-plaats="{plaats['slug']}" data-naam="{plaats['naam']}" data-lat="{lat}" data-lon="{lon}"{_api_attr()} style="min-height:210px">
  <h3>Kun je deze week buiten schilderen in {plaats['naam']}?</h3>
  <div class="sw-doel"><p class="sw-laden">De weersverwachting wordt geladen…</p></div>
  <p class="sw-voet"><a href="{PAD}?plaats={plaats['slug']}">Bekijk alle dagen en de uitleg</a> · weerdata <a href="https://www.met.no/en" rel="nofollow noopener">MET Norway</a> (<a href="https://creativecommons.org/licenses/by/4.0/deed.nl" rel="nofollow noopener">CC BY 4.0</a>)</p>
</div>
<script>(function(){{var e=document.currentScript.previousElementSibling,d=0;function l(){{if(d)return;d=1;var c=document.createElement('link');c.rel='stylesheet';c.href='/assets/css/schilderweer.css';document.head.appendChild(c);var s=document.createElement('script');s.src='/assets/js/schilderweer.js';s.defer=true;document.body.appendChild(s)}}if('IntersectionObserver'in window){{var o=new IntersectionObserver(function(x){{if(x[0].isIntersecting){{o.disconnect();l()}}}},{{rootMargin:'300px'}});o.observe(e)}}else{{l()}}}})();</script>"""


def _api_attr():
    return f' data-api="{API_URL}"' if API_URL != "https://api.met.no/weatherapi/locationforecast/2.0/compact" else ""


# ---------------------------------------------------------------------------
# De pagina
# ---------------------------------------------------------------------------

def _opties():
    per_prov = {}
    for p in sorted(PLAATSEN, key=lambda x: x["naam"]):
        per_prov.setdefault(p["provincie"], []).append(p)
    html = ""
    for prov in sorted(per_prov):
        opts = "".join(
            f'<option value="{p["slug"]}" data-lat="{COORD[p["slug"]][0]}" data-lon="{COORD[p["slug"]][1]}"'
            f'{" selected" if p["slug"] == STANDAARD else ""}>{p["naam"]}</option>'
            for p in per_prov[prov])
        html += f'<optgroup label="{prov}">{opts}</optgroup>'
    return html


def build_schilderweer(write, out):
    for pad, inhoud in (("css/schilderweer.css", SW_CSS), ("js/schilderweer.js", SW_JS)):
        full = os.path.join(out, "assets", pad)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as f:
            f.write(inhoud)

    cr, cr_ld = crumbs([("Home", "/"), ("Schilderweer", None)])
    faq_html, faq_ld = faq_blok(FAQ, "Veelgestelde vragen over schilderweer")

    regels = "".join(
        f'<div class="sw-regel"><h3>{naam}</h3><p class="sw-regel-kort">{kort}</p><p>{uitleg}</p></div>'
        for naam, kort, uitleg in REGELS)

    body = f"""<link rel="stylesheet" href="/assets/css/schilderweer.css">
<link rel="preconnect" href="{'/'.join(API_URL.split('/')[:3])}" crossorigin>
{cr}
<section class="section-sm sw-kop">
<div class="wrap">
  <span class="badge">Gratis · ruim een week vooruit · niets opgeslagen</span>
  <h1>Kun je deze week buiten schilderen?</h1>
  <p class="lead">Kies je plaats en zie per dag of het schilderweer is: warm genoeg, droog en niet te veel wind. Groen is goed, oranje kan met beleid, rood is geen schilderweer.</p>

  <div class="sw-app" data-sw="vol"{_api_attr()} aria-live="polite">
    <div class="sw-kies">
      <label for="sw-plaats">Plaats</label>
      <select id="sw-plaats">{_opties()}</select>
      <button type="button" class="btn btn-ghost sw-locatie">Mijn locatie</button>
    </div>
    <div class="sw-doel"><p class="sw-laden">De weersverwachting wordt geladen…</p></div>
    <noscript><div class="callout"><p>Zet JavaScript aan om de schilderweer-check te gebruiken. De vuistregels staan hieronder, en meer lees je in de gids <a href="/gids/wanneer-buiten-schilderen/">wanneer kun je buiten schilderen</a>.</p></div></noscript>
    <p class="sw-voet">Een indicatie op basis van de weersverwachting. De schilder en wat er op het verfblik staat zijn altijd leidend. {BRON}</p>
  </div>
</div>
</section>

<section class="section soft" id="vuistregels"><div class="wrap">
  <div class="prose narrow" style="margin:0 auto 26px">
    <h2>Zo beoordelen we een dag</h2>
    <p>We kijken naar de uren waarop een schilder werkt, van 9 tot 17 uur, en naar de avond en nacht ervoor en erna. Een dag is groen als alles klopt. Is er één punt twijfelachtig, dan wordt hij oranje. Rood betekent: hier gaat het mis.</p>
  </div>
  <div class="sw-regels">{regels}</div>
  <div class="prose narrow" style="margin:26px auto 0">
    <p>Dit zijn gangbare vuistregels. Elke verf is anders: op het blik staat bij welke temperatuur en luchtvochtigheid hij gebruikt kan worden. Een goede schilder meet ook het vocht in het hout voordat hij begint. Meer over de seizoenen lees je in de gids <a href="/gids/wanneer-buiten-schilderen/">wanneer kun je buiten schilderen</a>.</p>
  </div>
</div></section>

<section class="section"><div class="wrap">
  <div class="grid g2" style="gap:48px;align-items:start">
    <div class="prose">
      <h2>Schilderweer op komst? Plan op tijd</h2>
      <p class="lead">Goede schilders hebben in het voorjaar en de zomer vaak weken vooruit een volle agenda. Wie nu offertes vraagt, staat op tijd in de planning.</p>
      <ul class="checklist">
        <li>Gratis offertes van maximaal drie schilders uit jouw regio</li>
        <li>De schilder plant het werk op de goede dagen</li>
        <li>Je vergelijkt en kiest zelf, of niet</li>
      </ul>
      <p>Is het nu geen buitenweer? Binnen schilderen kan het hele jaar. Lees ook <a href="/schilderwerk/buitenschilderwerk/">alles over buitenschilderwerk</a> of doe de <a href="/onderhoudscheck/">onderhoudscheck</a>.</p>
    </div>
    <div>{offerte_form("Offertes voor je buitenschilderwerk", "Vier korte vragen · gratis en vrijblijvend")}</div>
  </div>
</div></section>
{faq_html}"""

    app_ld = {
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": "Schilderweer-check",
        "url": "https://topschilder.nl" + PAD,
        "applicationCategory": "UtilitiesApplication",
        "operatingSystem": "Alle browsers",
        "inLanguage": "nl-NL",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"},
        "description": "Per dag voor ruim een week vooruit of het schilderweer is in jouw plaats: temperatuur, regen, luchtvochtigheid en wind.",
    }

    write(PAD, page(
        title("Schilderweer: kun je deze week buiten schilderen?"),
        "Kun je deze week buiten schilderen? Kies je plaats en zie per dag of het warm, droog en windstil genoeg is, voor ruim een week vooruit. Gratis.",
        PAD, body, [cr_ld, faq_ld, app_ld])
        .replace("</body>", '<script src="/assets/js/schilderweer.js" defer></script></body>'),
        prio=0.8, freq="daily")


# ---------------------------------------------------------------------------
# CSS (pagina en compacte variant)
# ---------------------------------------------------------------------------

SW_CSS = """/* Schilderweer-check */
.sw-app{background:#fff;border-radius:var(--radius-lg);box-shadow:var(--shadow-lg);padding:24px;margin-top:22px;min-width:0}
.sw-kies{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin-bottom:18px}
.sw-kies label{font-weight:700;color:var(--ink)}
@media(max-width:600px){.sw-kies{flex-wrap:nowrap}.sw-kies label{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)}.sw-kies select{flex:1 1 auto;max-width:none}.sw-kies .btn{white-space:nowrap;padding:10px 12px}}
.sw-kies select{font:inherit;font-size:1rem;padding:10px 12px;border:1.5px solid var(--line);border-radius:10px;background:#fff;color:var(--ink);min-width:0;flex:1 1 180px;max-width:300px}
.sw-kies .btn{padding:10px 16px}
.sw-laden{color:var(--muted);margin:0;padding:30px 0;text-align:center}
.sw-conclusie{display:flex;gap:14px;align-items:flex-start;border-radius:var(--radius);padding:16px 18px;margin-bottom:18px;background:var(--bg-soft);border-left:5px solid var(--line)}
.sw-conclusie.sw-g{background:#e9f6ef;border-left-color:#0f8a5f}
.sw-conclusie.sw-o{background:var(--accent-soft);border-left-color:var(--accent)}
.sw-conclusie.sw-r{background:#fbecea;border-left-color:#c0392b}
.sw-conclusie h2,.sw-conclusie h4{font-size:1.25rem;margin:0 0 4px;color:var(--ink);line-height:1.25}
.sw-conclusie p{margin:0;font-size:.97rem}
.sw-week{font-size:.82rem;font-weight:750;text-transform:uppercase;letter-spacing:.05em;color:var(--muted);margin:14px 0 8px;display:flex;justify-content:space-between;gap:8px;flex-wrap:wrap}
.sw-week span{font-weight:500;text-transform:none;letter-spacing:0}
.sw-strip{display:grid;grid-template-columns:repeat(7,minmax(0,1fr));gap:6px}
.sw-dag{position:relative;font:inherit;color:var(--ink);background:#fff;border:1.5px solid var(--line);border-radius:12px;padding:8px 2px 7px;text-align:center;cursor:pointer;min-width:0;display:flex;flex-direction:column;align-items:center;gap:2px;transition:transform .1s,box-shadow .15s}
.sw-dag:hover{box-shadow:var(--shadow)}
.sw-dag:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
.sw-dag .sw-dn{font-size:.78rem;font-weight:750;text-transform:uppercase;color:var(--muted)}
.sw-dag .sw-dd{font-size:.78rem;color:var(--muted)}
.sw-dag svg{width:26px;height:26px;margin:2px 0}
.sw-dag .sw-tmp{font-weight:750;font-size:.95rem}
.sw-dag .sw-bar{display:block;width:70%;height:6px;border-radius:99px;margin-top:3px;background:var(--line)}
.sw-dag.sw-g{background:#f0faf4;border-color:#9fd9bd}.sw-dag.sw-g .sw-bar{background:#0f8a5f}
.sw-dag.sw-o{background:#fff8ef;border-color:#f6c58d}.sw-dag.sw-o .sw-bar{background:#f4820b}
.sw-dag.sw-r{background:#fdf3f2;border-color:#ecb8b2}.sw-dag.sw-r .sw-bar{background:#c0392b}
.sw-dag.sw-best::before{content:"Beste";position:absolute;top:-9px;left:50%;transform:translateX(-50%);background:#0f8a5f;color:#fff;font-size:.62rem;font-weight:800;text-transform:uppercase;letter-spacing:.04em;padding:1px 6px;border-radius:99px}
.sw-dag.sw-actief{box-shadow:0 0 0 3px var(--ink)}
.sw-dag.sw-voorbij{opacity:.55}
.sw-strip.sw-onzeker .sw-dag{opacity:.82}
.sw-detail{margin-top:16px;border:1px solid var(--line);border-radius:var(--radius);padding:16px 18px;background:#fff}
.sw-detail h3{font-size:1.1rem;margin:0 0 4px}
.sw-detail .sw-oordeel{margin:0 0 12px;font-weight:600}
.sw-punten{list-style:none;padding:0;margin:0;display:grid;gap:8px}
.sw-punten li{display:grid;grid-template-columns:14px minmax(0,1fr);gap:10px;align-items:start;font-size:.95rem;line-height:1.4}
.sw-punten li::before{content:"";width:12px;height:12px;border-radius:50%;margin-top:4px;background:var(--line)}
.sw-punten li.sw-g::before{background:#0f8a5f}.sw-punten li.sw-o::before{background:#f4820b}.sw-punten li.sw-r::before{background:#c0392b}
.sw-punten b{color:var(--ink)}
.sw-legenda{display:flex;flex-wrap:wrap;gap:6px 16px;font-size:.85rem;color:var(--muted);margin:14px 0 0}
.sw-legenda i{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:6px;vertical-align:-1px}
.sw-acties{display:flex;flex-wrap:wrap;gap:10px;margin-top:16px}
.sw-voet{font-size:.84rem;color:var(--muted);margin:16px 0 0}
.sw-fout{border-radius:var(--radius);background:var(--bg-soft);border:1px solid var(--line);padding:16px 18px}
.sw-fout h3{font-size:1.1rem;margin:0 0 6px}
.sw-fout p{margin:0 0 8px;font-size:.95rem}
.sw-fout ul{margin:0 0 8px;padding-left:20px;font-size:.95rem}
.sw-regels{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,200px),1fr));gap:14px}
.sw-regel{background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:18px}
.sw-regel h3{font-size:1.05rem;margin:0 0 4px}
.sw-regel .sw-regel-kort{font-weight:700;color:var(--accent-dark);margin:0 0 6px}
.sw-regel p{font-size:.93rem;margin:0}
.sw-compact{background:var(--bg-soft);border:1px solid var(--line);border-radius:var(--radius-lg);padding:20px;margin:26px 0;min-width:0}
.sw-compact h3{margin:0 0 12px;font-size:1.15rem}
.sw-compact .sw-conclusie{background:#fff;margin-bottom:12px;padding:12px 14px}
.sw-compact .sw-conclusie h4{font-size:1.02rem}
.sw-compact .sw-conclusie p{font-size:.9rem}
.sw-compact .sw-voet{margin-top:12px}
@media(max-width:600px){
  .sw-app{padding:16px 12px;margin-left:-4px;margin-right:-4px}
  .sw-strip{gap:4px}
  .sw-dag{border-radius:9px;padding:7px 0 6px}
  .sw-dag .sw-dn,.sw-dag .sw-dd{font-size:.7rem}
  .sw-dag .sw-tmp{font-size:.82rem}
  .sw-dag svg{width:22px;height:22px}
  .sw-dag.sw-best::before{font-size:.55rem;padding:0 4px;top:-8px}
  .sw-compact{padding:16px 12px}
  .sw-conclusie{padding:12px 14px}
}
"""


# ---------------------------------------------------------------------------
# JS (pagina en compacte variant). Geen opslag, geen cookies.
# ---------------------------------------------------------------------------

SW_JS = r"""(function () {
  'use strict';
  var API = 'https://api.met.no/weatherapi/locationforecast/2.0/compact';
  var DAGEN = ['zo', 'ma', 'di', 'wo', 'do', 'vr', 'za'];
  var DAGEN_LANG = ['zondag', 'maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag'];
  var MAANDEN = ['januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli', 'augustus', 'september', 'oktober', 'november', 'december'];
  var NIVEAU = { g: 0, o: 1, r: 2 };
  var TEKST = { g: 'Schilderweer', o: 'Kan met beleid', r: 'Geen schilderweer' };

  // Vuistregels (gelijk houden met REGELS in schilderweer.py)
  var WERK_VAN = 9, WERK_TOT = 17;           // werkuren
  var T_GOED = 10, T_MIN = 5, T_HEET = 30;   // graden
  var RV_GOED = 80, RV_MAX = 90;             // procent luchtvochtigheid
  var DAUW_MARGE = 3;                        // graden boven het dauwpunt
  var WIND_OK = 28, WIND_MAX = 39, VLAAG_MAX = 60; // km/u (windkracht 4 / 6); MET geeft geen windstoten voor NL
  var REGEN = 0.2;                           // mm per uur telt als regen
  var REGEN_BLOK = 0.5;                      // mm in de werkuren telt als bui bij blokken van 6 uur

  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function r1(x) { return String(Math.round(x * 10) / 10).replace('.', ','); }

  var IC = {
    zon: '<circle cx="12" cy="12" r="4" fill="#f4b400" stroke="#e09a00"/><path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2M5.3 5.3l1.4 1.4M17.3 17.3l1.4 1.4M5.3 18.7l1.4-1.4M17.3 6.7l1.4-1.4" stroke="#e09a00"/>',
    halfzon: '<circle cx="9" cy="9" r="3.4" fill="#f4b400" stroke="#e09a00"/><path d="M9 2.5v1.5M2.5 9H4M4.4 4.4l1 1M13.6 4.4l-1 1" stroke="#e09a00"/><path d="M8 19h9a3.5 3.5 0 0 0 0-7 4.8 4.8 0 0 0-9.2 1.2A2.9 2.9 0 0 0 8 19z" fill="#fff" stroke="#8a7b63"/>',
    wolk: '<path d="M7 18h10a4 4 0 0 0 0-8 5.5 5.5 0 0 0-10.6 1.5A3.3 3.3 0 0 0 7 18z" fill="#eee9e0" stroke="#8a7b63"/>',
    mist: '<path d="M4 9h16M6 13h12M4 17h16" stroke="#8a7b63"/>',
    regen: '<path d="M7 14h10a4 4 0 0 0 0-8 5.5 5.5 0 0 0-10.6 1.5A3.3 3.3 0 0 0 7 14z" fill="#eee9e0" stroke="#8a7b63"/><path d="M8 17l-1 3M12 17l-1 3M16 17l-1 3" stroke="#2f7fc1"/>',
    sneeuw: '<path d="M7 14h10a4 4 0 0 0 0-8 5.5 5.5 0 0 0-10.6 1.5A3.3 3.3 0 0 0 7 14z" fill="#eee9e0" stroke="#8a7b63"/><path d="M8 18h.01M12 20h.01M16 18h.01" stroke="#2f7fc1" stroke-width="2.6"/>',
    onweer: '<path d="M7 14h10a4 4 0 0 0 0-8 5.5 5.5 0 0 0-10.6 1.5A3.3 3.3 0 0 0 7 14z" fill="#eee9e0" stroke="#8a7b63"/><path d="M12 14l-2 4h3l-2 4" stroke="#e09a00"/>'
  };
  function icoon(sym, droog) {
    // MET-symbolen zoals 'lightrainshowers_day'. Regent het alleen buiten de werkuren, dan een wolk.
    sym = String(sym || 'cloudy').replace(/_(day|night|polartwilight)$/, '');
    var n = /thunder/.test(sym) ? 'onweer' : /snow|sleet/.test(sym) ? 'sneeuw' : /rain/.test(sym) ? 'regen'
      : sym === 'fog' ? 'mist' : sym === 'clearsky' || sym === 'fair' ? 'zon' : sym === 'partlycloudy' ? 'halfzon' : 'wolk';
    if (droog && n === 'regen') n = 'wolk';
    return '<svg viewBox="0 0 24 24" fill="none" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + IC[n] + '</svg>';
  }

  // Coördinaten met hooguit 4 decimalen (eis van MET Norway). Geen eigen headers:
  // dan blijft het een eenvoudige aanvraag en stuurt de browser zelf zijn Origin mee.
  function url(el, lat, lon) {
    return (el.getAttribute('data-api') || API) + '?lat=' + (+lat).toFixed(4).replace(/\.?0+$/, '') + '&lon=' + (+lon).toFixed(4).replace(/\.?0+$/, '');
  }

  function haal(el, lat, lon) {
    var ctrl = window.AbortController ? new AbortController() : null;
    var t = ctrl ? setTimeout(function () { ctrl.abort(); }, 9000) : null;
    return fetch(url(el, lat, lon), ctrl ? { signal: ctrl.signal } : {})
      .then(function (r) { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); })
      .then(function (j) { if (t) clearTimeout(t); return naarUren(j); });
  }

  // ---- MET-antwoord omzetten naar uurwaarden in Nederlandse tijd -----------
  // De eerste dagen geeft MET per uur, daarna om de 6 uur. Die blokken vullen we aan
  // tot uren: temperatuur, vocht en wind lopen lineair door, de neerslag van het blok
  // verdelen we over de zes uur. Zulke uren krijgen 'grof' mee.
  var NL = window.Intl ? new Intl.DateTimeFormat('en-CA', { timeZone: 'Europe/Amsterdam', year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', hourCycle: 'h23' }) : null;
  function lokaal(ms) {
    if (!NL) { var x = new Date(ms); return x.getFullYear() + '-' + ('0' + (x.getMonth() + 1)).slice(-2) + '-' + ('0' + x.getDate()).slice(-2) + 'T' + ('0' + x.getHours()).slice(-2) + ':00'; }
    var o = {}; NL.formatToParts(new Date(ms)).forEach(function (p) { o[p.type] = p.value; });
    return o.year + '-' + o.month + '-' + o.day + 'T' + o.hour + ':00';
  }
  function naarUren(j) {
    var ts = j && j.properties && j.properties.timeseries;
    if (!ts || ts.length < 24) throw new Error('Onverwacht antwoord');
    var H = { time: [], temperature_2m: [], relative_humidity_2m: [], dew_point_2m: [], precipitation: [], wind_speed_10m: [], grof: [], sym: [], tmax6: [] };
    var gezien = {};
    function zet(ms, a, b, f, regen, grof, sym, tmax6) {
      var k = lokaal(ms); if (k in gezien) return; gezien[k] = 1;
      function m(v) { var x = a[v], y = b ? b[v] : x; return x === undefined ? null : y === undefined ? x : x + (y - x) * f; }
      H.time.push(k); H.temperature_2m.push(m('air_temperature')); H.relative_humidity_2m.push(m('relative_humidity'));
      var t = m('air_temperature'), rv = m('relative_humidity'), dp = m('dew_point_temperature');
      // Verder vooruit geeft MET geen dauwpunt; dan rekenen we het uit (formule van Magnus).
      if (dp === null && t !== null && rv > 0) { var g = Math.log(rv / 100) + 17.62 * t / (243.12 + t); dp = 243.12 * g / (17.62 - g); }
      H.dew_point_2m.push(dp); var w = m('wind_speed'); H.wind_speed_10m.push(w === null ? null : w * 3.6);
      H.precipitation.push(regen); H.grof.push(grof); H.sym.push(sym); H.tmax6.push(tmax6);
    }
    for (var i = 0; i < ts.length; i++) {
      var e = ts[i], d = e.data || {}, a = d.instant && d.instant.details || {}, ms = Date.parse(e.time);
      var n1 = d.next_1_hours, n6 = d.next_6_hours;
      var sym = (n6 && n6.summary && n6.summary.symbol_code) || (n1 && n1.summary && n1.summary.symbol_code) || null;
      var tmax6 = n6 && n6.details && n6.details.air_temperature_max;
      if (n1) { zet(ms, a, null, 0, n1.details ? n1.details.precipitation_amount || 0 : null, false, sym, tmax6); continue; }
      if (!n6) continue;
      var vlg = ts[i + 1], b = vlg && vlg.data && vlg.data.instant ? vlg.data.instant.details : null;
      var stap = vlg ? Math.round((Date.parse(vlg.time) - ms) / 3600000) : 6;
      var r6 = n6.details ? n6.details.precipitation_amount || 0 : 0;
      for (var h = 0; h < 6; h++) zet(ms + h * 3600000, a, b, b ? h / stap : 0, r6 / 6, true, sym, tmax6);
    }
    var daily = { time: [] };
    H.time.forEach(function (k) { var dag = k.slice(0, 10); if (daily.time.indexOf(dag) < 0) daily.time.push(dag); });
    return { hourly: H, daily: daily };
  }

  // ---- beoordeling -------------------------------------------------------
  function beoordeel(d) {
    var H = d.hourly, uur = {};
    for (var i = 0; i < H.time.length; i++) uur[H.time[i]] = i;
    var vandaag = lokaal(Date.now()).slice(0, 10);
    var nu = new Date(), nuUur = nu.getHours();
    function uren(dag, van, tot) { // [van, tot) op dag, tot mag > 24
      var out = [], base = new Date(dag + 'T00:00:00');
      for (var h = van; h < tot; h++) {
        var x = new Date(base.getTime() + h * 3600000);
        var k = x.getFullYear() + '-' + ('0' + (x.getMonth() + 1)).slice(-2) + '-' + ('0' + x.getDate()).slice(-2) + 'T' + ('0' + x.getHours()).slice(-2) + ':00';
        if (k in uur) out.push(uur[k]);
      }
      return out;
    }
    function waarden(idx, veld) { var a = H[veld] || []; return idx.map(function (j) { return a[j]; }).filter(function (v) { return v !== null && v !== undefined; }); }
    function max(a) { return a.length ? Math.max.apply(null, a) : null; }
    function min(a) { return a.length ? Math.min.apply(null, a) : null; }
    function som(a) { return a.reduce(function (s, v) { return s + v; }, 0); }
    function gem(a) { return a.length ? som(a) / a.length : null; }

    var res = [];
    for (var di = 0; di < d.daily.time.length; di++) {
      var dag = d.daily.time[di];
      var werk = uren(dag, WERK_VAN, WERK_TOT);
      var na = uren(dag, WERK_TOT, 23);           // tot 23 uur: de verf moet een paar uur drogen
      var nachtVoor = uren(dag, -6, WERK_VAN - 1); // 18 uur de avond ervoor tot 8 uur
      var nachtNa = uren(dag, 24, 31);            // nacht erna, 0 tot 7 uur
      var tw = waarden(werk, 'temperature_2m');
      if (tw.length < (dag === vandaag ? 1 : 6)) continue; // onvolledige dag aan het eind (of vandaag na het werk)
      var grof = werk.some(function (j) { return H.grof[j]; });
      var punten = [], score = 100;
      function punt(s, tekst) { punten.push({ s: s, t: tekst }); }

      // Temperatuur
      var tMin = min(tw), tMax = max(tw), tNacht = min(waarden(nachtNa, 'temperature_2m'));
      if (tMin >= T_GOED) punt('g', '<b>Temperatuur</b> overdag ' + Math.round(tMin) + ' tot ' + Math.round(tMax) + ' °C. Prima.');
      else if (tMax >= T_MIN && tMin >= T_MIN - 1) { punt('o', '<b>Temperatuur</b> overdag ' + Math.round(tMin) + ' tot ' + Math.round(tMax) + ' °C. Onder de 10 graden: alleen met verf die daarvoor geschikt is.'); score -= (T_GOED - tMin) * 4; }
      else { punt('r', '<b>Te koud</b>: overdag ' + Math.round(tMin) + ' tot ' + Math.round(tMax) + ' °C. Verf droogt en hecht dan slecht.'); score -= 60; }
      if (tNacht !== null && tNacht < 0) { punt('r', '<b>Nachtvorst</b> erna (' + r1(tNacht) + ' °C). Dat is slecht voor een verse verflaag.'); score -= 40; }
      else if (tNacht !== null && tNacht < T_MIN) { punt('o', '<b>Koude nacht</b> erna (' + Math.round(tNacht) + ' °C). De verf droogt langzaam door.'); score -= 8; }
      if (tMax > T_HEET) { punt('o', '<b>Heet</b> (' + Math.round(tMax) + ' °C). Niet in de volle zon schilderen; vroeg beginnen.'); score -= 10; }

      // Regen
      var rWerk = waarden(werk, 'precipitation'), rNa = waarden(na, 'precipitation'), rVoor = som(waarden(nachtVoor, 'precipitation'));
      var rWerkSom = som(rWerk);
      // Bij blokken van 6 uur is de neerslag uitgesmeerd: dan tellen we op de som.
      var natUren = grof ? (rWerkSom >= 2 ? 3 : rWerkSom >= REGEN_BLOK ? 1 : 0) : rWerk.filter(function (v) { return v >= REGEN; }).length;
      var kansWerk = max(waarden(werk, 'precipitation_probability'));
      var natNa = grof ? (som(rNa) >= REGEN_BLOK ? 1 : 0) : rNa.filter(function (v) { return v >= REGEN; }).length;
      if (natUren >= 3 || rWerkSom >= 2) { punt('r', '<b>Regen</b> tijdens de werkuren (' + r1(rWerkSom) + ' mm' + (grof ? ' verwacht' : '') + ').'); score -= 50; }
      else if (natUren > 0) { punt('o', '<b>' + (grof ? 'Kans op een bui' : 'Af en toe een bui') + '</b> tijdens de werkuren (' + r1(rWerkSom) + ' mm). Een droog dagdeel kiezen.'); score -= 20; }
      else if (kansWerk !== null && kansWerk >= 50) { punt('o', '<b>Kans op een bui</b> tijdens de werkuren (' + kansWerk + '%).'); score -= 15; }
      else punt('g', '<b>Droog</b> tijdens de werkuren' + (kansWerk >= 10 ? ' (kans op een bui hooguit ' + kansWerk + '%)' : '') + '.');
      if (natNa > 0) { punt('o', '<b>Regen in de avond</b> na het werk. De verf heeft een paar uur droog nodig.'); score -= 15; }
      if (rVoor >= 1) { punt('o', '<b>Natte nacht ervoor</b> (' + r1(rVoor) + ' mm). Het hout moet eerst opdrogen; misschien later beginnen.'); score -= 10; }

      // Luchtvochtigheid en dauwpunt
      var rv = gem(waarden(werk, 'relative_humidity_2m'));
      var dp = H.dew_point_2m || [], marge = min(werk.map(function (j) { return dp[j] === null || H.temperature_2m[j] === null ? NaN : H.temperature_2m[j] - dp[j]; }).filter(function (v) { return !isNaN(v); }));
      if (rv !== null) {
        if (rv > RV_MAX) { punt('r', '<b>Erg vochtig</b>: gemiddeld ' + Math.round(rv) + '% luchtvochtigheid. Verf droogt dan nauwelijks.'); score -= 35; }
        else if (rv > RV_GOED) { punt('o', '<b>Vochtig</b>: gemiddeld ' + Math.round(rv) + '% luchtvochtigheid. De verf droogt langzamer.'); score -= (rv - RV_GOED) * 2; }
        else punt('g', '<b>Luchtvochtigheid</b> gemiddeld ' + Math.round(rv) + '%. Goed.');
      }
      if (marge !== null && marge < DAUW_MARGE && !(rv > RV_MAX)) { punt('o', '<b>Kans op condens</b>: de temperatuur zit dicht bij het dauwpunt.'); score -= 10; }

      // Wind
      var wind = max(waarden(werk, 'wind_speed_10m')), vlaag = max(waarden(werk, 'wind_gusts_10m'));
      if (wind !== null) {
        if (wind >= WIND_MAX || (vlaag !== null && vlaag >= VLAAG_MAX)) { punt('r', '<b>Harde wind</b>: tot ' + Math.round(wind) + ' km/u' + (vlaag ? ', windstoten ' + Math.round(vlaag) + ' km/u' : '') + '.'); score -= 40; }
        else if (wind >= WIND_OK) { punt('o', '<b>Flinke wind</b>: tot ' + Math.round(wind) + ' km/u. Verf droogt sneller en er waait stof in.'); score -= 12; }
        else punt('g', '<b>Wind</b> tot ' + Math.round(wind) + ' km/u. Geen probleem.');
      }

      var status = 'g';
      punten.forEach(function (p) { if (NIVEAU[p.s] > NIVEAU[status]) status = p.s; });
      punten.sort(function (a, b) { return NIVEAU[b.s] - NIVEAU[a.s]; });
      var datum = new Date(dag + 'T12:00:00');
      var dagUren = uren(dag, 0, 24), tDag = max(waarden(dagUren, 'temperature_2m').concat(waarden(werk, 'tmax6')));
      // Symbool voor de dag: het blok dat het dichtst bij 10 uur begint (dekt de werkdag).
      var symIdx = werk.length ? werk[0] : dagUren[0], beste = 99;
      dagUren.forEach(function (j) { var hh = +H.time[j].slice(11, 13), a = Math.abs(hh - 10); if (H.sym[j] && a < beste) { beste = a; symIdx = j; } });
      if (grof) punt('g', '<b>Let op</b>: voor deze dag rekent de verwachting in blokken van zes uur. Dat is minder precies.');
      res.push({
        dag: dag, datum: datum, status: status, score: score, punten: punten,
        code: H.sym[symIdx], tMax: tDag, regen: som(waarden(dagUren, 'precipitation')),
        droog: natUren === 0, vandaag: dag === vandaag, voorbij: dag === vandaag && nuUur >= 15
      });
    }
    return res;
  }

  function datumTekst(x, kort) {
    return (x.vandaag ? 'vandaag' : DAGEN_LANG[x.datum.getDay()]) + ' ' + x.datum.getDate() + (kort ? '/' + (x.datum.getMonth() + 1) : ' ' + MAANDEN[x.datum.getMonth()]);
  }

  function besteDagen(dagen) {
    return dagen.filter(function (x) { return x.status === 'g' && !x.voorbij; })
      .sort(function (a, b) { return b.score - a.score; }).slice(0, 3)
      .map(function (x) { return x.dag; });
  }

  function conclusie(dagen, naam, kop) {
    var week = dagen.slice(0, 7).filter(function (x) { return !x.voorbij; });
    var groen = week.filter(function (x) { return x.status === 'g'; });
    var oranje = week.filter(function (x) { return x.status === 'o'; });
    var later = dagen.slice(7).filter(function (x) { return x.status === 'g'; });
    var maand = new Date().getMonth(), winter = maand >= 10 || maand <= 1;
    var s, h, p;
    if (groen.length) {
      var beste = groen.slice().sort(function (a, b) { return b.score - a.score; })[0];
      s = 'g';
      h = groen.length === 1 ? 'Deze week één goede schilderdag in ' + naam : 'Deze week ' + groen.length + ' goede schilderdagen in ' + naam;
      p = 'De beste dag lijkt ' + datumTekst(beste) + '.' + (oranje.length ? ' Daarnaast ' + oranje.length + (oranje.length === 1 ? ' dag die met beleid kan.' : ' dagen die met beleid kunnen.') : '');
    } else if (oranje.length) {
      var b2 = oranje.slice().sort(function (a, b) { return b.score - a.score; })[0];
      s = 'o';
      h = 'Deze week twijfelachtig schilderweer in ' + naam;
      p = 'Geen dag is helemaal goed. De beste kans lijkt ' + datumTekst(b2) + '. Bekijk per dag wat er speelt.';
    } else {
      s = 'r';
      h = 'Deze week geen schilderweer in ' + naam;
      p = winter ? 'Dat is normaal in deze tijd van het jaar. Binnen schilderen kan wel, en dit is een goed moment om je buitenwerk voor het voorjaar te plannen.'
        : 'Het is te nat, te koud of te winderig. Kijk of het daarna beter wordt.';
    }
    if (s !== 'g' && later.length) p += ' Daarna ' + (later.length === 1 ? 'ziet één dag' : 'zien ' + later.length + ' dagen') + ' er goed uit, maar zo ver vooruit is de verwachting nog onzeker.';
    return '<div class="sw-conclusie sw-' + s + '"><div><' + kop + '>' + esc(h) + '</' + kop + '><p>' + esc(p) + '</p></div></div>';
  }

  function dagKnop(x, best, i) {
    return '<button type="button" class="sw-dag sw-' + x.status + (best.indexOf(x.dag) > -1 ? ' sw-best' : '') + (x.voorbij ? ' sw-voorbij' : '') + '" data-i="' + i + '" ' +
      'aria-label="' + esc(datumTekst(x) + ': ' + TEKST[x.status]) + '">' +
      '<span class="sw-dn">' + (x.vandaag ? 'nu' : DAGEN[x.datum.getDay()]) + '</span>' +
      '<span class="sw-dd">' + x.datum.getDate() + '/' + (x.datum.getMonth() + 1) + '</span>' +
      icoon(x.code, x.droog) +
      '<span class="sw-tmp">' + Math.round(x.tMax) + '°</span>' +
      '<span class="sw-bar"></span></button>';
  }

  function detail(x) {
    return '<h3>' + esc(datumTekst(x).replace(/^./, function (c) { return c.toUpperCase(); })) + '</h3>' +
      '<p class="sw-oordeel">' + TEKST[x.status] + (x.voorbij ? ' (de werkdag is vandaag al grotendeels voorbij)' : '') + '</p>' +
      '<ul class="sw-punten">' + x.punten.map(function (p) { return '<li class="sw-' + p.s + '"><span>' + p.t + '</span></li>'; }).join('') + '</ul>';
  }

  var LEGENDA = '<p class="sw-legenda"><span><i style="background:#0f8a5f"></i>Schilderweer</span><span><i style="background:#f4820b"></i>Kan met beleid</span><span><i style="background:#c0392b"></i>Geen schilderweer</span></p>';

  function fout(doel) {
    doel.innerHTML = '<div class="sw-fout" role="status"><h3>De weersverwachting is nu niet op te halen</h3>' +
      '<p>Misschien is er even geen verbinding. Probeer het later nog eens. Tot die tijd gelden deze vuistregels:</p>' +
      '<ul><li>Buiten schilderen kan meestal van april tot en met oktober.</li><li>Overdag minimaal 10 °C, ook \'s nachts liefst niet onder de 5 °C.</li><li>Droog weer, ook de nacht ervoor en een paar uur erna.</li><li>Niet bij harde wind en niet in de volle zon op een hete dag.</li></ul>' +
      '<p>Lees meer in de gids <a href="/gids/wanneer-buiten-schilderen/">wanneer kun je buiten schilderen</a>.</p></div>';
  }

  // ---- volledige pagina --------------------------------------------------
  function vol(el) {
    var doel = el.querySelector('.sw-doel'), sel = el.querySelector('#sw-plaats'), knop = el.querySelector('.sw-locatie');
    var teller = 0, huidigeDagen = [];

    function kies(i) {
      doel.querySelectorAll('.sw-dag').forEach(function (b) { b.classList.toggle('sw-actief', +b.getAttribute('data-i') === i); });
      var det = doel.querySelector('.sw-detail');
      if (det && huidigeDagen[i]) det.innerHTML = detail(huidigeDagen[i]);
    }
    doel.addEventListener('click', function (e) {
      var b = e.target.closest('.sw-dag'); if (b) kies(+b.getAttribute('data-i'));
    });

    function toon(dagen, naam, slug) {
      var best = besteDagen(dagen.slice(0, 7));
      var w1 = dagen.slice(0, 7), w2 = dagen.slice(7, 14);
      var link = slug ? '<a class="btn btn-primary" href="/schilder/' + slug + '/buitenschilderwerk/">Schilders in ' + esc(naam) + '</a>' : '<a class="btn btn-primary" href="#offerte">Vraag offertes aan</a>';
      doel.innerHTML = conclusie(dagen, naam, 'h2') +
        '<p class="sw-week">De komende 7 dagen <span>Tik op een dag voor de details</span></p>' +
        '<div class="sw-strip">' + w1.map(function (x, i) { return dagKnop(x, best, i); }).join('') + '</div>' +
        (w2.length ? '<p class="sw-week">Daarna <span>Nog onzeker</span></p><div class="sw-strip sw-onzeker">' + w2.map(function (x, i) { return dagKnop(x, [], i + 7); }).join('') + '</div>' : '') +
        LEGENDA + '<div class="sw-detail"></div>' +
        '<div class="sw-acties">' + link + '<button type="button" class="btn btn-ghost sw-deel">Deel deze check</button></div>';
      huidigeDagen = dagen;
      // Begin bij de beste dag van deze week die nog niet voorbij is.
      var start = 0, top = -1e9;
      w1.forEach(function (x, i) { var s = x.score - NIVEAU[x.status] * 1000; if (!x.voorbij && s > top) { top = s; start = i; } });
      kies(start);
      var deel = doel.querySelector('.sw-deel');
      deel.addEventListener('click', function () {
        var u = location.origin + location.pathname + (slug ? '?plaats=' + slug : '');
        var groen = w1.filter(function (x) { return x.status === 'g' && !x.voorbij; }).length;
        var t = 'Schilderweer in ' + naam + ' deze week: ' + (groen ? groen + (groen === 1 ? ' goede dag' : ' goede dagen') : 'geen goede dagen') + '.';
        if (navigator.share) { navigator.share({ title: 'Schilderweer-check', text: t, url: u }).catch(function () {}); return; }
        if (navigator.clipboard) navigator.clipboard.writeText(t + ' ' + u).then(function () { deel.textContent = 'Link gekopieerd'; }, function () {});
      });
    }

    function laad(lat, lon, naam, slug) {
      var nr = ++teller;
      doel.innerHTML = '<p class="sw-laden">De weersverwachting voor ' + esc(naam) + ' wordt geladen…</p>';
      haal(el, lat, lon).then(function (d) {
        if (nr !== teller) return;
        var dagen = beoordeel(d);
        if (!dagen.length) throw new Error('Geen dagen');
        toon(dagen, naam, slug);
      }).catch(function () { if (nr === teller) fout(doel); });
    }

    function vanSelect() {
      var o = sel.options[sel.selectedIndex];
      laad(o.getAttribute('data-lat'), o.getAttribute('data-lon'), o.textContent, o.value);
      if (history.replaceState) history.replaceState(null, '', location.pathname + '?plaats=' + o.value);
    }

    var q = new URLSearchParams(location.search).get('plaats');
    if (q && sel.querySelector('option[value="' + q.replace(/[^a-z-]/g, '') + '"]')) sel.value = q;
    sel.addEventListener('change', vanSelect);

    if (!navigator.geolocation) knop.hidden = true;
    knop.addEventListener('click', function () {
      knop.disabled = true; knop.textContent = 'Locatie zoeken…';
      navigator.geolocation.getCurrentPosition(function (pos) {
        knop.disabled = false; knop.textContent = 'Mijn locatie';
        // Afronden op twee decimalen (ongeveer een kilometer) voordat iets de browser verlaat.
        var lat = Math.round(pos.coords.latitude * 100) / 100, lon = Math.round(pos.coords.longitude * 100) / 100;
        var dichtst = null, afst = 1e9;
        Array.prototype.forEach.call(sel.options, function (o) {
          var dy = (o.getAttribute('data-lat') - lat) * 111, dx = (o.getAttribute('data-lon') - lon) * 68;
          var a = Math.sqrt(dx * dx + dy * dy); if (a < afst) { afst = a; dichtst = o; }
        });
        if (dichtst && afst < 8) sel.value = dichtst.value;
        if (history.replaceState) history.replaceState(null, '', location.pathname);
        laad(lat, lon, dichtst && afst < 8 ? dichtst.textContent : 'jouw omgeving', dichtst && afst < 25 ? dichtst.value : null);
      }, function () {
        knop.disabled = false; knop.textContent = 'Mijn locatie';
        doel.insertAdjacentHTML('afterbegin', '<p class="sw-voet" role="status" style="margin:0 0 12px">Je locatie is niet gedeeld. Kies hierboven je plaats.</p>');
      }, { timeout: 10000, maximumAge: 600000 });
    });

    var o = sel.options[sel.selectedIndex];
    laad(o.getAttribute('data-lat'), o.getAttribute('data-lon'), o.textContent, o.value);
  }

  // ---- compacte variant (plaatspagina's) ---------------------------------
  function compact(el) {
    var doel = el.querySelector('.sw-doel'), naam = el.getAttribute('data-naam');
    haal(el, el.getAttribute('data-lat'), el.getAttribute('data-lon')).then(function (d) {
      var dagen = beoordeel(d).slice(0, 7);
      if (!dagen.length) throw new Error('Geen dagen');
      var best = besteDagen(dagen);
      doel.innerHTML = conclusie(dagen, naam, 'h4') + '<div class="sw-strip">' + dagen.map(function (x, i) { return dagKnop(x, best, i); }).join('') + '</div>';
      doel.addEventListener('click', function (e) {
        if (e.target.closest('.sw-dag')) location.href = '/schilderweer/?plaats=' + el.getAttribute('data-plaats');
      });
    }).catch(function () { fout(doel); });
  }

  document.querySelectorAll('[data-sw="vol"]').forEach(vol);
  document.querySelectorAll('[data-sw="compact"]').forEach(compact);
})();
"""
