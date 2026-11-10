# -*- coding: utf-8 -*-
"""
Topschilder.nl — statische site generator.

Gebruik:   python3 build.py
Resultaat: alles in ./site/ — klaar om te uploaden naar je hosting.
"""

import os
import re
import shutil
import datetime
import html as htmllib

from data import (SITE, DIENSTEN, PLAATSEN, buurplaatsen,
                  PRIJSINDEX, INDEX_TOELICHTING, lokale_prijs)
from illustraties import illustratie, voor_na
from foto_data import FOTOS, FOTO_HOME, FOTOS_PAGINA
from kosten_data import KOSTEN, PRIJSBANDEN
import json
from components import (
    page, crumbs, offerte_form, hoe_werkt_het, waarom_blok, dienst_cards,
    faq_blok, cta_blok, prijstabel, icon, eur, title, desc, calculator, foto, werkgebied_kaart,
)

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "site")
TODAY = datetime.date.today().isoformat()

URLS = []  # (pad, prioriteit, changefreq)


def write(path, html, prio=0.6, freq="monthly", index=True):
    full = os.path.join(OUT, path.strip("/"), "index.html") if path != "/" else os.path.join(OUT, "index.html")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)
    if index:
        URLS.append((path, prio, freq))


def wrap(inner, cls="section", extra=""):
    return f'<section class="{cls}"{extra}><div class="wrap">{inner}</div></section>'


# ===========================================================================
# HOME
# ===========================================================================

def build_home():
    kern = [p for p in PLAATSEN if p["prio"] == 1]
    chips = "".join(f'<li><a href="/schilder/{p["slug"]}/">Schilder {p["naam"]}</a></li>' for p in kern)

    hero = f"""<section class="hero">
<div class="wrap hero-in">
  <div>
    <span class="badge badge-dark badge-live"><i></i>Gratis &amp; vrijblijvend</span>
    <h1>Vergelijk schilders bij jou in de buurt</h1>
    <p class="lead">Eén aanvraag, tot drie offertes van schildersbedrijven uit jouw regio. Zo weet je binnen een paar dagen wat je klus écht hoort te kosten.</p>
    <ul class="hero-usps">
      <li><span class="check">{icon('check',12)}</span><span>Maximaal 3 schilders nemen contact op — niet meer</span></li>
      <li><span class="check">{icon('check',12)}</span><span>Alleen bedrijven met KvK-inschrijving en verzekering</span></li>
      <li><span class="check">{icon('check',12)}</span><span>Je zit nergens aan vast en betaalt niets</span></li>
    </ul>
    <div class="hero-proof">
      <span>Binnen- en buitenschilderwerk</span><span>·</span>
      <span>Houtrot &amp; spuitwerk</span><span>·</span>
      <span>Particulier en zakelijk</span>
    </div>
    <div style="margin-top:30px;max-width:460px">{foto(FOTO_HOME, "(max-width:500px) calc(100vw - 40px), 460px", boven_vouw=True)}</div>
  </div>
  <div>{offerte_form()}</div>
</div>
</section>"""

    diensten_sec = f"""<section class="section">
<div class="wrap">
  <div class="center" style="max-width:620px;margin:0 auto 40px">
    <h2>Waar heb je een schilder voor nodig?</h2>
    <p class="lead">Per klus zie je wat het ongeveer kost, waar de prijs door bepaald wordt en waar je op moet letten in een offerte.</p>
  </div>
  {dienst_cards()}
</div>
</section>"""

    prijs_sec = f"""<section class="section soft">
<div class="wrap narrow">
  <span class="badge">Richtprijzen 2026</span>
  <h2>Wat kost een schilder?</h2>
  <p class="lead">Een schilder rekent gemiddeld €45 tot €65 per uur exclusief btw. Maar bijna niemand koopt uren — je koopt een afgewerkte muur of een kozijn dat weer tien jaar meekan. Daarom rekenen de meeste bedrijven per vierkante meter of per stuk.</p>
  {prijstabel()}
  <p style="margin-top:22px"><a class="btn btn-ghost" href="/prijzen/">Volledig prijzenoverzicht bekijken</a></p>
</div>
</section>"""

    regio_sec = f"""<section class="section">
<div class="wrap">
  <h2>Schilders per plaats</h2>
  <p class="lead" style="max-width:60ch">We zijn begonnen in Flevoland en de randmeren en breiden stap voor stap uit. Staat jouw plaats er niet bij? Vraag alsnog offertes aan — vaak rijden schilders uit de buurgemeente er graag heen.</p>
  <ul class="chips" style="margin:26px 0">{chips}</ul>
  <p><a href="/werkgebied/">Bekijk alle {len(PLAATSEN)} plaatsen →</a></p>
</div>
</section>"""

    vergelijk_sec = f"""<section class="section soft">
<div class="wrap">
  <div class="grid g2" style="align-items:center;gap:44px">
    <div>
      <span class="badge">Uniek</span>
      <h2>Al een offerte binnen? Laat 'm checken</h2>
      <p>Je hebt een offerte van een schilder liggen maar je hebt geen idee of het een normale prijs is. Herkenbaar. Stuur 'm naar ons op en je krijgt binnen twee werkdagen een eerlijk oordeel: is dit marktconform, wat ontbreekt er in de omschrijving en welke posten zou je nog willen zien.</p>
      <ul class="checklist">
        <li>Prijs vergeleken met wat vergelijkbare klussen in jouw regio kosten</li>
        <li>Ontbrekende posten die later meerwerk worden</li>
        <li>Concrete vragen die je aan de schilder kunt stellen</li>
      </ul>
      <p><a class="btn btn-dark" href="/offerte-vergelijken/">Mijn offerte laten checken</a></p>
    </div>
    <div>
      <div class="card" style="box-shadow:var(--shadow-lg);border:0">
        <h3 style="margin-bottom:16px">Waar mensen het vaakst op misgrijpen</h3>
        <div class="faq">
          <details><summary>Steigerkosten niet benoemd</summary><div class="a"><p>Staat er niets over steiger of hoogwerker, dan komt die post er vrijwel zeker later bij. Reken op €300 tot €900.</p></div></details>
          <details><summary>Houtrot als losse post</summary><div class="a"><p>&quot;Houtrot in regie&quot; betekent: onbekend bedrag. Vraag om een stelpost met een maximum.</p></div></details>
          <details><summary>Aantal lagen niet vermeld</summary><div class="a"><p>Twee lagen of drie scheelt zomaar 25% in arbeidsuren én jaren in levensduur.</p></div></details>
          <details><summary>Btw-tarief klopt niet</summary><div class="a"><p>Schilderwerk aan een woning ouder dan twee jaar valt onder 9%, inclusief de gebruikte materialen. Staat alles op 21%, vraag dan waarom.</p></div></details>
        </div>
      </div>
    </div>
  </div>
</div>
</section>"""

    schilders_sec = """<section class="section dark">
<div class="wrap center" style="max-width:680px">
  <span class="badge badge-dark">Voor schildersbedrijven</span>
  <h2>Zoek je zelf werk in plaats van een schilder?</h2>
  <p class="lead" style="color:#b8cadd">We koppelen aanvragen aan schilders in de regio. Je betaalt per lead, niet per maand, en je kunt je werkgebied en het aantal aanvragen zelf begrenzen.</p>
  <p style="margin-top:24px"><a class="btn btn-primary btn-lg" href="/voor-schilders/">Bekijk de voorwaarden voor schilders</a></p>
</div>
</section>"""

    faqs = [
        ("Wat kost het om via Topschilder offertes aan te vragen?",
         "Niets. Aanvragen is volledig gratis en vrijblijvend voor particulieren en bedrijven. Wij worden betaald door de schildersbedrijven die de aanvraag ontvangen."),
        ("Hoeveel schilders nemen er contact met mij op?",
         "Maximaal drie. Dat is genoeg om echt te kunnen vergelijken, en weinig genoeg om niet dagenlang gebeld te worden. Je gegevens gaan nooit naar meer partijen dan dat."),
        ("Ben ik verplicht een offerte te accepteren?",
         "Nee. Je vergelijkt de offertes, kiest wat je wilt en kunt alle drie afwijzen zonder opgaaf van reden. Er zijn geen kosten en geen kleine lettertjes."),
        ("Hoe snel heb ik een reactie?",
         "Aanvragen worden dezelfde werkdag doorgezet naar schilders in jouw regio. In de praktijk belt de eerste schilder meestal binnen één werkdag. In het hoogseizoen (april tot september) kan dat iets langer duren."),
        ("Hoe worden schilders geselecteerd?",
         "We controleren KvK-inschrijving en aansprakelijkheidsverzekering, en we kijken of het bedrijf het gevraagde type werk daadwerkelijk uitvoert. Bij herhaalde klachten stoppen we de samenwerking."),
        ("Wat gebeurt er met mijn gegevens?",
         "Je gegevens gaan alleen naar maximaal 3 schilders uit jouw regio. Zij betalen ons een vergoeding om je aanvraag te ontvangen. Andere partijen krijgen je gegevens niet en we gebruiken ze niet voor ongevraagde reclame. Zie onze privacyverklaring."),
    ]
    faq_html, faq_ld = faq_blok(faqs)

    org_ld = {
        "@context": "https://schema.org",
        "@type": "Organization",
        "@id": SITE["url"] + "/#organization",
        "name": SITE["naam"],
        "url": SITE["url"],
        "email": SITE["email"],
        "areaServed": [{"@type": "AdministrativeArea", "name": p["provincie"]}
                       for p in [{"provincie": x} for x in ["Flevoland", "Gelderland", "Overijssel", "Utrecht", "Noord-Holland"]]],
        "description": "Topschilder koppelt particulieren en bedrijven aan schildersbedrijven in hun regio en laat hen gratis offertes vergelijken.",
    }
    web_ld = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "@id": SITE["url"] + "/#website",
        "name": SITE["naam"],
        "url": SITE["url"],
        "inLanguage": "nl-NL",
        "publisher": {"@id": SITE["url"] + "/#organization"},
    }

    body = (hero + waarom_blok() + diensten_sec + hoe_werkt_het() + prijs_sec
            + vergelijk_sec + regio_sec + faq_html + schilders_sec + cta_blok())

    write("/", page(
        "Schilder nodig? Vergelijk gratis 3 offertes | Topschilder.nl",
        "Vergelijk vrijblijvend offertes van schilders bij jou in de buurt. Binnen- en buitenschilderwerk, houtrot en spuitwerk. Gratis, max. 3 schilders, geen verplichtingen.",
        "/", body, [org_ld, web_ld, faq_ld]), prio=1.0, freq="weekly")


# ===========================================================================
# DIENSTEN
# ===========================================================================

def build_diensten_index():
    cr, cr_ld = crumbs([("Home", "/"), ("Diensten", None)])
    body = f"""{cr}
<section class="section-sm"><div class="wrap narrow">
  <h1>Schilderwerk: alle diensten en wat ze kosten</h1>
  <p class="lead">Van een enkele deur laten spuiten tot het complete buitenschilderwerk van een vrijstaande woning. Kies hieronder je klus en zie meteen de richtprijzen, waar de prijs door bepaald wordt en waar je in een offerte op moet letten.</p>
</div></section>
<section class="section-sm"><div class="wrap">{dienst_cards()}</div></section>
<section class="section soft"><div class="wrap narrow prose">
  <h2>Welke dienst past bij jouw klus?</h2>
  <p>Niet elke klus heeft een duidelijke naam. Herken je je situatie hieronder, dan weet je waar je moet zijn.</p>
  <div class="tablewrap"><table>
    <thead><tr><th>Wat je ziet of wilt</th><th>Kijk bij</th></tr></thead>
    <tbody>
      <tr><td>Muren en plafonds zijn vlekkerig, of je wilt een andere kleur</td><td><a href="/schilderwerk/binnenschilderwerk/">Binnenschilderwerk</a></td></tr>
      <tr><td>De verf op kozijnen, deuren of boeiboorden bladdert of wordt dof</td><td><a href="/schilderwerk/buitenschilderwerk/">Buitenschilderwerk</a></td></tr>
      <tr><td>Hout voelt zacht aan, vooral in de onderhoek van een kozijn</td><td><a href="/schilderwerk/houtrot-reparatie/">Houtrot reparatie</a></td></tr>
      <tr><td>Muren of plafonds moeten egaal gespoten worden, of deuren en keukenfronten moeten strak worden</td><td><a href="/schilderwerk/spuitwerk/">Latex spuiten en spuitwerk</a></td></tr>
      <tr><td>Oud behang moet eraf, of je wilt glasvlies of een statementwand</td><td><a href="/schilderwerk/behangen/">Behangen</a></td></tr>
      <tr><td>Het gaat om een kantoor, winkel of bedrijfspand</td><td><a href="/schilderwerk/zakelijk-schilderwerk/">Zakelijk schilderwerk</a></td></tr>
    </tbody>
  </table></div>
  {foto(FOTOS_PAGINA["diensten"], "(max-width:760px) calc(100vw - 40px), 720px")}
  <h2>Eerst repareren, dan schilderen</h2>
  <p>Verf is geen reparatie. Zit er houtrot in een kozijn, dan moet dat eerst hersteld zijn, anders werkt het vocht onder de nieuwe laag gewoon door. Twijfel je of het om schilderwerk of om reparatie gaat? Beschrijf in je aanvraag wat je ziet. De schilder kan dat dan ter plekke beoordelen.</p>
  <h2>Klussen combineren</h2>
  <p>Staat er zowel binnen als buiten iets op de planning, noem dat dan meteen. Eén planning scheelt de schilder opstarttijd, en jij ziet in één offerte wat alles samen kost. Vraag wel om een aparte regel per onderdeel, zodat je kunt vergelijken en eventueel iets kunt schrappen.</p>
</div></section>
{hoe_werkt_het()}
{cta_blok()}"""
    write("/schilderwerk/", page(
        title("Schilderwerk: diensten en richtprijzen"),
        "Overzicht van al het schilderwerk dat je via Topschilder kunt aanvragen: binnen, buiten, houtrot, spuitwerk, behangen en zakelijk. Met actuele richtprijzen per dienst.",
        "/schilderwerk/", body, [cr_ld]), prio=0.8)


def dienst_body(d, plaats=None):
    """Bouwt de inhoud voor zowel /schilderwerk/{dienst}/ als /schilder/{plaats}/{dienst}/."""
    pn = plaats["naam"] if plaats else None
    inplaats = f" in {pn}" if pn else ""
    p_van, p_tot = lokale_prijs(d, plaats) if plaats else (d["prijs_van"], d["prijs_tot"])
    prijsnoot = (
        f" Dat is de richtprijs voor {plaats['provincie']}, "
        f"{'iets onder' if PRIJSINDEX.get(plaats['provincie'],1) < 0.99 else 'rond' if PRIJSINDEX.get(plaats['provincie'],1) < 1.03 else 'boven'}"
        f" het landelijk gemiddelde."
    ) if plaats else ""

    if plaats:
        cr, cr_ld = crumbs([("Home", "/"), ("Werkgebied", "/werkgebied/"),
                            (pn, f"/schilder/{plaats['slug']}/"), (d["naam"], None)])
        h1 = f"{d['naam']} {pn}"
        intro_extra = f"<p>{plaats['hook']}</p>"
    else:
        cr, cr_ld = crumbs([("Home", "/"), ("Diensten", "/schilderwerk/"), (d["naam"], None)])
        h1 = f"{d.get('naam_lang', d['naam'])}: kosten, werkwijze en offertes"
        intro_extra = ""

    vn_blok = ("" if d["slug"] not in ("buitenschilderwerk", "houtrot-reparatie") else
        '<h2>Het verschil, in beeld</h2>'
        '<p>Sleep de streep opzij. Links een gevel die vier jaar te lang heeft gewacht, '
        'rechts dezelfde gevel na een beurt. Het gaat niet alleen om hoe het oogt: die '
        'verflaag houdt het water uit je houtwerk.</p>' + voor_na())
    wat = "".join(f"<li>{x}</li>" for x in d["wat"])
    werk = "".join(
        f"<li><h3>{t}</h3><p>{p}</p></li>" for t, p in
        [(f"{i+1}. {t}", p) for i, (t, p) in enumerate(d["werkwijze"])]
    )
    werk = "<ol style='list-style:none;padding:0'>" + "".join(
        f"<li style='border-left:3px solid var(--line);padding:0 0 18px 20px;margin:0'>"
        f"<h3 style='margin-bottom:.2em'>{t}</h3><p style='margin:0;font-size:.97rem'>{p}</p></li>"
        for t, p in d["werkwijze"]
    ) + "</ol>"
    fotos = FOTOS.get(d["slug"], {})
    beeld = (foto(fotos["hero"], "(max-width:980px) calc(100vw - 40px), 536px", boven_vouw=True) if fotos else
             f'<div class="reveal" style="margin-top:24px">{illustratie(d["slug"])}</div>')
    sectiefoto = foto(fotos["sectie"], "(max-width:760px) calc(100vw - 40px), 720px") if fotos else ""
    latex_blok = ("" if d["slug"] != "spuitwerk" else """
  <h2>Latex spuiten of spuitwerk: wat is het verschil?</h2>
  <p>Latex spuiten is de naam die je tegenkomt bij muren en plafonds. De schilder brengt de muurverf dan aan met een verfspuit, meestal airless. Het is een vorm van spuitwerk. Spuitwerk is de bredere term: ook deuren, kozijnen, keukenfronten en metaal kunnen worden gespoten.</p>
  <h3>Wanneer past latex spuiten?</h3>
  <ul class="checklist">
    <li><strong>Egale muren en plafonds.</strong> De verf komt verneveld op het oppervlak, zonder rolbanen of strepen. Dat zie je vooral op plafonds en bij strijklicht.</li>
    <li><strong>Veel oppervlak in een lege ruimte.</strong> Dan weegt het afdekken op tegen de tijd die spuiten scheelt.</li>
  </ul>
  <h3>Waar je rekening mee houdt</h3>
  <ul>
    <li>Verfnevel verspreidt zich. Alles wat niet geverfd wordt moet worden afgedekt, en dat is een flink deel van het werk.</li>
    <li>Spuiten maskeert niets. Gaten, scheuren en andere oneffenheden moeten eerst worden gerepareerd.</li>
  </ul>
  <h3>Wat kost latex spuiten?</h3>
  <p>De richtprijs bovenaan deze pagina gaat over het spuiten van deuren. Voor latex spuiten noemen andere Nederlandse sites deze indicaties per m²: <a href="https://www.homedeal.nl/schilderwerk/latex-spuiten/" rel="nofollow noopener">Homedeal</a> gemiddeld €6 tot €12, <a href="https://trustoo.nl/kennisbank/schilder/latex-spuiten/" rel="nofollow noopener">Trustoo</a> gemiddeld €5 tot €15 en <a href="https://slimster.nl/schilder/schilderwerk-prijzen/kosten-latex-spuiten/" rel="nofollow noopener">Slimster</a> €5 tot €20. Dit zijn indicaties van die sites (geraadpleegd in november 2026), geen prijzen van Topschilder. Je echte prijs hangt af van de ruimte, de ondergrond en het afdekwerk.</p>
  <p>De Belastingdienst noemt schilderen van woningen ouder dan twee jaar onder het 9%-tarief, maar noemt spuiten niet apart. Kijk daarom op de offerte welk tarief er staat en vraag ernaar als het je niet duidelijk is.</p>
""")
    btw_extra = {
        "houtrot-reparatie": "<li>Houtwerk apart benoemd: inzetstukken en nieuwe onderdorpels vallen onder 21% btw, het schilderwerk eromheen onder 9%</li>",
        "behangen": "<li>Het behang apart benoemd: de levering van behang valt onder 21% btw, het behangen zelf en de lijm onder 9%</li>",
    }.get(d["slug"], "")
    fact = "".join(f"<li>{x}</li>" for x in d["prijsfactoren"])
    tips = "".join(f"<li>{x}</li>" for x in d["tips"])

    hero = f"""<section class="section-sm">
<div class="wrap">
  <div class="grid g2" style="gap:48px;align-items:start">
    <div>
      <span class="badge">{d['naam_kort']}</span>
      <h1>{h1}</h1>
      <p class="lead">{d['intro']}</p>
      {intro_extra}
      <div class="callout">
        <p><strong>Richtprijs{inplaats}:</strong> {eur(p_van)} – {eur(p_tot)} {d['prijs_eenheid']}{'' if 'excl' in d['prijs_eenheid'] else ', inclusief materiaal en btw'}.{prijsnoot}</p>
        <p style="font-size:.93rem;margin-top:8px">{d['prijs_extra']}</p>
        {kosten_links(d)}
      </div>
      {beeld}
    </div>
    <div>{offerte_form(f"Offertes voor {d['naam_kort'].lower()}{inplaats}", "Vier korte vragen · gratis en vrijblijvend")}</div>
  </div>
</div>
</section>"""

    content = f"""<section class="section soft"><div class="wrap narrow prose reveal">
  <h2>Wat valt er onder {d['naam'].lower()}?</h2>
  <ul class="checklist">{wat}</ul>
  {latex_blok}

  <h2>Zo gaat een schilder te werk</h2>
  {werk}
  {sectiefoto}

  {vn_blok}

  <h2>Waar hangt de prijs vanaf?</h2>
  <p>Twee offertes voor ogenschijnlijk dezelfde klus kunnen honderden euro's uit elkaar liggen. Dat komt zelden door de winstmarge en bijna altijd door deze factoren:</p>
  <ul>{fact}</ul>

  <h2>Drie tips die je geld schelen</h2>
  <ul class="checklist">{tips}</ul>

  <h2>Let hierop in de offerte</h2>
  <p>Een goede offerte voor {d['naam'].lower()} is meer dan een bedrag onderaan een A4'tje. Controleer of het volgende erin staat:</p>
  <ul>
    <li>Welk verfmerk, welk type en welke glansgraad er gebruikt wordt</li>
    <li>Het aantal lagen — grondlaag plus twee dekkende lagen is de norm</li>
    <li>Wat er precies onder de voorbereiding valt (schuren, ontvetten, plamuren)</li>
    <li>Het btw-tarief per post: 9% voor schilderwerk en gebruikte materialen aan een woning ouder dan twee jaar, 21% voor wat daarbuiten valt</li>{btw_extra}
    <li>Een concrete start- en opleverdatum, geen &quot;in overleg&quot;</li>
    <li>De garantietermijn en wat daar wel en niet onder valt</li>
  </ul>
</div></section>"""

    return cr, cr_ld, hero + content


def build_dienst_pages():
    for d in DIENSTEN:
        cr, cr_ld, body_top = dienst_body(d)
        faq_html, faq_ld = faq_blok(d["faq"], f"Veelgestelde vragen over {d['naam'].lower()}")

        andere = f"""<section class="section"><div class="wrap">
  <h2>Ander schilderwerk</h2>
  {dienst_cards(exclude=d['slug'])}
</div></section>"""

        plaats_chips = "".join(
            f'<li><a href="/schilder/{p["slug"]}/{d["slug"]}/">{d["naam_kort"]} {p["naam"]}</a></li>'
            for p in PLAATSEN if p["prio"] <= 2
        )
        regio = f"""<section class="section soft"><div class="wrap">
  <h2>{d['naam']} per plaats</h2>
  <p class="lead" style="max-width:60ch">Bekijk wat {d['naam'].lower()} kost in jouw gemeente en vraag direct offertes aan bij schilders uit de buurt.</p>
  <ul class="chips" style="margin-top:22px">{plaats_chips}</ul>
  <p style="margin-top:20px"><a href="/werkgebied/">Alle plaatsen bekijken →</a></p>
</div></section>"""

        svc_ld = {
            "@context": "https://schema.org",
            "@type": "Service",
            "serviceType": d["naam"],
            "name": f"{d['naam']} offertes vergelijken",
            "provider": {"@id": SITE["url"] + "/#organization"},
            "areaServed": {"@type": "Country", "name": "Nederland"},
            "description": d["kort"],
            "offers": {
                "@type": "AggregateOffer",
                "priceCurrency": "EUR",
                "lowPrice": d["prijs_van"],
                "highPrice": d["prijs_tot"],
            },
        }

        body = body_top + faq_html + regio + andere + cta_blok(
            f"Offertes voor {d['naam'].lower()} vergelijken?",
            "Vertel in een minuut wat je nodig hebt. Wij zoeken maximaal drie schilders die dit werk doen en beschikbaar zijn.")

        write(f"/schilderwerk/{d['slug']}/", page(
            title(d.get("seo_titel") or f"{d['naam']} kosten {eur(d['prijs_van'])}–{eur(d['prijs_tot'])} {d['prijs_eenheid']}"),
            desc(f"Wat kost {d.get('naam_lang', d['naam']).lower()}?",
                 f"Richtprijzen {d['prijs_eenheid']}, werkwijze en prijsfactoren.",
                 "Plus waar je op let in een offerte.",
                 "Vergelijk gratis 3 schilders bij jou in de buurt."),
            f"/schilderwerk/{d['slug']}/", body, [cr_ld, faq_ld, svc_ld]), prio=0.9)


# ===========================================================================
# PLAATSEN
# ===========================================================================

REGIO_TEKST = {
    "Flevoland": "De steden en dorpen hier zijn gebouwd nadat de polders waren drooggelegd. Daardoor zijn hele wijken even oud en komt het houtwerk van een buurt vaak rond dezelfde tijd aan onderhoud toe.",
    "Gelderland": "Langs de randmeren en de Veluwe staan historische kernen zoals Elburg en Harderwijk naast naoorlogse wijken en nieuwbouw. Dat vraagt per woning om een andere aanpak.",
    "Noord-Holland": "In het Gooi en rond Weesp vind je veel oudere vrijstaande woningen met flink wat houtwerk, en met Naarden en Weesp ook vestingsteden. Zet in je aanvraag wat voor woning je hebt.",
    "Overijssel": "Kampen en Zwolle hebben historische binnensteden met oude gevels. Woon je in een monument of beschermd stadsgezicht, vraag dan bij je gemeente na of je voor een andere kleur een vergunning nodig hebt.",
    "Utrecht": "In Amersfoort en Bunschoten-Spakenburg staan oude stadskernen en dorpsgezichten naast grote uitbreidingswijken. Bij die laatste komt het onderhoud vaak per straat tegelijk.",
}


def build_werkgebied():
    per_prov = {}
    for p in sorted(PLAATSEN, key=lambda x: x["naam"]):
        per_prov.setdefault(p["provincie"], []).append(p)

    secs = ""
    for prov in sorted(per_prov):
        lis = "".join(f'<li><a href="/schilder/{p["slug"]}/">Schilder {p["naam"]}</a></li>' for p in per_prov[prov])
        secs += f"<h2>{prov}</h2><p style='max-width:68ch'>{REGIO_TEKST[prov]}</p><ul class='places' style='margin-bottom:34px'>{lis}</ul>"

    cr, cr_ld = crumbs([("Home", "/"), ("Werkgebied", None)])
    body = f"""{cr}
<section class="section-sm"><div class="wrap narrow">
  <h1>Ons werkgebied</h1>
  <p class="lead">Topschilder is begonnen in Flevoland en werkt inmiddels ook in de randmeren-regio, de Veluwe, de IJsseldelta en het Gooi. Kies je plaats voor lokale richtprijzen en schilders uit de buurt.</p>
  <p>Staat jouw plaats er niet tussen? Vraag toch offertes aan. Veel schildersbedrijven rijden zonder problemen 20 tot 30 kilometer, zeker bij een meerdaagse klus.</p>
</div></section>
<section class="section-sm" id="kaart"><div class="wrap">{werkgebied_kaart()}</div></section>
<section class="section-sm"><div class="wrap">
  <h2 style="margin-bottom:6px">Alle plaatsen per provincie</h2>
  <p style="margin-bottom:30px">Elke plaats heeft een eigen pagina met lokale richtprijzen en de diensten die je daar kunt aanvragen.</p>
  {secs}
</div></section>
<section class="section soft"><div class="wrap narrow prose">
  {foto(FOTOS_PAGINA["werkgebied"], "(max-width:760px) calc(100vw - 40px), 720px")}
  <h2>Hoe we bepalen wie er bij jou langskomt</h2>
  <p>Je vult je plaats en de klus in. Wij zoeken daarna maximaal drie schilders die in jouw regio werken en dit type werk doen. Staat jouw plaats niet op de kaart, dan kun je alsnog een aanvraag doen. We laten je weten of er een schilder beschikbaar is.</p>
</div></section>
{cta_blok()}"""
    write("/werkgebied/", page(
        title(f"Werkgebied: schilders in {len(PLAATSEN)} plaatsen"),
        "Bekijk in welke plaatsen Topschilder schilders koppelt. Van Almere en Lelystad tot Zwolle, Amersfoort en Hilversum. Vergelijk gratis offertes in jouw gemeente.",
        "/werkgebied/", body, [cr_ld]), prio=0.8)


def build_plaats_pages():
    for p in PLAATSEN:
        buren = buurplaatsen(p, 8)
        buren_li = "".join(f'<li><a href="/schilder/{b["slug"]}/">Schilder {b["naam"]}</a></li>' for b in buren)
        cr, cr_ld = crumbs([("Home", "/"), ("Werkgebied", "/werkgebied/"), (p["naam"], None)])

        hero = f"""<section class="section-sm">
<div class="wrap">
  <div class="grid g2" style="gap:48px;align-items:start">
    <div>
      <span class="badge">{p['gemeente']} · {p['provincie']}</span>
      <h1>Schilder in {p['naam']} nodig?</h1>
      <p class="lead">Vergelijk vrijblijvend offertes van schildersbedrijven die in {p['naam']} werken. Eén aanvraag, tot drie prijzen, en je zit nergens aan vast.</p>
      <p>{p['hook']}</p>
      <ul class="checklist">
        <li>Schilders die {p['naam']} en omgeving als vast werkgebied hebben</li>
        <li>Gecontroleerd op KvK-inschrijving en aansprakelijkheidsverzekering</li>
        <li>Gratis vergelijken, geen abonnement, geen verplichtingen</li>
      </ul>
    </div>
    <div>{offerte_form(f"Offertes van schilders in {p['naam']}", "Vier korte vragen · reactie meestal binnen 24 uur")}</div>
  </div>
</div>
</section>"""

        diensten_sec = f"""<section class="section soft"><div class="wrap">
  <div class="center" style="max-width:640px;margin:0 auto 40px">
    <h2>Waar heb je een schilder voor nodig in {p['naam']}?</h2>
    <p class="lead">Klik door voor de richtprijzen per klus en vraag direct offertes aan bij lokale bedrijven.</p>
  </div>
  {dienst_cards(p['slug'], p['naam'])}
</div></section>"""

        idx = PRIJSINDEX.get(p["provincie"], 1.0)
        uur_van, uur_tot = int(round(45 * idx)), int(round(65 * idx))
        v = PLAATSEN.index(p) % 3
        groot = p["inwoners"] >= 40000

        if v == 0:
            blok_a = f"""<h3>Waarom je in {p['naam']} meerdere offertes wilt</h3>
  <p>{'In een stad van dit formaat zijn er genoeg schildersbedrijven, en juist daardoor lopen de prijzen ver uiteen. Het ene bedrijf werkt met twee man en een bestelbus, het andere met een kantoor, een planner en een bedrijfsauto per monteur. Beide leveren goed werk, maar hun kostenstructuur verschilt met tientallen procenten.' if groot else 'Het aantal actieve schildersbedrijven in ' + p['naam'] + ' is beperkt, en dan bepaalt de agenda de prijs. Een schilder met drie weken lucht offreert wezenlijk anders dan iemand die tot november volgeboekt zit.'} Met één offerte weet je nooit in welke categorie je terecht bent gekomen.</p>"""
        elif v == 1:
            blok_a = f"""<h3>Lokaal of van verderop?</h3>
  <p>Veel mensen zoeken bewust een schilder uit {p['naam']} zelf. Begrijpelijk, maar niet altijd de scherpste keuze. Schildersbedrijven werken doorgaans in een straal van twintig tot dertig kilometer, en een bedrijf uit de buurgemeente met een gat in de planning kan makkelijk honderden euro's onder je lokale bedrijf duiken. Voor een meerdaagse klus wegen voorrijkosten nauwelijks mee. Kijk dus naar {p['gemeente']} én de gemeenten eromheen.</p>"""
        else:
            blok_a = f"""<h3>Wat een schilder in {p['naam']} van je nodig heeft</h3>
  <p>Hoe concreter jouw vraag, hoe scherper de offerte. Noem het aantal ramen of vierkante meters, wanneer er voor het laatst geschilderd is, en of je ergens houtrot of afbladderende verf ziet. Schilders calculeren onzekerheid altijd in — vertel je niets, dan zit er een marge in de prijs voor tegenvallers die er misschien niet eens zijn. Een paar foto's meesturen scheelt in de praktijk zo tien procent.</p>"""

        if v == 0:
            blok_b = f"""<h3>Het seizoen scheelt geld</h3>
  <p>Van maart tot en met september draaien schilders overuren aan buitenwerk. Wil je scherp zitten, plan buitenschilderwerk dan in september of oktober en binnenschilderwerk tussen november en februari. Je hebt dan meer keuze én meer onderhandelingsruimte. Dat geldt in {p['naam']} net zo hard als in de rest van {p['provincie']}.</p>"""
        elif v == 1:
            blok_b = f"""<h3>Het btw-voordeel dat veel mensen missen</h3>
  <p>Is je woning in {p['naam']} ouder dan twee jaar, dan valt schilderwerk onder het btw-tarief van 9%, en dat geldt ook voor de gebruikte materialen. Staat er 21% over het hele bedrag, vraag dan waarom. Voor werk dat verder gaat dan schilderen, zoals het inzetten van nieuw hout in een kozijn, geldt wel 21%.</p>"""
        else:
            blok_b = f"""<h3>Wachttijden in {p['gemeente']}</h3>
  <p>Buiten het hoogseizoen kun je in {p['naam']} meestal binnen twee tot vier weken terecht. Tussen april en september loopt dat op tot zes weken of meer, zeker voor buitenwerk. Ben je flexibel in je planning, zeg dat er dan bij: schilders vullen graag gaten tussen twee grote klussen en zijn daar vaak scherper voor geprijsd dan voor een klus die op een vaste datum moet vallen.</p>"""

        prijs_sec = f"""<section class="section"><div class="wrap narrow prose">
  <h2>Wat kost een schilder in {p['naam']}?</h2>
  <p>Schilders in {p['gemeente']} rekenen doorgaans <strong>{eur(uur_van)} tot {eur(uur_tot)} per uur exclusief btw</strong>. {INDEX_TOELICHTING.get(p['provincie'], '')} In de praktijk zie je dat uurtarief zelden terug op een offerte: het meeste werk wordt aangeboden per vierkante meter of per stuk, omdat je dan vooraf weet waar je aan toe bent.</p>
  {prijstabel(plaats=p)}

  <h3>De woningvoorraad van {p['naam']}</h3>
  <p>Het gros van de woningen in {p['naam']} is gebouwd {p['bouwperiode']}. Het gaat overwegend om {p['woningmix']}. Dat is relevant voor je offerte, want het bepaalt hoeveel kozijnen er zijn, hoe hoog er gewerkt moet worden en of er een steiger nodig is. Bij {'ruime, vrijstaande bouw loopt het aantal te schilderen kozijnen snel op' if 'vrijstaande' in p['woningmix'] or 'villa' in p['woningmix'] else 'rijwoningen blijft het aantal kozijnen beperkt, maar is de bereikbaarheid van de achtergevel soms lastig'}.</p>
  <p>Daarnaast telt de ligging mee: {p['naam']} kenmerkt zich door {p['ligging']}. Gevels die het meeste weer vangen, vragen eerder onderhoud dan de beschutte kant van hetzelfde huis. Een schilder die daar bij de opname onderscheid in maakt, weet waar hij het over heeft.</p>

  {blok_a}

  {blok_b}
</div></section>"""

        buren_sec = f"""<section class="section soft"><div class="wrap">
  <h2>Ook actief rond {p['naam']}</h2>
  <p class="lead" style="max-width:60ch">De meeste schilders in deze regio werken in een straal van 20 tot 30 kilometer. Zoek je in een buurgemeente?</p>
  <ul class="places" style="margin-top:22px">{buren_li}</ul>
</div></section>"""

        faqs = [
            (f"Hoeveel schilders in {p['naam']} nemen contact met mij op?",
             "Maximaal drie. Zo kun je goed vergelijken zonder dat je de hele week wordt gebeld. Reageren er minder, dan zijn er op dat moment simpelweg niet meer bedrijven met ruimte in de agenda."),
            (f"Werken deze schilders ook echt in {p['naam']}?",
             f"Ja. We koppelen alleen bedrijven die {p['naam']} en omgeving in hun vaste werkgebied hebben opgenomen. Zo voorkom je voorrijkosten van een bedrijf dat drie provincies verderop zit."),
            (f"Wat is de gemiddelde wachttijd voor een schilder in {p['gemeente']}?",
             "Buiten het hoogseizoen kun je meestal binnen twee tot vier weken terecht. Tussen april en september loopt dat op tot zes weken of meer, zeker voor buitenwerk. Ben je flexibel in je planning, meld dat dan — je krijgt vaak een betere prijs."),
            ("Geldt het lage btw-tarief van 9%?",
             "Ja, voor schilderwerk aan een woning ouder dan twee jaar, inclusief de gebruikte materialen. Voor werk dat verder gaat dan schilderen geldt 21%. Staat er 21% over het geheel, vraag dan waarom."),
            ("Kan ik ook zakelijk schilderwerk aanvragen?",
             f"Zeker. Kantoren, winkels, VvE's en bedrijfspanden in {p['naam']} kunnen dezelfde route volgen. Kies bij de eerste vraag voor zakelijk schilderwerk, dan komt je aanvraag bij bedrijven terecht die dit type werk aankunnen."),
        ]
        faq_html, faq_ld = faq_blok(faqs, f"Veelgestelde vragen over schilders in {p['naam']}")

        svc_ld = {
            "@context": "https://schema.org",
            "@type": "Service",
            "serviceType": "Schilderwerk",
            "name": f"Schilder vinden in {p['naam']}",
            "provider": {"@id": SITE["url"] + "/#organization"},
            "areaServed": {
                "@type": "City", "name": p["naam"],
                "containedInPlace": {"@type": "AdministrativeArea", "name": p["provincie"]},
            },
            "description": f"Vergelijk gratis offertes van schildersbedrijven in {p['naam']} ({p['provincie']}).",
        }

        body = (cr + hero + diensten_sec + hoe_werkt_het(p["naam"]) + prijs_sec
                + faq_html + buren_sec
                + cta_blok(f"Schilder zoeken in {p['naam']}?",
                           f"Vul het formulier in en ontvang vrijblijvend offertes van maximaal drie schildersbedrijven die in {p['naam']} werken."))

        write(f"/schilder/{p['slug']}/", page(
            title(f"Schilder {p['naam']}: vergelijk gratis 3 offertes"),
            desc(f"Schilder nodig in {p['naam']}?",
                 f"Vergelijk vrijblijvend offertes van schildersbedrijven uit {p['gemeente']}.",
                 "Binnen- en buitenschilderwerk, houtrot en spuitwerk.",
                 "Gratis en zonder verplichtingen."),
            f"/schilder/{p['slug']}/", body, [cr_ld, faq_ld, svc_ld]),
            prio=0.9 if p["prio"] == 1 else 0.7)


def build_plaats_dienst_pages():
    for p in PLAATSEN:
        buren = buurplaatsen(p, 5)
        for d in DIENSTEN:
            cr, cr_ld, body_top = dienst_body(d, p)

            p_van, p_tot = lokale_prijs(d, p)
            idx = PRIJSINDEX.get(p["provincie"], 1.0)
            seizoen = d["slug"] in ("buitenschilderwerk", "houtrot-reparatie")

            # Derde blok rouleert, zodat geen twee combinaties hetzelfde lezen.
            variant = (PLAATSEN.index(p) + DIENSTEN.index(d)) % 4
            if variant == 0:
                derde = f"""<h3>Hoeveel schilders zitten er in {p['naam']}?</h3>
  <p>Met ongeveer {p['inwoners']:,} inwoners is het aantal actieve schildersbedrijven in {p['naam']} overzichtelijk. Dat heeft twee kanten. Positief: je krijgt een lokale partij die je buurt kent en geen anderhalf uur hoeft te rijden. Minder positief: bij weinig aanbod bepaalt de agenda de prijs. Een schilder die tot november volgeboekt zit, geeft simpelweg een hogere offerte dan iemand met drie weken lucht. Precies daarom heeft één offerte opvragen geen zin — je hebt geen enkel ijkpunt.</p>""".replace(",", ".")
            elif variant == 1:
                derde = f"""<h3>Voorrijkosten en bereikbaarheid</h3>
  <p>{p['naam']} ligt in {p['gemeente']}. Voor een meerdaagse klus rekenen schilders hier zelden voorrijkosten — die zitten in de aanneemsom. Gaat het om een kleine klus van een halve dag, dan zie je regelmatig €35 tot €75 aan voorrijkosten op de offerte verschijnen. Vraag dat vooraf, want het verschil tussen twee offertes zit soms alleen daarin. Woon je aan de rand van {p['gemeente']}, meld dat dan meteen: schilders uit de buurgemeente rekenen soms scherper dan die uit je eigen plaats.</p>"""
            elif variant == 2:
                derde = f"""<h3>Wat de ligging van {p['naam']} betekent</h3>
  <p>{p['naam']} kenmerkt zich door {p['ligging']}. Dat is geen detail: gevels die de meeste wind en regen vangen, verliezen hun verflaag merkbaar eerder dan gevels aan de beschutte kant. Loop bij de opname samen met de schilder rond de woning en let erop dat hij per gevel kijkt in plaats van één prijs voor het geheel te noemen. Een offerte die onderscheid maakt tussen de zwaar belaste en de beschutte zijde, is bijna altijd van iemand die weet wat hij doet.</p>"""
            else:
                derde = f"""<h3>Vraag hier expliciet naar</h3>
  <p>Of je nu in {p['naam']} zit of ergens anders, dit zijn de vragen die het verschil maken tussen een offerte die klopt en een offerte die later duurder uitvalt: hoeveel lagen worden er gerekend, welk verfmerk gebruikt u, wat valt er precies onder de voorbereiding, en wat gebeurt er als er onderweg iets tegenvalt. Een schilder die daar zonder aarzelen antwoord op geeft, is bijna altijd de juiste keuze — ook als hij niet de goedkoopste is.</p>"""

            lokaal = f"""<section class="section"><div class="wrap narrow prose">
  <h2>{d['naam']} in {p['naam']}: wat je moet weten</h2>
  <p>De woningen in {p['naam']} stammen grotendeels uit {p['bouwperiode']}. Het gaat vooral om {p['woningmix']}. Dat bepaalt meer van je offerte dan mensen denken: {'bij dit type woning zit het buitenschilderwerk vooral in kozijnen, boeidelen en dakranden, en dus in bereikbaarheid' if seizoen else 'bij dit type woning gaat het vooral om de hoeveelheid vierkante meters en om hoeveel voorbereiding de ondergrond vraagt'}. {p['hook']}</p>

  <h3>Richtprijs in {p['provincie']}</h3>
  <p>Voor {d['naam'].lower()} in {p['naam']} zie je prijzen tussen <strong>{eur(p_van)} en {eur(p_tot)}</strong> {d['prijs_eenheid']}. {INDEX_TOELICHTING.get(p['provincie'], '')}</p>
  <p>Ligt een offerte daar duidelijk boven, vraag dan om een specificatie per onderdeel. Ligt hij er ver ónder, wees dan juist alert: dat verschil zit meestal niet in de marge maar in het aantal lagen of in voorbereiding die stilzwijgend wordt overgeslagen.</p>

  <h3>Het beste moment om in te plannen</h3>
  <p>{'Buitenwerk kan in ' + p['naam'] + ' van maart tot en met oktober, maar de scherpste prijzen liggen in september en oktober. De piek is dan voorbij en schilders willen hun najaar volmaken. Wacht je tot het voorjaar, dan sta je achter in de rij bij iedereen die de winter heeft afgewacht.' if seizoen else 'Dit werk kan het hele jaar door, en juist daarom loont het om het in de winter te plannen. Tussen november en februari hebben schilders in ' + p['gemeente'] + ' nauwelijks buitenwerk en dus ruimte in de agenda. Je hebt meer keuze én meer onderhandelingsruimte.'}</p>

  {derde}

  <h3>Ook in de buurt</h3>
  <p>Zoek je {d['naam'].lower()} net over de gemeentegrens? Bekijk dan {', '.join(f'<a href="/schilder/{b["slug"]}/{d["slug"]}/">{b["naam"]}</a>' for b in buren)}.</p>
</div></section>"""

            faqs = list(d["faq"]) + [
                (f"Werken jullie schilders ook in {p['naam']}?",
                 f"Ja. We koppelen je alleen aan bedrijven die {p['naam']} in hun werkgebied hebben staan, zodat je geen onnodige voorrijkosten betaalt."),
            ]
            faq_html, faq_ld = faq_blok(faqs, f"Vragen over {d['naam'].lower()} in {p['naam']}")

            andere = f"""<section class="section soft"><div class="wrap">
  <h2>Ander schilderwerk in {p['naam']}</h2>
  {dienst_cards(p['slug'], p['naam'], exclude=d['slug'])}
  <p style="margin-top:22px"><a href="/schilder/{p['slug']}/">Alles over schilders in {p['naam']} →</a></p>
</div></section>"""

            svc_ld = {
                "@context": "https://schema.org",
                "@type": "Service",
                "serviceType": d["naam"],
                "name": f"{d['naam']} in {p['naam']}",
                "provider": {"@id": SITE["url"] + "/#organization"},
                "areaServed": {"@type": "City", "name": p["naam"]},
                "description": f"{d['kort']} in {p['naam']}. Vergelijk gratis offertes van lokale schilders.",
                "offers": {"@type": "AggregateOffer", "priceCurrency": "EUR",
                           "lowPrice": p_van, "highPrice": p_tot},
            }

            body = (cr + body_top + lokaal + faq_html + andere
                    + cta_blok(f"{d['naam']} in {p['naam']} laten doen?",
                               "Eén formulier, maximaal drie offertes van schilders uit de buurt. Gratis en vrijblijvend."))

            write(f"/schilder/{p['slug']}/{d['slug']}/", page(
                title(f"{d['naam']} {p['naam']}: kosten &amp; 3 offertes")
                if len(f"{d['naam']} {p['naam']}") <= 40
                else title(f"{d['naam_kort']} {p['naam']}: kosten &amp; offertes"),
                desc(f"{d['naam']} in {p['naam']} nodig?",
                     f"Richtprijs {eur(p_van)}–{eur(p_tot)} {d['prijs_eenheid']}.",
                     "Vergelijk gratis en vrijblijvend offertes van maximaal 3 lokale schilders.",
                     f"Actief in heel {p['gemeente']}.",
                     "Geen verplichtingen."),
                f"/schilder/{p['slug']}/{d['slug']}/", body, [cr_ld, faq_ld, svc_ld]),
                prio=0.7 if p["prio"] == 1 else 0.5)


# ===========================================================================
# CONVERSIEPAGINA'S
# ===========================================================================

def build_offerte_aanvragen():
    cr, cr_ld = crumbs([("Home", "/"), ("Offertes aanvragen", None)])
    body = f"""{cr}
<section class="section-sm"><div class="wrap">
  <div class="grid g2" style="gap:48px;align-items:start">
    <div>
      <span class="badge">Gratis &amp; vrijblijvend</span>
      <h1>Vraag gratis 3 offertes aan</h1>
      <p class="lead">Vier korte vragen en je bent klaar. Wij zoeken schilders in jouw regio die dit werk doen en op dit moment ruimte hebben.</p>
      <ul class="checklist">
        <li><strong>Kost je niets.</strong> Aanvragen en vergelijken is volledig gratis. Wij worden betaald door de schilders.</li>
        <li><strong>Maximaal drie bedrijven.</strong> Je nummer gaat nooit naar meer partijen.</li>
        <li><strong>Geen verplichting.</strong> Alle drie afwijzen mag, zonder uitleg.</li>
        <li><strong>Alleen naar jouw schilders.</strong> Je gegevens gaan naar maximaal 3 schilders uit jouw regio en naar niemand anders.</li>
      </ul>
      <div class="callout">
        <p><strong>Tip:</strong> hoe concreter je omschrijving, hoe scherper de offertes. Noem het aantal ramen of vierkante meters, wanneer er voor het laatst geschilderd is en of je ergens houtrot of schade ziet. Een foto meesturen kan altijd na het eerste contact.</p>
      </div>
    </div>
    <div>{offerte_form("Start je aanvraag", "Klaar in ongeveer een minuut")}</div>
  </div>
</div></section>
{hoe_werkt_het()}
{cta_blok("Liever eerst weten wat het kost?", "Bekijk het complete prijzenoverzicht met richtprijzen per type schilderwerk.", "Naar het prijzenoverzicht")}"""
    write("/offerte-aanvragen/", page(
        title("Gratis 3 offertes van schilders aanvragen"),
        "Vraag in een minuut gratis offertes aan bij maximaal 3 schilders uit jouw regio. Vrijblijvend en zonder kosten voor jou.",
        "/offerte-aanvragen/", body, [cr_ld]), prio=0.9, freq="weekly")


def build_offerte_vergelijken():
    cr, cr_ld = crumbs([("Home", "/"), ("Offerte laten checken", None)])
    faqs = [
        ("Wat kost het om mijn offerte te laten checken?",
         "Niets. We doen dit omdat het ons helpt de markt scherp te houden en omdat mensen die hun offerte laten checken vaak alsnog een tweede prijs willen opvragen."),
        ("Wordt mijn offerte verstuurd bij de directe check?",
         "Nee. De directe check werkt helemaal in je browser. Ook als je een pdf kiest, wordt die alleen op je eigen apparaat uitgelezen. Alleen als je het formulier gebruikt om je offerte door ons te laten bekijken, ontvangen wij hem."),
        ("Hoe snel krijg ik een reactie?",
         "Doorgaans binnen twee werkdagen. Bij grote of complexe offertes, bijvoorbeeld VvE-onderhoud, kan het iets langer duren."),
        ("Wordt mijn offerte naar de concurrent gestuurd?",
         "Nee. We delen je offerte niet met andere schilders. De beoordeling doen wij op basis van wat we in de markt zien voor vergelijkbaar werk."),
        ("Krijg ik een oordeel over het bedrijf zelf?",
         "We beoordelen de offerte, niet het bedrijf. Wel wijzen we je op signalen in de offerte zelf: ontbrekende posten, vage formuleringen of een garantie die weinig voorstelt."),
    ]
    faq_html, faq_ld = faq_blok(faqs)

    body = f"""{cr}
<section class="section-sm"><div class="wrap">
  <div class="grid g2" style="gap:48px;align-items:start">
    <div>
      <span class="badge">Gratis check</span>
      <h1>Offerte ontvangen? Laat 'm gratis beoordelen</h1>
      <p class="lead" data-check-uit>Je hebt een prijs van een schilder maar geen idee of het klopt. Stuur de offerte naar ons en je krijgt binnen twee werkdagen een eerlijk oordeel.</p>
      <p class="lead" data-check-aan hidden>Je hebt een prijs van een schilder maar geen idee of het klopt. Zet de posten erin, of laat ze uit je pdf halen, en zie direct hoe ze zich verhouden tot de richtprijzen in jouw regio. Je offerte blijft op je eigen computer.</p>
      <h3>Waar we naar kijken</h3>
      <ul class="checklist">
        <li>Is de prijs marktconform voor dit type werk in jouw regio?</li>
        <li>Staat het aantal lagen en het verfmerk erin?</li>
        <li>Zijn steiger-, houtrot- en voorbereidingskosten meegenomen of komen die later?</li>
        <li>Klopt het btw-tarief per post: 9% voor schilderwerk aan een woning ouder dan twee jaar, 21% voor de rest?</li>
        <li>Wat stelt de garantie precies voor?</li>
      </ul>
      <div class="callout">
        <p><strong>Wat we níét doen:</strong> we sturen je offerte niet door naar andere schilders en we bellen je niet plat. Wil je daarna alsnog een tweede prijs, dan kun je zelf een aanvraag starten.</p>
      </div>
    </div>
    <div>
      <div class="formcard" data-offertecheck hidden>
        <h2>Check je offerte direct</h2>
        <p class="sub">Gratis · je offerte blijft op je eigen computer</p>
        <h3 class="oc-stap">1. Laat de posten uitlezen <span class="hint">— mag ook overslaan</span></h3>
        <div class="field" style="margin-bottom:10px">
          <label for="oc-bestand">Offerte als pdf</label>
          <input type="file" id="oc-bestand" name="bestand" accept="application/pdf">
        </div>
        <details class="oc-plak">
          <summary>Of plak de tekst van de offerte</summary>
          <textarea name="tekst" rows="6" aria-label="Tekst van de offerte" placeholder="Bijvoorbeeld:&#10;12 kozijnen schuren en 2x aflakken € 1.680,00&#10;Steiger achtergevel € 450,00&#10;Totaal excl. btw € 2.130,00"></textarea>
        </details>
        <button type="button" class="btn btn-ghost" data-oc-lees>Lees de offerte uit</button>
        <p class="oc-melding" data-oc-melding aria-live="polite"></p>

        <h3 class="oc-stap">2. Controleer de posten</h3>
        <div class="oc-kop"><span>Soort werk</span><span>Aantal</span><span>Bedrag</span><span></span></div>
        <div data-oc-rijen></div>
        <button type="button" class="btn-link" data-oc-plus>+ Post toevoegen</button>
        <div class="oc-btw">
          <span>Bedragen zijn</span>
          <label><input type="radio" name="btwsoort" value="excl" checked> excl. btw</label>
          <label><input type="radio" name="btwsoort" value="incl"> incl. btw</label>
        </div>
        <div class="field" style="margin-top:12px">
          <label for="oc-plaats">Waar woon je?</label>
          <select id="oc-plaats" name="plaats">
            <option value="">Kies je plaats</option>
            {"".join(f'<option value="{PRIJSINDEX.get(p["provincie"], 1.0)}">{p["naam"]}</option>' for p in sorted(PLAATSEN, key=lambda p: p["naam"]))}
            <option value="1">Andere plaats</option>
          </select>
        </div>

        <h3 class="oc-stap">3. Wat staat er in de offerte?</h3>
        <div class="oc-lijst">{"".join(f'<label><input type="checkbox" name="lijst" value="{k}"> {t}</label>' for k, t in [("lagen", "Aantal lagen"), ("merk", "Verfmerk en type"), ("voorbereiding", "Voorbereiding (schuren, ontvetten, kitten)"), ("steiger", "Steiger of hoogwerker"), ("houtrot", "Afrekening van houtrot"), ("garantie", "Garantie"), ("btw", "Btw-tarief"), ("planning", "Planning")])}</div>

        <div class="err" data-oc-fout></div>
        <div class="formnav"><button type="button" class="btn btn-primary" data-oc-check>Bekijk de uitslag</button></div>
        <p class="formfoot">Liever dat een mens meekijkt? <a href="#handcheck" data-oc-hand>Stuur je offerte in</a>.</p>
        <div class="oc-uitslag" data-oc-uitslag hidden></div>
      </div>
      <div class="formcard" id="handcheck" data-handcheck>
        <h2>Stuur je offerte in</h2>
        <p class="sub">Gratis · reactie binnen 2 werkdagen</p>
        <div class="steps"><div class="on"></div><div></div></div>
        <form data-wizard data-table="offerte_checks" novalidate>
          <div class="step active">
            <div class="field">
              <label for="c-oms">Plak hier de belangrijkste regels uit de offerte</label>
              <textarea id="c-oms" name="offerte_tekst" required placeholder="Bijvoorbeeld:&#10;Buitenschilderwerk woning, 12 kozijnen 2-zijdig&#10;Schuren, gronden, 2x aflak Sikkens&#10;Steiger niet inbegrepen&#10;Totaal € 4.850 incl. btw" style="min-height:170px"></textarea>
            </div>
            <div class="row2">
              <div class="field">
                <label for="c-bedrag">Totaalbedrag</label>
                <input type="text" id="c-bedrag" name="bedrag" placeholder="€ 4.850" required>
              </div>
              <div class="field">
                <label for="c-plaats2">Plaats</label>
                <input type="text" id="c-plaats2" name="plaats" placeholder="Almere" required>
              </div>
            </div>
            <div class="err"></div>
            <div class="formnav"><button type="button" class="btn btn-primary" data-next>Volgende</button></div>
          </div>
          <div class="step">
            <div class="field">
              <label for="c-naam">Naam</label>
              <input type="text" id="c-naam" name="naam" required autocomplete="name">
            </div>
            <div class="field">
              <label for="c-mail2">E-mailadres <span class="hint">— hier sturen we de beoordeling naartoe</span></label>
              <input type="email" id="c-mail2" name="email" required autocomplete="email">
            </div>
            <div class="field">
              <label>Wil je er ook vergelijkende offertes bij?</label>
              <div class="choice">
                <label><input type="radio" name="ook_offertes" value="Ja, graag" data-required><span>Ja, graag</span></label>
                <label><input type="radio" name="ook_offertes" value="Nee, alleen de check" data-required><span>Nee, alleen de check</span></label>
              </div>
            </div>
            <div class="err"></div>
            <div class="formnav">
              <button type="button" class="btn btn-ghost" data-prev>Terug</button>
              <button type="submit" class="btn btn-primary" data-submit>Verstuur ter beoordeling</button>
            </div>
            <p class="formfoot">We delen je offerte niet met derden. Zie onze <a href="/privacy/">privacyverklaring</a>.</p>
          </div>
        </form>
        <div class="success">
          <div class="big">{icon('check',26)}</div>
          <h2>Offerte ontvangen</h2>
          <p>We nemen 'm door en mailen je binnen twee werkdagen onze beoordeling.</p>
        </div>
      </div>
    </div>
  </div>
</div></section>
<section class="section soft"><div class="wrap narrow prose">
  <h2>Zo lees je zelf een schildersofferte</h2>
  <p>Voordat je 'm opstuurt, kun je al veel zien. Vaag taalgebruik is het belangrijkste waarschuwingssignaal: wat niet is omschreven, kan later meerwerk worden.</p>
  <div class="tablewrap"><table>
    <thead><tr><th>Vaag</th><th>Duidelijk</th></tr></thead>
    <tbody>
      <tr><td>Kozijnen schilderen</td><td>Welke kozijnen, aan welke kant, en hoeveel stuks</td></tr>
      <tr><td>Goede kwaliteit verf</td><td>Merk, type en glansgraad</td></tr>
      <tr><td>Voorbereiding inbegrepen</td><td>Schuren, ontvetten, plamuren, en waar dat gebeurt</td></tr>
      <tr><td>Houtrot in overleg</td><td>Hoe houtrot wordt vastgesteld en wat het per plek of per uur kost</td></tr>
      <tr><td>Steiger indien nodig</td><td>Steiger of hoogwerker inbegrepen, of met een apart bedrag</td></tr>
      <tr><td>Garantie volgens afspraak</td><td>De termijn, en waar die wel en niet voor geldt</td></tr>
    </tbody>
  </table></div>
  {foto(FOTOS_PAGINA["checken"], "(max-width:760px) calc(100vw - 40px), 720px")}
  <h2>Twee offertes naast elkaar leggen</h2>
  <p>Vergelijk niet alleen het eindbedrag. Zet per offerte op een rij hoeveel lagen er worden gezet, wat er voorbereid wordt en wat er buiten de prijs valt. Is de ene offerte veel goedkoper, zoek dan eerst uit wat er ontbreekt. Pas als de inhoud gelijk is, zegt de prijs iets.</p>
</div></section>
<script>window.TS_PRIJSBANDEN = {json.dumps(PRIJSBANDEN, ensure_ascii=False)};</script>
{faq_html}
{cta_blok("Toch liever direct vergelijken?", "Vraag gratis offertes aan bij maximaal drie schilders en zie zelf hoe de prijzen uiteenlopen.")}"""
    write("/offerte-vergelijken/", page(
        title("Schildersofferte gratis laten checken"),
        "Offerte van een schilder ontvangen? Laat 'm gratis beoordelen. We checken of de prijs marktconform is en welke posten ontbreken. Reactie binnen 2 werkdagen.",
        "/offerte-vergelijken/", body, [cr_ld, faq_ld]), prio=0.8)


def build_voor_schilders():
    cr, cr_ld = crumbs([("Home", "/"), ("Voor schilders", None)])
    dienstopties = "".join(
        f'<label><input type="checkbox" name="diensten" value="{d["naam"]}"><span>{d["naam"]}</span></label>'
        for d in DIENSTEN
    )
    faqs = [
        ("Zit ik vast aan een contract?",
         "Nee. Je betaalt per lead, niet per maand. Wil je een maand pauzeren omdat je agenda vol zit, dan zet je je account op pauze."),
        ("Wat als een lead niet deugt?",
         "Verkeerd nummer, dubbele aanvraag of iemand die duidelijk buiten je werkgebied zit: melden binnen vijf werkdagen en je krijgt de lead gecrediteerd. We houden geen ingewikkelde discussie over 'hij nam niet op' — daar hebben we allebei geen zin in."),
        ("Hoeveel schilders krijgen dezelfde lead?",
         "Maximaal drie, inclusief jij. Bij een exclusieve lead ben jij de enige."),
        ("Kan ik mijn werkgebied begrenzen?",
         "Ja, op plaats- of postcodeniveau. Je kunt ook een maximum instellen op het aantal leads per maand, zodat je niet overspoeld wordt."),
        ("Hoe snel krijg ik een lead binnen?",
         "Direct per e-mail en sms zodra de aanvraag binnenkomt. Snelheid van reageren is in dit spel het verschil tussen wel en niet de opdracht krijgen."),
    ]
    faq_html, faq_ld = faq_blok(faqs, "Vragen van schilders")

    body = f"""{cr}
<section class="section-sm"><div class="wrap">
  <div class="grid g2" style="gap:48px;align-items:start">
    <div>
      <span class="badge">Voor schildersbedrijven</span>
      <h1>Aanvragen uit jouw regio, betaal per lead</h1>
      <p class="lead">Geen maandabonnement, geen opstartkosten. Je betaalt alleen voor de aanvragen die je daadwerkelijk ontvangt, en je bepaalt zelf je werkgebied en je maximum per maand.</p>
      <ul class="checklist">
        <li>Aanvragen uit jouw eigen plaats en omliggende gemeenten</li>
        <li>Maximaal drie schilders per aanvraag — of exclusief, als je dat wilt</li>
        <li>Direct per mail en sms, zodat je als eerste kunt bellen</li>
        <li>Ongeldige leads worden gecrediteerd</li>
        <li>Opzeggen of pauzeren kan per direct</li>
      </ul>
      <p><a class="btn btn-primary btn-lg" href="#aanmelden">Vrijblijvend aanmelden</a></p>
    </div>
    <div id="aanmelden">
      <div class="formcard">
        <h2>Meld je bedrijf aan</h2>
        <p class="sub">We bellen je binnen één werkdag om je werkgebied door te nemen</p>
        <div class="steps"><div class="on"></div><div></div></div>
        <form data-wizard data-table="schilders" novalidate>
          <div class="step active">
            <div class="field">
              <label for="s-bedrijf">Bedrijfsnaam</label>
              <input type="text" id="s-bedrijf" name="bedrijfsnaam" required autocomplete="organization">
            </div>
            <div class="row2">
              <div class="field">
                <label for="s-contact">Contactpersoon</label>
                <input type="text" id="s-contact" name="contactpersoon" required autocomplete="name">
              </div>
              <div class="field">
                <label for="s-kvk">KvK-nummer</label>
                <input type="text" id="s-kvk" name="kvk" required inputmode="numeric">
              </div>
            </div>
            <div class="row2">
              <div class="field">
                <label for="s-mail">E-mailadres</label>
                <input type="email" id="s-mail" name="email" required autocomplete="email">
              </div>
              <div class="field">
                <label for="s-tel">Telefoonnummer</label>
                <input type="tel" id="s-tel" name="telefoon" required autocomplete="tel">
              </div>
            </div>
            <div class="err"></div>
            <div class="formnav"><button type="button" class="btn btn-primary" data-next>Volgende</button></div>
          </div>
          <div class="step">
            <div class="field">
              <label for="s-gebied">In welke plaatsen werk je?</label>
              <input type="text" id="s-gebied" name="werkgebied" required placeholder="Zeewolde, Almere, Harderwijk">
            </div>
            <div class="field">
              <label>Welk werk doe je? <span class="hint">— meerdere mogelijk</span></label>
              <div class="choice">{dienstopties}</div>
            </div>
            <div class="field">
              <label>Hoeveel aanvragen wil je maximaal per maand?</label>
              <div class="choice">
                <label><input type="radio" name="leads_per_maand" value="1-5" data-required><span>1 – 5</span></label>
                <label><input type="radio" name="leads_per_maand" value="6-15" data-required><span>6 – 15</span></label>
                <label><input type="radio" name="leads_per_maand" value="16-30" data-required><span>16 – 30</span></label>
                <label><input type="radio" name="leads_per_maand" value="Zoveel mogelijk" data-required><span>Zoveel mogelijk</span></label>
              </div>
            </div>
            <div class="err"></div>
            <div class="formnav">
              <button type="button" class="btn btn-ghost" data-prev>Terug</button>
              <button type="submit" class="btn btn-primary" data-submit>Aanmelden</button>
            </div>
            <p class="formfoot">Aanmelden is vrijblijvend. Je zit nergens aan vast tot je de eerste lead accepteert.</p>
          </div>
        </form>
        <div class="success">
          <div class="big">{icon('check',26)}</div>
          <h2>Aanmelding ontvangen</h2>
          <p>We bellen je binnen één werkdag om je werkgebied en de eerste leads door te nemen.</p>
        </div>
      </div>
    </div>
  </div>
</div></section>

<section class="section"><div class="wrap narrow prose">
  <h2>Zo werkt het als je je aanmeldt</h2>
  <ol>
    <li><strong>Je meldt je aan</strong> met je bedrijfsgegevens, je werkgebied en het werk dat je doet.</li>
    <li><strong>We bellen je</strong> om je werkgebied en je maximum aantal aanvragen door te nemen.</li>
    <li><strong>Je ontvangt aanvragen</strong> uit jouw gebied, met de omschrijving en de contactgegevens van de aanvrager.</li>
    <li><strong>Jij neemt contact op</strong> en maakt je eigen offerte. De opdracht sluit je rechtstreeks met de klant.</li>
  </ol>
  {foto(FOTOS_PAGINA["schilders"], "(max-width:760px) calc(100vw - 40px), 720px")}
</div></section>

<section class="section soft" id="tarieven"><div class="wrap narrow prose">
  <h2>Wat kost een lead?</h2>
  <p>Je betaalt per aanvraag, en de prijs hangt af van het type werk. Grotere klussen zijn meer waard, dus daar betaal je meer voor. Alle bedragen zijn exclusief btw.</p>
  <div class="tablewrap">
  <table>
    <thead><tr><th>Type aanvraag</th><th>Gedeeld (max. 3)</th><th>Exclusief</th></tr></thead>
    <tbody>
      <tr><td>Binnenschilderwerk / behangen</td><td class="num">€ 22</td><td class="num">€ 44</td></tr>
      <tr><td>Spuitwerk (deuren, keuken)</td><td class="num">€ 26</td><td class="num">€ 52</td></tr>
      <tr><td>Houtrot reparatie</td><td class="num">€ 28</td><td class="num">€ 56</td></tr>
      <tr><td>Buitenschilderwerk woning</td><td class="num">€ 38</td><td class="num">€ 76</td></tr>
      <tr><td>Zakelijk / VvE</td><td class="num">€ 55</td><td class="num">€ 110</td></tr>
    </tbody>
  </table>
  </div>

  <h3 id="exclusief">Exclusieve leads</h3>
  <p>Bij een exclusieve lead krijg jij de aanvraag als enige. Geen concurrentie, geen race om als eerste te bellen. Je betaalt het dubbele, dus reken het voor je eigen bedrijf uit: is je kans op de opdracht bij een exclusieve lead meer dan twee keer zo groot als bij een gedeelde, dan ben je per gewonnen opdracht goedkoper uit. Houd daarom een paar maanden bij hoeveel offertes je wint.</p>

  <div class="callout">
    <p><strong>Eerste drie leads gratis.</strong> We snappen dat je eerst wilt zien wat de kwaliteit is. Meld je aan en de eerste drie aanvragen in je werkgebied kosten je niets. Bevalt het niet, dan stopt het daar.</p>
  </div>

  <h2>Hoe wij aanvragen binnenhalen</h2>
  <p>Via Google. Mensen die zoeken op &quot;schilder Almere&quot; of &quot;kosten buitenschilderwerk&quot; komen op onze pagina's terecht en vragen daar offertes aan. Dat is warme vraag: iemand die actief zoekt, heeft al een klus in gedachten.</p>

  <h2>Wat we van jou verwachten</h2>
  <ul class="checklist">
    <li>Bel of mail binnen één werkdag. Aanvragers vergelijken, en de eerste die belt heeft een enorme voorsprong.</li>
    <li>Geef een nette, gespecificeerde offerte. Dat verhoogt jouw scoringskans én de reputatie van het platform.</li>
    <li>Meld het als een lead niet deugt, dan crediteren we hem.</li>
    <li>Geldige KvK-inschrijving en een aansprakelijkheidsverzekering.</li>
  </ul>
</div></section>
{faq_html}
<section class="section"><div class="wrap">
  <div class="cta">
    <h2>Klaar om aanvragen te ontvangen?</h2>
    <p>Meld je vrijblijvend aan. De eerste drie leads in jouw werkgebied zijn gratis, daarna betaal je alleen voor wat je ontvangt.</p>
    <a class="btn btn-primary btn-lg" href="#aanmelden">Aanmelden als schilder</a>
  </div>
</div></section>"""
    write("/voor-schilders/", page(
        title("Leads voor schilders: betaal per aanvraag"),
        "Ontvang schilderaanvragen uit jouw regio. Geen abonnement, betaal per lead, eerste 3 gratis. Max. 3 schilders per aanvraag of kies voor exclusieve leads.",
        "/voor-schilders/", body, [cr_ld, faq_ld]), prio=0.8)


def kosten_links(d):
    """Links van een dienstpagina naar de kostenpagina's die erbij horen."""
    ks = [k for k in KOSTEN if k["dienst"] == d["slug"]]
    if not ks:
        return ""
    links = " · ".join(f'<a href="/kosten/{k["slug"]}/">Wat kost {k["klus"]}?</a>' for k in ks)
    return f'<p style="font-size:.93rem;margin-top:8px">{links}</p>'


# Plaatsen per provincie die we in de regiotabel van een kostenpagina tonen.
KOSTEN_REGIO = ["almere", "zwolle", "harderwijk", "amersfoort", "hilversum"]


def build_kosten():
    """Kostenpagina's per klus (/kosten/{slug}/) plus een overzicht op /kosten/."""
    plaatsen = {p["slug"]: p for p in PLAATSEN}
    for k in KOSTEN:
        d = next(x for x in DIENSTEN if x["slug"] == k["dienst"])
        cr, cr_ld = crumbs([("Home", "/"), ("Kosten", "/kosten/"), (k["klus"].capitalize(), None)])

        if k["voorbeelden"][0][1] is not None:
            vb_rows = "".join(
                f'<tr><td><strong>{lab}</strong><br><small>{uitleg}</small></td>'
                f'<td class="num">{eur(n * k["van"])} – {eur(n * k["tot"])}</td></tr>'
                for lab, n, uitleg in k["voorbeelden"])
        else:
            vb_rows = "".join(
                f'<tr><td><strong>{lab}</strong></td><td>{uitleg}</td></tr>'
                for lab, n, uitleg in k["voorbeelden"])
        extra_rows = "".join(f'<tr><td>{a}</td><td class="num">{b}</td></tr>' for a, b in k["extra"])

        regio_rows = ""
        for slug in KOSTEN_REGIO:
            p = plaatsen[slug]
            i = PRIJSINDEX.get(p["provincie"], 1.0)
            regio_rows += (f'<tr><td><a href="/schilder/{slug}/{d["slug"]}/">{p["naam"]}</a></td>'
                           f'<td>{p["provincie"]}</td>'
                           f'<td class="num">{eur(round(k["van"] * i))} – {eur(round(k["tot"] * i))}</td></tr>')

        fact = "".join(f"<li>{x}</li>" for x in k["prijsfactoren"])
        tips = "".join(f"<li>{x}</li>" for x in k["tips"])
        uitleg = "".join(f"<h2>{t}</h2><p>{p}</p>" for t, p in k["uitleg"])
        andere = " · ".join(f'<a href="/kosten/{x["slug"]}/">Wat kost {x["klus"]}?</a>'
                            for x in KOSTEN if x is not k)
        fotos = FOTOS.get(d["slug"], {})
        beeld = foto(fotos["sectie"], "(max-width:760px) calc(100vw - 40px), 720px") if fotos else ""
        faq_html, faq_ld = faq_blok(k["faq"], f"Veelgestelde vragen over {k['klus']}")

        body = f"""{cr}
<section class="section-sm"><div class="wrap narrow prose">
  <span class="badge">Richtprijzen {TODAY[:4]}</span>
  <h1>{k['h1']}</h1>
  <p class="lead">{k['intro']}</p>
  <div class="callout">
    <p><strong>Richtprijs:</strong> {eur(k['van'])} – {eur(k['tot'])} {k['eenheid']}, inclusief materiaal en btw. Gemiddeld over Nederland; per regio zie je hieronder het verschil.</p>
  </div>

  <h2>Rekenvoorbeelden</h2>
  <div class="tablewrap"><table>
    <thead><tr><th>Situatie</th><th>Indicatie</th></tr></thead>
    <tbody>{vb_rows}</tbody>
  </table></div>

  <h2>Wat er vaak bij komt</h2>
  <div class="tablewrap"><table>
    <thead><tr><th>Post</th><th>Richtprijs</th></tr></thead>
    <tbody>{extra_rows}</tbody>
  </table></div>

  <h2>Wat bepaalt de prijs?</h2>
  <ul>{fact}</ul>

  {beeld}
  {uitleg}

  <h2>Prijs per regio</h2>
  <p>Schilders in de Randstad rekenen meer dan in Flevoland en Overijssel. Dit is dezelfde richtprijs, gecorrigeerd voor de regio.</p>
  <div class="tablewrap"><table>
    <thead><tr><th>Plaats</th><th>Provincie</th><th>Richtprijs {k['eenheid']}</th></tr></thead>
    <tbody>{regio_rows}</tbody>
  </table></div>
  <p><small>De regiocorrectie is onze eigen inschatting op basis van prijsverschillen tussen provincies. Gebruik hem als ijkpunt, niet als offerte.</small></p>

  <h2>Welke btw betaal je?</h2>
  <p>{k['btw']}</p>

  <h2>Zo bespaar je zonder in te leveren op kwaliteit</h2>
  <ul class="checklist">{tips}</ul>

  <h2>Heb je al een offerte?</h2>
  <p>Leg hem naast deze richtprijzen, of <a href="/offerte-vergelijken/">laat je offerte checken</a>. Meer prijzen vind je op <a href="/prijzen/">wat kost een schilder</a> en op de pagina over <a href="/schilderwerk/{d['slug']}/">{d['naam'].lower()}</a>.</p>
  <p><small>Ook handig: {andere}</small></p>
</div></section>
{faq_html}
{cta_blok(f"Wat kost {k['klus']} bij jou?", "Een richtprijs is een startpunt. Een echte prijs krijg je pas als een schilder naar jouw situatie kijkt. Vraag gratis en vrijblijvend offertes aan.")}"""
        write(f"/kosten/{k['slug']}/", page(title(k["title"]), k["description"],
              f"/kosten/{k['slug']}/", body, [cr_ld, faq_ld]), prio=0.8)

    # overzicht
    cr, cr_ld = crumbs([("Home", "/"), ("Kosten", None)])
    kaarten = "".join(f"""<div class="card">
    <h3><a href="/kosten/{k['slug']}/">Wat kost {k['klus']}?</a></h3>
    <p><strong>{k['kort']}</strong></p>
    <p>{k['description'].split('. ')[1] if k['description'].count('. ') > 1 else ''}</p>
    <p><a href="/kosten/{k['slug']}/">Bekijk de prijzen →</a></p>
  </div>""" for k in KOSTEN)
    body = f"""{cr}
<section class="section-sm"><div class="wrap">
  <div class="narrow prose">
    <h1>Wat kost schilderwerk per klus?</h1>
    <p class="lead">Richtprijzen voor de klussen waar het meest naar wordt gevraagd, met rekenvoorbeelden, prijs per regio en wat er vaak bij komt. Alle prijzen zijn inclusief materiaal en btw.</p>
  </div>
  <div class="grid g3" style="margin-top:28px">{kaarten}</div>
  <div class="narrow prose" style="margin-top:32px">
    <p>Zoek je het uurtarief of prijzen per m²? Kijk op <a href="/prijzen/">wat kost een schilder in {TODAY[:4]}</a>. Heb je al een offerte, <a href="/offerte-vergelijken/">laat hem dan checken</a>.</p>
  </div>
</div></section>
{cta_blok()}"""
    write("/kosten/", page(title("Wat kost schilderwerk? Prijzen per klus"),
          "Richtprijzen per klus: keuken spuiten, trap schilderen en kozijnen schilderen. Met rekenvoorbeelden, prijs per regio en btw-regels.",
          "/kosten/", body, [cr_ld]), prio=0.8)


def build_prijzen():
    cr, cr_ld = crumbs([("Home", "/"), ("Prijzen", None)])
    blokken = ""
    for d in DIENSTEN:
        fact = "".join(f"<li>{x}</li>" for x in d["prijsfactoren"][:3])
        blokken += f"""<h3 id="{d['slug']}">{d['naam']}: {eur(d['prijs_van'])} – {eur(d['prijs_tot'])} {d['prijs_eenheid']}</h3>
<p>{d['prijs_extra']}</p>
<p><strong>Grootste prijsbepalers:</strong></p><ul>{fact}</ul>
<p><a href="/schilderwerk/{d['slug']}/">Alles over {d['naam'].lower()} →</a></p>"""

    faqs = [
        ("Hoeveel rekent een schilder per uur?",
         "In 2026 ligt het gangbare uurtarief tussen €45 en €65 exclusief btw. Een eenmanszaak zit doorgaans aan de onderkant, een bedrijf met personeel en een bedrijfsauto aan de bovenkant. Op offertes zie je dit tarief overigens zelden terug, omdat de meeste schilders per m² of per stuk offreren."),
        ("Klopt het dat ik maar 9% btw betaal?",
         "Voor schilderwerk en de gebruikte materialen wel, als je woning ouder is dan twee jaar. Voor bedrijfspanden en voor werk dat verder gaat dan schilderen geldt 21%."),
        ("Waarom lopen offertes zo ver uiteen?",
         "Meestal door drie dingen: het aantal lagen dat wordt gerekend, hoeveel voorbereiding er is ingecalculeerd, en of houtrot en steiger zijn meegenomen. Een offerte die €1.500 lager is, is vaak niet goedkoper maar minder compleet."),
        ("Is de goedkoopste offerte een slechte keuze?",
         "Niet per se. Een schilder met een gat in zijn planning kan scherp zitten zonder in te leveren op kwaliteit. Maar leg de offertes naast elkaar en check of het verschil in de prijs zit of in de omschrijving."),
        ("Kan ik onderhandelen over de prijs?",
         "Zeker, en het werkt het beste als je flexibel bent in de planning. &quot;Wat als jullie het in november doen?&quot; levert vaak meer op dan simpelweg vragen om korting."),
        ("Zijn voorrijkosten normaal?",
         "Bij grotere klussen zit dat in de prijs. Bij kleine klussen — één deur, een paar kozijnen — rekenen sommige bedrijven €35 tot €75 voorrijkosten. Vraag het vooraf."),
    ]
    faq_html, faq_ld = faq_blok(faqs, "Veelgestelde vragen over schildersprijzen")

    body = f"""{cr}
<section class="section-sm"><div class="wrap narrow prose">
  <span class="badge">Bijgewerkt {TODAY[:7].replace('-', '/')}</span>
  <h1>Wat kost een schilder in 2026?</h1>
  <p class="lead">Het eerlijke antwoord: dat hangt ervan af. Maar met de richtprijzen hieronder weet je binnen twee minuten of een offerte in de goede orde van grootte zit, en welke vragen je moet stellen als dat niet zo is.</p>

  <h2>Uurtarief of vaste prijs?</h2>
  <p>Een schilder rekent gemiddeld <strong>€45 tot €65 per uur exclusief btw</strong>. Toch krijg je zelden een offerte op uurbasis. De meeste bedrijven werken met een prijs per vierkante meter of per stuk, omdat je dan vooraf weet waar je aan toe bent en de schilder het risico van tegenvallers zelf draagt.</p>
  <p>Werken op regie (dus per gewerkt uur) zie je vooral bij klussen waarvan de omvang vooraf onduidelijk is — houtrotherstel is het klassieke voorbeeld. Vraag in dat geval altijd om een maximumbedrag, zodat je niet voor verrassingen komt te staan.</p>

  <h2>Reken het snel even uit</h2>
  <p>Kies je klus en schuif naar de omvang. Je krijgt de bandbreedte die schilders in
  Nederland hiervoor rekenen — geen offerte, wel een ijkpunt waarmee je weet of een
  prijs redelijk is.</p>
  {calculator()}

  <h2>Richtprijzen per type schilderwerk</h2>
  {prijstabel()}

  <p>Prijzen voor een specifieke klus: {" · ".join(f'<a href="/kosten/{k["slug"]}/">wat kost {k["klus"]}</a>' for k in KOSTEN)}.</p>

  <h2>Per klus toegelicht</h2>
  {blokken}

  <h2>Welke btw betaal je?</h2>
  <p>Voor schilderwerk aan een woning die ouder is dan twee jaar geldt <strong>9% btw</strong>, ook over de gebruikte materialen. De twee jaar tellen vanaf het moment dat de woning voor het eerst is gebruikt.</p>
  <div class="tablewrap"><table>
    <thead><tr><th>Onderdeel</th><th>Btw</th></tr></thead>
    <tbody>
      <tr><td>Schilderen van een woning ouder dan twee jaar, met voorbereiding en gebruikte materialen</td><td class="num">9%</td></tr>
      <tr><td>Behangen, voorbereiding en lijm</td><td class="num">9%</td></tr>
      <tr><td>De levering van het behang zelf</td><td class="num">21%</td></tr>
      <tr><td>Houten inzetstukken in kozijnen en het vervangen van onderdorpels</td><td class="num">21%</td></tr>
      <tr><td>Vervangen van ramen, deuren en kozijnen</td><td class="num">21%</td></tr>
      <tr><td>Bedrijfsruimtes en woningen van twee jaar of jonger</td><td class="num">21%</td></tr>
    </tbody>
  </table></div>
  <p><small>Bron: <a href="https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/tarieven_en_vrijstellingen/diensten_9_btw/werkzaamheden_aan_woningen/werkzaamheden_aan_woningen" rel="nofollow noopener">Belastingdienst, btw-tarief werkzaamheden aan woningen</a>, geraadpleegd in november 2026. Is een pand deels woning, dan geldt 9% alleen voor het woongedeelte.</small></p>
  <div class="callout">
    <p><strong>Check dit altijd.</strong> Staat er 21% over schilderwerk aan je woning, vraag dan waarom. Combineert de offerte schilderwerk met ander werk, dan hoort het bedrijf de posten met 9% en 21% te splitsen.</p>
  </div>

  {foto(FOTOS_PAGINA["prijzen"], "(max-width:760px) calc(100vw - 40px), 720px")}

  <h2>Wat een richtprijs niet vertelt</h2>
  <p>Een richtprijs gaat uit van een gewone klus. Je prijs komt hoger uit als de ondergrond slecht is, als er houtrot zit, als het werk moeilijk bereikbaar is of als je een sterke kleurwissel wilt. Hij komt lager uit als de verflaag nog goed is en de schilder makkelijk bij het werk kan. Gebruik een richtprijs dus om te zien of een offerte in de buurt zit, niet als bedrag dat je mag verwachten.</p>

  <h2>Zo bespaar je zonder in te leveren op kwaliteit</h2>
  <ul class="checklist">
    <li><strong>Plan in het laagseizoen.</strong> Buitenwerk in september of oktober, binnenwerk in de winter. Schilders hebben dan ruimte in de agenda en zijn scherper.</li>
    <li><strong>Doe het voorwerk zelf.</strong> Meubels weghalen, vloeren afdekken en plinten aftapen scheelt makkelijk een dagdeel arbeid.</li>
    <li><strong>Combineer klussen.</strong> Binnen- en buitenwerk tegelijk laten doen scheelt opstartkosten en voorrijkosten.</li>
    <li><strong>Vraag drie offertes.</strong> Pas als je prijzen naast elkaar legt, zie je wat redelijk is en wat ontbreekt.</li>
    <li><strong>Wacht niet te lang met buitenwerk.</strong> Een beurt uitstellen tot het hout rot is, verdubbelt de rekening.</li>
  </ul>

  <h2>Hoe je twee offertes eerlijk vergelijkt</h2>
  <p>Leg ze naast elkaar en check per offerte: het aantal lagen, het verfmerk en type, wat er onder voorbereiding valt, of steiger of hoogwerker is inbegrepen, hoe houtrot wordt afgerekend, de btw-splitsing, de garantietermijn en de opleverdatum. Ontbreekt er iets, dan is dat geen detail maar een toekomstige meerprijs.</p>
  <p>Kom je er niet uit? <a href="/offerte-vergelijken/">Laat je offerte gratis door ons checken</a> — je krijgt binnen twee werkdagen een oordeel.</p>
</div></section>
{faq_html}
{cta_blok("Benieuwd wat het bij jou kost?", "Richtprijzen zijn een startpunt. Een echte prijs krijg je pas als een schilder naar jouw situatie kijkt. Vraag gratis drie offertes aan.")}"""
    write("/prijzen/", page(
        title("Wat kost een schilder in 2026? Prijzen per m² en uur"),
        "Actuele schilderprijzen 2026: uurtarief €45–€65, binnenschilderwerk vanaf €10/m², buitenschilderwerk vanaf €90 per kozijn. Inclusief btw-regels en bespaartips.",
        "/prijzen/", body, [cr_ld, faq_ld]), prio=0.9, freq="weekly")


# ===========================================================================
# STATISCHE PAGINA'S
# ===========================================================================

def build_static_pages():
    # --- Over ons ---
    cr, cr_ld = crumbs([("Home", "/"), ("Over ons", None)])
    body = f"""{cr}
<section class="section-sm"><div class="wrap narrow prose">
  <h1>Over Topschilder</h1>
  <p class="lead">Topschilder is opgericht omdat het vinden van een goede schilder onnodig ingewikkeld is. Je belt drie bedrijven, twee bellen niet terug, en de derde noemt een bedrag waar je niets mee kunt vergelijken.</p>

  <h2>Wat we doen</h2>
  <p>Wij verzamelen jouw aanvraag en zetten die door naar maximaal drie schildersbedrijven die in jouw regio werken en het gevraagde type werk daadwerkelijk doen. Zij nemen rechtstreeks contact met je op. Wij zitten daar verder niet tussen: je onderhandelt zelf, je kiest zelf, en de opdracht sluit je rechtstreeks met de schilder.</p>

  <h2>Hoe we geld verdienen</h2>
  <p>Daar doen we niet geheimzinnig over. Schildersbedrijven betalen ons per aanvraag die ze ontvangen. Voor jou als aanvrager is de dienst gratis en er zit geen opslag op de offertes — de schilder rekent zijn normale prijs. Wij hebben er belang bij dat je een goede schilder vindt, want een bedrijf dat structureel slecht werk levert of niet terugbelt, kost ons uiteindelijk klanten.</p>

  <h2>Welke schilders we toelaten</h2>
  <ul class="checklist">
    <li>Geldige inschrijving bij de Kamer van Koophandel</li>
    <li>Aansprakelijkheidsverzekering voor bedrijven</li>
    <li>Aantoonbare ervaring met het type werk waarvoor ze aanvragen ontvangen</li>
    <li>Reactie binnen één werkdag op een doorgestuurde aanvraag</li>
  </ul>
  <p>Bij herhaalde klachten stoppen we de samenwerking. Dat is geen loze belofte maar simpel eigenbelang.</p>

  <h2>Waar we werken</h2>
  <p>We zijn begonnen in Flevoland en de randmeren-regio en breiden gestaag uit richting de Veluwe, de IJsseldelta, Utrecht en het Gooi. <a href="/werkgebied/">Bekijk alle plaatsen</a> waar we op dit moment actief zijn.</p>

  <h2>Contact</h2>
  <p>Vragen, klachten of een suggestie? Mail naar <a href="mailto:{SITE['email']}">{SITE['email']}</a> of ga naar de <a href="/contact/">contactpagina</a>. We reageren doorgaans binnen één werkdag.</p>
</div></section>
{cta_blok()}"""
    write("/over-ons/", page(
        title("Over Topschilder: zo werken we", brand=""),
        "Topschilder koppelt aanvragers aan schilders in hun regio. Lees hoe we werken, welke schilders we toelaten en waarom de dienst voor jou gratis is.",
        "/over-ons/", body, [cr_ld]), prio=0.5)

    # --- Contact ---
    btwregel = f"<br>Btw {SITE['btw']}" if SITE.get("btw") else ""
    cr, cr_ld = crumbs([("Home", "/"), ("Contact", None)])
    body = f"""{cr}
<section class="section-sm"><div class="wrap">
  <div class="grid g2" style="gap:48px;align-items:start">
    <div class="prose">
      <h1>Contact</h1>
      <p class="lead">Een vraag over je aanvraag, een klacht over een schilder of interesse om je bedrijf aan te melden — laat het weten.</p>
      <h3>E-mail</h3>
      <p><a href="mailto:{SITE['email']}">{SITE['email']}</a><br><small>We reageren doorgaans binnen één werkdag.</small></p>
      <h3>Ik zoek een schilder</h3>
      <p>Dat gaat het snelst via het <a href="/offerte-aanvragen/">aanvraagformulier</a>. Je aanvraag komt dan direct bij de juiste bedrijven terecht.</p>
      <h3>Ik ben schilder</h3>
      <p>Kijk op <a href="/voor-schilders/">voor schilders</a> voor de tarieven en meld je daar vrijblijvend aan.</p>
      <h3>Klacht over een schilder</h3>
      <p>Mail ons met je aanvraagnummer en een korte omschrijving. We nemen elke klacht op in het dossier van het betreffende bedrijf en stoppen de samenwerking bij herhaling.</p>
      <h3>Bedrijfsgegevens</h3>
      <p>{SITE['naam']}<br>{SITE['adres']}<br>KvK {SITE['kvk']}{btwregel}</p>
    </div>
    <div>
      <div class="formcard">
        <h2>Stuur een bericht</h2>
        <p class="sub">Reactie binnen één werkdag</p>
        <div class="steps"><div class="on"></div></div>
        <form data-wizard data-table="berichten" novalidate>
          <div class="step active">
            <div class="field">
              <label for="k-naam">Naam</label>
              <input type="text" id="k-naam" name="naam" required autocomplete="name">
            </div>
            <div class="field">
              <label for="k-mail">E-mailadres</label>
              <input type="email" id="k-mail" name="email" required autocomplete="email">
            </div>
            <div class="field">
              <label for="k-ber">Bericht</label>
              <textarea id="k-ber" name="bericht" required></textarea>
            </div>
            <div class="err"></div>
            <div class="formnav"><button type="submit" class="btn btn-primary btn-block" data-submit>Versturen</button></div>
          </div>
        </form>
        <div class="success">
          <div class="big">{icon('check',26)}</div>
          <h2>Bericht verstuurd</h2>
          <p>Bedankt. We reageren doorgaans binnen één werkdag.</p>
        </div>
      </div>
    </div>
  </div>
</div></section>"""
    write("/contact/", page(
        "Contact | Topschilder",
        "Neem contact op met Topschilder: vragen over je offerteaanvraag, een klacht over een aangesloten "
        "schilder of je bedrijf aanmelden. We reageren binnen één werkdag.",
        "/contact/", body, [cr_ld]), prio=0.4)

    # --- Privacy ---
    cr, cr_ld = crumbs([("Home", "/"), ("Privacy", None)])
    body = f"""{cr}
<section class="section-sm"><div class="wrap narrow prose">
  <h1>Privacyverklaring</h1>
  <p><small>Laatst bijgewerkt: {TODAY}</small></p>

  <h2>Wie zijn wij</h2>
  <p>{SITE['naam']}, gevestigd te {SITE['adres']}, KvK {SITE['kvk']}, is verwerkingsverantwoordelijke voor de gegevens die via {SITE['domein']} worden verzameld. Contact: <a href="mailto:{SITE['email']}">{SITE['email']}</a>.</p>

  <h2>Welke gegevens verzamelen we</h2>
  <ul>
    <li><strong>Aanvraaggegevens:</strong> naam, e-mailadres, telefoonnummer, postcode, plaats, type pand en de omschrijving van je klus.</li>
    <li><strong>Technische gegevens:</strong> de pagina waarop je de aanvraag deed, de verwijzende website en eventuele campagneparameters (utm-tags, gclid).</li>
    <li><strong>Schildersgegevens:</strong> bedrijfsnaam, KvK-nummer, contactpersoon, e-mail, telefoon en werkgebied.</li>
  </ul>

  <h2>Waarom en op welke grondslag</h2>
  <p>We verwerken je gegevens om je aanvraag door te sturen naar maximaal drie schildersbedrijven. De grondslag is de uitvoering van de overeenkomst die ontstaat op het moment dat je het formulier verstuurt. Voor het meten van websitegebruik en advertentie-effectiviteit is de grondslag ons gerechtvaardigd belang, dan wel je toestemming waar de wet die vereist.</p>

  <h2>Met wie delen we gegevens</h2>
  <p>Je aanvraaggegevens gaan naar maximaal drie schildersbedrijven die in jouw regio werken. Deze bedrijven betalen ons een vergoeding om je aanvraag te ontvangen. Zij zijn zelfstandig verwerkingsverantwoordelijke voor wat zij daarna met je gegevens doen. <strong>Aan andere partijen geven of verkopen we je gegevens niet</strong> en we gebruiken ze niet voor ongevraagde reclame van derden.</p>
  <p>Daarnaast maken we gebruik van verwerkers voor hosting en dataopslag. Met deze partijen zijn verwerkersovereenkomsten gesloten.</p>
  <h2>Offertecheck</h2>
  <p>De directe offertecheck op onze site werkt helemaal in je browser. De offerte die je kiest of plakt, wordt niet naar ons of naar anderen verstuurd. Alleen als je je offerte via het formulier naar ons stuurt om hem door een mens te laten bekijken, ontvangen wij hem.</p>

  <h2>Hoelang bewaren we gegevens</h2>
  <p>Aanvraaggegevens bewaren we maximaal 24 maanden na je aanvraag, tenzij een langere bewaartermijn wettelijk verplicht is. Gegevens van schildersbedrijven bewaren we zolang de samenwerking loopt en daarna zeven jaar in verband met de fiscale bewaarplicht.</p>

  <h2>Jouw rechten</h2>
  <p>Je hebt recht op inzage, correctie, verwijdering, beperking, bezwaar en dataportabiliteit. Stuur een mail naar <a href="mailto:{SITE['email']}">{SITE['email']}</a> en we reageren binnen vier weken. Ben je het oneens met onze reactie, dan kun je een klacht indienen bij de Autoriteit Persoonsgegevens.</p>

  <h2>Beveiliging</h2>
  <p>De website werkt uitsluitend over een beveiligde verbinding (https). Aanvraaggegevens worden opgeslagen in een database met toegangsbeperking; alleen geautoriseerde medewerkers kunnen leads inzien.</p>

  <h2>Cookies</h2>
  <p>Zie onze <a href="/cookies/">cookieverklaring</a>.</p>
</div></section>"""
    write("/privacy/", page("Privacyverklaring | Topschilder",
                            "Hoe Topschilder omgaat met je persoonsgegevens: wat we verzamelen, met wie we het delen, hoelang we het bewaren en welke rechten je hebt.",
                            "/privacy/", body, [cr_ld]), prio=0.3)

    # --- Fotoverantwoording ---
    cr, cr_ld = crumbs([("Home", "/"), ("Fotoverantwoording", None)])
    e = htmllib.escape
    blokken = ""
    groepen = [("Homepage", [FOTO_HOME]), ("Diensten-overzicht", [FOTOS_PAGINA["diensten"]]), ("Werkgebied", [FOTOS_PAGINA["werkgebied"]]), ("Wat kost het?", [FOTOS_PAGINA["prijzen"]]), ("Offerte laten checken", [FOTOS_PAGINA["checken"]]), ("Voor schilders", [FOTOS_PAGINA["schilders"]])] + [(d["naam"], list(FOTOS[d["slug"]].values())) for d in DIENSTEN if d["slug"] in FOTOS]
    for naam, lijst in groepen:
        blokken += f"<h2>{naam}</h2>"
        for f in lijst:
            sa = " De bewerkte foto valt onder dezelfde licentie." if "SA" in f["licentie"] else ""
            blokken += (f'<p><strong>{e(f["alt"])}</strong><br>'
                        f'Titel: <a href="{e(f["bron"])}" rel="nofollow noopener">{e(f["titel"])}</a> (Wikimedia Commons)<br>'
                        f'Maker: {e(f["maker"])}<br>'
                        f'Licentie: <a href="{e(f["licentie_url"])}" rel="nofollow noopener license">{e(f["licentie"])}</a><br>'
                        f'Bewerking: {e(f["bewerking"])}{sa}</p>')
    body = f"""{cr}
<section class="section-sm"><div class="wrap narrow prose">
  <h1>Fotoverantwoording</h1>
  <p class="lead">De foto's op onze website komen van Wikimedia Commons en zijn niet door ons of door aangesloten schilders gemaakt. Hieronder staat per foto wie hem maakte, onder welke licentie en wat wij eraan veranderden.</p>
  {blokken}
</div></section>"""
    write("/fotoverantwoording/", page("Fotoverantwoording | Topschilder",
                            "Per foto op Topschilder: de maker, de licentie, de bron op Wikimedia Commons en welke bewerkingen wij hebben uitgevoerd.",
                            "/fotoverantwoording/", body, [cr_ld]), prio=0.2)

    # --- Voorwaarden ---
    cr, cr_ld = crumbs([("Home", "/"), ("Algemene voorwaarden", None)])
    body = f"""{cr}
<section class="section-sm"><div class="wrap narrow prose">
  <h1>Algemene voorwaarden</h1>
  <p><small>Laatst bijgewerkt: {TODAY}</small></p>

  <h2>1. Definities</h2>
  <p><strong>Topschilder:</strong> {SITE['naam']}, KvK {SITE['kvk']}. <strong>Aanvrager:</strong> de particulier of onderneming die via de website een aanvraag indient. <strong>Vakman:</strong> het schildersbedrijf dat via Topschilder aanvragen ontvangt.</p>

  <h2>2. Rol van Topschilder</h2>
  <p>Topschilder is uitsluitend een bemiddelend platform. Wij brengen aanvragers en vakmannen met elkaar in contact. Wij zijn geen partij bij de overeenkomst die daarna tussen aanvrager en vakman tot stand komt, voeren zelf geen schilderwerk uit en zijn niet aansprakelijk voor de uitvoering, kwaliteit, planning of prijs van dat werk.</p>

  <h2>3. Voor aanvragers</h2>
  <p>Het indienen van een aanvraag is gratis en vrijblijvend. Je bent niet verplicht een offerte te accepteren. Door een aanvraag in te dienen ga je ermee akkoord dat maximaal drie vakmannen contact met je opnemen via de door jou opgegeven gegevens. Je verklaart dat de opgegeven gegevens juist zijn en dat je bevoegd bent de aanvraag te doen voor het betreffende pand.</p>

  <h2>4. Voor vakmannen</h2>
  <p>De vakman betaalt per ontvangen aanvraag conform de op de website vermelde tarieven. Een aanvraag wordt aan maximaal drie vakmannen verstrekt, tenzij uitdrukkelijk een exclusieve lead is afgenomen. Facturatie geschiedt maandelijks achteraf met een betaaltermijn van veertien dagen.</p>
  <p>De vakman kan een aanvraag binnen vijf werkdagen ter creditering aanbieden indien het opgegeven telefoonnummer of e-mailadres aantoonbaar onjuist is, de aanvraag een duplicaat is, of de aanvraag buiten het overeengekomen werkgebied valt. Het enkele feit dat de aanvrager niet reageert of de opdracht aan een ander gunt, geeft geen recht op creditering.</p>
  <p>De vakman is verplicht te beschikken over een geldige KvK-inschrijving en een bedrijfsaansprakelijkheidsverzekering, en dient binnen één werkdag te reageren op een ontvangen aanvraag. Topschilder kan de samenwerking met onmiddellijke ingang beëindigen bij herhaalde klachten of het niet nakomen van deze verplichtingen.</p>

  <h2>5. Aansprakelijkheid</h2>
  <p>Topschilder spant zich in om aanvragen te koppelen aan geschikte vakmannen, maar geeft geen garantie op het aantal reacties, de kwaliteit van de offertes of de uitvoering van het werk. Aansprakelijkheid van Topschilder is in alle gevallen beperkt tot het bedrag dat de betreffende partij in de drie maanden voorafgaand aan het schadeveroorzakende feit aan Topschilder heeft betaald, en bij aanvragers tot nihil aangezien de dienst kosteloos is.</p>

  <h2>6. Klachten</h2>
  <p>Klachten kunnen worden gemeld via <a href="mailto:{SITE['email']}">{SITE['email']}</a>. Wij nemen elke klacht op in het dossier van het betreffende bedrijf en reageren binnen tien werkdagen.</p>

  <h2>7. Toepasselijk recht</h2>
  <p>Op deze voorwaarden is Nederlands recht van toepassing. Geschillen worden voorgelegd aan de bevoegde rechter in het arrondissement waarin Topschilder is gevestigd, onverminderd het recht van consumenten om zich tot de wettelijk bevoegde rechter te wenden.</p>
</div></section>"""
    write("/voorwaarden/", page("Algemene voorwaarden | Topschilder",
                                "De algemene voorwaarden van Topschilder voor aanvragers en aangesloten schildersbedrijven: "
                                "onze rol als bemiddelaar, leadtarieven, creditering en aansprakelijkheid.",
                                "/voorwaarden/", body, [cr_ld]), prio=0.3)

    # --- Cookies ---
    cr, cr_ld = crumbs([("Home", "/"), ("Cookies", None)])
    body = f"""{cr}
<section class="section-sm"><div class="wrap narrow prose">
  <h1>Cookieverklaring</h1>
  <p><small>Laatst bijgewerkt: {TODAY}</small></p>
  <h2>Wat we gebruiken</h2>
  <p>Topschilder gebruikt zo min mogelijk cookies. Concreet:</p>
  <ul>
    <li><strong>Functionele opslag.</strong> We bewaren in de lokale opslag van je browser de campagneparameters waarmee je op de site bent gekomen (bijvoorbeeld een gclid van Google Ads), zodat we kunnen meten welke advertentie tot een aanvraag heeft geleid. Deze gegevens worden na negentig dagen verwijderd en bevatten geen persoonsgegevens.</li>
    <li><strong>Analytische en advertentiecookies.</strong> Als wij Google Analytics of Google Ads inzetten, plaatsen die diensten cookies. Deze worden pas geplaatst nadat je daarvoor toestemming hebt gegeven.</li>
  </ul>
  <h2>Cookies weigeren of verwijderen</h2>
  <p>Je kunt cookies op elk moment verwijderen via de instellingen van je browser. Het weigeren van analytische of advertentiecookies heeft geen invloed op de werking van de aanvraagformulieren.</p>
  <h2>Vragen</h2>
  <p>Mail naar <a href="mailto:{SITE['email']}">{SITE['email']}</a>. Zie ook onze <a href="/privacy/">privacyverklaring</a>.</p>
</div></section>"""
    write("/cookies/", page("Cookieverklaring | Topschilder",
                            "Welke cookies en lokale opslag Topschilder gebruikt, waarvoor we campagneparameters bewaren "
                            "en hoe je cookies in je browser weigert of verwijdert.",
                            "/cookies/", body, [cr_ld]), prio=0.2)

    # --- Bedankt (voor Ads-conversie tracking, niet indexeren) ---
    body = f"""<section class="section"><div class="wrap narrow center">
  <div class="big" style="width:64px;height:64px;border-radius:50%;background:#e7f7ef;color:var(--green);display:grid;place-items:center;font-size:1.7rem;margin:0 auto 20px">{icon('check',28)}</div>
  <h1>Bedankt voor je aanvraag</h1>
  <p class="lead">We zoeken nu schilders in jouw regio die bij deze klus passen. Je hoort doorgaans binnen één werkdag iets.</p>
  <p><a class="btn btn-primary" href="/prijzen/">Bekijk alvast wat schilderwerk kost</a></p>
</div></section>"""
    write("/bedankt/", page("Bedankt voor je aanvraag | Topschilder",
                            "Je aanvraag is ontvangen.", "/bedankt/", body, noindex=True), index=False)

    # --- 404 ---
    html404 = page("Pagina niet gevonden | Topschilder",
                   "Deze pagina bestaat niet (meer).", "/404/",
                   f"""<section class="section"><div class="wrap narrow center">
  <h1>Deze pagina bestaat niet</h1>
  <p class="lead">Mogelijk is de link verouderd. Probeer het via een van deze routes:</p>
  <p style="margin-top:26px">
    <a class="btn btn-primary" href="/offerte-aanvragen/">Offertes aanvragen</a>
    <a class="btn btn-ghost" href="/werkgebied/">Alle plaatsen</a>
    <a class="btn btn-ghost" href="/prijzen/">Prijzen</a>
  </p>
</div></section>""", noindex=True)
    with open(os.path.join(OUT, "404.html"), "w", encoding="utf-8") as f:
        f.write(html404)


# ===========================================================================
# ASSETS, SITEMAP, ROBOTS
# ===========================================================================

def build_assets():
    """Schrijft CSS, JS en favicon vanuit assets.py naar site/assets/."""
    from assets import STYLE_CSS, APP_JS, CONFIG_JS, FAVICON_SVG

    bestanden = {
        "css/style.css":  STYLE_CSS,
        "js/app.js":      APP_JS,
        "js/config.js":   CONFIG_JS,
        "img/favicon.svg": FAVICON_SVG,
    }
    for pad, inhoud in bestanden.items():
        full = os.path.join(OUT, "assets", pad)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as f:
            f.write(inhoud)

    shutil.copytree(os.path.join(ROOT, "fotos"), os.path.join(OUT, "assets", "fotos"))
    shutil.copytree(os.path.join(ROOT, "vendor"), os.path.join(OUT, "assets", "vendor"))

    # logo en witte variant (base64 in merk_data.py)
    from merk_data import BESTANDEN as MERK
    merkmap = os.path.join(OUT, "assets", "merk")
    os.makedirs(merkmap, exist_ok=True)
    for naam, data in MERK.items():
        with open(os.path.join(merkmap, naam), "w", encoding="utf-8") as f:
            f.write(data)


def build_sitemap():
    urls = "".join(
        f"<url><loc>{SITE['url']}{p}</loc><lastmod>{TODAY}</lastmod>"
        f"<changefreq>{freq}</changefreq><priority>{prio}</priority></url>"
        for p, prio, freq in sorted(set(URLS))
    )
    xml = ('<?xml version="1.0" encoding="UTF-8"?>'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + urls + "</urlset>")
    with open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)

    robots = f"""User-agent: *
Allow: /
Disallow: /bedankt/

Sitemap: {SITE['url']}/sitemap.xml
"""
    with open(os.path.join(OUT, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots)

    # .htaccess voor Apache-hosting (Cloud86, Vimexx, Antagonist e.d.)
    htaccess = """# Topschilder — Apache config
Options -Indexes
ErrorDocument 404 /404.html

<IfModule mod_rewrite.c>
  RewriteEngine On
  # Forceer https
  RewriteCond %{HTTPS} off
  RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
  # Forceer non-www (pas aan als je juist www wilt)
  RewriteCond %{HTTP_HOST} ^www\\.(.+)$ [NC]
  RewriteRule ^(.*)$ https://%1%{REQUEST_URI} [L,R=301]
</IfModule>

<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/css application/javascript image/svg+xml text/xml
</IfModule>

<IfModule mod_expires.c>
  ExpiresActive On
  ExpiresByType text/css "access plus 1 year"
  ExpiresByType application/javascript "access plus 1 week"
  ExpiresByType image/svg+xml "access plus 1 year"
  ExpiresByType text/html "access plus 1 hour"
</IfModule>

<IfModule mod_headers.c>
  Header set X-Content-Type-Options "nosniff"
  Header set Referrer-Policy "strict-origin-when-cross-origin"
</IfModule>
"""
    with open(os.path.join(OUT, ".htaccess"), "w", encoding="utf-8") as f:
        f.write(htaccess)

    # Netlify/Vercel-vriendelijke redirects
    with open(os.path.join(OUT, "_redirects"), "w", encoding="utf-8") as f:
        f.write("/*  /404.html  404\n")

    # --- GitHub Pages ---
    # CNAME koppelt het custom domein. .nojekyll voorkomt dat GitHub de site
    # door Jekyll haalt; die negeert namelijk mappen en bestanden die met een
    # underscore beginnen en dat sloopt je build.
    with open(os.path.join(OUT, "CNAME"), "w", encoding="utf-8") as f:
        f.write(SITE["domein"] + "\n")
    open(os.path.join(OUT, ".nojekyll"), "w").close()


# ===========================================================================

def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT, ignore_errors=True)
    os.makedirs(OUT, exist_ok=True)

    build_home()
    build_diensten_index()
    build_dienst_pages()
    build_werkgebied()
    build_plaats_pages()
    build_plaats_dienst_pages()
    build_offerte_aanvragen()
    build_offerte_vergelijken()
    build_voor_schilders()
    build_prijzen()
    build_kosten()
    build_static_pages()
    build_assets()
    build_sitemap()

    n = sum(len(files) for _, _, files in os.walk(OUT) if True)
    pages = len(URLS)
    print(f"✓ {pages} indexeerbare pagina's gegenereerd in {OUT}")
    print(f"  {len(PLAATSEN)} plaatsen × {len(DIENSTEN)} diensten = {len(PLAATSEN)*len(DIENSTEN)} longtail-pagina's")
    print("  Supabase-koppeling staat in assets.py onder CONFIG_JS.")


if __name__ == "__main__":
    main()
