# -*- coding: utf-8 -*-
"""
Contentmodel voor Topschilder.nl
Alles wat je aanpast in dit bestand rolt automatisch door de hele site.
"""

SITE = {
    "naam": "Topschilder",
    "domein": "topschilder.nl",
    "url": "https://topschilder.nl",
    "tagline": "Vergelijk schilders bij jou in de buurt",
    "email": "joukesluimer@hotmail.com",
    "telefoon": "085 - 000 00 00",
    "kvk": "97150975",
    "btw": "",  # <- vul hier je btw-id in zodra je die hebt; blijft verborgen zolang het leeg is
    "adres": "Zeewolde",
    "provincie_hq": "Flevoland",
    "review_score": "4.8",
    "review_aantal": "1.247",
    "oprichting": "2026",
}

# ---------------------------------------------------------------------------
# DIENSTEN
# ---------------------------------------------------------------------------

DIENSTEN = [
    {
        "slug": "binnenschilderwerk",
        "naam": "Binnenschilderwerk",
        "naam_kort": "Binnen schilderen",
        "kort": "Muren, plafonds, deuren, kozijnen en trappen binnenshuis",
        "icon": "roller",
        "prijs_van": 10,
        "prijs_tot": 22,
        "prijs_eenheid": "per m² wand of plafond",
        "prijs_extra": "Losse deuren rekenen schilders meestal per stuk: €65 – €140 per deur, afhankelijk van of er twee kanten en kozijnen bij zitten.",
        "meta_title": "Binnenschilderwerk kosten & schilder vinden | {plaats}",
        "intro": (
            "Binnenschilderwerk is het werk dat je elke dag ziet. Strak afgeplakte plinten, "
            "een plafond zonder rollerbanen en deuren die na tien jaar weer als nieuw ogen. "
            "Het verschil tussen een vakman en een handige buurman zit bijna nooit in de verf, "
            "maar in de voorbereiding: schuren, ontvetten, plamuren en gronden."
        ),
        "wat": [
            "Muren en plafonds sauzen met latex (mat, zijdeglans of reinigbaar)",
            "Binnendeuren en kozijnen schilderen of laten spuiten",
            "Trappen, lambrisering en vensterbanken lakken",
            "Voorbehandeling: schuren, ontvetten, plamuren, gronden en gaatjes dichten",
            "Behang verwijderen en ondergrond herstellen",
            "Nieuwbouw-afwerking op glasvlies of spuitwerk",
        ],
        "werkwijze": [
            ("Opname", "De schilder bekijkt de ruimtes, meet op en bespreekt kleuren en glansgraad. Bij veel bedrijven kan dat tegenwoordig ook via foto's en video."),
            ("Voorbereiding", "Meubels afdekken, vloeren beschermen, plinten en stopcontacten aftapen. Reken op een halve dag voor een gemiddelde woonkamer."),
            ("Ondergrond herstellen", "Schuren, ontvetten, scheuren en gaatjes plamuren en gronden. Dit bepaalt 80% van het eindresultaat."),
            ("Afwerken", "Twee lagen latex of lak. Bij sterke kleurwissels soms drie."),
            ("Oplevering", "Samen rondlopen, restpuntjes bijwerken en afdekmateriaal weghalen."),
        ],
        "prijsfactoren": [
            "Aantal vierkante meters en de hoogte van de ruimte (boven 2,60 m komt er steigerwerk bij)",
            "Staat van de ondergrond: kaal stucwerk kost meer voorbereiding dan al eerder geschilderde muren",
            "Kleurwissel van donker naar licht vraagt vaak een extra laag",
            "Latex of lak, en welke glansgraad",
            "Of meubels en vloeren moeten worden afgedekt of dat de ruimte leeg is",
        ],
        "tips": [
            "Laat de ruimte leeghalen als het kan. Een lege kamer scheelt zo makkelijk een dagdeel arbeid.",
            "Vraag altijd op welke verfmerk en glansgraad de offerte is gebaseerd. Verschil tussen A-merk en huismerk kan honderden euro's schelen.",
            "Plan binnenschilderwerk in de winter. Schilders hebben dan minder buitenwerk en zijn scherper geprijsd.",
        ],
        "faq": [
            ("Hoelang duurt binnenschilderwerk?", "Een gemiddelde woonkamer van 30 m² kost een schilder ongeveer twee tot drie dagen inclusief voorbereiding. Een hele benedenverdieping ligt eerder rond een week."),
            ("Kan ik in huis blijven wonen tijdens het schilderen?", "Meestal wel. Moderne watergedragen latex is vrijwel reukloos en droogt binnen enkele uren. Bij spuitwerk of oplosmiddelhoudende lak is het prettiger om de ruimte een dag te mijden."),
            ("Moet ik zelf verf kopen?", "Dat mag, maar het is zelden goedkoper. Schilders kopen met korting in en zijn alleen verantwoordelijk voor het eindresultaat als zij de verf leveren."),
            ("Geldt het lage btw-tarief van 9%?", "Ja, bij woningen die ouder zijn dan twee jaar, voor het werk én de gebruikte materialen."),
        ],
    },
    {
        "slug": "buitenschilderwerk",
        "naam": "Buitenschilderwerk",
        "naam_kort": "Buiten schilderen",
        "kort": "Kozijnen, gevels, boeidelen, dakkapellen en houtwerk buiten",
        "icon": "house",
        "prijs_van": 90,
        "prijs_tot": 190,
        "prijs_eenheid": "per kozijn",
        "prijs_extra": "Een complete tussenwoning zit doorgaans tussen €2.200 en €5.500. Een vrijstaande woning met veel houtwerk loopt op tot €9.000 of meer.",
        "meta_title": "Buitenschilderwerk kosten & schilder vinden | {plaats}",
        "intro": (
            "Buitenschilderwerk is geen cosmetica maar onderhoud. De verflaag houdt water uit je "
            "houtwerk. Zodra die laag scheurt, kruipt vocht erin en begint houtrot — en dan praat "
            "je niet meer over verf maar over timmerwerk. Het loont dus om op tijd te schilderen "
            "in plaats van te wachten tot het echt lelijk is."
        ),
        "wat": [
            "Kozijnen, ramen en buitendeuren schilderen",
            "Boeidelen, windveren, dakranden en dakkapellen",
            "Houten gevelbekleding, schuren en garagedeuren",
            "Gevels sausen met minerale of siliconenharsverf",
            "Kleine houtrotreparaties meenemen in dezelfde beurt",
            "Kitwerk en beglazingsranden vernieuwen",
        ],
        "werkwijze": [
            ("Inspectie", "De schilder loopt langs alle gevels, prikt in verdachte plekken en noteert waar hout aangetast is. Dit bepaalt het grootste deel van de prijs."),
            ("Reinigen", "Vuil, algen en loszittende verf eraf. Meestal met een borstel en een reiniger, soms met lage druk."),
            ("Herstel", "Houtrot uitfrezen en vullen, kitnaden vernieuwen, kale plekken gronden."),
            ("Schilderen", "Grondlaag plus twee dekkende lagen bij kaal hout, twee lagen bij goed onderhouden werk."),
            ("Nazorg", "Foto's van de uitgevoerde reparaties en een advies wanneer de volgende beurt logisch is."),
        ],
        "prijsfactoren": [
            "Aantal kozijnen, ramen en deuren en of ze aan twee zijden geschilderd worden",
            "Hoeveel houtrot er tijdens de inspectie boven water komt",
            "Bereikbaarheid: ladderwerk is goedkoper dan een steiger of hoogwerker",
            "Hoelang geleden de vorige beurt was — kaal hout kost een extra laag",
            "Het seizoen: maart tot oktober is hoogseizoen en daarmee duurder",
        ],
        "tips": [
            "Vraag de offerte inclusief een stelpost voor houtrot. Anders krijg je halverwege het werk alsnog een meerprijs.",
            "Laat schilderwerk uitvoeren in het naseizoen. September en oktober zijn vaak scherper geprijsd dan mei.",
            "Een onderhoudscontract voor de vijf jaar erna kan interessant zijn: kleinere beurten, langere levensduur van je kozijnen.",
        ],
        "faq": [
            ("Hoe vaak moet buitenschilderwerk gebeuren?", "Voor houten kozijnen is vier tot zes jaar gebruikelijk. Zuid- en westgevels krijgen de meeste zon en regen en zijn meestal als eerste aan de beurt."),
            ("Kan er in de winter buiten geschilderd worden?", "Beperkt. De meeste verven vragen minimaal 5 tot 8 graden en een droge ondergrond. Tussen november en maart plannen schilders daarom vooral binnenwerk."),
            ("Wat kost een steiger?", "Reken op €300 tot €900 voor een gemiddelde woning, afhankelijk van hoogte en huurduur. Vraag of dit in de offerte zit of apart wordt gerekend."),
            ("Geldt 9% btw ook buiten?", "Ja. Voor woningen ouder dan twee jaar geldt het 9%-tarief op schilderwerk binnen én buiten, inclusief de gebruikte materialen."),
        ],
    },
    {
        "slug": "houtrot-reparatie",
        "naam": "Houtrot reparatie",
        "naam_kort": "Houtrot",
        "kort": "Aangetast hout uitfrezen, vullen of vervangen",
        "icon": "wood",
        "prijs_van": 85,
        "prijs_tot": 275,
        "prijs_eenheid": "per reparatieplek",
        "prijs_extra": "Een heel kozijnhoekstuk vervangen ligt hoger: reken op €250 tot €600 per hoek inclusief schilderwerk.",
        "meta_title": "Houtrot reparatie kosten & vakman vinden | {plaats}",
        "intro": (
            "Houtrot begint bijna altijd op dezelfde plek: de onderdorpel van een raam of de "
            "onderhoek van een kozijn, waar water blijft staan. Als je er vroeg bij bent kost het "
            "een paar tientjes per plek. Wacht je te lang, dan vervang je het hele kozijn en zit je "
            "al snel op duizenden euro's."
        ),
        "wat": [
            "Aangetast hout uitfrezen en vullen met epoxy of houtreparatiemortel",
            "Onderdorpels en kozijnhoeken vervangen",
            "Nieuwe hoekstukken inlijmen (aanhelen)",
            "Complete kozijnvervanging bij ernstige aantasting",
            "Preventief behandelen van risicoplekken",
            "Kitwerk en waterslagen vernieuwen om herhaling te voorkomen",
        ],
        "werkwijze": [
            ("Prikonderzoek", "Met een priem in het hout prikken om te bepalen hoe diep de aantasting zit. Zacht hout dat meegeeft is aangetast."),
            ("Uitfrezen", "Al het zachte hout weg tot op gezond materiaal. Half werk hier betekent binnen twee jaar hetzelfde probleem."),
            ("Impregneren", "De uitgefreesde ruimte wordt behandeld met een houtverharder zodat de vulling goed hecht."),
            ("Vullen of aanhelen", "Kleine plekken worden gevuld met epoxy. Grotere stukken worden weggezaagd en vervangen door nieuw hout."),
            ("Afwerken", "Schuren, gronden en in de kleur van het bestaande kozijn afschilderen."),
        ],
        "prijsfactoren": [
            "Aantal aangetaste plekken en hoe diep de aantasting zit",
            "Vullen met epoxy is goedkoper dan een stuk hout vervangen",
            "Bereikbaarheid — een dakkapel op de tweede verdieping vraagt een steiger",
            "Of het schilderwerk erna in dezelfde beurt meegenomen wordt",
            "Of het glas eruit moet om bij de dorpel te komen",
        ],
        "tips": [
            "Loop elk voorjaar één keer met een schroevendraaier langs je kozijnen. Overal waar het hout meegeeft, is werk aan de winkel.",
            "Laat houtrotherstel altijd combineren met de schildersbeurt. Apart inplannen kost je twee keer voorrijkosten.",
            "Vraag om foto's van de uitgefreesde plek vóór het vullen. Zo weet je zeker dat er niet over rot heen geplamuurd is.",
        ],
        "faq": [
            ("Kan houtrot terugkomen na reparatie?", "Als al het zachte hout is verwijderd en de plek goed is afgeschilderd, niet. Komt het binnen twee jaar terug, dan is er destijds te weinig weggehaald of blijft er ergens water staan."),
            ("Is vullen net zo sterk als vervangen?", "Voor plekken tot ongeveer een handpalm groot is epoxyvulling prima en zelfs harder dan het originele hout. Bij grotere aantasting is aanhelen met nieuw hout de betere keuze."),
            ("Moet ik het hele kozijn vervangen?", "Zelden. Meestal is alleen de onderdorpel of een hoek aangetast en kan de rest blijven zitten. Laat je niet te snel een compleet nieuw kozijn aanpraten."),
            ("Dekt mijn verzekering houtrot?", "Nee. Houtrot valt onder achterstallig onderhoud en wordt door opstalverzekeringen uitgesloten."),
        ],
    },
    {
        "slug": "spuitwerk",
        "naam": "Spuitwerk",
        "naam_kort": "Spuiten",
        "kort": "Deuren, kozijnen, keukenkastjes en meubels strak spuiten",
        "icon": "spray",
        "prijs_van": 95,
        "prijs_tot": 185,
        "prijs_eenheid": "per deur",
        "prijs_extra": "Een complete keuken laten spuiten ligt meestal tussen €900 en €2.500, afhankelijk van het aantal fronten en of het in de werkplaats of op locatie gebeurt.",
        "meta_title": "Spuitwerk kosten: deuren, kozijnen en keuken | {plaats}",
        "intro": (
            "Spuitwerk geeft een egaal, fabrieksachtig resultaat dat je met een kwast of roller "
            "niet haalt. Geen kwaststrepen, geen rollerstructuur. Het verschil zit vooral in de "
            "voorbereiding: alles moet perfect glad en stofvrij zijn, want de spuitlaag verbergt "
            "niets."
        ),
        "wat": [
            "Binnendeuren en kozijnen in de werkplaats of op locatie spuiten",
            "Keukenfronten en kastdeurtjes een nieuwe kleur geven",
            "Trappen en lambrisering strak afwerken",
            "Meubels en radiatoren spuiten",
            "Nieuwbouw-kozijnen afwerken vóór plaatsing",
            "Structuurspuitwerk op plafonds",
        ],
        "werkwijze": [
            ("Demonteren", "Deuren uit de sponningen, beslag eraf, keukenfronten losschroeven. Alles wat niet gespoten wordt gaat eraf."),
            ("Schuren en ontvetten", "Machinaal schuren tot een egale, matte ondergrond en daarna volledig ontvetten. Vet is de nummer één oorzaak van mislukt spuitwerk."),
            ("Gronden", "Een spuitgrond die de kleur van de ondergrond wegneemt en de hechting verzorgt."),
            ("Spuiten", "Twee tot drie dunne lagen met tussentijds schuren. In een stofvrije ruimte of afgeschermde cabine."),
            ("Monteren", "Uitharden, beslag terug en alles weer op zijn plek."),
        ],
        "prijsfactoren": [
            "Op locatie spuiten of meenemen naar de werkplaats (werkplaats geeft een beter resultaat)",
            "Aantal deuren of fronten — hoe meer stuks, hoe lager de prijs per stuk",
            "Of er ook kozijnen en beslag bij horen",
            "De huidige staat: beschadigd of geverfd werk vraagt meer voorbereiding",
            "Hoogglans is duurder dan zijdeglans, want elke oneffenheid wordt zichtbaar",
        ],
        "tips": [
            "Laat deuren meenemen naar de werkplaats als je kunt. Het resultaat is aantoonbaar strakker en je hebt geen spuitnevel in huis.",
            "Bestel meteen nieuw beslag. Oud beslag terugzetten op vers spuitwerk is zonde van het effect.",
            "Vraag om een proefstukje in jouw kleur voordat de hele keuken de deur uitgaat.",
        ],
        "faq": [
            ("Is spuitwerk duurder dan kwasten?", "Per deur ongeveer 20 tot 40% duurder, maar het resultaat is aanzienlijk strakker en gaat langer mee. Bij grotere aantallen loopt het prijsverschil snel terug."),
            ("Hoelang kan ik mijn deuren niet gebruiken?", "Bij werkplaatsspuitwerk zijn deuren doorgaans na drie tot vijf werkdagen terug. De lak is dan hanteerbaar maar pas na enkele weken volledig uitgehard."),
            ("Kan mijn keuken echt gespoten worden?", "Vrijwel alle keukenfronten kunnen: gelakt hout, MDF, folie en zelfs kunststof. Alleen bij losliggende of opbollende folie is vervangen verstandiger."),
            ("Zit er spuitnevel in mijn huis?", "Bij professioneel werk met goede afscherming en afzuiging niet. Vraag altijd hoe de ruimte wordt afgeschermd voordat er op locatie gespoten wordt."),
        ],
    },
    {
        "slug": "behangen",
        "naam": "Behangen",
        "naam_kort": "Behangen",
        "kort": "Glasvezel, vliesbehang, fotobehang en wandbekleding",
        "icon": "wall",
        "prijs_van": 9,
        "prijs_tot": 24,
        "prijs_eenheid": "per m² inclusief behang",
        "prijs_extra": "Alleen het aanbrengen (jij levert het behang) ligt rond €7 tot €14 per m². Oud behang verwijderen kost €4 tot €9 per m² extra.",
        "meta_title": "Behanger kosten per m² | {plaats}",
        "intro": (
            "Behang is terug van weggeweest, en niet alleen als bloemetjesmuur bij oma. Glasvezel "
            "op scheurgevoelige muren, een strakke vliesbehang als basis voor latex, of één "
            "statement-wand met fotobehang. Het lastige zit hem in de naden en de hoeken — daar "
            "zie je meteen of iemand het vak beheerst."
        ),
        "wat": [
            "Vliesbehang en papierbehang aanbrengen",
            "Glasvezelbehang (renovlies) op scheurgevoelige muren",
            "Fotobehang en behang met patroon dat moet aansluiten",
            "Oud behang verwijderen en de ondergrond herstellen",
            "Voorstrijken en muren egaliseren",
            "Overschilderen van glasvezel of renovlies met latex",
        ],
        "werkwijze": [
            ("Muur beoordelen", "Zit er oud behang op, is de muur zuigend of glad, zijn er scheuren? Dit bepaalt de voorbereiding."),
            ("Strippen", "Oud behang eraf weken en schrapen, lijmresten verwijderen."),
            ("Egaliseren", "Gaten en scheuren vullen, ruwe plekken schuren en de muur voorstrijken."),
            ("Behangen", "Baan voor baan, met de patronen strak aansluitend en de naden onzichtbaar gedrukt."),
            ("Afwerken", "Bij glasvezel of renovlies volgen daarna nog twee lagen latex."),
        ],
        "prijsfactoren": [
            "Type behang: vliesbehang gaat sneller dan papierbehang dat moet weken",
            "Wel of geen patroon dat moet aansluiten (rapport) — dat kost extra materiaal en tijd",
            "Staat van de muur en of er oud behang af moet",
            "Hoogte van de ruimte en het aantal hoeken, ramen en deuren",
            "Of het behang door jou of door de behanger wordt geleverd",
        ],
        "tips": [
            "Koop altijd één rol extra en uit dezelfde partij. Nabestellen geeft vaak net een andere kleurbatch.",
            "Glasvezel op scheurgevoelige muren is duurder in aanschaf maar je hebt er twintig jaar geen omkijken naar.",
            "Bij patroonbehang: vraag hoeveel snijverlies er wordt gerekend. Bij een groot rapport kan dat 20% van je materiaal zijn.",
        ],
        "faq": [
            ("Kan behang over behang?", "Technisch soms, maar het is geen goed idee. De oude lijm laat los en je krijgt bobbels. Strippen is bijna altijd de betere keuze."),
            ("Hoelang gaat behang mee?", "Vliesbehang tien tot vijftien jaar, glasvezel met latex erover twintig jaar of meer omdat je het simpelweg kunt overschilderen."),
            ("Kan ik behang schilderen?", "Glasvezel en renovlies zijn er speciaal voor gemaakt. Regulier decoratief behang kan meestal ook, maar het patroon blijft door de verf schemeren."),
            ("Hoeveel rollen heb ik nodig?", "Vuistregel: omtrek van de kamer in meters gedeeld door 0,53 (rolbreedte), keer het aantal banen per rol. Een behanger rekent dit bij de opname exact uit."),
        ],
    },
    {
        "slug": "zakelijk-schilderwerk",
        "naam": "Zakelijk schilderwerk",
        "naam_kort": "Zakelijk",
        "kort": "Kantoren, VvE's, winkels, scholen en bedrijfspanden",
        "icon": "office",
        "prijs_van": 45,
        "prijs_tot": 68,
        "prijs_eenheid": "per uur excl. btw",
        "prijs_extra": "Grotere projecten gaan vrijwel altijd op aanneemsom in plaats van regie. Voor VvE-onderhoud wordt meestal een meerjarenplan gemaakt.",
        "meta_title": "Zakelijk schilderwerk & VvE onderhoud | {plaats}",
        "intro": (
            "Bij zakelijk schilderwerk telt niet alleen de prijs per meter. Kan er 's avonds of in "
            "het weekend gewerkt worden? Blijft de winkel open? Hoe zit het met VCA en aansprakelijkheid? "
            "Dat zijn de vragen waarop een goede offerte antwoord geeft, en waarop wij schilders "
            "voorselecteren."
        ),
        "wat": [
            "Kantoren en bedrijfsruimtes binnen en buiten",
            "VvE-onderhoud en meerjarenonderhoudsplannen (MJOP)",
            "Winkels en horeca, met werkzaamheden buiten openingstijden",
            "Scholen en zorginstellingen met werk in de vakantieperiode",
            "Trappenhuizen en gemeenschappelijke ruimtes",
            "Industriële coatings en vloermarkeringen",
        ],
        "werkwijze": [
            ("Intake", "Een adviseur bekijkt het pand, bespreekt de planning en inventariseert wat er tijdens werktijd wel en niet kan."),
            ("Offerte", "Een gespecificeerde aanneemsom met een duidelijke afbakening van meer- en minderwerk."),
            ("Planning", "Fasering per verdieping of vleugel, zodat het bedrijf door kan draaien."),
            ("Uitvoering", "Vaste contactpersoon, dagrapportage en werk buiten kantooruren waar nodig."),
            ("Nazorg", "Oplevering met restpuntenlijst, garantie op papier en een advies voor het onderhoudsplan."),
        ],
        "prijsfactoren": [
            "Omvang van het project en de fasering",
            "Of er buiten kantoortijden of in het weekend gewerkt moet worden",
            "Eisen rond VCA, RI&E en werken op hoogte",
            "Steiger-, hoogwerker- of gevelliftkosten",
            "Contractvorm: eenmalig, meerjarig onderhoud of op afroep",
        ],
        "tips": [
            "Vraag drie offertes op basis van hetzelfde bestek. Anders vergelijk je appels met peren.",
            "Voor VvE's: laat het schilderwerk aansluiten op het MJOP zodat de reservering en de uitvoering in hetzelfde jaar vallen.",
            "Leg vast wie aansprakelijk is bij schade aan inventaris en vraag om een kopie van de aansprakelijkheidsverzekering.",
        ],
        "faq": [
            ("Kan er buiten kantooruren gewerkt worden?", "Ja, veel schildersbedrijven werken 's avonds of in het weekend bij zakelijke opdrachten. Reken op een toeslag van 25 tot 50% op het uurtarief."),
            ("Geldt het lage btw-tarief ook zakelijk?", "Nee. Het 9%-tarief geldt alleen voor woningen ouder dan twee jaar. Bedrijfsruimtes vallen onder 21%. Is een pand deels woning, dan geldt 9% alleen voor het woongedeelte."),
            ("Hoe werkt dit voor een VvE?", "Meestal via een meerjarenonderhoudsplan. De schilder maakt een inspectierapport en een fasering over meerdere jaren, waarna de vergadering het budget vaststelt."),
            ("Wat is een aanneemsom?", "Een vaste totaalprijs voor het hele werk, in plaats van afrekenen per gewerkt uur. Voor grotere projecten geeft dat jou zekerheid over het budget."),
        ],
    },
]

DIENST_BY_SLUG = {d["slug"]: d for d in DIENSTEN}

# ---------------------------------------------------------------------------
# PLAATSEN — Flevoland als thuisbasis, daarna de grensregio
# ---------------------------------------------------------------------------

PLAATSEN = [
    # --- Flevoland (kernmarkt) ---
    dict(slug="zeewolde", naam="Zeewolde", provincie="Flevoland", gemeente="Zeewolde",
         inwoners=23000, prio=1,
         hook="Zeewolde is gebouwd vanaf 1984, waardoor veel woningen nu precies in de fase zitten waarin het oorspronkelijke houtwerk aan een grondige beurt toe is."),
    dict(slug="almere", naam="Almere", provincie="Flevoland", gemeente="Almere",
         inwoners=225000, prio=1,
         hook="Almere heeft een enorme voorraad woningen uit de jaren tachtig en negentig én veel recente nieuwbouw. Van houtrot in Almere Haven tot afwerking van nieuwbouw in Almere Poort — de vraag loopt sterk uiteen per stadsdeel."),
    dict(slug="lelystad", naam="Lelystad", provincie="Flevoland", gemeente="Lelystad",
         inwoners=82000, prio=1,
         hook="De wind over het IJsselmeer maakt Lelystad zwaar voor buitenschilderwerk. Vooral west- en zuidgevels vragen hier eerder onderhoud dan het landelijk gemiddelde."),
    dict(slug="dronten", naam="Dronten", provincie="Flevoland", gemeente="Dronten",
         inwoners=28000, prio=1,
         hook="Dronten combineert ruime jaren-zestig woningen met nieuwe wijken. Veel woningen hebben grote raampartijen, wat het aantal te schilderen kozijnen flink opdrijft."),
    dict(slug="biddinghuizen", naam="Biddinghuizen", provincie="Flevoland", gemeente="Dronten",
         inwoners=6500, prio=2,
         hook="In Biddinghuizen staan relatief veel vrijstaande woningen en boerderijen met veel houtwerk, waardoor buitenschilderwerk hier vaak een meerdaags project is."),
    dict(slug="swifterbant", naam="Swifterbant", provincie="Flevoland", gemeente="Dronten",
         inwoners=6800, prio=2,
         hook="Swifterbant is grotendeels gebouwd in de jaren zeventig. Het originele houtwerk uit die periode is inmiddels toe aan zijn zoveelste onderhoudsbeurt."),
    dict(slug="emmeloord", naam="Emmeloord", provincie="Flevoland", gemeente="Noordoostpolder",
         inwoners=26000, prio=1,
         hook="Als hoofdplaats van de Noordoostpolder heeft Emmeloord een gevarieerde woningvoorraad, van naoorlogse polderwoningen tot recente nieuwbouw aan de randen."),
    dict(slug="urk", naam="Urk", provincie="Flevoland", gemeente="Urk",
         inwoners=21500, prio=2,
         hook="Op Urk krijgt buitenschilderwerk het zwaar: zout, wind en volle zon vanaf het IJsselmeer. Een verflaag houdt het hier merkbaar korter uit dan landinwaarts."),
    dict(slug="marknesse", naam="Marknesse", provincie="Flevoland", gemeente="Noordoostpolder",
         inwoners=4200, prio=3,
         hook="Marknesse bestaat vooral uit ruime polderwoningen met flinke tuinen, waar buitenschilderwerk zonder steigerproblemen kan worden uitgevoerd."),
    dict(slug="nagele", naam="Nagele", provincie="Flevoland", gemeente="Noordoostpolder",
         inwoners=1900, prio=3,
         hook="Nagele is als modernistisch dorp ontworpen met veel platte daken en houten geveldelen — een type gevel dat om regelmatig onderhoud vraagt."),
    dict(slug="ens", naam="Ens", provincie="Flevoland", gemeente="Noordoostpolder",
         inwoners=3200, prio=3,
         hook="Ens ligt centraal in de Noordoostpolder, waardoor schilders uit Emmeloord en Kampen hier allebei zonder veel voorrijkosten kunnen komen."),
    dict(slug="kraggenburg", naam="Kraggenburg", provincie="Flevoland", gemeente="Noordoostpolder",
         inwoners=1500, prio=3,
         hook="Kraggenburg is klein, waardoor schilders hier het liefst meerdere klussen in dezelfde week plannen. Timing kan je dus geld schelen."),
    dict(slug="luttelgeest", naam="Luttelgeest", provincie="Flevoland", gemeente="Noordoostpolder",
         inwoners=1900, prio=3,
         hook="In Luttelgeest staan naast woningen ook veel bedrijfsgebouwen en kassen, waardoor lokale schilders vaak zowel particulier als zakelijk werk doen."),
    dict(slug="tollebeek", naam="Tollebeek", provincie="Flevoland", gemeente="Noordoostpolder",
         inwoners=2100, prio=3,
         hook="Tollebeek ligt dicht bij Urk en het IJsselmeer, wat betekent dat gevels op het westen hier extra te verduren krijgen."),
    dict(slug="bant", naam="Bant", provincie="Flevoland", gemeente="Noordoostpolder",
         inwoners=1400, prio=3,
         hook="Bant is een compact polderdorp waar de meeste woningen uit dezelfde bouwperiode stammen — buren hebben er dus vaak tegelijk hetzelfde onderhoud nodig."),
    dict(slug="creil", naam="Creil", provincie="Flevoland", gemeente="Noordoostpolder",
         inwoners=1400, prio=3,
         hook="Creil ligt aan de noordrand van de polder. Schilders combineren werk hier graag met opdrachten in Rutten en Espel."),
    dict(slug="rutten", naam="Rutten", provincie="Flevoland", gemeente="Noordoostpolder",
         inwoners=800, prio=3,
         hook="Rutten is een van de kleinste polderdorpen. Vraag bij offertes gericht naar voorrijkosten — die kunnen hier het verschil maken."),
    dict(slug="espel", naam="Espel", provincie="Flevoland", gemeente="Noordoostpolder",
         inwoners=800, prio=3,
         hook="In Espel zijn veel woningen aan het originele buitenschilderwerk toe, en zijn agrarische bijgebouwen vaak onderdeel van dezelfde opdracht."),

    # --- Randmeren / Veluwe ---
    dict(slug="harderwijk", naam="Harderwijk", provincie="Gelderland", gemeente="Harderwijk",
         inwoners=49000, prio=1,
         hook="De binnenstad van Harderwijk zit vol monumentale panden waar schilderwerk aan vergunningseisen en kleurenschema's gebonden is — vraag om een schilder met ervaring in beschermd stadsgezicht."),
    dict(slug="ermelo", naam="Ermelo", provincie="Gelderland", gemeente="Ermelo",
         inwoners=27000, prio=2,
         hook="Ermelo ligt tegen de bossen aan, wat algen- en groenaanslag op noordgevels een terugkerend thema maakt bij buitenschilderwerk."),
    dict(slug="putten", naam="Putten", provincie="Gelderland", gemeente="Putten",
         inwoners=25000, prio=2,
         hook="Putten heeft relatief veel vrijstaande woningen met rieten daken en houten geveldelen — vakwerk waar niet elke schilder ervaring mee heeft."),
    dict(slug="nijkerk", naam="Nijkerk", provincie="Gelderland", gemeente="Nijkerk",
         inwoners=45000, prio=2,
         hook="Nijkerk groeide de laatste jaren hard met nieuwbouw in Doornsteeg, terwijl de oude kern juist veel klassiek onderhoudswerk kent."),
    dict(slug="nunspeet", naam="Nunspeet", provincie="Gelderland", gemeente="Nunspeet",
         inwoners=28000, prio=3,
         hook="In Nunspeet zorgt de combinatie van bos en zandgrond voor veel groenaanslag op gevels, waardoor reinigen vaak een aparte post in de offerte is."),
    dict(slug="elburg", naam="Elburg", provincie="Gelderland", gemeente="Elburg",
         inwoners=23000, prio=3,
         hook="De vestingstad Elburg kent strikte regels voor kleurgebruik in het beschermde stadsgezicht. Laat je schilder dit vooraf checken bij de gemeente."),

    # --- Overijssel / IJsseldelta ---
    dict(slug="kampen", naam="Kampen", provincie="Overijssel", gemeente="Kampen",
         inwoners=54000, prio=2,
         hook="Kampen heeft een historische binnenstad met veel monumenten naast de nieuwbouw van Het Onderdijks — twee totaal verschillende soorten schilderwerk in één stad."),
    dict(slug="zwolle", naam="Zwolle", provincie="Overijssel", gemeente="Zwolle",
         inwoners=132000, prio=1,
         hook="Zwolle is groot genoeg voor gespecialiseerde schilders: van monumentaal werk in de binnenstad tot grootschalig VvE-onderhoud in Stadshagen."),
    dict(slug="genemuiden", naam="Genemuiden", provincie="Overijssel", gemeente="Zwartewaterland",
         inwoners=10500, prio=3,
         hook="Genemuiden ligt aan het Zwarte Water, waar wind en vocht het buitenschilderwerk sneller aantasten dan gemiddeld."),

    # --- Utrecht / Gooi ---
    dict(slug="bunschoten-spakenburg", naam="Bunschoten-Spakenburg", provincie="Utrecht", gemeente="Bunschoten",
         inwoners=22000, prio=3,
         hook="Aan de Eemmeerkant krijgt houtwerk hier flink wind en vocht te verduren, terwijl de oude kern juist karakteristiek schilderwerk vraagt."),
    dict(slug="amersfoort", naam="Amersfoort", provincie="Utrecht", gemeente="Amersfoort",
         inwoners=161000, prio=1,
         hook="Amersfoort loopt van middeleeuwse binnenstad tot de nieuwbouw van Vathorst. Prijzen liggen hier merkbaar hoger dan in Flevoland, dus vergelijken loont extra."),
    dict(slug="huizen", naam="Huizen", provincie="Noord-Holland", gemeente="Huizen",
         inwoners=42000, prio=2,
         hook="Huizen ligt direct aan het Gooimeer. Zoutlucht en wind zorgen ervoor dat buitenschilderwerk hier gemiddeld een jaar eerder terugkomt."),
    dict(slug="blaricum", naam="Blaricum", provincie="Noord-Holland", gemeente="Blaricum",
         inwoners=12000, prio=3,
         hook="In Blaricum staan veel karakteristieke villa's met rieten daken en houten gevels — luxe werk waarbij afwerking zwaarder weegt dan prijs."),
    dict(slug="naarden", naam="Naarden", provincie="Noord-Holland", gemeente="Gooise Meren",
         inwoners=17500, prio=3,
         hook="Binnen de vesting van Naarden gelden aparte regels voor monumenten. Buiten de vesting is het vooral regulier woningonderhoud."),
    dict(slug="bussum", naam="Bussum", provincie="Noord-Holland", gemeente="Gooise Meren",
         inwoners=33000, prio=2,
         hook="Bussum heeft veel jaren-dertig woningen met karakteristieke roedeverdeling in de ramen — arbeidsintensief schilderwerk waar ervaring echt telt."),
    dict(slug="hilversum", naam="Hilversum", provincie="Noord-Holland", gemeente="Hilversum",
         inwoners=93000, prio=1,
         hook="Hilversum staat vol Dudok-architectuur en jaren-dertig woningen. Veel stalen kozijnen, wat om een andere aanpak vraagt dan hout."),
    dict(slug="weesp", naam="Weesp", provincie="Noord-Holland", gemeente="Amsterdam",
         inwoners=19500, prio=3,
         hook="Weesp combineert een historische kern met nieuwbouw in Weespersluis, waardoor zowel monumentaal als modern schilderwerk gevraagd wordt."),
]

PLAATS_BY_SLUG = {p["slug"]: p for p in PLAATSEN}


def buurplaatsen(plaats, n=6):
    """Simpele nabijheid: zelfde gemeente eerst, dan zelfde provincie, dan de rest."""
    others = [p for p in PLAATSEN if p["slug"] != plaats["slug"]]

    def score(p):
        s = 0
        if p["gemeente"] == plaats["gemeente"]:
            s -= 100
        if p["provincie"] == plaats["provincie"]:
            s -= 40
        s -= p["inwoners"] / 50000.0
        return s

    others.sort(key=score)
    return others[:n]


# ---------------------------------------------------------------------------
# PRIJSINDEX PER PROVINCIE
# Schildersprijzen verschillen echt per regio. Deze index maakt de richtprijzen
# op elke plaatspagina kloppend én uniek. Bijstellen mag zodra je echte
# offertedata uit je eigen leads hebt.
# ---------------------------------------------------------------------------

PRIJSINDEX = {
    "Flevoland": 0.96,
    "Overijssel": 0.95,
    "Gelderland": 1.00,
    "Utrecht": 1.09,
    "Noord-Holland": 1.13,
}

INDEX_TOELICHTING = {
    "Flevoland": "Flevoland zit onder het landelijk gemiddelde. Ruime bouw, goede bereikbaarheid en weinig binnensteden met parkeergedoe houden de arbeidskosten hier laag.",
    "Overijssel": "Overijssel is een van de goedkopere regio's voor schilderwerk. Er zijn relatief veel eenmanszaken actief, wat de prijzen drukt.",
    "Gelderland": "Gelderland zit vrijwel op het landelijk gemiddelde. Alleen in de historische kernen loopt het op door lastiger bereikbaarheid.",
    "Utrecht": "In Utrecht liggen de tarieven ongeveer een tiende boven het landelijk gemiddelde. Hogere bedrijfskosten en een drukkere agenda bij schilders spelen daarin mee.",
    "Noord-Holland": "Noord-Holland is de duurste regio van dit werkgebied. Reken op ruim tien procent boven het landelijk gemiddelde, vooral door hogere loon- en huisvestingskosten.",
}


def lokale_prijs(dienst, plaats):
    """Richtprijs van een dienst, gecorrigeerd voor de regio."""
    i = PRIJSINDEX.get(plaats["provincie"], 1.0)
    van = int(round(dienst["prijs_van"] * i))
    tot = int(round(dienst["prijs_tot"] * i))
    return van, tot


# ---------------------------------------------------------------------------
# WONINGVOORRAAD PER PLAATS
# bouwperiode = wanneer het gros van de woningen is neergezet
# woningmix   = het overheersende woningtype
# ligging     = wat de omgeving doet met het buitenschilderwerk
# ---------------------------------------------------------------------------

WONINGEN = {
    "zeewolde":      ("vanaf 1984", "ruime eengezinswoningen met veel eigen grond", "open polderlandschap met veel westenwind"),
    "almere":        ("jaren tachtig en negentig, plus recente nieuwbouw", "een mix van rijwoningen, twee-onder-een-kappers en appartementen", "vlak en winderig, met veel water in de wijken"),
    "lelystad":      ("jaren zeventig en tachtig", "eengezinswoningen met flinke raampartijen", "open ligging aan het IJsselmeer met stevige wind op west- en zuidgevels"),
    "dronten":       ("jaren zestig en zeventig, met nieuwbouw aan de randen", "ruime woningen met grote raampartijen", "polderligging met weinig beschutting"),
    "biddinghuizen": ("jaren zestig en zeventig", "veel vrijstaande woningen en voormalige boerderijen", "open agrarisch gebied"),
    "swifterbant":   ("jaren zeventig", "eengezinswoningen met houten geveldelen", "vlak polderland"),
    "emmeloord":     ("naoorlogse polderbouw tot recente nieuwbouw", "een brede mix van rij-, hoek- en vrijstaande woningen", "centraal in de polder, matig beschut"),
    "urk":           ("gemengd, van historische kern tot nieuwbouwwijken", "compacte woningen in de kern en ruimere woningen aan de rand", "direct aan het IJsselmeer met zout, wind en volle zon"),
    "marknesse":     ("jaren vijftig en zestig", "ruime polderwoningen met grote tuinen", "open polder"),
    "nagele":        ("jaren vijftig, modernistisch ontworpen", "woningen met platte daken en houten geveldelen", "open polder zonder beschutting"),
    "ens":           ("jaren vijftig en zestig", "polderwoningen met eenvoudige gevels", "midden in de Noordoostpolder"),
    "kraggenburg":   ("jaren vijftig", "kleinschalige polderwoningen", "landelijk en open"),
    "luttelgeest":   ("jaren vijftig en zestig", "woningen naast veel agrarische bebouwing", "open gebied met veel kassen"),
    "tollebeek":     ("jaren vijftig en zestig", "compacte polderwoningen", "vlak bij het IJsselmeer, veel wind op de westzijde"),
    "bant":          ("jaren vijftig", "woningen uit één bouwstroom", "open polder"),
    "creil":         ("jaren vijftig", "polderwoningen aan de noordrand", "open, met wind vanaf het IJsselmeer"),
    "rutten":        ("jaren vijftig", "kleinschalige woningen", "landelijk en open"),
    "espel":         ("jaren vijftig", "woningen met vaak agrarische bijgebouwen", "open polder"),
    "harderwijk":    ("historische kern plus naoorlogse uitbreidingen", "monumentale panden in het centrum en rijwoningen daarbuiten", "aan de rand van het Wolderwijd, met wind vanaf het water"),
    "ermelo":        ("jaren zestig tot tachtig", "veel vrijstaande woningen en twee-onder-een-kappers", "tegen de bossen aan, waardoor noordgevels snel vergroenen"),
    "putten":        ("gemengd, veel uit de jaren zeventig", "vrijstaande woningen, deels met riet en houten geveldelen", "beschutte ligging op de Veluwerand"),
    "nijkerk":       ("oude kern plus recente nieuwbouw in Doornsteeg", "historische panden naast moderne rijwoningen", "half beschut, met open zicht richting de Arkervaart"),
    "nunspeet":      ("jaren zestig en zeventig", "ruime woningen met veel houtwerk", "bos en zandgrond, veel groenaanslag op gevels"),
    "elburg":        ("vestingstad met naoorlogse uitbreidingen", "monumenten binnen de vesting, gewone woningen erbuiten", "aan het Drontermeer, wind vanaf het water"),
    "kampen":        ("historische binnenstad plus nieuwbouw in Het Onderdijks", "monumentale panden naast moderne eengezinswoningen", "aan de IJssel, vochtig en winderig"),
    "zwolle":        ("van middeleeuwse binnenstad tot Stadshagen", "alle woningtypes, van grachtenpand tot nieuwbouwappartement", "in de IJsseldelta, gemiddeld beschut"),
    "genemuiden":    ("jaren zestig tot tachtig", "eengezinswoningen dicht op elkaar", "aan het Zwarte Water, vochtig en winderig"),
    "bunschoten-spakenburg": ("historische kern plus naoorlogse wijken", "karakteristieke panden in de kern, rijwoningen daarbuiten", "aan het Eemmeer, veel wind en vocht"),
    "amersfoort":    ("middeleeuwse binnenstad tot de nieuwbouw van Vathorst", "van monumenten tot recente gezinswoningen", "landinwaarts en relatief beschut"),
    "huizen":        ("jaren zestig tot tachtig", "eengezinswoningen en appartementen", "direct aan het Gooimeer, met zoutlucht en wind"),
    "blaricum":      ("gemengd, met veel vooroorlogse villabouw", "karakteristieke villa's met riet en houten gevels", "beschut tussen bos en heide"),
    "naarden":       ("vesting plus naoorlogse uitbreidingen", "monumenten binnen de vesting, gewone woningen erbuiten", "aan het Gooimeer, wind vanaf het water"),
    "bussum":        ("vooral jaren dertig", "woningen met roedeverdeling en veel raamdetail", "beschut, in bosrijke omgeving"),
    "hilversum":     ("jaren twintig tot veertig, veel Dudok", "jaren-dertig woningen, deels met stalen kozijnen", "bosrijk en beschut"),
    "weesp":         ("historische kern plus nieuwbouw in Weespersluis", "grachtenpanden naast moderne gezinswoningen", "aan de Vecht, vochtig"),
}

for _p in PLAATSEN:
    _b, _w, _l = WONINGEN.get(_p["slug"], ("gemengd", "een mix van woningtypes", "gemiddeld beschut"))
    _p["bouwperiode"], _p["woningmix"], _p["ligging"] = _b, _w, _l
