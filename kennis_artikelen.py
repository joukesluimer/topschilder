# -*- coding: utf-8 -*-
"""Inhoud van de kennisbank (/kennisbank/{slug}/). De opbouw staat in kennisbank.py.

Per artikel: titels, intro, kort antwoord, secties (h2 + html), stappenplan, kostenlinks,
FAQ en bronnen. Technische cijfers komen uit de genoemde technische bladen; controleer die
bij een update, want fabrikanten geven geregeld een nieuwe versie uit.
"""

# Bronnen die in meerdere artikelen terugkomen
TDS_PRIMER = ("Sikkens, technisch blad Rubbol Primer (grondverf op oplosmiddelbasis, 3 oktober 2025)",
              "https://msp.images.akzonobel.com/prd/dh/enlexp/documents/da/77/e9/23/sikkens_rubbol_primer.pdf")
TDS_BL_PRIMER = ("Sikkens, technisch blad Rubbol BL Primer (watergedragen grondverf, 2 september 2025)",
                 "https://msp.images.akzonobel.com/prd/dh/enlexp/documents/35/a1/16/f0/sikkens_rubbol_bl_primer.pdf")
TDS_MUURVERF = ("Sikkens, technisch blad Muren & Plafonds (watergedragen muurverf, 27 februari 2025)",
                "https://msp.images.akzonobel.com/prd/dh/enlexp/documents/aa/b6/56/15/sikkens_muren_en_plafonds_tds.pdf")
TDS_LATEX = ("Sigma, productblad Sigmatex Superlatex Matt (muurverf op basis van kunstharsdispersie)",
             "https://data.decoprof.nl/productblad/sigma-sigmatex-superlatex-matt.pdf")
VOS_RICHTLIJN = ("Europese richtlijn 2004/42/EG over vluchtige organische stoffen (VOS) in verf",
                 "https://eur-lex.europa.eu/legal-content/NL/ALL/?uri=CELEX:32004L0042")
BELASTINGDIENST = ("Belastingdienst, 9% btw voor werkzaamheden aan woningen",
                   "https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/tarieven_en_vrijstellingen/diensten_9_btw/werkzaamheden_aan_woningen/werkzaamheden_aan_woningen")
GGD_LOOD = ("GGD Zeeland, folder Lood in de leefomgeving",
            "https://ggdzeeland.nl/app/uploads/2024/12/Folder_lood_in_de_leefomgeving.pdf")
KASSA_HOUT = ("Kassa (BNNVARA), schimmel in hout en het vochtgehalte waarbij die groeit",
              "https://www.bnnvara.nl/kassa/artikelen/hoe-verwijder-je-schimmelplekken-uit-hout")
BW7 = ("Burgerlijk Wetboek Boek 7, titel 12: aanneming van werk",
       "https://wetten.overheid.nl/BWBR0005290/")
CONSUMENTENBOND = ("Consumentenbond, klacht over een dienstverlener",
                   "https://www.consumentenbond.nl/juridisch-advies/klacht-dienstverlener")


ARTIKELEN = [
# ---------------------------------------------------------------------------
{
"slug": "welke-verf-voor-kozijnen",
"groep": "Verf kiezen",
"titel": "Welke verf voor kozijnen? Hout, kunststof en binnen",
"seo_titel": "Welke verf voor kozijnen? Zo kies je de juiste",
"description": "Welke verf gebruik je voor houten, kunststof en binnenkozijnen? Grondverf, voorlak en aflak, hoogglans of zijdeglans, water- of terpentinebasis uitgelegd.",
"kort": "Grondverf, voorlak en aflak, glansgraad en kleur: wat past bij houten, kunststof en binnenkozijnen.",
"foto": "monumentale-voordeur-amsterdam",
"intro": "Kozijnen hebben het zwaarst van al het houtwerk aan je huis. Regen, zon en temperatuurwisselingen werken er het hele jaar op in. De verf die je kiest bepaalt dus niet alleen hoe ze eruitzien, maar ook hoe lang het hout droog en gezond blijft. Hier lees je welke verf bij welk kozijn past en waar een schilder op let.",
"kort_antwoord": "Houten buitenkozijnen krijgen een dekkend verfsysteem van grondverf, voorlak en aflak, op terpentine- of op waterbasis. Hoogglans of zijdeglans beschermt het best. Binnenkozijnen schilder je met watergedragen lak. Kunststof en aluminium kun je ook schilderen, maar alleen met een hechtprimer die voor die ondergrond geschikt is.",
"secties": [
("Houten buitenkozijnen: een compleet verfsysteem",
"""<p>Een schilder spreekt over een <strong>verfsysteem</strong>: een reeks lagen die op elkaar zijn afgestemd. Voor kaal of nieuw hout buiten is dat meestal:</p>
<ul>
<li><strong>Grondverf</strong> voor hechting op het hout en om de poriën te vullen.</li>
<li><strong>Voorlak</strong> (ook wel overgrondverf) om laagdikte op te bouwen en het oppervlak egaal te maken.</li>
<li><strong>Aflak</strong>, de laag die je ziet. Die zorgt voor de glans, de kleur en de bescherming tegen weer en vuil.</li>
</ul>
<p>Bij een gewone herschilderbeurt van een kozijn dat nog in goede staat is, hoeft niet alles opnieuw. De technische bladen van de fabrikanten beschrijven dan: alles reinigen en matteren, kale plekken plaatselijk gronden en voorlakken, en daarna het geheel aflakken. Wat het verschil is tussen grondverf en voorlak lees je in <a href="/kennisbank/grondverf-of-voorlak/">grondverf of voorlak</a>.</p>"""),
("Hoogglans of zijdeglans?",
"""<p>Hoe hoger de glans, hoe gladder en geslotener de verflaag. Vuil en water hechten minder aan een glanzend oppervlak, en dat is precies wat je buiten wilt. Daarom kiezen veel schilders voor hoogglans op ramen en deuren. Het nadeel: hoogglans laat elke oneffenheid in het hout zien. Zijdeglans is iets vergevingsgezinder en geeft een rustiger, moderner beeld. Bij oude, wat onrustige kozijnen is zijdeglans daarom vaak de mooiere keuze. Beide beschermen goed, zolang de laagdikte klopt.</p>"""),
("Lichte of donkere kleur?",
"""<p>Een donkere kleur wordt in de zon veel warmer dan wit of crème. Het hout zet daardoor meer uit en krimpt weer als het afkoelt, en hars of inhoudsstoffen kunnen eerder naar buiten komen. Donkere kozijnen op een zonnige zuid- of westgevel vragen daarom vaak eerder om onderhoud dan lichte. Dat is geen reden om het niet te doen, wel om de verf en het onderhoudsschema erop af te stemmen. Twijfel je over een kleur, kijk dan in de <a href="/kleuren-kiezen/">kleurenkiezer</a>.</p>"""),
("Terpentinebasis of waterbasis?",
"""<p>Voor buitenkozijnen bestaan goede systemen op beide basissen. Verf op terpentinebasis (alkyd) vloeit mooi uit en is te verwerken vanaf 5 °C. De watergedragen grondverf in hetzelfde assortiment heeft volgens het technische blad minimaal 8 °C nodig, maar is na ongeveer 6 uur overschilderbaar, tegen zo'n 18 uur voor de grondverf op terpentinebasis. Watergedragen verf bevat ook veel minder oplosmiddelen. Alle verschillen op een rij staan in <a href="/kennisbank/verf-op-waterbasis-of-terpentinebasis/">verf op waterbasis of terpentinebasis</a>.</p>"""),
("Kunststof en aluminium kozijnen",
"""<p>Kunststof kozijnen hoeven niet geschilderd te worden, maar het kan wel, bijvoorbeeld als de kleur verouderd is. Gewone lak hecht niet goed op hard pvc. Het technische blad van een watergedragen grondverf die er wel voor geschikt is, schrijft voor: reinigen, schuren, afnemen met een verdunning, en dan gronden. Aluminium vraagt ook om een speciale hechtprimer en wordt vaak gespoten. Laat dit doen door een schilder die er ervaring mee heeft, en vraag naar de garantie op de hechting.</p>"""),
("Binnenkozijnen",
"""<p>Binnen gebruik je watergedragen lak. Die ruikt nauwelijks, droogt snel en vergeelt niet, wat verf op terpentinebasis binnen op plekken met weinig licht wel kan doen. Voor deurkozijnen in een gang of hal is een slijtvaste zijdeglans praktisch: je kunt hem goed schoonmaken.</p>"""),
],
"stappen": [
("Inspecteer het kozijn", "Kijk naar loszittende verf, open naden en zachte plekken. Prik met een priem in de onderdorpel en de onderkant van de stijlen. Is het hout zacht, dan is er eerst houtrotherstel nodig."),
("Reinig en ontvet", "Was het kozijn met een ontvetter of sodaoplossing en spoel na met schoon water. Schuren zonder te reinigen wrijft vuil juist in het hout."),
("Verwijder loszittende verf en schuur", "Schraap losse verf weg, schuur de randen glad en mat de intacte verf op, zodat de nieuwe laag kan hechten."),
("Grond de kale plekken", "Kaal hout en reparaties krijgen grondverf. Let op de omstandigheden: volgens de technische bladen maximaal 85% luchtvochtigheid en een ondergrond van minstens 3 °C boven het dauwpunt."),
("Voorlakken", "Breng een voorlak aan op de gegronde plekken, of op het hele kozijn bij een grote kleurverandering. Licht matteren als hij droog is."),
("Aflakken", "Lak het geheel af, meestal in één of twee lagen. Kit de naden tussen kozijn en glaslat of muur pas als de verf droog is, met een overschilderbare kit."),
],
"kosten": ["kozijnen-schilderen", "dakkapel-schilderen"],
"faq": [
("Welke verf is het best voor houten buitenkozijnen?", "Een dekkend systeem van grondverf, voorlak en aflak uit hetzelfde merk, in hoogglans of zijdeglans. Of het op terpentine- of waterbasis is, maakt voor de bescherming weinig uit als het systeem goed wordt opgebouwd."),
("Kun je watergedragen verf over oude verf op terpentinebasis zetten?", "Ja, mits de oude laag intact is. De fabrikant schrijft voor om die eerst te reinigen en zeer goed te schuren, kale plekken bij te werken en dan met een geschikte watergedragen grondverf verder te gaan."),
("Hoe vaak moeten kozijnen geschilderd worden?", "Dat hangt af van de verf, de kleur en de ligging. Een zonnige of natte gevel en een donkere kleur vragen eerder onderhoud. Laat de kozijnen elk jaar nakijken en bijwerken waar de verf beschadigd is; dat rekt de tijd tot de volgende complete beurt."),
("Kun je kunststof kozijnen schilderen?", "Ja, met een hechtprimer die geschikt is voor hard pvc, na grondig reinigen en schuren. Gewone grondverf voor hout hecht niet goed op kunststof."),
("Hoogglans of zijdeglans voor kozijnen?", "Hoogglans sluit het best af en blijft het langst schoon, maar laat oneffenheden zien. Zijdeglans oogt rustiger en is mooier op oud, onregelmatig hout."),
],
"bronnen": [TDS_PRIMER, TDS_BL_PRIMER],
"gerelateerd": ["grondverf-of-voorlak", "kozijnen-schuren-en-voorbereiden", "houtrot-herkennen-en-herstellen"],
},
# ---------------------------------------------------------------------------
{
"slug": "grondverf-of-voorlak",
"groep": "Verf kiezen",
"titel": "Grondverf of voorlak: wat is het verschil?",
"seo_titel": "Grondverf of voorlak? Het verschil uitgelegd",
"description": "Grondverf zorgt voor hechting op kaal hout, voorlak bouwt de laag op voor de aflak. Wanneer je welke gebruikt, hoe lang je moet wachten en wat er misgaat zonder.",
"kort": "Wat grondverf, voorlak en aflak doen, wanneer je welke laag nodig hebt en hoe lang je moet wachten.",
"foto": "witte-grondverf-rollen-op-hout",
"intro": "In de bouwmarkt staan grondverf, voorlak, primer en aflak naast elkaar, en op de offerte van een schilder kom je ze ook tegen. Ze lijken op elkaar, maar ze doen elk iets anders. Wie een laag overslaat, merkt dat vaak pas na een paar jaar: de verf bladdert, of het hout schemert door.",
"kort_antwoord": "Grondverf breng je aan op kaal hout: hij hecht en vult de poriën. Voorlak komt daarna, of op oude verf die je opknapt: hij bouwt laagdikte op en maakt het oppervlak egaal, zodat de aflak mooi uitvloeit. De aflak is de beschermende toplaag. Op kaal hout heb je alle drie nodig; bij een opknapbeurt van intacte verf vaak alleen voorlak op de bijgewerkte plekken en daarna aflak.",
"secties": [
("Wat doet grondverf?",
"""<p>Grondverf is gemaakt om te hechten op een ondergrond die nog niets heeft: kaal hout, reparatieplekken met houtrotvuller, of soms kunststof en metaal. Hij dringt een stukje in het hout, vult de poriën en geeft de volgende laag iets om zich aan vast te houden. Een grondverf voor buiten op terpentinebasis heeft volgens het technische blad van de fabrikant een "uitstekende vulling" en is "uitstekend schuurbaar". Die schuurbaarheid is belangrijk: na het gronden schuur je de opstaande houtvezels weg, zodat het eindresultaat glad wordt.</p>
<p>Grondverf is geen eindlaag. Hij heeft een lage glans en is niet gemaakt om jarenlang weer en wind te verdragen. Dezelfde fabrikant schrijft dat zijn grondverf, in twee lagen, hooguit een jaar zonder aflak buiten kan staan.</p>"""),
("Wat doet voorlak?",
"""<p>Voorlak zit tussen grondverf en aflak in. Hij heeft meer vulkracht en dekking dan aflak en is makkelijk te schuren. Je gebruikt hem om:</p>
<ul>
<li>laagdikte op te bouwen, want een verfsysteem beschermt pas goed als het dik genoeg is;</li>
<li>kleine oneffenheden weg te werken, zodat de aflak strak oogt;</li>
<li>bij een grote kleurverandering de oude kleur af te dekken, met een voorlak in een tint die bij de aflak past;</li>
<li>bijgewerkte plekken op gelijke hoogte te brengen met de oude verf eromheen.</li>
</ul>
<p>Sommige grondverven zijn ook als voorlak te gebruiken. In het technische blad staat dan "gronden en overgronden". Bij bepaalde aflakken schrijft de fabrikant juist een aparte voorlak voor, of twee lagen aflak.</p>"""),
("Wanneer heb je welke laag nodig?",
"""<div class="tablewrap"><table>
<thead><tr><th>Situatie</th><th>Opbouw</th></tr></thead>
<tbody>
<tr><td>Nieuw of kaal hout</td><td>Grondverf, voorlak, aflak (eventueel twee lagen aflak)</td></tr>
<tr><td>Intacte verf, zelfde kleur</td><td>Reinigen, matteren, kale plekken gronden en voorlakken, geheel aflakken</td></tr>
<tr><td>Intacte verf, andere kleur</td><td>Reinigen, matteren, kale plekken gronden, geheel voorlakken in passende tint, aflakken</td></tr>
<tr><td>Reparatie met houtrotvuller</td><td>Vuller schuren, gronden, voorlakken, aflakken</td></tr>
<tr><td>Hout dat doorbloedt (bijvoorbeeld eiken, meranti, kwasten in grenen)</td><td>Eerst een isolerende grondverf, dan het normale systeem</td></tr>
</tbody></table></div>
<p>Die laatste regel komt uit het technische blad van een watergedragen grondverf. Daarin staat dat bij houtsoorten als eiken, Dark Red Meranti en Western Red Cedar inhoudsstoffen door de verf heen kunnen komen, en dat kwasten en noesten in grenen en vuren geel kunnen verkleuren. Een isolerende primer voorkomt dat.</p>"""),
("Hoe lang moet je wachten tussen de lagen?",
"""<p>Dat verschilt per product en per temperatuur. Twee voorbeelden uit technische bladen:</p>
<ul>
<li>Een grondverf op terpentinebasis is bij 23 °C na ongeveer 18 uur overschilderbaar, bij 10 °C na ongeveer 20 uur.</li>
<li>Een watergedragen grondverf is bij 20 °C na ongeveer 6 uur overschilderbaar. Daarmee kun je op één dag meerdere lagen zetten.</li>
</ul>
<p>Koud of vochtig weer rekt de droogtijd. Schilder je buiten in het voor- of najaar, kijk dan ook naar de nachttemperatuur en het dauwpunt. Daarover gaat de gids <a href="/gids/wanneer-buiten-schilderen/">wanneer kun je buiten schilderen</a>.</p>"""),
("Wat gaat er mis als je een laag overslaat?",
"""<p>Aflak direct op kaal hout hecht minder goed en vult de poriën niet. Het hout zuigt de verf ongelijk op, waardoor je vlekken krijgt en de laag op sommige plekken te dun blijft. Water komt er dan sneller achter, en dat is het begin van bladderende verf en uiteindelijk <a href="/kennisbank/houtrot-herkennen-en-herstellen/">houtrot</a>. Een voorlak overslaan op een opgeknapt kozijn levert vooral een minder strak resultaat op: je ziet de randen van de bijgewerkte plekken door de aflak heen.</p>"""),
],
"stappen": [
("Bepaal wat je ondergrond is", "Kaal hout, intacte oude verf, of een mix? Dat bepaalt of je overal moet gronden of alleen plaatselijk."),
("Reinig en schuur", "Ontvet het werk en schuur het op. Bij kaal hout schuur je de vezels glad; bij oude verf mat je het oppervlak."),
("Grond", "Breng grondverf aan op alle kale plekken en reparaties. Werk niet bij meer dan 85% luchtvochtigheid."),
("Licht schuren", "Als de grondverf droog is, schuur je de opgestane houtvezels weg en maak je het werk stofvrij."),
("Voorlak", "Zet een voorlak, op de bijgewerkte plekken of op het geheel. Laat hem drogen en mat hem licht op."),
("Aflak", "Breng de aflak aan in een gelijkmatige laag. Bij twee lagen aflak tussendoor licht matteren."),
],
"kosten": ["kozijnen-schilderen", "deuren-spuiten"],
"faq": [
("Is primer hetzelfde als grondverf?", "Meestal wel. Primer is de Engelse naam en wordt vaak gebruikt voor grondverven die op meerdere ondergronden hechten, zoals hout, kunststof en metaal."),
("Kan ik grondverf als eindlaag laten staan?", "Nee. Grondverf is niet gemaakt als toplaag. Een fabrikant geeft aan dat zijn grondverf in twee lagen hooguit een jaar zonder aflak buiten kan staan."),
("Moet ik altijd voorlakken?", "Op kaal hout en bij een grote kleurverandering wel. Bij een opknapbeurt van intacte verf in dezelfde kleur kun je vaak volstaan met voorlak op de bijgewerkte plekken."),
("Mag grondverf op terpentinebasis onder watergedragen aflak?", "Combineer bij voorkeur producten die de fabrikant als systeem voorschrijft. In het technische blad staat met welke aflakken een grondverf overschilderbaar is."),
("Waarom moet ik schuren na het gronden?", "Grondverf laat de houtvezels opstaan. Door licht te schuren wordt het oppervlak weer glad en hecht de volgende laag beter."),
],
"bronnen": [TDS_PRIMER, TDS_BL_PRIMER],
"gerelateerd": ["welke-verf-voor-kozijnen", "verf-op-waterbasis-of-terpentinebasis", "kozijnen-schuren-en-voorbereiden"],
},
# ---------------------------------------------------------------------------
{
"slug": "houtrot-herkennen-en-herstellen",
"groep": "Schade en onderhoud",
"titel": "Houtrot herkennen en herstellen: zo pak je het aan",
"seo_titel": "Houtrot herkennen en herstellen: stap voor stap",
"description": "Hoe herken je houtrot in kozijnen en deuren, wat is de oorzaak en wanneer volstaat houtrotvuller of is een inzetstuk nodig? Met stappenplan en richtprijzen.",
"kort": "De signalen van houtrot, waar je moet kijken, en wanneer vuller, een inzetstuk of vervangen nodig is.",
"foto": "bruinrot-blokbreuk-hout-close-up",
"intro": "Houtrot begint onzichtbaar. Water komt achter de verf, het hout blijft vochtig en schimmels gaan aan het werk. Als je het ziet, is het vaak al een tijd bezig. Hoe eerder je het vindt, hoe kleiner en goedkoper de reparatie. Hier lees je waar je moet kijken, hoe je het herkent en hoe een schilder het herstelt.",
"kort_antwoord": "Houtrot herken je aan zacht hout dat meegeeft als je erin prikt, bladderende verf, donkere verkleuring en scheurtjes dwars op de nerf. Kleine plekken worden uitgekapt en gevuld met een tweecomponenten houtrotvuller. Is de aantasting dieper of groter, dan zet de schilder er een stuk nieuw hout in. Een kozijn dat grotendeels rot is, moet worden vervangen.",
"secties": [
("Hoe ontstaat houtrot?",
"""<p>Hout gaat rotten als het lange tijd te vochtig blijft. Dan kunnen schimmels het hout afbreken. Als grens wordt een vochtgehalte van ongeveer 20 tot 22 procent genoemd: daaronder groeit de schimmel niet of nauwelijks. Droog hout rot dus niet. Het probleem ontstaat bijna altijd waar water blijft staan of naar binnen trekt:</p>
<ul>
<li>door een beschadigde of te dunne verflaag;</li>
<li>via open naden en verbindingen, bijvoorbeeld in de hoeken van een kozijn;</li>
<li>langs kit die is losgekomen bij de glaslatten of de aansluiting op de muur;</li>
<li>op plekken waar water niet wegloopt, zoals een onderdorpel zonder goede afwatering.</li>
</ul>"""),
("Waar moet je kijken?",
"""<p>Begin altijd onderaan. Water loopt naar beneden en blijft liggen op horizontale delen. De bekende probleemplekken zijn:</p>
<ul class="checklist">
<li>de onderdorpel van ramen en deuren;</li>
<li>de onderkant van de stijlen, waar ze op de dorpel aansluiten;</li>
<li>de hoekverbindingen van de raamvleugels;</li>
<li>de glaslatten, vooral de onderste;</li>
<li>de onderkant van voordeuren en de deurdorpel;</li>
<li>houtwerk op een dakkapel en boeidelen.</li>
</ul>"""),
("Zo herken je houtrot",
"""<p>De verf vertelt vaak als eerste dat er iets mis is. Bladdert hij plaatselijk, zitten er blazen in of zie je donkere vlekken onder de verf, dan is het hout erachter waarschijnlijk vochtig. Daarna volgen de echte signalen van rot:</p>
<ul>
<li><strong>Zacht hout.</strong> Prik met een priem of kleine schroevendraaier. Gezond hout geeft weinig mee; rot hout is zacht en de punt zakt erin.</li>
<li><strong>Scheuren dwars op de nerf.</strong> Bij bruinrot breekt het hout in kleine blokjes, zoals op de foto bovenaan.</li>
<li><strong>Verkleuring.</strong> Donker of juist verbleekt, vezelig hout.</li>
<li><strong>Een muffe lucht</strong> of schimmeldraden in naden.</li>
</ul>
<p>Twijfel je, laat dan een schilder kijken. Die ziet ook of er alleen een plek rot is of dat het vocht dieper zit. Met de <a href="/onderhoudscheck/">onderhoudscheck</a> zie je per onderdeel waar je op kunt letten.</p>"""),
("Drie manieren van herstel",
"""<p><strong>1. Uitkappen en vullen.</strong> Bij kleine, ondiepe plekken haalt de schilder het rotte hout weg tot hij op gezond, droog hout zit. Het gat wordt gevuld met een tweecomponenten houtrotvuller, die na uitharden geschuurd en geschilderd wordt. Dit is de snelste en goedkoopste oplossing.</p>
<p><strong>2. Een inzetstuk.</strong> Is de aantasting groter of dieper, dan zaagt de schilder het slechte deel eruit en lijmt er een passend stuk nieuw hout in. Dat is sterker en duurzamer dan een grote plek vuller. Let op de btw: het vervangen van hout valt onder 21%, het schilderwerk eromheen onder 9% (zie <a href="/gids/btw-schilderwerk/">btw op schilderwerk</a>).</p>
<p><strong>3. Vervangen.</strong> Is een onderdorpel of een kozijn grotendeels rot, of zit het in de constructie, dan is vervangen vaak goedkoper dan blijven repareren. Dat is werk voor een timmerman of kozijnenleverancier; de schilder werkt het daarna af.</p>"""),
("Houtrot of huiszwam?",
"""<p>Houtrot in kozijnen is iets anders dan huiszwam, een schimmel die binnen in vochtige, slecht geventileerde ruimtes zoals kruipruimtes kan groeien en zich over metselwerk verspreidt. Zie je wit, watten- of vliesachtig schimmelweefsel onder een vloer of achter een betimmering, schakel dan een specialist in. Dat valt buiten gewoon schilderwerk.</p>"""),
("Voorkomen is goedkoper",
"""<p>De meeste houtrot ontstaat door uitgesteld onderhoud. Een verflaag die op tijd wordt bijgewerkt, houdt het water buiten. Loop daarom elk voorjaar je kozijnen na, werk beschadigingen en losse kit direct bij, en laat het buitenschilderwerk doen voordat de verf op grote schaal bladdert.</p>"""),
],
"stappen": [
("Spoor de plekken op", "Prik systematisch in onderdorpels, stijlen, hoeken en glaslatten en markeer elke zachte plek."),
("Kap het rotte hout weg", "Verwijder al het aangetaste hout tot je op gezond, hard hout zit. Halve maatregelen komen terug."),
("Laat het hout drogen", "Vuller hecht niet goed op nat hout. Werk bij droog weer, en geef een natte plek de tijd om op te drogen."),
("Behandel en vul", "Breng zo nodig een verzadiger aan en vul met tweecomponenten houtrotvuller, iets boven het oppervlak uit. Bij grote schade een inzetstuk van nieuw hout."),
("Schuur en schilder", "Schuur de reparatie strak, grond hem, voorlak en lak af in hetzelfde systeem als de rest van het kozijn."),
("Sluit de naden", "Kit naden en aansluitingen met een overschilderbare kit, zodat het water er niet opnieuw in kan."),
],
"kosten": ["kozijnen-schilderen", "huis-schilderen"],
"dienst": "houtrot-reparatie",
"faq": [
("Kun je houtrot zelf repareren?", "Kleine plekken wel, met houtrotvuller en het goede gereedschap. Bij grote of diepe aantasting, of als de onderdorpel is aangetast, is een inzetstuk door een vakman duurzamer."),
("Hoe lang gaat een houtrotreparatie mee?", "Een goed uitgevoerde reparatie gaat lang mee, mits al het rotte hout is verwijderd, het hout droog was en de verflaag daarna wordt onderhouden."),
("Wat kost houtrot laten repareren?", "Dat hangt af van het aantal en de grootte van de plekken. Een schilder rekent meestal per reparatieplek of per inzetstuk. De richtprijzen staan hieronder."),
("Valt houtrotherstel onder 9% btw?", "Het vullen en schilderen valt onder 9% bij een woning ouder dan twee jaar. Inzetstukken van nieuw hout en het vervangen van onderdelen vallen onder 21%."),
("Komt houtrot terug na een reparatie?", "Alleen als de oorzaak blijft: water dat binnenkomt via een kapotte verflaag, open naden of slechte kit. Herstel dus ook de oorzaak."),
],
"bronnen": [KASSA_HOUT, BELASTINGDIENST],
"gerelateerd": ["kozijnen-schuren-en-voorbereiden", "verfschade-en-garantie", "welke-verf-voor-kozijnen"],
},
# ---------------------------------------------------------------------------
{
"slug": "plafond-schilderen-zonder-strepen",
"groep": "Voorbereiden en uitvoeren",
"titel": "Plafond schilderen zonder strepen: zo lukt het",
"seo_titel": "Plafond schilderen zonder strepen: zo doe je het",
"description": "Strepen en randen op je plafond voorkomen? Nat-in-nat werken, de goede roller, de juiste richting en een voorstrijk. Met stappenplan en richtprijzen.",
"kort": "Waarom je strepen ziet, hoe je nat-in-nat werkt en welke roller en verf je nodig hebt.",
"foto": "verfroller-close-up-in-verfbak",
"intro": "Een plafond schilderen lijkt simpel: een grote witte vlakte en een roller. Toch is het de klus waarbij de meeste mensen strepen en randen overhouden, die je pas ziet als het licht er schuin over valt. Dat komt bijna altijd door de manier van werken, niet door de verf. Met deze aanpak krijg je een egaal plafond.",
"kort_antwoord": "Strepen ontstaan als je nieuwe verf tegen een rand zet die al aan het drogen is. Werk daarom nat-in-nat in banen, met genoeg verf op een goede vachtroller, en rol het laatst in de richting van het raam. Zorg voor een gelijkmatig zuigende ondergrond met een voorstrijk, schilder niet in de zon of tocht, en stop nooit halverwege het plafond.",
"secties": [
("Waar komen strepen vandaan?",
"""<p>Bijna alle strepen hebben een van deze oorzaken:</p>
<ul>
<li><strong>Aanzetten op droge verf.</strong> Rol je een nieuwe baan tegen een baan die al begint te drogen, dan krijgt die rand twee lagen. Dat zie je als een streep.</li>
<li><strong>Te weinig verf.</strong> Een droge roller laat een dunne, ongelijke laag achter.</li>
<li><strong>Een zuigende ondergrond.</strong> Kaal stucwerk of gipsplaat zuigt de verf plaatselijk op, waardoor de ene plek matter wordt dan de andere.</li>
<li><strong>Te snel drogen.</strong> Warmte, zon of tocht laat de verf zo snel aandrogen dat je niet meer nat-in-nat kunt werken.</li>
<li><strong>Verkeerde richting.</strong> Het licht van het raam laat elke rolbaan zien die er dwars op ligt.</li>
</ul>"""),
("De juiste verf en het juiste gereedschap",
"""<p>Kies een matte muurverf die geschikt is voor plafonds. Mat verbergt oneffenheden; hoe meer glans, hoe meer je ziet. Een fabrikant raadt in zijn technische blad voor muur- en plafondverf een <strong>vachtroller</strong> aan, en een acrylkwast of blokwitter voor de randen. Neem een roller van 25 centimeter breed met een steel, zodat je zonder trap kunt werken en gelijkmatig druk zet. Gebruik een verfbak met rooster om overtollige verf af te rollen.</p>
<p>Let ook op de temperatuur: dezelfde verf mag volgens het technische blad niet worden verwerkt onder 10 °C of boven 30 °C. Bij 20 °C is hij na ongeveer 5 uur overschilderbaar, bij 10 °C pas na 12 uur.</p>"""),
("De ondergrond voorbereiden",
"""<p>Een egaal resultaat begint met een egale ondergrond. Volgens hetzelfde technische blad:</p>
<ul>
<li>reinig het plafond, bijvoorbeeld met een verfreiniger;</li>
<li>behandel zuigende en poederende ondergronden, zoals spuitpleister, eerst met een voorstrijk;</li>
<li>isoleer vochtkringen en nicotinevlekken, anders komen ze door de nieuwe verf heen;</li>
<li>verwijder veegvaste sauslaag (witkalk) en slecht hechtende verf, want daarop hecht muurverf niet.</li>
</ul>
<p>Twijfel je of er een sauslaag op je plafond zit? Veeg er met een vochtige doek over. Geeft het wit af, dan is het saus. Meer daarover in <a href="/kennisbank/latex-of-muurverf/">latex of muurverf</a>.</p>"""),
("Nat-in-nat werken: zo doe je het",
"""<p>Het geheim is dat je steeds aansluit op verf die nog nat is. Werk daarom in banen van ongeveer een meter breed, van het raam af naar achteren. Zet in elke baan vakken van ongeveer een vierkante meter op: verf aanbrengen, kruislings verdelen en dan zonder nieuwe verf in één richting narollen, naar het raam toe. Begin het volgende vak tegen de natte rand aan. Ben je aan het eind van een baan, begin dan meteen aan de volgende, zodat de lange rand nog nat is.</p>
<p>Schilder eerst de randen langs de muren met een kwast, maar niet het hele plafond tegelijk: doe de rand per baan vlak voor je hem rolt, dan droogt hij niet aan voordat je er met de roller overheen gaat.</p>"""),
("Twee lagen, en nooit halverwege stoppen",
"""<p>Op een plafond dat van kleur verandert of dat al lang niet geschilderd is, heb je meestal twee lagen nodig. Laat de eerste goed drogen. Stop tijdens een laag nooit midden in het plafond om koffie te drinken: die rand zie je altijd terug. Doe ramen en deuren dicht tijdens het schilderen tegen tocht, en zet daarna pas de ramen open om te ventileren.</p>
<p>Is het een groot of hoog plafond, of zie je erg op tegen strepen, dan kan <a href="/kosten/latex-spuiten/">latex spuiten</a> een alternatief zijn. Een gespoten plafond heeft geen rolbanen, maar de ondergrond moet dan wel goed zijn, want oneffenheden vallen juist meer op.</p>"""),
],
"stappen": [
("Maak de ruimte leeg en dek af", "Haal meubels weg of zet ze in het midden onder folie, en dek de vloer af met stucloper."),
("Reinig en repareer", "Maak het plafond stofvrij, vul gaten en scheuren en schuur ze glad als ze droog zijn."),
("Voorstrijk waar nodig", "Behandel kaal stucwerk, gipsplaat en reparatieplekken met een voorstrijk, zodat het plafond overal even sterk zuigt."),
("Plak de randen af", "Plak de bovenrand van de muren af als je die niet meeschildert, en haal lampen en afdekkapjes weg."),
("Rol nat-in-nat in banen", "Werk in banen van ongeveer een meter breed, verdeel kruislings en rol het laatst in de richting van het raam."),
("Controleer en zet de tweede laag", "Bekijk het plafond met strijklicht van een lamp. Laat drogen volgens de tijd op het blik en zet de tweede laag op dezelfde manier."),
],
"kosten": ["plafond-schilderen", "latex-spuiten"],
"faq": [
("Waarom zie ik strepen op mijn plafond nadat het droog is?", "Meestal omdat er tegen al aandrogende verf is aangezet, waardoor die randen dubbel zijn. Ook een ongelijk zuigende ondergrond of te weinig verf op de roller geeft strepen."),
("Welke kant op moet je een plafond rollen?", "Verdeel kruislings en rol de laatste keer in één richting, naar het raam toe. Dan valt het licht in de lengte van de rolbanen en zie je ze het minst."),
("Hoeveel lagen heeft een plafond nodig?", "Bij een opfrisbeurt in dezelfde kleur soms één, meestal twee. Op kaal stucwerk eerst een voorstrijk en daarna twee lagen."),
("Kun je strepen wegwerken?", "Ja, met een extra laag die je zorgvuldig nat-in-nat aanbrengt. Bijwerken met een kwastje op losse plekken maakt het meestal erger."),
("Hoeveel verf heb ik nodig voor mijn plafond?", "Een matte muurverf dekt ongeveer 8 tot 11 m² per liter per laag, afhankelijk van de ondergrond. Reken het uit met onze gids over verf berekenen."),
],
"bronnen": [TDS_MUURVERF],
"extra_links": [("/gids/verf-berekenen/", "Hoeveel verf heb je nodig?")],
"gerelateerd": ["latex-of-muurverf", "behang-verwijderen", "verf-op-waterbasis-of-terpentinebasis"],
},
# ---------------------------------------------------------------------------
{
"slug": "latex-of-muurverf",
"groep": "Verf kiezen",
"titel": "Latex of muurverf: wat is het verschil?",
"seo_titel": "Latex of muurverf? Het verschil en wat je kiest",
"description": "Is latex hetzelfde als muurverf? Wat het verschil is met saus en kalkverf, welke glans je kiest en welke verf in keuken, badkamer en woonkamer hoort.",
"kort": "Waarom latex en muurverf vaak hetzelfde zijn, het verschil met saus en welke verf je per ruimte kiest.",
"foto": "muur-verven-met-roller-zwartwit",
"intro": "In de winkel staat latex, muurverf, binnenmuurverf en soms nog saus. Veel mensen denken dat latex een betere of duurdere soort is. In werkelijkheid gaat het meestal om hetzelfde soort verf onder een andere naam. Waar je wel op moet letten, zijn de glans, de reinigbaarheid en de ondergrond.",
"kort_antwoord": "Latex is in Nederland vooral een gangbare naam voor muurverf op basis van kunsthars, opgelost in water. Het verschil zit dus niet in de naam maar in de eigenschappen: mat of zijdeglans, hoe goed je hem kunt afnemen en of hij geschikt is voor vochtige ruimtes. Saus of witkalk is wel iets anders: die geeft af als je eroverheen veegt en moet weg voordat je gaat schilderen.",
"secties": [
("Waar komt de naam latex vandaan?",
"""<p>Vroeger werd een deel van de muurverven gemaakt met latex, een rubberachtig bindmiddel. Die naam is blijven hangen. Tegenwoordig is vrijwel alle muurverf voor binnen een watergedragen dispersieverf op basis van kunsthars, zoals acrylaat. Fabrikanten beschrijven hun "latex" ook gewoon zo: het productblad van een bekende latex noemt hem een muurverf "op basis van kunstharsdispersie". Of er latex of muurverf op het blik staat, zegt dus weinig over de kwaliteit.</p>"""),
("Saus en kalkverf: wel een verschil",
"""<p>Saus, ook wel witkalk genoemd, is een goedkope, poederige verf die vroeger veel op plafonds werd gebruikt. Hij hecht slecht en geeft af als je eroverheen veegt. Kalkverf, die je tegenwoordig weer ziet voor een wolkerig effect, is ook een aparte soort met eigen verwerkingsregels.</p>
<p>Gewone muurverf hecht niet op een sauslaag. In het technische blad van een muurverf staat dan ook dat veegvaste muurverf, witkalk of saus, en slecht hechtende verflagen eerst verwijderd moeten worden. Test het met een vochtige doek: geeft de muur of het plafond wit af, dan zit er saus op.</p>"""),
("Mat, zijdemat of zijdeglans?",
"""<div class="tablewrap"><table>
<thead><tr><th>Glans</th><th>Eigenschappen</th><th>Geschikt voor</th></tr></thead>
<tbody>
<tr><td>Mat</td><td>Verbergt oneffenheden, rustig beeld, minder goed af te nemen</td><td>Plafonds, woonkamer, slaapkamer</td></tr>
<tr><td>Zijdemat</td><td>Iets meer glans, beter afwasbaar, nog steeds rustig</td><td>Gang, trapgat, kinderkamer</td></tr>
<tr><td>Zijdeglans</td><td>Goed afwasbaar en slijtvast, laat oneffenheden meer zien</td><td>Keuken, plekken die vaak vies worden</td></tr>
</tbody></table></div>
<p>Hoe goed een verf tegen schoonmaken kan, staat vaak op het blik als <em>natte schrobvastheid</em> volgens de Europese norm EN 13300, in klasse 1 (zeer goed) tot 5. Voor een gang of keuken kies je klasse 1 of 2. Ook een matte verf kan goed scoren: het productblad van een bekende matte latex noemt schrobklasse 1. Wel waarschuwt dezelfde fabrikant dat matte verf binnen handbereik glimmende plekken kan krijgen als je er vaak aankomt of hem schoonmaakt.</p>"""),
("Welke verf per ruimte?",
"""<ul>
<li><strong>Woonkamer en slaapkamer:</strong> een matte, goed dekkende muurverf.</li>
<li><strong>Plafond:</strong> mat, want strijklicht laat bij meer glans elke oneffenheid zien. Lees ook <a href="/kennisbank/plafond-schilderen-zonder-strepen/">plafond schilderen zonder strepen</a>.</li>
<li><strong>Keuken en gang:</strong> een reinigbare muurverf, zijdemat of zijdeglans.</li>
<li><strong>Badkamer en toilet:</strong> een muurverf die geschikt is voor vochtige ruimtes, eventueel met een middel tegen schimmel. Het productblad van een matte latex noemt badkamer en keuken geschikt, behalve het douchegedeelte. Ventileren blijft nodig.</li>
<li><strong>Op oude lakverf:</strong> zet geen dampdoorlatende muurverf direct op een gesloten laag zoals alkydverf; volgens hetzelfde productblad kan dat bij vocht tot loslaten leiden.</li>
<li><strong>Nieuw stucwerk of gipsplaat:</strong> eerst een voorstrijk, anders zuigt de wand de verf ongelijk op.</li>
</ul>"""),
("Latex spuiten of rollen?",
"""<p>Bij nieuwbouw of een leeg huis laten veel mensen de muren en plafonds spuiten. Dat heet latex spuiten. Het gaat snel bij grote vlakken en geeft een egaal resultaat zonder rolbanen. Het afdekken kost wel veel tijd, en de ruimte moet leeg zijn. Wat het kost en wanneer het goedkoper is dan rollen, lees je op <a href="/kosten/latex-spuiten/">wat kost latex spuiten</a>.</p>"""),
],
"stappen": [
("Test de ondergrond", "Veeg met een vochtige doek over de muur. Geeft hij wit af, dan zit er saus op die eerst weg moet."),
("Kies de glans per ruimte", "Mat voor woonruimtes en plafonds, reinigbaar voor keuken en gang, geschikt voor vocht in de badkamer."),
("Bereid de wand voor", "Vul gaten, schuur ze glad, reinig de wand en zet een voorstrijk op kaal of zuigend stucwerk."),
("Plak af en dek af", "Plak plinten, kozijnen en stopcontacten af en dek de vloer af."),
("Schilder in twee lagen", "Zet eerst de randen met een kwast en rol daarna nat-in-nat. Laat de eerste laag drogen volgens het blik."),
],
"kosten": ["schilderen-per-m2", "latex-spuiten"],
"faq": [
("Is latex beter dan muurverf?", "Niet per se. Latex is meestal gewoon een naam voor muurverf op basis van kunsthars. Kijk naar dekkracht, glans en reinigbaarheid op het blik."),
("Kun je latex over saus schilderen?", "Nee. Muurverf hecht niet op een veegvaste sauslaag. Die moet eerst worden verwijderd, of in sommige gevallen worden vastgezet met een speciale fixeer."),
("Welke muurverf is afwasbaar?", "Verf met een goede natte schrobvastheid volgens EN 13300, klasse 1 of 2. Hoe hoger de glans, hoe makkelijker meestal schoon te maken."),
("Kun je muurverf op een plafond gebruiken?", "Ja. De meeste muurverven zijn geschikt voor muren en plafonds. Kies voor plafonds een matte variant."),
("Wat is het verschil tussen latex en acrylverf?", "In de praktijk weinig: beide zijn watergedragen verven op basis van kunsthars. Acryl verwijst naar het type kunsthars dat erin zit."),
],
"bronnen": [TDS_LATEX, TDS_MUURVERF],
"gerelateerd": ["plafond-schilderen-zonder-strepen", "behang-verwijderen", "verf-op-waterbasis-of-terpentinebasis"],
},
# ---------------------------------------------------------------------------
{
"slug": "verf-op-waterbasis-of-terpentinebasis",
"groep": "Verf kiezen",
"titel": "Verf op waterbasis of terpentinebasis: wat kies je?",
"seo_titel": "Verf op waterbasis of terpentinebasis? Het verschil",
"description": "Watergedragen verf of verf op terpentinebasis (alkyd)? Droogtijd, glans, vergelen, gezondheid en wanneer je welke kiest, binnen en buiten, met bronnen.",
"kort": "Droogtijd, glans, vergelen en gezondheid: het verschil tussen watergedragen verf en alkyd.",
"foto": "kwasten-van-natuurhaar",
"intro": "Lakverf voor hout en metaal heb je in twee hoofdsoorten: watergedragen, vaak herkenbaar aan BL of aqua op het blik, en verf op terpentinebasis, ook wel alkyd of oplosmiddelhoudend genoemd. Schilders hebben er vaak een uitgesproken mening over. Beide hebben echte voor- en nadelen, en welke het best past hangt af van waar je hem gebruikt.",
"kort_antwoord": "Binnen kies je watergedragen verf: hij ruikt nauwelijks, droogt snel en vergeelt niet. Buiten kunnen beide goed werken. Verf op terpentinebasis vloeit mooier uit en is bij lagere temperaturen te verwerken; watergedragen verf droogt sneller, blijft langer kleurvast en bevat veel minder oplosmiddelen. Het belangrijkste is dat je één systeem van dezelfde fabrikant gebruikt.",
"secties": [
("Wat is het verschil?",
"""<p>Alle verf bestaat uit een bindmiddel, pigment en een middel dat de verf vloeibaar houdt tot hij droog is. Bij verf op terpentinebasis is dat een oplosmiddel; bij watergedragen verf is het grotendeels water. Dat verschil bepaalt hoe de verf droogt, ruikt en zich gedraagt.</p>
<div class="tablewrap"><table>
<thead><tr><th></th><th>Watergedragen</th><th>Terpentinebasis (alkyd)</th></tr></thead>
<tbody>
<tr><td>Droogtijd (voorbeeld grondverf)</td><td>Overschilderbaar na ca. 6 uur bij 20 °C</td><td>Overschilderbaar na ca. 18 uur bij 23 °C</td></tr>
<tr><td>Minimale verwerkingstemperatuur (zelfde voorbeeld)</td><td>8 °C</td><td>5 °C</td></tr>
<tr><td>Oplosmiddelen (VOS)</td><td>Laag; voorbeeld: 90 g/l</td><td>Hoger; voorbeeld: tot 300 g/l</td></tr>
<tr><td>Geur</td><td>Nauwelijks</td><td>Duidelijk, ook tijdens het drogen</td></tr>
<tr><td>Uitvloeiing</td><td>Goed, minder dan alkyd</td><td>Zeer goed, strak resultaat</td></tr>
<tr><td>Vergelen binnen</td><td>Nee</td><td>Kan vergelen, vooral op donkere plekken</td></tr>
<tr><td>Kwasten reinigen</td><td>Met water</td><td>Met terpentine</td></tr>
</tbody></table></div>
<p><small>De voorbeelden komen uit de technische bladen van een grondverf op terpentinebasis en een watergedragen grondverf uit hetzelfde assortiment. Andere producten wijken af; kijk altijd op het blik of het technische blad.</small></p>"""),
("Gezondheid en regels",
"""<p>Verf op terpentinebasis bevat meer vluchtige organische stoffen (VOS). Die komen vrij tijdens het schilderen en drogen. Daarom gelden er in de hele Europese Unie maximale gehaltes per soort verf, vastgelegd in richtlijn 2004/42/EG. In het technische blad van een watergedragen grondverf staat bijvoorbeeld een wettelijke grens van 130 gram per liter, en een gemeten gehalte van 90 gram per liter. Voor de grondverf op terpentinebasis noemt de fabrikant een grens van 300 gram per liter.</p>
<p>Binnen werken schilders daarom vrijwel altijd met watergedragen verf. Schilder je zelf met verf op terpentinebasis, zorg dan voor goede ventilatie en kijk op het etiket welke bescherming nodig is.</p>"""),
("Buiten: wat werkt beter?",
"""<p>Buiten is de keuze minder duidelijk. Verf op terpentinebasis is de traditionele keuze voor kozijnen en deuren: hij vloeit mooi uit tot een strakke hoogglans en is bij koeler weer te verwerken. Watergedragen buitenverf is de afgelopen jaren sterk verbeterd. Hij blijft elastisch, behoudt zijn kleur en glans lang en droogt snel, zodat een schilder meer lagen op een dag kan zetten.</p>
<p>Een praktisch nadeel van watergedragen verf staat in het technische blad: hij kan worden aangetast door weekmakers in tochtprofielen van pvc-rubber. De verf wordt daar zacht en kleverig. De fabrikant raadt profielen van EPDM- of siliconenrubber aan.</p>"""),
("Kun je ze combineren?",
"""<p>Ja, met de juiste voorbereiding. Wil je watergedragen verf op een oude laag op terpentinebasis zetten, dan schrijft de fabrikant voor: de verf afwassen met een reiniger, zeer goed schuren, kale plekken bijwerken en dan overschilderen met een watergedragen grondverf die daarvoor geschikt is. Andersom kan ook vaak, maar kijk in het technische blad met welke lagen een product overschilderbaar is. Mix nooit verf van verschillende soorten in één pot.</p>"""),
("Restjes en kwasten",
"""<p>Spoel verf nooit door de gootsteen, ook watergedragen verf niet. Dat staat op elk technisch blad. Laat kwasten uitlekken op een krant, laat restjes indrogen en lever verf op terpentinebasis, terpentine en kwasten in bij het klein chemisch afval van je gemeente.</p>"""),
],
"stappen": [
("Bepaal waar je schildert", "Binnen: watergedragen. Buiten: beide mogelijk; kies op basis van temperatuur, gewenste glans en wat er al op zit."),
("Kijk wat er op het werk zit", "Test oude verf met een doekje met spiritus: verf op waterbasis wordt zacht, alkyd meestal niet. Twijfel je, behandel het dan als alkyd."),
("Kies één systeem", "Gebruik grondverf, voorlak en aflak van dezelfde fabrikant die als systeem bij elkaar horen."),
("Bereid voor volgens het blad", "Reinigen en schuren zijn bij beide soorten nodig; bij watergedragen verf op alkyd extra goed schuren."),
("Let op de omstandigheden", "Controleer de minimumtemperatuur en luchtvochtigheid op het blik en houd rekening met de droogtijd."),
],
"kosten": ["kozijnen-schilderen", "deuren-spuiten", "schilder-uurtarief"],
"faq": [
("Is watergedragen verf net zo goed als verf op terpentinebasis?", "Voor binnen is watergedragen verf de betere keuze. Buiten zijn er goede systemen van beide soorten; het verschil zit meer in verwerking en uiterlijk dan in de bescherming."),
("Waarom vergeelt witte lak binnen?", "Verf op terpentinebasis kan vergelen, vooral op plekken met weinig daglicht. Watergedragen lak heeft daar geen last van."),
("Kan ik terpentine gebruiken om watergedragen verf te verdunnen?", "Nee. Watergedragen verf verdun je, als dat al nodig is, met water. Veel producten zijn gebruiksklaar en hoeven niet verdund te worden."),
("Hoe weet ik welke verf er op mijn kozijnen zit?", "Wrijf met een doekje met spiritus over een onopvallende plek. Watergedragen verf wordt zacht of geeft kleur af; alkyd meestal niet."),
("Ruikt watergedragen verf helemaal niet?", "Hij ruikt veel minder, maar niet niets. Ventileer ook bij watergedragen verf tijdens en na het schilderen."),
],
"bronnen": [TDS_PRIMER, TDS_BL_PRIMER, VOS_RICHTLIJN],
"gerelateerd": ["welke-verf-voor-kozijnen", "grondverf-of-voorlak", "latex-of-muurverf"],
},
# ---------------------------------------------------------------------------
{
"slug": "kozijnen-schuren-en-voorbereiden",
"groep": "Voorbereiden en uitvoeren",
"titel": "Kozijnen schuren en voorbereiden voor het schilderen",
"seo_titel": "Kozijnen schuren en voorbereiden: stappenplan",
"description": "Goede voorbereiding bepaalt hoe lang je schilderwerk meegaat. Zo reinig, schraap en schuur je kozijnen, welke korrel je gebruikt en waar je op let bij oude verf.",
"kort": "Reinigen, schrapen, schuren en afplakken: de voorbereiding die bepaalt hoe lang je verf het houdt.",
"foto": "wit-kozijn-afbladderend-oude-gevel",
"intro": "Schilders zeggen het vaak: de voorbereiding is het halve werk. Eerlijker is: het is meer dan de helft. Een dure verf op een slecht voorbereid kozijn bladdert binnen een paar jaar, terwijl een gewone verf op een goed geschuurd en gereinigd kozijn veel langer meegaat. Zo pak je de voorbereiding aan.",
"kort_antwoord": "Eerst reinigen en ontvetten, dan loszittende verf verwijderen, eventuele houtrot herstellen, schuren en stofvrij maken. Kaal hout schuur je met een grovere korrel, intacte verf mat je op met een fijne korrel. Werk bij droog weer, plak het glas af en wees voorzichtig met oude verf in huizen van vóór de jaren zestig: die kan lood bevatten.",
"secties": [
("Waarom voorbereiden zo belangrijk is",
"""<p>Verf moet zich ergens aan vasthouden. Op vuil, vet, losse verf of een glad, glanzend oppervlak lukt dat slecht. Elk technisch blad van een lakverf begint daarom met dezelfde stappen: reinigen, matteren, plaatselijk repareren. Pas daarna komen gronden, voorlakken en aflakken. Sla je die stappen over, dan zit de nieuwe laag vast op iets dat zelf loslaat.</p>"""),
("Eerst reinigen, dan pas schuren",
"""<p>Dat lijkt omgekeerd, maar het klopt: als je eerst schuurt, wrijf je vuil en vet in de geschuurde krassen. Was het kozijn daarom eerst met een ontvetter of een sodaoplossing, spoel na met schoon water en laat het drogen. Fabrikanten noemen hiervoor een eigen reinigingsmiddel, maar het principe is hetzelfde.</p>"""),
("Loszittende verf verwijderen",
"""<p>Schraap alle verf weg die loszit of bladdert, met een driehoekige verfkrabber. Test met tape of verf nog goed hecht: plak een stuk tape op de verf, trek het er met een ruk af, en kijk of er verf aan blijft zitten. Bij grote stukken met veel oude lagen kan een heteluchtföhn helpen. Houd die niet te lang op één plek en blijf uit de buurt van glas, want dat kan door de hitte barsten. Afbranden met een open vlam raden we af: het geeft brandgevaar en schadelijke dampen.</p>"""),
("Let op: oude verf kan lood bevatten",
"""<p>In oude woningen kunnen onder de bovenste lagen nog verflagen met lood zitten. Lood mag al lang niet meer in verf, maar oude lagen blijven zitten. Het risico zit in het stof en de dampen die vrijkomen bij droog schuren en afbranden. De GGD adviseert verf waarover je twijfelt te laten testen. Verf die nog goed zit, kun je overschilderen. Moet slechte verf eraf, houd dan kinderen en zwangeren uit de buurt en maak alles nat schoon in plaats van te vegen of te stofzuigen. Een schilder werkt in zo'n geval nat of met afzuiging.</p>"""),
("Schuren: welke korrel?",
"""<ul>
<li><strong>Kaal hout en oneffenheden:</strong> grof tot middel, ongeveer korrel 80 tot 120. Schuur met de nerf mee.</li>
<li><strong>Randen van oude verf glad maken:</strong> korrel 120 tot 150, zodat er geen trapje zichtbaar blijft.</li>
<li><strong>Intacte verf matteren en tussen de lagen:</strong> fijn, korrel 180 tot 240, of een schuurspons.</li>
</ul>
<p>Fabrikanten geven in een apart schuurschema per laag de juiste korrel. Gebruik schuurpapier voor hout en verf, geen staalwol op hout dat je met watergedragen verf gaat schilderen: achtergebleven staaldeeltjes kunnen gaan roesten.</p>"""),
("Repareren, stofvrij maken en afplakken",
"""<p>Vind je zachte plekken tijdens het schuren, herstel die dan eerst. Hoe dat gaat lees je in <a href="/kennisbank/houtrot-herkennen-en-herstellen/">houtrot herkennen en herstellen</a>. Vul kleine gaatjes en krassen met een plamuur voor buiten. Maak daarna alles stofvrij met een stofdoek of een licht vochtige doek, en plak het glas en het hang- en sluitwerk af. Werk bij droog weer: het hout moet droog zijn en de technische bladen noemen een maximale luchtvochtigheid van 85%. Wanneer het weer goed genoeg is, lees je in <a href="/gids/wanneer-buiten-schilderen/">wanneer kun je buiten schilderen</a>.</p>"""),
],
"stappen": [
("Controleer het kozijn", "Kijk naar losse verf, open naden en zachte plekken. Prik in de onderdorpel en de onderkant van de stijlen."),
("Reinig en ontvet", "Was met een ontvetter of soda, spoel na met water en laat drogen."),
("Schraap losse verf weg", "Verwijder alles wat loszit. Doe de tapetest om te zien of de rest goed hecht."),
("Herstel schade", "Herstel houtrot en vul gaatjes. Laat vullers volgens de verpakking uitharden."),
("Schuur", "Kaal hout grof tot middel, randen glad, intacte verf fijn opmatteren."),
("Maak stofvrij en plak af", "Neem het stof af, plak glas en beslag af en begin bij droog weer met gronden."),
],
"kosten": ["kozijnen-schilderen", "schilder-uurtarief"],
"faq": [
("Moet je kozijnen altijd schuren voor het schilderen?", "Ja. Ook intacte verf moet je opmatteren, anders hecht de nieuwe laag slecht op het gladde oppervlak."),
("Welke schuurkorrel gebruik je voor kozijnen?", "Grof tot middel (ongeveer 80 tot 120) voor kaal hout en oneffenheden, fijn (180 tot 240) om intacte verf op te matteren en tussen de lagen."),
("Moet alle oude verf eraf?", "Nee. Verf die goed hecht mag blijven zitten. Alleen loszittende of bladderende verf moet weg."),
("Is schuren in een oud huis gevaarlijk?", "Het kan, als er loodhoudende verf in de oude lagen zit. Laat het bij twijfel testen, schuur nat of met afzuiging en houd kinderen uit de buurt."),
("Hoeveel tijd kost de voorbereiding?", "Bij oude kozijnen vaak meer dan het schilderen zelf. Dat zie je terug in een offerte: een schilder die weinig tijd voor voorbereiding rekent, slaat misschien stappen over."),
],
"bronnen": [TDS_PRIMER, GGD_LOOD],
"gerelateerd": ["houtrot-herkennen-en-herstellen", "grondverf-of-voorlak", "welke-verf-voor-kozijnen"],
},
# ---------------------------------------------------------------------------
{
"slug": "behang-verwijderen",
"groep": "Voorbereiden en uitvoeren",
"titel": "Behang verwijderen: zo krijg je het van de muur",
"seo_titel": "Behang verwijderen: snel en zonder schade",
"description": "Papier, vinyl, vlies of glasvezel: per soort behang de beste manier om het te verwijderen, met stappenplan, en wat je daarna met de muur doet.",
"kort": "Per soort behang de beste aanpak: inweken, stomen of droog aftrekken, en de wand daarna klaarmaken.",
"foto": "structuurbehang-witte-wand",
"intro": "Wie een kamer opknapt, begint vaak met het oude behang. Soms komt het er in lange banen af, soms zit je dagen te krabben. Het verschil zit vooral in het soort behang en de ondergrond. Met de juiste aanpak voorkom je dat je het stucwerk of de gipsplaat eronder beschadigt.",
"kort_antwoord": "Vliesbehang kun je vaak droog in banen aftrekken. Papierbehang week je los met warm water en een beetje afwasmiddel of een behangafweker, en schraap je daarna weg. Bij vinyl trek je eerst de toplaag eraf. Lastige lagen gaan het best met een behangstomer. Wees voorzichtig op gipsplaat: die beschadigt snel bij te veel water of stoom.",
"secties": [
("Welk behang zit er op je muur?",
"""<p>Kijk eerst wat voor behang het is, want dat bepaalt de aanpak:</p>
<ul>
<li><strong>Vliesbehang:</strong> stevig en papierachtig, vaak in de laatste twintig jaar geplakt. Is gemaakt om droog te verwijderen. Probeer een hoek los te maken en trek: komt de baan heel mee, dan heb je geluk.</li>
<li><strong>Papierbehang:</strong> dun en scheurt makkelijk. Moet worden ingeweekt.</li>
<li><strong>Vinylbehang:</strong> heeft een kunststof toplaag die water tegenhoudt. De toplaag trek je eraf, het papier eronder week je in.</li>
<li><strong>Structuurbehang en glasvezelbehang:</strong> vaak overgeschilderd, waardoor water er niet in komt. Dat is het meeste werk; een stomer is dan bijna onmisbaar.</li>
</ul>"""),
("Wat zit eronder?",
"""<p>Klop op de muur. Klinkt hij hol, dan is het waarschijnlijk gipsplaat. Daar zit een kartonlaag op die loslaat als hij te nat wordt of als je te hard schraapt. Werk op gipsplaat dus met weinig water, kort stomen en een breed plamuurmes dat je vlak houdt. Op gestuct metselwerk kun je meer water gebruiken, maar ook daar maak je met een scherpe krabber snel krassen die je later moet vullen.</p>"""),
("Gereedschap",
"""<ul class="checklist">
<li>Afdekfolie of stucloper voor de vloer en afplakband</li>
<li>Een spons, een plantenspuit of een verfroller voor het water</li>
<li>Warm water met een scheutje afwasmiddel, of behangafweker uit de bouwmarkt</li>
<li>Een breed plamuurmes en een behangkrabber</li>
<li>Een perforatieroller (egel) voor vinyl en overgeschilderd behang</li>
<li>Eventueel een behangstomer, die je bij veel bouwmarkten kunt huren</li>
</ul>"""),
("Na het verwijderen: de muur klaarmaken",
"""<p>Als het behang eraf is, zitten er meestal nog lijmresten op de wand. Was die weg met warm water en een spons, anders laat nieuwe verf of nieuw behang plaatselijk los. Laat de muur goed drogen, ten minste een dag. Vul gaten en beschadigingen, schuur ze glad en controleer met strijklicht of de wand vlak genoeg is.</p>
<p>Ga je schilderen, dan heeft een wand waar behang op zat bijna altijd een voorstrijk nodig: reparaties en kale plekken zuigen anders verf op, en dat zie je als vlekken. Het technische blad van een muurverf schrijft voor gaten op te vullen, glad te schuren, de ondergrond te reinigen en bij gladde ondergronden een voorstrijklaag aan te brengen. Welke verf je dan kiest, lees je in <a href="/kennisbank/latex-of-muurverf/">latex of muurverf</a>.</p>"""),
("Laten doen en de btw",
"""<p>Behang verwijderen is tijdrovend werk dat een schilder of behanger meestal per uur of per vierkante meter rekent. Laat je ook opnieuw behangen, dan valt het behangen zelf bij een woning ouder dan twee jaar onder 9% btw, maar de levering van het behang onder 21%. Een nette offerte splitst die twee. Meer daarover in de gids <a href="/gids/btw-schilderwerk/">btw op schilderwerk</a>.</p>"""),
],
"stappen": [
("Maak de ruimte klaar", "Haal meubels weg, dek de vloer af en schakel de stroom uit voordat je afdekplaatjes van stopcontacten en schakelaars losschroeft."),
("Test een hoek", "Probeer een baan droog los te trekken. Lukt dat, dan is het vlies en ben je snel klaar."),
("Perforeer en week in", "Rol bij vinyl of overgeschilderd behang eerst met een perforatieroller. Maak het behang daarna royaal nat en laat het een kwartier inweken."),
("Schraap het los", "Duw het plamuurmes vlak onder het behang en werk van onder naar boven. Maak hardnekkige plekken opnieuw nat of gebruik de stomer."),
("Was de lijmresten weg", "Neem de wand af met warm water en een spons tot hij niet meer plakt, en laat hem drogen."),
("Herstel en voorstrijk", "Vul gaten, schuur glad en zet een voorstrijk voordat je schildert of opnieuw behangt."),
],
"kosten": ["schilderen-per-m2", "schilder-uurtarief"],
"dienst": "behangen",
"faq": [
("Hoe krijg je oud behang er makkelijk af?", "Week papierbehang goed in met warm water en wat afwasmiddel of behangafweker en geef het tijd. Bij vinyl en overgeschilderd behang eerst perforeren, of een stomer gebruiken."),
("Kun je over oud behang heen schilderen?", "Soms, als het behang overal goed vastzit en geschikt is om te overschilderen, zoals glasvezel- of structuurbehang. Op papierbehang met naden die loslaten wordt het resultaat slecht."),
("Hoe verwijder je behang van gipsplaat?", "Met weinig water of kort stomen, en een breed plamuurmes dat je vlak houdt. De kartonlaag van gipsplaat beschadigt snel."),
("Hoe lang moet de muur drogen na het verwijderen van behang?", "Minstens een dag, en langer als de wand erg nat is geworden. Schilder of behang niet op een vochtige muur."),
("Wat kost behang laten verwijderen?", "Een schilder rekent het meestal per uur of per vierkante meter, afhankelijk van het soort behang. De richtprijzen staan hieronder."),
],
"bronnen": [TDS_MUURVERF, BELASTINGDIENST],
"gerelateerd": ["latex-of-muurverf", "plafond-schilderen-zonder-strepen", "goede-offerte-schilderwerk"],
},
# ---------------------------------------------------------------------------
{
"slug": "verfschade-en-garantie",
"groep": "Schade en onderhoud",
"titel": "Verfschade en garantie: wat zijn je rechten?",
"seo_titel": "Verfschade en garantie op schilderwerk",
"description": "Bladderende verf, blazen of verkleuring na het schilderen? Zo herken je de oorzaak, wat garantie op schilderwerk dekt en hoe je een klacht netjes regelt.",
"kort": "De bekendste verfschade en de oorzaak, wat garantie dekt en hoe je een klacht aanpakt.",
"foto": "verweerde-blauwe-houten-schutting",
"intro": "Je hebt je huis laten schilderen en na een tijd zie je blazen, bladders of verkleuring. Is dat de schuld van de schilder, van het weer, of van de staat van het hout? En wat kun je dan doen? Hier lees je hoe je de bekendste verfschade herkent, wat garantie wel en niet dekt en hoe je een klacht netjes regelt.",
"kort_antwoord": "Een schilder moet het werk goed en vakkundig uitvoeren; dat staat los van een garantietermijn. Zie je kort na het schilderen schade die door het werk komt, meld het dan zo snel mogelijk schriftelijk met foto's en geef de schilder de kans het te herstellen. Een schriftelijke garantie geeft daarbovenop extra zekerheid, maar dekt meestal niet alles: normale veroudering, mechanische schade en problemen door achterstallig onderhoud vallen er vaak buiten.",
"secties": [
("Veelvoorkomende verfschade en de oorzaak",
"""<div class="tablewrap"><table>
<thead><tr><th>Schade</th><th>Hoe het eruitziet</th><th>Mogelijke oorzaak</th></tr></thead>
<tbody>
<tr><td>Bladderen</td><td>Verf laat in schilfers los</td><td>Vocht achter de verf, slecht gereinigd of niet geschuurd, oude losse lagen niet verwijderd</td></tr>
<tr><td>Blaasvorming</td><td>Bobbels in de verflaag</td><td>Vocht of hars in het hout, schilderen in de volle zon of op een te vochtige ondergrond, open poriën</td></tr>
<tr><td>Doorbloeden</td><td>Bruine of gele vlekken door de verf</td><td>Inhoudsstoffen uit hout, kwasten in grenen, geen isolerende grondverf</td></tr>
<tr><td>Craquelé</td><td>Fijne scheurtjes als een netwerk</td><td>Te dikke lagen, een harde laag op een zachte, of te snel overschilderd</td></tr>
<tr><td>Lopers en zakkers</td><td>Druppels of gordijnen in de verf</td><td>Te veel verf in één keer</td></tr>
<tr><td>Doffe of plakkerige verf</td><td>Glans verdwijnt of verf blijft kleven</td><td>Schilderen bij te hoge luchtvochtigheid of dauw, of weekmakers in tochtprofielen bij watergedragen verf</td></tr>
</tbody></table></div>
<p>Technische bladen leggen grenzen vast waarbinnen een verf mag worden verwerkt, zoals een maximale luchtvochtigheid van 85% en een ondergrond die minstens 3 °C warmer is dan het dauwpunt. Schade die kort na het schilderen ontstaat, heeft vaak te maken met een van die omstandigheden of met de voorbereiding. Zie ook <a href="/kennisbank/kozijnen-schuren-en-voorbereiden/">kozijnen schuren en voorbereiden</a>.</p>"""),
("Je rechten: goed werk is de basis",
"""<p>Als je een schilder inhuurt, sluit je juridisch een overeenkomst van <em>aanneming van werk</em>. Die is geregeld in Boek 7 van het Burgerlijk Wetboek. De kern: de schilder moet het werk goed en volgens de afspraken uitvoeren. Is het werk gebrekkig, dan kun je hem vragen het te herstellen. Doe dat binnen redelijke tijd nadat je het gebrek ontdekt; wie lang wacht, verzwakt zijn positie.</p>
<p>Een garantie is een extra belofte van de schilder, bovenop wat de wet al regelt. De duur en de voorwaarden verschillen per bedrijf. Laat de garantie daarom altijd op papier zetten, in de offerte of de opdrachtbevestiging.</p>"""),
("Wat dekt garantie meestal niet?",
"""<ul>
<li>Normale veroudering en verkleuring van verf door zon en weer.</li>
<li>Schade door stoten, krassen of verkeerd schoonmaken.</li>
<li>Houtrot of vocht in delen die niet zijn hersteld, bijvoorbeeld omdat je dat niet wilde laten doen.</li>
<li>Problemen door constructiefouten, lekkages of een kapotte dakgoot.</li>
<li>Werk dat later door iemand anders is aangepast of overgeschilderd.</li>
</ul>
<p>Vraag vooraf wat de garantie precies dekt, hoe lang, en of er onderhoud van je verwacht wordt, zoals jaarlijks reinigen.</p>"""),
("Ben je lid van een brancheorganisatie?",
"""<p>Is de schilder aangesloten bij een brancheorganisatie of een geschillencommissie, dan kun je daar terecht als je er samen niet uitkomt. Vraag hier vooraf naar. De Consumentenbond adviseert bij een klacht over een dienst om schade vast te leggen met foto's, de afspraken en voorwaarden na te lezen en de dienstverlener eerst zelf de kans te geven het op te lossen.</p>"""),
],
"stappen": [
("Leg de schade vast", "Maak foto's met datum, van dichtbij en van een afstand, en noteer wanneer je het voor het eerst zag."),
("Lees de afspraken na", "Pak de offerte, opdrachtbevestiging en voorwaarden erbij: wat was er afgesproken over verf, lagen en garantie?"),
("Meld het schriftelijk", "Stuur de schilder een e-mail of brief met de foto's en een duidelijke omschrijving. Bel gerust, maar zet het daarna op papier."),
("Geef een redelijke termijn", "Vraag de schilder het te herstellen binnen een redelijke termijn, bijvoorbeeld enkele weken, afhankelijk van het weer."),
("Escaleer als het nodig is", "Komt er geen oplossing, stuur dan een ingebrekestelling en kijk of de schilder bij een geschillencommissie is aangesloten. Laat herstel niet door een ander doen voordat dit is afgerond."),
],
"kosten": ["huis-schilderen", "kozijnen-schilderen"],
"faq": [
("Hoe lang garantie krijg je op schilderwerk?", "Dat verschilt per schilder en per soort werk. Laat de duur en de voorwaarden in de offerte zetten. Los daarvan moet het werk altijd vakkundig zijn uitgevoerd."),
("De verf bladdert na een jaar. Wat nu?", "Leg het vast met foto's en meld het schriftelijk bij de schilder. Bladderen zo kort na het schilderen wijst vaak op een probleem met voorbereiding of omstandigheden tijdens het werk."),
("Mag ik een deel van de rekening inhouden?", "Bij een gebrek mag je soms een deel inhouden dat in verhouding staat tot wat er mis is. Meld dat schriftelijk. Houd niet meer in dan redelijk is."),
("Valt houtrot onder de garantie?", "Meestal alleen als de schilder de houtrot heeft hersteld en die reparatie faalt. Houtrot in delen die niet zijn behandeld, valt er doorgaans buiten."),
("Wat als de schilder niet reageert?", "Stuur een ingebrekestelling met een redelijke termijn. Is hij aangesloten bij een geschillencommissie, dan kun je daar een klacht indienen."),
],
"bronnen": [BW7, CONSUMENTENBOND, TDS_PRIMER],
"gerelateerd": ["goede-offerte-schilderwerk", "kozijnen-schuren-en-voorbereiden", "houtrot-herkennen-en-herstellen"],
},
# ---------------------------------------------------------------------------
{
"slug": "goede-offerte-schilderwerk",
"groep": "Offerte, kosten en btw",
"titel": "Wat staat er in een goede offerte voor schilderwerk?",
"seo_titel": "Goede offerte schilderwerk: checklist van 12 punten",
"description": "Waar herken je een goede schildersofferte aan? Checklist met 12 punten: omschrijving, verf en lagen, voorbereiding, btw, meerwerk, planning, betaling en garantie.",
"kort": "Een checklist van twaalf punten om een schildersofferte te beoordelen en offertes eerlijk te vergelijken.",
"foto": "villa-in-de-steigers-achtergevel-elburg",
"intro": "Twee offertes voor dezelfde klus kunnen honderden euro's uit elkaar liggen. Vaak zit het verschil niet in de prijs per uur, maar in wat er wel en niet in staat. Een goede offerte maakt precies duidelijk wat je krijgt. Met deze checklist beoordeel je een offerte en vergelijk je er meerdere op dezelfde basis.",
"kort_antwoord": "Een goede offerte omschrijft per onderdeel wat er gebeurt, met hoeveelheden, de voorbereiding, het verfmerk en type, het aantal lagen, de btw per post, afspraken over meerwerk zoals houtrot, de planning, de betaling en de garantie. Hoe vager de offerte, hoe groter de kans op discussie achteraf.",
"secties": [
("De checklist",
"""<ol>
<li><strong>Bedrijfsgegevens.</strong> Naam, adres, KvK-nummer en btw-nummer. Zo weet je met wie je zaken doet.</li>
<li><strong>Omschrijving per onderdeel.</strong> Niet alleen "buitenschilderwerk", maar kozijnen, deuren, boeidelen, dakkapel, elk apart.</li>
<li><strong>Hoeveelheden.</strong> Aantal kozijnen en deuren, of vierkante meters muur en plafond. Dan kun je offertes vergelijken.</li>
<li><strong>Voorbereiding.</strong> Reinigen, schuren, losse verf verwijderen, plamuren, kitten. Dit is het grootste deel van het werk.</li>
<li><strong>Verf.</strong> Merk, type, glansgraad en kleur. "Eerste kwaliteit verf" zegt niets.</li>
<li><strong>Aantal lagen.</strong> Bijvoorbeeld kale plekken gronden, voorlakken en één of twee lagen aflak.</li>
<li><strong>Houtrot en meerwerk.</strong> Een prijs per reparatieplek of inzetstuk, of een stelpost, en hoe meerwerk wordt afgesproken.</li>
<li><strong>Steiger of hoogwerker.</strong> Zit die erin, en wie regelt een eventuele vergunning?</li>
<li><strong>Btw per post.</strong> 9% voor schilderwerk aan een woning ouder dan twee jaar, 21% voor bijvoorbeeld nieuw hout of de levering van behang.</li>
<li><strong>Planning.</strong> Een startweek, de duur en wat er gebeurt bij slecht weer.</li>
<li><strong>Betaling.</strong> Termijnen en wanneer je betaalt. Wees voorzichtig met een hoge aanbetaling vooraf.</li>
<li><strong>Garantie en voorwaarden.</strong> Hoe lang, wat het dekt, en welke algemene voorwaarden gelden.</li>
</ol>"""),
("Let op deze signalen",
"""<ul>
<li>Eén totaalbedrag zonder uitsplitsing.</li>
<li>Geen enkele vermelding van voorbereiding of van het aantal lagen.</li>
<li>21% btw over schilderwerk aan je woning, terwijl die ouder is dan twee jaar.</li>
<li>Een grote aanbetaling voordat er iets is gebeurd.</li>
<li>Druk om snel te tekenen, bijvoorbeeld met een korting die "alleen vandaag" geldt.</li>
<li>Geen enkele afspraak over houtrot, terwijl je huis oud houtwerk heeft.</li>
</ul>
<p>Dat hoeft niet te betekenen dat de schilder onbetrouwbaar is. Het betekent wel dat je moet doorvragen voordat je tekent.</p>"""),
("Offertes eerlijk vergelijken",
"""<p>Vergelijk offertes op dezelfde basis: zelfde onderdelen, zelfde hoeveelheden, inclusief of exclusief btw. Een goedkope offerte zonder houtrotherstel kan uiteindelijk duurder uitvallen dan een duurdere waarin het al is meegenomen. Leg de bedragen naast de richtprijzen op <a href="/kosten/">wat kost schilderwerk per klus</a>, of <a href="/offerte-vergelijken/">laat je offerte gratis checken</a>.</p>"""),
("Btw: het meest gemaakte foutje",
"""<p>Voor schilderwerk aan een woning die ouder is dan twee jaar geldt het lage tarief van 9%, ook over de verf die de schilder gebruikt. Voor nieuw hout, zoals inzetstukken en nieuwe onderdorpels, en voor de levering van behang geldt 21%. Een offerte die schilderwerk en ander werk combineert, hoort die posten te splitsen. Alle regels staan in <a href="/gids/btw-schilderwerk/">btw op schilderwerk</a>.</p>"""),
("Na het tekenen",
"""<p>Bewaar de getekende offerte goed. Als er tijdens het werk iets bijkomt, zoals meer houtrot dan verwacht, spreek het meerwerk dan vooraf af, met een prijs, en laat het per e-mail bevestigen. Bij de oplevering loop je het werk samen na. Ontdek je later een gebrek, lees dan <a href="/kennisbank/verfschade-en-garantie/">verfschade en garantie</a>.</p>"""),
],
"stappen": [
("Vraag meerdere offertes aan", "Drie offertes geven een goed beeld van de prijs en van de aanpak van verschillende schilders."),
("Geef iedereen dezelfde informatie", "Zelfde onderdelen, zelfde wensen voor kleur en glans. Anders vergelijk je appels met peren."),
("Loop de checklist langs", "Streep per offerte de twaalf punten af en noteer wat ontbreekt."),
("Vraag door", "Vraag naar ontbrekende punten, zoals het aantal lagen of de prijs per houtrotplek."),
("Vergelijk op dezelfde basis", "Zet de bedragen naast elkaar, inclusief btw en inclusief een redelijke inschatting van meerwerk."),
("Leg afspraken vast", "Laat mondelinge afspraken toevoegen aan de offerte voordat je tekent."),
],
"kosten": ["huis-schilderen", "schilder-uurtarief", "kozijnen-schilderen"],
"faq": [
("Wat moet er minimaal in een schildersofferte staan?", "Wie de schilder is, wat er per onderdeel gebeurt, de voorbereiding, de verf en het aantal lagen, de prijs met btw per post, de planning, de betaling en de garantie."),
("Is een offerte bindend?", "Een offerte is een aanbod. Teken je hem, dan is er een overeenkomst. Lees daarom ook de algemene voorwaarden die erbij horen."),
("Hoeveel aanbetaling is normaal bij een schilder?", "Veel schilders vragen geen of een kleine aanbetaling en factureren na afloop of in termijnen. Wees voorzichtig met een hoge aanbetaling voordat het werk begint."),
("Wat is een stelpost?", "Een geschat bedrag voor werk dat vooraf niet precies bekend is, zoals houtrotherstel. Achteraf wordt afgerekend wat het werkelijk kostte."),
("Waarom verschillen offertes zo veel?", "Door verschillen in voorbereiding, het aantal lagen, de verf, houtrotherstel, de steiger en de drukte van de schilder. Vergelijk daarom op inhoud, niet alleen op het eindbedrag."),
],
"bronnen": [BELASTINGDIENST, CONSUMENTENBOND],
"gerelateerd": ["verfschade-en-garantie", "houtrot-herkennen-en-herstellen", "kozijnen-schuren-en-voorbereiden"],
},
]
