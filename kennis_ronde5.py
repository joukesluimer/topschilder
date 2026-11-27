# -*- coding: utf-8 -*-
"""Kennisbank ronde 5: acht nieuwe artikelen, zelfde formaat als ARTIKELEN in kennis_artikelen.py.

Onderwerpen gekozen op zoekvolume (Semrush nl, november 2026): RAL 9010 of 9001, voordeur
schilderen, binnendeuren verven, glaslatten vervangen, muur plamuren, oude verf verwijderen,
beits of verf en schilderwerk bij een VvE. Zie CONTENT-RONDE5.md.

Technische cijfers komen uit de genoemde productbladen (geopend op 27 november 2026).
Controleer ze bij een update; fabrikanten geven geregeld een nieuwe versie uit.
"""

from kennis_artikelen import TDS_PRIMER, TDS_BL_PRIMER, TDS_MUURVERF, BELASTINGDIENST, GGD_LOOD, BW7
from kennis_ronde4a import SIKKENS_REZISTO, TDS_VOORSTRIJK

# Bronnen voor deze ronde
PRAXIS_RAL = ("Praxis, RAL 9001 en RAL 9010: dit is het verschil", "https://praxis.nl/productadvies/ral-9001")
RAL_CLASSIC = ("RAL gGmbH, RAL CLASSIC kleurencollectie (216 kleuren)", "https://www.ral-farben.de/ral-classic")
RUBBOL_ENDURANCE = ("Sikkens, productpagina Rubbol BL Endurance High Gloss (watergedragen buitenlak)",
                    "https://www.sikkens.nl/nl/producten/rubbol-bl-endurance-high-gloss")
ALAB_MUURVULLER = ("Alabastine, productinformatie Sneldrogende Muurvuller (pot)",
                   "https://www.alabastine.nl/wp-content/uploads/2015/03/sneldrogende-muurvuller-pot.pdf")
ALAB_MUURVULLER_WEB = ("Alabastine, productpagina Sneldrogende Muurvuller",
                       "https://www.alabastine.nl/product/sneldrogende-muurvuller/")
ALAB_MUURGLAD = ("Alabastine, productpagina Muurglad Rolbaar", "https://www.alabastine.nl/product/muurglad-rolbaar/")
WIJZONOL_BEITS = ("Wijzonol, productinformatieblad Dekkend Tuinbeits (alkyd, v1.1)",
                  "https://www.wijzonol.nl/wp-content/uploads/wpallimport/files/documents/10083_nl_PIB_Wijzonol_Bouwverven_B.V._Wijzonol%20Dekkend%20Tuinbeits_1_1_1762318992531.pdf")
CETABEVER_BEITS = ("CetaBever, productinformatie Gevel Hout Snel Beits Dekkend (versie 27-02-2026)",
                   "https://msp.images.akzonobel.com/prd/dh/enlkge/documents/05/5b/53/41/cb_gevel_hout_snel_beits_dk.pdf")
RIJKSOVERHEID_VVE = ("Rijksoverheid, Hoeveel geld moeten vve's reserveren voor groot onderhoud?",
                     "https://www.rijksoverheid.nl/onderwerpen/huis-kopen/vraag-en-antwoord/vve-geld-reserveren-groot-onderhoud")
HOMEDEAL_BUITEN = ("Homedeal, Buitenschilder kosten (2026)", "https://www.homedeal.nl/schilderwerk/buitenschilder-kosten/")


ARTIKELEN_RONDE5 = [
# ---------------------------------------------------------------------------
{
"slug": "ral-9010-of-ral-9001",
"groep": "Verf kiezen",
"titel": "RAL 9010 of RAL 9001: welk wit kies je voor kozijnen en muren?",
"seo_titel": "RAL 9010 of RAL 9001? Verschil en welk wit je kiest",
"description": "RAL 9010, RAL 9001, RAL 9016 of gebroken wit: wat is het verschil en welk wit past bij je kozijnen, deuren en muren? Met kleurtips per woningtype.",
"kort": "Het verschil tussen zuiver wit, crèmewit en verkeerswit, en welk wit bij jouw huis past.",
"foto": "nederlandse-woonkamer-klassiek-interieur",
"intro": "Wit is de meest gekozen kleur voor kozijnen, deuren en plafonds. Maar wit is niet gewoon wit. In de winkel en op offertes kom je RAL 9010, RAL 9001 en RAL 9016 tegen, en ook \"gebroken wit\". Het verschil lijkt klein op een kleurenwaaier, maar op een hele gevel of in een lichte kamer zie je het wel. Hier lees je wat de codes betekenen en welk wit bij jouw huis past.",
"kort_antwoord": "RAL 9010 heet zuiver wit: een wit met een lichte, warme ondertoon. RAL 9001 heet crèmewit: duidelijk warmer en zachter, met een gele tot roodachtige ondertoon. RAL 9016, verkeerswit, is helderder en koeler. Voor kozijnen in een rijtjeshuis of jaren-30-woning kiezen veel mensen RAL 9010. RAL 9001 past bij oudere huizen en een warm interieur. RAL 9016 kies je bij moderne nieuwbouw en kunststof kozijnen.",
"secties": [
("Wat is een RAL-kleur?",
"""<p>RAL is een Duits kleursysteem. De bekendste reeks, RAL CLASSIC, bevat 216 kleuren met elk een vast nummer. Wie RAL 9010 bestelt, krijgt bij elke fabrikant ongeveer dezelfde kleur. Dat maakt het makkelijk: een schilder kan dezelfde kleur bijwerken met verf van een ander merk.</p>
<p>Alle witten en grijzen zitten in de 9000-reeks. Daarnaast heeft elk verfmerk eigen kleurcodes. "Gebroken wit" is geen RAL-code, maar een verzamelnaam voor wit met een beetje kleur erin. Vraag de schilder bij gebroken wit altijd om de precieze code, anders weet je niet wat je krijgt.</p>"""),
("RAL 9010, 9001 en 9016 naast elkaar",
"""<div class="tablewrap"><table>
<thead><tr><th>Code</th><th>Naam</th><th>Uitstraling</th><th>Past vaak bij</th></tr></thead>
<tbody>
<tr><td><strong>RAL 9010</strong></td><td>Zuiver wit</td><td>Wit met een lichte, warme ondertoon. Rustig en tijdloos.</td><td>Kozijnen en deuren in rijtjeshuizen, jaren-30 en jaren-70 woningen, plafonds.</td></tr>
<tr><td><strong>RAL 9001</strong></td><td>Crèmewit</td><td>Zacht en warm, neigt naar crème. Wordt vaak gebroken wit genoemd.</td><td>Oudere en monumentale panden, landelijke stijl, warme interieurs.</td></tr>
<tr><td><strong>RAL 9016</strong></td><td>Verkeerswit</td><td>Helder en koel, bijna fris blauwachtig naast 9010.</td><td>Moderne nieuwbouw, kunststof kozijnen, strak interieur.</td></tr>
</tbody></table></div>
<p>Naast elkaar zie je het verschil meteen. Los op een kozijn lijkt RAL 9010 gewoon wit. Zet je het naast RAL 9016, dan zie je hoe warm het is. RAL 9001 valt naast beide op als crème.</p>"""),
("Welk wit voor je kozijnen?",
"""<p>Kijk eerst naar de stenen en het dak. Rode of oranje baksteen maakt koel wit harder; daar staat RAL 9010 of 9001 vaak rustiger. Bij grijze of witte stenen en een strak, modern huis past RAL 9016 beter. Kijk ook naar de buren: in een rij woningen valt een andere witte tint snel op.</p>
<p>Heb je kunststof kozijnen? De meeste witte kunststof kozijnen zijn ongeveer RAL 9016. Schilder je de houten voordeur in RAL 9010 naast een kunststof kozijn in 9016, dan zie je dat. Kies dan dezelfde tint als het kunststof. Over schilderen van kunststof lees je bij <a href="/kosten/kunststof-kozijnen-schilderen/">kunststof kozijnen schilderen</a>.</p>
<p>Woon je in een beschermd stads- of dorpsgezicht of een monument? Dan kan de gemeente eisen stellen aan de kleur. Vraag dat na voor je de schilder opdracht geeft. Meer kleuradvies per woningtype vind je in de <a href="/inspiratie/">inspiratiegids</a>.</p>"""),
("Welk wit binnen?",
"""<p>Binnen werkt het licht anders dan buiten. Een kamer op het noorden heeft koel licht; daar maakt RAL 9016 de ruimte kil, en voelt 9010 of 9001 prettiger. Een kamer op het zuiden met veel zon verdraagt een koeler wit beter.</p>
<p>Voor plafonds kiezen veel schilders standaard wit van de muurverf, en voor kozijnen en deuren RAL 9010. Wil je muren en lakwerk in dezelfde tint? Laat de muurverf dan op dezelfde RAL-code mengen. Wil je eerst proberen, gebruik dan de <a href="/kleuren-kiezen/">kleurenkiezer</a>.</p>"""),
("Glans maakt ook verschil",
"""<p>Dezelfde RAL-kleur ziet er in hoogglans anders uit dan in mat. Hoogglans weerkaatst meer licht en lijkt daardoor iets lichter en kouder. Zijdeglans en mat ogen zachter. Op kozijnen buiten is hoogglans of zijdeglans gangbaar, omdat die het beste beschermen. Meer daarover in <a href="/kennisbank/welke-verf-voor-kozijnen/">welke verf voor kozijnen</a>.</p>
<p>Wit vergeelt ook. Verf op terpentinebasis (alkyd) vergeelt binnen sneller, vooral op plekken met weinig daglicht. Watergedragen lak blijft witter. Wil je je witte binnendeuren wit houden, lees dan <a href="/kennisbank/verf-op-waterbasis-of-terpentinebasis/">verf op waterbasis of terpentinebasis</a>.</p>"""),
("Rekenvoorbeeld: kozijnen van wit naar wit",
"""<p>Je wilt de kozijnen van een tussenwoning, nu in een vergeeld wit, laten schilderen in RAL 9010. Omdat het van wit naar wit gaat, is geen extra laag nodig. De prijs is gelijk aan een gewone beurt: acht buitenkozijnen à €90 tot €190 is €720 tot €1.520, inclusief verf en btw. Ga je van donkergroen naar RAL 9010, dan dekt één laag aflak niet en komt er een laag voorlak bij. Reken dan op 15 tot 25% meer voor die kozijnen.</p>"""),
],
"stappen": [
("Kijk naar het geheel", "Bekijk stenen, dak, kunststof delen en de buren. Een warm huis vraagt meestal een warm wit."),
("Vraag om stalen", "Laat de schilder of verfwinkel echte verfstalen maken van RAL 9010, 9001 en eventueel 9016."),
("Test op de plek zelf", "Houd de stalen tegen het kozijn of de muur, bij daglicht en op verschillende momenten van de dag."),
("Kies de glans", "Hoogglans of zijdeglans voor buiten, zijdeglans of mat voor binnen."),
("Leg de code vast", "Laat de RAL-code en het verfproduct op de offerte zetten, zodat later bijwerken makkelijk is."),
],
"kosten": ["kozijnen-schilderen", "deuren-spuiten"],
"faq": [
("Wat is het verschil tussen RAL 9010 en RAL 9001?", "RAL 9010 is zuiver wit met een lichte, warme ondertoon. RAL 9001 is crèmewit: duidelijk warmer en zachter. Naast elkaar zie je RAL 9001 als crème."),
("Is RAL 9010 gebroken wit?", "Sommige winkels noemen het zo, omdat het niet helemaal koel wit is. Officieel heet het zuiver wit. Gebroken wit is geen RAL-code; vraag altijd om de precieze code."),
("Welk wit is het meest gekozen voor kozijnen?", "RAL 9010 is in Nederland een veelgekozen wit voor houten kozijnen en deuren. Bij kunststof kozijnen is RAL 9016 gebruikelijker."),
("Past RAL 9010 bij witte kunststof kozijnen?", "Niet altijd. Witte kunststof kozijnen liggen vaak dichter bij RAL 9016. Naast elkaar zie je dan verschil. Kies voor houten delen dezelfde tint als het kunststof."),
("Welk wit voor het plafond?", "Meestal gewoon wit muurverf of RAL 9010. In een kamer op het noorden voelt een warmer wit prettiger."),
("Vergeelt witte verf?", "Verf op terpentinebasis vergeelt binnen sneller, vooral bij weinig daglicht. Watergedragen lak blijft langer wit."),
("Kost een andere witte kleur meer?", "Nee, de RAL-kleur zelf maakt de prijs niet uit. Een kleurwissel van donker naar wit kan wel een extra laag vragen."),
],
"bronnen": [RAL_CLASSIC, PRAXIS_RAL, TDS_BL_PRIMER],
"gerelateerd": ["welke-verf-voor-kozijnen", "verf-op-waterbasis-of-terpentinebasis", "voordeur-schilderen"],
"extra_links": [("/kleuren-kiezen/", "Kleurenkiezer: probeer kleuren op je eigen huis")],
},
# ---------------------------------------------------------------------------
{
"slug": "voordeur-schilderen",
"groep": "Voorbereiden en uitvoeren",
"titel": "Voordeur schilderen: verf, kleur en stappenplan",
"seo_titel": "Voordeur schilderen of verven: zo doe je het",
"description": "Je voordeur schilderen of laten verven? Welke lak, welke kleur, hoe je hem schildert terwijl hij in het kozijn hangt, en wat het kost. Met stappenplan.",
"kort": "Welke lak, welke kleur en hoe je een voordeur schildert zonder hem uit te hangen.",
"foto": "monumentale-voordeur-amsterdam",
"intro": "De voordeur is het eerste wat bezoekers zien, en hij krijgt het zwaar: zon, regen en elke dag handen en sleutels. Een geschilderde deur gaat daardoor minder lang mee dan de kozijnen eromheen. Een nieuwe laag lak geeft je huis meteen een frisser gezicht. Hier lees je welke verf je nodig hebt, hoe je een kleur kiest en hoe je de deur schildert zonder dat je huis een dag openstaat.",
"kort_antwoord": "Een voordeur schilder je met een buitenlak voor hout, meestal in hoogglans of zijdeglans. Ontvet en schuur de deur, gron kale plekken, en zet twee lagen aflak. Je kunt de deur in het kozijn laten hangen: schilder dan vroeg op een droge dag zodat hij voor de avond dicht kan. Een schilder rekent €100 tot €185 voor een voordeur.",
"secties": [
("Welke verf hoort op een voordeur?",
"""<p>Op een houten voordeur hoort een <strong>buitenlak</strong>: verf die tegen zon, regen en temperatuurwisselingen kan en elastisch blijft als het hout werkt. Er zijn goede buitenlakken op terpentinebasis (alkyd) en op waterbasis.</p>
<p>Een voorbeeld uit de productinformatie van een watergedragen hoogglans buitenlak: het rendement is ongeveer 12 m² per liter en de lak is na ongeveer 16 uur overschilderbaar. De fabrikant beschrijft een systeem van grondlaag, voorlak en aflak voor kaal hout. Bij een deur die nog goed in de verf zit, is opschuren en één of twee lagen aflak meestal genoeg.</p>
<p>Een voordeur heeft zo'n 4 m² aan elke kant. Voor de buitenkant plus de kanten van de deur kom je met twee lagen op ongeveer een kwart tot een halve liter lak. Een klein blik is dus genoeg.</p>"""),
("Hoogglans of zijdeglans?",
"""<p>Hoogglans is klassiek op een Nederlandse voordeur. Het beschermt goed, vuil hecht er minder aan en het staat chic bij paneeldeuren. Het nadeel: elke oneffenheid is te zien. Zijdeglans is rustiger en vergevingsgezinder, en past goed bij moderne vlakke deuren. Beide beschermen goed, zolang de laagdikte klopt.</p>"""),
("Welke kleur kies je?",
"""<p>Populaire kleuren voor een voordeur zijn donkergroen, donkerblauw, antraciet, zwart en diep rood. Een donkere deur wordt in de zon wel veel warmer. Op een zuid- of westgevel kan het hout daardoor meer werken, en hars uit naaldhout kan naar buiten komen. Kies dan een lak die daarvoor geschikt is en houd rekening met wat vaker onderhoud.</p>
<p>Kijk ook naar de kozijnen. Een donkere deur in een wit kozijn geeft contrast. Welk wit, lees je in <a href="/kennisbank/ral-9010-of-ral-9001/">RAL 9010 of RAL 9001</a>. In een beschermd stads- of dorpsgezicht kan de gemeente regels hebben voor de kleur. Probeer kleuren op een foto van je huis met de <a href="/kleuren-kiezen/">kleurenkiezer</a>.</p>"""),
("Deur in het kozijn laten of uithangen?",
"""<p>Uithangen geeft het mooiste resultaat, omdat je de deur plat kunt leggen en alle kanten goed bereikt. Maar dan staat je huis open, of je moet een tijdelijke afsluiting maken. Daarom schilderen de meeste mensen en schilders de deur in het kozijn.</p>
<p>Zo pak je dat aan:</p>
<ul>
<li>Begin vroeg op een droge dag zonder felle zon op de deur, met een temperatuur boven ongeveer 10 °C.</li>
<li>Schilder eerst de randen en de sponning, daarna de panelen en als laatste de stijlen en dorpels.</li>
<li>Zet de deur een stukje open met een wig, zodat hij niet tegen het kozijn plakt.</li>
<li>Laat hem pas dicht als de lak kleefvrij is. Doe de deur de eerste dagen voorzichtig dicht.</li>
</ul>
<p>Haal brievenbus, deurbeslag en huisnummer eraf, of plak ze goed af. Afplakken met tape geeft vaak randjes.</p>"""),
("Vergeet de onderkant en de dorpel niet",
"""<p>Houtrot in een voordeur begint bijna altijd onderaan: de onderkant van de deur en de dorpel eronder. Water loopt daar langs en blijft staan. Schilder de onderkant van de deur mee, als het kan met de deur even uit de scharnieren. Prik met een schroevendraaier in de dorpel: is het hout zacht, dan moet er eerst houtrot hersteld worden. Wat dat kost, staat bij <a href="/kosten/houtrot-herstellen/">houtrot herstellen</a>.</p>"""),
("Wat kost het om je voordeur te laten schilderen?",
"""<p>Een schilder rekent voor een buitendeur meestal €100 tot €185, inclusief lak en btw. Homedeal noemt €100 tot €300 voor een voor- of achterdeur. Moet de deur helemaal kaal worden gemaakt, of is er houtrot, dan zit je aan de bovenkant of erboven. Laat je de deur meenemen in een buitenbeurt, dan deel je de opstart- en voorrijkosten. Zie <a href="/kosten/buitenschilderwerk/">kosten buitenschilderwerk</a>.</p>"""),
],
"stappen": [
("Kies een droge dag", "Boven ongeveer 10 °C, geen regen voorspeld en geen felle zon op de deur. Begin 's ochtends."),
("Haal beslag eraf", "Verwijder brievenbus, klink en huisnummer, of plak ze zorgvuldig af."),
("Reinig en ontvet", "Was de deur met een ontvetter en spoel na met schoon water. Laat hem drogen."),
("Schuur", "Schuur de oude laag mat met fijn schuurpapier. Losse verf schraap je weg en de randen schuur je glad."),
("Gron kale plekken", "Zet grondverf op kaal hout. Laat die drogen volgens het blik."),
("Lak in de goede volgorde", "Eerst randen en sponning, dan panelen, dan stijlen en dorpels. Twee lagen, met tussendoor licht schuren."),
("Laat drogen voor je sluit", "Zet de deur op een wig en sluit hem pas als de lak kleefvrij is."),
],
"kosten": ["buitenschilderwerk", "deuren-spuiten"],
"faq": [
("Welke verf gebruik je voor een voordeur?", "Een buitenlak voor hout, op terpentine- of waterbasis, meestal in hoogglans of zijdeglans. Op kaal hout komt eerst grondverf."),
("Kun je een voordeur schilderen zonder hem uit te hangen?", "Ja. Begin vroeg op een droge dag, schilder in de goede volgorde en laat de deur op een wig openstaan tot de lak kleefvrij is."),
("Hoeveel lagen lak heeft een voordeur nodig?", "Bij een deur in goede staat één tot twee lagen aflak na het schuren. Bij kaal hout grondverf, voorlak en aflak."),
("Wat kost een voordeur laten schilderen?", "Meestal €100 tot €185, inclusief lak en btw. Met houtrot of als de deur helemaal kaal moet, wordt het meer."),
("Hoe vaak moet een voordeur geschilderd worden?", "Vaak iets eerder dan de kozijnen, omdat hij meer te verduren krijgt. Kijk elk voorjaar naar de onderkant en de zonkant."),
("Mag ik mijn voordeur elke kleur geven?", "Meestal wel. In een beschermd stads- of dorpsgezicht of bij een monument kan de gemeente regels hebben. Vraag dat na."),
("Waarom plakt mijn deur aan het kozijn na het schilderen?", "De lak was nog niet droog genoeg toen de deur dicht ging. Laat hem langer op een wig staan, zeker bij kou."),
],
"bronnen": [RUBBOL_ENDURANCE, TDS_PRIMER, HOMEDEAL_BUITEN, BELASTINGDIENST],
"gerelateerd": ["welke-verf-voor-kozijnen", "ral-9010-of-ral-9001", "kozijnen-schuren-en-voorbereiden"],
},
# ---------------------------------------------------------------------------
{
"slug": "binnendeuren-verven",
"groep": "Voorbereiden en uitvoeren",
"titel": "Binnendeuren verven: zo krijg je een strak resultaat",
"seo_titel": "Binnendeuren verven of lakken: stappenplan",
"description": "Binnendeuren verven zonder strepen? Welke lak, rollen of kwasten, hoe je opdekdeuren en kozijnen aanpakt, en wanneer laten spuiten slimmer is. Met kosten.",
"kort": "Welke lak, welke volgorde en hoe je strepen voorkomt op binnendeuren en kozijnen.",
"foto": "witte-grondverf-rollen-op-hout",
"intro": "Vergeelde of beschadigde binnendeuren maken een huis ouder dan het is. Verven is een klus die je zelf kunt doen, maar het verschil tussen een strak resultaat en een deur vol strepen zit in het voorwerk en de goede lak. Hier lees je hoe je het aanpakt, en wanneer je de deuren beter kunt laten spuiten.",
"kort_antwoord": "Ontvet en schuur de deur, vul beschadigingen en gron kale plekken. Lak de deur daarna met een watergedragen, slijtvaste binnenlak: eerst de randen, dan de panelen of het vlak met een lakroller, en strijk na met een kwast of roller in één richting. Twee lagen, licht schuren ertussen. Vlakke deuren worden het strakst als ze gespoten worden; een schilder rekent daarvoor €95 tot €185 per deur.",
"secties": [
("Welke lak voor binnendeuren?",
"""<p>Op binnendeuren hoort een <strong>slijtvaste binnenlak</strong>. Watergedragen lak heeft binnen de voorkeur: hij ruikt weinig, droogt snel en vergeelt minder dan lak op terpentinebasis. Het technische blad van een slijtvaste watergedragen binnenlak noemt toepassing op deuren, kozijnen, trappen en meubels, en een hoge weerstand tegen krassen en stoten.</p>
<p>Op kaal hout of MDF komt eerst een grondverf. Een watergedragen grondverf is volgens het technische blad na ongeveer 6 uur overschilderbaar. Op een oude laag terpentineverf die nog goed vastzit, kun je watergedragen lak zetten, mits je goed ontvet en schuurt. Twijfel je over de ondergrond, lees dan <a href="/kennisbank/grondverf-of-voorlak/">grondverf of voorlak</a>.</p>"""),
("Glans: mat, zijdeglans of hoogglans?",
"""<p>Zijdeglans is de meest gekozen glans voor binnendeuren: goed schoon te houden en vergevingsgezind. Mat oogt modern, maar laat vlekken van handen sneller zien. Hoogglans geeft een klassieke uitstraling, maar elke oneffenheid valt op, vooral op een vlakke deur met strijklicht van een raam.</p>"""),
("Rollen, kwasten of spuiten?",
"""<div class="tablewrap"><table>
<thead><tr><th>Methode</th><th>Resultaat</th><th>Geschikt voor</th></tr></thead>
<tbody>
<tr><td><strong>Lakroller (vilt of schuim)</strong></td><td>Glad, met een fijne structuur</td><td>Vlakke deuren, zelf doen</td></tr>
<tr><td><strong>Kwast</strong></td><td>Zichtbare streken als je niet goed naloopt</td><td>Panelen, profielen, randen</td></tr>
<tr><td><strong>Spuiten</strong></td><td>Strak en glad, als nieuw</td><td>Vlakke deuren, veel deuren tegelijk, in de werkplaats</td></tr>
</tbody></table></div>
<p>Bij zelf verven werk je het snelst met een combinatie: de kwast voor randen en profielen, de roller voor de vlakken. Spuiten doet een schilder meestal in de werkplaats. De deuren gaan dan een paar dagen weg. Wat dat kost, zie je bij <a href="/kosten/deuren-spuiten/">deuren spuiten</a>.</p>"""),
("De volgorde bij een paneeldeur",
"""<ol>
<li>De profielen rond de panelen, met de kwast.</li>
<li>De panelen zelf.</li>
<li>De middenstijl en de dwarsregels.</li>
<li>De buitenste stijlen, van boven naar beneden.</li>
<li>De randen van de deur, als laatste.</li>
</ol>
<p>Werk nat-in-nat en strijk elk vlak na in de richting van de nerf of de lengte van het deel. Zo voorkom je aanzetten. Lakken op een warme dag of bij de verwarming droogt sneller, en dan zie je eerder strepen. Werk liever bij een gewone kamertemperatuur.</p>"""),
("En het kozijn?",
"""<p>Een witte deur in een vergeeld kozijn valt op. Neem het kozijn daarom in dezelfde ronde mee. Een kozijn schilder je ter plekke met de kwast. Begin bovenaan en werk naar beneden; de onderkant van de stijlen krijgt de meeste klappen van stofzuiger en schoenen, dus geef die extra aandacht. Een schilder rekent €35 tot €75 per binnenkozijn.</p>"""),
("Rekenvoorbeeld: zes deuren en kozijnen",
"""<p>Je hebt zes binnendeuren en zes kozijnen. Zelf verven kost je ongeveer twee liter grondverf en twee liter lak, plus schuurpapier, rollers en kwasten: grofweg €120 tot €200 aan materiaal, en twee tot drie weekenden. Laten doen: zes deuren × €95 – €185 is €570 tot €1.110, en zes kozijnen × €35 – €75 is €210 tot €450. Samen €780 tot €1.560, inclusief verf en 9% btw. Meer prijzen bij <a href="/kosten/binnenschilderwerk/">kosten binnenschilderwerk</a>.</p>"""),
],
"stappen": [
("Haal beslag eraf", "Schroef klinken en schilden eraf. Haal de deur eventueel uit de scharnieren en leg hem op schragen."),
("Ontvet", "Was de deur met een ontvetter, vooral rond de klink. Spoel na en laat drogen."),
("Vul en schuur", "Vul deuken met houtplamuur. Schuur alles mat met korrel 180 tot 240 en maak stofvrij."),
("Gron kale plekken", "Zet grondverf op kaal hout, MDF en plamuurplekken."),
("Eerste laag lak", "Eerst profielen en randen met de kwast, dan de vlakken met de roller. Strijk na in één richting."),
("Licht schuren", "Na droging licht schuren met fijn schuurpapier en stofvrij maken."),
("Tweede laag lak", "Dezelfde volgorde. Laat de deur droog worden voor je hem terughangt."),
],
"kosten": ["deuren-spuiten", "binnenschilderwerk"],
"faq": [
("Welke verf voor binnendeuren?", "Een slijtvaste binnenlak, bij voorkeur watergedragen. Die vergeelt minder en ruikt weinig. Op kaal hout komt eerst grondverf."),
("Moet je een deur schuren voor het verven?", "Ja. Schuren maakt de oude laag mat, zodat de nieuwe lak hecht. Zonder schuren kan de lak later loslaten."),
("Kun je binnendeuren verven zonder strepen?", "Ja, met een lakroller voor de vlakken, nat-in-nat werken en in één richting naloopen. Voor een echt strak resultaat op vlakke deuren: laten spuiten."),
("Hoeveel lagen lak op een binnendeur?", "Twee lagen aflak, met licht schuren ertussen. Op kaal hout eerst een grondlaag."),
("Wat kost binnendeuren laten spuiten?", "€95 tot €185 per deur, inclusief lak en btw. Het kozijn komt er apart bij: €35 tot €75."),
("Kan watergedragen lak over terpentineverf?", "Ja, als de oude laag goed vastzit, ontvet en mat geschuurd is. Twijfel je, zet dan eerst een hechtprimer."),
("Hoe lang moet een gelakte deur drogen?", "Na een paar uur is watergedragen lak droog genoeg om aan te raken, maar hij is pas na enkele dagen helemaal hard. Sluit de deur de eerste dagen voorzichtig."),
],
"bronnen": [SIKKENS_REZISTO, TDS_BL_PRIMER, BELASTINGDIENST],
"gerelateerd": ["verf-op-waterbasis-of-terpentinebasis", "grondverf-of-voorlak", "trap-verven"],
},
# ---------------------------------------------------------------------------
{
"slug": "glaslatten-vervangen",
"groep": "Schade en onderhoud",
"titel": "Glaslatten vervangen of schilderen: zo voorkom je houtrot",
"seo_titel": "Glaslatten vervangen of schilderen: zo werkt het",
"description": "Rotte of losse glaslatten? Hoe je ze herkent, wanneer schilderen genoeg is en wanneer vervangen nodig is, hoe het kitten werkt en wat het kost.",
"kort": "Wanneer glaslatten vervangen moeten, hoe ze gekit worden en wat het kost.",
"foto": "dakkapel-verweerd-houten-kozijn",
"intro": "Glaslatten zijn de smalle latjes die het glas in een houten raam op zijn plek houden. Ze zijn klein, maar ze bepalen of er water achter het glas komt. Een losse of rotte glaslat is een van de bekendste plekken waar houtrot in een kozijn begint. Hier lees je hoe je ziet of ze aan de beurt zijn, wat een schilder eraan doet en wat het kost.",
"kort_antwoord": "Zitten de glaslatten vast, is het hout hard en is alleen de verf verweerd, dan is schuren, kitten en schilderen genoeg. Zijn ze zacht, gescheurd of los, dan moeten ze vervangen worden. De nieuwe latten worden gegrond, met beglazingskit aangesloten op het glas en meegeschilderd. Reken op €8 tot €20 per meter voor vervangen, bovenop het schilderwerk.",
"secties": [
("Wat doet een glaslat?",
"""<p>In een houten raam zit het glas in een sponning. Aan de buitenkant houdt een glaslat het glas vast. Tussen glas en lat zit een kitvoeg of een rubber profiel, zodat er geen water tussen kan lopen. Bij oude ramen zit er geen lat maar stopverf.</p>
<p>Het zwakke punt is de onderste glaslat. Regenwater loopt langs het glas naar beneden en blijft daar liggen. Scheurt de kit of de verf, dan trekt het water de lat en het kozijn in. Binnen een paar jaar kan daar houtrot ontstaan, ook als de rest van het kozijn er nog goed uitziet.</p>"""),
("Zo zie je of ze aan de beurt zijn",
"""<ul class="checklist">
<li><strong>Gescheurde of losse kit</strong> tussen glas en lat.</li>
<li><strong>Afbladderende verf</strong> op de onderste lat, of grijs, kaal hout.</li>
<li><strong>Zacht hout</strong>: prik met een schroevendraaier in de lat en in de hoeken.</li>
<li><strong>Een lat die loskomt</strong> of een spleet tussen lat en kozijn.</li>
<li><strong>Vocht of condens tussen de ruiten</strong> van dubbel glas. Dan is vaak de rand van het glas zelf beschadigd, en dat is een ander probleem.</li>
</ul>
<p>Doe deze check elk voorjaar, samen met de onderdorpels. Voor een snelle inschatting van je hele huis kun je de <a href="/onderhoudscheck/">onderhoudscheck</a> doen.</p>"""),
("Schilderen of vervangen?",
"""<div class="tablewrap"><table>
<thead><tr><th>Situatie</th><th>Wat er gebeurt</th></tr></thead>
<tbody>
<tr><td>Lat zit vast, hout is hard, verf is verweerd</td><td>Schuren, oude kit weg, opnieuw kitten, gronden en schilderen.</td></tr>
<tr><td>Een kleine zachte plek</td><td>Plaatselijk herstellen met houtreparatiemiddel, of alleen die lat vervangen.</td></tr>
<tr><td>Lat is zacht, gescheurd of los</td><td>Lat vervangen. Het kozijn eronder controleren op houtrot.</td></tr>
<tr><td>Sponning onder de lat is ook rot</td><td>Houtrot in het kozijn herstellen, dan nieuwe lat.</td></tr>
</tbody></table></div>
<p>Bij het vervangen haalt de schilder de oude lat voorzichtig weg zonder het glas te beschadigen. De nieuwe lat wordt op maat gezaagd, rondom gegrond (ook de achterkant), vastgezet en met beglazingskit aangesloten op het glas. Daarna gaat hij mee in de verfbeurt. Is het kozijn eronder ook aangetast, lees dan <a href="/kennisbank/houtrot-herkennen-en-herstellen/">houtrot herkennen en herstellen</a>.</p>"""),
("Het kitwerk",
"""<p>De kitvoeg tussen glas en lat is het belangrijkste onderdeel. Een schilder gebruikt een beglazingskit die overschilderbaar is en aan glas en hout hecht. De oude kit moet er helemaal uit; nieuwe kit over oude, gescheurde kit houdt het niet. De verf moet een klein stukje over de kit op het glas doorlopen. Zo sluit de verflaag de naad af en kan er geen water achter komen.</p>
<p>Laat de kitvoeg niet op het laatste moment in de buitenbeurt doen. Kit moet even kunnen uitharden voordat de verf erop komt; op de verpakking staat hoe lang.</p>"""),
("Wat kost glaslatten vervangen?",
"""<p>Een vaste landelijke prijs is er niet. Schilders rekenen het meestal per meter of per raam, als onderdeel van de buitenbeurt. Onze eigen inschatting: €8 tot €20 per meter glaslat, inclusief gronden en kitten, en exclusief het schilderen van het kozijn. Een raam van 1 bij 1,2 meter heeft rondom ongeveer 4,4 meter lat; vaak is alleen de onderste lat van 1 meter aan de beurt.</p>
<p><strong>Rekenvoorbeeld:</strong> bij een buitenbeurt van acht kozijnen vervangt de schilder bij zes ramen de onderste glaslat, samen 7 meter. Dat is €56 tot €140 extra. Het kozijn zelf kost €90 tot €190 per stuk. Hout dat vervangen wordt, valt onder 21% btw; het schilderwerk aan een woning ouder dan twee jaar onder 9%. Zie ook <a href="/kosten/kozijnen-schilderen/">kozijnen schilderen</a>.</p>"""),
],
"stappen": [
("Controleer de latten", "Kijk naar kit en verf, prik met een schroevendraaier in de onderste latten en de hoeken."),
("Verwijder oude kit", "Snijd oude, gescheurde kit tussen glas en lat helemaal weg."),
("Vervang wat zacht is", "Wip rotte latten voorzichtig los zonder het glas te raken. Controleer de sponning eronder."),
("Gron de nieuwe lat rondom", "Ook de achterkant en de kopse kanten, want daar trekt het water in."),
("Zet vast en kit af", "Zet de lat vast en sluit hem met overschilderbare beglazingskit aan op het glas."),
("Schilder over de kit", "Laat de kit uitharden en schilder dan, met de verf een klein stukje over de kit op het glas."),
],
"kosten": ["kozijnen-schilderen", "houtrot-herstellen"],
"faq": [
("Wat kost glaslatten vervangen?", "Reken op €8 tot €20 per meter, inclusief gronden en kitten. Dat is een eigen inschatting; het schilderwerk van het kozijn komt erbij."),
("Moet je glaslatten schilderen?", "Ja. Glaslatten horen bij het kozijn en krijgen dezelfde verfbeurt. De verf moet een klein stukje over de kit doorlopen."),
("Waarom rotten glaslatten zo snel?", "Regenwater loopt langs het glas naar de onderste lat. Scheurt de kit of de verf, dan trekt het water in het hout."),
("Kan ik glaslatten zelf vervangen?", "Het kan, maar het glas kan breken als je de oude lat loswrikt. Bij dubbel glas en grote ruiten laat je het beter aan een vakman over."),
("Wat is beter: stopverf of glaslatten met kit?", "Bij oude, enkele beglazing zit vaak stopverf. Bij dubbel glas worden glaslatten met kit of rubber gebruikt. Bij een monument kan stopverf verplicht zijn."),
("Welke btw betaal ik over nieuwe glaslatten?", "Het vervangen van hout valt onder 21%, het schilderwerk aan een woning ouder dan twee jaar onder 9%. Een nette offerte splitst dat."),
],
"bronnen": [TDS_PRIMER, TDS_BL_PRIMER, BELASTINGDIENST],
"gerelateerd": ["houtrot-herkennen-en-herstellen", "kozijnen-schuren-en-voorbereiden", "hoe-vaak-buitenschilderwerk"],
},
# ---------------------------------------------------------------------------
{
"slug": "muur-plamuren",
"groep": "Voorbereiden en uitvoeren",
"titel": "Muur plamuren voor het schilderen: gaten, scheuren en glad maken",
"seo_titel": "Muur plamuren voor het schilderen: zo doe je het",
"description": "Gaten en scheuren vullen of een hele muur glad plamuren voor het schilderen? Welke vuller, hoe dik per laag, droogtijd, schuren en wat een schilder rekent.",
"kort": "Welke vuller, hoe dik per laag, hoe lang drogen en hoe je strak schuurt voor het verven.",
"foto": "muur-afplakken-en-verven-gele-kleur",
"intro": "Verf verbergt niets. Elk gaatje van een schilderijhaak en elke scheur zie je na het schilderen nog steeds, en met strijklicht zelfs beter. Plamuren is daarom het belangrijkste voorwerk voor een strakke muur. Hier lees je welk product je gebruikt, hoe je gaten en scheuren vult, wanneer je een hele muur glad moet maken en wat dat kost als je het laat doen.",
"kort_antwoord": "Kleine gaten en scheuren vul je met een muurvuller, in lagen van maximaal 1 cm. Na droging schuur je de plek glad en stofvrij, en zet je er een voorstrijk of eerste laag muurverf op. Is de hele muur ruw of ongelijk, dan gebruik je een egaliseerplamuur die je in dunne lagen over de muur rolt en glad strijkt. Een schilder rekent €3 tot €8 per m² extra voor vullen en plamuren.",
"secties": [
("Vullen of glad plamuren?",
"""<p>Er zijn twee soorten werk die allebei plamuren heten:</p>
<ul>
<li><strong>Vullen</strong>: losse gaten, scheuren en beschadigingen dichtmaken met een muurvuller. Dat is bijna altijd nodig.</li>
<li><strong>Egaliseren</strong>: een hele muur van een dunne laag voorzien, zodat hij glad wordt. Dat is nodig bij ruwe muren, oude verflagen met randen, of na het verwijderen van behang.</li>
</ul>
<p>Een muur met spachtelputz of een grove structuur maak je niet glad met plamuur. Dat is werk voor een stukadoor.</p>"""),
("Gaten en scheuren vullen",
"""<p>Een veelgebruikte muurvuller heeft volgens de productinformatie een maximale laagdikte van 1 cm en een maximale diepte van 2 cm. Diepere gaten vul je in meerdere lagen, met droogtijd ertussen. Bij een laag van 5 mm is het product na ongeveer 30 minuten overschilderbaar bij 20 °C. Hij hecht op steen, beton, gipsplaat en stucwerk, maar niet op metaal, kunststof of een vochtige ondergrond. Verwerk hem niet onder 5 °C.</p>
<p>Zo pak je het aan:</p>
<ul>
<li>Haal losse stukjes stuc en oude pluggen weg.</li>
<li>Maak scheuren iets wijder met de punt van een plamuurmes, zodat de vuller er goed in komt.</li>
<li>Druk de vuller stevig in het gat en strijk hem af met een vochtig plamuurmes, iets boller dan de muur.</li>
<li>Laat drogen en schuur hem vlak met fijn schuurpapier op een schuurblok.</li>
</ul>
<p>Scheuren die steeds terugkomen, bijvoorbeeld bij de aansluiting van muur en plafond, kun je beter met acrylaatkit afkitten. Die blijft elastisch.</p>"""),
("Een hele muur glad maken",
"""<p>Voor een hele muur is er rolbare egaliseerplamuur. Volgens de productinformatie van zo'n product breng je maximaal 2 mm per laag aan, is het na 8 tot 12 uur droog en is het schuurbaar. Je hebt ongeveer 30 minuten om het glad te strijken voordat het te stug wordt. Met 5 liter doe je ongeveer 12 m² op een licht beschadigde muur.</p>
<p>Je rolt de plamuur in banen op de muur en trekt hem direct glad met een breed plamuurmes of een spaan. Werk van boven naar beneden en houd een natte rand aan. Vaak zijn twee dunne lagen beter dan één dikke. Daarna schuur je de muur glad, het liefst met een schuurmachine met stofafzuiging.</p>"""),
("Schuren en stof",
"""<p>Schuren geeft veel fijn stof. Werk met een stofmasker, zet een raam open en dek vloer en meubels af. Zuig de muur daarna af met een zachte borstel of neem hem af met een licht vochtige doek. Stof op de muur zorgt dat de verf slecht hecht en geeft korreltjes in je verflaag.</p>
<p>Kijk voor het schilderen of het goed is: houd een lamp of zaklamp schuin langs de muur. Dan zie je elke oneffenheid zoals je hem later in strijklicht ook ziet.</p>"""),
("Voorstrijken na het plamuren",
"""<p>Plamuurplekken zuigen anders dan de rest van de muur. Zonder voorstrijk zie je ze door de muurverf heen als doffe vlekken. Zet daarom eerst een voorstrijk, of minstens een eerste laag verdunde muurverf over de plekken. Een watergedragen voorstrijk dekt volgens het technische blad ongeveer 12 m² per liter. Meer over voorstrijken lees je in <a href="/kennisbank/nieuw-stucwerk-schilderen/">nieuw stucwerk schilderen</a>.</p>"""),
("Wat kost plamuren door een schilder?",
"""<p>Gaten en scheuren vullen rekent een schilder meestal mee in de prijs per m², of als toeslag van €3 tot €8 per m². Bij een muur van 15 m² die veel gaten heeft en gedeeltelijk geëgaliseerd moet worden, komt dat op €45 tot €120 bovenop €150 tot €240 voor het schilderen (€10 tot €16 per m²). Is de muur echt slecht, dan is een stukadoor vaak de betere keuze. Meer prijzen bij <a href="/kosten/schilderen-per-m2/">schilderen per m²</a>.</p>"""),
],
"stappen": [
("Maak de muur schoon", "Haal spijkers, pluggen en loszittend stucwerk weg en neem de muur af."),
("Vul gaten en scheuren", "Druk muurvuller in de gaten, maximaal 1 cm per laag. Diepe gaten in meerdere lagen."),
("Egaliseer als het nodig is", "Rol egaliseerplamuur in dunne lagen op ruwe delen en strijk hem glad."),
("Laat drogen", "Kleine plekken zijn na ongeveer 30 minuten droog, een egaliseerlaag na 8 tot 12 uur. Kijk op de verpakking."),
("Schuur en maak stofvrij", "Schuur vlak met fijn schuurpapier, zuig af en controleer met strijklicht."),
("Voorstrijken", "Zet een voorstrijk of eerste laag over de plamuurplekken, dan twee lagen muurverf."),
],
"kosten": ["schilderen-per-m2", "binnenschilderwerk"],
"faq": [
("Hoe dik mag je plamuren?", "Een muurvuller tot ongeveer 1 cm per laag, een egaliseerplamuur tot 2 mm per laag. Kijk op de verpakking van je product."),
("Hoe lang moet plamuur drogen voor je kunt schilderen?", "Een sneldrogende muurvuller is bij een dunne laag na ongeveer 30 minuten overschilderbaar. Een egaliseerlaag heeft 8 tot 12 uur nodig."),
("Moet je plamuur voorstrijken?", "Ja, of minstens een eerste laag muurverf over de plekken zetten. Anders zie je ze als doffe vlekken door de verf."),
("Wat is het verschil tussen plamuren en stucen?", "Plamuren is dunne lagen vullen en egaliseren. Stucen is een nieuwe pleisterlaag van enkele millimeters tot centimeters. Bij een slechte muur is stucen beter."),
("Kan ik over behang plamuren?", "Nee. Haal het behang eerst weg. Zie behang verwijderen."),
("Wat kost een muur laten plamuren?", "Bij een schilder meestal €3 tot €8 per m² extra bovenop het schilderwerk. Een hele muur strak laten stucen is duurder."),
],
"bronnen": [ALAB_MUURVULLER, ALAB_MUURVULLER_WEB, ALAB_MUURGLAD, TDS_VOORSTRIJK, TDS_MUURVERF],
"gerelateerd": ["nieuw-stucwerk-schilderen", "behang-verwijderen", "plafond-schilderen-zonder-strepen"],
},
# ---------------------------------------------------------------------------
{
"slug": "oude-verf-verwijderen",
"groep": "Voorbereiden en uitvoeren",
"titel": "Oude verf verwijderen van hout: schuren, afbijten of föhnen",
"seo_titel": "Oude verf verwijderen van hout: schuren of afbijten?",
"description": "Oude verf van kozijnen, deuren of een trap verwijderen? Schuren, afbijten of met een verfföhn, wanneer het nodig is, waar je op let met lood en wat het kost.",
"kort": "Wanneer alles eraf moet en hoe je dat doet met schuren, afbijtmiddel of een verfföhn.",
"foto": "wit-kozijn-afbladderend-oude-gevel",
"intro": "Bij de meeste schilderbeurten hoeft de oude verf er niet af. Opschuren en een nieuwe laag erop is genoeg. Maar soms bladdert het zo erg, of zitten er zoveel lagen op, dat alles weg moet. Dat is het zwaarste werk van een schilderklus. Hier lees je wanneer het echt nodig is, welke methode bij welk hout past en waar je op let in een oud huis.",
"kort_antwoord": "Oude verf verwijder je alleen als hij bladdert, scheurt of in dikke lagen zit. Kleine plekken schraap en schuur je weg. Grote vlakken haal je eraf met een verfföhn en een krabber, of met afbijtmiddel op lastige profielen. Daarna schuren, ontvetten en het hout opnieuw opbouwen met grondverf, voorlak en aflak. In huizen van vóór de jaren zestig kan oude verf lood bevatten: werk dan stofarm en houd kinderen uit de buurt.",
"secties": [
("Moet alles er echt af?",
"""<p>Nee, meestal niet. Een verflaag die goed vastzit is een prima ondergrond. Je schuurt hem mat, werkt kale plekken bij en lakt eroverheen. Alles verwijderen is alleen nodig als:</p>
<ul>
<li>de verf over grote delen <strong>bladdert of loslaat</strong>, ook als je er met tape aan trekt;</li>
<li>er zoveel <strong>lagen</strong> op zitten dat ramen en deuren klemmen of profielen dichtgeslibd zijn;</li>
<li>de oude laag <strong>craquelé</strong> of diepe scheuren heeft;</li>
<li>je van dekkende verf naar <strong>transparante beits of lak</strong> wilt.</li>
</ul>
<p>Waarom verf bladdert, en wat dat zegt over je hout, lees je in <a href="/kennisbank/verf-bladdert-af/">verf bladdert af</a>.</p>"""),
("De methodes naast elkaar",
"""<div class="tablewrap"><table>
<thead><tr><th>Methode</th><th>Goed voor</th><th>Let op</th></tr></thead>
<tbody>
<tr><td><strong>Schrapen en schuren</strong></td><td>Losse plekken, dunne lagen, vlakke delen</td><td>Veel stof. Gebruik een schuurmachine met afzuiging.</td></tr>
<tr><td><strong>Verfföhn (heteluchtpistool) en krabber</strong></td><td>Dikke lagen op kozijnen, deuren en planken</td><td>Niet te heet: hout kan schroeien en glas kan springen. Niet bij oude verf met lood.</td></tr>
<tr><td><strong>Afbijtmiddel</strong></td><td>Profielen, spijlen, houtsnijwerk, meubels</td><td>Ventileren, handschoenen, en het hout goed neutraliseren voor je schildert.</td></tr>
<tr><td><strong>Infrarood verfverwijderaar</strong></td><td>Grote vlakken en oude panden</td><td>Werkt op lagere temperatuur dan een föhn. Duur in aanschaf.</td></tr>
</tbody></table></div>"""),
("Werken met een verfföhn",
"""<p>Een verfföhn maakt de verf zacht, zodat je hem met een krabber in één beweging wegschuift. Houd de föhn in beweging en niet te dicht op het hout. Zodra de verf blaasjes trekt, krab je hem weg. Werk bij ramen met een glasbeschermer of ver van het glas, want door de hitte kan het glas springen. Na het föhnen blijven er altijd resten zitten; die schuur je weg.</p>"""),
("Werken met afbijtmiddel",
"""<p>Afbijtmiddel lost de verf chemisch op. Je smeert een dikke laag op, laat het de tijd op de verpakking inwerken en schraapt de verf weg met een plamuurmes of staalwol. Op profielen en spijlen werkt het beter dan schuren. Werk buiten of met de ramen open, draag handschoenen en een veiligheidsbril, en volg de verpakking voor het naspoelen of neutraliseren. Resten afbijtmiddel in het hout kunnen ervoor zorgen dat nieuwe verf niet hecht.</p>"""),
("Pas op met lood in oude huizen",
"""<p>Verf bevat tegenwoordig geen lood meer. Maar in huizen die vóór de jaren zestig zijn gebouwd, kunnen onder de bovenste lagen nog oude verflagen met lood zitten. Bij schuren en föhnen komt lood vrij als stof en damp. Dat is vooral schadelijk voor jonge kinderen en zwangere vrouwen.</p>
<p>De GGD adviseert om te zorgen dat er geen kinderen in de buurt zijn als oude loodhoudende verf wordt geschuurd of verwijderd, en om de ruimte daarna schoon te maken met een natte doek in plaats van te stofzuigen of vegen. Twijfel je of er lood in de verf zit? Laat een schilder kijken. Een vakman werkt dan nat of met afzuiging, en vaak met afbijtmiddel in plaats van hitte.</p>"""),
("Na het verwijderen: het hout opnieuw opbouwen",
"""<p>Kaal hout heeft een volledig verfsysteem nodig. Schuur het hout glad, maak het stofvrij en ontvet het. Zet daarna een grondverf, een voorlak en een of twee lagen aflak. Op kaal hout buiten is een grondverf op terpentinebasis volgens het technische blad na ongeveer 18 uur overschilderbaar. Wacht niet te lang met gronden: kaal hout neemt vocht op en vergrijst binnen een paar weken. Meer in <a href="/kennisbank/grondverf-of-voorlak/">grondverf of voorlak</a>.</p>"""),
("Wat kost het om oude verf te laten verwijderen?",
"""<p>Kaal maken is veel werk en wordt vaak per uur gerekend: €45 tot €65 per uur exclusief btw. Een buitenkozijn helemaal kaal maken en opnieuw opbouwen kost al snel twee tot drie keer zoveel als een gewone beurt. Waar een gewone beurt €90 tot €190 per kozijn kost, kom je dan op €200 tot €500. Laat de schilder op de offerte zetten welke kozijnen helemaal kaal gaan en welke alleen geschuurd worden. Zie <a href="/kosten/kozijnen-schilderen/">kozijnen schilderen</a>.</p>"""),
],
"stappen": [
("Test of het moet", "Plak tape op de verf en trek hem eraf. Komt de verf mee, dan moet hij weg. Zo niet, dan is schuren genoeg."),
("Bescherm de omgeving", "Leg folie neer, plak glas af en houd kinderen en huisdieren uit de buurt."),
("Kies je methode", "Föhn voor vlakke delen met dikke lagen, afbijtmiddel voor profielen, schuren voor dunne lagen. Geen hitte bij mogelijk loodhoudende verf."),
("Verwijder de verf", "Krab de zachte verf weg, of schraap het afbijtmiddel met de verf eraf."),
("Schuur na", "Schuur resten en ruwe plekken weg en maak alles stofvrij."),
("Ruim stofarm op", "Neem alles af met een natte doek en gooi het afval weg volgens de regels van je gemeente."),
("Bouw opnieuw op", "Ontvet, gron, zet voorlak en een of twee lagen aflak."),
],
"kosten": ["kozijnen-schilderen", "buitenschilderwerk"],
"faq": [
("Moet oude verf er altijd af voor het schilderen?", "Nee. Zit de verf goed vast, dan is mat schuren genoeg. Alleen bladderende of zeer dikke lagen moeten eraf."),
("Wat is de snelste manier om verf van hout te halen?", "Op vlakke delen met dikke lagen werkt een verfföhn met een krabber het snelst. Op profielen is afbijtmiddel handiger."),
("Kan ik verf afbranden in een oud huis?", "Beter niet als de verf lood kan bevatten, in huizen van vóór de jaren zestig. Laat dan een vakman kijken."),
("Hoe weet ik of er lood in mijn verf zit?", "Dat zie je niet. In huizen van vóór de jaren zestig is de kans groter. Een schilder of laboratorium kan het testen."),
("Wat doe je na het afbijten?", "Het hout naspoelen of neutraliseren volgens de verpakking, laten drogen, schuren en opnieuw opbouwen met grondverf."),
("Wat kost een kozijn kaal laten maken?", "Vaak €200 tot €500 per kozijn inclusief opnieuw schilderen, tegen €90 tot €190 voor een gewone beurt. Het wordt vaak per uur gerekend."),
],
"bronnen": [GGD_LOOD, TDS_PRIMER, TDS_BL_PRIMER],
"gerelateerd": ["verf-bladdert-af", "kozijnen-schuren-en-voorbereiden", "grondverf-of-voorlak"],
},
# ---------------------------------------------------------------------------
{
"slug": "beits-of-verf",
"groep": "Verf kiezen",
"titel": "Beits of verf: wat kies je voor buitenhout?",
"seo_titel": "Beits of verf voor buitenhout: wat kies je?",
"description": "Transparante beits, dekkende beits of verf? Het verschil, wat bij een schutting, gevelbetimmering of kozijn past, hoe lang het meegaat en hoe je onderhoudt.",
"kort": "Het verschil tussen transparante beits, dekkende beits en verf, en wat bij welk hout past.",
"foto": "verweerde-blauwe-houten-schutting",
"intro": "Beits en verf beschermen allebei hout, maar ze werken anders. Verf vormt een dichte, glanzende laag op het hout. Beits trekt meer in het hout en laat vocht beter door. Welke je kiest, hangt af van wat je schildert: een schutting, een houten gevel of een kozijn. Hier lees je het verschil, wat de fabrikanten zeggen over duurzaamheid en hoe je het onderhoud plant.",
"kort_antwoord": "Kies verf voor kozijnen, ramen en deuren: hout dat precies moet passen en een dichte, glanzende laag nodig heeft. Kies beits voor schuttingen, tuinhuizen en gevelbetimmering: hout dat mag werken en waar je geen dikke laag wilt die kan bladderen. Dekkende beits geeft kleur en beschermt tegen uv; transparante beits laat de houtnerf zien, maar moet vaker onderhouden worden.",
"secties": [
("Het verschil in het kort",
"""<div class="tablewrap"><table>
<thead><tr><th></th><th>Transparante beits</th><th>Dekkende beits</th><th>Verf (lak)</th></tr></thead>
<tbody>
<tr><td><strong>Uiterlijk</strong></td><td>Houtnerf zichtbaar</td><td>Egale kleur, structuur blijft zichtbaar</td><td>Egale, gesloten laag</td></tr>
<tr><td><strong>Glans</strong></td><td>Mat tot zijdeglans</td><td>Mat tot zijdeglans</td><td>Zijdeglans tot hoogglans</td></tr>
<tr><td><strong>Vochtregulerend</strong></td><td>Ja</td><td>Ja</td><td>Minder; vormt een dichte film</td></tr>
<tr><td><strong>Bij slijtage</strong></td><td>Verweert, wordt dunner</td><td>Verweert, bladdert zelden</td><td>Kan bladderen als er vocht achter komt</td></tr>
<tr><td><strong>Past bij</strong></td><td>Hardhout, ceder, tuinmeubels</td><td>Schuttingen, tuinhuizen, gevelbetimmering</td><td>Kozijnen, ramen, deuren</td></tr>
</tbody></table></div>"""),
("Wat zeggen de productbladen?",
"""<p>Twee voorbeelden van dekkende beits uit actuele productinformatie:</p>
<ul>
<li>Een <strong>watergedragen dekkende beits voor gevelhout</strong> is volgens de fabrikant geschikt voor hard- en zachthout zoals gevelbetimmering en rabatdelen. Het rendement is ongeveer 10 m² per liter. Bij 20 °C is hij na 4 uur overschilderbaar en na 7 dagen doorgehard. Niet verwerken onder 10 °C of boven 25 °C. De verwachte duurzaamheid is 7 jaar in een systeem van drie lagen.</li>
<li>Een <strong>dekkende tuinbeits op alkydbasis</strong> is volgens het productblad bedoeld als grond-, tussen- en aflaag in één (één-pot-systeem), voor tuinmeubels, tuinhuizen, schuttingen, pergola's en gevelbetimmering. Theoretisch rendement 16 m² per liter, in de praktijk 60 tot 85% daarvan. Overschilderbaar na ongeveer 18 uur, te verwerken vanaf 5 °C. Onderhoud: tot 5 jaar.</li>
</ul>
<p>Let op het verschil tussen theoretisch en praktisch rendement. Ruw, zagend hout neemt veel meer beits op dan geschaafd hout. Koop daarom liever iets te veel.</p>"""),
("Transparant: mooi, maar meer onderhoud",
"""<p>Transparante beits laat de nerf van het hout zien, en dat is precies waarom mensen ervoor kiezen. Omdat er weinig pigment in zit, komt er meer zonlicht bij het hout. Dat breekt de bovenkant van het hout langzaam af. Transparante beits moet daarom vaker bijgewerkt worden dan dekkende beits. Helemaal kleurloze beits of lak raden fabrikanten buiten meestal niet aan, juist vanwege die uv-straling.</p>"""),
("Kun je beits overschilderen met verf, of andersom?",
"""<p>Van beits naar verf kan, als de beitslaag goed is verweerd of geschuurd, het hout schoon en vetvrij is en je met een geschikte grondverf begint. Van verf naar beits is lastiger: beits moet in het hout kunnen trekken, en dat lukt niet door een verflaag heen. Dan moet de verf er eerst helemaal af. Hoe je dat doet, lees je in <a href="/kennisbank/oude-verf-verwijderen/">oude verf verwijderen</a>.</p>
<p>Blijf je bij hetzelfde systeem, dan is onderhoud makkelijk: reinigen, licht opschuren en een nieuwe laag. Een schutting beitsen kost bij een schilder €8 tot €20 per m²; zie <a href="/kosten/schutting-beitsen/">schutting beitsen</a>.</p>"""),
("Welke kleur?",
"""<p>Donkere kleuren worden in de zon warmer, en daardoor werkt het hout meer. Bij dekkende beits is dat minder een probleem dan bij verf, omdat beits niet snel bladdert. Een zwarte of antraciet gevelbetimmering is daarom meestal met dekkende beits gedaan. Kijk voor kleuren bij de <a href="/inspiratie/">inspiratiegids</a>.</p>"""),
("Rekenvoorbeeld: schutting van 20 meter",
"""<p>Een schutting van 20 meter lang en 1,8 meter hoog is 36 m² aan één kant, 72 m² aan twee kanten. In twee lagen is dat 144 m² beitswerk. Bij een praktisch rendement van ongeveer 10 m² per liter heb je zo'n 14 tot 15 liter nodig; op ruw hout meer. Zelf doen kost je vooral tijd. Laten doen: 72 m² × €8 – €20 is €576 tot €1.440, inclusief beits en btw.</p>"""),
],
"stappen": [
("Kies het systeem", "Verf voor kozijnen en deuren, dekkende beits voor schutting en gevel, transparante beits als je de nerf wilt zien."),
("Reinig en ontvet", "Borstel vuil en groene aanslag weg en ontvet het hout. Laat het droog worden."),
("Schuur", "Schuur in de richting van de nerf en rond scherpe randen af. Maak stofvrij."),
("Breng de eerste laag aan", "Werk in de lengte van de planken en zet de beits goed in de kopse kanten."),
("Tweede en derde laag", "Houd de overschilderbare tijd van het blik aan. Bij een nieuw systeem: twee à drie lagen."),
("Plan het onderhoud", "Controleer elk jaar en werk bij voordat het hout kaal wordt."),
],
"kosten": ["schutting-beitsen", "gevel-schilderen"],
"faq": [
("Wat is het verschil tussen beits en verf?", "Verf vormt een dichte laag op het hout, beits trekt meer in en laat vocht beter door. Verf kan bladderen als er vocht achter komt; beits verweert en wordt dunner."),
("Is beits beter dan verf?", "Niet beter, wel anders. Beits past bij hout dat mag werken, zoals schuttingen en gevelbetimmering. Verf past bij kozijnen en deuren."),
("Hoe lang gaat dekkende beits mee?", "Volgens productbladen 5 tot 7 jaar bij een goed opgebouwd systeem. De zonkant gaat sneller."),
("Kun je over beits verven?", "Ja, als de beits verweerd of geschuurd is en je begint met een geschikte grondverf."),
("Kun je beits over verf zetten?", "Nee, beits moet in het hout trekken. De verf moet er eerst helemaal af."),
("Hoeveel lagen beits heb je nodig?", "Op kaal hout twee à drie lagen. Bij onderhoud vaak één laag."),
("Wat kost een schutting laten beitsen?", "€8 tot €20 per m², inclusief beits en btw."),
],
"bronnen": [CETABEVER_BEITS, WIJZONOL_BEITS, TDS_PRIMER],
"gerelateerd": ["welke-verf-voor-kozijnen", "verf-op-waterbasis-of-terpentinebasis", "oude-verf-verwijderen"],
},
# ---------------------------------------------------------------------------
{
"slug": "schilderwerk-vve",
"groep": "Offerte, kosten en btw",
"titel": "Schilderwerk bij een VvE: MJOP, reservefonds en offertes",
"seo_titel": "Schilderwerk VvE: MJOP, reservefonds en offertes",
"description": "Schilderwerk regelen als VvE? Hoe het meerjarenonderhoudsplan werkt, wat er in het reservefonds moet, hoe je offertes vergelijkt en wat buitenschilderwerk kost.",
"kort": "Hoe een VvE schilderwerk plant met een MJOP, het reservefonds gebruikt en offertes vergelijkt.",
"foto": "villa-in-de-steigers-voorgevel-elburg",
"intro": "In een appartementencomplex is het buitenschilderwerk van iedereen. De Vereniging van Eigenaren (VvE) regelt het, betaalt het uit het reservefonds en kiest de schilder. Dat vraagt om planning: schilderwerk is bij veel complexen een van de grootste terugkerende posten. Hier lees je hoe het meerjarenonderhoudsplan werkt, wat de wet zegt over reserveren en hoe je als bestuur offertes vergelijkt.",
"kort_antwoord": "Een VvE moet volgens de Rijksoverheid geld reserveren voor groot onderhoud, op basis van een meerjarenonderhoudsplan (MJOP) of minimaal 0,5% van de herbouwwaarde per jaar. Buitenschilderwerk staat in een MJOP meestal elke zes tot acht jaar ingepland. Laat ruim op tijd een opname doen, vraag minstens drie offertes op hetzelfde bestek en leg de keuze voor aan de vergadering.",
"secties": [
("Wat zegt de wet over het reservefonds?",
"""<p>Een VvE is verplicht geld te reserveren voor groot onderhoud, zoals schilderwerk, dak en gevel. Dat geld staat in het reservefonds, op een aparte rekening. Volgens de Rijksoverheid bepaalt de VvE het bedrag op een van twee manieren:</p>
<ul>
<li>met een <strong>meerjarenonderhoudsplan (MJOP)</strong>, dat beschrijft welk onderhoud er de komende tien jaar nodig is, wanneer en wat het kost;</li>
<li>of met een <strong>percentage van de herbouwwaarde</strong> van het gebouw, minimaal 0,5% per jaar. De herbouwwaarde staat op de polis van de opstalverzekering.</li>
</ul>
<p>De eigenaren betalen het reservefonds mee via hun maandelijkse VvE-bijdrage. Een MJOP geeft meer houvast dan een vast percentage, omdat je per onderdeel ziet wanneer het geld nodig is.</p>"""),
("Schilderwerk in het MJOP",
"""<p>In een MJOP staat buitenschilderwerk meestal als terugkerende post: elke zes tot acht jaar een volledige beurt, met daartussen een kleine beurt of inspectie. Houten kozijnen, boeidelen, deuren en balkonhekken staan er vaak apart in. Zo'n plan is een schatting. Laat daarom een jaar voor de geplande beurt een schilder of adviseur kijken naar de werkelijke staat. Soms kan het een jaar later, soms moet het eerder.</p>
<p>Over hoe vaak schilderwerk nodig is en waar het van afhangt, lees je in <a href="/kennisbank/hoe-vaak-buitenschilderwerk/">hoe vaak buitenschilderwerk</a>.</p>"""),
("Zo regel je het schilderwerk als bestuur",
"""<ol>
<li><strong>Opname.</strong> Laat de staat van het schilderwerk vastleggen, met foto's en een lijst van houtrot.</li>
<li><strong>Bestek of werkomschrijving.</strong> Zet op papier wat er moet gebeuren: welke onderdelen, voorbehandeling, verfsysteem, aantal lagen, steigers, en hoe houtrot wordt afgerekend.</li>
<li><strong>Offertes.</strong> Vraag minstens drie schilders om een prijs op hetzelfde bestek. Dan kun je echt vergelijken.</li>
<li><strong>Besluit.</strong> Leg de keuze voor aan de ledenvergadering, of volg wat de splitsingsakte en het reglement zeggen over wie mag beslissen.</li>
<li><strong>Uitvoering en oplevering.</strong> Spreek een contactpersoon af en loop bij de oplevering samen rond.</li>
</ol>"""),
("Offertes vergelijken: waar let je op?",
"""<ul class="checklist">
<li><strong>Zelfde werk, zelfde aantallen.</strong> Vergelijk per onderdeel, niet alleen het totaal.</li>
<li><strong>Houtrot:</strong> prijs per plek of een stelpost met een maximum.</li>
<li><strong>Steigers en hoogwerker:</strong> inbegrepen, en hoe lang ze staan.</li>
<li><strong>Verfsysteem:</strong> merk, product en aantal lagen.</li>
<li><strong>Garantie:</strong> termijn en wat eronder valt.</li>
<li><strong>Planning:</strong> wanneer, hoe lang en wat bewoners merken.</li>
<li><strong>Btw:</strong> 9% voor schilderwerk aan woningen ouder dan twee jaar, ook bij een VvE.</li>
</ul>
<p>Plak een ontvangen offerte in de <a href="/offerte-vergelijken/">offertechecker</a> om de posten naast de richtprijzen te leggen. De opdracht valt onder de regels voor aanneming van werk in het Burgerlijk Wetboek. Meer over goede offertes in <a href="/kennisbank/goede-offerte-schilderwerk/">zo herken je een goede offerte</a>.</p>"""),
("Wat kost buitenschilderwerk voor een VvE?",
"""<p>Bij een complex rekent een schilder per onderdeel: kozijnen, deuren, boeidelen, balkonhekken. De richtprijzen zijn dezelfde als bij een eengezinswoning, maar door de hoeveelheid en de steigers ziet de offerte er anders uit. Homedeal noemt voor de buitengevel van een appartement €1.000 tot €2.000.</p>
<p><strong>Rekenvoorbeeld:</strong> een complex met 12 appartementen, elk met vier buitenkozijnen en een balkondeur. Dat is 48 kozijnen × €90 – €190 en 12 deuren × €100 – €185: €5.520 tot €11.340. Daar komen steigers bij, bijvoorbeeld vier gevels × €300 – €900, en houtrot. Samen grofweg €7.000 tot €15.000, of €580 tot €1.250 per appartement. Bij zes tot acht jaar tussen de beurten is dat €75 tot €210 per appartement per jaar in het reservefonds, alleen voor schilderwerk. Zie <a href="/kosten/buitenschilderwerk/">kosten buitenschilderwerk</a> voor de prijzen per onderdeel.</p>"""),
("Wat valt onder de VvE en wat onder de eigenaar?",
"""<p>Dat staat in de splitsingsakte. Meestal zijn de buitenkant, de gevel, de kozijnen en de gemeenschappelijke ruimtes van de VvE, en het binnenschilderwerk van de eigenaar. Bij kozijnen is het soms verdeeld: de buitenkant van de VvE, de binnenkant van de eigenaar. Kijk het na voordat je een schilder vraagt, zodat de offerte klopt.</p>"""),
],
"stappen": [
("Kijk in het MJOP", "Zoek op wanneer schilderwerk is gepland en hoeveel er in het reservefonds staat."),
("Laat een opname doen", "Laat een jaar voor de geplande beurt de werkelijke staat vastleggen."),
("Maak een werkomschrijving", "Onderdelen, voorbehandeling, verfsysteem, steigers en afrekening van houtrot."),
("Vraag drie offertes", "Op dezelfde werkomschrijving, zodat ze te vergelijken zijn."),
("Besluit in de vergadering", "Leg de offertes en het advies van het bestuur voor."),
("Plan en informeer bewoners", "Spreek data, steigers en bereikbaarheid af en laat bewoners op tijd weten wat er gebeurt."),
("Werk het MJOP bij", "Zet na de oplevering de volgende beurt en de nieuwe kosten in het plan."),
],
"kosten": ["buitenschilderwerk", "huis-schilderen"],
"faq": [
("Is een VvE verplicht om te reserveren voor schilderwerk?", "Een VvE moet reserveren voor groot onderhoud, en schilderwerk hoort daarbij. Het bedrag volgt uit een MJOP of is minimaal 0,5% van de herbouwwaarde per jaar."),
("Is een meerjarenonderhoudsplan verplicht?", "De Rijksoverheid noemt het MJOP als een van de twee manieren om het reservefonds te bepalen. Het andere is een percentage van minimaal 0,5% van de herbouwwaarde."),
("Hoe vaak moet een VvE buitenschilderwerk laten doen?", "Meestal elke zes tot acht jaar, met tussendoor een kleine beurt of inspectie. De werkelijke staat bepaalt het moment."),
("Wie beslist over de keuze van de schilder?", "Dat staat in de splitsingsakte en het huishoudelijk reglement. Vaak beslist de ledenvergadering op voorstel van het bestuur."),
("Betaalt een VvE 9% btw op schilderwerk?", "Ja, voor schilderwerk aan woningen ouder dan twee jaar, ook als de VvE opdrachtgever is."),
("Wat kost buitenschilderwerk per appartement?", "Grofweg €580 tot €1.250 per appartement per beurt, afhankelijk van het aantal kozijnen, steigers en houtrot."),
("Wie betaalt het schilderen van mijn kozijnen binnen?", "Meestal de eigenaar zelf. De buitenkant valt vaak onder de VvE. Kijk in de splitsingsakte."),
],
"bronnen": [RIJKSOVERHEID_VVE, BELASTINGDIENST, BW7, HOMEDEAL_BUITEN],
"gerelateerd": ["goede-offerte-schilderwerk", "hoe-vaak-buitenschilderwerk", "verfschade-en-garantie"],
"extra_links": [("/schilderwerk/zakelijk-schilderwerk/", "Zakelijk schilderwerk en VvE's")],
},
]


# ---------------------------------------------------------------------------
# Verdieping van de vijf dunste bestaande artikelen (november 2026).
# Wordt in kennis_artikelen.py achter de bestaande secties en FAQ gezet.
# ---------------------------------------------------------------------------

VERDIEPING_R5 = {
"goede-offerte-schilderwerk": {
"secties": [
("Voorbeeld: twee offertes naast elkaar",
"""<p>Stel: je vraagt twee schilders om een prijs voor de buitenkant van een tussenwoning. Op het eerste gezicht is offerte A €600 goedkoper. Maar zet je ze per post naast elkaar, dan zie je iets anders.</p>
<div class="tablewrap"><table>
<thead><tr><th>Post</th><th>Offerte A</th><th>Offerte B</th></tr></thead>
<tbody>
<tr><td>8 kozijnen en 2 deuren</td><td class="num">€1.450</td><td class="num">€1.600</td></tr>
<tr><td>Boeidelen 12 m</td><td class="num">€420</td><td class="num">€450</td></tr>
<tr><td>Steiger achtergevel</td><td class="num">niet genoemd</td><td class="num">€550</td></tr>
<tr><td>Houtrot</td><td class="num">op regie</td><td class="num">3 plekken à €110, extra plek €110</td></tr>
<tr><td>Kitwerk glas</td><td class="num">niet genoemd</td><td class="num">inbegrepen</td></tr>
<tr><td>Btw</td><td class="num">21%</td><td class="num">9%</td></tr>
<tr><td><strong>Totaal op papier</strong></td><td class="num"><strong>€2.250</strong></td><td class="num"><strong>€2.850</strong></td></tr>
</tbody></table></div>
<p>Offerte A mist de steiger en het kitwerk, rekent houtrot open af en zet er 21% btw op terwijl 9% hoort. Corrigeer je dat, dan is A niet goedkoper, en weet je bij A nog steeds niet wat de houtrot gaat kosten. Leg je eigen offertes naast de richtprijzen op <a href="/kosten/buitenschilderwerk/">kosten buitenschilderwerk</a>, of laat de <a href="/offerte-vergelijken/">offertechecker</a> het voor je doen.</p>"""),
("Stelposten en meerwerk",
"""<p>Een <strong>stelpost</strong> is een bedrag voor werk dat de schilder vooraf niet precies kan inschatten, zoals houtrot. Dat is normaal, maar spreek af hoe het wordt verrekend: per plek, per uur met een maximum, of met foto's vooraf. <strong>Meerwerk</strong> is werk dat er tijdens de klus bij komt. Laat meerwerk altijd vooraf op papier of per mail bevestigen, met een prijs. Achteraf discussiëren over uren is lastig.</p>
<p>Ook <strong>minderwerk</strong> komt voor: valt een stelpost lager uit, dan hoort het verschil terug te komen op de factuur. Vraag ernaar bij de eindafrekening. Wat je kunt doen als het werk tegenvalt, lees je in <a href="/kennisbank/verfschade-en-garantie/">verfschade en garantie</a>.</p>"""),
("Hoeveel offertes vraag je aan?",
"""<p>Drie is een goed aantal. Met één offerte heb je niets om mee te vergelijken; met vijf of meer kost het veel tijd, en haken schilders soms af. Geef alle schilders dezelfde informatie, het liefst met foto's en een lijstje onderdelen. Dan krijg je offertes die je echt kunt vergelijken. Via <a href="/offerte-aanvragen/">offerte aanvragen</a> kun je in één keer bij maximaal drie schilders uit je regio terecht.</p>"""),
],
"faq": [
("Hoe weet ik of een offerte voor schilderwerk te duur is?", "Vergelijk elke post met de richtprijzen op de kostenpagina's, bijvoorbeeld €90 tot €190 per buitenkozijn. Of plak de offerte in de offertechecker."),
("Moet de steiger in de offerte staan?", "Ja, of er moet staan dat hij er niet in zit. Een offerte zonder steiger lijkt goedkoper, maar is het vaak niet."),
("Wat doe ik als de schilder meerwerk rekent?", "Meerwerk hoort vooraf te worden afgesproken, met een prijs. Vraag om een onderbouwing als het niet was afgesproken."),
],
},
"behang-verwijderen": {
"secties": [
("Rekenvoorbeeld: een woonkamer ontbehangen en schilderen",
"""<p>Een woonkamer met 47 m² muur heeft oud vliesbehang met daaronder een redelijk vlakke stucmuur. Na het verwijderen moeten gaten en kleine beschadigingen worden gevuld, en daarna wordt de muur in twee lagen geschilderd.</p>
<div class="tablewrap"><table>
<thead><tr><th>Post</th><th>Berekening</th><th>Richtprijs</th></tr></thead>
<tbody>
<tr><td>Behang verwijderen</td><td>47 m² × €4 – €10</td><td class="num">€188 – €470</td></tr>
<tr><td>Vullen en plamuren</td><td>47 m² × €3 – €8</td><td class="num">€141 – €376</td></tr>
<tr><td>Voorstrijken en twee lagen muurverf</td><td>47 m² × €10 – €16</td><td class="num">€470 – €752</td></tr>
<tr><td><strong>Totaal</strong></td><td></td><td class="num"><strong>€799 – €1.598</strong></td></tr>
</tbody></table></div>
<p>Het behang verwijderen en het vullen zijn eigen inschattingen; de prijs voor schilderen komt van <a href="/kosten/schilderen-per-m2/">schilderen per m²</a>. Is de muur onder het behang slecht, dan kan stucen goedkoper zijn dan veel plamuurwerk. Hoe je een muur glad maakt, lees je in <a href="/kennisbank/muur-plamuren/">muur plamuren</a>.</p>"""),
("Opnieuw behangen of schilderen?",
"""<p>Na het verwijderen sta je voor de keuze: nieuw behang of verf. Verf is goedkoper en makkelijker bij te werken, maar de muur moet dan wel glad zijn. Behang verbergt meer oneffenheden, zeker structuur- of glasvliesbehang. Glasvlies kun je overschilderen en is sterk, wat handig is in een gang of kinderkamer. Wat behangen kost, zie je op <a href="/schilderwerk/behangen/">behangen</a>.</p>"""),
],
"faq": [
("Is het goedkoper om over behang te schilderen dan het te verwijderen?", "Op korte termijn wel, maar de naden en randen blijven zichtbaar en het behang kan loslaten door het vocht in de verf. Meestal is verwijderen de betere keuze."),
("Kan ik na het verwijderen van behang direct schilderen?", "Pas als de muur droog is, lijmresten weg zijn en gaten gevuld zijn. Zet eerst een voorstrijk."),
],
},
"kozijnen-schuren-en-voorbereiden": {
"secties": [
("Hoeveel tijd kost het voorwerk echt?",
"""<p>Bij een gewone onderhoudsbeurt gaat ongeveer de helft van de tijd naar het voorwerk: reinigen, schuren, losse verf verwijderen, kitten en gronden. Bij een kozijn dat lang niet is geschilderd, kan dat oplopen tot twee derde. Dat verklaart waarom de ene offerte veel hoger is dan de andere: de ene schilder rekent met echt voorwerk, de andere niet.</p>
<div class="tablewrap"><table>
<thead><tr><th>Staat van het kozijn</th><th>Voorwerk</th><th>Gevolg voor de prijs</th></tr></thead>
<tbody>
<tr><td>Licht verweerd, verf zit vast</td><td>Reinigen, mat schuren, één laag aflak</td><td>Onderkant van €90 – €190</td></tr>
<tr><td>Plaatselijk bladderend</td><td>Schrapen, bijschuren, kale plekken gronden en voorlakken</td><td>Midden van de bandbreedte</td></tr>
<tr><td>Grote delen kaal of gescheurd</td><td>Alles eraf, volledig nieuw opbouwen</td><td>Vaak €200 – €500 per kozijn</td></tr>
</tbody></table></div>
<p>Hoe je oude verf er helemaal af haalt, lees je in <a href="/kennisbank/oude-verf-verwijderen/">oude verf verwijderen</a>. Wat de rest van het buitenwerk kost, staat bij <a href="/kosten/kozijnen-schilderen/">kozijnen schilderen</a>.</p>"""),
("Glaslatten en kit: het vergeten voorwerk",
"""<p>Bij het voorbereiden kijkt een goede schilder ook naar de glaslatten en de kitvoegen rond het glas. Gescheurde kit laat water achter de lat lopen, en daar begint houtrot. Oude kit moet er helemaal uit voordat er nieuwe in komt. Rotte glaslatten worden vervangen. Hoe dat gaat en wat het kost, staat in <a href="/kennisbank/glaslatten-vervangen/">glaslatten vervangen</a>.</p>"""),
],
"faq": [
("Waarom is het voorwerk zo duur?", "Omdat het het meeste werk is. Reinigen, schuren, verf verwijderen, kitten en gronden kost vaak de helft van de tijd. Zonder goed voorwerk laat de nieuwe verf snel los."),
("Kan ik het schuren zelf doen om geld te besparen?", "Dat kan, maar spreek het vooraf af. Sommige schilders geven geen garantie als ze het voorwerk niet zelf hebben gedaan."),
],
},
"latex-of-muurverf": {
"secties": [
("Rekenvoorbeeld: hoeveel verf en wat kost het?",
"""<p>Een woonkamer van 5 bij 4 meter en 2,60 meter hoog heeft ongeveer 47 m² muur en 20 m² plafond. In twee lagen is dat 134 m² verfwerk. Met muurverf kom je met een liter ongeveer 8 tot 11 m² ver per laag; het precieze getal staat op het blik. Je hebt dus zo'n 12 tot 17 liter nodig, en op kaal stucwerk nog een voorstrijk.</p>
<p>Zelf doen kost je vooral de verf en een weekend. Laten doen kost €10 tot €16 per m² muur en €12 tot €22 per m² plafond, inclusief verf: €710 tot €1.190 voor deze kamer. Reken je eigen kamer uit met de <a href="/gids/verf-berekenen/">verfcalculator</a>, of kijk bij <a href="/kosten/binnenschilderwerk/">kosten binnenschilderwerk</a> voor een kamer met kozijnen en deuren.</p>"""),
("Welke kleur wit voor muren?",
"""<p>Muurverf in "wit" is per merk anders. Wil je dat muren en lakwerk precies bij elkaar passen, laat dan beide op dezelfde RAL-code mengen, bijvoorbeeld RAL 9010. Het verschil tussen de bekende witten lees je in <a href="/kennisbank/ral-9010-of-ral-9001/">RAL 9010 of RAL 9001</a>.</p>"""),
("Muurverf op een gladde muur na het plamuren",
"""<p>Op plamuurplekken zuigt de muur anders dan op de rest. Zet daar eerst een voorstrijk of een verdunde eerste laag, anders zie je doffe vlekken door de latex heen. Meer daarover in <a href="/kennisbank/muur-plamuren/">muur plamuren</a>.</p>"""),
],
"faq": [
("Hoeveel liter latex heb ik nodig voor een kamer?", "Reken muren plus plafond in m², keer twee lagen, gedeeld door 8 tot 11 m² per liter. Voor een woonkamer van 20 m² vloer is dat zo'n 12 tot 17 liter."),
("Wat kost latex laten aanbrengen?", "Muren €10 tot €16 per m², plafonds €12 tot €22 per m², inclusief verf en btw. Spuiten in een lege ruimte kan voordeliger zijn."),
],
},
"verf-op-waterbasis-of-terpentinebasis": {
"secties": [
("Wat kies je per onderdeel?",
"""<div class="tablewrap"><table>
<thead><tr><th>Onderdeel</th><th>Gangbare keuze</th><th>Waarom</th></tr></thead>
<tbody>
<tr><td>Binnendeuren en binnenkozijnen</td><td>Waterbasis</td><td>Vergeelt minder, ruikt weinig, droogt snel. Zie <a href="/kennisbank/binnendeuren-verven/">binnendeuren verven</a>.</td></tr>
<tr><td>Trap</td><td>Watergedragen traplak</td><td>Slijtvast en snel weer te belopen.</td></tr>
<tr><td>Buitenkozijnen</td><td>Beide</td><td>Terpentine vloeit mooi uit en is te verwerken bij lagere temperatuur; water droogt sneller.</td></tr>
<tr><td>Voordeur</td><td>Beide</td><td>Kies een buitenlak die tegen zon en slijtage kan. Zie <a href="/kennisbank/voordeur-schilderen/">voordeur schilderen</a>.</td></tr>
<tr><td>Schutting en gevelhout</td><td>Beits (water of alkyd)</td><td>Vochtregulerend. Zie <a href="/kennisbank/beits-of-verf/">beits of verf</a>.</td></tr>
</tbody></table></div>"""),
("Maakt het uit voor de prijs?",
"""<p>Voor de offerte van een schilder maakt de verfsoort weinig uit: de verf is maar een klein deel van de prijs. Het verschil zit in de werkwijze. Watergedragen lak droogt sneller, zodat een schilder binnen op één dag twee lagen kan zetten. Dat kan een werkdag schelen. Buiten in het najaar kan terpentineverf juist handiger zijn, omdat je bij lagere temperaturen kunt werken. Vraag de schilder welk systeem hij gebruikt en laat merk en product op de offerte zetten. Prijzen per onderdeel vind je bij <a href="/kosten/kozijnen-schilderen/">kozijnen schilderen</a> en <a href="/kosten/deuren-spuiten/">deuren spuiten</a>.</p>"""),
],
"faq": [
("Is watergedragen verf duurder?", "Per liter soms iets, maar voor de totale prijs van een schilder maakt het weinig uit. De verf is een klein deel van de offerte."),
("Welke verf voor binnendeuren: water of terpentine?", "Meestal waterbasis. Die vergeelt minder en droogt sneller, zodat je de deur eerder terug kunt hangen."),
],
},
}
