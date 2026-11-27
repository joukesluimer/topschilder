# -*- coding: utf-8 -*-
"""Content-ronde 5: geldpagina's verdiept.

- Drie nieuwe kostenpagina's: buitenschilderwerk, binnenschilderwerk en houtrot herstellen.
- Verdieping voor kozijnen-schilderen, schilderen-per-m2 en huis-schilderen (UITBREIDING_R5).
- Extra inhoud voor het overzicht /kosten/ (KOSTEN_OVERZICHT).

Elke pagina krijgt een direct antwoord, een prijstabel met bron en peildatum,
valkuilen in offertes met een link naar de offertechecker, en een uitgebreide FAQ.
Prijzen zijn richtprijzen inclusief materiaal en btw (9% voor schilderwerk aan een woning
ouder dan twee jaar), tenzij anders vermeld. Bronnen geopend op 27 november 2026.

Dit bestand importeert niets uit kosten_data.py, zodat build.py en kosten_data.py het
allebei kunnen importeren zonder kringverwijzing.
"""

PEILDATUM = "november 2026"

# Bronnen (allemaal geopend op 27 november 2026)
HOMEDEAL_BUITEN = ("Homedeal, Buitenschilder kosten (2026)", "https://www.homedeal.nl/schilderwerk/buitenschilder-kosten/")
HOMEDEAL_SCHILDER = ("Homedeal, Schilder kosten (2026)", "https://www.homedeal.nl/schilderwerk/schilder-kosten/")
HOMEDEAL_KOZIJN = ("Homedeal, Kozijnen schilderen prijs (2026)", "https://www.homedeal.nl/schilderwerk/kozijnen-schilderen-prijs/")
HOMEDEAL_REPAREREN = ("Homedeal, Houten kozijnen repareren (17 juni 2026)", "https://www.homedeal.nl/kozijnen/houten-kozijnen-repareren/")
DSC_BUITEN = ("De Schilderscombinatie, Wat kost een buitenschilder (2026)", "https://www.deschilderscombinatie.nl/blog/wat-kost-een-buitenschilder/")
ZOOFY_BINNEN = ("Zoofy, Kosten binnenschilderwerk (bijgewerkt 22 juli 2026)", "https://zoofy.nl/prijsgidsen/kosten-binnenschilderwerk/")
SLIMSTER_HOUTROT = ("Slimster, Houtrot repareren (16 april 2026)", "https://slimster.nl/schilder/houtrot-repareren/")
BD_SCHILDEREN = ("Belastingdienst, 9% btw op schilderen van woningen",
                 "https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/tarieven_en_vrijstellingen/diensten_9_btw/werkzaamheden_aan_woningen/schilderen")

CHECKER = '<a href="/offerte-vergelijken/">offertechecker</a>'


def _a(bron):
    lab, url = bron
    return f'<a href="{url}" rel="nofollow noopener">{lab.split(",")[0]}</a>'


def _bronregel(bronnen, extra=""):
    items = "; ".join(f'<a href="{u}" rel="nofollow noopener">{lab}</a>' for lab, u in bronnen)
    return (f'<p><small>Bronnen: {items}. Geraadpleegd in {PEILDATUM}. {extra}'
            'De richtprijzen van Topschilder zijn indicaties, geen vaste prijzen.</small></p>')


def _tabel(kop, rijen, num_vanaf=1):
    th = "".join(f"<th>{k}</th>" for k in kop)
    tr = ""
    for r in rijen:
        tr += "<tr>" + "".join(
            (f'<td class="num">{c}</td>' if i >= num_vanaf else f"<td>{c}</td>") for i, c in enumerate(r)) + "</tr>"
    return f'<div class="tablewrap"><table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'


# ---------------------------------------------------------------------------
# Helpers die build_kosten aanroept (alleen actief als het veld bestaat)
# ---------------------------------------------------------------------------

def kosten_r5_kop(k):
    """Direct antwoord en prijstabel bovenaan de inhoud van een kostenpagina."""
    out = ""
    if k.get("direct"):
        out += f'<div class="callout"><p><strong>Kort antwoord:</strong> {k["direct"]}</p></div>'
    if k.get("prijstabel"):
        titel, html = k["prijstabel"]
        out += f'<h2 id="prijstabel">{titel}</h2>{html}'
    return out


def kosten_r5_valkuilen(k):
    """Sectie 'Valkuilen in offertes' met link naar de offertechecker."""
    if not k.get("valkuilen"):
        return ""
    items = "".join(f"<li>{x}</li>" for x in k["valkuilen"])
    return (f'<h2 id="valkuilen">Valkuilen in offertes voor {k["klus"].removeprefix("een ")}</h2>'
            f'<p>Deze fouten zien we het vaakst. Ze maken een offerte goedkoper op papier, maar duurder in de praktijk.</p>'
            f'<ul class="checklist">{items}</ul>'
            f'<p>Twijfel je over een offerte? Plak hem in de gratis {CHECKER}. Die legt elke post naast de richtprijzen en laat zien wat er ontbreekt.</p>')


# ---------------------------------------------------------------------------
# 1. Kosten buitenschilderwerk
# ---------------------------------------------------------------------------

_BUITEN = {
    "slug": "buitenschilderwerk",
    "klus": "buitenschilderwerk",
    "kruimel": "Buitenschilderwerk",
    "h1": "Kosten buitenschilderwerk 2026: prijs per onderdeel en per woning",
    "title": "Kosten buitenschilderwerk 2026: prijs per m² en per woning",
    "description": "Buitenschilderwerk kost €30 tot €45 per m² houtwerk, of €1.500 tot €3.450 voor een tussenwoning. Met prijzen per kozijn, deur, boeideel en steiger.",
    "dienst": "buitenschilderwerk",
    "eenheid": "per m² houtwerk buiten",
    "van": 30,
    "tot": 45,
    "kort": "€30 – €45 per m² houtwerk",
    "intro": "Buitenschilderwerk is het schilderen van alles wat buiten aan je huis van hout is: kozijnen, ramen, deuren, boeidelen en soms een dakkapel of gevel. Een schilder rekent per onderdeel of per m² houtwerk. Hieronder zie je per onderdeel wat het kost, wat je voor je woningtype kwijt bent en waar je op let in de offerte.",
    "direct": "Buitenschilderwerk kost gemiddeld <strong>€30 tot €45 per m² houtwerk</strong>, inclusief verf en 9% btw. Per onderdeel: een buitenkozijn €90 tot €190, een buitendeur €100 tot €185 en boeidelen €25 tot €55 per meter. Voor de hele buitenkant van een <strong>tussenwoning</strong> betaal je €1.500 tot €3.450, voor een <strong>vrijstaande woning</strong> €3.250 tot €7.200. Houtrot en een steiger komen er vaak bij.",
    "prijstabel": ("Prijzen buitenschilderwerk per onderdeel (peildatum november 2026)",
        _tabel(["Onderdeel", "Topschilder", "Homedeal", "De Schilderscombinatie"], [
            ["Houtwerk per m²", "€30 – €45", "€25 – €45", "€35 – €45"],
            ["Buitenkozijn met raam", "€90 – €190 per kozijn", "€250 – €500 per raam", "–"],
            ["Voor- of achterdeur", "€100 – €185", "€100 – €300", "€250 – €550 incl. deurpost"],
            ["Boeidelen en windveren", "€25 – €55 per meter", "–", "–"],
            ["Dakkapel", "€400 – €950", "€400 – €1.500", "€500 – €1.200"],
            ["Gevel (stucwerk of eerder geschilderd)", "€20 – €40 per m²", "€15 – €25 per m²", "€25 – €40 per m²"],
            ["Steiger of hoogwerker", "€300 – €900 per gevel", "–", "–"],
            ["Houtrot herstellen", "€50 – €275 per plek", "–", "–"],
        ])
        + _bronregel([HOMEDEAL_BUITEN, DSC_BUITEN], "Alle bedragen inclusief verf en btw, zoals de bronnen ze noemen. ")),
    "voorbeelden": [
        ("Tussenwoning, voor- en achtergevel", None, "€1.500 – €3.450. Acht kozijnen, twee deuren, 12 meter boeidelen en een steiger achter."),
        ("Hoekwoning of twee-onder-een-kap", None, "€2.100 – €4.650. Twaalf kozijnen, twee deuren, 20 meter boeidelen en een steiger."),
        ("Vrijstaande woning", None, "€3.250 – €7.200. Achttien kozijnen, drie deuren, een dakkapel, 25 meter boeidelen en een steiger."),
        ("Alleen de kozijnen beneden", None, "€360 – €760. Vier kozijnen op de begane grond, zonder steiger."),
    ],
    "extra": [
        ("Steiger of hoogwerker voor de bovenverdieping", "€300 – €900 per gevel"),
        ("Houtrot herstellen", "€50 – €275 per reparatieplek"),
        ("Glaslatten vervangen", "€8 – €20 per meter (eigen inschatting)"),
        ("Oude kitvoegen vervangen", "€6 – €15 per meter (eigen inschatting)"),
        ("Garagedeur (hout)", "€250 – €600"),
    ],
    "prijsfactoren": [
        "De hoeveelheid houtwerk. Een vrijstaande woning heeft vaak twee keer zoveel kozijnen en boeidelen als een tussenwoning.",
        "De staat van de verf. Licht verweerd: schuren en twee lagen. Bladderend of kaal: alles eraf, gronden en opbouwen. Dat is soms twee keer zoveel werk.",
        "Houtrot. De grootste onbekende post. Een schilder ziet het pas goed als hij gaat schuren.",
        "Hoogte en bereikbaarheid. Vanaf de bovenverdieping is een steiger of hoogwerker nodig.",
        "Verfsysteem en kleur. Een kleurwissel van donker naar licht vraagt een extra laag. Donkere kleuren op het zuiden vragen een verf die tegen warmte kan.",
        "Het seizoen en de regio. In het voorjaar zitten schilders vol, in de Randstad liggen de tarieven hoger.",
    ],
    "uitleg": [
        ("Wat valt onder buitenschilderwerk?", "Alle kozijnen, ramen en draaiende delen, de voor-, achter- en garagedeur, boeidelen, windveren en daklijsten, en de dakkapel. Soms ook een houten schuur, een schutting of een geschilderde gevel. Schoon metselwerk wordt niet geschilderd; voegwerk en impregneren zijn ander werk. Vraag de schilder elk onderdeel apart op de offerte te zetten."),
        ("Hoe vaak is buitenschilderwerk nodig?", "Met dekkende verf meestal elke zes tot acht jaar. Kozijnen op het zuiden en westen gaan sneller. Een kleine beurt tussendoor, alleen de onderdorpels en de zonkant, houdt de rekening laag. Meer hierover in <a href=\"/kennisbank/hoe-vaak-buitenschilderwerk/\">hoe vaak buitenschilderwerk</a>."),
    ],
    "verdieping": [
        ("Rekenvoorbeeld: tussenwoning uit de jaren zeventig",
         "<p>Stel: een tussenwoning met vier kozijnen voor, vier achter, een voordeur, een achterdeur en 12 meter boeidelen. De laatste beurt was acht jaar geleden. Er zijn drie plekken met beginnende houtrot.</p>"
         + _tabel(["Post", "Berekening", "Richtprijs"], [
             ["Kozijnen", "8 × €90 – €190", "€720 – €1.520"],
             ["Deuren", "2 × €100 – €185", "€200 – €370"],
             ["Boeidelen", "12 m × €25 – €55", "€300 – €660"],
             ["Steiger achtergevel", "1 gevel", "€300 – €900"],
             ["Houtrot", "3 plekken × €50 – €275", "€150 – €825"],
             ["<strong>Totaal</strong>", "", "<strong>€1.670 – €4.275</strong>"],
         ], num_vanaf=2)
         + "<p>Zonder houtrot is het €1.520 tot €3.450. Het verschil laat zien waarom je bij elke offerte vraagt hoe houtrot wordt afgerekend. Reken je eigen huis door met de <a href=\"/kosten/calculator/\">huiscalculator</a>.</p>"),
        ("Per m² of per stuk: hoe rekent een schilder?",
         "<p>Buiten rekenen de meeste schilders per stuk (per kozijn, per deur, per meter boeideel) of met één vaste prijs voor het hele huis. Prijssites rekenen het om naar m² houtwerk. Bij dat omrekenen tel je de zichtbare vlakken van kozijn, raam en dorpel op, niet het glas. Een gemiddeld kozijn heeft 2 tot 5 m² houtwerk.</p>"
         "<p>Krijg je een offerte per uur? Dan ligt het uurtarief meestal tussen €45 en €65 exclusief btw (zie <a href=\"/kosten/schilder-uurtarief/\">uurtarief schilder</a>). Vraag dan altijd om een schatting van het aantal uren en een maximum.</p>"),
        ("Zo verloopt een buitenschilderbeurt",
         "<ol><li><strong>Opname.</strong> De schilder loopt rond, prikt in de dorpels en hoeken en noteert houtrot.</li>"
         "<li><strong>Steiger en afdekken.</strong> Steiger plaatsen, planten en bestrating afdekken.</li>"
         "<li><strong>Voorwerk.</strong> Reinigen, ontvetten, schuren, losse verf eraf. Houtrot uithakken en vullen of een inzetstuk plaatsen.</li>"
         "<li><strong>Gronden en kitten.</strong> Kale plekken gronden, naden en glasaansluitingen kitten.</li>"
         "<li><strong>Aflakken.</strong> Eén of twee lagen aflak, bij voorkeur bij droog weer boven 10 °C.</li>"
         "<li><strong>Oplevering.</strong> Samen rondlopen en afspraken over garantie vastleggen.</li></ol>"
         "<p>Een tussenwoning duurt meestal drie tot vijf werkdagen. Plan het tussen april en oktober; zie <a href=\"/gids/wanneer-buiten-schilderen/\">wanneer buiten schilderen</a> of check de <a href=\"/schilderweer/\">schilderweer-tool</a>.</p>"),
    ],
    "valkuilen": [
        "<strong>Geen steiger in de prijs.</strong> De offerte lijkt laag, maar de steiger komt er later bij. Vraag of steiger of hoogwerker is inbegrepen.",
        "<strong>Houtrot \"op regie\" zonder maximum.</strong> Dan weet je pas achteraf wat het kost. Vraag een prijs per plek of een maximumbedrag.",
        "<strong>Alleen een totaalbedrag.</strong> Zonder losse posten kun je niet vergelijken. Vraag per onderdeel een prijs.",
        "<strong>Eén laag aflak waar twee nodig zijn.</strong> Bij verweerde verf is één laag te dun. Vraag hoeveel lagen er op komen.",
        "<strong>21% btw op schilderwerk aan een woning ouder dan twee jaar.</strong> Daar hoort 9% op. Alleen houten inzetstukken en nieuwe onderdorpels vallen onder 21%.",
        "<strong>Geen verfmerk of verfsysteem.</strong> Zonder merk en productnaam weet je niet wat je koopt, en is garantie lastig.",
        "<strong>Geen garantietermijn op papier.</strong> Spreek af hoe lang en wat eronder valt. Lees meer over <a href=\"/kennisbank/verfschade-en-garantie/\">verfschade en garantie</a>.",
    ],
    "tips": [
        "Laat binnen- en buitenwerk in één ronde doen; je deelt opstart- en voorrijkosten.",
        "Plan in september of oktober. De voorjaarspiek is voorbij en schilders hebben vaker ruimte.",
        "Laat de onderdorpels elke drie à vier jaar bijwerken. Daar begint houtrot bijna altijd.",
        "Vraag drie offertes en leg ze per onderdeel naast elkaar, niet alleen op het totaal.",
    ],
    "btw": "Schilderwerk aan een woning die ouder is dan twee jaar valt onder 9% btw, inclusief de verf die de schilder levert. Houten inzetstukken, nieuwe onderdorpels en het vervangen van kozijnen vallen onder 21%. Bij een woning van twee jaar of jonger en bij bedrijfspanden betaal je 21%, en dan liggen de prijzen in deze tabel ongeveer 11% hoger.",
    "faq": [
        ("Wat kost buitenschilderwerk per m²?",
         "Gemiddeld €30 tot €45 per m² houtwerk, inclusief verf en btw. Homedeal noemt €25 tot €45, De Schilderscombinatie €35 tot €45. Een gevel van stucwerk is goedkoper per m²: €20 tot €40."),
        ("Wat kost buitenschilderwerk voor een tussenwoning?",
         "Reken op €1.500 tot €3.450 voor de hele buitenkant: kozijnen, deuren, boeidelen en een steiger achter. Houtrotherstel komt er meestal apart bij."),
        ("Wat kost buitenschilderwerk voor een vrijstaand huis?",
         "Meestal €3.250 tot €7.200. Het hangt af van het aantal kozijnen, de dakkapel en hoeveel steigerwerk er nodig is."),
        ("Wat kost het schilderen van één kozijn buiten?",
         "€90 tot €190 per kozijn, inclusief raam en dorpel. Een groot kozijn met meerdere ramen of roeden zit aan de bovenkant."),
        ("Is een steiger altijd nodig?",
         "Voor de bovenverdieping bijna altijd. Een steiger of hoogwerker kost €300 tot €900 per gevel. Op de begane grond werkt de schilder met een ladder of trap."),
        ("Hoeveel btw betaal ik over buitenschilderwerk?",
         "9% als de woning ouder is dan twee jaar, ook over de verf. Houten inzetstukken en nieuwe onderdorpels vallen onder 21%."),
        ("Rekent een buitenschilder per uur of per stuk?",
         "Meestal per stuk of met een vaste prijs voor het hele huis. Alleen houtrot wordt soms per uur gerekend. Vraag dan een maximum."),
        ("Wanneer is buitenschilderwerk het goedkoopst?",
         "In het naseizoen, september en oktober. Sommige schilders geven ook in de winter korting, maar buiten schilderen kan dan alleen op droge dagen boven 5 tot 10 °C."),
        ("Hoe lang gaat buitenschilderwerk mee?",
         "Met een goed verfsysteem zes tot acht jaar. De zonkant en de onderdorpels gaan eerder; een kleine beurt na drie à vier jaar verlengt de levensduur."),
        ("Kan ik buitenschilderwerk deels zelf doen?",
         "De begane grond en het schuurwerk kun je zelf doen. Werk op hoogte en houtrotherstel laat je beter aan een schilder over. Spreek vooraf af wat de schilder dan wel en niet garandeert."),
    ],
}


# ---------------------------------------------------------------------------
# 2. Kosten binnenschilderwerk
# ---------------------------------------------------------------------------

_BINNEN = {
    "slug": "binnenschilderwerk",
    "klus": "binnenschilderwerk",
    "kruimel": "Binnenschilderwerk",
    "h1": "Kosten binnenschilderwerk 2026: per kamer en per woning",
    "title": "Kosten binnenschilderwerk 2026: prijs per kamer en woning",
    "description": "Binnenschilderwerk kost €950 tot €2.050 voor een woonkamer met kozijnen en deur, en €3.900 tot €8.500 voor een hele woning. Met prijzen per onderdeel.",
    "dienst": "binnenschilderwerk",
    "eenheid": "per woonkamer van 20 m² (alles)",
    "van": 950,
    "tot": 2050,
    "kort": "€950 – €2.050 per woonkamer",
    "intro": "Bij binnenschilderwerk gaat het om meer dan muren. Kozijnen, deuren, plinten en de trap horen er ook bij, en daar zit vaak het meeste werk. Hier zie je wat een kamer en een hele woning kosten, met alle onderdelen. Zoek je alleen de prijs voor muren en plafonds, kijk dan bij <a href=\"/kosten/schilderen-per-m2/\">schilderen per m²</a>.",
    "direct": "Een woonkamer van 20 m² helemaal laten schilderen (muren, plafond, kozijnen, deur en plinten) kost <strong>€950 tot €2.050</strong>, inclusief verf en 9% btw. Een slaapkamer kost <strong>€575 tot €1.250</strong>. Voor een hele tussenwoning binnen, met deuren en trap, betaal je <strong>€3.900 tot €8.500</strong>. Muren en plafonds kosten €10 tot €22 per m².",
    "prijstabel": ("Prijzen binnenschilderwerk per onderdeel (peildatum november 2026)",
        _tabel(["Onderdeel", "Topschilder", "Zoofy", "Homedeal"], [
            ["Muren, twee lagen", "€10 – €16 per m²", "€8 – €17 per m²", "€10 – €15 per m² (sauswerk)"],
            ["Plafond, twee lagen", "€12 – €22 per m²", "€10 – €15 per m²", "–"],
            ["Binnenkozijn (deurkozijn)", "€35 – €75", "€50 – €75", "–"],
            ["Binnendeur lakken of spuiten", "€95 – €185", "€100 – €150", "–"],
            ["Plinten", "€4 – €8 per meter", "–", "–"],
            ["Trap", "€350 – €950", "–", "€600 – €800"],
            ["Latex spuiten (lege ruimte)", "€6 – €15 per m²", "–", "€6 – €12 per m²"],
            ["Hele woning", "€3.900 – €8.500", "€2.000 – €8.000", "–"],
        ])
        + _bronregel([ZOOFY_BINNEN, HOMEDEAL_SCHILDER], "Zoofy zegt dat zijn prijzen inclusief 21% btw zijn; Topschilder rekent met 9% voor een woning ouder dan twee jaar. De prijs voor plinten is een eigen inschatting. ")),
    "voorbeelden": [
        ("Slaapkamer van 3 bij 4 meter", None, "€575 – €1.250. Zo'n 45 m² muur en plafond, een deurkozijn, een raamkozijn binnen en 14 meter plint."),
        ("Woonkamer van 20 m²", None, "€950 – €2.050. Zo'n 67 m² muur en plafond, twee kozijnen, een deur en 18 meter plint."),
        ("Hal, trap en overloop", None, "€900 – €2.100. Trap, trapgat en wanden; door de hoogte vaak met rolsteiger."),
        ("Hele tussenwoning binnen", None, "€3.900 – €8.500. 250 m² muren en plafonds, acht deurkozijnen, acht deuren en de trap."),
    ],
    "extra": [
        ("Gaten en scheuren vullen, plamuren", "€3 – €8 per m² extra"),
        ("Voorstrijken van kaal stucwerk", "€2 – €4 per m² extra (eigen inschatting)"),
        ("Meubels verplaatsen en afdekken", "vaak inbegrepen; vraag het na"),
        ("Radiatoren schilderen", "€90 – €225 per radiator"),
        ("Behang verwijderen", "€4 – €10 per m² (eigen inschatting)"),
    ],
    "prijsfactoren": [
        "Hoeveel lakwerk er is. Kozijnen, deuren en plinten kosten per m² veel meer tijd dan muren.",
        "De staat van de muren. Gaten, scheuren en oud behang betekenen extra voorwerk.",
        "Kleurwissel. Van donker naar licht of andersom vraagt vaak een extra laag.",
        "Hoogte. Boven 2,60 meter, in een trapgat of bij een vide is een rolsteiger nodig.",
        "Bewoond of leeg. In een lege woning werkt een schilder sneller en kan hij spuiten.",
        "De hoeveelheid. Bij een hele woning daalt de prijs per m² door minder opstart.",
    ],
    "uitleg": [
        ("Wat valt onder binnenschilderwerk?", "Muren en plafonds sauzen, kozijnen en deuren lakken, plinten, radiatoren, de trap en eventueel spuitwerk. Wat een schilder per onderdeel doet en hoe hij werkt, lees je op <a href=\"/schilderwerk/binnenschilderwerk/\">binnenschilderwerk</a>."),
        ("Hoe lang duurt binnenschilderwerk?", "Een kamer is meestal in één tot twee dagen klaar, inclusief droogtijd tussen de lagen. Een hele woning duurt een tot twee weken. Lakwerk heeft langer nodig om hard te worden dan muurverf."),
    ],
    "verdieping": [
        ("Rekenvoorbeeld: woonkamer van 5 bij 4 meter",
         "<p>Een woonkamer van 5 bij 4 meter en 2,60 meter hoog. De muren zijn wit en blijven licht. Er zijn twee kozijnen, één binnendeur en 18 meter plint.</p>"
         + _tabel(["Post", "Berekening", "Richtprijs"], [
             ["Muren", "47 m² × €10 – €16", "€470 – €752"],
             ["Plafond", "20 m² × €12 – €22", "€240 – €440"],
             ["Kozijnen binnen", "2 × €35 – €75", "€70 – €150"],
             ["Binnendeur", "1 × €95 – €185", "€95 – €185"],
             ["Plinten", "18 m × €4 – €8", "€72 – €144"],
             ["<strong>Totaal</strong>", "", "<strong>€947 – €1.671</strong>"],
         ], num_vanaf=2)
         + "<p>Moeten er gaten en scheuren gevuld worden, of is het een kleurwissel, dan kom je richting €2.050. Het aantal liters verf reken je uit met de <a href=\"/gids/verf-berekenen/\">verfcalculator</a>.</p>"),
        ("Zelf doen of uitbesteden?",
         "<p>Muren sauzen doen veel mensen zelf. Bij lakwerk ligt dat anders: kozijnen en deuren vragen schuren, gronden en strak aflakken, en daar zie je elk foutje. Een veelgekozen tussenweg: zelf de muren, de schilder het lakwerk. Wat het lakwerk los kost, staat bij <a href=\"/kosten/deuren-spuiten/\">deuren spuiten</a> en <a href=\"/kosten/kozijnen-schilderen/\">kozijnen schilderen</a>.</p>"),
        ("Schilderen in de winter",
         "<p>Binnen kun je het hele jaar schilderen, zolang de ruimte verwarmd is en je kunt ventileren. In de winter hebben schilders vaker ruimte in de planning. Lees <a href=\"/kennisbank/binnen-schilderen-in-de-winter/\">binnen schilderen in de winter</a> voor de aandachtspunten.</p>"),
    ],
    "valkuilen": [
        "<strong>Alleen \"muren en plafonds\" genoemd.</strong> Kozijnen, deuren en plinten ontbreken dan. Vraag elk onderdeel apart op de offerte.",
        "<strong>Geen voorwerk benoemd.</strong> Vullen, schuren en voorstrijken zijn het halve werk. Staat het er niet in, dan komt het later als meerwerk.",
        "<strong>Eén laag muurverf.</strong> Op een nieuwe kleur of kaal stucwerk is één laag bijna nooit genoeg.",
        "<strong>Prijs per m² zonder aantal m².</strong> Dan kun je niet controleren wat je betaalt. Vraag hoeveel m² de schilder heeft gemeten.",
        "<strong>21% btw in een woning ouder dan twee jaar.</strong> Daar hoort 9% op, ook over de verf.",
        "<strong>Niet duidelijk wie meubels verplaatst en afdekt.</strong> Spreek het af, anders betaal je er per uur voor.",
    ],
    "tips": [
        "Maak de kamer zelf leeg of zet alles in het midden. Dat scheelt uren.",
        "Laat meerdere kamers tegelijk doen. Dan daalt de prijs per m².",
        "Kies voor muren een kleur in dezelfde tint als nu. Dan is twee lagen genoeg.",
        "Plan binnenwerk in de winter. Schilders hebben dan vaker ruimte.",
    ],
    "btw": "Schilderwerk in een woning die ouder is dan twee jaar valt onder 9% btw, ook over de verf die de schilder gebruikt. Is je woning twee jaar of jonger, dan betaal je 21%, en liggen de prijzen ongeveer 11% hoger.",
    "faq": [
        ("Wat kost binnenschilderwerk per m²?",
         "Muren kosten €10 tot €16 per m², plafonds €12 tot €22 per m², inclusief verf en btw. Kozijnen, deuren en plinten worden per stuk of per meter gerekend."),
        ("Wat kost een woonkamer laten schilderen?",
         "Een woonkamer van 20 m² met muren, plafond, twee kozijnen, een deur en plinten kost €950 tot €2.050. Alleen muren en plafond: €710 tot €1.190."),
        ("Wat kost een hele woning binnen schilderen?",
         "Voor een tussenwoning met muren, plafonds, deuren, kozijnen en de trap reken je op €3.900 tot €8.500. Zoofy noemt €2.000 tot €8.000 voor een heel huis."),
        ("Wat kost een slaapkamer schilderen?",
         "€575 tot €1.250 met kozijnen en plinten. Alleen muren en plafond van een kamer van 3 bij 4 meter: €450 tot €990."),
        ("Wat kost het lakken van binnendeuren?",
         "€95 tot €185 per deur, afhankelijk van lakken of spuiten en de staat van de oude laag. Een deurkozijn kost €35 tot €75."),
        ("Hoeveel uur doet een schilder over een kamer?",
         "Voor muren en plafond van een slaapkamer meestal een dag. Met kozijnen, deur en plinten anderhalve tot twee dagen, inclusief droogtijd."),
        ("Is binnenschilderwerk goedkoper in de winter?",
         "Soms. Schilders hebben dan meer ruimte en zijn vaker flexibel in prijs of planning. Een vaste winterkorting is er niet meer."),
        ("Moet ik de kamer zelf leeghalen?",
         "Dat scheelt geld. Veel schilders schuiven meubels naar het midden en dekken ze af, maar dat kost tijd. Vraag of het in de prijs zit."),
        ("Welke btw betaal ik over binnenschilderwerk?",
         "9% in een woning ouder dan twee jaar, inclusief verf. In nieuwbouw van twee jaar of jonger en in bedrijfspanden 21%."),
    ],
}


# ---------------------------------------------------------------------------
# 3. Kosten houtrot herstellen
# ---------------------------------------------------------------------------

_HOUTROT = {
    "slug": "houtrot-herstellen",
    "klus": "houtrot herstellen",
    "kruimel": "Houtrot herstellen",
    "h1": "Houtrot herstellen: kosten per plek in 2026",
    "title": "Houtrot herstellen kosten 2026: prijs per plek en kozijn",
    "description": "Houtrot laten herstellen kost €50 tot €275 per plek. Met prijzen per aantal plekken, voor een inzetstuk of onderdorpel, en wanneer vervangen goedkoper is.",
    "dienst": "houtrot-reparatie",
    "eenheid": "per reparatieplek",
    "van": 50,
    "tot": 275,
    "kort": "€50 – €275 per plek",
    "intro": "Houtrot zit meestal op plekken waar water blijft staan: onderdorpels, hoeken van kozijnen en de onderkant van deuren. Een schilder of timmerman haalt het rotte hout weg en vult het met epoxy of zet er een nieuw stuk hout in. Je betaalt per plek. Hier zie je wat dat kost, wanneer een inzetstuk nodig is en wanneer vervangen slimmer is.",
    "direct": "Houtrot herstellen kost <strong>€50 tot €275 per plek</strong>. Een kleine plek die met epoxy wordt gevuld zit aan de onderkant. Een houten inzetstuk aan de bovenkant. Drie plekken kosten dus €150 tot €825. Een complete onderdorpel vervangen kost €150 tot €400. Is meer dan een derde van het kozijn aangetast, vraag dan ook een prijs voor vervangen.",
    "prijstabel": ("Prijzen houtrot herstellen (peildatum november 2026)",
        _tabel(["Situatie", "Topschilder", "Slimster", "Homedeal"], [
            ["1 plek", "€50 – €275", "€50 – €150", "€100 – €150 (kleine reparatie)"],
            ["3 plekken", "€150 – €825", "€280 – €420", "–"],
            ["6 plekken", "€300 – €1.650", "€690 – €825", "–"],
            ["Reparatie per kozijn", "–", "–", "€150 – €500"],
            ["Ernstige houtrot per kozijn", "–", "–", "€500 – €1.000"],
            ["Uurtarief vakman", "€45 – €65 excl. btw", "€35 – €60", "–"],
            ["Kozijn vervangen", "–", "–", "€850 – €1.300 per m² incl. HR++ glas"],
        ])
        + _bronregel([SLIMSTER_HOUTROT, HOMEDEAL_REPAREREN], "Slimster en Homedeal noemen niet of hun bedragen inclusief btw zijn. ")),
    "voorbeelden": [
        ("Eén kleine plek in een onderdorpel", 1, "Uithakken, drogen, epoxy vullen, schuren en gronden."),
        ("Drie plekken bij een buitenbeurt", 3, "De meest voorkomende situatie bij een woning die acht jaar niet geschilderd is."),
        ("Zes plekken, deels inzetstukken", 6, "Een woning waar het onderhoud lang is uitgesteld."),
    ],
    "extra": [
        ("Onderdorpel vervangen", "€150 – €400 per dorpel (eigen inschatting, 21% btw)"),
        ("Houten inzetstuk in een stijl of hoek", "valt binnen de prijs per plek, aan de bovenkant"),
        ("Kozijn daarna opnieuw schilderen", "€90 – €190 per kozijn"),
        ("Steiger voor plekken op hoogte", "€300 – €900 per gevel"),
        ("Kozijn vervangen", "€850 – €1.300 per m², volgens Homedeal"),
    ],
    "prijsfactoren": [
        "De grootte en diepte van de plek. Een plek van een paar centimeter is snel gevuld; rot dat tot in de pen-en-gatverbinding zit, vraagt een inzetstuk.",
        "Epoxy of nieuw hout. Epoxy is sneller. Een inzetstuk of nieuwe dorpel is timmerwerk.",
        "Hoe nat het hout is. Nat hout moet eerst drogen; dat kan een extra bezoek betekenen.",
        "Bereikbaarheid. Plekken op de bovenverdieping vragen een steiger of hoogwerker.",
        "Hoeveel plekken tegelijk. Bij meerdere plekken in één ronde daalt de prijs per plek.",
    ],
    "uitleg": [
        ("Wat je ervoor krijgt", "Het rotte hout wordt tot op gezond hout weggehaald. Het hout droogt, krijgt een impregneermiddel of primer, en wordt gevuld met een tweecomponenten-houtreparatiemiddel of een nieuw stuk hout. Daarna schuren, gronden en meeschilderen met de rest van het kozijn. Zonder dat laatste is het werk niet af."),
        ("Epoxy of inzetstuk?", "Epoxy is geschikt voor plekken tot een paar centimeter diep. Is het rot dieper, zit het in een verbinding of is de dorpel over de hele lengte zacht, dan is een inzetstuk of een nieuwe dorpel beter. Meer uitleg in <a href=\"/kennisbank/houtrot-herkennen-en-herstellen/\">houtrot herkennen en herstellen</a>."),
    ],
    "verdieping": [
        ("Rekenvoorbeeld: drie plekken en een nieuwe onderdorpel",
         "<p>Bij de opname van een tussenwoning vindt de schilder twee kleine plekken in de hoeken van een kozijn, één plek in de onderkant van de achterdeur, en een onderdorpel die over de hele lengte zacht is.</p>"
         + _tabel(["Post", "Berekening", "Richtprijs"], [
             ["Kleine plekken met epoxy", "2 × €50 – €125", "€100 – €250"],
             ["Plek in de achterdeur", "1 × €75 – €200", "€75 – €200"],
             ["Onderdorpel vervangen", "1 dorpel", "€150 – €400"],
             ["Kozijn en deur bijschilderen", "meegenomen in de buitenbeurt", "–"],
             ["<strong>Totaal herstel</strong>", "", "<strong>€325 – €850</strong>"],
         ], num_vanaf=2)
         + "<p>De onderdorpel valt onder 21% btw, de rest onder 9%. Een nette offerte splitst dat. Het schilderwerk erna zie je bij <a href=\"/kosten/buitenschilderwerk/\">kosten buitenschilderwerk</a>.</p>"),
        ("Repareren of vervangen?",
         _tabel(["Situatie", "Advies"], [
             ["Een paar losse plekken, de rest is hard", "Repareren. Veel goedkoper dan vervangen."],
             ["De onderdorpel is helemaal zacht, de stijlen niet", "Alleen de dorpel vervangen."],
             ["Meer dan een derde van het kozijn is aangetast", "Vraag ook een prijs voor een nieuw kozijn."],
             ["Je wilt toch nieuw glas (HR++ of triple)", "Vervangen kan dan samen met het glas."],
         ], num_vanaf=9)
         + "<p>Een nieuw houten kozijn kost volgens Homedeal €850 tot €1.300 per m², inclusief HR++ glas en montage. Voor een kozijn van 2 m² is dat €1.700 tot €2.600. Reparatie is in bijna alle gevallen goedkoper, zolang de rest van het hout gezond is.</p>"),
        ("Hoe voorkom je nieuwe houtrot?",
         "<ul><li>Laat de buitenkant op tijd schilderen: elke zes tot acht jaar, de onderdorpels vaker.</li>"
         "<li>Laat open naden en losse kitvoegen dicht maken voordat er water in trekt.</li>"
         "<li>Zorg dat water weg kan: geen planten of tegels tegen de dorpel.</li>"
         "<li>Doe elk voorjaar de priemtest: prik met een schroevendraaier in hoeken en dorpels.</li></ul>"
         "<p>Twijfel je of je huis toe is aan onderhoud? Doe de gratis <a href=\"/onderhoudscheck/\">onderhoudscheck</a>.</p>"),
    ],
    "valkuilen": [
        "<strong>\"Houtrot op regie\" zonder maximum.</strong> Je weet pas achteraf wat het kost. Vraag een prijs per plek of een plafondbedrag.",
        "<strong>Geen aantal plekken genoemd.</strong> Vraag hoeveel plekken de schilder heeft gezien en waar.",
        "<strong>Vullen zonder rot weg te halen.</strong> Dan rot het onder de vuller door. Vraag of het rotte hout tot op gezond hout wordt verwijderd.",
        "<strong>Alles onder 9% btw.</strong> Houten inzetstukken en nieuwe dorpels vallen onder 21%. Andersom: schilderwerk erna hoort 9% te zijn.",
        "<strong>Geen schilderwerk na het herstel.</strong> Een gevulde plek zonder grondverf en lak houdt het niet lang.",
        "<strong>Geen garantie op het herstel.</strong> Spreek af hoe lang de reparatie gegarandeerd is.",
    ],
    "tips": [
        "Laat houtrot herstellen samen met de buitenbeurt; de steiger staat er dan toch.",
        "Laat de schilder bij de opname al prikken en plekken markeren, zodat de offerte klopt.",
        "Wacht niet: een plek van €50 kan binnen een paar jaar een dorpel van €400 worden.",
        "Vraag foto's van de plekken voor en na het herstel.",
    ],
    "btw": "Het herstellen met vulmiddel en het schilderwerk erna vallen bij een woning ouder dan twee jaar onder 9% btw. Een houten inzetstuk, een nieuwe onderdorpel of een nieuw kozijn valt onder 21%.",
    "faq": [
        ("Wat kost houtrot herstellen per plek?",
         "€50 tot €275 per plek. Een kleine plek met epoxy zit aan de onderkant, een plek met een houten inzetstuk aan de bovenkant."),
        ("Wat kost houtrot repareren in een kozijn?",
         "Homedeal noemt €150 tot €500 per kozijn voor een gewone reparatie, en €500 tot €1.000 bij ernstige houtrot. Het schilderwerk erna komt er vaak bij."),
        ("Wat kost het vervangen van een onderdorpel?",
         "Reken op €150 tot €400 per dorpel, afhankelijk van de lengte en het profiel. Dit valt onder 21% btw."),
        ("Is houtrot repareren met epoxy duurzaam?",
         "Ja, als het rotte hout helemaal is weggehaald, het hout droog is en de plek daarna goed wordt geschilderd. Bij diepe rot is een inzetstuk beter."),
        ("Wanneer is een nieuw kozijn goedkoper dan repareren?",
         "Als meer dan een derde van het kozijn rot is, of als de verbindingen zijn aangetast. Een nieuw houten kozijn kost €850 tot €1.300 per m² volgens Homedeal."),
        ("Doet een schilder ook houtrot?",
         "De meeste schilders herstellen kleine en middelgrote plekken zelf. Voor nieuwe dorpels of kozijnen werken ze vaak samen met een timmerman."),
        ("Kan ik houtrot zelf repareren?",
         "Kleine plekken wel, met een tweecomponenten-houtreparatiemiddel uit de bouwmarkt. Haal het rot tot op gezond hout weg en schilder de plek daarna. Bij twijfel over de omvang: laat een vakman kijken."),
        ("Hoe herken ik houtrot?",
         "Afbladderende verf, donkere plekken en hout dat zacht aanvoelt als je erin prikt. Vaak in onderdorpels en hoeken. Meer in houtrot herkennen en herstellen."),
        ("Valt houtrot onder de garantie van de schilder?",
         "Alleen als de schilder het herstel zelf heeft gedaan en er garantie op heeft gegeven. Nieuwe houtrot door achterstallig onderhoud valt er niet onder."),
    ],
}

KOSTEN_RONDE5 = [_BUITEN, _BINNEN, _HOUTROT]


# ---------------------------------------------------------------------------
# Verdieping voor bestaande pagina's
# ---------------------------------------------------------------------------

UITBREIDING_R5 = {
    "kozijnen-schilderen": {
        "title": "Kozijnen schilderen kosten 2026: prijs binnen en buiten",
        "direct": "Een buitenkozijn laten schilderen kost <strong>€90 tot €190 per kozijn</strong>, inclusief raam, dorpel, verf en 9% btw. Een binnenkozijn kost <strong>€35 tot €75</strong>. Alle buitenkozijnen van een tussenwoning (acht stuks) kosten €720 tot €1.520, plus €300 tot €900 voor een steiger als de bovenverdieping meegaat.",
        "prijstabel": ("Prijzen kozijnen schilderen (peildatum november 2026)",
            _tabel(["Situatie", "Topschilder", "Homedeal", "De Schilderscombinatie"], [
                ["Buitenkozijn", "€90 – €190 per kozijn", "€50 – €100 per kozijn", "–"],
                ["Binnenkozijn", "€35 – €75 per kozijn", "€35 – €75 per kozijn", "–"],
                ["3 buitenkozijnen beneden", "€270 – €570", "€690 (voorbeeld)", "–"],
                ["Alle buitenkozijnen, tussenwoning", "€720 – €1.520 + steiger", "€500 – €1.800", "€700 – €2.500"],
                ["Alle buitenkozijnen, hoekwoning", "€1.080 – €2.280 + steiger", "€1.800 (voorbeeld)", "–"],
                ["Houtrot per plek", "€50 – €275", "–", "–"],
            ])
            + _bronregel([HOMEDEAL_KOZIJN, DSC_BUITEN],
                         "Homedeal rekent zonder steiger en noemt een lager bedrag per buitenkozijn; in hun voorbeelden komt een buitenkozijn op ongeveer €230 per stuk. ")),
        "verdieping": [
            ("Rekenvoorbeeld: twee-onder-een-kap met twaalf kozijnen",
             "<p>Twaalf buitenkozijnen, waarvan zes op de bovenverdieping. De verf is verweerd maar niet kaal. Bij de opname vindt de schilder twee plekken houtrot in onderdorpels.</p>"
             + _tabel(["Post", "Berekening", "Richtprijs"], [
                 ["Buitenkozijnen", "12 × €90 – €190", "€1.080 – €2.280"],
                 ["Steiger zijgevel en achtergevel", "2 gevels × €300 – €900", "€600 – €1.800"],
                 ["Houtrot", "2 × €50 – €275", "€100 – €550"],
                 ["Kitvoegen glas vervangen", "30 m × €6 – €15", "€180 – €450"],
                 ["<strong>Totaal</strong>", "", "<strong>€1.960 – €5.080</strong>"],
             ], num_vanaf=2)
             + "<p>De steiger en de houtrot maken samen bijna de helft van het verschil tussen een lage en een hoge offerte. Wat de rest van het buitenwerk kost, staat bij <a href=\"/kosten/buitenschilderwerk/\">kosten buitenschilderwerk</a>.</p>"),
            ("Welke verf en kleur?",
             "<p>Buiten krijgt een houten kozijn een dekkend systeem van grondverf, voorlak en aflak. Wit is de meest gekozen kleur; over het verschil tussen RAL 9010, RAL 9001 en gebroken wit lees je in <a href=\"/kennisbank/ral-9010-of-ral-9001/\">RAL 9010 of RAL 9001</a>. Meer over de verf zelf in <a href=\"/kennisbank/welke-verf-voor-kozijnen/\">welke verf voor kozijnen</a>. Glaslatten die rot of los zijn, vervang je bij voorkeur in dezelfde ronde: zie <a href=\"/kennisbank/glaslatten-vervangen/\">glaslatten vervangen</a>.</p>"),
        ],
        "valkuilen": [
            "<strong>Steiger niet genoemd.</strong> Voor de bovenverdieping is die bijna altijd nodig. Vraag of hij in de prijs zit.",
            "<strong>Houtrot op regie zonder maximum.</strong> Vraag een prijs per plek of een plafondbedrag.",
            "<strong>Draaiende delen niet inbegrepen.</strong> Sommige offertes rekenen ramen en klepramen apart. Vraag wat \"per kozijn\" precies omvat.",
            "<strong>Kitwerk ontbreekt.</strong> Oude, gescheurde kitvoegen rond het glas laten water door. Vraag of ze worden vervangen.",
            "<strong>Eén laag aflak.</strong> Bij verweerde verf zijn twee lagen nodig voor de juiste laagdikte.",
            "<strong>21% btw op het schilderwerk.</strong> Bij een woning ouder dan twee jaar hoort daar 9% op.",
        ],
        "faq_extra": [
            ("Wat kost het schilderen van kozijnen per m²?",
             "Omgerekend €30 tot €45 per m² houtwerk. Schilders rekenen kozijnen meestal per stuk, omdat elk kozijn een andere vorm heeft."),
            ("Wat kosten binnen- en buitenkozijnen samen?",
             "Voor een tussenwoning met acht buitenkozijnen en acht binnenkozijnen: €1.000 tot €2.120, plus eventueel een steiger. In één ronde deel je de voorrijkosten."),
            ("Wat kost kozijnen schilderen in RAL 9010?",
             "Hetzelfde als in een andere lichte kleur. Een kleurwissel van donker naar wit kan wel een extra laag vragen."),
            ("Hoe vaak moeten buitenkozijnen geschilderd worden?",
             "Met dekkende verf elke zes tot acht jaar. De onderdorpels en de zonkant gaan sneller; daar helpt een kleine beurt na drie à vier jaar."),
            ("Kan ik kunststof kozijnen laten schilderen?",
             "Ja, met een speciale hechtprimer. Dat kost €60 tot €140 per kozijn. Zie kunststof kozijnen schilderen."),
        ],
    },
    "schilderen-per-m2": {
        "title": "Schilderen per m² kosten 2026: muren, plafonds en buiten",
        "direct": "Een schilder rekent in 2026 <strong>€10 tot €16 per m² voor muren</strong> en <strong>€12 tot €22 per m² voor plafonds</strong>, inclusief verf, twee lagen en 9% btw. Latex spuiten in een lege ruimte kost €6 tot €15 per m². Buiten ligt de prijs hoger: <strong>€30 tot €45 per m² houtwerk</strong> en €20 tot €40 per m² gevel.",
        "prijstabel": ("Prijs per m² per soort werk (peildatum november 2026)",
            _tabel(["Soort werk", "Topschilder", "Zoofy", "Homedeal"], [
                ["Muren binnen, twee lagen", "€10 – €16", "€8 – €17", "€10 – €15 (sauswerk)"],
                ["Plafond, twee lagen", "€12 – €22", "€10 – €15", "–"],
                ["Muren, drie lagen (kleurwissel)", "€13 – €20", "€9 – €20", "–"],
                ["Latex spuiten", "€6 – €15", "–", "€6 – €12"],
                ["Plamuren en vullen", "+ €3 – €8", "–", "–"],
                ["Houtwerk buiten", "€30 – €45", "–", "€25 – €45"],
                ["Gevel buiten", "€20 – €40", "–", "€15 – €25"],
            ])
            + _bronregel([ZOOFY_BINNEN, HOMEDEAL_SCHILDER, HOMEDEAL_BUITEN],
                         "Homedeal noemt daarnaast €30 tot €35 per m² voor \"binnen\" in het algemeen; dat is inclusief lakwerk en dus niet te vergelijken met alleen muren. ")),
        "verdieping": [
            ("Rekenvoorbeeld: drie kamers in één keer",
             "<p>Een woonkamer van 5 bij 7 meter, een slaapkamer van 3 bij 4 meter en een hal, allemaal 2,60 meter hoog. Muren in een lichte kleur, plafonds wit.</p>"
             + _tabel(["Ruimte", "m² muur + plafond", "Richtprijs"], [
                 ["Woonkamer", "55 + 35 m²", "€970 – €1.650"],
                 ["Slaapkamer", "33 + 12 m²", "€474 – €792"],
                 ["Hal", "25 + 5 m²", "€310 – €510"],
                 ["Gaten en scheuren vullen", "40 m² × €3 – €8", "€120 – €320"],
                 ["<strong>Totaal</strong>", "165 m²", "<strong>€1.874 – €3.272</strong>"],
             ], num_vanaf=2)
             + "<p>Gerekend met €10 – €16 per m² muur en €12 – €22 per m² plafond. Laat je kozijnen en deuren meenemen, kijk dan bij <a href=\"/kosten/binnenschilderwerk/\">kosten binnenschilderwerk</a>.</p>"),
            ("Waarom verschillen prijzen per m² zo veel?",
             "<p>Een prijs per m² zegt alleen iets als je weet wat erin zit. Let op drie dingen:</p>"
             "<ul><li><strong>Hoeveel lagen.</strong> Eén laag opfrissen is goedkoper dan twee lagen met een kleurwissel.</li>"
             "<li><strong>Voorwerk.</strong> Vullen, schuren en voorstrijken kunnen €3 tot €8 per m² extra kosten.</li>"
             "<li><strong>Wat er meetelt.</strong> Rekent de schilder ramen en deuren mee of trekt hij ze af? Bij een kamer met grote ramen scheelt dat al snel 10 m².</li></ul>"
             "<p>Moet de muur eerst glad, lees dan <a href=\"/kennisbank/muur-plamuren/\">muur plamuren voor het schilderen</a>.</p>"),
        ],
        "valkuilen": [
            "<strong>Geen aantal m² op de offerte.</strong> Vraag hoeveel m² is gemeten, dan kun je het narekenen.",
            "<strong>Voorwerk niet inbegrepen.</strong> Vullen en voorstrijken komen dan als meerwerk. Vraag of het in de prijs per m² zit.",
            "<strong>Eén laag waar twee nodig zijn.</strong> Zeker bij een kleurwissel of kaal stucwerk.",
            "<strong>Plafond tegen muurprijs.</strong> Lijkt goedkoop, maar dan wordt er vaak ergens anders op bespaard. Plafonds kosten meer werk.",
            "<strong>Ramen en deuren meegeteld als m² muur.</strong> Vraag hoe de schilder meet.",
        ],
        "faq_extra": [
            ("Wat kost schilderen per m² buiten?",
             "Houtwerk buiten kost €30 tot €45 per m², een gevel van stucwerk €20 tot €40 per m², inclusief verf en btw."),
            ("Wat kost een muur van 10 m² laten schilderen?",
             "€100 tot €160 voor twee lagen. Bij zo'n kleine klus rekenen veel schilders een minimumprijs of voorrijkosten, dus combineer het met ander werk."),
            ("Is de prijs per m² inclusief verf?",
             "Bij de richtprijzen op deze pagina wel. Op een offerte staat het soms apart. Vraag het na als het niet duidelijk is."),
            ("Hoeveel verf heb ik nodig per m²?",
             "Met muurverf kom je met een liter ongeveer 8 tot 11 m² ver per laag. Reken het uit met de verfcalculator."),
        ],
    },
    "huis-schilderen": {
        "direct": "De buitenkant van een huis laten schilderen kost <strong>€1.500 tot €3.500 voor een tussenwoning</strong>, €2.000 tot €4.800 voor een hoekwoning of twee-onder-een-kap en <strong>€3.000 tot €7.000 voor een vrijstaande woning</strong>, inclusief verf en 9% btw. Binnen kost een hele woning €2.500 tot €5.500 voor muren en plafonds.",
        "valkuilen": [
            "<strong>Steiger of hoogwerker ontbreekt.</strong> Vraag of hij in de prijs zit.",
            "<strong>Houtrot zonder prijs per plek of maximum.</strong>",
            "<strong>Alleen een totaalbedrag zonder losse posten.</strong> Dan kun je niet vergelijken.",
            "<strong>21% btw op schilderwerk aan een woning ouder dan twee jaar.</strong>",
            "<strong>Geen verfmerk en geen garantietermijn op papier.</strong>",
        ],
    },
}


# ---------------------------------------------------------------------------
# Overzicht /kosten/
# ---------------------------------------------------------------------------

KOSTEN_OVERZICHT = {
    "kop": (
        '<div class="callout"><p><strong>Kort antwoord:</strong> een schilder kost in 2026 gemiddeld '
        '<strong>€45 tot €65 per uur</strong> exclusief btw. Per klus: muren en plafonds <strong>€10 tot €22 per m²</strong>, '
        'een buitenkozijn <strong>€90 tot €190</strong>, een binnendeur spuiten €95 tot €185 en houtrot €50 tot €275 per plek. '
        'De buitenkant van een tussenwoning kost €1.500 tot €3.450. Alle prijzen hieronder zijn inclusief verf en 9% btw, '
        'tenzij anders vermeld.</p></div>'
        '<h2>De belangrijkste prijzen (peildatum november 2026)</h2>'
        + _tabel(["Wat", "Richtprijs", "Meer"], [
            ["Uurtarief schilder", "€45 – €65 excl. btw", '<a href="/kosten/schilder-uurtarief/">uurtarief</a>'],
            ["Muren en plafonds", "€10 – €22 per m²", '<a href="/kosten/schilderen-per-m2/">per m²</a>'],
            ["Woonkamer, alles", "€950 – €2.050", '<a href="/kosten/binnenschilderwerk/">binnenschilderwerk</a>'],
            ["Houtwerk buiten", "€30 – €45 per m²", '<a href="/kosten/buitenschilderwerk/">buitenschilderwerk</a>'],
            ["Buitenkozijn", "€90 – €190", '<a href="/kosten/kozijnen-schilderen/">kozijnen</a>'],
            ["Tussenwoning buiten", "€1.500 – €3.450", '<a href="/kosten/huis-schilderen/">huis schilderen</a>'],
            ["Houtrot", "€50 – €275 per plek", '<a href="/kosten/houtrot-herstellen/">houtrot</a>'],
        ], num_vanaf=1)
        + _bronregel([HOMEDEAL_SCHILDER, ZOOFY_BINNEN, DSC_BUITEN],
                     "De bronnen geven we per kostenpagina met hun eigen bedragen, naast die van Topschilder. ")
    ),
    "verdieping": (
        "<h2>Zo lees je een offerte voor schilderwerk</h2>"
        "<p>Een goede offerte zet elk onderdeel apart, met aantal, eenheid en prijs. Let vooral op:</p>"
        '<ul class="checklist">'
        "<li><strong>Steiger of hoogwerker:</strong> inbegrepen of apart?</li>"
        "<li><strong>Houtrot:</strong> prijs per plek of een maximum, nooit open op regie.</li>"
        "<li><strong>Voorwerk:</strong> schuren, vullen, kitten en gronden staan erin.</li>"
        "<li><strong>Verf:</strong> merk, productnaam en aantal lagen.</li>"
        "<li><strong>Btw:</strong> 9% voor schilderwerk aan een woning ouder dan twee jaar, 21% voor houtvervanging.</li>"
        "<li><strong>Garantie:</strong> termijn en wat eronder valt, op papier.</li>"
        "</ul>"
        '<p>Heb je een offerte? <a href="/offerte-vergelijken/">Laat hem gratis checken met de offertechecker</a>. '
        'Wil je weten wat je hele huis kost? Gebruik de <a href="/kosten/calculator/">huiscalculator</a>. '
        'Meer achtergrond in <a href="/kennisbank/goede-offerte-schilderwerk/">zo herken je een goede offerte</a>.</p>'
        "<h2>Waarom prijzen per regio verschillen</h2>"
        "<p>In Noord-Holland en Utrecht rekenen schilders ongeveer 9 tot 13% meer dan het landelijke gemiddelde, in Flevoland en Overijssel 4 tot 5% minder. "
        "Dat komt door huur, loonkosten en hoe druk schilders het hebben. Op elke kostenpagina staat de prijs voor een aantal plaatsen. Die regiocorrectie is een eigen inschatting.</p>"
    ),
    "faq": [
        ("Wat kost een schilder per uur in 2026?",
         "Gemiddeld €45 tot €65 per uur exclusief btw. Een zzp'er zit vaak aan de onderkant, een bedrijf met personeel aan de bovenkant. Inclusief 9% btw is dat €49 tot €71."),
        ("Wat kost schilderen per m²?",
         "Binnen €10 tot €16 per m² voor muren en €12 tot €22 voor plafonds. Buiten €30 tot €45 per m² houtwerk. Alles inclusief verf en btw."),
        ("Wat kost het om een huis buiten te laten schilderen?",
         "Een tussenwoning €1.500 tot €3.450, een vrijstaande woning €3.250 tot €7.200. Houtrot en steiger kunnen erbij komen."),
        ("Wat kost een hele woning binnen schilderen?",
         "€3.900 tot €8.500 voor een tussenwoning met muren, plafonds, deuren, kozijnen en trap."),
        ("Zijn deze prijzen inclusief btw?",
         "Ja, inclusief verf en btw, behalve het uurtarief. Voor schilderwerk aan een woning ouder dan twee jaar geldt 9%. Bij nieuwbouw van twee jaar of jonger en bedrijfspanden 21%, en dan liggen de prijzen ongeveer 11% hoger."),
        ("Hoe weet ik of mijn offerte te duur is?",
         "Leg elke post naast de richtprijzen op de kostenpagina's, of plak je offerte in de gratis offertechecker. Die laat per post zien of hij binnen de bandbreedte valt."),
        ("Waarom verschillen offertes van schilders zo veel?",
         "Door de staat van het hout, houtrot, steigerwerk, het aantal lagen en de verf. Vergelijk daarom per onderdeel, niet alleen het totaal."),
        ("Wanneer is een schilder het goedkoopst?",
         "Buitenwerk in september en oktober, binnenwerk in de winter. Dan hebben schilders vaker ruimte in hun planning."),
    ],
}
