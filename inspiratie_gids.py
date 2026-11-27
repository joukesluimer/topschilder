# -*- coding: utf-8 -*-
"""
Inhoud voor /inspiratie/ en de gidsen per woningtype (/inspiratie/{type}/).

- KLEURCODES: per kleur uit de stijlen de RAL Classic-code die wij aanhouden, met de
  officiële Nederlandse RAL-naam en een hexwaarde als benadering voor het scherm.
  Codes en namen: officiële RAL-lijst (ral-farben.de). Hex: Wikipedia ‘Lijst van
  RAL-kleuren’. Gecontroleerd op 22-11-2026. Welke RAL-code bij een stijl hoort, is
  onze eigen keuze; traditionele namen als monumentengroen of grachtengroen hebben
  geen vaste code (elk verfmerk maakt een eigen versie).
- BRONNEN: elke historische bewering op de pagina's verwijst naar een van deze bronnen.
- GIDSEN: de tekst per woningtype. Geen verzonnen feiten: bouwjaren en architecten
  komen van de bestandspagina's van de foto's op Wikimedia Commons.
"""

# id uit kleuren_kiezer.VERFKLEUREN -> (RAL-naam of omschrijving, RAL-code of None, hex, noot)
KLEURCODES = {
    "cremewit": ("Crèmewit", "RAL 9001", "#EFEBDC", ""),
    "gebroken-wit": ("Zuiver wit", "RAL 9010", "#F7F9EF", "Een zacht, iets warm wit."),
    "wit": ("Verkeerswit", "RAL 9016", "#F1F0EA", "Helder wit. De hexwaarde verschilt per bron."),
    "lichtgrijs": ("Lichtgrijs", "RAL 7035", "#CBD0CC", ""),
    "antraciet": ("Antracietgrijs", "RAL 7016", "#373F43", ""),
    "zwart": ("Gitzwart", "RAL 9005", "#0A0A0D", ""),
    "gooiers-groen": ("Dennengroen", "RAL 6009", "#26392F",
                      "In de kleurenkiezer heet deze tint ‘Gooiers groen’. Dat is een omschrijving, geen vaste kleur."),
    "monumentengroen": ("Zwartgroen", "RAL 6012", "#31403D",
                        "Een benadering van wat vaak monumentengroen heet. Elk verfmerk heeft daar een eigen versie van."),
    "olijfgroen": ("Olijfgroen", "RAL 6003", "#4B573E", ""),
    "salie": ("Bleekgroen", "RAL 6021", "#86A47C", "Een zacht grijsgroen."),
    "staalblauw": ("Duifblauw", "RAL 5014", "#6C7C98", "Een rustig grijsblauw."),
    "nachtblauw": ("Staalblauw", "RAL 5011", "#232C3F", "Een heel donker blauw."),
    "ossenbloed": ("Wijnrood", "RAL 3005", "#5E2028",
                   "Ligt dicht bij wat vaak ossenbloedrood heet; ook daarvan heeft elk merk een eigen versie."),
    "bentheimer": ("Zandgeel", "RAL 1002", "#D2AA6D",
                   "Ligt dicht bij wat verfmerken Bentheimer geel noemen. Die naam heeft geen vaste code."),
    "eiken": ("Lichte eikenkleur", None, "#b88a53",
              "Transparante beits of lak in houtkleur. Daar bestaat geen RAL-code voor; kies bij de schilder uit een staal."),
    "noten": ("Notenkleur", None, "#7b5131",
              "Transparante beits in een middelbruine houtkleur. Ook hier kies je uit een staal van het verfmerk."),
}


def kleur_label(kleur_id):
    """‘Crèmewit (RAL 9001)’ of, zonder code, alleen de omschrijving."""
    naam, ral, _hex, _noot = KLEURCODES[kleur_id]
    return f"{naam} ({ral})" if ral else naam


BRONNEN = {
    "olm-kozijn": ("Nederlands Openluchtmuseum, ‘Wat vertelt de kleur van een kozijn?’",
                   "https://www.openluchtmuseum.nl/nl/verdiep/wat-vertelt-de-kleur-van-een-kozijn"),
    "olm-gebouwen": ("Nederlands Openluchtmuseum, ‘De kleuren van historische gebouwen’",
                     "https://www.openluchtmuseum.nl/nl/verdiep/de-kleuren-van-historische-gebouwen"),
    "rijksoverheid": ("Rijksoverheid, ‘Heb ik een vergunning nodig voor verbouwing of restauratie van een monument?’",
                      "https://www.rijksoverheid.nl/onderwerpen/erfgoed/vraag-en-antwoord/heb-ik-een-vergunning-nodig-voor-verbouwing-of-restauratie-van-een-monument"),
    "kampen": ("Gemeente Kampen, welstandsbeleid (Lokale regelgeving, overheid.nl)",
               "https://lokaleregelgeving.overheid.nl/CVDR661794/2"),
    "consumentenbond": ("Consumentenbond, ‘Zelf kozijnen schilderen’",
                        "https://www.consumentenbond.nl/verbouwen-en-klussen/zelf-kozijnen-schilderen"),
    "rce-nop": ("Rijksdienst voor het Cultureel Erfgoed, ‘Noordoostpolder, een wederopbouwgebied van nationaal belang’ (2015)",
                "https://www.cultureelerfgoed.nl/binaries/cultureelerfgoed/documenten/publicaties/2015/01/01/noordoostpolder-een-wederopbouwgebied-van-nationaal-belang-nr-24/rijksdienst_voor_het_cultureel_erfgoed_2015_24_noordoostpolder.pdf"),
    "ral": ("RAL gGmbH, overzicht van alle RAL Classic-kleuren", "https://www.ral-farben.de/en/all-ral-colours"),
    "ral-hex": ("Wikipedia, ‘Lijst van RAL-kleuren’ (hexwaarden als benadering)",
                "https://nl.wikipedia.org/wiki/Lijst_van_RAL-kleuren"),
}


def bron(sleutel, tekst=None):
    """Link naar een bron, voor in de lopende tekst."""
    naam, url = BRONNEN[sleutel]
    return f'<a href="{url}" rel="nofollow noopener" target="_blank">{tekst or naam}</a>'


# Onderhoud geldt voor alle types; per type komt er een eigen alinea bij.
ONDERHOUD_ALGEMEEN = (
    "Volgens de " + bron("consumentenbond", "Consumentenbond") + " zit er gemiddeld vijf jaar tussen twee "
    "schilderbeurten. Hoe lang het bij jou is, hangt af van de verf, de kwaliteit van het werk en hoeveel zon en "
    "vocht het hout vangt. Loop daarom elk voorjaar een rondje om het huis en kijk naar scheurtjes, bladders en "
    "zachte plekken, vooral onderaan kozijnen en aan de uiteinden van boeidelen.")

GIDSEN = {
    "jaren30": {
        "titel": "Kleuren voor een jaren-30-woning",
        "h1": "Kleuren voor je jaren-30-woning",
        "description": "Welke kleuren passen bij een jaren-30-woning? Kozijnen, erker, glas-in-lood en voordeur: "
                       "wat je schildert, waar je op let, onderhoud en RAL-codes.",
        "intro": "Een jaren-30-woning herken je aan de erker, de diepe overstekken, kleine ruitjes en vaak "
                 "glas-in-lood boven de ramen. Er zit veel houtwerk aan, en juist dat bepaalt hoe de woning "
                 "eruitziet. Met de juiste kleuren blijft dat rijke karakter zichtbaar.",
        "kenmerken": [
            "Met ‘jaren 30’ bedoelen de meeste mensen de woningen uit de periode tussen de twee wereldoorlogen. "
            "Op de foto’s zie je er twee uit Hilversum: een dubbel woonhuis uit 1927 aan de Van der Helstlaan en "
            "een uit 1928 aan de Zonnelaan. Typisch zijn de baksteen, het hoge dak met pannen en de vele "
            "geschilderde onderdelen: kozijnen, ramen, de erker, de dakgoot, de boeidelen en vaak een houten "
            "luifel boven de voordeur.",
            "Omdat er zoveel houtwerk is, heeft de kleur veel effect. Lichte kozijnen met donkere ramen laten "
            "de verdeling in kleine ruitjes goed zien. Alles in één lichte tint maakt de gevel juist rustiger, "
            "zodat het metselwerk en de erker de aandacht krijgen.",
        ],
        "onderdelen": [
            ("Kozijnen en ramen", "Het vaste kozijn en de draaiende ramen krijgen vaak elk een eigen kleur. "
                                  "Dat is meer werk, want de schilder moet strak langs de naad werken."),
            ("Erker", "Veel losse delen, hoeken en een dakje. Reken hier op extra uren en controleer de "
                      "aansluiting met het lood of zink."),
            ("Glas-in-lood en roedes", "Het lood zelf wordt niet geschilderd. De roedes en de stopverf wel; "
                                       "dat is precisiewerk."),
            ("Boeidelen, goot en overstek", "Die zitten hoog en vangen veel weer. Vaak is hier een steiger of "
                                            "hoogwerker nodig."),
            ("Voordeur en luifel", "Een vaste plek voor een accentkleur."),
        ],
        "letop": [
            "Laat glas-in-lood goed afplakken. Verf op het lood of het glas krijg je er lastig weer af.",
            "Kijk of de stopverf nog goed zit. Bij oude ramen is die vaak uitgedroogd en gescheurd. Vervangen "
            "hoort dan bij het voorwerk.",
            "Onderdorpels en de onderkant van de erker staan het meest bloot aan regen. Vraag de schilder om "
            "daar te prikken op houtrot.",
            "Woon je in een dubbel woonhuis? Het oogt het mooist als beide helften dezelfde kleuren hebben. "
            "Overleg met je buren.",
        ],
        "onderhoud": "Door de vele kleine ruitjes en profielen kost een schilderbeurt hier meer uren dan bij een "
                     "strakke gevel. Bijhouden loont: wie op tijd schildert, hoeft minder hout te repareren.",
        "kleuren": [
            "Groen met wit of crème is in Nederland al heel lang gewoon. Het "
            + bron("olm-kozijn", "Nederlands Openluchtmuseum") + " schrijft dat groene kozijnen eerst een teken "
            "van welstand waren, omdat die verf duur was. Toen in de negentiende eeuw het goedkopere standgroen "
            "op de markt kwam, kozen veel mensen alsnog voor groen. Een donkergroen of donkerrood raam met "
            "crème kozijnen past daarom goed bij de warme baksteen van een jaren-30-woning.",
        ],
        "kosten": [("/kosten/kozijnen-schilderen/", "Wat kost kozijnen schilderen?"),
                   ("/kosten/huis-schilderen/", "Wat kost je huis buiten laten schilderen?")],
        "plaatsen": ["hilversum", "amersfoort", "bussum"],
        "bronnen": ["olm-kozijn", "consumentenbond"],
    },
    "jaren70": {
        "titel": "Kleuren voor een jaren-70-rijtjeshuis",
        "h1": "Kleuren voor je jaren-70-rijtjeshuis",
        "description": "Een jaren-70-rijtjeshuis opfrissen met nieuwe kleuren? Brede kozijnen, dakkapel, "
                       "boeidelen en voordeur: aandachtspunten, onderhoud en RAL-codes.",
        "intro": "Veel rijtjeshuizen uit de jaren 70 en 80 hebben brede kozijnen, een dakkapel en een donkere "
                 "steen. Met een andere kleur op het houtwerk ziet zo’n huis er in één keer frisser uit, zonder "
                 "te verbouwen.",
        "kenmerken": [
            "Op de foto zie je rijwoningen in Lelystad, met een grijs pannendak, dakkapellen en lichte "
            "kozijnen. Zo’n rij kom je in Flevoland en daarbuiten veel tegen. Het houtwerk is vaak "
            "eenvoudig van vorm, maar breed: grote kozijnen, een houten paneel onder of naast het raam en een "
            "dakkapel met brede boeidelen.",
            "Juist die brede vlakken bepalen het beeld. In een donkere kleur ogen ze slanker en rustiger. In "
            "een lichte kleur geven ze een vriendelijk, open gevelbeeld. Een opvallende voordeur maakt het "
            "verschil tussen jouw huis en dat van de buren, zonder dat de rij onrustig wordt.",
        ],
        "onderdelen": [
            ("Kozijnen en ramen", "Vaak breed en vlak. Een nieuwe kleur valt hier direct op."),
            ("Panelen en borstweringen", "Houten of plaatmateriaal onder of naast de ramen. Plaatmateriaal "
                                         "vraagt soms een andere voorbehandeling dan hout."),
            ("Dakkapel", "Boeidelen, zijwangen en kozijnen. Hoog en in de volle zon, dus de eerste plek waar "
                         "verf slijt."),
            ("Boeidelen en windveren", "De planken langs de dakrand. Vaak de eerste plek waar verf bladdert."),
            ("Voordeur en bergingsdeur", "Samen een goede plek voor één accentkleur."),
        ],
        "letop": [
            "Ga je van licht naar donker of andersom? Dan dekt één laag meestal niet. Vraag of die extra laag in "
            "de offerte zit.",
            "Donkere verf wordt in de zon warmer dan lichte. Op een gevel op het zuiden of westen vraag je om "
            "verf die daarvoor bedoeld is.",
            "Was het houtwerk eerder gebeitst? Dan moet het anders worden voorbehandeld als je overstapt op "
            "dekkende verf. Laat de schilder vooraf kijken wat er nu op zit.",
            "Hoort je huis bij een VvE of een verhuurder? Dan liggen de buitenkleuren vaak vast. Vraag het vooraf.",
        ],
        "onderhoud": "Bij een rijtjeshuis is het slim om met de buren samen te laten schilderen. De steiger of "
                     "hoogwerker hoeft dan maar één keer te komen, en de rij blijft één geheel.",
        "kleuren": [
            "Voor deze woningen bestaat geen historische kleur die je moet volgen. Je hebt dus veel vrijheid. "
            "Antracietgrijs (RAL 7016) maakt brede kozijnen rustig en strak. Crèmewit (RAL 9001) met een "
            "zacht groen geeft een lichter, vriendelijker beeld. Kijk wel naar de steen: die blijft, en de "
            "verf moet erbij passen.",
        ],
        "kosten": [("/kosten/kozijnen-schilderen/", "Wat kost kozijnen schilderen?"),
                   ("/kosten/dakkapel-schilderen/", "Wat kost een dakkapel schilderen?")],
        "plaatsen": ["lelystad", "almere", "dronten"],
        "bronnen": ["consumentenbond"],
    },
    "villa": {
        "titel": "Kleuren voor een villa of landhuis",
        "h1": "Kleuren voor je villa of landhuis",
        "description": "Kleuradvies voor een vrijstaande villa of een landhuis in het Gooi: kozijnen, luiken, "
                       "lijsten en voordeur. Wat je schildert, waar je op let en RAL-codes.",
        "intro": "Een villa of landhuis heeft veel geschilderd houtwerk: grote kozijnen, luiken, lijsten onder "
                 "de dakrand en soms een gepleisterde gevel. De kleuren bepalen voor een groot deel hoe "
                 "deftig of juist hoe ontspannen het huis oogt.",
        "kenmerken": [
            "In het Gooi staan veel villa’s en landhuizen uit het begin van de twintigste eeuw. Op de foto’s "
            "zie je twee voorbeelden uit Hilversum, allebei uit 1911: een bakstenen landhuis aan de "
            "Soestdijkerstraatweg, ontworpen door Philip A. Wormser, en het witte landhuis ’t Zuidereind aan de "
            "Utrechtseweg, ontworpen door H.W. Leliman. Beide zijn gemeentelijk monument.",
            "Bij zulke huizen is de verhouding tussen gevel en houtwerk belangrijk. Op baksteen valt wit of "
            "crème houtwerk op en tekent het de vorm van het huis. Bij een witte gevel draait het om: daar "
            "geven luiken en de voordeur in een donkere kleur het huis houvast.",
        ],
        "onderdelen": [
            ("Kozijnen en ramen", "Vaak groot en met roedes of een bovenlicht. Veel meters en veel snijwerk."),
            ("Luiken", "Moeten er meestal af om goed te schilderen, ook aan de achterkant. Vraag of dat in de "
                       "offerte zit."),
            ("Lijsten, gootklossen en overstekken", "Hoog werk, vaak met profielen. Een steiger of "
                                                    "hoogwerker hoort erbij."),
            ("Voordeur, luifel en bovenlicht", "Het visitekaartje van het huis."),
            ("Gepleisterde of geschilderde gevel", "Een vak apart. Gebruik verf die past bij wat er al op "
                                                   "zit, anders kan de laag gaan bladderen."),
        ],
        "letop": [
            "Is je villa een gemeentelijk of rijksmonument, of staat hij in een beschermd dorpsgezicht? Vraag "
            "dan eerst bij de gemeente of je een andere kleur mag kiezen.",
            "Een bakstenen gevel laten schilderen of keimen draai je niet zomaar terug. Laat je daar apart "
            "over adviseren.",
            "Bij veel houtwerk loont een onderhoudsplan: niet alles in één keer, maar elk jaar de zwaarst "
            "belaste kant.",
            "Rieten daken en dakkapellen in riet vragen voorzichtig werk. Vraag hoe de schilder het riet "
            "beschermt.",
        ],
        "onderhoud": "Bij een groot huis met veel houtwerk lopen de kosten van een volledige schilderbeurt snel op. "
                     "Daarom laten veel eigenaren per jaar een gevel doen. Zo blijft de kwaliteit gelijk en "
                     "spreid je de kosten.",
        "kleuren": [
            "Groen met wit of crème is een klassieke keuze. Volgens het "
            + bron("olm-kozijn", "Nederlands Openluchtmuseum") + " hadden deftige huizen vaak groene "
            "kozijnen, omdat groene verf lang duur was. Het museum waarschuwt ook dat groen dat uit geel en "
            "blauw pigment is gemengd, na verloop van tijd blauwer en donkerder wordt. Kies daarom een goede "
            "kwaliteit verf en bekijk een proefvlak in het daglicht.",
        ],
        "kosten": [("/kosten/huis-schilderen/", "Wat kost je huis buiten laten schilderen?"),
                   ("/kosten/schilder-uurtarief/", "Wat is een normaal uurtarief voor een schilder?")],
        "plaatsen": ["hilversum", "blaricum", "naarden"],
        "bronnen": ["olm-kozijn", "rijksoverheid", "consumentenbond"],
    },
    "polder": {
        "titel": "Kleuren voor een polderwoning in Flevoland",
        "h1": "Kleuren voor je polderwoning of boerderij",
        "description": "Kleuradvies voor een woning of boerderij in de polder: houten topgevel, staldeuren, "
                       "kozijnen en boeidelen in zon en wind. Aandachtspunten en RAL-codes.",
        "intro": "In de open polder staat een huis vol in de zon en de wind. Dat vraagt iets van de verf, en "
                 "van je kleurkeuze. Lichte, rustige kleuren passen bij het weidse landschap en worden minder "
                 "heet in de zon.",
        "kenmerken": [
            "De Noordoostpolder en Flevoland zijn na de drooglegging ingericht als nieuw land. De "
            + bron("rce-nop", "Rijksdienst voor het Cultureel Erfgoed") + " noemt de Noordoostpolder een "
            "wederopbouwgebied van nationaal belang. Op de foto’s zie je twee wederopbouwboerderijen die "
            "gemeentelijk monument zijn: een bij Tollebeek met een blauw geschilderde houten topgevel, en een "
            "bij Emmeloord met groene staldeuren.",
            "Veel woningen en boerderijen in de polder hebben grote houten delen: een betimmerde topgevel, "
            "brede staldeuren of een houten aanbouw. Die vlakken bepalen het beeld. Ook bij nieuwere "
            "twee-onder-een-kapwoningen in Dronten, Emmeloord of Zeewolde vangt het houtwerk veel weer.",
        ],
        "onderdelen": [
            ("Gevelbetimmering", "Houten delen op de topgevel of de aanbouw. Grote vlakken die in één kleur "
                                 "rustig ogen."),
            ("Staldeuren en garagedeuren", "Groot, vaak met veel naden. Hier zie je slijtage snel."),
            ("Kozijnen en ramen", "Staan in de open polder vol in zon en regen."),
            ("Boeidelen en windveren", "Bij een groot dakvlak lange stukken, hoog en in de wind."),
            ("Voordeur", "Een plek voor een accent dat bij de rest past."),
        ],
        "letop": [
            "Wind en zon werken hier harder dan in een beschutte straat. Plan het schilderwerk op tijd en kies "
            "verf die voor buiten in zware omstandigheden bedoeld is.",
            "Donkere kleuren worden in de zon warmer. Op grote houten vlakken kan dat het hout laten werken. "
            "Lichtere tinten zijn hier vaak de veiligere keuze.",
            "Betimmering heeft veel naden en kopse kanten. Laat die goed afdichten, daar komt vocht het eerst in.",
            "Is je boerderij een gemeentelijk monument? Vraag de gemeente dan vooraf of een andere kleur mag.",
        ],
        "onderhoud": "Voor huizen in het open veld is een jaarlijkse controle extra belangrijk. Een klein "
                     "scheurtje in de verf op de windkant kan in één winter flink vocht doorlaten.",
        "kleuren": [
            "Zachte groentinten, gebroken wit en grijsblauw passen goed bij het open, groene land. Een "
            "combinatie als Zuiver wit (RAL 9010) met Bleekgroen (RAL 6021) oogt rustig in het volle licht. "
            "Wie meer contrast wil, kiest Duifblauw (RAL 5014) voor de ramen en een donkerblauwe voordeur.",
        ],
        "kosten": [("/kosten/huis-schilderen/", "Wat kost je huis buiten laten schilderen?"),
                   ("/kosten/schilderen-per-m2/", "Wat kost schilderen per m²?")],
        "plaatsen": ["emmeloord", "tollebeek", "dronten"],
        "bronnen": ["rce-nop", "consumentenbond"],
    },
    "monument": {
        "titel": "Kleuren voor een monument in een vestingstad",
        "h1": "Kleuren voor een monument of historisch pand",
        "description": "Een monument of historisch pand schilderen in Kampen, Elburg of Amersfoort? Over "
                       "vergunning, historische kleuren, kozijnen en luiken, met RAL-codes.",
        "intro": "Bij een monument of een oud pand in een historische binnenstad kies je niet zomaar een "
                 "nieuwe kleur. Soms heb je een vergunning nodig, en altijd is het goed om te weten welke "
                 "kleuren echt bij de tijd van het pand horen.",
        "kenmerken": [
            "Op de foto’s zie je twee rijksmonumenten: Zuiderwalstraat 19 in Elburg, met witte kozijnen, "
            "zwarte luiken en een zwarte voordeur, en IJsselkade 37 in Kampen, een wit gepleisterd pand met "
            "blauwgrijze ramen. De "
            + bron("kampen", "gemeente Kampen") + " schrijft dat de hele binnenstad door het Rijk is "
            "aangewezen als beschermd stadsgezicht.",
            "Typisch voor zulke panden zijn hoge schuiframen met roedes, een kroonlijst, luiken en een "
            "voordeur met bovenlicht. Al dat houtwerk is vaak ouder en fijner geprofileerd dan bij een "
            "gewone woning. Dat vraagt een schilder die met oud hout en traditionele verf kan werken.",
        ],
        "onderdelen": [
            ("Schuiframen en roedes", "Veel kleine vlakken en oude stopverf. Precisiewerk."),
            ("Kroonlijst en gootlijst", "Hoog en vaak met klossen of profielen. Een steiger hoort erbij."),
            ("Luiken", "Vaak in een eigen kleur, soms met een patroon. Ze moeten er meestal af."),
            ("Voordeur en bovenlicht", "Vaak het oudste stuk houtwerk van de gevel."),
            ("Pleisterwerk", "Gepleisterde gevels vragen een verf die vocht doorlaat. Overleg met de "
                             "schilder welke verf er nu op zit."),
        ],
        "letop": [
            "Volgens de " + bron("rijksoverheid", "Rijksoverheid") + " heb je bij een monument geen "
            "vergunning nodig voor gewoon onderhoud als kleuren, materialen, details, vorm en profiel hetzelfde "
            "blijven. Kies je een andere kleur, dan geldt die vrijstelling dus niet. Vraag het vooraf na bij je "
            "gemeente.",
            "Ook een pand dat zelf geen monument is, kan in een beschermd stadsgezicht staan. Dan kan een "
            "kleurwissel ook vergunningplichtig zijn.",
            "Laat oude verflagen niet zomaar wegbranden of afbijten. Daarmee verdwijnt ook informatie over de "
            "oorspronkelijke kleuren.",
            "Werk met een schilder die ervaring heeft met monumenten, en vraag naar eerdere klussen.",
        ],
        "onderhoud": "Oud hout is vaak van goede kwaliteit, maar de verbindingen en onderdorpels zijn kwetsbaar. "
                     "Herstel kleine schade direct, dan blijft er meer origineel hout bewaard.",
        "kleuren": [
            "Monumentengroen klinkt oud, maar dat is het niet. Het "
            + bron("olm-gebouwen", "Nederlands Openluchtmuseum") + " schrijft dat monumentengroen pas sinds de "
            "twintigste eeuw bestaat. Daarvoor werden heel andere groenen gebruikt, van grijsgroen tot helder "
            "lichtgroen. Ook ‘Zaans groen’ bestaat volgens het museum niet als één kleur: in de Zaanstreek "
            "werden verschillende groenen gebruikt.",
            "Rood heeft ook een lange geschiedenis. Volgens het "
            + bron("olm-kozijn", "Openluchtmuseum") + " werd in de Middeleeuwen echt ossenbloed gebruikt als "
            "bindmiddel in verf. Wil je weten welke kleur jouw pand vroeger had? Dan kan een kleurhistorisch "
            "onderzoek van de oude verflagen uitsluitsel geven.",
        ],
        "kosten": [("/kosten/kozijnen-schilderen/", "Wat kost kozijnen schilderen?"),
                   ("/kosten/schilder-uurtarief/", "Wat is een normaal uurtarief voor een schilder?")],
        "plaatsen": ["kampen", "elburg", "amersfoort"],
        "bronnen": ["rijksoverheid", "kampen", "olm-gebouwen", "olm-kozijn", "consumentenbond"],
    },
    "nieuwbouw": {
        "titel": "Kleuren voor een moderne nieuwbouwwoning",
        "h1": "Kleuren voor je nieuwbouwwoning",
        "description": "Nieuwbouw laten schilderen? Over houten, kunststof en aluminium kozijnen, "
                       "gevelbekleding, boeidelen en moderne kleuren, met onderhoud en RAL-codes.",
        "intro": "Bij een nieuwbouwwoning is het houtwerk vaak strak en eenvoudig, en zijn er grote glasvlakken. "
                 "Toch valt er veel te kiezen: de kleur van de kozijnen, de boeidelen, houten gevelbekleding en "
                 "de voordeur.",
        "kenmerken": [
            "Op de foto’s zie je nieuwbouw in het Homeruskwartier in Almere Poort: woningen in allerlei "
            "kleuren en vormen naast elkaar, met grote ramen en strakke lijnen. In zo’n wijk zie je goed hoe "
            "verschillend je met kleur kunt omgaan.",
            "Veel nieuwbouw heeft kozijnen van kunststof of aluminium, of houten kozijnen die al in de fabriek "
            "zijn afgelakt. Houten gevelbekleding, boeidelen en een houten voordeur komen ook veel voor. Elk "
            "materiaal vraagt een eigen aanpak.",
        ],
        "onderdelen": [
            ("Houten kozijnen", "Vaak in de fabriek voorbehandeld. De eerste beurt door een schilder komt "
                                "meestal pas na een aantal jaar."),
            ("Kunststof en aluminium kozijnen", "Kunnen geschilderd worden, maar alleen na een speciale "
                                                "voorbehandeling. Vraag daarnaar in de offerte."),
            ("Houten gevelbekleding", "Dekkend geschilderd of transparant gebeitst. Beits laat de nerf zien, "
                                      "maar vraagt vaker onderhoud."),
            ("Boeidelen", "Vaak donker, als strakke lijn langs de dakrand."),
            ("Voordeur", "Een houten deur geeft warmte tussen de strakke vlakken."),
        ],
        "letop": [
            "Kijk in je opleverdossier of de garantie van de fabrikant iets zegt over overschilderen. Bij "
            "kunststof en aluminium kan dat de garantie raken.",
            "Antraciet en zwart worden in de zon heet. Kies verf die daarvoor bedoeld is, zeker op het zuiden.",
            "Woon je in een wijk met een beeldkwaliteitsplan of een VvE? Dan kunnen er regels zijn voor "
            "buitenkleuren.",
            "Bij grote glasvlakken is goed afplakken extra belangrijk. Verfspatten op glas met een coating "
            "krijg je er lastig af.",
        ],
        "onderhoud": "Ook fabrieksmatig gelakt hout heeft onderhoud nodig. Laat na een paar jaar kijken of de "
                     "laklaag nog dicht is, vooral op de hoeken en aan de onderkant.",
        "kleuren": [
            "Bij nieuwbouw ben je vrij in je keuze, tenzij er een beeldkwaliteitsplan geldt. Antracietgrijs "
            "(RAL 7016) op een lichte gevel geeft strakke lijnen bij grote ramen. Met houtkleuren tegen een "
            "donkere steen krijgt een moderne woning juist warmte.",
        ],
        "kosten": [("/kosten/kozijnen-schilderen/", "Wat kost kozijnen schilderen?"),
                   ("/kosten/huis-schilderen/", "Wat kost je huis buiten laten schilderen?")],
        "plaatsen": ["almere", "zeewolde", "lelystad"],
        "bronnen": ["consumentenbond"],
    },
}


# --- inspiratie-ronde 2: verdieping van de dunste gidsen (jaren70, nieuwbouw, polder) ---
# Extra kleuralinea's en extra FAQ's. Alleen algemeen kleuradvies, geen nieuwe historische
# claims. Links naar de nieuwe kleuradviespagina's (kleuradvies.py).
GIDSEN["jaren70"]["kleuren"] += [
    "Veel jaren-70-woningen hebben brede, liggende kozijnen en houten delen tussen de ramen, zoals "
    "borstweringen en betimmering onder de ramen. Geef je die allemaal dezelfde kleur als de kozijnen, dan "
    "wordt de gevel één rustig vlak. Geef je ze een eigen kleur, dan zie je juist de horizontale lijnen goed. "
    "Kies dan een tint uit dezelfde familie, bijvoorbeeld kwartsgrijs (RAL 7039) bij antraciet.",
    "Bruine en oranjebruine baksteen, veel gebruikt in deze periode, gaat goed samen met warme tinten: crèmewit, "
    "licht ivoor (RAL 1015), olijfgroen of een warm grijs. Koel helder wit kan er hard tegen afsteken. "
    "Op <a href=\"/kleuradvies/kozijnen/\">kleur kozijnen kiezen</a> zie je voorbeelden per steenkleur.",
    "In een rij woningen kijk je ook naar de buren. Een andere kleur mag meestal, maar een rij met dezelfde "
    "kleuren oogt rustig. Wil je een eigen accent zonder uit de toon te vallen? Gebruik dat dan op de voordeur; "
    "zie <a href=\"/kleuradvies/voordeur/\">kleur voordeur kiezen</a>.",
]
GIDSEN["jaren70"]["faq"] = [
    ("Welke kleur kozijnen past bij een jaren-70-woning met bruine steen?",
     "Warme lichte tinten zoals crèmewit of licht ivoor geven contrast en maken de gevel lichter. Antraciet of "
     "zwartgrijs maakt het geheel strak en modern. Koel helder wit steekt vaak hard af tegen bruine steen."),
    ("Kan ik de betimmering onder de ramen een andere kleur geven?",
     "Ja. Dezelfde kleur als de kozijnen geeft rust; een tint uit dezelfde kleurfamilie laat de liggende lijnen "
     "van de gevel juist zien. Laat bij gebeitst hout eerst kijken wat er nu op zit."),
]

GIDSEN["nieuwbouw"]["kleuren"] += [
    "Bij nieuwbouw zijn de kozijnen vaak van kunststof of aluminium, en worden ze niet geschilderd zolang ze "
    "goed zijn. Wat wél vaak houtwerk is: de voordeur, boeidelen, dakkapellen en soms een houten gevel- of "
    "dakrand. Daar kies je een kleur die aansluit bij de kozijnen die blijven, of een bewust accent.",
    "Moderne gevels hebben vaak meerdere materialen: baksteen, stucwerk, hout en metaal. Houd dan het aantal "
    "kleuren klein. Laat de materialen het werk doen, en kies voor het geschilderde werk één kleur die al in de "
    "gevel zit, zoals het grijs van de kozijnen of de toon van de steen.",
    "Binnen begin je bij nieuwbouw vaak met witte muren. Wil je kleur, kijk dan eerst naar de lichtval: een "
    "woonkamer met grote ramen op het zuiden kan koele tinten aan, een kamer op het noorden vraagt warmere. "
    "Lees meer op <a href=\"/kleuradvies/lichtval/\">kleur en lichtval</a> en "
    "<a href=\"/kleuradvies/woonkamer/\">kleur woonkamer kiezen</a>. Nieuw stucwerk moet eerst goed droog zijn "
    "en een voorstrijklaag krijgen; zie <a href=\"/kennisbank/nieuw-stucwerk-schilderen/\">nieuw stucwerk schilderen</a>.",
]
GIDSEN["nieuwbouw"]["faq"] = [
    ("Mag ik kunststof kozijnen van een nieuwbouwwoning schilderen?",
     "Dat kan met een speciale verf, maar kijk eerst in je opleverdossier of de garantie van de fabrikant iets "
     "zegt over overschilderen. Lees ook wat het kost op <a href=\"/kosten/kunststof-kozijnen-schilderen/\">kunststof "
     "kozijnen schilderen</a>."),
    ("Welke kleur voordeur past bij een moderne woning?",
     "Antraciet en zwart passen bij bijna elke moderne gevel. Wil je een accent, dan geeft een warme kleur zoals "
     "maisgeel of een houtkleur juist warmte bij grijze of donkere steen."),
]

GIDSEN["polder"]["kleuren"] += [
    "In het open polderlandschap zie je een huis of boerderij van ver. Kleuren die passen bij het land, zoals "
    "gebroken wit, zacht groen, grijsblauw en de rode of grijze kleur van het dak, vallen dan minder hard op dan "
    "felle tinten. Dat is geen regel, maar wel de reden dat die kleuren hier zo vaak terugkomen.",
    "Grote houten vlakken, zoals deuren van een schuur of betimmering, vangen veel zon en wind. Lichte en "
    "middentinten blijven daar vaak langer mooi dan heel donkere kleuren. Kies je toch donker, dan is goede "
    "verf en tijdig onderhoud extra belangrijk. Lees meer over donkergroen op "
    "<a href=\"/kleuradvies/grachtengroen/\">grachtengroen en monumentengroen</a>, en over kleuren combineren op "
    "<a href=\"/kleuradvies/kleurcombinaties/\">kleurcombinaties</a>.",
]
GIDSEN["polder"]["faq"] = [
    ("Welke kleuren passen bij een boerderij in de polder?",
     "Gebroken wit, zacht groen, grijsblauw en donkergroen passen goed bij het open, groene land en bij een rood "
     "of grijs pannendak. Felle kleuren vallen in het open landschap sterk op."),
    ("Zijn donkere kleuren een probleem op een schuur of boerderij?",
     "Op grote houten vlakken in de volle zon worden donkere kleuren warm, waardoor het hout meer werkt. Met "
     "goede verf gaat het prima, maar reken op iets vaker onderhoud. Lichte tinten zijn de veiligere keuze."),
]
# --- einde inspiratie-ronde 2 ---
