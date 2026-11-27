# -*- coding: utf-8 -*-
"""Extra inhoud voor de zes dienstpagina's (/schilderwerk/<dienst>/), lokale ronde.

Per dienst:
  intentie  -> blok 'In het kort' bovenaan: het antwoord op de vraag waarmee mensen zoeken
  lagen     -> het werk laag voor laag: (stap, wat er gebeurt, wachttijd voor de volgende stap)
  cyclus    -> onderhoudscyclus: (onderdeel, hoe vaak)
  keuze     -> wanneer kies je wat: (situatie, keuze, waarom)
  faq       -> extra vragen, bovenop DIENSTEN[...]['faq'] in data.py
  links     -> kennisbankartikelen die er extra bij horen (bestaande slugs)

Droog- en wachttijden zijn bewust ranges. Ze komen uit de technische bladen van verffabrikanten
en gelden bij ongeveer 20 °C en normale luchtvochtigheid. Kouder of vochtiger weer = langer wachten.
Geen claims over schilders, reviews of aantallen.
"""

from kosten_data import KOSTEN
from kennisbank import ARTIKELEN, _link

_ART = {a["slug"]: a for a in ARTIKELEN}

DROOG_NOOT = ("Wachttijden gelden bij ongeveer 20 °C en normale luchtvochtigheid, en verschillen per verf. "
              "Ze komen uit de technische bladen van verffabrikanten; het blad van de verf die jouw schilder "
              "gebruikt, is leidend. Bij kou of hoge luchtvochtigheid duurt alles langer.")

UITLEG = {
    "binnenschilderwerk": {
        "intentie": [
            ("Wat kost het?", "Reken op €10 tot €22 per m² wand of plafond, inclusief verf en 9% btw. Een woonkamer met hal komt al snel op 60 tot 90 m²."),
            ("Hoe lang duurt het?", "Een woonkamer is meestal in twee tot drie werkdagen klaar, inclusief afplakken en voorwerk."),
            ("Wat bepaalt de prijs?", "Vooral de staat van de muur. Gaten, scheuren en oude spachtelputz kosten meer tijd dan het schilderen zelf."),
        ],
        "lagen": [
            ("Leeghalen en afdekken", "Meubels naar het midden, vloer en plinten afdekken, stopcontacten en schakelaars losschroeven of afplakken.", "—"),
            ("Repareren", "Gaten en scheuren vullen met vulmiddel, na drogen vlak schuren. Bij veel herstel volgt een extra laag om vlekken te voorkomen.", "vulmiddel 1 tot 24 uur, afhankelijk van dikte"),
            ("Voorstrijken", "Nieuw stucwerk, kale plekken en sterk zuigende muren krijgen een voorstrijkmiddel of grondlaag. Zo droogt de verf overal gelijk.", "meestal 2 tot 12 uur"),
            ("Eerste laag muurverf", "Eerst de randen met de kwast, daarna nat-in-nat rollen per wand. Zo zie je geen aanzetten.", "meestal 4 tot 6 uur tot de volgende laag"),
            ("Tweede laag", "De tweede laag geeft de egale kleur. Bij een sterke kleurwissel is soms een derde laag nodig.", "na een dag droog aan te raken; muurverf is pas na ongeveer twee tot vier weken volledig hard"),
            ("Houtwerk binnen", "Deuren, kozijnen en plinten licht schuren, ontvetten en twee lagen lak.", "watergedragen lak meestal 4 tot 8 uur, terpentinehoudende lak meestal 16 tot 24 uur"),
        ],
        "cyclus": [
            ("Muren in woonkamer en slaapkamers", "om de 5 tot 10 jaar, of eerder bij een andere kleur"),
            ("Hal, trapgat en keuken", "om de 3 tot 6 jaar: hier stoot en vlekt het meest"),
            ("Plafonds", "om de 8 tot 12 jaar, in de badkamer eerder"),
            ("Binnendeuren en kozijnen (lak)", "om de 8 tot 15 jaar; bijwerken bij beschadigingen"),
        ],
        "keuze": [
            ("Gladde, gave muren en weinig spullen in huis", "Muurverf rollen", "Netjes resultaat, je kunt in huis blijven en het is per m² vaak het voordeligst."),
            ("Lege woning of nieuwbouw met veel m²", "Latex spuiten", "Sneller bij grote oppervlakken; in een leeg huis weegt het afplakken minder zwaar."),
            ("Muren met haarscheurtjes of oneffenheden", "Glasvlies of renovlies, daarna schilderen", "Het vlies overbrugt kleine scheuren, de verf erop is later makkelijk te vernieuwen."),
            ("Badkamer of vochtige ruimte", "Vochtbestendige of schimmelwerende muurverf", "Gewone muurverf laat in vochtige ruimtes sneller los en krijgt eerder plekken."),
        ],
        "faq": [
            ("Hoeveel lagen muurverf zijn nodig?", "Meestal twee. Bij nieuw stucwerk komt daar een voorstrijklaag bij, en bij een donkere kleur over een lichte (of andersom) soms een derde laag."),
            ("Moet ik de kamer helemaal leeghalen?", "Nee, meestal niet. Zet meubels in het midden van de kamer en haal kleine spullen en schilderijen weg. Spreek met de schilder af wie dat doet; sommige schilders rekenen er tijd voor."),
            ("Kan ik direct na het schilderen weer meubels terugzetten?", "Na een dag kun je de ruimte weer gebruiken. Zet kasten nog een paar dagen niet strak tegen de muur: muurverf is pas na enkele weken volledig hard."),
            ("Wat is het verschil tussen mat en zijdeglans?", "Mat verbergt oneffenheden het best en is de standaard voor muren en plafonds. Zijdeglans is beter afwasbaar, maar laat elk bultje zien. Voor hal en keuken kiezen veel mensen een goed afwasbare matte verf."),
            ("Kan er in de winter binnen geschilderd worden?", "Ja. Binnen hangt het af van de temperatuur in huis, niet van het weer. De winter is juist rustig bij schilders, dus je hebt meer keuze."),
            ("Moet nieuw stucwerk eerst drogen?", "Ja. Stucwerk moet goed droog zijn voordat er verf op komt; anders kan de verf gaan bladderen of vlekken. Hoe lang dat duurt, lees je in ons artikel over nieuw stucwerk schilderen."),
        ],
        "links": ["nieuw-stucwerk-schilderen", "plafond-schilderen-zonder-strepen", "latex-of-muurverf", "schimmel-op-muur", "binnen-schilderen-in-de-winter"],
    },
    "buitenschilderwerk": {
        "intentie": [
            ("Wat kost het?", "Reken op €90 tot €190 per kozijn, inclusief verf en 9% btw. Een tussenwoning kost samen vaak €2.200 tot €5.500."),
            ("Hoe vaak moet het?", "Dekkende verf op houten kozijnen gaat meestal vier tot acht jaar mee. De kant met de meeste zon en regen is het eerst aan de beurt."),
            ("Wanneer laat je het doen?", "Van april tot en met oktober, bij droog weer en boven ongeveer 5 tot 8 °C. In september en oktober is de agenda vaak ruimer."),
        ],
        "lagen": [
            ("Opname", "De schilder loopt om het huis, prikt in verdachte plekken en schrijft op wat er hersteld moet worden. Hier valt de prijs.", "—"),
            ("Reinigen", "Vuil, groene aanslag en vet eraf met een reiniger. Daarna laten drogen.", "hout moet droog zijn: meestal minimaal een dag na reinigen of regen"),
            ("Schuren en herstellen", "Losse en bladderende verf eraf, randen bijschuren, houtrot uitfrezen en vullen, kitnaden vernieuwen.", "vulmiddel en kit: een paar uur tot een dag, volgens het blad"),
            ("Gronden", "Kale plekken krijgen een grondverf. Die hecht op het hout en vormt de basis voor de lak.", "meestal 4 tot 24 uur, afhankelijk van het type"),
            ("Tussenlaag (voorlak)", "Bij kaal hout of veel herstel volgt een tussenlaag die de dikte opbouwt.", "watergedragen meestal 4 tot 8 uur, terpentinehoudend meestal 16 tot 24 uur"),
            ("Aflak", "De laatste laag geeft kleur, glans en bescherming. Bij goed onderhouden werk zijn twee lagen vaak genoeg.", "regenvast na enkele uren; volledig hard na enkele dagen tot weken"),
        ],
        "cyclus": [
            ("Dekkend geschilderde houten kozijnen, beschutte kant", "om de 6 tot 8 jaar"),
            ("Dekkend geschilderd hout op de zon- en regenkant", "om de 4 tot 6 jaar"),
            ("Transparante of semitransparante beits", "vaker dan dekkende verf; Centrum Hout noemt beits onderhoudsgevoeliger"),
            ("Boeidelen en windveren", "zelfde ritme als de kozijnen; ze zitten hoog, dus combineren scheelt een steiger"),
            ("Kitnaden en glaslatten", "elke beurt nalopen: hier komt het water binnen"),
        ],
        "keuze": [
            ("Hout in goede staat, verf alleen dof of verkleurd", "Licht schuren en één of twee lagen aflak", "Op tijd bijhouden is het goedkoopst: weinig voorwerk, geen herstel."),
            ("Bladderende verf en kale plekken", "Volledige beurt: schuren, gronden, voorlak en aflak", "Op kaal hout hecht aflak niet goed zonder grondlaag."),
            ("Zacht hout of zwarte plekken", "Eerst houtrotreparatie, dan schilderen", "Verf over rot hout houdt het vocht binnen en het rot gaat door."),
            ("Kunststof kozijnen die vergeeld zijn", "Speciaal systeem voor kunststof", "Gewone lak hecht niet goed op kunststof. Zie de pagina over kunststof kozijnen schilderen."),
            ("Kozijnen al veel beurten gehad en rot in meerdere hoeken", "Laat vervangen overwegen", "Soms is nieuw goedkoper dan nog een keer veel herstel. Een eerlijke schilder zegt dat."),
        ],
        "faq": [
            ("Welke kant van het huis moet als eerste?", "Meestal de kant met de meeste zon en slagregen. In Nederland komt de meeste regen met zuidwestenwind (KNMI). De beschutte noord- of oostkant kan vaak langer mee."),
            ("Hoeveel lagen verf komen er op een kozijn?", "Bij kaal hout: grondverf, voorlak en aflak. Bij goed onderhouden kozijnen zijn één of twee lagen aflak vaak genoeg. Laat het aantal lagen in de offerte zetten."),
            ("Mag het regenen na het schilderen?", "De meeste buitenlakken zijn na enkele uren regenvast. Daarom begint een schilder niet als er binnen een paar uur regen komt, en schildert hij niet op nat hout."),
            ("Wat is het verschil tussen dekkend en transparant?", "Dekkende verf bedekt het hout helemaal en beschermt het langst. Transparante beits laat de houtnerf zien, maar moet vaker worden bijgewerkt."),
            ("Kan ik de ramen open tijdens het schilderen?", "Niet als ze net geschilderd zijn: ramen en deuren blijven open staan tot de lak droog genoeg is, anders plakken ze vast. Vraag de schilder hoe hij dat per dag regelt."),
            ("Moet ik een vergunning hebben voor een andere kleur?", "Bij een gewone woning meestal niet. Bij een monument of in een beschermd stads- of dorpsgezicht vaak wel. Vraag het vooraf na bij je gemeente."),
        ],
        "links": ["hoe-vaak-buitenschilderwerk", "welke-verf-voor-kozijnen", "kozijnen-schuren-en-voorbereiden", "grondverf-of-voorlak", "verf-bladdert-af", "sikkens-sigma-of-histor"],
    },
    "houtrot-reparatie": {
        "intentie": [
            ("Wat kost het?", "Reken op €50 tot €275 per plek. Een kleine plek met vulmiddel zit aan de onderkant, een nieuw stuk hout of een nieuwe onderdorpel aan de bovenkant."),
            ("Hoe herken je houtrot?", "Hout dat zacht aanvoelt, bladderende verf in een onderhoek, donkere plekken of scheurtjes in de verf. Prik met een schroevendraaier: zakt hij erin, dan is het raak."),
            ("Hoe snel moet het?", "Liefst voor de winter. Vocht en vorst maken een kleine plek in een paar jaar groter."),
        ],
        "lagen": [
            ("Opsporen", "Alle verdachte plekken prikken en markeren. Vaak zit er meer dan je ziet.", "—"),
            ("Uitfrezen", "Al het zachte en aangetaste hout eruit, tot er gezond hout over is.", "het hout moet daarna droog zijn: soms een dag of langer"),
            ("Voorbehandelen", "Het gezonde hout krijgt een primer of consolidant, zodat het vulmiddel goed hecht.", "meestal minder dan een uur tot enkele uren"),
            ("Vullen of aanhelen", "Kleine plekken vullen met een tweecomponenten vulmiddel. Grotere stukken vervangen door een inzetstuk van nieuw hout.", "vulmiddel is na een paar uur schuurbaar, afhankelijk van type en temperatuur"),
            ("Vlak schuren en gronden", "Reparatie strak schuren in de vorm van het kozijn, daarna gronden.", "grondverf meestal 4 tot 24 uur"),
            ("Afschilderen", "Twee lagen lak over de reparatie en het kozijn eromheen, zodat er geen naad overblijft waar water in kan.", "zie buitenschilderwerk"),
        ],
        "cyclus": [
            ("Gerepareerde plek", "meenemen in elke schilderbeurt; controleer de naad tussen vulmiddel en hout"),
            ("Onderdorpels en kozijnhoeken", "elk jaar even kijken en prikken, vooral na de winter"),
            ("Kitnaden rond glas en kozijn", "bij elke schilderbeurt vernieuwen waar ze scheuren"),
        ],
        "keuze": [
            ("Plek kleiner dan ongeveer een handpalm", "Vullen met tweecomponenten vulmiddel", "Snel, sterk en goedkoper dan nieuw hout."),
            ("Groter stuk, maar de rest van het kozijn is gezond", "Inzetstuk van nieuw hout", "Nieuw hout houdt grote reparaties beter vast dan veel vulmiddel."),
            ("Onderdorpel grotendeels rot", "Nieuwe onderdorpel", "De dorpel vangt het meeste water; een nieuwe gaat weer jaren mee."),
            ("Rot in meerdere hoeken en stijlen", "Nieuw kozijn overwegen", "Bij veel plekken tegelijk kan vervangen op termijn goedkoper zijn."),
        ],
        "faq": [
            ("Hoe ontstaat houtrot?", "Door vocht dat langere tijd in het hout blijft zitten. Dat gebeurt via scheuren in de verf, kapotte kitnaden of plekken waar water blijft staan, zoals een onderdorpel."),
            ("Kan ik houtrot zelf repareren?", "Een kleine plek kan, als je al het zachte hout weghaalt en de plek goed afschildert. Twijfel je hoe groot de schade is, laat dan eerst iemand prikken: vaak zit er meer dan je ziet."),
            ("Welke btw geldt voor houtrot herstellen?", "Het schilderwerk valt bij een woning ouder dan twee jaar onder 9%. Timmerwerk, zoals een inzetstuk of een nieuwe dorpel, valt onder 21%. Een goede offerte noemt die posten apart."),
            ("Hoe lang duurt een houtrotreparatie?", "Een paar plekken met vulmiddel kosten meestal een tot twee dagen, omdat er droogtijd tussen de stappen zit. Inzetstukken en nieuwe dorpels duren langer."),
            ("Waarom zit houtrot vooral onderin een kozijn?", "Daar loopt het water naartoe en blijft het het langst staan. Ook de naad tussen dorpel en stijl is een zwakke plek."),
        ],
        "links": ["houtrot-herkennen-en-herstellen", "kozijnen-schuren-en-voorbereiden", "verf-bladdert-af", "hoe-vaak-buitenschilderwerk"],
    },
    "spuitwerk": {
        "intentie": [
            ("Wat kost het?", "Reken op €95 tot €185 per deur, inclusief lak en 9% btw. Keukens, trappen en radiatoren hebben een eigen prijs."),
            ("Waarom spuiten?", "Gespoten lak is strak, zonder kwaststrepen. Dat zie je vooral op deuren, keukenfronten en radiatoren."),
            ("Hoe lang ben je iets kwijt?", "Deuren en fronten worden vaak meegenomen naar de spuiterij. Reken op enkele dagen tot een week; vraag het vooraf."),
        ],
        "lagen": [
            ("Demonteren", "Deuren en fronten los, scharnieren en grepen eraf. Wat blijft hangen, wordt goed afgeplakt.", "—"),
            ("Schuren en ontvetten", "Oude lak opschuren en vet verwijderen, vooral bij keukenfronten. Hier valt of staat de hechting.", "—"),
            ("Primer of hechtgrond", "Een grondlaag die hecht op de ondergrond: hout, MDF, folie of metaal vraagt elk een eigen primer.", "meestal 1 tot 4 uur, afhankelijk van type"),
            ("Tussenschuren", "Na de grondlaag licht schuren voor een glad oppervlak.", "—"),
            ("Aflak spuiten", "Een of twee lagen lak in een stofvrije ruimte of goed afgeschermd op locatie.", "stofdroog vaak binnen een uur; hanteerbaar na enkele uren; volledig hard na enkele dagen tot weken"),
            ("Terugplaatsen", "Deuren en fronten terug, beslag erop, afstellen.", "voorzichtig gebruiken tot de lak volledig hard is"),
        ],
        "cyclus": [
            ("Gespoten binnendeuren", "10 jaar of langer; bijwerken bij stootplekken"),
            ("Gespoten keukenfronten", "8 tot 15 jaar, afhankelijk van gebruik en schoonmaakmiddelen"),
            ("Radiatoren", "10 jaar of langer; vergeling komt vooral door warmte"),
            ("Latex gespoten muren en plafonds", "zelfde ritme als gewone muurverf: om de 5 tot 10 jaar"),
        ],
        "keuze": [
            ("Veel deuren met oude kwaststrepen", "Spuiten", "Strak resultaat zonder strepen; het meeste werk zit in demonteren en schuren."),
            ("Eén of twee deuren bijwerken", "Kwasten en rollen", "Spuiten loont pas bij meerdere stuks, door de opstartkosten."),
            ("Keuken in goede staat, maar kleur gedateerd", "Keukenfronten spuiten", "Veel goedkoper dan een nieuwe keuken, als de kasten zelf nog goed zijn."),
            ("Folie op fronten laat los", "Vervangen", "Lak op losse folie bladdert mee; spuiten heeft dan geen zin."),
            ("Lege woning met veel muren en plafonds", "Latex spuiten", "Sneller dan rollen bij grote oppervlakken."),
        ],
        "faq": [
            ("Wordt er bij mij thuis gespoten of in een werkplaats?", "Allebei komt voor. Deuren en fronten gaan vaak mee naar een spuiterij, omdat het daar stofvrij is. Kozijnen, trappen en muren worden op locatie gespoten, met afscherming."),
            ("Kan ik een andere kleur kiezen dan de huidige?", "Ja. Met een goede primer kun je van donker naar licht en andersom. Een groot kleurverschil kan een extra laag vragen."),
            ("Hoe lang gaat gespoten lak mee?", "Bij normaal gebruik tien jaar of langer op deuren. Stootplekken kun je laten bijwerken."),
            ("Kunnen radiatoren gespoten worden?", "Ja, met een lak die tegen warmte kan. Zet de verwarming uit tijdens het werk en tot de lak droog is."),
            ("Is spuiten gezond voor mijn huis?", "Watergedragen lakken en goede afscherming beperken nevel en geur. Vraag welke lak er gebruikt wordt en hoe de ruimte wordt afgeschermd en geventileerd."),
        ],
        "links": ["verf-op-waterbasis-of-terpentinebasis", "grondverf-of-voorlak", "latex-of-muurverf", "trap-verven", "tegels-verven"],
    },
    "behangen": {
        "intentie": [
            ("Wat kost het?", "Reken op €9 tot €24 per m², inclusief standaard behang en 9% btw op het werk. Duur designbehang komt daar los bij."),
            ("Hoe lang duurt het?", "Een slaapkamer is vaak in een dag klaar. Moet er eerst oud behang af, reken dan op een dag extra."),
            ("Welk behang?", "Vliesbehang is het makkelijkst en het meest gebruikt. Glasvlies is er om over te schilderen."),
        ],
        "lagen": [
            ("Oud behang verwijderen", "Inweken en afsteken, of met een stoomapparaat. Lijmresten eraf wassen.", "muur laten drogen: meestal een dag"),
            ("Muur egaliseren", "Gaten en naden vullen, vlak schuren. Behang laat elke oneffenheid zien.", "vulmiddel 1 tot 24 uur"),
            ("Voorstrijken", "Een voorstrijkmiddel zorgt dat de lijm niet te snel in de muur trekt en dat het behang later weer los kan.", "meestal enkele uren tot een dag"),
            ("Behangen", "Baan voor baan lood plakken, patronen op elkaar laten aansluiten, randen strak afsnijden.", "—"),
            ("Drogen", "Tijdens het drogen niet stoken en geen tocht: anders krimpt het behang en zie je naden.", "lijm droogt meestal in 24 tot 48 uur"),
            ("Schilderen (bij glasvlies)", "Glasvlies en renovlies krijgen daarna twee lagen muurverf.", "zie binnenschilderwerk"),
        ],
        "cyclus": [
            ("Vliesbehang", "10 tot 15 jaar"),
            ("Papierbehang", "korter: gevoeliger voor stoten en vocht"),
            ("Glasvlies met muurverf", "20 jaar of meer; tussendoor alleen overschilderen"),
        ],
        "keuze": [
            ("Gewone woonkamer of slaapkamer", "Vliesbehang", "Makkelijk aan te brengen en later in één keer droog los te trekken."),
            ("Muur met haarscheurtjes", "Glasvlies of renovlies, daarna schilderen", "Overbrugt kleine scheuren en is steeds opnieuw over te schilderen."),
            ("Kinderkamer of hal", "Vinyl- of afwasbaar behang", "Beter bestand tegen vlekken en schoonmaken."),
            ("Eén statementwand", "Fotobehang of designbehang", "Groot effect op een kleine oppervlakte; laat het door een ervaren behanger plakken."),
        ],
        "faq": [
            ("Moet oud behang er altijd af?", "Bijna altijd. Nieuw behang over oud behang laat vaak los of geeft bobbels. Strippen kost extra tijd, maar voorkomt problemen."),
            ("Mag ik zelf het behang kopen?", "Dat kan. Overleg wel vooraf met de behanger welk type en hoeveel rollen. Koop rollen met hetzelfde productienummer, anders kan de kleur verschillen."),
            ("Welke btw betaal ik bij behangen?", "Het behangen zelf en de lijm vallen bij een woning ouder dan twee jaar onder 9%. Het behang zelf valt onder 21%. Een goede offerte zet die posten apart."),
            ("Kan behang in de badkamer?", "Gewoon behang niet. In vochtige ruimtes zijn glasvlies met een geschikte verf of speciaal vochtbestendig behang beter."),
            ("Waarom zie ik naden na het behangen?", "Vaak door snel drogen (verwarming hoog, tocht) of door een muur die te veel zuigt. Daarom is voorstrijken en rustig laten drogen belangrijk."),
        ],
        "links": ["behang-verwijderen", "latex-of-muurverf", "goede-offerte-schilderwerk", "schimmel-op-muur"],
    },
    "zakelijk-schilderwerk": {
        "intentie": [
            ("Wat kost het?", "Uurtarieven liggen rond €45 tot €68 exclusief btw. Grotere klussen worden meestal als aanneemsom of per m² geprijsd."),
            ("Welke btw?", "Bedrijfspanden vallen onder 21% btw. Alleen het woongedeelte van een gemengd pand kan onder 9% vallen."),
            ("Hoe plan je het?", "Buiten openingstijden, in fases of in een rustige periode. Spreek dat vooraf af, want avond- en weekendwerk kost meer."),
        ],
        "lagen": [
            ("Inspectie en plan", "De schilder inventariseert het pand en maakt een plan: wat, in welke volgorde, met welke verf.", "—"),
            ("Fasering", "Werk in delen, zodat het bedrijf door kan draaien. Afspraken over toegang, sleutels en veiligheid.", "—"),
            ("Voorbereiden", "Reinigen, schuren en repareren zoals bij woningen, maar vaak op grotere schaal en met hoogwerker of steiger.", "per ondergrond, zie binnen- en buitenschilderwerk"),
            ("Schilderen", "Verfsystemen voor zware belasting: slijtvast in gangen, afwasbaar in sanitair, geschikt voor metaal of beton.", "per verfsysteem, volgens het technische blad"),
            ("Oplevering", "Samen nalopen, restpunten afspreken en een rapport voor het onderhoudsplan.", "—"),
        ],
        "cyclus": [
            ("Gangen, trappenhuizen en entree", "om de 3 tot 6 jaar, door slijtage"),
            ("Kantoorruimtes", "om de 5 tot 8 jaar, of bij een nieuwe huurder"),
            ("Buitenschilderwerk bedrijfspand", "volgens het meerjarenonderhoudsplan, vaak om de 6 tot 8 jaar"),
            ("VvE-complexen", "volgens het meerjarenonderhoudsplan, met een jaarlijkse inspectie"),
        ],
        "keuze": [
            ("Duidelijke klus met vaste omvang", "Aanneemsom", "Je weet vooraf wat het kost."),
            ("Omvang moeilijk te schatten, bijvoorbeeld veel herstel", "Regie (per uur) met een maximum", "Je betaalt wat er echt gedaan is, met een plafond."),
            ("VvE of vastgoed met meerdere panden", "Meerjarig onderhoudscontract", "Vaste cyclus, betere planning en geen achterstallig onderhoud."),
            ("Winkel of horeca die open moet blijven", "Werk buiten openingstijden", "Geen omzetverlies, wel een toeslag op het uurtarief."),
        ],
        "faq": [
            ("Wat is een meerjarenonderhoudsplan?", "Een plan dat per jaar laat zien welk onderhoud nodig is en wat het ongeveer kost. Voor VvE's is het verplicht om voor groot onderhoud te reserveren; een plan helpt om dat bedrag te bepalen."),
            ("Kan het werk in fases?", "Ja. Bij kantoren en winkels is werken per verdieping of per ruimte gebruikelijk. Zo kan het bedrijf doordraaien."),
            ("Moet de schilder een VCA-certificaat hebben?", "Dat is niet wettelijk verplicht voor schilderwerk, maar veel bedrijven en VvE's vragen erom bij werk op hoogte of in bedrijfsomgevingen. Vraag het na als het voor jou belangrijk is."),
            ("Wie regelt de steiger of hoogwerker?", "Meestal de schilder, en die rekent het door. Laat in de offerte zetten of het erin zit, en wie de vergunning voor de stoep of straat aanvraagt."),
        ],
        "links": ["goede-offerte-schilderwerk", "verfschade-en-garantie", "hoe-vaak-buitenschilderwerk"],
    },
}


def _tabel(kop, rijen):
    th = "".join(f'<th scope="col">{k}</th>' for k in kop)
    tr = "".join("<tr>" + "".join(f'<td data-label="{k}">{c}</td>' for k, c in zip(kop, r)) + "</tr>" for r in rijen)
    return f'<div class="tablewrap"><table class="du-tabel"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'


def intentie_blok(d):
    """'In het kort' bovenaan de dienstpagina: het antwoord op de zoekvraag."""
    u = UITLEG.get(d["slug"])
    if not u:
        return ""
    li = "".join(f"<li><strong>{v}</strong> {a}</li>" for v, a in u["intentie"])
    return (f'<div class="callout du-kort"><p><strong>In het kort</strong></p><ul>{li}</ul>'
            f'<p style="font-size:.93rem;margin-top:6px"><a href="#laag-voor-laag">Zo gaat het werk</a> · '
            f'<a href="#wat-kies-je">Wat kies je?</a> · <a href="#onderhoud">Hoe vaak?</a></p></div>')


def uitleg_blok(d):
    """Het werk laag voor laag, onderhoudscyclus en 'wanneer kies je wat'."""
    u = UITLEG.get(d["slug"])
    if not u:
        return ""
    naam = d["naam"].lower()
    lagen = _tabel(("Stap", "Wat er gebeurt", "Wachten tot de volgende stap"),
                   [(f"{i + 1}. {s}", w, t) for i, (s, w, t) in enumerate(u["lagen"])])
    cyclus = _tabel(("Onderdeel", "Hoe vaak"), u["cyclus"])
    keuze = _tabel(("Jouw situatie", "Kies voor", "Waarom"), u["keuze"])
    return f"""<h2 id="laag-voor-laag">{d['naam']} laag voor laag</h2>
  <p>Wat er precies gebeurt, in de volgorde waarin het gebeurt. De wachttijden laten zien waarom {naam} vaak meer dagen kost dan je verwacht: tussen de lagen moet het drogen.</p>
  {lagen}
  <p class="pc-bron"><small>{DROOG_NOOT}</small></p>
  <h2 id="wat-kies-je">Wanneer kies je wat?</h2>
  {keuze}
  <h2 id="onderhoud">Hoe vaak is het nodig?</h2>
  <p>Richtlijnen voor normaal gebruik. Ligging, gebruik en de kwaliteit van de vorige beurt maken veel uit.</p>
  {cyclus}"""


def faq_extra(d):
    u = UITLEG.get(d["slug"])
    return list(u["faq"]) if u else []


def verdieping_blok(d):
    """Interne links naar alle kostenpagina's en kennisbankartikelen die bij deze dienst horen."""
    u = UITLEG.get(d["slug"]) or {}
    ks = [k for k in KOSTEN if k["dienst"] == d["slug"]]
    arts = [_ART[s] for s in u.get("links", []) if s in _ART]
    if not ks and not arts:
        return ""
    kos = "".join(f'<li><a href="/kosten/{k["slug"]}/">Wat kost {k["klus"]}?</a></li>' for k in ks)
    ken = "".join(f"<li>{_link(a['slug'])}</li>" for a in arts)
    kolom_k = f'<div><h3>Kosten</h3><ul>{kos}</ul><p><a href="/kosten/">Alle kosten per klus</a></p></div>' if ks else ""
    kolom_a = f'<div><h3>Uitleg in de kennisbank</h3><ul>{ken}</ul><p><a href="/kennisbank/">Naar de kennisbank</a></p></div>' if arts else ""
    return f'<h2>Kosten en verdieping</h2><div class="grid g2 du-links">{kolom_k}{kolom_a}</div>'
