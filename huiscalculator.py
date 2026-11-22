# -*- coding: utf-8 -*-
"""Huiscalculator: wat kost het schilderen van je hele huis? (/kosten/calculator/)

Losse module, zodat build.py en assets.py bijna niet veranderen.
build.py roept alleen build_huiscalculator(write, out) aan.

Prijzen komen uitsluitend uit kosten_data.py (PRIJSBANDEN en KOSTEN) en de
regiocorrectie uit data.py (PRIJSINDEX). Hier staan geen eigen prijzen.
Wel staan hier de standaardaantallen per woningtype (hoeveel kozijnen, m²).
Waar de kostenpagina's die noemen, komen ze daarvandaan; de rest is een
startwaarde die de bezoeker zelf aanpast.
"""

import os
import re
import json

from data import DIENSTEN, PLAATSEN, PRIJSINDEX
from kosten_data import PRIJSBANDEN, KOSTEN_BY_SLUG
from components import page, crumbs, offerte_form, faq_blok, eur, title, icon

PAD = "/kosten/calculator/"


# ---------------------------------------------------------------------------
# Hulpjes om getallen uit de bestaande kostenteksten te halen
# ---------------------------------------------------------------------------

def _bereik(tekst):
    """'€1.500 – €3.500. ...' -> (1500, 3500). Faalt hard als het niet lukt."""
    m = re.search(r"€([\d.]+)\s*–\s*€([\d.]+)", tekst)
    if not m:
        raise ValueError(f"Geen prijsbereik gevonden in: {tekst!r}")
    return int(m.group(1).replace(".", "")), int(m.group(2).replace(".", ""))


def _extra(slug, begin):
    """Prijsbereik uit de 'extra'-lijst van een kostenpagina, op labelbegin."""
    for label, prijs in KOSTEN_BY_SLUG[slug]["extra"]:
        if label.startswith(begin):
            return _bereik(prijs)
    raise KeyError(f"{slug}: geen extra die begint met {begin!r}")


def _voorbeeld(slug, i):
    return KOSTEN_BY_SLUG[slug]["voorbeelden"][i]


def _band(sleutel):
    b = PRIJSBANDEN[sleutel]
    return b["van"], b["tot"]


# ---------------------------------------------------------------------------
# Woningtypes en standaardaantallen
# ---------------------------------------------------------------------------

KOZ_TUSSEN = _voorbeeld("kozijnen-schilderen", 0)[1]     # 8
KOZ_HOEK = _voorbeeld("kozijnen-schilderen", 1)[1]       # 12
KOZ_VRIJ = _voorbeeld("kozijnen-schilderen", 2)[1]       # 18
DEUR_TUSSEN = _voorbeeld("deuren-spuiten", 0)[1]         # 7
DEUR_VRIJ = _voorbeeld("deuren-spuiten", 1)[1]           # 11
M2_WONING = int(re.search(r"(\d+) m²", _voorbeeld("huis-schilderen", 3)[2]).group(1))  # 250
FRONTEN = _voorbeeld("keuken-spuiten", 1)[1]             # 16

WONINGTYPES = [
    {"key": "appartement", "naam": "Appartement",
     "std": {"kozijnen": 4, "buitendeuren": 1, "dakkapel": 1, "steiger": 1, "houtrot": 2,
             "muren": 150, "binnendeuren": 5, "binnenkozijnen": 5, "trap": 1, "keuken": FRONTEN},
     "bench": None},
    {"key": "tussenwoning", "naam": "Tussenwoning",
     "std": {"kozijnen": KOZ_TUSSEN, "buitendeuren": 2, "dakkapel": 1, "steiger": 1, "houtrot": 2,
             "muren": M2_WONING, "binnendeuren": DEUR_TUSSEN, "binnenkozijnen": DEUR_TUSSEN, "trap": 1, "keuken": FRONTEN},
     "bench": 0},
    {"key": "hoekwoning", "naam": "Hoekwoning",
     "std": {"kozijnen": KOZ_HOEK, "buitendeuren": 2, "dakkapel": 1, "steiger": 2, "houtrot": 2,
             "muren": 270, "binnendeuren": 8, "binnenkozijnen": 8, "trap": 1, "keuken": FRONTEN},
     "bench": 1},
    {"key": "twee-onder-een-kap", "naam": "Twee-onder-een-kap",
     "std": {"kozijnen": KOZ_HOEK, "buitendeuren": 2, "dakkapel": 1, "steiger": 2, "houtrot": 2,
             "muren": 290, "binnendeuren": 9, "binnenkozijnen": 9, "trap": 1, "keuken": FRONTEN},
     "bench": 1},
    {"key": "vrijstaand", "naam": "Vrijstaand",
     "std": {"kozijnen": KOZ_VRIJ, "buitendeuren": 2, "dakkapel": 1, "steiger": 3, "houtrot": 3,
             "muren": 350, "binnendeuren": DEUR_VRIJ, "binnenkozijnen": DEUR_VRIJ, "trap": 1, "keuken": FRONTEN},
     "bench": 2},
]

BOUWPERIODES = [
    {"key": "voor-1945", "naam": "Voor 1945",
     "tip": "Bij een oudere woning zit er vaak meer voorwerk in: oude verflagen, kitnaden en houtrot. Reken eerder met de bovenkant van de range."},
    {"key": "1945-1974", "naam": "1945 – 1974",
     "tip": "Veel woningen uit deze tijd hebben grote raampartijen. Tel je kozijnen even na: dat bepaalt een groot deel van de prijs buiten."},
    {"key": "1975-1999", "naam": "1975 – 1999",
     "tip": "Veel woningen uit deze periode zijn toe aan een flinke beurt van het oorspronkelijke houtwerk. Laat de schilder op houtrot controleren."},
    {"key": "2000-nu", "naam": "2000 of later",
     "tip": "Bij een jongere woning is het voorwerk meestal beperkt. Dan kom je vaak dichter bij de onderkant van de range."},
    {"key": "nieuwbouw", "naam": "Jonger dan 2 jaar",
     "tip": "Je woning is jonger dan twee jaar. Dan geldt 21% btw in plaats van 9%. De calculator rekent dat voor je om."},
]

# Prijzen zijn inclusief 9% btw. Voor een woning jonger dan twee jaar geldt 21%.
BTW_NIEUWBOUW = round(1.21 / 1.09, 4)


# ---------------------------------------------------------------------------
# Onderdelen (alle prijzen uit kosten_data.py)
# ---------------------------------------------------------------------------

def onderdelen():
    dakkapel = KOSTEN_BY_SLUG["dakkapel-schilderen"]
    spuit = KOSTEN_BY_SLUG["deuren-spuiten"]
    kwast = _extra("deuren-spuiten", "Deur met de kwast")
    trap_vb = KOSTEN_BY_SLUG["trap-schilderen"]["voorbeelden"]
    return [
        # ---- buiten
        {"key": "kozijnen", "groep": "buiten", "naam": "Buitenkozijnen", "prijs": _band("buitenkozijn"),
         "een": "kozijn", "mv": "kozijnen", "max": 40,
         "tip": f"Ongeveer {KOZ_TUSSEN} bij een tussenwoning, {KOZ_HOEK} bij een hoekwoning of twee-onder-een-kap en {KOZ_VRIJ} bij een vrijstaande woning. Ramen en draaiende delen horen erbij.",
         "link": "/kosten/kozijnen-schilderen/"},
        {"key": "buitendeuren", "groep": "buiten", "naam": "Buitendeuren", "prijs": _band("deur"),
         "een": "deur", "mv": "deuren", "max": 6,
         "tip": "Voordeur, achterdeur en eventueel de deur van de schuur of garage."},
        {"key": "boeidelen", "groep": "buiten", "naam": "Boeidelen en windveren", "prijs": None,
         "tip": "De planken langs de dakrand. Schilders nemen ze mee in de prijs voor het houtwerk buiten; er is geen losse richtprijs. Ze komen wel in je aanvraag te staan."},
        {"key": "dakkapel", "groep": "buiten", "naam": "Dakkapel", "prijs": (dakkapel["van"], dakkapel["tot"]),
         "een": "dakkapel", "mv": "dakkapellen", "max": 4,
         "tip": "De prijs hangt af van de breedte en hoe goed hij bereikbaar is. Vaak zit de steiger er al bij.",
         "link": "/kosten/dakkapel-schilderen/"},
        {"key": "steiger", "groep": "buiten", "naam": "Steiger of hoogwerker", "prijs": _band("steiger"),
         "een": "gevel", "mv": "gevels", "max": 4,
         "tip": "Bijna altijd nodig voor de bovenverdieping. Tel de gevels waar de schilder hoog moet werken."},
        {"key": "houtrot", "groep": "buiten", "naam": "Houtrot repareren", "prijs": _band("houtrot_plek"),
         "een": "plek", "mv": "plekken", "max": 15,
         "tip": "Plekken waar het hout zacht is als je er met een schroevendraaier in prikt. Weet je het niet, laat de schilder het dan bekijken."},
        # ---- binnen
        {"key": "muren", "groep": "binnen", "naam": "Muren en plafonds", "prijs": _band("muren_plafonds_m2"),
         "een": "m²", "mv": "m²", "max": 600, "min": 10, "stap": 10, "schuif": True,
         "tip": f"Een slaapkamer is zo'n {_voorbeeld('schilderen-per-m2', 0)[1]} m² muur en plafond, een woonkamer zo'n {_voorbeeld('schilderen-per-m2', 1)[1]} m². Een hele woning zit rond de {M2_WONING} m².",
         "link": "/kosten/schilderen-per-m2/"},
        {"key": "binnendeuren", "groep": "binnen", "naam": "Binnendeuren", "prijs": kwast,
         "een": "deur", "mv": "deuren", "max": 20,
         "varianten": [
             {"key": "k", "naam": "Met de kwast", "prijs": kwast},
             {"key": "s", "naam": "Gespoten", "prijs": (spuit["van"], spuit["tot"])},
         ],
         "tip": "Spuiten geeft een gladde laag zonder kwaststreken. Met de kwast is goedkoper.",
         "link": "/kosten/deuren-spuiten/"},
        {"key": "binnenkozijnen", "groep": "binnen", "naam": "Binnenkozijnen", "prijs": _band("binnenkozijn"),
         "een": "kozijn", "mv": "kozijnen", "max": 20,
         "tip": "De kozijnen rond je binnendeuren. Meestal net zoveel als je deuren hebt."},
        {"key": "trap", "groep": "binnen", "naam": "Trap", "prijs": _band("trap"),
         "een": "trap", "mv": "trappen", "max": 3,
         "varianten": [
             {"key": "d", "naam": "Dichte rechte trap", "prijs": _bereik(trap_vb[0][2])},
             {"key": "k", "naam": "Met een draai", "prijs": _bereik(trap_vb[1][2])},
             {"key": "o", "naam": "Open met spijlen", "prijs": _bereik(trap_vb[2][2])},
         ],
         "tip": "Per trap van één verdieping. Het trapgat komt er soms apart bij.",
         "link": "/kosten/trap-schilderen/"},
        {"key": "keuken", "groep": "binnen", "naam": "Keukenfronten spuiten", "prijs": _band("keukenfront"),
         "een": "front", "mv": "fronten", "max": 40,
         "tip": f"Elke deur en la telt als front. Een gemiddelde keuken heeft er zo'n {FRONTEN}.",
         "link": "/kosten/keuken-spuiten/"},
    ]


def _benchmarks():
    vb = KOSTEN_BY_SLUG["huis-schilderen"]["voorbeelden"]
    buiten = [{"label": vb[i][0], "prijs": _bereik(vb[i][2])} for i in range(3)]
    binnen = {"label": vb[3][0], "prijs": _bereik(vb[3][2]), "m2": M2_WONING}
    return buiten, binnen


def _dienstnaam(slug):
    return next(d["naam"] for d in DIENSTEN if d["slug"] == slug)


def _data_json():
    buiten, binnen = _benchmarks()
    plaatsen = [{"slug": p["slug"], "naam": p["naam"], "prov": p["provincie"],
                 "index": PRIJSINDEX.get(p["provincie"], 1.0)} for p in PLAATSEN]
    data = {
        "onderdelen": [{k: v for k, v in o.items() if k not in ("tip",)} for o in onderdelen()],
        "types": WONINGTYPES,
        "periodes": BOUWPERIODES,
        "btwNieuwbouw": BTW_NIEUWBOUW,
        "plaatsen": plaatsen,
        "benchBuiten": buiten,
        "benchBinnen": binnen,
        "diensten": {s: _dienstnaam(s) for s in ("buitenschilderwerk", "binnenschilderwerk", "spuitwerk", "houtrot-reparatie")},
    }
    return json.dumps(data, ensure_ascii=False).replace("</", "<\\/")


# ---------------------------------------------------------------------------
# Markup
# ---------------------------------------------------------------------------

TYPE_ICON = {
    "appartement": '<rect x="10" y="6" width="28" height="36" rx="1.5"/><path d="M16 13h4M24 13h4M16 20h4M24 20h4M16 27h4M24 27h4M21 42v-7h6v7"/>',
    "tussenwoning": '<path d="M2 22 10 14l8 8M18 22l8-8 8 8M34 22l8-8 4 4"/><path d="M4 21v21h40V21"/><path d="M22 42v-9h4v9"/>',
    "hoekwoning": '<path d="M4 22 14 12l10 10M24 22l10-10 10 10"/><path d="M6 21v21h36V21"/><path d="M30 42v-9h5v9M10 28h6v5h-6z"/>',
    "twee-onder-een-kap": '<path d="M3 24 24 7l21 17"/><path d="M7 21v21h34V21M24 7v35"/><path d="M12 42v-8h5v8M31 42v-8h5v8"/>',
    "vrijstaand": '<path d="M6 24 24 9l18 15"/><path d="M10 21v21h28V21"/><path d="M21 42v-9h6v9M14 27h5v5h-5zM29 27h5v5h-5z"/>',
}


def _type_keuzes():
    out = ""
    for t in WONINGTYPES:
        out += (f'<label class="hc-type"><input type="radio" name="hc-type" value="{t["key"]}">'
                f'<span class="hc-type-kaart"><svg viewBox="0 0 48 48" aria-hidden="true" focusable="false">{TYPE_ICON[t["key"]]}</svg>'
                f'<span>{t["naam"]}</span></span></label>')
    return out


def _periode_keuzes():
    return "".join(
        f'<label class="hc-chip"><input type="radio" name="hc-periode" value="{p["key"]}"><span>{p["naam"]}</span></label>'
        for p in BOUWPERIODES)


def _onderdeel_html(o):
    k = o["key"]
    if o["prijs"]:
        prijs = f'{eur(o["prijs"][0])} – {eur(o["prijs"][1])} per {o["een"]}'
        if o.get("varianten"):
            lo = min(v["prijs"][0] for v in o["varianten"])
            hi = max(v["prijs"][1] for v in o["varianten"])
            prijs = f'{eur(lo)} – {eur(hi)} per {o["een"]}'
    else:
        prijs = "zit in de prijs voor het houtwerk"
    link = f' <a href="{o["link"]}">Meer over deze prijs</a>' if o.get("link") else ""

    aantal = ""
    if o["prijs"]:
        mn = o.get("min", 1)
        stap = o.get("stap", 1)
        schuif = (f'<input type="range" class="hc-schuif" min="{mn}" max="{o["max"]}" step="{stap}" '
                  f'aria-label="{o["naam"]} in m²" data-schuif="{k}">') if o.get("schuif") else ""
        var = ""
        if o.get("varianten"):
            var = '<div class="hc-var" role="radiogroup" aria-label="Soort">' + "".join(
                f'<label class="hc-chip hc-chip-sm"><input type="radio" name="hc-var-{k}" value="{v["key"]}"{" checked" if i == 0 else ""}>'
                f'<span>{v["naam"]} <small>{eur(v["prijs"][0])} – {eur(v["prijs"][1])}</small></span></label>'
                for i, v in enumerate(o["varianten"])) + "</div>"
        aantal = f"""<div class="hc-aantal" hidden>
  {var}
  <div class="hc-stepper">
    <button type="button" class="hc-min" aria-label="Minder {o['mv']}">−</button>
    <input type="number" inputmode="numeric" min="{mn}" max="{o['max']}" step="{stap}" id="hc-n-{k}" aria-label="Aantal {o['mv']}">
    <span class="hc-eenheid">{o['mv']}</span>
    <button type="button" class="hc-plus" aria-label="Meer {o['mv']}">+</button>
    <output class="hc-regel" for="hc-n-{k}" aria-live="off"></output>
  </div>
  {schuif}
</div>"""
    return f"""<div class="hc-opt" data-key="{k}">
  <label class="hc-opt-kop">
    <input type="checkbox" class="hc-check" value="{k}">
    <span class="hc-vink" aria-hidden="true">{icon('check', 14)}</span>
    <span class="hc-opt-tekst"><strong>{o['naam']}</strong><small>{prijs}</small></span>
  </label>
  {aantal}
  <p class="hc-tip">{o['tip']}{link}</p>
</div>"""


def _huis_svg():
    """Huisje in het overzicht. Onderdelen lichten oranje op als je ze kiest."""
    return """<svg class="hc-huis" viewBox="0 0 240 172" role="img" aria-label="Tekening van je woning; gekozen onderdelen kleuren oranje">
  <g class="hc-woning">
    <g class="hc-buur hc-buur-l"><path d="M8 84 44 46l36 38v76H8z"/><rect x="20" y="96" width="20" height="18" rx="1"/><rect x="48" y="96" width="20" height="18" rx="1"/><rect x="20" y="126" width="20" height="18" rx="1"/></g>
    <g class="hc-buur hc-buur-r"><path d="M160 84l36-38 36 38v76h-72z"/><rect x="172" y="96" width="20" height="18" rx="1"/><rect x="200" y="96" width="20" height="18" rx="1"/><rect x="200" y="126" width="20" height="18" rx="1"/></g>
    <rect class="hc-muur" x="82" y="82" width="76" height="78"/>
    <path class="hc-dak" d="M74 86 120 38l46 48z"/>
    <polyline class="hc-p hc-p-boeidelen" points="72,88 120,37 168,88"/>
    <g class="hc-p hc-p-dakkapel"><rect x="104" y="58" width="32" height="20" rx="1"/><path d="M100 58h40"/><rect class="hc-raam" x="110" y="62" width="20" height="12"/></g>
    <rect class="hc-p hc-p-kozijnen hc-raam" x="90" y="94" width="24" height="20" rx="1"/>
    <rect class="hc-p hc-p-kozijnen hc-raam" x="126" y="94" width="24" height="20" rx="1"/>
    <rect class="hc-p hc-p-kozijnen hc-raam" x="126" y="126" width="24" height="22" rx="1"/>
    <rect class="hc-p hc-p-buitendeuren" x="93" y="122" width="18" height="38" rx="1"/>
    <g class="hc-p hc-p-steiger"><path d="M168 160V70M182 160V70M166 84h18M166 112h18M166 140h18M168 112l14-28M168 140l14-28"/></g>
  </g>
  <g class="hc-flat">
    <rect class="hc-muur-flat" x="54" y="26" width="132" height="134" rx="2"/>
    <g class="hc-flat-ramen"><rect x="66" y="38" width="20" height="16"/><rect x="154" y="38" width="20" height="16"/><rect x="66" y="66" width="20" height="16"/><rect x="154" y="66" width="20" height="16"/><rect x="66" y="94" width="20" height="16"/><rect x="154" y="94" width="20" height="16"/><rect x="66" y="122" width="20" height="16"/><rect x="154" y="122" width="20" height="16"/></g>
    <rect class="hc-unit" x="92" y="60" width="56" height="28" rx="2"/>
    <rect class="hc-p hc-p-kozijnen hc-raam" x="98" y="66" width="18" height="16"/>
    <rect class="hc-p hc-p-kozijnen hc-raam" x="124" y="66" width="18" height="16"/>
    <rect class="hc-p hc-p-buitendeuren" x="110" y="132" width="20" height="28" rx="1"/>
  </g>
  <path class="hc-grond" d="M0 160h240"/>
</svg>"""


def huiscalculator_html():
    ond = onderdelen()
    buiten = "".join(_onderdeel_html(o) for o in ond if o["groep"] == "buiten")
    binnen = "".join(_onderdeel_html(o) for o in ond if o["groep"] == "binnen")

    plaats_opts = '<option value="">Kies je plaats</option>'
    for prov in sorted(PRIJSINDEX, key=lambda p: PRIJSINDEX[p]):
        ps = sorted((p for p in PLAATSEN if p["provincie"] == prov), key=lambda p: p["naam"])
        if ps:
            plaats_opts += f'<optgroup label="{prov}">' + "".join(
                f'<option value="{p["slug"]}">{p["naam"]}</option>' for p in ps) + "</optgroup>"
    plaats_opts += '<option value="anders">Een andere plaats</option>'

    stappen = ["Woning", "Buiten", "Binnen", "Plaats", "Uitkomst"]
    huidig = ' aria-current="step"'
    nav = "".join(
        f'<li><button type="button" data-ga="{i}"{huidig if i == 0 else " disabled"}>'
        f'<span class="hc-nr">{i + 1}</span><span class="hc-nav-tekst">{s}</span></button></li>'
        for i, s in enumerate(stappen))

    return f"""<div class="hc" data-hc>
  <ol class="hc-nav" aria-label="Stappen">{nav}</ol>
  <div class="hc-grid">
    <div class="hc-main">

      <section class="hc-stap is-actief" data-stap="0" aria-labelledby="hc-k0">
        <h2 id="hc-k0" tabindex="-1">Wat voor woning heb je?</h2>
        <fieldset class="hc-fs"><legend class="hc-sr">Woningtype</legend>
          <div class="hc-types">{_type_keuzes()}</div>
        </fieldset>
        <fieldset class="hc-fs"><legend class="hc-legend">Wanneer is je woning gebouwd? <span class="hint">— helpt bij het inschatten</span></legend>
          <div class="hc-chips">{_periode_keuzes()}</div>
        </fieldset>
        <p class="hc-periodetip" hidden></p>
        <p class="hc-fout" role="alert"></p>
        <div class="hc-knoppen"><button type="button" class="btn btn-primary" data-volgende>Volgende: buiten</button></div>
      </section>

      <section class="hc-stap" data-stap="1" aria-labelledby="hc-k1" hidden>
        <h2 id="hc-k1" tabindex="-1">Wat moet er buiten gebeuren?</h2>
        <p class="hc-intro">Vink aan wat je wilt laten schilderen. We vullen een gangbaar aantal in voor jouw woningtype; pas het gerust aan.</p>
        <div class="hc-opts">{buiten}</div>
        <div class="hc-knoppen"><button type="button" class="btn btn-ghost" data-terug>Terug</button><button type="button" class="btn btn-primary" data-volgende>Volgende: binnen</button></div>
      </section>

      <section class="hc-stap" data-stap="2" aria-labelledby="hc-k2" hidden>
        <h2 id="hc-k2" tabindex="-1">En binnen?</h2>
        <p class="hc-intro">Alleen buiten? Ga dan gewoon door naar de volgende stap.</p>
        <div class="hc-opts">{binnen}</div>
        <div class="hc-knoppen"><button type="button" class="btn btn-ghost" data-terug>Terug</button><button type="button" class="btn btn-primary" data-volgende>Volgende: plaats</button></div>
      </section>

      <section class="hc-stap" data-stap="3" aria-labelledby="hc-k3" hidden>
        <h2 id="hc-k3" tabindex="-1">Waar woon je?</h2>
        <p class="hc-intro">Schilders rekenen niet overal hetzelfde. We passen de prijzen aan op de regio.</p>
        <div class="field">
          <label for="hc-plaats">Plaats</label>
          <select id="hc-plaats">{plaats_opts}</select>
        </div>
        <p class="hc-regio" aria-live="polite"></p>
        <div class="hc-knoppen"><button type="button" class="btn btn-ghost" data-terug>Terug</button><button type="button" class="btn btn-primary" data-volgende>Bekijk de uitkomst</button></div>
      </section>

      <section class="hc-stap" data-stap="4" aria-labelledby="hc-k4" hidden>
        <h2 id="hc-k4" tabindex="-1">Dit kost het ongeveer</h2>
        <div class="hc-uitkomst">
          <p class="hc-uit-label" data-uit-label></p>
          <p class="hc-uit-totaal"><span data-tel="van">€0</span> <span class="hc-tot-streep">–</span> <span data-tel="tot">€0</span></p>
          <p class="hc-uit-sub">inclusief materiaal en btw</p>
        </div>
        <ul class="hc-lijst" data-lijst></ul>
        <p class="hc-leeg" data-leeg hidden>Je hebt nog niets gekozen. <button type="button" class="btn-link" data-ga-naar="1">Kies wat er moet gebeuren</button></p>
        <div class="hc-noten" data-noten></div>
        <div class="hc-cta">
          <button type="button" class="btn btn-primary btn-lg" data-naar-offerte>Vraag offertes aan voor deze klus</button>
          <p class="hc-cta-sub">Gratis en vrijblijvend. We vullen je keuzes alvast in het formulier in.</p>
        </div>
        <div class="hc-acties">
          <button type="button" class="btn btn-ghost" data-delen>Bewaar of deel je berekening</button>
          <button type="button" class="btn-link" data-opnieuw>Opnieuw beginnen</button>
          <span class="hc-gedeeld" role="status"></span>
        </div>
      </section>

    </div>

    <aside class="hc-zij" aria-label="Je berekening tot nu toe">
      <div class="hc-zij-kaart">
        {_huis_svg()}
        <p class="hc-zij-label">Indicatie tot nu toe</p>
        <p class="hc-zij-totaal"><span data-tel="van">€0</span> – <span data-tel="tot">€0</span></p>
        <p class="hc-zij-sub" data-zij-sub>Kies je woning om te beginnen</p>
        <ul class="hc-zij-lijst" data-zij-lijst></ul>
      </div>
    </aside>
  </div>

  <div class="hc-balk" aria-hidden="true">
    <div><span class="hc-balk-label">Indicatie</span><strong><span data-tel="van">€0</span> – <span data-tel="tot">€0</span></strong></div>
    <button type="button" class="btn btn-primary" data-balk tabindex="-1">Uitkomst</button>
  </div>
  <p class="hc-sr" aria-live="polite" data-live></p>
  <noscript><p class="hc-noscript">Deze calculator werkt met JavaScript. Zonder JavaScript vind je alle richtprijzen op <a href="/kosten/huis-schilderen/">wat kost een huis schilderen</a>.</p></noscript>
</div>
<script type="application/json" id="hc-data">{_data_json()}</script>"""


# ---------------------------------------------------------------------------
# Pagina
# ---------------------------------------------------------------------------

def _uitleg_tabel():
    rijen = ""
    for o in onderdelen():
        if not o["prijs"]:
            continue
        if o.get("varianten"):
            for v in o["varianten"]:
                rijen += f'<tr><td>{o["naam"]}: {v["naam"].lower()}</td><td class="num">{eur(v["prijs"][0])} – {eur(v["prijs"][1])} per {o["een"]}</td></tr>'
        else:
            rijen += f'<tr><td>{o["naam"]}</td><td class="num">{eur(o["prijs"][0])} – {eur(o["prijs"][1])} per {o["een"]}</td></tr>'
    regio = "".join(
        f'<tr><td>{prov}</td><td class="num">{"+" if i > 1 else ("−" if i < 1 else "±")}{abs(round((i - 1) * 100))}%</td></tr>'
        for prov, i in sorted(PRIJSINDEX.items(), key=lambda x: x[1]))
    return rijen, regio


FAQ = [
    ("Hoe nauwkeurig is de huiscalculator?",
     "De calculator geeft een bandbreedte, geen offerte. Hij rekent met dezelfde richtprijzen als onze kostenpagina's en past die aan op je regio. De echte prijs hangt af van de staat van het schilderwerk, houtrot en de bereikbaarheid. Daarom zie je altijd een van-totbedrag."),
    ("Waarom staat er geen prijs bij de boeidelen?",
     "Schilders rekenen boeidelen en windveren bijna altijd mee in de prijs voor het houtwerk buiten. Een losse richtprijs per meter hebben we niet, dus die verzinnen we ook niet. Kies je ze aan, dan staan ze wel in je aanvraag, zodat de schilder ze meeneemt."),
    ("Zit de btw in de bedragen?",
     "Ja. De bedragen zijn inclusief materiaal en 9% btw. Is je woning jonger dan twee jaar, dan geldt 21% btw; kies dan bij de bouwperiode 'jonger dan 2 jaar' en de calculator rekent het om."),
    ("Waarom verschilt de prijs per plaats?",
     "Schilders in Noord-Holland en Utrecht rekenen meer dan in Flevoland en Overijssel, vooral door hogere loon- en bedrijfskosten. De calculator corrigeert daarvoor per provincie."),
    ("Wat doe ik met de uitkomst?",
     "Gebruik hem als ijkpunt. Vraag daarna offertes aan en leg die per onderdeel naast de uitkomst. Met de knop onder de uitkomst zet je je keuzes meteen in het aanvraagformulier."),
]


def build_huiscalculator(write, out):
    """Schrijft /kosten/calculator/ en de eigen CSS en JS naar site/assets/."""
    for pad, inhoud in (("css/huiscalculator.css", HC_CSS), ("js/huiscalculator.js", HC_JS)):
        full = os.path.join(out, "assets", pad)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as f:
            f.write(inhoud)

    cr, cr_ld = crumbs([("Home", "/"), ("Kosten", "/kosten/"), ("Calculator", None)])
    faq_html, faq_ld = faq_blok(FAQ, "Veelgestelde vragen over de huiscalculator")
    rijen, regio = _uitleg_tabel()
    app_ld = {
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": "Huiscalculator schilderwerk",
        "url": "https://topschilder.nl" + PAD,
        "applicationCategory": "UtilitiesApplication",
        "operatingSystem": "Alle",
        "inLanguage": "nl-NL",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"},
    }

    body = f"""<link rel="stylesheet" href="/assets/css/huiscalculator.css">
{cr}
<section class="hc-kop tool-hero">
  <div class="wrap">
    <span class="badge">Gratis tool · huiscalculator</span>
    <h1>Wat kost het schilderen van je hele huis?</h1>
    <p class="lead">Kies je woning, wat er buiten en binnen moet gebeuren en waar je woont. Je ziet meteen wat het per onderdeel kost, en wat het totaal wordt in jouw regio.</p>
  </div>
</section>
<section class="hc-sectie">
  <div class="wrap">{huiscalculator_html()}</div>
</section>

<section class="section soft" id="offerte-sectie">
  <div class="wrap">
    <div class="hc-offerte">
      <div class="prose">
        <h2>Van indicatie naar echte prijs</h2>
        <p>Een calculator weet niet hoe jouw kozijnen erbij staan. Een schilder wel. Vraag gratis offertes aan bij maximaal drie schilders uit jouw regio en leg ze per onderdeel naast deze uitkomst.</p>
        <ul class="checklist">
          <li>Je keuzes uit de calculator staan al in het formulier</li>
          <li>Maximaal drie schilders nemen contact op</li>
          <li>Je zit nergens aan vast en betaalt niets</li>
        </ul>
        <p>Heb je al een offerte? <a href="/offerte-vergelijken/">Laat hem checken</a>.</p>
      </div>
      <div>{offerte_form("Vraag offertes aan voor je huis", "Gratis · vrijblijvend · maximaal 3 schilders")}</div>
    </div>
  </div>
</section>

<section class="section"><div class="wrap narrow prose">
  <h2>Zo rekent de calculator</h2>
  <p>Per onderdeel vermenigvuldigen we het aantal met de richtprijs die schilders in Nederland rekenen. Dat zijn dezelfde prijzen als op onze <a href="/kosten/">kostenpagina's</a>, inclusief materiaal en 9% btw. Daarna corrigeren we voor je regio.</p>
  <div class="tablewrap"><table>
    <thead><tr><th>Onderdeel</th><th>Richtprijs</th></tr></thead>
    <tbody>{rijen}</tbody>
  </table></div>
  <h3>Regiocorrectie per provincie</h3>
  <div class="tablewrap"><table>
    <thead><tr><th>Provincie</th><th>Ten opzichte van het gemiddelde</th></tr></thead>
    <tbody>{regio}</tbody>
  </table></div>
  <h2>Waarom een range en geen vast bedrag?</h2>
  <p>Twee woningen van hetzelfde type kunnen heel anders uitvallen. Afbladderende verf, houtrot of een steiger aan de straatkant maken een groot verschil. De onderkant van de range geldt voor schilderwerk in goede staat dat makkelijk bereikbaar is. De bovenkant voor veel voorwerk of lastig werk op hoogte.</p>
  <p>Meer over de prijs van een complete woning lees je op <a href="/kosten/huis-schilderen/">wat kost een huis schilderen</a>. Alle prijzen per type werk staan op <a href="/prijzen/">wat kost een schilder</a>.</p>
</div></section>
{faq_html}"""

    write(PAD, page(
        title("Kostencalculator: wat kost je huis schilderen?"),
        "Bereken in vier stappen wat het schilderen van je hele huis kost: kozijnen, deuren, dakkapel, muren en trap, met de prijzen in jouw regio. Gratis.",
        PAD, body, [cr_ld, faq_ld, app_ld], body_attrs='class="hc-pagina"')
        .replace("</body>", '<script src="/assets/js/huiscalculator.js" defer></script></body>'),
        prio=0.8)


def calculator_teaser(stijl=""):
    """Kleine verwijzing naar de huiscalculator, voor de home, /kosten/ en /prijzen/."""
    return f"""<a class="hc-teaser" href="{PAD}"{f' style="{stijl}"' if stijl else ''}>
  <span class="hc-teaser-icoon" aria-hidden="true"><svg viewBox="0 0 48 48"><path d="M6 24 24 9l18 15"/><path d="M10 21v21h28V21"/><path d="M21 42v-9h6v9M14 27h5v5h-5zM29 27h5v5h-5z"/></svg></span>
  <span class="hc-teaser-tekst"><strong>Nieuw: de huiscalculator</strong><span>Reken in vier stappen uit wat het schilderen van je hele huis kost, binnen en buiten, met de prijzen in jouw regio.</span></span>
  <span class="hc-teaser-pijl" aria-hidden="true">→</span>
</a>"""


# De teaser staat op pagina's zonder huiscalculator.css; daarom inline-stijl in deze blokjes.
TEASER_CSS = """<style>
.hc-teaser{display:flex;align-items:center;gap:16px;padding:18px 20px;border-radius:14px;background:linear-gradient(120deg,#fff4e6,#fff);border:1.5px solid #f8c48a;color:var(--ink);text-decoration:none;transition:transform .15s,box-shadow .15s}
.hc-teaser:hover{text-decoration:none;transform:translateY(-2px);box-shadow:var(--shadow)}
.hc-teaser-icoon{flex:0 0 52px;height:52px;border-radius:12px;background:var(--accent);display:grid;place-items:center}
.hc-teaser-icoon svg{width:32px;height:32px;fill:none;stroke:#fff;stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round}
.hc-teaser-tekst{display:flex;flex-direction:column;gap:2px;min-width:0}
.hc-teaser-tekst strong{font-size:1.05rem}
.hc-teaser-tekst span{font-size:.93rem;color:var(--body);line-height:1.45}
.hc-teaser-pijl{margin-left:auto;font-size:1.4rem;color:var(--accent-dark);font-weight:700}
@media(max-width:480px){.hc-teaser{align-items:flex-start}.hc-teaser-pijl{display:none}}
</style>"""


def teaser_blok(stijl=""):
    return TEASER_CSS + calculator_teaser(stijl)


# ---------------------------------------------------------------------------
# CSS
# ---------------------------------------------------------------------------

HC_CSS = r'''/* Huiscalculator — alleen op /kosten/calculator/ */
.hc-kop{padding:34px 0 8px}
.hc-kop h1{max-width:20ch}
.hc-kop .lead{max-width:62ch}
.hc-sectie{padding:12px 0 56px}
.hc-sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.hc{position:relative}

/* stappenbalk */
.hc-nav{list-style:none;margin:0 0 22px;padding:0;display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:8px;counter-reset:none}
.hc-nav li{margin:0}
.hc-nav button{width:100%;display:flex;align-items:center;gap:9px;background:#fff;border:1.5px solid var(--line);border-radius:12px;padding:10px 12px;font:inherit;font-size:.92rem;font-weight:650;color:var(--muted);cursor:pointer;position:relative;overflow:hidden;transition:border-color .2s,color .2s,background .2s}
.hc-nav button:disabled{cursor:default;opacity:.7}
.hc-nav button:not(:disabled):hover{border-color:var(--navy-500)}
.hc-nav .hc-nr{flex:0 0 auto;width:26px;height:26px;border-radius:50%;display:grid;place-items:center;background:var(--bg-soft);color:var(--muted);font-size:.85rem;font-weight:750;transition:background .25s,color .25s}
.hc-nav button.is-klaar .hc-nr{background:var(--green);color:#fff}
.hc-nav button[aria-current=step]{border-color:var(--accent);color:var(--ink);background:var(--accent-soft)}
.hc-nav button[aria-current=step] .hc-nr{background:var(--accent);color:#fff}
@media(max-width:640px){
  .hc-nav{gap:5px}
  .hc-nav button{flex-direction:column;gap:4px;padding:8px 2px;font-size:.72rem}
  .hc-nav .hc-nav-tekst{white-space:nowrap}
}

.hc-grid{display:grid;grid-template-columns:minmax(0,1fr) 340px;gap:28px;align-items:start}
@media(max-width:900px){.hc-grid{grid-template-columns:minmax(0,1fr)}.hc-zij{display:none}}

.hc-stap{background:#fff;border:1px solid var(--line);border-top:4px solid var(--accent);border-radius:var(--radius-lg);box-shadow:var(--shadow);padding:28px}
.hc-stap[hidden]{display:none}
.hc-stap.is-actief{animation:hcIn .35s ease}
@keyframes hcIn{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
.hc-stap h2{font-size:clamp(1.3rem,2.4vw,1.7rem);outline:none}
.hc-intro{color:var(--muted);margin-bottom:18px}
@media(max-width:560px){.hc-stap{padding:20px 16px}}

.hc-fs{border:0;padding:0;margin:0 0 20px;min-width:0}
.hc-legend{font-weight:700;color:var(--ink);font-size:1rem;margin-bottom:10px;padding:0}

/* woningtypes */
.hc-types{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:10px}
@media(max-width:760px){.hc-types{grid-template-columns:repeat(3,minmax(0,1fr))}}
@media(max-width:420px){.hc-types{grid-template-columns:repeat(2,minmax(0,1fr))}}
.hc-type{display:block;margin:0;cursor:pointer;position:relative}
.hc-type input,.hc-chip input,.hc-opt-kop input{position:absolute;opacity:0;width:1px;height:1px}
.hc-type-kaart{display:flex;flex-direction:column;align-items:center;gap:8px;text-align:center;border:1.5px solid var(--line);border-radius:14px;padding:16px 8px 12px;font-weight:650;font-size:.9rem;color:var(--ink);line-height:1.25;background:#fff;transition:border-color .15s,background .15s,transform .15s,box-shadow .15s;min-height:100%}
.hc-type-kaart svg{width:46px;height:46px;fill:none;stroke:var(--navy-500);stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round;transition:stroke .2s,transform .3s}
.hc-type:hover .hc-type-kaart{border-color:var(--navy-500)}
.hc-type input:checked+.hc-type-kaart{border-color:var(--accent);background:var(--accent-soft);box-shadow:0 0 0 3px rgba(244,130,11,.14)}
.hc-type input:checked+.hc-type-kaart svg{stroke:var(--accent-dark);transform:scale(1.08)}
.hc-type input:focus-visible+.hc-type-kaart,.hc-chip input:focus-visible+span,.hc-opt-kop input:focus-visible~.hc-vink{outline:3px solid var(--accent);outline-offset:2px}

/* chips */
.hc-chips,.hc-var{display:flex;flex-wrap:wrap;gap:8px}
.hc-chip{display:inline-block;margin:0;cursor:pointer;position:relative;font-weight:600}
.hc-chip span{display:inline-block;border:1.5px solid var(--line);border-radius:99px;padding:8px 15px;font-size:.92rem;color:var(--ink);background:#fff;transition:all .15s}
.hc-chip small{color:var(--muted);font-weight:500;margin-left:2px}
.hc-chip:hover span{border-color:var(--navy-500)}
.hc-chip input:checked+span{border-color:var(--accent);background:var(--accent-soft)}
.hc-chip-sm span{padding:6px 12px;font-size:.85rem}
.hc-periodetip{background:var(--bg-soft);border-left:3px solid var(--accent);border-radius:8px;padding:10px 14px;font-size:.93rem;margin:0 0 14px}
.hc-fout{color:#c0392b;font-size:.92rem;min-height:1.2em;margin:0}

/* onderdelen */
.hc-opts{display:grid;gap:10px}
.hc-opt{border:1.5px solid var(--line);border-radius:14px;background:#fff;transition:border-color .2s,background .2s,box-shadow .2s}
.hc-opt.is-aan{border-color:var(--accent);background:linear-gradient(180deg,var(--accent-soft),#fff 70%);box-shadow:0 2px 10px rgba(244,130,11,.10)}
.hc-opt-kop{display:flex;align-items:center;gap:14px;padding:14px 16px;margin:0;cursor:pointer;position:relative}
.hc-vink{flex:0 0 26px;height:26px;border-radius:8px;border:2px solid #cfc3ae;display:grid;place-items:center;color:transparent;background:#fff;transition:all .18s}
.hc-vink svg{width:14px;height:14px}
.hc-opt.is-aan .hc-vink{background:var(--accent);border-color:var(--accent);color:#fff;transform:scale(1.06)}
.hc-opt-tekst{display:flex;flex-direction:column;min-width:0}
.hc-opt-tekst strong{color:var(--ink);font-size:1rem}
.hc-opt-tekst small{color:var(--muted);font-weight:500;font-size:.86rem}
.hc-aantal{padding:0 16px 6px 56px;display:grid;gap:10px}
.hc-aantal[hidden]{display:none}
.hc-stepper{display:flex;align-items:center;gap:8px;flex-wrap:wrap}
.hc-stepper button{width:40px;height:40px;border-radius:10px;border:1.5px solid var(--line);background:#fff;font-size:1.3rem;font-weight:700;color:var(--ink);cursor:pointer;line-height:1;display:grid;place-items:center}
.hc-stepper button:hover{border-color:var(--accent);color:var(--accent-dark)}
.hc-stepper input[type=number]{width:76px;text-align:center;padding:8px 6px;font-weight:700;-moz-appearance:textfield}
.hc-stepper input::-webkit-outer-spin-button,.hc-stepper input::-webkit-inner-spin-button{-webkit-appearance:none;margin:0}
.hc-eenheid{color:var(--muted);font-size:.92rem;min-width:4.5em}
.hc-regel{margin-left:auto;font-weight:750;color:var(--navy);font-variant-numeric:tabular-nums;white-space:nowrap}
.hc-schuif{width:100%;accent-color:var(--accent)}
.hc-tip{margin:0;padding:0 16px 14px 56px;font-size:.86rem;color:var(--muted);line-height:1.5}
@media(max-width:560px){
  .hc-aantal,.hc-tip{padding-left:16px}
  .hc-regel{margin-left:0;width:100%}
}

.hc-knoppen{display:flex;gap:10px;margin-top:22px}
.hc-knoppen .btn{flex:1}
.hc-knoppen .btn-ghost{flex:0 0 auto}
.hc-regio{font-size:.95rem;min-height:1.4em}
.hc-regio strong{color:var(--ink)}

/* uitkomst */
.hc-uitkomst{background:linear-gradient(150deg,var(--navy) 0%,#241906 70%,#5c431a 100%);color:#e9dcc6;border-radius:16px;padding:24px;text-align:center;margin-bottom:18px;position:relative;overflow:hidden}
.hc-uitkomst::after{content:"";position:absolute;inset:auto -40px -60px auto;width:180px;height:180px;border-radius:50%;background:radial-gradient(circle,rgba(244,130,11,.35),transparent 70%)}
.hc-uit-label{margin:0 0 4px;font-size:.95rem}
.hc-uit-totaal{margin:0;font-size:clamp(1.9rem,6vw,2.9rem);font-weight:800;color:#fff;letter-spacing:-.02em;font-variant-numeric:tabular-nums;line-height:1.15}
.hc-tot-streep{color:#ffb766}
.hc-uit-sub{margin:4px 0 0;font-size:.88rem;color:#cdbb9c}
.hc-lijst{list-style:none;margin:0 0 16px;padding:0;display:grid;gap:12px}
.hc-lijst li{margin:0;animation:hcRegel .45s ease both}
.hc-lijst .hc-groep{display:flex;justify-content:space-between;gap:12px;margin-top:6px;padding-bottom:6px;border-bottom:2px solid var(--line);font-weight:800;color:var(--ink);text-transform:uppercase;letter-spacing:.04em;font-size:.82rem}
.hc-lijst .hc-groep:first-child{margin-top:0}
@keyframes hcRegel{from{opacity:0;transform:translateX(-12px)}to{opacity:1;transform:none}}
.hc-lijst-kop{display:flex;justify-content:space-between;gap:12px;font-size:.95rem}
.hc-lijst-kop span:first-child{color:var(--ink);font-weight:650}
.hc-lijst-kop small{display:block;color:var(--muted);font-weight:500}
.hc-lijst-kop span:last-child{font-weight:750;color:var(--navy);white-space:nowrap;font-variant-numeric:tabular-nums}
.hc-staaf{height:10px;border-radius:99px;background:var(--bg-soft);margin-top:6px;position:relative;overflow:hidden}
.hc-staaf i{position:absolute;top:0;bottom:0;border-radius:99px;background:linear-gradient(90deg,#ffc784,var(--accent));transition:left .7s cubic-bezier(.2,.8,.2,1),width .7s cubic-bezier(.2,.8,.2,1)}
.hc-lijst .hc-info span:last-child{color:var(--muted);font-weight:600}
.hc-noten{display:grid;gap:10px;margin-bottom:20px}
.hc-noot{background:var(--bg-soft);border-radius:10px;padding:12px 14px;font-size:.92rem;margin:0}
.hc-noot strong{color:var(--ink)}
.hc-cta{text-align:center;margin:8px 0 14px}
.hc-cta .btn{width:100%;max-width:440px}
.hc-cta-sub{font-size:.88rem;color:var(--muted);margin:8px 0 0}
.hc-acties{display:flex;flex-wrap:wrap;gap:10px 18px;align-items:center;justify-content:center;border-top:1px solid var(--line);padding-top:16px}
.hc-gedeeld{font-size:.88rem;color:var(--green);font-weight:650}
.hc-leeg{background:var(--bg-soft);border-radius:10px;padding:14px;text-align:center}

/* zijkolom */
.hc-zij{position:sticky;top:92px}
.hc-zij-kaart{background:#fff;border:1px solid var(--line);border-radius:var(--radius-lg);box-shadow:var(--shadow-lg);padding:20px;text-align:center}
.hc-zij-label{margin:6px 0 0;font-size:.85rem;color:var(--muted);text-transform:uppercase;letter-spacing:.05em;font-weight:700}
.hc-zij-totaal{margin:0;font-size:1.7rem;font-weight:800;color:var(--ink);font-variant-numeric:tabular-nums;letter-spacing:-.02em}
.hc-zij-totaal.is-pop{animation:hcPop .45s ease}
@keyframes hcPop{40%{transform:scale(1.06);color:var(--accent-dark)}}
.hc-zij-sub{font-size:.88rem;color:var(--muted);margin:0 0 10px}
.hc-zij-lijst{list-style:none;margin:0;padding:10px 0 0;border-top:1px solid var(--line);text-align:left;font-size:.88rem;display:grid;gap:6px}
.hc-zij-lijst:empty{display:none}
.hc-zij-lijst li{display:flex;justify-content:space-between;gap:10px;margin:0;animation:hcRegel .35s ease both}
.hc-zij-lijst li span:last-child{font-weight:700;color:var(--navy);white-space:nowrap;font-variant-numeric:tabular-nums}

/* huisje */
.hc-huis{width:100%;max-width:260px;height:auto;margin:0 auto;display:block;overflow:visible}
.hc-huis *{transition:fill .45s ease,stroke .45s ease,opacity .45s ease,transform .45s cubic-bezier(.3,1.4,.5,1)}
.hc-buur path,.hc-buur rect{fill:#f1ece3;stroke:#ddd3c2;stroke-width:1.5}
.hc-buur{opacity:0}
.hc-huis.b-l .hc-buur-l,.hc-huis.b-r .hc-buur-r{opacity:1}
.hc-muur{fill:#fffaf2;stroke:var(--navy-500);stroke-width:2}
.hc-dak{fill:#e3d6c1;stroke:var(--navy-500);stroke-width:2;stroke-linejoin:round}
.hc-p-boeidelen{fill:none;stroke:#cdbfa8;stroke-width:5;stroke-linecap:round;stroke-linejoin:round}
.hc-huis.on-boeidelen .hc-p-boeidelen{stroke:var(--accent)}
.hc-p-dakkapel{transform-origin:120px 78px;transform:scale(0);opacity:0}
.hc-p-dakkapel rect:first-child{fill:#fffaf2;stroke:var(--navy-500);stroke-width:2}
.hc-p-dakkapel path{stroke:var(--navy-500);stroke-width:3;stroke-linecap:round}
.hc-huis.on-dakkapel .hc-p-dakkapel{transform:scale(1);opacity:1}
.hc-huis.on-dakkapel .hc-p-dakkapel rect:first-child,.hc-huis.on-dakkapel .hc-p-dakkapel path{stroke:var(--accent-dark)}
.hc-raam{fill:#dbe7ef;stroke:#9a8a70;stroke-width:3}
.hc-huis.on-kozijnen .hc-p-kozijnen{stroke:var(--accent)}
.hc-huis.on-binnen .hc-raam{fill:#ffe2b8}
.hc-p-buitendeuren{fill:#cdbfa8;stroke:#9a8a70;stroke-width:2}
.hc-huis.on-buitendeuren .hc-p-buitendeuren{fill:var(--accent);stroke:var(--accent-dark)}
.hc-p-steiger{fill:none;stroke:#b7a98f;stroke-width:2.5;stroke-linecap:round;opacity:0;transform:translateX(12px)}
.hc-huis.on-steiger .hc-p-steiger{opacity:1;transform:none;stroke:var(--accent-dark)}
.hc-grond{stroke:#cdbfa8;stroke-width:2}
.hc-flat{opacity:0}
.hc-huis.t-appartement .hc-flat{opacity:1}
.hc-huis.t-appartement .hc-woning{opacity:0}
.hc-muur-flat{fill:#f6f0e6;stroke:var(--navy-500);stroke-width:2}
.hc-flat-ramen rect{fill:#e6edf1;stroke:#b9ad98;stroke-width:2}
.hc-unit{fill:#fffaf2;stroke:var(--accent);stroke-width:2.5;stroke-dasharray:5 4}
@media(prefers-reduced-motion:reduce){.hc-huis *,.hc-staaf i{transition:none}.hc-stap.is-actief,.hc-lijst li,.hc-zij-lijst li,.hc-zij-totaal.is-pop{animation:none}}

/* mobiele balk */
.hc-pagina .sticky-cta{display:none}
.hc-balk{display:none}
@media(max-width:900px){
  .hc-balk{display:flex;position:fixed;left:0;right:0;bottom:0;z-index:70;align-items:center;justify-content:space-between;gap:12px;padding:10px 16px;background:rgba(255,255,255,.97);border-top:1px solid var(--line);box-shadow:0 -4px 20px rgba(60,41,15,.10);transform:translateY(110%);transition:transform .3s ease}
  .hc-balk.is-zichtbaar{transform:none}
  .hc-balk div{display:flex;flex-direction:column;line-height:1.2;min-width:0}
  .hc-balk-label{font-size:.75rem;color:var(--muted);text-transform:uppercase;letter-spacing:.05em;font-weight:700}
  .hc-balk strong{font-size:1.15rem;color:var(--ink);font-variant-numeric:tabular-nums;white-space:nowrap}
  .hc-balk .btn{padding:11px 18px}
  .hc-pagina{padding-bottom:76px}
}

/* offerteblok onder de calculator */
.hc-offerte{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,460px);gap:44px;align-items:start}
@media(max-width:900px){.hc-offerte{grid-template-columns:minmax(0,1fr);gap:24px}}
.hc-offerte .formcard.is-voorgevuld{box-shadow:0 0 0 3px var(--accent),var(--shadow-lg);transition:box-shadow .4s}
.hc-noscript{background:var(--accent-soft);padding:14px;border-radius:10px}
'''


# ---------------------------------------------------------------------------
# JS
# ---------------------------------------------------------------------------

HC_JS = r'''/* Huiscalculator — vanilla JS, geen afhankelijkheden. */
(function () {
  "use strict";
  var root = document.querySelector("[data-hc]");
  var bron = document.getElementById("hc-data");
  if (!root || !bron) return;
  var D = JSON.parse(bron.textContent);
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  var ONDERDELEN = {};
  D.onderdelen.forEach(function (o) { ONDERDELEN[o.key] = o; });
  var TYPES = {}; D.types.forEach(function (t) { TYPES[t.key] = t; });
  var PERIODES = {}; D.periodes.forEach(function (p) { PERIODES[p.key] = p; });
  var PLAATSEN = {}; D.plaatsen.forEach(function (p) { PLAATSEN[p.slug] = p; });

  var state = { type: "", periode: "", plaats: "", items: {} };  // items[key] = {n, v}
  var stap = 0, bezocht = 0;

  var stappen = [].slice.call(root.querySelectorAll(".hc-stap"));
  var navKnoppen = [].slice.call(root.querySelectorAll(".hc-nav button"));
  var huis = root.querySelector(".hc-huis");
  var balk = root.querySelector(".hc-balk");

  /* ---------------------------------------------------------- rekenen */
  function euro(n) { return "€" + Math.round(n).toLocaleString("nl-NL"); }
  function rond(n, op) { return Math.round(n / op) * op; }
  function factor() {
    var f = 1;
    var p = PLAATSEN[state.plaats];
    if (p) f *= p.index;
    if (state.periode === "nieuwbouw") f *= D.btwNieuwbouw;
    return f;
  }
  function prijsVan(o, it) {
    if (o.varianten) {
      var v = o.varianten.filter(function (x) { return x.key === it.v; })[0] || o.varianten[0];
      return v.prijs;
    }
    return o.prijs;
  }
  function regels() {
    var f = factor(), uit = [];
    D.onderdelen.forEach(function (o) {
      var it = state.items[o.key];
      if (!it) return;
      if (!o.prijs) { uit.push({ o: o, info: true }); return; }
      var p = prijsVan(o, it);
      uit.push({ o: o, n: it.n, it: it, van: rond(p[0] * it.n * f, 5), tot: rond(p[1] * it.n * f, 5) });
    });
    return uit;
  }
  function totaal(rs) {
    var van = 0, tot = 0;
    rs.forEach(function (r) { if (!r.info) { van += r.van; tot += r.tot; } });
    return { van: rond(van, 10), tot: rond(tot, 10) };
  }
  function omschrijf(r) {
    var o = r.o;
    if (r.info) return o.naam;
    var naam = o.naam;
    if (o.varianten) {
      var v = o.varianten.filter(function (x) { return x.key === r.it.v; })[0];
      if (v) naam += " (" + v.naam.toLowerCase() + ")";
    }
    return naam;
  }
  function aantalTekst(r) {
    if (r.info) return "";
    return r.n + " " + (r.n === 1 ? r.o.een : r.o.mv);
  }

  /* ---------------------------------------------------- optel-animatie */
  function tel(el, naar) {
    var van = parseFloat(el.dataset.waarde || "0");
    el.dataset.waarde = naar;
    if (reduce || van === naar) { el.textContent = euro(naar); return; }
    var start = null, duur = 650;
    if (el._raf) cancelAnimationFrame(el._raf);
    clearTimeout(el._fin);
    // vangnet: zonder animatieframes (achtergrondtab) toch het eindbedrag tonen
    el._fin = setTimeout(function () { cancelAnimationFrame(el._raf); el.textContent = euro(naar); }, duur + 150);
    function frame(t) {
      if (!start) start = t;
      var x = Math.min(1, (t - start) / duur);
      var e = 1 - Math.pow(1 - x, 3);
      el.textContent = euro(rond(van + (naar - van) * e, 5));
      if (x < 1) el._raf = requestAnimationFrame(frame);
    }
    el._raf = requestAnimationFrame(frame);
  }

  /* ------------------------------------------------------- weergeven */
  var liveTimer = null, vorigTotaal = -1;
  function render() {
    var rs = regels(), t = totaal(rs);

    root.querySelectorAll('[data-tel="van"]').forEach(function (el) { tel(el, t.van); });
    root.querySelectorAll('[data-tel="tot"]').forEach(function (el) { tel(el, t.tot); });
    if (t.tot !== vorigTotaal && vorigTotaal >= 0) {
      var z = root.querySelector(".hc-zij-totaal");
      if (z) { z.classList.remove("is-pop"); void z.offsetWidth; z.classList.add("is-pop"); }
    }
    vorigTotaal = t.tot;

    // regelprijs bij elk aangevinkt onderdeel
    rs.forEach(function (r) {
      if (r.info) return;
      var out = root.querySelector('.hc-opt[data-key="' + r.o.key + '"] .hc-regel');
      if (out) out.textContent = euro(r.van) + " – " + euro(r.tot);
    });

    // zijkolom
    var zij = root.querySelector("[data-zij-lijst]");
    zij.innerHTML = "";
    rs.forEach(function (r) {
      var li = document.createElement("li");
      li.innerHTML = "<span></span><span></span>";
      li.firstChild.textContent = omschrijf(r) + (r.info ? "" : " · " + aantalTekst(r));
      li.lastChild.textContent = r.info ? "in offerte" : euro(r.van) + " – " + euro(r.tot);
      zij.appendChild(li);
    });
    var sub = root.querySelector("[data-zij-sub]");
    var type = TYPES[state.type];
    if (!type) sub.textContent = "Kies je woning om te beginnen";
    else {
      var bits = [type.naam];
      if (PLAATSEN[state.plaats]) bits.push(PLAATSEN[state.plaats].naam);
      var n = rs.length;
      bits.push(n === 0 ? "nog niets gekozen" : n + (n === 1 ? " onderdeel" : " onderdelen"));
      sub.textContent = bits.join(" · ");
    }

    // huisje
    if (huis) {
      var cls = ["hc-huis"];
      if (type) {
        cls.push("t-" + type.key);
        if (type.key === "tussenwoning") cls.push("b-l", "b-r");
        if (type.key === "hoekwoning") cls.push("b-l");
        if (type.key === "twee-onder-een-kap") cls.push("b-r");
      }
      rs.forEach(function (r) {
        cls.push("on-" + r.o.key);
        if (r.o.groep === "binnen") cls.push("on-binnen");
      });
      huis.setAttribute("class", cls.join(" "));
    }

    // mobiele balk
    if (balk) balk.classList.toggle("is-zichtbaar", !!type && stap < 4 && !formInBeeld);

    // schermlezer: rustig melden
    clearTimeout(liveTimer);
    liveTimer = setTimeout(function () {
      var live = root.querySelector("[data-live]");
      if (live && type) live.textContent = "Indicatie nu " + euro(t.van) + " tot " + euro(t.tot) + ".";
    }, 900);

    if (stap === 4) renderUitkomst(rs, t);
    bewaarInUrl();
  }

  function renderUitkomst(rs, t) {
    var type = TYPES[state.type];
    var plaats = PLAATSEN[state.plaats];
    root.querySelector("[data-uit-label]").textContent =
      (type ? type.naam : "Je woning") + (plaats ? " in " + plaats.naam : "");

    var lijst = root.querySelector("[data-lijst]");
    lijst.innerHTML = "";
    var max = 1;
    rs.forEach(function (r) { if (!r.info && r.tot > max) max = r.tot; });
    var groepVan = { buiten: 0, binnen: 0 }, groepTot = { buiten: 0, binnen: 0 }, groepN = { buiten: 0, binnen: 0 };
    rs.forEach(function (r) { groepN[r.o.groep]++; if (!r.info) { groepVan[r.o.groep] += r.van; groepTot[r.o.groep] += r.tot; } });
    var vorigeGroep = "";
    rs.forEach(function (r, i) {
      if (r.o.groep !== vorigeGroep && groepN.buiten && groepN.binnen) {
        vorigeGroep = r.o.groep;
        var g = document.createElement("li");
        g.className = "hc-groep";
        g.innerHTML = "<span></span><span></span>";
        g.firstChild.textContent = r.o.groep === "buiten" ? "Buiten" : "Binnen";
        g.lastChild.textContent = euro(rond(groepVan[r.o.groep], 10)) + " – " + euro(rond(groepTot[r.o.groep], 10));
        lijst.appendChild(g);
      }
      var li = document.createElement("li");
      li.style.animationDelay = (reduce ? 0 : i * 70) + "ms";
      var kop = document.createElement("div");
      kop.className = "hc-lijst-kop" + (r.info ? " hc-info" : "");
      var a = document.createElement("span");
      a.textContent = omschrijf(r);
      if (!r.info) { var s = document.createElement("small"); s.textContent = aantalTekst(r); a.appendChild(s); }
      else { var s2 = document.createElement("small"); s2.textContent = "Geen losse richtprijs; staat wel in je aanvraag"; a.appendChild(s2); }
      var b = document.createElement("span");
      b.textContent = r.info ? "in de offerte" : euro(r.van) + " – " + euro(r.tot);
      kop.appendChild(a); kop.appendChild(b);
      li.appendChild(kop);
      if (!r.info) {
        var staaf = document.createElement("div");
        staaf.className = "hc-staaf";
        staaf.setAttribute("aria-hidden", "true");
        var bar = document.createElement("i");
        bar.style.left = "0%"; bar.style.width = "0%";
        staaf.appendChild(bar);
        li.appendChild(staaf);
        (function (bar, r) {
          setTimeout(function () {
            bar.style.left = (r.van / max * 100) + "%";
            bar.style.width = Math.max(2, (r.tot - r.van) / max * 100) + "%";
          }, 40);
        })(bar, r);
      }
      lijst.appendChild(li);
    });
    root.querySelector("[data-leeg]").hidden = rs.length > 0;
    root.querySelector(".hc-uitkomst").hidden = rs.length === 0;
    root.querySelector(".hc-cta").hidden = rs.length === 0;

    // toelichting
    var noten = [];
    if (plaats) {
      var pct = Math.round((plaats.index - 1) * 100);
      noten.push("<strong>Regio:</strong> in " + esc(plaats.prov) + " liggen de prijzen " +
        (pct === 0 ? "op het landelijk gemiddelde." : Math.abs(pct) + "% " + (pct < 0 ? "onder" : "boven") + " het landelijk gemiddelde. Dat zit al in de bedragen."));
    } else {
      noten.push("<strong>Regio:</strong> je hebt geen plaats gekozen, dus we rekenen met landelijke prijzen.");
    }
    if (state.periode === "nieuwbouw") noten.push("<strong>Btw:</strong> je woning is jonger dan twee jaar, dus we rekenen met 21% btw in plaats van 9%.");
    else noten.push("<strong>Btw:</strong> de bedragen zijn inclusief materiaal en 9% btw, het tarief voor woningen ouder dan twee jaar.");
    var buitenGekozen = rs.some(function (r) { return r.o.groep === "buiten"; });
    if (type && type.bench !== null && buitenGekozen) {
      var bb = D.benchBuiten[type.bench];
      noten.push("<strong>Ter vergelijking:</strong> voor de hele buitenkant van een " + esc(bb.label.split(",")[0].toLowerCase()) + " noemen we op onze kostenpagina " +
        euro(bb.prijs[0]) + " – " + euro(bb.prijs[1]) + " (landelijk). <a href=\"/kosten/huis-schilderen/\">Lees hoe dat is opgebouwd</a>.");
    }
    if (state.periode && PERIODES[state.periode] && state.periode !== "nieuwbouw") {
      noten.push("<strong>Bouwperiode:</strong> " + esc(PERIODES[state.periode].tip));
    }
    root.querySelector("[data-noten]").innerHTML = noten.map(function (n) { return '<p class="hc-noot">' + n + "</p>"; }).join("");
  }

  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  /* --------------------------------------------------------- stappen */
  function ga(n, focus) {
    if (n > 0 && !state.type) { foutType(); n = 0; }
    stap = Math.max(0, Math.min(4, n));
    bezocht = Math.max(bezocht, stap);
    stappen.forEach(function (s, i) {
      s.hidden = i !== stap;
      s.classList.toggle("is-actief", i === stap);
    });
    navKnoppen.forEach(function (b, i) {
      b.disabled = i > bezocht || (i > 0 && !state.type);
      if (i === stap) b.setAttribute("aria-current", "step"); else b.removeAttribute("aria-current");
      b.classList.toggle("is-klaar", i < stap || (i <= bezocht && i !== stap && i < 4));
    });
    render();
    if (focus !== false) {
      var kop = stappen[stap].querySelector("h2");
      var top = root.getBoundingClientRect().top + window.pageYOffset - 84;
      if (window.pageYOffset > top) window.scrollTo({ top: top, behavior: reduce ? "auto" : "smooth" });
      if (kop) kop.focus({ preventScroll: true });
    }
  }
  function foutType() {
    var f = root.querySelector(".hc-fout");
    if (f) f.textContent = "Kies eerst wat voor woning je hebt.";
  }

  root.addEventListener("click", function (e) {
    var b = e.target.closest("button");
    if (!b || !root.contains(b)) return;
    if (b.hasAttribute("data-volgende")) ga(stap + 1);
    else if (b.hasAttribute("data-terug")) ga(stap - 1);
    else if (b.dataset.ga !== undefined) ga(parseInt(b.dataset.ga, 10));
    else if (b.dataset.gaNaar !== undefined) ga(parseInt(b.dataset.gaNaar, 10));
    else if (b.hasAttribute("data-balk")) ga(4);
    else if (b.hasAttribute("data-naar-offerte")) naarOfferte();
    else if (b.hasAttribute("data-delen")) deel();
    else if (b.hasAttribute("data-opnieuw")) opnieuw();
    else if (b.classList.contains("hc-min") || b.classList.contains("hc-plus")) {
      var opt = b.closest(".hc-opt"), inp = opt.querySelector("input[type=number]");
      var stapG = parseFloat(inp.step) || 1;
      zetAantal(opt.dataset.key, (parseFloat(inp.value) || 0) + (b.classList.contains("hc-plus") ? stapG : -stapG));
    }
  });

  /* ------------------------------------------------------ invoervelden */
  root.querySelectorAll('input[name="hc-type"]').forEach(function (r) {
    r.addEventListener("change", function () {
      var oud = TYPES[state.type];
      state.type = r.value;
      root.querySelector(".hc-fout").textContent = "";
      // standaardaantallen meeschuiven als de bezoeker ze niet zelf heeft aangepast
      Object.keys(state.items).forEach(function (k) {
        var it = state.items[k];
        if (!it.eigen && TYPES[state.type].std[k] !== undefined) { it.n = TYPES[state.type].std[k]; syncOpt(k); }
      });
      if (!oud) navKnoppen.forEach(function (b, i) { if (i <= bezocht) b.disabled = false; });
      render();
    });
  });
  root.querySelectorAll('input[name="hc-periode"]').forEach(function (r) {
    r.addEventListener("change", function () {
      state.periode = r.value;
      var tip = root.querySelector(".hc-periodetip");
      tip.textContent = PERIODES[r.value].tip;
      tip.hidden = false;
      render();
    });
  });
  root.querySelectorAll(".hc-check").forEach(function (c) {
    c.addEventListener("change", function () {
      var k = c.value, o = ONDERDELEN[k];
      if (c.checked) {
        var std = TYPES[state.type] ? TYPES[state.type].std[k] : 1;
        state.items[k] = { n: o.prijs ? (std || o.min || 1) : 0, v: o.varianten ? o.varianten[0].key : "" };
      } else delete state.items[k];
      syncOpt(k);
      render();
    });
  });
  root.querySelectorAll(".hc-opt input[type=number]").forEach(function (inp) {
    inp.addEventListener("input", function () {
      var v = parseFloat(inp.value);
      if (!isNaN(v)) zetAantal(inp.closest(".hc-opt").dataset.key, v, true);
    });
    inp.addEventListener("blur", function () { syncOpt(inp.closest(".hc-opt").dataset.key); });
  });
  root.querySelectorAll(".hc-schuif").forEach(function (s) {
    s.addEventListener("input", function () { zetAantal(s.dataset.schuif, parseFloat(s.value)); });
  });
  root.querySelectorAll(".hc-var input").forEach(function (r) {
    r.addEventListener("change", function () {
      var k = r.closest(".hc-opt").dataset.key;
      if (state.items[k]) { state.items[k].v = r.value; render(); }
    });
  });
  var plaatsSel = root.querySelector("#hc-plaats");
  plaatsSel.addEventListener("change", function () {
    state.plaats = plaatsSel.value === "anders" ? "" : plaatsSel.value;
    var p = PLAATSEN[state.plaats], uit = root.querySelector(".hc-regio");
    if (p) {
      var pct = Math.round((p.index - 1) * 100);
      uit.innerHTML = "<strong>" + esc(p.prov) + "</strong>: " + (pct === 0 ? "prijzen op het landelijk gemiddelde." :
        "prijzen gemiddeld " + Math.abs(pct) + "% " + (pct < 0 ? "lager" : "hoger") + " dan landelijk.");
    } else if (plaatsSel.value === "anders") {
      uit.textContent = "We rekenen met landelijke prijzen.";
    } else uit.textContent = "";
    render();
  });

  function zetAantal(k, n, typen) {
    var o = ONDERDELEN[k], it = state.items[k];
    if (!o || !it) return;
    var mn = o.min || 1;
    n = Math.max(mn, Math.min(o.max, Math.round(n)));
    it.n = n; it.eigen = true;
    if (!typen) syncOpt(k);
    else { var s = root.querySelector('[data-schuif="' + k + '"]'); if (s) s.value = n; }
    render();
  }
  function syncOpt(k) {
    var opt = root.querySelector('.hc-opt[data-key="' + k + '"]');
    if (!opt) return;
    var it = state.items[k];
    opt.classList.toggle("is-aan", !!it);
    opt.querySelector(".hc-check").checked = !!it;
    var aantal = opt.querySelector(".hc-aantal");
    if (aantal) aantal.hidden = !it;
    if (!it) return;
    var inp = opt.querySelector("input[type=number]");
    if (inp) inp.value = it.n;
    var s = opt.querySelector(".hc-schuif");
    if (s) s.value = it.n;
    if (it.v) {
      var r = opt.querySelector('.hc-var input[value="' + it.v + '"]');
      if (r) r.checked = true;
    }
  }

  /* ------------------------------------------- bewaren en delen (URL) */
  var geladen = false;
  function bewaarInUrl() {
    if (!geladen || !window.history || !history.replaceState) return;
    var q = new URLSearchParams();
    if (state.type) q.set("woning", state.type);
    if (state.periode) q.set("bouw", state.periode);
    if (state.plaats) q.set("plaats", state.plaats);
    var o = Object.keys(state.items).map(function (k) {
      var it = state.items[k];
      return k + (ONDERDELEN[k].prijs ? "." + it.n : "") + (it.v ? "." + it.v : "");
    });
    if (o.length) q.set("klus", o.join(","));
    var s = q.toString();
    history.replaceState(null, "", location.pathname + (s ? "?" + s : ""));
  }
  function laadUitUrl() {
    var q = new URLSearchParams(location.search);
    var t = q.get("woning");
    if (t && TYPES[t]) {
      state.type = t;
      var r = root.querySelector('input[name="hc-type"][value="' + t + '"]'); if (r) r.checked = true;
    }
    var b = q.get("bouw");
    if (b && PERIODES[b]) {
      state.periode = b;
      var rb = root.querySelector('input[name="hc-periode"][value="' + b + '"]'); if (rb) rb.checked = true;
      var tip = root.querySelector(".hc-periodetip"); tip.textContent = PERIODES[b].tip; tip.hidden = false;
    }
    var p = q.get("plaats");
    if (p && PLAATSEN[p]) { state.plaats = p; plaatsSel.value = p; plaatsSel.dispatchEvent(new Event("change")); }
    (q.get("klus") || "").split(",").forEach(function (deel) {
      var d = deel.split("."), o = ONDERDELEN[d[0]];
      if (!o) return;
      var it = { n: 0, v: "", eigen: true };
      if (o.prijs) {
        var n = parseInt(d[1], 10);
        it.n = isNaN(n) ? 1 : Math.max(o.min || 1, Math.min(o.max, n));
        if (o.varianten) {
          var v = d[2];
          it.v = o.varianten.some(function (x) { return x.key === v; }) ? v : o.varianten[0].key;
        }
      }
      state.items[o.key] = it;
      syncOpt(o.key);
    });
    geladen = true;
    if (state.type && Object.keys(state.items).length) { bezocht = 4; ga(4, false); }
    else ga(0, false);
  }
  function deel() {
    bewaarInUrl();
    var url = location.href, meld = root.querySelector(".hc-gedeeld");
    function klaar(t) { meld.textContent = t; setTimeout(function () { meld.textContent = ""; }, 4000); }
    if (navigator.share && window.matchMedia("(max-width: 900px)").matches) {
      navigator.share({ title: "Mijn berekening schilderwerk", url: url }).catch(function () {});
    } else if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(url).then(function () { klaar("Link gekopieerd. Met deze link open je je berekening later weer."); },
        function () { klaar("Kopieer de link uit de adresbalk om je berekening te bewaren."); });
    } else klaar("Kopieer de link uit de adresbalk om je berekening te bewaren.");
  }
  function opnieuw() {
    state = { type: "", periode: "", plaats: "", items: {} };
    root.querySelectorAll('input[name="hc-type"],input[name="hc-periode"]').forEach(function (r) { r.checked = false; });
    root.querySelector(".hc-periodetip").hidden = true;
    plaatsSel.value = ""; root.querySelector(".hc-regio").textContent = "";
    Object.keys(ONDERDELEN).forEach(syncOpt);
    bezocht = 0;
    ga(0);
  }

  /* ------------------------------------- brug naar het offerteformulier */
  var formInBeeld = false;
  var formSectie = document.getElementById("offerte-sectie");
  if (formSectie && "IntersectionObserver" in window) {
    new IntersectionObserver(function (es) {
      formInBeeld = es[0].isIntersecting;
      if (balk) balk.classList.toggle("is-zichtbaar", !!state.type && stap < 4 && !formInBeeld);
    }).observe(formSectie);
  }

  function kiesRadio(form, naam, waarde) {
    var r = [].slice.call(form.querySelectorAll('input[name="' + naam + '"]')).filter(function (i) { return i.value === waarde; })[0];
    if (r) r.checked = true;
    return !!r;
  }
  function naarOfferte() {
    var form = document.querySelector("#offerte form[data-wizard]");
    var card = document.getElementById("offerte");
    if (!form || !card) { location.href = "/offerte-aanvragen/"; return; }
    var rs = regels(), t = totaal(rs);
    var buiten = rs.filter(function (r) { return r.o.groep === "buiten"; });
    var binnen = rs.filter(function (r) { return r.o.groep === "binnen"; });
    var type = TYPES[state.type], plaats = PLAATSEN[state.plaats];

    // dienst: de grootste groep bepaalt; de rest staat in de omschrijving
    var dienst = D.diensten.buitenschilderwerk;
    if (!buiten.length && binnen.length) {
      var alleenSpuit = binnen.every(function (r) {
        return r.o.key === "keuken" || (r.o.key === "binnendeuren" && r.it.v === "s");
      });
      dienst = alleenSpuit ? D.diensten.spuitwerk : D.diensten.binnenschilderwerk;
    } else if (buiten.length && buiten.every(function (r) { return r.o.key === "houtrot"; }) && !binnen.length) {
      dienst = D.diensten["houtrot-reparatie"];
    }
    kiesRadio(form, "dienst", dienst);
    if (type && type.key === "appartement") kiesRadio(form, "pandtype", "Appartement / VvE");
    var omvang = (buiten.length && binnen.length) || rs.length >= 4 ? "Groot (hele woning)"
      : rs.length >= 2 ? "Gemiddeld (meerdere ruimtes / halve woning)" : "Klein (1 ruimte / paar kozijnen)";
    kiesRadio(form, "omvang", omvang);
    var pl = form.querySelector('input[name="plaats"]');
    if (pl && plaats && (!pl.value || pl.dataset.hc)) { pl.value = plaats.naam; pl.dataset.hc = "1"; }

    function regel(r) {
      if (r.info) return r.o.naam.toLowerCase();
      if (r.o.key === "muren") return "muren en plafonds (ca. " + r.n + " m²)";
      var naam = r.o.naam.toLowerCase();
      if (r.o.varianten) {
        var v = r.o.varianten.filter(function (x) { return x.key === r.it.v; })[0];
        if (v) naam += ", " + v.naam.toLowerCase();
      }
      return naam + " (" + r.n + ")";
    }
    var tekst = "Via de huiscalculator: " + (type ? type.naam.toLowerCase() : "woning") +
      (state.periode === "nieuwbouw" ? ", jonger dan 2 jaar" : state.periode ? ", gebouwd " + PERIODES[state.periode].naam.toLowerCase() : "") + ".";
    if (buiten.length) tekst += "\nBuiten: " + buiten.map(regel).join(", ") + ".";
    if (binnen.length) tekst += "\nBinnen: " + binnen.map(regel).join(", ") + ".";
    if (rs.length) tekst += "\nIndicatie calculator: " + euro(t.van) + " – " + euro(t.tot) + ".";
    var oms = form.querySelector('textarea[name="omschrijving"]');
    if (oms && (!oms.value || oms.dataset.hc)) { oms.value = tekst; oms.dataset.hc = "1"; }

    // eerste stap (dienst) is ingevuld: door naar postcode
    var eerste = form.querySelector(".step.active");
    if (eerste && eerste === form.querySelector(".step")) {
      var volgende = eerste.querySelector("[data-next]");
      if (volgende) volgende.click();
    }
    card.classList.add("is-voorgevuld");
    setTimeout(function () { card.classList.remove("is-voorgevuld"); }, 2200);
    card.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "start" });
    var pc = form.querySelector('input[name="postcode"]');
    if (pc) setTimeout(function () { pc.focus({ preventScroll: true }); }, reduce ? 0 : 600);
  }

  laadUitUrl();
})();
'''
