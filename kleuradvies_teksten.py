# -*- coding: utf-8 -*-
"""
Teksten voor /kleuradvies/ (zie kleuradvies.py voor de opbouw).

Onderwerpen gekozen op basis van Semrush, database nl, november 2026 (zoekvolume per
maand, gemiddeld):
- kozijnen: antraciet kozijnen 590, zwarte kozijnen 480, kozijn kleuren 170,
  kleur kozijnen 140, witte/groene kozijnen 170, grijze kozijnen 140
- grachtengroen 1.300, monumentengroen 1.300, RAL 6009 3.600, RAL 6012 1.000
- voordeur: kleur voordeur 390, voordeur kleur 320, voordeur antraciet 320
- woonkamer: kleur woonkamer muur 590, kleur woonkamer 260, accentmuur 170, warme kleuren 720
- slaapkamer: kleur slaapkamer 720, rustgevende kleuren slaapkamer 590, kleur slaapkamer muur 260
- keuken en hal: kleur keuken 720, kleur hal 70, kleur gang 70, kleur plafond 210
- kleurcombinaties 390, welke kleuren passen bij elkaar 260, kleuren combineren 210, 60 30 10 regel 140
- trends: kleur van het jaar 2026 1.300, kleurtrends 2026 90, kleur van het jaar 2027 50,
  saliegroen 6.600 (muurverf 590), greige 2.400 (muurverf 880), terracotta muurverf 1.300
- lichtval: weinig zoekvolume, wel gevraagd als verdieping (noorden/zuiden).

RAL: codes en namen uit de officiële RAL Classic-lijst; hex als benadering uit de
Wikipedia-lijst van RAL-kleuren. Codes die niet met 'RAL ' beginnen zijn geen verfkleur
(baksteen, vloer) en staan alleen in de tekening.
"""

# code -> (naam, hex, noot)
RAL = {
    "RAL 9001": ("Crèmewit", "#EFEBDC", "Warm wit met een vleugje geel."),
    "RAL 9010": ("Zuiver wit", "#F7F9EF", "Zacht, iets warm wit. Veel gebruikt op muren, plafonds en kozijnen."),
    "RAL 9016": ("Verkeerswit", "#F1F0EA", "Helder wit. De hexwaarde verschilt per bron."),
    "RAL 9002": ("Grijswit", "#D7D5CB", "Wit met een grijze ondertoon."),
    "RAL 1013": ("Parelwit", "#E3D9C6", "Gebroken wit met een beige ondertoon."),
    "RAL 1015": ("Licht ivoorkleurig", "#E6D2B5", "Warm, zacht ivoor."),
    "RAL 1001": ("Beige", "#D0B084", ""),
    "RAL 1002": ("Zandgeel", "#D2AA6D", ""),
    "RAL 7044": ("Zijdegrijs", "#B7B3A8", "Licht grijs met een warme ondertoon, de richting van ‘greige’."),
    "RAL 7032": ("Kiezelgrijs", "#B5B0A1", "Warm grijs, iets donkerder dan zijdegrijs."),
    "RAL 7035": ("Lichtgrijs", "#CBD0CC", "Koel, licht grijs."),
    "RAL 7039": ("Kwartsgrijs", "#6B695F", "Warm middengrijs met een bruine ondertoon."),
    "RAL 7022": ("Ombergrijs", "#4B4D46", "Donker grijs met een groenbruine ondertoon."),
    "RAL 7016": ("Antracietgrijs", "#373F43", "Donkergrijs met een blauwe ondertoon."),
    "RAL 7021": ("Zwartgrijs", "#2F3234", "Bijna zwart, zachter dan gitzwart."),
    "RAL 9005": ("Gitzwart", "#0A0A0D", ""),
    "RAL 6009": ("Dennengroen", "#26392F", "Diep donkergroen."),
    "RAL 6012": ("Zwartgroen", "#31403D", "Groen dat bijna zwart lijkt. Dicht bij wat vaak monumentengroen heet."),
    "RAL 6005": ("Mosgroen", "#0F4336", "Diep groen met een blauwe ondertoon."),
    "RAL 6003": ("Olijfgroen", "#4B573E", ""),
    "RAL 6011": ("Resedagroen", "#68825B", "Middelgroen met grijs."),
    "RAL 6021": ("Bleekgroen", "#86A47C", "Zacht grijsgroen, de richting van ‘saliegroen’."),
    "RAL 6019": ("Pastelgroen", "#B9CEAC", "Heel licht groen."),
    "RAL 5014": ("Duifblauw", "#6C7C98", "Rustig grijsblauw."),
    "RAL 5011": ("Staalblauw", "#232C3F", "Heel donker blauw."),
    "RAL 5024": ("Pastelblauw", "#6093AC", "Zacht middelblauw."),
    "RAL 5008": ("Grijsblauw", "#2B3A44", "Donker blauw met veel grijs, de richting van indigo."),
    "RAL 3005": ("Wijnrood", "#5E2028", "Ligt dicht bij wat vaak ossenbloedrood heet."),
    "RAL 3009": ("Oxiderood", "#6D342D", "Bruinrood."),
    "RAL 3012": ("Beigerood", "#C6846D", "Zacht roze-oranje, de richting van ‘terracotta’."),
    "RAL 8023": ("Oranjebruin", "#A65E2F", "Warm roestbruin."),
    "RAL 8011": ("Notenbruin", "#5A3826", ""),
    "RAL 1006": ("Maisgeel", "#E4A010", "Warm, vol geel."),
    # geen verfkleuren, alleen voor de tekening
    "steen-rood": ("Rode baksteen", "#9a4a36", ""),
    "steen-oranje": ("Oranjerode baksteen", "#b5623f", ""),
    "steen-geel": ("Gele baksteen", "#d2b27a", ""),
    "steen-bruin": ("Bruine baksteen", "#6e4a36", ""),
    "steen-grijs": ("Grijze baksteen", "#8a8580", ""),
    "steen-wit": ("Witte gevel (pleister)", "#ece8de", ""),
    "vloer-eiken": ("Eiken vloer", "#b88a53", ""),
    "vloer-licht": ("Lichte vloer", "#d9c4a3", ""),
    "vloer-donker": ("Donkere vloer", "#5b4330", ""),
    "vloer-grijs": ("Grijze tegelvloer", "#9c9890", ""),
}

EXTRA_BRONNEN = {
    "flexa-2027": ("Rodi Media, ‘Flexa introduceert de kleur van het jaar voor 2027’",
                   "https://www.rodi.nl/wonen/accessoires/506651/flexa-introduceert-de-kleur-van-het-jaar-voor-2027-dit-is-m-"),
    "flexa-2026": ("Rodi Media, ‘Flexa verrast iedereen met de Kleur van het jaar 2026’",
                   "https://www.rodi.nl/wonen/accessoires/461495/wil-je-zien-flexa-verrast-iedereen-met-de-kleur-van-het-jaar-2026"),
    "pantone-2026": ("Pantone, persbericht ‘Pantone announces Color of the Year 2026: Cloud Dancer’",
                     "https://www.pantone.com/articles/press-releases/pantone-announces-color-of-the-year-2026-cloud-dancer"),
}

K = "/kleuren-kiezen/"
LINKS_BUITEN = [
    ("/schilderwerk/buitenschilderwerk/", "Buitenschilderwerk laten doen"),
    ("/kosten/kozijnen-schilderen/", "Wat kost kozijnen schilderen?"),
    ("/kosten/calculator/", "Reken je eigen huis door"),
    (K, "Probeer kleuren in de kleurenkiezer"),
    ("/onderhoudscheck/", "Doe de onderhoudscheck"),
]
LINKS_BINNEN = [
    ("/schilderwerk/binnenschilderwerk/", "Binnenschilderwerk laten doen"),
    ("/kosten/binnenschilderwerk/", "Wat kost binnenschilderwerk?"),
    ("/kosten/schilderen-per-m2/", "Schilderen: prijs per m²"),
    ("/verfcalculator/", "Bereken hoeveel verf je nodig hebt"),
    ("/kennisbank/latex-of-muurverf/", "Latex of muurverf?"),
]


def _p(*zinnen):
    return "".join(f"<p>{z}</p>" for z in zinnen)


def _ul(*items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def _tip(t):
    return f'<p class="ka-tip">{t}</p>'


PAGINAS = []

# ---------------------------------------------------------------------------
# 1. Kozijnen
# ---------------------------------------------------------------------------
PAGINAS.append(dict(
    slug="kozijnen", kort="Kleur kozijnen kiezen",
    teaser="Antraciet, zwart, wit, crème of groen: wat past bij jouw steen en dak?",
    titel="Kleur kozijnen kiezen: antraciet, zwart, wit of groen",
    h1="Welke kleur kozijnen past bij jouw huis?",
    description="Antraciet, zwart, wit, crème of groen: zo kies je de kleur van je kozijnen bij rode, gele of "
                "bruine steen. Met RAL-codes, voorbeelden en tips.",
    badge="Kleuradvies buiten",
    intro="De kozijnen bepalen voor een groot deel hoe je huis eruitziet. Een andere kleur kan een woning "
          "frisser, strakker of juist warmer maken. Op deze pagina lees je hoe je kiest, welke kleuren goed "
          "samengaan met de steen en het dak, en waar je op let bij donkere kleuren.",
    snel='<a href="#steen">Kleur per steen</a> · <a href="#donker">Antraciet of zwart</a> · <a href="#combinaties">Voorbeelden</a>',
    secties=[
        ("Begin bij wat blijft", _p(
            "Je kiest de kleur van je kozijnen niet los. Kijk eerst naar wat je niet verandert: de kleur van de "
            "steen, de voegen, het dak en eventueel glas-in-lood of een gekleurde voordeur. Die vormen de basis. "
            "De kozijnkleur moet daar rustig naast staan of er een duidelijk, bewust contrast mee maken.",
            "Een handige vuistregel: kies één basiskleur voor kozijnen, boeidelen en dakgoot, en hooguit één "
            "accent voor de voordeur of de ramen (de beweegbare delen). Meer kleuren tegelijk maakt een gevel "
            "snel onrustig.")),
        ("steen", "Welke kleur kozijnen past bij de steen?", _p(
            "<strong>Rode of oranjerode baksteen.</strong> De klassieke keuze is wit of crèmewit, eventueel met "
            "groene ramen of een groene voordeur. Crèmewit (RAL 9001) is wat zachter dan helder wit en past goed "
            "bij warme rode steen. Wil je het moderner, dan staat antraciet (RAL 7016) ook mooi bij rode steen, "
            "zeker als de voegen donker zijn.",
            "<strong>Gele of lichte baksteen.</strong> Hier werkt een donkere kozijnkleur vaak beter dan wit, "
            "omdat wit wegvalt tegen de lichte steen. Denk aan dennengroen (RAL 6009), antraciet of een "
            "warm grijs als kwartsgrijs (RAL 7039). Crèmewit kan ook, maar maakt de gevel vlakker.",
            "<strong>Bruine of donkere baksteen.</strong> Lichte kozijnen geven contrast en maken de gevel "
            "lichter: crèmewit of licht ivoor (RAL 1015). Zwartgrijs (RAL 7021) maakt het geheel juist strak en "
            "donker, wat vooral bij moderne woningen goed werkt.",
            "<strong>Witte of lichte gepleisterde gevel.</strong> Bijna alles past. Zwart of antraciet geeft een "
            "strak, eigentijds beeld. Groen of blauw grijpt terug op oude kustdorpen en monumenten.")),
        ("donker", "Antraciet of zwart?", _p(
            "Antraciet en zwart zijn al jaren populair: in Nederland wordt per maand ongeveer 590 keer gezocht op "
            "‘antraciet kozijnen’ en 480 keer op ‘zwarte kozijnen’ (Semrush, november 2026). Het verschil is "
            "kleiner dan je denkt. Antracietgrijs (RAL 7016) heeft een blauwe ondertoon en oogt iets zachter. "
            "Gitzwart (RAL 9005) is hard en grafisch. Zwartgrijs (RAL 7021) zit daartussen.",
            "Let bij donkere kleuren op houten kozijnen op de warmte. Een donkere kleur wordt in de zon veel "
            "warmer dan wit. Hout werkt daardoor meer, en verf en kit krijgen het zwaarder. Vraag je schilder "
            "naar een verf die daarvoor geschikt is, en houd vooral op de zuid- en westgevel rekening met "
            "iets vaker onderhoud.")
         + _tip("Twijfel je tussen twee donkere tinten? Laat beide als proefvlak op één kozijn zetten en kijk "
                "op een zonnige en een bewolkte dag. Het verschil tussen antraciet en zwart zie je pas buiten.")),
        ("Wit, gebroken wit en crème", _p(
            "Wit is niet zomaar wit. Zuiver wit (RAL 9010) is zacht en een beetje warm. Crèmewit (RAL 9001) is "
            "duidelijk geler en past bij oudere woningen en warme steen. Verkeerswit (RAL 9016) is helder en "
            "koel, en zie je veel bij nieuwbouw en kunststof kozijnen. Meer over het verschil lees je in "
            "<a href=\"/kennisbank/ral-9010-of-ral-9001/\">RAL 9010 of RAL 9001</a>.",
            "Witte kozijnen laten vuil en groene aanslag sneller zien. Een keer per jaar afwassen houdt ze mooi "
            "en laat de verf langer meegaan.")),
        ("Groen, blauw en andere kleuren", _p(
            "Donkergroen is een oude Nederlandse kleur voor kozijnen en ramen. Lees meer op onze pagina over "
            "<a href=\"/kleuradvies/grachtengroen/\">grachtengroen en monumentengroen</a>. Blauw zie je vooral "
            "in kustdorpen en bij boerderijen; duifblauw (RAL 5014) is een rustige keuze. Een warme houtkleur "
            "met transparante beits laat de nerf van het hout zien, maar vraagt vaker onderhoud dan dekkende verf.")),
        ("Andere kleur dan nu: waar let je op?", _ul(
            "<strong>Meer lagen.</strong> Van licht naar donker of andersom dekt één laag meestal niet. Reken op "
            "een extra laag, soms een grondlaag in een tussenkleur.",
            "<strong>Vergunning.</strong> Bij een monument of in een beschermd stadsgezicht is een andere kleur "
            "soms vergunningplichtig. Vraag het vooraf na bij de gemeente. Woon je in een VvE of huur je, vraag "
            "het dan de VvE of de verhuurder.",
            "<strong>Kunststof kozijnen</strong> kun je ook laten schilderen, met een speciale verf. Lees wat dat "
            "kost op <a href=\"/kosten/kunststof-kozijnen-schilderen/\">kunststof kozijnen schilderen</a>.",
            "<strong>Buren.</strong> In een rij woningen met dezelfde kozijnen valt een afwijkende kleur op. Dat "
            "mag meestal, maar het is goed om te weten.")),
    ],
    stalen_kop="Voorbeelden: kozijnkleur bij de steen",
    stalen_intro="Zes combinaties van steen, kozijn en voordeur. Wil je ze op een hele woning zien? Probeer ze in de <a href=\"/kleuren-kiezen/\">kleurenkiezer</a>.",
    stalen=[
        dict(naam="Rode steen, crèmewit en groen", soort="gevel", kleuren=[
            ("Steen", "steen-rood", "steen"), ("Kozijnen", "RAL 9001", "kozijn"),
            ("Ramen", "RAL 6009", "raam"), ("Voordeur", "RAL 6009", "deur")],
            uitleg="De klassieke Nederlandse combinatie. Groen in de ramen geeft diepte zonder druk te worden."),
        dict(naam="Rode steen en antraciet", soort="gevel", kleuren=[
            ("Steen", "steen-oranje", "steen"), ("Kozijnen", "RAL 7016", "kozijn"),
            ("Voordeur", "RAL 7016", "deur")],
            uitleg="Strak en eigentijds. Werkt het best als de voegen ook donker zijn."),
        dict(naam="Gele steen en dennengroen", soort="gevel", kleuren=[
            ("Steen", "steen-geel", "steen"), ("Kozijnen", "RAL 6009", "kozijn"),
            ("Ramen", "RAL 9001", "raam"), ("Voordeur", "RAL 6009", "deur")],
            uitleg="Op lichte steen heeft een donkere kozijnkleur meer kracht dan wit."),
        dict(naam="Bruine steen en licht ivoor", soort="gevel", kleuren=[
            ("Steen", "steen-bruin", "steen"), ("Kozijnen", "RAL 1015", "kozijn"),
            ("Voordeur", "RAL 3005", "deur")],
            uitleg="Lichte kozijnen maken een donkere gevel vriendelijker. Een wijnrode deur geeft warmte."),
        dict(naam="Grijze steen en zwartgrijs", soort="gevel", kleuren=[
            ("Steen", "steen-grijs", "steen"), ("Kozijnen", "RAL 7021", "kozijn"),
            ("Voordeur", "RAL 1006", "deur")],
            uitleg="Bij moderne nieuwbouw. Eén warm accent op de deur houdt het geheel levendig."),
        dict(naam="Witte gevel en gitzwart", soort="gevel", kleuren=[
            ("Gevel", "steen-wit", "steen"), ("Kozijnen", "RAL 9005", "kozijn"),
            ("Voordeur", "RAL 9005", "deur")],
            uitleg="Grafisch en tijdloos. Zwart op wit laat de vorm van de ramen goed zien."),
    ],
    extra_codes=["RAL 9010", "RAL 9016", "RAL 7039", "RAL 5014"],
    links=LINKS_BUITEN + [("/kosten/kunststof-kozijnen-schilderen/", "Kunststof kozijnen schilderen: kosten"),
                          ("/kennisbank/welke-verf-voor-kozijnen/", "Welke verf voor kozijnen?"),
                          ("/inspiratie/", "Kleurcombinaties per woningtype")],
    bronnen=["rijksoverheid"],
    cta_kop="Laat je kozijnen in een nieuwe kleur schilderen",
    cta_tekst="Weet je welke kleur je wilt? Vermeld de RAL-code in je aanvraag, dan rekent de schilder met de juiste verf en het aantal lagen.",
    form_kop="Offerte voor je kozijnen",
    faq=[
        ("Welke kleur kozijnen is het meest tijdloos?",
         "Wit, crèmewit en donkergroen zie je al meer dan honderd jaar op Nederlandse huizen. Antraciet is "
         "nieuwer, maar wordt al zo lang gebruikt dat het niet snel gedateerd oogt. Kies wat past bij de steen "
         "en het dak; dat blijft het langst mooi."),
        ("Is antraciet of zwart beter voor houten kozijnen?",
         "Voor het hout maakt het weinig uit: beide zijn donker en worden warm in de zon. Antraciet (RAL 7016) "
         "oogt iets zachter, zwart (RAL 9005) strakker. Vraag je schilder om een verf die geschikt is voor "
         "donkere kleuren in de zon."),
        ("Welke kleur kozijnen past bij rode baksteen?",
         "Crèmewit of wit is de klassieke keuze, vaak met groene ramen of een groene voordeur. Antraciet past "
         "ook, vooral bij donkere voegen. Felle kleuren vloeken vaak met warm rood."),
        ("Kost een andere kleur kozijnen meer?",
         "Meestal wel, omdat er een extra laag nodig is als je van licht naar donker gaat of andersom. Op "
         "<a href=\"/kosten/kozijnen-schilderen/\">kozijnen schilderen</a> lees je wat schilderen kost."),
        ("Mag ik de kleur van mijn kozijnen zomaar veranderen?",
         "In de meeste gevallen wel. Bij een monument, in een beschermd stadsgezicht of in een VvE gelden soms "
         "regels. Vraag het dan vooraf na bij de gemeente of de VvE."),
    ],
))

# ---------------------------------------------------------------------------
# 2. Grachtengroen en monumentengroen
# ---------------------------------------------------------------------------
PAGINAS.append(dict(
    slug="grachtengroen", kort="Grachtengroen en monumentengroen",
    teaser="Wat is het verschil, welke RAL-code komt in de buurt en waar past het?",
    titel="Grachtengroen en monumentengroen: kleur en RAL-code",
    h1="Grachtengroen en monumentengroen: wat is het en welke code kies je?",
    description="Wat is grachtengroen, wat is monumentengroen en welke RAL-code komt in de buurt? Uitleg over "
                "de geschiedenis van groene kozijnen, met voorbeelden.",
    badge="Kleuradvies buiten",
    intro="Grachtengroen en monumentengroen zijn twee van de bekendste kleurnamen voor kozijnen in Nederland. "
          "Er wordt elke maand zo’n 1.300 keer op elk van beide gezocht (Semrush, november 2026). Toch is geen "
          "van beide een vaste kleur. Hier lees je wat de namen betekenen, welke RAL-codes in de buurt komen en "
          "hoe je de goede tint kiest.",
    snel='<a href="#verschil">Het verschil</a> · <a href="#code">RAL-code</a> · <a href="#combinaties">Voorbeelden</a>',
    secties=[
        ("verschil", "Wat is het verschil?", _p(
            "Beide namen staan voor een heel donker groen dat op afstand bijna zwart lijkt. Het groen zie je pas "
            "goed als de zon erop staat. <strong>Grachtengroen</strong> verwijst naar de grachtenpanden in "
            "oude binnensteden. <strong>Monumentengroen</strong> is een verzamelnaam voor het donkergroen dat "
            "op veel monumenten zit.",
            "Elk verfmerk heeft er een eigen versie van, en die verschillen onderling. De ene is groener, de "
            "andere grijzer of blauwer. Twee potten ‘grachtengroen’ van verschillende merken zijn dus zelden "
            "precies gelijk.")),
        ("Een korte geschiedenis van groene kozijnen", _p(
            "Groen met wit is een oude Nederlandse combinatie. Volgens het Nederlands Openluchtmuseum waren "
            "groene kozijnen eerst iets voor deftige huizen, omdat groene verf duur was. Toen in de negentiende "
            "eeuw goedkoper groen op de markt kwam, kozen veel meer mensen voor groen.",
            "Het museum schrijft ook dat de naam monumentengroen pas uit de twintigste eeuw komt. Daarvoor werd "
            "groen gebruikt in veel tinten, van grijsgroen tot helder lichtgroen. ‘Historisch’ groen is dus niet "
            "per se het donkerste groen.",
            "Groen verandert met de jaren. Groen dat uit geel en blauw pigment is gemengd, wordt in de zon "
            "blauwer. Het oude groen dat je op een gevel ziet, was op de dag dat het gezet werd vaak anders van "
            "kleur.")),
        ("code", "Welke RAL-code komt in de buurt?", _p(
            "Er is geen officiële RAL-code voor grachtengroen of monumentengroen. Wil je toch een code noemen, "
            "dan komen deze in de buurt:")
         + _ul("<strong>Zwartgroen (RAL 6012)</strong>: groen dat bijna zwart is, met een grijze ondertoon. "
               "Ligt dicht bij wat veel merken monumentengroen noemen.",
               "<strong>Dennengroen (RAL 6009)</strong>: iets groener en warmer. Een veilige keuze als je het "
               "groen duidelijker wilt zien.",
               "<strong>Mosgroen (RAL 6005)</strong>: dieper en blauwer groen, met meer kleur.")
         + _p("Neem bij je verfwinkel of schilder een staal mee van de kleur die je mooi vindt, bijvoorbeeld een "
              "foto of een stukje van een buurpand. Een verfwinkel kan een kleur ook meten en namengen.")
         + _tip("Woon je in een monument of beschermd stadsgezicht? Dan heeft de gemeente soms een eigen "
                "kleurenlijst. Vraag die eerst op, voordat je een kleur kiest.")),
        ("Waar past grachtengroen?", _p(
            "Donkergroen past op bijna elk huis met baksteen: rode, oranje en gele steen. Het is de bekende kleur "
            "voor ramen en voordeuren bij oude stadshuizen, maar staat ook mooi op jaren-30-woningen en "
            "boerderijen. Bij een witte of lichte gepleisterde gevel geeft donkergroen een fris, klassiek beeld.",
            "Kies je groen voor de ramen en wit of crème voor de kozijnen? Dan krijg je de klassieke "
            "Nederlandse combinatie. Groen voor alles (kozijnen, ramen en deur) is moderner en rustiger.",
            "Bekijk ook onze gidsen voor een <a href=\"/inspiratie/monument/\">monument</a> en een "
            "<a href=\"/inspiratie/jaren30/\">jaren-30-woning</a>.")),
        ("Onderhoud van donkergroen", _p(
            "Donkere kleuren warmen in de zon sterker op dan lichte. Hout werkt daardoor meer. Laat de schilder "
            "een verf gebruiken die daar tegen kan, en kijk elk voorjaar naar scheurtjes onderaan de kozijnen "
            "en bij de naden. Groen kan na jaren wat doffer en blauwer worden; een nieuwe laag in dezelfde "
            "kleur brengt de diepte terug.")),
    ],
    stalen_kop="Voorbeelden met donkergroen",
    stalen_intro="Drie tinten donkergroen en vier gevels. De tinten zijn RAL-kleuren die in de buurt komen van grachtengroen en monumentengroen.",
    stalen=[
        dict(naam="Drie tinten naast elkaar", soort="balk", kleuren=[
            ("Zwartgroen", "RAL 6012", 1), ("Dennengroen", "RAL 6009", 1), ("Mosgroen", "RAL 6005", 1)],
            uitleg="Van links naar rechts: grijzer, warmer en blauwer. Op een kozijn lijkt elke tint donkerder."),
        dict(naam="Klassiek: crème met groene ramen", soort="gevel", kleuren=[
            ("Steen", "steen-rood", "steen"), ("Kozijnen", "RAL 9001", "kozijn"),
            ("Ramen", "RAL 6012", "raam"), ("Voordeur", "RAL 6012", "deur")],
            uitleg="Zoals je het in veel oude binnensteden ziet."),
        dict(naam="Alles in dennengroen", soort="gevel", kleuren=[
            ("Steen", "steen-oranje", "steen"), ("Kozijnen", "RAL 6009", "kozijn"),
            ("Voordeur", "RAL 6009", "deur")],
            uitleg="Rustiger en moderner. Werkt goed bij oranjerode steen."),
        dict(naam="Witte gevel met mosgroen", soort="gevel", kleuren=[
            ("Gevel", "steen-wit", "steen"), ("Kozijnen", "RAL 9010", "kozijn"),
            ("Ramen", "RAL 6005", "raam"), ("Voordeur", "RAL 6005", "deur")],
            uitleg="Fris en klassiek, zoals bij gepleisterde herenhuizen."),
        dict(naam="Gele steen en zwartgroen", soort="gevel", kleuren=[
            ("Steen", "steen-geel", "steen"), ("Kozijnen", "RAL 6012", "kozijn"),
            ("Ramen", "RAL 1015", "raam"), ("Voordeur", "RAL 6012", "deur")],
            uitleg="Op lichte steen springt donkergroen er duidelijk uit."),
    ],
    links=LINKS_BUITEN + [("/inspiratie/monument/", "Kleuren voor een monument"),
                          ("/kennisbank/voordeur-schilderen/", "Voordeur schilderen")],
    bronnen=["olm-kozijn", "olm-gebouwen", "rijksoverheid"],
    cta_kop="Laat je kozijnen in donkergroen zetten",
    cta_tekst="Vraag de schilder om een proefvlak van twee tinten op je eigen kozijn. Dan zie je het verschil in je eigen licht.",
    form_kop="Offerte voor groene kozijnen",
    faq=[
        ("Wat is de RAL-code van grachtengroen?",
         "Die bestaat niet: grachtengroen is een naam, geen vaste kleur. Zwartgroen (RAL 6012) en dennengroen "
         "(RAL 6009) komen in de buurt. Elk verfmerk maakt een eigen versie."),
        ("Wat is het verschil tussen grachtengroen en monumentengroen?",
         "Er is geen vast verschil. Beide namen staan voor heel donker groen dat bijna zwart lijkt. Per verfmerk "
         "kan de ene iets groener of grijzer zijn dan de andere."),
        ("Is monumentengroen een historische kleur?",
         "De naam is niet zo oud als hij klinkt. Volgens het Nederlands Openluchtmuseum bestaat hij pas sinds de "
         "twintigste eeuw. Daarvoor werd groen in veel tinten gebruikt."),
        ("Past donkergroen bij een modern huis?",
         "Ja. Donkergroen voor kozijnen, ramen én deur geeft een rustig, eigentijds beeld. Het is een warmer "
         "alternatief voor antraciet."),
        ("Moet ik voor groene kozijnen een vergunning hebben?",
         "Meestal niet. Bij een monument of in een beschermd stadsgezicht kan dat anders zijn. Vraag het vooraf "
         "na bij je gemeente."),
    ],
))

# ---------------------------------------------------------------------------
# 3. Voordeur
# ---------------------------------------------------------------------------
PAGINAS.append(dict(
    slug="voordeur", kort="Kleur voordeur kiezen",
    teaser="Antraciet, groen, rood of blauw: welke kleur voordeur past bij je gevel?",
    titel="Kleur voordeur kiezen: ideeën met RAL-codes",
    h1="Welke kleur voordeur kies je?",
    description="Een voordeur in antraciet, groen, rood, blauw of geel? Zo kies je een kleur die past bij je "
                "kozijnen en steen. Met voorbeelden, RAL-codes en tips.",
    badge="Kleuradvies buiten",
    intro="De voordeur is het visitekaartje van je huis. Het is ook de plek waar je het makkelijkst iets "
          "durft: een deur is klein, en je kunt hem later weer anders laten schilderen. Hier lees je hoe je "
          "een kleur kiest die past bij je kozijnen, je steen en je straat.",
    secties=[
        ("Accent of rustig meedoen?", _p(
            "Er zijn twee manieren. Je kunt de voordeur in <strong>dezelfde kleur als de kozijnen</strong> "
            "zetten. Dan oogt de gevel rustig en is de deur een onderdeel van het geheel. Of je kiest de deur als "
            "<strong>accent</strong>: een kleur die er duidelijk uitspringt, terwijl de kozijnen rustig blijven.",
            "Een accentkleur werkt het best als hij iets terugpakt uit de gevel. Een rode deur bij rode steen "
            "voelt logisch. Een gele deur bij een grijze, moderne gevel geeft juist warmte.")),
        ("Populaire kleuren voor de voordeur", _ul(
            "<strong>Antraciet (RAL 7016).</strong> In Nederland wordt per maand zo’n 320 keer gezocht op "
            "‘voordeur antraciet’ (Semrush, november 2026). Past bij bijna alles en oogt strak.",
            "<strong>Donkergroen (RAL 6009 of 6012).</strong> Klassiek bij baksteen en witte kozijnen. Zie ook "
            "<a href=\"/kleuradvies/grachtengroen/\">grachtengroen en monumentengroen</a>.",
            "<strong>Wijnrood of oxiderood (RAL 3005 of 3009).</strong> Warm en uitnodigend, vooral bij "
            "crèmewitte kozijnen.",
            "<strong>Donkerblauw (RAL 5011).</strong> Deftig en rustig. Mooi bij witte gevels en lichte steen.",
            "<strong>Duifblauw (RAL 5014).</strong> Zachter blauw, past bij boerderijen en kustwoningen.",
            "<strong>Maisgeel (RAL 1006).</strong> Een vrolijk accent bij grijze of zwarte gevels.")),
        ("Let op de zon", _p(
            "Een voordeur op het zuiden of westen krijgt veel zon. Donkere kleuren worden dan warm, en een houten "
            "deur kan gaan werken of klemmen. Lichte en middentinten hebben daar minder last van. Kies je toch "
            "voor donker, vraag dan om een verf die daarvoor geschikt is. Felle rode en gele tinten kunnen in "
            "de volle zon sneller verkleuren dan rustige tinten.")),
        ("Voordeur en glans", _p(
            "Een voordeur wordt veel aangeraakt. Hoogglans of zijdeglans is beter schoon te houden dan mat en "
            "laat de kleur dieper lijken. Hoogglans laat wel elke oneffenheid zien, dus goed schuren is "
            "belangrijk. Hoe een schilder dat aanpakt, lees je in <a href=\"/kennisbank/voordeur-schilderen/\">voordeur "
            "schilderen</a>. Wil je een egale, strakke laag, dan kan een deur ook gespoten worden: zie "
            "<a href=\"/kosten/deuren-spuiten/\">deuren spuiten</a>.")),
        ("Het beslag telt mee", _p(
            "Zwart beslag past bij bijna elke kleur. Messing en goud staan mooi bij groen, blauw en rood. RVS past "
            "bij antraciet, grijs en moderne gevels. Laat het beslag tijdens het schilderen afnemen in plaats van "
            "afplakken; dan wordt de rand netter.")),
    ],
    stalen_kop="Voorbeelden: voordeur en kozijnen",
    stalen_intro="Zes combinaties van gevel, kozijn en voordeur.",
    stalen=[
        dict(naam="Antraciet op antraciet", soort="gevel", kleuren=[
            ("Steen", "steen-rood", "steen"), ("Kozijnen", "RAL 7016", "kozijn"), ("Voordeur", "RAL 7016", "deur")],
            uitleg="Rustig en strak: de deur doet mee met de kozijnen."),
        dict(naam="Wijnrode deur, crème kozijnen", soort="gevel", kleuren=[
            ("Steen", "steen-rood", "steen"), ("Kozijnen", "RAL 9001", "kozijn"), ("Voordeur", "RAL 3005", "deur")],
            uitleg="Warm en klassiek. Het rood pakt de steen terug."),
        dict(naam="Donkerblauw bij een witte gevel", soort="gevel", kleuren=[
            ("Gevel", "steen-wit", "steen"), ("Kozijnen", "RAL 9010", "kozijn"), ("Voordeur", "RAL 5011", "deur")],
            uitleg="Deftig, zoals bij oude herenhuizen."),
        dict(naam="Gele deur bij grijs", soort="gevel", kleuren=[
            ("Steen", "steen-grijs", "steen"), ("Kozijnen", "RAL 7021", "kozijn"), ("Voordeur", "RAL 1006", "deur")],
            uitleg="Eén vrolijk accent op een strakke, moderne gevel."),
        dict(naam="Duifblauw bij gele steen", soort="gevel", kleuren=[
            ("Steen", "steen-geel", "steen"), ("Kozijnen", "RAL 9001", "kozijn"), ("Voordeur", "RAL 5014", "deur")],
            uitleg="Zacht en vriendelijk. Mooi bij boerderijen en dorpswoningen."),
        dict(naam="Groene deur, witte kozijnen", soort="gevel", kleuren=[
            ("Steen", "steen-oranje", "steen"), ("Kozijnen", "RAL 9010", "kozijn"), ("Voordeur", "RAL 6009", "deur")],
            uitleg="De bekende Nederlandse combinatie, op de deur samengebracht."),
    ],
    extra_codes=["RAL 3009"],
    links=[("/schilderwerk/buitenschilderwerk/", "Buitenschilderwerk laten doen"),
           ("/kosten/deuren-spuiten/", "Wat kost deuren spuiten?"),
           ("/kennisbank/voordeur-schilderen/", "Voordeur schilderen: zo gaat het"),
           (K, "Probeer kleuren in de kleurenkiezer"),
           ("/schilderweer/", "Is het weer goed om buiten te schilderen?")],
    bronnen=[],
    cta_kop="Laat je voordeur in een nieuwe kleur zetten",
    cta_tekst="Een voordeur schilderen is een kleine klus. Combineer het met je kozijnen, dan betaal je de voorrijkosten maar één keer.",
    form_kop="Offerte voor je voordeur",
    faq=[
        ("Moet de voordeur dezelfde kleur hebben als de kozijnen?",
         "Nee. Dezelfde kleur geeft een rustig beeld, een andere kleur maakt van de deur een accent. Kies hooguit "
         "één accentkleur op de gevel, anders wordt het onrustig."),
        ("Welke kleur voordeur is het populairst?",
         "Antraciet wordt veel gekozen; in Nederland wordt er per maand zo’n 320 keer op ‘voordeur antraciet’ "
         "gezocht. Donkergroen en donkerblauw zijn klassieke alternatieven."),
        ("Is een donkere voordeur op het zuiden een probleem?",
         "Het kan. Donkere kleuren worden in de zon warm, waardoor een houten deur meer gaat werken. Met de "
         "juiste verf en goed onderhoud gaat het prima, maar reken op iets vaker bijwerken."),
        ("Welke glans kies ik voor een voordeur?",
         "Meestal hoogglans of zijdeglans. Dat is goed schoon te houden en geeft diepte. Hoogglans laat wel "
         "oneffenheden zien."),
        ("Wat kost een voordeur laten schilderen?",
         "Dat hangt af van de staat van de deur en of de kozijnen meegaan. Lees meer op "
         "<a href=\"/kosten/deuren-spuiten/\">deuren spuiten</a> en vraag een offerte voor je eigen deur."),
    ],
))

# ---------------------------------------------------------------------------
# 4. Woonkamer
# ---------------------------------------------------------------------------
PAGINAS.append(dict(
    slug="woonkamer", kort="Kleur woonkamer kiezen",
    teaser="Warm, licht of juist diep: muurkleuren en accentmuren voor de woonkamer.",
    titel="Kleur woonkamer kiezen: muurverf en accentmuur",
    h1="Welke kleur past in je woonkamer?",
    description="Muurverf voor de woonkamer kiezen: warme tinten, greige, groen of een donkere accentmuur. "
                "Met kleurcombinaties, RAL-codes en tips per lichtval.",
    badge="Kleuradvies binnen",
    intro="In de woonkamer breng je de meeste tijd door. De kleur van de muren bepaalt hoe groot, warm en "
          "rustig de kamer voelt. Hier lees je hoe je een kleur kiest die past bij je vloer, je meubels en het "
          "licht, en wanneer een accentmuur een goed idee is.",
    snel='<a href="#stappen">In vier stappen</a> · <a href="#accentmuur">Accentmuur</a> · <a href="#combinaties">Voorbeelden</a>',
    secties=[
        ("stappen", "In vier stappen naar een kleur", "<ol>"
         "<li><strong>Kijk naar wat blijft.</strong> Je vloer, de bank, de keuken en grote kasten veranderen niet "
         "zo snel. Hebben die een warme (geel, rood, bruin) of koele (grijs, blauw) ondertoon? Kies een muurkleur "
         "met dezelfde ondertoon.</li>"
         "<li><strong>Kijk naar het licht.</strong> Een kamer op het noorden krijgt koel licht; daar werken warme "
         "tinten beter. Lees meer op <a href=\"/kleuradvies/lichtval/\">kleur en lichtval</a>.</li>"
         "<li><strong>Kies een basis en een accent.</strong> Een rustige kleur voor de meeste muren, en eventueel "
         "één accent. De <a href=\"/kleuradvies/kleurcombinaties/\">60-30-10-regel</a> helpt daarbij.</li>"
         "<li><strong>Test op de muur.</strong> Zet een proefvlak van minstens een A4 op twee muren en kijk "
         "’s ochtends, ’s middags en ’s avonds bij lamplicht.</li></ol>"),
        ("Licht of donker?", _p(
            "Lichte kleuren kaatsen meer licht terug. Een kamer voelt daardoor groter en lichter. Gebroken wit, "
            "zacht beige en lichtgrijs zijn veilige keuzes. Het nadeel: een heel lichte kamer kan kaal aanvoelen, "
            "zeker met veel witte meubels.",
            "Donkere kleuren maken een kamer intiemer. Dat werkt goed in een grote kamer met veel licht, of in "
            "een deel van de kamer waar je ’s avonds zit. In een kleine, donkere kamer kan het benauwd worden. "
            "Een donkere kleur op de muur met een licht plafond geeft houvast.")),
        ("Warme kleuren en aardetinten", _p(
            "Warme kleuren zijn kleuren met geel, rood of bruin erin: zandkleur, oker, terracotta, warm groen en "
            "greige (grijs met beige). Er wordt veel naar gezocht: ‘warme kleuren’ zo’n 720 keer per maand, "
            "‘greige muurverf’ 880 keer en ‘terracotta muurverf’ 1.300 keer (Semrush, november 2026).",
            "Warme kleuren maken een woonkamer gezellig en passen goed bij houten vloeren en meubels. Combineer "
            "ze met gebroken wit op het plafond en de kozijnen. Wil je ook weten welke kleuren nu in opkomst zijn? "
            "Lees <a href=\"/kleuradvies/kleurtrends/\">kleurtrends 2026 en 2027</a>.")),
        ("accentmuur", "Een accentmuur: wel of niet?", _p(
            "Een accentmuur is één muur in een andere, vaak donkerdere of vollere kleur. Hij trekt de aandacht en "
            "kan een kamer indelen, bijvoorbeeld de zithoek of de eettafel.")
         + _ul("Kies een muur die al opvalt: achter de bank, achter de eettafel of de muur met een schoorsteen.",
               "Vermijd een muur met veel deuren of ramen. Dan wordt het een rommelig vlak.",
               "Kies een kleur uit iets wat al in de kamer staat: een kussen, een kleed of een schilderij.",
               "Wil je het rustiger? Zet de accentkleur ook op een kast of een raamkozijn. Dan voelt het minder los.")),
        ("Plafond, kozijnen en plinten", _p(
            "Een wit plafond maakt een kamer hoger. Zuiver wit (RAL 9010) is zacht en past bij bijna elke "
            "muurkleur. Bij een warme muurkleur kan een iets gebroken wit op het plafond rustiger zijn dan helder wit.",
            "Plinten en binnenkozijnen zijn meestal wit, maar dat hoeft niet. Plinten in de muurkleur maken een "
            "kamer strakker en rustiger. Gebruik op houtwerk een zijdeglans lak: die is beter schoon te houden dan "
            "muurverf.")),
        ("Muurverf: mat of zijdeglans?", _p(
            "Op muren in de woonkamer gebruik je meestal matte muurverf. Die laat oneffenheden minder zien en "
            "geeft een rustige, zachte kleur. Een schrobvaste matte verf kun je ook afnemen. Meer uitleg vind je "
            "in <a href=\"/kennisbank/latex-of-muurverf/\">latex of muurverf</a>. Hoeveel verf je nodig hebt, "
            "bereken je met de <a href=\"/verfcalculator/\">verfcalculator</a>.")),
    ],
    stalen_kop="Voorbeelden voor de woonkamer",
    stalen_intro="Zes kamers met muur, accentmuur, houtwerk en vloer. De linkermuur in de tekening is de accentmuur.",
    stalen=[
        dict(naam="Licht en warm", soort="kamer", kleuren=[
            ("Muren", "RAL 1013", "muur"), ("Accentmuur", "RAL 1001", "accent"),
            ("Houtwerk", "RAL 9010", "hout"), ("Vloer", "vloer-eiken", "vloer")],
            uitleg="Parelwit met een beige accent. Veilig, licht en gezellig bij een eiken vloer."),
        dict(naam="Greige met groen", soort="kamer", kleuren=[
            ("Muren", "RAL 7044", "muur"), ("Accentmuur", "RAL 6003", "accent"),
            ("Houtwerk", "RAL 9010", "hout"), ("Vloer", "vloer-licht", "vloer")],
            uitleg="Zijdegrijs is grijs met een warme ondertoon. Olijfgroen erbij maakt het rijker."),
        dict(naam="Terracotta-accent", soort="kamer", kleuren=[
            ("Muren", "RAL 9001", "muur"), ("Accentmuur", "RAL 3012", "accent"),
            ("Houtwerk", "RAL 9001", "hout"), ("Vloer", "vloer-eiken", "vloer")],
            uitleg="Crèmewit met een terracotta muur achter de bank. Warm en zonnig."),
        dict(naam="Diep groen in de zithoek", soort="kamer", kleuren=[
            ("Muren", "RAL 9010", "muur"), ("Accentmuur", "RAL 6009", "accent"),
            ("Houtwerk", "RAL 6009", "hout"), ("Vloer", "vloer-eiken", "vloer")],
            uitleg="Donkergroen op één muur én op het houtwerk. Voelt rustig en luxe."),
        dict(naam="Koel en rustig", soort="kamer", kleuren=[
            ("Muren", "RAL 7035", "muur"), ("Accentmuur", "RAL 5014", "accent"),
            ("Houtwerk", "RAL 9016", "hout"), ("Vloer", "vloer-grijs", "vloer")],
            uitleg="Voor een kamer met veel zon. Lichtgrijs en duifblauw bij een grijze vloer."),
        dict(naam="Donker en knus", soort="kamer", kleuren=[
            ("Muren", "RAL 7039", "muur"), ("Accentmuur", "RAL 7022", "accent"),
            ("Houtwerk", "RAL 7039", "hout"), ("Vloer", "vloer-donker", "vloer")],
            uitleg="Warm middengrijs met een donkere accentmuur. Alleen in een ruime, lichte kamer."),
    ],
    links=LINKS_BINNEN + [("/kosten/latex-spuiten/", "Wat kost latex spuiten?"),
                          ("/kosten/plafond-schilderen/", "Wat kost een plafond schilderen?")],
    bronnen=[],
    cta_kop="Laat je woonkamer schilderen",
    cta_tekst="Een schilder zet je kleur strak en egaal op de muur, ook rond plinten en plafond. Vermeld je kleurcode in de aanvraag.",
    form_kop="Offerte voor je woonkamer",
    faq=[
        ("Welke kleur maakt een woonkamer groter?",
         "Lichte kleuren met een zachte ondertoon, zoals gebroken wit, parelwit of lichtgrijs. Zet dezelfde of "
         "een iets lichtere kleur op het plafond, dan lopen muur en plafond in elkaar over."),
        ("Welke muurkleur past bij een eiken vloer?",
         "Warme tinten passen goed: gebroken wit, beige, greige, zacht groen en terracotta. Koel blauw en koel "
         "grijs kunnen tegen het warme hout kil aanvoelen."),
        ("Welke muur kies ik voor een accentmuur?",
         "Een muur die al opvalt en weinig deuren of ramen heeft, zoals de muur achter de bank of de eettafel."),
        ("Moet het plafond wit zijn?",
         "Nee, maar wit maakt een kamer hoger en lichter. Bij een warme muurkleur is gebroken wit vaak rustiger "
         "dan helder wit."),
        ("Hoeveel kost het om een woonkamer te laten schilderen?",
         "Dat hangt af van het aantal vierkante meter, de staat van de muren en of het plafond meegaat. Lees de "
         "richtprijzen op <a href=\"/kosten/binnenschilderwerk/\">binnenschilderwerk</a>."),
    ],
))

# ---------------------------------------------------------------------------
# 5. Slaapkamer
# ---------------------------------------------------------------------------
PAGINAS.append(dict(
    slug="slaapkamer", kort="Kleur slaapkamer kiezen",
    teaser="Rustgevende kleuren voor de slaapkamer en de kinderkamer.",
    titel="Kleur slaapkamer: rustgevende kleuren voor je muur",
    h1="Rustgevende kleuren voor je slaapkamer",
    description="Welke kleur kies je voor de slaapkamer? Rustgevend groen, blauw, warm grijs of een donkere "
                "muur achter het bed. Met voorbeelden en RAL-codes.",
    badge="Kleuradvies binnen",
    intro="Een slaapkamer is een plek om tot rust te komen. Veel mensen zoeken daarom een kleur die rustig "
          "voelt: ‘rustgevende kleuren slaapkamer’ wordt zo’n 590 keer per maand gezocht (Semrush, november 2026). "
          "Hier lees je welke kleuren daarvoor geschikt zijn en hoe je ze combineert.",
    secties=[
        ("Wat maakt een kleur rustig?", _p(
            "Rustige kleuren hebben weinig verzadiging: ze zijn een beetje grijs, gebroken of zacht. Denk aan "
            "grijsgroen, grijsblauw, zand en warm grijs. Felle, heldere kleuren zoals knalrood of fel geel geven "
            "juist energie. Die passen beter in een werkkamer of als klein accent.",
            "Er bestaat geen kleur die bij iedereen hetzelfde gevoel geeft. Wat jij rustig vindt, hangt ook af van "
            "je smaak. Kies dus een kleur waar je zelf graag naar kijkt.")),
        ("Kleuren die vaak gekozen worden", _ul(
            "<strong>Zacht groen.</strong> Saliegroen is al een paar jaar populair; er wordt per maand zo’n 6.600 "
            "keer op gezocht. Bleekgroen (RAL 6021) komt in de buurt. Groen past goed bij hout en linnen.",
            "<strong>Grijsblauw.</strong> Duifblauw (RAL 5014) is rustig en fris. Het past goed in een slaapkamer "
            "op het zuiden, waar het warme licht het blauw verzacht.",
            "<strong>Warm grijs en greige.</strong> Zijdegrijs (RAL 7044) of kiezelgrijs (RAL 7032). Neutraal, "
            "maar niet kil.",
            "<strong>Zand en ivoor.</strong> Licht ivoorkleurig (RAL 1015) of beige. Warm en licht, mooi in een "
            "kamer op het noorden.",
            "<strong>Diep blauw of groen achter het bed.</strong> Een donkere muur achter het hoofdeinde maakt de "
            "kamer knus, zonder dat de hele kamer donker wordt.")),
        ("De muur achter het bed", _p(
            "Een donkere of volle kleur op de muur achter het bed is een makkelijke manier om sfeer te maken. Je "
            "kijkt er niet naar als je in bed ligt, maar het geeft de kamer een middelpunt. Je kunt ook een "
            "‘halve muur’ schilderen: alleen de onderste meter, tot net boven het hoofdeinde. Dat is minder werk "
            "en ziet er speels uit.")),
        ("Kinderkamer", _p(
            "In een kinderkamer kun je met kleur spelen. Kies voor de grote muren een rustige basis en gebruik "
            "vrolijke kleuren in een accent: een halve muur, een vlak achter het bed of een kast. Zo hoef je niet "
            "de hele kamer over te schilderen als je kind groter wordt. Gebruik een goed afwasbare muurverf.")),
        ("Slaapkamer op het noorden of zuiden", _p(
            "Een slaapkamer ligt vaak aan de achterkant van het huis. Krijgt de kamer weinig zon (noorden), kies "
            "dan een warme tint: zand, ivoor, warm grijs of warm groen. Krijgt hij veel zon (zuiden of westen), dan "
            "kun je ook koele tinten gebruiken, zoals grijsblauw. Meer daarover lees je op "
            "<a href=\"/kleuradvies/lichtval/\">kleur en lichtval</a>.")),
        ("Matte verf en een donker plafond?", _p(
            "Matte muurverf geeft de rustigste uitstraling. Een plafond in een iets lichtere versie van de "
            "muurkleur maakt de kamer intiem. Een heel donker plafond maakt een lage kamer drukkend; doe dat "
            "alleen bij een hoog plafond.")),
    ],
    stalen_kop="Voorbeelden voor de slaapkamer",
    stalen_intro="Vijf slaapkamers. De linkermuur in de tekening staat voor de muur achter het bed.",
    stalen=[
        dict(naam="Saliegroen en linnen", soort="kamer", kleuren=[
            ("Muren", "RAL 1013", "muur"), ("Muur achter bed", "RAL 6021", "accent"),
            ("Houtwerk", "RAL 9010", "hout"), ("Vloer", "vloer-licht", "vloer")],
            uitleg="Bleekgroen achter het bed, parelwit op de andere muren. Zacht en natuurlijk."),
        dict(naam="Grijsblauw", soort="kamer", kleuren=[
            ("Muren", "RAL 9010", "muur"), ("Muur achter bed", "RAL 5014", "accent"),
            ("Houtwerk", "RAL 9010", "hout"), ("Vloer", "vloer-eiken", "vloer")],
            uitleg="Fris en rustig. Mooi in een slaapkamer met ochtend- of middagzon."),
        dict(naam="Warm grijs overal", soort="kamer", kleuren=[
            ("Muren", "RAL 7044", "muur"), ("Muur achter bed", "RAL 7032", "accent"),
            ("Houtwerk", "RAL 7044", "hout"), ("Vloer", "vloer-licht", "vloer")],
            uitleg="Twee tinten warm grijs. Rustig en neutraal, ook op het houtwerk."),
        dict(naam="Nachtblauw achter het bed", soort="kamer", kleuren=[
            ("Muren", "RAL 9001", "muur"), ("Muur achter bed", "RAL 5011", "accent"),
            ("Houtwerk", "RAL 9001", "hout"), ("Vloer", "vloer-eiken", "vloer")],
            uitleg="Een donkere muur maakt de kamer knus. De andere muren blijven licht."),
        dict(naam="Zand voor een noordkamer", soort="kamer", kleuren=[
            ("Muren", "RAL 1015", "muur"), ("Muur achter bed", "RAL 1001", "accent"),
            ("Houtwerk", "RAL 9010", "hout"), ("Vloer", "vloer-eiken", "vloer")],
            uitleg="Warme tinten compenseren koel noorderlicht."),
    ],
    links=LINKS_BINNEN + [("/kennisbank/plafond-schilderen-zonder-strepen/", "Plafond schilderen zonder strepen")],
    bronnen=[],
    cta_kop="Laat je slaapkamer schilderen",
    cta_tekst="Een slaapkamer is vaak in één dag klaar. Vraag offertes aan en noem de kleur die je gekozen hebt.",
    form_kop="Offerte voor je slaapkamer",
    faq=[
        ("Wat is de meest rustgevende kleur voor een slaapkamer?",
         "Zachte, wat grijze kleuren zoals grijsgroen, grijsblauw, zand en warm grijs worden vaak als rustig "
         "ervaren. Welke kleur jij het rustigst vindt, hangt ook af van je smaak."),
        ("Mag een slaapkamer een donkere kleur hebben?",
         "Ja. Een donkere muur achter het bed maakt de kamer knus. Houd de andere muren en het plafond lichter, "
         "zeker in een kleine kamer."),
        ("Welke kleur kies ik voor een slaapkamer op het noorden?",
         "Een warme tint: zand, ivoor, warm grijs of warm groen. Koel blauw of koel grijs kan daar kil aanvoelen."),
        ("Welke verf gebruik ik in de slaapkamer?",
         "Matte muurverf geeft de rustigste uitstraling. In een kinderkamer is een schrobvaste muurverf handig."),
        ("Is saliegroen nog populair?",
         "Ja, er wordt in Nederland nog altijd veel naar gezocht: zo’n 6.600 keer per maand (Semrush, november "
         "2026). Flexa koos een zacht groen, Soulful Sage, als kleur van het jaar 2027."),
    ],
))

# ---------------------------------------------------------------------------
# 6. Keuken, hal en trap
# ---------------------------------------------------------------------------
PAGINAS.append(dict(
    slug="keuken-en-hal", kort="Kleur keuken, hal en trap",
    teaser="Afwasbare kleuren voor de keuken, de gang en het trapgat.",
    titel="Kleur keuken, hal en gang kiezen: tips en voorbeelden",
    h1="Welke kleur voor je keuken, hal en trap?",
    description="Kleuradvies voor keuken, hal, gang en trapgat: welke kleuren werken, welke verf houdt het "
                "lang mooi en hoe maak je een smalle gang lichter?",
    badge="Kleuradvies binnen",
    intro="De keuken, de hal en het trapgat hebben het zwaar: er wordt gekookt, gelopen, gestoten en met "
          "jassen langs de muur geschuurd. De kleur moet dus mooi zijn én tegen een stootje kunnen. Hier lees je "
          "welke kleuren en welke verf daar het best werken.",
    snel='<a href="#keuken">Keuken</a> · <a href="#hal">Hal en gang</a> · <a href="#trap">Trap</a>',
    secties=[
        ("keuken", "Kleur in de keuken", _p(
            "In de keuken is de kleur van de kastjes en het werkblad de basis. Bij witte of lichte kastjes kun je "
            "de muren een kleur geven: zacht groen, warm grijs of een volle kleur op één muur. Bij donkere of "
            "houten kastjes zijn lichte, warme muren vaak rustiger.",
            "Wil je de kastjes zelf een andere kleur geven? Laat ze dan spuiten. Dat geeft een harde, gladde laag "
            "die beter tegen vet en water kan dan geschilderd. Lees wat dat kost op "
            "<a href=\"/kosten/keuken-spuiten/\">keuken spuiten</a>.")
         + _ul("Gebruik een goed afwasbare, schrobvaste muurverf. Rond het fornuis en de spoelbak liever een "
               "zijdeglans, of tegels of een glazen achterwand.",
               "Een kleur op de kastjes en een rustige kleur op de muur, of andersom. Niet allebei vol.",
               "Donkergroen en donkerblauw zijn populair voor keukenkastjes en staan mooi bij messing grepen.")),
        ("hal", "Hal en gang: lichter maken", _p(
            "Een hal is vaak smal en heeft weinig daglicht. Lichte, warme kleuren maken hem groter en "
            "vriendelijker. Er zijn een paar trucs:")
         + _ul("<strong>Lichte muren, donkere onderkant.</strong> Schilder de onderste meter in een donkerdere "
               "kleur of in zijdeglans. Daar zie je vlekken en schuifsporen minder.",
               "<strong>Kopse muur donkerder.</strong> Een donkerdere kleur op de muur aan het eind van een lange "
               "gang laat die muur dichterbij lijken. De gang voelt dan minder lang.",
               "<strong>Plafond licht.</strong> Een wit of heel licht plafond geeft hoogte.",
               "<strong>Deuren meenemen.</strong> Binnendeuren in een kleur geven de hal karakter. Zie "
               "<a href=\"/kennisbank/binnendeuren-verven/\">binnendeuren verven</a>.")),
        ("trap", "Het trapgat en de trap", _p(
            "Het trapgat is vaak de hoogste muur in huis en moeilijk te bereiken. Kies daarom een kleur waar je "
            "lang tevreden mee bent, en een verf die je kunt afnemen. Een schilder werkt hier met een steiger of "
            "trapsteiger.",
            "De trap zelf krijgt het zwaarst te verduren. Een donkere kleur op de treden laat minder vuil zien; "
            "een lichte kleur op de stootborden maakt de trap licht. Gebruik voor de treden een slijtvaste "
            "traplak. Meer lees je in <a href=\"/kennisbank/trap-verven/\">trap verven</a> en op "
            "<a href=\"/kosten/trap-schilderen/\">trap schilderen: kosten</a>.")),
        ("Badkamer en toilet", _p(
            "In een badkamer en toilet gebruik je verf die tegen vocht kan. Een kleine ruimte mag best een volle "
            "of donkere kleur hebben: het toilet is vaak de plek waar mensen het meest durven. Zorg voor goede "
            "ventilatie, anders krijg je last van schimmel. Lees meer in "
            "<a href=\"/kennisbank/schimmel-op-muur/\">schimmel op de muur</a>.")),
    ],
    stalen_kop="Voorbeelden voor keuken, hal en trap",
    stalen_intro="Vijf combinaties. Bij de hal staat de linkermuur in de tekening voor de onderkant of de kopse muur.",
    stalen=[
        dict(naam="Witte keuken, groene muur", soort="kamer", kleuren=[
            ("Muren", "RAL 9010", "muur"), ("Accentmuur", "RAL 6011", "accent"),
            ("Kastjes", "RAL 9016", "hout"), ("Vloer", "vloer-grijs", "vloer")],
            uitleg="Resedagroen geeft kleur zonder dat de keuken druk wordt."),
        dict(naam="Donkerblauwe kastjes", soort="kamer", kleuren=[
            ("Muren", "RAL 9001", "muur"), ("Accentmuur", "RAL 9001", "accent"),
            ("Kastjes", "RAL 5011", "hout"), ("Vloer", "vloer-eiken", "vloer")],
            uitleg="Gespoten kastjes in staalblauw met crèmewitte muren."),
        dict(naam="Lichte hal met donkere onderkant", soort="kamer", kleuren=[
            ("Muren", "RAL 1015", "muur"), ("Onderkant", "RAL 7039", "accent"),
            ("Deuren", "RAL 7039", "hout"), ("Vloer", "vloer-grijs", "vloer")],
            uitleg="Licht ivoor boven, kwartsgrijs onder en op de deuren. Praktisch en warm."),
        dict(naam="Lange gang, donkere kopmuur", soort="kamer", kleuren=[
            ("Muren", "RAL 9010", "muur"), ("Kopse muur", "RAL 6009", "accent"),
            ("Houtwerk", "RAL 9010", "hout"), ("Vloer", "vloer-eiken", "vloer")],
            uitleg="De groene muur aan het eind maakt de gang korter en gezelliger."),
        dict(naam="Trap: donkere treden", soort="balk", kleuren=[
            ("Treden", "RAL 7016", 2), ("Stootborden", "RAL 9010", 2), ("Muur trapgat", "RAL 7044", 3)],
            uitleg="Antraciet op de treden, wit op de stootborden en een warm grijs in het trapgat."),
    ],
    links=LINKS_BINNEN + [("/kosten/keuken-spuiten/", "Wat kost keuken spuiten?"),
                          ("/kosten/trap-schilderen/", "Wat kost een trap schilderen?"),
                          ("/schilderwerk/spuitwerk/", "Spuitwerk laten doen")],
    bronnen=[],
    cta_kop="Laat je keuken, hal of trap schilderen",
    cta_tekst="Vooral het trapgat is lastig zelf te doen. Een schilder heeft de juiste steiger en is snel klaar.",
    form_kop="Offerte voor je binnenschilderwerk",
    faq=[
        ("Welke kleur maakt een donkere hal lichter?",
         "Lichte, warme kleuren zoals gebroken wit, ivoor of zacht beige, met een wit plafond. Koel wit kan in "
         "een hal zonder daglicht grauw ogen."),
        ("Welke verf gebruik ik in de keuken?",
         "Een schrobvaste muurverf die je kunt afnemen. Rond het fornuis en de spoelbak liever een zijdeglans, of "
         "tegels of een glazen achterwand."),
        ("Kan ik mijn keukenkastjes een andere kleur geven?",
         "Ja, door ze te laten spuiten. Dat is vaak veel goedkoper dan een nieuwe keuken. Zie "
         "<a href=\"/kosten/keuken-spuiten/\">keuken spuiten</a>."),
        ("Hoe maak ik een lange gang korter?",
         "Geef de muur aan het eind een donkerdere kleur dan de zijmuren. Die muur lijkt dan dichterbij."),
        ("Welke kleur kies ik voor een trap?",
         "Een donkere kleur op de treden laat minder vuil zien, een lichte kleur op de stootborden houdt de trap "
         "licht. Gebruik een slijtvaste traplak."),
    ],
))

# ---------------------------------------------------------------------------
# 7. Lichtval
# ---------------------------------------------------------------------------
PAGINAS.append(dict(
    slug="lichtval", kort="Kleur en lichtval (noord, zuid, oost, west)",
    teaser="Waarom dezelfde kleur in elke kamer anders oogt, en wat je per windrichting kiest.",
    titel="Kleur kiezen per lichtval: noorden, zuiden, oosten, westen",
    h1="Kleur kiezen bij de lichtval in je kamer",
    description="Een kamer op het noorden vraagt om andere kleuren dan een kamer op het zuiden. Zo kies je een "
                "muurkleur per windrichting, met voorbeelden en RAL-codes.",
    badge="Kleuradvies binnen",
    intro="Dezelfde pot verf ziet er in elke kamer anders uit. Dat komt door het licht. Op deze pagina lees je "
          "hoe daglicht en lamplicht een kleur veranderen, en welke kleuren werken in een kamer op het noorden, "
          "oosten, zuiden of westen.",
    snel='<a href="#noorden">Noorden</a> · <a href="#zuiden">Zuiden</a> · <a href="#oosten">Oosten</a> · <a href="#westen">Westen</a>',
    secties=[
        ("Waarom licht een kleur verandert", _p(
            "Een kleur is wat er van het licht op je muur terugkaatst. Is het licht koel en blauwig, dan lijkt de "
            "muur koeler. Is het licht warm en geel, dan lijkt hij warmer. In Nederland, op het noordelijk "
            "halfrond, komt de zon nooit echt uit het noorden. Een kamer op het noorden krijgt dus vooral "
            "indirect licht van de hemel. Dat licht is koeler en gelijkmatiger. Een kamer op het zuiden krijgt "
            "de hele dag direct zonlicht.",
            "Ook lampen tellen mee. Warm wit lamplicht (rond 2700 kelvin) maakt kleuren ’s avonds geler. Koel "
            "lamplicht maakt ze blauwer. Test een kleur daarom ook ’s avonds.")),
        ("noorden", "Kamer op het noorden", _p(
            "Het licht is koel, gelijkmatig en zonder harde schaduwen. Koele kleuren zoals lichtgrijs en "
            "lichtblauw worden hier al snel grauw en kil. Kies liever kleuren met een warme ondertoon: crèmewit, "
            "ivoor, zand, warm grijs (greige), oker of warm groen.",
            "Wil je donker? Dat kan best. Een diep warm groen of terracotta maakt een noordkamer juist knus. Wat "
            "niet werkt, is een koel grijs dat net niet licht genoeg is.")),
        ("zuiden", "Kamer op het zuiden", _p(
            "Hier is veel licht, en het is warm en geel, vooral midden op de dag. Bijna elke kleur werkt. Warme "
            "kleuren worden hier nog warmer, soms te fel. Koele kleuren, zoals grijsblauw, zacht groen en "
            "koel grijs, komen hier juist mooi uit, omdat het warme licht ze verzacht.")),
        ("oosten", "Kamer op het oosten", _p(
            "’s Ochtends krijg je fris, helder licht; ’s middags en ’s avonds wordt het koeler en wat blauwer. "
            "Denk na over wanneer je de kamer gebruikt. Een slaapkamer of ontbijthoek op het oosten mag fris zijn. "
            "Gebruik je de kamer vooral ’s avonds, kies dan iets warmers.")),
        ("westen", "Kamer op het westen", _p(
            "’s Ochtends is het licht wat vlak en koel. In de late middag en avond komt warm, oranje licht binnen. "
            "Warme kleuren gloeien dan op; koele kleuren worden zachter. Een woonkamer op het westen is daarom "
            "een goede plek voor rustige middentinten die bij elk licht mooi blijven.")),
        ("Zo test je een kleur", _ul(
            "Koop een tester of laat een staal maken van minstens een A4. Kleine kaartjes uit de winkel zeggen "
            "weinig.",
            "Zet het staal op twee muren: één die licht vangt en één in de schaduw.",
            "Kijk op drie momenten: ’s ochtends, ’s middags en ’s avonds bij je eigen lampen.",
            "Zet het staal niet direct naast de oude kleur; die kleurt je blik. Gebruik een wit vel papier als "
            "rand eromheen.")
         + _tip("Een schilder kan een proefvlak zetten voordat hij de hele kamer doet. Vraag daar gerust om in "
                "je offerte.")),
        ("Buiten werkt het ook zo", _p(
            "Ook buiten maakt de lichtval verschil. Een kozijnkleur op een zonnige zuidgevel oogt lichter en "
            "warmer dan dezelfde kleur op een noordgevel. Bovendien verbleekt en veroudert verf op het zuiden "
            "sneller. Daar zit vaak de eerste schade. Lees meer op <a href=\"/kleuradvies/kozijnen/\">kleur "
            "kozijnen kiezen</a> en bekijk met de <a href=\"/onderhoudscheck/\">onderhoudscheck</a> wanneer je "
            "gevel aan de beurt is.")),
    ],
    stalen_kop="Kleuren per windrichting",
    stalen_intro="Per windrichting een kamer met een kleur die daar goed werkt.",
    stalen=[
        dict(naam="Noorden: warm en zacht", soort="kamer", kleuren=[
            ("Muren", "RAL 1015", "muur"), ("Accentmuur", "RAL 8023", "accent"),
            ("Houtwerk", "RAL 9001", "hout"), ("Vloer", "vloer-eiken", "vloer")],
            uitleg="Licht ivoor met een oranjebruin accent. Warm tegen het koele noorderlicht."),
        dict(naam="Noorden: diep en knus", soort="kamer", kleuren=[
            ("Muren", "RAL 6003", "muur"), ("Accentmuur", "RAL 6003", "accent"),
            ("Houtwerk", "RAL 1013", "hout"), ("Vloer", "vloer-eiken", "vloer")],
            uitleg="Olijfgroen rondom. Donker, maar met een warme ondertoon."),
        dict(naam="Zuiden: koel en fris", soort="kamer", kleuren=[
            ("Muren", "RAL 9002", "muur"), ("Accentmuur", "RAL 5024", "accent"),
            ("Houtwerk", "RAL 9016", "hout"), ("Vloer", "vloer-licht", "vloer")],
            uitleg="Grijswit en pastelblauw. Het warme zonlicht maakt het blauw zacht."),
        dict(naam="Oosten: fris in de ochtend", soort="kamer", kleuren=[
            ("Muren", "RAL 6019", "muur"), ("Accentmuur", "RAL 6021", "accent"),
            ("Houtwerk", "RAL 9010", "hout"), ("Vloer", "vloer-licht", "vloer")],
            uitleg="Licht groen voor een ontbijthoek of slaapkamer."),
        dict(naam="Westen: rustige middentint", soort="kamer", kleuren=[
            ("Muren", "RAL 7032", "muur"), ("Accentmuur", "RAL 7039", "accent"),
            ("Houtwerk", "RAL 9001", "hout"), ("Vloer", "vloer-eiken", "vloer")],
            uitleg="Kiezelgrijs en kwartsgrijs blijven mooi bij koel ochtendlicht én warm avondlicht."),
    ],
    links=LINKS_BINNEN + [("/onderhoudscheck/", "Doe de onderhoudscheck")],
    bronnen=[],
    cta_kop="Laat een proefvlak zetten en daarna schilderen",
    cta_tekst="Vraag in je offerte om een proefvlak. Dan weet je zeker dat de kleur in jouw licht goed uitpakt.",
    faq=[
        ("Welke kleur kies ik voor een kamer op het noorden?",
         "Een kleur met een warme ondertoon: crèmewit, ivoor, zand, warm grijs, oker of warm groen. Koel grijs en "
         "koel blauw worden daar snel kil."),
        ("Waarom ziet mijn kleur er anders uit dan op het kaartje?",
         "Door het licht. In de winkel hangt ander licht dan bij jou thuis, en een klein kaartje zegt weinig over "
         "een hele muur. Test met een groot staal op je eigen muur."),
        ("Welke kleuren passen in een kamer op het zuiden?",
         "Bijna alles. Koele kleuren zoals grijsblauw en zacht groen komen er mooi uit, omdat het warme zonlicht "
         "ze verzacht."),
        ("Maakt lamplicht ook verschil?",
         "Ja. Warm wit lamplicht maakt kleuren geler, koel lamplicht blauwer. Kijk daarom ook ’s avonds naar je "
         "staal."),
        ("Lijkt een kleur op de muur donkerder dan op het staal?",
         "Vaak wel. Op een grote muur, en in een hoek waar weinig licht komt, oogt een kleur meestal donkerder. "
         "Twijfel je, kies dan een tint lichter."),
    ],
))

# ---------------------------------------------------------------------------
# 8. Kleurcombinaties
# ---------------------------------------------------------------------------
PAGINAS.append(dict(
    slug="kleurcombinaties", kort="Kleurcombinaties en de 60-30-10-regel",
    teaser="Welke kleuren passen bij elkaar? Uitleg, vuistregels en kant-en-klare paletten.",
    titel="Kleurcombinaties: welke kleuren passen bij elkaar?",
    h1="Welke kleuren passen bij elkaar?",
    description="Zo combineer je kleuren in huis: de 60-30-10-regel, warme en koele tinten, ton-sur-ton en "
                "contrast. Met tien paletten met RAL-codes als CSS-staal.",
    badge="Kleuradvies",
    intro="Een mooie kleur is één ding; een kleur die past bij de rest is iets anders. Hier lees je een paar "
          "eenvoudige vuistregels om kleuren te combineren, binnen en buiten. Onderaan staan tien paletten om "
          "mee te beginnen.",
    snel='<a href="#regel">De 60-30-10-regel</a> · <a href="#manieren">Vier manieren</a> · <a href="#combinaties">Tien paletten</a>',
    secties=[
        ("regel", "De 60-30-10-regel", _p(
            "Een bekende vuistregel van interieurontwerpers: verdeel een ruimte in drie kleuren. Ongeveer "
            "<strong>60 procent</strong> is de hoofdkleur (de meeste muren), <strong>30 procent</strong> een "
            "tweede kleur (een accentmuur, gordijnen, een grote kast of de bank) en <strong>10 procent</strong> "
            "een accent (kussens, een lamp, een deur).",
            "Het is geen wet, maar het helpt. Zo krijg je genoeg rust én genoeg spanning. De kleurbalken in de "
            "voorbeelden hieronder laten die verhouding zien.")),
        ("Warm en koel", _p(
            "Elke kleur heeft een ondertoon. Warme kleuren hebben iets geel, rood of bruin in zich: crème, zand, "
            "terracotta, olijfgroen. Koele kleuren hebben iets blauw of grijs: lichtgrijs, grijsblauw, "
            "koel wit. Kleuren met dezelfde ondertoon passen meestal makkelijk bij elkaar.",
            "Twijfel je over een ondertoon? Leg het staal naast een vel wit printpapier. Een warme kleur lijkt "
            "dan geler of roder, een koele blauwer of groener.")),
        ("manieren", "Vier manieren om te combineren", _ul(
            "<strong>Ton-sur-ton.</strong> Twee of drie tinten van dezelfde kleur, van licht naar donker. Rustig "
            "en altijd goed. Bijvoorbeeld zijdegrijs, kiezelgrijs en kwartsgrijs.",
            "<strong>Buurkleuren.</strong> Kleuren die in de kleurencirkel naast elkaar liggen, zoals groen en "
            "blauw, of geel en oranje. Harmonieus en natuurlijk.",
            "<strong>Contrast.</strong> Kleuren die tegenover elkaar liggen, zoals blauw en oranje, of groen en "
            "rood. Levendig, maar gebruik er één als klein accent.",
            "<strong>Neutraal met één kleur.</strong> Wit, grijs of zand als basis met één duidelijke kleur. De "
            "makkelijkste manier om kleur te durven.")),
        ("Buiten: steen, kozijn en deur", _p(
            "Buiten is de steen je hoofdkleur, de kozijnen en boeidelen de tweede kleur en de voordeur het accent. "
            "Ook daar werkt 60-30-10 dus. Meer daarover lees je op <a href=\"/kleuradvies/kozijnen/\">kleur "
            "kozijnen kiezen</a> en <a href=\"/kleuradvies/voordeur/\">kleur voordeur kiezen</a>. Of probeer het "
            "zelf op een getekende woning in de <a href=\"/kleuren-kiezen/\">kleurenkiezer</a>.")),
        ("Veelgemaakte fouten", _ul(
            "Te veel kleuren tegelijk. Drie is meestal genoeg, plus wit.",
            "Alleen naar de muur kijken. Vloer, meubels en gordijnen doen mee.",
            "Kiezen van een klein kaartje. Op een grote muur oogt een kleur voller en vaak donkerder.",
            "Koel en warm door elkaar zonder dat het bewust is, bijvoorbeeld koel grijs naast een warme eiken vloer.")),
    ],
    stalen_kop="Tien paletten om mee te beginnen",
    stalen_intro="Elke balk laat de verhouding zien: hoofdkleur, tweede kleur en accent.",
    stalen=[
        dict(naam="Zacht natuurlijk", soort="balk", kleuren=[
            ("Hoofdkleur", "RAL 1013", 60), ("Tweede kleur", "RAL 6021", 30), ("Accent", "RAL 8023", 10)],
            uitleg="Parelwit, bleekgroen en een roestbruin accent."),
        dict(naam="Ton-sur-ton grijs", soort="balk", kleuren=[
            ("Hoofdkleur", "RAL 7044", 60), ("Tweede kleur", "RAL 7032", 30), ("Accent", "RAL 7039", 10)],
            uitleg="Drie warme grijzen van licht naar donker. Rustig en tijdloos."),
        dict(naam="Kust", soort="balk", kleuren=[
            ("Hoofdkleur", "RAL 9010", 60), ("Tweede kleur", "RAL 5014", 30), ("Accent", "RAL 1002", 10)],
            uitleg="Wit, duifblauw en zandgeel. Fris en licht."),
        dict(naam="Warm aards", soort="balk", kleuren=[
            ("Hoofdkleur", "RAL 1015", 60), ("Tweede kleur", "RAL 3012", 30), ("Accent", "RAL 6003", 10)],
            uitleg="Ivoor, terracotta en olijfgroen. Gezellig bij hout."),
        dict(naam="Diep en deftig", soort="balk", kleuren=[
            ("Hoofdkleur", "RAL 9001", 60), ("Tweede kleur", "RAL 5011", 30), ("Accent", "RAL 1006", 10)],
            uitleg="Crèmewit, nachtblauw en een gouden accent."),
        dict(naam="Bosgroen", soort="balk", kleuren=[
            ("Hoofdkleur", "RAL 9002", 60), ("Tweede kleur", "RAL 6009", 30), ("Accent", "RAL 3009", 10)],
            uitleg="Grijswit, dennengroen en bruinrood. Klassiek, binnen en buiten."),
        dict(naam="Modern contrast", soort="balk", kleuren=[
            ("Hoofdkleur", "RAL 9016", 60), ("Tweede kleur", "RAL 7021", 30), ("Accent", "RAL 8023", 10)],
            uitleg="Helder wit, zwartgrijs en een warm oranjebruin."),
        dict(naam="Indigo", soort="balk", kleuren=[
            ("Hoofdkleur", "RAL 7035", 60), ("Tweede kleur", "RAL 5008", 30), ("Accent", "RAL 1015", 10)],
            uitleg="Lichtgrijs, grijsblauw en ivoor. Koel en rustig."),
        dict(naam="Zonnig", soort="balk", kleuren=[
            ("Hoofdkleur", "RAL 1013", 60), ("Tweede kleur", "RAL 1002", 30), ("Accent", "RAL 5011", 10)],
            uitleg="Parelwit en zandgeel met een donkerblauw accent: een contrast van warm en koel."),
        dict(naam="Gevel klassiek", soort="balk", kleuren=[
            ("Steen", "steen-rood", 60), ("Kozijnen", "RAL 9001", 30), ("Voordeur", "RAL 6012", 10)],
            uitleg="Ook buiten werkt 60-30-10: steen, kozijnen en een donkergroene deur."),
    ],
    links=LINKS_BINNEN[:3] + [(K, "Probeer combinaties in de kleurenkiezer"),
                              ("/schilderwerk/buitenschilderwerk/", "Buitenschilderwerk laten doen"),
                              ("/inspiratie/", "Kleurcombinaties per woningtype")],
    bronnen=[],
    cta_kop="Een kleurcombinatie gekozen?",
    cta_tekst="Zet de RAL-codes in je aanvraag. Dan kan de schilder meteen rekenen met de juiste verf.",
    faq=[
        ("Wat is de 60-30-10-regel?",
         "Een vuistregel om kleuren te verdelen: 60 procent hoofdkleur, 30 procent tweede kleur en 10 procent "
         "accent. Zo krijg je rust en spanning tegelijk."),
        ("Welke kleuren passen altijd bij elkaar?",
         "Tinten van dezelfde kleur (ton-sur-ton) en een neutrale basis met één kleur gaan bijna altijd goed. "
         "Let erop dat de ondertoon (warm of koel) overeenkomt."),
        ("Hoeveel kleuren mag ik in één kamer gebruiken?",
         "Meestal zijn drie kleuren plus wit genoeg. Meer kan, maar wordt snel onrustig."),
        ("Hoe weet ik of een kleur warm of koel is?",
         "Leg het staal naast wit printpapier. Een warme kleur lijkt dan geler of roder, een koele blauwer of "
         "groener."),
        ("Werkt de 60-30-10-regel ook buiten?",
         "Ja. De steen is de hoofdkleur, de kozijnen en boeidelen zijn de tweede kleur en de voordeur is het accent."),
    ],
))

# ---------------------------------------------------------------------------
# 9. Kleurtrends
# ---------------------------------------------------------------------------
PAGINAS.append(dict(
    slug="kleurtrends", kort="Kleurtrends 2026 en 2027",
    teaser="Kleur van het jaar, saliegroen, greige en terracotta: wat is het en past het bij jou?",
    titel="Kleurtrends 2026 en 2027: kleur van het jaar uitgelegd",
    h1="Kleurtrends 2026 en 2027: wat is er populair en past het bij jou?",
    description="Kleur van het jaar 2026 en 2027, en waar Nederland echt naar zoekt: saliegroen, greige, "
                "terracotta en antraciet. Met uitleg, voorbeelden en RAL-codes.",
    badge="Kleuradvies",
    intro="Elk jaar kiezen verfmerken en kleurinstituten een ‘kleur van het jaar’. Daarnaast laten de "
          "zoekcijfers zien welke kleuren mensen in Nederland echt willen. Op deze pagina zetten we het op een "
          "rij, met uitleg hoe je een trendkleur gebruikt zonder dat je huis over een paar jaar gedateerd oogt.",
    snel='<a href="#jaar">Kleur van het jaar</a> · <a href="#zoeken">Waar Nederland naar zoekt</a> · <a href="#tijdloos">Trend of tijdloos</a>',
    secties=[
        ("jaar", "Kleur van het jaar 2026 en 2027", _p(
            "<strong>Flexa, 2027: Soulful Sage.</strong> Flexa koos voor 2027 een zacht groen, Soulful Sage. "
            "Volgens het nieuwsbericht komt de keuze voort uit het jaarlijkse kleurentrendonderzoek van het merk. "
            "Ook zustermerk Levis heeft deze kleur als kleur van het jaar.",
            "<strong>Flexa, 2026: The Rhythm of Blues.</strong> Voor 2026 koos Flexa niet één kleur, maar een "
            "familie van drie blauwe tinten, richting indigo.",
            "<strong>Pantone, 2026: Cloud Dancer.</strong> Het Amerikaanse kleurinstituut Pantone koos voor 2026 "
            "PANTONE 11-4201 Cloud Dancer: een zacht wit. Het is de eerste keer dat Pantone een wit kiest. Pantone "
            "kiest kleuren voor mode en design in het algemeen, niet speciaal voor verf. De keuze voor 2027 maakt "
            "Pantone meestal begin december bekend.",
            "Let op: de exacte kleuren van een merk heb je alleen bij dat merk. Wil je ze bij een ander merk laten "
            "mengen, dan heb je een benadering. Wij noemen hieronder RAL-kleuren die in de buurt komen.")),
        ("zoeken", "Waar Nederland echt naar zoekt", _p(
            "Een kleur van het jaar zegt iets over wat merken verwachten. Zoekcijfers zeggen iets over wat mensen "
            "willen. Volgens Semrush (november 2026, gemiddeld per maand in Nederland):")
         + _ul("<strong>Saliegroen</strong>: zo’n 6.600 zoekopdrachten, en 590 op ‘saliegroen muurverf’. Een zacht "
               "grijsgroen; bleekgroen (RAL 6021) komt in de buurt.",
               "<strong>Greige</strong>: 2.400 zoekopdrachten, en 880 op ‘greige muurverf’. Grijs met beige, warm "
               "en neutraal; denk aan zijdegrijs (RAL 7044).",
               "<strong>Terracotta muurverf</strong>: 1.300 zoekopdrachten. Gebakken-aarde-oranje; beigerood "
               "(RAL 3012) komt in de buurt.",
               "<strong>Grachtengroen en monumentengroen</strong>: elk 1.300. Vooral voor kozijnen. Zie "
               "<a href=\"/kleuradvies/grachtengroen/\">grachtengroen</a>.",
               "<strong>Antraciet kozijnen</strong> (590) en <strong>zwarte kozijnen</strong> (480): donker "
               "buiten blijft gewild. Zie <a href=\"/kleuradvies/kozijnen/\">kleur kozijnen</a>.")
         + _p("Wat opvalt: binnen gaat het vooral om zachte, warme en aardse kleuren. Buiten blijven donkere "
              "kleuren populair.")),
        ("Waarom zijn deze kleuren populair?", _p(
            "Zachte groenen en aardetinten passen bij hout, linnen en planten, en voelen rustig. Greige is een "
            "warme opvolger van het koele grijs dat lange tijd overal zat. Het past bij bijna elke vloer. "
            "Terracotta brengt warmte in een kamer zonder dat het schreeuwerig wordt. Of deze kleuren over vijf "
            "jaar nog net zo populair zijn, weet niemand.")),
        ("tijdloos", "Trend of tijdloos: zo gebruik je een trendkleur", _ul(
            "<strong>Begin klein.</strong> Zet een trendkleur op één muur, een kast of de binnendeuren. Wil je "
            "over een paar jaar iets anders, dan is dat een kleine klus.",
            "<strong>Houd de grote vlakken rustig.</strong> Plafonds, de meeste muren en buiten de kozijnen in "
            "een kleur waar je lang tevreden mee bent.",
            "<strong>Kijk naar je huis, niet naar de trend.</strong> Een warme trendkleur in een kamer op het "
            "noorden werkt; een koele trendkleur daar misschien niet. Zie "
            "<a href=\"/kleuradvies/lichtval/\">kleur en lichtval</a>.",
            "<strong>Buiten voorzichtiger.</strong> Buitenschilderwerk gaat vaak vijf jaar of langer mee. Kies "
            "buiten een kleur die bij de steen en de straat past, en gebruik een trend hooguit op de voordeur.")),
    ],
    stalen_kop="Trendkleuren in een kamer",
    stalen_intro="Vijf voorbeelden met RAL-kleuren die in de buurt komen van de trends. Het zijn benaderingen, geen merkkleuren.",
    stalen=[
        dict(naam="Zacht groen (richting Soulful Sage)", soort="kamer", kleuren=[
            ("Muren", "RAL 6021", "muur"), ("Accentmuur", "RAL 6011", "accent"),
            ("Houtwerk", "RAL 9010", "hout"), ("Vloer", "vloer-licht", "vloer")],
            uitleg="Bleekgroen en resedagroen. Rustig en natuurlijk."),
        dict(naam="Indigo (richting Rhythm of Blues)", soort="kamer", kleuren=[
            ("Muren", "RAL 9002", "muur"), ("Accentmuur", "RAL 5008", "accent"),
            ("Houtwerk", "RAL 5008", "hout"), ("Vloer", "vloer-eiken", "vloer")],
            uitleg="Grijsblauw op één muur en het houtwerk, met grijswit."),
        dict(naam="Zacht wit (richting Cloud Dancer)", soort="kamer", kleuren=[
            ("Muren", "RAL 9010", "muur"), ("Accentmuur", "RAL 1013", "accent"),
            ("Houtwerk", "RAL 9010", "hout"), ("Vloer", "vloer-eiken", "vloer")],
            uitleg="Zuiver wit met parelwit. Licht en rustig, nooit gedateerd."),
        dict(naam="Greige", soort="kamer", kleuren=[
            ("Muren", "RAL 7044", "muur"), ("Accentmuur", "RAL 7032", "accent"),
            ("Houtwerk", "RAL 9001", "hout"), ("Vloer", "vloer-eiken", "vloer")],
            uitleg="Zijdegrijs en kiezelgrijs. De warme opvolger van koel grijs."),
        dict(naam="Terracotta", soort="kamer", kleuren=[
            ("Muren", "RAL 1015", "muur"), ("Accentmuur", "RAL 3012", "accent"),
            ("Houtwerk", "RAL 1015", "hout"), ("Vloer", "vloer-licht", "vloer")],
            uitleg="Beigerood op één muur. Warm en zonnig."),
    ],
    links=LINKS_BINNEN + [(K, "Probeer kleuren in de kleurenkiezer")],
    bronnen=["flexa-2027", "flexa-2026", "pantone-2026"],
    cta_kop="Een trendkleur op je muur?",
    cta_tekst="Laat een schilder je nieuwe kleur strak zetten. Een accentmuur of een paar binnendeuren is vaak in één dag klaar.",
    form_kop="Offerte voor je nieuwe kleur",
    faq=[
        ("Wat is de kleur van het jaar 2027?",
         "Flexa koos voor 2027 Soulful Sage, een zacht groen. Pantone maakt zijn keuze voor 2027 meestal begin "
         "december bekend."),
        ("Wat was de kleur van het jaar 2026?",
         "Bij Flexa was dat The Rhythm of Blues, een familie van drie blauwe tinten. Pantone koos Cloud Dancer, "
         "een zacht wit."),
        ("Is saliegroen nog in de mode?",
         "Er wordt in Nederland nog altijd veel naar gezocht: zo’n 6.600 keer per maand (Semrush, november 2026). "
         "En Flexa koos een zacht groen als kleur van het jaar 2027."),
        ("Wat is greige?",
         "Een mengsel van grijs en beige: een warm, neutraal grijs. Zijdegrijs (RAL 7044) komt in de buurt."),
        ("Hoe voorkom ik dat mijn huis gedateerd oogt?",
         "Gebruik trendkleuren op kleine vlakken, zoals een accentmuur of deuren, en houd de grote vlakken rustig. "
         "Dan is overschilderen later een kleine klus."),
    ],
))

# ---------------------------------------------------------------------------
# Overzichtspagina /kleuradvies/
# ---------------------------------------------------------------------------
HUB = dict(
    titel="Kleuradvies voor binnen en buiten",
    h1="Kleuradvies voor je huis, binnen en buiten",
    description="Kleuradvies voor kozijnen, voordeur, woonkamer, slaapkamer, keuken en hal. Plus uitleg over "
                "lichtval, kleurcombinaties en de kleurtrends van 2026 en 2027.",
    intro="Een andere kleur kan je huis helemaal veranderen. Hier vind je advies per onderdeel en per ruimte, "
          "met kleurcombinaties als staal, RAL-codes en uitleg waarom iets werkt. Liever per woningtype kijken? "
          "Ga naar <a href=\"/inspiratie/\">inspiratie per woningtype</a>.",
    groepen=[
        ("Buiten", ["kozijnen", "grachtengroen", "voordeur"]),
        ("Binnen", ["woonkamer", "slaapkamer", "keuken-en-hal"]),
        ("Kleur begrijpen", ["lichtval", "kleurcombinaties", "kleurtrends"]),
    ],
    tekst=("<h2>Hoe gebruik je dit advies?</h2>"
           "<p>Begin bij wat blijft: de steen en het dak buiten, de vloer en de grote meubels binnen. Kies daar een "
           "rustige hoofdkleur bij en hooguit één accent. Kijk naar de lichtval, want dezelfde kleur oogt in een "
           "kamer op het noorden anders dan op het zuiden. En test altijd met een groot staal op je eigen muur of "
           "kozijn.</p>"
           "<p>Bij elk advies staan RAL-codes. RAL is een kleurnorm die schilders en verfwinkels kennen; met de "
           "code kan elke verfwinkel de kleur mengen. De kleuren op je scherm zijn een benadering.</p>"
           "<h2>Kleuradvies per bouwstijl</h2>"
           "<p>Elk woningtype vraagt om eigen kleuren. In onze gidsen lees je per bouwstijl wat er geschilderd "
           "wordt, waar je op let en welke kleuren passen, met foto’s en RAL-codes:</p>"
           "<ul><li><a href=\"/inspiratie/jaren30/\">Jaren-30-woning</a></li>"
           "<li><a href=\"/inspiratie/jaren70/\">Jaren-70-woning</a></li>"
           "<li><a href=\"/inspiratie/villa/\">Villa en landhuis</a></li>"
           "<li><a href=\"/inspiratie/polder/\">Boerderij en polderwoning</a></li>"
           "<li><a href=\"/inspiratie/monument/\">Monument</a></li>"
           "<li><a href=\"/inspiratie/nieuwbouw/\">Nieuwbouw</a></li></ul>"
           "<h2>Meer hulp bij kiezen</h2>"
           "<ul><li><a href=\"/kleuren-kiezen/\">Kleurenkiezer</a>: probeer kleuren op een getekende woning.</li>"
           "<li><a href=\"/inspiratie/\">Inspiratie per woningtype</a>: van jaren-30-woning tot nieuwbouw, met foto’s.</li>"
           "<li><a href=\"/verfcalculator/\">Verfcalculator</a>: hoeveel liter verf heb je nodig?</li>"
           "<li><a href=\"/kosten/calculator/\">Kostencalculator</a>: wat kost het schilderen van je huis?</li></ul>"),
    faq=[
        ("Hoe kies ik een kleur voor mijn huis?",
         "Begin bij wat blijft (steen, dak, vloer, meubels), kies één rustige hoofdkleur en hooguit één accent, en "
         "test met een groot staal in je eigen licht."),
        ("Wat is een RAL-code?",
         "Een code uit de RAL-kleurnorm, bijvoorbeeld RAL 9010 voor zuiver wit. Met de code kan elke verfwinkel de "
         "kleur mengen, bij elk merk."),
        ("Kan een schilder mij helpen met kleur kiezen?",
         "Veel schilders denken mee en zetten op verzoek een proefvlak. Vraag daar gerust om als je een offerte "
         "aanvraagt."),
        ("Kloppen de kleuren op mijn scherm?",
         "Niet precies. Elk scherm toont kleuren anders. Gebruik de RAL-code en kijk naar een echt staal."),
    ],
)
