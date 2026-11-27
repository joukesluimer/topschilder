# -*- coding: utf-8 -*-
"""Plaatscontent op basis van open data (plaats_cijfers.py).

Zet de cijfers per plaats om in leesbare tekst, concreet advies en een staafdiagram.
Wordt gebruikt door build_plaats_pages en build_plaats_dienst_pages in build.py.

Regels:
- Alleen cijfers uit plaats_cijfers.py, met bron en peildatum op de pagina.
- Geen claims over schilders, reviews of projecten.
- Advies volgt uit de cijfers (bouwjaren, monumenten, eigendom), niet uit aannames.
"""

import re

from plaats_cijfers import CIJFERS, META

INSPIRATIE = "/inspiratie/"
ONDERHOUD_INTERVAL = (6, 8)  # jaren tussen buitenbeurten, zoals elders op de site

# Polder- en ontstaansgeschiedenis. Alleen breed gedocumenteerde jaartallen.
POLDER = {
    "noordoostpolder": ("Noordoostpolder", 1942),
    "oostelijk": ("Oostelijk Flevoland", 1957),
    "zuidelijk": ("Zuidelijk Flevoland", 1968),
}
POLDER_VAN = {
    "emmeloord": "noordoostpolder", "marknesse": "noordoostpolder", "nagele": "noordoostpolder",
    "ens": "noordoostpolder", "kraggenburg": "noordoostpolder", "luttelgeest": "noordoostpolder",
    "tollebeek": "noordoostpolder", "bant": "noordoostpolder", "creil": "noordoostpolder",
    "rutten": "noordoostpolder", "espel": "noordoostpolder",
    "lelystad": "oostelijk", "dronten": "oostelijk", "biddinghuizen": "oostelijk", "swifterbant": "oostelijk",
    "almere": "zuidelijk", "zeewolde": "zuidelijk",
}
EXTRA_GESCHIEDENIS = {
    "almere": "De eerste bewoners kwamen in 1976 in Almere Haven wonen; Almere Stad en Almere Buiten volgden in de jaren tachtig.",
    "lelystad": "De eerste bewoners kwamen in 1967.",
    "zeewolde": "De eerste bewoners kwamen in 1984, waarmee Zeewolde een van de jongste gemeenten van Nederland is.",
    "urk": "Urk was eeuwenlang een eiland in de Zuiderzee, tot de Noordoostpolder in 1942 droogviel. Daarom heeft Urk, anders dan de polderdorpen eromheen, een oude kern.",
    "nagele": "Nagele is in de jaren vijftig ontworpen door architecten van de modernistische groepen De 8 en Opbouw, met platte daken en veel groen tussen de woningen.",
}


def _wijknaam(naam):
    """'Wijk 06 Biddinghuizen' -> 'Biddinghuizen' (CBS-nummering weg)."""
    return re.sub(r"^Wijk \d+\s*", "", naam).strip() or naam


def _nl(n):
    return f"{n:,}".replace(",", ".")


def _datum(iso):
    j, m, d = iso.split("-")
    maanden = ["januari", "februari", "maart", "april", "mei", "juni", "juli", "augustus",
               "september", "oktober", "november", "december"]
    return f"{int(d)} {maanden[int(m) - 1]} {j}"


def cijfers(p):
    return CIJFERS.get(p["slug"])


def eigendom(c):
    """CBS-cijfers van de kern als die er zijn, anders van de gemeente: (dict, omschrijving)."""
    k = c.get("cbs_kern")
    if k and k.get("koop_pct") is not None:
        if len(k["wijken"]) == 1:
            return k, f"{k['naam']} (CBS-wijk ‘{_wijknaam(k['wijken'][0])}’)"
        return k, f"{k['naam']} (de {len(k['wijken'])} CBS-wijken die samen de woonplaats vormen)"
    g = c.get("cbs_gemeente") or {}
    return g, f"de gemeente {g.get('naam', '')}"


def _klas(c, label):
    for lab, n, pct in c["bag"]["klassen"]:
        if lab == label:
            return n, pct
    return 0, 0


def _pct(c, *labels):
    return sum(_klas(c, lab)[1] for lab in labels)


def _pct_vanaf(c, jaar):
    """Aandeel woningen (afgerond, %) met bouwjaar >= jaar; jaar moet 1940 of later zijn."""
    b = c["bag"]
    per = b["per_jaar_vanaf_1940"]
    vanaf = sum(per[max(0, jaar - 1940):])
    return int(100 * vanaf / b["woningen"]) if b["woningen"] else 0


def _beurten(jaar):
    """Hoeveel buitenbeurten een woning van dit bouwjaar bij normaal onderhoud ongeveer heeft gehad."""
    leeftijd = int(META["opgehaald"][:4]) - jaar
    return leeftijd // ONDERHOUD_INTERVAL[1], leeftijd // ONDERHOUD_INTERVAL[0]


# ---------------------------------------------------------------- visual
def staafdiagram(c, naam):
    """Horizontaal staafdiagram in HTML/CSS; leesbaar zonder CSS en met schermlezer."""
    klassen = c["bag"]["klassen"]
    hoogste = max(pct for _, _, pct in klassen) or 1
    rijen = "".join(
        f'<li><span class="pc-lab">{lab}</span>'
        f'<span class="pc-bar" aria-hidden="true"><span style="width:{max(pct / hoogste * 100, 0.8 if n else 0):.0f}%"></span></span>'
        f'<span class="pc-val">{pct}%<span class="pc-n"> · {_nl(n)}</span></span></li>'
        for lab, n, pct in klassen)
    return (f'<figure class="pc-fig"><figcaption>Woningen in {naam} naar bouwjaar '
            f'<span class="hint">(aandeel en aantal, BAG)</span></figcaption>'
            f'<ol class="pc-bars">{rijen}</ol></figure>')


# ---------------------------------------------------------------- tekstblokken
def _geschiedenis(p, c):
    slug = p["slug"]
    delen = []
    if slug in POLDER_VAN:
        polder, jaar = POLDER[POLDER_VAN[slug]]
        na = _pct_vanaf(c, jaar + 1)
        aandeel = "zijn vrijwel alle" if na >= 99 else f"is {na}% van de"
        delen.append(f"{p['naam']} ligt in de {polder}, die in {jaar} droogviel. Volgens de BAG {aandeel} woningen hier na {jaar} gebouwd. "
                     f"Daardoor is de woningvoorraad veel gelijkmatiger dan in een oude stad. "
                     f"Hele straten zijn in dezelfde jaren en vaak met dezelfde materialen gebouwd, en komen dus ook tegelijk aan onderhoud toe.")
    if slug in EXTRA_GESCHIEDENIS:
        delen.append(EXTRA_GESCHIEDENIS[slug])
    return " ".join(delen)


def advies_bouwjaren(p, c):
    """Lijst van (kop, tekst) met advies dat volgt uit de bouwjaarverdeling."""
    b = c["bag"]
    naam = p["naam"]
    uit = []
    voor45 = _klas(c, "vóór 1945")[1]
    if voor45 >= 15:
        jaren30 = (f" Een flink deel daarvan, {b['jaren30_pct']}% van alle woningen, is tussen 1920 en 1940 gebouwd: de bekende "
                   f"jaren-30-woningen met roedes, glas-in-lood en veel houtwerk. Kleurcombinaties die daarbij passen vind je bij "
                   f'<a href="{INSPIRATIE}#jaren30">inspiratie voor jaren-30-woningen</a>.') if b["jaren30_pct"] >= 8 else ""
        uit.append(("Veel vooroorlogse woningen",
                    f"{voor45}% van de woningen in {naam} is van vóór 1945.{jaren30} Bij zulke woningen zit er vaak een dik pakket oude verflagen "
                    f"op het hout. In oude lagen kan lood zitten (loodwit was voor buitenwerk pas in 2009 helemaal verboden, volgens OnderhoudNL); een zorgvuldige schilder schuurt die nat of stofarm en ruimt "
                    f"het stof goed op. Reken op meer voorwerk per kozijn dan bij een jonger huis."))
    naoorlogs = _pct(c, "1945–1964", "1965–1974")
    if naoorlogs >= 30:
        voorbeeld = 1960 if _klas(c, "1945–1964")[1] > _klas(c, "1965–1974")[1] else 1970
        n1, n2 = _beurten(voorbeeld)
        link = ("" if p["slug"] in POLDER_VAN else
                f' Ideeën voor dit type huis: <a href="{INSPIRATIE}#jaren70">inspiratie voor jaren-70-woningen</a>.')
        uit.append(("De naoorlogse voorraad",
                    f"{naoorlogs}% van de woningen is gebouwd tussen 1945 en 1975. Een woning uit {voorbeeld} heeft bij een buitenbeurt om de "
                    f"{ONDERHOUD_INTERVAL[0]} tot {ONDERHOUD_INTERVAL[1]} jaar al zo'n {n1} tot {n2} beurten achter de rug. Waar de originele houten "
                    f"kozijnen er nog in zitten, is houtrot in onderdorpels en kozijnhoeken de grootste post. Veel van deze woningen hebben "
                    f"inmiddels kunststof of nieuwe hardhouten kozijnen; vraag de schilder dan alleen te prijzen wat nog echt geschilderd moet worden.{link}"))
    groei = _pct(c, "1975–1984", "1985–1994")
    if groei >= 30:
        n1, n2 = _beurten(1985)
        uit.append(("Woningen uit 1975 tot 1995",
                    f"{groei}% van de woningen in {naam} komt uit de jaren 1975 tot 1995. Die huizen zijn nu 30 tot 50 jaar oud. Een woning uit 1985 "
                    f"heeft bij normaal onderhoud zo'n {n1} tot {n2} buitenbeurten gehad. Het hout is vaak nog gezond, maar kitnaden, "
                    f"onderdorpels en de aansluiting van glaslatten verdienen extra aandacht. Dit is ook de leeftijd waarop eigenaren kiezen: "
                    f"nog een keer goed schilderen of de kozijnen vervangen. Een eerlijke schilder zegt het als vervangen verstandiger is."))
    jong = b["vanaf_2005_pct"]
    if jong >= 20:
        uit.append(("Veel jonge woningen",
                    f"{jong}% van de woningen is in 2005 of later gebouwd. Daar zijn de kozijnen meestal in de fabriek gegrond en afgelakt. "
                    f"De eerste echte buitenbeurt komt na zes tot acht jaar, dus de woningen uit de jaren 2015 tot 2019 zijn daar nu aan toe. "
                    f"Binnen gaat het in nieuwbouw vaak om het sauzen van kale wanden en plafonds. "
                    f'Kleurideeën: <a href="{INSPIRATIE}#nieuwbouw">inspiratie voor nieuwbouw</a>.'))
    if p["slug"] in POLDER_VAN:
        uit.append(("Polderwoningen",
                    f"Op de open polder vangen gevels veel wind en regen, vooral op de west- en zuidkant. Laat de schilder per gevel kijken: de "
                    f"beschutte kant kan vaak een jaar langer mee. Kleurcombinaties voor dit type huis staan bij "
                    f'<a href="{INSPIRATIE}#polder">inspiratie voor polderwoningen</a>.'))
    return uit


def monumenten_telling(c):
    """(gebouwde rijksmonumenten, archeologische rijksmonumenten)."""
    arch = c.get("rijksmonumenten_archeologisch", 0)
    return c.get("rijksmonumenten", 0) - arch, arch


_ARCH_UITLEG = {True: "in de polder meestal scheepswrakken en andere vindplaatsen in de bodem",
                False: "zoals grafheuvels en andere vindplaatsen in de bodem"}


def advies_monumenten(p, c):
    n, arch = monumenten_telling(c)
    gez = c.get("beschermde_gezichten") or []
    if not n and not gez and not arch:
        return None
    zinnen = []
    if n:
        zinnen.append(f"In {p['naam']} staan {_nl(n)} gebouwde rijksmonumenten" if n > 1
                      else f"In {p['naam']} staat één gebouwd rijksmonument")
    if gez:
        lijst = " en ".join([", ".join(gez[:-1]), gez[-1]] if len(gez) > 1 else gez)
        soort = ("een rijksbeschermd stads- of dorpsgezicht" if len(gez) == 1
                 else f"{['', '', 'twee', 'drie', 'vier'][min(len(gez), 4)] or len(gez)} rijksbeschermde stads- en dorpsgezichten")
        zinnen.append(("en " if n else f"{p['naam']} heeft ") + f"{soort} ({lijst})")
    tekst = (" ".join(zinnen) + ". ") if zinnen else ""
    if arch:
        tekst += (f"Daarnaast {'zijn er' if arch > 1 else 'is er'} {_nl(arch)} archeologische rijksmonument{'en' if arch > 1 else ''}, "
                  f"{_ARCH_UITLEG[p['slug'] in POLDER_VAN]}; die raken je schilderwerk niet. ")
    if n >= 10 or gez:
        tekst += ("Aan een rijksmonument mag je onderhoud doen zonder vergunning zolang het uiterlijk niet verandert. Een andere kleur, "
                  "een ander verfsysteem of het vervangen van historische onderdelen is wél een wijziging, en daarvoor heb je vaak een "
                  f"omgevingsvergunning nodig. In een beschermd gezicht stelt de gemeente {p['gemeente']} de regels in het omgevingsplan. "
                  "Vraag het vooraf na, en kies een schilder die met oud hout en bijvoorbeeld lijnolieverf kan werken. "
                  f'Kleuren die passen bij oude panden vind je bij <a href="{INSPIRATIE}#monument">inspiratie voor monumenten</a>.')
    elif n:
        tekst += ("Woon je in een van die panden, overleg dan vóór een kleurwijziging met de gemeente: veranderen aan een rijksmonument "
                  "kan een omgevingsvergunning vragen.")
    return tekst.strip()


def advies_eigendom(p, c):
    e, waar = eigendom(c)
    if e.get("koop_pct") is None:
        return None
    t = (f"In {waar} is {e['koop_pct']}% van de woningen een koopwoning, {e['corporatie_pct']}% een huurwoning van een corporatie en "
         f"{e['overige_huur_pct']}% een huurwoning van een andere verhuurder. {e['eengezins_pct']}% is een eengezinswoning, "
         f"{e['meergezins_pct']}% een appartement of andere meergezinswoning. ")
    if e["meergezins_pct"] >= 30:
        t += ("Bij zoveel appartementen loopt veel buitenschilderwerk via een VvE en het meerjarenonderhoudsplan. Als bewoner regel je dan "
              "vooral het binnenwerk zelf. ")
    if e["corporatie_pct"] >= 30:
        t += ("Huur je van een corporatie, dan is buitenschilderwerk meestal haar zaak; binnen schilderen en behangen doe je zelf of laat je zelf doen. ")
    if e["eengezins_pct"] >= 75:
        t += "Bijna alles is een eengezinswoning: buitenwerk regel je als eigenaar zelf, en dan loont het om meerdere offertes te vergelijken."
    return t.strip()


def wijk_tabel(p, c):
    wijken = c.get("wijken") or []
    soort = "Wijk"
    if len(wijken) < 3 and len(c.get("buurten") or []) >= 3:  # seo-ronde 4: middelgrote plaatsen per buurt
        wijken, soort = c["buurten"], "Buurt"
    if len(wijken) < 3:
        return ""
    rijen = "".join(f"<tr><td>{_wijknaam(w['naam'])}</td><td class=\"num\">{_nl(w['woningen'])}</td>"
                    f"<td class=\"num\">{w['mediaan_bouwjaar']}</td><td class=\"pc-groep\">{w['dominant']}</td></tr>" for w in wijken)
    oudst, jongst = wijken[0], wijken[-1]
    return f"""<h3>Bouwjaren per {soort.lower()}</h3>
  <p>Binnen {p['naam']} verschilt het flink. In {_wijknaam(oudst['naam'])} is de helft van de woningen van vóór {oudst['mediaan_bouwjaar']}, in {_wijknaam(jongst['naam'])} van na {jongst['mediaan_bouwjaar']}. Het mediane bouwjaar is het jaar waarvoor en waarna evenveel woningen zijn gebouwd.</p>
  <div class="tablewrap"><table class="pc-wijken"><thead><tr><th scope="col">{soort} (CBS)</th><th scope="col" class="num">Woningen</th><th scope="col" class="num">Mediaan bouwjaar</th><th scope="col" class="pc-groep">Grootste groep</th></tr></thead><tbody>{rijen}</tbody></table></div>"""


def bronnen(c, met_wijken=False):
    datum = _datum(META["opgehaald"])
    delen = [f"bouwjaren: Basisregistratie Adressen en Gebouwen (Kadaster), via PDOK, stand {datum}; het bouwjaar is dat van het pand",
             "eigendom en woningtype: CBS, Kerncijfers wijken en buurten 2024 (CC BY 4.0)"]
    if met_wijken:
        delen.append("wijkgrenzen: CBS Wijk- en buurtkaart 2024 (CC BY 4.0)")
    if c.get("rijksmonumenten") or c.get("beschermde_gezichten"):
        delen.append("rijksmonumenten: Rijksmonumentenregister en geodata van de Rijksdienst voor het Cultureel Erfgoed (CC BY 4.0), "
                     f"geraadpleegd {datum}, geteld op adres in de woonplaats of ligging binnen de woonplaatsgrens; "
                     "beschermde gezichten: RCE (CC BY 4.0)")
    return f'<p class="pc-bron"><small>Bronnen: {"; ".join(delen)}. Bewerking en telling: Topschilder.</small></p>'


def woningen_intro(p, c):
    b = c["bag"]
    dom_n, dom_pct = _klas(c, b["dominant"])
    return (f"Volgens de BAG staan er in {p['naam']} {_nl(b['woningen'])} woningen. De helft daarvan is gebouwd vóór "
            f"{b['mediaan_bouwjaar']}, de andere helft daarna. De grootste groep komt uit de periode {b['dominant']}: "
            f"{_nl(dom_n)} woningen, {dom_pct}% van het totaal.")


def rangorde(p):
    """Zin over waar de plaats staat tussen alle plaatsen in het werkgebied, op mediaan bouwjaar."""
    med = {s: c["bag"]["mediaan_bouwjaar"] for s, c in CIJFERS.items()}
    eigen, n = med[p["slug"]], len(med)
    ouder = sum(1 for v in med.values() if v < eigen)
    jonger = sum(1 for v in med.values() if v > eigen)
    gedeeld = " (gedeeld)" if sum(1 for v in med.values() if v == eigen) > 1 else ""
    if ouder <= jonger:
        return f"Daarmee staat {p['naam']} op plek {ouder + 1}{gedeeld} van de {n} plaatsen in ons werkgebied met de oudste woningen."
    return f"Daarmee staat {p['naam']} op plek {jonger + 1}{gedeeld} van de {n} plaatsen in ons werkgebied met de jongste woningen."


# ---------------------------------------------------------------- plaatspagina
def plaats_sectie(p):
    """Volledige sectie 'woningen in cijfers' voor /schilder/{plaats}/. Leeg als er geen cijfers zijn."""
    c = cijfers(p)
    if not c:
        return ""
    gesch = _geschiedenis(p, c)
    adv = "".join(f"<h3>{k}</h3><p>{t}</p>" for k, t in advies_bouwjaren(p, c))
    mon = advies_monumenten(p, c)
    eig = advies_eigendom(p, c)
    wijk = wijk_tabel(p, c)
    kosten = ('<p>Wat dit in euro\'s betekent, lees je bij <a href="/kosten/kozijnen-schilderen/">wat kozijnen schilderen kost</a> '
              'en <a href="/kosten/huis-schilderen/">wat een huis buiten schilderen kost</a>. Wil je weten wat er bij jouw huis nu speelt, '
              'doe dan de <a href="/onderhoudscheck/">onderhoudscheck</a>.</p>')
    return f"""<section class="section" id="woningen-in-cijfers"><div class="wrap narrow prose">
  <h2>De woningen in {p['naam']} in cijfers</h2>
  <p>{woningen_intro(p, c)}{(' ' + gesch) if gesch else ''}</p>
  {staafdiagram(c, p['naam'])}
  <h3>Wat dat betekent voor je schilderwerk</h3>
  {adv}
  {f'<h3>Monumenten</h3><p>{mon}</p>' if mon else ''}
  {f'<h3>Koop, huur en appartementen</h3><p>{eig}</p>' if eig else ''}
  {wijk}
  {kosten}
  {bronnen(c, met_wijken=bool(wijk))}
</div></section>"""


# ---------------------------------------------------------------- plaats-dienstpagina
def dienst_blok(d, p):
    """Eén blok met cijfers die specifiek zijn voor deze dienst in deze plaats."""
    c = cijfers(p)
    if not c:
        return ""
    b = c["bag"]
    naam, slug = p["naam"], d["slug"]
    voor45 = _klas(c, "vóór 1945")[1]
    naoorlogs = _pct(c, "1945–1964", "1965–1974")
    groei = _pct(c, "1975–1984", "1985–1994")
    jong = b["vanaf_2005_pct"]
    e, waar = eigendom(c)
    n_mon, _ = monumenten_telling(c)
    gez = c.get("beschermde_gezichten") or []
    zinnen = [f"{naam} telt volgens de BAG {_nl(b['woningen'])} woningen, met als mediaan bouwjaar {b['mediaan_bouwjaar']}. {rangorde(p)}"]

    if slug == "buitenschilderwerk":
        n1, n2 = _beurten(b["mediaan_bouwjaar"])
        zinnen.append(f"Een woning uit {b['mediaan_bouwjaar']} heeft bij een beurt om de zes tot acht jaar al zo'n {n1} tot {n2} buitenbeurten gehad.")
        if voor45 >= 15:
            zinnen.append(f"{voor45}% is van vóór 1945: veel houtwerk, roedes en oude verflagen, dus meer voorwerk per kozijn.")
        if groei >= 30:
            zinnen.append(f"{groei}% komt uit 1975 tot 1995; daar zijn kitnaden en onderdorpels de aandachtspunten.")
        if jong >= 20:
            zinnen.append(f"{jong}% is van 2005 of later; die kozijnen zijn in de fabriek afgelakt en krijgen hun eerste beurt na zes tot acht jaar.")
        if e.get("meergezins_pct") is not None and e["meergezins_pct"] >= 30:
            zinnen.append(f"In {waar} is {e['meergezins_pct']}% een appartement; daar loopt buitenwerk meestal via de VvE.")
    elif slug == "houtrot-reparatie":
        oud = voor45 + naoorlogs
        zinnen.append(f"{oud}% van de woningen is van vóór 1975. Juist bij die leeftijd zitten er vaak nog originele houten kozijnen in, "
                      f"en daar ontstaat houtrot het eerst: in onderdorpels, kozijnhoeken en de onderkant van deuren.")
        if groei >= 30:
            zinnen.append(f"Daarnaast is {groei}% gebouwd tussen 1975 en 1995; na dertig jaar of meer kan ook daar vocht achter kapotte kitnaden zijn gekropen.")
        if jong >= 40:
            zinnen.append(f"Met {jong}% woningen van na 2005 komt houtrot hier minder voor dan in een oudere plaats; een kleine reparatie is dan vaak genoeg.")
    elif slug == "binnenschilderwerk":
        if voor45 >= 15:
            zinnen.append(f"{voor45}% is van vóór 1945: hoge plafonds, oude pleisterlagen en soms scheve muren vragen meer voorwerk.")
        if groei >= 30:
            zinnen.append(f"{groei}% komt uit 1975 tot 1995, toen spachtelputz en structuurplafonds veel werden toegepast; wie strak wil, laat eerst glad stucen.")
        if jong >= 20:
            zinnen.append(f"{jong}% is van 2005 of later; daar is het eerste werk vaak het sauzen van kale wanden, met een extra voorstrijklaag.")
        if naoorlogs >= 30:
            zinnen.append(f"{naoorlogs}% is gebouwd tussen 1945 en 1975; onder de verf zit daar soms nog behang of oude olieverf op houtwerk. Een schilder test dan eerst of nieuwe verf hecht.")
    elif slug == "spuitwerk":
        delen = [f"{groei}% uit 1975 tot 1995" if groei else "", f"{naoorlogs}% uit 1945 tot 1975" if naoorlogs else ""]
        zinnen.append(f"Van de woningen komt {' en '.join(x for x in delen if x)}. In woningen van die leeftijd zitten vaak "
                      "nog de originele binnendeuren en kozijnen, met meerdere lagen kwastverf. Spuiten geeft dan een strak resultaat, mits de "
                      "oude lagen goed geschuurd en ontvet worden.")
        if jong >= 20:
            zinnen.append(f"In de {jong}% woningen van 2005 of later gaat spuitwerk vaker over kale wanden en plafonds (latex spuiten).")
    elif slug == "behangen":
        if voor45 + naoorlogs >= 40:
            zinnen.append(f"{voor45 + naoorlogs}% is van vóór 1975. In die woningen zit vaak nog oud behang, soms in meerdere lagen of overgeschilderd; "
                          "het verwijderen daarvan is een aparte post op de offerte.")
        else:
            zinnen.append(f"Met {groei + jong}% woningen van 1975 of later zijn de wanden meestal vlakker; vliesbehang kan dan vaak direct op de "
                          "voorbehandelde wand, wat scheelt in arbeid.")
    elif slug == "zakelijk-schilderwerk":
        if e.get("corporatie_pct") is not None:
            zinnen.append(f"In {waar} is {e['corporatie_pct']}% van de woningen van een corporatie en {e['meergezins_pct']}% een meergezinswoning. "
                          "Corporaties en VvE's besteden hun schilderwerk meestal uit volgens een meerjarenonderhoudsplan, met een vaste cyclus per complex.")
        if n_mon:
            zinnen.append(f"Er {'staan' if n_mon > 1 else 'staat'} {_nl(n_mon)} gebouwd{'e' if n_mon > 1 else ''} rijksmonument{'en' if n_mon > 1 else ''} in {naam}; voor bedrijfspanden in een monument gelden dezelfde vergunningsregels als voor woningen.")

    if slug in ("buitenschilderwerk", "houtrot-reparatie") and (n_mon >= 10 or gez):
        delen = []
        if n_mon:
            delen.append(f"{_nl(n_mon)} gebouwde rijksmonumenten" if n_mon > 1 else "één gebouwd rijksmonument")
        if gez:
            delen.append((f"een beschermd gezicht ({gez[0]})" if len(gez) == 1
                          else f"{len(gez)} beschermde gezichten ({', '.join(gez)})"))
        zinnen.append(f"Let op: {naam} heeft {' en '.join(delen)}. Een kleurwijziging of het vervangen van historisch hout "
                      "kan daar een vergunning vragen.")

    if len(zinnen) < 2:
        return ""
    meer = f'<a href="/schilder/{p["slug"]}/#woningen-in-cijfers">alle woningcijfers van {naam}</a>'
    return (f"<h3>{d['naam']} en de woningen in {naam}</h3><p>{' '.join(zinnen)}</p>"
            f"<p>Meer achtergrond, met een grafiek van de bouwjaren: {meer}.</p>"
            + bronnen(c))


def bouwperiode_zin(p):
    """Eén zin over de bouwperiode: uit de BAG als die er is, anders de handgeschreven omschrijving."""
    c = cijfers(p)
    if not c:
        return f"Het gros van de woningen in {p['naam']} is gebouwd {p['bouwperiode']}."
    b = c["bag"]
    _, pct = _klas(c, b["dominant"])
    return (f"De grootste groep woningen in {p['naam']} is gebouwd in de periode {b['dominant']} ({pct}%), "
            f"en de helft van alle woningen is van vóór {b['mediaan_bouwjaar']} (BAG).")
