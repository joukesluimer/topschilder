# -*- coding: utf-8 -*-
"""Gratis tools: één tools-sectie voor de home en de overzichtspagina /tools/.

Een tool verschijnt alleen als zijn bouwfunctie in build.py bestaat (zie `beschikbare_tools`).
Zo komen er geen dode links naar pagina's die (nog) niet gebouwd worden.
"""

from components import page, crumbs, cta_blok

# Volgorde = volgorde op de site. 'bouwer' is de naam van de bouwfunctie in build.py.
TOOLS = [
    {"slug": "calculator", "pad": "/kosten/calculator/", "bouwer": "build_huiscalculator",
     "titel": "Huiscalculator", "kort": "Wat kost het schilderen van je hele huis?",
     "tekst": "Kies je woning en wat er moet gebeuren. Je ziet per onderdeel wat het kost en het totaal voor jouw regio.",
     "knop": "Bereken je prijs", "label": "5 stappen"},
    {"slug": "kleuren", "pad": "/kleuren-kiezen/", "bouwer": "build_kleurenkiezer",
     "titel": "Kleurenkiezer", "kort": "Welke kleur krijgen jouw kozijnen?",
     "tekst": "Klik door de kleuren voor kozijnen, deur, boeidelen en gevelsteen. Deel je ontwerp of bewaar het als plaatje.",
     "knop": "Kies je kleuren", "label": "Direct zichtbaar"},
    {"slug": "onderhoud", "pad": "/onderhoudscheck/", "bouwer": "build_onderhoudscheck",
     "titel": "Onderhoudscheck", "kort": "Is jouw schilderwerk aan de beurt?",
     "tekst": "Acht korte vragen over je kozijnen, deuren en boeidelen. Je ziet hoe je ervoor staat en wat het ongeveer kost.",
     "knop": "Doe de check", "label": "2 minuten"},
    {"slug": "weer", "pad": "/schilderweer/", "bouwer": "build_schilderweer",
     "titel": "Schilderweer", "kort": "Kun je deze week buiten schilderen?",
     "tekst": "Zie per dag of het droog en warm genoeg is om buiten te schilderen in jouw plaats.",
     "knop": "Bekijk het schilderweer", "label": "Per dag"},
    {"slug": "inspiratie", "pad": "/inspiratie/", "bouwer": "build_inspiratie",
     "titel": "Inspiratie", "kort": "Ideeën voor je gevel en interieur",
     "tekst": "Blader door voorbeelden van kleuren en schilderwerk en ontdek wat bij jouw huis past.",
     "knop": "Bekijk de inspiratie", "label": "Galerij"},
]


def beschikbare_tools(namespace):
    """Alleen tools waarvan de bouwfunctie in `namespace` (de globals van build.py) bestaat."""
    return [t for t in TOOLS if callable(namespace.get(t["bouwer"]))]


# Kleine, lichte illustraties (inline SVG, geen extra bestanden).
_VISUALS = {
    "calculator": '''<svg viewBox="0 0 160 110" aria-hidden="true"><path d="M28 96V52l40-30 40 30v44z" fill="#fff" stroke="#6b5024" stroke-width="3" stroke-linejoin="round"/><path d="M20 58 68 22l48 36" fill="none" stroke="#6b5024" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/><rect x="42" y="58" width="16" height="14" rx="2" fill="#cfe1ee" stroke="#6b5024" stroke-width="2.5"/><rect x="78" y="58" width="16" height="14" rx="2" fill="#cfe1ee" stroke="#6b5024" stroke-width="2.5"/><rect x="60" y="76" width="16" height="20" rx="2" fill="#f4820b"/><circle cx="122" cy="70" r="24" fill="#f4820b"/><path d="M131 61a11 11 0 1 0 0 18M111 67h14M111 73h14" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round"/><path d="M8 96h144" stroke="#d9c7a8" stroke-width="3" stroke-linecap="round"/></svg>''',
    "kleuren": '''<svg viewBox="0 0 160 110" aria-hidden="true"><g stroke="rgba(0,0,0,.15)" stroke-width="1"><circle cx="40" cy="30" r="15" fill="#efe6d2"/><circle cx="80" cy="30" r="15" fill="#1f3a2e"/><circle cx="120" cy="30" r="15" fill="#8e3a2b"/><circle cx="40" cy="70" r="15" fill="#3a3d40"/><circle cx="80" cy="70" r="19" fill="#f4820b" stroke="#fff" stroke-width="4"/><circle cx="120" cy="70" r="15" fill="#3b5068"/></g><circle cx="80" cy="70" r="24" fill="none" stroke="#f4820b" stroke-width="2.5"/><path d="M28 100h104" stroke="#d9c7a8" stroke-width="3" stroke-linecap="round"/></svg>''',
    "onderhoud": '''<svg viewBox="0 0 160 110" aria-hidden="true"><path d="M30 88a50 50 0 0 1 22-41" fill="none" stroke="#0f8a5f" stroke-width="14"/><path d="M56 44a50 50 0 0 1 48 0" fill="none" stroke="#e2a80c" stroke-width="14"/><path d="M108 47a50 50 0 0 1 22 41" fill="none" stroke="#c0392b" stroke-width="14"/><path d="M80 88 104 56" stroke="#3c290f" stroke-width="5" stroke-linecap="round"/><circle cx="80" cy="88" r="9" fill="#3c290f"/><circle cx="80" cy="88" r="3.5" fill="#fff"/></svg>''',
    "weer": '''<svg viewBox="0 0 160 110" aria-hidden="true"><circle cx="66" cy="44" r="20" fill="#f4b740"/><g stroke="#f4b740" stroke-width="4" stroke-linecap="round"><path d="M66 12v8M66 68v8M34 44h8M90 44h8M43 21l6 6M83 61l6 6M43 67l6-6M83 27l6-6"/></g><path d="M78 92h46a16 16 0 0 0 0-32 22 22 0 0 0-42 6 13 13 0 0 0-4 26z" fill="#fff" stroke="#6b5024" stroke-width="3" stroke-linejoin="round"/></svg>''',
    "inspiratie": '''<svg viewBox="0 0 160 110" aria-hidden="true"><rect x="18" y="18" width="58" height="44" rx="6" fill="#1f3a2e"/><rect x="84" y="18" width="58" height="30" rx="6" fill="#efe6d2" stroke="#d9c7a8" stroke-width="2"/><rect x="18" y="70" width="58" height="26" rx="6" fill="#f4820b"/><rect x="84" y="56" width="58" height="40" rx="6" fill="#8e3a2b"/><path d="M26 54l14-14 10 10 8-6 10 10" fill="none" stroke="#efe6d2" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>''',
}


def _kaart(t, kop="h3"):
    return (f'<a class="tool-kaart tool-{t["slug"]} reveal" href="{t["pad"]}">'
            f'<div class="tool-beeld">{_VISUALS[t["slug"]]}<span class="tool-label">{t["label"]}</span></div>'
            f'<div class="tool-tekst"><{kop}>{t["titel"]}</{kop}><p class="tool-kort">{t["kort"]}</p>'
            f'<p>{t["tekst"]}</p><span class="tool-knop">{t["knop"]} <span aria-hidden="true">→</span></span></div></a>')


def tools_grid(tools, kop="h3"):
    return f'<div class="tools-grid tools-n{len(tools)}">' + "".join(_kaart(t, kop) for t in tools) + "</div>"


def tools_sectie(tools):
    """Tools-blok voor de home."""
    if not tools:
        return ""
    return f"""<section class="section tools-sectie">
<div class="wrap">
  <div class="center" style="max-width:640px;margin:0 auto 40px">
    <span class="badge badge-dark">Gratis tools</span>
    <h2>Eerst zelf rekenen, kiezen of checken?</h2>
    <p class="lead">Handige hulpjes die in je browser werken. Je hoeft niets in te vullen over jezelf.</p>
  </div>
  {tools_grid(tools)}
  <p class="center" style="margin:30px 0 0"><a class="tools-alle" href="/tools/">Alle tools bekijken →</a></p>
</div>
</section>"""


def build_tools_pagina(write, tools):
    cr, cr_ld = crumbs([("Home", "/"), ("Tools", None)])
    body = f"""{cr}
<section class="section-sm tool-hero">
<div class="wrap narrow center">
  <span class="badge">Gratis tools</span>
  <h1>Gratis tools voor je schilderklus</h1>
  <p class="lead">Reken uit wat je huis kost, probeer kleuren op je gevel of check of je schilderwerk aan de beurt is. Alles werkt in je browser en je hoeft geen gegevens achter te laten.</p>
</div>
</section>
<section class="section tools-sectie tools-pagina">
<div class="wrap">
  {tools_grid(tools, kop="h2")}
</div>
</section>
{cta_blok("Liever meteen echte prijzen?", "Een tool geeft een indicatie. Een schilder die je huis gezien heeft, geeft een prijs. Vraag gratis offertes aan bij maximaal drie schilders uit jouw regio.")}"""
    write("/tools/", page(
        "Gratis tools voor je schilderklus | Topschilder",
        "Gratis tools voor je schilderklus: bereken wat je huis kost, kies kleuren voor gevel en kozijnen en check of je schilderwerk aan de beurt is.",
        "/tools/", body, [cr_ld]), prio=0.7)
