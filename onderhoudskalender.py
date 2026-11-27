# -*- coding: utf-8 -*-
"""
Onderhoudskalender (/onderhoudskalender/): "Wanneer moet je huis weer geschilderd worden?"

Vul je woning, bouwjaar, laatste buitenbeurt, kleur en ligging in. Je krijgt een tijdlijn
van 15 jaar met bijwerken, nieuwe lagen en jaarlijkse controles, met richtprijzen.
Exporteren kan naar je agenda (.ics) en als afbeelding (canvas). Alles gebeurt in de
browser; er wordt niets opgeslagen of verstuurd.

Verschil met /onderhoudscheck/: de check kijkt naar de staat van je verf nu; de kalender
plant vooruit vanaf je laatste schilderbeurt.

Termijnen: dezelfde onderhoudsschema's als de onderhoudscheck (NBvT/SGT, Sikkens- en
Sigma-schema's). Prijzen: kosten_data.py via onderhoudscheck.prijzen().
"""

import json
import os

from components import page, crumbs, offerte_form, faq_blok, title, eur
from kosten_data import PRIJSBANDEN
from onderhoudscheck import prijzen, BRONNEN_TERMIJN

PAD = "/onderhoudskalender/"
JAREN = 15

# [bijwerken na, nieuwe laag na] in jaren (NBvT/SGT-schema, zie onderhoudscheck)
TERMIJN = {"licht": [3, 6], "donker": [2, 4], "transparant": [1, 2]}


def _bl(k, kort):
    return f'<a href="{BRONNEN_TERMIJN[k][1]}" rel="nofollow noopener" target="_blank">{kort}</a>'


def teaser_kort():
    """Korte verwijzing voor andere pagina's (onderhoudscheck, gidsen)."""
    return ('<p class="okal-teaser"><strong>Vooruit plannen?</strong> Zet je schilderbeurten voor de komende '
            f'15 jaar op een rij met de <a href="{PAD}">onderhoudskalender</a>, inclusief richtprijzen en '
            'een herinnering in je agenda.</p>')


def _keuze(naam, opties, gekozen):
    return "".join(
        f'<label><input type="radio" name="{naam}" value="{w}"{" checked" if w == gekozen else ""}><span>{lbl}</span></label>'
        for w, lbl in opties)


def build_onderhoudskalender(write, out):
    p = prijzen()
    nu = __import__("datetime").date.today().year
    data = {
        "jaren": JAREN,
        "termijn": TERMIJN,
        "woning": p["woning"],
        "uur": [PRIJSBANDEN["uurloon"]["van"], PRIJSBANDEN["uurloon"]["tot"]],
        "woningNaam": {"tussen": "tussenwoning", "hoek": "hoekwoning of 2-onder-1-kap", "vrijstaand": "vrijstaande woning"},
        "kleurNaam": {"licht": "dekkend, lichte kleur", "donker": "dekkend, donkere kleur", "transparant": "transparant (beits of blanke lak)"},
    }

    cr, cr_ld = crumbs([("Home", "/"), ("Tools", "/tools/"), ("Onderhoudskalender", None)])

    tool = f"""{cr}
<section class="section-sm tool-hero okal-hero">
<div class="wrap">
  <div class="okal-kop">
    <span class="badge">Gratis tool · 1 minuut · niets opgeslagen</span>
    <h1>Onderhoudskalender voor je schilderwerk</h1>
    <p class="lead">Wanneer moet je huis weer geschilderd worden, en wat kost dat? Vul vijf dingen in en je ziet je schilderbeurten voor de komende {JAREN} jaar op een tijdlijn. Zet ze daarna in je agenda of bewaar ze als plaatje.</p>
  </div>
  <div class="okal-grid">
    <form class="formcard okal-form" id="okal-form" novalidate>
      <h2>Over je huis</h2>
      <p class="sub">Weet je iets niet zeker? Kies wat het meest in de buurt komt.</p>
      <div class="field"><label id="okal-l-woning">Wat voor woning heb je?</label>
        <div class="choice" role="radiogroup" aria-labelledby="okal-l-woning">{_keuze("woning", [("tussen", "Tussenwoning"), ("hoek", "Hoekwoning / 2-onder-1-kap"), ("vrijstaand", "Vrijstaand")], "tussen")}</div></div>
      <div class="row2">
        <div class="field"><label for="okal-bouwjaar">Bouwjaar</label>
          <input type="number" id="okal-bouwjaar" name="bouwjaar" inputmode="numeric" min="1600" max="{nu}" value="1985"></div>
        <div class="field"><label for="okal-laatst">Laatste buitenbeurt</label>
          <select id="okal-laatst" name="laatst">
            <option value="">Weet ik niet</option>
            {"".join(f'<option value="{j}"{" selected" if j == nu - 4 else ""}>{j}</option>' for j in range(nu, nu - 21, -1))}
            <option value="oud">Langer dan 20 jaar geleden</option>
          </select></div>
      </div>
      <div class="field"><label id="okal-l-kleur">Kleur van kozijnen en boeidelen</label>
        <div class="choice okal-choice3" role="radiogroup" aria-labelledby="okal-l-kleur">{_keuze("kleur", [("licht", "Licht (wit, crème)"), ("donker", "Donker (antraciet, groen)"), ("transparant", "Transparant (beits)")], "licht")}</div></div>
      <div class="field"><label id="okal-l-ligging">Ligging van de gevel</label>
        <div class="choice" role="radiogroup" aria-labelledby="okal-l-ligging">{_keuze("ligging", [("normaal", "Gewoon, wat beschut"), ("zwaar", "Veel zon, wind of open ligging")], "normaal")}</div></div>
      <p class="okal-fout" role="alert" hidden></p>
      <button type="submit" class="btn btn-primary btn-block">Maak mijn kalender</button>
    </form>

    <div class="okal-uit" id="okal-uit" aria-live="polite">
      <div class="okal-leeg">
        <svg viewBox="0 0 120 90" width="120" height="90" aria-hidden="true"><rect x="10" y="14" width="100" height="68" rx="8" fill="#fff" stroke="#6b5024" stroke-width="3"/><path d="M10 32h100" stroke="#6b5024" stroke-width="3"/><path d="M34 6v16M86 6v16" stroke="#6b5024" stroke-width="4" stroke-linecap="round"/><circle cx="36" cy="50" r="6" fill="#0f8a5f"/><circle cx="60" cy="50" r="6" fill="#d9c7a8"/><circle cx="84" cy="50" r="8" fill="#f4820b" stroke="#a35200" stroke-width="2"/><circle cx="36" cy="68" r="6" fill="#d9c7a8"/><circle cx="60" cy="68" r="6" fill="#0f8a5f"/></svg>
        <p>Vul links je gegevens in. Je kalender verschijnt hier.</p>
      </div>
    </div>
  </div>
</div>
</section>"""

    uitleg = f"""<section class="section soft" id="zo-werkt-het"><div class="wrap narrow prose">
  <h2>Zo rekent de kalender</h2>
  <p>De kalender gaat uit van de onderhoudsschema's die de timmerindustrie en de verffabrikanten gebruiken. Die gaan uit van goed aangebracht schilderwerk. Vanaf je laatste schilderbeurt telt hij door: eerst een keer <strong>bijwerken</strong> (kleine plekken, kit en de onderdorpels), daarna een <strong>nieuwe laag</strong> over alles. Daartussen loop je elk voorjaar zelf het houtwerk na.</p>
  <div class="tablewrap"><table>
    <thead><tr><th>Afwerking</th><th>Bijwerken</th><th>Nieuwe laag</th></tr></thead>
    <tbody>
      <tr><td>Dekkend, lichte kleur</td><td>na ± 3 jaar</td><td>na ± 6 jaar</td></tr>
      <tr><td>Dekkend, donkere kleur</td><td>na ± 2 jaar</td><td>na ± 4 jaar</td></tr>
      <tr><td>Transparant (beits, blanke lak)</td><td>elk jaar</td><td>om de 2 jaar</td></tr>
    </tbody>
  </table></div>
  <p><small>Bron: onderhoudsschema van de {_bl("nbvt", "NBvT en Stichting Garantiefonds Timmerwerk")}; de schema's voor {_bl("sikkens", "Sikkens")} en {_bl("sigma", "Sigma")} liggen in dezelfde orde. Meer uitleg en alle bronnen staan bij de <a href="/onderhoudscheck/#termijnen">onderhoudscheck</a>.</small></p>
  <h3>Wat we aanpassen</h3>
  <ul>
    <li><strong>Veel zon, wind of een open ligging:</strong> bij dekkende verf rekenen we een jaar korter. De schema's noemen daar geen apart getal; wij houden de korte kant aan.</li>
    <li><strong>Laatste beurt niet bekend:</strong> is je huis jonger dan vijf jaar, dan tellen we vanaf het bouwjaar. Anders zetten we dit jaar een opname door een schilder in de kalender.</li>
    <li><strong>Achterstallig:</strong> had er al een beurt moeten zijn, dan zetten we die in dit jaar.</li>
  </ul>
  <h3>Waar komen de prijzen vandaan?</h3>
  <p>Een nieuwe laag kost voor een tussenwoning {eur(p['woning']['tussen'][0])} tot {eur(p['woning']['tussen'][1])}, voor een hoekwoning {eur(p['woning']['hoek'][0])} tot {eur(p['woning']['hoek'][1])} en voor een vrijstaande woning {eur(p['woning']['vrijstaand'][0])} tot {eur(p['woning']['vrijstaand'][1])}. Dat zijn de richtprijzen van onze pagina <a href="/kosten/huis-schilderen/">wat kost het om je huis te laten schilderen</a>, inclusief 9% btw en materiaal, prijspeil 2026. Bijwerken is kleiner werk; dat rekent een schilder vaak per uur ({eur(PRIJSBANDEN['uurloon']['van'])} tot {eur(PRIJSBANDEN['uurloon']['tot'])} excl. btw). Prijzen stijgen meestal elk jaar een beetje; de kalender rekent met de prijzen van nu.</p>
  <p>Wil je weten hoe je schilderwerk er nu voor staat? Doe de <a href="/onderhoudscheck/">onderhoudscheck</a>. Wil je de hele klus uitrekenen? Gebruik de <a href="/kosten/calculator/">huiscalculator</a>. En voor het beste moment in het jaar kijk je bij het <a href="/schilderweer/">schilderweer</a>.</p>
</div></section>"""

    offerte = f"""<section class="section"><div class="wrap">
  <div class="grid g2" style="gap:48px;align-items:start">
    <div class="prose">
      <h2>Staat er dit jaar of volgend jaar een beurt gepland?</h2>
      <p class="lead">Goede schilders zitten in het voorjaar snel vol. Vraag op tijd gratis offertes aan bij maximaal drie schilders uit jouw regio. Na je kalender vullen we je planning alvast voor je in.</p>
      <ul class="checklist">
        <li>Gratis en vrijblijvend</li>
        <li>Maximaal drie schilders nemen contact op</li>
        <li>Je kiest zelf of je verder gaat</li>
      </ul>
    </div>
    <div>{offerte_form("Offertes voor je buitenschilderwerk", "Vier korte vragen · gratis en vrijblijvend")}</div>
  </div>
</div></section>"""

    faqs = [
        ("Hoe vaak moet je je huis buiten laten schilderen?",
         "Bij dekkende verf in een lichte kleur is het advies: na ongeveer 3 jaar bijwerken en na ongeveer 6 jaar een nieuwe laag. Bij een donkere kleur is dat 2 en 4 jaar, bij transparante beits elk jaar bijwerken en om de 2 jaar een nieuwe laag. Dat zijn de schema's van de timmerindustrie."),
        ("Wat is het verschil tussen bijwerken en een nieuwe laag?",
         "Bij bijwerken herstelt de schilder alleen de plekken die slijten: onderdorpels, hoeken, kit en kale randen. Bij een nieuwe laag wordt al het houtwerk geschuurd en opnieuw geschilderd. Op tijd bijwerken zorgt dat de nieuwe laag later minder werk is."),
        ("Hoe zet ik de kalender in mijn agenda?",
         "Klik na het maken van je kalender op 'Zet in je agenda'. Je downloadt dan een .ics-bestand. Open dat bestand en je agenda (Google, Outlook of Apple) zet de afspraken erin. Er gaat niets naar ons toe."),
        ("Waarom staat er een opname in mijn kalender?",
         "Als je niet weet wanneer je huis voor het laatst geschilderd is, of als dat lang geleden is, kunnen we niet goed doortellen. Dan is het slim dat een schilder eerst komt kijken. Daarna weet je wat er nodig is."),
        ("Kloppen de prijzen voor mijn huis?",
         "Het zijn richtprijzen voor een gemiddelde woning, inclusief btw en materiaal. De echte prijs hangt af van het aantal kozijnen, de staat van het hout, de bereikbaarheid en je regio. Een offerte van een schilder die je huis gezien heeft, is altijd preciezer."),
    ]
    faq_html, faq_ld = faq_blok(faqs)

    app_ld = {
        "@context": "https://schema.org", "@type": "WebApplication",
        "name": "Onderhoudskalender schilderwerk", "url": "https://topschilder.nl" + PAD,
        "applicationCategory": "UtilitiesApplication", "operatingSystem": "Alle browsers",
        "inLanguage": "nl-NL", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"},
        "description": "Planning van je buitenschilderwerk voor 15 jaar, op basis van bouwjaar, laatste schilderbeurt, kleur en ligging, met richtprijzen en export naar je agenda.",
    }
    howto_ld = {
        "@context": "https://schema.org", "@type": "HowTo",
        "name": "Zo plan je het onderhoud van je buitenschilderwerk",
        "totalTime": "PT2M",
        "step": [
            {"@type": "HowToStep", "position": 1, "name": "Zoek je laatste schilderbeurt op",
             "text": "Kijk in je administratie of vraag het de vorige eigenaar. Weet je het niet, dan begint de kalender met een opname door een schilder."},
            {"@type": "HowToStep", "position": 2, "name": "Kies je afwerking en ligging",
             "text": "Lichte dekkende verf gaat het langst mee, donkere verf en transparante beits korter. Veel zon of wind maakt de termijn korter."},
            {"@type": "HowToStep", "position": 3, "name": "Zet de beurten in je agenda",
             "text": "Plan bijwerken en nieuwe lagen in het voorjaar en loop elk jaar zelf het houtwerk na."},
            {"@type": "HowToStep", "position": 4, "name": "Vraag op tijd offertes aan",
             "text": "Vraag in de winter offertes aan voor een beurt in het voorjaar of de zomer. Dan heb je de meeste keus."},
        ],
    }

    data_tag = ('<script type="application/json" id="okal-data">'
                + json.dumps(data, ensure_ascii=False).replace("</", "<\\/") + "</script>")
    body = (tool + uitleg + offerte + faq_html
            + '<link rel="stylesheet" href="/assets/css/onderhoudskalender.css">'
            + data_tag + '<script src="/assets/js/deelbeeld.js" defer></script>'
            + '<script src="/assets/js/onderhoudskalender.js" defer></script>')

    write(PAD, page(
        title("Onderhoudskalender: wanneer je huis weer schilderen?"),
        "Zie in één minuut wanneer je huis weer geschilderd moet worden: een tijdlijn van 15 jaar met bijwerken, nieuwe lagen en richtprijzen. Zet hem in je agenda.",
        PAD, body, [cr_ld, app_ld, howto_ld, faq_ld]), prio=0.8)

    from assets import css_klein
    for pad, inhoud in (("css/onderhoudskalender.css", css_klein(CSS)), ("js/onderhoudskalender.js", JS)):
        full = os.path.join(out, "assets", pad)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as f:
            f.write(inhoud)


CSS = """
.okal-kop{max-width:720px;margin-bottom:26px}
.okal-grid{display:grid;grid-template-columns:minmax(0,380px) minmax(0,1fr);gap:32px;align-items:start}
@media(max-width:900px){.okal-grid{grid-template-columns:minmax(0,1fr)}}
.okal-form .choice{grid-template-columns:1fr}
.okal-form .field select,.okal-form .field input[type=number]{width:100%}
.okal-fout{color:#b3261e;font-weight:600;font-size:.95rem;margin:0 0 12px}
.okal-uit{background:#fff;border:1px solid var(--line);border-radius:var(--radius-lg);box-shadow:var(--shadow);padding:26px;min-height:420px;min-width:0}
.okal-leeg{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;min-height:360px;color:var(--muted)}
.okal-leeg svg{margin-bottom:14px}
.okal-samen{display:flex;flex-wrap:wrap;gap:10px 22px;align-items:baseline;margin:0 0 6px}
.okal-samen h2{font-size:1.35rem;margin:0}
.okal-meta{color:var(--muted);font-size:.93rem;margin:0 0 18px}
.okal-lijn{list-style:none;margin:0 0 8px;padding:0;display:grid;grid-template-columns:repeat(16,minmax(0,1fr));gap:4px;position:relative}
.okal-lijn::before{content:"";position:absolute;left:0;right:0;top:15px;height:3px;background:var(--line);border-radius:2px}
.okal-lijn li{position:relative;display:flex;flex-direction:column;align-items:center;font-size:.72rem;color:var(--muted);font-variant-numeric:tabular-nums}
.okal-stip{width:12px;height:12px;border-radius:50%;background:#fff;border:2px solid #b9a988;margin:10px 0 6px;position:relative;z-index:1}
.okal-lijn .t-bij .okal-stip{width:18px;height:18px;margin:7px 0 3px;background:#0f8a5f;border-color:#0b6b49}
.okal-lijn .t-laag .okal-stip,.okal-lijn .t-opname .okal-stip{width:24px;height:24px;margin:4px 0 0;background:#f4820b;border-color:#a35200}
.okal-lijn .t-opname .okal-stip{background:#fff;border:4px solid #a35200}
.okal-lijn .sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.okal-lijn .nu{color:var(--ink);font-weight:750}
@media(max-width:640px){.okal-lijn{grid-template-columns:repeat(8,minmax(0,1fr));row-gap:10px}.okal-lijn::before{display:none}}
.okal-legenda{display:flex;flex-wrap:wrap;gap:6px 16px;font-size:.84rem;color:var(--muted);margin:0 0 20px;padding:0;list-style:none}
.okal-legenda li{display:flex;align-items:center;gap:6px}
.okal-legenda i{display:inline-block;width:12px;height:12px;border-radius:50%;border:2px solid #b9a988;background:#fff}
.okal-legenda .l-bij{background:#0f8a5f;border-color:#0b6b49}
.okal-legenda .l-laag{background:#f4820b;border-color:#a35200}
.okal-items{list-style:none;margin:0 0 18px;padding:0;border-top:1px solid var(--line)}
.okal-items li{display:grid;grid-template-columns:64px minmax(0,1fr) auto;gap:4px 14px;padding:12px 0;border-bottom:1px solid var(--line);align-items:baseline}
.okal-items .j{font-weight:800;color:var(--ink);font-variant-numeric:tabular-nums}
.okal-items .w strong{display:block;color:var(--ink)}
.okal-items .w span{font-size:.9rem}
.okal-items .p{font-weight:700;color:var(--ink);text-align:right;white-space:nowrap;font-variant-numeric:tabular-nums}
.okal-items .te-laat{display:inline-block;background:#fdecea;color:#8c1d18;font-size:.74rem;font-weight:750;border-radius:99px;padding:1px 8px;margin-left:6px;text-transform:uppercase;letter-spacing:.03em}
@media(max-width:520px){.okal-items li{grid-template-columns:52px minmax(0,1fr)}.okal-items .p{grid-column:2;text-align:left}}
.okal-totaal{background:var(--accent-soft);border-radius:var(--radius);padding:14px 16px;margin:0 0 18px;color:var(--ink)}
.okal-totaal strong{font-size:1.1rem}
.okal-tip{font-size:.92rem;margin:0 0 18px}
.okal-knoppen{display:flex;flex-wrap:wrap;gap:10px}
.okal-knoppen .btn{flex:1 1 180px}
.okal-gedeeld{font-size:.88rem;color:#0b6b49;margin:10px 0 0;min-height:1.4em}
.okal-teaser{background:var(--bg-soft);border-left:4px solid var(--accent);border-radius:8px;padding:12px 16px;margin:18px 0}
.okal-in{animation:okalIn .35s ease-out both}
@keyframes okalIn{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
@media(prefers-reduced-motion:reduce){.okal-in{animation:none}}
"""

JS = r"""(function () {
  "use strict";
  var DATA = JSON.parse(document.getElementById("okal-data").textContent);
  var form = document.getElementById("okal-form");
  var uit = document.getElementById("okal-uit");
  if (!form || !uit) return;
  var NU = new Date().getFullYear();
  var fout = form.querySelector(".okal-fout");
  var plan = null;

  function eur(n) { return "\u20ac" + Math.round(n).toLocaleString("nl-NL"); }
  function waarde(naam) { var i = form.querySelector('[name="' + naam + '"]:checked') || form.querySelector('[name="' + naam + '"]'); return i ? i.value : ""; }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  function bereken(inv) {
    var t = DATA.termijn[inv.kleur].slice();
    if (inv.ligging === "zwaar" && inv.kleur !== "transparant") { t[0] = Math.max(1, t[0] - 1); t[1] = Math.max(t[0] + 1, t[1] - 1); }
    var eind = NU + DATA.jaren, items = [], basis = null, notities = [];
    if (inv.laatst === "oud") basis = null;
    else if (inv.laatst) basis = +inv.laatst;
    else if (inv.bouwjaar >= NU - 4) { basis = inv.bouwjaar; notities.push("We tellen vanaf het bouwjaar " + inv.bouwjaar + "."); }

    if (basis === null) {
      items.push({ j: NU, t: "opname", laat: false });
      basis = NU;  /* na de opname volgt meestal een nieuwe laag; daarna telt de cyclus */
      items.push({ j: NU, t: "laag", laat: false, naOpname: true });
    } else {
      /* achterstallig? */
      if (basis + t[1] < NU) { items.push({ j: NU, t: "laag", laat: true }); basis = NU; }
      else if (basis + t[1] === NU) { items.push({ j: NU, t: "laag", laat: false }); basis = NU; }
      else if (basis + t[0] < NU) items.push({ j: NU, t: "bij", laat: true });
    }
    function heeft(j) { return items.some(function (i) { return i.j === j; }); }
    var c = basis;
    while (c <= eind) {
      var b = c + t[0], l = c + t[1];
      if (t[0] < t[1] && b >= NU && b <= eind && !heeft(b)) items.push({ j: b, t: "bij", laat: false });
      if (l >= NU && l <= eind && !heeft(l)) items.push({ j: l, t: "laag", laat: false });
      if (l <= c) break;
      c = l;
    }
    /* jaarlijkse controle in jaren zonder beurt */
    var bezet = {};
    items.forEach(function (i) { bezet[i.j] = true; });
    items.sort(function (a, b) { return a.j - b.j || (a.t === "opname" ? -1 : 1); });
    var w = DATA.woning[inv.woning];
    var lagen = items.filter(function (i) { return i.t === "laag"; }).length;
    var bij = items.filter(function (i) { return i.t === "bij"; }).length;
    if (NU - inv.bouwjaar >= 30) notities.push("Je huis is " + (NU - inv.bouwjaar) + " jaar oud. Vraag de schilder bij de opname ook naar houtrot en de staat van de kit.");
    return { inv: inv, t: t, items: items, bezet: bezet, prijs: w, lagen: lagen, bij: bij,
             totaal: [w[0] * lagen, w[1] * lagen], notities: notities, eind: eind };
  }

  function label(i) {
    if (i.t === "opname") return { kop: "Opname door een schilder", sub: "Laat de staat van het houtwerk bekijken. Daarna weet je wat er nodig is." };
    if (i.t === "laag") return { kop: i.naOpname ? "Waarschijnlijk: nieuwe laag" : "Nieuwe laag over al het houtwerk", sub: "Schuren, bijwerken en alles opnieuw schilderen. Plan in het voorjaar of de zomer." };
    return { kop: "Bijwerken", sub: "Onderdorpels, hoeken, kale randen en kit nalopen en bijwerken." };
  }
  function prijsTekst(i, p) {
    if (i.t === "laag") return eur(p.prijs[0]) + " \u2013 " + eur(p.prijs[1]);
    if (i.t === "bij") return "per uur";
    return "gratis offerte";
  }

  function toon(p, scroll) {
    var jaren = "";
    for (var j = NU; j <= p.eind; j++) {
      var it = p.items.filter(function (i) { return i.j === j; });
      var t = it.some(function (i) { return i.t === "opname"; }) ? "opname" : it.some(function (i) { return i.t === "laag"; }) ? "laag" : it.length ? "bij" : "controle";
      var lbl = t === "controle" ? "controle" : label(it[0]).kop;
      jaren += '<li class="t-' + t + '"><span class="okal-stip" title="' + esc(lbl) + '"></span><span class="' + (j === NU ? "nu" : "") + '">' + (j === NU ? "nu" : "\u2019" + String(j).slice(2)) + '</span><span class="sr-only"> ' + j + ": " + esc(lbl) + "</span></li>";
    }
    var lijst = p.items.map(function (i) {
      var l = label(i);
      return '<li><span class="j">' + i.j + '</span><span class="w"><strong>' + esc(l.kop) + (i.laat ? '<span class="te-laat">achterstallig</span>' : "") + "</strong><span>" + esc(l.sub) + '</span></span><span class="p">' + prijsTekst(i, p) + "</span></li>";
    }).join("");
    var inv = p.inv;
    uit.innerHTML =
      '<div class="okal-in">' +
      '<div class="okal-samen"><h2>Jouw kalender ' + NU + "\u2013" + p.eind + "</h2></div>" +
      '<p class="okal-meta">' + esc(DATA.woningNaam[inv.woning]) + ", bouwjaar " + inv.bouwjaar + ", " + esc(DATA.kleurNaam[inv.kleur]) +
      (inv.ligging === "zwaar" ? ", veel zon of wind" : "") + ". Bijwerken na " + p.t[0] + " jaar, nieuwe laag na " + p.t[1] + " jaar.</p>" +
      '<ol class="okal-lijn" aria-label="Tijdlijn per jaar">' + jaren + "</ol>" +
      '<ul class="okal-legenda" aria-hidden="true"><li><i class="l-laag"></i>Nieuwe laag</li><li><i class="l-bij"></i>Bijwerken</li><li><i></i>Zelf nalopen</li></ul>' +
      '<ul class="okal-items">' + lijst + "</ul>" +
      '<p class="okal-totaal">In ' + DATA.jaren + " jaar: <strong>" + p.lagen + (p.lagen === 1 ? " nieuwe laag" : " nieuwe lagen") + "</strong>" +
      (p.lagen ? ", samen ongeveer <strong>" + eur(p.totaal[0]) + " \u2013 " + eur(p.totaal[1]) + "</strong>" : "") +
      (p.bij ? ", plus " + p.bij + "\u00d7 bijwerken (per uur, " + eur(DATA.uur[0]) + " \u2013 " + eur(DATA.uur[1]) + " excl. btw)" : "") + ". Prijspeil 2026.</p>" +
      (p.notities.length ? '<p class="okal-tip">' + p.notities.map(esc).join(" ") + "</p>" : "") +
      '<div class="okal-knoppen">' +
      '<button type="button" class="btn btn-primary" data-act="offerte">Offertes voor ' + (p.items.length && p.items[0].j <= NU + 1 ? "mijn eerste beurt" : "later") + "</button>" +
      '<button type="button" class="btn btn-ghost" data-act="ics">Zet in je agenda (.ics)</button>' +
      '<button type="button" class="btn btn-ghost" data-act="beeld">Bewaar als plaatje</button>' +
      '<button type="button" class="btn btn-ghost" data-act="link">Kopieer link</button>' +
      '</div><p class="okal-gedeeld" aria-live="polite"></p></div>';
    if (scroll && window.innerWidth < 900) {
      var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      uit.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "start" });
    }
  }

  function lees() {
    var bj = parseInt(form.querySelector("#okal-bouwjaar").value, 10);
    if (!bj || bj < 1600 || bj > NU) return { fout: "Vul een bouwjaar in tussen 1600 en " + NU + "." };
    var laatst = waarde("laatst");
    if (laatst && laatst !== "oud" && +laatst < bj) return { fout: "De laatste schilderbeurt kan niet voor het bouwjaar liggen." };
    return { woning: waarde("woning"), bouwjaar: bj, laatst: laatst, kleur: waarde("kleur"), ligging: waarde("ligging") };
  }

  function maak(scroll) {
    var inv = lees();
    if (inv.fout) { fout.textContent = inv.fout; fout.hidden = false; return; }
    fout.hidden = true;
    plan = bereken(inv);
    toon(plan, scroll);
    try {
      var q = "w=" + inv.woning + "&b=" + inv.bouwjaar + "&l=" + (inv.laatst || "x") + "&k=" + inv.kleur + "&g=" + inv.ligging;
      history.replaceState(null, "", "#" + q);
    } catch (e) {}
  }

  form.addEventListener("submit", function (e) { e.preventDefault(); maak(true); });

  /* --- .ics --- */
  function icsTekst(s) { return String(s).replace(/\\/g, "\\\\").replace(/;/g, "\\;").replace(/,/g, "\\,").replace(/\r?\n/g, "\\n"); }
  function ics(p) {
    var stamp = new Date().toISOString().replace(/[-:]/g, "").replace(/\.\d+/, "");
    var r = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Topschilder//Onderhoudskalender//NL", "CALSCALE:GREGORIAN"];
    var n = 0;
    function ev(datum, titel, oms, extra) {
      var d = datum.replace(/-/g, "");
      var dt = new Date(datum + "T12:00:00"); dt.setDate(dt.getDate() + 1);
      var d2 = dt.toISOString().slice(0, 10).replace(/-/g, "");
      r.push("BEGIN:VEVENT", "UID:okal-" + d + "-" + (n++) + "@topschilder.nl", "DTSTAMP:" + stamp,
        "DTSTART;VALUE=DATE:" + d, "DTEND;VALUE=DATE:" + d2, "SUMMARY:" + icsTekst(titel), "DESCRIPTION:" + icsTekst(oms));
      if (extra) r.push(extra);
      r.push("BEGIN:VALARM", "ACTION:DISPLAY", "DESCRIPTION:" + icsTekst(titel), "TRIGGER:PT9H", "END:VALARM", "END:VEVENT");
    }
    p.items.forEach(function (i) {
      var l = label(i);
      var datum;
      if (i.j <= NU) { var d = new Date(); d.setDate(d.getDate() + 7); datum = d.toISOString().slice(0, 10); }
      else datum = i.j + "-01-15";
      ev(datum, "Schilderwerk: " + l.kop.toLowerCase() + " plannen",
        l.sub + " Vraag nu offertes aan, dan heb je voor het voorjaar nog keus. " + (i.t === "laag" ? "Richtprijs " + prijsTekst(i, p) + " (prijspeil 2026). " : "") + "https://topschilder.nl/offerte-aanvragen/");
    });
    ev((NU + 1) + "-03-20", "Houtwerk nalopen (jaarlijks)", "Loop kozijnen, deuren en boeidelen na: bladderende verf, scheuren, kale plekken en zachte plekken. Was het houtwerk mee als je de ramen lapt. Uitleg: https://topschilder.nl/onderhoudscheck/#zelf-checken",
      "RRULE:FREQ=YEARLY;COUNT=" + DATA.jaren);
    r.push("END:VCALENDAR");
    return r.join("\r\n");
  }

  /* --- afbeelding --- */
  function beeld(p) {
    return window.TSDeel.kaart(function (ctx, k, F) {
      ctx.fillStyle = "#241906"; ctx.font = "800 40px " + F;
      ctx.fillText("Mijn onderhoudskalender " + NU + "\u2013" + p.eind, k.x, k.y + 36);
      ctx.fillStyle = "#57492f"; ctx.font = "500 22px " + F;
      ctx.fillText(DATA.woningNaam[p.inv.woning] + ", bouwjaar " + p.inv.bouwjaar + ", " + DATA.kleurNaam[p.inv.kleur], k.x, k.y + 74);
      /* tijdlijn */
      var y = k.y + 150, n = DATA.jaren + 1, stap = k.b / n;
      ctx.fillStyle = "#e9e2d6"; ctx.fillRect(k.x + stap / 2, y - 2, k.b - stap, 4);
      for (var j = 0; j < n; j++) {
        var jaar = NU + j, cx = k.x + stap * j + stap / 2;
        var it = p.items.filter(function (i) { return i.j === jaar; });
        var t = it.some(function (i) { return i.t === "laag" || i.t === "opname"; }) ? "laag" : it.length ? "bij" : "c";
        ctx.beginPath(); ctx.arc(cx, y, t === "laag" ? 17 : t === "bij" ? 12 : 7, 0, Math.PI * 2);
        ctx.fillStyle = t === "laag" ? "#f4820b" : t === "bij" ? "#0f8a5f" : "#ffffff"; ctx.fill();
        ctx.lineWidth = 3; ctx.strokeStyle = t === "laag" ? "#a35200" : t === "bij" ? "#0b6b49" : "#b9a988"; ctx.stroke();
        ctx.fillStyle = j === 0 ? "#241906" : "#6f6047"; ctx.font = (j === 0 ? "800 " : "500 ") + "18px " + F; ctx.textAlign = "center";
        ctx.fillText(j === 0 ? "nu" : "\u2019" + String(jaar).slice(2), cx, y + 44);
      }
      ctx.textAlign = "left";
      /* eerstvolgende beurten */
      var regels = p.items.slice(0, 4), ry = y + 96;
      regels.forEach(function (i) {
        var l = label(i);
        ctx.fillStyle = "#241906"; ctx.font = "800 24px " + F; ctx.fillText(String(i.j), k.x, ry);
        ctx.font = "600 24px " + F; ctx.fillText(l.kop + (i.laat ? " (achterstallig)" : ""), k.x + 90, ry);
        ctx.textAlign = "right"; ctx.fillText(prijsTekst(i, p), k.x + k.b, ry); ctx.textAlign = "left";
        ry += 40;
      });
      if (p.lagen) {
        ctx.fillStyle = "#fff4e6"; window.TSDeel.rondRect(ctx, k.x, k.y + k.h - 56, k.b, 50, 10); ctx.fill();
        ctx.fillStyle = "#241906"; ctx.font = "700 22px " + F;
        ctx.fillText("In " + DATA.jaren + " jaar: " + p.lagen + (p.lagen === 1 ? " nieuwe laag" : " nieuwe lagen") + ", samen ongeveer " + eur(p.totaal[0]) + " \u2013 " + eur(p.totaal[1]), k.x + 18, k.y + k.h - 24);
      }
    }, "Onderhoudskalender");
  }

  function melding(t) { var m = uit.querySelector(".okal-gedeeld"); if (m) m.textContent = t; }

  uit.addEventListener("click", function (e) {
    var b = e.target.closest("[data-act]");
    if (!b || !plan) return;
    var act = b.getAttribute("data-act");
    if (act === "ics") {
      var blob = new Blob([ics(plan)], { type: "text/calendar;charset=utf-8" });
      var url = URL.createObjectURL(blob), a = document.createElement("a");
      a.href = url; a.download = "onderhoudskalender-schilderwerk.ics";
      document.body.appendChild(a); a.click(); a.remove();
      setTimeout(function () { URL.revokeObjectURL(url); }, 2000);
      melding("Het agendabestand is gedownload. Open het om de afspraken toe te voegen.");
    } else if (act === "beeld") {
      if (!window.TSDeel) return;
      var c = beeld(plan);
      if (navigator.canShare && /Mobi|Android|iPhone|iPad/.test(navigator.userAgent)) window.TSDeel.delen(c, "onderhoudskalender.png", "Mijn onderhoudskalender", "Mijn schilderbeurten voor de komende " + DATA.jaren + " jaar:", location.href);
      else { window.TSDeel.opslaan(c, "onderhoudskalender.png"); melding("Het plaatje is opgeslagen."); }
    } else if (act === "link") {
      var link = location.href;
      if (navigator.clipboard) navigator.clipboard.writeText(link).then(function () { melding("Link gekopieerd. Met deze link zie je dezelfde kalender."); }, function () { melding(link); });
      else melding(link);
    } else if (act === "offerte") {
      var box = document.getElementById("offerte");
      var f = box && box.querySelector("form[data-wizard]");
      if (!f) { location.href = "/offerte-aanvragen/"; return; }
      var eerste = plan.items[0];
      var planning = !eerste ? "Nog aan het ori\u00ebnteren" : eerste.laat ? "Zo snel mogelijk" : eerste.j <= NU ? "Binnen 1-3 maanden" : eerste.j === NU + 1 ? "Over 3-6 maanden" : "Nog aan het ori\u00ebnteren";
      [].forEach.call(f.querySelectorAll('input[name="dienst"]'), function (i) { i.checked = i.value === "Buitenschilderwerk"; });
      [].forEach.call(f.querySelectorAll('input[name="planning"]'), function (i) { i.checked = i.value === planning; });
      var oms = f.querySelector('textarea[name="omschrijving"]');
      if (oms && (!oms.value || oms.value.indexOf("Onderhoudskalender") === 0)) {
        oms.value = ("Onderhoudskalender: " + DATA.woningNaam[plan.inv.woning] + ", bouwjaar " + plan.inv.bouwjaar +
          ", laatste buitenbeurt " + (plan.inv.laatst === "oud" ? "langer dan 20 jaar geleden" : plan.inv.laatst || "onbekend") + ", " + DATA.kleurNaam[plan.inv.kleur] +
          (eerste ? ". Eerstvolgende: " + label(eerste).kop.toLowerCase() + " in " + eerste.j : "") + ".").slice(0, 900);
      }
      var actief = f.querySelector(".step.active"), stap1 = f.querySelector(".step");
      if (actief === stap1) { var nx = stap1.querySelector("[data-next]"); if (nx) nx.click(); }
      var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      box.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "start" });
      setTimeout(function () { var pc = f.querySelector('input[name="postcode"]'); if (pc && !pc.value) pc.focus({ preventScroll: true }); }, 500);
    }
  });

  /* --- link met instellingen terugzetten --- */
  (function () {
    var h = location.hash.slice(1);
    if (h.indexOf("w=") !== 0) return;
    var q = {};
    h.split("&").forEach(function (kv) { var d = kv.split("="); q[d[0]] = decodeURIComponent(d[1] || ""); });
    function zet(naam, v) { var i = form.querySelector('[name="' + naam + '"][value="' + v + '"]'); if (i) i.checked = true; }
    zet("woning", q.w); zet("kleur", q.k); zet("ligging", q.g);
    if (q.b) form.querySelector("#okal-bouwjaar").value = q.b;
    var sel = form.querySelector("#okal-laatst");
    if (q.l === "x") sel.value = "";
    else if (q.l && sel.querySelector('option[value="' + q.l + '"]')) sel.value = q.l;
    maak(false);
  })();
})();
"""
