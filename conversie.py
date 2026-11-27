# -*- coding: utf-8 -*-
"""Conversie-sessie: meer aanvragen, zonder valse claims.

build.py roept alleen aan:
  - ``html = conversie.verrijk(path, html)`` in write()
  - ``conversie.schrijf_js(OUT)`` in main()

verrijk() werkt op de kant-en-klare HTML, zodat components.py en de paginabouwers
niet hoeven te veranderen. Wat het doet:

  * body krijgt data-dienst / data-plaats / data-cv (paginatype). app.js vult
    daarmee het formulier al voor; conversie.js gebruikt het voor links en de sticky knop.
  * Formulier: tekst bij de voortgangsbalk ("Stap 2 van 4 · Adres en pand"),
    hulpteksten bij postcode, e-mail en telefoon, en onder het formulier het blok
    "Wat gebeurt er na je aanvraag?".
  * Kostenpagina's: de kale CTA "Wat kost X bij jou?" wordt een tussenstap met
    aantal + plaats, een indicatie op basis van de richtprijs, en een knop naar
    een voorgevuld formulier.
  * /offerte-aanvragen/: op mobiel staat het formulier direct onder de kop.

Veldnamen en de Supabase-koppeling blijven precies zoals ze waren.
"""

import json
import os
import re

from data import DIENSTEN, PLAATSEN
from kosten_data import KOSTEN

DIENST_NAAM = {d["slug"]: d["naam"] for d in DIENSTEN}
DIENST_KORT = {d["slug"]: d.get("naam_kort", d["naam"]) for d in DIENSTEN}
PLAATS_NAAM = {p["slug"]: p["naam"] for p in PLAATSEN}
KOSTEN_BY = {k["slug"]: k for k in KOSTEN}

STAPNAMEN = ["Je klus", "Adres en pand", "Omvang en planning", "Je gegevens"]

TELLER = {"form": 0, "kosten": 0}


def _esc(s):
    return (str(s).replace("&", "&amp;").replace('"', "&quot;")
            .replace("<", "&lt;").replace(">", "&gt;"))


def context(path):
    """(paginatype, dienst-slug, plaats-slug, kosten-slug) uit het pad."""
    delen = [d for d in path.strip("/").split("/") if d]
    if not delen:
        return "home", None, None, None
    if delen[0] == "schilderwerk" and len(delen) == 2 and delen[1] in DIENST_NAAM:
        return "dienst", delen[1], None, None
    if delen[0] == "schilder" and len(delen) >= 2 and delen[1] in PLAATS_NAAM:
        if len(delen) == 3 and delen[2] in DIENST_NAAM:
            return "plaatsdienst", delen[2], delen[1], None
        if len(delen) == 2:
            return "plaats", None, delen[1], None
    if delen[0] == "kosten" and len(delen) == 2 and delen[1] in KOSTEN_BY:
        k = KOSTEN_BY[delen[1]]
        return "kosten", k.get("dienst"), None, delen[1]
    if delen[0] == "offerte-aanvragen":
        return "offerte", None, None, None
    if delen[0] in ("gids", "kennisbank"):
        return "gids", None, None, None
    if delen[0] in ("prijzen", "kosten"):
        return "prijzen", None, None, None
    return "overig", None, None, None


# ---------------------------------------------------------------------------
# Formulier
# ---------------------------------------------------------------------------

HULP = [
    ('autocomplete="postal-code">',
     'autocomplete="postal-code" aria-describedby="cv-h-pc">'
     '<small class="cv-hulp" id="cv-h-pc">Alleen om schilders in jouw buurt te vinden.</small>'),
    ('<label>Hoe groot is de klus ongeveer?</label>',
     '<label>Hoe groot is de klus ongeveer?</label>'
     '<small class="cv-hulp">Een schatting is genoeg. De schilder vraagt zelf naar de details.</small>'),
    ('autocomplete="email" placeholder="naam@email.nl">',
     'autocomplete="email" placeholder="naam@email.nl" aria-describedby="cv-h-mail">'
     '<small class="cv-hulp" id="cv-h-mail">Hier krijg je direct een bevestiging van je aanvraag.</small>'),
    ('autocomplete="tel" placeholder="06 12345678">',
     'autocomplete="tel" placeholder="06 12345678" aria-describedby="cv-h-tel">'
     '<small class="cv-hulp" id="cv-h-tel">Alleen de schilders die je aanvraag krijgen (maximaal 3) bellen je. Geen reclame.</small>'),
]

NA_AANVRAAG = """<details class="cv-na"{open}>
  <summary>Wat gebeurt er na je aanvraag?</summary>
  <ol>
    <li><strong>Direct:</strong> je krijgt een bevestiging per mail met je klus, plaats en planning.</li>
    <li><strong>Wij kijken mee:</strong> we lezen elke aanvraag zelf en zoeken schilders die in jouw plaats werken en dit soort werk doen. Is iets onduidelijk, dan bellen we je soms kort.</li>
    <li><strong>De schilders bellen jou:</strong> maximaal drie bedrijven krijgen je gegevens en nemen zelf contact op voor een afspraak of offerte.</li>
    <li><strong>Jij kiest:</strong> vergelijk rustig. Je mag alle offertes afwijzen. Wil je je aanvraag intrekken? Beantwoord dan de bevestigingsmail.</li>
  </ol>
  <p>Is er in jouw plaats (nog) geen passende schilder? Dan laten we je dat weten.</p>
</details>"""

FORM_EINDE = ('<p><a class="btn btn-ghost" href="/prijzen/">Bekijk alvast wat schilderwerk kost</a></p>\n'
              '  </div>\n</div>')

STEPS_DIV = '<div class="steps"><div class="on"></div><div></div><div></div><div></div></div>'


def _formulier(html, open_na):
    if 'data-wizard data-table="leads"' not in html:
        return html
    for oud, nieuw in HULP:
        html = html.replace(oud, nieuw)
    html = html.replace(
        STEPS_DIV,
        STEPS_DIV.replace('<div class="steps">', '<div class="steps" aria-hidden="true">')
        + f'<p class="cv-stap" aria-live="polite" data-namen="{_esc(json.dumps(STAPNAMEN))}">'
          f'Stap 1 van 4 · {STAPNAMEN[0]}</p>')
    if FORM_EINDE in html:
        html = html.replace(FORM_EINDE, FORM_EINDE + "\n"
                            + NA_AANVRAAG.format(open=" open" if open_na else ""), 1)
        TELLER["form"] += 1
    return html


# ---------------------------------------------------------------------------
# Kostenpagina: tussenstap "Wat kost het bij jou?"
# ---------------------------------------------------------------------------

CTA_KOSTEN = re.compile(
    r'<div class="cta-midden reveal">\s*<div class="cta-midden-tekst"><p class="cta-midden-titel">'
    r'Wat kost [^<]* bij jou\?</p>.*?</a>\s*</div>', re.S)


def _eenheid_telbaar(eenheid):
    e = eenheid.lower()
    return e.startswith("per ") and "uur" not in e


def _kosten_blok(k, dienst):
    telbaar = _eenheid_telbaar(k["eenheid"])
    eenheid = k["eenheid"]
    aantal = ""
    if telbaar:
        aantal = f"""<div class="cv-veld">
      <label for="cv-aantal">Hoeveel ongeveer? <span>({_esc(eenheid)})</span></label>
      <input type="number" id="cv-aantal" min="1" max="999" step="1" inputmode="numeric" placeholder="bijv. 6">
    </div>"""
    return f"""<div class="cv-bijjou reveal" id="bij-jou" data-van="{k['van']}" data-tot="{k['tot']}"
  data-eenheid="{_esc(eenheid)}" data-klus="{_esc(k['klus'])}" data-dienst="{_esc(DIENST_NAAM.get(dienst, ''))}">
  <p class="cv-bijjou-titel">Wil je weten wat {_esc(k['klus'])} bij jou kost?</p>
  <p class="cv-bijjou-sub">Een richtprijs is een gemiddelde. Wat jij betaalt, hangt af van je huis, de staat van het werk en je regio. Vul twee dingen in, dan rekenen we een indicatie uit en zetten we je aanvraag alvast klaar.</p>
  <div class="cv-bijjou-velden">
    {aantal}
    <div class="cv-veld">
      <label for="cv-plaats">In welke plaats?</label>
      <input type="text" id="cv-plaats" autocomplete="address-level2" placeholder="bijv. Almere" maxlength="60">
    </div>
  </div>
  <p class="cv-indicatie" aria-live="polite" hidden></p>
  <a class="btn btn-primary" href="/offerte-aanvragen/" data-cv-door>Vraag offertes voor jouw situatie</a>
  <p class="cv-bijjou-noot">Gratis en vrijblijvend. Je ziet eerst het formulier; er wordt nog niets verstuurd.</p>
</div>"""


def _kosten(html, kosten_slug, dienst):
    k = KOSTEN_BY.get(kosten_slug)
    if not k:
        return html
    nieuw, n = CTA_KOSTEN.subn(lambda m: _kosten_blok(k, dienst), html, count=1)
    if n:
        TELLER["kosten"] += 1
    return nieuw


# ---------------------------------------------------------------------------
# Hoofdingang
# ---------------------------------------------------------------------------

def verrijk(path, html):
    if "<body" not in html or "/assets/js/app.js" not in html:
        return html
    soort, dienst, plaats, kosten_slug = context(path)

    attrs = f' data-cv="{soort}"'
    if dienst and "data-dienst=" not in html[:html.find("<body") + 400]:
        attrs += f' data-dienst="{_esc(DIENST_NAAM[dienst])}" data-dienst-kort="{_esc(DIENST_KORT[dienst])}"'
    if plaats:
        attrs += f' data-plaats="{_esc(PLAATS_NAAM[plaats])}"'
    html = html.replace("<body", "<body" + attrs, 1)

    html = _formulier(html, open_na=(soort == "offerte"))
    if soort == "kosten":
        html = _kosten(html, kosten_slug, dienst)

    html = html.replace('<script src="/assets/js/app.js" defer></script>',
                        '<script src="/assets/js/app.js" defer></script>'
                        '<script src="/assets/js/conversie.js" defer></script>', 1)
    html = html.replace("</head>", '<link rel="stylesheet" href="/assets/css/conversie.css"></head>', 1)
    return html


def schrijf_js(out):
    for sub, naam, inhoud in (("js", "conversie.js", JS), ("css", "conversie.css", CSS)):
        d = os.path.join(out, "assets", sub)
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, naam), "w", encoding="utf-8") as f:
            f.write(inhoud)
    print(f"  conversie: {TELLER['form']} formulieren met hulpteksten, "
          f"{TELLER['kosten']} kostenpagina's met tussenstap")


CSS = r"""/* Conversie-sessie: voortgang, hulpteksten, na-aanvraag, kosten-tussenstap, sticky */
.cv-stap{margin:-14px 0 16px;font-size:.84rem;font-weight:600;color:var(--muted,#6b5d4d)}
.cv-hulp{display:block;margin-top:5px;font-size:.8rem;line-height:1.35;color:var(--muted,#6b5d4d)}
.field > label + .cv-hulp{margin:-4px 0 8px}
.cv-klus{display:flex;align-items:center;justify-content:space-between;gap:8px;line-height:1.35;margin:0 0 14px;padding:9px 12px;border-radius:10px;background:var(--accent-soft,#fff1e0);font-size:.9rem}
.cv-klus button{background:none;border:0;padding:0;color:var(--accent-dark,#a04f00);text-decoration:underline;font:inherit;cursor:pointer}
.cv-na{margin-top:14px;background:#fff;border:1px solid var(--line,#eadfce);border-radius:var(--radius-lg,16px);padding:14px 18px;color:var(--body,#3b3024);font-size:.92rem}
.cv-na summary{cursor:pointer;font-weight:700;color:var(--ink,#22180e)}
.cv-na ol{margin:12px 0 8px;padding-left:20px}
.cv-na li{margin:0 0 6px}
.cv-na p{margin:0;font-size:.86rem;color:var(--muted,#6b5d4d)}
.cv-bijjou{margin:32px 0;padding:24px;border-radius:var(--radius-lg,16px);background:linear-gradient(135deg,#fff4e6,#fff);border:1.5px solid #f6d9b2}
.cv-bijjou-titel{font-size:1.25rem;line-height:1.3;font-weight:800;color:var(--ink,#22180e);margin:0 0 6px}
.cv-bijjou-sub{font-size:.95rem;margin:0 0 16px}
.cv-bijjou-velden{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px;margin-bottom:12px}
.cv-veld label{display:block;font-weight:600;font-size:.9rem;margin-bottom:5px}
.cv-veld label span{font-weight:400;color:var(--muted,#6b5d4d)}
.cv-veld input{width:100%;padding:12px 14px;border:1.5px solid var(--line,#eadfce);border-radius:10px;font:inherit;background:#fff}
.cv-indicatie{margin:4px 0 14px;font-size:1rem}
.cv-indicatie strong{font-size:1.15rem}
.cv-bijjou-noot{margin:10px 0 0;font-size:.82rem;color:var(--muted,#6b5d4d)}
.cv-exit{position:fixed;right:20px;bottom:20px;z-index:70;max-width:330px;background:#fff;border:1px solid var(--line,#eadfce);border-top:4px solid var(--accent,#d96f00);border-radius:14px;box-shadow:0 18px 50px rgba(40,25,5,.25);padding:18px 18px 16px;transform:translateY(20px);opacity:0;transition:transform .3s ease,opacity .3s ease}
.cv-exit.in{transform:none;opacity:1}
.cv-exit p{margin:0 0 12px;font-size:.92rem}
.cv-exit p strong{display:block;font-size:1.02rem;margin-bottom:4px;color:var(--ink,#22180e)}
.cv-exit .x{position:absolute;top:6px;right:8px;background:none;border:0;font-size:1.3rem;line-height:1;cursor:pointer;color:var(--muted,#6b5d4d);padding:4px}
.sticky-cta.cv-weg{transform:translateY(120%);opacity:0;pointer-events:none}
@media(max-width:980px){
  .cv-offerte .g2 > div:first-child{display:contents}
  .cv-offerte .g2{row-gap:12px !important}
  .cv-offerte .g2 > div:first-child > *{margin-top:0}
  .cv-offerte .g2 > div:first-child > .badge{justify-self:start}
  .cv-offerte .g2 > div:first-child > .checklist,.cv-offerte .g2 > div:first-child > .callout{order:3}
  .cv-offerte .g2 > div:last-child{order:2}
  .cv-offerte .g2 > div:first-child > h1,.cv-offerte .g2 > div:first-child > .lead{margin-bottom:0}
}
@media(prefers-reduced-motion:reduce){.cv-exit{transition:none}}
"""


JS = r"""/* Conversie-sessie: context vasthouden, slimmer voorvullen, voortgang, sticky knop,
   kosten-tussenstap. Verstuurt zelf niets: het formulier en de Supabase-koppeling
   staan in app.js en zijn niet aangepast. */
(function () {
  "use strict";
  var body = document.body, ds = body.dataset;
  var soort = ds.cv || "overig";
  var url = new URLSearchParams(location.search);
  var heeftForm = !!document.querySelector("form[data-wizard]");
  if (soort === "offerte") body.classList.add("cv-offerte");

  /* ---------- context: plaats onthouden binnen dit bezoek ---------- */
  function lees(k) { try { return sessionStorage.getItem(k) || ""; } catch (e) { return ""; } }
  function bewaar(k, v) { try { if (v) sessionStorage.setItem(k, v); } catch (e) {} }
  var plaats = url.get("plaats") || ds.plaats || lees("cv_plaats");
  bewaar("cv_plaats", url.get("plaats") || ds.plaats);
  var dienst = url.get("dienst") || ds.dienst || "";

  /* ---------- links naar het formulier: context meegeven ---------- */
  function offerteUrl(extra) {
    var q = new URLSearchParams();
    if (dienst) q.set("dienst", dienst);
    if (plaats) q.set("plaats", plaats);
    q.set("via", soort);
    Object.keys(extra || {}).forEach(function (k) { if (extra[k]) q.set(k, extra[k]); });
    return "/offerte-aanvragen/?" + q.toString();
  }
  [].forEach.call(document.querySelectorAll('a[href="/offerte-aanvragen/"]'), function (a) {
    if (a.hasAttribute("data-cv-door")) return;
    // Staat er een formulier op deze pagina, dan blijf je hier: geen nieuwe pagina, geen context kwijt.
    a.href = heeftForm ? "#offerte" : offerteUrl();
  });

  /* ---------- sticky knop: tekst per paginatype, weg bij formulier of typen ---------- */
  var sticky = document.querySelector(".sticky-cta");
  var stickyKnop = sticky && sticky.querySelector("a");
  if (stickyKnop) {
    var kort = (ds.dienstKort || dienst || "").toLowerCase();
    var label = "";
    if (soort === "kosten" && document.getElementById("bij-jou")) {
      label = "Wat kost het bij jou?"; stickyKnop.href = "#bij-jou";
    } else if (heeftForm) {
      if (soort === "plaatsdienst" && ds.plaats) label = "Offertes in " + ds.plaats;
      else if (soort === "plaats" && ds.plaats) label = "Offertes in " + ds.plaats + " aanvragen";
      else if (soort === "dienst" && kort) label = "Offertes voor " + kort;
      else label = "Start je aanvraag";
    } else if (soort === "gids" || soort === "prijzen") {
      label = "Vergelijk prijzen voor jouw klus";
    }
    if (label) stickyKnop.firstChild.nodeValue = label;
    var typt = false, bjInBeeld = false;
    var zet = function () { sticky.classList.toggle("cv-weg", typt || bjInBeeld); };
    var isVeld = function (el) { return !!(el && el.matches && el.matches("input, textarea, select")); };
    document.addEventListener("focusin", function (e) { if (isVeld(e.target)) { typt = true; zet(); } });
    document.addEventListener("focusout", function () {
      setTimeout(function () { typt = isVeld(document.activeElement); zet(); }, 50);
    });
    var bijjou = document.getElementById("bij-jou");
    if (bijjou && "IntersectionObserver" in window) {
      new IntersectionObserver(function (es) {
        es.forEach(function (e) { bjInBeeld = e.isIntersecting; }); zet();
      }, { threshold: 0.2 }).observe(bijjou);
    }
  }

  /* ---------- formulier: voortgangstekst, dienst overslaan, omschrijving ---------- */
  [].forEach.call(document.querySelectorAll("form[data-wizard]"), function (form) {
    var kaart = form.closest(".formcard") || form.parentNode;
    var stappen = [].slice.call(form.querySelectorAll(".step"));
    var tekst = kaart.querySelector(".cv-stap");
    var namen = [];
    try { namen = JSON.parse(tekst.getAttribute("data-namen")); } catch (e) {}
    function bijwerken() {
      var i = stappen.findIndex(function (s) { return s.classList.contains("active"); });
      if (i < 0 || !tekst) return;
      tekst.textContent = (i === stappen.length - 1 ? "Laatste stap · " : "Stap " + (i + 1) + " van " + stappen.length + " · ") + (namen[i] || "");
    }
    if (tekst && "MutationObserver" in window) {
      var mo = new MutationObserver(bijwerken);
      stappen.forEach(function (s) { mo.observe(s, { attributes: true, attributeFilter: ["class"] }); });
    }

    // Omschrijving voorvullen vanuit de kosten-tussenstap.
    var oms = url.get("oms");
    var ta = form.querySelector("textarea[name=omschrijving]");
    if (oms && ta && !ta.value) ta.value = oms.slice(0, 300);

    // Plaats ook voorvullen als die alleen uit dit bezoek bekend is.
    var pl = form.querySelector("input[name=plaats]");
    if (pl && !pl.value && plaats) pl.value = plaats.slice(0, 60);

    // Dienst al bekend (pagina of link)? Sla stap 1 over en laat zien wat er gekozen is.
    var gekozen = form.querySelector("input[name=dienst]:checked");
    if (gekozen && stappen[0] && stappen[0].classList.contains("active")) {
      var volgende = stappen[0].querySelector("[data-next]");
      if (volgende) {
        volgende.click();
        var chip = document.createElement("p");
        chip.className = "cv-klus";
        chip.innerHTML = '<span>Je klus: <strong></strong></span><button type="button">wijzigen</button>';
        chip.querySelector("strong").textContent = gekozen.value;
        chip.querySelector("button").addEventListener("click", function () {
          var terug = stappen[1].querySelector("[data-prev]");
          if (terug) terug.click();
        });
        stappen[1].insertBefore(chip, stappen[1].firstChild);
        form.querySelectorAll("input[name=dienst]").forEach(function (r) {
          r.addEventListener("change", function () { chip.querySelector("strong").textContent = r.value; });
        });
      }
    }
    bijwerken();
  });

  /* ---------- kostenpagina: tussenstap ---------- */
  var bj = document.getElementById("bij-jou");
  if (bj) {
    var van = parseFloat(bj.dataset.van), tot = parseFloat(bj.dataset.tot);
    var aantal = bj.querySelector("#cv-aantal"), plIn = bj.querySelector("#cv-plaats");
    var uit = bj.querySelector(".cv-indicatie"), door = bj.querySelector("[data-cv-door]");
    if (plIn && plaats) plIn.value = plaats;
    var euro = function (n) { return "€" + Math.round(n).toLocaleString("nl-NL"); };
    var rond = function (n) { return n >= 1000 ? Math.round(n / 50) * 50 : Math.round(n / 5) * 5; };
    function reken() {
      var n = aantal ? parseInt(aantal.value, 10) : 0;
      var p = (plIn.value || "").trim();
      var extra = {};
      if (n > 0 && n < 1000) {
        uit.hidden = false;
        uit.innerHTML = "Indicatie voor " + n + " (" + bj.dataset.eenheid + "): <strong>" +
          euro(rond(van * n)) + " – " + euro(rond(tot * n)) + "</strong>. " +
          "Een schilder geeft pas een vaste prijs als hij het werk heeft gezien.";
        extra.oms = "Via de kostenpagina " + bj.dataset.klus + ": ongeveer " + n + " (" + bj.dataset.eenheid + "). ";
      } else {
        uit.hidden = true;
      }
      if (p) bewaar("cv_plaats", p);
      var q = new URLSearchParams();
      if (bj.dataset.dienst) q.set("dienst", bj.dataset.dienst);
      if (p) q.set("plaats", p);
      q.set("via", "kosten");
      if (extra.oms) q.set("oms", extra.oms);
      door.href = "/offerte-aanvragen/?" + q.toString() + "#offerte";
    }
    if (aantal) aantal.addEventListener("input", reken);
    plIn.addEventListener("input", reken);
    reken();

    /* Exit-vriendelijk (alleen desktop): wie met de muis naar de tabbalk gaat, krijgt één keer
       per bezoek een klein kaartje. Geen pop-up over de pagina, wegklikken kan altijd. */
    var groot = window.matchMedia("(min-width: 981px) and (hover: hover)").matches;
    if (groot && !lees("cv_exit")) {
      var gezien = false;
      document.addEventListener("mouseout", function (e) {
        if (gezien || e.relatedTarget || e.clientY > 12) return;
        var r = bj.getBoundingClientRect();
        if (r.top < window.innerHeight && r.bottom > 0) return; // tussenstap al in beeld
        gezien = true; bewaar("cv_exit", "1");
        var k = document.createElement("div");
        k.className = "cv-exit"; k.setAttribute("role", "dialog"); k.setAttribute("aria-label", "Wat kost het bij jou?");
        k.innerHTML = '<button type="button" class="x" aria-label="Sluiten">×</button>' +
          "<p><strong>Wil je weten wat het bij jou kost?</strong>Vul het aantal en je plaats in, dan zie je meteen een indicatie.</p>" +
          '<a class="btn btn-primary btn-block" href="#bij-jou">Reken het uit</a>';
        document.body.appendChild(k);
        requestAnimationFrame(function () { k.classList.add("in"); });
        var sluit = function () { k.remove(); };
        k.querySelector(".x").addEventListener("click", sluit);
        k.querySelector("a").addEventListener("click", function () {
          sluit(); setTimeout(function () { (aantal || plIn).focus({ preventScroll: true }); }, 500);
        });
      });
    }
  }
})();
"""
