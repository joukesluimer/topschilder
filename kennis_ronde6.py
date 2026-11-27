# -*- coding: utf-8 -*-
"""Kennisbank ronde 6: tien nieuwe artikelen, zelfde formaat als ARTIKELEN in kennis_artikelen.py.

Onderwerpen gekozen op zoekvolume (Semrush database nl, november 2026), alleen vragen die nog
geen eigen artikel hadden: behang verven (720) en behang overschilderen (390), renovlies (5.400)
en glasvliesbehang (3.600), radiator verven (1.600), keukenkastjes verven (1.600), buitenmuur
verven (1.300), gevel impregneren (2.400), vochtige muur (320) en opstijgend vocht (260),
scheuren in muur (720), nicotine aanslag verwijderen (590) en kalkverf (2.900) / krijtverf (3.600).

Daarnaast VERDIEPING_R6: extra secties en FAQ voor de vijf dunste artikelen die nog niet in
ronde 5 zijn verdiept. Prijzen komen uit kosten_data.py; technische cijfers uit de genoemde
productbladen en -pagina's (geraadpleegd op 27 november 2026).
"""

from kennis_artikelen import TDS_MUURVERF, TDS_LATEX, TDS_PRIMER, TDS_BL_PRIMER, CONSUMENTENBOND, KASSA_HOUT
from kennis_ronde4a import TDS_VOORSTRIJK, RIVM_FOLDER, RIJKSOVERHEID_VENTILEREN

# Bronnen voor deze ronde
ALAB_ALLES_IN_1 = ("Alabastine, productinformatie Voorstrijk Alles in 1 (isoleert vlekken, zet poederende ondergrond vast)",
                   "https://www.alabastine.nl/wp-content/uploads/2015/12/Voorstrijk-Alles-in-1.pdf")
ALAB_2IN1_VLEKKEN = ("Alabastine, productpagina 2-in-1 Muurverf Vlekken", "https://www.alabastine.nl/product/2-in-1-muurverf-vlekken/")
HORNBACH_XTRA_VLEKKEN = ("Hornbach, productpagina Alabastine Xtra Voorstrijk Vlekken (terpentinebasis, verbruik)",
                         "https://www.hornbach.nl/p/alabastine-xtra-voorstrijk-vlekken-wit-250-ml/10174087/")
GAMMA_RENOVATIEVLIES = ("Gamma, productpagina Renovatievlies overschilderbaar 130 g/m²",
                        "https://www.gamma.nl/assortiment/renovatievlies-overschilderbaar-uni-wit-7920-130gr-20m/p/B243173")
SLIMSTER_VLIES = ("Slimster, Wat is het verschil tussen renovlies, glasvlies en glasvezel?",
                  "https://slimster.nl/blog/verschil-renovlies-glasvlies-glasvezel")
WERKSPOT_GLASVLIES = ("Werkspot, Glasvliesbehang: wat is het en wat zijn de voordelen?",
                      "https://www.werkspot.nl/schilderen/artikelen/glasvliesbehang-wat-is-het-en-wat")
BOSTIK_GLASVEZELLIJM = ("Bostik, productpagina Glasvezellijm", "https://www.bostik.com/netherlands/nl_NL/catalog/product/construction/emea/netherlands/product-glasvezellijm/")
FLEXA_RADIATOR = ("Flexa, productpagina Radiatorlak alkyd", "https://www.flexa.nl/nl/producten/radiatorlak-alkyd")
GAMMA_FLEXA_RADIATOR = ("Gamma, productpagina Flexa Mooi Makkelijk Radiatorlak zijdeglans (hittebestendig tot 80 °C)",
                        "https://www.gamma.nl/assortiment/flexa-mooi-makkelijk-radiatorlak-zijdeglans-750-ml/p/B225494")
HAMMERITE_RADIATOR = ("Hammerite, kenmerkenblad Radiatorlak Hoogglans",
                      "https://cdn11.bigcommerce.com/s-ji12049oz7/content/downloads/Kenmerkenblad_Hammerite-Radiatorlak-Hoogglans.pdf")
WIJZONOL_HECHTPRIMER = ("Wijzonol, kenmerkenblad Hechtprimer Waterverdunbaar (hout en hard pvc)",
                        "https://cdn11.bigcommerce.com/s-ji12049oz7/content/downloads/Kenmerkenblad_Wijzonol-Hechtprimer-Waterverdunbaar.pdf")
GAMMA_KEUKENKAST = ("Gamma, klusadvies Keukenkastjes verven", "https://www.gamma.nl/klusadvies/a/keukenkastjes-verven")
GAMMA_FLEXA_KEUKEN = ("Gamma, productpagina Flexa Mooi Makkelijk Keukenkasten zijdeglans (hout, melamine, formica, hard kunststof)",
                      "https://www.gamma.nl/assortiment/flexa-mooi-makkelijk-keukenkasten-zijdeglans-750-ml/p/B624021")
SIKA_SILICAAT = ("Sika, productinformatie SikaWall-475 Silicate (silicaatgevelverf voor minerale ondergronden)",
                 "https://nld.sika.com/dam/dms/nl01/a/sikawall-475-silicate.pdf")
SIKA_SILOXAAN = ("Sika, productinformatie SikaWall-465 Siloxane (siloxaangevelverf)",
                 "https://nld.sika.com/dam/dms/nl01/n/sikawall-465-siloxane.pdf")
KNB_HYDROFOBEREN = ("Kennisnetwerk Baksteenmetselwerk (KNB), verslag bijeenkomst Gevelreiniging en hydrofoberen",
                    "https://www.knb-keramiek.nl/media/37443/3e_bijeenkomst__gevelreiniging_en_hydrofoberen.pdf")
TUD_HYDROFOBEREN = ("Lubelli e.a. (TU Delft en TNO), artikel over waterwerende behandeling van metselwerk, Monumenten en Kennis 2016",
                    "https://pure.tudelft.nl/ws/files/9427395/Lubelli_et_al_MenK_2016.pdf")
CONSUMENTENBOND_VOCHT = ("Consumentenbond, Vocht in huis: oorzaken en oplossingen", "https://www.consumentenbond.nl/luchtontvochtiger/vocht-in-huis")
ALAB_SUPERIEUR = ("Alabastine, productinformatie Superieure Muurvuller", "https://alabastine.nl/wp-content/uploads/2015/11/superieure-muurvuller.pdf")
ALAB_MUURVULLER_SNEL = ("Alabastine, productinformatie Sneldrogende Muurvuller (pot)",
                        "https://www.alabastine.nl/wp-content/uploads/2015/03/sneldrogende-muurvuller-pot.pdf")
GAMMA_SCHEUREN_NADEN = ("Gamma, productpagina Alabastine Scheuren & Naden muurvuller (flexibel, acrylaat)",
                        "https://www.gamma.nl/assortiment/alabastine-scheuren-naden-muurvuller-330-gram/p/B536714")
PO_CLASSICO = ("Pure & Original, kenmerkenblad Classico krijtverf",
               "https://cdn11.bigcommerce.com/s-ji12049oz7/content/downloads/Kenmerkenblad_Pure-En-Original-Classico.pdf")
PO_FRESCO = ("Pure & Original, kenmerkenblad Fresco kalkverf",
             "https://cdn11.bigcommerce.com/s-ji12049oz7/content/downloads/Kenmerkenblad_Pure-En-Original-Fresco.pdf")
HISTOR_KALKMAT = ("Histor, productpagina One by Histor Muurverf Kalkmat", "https://histor.nl/Producten/muurverf/one-by-histor-muurverf-kalkmat.html")


ARTIKELEN_RONDE6 = [
# ---------------------------------------------------------------------------
{
"slug": "behang-verven",
"groep": "Voorbereiden en uitvoeren",
"titel": "Behang verven of overschilderen: wanneer kan het en hoe doe je het?",
"seo_titel": "Behang verven of overschilderen: zo doe je het",
"description": "Kun je behang overschilderen? Welk behang je kunt verven, welke verf je gebruikt, hoe je naden en bobbels voorkomt en wat een schilder ervoor rekent.",
"kort": "Welk behang je kunt overschilderen, met welke verf, en wanneer je het beter weghaalt.",
"foto": "structuurbehang-witte-wand",
"intro": "Behang weghalen is veel werk. Daarom vragen veel mensen zich af of ze er niet gewoon overheen kunnen schilderen. Soms kan dat prima, soms krijg je er spijt van. Het hangt af van het soort behang en hoe goed het nog vastzit. Hier lees je hoe je dat beoordeelt, welke verf je gebruikt en hoe je het netjes doet.",
"kort_antwoord": "Je kunt behang overschilderen als het goed vastzit en bedoeld is om te verven, zoals vliesbehang, renovlies, glasvlies en structuurbehang. Gewoon papierbehang kan ook, maar kan bobbelen. Vinylbehang en behang met een glanzende toplaag kun je beter niet verven: de verf hecht slecht. Gebruik een goede muurverf, test eerst op een klein stuk en zet twee lagen. Een schilder rekent ongeveer €10 tot €16 per m² voor muren.",
"secties": [
("Welk behang kun je overschilderen?",
"""<div class="tablewrap"><table>
<thead><tr><th>Soort behang</th><th>Overschilderen?</th><th>Let op</th></tr></thead>
<tbody>
<tr><td><strong>Vliesbehang, renovlies, glasvlies</strong></td><td>Ja, daar is het voor gemaakt.</td><td>Meestal één tot twee lagen muurverf. Soms is het al voorgeschilderd.</td></tr>
<tr><td><strong>Structuurbehang (overschilderbaar)</strong></td><td>Ja.</td><td>De structuur neemt meer verf op. Gebruik een roller met een langere vacht.</td></tr>
<tr><td><strong>Papierbehang</strong></td><td>Soms.</td><td>Het papier wordt nat van de verf en kan gaan bobbelen of loslaten. Test eerst.</td></tr>
<tr><td><strong>Vinylbehang, behang met glanslaag</strong></td><td>Liever niet.</td><td>Verf hecht slecht op de kunststof toplaag en kan later afbladderen.</td></tr>
<tr><td><strong>Behang met zware print of donkere kleur</strong></td><td>Met een isolerende voorstrijk.</td><td>Anders kan het patroon of de kleur door de nieuwe verf heen blijven schemeren.</td></tr>
</tbody></table></div>
<p>Weet je niet wat er hangt? Kras met je nagel over het oppervlak. Voelt het glad en plastic aan, dan is het waarschijnlijk vinyl. Trek een hoekje los: vlies laat droog in één stuk los, papier scheurt. Meer over het verschil tussen vliessoorten lees je in <a href="/kennisbank/renovlies-of-glasvlies/">renovlies of glasvlies</a>.</p>"""),
("Eerst controleren: zit het behang goed vast?",
"""<p>Verf maakt behang niet steviger. Losse naden, bobbels en hoeken die loslaten worden na het schilderen vaak erger, omdat het vocht uit de verf het behang even zacht maakt. Loop daarom de hele muur af met je hand en let op:</p>
<ul>
<li><strong>Naden.</strong> Een losse naad plak je eerst opnieuw vast met naadlijm en een naadroller.</li>
<li><strong>Bobbels.</strong> Een kleine bobbel snij je in met een mesje, je spuit er lijm achter en drukt hem plat.</li>
<li><strong>Grote losse delen.</strong> Laat je een groot stuk los zitten, dan kun je het behang beter helemaal verwijderen. Hoe dat gaat, lees je in <a href="/kennisbank/behang-verwijderen/">behang verwijderen</a>.</li>
<li><strong>Vocht en schimmel.</strong> Schimmelplekken of een vochtige muur los je eerst op. Verf eroverheen helpt niet. Zie <a href="/kennisbank/vochtige-muur/">vochtige muur</a>.</li>
</ul>"""),
("Welke verf gebruik je op behang?",
"""<p>Op behang gebruik je gewone <strong>muurverf</strong> of latex op waterbasis. Een matte verf verbergt naden en kleine oneffenheden het best. Zijdeglans laat juist elke naad zien. Het verschil tussen de soorten muurverf staat in <a href="/kennisbank/latex-of-muurverf/">latex of muurverf</a>.</p>
<p>Gaat het om behang met een donker patroon, vlekken of een print die door kan slaan? Zet dan eerst een <strong>isolerende voorstrijk</strong>. Volgens de productinformatie van Alabastine isoleert hun Voorstrijk Alles in 1 onverdund vlekken zoals nicotine, roet en lekkage. Op gewoon wit vliesbehang is een voorstrijk meestal niet nodig, behalve als de fabrikant van het behang dat adviseert.</p>"""),
("Zo voorkom je bobbels en zichtbare naden",
"""<p>De meeste problemen bij geschilderd behang komen door te veel vocht in één keer. Werk daarom met twee dunne lagen in plaats van één dikke. Laat de eerste laag helemaal drogen voor je de tweede zet. Ontstaat er tijdens het schilderen een bobbel in papierbehang, raak hem dan niet aan. Vaak trekt hij bij het drogen weer strak.</p>
<p>Rol in banen van ongeveer een meter breed, van boven naar beneden, en werk nat in nat door. Zo voorkom je strepen, net als bij een plafond; zie <a href="/kennisbank/plafond-schilderen-zonder-strepen/">plafond schilderen zonder strepen</a>.</p>"""),
("Overschilderen of weghalen?",
"""<p>Overschilderen is sneller en goedkoper. Maar heb je het behang eenmaal geverfd, dan is het later moeilijker te verwijderen: de verflaag houdt water tegen, zodat het behang slechter week wordt. Wil je over een paar jaar toch een gestucte muur, dan betaal je dat later.</p>
<p>Weghalen is beter als er vinyl hangt, als het behang op veel plekken loszit, of als je echt een strakke, gladde wand wilt. Na het weghalen kun je de muur plamuren of laten sausen. Zie <a href="/kennisbank/muur-plamuren/">muur plamuren</a>.</p>"""),
("Wat vraag je de schilder?",
"""<ul>
<li>Wat voor behang hangt er volgens hem, en kan het echt overgeschilderd worden?</li>
<li>Worden losse naden en bobbels eerst vastgezet, en zit dat in de prijs?</li>
<li>Is een isolerende voorstrijk nodig, bijvoorbeeld bij een donker patroon?</li>
<li>Welke muurverf en hoeveel lagen worden gebruikt?</li>
<li>Wat kost het als het behang toch beter weg kan? Laat beide opties op de offerte zetten.</li>
</ul>"""),
("Rekenvoorbeeld: woonkamer met vliesbehang",
"""<p>Een woonkamer heeft 55 m² wand met wit vliesbehang dat goed vastzit. De schilder zet twee lagen muurverf. Voor muren rekenen schilders ongeveer €10 tot €16 per m², inclusief verf en btw. Dat is €550 tot €880. Moeten er eerst naden worden vastgezet of komt er een isolerende voorstrijk bij, reken dan €2 tot €5 per m² extra. Zijn de muren in slechte staat en moet het behang weg, dan komt daar de prijs van verwijderen en eventueel opnieuw behangen bij; behangen kost €9 tot €24 per m² inclusief behang.</p>"""),
],
"stappen": [
("Bepaal het soort behang", "Kras en trek een hoekje los. Vlies, renovlies en glasvlies zijn bedoeld om te verven; vinyl niet."),
("Controleer naden en bobbels", "Plak losse naden vast met naadlijm en zet kleine bobbels vast. Bij grote losse delen kun je beter alles weghalen."),
("Maak schoon", "Neem het behang af met een licht vochtige doek en laat het drogen. Vet en stof hechten slecht."),
("Test op een klein stuk", "Schilder een stuk van een halve m² op een onopvallende plek en kijk de volgende dag of er bobbels of doorslag zijn."),
("Isoleer waar nodig", "Zet een isolerende voorstrijk op vlekken of op een donker patroon."),
("Zet twee dunne lagen", "Rol muurverf in banen van boven naar beneden. Laat de eerste laag helemaal drogen voor de tweede."),
],
"kosten": ["schilderen-per-m2", "binnenschilderwerk"],
"dienst": "behangen",
"faq": [
("Kun je over behang heen schilderen?", "Ja, als het behang goed vastzit en geschikt is om te verven, zoals vliesbehang, renovlies, glasvlies en overschilderbaar structuurbehang. Op vinylbehang hecht verf slecht."),
("Welke verf gebruik je voor behang?", "Een matte muurverf of latex op waterbasis. Op behang met vlekken of een donker patroon zet je eerst een isolerende voorstrijk."),
("Gaat papierbehang bobbelen als je het verft?", "Dat kan, omdat het papier nat wordt van de verf. Werk met dunne lagen en test eerst. Kleine bobbels trekken bij het drogen vaak weer strak."),
("Moet je behang voorstrijken voor het verven?", "Meestal niet bij wit vliesbehang. Wel bij vlekken, een donker patroon of als de fabrikant het adviseert. Gebruik dan een isolerende voorstrijk."),
("Hoeveel lagen verf op behang?", "Meestal twee. Op voorgeschilderd glasvlies is soms één laag genoeg, maar bij een kleurwissel heb je er twee nodig."),
("Kun je geschilderd behang later nog verwijderen?", "Ja, maar het is lastiger. De verflaag houdt water tegen, dus het behang wordt minder goed week. Een stoomapparaat helpt."),
("Wat kost behang laten overschilderen?", "Ongeveer €10 tot €16 per m² voor muren, inclusief verf en btw. Voor een woonkamer met 55 m² wand is dat €550 tot €880."),
],
"bronnen": [ALAB_ALLES_IN_1, GAMMA_RENOVATIEVLIES, SLIMSTER_VLIES, TDS_MUURVERF],
"gerelateerd": ["behang-verwijderen", "renovlies-of-glasvlies", "latex-of-muurverf"],
},
# ---------------------------------------------------------------------------
{
"slug": "renovlies-of-glasvlies",
"groep": "Voorbereiden en uitvoeren",
"titel": "Renovlies of glasvlies: wat is het verschil en wat kies je?",
"seo_titel": "Renovlies of glasvlies? Verschil en wat je kiest",
"description": "Renovlies, glasvlies of glasweefsel: wat is het verschil, wanneer kies je wat, hoe breng je het aan en hoe schilder je het? Met kosten per m² en tips.",
"kort": "Het verschil tussen renovlies, glasvlies en glasweefsel, en welke je kiest voor een strakke muur.",
"foto": "behang-naast-gestucte-wand",
"intro": "Een muur met kleine scheurtjes, putjes of oud behang strak krijgen zonder te stucen: daar zijn renovlies en glasvlies voor. Je plakt een dunne laag vlies op de muur en schildert die over. In de bouwmarkt en op offertes worden de namen vaak door elkaar gebruikt, terwijl het verschillende producten zijn. Hier lees je wat het verschil is, wat je kiest en wat het kost.",
"kort_antwoord": "Renovlies is een vlies van cellulose en kunststofvezels. Het is goedkoper, makkelijk te verwerken en later weer droog van de muur te trekken. Glasvlies is gemaakt van glasvezels, is steviger en overbrugt kleine scheurtjes beter, maar is duurder en lastiger te verwijderen. Glasweefsel is nog grover en heeft een zichtbare structuur. Beide vliezen schilder je over met muurverf. Een schilder rekent voor behangen €9 tot €24 per m², plus €10 tot €16 per m² voor het schilderen.",
"secties": [
("Drie soorten naast elkaar",
"""<div class="tablewrap"><table>
<thead><tr><th>Soort</th><th>Gemaakt van</th><th>Sterk punt</th><th>Minder sterk</th></tr></thead>
<tbody>
<tr><td><strong>Renovlies</strong></td><td>Cellulose met kunststofvezels</td><td>Goedkoop, makkelijk te plakken, later droog af te trekken.</td><td>Minder stootvast. Verbergt minder grote oneffenheden.</td></tr>
<tr><td><strong>Glasvlies</strong></td><td>Glasvezels, glad vlies</td><td>Stevig, overbrugt haarscheurtjes, slijtvast, ook geschikt voor vochtiger ruimtes.</td><td>Duurder. Stofjes bij het snijden kunnen jeuken. Moeilijker te verwijderen.</td></tr>
<tr><td><strong>Glasweefsel</strong></td><td>Geweven glasvezel</td><td>Zeer sterk, met een zichtbare structuur (visgraat, ruit).</td><td>Je ziet het weefsel door de verf heen. Niet voor een gladde muur.</td></tr>
</tbody></table></div>
<p>Werkspot noemt glasvlies steviger en duurzamer dan renovlies door de hogere dichtheid, en daardoor ook duurder. Slimster wijst erop dat renovlies juist goed weer van de muur af te halen is. Kies dus niet alleen op prijs, maar ook op wat je over een paar jaar met de muur wilt.</p>"""),
("Wanneer kies je wat?",
"""<ul>
<li><strong>Nieuwbouw of een redelijk gladde muur</strong> die je alleen egaal wilt maken: renovlies is vaak genoeg.</li>
<li><strong>Een muur met haarscheurtjes</strong> die steeds terugkomen, bijvoorbeeld op naden van gipsplaten: glasvlies overbrugt die beter.</li>
<li><strong>Een gang, trapgat of kinderkamer</strong> waar veel tegenaan wordt gestoten: glasvlies of glasweefsel is slijtvaster.</li>
<li><strong>Een huurhuis</strong> of als je later wilt kunnen terugwerken naar een kale muur: renovlies is makkelijker te verwijderen.</li>
<li><strong>Grote scheuren, gaten of een bolle muur</strong>: vlies verbergt dat niet. Dan moet er eerst gerepareerd of gestuct worden. Zie <a href="/kennisbank/scheuren-in-muur-en-plafond/">scheuren in muur en plafond</a>.</li>
</ul>"""),
("Hoe wordt het aangebracht?",
"""<p>Vlies wordt anders geplakt dan papierbehang: de lijm gaat op de muur, niet op het vlies. Je drukt de droge baan in de natte lijm en strijkt hem aan. De banen gaan naad op naad, niet overlappend.</p>
<p>Voor glasvlies gebruik je een lijm die daarvoor bedoeld is, zoals een kant-en-klare glasvezellijm. Bostik biedt daar een aparte glasvezellijm voor aan. Een zuigende of poederende muur moet eerst worden voorgestreken, anders trekt de lijm te snel in. Hoe je voorstrijkt, lees je in <a href="/kennisbank/nieuw-stucwerk-schilderen/">nieuw stucwerk schilderen</a>.</p>"""),
("Overschilderen: één of twee lagen?",
"""<p>Glasvlies moet altijd worden geschilderd, het is niet bedoeld om kaal te laten. Renovlies kun je in principe kaal laten, maar bijna iedereen verft het. Gebruik een matte muurverf of latex. Bij vlies dat niet voorgeschilderd is, zuigt de eerste laag flink. Reken dus op twee lagen, en bij een donkere kleur soms drie.</p>
<p>Er bestaat ook voorgeschilderd glasvlies. Dat zuigt minder en heeft vaak genoeg aan één laag als je wit wilt. Kies voor het schilderen een verf die geschikt is voor vlies; volgens de bouwmarkt hecht kalkverf slecht op glasvlies. Meer over kalkverf in <a href="/kennisbank/kalkverf-of-krijtverf/">kalkverf of krijtverf</a>.</p>"""),
("Wat vraag je de schilder?",
"""<ul>
<li>Welk vlies stelt hij voor, en waarom: renovlies, glasvlies of voorgeschilderd glasvlies?</li>
<li>Welk gewicht (bijvoorbeeld 130 of 150 gram per m²)? Zwaarder vlies verbergt meer.</li>
<li>Worden scheuren en gaten eerst gerepareerd, en zit dat in de prijs?</li>
<li>Is het behangen en het schilderen samen geoffreerd, met het aantal lagen verf erbij?</li>
<li>Wat gebeurt er met plinten, stopcontacten en lichtknoppen?</li>
</ul>"""),
("Rekenvoorbeeld: slaapkamer met haarscheurtjes",
"""<p>Een slaapkamer heeft 33 m² muur met haarscheurtjes op de naden van de gipsplaten. De schilder plakt glasvlies en schildert dat twee keer. Behangen kost €9 tot €24 per m², afhankelijk van het vlies en de staat van de muur; dat is €300 tot €790. Schilderen kost €10 tot €16 per m², dus €330 tot €530. Samen kom je uit op ongeveer €630 tot €1.320, inclusief materiaal en btw. Met renovlies zit je meestal aan de onderkant van die bandbreedte.</p>"""),
],
"stappen": [
("Bekijk de muur", "Haarscheurtjes en putjes kan vlies verbergen. Grote scheuren, gaten en bolle plekken eerst repareren."),
("Kies het vlies", "Renovlies voor een gladde muur of huurhuis, glasvlies voor scheurtjes en plekken met stootschade."),
("Maak de muur klaar", "Oud losgeraakt behang eraf, gaten vullen, schuren en stofvrij maken. Zet een voorstrijk op zuigende ondergrond."),
("Lijm op de muur", "Rol lijm op de muur voor één baan tegelijk en druk de droge baan erin."),
("Naad op naad plakken", "Strijk elke baan glad zonder lucht eronder en snij boven en onder strak af."),
("Laat drogen en schilder", "Laat de lijm minstens een dag drogen. Zet daarna twee lagen matte muurverf."),
],
"kosten": ["schilderen-per-m2", "latex-spuiten"],
"dienst": "behangen",
"faq": [
("Wat is het verschil tussen renovlies en glasvlies?", "Renovlies is gemaakt van cellulose en kunststofvezels, glasvlies van glasvezels. Glasvlies is steviger en overbrugt scheurtjes beter. Renovlies is goedkoper en makkelijker te verwijderen."),
("Moet je renovlies schilderen?", "Het hoeft niet, maar bijna iedereen doet het. Glasvlies moet wel altijd worden geschilderd."),
("Hoeveel lagen verf op glasvlies?", "Meestal twee lagen muurverf. Voorgeschilderd glasvlies heeft bij wit vaak genoeg aan één laag."),
("Verbergt glasvlies scheuren?", "Kleine haarscheurtjes wel. Grote of werkende scheuren moeten eerst worden gerepareerd, anders komen ze terug."),
("Kun je glasvlies weer verwijderen?", "Ja, maar het is lastiger dan renovlies. Je moet het nat maken of met een stoomapparaat losweken. Renovlies trek je vaak droog los."),
("Is glasvlies geschikt voor de badkamer?", "Glasvlies kan tegen vocht, maar de lijm en verf moeten er ook geschikt voor zijn. Bij veel spatwater zijn tegels of een speciale coating beter."),
("Wat kost glasvlies laten aanbrengen en schilderen?", "Ongeveer €9 tot €24 per m² voor het behangen plus €10 tot €16 per m² voor het schilderen, inclusief materiaal en btw."),
],
"bronnen": [WERKSPOT_GLASVLIES, SLIMSTER_VLIES, GAMMA_RENOVATIEVLIES, BOSTIK_GLASVEZELLIJM],
"gerelateerd": ["behang-verven", "muur-plamuren", "nieuw-stucwerk-schilderen"],
},
# ---------------------------------------------------------------------------
{
"slug": "radiator-verven",
"groep": "Voorbereiden en uitvoeren",
"titel": "Radiator verven: welke verf en hoe doe je het zonder strepen?",
"seo_titel": "Radiator verven: welke verf en hoe doe je het?",
"description": "Je radiator verven of laten spuiten? Welke radiatorlak tegen hitte kan, hoe je roest behandelt, verven zonder strepen en wat een schilder per radiator rekent.",
"kort": "Welke lak tegen de warmte kan, hoe je roest aanpakt en hoe je een radiator strak verft.",
"foto": "kwast-tegen-lichte-muur",
"intro": "Een vergeelde radiator met roestplekjes valt meteen op naast een vers geschilderde muur. Gelukkig kun je een radiator prima opnieuw verven. Je hebt wel verf nodig die tegen warmte kan, en het voorwerk luistert nauw: anders vergeelt de laag snel of bladdert hij af. Hier lees je welke verf je kiest, hoe je roest behandelt en hoe je strepen voorkomt.",
"kort_antwoord": "Verf een radiator met radiatorlak: lak die tegen warmte kan en niet snel vergeelt. Zet de verwarming uit, laat de radiator afkoelen, ontvet en schuur hem, behandel roest met een roestwerende grondverf en zet twee dunne lagen. Werk alleen op een koude radiator en zet hem pas na de droogtijd op het blik weer aan. Een schilder rekent €90 tot €225 per radiator.",
"secties": [
("Welke verf hoort op een radiator?",
"""<p>Op een radiator hoort <strong>radiatorlak</strong>. Gewone muurverf of een goedkope lak kan bij warmte verkleuren, zacht worden of gaan ruiken. Radiatorlak is gemaakt om warmte te verdragen. Hoeveel, verschilt per product:</p>
<ul>
<li>Een watergedragen radiatorlak van Flexa is volgens de verkoper hittebestendig tot 80 °C.</li>
<li>Flexa heeft daarnaast een glanzende radiatorlak op alkydbasis voor radiatoren en cv-leidingen binnen.</li>
<li>Hammerite levert een radiatorlak in hoogglans die als hittebestendig wordt omschreven.</li>
</ul>
<p>Een gewone cv-radiator wordt in de praktijk niet heter dan zo'n 70 à 80 °C, en met een moderne cv-ketel of warmtepomp vaak veel minder. Controleer altijd de maximale temperatuur op het blik. Lak op terpentinebasis vergeelt op een warme radiator sneller dan watergedragen lak; wil je hem helder wit houden, kies dan watergedragen. Het verschil tussen beide lees je in <a href="/kennisbank/verf-op-waterbasis-of-terpentinebasis/">verf op waterbasis of terpentinebasis</a>.</p>"""),
("Roest: zo pak je het aan",
"""<p>Roestplekken zie je vooral onderaan de radiator en rond de ontluchtingskraan, waar water heeft gestaan. Verf er niet zomaar overheen: roest werkt door onder de nieuwe laag en drukt hem binnen een jaar los.</p>
<ol>
<li>Schuur of borstel de roest weg tot op blank metaal.</li>
<li>Maak de plek stofvrij en ontvet hem.</li>
<li>Zet een roestwerende grondverf voor metaal op de kale plekken.</li>
<li>Laat drogen en lak daarna de hele radiator.</li>
</ol>
<p>Is de radiator doorgeroest of lekt hij, dan helpt verven niet meer. Dan is vervangen de enige oplossing.</p>"""),
("Kwast, roller of spuitbus?",
"""<p>Voor de voorkant van een paneelradiator werkt een kleine lakroller van vilt of schuim goed: die geeft een gladde laag. Voor randen en hoeken neem je een kwast. Tussen de panelen en lamellen kom je met een speciale radiatorkwast met een lange, gebogen steel.</p>
<p>Een spuitbus geeft de strakste laag, maar je moet alles eromheen afdekken en hij is voor een hele radiator vrij duur. Een schilder spuit een radiator vaak met een verfspuit, ter plekke of in de werkplaats. Dat geeft een fabrieksachtige laag.</p>"""),
("Radiator los of laten hangen?",
"""<p>Laat je de radiator hangen, dan kun je de achterkant en de muur erachter niet goed verven. Dat is meestal geen probleem: je ziet alleen de voorkant. Wil je het echt netjes, of ook de muur erachter schilderen, dan moet de radiator los. Daarvoor moet de cv-installatie worden afgesloten of afgetapt, en daarna weer bijgevuld en ontlucht. Twijfel je, laat dat dan over aan een installateur of een schilder die het vaker doet.</p>
<p>Gaat de schilder de muren toch doen? Laat de radiatoren dan in dezelfde ronde meenemen. Dan deel je de kosten van afdekken en opstarten. Zie <a href="/kosten/binnenschilderwerk/">kosten binnenschilderwerk</a>.</p>"""),
("Veelgemaakte fouten",
"""<ul>
<li><strong>Verven op een warme radiator.</strong> De verf droogt dan te snel, trekt strepen en hecht slechter.</li>
<li><strong>Niet ontvetten.</strong> Op een radiator zit vet en stof. Verf hecht daar niet op.</li>
<li><strong>Te dikke lagen.</strong> Die gaan druipen, vooral aan de onderrand. Twee dunne lagen zijn beter.</li>
<li><strong>Te vroeg aanzetten.</strong> Zet de verwarming pas weer aan na de droogtijd op het blik, en eerst op een lage stand.</li>
<li><strong>Kranen en thermostaatknop meeverven.</strong> Haal de knop eraf en plak de kranen af.</li>
</ul>"""),
("Wat vraag je de schilder?",
"""<ul>
<li>Wordt de radiator ter plekke geschilderd of gespoten, of in de werkplaats?</li>
<li>Welke radiatorlak wordt gebruikt, en tot welke temperatuur kan die?</li>
<li>Hoe worden roestplekken behandeld, en kost dat extra?</li>
<li>Moet de radiator los, en wie regelt het aftappen en bijvullen van de cv?</li>
<li>Hoe lang moet de verwarming uit blijven?</li>
</ul>"""),
("Rekenvoorbeeld: tussenwoning met zeven radiatoren",
"""<p>In een tussenwoning hangen zes gladde paneelradiatoren en één handdoekradiator. Een schilder rekent €90 tot €150 voor een gladde paneelradiator en €120 tot €225 voor een handdoek- of designradiator, inclusief lak en btw. Samen is dat ongeveer €660 tot €1.125. Zijn er roestplekken, reken dan €15 tot €40 extra per radiator. Bij zoveel radiatoren in één keer zit je vaak aan de onderkant van de prijs.</p>"""),
],
"stappen": [
("Zet de verwarming uit", "Laat de radiator helemaal afkoelen. Verf nooit op een warme radiator."),
("Bescherm de omgeving", "Leg folie of papier op de vloer, plak de kranen af en haal de thermostaatknop eraf."),
("Ontvet en schuur", "Was de radiator met ontvetter, spoel na en schuur hem licht op met fijn schuurpapier of schuurvlies."),
("Behandel roest", "Schuur roestplekken tot blank metaal en zet daar een roestwerende grondverf op."),
("Lak in dunne lagen", "Eerst de randen en de ruimte tussen de panelen, dan de voorkant met een lakroller. Twee dunne lagen."),
("Laat uitharden", "Zet de verwarming pas weer aan na de droogtijd op het blik, eerst op een lage stand."),
],
"kosten": ["radiatoren-schilderen", "binnenschilderwerk"],
"faq": [
("Welke verf gebruik je voor een radiator?", "Radiatorlak: lak die tegen warmte kan en niet snel vergeelt. Kijk op het blik tot welke temperatuur hij bestand is."),
("Kun je een radiator verven met muurverf?", "Liever niet. Muurverf is niet gemaakt voor warmte en metaal. Hij kan verkleuren, loslaten en is minder stootvast."),
("Moet de radiator uit als je hem verft?", "Ja. Zet de verwarming uit en laat de radiator afkoelen. Op een warme radiator droogt de verf te snel en ontstaan strepen."),
("Hoe lang moet een geverfde radiator uit blijven?", "Volg de droogtijd op het blik. Zet hem daarna eerst op een lage stand, zodat de lak rustig kan uitharden."),
("Hoe verf je een radiator zonder strepen?", "Op een koude, schone radiator, met een lakroller voor de voorkant en twee dunne lagen. Spuiten geeft de gladste laag."),
("Kun je roest op een radiator overschilderen?", "Niet zomaar. Schuur de roest weg tot blank metaal, zet een roestwerende grondverf en lak daarna."),
("Wat kost een radiator laten verven?", "€90 tot €225 per radiator, inclusief lak en btw. Een gladde paneelradiator zit aan de onderkant, een designradiator aan de bovenkant."),
],
"bronnen": [GAMMA_FLEXA_RADIATOR, FLEXA_RADIATOR, HAMMERITE_RADIATOR],
"gerelateerd": ["verf-op-waterbasis-of-terpentinebasis", "binnendeuren-verven", "binnen-schilderen-in-de-winter"],
},
# ---------------------------------------------------------------------------
{
"slug": "keukenkastjes-verven",
"groep": "Voorbereiden en uitvoeren",
"titel": "Keukenkastjes verven: zo krijg je een strak en sterk resultaat",
"seo_titel": "Keukenkastjes verven: stappenplan en verf",
"description": "Keukenkastjes verven of laten spuiten? Welke primer en lak op hout, melamine of kunststof, hoe je het stap voor stap doet en wat het per front kost.",
"kort": "Welke primer en lak je nodig hebt, per soort front, en wanneer laten spuiten beter is.",
"foto": "paneel-spuiten-in-spuitcabine",
"intro": "Een keuken die nog prima werkt maar er gedateerd uitziet, kun je een nieuw uiterlijk geven met verf. Dat is veel goedkoper dan een nieuwe keuken. Maar keukenkastjes krijgen het zwaar: vet, stoom, schoonmaakmiddel en elke dag handen. Met gewone lak en weinig voorwerk zie je na een paar maanden de eerste beschadigingen. Hier lees je hoe het wel goed gaat.",
"kort_antwoord": "Haal de deurtjes en laden eraf, ontvet ze grondig, schuur ze op en zet een hechtprimer die past bij het materiaal: hout, MDF, melamine of kunststof. Lak daarna twee dunne lagen met een slijtvaste lak voor keukens of meubels. Rollen kan, spuiten geeft het gladste resultaat. Een schilder rekent €45 tot €95 per front, voor een gemiddelde keuken met 16 fronten €720 tot €1.520.",
"secties": [
("Van welk materiaal zijn je kastjes?",
"""<div class="tablewrap"><table>
<thead><tr><th>Materiaal</th><th>Herken je aan</th><th>Wat nodig is</th></tr></thead>
<tbody>
<tr><td><strong>Massief hout</strong></td><td>Houtnerf, aan de rand geen naad.</td><td>Ontvetten, schuren, grondverf, lak. Het makkelijkst.</td></tr>
<tr><td><strong>Gelakt MDF</strong></td><td>Glad, egaal, vaak met gefreesd profiel.</td><td>Ontvetten, opschuren, hechtprimer op kale plekken, lak.</td></tr>
<tr><td><strong>Melamine of formica</strong></td><td>Harde, gladde toplaag, soms met een randje aan de zijkant.</td><td>Grondig ontvetten, goed opschuren, hechtprimer voor kunststof, lak.</td></tr>
<tr><td><strong>Folie (vaak hoogglans)</strong></td><td>Een dun vel dat aan de randen kan loslaten.</td><td>Losse folie moet er eerst af. Zit hij goed vast: opschuren en hechtprimer. Laat bij twijfel een schilder kijken.</td></tr>
</tbody></table></div>
<p>Op gladde, harde materialen hecht gewone grondverf slecht. Daarom is een <strong>hechtprimer</strong> daar nodig. Het kenmerkenblad van Wijzonol Hechtprimer noemt voor hard pvc bijvoorbeeld: grondig reinigen en ontvetten, schuren, gronden met hechtprimer en dan aflakken.</p>"""),
("Welke lak kies je?",
"""<p>Kies een lak die tegen stoten, krassen en schoonmaken kan. Er zijn speciale keukenkastlakken; Flexa verkoopt er een voor hout, melamine, formica en hard kunststof, ook als 2-in-1 primer en lak. Ook een slijtvaste binnenlak voor deuren en meubels voldoet. Watergedragen lak vergeelt minder en ruikt minder; dat is in een keuken een voordeel. Zie <a href="/kennisbank/verf-op-waterbasis-of-terpentinebasis/">verf op waterbasis of terpentinebasis</a>.</p>
<p><strong>Glans:</strong> zijdeglans is het gangbaarst en makkelijk schoon te houden. Mat ziet er modern uit, maar vingerafdrukken en vetplekken vallen meer op. Hoogglans laat elke oneffenheid zien en is alleen mooi als hij gespoten is.</p>"""),
("Rollen of spuiten?",
"""<p>Met een fijne lakroller van schuim of vilt kom je een heel eind, zeker bij vlakke fronten. Je ziet wel een lichte rolstructuur als het licht schuin op de deur valt. Spuiten geeft een gladde laag die op een nieuwe keuken lijkt. Daar is een spuitinstallatie en een stofvrije ruimte voor nodig. Daarom halen veel schilders de fronten op en spuiten ze in de werkplaats. Wat het verschil kost, lees je bij <a href="/kosten/keuken-spuiten/">keuken laten spuiten</a>.</p>"""),
("Ombouw, plinten en grepen",
"""<p>Je hoeft niet altijd de hele keuken te doen. Is de ombouw (de kasten zelf) nog netjes en zit hij grotendeels achter de deurtjes, dan kun je alleen de fronten doen. Zichtbare zijpanelen en plinten neem je wel mee, anders zie je het kleurverschil.</p>
<p>Vervang de grepen in dezelfde ronde als je dat wilt. Nieuwe grepen met een andere maat passen dan meteen; oude gaten kun je vullen met houtvuller voor je gaat lakken.</p>"""),
("Hoe lang duurt het?",
"""<p>Reken op een paar dagen, vooral door de droogtijden: primer, licht schuren, eerste laag, licht schuren, tweede laag. Lak is na een dag vaak stofdroog, maar heeft langer nodig om echt hard te worden. Ga de eerste week voorzichtig om met de deurtjes en gebruik geen schuurmiddel. Lak die nog niet uitgehard is, beschadigt makkelijk.</p>"""),
("Wat vraag je de schilder?",
"""<ul>
<li>Van welk materiaal zijn mijn fronten, en welke hechtprimer is daarvoor nodig?</li>
<li>Wordt er gerold of gespoten, en gebeurt dat bij mij thuis of in de werkplaats?</li>
<li>Welke lak en welke glansgraad gebruikt hij, en hoeveel lagen?</li>
<li>Zitten zijpanelen, plinten en de binnenkant van de deurtjes in de prijs?</li>
<li>Hoeveel dagen kan ik de keuken niet gebruiken?</li>
<li>Welke garantie geeft hij op de hechting?</li>
</ul>"""),
("Rekenvoorbeeld: hoekkeuken met 16 fronten",
"""<p>Een gemiddelde hoekkeuken heeft 16 fronten: deurtjes en laden. Een schilder rekent €45 tot €95 per front, inclusief primer, lak en btw. Dat is €720 tot €1.520. Zijpanelen en plinten kosten €25 tot €60 per stuk extra. Nieuwe grepen monteren kost €5 tot €15 per greep, zonder de grepen zelf. Kunststof of folie met een hechtprimer en spuitwerk in de werkplaats zit aan de bovenkant; vlakke houten deurtjes die worden gerold aan de onderkant.</p>"""),
],
"stappen": [
("Haal deurtjes en laden eraf", "Nummer ze en bewaar scharnieren en grepen per deur in een zakje."),
("Ontvet grondig", "Gebruik een ontvetter of verfreiniger met water. Vet is de grootste vijand van de hechting. Spoel na met schoon water."),
("Schuur op", "Schuur het oppervlak mat. Gebruik op melamine en kunststof een schuurvlies of fijn schuurpapier. Maak alles stofvrij."),
("Zet een hechtprimer", "Kies een primer die past bij het materiaal. Laat hem drogen zoals op het blik staat."),
("Lak twee dunne lagen", "Schuur licht tussen de lagen. Werk in een stofvrije ruimte en leg de deurtjes plat."),
("Laat uitharden", "Monteer pas als de lak goed droog is, en ga de eerste week voorzichtig om met de keuken."),
],
"kosten": ["keuken-spuiten", "deuren-spuiten"],
"faq": [
("Kun je keukenkastjes verven?", "Ja. Hout, MDF, melamine, formica en vastzittende folie kun je verven, mits je goed ontvet, opschuurt en een passende hechtprimer gebruikt."),
("Welke verf gebruik je voor keukenkastjes?", "Een hechtprimer voor het materiaal en een slijtvaste lak voor keukens of meubels, het liefst watergedragen in zijdeglans."),
("Moet je keukenkastjes schuren voor het verven?", "Ja. Schuren maakt het oppervlak mat, zodat de primer zich vastzet. Zonder schuren laat de verf snel los."),
("Kun je hoogglans keukenkastjes verven?", "Ja, met grondig opschuren en een hechtprimer. Loszittende folie moet eerst weg. Voor hoogglans als eindresultaat is spuiten beter dan rollen."),
("Rollen of spuiten?", "Rollen kan prima bij vlakke fronten. Spuiten geeft een gladdere laag, vooral bij hoogglans en fronten met profiel."),
("Hoe lang gaat geverfde keuken mee?", "Met goed voorwerk en slijtvaste lak vele jaren. Zonder hechtprimer of ontvetten zie je vaak al binnen een jaar beschadigingen."),
("Wat kost keukenkastjes laten verven?", "€45 tot €95 per front. Voor een gemiddelde keuken met 16 fronten is dat €720 tot €1.520, inclusief materiaal en btw."),
],
"bronnen": [WIJZONOL_HECHTPRIMER, GAMMA_FLEXA_KEUKEN, GAMMA_KEUKENKAST],
"gerelateerd": ["binnendeuren-verven", "verf-op-waterbasis-of-terpentinebasis", "tegels-verven"],
},
# ---------------------------------------------------------------------------
{
"slug": "buitenmuur-verven",
"groep": "Verf kiezen",
"titel": "Buitenmuur verven: welke gevelverf kies je en hoe pak je het aan?",
"seo_titel": "Buitenmuur verven: welke gevelverf en hoe?",
"description": "Je buitenmuur of gevel verven? Het verschil tussen acrylaat-, siliconenhars- en silicaatverf, waarom dampopen belangrijk is, de juiste stappen en de kosten per m².",
"kort": "Acrylaat, siliconenhars of silicaat: welke gevelverf past bij jouw muur, en hoe je hem aanbrengt.",
"foto": "bakstenen-muur-verven-oranje-roller",
"intro": "Een buitenmuur verven geeft een huis een heel ander gezicht. Maar een gevel is geen binnenmuur. Hij krijgt regen, vorst en zon, en er moet vocht uit de muur naar buiten kunnen. Kies je de verkeerde verf, dan bladdert die binnen een paar jaar af of houd je vocht in de muur vast. Hier lees je welke gevelverf bij welke muur past en hoe je het aanpakt.",
"kort_antwoord": "Gebruik voor een buitenmuur een dampopen gevelverf: een verf die regen tegenhoudt maar waterdamp uit de muur doorlaat. Op pleisterwerk en eerder geverfde gevels is siliconenharsverf een veilige keuze. Silicaatverf hecht chemisch op kale minerale ondergronden zoals steen en kalkpleister. Gewone acrylaat buitenmuurverf is goedkoper maar minder dampopen. Reinig de gevel, herstel scheuren, gron waar nodig en zet twee lagen bij droog weer boven 5 à 10 °C. Een schilder rekent €20 tot €40 per m².",
"secties": [
("Moet je je buitenmuur wel verven?",
"""<p>Niet elke gevel moet geverfd worden. Schoon metselwerk, dus baksteen die nooit geverfd is, laat je meestal gewoon zo. Een verflaag maakt de muur minder goed in staat om te drogen, en heb je eenmaal geverfd, dan moet je blijven onderhouden. Vaak is reinigen en het voegwerk herstellen een betere keuze.</p>
<p>Verven is wel logisch bij een gevel die al eerder geverfd is, bij pleisterwerk of sierpleister, en bij een muur die er na reinigen nog vlekkerig of ongelijk uitziet. Op de pagina <a href="/kosten/gevel-schilderen/">gevel schilderen</a> staat per soort gevel of schilderen verstandig is.</p>"""),
("Drie soorten gevelverf",
"""<div class="tablewrap"><table>
<thead><tr><th>Soort</th><th>Hoe het werkt</th><th>Past bij</th><th>Let op</th></tr></thead>
<tbody>
<tr><td><strong>Acrylaat buitenmuurverf</strong></td><td>Kunsthars vormt een laag op de muur.</td><td>Eerder met acrylaat geverfde muren, beton, kleine oppervlakken.</td><td>Goedkoopst, maar minder dampopen. Niet ideaal op oude, vochtige muren.</td></tr>
<tr><td><strong>Siliconenharsverf</strong></td><td>Sterk waterafstotend, maar laat waterdamp goed door.</td><td>Pleisterwerk, metselwerk, eerder geverfde gevels.</td><td>Duurder, maar breed toepasbaar. Vuil hecht er minder aan.</td></tr>
<tr><td><strong>Silicaatverf</strong></td><td>Verbindt zich chemisch met de minerale ondergrond.</td><td>Kale baksteen, kalk- en cementpleister, natuursteen.</td><td>Hecht niet op oude kunststof verflagen. Vraagt vakkennis bij het verwerken.</td></tr>
</tbody></table></div>
<p>Sika beschrijft zijn silicaatgevelverf bijvoorbeeld als een verf voor minerale ondergronden, en levert daarnaast een siloxaanverf (een soort siliconenharsverf). Welke het beste past, hangt af van wat er nu op de muur zit. Een silicaatverf over een oude acrylaatlaag gaat niet; dan is siliconenharsverf meestal het veiligst.</p>"""),
("Waarom dampopen zo belangrijk is",
"""<p>In een buitenmuur zit altijd wat vocht: van regen, uit de grond of van binnenuit. Dat vocht moet als waterdamp naar buiten kunnen. Een dichte verflaag houdt het vast. Dan krijg je blazen in de verf, afbladderen, vorstschade aan de stenen of vochtplekken binnen. Een dampopen gevelverf laat damp door en houdt regen grotendeels tegen. Heb je binnen al vochtproblemen, los die dan eerst op voor je buiten gaat verven. Lees meer in <a href="/kennisbank/vochtige-muur/">vochtige muur</a>.</p>"""),
("Het juiste weer",
"""<p>Gevelverf heeft droog weer nodig, en een muur die zelf ook droog is. Veel gevelverven geven op het blik een minimum van ongeveer 5 tot 8 °C, voor zowel de lucht als de muur. Verf niet in de felle zon, niet als er nachtvorst of regen komt binnen een dag, en niet op een muur die nog nat is van de regen of van het reinigen. Na reinigen met water moet een muur vaak een paar droge dagen hebben. Wanneer het weer goed is, lees je in <a href="/gids/wanneer-buiten-schilderen/">wanneer kun je buiten schilderen</a>.</p>"""),
("Hoeveel verf heb je nodig?",
"""<p>Dat hangt sterk af van de ondergrond. Een gladde, eerder geverfde pleisterlaag neemt weinig op. Ruw metselwerk met diepe voegen zuigt veel meer verf op dan je verwacht. Reken met twee lagen en kijk naar het verbruik op het blik voor jouw soort muur. Reken het uit met <a href="/gids/verf-berekenen/">hoeveel verf heb je nodig</a> en neem wat extra voor ruwe muren.</p>"""),
("Wat vraag je de schilder?",
"""<ul>
<li>Welke gevelverf stelt hij voor, en is die dampopen? Vraag naar het productblad.</li>
<li>Past die verf op wat er nu op de muur zit?</li>
<li>Hoe wordt de gevel gereinigd, en worden scheuren en losse voegen eerst hersteld?</li>
<li>Is er een grondlaag nodig, en hoeveel lagen gevelverf komen erop?</li>
<li>Zit de steiger of hoogwerker in de prijs?</li>
<li>Wat is zijn advies over onderhoud: na hoeveel jaar moet de gevel opnieuw?</li>
</ul>"""),
("Rekenvoorbeeld: tussenwoning met geverfde gevel",
"""<p>Een tussenwoning heeft voor en achter samen zo'n 50 m² geverfde muur, na aftrek van ramen en deuren. Een schilder rekent €20 tot €40 per m², inclusief gevelverf en btw: €1.000 tot €2.000. Reinigen vooraf kost €5 tot €20 per m² als dat niet in de prijs zit. Voor de bovenverdieping komt er een steiger of hoogwerker bij, €300 tot €900 per gevel. Laat de kozijnen in dezelfde ronde doen, dan deel je de steiger; zie <a href="/kosten/kozijnen-schilderen/">kozijnen schilderen</a>.</p>"""),
],
"stappen": [
("Kijk of verven nodig is", "Schoon metselwerk laat je meestal kaal. Verf wel als de gevel al geverfd is of uit pleisterwerk bestaat."),
("Reinig de gevel", "Verwijder vuil, algen en mos. Laat de muur daarna een paar dagen drogen."),
("Herstel de muur", "Schraap losse verf weg, vul scheuren en herstel losse voegen of pleisterwerk."),
("Kies de verf", "Dampopen gevelverf die past bij de ondergrond: siliconenhars, silicaat of acrylaat."),
("Gron waar nodig", "Zet een grondlaag op kale, zuigende of poederende plekken volgens het productblad."),
("Verf twee lagen", "Bij droog weer, boven de minimumtemperatuur op het blik en niet in de felle zon."),
],
"kosten": ["gevel-schilderen", "gevel-reinigen-impregneren"],
"dienst": "buitenschilderwerk",
"faq": [
("Welke verf gebruik je voor een buitenmuur?", "Een dampopen gevelverf. Siliconenharsverf past op de meeste pleister- en eerder geverfde gevels. Silicaatverf op kale minerale ondergronden."),
("Wat betekent dampopen?", "Dat de verf waterdamp uit de muur doorlaat, terwijl hij regen grotendeels tegenhoudt. Zo kan de muur drogen."),
("Kun je een bakstenen muur verven?", "Het kan, met een dampopen gevelverf. Maar schoon metselwerk laat je meestal kaal: na verven moet je blijven onderhouden."),
("Bij welke temperatuur kun je een buitenmuur verven?", "Volg het blik. Veel gevelverven vragen minimaal zo'n 5 tot 8 °C voor de lucht én de muur, en geen regen of vorst binnen een dag."),
("Hoe vaak moet een geverfde gevel opnieuw?", "Gemiddeld na acht tot twaalf jaar, afhankelijk van de verf, de ligging en het onderhoud."),
("Kun je silicaatverf over oude verf zetten?", "Meestal niet. Silicaatverf hecht chemisch op minerale ondergronden, niet op oude kunststof verflagen. Dan is siliconenharsverf beter."),
("Wat kost een buitenmuur laten verven?", "€20 tot €40 per m², inclusief gevelverf en btw. Een steiger kost €300 tot €900 per gevel extra."),
],
"bronnen": [SIKA_SILICAAT, SIKA_SILOXAAN, KNB_HYDROFOBEREN],
"gerelateerd": ["gevel-impregneren", "vochtige-muur", "hoe-vaak-buitenschilderwerk"],
"extra_links": [("/gids/wanneer-buiten-schilderen/", "Wanneer kun je buiten schilderen?")],
},
# ---------------------------------------------------------------------------
{
"slug": "gevel-impregneren",
"groep": "Schade en onderhoud",
"titel": "Gevel impregneren: wanneer helpt het en wanneer niet?",
"seo_titel": "Gevel impregneren: wanneer helpt het en wanneer niet?",
"description": "Je gevel laten impregneren of hydrofoberen? Wat het doet, wanneer het helpt tegen vocht en wanneer het juist schade geeft, hoe lang het werkt en wat het kost.",
"kort": "Wat impregneren doet, wanneer het helpt en wanneer je het beter niet doet.",
"foto": "nederlandse-rijtjeswoningen-hoorn",
"intro": "Impregneren wordt vaak aangeprezen als de oplossing voor een natte of groene gevel. Een middel in de steen zorgt dat regen eraf parelt. Dat kan goed werken, maar het is geen wondermiddel. Op de verkeerde muur, of met vocht dat niet van buiten komt, kan het juist schade geven. Hier lees je wanneer impregneren zinvol is en waar je op let.",
"kort_antwoord": "Impregneren (ook hydrofoberen genoemd) maakt metselwerk waterafstotend, zonder de poriën dicht te maken. Het helpt als regen van buiten de muur in trekt, bijvoorbeeld bij een westgevel die vaak nat is. Het helpt niet tegen opstijgend vocht of condens binnen, en scheuren en kapotte voegen moeten eerst hersteld zijn. Laat altijd eerst de oorzaak van het vocht vaststellen. Alleen impregneren kost €5 tot €15 per m², reinigen en impregneren samen €12 tot €32 per m².",
"secties": [
("Wat doet impregneren precies?",
"""<p>Bij impregneren spuit of rolt de vakman een vloeistof of crème op de steen en de voegen. Het middel trekt een paar millimeter de steen in en maakt de poriën van binnen waterafstotend. De poriën blijven open, dus waterdamp kan er nog uit. Je ziet het bijna niet, maar regen parelt van de muur af in plaats van erin te trekken.</p>
<p>Een impregneermiddel is dus iets anders dan verf of een coating. Verf vormt een laag óp de muur. Een goed impregneermiddel zit ín de steen en verandert het uiterlijk nauwelijks. Wil je je gevel een kleur geven, dan heb je gevelverf nodig; zie <a href="/kennisbank/buitenmuur-verven/">buitenmuur verven</a>.</p>"""),
("Wanneer helpt het?",
"""<ul>
<li><strong>Doorslaand vocht door regen.</strong> Een gevel op het westen of zuidwesten die bij slagregen nat wordt, met vochtplekken binnen die na een regenbui erger worden.</li>
<li><strong>Een gevel die snel groen wordt.</strong> Een droge muur geeft algen en mos minder kans.</li>
<li><strong>Na het reinigen van de gevel.</strong> Een schone gevel blijft langer schoon als hij minder water opneemt.</li>
<li><strong>Bij spouwmuurisolatie</strong> kan het buitenblad droger blijven. Vraag het isolatiebedrijf om advies.</li>
</ul>"""),
("Wanneer helpt het niet, of is het riskant?",
"""<p>Onderzoekers van TU Delft en TNO schrijven dat een waterwerende behandeling alleen zinvol is als het water van buiten komt. Een behandelde muur droogt langzamer als er tóch water in komt. Dan neemt de kans op vorstschade en schimmel juist toe. Het Kennisnetwerk Baksteenmetselwerk wijst er ook op dat je een gevel altijd als geheel moet behandelen, niet in stukjes.</p>
<ul>
<li><strong>Opstijgend vocht</strong> uit de grond: impregneren houdt het vocht dan juist in de muur. Hier is een andere aanpak nodig, zie <a href="/kennisbank/vochtige-muur/">vochtige muur</a>.</li>
<li><strong>Condens of schimmel binnen</strong> door te weinig ventileren: daar doet de buitenkant niets aan.</li>
<li><strong>Scheuren en kapotte voegen</strong>: water loopt er dan nog steeds in. Eerst repareren.</li>
<li><strong>Zoutuitbloei</strong> (witte aanslag): zouten kunnen achter de behandelde laag kristalliseren en de steen beschadigen.</li>
<li><strong>Monumenten en oude, zachte steen</strong>: in sommige gemeenten mag het niet zonder overleg. Vraag het na.</li>
</ul>"""),
("Hoe lang werkt het?",
"""<p>Een goede impregnering werkt meestal jaren, maar niet voor altijd. Zon en regen breken het middel langzaam af. Fabrikanten en vakmensen noemen vaak een periode van ongeveer vijf tot tien jaar, afhankelijk van het middel en de ligging van de gevel. Test het zelf: spuit wat water op de muur. Parelt het niet meer af maar trekt het in, dan is de werking minder geworden.</p>"""),
("Het juiste moment",
"""<p>Impregneren gebeurt op een schone en droge muur. Na reinigen met water moet de gevel eerst een paar droge dagen hebben. Ook het weer moet droog zijn, zonder vorst. Laat voegwerk en scheuren altijd eerst herstellen. Nieuw voegwerk moet uitgehard zijn voordat het geïmpregneerd wordt; vraag de vakman hoe lang dat duurt.</p>"""),
("Wat vraag je de vakman?",
"""<ul>
<li>Waar komt het vocht volgens hem vandaan, en hoe heeft hij dat vastgesteld?</li>
<li>Welk middel gebruikt hij (vloeistof of crème, op basis van silaan of siloxaan), en is het dampopen?</li>
<li>Worden scheuren en voegen eerst hersteld, en zit dat in de prijs?</li>
<li>Wordt de hele gevel behandeld?</li>
<li>Hoe lang werkt het middel volgens de fabrikant, en geeft hij garantie?</li>
<li>Zit hoogwerker of steiger in de prijs?</li>
</ul>"""),
("Rekenvoorbeeld: westgevel van een hoekwoning",
"""<p>De zijgevel van een hoekwoning ligt op het westen en is 40 m² groot. Binnen ontstaan na regen vochtplekken. De vakman reinigt de gevel, vervangt een paar kapotte voegen en impregneert de muur. Reinigen en impregneren samen kost €12 tot €32 per m², dus €480 tot €1.280. Alleen impregneren, als de muur al schoon is, kost €5 tot €15 per m²: €200 tot €600. Voegwerk herstellen komt erbij. Voor een hoge gevel komt er een hoogwerker of steiger bij.</p>"""),
],
"stappen": [
("Laat de oorzaak vaststellen", "Komt het vocht van buiten (regen), uit de grond of van binnen (condens)? Alleen bij regen helpt impregneren."),
("Herstel de gevel", "Repareer scheuren en kapotte voegen. Laat nieuw voegwerk uitharden."),
("Reinig de gevel", "Verwijder vuil, algen en mos, en laat de muur daarna een paar dagen drogen."),
("Bescherm ramen en kozijnen", "Glas, kozijnen en planten worden afgedekt, omdat het middel daar vlekken kan geven."),
("Breng het middel aan", "Op de hele gevel, bij droog weer zonder vorst, in de hoeveelheid die het productblad noemt."),
("Controleer de werking", "Spuit na een paar weken water op de muur: het moet afparelen. Herhaal de test om de paar jaar."),
],
"kosten": ["gevel-reinigen-impregneren", "gevel-schilderen"],
"dienst": "buitenschilderwerk",
"faq": [
("Wat is het verschil tussen impregneren en hydrofoberen?", "In de praktijk betekent het hetzelfde: de steen waterafstotend maken zonder de poriën dicht te maken."),
("Helpt impregneren tegen vochtige muren binnen?", "Alleen als het vocht door regen van buiten komt. Tegen opstijgend vocht en condens helpt het niet, en het kan het zelfs erger maken."),
("Hoe lang werkt een impregnering?", "Meestal jaren, vaak genoemd wordt vijf tot tien jaar, afhankelijk van het middel en de ligging. Test met water of het nog afparelt."),
("Verandert de kleur van de gevel door impregneren?", "Een goed middel verandert het uiterlijk nauwelijks. Soms wordt de steen iets donkerder. Vraag om een proefvlak."),
("Kan ik mijn gevel zelf impregneren?", "Het kan, maar alleen op een schone, droge gevel zonder scheuren en als de oorzaak van het vocht duidelijk van buiten komt. Bij twijfel laat je een vakman kijken."),
("Mag je een monument impregneren?", "Vaak alleen na overleg met de gemeente, omdat oude steen er schade van kan krijgen. Vraag het na voordat je begint."),
("Wat kost gevel impregneren?", "Alleen impregneren kost €5 tot €15 per m². Reinigen en impregneren samen €12 tot €32 per m²."),
],
"bronnen": [TUD_HYDROFOBEREN, KNB_HYDROFOBEREN, CONSUMENTENBOND_VOCHT],
"gerelateerd": ["buitenmuur-verven", "vochtige-muur", "schimmel-op-muur"],
},
# ---------------------------------------------------------------------------
{
"slug": "vochtige-muur",
"groep": "Schade en onderhoud",
"titel": "Vochtige muur: oorzaak vinden, oplossen en daarna schilderen",
"seo_titel": "Vochtige muur: oorzaak, oplossing en schilderen",
"description": "Een vochtige muur binnen? Zo herken je opstijgend vocht, doorslaand vocht en condens, wat je eraan doet en wanneer en hoe je de muur weer kunt schilderen.",
"kort": "Opstijgend vocht, doorslaand vocht of condens: hoe je de oorzaak vindt en wanneer je weer kunt schilderen.",
"foto": "muur-verven-met-roller-zwartwit",
"intro": "Een vochtige plek op de muur, verf die bladdert of een muffe lucht: dat wil je snel weg hebben. De eerste reactie is vaak er een laagje verf overheen zetten. Maar zolang het vocht blijft, komt de plek terug, vaak met schimmel erbij. Eerst moet je weten waar het vocht vandaan komt. Hier lees je hoe je de drie bekendste oorzaken herkent, wat je eraan doet en hoe je daarna schildert.",
"kort_antwoord": "Een vochtige muur heeft bijna altijd één van drie oorzaken: opstijgend vocht uit de grond (onderaan de muur), doorslaand vocht door regen (hoger op een buitenmuur, erger na regen) of condens van binnenuit (op koude plekken, in hoeken en achter kasten). Los eerst de oorzaak op en laat de muur goed drogen. Daarna behandel je zoutplekken, zet je een voorstrijk en schilder je met een dampopen muurverf. Verf over een natte muur helpt niet.",
"secties": [
("Drie oorzaken herkennen",
"""<div class="tablewrap"><table>
<thead><tr><th>Oorzaak</th><th>Waar zie je het?</th><th>Typische kenmerken</th></tr></thead>
<tbody>
<tr><td><strong>Opstijgend vocht</strong></td><td>Onderaan de muur, tot zo'n halve tot één meter hoog.</td><td>Een vochtige rand met een duidelijke lijn, witte zoutkorrels, bladderende verf vlak boven de plint. Vooral in oudere huizen en kelders.</td></tr>
<tr><td><strong>Doorslaand vocht</strong></td><td>Op een buitenmuur, vaak hoger op de muur of rond een kozijn.</td><td>Wordt erger na regen, vooral bij een gevel op het westen. Vaak door scheuren, kapotte voegen of een lekkende dakgoot.</td></tr>
<tr><td><strong>Condens</strong></td><td>Koude plekken: hoeken, achter kasten, rond ramen, in badkamer en slaapkamer.</td><td>Zwarte puntjes schimmel, beslagen ramen, erger in de winter. Komt door vochtige lucht en te weinig ventilatie.</td></tr>
</tbody></table></div>
<p>De Consumentenbond noemt als meest voorkomende oorzaken te veel vocht in de lucht, te weinig ventilatie, slechte isolatie, lekkage, en doorslaand of optrekkend vocht. Een lekkende leiding in de muur kan ook; die herken je aan een plek die steeds groter wordt, los van het weer.</p>"""),
("Wat doe je eraan?",
"""<p><strong>Condens:</strong> ventileer elke dag, houd roosters open, zet de afzuiging aan bij koken en douchen en stook de woning gelijkmatig. Zet kasten een paar centimeter van de buitenmuur af. De Rijksoverheid en het RIVM geven daar praktische tips over. Schimmel die al op de muur zit, pak je aan zoals beschreven in <a href="/kennisbank/schimmel-op-muur/">schimmel op de muur</a>.</p>
<p><strong>Doorslaand vocht:</strong> laat de buitenkant controleren. Herstel scheuren, voegen, dakgoten en kitranden rond kozijnen. Komt regen door de steen zelf, dan kan impregneren helpen; lees eerst <a href="/kennisbank/gevel-impregneren/">gevel impregneren</a>.</p>
<p><strong>Opstijgend vocht:</strong> dit is werk voor een vochtbestrijdingsbedrijf. Meestal wordt er een vochtwerende laag in de muur gemaakt, bijvoorbeeld door een injectie onderaan de muur. Een schilder lost dit niet op. Laat je goed informeren voordat je kiest; de oorzaak moet echt vaststaan.</p>"""),
("Hoe lang moet de muur drogen?",
"""<p>Een muur die lang nat is geweest, heeft tijd nodig. Een dunne binnenmuur droogt sneller dan een dikke steenmuur. Reken bij een natte muur eerder op weken dan op dagen, en na een injectie tegen opstijgend vocht soms op maanden. Een vochtmeter geeft houvast: een schilder of vochtbestrijder kan meten of de muur droog genoeg is. Goed ventileren en gewoon stoken helpen bij het drogen. Schilder niet op gevoel.</p>"""),
("Zoutplekken en kapotte pleister",
"""<p>Bij opstijgend en doorslaand vocht neemt het water zouten mee uit de steen. Als de muur droogt, blijven die achter als witte korrels of pluizen (ook wel salpeter genoemd). Op zoutplekken hecht verf slecht en komt de plek vaak terug.</p>
<ul>
<li>Borstel de zouten droog weg, niet nat.</li>
<li>Pleisterwerk dat zacht is of hol klinkt, moet eraf en opnieuw worden gezet, vaak met een speciale saneerpleister die tegen zout kan.</li>
<li>Gaatjes en kleine scheuren vul je pas als de muur droog is. Zie <a href="/kennisbank/muur-plamuren/">muur plamuren</a>.</li>
</ul>"""),
("Schilderen na vochtschade",
"""<p>Is de oorzaak opgelost en de muur droog, dan kun je schilderen. Kies een <strong>dampopen muurverf</strong>, zodat restvocht nog kan verdampen. Een dichte verf of een vochtwerende coating aan de binnenkant sluit het vocht juist op. Zijn er bruine randen of vlekken van het vocht, zet daar dan eerst een isolerende voorstrijk op, anders slaan ze door. Hoe dat gaat, lees je in <a href="/kennisbank/vlekken-overschilderen/">vlekken overschilderen</a>.</p>
<p>In vochtige ruimtes zoals de badkamer kun je een schimmelwerende muurverf gebruiken. Dat is een extra bescherming, geen oplossing voor een vochtprobleem.</p>"""),
("Wat vraag je de schilder?",
"""<ul>
<li>Is de oorzaak van het vocht opgelost, en is de muur droog genoeg? Hoe meet hij dat?</li>
<li>Moeten zoutplekken of kapot pleisterwerk eerst worden hersteld, en door wie?</li>
<li>Welke voorstrijk en welke dampopen muurverf gebruikt hij?</li>
<li>Komt er een isolerende laag op vochtvlekken?</li>
<li>Geeft hij garantie als het vocht terugkomt? Vaak niet, en dat is logisch als de oorzaak niet bij het schilderwerk ligt.</li>
</ul>"""),
("Rekenvoorbeeld: vochtige muur in de woonkamer",
"""<p>In een woonkamer is een strook van 6 meter lang en 1 meter hoog onderaan de buitenmuur vochtig geweest. Na het oplossen van de oorzaak en drogen wordt de hele muur van 15 m² opnieuw geschilderd, anders zie je verschil. Een schilder rekent €10 tot €16 per m² voor muren: €150 tot €240. Een isolerende laag op de vochtranden kost €2 tot €5 per m² extra, en kleine reparaties met plamuur €3 tot €8 per m². De vochtbestrijding zelf en eventueel nieuw pleisterwerk komen daar los bij.</p>"""),
],
"stappen": [
("Kijk waar het vocht zit", "Onderaan de muur, hoog op een buitenmuur na regen, of op koude plekken en achter kasten?"),
("Los de oorzaak op", "Ventileren bij condens, gevel herstellen bij doorslaand vocht, een vakbedrijf bij opstijgend vocht."),
("Laat de muur drogen", "Ventileer en stook gewoon. Laat zo nodig meten of de muur droog genoeg is."),
("Herstel de ondergrond", "Borstel zouten droog weg, laat kapot pleisterwerk vervangen en vul gaatjes."),
("Isoleer vlekken", "Zet een isolerende voorstrijk op vochtranden en bruine vlekken."),
("Schilder dampopen", "Gebruik een dampopen muurverf, twee lagen, op de hele muur."),
],
"kosten": ["schilderen-per-m2", "gevel-reinigen-impregneren"],
"faq": [
("Hoe weet ik of het opstijgend vocht is?", "Opstijgend vocht zit onderaan de muur, met een duidelijke vochtrand en vaak witte zoutkorrels. Het hangt niet af van regen of de winter."),
("Kun je een vochtige muur overschilderen?", "Niet zolang hij nat is. Los eerst de oorzaak op en laat de muur drogen. Anders bladdert de verf en komt de plek terug."),
("Helpt vochtwerende verf binnen?", "Meestal niet. Het vocht blijft in de muur zitten en zoekt een andere weg. Een dampopen verf na het oplossen van de oorzaak is beter."),
("Wat zijn de witte korrels op mijn muur?", "Zouten die het vocht uit de steen heeft meegenomen, vaak salpeter genoemd. Borstel ze droog weg en los het vocht op."),
("Hoe lang moet een muur drogen voor je kunt schilderen?", "Dat verschilt: van weken bij een binnenmuur tot maanden na vochtbestrijding van een dikke muur. Laat het meten."),
("Doet een schilder ook vochtbestrijding?", "Meestal niet. Voor opstijgend vocht schakel je een vochtbestrijdingsbedrijf in. De schilder doet het herstel en schilderwerk daarna."),
("Wat kost een muur opnieuw schilderen na vochtschade?", "€10 tot €16 per m² voor muren, plus €2 tot €5 per m² voor een isolerende laag op vochtranden. Vochtbestrijding komt erbij."),
],
"bronnen": [CONSUMENTENBOND_VOCHT, RIVM_FOLDER, RIJKSOVERHEID_VENTILEREN, ALAB_ALLES_IN_1],
"gerelateerd": ["schimmel-op-muur", "gevel-impregneren", "vlekken-overschilderen"],
},
# ---------------------------------------------------------------------------
{
"slug": "scheuren-in-muur-en-plafond",
"groep": "Schade en onderhoud",
"titel": "Scheuren in muur of plafond: zo repareer je ze voor het schilderen",
"seo_titel": "Scheuren in muur of plafond repareren",
"description": "Scheuren in je muur of plafond? Welke scheuren onschuldig zijn en welke niet, hoe je ze vult zodat ze niet terugkomen en wat het kost om te laten repareren.",
"kort": "Welke scheuren onschuldig zijn, welke niet, en hoe je ze vult zodat ze wegblijven.",
"foto": "nederlandse-kamer-balkenplafond-zwartwit",
"intro": "Bijna elk huis heeft wel ergens een scheur: een haarscheurtje in het plafond, een barst boven een deur of een naad die steeds weer openspringt. Voor je gaat schilderen, wil je die weg hebben. Maar vul je een scheur op de verkeerde manier, dan zie je hem na een winter gewoon weer. Hier lees je welke scheuren je zelf kunt repareren, hoe je dat doet en wanneer je beter een expert laat kijken.",
"kort_antwoord": "Haarscheurtjes in stucwerk en plafonds zijn meestal onschuldig: ze ontstaan door krimp en kleine bewegingen. Kras ze iets open, maak ze stofvrij, vul ze met muurvuller en schuur glad. Scheuren die steeds terugkomen, zoals naden van gipsplaten of de hoek tussen muur en plafond, vul je met een flexibele acrylaatkit of een flexibele scheurvuller. Brede scheuren, trapvormige scheuren in metselwerk of scheuren die groeien, laat je eerst door een bouwkundige bekijken. Een schilder rekent voor vullen en plamuren €3 tot €8 per m² extra.",
"secties": [
("Welke scheur heb je?",
"""<div class="tablewrap"><table>
<thead><tr><th>Soort scheur</th><th>Oorzaak</th><th>Aanpak</th></tr></thead>
<tbody>
<tr><td><strong>Haarscheurtjes in stucwerk</strong></td><td>Krimp van pleister, kleine temperatuurverschillen.</td><td>Openkrassen, vullen met muurvuller, schuren.</td></tr>
<tr><td><strong>Scheur langs een naad van gipsplaat</strong></td><td>De platen werken ten opzichte van elkaar.</td><td>Flexibele scheurvuller of wapeningsband, of glasvlies over de hele muur.</td></tr>
<tr><td><strong>Scheur in de hoek muur-plafond</strong></td><td>Muur en plafond bewegen apart, bijvoorbeeld een houten balklaag.</td><td>Een strakke rups overschilderbare acrylaatkit.</td></tr>
<tr><td><strong>Scheur boven deur of raam</strong></td><td>Spanning rond een opening of een latei die werkt.</td><td>Vaak flexibel vullen. Wordt hij breder, laat het dan bekijken.</td></tr>
<tr><td><strong>Brede of trapvormige scheur in metselwerk</strong></td><td>Zetting, funderingsproblemen of een constructieprobleem.</td><td>Niet zelf dichtsmeren. Eerst een bouwkundige laten kijken.</td></tr>
</tbody></table></div>"""),
("Wanneer moet je je zorgen maken?",
"""<p>De meeste scheuren zijn cosmetisch. Laat een bouwkundige of constructeur kijken als:</p>
<ul>
<li>een scheur breder is dan een paar millimeter;</li>
<li>hij trapvormig door de voegen van metselwerk loopt;</li>
<li>hij groeit, of er steeds nieuwe bij komen;</li>
<li>deuren en ramen gaan klemmen;</li>
<li>de scheur ook aan de buitenkant van de muur te zien is.</li>
</ul>
<p>Twijfel je of een scheur groeit? Zet er met potlood een streepje bij met de datum, en meet na een paar maanden of hij langer of breder is geworden. Maak ook een foto met een meetlint ernaast.</p>"""),
("Het juiste vulmiddel",
"""<p><strong>Muurvuller</strong> is voor gaatjes en scheurtjes die niet meer bewegen. Volgens de productinformatie is de Sneldrogende Muurvuller van Alabastine na ongeveer 30 minuten droog; de Superieure Muurvuller is bedoeld voor scheuren en kleine én grote gaten. Gewone muurvuller is na het drogen hard. Werkt de scheur nog, dan scheurt de vuller weer.</p>
<p><strong>Flexibele vullers en acrylaatkit</strong> blijven een beetje rekbaar. Daarmee vul je naden en hoeken die bewegen. Er zijn flexibele scheurvullers op acrylaatbasis, zoals de Scheuren &amp; Naden muurvuller die bouwmarkten verkopen. Gebruik altijd een kit die overschilderbaar is. Siliconenkit kun je niet overschilderen: verf parelt eraf.</p>"""),
("Scheuren in het plafond",
"""<p>In plafonds zie je vaak scheuren langs de naden van gipsplaten of spaanplaten, en langs de randen. Een houten balklaag werkt met de seizoenen mee. Een hard gevulde naad scheurt dan opnieuw. Voor zulke naden werkt een flexibele vuller, of een strook wapeningsband of glasvlies over de naad. Op een spachtelputz- of spuitplafond is een reparatie lastig onzichtbaar te maken. Vaak moet het hele plafond daarna opnieuw worden geschilderd. Zie <a href="/kennisbank/plafond-schilderen-zonder-strepen/">plafond schilderen zonder strepen</a>.</p>"""),
("Na het vullen: schilderen",
"""<p>Gevulde plekken zuigen anders dan de rest van de muur. Schilder je er direct overheen, dan zie je ze als matte of glanzende vlekken terug. Zet daarom eerst een voorstrijk of een extra laag muurverf op de gevulde plekken, en schilder daarna de hele muur of het hele plafond. Een stukje bijwerken valt bijna altijd op. Meer over vullen en plamuren in <a href="/kennisbank/muur-plamuren/">muur plamuren</a>; wil je een muur met veel scheurtjes in één keer strak, kijk dan naar <a href="/kennisbank/renovlies-of-glasvlies/">renovlies of glasvlies</a>.</p>"""),
("Wat vraag je de schilder?",
"""<ul>
<li>Welke scheuren vult hij met muurvuller, en welke met een flexibele vuller of kit?</li>
<li>Zit het vullen en plamuren in de prijs per m², of komt het erbij?</li>
<li>Komt er een voorstrijk op de gevulde plekken?</li>
<li>Schildert hij daarna de hele muur of het hele plafond?</li>
<li>Ziet hij scheuren waarvoor hij een bouwkundige zou laten kijken?</li>
</ul>"""),
("Rekenvoorbeeld: plafond met scheuren langs de naden",
"""<p>Een woonkamerplafond van 35 m² heeft scheuren langs de naden van de platen. De schilder vult ze flexibel, zet een voorstrijk op de reparaties en schildert het plafond twee keer. Een plafond schilderen kost €12 tot €22 per m², dus €420 tot €770. Scheuren en naden repareren kost €3 tot €8 per m² extra: €105 tot €280. Samen zo'n €525 tot €1.050, inclusief materiaal en btw.</p>"""),
],
"stappen": [
("Beoordeel de scheur", "Haarscheurtje of naad: zelf te repareren. Breed, trapvormig of groeiend: eerst een bouwkundige."),
("Kras de scheur open", "Maak hem met een schraper of mesje iets breder in V-vorm, zodat de vuller houvast heeft."),
("Maak stofvrij", "Borstel of zuig het stof weg en maak de scheur licht vochtig als de vuller dat vraagt."),
("Vul met het juiste middel", "Muurvuller voor scheuren die stilstaan, flexibele vuller of overschilderbare acrylaatkit voor naden en hoeken."),
("Schuur glad", "Na het drogen glad schuren en zo nodig een tweede keer vullen."),
("Voorstrijken en schilderen", "Voorstrijk op de gevulde plekken, daarna de hele muur of het hele plafond schilderen."),
],
"kosten": ["plafond-schilderen", "schilderen-per-m2"],
"dienst": "binnenschilderwerk",
"faq": [
("Zijn scheuren in de muur gevaarlijk?", "Haarscheurtjes in stucwerk meestal niet. Brede, trapvormige of groeiende scheuren kunnen wijzen op een constructieprobleem. Laat die bekijken."),
("Waarmee vul je scheuren in de muur?", "Muurvuller voor scheuren die niet meer bewegen. Een flexibele scheurvuller of overschilderbare acrylaatkit voor naden en hoeken die werken."),
("Waarom komt een gevulde scheur terug?", "Omdat de scheur nog beweegt en harde muurvuller niet meegeeft. Gebruik dan een flexibel middel of wapeningsband."),
("Kun je een scheur in het plafond met kit vullen?", "In de hoek tussen muur en plafond werkt overschilderbare acrylaatkit goed. Midden in het plafond is een flexibele vuller beter."),
("Kun je siliconenkit overschilderen?", "Nee, verf hecht niet op siliconenkit. Gebruik acrylaatkit als je wilt schilderen."),
("Moet je na het vullen de hele muur schilderen?", "Meestal wel. Gevulde plekken en bijgewerkte stukken vallen anders op als matte of glanzende vlekken."),
("Wat kost scheuren laten repareren?", "Vullen en plamuren kost €3 tot €8 per m² extra bovenop het schilderen. Een plafond schilderen kost €12 tot €22 per m²."),
],
"bronnen": [ALAB_MUURVULLER_SNEL, ALAB_SUPERIEUR, GAMMA_SCHEUREN_NADEN, TDS_VOORSTRIJK],
"gerelateerd": ["muur-plamuren", "plafond-schilderen-zonder-strepen", "renovlies-of-glasvlies"],
},
# ---------------------------------------------------------------------------
{
"slug": "vlekken-overschilderen",
"groep": "Schade en onderhoud",
"titel": "Nicotine, waterschade en roet: vlekken overschilderen zonder doorslaan",
"seo_titel": "Nicotine en vlekken overschilderen zonder doorslaan",
"description": "Nicotineaanslag, een waterschadevlek of roet op muur of plafond? Zo maak je het schoon en isoleer je de vlek, zodat hij niet door de nieuwe verf heen komt.",
"kort": "Hoe je nicotine, water- en roetvlekken schoonmaakt en isoleert, zodat ze niet doorslaan.",
"foto": "verfroller-close-up-in-verfbak",
"intro": "Je schildert een vergeelde muur of een plafond met een lekkagevlek, en een dag later zie je de vlek gewoon weer door de verse verf heen. Dat heet doorslaan. Het gebeurt bij nicotine, waterschade, roet, vet en sommige soorten stift. Gewone muurverf houdt die stoffen niet tegen. Met de juiste voorbereiding en een isolerende voorstrijk lukt het wel.",
"kort_antwoord": "Was de muur of het plafond eerst grondig met een ontvetter of verfreiniger en laat drogen. Bij waterschade moet de oorzaak opgelost en het plafond droog zijn. Zet daarna een isolerende voorstrijk (vlekkenprimer) op de vlekken of op het hele vlak, en schilder pas dan twee lagen muurverf. Een schilder rekent €10 tot €22 per m² voor het schilderen, plus €2 tot €5 per m² voor de isolerende laag.",
"secties": [
("Waarom slaan vlekken door?",
"""<p>Nicotine, teer, roet en de bruine randen van waterschade bevatten stoffen die oplossen in het water van muurverf. Ze trekken mee naar boven als de verf droogt. Na een paar uur of een dag zie je een gele of bruine schaduw verschijnen. Een extra laag gewone muurverf helpt meestal niet: de vlek trekt ook daar weer doorheen.</p>
<p>Een <strong>isolerende voorstrijk</strong> sluit de vlek af. Volgens de productinformatie van Alabastine isoleert hun Voorstrijk Alles in 1 onverdund nicotine-, roet-, teer- en lekkagevlekken. Er zijn ook isolerende voorstrijken op terpentinebasis, die het sterkst isoleren; Hornbach noemt bij de Xtra Voorstrijk Vlekken een verbruik van ongeveer 8 m² per liter. Daarnaast bestaat muurverf met een isolerende werking erin, zoals de 2-in-1 Muurverf Vlekken. De fabrikant adviseert bij sterk vervuilde muren, zoals bij nicotine, wel eerst te reinigen.</p>"""),
("Nicotine en rookaanslag",
"""<p>Nicotine geeft een gele tot bruine, plakkerige laag, vaak het sterkst op het plafond en boven radiatoren. Daar is reinigen de belangrijkste stap. Zonder schoonmaken blijft de verf slecht hechten.</p>
<ul>
<li>Was muur en plafond met een ontvetter of verfreiniger en warm water. Werk van onder naar boven, zodat er geen strepen over vuile delen lopen.</li>
<li>Spoel na met schoon water en laat alles goed drogen.</li>
<li>Zet een isolerende voorstrijk op het hele vlak. Bij nicotine zit de aanslag overal, ook waar je het niet ziet.</li>
<li>Schilder twee lagen muurverf. Lucht het huis goed; de rooklucht zit ook in gordijnen, vloer en meubels.</li>
</ul>
<p>Lakwerk, zoals deuren en kozijnen, vergeelt ook. Dat moet je ontvetten, opschuren en opnieuw lakken. Zie <a href="/kennisbank/binnendeuren-verven/">binnendeuren verven</a>.</p>"""),
("Waterschade aan plafond of muur",
"""<p>Een lekkage laat een bruine rand achter, ook als het water allang weg is. Begin altijd bij de oorzaak: een lekkende leiding, douche, dakgoot of dak. Pas als dat gemaakt is, heeft schilderen zin.</p>
<ul>
<li>Laat het plafond helemaal drogen. Een gipsplaat die doorweekt is geweest, kan slap worden; die moet soms vervangen worden.</li>
<li>Verwijder losse verf en losse stukjes stucwerk en vul ze.</li>
<li>Zet een isolerende voorstrijk op de vlek en een stukje eromheen.</li>
<li>Schilder daarna het hele plafond. Alleen de vlek bijwerken valt bijna altijd op.</li>
</ul>
<p>Is er ook schimmel ontstaan, behandel die dan eerst; zie <a href="/kennisbank/schimmel-op-muur/">schimmel op de muur</a>. Waterschade valt soms onder je opstalverzekering. Maak foto's voor je gaat herstellen en vraag het na bij je verzekeraar.</p>"""),
("Roet, vet en andere vlekken",
"""<p><strong>Roet</strong> van kaarsen, een open haard of een kleine brand zit vet en zwart op muren en plafonds. Veeg losse roet eerst droog weg met een roetspons, anders smeer je het uit. Daarna ontvetten en isoleren.</p>
<p><strong>Vet</strong> boven het fornuis moet er goed af met ontvetter. <strong>Stift, ballpoint en krijt</strong> van kinderen kun je meestal met een paar streken isolerende voorstrijk afdekken. <strong>Roest</strong> van een spijker of beugel: haal de bron weg of behandel hem, anders komt de roestvlek terug.</p>"""),
("Wat vraag je de schilder?",
"""<ul>
<li>Hoe wordt de muur of het plafond eerst gereinigd, en zit dat in de prijs?</li>
<li>Welke isolerende voorstrijk gebruikt hij: op water- of terpentinebasis?</li>
<li>Komt die alleen op de vlekken of op het hele vlak?</li>
<li>Bij waterschade: is het plafond droog genoeg, en moet er iets vervangen worden?</li>
<li>Wordt daarna het hele vlak geschilderd, met hoeveel lagen?</li>
</ul>"""),
("Rekenvoorbeeld: woning van een roker opknappen",
"""<p>In een appartement waar jaren is gerookt, moeten de woonkamer en slaapkamer opnieuw: samen zo'n 90 m² muur en 35 m² plafond. De schilder reinigt alles, zet een isolerende voorstrijk op het hele vlak en schildert twee lagen. Muren kosten €10 tot €16 per m² en plafonds €12 tot €22 per m², samen €1.320 tot €2.210. De isolerende laag kost €2 tot €5 per m² extra, voor 125 m² dus €250 tot €625. Reinigen bij zware aanslag kan erbij komen, vaak op uurbasis.</p>"""),
],
"stappen": [
("Los de oorzaak op", "Bij waterschade eerst de lekkage laten maken en het plafond laten drogen."),
("Verwijder losse roet en vuil", "Veeg roet droog weg met een roetspons en schraap losse verf weg."),
("Ontvet en reinig", "Was met ontvetter of verfreiniger en warm water, spoel na en laat goed drogen."),
("Herstel kleine schade", "Vul gaatjes en losse plekken en schuur ze glad."),
("Isoleer de vlekken", "Zet een isolerende voorstrijk op de vlekken, bij nicotine op het hele vlak. Laat drogen volgens het blik."),
("Schilder het hele vlak", "Twee lagen muurverf op de hele muur of het hele plafond, niet alleen op de vlek."),
],
"kosten": ["schilderen-per-m2", "plafond-schilderen"],
"dienst": "binnenschilderwerk",
"faq": [
("Waarom komt een vlek door de verf heen?", "Stoffen in nicotine, roet en waterschade lossen op in het water van de muurverf en trekken mee naar boven. Een isolerende voorstrijk houdt ze tegen."),
("Hoe verwijder je nicotine van de muur?", "Was met een ontvetter of verfreiniger en warm water, van onder naar boven, en spoel na. Daarna isoleren en schilderen."),
("Wat is een isolerende voorstrijk?", "Een grondlaag die vlekken afsluit, zodat ze niet door de nieuwe verf heen komen. Er zijn soorten op water- en op terpentinebasis."),
("Kun je een waterschadevlek gewoon overschilderen?", "Niet met gewone muurverf: de bruine rand slaat door. Los de lekkage op, laat drogen, isoleer de vlek en schilder het hele plafond."),
("Moet het hele plafond geschilderd worden na een vlek?", "Meestal wel. Een bijgewerkte plek valt op, ook in dezelfde kleur."),
("Betaalt de verzekering het schilderen na waterschade?", "Soms, afhankelijk van je polis en de oorzaak. Maak foto's en vraag het na voordat je gaat herstellen."),
("Wat kost vlekken laten overschilderen?", "Schilderen kost €10 tot €22 per m², plus €2 tot €5 per m² voor een isolerende voorstrijk. Reinigen bij zware aanslag kan erbij komen."),
],
"bronnen": [ALAB_ALLES_IN_1, ALAB_2IN1_VLEKKEN, HORNBACH_XTRA_VLEKKEN, TDS_MUURVERF],
"gerelateerd": ["schimmel-op-muur", "plafond-schilderen-zonder-strepen", "vochtige-muur"],
},
# ---------------------------------------------------------------------------
{
"slug": "kalkverf-of-krijtverf",
"groep": "Verf kiezen",
"titel": "Kalkverf of krijtverf: wat is het verschil en wanneer kies je het?",
"seo_titel": "Kalkverf of krijtverf? Verschil en toepassing",
"description": "Kalkverf en krijtverf geven een zachte, matte muur met een wolkig effect. Wat is het verschil, op welke ondergrond kan het, hoe breng je het aan en wat kost het?",
"kort": "Het verschil tussen kalkverf, krijtverf en kalkmatte muurverf, en hoe je ze aanbrengt.",
"foto": "muur-afplakken-en-verven-gele-kleur",
"intro": "Kalkverf en krijtverf zijn populair voor een warme, stoffige uitstraling op de muur, met kleurverschillen die je bij gewone muurverf niet ziet. Ze worden vaak in één adem genoemd, maar ze werken anders. Ook de ondergrond, de manier van aanbrengen en het onderhoud verschillen van gewone muurverf. Hier lees je wat je kiest en waar je op let.",
"kort_antwoord": "Kalkverf is gemaakt van gebluste kalk en geeft een wolkig, levendig effect dat met het licht verandert. Het is dampopen en hecht het best op minerale ondergronden zoals kalk- of cementpleister en steen; op andere ondergronden is een speciale primer nodig. Krijtverf is een zeer matte verf met een egale, poederachtige uitstraling, die op meer ondergronden kan, ook op hout en meubels. Beide zijn minder goed afwasbaar dan gewone muurverf. Wil je de look zonder gedoe, kies dan een kalkmatte muurverf. Een schilder rekent ongeveer €10 tot €22 per m², bij kalkverf door het vele handwerk vaak aan de bovenkant.",
"secties": [
("Drie soorten naast elkaar",
"""<div class="tablewrap"><table>
<thead><tr><th>Soort</th><th>Uitstraling</th><th>Ondergrond</th><th>Afwasbaar</th></tr></thead>
<tbody>
<tr><td><strong>Kalkverf</strong></td><td>Wolkig, met kleurverschillen en diepte. Elk vlak is anders.</td><td>Minerale ondergronden; met de juiste primer ook gipsplaat en eerder geverfde muren.</td><td>Matig. Vlekken zijn lastig weg te krijgen.</td></tr>
<tr><td><strong>Krijtverf</strong></td><td>Zeer mat en poederachtig, vrij egaal.</td><td>Muren, maar ook hout en meubels.</td><td>Matig; op meubels vaak afgewerkt met was of vernis.</td></tr>
<tr><td><strong>Kalkmatte muurverf</strong></td><td>Diepmat, iets kalkachtig, maar egaal.</td><td>Zoals gewone muurverf.</td><td>Beter dan echte kalkverf.</td></tr>
</tbody></table></div>
<p>Pure &amp; Original noemt in het kenmerkenblad van zijn Classico krijtverf onder meer kalkpleister, cementpleister, metselwerk, gipsplaten en hout als geschikte ondergrond. Histor verkoopt een muurverf met een kalkmatte look die je net zo verwerkt als gewone muurverf.</p>"""),
("Op welke muur kan het?",
"""<p>Echte kalkverf hecht het best op een kale, minerale ondergrond die ademt: kalkpleister, cementpleister, steen of oud stucwerk. Op een muur met latex of gewone muurverf, of op glad gipsplaat, heb je eerst een speciale primer nodig. Die geeft de kalkverf iets om zich aan vast te hechten. Sla je die over, dan kan de kalkverf gaan poederen of loslaten. Op glasvlies wordt kalkverf vaak afgeraden; zie <a href="/kennisbank/renovlies-of-glasvlies/">renovlies of glasvlies</a>.</p>
<p>Omdat kalkverf dampopen is, wordt hij veel gebruikt in oude huizen met kalkpleister en op muren die moeten kunnen ademen. Een vochtprobleem los je er niet mee op; dat moet eerst. Zie <a href="/kennisbank/vochtige-muur/">vochtige muur</a>.</p>"""),
("Hoe breng je kalkverf aan?",
"""<p>Kalkverf breng je meestal aan met een grote, platte <strong>blokkwast</strong>, niet met een roller. Je werkt in kruislingse streken, in vlakken van ongeveer een vierkante meter, en laat de streken bewust zichtbaar. Zo ontstaat het wolkige effect. Meestal komen er twee lagen op.</p>
<ul>
<li>De verf droogt veel lichter op dan hij nat lijkt. Schrik niet als hij in het begin donker en vlekkerig is.</li>
<li>Werk een hele wand in één keer af, zonder pauze, anders zie je aanzetten.</li>
<li>Bestel genoeg verf uit één batch. Kleurverschil tussen blikken valt bij kalkverf sneller op.</li>
<li>Bescherm vloer en kozijnen goed: kalkverf spat en is lastig te verwijderen van hout.</li>
</ul>
<p>Krijtverf en kalkmatte muurverf kun je ook met een roller aanbrengen. Dan wordt het resultaat egaler.</p>"""),
("Onderhoud en schoonmaken",
"""<p>Kalkverf en krijtverf zijn minder goed bestand tegen schrobben dan gewone muurverf. Een vette vinger of een koffiespat is lastig weg te krijgen zonder dat er een vlek ontstaat. Kies het daarom liever niet voor een drukke gang, een kinderkamer of de muur achter het fornuis. Bijwerken kan wel: met kalkverf valt een bijgewerkte plek door het wolkige effect minder op dan bij egale verf. Wil je een makkelijk afwasbare muur, lees dan <a href="/kennisbank/latex-of-muurverf/">latex of muurverf</a>.</p>"""),
("Wat vraag je de schilder?",
"""<ul>
<li>Heeft hij ervaring met kalkverf? Het aanbrengen is echt anders dan gewone muurverf.</li>
<li>Welke primer zet hij eerst, en is die geschikt voor mijn ondergrond?</li>
<li>Kan hij een proefvlak maken, zodat ik het effect en de kleur zie?</li>
<li>Hoeveel lagen komen erop, en wordt elke wand in één keer afgewerkt?</li>
<li>Hoe moet ik de muur later schoonmaken of bijwerken?</li>
</ul>"""),
("Rekenvoorbeeld: slaapkamer in kalkverf",
"""<p>Een slaapkamer heeft 33 m² muur. De schilder zet een primer en twee lagen kalkverf met een blokkwast. Gewone muren kosten €10 tot €16 per m², inclusief verf en btw. Kalkverf is per liter duurder en het aanbrengen kost meer tijd, dus reken eerder op de bovenkant van de bandbreedte voor binnenschilderwerk, rond €16 tot €22 per m². Dat is €530 tot €730. Een kalkmatte muurverf die gerold wordt, zit dichter bij de prijs van gewone muurverf.</p>"""),
],
"stappen": [
("Kies je verf", "Echte kalkverf voor het wolkige effect, krijtverf voor diepmat en meubels, kalkmatte muurverf voor de look zonder gedoe."),
("Bekijk de ondergrond", "Minerale ondergrond: vaak direct. Latex, muurverf of gipsplaat: eerst een speciale primer."),
("Maak een proefvlak", "Bekijk kleur en effect als het droog is, bij daglicht."),
("Bescherm de omgeving", "Dek vloer en kozijnen goed af; kalkverf spat."),
("Breng twee lagen aan", "Met een blokkwast in kruislingse streken, een hele wand in één keer."),
("Laat drogen", "De kleur wordt pas na het drogen zichtbaar. Beoordeel het resultaat de volgende dag."),
],
"kosten": ["schilderen-per-m2", "binnenschilderwerk"],
"dienst": "binnenschilderwerk",
"faq": [
("Wat is het verschil tussen kalkverf en krijtverf?", "Kalkverf is gemaakt van kalk en geeft een wolkig effect met kleurverschillen. Krijtverf is een zeer matte, egale verf die ook op hout en meubels kan."),
("Kun je kalkverf op latex zetten?", "Niet direct. Op latex of gewone muurverf heb je eerst een speciale primer nodig, anders hecht kalkverf slecht."),
("Is kalkverf afwasbaar?", "Matig. Vlekken zijn lastig weg te krijgen. Kies het liever niet voor plekken waar veel tegenaan komt."),
("Is kalkverf goed tegen schimmel?", "Kalk is van nature basisch en dampopen, wat schimmel minder kans geeft. Maar een vochtprobleem los je er niet mee op."),
("Kun je kalkverf met een roller aanbrengen?", "Het kan, maar het wolkige effect ontstaat juist door de streken van een blokkwast. Met een roller wordt het egaler."),
("Kun je over kalkverf heen schilderen met gewone muurverf?", "Vaak niet direct, omdat kalkverf kan poederen. Meestal is eerst een fixeer- of hechtprimer nodig. Vraag het na bij de verfleverancier."),
("Wat kost kalkverf laten aanbrengen?", "Door het handwerk vaak rond €16 tot €22 per m², aan de bovenkant van gewoon binnenschilderwerk. Kalkmatte muurverf is goedkoper."),
],
"bronnen": [PO_CLASSICO, PO_FRESCO, HISTOR_KALKMAT],
"gerelateerd": ["latex-of-muurverf", "nieuw-stucwerk-schilderen", "renovlies-of-glasvlies"],
"extra_links": [("/kleuren-kiezen/", "Kleurenkiezer: probeer kleuren op je eigen huis")],
},
]


# Verdieping van de vijf dunste artikelen die in ronde 5 nog niet zijn verdiept.
VERDIEPING_R6 = {
"verfschade-en-garantie": {
"secties": [
("Stappenplan bij een klacht",
"""<ol>
<li><strong>Leg het vast.</strong> Maak foto's van dichtbij en van een afstand, met de datum erbij. Noteer wanneer je het zag en wat het weer was.</li>
<li><strong>Zoek je papieren op.</strong> Offerte, opdrachtbevestiging, factuur, algemene voorwaarden en eventueel het garantiebewijs. Daarin staat wat er is afgesproken.</li>
<li><strong>Meld het snel en schriftelijk.</strong> Stuur de schilder een mail of brief met foto's, beschrijf het probleem en vraag om een reactie binnen een redelijke termijn, bijvoorbeeld twee weken. Wacht niet maanden: je moet een gebrek melden binnen een redelijke tijd nadat je het hebt ontdekt.</li>
<li><strong>Geef de schilder de kans om te herstellen.</strong> Een vakman moet zijn eigen werk eerst kunnen bekijken en verbeteren. Laat het niet meteen door een ander doen, anders kun je de kosten vaak niet terugvragen.</li>
<li><strong>Reageert hij niet, of weigert hij?</strong> Stuur een ingebrekestelling: een brief waarin je een laatste termijn geeft om te herstellen. Is de schilder lid van een brancheorganisatie of geschillencommissie, dan kun je daar terecht. De Consumentenbond legt uit hoe je een klacht over een dienstverlener aanpakt.</li>
</ol>"""),
("Schade van de schilder of van het huis?",
"""<p>Niet elke beschadiging is de fout van de schilder. Om een klacht goed te beoordelen, helpt het om te weten waar je op let:</p>
<div class="tablewrap"><table>
<thead><tr><th>Wat je ziet</th><th>Vaak het werk</th><th>Vaak iets anders</th></tr></thead>
<tbody>
<tr><td>Verf laat los, met kale ondergrond eronder</td><td>Slecht ontvet of geschuurd, grondlaag vergeten, geschilderd bij te lage temperatuur.</td><td>Vocht dat van achteren het hout in komt, bijvoorbeeld door een lekkende dakgoot.</td></tr>
<tr><td>Blaasjes in de verf</td><td>Geschilderd op nat hout of in de felle zon.</td><td>Vocht uit de muur of het hout dat er niet uit kan.</td></tr>
<tr><td>Houtrot binnen een jaar</td><td>Rot niet goed weggehaald of niet gemeld.</td><td>Nieuwe rot op een plek die niet in de opdracht zat.</td></tr>
<tr><td>Strepen, druipers, kale plekken</td><td>Afwerking. Dit hoort bij goed vakmanschap.</td><td>Zelden iets anders.</td></tr>
</tbody></table></div>
<p>Meer over losse verf en de oorzaken lees je in <a href="/kennisbank/verf-bladdert-af/">verf bladdert af</a>.</p>"""),
("Zo voorkom je discussie achteraf",
"""<ul>
<li>Laat in de offerte zetten welke voorbereiding wordt gedaan, welke verf, hoeveel lagen en welke garantie geldt. Zie <a href="/kennisbank/goede-offerte-schilderwerk/">goede offerte schilderwerk</a>.</li>
<li>Maak voor de start foto's van de huidige staat, ook van plekken die niet geschilderd worden.</li>
<li>Loop het werk na afloop samen met de schilder na. Wijs dingen direct aan en leg ze vast.</li>
<li>Bewaar de gegevens van de gebruikte verf en kleur. Dat helpt bij bijwerken en bij een klacht.</li>
<li>Laat meerwerk, zoals extra houtrot, altijd vooraf per mail bevestigen.</li>
</ul>"""),
],
"faq": [
("Moet ik de schilder eerst laten herstellen voordat ik een ander inschakel?", "Ja, in de regel wel. De schilder moet de kans krijgen zijn werk te bekijken en te verbeteren. Doe je dat niet, dan kun je de kosten van een ander vaak niet verhalen."),
("Hoe snel moet ik een gebrek melden?", "Binnen een redelijke tijd nadat je het hebt ontdekt, en het liefst schriftelijk met foto's. Wacht je lang, dan wordt het lastiger om je recht te halen."),
("Wat is een ingebrekestelling?", "Een brief waarin je de schilder een laatste, redelijke termijn geeft om het gebrek te herstellen. Daarna kun je verdere stappen zetten."),
],
"bronnen": [CONSUMENTENBOND],
"gerelateerd": ["verf-bladdert-af"],
},
"grondverf-of-voorlak": {
"secties": [
("Welke laag op welke ondergrond?",
"""<div class="tablewrap"><table>
<thead><tr><th>Situatie</th><th>Grondverf</th><th>Voorlak</th><th>Aflak</th></tr></thead>
<tbody>
<tr><td>Kaal, nieuw hout</td><td>Ja, één of twee lagen</td><td>Ja</td><td>Ja</td></tr>
<tr><td>Oude verf in goede staat, zelfde kleur</td><td>Alleen op kale plekken</td><td>Meestal niet</td><td>Eén of twee lagen</td></tr>
<tr><td>Oude verf, kleurwissel van donker naar licht</td><td>Alleen op kale plekken</td><td>Ja, voor dekking</td><td>Ja</td></tr>
<tr><td>Reparatie met houtrotvuller of epoxy</td><td>Ja, volgens het systeem van de vuller</td><td>Ja</td><td>Ja</td></tr>
<tr><td>Hard kunststof of melamine</td><td>Hechtprimer in plaats van gewone grondverf</td><td>Soms</td><td>Ja</td></tr>
<tr><td>Kaal metaal</td><td>Roestwerende grondverf</td><td>Soms</td><td>Ja</td></tr>
</tbody></table></div>
<p>Op een harde, gladde ondergrond hecht gewone grondverf voor hout slecht. Daarvoor bestaat <strong>hechtprimer</strong>. Zie bijvoorbeeld <a href="/kennisbank/keukenkastjes-verven/">keukenkastjes verven</a> en <a href="/kosten/kunststof-kozijnen-schilderen/">kunststof kozijnen schilderen</a>.</p>"""),
("Hoeveel grondverf en voorlak heb je nodig?",
"""<p>Grondverf trekt in kaal hout en verbruikt daardoor meer dan je denkt; op hardhout en eerder geschilderd hout minder. Kijk voor het verbruik altijd op het technisch blad van het product, want dat verschilt per merk. Een buitenkozijn heeft al snel enkele vierkante meters aan houtwerk, met alle kanten en profielen erbij. Gebruik voor een schatting <a href="/gids/verf-berekenen/">hoeveel verf heb je nodig</a>.</p>"""),
("Wat vraag je de schilder?",
"""<ul>
<li>Welk verfsysteem gebruikt hij: grondverf, voorlak en aflak van hetzelfde merk en dezelfde lijn?</li>
<li>Waar komt grondverf: alleen op kale plekken of op het hele kozijn?</li>
<li>Komt er een voorlak, en waarom wel of niet?</li>
<li>Hoeveel lagen komen er in totaal op, en wordt er tussen de lagen geschuurd?</li>
<li>Staat dit allemaal op de offerte? Een offerte met alleen "kozijnen schilderen" zegt weinig.</li>
</ul>"""),
],
"faq": [
("Moet grondverf van hetzelfde merk zijn als de aflak?", "Dat is het veiligst. Fabrikanten testen hun lagen als systeem. Mengen kan, maar dan is de hechting niet gegarandeerd."),
("Heb je grondverf nodig op kunststof?", "Gewone grondverf voor hout hecht slecht op kunststof. Gebruik een hechtprimer die geschikt is voor pvc of melamine."),
("Kan voorlak ook als aflak dienen?", "Niet goed. Voorlak is zachter en minder glanzend, en beschermt minder tegen weer en slijtage. Er hoort een aflak overheen."),
],
"bronnen": [WIJZONOL_HECHTPRIMER],
"gerelateerd": ["keukenkastjes-verven"],
},
"houtrot-herkennen-en-herstellen": {
"secties": [
("Wat vraag je de schilder?",
"""<ul>
<li>Hoeveel plekken houtrot ziet hij, en waar precies? Vraag om foto's of een tekening.</li>
<li>Welke methode gebruikt hij per plek: vullen met houtrotvuller, een stuk nieuw hout inzetten of een deel vervangen?</li>
<li>Hoe wordt houtrot verrekend: een vaste prijs per plek, een stelpost of per uur met een maximum?</li>
<li>Wat gebeurt er als er tijdens het werk meer rot blijkt te zitten? Spreek af dat hij eerst belt, met foto's.</li>
<li>Welke garantie geeft hij op de reparatie, en hoe lang?</li>
</ul>"""),
("Prijs per soort reparatie",
"""<div class="tablewrap"><table>
<thead><tr><th>Reparatie</th><th>Wanneer</th><th>Richtprijs</th></tr></thead>
<tbody>
<tr><td><strong>Kleine plek vullen</strong></td><td>Ondiepe rot, bijvoorbeeld in een hoekverbinding.</td><td class="num">vanaf ongeveer €50</td></tr>
<tr><td><strong>Grotere plek met houtrotvuller</strong></td><td>Diepere rot, maar het kozijn is verder gezond.</td><td class="num">middenin de bandbreedte</td></tr>
<tr><td><strong>Stuk nieuw hout inzetten</strong></td><td>Zoveel rot dat vullen niet meer sterk genoeg is.</td><td class="num">tot ongeveer €275 per plek</td></tr>
<tr><td><strong>Onderdeel vervangen</strong></td><td>Een hele dorpel of stijl is rot.</td><td>apart offreren</td></tr>
</tbody></table></div>
<p>De richtprijs voor houtrotherstel is €50 tot €275 per reparatieplek, inclusief materiaal en btw. Meer rekenvoorbeelden staan bij <a href="/kosten/houtrot-herstellen/">kosten houtrot herstellen</a>.</p>"""),
("Na de reparatie: snel schilderen",
"""<p>Een reparatie is pas af als hij is geschilderd. Houtrotvuller en nieuw hout moeten worden afgesloten met grondverf en lak, anders trekt er opnieuw water in. Laat de reparatie daarom meenemen in dezelfde schilderbeurt. Zit er rot onderaan een kozijn of glaslat, controleer dan ook de kitnaden en de glaslatten; daar komt het water vaak binnen. Zie <a href="/kennisbank/glaslatten-vervangen/">glaslatten vervangen</a>.</p>"""),
],
"faq": [
("Hoe herken ik houtrot zonder te prikken?", "Let op verf die bladdert of blaast, donkere verkleuring, schimmel en hout dat zacht of veerkrachtig aanvoelt. Zekerheid krijg je door met een schroevendraaier te prikken."),
("Kun je houtrot overschilderen?", "Nee. Verf over rot hout houdt vocht vast, waardoor de rot verder gaat. Eerst het rotte hout weghalen en herstellen."),
("Wat is een stelpost voor houtrot?", "Een geschat bedrag in de offerte voor houtrot die vooraf niet precies bekend is. Achteraf betaal je wat er werkelijk aan rot is hersteld."),
],
"bronnen": [KASSA_HOUT],
"gerelateerd": ["glaslatten-vervangen", "oude-verf-verwijderen"],
},
"plafond-schilderen-zonder-strepen": {
"secties": [
("Gereedschap per soort plafond",
"""<div class="tablewrap"><table>
<thead><tr><th>Plafond</th><th>Roller</th><th>Let op</th></tr></thead>
<tbody>
<tr><td><strong>Glad gestuct of gipsplaat</strong></td><td>Vacht van ongeveer 12 tot 18 mm</td><td>Strijklicht laat elke rolbaan zien. Werk nat in nat.</td></tr>
<tr><td><strong>Spachtelputz of spuitpleister</strong></td><td>Langere vacht, ongeveer 18 tot 25 mm</td><td>Neemt veel verf op. Reken op meer verf en werk in kleinere vlakken.</td></tr>
<tr><td><strong>Houten balkenplafond</strong></td><td>Kwast en kleine roller</td><td>Hout krijgt lak of beits, geen muurverf. Zie <a href="/kennisbank/beits-of-verf/">beits of verf</a>.</td></tr>
<tr><td><strong>Plafond met vlekken</strong></td><td>Eerst isoleren</td><td>Een isolerende voorstrijk voorkomt doorslaan. Zie <a href="/kennisbank/vlekken-overschilderen/">vlekken overschilderen</a>.</td></tr>
</tbody></table></div>"""),
("Rollen of laten spuiten?",
"""<p>Een plafond rollen zonder strepen vraagt ervaring. Een schilder kan het plafond ook spuiten: dat geeft een egale laag zonder rolbanen. Spuiten is vooral voordelig in een lege ruimte, zoals nieuwbouw of na een verbouwing, omdat alles eromheen onder folie moet. In een bewoonde kamer wordt meestal gerold. Latex spuiten kost volgens prijssites gemiddeld €6 tot €15 per m²; een plafond laten schilderen €12 tot €22 per m².</p>"""),
("Wat vraag je de schilder?",
"""<ul>
<li>Rolt of spuit hij het plafond, en waarom?</li>
<li>Welke plafondverf of latex gebruikt hij, en in welke glans? Mat verbergt het meest.</li>
<li>Worden scheuren en naden eerst gerepareerd, en zit dat in de prijs? Zie <a href="/kennisbank/scheuren-in-muur-en-plafond/">scheuren in muur en plafond</a>.</li>
<li>Komen er twee lagen?</li>
<li>Wie maakt de kamer leeg en dekt af?</li>
</ul>"""),
("Rekenvoorbeeld: woonkamerplafond",
"""<p>Een woonkamerplafond van 5 bij 7 meter is 35 m². Een schilder rekent €12 tot €22 per m², inclusief verf en btw: €420 tot €770. Moeten er naden en scheuren worden gerepareerd, dan komt er €3 tot €8 per m² bij. Laat je de muren in dezelfde ronde doen, dan deel je het afdekken en de opstart.</p>"""),
],
"faq": [
("Welke roller is het beste voor een plafond?", "Voor een glad plafond een roller met een vacht van zo'n 12 tot 18 mm. Voor spachtelputz een langere vacht."),
("Is spuiten beter dan rollen voor een plafond?", "Spuiten geeft een egalere laag zonder rolbanen, maar alles moet worden afgedekt. In een lege ruimte is het vaak voordeliger."),
("Wat kost een plafond laten schilderen?", "€12 tot €22 per m², inclusief verf en btw. Een woonkamerplafond van 35 m² kost dus €420 tot €770."),
],
"bronnen": [TDS_LATEX],
"gerelateerd": ["scheuren-in-muur-en-plafond", "vlekken-overschilderen"],
},
"welke-verf-voor-kozijnen": {
"secties": [
("Verfsysteem per situatie",
"""<div class="tablewrap"><table>
<thead><tr><th>Situatie</th><th>Wat er nodig is</th></tr></thead>
<tbody>
<tr><td><strong>Onderhoudsbeurt, verf nog heel</strong></td><td>Reinigen, licht schuren, kale plekjes gronden, één of twee lagen aflak.</td></tr>
<tr><td><strong>Verf bladdert op meerdere plekken</strong></td><td>Losse verf weg, kale plekken gronden, voorlak, aflak. Zie <a href="/kennisbank/verf-bladdert-af/">verf bladdert af</a>.</td></tr>
<tr><td><strong>Kaal of nieuw hout</strong></td><td>Volledig systeem: grondverf, voorlak en aflak.</td></tr>
<tr><td><strong>Overstappen naar watergedragen</strong></td><td>Goed schuren en het advies van de fabrikant volgen voor de overgang.</td></tr>
<tr><td><strong>Kleurwissel</strong></td><td>Een extra laag voorlak of aflak voor goede dekking. Kies de kleur met <a href="/kennisbank/ral-9010-of-ral-9001/">RAL 9010 of 9001</a> of de <a href="/kleuren-kiezen/">kleurenkiezer</a>.</td></tr>
</tbody></table></div>"""),
("Wat vraag je de schilder?",
"""<ul>
<li>Welk merk en welke productlijn gebruikt hij voor grondverf, voorlak en aflak?</li>
<li>Op terpentine- of waterbasis, en waarom past dat bij mijn kozijnen?</li>
<li>Hoeveel lagen komen er in totaal op, en in welke glans?</li>
<li>Welke kleurcode komt op de offerte?</li>
<li>Na hoeveel jaar adviseert hij een volgende beurt? Zie <a href="/kennisbank/hoe-vaak-buitenschilderwerk/">hoe vaak buitenschilderwerk</a>.</li>
</ul>"""),
("Rekenvoorbeeld: acht kozijnen van een tussenwoning",
"""<p>Een tussenwoning heeft acht houten buitenkozijnen. Bij een gewone onderhoudsbeurt rekent een schilder €90 tot €190 per kozijn, inclusief verf en btw: €720 tot €1.520. Komt er een kleurwissel bij, reken dan op een extra laag en zo'n 15 tot 25% meer. Een dakkapel kost €400 tot €950 apart. Houtrot herstellen komt erbij, €50 tot €275 per plek.</p>"""),
],
"faq": [
("Kun je kozijnen in de winter schilderen?", "Buiten liever niet. Verf heeft droog weer en een temperatuur boven de minimumwaarde op het blik nodig, vaak zo'n 5 tot 10 °C. Binnenkozijnen kunnen het hele jaar."),
("Moet de verf voor kozijnen van één merk zijn?", "Dat is het veiligst. Grondverf, voorlak en aflak van één systeem zijn op elkaar afgestemd."),
("Wat kost kozijnen laten schilderen?", "€90 tot €190 per buitenkozijn, inclusief verf en btw. Voor acht kozijnen is dat €720 tot €1.520."),
],
"bronnen": [TDS_PRIMER, TDS_BL_PRIMER],
"gerelateerd": ["ral-9010-of-ral-9001", "verf-bladdert-af"],
},
}
