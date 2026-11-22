# -*- coding: utf-8 -*-
"""Kennisbank ronde 4b: vier extra artikelen in hetzelfde formaat als ARTIKELEN in kennis_artikelen.py.

Onderwerpen: verfmerken (Sikkens, Sigma, Histor, Flexa), hoe vaak buitenschilderwerk,
binnen schilderen in de winter en een betonvloer verven of coaten.
Alle bronnen zijn in november 2026 geopend. Prijzen van verf en vloeren komen uit
webwinkels en prijssites en veranderen geregeld; controleer ze bij een update.
"""

from kennis_artikelen import TDS_MUURVERF, TDS_BL_PRIMER

# Bronnen (gelezen in november 2026)
SIKKENS_ENDURANCE = ("Sikkens, productpagina Rubbol BL Endurance High Gloss (watergedragen buitenlak)",
                     "https://www.sikkens.nl/nl/rubbol-bl-endurance-high-gloss")
SIGMA_ALLURE = ("Sigma (PPG), productinformatie Sigma S2U Allure",
                "https://www.sigma.nl/over-sigma/innovaties/sigma-s2u-allure")
PPG_MERKEN = ("PPG, overzicht van merken voor bouw- en woningverf per regio (Sigma en Histor in Europa)",
              "https://www.ppg.com/en-US/architectural-coatings")
AKZO_FUSIE = ("AkzoNobel, informatie over de voorgenomen fusie met Axalta",
              "https://www.akzonobel.com/en/merger-information")
NBVT = ("Nederlandse Bond van Timmerfabrikanten en Stichting Garantiefonds Timmerwerk, brochure Onderhoud van houten gevelelementen",
        "https://www.gilskozijnen.nl/uploads/file/Onderhoud%20van%20houten%20gevelelementen.pdf")
STIPT = ("Helwig Stipt, Onderhoudsvoorschriften houten kozijnen (schema voor kozijnen afgewerkt met Sikkens)",
         "https://stiptkozijnen.nl/Content/Docs/Helwig%20Stipt%20-%20Onderhoudsvoorschriften.pdf")
VANDEVIN = ("Van de Vin ramen en kozijnen, Onderhoudsvoorschriften kozijnen (afgewerkt met Sigma Coatings)",
            "https://www.vandevin.nl/upload/e01303_vinEasyfitOnderhoudsvoor.pdf")
COT_WINTER = ("OnderhoudNL / COT, Praktijkonderzoek duurzaamheid winterschilderwerk (2002-2008)",
              "https://www.onderhoudnl.nl/stream/praktijkonderzoek-duurzaamheid-winterschilderwerk-cot")
FLEXA_GARAGE = ("Flexa, technisch blad Garagevloerverf (versie februari 2025)",
                "https://msp.images.akzonobel.com/prd/dh/enlkge/documents/aa/33/ec/3e/flexa_garagevloerverf.pdf")
SIKA_GARAGE = ("Sika, technische fiche Sikafloor Garage (2-componenten watergedragen epoxycoating)",
               "https://bel.sika.com/content/dam/dms/be01/0/tds-sikafloor-garage-nl.pdf")
HORNBACH_FLEXA = ("Hornbach, productpagina Flexa Garage vloerverf kiezelgrijs 2,5 liter (prijs en verbruik, november 2026)",
                  "https://www.hornbach.nl/p/flexa-garage-vloerverf-kiezelgrijs-2-5-l/8282087/")
SLIMSTER_GIETVLOER = ("Slimster, Wat kost een gietvloer? (prijzen per m², bijgewerkt april 2026)",
                      "https://slimster.nl/vloeren/kosten/gietvloer-prijzen")


ARTIKELEN_RONDE4B = [
# ---------------------------------------------------------------------------
{
"slug": "sikkens-sigma-of-histor",
"groep": "Verf kiezen",
"dienst": "buitenschilderwerk",
"titel": "Sikkens, Sigma, Histor of Flexa: wie maakt wat?",
"seo_titel": "Sikkens, Sigma of Histor? De merken uitgelegd",
"description": "Sikkens en Flexa zijn van AkzoNobel, Sigma en Histor van PPG. Het verschil tussen vakhandel en bouwmarkt, wat Rubbol, S2U en Perfect Finish zijn en wat verf kost.",
"kort": "Wie Sikkens, Sigma, Histor en Flexa maakt, waar je ze koopt en waarom je schilder vaak bij één merk blijft.",
"foto": "verfbak-kwasten-en-roller-zwartwit",
"intro": "Op een offerte voor buitenschilderwerk staat vaak een merknaam: Sikkens, Sigma of soms Histor. In de bouwmarkt zie je ook Flexa. Veel mensen vragen zich af welk merk het beste is. Dat is lastig te zeggen, en wij doen dat ook niet. Wel kunnen we uitleggen wie wat maakt, voor wie de merken bedoeld zijn en waar je echt op moet letten. Het merk blijkt vaak minder belangrijk dan je denkt.",
"kort_antwoord": "Sikkens en Flexa zijn merken van AkzoNobel, Sigma en Histor zijn merken van PPG. Sikkens en Sigma richten zich vooral op de vakschilder, Histor en Flexa vooral op mensen die zelf schilderen. Alle vier maken ze grondverf, lak en muurverf. Voor de levensduur van je schilderwerk zijn een goed opgebouwd verfsysteem en goede voorbereiding belangrijker dan het merk.",
"secties": [
("Wie maakt wat?",
"""<p>De vier bekende verfmerken in Nederland komen van twee grote verfconcerns:</p>
<div class="tablewrap"><table>
<thead><tr><th>Merk</th><th>Van wie</th><th>Vooral bedoeld voor</th></tr></thead>
<tbody>
<tr><td>Sikkens</td><td>AkzoNobel</td><td>Vakschilders</td></tr>
<tr><td>Flexa</td><td>AkzoNobel</td><td>Mensen die zelf schilderen</td></tr>
<tr><td>Sigma</td><td>PPG</td><td>Vakschilders</td></tr>
<tr><td>Histor</td><td>PPG</td><td>Mensen die zelf schilderen</td></tr>
</tbody></table></div>
<p><strong>Sikkens</strong> is een oud Nederlands merk. Volgens de eigen website begon Wiert Willem Sikkens in 1792 een verffabriek in Groningen. Sinds 1939 zit Sikkens in Sassenheim. Het merk hoort bij AkzoNobel, dat ook <strong>Flexa</strong> maakt. AkzoNobel werkt aan een fusie met het Amerikaanse Axalta. Volgens AkzoNobel wordt die eind 2026 of begin 2027 afgerond. Wat dat later voor de merken betekent, is nog niet bekend.</p>
<p><strong>Sigma</strong> en <strong>Histor</strong> zijn merken van het Amerikaanse PPG. PPG verkocht eind 2024 zijn verftak in de Verenigde Staten en Canada, maar de Europese tak bleef. Op de website van PPG staan Sigma en Histor nog steeds bij de merken voor Europa. Histor wordt volgens PPG alleen in Nederland en België verkocht, Sigma in een groot deel van Europa.</p>"""),
("Vakhandel of bouwmarkt",
"""<p>Het grootste verschil zit in waar je de verf koopt en voor wie hij gemaakt is. Sikkens en Sigma verkopen vooral via verfspeciaalzaken en eigen verkooppunten, waar schilders hun verf halen. Daar staat een kleurmengmachine en kun je technisch advies krijgen. Je kunt er als particulier ook terecht, al verschilt de prijs per winkel. Sommige producten van deze merken zie je ook in de bouwmarkt.</p>
<p>Histor en Flexa liggen vooral in de bouwmarkt. Ze zijn gemaakt voor mensen die af en toe zelf een kozijn, deur of muur schilderen. Daarom zie je op de blikken vaak beloftes als "makkelijk te verwerken" of "één laag dekt". Dat zegt niet dat de verf slechter is. Het assortiment is alleen anders opgezet: minder soorten, eenvoudiger systemen en kleinere blikken.</p>"""),
("Rubbol, S2U en Perfect Finish: wat zijn het?",
"""<p>Elk merk heeft productlijnen met een eigen naam. Een paar bekende, met wat de fabrikant er zelf over zegt:</p>
<ul>
<li><strong>Sikkens Rubbol</strong> is de naam voor de lakken en grondverven van Sikkens voor hout. Er zijn versies op terpentinebasis en watergedragen versies (te herkennen aan BL). Over de watergedragen buitenlak Rubbol BL Endurance High Gloss schrijft Sikkens dat hij "minimaal 6 jaar bescherming" biedt. Volgens het technische blad werk je hem bij 10 tot 30 °C.</li>
<li><strong>Sigma S2U</strong> is de lakfamilie van Sigma. S2U Allure is een buitenlak. Sigma noemt hem "gemakkelijk verwerkbaar van 0 °C tot 30 °C" en biedt bij een aangemelde schilder tot 10 jaar garantie, onder voorwaarden. S2U Nova is een lak voor binnen, die volgens Sigma bestand is tegen krassen en huidvet.</li>
<li><strong>Histor Perfect Finish</strong> is een lijn watergedragen lakken van Histor. In de productomschrijving bij bouwmarkten staat dat de lak niet vergeelt en kras- en slijtvast is. Voor buitenkozijnen heeft Histor ook een aparte buitenlak.</li>
<li><strong>Flexa</strong> heeft lakken en muurverf voor binnen en buiten, en ook specialiteiten zoals garagevloerverf. Daarover lees je meer in <a href="/kennisbank/betonvloer-verven/">een betonvloer verven of coaten</a>.</li>
</ul>
<p>Let op: zulke uitspraken komen van de fabrikant zelf. Onafhankelijke vergelijkende tests van deze lijnen hebben wij niet gevonden. Een termijn als "6 jaar" of "10 jaar garantie" geldt bovendien alleen als het werk volgens het voorschrift is uitgevoerd.</p>"""),
("Waarom je schilder vaak bij één merk blijft",
"""<p>Veel schilders werken jaren met hetzelfde merk. Dat heeft praktische redenen:</p>
<ul>
<li><strong>Het verfsysteem.</strong> Grondverf, voorlak en aflak horen bij elkaar. In het technische blad van Rubbol BL Endurance staat bijvoorbeeld dat je eerst gront met de bijbehorende Rubbol BL Endurance Primer. Een schilder die één merk kent, weet precies welke lagen op elkaar passen.</li>
<li><strong>Kleuren.</strong> Elk merk mengt kleuren met een eigen kleurmengsysteem. Wil je later bijwerken in precies dezelfde tint, dan is hetzelfde merk en dezelfde kleurcode het makkelijkst.</li>
<li><strong>Garantie.</strong> Fabrikanten geven soms garantie als het werk met hun systeem is gedaan. Sigma vraagt bijvoorbeeld dat je de garantie vóór de start aanvraagt, en sluit projecten aan de kust of in een industriegebied uit.</li>
<li><strong>Inkoop en ervaring.</strong> Een schilder koopt vaak in bij één groothandel of verkooppunt en kent de verwerking: hoe de lak vloeit, hoe snel hij droogt en wat er misgaat bij koud weer.</li>
</ul>
<p>Heb je een voorkeur voor een merk, zeg dat dan bij de offerteaanvraag. Maar een schilder die zijn eigen systeem goed kent, levert vaak beter werk dan een schilder die een onbekend merk moet gebruiken.</p>"""),
("Rekenvoorbeeld: wat kost de verf op een offerte?",
"""<p>Verf voelt duur als je in de winkel staat. Op een offerte voor buitenschilderwerk is het meestal maar een deel van de prijs. Een voorbeeld voor een tussenwoning, met deze aannames:</p>
<ul>
<li>Ongeveer 30 m² houtwerk aan voor- en achterkant: kozijnen, ramen, een deur en boeidelen.</li>
<li>Een opknapbeurt: kale plekken gronden en het geheel twee keer aflakken.</li>
<li>Een lak met een rendement van ongeveer 12 m² per liter per laag. Dat ligt binnen de 11 tot 13 m² per liter uit het technische blad van Rubbol BL Endurance.</li>
<li>Webwinkelprijzen van november 2026: watergedragen grondverf ongeveer €53 per liter, een buitenlak van een vakmerk ongeveer €70 per liter.</li>
</ul>
<div class="tablewrap"><table>
<thead><tr><th>Post</th><th>Berekening</th><th>Bedrag</th></tr></thead>
<tbody>
<tr><td>Grondverf</td><td>1 liter voor de kale plekken</td><td>€53</td></tr>
<tr><td>Aflak</td><td>30 m² × 2 lagen ÷ 12 m²/l = 5 liter × €70</td><td>€350</td></tr>
<tr><td><strong>Verf totaal</strong></td><td></td><td><strong>ca. €400</strong></td></tr>
<tr><td>Offerte buitenkant tussenwoning</td><td>richtprijs incl. materiaal en btw</td><td>€1.500 tot €3.500</td></tr>
</tbody></table></div>
<p>De verf is in dit voorbeeld dus ongeveer 11 tot 27 procent van de offerte. De rest gaat naar arbeid, voorbereiding, klein materiaal en soms een steiger. Stel dat een ander merk €10 per liter duurder of goedkoper is. Dan scheelt dat op 6 liter zo'n €60. Dat valt weg tegen het verschil tussen twee schilders. Schilders kopen bovendien vaak met korting in, dus de werkelijke materiaalkosten kunnen lager zijn. Hoeveel verf jij nodig hebt, reken je uit met de gids <a href="/gids/verf-berekenen/">hoeveel verf heb je nodig</a>.</p>"""),
("Waar moet je dan wel op letten?",
"""<p>Kijk bij het vergelijken van offertes niet alleen naar het merk, maar ook naar:</p>
<ul>
<li>welk product en welk systeem er staat, met grondverf, voorlak en aflak;</li>
<li>hoeveel lagen er komen en of kale plekken eerst worden gegrond;</li>
<li>wat er aan voorbereiding gebeurt: reinigen, schuren en houtrot herstellen;</li>
<li>of er garantie is, en onder welke voorwaarden.</li>
</ul>
<p>Welke verf bij welk kozijn past, lees je in <a href="/kennisbank/welke-verf-voor-kozijnen/">welke verf voor kozijnen</a>. Twijfel je over een offerte, dan kun je die <a href="/offerte-vergelijken/">gratis laten checken</a>.</p>"""),
],
"stappen": [
("Bepaal wat er geschilderd moet worden", "Maak een lijstje: kozijnen, deuren, boeidelen, binnen of buiten. Dat bepaalt welk soort verf nodig is, niet het merk."),
("Kijk wat er nu op zit", "Vraag aan de vorige schilder of zoek in je papieren welk merk en welke kleurcode er is gebruikt. Bijwerken in hetzelfde systeem is het makkelijkst."),
("Vraag offertes met productnamen", "Vraag de schilder om het merk, het product en het aantal lagen op de offerte te zetten. Dan kun je offertes echt vergelijken."),
("Vergelijk systeem en voorbereiding", "Let op grondverf, voorlak, aflak, schuren en houtrotherstel. Een goed systeem van welk vakmerk dan ook gaat langer mee dan een dure lak op slechte voorbereiding."),
("Leg kleur en product vast", "Bewaar na afloop het merk, de productnaam en de kleurcode. Bij een volgende beurt of een kras weet je dan precies wat je nodig hebt."),
],
"kosten": ["kozijnen-schilderen", "huis-schilderen"],
"faq": [
("Is Sikkens of Sigma beter?", "Dat kunnen we niet onderbouwen. Beide zijn merken voor vakschilders met complete systemen van grondverf tot aflak. Het verschil in levensduur hangt meer af van de voorbereiding, de laagdikte en het weer tijdens het schilderen dan van het merk."),
("Van wie is Sigma verf?", "Sigma is een merk van PPG, net als Histor. PPG verkocht eind 2024 zijn verftak in de Verenigde Staten en Canada, maar Sigma en Histor horen bij de Europese tak die PPG heeft gehouden."),
("Van wie is Flexa?", "Flexa is een merk van AkzoNobel, net als Sikkens. Flexa richt zich vooral op mensen die zelf schilderen en ligt vooral in de bouwmarkt."),
("Is Histor goedkoper dan Sigma?", "Per liter is bouwmarktverf vaak goedkoper dan verf voor vakschilders, maar dat verschilt per product en per actie. Vergelijk daarom ook het rendement per liter en het aantal lagen dat nodig is."),
("Mag ik mijn schilder een merk voorschrijven?", "Ja, dat mag. Zet het in je aanvraag. Houd er wel rekening mee dat een schilder het best werkt met een systeem dat hij goed kent. Vraag dus ook waarom hij een bepaald merk adviseert."),
("Wat betekent BL op een blik Sikkens?", "BL staat bij Sikkens voor een watergedragen product. Rubbol BL is dus de watergedragen variant, naast versies op terpentinebasis. Het verschil lees je in ons artikel over verf op waterbasis of terpentinebasis."),
],
"bronnen": [SIKKENS_ENDURANCE, SIGMA_ALLURE, PPG_MERKEN, AKZO_FUSIE],
"gerelateerd": ["welke-verf-voor-kozijnen", "verf-op-waterbasis-of-terpentinebasis", "goede-offerte-schilderwerk"],
},
# ---------------------------------------------------------------------------
{
"slug": "hoe-vaak-buitenschilderwerk",
"groep": "Schade en onderhoud",
"dienst": "buitenschilderwerk",
"titel": "Hoe vaak moet je buitenschilderwerk en kozijnen schilderen?",
"seo_titel": "Hoe vaak kozijnen en buitenwerk schilderen?",
"description": "Hoe vaak moet je kozijnen buiten schilderen? Termijnen voor lichte, donkere en transparante verf, bijwerken tussendoor, een onderhoudsplan en wat uitstel kost.",
"kort": "Termijnen voor lichte, donkere en transparante verf, bijwerken tussendoor en wat uitstellen je kost.",
"foto": "dakkapel-verweerd-houten-kozijn",
"intro": "Veel mensen laten hun huis buiten schilderen als het er slecht uit gaat zien. Dan is het vaak al te laat: de verf laat los, er komt water bij het hout en er ontstaat houtrot. Met een vast schema voor controle en onderhoud houd je het werk kleiner en goedkoper. Hier lees je welke termijnen de timmerindustrie en de verffabrikanten noemen en wat dat voor jouw huis betekent.",
"kort_antwoord": "Bij dekkende verf in een lichte kleur adviseert de timmerindustrie om na ongeveer 3 jaar beschadigingen bij te werken en na ongeveer 6 jaar een nieuwe laag aan te brengen. Bij donkere kleuren is dat na 2 en 4 jaar, bij transparante verf elk jaar bijwerken en om de 2 jaar een nieuwe laag. Controleer het houtwerk elk jaar: is het nog goed, dan schuift het schema op.",
"secties": [
("De termijnen uit de onderhoudsschema's",
"""<p>Er is geen wet die zegt hoe vaak je moet schilderen. Wel geven de timmerindustrie en kozijnfabrikanten onderhoudsschema's. Die gaan uit van goed aangebracht schilderwerk en een gewone ligging.</p>
<div class="tablewrap"><table>
<thead><tr><th>Soort afwerking</th><th>Bijwerken</th><th>Nieuwe laag</th></tr></thead>
<tbody>
<tr><td>Dekkend, lichte kleur (wit, crème, lichtgrijs)</td><td>na ca. 3 jaar</td><td>na ca. 6 jaar</td></tr>
<tr><td>Dekkend, donkere kleur (antraciet, donkergroen, zwart)</td><td>na ca. 2 jaar</td><td>na ca. 4 jaar</td></tr>
<tr><td>Transparant (beits of lak waar de nerf doorheen te zien is)</td><td>elk jaar</td><td>om de 2 jaar</td></tr>
</tbody></table></div>
<p><small>Bron: het onderhoudsschema voor de eigenaar-bewoner in de brochure van de Nederlandse Bond van Timmerfabrikanten (NBvT) en de Stichting Garantiefonds Timmerwerk (SGT).</small></p>
<p>Kozijnfabrikanten geven in hun eigen voorschriften vergelijkbare schema's. Een schema voor kozijnen met een Sikkens-systeem noemt voor lichte kleuren bijwerken na 4 jaar en een nieuwe laag na 7 jaar, en voor donkere kleuren na 3 en 5 jaar. Een schema voor kozijnen met Sigma noemt een nieuwe laag na 7 jaar bij lichte kleuren. Een watergedragen buitenlak van Sikkens belooft volgens de fabrikant "minimaal 6 jaar bescherming". De getallen liggen dus dicht bij elkaar: bij lichte, dekkende verf ongeveer elke 6 tot 7 jaar een nieuwe laag.</p>"""),
("Waarom de ene gevel vaker toe is dan de andere",
"""<ul>
<li><strong>Zon.</strong> Volgens de brochure van de timmerindustrie slijt de verf aan de zonkant sneller dan aan de schaduwkant of onder een ruime dakgoot, een balkon of een galerij. Het verpoederen begint meestal op de onderdorpels aan de zonzijde.</li>
<li><strong>Kleur.</strong> Donkere kleuren nemen veel meer warmte op. Het hout krimpt en zwelt daardoor meer, en de verf breekt sneller af. In het Sikkens-schema valt een middenkleur op een zeer zonnige, beschutte zuidgevel daarom ook onder het schema voor donkere kleuren.</li>
<li><strong>Vocht en vuil.</strong> Vuil houdt water vast. De brochure adviseert het houtwerk een of meer keren per jaar mee te wassen als je de ramen lapt. Zorg ook dat er minstens 10 tot 15 cm ruimte is tussen de onderdorpels en de bestrating of de tuin.</li>
<li><strong>Transparant of dekkend.</strong> Transparante verf laat meer zonlicht door naar het hout en moet daarom veel vaker worden bijgewerkt. Volgens de schema's mag een transparant systeem ook niet op elke houtsoort.</li>
</ul>
<p>Kies je een nieuwe kleur, denk dan dus ook aan het onderhoud. Kleuren vergelijken kan in de <a href="/kleuren-kiezen/">kleurenkiezer</a>.</p>"""),
("Bijwerken tussendoor: de kleine beurt",
"""<p>De schema's maken onderscheid tussen bijwerken en een nieuwe laag. Bij <strong>bijwerken</strong> herstelt de schilder alleen beschadigingen en de liggende delen, zoals de bovenkant van de dorpels. Die krijgen de meeste zon en regen. Bij een <strong>nieuwe laag</strong> worden eerst de beschadigingen bijgewerkt en gaat daarna alles opnieuw in de verf.</p>
<p>Zo'n kleine beurt kost veel minder dan een complete beurt, maar rekt de tijd tot die complete beurt wel op. Vergeet ook de kitvoegen niet. Volgens de voorschriften van een kozijnfabrikant controleer je die het best binnen een jaar na plaatsing en daarna elke 2 tot 3 jaar. Kit gaat ongeveer 10 tot 15 jaar mee.</p>"""),
("Een onderhoudsplan in vier stappen",
"""<p>De brochure van de timmerindustrie raadt aan om samen met een schilder een schema voor inspectie en onderhoud op te stellen. De schilder controleert het houtwerk dan altijd een jaar vóór het geplande bijwerken. Is het nog goed, dan schuift alles een jaar op.</p>
<ol>
<li><strong>Elk jaar zelf kijken.</strong> Liefst na de winter, op een droge dag. Let op bladderende verf, open naadjes, kale randen en verpoederen: wit poeder op je vinger.</li>
<li><strong>Een jaar voor de geplande beurt een schilder laten kijken.</strong> Die ziet dingen die je zelf mist, zoals zacht hout onder de verf.</li>
<li><strong>Bijwerken wat nodig is.</strong> Liever een kleine beurt aan de zonkant dan wachten tot het hele huis toe is.</li>
<li><strong>Vastleggen.</strong> Noteer wanneer er is geschilderd, met welk product en welke kleurcode.</li>
</ol>
<p>Wil je snel weten hoe jouw houtwerk ervoor staat? Doe de <a href="/onderhoudscheck/">onderhoudscheck</a>: negen vragen, en je ziet of een beurt nu of later nodig is.</p>"""),
("Rekenvoorbeeld: elke 6 of elke 8 jaar schilderen",
"""<p>Een tussenwoning laten schilderen aan de buitenkant kost volgens onze richtprijzen €1.500 tot €3.500, inclusief materiaal en btw. We rekenen met het midden: €2.500 per beurt.</p>
<div class="tablewrap"><table>
<thead><tr><th></th><th>Elke 6 jaar</th><th>Elke 8 jaar</th></tr></thead>
<tbody>
<tr><td>Beurten in 24 jaar</td><td>4</td><td>3</td></tr>
<tr><td>Kosten beurten in 24 jaar</td><td>€10.000</td><td>€7.500</td></tr>
<tr><td>Per jaar</td><td>ca. €417</td><td>ca. €313</td></tr>
</tbody></table></div>
<p>Op papier lijkt elke 8 jaar dus goedkoper. Maar dat klopt alleen als de verf het ook echt 8 jaar volhoudt. Gaat het mis, dan komen er kosten bij. Houtrot herstellen kost volgens onze richtprijzen €50 tot €275 per plek. Vindt de schilder bij een te late beurt 4 rotte plekken, dan is dat €200 tot €1.100 extra. Dat gebeurt dan bij elke beurt opnieuw, omdat het hout steeds langer onbeschermd is geweest. Bij 3 beurten in 24 jaar kan dat oplopen tot €600 tot €3.300. Dan is het voordeel van langer wachten weg.</p>
<p>Een tussentijdse bijwerkbeurt kost veel minder. Stel dat een schilder er een dag van 8 uur mee bezig is, tegen €45 tot €65 per uur exclusief btw. Dat is €360 tot €520, plus 9% btw en wat materiaal. Zo'n beurt kan het moment van de grote beurt uitstellen, zonder het risico op houtrot.</p>
<p>De les: 8 jaar wachten kan, als de jaarlijkse controle laat zien dat de verf nog goed is. Wacht niet alleen omdat het goedkoper lijkt. Hoe je houtrot herkent, lees je in <a href="/kennisbank/houtrot-herkennen-en-herstellen/">houtrot herkennen en herstellen</a>.</p>"""),
("Wanneer in het jaar?",
"""<p>Buitenschilderwerk doe je het liefst bij droog weer, als het niet te koud is en de nachten niet te vochtig. Mei, juni en september zijn vaak ideaal: droog, niet te heet en weinig nachtvorst. In de gids <a href="/gids/wanneer-buiten-schilderen/">wanneer kun je buiten schilderen</a> lees je welke temperatuur en luchtvochtigheid nodig zijn. Plan de jaarlijkse controle in het voorjaar. Dan heb je nog tijd om voor de zomer een schilder te vinden, want in het hoogseizoen zitten veel schilders vol.</p>"""),
],
"stappen": [
("Zoek uit wanneer er voor het laatst is geschilderd", "Kijk in je papieren of vraag het de vorige eigenaar. Noteer ook de kleur: licht, donker of transparant."),
("Bepaal je termijn", "Gebruik het schema: licht dekkend bijwerken na ca. 3 jaar en een nieuwe laag na ca. 6 jaar, donker na 2 en 4 jaar, transparant elk jaar bijwerken en om de 2 jaar een nieuwe laag."),
("Controleer elk voorjaar", "Loop op een droge dag om het huis. Let op bladderende verf, open naden, kale randen en verpoederen, vooral aan de zonkant en op de onderdorpels."),
("Prik in twijfelplekken", "Druk met een schroevendraaier of priem in de onderkant van kozijnen en dorpels. Zakt hij er makkelijk in, dan is er mogelijk houtrot en moet een schilder kijken."),
("Laat een jaar vooraf een schilder kijken", "Vraag een jaar voor de geplande beurt een inspectie. Op basis daarvan beslis je: nu doen, volgend jaar, of nog een jaar opschuiven."),
("Was het houtwerk mee", "Neem bij het ramen lappen ook de kozijnen mee, met een gewoon schoonmaakmiddel zonder schuurmiddel of chloor."),
("Leg alles vast", "Noteer datum, product, kleurcode en wat er is gedaan. Zo weet je bij de volgende controle waar je staat."),
],
"kosten": ["huis-schilderen", "kozijnen-schilderen", "dakkapel-schilderen"],
"faq": [
("Hoe vaak moet je kozijnen buiten schilderen?", "Bij lichte, dekkende verf adviseert de timmerindustrie ongeveer elke 6 jaar een nieuwe laag, met na ongeveer 3 jaar een kleine bijwerkbeurt. Bij donkere kleuren is dat na 4 jaar met bijwerken na 2 jaar."),
("Hoe vaak moet je transparant gelakte kozijnen schilderen?", "Volgens de onderhoudsschema's werk je transparante verf elk jaar bij en komt er om de 2 jaar een nieuwe laag op. Transparante verf beschermt het hout minder tegen zonlicht dan dekkende verf."),
("Is elke 8 jaar schilderen genoeg?", "Soms wel, maar alleen als de jaarlijkse controle laat zien dat de verf nog goed hecht en het hout gezond is. De schema's gaan voor lichte kleuren uit van 6 tot 7 jaar."),
("Wat is het verschil tussen bijwerken en een nieuwe laag?", "Bij bijwerken herstelt de schilder alleen beschadigingen en de liggende delen, zoals de bovenkant van de dorpels. Bij een nieuwe laag gaat na het bijwerken alles opnieuw in de verf."),
("Waarom moet de zonkant vaker geschilderd worden?", "Zon en warmte breken de verf sneller af. Het hout zet uit en krimpt meer, vooral bij donkere kleuren. Daardoor begint het verpoederen meestal op de onderdorpels aan de zonzijde."),
("Kan ik alleen de zonkant laten schilderen?", "Ja. Je hoeft niet alles tegelijk te doen. Laat de gevel die het slechtst is eerder bijwerken. Een schilder kan de beurten zo plannen dat je per gevel op schema blijft."),
],
"bronnen": [NBVT, STIPT, VANDEVIN, SIKKENS_ENDURANCE],
"gerelateerd": ["houtrot-herkennen-en-herstellen", "kozijnen-schuren-en-voorbereiden", "welke-verf-voor-kozijnen"],
},
# ---------------------------------------------------------------------------
{
"slug": "binnen-schilderen-in-de-winter",
"groep": "Offerte, kosten en btw",
"dienst": "binnenschilderwerk",
"titel": "Binnen schilderen in de winter: planning, prijs en tips",
"seo_titel": "Winterschilder: binnen schilderen in winter",
"description": "Waarom schilders in de winter binnen werken, of je dan korting krijgt, wat er wel en niet kan bij kou en wat binnenschilderwerk in een woonkamer ongeveer kost.",
"kort": "Waarom de winter goed is voor binnenwerk, of er korting is en waar je op let bij kou en vocht.",
"foto": "nederlandse-woonkamer-klassiek-interieur",
"intro": "In de zomer staan schilders op steigers langs gevels. In de winter is het buiten vaak te koud en te nat, en schuiven ze naar binnen. Voor jou kan dat handig zijn: er is meer ruimte in de planning en sommige schilders geven korting. Maar een vaste wintersubsidie is er niet meer. Hier lees je hoe het zit, wat er wel en niet kan bij kou en wat het kost.",
"kort_antwoord": "In de winter is buitenwerk vaak niet mogelijk, dus hebben veel schilders meer tijd voor binnenwerk. Dan kun je sneller terecht en geven sommige schildersbedrijven korting, maar daar heb je geen recht op. Binnen kan prima in de winter, zolang de ruimte warm genoeg blijft: muurverf mag volgens technische bladen niet onder 10 °C worden verwerkt. Ventileer wel goed.",
"secties": [
("Waarom schilders in de winter binnen werken",
"""<p>Buitenverf heeft een minimale temperatuur nodig, en het hout moet droog zijn. In de winter is het vaak te koud, te nat of te vochtig. Ook de korte dagen helpen niet. Veel schilders hebben daarom van november tot en met maart minder buitenwerk. Die tijd vullen ze graag met binnenwerk: muren, plafonds, deuren, trappen en kozijnen aan de binnenkant.</p>
<p>Daar komt de naam <strong>winterschilder</strong> vandaan. Vroeger was er een regeling waarbij je in de winter een vast bedrag per schilder per dag terugkreeg. Die regeling bestaat niet meer. De naam De Winterschilder is nu een merk van brancheorganisatie OnderhoudNL. Op de website daarvan vonden we geen landelijke korting of subsidie voor dit seizoen.</p>"""),
("Krijg je in de winter korting?",
"""<p>Soms wel, maar het is geen recht. Een schilder bepaalt zelf of hij in de winter korting geeft en hoeveel. Sommige schildersbedrijven adverteren met een vast percentage op binnenwerk in de wintermaanden, vaak met voorwaarden: alleen in een bepaalde periode, alleen als je het bij je aanvraag noemt, of alleen bij een minimale omvang.</p>
<p>Wat wel vaak scheelt, is de planning. In het voorjaar en de zomer zitten veel schilders vol. In de winter kun je eerder terecht en is er meer tijd om offertes te vergelijken. Zet in je aanvraag dat je flexibel bent met de datum. Dan kan een schilder je werk inplannen in een rustige week.</p>
<p>De btw verandert niet met het seizoen. Voor arbeid aan een woning van meer dan 2 jaar oud geldt 9% btw, in de zomer en in de winter. Hoe dat zit lees je in de gids <a href="/gids/btw-schilderwerk/">btw op schilderwerk</a>.</p>"""),
("Binnen schilderen bij kou: temperatuur en drogen",
"""<p>Binnen kun je het hele jaar schilderen, zolang de ruimte warm genoeg is. Het technische blad van een watergedragen muurverf van Sikkens zegt: niet verwerken beneden 10 °C of boven 30 °C. Hetzelfde blad laat zien hoeveel de temperatuur uitmaakt voor het drogen:</p>
<div class="tablewrap"><table>
<thead><tr><th></th><th>Bij 10 °C</th><th>Bij 20 °C</th></tr></thead>
<tbody>
<tr><td>Stofdroog</td><td>na 12 uur</td><td>na 1 uur</td></tr>
<tr><td>Overschilderbaar</td><td>na 12 uur</td><td>na 5 uur</td></tr>
<tr><td>Doorgehard</td><td>na 48 uur</td><td>na 24 uur</td></tr>
</tbody></table></div>
<p>In een koude kamer kan een schilder dus maar één laag per dag zetten. In een verwarmde kamer lukken er twee. Laat de verwarming daarom aan staan, ook 's nachts, en zet hem niet ineens hoog. Stook je in een vertrek dat lang koud is geweest, wacht dan tot muren en plafond ook zijn opgewarmd.</p>"""),
("Ventileren zonder dat het koud wordt",
"""<p>Verf droogt doordat water of oplosmiddel verdampt. Dat vocht moet weg. Op de technische bladen staat dan ook: zorg voor goede ventilatie tijdens het schilderen. In de winter wil je de ramen liever dicht houden. Een tussenweg: zet een raam op een kier in de ruimte waar geschilderd wordt en houd de deur naar de rest van het huis dicht. Laat de verwarming ondertussen gewoon branden.</p>
<p>Schilder je deuren of kozijnen binnen, kies dan watergedragen lak. Die ruikt minder en droogt sneller dan verf op terpentinebasis. Het verschil lees je in <a href="/kennisbank/verf-op-waterbasis-of-terpentinebasis/">verf op waterbasis of terpentinebasis</a>.</p>"""),
("En buiten schilderen in de winter?",
"""<p>Buiten is lastiger. Veel watergedragen buitenverf heeft een minimumtemperatuur. Het technische blad van een watergedragen grondverf noemt bijvoorbeeld 8 °C. Daarnaast moet de ondergrond droog zijn en minstens 3 °C warmer dan het dauwpunt, anders slaat er vocht neer op het werk.</p>
<p>Er zijn wel buitenlakken die bij lagere temperaturen kunnen. Sigma noemt zijn buitenlak S2U Allure bijvoorbeeld "gemakkelijk verwerkbaar van 0 °C tot 30 °C". Bij groot buitenwerk in de winter zetten schilders soms een steiger in met folie of gaas en verwarmen ze de ruimte erachter. Een praktijkonderzoek van onderzoeksbureau COT, gepubliceerd door OnderhoudNL, vergeleek winter- en zomerschilderwerk op houten gevels. De conclusie: tot 5 jaar na het schilderen was de duurzaamheid gelijk, technisch en qua uiterlijk. In dat onderzoek werd het werk wel afgeschermd en vaak verwarmd. Kijk voor het weer van de komende dagen op het <a href="/schilderweer/">schilderweer</a>.</p>"""),
("Rekenvoorbeeld: een woonkamer laten schilderen",
"""<p>Een woonkamer van 5 bij 4 meter, 2,60 meter hoog. De schilder doet de wanden en het plafond, in twee lagen.</p>
<div class="tablewrap"><table>
<thead><tr><th>Onderdeel</th><th>Berekening</th><th>Oppervlak</th></tr></thead>
<tbody>
<tr><td>Wanden</td><td>(5 + 4 + 5 + 4) m × 2,60 m = 46,8 m², min ca. 8 m² voor ramen en deur</td><td>ca. 39 m²</td></tr>
<tr><td>Plafond</td><td>5 m × 4 m</td><td>20 m²</td></tr>
<tr><td><strong>Totaal</strong></td><td></td><td><strong>ca. 59 m²</strong></td></tr>
</tbody></table></div>
<p>Volgens onze richtprijzen kost binnenschilderwerk €10 tot €22 per m², inclusief materiaal en btw. Voor 59 m² is dat ongeveer <strong>€590 tot €1.300</strong>. Geeft een schilder 10% winterkorting, dan scheelt dat ongeveer €60 tot €130. Dat is mooi meegenomen, maar het verschil tussen de goedkoopste en de duurste offerte is meestal groter. Vergelijk dus eerst de offertes en vraag daarna naar een winteractie.</p>
<p>Ter controle de verf: bij een rendement van ongeveer 11 m² per liter, zoals op het blad van de muurverf, heb je voor 59 m² in twee lagen zo'n 11 liter nodig. Rekent een schilder per uur, dan kost dat €45 tot €65 per uur exclusief btw. Meer rekenhulp vind je op de <a href="/kosten/calculator/">kostencalculator</a>.</p>"""),
],
"stappen": [
("Maak een lijst van het binnenwerk", "Schrijf op welke muren, plafonds, deuren en kozijnen geschilderd moeten worden, met de afmetingen van de kamers."),
("Vraag in het najaar offertes aan", "Vraag in oktober of november offertes aan en zet erbij dat je flexibel bent met de datum. Vraag of de schilder een winteractie heeft en onder welke voorwaarden."),
("Maak de ruimte leeg", "Zet meubels in het midden of in een andere kamer, haal schilderijen en gordijnen weg. Dat scheelt de schilder tijd en jou geld."),
("Stook de ruimte op", "Zorg dat de kamer een dag van tevoren op kamertemperatuur is, en houd de verwarming ook 's nachts aan zolang er geschilderd wordt."),
("Ventileer op een kier", "Zet een raam op een kier in de kamer waar geschilderd wordt en houd de deur naar de rest van het huis dicht."),
("Geef de verf tijd", "Hang schilderijen pas terug en zet meubels pas tegen de muur als de verf is doorgehard. Bij muurverf is dat volgens het technische blad na 24 uur bij 20 °C."),
],
"kosten": ["schilderen-per-m2", "schilder-uurtarief", "plafond-schilderen"],
"faq": [
("Bestaat de winterschilder-regeling nog?", "Nee. Vroeger kreeg je in de winter een vast bedrag per schilder per dag terug, maar die regeling is gestopt. De Winterschilder is nu een merk van OnderhoudNL. Korting in de winter hangt af van de schilder zelf."),
("Is schilderen in de winter goedkoper?", "Soms. Sommige schilders geven in de wintermaanden korting op binnenwerk, maar daar heb je geen recht op. Wat bijna altijd helpt: in de winter kun je sneller terecht en heb je meer tijd om offertes te vergelijken."),
("Hoe warm moet het zijn om binnen te schilderen?", "Volgens het technische blad van een watergedragen muurverf minimaal 10 °C en maximaal 30 °C. Bij 20 °C droogt de verf veel sneller dan bij 10 °C."),
("Moet je ramen openzetten bij schilderen in de winter?", "Ja, op een kier. De verf moet zijn vocht kwijt. Houd de deur naar de rest van het huis dicht en laat de verwarming aan."),
("Kun je in de winter buiten schilderen?", "Soms. Het moet droog zijn en de ondergrond moet minstens 3 °C warmer zijn dan het dauwpunt. Er zijn buitenlakken die vanaf 0 °C kunnen, maar een watergedragen grondverf vraagt volgens het technische blad minimaal 8 °C. Bij groot werk schermt een schilder de steiger soms af en verwarmt hij erachter."),
("Gaat winterschilderwerk minder lang mee?", "Niet als het goed wordt gedaan. Een praktijkonderzoek van COT, gepubliceerd door OnderhoudNL, vond tot 5 jaar na het schilderen geen verschil tussen winter- en zomerschilderwerk. Het werk was in dat onderzoek wel afgeschermd en vaak verwarmd."),
],
"bronnen": [COT_WINTER, TDS_MUURVERF, TDS_BL_PRIMER, SIGMA_ALLURE],
"gerelateerd": ["plafond-schilderen-zonder-strepen", "latex-of-muurverf", "goede-offerte-schilderwerk"],
},
# ---------------------------------------------------------------------------
{
"slug": "betonvloer-verven",
"groep": "Voorbereiden en uitvoeren",
"dienst": "binnenschilderwerk",
"titel": "Betonvloer verven of coaten: betonverf, epoxy of gietvloer?",
"seo_titel": "Betonverf of epoxy voor je vloer of garage?",
"description": "Een betonvloer of garagevloer verven? Het verschil tussen betonverf, 2K-epoxycoating en een gietvloer, de voorbereiding, banden en antislip, en wat het kost.",
"kort": "Betonverf, epoxycoating of gietvloer: wat het verschil is, hoe je voorbereidt en wat het kost.",
"foto": "muur-verven-met-roller-zwartwit",
"intro": "Een kale betonvloer in de garage, de schuur of de kelder stuift, neemt olie op en ziet er snel vies uit. Met verf of een coating maak je hem makkelijker schoon en mooier. Maar er is een groot verschil tussen een blik betonverf uit de bouwmarkt en een epoxycoating of een gietvloer. Hier lees je welke soort bij jouw vloer past, hoe je de vloer voorbereidt en wanneer je beter een vloerenspecialist inschakelt.",
"kort_antwoord": "Voor een garage of schuur met licht gebruik is betonverf (1-component) een goedkope oplossing die je zelf kunt aanbrengen. Een 2-componenten epoxy- of PU-coating is harder en beter bestand tegen banden en olie. Een gietvloer is een dikke laag die door een vloerenspecialist wordt gelegd. Bij alle drie bepaalt de voorbereiding het resultaat: de vloer moet droog, vetvrij, stevig en opgeruwd zijn.",
"secties": [
("Drie soorten: betonverf, coating en gietvloer",
"""<div class="tablewrap"><table>
<thead><tr><th></th><th>Betonverf (1K)</th><th>Epoxy- of PU-coating (2K)</th><th>Gietvloer</th></tr></thead>
<tbody>
<tr><td>Wat is het?</td><td>Verf uit één blik, vaak op acrylaatbasis</td><td>Twee componenten die je mengt en die chemisch uitharden</td><td>Dikke laag kunsthars, gegoten en verdeeld</td></tr>
<tr><td>Laagdikte</td><td>Dun</td><td>Dun tot middel</td><td>Enkele millimeters</td></tr>
<tr><td>Zelf te doen?</td><td>Ja</td><td>Ja, maar lastiger</td><td>Nee, werk voor een vloerenspecialist</td></tr>
<tr><td>Geschikt voor</td><td>Garage, schuur, balkon met licht gebruik</td><td>Garage, werkplaats, opslag</td><td>Woonruimte, keuken, showroom, garage</td></tr>
</tbody></table></div>
<p><strong>Betonverf</strong> is het eenvoudigst. Het technische blad van Flexa Garagevloerverf noemt het "een slijtvaste grond- en eindlaag voor vloeren binnen en beperkt buiten op basis van acrylaathars". Volgens hetzelfde blad is hij bestand tegen banden en antislip, en na volledige doorharding ook tegen tijdelijk contact met olie en benzine.</p>
<p>Een <strong>2K-coating</strong> bestaat uit hars en verharder. Na het mengen hardt het geheel chemisch uit tot een harde laag. Het technische blad van Sikafloor Garage, een watergedragen epoxycoating, noemt hem bestand tegen "normale tot middelzware mechanische en chemische belasting", voor onder meer garages en parkeerdekken.</p>
<p>Een <strong>gietvloer</strong> is geen verfklus meer. Dat is een vak apart, met eigen materialen en machines. Een schilder doet dat meestal niet; daarvoor zoek je een vloerenspecialist.</p>"""),
("Nieuw beton: eerst laten drogen",
"""<p>Vers gestort beton bevat veel water. Verf of coating op een natte vloer laat los of krijgt blazen. Hoe lang je moet wachten, hangt af van de dikte van de vloer en het weer. Meet daarom het vocht in plaats van alleen de dagen te tellen.</p>
<ul>
<li>Het technische blad van Sikafloor Garage noemt een maximum van 6% vocht in de ondergrond, gemeten met een vochtmeter of de zogeheten CM-methode. Bij andere producten kan die grens lager liggen; kijk altijd op het blad van jouw product.</li>
<li>Hetzelfde blad zegt ook: geen optrekkend vocht, te testen met polyethyleenfolie. Plak een stuk plastic folie met tape op de vloer en kijk na een dag of de onderkant nat is of het beton donker kleurt. Is dat zo, dan komt er vocht uit de vloer en kun je niet zomaar coaten.</li>
<li>De vloer moet ook stevig zijn. Sika vraagt een drukvast beton zonder zwakke toplaag.</li>
</ul>"""),
("Voorbereiden: ontvetten en opruwen",
"""<p>Een betonvloer is vaak glad en vuil, zeker in een garage. Verf hecht daar slecht op. Het technische blad van Flexa Garagevloerverf geeft deze voorbereiding voor een onbehandelde vloer:</p>
<ol>
<li>Ontvetten met een verfreiniger.</li>
<li>De poederende toplaag van het beton verwijderen met stugge borstels.</li>
<li>Glad, gevlinderd beton grover opruwen met schuurkorrel P24, bij voorkeur met een machine, en daarna stofvrij maken.</li>
<li>Beschadigingen herstellen met een vloervuller.</li>
</ol>
<p>Voor een 2K-coating zijn de eisen strenger. Sika schrijft voor dat de cementhuid mechanisch wordt verwijderd, door stofarm stralen of met een machine die het oppervlak opruwt, zodat het beton een open structuur krijgt. Dat is werk met zwaar gereedschap. Etsen met zuur zie je soms in klusvideo's, maar de technische bladen die wij lazen noemen dat niet; zij noemen schuren of stralen. Algemene tips voor schuren en stofvrij maken vind je ook in <a href="/kennisbank/kozijnen-schuren-en-voorbereiden/">schuren en voorbereiden</a>.</p>"""),
("Banden en antislip in de garage",
"""<p>In een garage krijgt de vloer het zwaar. Een auto die net heeft gereden heeft warme banden. Op een zachte of slecht hechtende verflaag kunnen die banden stukjes verf meetrekken. Dat heet in het Engels <em>hot tyre pick-up</em>. Je ziet dan kale plekken precies waar de wielen staan.</p>
<p>Wat helpt:</p>
<ul>
<li><strong>Goede hechting.</strong> Vooral opruwen en ontvetten zijn hier belangrijk.</li>
<li><strong>Wachten tot de verf echt hard is.</strong> Flexa Garagevloerverf is volgens het blad na 4 uur overschilderbaar, maar pas na 7 dagen doorgehard bij 20 °C, en na 14 dagen bij 10 °C. Rijd de auto pas daarna naar binnen.</li>
<li><strong>Een sterker systeem</strong> als de vloer intensief wordt gebruikt, zoals een 2K-coating.</li>
</ul>
<p>Een geverfde of gecoate vloer kan glad worden als hij nat is. Flexa Garagevloerverf noemt zichzelf antislip. Bij coatings kan een vakman een antislipmiddel instrooien in de natte laag. Sika noemt in zijn blad ook ingestrooide systemen.</p>"""),
("Let op het weer en de temperatuur",
"""<p>Een garage of schuur is in de winter vaak koud. Flexa schrijft: niet verwerken beneden 10 °C. Voor Sikafloor Garage geldt minimaal 10 °C voor de lucht en de vloer, een luchtvochtigheid van hoogstens 80%, en een vloer die minstens 3 °C warmer is dan het dauwpunt. Sika waarschuwt ook om geen gas- of oliekachels te gebruiken om de ruimte op te warmen: die geven veel waterdamp en CO2 af, en dat kan de coating aantasten. Gebruik alleen elektrische verwarming. Plan dit werk dus liever in het voorjaar of de zomer. Zorg in een dichte garage steeds voor frisse lucht.</p>"""),
("Rekenvoorbeeld: garagevloer van 18 m²",
"""<p><strong>Zelf verven met betonverf.</strong> Volgens het technische blad van Flexa Garagevloerverf breng je op een kale vloer eerst één verdunde laag aan om in te wassen, en daarna twee lagen. Het rendement is ongeveer 8 m² per liter.</p>
<div class="tablewrap"><table>
<thead><tr><th>Post</th><th>Berekening</th><th>Uitkomst</th></tr></thead>
<tbody>
<tr><td>Te verven oppervlak</td><td>18 m² × 3 lagen</td><td>54 m²</td></tr>
<tr><td>Liters</td><td>54 m² ÷ 8 m²/l</td><td>ca. 6,75 liter</td></tr>
<tr><td>Blikken</td><td>3 blikken van 2,5 liter</td><td>7,5 liter</td></tr>
<tr><td>Kosten verf</td><td>3 × €59,95 (bouwmarktprijs november 2026)</td><td>ca. €180</td></tr>
</tbody></table></div>
<p>Daar komen kosten bij voor ontvetter, roller, kwast, vloervuller en eventueel de huur van een schuurmachine. En je tijd: een dag voorbereiden, lagen met 4 uur droogtijd ertussen, en daarna 7 tot 14 dagen geen auto in de garage.</p>
<p><strong>Laten leggen: een epoxy gietvloer.</strong> Prijssite Slimster noemt voor een epoxy gietvloer gemiddeld €50 tot €65 per m², inclusief plaatsing en exclusief btw. Voor 18 m² is dat €900 tot €1.170 exclusief btw. Bij een kleine ruimte kan de prijs per m² hoger uitvallen, omdat voorbereiding en voorrijden vaste kosten zijn. Een dunne 2K-rolcoating is minder werk dan een gietvloer. Ter indicatie van het materiaal: Sika noemt voor zijn garagecoating een verbruik van 0,2 tot 0,3 kg per m² per laag. Voor 18 m² is dat 3,6 tot 5,4 kg per laag, ongeveer één set van 6 kg per laag.</p>
<p>Laat een schilder alleen de vloer verven, dan rekent hij meestal per uur. Wat schilderwerk per m² kost op muren en plafonds, zie je op <a href="/kosten/schilderen-per-m2/">schilderen per m²</a>. Een vloer vraagt meer voorbereiding, dus vraag altijd een offerte op maat.</p>"""),
],
"stappen": [
("Kies het systeem", "Licht gebruik in schuur of garage: betonverf. Veel auto's, olie of een werkplaats: een 2K-coating. Een woonruimte of een naadloze dikke vloer: een gietvloer door een vloerenspecialist."),
("Controleer of de vloer droog is", "Plak een stuk plastic folie met tape op de vloer. Is de onderkant na een dag nat of is het beton donker, dan komt er vocht uit de vloer. Bij nieuw beton: laat het vocht meten."),
("Ontvet en verwijder losse delen", "Ontvet de hele vloer, schrob olievlekken extra en borstel de poederende toplaag weg. Laat de vloer daarna goed drogen."),
("Ruw de vloer op en maak hem stofvrij", "Schuur glad beton op met grove korrel, bij voorkeur met een machine. Zuig daarna al het stof op."),
("Herstel gaten en scheuren", "Vul gaten en beschadigingen met een vloervuller en laat die uitharden volgens de verpakking."),
("Breng de lagen aan", "Begin met een verdunde eerste laag die je inwast met de kwast, en rol daarna de volgende lagen. Werk bij minimaal 10 °C en houd de wachttijd tussen de lagen aan."),
("Laat de vloer uitharden", "Loop pas over de vloer als de verf droog is en zet de auto pas terug als hij volgens het blad is doorgehard, bij Flexa Garagevloerverf na 7 dagen bij 20 °C of 14 dagen bij 10 °C."),
],
"kosten": ["schilderen-per-m2"],
"faq": [
("Wat is het verschil tussen betonverf en epoxy?", "Betonverf is verf uit één blik die droogt door verdamping. Epoxy bestaat uit twee componenten die je mengt en die chemisch uitharden. Epoxy wordt harder en is beter bestand tegen banden, olie en schoonmaakmiddelen, maar is lastiger aan te brengen."),
("Hoe lang moet nieuw beton drogen voor je kunt verven?", "Dat hangt af van de dikte en het weer. Tel niet alleen de dagen, maar meet het vocht. Het technische blad van een epoxycoating noemt een maximum van 6% vocht in de ondergrond. Kijk op het blad van jouw product."),
("Waarom laat verf los onder de banden van mijn auto?", "Warme banden kunnen een zachte of slecht hechtende verflaag meetrekken. Meestal is de vloer niet goed opgeruwd of ontvet, of is de auto er te vroeg op gezet. Wacht tot de verf volgens het blad is doorgehard."),
("Kun je een betonvloer in huis verven?", "Ja, maar in een woonruimte is betonverf vaak niet mooi of sterk genoeg. Daar kiezen mensen eerder voor een gietvloer of een andere vloerafwerking, gelegd door een vloerenspecialist."),
("Is een geverfde betonvloer glad?", "Dat kan, vooral als hij nat is. Sommige garagevloerverf is antislip. Bij een coating kan een vakman een antislipmiddel instrooien in de natte laag."),
("Kan ik betonverf in de winter aanbrengen?", "Alleen als het in de ruimte minstens 10 °C is. Verwarm niet met een gas- of oliekachel, want die geven veel waterdamp af. Plan het liever in het voorjaar of de zomer."),
],
"bronnen": [FLEXA_GARAGE, SIKA_GARAGE, HORNBACH_FLEXA, SLIMSTER_GIETVLOER],
"gerelateerd": ["kozijnen-schuren-en-voorbereiden", "verf-op-waterbasis-of-terpentinebasis", "sikkens-sigma-of-histor"],
},
]
