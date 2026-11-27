# -*- coding: utf-8 -*-
"""
Verfcalculator (/verfcalculator/): hoeveel verf heb je nodig, en zelf doen of laten doen?

Meerdere ruimtes met ramen, deuren en plafond, plus binnendeuren en kozijnen om te lakken.
Je krijgt een boodschappenlijst in blikken, de materiaalkosten als je zelf schildert en
de richtprijs als een schilder het doet. De lijst kun je als plaatje bewaren (deelbeeld.js).

Verschil met /gids/verf-berekenen/: die gids legt het rendement uit met een simpele
rekenhulp voor één kamer. Deze tool rekent een hele klus door en vergelijkt de kosten.

Getallen:
- Rendement per laag: dezelfde vuistregels als de gids (muurverf 9 m²/l, plafond 8, voorstrijk 10,
  grondverf 11, lak 13 m²/l).
- Verfprijzen per liter: afgeleid van de rekenvoorbeelden in de kennisbank (kennis_ronde4a.py).
- Schilderprijzen: PRIJSBANDEN in kosten_data.py.
"""

import json
import os

from components import page, crumbs, offerte_form, faq_blok, title, eur
from kosten_data import PRIJSBANDEN

PAD = "/verfcalculator/"

RAAM_M2 = 1.5      # gemiddeld raam dat je van de muur aftrekt
DEUR_M2 = 1.9      # deuropening in de muur
DEUR_LAK_M2 = 4.0  # binnendeur, beide kanten (zelfde als de gids)
KOZIJN_LAK_M2 = 1.0  # binnenkozijn, zichtbare kanten (eigen aanname)

PRODUCTEN = {
    # id: naam, m² per liter per laag, blikmaten (liter), prijs per liter (van, tot)
    "muur": {"naam": "Muurverf (latex)", "rend": 9, "blik": [10, 5, 2.5, 1], "prijs": [8, 15]},
    "plafond": {"naam": "Plafondverf", "rend": 8, "blik": [10, 5, 2.5, 1], "prijs": [8, 15]},
    "voorstrijk": {"naam": "Voorstrijk", "rend": 10, "blik": [10, 5, 2.5, 1], "prijs": [8, 12]},
    "grond": {"naam": "Grondverf voor hout", "rend": 11, "blik": [2.5, 0.75], "prijs": [24, 40]},
    "lak": {"naam": "Lak voor deuren en kozijnen", "rend": 13, "blik": [2.5, 0.75], "prijs": [24, 40]},
}
GEREEDSCHAP = [30, 50]


def build_verfcalculator(write, out):
    pb = PRIJSBANDEN
    data = {
        "raam": RAAM_M2, "deurgat": DEUR_M2, "deurLak": DEUR_LAK_M2, "kozijnLak": KOZIJN_LAK_M2,
        "producten": PRODUCTEN, "gereedschap": GEREEDSCHAP,
        "schilder": {"m2": [pb["muren_plafonds_m2"]["van"], pb["muren_plafonds_m2"]["tot"]],
                     "deur": [pb["deur"]["van"], pb["deur"]["tot"]],
                     "kozijn": [pb["binnenkozijn"]["van"], pb["binnenkozijn"]["tot"]]},
    }
    cr, cr_ld = crumbs([("Home", "/"), ("Tools", "/tools/"), ("Verfcalculator", None)])

    tool = f"""{cr}
<section class="section-sm tool-hero vc-hero">
<div class="wrap">
  <div class="vc-kop">
    <span class="badge">Gratis tool · per ruimte · niets opgeslagen</span>
    <h1>Verfcalculator: zelf schilderen of laten doen?</h1>
    <p class="lead">Vul je ruimtes in, met ramen, deuren en plafond. Je ziet hoeveel blikken verf je moet kopen, wat dat kost en wat een schilder ongeveer vraagt. De boodschappenlijst bewaar je als plaatje op je telefoon.</p>
  </div>
  <div class="vc-grid">
    <form class="formcard vc-form" id="vc-form" novalidate>
      <h2>Je ruimtes</h2>
      <p class="sub">Maten in meters. Een komma of punt mag allebei.</p>
      <div id="vc-ruimtes"></div>
      <button type="button" class="btn btn-ghost btn-block vc-plus" id="vc-plus">+ Ruimte toevoegen</button>

      <h2 class="vc-h2">Houtwerk lakken</h2>
      <div class="row2">
        <div class="field"><label for="vc-deuren">Binnendeuren</label><input type="number" id="vc-deuren" min="0" max="40" value="0" inputmode="numeric"></div>
        <div class="field"><label for="vc-kozijnen">Binnenkozijnen</label><input type="number" id="vc-kozijnen" min="0" max="40" value="0" inputmode="numeric"></div>
      </div>

      <h2 class="vc-h2">Hoe schilder je?</h2>
      <div class="field"><label for="vc-lagen">Aantal lagen</label>
        <select id="vc-lagen"><option value="1">1 laag (opfrissen, zelfde kleur)</option><option value="2" selected>2 lagen (aanbevolen)</option><option value="3">3 lagen (donker naar licht)</option></select></div>
      <div class="field"><label for="vc-grond">Ondergrond</label>
        <select id="vc-grond"><option value="geverfd">Al geverfd, in goede staat</option><option value="kleur">Al geverfd, maar een heel andere kleur</option><option value="kaal">Kaal stucwerk of nieuwe gipsplaat</option></select></div>
    </form>

    <div class="vc-uit" id="vc-uit" aria-live="polite"></div>
  </div>
</div>
</section>"""

    uitleg = f"""<section class="section soft" id="zo-rekent-hij"><div class="wrap narrow prose">
  <h2>Zo rekent de verfcalculator</h2>
  <p>De muuroppervlakte is de omtrek van de kamer keer de hoogte. Daar gaat per raam {str(RAAM_M2).replace(".", ",")} m² af en per deur {str(DEUR_M2).replace(".", ",")} m². Het plafond is lengte keer breedte. Dat aantal m² keer het aantal lagen, gedeeld door het rendement, geeft de liters.</p>
  <div class="tablewrap"><table>
    <thead><tr><th>Product</th><th>Rendement per liter, per laag</th><th>Prijs per liter</th></tr></thead>
    <tbody>
      {"".join(f'<tr><td>{p["naam"]}</td><td class="num">{p["rend"]} m²</td><td class="num">{eur(p["prijs"][0])} – {eur(p["prijs"][1])}</td></tr>' for p in PRODUCTEN.values())}
    </tbody>
  </table></div>
  <p><small>Het rendement is een gemiddelde van wat fabrikanten op het blik zetten (zie de <a href="/gids/verf-berekenen/">gids over verf berekenen</a>). Op ruw of zuigend werk heb je meer nodig. De literprijzen komen uit de rekenvoorbeelden in onze kennisbank, bijvoorbeeld bij <a href="/kennisbank/nieuw-stucwerk-schilderen/">nieuw stucwerk schilderen</a>; voor gereedschap rekenen we {eur(GEREEDSCHAP[0])} tot {eur(GEREEDSCHAP[1])}. Een binnendeur telt voor {str(DEUR_LAK_M2).replace(".", ",")} m² (twee kanten), een binnenkozijn voor ongeveer {str(KOZIJN_LAK_M2).replace(".", ",")} m².</small></p>
  <h3>Wat een schilder rekent</h3>
  <p>Voor muren en plafonds rekent een schilder {eur(pb['muren_plafonds_m2']['van'])} tot {eur(pb['muren_plafonds_m2']['tot'])} per m², een binnendeur kost {eur(pb['deur']['van'])} tot {eur(pb['deur']['tot'])} en een binnenkozijn {eur(pb['binnenkozijn']['van'])} tot {eur(pb['binnenkozijn']['tot'])}. Dat is inclusief materiaal en 9% btw, prijspeil 2026. Meer uitleg vind je bij <a href="/kosten/schilderen-per-m2/">schilderen per m²</a>, <a href="/kosten/plafond-schilderen/">plafond schilderen</a> en <a href="/kosten/deuren-spuiten/">deuren spuiten</a>. Rekent de schilder per uur, kijk dan bij het <a href="/kosten/schilder-uurtarief/">uurtarief van een schilder</a>.</p>
  <h3>Zelf doen: tips om niet te veel te kopen</h3>
  <ul>
    <li>Koop alles van één kleur in één keer. Dan heb je zeker dezelfde mengkleur.</li>
    <li>Een groot blik is per liter goedkoper. Toch is een klein blik extra soms beter dan een groot blik dat half vol blijft staan.</li>
    <li>Gaat er een heel andere kleur op, of kaal stucwerk? Dan heb je eerst voorstrijk nodig, of een laag extra.</li>
  </ul>
</div></section>"""

    offerte = f"""<section class="section"><div class="wrap">
  <div class="grid g2" style="gap:48px;align-items:start">
    <div class="prose">
      <h2>Liever laten doen?</h2>
      <p class="lead">Vraag gratis offertes aan bij maximaal drie schilders uit jouw regio. Met de knop bij je uitslag zetten we je ruimtes en m² alvast in het formulier.</p>
      <ul class="checklist">
        <li>Gratis en vrijblijvend</li>
        <li>Maximaal drie schilders nemen contact op</li>
        <li>Je kiest zelf of je verder gaat</li>
      </ul>
    </div>
    <div>{offerte_form("Offertes voor je binnenschilderwerk", "Vier korte vragen · gratis en vrijblijvend")}</div>
  </div>
</div></section>"""

    faqs = [
        ("Hoeveel verf heb ik nodig voor een kamer?",
         "Voor een kamer van 4 bij 3 meter en 2,6 meter hoog, met één raam en één deur, is de muur ongeveer 33 m². Met twee lagen muurverf heb je dan ruim 7 liter nodig. Voor het plafond komt daar zo'n 3 liter plafondverf bij. De verfcalculator rekent het voor je uit in blikken."),
        ("Hoeveel lagen verf heb ik nodig?",
         "Meestal twee. Eén laag is genoeg als je een muur opfrist in dezelfde kleur. Ga je van donker naar licht, dan heb je vaak drie lagen nodig. Op kaal stucwerk zet je eerst een laag voorstrijk."),
        ("Is zelf schilderen veel goedkoper?",
         "Aan materiaal betaal je vaak maar een deel van wat een schilder vraagt. Maar je betaalt met je eigen tijd, en het resultaat hangt af van je ervaring. Bij hoge plafonds, trappenhuizen en lakwerk aan deuren zie je het verschil het snelst."),
        ("Waarom kost lak zo veel meer dan muurverf?",
         "Lak voor deuren en kozijnen is een harde, slijtvaste verf. Die is per liter duurder dan muurverf. Je hebt er wel veel minder van nodig: een deur is maar zo'n 4 m² aan twee kanten."),
    ]
    faq_html, faq_ld = faq_blok(faqs)

    app_ld = {
        "@context": "https://schema.org", "@type": "WebApplication",
        "name": "Verfcalculator", "url": "https://topschilder.nl" + PAD,
        "applicationCategory": "UtilitiesApplication", "operatingSystem": "Alle browsers",
        "inLanguage": "nl-NL", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"},
        "description": "Bereken hoeveel liter verf je nodig hebt per ruimte, met ramen, deuren, plafond en lagen. Met een boodschappenlijst in blikken en een vergelijking van zelf doen en laten doen.",
    }
    howto_ld = {
        "@context": "https://schema.org", "@type": "HowTo",
        "name": "Zo bereken je hoeveel verf je nodig hebt",
        "totalTime": "PT5M",
        "supply": [{"@type": "HowToSupply", "name": "Muurverf"}, {"@type": "HowToSupply", "name": "Plafondverf"}],
        "tool": [{"@type": "HowToTool", "name": "Rolmaat"}],
        "step": [
            {"@type": "HowToStep", "position": 1, "name": "Meet de kamer op",
             "text": "Meet de lengte, de breedte en de hoogte van de kamer in meters."},
            {"@type": "HowToStep", "position": 2, "name": "Reken de muur uit",
             "text": f"Tel lengte en breedte op, keer twee, keer de hoogte. Trek per raam ongeveer {str(RAAM_M2).replace('.', ',')} m² af en per deur {str(DEUR_M2).replace('.', ',')} m²."},
            {"@type": "HowToStep", "position": 3, "name": "Vermenigvuldig met het aantal lagen",
             "text": "Meestal zet je twee lagen. Op kaal stucwerk komt er een laag voorstrijk bij."},
            {"@type": "HowToStep", "position": 4, "name": "Deel door het rendement",
             "text": "Muurverf doet ongeveer 9 m² per liter per laag, plafondverf 8 m². Rond af naar hele blikken."},
        ],
    }

    data_tag = ('<script type="application/json" id="vc-data">'
                + json.dumps(data, ensure_ascii=False).replace("</", "<\\/") + "</script>")
    body = (tool + uitleg + offerte + faq_html
            + '<link rel="stylesheet" href="/assets/css/verfcalculator.css">'
            + data_tag + '<script src="/assets/js/deelbeeld.js" defer></script>'
            + '<script src="/assets/js/verfcalculator.js" defer></script>')

    write(PAD, page(
        title("Verfcalculator: hoeveel verf heb je nodig?"),
        "Bereken per ruimte hoeveel liter verf je nodig hebt, met ramen, deuren en plafond. Met een boodschappenlijst in blikken en wat een schilder zou kosten.",
        PAD, body, [cr_ld, app_ld, howto_ld, faq_ld]), prio=0.8)

    from assets import css_klein
    for pad, inhoud in (("css/verfcalculator.css", css_klein(CSS)), ("js/verfcalculator.js", JS)):
        full = os.path.join(out, "assets", pad)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as f:
            f.write(inhoud)


CSS = """
.vc-kop{max-width:720px;margin-bottom:26px}
.vc-grid{display:grid;grid-template-columns:minmax(0,420px) minmax(0,1fr);gap:32px;align-items:start}
@media(max-width:900px){.vc-grid{grid-template-columns:minmax(0,1fr)}}
.vc-h2{margin-top:22px}
.vc-form input,.vc-form select{width:100%}
#vc-ruimtes{min-height:250px}
.vc-ruimte{border:1px solid var(--line);border-radius:var(--radius);padding:14px 14px 4px;margin:0 0 12px;background:var(--bg-soft)}
.vc-ruimte-kop{display:flex;gap:8px;align-items:center;margin-bottom:10px}
.vc-ruimte-kop input{font-weight:700;flex:1;min-width:0}
.vc-weg{flex:0 0 auto;background:none;border:1px solid var(--line);border-radius:8px;color:var(--muted);font-size:.85rem;padding:8px 10px;cursor:pointer;min-height:40px}
.vc-weg:hover{color:#8c1d18;border-color:#e3b3ae}
.vc-maten{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}
.vc-maten .field,.vc-tel .field{margin-bottom:10px}
.vc-maten label,.vc-tel label{font-size:.82rem}
.vc-tel{display:grid;grid-template-columns:repeat(2,minmax(0,1fr)) auto;gap:8px;align-items:end}
.vc-check{display:flex;align-items:center;gap:8px;font-size:.88rem;font-weight:600;color:var(--ink);margin:0 0 10px;min-height:44px;cursor:pointer}
.vc-check input{width:18px;height:18px;accent-color:var(--accent)}
.vc-plus{margin-bottom:6px}
.vc-uit{background:#fff;border:1px solid var(--line);border-radius:var(--radius-lg);box-shadow:var(--shadow);padding:26px;min-width:0;min-height:480px;position:sticky;top:90px}
@media(max-width:900px){.vc-uit{position:static}}
.vc-uit h2{font-size:1.3rem;margin:0 0 4px}
.vc-meta{color:var(--muted);font-size:.93rem;margin:0 0 16px}
.vc-lijst{list-style:none;margin:0 0 18px;padding:0;border-top:1px solid var(--line)}
.vc-lijst li{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:2px 14px;padding:12px 0;border-bottom:1px solid var(--line)}
.vc-lijst strong{color:var(--ink)}
.vc-lijst .l{font-weight:800;color:var(--ink);text-align:right;font-variant-numeric:tabular-nums}
.vc-lijst small{grid-column:1/-1;color:var(--muted);font-size:.85rem}
.vc-blik{display:inline-flex;gap:4px;margin-top:4px;flex-wrap:wrap}
.vc-blik span{display:inline-block;background:var(--accent-soft);color:#7a3f00;border-radius:6px;padding:1px 8px;font-size:.82rem;font-weight:700}
.vc-vs{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:0 0 14px}
.vc-vs>div{border-radius:var(--radius);padding:14px;border:1px solid var(--line)}
.vc-vs .zelf{background:#eef8f3;border-color:#bfe3d1}
.vc-vs .laat{background:var(--accent-soft);border-color:#f7d3a8}
.vc-vs span{display:block;font-size:.85rem;color:var(--body)}
.vc-vs strong{display:block;font-size:1.25rem;color:var(--ink);font-variant-numeric:tabular-nums;margin:2px 0}
.vc-balk{height:10px;border-radius:5px;background:var(--line);overflow:hidden;margin-top:8px}
.vc-balk i{display:block;height:100%;border-radius:5px;transition:width .4s ease}
.vc-vs .zelf .vc-balk i{background:#0f8a5f}
.vc-vs .laat .vc-balk i{background:#d96f00}
@media(max-width:420px){.vc-vs{grid-template-columns:minmax(0,1fr)}}
.vc-noot{font-size:.86rem;color:var(--muted);margin:0 0 16px}
.vc-waarschuw{font-size:.9rem;background:#fff8e1;border-radius:8px;padding:10px 12px;margin:0 0 14px;color:#5c4400}
.vc-knoppen{display:flex;flex-wrap:wrap;gap:10px}
.vc-knoppen .btn{flex:1 1 180px}
.vc-melding{font-size:.88rem;color:#0b6b49;margin:10px 0 0;min-height:1.4em}
.vc-form .sr-only,.vc-uit .sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.vc-leeg{color:var(--muted);text-align:center;padding:40px 10px}
@media(prefers-reduced-motion:reduce){.vc-balk i{transition:none}}
"""

JS = r"""(function () {
  "use strict";
  var D = JSON.parse(document.getElementById("vc-data").textContent);
  var form = document.getElementById("vc-form"), lijst = document.getElementById("vc-ruimtes"), uit = document.getElementById("vc-uit");
  if (!form || !uit) return;
  var MAX = 8, res = null, teller = 0;

  function num(v) { var n = parseFloat(String(v).replace(",", ".")); return isFinite(n) && n > 0 ? n : 0; }
  function eur(n) { return "€" + Math.round(n).toLocaleString("nl-NL"); }
  function nl(n, d) { return (Math.round(n * Math.pow(10, d || 1)) / Math.pow(10, d || 1)).toLocaleString("nl-NL"); }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  function ruimteHtml(r) {
    var i = ++teller;
    return '<fieldset class="vc-ruimte" data-r>' +
      '<legend class="sr-only">Ruimte</legend>' +
      '<div class="vc-ruimte-kop"><label class="sr-only" for="vc-n' + i + '">Naam van de ruimte</label><input type="text" id="vc-n' + i + '" data-k="n" maxlength="30" value="' + esc(r.n) + '">' +
      '<button type="button" class="vc-weg" data-weg aria-label="Ruimte weghalen">Weg</button></div>' +
      '<div class="vc-maten">' +
      '<div class="field"><label for="vc-l' + i + '">Lengte</label><input type="text" inputmode="decimal" id="vc-l' + i + '" data-k="l" value="' + String(r.l).replace(".", ",") + '"></div>' +
      '<div class="field"><label for="vc-b' + i + '">Breedte</label><input type="text" inputmode="decimal" id="vc-b' + i + '" data-k="b" value="' + String(r.b).replace(".", ",") + '"></div>' +
      '<div class="field"><label for="vc-h' + i + '">Hoogte</label><input type="text" inputmode="decimal" id="vc-h' + i + '" data-k="h" value="' + String(r.h).replace(".", ",") + '"></div></div>' +
      '<div class="vc-tel">' +
      '<div class="field"><label for="vc-r' + i + '">Ramen</label><input type="number" min="0" max="20" inputmode="numeric" id="vc-r' + i + '" data-k="r" value="' + r.r + '"></div>' +
      '<div class="field"><label for="vc-d' + i + '">Deuren</label><input type="number" min="0" max="10" inputmode="numeric" id="vc-d' + i + '" data-k="d" value="' + r.d + '"></div>' +
      '<label class="vc-check"><input type="checkbox" data-k="p"' + (r.p ? " checked" : "") + '> Plafond</label></div></fieldset>';
  }
  function voegToe(r) {
    if (lijst.querySelectorAll("[data-r]").length >= MAX) return;
    lijst.insertAdjacentHTML("beforeend", ruimteHtml(r));
    knoppen();
  }
  function knoppen() {
    var n = lijst.querySelectorAll("[data-r]").length;
    document.getElementById("vc-plus").hidden = n >= MAX;
    [].forEach.call(lijst.querySelectorAll("[data-weg]"), function (b) { b.hidden = n <= 1; });
  }
  function ruimtes() {
    return [].map.call(lijst.querySelectorAll("[data-r]"), function (f) {
      function v(k) { return f.querySelector('[data-k="' + k + '"]'); }
      return { n: v("n").value.trim() || "Ruimte", l: num(v("l").value), b: num(v("b").value), h: num(v("h").value),
               r: Math.round(num(v("r").value)), d: Math.round(num(v("d").value)), p: v("p").checked };
    });
  }

  /* beste combinatie blikken: weinig verf over en niet te veel losse blikken */
  function blikken(liter, maten) {
    if (liter <= 0) return { combi: [], totaal: 0 };
    var best = null;
    var max = maten.map(function (m, i) { return i === 0 ? Math.ceil(liter / m) : Math.ceil(maten[0] / m); });
    (function zoek(i, gekozen, vol, aantal) {
      if (i === maten.length) {
        if (vol + 1e-9 < liter) return;
        var score = vol + aantal * 0.1 * maten[0];  /* weinig over, maar ook niet tien kleine blikjes */
        if (!best || score < best.score - 1e-9) best = { combi: gekozen.slice(), totaal: vol, aantal: aantal, score: score };
        return;
      }
      for (var k = 0; k <= max[i]; k++) { gekozen.push(k); zoek(i + 1, gekozen, vol + k * maten[i], aantal + k); gekozen.pop(); }
    })(0, [], 0, 0);
    var combi = [];
    maten.forEach(function (m, i) { if (best.combi[i]) combi.push({ n: best.combi[i], m: m }); });
    return { combi: combi, totaal: best.totaal };
  }

  function bereken() {
    var rs = ruimtes(), lagen = +document.getElementById("vc-lagen").value, grond = document.getElementById("vc-grond").value;
    var deuren = Math.min(40, Math.round(num(document.getElementById("vc-deuren").value)));
    var kozijnen = Math.min(40, Math.round(num(document.getElementById("vc-kozijnen").value)));
    var muur = 0, plafond = 0, onvolledig = 0;
    rs.forEach(function (r) {
      if (!r.l || !r.b || !r.h) { onvolledig++; return; }
      r.muur = Math.max(0, 2 * (r.l + r.b) * r.h - r.r * D.raam - r.d * D.deurgat);
      r.plafond = r.p ? r.l * r.b : 0;
      muur += r.muur; plafond += r.plafond;
    });
    var hout = deuren * D.deurLak + kozijnen * D.kozijnLak;
    var P = D.producten, regels = [];
    function regel(id, m2, lg, uitleg) {
      if (m2 <= 0) return;
      var liter = m2 * lg / P[id].rend, b = blikken(liter, P[id].blik);
      regels.push({ id: id, naam: P[id].naam, m2: m2, lagen: lg, liter: liter, b: b, uitleg: uitleg,
                    kost: [b.totaal * P[id].prijs[0], b.totaal * P[id].prijs[1]] });
    }
    if (grond === "kaal") regel("voorstrijk", muur + plafond, 1, "1 laag op kaal stucwerk of gipsplaat");
    regel("muur", muur, lagen, lagen + (lagen === 1 ? " laag" : " lagen") + " op " + nl(muur) + " m² muur");
    regel("plafond", plafond, lagen, lagen + (lagen === 1 ? " laag" : " lagen") + " op " + nl(plafond) + " m² plafond");
    if (hout > 0) {
      regel("grond", hout, 1, "1 laag op geschuurd of kaal hout");
      regel("lak", hout, 2, "2 lagen op " + nl(hout) + " m² houtwerk");
    }
    var mat = regels.reduce(function (s, r) { return [s[0] + r.kost[0], s[1] + r.kost[1]]; }, [0, 0]);
    if (regels.length) { mat[0] += D.gereedschap[0]; mat[1] += D.gereedschap[1]; }
    var S = D.schilder, m2 = muur + plafond;
    var laat = [m2 * S.m2[0] + deuren * S.deur[0] + kozijnen * S.kozijn[0], m2 * S.m2[1] + deuren * S.deur[1] + kozijnen * S.kozijn[1]];
    return { rs: rs, lagen: lagen, grond: grond, deuren: deuren, kozijnen: kozijnen, muur: muur, plafond: plafond,
             regels: regels, mat: mat, laat: laat, onvolledig: onvolledig };
  }

  function toon(e) {
    res = bereken();
    if (!res.regels.length) {
      uit.innerHTML = '<p class="vc-leeg">Vul de maten van minstens één ruimte in, of het aantal deuren of kozijnen. Je boodschappenlijst verschijnt hier.</p>';
      return;
    }
    var rij = res.regels.map(function (r) {
      return "<li><span><strong>" + esc(r.naam) + '</strong><span class="vc-blik">' +
        r.b.combi.map(function (c) { return "<span>" + c.n + "× " + nl(c.m, 2) + " l</span>"; }).join("") +
        '</span></span><span class="l">' + nl(r.liter) + " l</span><small>" + esc(r.uitleg) + ". Je koopt " + nl(r.b.totaal, 2) + " liter, " + eur(r.kost[0]) + " – " + eur(r.kost[1]) + ".</small></li>";
    }).join("");
    var max = Math.max(res.mat[1], res.laat[1]) || 1;
    var namen = res.rs.filter(function (r) { return r.muur !== undefined; }).map(function (r) { return r.n; });
    uit.innerHTML =
      "<h2>Je boodschappenlijst</h2>" +
      '<p class="vc-meta">' + (namen.length ? esc(namen.join(", ")) + ": " : "") + nl(res.muur + res.plafond) + " m² muur en plafond" +
      (res.deuren || res.kozijnen ? ", " + res.deuren + " deuren en " + res.kozijnen + " kozijnen" : "") + ".</p>" +
      (res.onvolledig ? '<p class="vc-waarschuw">' + res.onvolledig + (res.onvolledig === 1 ? " ruimte telt" : " ruimtes tellen") + " nog niet mee: vul lengte, breedte en hoogte in.</p>" : "") +
      (res.grond === "kleur" && res.lagen < 3 ? '<p class="vc-waarschuw">Een heel andere kleur? Reken op een laag extra, zeker van donker naar licht.</p>' : "") +
      '<ul class="vc-lijst">' + rij + "</ul>" +
      '<div class="vc-vs">' +
      '<div class="zelf"><span>Zelf doen (materiaal)</span><strong>' + eur(res.mat[0]) + " – " + eur(res.mat[1]) + '</strong><span>incl. gereedschap</span><div class="vc-balk"><i style="width:' + Math.round(res.mat[1] / max * 100) + '%"></i></div></div>' +
      '<div class="laat"><span>Laten doen (schilder)</span><strong>' + eur(res.laat[0]) + " – " + eur(res.laat[1]) + '</strong><span>incl. materiaal en btw</span><div class="vc-balk"><i style="width:' + Math.round(res.laat[1] / max * 100) + '%"></i></div></div></div>' +
      '<p class="vc-noot">Richtprijzen, prijspeil 2026. Bij zelf doen betaal je met je eigen tijd; een schilder is meestal sneller klaar.</p>' +
      '<div class="vc-knoppen">' +
      '<button type="button" class="btn btn-ghost" data-act="beeld">Bewaar lijst als plaatje</button>' +
      '<button type="button" class="btn btn-ghost" data-act="link">Kopieer link</button>' +
      '<button type="button" class="btn btn-primary" data-act="offerte">Liever laten doen</button>' +
      '</div><p class="vc-melding" aria-live="polite"></p>';
    if (e !== false) bewaarHash();
  }

  /* --- link met de ingevulde waarden --- */
  function bewaarHash() {
    try {
      var r = res.rs.map(function (x) { return [x.n.replace(/[~|]/g, " "), x.l, x.b, x.h, x.r, x.d, x.p ? 1 : 0].join("~"); }).join("|");
      var h = "r=" + encodeURIComponent(r) + "&lg=" + res.lagen + "&o=" + res.grond + "&dr=" + res.deuren + "&kz=" + res.kozijnen;
      history.replaceState(null, "", "#" + h);
    } catch (e) {}
  }
  function leesHash() {
    var h = location.hash.slice(1);
    if (h.indexOf("r=") !== 0) return false;
    var q = {};
    h.split("&").forEach(function (kv) { var d = kv.split("="); q[d[0]] = decodeURIComponent(d[1] || ""); });
    q.r.split("|").slice(0, MAX).forEach(function (s) {
      var a = s.split("~");
      voegToe({ n: a[0] || "Ruimte", l: num(a[1]) || "", b: num(a[2]) || "", h: num(a[3]) || "", r: Math.round(num(a[4])), d: Math.round(num(a[5])), p: a[6] === "1" });
    });
    if (/^[123]$/.test(q.lg)) document.getElementById("vc-lagen").value = q.lg;
    if (/^(geverfd|kleur|kaal)$/.test(q.o)) document.getElementById("vc-grond").value = q.o;
    document.getElementById("vc-deuren").value = Math.round(num(q.dr));
    document.getElementById("vc-kozijnen").value = Math.round(num(q.kz));
    return lijst.children.length > 0;
  }

  /* --- plaatje --- */
  function beeld() {
    return window.TSDeel.kaart(function (ctx, k, F) {
      ctx.fillStyle = "#241906"; ctx.font = "800 40px " + F;
      ctx.fillText("Mijn verf-boodschappenlijst", k.x, k.y + 36);
      ctx.fillStyle = "#57492f"; ctx.font = "500 22px " + F;
      ctx.fillText(nl(res.muur + res.plafond) + " m² muur en plafond, " + res.lagen + (res.lagen === 1 ? " laag" : " lagen") +
        (res.deuren || res.kozijnen ? ", " + res.deuren + " deuren, " + res.kozijnen + " kozijnen" : ""), k.x, k.y + 72);
      var y = k.y + 122;
      res.regels.slice(0, 5).forEach(function (r) {
        ctx.fillStyle = "#ffffff"; window.TSDeel.rondRect(ctx, k.x, y - 30, k.b * 0.62, 44, 8); ctx.fill();
        ctx.fillStyle = "#241906"; ctx.font = "700 23px " + F; ctx.fillText(r.naam, k.x + 14, y);
        ctx.textAlign = "right"; ctx.font = "800 23px " + F;
        ctx.fillText(r.b.combi.map(function (c) { return c.n + "× " + nl(c.m, 2) + " l"; }).join(" + "), k.x + k.b * 0.62 - 14, y);
        ctx.textAlign = "left"; y += 54;
      });
      var bx = k.x + k.b * 0.66, bb = k.b * 0.34;
      function vak(yy, kleur, rand, kop, bedrag) {
        ctx.fillStyle = kleur; window.TSDeel.rondRect(ctx, bx, yy, bb, 120, 12); ctx.fill();
        ctx.strokeStyle = rand; ctx.lineWidth = 2; ctx.stroke();
        ctx.fillStyle = "#57492f"; ctx.font = "600 20px " + F; ctx.fillText(kop, bx + 18, yy + 38);
        ctx.fillStyle = "#241906"; ctx.font = "800 32px " + F; ctx.fillText(bedrag, bx + 18, yy + 86);
      }
      vak(k.y + 92, "#eef8f3", "#bfe3d1", "Zelf doen (materiaal)", eur(res.mat[0]) + " – " + eur(res.mat[1]));
      vak(k.y + 232, "#fff4e6", "#f7d3a8", "Laten doen (schilder)", eur(res.laat[0]) + " – " + eur(res.laat[1]));
    }, "Verfcalculator");
  }

  function melding(t) { var m = uit.querySelector(".vc-melding"); if (m) m.textContent = t; }

  uit.addEventListener("click", function (e) {
    var b = e.target.closest("[data-act]");
    if (!b || !res) return;
    var act = b.getAttribute("data-act");
    if (act === "beeld" && window.TSDeel) {
      var c = beeld();
      if (navigator.canShare && /Mobi|Android|iPhone|iPad/.test(navigator.userAgent)) window.TSDeel.delen(c, "verf-boodschappenlijst.png", "Mijn verf-boodschappenlijst", "Zoveel verf heb ik nodig:", location.href);
      else { window.TSDeel.opslaan(c, "verf-boodschappenlijst.png"); melding("Het plaatje is opgeslagen."); }
    } else if (act === "link") {
      var link = location.href;
      if (navigator.clipboard) navigator.clipboard.writeText(link).then(function () { melding("Link gekopieerd."); }, function () { melding(link); });
      else melding(link);
    } else if (act === "offerte") {
      var box = document.getElementById("offerte"), f = box && box.querySelector("form[data-wizard]");
      if (!f) { location.href = "/offerte-aanvragen/"; return; }
      var m2 = res.muur + res.plafond;
      var omvang = m2 > 150 ? "Groot (hele woning)" : m2 > 60 || res.rs.length > 1 ? "Gemiddeld (meerdere ruimtes / halve woning)" : "Klein (1 ruimte / paar kozijnen)";
      [].forEach.call(f.querySelectorAll('input[name="dienst"]'), function (i) { i.checked = i.value === "Binnenschilderwerk"; });
      [].forEach.call(f.querySelectorAll('input[name="omvang"]'), function (i) { i.checked = i.value === omvang; });
      var oms = f.querySelector('textarea[name="omschrijving"]');
      if (oms && (!oms.value || oms.value.indexOf("Verfcalculator") === 0)) {
        var namen = res.rs.filter(function (r) { return r.muur !== undefined; }).map(function (r) { return r.n + " (" + nl(r.muur + r.plafond) + " m²" + (r.p ? ", met plafond" : "") + ")"; });
        oms.value = ("Verfcalculator: " + namen.join(", ") + (res.deuren ? ". " + res.deuren + " binnendeuren lakken" : "") + (res.kozijnen ? ". " + res.kozijnen + " binnenkozijnen lakken" : "") +
          ". " + res.lagen + " lagen" + (res.grond === "kaal" ? ", kaal stucwerk" : res.grond === "kleur" ? ", andere kleur" : "") + ".").slice(0, 900);
      }
      var actief = f.querySelector(".step.active"), stap1 = f.querySelector(".step");
      if (actief === stap1) { var nx = stap1.querySelector("[data-next]"); if (nx) nx.click(); }
      var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      box.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "start" });
    }
  });

  lijst.addEventListener("click", function (e) {
    var w = e.target.closest("[data-weg]");
    if (!w) return;
    w.closest("[data-r]").remove(); knoppen(); toon();
  });
  document.getElementById("vc-plus").addEventListener("click", function () {
    voegToe({ n: "Slaapkamer", l: 4, b: 3, h: 2.6, r: 1, d: 1, p: true }); toon();
    var laatste = lijst.lastElementChild; if (laatste) laatste.querySelector('[data-k="l"]').focus();
  });
  form.addEventListener("input", toon);
  form.addEventListener("change", toon);
  form.addEventListener("submit", function (e) { e.preventDefault(); });

  if (!leesHash()) voegToe({ n: "Woonkamer", l: 6, b: 4, h: 2.6, r: 2, d: 2, p: true });
  toon(false);
})();
"""
